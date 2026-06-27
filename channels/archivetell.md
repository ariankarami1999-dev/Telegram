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
<img src="https://cdn4.telesco.pe/file/jc1kuLOHnH7CtxhYJt8QonIhPrYWYfpKqnjfGKWQMbcaBayuH2Yvoe_-56KGilW73mCg8upAhFQKOOW9WIui5pSnIL3JOP__BGpoBDQXKFa5zBIH5U1COmn-1Re6Dz8I3YudN-WW6JAMC3FT2s4lYRtuX-Mxxj5a1qzipGzW55VCgtpfWrgJe_Nkez1MvAIByOYTQXu545VnX1G3u9bFqTaXjgXb972Viq1bwS5JOuCDmFilsfe_cdEJDtGu5GhoU39AYJwu_xERIhB2otrxHRu27AJcYmH_N7lpT_Z20QiWBN2Ev24pAtoHSh-fsWV2xg64dvF46XDX_ASaS-yDUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.62K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTKvlFoUPBA4nauUNmDr0lyU1y8F_SkQgQsC6nk6xel20NOPzx13-Z3d9Ak8i5XOmIOURr3n2b_xn2xCMkoPpUFFJOaZeO1rxEq47rvt0VYa_8UHOZQ5b5Ovxsa1w8pr3wepHv84-m7YqjxLXVSxKCkxBVEU8inGbOpuwsjQcsE62J9wdYCq8hglXY_R65W_hWHvf-PhQbaH4oi3EUgAO63tc24TyARFZNUCfBqLeTfC_GNzLhOxVqwfZTAQRVU9kEkS7Rp8UOMASklbAzSuTQoqpqFdXny9_TPLaB4ItfHEKQ_LpfHlDC3yDE2ISAxn0M_z2J-nuOtEgDR9SH3T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 184 · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 205 · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=GeF_WUyEjb_ZWWGBwMjW-KkNYCVspU_5qvAT-b1c5NmYVMK1J1AaqsHDjy9zJA5UdSUnfXiK5BL8Nsi2QPKlkd7zji2lkO_TwReRAqVq-5ByMeZcJJQ2ztdCKPtyz3aOzp5JoH3hiNIYU7Ec2YVyfc3JQP7xaA-W58TFbceLJ-siMlWlV34MOF5k_0eML6d9-5TDEH289sTfPTC-TUp9pWQAJA4Hx87YTBvDgKmH6rpE9-iSFKZPHrU9fcxRLyjWGXVoeH3kILLtoN1wiF3DltDCgdVQwlaKAZMPLHwbtkiHZKfjKFhtmXTQQ5EcRyrgDfx66D4pFqXatb2UuFJhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=GeF_WUyEjb_ZWWGBwMjW-KkNYCVspU_5qvAT-b1c5NmYVMK1J1AaqsHDjy9zJA5UdSUnfXiK5BL8Nsi2QPKlkd7zji2lkO_TwReRAqVq-5ByMeZcJJQ2ztdCKPtyz3aOzp5JoH3hiNIYU7Ec2YVyfc3JQP7xaA-W58TFbceLJ-siMlWlV34MOF5k_0eML6d9-5TDEH289sTfPTC-TUp9pWQAJA4Hx87YTBvDgKmH6rpE9-iSFKZPHrU9fcxRLyjWGXVoeH3kILLtoN1wiF3DltDCgdVQwlaKAZMPLHwbtkiHZKfjKFhtmXTQQ5EcRyrgDfx66D4pFqXatb2UuFJhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 353 · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3EiScSDhquj1VFA2M54F3uWSPZKH6F07mfiisRItkP5NbbCxjkzDYRBr2MZ5VVVwkVV7Xy9qlf9Cyv3m6Jzh6OOcC-XH-7m2QAoeFHkCINRATIgvrpPU44gydrHjEJTtLHqHMQGfBnEn3dr6t8-eRR0O6O5zQ86fBupO_Uh7gThTMtpLmCKCmg4F_moZzXDZcMxQWsj27CWvpVRUCrQQedGvqLBMBCxXSyzBNG__pIXCFxjWivhgXloAWnQT-Vru70AYesrjvw7EK_fZkujuNbU1xntqZgl7m2wjh-6XWYXq3ad1Klf8RvTtIo4SixRmxWnD9mwxcAdiBV26FWp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLMjAVLvi27SwrQQYJcmVlP6Ei7ZPwMa04d1zZDeK1_Ra8V9bZlX8YqnmE8Tv0a0-DZHf3IA4PaBn2mGcrUkUPahBipDZ0h0PCA9ag3VqyymJwvxl4Amg8xdfv3D6Brcv8uo1ErHFJ07zeM_EXGR9FBkXOeLpaNs_o3mhHd13g6s_GxrdnXeRGDIX4pKZQdhn02ktMAExe7NgSxeQYLzi4ckaefaJfnypYBl-sTnm0VurGYThAQN1iJNgOLFjHV5Q8Tt0wZ9dX1MSGlTDxvXpsBUYBmAIJWHtf1FaIucNhOhFDudoPGDTasIXD0-XfTc1OOTfUbQY5J5CGd-ZxtnAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 513 · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5afGLPxXref98BtKieKJBZffyKJ_xEJ0vQbdBwA1MN0jxMAxu1ZsxEmzTuiboyOCSvh-VVhJThfhoO61Arj7rSwGZzeSukYpC0NZp1m7GlI2tT7GtAR32UdKtZeSKc4gWQCNBTlz76cHs-hgs0UtG6gy3Te3wrbFX54GCyMuC0M936Shq7Do6VuvVjLcNvaaBGqMRTl90J1gbsNuyJ5G9eY5GeCVqjlb1qBlmFYaFqQ4OtotLzwrPGfGcDwOcrkYnLFkF_DYygM34P0paXC6yxHAO0ZLo4Uljx7Wki0K_yLb-_8O92F_N92VEdZ5QtUFD1qKtSf6Mzc6eYVWe5HsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRS0kcwBDOPNrjueSW0v9pfAtdBKpZhdvEebQ-t3rVjlFfs0ckKvMwVJg-4LOIMiyxKVX7l6H1T60NHTNeB1Ur0PEsYZLrqEW67J433OnGeBtGiQ-H12yEOJoA77krk2-vt4MDUPZZkOBQEJZB_jwioz0dE0h9c6NoHZUSFkVhhboDpwxx0b9berEC0ZiCd6s5y9mCJXK-QjlCL4_moaXhnjvPFC-TQveiJl6PySBr8ViWNhAtc51wylTHAHQxH1pUGksuCuaCECHM-3ydyOBIVLjU0786iVm3laLSRAvbxEQYU0g6TOsNN-2MwupkEecP7l-kTMshmVnFRhl1kBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFqufkFzekGsYQktT0ebsU7CD3saKqIYlE0Bb2YCy4upfnaIME-N2yD2XkQUTo-cQg6HTitxsSkLPKShEYaJJtRuZvvyP7bA3mPs868bgCv50FQTXwvz3H19FWxZ9zYNO582VnHY1yJIOd_Og8ZjHcuVjKqcrfqwBWe4n93AOQV8sDs6P4tYxoWOwQIVFyE0ryOFjninqOH5VPWFCbL-5_Rsk4Z_xs7KDJkaro6BpQ_4TAYQJhDo3MgsFX1tcHrjs_V5onaODyHypZxTn9ugq6dVWg5ZfqwyRMiNw7H74wcWOJBXfYkGjb907Q1bjhYRQxw_U04e9Y87TWm79ISTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phpA2_2X596bfFA335dSrY9nZTWDYC5IyzfpPasN0EjDs7iby-wVozUi8dVEmlAjfCTelk0SZiZ4Cju5GJrzUOwGQxziBOShpGhFrEOs-GBOE34lZs7VFnOjD_m9sdurFkuuWqPfhOtzcUebven7RLBOHPK1Vk0wH2eiijs1u5UYg9BOK38BQn0RqV8jKi2or8gLbuOSZdrMol_xdIWbjTRc1YxShlpMEo_-IKlvF1zCeI7cX0XvdZeKDnNoAelrgra0Pra-dOopnOCMSNVfyTwmN2t4D-9J-LygAvo-9-a3dSuZd3YDSrlxfIguYGv8jiYpf9mreqvpKPsI-PjA8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Uiw779kySIPIWjUv-RKVdjk0LaKIJz7KBrZwegoNGDhSIrLrOLdfSZarTX1_C0v7yrtlCAqq9-_wfA9VaPPKZCHWdDsHXgcx6fKAKUyDb9YZuE3sUcnhLDE1OcB2BAVQm3II3CifQiSsRlAvBiMsUpAaXeHJVjWmKrIzyaPl8QbP9gRDsJ9aoYTKhdA_WMmLP0KVpIpkEWCEzC7QQrbKycdWUoSpRqrfeLYD5zKzfYGHJW_7WKpB3DAADQyxUsQuCO2We8ikWdyTMCrlIH-qNF0Xk3GdD3OMU7pSH3bwHHqE3X5mmSPYUUzEUaltMnnI9BbaGxMnA99yeeC4Ybj7jlup3HPeBlvGziengiWGQ7IdC3e7oR7ZEErLMH2KlN8WysowY7bdGhPxLJ9_q1sGsch6m-sudbOJw3qqDh9XVTtjPnk0JZcCWrsn4cirsUegwPvELqUhUwHiStf-3jDnI_Jc18tO2QGHIXI3BDTWiYaLPXEf9C9K5xEs5PUu6RdP46gI5DsuBes0xGcIxg3w3dR6ueTiibatbWw1l-RV390ah-6GcW5wpPXXeJigYyFUYC9dqgB1h6SNOtqRHagzyGTdIzYkH8YLpGXJcp-LpivXzk2Q05BQHB1Eb2EhcSrs8AclL7diyaUE8zoFSbnpyzP5x5sMJkZ7_wV-vM3_H1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Uiw779kySIPIWjUv-RKVdjk0LaKIJz7KBrZwegoNGDhSIrLrOLdfSZarTX1_C0v7yrtlCAqq9-_wfA9VaPPKZCHWdDsHXgcx6fKAKUyDb9YZuE3sUcnhLDE1OcB2BAVQm3II3CifQiSsRlAvBiMsUpAaXeHJVjWmKrIzyaPl8QbP9gRDsJ9aoYTKhdA_WMmLP0KVpIpkEWCEzC7QQrbKycdWUoSpRqrfeLYD5zKzfYGHJW_7WKpB3DAADQyxUsQuCO2We8ikWdyTMCrlIH-qNF0Xk3GdD3OMU7pSH3bwHHqE3X5mmSPYUUzEUaltMnnI9BbaGxMnA99yeeC4Ybj7jlup3HPeBlvGziengiWGQ7IdC3e7oR7ZEErLMH2KlN8WysowY7bdGhPxLJ9_q1sGsch6m-sudbOJw3qqDh9XVTtjPnk0JZcCWrsn4cirsUegwPvELqUhUwHiStf-3jDnI_Jc18tO2QGHIXI3BDTWiYaLPXEf9C9K5xEs5PUu6RdP46gI5DsuBes0xGcIxg3w3dR6ueTiibatbWw1l-RV390ah-6GcW5wpPXXeJigYyFUYC9dqgB1h6SNOtqRHagzyGTdIzYkH8YLpGXJcp-LpivXzk2Q05BQHB1Eb2EhcSrs8AclL7diyaUE8zoFSbnpyzP5x5sMJkZ7_wV-vM3_H1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=Yz7fSgeo65wsH--YcIrjrZ8cQlVk5BK0J4j_Ryn7WPBiBBZAaeens52LHoCjt95kxQ15usMgIubhqJaazY0-kB3_a4D_uHIxcBTfMR1aGa5LEJNtpqFV9TFUqmj3PdFcpQjBzDP6hmYg9sD14BCieyfS-suJypyfrMwmE4iPfWOt89x8LDzgREvGr5CJQu0-xnStGEDuscg4rm0ziw_r5bnNbHEvRoyzONh-ahH91u5s32VIjznHXRmO3uRGW1wsVV2ZkNLqutWut5nZe48M4j8xUbNJcx81l18kC3e695Xmk3f2JBh-CQiSZoCEl8izFn9hNNMCLjkL0_ZSDPgDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=Yz7fSgeo65wsH--YcIrjrZ8cQlVk5BK0J4j_Ryn7WPBiBBZAaeens52LHoCjt95kxQ15usMgIubhqJaazY0-kB3_a4D_uHIxcBTfMR1aGa5LEJNtpqFV9TFUqmj3PdFcpQjBzDP6hmYg9sD14BCieyfS-suJypyfrMwmE4iPfWOt89x8LDzgREvGr5CJQu0-xnStGEDuscg4rm0ziw_r5bnNbHEvRoyzONh-ahH91u5s32VIjznHXRmO3uRGW1wsVV2ZkNLqutWut5nZe48M4j8xUbNJcx81l18kC3e695Xmk3f2JBh-CQiSZoCEl8izFn9hNNMCLjkL0_ZSDPgDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxRifyTOfXnvkXMG8zFljjynpoGGq_yzvkuduTORaxOK-LU_hSsZucSKSa5zusf109Ad1ETq3p2xoTrFfwKYcYl4efrn4x6Jfvk0P9M5bDVrkJyFSa2xTMhiuCqh69ijOJHhRoC742BgL21mtXGFTbr8lqWXjX8BnjcBWsSUsBkZ7nAoeGHQplzyVPzC5cWJLexHrB1v00MlmTh9HVCtv4fbxH8e5xc3sPTi81YZZnvRq0gLu7g46vemS_-c_PTcxoAxG5izsnx60tHe9z5D6y-hhmBEOxzis_Y1f12ltW6o_j36CfggtjsJ4fhN5OmR8wa0qKFL9lTjWZgF-tFLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PmEUMmvRpMVTDxN5LLLhnAdeq_3JZ1bJSyTGkpTV4BA6h7agIkS7H0DRAL72Nk_d89igNrRrxa3Xu7D_6_Fn4JUeM0bZ_sprX-9ueqpSVLyNL6RLuB7hq01AlZuoAIC-ui8_2mGzOlpW-R_0ctiJEnMIZ5Dcrvnxa7oxChW43BfaSw8bfvhXSkJzw1z2jngdWtsjv0_EV3Vdcrtw9NPd16lZ0hqSE5MMv70HYQRAVd13I4xn1DiJaStMduPauQE50k_xYUBux8pBFvKc8_29mhr_I0UdYEUBFUkYy37o3JVunp4ca5DWP87GBP_8GgWjbFWffVEmvjvOdsmdYMOWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PmEUMmvRpMVTDxN5LLLhnAdeq_3JZ1bJSyTGkpTV4BA6h7agIkS7H0DRAL72Nk_d89igNrRrxa3Xu7D_6_Fn4JUeM0bZ_sprX-9ueqpSVLyNL6RLuB7hq01AlZuoAIC-ui8_2mGzOlpW-R_0ctiJEnMIZ5Dcrvnxa7oxChW43BfaSw8bfvhXSkJzw1z2jngdWtsjv0_EV3Vdcrtw9NPd16lZ0hqSE5MMv70HYQRAVd13I4xn1DiJaStMduPauQE50k_xYUBux8pBFvKc8_29mhr_I0UdYEUBFUkYy37o3JVunp4ca5DWP87GBP_8GgWjbFWffVEmvjvOdsmdYMOWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
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
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
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
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=isfPBAtoxgq1SwOjY1GGkYky1PmQwyNGrkqebc9OI7FNOlkiUreKU7DIzWU3dzVx1E-sB7bdgNrBmT7m4xRzcdwFH-QssWJmpixTD-f_0GbK5CMCoCShAwAH-ZIm1XGg34JfUZ3KwOmb2Xr2Uc3Qba_vKuTxP4ng1La7Y5epw1TkIKuh_82K0oZnZa4zycsiw6nT8K7XxJKlnhMUb3Jbw12doD1g2GTCTDdSoHiNbE0NbsVEL2SokAUKvRdVc4wIbMD2fBGs_MfXWpB5mIBY4tdmguDAvxa1jgAHYSJTws9TKJOoj-NfGZnVSaYhHKsdu19sQLDVGU0ys4l6S3Wkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=isfPBAtoxgq1SwOjY1GGkYky1PmQwyNGrkqebc9OI7FNOlkiUreKU7DIzWU3dzVx1E-sB7bdgNrBmT7m4xRzcdwFH-QssWJmpixTD-f_0GbK5CMCoCShAwAH-ZIm1XGg34JfUZ3KwOmb2Xr2Uc3Qba_vKuTxP4ng1La7Y5epw1TkIKuh_82K0oZnZa4zycsiw6nT8K7XxJKlnhMUb3Jbw12doD1g2GTCTDdSoHiNbE0NbsVEL2SokAUKvRdVc4wIbMD2fBGs_MfXWpB5mIBY4tdmguDAvxa1jgAHYSJTws9TKJOoj-NfGZnVSaYhHKsdu19sQLDVGU0ys4l6S3Wkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC3w9LV5cvUXwOBMCnN6T0GV-NwnPKPM2tKyze4UBr3U-d-siOD7ROqPlPCuJhSIhuAGql5d8p2RFrpg5q4pHpOAJjdVgyvP8oTtGWN55DXWyXGCQ3zvtm3p4zjHg_7JLfl9i3-vAWquHk5OvTj9OaSuGBS6IL_XV8veoX8hegcR_jIV4JHa-9mKNvrviLdRrJq7KB1HJ6YIt-FqtUBXsIxxosvReZwyRqTm3rJlyyrhtHqLC_3Unyib9u7tb-EtjxD3SfjNI3nhG3GT2evhppftmgSf-UhF0hOgbrp5aIuwwLyrZu3g4QsqVlk_BJPL6ThP1be72HC60Rvpso5vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1f4gX8ws72PSZ2oBp5mwbkZ9NU5re2-hovKllor0RKQmkgOdbkpKXDBaLlSL3YJQgIRbdmhoRETY_2_jmyxBbJX5XasX8TIk5Nw2rsGK-IDie6GMNkezdaNMeSXv9L9GkPWdQZw8j-dFo6H2Rbifonu4YgdM4xqkuoPS6WufdDunz9bMDNVEZ6venPNiQ0_acim-kLGG4RJ1aAK6jZogtbKST83Pl4HdMyhvopLIzC_b0mCBQyM0OjO98EfVdblPz29GCSViaC05wL4tB0VqxVzKfXpsQzFv9S2qUm1pF3SbSnYt4zs5Q1oZacjRTLzcM6SUP97PMazJFpfjSShIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeKI5rkce26ulxs_CZ3vEa7UUVDwjbvMwCEplcifpAejr_yOrb7QHR5wcP0BaAcb-3Dss5oAZg4Io1-NEH6YeJjA6ay6HlX_MqXNhgUiCCZ36sQoC5Agljmj5pp8J2LI3aNRNiLUGamVv_pre-MkGRc88dsAxhUzeQtQDkyrcMHvz81fRDOxSk9iHk5uSOtPzgYgYc-e4j0F99OYb1jnXxCS8IOzA2rxfR-l3Mt9DoAcVMh3939Ni-NofdpjAktGdgTc1wD5kYK3xOLh1jMuBSw9ZQCPPvoCgNfG-jvnim6pkulH9iueCOKAfYTaUiy4tPe9Tg8flHXGwRrM33xsjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=uTJx5cZ67HgPf7lbzzgIOUTQQcfevi0JCEMWeQoLXAjIbx_CsQBTAs0Nhrffk2_Zik7YiQF4W8C_Xau9wcsCtdxsRW932-qHmKebGPFi3br6ZTK4qY0_m3O9SDlx4ObOvbwJ_nf5fKRqFM6fM1ZpkGx3zrmBd2KVOjLXz5MMyQjw9SlXSd-q3qVYbpOnn0wbKiNP1nDPmaI0vmOALN0e3Dy3Ctk3840kyntN8w3FXyiGH1-YuwX8gyI5ZfbAEVoKaYhrMn1VcmhitIAtL8lolDn9stqTGPxD3ppQO5TRxBNZ6X0ph3EIoUj1-e9m1MINh7w4525GX6vh9rQBOtFz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=uTJx5cZ67HgPf7lbzzgIOUTQQcfevi0JCEMWeQoLXAjIbx_CsQBTAs0Nhrffk2_Zik7YiQF4W8C_Xau9wcsCtdxsRW932-qHmKebGPFi3br6ZTK4qY0_m3O9SDlx4ObOvbwJ_nf5fKRqFM6fM1ZpkGx3zrmBd2KVOjLXz5MMyQjw9SlXSd-q3qVYbpOnn0wbKiNP1nDPmaI0vmOALN0e3Dy3Ctk3840kyntN8w3FXyiGH1-YuwX8gyI5ZfbAEVoKaYhrMn1VcmhitIAtL8lolDn9stqTGPxD3ppQO5TRxBNZ6X0ph3EIoUj1-e9m1MINh7w4525GX6vh9rQBOtFz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=b87DeuTgu8VaY3bNEZ3RcNVLEg0354zLR-wwLNENA-IL_9QFNYwHga_uhiCjhXYMvEXExTG6SUwCDvW_ryEry2i7u2kuMY5tTMYKtNbpUQdLxtT1MbGV8TynJ9bEMcMwvsLetIGzcqgRYcceRFf6CM73ArGTmg4YIsm3yG2oKHKEl2wzkk2C3QLZPnfzCSS6Z0DL3x0BMfW7mlLYQAK9wutwPwaAyWjpuFCcSmasV63A26XR4rJSaGr2WN65M9zqB9p1cSGN_saBMf3_Gyv5-1VPyKzY7D5voDJZxcDLThrJ3TEqKl6PMDcBNImDV-lk-sm1b4MMwpeEugTxnTGltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=b87DeuTgu8VaY3bNEZ3RcNVLEg0354zLR-wwLNENA-IL_9QFNYwHga_uhiCjhXYMvEXExTG6SUwCDvW_ryEry2i7u2kuMY5tTMYKtNbpUQdLxtT1MbGV8TynJ9bEMcMwvsLetIGzcqgRYcceRFf6CM73ArGTmg4YIsm3yG2oKHKEl2wzkk2C3QLZPnfzCSS6Z0DL3x0BMfW7mlLYQAK9wutwPwaAyWjpuFCcSmasV63A26XR4rJSaGr2WN65M9zqB9p1cSGN_saBMf3_Gyv5-1VPyKzY7D5voDJZxcDLThrJ3TEqKl6PMDcBNImDV-lk-sm1b4MMwpeEugTxnTGltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5O4jBOMmSGcZ78DX-5i3Oyk35WC-wvWWet9dHNWE1Y_rFSOLbRJnjHTWu6F4kmZjREZw2JghPxzbeqObZhU-6D2SnTtm2n5HsIE6b9lA7CAa1RjErQpbhMCF_vtJ_mqRmAjvuKRPaLvsj2Jf7GvIuenfmRmR4os9AWfn9BJtmlBSxa-9fS__vxgVBw276Y1y-Qur9VTEewnq2OwvdplWidzj3jsXRK6SjERWrNwF8QzyeIxUwXhQoI2vKyaKi_ZqlBBaYSwPXPY9gHGMgRLXrhpb7StWVjAGNJbWE0zr055DC4HmDKyn_mAtc_tKtebUaga1FVG6pisksoJsJIIuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkzTvFsUdxuDxzpawKGR9yIgxCySTDYY68H8Yz5gn2YIx5hMViyoms4UfslOYj7i6u9FBDnqPCXEouAaAus2s1eQ2O6wGJ8Rc87DmLK6ZSV7Y0wWz2bn8NJywW0U5YcoUBx6nMyxlEADIJhoj_fJY8xo322yr3wDTQ0HOC_ckRCw7b8fRjtpQhzA2Pibm6WOxF7Xe6vaxf51P3s9wGO8t6pyUEbQ3dmm7nO1VDf-W--rBBYgppjXoBx7vnafPw7jzKjhypuwiLI00HkA4LzA1kQoLWePmMW7sJ4Aye1F5xs-lvfIAcQ4VF9kxzFLkv643H6YNygu-xw69MyPfo3duw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJqdgf6lnhcRy5TeNwoUD_ZmrUGfMmxN_8iqlfYirkSAPhIs0N-Gjdo75TDiB4L1ZBd_suyOJ2HjjQ_V02fqfs-LYjPrRf5lgO4hjhFgUQOyk3X9mG-Fhe6-kc2lt5ua6f1Qeb4rhKrjMqKJ5bTaZIPo2JlY5VUy8WKXx0XGcPLgLXhXd25eUuEkyRiJTftSrFKZuaS0EA1_nDEkXe0xkE6zJaBjZIGVj0ruDT_N72ukYo1wMC-vrZMYJfLlvES2jqjzeWuZrbmO9VScd5xC7CSnK9MMMorIxNg9RamnhdOV_OArENgoRtxHB8Otv018UMab3F6MPOsprvjes0T9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQrgsCmIUxoO5lHTsetsclzIlIbLJEgkRtnHDle9v2CkvTJ_NHxefIpiFGRNtzGBYxcJ4w9G1JRqBGHUzOM6fCVPx-ps3AuH5R4jK4oVJmC2vgOfPh6AI67YTQigVxl3pnqQELEJTJ-I8HFDLbgE8CAkWy1nXxdZPY3KAsFpLvUd2vdnUitYDFQgSTUfGPr--0vndC7vKrlpx9R-WMSasQR-rn5SjQ8uAtRowBXNjPo1KgoaJEFR67DPtuONm9afalrJm_nPnuJthvnES6i0lPM6VvQT60rVKZ2p9_5zhBGtvAdTuDsk0Be2AaDvJqwsAZWBJMk7gyPRe9jksPaKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1o1pgG2cnMTeOzQ58vcWHg3n-EUUcowvRrQTLVfR_HMj-_3YZu1OlhfgT9nrF0WziJQs1O7RhF2KexpATZRp35Z3o904oiRmnUgQrxoG5SNi8TYgRR-OulBJ_LByXty_CWQMIqu9bKbtCygxAQjrhcFsrtmRE0vNnBjacAGKwa5bWh4urKR7hpAXuEHFfe7ijk4KZCpLzL2YEEZguhSX5Nsef97H94bNN2izyYNRFdetW8qP0NeHIBBqI_TqKdM8adeKJfGue5hPzfYrl_6wamrcF3BsNb2rxhKuQLkD7uQxhfauZgOvuI8ijCPxDxCTo5xbfznw9FINySgrbublA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUq-7t2DECbSZaL3Gi_4PsQwxiW6D9lByA2YZwj3Q2tv41L5yygoK927qJUqS74AN3RRKKjDpTjG5Y8L8cn1h20_h_dSh13LuiXlr7dsBPKhLEJdCioL0ujBkHZLiXhkqTxuxo1-HwMpdCajAkYTUZG6P7vRYd11TQC5PSAiKS139-N-_s39g4Q_hO7NAD51ykeZfC6QTurgHKXhyMT7Dfj_V2UJ9V3s0sWEBmYINdhBw6S6rY6nyz9GVNAPk7HvtWRinsvJ7XeuvTElDIPWjjpigCKoPibr2rONzhE9CpNgXrr2lVa0ZGlWHB2u_3YAfXatlQdzMo4HEeu8jquSxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDaAbnZKaAwMruMwfZLO_illn3fu6d6rS_Ybue8MdWv0wPnLrzl5c9YaWoxdJhH0oekiv8E-CILiuSI9u6DsQI8-uMENaM6s6YKc4OFzCr94IWeb5wi2vmF8E1v764zjlX6iGlKVutuIKxUJnB-E9tu_MH3H04Oc2qMhN3-n7ecQ6d8h-CqDgsgCid79okg-jtL4x1EhIjUwVYE4v1uhfgZA36filRh3ldFeAhXPaebS8N-p9hClIgeaz8hOWLfq5WvIOSrvCOx7jAW85bz0oai_u6ii1y1n_JJZc6Zy6JHmgCHeSYF0bm__ZElPYoJ_cB0KdSvAXHsvQKqgvTNnIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ30tmvTs7diUoaMjclKpE1xhNY1KxjYeFKwhQPMKRAbfF7PI9V4pEdxgmxz7loNjD0cOAKBRH0r0cKyU-SNB7p5ebi-k6QJlzirVsMt8JEv1ACde_nBYRv-Ou6NRTqTctGudK57nNF6IgVCd0DT-nc2Kai-QcyNr66mUO4mUCefgU0f02cJyQB_H3QutPK3xVZaX0Fi4t6LtSn0NmywglClz24TEuJGnpLNsE_0BxYKy2tkzJ-KgxC_5TAODjJok3vsp_9rjWt1ZjDyqAJCkTuS45fv6SPup7gOvQL_ej01xj4bi_Mt3RSgiXh6ZrlCW30sfQp-oohgoUoK_XzimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsJm_iM3Az4ykXd3qfyoB8AKyp4Qc0QHRpjynl2UpCOkJb1tLKKi-fKNv9hzW8FBxAn64zoEZkCORgQW0NNDPvQxVpbO3TqEicLJNG8pIXWOCp6O-ushVkJKdbX2k5KqdtCO5CSiuJKEkj1nzceEMoOJ_9XV1Cp3lSHrjSWBPGJizkQIhv_isgicIs2aVmHWAbsrg0ChZy64VxU7902gNWxssE-S86w16jaOLnskfYqtc6OVQGCWSz_fxw7pWBvQ4FE3byibFQflaWPj-3UGqNFJUxchqYUol8_-NBYMb1zWRLpj0h2vGBx_lo7CIn6ZT0vP6_x6FPYf7AafPXThSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOWXBnMrxeRH1LKgILjnmC6khoJYeQBjALdVAIHe_ur0ArJSORBX7-raGqen1T7ihCJvYlDd3_oDlOTu8kzjxl0PzuBu2kuq_E58X6AySP1Akai5ABhP6TUIduCFGI3EwSSzoqIvhgqtIV_Kei_cn14OJ07x-54PhKDAGN0t9WCCR7bTLyAZZOWdmeBqY5V5uwlqiCH-UBvUp_rjw3nE0HMAoLNH7_A0gQTecyi1h6dt6rR2ocnv0lV_OnWLxHXsCVNXP-9-zwZIoxoDCEpJ-YwGdfynUMk7stKi7AQMewtTyq2_tTFBCXkka0du05UNYlKsNswQlU69saMF1gLc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gH8ZzMO2BXlxmUwZeRPvBEvkHG2Wt8x5zsbqbkt_fq9gHQtViYFZgJZbNP8KOw5S65XVQ9qkM0uSAH7npOXyd_xG113Xl-4L8uGrd8UPpZlRNVuETrTycrKMLpr7A52oGFasgQqtGojxHCa6AkenyqOHQNigQbcsQtU9wH9Od-g4Ff1s6hd4u8tAZZVVIPgFSAhlQDHsNBpPv18Hlg6hJqrxUEVz3F7XZ39hUYlnfynhuMkLqsPSbux3iTYC0LJwp8O_ElztoqJZI54srd0uUcEku3118dYCeNScOhALk8vMqAXX7NMHU6aWCG0bgyKbJSZ1XkmV_w58ZG-1vkWEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlFy3C9_xxrLFX64oalyukkTgS94B2o1xYu1IAdB2vTHWlBILFFKuqpRurbsr85bbbdUpguohYjNiNq_f85MD-Hcvdd39SOcgVr9oc9beWRKuV26ITg7vwJgOoiKQygV6VkRSJk-r9ThTvHCRt1tUZEeyur5fOMfuUWQCr_fo6yzl4f0B13Z0mEYTdN2LkMed8IWE_shrxZ8_7JC-zJjNrxCu6whtxT2wJ18V9FUGEvlrOpFzVZU6nrQ0bIv3Mxkw5M-COlUqaj9lH82n6BKF8L_Zfkt2gOtg19F6wf9HjHo7jNurh3UrTtdYgeG0Fr5Zpv2TYN3sle3NiyOK_4nEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6sDBrYQ_f0Rbj9q9tNJ_-2jBZCu1rQOJbXpYYSEjvDnb9HjIYFA0_Ww_zEV4FGg1Dvtr1IiEixwkIWD0-Oki7JplcaKzE7_QvFAbrrp5KblyBSXKSVAFESxgAITJSc8hSfYn424udDeqMoFumMfLQTJWWpwVFtAL43ayZ4AHAMLZPU5HcTzcKKGjzquHHpZJAaM14MnvYKQWZFrydZXDTfh_8a_mvCYLOJMcN1Hc-Q7UfBqApRVTqsM8bSJQ5OkV1fqL6xVVu_JCSBAVvG7ZqfokP6OarogGpXHgB96tOVwoYn6_2DplYD1erPDBerO7pXSn7DAFeLK-jcMEOnuVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU2FluBsh4LQFwQd_P58jCptZ5ejjfvFT55NoXlFkEbbCWK_Sa1rBk_MGaiOLI8IdayOwyFyx4imEDq_SjRjjmMC4_l4C5llmxRuIjJxwIiRjH5pHMaS_AY4cdyE3-kTqJVdgZroTK14fTj4v0PNo1fwZWEP4DijuY2wpCJVbNL0m3mIbFGZzyzaVWzlZAamMX7PBgtChfPFGzbzU8n3oi2D1QtfCrWl12mYo1a-bGFJBbuqacmUGgS8b3j2zzerfC0uxlAgxpv5WxqlRaUPXLzBCXXUBiyxk9YYE2TRCzr1x4LH1VGWWVhrpJNwDXkbZ5wHx9PSblHv6g1EHNv5MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=ZrITU4qx_RpbaNawiTcnEnCGYHUruAKWGExcb_y7T9jzHVABY25a8fF4Eit4k-xbiYhS7QAx7xBc15gq51d5-Blzg5J8v4-eJECidFvPPD90edR1YQhlIKwANMBPnDIPOlIHqSk1z2Z4rOS7ir_6-2QerxNEUHSkxe82KvLZ-8VtIHq5l4QXgxWSpWCx53aZVAftk4IpzOWmQEsMhXKYMCb530p0AOuCLgsPORDqfTVuUz0lxpxaDQhmAsxiyIIDWhsa8BspILTcXDylpEKc6b2ASWKSC2T9q57Qoz6td6ksordZg-bNCRhlRgjUa30-vQnU81iQiaR7ZkSONdN4yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=ZrITU4qx_RpbaNawiTcnEnCGYHUruAKWGExcb_y7T9jzHVABY25a8fF4Eit4k-xbiYhS7QAx7xBc15gq51d5-Blzg5J8v4-eJECidFvPPD90edR1YQhlIKwANMBPnDIPOlIHqSk1z2Z4rOS7ir_6-2QerxNEUHSkxe82KvLZ-8VtIHq5l4QXgxWSpWCx53aZVAftk4IpzOWmQEsMhXKYMCb530p0AOuCLgsPORDqfTVuUz0lxpxaDQhmAsxiyIIDWhsa8BspILTcXDylpEKc6b2ASWKSC2T9q57Qoz6td6ksordZg-bNCRhlRgjUa30-vQnU81iQiaR7ZkSONdN4yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guVhp6OFEvkubQBjQYJ0naxN0Bq2V5Kd3iQTzvXLwg9FqmQsfdHJ1l-s657yjiamM31I3hw33sB1BpKb-wa7HwLvy51z-KyPwuh68X5519H-r4jxUmLyb7mnyAcb5tqvHxauukVyL3FqhR2LirOdNFqIkClS8V3PttjYhLNBF_S2XKer0SblWACf-10355qxwbwt7bx9lGLi0XtvZZOPb8vKzLpjmTByjP06toNco4o4qFAQiJEqPz2XLH2Em4rFyLk-SNgN6O6jzPU-joGPskOvJy9yCdVQGYbYUj9Z26bWZQw1dZepZUz5Bh-exxQrEQZ2c6rUPdHtCmJtXvplPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U986cfjp97lVO9vj9VZpLyZoEeksxKXHDzVubYtf0dNKFac3EvP1-f2KpxgbxTMMwKb-GM-FRr0Is4bj9HCLA3rvKagVAZr-gw31aKGu3MaPXLifZxgYiN69J7oRsSHYvfm5JAh2znKiYIkifJzQiHZY4GBWmwrjmImmOA2d_s7iw2Cl1ftByxgAzBHhvIMoOCOjP3Rperjllh5uiLsctnBqtCCJoraN72s78mc3xrwUnxzTb9J4MJrcshwc0JqxZgXp69qDmueyzVwXNLmEhuoSjT-v9CnAyzXgm_y68TruvkgNgeHKYY-hHaOU-BDS92ewqj_HtqMLbFkkZZhZeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TInlfgozIKlp4Log_ZB8PnDrPuaAb7Fgl6YV1c3dWCdfcKeEqII0Ses4Q37iVN86RouYqu349wdLEBxNtnc9RZt3GtDoRCiIDEbIKA-sm5oWYlmENz2AKyTV3I7ss1uvJxU9WceJ4pZWkgmReljNQc6RTYx4N1an9QwjqE5tAAVVP-XnTHs7CTy9usPzjCG5b5T8oaFnG0tkpACNTb_8OaqeQQAUJRIGRU_R1z-PUoNBLu5bqTUF7rdoXJpYH-bJWjX2EDMUxWPgSIdCst-8IH8lNU7gqsNMIRl3sC1K4zJ0x7XVWlabqMFMarqhE4iZnaxMtqy0YUnSL_23CG3hTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fearFcJ6JEKGo_Z-xTWvXNRI4ONXx75sarkH3XE3j-7AAQ_j_vvZ653HtSCJoug5_nXVX3YtnmqGY-prYciAWwHhhTRGehyoyK9D1ckwJWdPKrZNtpdexUJ2X7WEIGguW-eVTTc1BFs740LZhOlx45tjZWhPb7amTz7rgluOB3fbeO13eNZJLeV_4VK54cYvXda5sR7RtZ4XBnDz8FD2rSp3Djpf3qXAt8QhlH2G50I7PJjxSuXhBmE9GLR0cbBlvElNKM7NBJ8SF0MbGcHQz9x_qJGRgQssk5AX03L_td2grt-4yMIEZVrPCGTnNMnJEhW8e8YKanHhAth5syHE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=WyPg1mOQszmrxkGpjElweXcx7vUR1AGZsjd_VWC4pp7OTr5hdUtaeml4gzviAPWS7SvrljjvvQ-thQECjFIigsDbJvNF2Tpx16rW5CAOF5NVF0eYVEyy8Fr64aMmwOdw5oBlJlXhIsosqZTKzHBgSHmi8Dhwgnx6VsV0-zGe16ReQ9UNbvHADQoBrcPhwdBh5mzFNEjB9BUzbsWBIFD9wmNjBIScHPcbHtM_5wnzQXvJXEwBP1J_3L0KdirfalGDRWXBKBmx-FMcqW1JzpyXAEPpccg8eMjkG-QRa1L4K2xdjCCmksxi7Ccnh4bWy9CFADycKYYdK1hCy9OQe7GXOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=WyPg1mOQszmrxkGpjElweXcx7vUR1AGZsjd_VWC4pp7OTr5hdUtaeml4gzviAPWS7SvrljjvvQ-thQECjFIigsDbJvNF2Tpx16rW5CAOF5NVF0eYVEyy8Fr64aMmwOdw5oBlJlXhIsosqZTKzHBgSHmi8Dhwgnx6VsV0-zGe16ReQ9UNbvHADQoBrcPhwdBh5mzFNEjB9BUzbsWBIFD9wmNjBIScHPcbHtM_5wnzQXvJXEwBP1J_3L0KdirfalGDRWXBKBmx-FMcqW1JzpyXAEPpccg8eMjkG-QRa1L4K2xdjCCmksxi7Ccnh4bWy9CFADycKYYdK1hCy9OQe7GXOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=cOVBj9D03wob1puXLPML4sDvo_eacDDlKJUR-GdEZAzoixRdvI8UHYWIqv6e9xe2tOIfyy_NRKsidHcY0YKum00efx8q-AarQXUvfAWQHNa9Fv922TL6b-409kitmRWbpX_u3MYVbA4zJ4izeaoOAfeWNhiS6j9t8lHDTzn7HRtD21WwMOa94-mzlCesVrCmwxRze2j-nmsDClwOom-m9Ou0yHm53GA6GYIQQkgiZ4WsHVpmW1t_3Ctf78LwwaxF5ksTdSWup8wFmJwmEQ8c5PHmrzBA8i2GGsyClx6PvOhSMjfebWK9VdJ6vudspmbbJvF7BzINXp6WSe_VJL_ang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=cOVBj9D03wob1puXLPML4sDvo_eacDDlKJUR-GdEZAzoixRdvI8UHYWIqv6e9xe2tOIfyy_NRKsidHcY0YKum00efx8q-AarQXUvfAWQHNa9Fv922TL6b-409kitmRWbpX_u3MYVbA4zJ4izeaoOAfeWNhiS6j9t8lHDTzn7HRtD21WwMOa94-mzlCesVrCmwxRze2j-nmsDClwOom-m9Ou0yHm53GA6GYIQQkgiZ4WsHVpmW1t_3Ctf78LwwaxF5ksTdSWup8wFmJwmEQ8c5PHmrzBA8i2GGsyClx6PvOhSMjfebWK9VdJ6vudspmbbJvF7BzINXp6WSe_VJL_ang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPjgAnUiIzg8yPOPHlZFqm5I_nE5JLLDNAAfCc_pzPqlJ2aLPx4o_DoRF_k3re4yyKg_I_WO7Wtj6vDf61XT6U7MF-gdahaE0TkfEAz0Ti6B0XuD-_lSbdAVVMWLfyRDttsBCWaT1Yosx5tbiMTfbGqd1j_t4NGI2Lb7oixIOHmGe4PZKPBJteUXlFAkstYgwv4_dg_Ex8g14j1TSjqKTOSrcmFoKgKkn3uORZAtwcc2RVko3CEo4FdDf7qnD-mExUPU-JNsEzQ-nxSErEeWqjO8EvkVWx98UkZs48GN-_E9eHG3pFv2z_I_S-Lc9EgzUvLtJesSNK4way3bgvv51A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=pSd6GP-aJ0DawAtG7RT2o6QSLSHNqjIvg110AyVEoRyO68ZzmaFtiNLlm7edGKDNFEtD9LPgOfRZOZiQxcSi3kEp3Juji1FxZyv50ZFVB6s4SOp_7NYCPFFVThJYAd0uRBgrl4OIz4WoIR3rRa9FxK-4F-Mw2NAd2cwwjoYE02aZ7l-XYL8n9J1cShAHQYHVMzqjEUjtloXTE1IV8AP4T6hkINzV20dhAUS2GL_zW5Fd0WC2znKiQvnAQscw2mdb5ol8zjjNvZE9JnQZ6lnAWZbsHmr07qWr8UcpRrBizJytnx7BXXJwjFd9z7cueUwUsleZ5jnxbIUzGbfMLVuVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=pSd6GP-aJ0DawAtG7RT2o6QSLSHNqjIvg110AyVEoRyO68ZzmaFtiNLlm7edGKDNFEtD9LPgOfRZOZiQxcSi3kEp3Juji1FxZyv50ZFVB6s4SOp_7NYCPFFVThJYAd0uRBgrl4OIz4WoIR3rRa9FxK-4F-Mw2NAd2cwwjoYE02aZ7l-XYL8n9J1cShAHQYHVMzqjEUjtloXTE1IV8AP4T6hkINzV20dhAUS2GL_zW5Fd0WC2znKiQvnAQscw2mdb5ol8zjjNvZE9JnQZ6lnAWZbsHmr07qWr8UcpRrBizJytnx7BXXJwjFd9z7cueUwUsleZ5jnxbIUzGbfMLVuVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6UmYEfmfOD9deS7AFIu0oLB8gEQA-x1VMr7ilj6XJeoCm0wZZ2WXNO1GRddyXYTZxEwTChYkDA1uMQvMOhg0ElTFet0Ie9A5dTA9dArOJcwdHBjelxdrulXjwkXmBrqOLIwLra22BRG7fnP7c6hd6VtybHffpsRiGUIwDO0gfqIGanhD4Qrcb_P3bisck1basqMkdfIxwnPEZEx-uy9DWwfFFdER5CPhCe_J8wKtM6Y5KSY-qBKJO0JDNAJ4gNvknq0Mu3xUhZ620FmLynCQtLDpxZEj02gY0HT8Pi_kkM8360-Ag28_Aap7Dy5SU32cD-TJJEgC-dDmsgL8RVFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyNIsVW1HpHGMIA_TtJ7OhzTjTplgRZMcxB8VIIKOF2N3GunuCyb-ZcANIwhnL5CZhyIPI7qhrsZ7m0lQSW2cxwMgOrjDjDJzq2xLQVuEBzgJpaZ_WtU0OF16UjZw0Ksn5BGJtLSRUrd8ig1HVkQ78sbeN4kgA4WXcQGDUxk57XnqK5JPxHhHWBnW0erGA5asBKVESsn6xLBZpW80GmnuJx1Sylt_6NxkBzYkwxEqEIo6p-b0yHY9fRNvJ7Yh-RLwI_I84DDuR_ORskvW5KiurbaSfHhpl8T2kYys6FddqcfzSnginedvF8K_7Aix4q2NR775-evuqNNyVVHd4xvTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj7bGP_S3S8O12v3NBaIvZtv0WzXbEWO8yAlPfvQJ_WMdgtzk0k0Vq_fxCdPDyiruUuH_HknQDK_4XgoSoPMGgVaQi1rD8m5OBpi9LtDkRvFgVaogKUAPdPsO9RRE0m9mDARhgntwp7vgLmU_UFrIwkPUP7lfgcya-qcSFos52Aoe_RqB-O_DgoMPj6vShjrnPvPqeWPDDtJUs9O7h00pSx-y2PPuekh2WQ_YtcZZU82dI5BUYVr0HsTOxlxXsbj_yvR05IoXlwlUKb5iiGtCnqHTCj763Z5txa0kvQGsdQgPdAuLGH8yDdlQ14pEs2gY0JGhN0ci-wVoLDAS2YWXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUu8aiDEkwjl81WJAB8ApgxOuF5w0vNoybHYBV7ppzkMb7uDW68bkVlQ8Oz_g5pJHzZHhV7ZsRUexPNJMN6W34rHerNQf-anci8ldZtvi86i1PjyMn33qHJHaVBN4-OWjBMWucRVGIDkvhBEShBZUY7x8BftXeGgpZKmXg7D7OqsmetrhyrCucT1lxXvr7DeKyYPkX3J4FEEi6YpWmzLnryZbpM1VxglYTqHKfaua-HCgO3E3x4l5Tm1Fnoxxx26mcDh09Y7B-dlPz0rK2q8AKQEvdijiyyBaPDmkoBX7elGXyyawPvUrJ69fIWVExOZmSSImvYdQxRT_L7YyroyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=DOBQ5dis6kqE3JmIRtSTHo3CD57r0eNR4E_giGnEM7i719GEVk6urxX3BJhQW56QPGz3rt6NRDUy9WZ1BqIyqj6iH9B2j-XkwXHEz6SAK5LaZuKAR7aqkv7-lk-WL2b3SSiX5afsamsEY2aYoImXFtlDHw31UsnvbJzMKSN-nptjwKiMDTQV6yDyJ-VGO_bPTR0tC6uPewXvz43sFMa4xGFIefc1xkWysgkKjVnaalHdQEZNVqjNjxuxLeIu9h7P_26vascgt2y57ceDX-HD5COEFQArqw4Zv2ju3POaXNlWhSFdo_Nk3vbKhY3TJwV8DpBKIfAqZLyk3XdZdNZJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=DOBQ5dis6kqE3JmIRtSTHo3CD57r0eNR4E_giGnEM7i719GEVk6urxX3BJhQW56QPGz3rt6NRDUy9WZ1BqIyqj6iH9B2j-XkwXHEz6SAK5LaZuKAR7aqkv7-lk-WL2b3SSiX5afsamsEY2aYoImXFtlDHw31UsnvbJzMKSN-nptjwKiMDTQV6yDyJ-VGO_bPTR0tC6uPewXvz43sFMa4xGFIefc1xkWysgkKjVnaalHdQEZNVqjNjxuxLeIu9h7P_26vascgt2y57ceDX-HD5COEFQArqw4Zv2ju3POaXNlWhSFdo_Nk3vbKhY3TJwV8DpBKIfAqZLyk3XdZdNZJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7BMMeCgpeKaVMbKF-OGZvgUi9KJyjPrAN1-KkdWyQL_GYP8HYRTtht-qpWP9i_4BLWxg-yx0U4oz2xtxu7hnPfj3YfaPjdzVB_GG8J1c4SB_maX0x9xmEjW2QaKboJXLXd4GTyuhkl-dz5oJApVuO4CRNpDJGqiVWDHcZQmOLae_zubP_wC43jfeHHYBmPSf_5qgLgTicK5xD1wdFKwp8sIlEh_kZQqAT7hm-aN8sTyvvP_HamDRaqj9hBOp7Wi3iyoZEJi1Mxy8eO0jYKmskYNGi4XA0STmg0bkM08KFvSAWsfbTjhrAEPpfeU0h_4kvStpzPLH6A5pbt5bTY4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWw3_tX45NbBBOSMjokrMWHUF9_WTekqT5XxX_u-O9iluzvZPcX8KtK3dkhVmFRJM_j2kdYTwgXOspMpQIotFl7436gKKYsn1U2lx1jEtizHtstgrnxN_9asC1ywEIyVLYpzfkUxrVwT9TGCR7HuNOpl7_7OWTNVvWBqFzC3TW3_lSvy0ymy_Sf_F3Izi-HNlLGp6-FA3nv4Q6wEhChdDx3aPe0p3K4xGlZe1rS6iwcACkTbOy2DjVp8TlOXL0fMjeSckBwCZJkki4ziZJ-Ecm5hqIUscDgD__qVH-eb8LKC-vfUYMedWr3NNlKl68s6DJl7cITzK8jPbGd82Ei_rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIsro2qK9yxLw_PVMOw-AAytvLiqjxKU4JAKvcSWJTnieeQBSGRmc2MRh-hJTe4pJpbGVBoq_nI5tnpKxn_es8UFqcC0IYUFbqm-7lTcVjB_sRM-5duQt62iDXjwRpKy16Fa5q4btAqHwRLtFsPrPVYWfQ2tJi13GHVKYjMwZhYYCThmJAPQwbaU4jROdOS7BqiAjZCNLDxanyb13esEcaaFCYw3tISI_LCBzoUwZebktjqMZXwuIdTOdS4F5dA_ROXkIrfQPlO_OQkRHi5ttQXmMjUzE77xM8Az4EaZz8N76arVSGlbBsdP7HZDxAGEHHyVJIGScQdvJVrmtNiCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8oZHawMf27SUKw-Dhokq3pnHl3AF1SXUpk9DuqiJeqW68CMRpdoItSSSuqzSy7I2dxSjTKn9tyqP1sGLUSjRhT8P_Y2WDoOLrC3mcRB8GZFDNzDYHLo4Zgr5jHYHytyfs4L1_jgwrx1CJzLS5S--XrtDcMvT35bLOfeSueJaPs-ftfIgXtFk-mhWog6OarERt3bYh23GfxM2p9juf-e672uUE_zlmjo_3WThDwc45dcOsIsGk0ogpqzicOcmvkJpcl0I9PwPYe0YX2OARPEUpaunUFigj0ZCVOV-U5grj6BULiErM7ZNBr2ROLBq-DsdYXw8SwGJtg4uPmGYhiEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzp2eSBsBFs9_UreGt3Et3SIUEV5SVnDGq-alrPngj8xOcQLSP35qgn1t66cKOBxesGx_xcKMlBwTZspBuO4tSSIjwKxCKL-_WF9kpe2xZEA_oYHsCoHApJAFKZbiZAt3hk6mIItYtfO66sWBfktJ0dyBBwPKaVGHLIOtB8pNb15SHDiBwiAS20mCIKtecRPLqDvzFMU3XLh96UtG6bNBEf2BvwFVAjrEh1flgrufvvvTQz993xpLB-NBXnCW1pQfhgv7WcWYOBRfDzQAatj9vLezl88LGyZ9VjaqrqAdfpFg50iGJiILoVH0RDcU9SLeuWwYpo19uc1CmwIB0FQhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buNCGezE2OHSN-R-8sF6fStoTtSJ1HgJW25ULu5daHkg8SXwpbNPDKfT1w4qUcFMKA04GvJ70837N-0KrDmk97411SFJGF8j9NTyhNrs96gqUfMMK7WKBK3e2PvhpwM8cgFaHHlYj7sk7vefqLSnWRISYqI58m197lg7kBr6NVgrByumy9fPjbf9LDZXQsrr4zdEJXRo5QPw2nEY08twaOdqUX0w3YKqGeTFKcNoVQpMv3bkS976lds4u01cxIsMbnfNlZFJBGz1H5RVnYEUfYub-DF-kYlUCwkYS_rIBU3a-w1hp_v0ebMnnyMvhUfPwCFatuOBLoClGkHi_nat-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqnUYSBYFa2b1OH9twB5eKTv0hRyADwNjc0bTJZVdHY3enRpRjRSwwR0vzi8bsbxDj-RUu2IIoKi6nE90tMRgnBS6p87Cqf5pw1LZbLiaN3OxxnH4B6GLVXxPYTT4Lz9qIaacBLBg9zVKR9y123edIt5vHaPdJ7d03NfaiKwsWKk-jup4ktToC_cyiszwPc27hF2o1gYDIWwQwU6R0Y84qwKGDf84a5-08Iocn45JSlMcRp7j0SZ6zYmKR57UfgmX9sFRK8bbv9dA7pOMaz9rVMMkWB37xsofApCAMgA4-NNjBiMWdXlV5Q3s5FHB1SsY88xOFBLuuNaF6Rxuehfdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=iO-uaTLl09mqFHRyUHFx0yxy2o-0KyU9qxoDevevbOqtz8N0bIFNPCJtIbvhcw1q-I5VHaUiPL5kGzfw3H8FRvH3yHldj11ki6RRvI4ssDzTqSHOEQhcZBI3SQg9rVaits-fQ642tMfdyBaZbAzLkCdqEIw_x1KRuVE84_cNm2fYLItk91l5wiulGytTMEV6-cg73oA28QKWEdiC0Aanjg7SpIaUGE_wxS-TlbzA5RkF-bqyHcSOuVDwqU91UFrel6LovFKauow3wgE6CUgGuDAy_msHOfdhLxeqFEo7sIjHVaXLpuiPF7OfiybdPHjhXNKRuXwNmCs8zv5e7sTM9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=iO-uaTLl09mqFHRyUHFx0yxy2o-0KyU9qxoDevevbOqtz8N0bIFNPCJtIbvhcw1q-I5VHaUiPL5kGzfw3H8FRvH3yHldj11ki6RRvI4ssDzTqSHOEQhcZBI3SQg9rVaits-fQ642tMfdyBaZbAzLkCdqEIw_x1KRuVE84_cNm2fYLItk91l5wiulGytTMEV6-cg73oA28QKWEdiC0Aanjg7SpIaUGE_wxS-TlbzA5RkF-bqyHcSOuVDwqU91UFrel6LovFKauow3wgE6CUgGuDAy_msHOfdhLxeqFEo7sIjHVaXLpuiPF7OfiybdPHjhXNKRuXwNmCs8zv5e7sTM9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv9mBpvyl13UzrwVUJqqUqiah1HmMPcDzoA11WgrSl8O8QZw4I-SBjDrs3K5BL6QWoerrP_vyDnV_0C6way-DDx_zQa3QkQKP1uIBXBqYgdcq0r_UNGzr7Sxo-jqwJz5xFW9JE8J0rQtTAtu6qgxvP_Ckt70sLspYYbss5JjcVf3apD1zS-C_8surt8cGUmzJApFsI5Gcsn2AnVT4_95Bpuy4gNaQ-rWDuZldZp8gQZpx3aqiwhrBeVO2rkqBjUMD7WwtHavVhZcbdLfApX7ZHZG6BOvki9iIzME9u2AWfsdplGtaVb70CsqaPbREqsvmL3l9PwrnzUq4Df2Vcrtbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd63Q_8hCc2SHnlAQPKDIX8mXSGFLk5eZmA32JoCLSVF825kHdP_XcmdwK951UOMOKTbPLBQxaoNajpKCDRpcBCzQeNlIMXfCYVp6_xRfb0GV_YTE5OAoYcJxJNfCvv7UTlF9rzu1yjTExgk-jLOxj4Dzs3OrS10teqUre6SyI8y3eYcF3RRn9Hf1epIuGw-WCMq3mZ5Y4xH_VD4MuMcZ1-eU3vjexOYu7yZTB7N26mg2L8KeFFk48vrshgmQXWI6gZDlwEo_tLFgud8GC62V-cn3yvMTDtY3REagNWkcFSass0fhmBL45FNOljTYpYk_IGS0gkR49BAgpt6j61dTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5gDrpJt-yWxxosKONruXOa7aLgOjkp4SdKTLHZ9v0MSaoBZeOL5LK1_kyzqVheKDc-qHw-4tMtTIKkUHFMsIJdk_aRPBmuYenXkAE_HJMmrSchvy51dqbHhwmFViNJIe-V7wXyzR6aqXNdDE1XkQS39lXvyxg0TO8_k3JymwATldfSEbSQsovDUMQ7bs6v4YHSrD9855oL3XosnUIVD0bP3KPn3VQH0YQb0bE7Xk2G05sp9_CqhRx98-z73ecMk0DSpweWJGCieLxAajsNHujthYYbj3zkYiHzyY2Mq5uOHVUl-Ir4UzhMjkur_Rm_ofmCrzQp4OVy5ipzCqy8VxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoPJCh-j8v6QWXjm9sCsyZl1TTPr3JSYgpeWdwkA-xlj5IG4BqW4iG0IK0gcnaE2SqcwhDTuxKEbQ8GlxAyLBextYJbL7e6i7J8zM3J2YVDe0buOBMLrwYPO616Zx-6ShEix-dzdoWvePnN90PVCLyB5Pjhtj5U5Ul_cgwcT3l8FjESjh3JR5brg8OGWR9DWUCaIqfkashCcWSlPpnPeCgOemZqrSHUdq7CLIXNiARuk5B2_EaTpwZ1kwDjqBe1cieLFCmaUqqbe24Aint9Dd90qqZBYmSNnJCwXppyopn-AYDsnlatiU9Cs4FlrhQiczHkbkqDQD553vsbm0-87FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7rx6tZoMzp--6LZoBKzeojid-3nh_y_GaHp-Q9SePn5HvD-Rti_yi4urHFwtOQ9aZdOofXdEeQq7wbSQIdrOijjyc4pOU35fCLotcH4RlDg5-vLdzWKI5-qSNGOCJhONdQ161lXWZtoSWCaS93HXKRsN6vkRPcn6UMo_Df1dHdHnoY05XdgNT-saFfvXrEkDhFdNFP9dXAfBhhLlErSUwoJ2R8EHi2sS6fLoxi-ogx7d9caHK__iMmPal0c5TncGj3V3Q7w-r8qKPurTHXI19uXAd_eMiVzYGaNrL13wAw4_zzvwWf0zZQZKyjSok0FoNoeB2hjQ77XDMNW0t9ajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXBO0jbSAsCC0o-lCOfnJZhxWYR9smW0bWcuJwwMlOjxYhmKKXrK_H6pPk42kVqqtsndEsWapfG_wNQs0IEPnj_ZM7O0GQsitDcqxzEPLFHIB5sH5tvmg957EKeeY_zaeuLpXGKDB6Zj5NUGV0qj83VnDnK99jGT8VQRkaZUamV0K1UjeuBha4fiVmPAkMWa3Xp9ZCdNvJy-EqqLqcH2EACrgEGq1hXy2K_CYxm2vAil3b45FNSdVgWRTl0Bt_3pV0BUy4jylZDYOEoz15s-ZBTyWbfyUY0rUZf2rRKFW5A9m1vONAwws6P6WeClalyyjndiNkvUDLuu2h7kKXQhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-vx5opqMXTWDnj0Nfd-urd2xfu9ZJv4AgTNLT6V-WruG53DnuQnmIV8ZBciAyjVwuZERhpI5WDUTbOPLQMoaGvZITVoOUBgSFd-6itMD6ysQzdT2iiHVvnRQIvcY3KEw8IwDld1jNxVSuNRPZKVN44TB3iO6JhZnpReKOyTfkBqROZaZHjyJPBa6y3hsfGV8TuExyYOkanFsVbXUDwbEPprc1fbZ7d9I6ZAVvdVIEGq_BwyqowOPMjB2s5pCmdZUjt8YOioEnp3y51k8445Wp4-CyQ05E2pDga766dVzh2eX1nOzAYngEBYnVHmC9_C3O5XtKSZUGekDhFjtufKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZF__IysQ02c7FmfMlZw1RCuzoZoCvjDloH2N6RvEWl0bnX3EBu7TGLHfd9IS30WtX_C18NZ96NqETT62VytcimpEV48T2rlvAbCbiYsAohEyzddL5177OU8o0U0VOwLIPQIgyO17-WTa1cj1uIJCJY4NkMLPjuC2TZVZo_mWQBQezYN3jBJ7IL_b0461xxN7ZKiJ_Mk4v-wWqOO46xQIC4pgP1EmKoYZ_RK-qmYf3WHbaFmfEe2YGFBlcIfeFRmKTudLT3fFhigFkgGsTMmPVEgP6_RjGLww2E7_QuzCRBCFJQY4x-Cr5tJ7MP9DqfUNajkgbQAo5rHespyqHdKVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-Z0fTjh5AK1_DBceKSZgzAHJL_K9XLoqUvuPu9z0FE5oMYcg3tHyPXPCD2udXGBJ2glHFj357KmpA3y9aoIJsgEg3bLJC0yNEcYfsYdt-lEj0Jdlb6gkaojAMsLpHwxAMIItkNvdJBLTFVF_ahvQg7huo3lxZ6txuzLW-jICMiSiwmaJu_JIZN8PO-Mpz0kT5pBj3h6br4fBrzmhArxvYYLIsTSvTJdtdKyhFlHgEXW1T8reCzg-pjQct67A8A_nUMQDzkCQoL9E7b7hXRd5S_6MqbHJlKJsctO1K8TRgD9ITYjmjgiIxLa18n2IM3hc3JMoVYcRsd-T1IsP6thsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrTTodyoYeIkTBlO6WVV5PLh76eoztxWDDXrEcNGIPJpBB9KnfePJ-TXS1zobHhAA-9D_Mkj2mw8Ql-JmluyYMdwzzQU6PiG88PpoyoyeY_R5q154kppkCxGNSyiNEFo8rXP-gM_V9qEWCFzuTGGRcx-dY3aCBhRfrVMpzIvlEqg5gNwYikBnSwL04dDJ5ApWKaO2aA-7nN7D5pM7YsfnWoRw1eNvE6lHryfQTgwL9qilKFf4x6pJG46-rZ8uB_JUOe13zuWK6KAW2ybXZGYaAPv3xC6UHlrb_bpWiSgPVNdbM184qzljAQmXViL6ZXbpQnuP1lPoF4kH0Erm3ycCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLcYnROkPu8-DFw9pX_AhUDMKiW0GN5vCNw04WClJuEco2caUL1CW-ZT3jLb_sl41tp_0DwaXPyLjNzZZ79Qpc71pnUZS5kIBNgacpXuV59oFoFBO5dzwqhtWZrWFmggHnM83hjzE_sud3q05-NroZDYM9jqRefQjPYb-Pd2INFmwDfJY5DQtILE-3OtNSi-m4FpCJ76rUjxPQaoSLafW34JIZ69PbVumpAcn6Yx41aV8cruuupCqdjaUGB9zSn0YmNTgDI5sRuCmxM71-hgw0RlIEXucJzOi6ZjaeC0Zi-waGkg-rk3b_SvrFLlr7f1FHwvqIfynyOOExePCk5g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sla3mQmsVSq-QvsHjCbjVurUGVLz1v0-Ffq-UwWK3GgSqTYVHhvvUuZoY0lPADzx_g2mDCiTejuG-iJe1p9HadiyvsRrCOrqPjfQMdCxNx9pPV0CeWsVoorqwJqnzsxGEZh_mfdY1UdxXV30q44MMSmtqTqz9xETRJQ88EtwHSCVb7qL5Q9Mvx8TmJHiBJm_v6-RrTdzwUQ2aAq5el9AD4ON0FjUK87PN1v4VXMYcocwa6tFhrx-ceUPCwRVrdA5jeAgo_4leWFFEOmlZhFDxu1mui56GiSliO6SuCnBdJDGTUIzOSdlKA11X2hty0--SnUb7Z4RTh3XUQNLE3rwSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SaDKqbGiO74aVYSor3mSXraAttBifOgBXHfYlNns7MFd3EaK6pYAAJTPtwTmuDoNohfzf0hvEQ1UabrOGMSHuzRG7frGQrhMkcp4YFX-_fMQ-XDRaL8EwnXjjW-yS9pYZGu1rh9DG2og-9SYK74yW55rr75895mjS8TwU8K6xHlqsLGctUf07Eiye9DNhRTqfsPb0HbhUxMzHAWUJxUn_6uIuT252S6r8nzpAcb0DI7PHwyeheqkA9H7k0qADsNlbqLifUFNfx7cUlJrfY6hvE5ElK1BmwcWKtSd342GKgc1z94ZBnaXf1bxm_YtiCL8B_Fo2oDeM6gPgtHSLv5CBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SaDKqbGiO74aVYSor3mSXraAttBifOgBXHfYlNns7MFd3EaK6pYAAJTPtwTmuDoNohfzf0hvEQ1UabrOGMSHuzRG7frGQrhMkcp4YFX-_fMQ-XDRaL8EwnXjjW-yS9pYZGu1rh9DG2og-9SYK74yW55rr75895mjS8TwU8K6xHlqsLGctUf07Eiye9DNhRTqfsPb0HbhUxMzHAWUJxUn_6uIuT252S6r8nzpAcb0DI7PHwyeheqkA9H7k0qADsNlbqLifUFNfx7cUlJrfY6hvE5ElK1BmwcWKtSd342GKgc1z94ZBnaXf1bxm_YtiCL8B_Fo2oDeM6gPgtHSLv5CBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJk4MSIF4ZoeMThjIbAyyXRWF5EthVntnENvasJ-IenrlnXa0pFw5mD6QfUSlm8C96x9CvNlho-QQ4YBVxAdpuShJRborM6lwfS-p5OOz-do7CkGR5WAppPnXzD4WWQADBIPW6a9PdlAaun2n3gF2D46NDeHKx9V4M8u_h_YBzUqohYWG3xSzSqTfMWx1zEEVqKsreu6zks9q5w-pLBjEknhp4o-J5a18vZRQ1Rs6glVS9lcY0G5MyFahZSSsm5mMpWIWpsl611Hvc1FlHlhMDKYDqyouidW9SBgFQBaytewULLUmWlTwJPLgyEZQE2iEd-kAoITO2Oclq_CWgTyBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv52eQTkHiFtgurJHYUNCHp9exClGtTRVwkdzCeODs7DDCKU3Hu-VzpPkBfGAvH6wjMhamjlN3ftJGFMUcS0L1oMkZG4fvPwfbh8bq5SoSGo7Sue5nQsn8xEkFL8YXbJnwVGAeDfDLulyV4V5ZTWX5OWPicm74uPU4XJQNowa2YxhcZI7NzIFwi373rqNQO26YnWVYQYIEEQRbcYyFPmdbwvhsiQYZlL12TQ_nezq6HPqaYl_TQEpeTueedXTAyuqDKXP-ZjGPoRJoEuR_2NwGVO4ghSErzSkgxkQ8K2ehBBHubt8bGvo0v0eddqfzPsH0MLk7Gf8xsa2ImT_JRJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzF6-7jy4tOmHWXZqOOgrcLX7dwrqn5UrOOlMa91eldAiuIyHD8YuVUPLbmHKLTMr6lC-tJlK5XEBk7poN8pOyfmcyLiXzHvNqeMTeCuwdCDNXjgwnaGMBvG7lBKOh40R7CI--OR33OBHSODo6ffVN1a4NcNm_50FDNcwjUVQeqz4grKbXtenA5ze68gCioWYpDNxQpNK8GvVL5Z0zw0QYxcgyNl_OTqkbcq26WzZyE-KPbT_SUGGlfyWMBwudMqb2aurTS-Aoxq6INNncyxTUivfJSrSVF29M-R9g-DT8PRm79ioDVR3wbJ09yikZ8c6gsUqZYCXQNBhtfaOXXgjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsE9FNhX4nPI4MZfxgcHwnOsS-31ZtteQWO0LCHpc4P0X8qDFH9Pl68i4CMQP-6ql9gM9Jc2tPfgHvYpNbKTWq2UzRbNZNLUooA8po8xWZV1lrdmZcj3WCnxB-uPsxhBHdVt65-RJhGq-ol8mhZZl-O4V5by_2l2MQkMzAZh--KXERP_TvQgh1rjZ-bZODRsvIx3qrb2vs1mNx1AY7BBKOWu-otnmGX4z1JPkMn_wz2XXzAlV-lLChVP-gk3gRKHew-Jp7z3DjBcrtZls-KaX55BKJ8-ksP8PbmUPCbBfnqOY1eF8WFafIYgSB1Mta_ZMs9uhUW1gjypbHPRakYHpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzm0ACEXGW6rhJs2AXY5DS7g48NuRX0QH4XSMk5dJZwI-z2bVWmBqmUQTpvHtqCNQLLHWx8vfxrZjFjHX8yc51axvd9TekVrfSmfs7Jjzo7W7_gP3K6pKmBHyNlNvGjrWyPE6pVAhiVjZ92QgRrkfbBJeCtkOJlZfJxe03wb_SPF-5gnXvKOmA6K6DgJx5xnZG43dg-N2zsjE-9x17atK6qFquyjEaWkv7-hX0BWpN_nbNtfPLi4sPhsZ8pYY3hbCgjemR7R6NqjPeMXW65WjvzRBMzP9IwAfvO15VI5T2BQYbp6yxrBDxZoOcJ8wDIq-YTDsnZdLTgC_VS7Dn5cXPro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzm0ACEXGW6rhJs2AXY5DS7g48NuRX0QH4XSMk5dJZwI-z2bVWmBqmUQTpvHtqCNQLLHWx8vfxrZjFjHX8yc51axvd9TekVrfSmfs7Jjzo7W7_gP3K6pKmBHyNlNvGjrWyPE6pVAhiVjZ92QgRrkfbBJeCtkOJlZfJxe03wb_SPF-5gnXvKOmA6K6DgJx5xnZG43dg-N2zsjE-9x17atK6qFquyjEaWkv7-hX0BWpN_nbNtfPLi4sPhsZ8pYY3hbCgjemR7R6NqjPeMXW65WjvzRBMzP9IwAfvO15VI5T2BQYbp6yxrBDxZoOcJ8wDIq-YTDsnZdLTgC_VS7Dn5cXPro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBxxC110nH05By0gyRXJ3Xy-dNbdTOdkyZK06qinOlHH9hThiE7DKNa62LmgpAOy5Bj0wZf0hKcpeIQ5HRFEH2LUnaOPI03cbJ87FkBaxPASQ71hjJGV2-Cr8YBPzfFcs7XeoGVP6ncqiXQbkTPJPXhpSgbrLKnTSKk1ZUPwH4vpl5fSsEvff62MpiWmnJLhxXK_uHrtNuQt8GKlmxAoabRWM_0afzZ3Dtaz72JQUs-ue3zJAc7zNU9H1OJGfstArUggxfw0sN_eV6hr7XzQTXZ-HyEQcC9GT7vefJG4cj-7881DS9PnZK_5IWsJNB6whIqLMcoPcKO1FFn54yePGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
