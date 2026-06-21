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
<img src="https://cdn4.telesco.pe/file/TfG8o_W9IfclDPleEO-4ejekbKIYpX8B00-ZtJIb58rp4nU1iSdo4VZtTcpklMmJ3G40I9MxtbM3VciKzcqkRDp_8SXH7YPi_OvDIDEfGhjHbx1SeEk-5m2pGINV9QkDbFSse6-knTSFaQjIrYut5GFusD-Tul-2oWabVzoe7Hy28l-APUx9NNEi0_ez-NGIFkxq2ST8Gm6Ohmaokl-Jxf-YkwD9aa_ULUVJZadh4qVUY5ZmwvVAyWfn4OeIg2cBv7KsmSqLiqdSil05pAvHLJ_AAvM5FHew-tqyy-48GCwjpQJ2XNk-Bl9znU8tP9GJ_Gy276nv3o9yYNg-OLgCPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.64K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTS46cPR4UyI8m6mShwmcnKJ7B7vpaWklTBQv6RPEwXK8Fbdrrv4zrZs3QuvVUQghrLMSKSlOgw-5_6VjjsupPFHIfAUPQfTziKnpmV9j9epC5S7ZK0KVPrzexpub6YQhbdVFCA2vUg_MDMnYLEyvl8myRIeGMHaaojuUvHRBhi8RGBZeSd8cgZeICeMuw8ktZEqH85BKFemFQ-2vLL6oPOad5WkRx7M2m2p0MfarJnNMn3acWllXkV7iVvErUqq84vbIPdmjPkkaBGIvLlBQ18vfj898EMinz6dWIq-bdqBhnJYxDdys3OO8zIdH9Y0q4t1PAFA18frsRkALU1qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 646 · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 883 · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcwxwAus3AoD1ZcbNJInBM0TjQ7GPB_YufaItVQgiac5n1RC-aXj9pIax0CXIknl9n28YQSNIkAVnx49YebQjr16uIh-cpxLcQ8rk_4OhCzEVxMoU0Bv9SxCKz-GI9r_0kpCH1U4DaN1Go81Gr4UOfPdtJg45_Ldxl7rpy6r-VsV5OGQD0FVqZvUoZTS8J3_E9a7uMWdeNSRG8LldTVNydHigroP3QpbSds5pmyOvjwlhDtq_qd4xWJDaJi9Mjqt3RTMT0d9_VNxrLiPY3aV1GciO5VXswSIbvAYpBTjdqgD-8Nq_Rya90wMM3zE1c1W6B98tzqJESt1wwS8l6hnCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsSjzvj7fCgxWibz3cu0cSdhiGxzH3Lvv1A1mn5gd4QSQGihPsyPJ3peEWwYuyzc3y5BfbmCLKa7XWE-ge3pInjKwusuUrMbRiUJCvdq9Ey0wPuBhmiIoVUySLdbSz6Q_DMaG7CdhXNZOfQub5XGrQzfbV-WOBa4B9CNkfOlQAWsdChKeJdJMIxuIQ1m3j0bfo7nFErJIKHGsU0Mo5x0ujZzr2wYhqGQNxqb3KsocKYTpjhIoBPZGRmk6BaY17Tg1JS43Bf_sQMeOiD2duuZcxfyQBDRCx05aPV2-bbZK3PsvSt9D5Tt2bNTdPrbHrxj3FzE6G0NRJlCJm2Tt7avEw.jpg" alt="photo" loading="lazy"/></div>
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
🏞️
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8o_R3jogyF990u7hvY3uMXuOUdwAmm02XAm7WUbaf7Kx4-KhL3wBCLBdoxff_zPmhz6-AaJEm4UmxYZTrTPp2T06VmTeuEB-fBisaxfTXiCtsMbGbuz6sB2lw1CZzAwBH5U4v2QXd0uP_hsIdZuKJptWzHUGvJZ12S80rT5PhHNiSFPHFc4T4Pe3GlkgkfyPudUWc6ePnJDH14Pfp1TBepU3rJvUzwr3QXfLnurj1j0Gvs1YV0ikT6jcy01pTTktAVm8CJaVpNozji-kjPXUHZvbsQTchAPbD6WxGYSjBH2T9ikRMXKUFhDT_7MUsEJ07obt4moasFUYsnO61vS5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=ouuvnu5K3GNIhmUlPtfX8-WHHBXUkmZKvjo_X5ee12x__--nahLPwuNzm7BTu_somHgvOA_WMPk8OcLXvP-7pRfV0xdlf506RgI1AWCKIbDDYPh4AdilYFZlgMhp1eOJgbdEA0L0Sj-FPKdi_T6_0Qci5UzijoLCgNzElTPKXC9zVwt_7o6bXqJ4ox2wuJJSHuMZPlm8WC-eDdG_w6KFqKWHGXFWztqSy2SZy1yHpGLl29fYgmok4YNdJUoIq9LkjnJhv-PUItXsAhCPLX4xFUuxrBBtObU3Jz4QJuWBn8NAnwE_yF4P5RDLTrl6BzYNt1vNrz202_bN_e2luQYyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=ouuvnu5K3GNIhmUlPtfX8-WHHBXUkmZKvjo_X5ee12x__--nahLPwuNzm7BTu_somHgvOA_WMPk8OcLXvP-7pRfV0xdlf506RgI1AWCKIbDDYPh4AdilYFZlgMhp1eOJgbdEA0L0Sj-FPKdi_T6_0Qci5UzijoLCgNzElTPKXC9zVwt_7o6bXqJ4ox2wuJJSHuMZPlm8WC-eDdG_w6KFqKWHGXFWztqSy2SZy1yHpGLl29fYgmok4YNdJUoIq9LkjnJhv-PUItXsAhCPLX4xFUuxrBBtObU3Jz4QJuWBn8NAnwE_yF4P5RDLTrl6BzYNt1vNrz202_bN_e2luQYyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡
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
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbcxoqvEQp2cjCEb6Ebm3xndQwdjQ1ElFTpIK-IWUeDbJ75oFYgaCpEuQ3S1abSC2r69FyfvWMZCRz6QvNUhcBnxycBK08lDPap6GSBaE1YO8YUXA4ZA_igdcpI_xgbb__Cg4m-A4NWa1yl2jfvkcBObygXAEmu8ML43J51fqkKIibJC6sAZ650ns-HlV7z8HxrPOk5pcklUK5s8EIo6NhdlYmdtqfuOh4yDEq-Bhw0_mS6EPmRUqHQhoE_ONyRdmZwliS2LVs9sNexLSe4TRaMsdKA2R7IvxaNtBoeIexWHFVNPDtU4Fi6_DLPsSn7wj-oO7qlLTi-919hNtpNJSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqHhYqp8GPjPznZGx-TxAKRlarsSk972CGn2rTXabE5TeFu9UELoKnGW7LZ9gmvAin0pgZq8Gcj2AFSlz4fkXv7LPsYrfCG_lHJpt9B0dWJ5IWSXXEtKNQ1Mcv8XaixN8zvLMLkaIx16Hh9qp1n5DaXx-Jax2wmvNOahnMycRkwsInMsL-hV8bUsnvQkmTGuXqlo1C_nl2gflgQuyNC8UvS3zHPXHEleZCEbqK1wU3ne5Tg1XhOT1knRNoyG4EMxx3GVkxFHC-oQAKHRSx7VEuI21fT-3H-rOMHIIk7nS6EP1yJE8AnzHIZjmtdEYAWWY7sE7J1JLQaP7L-6SDuQSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJtdMoXGHHuFJ_Yh7pwekZKqrz2ZVpQSGqiU21jZTjprLWghkXz_aJ4CLIzMbNFo9_KQkf4lEhoPjZdw-Dqh_yCSt24TuE-99K2AQABrr5fuvpGPTNND3hp2J4xtVriBfYfJJ0A5Bwl-5Zizc6yC-qMpveW9LGxPTjMzGr-jSDY93VgJmd8dHtB9ydzYtdWraL9qbStWrIvlvaviWD3JRjqf3xXt4Bmi97-obYDuAY5ivzzKt7OuHiGri24r5CAcqU-hFHiIMQDX5MN_0Yfb7-9WGXtjJxITfMAu6TJyeUbIS4nHaazP4m3X80yr2Vzb3bB780BhL4fF_7SHg_hoWQ.jpg" alt="photo" loading="lazy"/></div>
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
⚡
قابل استفاده رایگان در AI Studio
•
🗂️
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6btOjLkSAaClp00KRUN24BneyW2POwPpz2OLa2GlhozJyu4UKrnN5ruBnxKoeVXOSRoHOMgPQahE-euJHZZp3S6oDbpj8vRdiBUabftGewDxYLyPxmQXfWDccahIZEm9pPWvt-9rogEuKW6rYq5uVSbWp-naZAyV7lSd-yyPOO1mWGXZ9FQO5Q07mtS2tQr9Mav7jsJQ675ozSkf2auQXpUSALmUof-Qo1d-QWyarF5RYPBf-Neb7EUgxmEqjgKFVhYMR6EwtNxtQSd9MTJ2mfG4UffZflFlyg8TV2XdM69BY7S7mAxs2hKodlzC2oMh5lbsEpRW2wQEsbXaikF3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXg-VG0bxHgmqONOU4Qn26aWCazHRq-NSk2a1UhzGkYvUmC7HRbYWvZbnE17g-mA6gl6krb-wBflQ-8oCd2qci_q4_dY3bJUQ4LraETm1A_WgxxgaeAnxSuK-xD8Msmp4Jj-8C0s-TlsbfJyi-zOlyEh4onrT-DnX-mM-Dy18GXO8eBFOqWHk4XleiY0iwNma3pPNCTbUef0oLWcL7WCe8hR6TS-albQ7tCatZZX5WBOpsRh8nA3HD7YyVGBHHOZ2G5IOlyjcRkTGADMCCZcY41dnQdP5ikvupsaz5KQaHh5Bi4FoMNd39TkPzLsGqY4XElg162Kq3Y1YsPw-w_q3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKmjxKQp8SpduoocbHU86qsi0Uw5E5H9N1I2so4NbS0Tm8Zf8Y_J2wFsEXTv9oO8b7eQCly-OI5sGbY4YkUoFIe8RJpEZwmZ-7hA1MITix5CZXqTrDy56OII_9dGbyCP3HSCAlsGQdrBk3L9soNeWbpmFar23Wsdz6NymMmp_iedb5zwZqBjvnIQinos_LYvvJgvrTMS5ipM8_Y8dHJlBV8a7fAyrVr94bQr3qVc_970_EXMnpiswTxxWIKyiQ5Pl17V3Dqv4xJxF5CtmtYfxoCoowOoXD0lPU8u-6Cpk7uKpIZvLnJnxWplScT0NbmqcVGDHdIR8ScWSUkpXLEuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmVxAdtNKrUESIbOzMOlkhFAKdG2CgRnS3xaZdeqqJnnvs5UBFUbb6SP9-WnhwiCKsCoYrMbdBpwiwh1RzbR8EFI5wfOE0ASilntlozBfI-pJqgnhQou692Pz4vtJO8IpPeMgm86yeLLkqjB2ge5p4Ko070bin6FtCL0cMwUj1XpSMExAehtZVGv4mSGRIUINo6fOx2XzQ5zHWj12YhW3BgnKYr0JbsiLktkcXPVcCwsvLu5RjSEtsxZRDSr-vfpgpivFkqIxmZ29nphck8_k-kXSBo1XkIFf4GbamUz8E8mcxaPXPTWxZLIAPRWb9USNBT9oX92dtxRaLfjJvbxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBHEfkSN0jTILqY0Srwstp729RpK03YsCeyb214g4EzIT1hk7PIbkLYv98Yh9aaBH0hTtBgZW8bDR226tjF-3uK7UMQrZfrE9K47le2oyf4JkXHH_4okGqB58oK9E0AP1_gP3CDzMALL0T55tLaj9s_DrSe65VEbLC38gPluIhVfDsyTwcDxJ6zHhZoy1z9lJyTU50pfnj5fFJr-z263wwa8AZ1OFK1o2ykiZutHgxG1nayqptBbuHl34Uzss47M6TGwm_N0y_JlNIIsHKZE4yxYqJJ0VwZn38Z8h-03cbuFlk9cz1jk55R2mew8ishVHCGP_Rhqn5MTQ2UCG7xTKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWxrrn1E5x8NxWisWPPEuw8qyYlJLSK8dVXU_Kc6MmNUjVsaV2K4iNDLns8jIDHhnayu_OzNOYf9LuhCQVMtpPGmv7D-xBOp30VWOdAaypXmcXlKvow4g370bQhXpIRpOTEAqJw3sip1wBGcsnm-46pIxEkU2RkTYLUGrBO07yvFqZhcyylga8_lwzLb8cXbbGOzOmPQLTRpfDpbEMZeJyZ891ka1JicNn_g3gYU91N8N1QLuN5MUravqw1sAAHKSNcGHkHibLHQX6l4ZiK74VSTSZsnaG67nIGjahIwO2RWicvAp8G8-slSZEersRF94V15jKrdM-qLSAHE9RlQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9L-7_aIfR1QlC8ux8yQJ_euPqRuhfycn1-yxD5PkG4KI2gRapai38p_WEIIEa0tBlgFgJCBLQDF71yFT_LcEzevDnma0Zvbu1X7B53--Uvb7rxGlx6uY3QdxH87nay9eNXjQfUU8CJeIzXIOw_D6gqf3xMLikESFiPPfgHrXCGwNcGIUzWZQzCXhNrWSHE1tphWTgbmOoaR7EAgVCsEqnRUdjyGArwvTXjXijWjnB26kYljgjSkwc8DOxFdZyB46Y5uZyTT2Ffx9JOOy3DYIKz2zrMpHwofbIwdk0dwDvSPlKmq_06aFe2fzCOV5Vexg20rlAKfTnTX9f-4DeWfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvXCJ8VTEQ9ZJ4keQZtZR2aZYEFWdI75N9Pyqw-LSGBaga6NrsLHDdl-aPEiOo7goU2jibpAOHPYXUUlBUbwHhUO4HqMpDh1MG4xNaBsHeMVENRBNm4fTLWB3utX8lpz5xZ7pYepqvmCnNo_lSGuRrPH_IaeTkHLM2eSZk8SMXBI-PZWDZnPLxK16SGJ_CaASpOldQiTONmLXAhBxGfbW4EB3CRgza36zqJJ8Cm-M0QSlO8nMXjozKvmFmgPyrdimrPlLxP5vcKITCLDsCMsOg1gVHFwamlmBSe14LSpkgW7hsff04n8ldI_XTnrE17gOrSZsKb0QvHbzHjs7UG4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_rSRBNYQ0ZyxLrfsGpDarhZv6MSoFv3WqPW9TP9jMzKTg_g-YBDuoaSsrcsrN39v7z9n_s9LTnbvjKR5CbG__-BhWzwk7Zr_MzbpnzMD1Le0J2bkEkzwKj3989ou0jm2EluGLM4kavNSEw8CaIdzIEGYmIZAdKa_9FqxxTs4zeYmJsNl7Is4zie3pKjOpR2wcqnX2RyX6cYwh_mKSJIhf4-_fFfFRTld-xAiJ_OzII6Qzrj50waR_MiPZ6WEQARYM9I7sV3y2M3R_3sgHEMsMFdrEI5GdZTvSd7y2ptd4wLjfSNM44wdtsI5gsyJ-yeMfvZz_RqYJ2u4q1wGWSpGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=pCBCo9NnzV0W4tUse9BCRdDS_UYD6ur4h0_VgJZ_6zNxOFjgtJYhi9mln3rHtICPSrvvgL7ccw8zni-NgyhVwCp2q9JwD90jRNEs_7KVC7CX4NU85tQ9R_izqwW5V0RT2CIXaVoaTVVhvZgpPhSX8-WIJa991kQfCXK6hm4RKDqPobLxOefjTNwCRngNgHB_f1hyyACL0wVlKORQlEUzYEBP8uT6XbeAdREIal_3tqr8628P9h9FHbodwjXxsmj-ISF6pUeDXwuwONUWWFC-pszgjX0d56NV094CmrqxzPeTEa1HIfdRhQKEC2KonEXN-tHtA8HUX25ZF76sFyiiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=pCBCo9NnzV0W4tUse9BCRdDS_UYD6ur4h0_VgJZ_6zNxOFjgtJYhi9mln3rHtICPSrvvgL7ccw8zni-NgyhVwCp2q9JwD90jRNEs_7KVC7CX4NU85tQ9R_izqwW5V0RT2CIXaVoaTVVhvZgpPhSX8-WIJa991kQfCXK6hm4RKDqPobLxOefjTNwCRngNgHB_f1hyyACL0wVlKORQlEUzYEBP8uT6XbeAdREIal_3tqr8628P9h9FHbodwjXxsmj-ISF6pUeDXwuwONUWWFC-pszgjX0d56NV094CmrqxzPeTEa1HIfdRhQKEC2KonEXN-tHtA8HUX25ZF76sFyiiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
⚡
اجرای سریع‌تر و مصرف رم کمتر
•
🛠️
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFZIxZDd_Dr0wXs4eGsfvsKCAb_pbi88gAI9upu9gsD9-Sok0ye1FWFz8fIjlSsbkc7XU-SQBuDVbBdMDH-tU5vbewoH5SERdsim36z9GjquOTEmRUOD7X_C_LVUu58xY5CQ2Z3zJsFCxj8zlbOP28XwCMtOE2teQ53B3shTSp3vYJXaFEqlz-SYk8_gwsHqHy38TpqnYtJZm8ToE58NamnMZFiJiJtxBv6jNdx_Aju--rfHZICKwhgAky5UR_tZ3xk041HIzLrjzVFOjSqUtEF_hDW9uZZGXz3Zbspjqd5QZXchV5aXgluILADJvhzpXtBEOo3qmO92QB9PlupcEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekBkx8i6EGLtvaKjbQ2tANRADWrPm4_dlOm6-dIgKf9y21FLmqboi2_AEdV4GnWb5oN_KXBcyYXe9jIX2y8GJTggeZj185faM8FCaeU0U-Xs8P2io8Tt0est3I6SjgsAgGca3e_lMrDsgGErVucydmpRbbMHpyqPCtL55TIUbQ1BUvfWEVr7BQYd6CFjzShMRc4fhcCQFQ8Uj-sZ3_tYzLTIy-2QZT6gXmt523Q4Y_ojJZRNmW1aY9_cCq5aTGAlL25wDDbDcKyTsf3ujMuqCKEjPRQutK4Ndj9N9H0hpUxAFfBeby3VTH86zh6z4zS2q1H27I9tqRiqFlVNTK_skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mkwxl2yWSsAGl2y4tTENIQht2sXoncv8fuNAZFwLR98MxHazF6Negpk2g6MQu79v06oIIkdcU3CTdk0Nhpvv-eNrtK0gGp5RM2DZfekkx8tuTRX2IiBVkRztfzIwHNXgTZE-u-k6F82BYWvcdk0Of4Zpuoztj2kAt2lp2CBEZE43f_hm24-4nfWZFvC-Ux4og_F2VQHHqHfTHAZEVXpL2N2An6PDiqJ014AtWcc5TJJEYHQyOvAAjw6-rgtRUWyHBwH4pbUG_IqbmI8UM2He2fmTRo9YT7nz7C2or6vdj36FFU_TOYiic4hvl4ylQF8WGlkwAvuxb1IBkfB4Vy9lqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvPlRxk35kSrFaEis3F1z_4Ss1cfjLAlVoBh7j_DXdYlSIiDWf6fy6_TPTZG0BIniIeVwxegFz09c1_IgidyZ8S2pDnOYvS4iEf1rKMoAdQswQ1s1f51K0epXBfua9EXLn3w95TsEorDjYiKK96wO0pdiUJTCdjr2GeT_8FMyRWDsh8EOL7oPD_wbp2yccmOfv_WHB8Q_29x2Di3zxNARBEx7FmpUpBgxj3evFvWDfhH0aAvkeHlzKwP-8s8utK43PbdNt4DioNuQ_vBNJUe0o59wMFLnsn8XnlE9fWsgXM0Kew6ChJdZ6gNPk6cHklgpYlf9-hHyhPHNtKgi-rOvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzqL_GzTm1cKQv4he3LsWYPf23EKTvmwYVS5o86cC8bZ0W4iZbDmbcX7xajAPiRjpHW-sEMv-4NYKoDwQLqmj-HKnnaR2GJ0NxRw1aB4HqGH_zSNcFTKia7LaDusEAB45Ec4w5WHdWNd87J95tmnzInQe_6k3SeB6jHUn5VT6nb-TTQPfdhX38uLhFMTjXSgAkEQ6u-ec8I57R_5RhjhUDoGuvfnXcheD8WdSiqAGmdv1-tncciLWl7ax45-aRXEvCP3cXADZHwYzoFuDiASD7VamWQVHEXVksLrfzgKvTNcfLS-taMemZjxjiRc_1wW_V_lK63r4KbvDv5yaFdb7pGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzqL_GzTm1cKQv4he3LsWYPf23EKTvmwYVS5o86cC8bZ0W4iZbDmbcX7xajAPiRjpHW-sEMv-4NYKoDwQLqmj-HKnnaR2GJ0NxRw1aB4HqGH_zSNcFTKia7LaDusEAB45Ec4w5WHdWNd87J95tmnzInQe_6k3SeB6jHUn5VT6nb-TTQPfdhX38uLhFMTjXSgAkEQ6u-ec8I57R_5RhjhUDoGuvfnXcheD8WdSiqAGmdv1-tncciLWl7ax45-aRXEvCP3cXADZHwYzoFuDiASD7VamWQVHEXVksLrfzgKvTNcfLS-taMemZjxjiRc_1wW_V_lK63r4KbvDv5yaFdb7pGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmTjXH_Slivzwgaui78grWCtv65xM2bXaI13HvZZ2ymyeG0DQR8MUd1S0NcCCuesjxsRtlVSGQgNxfy6df_XeaEuPwWPtfEJxK1IDEiKDc43QzdejiYMDPVmGxSeU6vxoWRqT-KSaZH_SbtJug5bFZTt9UDQOsw7pfULwjPRyOalBO9IhA7_9jCtsGZSAPoRD-c3dIs7AGE-4ufx4kLfpE6lWc7DgvE5Mu1LteCzhufBouRR6SD5xUwj7E8cd-hAGemItHfv_p2U4FlAcpcxie6jHv0FjOaMg-LaLOZ1Xk0Pen08hXhG5jhkDSytM1y-XqKbdv8o5ud5b58xyRdxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYJqqDgyZ6W2dTH5XhHlqi6KG3NN4R33zobdRqLELdJWDZ8hvQCgpde7kQMgwF1_N0o4anYginE1ZMzpY_OOo5E7wjv62ALT-pLVwhmN2Fg4E75jUsj4q8XIsdhP_9WPtMNeza8WX_U-EINvmv6Ijn-gjw1EOHpsFezt92k1PR2xoobtTsqGjWTjl9rcjSovZhO_lPF3w0djQy7j_xSzqGfNBnAecnniYXeki0wBqqIA5meuauxey7bcZvr9f0IWASisZ1jDxOEWV7Ttvdtsfq7s2PrEiOg65-mbmO425DHVbY67lnZMBY3mlsgg-XpuOaPW2hXVgUn188Qq5cFR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq-nutm9Bt2OVBH2Lo5_9vP3hEyMHj2gB_5sMYIC9o7vSW3O4QP-uXS79OcBwPQkBGMskreX-S7bZ-FHCBlTxWUWVA8zeY_F-Wkvy_dB8iwS30c5FHhRUCCJfWOglOFxKiTDUrPYTCV3pvmcWM2byuWtT8lDF4Ul2GPUu7V7vfMNyLbbvho1J4WeoozhegGbEa358QYV-To33hJZ5u6u3hSm4d3ja-LGLAZzwsnDvm8qHagbz3SI7pHEKTqbFK3wy90-w8ew78pMC32GZEKDql4oovVIWUMQlJ_PjYaAbnFiqqJC6tkoaKf51rnbG6BMFUGsvLQ0oElgOjQDaIJH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlZ2cQ1aWmFRMFWnNqBKZ8z6OnpAFdp1OFKwhu2y-nYopEBpWLA4U4eKh-OjePPNXQ6YcWV3GOp3Ix7tRK--8RQyVi0DadmHykbEpjwRjuzzw57jcIszmTIixk9yZzJrk8CVnEaw9pOmajdh3oOw7nUXRELvAXyXeXMkewqPQ1ELTQCJ6ASHDcWx2zr6Sli0v_fqdpngIUBVWulpbxQtM4RdHl7AjQSLQr6zHR9fNbPWM7Mbj219_fbmvWue0CgFr6F-U6KzWT9lDx36TSbeCyAtRy0qO7I5qJiFZjqgIldtCu1KevjKKgxBpI8OZqcH5tZs40vAfMnyOymQwf1Dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKb9SndfrQ9q-Hn9NpmPqmEPLHjermhJgnpO0xQT-As1DXXznzW7vGIIrYUF5NxjqzF4Le-0yeRZKPfE-1tm1cQwmf6tXvq9usVkjO76paboBKh0PQzspd_naUWw4bH0UYB78PwdfDHIqFdW8_NLITjkc8a-lQW3h3nxRQbdU-Hq9oQ_Hogb7xSEkZ_BLGtoh48XKLXyk-_Ayiy0xNlKzT5bRVFtU77MzWR5xt_MugSEG0qMizStGjWqdx0RFynG69wApLY4ZuGWhOnF_CRRt8FMWABKZVYXUSqxHc3f7MkozXA1AgLOyx5JvFb-B1HF7e-jjQJgl3Ir-APUmZRqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">💻
ایده داری ولی حوصله نصب ابزار و دردسرهای راه‌اندازی رو نداری؟
🚀
Replit
یه محیط برنامه‌نویسی آنلاین با AI داخلیه که می‌تونی مستقیم از مرورگر پروژه‌هات رو بسازی.
✨
امکانات:
• کدنویسی با کمک AI
🤖
• ساخت سایت، ربات و اپلیکیشن
🌐
• اجرا و هاست پروژه‌ها در همان محیط
⚡
• بدون نیاز به سیستم قوی یا تنظیمات پیچیده
🔧
برای شروع سریع پروژه‌های شخصی، استارتاپی یا AI گزینه جالبیه
👀
🔗
سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeJSa1gs6Qxvx_XR2oY8d6mVjLY7883CwgARJl7uAgqE4y8RjYQdpqkJW0-H3PTmJKUfHzoBe5JysHBKrsTg__PAnVY1agQBRIfX-cFql89JzqorX2r4RbYT7v5SegN_HqEbR0l4dotkibvJfZsO50TArYbLYU5bOWsJsH3z2YlkgP63A2O2vh2oAKXbS683r_S1aO-Y7iJo9prY3Ihe4tMIiyw9cZU4yZ1VlkNJGljCtP6n5YYvTOV5By5OsTlwLsn7gvcAYMFLKl9HUSvn7ZQSDGEkaNksR9_8rBuEV85GjiEagaAJs7H_NV_olu-Y9t775yB-gY4Pukrj4MiLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دسترسی رایگان به Claude OPUS 4.8 و GPT 5.5 + دریافت ۷,۲۰۰ اعتبار!
💯
🤩
پلتفرم
Gumloop.com
یک رابط کاربری چت حرفه‌ای با قابلیت اتصال به سرویس‌های مختلفه. جالب اینجاست که این شرکت به‌تازگی ۵۰ میلیون دلار هم سرمایه جذب کرده!
مراحل دقیق دریافت اعتبار:
🔹
از طریق حساب گوگل یا مایکروسافت (OAuth) ثبت‌نام کنید.
🔹
در مراحل ثبت‌نام اولیه، به سوالات پاسخ بدید و هر گزینه‌ای که می‌تونید رو انتخاب کنید.
🔹
وقتی به بخش اتصال سرویس‌ها رسیدید، Apify، Semrush و Reducto رو انتخاب کنید (هیچ‌کدوم نیازی به لاگین ندارن).
🔹
اتصال به Slack رو اسکیپ (Skip) کنید و نادیده بگیرید.
🔹
اگه مراحل رو درست برید، حداقل
۷,۲۰۰ اعتبار
به حسابتون اضافه می‌شه!(که مال من نشد
😂
)
🤖
مدل‌های هوش مصنوعی موجود در پلتفرم:
Opus 4.6 تا 4.8، GPT 5.3 Codex، GPT 5.4، GPT 5.5، Gemini 3 Flash، Gemini 3.1 Pro، Gemini 3.5 Flash، DeepSeek V4 Flash & Pro و Kimi K2.6.
❌
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 Ultra در Claude Code رو ترمینال ( کاملا رایگان )
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
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
"ANTHROPIC_BASE_URL": "https://cc.freemodel.dev",
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
حالا Claude Code روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KImKtAvpfp4qdLpUYAp-ZhgXKcdRLzmo-G89c-FGiIQZ2RIEfX1bv8rjkqeSxuZXIOFnAJJqFqQKJ5Lf9WiqQGoQsw7Ux-R1mHtgiUHuhXzOSj9C_lElZYk73sfxn5Shi8yFIunprStzLQsMQApRotADsSNlyXGAy9p2e-rHiLzXYYunIBnMZS9hDVDzYrXzh1qXo8ralSDQJNQkGy2P81dej29CidgkrGFSp7R33SFvmGKpXGSkACEkJTzv-FqD6oKXAneFJEy8VNgikMhJs-FScwxi38Sh08ch_rubo4AA4tFtIIs5sZlyc6UEqA9LkatsVNDBLejxHX7KJz6Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ دلار اعتبار رایگان OPUS 4.8 و GPT 5.5
🔥
🌐
ثبت نام
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=f_vcv4ZrBK72RYWwLuqp_rtfqWtEj2DZNgpB54fwuoRfTfHC6TU0-WtmI8CllOnl8SGura17QD61bw-zT61Ov2jgZBWTHV04qliJlP_2w2yW_zZAsXtcFdt_GPQUk1zeXRrL1td1wbWu0MiqKGE6BNb5CTRPZOq3K3MNR2nA4N8fAYkY-O3IlqRIs6MRYYLuGR-a5GXWy4XyRruNR93kkWCDGehjMlK0Y-FEW5c4yshArOYsd6-7hWgzMrrB5vyokEjyzeQEEDzNRjMJWP_qXUAP2JOnqm7L6my35pH-FTQPc55YZ_eegl2H0sXXcatUCAuqg2Ya5QG3MAuIg69v3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=f_vcv4ZrBK72RYWwLuqp_rtfqWtEj2DZNgpB54fwuoRfTfHC6TU0-WtmI8CllOnl8SGura17QD61bw-zT61Ov2jgZBWTHV04qliJlP_2w2yW_zZAsXtcFdt_GPQUk1zeXRrL1td1wbWu0MiqKGE6BNb5CTRPZOq3K3MNR2nA4N8fAYkY-O3IlqRIs6MRYYLuGR-a5GXWy4XyRruNR93kkWCDGehjMlK0Y-FEW5c4yshArOYsd6-7hWgzMrrB5vyokEjyzeQEEDzNRjMJWP_qXUAP2JOnqm7L6my35pH-FTQPc55YZ_eegl2H0sXXcatUCAuqg2Ya5QG3MAuIg69v3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-jGbCecD81ygTzctpJ2BMPchCdlSllo4edtmwJH8yxbj4zBZPqbgtQTAM7wpj7xeOFpbp6wjWRX2c8Hwa7zFt9QMCcJzFaNdglxF4_0wq-zcmhl_imTDJdMeiN5HdtwRXpTdnENBqnt02xrEvHVGu6T2cmmoOHvst3QttGw3SWHmRNEjR9UfQKn7vL7NC0sywBNewLa5DqRLNJ78Bo33sIoHS0VdduGxw9UAaAkEVgHYhxyLeA-99G_Lk715QsJMo7xbdGarLq_BG4e6f1k5ynAaoko3i-hUoLwSAhEoz7ld8z0RLI3ok82l3u4jDwA5y5Ido9sR12gRuTuCihRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKPtf4mJQRzPkwQmwPfQr6pW6burAd5Gh4zZdkRiPXWBJXyfzu5_lss_9sSkH5Mx_KXDxO4bKDpVknUu-uFdWAmQZZH-MIXKYnQZo-Wl8F1KAEgxeqiFpmqXgX6TFdo5pv5c_0bNwtnurgRGcvKsHzTAKvZnDnuQSe_g9QGGnlxZ5bAzdC6RYDq5Lw6ih-hwJ4uJNBfwtK6VnoB7y0kh40018MkptgcfiAQPoIUvSrfrFjLL2ZVw2bPYhJ-6-ewWuuJVZ1in3lnuDLnc8fPZ6BqdhXTexpntOXxQdHDkIJZrrPwkED-VmFB9Yv1XsJ9G7UzRJ7BSYasK6Y6vyC4azg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCo_gn-YsE-1E-bYEpFrT_pxUz30Rluhcc_VFYFUOK_lg2PUnH9CWquPyh83FwRGZWnK7f-CHgAguRlydvd0O8SUwIAOkwMazQ_xuGSwZ9tcFkV-nZVwP-jGYaKn9wqqoIBu-ezM0v6gSLVS8tmxOS6QASLE28Wdsw5GUmYpB6jVfyuuGS69sZ4gJwDxQvYjmgAmkqcNAvzUxwBlnTKY9h0_k1FaVHeWrFCiqpfXbAhm_KdAST5ltPQ_ZCgydaTQ-vl25THraLkWqCmlC2vtxMR6IB_3zRTJZoUJCXkoVcScUsDxpCSEM0ePZazExOjr5NVnvp0KxxB_bAgfuEEX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmyQEdeTz615cidM6UAoHeB_wjKsrrG1ODYeXfLmx39e033zVlFfKIU7vmbt7c7WXp1N1GjPV0jWgzJyhLau0S5qheC3aY3JO_a2ARDziPAF00IA2rzYZ9ejNZ0pTCIiOG4t2WLSHBvChpiNfv9lfAaZPrQCOXoW1do_CtdXzDOFhGxfTnMl59ti4ZTB4HwtFkbeh_pZBecJJgyVkXdbUgpxNwRY7icaDH-u00O71bCTTgWQq4AzLSWOy9CQP379M4fsoYIzyqI1X3zSXDh3x75QwVjHiyjwb5gYfKNQUTsbypsHm8MpFhnhXRsIu5iZWcVFERt1FV76t2g1uTJrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obpnqTPuCMZmsN2DzWU-2ux0AxksyhMw44qqLmAlfYnLvLkSmAjHCzwW5ej6Dtm409Ozdkv9_X26WAv_uCXJWZOF4TIwYb7E8EbQ0fe9LjEebC53BXcyRcbVT2RMmZGcaDMAq3WppqDny7IvD6ihtCX93hsoaCTz5kinVDi2VPNTrj5Vn0zZ33gMUw_bvee7VszrzpN9xHi4LKG34WBO6VRDf2noo5WS3MEIpMyihr_wnkbPDxarjWkzu8VMue3iN09uLGQUSfvRXe8dRFRrwglPcKP4OG7aaiwqMXDaUnaOrv6X6LP9pizVhv_LAYPhIyqXGLn_J0vjevMHN5vyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jquAmtxWjw_BHndrGMZaQdiNO1sBlQY80IptkKrWKxzaGfE6AkHU-RLHDksx4byhUMaRhGxMzEl6jTmFxNJIGNdIDRGWVHvVRgGe-FrsXORQetvb7rxAl4TjQNKBF5pA7X1SzOpf8sSdSG_gPDBfl_yFgW--klVaRNBIduyp1s0XnoKpI9FEcKHL2T54oMIkGYn0nS3l3nXADBlbL6UR5HfNc2htbWSORPhLMhPuD96YgOYysvy2zym7n6DasVKg8GTmc1PniidJ9L0uQKfl4Jz74naRoTtZyjz-_dAWcHPwoZWdLSy47_IybwCqqKdIUCQfq3Ci7uwgqYLynC8lGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPRuuyHfaYDKVkOyUBYQNyAnc4hVPeveLqdIvoZtyCpuG0hoPZv9TKHoaOuSaaB-J30QKz9-GS2lMeUJhKNtGTKHcx7-HX2p973L3W40MsVayS-pSyXR_4ggv-ktsOD46ODytNWnIiIwHD9igaAnjOrpnnBW_DflDoQUldO5UUtqt13dPR0qMvwdZxa5d3U_a5gjyy8qc22ILQ0j5k9E7fL4ztvM__9nKDFqO_mJI0BkTZhQUAh1BhNVpVzBge9Biw4-zP6bQVlcMeRsdTTL3cmsCJz9-IvG0gndLrBYpGY9gauymFeynJuucHVn-7uJbX11b9NcSwxyybnFCDctnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oE4oLdXBX4jKnzMLWn2uBBjkyzRA2nBK35UZs_tt3-G0srahZLwIWBbn64S6gNyUq01R0EtApVdpm6Jh2CYboqvjqHeagEDGQPcqxzcNtuLN36bk3_w_cs7ky0E21JuBqcoCuK8XOJUaR_iijLybZ5vd0lsGQVTtd5ikfnSJez0d1SIpN3gQL8BQ0fxLB_6i1Dd_GIUxldoKw4R3cne6DkgV4inJjp6hql6mTtFwVh--5UKIvRROFZcXw1u4AIOz6h9_OAseHJHRPxZiY-Ys_sGrYc1vA3tlD_G2MnkGq8M2YzB9_AWP5KaOF0WXBq3mgUlZTYf0B6TnDPXMXmAYsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAQsj3yT6rpvqWVOrZi8ROjZZ98SgPrA1JBRSBenOiKKimZ2yVX7wcwpLIzqzn9KxrMRfKQDFwZaxPAdtkvBfEWsNxCoxpjNg2gnxnGElVp1mpHO3r-vH4jfBBgxGrHuLpry0_x28u9Xo3w7EUwc1-PZ3uXmMiYJ_jS8IQPdufO1F5MOjY7j72HVhTqkVnOP1ytiUG3skdNkFK9lTzIgTd6M_13KMW7kH3b9pGcqUtgeWRc8fVQpUdOEse6JkVfRK9bNl6rHL-U_r1QKaShToIj6xCUnFknEP6dvYJCXuRgBTZE0xU2jwd3EUqkERKdCR25Yue_G_K6Fu4WLrIFcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5xlyS8kwfobmbqIQwhozaStcJq1EqNpzgMbFkNK9fba6Q3aZEN9wokEBOMQ4phIL-fz35_YtnfrFscv7POu3O8IAAdhYZ-oK1jQtHuMimOVocGruTdME6C74CT51aXN-m34u1OJDdk2Awnmz2TpgZBgWN98Q1lbblw2GkJJ4k8KpgThhgkQVo8AIkulS5C0QfWwkjvJoLRPAfX4yAG8v7xQS50IhANuHtLTOeFgV4sE5CmLAChMz5NJ-Wy55XL-W2Ha1ZTGA68BmYmGaPByv6QY4mkSVN-gi2lY0fH6ynnLsBNEsCxnIqUS87pesMVuH-1p0FiQMvD83IrOYLWTBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mds7R6l7rJhat53RezZnQ-P8efHpSLDJuosXyR5xZRS9eGpLil_wTBpO7Q4FbAP3QUj2Wi7Z6pAs8apGPxAWiiHhfc1b6UQ7Z-igUiznLt-RZBupmZIRaV43pRUbZgkMOAd6gLOmvPjfgCHeolH7E7iEI8lmyKyvVnwaouTRfk7jAPfHB2UNjuGC_JzpgT-74MLwlhqMnI1ChtPI3oGBFKbUkettLnimjgC_7DuAhOx4eORqLMzt9pRQabB3Fe1YQBtaAtaX2EzHNzpuuHqJFH_Zsv5u-M3oSRDUF7tjyPxpKnEbXu8KJcTu86FEnDhUu4Rbcsgm-R3cPof4i0Pucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8YnmrEtIq3jX3NcnBgkveKy32b2X1u0omIM7o-jBFiQIYWBnqcLdxLv372cOIKoOqPYG4I8br-pQ1vzyW1-aVNZ2vNQeXt3g--D70z8d5MP2dC_JQoU5cnRKg-swhBYbbpqHApUY9Q8cwHB3s57j1ZmdVnF4GbhFS1LbgTgXaydTzNsSt5_nF3u3WgWHhUdkS68L9xMOSbF8f8LMIp07sOk0WyxnV5Jonha1j1eWXuARLxEv1hsXYf0-8TCag_hQXWvYPjHay13A-mq5MXslkS4N1hQuK5apkQ5aPgfLYp9GBu-Uwx4pmFWJqJTS4zu_NdlNXEyyLSidX6RbGoB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_GOKAsiq_ag3_4WTMOMt4bUHJWVvKh73OzRlPyEziXfnJRORfFtzguN7qsGwP2WNZDP4_iigb1jMKhZTdjbRPqRC0eDBSpMvs6TKWnl-qOh8TPkFyTY76aMrwNs6rVDJ4tIf1cxBTixPRrZOn6ku7uAGbOz6ql6GsdS-SixfEQ4jaFrykH_fwQIuzzViEcMX2_YNEwdkw_f7H21YU0kZA77mWIcMzgFLZoz8fu2vkiCr8J8roxr6sLNU9AV7ThSByPCGbzfy3ouu5QUevCoU_dBC-Who_20KoNcQaXEe8ECtoF0DEJa6ZxtuESYr6HHQvjhvnPIiXPgkntXLmv7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjYnHVtmLEp1dlRXbZN_qC5el4uO7h-ob-0ulw2LjQezzkBg6_FUgITHueNVaHEZjca4NBNWRDnEmBUL01TJy10tgmGdvJCw4b_3sthzC_2BeiqN8KxofMSR6bABIkWyouUGO3PsmJk-nEu7dBDZwwtWcN0dJLqKo2kIQ7zxoiFLsipbeuxNcW9CkKr6ayG-LekO4sfMj_VWsHt8eRjHlRBc4aAugPrBZmPvZeFxs_N6O1pO-KEI4ZjLNbZLZ2JMA8WHBiOX5FZeKjHbOlXlgT5C7TDCxmJ0c5yjkWVr6OfiLa1tk6KF69Pj-Co6FaepuQT9jeD0n6_gnxuCBpVbRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=vDR4n5S1pFg_gIiIvtieBQmzpRpQg6FGrRGYYnEasbg7ycrPcgvqZqAtBBJ5PVz_Gb93TwjMlH3mKlcRFVt76DS8M3uwSHUzFVMINUc5p6sNE9U1PK8PCPjqYdx9x6LPWgZY6ZKHc-7HOScur_iJy7Phl3A_xTrm37H-WDaEaTiWm-N351HRw-8YmzDdGxw1-xhi97f03q6rtBnrumVAak9OChQsg8G6KAfLueKaOo_hdsLwzJGKF7PVMEQWzKsaP8mqcZ1Ue4YJq6UMcs6BiFUS8pv17wZEPkO9N5YGKso3rZFWEn7xTHWwN_Zm2jcR1TqmhOjiKNnF0TrDkfDB9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=vDR4n5S1pFg_gIiIvtieBQmzpRpQg6FGrRGYYnEasbg7ycrPcgvqZqAtBBJ5PVz_Gb93TwjMlH3mKlcRFVt76DS8M3uwSHUzFVMINUc5p6sNE9U1PK8PCPjqYdx9x6LPWgZY6ZKHc-7HOScur_iJy7Phl3A_xTrm37H-WDaEaTiWm-N351HRw-8YmzDdGxw1-xhi97f03q6rtBnrumVAak9OChQsg8G6KAfLueKaOo_hdsLwzJGKF7PVMEQWzKsaP8mqcZ1Ue4YJq6UMcs6BiFUS8pv17wZEPkO9N5YGKso3rZFWEn7xTHWwN_Zm2jcR1TqmhOjiKNnF0TrDkfDB9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvCP6SQ1ZBooo0_BSbjOPDdIDLzYe0N6EyiVW0PMIrdunvxpsHfTu5S_cG-PSPpausomZ6oqVBwnZlspLIrurnptnFHeWACC80TY4u_nIGNV_6CAwmTLv28Nrz5fX6oqL1gy9j7jOR2GNBuGB9fRqLrpZ0FmxgbtA4LLLI0e9twypxHerJsQ1gSHESp15w7Ivu8dnTMhl14SkVH-ZCDF78vDJCbRhCo1uAgdsj9SilVzcA8lYlS2V-qT_aLIma-4ueVwRVTXxGXKQffmZnsz8xHZ8ve0-RLxUhV_mmD7ed0BcIVwzW7oA73PRqdRyQzcc5QfdUXKffYD9Zh7UgFSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=toKeNhj7Yrnh-ybUrEiMnDzQCMRquagmYlgDUV4vmXV3ig6G6gFbgvC-s5nPHn4hKggFV7kDDcnpL2VzMoPdQSeALuKZH2Abljvbg_uBTMden8hXaQB-AgyddTJ6IS7oxa135r5JB-I35zypqfwTcQnzwbMgE3qadyEqWlG6JvQtTDEn7T1U4cfb1fOYMkqfJ2oepnteFmWvFaQhKVZqK_7ZR0HVj2MST8koSPQL0plPDJuX8Pg37ss-9MOr-Nh2hVaBgwV2PUy1N0Lb2zU2uNpqNZdyAhrxt0FkF3vj6F9wKmiMBQXvU5E5mDn5cFsi66KjiGTvwiccGXapq3y2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=toKeNhj7Yrnh-ybUrEiMnDzQCMRquagmYlgDUV4vmXV3ig6G6gFbgvC-s5nPHn4hKggFV7kDDcnpL2VzMoPdQSeALuKZH2Abljvbg_uBTMden8hXaQB-AgyddTJ6IS7oxa135r5JB-I35zypqfwTcQnzwbMgE3qadyEqWlG6JvQtTDEn7T1U4cfb1fOYMkqfJ2oepnteFmWvFaQhKVZqK_7ZR0HVj2MST8koSPQL0plPDJuX8Pg37ss-9MOr-Nh2hVaBgwV2PUy1N0Lb2zU2uNpqNZdyAhrxt0FkF3vj6F9wKmiMBQXvU5E5mDn5cFsi66KjiGTvwiccGXapq3y2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfrt0fcZqhDu5dqTHcchcZNdZqaZF8G6clqBdL9y0ODmFFhqVKKc10aA4E-g4ckPi3BD3vxSHm99HLNIjfhUgL114mdlMPqAvBldo0VYPocF-esusKzMcqXLNdT6G4Fzwge7TGc53yBTqe9ePdaE24oZFQoUdmoeTCkBMFWL-7aog5fGC8MayNOanZEm28Q4NsnOPGg59sr1WWuP5hrxcrCnKmeosAri3m5ymyE4CO5ki2jwE3xeGjHI76-Xrk1god3DBh8FIovcmAEwdrFEPpN64pfi2Gxakrhbv6VXY6fs8kdEt1akeHub67sSx_nVdkc4X0dzs8xU2VCv6lAiVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XsBTpBivCy6FC2Vfw5mfWXMC-RCrotaXJMoKOBcEeAF2SBadKsYNzJMxEp8PJEPqpiBacQbgcYNRzA-eW4K7P18BIz4EhrSghnlw8VQCPPC2e1qT1xzj04xyAFEv6ExWcZXKC112g0oLP-7uCWMOVg4eAxm94KVrw4FIpXQ3tswlV9mkFilEYfqJEbAty5rI30lZ_aOgBUk0pf8h6fnphxYjAyE2O-mvZzEHkh3ITSXYtqG-CUXG8U0cZZQ8tkXseV8SVyiLlhJErTK9cSp-m5EslnOmXOBbK9ki-BUJfwQ9LXNMZCT0bfPHNAS1GC-mwdrPTpXbB-GLlAAXs5vnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dscU51KWLDhyBLTPIj9vVvpDCq6sGMggqAmLJS_YUQ1Gx8oJAgbrHV1fwflkll7h6scm-d8XSJHgmc_8lvJ44S_Qi81dQgRDEQ52K8C2IEyBJ0Czjul8NqkRtxP5R-xkPfYCx6UKPRqFqiiK25vwWWZyj618SwkvZmo6hyV_doYBhSyZVUmYcUrTju7kBdOLCJ3F5PUJ7SqegK-Nx2seqx3sfXpiPll0ugW2vOUvm5LekKSC7DXXwrcEPKLrxY1NBcBp_9KyzArZhEWI9Xf09vXgGBhasDdWyIqESYiwQG1-sUQt469Y99gqlAWZfRr6AmiEQMXP-UANKESZkKcZYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W02EF-rgNAHNHuwbKL-NdFlIVc5NcRF0Qbq8vZxoOY2c7IxNAWSPIBwvlEJASoWHfnGk6guTz9tv6M5JJhI56yjcZ6X_nsQc4PZdYtixh2YpHqv6J6uO7YScRDIIfTnzRXu90a-zIo50nEjYZQ6JBo_CuOMYS7-MqOImiWVzKXWlLJx5AkDQCw_NeZRi4Jq7i6JKSUPzLesUFiWakJSJREypT0JXX9OKqg8nyqLY6q_hriPz_Q2n7qs1as4qW_EiAf473t9CHe2LW0XPltzjmSbHlxg0nPMRSsllGj7Sgpt5up_f0_tKMAD31mG_uAtgIzP1suxvDblHPkldpBayoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLxqw8nqAyGFt7CDoCaCm8BAVRvYisVx5LTGwrmcRIdpl2W0KQ90u920PgxaiG92DQLGsgp_uEzcvKUxyizdEUt9kQkCaIrbriJvJZ-ZCSRNF8AACShXkAll94eX8skMfnxqoqr109u6gl9vVXO-DFu7fYaCM10bcEmI4FSeBFmVYuj-MjAs9DucL7ed1lzh2DcY7RmeYvHpr_vYhPY_oqTvYF-Vz9FwN-X2TWL6gcGwkHD_oE6DMeGJtkCgY7X383h9-5nYO7UmD_qBaKwhg1xi5f13EtzkNfQawMYeyOV13kQ9V6wNRTN3pgXw-Ue1VGYYNWxYZEEgLk477zKF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl9M0TmMjmiip1brnBPhUDYjZ0skZpcimueBlp3OYjXDUHEf-2A7Of79ek9dKvRHHx8GRfyu_Q-sL2QFfobIAAmGg9fzQOGKnUQcwYgmg7icncQtcCZBzevn_iwXi3V6A0cZmKz8Ifck15qx7uvhrMSBqCWynjWaDThZg1i-zTBmGTuRoyeOdPkMLqZkpRSKaOXCQm3Mj7_1d9TqWKd9ncfmdfZ8_BAAEAr13rg53-V8ropk8jbS-OlVo2GFrAegMZ2Q7M0qBd_egHOd-xPCWxl6v9_pRrGc7be1A4NaOR-TgoSKPc35B71hs8_o8fxNznKIxr7xomPxOSgF9o0yHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLLSx_LEOQn-F5XffYbXCs7JS4Afut-YN8lybrPFfyuJ2Zq4UnEznEg-U-Jvr6owcBy-NvvwDIrkVzJYg7I2AQEydTtvEpzYsOePC092lhhc3ECVtfhotSup7GS-4bVQit8pQb2fH1vNdpbSOCNX1k_ugMxUFnSMnNzaMrVEOowlNyqq6jZAtY38BlX4QMgI8IfM7DCYw11d70nV944XJuwPgM7jf3D53X1ao-GLl3DK-vBs61PJD9LM5VOM6XQAvwTztNRsOjlyCA64AWw3idM1YCyF7gYot4VX4R3XIi6s4CzndDOFUppEMCdbHib66UW0evmcIobrFd7RkL72sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGV77XjfMSerUHqCq4TKAftSrCYzxmuefxLsFAKcYGj4AcS8iXT-03kn3JKaP7pfw9OYRC1v3XZ4pbl1D1SYI8gy0y6HJOoAjJLm5eRkh2NG44DfFr4wymjt05m1ikAkdlo1HNLdokPS1haj5LhNAYEucicN13G_psFHatcpmoK14hapPewAoCr09Tg4zj_PszDUNY_7RRv5eYtRTy6mg35ZGsZAKRWG9wEw8m-gkESNuUV3FPtYbD2we8TNogoJP3_e4SM68ot_Umzn8QaGqLzYe2enUfjiuD-DGA8-8MgFrvs23_wNPeT9dm6QcyH6GV6f9oT8vbUqKIt6RJnrTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLiVUnVYUu1jzQHCzIxFOlAO9oOp-YZF9As6yCVfzoYIVjugo6Jb2o2KrU9YbRkxka1bqLqKfxnQet9f2-iGw40ULJtiRJ__eUV2qElxO4UnyAApH5N2-1bqWKnqe-ofshPhue_ojn3uqRc0XssxBdGVHMO99G75R5ejKhJz_mxK57Obyk4lu74uG0lTcMiTvQSH-fSTmep8yqTaUrGHJj2Z22sS1CZO6-UtxDMmuKu-nmQHyUO-y9xq2V57R096cOzsB8J_djusIm5dEQzmCTYGd8P9DoANeosbv01kqFjsyMkarDBHMyYhk2zMALjvSU9oVbyIJKhvR1noBqzWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-w6rlLvKPzadFyxAFyzxutbHLWoujnInm2tvpsCydQwnsS_RK13DVfg-kZL-mJKT51b3A0dMH5JxNRZisJON1I9aK6NfucyGjWkoPMhs41PuKVprXGuTESu0Th2bCM9qQwVmWT0kaWRrxjlQI4f8SCQmThhEVTFhi4FzQoDm7_2HifmSOzp1D0JFz7wpFocWj9Ir0zesep2y3V6iWN6Vc1YrFWNffgaGZnemys1ac_nTCpna_2ZOumDabqtpMf_INXfB3zLFUiVDjDZm7brhYMHq0MFWMWTumHWtgJ7Sn2GwUvVVwC_BIGX71_hRr1wXp1YKuALNb7QQEQD6rEmWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyeAngT0l6VEx4V3gQmVdaUubGE_n5iuwyQ_fRgkjZQiQ1eueoFysUyiW2v-DZ6OdA3pk9dqN5lY7-Do_bjnvz_65vFTr6f4ITx9M7guaofAt2Ah42yFDcWQlHwgP_Vd1byPl4xoz27mGEsrSurOsMkdqu15JcLdecQPr9RjrYtVrz3x0OUHBVMDCP6-borexG3NqL8BWHDclZ6snqzcDkrK9_qS4foYt9HpPkxs-l5BJFo5XRm59z922NYCab0CpyDXZwWUDkbvBGnl6SuXZplJmqugcvezbwHoIt19uJokDw7BDaWGB6_BdX_4dN-4L2uRmytUKjSDZZycHTzqOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=oScTROPLkhX3EPIbuFZO2f0ouqxeQRbFO08ekm7cZWh6aVaEfpIkCEgQqL28Sd5pbwX1J4VGnw4vHb7RQNWlFkT8keHEqwcPDDLEmznq9CBTzeNEYlUCqbawVfkz5E-u2RpM5xLtDcIYTf0g25w5b-6xamRYL2cjS8KgeQUYUqEKEhIwcWNJn8GF24Zh4WuVsw4RKee9X2PTfix09luI59Mh6Ja2vZ5yyaeMlpjn0zCzO_Qxllf4BZO2cna52m-NxZBnKcIIYRX3dJTfrA8yMv-NIjc4J2ZGJLI291sl20XhfdvsBIArI_jITb9KG3tBmQP30gqwhj0qdjYrcdl3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=oScTROPLkhX3EPIbuFZO2f0ouqxeQRbFO08ekm7cZWh6aVaEfpIkCEgQqL28Sd5pbwX1J4VGnw4vHb7RQNWlFkT8keHEqwcPDDLEmznq9CBTzeNEYlUCqbawVfkz5E-u2RpM5xLtDcIYTf0g25w5b-6xamRYL2cjS8KgeQUYUqEKEhIwcWNJn8GF24Zh4WuVsw4RKee9X2PTfix09luI59Mh6Ja2vZ5yyaeMlpjn0zCzO_Qxllf4BZO2cna52m-NxZBnKcIIYRX3dJTfrA8yMv-NIjc4J2ZGJLI291sl20XhfdvsBIArI_jITb9KG3tBmQP30gqwhj0qdjYrcdl3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLJBGILbHpSDan1Fdy-nFyA85rW5cfZAxkL1Qx5UqZ7My_czzn3zmoTktR40lJMT_PmNDzpnZMgFT1nfeNQEesFRRT5WwL0H95fNnymkNdQB3XFRe6JLcLnTAUSnW7p0fdmcw_TP8v30gi1ZKEoPr87Dpwd--lBYXJ0IABWZAPN3U4dNUWKpL9cDdkuYD_oirMYMw1oCcJkRJBL5xio3uUk1Bn5Gr9vF-REAPyJQd7wjQXV7ZqLhzH3nSuIo3QZKKoXtKk4Py21sZcld5R4pGd3JRVW18z7hVve2QRqH_tJ4hJTAt6iWXO_ZRPUZmZw4bv8AshnXNU03QShA1M9-gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2a26KrPc8f9cBbHMpChPjtgDuqGiYz9N0zMtD0oFJZvNCZZuOMN1rd5ABG2qZewnnKz3t-1FmSGycawf9NsdjjvM7i0mbJCw5aigjdhzolhLUxLlnpWCp__9NgFgsrdVEGqJfrKaFfsfc24YOaJoSoiG_JMRGKDuK0njXtwLX1zFoPzKFZasqBVZft6WMpIMowae0t1vFOF4gRSjVfof3NdLMNBjH6dnJnxDpl4aQdcPDbh3GeXDKtwjKGLvRzOPzE_9_aja8EHMQMmFIsZZAwJfQ6NZQ8DDhKano9ovLc-qABns5wT164umbzPimUWC5KCEfBHOQeR0cvNIEs1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=sP5ra38IWIM5fIHS0-e-wV2wnHu5A1LqwmatDhtu-VE6tnvi6NWQTq01liCquB4JHXvdTmmo9K4FdBLNEjkttRQlBBrtOoEdykHiySDxZU1O1zvSci_WlvIUOMdg-UsxtZtcNqFr4dHzgjtQxp8VaqavtWAHefbdPxEGDXSAqa-JyiCAnDctepC7cPWyC6KddtxwrhqGWzsT_3QSe32UDarnI-M9dLOTDQl234EDhmS7b_44JVkXO30x1gFXQi3-YCV1bvdYdV-Z2BkzotbguVolH_0EszZOn220lbcCFm4xEoRQecM_zfDNgMLnWc-2WQz1bzdpvTqQWNlJUNHHZK-_gxE7Ope7PozQNR9aYS8cgW6OvdVfzWYflFU3uS8oXLUecJic1EyhZJUy_yaXnlmWikr0rReI61vgXHUjJPzTlJiPXLIU92T4f8jHU9zjV9Fbeadf2pAjTsW7MJKIjKQUXH2Fj9g15-SWWkUCax4286IXaIpmPYtr7kf-rwLnbOFrIF_Jkoxl8cbY7KImcNbHmNvdb3KplGWUEAO2eCSlzvgkK6MWWHMAs_tKfzAvm2dwCDOlo_gO4uzcoer8T7P8kPhL0A6YJQOnMCB-3WIfF9MoD1vNcPS8gzX1Gz_Cfi0eiy1IFEHAG5qZtSL6ZnHOZs9oWSbGm5GCvlp-Bxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=sP5ra38IWIM5fIHS0-e-wV2wnHu5A1LqwmatDhtu-VE6tnvi6NWQTq01liCquB4JHXvdTmmo9K4FdBLNEjkttRQlBBrtOoEdykHiySDxZU1O1zvSci_WlvIUOMdg-UsxtZtcNqFr4dHzgjtQxp8VaqavtWAHefbdPxEGDXSAqa-JyiCAnDctepC7cPWyC6KddtxwrhqGWzsT_3QSe32UDarnI-M9dLOTDQl234EDhmS7b_44JVkXO30x1gFXQi3-YCV1bvdYdV-Z2BkzotbguVolH_0EszZOn220lbcCFm4xEoRQecM_zfDNgMLnWc-2WQz1bzdpvTqQWNlJUNHHZK-_gxE7Ope7PozQNR9aYS8cgW6OvdVfzWYflFU3uS8oXLUecJic1EyhZJUy_yaXnlmWikr0rReI61vgXHUjJPzTlJiPXLIU92T4f8jHU9zjV9Fbeadf2pAjTsW7MJKIjKQUXH2Fj9g15-SWWkUCax4286IXaIpmPYtr7kf-rwLnbOFrIF_Jkoxl8cbY7KImcNbHmNvdb3KplGWUEAO2eCSlzvgkK6MWWHMAs_tKfzAvm2dwCDOlo_gO4uzcoer8T7P8kPhL0A6YJQOnMCB-3WIfF9MoD1vNcPS8gzX1Gz_Cfi0eiy1IFEHAG5qZtSL6ZnHOZs9oWSbGm5GCvlp-Bxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=Af_QhrzqkFVmMWeeM2-gGo_rRG_WrnCO5tFASxj8XLC4O0omLNpC_KFfJL2ecpW9ecWMGAdQCIMq13_YryUF7vyCkI64_4QXViwUjtcm5-e1PToTw3zKXszxHbMx_pBoPFB7sI_VjlauBjgr32GGts6a-aKu0pcqUfKX1FgR_oglf-cvki6UTeSgFXaROcJS-7S8bAOPKB2BbKNSC9nU74BaYSxV5c7P7OqtTlbHEoZaWLIvgKd8XgJewkSaW4eHI53hoCnSXFt6bGwgkiC_Bnmua6ltDuxKX6Wq0qsZzr7jfnXCOO77jOzKelKjyx-_TktVju_dBqS7etc314ZFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=Af_QhrzqkFVmMWeeM2-gGo_rRG_WrnCO5tFASxj8XLC4O0omLNpC_KFfJL2ecpW9ecWMGAdQCIMq13_YryUF7vyCkI64_4QXViwUjtcm5-e1PToTw3zKXszxHbMx_pBoPFB7sI_VjlauBjgr32GGts6a-aKu0pcqUfKX1FgR_oglf-cvki6UTeSgFXaROcJS-7S8bAOPKB2BbKNSC9nU74BaYSxV5c7P7OqtTlbHEoZaWLIvgKd8XgJewkSaW4eHI53hoCnSXFt6bGwgkiC_Bnmua6ltDuxKX6Wq0qsZzr7jfnXCOO77jOzKelKjyx-_TktVju_dBqS7etc314ZFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
