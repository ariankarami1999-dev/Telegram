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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY8zYupJdxq920eK5pAGv2UzQ6i5m2AupMOUDLS3AgB8ROHRxtCjY_EWjzLT6rFlLfDc3o6GD0Eyf-glUANN4b3EA8-_wVva3d4pb9TuIQpNkjqJfHyclw3NXLlPx0kiLIhmN0JO89dN6PvghfzvcpaST3NLnE5UgT4JDCiwICt07y3hLL8IEZ1S7LDi-pxRl1OqoHCgpb85e_4LqWh91cTjVVJrC4O34UTyQlQPp2VAbznJjiI6oFPYLgoHSstUfEGVfNZIp0sk5s5CvsXzBhCbq5566QoUBTD61mbKhrfKlHpuIT0fOGFGbEDtQg9-6WFOuQQuCAj9lrN3S-30Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 495 · <a href="https://t.me/archivetell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=cuBklSUfd9gedgYT2Ck9o1_FLRKFFFNvdJ3eylOK0Nd8v8IvxQK0PW6gJ9Q2L-MwTD41NOY5JoIIfayuhcvJsvrThXzd9NYZjP6RHjOQGI61RvXl2hC0LHNpxLjUpAv90hUgnk5dCry_JkEcaBAkSvrvvXDH9CC0Zi2uppKzczY4pKo-711ZEaizDYN8GQTdaJPH8FpJJxpps3BWsZ7f0Rg-ChoCGfS1KQoqlRlNehFf380IwcsR0jOR1q10Ml1hew9Yv--DOWhCH8H3XqSda68Hmar0EUzka_IvTjrOE2S4OLGpqY_f17OjjD7hnOOsGQcx9P__ryMI_H-OUO35iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=cuBklSUfd9gedgYT2Ck9o1_FLRKFFFNvdJ3eylOK0Nd8v8IvxQK0PW6gJ9Q2L-MwTD41NOY5JoIIfayuhcvJsvrThXzd9NYZjP6RHjOQGI61RvXl2hC0LHNpxLjUpAv90hUgnk5dCry_JkEcaBAkSvrvvXDH9CC0Zi2uppKzczY4pKo-711ZEaizDYN8GQTdaJPH8FpJJxpps3BWsZ7f0Rg-ChoCGfS1KQoqlRlNehFf380IwcsR0jOR1q10Ml1hew9Yv--DOWhCH8H3XqSda68Hmar0EUzka_IvTjrOE2S4OLGpqY_f17OjjD7hnOOsGQcx9P__ryMI_H-OUO35iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/archivetell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/archivetell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 946 · <a href="https://t.me/archivetell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/archivetell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhQckX4JN9gTYq27cydCUcLlNVQJFrFMRHI6uxnEG7rsRnsuU0Of8bohzwAYesGjJwfnI8ZaUiXPEJW2dPYTjm4r3eEDeQZqyTCwISE6zbwQ7IHSsz68ikzwx-XR6YY2YVRQFpRxkCySTxaalhllErBrA6gUvmf4jdXN11da1tdDGy1OxlHdmScV9E_IRXAzc-PZnW1yCxNO-iZ70CkDxZ9bj3lKD27BY74T7KsH4OWxgds07uodL9txTi6r181fLx33Kl5zzMVsoft7OlawYYfNIAVuYL_9Z13a44IhUYRx-Uvwauob5cIsVQS2KkkYPKn3eowXwLNf3qWWyrasVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmcZVXA7p_3e5sGZD3gGfcdPbabpAd82rrU45fJFX-xch4D62Cs1mhnZAxlPzD_VESsyFLtWGrKcdKYIy_yaTxoOOqqh0VGv_oAfcTkFwioaDCJ_bQ5W2DC5JJqRioGOZBp3CnhtPgSN3NhkzuvTOLIojQABBtfVD8XwCyAdnoW-4gtorRhgox3yI3Xq9cBJmOthAK_95zYDet7K0IUpp_-CnN13wcComU0pYU1PUFM-GSaz6YG4sj93jrXWpawMxSJbVuSeXvP8XQ5nInXyjHsFU-cvpTdhXW_RgT4v1AmeYAUbDGDF99uBrEpesK3ZNiKabGSJXIN7EkxPAHrS_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgTKsFiFd2eQ9RdlHltVT0bQPW8xVgWwQICp84C_mtXQcQFTKZgpMVlHUX6dAxZJqwGMQl41hIjCscUh0bcOPirpM6ZOBPoaUR0tN-uaPapuGu3TQo-t4jdqfNmwD8kvd0OU88hQfqK6zXqrVV3_sIt2hQbqeCDw3lUWsPdi_kXc4DGtH2vQFJx2ufjlYUrl1_vBysHyCTgnPAYOVX_6ez0VjyZhP18lXcKs46VmpoiTBwXw3MWzwjaxeCz-Z5ba4y-JnuOMs6bnKF9AvxmpMgT3kV2tWihG3ofbPC49Cv8yxk-2J6h68Ms-44MIhA4a5BTS-P94m5Lu-E8KFREhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnmr3hhGQrmjUTI1g5Vh8eXrCxUujlehUROfjK_R3vdmK9_IZJrsDBHLS2FjG9Ix3900jc0Wp8Asd3v573-Y1Kws5_mXcCvCfQ_uYzAGu7BXIDzsd1GUFik_nrtVECLktM_ZHhtwcDR-NZs4Jiir5NPrAH30pT3oEdeR7wCwzf5tmHhLFJdukmSXt3vWAlDIk6KX_iBb2jyJcZiKa5nPdY68XH6XLwxc7zJ5Mh5DyTml1Ahb4CmMO4GXLhFkoMkMMIwE8odSIskOGU11bO1PN5MxhOxpE_-eS_XnMazya7SMaYKBU9vSKuiW8TJVhSkbK4UWfsr9CSPosVSQ5IusaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REN02-W5DVZl2Xjy5punB_bN9ldyNCDqAoDembOd7yelklbnMxIHD-n8_pwCeqi1ZTW0Zw9EHjS15BqdxQPBmrbGHzfw4EaOdoJB1NFvRr_Zz0Yz3ztB9XtT7nbone6Uy-0Ksv7G4XaGFH7EsEj5qWycWT_gQqtDbEqTn0qnlF3hR5b3MaWefZFeNgWk5vCwhoc-pex4yx216dlhAJU3N3GPGKdPA5J2_ipthAGrXO1IdlY-69Li0MWj0KBw6d7A67ZEia0_iSQ1bY6QjPFOJlSwLpsnirm4d46oeP0-zL482fiA0v4iBSE3txWoTOEWACkge4QOffr1A9-LOBL-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_K1e-oXAAtdeGl0On26e12JFiCgDUruWhwH1zvUqjGj73kU8xD-NAEk1WEt4Ku_v1oGsMUiHJk-qzNQ26T6z26BMVATS0dMSJGmetwPwZ1QOSBIxpCBqAdSPxcKHthDtxNyIWZXrtIZo13mbj_I2ZtjCJJtdBPEUh_Wbh3dR8fdMl-IZHFP7obQ_IPG1OGK1Qv0sO5BUMplgdEIc8Jtj1qiSbhS_xIGGR3UScsCTYTmqzqlT0W4IZ7hUuEMEoW7NVnAmJG_biuF6HNWLK-PACCkQ2GZkpv7-P9f9X88_UMXFjfrerJxthJrIyLHnHtR1Fk7QyuZCwgTIXLhNwa7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wrqt5jZKhTEw8chzKwiLkP5SCBpGRkPf3ydYp_BZiEQ_dZXI2ZvoSja4uUQ2cPM3PSAve1MXoe5TotNKXQEiwQmRAAQfriw0xk7p1rq-FrDnGHeULSX-2fClchPpDEIPBpMncVzIPwFkqpKgr6FC-rcCFFpMNctY_P-O7OSUUlX1GBVVqUrkNZN1KQawU2EFJtz0jIhfjgUhG2fFJhKQI_zRmgX7PDmYFx4LFY9ZnvANAd9UEZ9i-vDYX_aUaJZQE0k1i_pFr-tAfDPYJbMlBEGyE_4okAfp1PWd4usDFpWSQY5JgpaGtvQ5SK3C8CHkFfxd1gm0Ml54mPEKAj-xRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPlzUHpHRA6YRxd1955J0B0E0rwPS_PzAjieSrzCgzSDkWIpU1xw-gMVMAOsIYzvnW6RvXmNtIO526jJ7u8cETwphEQnHHnjaXce8MWVCyP__rbWE2rjat2mI0vB3rpL_pDPB8EnLGDWvCUvp3QceTGZap8bxQhtsV2YRuYo415ir9aAk_DDOj6l1ZZhZ1htbA_4hiuKRVAMDuKqDQoUZ8GF4rXn5FES8UsnDNQAjFOPqz5RSfOi_zPYid_ViBwTd4N4Vtl-UUDPcLZpWKbvCXZERJUUqqUAHZFWh-bOQDXa4-ROXgHTCmJYe_NcNn-72mJaffNGu4QRZR4s_K9TfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=Cv_xzag93Fj_JnAasppsm-snkWENBikkuGI638azxUt456v5P6PqauMaRUxPKpK6fLgDf7iI5MvpZeH7EY29OZmSbR5qWqjAFPYLaMi_oh-1Ypbw2eDfAyptHMUg4u3GhTg-uF2SYQOk2BDgiDh5Ozo-oWn6xN2DQvHOM7Jm4rhRTdk5HFF0h60yBpKZ2iGTOoalRCMx_aTTij2sBsoXyVlWJiccqYTTbvViCFuVF_bANuAUKKCUO3i4J7xHulQlZODml4xUx6kAKDQRC4yY0FGf5nmrme0f9B9QaY9DxPZio7Hr8VHo5shLEv_UW1wXSVeDAYqG1ss47LAjkI5p4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=Cv_xzag93Fj_JnAasppsm-snkWENBikkuGI638azxUt456v5P6PqauMaRUxPKpK6fLgDf7iI5MvpZeH7EY29OZmSbR5qWqjAFPYLaMi_oh-1Ypbw2eDfAyptHMUg4u3GhTg-uF2SYQOk2BDgiDh5Ozo-oWn6xN2DQvHOM7Jm4rhRTdk5HFF0h60yBpKZ2iGTOoalRCMx_aTTij2sBsoXyVlWJiccqYTTbvViCFuVF_bANuAUKKCUO3i4J7xHulQlZODml4xUx6kAKDQRC4yY0FGf5nmrme0f9B9QaY9DxPZio7Hr8VHo5shLEv_UW1wXSVeDAYqG1ss47LAjkI5p4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddA-9Bbtq3NcZDwVEyZkOyi2WaMQAU7jpOwNgJxoE1ISYarxmn42Teb_-Sy-zGMco9ONwUGZGwCjhC6QTd4Iqu67CNYhZM2xceaEef0x0I_voYFcczgzkrh1uIlYTEZvPK9C_03zCyhfspilTMK9VNx_bYHwEMZ_mqLaRV6b0EmWMDorMQ9B4lUuk4kL9yxVPK28Jh09IFYZrtyAFrQ78u1SPEHsIv7sj7eaf-58Ah5S7tkZiyXdkZF45B0CrD0bhF6zDGbjU4D55pJlIADhYlen83_ueSX3pUW171qatUyAFCpQHrDNPTnROHHdIT5zWx98WilKUvqYzdbYP7PKfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiX9z2h1zZ15rneD4hY5uR7zffdfXHYbXauHMMnV3lh7ZYpxoO2LlD7Q50rz6wGxp-OsLh2yJdNNpCE2I4lEi10e_CCITtpJZ-EITfkL73edJp72FCNWgp3C5MO6ft7d8aR8p1dCaVJKj2euTQIPQVLZkuwR1bYMb1zs7hjZ_QZkcPKwyUjsuByMvoCyBGxAglrB0Uq9I5Vcxe9IRYdsBgdjB5oBKQ6H9DeWW7QJdOWtH1nV3zItYZHXxaboKyXRtqdvkDSiRfiW1NtG_4VHHp-9ilWSQoe0D1Zu7NYsbziKq8raaaWDxENBLK8y-A6Ccv7k5UENC7XWiY8zUye00Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgnSpat8cQLS0OJSsZu0CLETTS-W6uoby0WIlal06jty4mmVjhVbWuuPImMg9rs5V59PVL7zbo8xb_1tGMJfvUhyYmfiRZtaA25LF4alQS2acN6RF9KMAy8aazSF-tHX0QNtTUF5nSVIZANYog9PbhfMtGdUrgjehqHNOSMgMrA5tLfEHD6mabJaExRCSYf8k3bsOh-2IIKn5Fk7p7L9VYM3uso1WSqvwQPzbeoYqKt-jYfnzKawS0TF7dW0uuyQu1s6scLx_M3ErXBPaQ2FkbNCzzZJ90u1kdNBH3WDbbgMCdZkPC_He4SGP23skieL29hgB6Zw9jd8fq1JuuWwow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k48kGxH9R3Mj7KFAiy5kITaUa3k7HHXuePKBajp2B8Ioq6QfoL_VOtUBZSWWvSn-sarAVmodXSQxdxTkbamehDzMZcdMvJSU_dNrpRm2G5HBnLPlze8AkLoSQjIYUbExIHo864fNxzqtqLtEmxOCb4zkAgjJuGv9LEqA9OXIFIJkohhliJfR0e6hQHlO1ZSJTrBVojOGfCJ_FWZoT0xjF-ps5s_q3HuEhq8Vns6Qahm3HN7KKP8Qa5ZpyzULM_YpI_4Ju6fQ84S22HtbnD9bs2wS1t-AJAEe0Y9NFBOYOpTdgtOgV_Yu0YEAFpb9KLBLkUFS23fgiaqBKZ5Y15khOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=hiH0T5Eg07oROLnVrVc0YB7hZYvCVb6d4Suz5e2pFD9q41YosxN3TlgW6bkHTY-slN2dkDWdXSQnSGUikXgPk3ABGJc6nrZ8E7eyvrGx1nmAY9baZm4kCdp0wo5cBCoxPsSGDDsQBjzo6wPM2FNMsXd5YI4e6oWiLKjKYSV0iHB-p2pQ4UpWC9dPNG-jNWWQaLofGr1m0jhpzpWOBLyS0t2k7tJ4OivQFpCmaEgsWz5LVcU0sAXR7SsbskoTUqZDtt9VgaSkphpGoXJ6_lSERgpAfekv8JcBH2HLTmtc8ZV3J--GIseYL8LPHWem4M2AfCoHVNbOwLM99PVwgNVq7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=hiH0T5Eg07oROLnVrVc0YB7hZYvCVb6d4Suz5e2pFD9q41YosxN3TlgW6bkHTY-slN2dkDWdXSQnSGUikXgPk3ABGJc6nrZ8E7eyvrGx1nmAY9baZm4kCdp0wo5cBCoxPsSGDDsQBjzo6wPM2FNMsXd5YI4e6oWiLKjKYSV0iHB-p2pQ4UpWC9dPNG-jNWWQaLofGr1m0jhpzpWOBLyS0t2k7tJ4OivQFpCmaEgsWz5LVcU0sAXR7SsbskoTUqZDtt9VgaSkphpGoXJ6_lSERgpAfekv8JcBH2HLTmtc8ZV3J--GIseYL8LPHWem4M2AfCoHVNbOwLM99PVwgNVq7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Ze9t6pna7bTEYhQDdGJ1jeeCEDHUoVX8lDbGJVSTTlsbq6Yc1I07DdO-O3iyOrCg1GZKKHq7Jebzr1CDIqFe0e1LVFbir-fvtUzEMBns-eRzBcLH-QFdUPOqLrsFvcNxiWPDBTT7s0fjCCWsSC4fosiSxsR_dSNFc0ONggkt_lF5lhf6JszmS3JVoqn_q7p8asaMg5MIUfpEz61toTljv0nwHA8P-Kxr2509HjaQIcTTLx7HB4m4yi3vF2gbZRbixP1HIHWcjwhy1-hDVVBdegjNv6fKZI03M2vKrSfG7mYDx3LMBs8bmlSL_25lRXrPVNflNGBJ84mFXq2V0QB6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Ze9t6pna7bTEYhQDdGJ1jeeCEDHUoVX8lDbGJVSTTlsbq6Yc1I07DdO-O3iyOrCg1GZKKHq7Jebzr1CDIqFe0e1LVFbir-fvtUzEMBns-eRzBcLH-QFdUPOqLrsFvcNxiWPDBTT7s0fjCCWsSC4fosiSxsR_dSNFc0ONggkt_lF5lhf6JszmS3JVoqn_q7p8asaMg5MIUfpEz61toTljv0nwHA8P-Kxr2509HjaQIcTTLx7HB4m4yi3vF2gbZRbixP1HIHWcjwhy1-hDVVBdegjNv6fKZI03M2vKrSfG7mYDx3LMBs8bmlSL_25lRXrPVNflNGBJ84mFXq2V0QB6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znq-x-n589d5IbcOBTNvE4rkd-f8LlPgQEJW5kzBcCDpmqBBnAQq4qVF9-MYJIrCI3J7et5plTsO4EKKfHUvheEePFBd16AOwsXFDpR56fvGiDNIi9eMUrPN_TnEoybx1j0OotE0GJwysQqmLw6ScMvj3jmwwj_YkRw0LVHl0qtTmRxJSfJ9CiKnpI08o5lzfV0CyyLvCI2KKxPlDsNelEm2ABM1-cNYdvJuX7t_CI5i9FrVuWdp5dg_6mwrAxzCXZuVTsTFpDPOIMAXxXsdGEx1A1JQWU10k2_y2_42qu9rxPJ7vDWV2uqjCzLPLqSQ7_K3kpv-pFWactasbpYOCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=tlRrTlWMnJRmFyiM1qu9AIfxaQ-8eB4m32QPp2IxCk-jHxSnlqdACpo-RRuGqqv4pPkUZcwr7zozqAOx0tlh8I_h7Qz-RrHOX0xoXHCiMcvbcK2OsRIgwRROrYWG_e2Qcis7BQfHZLesFh0ZIT4iS_OtMsP6tlAq2v4fmv5w5mLIipqFBOa0zwiR7WjpJXT4VO2X04galMlI3Ne4Tr1Y2J6KHC46_91ypj5f-a9W-m6ox_Fsvxs3PcNsEwhWkmPybL5M4LzRjfVU-SvWqlnYRXC2tAFvZNZOnSC4tT7JerK1Vv11ylcbUOZJyF9-A3HqKweqUDCvRHnMvZ2MPw0sPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=tlRrTlWMnJRmFyiM1qu9AIfxaQ-8eB4m32QPp2IxCk-jHxSnlqdACpo-RRuGqqv4pPkUZcwr7zozqAOx0tlh8I_h7Qz-RrHOX0xoXHCiMcvbcK2OsRIgwRROrYWG_e2Qcis7BQfHZLesFh0ZIT4iS_OtMsP6tlAq2v4fmv5w5mLIipqFBOa0zwiR7WjpJXT4VO2X04galMlI3Ne4Tr1Y2J6KHC46_91ypj5f-a9W-m6ox_Fsvxs3PcNsEwhWkmPybL5M4LzRjfVU-SvWqlnYRXC2tAFvZNZOnSC4tT7JerK1Vv11ylcbUOZJyF9-A3HqKweqUDCvRHnMvZ2MPw0sPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGWLuzna9GgK4XQsvysBYCnruyya0L9N6iQ95UWFv3VkodHjXBZrReGvbpU-_ZModxuFE2wyiXdV2bODBWxBbmJExCA6fBKqG_KwicTgxk0w9CE3I14F2xBioiyJqAmk3XxyswIfUf5rSKrYaU0MPT1eLkyzU_C6FH1pzB6jgE3v9lUagMfS7J2YEDOgxZHbR4WHnNfxcTtBcZ7wyxcl2V9CsJVWHIO10VyIHEK_bkyR1BTt5K3Cqsk6hvX50aaHaylzbyYCldWUQyNl1SluYt_zBja353JLuNQ_6cjt7rWJIrF-K1E73pu8sIwjOUb-_b1Tekw-RBmo3XcEZFYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXdg0Wdyc6PbaEjBdRFN7ZrwdT00xhH25vDPhUrTN9uDbSNkLaWuXAlRM7Cg5PexHpZUk439FmEgBLEgFHZpYiOhPK9wZEQGCjBtK6dDDl-l0YSyJGxxgHxLK6PXJ4y-kfbkM7d6M7d6se1PclVn5ys8HR5O0VtBQo-HRyeQoZ01sWsMcaqsOjO5URkK7spHt9Ppn_ghvraRHcjNqr5Ti4ZlZFUo1jt6P5k8zrESpY0JA7YSkybCrETReQLbSdxBcE2mQ30fsIaX6ZF5NyHtCQxLqA_YzQZRF23omYrm73ADMmnEieUjT6xt88fJtSnMnd54C19Vr1eUD-RU1Dr_7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG31MDwMsxtBMmHhmpdxpT8S_QE5RxIIzeE9-urp9onV4GVP_lxmjB1VVLSOLddO2UHFG3Fv60hgUCmFbIYsncrbS_VJ75MxPdYov5Roujhd--onJjpA8Fvjya8VWrzBoTDCrnK-2lQMsIU6HueirPU9RxdHcb6H7XXGLmNcffx3uS6kzykiUzJyPqP0sc8TsF0z9zIRnZNIG81HovyxJrpNiHnOH1eNxYWWGDS6JvxIwR8i2d7oFe3Xk4ysuV5Ch2pKhsbyIskPBjhbqj5nLmF7Rh-u-eZzLUdmdJHvFmdJTezbX1mRZNST71wrdLGLf2JQvWGo5ShcuRK08YgoBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_-5wdKFpVBZU0LLkTiOJWjiCWmZgQHwNKLBgAE2i8HnA5-6coJxtnc8U6JK3uEjubqLUz_W_6xNCsi-Enb_AdGyYoeig05aLTbmbGYC--lRsJXQi0FwnxgQGVvztLrEjvObHn8v8gm_RTjt8nY5Vc58z5jsD72VWBz9B2KvreV3TRY53t0cQgSetumV4J8DZmEmBeiu51TY76YF6yumX32Z24CmmNO2pxEnlXIlf9Qqpjkbi_DTAooMHu5vCcoyHLgV4R3DiUL-uzjT_8t5hhJtLU5fVzhkc9P80ws1dFbAe0ihTTkH4K2JaZ7Q0FbP55Ktv4YquE1Bd3WNLqB4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=JBb8Fa2zYTNA47VeXbYnH1B7Ff2S2dWRCAcOCVb8MUC8TMpcDVyXfdf3nonQmEIJOUYM6TRvvwkCDLHIwdwuGrKdOYH6_mxOKnJ-lfLnNXwO57xIuwX0AH5CE74P-_VKo55rpX-u5I9ePhte7RnmVLAGtokjR1Q0b7wMIAS0w7lVaDu5hD0w3_eWiyEJeTLdpstgb6PA0t2izq-jS2oFj_DW99v9O-l64iW9zrPWDI44cpyGvqB_pRFazesuAieyJMpt9LHjnraUFBW63dQju4NOcRfRLmwAhvMKM-i_uXlg1KTigXufY9PskhbzGFQfhbWXIVCwaOec4MK2G6hpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=JBb8Fa2zYTNA47VeXbYnH1B7Ff2S2dWRCAcOCVb8MUC8TMpcDVyXfdf3nonQmEIJOUYM6TRvvwkCDLHIwdwuGrKdOYH6_mxOKnJ-lfLnNXwO57xIuwX0AH5CE74P-_VKo55rpX-u5I9ePhte7RnmVLAGtokjR1Q0b7wMIAS0w7lVaDu5hD0w3_eWiyEJeTLdpstgb6PA0t2izq-jS2oFj_DW99v9O-l64iW9zrPWDI44cpyGvqB_pRFazesuAieyJMpt9LHjnraUFBW63dQju4NOcRfRLmwAhvMKM-i_uXlg1KTigXufY9PskhbzGFQfhbWXIVCwaOec4MK2G6hpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Euvflq45OMLRx8iGaXXA3YrlL_RkUDG6a-qliN1s_UtT7lsSOWAsDqH0PrzAoLy-3ByWjDUwwobVZIdHzr0yhndJOLbPdIKK8VpE8_TaARNn5SFUEIn90nvszuBczJbqhT_fqTTQ_6Imo5VenyBdEWplonyluDTPkeMw25oMTflNgWcs8Mb3Im0eplqVPR0Rj8R8v-Cx4yI55NvF9_b77lw2bmZbErLGq2foMT8e0t3Nmd8liI2Ox6XEVdRapjtJnedIngf5BI4huSGqQlwLx-pib58fjQoPNyfbg4eEizCqfo72kGLJUTkP_DPCAHrO7YhiHh-YbivoCk2kwuxp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr73Z0O5TyznnMgTObntFbPRFYRlaGnmOMYx6arjIzfl6rrtl5ZR3-n6qIg8K3v694-6z0i6FGJ8ITyeJSG79tf91cPEORXyuQ7hFoC26-AcMjEimw-VN3nshIqfL0zlt_G-ys3ONI-Y-rJZmbgU5N9bVO_WPGaa2TH0DEeT84ZD7cQm0ZoY40z918Op2KYwbyBqINPqqKHPY96D2CZchzinXHWknod15q8NZFj26HEXJapOVmR4yFsTPZSnGgCiClQgqPAE-F8-i16ARz1fDEapGWF2jHPar0o8-05QFCACnjuDmh6WEW16_OChhUgw59_ocEUKSGJAjooXMKfEMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1IEs_2LU2lvIB-4W7Ey5JJple67bfsw3c6U_hPxpoXT14zy7n5nDogtj3CSEZQyEz7j-V-nFSnRZorZx58Ijp6z5MDEq-TfaofqbOkAhbrsoh297n94WnWraU3oeuOaWv8Z4VNTabe6B9rDRIGG71w3wzBXMBIv8maUf0Y-a-SEsjpz_l8iDyjEcC6uuLfVRjVb2jiSf7iqWZ5mA4v_FKYzJRbrkub_jQcIMksgQguITuIo2L6UhKCGEej28uPgfE1cD2EVhZHEnaPXAFblmCIifGG5erT62XxUXeyPSRoUkj6kGs6o25JSqt65r9jRBD6bKZ3uaF5JTqrXDfpMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clgxHbA4PtkKT8-UwwBFVlK4IT4IP6PiCoo4nxrZxYy40KdTqCcwJM3z3hulkxT6884hcvEeH9tBNJil2nE2xu7GktVb4ExCgfvZ3c5v3BFM89VNur_el7za6Pr3LdP1aKyUUMwPeiWzMUeiEBIOrExdRHTrSH8pR6P2AhiFLEV4mahef3Wi0TpM7ddcCKcgX8A3L6DK8RjfAtwCkdIMtN9XxzJnCCd0pP5HZ411um4Vnmo-C2F14_AkYA5xGEk0MYQGedUkTFQZ7JSL6PAx9qxvziyLHqa6qEjf8sp3efaR7aR2TRlhRPee9xIdWKdfPg548suth_4gn8cHR4TcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuRNnTJiN1Li4nq_UI1aiCrUSqJ6jCGG1l8_cx9UoWFmYsFwIFdK6i5CfMd4Iqp6aunPjV7iLTnLy1C-MMChpJhEzD9hA00rk2W5wK7o0j5GW_Z38Bu2Z2XEBV_3eo8vrd6mD2--Z39qPWiKXdWaQrU807n3rNktYuUnHVVS4_UMbSjpSTQhZIZL0oFSOQ5nD21c_zX1dSOmo-mzp2CKhKGRqKlOJI5rnbowsvAPLg5fq7Iek1gMpdYS508ZbFRAMqQC8ie8og0wEzOg_N010XMNN0YXMoXaVEooF-QYfeLh_Y1EApulVkZnjwU3ssYcZpB09pafgHsJ1i7gNn4TLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKq8SUf_q1vMdj1p4WWqyQebX4aeXG2ww_qrEv0wKfqMPEYZbpyDdNlvO7ly_iwnsR-tJGFdbzEufuEDBtlS7Fjxiy347eO2skbC27jHI36NoeD-gc6kYsQdgpIdM1N7jotCABPwF0S8kxTsq9qcHHMZBAlgUJkY2v78oXXz4FN96r4iBDMbBtEg3leZoQEHrQMlhGquGKulMECIda_8TNiiwjtsprI8RNC9gDwwy5aDO6ndpzha3PwfEIq9vm5xrPmojKMddrpfU1tX1GDXdeOAY2FszjvefxgOxJ8IDPPQZwaOj0jyT6RP21lIGU3HPc750eBX9RcRNHw3c1OdOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEG21Ldj-87If-pH8dCRJysb03GoAnclhODq72jHL0zyUkTr_UDjEeTje-Td_Y11m1RudSkpxd7Qd9efOoio5i3SjWtJobSqaGGthBEhfHJQ-8YEs3Gon580is7qHsuCTDsd7UvIyfQSPDPRCLTNYnO9H5ngoMbH6VEN2MlM8thpJUsQ_Y13XmyJ30j17FQniwMo0leWZi-Heg_PvbgxBpT8iIjWwed_4_CAviF7obHmZFyOCwxW0we9cdW7BNLfmPOmozeFqSnOAl-fx3rTXCDIiVciEAUWFsnweaXFAMp2JYniMxE0A-c1Va6c8si6wa6BkB0h-QJ42BsgyyKzxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=W7trzGUH1FlT-1TsMBxVRFQeZtbWmOGGwj7hddRYeXD8AH9MFdZE1uxEiCrK9Ts5L4lom7eNkcioq6kozWaE3_BqD_Rexqw-I_kn8CEDA6P4FHH-Exsagae11IxBEBr6T-u_pKo87kH4xjyOII6biGhs5qExk9RX2_PPVeK8mQpogh5f1TdaE1-tN0M2eJNsYNnoV23xEabI4alHz4lybE2L3xUuLMU3BPF646Zj1okdDEHGGP5bGbbbKlehdLubP1SJbCTDx4cXGlRlWefvfplW0n52HL6ETv56eU_9CdkTQAi7b-NfUoflYS0HB1F77WLTKI5_iYTMbLOQqewHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=W7trzGUH1FlT-1TsMBxVRFQeZtbWmOGGwj7hddRYeXD8AH9MFdZE1uxEiCrK9Ts5L4lom7eNkcioq6kozWaE3_BqD_Rexqw-I_kn8CEDA6P4FHH-Exsagae11IxBEBr6T-u_pKo87kH4xjyOII6biGhs5qExk9RX2_PPVeK8mQpogh5f1TdaE1-tN0M2eJNsYNnoV23xEabI4alHz4lybE2L3xUuLMU3BPF646Zj1okdDEHGGP5bGbbbKlehdLubP1SJbCTDx4cXGlRlWefvfplW0n52HL6ETv56eU_9CdkTQAi7b-NfUoflYS0HB1F77WLTKI5_iYTMbLOQqewHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dshJhHQ09q-uQCof63Bu46V4qs4sKUHaRfb2ky-ggFKgoz8CoSq_WZHM8EXO0g0636FOjsOGZmd_GCepxLvnN7kT4faZxbNhZbACYkTTvw_rtevXaX1OLn80WL-VEr6GJi9Jh8puN3U9EyqjgVx07xsxJNAEgSowQgBbQustyFpB7PN9xbRhuGKtGAmghSahFRlae4lB-Z765ptQbcaMsed-0a2qpncWLR9cEzthQqNY9F59b5t3hYZh9wyuW8PttpuIxgy_dqvh95h16T84K9pUOlfSeNr7yXsI4qbbaRKNTeOSvV8kqMSvX7YN-4nl_MVO_eOcbGEGLo16xaNMsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiB2d5FAibHGrGLihVNOxDFCEst5jzrhoVUhq0gBEy0vnG4CaY7L_ykavBTDNvi1uJtp7LqSfigmKUBGEsbMTB6PwHCXvmeBg6RtEeiH495dbk-WvnbI3offynYlFBYY7_8D6U5LoP6WCPvINNxVtO_5H7roCAmzLq_Jl8nDYvTJfFlDrzvU09LCatkefGZaQJWN3EBWWpkqGq2zHk3smvlZXbanN0e4VGq3PfbyksDV7Rc3RXWDUT-QAABtXl8HDxWj3y5BmIjB0RRN8GbnJdrKC-opfK6JVKAHG94Nqq-Y4w2GwBF5Qw0PvHSznQ9a05Q_vbY5bzeZBh03qMzt4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDl7EIePxGcfxYTYsGHrDF46ZLRdScmqDyeMg2CUQ5B8AJH7tpU-1npf9R91u2QGxpMp2ltwuGdNzfqkhVE4h0KpA9_hErOP0hJkAy6vRcE6VdGoVou_g9gX_xrfzcQHXIUBpg1vav23wDxCpq_L7ROgDdddvwKeSp3nLkddPcan4JbEY2_uUVL1Np_hHAY1-mQYb9oqYR8pezBYqnwCj6wdLnwWTO1m6VY8cTvETvvUYUItl9bL0DKxZTO645DYFUPzudZpZ8OLw2ya6D2H0f-VUgq_N-q-pZsMV06PIYVheuEzGOttrcirjQealhOOkKdsOZbpkbuz8PzAj7BGkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4BDXDO8GXtTosjlaaYnoXgEM_r31GHdtAhh0Nk6URdcg3bcz5wEAVa6SgycM_rKTHq_kjEffeJnUidlr69QVJQUJp5E_QhTlLS2BbDDzfU3SWuLyzV1vz476pkxKhsIjmdIU_Wjy5JI_88rSOTAZ_xWPjkZicxZUjE3HHbK6fvJ34LDs1lLH8IM4LNjbbiWpvzjUZTCEueKQaj8cx93o6PxREiIKnLRdfcZVLsq3guPDqXoc0ZJuxI_UsCiN1Rh96taULjhbJiA6jiydvV1e2_opaHDKRPzZ-NnZaRCfviLh7qIaRxThvB7y8NHYYRADK3R7dOErcfTkmg9QMZDLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmxICIEofTxDBNq0ku1z7nj35TRhCOO5U2W2ktu2-5qKmFgCAX8ERfM8D-X5asvurcQkGzJU3zWXxdhoX1RR3IdLCjqCm0URLe3Wo5tl509QROHOFZwChcQzJI4yU08lvg3GxSEt4pVVn1awBqzgzCIptOB834EoGM17mRtcrOHX9BbxWZ8U1ikNYHvGYoRpaWYde6UTGtCifOC_A2YnyIjw5RWsdAM-tjgpC34w3zadys71ujZBgBhBiJjUjfcu3_500xq9p8gXEjygXHRGzIpFlhEpNr9TFM68z8grAgXxd-RGMAOC3P4Q6_hggiFkOePUSwLxzZe0ByJph0Vy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny5K5x1ItmoqqXdw8diaX8T-5Xdg69apD2PxTsgPkYlEzbf9tDW8XnVyeeHZPAYXM7M9abrHyHsuQ8W9rlOsNu7ltol4cn4f464q-vSRLapjDkLDo6Uq_3dY7V5zUuA-lZGa6TfqfO7vUpxCilyglpN08LFyLXMFGcfyjRbwP1tQdup1YJb5O-PeMZqqyvju7wEw2q_LKtMyMCUaEqfgIz6KDmgoUNZgSPZYADT7AfBVAYrcqtWl9yJZjLAqzf2zIcTQlXeKIwm1qEMreoY2YmrxwbxMzADn9Xu_qa8C0Ol6McAXH3Ckn5ChYiqrxiJg3e_Ut5FheEFlt6a6uf8NMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QE9gpSADKV64hgPa0Y74HfVwKI2IIAnpIAYoNWrC2w3q6mrXganKWSaLwWUDAvovfYTkVL2xcn_25dYKBKVVSYakc78qJug_ypumrGnFXCpqLm5zeDdYfUkXN3yFRWXFxnB9tLYPcLFmlWdv4kHIAydsjkYztJ9nMoHdCVz0i58odSZ9D2JX0nMgFOgu2FeGBCnFFpeBQeT4r9QcXsU5_tuqmp3wNxD1xEVm7P-AZMNVh6ioMBJVGw_Ljh4viS8ckJSt3dcxubGnJgzVfIZmcL_JSpDjciOlSywV3or4-1TLJwh59f4cX6HNpTUQR_A_YBKmjBZbCu5qWBJ3jlZzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMEr8uDjd6Xsl7LqGgVpxC9nmXYofA0EFZ2t3z6W-H7quUsK0LZPliNwnWQjo0LnyxMs_eNnphiatGEZe1Tx7kmC_rW6kdnyZ2LWQZQRIjsadp0YVpDwCWra1BKm56hQzcuyWE-b3S2rYs-rd-V6HFRr0vEBZWxnlc3iPt5pAbdJfk7SEV5Q3gnYfs7QzfkLhiU6C_SG5kFFUVcDbr61iIwtSa-UFBunAr7QAhtCf72vogwkdeL2N2Oyo10BN6l2UcSdWEMrjvzA1ayUCHgVx058aYaAL3GKHheyUwHZ3zokWWIWbLDJL0c_yBpcKROCzgwK9AIwyOAIxYlRcNemSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbZEKjY6FUUPMb8WFwnjHblphGQBMe_opivO6D0wA534HUNFAJNk0DRxggiqsNHRBv0uSWV_tXiYN3KxFb0JoitMO54MuwPDurF-PqTa1JcKlFJ1y2o1oP60pV59kvpkc4hYKpsZNokqhEJVjtezj73VTZKmfTMBaCsmWkVKxj5Nq8qogR4OhGdgCJ5E8LGbns2xuUFOcCoxV-jQXF18P2bVGXaidL1Ozae8JrfmB67ejTJJEPqcq8K7GVbzpjD307O9Cifm5-fDgLPm6yv5IJvM6xDeriB0umBNfI38tsnzX3sDRYF6Z0QjuhEpxl4uMymNgtSAwYH4aq0_SzeL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjOc_11O0uZwgIjaN9oSAItlcQM-q0rbRcWpiDZNhvjHD3C1nTqcwuge0iE3M_5xers_X89ge9uIUHUqAfH_oCru-cbqZo7cHXLgmTYe4_KYJrRvjTDsbtY1bqpFIJQ0MncgRGmDEOmE3U-mxppV8VufNR6FwAXF6Np_oZH_a5cwosRQbru7LlJg7MU-FmJfPTAxm10zZZPeEGT_3bfGhf6bNfwp2jqN4QG6dkVILaXh5bxJOziZHNHiWjzdnzvbZOdUBiGLZfvMP2DEWeVqDmDMCf2LN40mmryD-faFeSJJP9dD0Kmq-n6SHDPL29HNW79LPn61SrtdhEC3Ka9GRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WekJpbQbdf-TrugduRRyg0dj1HCGwRePzQ9t5DSSGN2BrZhyslE8bKaRmyINNwBQkNqKuUsi0cD1uKCAxDq1oeucgXj2EZAv_G5MhB9OyxdP0aTOolipXHq_zi64fO44-gLQj_UGE9T67tP7d6dk6BZyoeSPcJCa0dxhalNH7gFXnuyXrFf1bbx2TG6KG2ZWzsiZ1PSf71j-QplZcStXl_dEXLt95t22r8wtJiK82C9MpKls775jfQkIob5Clry4xMwMzIh39WOEepDU_Wu5LXf-uT0Qf1QSneOCgGRqkUDFfO1GV2B-hdBrRPRd1TRhM7xh6A5UTmBykAZmdyhgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOm_owkOhXEEp7vwBNsPjNOVUNeStfuKkDdmumFMHbSnYC-BN73NrfZQgj47IimOUeJVorQ02iZn1sXtSIReVh-xd2WHX1ca7XjPIHb25tKK_q0XFpIK02HLxIwG5-4sB72tpEAeY2e0vzuoPnuAZ8Y9JQgz4tTgocT9xs19RxByJJJjnsk5bkOWBQw2Kxhf6Try9TYVgNPRsNsYin-d7eUqiOZfYa01k-SZhmuFFiON0NRIJ_oGoSrfY83AVNd5eGQjAOKzVGwzhE7x-LzT-O6AlxpITEdGd_ZPkTPVZXvIxZdtqEv0_0VGSCuLAdnPHGkRJs2DM9Fir73hjSlFtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=HOJY2B2Ds228WAIHfELoOJ0wxqVkdkC56y4IBl5hUKOx-eH9LkyUhNHL_54wRYAuFkppk-HOpug_2AjuJhYAlqWh55Tsi5mC7ecn8SfNWezKgw0d5SfAYYANy7-8puNarPXKOG6xyGvL9WgqwQzDFhW1ye8WY8WUi5PlllL0hl_jyN_6z_wT_gc3BtN6XKFwEWQpNm083b7McGvFFUa1ORmVVXapn3d2byir_dnNXdCDu6oCXps6J-DHc1CxCsoV0gFSmiFV3-IDvz1YtSL7POZHTp_G2luvOxfxOBFMhDirTFQTOWjgRXJQYX3pVaV6o1hFcFb0l1v_Xi4u_oaRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=HOJY2B2Ds228WAIHfELoOJ0wxqVkdkC56y4IBl5hUKOx-eH9LkyUhNHL_54wRYAuFkppk-HOpug_2AjuJhYAlqWh55Tsi5mC7ecn8SfNWezKgw0d5SfAYYANy7-8puNarPXKOG6xyGvL9WgqwQzDFhW1ye8WY8WUi5PlllL0hl_jyN_6z_wT_gc3BtN6XKFwEWQpNm083b7McGvFFUa1ORmVVXapn3d2byir_dnNXdCDu6oCXps6J-DHc1CxCsoV0gFSmiFV3-IDvz1YtSL7POZHTp_G2luvOxfxOBFMhDirTFQTOWjgRXJQYX3pVaV6o1hFcFb0l1v_Xi4u_oaRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX1jOnbuYbbCvfWYPG8BHU-mdu1jh8dm7trgidLm0V74t1Jr9KW-RR1ttRPDMePvmcEAqL7ObFio7vWFpaDkV74ULW12jhlPHlZeePWcemR1Ww4J56bnOPiVeXmDWvMrcidFf-zRwO-Ogz5fcibwWAB0asZ3V_7Ev0izEfSu7iLfXC-BpY45Jhi22zzVoLDTmV99WRrv9lQB3do3-g92iWwpb7wI1HT9uBaPIBYGyDSKZnzej_8iIXZ6vuStmmyHc-6Oe4vwle4ahOI9nr9bJSg_L0kr1mxBLsucE7GYXWo0h2D_m8fWxzmB2ItVyG0zBlk1YLwJysooOpn5O4cdqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vN5O_ie8sv1EnSSGu2RVzfBAmt3ewzTmdRpB_0h7B9p3l0_yq6VDFDj8xlzeBH4aKe7UvCrYcEw9ZLjHITZxhO79XnsHORbZhjbLVsH9oNtGX9U8WW2gseLnpuggoxw2aj5BypQZ5dw7Q3M45_jJ-UVDy5iAIrBdXEEuzOXIT8clrlHnudXo5-TvYgY2L4uTRUcAErcgKJc9jgAWEm3Aq39kHHLpBVR_8hYNmruY7BQT13f3JXfu8OuMge6Z9M3MaVtlYR3wmPrwzu4Ve7Oz7hEoICN2LdkPZwmvobgQT5esqTfEnZ3Q2KPfK_1A5NXYykr7RJdvRqIFxBBif2dh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFPVmcuhR7I8apvCL50jjMqVmPv4vWKs5BAtxDNxVdb_VT7Wjsw_tScFcm9ZoMwa4KA1x-_sqbdPZGqK5Kx70WqAqfc_yFyIXaFeHwNd4GRr12865ETVkHGU8vqj4sA8ZG5CJ0xlpEiqpuSIVtYaKL0PRohM3_53LoYHyXDHzrLRPQujreAiFbfyQCid0XMB2iHdc85uw3XBBZZPKPo1Oocah72cGtxUq40Tp8gcOINZ-DoZ_YIQR58XviQtaqEkkKS4OPUY_GaxbuzumGsCNMjJQM0csNwrF76bMKkZPZLeXsXnywRpbEMclRsCAK6QQjSQpEJDEgLEI30ya-TSww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq9N8duNoXX8RUEhBeBjuDdBQYDMbO7w4PRwPregnXTZ0D32rYxDIzep3X-UOPoW7idYSMp6ZucT95cXtnfc4yRTbdDETLwu4pyltOkn69A6FYjwRuxIbc8Wh8_k_trR4mGeZeuZKGrlMuetBdrtqoEBFtqI7LaxQWCM_O9tvo9PacUEpxyMy2poaChud6pjLzkq-oHWBxix_F842YyLQYH8WpprLKZbQnt2LcSc2OqcC8N8lImkIY70Qtbwyu0eXhH2svus8SIBihk09FRGcape_Je1sxdrk3GtatleouAtn_y9s7Op5_InYyjWFrDtJRpLvsX4GWQLvGL6OurehQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzlMwvJBXssoGHelq05GMvtsxnc_JOArCbPHYcunRoGI496D2vXc-kkd0Toooh2xAWcYl_lN-76P7Gj5CmNh4Vvs8c-uupRDl7395AtlPt52yFIck3VaYANYPEnnNkHktHvOzKyr6EWz2JO53T9dSNEWdxki_pokj_0qI6TvGL798SoRySSat5wmdWk4ZDKW--D5f7kzJFd8laybe03VXpT6F3yZaC1iszVIvsS2SMxgYWqwwKZ8QN3CvmeVJplFl4zpuwya607uuPKznHI6bIKDNYgkU3nDJVepUKzNcJTxEgzOSqwKq1RFpSgaj92gDbWnjISxEKJ3N7ZWzTJJru0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzlMwvJBXssoGHelq05GMvtsxnc_JOArCbPHYcunRoGI496D2vXc-kkd0Toooh2xAWcYl_lN-76P7Gj5CmNh4Vvs8c-uupRDl7395AtlPt52yFIck3VaYANYPEnnNkHktHvOzKyr6EWz2JO53T9dSNEWdxki_pokj_0qI6TvGL798SoRySSat5wmdWk4ZDKW--D5f7kzJFd8laybe03VXpT6F3yZaC1iszVIvsS2SMxgYWqwwKZ8QN3CvmeVJplFl4zpuwya607uuPKznHI6bIKDNYgkU3nDJVepUKzNcJTxEgzOSqwKq1RFpSgaj92gDbWnjISxEKJ3N7ZWzTJJru0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9QUukXOX4543LCSHNoZE4c1OtD4mfIu8FhxXQAUW4n_iQ_DTeoC32O8YtbyifjvD6VqRvtumYWsV_H-6yoLpD5MYrZKP5uZqcFEA7IYMFq-oCKX4GL581av5X2UStlGv72zsRWHKeHoPKgN96nQ9RQvDlTK4bToue9eDzTHB04DVpFucmigFs7BNMuWdavdeQjVRIZ1P2BZB2EzmyhKe2XS6wkjnKkLGCM7AR8oR8dQo4x3kC7o9wRz9T8_lnjh7Ck-tB7pN51tGsYxGuMfTcZyLWhlJTCaxxBgsOdnfyKY-kwqnHgMf4EwnT3Sz0Kqfpy1DrrZ3KHY0hKSjgxKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCvoV_m5f4Jkyq0rdS0uxuC8Qnoux_dBNPpQ9KDYBM-O_3DpnPC95iQ2XDcpT9B_hGfLqiyz47zwy-C-EC-rXDxke7OFa-OXzozJ3Fz6ZPX3cX6Jw1b4aPs_Ohri-kXNcubXshmAaWamA5SSeQfPAHhD1HQ0A_vjNuQIIfY4t1viACzJbSBXlw1uKNpcKyHtfg6iGjXTFce-gf0UzGhnONeR2c6I4RhrsYCvKdEjOYFAEGsEMT2DwWiN3XhImlvgdyi5vBnsrVc02yP4UwuiqRPXjl-mySXRv87RaSLYz0NOZB1vU3-L7I-5Vx1m_2qX95YIoUg2tEstyOSi8gQABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD3S_0bfkqOb_aRBvsjp7Y4tQ2LnPPfdVQYqVAd8dWtu0Khaeq_1Fi9JxYyqAuIbX7RLRpnkqhNPrB5awLIw3ib0L8VNZWJp3rzyAK6PoBCzSqcNStqSrnJTJoUyGvEd2aeegdz9hNj-xp5_DX2tmyoE045BKO9GFpyGIolJkK4pBuBvkOI8x1uSVOHJy3G4xscMMXYsuZej6P9A0PR6CPeWUU5DK7Ru7Dz9RoM-qZQMZXOPS5oyoSVoZRVQ4qEeumfDVT3UREzH0d4-gQT2RoiHKXOY9Zp5LU7IJtMtdZEWre-FctPpo_Py_ykGRCCRG8jMpbMcCWqFd9hi94vbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4grZY26kkEa2OUm3tUS5slDiTFhg3Ffq6KDW0CzzrscHmYUxkEsPD9E1ye5N1yaFYG5XZx5joMAliae8qw--Zj0pA5vsDZORlqaZuSFyazR_-AvhsQib8moT8SKj1QpkK3kc9VI7vt9Jzupit2tAbAkdsStePRGRqaVOLCC9jUuIr7P_fEqIhAwGjKaYIHUBKkrQ-sSo1AzWgzfPDktEehEcitLkpjZPppBYbV_G1Pb4ZJ9VEh3N1z3-7l3AF216RlbGoZ-z274immXjTugMR_13CBl-EuqjLqay-ATJmXPW4tWgAqnRyOM5K4kcrw8xoZ9Wz8MZQWpP_BQUS5t5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAPe5PyzfjKS7sX9dI6hsyM8TJMmDQbpTR793fPwYUN_DnTHAmJeh9ZQ-Unuxm9gOHNHEvYTVL2HnVpp_Ugc6C-9EUaK7cNbqGqGL3-hJMC-GNsUl3disl8Hhfk8aajvqokSLy2HWglCVQzSTSYPdVYOIk8xDlKlF78FFJoLIGt-Z02koknB6i3rEPkT9dpyAq4fiwOQuKKXq-PV0E2xwvYtCKI4kv3ZsJKLYPka2wLjkSYqyq4IgZd_OtRPX6ZRYhg3M1o2kQygfjaKzrl6oNgAai0CdORKXzGf2JkcQ8JZ3OPc1C9Ppn0tLIl-Gcj0h9gUuP1HL-zIG5DquDNeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A631yClfzqgOMOozdydrkLiyoCCuxtjZ9mJy8_OWHx95ScjRWxogDSrh0xjm7UXOnbZaMfmyrnOHTBoO94nDQOulsOxmh5rbkJU3R2wixIAk0cOIMIoTIGopyZT6uduRClh2Cs4EMFnUinQ-7UNu1H1pwXAFdVGH2BKG1xL1fl0bERci4PClt-iM5yngQKAf48Y-pVaRbo59yWEFYON5NZCaLJvhomVWUElPh8MvBz3gApNSnw5uNS1ELWF_xOb9Y6S0sUzjEMtz17y5HRXPL8IYvi7_bIeVj2gbeBElUwH_KFwvKuDsTqU8Aywj4iYbUYSvYlQ5a-l7PrIsrQ3yHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHNvhMMyjxJYwmmdZXfpC27WQM2B5aZ__fsg2smwUt_PS6_E_l0wpyJBKIkyg0EYznVO-VPaOC6LaP_MwOQ9kcW76gv8Ysa1z4fR_hcl2Zjz-x6B4nGxduHv1IQUEsPejAJEsoOR-dajT928Rd5H47cGEmHLDnJdptL0JSOud8_WBPFj5hGwaGa-vxwxWIM1LfscrJLwgx89GivKrJMAuBUjL3xqljcLJDPJB7YHWpd_bwmGdVIhDwOCcLXUz5cmyK7m5RoEcAx0CfcyM6tzTXHRPc1vhqN6naDu72kCmb7kFsjhSNvoMaU77hXtC4mr8uW7lKtwmWeNLnMeeZQwrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=vbb29i611268gBq-vY8Xmv3WlZu7DOj2q9rc4nVvpVUfY4GdWem-cui4ZkqL2Xc9T2VuMf5Drb7zEDvSv56Rm7zT1_Gy1pXiZgmQ9Xr8AxuVW9KUSUgxGt2fjibRqPxKTfuXQL4csUmxzZB-JYYcSAYl1S1x8Fem-3r05iCIcDCeo1Fo-U18hVhF7EhZpd3k1lQNPMhaKobIuv0bkko4979ItFxpwJPN-mlUTrldrh5Ytw41IMr08ezNm9h4Lp3q-7ZN1SMWtj5uRGZE1MHnEyO_LvrAVo_GC49-tlAa1flQhKCk9Apo48m3eNyZz3LavxZhkn8fdNyG84QkR5bB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=vbb29i611268gBq-vY8Xmv3WlZu7DOj2q9rc4nVvpVUfY4GdWem-cui4ZkqL2Xc9T2VuMf5Drb7zEDvSv56Rm7zT1_Gy1pXiZgmQ9Xr8AxuVW9KUSUgxGt2fjibRqPxKTfuXQL4csUmxzZB-JYYcSAYl1S1x8Fem-3r05iCIcDCeo1Fo-U18hVhF7EhZpd3k1lQNPMhaKobIuv0bkko4979ItFxpwJPN-mlUTrldrh5Ytw41IMr08ezNm9h4Lp3q-7ZN1SMWtj5uRGZE1MHnEyO_LvrAVo_GC49-tlAa1flQhKCk9Apo48m3eNyZz3LavxZhkn8fdNyG84QkR5bB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oioAOAwYkcbycZy77kO4NKrJ7JOqukDCyeQtMTbA5iF3SqpnFbpHuXNgs95lp1BlcufOSVpigPPzBgdb3bsnicET38-xYSfDY8eGr2_fLAqRlmhNhBXB-8ypqBudPNhyDXxxEXDWj_mnEtWT_4VCPdYn5G47A8_14Hn2lzGHFXroC14WfTfTrJ2SbNVakkqlBghzAGS7d3ejCz7i7E1jlWdPGovwAtxI9wdJnC6wwv-0YAu5tkGTg59I5ia7AZB6F0uz2S56hpdnkQrydnRh65dx7Z1dPS1MnOBf208Orjq1acuiwdSA5eK-u9mvthvMO0RdrlCq1W1xz7bFUExXfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbUPuOdbDpGGHa7kU9-oClXoVtxzrwHEvg2WT9j3SrdRpiy9SmCdecEsb0_HalJoREqjSIfVW0-UaCrjZ1BCt7B1eRfk7CPHONnQRZdA4XE9Y96ZVL8ainkIfd7dZGlfgZyr4ft1m5aeYKRhWa0nf11LdTfPjztViu12xrPMLA2g9Ld2TcYA6fDKGjYDpHUhAbYQ30AtME3R8cZ7FcSRMBQHd1URqoHgIu4FXc0zvE-gYEBphd13VHbp_qrzwHWaDQzOqhqPBQm1278bfsAPqSmcS3DHnaKXWPdLb2ngQ7vbMy4OyJvcPw8fWKmcbzyXZxTAC_09254Gnsyyo36tLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R98ZI6Rj5U5i9q46jwupwg8BgfblknRUd05w0bRsjf4e57MkMnmQa5P_4QZHJfm8MiaFsA2PUcgANotSsFIEMGCtglSK-vudoWnAeBfY4zhHmVZJq-8EmkR6CaN4-9Bt-ul4ohG5vtSb-KcM3vVZ3qeeCOTEyGyrPE4oLuC0M0Fwn7KHdGWNAyps-7NSHIslL34Q05xzRS8Ef7JPjLA9WdEhS0anC_gtdTeex_EjN1MHloKjzbfOXBkNubOjDTut-vci3TlB67oH_pHUH5kgtFTHvQc_cioGQ3zO8G8j5_aRU3DSzO4blHZ1VnGFxuRMeO0bF4aBtF2dZrVfvaJ_VQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
