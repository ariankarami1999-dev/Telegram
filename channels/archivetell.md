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
<img src="https://cdn4.telesco.pe/file/Gz9shs9pNYiISNdsjJ5xVB-h66NXUr4hHEhLKrx5o0wWAabZH3WClvprOIhkOqs1QWedsiOjEd3d-ti_GLU4iPm_IPemKFgLZi9ljG_1TtPkFvpDDZQdvuwQn23n3CLYYqxh4hfyduDf7Mlunmn-S-un88-hQJN3Ocgtj3AOUoYogNqpw-SlknhAugIi9Ee8aLWvnB9SMM60LiAJD0RqbBZTZV0eYn_7wL0qoSOr4qHJHGmsU1nqV3mx2a-ncVWvcHTVdRtd5iRq0dShwIAVNkMRTjZLTtuk1mgXd3q5V2oVUcQ49YVKrHtQ_jzOKpBbRqM9Se9QN8oKE9E24blZ6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.84K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 19:15:34</div>
<hr>

<div class="tg-post" id="msg-7089">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZTMw-SNHC23jLzTnjJgQKv-BOcjNweXUPVbgU2xxJvNVfvwvRISvBTGCcA3yiiG_eZ5xkAAGrBLV8e-BIeOipyVVdDQh_CXIrSVph40DatifW36JeNOopAgmutiYJB20KF9CSa6aYXDlD8dXnh0J5vBp39dby2jiWAqLORQdsegje4GGAeenj5CI164cZnw-Vo7WM0MKDIboM_Fo8GfwxKze5qBZxresU8Y5o5d4X8oY1BdbwOlpY6SzZvuvtZrEeD9Yl0aUaNbG21iJPc1O4VI7KDR8QeGprzzVRDe3xpoGdz-aEPvWqs9QPUb-dy9_NWkSiaGpMfrXlsSAjDG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ویرایش عکس در مرورگر
رایگان و کاملاً محلی
✨
امکانات:
🔸
افزایش کیفیت تصویر.
🔸
فشرده‌سازی بدون کاهش کیفیت.
🔸
تبدیل بین فرمت‌های رایج.
🔸
فیلترها و سایر ابزارهای ویرایش.
🔸
رایگان و بدون واترمارک.
🔗
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 121 · <a href="https://t.me/ArchiveTell/7089" target="_blank">📅 19:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7088">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🤖
دسترسی رایگان به مدل قدرتمند Kimi K3  یکی از قوی‌ترین مدل‌های هوش مصنوعی رایگانِ حال حاضر با کانتکست عظیم ۲ میلیون توکنی که در بنچمارک‌ها رقیب جدی مدل‌های پرچم‌دار محسوب می‌شود.
✨
امکانات کلیدی:
🔸
تحلیل داده‌های حجیم: دارای پنجره کانتکست ۲ میلیون توکنی؛…</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/ArchiveTell/7088" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7087">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🤖
دسترسی رایگان به مدل قدرتمند Kimi K3
یکی از قوی‌ترین مدل‌های هوش مصنوعی رایگانِ حال حاضر با کانتکست عظیم ۲ میلیون توکنی که در بنچمارک‌ها رقیب جدی مدل‌های پرچم‌دار محسوب می‌شود.
✨
امکانات کلیدی:
🔸
تحلیل داده‌های حجیم:
دارای پنجره کانتکست ۲ میلیون توکنی؛ ایده‌آل برای آنالیز اسناد طولانی و پروژه‌های برنامه‌نویسی (Codebases) سنگین.
🔸
رایگان و بی‌دردسر:
بدون نیاز به وارد کردن کارت اعتباری، همراه با اعتبار رایگان روزانه که هر روز به‌صورت خودکار شارژ می‌شود.
🔸
دسترسی آسان:
ثبت‌نام سریع با اکانت گوگل (مدل K3 به صورت پیش‌فرض برای چت فعال است).
🔸
پشتیبانی جامع:
قابل استفاده به‌صورت تحت وب در موبایل و دسکتاپ، و همچنین محیط خط فرمان (CLI).
⚠️
نکته:
پیشنهاد می‌شود پیش از اعمال محدودیت روی پلن‌های رایگان، این مدل را تست کنید.
🌐
وب‌سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/ArchiveTell/7087" target="_blank">📅 17:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7086">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 33/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7086" target="_blank">📅 13:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📱
اپلیکیشن Aethery؛ نسخه بومی و گرافیکی Aether برای اندروید منتشر شد!  اگر یادتون باشه قبلاً برای استفاده از فیلترشکن Aether روی اندروید باید دست به دامن برنامه Termux می‌شدیم. اما حالا با پروژه Aethery، این ابزار ضدسانسور و خودکار (که نیازی به خرید سرور نداره)…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7084" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌐
معرفی OrcaRouter؛ روتر هوشمند و هاب یکپارچه ۲۰۰+ مدل هوش مصنوعی
این پلتفرم یک درگاه (Gateway) قدرتمند برای توسعه‌دهندگان است که به‌جای درگیری با ده‌ها API مختلف، همه را زیر یک سقف و با استاندارد OpenAI ارائه می‌دهد.
✨
امکانات کلیدی:
🔸
مسیریابی هوشمند (Smart Routing):
با استفاده از مدل
orcarouter/auto
، سیستم در کسری از ثانیه پرامپت شما را آنالیز کرده و به‌طور خودکار بهترین، ارزان‌ترین یا باکیفیت‌ترین مدل را برای آن درخواست انتخاب می‌کند.
🔸
تنوع بی‌نظیر (۲۰۰+ مدل):
پشتیبانی فوری از جدیدترین غول‌های بازار مثل Kimi K3، GPT-5.6، Claude Opus 4.8 / Fable 5 و Gemini 3.1 Pro.
🔸
بدون کارمزد (Zero Markup):
شما دقیقاً همان تعرفه رسمی شرکت سازنده را پرداخت می‌کنید و OrcaRouter هیچ هزینه اضافه‌ای روی توکن‌ها برای مسیریابی دریافت نمی‌کند ($0 Routing Fee).
🔸
پایداری بالا (Auto-Failover):
در صورت قطعی یا لیمیت شدن یک ارائه‌دهنده (ارورهای 5xx یا 429)، در کمتر از ۵۰ میلی‌ثانیه درخواست شما به یک سرور سالم منتقل می‌شود تا کاربر نهایی هیچ خطایی نبیند.
🔸
یکپارچگی سریع:
اتصال در کمتر از ۶۰ ثانیه؛ تنها با تغییر
base_url
در کدهای فعلی‌تان (کاملاً سازگار با OpenAI SDK، Cline، OpenCode و...).
🎁
طرح‌های رایگان و هدایا:
🔹
طرح Hacker:
استفاده دائمی رایگان از زیرساخت روتر به همراه امکان ساخت ۳ کلید API.
🔹
امکان
تست رایگان ۲ مدل
به صورت آزمایشی در بدو ثبت‌نام.
🔹
دریافت تا
۱۰٪ اعتبار هدیه (Bonus)
در صورت استفاده از پکیج‌های شارژ خودکار.
🎁
پروموکد
KIMIK3WITHORCA
پنج دلار شارژ رایگان برای تست مدل Kimi K3 به شما می‌دهد
🌐
وب‌سایت:
orcarouter.ai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7083" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها  یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7082" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها
یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار جذابی برای دریافت اعتبار رایگان اضافه کرده است!
✨
امکانات و راه‌های افزایش اعتبار:
🔸
تست مدل‌های پرچم‌دار:
دسترسی رایگان به غول‌هایی مثل Claude Opus 4.8، Fable 5 و GPT-5.5.
🔸
ابزارهای همه‌کاره:
امکان تولید تصویر، ویدیو، موزیک، مدل‌های 3D و حتی ساخت فایل پاورپوینت مستقیماً در محیط چت!
🔸
دریافت بیش از ۵۰۰ کردیت اضافی:
با انجام تسک‌های ساده می‌توانید اعتبارتان را بالا ببرید. مثلاً انتقال تاریخچه چت‌ها (Import) از ChatGPT یا Claude معادل
+۲۰۰ کردیت**، فعال‌سازی تایید دومرحله‌ای
+۵۰ کردیت** و ورود از دستگاه دیگر
+۵۰ کردیت
پاداش دارد (به‌علاوه تسک‌های روزانه).
🔸
سیستم دعوت (Referral):
اگر دوستانتان با لینک شما ثبت‌نام کرده و اشتراک Plus تهیه کنند، به هر دو نفرتان
۲۵۰ کردیت
هدیه داده می‌شود.
⚠️
واقعیت‌سنجی (Reality Check):
میزان مصرف مدل‌های برتر بالاست؛ ارسال هر پیام در Opus 4.8 و Fable 5 معادل ۱۶ کردیت کسر می‌کند. همچنین طرح رایگان صرفاً برای محیط کاربری وب/اپلیکیشن است و دسترسی به API نیاز به خرید اشتراک دارد. با این حال، برای تست سریعِ جدیدترین مدل‌ها بدون دردسرِ کارت بانکی، گزینه‌ای بی‌نظیر است.
🌐
وب‌سایت:
gab.ai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7081" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQxJbGEV_H6YDoM8aM3rsmlCGNLXafmXDBWkI_-eRyrXfzfcd9o89WJ9qqRQ0uBFYYt0Li9cCXCE1KGtON6cfUuadmyrNuB-PYzPtAgvb0N9_XvuJrjtcej0hdR6g3-YJWhk1XGllyOy6AX7P5--RrjL_3hzW82hYt2MN939gtVe1-UfvlT2Gqnw9w_RDuLoALcB_OIikg0sCts8fRIbEImLsKH47UibvqTkhTT8jg9LKneNjusIvj7M_ErzceM_JTo7fs-e0dJz18L7-Ed-bvpKtAtqXVq9ocfBjPhdoqMoR4HosveRbTt0bkdZRYgGXmZodJTixnGs87Aw_K95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/7080" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی  دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا: پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7079" target="_blank">📅 00:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Gemini 3.5 Pro
از درد عشق تو خوابمون نمیبره چرا نمیای لعنتی
😂
💔</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7078" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی
دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا:
پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.
🔸
پلن رایگان:
۱۳ مدل رایگان (مثل gpt-4o-mini و تولید موزیک Suno) با سهمیه روزانه ۱۰۰۰ درخواست (۱ ریکوئست در دقیقه) جهت تست اولیه.
🔸
مدیریت منعطف:
ساخت بی‌نهایت API Key بدون محدودیت آی‌پی (IP Whitelist) به همراه داشبورد مانیتورینگ.
🔸
سازگاری استاندارد:
پشتیبانی کامل از فرمت OpenAI API جهت همگام‌سازی آسان با کلاینت‌هایی نظیر Cline و OpenCode.
🔸
کسب درآمد:
دریافت ۱۰٪ از مبلغ شارژ دوستانِ دعوت‌شده (به‌علاوه ۱ روز اشتراک Premium رایگان برای آن‌ها).
🌐
وب‌سایت: api.airforce
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7077" target="_blank">📅 23:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSR5J4CPMjdc6w6J6s1wdP25oILWWbl1Go2hyaz4lkoqAgGcMB2PcUg9K5qEiCjMljPeSjIZohjbvXUqf2A45Sp75mmtXSZv_6XIGJUvsoYzmhaDNVqTcTeoTFTSBMynrMjEWA5DHpKXIQXvbcip-Qjs8LH2sq1KbF3W9Eutx3NV8QV_ckAPVyluH-ZKST_sIjdtbsQJEAz-GOWB0c0XJwRs25jXHzVu8eImgXkEZy4Mr4ryaqieB5hJvg2l7Ftcmv9JV_9PUUZddOEOQUp09E7XU5b18-P3az1WtGoHy1sNVO2zwOXTcs7t4Q-muUq-CXtIePV3DSN8dbBS3DyGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی افزونه YouTube Subtitle Pro؛ شخصی‌سازی زیرنویس یوتیوب
یک افزونه کاربردی کروم برای کنترل کامل و تغییر ظاهر زیرنویس ویدیوها و شورتس‌ها در یوتیوب.
✨
امکانات کلیدی:
🔸
فونت و فایل دلخواه:
استفاده از فونت‌های سیستم و امکان بارگذاری فایل زیرنویس خارجی (SRT).
🔸
استایل مجزا:
تنظیمات ظاهری جداگانه برای زبان‌های فارسی و انگلیسی (به همراه اصلاح علائم نگارشی).
🔸
تغییرات ظاهری:
ویرایش دقیق سایز، رنگ، بک‌گراند و حاشیه کلمات.
🔸
فیلتر هوشمند:
امکان تعریف و حذف خودکار کلمات تبلیغاتی یا مزاحم از متن زیرنویس.
⚡️
دسترسی سریع:
فشردن کلیدهای Alt + S هنگام تماشای ویدیو.
📥
نصب از کروم استور
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7076" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7075" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF   بزنید عشق کنید زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7074" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7073">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
بزنید عشق کنید
زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7073" target="_blank">📅 20:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7072">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏دسترسی رایگان به مدل‌های هوش مصنوعی با این لیستِ کاربردی!
⚡️
‏این سرویس‌ها بهترین انتخاب برای دریافت ‌API Key⁩ و تستِ مدل‌های مختلف هستند:
‏
👑
برترین‌ها:
‌
Agentrouter⁩
| ‌
Iamhc⁩
| ‌
Google⁩
| ‌
Groq⁩
| ‌
Nvidia
| ‌
Cloudflare⁩
| ‌
Freetokenfaucet⁩
| ‌
Dahl⁩
| ‌
Tokengo⁩
| ‌
Opencode⁩
|
Unorouter⁩
‏
✨
سایر گزینه‌ها:
‌
Kenari⁩
| ‌
Cerebras⁩
| ‌
Nararouter⁩
| ‌
Llm7⁩
|
Openrouter⁩
‏با این ابزارها، پروژه‌هات رو بدون هزینه پیش ببر.
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7072" target="_blank">📅 20:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7071">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔓
آرشیو کامل پرامپت‌های سیستمیِ لورفته هوش مصنوعی!
ریپازیتوری
system_prompts_leaks
یک گنجینه واقعی برای توسعه‌دهندگان و مهندسان پرامپت است که دستورات مخفی و پایه (System Prompts) معروف‌ترین چت‌بات‌ها را جمع‌آوری کرده است.
✨
محتوای این ریپازیتوری:
🔸
جدیدترین مدل‌ها:
شامل دستورات پایه‌ی مخفی GPT-5.6, Claude Sonnet 5, Gemini 3.5 Flash, DeepSeek و Kimi.
🔸
تفکیک شرکتی:
آرشیو کامل و تفکیک‌شده‌ی مدل‌های OpenAI, Google, Anthropic, xAI, Meta و Perplexity.
🔸
ابزارهای توسعه:
شامل پرامپت‌های سیستمی دستیارهای برنامه‌نویسی مثل Cursor و GitHub Copilot.
🔸
یک منبع آموزشی ناب:
بهترین رفرنس برای یادگیری نحوه ساختاربندی دستورات و محدودیت‌گذاری توسط غول‌های تکنولوژی.
📥
مشاهده پرامپت‌ها در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7071" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7070">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">؛MIT OpenCourseWare یه پلتفرم آنلاین رایگانه که توسط موسسه فناوری ماساچوست (MIT) ارائه میشه و بیش از 2500 دوره آموزشی رو شامل میشه
🎓
🌐
http://ocw.mit.edu/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7070" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7069">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk-gQ4PXK81bUI7jai90_dQzWOyYfw3o753PK84JR_uKj1z0YvxREHp8IqUp8KQyr5wK2taYl_hLHYtM2a8CKo6Y_98DEWGRbA76JaTo0Ayt-er91slLN5mO0lllcdq89QAYYonhFV73hIGBb-ykxD4OhhIInB0wCRhZ_Qw0z2-lzSNNsYtf1mfCqe8mJXcDSvoRdY9DuncTd3VUBwGXEIWXnPfKj6TAqXIN_Me89V1-KBeYrqqQiR2BEP49cxktnyXSmu9Vl6DLd7YVVMzJx5hz4V-CYbU63DAgnxa3h6sjk-tN7MwQS549Oh1z2tpZnus1Giaa3JPX_w4N79JI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Oh My HuggingFace برنامه کاربردی و متن‌باز برای HuggingFace که برای مرور و دانلود سریع، محلی و خصوصی مدل‌ها، مجموعه‌داده‌ها و غیره استفاده میشه.
🌐
https://ohmyhf.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7069" target="_blank">📅 18:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">happy کنترل ai از راه دور
🧠
Happy
یک پروژه
متن‌باز
است که به شما اجازه می‌دهد
Claude Code
و
OpenAI
Codex CLI
را از طریق
موبایل
یا
مرورگر
مدیریت کنید
⭐️
ویژگی‌ها:
✅
کنترل سشن از راه دور
✅
دریافت نوتیفیکیشن
✅
ادامه چت از موبایل یا وب
✅
پشتیبانی از مکالمه صوتی
✅
رمزنگاری End-to-End
✅
کاملاً متن‌باز (Open Source)
اگر از
AI Coding Agent
ها استفاده می‌کنید،
Happy
می‌تواند مدیریت تسک‌های طولانی را بسیار راحت‌تر کند؛ بدون اینکه همیشه پشت سیستم باشید
Github
💻
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7068" target="_blank">📅 18:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=vBb8ZBfFisW32MLdYY7BiotNqTqlegMX8vQrHpHEKRXH4hm_VHw9Cmk-V7_T99F1htSi4PY2RSZuNtllI2AaudWhmOC0BnKm9SzmBA-v6g_PndCL6qwUbwgKPT7baLjzo-AweLLJ_OHqLjPl1dJ0RIsEcZBk9qh_MmAa_Y6GL6Jd7uJ-hKfDoMhwIYNzRASneXkeidEGez5U93p_LvnIxAX3ToroTb3qZVeENqslajvlBl9MkXKskPNcUm9c4Mxe_5EAeU8SoEAF21mmEH5r5LSTddrwMwR0IFXvobCdVUJ4bQoJ-qGGf0IeEmDgIimGT-jjHBbBC5ljHE9anaoPLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=vBb8ZBfFisW32MLdYY7BiotNqTqlegMX8vQrHpHEKRXH4hm_VHw9Cmk-V7_T99F1htSi4PY2RSZuNtllI2AaudWhmOC0BnKm9SzmBA-v6g_PndCL6qwUbwgKPT7baLjzo-AweLLJ_OHqLjPl1dJ0RIsEcZBk9qh_MmAa_Y6GL6Jd7uJ-hKfDoMhwIYNzRASneXkeidEGez5U93p_LvnIxAX3ToroTb3qZVeENqslajvlBl9MkXKskPNcUm9c4Mxe_5EAeU8SoEAF21mmEH5r5LSTddrwMwR0IFXvobCdVUJ4bQoJ-qGGf0IeEmDgIimGT-jjHBbBC5ljHE9anaoPLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جستجوی چت‌های قدیمی در ‌ChatGPT⁩ بالاخره راحت شد!
🔍
✨
‏دیگر نیازی به اسکرول کردن‌های بی‌پایان نیست. ‌OpenAI⁩ قابلیت «جستجوی یکپارچه» را برای وب، اندروید و ‌iOS⁩ فعال کرده است. حالا می‌توانید از یک پنجره واحد، میان تمام گفتگوها، پروژه‌ها، فایل‌های آپلود شده و تصاویر جستجو کنید.
📂
🚀
‏با استفاده از فیلترهای جدید، دسترسی به پیام‌ها یا اسناد قدیمی که ماه‌ها پیش ذخیره کرده بودید، در چند ثانیه انجام می‌شود. یک آپدیت کوچک اما به‌شدت کاربردی برای کسانی که زیاد با هوش مصنوعی سروکار دارند!
💡
✅
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7067" target="_blank">📅 17:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF  تمام نامحدود</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7066" target="_blank">📅 17:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
تمام نامحدود</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7065" target="_blank">📅 16:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIYuSr7cqNf3Q8VGR958aQZAxYH_juScF1boN0m5SX3Nx8OFQ8e8O-UMUAFQDrnCXeYYBkSnAK7kU2tYGsk5jiYpskyZ7E1ncNiok2d_HCnvjVj9kDFKeGu-lABeUOZOWfErgU_iydi2K2TWgZu0HFO20IkB1YxlbYJm_XPpXcvILY3EMzV4tvsd_yWgMimBJDszazGNfEbn9zCHPkT8HtDXSFB3Ny202phdDV4QGJFHXHtwij489i70DSxYl5f4Ye1EjxGtyvNiHSsBY491bTmlEKs115V8_SFRmDc0v9KbQfgkqnmHsfCmOUFj8dL8I1B6D9qfy5Eq5mW0OnGBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی SHADOHDORKS؛ موتور جستجوی قدرتمند گوگل دورکینگ
یک مرجع فوق‌العاده و ابزار تخصصی برای OSINT و جستجوی پیشرفته (Dorking) در گوگل که برای محققین امنیت، باگ‌هانترها و تحلیلگران شبکه به‌شدت کاربردی است.
✨
ویژگی‌های کلیدی این ابزار:
🔸
دارای بیش از
۱۰۰۰ دورک (Dork) پیشرفته
و دسته‌بندی‌شده.
🔸
پیدا کردن هوشمند
ساب‌دامین‌ها (Subdomains)
.
🔸
جستجو و کشف
پنل‌های مدیریتی مخفی یا در معرض دید (Exposed Panels)
.
🔸
شناسایی
نشت اطلاعات و کلیدهای API
در سطح وب.
🌐
آدرس دسترسی مستقیم به ابزار:
🛠
مشاهده سایر ابزارهای کاربردی OSINT:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7064" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=R90_2w2CcMjLg1EMB6M0xoaxjz72zT-Vvh6CSTykZgXkThXbji_SvuT66F64_yRcc7s3TJERMfZtXHcjcEQ80HuSF10HtwNxYd8reoZqFt0v9TmOGJt6KAs7lZ_xVkwAAM3rWAele05Yxupny_lExu_IRvGa9XmIgSlhJTRMmsyFxG09-Bzgc5evbi4yR_VafzMVtpwOWXZ2fxjSY5jnHOrETa2SpGSmYuWKLqnBlw9kJYLoe659GCXa6qJ6wHnvwSnMluCn3q_WTOdwN_pHZeu3JQu_TznhOsAud_QASGXVCSV4EXyMfFMs6s1YJ_ozPWcztlEwj68tQx8ldPoryg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=R90_2w2CcMjLg1EMB6M0xoaxjz72zT-Vvh6CSTykZgXkThXbji_SvuT66F64_yRcc7s3TJERMfZtXHcjcEQ80HuSF10HtwNxYd8reoZqFt0v9TmOGJt6KAs7lZ_xVkwAAM3rWAele05Yxupny_lExu_IRvGa9XmIgSlhJTRMmsyFxG09-Bzgc5evbi4yR_VafzMVtpwOWXZ2fxjSY5jnHOrETa2SpGSmYuWKLqnBlw9kJYLoe659GCXa6qJ6wHnvwSnMluCn3q_WTOdwN_pHZeu3JQu_TznhOsAud_QASGXVCSV4EXyMfFMs6s1YJ_ozPWcztlEwj68tQx8ldPoryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسخه جدید گفتگوی صوتی Chat gpt منتشر شده و انقد طبیعیه، پشمای همه ریخته!
+ خوراک غیبت برای دختراس.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7062" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">1.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش پنل ثنایی به زبان ساده
✨
منتشر شده توسط
@ArchiveTell
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7061" target="_blank">📅 15:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7059">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید .
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود
✅
.
از توجهتان ممنونم
🙏
.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7059" target="_blank">📅 15:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7057">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">معرفی Ghost Downloader؛ جایگزین مدرن و متن‌باز برای IDM
🚀
📂
نرم‌افزار Ghost Downloader یک دانلود منیجر پیشرفته و چندپلتفرمی است که با رفع محدودیت‌های ابزارهای کلاسیک، تجربه‌ای سریع، پایدار و بهینه را برای دانلود فایل‌ها ارائه می‌دهد.
🛠
✨
✨
امکانات کلیدی:
🔸
…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7057" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7056">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">معرفی Ghost Downloader؛ جایگزین مدرن و متن‌باز برای IDM
🚀
📂
نرم‌افزار Ghost Downloader یک دانلود منیجر پیشرفته و چندپلتفرمی است که با رفع محدودیت‌های ابزارهای کلاسیک، تجربه‌ای سریع، پایدار و بهینه را برای دانلود فایل‌ها ارائه می‌دهد.
🛠
✨
✨
امکانات کلیدی:
🔸
سرعت خیره‌کننده:
قطعه‌بندی هوشمند
(AI)
فایل‌ها برای دستیابی به نهایت سرعت،
بدون نیاز به زمان انتظار
جهت ادغام (Merge) پارت‌ها در انتهای کار!
⚡️
🏎
🔸
پشتیبانی جامع:
سازگاری کامل با پروتکل‌های HTTP، تورنت (Magnet/BT)، FTP و فرمت‌های استریم نظیر M3U8.
🌐
📁
🔸
دانلودر اختصاصی یوتوب:
قابلیت دریافت مستقیم ویدیوها تا کیفیت 4K، پلی‌لیست‌ها و زیرنویس‌ها.
🎥
🍿
🔸
امنیت و عبور از محدودیت‌ها:
شبیه‌سازی دقیق اثر انگشت مرورگر (TLS Fingerprint) جهت جلوگیری از مسدود شدن دانلود توسط سیستم‌های آنتی‌بات.
🛡
🥷
🔸
افزونه هوشمند مرورگر:
شناسایی و استخراج (Sniff) خودکار لینک‌های مدیا و ویدیوها از صفحات وب.
🔗
🧠
🔸
پشتیبانی چندپلتفرمی:
بهینه‌شده برای ویندوز، لینوکس، مک و دارای اپلیکیشن کامل برای اندروید.
💻
📱
🤖
این ابزار کاملاً رایگان است، رابط کاربری مینیمالی دارد و در پس‌زمینه کمترین میزان مصرف منابع سیستم را به خود اختصاص می‌دهد.
💎
🍃
📥
دریافت فایل‌های نصبی و سورس‌کد از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7056" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7055">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHMKnEFMd--RqKDwLm8EhsAZJqSpQRU8srrhNKf44qAmCWjP8OJKhrUl8uK3buGJZDFP1LFgK9Xgi-k3zmIbN_AsxFyxcjzHx1qD-SYsKa02o6lf5QyBlthTt4znSrCHitcSif4lWRLQqMSC6RmpsJQh8O0AaIC9_ZPmapCB_SXPeiZ6qkNomcsrdHbuNlEwKXtjB3x_IlkMfMKyn6O3EUNS40atDtzEHFj47dIQLn9bOAXT46cTrrjCk9y3JJyboM73uvIH1Mx6yqmWgDUtG-FfH10H3nHg6kT2Kl2VGvAvcJGtOBRLJPnf6Eigl7pWGR4tFSym8dNcaZ5y1LbMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7055" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7053">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اشتراک Gemini pro برای ۱۸ ماه فقط ۶۹۹ هزار تومن!
🎉
💰
اینو قطعا این روزا زیاد دیدین تو چنلای مختلف. خواستم بگم ماجراشو بدونین.
یه شرکت تلکام هس تو هند به اسم jio اومده با گوگل قرارداد همکاری امضا کرده.
همکاری اینطوری هستی که هر کی سیمکارت jio داشته باشه، و ماهانه ۳۴۹ روپیه معادل ۳.۷ دلار به صورت مداوم شارژش کنه، میتونه اشتراک ۱۸ ماهه جمینای رو داشته باشه. اگه یک ماه شارژ نکنه، اشتراک جمینایش غیر فعال میشه و برمیگرده نسخه رایگان.
این جیو تو هند تبدیل شده به اسکم
🤑
هندیا میخرنش، ۳ دلار شارژ میکنن، میفروشن ۵ دلار (حالا فمیلی هم میشه اشتراک گذاش، اینم حساب کنیم میشه یه ۳۰ دلار)، ولی ماه بعد تمدید نمیکنن!!! یجورایی کسب درآمد میکنن باش.
۳ دلار میدن ۳۰ دلار کسب میکنن. دلالی عالی.
خلاصه به احتمال زیاد فقط یک ماه کار میکنه حواستون باشه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7053" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrOczvnQQAkYZzCD_i2dbkw4unudsufPQz8-yUX7VsE9W7e4-LLhESDSSwHUIpzUSKm0Sn0KhdLjD_k7IKNdZ3F7mcZmqlTfxmJJLErcfFmTWj_kZW07oFxL_3HII0edCtIkkc-ndKJ_p_kkaSxF1l4SdHq0plTKF7B5_Vhi_wnYw27JwhoVJ04UKORiyTzYMTmViwDdRqHTeuLsCrBWcqqo9WltUYq965jh3e97HLFmxDAcoEPNzzvMf-dY0nKUo-S6XPEAY_MQL9v4c3NL1AIQX3r8c4QuwMBMI3__8lxYKDrAH0tDOAdmKOzAQjCKGEz1pJCmqs0g5tp-deED8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
امروز باید منتظر Gemini 3.5 Pro باشیم؟
طبق جدیدترین شایعات، احتمالاً امروز گوگل از نسخه جدید هوش مصنوعی خود یعنی
Gemini 3.5 Pro
رونمایی خواهد کرد.
✨
ویژگی‌های لو رفته و انتظارات از این مدل:
🔸
حافظه ۲ میلیونی:
دارای کانتکست ویندوز (Context Window) عظیم ۲ میلیون توکنی برای پردازش یکجای داکیومنت‌ها و پروژه‌های حجیم.
🔸
حالت تفکر عمیق (Deep Think):
اضافه شدن قابلیت استدلال پیشرفته و منطقی برای حل مسائل چندمرحله‌ای و پیچیده.
🔸
غول فرانت‌اند:
تمرکز ویژه بر روی کدنویسی و عملکرد فوق‌العاده قدرتمند در حوزه فرانت‌اند (Front-End).
🛑
احتمال تأخیر در عرضه:
با توجه به رقابت بی‌رحمانه در بازار، اگر گوگل احساس کند این مدل هنوز توانایی رقابت کامل با برترین‌های فعلی را ندارد، احتمال تأخیر آن بسیار زیاد است و رونمایی به هفته آینده (۲۴ ژوئیه) موکول خواهد شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7051" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
: نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 0/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7049" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 0/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7048" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7045">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGokLIkoVixUGOwc7PbKEPCcQLlZ8qGqZQQFMubci6D_Zp1HVDioHS0Rw2xIFbB2bZrG1VNudVp4BpqyTdVA_jwXLnRrDqhmuJFn5y4anImgtOoWuH20ml76vUlWlMGDMMupox9w2_8u9fZySThqbUBVEqlrSwnB96yVoRVwv1zUUcIi_fXKKwy0q2K9ayL1dJ6cVeOXLA_Sh1WbIer-nOePkDioxXdDwMJolOHWC0gJBvofG2BUUTtD-WzdDKD32DEAxIx11jhiSq5TbeTp7_A4DUrSZYH3okGqPS87MSDZ__EfWVX2eqTvkiJvNklwnbk7Cn2oA89aHaGylzFRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
Google AI Edge Gallery – اجرای  هوش مصنوعی بدون اینترنت
📊
💡
گوگل پروژه متن‌باز AI Edge Gallery را منتشر کرده؛ اپلیکیشنی که به شما اجازه می‌دهد مدل‌های هوش مصنوعی را مستقیماً روی گوشی اجرا کنید، بدون اینکه به اینترنت یا سرورهای ابری نیاز داشته باشید
🌐
🔻
قابلیت ها :
🔹
چت با مدل‌های هوش مصنوعی به‌صورت کاملاً آفلاین
🔸
تحلیل و درک تصاویر
🔹
دانلود و مدیریت مدل‌های مختلف
🔸
حفظ حریم خصوصی، چون تمام پردازش روی خود دستگاه انجام می‌شود
🔥
با توجه به تجربه اختلال‌ها و محدودیت‌های اینترنت در ایران طی سال‌های اخیر، چنین ابزارهایی می‌توانند گزینه‌ای کاربردی باشند؛ چون حتی اگر دسترسی به سرویس‌های آنلاین محدود شود، همچنان امکان استفاده از هوش مصنوعی روی گوشی وجود خواهد داشت
🟡
🧪
این پروژه هنوز در مرحله آزمایشی است، اما می‌تواند یکی از مهم‌ترین قدم‌ها برای اجرای مدل‌های هوش مصنوعی به‌صورت کاملاً محلی روی موبایل باشد
GitHub
🐱
PlayStore
📲
ios
🏬
Mac
💻
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7045" target="_blank">📅 03:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">172.64.147.128 104.17.166.13 104.17.166.13 198.41.195.250 104.27.51.177  اگه پینگ نداد باید آیپی های تمیز کلودفلر رو بندازین توش</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7043" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVmMCkktwJCRy2_qL24yFqtqPN528BJIlXeTLs56Fsi_oCXsO-gkYhNktYBKQGpifTeMyIqgDnQu-hXJE26v8xuG8hKYYrt--jTD100bbyKeYuPuIFRjzncT90VNXaWorIQG7Hb9kgeObQ_KqTFN3_YsZ8dt3_gpxC7ws4Wh_ilZzTFiuM2zNeAt_AW1o1bwCLUhTIzANkUkaw5_SFkkjhJexyOUWdAL126P_vdeUcrjnIQCrxjrytSvr4avqvsKE55wtBG1WptGtBhB8_044XKo2P5mmjZZ7B7wi1D6cIUaY9i7skqvKZlZPXHJi2BBj1758MwRaLVig1mLuz4qGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛HyCanvas جایگزین Open Source و Self Hosted برای Canva
🎨
مناسب افرادی که میخوان طراحی گرافیک، پست شبکه‌های اجتماعی، ارائه، ویدئو و اسناد رو روی زیرساخت خودشون، بدون واترمارک و رایگان انجام بدن.
✨
ویژگی‌ها:
🔹
اجرا در مرورگر
🔹
پشتیبانی از طراحی پست، ارائه، ویدیو، وایت‌بورد، اسناد و چاپ.
🔹
خروجی در فرمت‌های PNG، PDF و سایر فرمت‌ها.
🔹
پشتیبانی از "Bring Your Own Key" (BYOK) برای قابلیت‌های هوش مصنوعی.
🔹
امکان Build در محیط Production به‌صورت یک فایل Go.
🔗
سورس پروژه و دانلود در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7041" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7040">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_wpslUykqS6tv3uajfomxqduqEyeq4kAurdEK0m9UxoAYSqaYKqVf673Y_uWei6FICp4IAPPU03JtzsJoaP0vAD38MHB8JBuu5tL4pxMhQN5_tr83YNxrpsDppQTcQOfQXmbEvWAcZKB4Zzt0QgQfVTmql5xXzPet_5bevrBBg7MDBqU_en8xeT7bveyacpOP4vYaQN2F5PfxIWjaOKzI3PNA-E68rBfy52EbMVabwKH-BIJkJqbIKBzmgY8p3DGjvAYZQTP9uEgLjJxHmR7TGcIi2txpOp_GtPLn1xhn6SpH4maWVBlbqLTKbKYmKeSlpFD__ZN6fXKcn7POvbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200GB   vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell  تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7040" target="_blank">📅 21:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7039">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">200GB
vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell
تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7039" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7036">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4OxtS8hi1PBUyleSmXjXvPJDKAl7bIgR7m1pV1ZxSt5m0fDWr0tFhHhgMu57cPhdhHKjjA6Kfr8ETcfcOciFg6syaffXuGPr81ArLW_8XQuDwYfwCot_XOGDmzb9AZW7N2ES5WM96Z-jnvxqtbj9cZZauPvA1i1nDQgt_rUSCLY3wvRO8pqYkbacnIgqISoTV8huhDmDXLo62qDhbq3EO7DVB-m7j-7s9NaDo6tkhdxHlSKgjNi5YBFVO1w1dhtI9RTngymwIf-pPLGqJDzuSNCB31uCc2JL1oAPyBQqGIo8VkdYuNMOOdTgEKk_m7Ja1WRHY3x2GerSKc_tHfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
هوش مصنوعی Kimi K3؛ رقیب قدرتمند چینی برای Fable 5 و GPT-5.6!
استارتاپ Moonshot AI از مدل زبانی جدید خود رونمایی کرد که با مشخصات خیره‌کننده‌اش مستقیماً غول‌های هوش مصنوعی را به چالش می‌کشد.
🔥
ویژگی‌های کلیدی:
این مدل با حدود
۳ تریلیون پارامتر
و پشتیبانی از کانتکست ویندوز
۱ میلیون توکنی
، توانایی پردازش حجم عظیمی از داده‌ها را دارد. Kimi K3 می‌تواند اسناد بسیار طولانی و پروژه‌های برنامه‌نویسی سنگین را بدون فراموشی یا از دست دادن رشته‌ی کار، به‌خوبی تحلیل کند.
🛠
امکانات و قابلیت‌ها:
🔸
نسخه Kimi K3 Max:
دارای رابط کاربری چت (Chat Interface) با حالت‌های اختصاصی و بهینه‌شده برای برنامه‌نویسی.
🔸
سیستم K3 Swarm:
یک فریم‌ورک پیشرفته برای کار با گروهی از ایجنت‌های هوش مصنوعی (AI Agents) تا وظایف پیچیده را به بخش‌های کوچک‌تر تقسیم کرده و تحقیقات گسترده انجام دهند.
🔸
دسترسی API:
به‌صورت کامل برای توسعه‌دهندگان در دسترس است.
🚀
لینک دسترسی و تست مدل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7036" target="_blank">📅 19:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrDCvpEWcw_rddkeTpavXBpk9y4lKR31YO5lvwNCFG4-VPPR7gjXIy7LqM-rQK_Bn5VtJifZF1PYpJV0ZHfVn-qByfp_AiQReGLXSxtcjE6nYLZC034celPrMw97BfOKCGxIVGgnX27CI_UFwn8ay225TrxCi1-mS5l-W9623RqbL1hsFXwa0rbmyvDMyaPhCPfNFS7m5h5tPON6pXF4QfzOCMB3kcyRkM6wO0JrsGiXHNYsu7vXWbkpzJL6UJEdfMgAnuHPkWu0yR5QspRWQOw0-EvJl9DeTsk5yrXLiWUWIh1SDWA5wDEEsw5jAgj1uMEEzavGoe8CNYqP1vjuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8Avf-vx2HY8trV4oUS9JVGDxwTor15r5nGdPxNDfL4jhX-T-L184n8zyklMtmpaZftVoMLZn2DCPrLh0aSXYnVwwif54WtG3qxS555QhG_aX_ATjGGDqpne9_M1_cKA35z1U6MDhY-FcjJB2VilVcRx6EVRWi0pZuBziHPGI0B7SJJ3gVq5DFQGO6W4CItZenOyzh0afNcEeVO4UDY4e2URx00A7zBxow88xuh3DrC2Qr0K3fXR4YyWbc9BlTLwcC-e-BA8T_FHj3umHrapB_XV_hqF7-1cZYcjPdUdkbgmfgkx_rfx1etbk_O2Nxw0xEpUlolXMT_OWJzsEvhbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMV3DfbMWB28uUIWxw1revVESeSlmkfI2-7BEIGgvCVdq8-H6IJwclhlgvR_BBSZYMQYiGflM_doym5RXMSxUVIhGZ-2RkH6vy833XgA0xoeQPpqyIK1kJQgNE_ireO4etFftgi3BGS-UdLYH6wl_9rl04qpHMJ_bM6BIIkwsUWRA1AwgnT8ttS74ij1V-o-_EqrNBkGZ1Ninh8WwKZhOgubjpzMlpKdm4byo1Esv-HK6p4uAUMdhhmrSm27Aq1KA9EPBx0lrD3ah1ZvO5QnoYQPPsTtpKUOhov8MBaxc2T_FfqyNsO90S5EItgo_iW4z6vQWuUQNu56SFUC973tow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤖
دالتون بات (Daltoon Bot)
یک دستیار هوشمند و متن‌باز برای ساخت، مدیریت و فروش خودکار سرویس‌های VPN (از طریق ربات تلگرام و پنل وب).
✨
امکانات کلیدی:
🔸
پشتیبانی یکپارچه از پنل‌های سنایی (3x-ui)، ریبکا و پاسارگاد
🔸
کیف‌پول داخلی برای شارژ حساب و خرید آنی اشتراک
🔸
داشبورد مدیریت تحت وب (React) با قابلیت کنترل چند سرور همزمان
🔸
مانیتورینگ زنده ترافیک کاربران و پشتیبانی از زبان فارسی
🚀
نصب سریع با یک دستور (لینوکس):
Bash
bash <(curl -Ls https://raw.githubusercontent.com/mdaltoon10/Daltoon-Bot/main/install.sh)
📥
سورس‌کد و راهنما در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7033" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)  کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها: سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز: ساخت کانفیگ…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7032" target="_blank">📅 19:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRLuql2CO4Fv9u3df_oBLWD9wUUKT02JyXjRC_XZRjhb-SlfbOd7kg60AKpD_rSCWbErAvwfEPTuRA0QqIFENjGehHu1GRdFs9OzZNdbQCIgYs2wwujkIpzylwV9NAfqQ4cTITcFhBBpPjBswOaEfj9TT-UeBcEcB_PGKRXM_d49oCDAjmDUW5zOoaoE2Hd9nhu1SqyPSJjG2p7z6Gl_r9IX4QTnqi5MHR68vHwY_hhG7IyKrMAdW0ewbYFA7QU0tSPA-h_u-JeFcExt2Rh3YXn1_WA350LnvtSA5QyeUdKU2gnXzysOUAKVVjnPixI-ysThObG1yvys_d_ZsLgzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)
کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها:
سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز:
ساخت کانفیگ WARP با یک کلیک و دارای اسکنر داخلی Clean IP.
🔸
مقابله با فیلترینگ:
تنظیمات Fragment (ضد DPI) و Sniffing برای اتصال پایدار.
🔸
مسیریابی هوشمند:
تونل کردن برنامه‌های دلخواه و باز کردن سایت‌های ایرانی بدون مصرف ترافیک.
🔸
مدیریت سابسکریپشن:
آپدیت خودکار لینک‌ها و نمایش حجم باقی‌مانده.
🔸
ابزار تست:
قابلیت تست سرعت، پینگ و نمایش لاگ شبکه.
📥
دانلود فایل نصبی (APK) از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7031" target="_blank">📅 19:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyF0ofeafsfEm0_xWSWsY_Dt8su7v88QA7Gc_WJEJwsLp7BfXgS2n6dxZvwwPzfPJODZ311ia6HL14PYk63l9YFskU3Yv18jRPFrFI6nmRx_lqiyKCsnTsteyZvFJMZ1VmmMpZGXS6Dyw8s6ntMMr8WYdWXrbTaArt57AywzQSd5fkwUZsiQ0C_nxOGQcWLp_38s0TAkGHYkfBv4_C74RS587zNQ_m5F_EwqsCgZuzZvgwusSjz5T5TLX2hChcwstyH6K7FXvLA-BvSXfQkh8dMezhY0qGjIcAyxCgbH-WWQGK9mxySHW9GvtDI0tNEkH6tBx1H4LPkYIE1iilnZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm4105147eCwfg-rdxvkdPeizqnhLa7T1Ykvc7p-hFgDOpbhL-5wP-rNE5z4Msl1OgjdAYX1_ds-w09_0NVEyQmLQk6swhngQ2YYj-cAv_aCGNN9Dj-ILNXq1-WuHEFTBxaFzch3iSlNcgXqU_FNyPXupODjj806uJZ__4d0isZ5zTyk6lWLZP14U_JIkqgbg3F5o5n6CJZjuBDOCBOeaHUjoj68n8lfFycWJiLrJGxn76T3y6OjKqt4iMo1ZMCy9_qslbYbw0HeR_LwThmsWBnw0wtOWUDe8TwD1rL4TfdpxeQRj_WfenpNKtSQxyqkVE8V3ZucNmHGpNpnKVMJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKwNc3P1gMy-keYwq9pcciZm74fX1k7OpPjSL6tXM7UPoWCX3uJ2iTrEeFh-Y5D8xYhBg9JTpjh6n5cFcWbgWAoYLxESwEo8rOx1WtcY9zJJYwrIbrCt8ty951VE6E2Zl9zqXUj0AbA4OBSCS3Svi9gaJJBOssW0HjuRvGbB4mcT34kRdel4vwC_7k94eDiO3Boyh2xT5mOU9lyLx3j8eZecDBn-5ljN29TPfQ15rbJ61HVRti6bpEkqbSZXjgasAyKsnVjSy_YD5slvN6TrIGPbNdyweIzglVAkw9mTKGgjULlPQjudDdEewGJrLOCFgGvbTda4QF9FkfYujYqoMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
مجموعه‌ای از پرامپت‌های متنی، تصویری و ویدیویی رایگان و قابل کپی برای مدل‌های هوش مصنوعی مانند ChatGPT، Claude، Gemini، Nano Banana و Veo که امکان فیلتر کردن بر اساس نوع، مدل، دسته‌بندی و امتیاز وجود داره.
🌐
https://freeprompts.io/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7028" target="_blank">📅 17:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1g7vGZ9Ij-LDxvUv5eaZPePf0dgsGEJYZ553TE5jMCh8uKp6x3D4Y-co-ypv1JE_PmPHth3Y6EKRo6hYuUDYK5tXVOIkoAAldooOCwyzEbso0VOTFXcmLI-9g2vbwvTiylHwSFArqNDFKWfvBIc4G9El7Rb-Ysu0r7WU-_RpilSVO6esiMMofJqvQFiHvsGCDE6_18CYN8vVVyy9h9XGgYPuHLrAQ4LcrVwuwWJH5KnTpRlAUGmQSIDiP88kes_Vw-ZfRZQndDjK_meTdISgK0wT-iGZA_YuhqupTNw6R-BCrSpVd-5MdcukVtPkRIb2F9rovV34_tpyo4Cr05y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
استفاده از Claude Code با مدل‌های رایگان و لوکال
محیط Claude Code عالیست اما استفاده از API آن پرهزینه‌ست. ابزار
Free Claude Code
یک پروکسی هوشمند است که اجازه می‌دهد این محیط ترمینالی را به هر مدل دلخواهی متصل کنید.
✨
ویژگی‌های اصلی:
🔸
پشتیبانی وسیع:
اتصال بی‌دردسر به API سرویس‌هایی مثل DeepSeek، Gemini و OpenRouter.
🔸
اجرای آفلاین:
پشتیبانی از Ollama و LM Studio برای کدنویسی کاملاً رایگان با مدل‌های لوکال.
🔸
پنل مدیریت (Admin UI):
رابط کاربری تحت وب ساده برای تنظیم سریع کلیدهای API و تغییر مدل‌ها.
🔸
مسیریابی هوشمند:
امکان تخصیص مدل‌های سبک برای وظایف ساده و مدل‌های قدرتمند برای پردازش‌های پیچیده.
این ابزار روی ویندوز، مک و لینوکس به‌راحتی نصب می‌شود.
📥
سورس‌کد و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7027" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7026">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVa0z04Cc78cxicYF0gIAkVnL7afDrTUpZf75MmchNT2yqIOY6ezxzZREdUYEjLCXvB2VPTvzS2THCD3HkgcYnJHELJMY8XryWyC0qDoMrzw-66cBeFahkyXf57UzXDG6VsKirsz7KTb2mgNuFXEOc_TOsd5_M9CAEfGT3tcjmV7Fe-48yvUoNW9RXYS8f4xhq0L4bTct7ZnGzlMfI00CgjiiISPUnyhKfCXA7zTL5crByQ36BF56kw1mY7fAfQG6mCaJ7dHw693FuHNVeyxTtdfFdkRqfSETrpITYM8yXS6RqOqD6BNfpjxBe5hwY87NKBUTXIVvDNXTd57SFXSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی و آموزش راه‌اندازی UAC SNI Spoofer برای ویندوز
یه کلاینت متن‌باز، سبک و دو زبانه (فارسی/انگلیسی) که با متد SNI Spoofing و هسته Xray کار می‌کنه. تو آپدیت جدید فایل‌های پروژه،
آموزش ساده و قدم‌به‌قدم راه‌اندازی
هم قرار گرفته تا خیلی راحت‌تر بتونید وصل بشید.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
پروفایل اختصاصی اپراتورها:
تنظیمات کاملاً مجزا و بهینه‌شده برای همراه اول و ایرانسل (بدون تداخل با هم).
🔸
اسکنر هوشمند:
تست زنده و پیدا کردن خودکار سریع‌ترین SNI و مسیر.
🔸
مدیریت بی‌دردسر پروکسی:
ست کردن خودکار پروکسی ویندوز و بازگردانی امن اون بعد از بستن برنامه.
🔸
بهینه‌ساز یوتیوب:
استارت سریع‌تر و روان‌تر ویدیوها با قابلیت گرم‌سازی مسیر.
🔸
نسخه پرتابل:
اجرای مستقیم بدون نیاز به نصب پایتون (فقط کافیه فایل ZIP رو دانلود و اکسترکت کنید).
📥
دانلود نسخه پرتابل و مشاهده آموزش راه‌اندازی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7026" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7025" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دفترچه راهنمای کاربری پنل 3X-UI ثنایی به زبان فارسی
✔️
راهنمای جامع پنل 3X-UI ثنایی که برای نسخه‌ی 3.5.0 نوشته شده است.
منبع:
https://github.com/yukh975/3X-UI-Manual
@break_the_barriers
💎</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7025" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5LQ7dB855K6osJWXQfwowGnQJNsAzrOvLXKgHdB2c18TgFUllTP2Vz9NrQgVd_nycs5DNLsMLpmvm--CdZguEXk7rav5_SOXRuMxJjFaXLKI3psdARj81K6r1y8W31vNczW3LfTSsKK5J_ONmznn5T268GjQ6UxsT5vpJ_6h3riaodXkj_VNdhDQ62mHEG9UQnPF_XIIJSu_oFv5OIuhDKvx7h6rm09q9d_AuFJ2wLsWcZ7AW56opVk15I8iqB7EZ8zzXUxVbndOmulWUebHB5H5xb-zzA5zi7vjdwc01INEbN1cFAZJDHmJIMHlSNs-LDYR0MMUyWa6apD5oWkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
؛OpenAI قابلیت جستجو در ChatGPT رو اضافه کرد که به طور همزمان در چت‌ها، پروژه‌ها، تصاویر و اسناد جستجو میکنه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7024" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون  اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی Hermex، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید. این برنامه…</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7023" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون
اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی
Hermex
، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید.
این برنامه کاملاً رایگان است و هیچ اطلاعاتی رو برای سرورهای واسطه ارسال نمی‌کنه؛ یعنی گوشی شما فقط نقش یک «ریموت کنترل» رو بازی می‌کنه و تمام داده‌ها و پردازش‌ها روی سرور امن خودتون باقی می‌مونه.
✨
ویژگی‌های کلیدی اپلیکیشن:
🔸
رابط کاربری بومی (Native):
ساخته‌شده با SwiftUI (مخصوص iOS 18 به بالا) با طراحی بسیار روان، بدون نیاز به واسطه‌های وب.
🔸
چت زنده و هوشمند:
ارتباط در لحظه با دستیار هوشمند، امکان ارسال فایل و عکس، و مشاهده روند استدلال و تفکر مدل.
🔸
مدیریت همه‌جانبه:
قابلیت مدیریت تسک‌ها (Cron jobs)، مشاهده مهارت‌های نصب‌شده (Skills)، ابزارهای آنالیز و بررسی حافظه مدل.
🔸
شخصی‌سازی کانکشن:
امکان اتصال به سرور از طریق HTTPS، پراکسی معکوس (Reverse Proxy) یا شبکه‌های امنی مثل Tailscale.
🔸
بدون هزینه پنهان:
فاقد هرگونه تبلیغات، سیستم ردیابی (Tracking) یا پرداخت درون‌برنامه‌ای.
📥
دانلود و اطلاعات بیشتر:
لینک نصب از App Store
(یا جستجوی Hermex)
🔗
سورس کد پروژه در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7022" target="_blank">📅 13:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaCPp6-3k9ptGP2DND0TbhUP4VsOLhmmPkcwzfnFYbuOLyca7Egc-_No7wd5WrfW__KNOT4h5oXAszBOGor2IWyH38iZOUztwg-ynktYTf_PYi5FWbaWJHj0I3hvc4DM2Zq5kkZr1w5w1rQuIsliYnas9TkitggARVBxJz2z73A_Kr7cryaWOTiBL3KVZXhDfoH7vLubf7AfBQJHpk_elDBs6Xa-VEOa2ikL0B1FSIUFEyXTox2BTMew3WRi79scAiu8IPweIFPla7sUukv1r7Y62PJ6HEz7N0eMFzaKA1HAe4Q9UWQtRFgplcD2H870zDo-Xxf4T7QNpGlFZRNRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7021" target="_blank">📅 13:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3yLFbdToujplss1NBbqHwu2extmrH_vH7LgbfgIWtg6pIIihDxmkSGMb1wiqvpPg_5h_KhLCTyBZ5DKLvT7Hi8XVm0EPrMk8UhH8jIhMcW1UIpM3rLmNKaBGZUJh6rsU96xXdMafK2rw751-IBt-xUz5n9ymtS_kloP6fBW9eiy3WFRjx5105ZbTw4CYaRyTgWC_F2qqZlXtfOYIia9EpnWG_OwW0AU9zAndN8mkEOA5cHXjCUIvJrePPxx5Pz3n9y3rAVgsSFiVDGuU3deGKrhlZmWsLwprLBNjPRNW9GwBhWepxQmQ6DzGkcPtk9q9fjYlJ8ce3oifeJM3Gqhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RohanKar Launcher
🎮
یک لانچر دسکتاپ برای اجرای مجموعه‌ای از بازی‌های کلاسیک
PC
که روی
Archive.org
منتشر شده‌اند. با این ابزار می‌توانید بازی‌ها را از طریق یک رابط کاربری یکپارچه مرور، دانلود، نصب و اجرا کنید؛ بدون اینکه نیازی به ساخت حساب کاربری داشته باشید
👤
مناسب برای علاقه‌مندان به بازی‌های کلاسیک که به دنبال دسترسی ساده و سریع به آرشیو بزرگی از عناوین قدیمی هستند
🎮
Github
🐱
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7019" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghb_php6pYRGtri1dtXjP_O_KmOd_yf10rZOI-0nrFkwkzoiicSv7996DdRdSWsqmzx56YF56-UUkEWXwfC7ePgNHzQloV0Jfpi3wBKqUYxhLOh0PKiah4d2iyuiWMfiVwAzXDsKD2_SYzPaGEBCjySGlpGcxWLh1qUPWEvMd9dzWHvnhFcvRkzRxNTyOdpogo7hg3VZLLg0Nppoosk8GkLa_OiLLxnsB4TPZlhUNZNE4k892Qu4lu3866FHPb5p5xupNPTH9yeU6D__PcTYRGK99YEfwM47_75-S81vi-pb0tXftYd6oYQQLTcoM4atzdpm02NHilQEI4z_z-Kz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
هوش مصنوعی برنامه‌نویس Grok Build متن‌باز شد!
شرکت SpaceXAI دستیار قدرتمند
Grok Build
رو در گیت‌هاب منتشر کرد. این ایجنت (Agent) هوشمند مستقیماً تو محیط ترمینال اجرا می‌شه و مثل یک برنامه‌نویس کنارتون کار می‌کنه.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
همه‌فن‌حریف:
درک عمیق سورس‌کدها، ویرایش خودکار فایل‌ها، اجرای دستورات (Shell) و سرچ در وب.
🔸
انعطاف‌پذیر:
دارای رابط کاربری تمام‌صفحه ترمینالی (TUI)، قابل اجرا در اسکریپت‌ها (Headless) و اتصال به ادیتورها.
🔸
سبک و سریع:
نوشته‌شده با زبان قدرتمند Rust (دارای نسخه آماده برای ویندوز، مک و لینوکس).
🔸
متن‌بازِ یک‌طرفه:
کدها کاملاً در دسترس هستن (لایسنس Apache 2.0)، اما فعلاً مشارکت و ارسال کد (Pull Request) از سمت برنامه‌نویس‌های خارجی پذیرفته نمی‌شه.
📥
سورس‌کد و دستورات نصب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7018" target="_blank">📅 11:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHWPbR182gIEq2Gmj71AeJ1r0-7FGRU_BD333Mlbz_ol7zz5IX6qoIPZuBGgl9SEq2UiHI65Gr88RQt9s0RHcskWpdcxvbBiirkrB8lPcSBJSgIRGysubzRkDw3iK_nNGiLJuyMmofYFO_s4RszFZCUTuSkuQzOuGcBiE-OxtpKdDtgd-G5ETpuBwuHbylt4TIU-Etcx3s6e3gAFD1MgJJOBh6uAgZQlkq2qkulpqckvRmRtBcTtxBxSkJg7fGCeIfaXVZX3mhjrthQgD8wIC9B0k-FFbbDkH8vdbziTJVJEl4Rsx2enfTr5RxgTun0ud-9HtcgK2jo9dKAr1kZZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ OpenCut جایگزین رایگان CapCut که متن‌بازه و مستقیم در مرورگر کار میکنه
🔥
🔹
این پروژه هنوز در مراحل اولیه توسعه قرار داره، توسعه‌دهندگان وعده دادند که امکان دسترسی به ویژگی‌هایی که در CapCut فقط برای مشترکین پولی هست رو فراهم کنند.
🔹
در حال حاضر تمام عملکردهای اصلی ویرایش، تولید زیرنویس، تنظیمات خروجی و .. در دسترسه.
🔹
به زودی یه کتابخانه از جلوه‌ها و انتقال‌ها و همچنین یک سرور MCP برای کار با هوش مصنوعی به این نرم‌افزار اضافه میشه.
🌐
https://opencut.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7017" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN6c6fA4NHlMWoGIMIaKq7H4J8ouS1WwW0mcWPHwTzLGApU58USxnC4sNcys5ZLeMlJafqDWL5hbPMRsbg6Iu95jrv3_ND54e5c6bsZ-vIFn8GuoEBh95LDe7s-lKLj93n2c0Hx_DsiASNmeEir6fV6Dc6wu0nt-BHh79H6XbKjb9C5JjJoVoI8bpfP-KIpFMNsjgWe0Dls_xQ4FGh5c_eCud0F_gnFteJy0__G6wxZngpFRhdfUPzoH_ZbOR2ozSl2Eb6awC3bJkR3RG1lKEfma4SwnefdRoRsgMjuZnNccaQ9QHD9KFWLvsb2fxdjm8Qc8nIpNYXgFeasODNsXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
یه کتابخانه عظیم از دوره‌های آنلاین رایگان
با CourseCorrect میتونی هر مهارتی رو یاد بگیری
🔎
فقط بنویس چی میخوای یاد بگیری؛
سیستم خودش دوره‌های مناسب از منابعی مثل Coursera، edX، یوتیوب و… رو پیدا میکنه.
✨
اطلاعات هر دوره:
🔹
زمان تقریبی یادگیری
🔹
سطح موردنیاز برای شروع
🔹
چت با هوش مصنوعی برای بررسی اینکه این دوره مناسب تو هست یا نه
🌐
https://coursecorrect.fyi/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7016" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcMgTdKUdbxKarrJ3KHSDIJpTlRFQtXoVqdygycODKxz7k1e3q2EhOI8AwW6FvsByw2FWBYn0ExYTbU4aK3tYpk_wdqM_uk7nq7ybEuyYzq9cCls36MoII89sVlYakAngqxptFFGirfYQEfqeaNsQz2TaNeVp3QP_O-XkoaL-W907C39NdCYiixIJQnsbqJOhfoYerkfj2u0QStw5LC2x6dT6MyfrcIzVPli-XFiZjA0TiA1VnB6Aht7B4OJpuHbRf8T4lGAdQv4A-DEdHVb62_eF273d2FARjjaYzYzBGGJ7FEa87VUtqrFaC61ZzAzS-4dIxEPqOYja6qAW1R-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
دور زدن محدودیت‌های پولی مقالات با یک کلیک!
این افزونه مرورگر به شما کمک می‌کنه تا بدون نیاز به خرید اشتراک (Paywall)، به متن کامل مقالات در سایت‌های پولی دسترسی پیدا کنید.
✨
این ابزار چطور کار می‌کنه؟
🔸
فریب سایت‌ها:
افزونه خودش رو جای ربات‌های موتور جستجو جا می‌زنه؛ در نتیجه سایت‌ها تصور می‌کنن با یه ربات طرفن و کل محتوا رو رایگان نمایش می‌دن!
🔸
استفاده از نسخه آرشیو:
در صورتی که سایت خیلی سخت‌گیر باشه، افزونه به‌طور خودکار می‌گرده و نسخه ذخیره‌شده (Cached) همون مقاله رو براتون پیدا می‌کنه.
🔗
لینک دریافت افزونه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7015" target="_blank">📅 09:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7013">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=MhURvBgxElQzbkf0i4ijwxj6VZ2by88t782XwwpSd-ht2XqQEVOmvgM0-eCaxeuT78HzrKROP0J_dGJn9X-l1LHaNwewJF6tY49zNH2D-nS0_Ar66_jetL-ICSthRSJm-8YazhkRvWPBy2pn74D_6A2Q5HOo-vFGiyPn4LbH_ry5NaiaL6KJOiYKkVryy17CWdqHLb2DIDbV9nETHWzogQ8xH1fRAbI57GyabFuvreWt5Fnr1fI9so7RvHO74qFlj-44odvtHas2eUBAIOcCuPJMXmbSh-QLnXKUB5ENbcO2uWTQWYFEBgVHr6alVuciHa4NOuZSAysMYesP1nemgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=MhURvBgxElQzbkf0i4ijwxj6VZ2by88t782XwwpSd-ht2XqQEVOmvgM0-eCaxeuT78HzrKROP0J_dGJn9X-l1LHaNwewJF6tY49zNH2D-nS0_Ar66_jetL-ICSthRSJm-8YazhkRvWPBy2pn74D_6A2Q5HOo-vFGiyPn4LbH_ry5NaiaL6KJOiYKkVryy17CWdqHLb2DIDbV9nETHWzogQ8xH1fRAbI57GyabFuvreWt5Fnr1fI9so7RvHO74qFlj-44odvtHas2eUBAIOcCuPJMXmbSh-QLnXKUB5ENbcO2uWTQWYFEBgVHr6alVuciHa4NOuZSAysMYesP1nemgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
انتقال فایل بین تمام دستگاه‌ها با PairDrop (بدون نیاز به نصب)
ابزار متن‌باز و تحت وب
PairDrop
سریع‌ترین راه برای جابه‌جایی فایل بین ویندوز، مک، لینوکس، اندروید و iOS است.
✨
ویژگی‌های کلیدی:
🔸
انتقال محلی:
شناسایی خودکار دستگاه‌ها در یک شبکه Wi-Fi.
🔸
انتقال از راه دور:
اتصال دستگاه‌ها در شبکه‌های مختلف فقط با یک کد ۶ رقمی.
🔸
امن و مستقیم (P2P):
ارسال فایل‌ها بین دو دستگاه بدون ذخیره در هیچ سرور واسطه‌ای.
🌐
اجرای مستقیم:
pairdrop.net
🔗
سورس در گیت‌هاب:
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7013" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehct-EEJQ9PejGkTg1LlEgIhnhiOPd2HR6bGJEhWb757lHfGIMetT-Fx2ABhCdNEjdtQ9huGEfMSguWpZemNyFseg5VOoBvnv7HghvDQw9ywOGV5rUNQfobUdzjkoRS4FiO8XIRSseIIz_xgqMBdznfAORxWmLqg3zFha766gJe0Db-ibDmoA4ftjr5NSFTIUoX9YDPpsnf7guIDH9p1XIOBNNZpwdqRfZVGKoNuH2EKNKfR0kV-9NLxQOGB179G6Wpd_xCz4PsNjnL019Nx-WoJZuq_ukwKO0imeT-dxrPIqHVOGaougeOyChKppjd0CoFlrW2eqtq-AbDlfsR0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دریافت اکانت ۳ ماهه رایگان Avira VPN (نسخه Prime) (
تست نشده)
یه فرصت عالی برای دریافت اشتراک ۹۰ روزه و کاملاً رایگان فیلترشکن قدرتمند آویرا، بدون دردسر و خیلی سریع!
✨
مراحل دریافت اشتراک:
🔸
مرحله اول: وارد لینک کمپین آویرا بشید و با یه ایمیل (واقعی یا موقت/فیک) ثبت‌نام کنید.
🔸
مرحله دوم: ایمیلتون رو تایید (Verify) کنید و یه پسورد برای اکانتتون بسازید.
🔸
مرحله سوم: وارد داشبورد بشید؛ تو بخش وضعیت اشتراک (Subscription Status) می‌بینید که اکانت ۳ ماهه شما آماده استفاده‌ست!
📥
لینک دانلود اپلیکیشن از گوگل‌پلی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se3v_tlEwm_mZ8LOH32z9IHctkdX4CuVNLJsbh0Dn8kabJNlzuh3uJhlgOcTslus4kwd2HA21UFJ4ZQKL8O9QU6IDaMOIrk2_pY9eTrTn7lcGFaRfmgju7XRD7hJQ2RuiUOrDDsxI4r_NOyc_po96gkH3idYtj6-hgt-qA85AWnTkLagQJGCbl-bPJWQOL5-7DbWENhnm9NlVIxKig-67c7qh_VMUATrBvM5yXHPNKSL-bmVuy3Kj5werqPHpoeJtQcBpHT0F9clrg5A1jVhP8tBpP4DjfOo9I93YZdd6JXb8hPTYnFAYjF3RaonuG9P58SXi_Nu0wFbcwuDEwPJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)
اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار
Aether-GUI
اومده تا همون قدرت رو با یک رابط کاربری تر و تمیز و فقط با یک کلیک در اختیارتون بذاره!
✨
امکانات برنامه و تغییرات این آپدیت:
🔸
خداحافظی با ترمینال:
دیگه نیازی به دستور زدن نیست؛ یه دکمه Connect می‌زنید و تمام تنظیمات و اسکن‌ها تو پس‌زمینه خودکار انجام می‌شه.
🔸
ارتقا به هسته جدید (v1.1.1):
مشکل اتصال فیک کاملاً حل شده؛ پروکسی SOCKS5 فقط زمانی فعال می‌شه که تونل واقعاً تست شده و ترافیک رو عبور بده.
🔸
ریکانکت هوشمند و اتصال سریع:
برنامه آخرین مسیر سالم رو یادش می‌مونه تا دفعه بعد بدون اسکنِ کامل، درجا وصل بشید. اگه اتصال هم قطع بشه، خودش خودکار ریکانکت می‌کنه.
🔸
فوق‌العاده سبک:
مشکل مصرف پردازنده برطرف شده و مصرف CPU برنامه وقتی مینیمایز (تو بک‌گراند) باشه تقریباً صفره!
🔸
پنل پیشرفته:
می‌تونید پروتکل‌ها (مثل MASQUE یا gool) و نوع اسکنر رو خیلی راحت با رابط گرافیکی تغییر بدید.
این نسخه در حال حاضر برای
ویندوز
(فایل‌های نصبی exe. و msi.) آماده شده است.
📥
دانلود فایل نصبی (از بخش Releases)
🔗
صفحه اصلی پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7007">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppZS2AURexOWjvvkLw7GFdqdAEI-FSk6YXemzwjTcKxjhhUz3xE1UCiA2g7tKDAUrEgQx6Zii8j2K9rbXndgc1PV_EYtasLsKJ5Qb7IN5IAyJ0mCdNjtEIfAO89jkOrkswnlGyxPYuTvchUhmyC3wCDQTyKfMMI30EdFU5Pyt-jRiMi8lbY2sBo-cKNPDRJubJ9gyH8TLs3dXqXIzZDzx9h0T2z_-jY38AWpkUyJ_kf21SMI48ayj-i3jxN0Ftgc6FpGvHuj4kYwRibZkrLthm8TRF3vr7QQdfKVJSxUXiAPBi9LWIRRbzy0x81xq92EArhzZgsTSNaoTB6UATq10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید و خفن Aether (نسخه 1.1.1) منتشر شد!  تو این نسخه کلی از باگ‌ها برطرف شده و امکانات جدیدی اضافه شده که اتصال رو خیلی پایدارتر و راحت‌تر می‌کنه.
✨
تغییرات مهم این آپدیت در یک نگاه:
🔸
خداحافظی با اتصال فیک: مشکل وصل شدن ظاهری برطرف شد. پروکسی SOCKS5…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7007" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7006">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7006" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox
این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی در چند قدم ساده:
🔸
۱. نصب پلاگین: ابتدا پلاگین Bepass را دانلود کرده و داخل برنامه Nekobox (نسخه ۱.۳.۴ به بالا) فعال کنید.
🔸
۲. ساخت ورکر: فایل Worker را دانلود کرده و یک ورکر جدید در Cloudflare بسازید و کدها را داخلش آپلود کنید.
🔸
۳. تنظیم آدرس: به انتهای لینک ورکری که ساختید، عبارت /dns-query را اضافه کنید.
(مثال: https://name.workers.dev/dns-query)
🔸
۴. ساخت کانفیگ نهایی: لینک به‌دست‌آمده را داخل «فایل خام» که در این لینک (Rentry) قرار دارد، جایگذاری کنید.
🎁
راهکار سریع‌تر (کانفیگ آماده):
اگر زمان یا حوصله ساخت کانفیگ را ندارید، می‌توانید مستقیماً از کانفیگ‌های آماده‌ای که در همان لینک Rentry
قرار داده شده استفاده کنید (فقط فراموش نکنید که حتماً باید پلاگین را روی نکوباکس نصب داشته باشید).
با تشکر از یوسف قبادی عزیز
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7004" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7002">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDk59lvrNxJpvX3Vah5XzP__aYeWDK9Tkas9NwmStZkL3dlP-xE2anLiSbW6HMe1A3_GeEe4CB25dyNjiETrpIW_TviK7WcAfjsmaVvMiaH6VA9sJ9HfTj68jYB4R25wkv6F22lPvlye4d5QucU8CD2WCTOWV_Qz61MJIghTTToyUs8K4weDdYaBbWB5YkgU2MVb6RESZFpjEZKhpRe94gfehO-c7dsYBoFjacl1XyO-BAWdDACVR6JpD_Hh2a34_vccf7qT240UhN9JmHU8o_vlXFY4nqMnPrh94YrpsmZdrSEsC8mJRWviDGZXa18GuNqyz1nhPB-rsZMdGP9Djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی Consensus؛ موتور جستجوی هوش مصنوعی برای تحقیقات علمی!
اگر دانشجو، پژوهشگر یا حتی یک فرد کنجکاو هستید، Consensus یک موتور جستجوی مبتنی بر هوش مصنوعی است که پاسخ سوالات شما را مستقیماً از دل مقالات و منابع معتبر علمی پیدا می‌کند.
✨
ویژگی‌های این ابزار در یک نگاه:
🔸
دسترسی به پایگاه داده عظیم:
جستجوی هوشمند در بین بیش از ۲۰۰ میلیون مقاله و سند علمی معتبر.
🔸
پاسخ‌های مستند و واقعی:
ارائه جواب‌های کاملاً مبتنی بر فکت و شواهد علمی (به دور از اطلاعات زرد و نامعتبر اینترنتی).
🔸
استخراج هوشمندانه:
پیدا کردن مرتبط‌ترین تحقیقات و استخراج نکات کلیدی آن‌ها در چند ثانیه.
🔸
کاربرد همه‌جانبه:
یک دستیار عالی برای نوشتن پایان‌نامه، مقاله‌نویسی، یافتن جدیدترین دستاوردهای پزشکی و تحقیقات شخصی.
🔗
آدرس سایت:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7002" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7000">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMYatE9DqAHe2gY6wM9jR2M8Spq-Is9XfIRviYqwKDi98U1IyjKEbd0QJXpt0AtIqAXVIdZkGH2riu_zKiFj0cV4BTeyvFCwGZKUqjTVU-0yqqBYDQ8DHzMJaZd6d9lzcT3Zf4tRwkzPW0R3n8i0KnzcARj6HT0W9qplFwq1xQSI_77cDlR9ohld_DoZNe5n2GsaZEEdSR7bsqwdwNhKh1WFt8tDgaakdn7fNLcrSWY5mNJtt1JmXKy2REDGc0G2kIQ1xLJQnDvFEY6lnzNPtL2iBtRMtZvTysBRNIY4LcSmRa7TBcINQ6ClR8Wmi3HikLGM-dBDuEn7PBs_YUX9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
Universal Installer؛ همه‌کاره‌ترین نصاب برنامه‌های اندروید!
اگر زیاد برنامه‌ها را خارج از گوگل‌پلی دانلود می‌کنید یا با فایل‌های چندتکه سروکار دارید، این ابزار متن‌باز جایگزین بی‌نظیری برای نصاب پیش‌فرض گوشی شماست.
✨
ویژگی‌های اصلی در یک نگاه:
🔸
نصب هر نوع فرمتی:
پشتیبانی کامل از APK, APKS, XAPK (همراه با OBB) و APKM.
🔸
نصب خاموش و گروهی:
نصب و حذف بدون نیاز به تایید مکرر (نیازمند Root یا Shizuku).
🔸
جعل هویت (Spoofing):
گول زدن سیستم برای اینکه فکر کند برنامه از گوگل‌پلی نصب شده است.
🔸
شخصی‌سازی نصب:
امکان داون‌گرید کردن نسخه‌ها و دور زدن محدودیت‌های SDK.
🔸
سد امنیتی:
اسکن خودکار فایل‌های نصبی توسط VirusTotal.
🔸
انتقال محلی (LAN Sync):
اشتراک‌گذاری و نصب راحت فایل‌ها بین دستگاه‌ها از طریق Wi-Fi.
🔸
طراحی و پشتیبانی:
رابط کاربری مدرن (Material 3)، بدون تبلیغات + نسخه مخصوص Android TV.
📥
سایت رسمی جهت دانلود (گیت‌هاب، گوگل‌پلی و F-Droid)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7000" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFzhMbWgH5K-RHAM5KkQhF83L8zA0-C2ppCRgY0iJLAz0JIs02kJE4bh4AuilvaXQ-yRskHJH4kNnIUJm-S1294SvVIWxDB6pGuyFDeLKjTY0mIUjkrm5IBZV42OvWIMxIIBpE9JrPj7SNKizAHkRN0kz3geQdNVP_rPoOlT9pBV51yMbBP3nPgkPtIoi8UaZVa0H30S_ALR7hxVL8Uq4lfYkU_LiiPL9vTA1DglHOC5VtfT3gQzmePMQU2ZK16NuauH8LwsfBSN1lfCwB4wis5reJRHKTaLgRpt6ES0ZOsfPob5GvFPaDBIu6Z8cP-UroNRN1Zin6xPj-iiUygZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTEsblD8mU6zkzlmbS5pQkwr02X3-wOXAJEpNkprMTOZk4Ao83CIwP9cpIKkEYv2OeIpCuIsVvNX1JFKwjCHA-823SEc2X0EwyXzNRCMX8mWO_YzGxioifo5g9FQe9KfPWAvJTtBzuKp-Sm70gVtnLKkDIblY_jyE0cAB0nXefdPpzQb1KE4AN_7XddDWJdn9ZHOKe94xw2ZMCfeqqMFIpgLjtRYqSwmY4hL9gHmrj-l3EsWJkvc7UDpC5WD-5zrPP31pkSdHThVUEDUCBkdTQgoiv0xbwhTJVlnxfbjJL0O4GX1T9XzMTKCF4fpruqZ90z4LNQmM6prkNnbPnkrWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گوگل برای ۲۵ سالگی Google Images سورپرایزهای بزرگی
معرفی
کرد.
🔹
تولید تصویر با مدل Nano Banana 2 Lite داخل Google Images
🔹
طراحی جدید و مدرن صفحه اصلی
🔹
گالری شخصی‌سازی‌شده شبیه Pinterest که با توجه به سلیقه کاربر تغییر می‌کند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6997" target="_blank">📅 18:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk1hbDIr0KO3LqzAWgwGJ_XhhJkH3xZSDwxB_h4lS7YlfVFJjvmmQKC-MLL5Wq2JKjzjHCpa_oVdmJse4BtRwwfWmKU3gmBL6FCOoCcdC1TXA-MlrQLKitRjKkAdFgA0qk-0_j4r5HLutPCRYgmrbLy81Hn3b8BRp_ZRTIETOtb1HXzJ-8I7Eia0tUgBFYvfm7NBmInbQhVBLj-WiasrHZBtHx7thFiq4919aV3IRvd3drijdbKPMDRZipn7o8bUMXDc50hOVxuVPsIs7XK2gb2vcWdd7S0FCUf101PbD5G9ji4CIvQAQf26GGXA8iPe3yOmGWQyATNFBTJuseKojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه آب خوردن  کلا ۱۰ ثانیه هم طول نکشید
😐
ولی وصل نشد رو ایرانسل برام
😐
😂
😂</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6996" target="_blank">📅 17:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUR5YENrOvRO-9Irh_jPH6JT_9cL_Q0n4_0pcQiZZU0XhJ-y9VTrYFJuUoU3j2kxvHC8cGiKd_ePwM6oma0Fn3r_Sp6cZwMIJtQdqH0W5aqdLTPFGnx4FlqWWgduQsv0mrXOMwEJjoW_vQXwc1lpPaWdQnpDMlweX6U_oB0n8LME9PeJVvBZaGhsXkm09hChySqnuiPX-Atstivg8KMJvUr4cm3WWhfrDdEX70Gy6wg-v1fFgjJSKsMFTN5cfN8VzEdv_-CvZ0o_sdKyyxjBgbRD8d5_f0auMok8sUw8NKFYzzVMbfN74abivIBAJalLcBaKtRbeSWH4hkNrFyyJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6995" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه
پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز می‌کند.
✨
ویژگی‌های کلیدی:
🔸
بدون نیاز به سرور شخصی:
سیستم به صورت خودکار سرورها و مسیرهای سالم (Endpoints) را پیدا کرده و متصل می‌شود.
🔸
پنهان‌سازی ترافیک (MASQUE):
ترافیک شما در بستر HTTP/3 و HTTP/2 کپسوله می‌شود تا کاملاً شبیه به وب‌گردی عادی (HTTPS) به نظر برسد و مسدود نشود.
🔸
امنیت مضاعف (gool):
علاوه بر پروتکل WireGuard، از حالت وایرگارد تودرتو (Nested) برای ایجاد یک لایه رمزنگاری اضافه پشتیبانی می‌کند.
🔸
کراس‌پلتفرم:
دارای نسخه‌های آماده برای ویندوز، مک، لینوکس و اندروید.
📱
نصب سریع در اندروید (از طریق Termux):
برای نصب خودکار، کد زیر را در محیط Termux کپی و اجرا کنید:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
پس از اتمام نصب، کلمه
aether
را تایپ کنید تا برنامه اجرا شود.
ابزار پس از اتصال، یک پروکسی SOCKS5 (به عنوان مثال روی لوکال‌هاست و پورت
1819
) در اختیار شما قرار می‌دهد که می‌توانید آن را در تلگرام، V2ray، Nekobox یا تنظیمات سیستم وارد کنید.
📥
لینک گیت‌هاب (جهت دانلود نسخه ویندوز، لینوکس و مک)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6994" target="_blank">📅 17:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6992">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ_CgC37QXwuuJoZPWC4zvgF4yXgFKHReGhMH6X1B4vx1m8wSunjP9HKNlswIy6ZXT2Yr5JLaAFosnlA1851YsM73W_o6REKk9eLy49FVZzW1rP-jdT_CiiAcs83qvZ327SvTJ2czd0YACChFmDJk1D-983PLuHgt8-Vg45ntudhiN4SEDZApmHq3ukYd50LmfFOwB39ol98F0parNW3xyIlKsb6CQyGyYNClXtGKkD_bHBwH08W6coMsASZRjHvATYTrm3B85w2Z1klssCiawNhb8X_SOeSOAkehyflyvaCZbrZJdE2lwJbuCp2QjA1ad05HLVa3Zv09aXtjS4TMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)  مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را بدون نیاز به دانلود و…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6992" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6991">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlMjGGre9KmdDzx04Y2RKi7aC-d_t8cTj_MJ-jGHlN_hDxXMcIgCpOEOCQEvUUzhtz1z9VSw2bg6cq8VwqGS28Zy6rs3g7mY4vr2Y2WluFjCHCdJW3nV_82LxJD61qOGNac3GChbNeUmtIX9kzKaAbP2JOkjrvLgZq8UruN58sBQpfQ2eT314QbmXoU-d6e1G9amMbM5RbmpxvdlBQKsFZCXUkTcqOt-aT0jqtXLCiwmloigfFTa-5WxUzrJGdkAYCfJml62BJLDNaNP-CWOmmUeI1ZhjfTCmuac6G7Vd8VY7dv9DMV4cD01NKYhn2QEWJ4rmSF0-xn75008UNC58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)
مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را
بدون نیاز به دانلود و مصرف حجم اینترنت
، مستقیماً بین فضاهای ابری مختلف منتقل، سینک یا بکاپ‌گیری کنید!
🎁
نحوه دریافت اکانت پرمیوم ۱ ساله:
🔸
وارد لینک زیر شوید و یک حساب جدید بسازید.
🔸
در پنل کاربری، از منوی بالا روی آیکون کلید (
🔑
) کلیک کنید.
🔸
کد پروموی زیر را برای فعال‌سازی وارد کنید:
BAAYK667N5K3K0N6
🔗
ورود به سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6991" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=QYrTJRk6N9FRc9xfYWSmZtNxrLlBVkgl9Ne8NRHF5wUDe9L0hP-Q40w_fDKtP8XlXNWTZw4waHZhq4eYOHBIRGMj5uEOJJpNjp9Nacnm2XNG11ls1nHD3-HIROpMi-0QZBiFyZUjyDHcVbYmTYGGKRc3aSWaOJBKGuwo-kbJ9qUlPr1im8gMClL4jVYLVnnS8eWpavXGag_kxkn-v3wrz1jZWI48SkUTK7DVuf_Mces5kX2BvmY-bU5xl1V2vk-Ae5A_wkUV3uwb80NCG4B26dR3hJWucQhDQ2Iwrr8EAuEocZzUuAM4Cyz0nuxcBFyYtEd-5DWgmlE0W6BcTcKwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=QYrTJRk6N9FRc9xfYWSmZtNxrLlBVkgl9Ne8NRHF5wUDe9L0hP-Q40w_fDKtP8XlXNWTZw4waHZhq4eYOHBIRGMj5uEOJJpNjp9Nacnm2XNG11ls1nHD3-HIROpMi-0QZBiFyZUjyDHcVbYmTYGGKRc3aSWaOJBKGuwo-kbJ9qUlPr1im8gMClL4jVYLVnnS8eWpavXGag_kxkn-v3wrz1jZWI48SkUTK7DVuf_Mces5kX2BvmY-bU5xl1V2vk-Ae5A_wkUV3uwb80NCG4B26dR3hJWucQhDQ2Iwrr8EAuEocZzUuAM4Cyz0nuxcBFyYtEd-5DWgmlE0W6BcTcKwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
نتفلیکس شخصیت رو تو چند دقیقه بساز!
با Reiverr همه فیلم‌ها و سریال‌هات رو یکجا و مرتب داشته باش:
✨
امکانات:
🔸
جست‌وجوی هوشمند با پوستر، تریلر، امتیاز و توضیحات
🔸
ادامه تماشا از همون ‌جایی که متوقف شدی
🔸
پیشنهادهای شخصی برای وقتی نمیدونی چی ببینی
🔸
رابط کاربری مناسب برای تلویزیون
🔸
اتصال به تورنت‌ها و سایر منابع دانلود
🔸
نصب روی کامپیوتر یا سرور شخصی تنها با یک دستور
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6990" target="_blank">📅 12:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👱‍♂️
پروژه Ponytail
برنامه‌نویس ارشد تنبل برای هوش مصنوعی شما!
✨
ویژگی‌ها:
🔹
جلوگیری از پیچیده‌نویسی (Over-engineering) توسط هوش مصنوعی
🔹
کاهش حجم کدها تا ۹۴٪ و صرفه‌جویی ۲۰٪ در هزینه‌ها
🔹
افزایش ۲۷٪ سرعت انجام وظایف، همراه با حفظ امنیت کد
🔹
اولویت دادن به کدهای موجود و کتابخانه‌های بومی، به‌جای تولید کدهای اضافی
🔹
سازگار با بیش از ۲۰ دستیار هوش مصنوعی، از جمله Cursor، Copilot و Claude Code
📥
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6988" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6986">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent (نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6986" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6985">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNb70HwQ8aTQYimL-jfV_taKvooorrNeFWxM8VL3Xuo0rALmrXWj8-fS6S_YLs5YXlYOGzrleOc_60fgBBW_1KshINoBE6vOEq-g16DZbkmI5UbnQUABnjdVAkWCnPIrHY-kaagGgdHbEA2yka8heF5KgyltvxSKI1FHdI-dgWCLgei_g4ik6mWKKpuOQVsf_qo5-0qw08pD4c3dvWd2PVYZ1CI5obEWRLCIsHR_PQQfgmbYSnrsTP7R24uyhabC7bcYaLyy4LO8MD3WVo6EgXjKbGHLIvrhopsC33V4YspLQyljTxewY5enLXJj_ArFN5ekV51wFYUVOMqQGwIpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent
(نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری خودکار و ساخت مهارت‌های جدید
🔸
اتوماسیون و زمان‌بندی وظایف (Cron) فقط با زبان طبیعی
🔸
دارای اپلیکیشن بومی اندروید برای اجرای مدل‌های آفلاین (Gemma و Qwen)
📥
دسترسی و نصب:
GitHub
,
F-Droid
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6985" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6984">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvVqcCsFc4tXcsr8kLC3NRJCVVnoqyw4HE76G0WIj0Q6oT0e5H-s64RaG6h0ioU4lyDAR2KtffD_M135s2SI1bMSagjXBuTb8Aogb8-W5X3Dx7cOSzsCSQJxOViLT6kHzIuPh9s4TmFCZAFAoncg8sgF_p-0vMfi1fBKo-ftEfOHFiQXeIuvvj0IJw4E_g8G45o4YuNLJuOWoGBtJVMYx1nX1JpPGr3nZfE2UHDmeOUTfn6mD_xtkIgJAwRSGWHRLgi2StyQmwTUlvIZlhRH_wmNVkAdXCdPsEFVCRoHiTYz-kuTCdJBb1gLEiOml5vI6PS2hOOab_IadMvFWjWc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💎
Google Gemini API
دریافت رایگان توکن‌های هوش مصنوعی گوگل!
✨
امکانات:
🔸
دسترسی به مدل‌های Gemini 2.5 Flash، Flash-Lite و Pro
🔸
بدون نیاز به کارت اعتباری یا اشتراک
🔸
ساخت کلید API رایگان در چند دقیقه
🔸
توسعه اپلیکیشن با جدیدترین مدل‌های گوگل
📥
دریافت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6984" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6983">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcuJicEDi9UQbPib99wECdYgvR9WdLv9ZAL28t8OgWYmpdAC8lfEqTk2tfr21W5a4Ag4HdaD1uyUvnoaYizgFjd715nGLKHLtewTafEivcL8Sa_VDx0TkcuYrHSmLknJrmpSwaA2gacGUuEBkVOzanWeQYxHL_kxsMqNk9JJuB6f7JwRRct3en6PjqTFXHsXa5aN1dv1_YmUNdAHYyauHnBsXzIzErSDTAXaUoW9yUxiJEBTX_D-e3RA9PfFx7GIcqZ0TDvAXnzV5l6jbGC-T1SgGq_4MsHU-cQzhRZYVJkbNJOXrKfq2Uegm3kQfB8E04Un-NCYgPoCTaLd0YxowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
هفته توسعه OpenAI
شرکت در رویداد و دریافت ۱۰۰ دلار اعتبار رایگان Codex!
❓
نحوه دریافت و جزئیات:
🔸
ثبت‌نام و ارسال درخواست شرکت در رویداد از طریق پلتفرم Devpost
🔸
مراجعه به تب منابع (Resources) در صفحه رویداد
🔸
کلیک روی گزینه "درخواست 100 دلار اعتبار Codex" و ثبت آن
🔸
مهلت ثبت‌نام:
تا ۱۸ جولای ۲۰۲۶
🔗
ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6983" target="_blank">📅 08:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6981">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite  (جایگزین کروم)  اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید، Cromite دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6981" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6980">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite
(جایگزین کروم)
اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید،
Cromite
دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید روی
حریم خصوصی
و
حذف تبلیغات مزاحم
توسعه داده شده است.
✨
ویژگی‌های برجسته کرومایت:
*
🔸
ضدتبلیغ داخلی (Ad-blocker):
مسدودسازی خودکار تبلیغات و ردیاب‌ها بدون نیاز به نصب هیچ افزونه اضافی.
*
🔸
پشتیبانی از افزونه‌ها:
امکان نصب و اجرای اکستنشن‌ها (Extensions) در حالت توسعه‌دهنده (Developer Mode).
*
🔸
حریم خصوصی حداکثری:
محدود کردن و غیرفعال‌سازی ویژگی‌هایی از کرومیوم که برای ردیابی عادات وب‌گردی کاربران استفاده می‌شوند (قطع ارتباطات اضافه با گوگل).
*
🔸
مقابله با انگشت‌نگاری (Anti-Fingerprinting):
جلوگیری از شناسایی و ردیابی دستگاه شما توسط سایت‌های مختلف.
*
🔸
آپدیت خودکار:
دارای سیستم آپدیت داخلی در اندروید (همچنین پشتیبانی از مخزن رسمی F-Droid).
*
🔸
پشتیبانی گسترده:
قابل نصب روی اندروید (نسخه ۱۰ به بالا)، ویندوز و لینوکس (۶۴ بیتی).
🧪
نکته امنیتی:
این مرورگر برای استفاده روزمره و وب‌گردیِ امن و بدون ردیابی عالی است؛ اما خود توسعه‌دهنده صادقانه تاکید کرده که برای خبرنگاران یا افراد تحت محدودیت‌ها و سانسورهای شدید، همچنان استفاده از نسخه دسکتاپ
Tor Browser
پیشنهاد می‌شود.
🔗
[سورس پروژه و دانلود در گیت‌هاب]
🔗
[لینک مخزن F-Droid]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6980" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6979">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">net.yukh.xui_81000@ArchiveTell.apk</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6979" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6978">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
⚡️
پنل نهان (Nahan Panel)
ساخت و مدیریت فوق‌حرفه‌ای پروکسی (VLESS/Trojan) روی کلودفلر!
بدون نیاز به خرید سرور و درگیری با ترمینال، یک شبکه کامل و ضدفیلتر بسازید.
✨
امکانات برجسته سیستم:
🔸
نصب تک‌کلیکی:
راه‌اندازی خودکار Worker و دیتابیس D1 فقط با دادن یک API Token.
🔸
مدیریت آی‌پی و شبکه:
اسکنر داخلی برای آی‌پی تمیز (Clean IP)، آی‌پی پشتیبان (Relay) و مبدل پیشرفته NAT64.
🔸
مسیریابی هوشمند:
جداسازی ترافیک سایت‌های داخلی (GeoIP/GeoSite) برای اتصال بدون مشکل.
🔸
ضدفیلترینگ پیشرفته:
جعل اثرانگشت ترافیک (TLS Signature Chrome) و تنظیم دی‌ان‌اس اختصاصی (DoH).
🔸
ساب حرفه‌ای:
دامنه اختصاصی لینک ساب، مخفی‌سازی با تغییر User-Agent و نمایش حجم/تاریخ انقضای فیک برای گمراه کردن فیلترینگ.
🔸
امنیت بالا:
دکمه توقف اضطراری (Kill Switch)، مسیر ورود مخفی به پنل و استفاده از پورت‌های امن.
🔸
مدیریت همه‌جانبه:
اتصال به ربات تلگرام اختصاصی (فقط برای آیدی ادمین) و مدیریت همزمان چند پنل (Master/Slave) از طریق API.
🔸
نگهداری آسان:
آپدیت خودکار مستقیم از مخزن گیت‌هاب و بکاپ‌گیری/بازگردانی سریع با فایل JSON.
✅
تا به حال مسدودی روی این پنل گزارش نشده است.
🔗
اجرای مستقیم نصب‌کننده (وب)
🔗
سورس پروژه و پروکسی در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6978" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6975">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVfF6zi042KKbljzfVJ5ZK4qBLKCiL6vb6XmzPGECek6Sh09m7I2yr-uNo5P2HlbJM3MzZWmEop-mqEy4BLZbTenFGFeVVzexI3A3zCSuMOYgvEbSvx56JydjWsCBL72ik5IkGMfKhQ6X6ROrwRGlzKX8JXXA9muGHN7aawAipwQb6XuhhBerMTDzWkfU9lWf4lVSUfHE2-8u5-XGbDqa3OBNbBMotwilf7OS-KCOQbQeSYVZdvJBQmOYjJ2-MwevZwKABVLzLma07IjGR1TCsS0hojwGH9ckhEwuSf_tnwooVgCxg43QIfnOlJ9ueukrq0nBcp6Flvo64ySHN71mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
تلگرام دیگر برای اجرای ربات به سرور نیاز ندارد
❗️
با قابلیت جدید و فوق‌العاده
Serverless Bots
، از این پس می‌توانید کدهای ربات خود را مستقیماً روی زیرساخت خود تلگرام اجرا کنید.
✨
ویژگی‌های این قابلیت:
🔥
پشتیبانی از JavaScript:
کدنویسی مستقیم و سریع.
🔥
دیتابیس SQLite:
مدیریت داده‌ها درون خود اکوسیستم تلگرام.
🔥
میزبانی بومی:
اجرا مستقیماً توسط سرورهای تلگرام.
🔥
کاملاً رایگان (فعلاً):
صفر شدن هزینه‌های هاستینگ.
🧪
نکته: این یعنی ساخت و اجرای ربات‌های کوچک و متوسط، از این به بعد بدون هیچ‌گونه دردسرِ خرید و مدیریت سرور امکان‌پذیر است
🟠
⛓
منبع
👉
🔤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6975" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6974">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6974" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6972">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goUItXrVnJfY67RIZkrSfNtyqvHa1KvMnUBM3vmmAuKDXu1yk5Ym93pBGLoVLe6nl46HnKojytdSlyquKHRQuUPh4BQ2TApXSt0ZahpduJ56bctimDdYGl2ntA3cQgcL319bPZUDu-1SXzhqAygo83KlNVvxXzOAyvLAuiSgB5K8FbYR5nPkSnZFYvYG0PS1LXZfLwmxm05Ejf655rEtBgCTHizLpbPYuUBKLWIJBm1569gQ2NVTMVOeenkXDfYagCVp7nOdnfOUVPhB-fvFBN9e8InahilnPEmMVRxVK7G2gdJPI0ATJhfBkpi89MrYnmMnnSjPQhpg9adi5CBBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
3X-UI Manager
مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع
(فقط نسخه +3.3.0)
📥
دانلود:
F-Droid
و
GitHub
و
Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/ArchiveTell/6972" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6971">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acewDz1gfYANM2Y5p6q48wEuqm4XxJNdxlVVi2lZzALFLjz42gnZDxHhunqJcD_2ZoqY2Xvp-teWLlpYLzwMQ-kBjy2o2zsPlcm8xPmxrYbcXQ8UOqiznQr9IpavkuUmqAwreshqcnI7QfEv11o3Yc05B7Mg1Cr-ZGRqBTpMheowaGQxc88hepnjzvNiG0eOqZzYWKRtr8FSzrTDHizwoK6e7N71MjVcxkO40lHxuctMWTUTxb2GtNXXc2lz5TwlJWIqTIyQI0E22JKT76g9PVi4joZgpYiZaaPGHpfU-ZWVCBM9_ny0vcUVAPBfJisBBTnTtjgSyXeEZ3Tj2aVHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Droid-ify
یک کلاینت (رابط کاربری) مدرن، روان و فوق‌العاده زیبا برای مخزن بزرگ F-Droid!
اگر از سرعت پایین و ظاهر قدیمی کلاینت رسمی خسته شده‌اید، این اپلیکیشن جایگزین متن‌باز (Open-Source) دقیقاً همان چیزی است که نیاز دارید.
✨
ویژگی‌ها:
⚡️
سرعت بی‌نظیر:
همگام‌سازی (Sync) و لود شدن لیست برنامه‌ها در عرض چند ثانیه (بسیار سریع‌تر از نسخه رسمی).
🎨
طراحی مدرن:
رابط کاربری چشم‌نواز، روان و منطبق بر زبان طراحی Material You.
⚙️
نصب و آپدیت خودکار (بی‌صدا):
پشتیبانی کامل از ابزار Shizuku، دسترسی روت و Session برای آپدیت برنامه‌ها در پس‌زمینه بدون نیاز به تایید دستی.
📦
مدیریت آسان مخازن:
قابلیت اضافه کردن و فعال‌سازی مخازن جانبی محبوب (مثل IzzyOnDroid) تنها با روشن کردن یک سوییچ.
🧪
نکته:
این برنامه در واقع یک پوسته سریع‌تر و بهینه‌تر روی همان دیتابیس امن F-Droid است و امنیت شما را به هیچ‌وجه به خطر نمی‌اندازد. اگر از برنامه‌های اوپن‌سورس استفاده می‌کنید، نصب Droid-ify یکی از واجبات است!
📥
دانلود از GitHub
و F-Droid
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6971" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3ban2JQgylEpQ4XfLtRJP2HsTrFux4HeNVqumWC6a0Ytrt1ELCRD-yYcBtm7n48OK09ZqLMSMWgETm21M7OPp1QYE8bGQZqdSVBEKQLx3Y2_q5ma5gi2-mWQXBjXeXjgRi4xInMtE_O2Rd0eyQD_RK7MeemL-LU_C2ei_MAuSt-moq_MQW0MrS1tyOZTOVRrlehMr4iaR60CBkcv8FoxYRtXo3LhUKkO2EkT4cUS-Vg64nyTPvzpPAOOZG7utwRwFYOrGrOGXRJlwsOjESiaMd3ZR2ktk3Eqp-PP1SX3xGPO5d0gIDs4jOSh5OhF5QI7QekgQG_03tkvckI_tlT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHkCQPz3ygB5f1XZrG_VKRk1LdVu-KvNdHQAe8MR1AWYucPPG7zerZHIDkEx8npa6-DTk3oJb1nBgMkgjqTCBGkmbk1Bzd0D3gCou5o6irTxav7zCu0l3D_47NjLx8jS-Xvrjn5vmhF8uQDtcZsmxCHATLkeQCAgUHQW-tNzOs68dC9N8V3-G-q4WlZ8WS8otVYd9H5IfE9Si_gU8G9WtkfcNSN2sl2bk8kaBCpKw8Lplk7mhkypg5x-odFZk3sM1ZSpuoQ5VYgkKqFWAh-cGnG4jEeeXgp48VyBWuHPn1GIPrMtKoXZfUJhaQqMqsybAcBq9oBCt3qScGLFQwTaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQjyqE6o0-ryPBWaes6VgCUXtnnZLAgi5ylxzxRr346zp6K2tyAmpkgvc_pKUl5kBBCjBvQ7FDLtlBs7yZkCjOq5j2PV30NDHHnNQBKT_cezq_BC1kKOfEX6uOpW6fyrtj7MQ0iX4hY7r3NpNXogHN3sPb2fG8sPhha-zxpmTlfpWIFgOaIAFO6iWJR7Db5FA8OQLD00UaBLq9yahcJgeh5ILtemq6foFYcN-9rmKjXQoSUVseydvYuVl5Mx3rtjH9WqOQHQftJkEw0YuL5f5TdkyBv8mypNOD-6K5sHXzVQPZC5lELNf39VAXufOvPJVlwuTcgMmFuAqgpyXiBckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMjmRlTwFzruf6UlrzyhUiPMwt6z2JQCJUiTcvj9jQB6vvva0r6cxCYpdWPtvBSWx2F4-8bZKONYyBPDfYVV5AGYUmOfFXfI2V4_QrO2EccqS1l0Pz8Pr0TMtjcGr0CIS-6_olN9WoNPcxu_j_tlMBFrCjvG3mpcG_N9_fbonFF_urMGh0LvbjMIEbswkdEsgGKbN97NRyyqu1dORrTElblHS798XI_jFJexvi97d47yLh6QQVBbYw0ze4-6Yhy7sT1rscup3DYmj-Bo_8ZDgWRlPjvc87ZCzhXNwkJxh1ULMhg8RVodqSNVU0jYdV5jmByC4EUlODLZCagrOqLEZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
آپدیت بزرگ تلگرام با ویژگی‌های بی‌نظیر منتشر شد!
تلگرام به‌تازگی یک به‌روزرسانی عظیم دریافت کرده که قابلیت‌های کاملاً جدیدی را به این پیام‌رسان اضافه می‌کند.
✨
ویژگی‌های این آپدیت:
🌐
بخش «انجمن‌ها» (Communities):
فضایی جدید و یکپارچه برای تجمیع کانال‌ها، چت‌ها و ربات‌ها در یک مکان واحد.
📝
ویرایشگر پیشرفته پیام‌ها:
ادیتور متن تلگرام دگرگون شده و اکنون از ابزارهایی مانند
جداول
،
چک‌لیست‌ها
و
عنوان‌بندی (Headings)
پشتیبانی می‌کند.
🤖
تولید محتوا با هوش مصنوعی:
از این پس هوش مصنوعی می‌تواند مستقیماً بر اساس درخواست شما، پست‌های آماده و کامل ایجاد کند.
🕵️‍♂️
پیام‌های خصوصی مخفی:
ربات‌ها قابلیتی پیدا کرده‌اند که می‌توانند پیام‌های خصوصی ارسال کنند؛ به‌طوری که این پیام‌ها حتی از دید مدیران چت نیز کاملاً پنهان می‌ماند.
🧪
نکته:
این به‌روزرسانی به‌صورت تدریجی در حال انتشار است، بنابراین ممکن است این ویژگی‌های جدید هنوز برای همه کاربران فعال نشده باشد و دسترسی به آن‌ها کمی زمان ببرد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6967" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6966">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOVwB2v25KOxzAW3U1CCJdLjIfP2XJ8aDNiVdxXjRv9hHmF4OZHs03IaZgO--dZX31BSDknk7x_t1XQEdiJpwtIr2DkFhfJcbThUTk8hdTZ9af7wHGefjcz84kKuz6GA07Xk0GKMRhJxgIj1HDhLT_IjMcV-0oNuReXQL08f3MwBZdZALqMNA_S8lD6n86_0_CHUpo7pLWHoWEXWIS5yIryXZz12Eeo1OeqwH7L8d1ecBXrqoETvcftsWSUK67VwUwl7hDfXfTpvY-qj5nVzqFwZrnT3YLuKQXJljTTCat7dwGQeL_335xPBJq9D7dQuNXm1P2Dt4PY_UwG4mcVZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Acode
یک IDE تمام‌عیار و ویرایشگر کد بسیار پیشرفته (Open-Source) برای اندروید! با این اپلیکیشن می‌توانید پروژه‌های برنامه‌نویسی خود را با امکاناتی در سطح دسکتاپ، مستقیماً روی موبایل یا تبلت مدیریت و توسعه دهید.
✨
ویژگی‌ها:
🎨
پشتیبانی وسیع:
رنگ‌بندی سینتکس برای
+۱۰۰ زبان
و پیش‌نمایش زنده (Live Preview) وب.
🛠
ابزارهای حرفه‌ای:
اتصال مستقیم به
GitHub
، مدیریت سرور با
FTP/SFTP
و کنسول داخلی JS.
⚡️
قدرت و سرعت:
اجرای روان فایل‌های سنگین (بیش از ۵۰,۰۰۰ خط کد!) و پشتیبانی از کلیدهای میانبر کیبورد.
🧩
شخصی‌سازی عالی:
سیستم پلاگین‌پذیر (دارای افزونه‌های هوش‌مصنوعی)، سازگاری کامل با تبلت و
منوی فارسی
.
🧪
نکته:
این برنامه با مجوز MIT منتشر شده و دارای قابلیت بازیابی فایل‌ها (File Recovery) برای جلوگیری از پاک شدن ناگهانی اطلاعات است. (اجرای آخرین نسخه نیازمند اندروید ۸.۰ به بالا می‌باشد).
📥
دانلود از Google Play ،
F-Droid
و GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
⭐️
Cyru55</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6966" target="_blank">📅 17:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6965">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay9X9emiJA9TkH_1kfku14yCj5o8VMnBDigW2sKM-0F-tP32DNzp5FjFDWb_X6gV5mFh2-s6wQzG3cb9hp9MHtDdJwxjZUKZ_B4LGl4UXDr5CVJlzfqa9u6IwWmbXfjUXhMSqVURvCO7UjN-Odl9c320XalPCkHb2NBzenJ2o9jWsMMkNNEgdNYLBn1jVqK2agAX-GD8Smo-H6VuznAQsCw3UB13iPCj_WgGR7_Zx8s2lk-BbmxVyNocM6RPphrmNAq6AG3qDm3QRaswEFCkBmT5cR_wM1ieDcPmYcqv317fS337S6A8U3QIvQIXXcgrSpkdSjIORYwCqurfPguUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
وقتی هوش مصنوعی علیه هوش مصنوعی رقابت می‌کند!
در یکی از آزمایش‌های جالب روی مدل‌های
Sol
و
Terra
، رفتارهای غیرمنتظره‌ای مشاهده شد.
🔹
کارتل قیمتی
مدل
Terra
پیشنهاد داد قیمت‌ها را با هماهنگی افزایش دهند، اما
Sol
پس از پذیرفتن پیشنهاد، آن را گزارش کرد و حتی خواستار حذف Terra شد.
🔹
اتهام به رقیب
مدل
Terra
در مرحله‌ای دیگر، برای حذف
Sol
او را به تقلب متهم کرد.
🔹
رقابت بر سر درآمد
مدل
Terra
با کاهش جزئی قیمت‌ها نسبت به
Sol
، مشتریان بیشتری جذب کرد و درآمد بالاتری به دست آورد.
📌
این آزمایش نشان می‌دهد که مدل‌های هوش مصنوعی در سناریوهای رقابتی، گاهی رفتارهایی شبیه رقابت‌های دنیای واقعی از خود نشان می‌دهند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6965" target="_blank">📅 17:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6964">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
مدل بی‌نظیر GLM 5.2 به نرم‌افزار Trae اضافه شده؛ کاملاً رایگان و نامحدود!
اگر اهل کدنویسی و دنیای هوش مصنوعی هستید، احتمالاً با
Trae
آشنایی دارید؛ یه ابزار و دستیار فوق‌العاده هوشمند (Coding Agent) که کارش راحت کردن زندگی برنامه‌نویس‌هاست. حالا خبر جدید و جذاب اینه که مدل پرقدرت
GLM 5.2
به این پلتفرم اضافه شده و می‌تونید کاملاً رایگان و بدون محدودیت ازش استفاده کنید.
🤓
من خودم هنوز این مدل جدید رو فرصت نکردم تست کنم ولی Trae کلاً سیاستش اینه که مدل‌های خوب رو رایگان ارائه میده، اما قبلاً یه
صف انتظار طولانی و رو‌مخی
داشت که آدم رو کلافه می‌کرد. نمیدونم واسه این مدل جدید هم همون بساط صف برقرار باشه یا نه!
🌐
لینک سایتش:
🔗
https://work.trae.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6964" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
🎙
Voicetypr
ابزار متن‌باز و قدرتمند برای تبدیل گفتار به متن به کمک هوش مصنوعی. جایگزینی عالی برای تایپ صوتی که در پس‌زمینه سیستم‌عامل اجرا شده و همه‌جا در دسترس شماست!
✨
ویژگی‌ها:
*
🔸
تایپ سراسری (System-wide):
با فشردن یک کلید میانبر، در هر نرم‌افزاری (ادیتور کد، تلگرام، مرورگر و...) صحبت کنید تا متن بلافاصله همان‌جا تایپ شود.
*
🔸
آفلاین و امن:
پردازش کامل صدا روی سیستم خودتان (Local) به کمک مدل‌های Whisper بدون نیاز به اینترنت (پشتیبانی از +۹۹ زبان از جمله فارسی).
*
🔸
سبک و فوق‌سریع:
توسعه‌یافته با زبان Rust و فریم‌ورک Tauri با پشتیبانی کامل از پردازشگر گرافیکی (GPU در ویندوز و Metal در مک).
*
🔸
ویرایش هوشمند متن:
قابلیت اتصال به API مدل‌هایی مثل Groq یا Gemini برای اصلاح لحن، یا تبدیل صحبت‌های پراکنده به ایمیل رسمی و کامیت.
🧪
نکته:
این برنامه برای ویندوز و مک در دسترس است. در اولین اجرا، به حدود ۳ تا ۴ گیگابایت فضای خالی برای دانلود مدل پردازش محلی نیاز دارید و پس از آن کاملاً مستقل کار می‌کند (برای لغو سریع فرآیند ضبط، کافیست دوبار کلید
Esc
را بزنید).
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6963" target="_blank">📅 16:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6962">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8BVVpykerTpF4UCXinV_RMJFnX-89tl5RcrVNSGMZpb_PWVUlITZsveay_YlDX8FzMX0aG6JZNXlTpwIEs64O57pyhCE8z6WKn3fzqK82TtBI16hJd0uV1Jv5GfwB0fGjMifZ3-zGVTYdPLS8Jhj24uKa_fW6lRzxo_3Mo1qj_I4VCx9uEPn48Znd2LRzujNQwYPyvZlJnRAYloqs_kSnyzsv1_pA0lKWr3Co3B5MYF1nG6ExMSFyRrrVfsiJanjCAtT-B6j7Hq3tKxMzuR4Rdq8fGtrg07ZWpc1T6vrAYVe3v7ZkoaKPLctlDc5VvIQ_q6rcX6pD6KCqid6F-IOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
TelegramOS
پلتفرمی یکپارچه که تلگرام را به یک سیستم‌عامل کامل برای کسب‌وکار شما تبدیل می‌کند؛ تمام ابزارهای مدیریت، پشتیبانی و توسعه در یک داشبورد جامع!
✨
ویژگی‌ها:
🔸
مدیریت متمرکز تیمی:
کنترل همزمان چند اکانت، صندوق پیام مشترک (Shared Inbox) و مدیریت سطح دسترسی اعضا.
🔸
اتوماسیون و CRM:
ساخت سناریوهای کاری (Workflows)، سیستم پاسخگویی خودکار و مدیریت پیشرفته ارتباط با مشتریان.
🔸
آنالیتیکس و مارکتینگ:
ارائه گزارش‌های دقیق از عملکرد، تحلیل کمپین‌ها و دسترسی به مارکت‌پلیس داخلی.
🧪
نکته:
این پلتفرم بهترین گزینه برای تیم‌های پشتیبانی، فروش و بازاریابی است که می‌خواهند تلگرام را به قطب اصلی و خودکار فعالیت‌های تجاری خود تبدیل کنند.
🔗
وب‌سایت رسمی TelegramOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6962" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6961">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=YMRUsCGhRQVS91EIQWP1CR3hBuo7vMTzFjsMmKlwTPZ25hNFfN7vbxdmwl6IbCdFFY_7ze9erZxxcqe-iIG6FAJTGrYIIK071aQRywOKBChSvzZU5r6R6uIIGCaYgWnM_pEOEVe3vX1LHNegS29VT71Hu2B_i8VycXJlX5NCkIPeIlDXkkvYkpAvimz7rPNs0bSg3BVjRnLX5FnPFHxLc9cqq8hScjyUg7ALst1GEshZ4m04JKwHmjD_AfhxVSNC_eddn-mOaFlRxfBS9748fXEb8CIEptdHPE1n9Nthy3hHLKr-M7ZCZ4Hldj1M4db-cpDhzrZyCetO14psqtaSDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=YMRUsCGhRQVS91EIQWP1CR3hBuo7vMTzFjsMmKlwTPZ25hNFfN7vbxdmwl6IbCdFFY_7ze9erZxxcqe-iIG6FAJTGrYIIK071aQRywOKBChSvzZU5r6R6uIIGCaYgWnM_pEOEVe3vX1LHNegS29VT71Hu2B_i8VycXJlX5NCkIPeIlDXkkvYkpAvimz7rPNs0bSg3BVjRnLX5FnPFHxLc9cqq8hScjyUg7ALst1GEshZ4m04JKwHmjD_AfhxVSNC_eddn-mOaFlRxfBS9748fXEb8CIEptdHPE1n9Nthy3hHLKr-M7ZCZ4Hldj1M4db-cpDhzrZyCetO14psqtaSDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با یک کلیک، طراحی هر وب‌سایتی را کپی کنید!
یک ابزار فوق‌العاده به نام Ditto می‌تواند در چند ثانیه، سیستم طراحی هر وب‌سایت را استخراج کند.
✨
امکانات Ditto:
🔍
فقط کافی است لینک سایت را وارد کنید؛ Ditto آن را تحلیل کرده و نسخه‌ای بسیار دقیق از سبک طراحی‌اش را آماده می‌کند.
🎨
تمام توکن‌های طراحی را به‌صورت خودکار استخراج می‌کند؛ از جمله رنگ‌ها، فونت‌ها، اندازه‌ها، فاصله‌ها، سایه‌ها، گریدها و سایر جزئیات بصری.
📄
یک فایل
DESIGN.md
تولید می‌کند که می‌توانید مستقیماً در Claude، ChatGPT، Cursor، v0 و سایر ابزارهای هوش مصنوعی استفاده کنید.
✨
بدون نیاز به کار دستی، ساختار و سبک طراحی سایت را بازسازی می‌کند.
🔄
حتی می‌توانید سبک چند سایت را با هم ترکیب کنید؛ مثلاً رنگ‌بندی و انیمیشن‌های یک سایت را با تایپوگرافی سایت دیگری ادغام کنید.
👀
نتیجه را بلافاصله پس از تولید مشاهده و در صورت نیاز ویرایش کنید.
📦
امکان خروجی گرفتن برای Figma، کامپوننت‌های React، تنظیمات Tailwind، Storybook، WordPress/Elementor و متغیرهای CSS را نیز دارد.
https://www.ditto.site/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6961" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">موتور جستجوی مبتنی بر شبکه DHT بیت‌تورنت، که امکان جستجو و یافتن منابع تورنت و لینک‌های مگنتی رو فراهم میکنه
☠
http://cilimo.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6960" target="_blank">📅 14:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV7OJ9RdT2192Et8zNIJ64TWNJgf28Sc12wXjkYWiFOylyV7zrlQH2QyBMJwd9GGPWF16vkk5BTTbX49lq33KoHuiKDM8vJ27J8FlJ27Yca81mqP2zgn48FI2GXNKVWz2lUdFtrAeje9GoLz-tlrvdocliDMpFxqZgnlBYTtPk0UVqVLw072HNRyKMp6jf41AJJhWKgoub4sGgDoyRQO5In4uxG8Du8LR3F3SQr9aYZnFnswVw_T2v_ueHuQ-bSOUrrcRZS_0DDZy3LmmWnCAhLStIdsaNIt6ZFb_EUJAGzYqVK81K_kPQlZWXylEgApyc5OKDLHbC2I3uOVt7WvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
Magnitude Browser Agent
دستیار هوش مصنوعی قدرتمندی که با استفاده از بینایی ماشین (Vision AI) به شما اجازه می‌دهد مرورگر وب را فقط با دستورات متنی ساده کنترل و اتوماتیک کنید!
✨
ویژگی‌ها:
*
👁
معماری بینایی‌محور: برخلاف ابزارهای قدیمی که به کدهای سایت (DOM) وابسته‌اند، این ابزار صفحه وب را مثل یک انسان می‌بیند و با مختصات پیکسلی کار می‌کند.
*
🖱
تعامل و اتوماسیون کامل: کلیک، تایپ، و جابه‌جایی المان‌ها (Drag & Drop) در پیچیده‌ترین سایت‌ها.
*
📊
استخراج هوشمند دیتا: توانایی خواندن و استخراج داده‌های ساختاریافته (بر اساس Zod Schema) مستقیماً از روی ظاهر سایت.
*
✅
تست‌رانر داخلی: ابزاری فوق‌العاده برای تست خودکار وب‌اپلیکیشن‌ها با بررسی و تأییدیه بصری (Visual Assertions).
🧪
نکته: این پروژه در بنچمارک WebVoyager امتیاز خیره‌کننده ۹۴٪ را کسب کرده است. برای بهترین عملکرد، به یک مدل بینایی قدرتمند مثل Claude 3.5 Sonnet یا Qwen-2.5VL 72B نیاز دارید. نصب اولیه به سادگی با دستور npx create-magnitude-app در ترمینال انجام می‌شود.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6959" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghphHwCuznaz-ChNEBgbnjn8AN8XofFQdIL4rOkeKmIHcyA1WbuKFNJ4SxoieDVu92OVm3XtMQI1V4hi2vQRSAcVIjqO6oI3kuYeaxlRc8fO9eRQuySu3BpHqDeBKLzC2AKVfgKF4B4EpgnQq2sNFXurivFCiQQY1JT4dbRGu2PEx_caq4duji61TrnTJpUbZ1jZ6-tJ9heM5w8foLYcjikPe2LBYtRGA3xi1TdiF_wqaTxqVItyOtwq6JR0KIgYTDwVe9vkxOnUBO9uOF1Wl4gBTT2seYXbTjU3yfzaMakkjl_tHq2olBsGGuoJWVloogEaH1ZhhkmKv9TowDxvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار چندمنظوره رایگان برای ویرایش صدا، عکس و ویدیو
سرویس
Magic Hour
مجموعه‌ای از ابزارها و فناوری‌های هوش مصنوعی کاربردی را برای انجام هر نوع وظیفه‌ای گرد هم آورده است:
🔹
تولید تصاویر، حذف پس‌زمینه و افزایش کیفیت تصاویر؛
🔹
ویرایشگر دیپ‌فیک با قابلیت
جایگزینی افراد در ویدیو
؛
🔹
بازسازی عکس‌های سیاه و سفید + جایگزینی افراد در تصویر؛
🔹
مجموعه‌ای از ابزارها برای کار با موسیقی و فایل‌های صوتی؛
🔹
تولیدکننده زیرنویس.
🌐
magichour.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6958" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی
🔥
vless://63dc39fe-3bc3-4267-8bf1-4069b47baa18@194.110.172.150:443?encryption=none&fp=chrome&pbk=3sRLbKljY5s7LCik-w9MqgenayhgHgLV0v9lmFGQ9TQ&security=reality&sid=3094219d2cfd2b3d&sni=www.samsung.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6957" target="_blank">📅 11:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
🤖
3xui-telegram-bot
ربات قدرتمند و متن‌باز تلگرام برای فروش خودکار سرویس VPN، با اتصال مستقیم به پنل 3X-UI. با این ابزار تمام فرآیندهای فروش، تمدید و مدیریت اکانت‌ها بدون نیاز به دخالت دستی ادمین انجام می‌شود!
✨
ویژگی‌ها:
🛍
فروش خودکار سرویس با حجم دلخواه، شارژ کیف پول (کارت‌به‌کارت) و پشتیبانی از چند سرور (Inbound)
🎁
مجهز به سیستم ساخت کد تخفیف، ارائه تست رایگان و زیرمجموعه‌گیری (Referral)
💻
دارای ابزار اختصاصی خط‌فرمان (vpn-bot) برای نصب سریع یک‌خطی، بکاپ‌گیری و آپدیت
🔐
اتصال کاملاً امن به پنل صرفاً از طریق API Token (بدون نیاز به یوزرنیم و پسورد پنل)
🧪
نکته:
مدیریت کامل ربات اعم از تغییر قیمت‌ها، تایید یا رد پرداخت‌ها، و مشاهده آمار، مستقیماً از طریق دستورات داخل تلگرام توسط ادمین انجام می‌شود. همچنین برای سرورهای ایران، امکان تنظیم پروکسی SOCKS5 نیز تعبیه شده است.
📥
دانلود و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6956" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
