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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستید؟
اگر می‌خواهید قدرت واقعی مدل‌ها را مقایسه کنید، این دو سایت را حتماً ببینید:
🌐
Artificial Analysis
🔗
https://artificialanalysis.ai
یکی از کامل‌ترین Leaderboardهای هوش مصنوعی؛ مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر. تقریباً همه مدل‌هارو را پوشش می‌دهد.
💻
DeepSWE
🔗
https://deepswe.datacurve.ai
به‌نظر من بهترین بنچمارک برای بررسی قدرت برنامه‌نویسی مدل هاست. به‌جای آزمون از مسائل قدیمی، از پروژه‌های جدید و واقعی استفاده می‌کند تا مدل‌ها نتوانند با حفظ کردن جواب‌ها امتیاز بگیرند(تقلب بکنند)؛
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 261 · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 707 · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 770 · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 791 · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 861 · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 889 · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 848 · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXyGHbLml5DzjjmT4sQFQmfX1W71Nd8bzrhGwPZd3dbAehSfNazUd3P5YWwqNDUf8b295E6IQC58iAq4dfXydPGd4TBOTGOCN3QpMNyXViqndePlvuBdbrZuElo7P5EZ_5DBdtwbmz5fOgmoCsny63Lhx9LkUyjTD9uRsgzB8feBKrfiCOQ6ZasT6UeC1YPmqUijhRVcZ9_GsK2VNZIuXL6btGSt-DV5rPTCO3ps0ahe7jnefKBFFm1kE049ypIYEbfaBLwqs511Glb7fMjgSM12YhR9fyAmo6EAlwoi_1_eIt_T1WLfybOVrszvThsh0gQtJk9kJDnFvQhHh_4tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy5nwCj6cALialeXngS0wO_VVbwdJgF1-xM0laUUaQto-A38emKG2qD8vehFHT_-nlZKHvnxOCJSWV-ZWCrMMhsFsM7UB2BK_Dij4qAOZJhtuFxODENNNMTJ1TwLB_QkTZEf4W1g_L5ZEtPoZN-z0lkS7-KXbZXRdYUT0lNRQaK9gDoUOvqJOe6a73XbJiGMNlkjNbnl47GVWNr7ZUx-kShx9lDuvb79KtV0K1MmmiFdKo5s_wlwPFY_EvsUP7c_uz9W2PO2sKi7_1hUxCbYeKMls99n_OjkQ2Ty9s9gQEUGCZlQSBTXW7MbxwhPZiIp36LATnQRz1s8lwueeWBKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 987 · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyTZXafQnpP8oH8aiE75ZNrEItxJFHgIFnuLTkvYdfVxdtG3flVei-LMgtMPTXrpdxER9hns6eUYZ1WUFsJmd0ruMnBf5maoGbPrRgXcoK3X-C22tjWp03DoaFA_6K6GaCRf0BXx_q1PQuo4pZCTDKqDhQ-aS0VBmImG6kkQH8pDpKH_aF42gpfgoyG3uDzebyR7Lp4buDmPuNx9p6iGUaz-g_Va8uXeSJZSVY3aUgsCm3T6-FgrLQsMSCNcV63Se1NtQiZcgvf6tqAWy3hHUdlG6lgFfI3KduFF7w-WuRGwtt7wYkA8HqwPwPZh3X1thCk5lIubrisXuSq8vIlzvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss3gNhUr-r4DJhfVq9jYefdLGTarSanMlteC_ZYu9OhzLVFJaOtX959n0gRApvy2b-FJU9k2XYBpPbrNHtpKF5jOqpwmys5o9_jXC0lXyu_vHVLfXRtVLC8ZzO5RMD3d2fL46N9TIxOHAWAqQH6HP2a_2lYhKtWOTs9Y-b_FvLc2HG2CJNn05MY4-AQP6nW1OvuYPxfwcWQ6yDpQHKa-kZWY8DJH1-dxCzxP6NPqfNyFxsmQQs5zO_EnEXunf-VKQQKH0g2LWv9ulepEAgzWm0z1JUCHBA88K6uoEavCuvbig_obdUaFGd--ghr12SkMTeh2_gAcfIO0Hrwzk7UGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHajyar6B0DGMUn4vpQJz1bOShG5LgtOAEe_GqUD4LI1U6AX5p-Y08at3u8xMl3u-I9jt6hmGErChGcqiIvwvUYgt7HVkQbfBuvz1GVw807dHY5Zdcva7QE5WzKcmgvEvRtjVzBThGyN1L1E7scOej5SxB6oYSFxLBjEvNbYCcWJ6Lc67OIhGZepmwrcxhG3jL4nhPwwd7QFsLctDtF5Qc4DMt5SNId7bLg1SnQk6x7utu2CdKiTJHHJuubVdbUbvlmNmSxJ1Ieckp5h4Xz1wMAn7RJQ9FwBtDxOdGxicy8pxm0PvYu48i-TLfaGoeiMrIqj29W6AT3MhLYVTN_1ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtyqdQbW6VXhM94UxTL6s6At5TQdHcl5qAGSfU18SK70fbIcey0DZcrbfA0rCH0UBBQ4-QWh-6byVr2Hxsh1QUloQ0yBSZeEwfnC1YX9M_6MuCq7VJYA7h5mrjJ7dBOpg2JaYiHRM0OnoZCHW4BUjpkaWvwSjsSxNrvrl0Ik4DYqeTgj0vpnjOD9uFkHDb9sNAROdQv6io6s-QyPRRNAZpmL8mDUd02ZVGqbXGFkP-Xz0d5yL55StHY8KoV1lkWD0dz_qz765cRgr2uo2w0QXAx2MIdQ3bHO3JRsKwR57fyqffLD6wPN6UQgjbak4c21NdtHub9iFWet4kHXYNJjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLf8j7aiRPI4Swvsp2jd3tSATF0KfgzW5O0XFMO_0o8ZCbdrtvImZFbDbLdjj9U7hTtjbJPEVij0qgXVpHzz3Dfk6l4Q7KeBOk0CjEL-oMiQq2J6kx5q_r4iDhnvcdb_D4ixZqaw3NBlJsbAECVwzzD-uB52JLFNAtFrGewi55nsV6lZCk1CigVNcQW3c42W5sznVHnExOGMuF2oVwCwe2HGBjj_Dz2YKn0G0bc4JYFNKaLHUny9epSjfmHt5XLmZDDfoUFnNpmMWqopkkYSHo_lE1xdyC-raNAWhpAggmckDzhXN17_y_FzMPSw9sgolXkDYug4XX3XunRTyNCOvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=Wb-ZixwQZjR0MRG5meDBBRVkGeFah9476WZFF4XbplHs1N3LuYr6ZyIY4SNFr2H6cK9DaKkKKuVbw9IkefPZbN5wMxU0TBj7cyB3mg_yKguHgRvuy_d98gUEd98M2Uqdh_0NrJg2ORrekU2rpzMsJDlUdl9fkMgyF8RbjWoxrkc_aP0I-n3vHDf3H30ZQenZEU9JQk5cMwETB0TOZlC4JnJ6yXy7GDZQUatNwuEHj3SZlDIseVz-IBDqzJaAllh-OSmQNWZ96z6YCqlm_CratG8iQpdpAUdBHZZEueHTGzQs5rNM43c6WKzD3Bab-kd_AOITiUEVY-4G1m3oZmqvHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=Wb-ZixwQZjR0MRG5meDBBRVkGeFah9476WZFF4XbplHs1N3LuYr6ZyIY4SNFr2H6cK9DaKkKKuVbw9IkefPZbN5wMxU0TBj7cyB3mg_yKguHgRvuy_d98gUEd98M2Uqdh_0NrJg2ORrekU2rpzMsJDlUdl9fkMgyF8RbjWoxrkc_aP0I-n3vHDf3H30ZQenZEU9JQk5cMwETB0TOZlC4JnJ6yXy7GDZQUatNwuEHj3SZlDIseVz-IBDqzJaAllh-OSmQNWZ96z6YCqlm_CratG8iQpdpAUdBHZZEueHTGzQs5rNM43c6WKzD3Bab-kd_AOITiUEVY-4G1m3oZmqvHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re00Tu8ogZca7GCg53pAFChP4vHY4XGsAZ8n50gzSLdVKLQdt29VzFBn1CLa_a01jKRm42AQ5zCmlhB4pGkYg5GR0gXiN--u9sdPasKSIufedERK3MmQaXXgFwmVTWSSg2vrj2kYnP28vzOAL2qMNGo6rLUp4kt00nTyuOc7kkF9EeHSe02sCkM-eCj5SUKfruVaROVsD1Fy96wCkMYX0SNid9ae8cQAP1WCR9jpVL8G95-xJh44Rc7_EkgJYFz-8sIoADvihAZkiyxf_aiLSc23TO6yllpM_Vf9w3If9LbnaYdU1vJQK4inKKrcMr4y5tPQHTxZMHUQIZDC3y8XBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8MjS5d_XiUa1tiTWZyzZQkrvVDsD0WWekhOX7fSne2mEfFIbH58G-TnYQGeByELBRuZSss_SUMEi2St-B5XOwpJRCz3kLGYoiClZ6HmyC4-ntH9bDyQAKglJY8AFnRjhlBazYrT-IUYzginc1-YG_Jqo6pWmlsyLhMdSHUv_j450oNhWQ8GS9x_7DfG5DDDpEqnxyaju61xdUGp1lpQVN38zZ1CzBqRF3pgqIADEvGQ2yvTwkEJDhUwJFbGt2PIlF_BksDm8xvJwPbC4lbB7icaERmnv5LK8kUJVfd6jaCxSHPBpfuREDfst3LnROqftcKGydVLVs59HBj7BCP6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN943_AsIZ8ODKnLI3698U1iHtbJlGJHp-C_sgQMb9fUyLAozT6ozMmMSgSNTjQ9_OGW-nfgkRlbe_Mu7ony21hJltbC9422QUOmvuiDDsFG-tUTDKOtahq8hdlz4Oyq9BRLTQYiEGZqcZm6TuoJHpIsm3hwDPx1Vq8Xz-z__Zfe8Fp4AwScT6N3sXVjvN17tro-EMMJyrmAYB1R7fmMdwUF_qd--XGATiB6h3IAQ6dIOi8E79aAbs5jaDvHUkAsiXQDTHoZ78s4-fRQqDrNhi8rWB9BHyOHsJZYGxglduZbTtLOwwOZBSOI4h7M2Y_y3Sp135EgElEbWY0gg__YFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGrgnghMB5y65B-pqX4VcEcIaOCew8RY2AKQeP_8fpvhJf9Nl_TvsqEl-q-r3_f2NRUaw2b2xwO6EldAzTQXcPIECae43xP0B8ItXvDc3CLc90LcoVU_QTd7MuCepxEYakSKi4OvLO9jA40VLnlVlYnIpYG6A5gWgFeXT4Cf8afcbFfqmERwev9qXaqjLwJ-sh88aF_Svxp0u8gB0jK-dCAcyxu1XNJOHlKJIw-nSyYBJ4dKFGhxdWhjztnAA6m_4UJqdx_sakEwlq6Hk4a9f6IpJrGJBShIG8D5Xhc09Ba3uaTPBChSitRux9obsS7qY0b2U4kqPIE6zRNh_OsDiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUg1Ho_LiTmqYgoAfhN2r0A0eMHbgCrhtgeRNSnUVBLGSRDINepKU2UdLEeJEGX8foY8cpvIsEs1KiuX_fnW65pa_TCHhE4ddotIA9yGc_gGMr6PeRkQjvSUmfjjYUMUsi-m4BsKarrmh6pnibLJvjdKb1C-rPFfO_dWdk9kBP2SgnwBtq1GQMEsxCIR0NOa94tSjtZKZ9xhuyVmFMC7Cxiy-GjIf53xowMgBGzCEblU_vjMWXCrphmTuu7ZWATv2LVkAO_nJv5uBgLf19GnKSRSAgvpTVY_MxyHC-n2bW-Qrx3VLmJHhcw4w1HokDxuK2ISrpcWu0X1bBUIw9di4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=PV07jiS98lf4drn7BZ6euKubIpq3YdmQBC3OtqKlzPYa2G82so6AE5Vs86tnXfI8mu7jDTZkzxYgsvxFubFZnPabO_yiCjj8ifNr-VB9r7d_c2kUEVkvyOW1_bauBYqiX7GMwFoYHdaiQn5VPXiJDMfl48rvplUrFwLJsR4EpQDTqJ-tvZc08AobYTe_8QrEvftJu3rr07ewLeuqXST-Z9_zpA7N76JneaE1vT5lFfxFfdlr1z0N14wZGo0cYsTx-0tKrc6ku4LDiAXK60-JCIZjX_L6CcoVqonhgL8PZmDSiUXX-2a-BiL0TSpZ9ea058_wbVbDJjxHnV4bJtPUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=PV07jiS98lf4drn7BZ6euKubIpq3YdmQBC3OtqKlzPYa2G82so6AE5Vs86tnXfI8mu7jDTZkzxYgsvxFubFZnPabO_yiCjj8ifNr-VB9r7d_c2kUEVkvyOW1_bauBYqiX7GMwFoYHdaiQn5VPXiJDMfl48rvplUrFwLJsR4EpQDTqJ-tvZc08AobYTe_8QrEvftJu3rr07ewLeuqXST-Z9_zpA7N76JneaE1vT5lFfxFfdlr1z0N14wZGo0cYsTx-0tKrc6ku4LDiAXK60-JCIZjX_L6CcoVqonhgL8PZmDSiUXX-2a-BiL0TSpZ9ea058_wbVbDJjxHnV4bJtPUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaBYiqclLyh9S0HARQQZjPxuJDgMFEHe-H4WFJheMDE9pm_qwi79KFOmHIvTP8BcWOFKuyShR2nMUCqC5cJXgin-wDrLkuz89WWhD8ykFvBVijahoCYDWKbJKPfbBi-Y9pYQqQahClAYp_K1v8xvdziAa9aCJEXf1KDP440iW5DtKjo8-QxFapkpJIS8j1hWczBzK2zRg3AyPSt0ujBNO6mBHBCMKEilQnttJKLjz6BN1ri0-mUi_LhTsRM3NKwrQW_JF5G1i0AFUhhrC_8a1VGVS39FmdW_yUR02qTA-DzKAZ1yiDxg8Pdb16YP0FfRJcQhCgyEqF35Vgs6q8X_Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWQgp0sS5SXYilSXQcNdDU1Lm1Wf9OI8SpQQ9-2CvbVwUPb_XFltNg6_lVkx7xhYnb7p_-PI6b20ytVzvAO-UGelteflzmgBAGr-BND6HconeMD8Dx0tkyzVWzll8oZTFPQqLntrPL3DpXctbc0w6kBRJxp3YItAFJgn_rMPueSMWA3L6y-JJncpky_ARpDUn1rXpcrtzmNT57KuqnZcBAk3Fg4lA1HqnB6DYfFrjCPFcHJ-z7UI-Jrxyml5fAUsjZsjxPLzcg29W0t4zjoM3gHVIJ2ZP2fDsGBz9W3PkE56vZr8QRZNnpOGXRpG2WpTkXL0BU8AAeYU0l8iu3AQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdEDJgRsw5RTEWSIZ0dlO5_71IxVKKo78bs5EZsgH1BqPq-ci_wjs8qmOtimWVWFvjshlvJNCkuiNZqaQHYaWPzVqlrl1AAOgq0L3fxz3MkYdhgl5A8HQeVOMxYcbBcI8QWsDh_-H_iAR8ehHsXA5EJlnGrnXgZQJutg_Fb7s7hCim6cRAVLir9x_tH3thT1i225n4kYg1aPc_N3GuVTmJxvmsYAsH_JCAqGAfbrMcfzhUxebl_mDhJEslzKg9Vya5JoRgb0wbH_F__I7UxViKoVW0GkIpWKvDB97Qpha-SSKHXXrvGkWRlb86uiuZdnLpR146AmPkkb_B8brI4vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baqpaot8nHTS9byJSmLua4k0ajhOsYGECskxmteLAJ3sIqrEPWrhpYbEzBkK-PavkpLWsdJcwfjI-aNoin2D1LGHqc5hv5i7aCkoQn6rGntXe7KTKESSCLJa9R-rQCiuk-ho-cgUqteZCeVEO7tVYqvjDllgMcIU9t4TwBd0EGs0hrcUfgIKDDD4K7ffVQVQ-ch8dnuVOWARTugl5PGt_fGMiOrJdrS9jjXKVhikxyB7hgq4nu7vDr87pSvoAXoEvCXEzzdqG4UNDuWO01p6-lKvWHJqnoY4BEb9xPV2QOIbz5FHPPUXCBFCl7wybqEIcDh7s_rdZ9kRtDiRwLD56g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kfa9eqGP-mpokwrhhTJrYoN0M75U_uAG9FXKe1BJmgnWLT6zdW2iWJff-atvcq0DW4pxXq2rIO73OQm5wnK7MwbBzrLFuObbag___1lkYDT9HXTOIcboiseu4UPdceLP-_al0Icf6tQWqJLv3EJ1BC1NpB9OewrBDWQu3xgI8xUdV4ZNTMKRml_gn3HUwct8QuSA9nyiDN6bp7jUvoZpnTNmTjlTz35iHuWh8kRUuqgrxZZtjxNvK_GrsH5d_I-W0EfO46usxFAzSCzzLVY8RljiQeKnr8Jni--mpVCiEGWj9jYUyNKhAEeqjNytGAjGeRVP5xs1tABj__izhUnuwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV2560JPHBoZxvdzfJZ6LAngvzhQ4TgGs-vYQfCetMpDsYLC2B9w4pmQxxVG7tKIRa_7hOxRpDm3__maYabUe1_e0JLMlv89hiMmOWxIXIK-6IIJhgNvT16-5xSCt545lPaeMKmfhv0Wfr9riIxHcciq5Rbn8V4b_6RsTy72HHzakMGIwgziUHup2E8I2wIwQWKxShYnbFOhNrIrqdAIChO40F_bcK7g6JLpv_cjpP4AYPgBFXth1Bn-bliYisyK0b397rvzKH30fS_SElNjs-gMRfnsOkgGg85VuBu-SarKCsb1QtcAuPg7grZOFBAKevEetQgJzdrdznbts1jt_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpSskmWq9J8sJWGTRwTVbHClbxd-Z1axoAP8VEMj08SkpMAzlAz96deeCPoqRVJvQlcLyK2Rf7PyEXhkBPVslIGFvKu8FiK6kWXgZc_Se2alkrYP8SF6qcH3HjLmWLdYKRiS4RY656lk0uiJW6aHAE0y3D3-b2cDeWF80MrMOkaEw5vtzTX1cNVidfi-HkbJV4U6LLnuQd5ygbnTVPcFTgAfY-KGCZb0IuifOm2bnxVk1GrhdOOcOS90_vxRVAyjkI_cH-7Hy9r4jdBkkSPWo2JY8GoBZnCS3OxJ4YuFbp_KxAPIbLEXbI9epr3rnPikbgUEwT6zk0csCB221NwZ4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=G6VyrsMUxJ61j1LzA3zXdP4BlkTpw7iehK-G8QsbXzWYAcHzgOH7bj_beuAgyyTgfDY0GsVLg9xI4tXqhJWgAm1wF_7z2AlY8sUVfNT_JfxJ0WKX7NI6arThzJhtrSEDH9l_kya3WbSuq3ORlxgDqL3rJ5o3n7tv4SqP3DG5VCEIZJKip85NZZ_PBbfDkEtKzt1rIpWDTKet3z8Rgg0JHKyVn2EqrqgjZesBlLLM0nAIYwlxYHzyiG6HP48YjD_Kx0A4aNktjEaIDTSK1Xc_59ISr2QzdtaTQ7QIOwiWcbUAB1pwOaIpaPTOgE-TaEZjsFbRHdfTBWtpnqiOEz-gFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=G6VyrsMUxJ61j1LzA3zXdP4BlkTpw7iehK-G8QsbXzWYAcHzgOH7bj_beuAgyyTgfDY0GsVLg9xI4tXqhJWgAm1wF_7z2AlY8sUVfNT_JfxJ0WKX7NI6arThzJhtrSEDH9l_kya3WbSuq3ORlxgDqL3rJ5o3n7tv4SqP3DG5VCEIZJKip85NZZ_PBbfDkEtKzt1rIpWDTKet3z8Rgg0JHKyVn2EqrqgjZesBlLLM0nAIYwlxYHzyiG6HP48YjD_Kx0A4aNktjEaIDTSK1Xc_59ISr2QzdtaTQ7QIOwiWcbUAB1pwOaIpaPTOgE-TaEZjsFbRHdfTBWtpnqiOEz-gFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDru8Oh2BQUf1YFItrw_3dxJIeTfmNsKtx19RnYX9uUSl5F1wfGcFBe0IXAKB84fageq4izzerjdWhpUm7fDJ2_2P72Ymwx-_2_V9Db5C0ErCbMCu0L2lZKQ5c8sox1rp1tP4_YCzOjRpIHjIPIXmFY-uJrVMXgudIGwZeddBbEkQSCpiIEguItuTQqV8ngbKuKH4VPg0N263YZrKmp3Pa_4AsnNjaROIZNGlgJ-jvpaee6nHdizX26clcmNN4vz-Xfh89FyxX1IPvDYvVH70i6RS8F0B33LfEkBvS7QfPHXUVr-zp7ZsP60zCrdo2HvwpjbX7hyTFqqHPzY6JjGWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=jGxuOOT6G1pYzjmr3c4kzmnSjDYehQKokLZYDEkKh3Q_lfzoQYxC3ugj7wg0EHbrNrzZt1bjV_1Fcob0bouIq4v_fKsTkWYVtmjZ_gmVo9P13XEiGAB504RkOoUOsRPKSEwsHJvoXluiBRLaqmjBn_bb4HogYckBA_V9-hGslYT0c1eHnE17yFhrduuLnPQ-QeqNGK45EVUV6Wcq737zSiNryvLnVaktMPtAhTEmjRlPHEG3Y_F6B4jFuiJmjgzbS4fsyaPzIE_LduKP4HQu0fWUcStQI6c6G3qCdH_iEJY9z5QxxIlJuH6Gze5ldc4r9beEWbY74ZbcvZvP_wXg86FQmUsyqx_nSOBT_XQ6TeYk-ty89j8JI8p-BOiCYPdvPt7f9A6a5kMnYMPO8fD9iGKKf5-NtnH8rQDqymT4xmdY40uoXPDbcxbyyPKVVKVTwe5XBRpvHB3b5wYZqP8MF2uTv-q1UOR0u984D7nv7yceqidbEsllmDCA1nPRZs5Ao5x-IAXz9sUsQHiKb2NpWh70G5MS38Jr0B_gizwsLUACjcgmI93gij0YlRQexqAcQeLI_DCt_Tw4W3EpsglQmNQ3Ofjm_NUOAFSzcECPcSbSI0qF5FY591i66pIfCnRc-REOgrdHuJULYhMhiQmIAfzey3vcoAK6vU_7Y1LagEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=jGxuOOT6G1pYzjmr3c4kzmnSjDYehQKokLZYDEkKh3Q_lfzoQYxC3ugj7wg0EHbrNrzZt1bjV_1Fcob0bouIq4v_fKsTkWYVtmjZ_gmVo9P13XEiGAB504RkOoUOsRPKSEwsHJvoXluiBRLaqmjBn_bb4HogYckBA_V9-hGslYT0c1eHnE17yFhrduuLnPQ-QeqNGK45EVUV6Wcq737zSiNryvLnVaktMPtAhTEmjRlPHEG3Y_F6B4jFuiJmjgzbS4fsyaPzIE_LduKP4HQu0fWUcStQI6c6G3qCdH_iEJY9z5QxxIlJuH6Gze5ldc4r9beEWbY74ZbcvZvP_wXg86FQmUsyqx_nSOBT_XQ6TeYk-ty89j8JI8p-BOiCYPdvPt7f9A6a5kMnYMPO8fD9iGKKf5-NtnH8rQDqymT4xmdY40uoXPDbcxbyyPKVVKVTwe5XBRpvHB3b5wYZqP8MF2uTv-q1UOR0u984D7nv7yceqidbEsllmDCA1nPRZs5Ao5x-IAXz9sUsQHiKb2NpWh70G5MS38Jr0B_gizwsLUACjcgmI93gij0YlRQexqAcQeLI_DCt_Tw4W3EpsglQmNQ3Ofjm_NUOAFSzcECPcSbSI0qF5FY591i66pIfCnRc-REOgrdHuJULYhMhiQmIAfzey3vcoAK6vU_7Y1LagEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=vp2uDPazUZCaHwaiVgXYPWrIxRtuP53I2HwZ8EZHOfn-3EtH7n0HYZ6XmzaADhAcQdgkhYy5tIpcuJJgC70dQ2caqG10Uv9CjGzYpF_V_TNs-DUYE1-XyLibZm8icwoKWrNGlDy1WZWxtJ_Ia93LVGHDDSald4xZTjYbyG40mfkaYseTEA_2hvdK-plgv7USk3d80PoOSZRda4WD7z0MlDZ5aLWqgtf1hGp8L7rKUBPRlNf0FHR387tfF9lFGYVe4nOEClpO33Bk4mpCDg1MmgdG8LYAXg6LZ3BNY1uoHrQurn5F_SYCZXYv_SzZwsCQehL20ac8_VQK6NwRukhJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=vp2uDPazUZCaHwaiVgXYPWrIxRtuP53I2HwZ8EZHOfn-3EtH7n0HYZ6XmzaADhAcQdgkhYy5tIpcuJJgC70dQ2caqG10Uv9CjGzYpF_V_TNs-DUYE1-XyLibZm8icwoKWrNGlDy1WZWxtJ_Ia93LVGHDDSald4xZTjYbyG40mfkaYseTEA_2hvdK-plgv7USk3d80PoOSZRda4WD7z0MlDZ5aLWqgtf1hGp8L7rKUBPRlNf0FHR387tfF9lFGYVe4nOEClpO33Bk4mpCDg1MmgdG8LYAXg6LZ3BNY1uoHrQurn5F_SYCZXYv_SzZwsCQehL20ac8_VQK6NwRukhJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=FRT5FPQGaj0gxe56JUxEeIJWELnnFtiN9O50BbrUYkoIrd8engCziB0krYr4foqLQtbND7EEHHu-R4DrWGKV-sG_MOvKczD5Hfj8fh8IDDovxHcE-VHTMTgsPqw1qrEg7hjB7iDYvrLmoC2rCwcYA4cy--8pT3nsh3ZFIwjzqjbOwRpN7IOUKC796eqiBA7muNEzwj4a-FS45Z0xdicEmwIgFYeWf9nC4i1a2Jha_qQ8y_eHAsV6maFy7Cu0QQUjWtaz8ylb4i-dhSPd05nNDVaoi2lo7WKoBpf8XgsB2XAADs15mLXKVCXFvoL04Spf9t4krXuqUUEFhMpjaTXgWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=FRT5FPQGaj0gxe56JUxEeIJWELnnFtiN9O50BbrUYkoIrd8engCziB0krYr4foqLQtbND7EEHHu-R4DrWGKV-sG_MOvKczD5Hfj8fh8IDDovxHcE-VHTMTgsPqw1qrEg7hjB7iDYvrLmoC2rCwcYA4cy--8pT3nsh3ZFIwjzqjbOwRpN7IOUKC796eqiBA7muNEzwj4a-FS45Z0xdicEmwIgFYeWf9nC4i1a2Jha_qQ8y_eHAsV6maFy7Cu0QQUjWtaz8ylb4i-dhSPd05nNDVaoi2lo7WKoBpf8XgsB2XAADs15mLXKVCXFvoL04Spf9t4krXuqUUEFhMpjaTXgWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gas300WiLBAXj0LvGhjXxYVJrjysBxM9CAZ1uqq7piI9__VzB-J12QcmE7jsnbJ9x-IQzRnGxDErMF_nx-BoQMhXbb6LxC-nhAEJeNkHkS2-3mcMthqJcat95a15_RP_eIv22VuZNIW4gQ0oDvOWaxT_H6uQEl4pfi9HEKVFs7EXHIANDCWOykcoMcMfZiw27FxosvKl5dy0EmBub08Idm8JQc85SLk843EHLl6B1DrrP9_IDmmWk0xt-NcVhjkneHgJmMRuPliqO7Ip3-NskWFzeV8xmR1CmddZTIHrFCMzxGFh63OkcaGsMCihOB2MxSCfcQJmkYX3hNdztPALxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=OZIHpOmLYnCoI5_F7jAs-po6Lh73SSX9h6ISZiauynbznOrh05PqVmX9-KvpGgxgq4l4THmBfs-VAwRgJdSQSyqFgr7WHn2mMi8Ajg5Gr5DJ6yvciW_E4e7yy2Dr5ByarjUfrIMPVr-4k9lB5u1UjEpDGQyxpYgNHRfh8Rg5C4ra_xQ5H_7_lcCxSagV0SB2Gp0E9_NSxTvJrfOnhrwhxxe1kpE9a7Cx-PONhEjGQMr2jNkZ9hmVLcOvAqbPfv7I28YHLIenDubxPF2n6jjGucuxq_q8AW7XODCjY2S-g6kTW146vnmAVK5LOGDDp9wkaK951Loewn_PrC-FgFxACg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=OZIHpOmLYnCoI5_F7jAs-po6Lh73SSX9h6ISZiauynbznOrh05PqVmX9-KvpGgxgq4l4THmBfs-VAwRgJdSQSyqFgr7WHn2mMi8Ajg5Gr5DJ6yvciW_E4e7yy2Dr5ByarjUfrIMPVr-4k9lB5u1UjEpDGQyxpYgNHRfh8Rg5C4ra_xQ5H_7_lcCxSagV0SB2Gp0E9_NSxTvJrfOnhrwhxxe1kpE9a7Cx-PONhEjGQMr2jNkZ9hmVLcOvAqbPfv7I28YHLIenDubxPF2n6jjGucuxq_q8AW7XODCjY2S-g6kTW146vnmAVK5LOGDDp9wkaK951Loewn_PrC-FgFxACg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWed1v_0Df88NdTq88lm8XW1S8zBHwFBDuCn7db9Q2mhgvtr0phkL_RQ5usvQKfw7FGgCJSRLK2ib-pC9NKzw2P8LFSxk3D570KDixvMSdifGAIEXMimiiRhpYnlLc10bvskyH2JrM3I0q3X5Twf9x8ZzSTo6NA3sJJlSnBABWuOtaJS1WP4fJpiZLyEcYZ6B_D5mUunkIxvzP18_hovndrVnKiaqlUPDe4Nun604DLvhAN10W1-dL7C7HMCfZMMQ5rPWSEFE7wS-3zoKeLeBPpzPfdluWzpmCiuBO67gGHyIhCqMPWO0YCKDO1ac-wnxpeybNpG4Dq2bSQMW1xD8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu9goCFI6pZUUPewPtWbQlrY_hhLyHaQfpuohjPHMsUexopTsR8hODHY4HXj3P3zrM5fUxwOV-T9app_AKZDrpsNOVXUR8rIZl22cZx9p2rbZ0NkP-5LkPlr6nkmKyooAIksBeeQC2tifUt8HORDjIL_BH1R2WurNuM8vX1l81oZ3Z8fQsP7Eq3SBzHZdyEoByJs7ZO5eYlaGfXn0R25bVTlJxGkY9LnxfjbBfF-gJ2DHEaozomhU6I-I1wOmUyxF9at4_UISQpoRRoovlqSE1bQbvj-rR6gMy0ShS8QNf1q_DUMQQRZBCiE4i-Ah_LLCJ8y2vlxFkRBbMP1MnvGyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In62ZE6RNEJvwJ3KQ-N9Dv1sX-RD3Y5TfyvF0cllNuVTSacqFoTZFvFpAq5H9XPCTmUmZaYRXLD9gFYMVYB3cZAMDguFh4Zocanj56odbx0-FLb8GK0Kj8GcEWPC2nggM_Fnw_nUmPcZHYDNS4BByIvGW5ljVHRPubYLbrsPzYAHcRUgmDrsmLnHXskYJrrmvVF79YUB1g7oCNpgseCXmETqegD2_eYDnoJJfKWg2hR4OLz31lYduLVdtgQFpbdgFCchBOM6B1tXzAi0cOtf1gVWl6fGtcCPmtiWLHrLm8dCTq-rwATcUSW2pp3SMkWcx71JSs5-gDUhDjM4svUhKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmJuCkvSJaC2t38xRkW9vG9UqFvVHrX-HzF4hrqGZVMlDnfHOt3V5scmUftGgHYsKxal6XEt9Trrg41McETy_fj2mnmrJuRfW9HC3eeiVPlbDKTUWG4PUImofjZBT7a_32pQPTSy17UVe_bRegRVi8AMvul_ZHCU53elvdcBPXhBNiOjG4UdItMyN7eC4Hw7ETur3pwIcmVAenbkoag5qO8sfCP2mvRyl50kRl6yYl3zJNg2-tyrS4b8zHvnj2Sb23Lr63Fb9p8qlN1RogvmmJMsvJr9h1d4Ye_oYdrd_eKi9f0v8KdAKjJTWqwS4SxzTQRXha3RjSOgR9bRy0dQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti1YYZ70AWeWaBfCTp82CN2xI8uVjo0WC0XxNxPK_SnT-Ow3QrzDVK62yh1KGNzb3KjDXXCgoa_gTjsm5jDax7zeYZpM1Esss2O4SZq9CzA5xFrCeeGftKJ-XZzYcBMbW7m4uw3DpCiH7cSCPtUq9hXhwhmt91X03TfWQ_kEpd3vvYiUO7kQVWLSiPMuMnSWOFb0wWK2J68THkZiH6F8mhD5AqZD-sLDgNsIraNtvsb54tkWrhaQAuKGgKbGKoHqfJgMsw_Q-ljL5MjCJ6CuPh1Z3DAPxBjdi2D7zvZ-_42d-ZpeKG8Nb8Thr4V6T5704RTOtcFyG51Zzjy6BDEOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6LwK9m7K7FKslz1VbGAe85dO9cmyp5EadI5K23jYgc3GQMJzmFmTmffD8vMEPEd8aa5gnFdYEH5MsgXG_9WtgR-mRu-wVTvVikSGfq2nEgC8XO2jBJ_VRK8rx73DnaFzH7rdG7WFG8IkCQFdgaWMh7txhsNI47eQY7uKbM0AC_OCuaojtTdobHjZ8eqO7TjSjUSvmtmCTBV-EoywQM9VH0GARp13tVxRVElAK4ksSmEQJp-n4JlmN7aAFLjMxWSlpk7rbxAQpxdR7gOS_RgtQOn9-NKgRz4JGV8QlolvJ23QWS_U_lq7vsHW5uzaxLVDLNX1EwNXWJOO1z1l2DZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3xmtZq9KzQ_tGeLhOsCgpn4fQo4JLqZaAAgDqSSKI53tuepRgD2v-AtaejqFGPYuiLUKWC4EzYnzfGPZV2Lz2WyMgehBIhrFweGn6wwNGwg9_skuS62osLE8G4gDauGOwSgZXyxc2pixUxz3ER6tVEEMITYjFO5B5FBKwZXeZtUAOI9qH_x_5-DB700-nh_oof9iDcaM24sTxojMYZTj603xP7yDqb5MHF86pME6HR-LhPb_nbc2aJ7vV1AOfIfAmL1cQVbDwO7paQHdEMjAjo2eCpREMXC4Ef3KUGlSqxE0oLAw1FBYpO-7U6TOdzFym_4qiO-NzuPSsTSJGpTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoiTFn1MTbSpT7jWREWKb5Rj52nASoWW1lV2unGCeLaoRTgSYPgDeTuLG_Y_Ys3lY6j-uCja7Zeq3oycM9U5YlURcuhOCOuXS2XLXl8BwkqQlQC_PKYATn5qcWz5a0kddT5nT5FZ3Lrq26ChdYyimDTvXsSd7NOMh8Z-Ekiu3KUONEC5VTIPG0bc6DZ1lTd5hBwb6Hqv-_l8ggmImh49n07eR1mwRSp_5G6DxGSkQv537jwT6g3BTwwrwPj9zqy0OxtU6qbCD-J_dP8RVGsE7HnzooROGp2ZPJyYKRNxp8BtQu03nakROLHnE9INguMnL8D3eLUS6Ke-VLGhw1mTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIjjSJAn07Q2tLXXmcueTlbx3xk2fp2AUe6nFLwIEV30USGQIuCUVraZRW7sqhH2tSPF2UWCD55klpctPb0isvluKLDji19CHjeZrsWwPmL21E4mQLlEFWnf2crPxOtiEmdTRiVx61UK0kvoRxDTaIPdAyWLtb5C-tBpSnG90UAcrcD8MRq_kEWJBEwEYY7n-n65FvoPPxi_ilgh_DbxjxnZ8XWDynAzcc7zYMv1y2eMmV5nHGeBG6YXQui3mzGxxaLz_PlE1-vchea5c4UEzvnz3auYRp8AeRbmSKMeLlOBenDEAXzXg9h3rKJnCRQqU46Cq2W4k12qbxzy4WUKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmUdOesuVTnmvC6pigx_OpcREPftdLBR-2AmUMbmkHD14R_ulwyTV8xstxMJwUAK21uhbZOH1iwXC3Uv91Nr2sHvY1wUEcc6MRaAaKBvtuyLOIo5Jd1C0LZSRWyD6LnF45YTvqm8ZgUD95JW1g2BgKB-gmZJYZM-1Husae3tWkm_ppKFipeXgMyd_IZ2uDIOhDZm3PJpPQEjm7Q23ZYAjcuRXVzMPiVCFaWy571TVDuuH4Q_GmTBjGjS5Keoyv33nmqa4jGQQJF6jBJoVacWNBREhLND7gK1UOz7xbAFIPEGcdu7hx6fEJ6dqzVFuOwlfIPEamWV9m3q9A9LME1HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DsESTGKILV9IeQbdm375ckBAokcVFCAiDQFEFfTU_sNrsWmYgjrlth7FaCyk9zWBrj8zwqtfp6FqxtbnfUq3lOKsLwbWIbPzTlkkznUkHL_wfC04bcM5ObufMKzg1yO8Q-4Jz4mtqpiIKisWQ3cT4LRPK55f387ZcA2PuCc0RS811111Rdg3nvUDxzE8a-wn91scF-UQndxgIAcCPX943mOhubBGCvMfvIx610MUsnHcCGFzkVMs_zsT8IIP6WW7nrcWjD7OjdX3636HF9TBPeRdjiCfcIRIJjO0hqWZ1T6rbGsXnhlBm08VT6FjlXo9n9TlPasdb3fpb-JW8r_NUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDRR7h6jIrl7pMfXi7UMXuImvSXn8-JysenPhJOy53TmaMpFzvjNpNE1RIGKLG8elIbYf7YrxLgZYmlBxdY5mvAymyR1DznMk5SzcdpeTBKpIFVtOE6TqlLntpK6zLMcXY8jBBAaDwvAMV0G86BJ9P7W2IOynz3gSXAcY961EViqkhHUETF-76mB8VvgWza3qAJGaeSPpCI30iX5mDI8vicl-dfE2SHGajY6q0llrT_sJOXSDmLDobF6WcFq8Y2q76OcXlHvUhl2eYWJk33VUrECB9YJvJm0EeZkcoHoly-t6OaZcTFEY3FDkalqCyNczZAFAcsMy1wxRKsf7cF1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2f7KviVtsXaq7XxrWOVtoeRCcpeBPcKU8u-vI46e4Q2mUtL_bIvEcsRcZTmk7DLQcmD_vz9enFUmWiJSsQPXM4eZOsZdLwtXQVBQNwy4vf_XCF_8MFAG4JRGcDKSQA2zHk1YL1PrvTq0hYkKiS2Qa1S8f2Jj3fuSI8Hwm0ss82dvqFbRDqG5MiMczJVTE_sTxmGwrfiRTi7ymTw2VODAD1a1qbQ1QqPX9WOlBZGZ6NHRJZVjCj1BQbGGX8l86Hx0ZF6OwSfrWD4zr_Oi5IDuu14YpQpia5m3hhwveLmyOU43nSQcuZZG0MbtpEllLAFsg7pMSH_bpdyE6CdgeCC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jarFCl0KhVfEOT_cjzTKstmIXg1Kc1EVzTMxDOA4YkkUADpg5v-Jqy6HsmfU4hOM1F5OFoAoRnLKeyU1KnD67rTescuEz_MquFqS6iR45hEgk0OhotH9kuYxEBAdPp9gKsl8VUSwz9NnRsYQ_pjPw7jVGjZznlemdIs6y06sVXmpjPpeyu3aD2GI8DMwubwHhKNWzwAqKjWsaBXFA1x25_2TRrPGh5_JPMvdfAPToPkPp_8FUT8hX2J_IMYx1aCVFLp17kpQsLyDMUWBaEe18fqPV5vsHjpCc7IDH7P2-wvXNrFYkjeYiDauk53LnZ97y5staxradyuFjWQbx-7Urw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=O25obrpiiA1hajf_fsnZrRTxSH4DZE3bBRazDi9NfU5s5Vt3AO0hqYjS8eCOsFEVIRZSVdMsgT38-kJzFbkqzaiQt2AsVw3rfauZP642LLW7DPloO2Od7mRw1FjXYf_YNDysDH7WOI3w7tg8pwGbR-2AAl-3GoxfNc8X6Cobu4e7NFk4MDmb7fGP2jJNLpWEgV8qp3vn9QKfQtt2EN6p4Po4ZtzRnyBCJO2Yamb3jpTuELxqbUK50Ce9yYDosULdrRaf5n9Nt5rFrlFSNd2xvekEPasQvqsBuxepB4kHs_vgYLZ1APDwT2YHxwqSBdyd_8etSgEKlR5iYhik-tvgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=O25obrpiiA1hajf_fsnZrRTxSH4DZE3bBRazDi9NfU5s5Vt3AO0hqYjS8eCOsFEVIRZSVdMsgT38-kJzFbkqzaiQt2AsVw3rfauZP642LLW7DPloO2Od7mRw1FjXYf_YNDysDH7WOI3w7tg8pwGbR-2AAl-3GoxfNc8X6Cobu4e7NFk4MDmb7fGP2jJNLpWEgV8qp3vn9QKfQtt2EN6p4Po4ZtzRnyBCJO2Yamb3jpTuELxqbUK50Ce9yYDosULdrRaf5n9Nt5rFrlFSNd2xvekEPasQvqsBuxepB4kHs_vgYLZ1APDwT2YHxwqSBdyd_8etSgEKlR5iYhik-tvgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaSBt5qhXULfA5_-j7QXw87hS_Cxf6rPXlgsOw7JHYiLXezPpvqp9_6Gij5imRFduh0b-nTTHE2PVeMnzG-DbP_Ib-CPnb1_5Q29C5jWtVF7Wzl-cZgrFpSY91m_K1DKvMmIrVi7_k63ubioX5uceGabl-z0qo6bd-J7TVDxwNHFATi_7FC-UQRcnUX0Ny17XqG2TJrj8SYMdBToE2xFqA-CuOdy64PwgR1OwHu_UiAQHGm_cYIPHet-dKbnkS0Xp1IlNuOviR-e-t_DkJvDom2wt4LT-0Za3YqdMyTJQimv-yyIGnZut4yCjXA6W77JyT1c10_pNYp54WrCYTJ76r7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaSBt5qhXULfA5_-j7QXw87hS_Cxf6rPXlgsOw7JHYiLXezPpvqp9_6Gij5imRFduh0b-nTTHE2PVeMnzG-DbP_Ib-CPnb1_5Q29C5jWtVF7Wzl-cZgrFpSY91m_K1DKvMmIrVi7_k63ubioX5uceGabl-z0qo6bd-J7TVDxwNHFATi_7FC-UQRcnUX0Ny17XqG2TJrj8SYMdBToE2xFqA-CuOdy64PwgR1OwHu_UiAQHGm_cYIPHet-dKbnkS0Xp1IlNuOviR-e-t_DkJvDom2wt4LT-0Za3YqdMyTJQimv-yyIGnZut4yCjXA6W77JyT1c10_pNYp54WrCYTJ76r7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ty84AkFNeuDdkWQMWfL2xO_WYTFwUBMJHuIr3E_QkHy5ghtPdV5-5QnBvt4Qg6Vvx8bIKNm0guthbmZso5l5ovKRcQp2M91glAFWt_AzgkaEkPgdGU9wR0NjonMzdYpDJQYrut9MuDqx_LYlG-1XtFKsB3x292U0UwyBxYGTJ157gkCu4WMafVPvbVGjhUOnPlAGMMI0XbIomYn89JuwoGPCXNUY2D0MXUu14HFXQPilg5bQ3d1iOiumblOaJspSv0z56vJf_gdEBt4HBfsg3XRmTxFLqcKkpRS7uqjzZd6raCY_3qOKR_V4WTR8eoAT96XGE_gznpFw5O3IwqQLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnVF4PWTSs6lXk_Wquabwk4NxN2QfcQVjDJ90jgKUBUxXXCMLTCG3DPoxoQX_B9c8s04q2ZuL0imVYZaticO3eWuwfIgEpWBi81_n9rfJ9cX-DKXHuvZjobappdjIMJgPaKItnkaKwb97m4GiYecJim1RUAEzWbFZswesSTQWRViAdnqo5rVUstgtMrBcmTfQkmH1jH46Yu4heh5ELTDMl_9OJYtOkgtBHytVU-6XoO2NFZvhSroWYAkKZ2vKALp8RKIW8Xl4jIZnxFGvR-9D3PBU_5_PsMA-VXUAumjpZ8U9C10taLzrpy08AhYXFxR9-Co6nk7LXztYW150ZHS3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzDIFQCZoM-snfjqFSwAWis-KlNkJYPIdW4ZYtJs0ceI07RVGYVwrcV9G7VUrV3K1_KXv3kbsaNL6YZkeiKGppyRXyFIIAoCQ4iJGjU9UfIVRAc3X-JrJ4p07EzR-fcyOHav41ncSQeZKNL9EPRO0IU4EFRUYjBOPRnGBnWIqTpBT1ge8hVhWd3LtaqSjS2YHQadHMOwM1iGTRQBC-zG7iBR8_yTfuxA2nDAtJkhIblpuwapfOGxGmPVZt2ArjDvQId27crVVhCT08ln9bFLcwd8NSkqjZ-PWgSgMLhtxK0RPjx16A0spvkEOidbyTnJOZiGR2_TPH3UXuPJXd4vBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=l5eZc9zQG3r6rBTK0ubPZbes2ABaxxR4Ev-DFNbw9_Il59K6kapqyceOQG1mAV0ePiRmCM9Spb3K6sMiDUmIDzavy5dLwYdRz1U14wy8VASmHEQhGWLKRbz7RQs6q6aHr9qV6sYCPycqYsDdEH6PSCHWEH9crYRC14qdtSXGrntDHwEbQLPe-iWFNeDNP9qS5J76xkwLJldNNpMIvQj8Cy7zCcO9JlHtBMOKljKm7BFOda9kF3fPKGhmTtVIoa2JKoRE-PDgYtY5ZCrmKpwXgpmGmDnGgRt7TREZVi-VJr4cYJg4QNS3FRBen_hEcG2XLci5QJwpKgKeab8NgSllo2jNhRiM6cibXYdnmS1xsXTnMAeW4lMy5icnBm8QvMyAVATOqLTws9ra8-6qGKokvjmFWzepSC0h1P1-xk-L7gmBVlzpzsQ3N2NIJM7Y-GazduZiYCPZgUStYxkxLYEi8dm3Dx6eFo3ucZ88WcJK-S5Bjoxa2R1pL5-vystLOgGTly0blO6_rJmRL5niMqZ6cSncPhV0TUMGRSYdWBb-YmT86pk7xiHRo-W2MHA-bPE_m6WrCRiC3pn6_uObsDPtlbhkBgmESto9FB9qnZxHT6qL3OW9ro2gDVIHA75gX-1y5AqCR_QiLZXTBv1R5hByCDLw599VqrDfaqN_sxXLNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=l5eZc9zQG3r6rBTK0ubPZbes2ABaxxR4Ev-DFNbw9_Il59K6kapqyceOQG1mAV0ePiRmCM9Spb3K6sMiDUmIDzavy5dLwYdRz1U14wy8VASmHEQhGWLKRbz7RQs6q6aHr9qV6sYCPycqYsDdEH6PSCHWEH9crYRC14qdtSXGrntDHwEbQLPe-iWFNeDNP9qS5J76xkwLJldNNpMIvQj8Cy7zCcO9JlHtBMOKljKm7BFOda9kF3fPKGhmTtVIoa2JKoRE-PDgYtY5ZCrmKpwXgpmGmDnGgRt7TREZVi-VJr4cYJg4QNS3FRBen_hEcG2XLci5QJwpKgKeab8NgSllo2jNhRiM6cibXYdnmS1xsXTnMAeW4lMy5icnBm8QvMyAVATOqLTws9ra8-6qGKokvjmFWzepSC0h1P1-xk-L7gmBVlzpzsQ3N2NIJM7Y-GazduZiYCPZgUStYxkxLYEi8dm3Dx6eFo3ucZ88WcJK-S5Bjoxa2R1pL5-vystLOgGTly0blO6_rJmRL5niMqZ6cSncPhV0TUMGRSYdWBb-YmT86pk7xiHRo-W2MHA-bPE_m6WrCRiC3pn6_uObsDPtlbhkBgmESto9FB9qnZxHT6qL3OW9ro2gDVIHA75gX-1y5AqCR_QiLZXTBv1R5hByCDLw599VqrDfaqN_sxXLNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB-7VXWBQJHW7ryt5XfBy408D24chcmQS06zfmIlakRzk_zZ3s9s_3ARxqyohmShED8zw6GyanSNsMrygrPM4UjXPsCyeCqXeN0-LHNRMqWtQFM3woy57qdhaKHVHI8Rut4Z1SZFz-yW6iCgPMsfbUfXzyhmMhpWOTcBEMh5UvHYtXZCBc44v-JKEQrfc2BbZfAo9AE4oioZwkbqnTD39mXVWsC6dZ6AiL5omQk5KHlMqvErpgUZgp1kS8klm-c7uKpWL-aBfwnTRWmQzw53SyDCeScAElVlK39WWpX8wwh3s-TRwKyU37nh6fxW-tLfMzZ72Vn07I507iqzSNhWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DujZmlhkD13LtZ_3m9AJzypUffTkDii8s-zO7fGYfAsqQmzEimG6crjCsPwijG9eD-TOX1c-zevS23a5NsTSt81eGKntQGD5jAsgBSboNAnDA6SfhZqd6SxWjp2FVaNF7KcxiwFSTv3qLiwaoHp2NwhXkHtGr_d3baiqot_qIP9GO7911SitMyOmot--tpN92jsIufKfOcfsArP5eKNkYpShUlrKfUKR2zNBvZsMPokMMNVVHsSpvbhU1nZS_0mpTkLsL86YuHIYjTDFSmauD3mGvcc9Dq4Sdq3rkdauen2rlpUqh2LMihDcYsuODtPuwcMm893oIUNUmLg8h6FmUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=mDGEM_NE8Tq6tkPlbkfN5pFIurR3eJa9zPxYmcqHqlEi1eu0XRxCfU5tyyy98G2uUQ0IULYtK5vamkwSHdD0qOZtrphIG6eCjQD3PcbRKiTUkh9uEX_hh5ymNF4n3atAeF9fUU8lwmeUJjEpG42Zk8Ga6jtnSpVaW1Yr9dqwvGm58YfYMMdrrzcDtBpOpepSKmOZqvYCtZEdBM1TgzJJRNE4mNale8x2hREb15POoTuLOcCM956O49F0kOAjTw4WEEftb9CrIG1Dgs1p4-rEXGJqzcExq_RH4suktehFH9DcLHscqjqVJqiFZV3STzIEpsQ-o6bet_hrIPolHpha0a2QEwsGGEWcSxUeYG4OZDVNCwpcbHLMteGj4c-uIqCPGVqm9zP2J3uBOa6tO9BBH2BKvdDUH7O-sUnTBoZlF1KqB8Z5GujgsiBY7AfTi1WUe2t5GdXn5SAA6SaqCxlkeOz_6921BkAtZ2IxOSYXI5eWM19wqUd6JlUHyisY71_rIwLA_TAVLk6MHBakCQyqHmcSV6tTJATwNxs0C1yPLcbohGG-QJ8ZHCE9K8XLHW1DKmXnz_Xg2OM6kFMqVS8Ok8XtvAtLu-ZVL9yF_jg8codDY37OZP-tYHXkSK5inu3zf1dbXYOddHXsU9If8PfT5Qm3NX937f5TrCBibIOboGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=mDGEM_NE8Tq6tkPlbkfN5pFIurR3eJa9zPxYmcqHqlEi1eu0XRxCfU5tyyy98G2uUQ0IULYtK5vamkwSHdD0qOZtrphIG6eCjQD3PcbRKiTUkh9uEX_hh5ymNF4n3atAeF9fUU8lwmeUJjEpG42Zk8Ga6jtnSpVaW1Yr9dqwvGm58YfYMMdrrzcDtBpOpepSKmOZqvYCtZEdBM1TgzJJRNE4mNale8x2hREb15POoTuLOcCM956O49F0kOAjTw4WEEftb9CrIG1Dgs1p4-rEXGJqzcExq_RH4suktehFH9DcLHscqjqVJqiFZV3STzIEpsQ-o6bet_hrIPolHpha0a2QEwsGGEWcSxUeYG4OZDVNCwpcbHLMteGj4c-uIqCPGVqm9zP2J3uBOa6tO9BBH2BKvdDUH7O-sUnTBoZlF1KqB8Z5GujgsiBY7AfTi1WUe2t5GdXn5SAA6SaqCxlkeOz_6921BkAtZ2IxOSYXI5eWM19wqUd6JlUHyisY71_rIwLA_TAVLk6MHBakCQyqHmcSV6tTJATwNxs0C1yPLcbohGG-QJ8ZHCE9K8XLHW1DKmXnz_Xg2OM6kFMqVS8Ok8XtvAtLu-ZVL9yF_jg8codDY37OZP-tYHXkSK5inu3zf1dbXYOddHXsU9If8PfT5Qm3NX937f5TrCBibIOboGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv9Nky4Aw7EWknX354yzXzs5SQhveo7fpMiXAoMQUvMm_0pEtZUh5SIjc-QLilU28gwakl1S89BtMadhJ0cSenAdtny8BgnpqEk9TskbvE1B-DwN1D2RA8lFQSjSIqUyN-qw2yPKIWCb-ZKntBGgcQssb-ruaTwNp4I9ebBM45pVEphGFi6Ro2Rdo73ssBjXms2wyUO-AkxkQO9o2IL68GUvXdQ9PK9ucOMFfuR2sXacCfLUwhqQ6Vwcv_nJn_KvJEMrEK62jIT1J6U7HPfT4CbIYfreLuP9_mGctTD2jR3KOjvGGRRGOaY3nm7m34EfYH6V57pbSvpWZmFBtvqCjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=ukXXmVaX1_ijF7PhlKPBGeKvLDbvQ_uDJHbzxvFzc1mNFoQ9MJujz87s8qdaNyYezv8KZsNvJ_nuzU7h_cgc_0p7yytITLYXF_bV-sn3Wm9jka_Jkc_tagh3tfNSXavOmX_J9RhBp-VT_fpD50yE2nbOqIupriLf9nd0ToZ3BgS1RNoN4pnbXjaLaR10tK-7HrqWDp4r2-yofIMA1pBCPVM-tld_QNzW-nfdNyIFNRXMPsVfJYFg73md8DMl2kz-TWRpFW0Lqm2Tc7O7g4gnZM4VoJxgRmwF12-kEJxSh4WgkmeqdmMOTgteieRW9Dz888e3pEwEZX_wLVfOzeeexA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=ukXXmVaX1_ijF7PhlKPBGeKvLDbvQ_uDJHbzxvFzc1mNFoQ9MJujz87s8qdaNyYezv8KZsNvJ_nuzU7h_cgc_0p7yytITLYXF_bV-sn3Wm9jka_Jkc_tagh3tfNSXavOmX_J9RhBp-VT_fpD50yE2nbOqIupriLf9nd0ToZ3BgS1RNoN4pnbXjaLaR10tK-7HrqWDp4r2-yofIMA1pBCPVM-tld_QNzW-nfdNyIFNRXMPsVfJYFg73md8DMl2kz-TWRpFW0Lqm2Tc7O7g4gnZM4VoJxgRmwF12-kEJxSh4WgkmeqdmMOTgteieRW9Dz888e3pEwEZX_wLVfOzeeexA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ7ZQKJ_oFK8XLoIULiEHKrBvM0zx6pXao2BctS1A51Klw7gSJgMvulY89FSz18i2E7orzlSAb7FArv-GOUUD3bUzDsMdiJ9XXxCw6HOz78_ujw9x3LRfiCUbaWuMJHS9ogoZyiZkjTHkgGSxKBgcgM25sUMhH7vTqZqDbmCD-_qQxfkUhR0XvMAikoRNfDo9M9XTFBNQ1iMQ-DjBLCXkvZ2-rBfqDd25wMeXZ1pBgU08HbEsZfqO5jGAsvHgiZqsacyulUy93-3OcQWirHeX1bROpaaPmJSoP1ZJZ4HIK72R9qMrsf2JodzuGm4S0ohOW7-BW7LNciZFOR_EKvOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7Z4tjVhfOClJsIgnfdL1G0g6A0o5GMXIRRufp2WjZiaXa9qXmNUuRpUH1WvRamrjUg5U3uVbdRS89dB6QK75IMc8Q6yrX7GS0f-H2o5Mvr5SUT4u9LqAPR16_AHKPEn8QbncLpKq2ielZOvM5BtfJvXaEjBM4s4Sqr9BW0mlk3feeVP0AC41vXv_jFFzlMpO0h7jwcQBNQM_Xi9ojritwhoBFaN6elFlJQWtKNto0_4RCS5_raoL_QaaI56P7O8hnJex1WJg8NTiDMaTLzETMvuLGK5ZKZwgC0tOoAPoc4ypctTF8aCHI_ic_A4MCdFGswVs_aOY3LaIrxkkDCPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
