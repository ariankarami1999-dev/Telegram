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
<img src="https://cdn4.telesco.pe/file/jjXcb8SB3yQjEg9vKQNoaoqC9sQVaSYTrLAu8qSCwuQ79-sSNha4oUXW6wAI2G8nUlngUBiUgWeKs2jU_hojNZ0Eoql6CoCvdEADbwxt7_WeBj27U30IESYmfg13dO1Y2MTp6Ou_4UN01Mi9FGSZXxsexeVvD7d9R6Xy2ezO1dqajfOMmzYs3ksLHon7HzOcabgvPGUexZrLjI_YWM-Lx4_PGgXlUCYJ3s1Ba5QBGxxMs-sYaVAHnlX9BdNAUiF6dCbr3e8osxdTJfeN4Rs8WVNfI0Q3YozFr0GNIOMmXLMEetoVt_OwfGBQ3GraYRawqw5QnaWdflvFV4_FdAalqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.62K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=QXV047uVcgELxMLQgY7ucb0Rhqs-ORJXO3s-zlG8jOxJYP0rebMzgPkoMm0RNHq532ZzkWvDevi3ls5reSeDk5ff0HnV-pcBqufGuYD1D1iC_hffe2r-5qV0BQKDqJK3_Jaie1uysqQbidEXVySNwIJHvD-KnnKAYF32k55f7wRDintFj7gZeHZJVgDwaQMsg0yMRz6NWNiiyQ0Ukadk8BDIJ2cVBJTx--jpPNQz9ZAHOR-8mGaev2iECwg4LUsEi7Ew9i7ATYOVSTHzBoKvLNw5qws6f__JRkNG1HbQG_zmUe1za-XcxcV_W1JRRZA_azqKLR2BJJaFDNqki4DrlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=QXV047uVcgELxMLQgY7ucb0Rhqs-ORJXO3s-zlG8jOxJYP0rebMzgPkoMm0RNHq532ZzkWvDevi3ls5reSeDk5ff0HnV-pcBqufGuYD1D1iC_hffe2r-5qV0BQKDqJK3_Jaie1uysqQbidEXVySNwIJHvD-KnnKAYF32k55f7wRDintFj7gZeHZJVgDwaQMsg0yMRz6NWNiiyQ0Ukadk8BDIJ2cVBJTx--jpPNQz9ZAHOR-8mGaev2iECwg4LUsEi7Ew9i7ATYOVSTHzBoKvLNw5qws6f__JRkNG1HbQG_zmUe1za-XcxcV_W1JRRZA_azqKLR2BJJaFDNqki4DrlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 50 · <a href="https://t.me/archivetell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ__2B3xA8cZHMbmUhdTqVRc28XE-TWThx5KgA4GX3dxXby6pzHFDPNxwwjdrdgYtB1zmEm2aQ7SqAyptI6v6lOAxs1-zYlV5MPP4O0W8HaYRjZs__TxjkIf1hf9nt_VtWyrijbV7XTyEkQNjKWqTFw2577fcRVLfL5YtDi9AnEAIYTFz0XMjXSoOrdaUC1jxho3QsKJ_HixkBipNSMgEx99IJeCFhbfdCigSrLOZkKVnUqVftn6VDR-YJn0ToiMqcXTaSEYtXKxMdIVhtSnNwxLVK-GU09wV7Gpx0o4ERUWMmgU4b-zookwuhxKhudShjV1RMK-wxtvuRJoZiyxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 434 · <a href="https://t.me/archivetell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/archivetell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
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
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMQtaAFEFnKhWxymURf-BuZiOO1CsRVi3FDHXBIMrwdWcdAgnTht13PTdkuXCG9-mF3IdciSR0Rt7pqVfCwlCR3K_H-311W22oDTA24PsnCQAvuL5Tvra3Vxy1IiEvHkay9q3Sj8F_xmtAwcsulNEexFrj7W3e3TUEy7_K7wGZn3GEqOTa4Bf3-pvrqZVpRN8gJq_Z2A809eUXbD-ZgsXplDY6QogbF28Z1IczhcUBD74Pp0LWw65HksoivITFX3uVR9yEvaBwP5aLs-kdItZQWx73W5o-NPC2I17-Ce0mTd8Dbv9lY1nm0D8RiGammKFiM6a-QUPorVdpR13yOGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwkYzafYvDpnQn7RPcHYiTXE6aFk-pazk2JOcsfvq1OWupb1WxQc31dD2YGwEirYG6gDvjzaeWwSADPQM2H3v3R5OpLq2IGD9Ib62nMgaTW84-c7fcMKPsr4XHjKoQxHfnFn5AdOsBvx1ftts65wgrMT_MoA0WAw67CO2e5cURchBZ5BnRkF3I1MVTJkLrjDkOFS0MYhEcEfu2ZdOxiWW92diJ8LbWMvgMvRvuqk56PSWebavDPP8JMy-C1vUVyU_uPk2UYZKZd8Q-rctm3Vux9wG75LL2kLqfCab4U8oS0kp6yT8O1YEi0FxV5cPMHFoQfzG07a_7mpdRn7DwE1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMk2DGMOzYqndTNPM6xQafCkXN6U_u9j8eVjUhICgI-JyY1fkbx2jY5TorugwajLKcBbSU-NjCGICfFWkoq0felzBFGFhcewaqxSQ8SqJJWGtREkwgZd1wa-j_Jjm0KgrKoJJ4W8Ks9wDnbX2_TztXTK1iLxtUg2dWM45EU15VKzHA_ChdxOlS6hQIIQPuazPxA0AoGQQ1pT-Jr6aPHBadV6cpocOldElsH3eH4o1w71H9s2CfUFaDDduxjGmevzzSDdw6yvyX3Yh2RWwT7lYaLKYB2mDk1ICQiMd3vLlGtVmp4Evi8MY0_obciGSPgsx53AvKYoZj0-Uo7E-kR-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxetm78JfiJWwWcJw1Rfpl7bKM6Obk_YfgfOgA0QnkOP2tLhgMrP1DXWIrfStVL4GmeBnFHA_Tl0JeWW33Kn6XvxRmDLYImipljwuF9Cg-mlsKxL0pI0rnE_ZDhDoVd3WbR_KZqzZO1qW-zMyi1c59vertuYIY8EdmXtKS-wJx2zDg1IxOrnyEFbRj6ToD3o1nqFGkCEGtYDNKUthKH04SHQDFa8t06kKjoWyp7HsPBhWcwjYrgk0ZoUrJjV6uldAsFxdYtwJ22RS4Y4y7Othw-4G5fbfvKBM2ux0eIDbFDLG1Lp0XKrD6W8yXCP7S0lVMjvOIZWt-51oAwHx3tX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvE-rLskDm0jOJtebHXBWREau84wgE_-l3Ualzt_JXJOFpaHqXW78ES3Ik52Yi3bpC0vKWpBEshw4btxhW0bdApoQyakLuKa_Wtv1-X8-bterLdOCf42ysSM29W0LPKCTNqQQc6Y9tEUgPSH_ss3LOqrBvMHaW_FIaTJkCEpAZI-U1VKIyAGPmQTecOyrMdny1MnIr3ILNtZThaiVwrNwhq2ejvQ3ugmPBZnLRpZkSn74rT9H8zDk5y3Ww8URl4JVukbkOEO0Cl6DbsG8ydew8RJ_aqZ-sSTexuGL1FwbwaBasMUxN3XPugVDGkgOjjHC-gm8IC6WWJWXfxLU5EjFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/archivetell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZkgj266l0Pky82j0kxcx041ZEjx2vu4UG00uaTgaKgUWXwHMrtH-xjWwN-6IzqEaaDVdwmvRK0W1lr6IoqUu_HjjPgsUQpe-wcMpx1NY7IXvtmDk2QUoRgjfnpFuFm4gSjbdPreJAyz1QKxeP-WjLs53UO_zFeIhRwN9eTGfcaXMc01S7lBJSEGBl4Q9QZQlQ6jCXVyv9nIu3Wu-x1aEc8TaT789wK7p3DMPe22FL2hPG3hmqx1Jsb4stlT9xBZcodKYkZFb7SfkGQ2gGA7T2nXXoR2pF0rt5z5lUMPXNdDu-b8CTwCbLn8qZRdVCdPp7c0-IqQxVK9tgZazvgRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2P1F8mcICEOdY9IU6PbhnX7BaiSkXrOs89i7WttFkL6jXC-szVvf7GAWFUU5Y55JOnF0s14ZfVgc4FkKFxgAWonpDi-6-M-OnFg1nkVEByH51rX91uhAW8GMCaqcWiPws5B5-4hNFw_1QGnPG8QBYVVwNnT7kZ4GdtQX4UkCoRpQ57SMRARY8XB6B9IYi22morIag7QQEr11e2X2F0Jt0ZrUChWMdcyzotovLVzjG5k70eA3-PBN6lMMBn4TpznZ7CoAv4dLxlaQEeQnK4FqLePwtxdvSEVJXizMkNEGZZllPV69xwoMeXsyviSp7Kd4ZGYHJqVcAyjtNznxSHd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUhhl8RPh3uqiEag4oYVpCWzM1iPfxJbtKpwjX6PC8CQX1zDbNxSALitKJ_b-i-8I0CKm1yZl31e5q2S3nFyB80WHFt4k339ePq-_sq6tv72XU0HUDS1SuTu3qavYUBo4vvmbiuEFiFYIdk0G24dXYCnEehMb34_OAgp2mw2omc6JoM_okvxEY0vKf0D9jCSsjC3vLtYOMyNIrfbUGqEop3LyI9gepxhwWDt0NEEw75Fxgx8KfbhjbE0S4t1XAE5SWoQuwVI4jgcs6SumJWDNPL3XPCGoqNmG1MAWdC2wXmTv7sKZjhZf8O8cwe5b6WwiP8yv6U3EFcj6lxiMEro3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFzNWHlVw55nsJf-7ST0QjcLQGW2hopbynUowtaqfuyrHyb97yXExTTRKVlOD0kBT_-FJm2t6WbhsGlVcqZXYC0_r-M-KDims9BEDMPIyBn3D7EqsSgFCpkacACdM428w2P2iRYEa9dFQrqeRuZzLfIT8MoR5UDg4QmY3RLw5pRkwm-b25jFHmZru97eAYFLMdfb8X6ETbYy-wJe7VJzqTk11GNxS4XMgPGpwSegoTOmHrkioaWjfnKrN2mUpoYzz6HVos3YYjF8aEHZhemYB-WS3y8G_8OthyRbXn6eFaE0TRYzJSykIbjtWuDvQZFcDG2tnApMfsaWaUSu6Kml-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSE0kTRg7UGRjM5q_2L_9cNx-CpAQLM8Bnf__Br13E6WZ-XWbuEAAGWsYxtk8xdMVcfOGoJSyLo2NO7WR2cfIDo1cMmYeryEL6qB_zoxRurDwsB25LQGurfSjx_iIeIesrD1N2-QpeOgXdzY9cUudQ7oL_lZD-YfRtGjzjpKdmkY5GHXsMhhs8JKKP80kcbH-UvtV7zRomaV3kBEBKemrvZhJtb-pFqofzsgiYYv9ciwc2qmUt-H4tXEG7UuJ8YAtteDLyOX4nJsIYoRfLja_bYRwgheHIPMzvg5DXdTOZ7qz5d_yIGAI5CkF2kBTC6WozwPbU-Tr-Hgi1R4zNimBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odhpIbOxI3J3K5lLt1F7mSv9kjl7JGpasO8aKQcRIeOBFLCkGL4rXf_RWVs1obZ46YwmqNQYMMlaOYRnlSy5fdJ3V8LeUXv_8nkFD1G_7rdf3nl38iRA2zSazYhX7uh0G00ejt4y8ZBBF_KNwTIs9cNP58KWeMeO5F4aF3DFkdGlBBwU8ereX8vBl6RHWzzSjtaaYWU_NMqlDzzgaaBX5Csff3hhmBDzNB1ysf5iS5XQqDx57zsObFjS_LhfGCXP_mj4n5kpVl2o7HbObQ86v0lvGSC2lsGyyxI9dEck78O23PlHlZ98cVnSHSXfYiwEkcU9Ydmb9sg4ExK1zx3PbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkArSeN_cGPwEFUf50SWyFcu1-_I4Mnf5udDG0hjrW68FCcLhCcPsejvTfAEwM5NfxwrurSbaGfo6_TbnsyLDDMEuoPf0bxO29TGghjuAL5btw1nlJQQWBAC0DbE3jXIMamT0DGfK3O9xSZgzR73xFnbq930NCTv01RXCMMkQnJf1UTD4J2sWVCyEgvlwCl7aXF0XR7jJCIoRJb1Wes5qwhNbf58Ygx4ptHf0v-QcYw2L1c7I7cjmZNH5YOTKAzifECfx0lSFzvAW6VTlMMQccZszT284TlONNFy2ZKTrNCpsKsGvETiJgfZgjXk21G83_oVmlrdlvODLQjHGm7maw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooCdtO3plqgNRgC_fwsL2rIbQN1ecRsy_HyHh0EwpeM9pAuVBkrGDWs1Ht90wQLKanQaGu0YPfKox1LOTtRy6120Ay6lMzmvrPrvVGzOZ5XVHFKXqTLKYh7GIx2qd-0SfOyeTBazo--JkEzYQV1FQB28uxN3xpds6AY9YFsQWQB_sTHiP4qYGfpb06DMh9YKXOu5VeHZytcLcH8seaF2_XXH2JZ_mE9f1Pg3QgJIkmdJLnkPXb20ZiSeByfbKgoyrF3_EgtOBj2HTEx_j1p-jqiKejvjEpmlIiDpZyoKU7_cd25IzdeP5s5G5e3mT7Lf9XmfeYhgFtQAg4j0p6PApw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=XfVI_ybrI-A8wNnGQ_paTxF_PPgtXdeGFiy71cHqcscZFl6kP-qsE_TwO54TdxDp7Vzs1vhd2UfeLaPuGK4XQoMX_TFBzYFhy375jg8pf9YkoffT_nasI_8oq34utYqAszS6T4nq2DGdTT5NovT0OzNMU5vQj5NQv5mhC7K8UXMcPddiAwpewvE6DQ_uorsngmtoQk9KzvJxSCOhmGJ8g4GhyymE1yNxQ099ZpFEFKNkrIn3FaFZp5kuplpKBf8JVRgf5xKKf72LWBpiCNg2WUMPnJsSov3wA_MJW5VV8aWQMhy7hu-LxmMVTYsrBuI2qLKNWsNBBnp9WVRQ8s9mrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=XfVI_ybrI-A8wNnGQ_paTxF_PPgtXdeGFiy71cHqcscZFl6kP-qsE_TwO54TdxDp7Vzs1vhd2UfeLaPuGK4XQoMX_TFBzYFhy375jg8pf9YkoffT_nasI_8oq34utYqAszS6T4nq2DGdTT5NovT0OzNMU5vQj5NQv5mhC7K8UXMcPddiAwpewvE6DQ_uorsngmtoQk9KzvJxSCOhmGJ8g4GhyymE1yNxQ099ZpFEFKNkrIn3FaFZp5kuplpKBf8JVRgf5xKKf72LWBpiCNg2WUMPnJsSov3wA_MJW5VV8aWQMhy7hu-LxmMVTYsrBuI2qLKNWsNBBnp9WVRQ8s9mrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecPQGbfFrkt_F8kJ2pUFcNGkly2gDXrcS2S3DQ2E78qFEgQ15v9COb8PCPSetrNUXOI6ivmCy1mVDgfajbcj9H_QLwtm7MDZ76Jnzyie8A-dgvpba0InyPlDJoDgxM1EqKHGk4fR5xQicOQcEYgAY9DIjda75wIH6Gmq4OPkhTE_zK1_h5pnHFpoiastFRqx3YyNVv8VxxM2gBNDmNIuepB7xA7m9oNZy00Tq0h4uBwkyi4DWSMRbB-6wdBSCby1TKVykAQC-CiEMItvKUnLvqzeTPLp6BNYWZjuWK_q7p_gNPZl3J_LIi4ixOE2SvcPWRBhqUAwMleF0-dVHXppPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE13xfquDK3ljRsaOeDLgvx7DX8CaN3d8wxqelz8M05ytjwFBFwAWMMwdHgacWw4Jjhuq47tGATM7B4du4rV6GcCip6rQiq4l9H7-mKiPCG3iZTmAV3CEkLWVytA_K9xLlGtfcWlW1hYCqrcU3vQlcDz8RrTZmapMPQzaeWJ7kRp-jjVTwHIPqNtHjtfiG9ZAnV0HJqzWcJXcadOz4dKaYkbgEQkRgF_kcCo2zR3-DwJzZAPlVNtsRbm36su5xn1EXHzx6BbzaXrlmkZEnuvYsF0Vxx_6twYD5UkY-yzV5KdaItMhqs07lBEIuI2sAvpwBlXQIOZYUp29mXAB_gY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibtKYm7iJevFzx6X2xO06jnm9QhBKAQ0mjAw2OTj860tW7k--E_Mt_naqH2NYs43CnXI4mqkvyldAVoRnyztSh5prTOq3aF89TOhuzrA--q3EXyPL4uSjT8a_24uqcvW4cpxbdg-eLdVSexwjw5Xdmdl_PWN9ORSFy0pATY8WL1sy5mR7vUZB9RFpRCJwTTdVAv_xRBA7Zdkqp9VTJuQab6aVfh8ltbVUPsDZwp158fXnvtbESgCzqEQEPYWjVSEwc0qeuFSr20HQax7R6E5qfJ5Oljdw82phW1rKRNHejoOafRF76277FywcjBdQI3kyJxQ54wEz2sn1-t4cG5Rhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw8mUkanjf7cnz41hKlDMagy8Kvm_xOrGGS1aTS3j-Z10zRjqBVM05hsu4PBsNPAchw__ksOq-lPef64uuHOXXZpywICJjj2-zj-4AOhEwGJ-JsBja3KTYmFJbOjCjenLqN7bwHWk4BniJCCUd3rhor3VGoqwCwuup7j1M0jRlKEucynEAyLGvGwYZ-_WkCjSm5PuL2lVQpTptxYPyYUJ_bB2BTr6IvsYNZmQmXZ7W436LcziUvgqsQcJKnPQfFDAKugJgqdy18AgtuxWJdn4NOSw4HWbi8kwDOYS36emwuYfa0T23wGuS9UO-97JAUCyjLoVfxGq8hwvugwu0FQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=YNb7RJO1LY9jN-HWd51GpLWrZj6ktxwGULKMY3lwZxSPKfN3FLoPh8ebns6VGjZuQJeILHOqcwrH_aipbOAjYNpBMTRWGl0HCfYxHHwbQPHlZpM4IF7qpA77Cu8I-wlbhnTEgMrVw4i82IUZaUOG43cXJsmSGshWOcUGdhDI0LLF19J50ZwJ7Fc9V8SW59UOQAdOY2mIbGyFEjqprCigkMXhP4yIXdCF4VTyDfcR-RELdWFKxrbDvsRhkJJAwUW3oZOaT34quRiyPYMyhY2s9dVZR5Lhsi-wsb7IDq5zOkuKNQjSEbqtrxBgCIzXpOhtUrBcP56pRooMkiwp9zvrDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=YNb7RJO1LY9jN-HWd51GpLWrZj6ktxwGULKMY3lwZxSPKfN3FLoPh8ebns6VGjZuQJeILHOqcwrH_aipbOAjYNpBMTRWGl0HCfYxHHwbQPHlZpM4IF7qpA77Cu8I-wlbhnTEgMrVw4i82IUZaUOG43cXJsmSGshWOcUGdhDI0LLF19J50ZwJ7Fc9V8SW59UOQAdOY2mIbGyFEjqprCigkMXhP4yIXdCF4VTyDfcR-RELdWFKxrbDvsRhkJJAwUW3oZOaT34quRiyPYMyhY2s9dVZR5Lhsi-wsb7IDq5zOkuKNQjSEbqtrxBgCIzXpOhtUrBcP56pRooMkiwp9zvrDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=j-wfkSaXNbFSdTErHbLZZwQXTOJFMFReGqhq6r5Rl3pR9bGb-mu3LwJeBUJJfr7DalMP1-4xU_E1u8iMFDEbY5KT0-gZ7bOtUpKSqskwdKIlwX85fUg-QnO54rcX_BCHzTPrmoU9e2wfDe-0X4DoXomHbNWwk1MsBYUJVv5aTeB3jyzvbDROfZYqbGu4sviLX7O0LU4_yUEagBefsxAYYlaKyTizdsyaPZ_GvphD5hwqNcHTz561Br8JXR7JrV19Cmq3IPzhTunG5fGaoB0C_Cdr1-nHcZKdSmOQtnFi6ALm_bVvk-FRE6szdfh9dJfEI_yR7VJe2uVjVISIKrVDEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=j-wfkSaXNbFSdTErHbLZZwQXTOJFMFReGqhq6r5Rl3pR9bGb-mu3LwJeBUJJfr7DalMP1-4xU_E1u8iMFDEbY5KT0-gZ7bOtUpKSqskwdKIlwX85fUg-QnO54rcX_BCHzTPrmoU9e2wfDe-0X4DoXomHbNWwk1MsBYUJVv5aTeB3jyzvbDROfZYqbGu4sviLX7O0LU4_yUEagBefsxAYYlaKyTizdsyaPZ_GvphD5hwqNcHTz561Br8JXR7JrV19Cmq3IPzhTunG5fGaoB0C_Cdr1-nHcZKdSmOQtnFi6ALm_bVvk-FRE6szdfh9dJfEI_yR7VJe2uVjVISIKrVDEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1b0OUeWNGp6ig4dszblP4Nhkh0GX2J92W4Wztdq3Kuc17d3Bi4y4xB5FnIXkcruLktzS_eo39rxFd6bEao-Nb94HlXQmZzLEKD8vUiFiZs44dTO9zLLkB2M-YqzGo_0Uf2NCkikIYEhUMpKusCFOhrTqNb6XS2rFHUADVCR2oj6zFb5NKFrmzD4V5ugOUfDIt0rknTFOy8LTgzb_xJk3XmV4og39xmMnhTVqZwhR0wNeeWgIa05STjVLOMwmmtvN6toyOzuTS6IOiCqOCg9QhUNnAc545f1V7rvJNGq2Cl6zBXsvOdeLGjn0n0qS_VHPdVCXFq2Zf7GyCWiQdzQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=C-UbM_zPHoGt78Fag70z6_hXYVxbhUghGBxbaX7THlMt9a_w6JylSiqxyIXBhtyCr4bUitt51RwxdkHLdsmJU4a9JshK0VofZ60Ot67MEkfv8xjd2zR0TFuThhBeMCloagtmnjbOsJ59BF4FBBd4avPkiMyzRbtc2y1BKDztT9yFp5hQltYr7YLRWR5N1JdHna5741AO2Haz9DRFTPKdd56foRI7r27E5O1-OmuiiOrlwjhNtPcmAHeCc-DEFzo3KrOKtMUbaRw6EwNhhp5rY02AQHAI6AT7pnmjcIa9NtJL5F7RpTJ-kpMqlFEPdXi0lYy1AZEZChOoQSg0r19oAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=C-UbM_zPHoGt78Fag70z6_hXYVxbhUghGBxbaX7THlMt9a_w6JylSiqxyIXBhtyCr4bUitt51RwxdkHLdsmJU4a9JshK0VofZ60Ot67MEkfv8xjd2zR0TFuThhBeMCloagtmnjbOsJ59BF4FBBd4avPkiMyzRbtc2y1BKDztT9yFp5hQltYr7YLRWR5N1JdHna5741AO2Haz9DRFTPKdd56foRI7r27E5O1-OmuiiOrlwjhNtPcmAHeCc-DEFzo3KrOKtMUbaRw6EwNhhp5rY02AQHAI6AT7pnmjcIa9NtJL5F7RpTJ-kpMqlFEPdXi0lYy1AZEZChOoQSg0r19oAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d90svFVP178qans9jpvJh1Q99jIvMQKB06tYdTqEEc4e66wYB34QFyU1RJv4mMABvvipnx--hYDpy6xBvAeYHo9OHfUx_YiBpVoDhVgHwhL07RLOZmaB7HKsOvFuKsL3dIKhFeWbP6UxTse-5JsilXaoVqUy8JLmmY9Z-pBOGLC5TXT83U5chiTGkzpBqMeh7h0CLxeu2egherLKcMtaNDHH6dLgytRi1crWYnOczVhsY6be3FV_41gybSfj64DaywSpTKXxxkvozUnjLy6fYWWa6UjC_4AXndsQ6jmy-vGBwcT5cLvnC6ZJBlpAMjDLgTAaknCYGUKoMip3aWn8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBYR9daiYxI-vuf3AgezpLVuXA6ZSgjk5JR3aRXtp43qA2rxE2Mybe4875YXizgjZJqqflDG7azRcZiyWWpe4dQn7MYeyP5ViIAGjKczWI0S-AdNWKm6JvQcDoiruLOY4TaIwHzn9P4HeM85fpXu2M13tTRa-edhpwrIRQQpdzfJfBb9I_TjCZ9yL6bHrI-ojuzlqS3ilKFZK49I3DqVXryrvtihlzjhxE5Qn_1FjxbHuD4pBXbihViGQc0Du26iBe93QrvOnd6eCyESCal844jqBLVd_YyX4MlQg5SH9jEBVcsQcfbgARhCrMXIk_yGXDmJ2ufJynoEACdQFA7z7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8rHKvfxvdq17iqf4l0JZI-qNpxtqOTafc5utGBDwihqGNsCXQdiUFPgVpkMEpoFMXxqyOW3q_xn2V0zcFGOAd86lUyoZw6p7lqpGtFWiCqsk585P6trBs3akmmgtKWatyC5GB4NSSU7C8QIJt86TMP4YNyPHonKagCqggGWoZc0tP7hlzpORVSICmOSv3JsuFJVfRAYt-Yo7Z6m8vbBJnshLkKn27-LMEbMNgiRrP9kyPeCaWc18ZWewFcjyKi9o_H0ZThKpO5LS-03ZoRiRbMwTUYO2IsV340zbUSjc4WhHyyjHaZQPqyBO9MNG9qE3yFT3O-VXvY7dziAILZF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA3aRERKPyg6pntgELO8rH9CHSxwMbdP4z6Id-d9m6RNWy6prH6PxR94-VaX9j5QtjY0fR1g2P-Y5jwNUDH5uHJa9OY5aT2utX9XMayx-T8ApqNl4AiqtnUP8mTPpjxmz9_NThwH5Pb7_5GoKQh7n9kvr7kBQUb5Tnfp3A1aHqzfWDhkok2XKgbPP8vMPGFzY5HJii_RXk5YDYKKwTUD1Id1i4e4eVhEhLpNjr1rs6OZEv9qmybTwUGP7mVhiKuSjJHUpwtUKPWzBH9fQVGGCiIjvPCh-vniPv6gsizP50QrOXg3YXCgdCdD-bFpCZkpBYu70YndGf-5bP49yUyUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=jeCPM83cBQmkevTg53T4syQHATL0Z1Fc0vz6FP1oPgdyF6WoedGB3_269XDZLMrzjFk2uWcHMb_nIeLTxa4q3yQqgR6cSLZfpj41OUEGZhgOgPSpFwlqjihsCVoUl1OaqhiZGAYcEk7u1RlXjyEJTXqTtTRUnitE_bY0HJBQNpLTR-hPcElKwVOtOdVi1gurR6uCABojU0Jy5QenOzMWoxRYpBqoGH-6g3ZV90NVp_ZVSuCZpDjpDKoTG7kYEhlZkztUQz6Pk4Yxbe_9iNPqsKQf-rp0GZbPQkOFieok1-2OnH77oN2jUmowX0xklrRp1ru_IzjyHc_7MRAsKb_sIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=jeCPM83cBQmkevTg53T4syQHATL0Z1Fc0vz6FP1oPgdyF6WoedGB3_269XDZLMrzjFk2uWcHMb_nIeLTxa4q3yQqgR6cSLZfpj41OUEGZhgOgPSpFwlqjihsCVoUl1OaqhiZGAYcEk7u1RlXjyEJTXqTtTRUnitE_bY0HJBQNpLTR-hPcElKwVOtOdVi1gurR6uCABojU0Jy5QenOzMWoxRYpBqoGH-6g3ZV90NVp_ZVSuCZpDjpDKoTG7kYEhlZkztUQz6Pk4Yxbe_9iNPqsKQf-rp0GZbPQkOFieok1-2OnH77oN2jUmowX0xklrRp1ru_IzjyHc_7MRAsKb_sIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_VwdzuLb4-rDLLdFXW7kq83fuSqu2ryaOawo4IhBpIpMkyGa4WcOOcrzXtthKk2b0cHd4IEUZf7OaYjtCNaSaTDA0vQcXVh5o6gmPobfkEG4ytIP2Atehm9NgkpUeMo5YzSJEgX5OwG6y5dNRgFJbbXQXvNnEMlYUu6CRPj7wu78h1wULkwGAykN4JUu1paxoNXil0bBjGnLQZFNNlh9Urcrcr38TeJt9dogSwrPdVyT04DffOPzikFjm_wONvUtBcL5-eEM3IsaRdy1Qtr6yioqAolPwVLD8eitv-TewoCVHPRD36hJQGZm8AD3vokmUdmkkyXpzd005EOouOqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpeU3E6RHeP7ccz8lfuHodhll8fbkTVDpSYPhyIx-MJxzXqj7t4C1nmzSKWah1hA1zwZ6NH8f-_Mx4i-6bl-HUsVgqjINjxA_46wgyGkJdpjaguiag0BBRgeAn6NopqwiRN4jNMrgnw7BtKOJh3ueNrB8FlxoqtZrIRNztk39l2y8l3EVf0gahb4IMMK5i7ERUkZWKV3NdoTke_HHgT1wCTC5D3pQnJ-qLU1uhs6vL_8QWA2qYFJR63OWk5A0BEjmy0SQXaWuZiIuyoJXf17grCqMqueHvo-V9VMhaXO3xv7L_hXU_tFcAlvMVB42Sygwob-6QViIX5g933aRo3M4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfMU_NSaD8uoaeJvEKp9OEr_OMYPXdpM86IQKqJBgSvh0rJP4KnsHWN67MEdZmfQPTLSEdj3hkvYKulsIa-_00IftaGJNnHDdcVL7dz6q7rh6lfEW7oufxReQ7a_amPzIGWeq2xdZBFWtcFI5dGdO80f3G2rBFBwFpoEIEEWu8J8Epy_vlVZvOi70iU0g7N06py0vvgZVJu5lJvugM9yfplR3yFNYwezmErxhFVG5Y4n7CzOUFY7xHczoOQiFeew0Jp0cIiSAPSgW3A1zZm4kSlJ3bhpee4B2q9Uix4GUgCojsw1DlNLOR_TEjvUBRcs4AVZ7mrncye2pGJZXNLttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6Jo2kifo3GY4Q6L6rMWNFQX9AyLFd1iwJSJw958M5KinaBAJ1kxz1WDpzKBtCnUaknUzHhR5OUWLYtrq_8vyqgpgQHAfjdF1fzfNLgVTZEQB1Gsc5KNUs26ZNEkCujigQvzu6kRIY-bv97Ev5CVj2IitZSIk8C51O90GmjYgCdOb_lLWRS6J12aknXiWz-GV5DAjcTva77FGxhBU5B5-OsyV-yaple43aSyrjg59NU4Qzao2q4CNMz-r77sW0QoxM-X3SzO7E4RlgZxEe9j19UuRGZEFZ_CYUnK7ja7jXeCGShoxUiTwI3RXgMMpyuUlFmoNlIl-oBb2HX749CiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OANo_iKIg4jhehuBLdDfAKuxWgWPvbidQEDjCuG7FCxeIFMXrsw4ZaKTyR-qPMP5ZeD0RjhTANIV7QPMLOHxHGZCTuyjIqrUq5EvhqLSvteoBcYiHhBIv5Xgw9NHME5OyR16q82Z_iOhvL8zGzh1tn0ShylW63M0OVWyACIHizQGk7yWXsqeLY4fCgbdYMrlwbaXRikrZJfuhIkB19pFVlqreR877NDzWQhUBM2N8F8B1RfMQI79L4i2MrOrHbH26zHBo6gFvi_SW4cLOfq__Wz2TSUqZde_J0dCnsObjWf8ALZy6AdXaoz7CZ19jDb7Pn8MvEmSF5VnW-abEJC5hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdGayP0YNGIBxz6h7SRQ84uhQqNos4OkhVlU4UL_JYQk7_gM14QIm_sHuuwJ8P11eQg3S3xhcNlMwCNg49zuRQNISjuK1hAGZ8E6Zv1NIfPonaxHgg1sMLqDPjVcjOhckmtco3u_On9Y4w6Cjw4TgswGx7MsbB95A9fZzJyFVpsxg8I5o2jBd2m7l1KDV0GxiMgXiXumputbx6no-LNHicbfeLIz753BgxTbgfzvs4h5USMp5BYMMbqFmVrOX5PVkBZueumuDhWO9Bog-OlO818Q5_ZS6puLcBYrL0HlSjliwHaB8yxG1ruqHd_dWUHPYXMG8fqu0FQLeyT3HaG6bg.jpg" alt="photo" loading="lazy"/></div>
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
🏞
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1ezl66Ah9ggK7xqsjBPlDCIep1txaV4y-rMqx6fGzs6HU3XvVhDS7t9jAhbXIhun5QHlROQccbriLJ6YI07R0w3gRAqg3IFVOHwCV-6r2LurosYYjI8JFHUm6efYysXGqXozfiIoFjOsatvRvouQi1weCvaop7Unahnb-jPo7qAtbJFdtnT_LI3zl-MSOSg2wEVOadADR_fNagw3srcR8TcBPjpU9AWpy0W8fD0vgstZgf6pnIg09e9X-q8a3oIkSUz2In0Eo8Iap0zlzwo9qLzGUwzVfydcC3kZxUPg0_GxkLUjKCn8fiMF_REWgkLXAamT9tLhKNHzJl5y-v6Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=gvku9jINb19mM2d7-tvHo_TWWvVambIcvIQ_ot8sah3hmAPHIHlNAmFsLuj3n3uAcJmivDKpSwOhIhlX_zyaQ2bKa3uBiCy9Ita70diTf3VYYuE8tSQ_9-DzTi_garecBvTjB6j0i9CkOcGOCfv8HFfAxtxREketmxPNFN1GLN9LzlPnz1iNarfSZQH_XAZ75PSski1uMr8mbPhk2ZDbEeCbMi5auE-y8GeTyYBrGBaIYWXT2QP8fVdeqPfuZSwEMd8ef6Pzv-6MeUDW3ljLzvya3xTyNoMAVymHyiUwTP0Zuxbz4kcOp99SRqnvEcGCih2c4h-u3f_PhVYXGEH51w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=gvku9jINb19mM2d7-tvHo_TWWvVambIcvIQ_ot8sah3hmAPHIHlNAmFsLuj3n3uAcJmivDKpSwOhIhlX_zyaQ2bKa3uBiCy9Ita70diTf3VYYuE8tSQ_9-DzTi_garecBvTjB6j0i9CkOcGOCfv8HFfAxtxREketmxPNFN1GLN9LzlPnz1iNarfSZQH_XAZ75PSski1uMr8mbPhk2ZDbEeCbMi5auE-y8GeTyYBrGBaIYWXT2QP8fVdeqPfuZSwEMd8ef6Pzv-6MeUDW3ljLzvya3xTyNoMAVymHyiUwTP0Zuxbz4kcOp99SRqnvEcGCih2c4h-u3f_PhVYXGEH51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡️
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
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0AtzkPcYkg9tcxqafT54wtm2IWXhCLtx7OseaTFcp4IXs_tAdjftmx5o9nlyl74huwB4rj4JTLd8Le7Kf2FugXqe54ukv72TrpXvWYZebeSEFmh-rpaCD6sSQVK4MMj4Az0ybIY7lRwHEEDJbQDmx736_t1oPEgGL9O1B2qovIE5ifHZHEfHyMJ0ej_5-K9Wr4hnOUt9d08dvBqg5pqIWp0ZSBxZ-2I62tNh9WeiZ_kj77axzLxpxIHeUEdaD392HdfTPUODEkrFuzFV6iBDhs9qUK3XGJjoarL4p0X90oO0RPnEVhPSV1Mvbq0Q_xbcaEyVuh_XiBRIfeZhrgrgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0Z0Ubz_KIMAv4sVKwujc-0XFeZjU5zG-QwUuwNQ1mpCSX1392ZCOtulPkwm9UiXO4ZU7e1ehWIGEPCORiVXVS8Mwf9PL0x3ijsl4RMjdjThi78M0HmONPBCf0-1uKfpw8weepH1zQd9gjRrZ61V16QWMJf2JoTgxFfKC6d9hzC7zBaYiC_t2vi52pYDZD9tkRW6QmELNTzMAtbG_aSZgevFxM6jP7VWQ1B_59haIRS4I9SV76cK0ZpI86RqIVvPYWhCBhVfJAe3fgfBddgn0HSJJC-Dscyu4F5309-aqHTGOnSvtOkFQAjhVqqD7DaatoqfF30DN7dgr87CCUYE1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqBDNQq7iUsDVGnn9h-PuwyP9TCJO2MeKmeHnuYSBlfU9CYyQJ9-hL3TZHGevO-grJjOYaBzD5el6bbvtAdxXpjbr0mlNtChWhcPR_yhVt3hzPfWOo0EGpc6ffv3y7qR3OVrM5ZuTGuzLndz8rPNeRVzP1AJ5BO20nAnhTyMjI6RgFW_WtGats067A7XpZm5ZnrI3friHwsx0K7jVeZCZIRfORcfyNpwVh8h5dfUG9SBVek5fiOWBSXPGWQ-rU6l9T8cPuCebHod5kPHdKj1Y-OaaV2p1guLplZxJFtAOlAgbExcCjZEhPlwA0V6P2XnBGweHodpjxl3v1oirrkIUQ.jpg" alt="photo" loading="lazy"/></div>
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
⚡️
قابل استفاده رایگان در AI Studio
•
🗂
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhVH41mx60coVIyW4pg8-NxTawElEHspTJ0WRUyudCBbjgBn0tsE5SYL-v1lH5SBAawMpaEtBO8_fZfKS3lz4hOSxm0lgZGcgyhlyYvCnJw3kqeLvCCuyTdTRawGGUN_sAS2G1Xwka6oJfjHwAJM7jzDwnw9jCjs-4Lkdp3gmN_RCHFoXT6jY0q0WCbIgbQWhTrABE_gW00BTsEgx561uji3XrpCZEf48zeLY-cp7tnXTixXXAXfPsMV-_bAPynubh2Qe4fMSKyn3163MpNguCWOzXwTXQ-uhaibyz_wELC-8ju82qtlTOVFaJ9xvWi-RFEmYFzz1j6UX4FeFgvGPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/foeSJImU95-ZwiM80ShgZc5-6SjfMuyX-PwbRRJNhAD4EbPWdJ6Kn5JeEVDcBBgrJw8HXbBfuMsR7BBoBg4aolZUonARPzVLa-UdalTJ6o5bx-AqUqnJ64mwJ7vDmp24Q1RlH60j56GY5QaBfXawZvgpqqB6DEOEfE0W1HzqQy0koCRA2DK6a5cCm0jW0r0VwrNjBRklYn_GmsyDxIHTThQvmPFbqgYh7DBCBXxeRqtj-uT9vz-KqRDZpf6b2QHqXjN7j2ozPTjGzpcXnhNkmvf1ikrRS7MCG0DZQBnPjNDHHMyvbSwy0Ygqi3NiNHjLT7CH_n9whZwS0QZGwz81vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgO1uiQDd5_iAeeJ_upxlbg-uWibIJsENuga3aYp0XCPIZlKrBj3j2rYvz_Gq3wp6GzqmRdnf40_x9tmBog9u4gMG9ucQO7c0LDYWghmhUdx0TUAkKin6UBepe1IOHDyAFSRIjiuagkUq4OnPfeHPULhq269LDualmkASv3LYBTwbW-QfTSHeQg1AXTmKHypB7h-L08VyaIT-pZA8R8Fo2ryyne9NsOpzQ3hu1FGRVb0NEe09L-aMQd96mF4vgBOW5fuadIflfmlUz8bd2g2Rv0478PfdsbZg32A-3Y2Ypv79iEYCE3uieZfDFaGIIaUe5FRNiS4P9fBbQX_a_Jm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiFZamgvu1ySzlC3R6VWxpmeEiyc-VWQDA6NP4SpzF8fMP-3kvthYiWKZHVZ_HM3NSHB_ihzc7BS_aUZK4C9i3aWp5t_u9chxsyGg43sloI4UFFV8M-43DPocwjmqoPgnvG-XZ8fKliifmvVPw00dF_9bUGmoQvIzD2DcssruDeLGvUQHMh9ZT0xhw_ADZkk6kWVijiuRC9YbcUbXKQ4ai6MY9PbqdTUiVvpFDyqEyrUSuHmVK3rqfGlkNLjRocJ2nb1eiWOpoyRzqhB4BUeYIU2UjKxFYt7T4TU59BT3bToU7mwrizNJinTGsGyi72eBbafg0h16VjtjE5ilpLFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJuUCsDHUBwqP_Mz9byaSWlLdYoyVIl4OSPvEc7K9mmutXhwN82a7rAq0tGAmcbI6jlXPFgQTTKC94XLyxjv728BAft1IIJzpY6MjJ6FyV0cjaFG3oijUzslsLLtIojcmlelpheHk31dysYDc8r5g9ll5NBLNiOC4pkf9Hu3TI8HlKLySru9UTDzivJRm74DVwVzGhKCcnU95RVZl0xBdro38SeIxDtTjJTyN3qcoGljuX-w7p2DinPGTONvtMD-mE1XHm8KUVc4euekgLv6es7QsOFuydR1FE5kxSzideTIO9QFPUOvTIjk266WLCFBVZ_deWRAPDcWGnePOFeP5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1ws4Voqfpy9g0hsnGV_qqEbKDW4imd-3I7h_xOAhjGNwwZeSwPH5VC0jU_BOUxAb6J7XSuGbJVdhN9k7azYJzosqmFX9JZxNm0HLsrv24pVwAy0SQr3kfqiA1Cky6EU3fL81euJ-ZjOurzmXBLC0EoBrHZBKrRTBfCTcnubzFBNNhROE-W-mAZ8bYSVd6ZOOFt-Z9WwrjnWEQJH_g3GWtkYiES7h8vPJEyjA_SGOvXYSr_JTnbKdRICDYpEKr9uHWkcXjURO2JIBqFMi7LXh_y0Z4teEWZHVor-MUerSUMthaWB3VCwlj3KuCITLS4x0g1mKI6Z0YWeL0svnLEadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5qwgiDdi7Kfl-pc7WM1wxs49gmBq2RNwgrxPMmkFUtt-TFMpJ1kTxGeHsfGIqXo9NaLAn4A_PK5fiYC779DpiPjxPxldjcoQvAGBQmfvxatkSIh6QlrGQRSyipweN3-a1Ul15SHJ1hLmZk76S4Uyh8DQ7D_4TkCIYv_ir4MizYdumHGnJn7EkjFgJl33qbzyAlEii-4G2E6EG2ClriNcWHqdpWnpi_AEnTN868me07gdrMh-MZxd1vrj2mR7MNI2bwoBlsVbRv3CGKRYjxfzYSslxozd-PVA6gPSt66TCIxVvKQNHJ9qZDdinueEUiNo-gEuLFCgvyUpQdF5G1nUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQIszLprg9x9iRHra3GG3DsVaraObAxmm4JXMIeg9G1pBayXfsPJMbUCVYth6TrqWwQPlvRPM56jJ1EB6g3KsarP9AzIRwOqJfte4RFeG2GIc_Al_fsl4pT5TdAEbRgMIWqxSlVz25kGGkL2Jo4gvuCSz9JBhqvjZuUIC82GRcPEOh1BFMYb1kaunQTU3dAwwqC2P47zxhfCC15aNJIZx0Ulp8RxGtfxdeGhyYAOuyEBSYQOJnEWPoGhtKyNzwhblJne-J-dgfqa2GJxFmsC54HQ4bJuYOw0LuIYXkEcug9Z-PDTSDk5Hwr0jDPuj_ZRt9iipJqg9drqFr0aAR-e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTs6yh4y51J0MGLtYI5NHiol1JEwJ37A4oalhYLXcs4sKNyPlamCQkFaOdYirBk5L4TFauoE9wMpK6FG65j1F1B-IfD_Au33Z2tYHUBQ_6ZLboc0S-wI9gQCtTfVN7W5MRDVjiKUoW_ZXDWcSUFBR6yTwWFwuLpgvMggxmEIYWVw_hLZfGCB95OY7QJxRgK4N3C3WMa9yYKeARLvWZK00rZvWQYDp9ASmaUNtnoaM9sU1MfDATqM9WyzPCAbz-qP3oXPQF9_5-5FIWslMyQ6BQ-vUCv76qvcSVSZ2A6qQlK0LHu7-t-Z1Ty0fkLb94JfwzHDVJLhTO4TzOLzwOLmHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=B8fbixc6x126UVnyI9qEKBAHOeaK8mCXahRl17Lrnv2L_70flBtfN6RpXNsp4Wn8mqNuC_pXNNhDdR2520oPU6sFOh026P07hQ5ccb1QImvOdzk9gJzD-Y_0zndvmMHD6wQw_P4j6Q0oEmeUD3GB2UaOLCO5ras7yDgS9rVqq7gb07VZYNApjnFTETiesMwks95etPF-UEXOShydZYxk3Y7CmiVWqv8CMHMQwQkD8MzB9QD3dF5mwTeN-9IOj7u-gbHGhbTD1dpJUyWd1eCdN6914vbDL0DS-JUtV6187Tw9WkmOOQZTs6HSepRdA7CEBkju7qBPOopD1_bIW-0S9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=B8fbixc6x126UVnyI9qEKBAHOeaK8mCXahRl17Lrnv2L_70flBtfN6RpXNsp4Wn8mqNuC_pXNNhDdR2520oPU6sFOh026P07hQ5ccb1QImvOdzk9gJzD-Y_0zndvmMHD6wQw_P4j6Q0oEmeUD3GB2UaOLCO5ras7yDgS9rVqq7gb07VZYNApjnFTETiesMwks95etPF-UEXOShydZYxk3Y7CmiVWqv8CMHMQwQkD8MzB9QD3dF5mwTeN-9IOj7u-gbHGhbTD1dpJUyWd1eCdN6914vbDL0DS-JUtV6187Tw9WkmOOQZTs6HSepRdA7CEBkju7qBPOopD1_bIW-0S9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
⚡️
اجرای سریع‌تر و مصرف رم کمتر
•
🛠
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmOtdusqa3eKIZTghrXjxhwc0hlqR3IsD8aN_E7jykmmOFjepe0AAuzdwQgP0mSF5f-9CNOsu4GYj5cYSW_6lBwt6gXhJWEI8L5curU10PMFpvtFFSULPRjezI7dgBDLt0mBU6hksr9QftiCjT2TCb81CxTV-B9naAQtIvT8s9WvdM5Zfurt7iekasw7yOgkGqFYIXraVPxNrIwLFF46qW_79yRHdbh6vydbEh3zeL14Unsr3KrOe9RtKNtIsuZdI7hQtRAfuwh7XxvvaMDfmHVJmD9vmaBsasPoQ1__RhoeINiFY7uurKG0BFJQ_2F7-qbp3pPRbHIe7BwH4LcZfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrMkxWdjKb5sOMLlsbeRrX7b5si2We-F0PWU4rr17-nCa_7o55ZdNySJ30SAIHwYQarttVrb5r43qqslJQJ5Ky7I8EyiNAWOf5D0dJKdac4KVKMGgB03UnIsgEABf-KGlTQBgtmdW5d7P9TyXQm36aRbGFcliPsOrd3kaOR80JStLcV1DMrobq9li9kXlr8wsQdfRlukD2F7bp4vUfvuU42320utvYC7P3sm_qFzhRWfloED_vXE4pXwiLym_9reMJ7gTuxtr0gDSpVd5cyT78aCQ-IU13m6PQhXHHTg9q0CawGa2Qma6YClNYpVo0tIOc4ekWXJp-jdNOZqXN1UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGYGfrxKKw1n50dhW7qIKHBxHxTDtxt0THy2bxe8FhDg4grTgzO9itYLE4mato_DHQNZ4vPBaHwDtkc7BMr83vkanFq5rFkuBU8NGHsMOaDUHWQwVSRmRFxZ735KXlnbuauVDa_5qgQdPKysccLMdrpDbcNUaPRMydoOYGGTCHxkjLtJovnHAgyiVe8DJ2WN2tOHaFJTg1JwvysluGeD6QVY08aYdAA0nU7RkmWfSvgNA8g-agsrhzVAArwV0KqGXsJK8EjxpRmGr1eoBpf_ct7lZTcAl6ecnlhP1IgyIQsZKiyO6bIS_5htlf8fPRJljU-MVCNgbiIluAPYevsv0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQHZamorrEifQNghwBMdqlzECL-xBnZwLCdGjisNLi0vZE_hcXFXiROeRExz46io265-NI5D_4PBf_u7NhvkF8Fz9m6QZeSXAjjbnhwOUpkmubgKxB_dsGWylz5FW9aKRLLcXCD5PSGALSIA1TrO63jwMJqtocYjyh-S9eBF8htoJ2UUOhuXOtglAPfO7ejqdKMIqD3dXSbkqRQgh1YtqCr_8e0HapVuvsBU6Cpe3euqsxAAR_pjj6Lc3K_Vj0Xwf_fHN_9mkMlLu_wnNdg9vbpW7Q4rZC-LiWWL5dlwTYTO6QTAQojQuSmMwFqiMhlhyH7DC0ULIeS3Ercnm3rHQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=lA5zV8ODe7ZOtUyfP0287cqKNeRNTGJpD7AlltE0LoEZlCRYymQQPuWBsGtbLhCKTUuBxida81IMWKEn9_dPbJz3Kd9n9x_j2qsxZXLP2nliJitsjYtx3Xf6ToG0EFzFtYTzKpyMwFZigplsSyYcQQXkC_LvkR2i3meHeFT-MzrmDNGpR90q0zzFQ1fDAyY2xV1bJDOzV3l72H4CSAHdULFhqm8stN76Fe1e3uQZarY5Ek46S4BMaUbBj9f-v8uJ8-jkWnq5W_QPkrXwypRzCnTTr9X35Fd8TTGoiQFdpMcv0_xGJiuJofNA37c-Ax7Ps3G6Hxus0CVBfqT_JOqNmKNA6sAtcxVoV6YCLHio1ZBcPyOEbnKlJclHNRjtUTp3O3UVab-gHZL7JBOvnZ2bYB1TWvBKXFD_YTpjHv9FCeuCVmwokFGvuaizxrFtBiaSrDgRJCgTL8Iv9OeVI_jF_3wyORIX0FGAlSIimufVyPlDsEVlR-hlJf_oEPszT_FBzR7Gj-NNSobVsrjmIADSXUfldKJAE87SdkW0KOQAuq4r6RoolxCVCe78ynYe3r6Iq8gj4t_1-QLqjL_EJ5hhneBCb1QHmEFrXStrzPJB4kC9lZICt4cerMHxoRZJcjhhVrh2_vuLsI-Ug90cBUFpeVSkK-gPvHv0MLmIp7BZh6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=lA5zV8ODe7ZOtUyfP0287cqKNeRNTGJpD7AlltE0LoEZlCRYymQQPuWBsGtbLhCKTUuBxida81IMWKEn9_dPbJz3Kd9n9x_j2qsxZXLP2nliJitsjYtx3Xf6ToG0EFzFtYTzKpyMwFZigplsSyYcQQXkC_LvkR2i3meHeFT-MzrmDNGpR90q0zzFQ1fDAyY2xV1bJDOzV3l72H4CSAHdULFhqm8stN76Fe1e3uQZarY5Ek46S4BMaUbBj9f-v8uJ8-jkWnq5W_QPkrXwypRzCnTTr9X35Fd8TTGoiQFdpMcv0_xGJiuJofNA37c-Ax7Ps3G6Hxus0CVBfqT_JOqNmKNA6sAtcxVoV6YCLHio1ZBcPyOEbnKlJclHNRjtUTp3O3UVab-gHZL7JBOvnZ2bYB1TWvBKXFD_YTpjHv9FCeuCVmwokFGvuaizxrFtBiaSrDgRJCgTL8Iv9OeVI_jF_3wyORIX0FGAlSIimufVyPlDsEVlR-hlJf_oEPszT_FBzR7Gj-NNSobVsrjmIADSXUfldKJAE87SdkW0KOQAuq4r6RoolxCVCe78ynYe3r6Iq8gj4t_1-QLqjL_EJ5hhneBCb1QHmEFrXStrzPJB4kC9lZICt4cerMHxoRZJcjhhVrh2_vuLsI-Ug90cBUFpeVSkK-gPvHv0MLmIp7BZh6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADTyyckA_4DTqYdC2um0MHaHKgzRq3NW_5dORhDj1HXDvcKjSJPQD5FNuk4mG22ITB3OqtYCFnLhs128UvIdfSHXnJgRPCNKL580-K714kgCDSVQaY6W3WYUq_28-X1fY4B6ShwVsGdc9MzUBJEc-6zxg8VUr_g8tOTU5aPNrZJANC9gk8b0hcZ4nEYy1jA0GQyYC2hzwv-Ix9-FBCZ2i2Dpr6n7tq9x18cXYi35-Dy4Ag3vSVzv2Y7DOzc2uvNUaahwaDyH6XrzdT3K2IqNQcWGvI9m35Yh2TJhLe1elOY8z_ReiEW7dISVHm1K-jyVnyhIdAfWz_pi2nb2U-uCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNroNZ7HvcR9RwB5jLE-ihW7puY-qxhuaskISQlg3PGEFi_MrTS0MVbYkMEbHCR-oX13gfcksL1rcg7iug45GFzYlRZb_fkVxn0YRkcKGMZTjVvuTODOWXAtolayi-ygjghuurJWgMN_4QndQgLllmj04MCvNXj0cfhJADh-G6WTqUBt0VEF3up-gPdZ3wRzf5t2J1bLIQLMLyoPV4WoxcVVu2xl_Ezx3i-O9aDxv4nJ10euSk7c0mvu87YGktjOsCeies0SYkiYOcfaacb0JLVVdKO50caQ-wkFNE08O55rfY1Yng_uooBi06IDogoPbft41d7896fEqyZ06JPdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg5fE9vn_G7BhtwLAftZSMUh_J4eseywmlzc1ocPPSRiAwjG4J_c1GbPzkv5Xu8ij3AVKksI-pEhetxQgU_OpmXJlqpLQzea-43FdKaqxEz5tN5R30MPW5_lrwxXpSXLOye6Pe2ckM6PL5zrJmdWn8Zk9hG3o3fR1CInQydOT4E3dFVTdgvqStmqGn8yKvRzPl1-VQgl5gHNNn7TgqPbujXZOyNJHMI2s25Huj58uyvUlK2nrkDljt4hsOzA5-ib0B_uA4Toz5OsL50uZL5CIQJAAORICMzlfYRmPFcXdQ5tABcV9XX_ohWHf3TRxQwwCjEr7TgzW-ZcaGvv6ngkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZtfpoUkFkDX_03rEcgas35IMQ9YihzbFj3I13sEP4rg8fCg_GMnyokAOEDXV0zl5e21xS0zPoacYHZDaKvCgIjQoCSVZkfrCDiVSmY1z_R0OmLXGgHlFC9J4fnkG-CemQifnsKNBZZrmgjXtihCmo5uSfFWhFPopJfeqEsfSyec89HMvtUBBuMa4TpDOcPbP8-U5otfr0qIq8X2CQQLIVLl3t6Y-gcQsXIemqD4OH2bO4dXa-WjG2gAWnukaiu3FSN0_h983tXDhdL3LQWW5_pxqHtwdDrfrnltcQKIWK1L5px8jt36zsoAFgjjfHAXF07_M8rOiEEcOIE_MStT5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeEzePv9YJ3z0673tZ_0hJrn5DlhOTuO6laWgx7bnv2ZbzagNYlSt0jdK7JZB_0n4dsfeo6PKNno7szNw6x4oTb7hJPhCwFiXclfFzR5Hhd40UHMnaHGo5KCvrPXCfVXJgOZMHWrVwWz7up8X7g-CcpLtOjVMbcR37fzfDj-In2mQHZXEEbYjhehRpjVf09AZk52p-FcMqu7gjATfl8MZ1lci9tgb0wVyUj1esd7zMXUeKRkXfXUI5evLfhJBwblh_Fk0gzXkeU7wj4gjPCzBdI7fTtYHZvuMnejb-ugC8Svg0bu6k1YrgGsw9-Bj6-OCqvVVK5xSpl40DVgG_Pl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8wQSdV0yvUNgH-qOha2TIu8Qx9j7I5x7OfVn7gIsPOjnP6Bi2J5VeBnb5rJnyrD4cAQb7cuwM5-0tHrWh4y4BS7eXWD7ad3aWbUn5KKEvxSEBqku_p6tsysdOi3lr3fTjjrFPHYzEswKc83VrocD2TbKtKXKof0uW-keP9kBckdXd9oWvqPLLwQ2Ajyl9F0wMtWTA9kjVWgiYTMqQ5LA5TxHOMzsRkuJka5slOQ1GS9BaEve2OKVZ82cTi-7CLqsIjy2CQTlk8_QNSqPha1ECsP9QxSWL59TVnNe_iG4pmBgKgaZ1dZd-7QQrexDkL0kQBxWcIs_rizWe23WAI3ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEy9KaQEQg4DUOrjF_2LH0YsQeP9LJEvppI0gNXHiym-p-wZDQHaTd11tFbsBDADVVOrSg3TcCQsgXAkIKGPU1YdQyahrUBJDs-YvmpC2q9uKZZEE5ELXe0cVNjSCXEcRhpLBepDDA_2u4mAGlRXR3xGKRY64M2qPeIuZ68NKQeUdR-3CqDrOEzVJ_r-PpeHldW_w5CEkVrIGcDeWBmFXcC42lgoyecVu8qKeS4n7Us6UQrpZs4Gd5r2u2LMUfO0cRB4P-esuEJVor4izhgj4vInxTKYXXOz0Sihmtpel7Izj7lYAbkAYqLZOcjGhYXU8bQdN4pr7venmATH7BGNhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=OfiYHnFJG3WloJHGPl_Uz7nPCtUT53meP86s56_ZNWqoBOPEGva7a3ELOJ4uMBxqBrpZUPh99elzBSAyHckHk_W0kMqA2CNgEZPdD8lEd3FkDXhyv0AGvMCUrBN9GTRrV_21jXLe8MImRJtnNno3fhhFtQ3H7JMbrHToFzmuVRjR6kzFgs7XNUjA-QgMI5bzG4F_6dgK_CCZOZFR9xZujjFgT4B6kCEglDuxsDVPLf1fu8Hct5tg-02Np2CXP2jCUPxGRQ8hGYve_SUBzJ4_2sGW_snkdGBNEEFIQZmFbGf38cAkPY3f8LTncKzz4Jlm6TWfUnBh8nzUxzfMZfzXSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=OfiYHnFJG3WloJHGPl_Uz7nPCtUT53meP86s56_ZNWqoBOPEGva7a3ELOJ4uMBxqBrpZUPh99elzBSAyHckHk_W0kMqA2CNgEZPdD8lEd3FkDXhyv0AGvMCUrBN9GTRrV_21jXLe8MImRJtnNno3fhhFtQ3H7JMbrHToFzmuVRjR6kzFgs7XNUjA-QgMI5bzG4F_6dgK_CCZOZFR9xZujjFgT4B6kCEglDuxsDVPLf1fu8Hct5tg-02Np2CXP2jCUPxGRQ8hGYve_SUBzJ4_2sGW_snkdGBNEEFIQZmFbGf38cAkPY3f8LTncKzz4Jlm6TWfUnBh8nzUxzfMZfzXSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j86zMRZp1gXhOVGq4N3bEFPDyuoB5RmnKX_a29nlNL4Zel4Xh685lLqpgO1KDhPefILqW19xbQl4wLUYrF0aelncI3jWqwc_3890vCf6hbnu7nsOWV7fHNAP8kbjpiR8ndiBjrWlPrz6PBtMo0OK_jhO4p2qU2XWK1YAJIsFMF8zVfgRZm_9-0Fl2nRbjuAGVZ6o4WYy3ZhXv1cQFhaz-DrF4Je_6XFb0G0PqFy72pgwFq1nCfhgFptEwk_767rCw476a8-AvarEBYfkHgjzvfXOZdC-2OQ1DdM7Yii7-KMsd28XZ5fSi7AD1K0RUyvl_qfIIzMliKhsjQAFkNIBBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0kKydD47K03kfdLIl6Zmkk00YiN3FWfJRZruELTnknLuYl9qS7MOk4SqMu4mLbuwscYGV-o153OnySzIV7mBYVOVtK1Yhshte84s1u_Rb1BWckMaYZlH_7pNiZEb2vvzXBC1-79x1SsbmMaumn6SQi9A1aiMKsPCqSM5FMknPGjPYGkStqzSwhcJz-Vdm59-hhbOZfp6ecdmvhMebnbrYbFb_ewn-ODQO_SNSRISmXdXYF4xKUCFGiuR8hLKePV1wjivCdcYP0lj3QpZF5UwiuCvGwr_CBGdtBLT5ilw9oBoUrw8VJpu02oSb6M-6LQ4hsHTz-ZHOMgC7bV1m81rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSiqtyCJsoMiVdWl2Zrsh1KeC0lv1u0khtB4Z8Izp6oZRsDCcE518P_APdQBz6gXDqXzVKiLNb_WzoTikqTZVW4S8jPodBFNmlobM26pyCQoRsHzhwhygy7bFOr60vwnRMuY52fBsC1BhcOHtXMlIHJ9PNLHdceDy1K0egHAmn2Zhgpw2dX6cD674b5hCALaTz9eziJxDlkuMnR3qf5ddoL8ZNAMQIMKVZE1Zajk8lZ_uaC-xr3cR8rsVizMNzqjXCXk7k2dEidmRwnkOSlX5mR1CoBLpu4_gnecPvTR_wOjMCBHWaLUNLaJUAodHyqeOh2Gc35ZTyq4FYHPifoPLw.jpg" alt="photo" loading="lazy"/></div>
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
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAdb2OyJxOTtUOEGJxiSPZNJ8wfrUZjgh3kUfZI4zGA0KANt5ZV9PDu5ajw8NKGNv8J_3W0j2LcQ7Rr3olT_iM6mC2uXIAKYzhfwon4l1XZXeKomX7h2qtT02Tz9BnsS4rUy8V50SdczZivHp_lSgLVB0pVi5tMUyNnOorWaXTL9idkzN_7AjJ7YXZ2d2Kt9DgpnqLuKEWEt3RWssDR3t-A_blc2zQQU_R4EpEyE3HN6s2fv8ay_Ka-VObs0GgJgbh25p98b2cCkOS9Y28GYdBjG7sf_oQIF-923LnYWslOcLs6NsJ7tLcMApF3rQUJKCLvG2e9bcatNByNV4yDZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9qD_F4nwEuXE281uTPvgPH4QIe6YMNUJsyBNS3Z9CDKbHiJl2pPyZa5qkQZEuqltIGvU8TyTFzaV3u7xXIXxXD0TxBPcZegB-J5NYFaNr7tO3LA4o69wLTnrCI4MCcojWCqDmRPST3imIMxig7CPixFS3z6dWb06z_LIH59oCiy9R1nht21prE0NspoQqo4Bdo1vqs598BtKu_dya1BFmF0wyy-ugnEHZrCWVMv0EbBWcFWuu7xkXQVGFMjU3nls9j2cLi8o4Ljvr77f05D8kRYrQG-zX0s05LfJIaUza5RXhn0yphw908h32FngMQ8VNSZR_GeLYYld2geuvJitA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjqhBFsrEGx6jnrtN2X92ltRBNcmePPd061qiYqToBZtIo--A9hly06u5303Lzjgk-e7ty5yyBLS509nk5ewPb-dZnFSk7z1IjMbyEYTEf2hXUjDHnEUq-sLaP5jOjXxyl5IqgYfQ45roSKCzgZ25out3QpISQuFv7WxemzweA1xRW8Li-5t-5hZTsj8NSOgaIOJpMs7HYLO8Xc5IzpSEhPtfESccjapBfNtz8RDq0E50kT68Pzw68kKTfWu-TPxGnYnASjvt2jxXqXC15FDoVYEvKIx2qA_Lj-Yecrgplx5mAyRNaFq3yJDYk1d37OlC92rq7Z3CEZxFg-YcFneWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoMljDxfL-lILZCG7y6pxV7CxCEV_S3nuS_FSZEQShINMDW743_6JTvmq4Sop7yJIKGIYPgimVpo4LUhP1BwL4MOTjpMbl08uBkoG0IIOus1nt6rumVc4F7nrOMc8Xx31rwbx0Y2tEStUXDlytwfNJ7Zb--ZAOPlTYZtkrysP4KzSjD7dsxJ51Pn-405_gg9Efbj9V71p8A9RmM9F_P1gfb-4raPOSsB1QeLUJyVdpRktdhhlkZwVWpB6RcInznIlqeYUQ8vR4mg0bFqjL6vBbR1lzSO0IBCMUgkxxJ6wtQKMXbOqWbgWmd3FSeOTU6APNVC9Rp1w3EK1Wk-7BHDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sks4hcX5IjV00Id1_2Sr5oyHFPYda0tQUhV75VGhjmMsJxvboMD9ULkDRITobimADjJb9Yd19T5xzfXdjuTpz8GTePy57JLvAPIrjEgdtBFbF0_ovKrwaljd3-W4U2SMj7R6PBNeaccLLFMBvUHclNaCIq6t3wtLa6opjJQOeJOchd41Zu32R07bfcZ8aCAcEh4ew82owKwMvMAqNEcV7PgkkYTJBRZgXam5i4-RJeHIHq1SzCWuinv_9xdFEQMEgixus48Yg9Ssvr4JqAOpCKM2v08dHC4l4ljjq3ykFleYyYVpbU3X69BIHzTqyYQ9LULj6lqYhWMmFqRnmwWMwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
