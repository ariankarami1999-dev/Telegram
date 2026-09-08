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
<img src="https://cdn4.telesco.pe/file/ohEmD06bAw9YfcDzaId8UAQs5UMCuYoiLl2Eo-ap7kI2YgaH_r-fCyi790M3B-ap94PPHScAVf2RBDr6a_8nFUxw2TF_wCQswoOWRrxhl7ldJViM31179ITvafQAtjdrxFN0zhQIB-Nnd0F0ksHsfctLzR6i3QvBgEWiv-aChqntTbicc6HF11DZBgoJSNua8uH92k3IZYQZ0So_KpagngR3dTCoV2SexlbpAyHA-BYfHzWPFOpF1dWYXVYSFJ9MDpKL3YIlNYD8djS36O9mH3avjmnE8oHDG7wyr0ix1HI73g3iVVthjlUFO6dvvygvmrtkz68AjGCJdRKImtXf3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
۶ تا پلتفرم برای تست رایگان GPT-6 Astra (بدون خالی شدن جیب!)
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
🔺
۱. پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
🔗
ورود به Vercel AI Gateway
🔺
۲. پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
🔗
ورود به Brainbase
🔺
۳. ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
🔗
ورود به Roboflow Playground
🔺
۴. سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
🔗
ورود به CometAPI
🔺
۵. پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
🔗
ورود به Imaginode
🔺
۶. سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
🔗
ورود به Vibany
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 465 · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 588 · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=ZvgAqaNWh6gw1QRG-K07JrSGbVbK39v9Trp6500kQ78CRp59cdb--cqkMEHOOhsS8q11gWzQ7CelMFUDpp5YnxnDHiOVRoQpSp_20xBr88XrWNZR4Ze9SPEP6VnQ6JfIjBPu4ZS_444yKJIxea85WaIK_kFKcKCJ6ZWYFrRWPy5GGTjFsEyKSbf6H0f2sZkihqu5oLBxxD_8vffWbHmfHeXCxrmKGE9vWJEqe495PuvGnGFlxnN8tCfEXlW8sdHcriXjjRphB9n5T5w4pWmnTp88GlEDcTaEwt8HQMymbqClhOnfESlVo3AisKR3prSxQd-A_hc111rPv5Mzc6fCzXAESOoVM4wh_OuDhQpgGPNtoH50rZqmIZrm28_LlzJ6eOJQ2pSy2QCBmPWYkVzvFwmEJeRBu5KO14aeWGYfRbI-faUliPywhThgwOBWlToIGW944HcJ_V5W4W-OyA4_h3yDDDJJu0S2cgwFtIHUZjQ-hQZI-ReNmG6-iLF9ISNHSbiR_MJUa1nmCdQlDromUqWnECCaj3GvUWQNuC9njj3QqOyquFemO0C-85GYPu2MbJ6Qr0Pmo90TD4XVPhPMn9hS4MOJLXv_WK3x_2OpmkeZtTNB9Z0NaA8Yux7ixZ2_ZlqZLBdZJPeSl5LGkRpc9mCCR0ceirWNuPLvyBpNLSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=ZvgAqaNWh6gw1QRG-K07JrSGbVbK39v9Trp6500kQ78CRp59cdb--cqkMEHOOhsS8q11gWzQ7CelMFUDpp5YnxnDHiOVRoQpSp_20xBr88XrWNZR4Ze9SPEP6VnQ6JfIjBPu4ZS_444yKJIxea85WaIK_kFKcKCJ6ZWYFrRWPy5GGTjFsEyKSbf6H0f2sZkihqu5oLBxxD_8vffWbHmfHeXCxrmKGE9vWJEqe495PuvGnGFlxnN8tCfEXlW8sdHcriXjjRphB9n5T5w4pWmnTp88GlEDcTaEwt8HQMymbqClhOnfESlVo3AisKR3prSxQd-A_hc111rPv5Mzc6fCzXAESOoVM4wh_OuDhQpgGPNtoH50rZqmIZrm28_LlzJ6eOJQ2pSy2QCBmPWYkVzvFwmEJeRBu5KO14aeWGYfRbI-faUliPywhThgwOBWlToIGW944HcJ_V5W4W-OyA4_h3yDDDJJu0S2cgwFtIHUZjQ-hQZI-ReNmG6-iLF9ISNHSbiR_MJUa1nmCdQlDromUqWnECCaj3GvUWQNuC9njj3QqOyquFemO0C-85GYPu2MbJ6Qr0Pmo90TD4XVPhPMn9hS4MOJLXv_WK3x_2OpmkeZtTNB9Z0NaA8Yux7ixZ2_ZlqZLBdZJPeSl5LGkRpc9mCCR0ceirWNuPLvyBpNLSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 774 · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAaDgmo7VGXodF21R8p3eaPsNV45pvan1W0putjl4oXHQPVs9mDpaZUeX5ahKfSykGcnighxVygcFqYQTNx9PlKkmxE2uQQYdhOcnFEFJkjyWntfk7ChVEKX1Mi8ndCPkHbDApHUcxIgdiOGlSd9EZC-0dBBELB_v3EMt7g9rLVAhi3j1PLAgHTR1e7HjcPF9CTyt8zKagw8s8IOMaxT6qYUSOAT5PHVT1h7C7pYB_1SCbZfKoO0MO5HHSjNIqWDW5pmqozuB0UKLUaftT7GUwhDLgJcNvGtFyAmoKRlmrzPWIyGbZ_IngmoOiAZQoLCLqVQWSilsovOgo9HngdyAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 864 · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=jGOwjXspA5uvhTRLSpfnjJXaYD6q2rSTZeTIc9C8uWtI_LghTbFpV_iWRYuaXLyiXDMZj7YA9nmJ7oq4bX_9T460CsbzbNW67o5ClxXszQEcOJAfKH5TJpFAjd9dfWw1P7x5fHACPjKctpgZkmsFOUzz709yLkpb3n0xXXHHhNVfbRglIV__V9dI1ipWevr27xHvx6i65Y-9WlwVfDYOhJEvu1dPmwtx6F1gamfVrK_1-OY41CPX4PwkCbF6KxppfQAgbIZzZdsu-iPfk6R1G078FVx7gZnzLrbEMsX4T6YKn2O7mA4AUiY-_W2B-56IklaPmHdNmOai8YeoaHqhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=jGOwjXspA5uvhTRLSpfnjJXaYD6q2rSTZeTIc9C8uWtI_LghTbFpV_iWRYuaXLyiXDMZj7YA9nmJ7oq4bX_9T460CsbzbNW67o5ClxXszQEcOJAfKH5TJpFAjd9dfWw1P7x5fHACPjKctpgZkmsFOUzz709yLkpb3n0xXXHHhNVfbRglIV__V9dI1ipWevr27xHvx6i65Y-9WlwVfDYOhJEvu1dPmwtx6F1gamfVrK_1-OY41CPX4PwkCbF6KxppfQAgbIZzZdsu-iPfk6R1G078FVx7gZnzLrbEMsX4T6YKn2O7mA4AUiY-_W2B-56IklaPmHdNmOai8YeoaHqhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 926 · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZVNqWkrG1texyzFde0Ng27i8gE1xn_4kJnAsmaXD0uE9tlK1D2uzXTWsHjqNvqutn6bcS5QCKrBjuo8pjv4joMBFe6akJ2YKUJxE17XX7uuumgHPCtw9QY3pilb7ykvyVyf8e5VEGRgGYGvbS3j553F_VXzOyazenT6mdJNvnmO26ujXxIIT-nRD_ScrVhsNDj4Nart5MJDjgmHUArGu-Utjj5W044z6STY7Gve6xIt6shFgy17acD4nIFiojePoYF1bUHNb2egDsrS4zpImEWBdWPnHONWerRl__z6y60HNjBjRpuevfYTlYekPp5UBYOuhK-2MEp1mUZT3gbIlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 901 · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=feSHLbuwdo3l31obOvH7Lp9gBSOVkxkVk44YJZfWsiRebyAOqhZurq3YdV0uP_SntD1d2cQjPYnrJKCQ48F8av-TkNbtbKDXjHx2MAArKOZgqjbx9CpaqEOUQiavi9PEHevnpVxuZ9K4qQS8CHWxTUnVxszADiH8w7VBnRz_SMXzoIc8hyChkZ6vO5UGE1ebp9bTtGJPEO351pOR9-6_mOU4VGtcD6WLjYJx5lQZbeMfaJh47BRJ7qlux06IXztWT6niBdfDhMdrbPYAVGdx7bsu0jGzJ4qLHFgZo4C162ZXMwSDKY0ve4nLpgaBtjBkyYw3WCJQcVlZxj-EUjjyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=feSHLbuwdo3l31obOvH7Lp9gBSOVkxkVk44YJZfWsiRebyAOqhZurq3YdV0uP_SntD1d2cQjPYnrJKCQ48F8av-TkNbtbKDXjHx2MAArKOZgqjbx9CpaqEOUQiavi9PEHevnpVxuZ9K4qQS8CHWxTUnVxszADiH8w7VBnRz_SMXzoIc8hyChkZ6vO5UGE1ebp9bTtGJPEO351pOR9-6_mOU4VGtcD6WLjYJx5lQZbeMfaJh47BRJ7qlux06IXztWT6niBdfDhMdrbPYAVGdx7bsu0jGzJ4qLHFgZo4C162ZXMwSDKY0ve4nLpgaBtjBkyYw3WCJQcVlZxj-EUjjyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 874 · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLdC0l7x0w4ca00oZa2-qaFHyJQC-cJoZbDb2102d-N9VkkkENwV-mF-LJahhUnAYhRHgR2N75NSZPridUNXwufkV1J2QSq_7gvakLq8TANZ9iIXOQRDRHnV_1FvujF9SN9sf9OZsOEgStllQMWBuu-kc5rZQ-MdfVm1UQLZv8ySKz0pD9nvtSzVNotOmUfbZELv7zwVuv0_BVaaSjUO-vqf_7ZrP2aMFD28DGr9oNgh7-_AD4gyShTBAW8dn8dIyJP8C4ruWrsFeergonqlhBvpSt8yo5jrWHuQpPfuKGHWPZJgAGd4RNolXwR6Joi_3vOOZF5580_ldwH4urHSmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 946 · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JefVfhcxDBzK5O0278mrGXAv9XycRkQkCS_9GXyKCL0VoVe6EgCIxj5LsA6TvT-4voNaM65Aib1p8U0zDcZJg6hzTH6-do6-lnf7L68Y9lJBlD2ONCd8JJ-dPnDHihVwUGrhumvLMxUxCqlgf4zDSd7qnX6KQfcszu8jxBKGi00VNlG03gbn9lXWwAkZ_lLxMSppxr-dgyVdIHuwt4eJ3M3Xp3zUkhsjTbwZPIi7Oojuyntntk7PtkyqtkJixyXw8Br2tsawSZ_tMAOSLvb-BK0I1QsZbBJmXhGymgHkLNZiHKU5ENHoOG-DLNv8Cyb3nkauOaygNUA56WQm4yRUZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbZLC7PFYfyfTk2Kg1XEZ8AXlz8Vm2DjXpoMvXjYMdGVkSWp6mgR0bcnJmm4ABypAWHA4q_wT81gc_d72pmwgZU8426ef2xg4f7_BfYo2LOWcpn4_S3PmuoakWQxwKbYqTzNFjrmJK7aobp2vrHMgtX9daPQ9MLOB-TDYcy1PKtbnuM2uyv2kIgk6NwosymxumZuNhA66MeXU3gs1fS5K1s33QmK2fCtQRk0si2U0XgwH-R8c-GbOy4Qeh5T5O0cW3P5jJHRySHRZ5QzfEyb3SMy76poFWc3GfAzGmN5_Lvkl7tSh-4L8CR2uOggJ8BLWvF6OKIcN_KJ-KRp9WUiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9TSZyNRuNFWT0aB69Q86r5UzdNZq7obLp-jpo1yq0mxgpRdIopD10y5W8_P14nn6UdRhx2QjuePFih1MXhPzKhiMyH-lklUXwKZ2kn3MuWEnHC-AIcqt-5dTRDIDN09WrjnlUNrlZoOtapiMYBnvvXbnEZCMPcqmqtJqTU5NIIPVP0CExCKFI2I2gngCpNfnWx7WRryISPjLtMDq9S6uZJBA4B51DbwpNtdSflV5Jc1M6LWvrNNfsF2QFXMznsVEg3Lw0xOj6LoUm6xPJ9aNla8QmPfyy2rxTeFA8yHzVl9fCikl-XAreb5efDkiOtgVaoUpFgiKjcN6NJyJpZFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yje1WbdNm9QTwjC1R7KZYP5LhRpEF-DOD-WsbSKk1tWjG7v3mncuLCKFM9sWynwEkhtqFg_mDysFSQVu3D_jsbs7Ld9533AFAl-AXVsl24iDzdYBEgGHNpYCWRF3xROqNo5_GrgShz1KvAe-lct-aBJRxhSCNsX2U90A6uAk5yP1VrmqjxGON3I0u8BzU9PPCyDJMF1QDAVsWGCsLJ14EJ4pq8WDnq3ZekieoJVKcW_QO4T9KimMJWs-O4JQO6_CR7o1KVF9yB4Kntoudxv3NFEvDqOfBzZaj95gk39RywtkoDtrcPJtuyFHO4-4mUB-LNDdwFqCSq4C-ZLdPfvjHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLsf9iZPxtGCscBdZrrOuEMVAJU1O6oz3_DC4t8k7GQjKbiWITq8tB54Q70KixyYfaokChBa7sElwEfTD-hkSLTIEUnpjX3Iyq8tMlW_tXMteF6TfEpdD8yvWFt34kCKnep1fouVOov7CvyvHHY9XAzZ7u-K7qvC8hslX6ThYNqUVriCaKMJ6aPDUoXAZPqsEefYTuleIIUCGDxzAFXDlRio292j1a_2eq5Ob2UEY8umK8WhLqn4H4Zp8EPEQgwW0qZcd2gVrYr5dy9-ivby4v4Sy5R98jtzz37XHgnEfYypIcp_ygk0pJ6r9v5Srv12ApXewuRViNzSj2iCkdTP-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=VjQdNg1jmmVDTvO-sVmY4rQKOS1p1vV4lIvfuZfR9GcFZiTzvUXUbZRpDbCQUjgREAa3KLWm3gEc7iUhOSYhJ9T3iqMtW4GJ7SlbYTVRqYNpaOKzLIysCVBz14q6X7rUhAdB-_ddw-q_CTY_srxK76yU8mykoghCkXafJLJfSbW3fIfYurNsOO4HkdGjvbYDEgiAJAD5JbrqkhGLzEBQi0d8xVipXsJGRruQwmTpugMmKKAc_R9uorV27w8rzYky3zNs477usUf2kRv38S4cCNSNxz1CevLUvip22xwi3fMOMJnIbP750WGbMLj-URxyyaZ7cOPGkIgabMcYYntsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=VjQdNg1jmmVDTvO-sVmY4rQKOS1p1vV4lIvfuZfR9GcFZiTzvUXUbZRpDbCQUjgREAa3KLWm3gEc7iUhOSYhJ9T3iqMtW4GJ7SlbYTVRqYNpaOKzLIysCVBz14q6X7rUhAdB-_ddw-q_CTY_srxK76yU8mykoghCkXafJLJfSbW3fIfYurNsOO4HkdGjvbYDEgiAJAD5JbrqkhGLzEBQi0d8xVipXsJGRruQwmTpugMmKKAc_R9uorV27w8rzYky3zNs477usUf2kRv38S4cCNSNxz1CevLUvip22xwi3fMOMJnIbP750WGbMLj-URxyyaZ7cOPGkIgabMcYYntsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vim4WTc7Nm66yE_u5tIs-_IulSJ6g1K1iXR6yxh2pLYNzzi_yE2YyXuIUUGXTY2oiLD_iuOTIOawGbfw_F_CrQa5apkdnUpmTR6OidMltpkhDa9pYw-fqv3TTXkt1M1xDVV6putekL3n1CGEIUe3-fAsiqM04lx5tMe1Yo7l6vO_fOrxp8Km5At_DppxfwcfTaT3PagAu7ZZh9cUofGpccxkUZOhOHTXo804t05mfTvGnCMyi_gg5YRtgqZYUznl3pGESxNqdM4ZXAwTjyox5WPOY78pTONjH2WuiXeGOSDVZxz23GtzCIrJ3hxzW1InOnpJupRc3TXfisSK3zUWFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFlHKSGDno-ruYCQ4lL13lSpYExGiLUEtByXD67LVnfmcnK-TJZe6GGrdSTpL8K-j5nIJNLSNe3Z2WmB-OAHfPRPzMh11DguXCDXWY1-QWgzO1TVndUsnLCxcer-Mu8CdhtbgvSfQyFnXg0X41nrlHdlfW9uQGx6sBbVyje5DPLxi-YRQ2ugf7nLzDCjJuPpwDv3nmHOOaPmDxzWjVYmYNSnL_uPMfJRmZyo9NrJWFsD81jsaNecN_H8yT5r2HNB1nehM309qEfUhRsu0oB-Azq9qpiop4MsWPKmmqsk-Hv22ifmJYpwr5AFkV5NdMJj5T_ZVal7649ddS9Dy09aZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk74QsJuAAAtYmSuGReZwp-JG_wTJtUG0gAAr34bBFzDQ2JDPFJ6AwAFzZQaRZHTdLTnlR3t3eYvmNn0pNNc56zew2Ogj4YEMY0QCHhFudzivAxBszBVEsirkIymFLoCrSU86vnSJ1b0LpiYfE-bRg2h664U2MWtkwLdrAehSnL0DzMQM4arwxDZJSm7lgiitE_DBGBo15Jgzk1KP_6FRO-kaun_UHdtxVshtQQqFEQRVGNGCZ4_BJA0M_ZEfDYdE7zMTAojRrJgTlNZw9dz6YNv-RIpdAdT3kSlXUhVGP0FZ8eW3pGlmtaReXN79RRyNh2sPvaLXjXnzjmA-EgmRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azxnVtXn8WRInSU0-4vz9DxlLGHKAb5UQ0ygRz3mFHtT9ZqTk4Qcw_O_JFxY3w68ctnVtHZWNJZjyNJuuDAAJCdc0XAncFRM2eazoVfISdc-myUOwkRTvFlNqNHpgoDVpHZY87Ple4Ij5sAi1eIwseg7C5xFpSKu3xJvX5M_ePYaCp0McEmtpL90ibDqyPvOucT9CtNdeTpzxYakk7mSOuM9LtGkjh5dHURO6ENMy3sIinc34KY6sWQ9Fe4o4eewUllZQjm1FQCMDSMQYooMQg5G2Kk-cDL9Exc_X5oo928kQEqig8Bq5ATgwi3UOoAN8vhIfzLHL-LREG2Q5bLVLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgbYqWEpGVeRlEGwmPleCnih6-v7VtIZcTyQSjo7gcNK_NhnmW1HAxClYDXdOAXy6lcoZPEGLLZ849phuWuehI7cZMvCW_3ETPMdnFz-UgrjVz_lCfHcnRBwyoYkUDUgG7XL68OcgMJVbj6NKFX5HNsVA8tEKA7_cKfecpzxaLG-WT1jfqAZG5o3bwwYJdfKeimIZq53soIqTwosXoAqXVK0ATuCM-ZlDjOtGASi3jVGHhcKiRmOh-SkuClIRMbiLwXrsVzRhRuag18wDyHuWNNATHcGm5CH2UIPMZ9ce22snkzFm9W0_ETceRz38HvD8JS4gjOhWP5gGwBRK17TAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP6oDSCS_R0Ya1dTSt54Whk8xhX_mBPTse5QAaCxqUf1swFslsk9-lnZn_QLrqaOfEyp3HFynZxsApaE4DWQ1VpsQSjPmPHSH5jNkUlXjdgHYP_XrZ_3U7ECA2x1iswV11JAvihRoOK7BuNb9U5HaENTTSihrRw2NANz-flkkDWj6B5Z8UfnPlkn-l2IIpT4Mv-WIHou4zlFPei7_gpaTmJJFVOu0_UrPXBmyloNFwm45MlDCFb9OT6Q_4g1EiYjo2a75T4P_TKgoJNvJSFO_HlYFuSY3OsggJ2tcRqNw-bLdv1V_WaGqBkDvU4JSwdc2AnPj-N6m_FwvK4IzpX1Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRTTbqw2bYHz9zEn1xJB8Y0g16p51qlkIB2KqGezICn-b2HPzUy980QPpvrux4ODmZC8QlxA44JDzkYdxHp6cAM9TGawmULGMyDP6H8_v18rLLorHCvwtW4R9Ys8Ubj1obg7_vQRXu0GDsvc_JQ_80YQ9FNkKnboeX645hDjskwehuqNMjUVYj4_YtimXdM42hDrYOXLe3WL60mFmSh2GX7keCTIbY3ZxMaZ67OrVH0TxLhrc79vk488UFkNzugXKA42IqnGdd3z_Ts4-KeiBzIjt9ASETaOuFnTHDZ8GFbXWZkF0nM7FP0BncJ0Ex__SzoMGqOjYGT40bRUlFCceQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atEe967GOSkyVzBoDjTvO0sseoRN6HvOzF-xqBZz2ZauUPsRXlv02Ut5kOMPq73updKbUPGrQ746YWNADBU2oH8wQ4mnBCJ_rlT1zopn5TqL8mcazBowq0eIq2GRn0DErNMr806uIuqcRqv58zqgW_znyUzsocK73Um3KtrZsmd5TzhOKYS_1AnA2HBkMggsNnFjDlkdeutFZAUou9QQAAulUxIYl5JEvRXDXlyVOQplSYdfor0SNQiD2SPgC3PB_AfcuD0QYV1LlybMyYpWLMpIsngL-BMJntfYkiGZycPXdwIp2MP1u9hi0CxXJ2VOg_A3jtOB3S5sJCGcWx-mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI_ZJf0nX_YQ6Bi98gE95YLfRS_CmCj3gmDXNBfN3PamJJgepS6_y5oZLUQSSw4TZui0sMTGFskfETjjox7g4bz5WjZh-F452Cq61VIj4UZXPJn_5KEhPs7Qia572A_dBhRNH2z4be9LXshrR41Rdu2utu8TUIKPZzzt5PH6DphYNVF6fcFVGg89gUjQmCGWm6Gf4P_hcNZfH9gUdid8bfYx38NPvGr9n2nxsnPn7QkHuYnq_Gl4sKVdYewpuD4ww1Dctq867ktyYtzUFjPRg2n7t9oFqcppTZHE9SSfUZxnk1hOkB9iARCMjDXn0_reF-91IslI6COSliQruKb1XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4TGpd7Qxo0fx6hqgIrR6mEiQKC9UN-dNywOExLzPt4mssDj5bCMv7lnZjV5MaWJSvVD5p9Rm-dg7w2Q-iRsT8a7tSW4hFEs5l2gLSGeufNJS6MVod0s9su3jJUePqQO6zJyWAbpUxzsrC6RRA-IoFJ7cpAkCll7FslmD2QOImJmSlDaBzaUuM2LoeNvJbW8TtY88VSVHs9HNe8graadwYlrXgFT4xJJlbJQSecaI8B48Y0K-MCGkyKYNV5o8CZXHEwfZIOvMqZN50cm8A8X8jzZbJ3EYZzu3kDGatN0hhrJPkcSEkujlS_RMMGzZDzwKCwPqsHGnzqlDVheMWTL3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbLmpXdpDfoxqpoSPtww6hBO_yJsbO6kmxm2MXRUsE7qjd8KBf8IW39UvrfmZqwRFZ-0dBTjaW7U3XP0X8dHPnvy9DLqczr915FlyroQS83xZJlj2NYE_kxIC8BTr42_jRCJqCJRAixz6rQghxA5QygVvKw31wLFccAlHnpfDP_u68xX6U3E-YSRCSK4U_FTqlS4sTPbu9bNED3TZBNQrW1qIUFOi9e53enoQoP6Pd_xktN3amyRwI2ynDaTUQ3ntWpC67x3jfq8y2ohaSc92EAecMGlsuGxD3415DMtSD5RZk3jJdrP488kWolK1EX6Gqvcaa7wXzYP9n55giLuTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ4JhCxNxOCdOfShuPbEglvbczLQkvTDN8Z0_ufxpkwM1auGYyBC92mzhl_RZn_kYV7eIqg5aFhCFvy8dfhHlLQBjuxC8csxFDcZH6SShmnM6tKktkJkYUtpzZv7EDzmf7PYU3p7iyfrv-XcSxfeTkP2AU8WmMukmhsezdNm-EO3kTFfLsEf7XNnGKV4RnB0X6gvNoOcZ6eDbh0MURrrHOoSB8v1IOLimdbkjIclMKwW3WEytDWjzNnzig21uNl5iYD0i416BhFzyLmkHoCuMMBJtk6iPBEUPcUVolNP8snwrnKZebbEu_IV37npvbC2PCXvaed_9QMN6qGDNXcwYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpF1YnHhLTssq1na0EiVV8YyRHndXCA7S-qEf8ZNYA-1GkdMwzF3CFwAB3HItyrGdniFLzmFiEqrhl_2b9-TPbEsGG6YLyrczPU1LGlBmKkoqs0AVEM4n9fUHa8NInPqVANO4QJ7w_SZ-heHg-mVXxKknbufNv2JaOckfwouCZfIfdHfvtZB_ixaXDU8HKyx5QrY4kdo6MXuvmSC2geedWeZTBmrlOUdH7enIg5I_k1NgLaR10AAtgp6QSiMXtR2be5IWt96X_NUK6ECZJlC5zK86f4Yjlvd1lsC-KtHcymV6nHRZgfr1XWBU0ZxfQ0PngWB0mkupJBpnJGsLlb7oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGtWoF94IKAveN1jDh4qqxrjsuPVi7SwTsG8rYGeVO5WKm1HoRb1rlRxRVenTWGqh13tgwtn6IRB9pTGWoWzX929Z5YMz3QuVW4yz3Gc3J7dMRF_-DUueVPWLD93w-IxY5RwV2mSQbgqU9jBS-CNdt6rOMEYBhDBjAFLdNr9DmmCPIDH-iaLE07yQGKgYZuP9zbUxSMqT-JihZV-RpcaLQOmaW5gM5DDfyNgsdDACXkLYmIVvEaElpW6LH7bh8EhsIheLa1Jo32R_XpwOVj2mGvhe84G67FPyWZ_qdOF94eTuDcEYBRXGNKz1jdGORfJs4gIo9xW-YvHdptJnZN0eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItfERMCg9Q-8M8wAlq1pksxYlH_0X1MYgw99zHrOeSyb5KrfvBLPw9Ty2wEhh6x2lu4XQo7Hk--t3XWdTkqmJwkg3-kqjCQwSLClxNT2z72efkHnORhUCso_AvDBKO3zcVfZvcCAXtMYzKXDT_0miPSbmzD1iGQ41TiANf1BeNu_d5_bKWrfORXAcH14eamEJAnrp7m7l3NYNeoxBPak6lCoCw_ObQ8spgNmBAa_ZrvbDbIV-mEfpNX7Ow8Y6Zw7FRSWvme9TRh9j4ShxruI5Q56-mlA4q-T1nZCcVlCI1P__9rhgeiYgzzrTUgdhWmzekxoRwssTtdUfKYPYn1Udw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE5QZ__FdPZS4w5jm4FEuuyyKSKLPHpTR-_aASsln15RRgBke6mpI_7LMmiVJ0GnkSoiXWjQJJNJrxVcXu42n5Sh9Q6qCZV6YbljnB4ox2U6iM8jVEZ-cQjgskz1zN17Y_aQnIP0tTq3pfcQ9rHjal3zhZQdP82q75D2d17RnXiS4U5IXySVAZMccGxCocM7kF-K2A-HMwn6ZKx1cl3Od-GUTZIhEjvtCbWvcj14s5wmw-iG-pQCmtYl-WZPDhpCti1kTIpQGXGHPCq_oOLZw8EdiBhJyD_x82er7f9l-jjTUK4YH148_TxlNtY6MkBQJQlOQ0p-7q5H8_wySIMgvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyXcZrI9e_53BTs88rWTH2iy50H8x1EfNegUeH_0Mdkz848Xinm6Y6khAlDIL84I3TMabVUD2e0e4vKzbQFVSu9umtMi9eOaqqq2mLF0ArDu4Q2gWVrxmeT-xeML238eAZh2JBbyiyEBfBt6zZn5QTimX47TffbhGDKJU23D8URHKcLmLSwrrs3k77t_OilximWwdqK2SLpLTEZ8GupnQOtvgpg2R5lBYejOtjrZPNf0H19qzSp78q_R94IMn8lYrITvTVmpUEK43PJT6-tVigTREd8foDdoCUNnLJjiDWi8hDXGF9CL2LdV9OiyZ7gWhek6Dkeoihwh2JPvhwf9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXMWvp0J3sR3UH2J_s-FhsqZYZ0osoV-scrD4bqlkQRDLG0Qc1WQrmCgpRdfxil06GvbzYQAcH-j5DMoD6B37DD32V4e9b5IwagGhu3vs6-sB-tAx9E8fROGJY07ajq91kYdECU9quv_Bi1T0KqPatK3brXjOQykohyH5ANtEVb1MgqrBpA2t48tZ1kT3YKi1_4yFC3HL91MaviyXMLxpyQj-JPtXIoY1CL9KwvUG6_nTUc3_sS9DmYF1l8vnS8g03FefkQOTC5D2SEFI1uD0NxpFXTuymYN0S6pTStkll4_pRNmCzLhQ5dr1-mACbkSD1IdDHf1nYmAO1vKmD8oJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA5Z2AWqbAv5SZjSPq3qLf0mipNaGonJ42RK4e2erw5tQ9UfM-LFGX2J65OZ6T5_D5Fyzia8-8MyxNfozvR_4Q_ftEiw_szh9Kb6s-U4Yc-pF-Ssx0D0KZh-EiihvYFef4XeRy3B--BGcCegY0qscb4BmDcE-KtWnJoJFgp0RMESYINdG9DztXV4HXecX9i6l4ipZbCYZnurFGvJtCBuTb5Z2SdWxPoepUCFChg20zdM66yB9QJRswDEhJc-s8pvcKu8U3CT8LnVkL9Jd7NrtdJz7n7xba-4ic_jJpgUJbSyG1PI43B2BPWVgG3WHiQOpgm4Zj_fLNpKwTLGse1SIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=dr22yErDY8VuQlwEnx5mz4FX3Juc0OPTDnleO5q1__y67JL3qmAE5L1-pzrAAZuo9hNPdQgti4i2Y6b8EQsKNddPmVdWxy7ZN6J40AyUB9chFH3NUrhx0AcaEWNVlzVtLDz8sB0n3owM3QiWpXL4UFB0W5XxtdlSnbrBgZ9LQDeXd2vBUZtpBN-dr6V5O59-gOxFBnu75V0RqhKUmIdH0qNcCU8VK1DL-Y3wA9dHfOOQFWcz5vjmyQDRy7gQg9-Fi-uanxLyx1muTJn_XwQE-3H68xsfI3hNhCE6gpzMQ1YuZ3uKuTz0ixguKwJ_URQmyC6jUHVk8jHyJm0GxJcRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=dr22yErDY8VuQlwEnx5mz4FX3Juc0OPTDnleO5q1__y67JL3qmAE5L1-pzrAAZuo9hNPdQgti4i2Y6b8EQsKNddPmVdWxy7ZN6J40AyUB9chFH3NUrhx0AcaEWNVlzVtLDz8sB0n3owM3QiWpXL4UFB0W5XxtdlSnbrBgZ9LQDeXd2vBUZtpBN-dr6V5O59-gOxFBnu75V0RqhKUmIdH0qNcCU8VK1DL-Y3wA9dHfOOQFWcz5vjmyQDRy7gQg9-Fi-uanxLyx1muTJn_XwQE-3H68xsfI3hNhCE6gpzMQ1YuZ3uKuTz0ixguKwJ_URQmyC6jUHVk8jHyJm0GxJcRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox7n-LeosoM45afkPBrrnFf0FuXcqwDMAGJPkbQ29sug5a4tmv-ErnosxMqNLJXYys56lIxdmmCVq03nSDZERCsTclUX_P-ev31Z8gVNRKiQJeRjDIUBGdvKQSevcQGFUXukJoFwpcVp2HjsR5Qf-2ctrJMgSTt8jkYU5_r6lKSPbtuWgE94XNjfDS2hmJrBETijOUZD5A6wavcYK1JJsytoMY41nAYOHzDCqUyHXk3vzgDAeoKajtpGCCCl4MU4gXcFwyI71fCqGEDX_rNVtznFAZ_OFu193w3_XDv8-abv3HjCq_yxoYgpiAI6DZQBC82tbkU7o41Jy30Pt_1CuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWfhN48aCHhZM1IvX4fFfGUw2ShPPB8944nIyHzJ8Oj48E2UJjju5N-Z-bTXIgQsfa6mGRQ_Q3KaUt_xpT5MPFEKj0cUTdvFZ7Pb3SpiXAVNpPr5J0ZFzHjS_c736sFu30jIL1PknPvkAd9EjztXpdZKtgWpiEXpeuPUWUYHjplGx9zi3cWOFEc-7XGD78djeF2YcyegnVt4LS8KrVzGS5928KZhOQIV5JOwkdWwHmN9HqNRrlakCcgu9zAUQwUdDE5TzRCK3uaVso5g_Q6Zz2b85AVtP_8QXV5x6rtCbtRSt8k9LcPt4XLh26S-45w1Q6sEmuTuKNeM9v3FZrHvdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=cZCR1Gk2XvP9X-9IXjCmkVVz6D2rziWwLCBnAFhYZSo8BzAcqdhoHgHJyBKz6JSiIQaSzCt51MrclsUOPlMAmBCUsIt6NFs8rOI8xQ921DejBnMLT2IOw5HtvJJ5JAjecRp1QIKnv7TSS0qRcBJ2Ne-Q7289VvtzUb_diwIHq3PPIWNz4TH-54mjRuCuOsParznLZIaXyZJ-BuG7KSPtQ78KBxXpTQPG0kqHefPDhRUUb69MbuQzhHWi8czROE1eQ-5LhIYZGznSDf8Pi34b2A3J9huRkS_AnKbjdBdKDJaVzSJdFBydNinGfaTiICuZ34IyGz_gr6bCbnIXYtVcjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=cZCR1Gk2XvP9X-9IXjCmkVVz6D2rziWwLCBnAFhYZSo8BzAcqdhoHgHJyBKz6JSiIQaSzCt51MrclsUOPlMAmBCUsIt6NFs8rOI8xQ921DejBnMLT2IOw5HtvJJ5JAjecRp1QIKnv7TSS0qRcBJ2Ne-Q7289VvtzUb_diwIHq3PPIWNz4TH-54mjRuCuOsParznLZIaXyZJ-BuG7KSPtQ78KBxXpTQPG0kqHefPDhRUUb69MbuQzhHWi8czROE1eQ-5LhIYZGznSDf8Pi34b2A3J9huRkS_AnKbjdBdKDJaVzSJdFBydNinGfaTiICuZ34IyGz_gr6bCbnIXYtVcjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=OqcQ2pTUo_lcFaRl87Ux1M7qOiipGiWKjwYc__RZR-bdmkOdLFCjUzGlNMRnEiSK_-MjbS4wy175hK6ZkGdRvV-UgOgeKIcaqByCTn_QnO_S58P-rLTRN7jxluKRZJLxjAEv4Vrscq8m69z_WKLdrerxwVZl4cFcTMRHVGXy_LXBuYcKgXewnyA0JoVj-ZOSLthAsrzPOS5XujtX3hUBx0kNklK0fBDrfGiMAuVLQ8H73OP65JKurPu7ejHKGgOZkejLE0pOZ4GtOJzWclu-S8jwTczirps-FpMTbrHW4Sn3SDajF3Uof0-vEUrop1Er7kvhrySlEObzENnR8Wl47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=OqcQ2pTUo_lcFaRl87Ux1M7qOiipGiWKjwYc__RZR-bdmkOdLFCjUzGlNMRnEiSK_-MjbS4wy175hK6ZkGdRvV-UgOgeKIcaqByCTn_QnO_S58P-rLTRN7jxluKRZJLxjAEv4Vrscq8m69z_WKLdrerxwVZl4cFcTMRHVGXy_LXBuYcKgXewnyA0JoVj-ZOSLthAsrzPOS5XujtX3hUBx0kNklK0fBDrfGiMAuVLQ8H73OP65JKurPu7ejHKGgOZkejLE0pOZ4GtOJzWclu-S8jwTczirps-FpMTbrHW4Sn3SDajF3Uof0-vEUrop1Er7kvhrySlEObzENnR8Wl47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=YX62wggRON1LKZdZMSeHy9ccX2NmYOk3LMM4TG2lQ6kwQv27AOyDGGBI6XLYk9WFFZwa-PMKBdZ_kPlQje0oUap37AN3kSHS2TOW-5dIjtpI1zZuR0-BF7Bn_Pmju1q_njD-yWr68iwZVEUtks9J7i-_ocdaOR12SXsqxnD7L5VEJAyomCa08aoCp36PE7ROs24A9EEynY0v17jFy9TIX8HSkQozA3awIbFARZHho0ISQWq0jfXXijdnBKms8aMCgVks4tmfLQm5T_DRJmhEu_JV5uphLV5A5tW_aio54ciznuObGAafx2-Qa2cDsEzc1KNjCNiI85TnTJ8JrWkOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=YX62wggRON1LKZdZMSeHy9ccX2NmYOk3LMM4TG2lQ6kwQv27AOyDGGBI6XLYk9WFFZwa-PMKBdZ_kPlQje0oUap37AN3kSHS2TOW-5dIjtpI1zZuR0-BF7Bn_Pmju1q_njD-yWr68iwZVEUtks9J7i-_ocdaOR12SXsqxnD7L5VEJAyomCa08aoCp36PE7ROs24A9EEynY0v17jFy9TIX8HSkQozA3awIbFARZHho0ISQWq0jfXXijdnBKms8aMCgVks4tmfLQm5T_DRJmhEu_JV5uphLV5A5tW_aio54ciznuObGAafx2-Qa2cDsEzc1KNjCNiI85TnTJ8JrWkOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvglW0VBMUopnw9jEime9VLOYFiOARy0Y89zNtVfONuTEHPEfbhmMHvbaoKJnIKPlWWv7CgXaHeOojTFI31NDRmub_wZkg3hoDBGNNKBhqSPRkmGX3sAv9v4BTWEoKePstQ018yZx1Ha6XiBJWCmGR_K46u6vPh_YxedE29Pk_VI_LgUawwJDMzC1znTCGQio7Mm86qOPALe061bNhDRxkpF_ICPgo8Q4jAFEW_SDjNMxzXDfDCLIRdlC-zXn4NqJ8olVSFyS4MPWxIwr86Ksa15pnotaZ6Kiun5eaMRQxy8vv2h9ZuP_1ZHqm4sPFX3YPiTHgTFAzspM7ypHkoHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EC3rqsKaGMrzSPwQSwiNGwIECugMvT-zVjJnqg7aVVrMaIo6oE1nk1CiuN2cmm-dLfBPsMRwg5ly51n4xeVDppKRpxnaK_M235S8J4Wqqp2rZDdIt_S32W-7M2s847JGAKd0fU-zmx3awnY2HQRIo9pjwtwEaQKKJqNdLcnSfZ7Mxohd0MWAhvgfuLY8z4cdVWopIfQrWAA2CdY7ZA6ZhcA6YgvPvL2QUz7Hu2LQPYfmtGkEMxs04IO9M0UMSslfK_Fa2LcA4DKUAVj5sh7aTjg4lJse1JJbpm5WHtE6fZO0_hdBm87hsskVcls-kMo9YbuHVIt9uJ4hax53X619Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EC3rqsKaGMrzSPwQSwiNGwIECugMvT-zVjJnqg7aVVrMaIo6oE1nk1CiuN2cmm-dLfBPsMRwg5ly51n4xeVDppKRpxnaK_M235S8J4Wqqp2rZDdIt_S32W-7M2s847JGAKd0fU-zmx3awnY2HQRIo9pjwtwEaQKKJqNdLcnSfZ7Mxohd0MWAhvgfuLY8z4cdVWopIfQrWAA2CdY7ZA6ZhcA6YgvPvL2QUz7Hu2LQPYfmtGkEMxs04IO9M0UMSslfK_Fa2LcA4DKUAVj5sh7aTjg4lJse1JJbpm5WHtE6fZO0_hdBm87hsskVcls-kMo9YbuHVIt9uJ4hax53X619Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfEY1vWjpX2-cqCPyV39uflbDj9t70PU0Zs4Xc5Z6GsLaanL2B0_p0mZWed3VXDBsKV_OLmrREBaFBfH2MZgtPQHmeS2MYY4e7N1gc9vPT7kXsaR9JPebkr1s-wWkFeoGJl4FhDiVv-Jwnn-KcSe3mDKetSu9rVtWwJWEH-mfiiLLjKTiId0N9rAYVUO5VbvZGz5HuLBddb8CoTQADWR_hlQF_ew3k7XxYQ6k9yc8p1fxSC2i16yPDBYCRs-7hoGCXkF6aruJI7SK9GKZIgzcTk_s_6lcoWL_SYerh87r6Bw2n9sfrKrvtw7GW6QaGgly4WGP7A2ysYUSqn3uXfc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2hOTTJd49xMV3pkc8xi4YthsPj8mozYW4Jb55LL51XgKNYiVLNBm7XtT78-hQG_482Vwd3nwBrz1Qv5DJjrLKdA8bnj-j95q1MWbsNcHkxFPEXDZUH290F5Nkb9zpYS62Q_mUS_A1QCvJLUEFR3p_72Gj5kbr0ooh8ClMDu8IZTaLAcwyG0kU8d6F8wDWWDc0Illd3XZXOu6Su_YI2rqmwhtUIDhhJAQLNeTVjoGbOQzf3NSHBNNI-UgpHZc_89AFV3JbBFDpMsIZUfM9_RJ77yroDyh1jJV3Z7qeLy1pO6b-J-TOEGuKFJkdNe0ulra6EGpw9HnEKPDbP165Y8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDsexw0S-lyH0g4TgXA2lnCGHlppP0u44H9nsRv9praFTLPMvgss_DzMdK5g1v-kkR9pqCW3b9ZwXMNmpzm4jSZKcpKr1G59JNziAq6FwTXab9DRhcj5VVBsrYnQ6LnmIflvF8IHQa3kexJpTDSOWMtODyEnMZcu-y6aQlz8zbm6Cc9bR17svyj75W6RFDx_4e2idCq_HBboSwXTd_cFhQt3umTkzYZrUrwYViMzQppGKQsGUtpt6biRWOBaqem_CrHptsZdbq6h8Asv24iXS2GJjRvFjU051ceV8T4DYMyIlWWZraSxdQ_7-_2fbts9KjBiwO2pNY-xJJkDCydq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxcIqWntxI9CrJ5HZ2z72UzKPSEdYNwfd72UoNJ67K-7Zc-ItBO9kT4mzMAZuqO55RY3iW2ZiLCCSQ0eEbzeO1TNslWt3W1Alz-CaHASwK9Mdwkf78BswTlBcvKbjgR_OWvEVjXcuaCGxbAtAiyMJ7atZ160XWaXPODxmZytLgklejQHU9l-KgByBVuQQh1DcEADimWCbZb1dUi4ilBkvBy3gIJ4tkLNt9rRtp5rgd9bTopu3w2mjaOPVTTGicrzz4pSScbcVhU1R5m9q2un6Ozhq5YCTxnD83cL3O0jiuAeXGo300GKGtwtfRmJSINHPUrVrSpZnP_r1su3NkcCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzsE0vBNkWZeH06ztvd8WrXNyDS2X6LGabSFwmPLpRjEtpgY8vLBTj3gNJes8fgW9UUCYLGfpT7v3Gg19a4BHE8F6ZF5yQod89n57wo_SnWv6oX-EGzq1RB3g-KT7V9l79kLb8zL1JHFSYxMxk4yHyjUjLatT3m_wyTqCJfWXymettwJF4pO-Uuy-ztPgg5u7_zadYP6_JaUasoWhVTlVr4QLoyonYRoRgJkoqY7FtLjekVElOl6H26hlC17m8E20fD-JCuXV2_86Z_t2DeIU9eRkryqJ7YHZYKo6Iz6gYrZEqhaKssSGcznLOWjd9YM0h9qUduMTbEUfvosZefxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsub63N6BOAYWnufe6SWybzMyYl2_IpMRdCeyjzqMxC3OxNNN_z34tmqMbLdKP-IKqYYXDXNOEdkfJgd9-uF2RpRw_GH-qcVmyXrGoBb9GBiH8CPp_PpszMd3fRBM4cRoEQqWX2IpCbjrlf3hXwnLD1NObhoHsPBs3AdIJ8Hja3Mx93BJIbLSCVp_zklGX-GWbuRVmLmGjqK0SYqYvLqennKHq6eSAS_rOudLXdlmvHUJsrwuVeagUT_zgqJaXAYRz1UOMOnpEs7t1tAjeiS8WUvb2W9d0-xmpmJS1qtHfPfIp2zNcM6CrhE4FadcJK-pd3Vux1nUSvwhNsnqCQ_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaLSvol-HI-VvnVh5Let8u8ZgIGhOFCfGsxEL4laPTF414IohMIYicChUQJvfUqidDtqw1F4YuS-GZmrXVrzioOxFFyxE-mkqM4wsLqZceYPEf0xwOSciADDXHM5pI56yRfO28N_nL9yRE1Md9oG58M5pZoULyBjwA16LkVFIk9aI0TOdMudumRkxY0boAImYXy7ZP0xMV4_IFmlB8jIvZF-Xq5iXqB_i9sw-PIWNFD_J41JT3QiamhUy5sDx2yDgfoGCys7j_D7smmnbD8X7ubzu3IFPPh-LX1y_PcYASls5WarcGJGjVtTHWb0luX99fBkurWk1wIvlU7ZmoXcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JepJyQGZwfe-tKOYtOsqIJmGtOmZv6tSnRfMHChM3WyoykAClMsK_Rt3V9pq3KWsnw4VVrqLN5QgA-XhRpcvg83p2PxBm1fdhZhCgurWxe-A_Mzy2jPNmWNEym7Ja_RwspADAkYEnMjViM-veEuy234AEawy0YBPyNlSAe15xkrtD-clv809C6BAjGDe63plC1YjqfBRjY71tbK7eNLufLcAji28uoVtcIthzlQSiC99QXkNJpcnu_b52NgbYz6zeck8XFeBGsKWIamqCV9TgwaQqKg0H0Z8tkJ0MgDkzXDhD7hCfnMnxSA6ysXdL3d4RgZmh2gALHmgBE3IdStzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzbASBrkSX_ZPkeUM_y5KesThyTkLTOj4VCBlO2unP3YN02W-jd6g_7jynWKkePakACzDsjoffEi0zIh-rwMQk7wQV4xFFSGO3C6ReO1WKeT8OzPq2kkdBZyGlMdh9tchuG1IXoGBBei16Muqui1j0yFkXgZ4qBbm0pvzCn7mxQ7ZgviwKoaF3JOTIKNWnU31dHapMqKchO5aioMn2VnbS9GUWqCDrxOHUg6TGc_VmzsZJx1ZvvS9lH5jb2MZKKG1dn0FMtNs3ObuXhLb8BqKcG4QgcpoIOJVM5FpJ8pvW9khuMnkjT8I8oJL22_sEdNQv3ohKgQ-OKLVur9wz-hKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6mgk_8Td0lTQ_ta4Fj2cm4Zyx0PaHhNbIqgVlNVpCEwRuL449K19VboedXbvRpG4LG7QTvANqvsN28G4-t_Dcy2EpaReK4fh3tks9PnPlx6jfrlVfx_gfafdCMEKxj6_aINA6bQsgp5fzBdzbpDopaOoVlxpTfBaQYLsjXnzZSS6gHzpG6Xa0VV4G478Pwfvtt2jJillYyEYKXt9T0l2KlfRhd5AwNOHQqaCMa9luZcHYx7QdaEgz-8mOFUkRlmCPfLO7Max-ldfazvbYw7uEav1siiXyQKzpNYrcRgueJXAOYfv_vUSRlrmGytdvKM5ENHWQ9XjWqDhPZb9_wZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5YDqns0jDijWWpN8WNSPoVhclCqqRnc3Is1XH9TeliOe2UtCYYh4DTLGynSrrY-7SuteLe3_n989BpLoPvwpNqr_CY6mWpZ2yb93JRKkJKuAbIl-_UKev5Pq4ziwYQFoD1xMR4p4DoOscoCKsL0WzUQkOI6VFes1V26KDVSPA_8seq-Ju_5EA0J2c5WKtRiwcdw-VOjGBrwCIvNyhb6OFAogv_jiKFz4f4JOla2kyrrSOPhgKOHdsP2cwRLtCRFdyiEm4n7NFetUF3b8U7QkqPpswoyeAEm2O7Tzc_0E6-JEdfKoqUYlCdfoNnF0HwDepxDW5a5fQZVDPD-SFgz2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCA07jxoiqZg76GcpmzfrnYxjUGtmQZIQ1Nh9hmKFDBJzIVfqDOmDlmo2lMUreJ3hia8d2835-leNBDpW808V6Wv8rau0j0B8sPdw2-R9-Wq59cu0TpuaZG_AVijYUH9koF4MFruj13wiivXvq93so190eB15yTeRh1UF-Kg-MM1ez6zKX4C4HdZesnIbMfMTGfKIgDNIfM0qqWlS5b-uLIlkErCXr9cAAcWJ3nEksfmmkIUOW2TYJXk6fHqKnWndVsVz-AAWqKF9NzpB4tFmHXyekMK7lvDZa0iTOcSd2X5r0N6m7XacPz3_WXvJ9EXQsRO-X1Xs_ZL4wbLxfZslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU1SbO1HxVwIFT0kwjKglHvMxtaaiamN69Twg77j8eIHCOczaQKf5pa115GXC_14igbNorH1yrMzKDjH_mHKpEhtd1D9oCPnCTDzfLTKNkGBETCVgu6lY2rRwtLDJgpQIz-iKK_G8LH4x6hZNYUvzKhv-_9N-rguyNvYX6pBVM9STOSOlRk6lVcsEgoh3dWZ4TQrmwZq3kqaYn9qj98oEMwYiaKRA0u8hSch2v8JiuGlnNsUaIor5bLivT2t_CHDMVewKt7IBnSE2QAexNfq5NiYAkuKX74ZkMOeTfOnEPeL8GE6tIY9nzOSJm-eRzSXV9FVhiauh7NPebOp4iF-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlA4kuJ_2AU9Qh5K1HUvkveOfgfeclJJKqhdhyC3_KRHKsom7RLxCqgvA0SZo_lrTp69nQEfHXPtna-LKSusNzakN-kpj51TfSiawSb6vu3j1HiZJXVkPqMZsPhXeFTClHbGM8oDcaJCvN2IQ0K0RYXPwkTNRYJy1oTFFqr2CP5G3yXY-nntsrr6DGxKGSnF418OsrxtgjAm7_aAY92ooKrswm-uqEy5SF6H3eE1q-RB_rMNsD7H5RcJbP0XYHXyJdYSwPjJSD-OXXlQ6GuJKKm5tswHGxyPxXe8bMLnuU0U3gyvW9tfDDAeomm6x0ZetBq3aajeZ30x1SbZBloPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1gnH9walMd1wMArKhAhxVegg9vx3a5rjtjUDAw6dpt1Du06T9qD7r2NTENYLAKyhyIQ2lJuZ6Js5v7jngo31CId2WlaqHUcI9Ic6_4avUtpuDyhiTTf5Ot3dY_5uNBOqdzvdtCTUSsFqbXT9gHx8_mZOM268zHS5IAKTMYu2UliojQq2d0CwxdQ4NuDfP3p43C7M-tpLT1BM0noFJFeiipO4eOiB51AL5fi3Zg1lnBj-4Fwnv9fJ2PxZ8G4oysDLGw5ZyRjeMOvECsdtXt_m-q1uPgoN9nKIAuRMW0dl5A6b5QOMati0sTub9V7oxtqU-zoDDBo3Q9g1jN7PAlmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oirmrUyOcQvyku0hpA1iyYKmM0CJOZyLh2es_DqO2rTaYjQRFalFmhJGRgsdWbXxCzR-1qdR-gk6bDlbd5V03XRA8iQDnfpwgJcuRkCWd9J-Uthhg-aQqHejZiKTFv6qgiwr8q9DmQAYUCrYqTtkzaLONs5qf3xgGPypu3zvIYl7Rd0f7jAu11JEIssjoXAtWJXsNPMK10wjKRXnj-lzZTeZ5NmAmuuihWS-jH37Fasq3xyWPVu8h6TrbaAc321hkKDKQzldIuaQrvP0TdCxeXyslriQBbck2V-4mImdhwpyJWj_Rnh5qLOEKuerBtfay9VxlMnaUzJfFQ7hoe7gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe-Avb771D-eB-eomfFSZsaFm5u9WzOW_wJYqcGOWNEPGfCspMfye8UwwJfEWLBUlc0i63vX9E3yzkmy77eLL6NYXSdVzye1Ap1-GEs2yLlA93klDvb1DhfSZ75euEeZq6r9XBxhDwykFJsTgCMQZoBWDyuz5MDREtdhGih-PNsLE0SOBpSOXADyfJOp3N0vTwrJLeHXtTaML4jXUzWv62Y01gHtayhmr5m1vP89GcJ4jnEM4w_Ik8hN7eM72UsEzveNmHtCuVB_XSzs5sTQbq6xytpXiyVVYdXD7lTu5gE18ei2WZOYo7wK8SYtphLIEGSj4OiqPLPJiwoL2dV4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuIbEnKLWG8USz9oPWxyhnk1gPEsHYABv7U67CdrFLGu3DI77K-UCBK0ARaz0y6WbLnV23VgMV99APr_LOnNfhgDga0Viz0wsN64la90p0mC5XIF2cftZIT7wQvjRGXg-5GQWQw6dXzab7WtWWmQUkWXHJC5-sXNc72avgBbHu-5ZuVBRuYTBdon_QmFWVJMQvQXzjjkcwL71wJgzNpJrtR12iJuokig55F24sI5d0BEzuF9HYw7KSXQUt9qf97s78uFz9mfPuIN5RI8GLEJdo5MqiMqC0CLJLtUn6NiAE5mJbsQ56IYDH-_ie3wowJf0yJw83EEQLWY1aAyRDatqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=XSqyhvktjp5Z8FPCLclDd0tarS5JiffWuiYckp1Y70N_42Qj6b_8tYD11lZ9ymoHD0kSM9wlXy-_Ji8QT4aBX8pSe7ghTiq4_n2IIDW_60R0F_k6HbpDuRO9Zx7rySyOJNkxxEuTi1n0QggmiISyV2ZL71Exy6ChtKnxHoFzKTWnFSQLENOd303Csr4I4nP8FtAv-QrWdvZDvw5J5kRgqajg6hOx3TV3hbqlIDWH2bn7Bqiy9tuNvGZNBpSpJiBzcrHa61TchXFRW2ADrrb_cspWEpIhGRsyzpr201jTslJIXl4EzwP0GgAoW4fUwjaOQdgQ6IUQmLg2KS3Qqy7hBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=XSqyhvktjp5Z8FPCLclDd0tarS5JiffWuiYckp1Y70N_42Qj6b_8tYD11lZ9ymoHD0kSM9wlXy-_Ji8QT4aBX8pSe7ghTiq4_n2IIDW_60R0F_k6HbpDuRO9Zx7rySyOJNkxxEuTi1n0QggmiISyV2ZL71Exy6ChtKnxHoFzKTWnFSQLENOd303Csr4I4nP8FtAv-QrWdvZDvw5J5kRgqajg6hOx3TV3hbqlIDWH2bn7Bqiy9tuNvGZNBpSpJiBzcrHa61TchXFRW2ADrrb_cspWEpIhGRsyzpr201jTslJIXl4EzwP0GgAoW4fUwjaOQdgQ6IUQmLg2KS3Qqy7hBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqGB3q_jhPK2i-1uk5xtdgfbt2afzWFYlhFfetNy4OoQfS9fhfyvIPCN3abJCBhW9_Nvwdz23w_9HFdFtELJi7ghah9RtwscKkdVqEtC6MYlF8SyLHXeH3wvKRnHVg-LoUKOK5riuj9dLdJe-VpFNinYpRFM765xMH_6HscWREwztK2OAgZBDbyi15RaaXLiCNT3z44tk0nxLT2VCyJrPYiZFy_GTKb9bMC1q2vydTZjKaXSTbQeOkoq3xlFhLhh0ANr97PSh8XxIZfiboA57cYM6bJhlnXVocgAWjnS-agA9Y9hk9lp3gPsZJ1bU_uPwsB_7NPJQVHJEKjjbMPQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=PCbmWCevGOVSJaVkFzzSLUIdSjzdQkMGC5rTtA4QG2cm9ucXfAJ1d9nr_PHr8UfvOA09KeVnLAje4H9kHL2KGW7UQed_i5Z-RMhYsOZoyv_8TdvQOrkbN_Jfu1qzAsCTMIi3j3U3RyZZRzyxDO-C50VL5bsqKwwp5fl2DIQacHhhc5b-h2nPh7Nq_Cgm1p9oT2lRIVJ13hE3dzjUW9UwrmmggbYSl4v3G28xG0YcmmAhKJKEAGRQnCSD2HXMK1IiBnADWpmYedfDd4GZ1k7d2Cqb_ze7gP3gzhMbzRoCQl3ocT7I-GU38P4seJdz6IEFM5gj65ylvNf2urboBy0mZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=PCbmWCevGOVSJaVkFzzSLUIdSjzdQkMGC5rTtA4QG2cm9ucXfAJ1d9nr_PHr8UfvOA09KeVnLAje4H9kHL2KGW7UQed_i5Z-RMhYsOZoyv_8TdvQOrkbN_Jfu1qzAsCTMIi3j3U3RyZZRzyxDO-C50VL5bsqKwwp5fl2DIQacHhhc5b-h2nPh7Nq_Cgm1p9oT2lRIVJ13hE3dzjUW9UwrmmggbYSl4v3G28xG0YcmmAhKJKEAGRQnCSD2HXMK1IiBnADWpmYedfDd4GZ1k7d2Cqb_ze7gP3gzhMbzRoCQl3ocT7I-GU38P4seJdz6IEFM5gj65ylvNf2urboBy0mZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLsSEIXzjN9CGmTuiOTVQTgpmwmOjwofuipD_WJ2zUTgwari_K8M5GHnJljNymsFLLc6bjk-HlwymiT6o_lC1ri7I7-saKjLucaQ4Q7b39rny1LajfqbOoQ-vRpwpY1eYesv-BpM2eLE_FAX6awbtoC9_VzAGIEsdWbu9RIb5E1VYWEoIlU28u8-q6tjRgfkOkEP9qFJxSV9DzjK-vISmHt_OWddkaV_KXp8Zr_9ESheoz1jrGP2bN44h8bG4Aq_ZOUfoi3DnpzGYfqVgSjbC2Kln52Wj1yUCfT_dQkidrqRzKLIOjl33E0OCNBHg9abkyU6J1K15qXIHHmnnnd8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxOmKEnLlfZhHjdCL1kMt_YlyNz9tXtaBmzFfzdYdlrUvFXLSzqoxrYzLVOv8YtpRy_QbeKBHN_9p61HeskJy9rYHWOQapZtPHsAJqyGs5iTtxz9OlcWOCGoeoGtAoMzZXYDH6kRk3juekj7eVUtYsdairnKs8OxOLTCXEUPtCy0XEPXnB5UjjLqCt2fA9mQvMz39woUN2TRw8VXGIN4aFpa39JaJhWNz9b-4qFiiSoI4fqS9qd5SKTP4GX2onRO_dMNc8UHGrSJANDmXlrwfgRWW2LKmRBYLvmhEq1wgZw6MatwJyCam4PHFgtE7r51wvrMaA5XZqDk82MfUK07hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lgmu4ci2nP94MWq3Op5AaQq40-JTOazgp6LKx8472BMNiRtigL5_PmvHF4ernWe_WhQqwQ_QxJIQhwuxuyUE1vixfN096InJqMpzC-3Mw52iv_K0Se1toJsqgWbh7r7uQ-WBeq5QQUD_XxHhYMkd0n7rSqiw3u7RKuy9iAFnW1hlS_RYymPt1hGj5yH_e4bepnZ9bioCsFYKG0tY9ZyKn2_7H83Wk6TGdwcjJm1JH7dixVLEYIOfrwYWJlTAl0rEMVG2zbeq22VGOpZwvWWseyNeK0D_QbhKz2LZQ-Dl88Sl0xsXj8RctSQ28ARU2UNtoHE15c8oP7m7Kl7dqhY8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3Ha2f12HlOCOOoHfXLtkA8X2MzBN9tIxdEqs-HbdB2ttsnPY-4zdN9ViKQkN-380Q-R5dVI4M0wZNSTefPJ4Y89oljT0xw41yiaS7rwgOr4W81wBaz1rUGInikDXcb4kFUphQl5jGm0FZHc-TaXyqPWhsGtoNqAdOiYJnEwpUCR54V5nNNYSMOzY5tGFhyykoSv0fGc8kyfdZ_TvELU7oY_tPiEVyeBmLtgDmt_Z_V9UuheChLtgfMbUGge5ilZbxiAC5YPvsmiQlTpXGgheRZmgv0rJB0fZrJgBUdsnvf8ZAhNoBFBqg1R3dWmBuSjzGx-ewcnTC-GNdyuEjqy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIFSI2QTC2g3JN5rSGgN_wDlhCHpv01VB36C5zuEGokGkPeuLqBGMrLiC92NpDLQxYIsJ7r6CsAs2Gn3vq9I7D2xYLuVx3dP33xWADLVXsO8Ht0Qlg16cXAtZgZNaAEr37rP0HQgx3HMl5v1hDlIhPKq-Y7V3fmaojCzkB6oyLsyFS9gHV9ei5eMdPnu4Vb1xXjTWo3JFtd07fiduzQwvJMThjpeHT2n3RPnludyAp5QnMoP38CfrH8_L0NC5XG51pVndVs85knTraD3QNSDh_5tChh1ue-GTY5GtPvzr77ezVEVpGtw3tkjaft7TqsuHgOA3JDmZHQSqxf6PcjfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifH31pBtutXav8rOupYGH7TbyTp3UW3kyRa_Z5neK-NIuxr4AbqJmC-4lYQ7ahWwtL7hFKgRVVY-VvJJ4Ql-xysupjYHCuauEf4R7WIwtFQeEuQsJ-43OMovCtNmz-kCTcyxHQXLh--j3JEN67pD6OArASXocelmpjYDTzp_800Y3Nz5BYHkIZlVliAvIEHuuxMewxGGAZR3QSlli7SIQdoRzUzM9SbvQTBdsjeDFx7gc7Rk4Dc6aO8HS3rmedvg22DU_CGxY_A1gua86zaSvFqVEN4966MH9R8_nn-2K7bBnvQ2DgpdzbfQT0kSQLMvYGTdyEpTU7B-nZT2Z6E22g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwodLTuFpaDJa197cIwDAitpQkjgomQ03W242JSD_vWXryEXkYl3TGcY0jBHElr6TGAM5wDQ3HkHvFOhl-AbPVBFvpV691zLTiaqbquMr3LmeVpg2ILYLlpGAG_FLNii2urKCFAnM_PYcpmEJ4hyesAqTBzIvlU401r5EOvz4MVywH7PM8r_WeGAsuGgyk6wgIAzqiaU9zrJmHNnYWHbK62kuxBCU0mwAOdslQT0GU1mVc9SE2xnTc81Z9HC1EFPD0wfGbqy4cYXcNS8pjExNO4vLtYWQ4DA4XZ2OLLMRGg-2sxyE3LFTHTuhlwu700ShJHZSWLct3nHkblY-t6DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9gXlK2K0m0rMhC4XRgWY7dp95B6bJrfaDDtSYr5t4u6AEsVJnwP_fEw4VxwaHGwjjei9mH4LtZOugO_0TD8Dbio71ecT860LtyRV3fJleM1r1QAvCvlPBHmBLZMKCv5vEWF_1q-tp9T7pGFx6RVzyKA2qkOFeHiu-TFHUIJGRmW8ee2yzZa_06w-T-3p4AElBaGSu9F3SWQqRnLWkbIt6TwC0w0PKsBKc5YbgsbyyunpsXIGMSA-WClHufDt_qA381SmpvTNJrRTg9QxRIYqoMBeaXIM8Wk4cPa470n8EuRW1kp7np5WkHYmtAC_R0EBc3T0SnhT0yqK37xpq2g7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAWuuAaOLtKLbfkJW4qgTbfK-XLUt2MOndFZDwu_CQp4PUt4AL0fWRQvVk2KmwknjC6x3JNtClM1jRksgV80ClFq3c5YfTb8CqShg_Vz-jDhtHS89i69ACtv8bkKDiHqCdI-m3aeehORPi1H4Iu_BWF73ff_lCBDod1k2nO1-20Idsqph4cl2kUwp3kdmhXayegz-eED5y_C7qsavMphny3H1EOxICRKogx_p5pGUfoM1_YrhfAnXJZnclzHmXkDdx7Eqxcu-Tt3pAoGkCL2DSnTy6hGCFDwNbXfaD0kxY9NU5uyEaqKUs2g2VTVpcJmsWIeCUmsAq0mo9WshsNQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7n4WOEuee_-0v-9DWMzLO7iMTsgplMAYn8oo7qZNwsCn5onvmVHrXgkQ3eAuy9BlqD3Kc53FHyoHPYjWzaNXiakZ-maSz4uFrCvgs-Y42jR8YabtSqR7muktChg5-UTqZBDdhc8dhD2j9XLfwouQodSNfiYR4PMhc5a4r_9DqpfiROjijb_CfOFuIy8EHyqWwByIqb6iBYX9wsIEfzzHnZFAH2p01B4wbS_-loWEQSwNuViktU7QlpQtiglM1RNfGVAR3IWBbWvz5eV1HmyQORq_AIgrJxoa0D1uy_8e5pOnNDaTbIwzaYmpaQyCcdzRG6RbSdH4bZZWbHYRNFPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge2ZWuG665i0CSkwEg1k7F2oE_KEPR9ph_wo3R29mP64N80zSIOG0zMxWnAj29_BGn47mT4Duzm__04m0pxFGbmoKV0oJoHJz_sHpqCXsqeYMpdEM_lbjr3DAw3-ZhcOGUTGySciqodo2KXt3UY2zbLEgEUvv_u8wZ4pjmtF6iUNhwlLAQ4RiO38Y_BXrj75aKPX0UsNMl-PexnPJU8az5tQdqU3wMz9MTzwrcuAF8EqQ-HJscw9j5WzPWC4OUFZgadY28YGBrozyFyzEp7LXrqXTCKrWEE_mo2gda0yJYL678UdwDLdIaQDd19x9ludCoyRG131_RIe5LlQkPi2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DljhUObz4t5dxhZERFWqcTIoUgI_DQpxD8_S1BZyQIZ3o1u87VIN34oYYxAfE---7-O7UFHt9aGckqLo6s4qg_ZVesR3LGM8OC4--XTfBaanp4cOOY9_2mEkZvAPB1wX2GklQLauQuDqQs9JrH0KxhVmpjCGhRi8ycOlE4lYaDvyJTN3wkwJr_MyXaV8vZDBneeJ_L5-N6548wzNeWPlZVBh51nSV0axZhOLVUjJreHTo4s7QwFJ_mXNwO0GLvlBr7_8ePbnKChGRt2RJjY7sHWQpJA5ErHwrbiq1vph1zYUA6G-WZnHHPCVlgVzjOu6eSScWuNaWjLx3jL9uT2WWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfkYHxUrbxKZsqaE-b7Y2KY-xKpNr1BuB8bEeA8DDxT5ZMOKJMjxOgdbw_s-KWqEJ4CQ_-u9wFOfx3py08LUiziWHsVpZASPGHYi1jb6csIVF7EFDc3jsTRbeyt8u9s7nB5P8XRo3OeRoCoW6ced2FVFfk3bRJHJdhq9sK3C_r6Q-fUQdtCeyFjtB2fF32XW4Qp7hfMRcyaUFEnfIxOX3UGMEkH0_40HA-9UKOQpV3ndHrr2xpmT4B1zxsmrwyWvKFlZ4GWVOgZyq1pvRoPoWFctkqNQ7PgqURIkWWRp9b_DYtxGgbrHPnRAborYf2LDEPAF3o5vc5ieG9cy5hcN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=aeO6XBD5QiV8dnu_0MJ5RCbP__xNZrz_Pp-caw-0tDzcxhORB9iCji70bxZQyUAyXzjf_2HY1mdzmL0lKEXlvGIg1DT_xpJPSy5rj224MawfRu-y1UeNvBLmuwFK9M7qGWrurW3SxG_pXbQYGihkIlYLKljdF42yArndWITUf2y9y9ip4iIcPqMA4n04ioF48RvUyxLlqqBaVosqV-WBGw53bRX6DrYG4VWSwnn-SmOGUimzFuiy0Y_mq9H6iet-qWxTR3U17Th6BlCHhE5R0dn7Ncw25bwgU8s9MgG-ruXxGLWMLJT4axghuWI9jIIXnbQ592BL1OO7HuN5NUyBtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=aeO6XBD5QiV8dnu_0MJ5RCbP__xNZrz_Pp-caw-0tDzcxhORB9iCji70bxZQyUAyXzjf_2HY1mdzmL0lKEXlvGIg1DT_xpJPSy5rj224MawfRu-y1UeNvBLmuwFK9M7qGWrurW3SxG_pXbQYGihkIlYLKljdF42yArndWITUf2y9y9ip4iIcPqMA4n04ioF48RvUyxLlqqBaVosqV-WBGw53bRX6DrYG4VWSwnn-SmOGUimzFuiy0Y_mq9H6iet-qWxTR3U17Th6BlCHhE5R0dn7Ncw25bwgU8s9MgG-ruXxGLWMLJT4axghuWI9jIIXnbQ592BL1OO7HuN5NUyBtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=HNx4e2Y5HsKIRJ-jXGPZfgz4zMFHSiXc4vy35wxiYkb4LLrr71t7Thw7ksruxZRSfh0NcEXghV5-tf-2BWEk8nAMEPJ6hW6ukz95xcz7VGZijswE8thAEJEwf4pvF1gdBVzaFKwsmEi41R3L1TQ_P2M5yVsLkETolSaellqYjTqVut0YDfTZzzjixyvdwoe_gx4hQg_X-Rb0Oy8Cruk3xNw7PfOSFsmGQU3N2ZCodShOpetrKgsZzmqwPr61a7dOv6gnRdZWQWA63QgFQ_OabW7I_yEORPqL4pjm2JAtm2EGmkZKQAn45Z04n4pAqXyEZUTfyZXOuxx_mowPY1FkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=HNx4e2Y5HsKIRJ-jXGPZfgz4zMFHSiXc4vy35wxiYkb4LLrr71t7Thw7ksruxZRSfh0NcEXghV5-tf-2BWEk8nAMEPJ6hW6ukz95xcz7VGZijswE8thAEJEwf4pvF1gdBVzaFKwsmEi41R3L1TQ_P2M5yVsLkETolSaellqYjTqVut0YDfTZzzjixyvdwoe_gx4hQg_X-Rb0Oy8Cruk3xNw7PfOSFsmGQU3N2ZCodShOpetrKgsZzmqwPr61a7dOv6gnRdZWQWA63QgFQ_OabW7I_yEORPqL4pjm2JAtm2EGmkZKQAn45Z04n4pAqXyEZUTfyZXOuxx_mowPY1FkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
