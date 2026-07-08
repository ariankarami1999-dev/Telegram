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
<img src="https://cdn4.telesco.pe/file/ArrzSfd7415rdhQu8gkBw_ivSjd-rWi8dOLAgY03HCyvryPTn0ksuMtHEsg8Ui5EKl1nWXB0Se8HJt4y_E_97uCe59m2f64jZJ_9Jf00x1sYFseFvGP4vDw2MuBCgn07dUmWG-14YWpJaOAG-zjE9_1GEkQh-_m6DMJcmnVvUk5OeeYLbV8k9HXptp9aP3vF-NpPlEOuJseRquI8iBgtLq66Jf5G-dZYGYsnuxMJG0ahSStXRyOgEFpBGwANF-vyrSOHr76ez7PCn1Fv0YJihF9FPNmykNyrEwOcJXcNW6fJpV9mKiRjfFbGzKMy9BWoV1-6JUAXM08cPGktZrtSaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.82K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 205 · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 522 · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3M5kD1_C8IlsZ2sd56qW_EezOhDpoyeCxV1bMTnKA0Kc3hbvBc_6I0gexM6uEYQuCd7M2to9qKlFUcPez7tVvmF_Q4axChSF6IWvzjK1KzpFSKB0Tg3HzX3w5ttmOOuk1CS48PDx0m39Y2GeBlPmPDj3gTFMTbD7GhaIyOmAc-5yardAbpekno5jvKE1o2NZ2BIY7qb8Bz5yQi53E0PY4Pjf8MXQpDndSOJVvg5HYmbv2OlfarmpvIbVYQPdZPNmvITQqTuU5sh3gSVFJ8tf7zFkIzv_Yb9XDpCWDhn5IW8GlQajUL3IsB_JrsImxOSrVuWMUWJFGmotJREOsu1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 993 · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JapSbfCnpFeXTnz58PQ3EFxQ2f3RpZq52DoMp_osJ3tF3vl84jaZpJtWktRvl5nBT0owQTbE7UgpwOkBm1ccXlMRkMJJwdQAMNx9QZ7kZU8tGv95rIbyL0yvEZcsczK1HGvX_NjB7mUwAKTfn22R0d8uomQSQHm0Vxfn4hlA21hy2bAdKkniF3d1LqhZdaI5a21Lb4AFOwCH3Cmn1KqHgExaSfIRJUQq6XsUsgfpzRart9UWEPk3ZyqHKytNrNN87S3QzsaiyxT_xLZYCVMNZ7myhlqPFUP0T2MXW0E8g2alEJ7RWONVoi9GpR6shW_Dv50BL1rYJFm1OxHGW3HobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7jqo6V8yBNVqL30IDF2dA-1i5NkF7OzbXuqtsa7_qoZWxbTLsq-gnEkv3yBWwrcaMlryr5qHiAiSYYxwE-Xl5gMOqJC-Vb_najiZp90Yqhp8sw8hLO1SXGmHlWk71IDc1Dw-CSMG-Uzlj1paPDz4Z3RVxe0X1vpXWtZWmD9Cj83_Zn8ckOpM-dkpFnPg1ZUuZr6MdgNqVsgk0nydq34l6tSIH3HjlT6noHr1y-yM2VJpuTp4jRGYWRi6_NlarDYvUkZM6E0mikuswdJip-PGwUUkIh75YHbXrjyw-jOcVGSsMSm_zY_PEWO06BM-wfRFPMkVq-DAbR4sf2cRcnkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXyGHbLml5DzjjmT4sQFQmfX1W71Nd8bzrhGwPZd3dbAehSfNazUd3P5YWwqNDUf8b295E6IQC58iAq4dfXydPGd4TBOTGOCN3QpMNyXViqndePlvuBdbrZuElo7P5EZ_5DBdtwbmz5fOgmoCsny63Lhx9LkUyjTD9uRsgzB8feBKrfiCOQ6ZasT6UeC1YPmqUijhRVcZ9_GsK2VNZIuXL6btGSt-DV5rPTCO3ps0ahe7jnefKBFFm1kE049ypIYEbfaBLwqs511Glb7fMjgSM12YhR9fyAmo6EAlwoi_1_eIt_T1WLfybOVrszvThsh0gQtJk9kJDnFvQhHh_4tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy5nwCj6cALialeXngS0wO_VVbwdJgF1-xM0laUUaQto-A38emKG2qD8vehFHT_-nlZKHvnxOCJSWV-ZWCrMMhsFsM7UB2BK_Dij4qAOZJhtuFxODENNNMTJ1TwLB_QkTZEf4W1g_L5ZEtPoZN-z0lkS7-KXbZXRdYUT0lNRQaK9gDoUOvqJOe6a73XbJiGMNlkjNbnl47GVWNr7ZUx-kShx9lDuvb79KtV0K1MmmiFdKo5s_wlwPFY_EvsUP7c_uz9W2PO2sKi7_1hUxCbYeKMls99n_OjkQ2Ty9s9gQEUGCZlQSBTXW7MbxwhPZiIp36LATnQRz1s8lwueeWBKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shWxaqEPTXQmvcWpI2lmoVGs3gJHvi8LR4xqppWQxnH89L6lyFzv2SEztVBHvJUYBDXZi8RNoCQUzvKZnEq1qiq8IvIVAIAOYzjP3NbGtwWqtdE_CU8IMu7x884-BnAVc9JwGqY3LDb6xOlvgyEOS918uSQQRUvFPdxaSKHtUfah9Zu6DtvV2b5UaAqfiWHiNX8uhbt1W2h9lrzXTfTQ4Rz9oCEMiM50SDCzSVOc6CWHqvtr2rqPBaELa4p2LNXp4UYfCyU3c7Trrl9qNg6Mle43A811oIAaam4UoXqTDabrLq3vX7hdtClvPIsWmYmhpbtOGZp4d9ouNmmAhosLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMxYP-6al6rVREWfK6z2Rjeyjfp521UnT7avSRIfOH_rJu84BQ7pyaKddW9-qJ4MRFrsVZF232mIcCbwdlRzYvF9fuKGrCijZbD2M5gAPQaaEVflJ8xzw9j9uk1kjaX8K2rLFXGeCf4eb7BK6aak5LPNgsYXixb1sQExHaouwBMg1OR55N35jmeQ1Pi43a0qrCL1oFOpVojevWdrgE1SrS1-8MRoIGMRJk5zwV6vm4bQJAcWr2Zf-VBORDGGNsQJOxlOgGyJCb6E9FUzB-b12kL-0TOAmY7S6fkUhxVsG08PbirQqcfQO3SVyoRA370W_47jbXgai_ePKlDYlcCWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj3FN8Z3pdXRGzkb1sHNgZyX644US2PHR7_TNv3LzAxCzxOHRnRA--6C5k95L4Uy5AfCiC-UwLFeaIFIMm9s6zno38ce4jXfPCGosIQpqqAlwFzvc2hmXx6pAhKdYagLYqgkjpst7_BtN0rBSomR2i84jFPVesxBP9A9whiCRanIYVC7HXjnO4kltwuDx5CoR3nrTDaq51dNkqEz_t5rdRfrTKVLR7OzY5Vrx4AH7d_LYPGQDBrPrWPUdKjGgPUYeeP-8NnVjIy-wZP1iRYn6clq6O7pVrheStL17SjBeKJ-8v1XQZUv6_YdC1ovor0cV6qxAvXglNN5UP50zLdSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3D-YgkCVjxBJTKywWz5lvBZQDTJjVXok0yzyd0xJqL1w8mhyKFYOrnL9mkXPlKrUQhbKNwEcQQTVeGqQ9oB9UIE4W6FRqeHjCVJieQJwaJJiOPphwwwB-KPV-oQ8wIpwzHzPWSnE1_AIeQSomCiwJJVHtUmCALvC_6FcK24KBhsUOcZk-YqXTkVZmyUcehZmVei9z2Hn34gF5mPdhe1Aoba8H8kkuqaiOqaoR_4AC1f6V_aP2evJaDOUYeFLAAk9522-Ie13X4F3gcNVe0yv388WW1IPrr7XBpl1mh-vqUAcsUyy9iQdEkaIyjwCNciPLvlbILlKOgLM7AL6xIFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwE_iYCTarFGyG5QNLtNRKej0SIY9nzfH-ub_kPsHaplcFwdJroRppLGDclVSS-ONCKWGLw1Gno7yJqLC-2UjTskhMOT8ZZykSadJyawKfIF92750CUDKUgagp_ih-7hvIn7H8yzdSUnJ4psjg-ZfjFDvEQSlQJ-GZQnLX23VziP3ratPbeg-9LaN3jAe0VTibwM77PraJCBG65SgWvvxnmw9lBmL72smTV0dUlhZYQDW1ObT03arvt3Wv1C47FTyo8S6oH2O-Zvegj-FjaQQN4fj9N29vsWCjaKMTuWRNErI8MUK2MhH9sajMr0R3d7RIUT6al7UMuxDOs2CvWhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOrwBmeclLogC89erzushW1Dfo6NsrE-Y2O1djtezi87jLuc9V-M63LD0P_Uk2k6hr-nwl25OUjSJ9iJudhgqF57PJnkcqA6_GgWYK5A_B7UKd8hZqhF6AjTuttUxyp7HBS9JyxUD52sOZ6xE6ZgL1GV6XEnZpK4gA0pfd3tZn0uTrKZoPLoUEldCzW7V1ndnInkLvfQLk0TSPl7TyP_sNkOIUUS4UsdtdwLboENpAEm1y6vx17h1hHV2u3XLVb9uS0_0Rg16RXK_Wjka6F3Zt_maYVfUExucbrt4I0ncyZIHhw0GXJEcpHusUgLwkhHILG_xzY2JdVjdc8mFT2ZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR1Z0HmAmtaf6TAWSyOwuqi27LFYiS7o0xiGvKw3_MiMbTH_mVummrKYW7Q6FSOF3JzxpRLSNVNcZDsa6uN-xPSTxJPp0UUl8eGtOByV-OplUxfez4E4ib8BQ94zx2mp7gcR3VShNTvAmsuxauP3nTHoKYB9-irlBmswzWnjeV02txuGNR-KNOq8jPPF4ZeNR-avPRltFBQrS1I7w_6KXqcQt2FuzxeHglgFIRM4kE1zFiQINs7wDgndxD4PA5ImXFSFaFqAPv-wg_o3jSAmVxvJESP4vq5nlmwgRFswn_H1Q_Yx_GiwNc4Xnhf6T0UEaTLV6zm2GFoRxgKLiw2kMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC-7j-D5lCF0R48EFHK3FajChd6j-HDaEJ3KNbj3p4uN2a9oaUZ-eDjZ56EUq37krR-PF6CAHCtEIidUN9I2mrr9GD_789BOIjMOZCkdGEyOSqUkHOejIR51NSHA4Scgm5-XUwahg--bRXPpPx7q4Cd0Jg8S8EsGlN5MW1dFr6LLWHJUIV4zS_iHeXiTi07osDBPsyDP3fBvWrk07FEvJ8tZPFe1nMPuSnCgJ6sgKqcvxZ-e31ND_wI-qLGl7Yvd-6gE_okm9g6gDneNCCU0bGLGgp8nWOyRrKnhXUTHNz0rsFQ2wuHZXwqqmbnnJmAFa8r--LptCVd0I31iuc1spA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=PC-EvyuyLMhVmiIvj7BXaFJ15iFrnjgMMxxSBv16-4M2TCG1Z3SztZkbUvdDQcCooFE_Y2RLIUqql0XUpOw3ZSQAPRHfhrZHJzvAZXq7D74SkNzCaTX4YaypXKMARswt0Z9mrtOEAsLIMOo9UHIF97YCCJTTXsVx5uPIvF7Ll7TcZJKZzXWc34hRuYcN36ZB-tboXlRvhSXrZ16XWoG8YMGqa_qp9SnjcY-GoFjpugheWIUAqD0_DUHOPjK99087MiEpHQjYZQMhdqMhq3QPFfsd-LSBzp2tjaIvCo_HalUx4Xhh6uKbMXZvCk_HU-Oh1KBA92XF3nLBk06djF7H7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=PC-EvyuyLMhVmiIvj7BXaFJ15iFrnjgMMxxSBv16-4M2TCG1Z3SztZkbUvdDQcCooFE_Y2RLIUqql0XUpOw3ZSQAPRHfhrZHJzvAZXq7D74SkNzCaTX4YaypXKMARswt0Z9mrtOEAsLIMOo9UHIF97YCCJTTXsVx5uPIvF7Ll7TcZJKZzXWc34hRuYcN36ZB-tboXlRvhSXrZ16XWoG8YMGqa_qp9SnjcY-GoFjpugheWIUAqD0_DUHOPjK99087MiEpHQjYZQMhdqMhq3QPFfsd-LSBzp2tjaIvCo_HalUx4Xhh6uKbMXZvCk_HU-Oh1KBA92XF3nLBk06djF7H7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5Pc9Z7vWjZMUCcSRSbQaQ7D21b-ij4z7o4oBN5pSdxgnlQm9UnGxax_DWYIy0u8Ppolx0j--z--nRwKu8OAShIBWvguNCkFOu482-Sadde81lbJjhImGMX6GBBOHZsOsfRIhPkCvfwHgFO8Y10TO7FXIvjwVwushAwyF-eUXiFgcJzn2OZENEKyZSbWYwpSJZdz6UzF46gljw1Dl3L53t17X08Wr2k4zrfXvlLNNBpDC-tSFb-ggskvXIiB6C9gP3eCbNFG3sYI7JrUVbhZVZWtqckQpxpbgTdxCOiX-fRAqXzR9A3huzDOhzNht1A7BBQvYJyAdNfHuTItCTxNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV8XcSBjvlr-Ni5AYghdftUOqQ5JS3EbX--vcithnDVM18YA9UQR6ZMGvpbKxtVeIC-JoN0wFLioxWdLPZ-FNJUAPHDsyNHLNnEEzEorBGH04hjei_nq4r_Uqr4KdbpibfnvUzEIER-N5WbRFGUsTxL2jciC5SqplYzDT94TsNRzP-SLuoXGCsXvqx5TQNDdDU6d3j0RL9aesk6QGN_6Ry6CrvVmlxujRn9e_MHIzmTe6hA8ucF-8-zkJm43I_qjYBHo8fgp71pbHYZGEkzAdWAgjrLsEf3TUPhw27MOBJcbZ6uaYx08bw1H9gzTwhX0zRXmW9togCh2EgbCybWjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPAnZj2GR8USh7KW8F2JmICW7SxLMXDQJot_rybyu6YD4gxEwrV6fwX_iFBZu3Myp-rO5qprvSEtZQKTuL-xF3ua6-kjNTQOkqgLewe7ThqYBIrwqDcG_UKNDXyPrjkEf-djAFDXu4GZjkSAJrLV3i5axkUegomVLc73LEp6SdUJMKKK67TCp-SPSTOxOnaAWr_fREDuXroFOjbCIqqKTSpWd5bPcGZ-3OajATA2fATdfO1UEXqB2TGMighcBAHUJinO_Xy9hW57GLcEuEUrEEF02nw9a0amEDSfvbMwv6A_-Vfb7no98NfYRgT5QOFDMftjzq-bScacv1oPdtFu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHnHmUoSjzBveN0NWyOdzJBbTjaj9u3eJw-VomtxjYFnA-vmEQvQYem2NLEuokuD9wJpxiBfwweoOriZvPgCCDR3Xkig5SD7KGp75b_EobX-tk0KR78SgHXKFu3SUczxDGB1IoWc_ajxEudqJtCJn2bownZKgrX9i32MLi4ImbKX8yMEuNCfW1QZ3Gh-UkAE9O4YniM56esNuS1ZAEDqfUYr10nhzvVSf-rKoXDt8dv8cwKFO-KN6Yo158lEWFWZyfe3JyFEPxs9UFOqZyZ_v6iLAwcNmU6EbmNM4ZTUcNenIRXjeJ_0hOYyao0Jhx1-SdynMA5iE4zXyub3aeE1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quZNYfnx0Vrh0IzUxYmkpDNX0XpI6B98NZYeT06kqBTb8HcXIFUDHxQAaj-46wBpAP-6p6bP1S3fvkpoyir2jn6F0ytgvywIaUl2Y_Ew53uW6oEnjhWPglgwUilUZnPFhe-iEPwb0FyrwQ0c6WUwcfp-MnzUa4FhGL9nKcpelWaaHrTsfmfw0zSsK_lKTb6nUyaqnVROitb2397bGo_TyB_-S432I-w3MnAKrUjznaNT2YtOMxp2KzOMYM2cIIpfQQoI5PJuWtJ8i3vWLZqv1IC01DL6zgQxVAZAPF7f3u6PU6WMC8oAJM144PfX_C1nkiC2nOWhnlj3ajVolxwNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=NHf-k-lhm8nL24DG-U-y-abfqtaOj8fJyN1a5H1QKrmxd-vnefVgzM86zZKKQRJG3KdJeN9VWZrdnTsH37ifeE6sb5UxGyGnaNEBK9L6BGAV8mFBUL-oN_SGmeiV885xmRRkOfTXgWc9A479ETONm4MGt10TE9oOqqULGCsdzHhLOMjBmrnH0J203uVK8ARZHY7a0m3tFqPTHPD8jx7W9TDj44ypxFJx2jUqeBZRqzb6tflLytwf3amjW-NonOSSBtXnLi68NKeTJ9nfLcb2rxEv4F0psnLzB6qqRghOEEiE4iRmIAqebLw1DURIl-BobOCVpp2rzuW2qU0Nu3hB2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=NHf-k-lhm8nL24DG-U-y-abfqtaOj8fJyN1a5H1QKrmxd-vnefVgzM86zZKKQRJG3KdJeN9VWZrdnTsH37ifeE6sb5UxGyGnaNEBK9L6BGAV8mFBUL-oN_SGmeiV885xmRRkOfTXgWc9A479ETONm4MGt10TE9oOqqULGCsdzHhLOMjBmrnH0J203uVK8ARZHY7a0m3tFqPTHPD8jx7W9TDj44ypxFJx2jUqeBZRqzb6tflLytwf3amjW-NonOSSBtXnLi68NKeTJ9nfLcb2rxEv4F0psnLzB6qqRghOEEiE4iRmIAqebLw1DURIl-BobOCVpp2rzuW2qU0Nu3hB2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOb3RhKza6OlMJV_4RQI2ymw3805eMzLHHFCYiFmjmYxEu38H2mrFhlOm44ztS5V4T0Wm4Te1RBwFQQhDE46tBvkcrfuqE5af39b6Zsdn8uMz18mIqQMg-rTevGdTnG0qvoG9esoj0HzzHPyYW8MxNxtiGGigkXt2M3U1HpBCIwav-RgFGWO7p2aC23ZzY6VbKxZ3A7udIGiqXWnjVbKaXw8p3jCc91lN_1k-6KJnbij9q2CCAuec4485Lspx2Nz3jetA2Yqw6RxRMpkdRxyYqGPkDVPzBnFwZ4JJltDls5cbag7GTJxxr4oUtlWvTO3GnLlLRWBS7_2-GiTC5UJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa9kF6pOuM1fvz8zRuMmJi8-eMqe-paNtpnuTK6vai_b09Xr9M4TdeOBbwK_fgIczOo_WZZqNnmYwFi6SWe7CRqiWyjdyj8V6xLWy-uikVAPvTbhPCRGvjbHarsCNcklM8zxTbGANT7-gNGnsMGb8d3VQd_QBXkZ5n_bunQ9m6DZxLy4PtyHCZxabg3EOH2xpNeaTHeaBuiZAdeqR7HzvfLvZuVj9hwr5WNCYOf-eKtUTUMgr9EdWSA1q3_nT-gL8uYDUXSFyEqYF9A58gm0C6kycfhOinC9heaniS26uVwnsSR5WsAXRHJApP2eGi3Qz2KhrXtFN2DZyNMKg_OJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI2CcJSoj9STwYGfXXMkfTNZ89lA4Pd6CTcdUjkn9kp-OGYQgFhyUYG_inSi0oVL2ltR4u_FdHF4gFRvg1_c5NhvjOtAUCxKfVCDjQkVe03h4_4a87vp9gp5jYAlfunJexOfD3OgTO_PiTEXHyIWKw9Q1zoArSZdMxqqLOmUFoAcfHk8U7wVn_EBR1-dJi8P8x5rUSx8MWSaN1IuFtWcA55EpnM0dzrXHgMJrK8gnlkEegl4LoF5BBG7tuo883J1jYSbkRlYohaFbwjK3pwsxBLpq8HS49sTQvRRWXb2Wlj6kiuHglFDMTMAts-ppre_AKBuCb3Ojhtgv27NH1KggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCCCu0hYoQwRVU7YcK0X7YX9Ph1xeqtoS9RuJywdrU3bGX0QM2WrP9R7M9LXEwB6cPys5BKP3QZdwhKphLPlf1J75KsuZ0DvpqTjcDLFnxA3xTDji517gjJCiCnuWQ9P53GT2ow7WgQNhPYU0y_7A_QhGnx-XNZBRmO2BXKGH9X7H_CuORTd4XSbt4eBtLv-AjmltELOh5hJHmT4H1UM9MQIZld0ezQR4LZ7p4ZduI28Fvsnhca8qVRbmX7pY8lYZ8_KZyehxM7MsGxXj11Ob4ZTanQqdr4Kjfh53Sya_gh6xnrz1iQjdIsSqo-YIcN8ydeKgsPCzpwW56F6AWpyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPVyG38MgNfV69OsTufixhIusZ3J1vGwSwmgfK2YWdaBkBQHxlYhN9UbVM__TJtHXEc_XAcHvJ4cYxnCdY7b-__u5fiZee1upEEjFwPozwPRvC1omJZTkjmEY-vuRtT1m1GqNpXHE0slukfSuj9J2Jc-QdDc9_UIpndUma7UiCycP66Qr6rhxa73ePXv2ahZHaP_lIOde3NYSI94YXVKqC3qku9lZu6DHxk5OkU3iue9nVop6QCTINDv3i7u_iqxYq-bzuwFyEQfp88AcIXvbfUH96e4JLrsyzqImpcpFTyw_Y2ZMBpr68zxAp0rzLNxcW8xSG0o5L139XFWxewYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAgyD53oNoG-OBcrvuu3Xq8DslMx4gIocYoJhMgLkO6721ICboOjfPRk5Bia6ktK6NPPtPoAwpbP1taoGRzL05MipPmN8A2fyXw3i4ZLSHacEGG5xuZj0WU-herLEMsjXGrW-Vym-GEFR06Vt0v9p3Ie7aBYF6p3sgNYQaGiGiOvYbmQQVpzjib75dneIkP8adsN4hhjGG3kGIMcqyStTx4SML49ipPGdn2fCOgto6FD8RESddfHAUsnaTMEV9X-jP8AUdEgC2YRoI6ERw8Wqvv_h2syZeUfdldOQMQEZ56VfP9mXLjE2U2vE48uGINiF_-Xavw6AAPOoN6oEg6qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
آموزش نصب OpenCode و استفاده رایگان از مدل های هوش مصنوعی زیر :
🔸
Mimo 2.5
🔸
Deepseek 4 flash
🔸
Nemotron 3 Ultra
🔸
Big Pickle
🔸
North Mini Code
🔘
آموزش نصب در موبایل
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب OpenCode
npm i -g opencode-ai
4) اجرای OpenCode
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس‌ :
opencode
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر OpenCode را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
opencode
🔘
داکیومنت رسمی برای نصب در جاهای دیگر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎬
تدوینگر اختصاصی شما داخل ترمینال! معرفی ابزار فوق‌العاده Video-Use
🚀
دوست دارید فقط با چت کردن با عامل‌های هوش مصنوعی (مثل Claude Code یا Codex) ویدیوهاتون رو ادیت کنید؟ پروژه اوپن‌سورس
video-use
دقیقاً همین کار رو می‌کنه. فقط کافیه ویدیوهای خام رو بریزید داخل یک پوشه و با زبان طبیعی بهش بگید چی می‌خواید تا یک فایل نهایی (
final.mp4
) ترتمیز بهتون تحویل بده
.
🔥
چرا این ابزار انقلابی و متفاوته؟
🧠
پردازش هوشمند و ارزان:
به جای اینکه کل ویدیو رو به خورد LLM بده (که به شدت گرون و پرخطاست)، فقط یک فایل متنی سبک از ترانسکریپت با تایم‌استمپ دقیق کلمات و در صورت نیاز اسکرین‌شات‌هایی از تایم‌لاین (شامل فرم تصویر و موج صدا) رو بررسی می‌کنه.
✂️
حذف اتوماتیک اضافات:
تپق‌ها، مکث‌های طولانی و کلمات اضافه رو به صورت خودکار تشخیص میده و هوشمندانه کات می‌زنه.
🎵
تدوین بی‌نقص:
روی تمام کات‌ها ۳۰ میلی‌ثانیه فید (Fade) صوتی میندازه تا هیچ‌وقت صدای پرش کات رو نشنوید.
🎨
زیرنویس و انیمیشن:
می‌تونه زیرنویس‌های کاستوم (مثلاً کلمات دوتایی بزرگ) روی ویدیو بندازه و با ابزارهایی مثل Manim ،Remotion و HyperFrames انیمیشن تولید کنه.
🤖
حلقه خودارزیابی (Self-Eval):
قبل از اینکه خروجی رو به شما نشون بده، خودش ویدیو رو بازبینی می‌کنه تا پرش‌های تصویری یا مشکلات صوتی رو پیدا و برطرف کنه.
این ابزار مثل این می‌مونه که یک کارگردان و یک تدوینگر رو همزمان داخل محیط کدنویسی خودتون داشته باشید که حتی پروژه‌ها رو ذخیره می‌کنه تا روزهای بعد بتونید ادیت رو ادامه بدید!
🔗
لینک گیت‌هاب پروژه برای نصب و راه‌اندازی
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.30.8-universal.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید
#TheFeed
(v.0.30.8)
🔹
بهبود مدیریت لینک ها در برنامه، اگر توی یک پست ای دی یک کانال دیگه و یا لینک یک پست از یک کانال دیگه باشه، وقتی روش بزنید میتونید به اون کانال و پست منتقل بشید، توی قسمت فید باید اون کانال حتما توی اون کانفیگ وجود داشته باشه، توی قسمت میرور خودکار اون کانال به لیستتون اضافه میشه.
📯
من نسخه اندروید
universal
که مناسب همه‌ی گوشی های اندروید هست رو توی این کانال میزارم. ولی اگر نسخه‌های دیگه رو میخواید باید از گیتهاب و یا کانال زیر دانلود کنید (
ویندوز
،
مک
،
لینوکس
،
بی‌اس‌دی
، اندروید‌های
قدیم
و
جدید
،
ترموکس
، و حتی
نسخه ipa
آیفون) و لینک دانلود نسخه آیفون از تست‌فلایت توی کانال پین شده، البته هنوز آپدیت نشده.
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل‌های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ‌های دفید:
@thefeedconfig
🔗
گیتهاب پروژه:
https://github.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
معرفی CdnScanner؛ جامع‌ترین و قدرتمندترین اسکنر IP و CDN
🚀
✨
ویژگی‌های برجسته:
* پشتیبانی کامل از ۱۷ سرویس‌دهنده (CDN): شامل Cloudflare (و WARP/Workers)، AWS CloudFront، Google Cloud، Azure، ArvanCloud، Fastly، Vercel، Akamai، Gcore و...
💪
تست فوق‌دقیق بر اساس کانفیگ شما: در این ابزار IPها فقط زمانی تأیید می‌شوند که با کانفیگ V2Ray واقعی شما (شامل SNI، Host و Path) پاسخگو باشند (پشتیبانی از TCP connect + TLS Handshake + HTTP HEAD).
🫆 اسکنر اختصاصی HTTP: امکان وارد کردن مستقیم IP، دامنه یا رنج CIDR (مانند
1.1.1.0/24
) با قابلیت بازگشایی و اسکن خودکار کل رنج.
* تولید خودکار خروجی V2Ray: ساخت بی‌درنگ لینک‌های VLESS ،VMess و Trojan از IPهای سالم با قابلیت کپی و دانلود یک‌کلیکه!
* پینگ واقعی (ICMP): عملکرد دقیق روی Windows ،Linux و macOS (همراه با سیستم جایگزین TCP در صورت مسدود بودن پینگ).
* اسکن کامل و بدون نقص: بررسی جزء‌به‌جزء تمامی IPهای یک رنج مشخص، به جای اکتفا به نمونه‌های تصادفی.
* رابط کاربری مدرن و فارسی (RTL): داشبورد حرفه‌ای و چشم‌نواز همراه با نوار پیشرفت (Progress bar)، کارت‌های آماری، پیام‌های Toast و طراحی کاملاً راست‌چین.
📥
دریافت و نصب:
همین الان می‌توانید این ابزار قدرتمند و متن‌باز را از گیت‌هاب دریافت کنید. (اگر ابزار برایتان کاربردی بود، دادن ستاره
⭐️
به پروژه در گیت‌هاب فراموش نشود!)
🔗
لینک پروژه در گیت‌هاب:
https://github.com/ScannerVpn/CdnScanner
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXcsxZCZc0yrvBkLXrowPTC-wb18JL8r5oOdjgq7lVsqTRptzepsciehUo-cG_sIU5-1XW6lLBLWp2vR4YnELgcu_asH7XQX-Hsk6ibEfW5v8ev6xkzytbmuUuhzmzHs1xVUViFpLiPvSxidivYroVK99tG2UGy-XOArBmdewLE6yhy9L3FfY92b27tc_iD85k54xHk07rum5TAHVGUnV3tDl1WcKJEKVl0UA6xP-rxbEW_Q4j3Dcp2BL3KwPL8DHwlebWgswgixN05tEJH7eHmbAI_3JyI73ryvBCBhj14wUuCH4BTbMRfXgoLpPD5lWqAaXVGAom3RtDSXMcK4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=qCOFg57MT2W9RmPx3CgIMSlBcYWAebj5enwsjfd-5JFc5vdY54HwWhFNFEpG2NNXJ5SlZetwmhhTAZ11JyqTS2oDnB-aabpAAYTuArOgXDHCNC62grLdu6xv2qLpJYjmUBzGlk3-rQy5rduifHgg6Nwl5-t0XGxIZDwNTTQt1vxz43n6WdL8S735ASzn30C2g6ibcUv8Xy3I559A4fgDY_gvHjqt2nSnC6vcTeWw4GA4neoyLaL2qEuaQfMi4t9QWLLlT8wQCT_GKltccRzEP46U4xVVuLElDFY27n4CNb_9EXGQjJyODa2o8PK1SUO-GWnRUcjX9jA9hFFn3B0cew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=qCOFg57MT2W9RmPx3CgIMSlBcYWAebj5enwsjfd-5JFc5vdY54HwWhFNFEpG2NNXJ5SlZetwmhhTAZ11JyqTS2oDnB-aabpAAYTuArOgXDHCNC62grLdu6xv2qLpJYjmUBzGlk3-rQy5rduifHgg6Nwl5-t0XGxIZDwNTTQt1vxz43n6WdL8S735ASzn30C2g6ibcUv8Xy3I559A4fgDY_gvHjqt2nSnC6vcTeWw4GA4neoyLaL2qEuaQfMi4t9QWLLlT8wQCT_GKltccRzEP46U4xVVuLElDFY27n4CNb_9EXGQjJyODa2o8PK1SUO-GWnRUcjX9jA9hFFn3B0cew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHCu8UvRL1ixYa-TrJzWcjpM_ydhxYsEc7mci89kBxJqd55gpsGao01oPqlo-5Frdpim0JaMHV_auIIa3shgV76l_RnIl43jRrT9rzWAYAO08JiiQETuIgzT69AuWP5Mcdqjl5i7Y9238bviFoScCkgVdqqxwh8V-dWamQamwXfb10WgQICXZ2nmpts4a3-ZEh0lri6h4ECeFNDC8D8OW83aVth0lx_GQkS5QVimbduEzqqUsBKM1kwunv0tQk6UUifP_WA4kXefLdhdeedkd383BjNSEwdu3FY5wDkHkUBbIUi3YdfQWMKfbeOwVJVXLRhZz3N2yKvB1YXxM1QCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=TtXUEqlKmOneNvHAayyYtJ9sKtMdG9SzK76Q9x5Xl0UALnTaVr0Nlb9yR1AQojvD6ktIDh0CQmz-R6dnQWGayHcB5h4KFOaij15Fv0aXVvyda3DE5Gpc12dfJ4wdV1gR5iaz70f4VqV-jFUFS8RoSERAyJVhVM4GzCFMCEe-xbgVO80UG1gT594GOTb5jqhb-s84nB5CwiO84hOVplL6QcTr7ZVYQRvMZ3xgMPveknPY6pVe_VVdNC7ZitzP3Yw1YhsLG1nL7dte4p2wG-7_xE2xzFvK2Lm76XrVx_kEsPCLq4TuDdCMuCO6gAEI7J_p-zCqgjc8nUIHeYCFNWpJ83C7l3uFurJInV4WhrC8evf_wERCFbzhCVHi4thk4N2imUW-fMVrdUWDf0H_kAdkRiqmGId8sqpYy87vKdH6urAMkXVEB5iI3lD0GOzS7UmXio5a64E_u-6vp1DOk9wHY_JPjgZneXu1R6oPp9Nlt1-Dul87HTkpq4-GSUQKHschTA0vqtcPUGLQJrrXV4TpPaPfoUCDsZbTjoVNeGFKcSCSc4oZfqZBz_QGdqpTcx2zVGMixqVWX1sRuobfNAqG0GU8mWUiwgwRLwms0HKx1nIfjFt1sfzpO6Fc3kj2DUmvzAjECJ_Drqm5FlXzVCVHEX_8INlXBzLSJ88ckZ9cSFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=TtXUEqlKmOneNvHAayyYtJ9sKtMdG9SzK76Q9x5Xl0UALnTaVr0Nlb9yR1AQojvD6ktIDh0CQmz-R6dnQWGayHcB5h4KFOaij15Fv0aXVvyda3DE5Gpc12dfJ4wdV1gR5iaz70f4VqV-jFUFS8RoSERAyJVhVM4GzCFMCEe-xbgVO80UG1gT594GOTb5jqhb-s84nB5CwiO84hOVplL6QcTr7ZVYQRvMZ3xgMPveknPY6pVe_VVdNC7ZitzP3Yw1YhsLG1nL7dte4p2wG-7_xE2xzFvK2Lm76XrVx_kEsPCLq4TuDdCMuCO6gAEI7J_p-zCqgjc8nUIHeYCFNWpJ83C7l3uFurJInV4WhrC8evf_wERCFbzhCVHi4thk4N2imUW-fMVrdUWDf0H_kAdkRiqmGId8sqpYy87vKdH6urAMkXVEB5iI3lD0GOzS7UmXio5a64E_u-6vp1DOk9wHY_JPjgZneXu1R6oPp9Nlt1-Dul87HTkpq4-GSUQKHschTA0vqtcPUGLQJrrXV4TpPaPfoUCDsZbTjoVNeGFKcSCSc4oZfqZBz_QGdqpTcx2zVGMixqVWX1sRuobfNAqG0GU8mWUiwgwRLwms0HKx1nIfjFt1sfzpO6Fc3kj2DUmvzAjECJ_Drqm5FlXzVCVHEX_8INlXBzLSJ88ckZ9cSFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=ToChpyTMWn9TN-VvpVIbbUZ4Y5_MSCUVOjRGDxw7fXiyJwktZBCL76pwSmLcoiQbzDYNtbzS2wSyA-X6MwUq7yMcUlL4WVzEvJpf1yZwazfwPcr8sv9PL-WAr2vMEaIbx472YwsR3B1Ez1CA7DmBkRHlBaqAOxyjm0LlrPErKpgDxWnGZx8XI4iPbiaULVok4n7dz5KTDXXf53r7YcXwM0fsYDAuZ7gsutMmA__T5qVTXIgyC4Emdy9Y3-XZgsqbTcD3o5KJLTr3bWYgpVU0lRsNMFTl_mNtwTN_XljWQRg4quolgf0xnaRL4vc5Di3KzBak5e-ukEeyH35yPrHCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=ToChpyTMWn9TN-VvpVIbbUZ4Y5_MSCUVOjRGDxw7fXiyJwktZBCL76pwSmLcoiQbzDYNtbzS2wSyA-X6MwUq7yMcUlL4WVzEvJpf1yZwazfwPcr8sv9PL-WAr2vMEaIbx472YwsR3B1Ez1CA7DmBkRHlBaqAOxyjm0LlrPErKpgDxWnGZx8XI4iPbiaULVok4n7dz5KTDXXf53r7YcXwM0fsYDAuZ7gsutMmA__T5qVTXIgyC4Emdy9Y3-XZgsqbTcD3o5KJLTr3bWYgpVU0lRsNMFTl_mNtwTN_XljWQRg4quolgf0xnaRL4vc5Di3KzBak5e-ukEeyH35yPrHCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=EwpalAoWMvJHfTwQd-2fYrknp665BhjRQ4mr1t6GyJLRhhh_5glDiEU3FeE3V6S84mBWAapmz1-CjcmKOaXxq4yiuvLMq7n4frn0e1bWxm3qRcCm4ZFeUtBGNLEQ1U3dAjInFu2RmRJVzF_yOqCzYaILlu0XKUX9dyxBHC_-B22QjARFe7oBim9tVxFnANWKamXYp7KzdGAOb9tvfoaK0Wsi642O1ePxHvnqlZbqBuPWFXLwZFF-pL8zbIOvw6BjEBRMMzZ4lRRegL_i0FmB7hUIKBnxZlj0XMBZOqGC9BJZeXlLmOrPHN96nPV4DQsrSj7Oc6RHtbsx7U0hJ2Ft1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=EwpalAoWMvJHfTwQd-2fYrknp665BhjRQ4mr1t6GyJLRhhh_5glDiEU3FeE3V6S84mBWAapmz1-CjcmKOaXxq4yiuvLMq7n4frn0e1bWxm3qRcCm4ZFeUtBGNLEQ1U3dAjInFu2RmRJVzF_yOqCzYaILlu0XKUX9dyxBHC_-B22QjARFe7oBim9tVxFnANWKamXYp7KzdGAOb9tvfoaK0Wsi642O1ePxHvnqlZbqBuPWFXLwZFF-pL8zbIOvw6BjEBRMMzZ4lRRegL_i0FmB7hUIKBnxZlj0XMBZOqGC9BJZeXlLmOrPHN96nPV4DQsrSj7Oc6RHtbsx7U0hJ2Ft1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA73OhbTuYR_Fce_zl5h80_5vQ9LJw_wtlHj-xNJYZq01jznEo3vYoPmuUaotfjv3XGAthaaOSwWgK7tIWL-yRqQ1idz-EtmTXShbzHWXAXw-6KKoPHSiusUPSLtPmj0JwcP-bCbAYhZg40YricGMAVmQQMCE2ZCvTqA8KLyxcDH9_XE0V-TewN00wLzJ9oo1ddTCxtenNaIW3umoWvQWV3OnHJ_UBHKlUuAJTFlOIkJwDmZD0kBaoemc2vXNUzSes0NE9_-BsvxOxLGlZZV0n8vwLIf8QYQFHCsLNUtvfmcQBUfpiOOsUp_15043UTHx8XMdM2CvNUkUqT_0HE82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=FurCxiGIRrMac2vNkvFAzrp_7eiNW14Q6PuY_M1goFQIfkBgQBdCjUHZygL66H-c0MaN8KdDCwv-cwpU6dIQYIqqW-jh41oAfrsrAexQQIkOVrWyC3oYA-qQ0zz7Hn89wxibIHyGuqKS1I3BOzLBudUA9voJ4-g2UMTIa08boMBGRz-NwiV1KZPwf-kHd0cGXcIZLAti7k5OSScWIf-PpE9caLy563zdZsbQM-5nvy1MbFV0nR1C8SK3xcqoKQNhiTlaN9V0RroCn88zuxJrrSTFxKbfOpJx8kwxPP9ObBoJMGZ7AgcTNMH5L8_JIGsJGrEQvkHPMlK7ntHwVv0hBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=FurCxiGIRrMac2vNkvFAzrp_7eiNW14Q6PuY_M1goFQIfkBgQBdCjUHZygL66H-c0MaN8KdDCwv-cwpU6dIQYIqqW-jh41oAfrsrAexQQIkOVrWyC3oYA-qQ0zz7Hn89wxibIHyGuqKS1I3BOzLBudUA9voJ4-g2UMTIa08boMBGRz-NwiV1KZPwf-kHd0cGXcIZLAti7k5OSScWIf-PpE9caLy563zdZsbQM-5nvy1MbFV0nR1C8SK3xcqoKQNhiTlaN9V0RroCn88zuxJrrSTFxKbfOpJx8kwxPP9ObBoJMGZ7AgcTNMH5L8_JIGsJGrEQvkHPMlK7ntHwVv0hBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOvRkO6_Tngzj7V-pE2qjgjKp4HpERRkeHleSGNvzRhezLmRctUqDcxLg89UqvrcoEd_aaJkdp_L0-wwv0HHhP3qMBrK9eOtLMD0PE5FknywzPPYdbcCBNfplppjvuwNglQOqeKtvH_rJ6HZ_0JwvqWjHMrjcceK7EZYo9Oi3ej_MGIxFPb3S4Swk_9nqHAgB33cz-3GpEtXfgHfynGRYM4UG6rb4Hf6B8vYwb31gwJolrxcweFfKCoIF77Khity3Rgc0iHWZXPy9xSb96ZGXwzCH8CmF21l-OpDWl5hd1qepYqqc8nkI1_krNvITiopywWbZP4bMq6MZb1i5j6i9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQTfHuZ5TBX9VjXD_BwsBpy8KOayFkXze_JI6NFlhfy7xzcrtdIYG5f1K1CwJc1Y-7uilYHVuYjYi-9BdkwyusETdWCC5zq2bYtT1ZbecTbSeBxOtCJPE8YUvLww5gH8TGCAuuoNqMUnHGVeXz0XlHDhY_zaxvzzDLFweOdXcoYDId7xJ3Zn62ci0HH6dcd_QzXcXSL-igiEX_LPvfzZJN8KPmbxAuPzwcec3-EP5LtYyQpvpErSArFCl8ZayIYonO-e9KRE66R54KZo9LA9CtDVIHj7MASJuC3nVNtfCiEZWwAY6Kt_uZ5jSUg0I-u-SmOzHkwnEXlnshuyvrZ8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک میلیون توکن رایگان Gemini از طرف
گوگل؛ بدون نیاز به کارت بانکی!
🎁
✨
گوگل به تازگی یک فرصت بی‌نظیر فراهم کرده است: دریافت یک میلیون توکن کاملاً رایگان برای استفاده از جدیدترین و قدرتمندترین مدل‌های هوش مصنوعی این شرکت. برای دریافت این توکن‌ها به هیچ‌گونه کارت اعتباری یا خرید اشتراک نیازی ندارید و همه‌چیز با یک کلیک انجام می‌شود!
🔥
چگونه کلید API خود را دریافت کنیم؟
1️⃣
ابتدا وارد پلتفرم Google AI Studio شوید.
2️⃣
روی دکمه Create API key کلیک کنید.
3️⃣
تنظیمات و محدودیت‌های تولید را به دلخواه مشخص کنید؛ کلید شما آماده استفاده است!
🤖
مدل‌هایی که می‌توانید با این کلید استفاده کنید:
Gemini 2.5 Pro (قدرتمندترین و هوشمندترین نسخه)
Gemini 2.5 Flash (سریع، بهینه و همه‌کاره)
Gemini 2.5 Flash-Lite (فوق‌سبک و اقتصادی)
💡
کاربرد: این حجم عظیم از توکن‌ها برای ماه‌ها کار فشرده، از جمله کدنویسی، پردازش و تولید متن، تحلیل داده‌ها و حل مسائل پیچیده کاملاً کافی است.
🔗
لینک دریافت کلید API
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzclcNUUWHIImQQYbX9hh2Mr4_jB0-4o2mNAvpDGQnD331cWgLnrZyYhDO2WLz8MjNJhOxA8LfoBkmeWMtMU7nfP_8Kum4cUorfEUnXVz4LW1ZOXtCdJwpRriicue1tsijiIffxLP9cKfFhsJTE-L16YsWRGBoFQgTZxtbd50VKm42QS9smdBoyoo59HRTIfXV290A9v9NBCz0JUMVvf_CjK_H2kGxgc61X1UxdZuA3MLQNthxFBZKTXdRk34q-ZEVzsj2WhAzRVDK2GNNxqeNAmmM3kfonLXTMvfmSrFl4Q_YHw-ppccQySqSZQYJJeGkjUc8J0Enk3NLeMmYdDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفسیر خطاهای ویندوز با ابزار داخلی
راهنما:
— کد مورد نظر را کپی کنید، مثلاً 0x80070422.
— ترمینال را باز کنید (با فشردن Win+R و وارد کردن CMD).
— دستور
certutil -error 0x80070422
را وارد کنید.
— توضیحات دقیقی از مشکل را دریافت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqdlgbnj3WGT8KsoWWMGn1kp2upKiHUP5qrnqnBjKFyQ1KdtdYIbfl1AettbNNov5mQGfl5gWAC-P6KHMsTU98Amua8TsPAsx1LxBmSBhETFiFyOQdjm3Og07HpRM_GXkl2UjTwa6R7t0SKhZr0HvzpdxPLJ9PLKf2Jql-uTZKE72s7TMsemuFRN3ReJMMT2mOlf18utWmgnovfgLC3DU9uKai3Wot9gTNDE3zDG7vxK6pNpaPwhRqO3aHH1GLt_c0aqXxkFCEry7L5n2azDc16perydJWLbS85xk9mc-QUVaDkq2GqvJFl-oyHL2i2p3q633vAVlXfJ15ZXsWdWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wq0vuYVVJiTWlZxcPTvhpGlJwWKVzfcRE-0vc4VA_-PQspbjRepOUU95EhsXeSSRtz0w47nfBJoWQytKCjhClTgpk4aZ4ouOZW13h_lRjxG-g8MyahDxTW49cM1PxIQmkxWB2lng3ed4sgdqPH5-K67fGMcpt3GYiQATCyPcZvwVAWgWwbo8vgwVyteeN_RYNxMQ4zH6Y1tc24sVBjl_Ygop6Iq0tuxWmH0_f3Y_cL8u8Bop8pIheXtKgSCt7SxfbzpHDIbLA7d4fCqQ2p2j63w48jzOUiLGg5SbG05XV2sT1vNH6SwpHQ5-N7At5IXP17I_sUr-V80brrHBzaxP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4DTEVd-p8VEd0ejViYF2_RUX2ETSr-74JFwIr_U2Kyy5r0p9CgegsOxqhGD8VYmuPLOd8CpOCZU7_THcROeO4VwZMP9HC4mH3QnDOgJSr9yxbdDWr0YwOZAVR_WVykbqQciQQwadNRjuREoxrOOmdHDfObj1UDKUoIPG4Ah5e_msM6KrK17uq5aNuQAJj6TkepVjVmPHtAl8xXIJ2iLGnSYNj-6kRi34cKUvWkYjsxAQhsyWTtTfUqZGJ1IKR8MGuQWpRwFhmY0r-pKVuE8lJWZf0JMPlw6qG8lpM5bh-Vw9z-fIqqOf7knN0GPUAoH5HCOqvd3DueeOaRJor5d1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRuyFxNMCmY57-jgcPBs4JCxU9wqVgbZwYloTBebkM8bcQQnLm7OsYofyCNdqbH0HWvVGgnhv2KURJTRJzRv6cVj7GRbh6XABwfYfFcg4Ek2rOCj7nkmqkOanDCEt_SgrccR1SlZPX51V4lYkePucLq0ZapfTgHFVWQLKgAniW0lKIfbEAmCWpZmxiFWaAHXzfZ6bgZiGw7Lt0pLvHeLFsJr5W3AEiIsgIO0r4Wn8uJQc9ArOhizL6KcsLZrhV-eKvlHLiXQ68u_Tvi-GyeOXbFn5kih5AoVCMxXMcNKQ9DmItphNcoOfDjyBb0DPv4E-rQJ9VzHBaxH7ZLXCUXVMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4B6JxF2Qien8_Prtkv-Ydzt3Lu3aQMLgh-_rOBvvOSPJxH6uI8k5lNhKGic6efHb9F-ar-yvKFaVf-VYMsbBZJLWY9k3cVCwUTYLQHzrVKGm4EBVfdbmMxmZeAes8I9VY80_5iE4Ap6KR82jSwBr9lt5Jk2qLeKCKMP6HmnTloB_nKmdhk_5KJgCqzKyx12D25UBsLbo6MDHh_L8PdhPa6UFKQ9EVKfj_sjGwIVYDo6KYSiPnvf_3PbOSPBBYTGLjEU6ncgALWQS1kQ3PLmGCfMW8QPHWa7dWcjFHJS5YQE0uFEEtVSPox2cmQyg9kB7qRkL7Qeo243Syz6Y0ikhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_uZYmVL6iXg9nsf4QjL11DwLYqfJcUpUNxbiYVaVIwsiPDzXMGgLwPqd5maolx_L7EVEALmpQ3ONlxeuPDHIvl5xsEmAmd6ytxHOOQHIPNWsHP0Tj2wsFrwZ_kpFGAeKbsxjhmHLI951zTHLKWcXZ0IwA0qORwIQBJyy__Qmbhu5BGafsO6XVGDP2O0eUVxRfdIdsBUNIZA_O_IjHODFywgdtjhAhtQZvHljDiVlXYsxxxlyjwCa0585eJbAbNCtS21q1kBpzKE_Jqo_cCtZbcidyutEXlBgMAzrIq4N8Ik55ZcE0iKi20_b33s1BRNhtRwNJsieFhzsHP1sWjsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIovNSVuFtkNLM2RgtC_IS2ondbvTomOnTYwEFooSk1itgesdKI-h5ofWKB-y_SGBY14y_wXs25XCT7-7j-AdKGSut-wwAqh9B3fE38NPAICNaiXZrhuXucD_YyAsXeX_dXWJ-jeXonC11uRuyc7C_qJ2BzbQ45lauvQlt55zl1HFNh5T_AoYwTS1tuzlR0-E_gQVGxronClGWVXDmHTQ3E5vfIsadsq6pTnYK01m-ArqTiW-v2xraZIe09s8bWzwf8uXmaZT2JTHHsjk-gbEegzNJzVaG4phyiDgRtz8WMwrwnY3Xfevwnp3rN7Y5B6gkB8V_eVhFZnPtyYf1wESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHyIux81Dim11LIfHvWdnvDbSiMsHsePyCQgaGEWLK8qs4cbWZGf1EvsHBhMa791PehfK6v8H5Zb9LPZFJONwCy5jnEJnp9pMCtP_l0t8QIv2t7M5Lb-u9x08sE0eLcUBQVH_rTCkkD3zG5W52Ty14uYp0ZG3fPs8owF4gZtOYIjZ13eIWIDjQYy08P0qBC6Np4geYW0AhUxm8SfxKbnxohBG06JsoMYh8OwN5C4AoYoh1FZuVJpDV4YtShBGheTIa4S6ViC3JHMZFFtYYD-WFoAKtW8050tOOjix7Qs-FYUTPxQIPe0-TRmjjwAfpklY3f6lHjCwi0OAIs2SSntGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOf3AYdspM9DmVCBbbN_kCFtWA1f2Fp7CkpVg4a8hIVe9K5MiSqCDB02Zkg_m_akwfOoJHbUIfDbmMfWEhVlJT7O5wTeoEecKNmIL104_H5c-n-mD8fOBA2c7FMR35lnNAnJJBFni45Nkvv3qwQWk8j1yx69aUmd0K0uGTauAfbAh-HwXccIEunWOA-0oW8qckkJZTMMtxi97CwlTXPKKKhhzLClNeQsAF4Jm9OAbBCXwHfFuzAx0UpTNO4ITi4-kwi7dZcjQAjsLN0SUTJdWcjbuBZdW6gkBUoxp-DdLCQGBrYKCfn0m1rXtOZmjOpNoOmCcxEIxkVLaD07UhGqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJOMqt48CuUCRLb01juc3WGOAqxSyfmodmTtNqARJAnrGhbyxwmSp8hyFAhLpCxamgWKG4mltki3mmgl-_5bTGv14OrS8q1qqDCWTjXXyEvLnOd8Hm8glHNuIuBxM8Hg5DUrOMJzY1fwQBfIWDYiwE_bXz2m1ArllytR1OkxjCYMD7oyBlosLHU3sKGrtNUAQ5AVKtA9Czl5z1Kw4fBongli03HE23Aco8xOrjq544NZLlfj2UnWmY3kPvFlG0bpFM1L46xPWUEW-t1cMKm63nchEdOT85C9QNnlGvpPjW9grRYSFi-E7imm0ybLXRfDfcLpYsTSqjHGH7ub14w1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkmeMvB0-hZzH-yL9rOZB5VDqpuPFqownQTcI_pXsDu6JO2aO--lRcR_DCrSzBt48ZGKFPD3Xx3gqdM_lV8ERfXpJt-mQmYWqgfdXvwIclLwKqR5KnqYlSsM9zHk0-QY7WQcpt-G3a-a5i2Bl25RHhqA2BgTPjcFWcl69OnwlCWnwjQXgadGgmsOoXmz-6LY35xiwkv91jJg-2gx0LPLAy-e7vjzgVZ_fTkskglKEla5fIHrK6YzkkJews5VSFn28dWNXA5Xs_eZNkfpmdQTd2amDi4mkGCvlRKTKb2xQPc_KuSKjOIpzeJYAH_l1NVtPq1MajxxgJ0sZUhTW2T6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=C0JtS_FEgCjdf3wfiFewUF9cRag_38z_hzbyp_frfv5AmCxKchQ018j1zqBzuFDycUzRA6Eq4UQWKj5Rd_EnuNwHk98JBrtBNKe5EH4KP0upYYRsdvADCTHbkfbKy5d5SXk4ii1JyKjEtSJl101JR0NwaMhiCoFMYVrFRPia02TXJSGHNAKN32W9CK68uU8mBiUTJ3O94E0Jkxh6HCrSNcI9x7Oy_fh_OmjDgmVoaDpV3V6r5Zjp3tS5zZa37np_e2n6z04fdG98jJNnxKDqncTk6YHNQDVFv3G3l2Uu_qJQ6wVm_dRYX1qPecgoOqYMBmx-HGuM8B23Ibq9DjmHyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=C0JtS_FEgCjdf3wfiFewUF9cRag_38z_hzbyp_frfv5AmCxKchQ018j1zqBzuFDycUzRA6Eq4UQWKj5Rd_EnuNwHk98JBrtBNKe5EH4KP0upYYRsdvADCTHbkfbKy5d5SXk4ii1JyKjEtSJl101JR0NwaMhiCoFMYVrFRPia02TXJSGHNAKN32W9CK68uU8mBiUTJ3O94E0Jkxh6HCrSNcI9x7Oy_fh_OmjDgmVoaDpV3V6r5Zjp3tS5zZa37np_e2n6z04fdG98jJNnxKDqncTk6YHNQDVFv3G3l2Uu_qJQ6wVm_dRYX1qPecgoOqYMBmx-HGuM8B23Ibq9DjmHyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaZ299WxlfbRvruWfJFYy6wDLJnDUyqiJWqTog24VGCir7ltvBhFbAfoNFfUVhqDsV9aUpA3iOIX4eFe9twT1z06O9Kk6QF7RGhIx-Uqjp1i8rl2-rI6M7gitgrIYS9BDVX887sI7yaOYkcixTSB6syq77UWtnCI3GoidH5ghj8ZE24sbrd2BXHHEw6LphJTLhur5vXxKmxsR3Z3AygrjvpzSDvX19EdM0fzC-DY0xVo5PsSh7HW-rYfS_dFC-RxcZmDkQ5nJ-ZdYKno_-wALXpkT-8xNagZgAOwi8b5TXKuF_ipZd34hB8iV6CVRCcrHuHfqggv53c3J5lBLboA1OCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaZ299WxlfbRvruWfJFYy6wDLJnDUyqiJWqTog24VGCir7ltvBhFbAfoNFfUVhqDsV9aUpA3iOIX4eFe9twT1z06O9Kk6QF7RGhIx-Uqjp1i8rl2-rI6M7gitgrIYS9BDVX887sI7yaOYkcixTSB6syq77UWtnCI3GoidH5ghj8ZE24sbrd2BXHHEw6LphJTLhur5vXxKmxsR3Z3AygrjvpzSDvX19EdM0fzC-DY0xVo5PsSh7HW-rYfS_dFC-RxcZmDkQ5nJ-ZdYKno_-wALXpkT-8xNagZgAOwi8b5TXKuF_ipZd34hB8iV6CVRCcrHuHfqggv53c3J5lBLboA1OCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTU0BIIZbEzW_yh4UUsTZGerUrOb5dQmS_PNC_WVPBqJ-mR7QOiX02jWafiaC_QvSegaNSvxZd_t4-YRQUMgCzps_XiJYkTvmiyPAdAVf3OPw82tttsxgRb6bb5k-w_tPgfpIYJaJplAQHkeMSugXAXHAUX4ODE3u3PdBWQ0hn2tSrF4dOUSTft3V-Nlm6WLyFRAWi7qCIBzdRpOuboBpnwgLGQAAcH4i6Pukvd6qpfqZ7UerMvTXUTasan3g2K04SlUqehDKbSxdtvdYbLVO5gIDEGl09b8jPJEa_AqZf255U3JKILboy8M0onFs_uWmyqRqVEyt4sQybIVdea7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHYMGr278WS2-WO8KgX78u2e-9Rh2E5ognjKWxEXIDStzAb6tJtVvckYwzT5UHp2BAHrDKYvph1Up3ARPdYIokDIm7FETjk1Sl1oDeHBJw5FtmCGYSDgRjztWi-2J3OgefYrpkjbm80EKOz9z1clM_APbh10MQzZPu09aqRB085CxX6nU8m7uN4mb9LQi3hjKv8cGBvbwdDukim3pWzgmWly5ND3M6Goybo6-vkFsHZ4rnhx4CtZSx260NrX8bV0L1bn-8hFGxBaVS5YYQiBE-HONZBJZTbrXopRfVDhM1xqJO-5yEEzHJJrAil0GdLVPO-WXVIjCxhSBKwFtcLQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqh6E5DTcFpNECecA6HfDT7wS78iCPOYGLZnqIW_ma-EEviGe6YGdWSGugtcy8dHKx_51U5epqwx-kTIB1j6ZB8VjHZJwSJ6VUCqZM6TGFN-WlEA1UsA67aAbtVjfh6HokH3CigrjQ2SVzQH_NgPbIoayFcyM08hsawVpR5LqqlkOfYGq3eYv9q9uhq9AeBbeIcxGcxsXM7DxAIpiUlTxS-1Dqw8aSBrOD-h56v8hietLFi9BvtfdfBvujqEypO5Wz3jlOlGKwOkxE6jEtxQwLMovGD0zWZ0N-BoDXjUvPb1kZ2iw7hBHxRBi4bejmcMgqBNwt4QBzijIwsfv-XGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=CRnQemNWwHtCsqDHzfuEEch8dxYbhL0Q9AaDkTLFroelhMsYpmvzphHcAhRg6mw-BQpDp5GG6gsJT7-J1iv7hIdanNbN9mweSH6q2OyNL4m2LCugWqhJ1G4m9yLvJ57jAV5e9FuDFd14QYSqsArsxQMZEE4IFCcah_Vy_rygEowzghQOq40F8k8aXhy7_lKbRXcLOV3BILWzD3FuAivgTqNO3_J0F0d3H24sygTL3ir-fWfSHCRMRRJmYBJQ94nVUKep3yxX1prY9zU06S_J2nmfrI0BtaViKZD6kpY9DL0lvdEWQalxJLVgOLSJRwWoAheYvRbsDlJ834DoVO6t8RDGp21v3ZCCxw8KPlAyqqSNXjwo4PRBBSELjVI4UnKwLjYUpH-TlAW1IW1PrQBlNcw6pCB65NEctoCAHEM2rEQHdyEntlWBzlABHkpaWpkK6b4pWjRX80x_gwmlTfoXA0UvbAjQxfVuDrVL4OqS3CJjsodS-Lg0GFM1-9iB4l5IFDJfTB9bMIDh9Ppiu79defUP5kkri7nA21zq861u6vElGd8XGDrwNaP40XD1Gsam5APqTYBy8h2fLRckbs1ze5L805v6K4X2y0WKw0AHkWfQDkWLI5uez8YZQF1Xgxhl8lJk3M-3csH3M6WtPvmgcGPOkK6lQS2vHL0Kl4Svpsc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=CRnQemNWwHtCsqDHzfuEEch8dxYbhL0Q9AaDkTLFroelhMsYpmvzphHcAhRg6mw-BQpDp5GG6gsJT7-J1iv7hIdanNbN9mweSH6q2OyNL4m2LCugWqhJ1G4m9yLvJ57jAV5e9FuDFd14QYSqsArsxQMZEE4IFCcah_Vy_rygEowzghQOq40F8k8aXhy7_lKbRXcLOV3BILWzD3FuAivgTqNO3_J0F0d3H24sygTL3ir-fWfSHCRMRRJmYBJQ94nVUKep3yxX1prY9zU06S_J2nmfrI0BtaViKZD6kpY9DL0lvdEWQalxJLVgOLSJRwWoAheYvRbsDlJ834DoVO6t8RDGp21v3ZCCxw8KPlAyqqSNXjwo4PRBBSELjVI4UnKwLjYUpH-TlAW1IW1PrQBlNcw6pCB65NEctoCAHEM2rEQHdyEntlWBzlABHkpaWpkK6b4pWjRX80x_gwmlTfoXA0UvbAjQxfVuDrVL4OqS3CJjsodS-Lg0GFM1-9iB4l5IFDJfTB9bMIDh9Ppiu79defUP5kkri7nA21zq861u6vElGd8XGDrwNaP40XD1Gsam5APqTYBy8h2fLRckbs1ze5L805v6K4X2y0WKw0AHkWfQDkWLI5uez8YZQF1Xgxhl8lJk3M-3csH3M6WtPvmgcGPOkK6lQS2vHL0Kl4Svpsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_7GKJaMOAJmr8wakase8P4S5bpvivIc5xz5wF37wh5BHOUJpXI4Q1qpIcCMXvNz1QXQltGXXs5rcf6LXqID1x8GvV93zooEAyTFQtswAXcTuvFa3KZUXJKS5PLDsHhjVOOpDYfKabCH22cn4Lr__-wlVBm9mT2-iL326lRFa6WTxveilenRytMA9dHgpiWaSryb2_d5xRoO7RlqSnmjhbGBbgDiBc--aOMUh3-G0hGwEwCYt7z20xTrExambzoioc7OOgajD-_vD3HeajmT7OWeIlDAwTqoJWK-re8ae57i28paZ5i4F5RynRZbRu7LsAUjrxThAZNY-SefOuFsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6R-wFVCFe7JRDDXJdYJpqm9BUcSPheqchryKdyO6Qs9gxZ-f_vJegqijtkpntLIGHYY6Ojia0da2W5-g_9AtKU198CbtJ3LBLKQmglcv9G3GF6Y45lgNAnTeiyDQKG-jGXS6nZozMV7UWyKnQUeNx1wnDuOhGTTaAA5m5szejFKNBxBuQKBFJJ12Or2rcsa6SkJM10m5N_6YqXLfBj-cl56Ql0HIb3sYFSqOnn45j_88ub4CHbxUeTagEey7dyl7ASKvld6JVhHcd3lpBCz4gxjnUk-9_1h1G7ax90K29CD095qeBNVccZjozW5Zu0CBjFpPXW8rTv6veEc9SXI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=nd0JaaSNE3z9ZLO0BTm3SqrQoL7hwo-OEqVAojkP8rqvxdadXtJRtVDr5i1lIp1Ueunh6gSMuJf2Wos__evhHqY74-GqzB_wxEyAcddR5WAIcbtiLAjNEtcNRIWNqi95ukdq9bti3XUGnVaKqYKiI0Tov5ZyDq1XQvCPHYZfb29cTuOd-EBi2AYnbUgjxn2MpVXta39v6LEtvJGQjIGrqrWNowNFk3K33UUeOr7QitHbFZJjvJxzWmzdKtduInxSG-DjJXea_LN84AnXoUm9UutUkd90Pd_9l4w3dbSuABRZ0YqSEeUJU7zw1A7dLa5aKfr5Kj2qYJ0d06hFAxI-zF6hwg_f2ERpQoetF5F_ExL-4ivnRZ8XnCNeUSVDwoY31bCxRWDHybOXFBmMIzU7w0f8c2yA7wHwQ9nu-R4bZo3j_2fub-7GOHwFCGj8-CSH8PdDItwFxjKWNWZWIS-_4gmzvztVVuuXs3sDa6s6C54ycI6bkef8i6TrNksEsC7HgTjsipf59xDF9Zwoo14O_cDYMf_wEAty2PV6ttCxdQdCqlyaPUjCNPvrQGJ1DxjZ13rQf3zNCYc7-MaV5Knmvqu_vuCPpf0Istom-IHsUYHDLq6qOvaUVr7znV-xOt5fx9lgxLIOHYTivz84BW7IsSxqw2HUU_i-vgJ2eCvt9ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=nd0JaaSNE3z9ZLO0BTm3SqrQoL7hwo-OEqVAojkP8rqvxdadXtJRtVDr5i1lIp1Ueunh6gSMuJf2Wos__evhHqY74-GqzB_wxEyAcddR5WAIcbtiLAjNEtcNRIWNqi95ukdq9bti3XUGnVaKqYKiI0Tov5ZyDq1XQvCPHYZfb29cTuOd-EBi2AYnbUgjxn2MpVXta39v6LEtvJGQjIGrqrWNowNFk3K33UUeOr7QitHbFZJjvJxzWmzdKtduInxSG-DjJXea_LN84AnXoUm9UutUkd90Pd_9l4w3dbSuABRZ0YqSEeUJU7zw1A7dLa5aKfr5Kj2qYJ0d06hFAxI-zF6hwg_f2ERpQoetF5F_ExL-4ivnRZ8XnCNeUSVDwoY31bCxRWDHybOXFBmMIzU7w0f8c2yA7wHwQ9nu-R4bZo3j_2fub-7GOHwFCGj8-CSH8PdDItwFxjKWNWZWIS-_4gmzvztVVuuXs3sDa6s6C54ycI6bkef8i6TrNksEsC7HgTjsipf59xDF9Zwoo14O_cDYMf_wEAty2PV6ttCxdQdCqlyaPUjCNPvrQGJ1DxjZ13rQf3zNCYc7-MaV5Knmvqu_vuCPpf0Istom-IHsUYHDLq6qOvaUVr7znV-xOt5fx9lgxLIOHYTivz84BW7IsSxqw2HUU_i-vgJ2eCvt9ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhRsQXfw8rttUBn8pLAqCcbIeoysGUd3Bd6lGdSoXRuETTDMBcgvD8sEWOnZYQy1moGHPZ-ujMIjXzPYw31v_nzH7zsVTY45KD17VUdAQjqjOH_vqmxIusZocBnmj1ph1_g_rACDACgyxsMA-DaYu4ZMOxoPUpnrUn-t9Ib9nQ_k75Ouv3kv5mNdxFZpe_WCTyCLWzyc4FgdhO_Z9c6ugLEX-TkVJx24hPW3Dhp-DCCj-zfJX9lANRODT1mmZsj03nhTex4lOxcebQLbFyNzQ63eKV2M7J-OKj4zKm_cALUCe8yClp7P3nmoVamOiAYUDOuu5gvlYlfGdjHXhfMEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=iT4XKvNPNi-WPVvrhiB4IMSn-hPmS8pTLS9LbWwg8d8gj0YHh4fUF5BQGewIF56r7xwIXRXeI68X2e4kh5jKN5XQw85Gq_T9ygt4JABAmjBlwKRvn_XH4s6JAq8QQW47p7lBMSJuosSdQ33Dk7k4CvNcAjP83PGHdzvb42wFTTSbLMFGGDO84mQiz5bgLQMUsq_5OGjg15CE3jUd8wbVqcEiInuM7ia6UyE30mJhPTjwQjZ4QnYBdKkkBSMzy7pYQnKbfFH7f-ZQ7ApljoYKeuADvklCYDHsJP9RdzgfzgDwD0zOzbkxnUTlg_qaa5Ad0nRuQZ3xs67X50r9Dg9oWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=iT4XKvNPNi-WPVvrhiB4IMSn-hPmS8pTLS9LbWwg8d8gj0YHh4fUF5BQGewIF56r7xwIXRXeI68X2e4kh5jKN5XQw85Gq_T9ygt4JABAmjBlwKRvn_XH4s6JAq8QQW47p7lBMSJuosSdQ33Dk7k4CvNcAjP83PGHdzvb42wFTTSbLMFGGDO84mQiz5bgLQMUsq_5OGjg15CE3jUd8wbVqcEiInuM7ia6UyE30mJhPTjwQjZ4QnYBdKkkBSMzy7pYQnKbfFH7f-ZQ7ApljoYKeuADvklCYDHsJP9RdzgfzgDwD0zOzbkxnUTlg_qaa5Ad0nRuQZ3xs67X50r9Dg9oWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
