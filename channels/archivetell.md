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
<img src="https://cdn4.telesco.pe/file/vtDjpBUpSU3-Sm_lSVunraY5esT5S22DAN_PMpLTUvJYRhGQBL09ztViWMmeVhubEPJRg7mgM1ceOhPXiz9rO8Nt8TVxNdpLM_PGlVmphLNMHb9zXEvVSy7fXy3crB20rLdcCy3_LFz3ksnpJAkHRMOaV6sfZK6rDJaDPIVJ7wWiBOTZuBLD7_yo3H2S6Tq-E7ukBS-MFF_1rSIxuKWJFCB6xkxRr9qa31k5V998JbKfayIdaI5qoDbAn6s5eUuFByd85DeKoXixlE_ICHwEBWOwobHAJZsp3nMnAH9UI3-lTflO45qRnxt8oMwsSrEYbWaERxibKgSCInkB1PiHpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.59K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6cLgwyKW1GHk0WgbqAwyJlkWPRodzl9L0HSTc7SJvxSR-CIghPdRR099aA-LZ3XjVkx03WkIj0yQl7QrQoO-Ytf6OdzfQUYnecN4E804T0xYoKEib3pRYnxDqgptnIVdN56sUY5jhAqOIki_3W0yorfL5xXe10XxjOk5STTw8UbIPSo5LgLziSOlgaDbopQJPfi2HKNmy0NsygYG4Z0XAKycRfwSufHvNhc1RGcthmgpEL0if7LPNX6P0f4ZsaRYIoADPi4-gHY53nhOJiCQ2pZMsms_rbfPvdiUh68R9eKHSRphE8kZP0IRckOTdqW93pAfg6gOgbbVTTsTJrd9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 671 · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 743 · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 971 · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=XqGZvlUOu-BgUT6yzJ2UFX4rOnBHgqL4eXQREb692hoFBgmQcHcgD5KBCTvXFm7eNzg69bztKISrETD9WJTXBpXMQ3KdS8x0lSJjB2_8cloxFVPFVQx1LnXIANqylwfmSCsmriFewfgowx9f22d3yVb5LRGqqbTnB15dUlElADNpqE1pi-EQ7KHLq3tI3OPc-sLg-PCmjO6MLweA6aK83rag-1RjICEgCn3Zk2xCGVhJgjzcVgJqUXNHGVtlAaPhBUiw8ACB1xgZJmPz7mfa3O1RWTmODJeBbej_0qpClycWvueTbZIZx6GELySWRy9pDib4zvY0PkNwiYpdE04dOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=XqGZvlUOu-BgUT6yzJ2UFX4rOnBHgqL4eXQREb692hoFBgmQcHcgD5KBCTvXFm7eNzg69bztKISrETD9WJTXBpXMQ3KdS8x0lSJjB2_8cloxFVPFVQx1LnXIANqylwfmSCsmriFewfgowx9f22d3yVb5LRGqqbTnB15dUlElADNpqE1pi-EQ7KHLq3tI3OPc-sLg-PCmjO6MLweA6aK83rag-1RjICEgCn3Zk2xCGVhJgjzcVgJqUXNHGVtlAaPhBUiw8ACB1xgZJmPz7mfa3O1RWTmODJeBbej_0qpClycWvueTbZIZx6GELySWRy9pDib4zvY0PkNwiYpdE04dOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyFbuYYHCk4Y02zqUd65LOCJWF4nHiSaDjKOh3NuCw0gZp3vlmvP7F8PNeM1L7IM-DffbPHFzQUzd-DLUj9R1M-SDUzYVDtEzou1Hd69yGrFDbkkz9znvDyn08Qpk8lA6Q3HgBRH7EIFVkLFZDN-jOw5P37BaqYAW6e9qd5nPH05v15cI4E_xq-4TZALqGQTUHH7yukwfTha5sU0xN9FKuQKksRkxwk81m-ywtB0f5W2gCGJsDqMWzJbMcSV1tB2w0yu_paAJXRxVxPoqVOnVDgcGH23JUBIaWPjZgMnSVGcACtNQUNNnVLrb_AIpieboNSxQ365Mh-EsZSd0wukJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C81-BqqjwKobxUFPXJDlB4nws0cbZfu5DPJPvRITTw4rRfE1pPnRjGocUgWnm1CxlMMS-2Aq4Qy7icq-dDBR1n3s3HJ12xgkSPAyRdhLNPwc57JP4qfiZNX1RTujNiISt87jgDP7BGFjx0zu4ofkJB31yQIdphA3i6HgSm4I0h2jX8nZ8Gl54t8J4Q5JEf3YBZweDOtGDxW28wA0dYx886BE8yu0jTwJu21hA_oBZTA6jE908IMcjYMxCQ7gi91xqMrxWmdkoN05h-s44qPtwS1Bei_vZ2YNo9KIdSlJipV21pAb0h6ygHigyNXKVLfyF4_bxz6tz6Lo0SG5j69fTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuEkLOjH1QKG_kjA0DVOf2mmyvQCTShb6Sm13VD_wANa2cjXs-HrFw6SbQ2MI_7rgyIlecY6ClcwjgOyStwKuk0RLJA1qGKkaUxaAXCfQ4fWpxS4elGaX-rfIQy3mOyc5UUAqEMvW5YcU_T7pgoanoNqq7JejzcFTmVZVKD4DBqURm0JrLqzlKRmeemlXl_Rv7jwPlIjfTdW2OkuSSAc5_cjdctczZEVxwfRmWmZr_iVR7FwxCuB7xeBRP-Gce9yy_-3mSKbeMaITId9CEWvm_QeTKdYtTmrxyIANqT9LLSa_yycAf20F6_TsWm7IcHTI4bQZXu_HefNT0hB0-Sm6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVtAbYwAK6ZcLrq2KavtGsR5oQwlD4dDASrDoZ2vDuNSwE07-KyzCVxaT1bb16B_CiwtaDMDecFK1XVJ6LpssO0Qo0NMGWbfxDhbF23r8PqonzMj1I7Qu1O1ON7XBNRU5FxuPbM5iooBP2BsnLO2gx9EXCcSf6w83Zsfj6A3ylN0cWon1mqDkwSZ18ZnhsTyemCcFDJ8xyjKY84T5ZPTgOJldMcfAbpI_-aeQoCIlJePjloSZNQ1BUMcGo7vRpw-C-X2AkCNYNUv260P6r5gUxfxRbt2tYMWDUe7DCRG2_hV7QxluhCHFv3PJhdS1--Pf0-dPO2Mpoub7VcqGGYgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=D-tQno1-iaubkB7mgMrNrxwCcWcmPsFgNEKfWEKfycfJZFAxpUNVzDqzKAXyC1fqfyORMrX-KM2AOh3xBV_qicj3xIUKvIFaVaLiRjTdYFrj4FGZnR17bQNJgYt_0K5Jm_LdUWPBCZAdnAf8JpSEIp4Loskf63Ao45XbVbkH9oa10l9ZliM0cpkm-uOf6j1cOeQC9NPb2Uj0n0f0PW8vgws74NBmt3iBlDzUMsanZZ9ZMPEIdMy_agnJX9QQBGWQ_UBb-uwPnklBHtFRaPaY-dWSgcVH-za3Nhl-5QQGtvU2EWLmPjbPG1Sgnjcb1fbVbUg069z6nZLr6DB8dqirwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=D-tQno1-iaubkB7mgMrNrxwCcWcmPsFgNEKfWEKfycfJZFAxpUNVzDqzKAXyC1fqfyORMrX-KM2AOh3xBV_qicj3xIUKvIFaVaLiRjTdYFrj4FGZnR17bQNJgYt_0K5Jm_LdUWPBCZAdnAf8JpSEIp4Loskf63Ao45XbVbkH9oa10l9ZliM0cpkm-uOf6j1cOeQC9NPb2Uj0n0f0PW8vgws74NBmt3iBlDzUMsanZZ9ZMPEIdMy_agnJX9QQBGWQ_UBb-uwPnklBHtFRaPaY-dWSgcVH-za3Nhl-5QQGtvU2EWLmPjbPG1Sgnjcb1fbVbUg069z6nZLr6DB8dqirwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=ESVnmKFdydTNTCy2LqiiBIDqsCMQ5wmPCa9S8ZAA5IpY1elZNDvDR9B_sH0o4i3dL85Kd1kJ8YLFEyIkne68LAMc6J8phmNOry3l_6KT9nMB6437PmugFDBRtgCuxsuPBgOnPHFfE9mvT9XYMLBy3SRNym3dmNV4EKw-ylqMW-MAB7gpd7R_04hvIFVuG9qjADRoLFrnf_mq1j0tvUcGicJWLQmfppWezqFl4oBiZzVvH66CRFUHOH2haBAqgPVqW4DOwwjxNYsutgFZG2MWgAj19yyKLtWLxN9nnZLfrUTFhly6vym6yKGU38UjUv644S0C8Y5_3mXLe9HHYzMp7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=ESVnmKFdydTNTCy2LqiiBIDqsCMQ5wmPCa9S8ZAA5IpY1elZNDvDR9B_sH0o4i3dL85Kd1kJ8YLFEyIkne68LAMc6J8phmNOry3l_6KT9nMB6437PmugFDBRtgCuxsuPBgOnPHFfE9mvT9XYMLBy3SRNym3dmNV4EKw-ylqMW-MAB7gpd7R_04hvIFVuG9qjADRoLFrnf_mq1j0tvUcGicJWLQmfppWezqFl4oBiZzVvH66CRFUHOH2haBAqgPVqW4DOwwjxNYsutgFZG2MWgAj19yyKLtWLxN9nnZLfrUTFhly6vym6yKGU38UjUv644S0C8Y5_3mXLe9HHYzMp7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2XClQMolopTf-OA2EsxlK7M2gXUoATMKUJhKIaLQgft0uUWut31DR1MxYlY8bcykET7aPg5BvSOEZTifjmdu7TilIE7Kb-aBJm7B-0hKqRfS6FVKkL1m5iH9YeQZJRwoYgiqtUEHlEHFRDfZmOFcrzVCBoEt9RCohllJ2dkASZ6oZveJKhuJ7X8ZGsSEwhNeBpfS4K7aHq9BgT-LuG_dRCUPcnQwJOhoSEpUJjcA03lc2C_cLGT1O1vRp5AyuzyRdVVqBrgRSxfejZQEhAUHFemz8tGFgHsWDDgZ0q96ZnheaUTZ9lX0WfPBcfL8VAljPZmGhHrxaYIHX89MIShTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=aCR7aF-_Jih1eHY0g1LNCZYsbMBq-QKUZw-y6Vaa-I76ORAW34C5hX_td74iVZ5bfV2H88HeAZ_luvpbTbjCCNEyyV1qfhVd__5l3-GxTVCtXw4PRu641bIoG8oEVyaQbODSdycIfDz41GTd_TnvVJPgf7k-9MbwbJo9PUp-N_lp_KJ5mDRdPWU6EIbtkz5aXaHWHY4iSSoL8MtxwJ1r6DgKtHh1Hc-cqYgsARJZ97hmipQc2wa73-fJ0BFEqZZIfGpfkS9u5fm7gRxiXkBzxX37uJGUBFtgpEJNSp2HVbU8Hmb7E6GNKvJ4EZR9OgAN8IK1LtWElvY0sskkQoj0nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=aCR7aF-_Jih1eHY0g1LNCZYsbMBq-QKUZw-y6Vaa-I76ORAW34C5hX_td74iVZ5bfV2H88HeAZ_luvpbTbjCCNEyyV1qfhVd__5l3-GxTVCtXw4PRu641bIoG8oEVyaQbODSdycIfDz41GTd_TnvVJPgf7k-9MbwbJo9PUp-N_lp_KJ5mDRdPWU6EIbtkz5aXaHWHY4iSSoL8MtxwJ1r6DgKtHh1Hc-cqYgsARJZ97hmipQc2wa73-fJ0BFEqZZIfGpfkS9u5fm7gRxiXkBzxX37uJGUBFtgpEJNSp2HVbU8Hmb7E6GNKvJ4EZR9OgAN8IK1LtWElvY0sskkQoj0nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geFraDJAPZuVHPq3e8Lymqqcb3mEtnLasl9D8QJZ-BuQLUN_cfjeRDtmIcwaRPxJB6ZiETMC7pZzFM0NgSnEOHUF62xuI05bcIlQb_tCqmpJcM-HJztoc6fmPGKFPcx5TrJWtztabTxiGnLnADZx2FSy8F0HbyoKxD1DR4VCeQTQyqNgUMbK8HWttAB5xHV1FkCIZMrrflTfaCVJQzPT23Fq-ncuh25D2axkoW3k_EWiJ5_GNAdDFb931jDqgMdSMyIZ79_3-RQs7GKRctGWyT7oFGVV85jrUMq8k7lSEPmXfijry-2DyD27XeRsGhRzcrHz6fq35xAK6olWdpDokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNWIReXGISBYdM7ob_0ICkAI0JhsncAlS0abecUSSOOXuX1EmtXlBx0OPkJ2Efkr49YXrpBsKYn-ZJamRMOJGt2o9I3B6schFWbnHgJtdVvQzg_p3SJjRY9bmjmZmI3yA11OS0V3ECwnBzjOfeNQe36AZdqjdQ2oSbUI_W84IOMJh_lGXW0Fxg8DPZKUu5pXQ8lBdoVVrWzVMFraTwsWL1AKkrNNjMR3nxLMLjqOy5h54DUSe-leEU2eb_a40BakNra9187QZH6Tq34LYL9oCWTzaYVmVHeR__8SlPfF8dL2aewQoYiHm0fbOwxj4bAXyIQ8xZbgcSuTY5Z5iGCMqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpBi09qT7MMnHvvKymsLpvivKi6ys_3DmaKrmpEurHtoXpO0yGdaTr0haSyddpKMEnHtpauefkouSazjNptMnBqQ3h35cIXELzO3_CjcaWYLyr_MtbCswDH-D0-Udkjn_uwTqB3S49-mAMTA2Jl3IIvpsfkFFH64U2REHi9Nqu0LUGyTcvz5z6cy3tJxYg7DJRGQ8N2pipd4Uz2XA12nAPMyX_NBsEB-NuhYKf6L2ZdCkBSJuzllighndLuY8IRU3ZVkhDna6yImwxDyc0umM2SZiQmVgEqKb_UkAm3AbfeVnM3yavVoeO12x0tXK2PUewF2uP07xjxlU8B6uxp7XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzPdef2_9MzomOtGH21D01Zx31PHU1ZyE5ELTxPSfVVRbQwlHzcEoc2HbK_6_nNyeaQSrjCjjb4TQG-O26RjtlVbqU0HsnMYMhN6jAS8ZnYOqT2Cui2ZL3bjmmqRQx3Buf4w6NcLBZWCselQ9Vs4WorEfvZGCorYvkwhjjUeUblAb3gCST2W2MS1NZ1xBV-RxzbpVbUXRI7tWFcajCOdfXNC70z2AFfmCD9a3xry5ATsNp4sio3xsXmGtHa_0Ok06ZEtPqNRXN_6RzbFPbVnUHyDvx2x73DNbxCTp75LsVOOB1qLIdDHptua19M9_eRpAJf_OiNgY-DSJ5iLTBHjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=DLcHDd0lcv5DqS3k5nRHh6nWpPaSfXUgcytfhPCrrwr31Wnkz8grnwRl7kG4EC1M0P8yHBwz7Fs8-q9BokDTcO4i1J0OgjUaPKIAiuliuE-Owg6kC0zR-1ZdvlQF8E1Y0Iy6Pz5AQbS1pvUkBm273LqbY1qo3g1gcaqttjBZ3L_gNAA3HJx6qQhKCY6KH2fnSZBa2lGwrHH9K1cFZLvSTmLWQ5P5Hoo77Zc4f1iwVFuEVryjz0l2gM4IzoibnFfSIRzbuNe4HGFcD_xf7UwYWuzGGG_AdjSwXfD3uM-Kz_8ZQIkeW5Ud6N7G8w2MUWcMa9vLVDsRJUgblMZdfUAt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=DLcHDd0lcv5DqS3k5nRHh6nWpPaSfXUgcytfhPCrrwr31Wnkz8grnwRl7kG4EC1M0P8yHBwz7Fs8-q9BokDTcO4i1J0OgjUaPKIAiuliuE-Owg6kC0zR-1ZdvlQF8E1Y0Iy6Pz5AQbS1pvUkBm273LqbY1qo3g1gcaqttjBZ3L_gNAA3HJx6qQhKCY6KH2fnSZBa2lGwrHH9K1cFZLvSTmLWQ5P5Hoo77Zc4f1iwVFuEVryjz0l2gM4IzoibnFfSIRzbuNe4HGFcD_xf7UwYWuzGGG_AdjSwXfD3uM-Kz_8ZQIkeW5Ud6N7G8w2MUWcMa9vLVDsRJUgblMZdfUAt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB0Ew2-1xx0mbhVXCiVBwhbTG2VLCVoRbRB--NHNj7VX4QvEiEmpFKfGIYFLt3VS2V9s_4sh1npvmxE5BmEd7_JvA6zeAUzEPQ10iuGLkSG3KiYKf--lkxpPG4jISrDg9ds18WEG30w0bU15Tmm2viNmLYsVHxiBD86Vqbyd2JmIMa8XFzTDJqQZFaRBQrtQqi04hSDIYLW3Kh4ZRysOf4gVb6bRVZxHi3OUfC020xhkT7NtvVnIncF5rWhXjCCzupno66vgQTls-G2WcUYVdZkYHmikDn4f9SoWXKCNSev6e3aiv9I5KdVW_SlrOOYb7eqXX3ZSTHMdPQE0IAV6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sk8eH5KG1MO9fP_Ju2KTGOHJF94P9j8ULnlwhzn3rRoWmU9W5oxV7ifFn8XoOlMM6oZQoG5uPGRQimy3gibTM-ce9AlUBr1r0lsuCGOSPugOF__OZ01xRBa2gH11_85fo5wtf7J3KzhvDWAGRvo6xUdBcwSxjpgvhUoYWxbmrRe8huFRnh4wi11dmtBYHNnrv6bSQG2Ze_4M5_QMYCbhJNzP8KlxfDK8h_uHuYabH8hbWUO0nKnMxBxWYcvmljrmlBqcmMO9VUUwJh85Ib-zULRr5NmYQLn51rv6_QgLtlKMnvuQxvFkUxjwJtx6zRTM3C6U3RAleGQD5GxW5cqCJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-OJREuht7OQhbDWk6N4xnLrS26267899A6Tf6r7g0e_VmiLZ3lD0eDtN8SyZeWm5d7BUoSYEQCwib2sOWECl7maKT8JKSr_6U6Lm4Ux-7fJWLYW8QzhJjRA4qoMn95dRXXitHF81pVhmA-JxaLLj1EjBl0zwiVBy3fP8cA17hdzl9MaIV7thmb8AIeoEFHSnlEbfJ1wPTQedEFB6imaI3QsriXfrlSFqg9705O-sgg4H1KcNUaxM9o7DDiS7_Mv-yy3rQv91HlJQMgwZxeb0KLpgiemJDFjayAH8MNgZEacU_JORG8KbCGB-qtmZyQuPC89afkniWprxEQELW-hsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTLGp9T5K1K3cY_clrFZzGslXye5CBGhxiUADCnT3iCGHlfHQVPJseysEQ4s-viwe8GVenuozLXERUF7dGNTU_9oEhE-4qKAXt5a3h5t9R_Rpx-uFdQsDFBymtC-tuCxYuaeGs7IF1mVc48CJ3st41IvnaRMJCqfy-K-0svcPIYi60E1hNBwcc5CcI55ak-gWzKlTPEa_2pFaac756l55XNG8jXh00KXERQgutzC46GMv0qqyU3vGSCTnmpIqjDy-7VJBudGCnwnihmCF3y7-gMaXU3op_cMwzjXtW8oGYv5O192mnJpYL3hDd5Ey8NCxm-Gp19EPCJwWJXktCRE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9uC601vOGDRw45dBznf5Fx4ou_qoBn5AO3s_1OiqmycU6Z66czJuGpcYhv5niWPS2dMSlfJBLGlPTZhWjxuwGnu8BZKW7RXDQS-5nCYSqLHn8PksMk6eiD5-jaXjS4KVns3F3GlZuiQD0hg5t0NYAZry8rmSQNusdaPeHe8KCgpFomRWNar5AMvO_z1fT1VDKmAsiyCIvgYbOcSrzH_t2xZ4as0fk8wwPqpBtnSZL-Yf1IGtG7ph1hM2ZVMTOB10oYMqdhF40_tmyMW8NKCAJtY1TuoSRzX6lmzok8Mw7HbwFsuw8AgF9WCqG-FkLr-2llJ1be4rOcWbH2aVCH3fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeOwDWkdWXQ33D-VT9guWslAAtOEOPLfMxTNbKMZyqqHdBKtanpVh8q_C6DIiM06ji7U3bPXmICJaJb9FhoV_aYUkIZwewDr7t0v0dOIw9QI5WXD2n99GPaLWGUYzaqAI4jSuUYEG2lsI2Dtdj0xRQtEZ1hSl_xyia32KiDlXsV2zsiOPpLBYLRVlsTpERTGV_lHtc_O7tI7RpNTzcURjf6Yn1ewf6gmCDXpYJbLdb6CwkFNixehGMNlTM04Jw_9vvrJW_Rnwq2N8F6-P800FBzpvQzDHYdwO4W9kWCgDkQm0cRotgIXUfjfLqH9Dje92B-fX_cxilMTuYQmJgwPsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYB-aLjZJHJXR29ex2ZhOch0U_o-F0EWpqrGqfJnv1Nclc4cRIA2vczugXqhGXbvvbt8k6NzK7lQnntAePctA8ShPBBXuiqU0YGEdn6hXtln1VoEgJr_BrIkUfmf1osu8l9YiFNsC0wQ5lfcV4OU-0PgnvKfpsPafMn3StloN28pig5rszg8Rgg1prheoHsilmyGklbBApk_0UWwwHK846-EaQuTZCmhucYIetH1CXtSD7rMkue3krvyeSp9T71-H0YLRs4VXeUDiRUKtmzCowSOA1be_H7HQxoDoO1TDcFB1nqDP6Fx4rBBj0Zz1t5BzLPjfQliE0Tu_saAB7hrEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=pkd7sIwo6CPMVG0b6rlctoKUtLLY3TRl4xxJ9Q_XBof7qkOL5d5-y9BvYYtTvsBNm7GiSN6GZEv6ZCowH6pzQRMMmM3luxIF15jz8tx1lqP9gF6BJTpG_9c0T6TYsJ5TySUzwHb6PXfhdCTy6Q6og2X8gNVUluF-qq83KbfeEgmF8wdL1C8JuxwLm8XLZuD5_5OliRuQiKBr0oAsAC-X21cJ_iCIn2Z1tl5Laps1n8sZdsiGq_Kr_-Wf2M6dUT-fH6qT5SHGvOvl49bHYAvm1GwpUDS8AP6JG4a6jcBMkDt9OOCYYV0L1KhACcjeXs9lu0q7d62HLqcpW5F9_MQCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=pkd7sIwo6CPMVG0b6rlctoKUtLLY3TRl4xxJ9Q_XBof7qkOL5d5-y9BvYYtTvsBNm7GiSN6GZEv6ZCowH6pzQRMMmM3luxIF15jz8tx1lqP9gF6BJTpG_9c0T6TYsJ5TySUzwHb6PXfhdCTy6Q6og2X8gNVUluF-qq83KbfeEgmF8wdL1C8JuxwLm8XLZuD5_5OliRuQiKBr0oAsAC-X21cJ_iCIn2Z1tl5Laps1n8sZdsiGq_Kr_-Wf2M6dUT-fH6qT5SHGvOvl49bHYAvm1GwpUDS8AP6JG4a6jcBMkDt9OOCYYV0L1KhACcjeXs9lu0q7d62HLqcpW5F9_MQCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCFK5FtPMDwadPa9MIcZGCD6eE9T6raw2OH_EZT4qkCfK11RWxOTgg9ZgoJkLQ1Ia0afYWOte2dzgFl1PndrT9tIXTGZpZpmnUCjDBk-4J0PA5_nJ9XV_hg3eKMAxtH2Sw-p_rkpNNXOdIS9Sxh1PJE3HKgyogWR2QpH2CNClHH_sS7FsWsxQA8GMo64k3TAf0qzKJdF-3ZtQvIG0VOt6G6CvVnJanQLjSIlvcxR9D_lw7AZRE0vjLQSBBDp_J_Uc2C-A1nuaWNUuB5av7g3xUSMvR0o-jKWpLMn91mDCNIJkXeYZ--ugyn14zXLE_lnl99jc08YGbO5rdoFgsTdBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3HgI0dLM_A8WZzQ2OsDNE2orsjtgqu2Rr6hAapb8mD0JgJAC-zaO9dZZ_N8GqmuFkQamBdpdBa2z1oiXFTZkOnzXIVVS3AX2BdU548jFNytCEtx3QVt5v8KLEn6vk9BMBQ5TQrw3vyhu5I0H-nwRs-MwUfXZJM7AiVFO2wrTS5UOCcQ4zIBiAErmIYPTRd5R_GFGlfE5ybqHp3Xj63mi4bIhFgxLj5E-RvV6B3TfYg-eG5G7HyupzZPev_sDSmwM_nM8JNSvKIaQsXy70uWA1nICmjQ0PyFzYay5nrcDjL1nnOaZRLArK9049w8VoPggjqZRuK-XQJ5eSXuBQnwYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtCXOmdRW_uyS_SLsjUTQls8q8g7LyxJY1x_AQrpJhX9EDb6-5f7bqD_ualNHpcN1ApmEOiAcLAQF-qeUrYpnwBhOgFgWY6JY7WAInzaHnA5CqAlm5aNaOUA8R-S8lnqPdwlb4hM7Aze6AeVVfLHRah7JUy9DyIZPczIVf03I24L3E7pn3HSc5n4sG8ZRhFwhISw-TsWlO0svDk13IRdamnBk81CMIr4OAj_dIX1yzfT_dYooFrCS33Ry51uzLe583SM4lO-NJPeeWdOa4P-hZZayrzzgnEAt8lSujlqI6ZwsO-KT_oj1Lzp7hWFHniLE_7rLDXkwBt7S-I_56xKQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuTzUujW8ks3WXjU0nRRrvjrJiw_5boPLipHA4qavYxRjGdzj-_XCe8vQoLxiNkyG4hc3ndZtaiI_i1IQNxwQgPGx_XrVxlji3Lfn-oCHv9OBRqOvoQQU_SoWoMzirg58ZjD23FeFATz5qqA-VB6vefJHzRkw2AUUUnQ84h1iC5q96810v0btfdHXzRVoOjNZ5fQlkHUk9Dm8qJRsrZ_EceEeRb3Rj16_-42sKh6gcGEF0xVqBrEIWamRdOpicwjMCrvfGsHps9cHpsuhDn0YhG4XrBNYju8uwGkHWmvhghXFCX-sfEWlzZV-4pXyK__jpPqm1uydiJjI-DIyIlkfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-WkgXvtkbxhy0pxl5iZS319ltHsFZ7ZB-6uvPOdtyfRuZ8YofURJSll2JNO9FSuY1Sin0nmpeUIxznF6qc4hFaoTYpg80W5ykwJ0ZUavc3dgze46Th8LNTeeOTdS5v9C4aqdoI-2dSFiAe-EIVjpJoCUnbHps33OoaPMti_diOa3ZcdzOh1wrxV5zEneJnLAjopSlmBFsVEwM74O00R-vjPZbyF7ILuimw98rmdeT3LLbXUDjTYSwk0XSDhl9ud5YCfxkRPPY85p21yP5M_5T_Jq97zIAvXOwGnjPWt_k52Nhni_b39HeVgIUNFqX9oeDcX70esJyj1yq9UFf3vPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPmdIRXQ3IHI9eW0pqOPsmauKIcm6QV0ELJEJVPKTPmj3L71JTEkEE6sJKi9KWhfTI79ZorXnud5g841My3cTMM4kF5TVKdRrmjNEhzt_mmb3y07Sb_w9nnq4SJyPwsQoXMCnESaqLfggDCE1fGmsjC5eLRxoVsPtE15gthxlcI_V_H_SmZmlwIOlDrfqJBJyakhRpBaSgmlc4-ahQsBqm1qAQgVeDWEuXF5jXlIHmABas1MdnoPYYnotnPrBD91QFQQgTkBFxztUlYybITJrit_EC2Kv_52XXWEGCCH7tZz1HhRLrtsyG12lCZL4CakWkVclXaUNt2j6h-7_wdsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDSRm60AqYxI96Xf8yuWEVoFDTlrJycLQhCarAVe7a1hLyKn0Ae8uql4HxL8Bd_lOv1aTdfGT6scnm5PGo-TmYhlRnWlMUpLVi5ZrSuajokVloQIt_F1uxlOeZJPmZfnu3IhDB3wH8PepRvdwY_vND-VUSw6UD-uyWfTKCy9pU3tYF8KPrqD-S91gsVmydNzK6MZIXhotMha6pgflLQf7PYL_rrGEdM7PU1NriBp1CNr-zZ1VsgUPK06kdIXXIv7R7jjWo1b_E_rJo616oNNDJ2j-aNvob-PYcj2LuaEJ9TSAO6-QOEHQeMZ2d8aue1yIHImmUiP2Y7ZRXXI2Paqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCDuAgVFmAL9J4ppWh-egm4i8nPt0c6G4bGSxNH-bFhaJX1x2nN6NrZXuy8K8SOKD0b9Ltkkx5_rF_GUYTOw3aN9__o-TLW4h_jxbywC-sm_UFEVs9T5iuhWlLIkSNdwbtwLzZtLvnVobLflWyS0tYZqubhobKa8rH-jQQUZpSW8sFfgZSa0n3ik5H1nto6KDUD6bWYESiZodXOFOMZLKtU6tcJOYckbxveFFY5RYQNuUpbsWIJVnKTchWEiGGSyYt-HtwqovcaOMjq0uoYDjye9dmFoLGR5w7CXWeWjL7S5tLhu3qkHieLQbdwMr1gJn_xwIYortvJJ51Xfky1CBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKLTdEwKjZosUNfKJLy0W7kvFUD9bjsTiMjpsVjOIr9asrDtBsAuOPl0ORdylK8gQOMxqhx202fQoSOiK17_fvL1-HpFl2wVq7gK14fozCRpsxQ9rl14qXRHjf_7KgD2300E_HAjgV8vv_Y-IzUcnM6Bj4CTAX7N-AHO_cTDM_ODwQKamLGPwye13MyPw5-dXGmTFJh2DpNZ1u2VzoSrT_Z9eHAJIB818s0cT5Nh22kGcjwRqb9hOTTYHxXyMEzmOTfMV_623FfLXHmcZE8R6VW93CliF896hSQR-EDYjcG-qLevd9Xpueys8IafgQzd5vB7-P5tzvKgbiWiksynAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qY7z08Lhg3-FmTyV69IQOZLI4IlmLdbNfiEKw133ZysqeA9Ln7i3CAC0rkg1g8GYmHdfxw9hEU2KvmycTJ6HlJRI5xrI_dL4h8dQ9m0uw6jDS9htec73xpxl1F5Q418TJx3svUr7QGHt4LXYgxIk82yy7JihLwgRFzk3TEniD0oMk2BO7Cg1E-paiW0UeA-CJywi_JTfTTlX2_GSBbF9iTDQDPNv10omEcFaTioiHEP7h0OXzijq3ZYx-NM14YXVJLLqQ4pMwPSb1J2O12-iymF5S5jI1mDZMuEF7ZO0ZUZ0TKRQ0EfU4n9CLIaj1wmt_lTODy1egFVwOPp3wZaDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLnCtqBaYyRasS9FMZh2nAzA2lxJuSXefIL5ApRHGYHT8LgooTASnYeSOTp8B0no63-XS_NFc9OkHT1Y44PlmX31BdLgQIJlcMRWFCYsn8eeWT55OJk_7z5OrEK8y1cRk-SF_S2sSbo2hU2kHITkte98qm3MEPvdn-NzhnnHhJ3_nlOn0b4LWZimBKpaFeRKuNPPb_zeJ6eHebIBe4DY7PsLSEb2z8SbuhzRWAY0b1p7M9ef4Dy1n30rltQ6ZBKDaRhyxIwDgjbPZvti5yVOdWmezU29BrX9DPbshK7CQ9kbdB5uU7a4fxiigox3pef4SlDqBwF54Nk47p9mdDoolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAziJYMYtx9xDjYsEQjVqKZIUwZoaT2BMt6WTTLLOIMPdUdCGWpOTw7DWCQrZUdz8NY6vkuHcg2TWCquBpckVG-DilbXQbsbxfpR-qFcgZS8wTW9purMCC7QZwiwhheH_lt2LGKQRyprRqS-T7tNvWlgB_cdtHax9Ilr9remeES3VvK1bZqMm32zshebBsk1ansK59yzQFxChW2bAvOLT2MWnYOATIrAsDqrdP-ZruU1zVEZpifSkeyY_3YuEZh_l349Tp1k9jsrE9Y56ibNhykHybPBtr2HwXtJjCSOKU9cPj-3PW0eEPQdeIUAnEI3UYQsOZjTtpx5HeGpEF57cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=kl5m8TvPscnlNdjeaH8Z2k9ucOf1EeiL9b4_y2bb9DhPaiRzl170Ms1Fd0_M-Yxmj-Y50Biap4zMMgT-sIlmpqouR1WZliG4sbkUXlseHPHJfyWJOlOznRGC8E_5RjNHXzH8pXWsOWgLmwYYFBaXV2U_Mwn76UW6Qyfq91r-PfD9MBSgY8kRbIj7p3B1l4wFZgBmBGJASC1HxbActhg917z16HjeBCIgo9bo6QWGLIy_Rdf5sK3ypq1RrLInJZnyxaB5WxCqCikAHkBzjyROFfD_Egwtk-6i5J9cj3qNMLIf-bw0gmFeMYdMwEUcIHUDEp5wvHGtRFyNyDDUZZ4CRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=kl5m8TvPscnlNdjeaH8Z2k9ucOf1EeiL9b4_y2bb9DhPaiRzl170Ms1Fd0_M-Yxmj-Y50Biap4zMMgT-sIlmpqouR1WZliG4sbkUXlseHPHJfyWJOlOznRGC8E_5RjNHXzH8pXWsOWgLmwYYFBaXV2U_Mwn76UW6Qyfq91r-PfD9MBSgY8kRbIj7p3B1l4wFZgBmBGJASC1HxbActhg917z16HjeBCIgo9bo6QWGLIy_Rdf5sK3ypq1RrLInJZnyxaB5WxCqCikAHkBzjyROFfD_Egwtk-6i5J9cj3qNMLIf-bw0gmFeMYdMwEUcIHUDEp5wvHGtRFyNyDDUZZ4CRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuHX6l9oIyn_UbVRUwh0qjZNNUnFySSpRwlubJV0ULFSw46PzDkt1V12jH8oNZGmv9uAUSZHBwPdwX_-g84zW6EMr0RorCN_aKP7SS68wTpVfRlKtRKQAO_U-3urOE_s2SbRew0MnAkndKyvigvuhHY7tYs0oCRynBr5BG7Igcr3aoxyPwc5YZlSZK0L5JIuj5qjNjRei3frINgQHtz0qp6KWy8Pz5d9nRibwTfUrqyMV5l6_gPWZhzxBN6oJXg8hs1vecuPJhBBOD-fs5jbVOpNj7GRL12HkAAgvjaKciC8GNHjoqNYIS8sFgWqAl9KNS1KPnk6kRB4FGT1dDkKcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgUZ2bY2ln8s58qWTcuF6bgJngAkMZ84B8W9W6RjieZi3fQhUZr84rM-vMbaZndREHfhzRgNYYjnpxzYymfm-f0jCtfptErncht3d9lJu7q7pB0AVECg9OggBo0w-mytj3eZyhdmCiG7Fe-MNpjQPoTgU-1pe6ekYVpQWCOJg2uGBI7_38zm23XmKx8euIgxrJ8WOoGt1kuyVGktjWwyoNmggMUTTLx2cIZQP9vbMRePDEJEeVkdY_hU_nXqcunQ9lQquMZwO35QK94yKTRte2py_XP7pXLB4NWYEtaX6m3VEGgE6A6LpVAccRVShdq6jTjt9h65qOt1Z5Yff3-eKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtdYKqTwr89TLVfjLk6uk-95c971Ia6KBHsOTLY9ocv8-FwSMNwHuwvp6XLlNX4k8Jf9_vBC4xf9kbstna_Dld3Arm0lnTBLP4XqV9KaYPXtbMo243toQVYX5tZ1zAVgt8ZrUyUPeo1h8seVjv1STdvT7lt2cavepncK_YWh4tXtwokmSmt7rIZGo9jLzC1J-MgLxOvrUnLCUVxeYcFFtpEYZ5OiWupGQK2uetcOc_TMfnKkCLTWu6PFZxuCUsDB6hC6-Ew9nizgDUW5pB68hZU_C3fRpgY73-7zmu7M-qWmSPCkU9Jg2AB_3_AlbVEtnD7UJInMMRwL2nx8rToc5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG6slnpuEr8gYsRf4V4wCgLy2dfC0MuW44SCtw94jP-Z0_dkRthuM6M35u7ygS8cSWUbdGnApRGBnyO7f1_gPPaRO085FOdYcAYG1hkZzUA0Pf_mmiX2QyuRLzUDbJ2NsVjo2SRZjpJkRZW-pyjUwnCqVlipNWGvZoTbH6Mia4Po2KQJVjK6Tvq2WE99UZbK-IGsZlxq3hrS7u2lGnaorszi4d0lJ1i7WHQNgY37R8VpTnYxvsDzFM4XlMC7HROWKr2b89t_Fes7ci4GKXaQgZB2z1bgqTVtTuISjv3uUds7he7kBU9TP6rLondKa3M2Fjw74LCe9bpn8Y5qW4Z5GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=Due-o-WLTwBDkm2BLIcHnbaZE1y-nSkiDoUzF8P7L3mh5ZN3mtR_EyMDpaULbzUgeOQrxBrzggWD7vjbjH_XnBcQcOr7hGzFmylA_gvUuAj2TSbMCLZRfTcwW-CpHslPaDpVu1cxacLY0oGlobydD893B8_VKrIxogYa6IVxAl82_DkE235t-OGZXZpDmC6tVWfB1SaeUL7f5FMS7xzP8eSDPhul6u4lP7XANCpqNKYm9L-X6jLK60xphfakj8Lcais7sBUKjU3cWAzkMkiooxGq3-RnczWzRIMmkm8VKNSZdcdBRzMF2aOGVVIJDGl1Zs1gE1KrWuwJcbswq00VHmoyy_c7UYcS5u0I6-4jOKu-RtyPyaX_fw82sGB9eTJtMkPkSfKjXfnexOgYxil0s6uuZXyifvJX_8i56I9Y4tUSsoEDEX84viTslFqV1EXb-4HujLR5wEbqGqhF9NrLSRld9Tl-SOtYV4Br12PP1jGWTqHdMH4n1vZGPNnFEIq3vb4cvo6MWvB0h7T5_hc3oqDsV51K47202aEpr-VybwBaA6hwGXqMDccWWHEfKGYKopqACpj4Zd7D8cwC3UL0acBpq2Xa1TiDSAW1y_hfMDsIJQK3j899BqxF_bNcP8gYbdAHLMKS_30GmSA2pG5jPQ57Ab8WgYUInxxaBg5-bEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=Due-o-WLTwBDkm2BLIcHnbaZE1y-nSkiDoUzF8P7L3mh5ZN3mtR_EyMDpaULbzUgeOQrxBrzggWD7vjbjH_XnBcQcOr7hGzFmylA_gvUuAj2TSbMCLZRfTcwW-CpHslPaDpVu1cxacLY0oGlobydD893B8_VKrIxogYa6IVxAl82_DkE235t-OGZXZpDmC6tVWfB1SaeUL7f5FMS7xzP8eSDPhul6u4lP7XANCpqNKYm9L-X6jLK60xphfakj8Lcais7sBUKjU3cWAzkMkiooxGq3-RnczWzRIMmkm8VKNSZdcdBRzMF2aOGVVIJDGl1Zs1gE1KrWuwJcbswq00VHmoyy_c7UYcS5u0I6-4jOKu-RtyPyaX_fw82sGB9eTJtMkPkSfKjXfnexOgYxil0s6uuZXyifvJX_8i56I9Y4tUSsoEDEX84viTslFqV1EXb-4HujLR5wEbqGqhF9NrLSRld9Tl-SOtYV4Br12PP1jGWTqHdMH4n1vZGPNnFEIq3vb4cvo6MWvB0h7T5_hc3oqDsV51K47202aEpr-VybwBaA6hwGXqMDccWWHEfKGYKopqACpj4Zd7D8cwC3UL0acBpq2Xa1TiDSAW1y_hfMDsIJQK3j899BqxF_bNcP8gYbdAHLMKS_30GmSA2pG5jPQ57Ab8WgYUInxxaBg5-bEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgCSbSLGuum_58rWKYaqkg_VVdJ_OyJ7MKEC9IJp6JwGaAypNjLFWdUTr9I9DpRyv47qNNBoHhT4qCIJU8DaVTZpbQ3P_9rmiTqzGAn3XkHJsT32gwnNBti3X-rxmm_P8MgtyvQQz1BNbYtwJXDE00ziFkm_DMsoKiqPGZxUh8drQjHuf7XCroFRR4YwM_yQNTa-_DChj4lUZ1Kj9-cjTvgWqUo_iV0fpp_olMRQuDn4RjTOp4yBp88wWCypqwv66PhjXOlO_s30UQmgQd3dLqG8SdNgMMIcTzXCkMei-o6E-BqZhwo8dYTf0J__VPfdCOK7--V671Q9STfPlO9_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2zkG5fx4g7gsosTqfrTuSo_HvYLq6QbZzYqXaXkoPmWSXQRh7eYI5ZTzr9BbrNiM34MsBZJn8WU9xs4Rj-L1TLWILHkB4qFovxalEx2f3hIJpl6x52oHWT7bnA_sOURw-KGKCRbG78k870CtL8eCau4QFA4jM9C5L8hVvfWXHg4yN05sPfdp9APwUpczGWzKfWlXPYynxjZvu8nJPZqyMEaaZxMIQ75iEQUOTuMFDoqRVs7Qfb0rFt3Nhv63QafebZIsgj3rMIf6edxiSrNh9AB2YEdINjupXJfaD5JFekQmtC8ac9Zu-CItTvPVSY0IwV1slCORryroM0WxAdVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoTRmG-ZECjFKZujpo2XHjrEzEvZgMweSY00DiL59eeDK6UxzWnsM-4RTYcgLaK6hB-8EYQbjFA2b8HBKt3Li_upaciPHO3ED9rw3uLWjsOgB_y4Us9JdajpUta6FrpeBo7gXwLW4ESWxp4xsa7s4Mn47anwMe-HGZZn3nYON_4B7F-Kz_ruhBPnzAkU9GSCh6qGWE5FAtKWlnuK9cQNnz7oVc7GFO9mnrxONBLzqmEeKOHAMQdTHBql-qiJNahQ2bxHTbc5ZIgwGxRB1GbiBtTIypk8HOUXXK0vmk-3ffXbKx7tLtJy4s9WYUUgC3hg7sOaI2rIapk20JPy_4vtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjjMBQ3DHfYsOmOCWjWl4V_K2NWchbU5QJ1O-_DRaQvSLKccUJNtx5DgBOtmlYm37igBgw73unS8EKsa8_RPET1gdRl6Uh5T5Yf8hK5N9Lxw1kHP8NY_imzhTRN8pe981JYuSqGvd46iFWTW8aYriAXNQLfX6S8uayv8lWIwb7e3FX3A-ZpSJ4sSkQla_kVFzIVgRna628D1zNfnaoTm2sQmT9PddOEU5vZihMGHYnc-ElMZKj-Jh_X4PotyXZ_CPsAeluLyaBWAlImafrAH2Lt5PYfg8L6qRgqYxLXuW1FQumbkwnC_0oFynqCr7--bH9KLpGJwV2afxjGW_4xPiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw2Gs3JJryDvm75aSdERf4CVrHXqXU5qty3-TPM7ofcsiKJ_Bc9MfRX1EedSmkh2iyFGakDGZ1O8WUuEqTcMRzwUUHm2YQ46Go9rOJNLCbgxNwRr5-AtOvAjSykpq3jiaVJDl77R4OmRnxn8bdE6ZPdNLGCGBWorno-s_vFjbSai22cSNTQwHhhotU5CvEQ_AJ9BQVezEbRKGl8Nuy3Hg0Y_HvRf3DYWG2PdqnTKJrVrihg-W5TtF3mQFENzdGy7smXnl3ERjs21ErVy4xiPQO6TSs45OQH9wuHtc4GhZTHKh2G1Ugh53IbWlnmOyWSYrROoimKrRBS1uB-zss-cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbTGQemrgB8ELjS88SMnisiZuOB9T5tZ5UHkLQrX3kprKmy62WU1aYKqbaSbIUQNjyDZTbGMJAP6lAuO8YCwULQQiHsEvh7slLwVGEEsCKaBN0tTNQcIMlDjecpVQJpvnPKLc7IM9lLXWXmxC1ZQptED1Awm5QkqFPNoE3b6IaGQ5eOVVtwdJRvCnm8xyyhL3kFODR8Gt2OjN1NtvpJVTKDQG7QF4-bePBIJyzRztAmLjUF_AW1TY55TFzbxAnA1q7Zu4ly0jgaeWTvfTeZYtuB2Tbslhzq_4UErT4Cqrze3FBTtzm2cFAcgQxVDMRmr7UDZl0zzaH4Qq9WRuaVALQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZUlTd3mCrKfvKrLfNhgMo6jkBnjbuaql3quWzPCsHBJZduJE6gUyoJi7MD0-ALukI-8Wdi8s74F5ci3OyevPg1PZQU4Olxqx484FFSyS6eWH1-dbhH-mWkWaee7KBh40kRzcI4xUsw8prt6vPcy01F_4wCQpYkauqIOVz_wJqNJCBsRXHxNrELd_KSSyot0LaEgp5Ba6GGRhgP5lv_uLv4AcnZH3fnDXjTvIdfiqA70k16CjDoDiE34RKzx4PlMjt4tCy3-4fvzND5xlnm2RjdYHBkQjLSZ8YIfqBvL-pEuYO4yfXYow6SP-sVQ7RqiTQ5VfjZAQNhdyK2jH1KfWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=a7F8yFmJz3yT24Dwl3iFQ-dR1L1rYbFDNF_UqwVGNQD-YOSAsM_kapFt9ebgsUE593OWs8RjrhWGOo0Ju8gJC9r8mMGBfuCIMoAauV-J9vtIXO7W-do3Ytiyb3VDTk9Q7nfu5uyajgF3XwWk7CU_c-LwcSM-9HHT3aTEuRGEiiwlwyxP1BFfl_JYZF8UWWuyN0CEZEcAHrgR1URJxnCBL3BJulM8jlLCdJ504GLB3EWnj6jhcNTbWoaUDUqsBbCc54e6tiaRX2X3Y8TL9uuZjpdsBW0mcMPK29BF6zj620FBFS8byrKbjyAiizqW_qaVjfC1yEBKI7ngGNF0KW3Wjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=a7F8yFmJz3yT24Dwl3iFQ-dR1L1rYbFDNF_UqwVGNQD-YOSAsM_kapFt9ebgsUE593OWs8RjrhWGOo0Ju8gJC9r8mMGBfuCIMoAauV-J9vtIXO7W-do3Ytiyb3VDTk9Q7nfu5uyajgF3XwWk7CU_c-LwcSM-9HHT3aTEuRGEiiwlwyxP1BFfl_JYZF8UWWuyN0CEZEcAHrgR1URJxnCBL3BJulM8jlLCdJ504GLB3EWnj6jhcNTbWoaUDUqsBbCc54e6tiaRX2X3Y8TL9uuZjpdsBW0mcMPK29BF6zj620FBFS8byrKbjyAiizqW_qaVjfC1yEBKI7ngGNF0KW3Wjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcbDh7onvvc0N_hKYTbt0eRsQgXjnVdSPnWtHVgEnaZTPZmjabpYbZXWRdB33Ntpp9nS_vJ_ejA2qwGEUDD1Sphj6Eb-IlDsa7oVT1qBrGIiT9PRemIsnRwRaf40lgb9V3h7P8ThO_1rAg5ZGw6L-WlOo40PMTml3QpKrcbC81-KJ6lLHT6y5SshFVIS5rcK4AiPqZ7jg_gP4ClMsth93SuDYBO5juZsDKvi3XvwXa3J2zmpBzYr0Php3S5H33XihVy4Tke8wOjfcmdvSS-FVtfNwJ8XZy62IS55QxyCoeMPVa1soCSk4YlZQ9ddxswmYsMCjWgzcXujeGKtZBazoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUAv12G2QruzRAUD6uaHkdnDgX6Tp2RPYqA__3qFigi9Eczgy0e2zD8kEZs4dxkv7ng7bbOEiCpPQ480lc_hmm8UGK6fTgGhrlX5-Nnvi4gkVy_4i8ZT5hSSWuU6HtW0Cm1WGRKQ24wHUCWTaBkb87dNn7R3PuvLQDVcwW2jJCeJlJjzqXQ35zapAXOBLf8fnoaTuxeoMpOia2ZrYW3tD93O1ZGvNLsR2tHIt4MT-quLhgphxe3OEV9zsUE1xBQUJpGsuHcHjU6RboqoOMFSIb_scBFasMJIfhyZX5HtXw6-H015g9PNzOqvHjxmtuLrbCjTtjGXfyiosZ7EnUniXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnNmuPqXTqhiJsQ8wWdjoRgNJcHOrCPESsEmuVmIiYMiPWTUKc3BbKfnhMi_wBr5eO7bL5GDeKLabhAa5H4y7cXwb-mTiCmubiQ5jdaUZBoO3FFIZwj6PuacYPIDQWDmdEH86KvpM6TzQjghocHYzAFs1Nq_TeadlB2oXnblkpf4w1DYDvVz2sjs-SlLuKGFuRA8NqJ0YBIXOlrL6R32_nHou__cjPuTTU1EO4M05mKLNBclGT9kivYeMDqDxVQTgA0OuodGyMUmvDh18SaYiU0s6BSuKmXZrVgVRAr1bZUj2ugj6Y3ooeB-ezMVQDcPdF-JdnBWO63Y7GoxL-TD4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFHBUU-E86MtH15XtVw52INlRq3F1DwxpXrQod4KoZzkL0P9n-WBoM2dtwU-Sdjee8CIY5kfS8JCC8WztVUAx5Hpt_zOUZgr3Vmd6Eka2wbz1GfH_l7x6SJSRptIQBlSAJ66XuzfHho0anXKssp5TpylKLZJ4T17R1gHuZxIv7hzr2nXNL1RfkQ3A_bft5gLFnh3JFkC3fz4id-zhltpSWoRpolIBJCYUn6xEkGVtTCII2x86x9h_fZO1TaUHTvaTRJpZAUbFNZ9Vi7emm_SdiKsK0a-osIordDobAPL8cHTKJI0YLYxKhWoLr82dCt8HMUI_7lff-2KZVx7_JGgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4jj6KkiLrSEXcmEHdAD0wYlCZKTmdEmCowjMhnkuzukjOHiOxDssSCfC0BY6KmxP8KHrjH-G6BldpLFRD_g5YgPvshqhY2tdw5VB0tPyVyzM5iZlNWna1AbKMQMNdn-spiPt8qvN9IJMtKHixbEazp-NuC0N4cpujL3YOhDygL_KeDoy7UJDSwRwrff1_rWAenIbtAaG0aKnWcohzLhD2CtE-Em9cj3S1g6dkrteABLzbPLFuQY356TmA4U_RM0Z-7ZkUwFMo745lMh1s7VhBBekLPPOjuyuPfg_U_KKxiEisKevFow-svbcbk5yYsJ7rMRBzXaXqYjIgYDQMBcmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhTYNqyFlgDogs6UC5AghS0siUEjE7sfpaAdEXpyTNDGyNAPFDC1eueDEMn_lB8elss39Rwo8-2ZphM5rSJIV7MgU9jP_Ey6Ni6crUJXybqkGXAzL4J_kOEGmwTZdCHUQ87Wj-KR6KT_ljk9PQQjuWpAFunAkUv5aEZbCgfe8MgvUhOxvKjovjI-2_MtulCjCXogEipL3Kh1lFkHas9-jR8wwooNUtm4Jwt3NlipJBrxomvqnrf8QvT3ipEsVH8-z5h3rKBbxS3Slsr0NJqIQVPr8Fq5j6O1ucaAeebsLVpPMgxsc0I4Ndr9zqeIfh5NcGuKPlM92DZqp5q-myYMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk9FPfpUjPYIcHrd6gM9x7UmWGLchw9zNcp07khYJaENXx1vgyqqmJ0iKK93IVM_RTPBfISv1I3hpkPb18PjPggqdEKpaO_NvknUcWM8GdCjDzYVp8LNUQBTsjn8TYLVTsXGBj4AcgBJysWJMowRi0_J8kn1UmcHqpZvAYLaeZuGyl12eEJMDlB8EhejohCzefxOTCraPTLEokWe_ZNWZeOtsd41LtXl7ds96_eNFf3szZwk9o4hSh8UzfU46Zzdx60EZVzfY2qfGCpbOsw8DxVUGQ291Ht8wvBqp88wANCoEf0292kthCNi7eYelMirZcwNLXkaF-FOZe39KP_Vvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JapDu8UgcKSih62s1_G8j09O-R7brwOiiVnE8Puvf_-Q_MBS-Vft_D17TdMYAz9IByfzZvFbnIB3uiTIIV2mhDuvy9_8PB9Kieb1Xppw-uOCvJI6Tt9cMhRISskg_0mbjWVpjTkJJn52HubDMikZq09CoXE5ToJYufFVNCTG9TgzaJi2VLi21kireCC6L8H86KMUkCcNQkdc5U70Khxi1fSSlte8xd8nxUY3d5kY5MuD7M1jr-WkmdFmsTjN-0P-Zzb2WO9S1tN8XfiqpK7FqF0nSvmG4hSA3xak3Po8MlsqVjQMOZLC5aprJwHRMMH-XBa6y9smN2_l36mkRJ2wkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llvQk9CuF-tFrV-XQKsVCDm980OCx-TY_-GqwQeVsOcNWDy7Pl2taLTp0SmHob_YwicgYvuYPTBDaWI09QWWfAWPEW9JnCJhn1TSNfW1Ez0nKbciew8L136VRKvEZXnQ47UCD2Snqbb32cfROwbLIdUuysF3p7WUE362LjjIx_55MX40oM81cjcgx1KhuCVt4b2w0n-cRygABMlTFCHY2C9_tGQpt1OBWOeqLL6TDo6TZhWbumGUE3kSLxBwrne5-JYC3HshU77NUXG7w5w4ld6V4CjiN5qCnJdWFmsl72oTIpiXwkcP5GHM3ryTVs9VO9oK6i-AIQi-d18lu33BGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F97xMGY8AUHqqKBAlsm9co2Shp_5cH_Cbkyy7XjmeYY2eLowt6MmcNsWIslpJqOZlMxqZlJ92c5OdfwJPYFT2j47LTCRgjZdIIbzBG9V7iQYvkQZBWvKnoLniNEGOctC_Qp8PlfJZnnvqJKMuAFkxm5DqFtL_YhEakosyodfdJcDnbZ8uUqLPxSG814pq9K-bq0n6W_4LklJutChumy5hJ-Ovbm5iBb-K6lJqqrjsSCczcv_ElN0qQ0TU1j0vNzNFT5MJbB9eMQ8Y9GtP1SmXRa9cTEZp_uQIWnTnXuVCQknmgui_s8xLKY65j8d_KwUeYQVo-mY9ObDrfxQ9mkTog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXqFooLmejMoyi1e9vvA_xH92aQs_pKMAnubdo2SmOMZdU9ST4Nxf5qh8FxoNNr_gl-9jXqYqIrd6iPE-KoMA4g5VUHMVQvv21cD6kjzDMHBGt5mQuEp9T9lE2WTrQfXs4Ab-ohp0mDcmRQMJsGZTCq07dE5nth-MDYy6Xsdt8-kcwMTMu_Pd39fMbDipyC73JcuygJ3chDY7Gpwk44oo5Abx9W-kBnH1MLJytOQtSE8mweLy6sqyYmuHI3SDleHAmkHBNezUB9c5f6dJLkQZ910J8KbgWfrQeQBRQ0HG5WRQJ9rwtd0t0TZV5iAI0a6mC6L9Qu3yaEZAArb76sFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNrIYiz4QvgU9Vfm6BP_0Yx_tS1F7tylCzbW3a9I1eNOXOblq1ztTYIg1hpHWvZd91_MgafTPA0_7G7Fg3C6jMGwZEm0VNJmKn1bDCAg6PCGZ7TqSnTXBvcXYyir2Zf2R1ibRAcfdwqYKhMxcHbNyzSNcgqQOPlJvWnv7XGh_GCe5nUCgc9-Nmqr0cI7S3lwrLv_a6mcAyirJZYsdmp1mZnpNvIEfELETVq5WJOQPI76HRDM96PuqKxtpJ-j8TAYRuXfgKJJnVXesEKWEkBJNdF_ErDRh_uJBuX_4nyocRoBxw_iT1bZhiyivQ5y1L3zTTsEo7REcuXDEi6RjburGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3vyvEgtg1g96rR5HSzdlv41ctG634PYOG385i47B_ZZZ8W5IttdxWrMwdOdoGTf5j6u4xXs6Rw5N4Oe6vj-x1AiKHSvSMh8F2IUg2-1Y4P4onmsUKNpPPqYlIjyUQr2kgt-boDHrjv-gcSkmiIeXfkPzGnqeoLqsMkj9BaO6hZE5kzWAwXnvIH7M_gR5aD0gtutsY5tWg8MXp7hwoWNqolXKCjTYwI2oLdwsdx09l-xTzaZe265k4ycmAex2WdAlkKgbOVRENs1hNWvFse4vBVGI3HrmMKaB6gFe27KGPHvvVmEcJ_MjGGZPGlk6irYcfL4YwMQG7HaNAknv0pfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eq7nXRUUddCOIYjpr811ibj23yqRGnW3h7sUSpVojopIe2B2vf7zTmu1G6G7lMuqG9EuP3kr_WOBx3dA2nTBVXgBkUsLZVPLbe_Wjq_iu0LydhXAlp27NUexe3uXbpxsiLiq9H_p3dG5R5CMYA63VYVmwxXfrpLNyYfhd3WOqT232MCOxu_Q3sreFBAedoevcEZRR1nwY2a8mtACSAq25__mnj3qU9mMyHaUxiQeaOk0K8-rFq03usHJl0G5Mer8qOlJk_D8L9_LBTL3ofqF6Hf1Sy6mHhPShSD7sVGefq-D3QwSqjoYUHtBJwzzieN7hvWE6iYr3DVKf6Vj7RsIrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=fQFYu7ld-KG0I7ja8b78XlG5zwdQ-NFCoOg3MNlImKdSEQRUEFv0gZzs7W8-R91J9nljCU-HYpFl_-2ulcV4VcsNp15P3yatP_zcBQshnBithfLJJdCb4cAxgY5LN1Sna27w-EKBhT9VDMfFLDab2Y1gj2U2DgwTlEExBtoG1uQbbFxQAHAEnMjijnovB2hkgVGA-0bHXSFHS1o4Z-Pz6K0wsLrdV74nJoIdCrd0VfFdb4kiFdKCG9dUaP5lkvQlX5jKx5ADBt0PQoZFUVjY414VmjXpDtgG_SGYen3S-pzqGBRn6KfGrOSTNcTv8fk7PabbC8xRo1HG1SWXZQXtjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=fQFYu7ld-KG0I7ja8b78XlG5zwdQ-NFCoOg3MNlImKdSEQRUEFv0gZzs7W8-R91J9nljCU-HYpFl_-2ulcV4VcsNp15P3yatP_zcBQshnBithfLJJdCb4cAxgY5LN1Sna27w-EKBhT9VDMfFLDab2Y1gj2U2DgwTlEExBtoG1uQbbFxQAHAEnMjijnovB2hkgVGA-0bHXSFHS1o4Z-Pz6K0wsLrdV74nJoIdCrd0VfFdb4kiFdKCG9dUaP5lkvQlX5jKx5ADBt0PQoZFUVjY414VmjXpDtgG_SGYen3S-pzqGBRn6KfGrOSTNcTv8fk7PabbC8xRo1HG1SWXZQXtjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxLEqUSRmyfGPk7bmRoKQj1Jl8ceK-qW3FAm-2qbnNCxICMrr99Djxg4BJtbAFtV75yrbjZvN7TKXJN9taAaWUHfLZf8Q80rUPioiAmrWgmbtbtuR42t6_9ISihk9_VIvpYBKjbmBGRpHGCEhIL8GG3VqpAKFz3NVLgfPIxn-OvAUKx_1x2e7um6kYzsBBTtxD8nHM0_nMvMDgX2fdfHucbSKAdgYEQ2nUaEccnPECS_4dbtY9ivv8gH9vF8fGZ_5f4Yf9EHlc_qmtsxUCODrEQjuNHA861QRJ410zbSNWEBoyvaDSVkwCWWTkTfZ1IFhXY_E2pXeW8uoJ5Pm158Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=tX4TQwPrdPlBCqBAcpa2VoG_RGydzBKH2-q2duJep2K-pgG-ehXbodLJVTX0LKJtvDjFozqDJ0rND6FVzuqAvsuSYj_LIj3U6P06Bhf9ayX5NA2QaEAMng_ryMSBBxBSQTxRCkvJD4a5KSA7MvijZy76oLXpULamCmmOEGD6bQYV0DShFaNJc96viTPgtBs9Th-Uw8H71144hYHXc1MU2oJcTb-1UdtU3CbkaB-FCS7wiaRUj9JktasX9xiSMsiUDqu11jY_tM55PmkHKpKfI7k1XELXeyqzKjBT1Mz8DoTp_xPIAAUe0lN2jS8uKUB4XnbQ6w7YFSXi2FLwoMXumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=tX4TQwPrdPlBCqBAcpa2VoG_RGydzBKH2-q2duJep2K-pgG-ehXbodLJVTX0LKJtvDjFozqDJ0rND6FVzuqAvsuSYj_LIj3U6P06Bhf9ayX5NA2QaEAMng_ryMSBBxBSQTxRCkvJD4a5KSA7MvijZy76oLXpULamCmmOEGD6bQYV0DShFaNJc96viTPgtBs9Th-Uw8H71144hYHXc1MU2oJcTb-1UdtU3CbkaB-FCS7wiaRUj9JktasX9xiSMsiUDqu11jY_tM55PmkHKpKfI7k1XELXeyqzKjBT1Mz8DoTp_xPIAAUe0lN2jS8uKUB4XnbQ6w7YFSXi2FLwoMXumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc9Kt42mOSMSO4pIigDznl0g61fGM1sBFoSkDTfiFuMEZSL7S3lpLYsAFusefl3Q4IUClxtr3tKJAlA-Awb4qqmZtRk8SX8p2hqE3gb895wC4eKLNH3tSHvevOBbxJeTnEXyI0lS1p5n9HkKJcAG93sFthYO_WKgRQ-mgM36uQHKj_2Q_yadzQygvVK1JNDg56o109rCfTy6WBTZ5xVNE-2FNngRzm20N8_1pxcJC4OJHB4D1FNPJOhqwnqj1_ej1FAToK2vxD36RZPvs083Xd-HLUm7-2IF25P42a96hZmGM-aQIYOYLAWQPaN5YsRAv23S3bobY6vTf1seypMAYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
