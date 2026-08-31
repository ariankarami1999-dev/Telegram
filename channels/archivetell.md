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
<img src="https://cdn4.telesco.pe/file/sL7oqzBGs47EnPW34IB_y3O9lT2Mlwyhu3h5hxBuo4zS3WJV_8MV4_1exyPEwwNSzVFjZBW8o6o3_bryNkThf9RIJ1gXM1BXT3o4_OtzFTZg-qSmLA3mrvAH7Ir-sPdT-jE6VPxSE_ksoZTLyPZVt221tkV3QwNu4JtuRFq1cZetaFxpiJ82Ki7g2xw4nXPekwN20ZJ189iKfvz5o991vdTXy8cU1uUzFRrJbSCxFX6tMAorRBckzpVOHLYoy8jiaUxyP8g3z_oN8dtA2ksTIHkaqFAP5QVDfABkclMfLh4VDlol51dqO5VM02lX5j4nXr6Iu23O1CdsQQ3r-QnLqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPEVMC2woED3n4sFIO54SdRfWMydU6LLI30KyODaDpetoRIjX4GJyKsJfj4eO2qYrB_NcuwwqoplpQ1IiCL2DDpqlEj3D00HIJldy4cI1YrEmBUSQFeZnw4iONFT87ZuQSFGmH_W7o4zn2QamXqusqlSvU2pL1Tqhr0emrs2RJki3bwcN-vaAZC1kkVFzv7o7N0p90a-astuyarsvGRfUAZHEHh8XVwuDp01il6vAJqF5Tgo6Gb0R5K8aMioSaANBjl2tBZlNZW0TAzZSZeAtc5MQGjbkJTBdCkHObpcjKkmCO14xatcSmIEboiLQzMzYxUJAyntKiH66vPRBZj8Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 627 · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUEfYyF5PGEtCsDkrjugHIxRzvl2Hxr7rS50YHUrcNlFvetTQf4yHAJo4PWDuZWz5OYLyLOCRX3BFilwE8_An9W2KlIn34p7sgWcuccYBPW4lJYcXJlNW7U-8mN1vhTqJSorofC0Fhn1H8Xj-rxO4r4SvNGA0fDUicuSRZ1hKL3fYBZ7X9bgfGCzyjkii6e8XcykaeB5ui8gZAY1EOFOFU5ByEKeVL8tO_ExuPaiLQrM4WvGiZBJAAd4DU0pVjC7sYJlI9zDdZVGELflfM9ltJJki5aodYmZnbmW0b7VYbD33y-moZ16Znv4h0LH1KVPOW-d3P-Fa8jZe5UynV3TTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 808 · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl0O1VINUhD3NOMU_tV_T2zccmd8YqqHeUlbauNk1QDS9qu_9JOP6rfcCIDyvQNExMRQsugwjVYaxBMegPCGIwHbERYBp2Sjmb8z9yJ__1dHd4Bq6oRpUkLHqYYOp-C1cmEZzhDNcFQeFF-MkLJr8RDwL7YZjOsPYlanD_L0O6gRzyfWznwtCjeFSaaVf0lYfJSNhTAOPiNXtHhxI4l6Tq9B5LDe4OyHiupDTjZ-8Cw33_vrq77zzfTJLKJt8R_jbAx4J7U44dJh0PsQgusX0H5usKRM4J0QSdsh9htPfpcFubR0P_-iZwzpmukNMTSGTw6bp_XB5bpCkPDu8DaOew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 950 · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOePhQO1i7MfXTmI-OFwsEF_lAGxANssmXcA4CEgj87Ubka8O2CAl0kINHlooMIsMjkL_OFjr06_DZekruZvmu4x1xtN9wD4L-mxVyGORoQlyjYeSLg1gSIzh6ZInzQfuSk5EqXrgcUDP4fjlcjjFsXs3PeG9t_ziNXI8X3PKYylSUutKaqSmKaVcgryoZT2cpA6d5yB_Uu_JBJSR4RygG0_brlsrE5cg8FQzOP7H6WhyWj5VWe4dwKGavZ1U6uZRTdhl7GEoeJ_bXfOMVG4kRcEgAXoWPx_kDoIlj63irSt1Vj2tonEZIEL4j_gIvOmI9XcG7tCnVyW50e6Cm_DJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WowZU-R-CW5lxnsQ7xXL-4-_yoxv3Usg5mVFjUclEZ8WxPscEDnX8239UlVVmYzAkD_39u2UaGIz1OyrK10wLRrUuVB_aSahtPvVMEhTcDPiYfRfD_4sprOPis__FDcZOpacostH1DIye9i-WZKJyx1jCIeuSZb9GOVLh1dVB03TGD6gCmxojZGD3suNPiHJj5bY5sgn5QTjclEhDUd-Z_6IP_z8IsNehkYCgArQtTETk0QdJhWPO6MZD0ZP11hx2eHtVUHJw4ziQvR2wteofqetB78lcKJKPeBt9345lhuMZvAGT-1Z-hdHVmqGtGMJjNjfppWY9wLKLYGxrztbVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujBb-l67YNhp0YNDduKzzdIbnWcrQ8FFJ2MljnfztdTZI0zfLIdIHYUicNmWLXDXl0eBKATPqYefZVNfyb1iFdOpiyxyw5SkysQm_TuieCWhY073ry9-ABtTM4u6oC78OqSKy5BnUWtJWfaHYtdTSaFgW2tkRQQQ3AkVUQPSWXm_duN0bp9AWAd3quSF1hO6PNk_c6fNczPtiRhtAGAraTSoOdH_oI4PDSTm3JgNED1h9FWyaDzWnrNZzPoQNxW8ao1Ok3lAFjY0a_KiNOEbkONZen7bOIY-kDTpG6Gd6iQbYC3SP1saEo0cXU2ruqjdalu28_OaDB3h8_vNLqLdog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8xl09S6_fS3ZQ0dqBNcsjFVHmtkee9iykhSTf9GgkptEe3q23WJXxvBS_sZoARZhqXg-O6239N0mBNwoQI7zkIZFUih1IOq6TKbcHWQ0ZXPnJATsgIKvY7p_dgHsi60itV7AJCWpO8JToBPAFELcKF0AX3-kwzbuAHe4laaOszO0-8ugG3oCxe0HUfCRwbEkkDvvzsjbOY8-L7EfEMO-Fe3oIA3i_z7MothD_RGPkautRmGOGPp61TD0ZISMnnNSE6yNmfen1YEFoYo8IZMo0iKOXX9xi6op5U3zXcnMQPRKBkoRwwAK6RiXkcjZ-DebU6Qcx9ugsOlzjTSBtrFUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ1QFcYrd9uEuQgGWwGMsR7oqGJL75thiUA0OK-Un4B_SkqbJnBpKCoeNA-DGs18OmWWNDs1Zoews69ulVsqWULQsbZKZ7gi5OcysIoa6Hf9Kvl-Wyd96CZARTmGzK7uy2RP2IWaq95nP589Kus8VGdRcjgtfEXfVspRX019bJWbz_O_ZWyMRepr5knQp5M_xLVYGLu0udInRYzgQdbdGsRgn0GbN-Qvr2T-mKul3AHhsy7OTF5tG96yrPJvaHZL9gJL2oeiAgzQnqF5MmM-yUUxqSqg4mQdhdIiDaGFRdw2AYpigVjDWfcQeDeE0FGyNoC7CB7BXKdvU2vO0Lvrxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U77S7-py9AOTXp2NkIzD6ylxswQHq3C9MLpwnZ4FvHdSEbQPrXeJD0lacW4oWHNuuVm_PRb1DhkZgMBH_sk9DtsjoqDuFy5OrlENikKmMgioGjhIAJI8JXVSVvrkdwiS3tqkcHCtiIRa_oiq60Z0E27flvNqXDodEbxJd95pVuFHURLgH2XRdMI2gZmMzEOQa3vZEIHbVr-tGXeUD_6rBa-zB9TdpO3ZVU_qJ07Cyhal7ueSxZ6NyxVHuy1qRJiVh7YrHZvW5epkQ-E502SfqwOnsxOBmdGMWOV_av03mwGYdE2oNlzAfYyH1x8kcUUd7ZPwRyiKz7sJJB1oax-1Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=fPawtB-JsEMj6jxymaZOLcIhxrf9B45r582w_qK-ymZCSxFrl065yrydxppZkZTlDwf_QgFurdj0jJV8nUSQM044WuA75EaLTazIl7ILLrY_W-0FvatBnpKFXT52ju8YRZxFlAl8wT3HCOA3VfMg3JSlZCnvtOr0q9hCX7J_VfmGGGVbt3hx-OPIKHlK0pl30xbRkxDfsMY1zUlaz51Zsq8Bec4rU20z4hiU3fMOR80xGKcevMfr7ncalZBgbJ2iDdWijzJi6qLC2uG5Npt4s62vH5DbYXS8s9wQGRVmHbmDJLdAaLuTJ6-hNjXy0byWLbDlYkYpHfTlAiocqXqKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=fPawtB-JsEMj6jxymaZOLcIhxrf9B45r582w_qK-ymZCSxFrl065yrydxppZkZTlDwf_QgFurdj0jJV8nUSQM044WuA75EaLTazIl7ILLrY_W-0FvatBnpKFXT52ju8YRZxFlAl8wT3HCOA3VfMg3JSlZCnvtOr0q9hCX7J_VfmGGGVbt3hx-OPIKHlK0pl30xbRkxDfsMY1zUlaz51Zsq8Bec4rU20z4hiU3fMOR80xGKcevMfr7ncalZBgbJ2iDdWijzJi6qLC2uG5Npt4s62vH5DbYXS8s9wQGRVmHbmDJLdAaLuTJ6-hNjXy0byWLbDlYkYpHfTlAiocqXqKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqdqU03FidujmchvF2k1Xthdk3iajRcAki57bsl9mVZIGbusEqkpJl3HkRD0W-1mLyCnIxeF2YUd80Xsh1LoR8WtEtP_uyfyMsr6c2JAIoFEdXQWYEqIJYAE2Eb3jyCcl-k_qs7BmGQtHa9Bvcfd8nNAVCOpDtSlYdPn0CbiDwEjao3IJ0mZ8TAva15VWUQp2UR3NoJG4F3AwYxzbY0rY9aWlRtpy700vSm2nBCCk97AIEA3CXJYMp3QqkaQCSVJ1rWicAgSNDyTSKHU10z2z7f7JZWYLmBShQz3KKnAO7NWAo_4JG1I7uKg3R4ziOZtQipsMmC4M88rJqG1_vemEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=X9HgFOSZseeCzEVeTLJct1g4_koH4MnAWjbRlluHoDy5-xdiNLlP0LtAX15GXeYMm96Ep7EJz7PkJ7nJjIM9M0ar9wZs6GTOBgqBkiybvp4zjOC9ozJ0jspJJ_AkMSXPIwrIOAgvbB02QCnx-hnqIWK7UPjeDo0D5KLzAhlkbvmOYD9pIG7SgbvEzcHXh5Y05v2q5PJK6f1vc7EXdO3r8mo83ajA1yA-KH-hK2Dun588ZQQquanjxIyLqCMyzfI4RjMm6sqPAX2EK0eElobNAf5XcLc-PWP2lbY4b7F3-5FSsTSccX8_KSWd02jrtEE8iE1_qn3diD75nr1c62uPOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=X9HgFOSZseeCzEVeTLJct1g4_koH4MnAWjbRlluHoDy5-xdiNLlP0LtAX15GXeYMm96Ep7EJz7PkJ7nJjIM9M0ar9wZs6GTOBgqBkiybvp4zjOC9ozJ0jspJJ_AkMSXPIwrIOAgvbB02QCnx-hnqIWK7UPjeDo0D5KLzAhlkbvmOYD9pIG7SgbvEzcHXh5Y05v2q5PJK6f1vc7EXdO3r8mo83ajA1yA-KH-hK2Dun588ZQQquanjxIyLqCMyzfI4RjMm6sqPAX2EK0eElobNAf5XcLc-PWP2lbY4b7F3-5FSsTSccX8_KSWd02jrtEE8iE1_qn3diD75nr1c62uPOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlSOUJF_6NdGH7KabseCYEWPsQPhXSNsffljXSdru9blooKjHOFoY9aBr7pPkj5UCA1yW6vQLPv3AvHZGoBZxwidhk_iTFMGF4j4LwHfWrLwc-AU1Bq_2B1I8iRYKMhfFzwtGi3FvVephHP9fSLMmEREAU1BCqp0VIaWQOgE6CQ4wDXSECgwJYJYESnf1HwN1EitLkLDlYW0IX-gsEPbECdbINpFGifcIawcuXFw3KHpNuwdq_Rn64ay5L0fz9_2UKjDCK0Q1EcxurNreDAgCP4MOUwKREh35nVkhT2HA4YOuUki7FJD2CyxQ4CPu67lingy6h0zHrktCFT8O3oidg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lado2V6U6kcnQ4kzeYLL-QOeg0r2cW824INN__LxFUi2vr5b8K4nlQp0BlMjpLaL1xADj4KPL5pI2VYJBd-CRcvenCzD9tFHzzQXmvpKmNXxQzchKGnoUY2PcDE_fMQSrCqIj6BscdkzLfta4AQduI5tVVeyt-rHXcvD787HkmB_90hzHOd-ZpN22AooxBsNYXTjcR3-jXepulqpzx0qzsbWlW3_RjIc-r3SgBQT27rW0WgZj4bUrWd1K_FC1826YHKyua7NE7wDtDFyNp5I8nBAXNdUCt16uid13vwlf6PPB7Rb7TsEx4GljWAkzVsqEtgL-DyvHwIHlBc2Q7zZzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9oNOTSOvFnrv-yyncPONdgRbwJmei9cg0_BI5Ujr-iKkSgc4C19iMcRW8-dt47uNRv21pBQ9s_lCx3iyxxaMGY3dXcGUSkFQRQ1unYFQaSCbTmHaAv3UEKtM7z9sRO2FHQtug1wkKYH242xaPnHB3BOzSpaHlSuYIoSNIiYYhEwhhRzJ2QJshsUn692-4GNv956NTvJuT9Poo6hht8H5Bav8svJ4o-uHgUXg53EYH2rLN0D_DMPyqgTSzrX7hXoZGZdxPquJxmYwsOcOxcGkVOzmpSvXAZvaB_NTESNhksO5PlW8GRGmCALDNqbfJT7n_R9fJtIHLP2bYus8MPL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5Iq6r05XxzeNxjVucp3NdplCkfEyBCPf6MNMyABJoDcdAHfNOQH_z0Tu02RDNc8-ANfcgqAmC_i5cvGwxWeOF7XLW6lAcwAXCDrtYo5kz7yDj5KjktxZpiGvWo6RRm43jOn4riV4F8Kmk3Ieln-0t12IjwxZQVUR9tZESA9olb0-zfBNYB4Ds72oahmjlYuDiN-1nCHkp2Z-Y9t1AcQf_MtcpXetHJPbO1f5M-iOAj4NL8pq8oQVLBf-Kyjc2VfmGHYX8pyhM1LF7cnreUsPFRRGNCi-Ix8xawt0EQoqkf9wDVHT9FytNFQU1sAjLE7VtTJrlRjI9vqPwMSfyBkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoO39bTl9wSMxZT1j7zfwyerWoDuXNuIVnuapfj3ncNdFm5gA-H_U_BnXgA9oSavC_8PVtK6L5RPXGHPEhlAxEoMeMRS15kc-iFYAARY-eql3jnCpRA0RLFPxlNMPqWIExL0BlioG_V9ml-C1N5Md9oxKkyOqPN3RCA_ywT4Ri6vzui99S6NcAReVDKXk-NbTnO3SzgglspuGWs450LJpFIHMS9Hg6nkdsfQb4-HNMbkiVoesMIjn7ArCA76_7Ro76g6XXhOwhjjtpBz2JnlOibM5yvpjOrU7EKcrU2YjjGkoyy0A-f4JBXHMQJlymWaM07Y0auoFCfcB2C8rCYGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWX1aqW0uoILUCLWKdwIFOLegVS-relQ3ii95Y3askH77aCtGsYKTn6VAwB1uDLmdKqeLu6k-ojufiFZ1B7ov02ztoWMVw6le1gFCyjh-VcI9ScuhFgzG_wl_IrBJiV0_LM1CuGXvk5hx5OFR0HWlc3asoTTGLgp-UZ-NUwd3ogZEwFs7mGkMaJqZRTay6oyKFUcC4831fodS8x76HLbKN26OnZawF9uMXBXM9aUiAa0vCSDUaXYLVHdpo8fnhHuxabCto2-46fBAVs5YtSwDILa55DlSOHPYV31D278OyTW2CxO8DGoRH3qTplUmw9dXjurEKydp5e64q8n-j7xow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ECRXZAgTl4u4ps-S_pqi552MktdV3eU6Qp9b8r4zAu1dH2sJzSMicjJZBGrEkiaDMf4KFtwjbLa7nRwLWCgO8PzZttOZ0ymg8wiVt_rknu9bLAvGcLliimAgrTiTKT3D0g4vJRhsBA-mQ_j_NXZCGhgP45XZZQ25IlUDUDVjcR2xPsmWnwmDbpGOXwl6hM9VQoOR7Z0IzZCOj69p67nzvAUyc81he8jM2X4uOxd9NSaUIzImf9lV5xowr3jQC_cAZSJCsiDZ8Cfsh5zq2tu3ONtHcoICV9A1tAHUVbOFdqmC73XEK4NNkeTKQLZCun7mavx9Dr7pf3fk7v7bsAPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtQbksyLXnuYZHx_9kkBZO8OKSBkp7ycsQsxU-U6pE3ZvAL0BvOKOvkGMcHQOKULYQeHj43QDlqYe5aFbpu8Vpdwv-ns10VSrLB2UfHPWDe5uKRrCdz1FE711EgX_fs2ux5Hk2v0Khb8MQKGhT4a7xVdWF-A_kDF406MiQ6Nf1Ob0CM9Nd-zTL0EfMxWv7jXCh7LaYWEPLvU4_7YWM16t1VSpoHONzHzWoiU9GZbEYAUAKvPZwydNxsGHnP8nDcZQNyHfXxLQYSjgOeJE3EEAumrHs0I3bnsbuBuXgwj7ew61fqxlp9VATVvNhhbH-oCjdDEGsuGAUnzliuEUvgiCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb_8Cc-0bvP0Htxk752uKiKrPtzi1DVltbZpLGrxS_0k-qwGsr_4p_nLJ3isGVHiqFhbndzmhgv2tEApgQXAhS6VZtinncB3UhoOABcPwBJ3MaCO9RFycVyIXJtX9SScDITVYVSpQXP1yVw_KWhjhegpfHbs_Q1E6W24rTVyhO3jKclX9Dvx22gtSpoLjV3CgJL9Yi7vExpkF5F3i_V2DA_Z8uEmZuyhu38z0EnShAwzf17T1J6jjSzAcuSe2p4MZOt1GuazozI4c-c5Uo23A_nAf2BmGtz1O0l7p0YSZOSO_jT8b_TYNFh0zsYZduCFX-MVhI3qD_0ZxGesTbQdKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad42p_KfNjonA3kDeOPJE1IX3qUTSWMrgtwEasgZ8g-I0n3ozbO_XLyDcRbNM_mIS9GhCPkt5duQ_FUYOKH3OhChif2FA0HArf69IlcoPRqkx-qkBBhpGf-Z1ndq3VJAg51JhlwO46H8vlgz-yT-VSFFXn0i0bQG_t4_Lx4DVOCb8qFAy0_CAQ-qbmS_H2AQu4OItCxjIpdgoUq6cdKB_0-BZeRsbqSJoOvNNbApmZxcTZPnXnPmEuhXvTnlaX7IyE_Xkvpmzrz85UvB8X5FwBJaJksOIpVnrkgxIov5JoggmAPse_LEqRWoXY04rBf9lw8RrMig7MkoBkrIWuOkOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae3SgfcwyiaQJ9bBy-wRKSNppGRd8b9qB-aYC0MGQ1SqzgyY0X9Qf41mYtYgX0gmVn4MQP1xl0U6UqLidANLStucwAHcIjzS97S1FRN0evNBc68OEeid087kotVFLbmisA_q7jyQmx61fnUVM--IgEBz82xDr9rUacYxQGyK4pDGURUn4QGxP2NR6_yYOhvrTv3YIawH_dxFYypLKivPzwvYSKtjBLL6T4YJj8-cxPk_iEBwLpZyOPmZ59IqGwXG7IZCdEV-3oeIeCjsQd-coMF047xpGd5VYKnR0Q_-AST8a2W6vGScv_Ftrq8DK_8Gz8lQmYA1bVK80hRlY0yoqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cetnmg1o-fqTd-0YeoS9jJjn2-a4h7ACzWRcicNHze65vE8uHky-PccPaQwHSCXAtlracFUUGLs2yu92QVp_uwWHgEbxtC2rIpZlPYyMNu4BWSeFk3LslNtvjDWCaU26tRuDxQpz7dRhcr9M01nCmmjNYCYbZfwdU8_Ufa2O_td289aKsj1arh_Lreyn2B-43AL3LX5Gl0BNtPK0UkR5EjlK27_Je7FuI_H7RLBTuWwsnqEVNf5lh8OMSHebQeq2FgDLVfqZ5RWMLcaJk7DrSQCvmN57Jnx4-1oTCvbdGuNK9BakNNk7nL1ylvgZU50xVPpF-zBLbvkZa79brr1Mbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzS_D9Cdy229LE0peGijACqOw2WrsFB1p1ypCqCfEn92EZQqkPaPl89AzTaj2jIM-rguvv9y_ckPaxJzWaBRPakrU916pNsw2-lh98ABVd-iln8Oz0rg4zBlGgisxiTlxgAD5RgbD0BGIcqEMSrMG8okF3X_nlEmUyTkAHOkMPW9PMCg8YpuxEq9SYHYYQgk9XuFwegSuBCeyI0P-BYtIE2YZj68yojAD8UVoCgMj4vjeGZVQIZcRUJOLoWlMJopRNx9ne7Iigb0rWLI5cqfZL1sow8gJPqFtsG11aRLcvjf1zeIC6NSTmGewjdW9gBituke_szSMKbYGMyBWxeAow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=tv9Fd0afOWu3TAO7_eJBC6VRVTGgI_nUh9WRMZ0Zx-UfphDKuNm7aehupMEyPq0lzdyWn9FoYx0ljgprtDq6eHdLf5YvhrlpcQDF6Lr2dfwnMCy2mVFUH1CI6Oetv9O7WqfdIlvKNFHDfCYtpeY7N0s_rq1yfNJzt1QIqXZCbDpSoJpg1wnnbNMg9pdGAtGKBChEhiPdVko0M4S54-tFn2_mJGKuWrQPmIE2fyEwqn6BG8UL2ufhBRqruEn6nLl0kaoERbErc40abUpuS_LCQv5GubKkAyGBwiK3GGmZ8d1rX4YyFC5SQB4ho6Bnm_2yS39QuuPC1WJAI69qadN7eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=tv9Fd0afOWu3TAO7_eJBC6VRVTGgI_nUh9WRMZ0Zx-UfphDKuNm7aehupMEyPq0lzdyWn9FoYx0ljgprtDq6eHdLf5YvhrlpcQDF6Lr2dfwnMCy2mVFUH1CI6Oetv9O7WqfdIlvKNFHDfCYtpeY7N0s_rq1yfNJzt1QIqXZCbDpSoJpg1wnnbNMg9pdGAtGKBChEhiPdVko0M4S54-tFn2_mJGKuWrQPmIE2fyEwqn6BG8UL2ufhBRqruEn6nLl0kaoERbErc40abUpuS_LCQv5GubKkAyGBwiK3GGmZ8d1rX4YyFC5SQB4ho6Bnm_2yS39QuuPC1WJAI69qadN7eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=L1NNB-C2Cb65RNHzjqIlEA01Ggtip40k9HIaXSdz1G_YkhTb_G8AwZiUw3UouTj3JeAuItFru7T5DW3z3Gzcga-l_miCQ6q5GIef7jqJVtCM_lXO5eA2E5eMxpdw5mUW6FDK3ybQ7O3p03zuT6oREgYCUkUuiZZREMj-V3-v66v_lI_QRGpBtMvWsFBfhAe5LCUhfhbnnNR_ULvhsDDGKh8BKHuCc_7f4KYzK6kZVPwXbN-hdPaoypdB8jPHXrFNL_0xgOpzf46NDjhkUtZpHM9w5RO0gI77awqwbaFnlNDTatviWtPMCh2e90mjlvWt8PgTQ0aQsbSzKCn2RN6HmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=L1NNB-C2Cb65RNHzjqIlEA01Ggtip40k9HIaXSdz1G_YkhTb_G8AwZiUw3UouTj3JeAuItFru7T5DW3z3Gzcga-l_miCQ6q5GIef7jqJVtCM_lXO5eA2E5eMxpdw5mUW6FDK3ybQ7O3p03zuT6oREgYCUkUuiZZREMj-V3-v66v_lI_QRGpBtMvWsFBfhAe5LCUhfhbnnNR_ULvhsDDGKh8BKHuCc_7f4KYzK6kZVPwXbN-hdPaoypdB8jPHXrFNL_0xgOpzf46NDjhkUtZpHM9w5RO0gI77awqwbaFnlNDTatviWtPMCh2e90mjlvWt8PgTQ0aQsbSzKCn2RN6HmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csBa9xEa8aUDMhWyjMTSxNCMycclTINBAoZHASuZQA06HfLulDDf0XTQX3kQZBpK4Pdoer86pUVnxZTfPbpP34bE6lwzqXnR0QhNj3QQqRQStqTAJGKiVo6ZAuIcLcxn9oqZlmyt0moUhYVjjtoO27VI9Ll-dmp5RxA0GaqGgyA2fiz9LZVl1RLMfA5u-1ecW2-l-0eDQO6wAwfALCkVR57LwerhxKwz25-c4-1LDgwmN8EC8AKwLLvGR0JFR0QGbpX6AYlEd1m2-aABVvtGCkoyx2PbrNAVs1JTeKb3Nx_QDDd0cczvRSSqwisCz1cT0hsjtbgMOctYk8TqWytIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1gPclb1LxLTbSUDlyYUqUWkSzuBp58Y9F9Pv80Fcq1OqQemKSESoVS8PpHc7BVMyuyPHrkiO4bQEq-Lf4Q0kjt4juccaWT6OBlkHfhHYAeJVWo34C-ddSDlnd3vhnowDr82XF05IiSp4vOfKljYop9eYdQOhW__qBQBPPsjbDlyDCT77-3FveMUg3E3k8rQzZogVYk4BFbzj3pWRUJrp6dgjKkSmBuYFwFHkoWWuCSyuc9Pvm8ZmGJpPVYv9bftmezD8MSbGdfIIBKHnWwFLVIt5AgHhq9_lV3iVmAOa5pFBF2rlSvL9_T1-odR7kHCazUOoHTd_gGD6H3NdDWwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJJnEqiIlkFor85rxQyYrnq-4o3P4uTQUFmPorOGYFZ_2cXnGty-a4H5EQVSRQxcpfKyPgWQ-SlwCV-vKMgAlC6ovyq8de3AJ6C-8SZZ1WiLyfIfhD_EnVHUlEyOPU0AgK5ed14ShWTX3LFHS2vnH5SXCN3whEJegzIOeWwSW9iappEz18NbbgUVLzeHhhJY4UdN2hf4hWA3YVPp0JpcxNnEB3_x6Aaer-uKRptYwfCQ2BWuThMLyh-j9jMQRUYSsny6BoB2hsNlT6d4i4VdF8UuCLXjek0mjHww1bP7_GKhZeSPEIMX8Izabv2kf5AvHF-NT0cjVzIi66J7VC8fBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=HQ_RPz9lVPgnlBKPfBUY4tmBUBR3ogsrFxaxs6muQT5j7i3DdlQY0CbRW6PnhqM_6UNn74A5pEbrIBB8iAQe1V4p3jroBu40HGSQa1bz81TXrmWEwJo319138Q00rNjajJFvb7AcP_ARxDT0zTxLvsXew8HIQqs3SWzPDxABKhUKdCt0r-VnWeafotNWs45RxZUnyU5zLJ-8VJx0x6QN6t4SW0pEqMNuYFhtYp3w_VB05ybufwF1KBGHVfIMzPdP2dtdNCnD2x0ohWWRQSRD1hmxDdOKzsU4l2rNJeRnlCpgRrCtoNHMyribXAIgxbdB5UjjHbb9CDJT7EU63OQZ0xqIGfvbk6yCzmL7r4AX5k7n4RKB2hAqCgiblfejeOW8NbdIIHRg05bQA6Q_n3jdp7eKnJmOAd4bmM-cnMU1buZzs-20ArfA8aNTsfZbD3SvoZ-NND3pKvVWKcTkgkpBTLUyco3OE3VIVW48899V6etpKWAs3HCPqKp9rMhSwvF36S2PB6VO5KT2_bizy11JFM73oO0B-Wf12MCc5fZvWYvPd1LqP1w9VRYNsHhHIMi-vsITS11P7Of1TlvsN91DW7NhqzYfcSXhT0kDkroVIkPVkT0Y8IfUxVGpBhfcVdWYTlwRWVTEDenQ4Z1FUw3-jJMAQVQ_1S1uJT48oL_mCQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=HQ_RPz9lVPgnlBKPfBUY4tmBUBR3ogsrFxaxs6muQT5j7i3DdlQY0CbRW6PnhqM_6UNn74A5pEbrIBB8iAQe1V4p3jroBu40HGSQa1bz81TXrmWEwJo319138Q00rNjajJFvb7AcP_ARxDT0zTxLvsXew8HIQqs3SWzPDxABKhUKdCt0r-VnWeafotNWs45RxZUnyU5zLJ-8VJx0x6QN6t4SW0pEqMNuYFhtYp3w_VB05ybufwF1KBGHVfIMzPdP2dtdNCnD2x0ohWWRQSRD1hmxDdOKzsU4l2rNJeRnlCpgRrCtoNHMyribXAIgxbdB5UjjHbb9CDJT7EU63OQZ0xqIGfvbk6yCzmL7r4AX5k7n4RKB2hAqCgiblfejeOW8NbdIIHRg05bQA6Q_n3jdp7eKnJmOAd4bmM-cnMU1buZzs-20ArfA8aNTsfZbD3SvoZ-NND3pKvVWKcTkgkpBTLUyco3OE3VIVW48899V6etpKWAs3HCPqKp9rMhSwvF36S2PB6VO5KT2_bizy11JFM73oO0B-Wf12MCc5fZvWYvPd1LqP1w9VRYNsHhHIMi-vsITS11P7Of1TlvsN91DW7NhqzYfcSXhT0kDkroVIkPVkT0Y8IfUxVGpBhfcVdWYTlwRWVTEDenQ4Z1FUw3-jJMAQVQ_1S1uJT48oL_mCQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI0evo2cjMRPtE1RNxfUJ2kwy06fSHuXUEuV8EL7IsqbRx4cEdp1yiZS7ih09FM16CRWgx7ZgSzYfVms-120XLGcEke4pl7jqWMLM9uQLECRkqdgHjeunhRtQapPartlV3zbS_5Fp8BcgHgxd55GIRz-6k1NAib_Hv5tnvVBGurUipY6LAxY534pLQDUOOPwF62EOObAD-IoS927ARpZwnl5tENkFWg5usOtbhPsXF0lujDv1oqJZ8QcoU_34PCY1xIUjfNgTsT9j-u2-kuXr2tAW0_rxErYx7INCYJVooENhbX8b05LFAgPRG-xjAAK6ZlMUd211KSG3yv5AlqwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI9tUq4vQIwFDJRTcO5lkVZ5gMobyASAmdTTRY_SERRYyQ8GTi-zhgEbJVdwbnTLb0FmcHKI0nJp4F40z1zN0b2VOb8tOBYjGIXtjKNy_MP9Y6SsT-q5PAAR0gl-CGUe8nLg3sJdWjf75LpRq1oO54P1-fzUUTCtR22ZEx0eiDb3jKbOB28zlH2ie2nIUojiwtwOwHknSCwL-a-XfKwjmmf19u2InvZdwgC5lqPZ0p1g58VSn2jL6UUuNX5Arj6IFd8Usd_FRCFE6MChEL_TLHeQafn4Opsnqpr4j6r-llx9-suuSuBeSQYZ1Q4G6xl_WLxGnSYlZ8qmaf9NOoUiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7vZfy5bJqq0nWaQRWwivHxxoQcTNgQFaRl1OTrbpJa_9HrTR0oG3t96h-AvpZb36YUjtpIq2fLr5PzsdNy8AqOsIfPlp1629_CfSLsjdOichE428r8sjikRCVy3f50E42jHXfimigXO6pdoAhG1-YkyJtw5k6rc1wh73yXWlLU4-9OuoMTvM5ERCAhKHDtEvi3ohE42V20xtKRucw4Dk2Rdopbj_eWAJKrcjLwZ9_HJ9FywF3JipvcI8sKNxAAqHddOppN2FSz0f6-7EdvdsLauwAr35x_NFZ7FqjU3Jfmf9H6Az1dpSbNP-4IGK6gS7X4c88xQy7AGlDN6H4xKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx1CnLWvBCGOLllALD_wmdcudiNgq10WLcMF7E0T4TnhdLWC8wWm4ExjF7iEGvYXJ4GiHngiucfzKXLooPfIg-ggRZsTp8LpGmlysgYLUpe3ax4wF_LMH0a2UsDZazcILHxfPPd1XqraZ1R6jKfuQlK1mn8pwXY_3P8uJEqEFZHN2l0yt8wsEPpSDmsehI0CrY7Yzk9sE9HaCuEOvlpIe-TiYZ70-U7jNFQK8h-bxmRotRn7uq5h693lAlYluG5H9Dp_2L2IPFBRNH1Lsu3h-A_yx-Q1HAOYrT0RKIrYQxQA2XhUYEb45d27CKzGrmme90Egscy9Gjubm85q2-XXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_ZPprlce0E8xRFsGrWx-NXxhRiZnDU4MngqSWIM2HLb8olQnctd3MKfQcLOODVrFCbE3zYRT-6ryGXK3PTBiGGS6D-evBPfKRzzcgU8oHOUZbZ75v0V1m2EGFNtzjOKUzSo3Dvv6eJidPf_zJvK3kFxiEZ6HOYN4RK6vQugt0lIxGaVs5m3PGeuDeic8SgGdyXDOF0gSqn9Iw70aN6nGZ_nbzueqVOFRvsT9-z59u1jJYJWN-nGfUjQZsIp3Mov697x-NilqPjMMUwrMUZ0dudn_uQB33n7g-v1zVtqgcYlMXA75u6ock--H_tsNd-9MtTOdyW7hu4ELvNYDJGfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1INn_4TjIkn6hW9FXrHTsYRzkGoyU5fQLQEaC3S01H6QaTj_ItYt1C99XqwzQBXdnast-MrLXMjxOcLjcLWiUNvzmaFPtv1HuYvwct6DA61sPPvm7ZG5i-oJeHvdUkd4BJqCtUMdT-h1-XZP0p7UNYcjRTjNDgis8hfwq63l1b_2FTYp8J-BWfTnCUB-Ns4AWmX5SL1XbrWjLrOHg3_57bu-0yof0hLPhGlB_Q73e-T_0Ex3jxVgDMB9jix97UFBu7iuvqDe6UViSIsDvgHDOlOrly063Jqy2B8I_q23BZv40qy6iamaVKYhpCSRmwaYwgr_LK3ZxRzzgIiTuMhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=WBFsjRYgiGMzE-evlslaXAxFEm9xvOf1tIF6omPp73tb6cHzXBTnz92Pyac39H5UEOO8RmPjz84Yw2JZif9yElAsu6WSRyQSr_OAukTuGyW3RHaNYa1x_Kby3J5hAaj8hRo18-uBE37BQwo2hgkp37kk7U9V5gpcjVM1sdWOAMHdtkwO4N1W5vcVUQm_9TvSfaf2E6XmVoWPIkdbSPgzQBszxy46EuujKOEnO8GvXQ3E-G_Y58r01hZRFY5BCsSQfVOT8dWZvSYLuAiBk-n9I8VHhC5iZDJDzsU62MeGAnzLwsD8dO-WPLFcwT-OEXfUTJKpsxK66KIU4ZoPZkh4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=WBFsjRYgiGMzE-evlslaXAxFEm9xvOf1tIF6omPp73tb6cHzXBTnz92Pyac39H5UEOO8RmPjz84Yw2JZif9yElAsu6WSRyQSr_OAukTuGyW3RHaNYa1x_Kby3J5hAaj8hRo18-uBE37BQwo2hgkp37kk7U9V5gpcjVM1sdWOAMHdtkwO4N1W5vcVUQm_9TvSfaf2E6XmVoWPIkdbSPgzQBszxy46EuujKOEnO8GvXQ3E-G_Y58r01hZRFY5BCsSQfVOT8dWZvSYLuAiBk-n9I8VHhC5iZDJDzsU62MeGAnzLwsD8dO-WPLFcwT-OEXfUTJKpsxK66KIU4ZoPZkh4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj_MsBcfRz--t6RJPviU22xtDxsjL-kaU_0LCyBYvM3IZqvyv_5FkDSdqSRU5J3xJBpm97C1r8Fu6OHjeHfb1VPiM5HWskMOMHfxpgAZHN0Jld7CplGcEZGJive0qGQicz6d6PASgmGVEYKtJWAzRgSEacGLsWPBqGrc-z6Cpe4y1OD-2fZkIWJxvTKgxKiHAUJxnLIKvtgiknVGxGq32liTSXSDPlUHlc65cF1e16TLtErZ6EgBN2JHtAJGZIcgOC9tAwBYHN_7n6qCIRrMDwaK2ujqMD3AjFDP5qzUeKFd3-6TyYJ_08SkJ1XWP8ERGQzFBEeW_Q5KHiu7oJ11FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIm7lVhZgwq3xTRI6sBoGWzuG6vynQMoJTFhWWjHMMVGwzhCvYfngIrL9EJvkWaCdesWa_rY-YotVKB71M_2ES8DSZZdrcAlfkVH8C_dHCOC0mxLGF2iFu68Am0Zc9EqU8byI_PL1z-XL9_DXEwmwno6KoR_IGcWQW09fqZjzYmLWf4gaMCCDZs_At-9Qvyihe9J_2B_gLIrnd7w9peXmYeSdh6rZm6LqdNn1pScSMEIVHe6Tz7fliQyb5VAYUcm0CBg_w3Bb8g364cwH1e4hjLAVFUEyfY-21NPNErJS0cjX7sq3dAlrGKwumeiBlXCCwRCNRKSkcQp0bxmp3kBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcA7XKokkyHSX0etT39X8bTe5-3_053IkBxJmYNyRTjTM4BP2DuwKJYSm9QyG0rqJIDMya-jFAKEm2xJwtnz4Db17VmBvubb2FfQKNmvpZ5hL3wBy-AueZwIPDyl4-m_5we1vE8jEL61O3KFWJVhbo8gmeS05Y_11jNjyCtyB2chnJH3oA2zDII2H6jT8Vpc-68WW3fS51Hq7LH77j50EK7eYh8KObPNlBBPAKeLx7I0GScK9yJOtTEBq82ZsvwvTq5f_NMU36mHvTLU5ZAK3RSJ361-U_DlpC_xcmO4RfwHXbWFVqOsiMZpJD8suVlJZLhhvryMIhuM2S577oqDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou_vxAt7gmOMCv01L5qy2jhpO9v5i9hOdnqlPWZdHYHD0otXHpQE7etca3DWQAm-DKacI8BF0Yp2cEkG3OXqPi8DlOCU3h6TBdMqT5H69l-60XCWwTUj_pZpSeVDDRBrBhHxPv32jh7rDCf1quK5dhyDo8A4WGwCh3hpzfY3SWCsNKCDIIcKZp2xx0HbnY04aVus6mLko4MYq1Jvnn1VL1qOX6iYw84gI8cv1PIMeVNKvinrlqK3X47rly7BhEgUP-8eAgcg1gIyfLMIos6lP4l1BPyQ89AjsEI2aFgjzm4kBTCdQYuunbPbi4lY0R7RpXejTH1KxZp6heiDLke3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGM8vFFZrdu4i1434aH3g40MGMk5bN7JJYxBXtIfRt5oYIokytIfgBB6-TnskG0s3QaOlbYoNuCJCdFphNJbzhURmvM8uP9ljs31nadVA8yUEvGzDOZx8Q5kh8ZTyhzJRfdGKEE0cZsaGQAPxvMd2MEHdf7dFq8bEcZjR_bDZps8AM9DnQ8nBe_KfL9qCUPoNX8lmeP4hijnnEOzNef-jGGdp8w7b-skxPQ8Z2p6P_PglWb-YKch157ayZkus-DAx9ZKcKnkWeNvdyKuiAbg6PYKgpWb_wzN-BAxP1tDCFc6JOl7QGuJquJ5Ji7JlI4KR09SCJjg8vu4Ui0tN4lWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgSRJirYsRCUj8JLAmJdmCAcFBUnwIx8H70mAX5JZPzetC9yIwB_K9MIPf0GEZVYfgu-FFH3WmqoBn8e2Y21owJj1ecXZhs0-Jlo4ltKY4WG-hyZ3pBwpqc2pxeM9MWdmypc_km5DgmYRWxsR_e7vZ1qI30ej_zWukIt_UCk2Cn1mjsWl-HfHUH1MqKNmPVWxNchUN-fLn1zDzkEfz3Per2IC2Bu_oIF3tXk86ci5Yk1hA4QavbYLSvfVNzEkd7l1AELT486k2TbPO1O1Uvu81slHruO-2JR0vfujjRc_yQMkG-8Q3hgEFgXZqr59AmGN9V5oqzdod5HmWVxyOYwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atL85uV5CSwQliieLCu--LuN1IbLyYxrgByJ62fWtdwOWA6LmYd02UxBtrYSie4XQMmE8iy2PvkiBIh_3lX1Gr3RDS0TxxDqsX2Vv3cifv4DJ9HF4tSVq9Q6EfdxrBiwYNtOLrRV6Kt0FkzKtNqiVdFydjHLayVC2ja6CCUcbF618n3wA24s4W0VTIV4v-WjN_wePng6ZrJp1ClAtEfQIG1xtvB5MirKiStMFhKzTmK8Id0rVnNJX_NUKE90nn2L-VcJQL-4qmf4dt-yaiTAcUE0ko9C5rAvsvLw75u09J2CRDMEjyt7QQDMrGil7TCEAe66UgemRLfkYHnkXCVJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVwAXXSJnbonahuJYCTNbAD9Yw-ePphpMOjv1xJIMKk7OQob6s7Jnf03dQ37zVGBlH8yHSgYd7iSGnqgqm4BhExXhbFn6wRK1Vp8rz1sC1msxCPMh5ho1aJF4K1712MoobwW5xxnjXGXWkG6U6XchnbpqOnlov2EOU0lLmu5mUMiLRGJknZqxhqIyyDdXXQq3BAqH1718PGigzW98iFFJtUDTr5GDvv-SacQz_YMobLEr-07e6VT7cav4ta7iiycGRY9wogX6QHwXU6cn7Q01NKX0YFDI6sIkSVrjCHEQv9BZo4aWjdRa7qHRUfzH0gN3qvmoBX-VlE7Z82a2wuyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZJCnt5qIX7vc3pqQBzJQ3N15N-0dT7cNJ-i6QTSFmiSV85i5KNlxig5oV9Gzx9z2UNgvQTC2UeYQnGcCEDgxtLaBF0oVG6RwSemLWNkZ-d2OQ42_NqWNAYX08v7gC5dGZ7-Yk-frVho7mY8ERsDVNhkV9TekS1KL6p89orYYWM08UdVZXi9QMdcc33R5GSK3vTIJXIEKQfvZ_ME2PQg2jwNl1VF-r3-leOo0QxhqS6gKMydRFEFSOSYFAJiDvL2Zxh1qKUV0SM1dVCbRbIKZy3zQa10qN1lHWvex6ft_g62teiHBgW04uY_FuX7XaAKeKffIawVObhHZoPwNGG0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=SmDrps3LWLMEq02TLsJjl-n-XNqRd1Fi4p8dZ5othdlI0bPeLsnAmb7urj1auqGNCjjEhmoQkxt3vgYrieTjuckujDLeeOn65ugbXwnJlEn-JJsqY2qSp0qQixTUmLDMDBZ04MMsTLgIFYL30ZJov2evRl3nADY4K4plZTfxI2GY8tjKaFVOjo4hwORRhhiAYtpi-fHjffgMa0eUQn3jtAgCszXhAVaLzqwZ-Qz2FwI3osar0EbA3wuV4YEGqKZBIU4SRGbh78IJpptdODUFaFhs-fhoro-XMXUwv4_TYvNkG8UtPyUtSKLYzkxkKZVkrEeAwnlcRwaI9Z0xRc_LzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=SmDrps3LWLMEq02TLsJjl-n-XNqRd1Fi4p8dZ5othdlI0bPeLsnAmb7urj1auqGNCjjEhmoQkxt3vgYrieTjuckujDLeeOn65ugbXwnJlEn-JJsqY2qSp0qQixTUmLDMDBZ04MMsTLgIFYL30ZJov2evRl3nADY4K4plZTfxI2GY8tjKaFVOjo4hwORRhhiAYtpi-fHjffgMa0eUQn3jtAgCszXhAVaLzqwZ-Qz2FwI3osar0EbA3wuV4YEGqKZBIU4SRGbh78IJpptdODUFaFhs-fhoro-XMXUwv4_TYvNkG8UtPyUtSKLYzkxkKZVkrEeAwnlcRwaI9Z0xRc_LzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5fY8A3S5sysYr5-JKp4H2gISHTdukbA9_HUBm5oZG6UMw-yZtcDr9BhQ-L63artIAoWztL1LlKHERHYQ5qGWqNkGjHDL8XPmP7Ee4QbHQjyegS4RVIk9tynm9DpQakNwL-S-pPw7aAoXb97WXg433seb_TDomdlCar3JWjpdpLAxp1oGl6ZDp9Hh9e589O2xpjdXhJhW8In8vNcYxA3zSlDhcev-C1ZFk3aA6peUepGfGT67Q_8heT3tf4-oEUV77IlsncRvHatEytpeS-FmJPDxJ-X3Mm7tub7qX59Unqn-2c56H7xjhKOTw_iPZQ_kFbVu5HqauPH66929FiT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBAbVN__0J-NPwXjfG5q4Cufi622QUPyyDkyoxGc2ldQIJkxEGyXFC_c840gT9VvumyGGz1yFgQ9TFfGgr6S8F3-irriOq25TnkZ0adqeY0mISr9YzzDGuIppIWGW4hHLm4JKyoCFqmA1KHibdd7zcBM-7U8NfYHraj1UwzM2KWhALTuSe4iPEV9zfR8bRNNs7c1vBJxCUNulBGuO5dN3CrqxzP0cIMnT9Mj8HGhGZcDGldzp0UlJuMrNpbmOnfIpsXtEnPVV6oZR7NYDNewt3YMhlbOeFWS85268P0WYUfIMvJacUivrsm6wO7p_woWgRAYcYVv9l8eHFBw3Upzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbccTdiXBrFWtwc5Gejxe9sSUirqwAFc8FHoGeE4xmnOpYfx9vSrW4G83BcCGisSyBV46axjaKOetkH4njg9bkXpXazoAzy2kAH-UFlbwu0eFxyN69L1xXO4MBpRuZvKINN7vvaTPDT4exd2rhOmm5HlOHqZb_5g6pCjUUE3bHIK3G9VmDi_Grwrrbl1NvKjRy25j92ZJVZloiAWdlel1eN64oQHVYqebAPJkAcJw3oXWzN8L5VIKXGSMpThrm3G4quW9t3C87ZrJYnAVM-u4fyfJWqeMiFab2_5OPKS1rzzTziaGfOINEePBq0FBagF2OutnjjswpAh4JuBqf8iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaCQaLayhQoWqMA30PB3FFdYitRT_ebKdM15W205-gsx1KvSfeHcq0DF_WnlOOlobzPZcYbIOY_6hX3dJi5RePD4gjFDjQbPALg7b8vz_-I20_YzxBzk0RcjHNQ-ZepbVTubKiNTinhWBArhiJQSaViehWPkNmnp10GWcpJQ0b7hLxAOvpwSY-PzBfqBra_96m6818DtrFLRP7Jg9PT0kTsP9AxlJ-oMu2T3mllaXKHzJPvWTc-xgT7dDI2SZyZOQUjojSM7kh2QvOHIYk_kEYcYbObrc5JhUtZrC956TFiehGDvw6gcrdAF8db4ABpapDWp0XW9UUdFB3wVqotNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=KGCw0BepJFCNnwDYaDcexBr3F-mPhQAd_0iTrD_4jlyPgRmX_3xEeI2dlajWX7SZx2RdPywfzu71uEvHkKwZl5JSRlfMpk234Kbluqn4MnqBKl8IDljZBz3IAj20E9L-dy3AIHs1Sitn_JrGr2iKAC_qG3x5RDAurFyMuaUrfp2gaRDeoLZUPMFQ9PlxCywJpYkut-kQpd9bzafdWwaUIwAVm_dD2Y0nHBOy7I41WNj9WkMYsWXF2e3QGfVN-pi2VSpBbz9402IkTprFhNwUo5wCaJ7ijIHisTaFoFlp7scf6t_wyEXsbTyG_llv3wCclU1pYbYWng0GhSKAu6X2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=KGCw0BepJFCNnwDYaDcexBr3F-mPhQAd_0iTrD_4jlyPgRmX_3xEeI2dlajWX7SZx2RdPywfzu71uEvHkKwZl5JSRlfMpk234Kbluqn4MnqBKl8IDljZBz3IAj20E9L-dy3AIHs1Sitn_JrGr2iKAC_qG3x5RDAurFyMuaUrfp2gaRDeoLZUPMFQ9PlxCywJpYkut-kQpd9bzafdWwaUIwAVm_dD2Y0nHBOy7I41WNj9WkMYsWXF2e3QGfVN-pi2VSpBbz9402IkTprFhNwUo5wCaJ7ijIHisTaFoFlp7scf6t_wyEXsbTyG_llv3wCclU1pYbYWng0GhSKAu6X2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRMruULWl1pS-b5Kh4RRJ-TNgt1bLmMb_E_m7rtV5h_CtMhfs8Jrg4ovv-8uz8vM6v2zJEm4kc3y2PUdqDFHiQ2iLNfvtIgsAljjG-l4WEJk58gpwe9pb4ZkU5Xg3g0vmimnRt42ptxgLhIjV5hWAgk8dtLh4F6j7CkvEd9ABr-cMfqmDrvDfEHeOWz0jnJkgrUdRXJn8QKO4Cy1-XkF38SGcrslv1KUrAzllZ5VDa_eJkKow_URxYEMx5n0LzyrhfEhfnPDfTsZjcKaV-K8LdeZYrNxMw-k1HqhG6nGGfOX9eDvBCgvUOckN-oHewifDVuMes0UMW_4tITnLy9Fvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=jIQq_c13-6hOJxmc7tlakrAIJc18LM_9XzoPT241mRpPS7WXcQg-NyKTE9f6nmjcZSLiYvDqwf28yN8Jh5co_JIHncH_0SwxIwdv-qF7wlLcWefDLvZGRz7BGApTOXDg827EIo7Wbw7jLG28l6iD-nTS1f-UZHXSWH8UXdQnykCADxqwUzG4057CIRuqXkNFexUOhdRij3KGrBDOmSyLDTqBjeA769VPRd0Mzyb9BuZ5OOyAC0Z2_Ad0rInl2Xx0qBDaFlG7FtqiSx0dHUY_mG6iGBK6qD8s05iln9TIOB4XCPHdslkqvsJ33GggncYhPcRDu1tFE2pII0yXeQEE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=jIQq_c13-6hOJxmc7tlakrAIJc18LM_9XzoPT241mRpPS7WXcQg-NyKTE9f6nmjcZSLiYvDqwf28yN8Jh5co_JIHncH_0SwxIwdv-qF7wlLcWefDLvZGRz7BGApTOXDg827EIo7Wbw7jLG28l6iD-nTS1f-UZHXSWH8UXdQnykCADxqwUzG4057CIRuqXkNFexUOhdRij3KGrBDOmSyLDTqBjeA769VPRd0Mzyb9BuZ5OOyAC0Z2_Ad0rInl2Xx0qBDaFlG7FtqiSx0dHUY_mG6iGBK6qD8s05iln9TIOB4XCPHdslkqvsJ33GggncYhPcRDu1tFE2pII0yXeQEE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOybLMOYm2c-WO1ofDtLO5nC1FgyYPLiIiChpz3xTlLezg7ZC5nBTp3esS3DDcJ3VqKLWBcyMbLxomFylOd5TJemSc4heoFNJIFenTlVH7ke25YH0IL90ArVZNqlImEXtnnaltXIncRJm_qcb9EF0GrdIyRLKQqypBu9tMRyxrbEvJ9xL8pmxgorqSYRh_BTTlbJnoUWDbnNCeNOYRusL8swoyjwTU993rdiUvNyrb8iQccNTqVJo9-AgFRbjfPxi2uTuoEl_IdpB-bOWDYrbJ988t4vjKad5BYGLVD9T7ltISSH9_gFxuRIdmWP6Vl5mJYW2r4b-D_qnuMzFS4N9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtromLgRXmOMSr2uNC_6lrZXiHlFyW_f8QAKZf28saJFS7cJZaL-PK7PEi5T-nZa6rZYVHYUeelnr9yBfPZHoUN8KlaSGW3D-DqnL9hPpVPMQTfHnIQP1sd0beuY1nG018LSsyinXseddJvmCYbIjKZ3FlkY-__Vaeq0_1LWVPVfVyfnM7wq6-rT2nZLsD8bVMXoAj45vviSSxWc0rgG6i6VIWKwmhgdK-Rx5APPe0_km-dl5ZriYJF4OHRN_qwgF3w889YfIu7kJ11PMZTDIAZqIzu2jMwmArRal9yHDeLEijf30DtI2mTTtA1pACqs-vzEBbrMBSvYIjvpNg9L3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=kuPoHD3otESGWVM_RKZqm7Y7HrmgpPNH3bBrET43SD-pIXmzTi4dUX3Y01bmapgWfKm3MMW277xO78Mo358GqLW6gjD6_A9UPskgBg3LIWB2WlAmUO6az_ZQKmH46g6xM5rule054_FNeDabSRH6FR1N70GkrilkMjadrAoaOyTVWxgoJ_urjahdRrpUb_rXfB82qLL7kyNy3WiioJrL93tXatMUWsTxsEksYu-QPMITsrEmIj5AKqlkRbGjvZsv_4u1OfntQGlQdfBn6VpKa4DvVbbMc5_HwRwzbPafHvthB6Kkz91oRd7Xn7cwHRHafBLFTcjCKAtTDEgrShm0Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=kuPoHD3otESGWVM_RKZqm7Y7HrmgpPNH3bBrET43SD-pIXmzTi4dUX3Y01bmapgWfKm3MMW277xO78Mo358GqLW6gjD6_A9UPskgBg3LIWB2WlAmUO6az_ZQKmH46g6xM5rule054_FNeDabSRH6FR1N70GkrilkMjadrAoaOyTVWxgoJ_urjahdRrpUb_rXfB82qLL7kyNy3WiioJrL93tXatMUWsTxsEksYu-QPMITsrEmIj5AKqlkRbGjvZsv_4u1OfntQGlQdfBn6VpKa4DvVbbMc5_HwRwzbPafHvthB6Kkz91oRd7Xn7cwHRHafBLFTcjCKAtTDEgrShm0Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ukg1FKT1IOWFJHJT7yQpR0yGE-AZ3_QAgvhd5g6s1iom0QikUf8F8AW0YR4igqn87i7p9uzCZUcl5NvbF2qZUAD1LDBVzLyM8ImXtwgCupLCsw3_qFeeykLlN1xP6sxuff5jS6L-6RNqtxOX2gLpcAyRdlh1-5gCq0U4GEmG28iQSr65SrQPadA56SU4ITquTDFaX5-mIO7xV_sih29KWRLQe5yCeqtZW-w9lrRnMv-DaQspkgmMsbKtSdn_Ql3UZ-dZEE3q-u__hP9gzYQfrKI7Kg6143uOoxhcYaVQakO8dUzvO9p0cymsr_XAbbU5HXo5pCsCiSEvMNYkxAEdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYByTzQoz29EF8yvn_1_jbPC9WrqAATFEJE7zeykBKErCOmGkufySbdvWUqnkH6BwOD3FBfZCJd51MprD-T5eoWvL9EnWGTMofzlM4vBMevXvXXnsmGqQo506KnVbAAL1HA19t2GBNo02mBZlpOhrHuoHlUZNjpuBU7voGG3PN58JC_m7R2T1kg-P3RryaKGTssOGlXhBETp4pxmdRvC5eGAAoist7kk631R18mn6uUuMwiJxrFW1VDVj9K-EGnIt8uh1dsvi2hP_EFBnngzZkO8BHYaU5JqwfdxVpRJFWh9UOPZ_vM_LSc-CvcqTLFEDw1SAfXA3-SPfAfxalXFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=qtY9Ylp9gQSzRLvEkb7Tg_NnTRrZwp41TajmmCSMrpIIb_98Pu6QDA6wOROIfr1mKGiJtpFJRzX-2A0lWZuAmzk6EnEciHvokiFhTtuTEH3fuDUNapJ2RPSu1XaZHqBUi_BC8QE8Eivq70QAHeoJDtB4yQ3OM3L0j8mTX96zE0DTbFbScjtDtIzNUjwd1t8Yh_RYFhjfDwGfOj32ljGY8GvDL8trYQD1DmSChfrU-GW_Mmg2hNb4h9cZd_xtwYGggxmcEoUZqTmXVNYZCN977QCp8KDEhh1pVrjkDTQniSpJ8007-YNgEoZ6yaZvjsSdtTmITyFZRrJhJMUpQ7_1pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=qtY9Ylp9gQSzRLvEkb7Tg_NnTRrZwp41TajmmCSMrpIIb_98Pu6QDA6wOROIfr1mKGiJtpFJRzX-2A0lWZuAmzk6EnEciHvokiFhTtuTEH3fuDUNapJ2RPSu1XaZHqBUi_BC8QE8Eivq70QAHeoJDtB4yQ3OM3L0j8mTX96zE0DTbFbScjtDtIzNUjwd1t8Yh_RYFhjfDwGfOj32ljGY8GvDL8trYQD1DmSChfrU-GW_Mmg2hNb4h9cZd_xtwYGggxmcEoUZqTmXVNYZCN977QCp8KDEhh1pVrjkDTQniSpJ8007-YNgEoZ6yaZvjsSdtTmITyFZRrJhJMUpQ7_1pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbJuOH-sN3falLTEoURkVsCZ0ZC3FYKv3yHsVcApm258hbkflQhreTcyUgFw0C8-mvdpeBjMYke4nO65Rv6fEQIiL8NkNdju6KWOYVrc7mohP23mLI0G-yANok-cma6xOl82NYmWyM06cwVNcpPpqUV8C2-10AeUdBlZcUKWl-P5JFfL0YurlNkMvHsaP99uNMXDA0a7EcBIodJaFOOUxZTWhu7VeVetaz1k4VbnIFTUCG4MveiRdYeh6mnPbwYdXkD1CoBDM-2CSilxbShEptq9asPds28M-VqMUi9XkWLueVHNxIRHBVvEAfAcb-WUV4P_z-BIc1ULKzrQt9vvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiQxtKKzIe-ldVmKCU8ciJIKVrWDxYiF6zAu9XgjV5rQIIZZAoNrhwh_mAFcNu-TNzec4XvAuBAaEnLMukZkoM5sCl9BAaBT9JuoE-9L13O8ih6U2VKkriep9HgQGylzAFF0Q-au-_Jrlc2LSKtHLmk8vXwBkENOSJl0WXb3iYjZmgD6iXESWO8NoKhCRbWlUw_0q7cKf3nbf0KTt-0MOsWmc9pVlKGVPK-_9Ve77I_C283jWcvUc6JxTOykyVAn3breYCiP7Jkq4lBxJnfzP5tTYqgN6idr0x_dZNfTlUypI6-qEIVwCV6QSijj2ZURbs8begRldTjM1lC2tl-jfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2JzHvXBr9hNHZsZXgC67fNyLxzlg_1pxtDkvJkX5ni_0WcoMT4DPJXdy2P8hslcxJrxxMQQrurOqTX-GgfdDqqEpeWeHA4Eh5OrRoNUtSulTgOhgzDiytUzdgLICdcj8ocUxGtIbAyaUv75ORJgCME4dfYzsgiq4fooOz91JmdY4YoYtI24dkWf50_V8vBM9XwgenmJ41GmmltK2xgZOmqyUEpyEbJPoYaC3eihQdrZ-d35uS2zWVUKMnDoJ3HYmhU9obn6oQs4JlHvMa-o-1VH_f2N2iuorr0alOSvpueK2gV5xPXdnbH6onAs--3tX0rp7e8kGFAH-I6QjWfdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_9lbAUyq286xEa01aLLMNNvQ9SEtI6nOIKmcRffUT9e9ixNmQursfBpxGNNOf-YbMEF_Rxe0DUjcbt0dBmaDW1FTSmCcamACDoRHYEuevsKPk_gsxzx1BCQgHHBtYVgti8ydRv7U_2EdJwAqE7BIqx1RCYUuppDxA7hlrmj-54WEw9HsdGYWzTzU5mJHaINsy8Xm9JNDOoZKzgEnv_6iZF3fQfeJDcfZVGv1ElVJt_mHhy7swQrgLbKRScpWdiP2reCgPpr3eBQ0IBby0Px9t2m6kh1N6Z6hA_OhhoqNcFJBxxq1FWN5yoy4U2pImRFRS_-UgRx7xgyWIcgxlMRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG8zBv-D3E_wCP7kmC_sHttq9viKVhFU4CC2ExyGB8on-sxei2pSvi3-QsOESLMcREkF31edNsqIGhsdwfdHl740Mmb1Vki6jCDpUbU4LKBsFGmF-oGtSqM5zqATngf-Hl22J5VuG6EtGZnVB7IhSVY-dTxBPdbogDdmAYe1cRtn1g7dH_Kjzb2My7LByrQ4MCXTGhhTJV4bS5SkLow3LKUcI3PBr9BS2eunaTkp0sM71fidwZG-iG-L8Ux_0RhNYBEfqR5cteIWyqUHcyJJsCDQaIVW4q_xCllbnPV4bEoajvQ2WcOAOvhzQXrYiBj7QB_VGVK0OzAchreBDvngww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnF1mw0btvHWw1Rs5HQteG5FpBG4QYYgahLk0HEMFUaolr0eAo5jocxDyoJ0qhSeZ6F0FUejfFdGIG-4_nOAUyX1nPGFylnfzwFj4bRO6KbjF302a6E7dNgb_IWAZdG5iuF_uKX2yohpib1wBwoqqrcyqMUiyqM1inllad5GmXC2K0C--BkJp4rWYh23L2jwhkH5qMF2F29o23cfXpO_bu7P6LhVM42DoXap-6kmUbI1ExwFheoxPaEzv2ysrC7g3mdOZ74WzB0PLwaq9Mcg5iNUfTrPariqoilpXIoU_ZVw9oGDKi0FggB9nCknsT6V3OiwlaIHl4t4KMcfXITIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZmx0ZmYM4JaifOgHZngGv5Ls5hdaULlKmfLF53ephga4w6cfN7MPwEdDSOKx3sMv79uL71jwYBDXp2YNQgmk2erl9jmTmhDQlDQmXk3V5YEbxYCTAFPFo9yrnnr571CTykcmyDmH_I1avNYbk0ub95Nup93Dg9NKw5U7cApQ6HDe_nK-ZGcu6FpWWmpEprjggtpIpnMIVWFb7tr-Za9WJM8IkzFoPez4WrXT4-Kcu36jh_xRsutcZ4FaFzFqIbe2_BQrL5BIlncnsYycBxfZPAagnGOV5TwfVWqvSeG5zTQleoABTaoHuP5CJHJPIXNxGi27ca0fnVa6OXt3MBe5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8plTDlUFFr-zJxK545uR8niHdWCBUATu08m8AtgrWJjr7ENs1umDyt5zV-VySE-Rmtm0J9d2SS0OV7mbx2-Rn2IRSRDwiS4epmqjmPq-aAykTuGkx92by_wsr2Nj3gtSyEONmYTmcx108NC19uSSRGRuUUgOmQqnF8uz74td2ngJUQ8w3MbJ66kX5rfKhxangy8u-IGWPWkxRgcrjNENw8bnZId18C-P4WuWnwkUhiSkm7a7V0dfHLh1HyGq9_SLvUa-hgDPXXUjCqCB9qGvVxfXkUZsUlP7ZSivBDPIaaYicXGVnmm7HXFvR9t-8g6_9i1G--fk3eA5Q0Wz_bewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYR7R77Kg8DoGr3yjFrwHJ__sAZm3znI3HYWBZar__IMO-tVaIgZDmNqYAEIUJ5Pf_P-m16MGExw0Ixz7AzqLUiw3_Q_bqRyRkndleY38_euiP8n49Cpfzql0yUxegCe__rsO8UbyFGbYBM_-UzgKsAaovvlp03v_9nE6XfjXY8GJgkd1tF3pka49j369vi6fqI0gPtNvSjE_jRrfx74_leEhcS9KOfUK976EGN9AMh6-6X1XclF_WWp3oS-nXaLpdHJ-Xm28WzzjiWWfQjyyHhIO2_uL5j9h-LPBaa-qk6LDdk-eRIfukTCcT-Mj7TqsqxwlHUgayz__gf-a6zw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP8K2EFAXb4JRV-4kPehZIw1Nboht8J_-5-3h1NFWHz1w3TMFv2bG3ZFW-giULZxozYH8jqd7qq_5TyaRDwDnlh1ffEXHXkG_P1En1prFi9yDH_kQDJBUHdNah6qWt_d11Tpq39drtfdBVtPIsYtS5Yeqh4NuN32HuFs6suPC7aw-ZKg19bwzNJxXnuATBIhKRlXTdQcHOyHZbQbsdNVIL8vDZx_AUXi5HfjWrLFb8ibeJmtQwiOCDcNC44V1rNYoPLMSM_uVpVanR7fXc6qoVWE4VlD6cdazzbRcI7ZoRSNle9w_UIZTtUM02Xhwr3BN6NvBwnmX84x3MPJ4og-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llTbxmrlS2L09eBdiiatT13oaMsgi8eRs94qVb1PWGDNXS4kBCq9zQ32dXRteIbWR4cZAq1IPjB6RsdjD-2ZWhpq9DwmmztuAh0DaJEbnrZ17raDJNfDBVLhf_JtzglPQ93K3CHEFvNOAxsINbep-chClQUe_4BMPDrnUjJ39_FcHpNlrgUO9ph7ecAB16ac7yNVfGnB0INe7K_0Lz-FbPe5Q4KXh53W55VvXpX-QBEoz9dPWiPFSkX6FPlL6FS3oCck2rQWbeg4EszPCUq7zrWE9mlNhvjZmbnIX9jBxJ-UUha-HhWk70fOgMxwJHb1vbqxHKf9ouKIgSWbgx2AqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4jE6dNtZ-KASKntPDG2fMzNBaaZF4S2PQ426YClHX_sGGT39kGIPOCgEJ5i_JcDaycF-xXn__4OqnjvhembHUP3jFWv0mn1Fj8WAtqnTGuyaMrS_Sgcv27eSGv7UXLlOTELeHYvCO9qGRyPL9DH2nnZa0UHhPj6Nib3gm4-6ZHSlWxOXICVOUFGE3bZGtouuBn8lTgc45lrIqwi-X2BXTbtMBrcb6cJaeqRxJZDXGFS5H-9JPrVwKWXA-_vDSB-okR-7RGdaKcdfty-VspsVk6zalWLD3GSotlAiVauW4Zz2-9v71aTDMuVQx16z3-Fb2wFibvImye15-lnqPppMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
