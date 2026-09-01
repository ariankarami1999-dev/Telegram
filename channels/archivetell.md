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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
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
<div class="tg-footer">👁️ 987 · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNV8tabVb3KBCnAquI92FBGjIJu0-oKreJNg2bXK6ogMImYy_LTwpRVPUnaojEotbGZyBwXsq3DPCD-dZakEzMoMGRgabOpXYK87J-YD8HBflj6zaejWFmfUgPbIBTwVJKP0PMONDgZHrWMpOVFkNjA9IYmxzQesBqjlGLf0LWPUei9e2oZhuRt9SWd0oBb_tw2-u2Ei9lzKZwXsB8IaDc9BzdXKhkCQiK90kUTs8hDgNLWRB_KsSyJD7ZvQMRmT5QeRsern57PYv38NKK-g0jjsyzQGwHhMSSWOpwKJMVCmQFQAMhbnH36dBBQWrnOZiYy4WxEhJMF3_yw7eBcuzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYwTA9ZMon1CD29K5MF9-Bov2UygzzLy0ILa-ExuZE3JDJo5SQTGHKHbwCkX-NYK0jDen3pV32hpztCzAbp1LCSq5jHpqtVujYQuBCS_ZpcJt6JPxY0smOAL_dFGLDbgSeZyc7OUDmufzOYHkMfVDEK5il2JUL7W8xkRnc5AweHqs5JyRBeKjGA1JlNaa0159wa6ivU5T9dif5x_8ayLGUpYpOWeNI8VmZPvnw_IrhGoqkoKtRppi9kOwH51P5JqHZEm3VPrPaadUfO4XZfVzXw-lyo0ItJHyIM4Zh9PQ_xywzKifIIANNMI0PNfBRRSPWrNAZVX0_bv_eM-hqp0wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RISTmBN5846XjSXJmSYwJq2B6YVNlR7O34YdG5l8zWCApQd4VNhBbMmBrJeifgVVIGYHSjLEFrxd9ASRE2C-GuiGT8wzDvALaaT5OXLA8WdDAP_iziJWsr5v5fkI_MCclR5WFzAFjfIdP4-_wjS6fG34hEl3_wJh7MtH8y8bFPHmJH4vvFyEMZBaUOttnDQGi3Fe71zxOGv2OQ3fQehESgUUyH0UViRP8yrMBH3x32DLu6J_CU7HLo3ZZOb_y6DySg7WHp61gtJjkaNRdEnHL18BsSHS3rrdBYCjmcZbTSYX9A121Bszr4oNHLkDC-X_LibplCmpD-KStoiFzx33Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlFdZ5xdruP-lqHl3hsJTLROGw-esVFgXjmqo2EQGGsNF-nL48Sq9TsyB_AAcp7oU9US5G_ZHl6sg_iYFf-4Mp7hccpK8jn5hOUAtZ_Zy-kX9AWbez9bEOaw92q827SElLqb55PVyJX0NeDr9AzyAiu_1lHAue7NCnHHXIi-CKwkkDNUIzHGKB4X1mb9hVX6LdKl1aUQaCN-yaFHBccVNjwsYgFmP5ffxPyys1bZyE12dqC8YWjKVqbLfoyxn7WvSUC7BudmpuvB0JDcal8YO9jhmD1fhAMRC26E92M1R709n8UeYv6fxR_nsXtHxjtbmMxaD6XCR2pw_L6EBzg6Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_bt1Tpw-13GT59Oe3cyOcjWcUZjgslpn6ysfjrLArtjfTlVda3hOFl3rFcMWUE2f_TUnHrUvj1ShX9gwkUbi-zPieWHAE6PSFG9-89ieyd6pTD7RN4OMIS7fGcQmx3VRyXWNuoGOeprw9DT7e90s6eP3IAmf06VBvgJMpi_Z4xn8yWUzSlgnbjPg8gmKt6rpdH3tW3GKF--arTfb8us0DHBHtbyGa7SpsfvwIA7kR3v83AQyQ7cOHINIJpjEK5bTj2PryfNF9116y4XqLhYei336BSfzokNzYydgAGaRBfqHc3_r8-MoZQofIDuqXNlc6bHHrmLkTxKeoPTLq1thQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtZhNv7PFRXYle6OjNEinND1KT347f3QFdbpuKL52hy2GA9TGE7uMgMzUFQ53mXlR7nArJkBFhCBtJomHXNrHaCJwC_tuy5GB0fvGefVOz0ZcxL1N7QHW1RI4asjNLCh1K8Q2HP4UFIfG7cwPklY4k7R4IZEK7QpugZfvkYOZvZheyQHH_nHfpvvRmwjL-4nvD9kL-D801ELvnY0gsVg2DCkR5w32scqB6wMs9uQotm-AeX3NBnzMiZfPABZ7B3QAaziIf3gyZAzlQdLKCHVicNS2bbn9IG2_WV-d78-qgK7FH-HE0Y2_pjITpJidEED2DojRdZScLj02yc0ROieIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=ICkGZESC0Vw2MAhUFDEYDNN53uu7PfenHtmWSg4G9DqLcyvEXdtpx5Jq6DdedX-YORI7kLBIQxqPoQRMS-S-MSsDFTjAMy7j0iFLXxJd_6Y96KNj5VEd2QADH5IA7uGF26Xkx13eK1FnBj2BZRoJUXsnPudde6-M2mG-INO6hwl2PfjWKpgGkwoL3gYH4lT8zevg1xPYh_37D6EVi8YEgif2ycpkEQG_jPAU4gdiBdBDg4nfjukjxp5K0RMVidL9ML6pU6ZcgzVsMDGjZQri2qgHaLh_DWYOxiLrf2GgRNsLugs0jIAlCnlfbFIqapEX4s90DVcibfxgpigRngGhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=ICkGZESC0Vw2MAhUFDEYDNN53uu7PfenHtmWSg4G9DqLcyvEXdtpx5Jq6DdedX-YORI7kLBIQxqPoQRMS-S-MSsDFTjAMy7j0iFLXxJd_6Y96KNj5VEd2QADH5IA7uGF26Xkx13eK1FnBj2BZRoJUXsnPudde6-M2mG-INO6hwl2PfjWKpgGkwoL3gYH4lT8zevg1xPYh_37D6EVi8YEgif2ycpkEQG_jPAU4gdiBdBDg4nfjukjxp5K0RMVidL9ML6pU6ZcgzVsMDGjZQri2qgHaLh_DWYOxiLrf2GgRNsLugs0jIAlCnlfbFIqapEX4s90DVcibfxgpigRngGhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=ICOXYKQAAGgdkxL9y3Lfk50y1VLAR2m_AMDaYpUYCxgPuAGH7Q0sFQV0gB78M5dkkwHCXiHHHp_UmeLOJ2ki_JotxZ5VVGdUxzYhUcPP-_pfums1YASGfSa-XqNR1mP8kvkz_mj6rKuiUMfTwRRqhGbS1GgfgbsIxv8-_4mbCDFLk-eBR3Hj8_ujgGONyWy1NChThP2boz0X0b5cx4aGFLJ_yRlBaqnOxv6ofyz9VKU74-hINFmGbZhkexyOzaeswDbXPwTyPtIn4ilmEVoWfOGJPPNtC9u3ap9mbezpSwfJEnpQe7c5aJMaWk21DEFK67LA4khV4CiYh9tR18hL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=ICOXYKQAAGgdkxL9y3Lfk50y1VLAR2m_AMDaYpUYCxgPuAGH7Q0sFQV0gB78M5dkkwHCXiHHHp_UmeLOJ2ki_JotxZ5VVGdUxzYhUcPP-_pfums1YASGfSa-XqNR1mP8kvkz_mj6rKuiUMfTwRRqhGbS1GgfgbsIxv8-_4mbCDFLk-eBR3Hj8_ujgGONyWy1NChThP2boz0X0b5cx4aGFLJ_yRlBaqnOxv6ofyz9VKU74-hINFmGbZhkexyOzaeswDbXPwTyPtIn4ilmEVoWfOGJPPNtC9u3ap9mbezpSwfJEnpQe7c5aJMaWk21DEFK67LA4khV4CiYh9tR18hL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB7PDX3_MSkFcjVswFHJxkl73VbzK8Ukhdd5Bp-93bQ8l7E2L0phh0siFLGAYe5phWmiZ8a45WgXy_-nurE3SlpbJoThYkbMHNypJUYKHZ7zQEOQ5xkgT2_XsmDMzWO30Pj5tWsk4csqfIfdc10t7MnPFDcBFM50Xwl1OENffNihC1muzP4TzTPc2XwJmtLCgMQfBXGG-klARzTw_i6NMxg4NFxd8MuQNK59Fx1z_eGLg5PF9S9SLk8rgs6xxSw5Am9Vkema4rTQnmpNbobibLzqvLY7hc4KcuTXuiD2n4D-h7k6ys14QUEqgaGAS8qnbw_WAPEj6xtUE0JGYObyaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub-VwIM310xv1dQHqwLgi_z1WkGNMTVWlrL__5VrFvHGdHEVLW9d2YrUTM64eGVdqAdgx19LjCvF4hkA0VcmhgzgMcsMOh-CP2vWFbF2WSZfc_XjlsUWkf8AFXxYTrTphGcC5RweM_1kOF6P7EcZYDlQOx21fpkEEciorYn0k-4RW_cqqYxsq_sEMgyjAxdGiBvqfGdlcPPvZo7K7sTSO7U4HMETH8asR86EtwyRqjcWwp3S02N49IteDjbh8-aunUlhjlbCa_hzTev4vD00DIyui_FBk7gJA8NVlunifk1LX-PR1kN4iWvUdaznntNX4XFp2HYgC74h9F-s3nhOPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZvsAlorJ-zcrLRBxey_hRrKaCn9CzRPeGFwX1qV0iNoT-eHNabsO8e09ZZW2XFl_P0nK4F_RMsPTXy-pEGMOmBWY9SXX-c2LnXd4Aq6IvPCkiLf_oqI0KJWxbNGVZL0hyLT_0y-m-6kvmNucTriW6IgHlKupHKLKik50JO_7p2NNIbr6HSM3DMsLwm4cxtIRJQSH8Di5KKOCVlu2y6M16eRAMu7vv97ayvrvLmzuyUxHuCBpWPk6qzFm2-PG0J1qOxEF3xGWELHyVj-_Tdq1zjk5-l9p2F1aB8F-A-vNexISursw54R-sriBGF5QNQibiKZZQL7tN4oNCwlhvSufA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=jyoVuBwAIa_sd4jNZ9qhQ0_E7rq_QwNDIt23UCEp6Sr3_rxUusnnZhqqlBhDz4Q4eh7FI0vjYYDrQWm5qoYKos85wKGeN8nYQyFDRb_lTAG9Osm78Tv8qi4hAzcEFp0DqlS3iAu03RkgSHKfyAGh6H8KaMAX-yRh1iUBs30LXxZBhyPSbbn5epxXbW1UcM2_Zvyb9ruZiSMFSIRhp3slzbXLSVsKuJYbyq5pebcLY4mW5_3qYEn5OjYPjn2v4Q3_ndDQAmisdLegpOUZtUxeJKQcTW6CpfnAc4tlZ6fwSrmoz9ABNWuHPmvg2EYD7gJYg4GFmPDiG2DzeabZa1B3vLW21SQQlFpHHBFS6RLPMJQYsR9R5i-tMWbpgqcmnDnrLdvX0HaN4aodFENeoW2OUSXXKwdynWfq8sEUJHwy0lRKJV2E2IyN5g4E4fXyCQzq7ZKbomuvg9cDX2-VSpFnsz-nIGMhFgJILUd8e8Lk3PJVvAHdbPYP0LJUL2IU_brnWCNnL4qFx73tDudL7rUCHuVtZ-dLT4cBodWgBYRWaZviRurgUo9jAHo0cW19Oo3YDyHfz4KaXhNapyqEqw8r0hcDcKX8mTPK5xUQcG5_smLnwyOgvGHLFwy2kH4Q9NLL3FSzK5sVfeTX_IN6Y1reooEZFin3LYKG_kjzSYHdCBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=jyoVuBwAIa_sd4jNZ9qhQ0_E7rq_QwNDIt23UCEp6Sr3_rxUusnnZhqqlBhDz4Q4eh7FI0vjYYDrQWm5qoYKos85wKGeN8nYQyFDRb_lTAG9Osm78Tv8qi4hAzcEFp0DqlS3iAu03RkgSHKfyAGh6H8KaMAX-yRh1iUBs30LXxZBhyPSbbn5epxXbW1UcM2_Zvyb9ruZiSMFSIRhp3slzbXLSVsKuJYbyq5pebcLY4mW5_3qYEn5OjYPjn2v4Q3_ndDQAmisdLegpOUZtUxeJKQcTW6CpfnAc4tlZ6fwSrmoz9ABNWuHPmvg2EYD7gJYg4GFmPDiG2DzeabZa1B3vLW21SQQlFpHHBFS6RLPMJQYsR9R5i-tMWbpgqcmnDnrLdvX0HaN4aodFENeoW2OUSXXKwdynWfq8sEUJHwy0lRKJV2E2IyN5g4E4fXyCQzq7ZKbomuvg9cDX2-VSpFnsz-nIGMhFgJILUd8e8Lk3PJVvAHdbPYP0LJUL2IU_brnWCNnL4qFx73tDudL7rUCHuVtZ-dLT4cBodWgBYRWaZviRurgUo9jAHo0cW19Oo3YDyHfz4KaXhNapyqEqw8r0hcDcKX8mTPK5xUQcG5_smLnwyOgvGHLFwy2kH4Q9NLL3FSzK5sVfeTX_IN6Y1reooEZFin3LYKG_kjzSYHdCBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwBEIk4FgSVcnDCtTGUq9yg6wW3OUAB8jIegBpcvQzOkj29n7H6sTqt_FDhw7UoPg0iyLq2ylWm_SNZBQbmmnw2fUOuNPwL886w8bW-FVJsMtSpeyu3ktgUtyZBAIkFJzoqzodwMi_qCJothgdWHYikut2rY2eQOzLddnh0x2Ga6CNo-KSy-CUfcg1HbWbPU3l4PNX59bu0UpiM--CmazAkWcA27yNVUA29xJrUPeHFLy26FM0eWWolDKdgj5DyczDES0ntkXHr90EGUxvUUp_DYtv8OcLdXoy2XI1zjwmNznD3rAg4Q__AoLFH42LabOJcVWp3oYBb93_wb90oysg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4NyjL0AtgnMG5yE68WKPWtsJ6HiL-TB6dwV-Ey4gV8yJVCdUAUdZHSqEl33u_XMUpGKUVEBqjdl6ROZv6qZ98JvLOy6F9vtsP0PPafif2DFY5tKJO66vLk_W5UvU9U7JkA8MDI7m_G-_pT6XNfJ0AwZD7qyJiaezrSlUUsc2r-DAQr18j-u_5yeI4eJ8EfzY_SN_TwXyXOv9-8pUlRfkV-qGqfQhtXK0IqDb5_UGoKweQYOePwxd1mLbE4KtKQ9uxzYwzjS0WHdesNgrOf8w2e-AOWj95cpIhC7EdCZdp9_BqmPoXAl-Xgbv7fHeLhPnibp2DQv8B3S9FIj1oaCiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfa7MkrZhlRZpugQ4b3gK4-9n3GwaDy1mtvNLcmubDHF6kFShx8YF9MUputzLn2BkRxkx2F6H3otZVX7qRWB6fgnPzmUUUt6U0MxfvSImnAuPxOpigULi-CI1DgBHmVHqt5E1rNFSVwnEGZHRDQGYyAR6yNIacVlc1pqtNu_9tviXpNwU9aSD3Eo18khzsSC_G5bo80sQB3DeEXSOCVaHxbwjcau_-6u5xdpPNSuP809gpH41fW6XGfwXlQWpDQMkRIax8bh0atmPteEFrZwvMzjZZsKmzrm2UXSTIu6I3CHFD5sHlBFnsE38KavMymaog04Q_Bdn5b_WL-J5lIkHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwDrG38qjBJH3lP9_WZHkUD0I33WT7NBNZb-xKWTLzhj7U57RdCIWRtugKolvb-UjuuqdOBLZ3TMHLMSzgGRu9jAFoxJexBC069nfuVbkGsJQj5vb-mG9fCM1QrJ9ymTQcAtD09rODLHoUHngsflqqwkXMyHLxEgpytatpDpyL0tp70j0RxAkC8vf0aT5GA0__THtDmgpE9_ZnKhMp3VR0Ti_rBJJIVcc1ioiry6BFnSwFyKZ-xxh_lhxhEJXlOBaOtIz6kPPxrhwU1EIHtChfEy7SFihkTRMFtS4BRMglSPLXZQ0RsA2ZOlLV_eluO5NRnT19ltr6c7iwjMzT68NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2YWxf378qkBF8d8vSrfk0vX3hs91ugbytfFgzduOQS4IcXytk8arSTblArhKY8qinmaGeXFvhtCi7XStvAQPpTmQ8tcW35RX26bChGJDhaTD9G8Vgr6y2LVjhBviAjCuVJX2YHA7u8AgEPj7PQKrADqDaFRozCmw3uzaMw-QHlosVss9jVazpoza49H-GyPPmy6-GAhdi3elx0amU80YqNrD5kKSbZFtFiXFerolAO7JHIwEWx8HubnJ23DKKTeweeIKrAW2ecOp--TuAnm2Hw74JnUwjAjxZtTFXDbD7kpFPicJYc5V-5FFTNj6VpbPMSpVbFbHHJowBCl7zpy5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7-VGh6-9iw0i1apMyPeA93WCHPipHuYad1Bc9z--4YqmbAdSNWnBNptGl0B8XpM5DAGEte0uOWCfjSYLoA3UcIebF_2OucIK9zfgm2hqpb0ZzlDJnz_2-LBJN2oajRFn8EX7FmTolUMhcUpi_zu6HneImgwgKPrur6KH7q44ax7DrBLOVRMcYSRkjUEHQu8zKtK_j8SbERyiUWkYxnuFVtWJ2sJzEdwUKxSg1B0155jT3qup-fcX9YeujBeb5ld0Zm2Xl0qqXDmNPlRQ3m6W1FRVMbAGEhABA8dbfcrcjAn5b1XIJKJv-KwXnSaNFJlwHcqM8Hc0PJn2xUGJ-BhBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=TUYXLHOKfOVDaeBABvzeg8vD_xiTjJxo9jC-bYk1818WJwtDTiNTDyAzI-jqF8whw63_ehCmfWoaYXt5Ex4hVnTnJ1aA7OH5Zr91KVz7ZNhbUiJ7B0s9sC2KejGuFXE3TVy6wWpeTeioKFERHO6dGQhz5weJjCHcbkVvkH3rc3n212_8xF8UT5JgnF6XbU0gYXkbc6DOKlBJTZ5rX1JJUXrOSHCyDWD8ZSL3uM2ooEJDDVvPOoSbZqOWji_cSfo0DiVV2rXbnJmCvO3nPQCQ_srovq73yn7sScfoOsl_Vhu2mmxnEge4vMpA2GUJzpYFzUZQARqq0WH76tpYCXU0jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=TUYXLHOKfOVDaeBABvzeg8vD_xiTjJxo9jC-bYk1818WJwtDTiNTDyAzI-jqF8whw63_ehCmfWoaYXt5Ex4hVnTnJ1aA7OH5Zr91KVz7ZNhbUiJ7B0s9sC2KejGuFXE3TVy6wWpeTeioKFERHO6dGQhz5weJjCHcbkVvkH3rc3n212_8xF8UT5JgnF6XbU0gYXkbc6DOKlBJTZ5rX1JJUXrOSHCyDWD8ZSL3uM2ooEJDDVvPOoSbZqOWji_cSfo0DiVV2rXbnJmCvO3nPQCQ_srovq73yn7sScfoOsl_Vhu2mmxnEge4vMpA2GUJzpYFzUZQARqq0WH76tpYCXU0jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf7ou_wk6w-cbgZBETDJjRqn7Oxr03Ql29nUM-hWqOKLvu1R8VGXd1fcadYEUIfZJxBZ1_QJ5gR6vIWlcMjw_4AuPAs6LGuH1WNJYx_2nVyLn8szbhDreuOsjneNmUxin_Y-CDenTxN_SdXOEwS8XOy2oQwkxpJZSo_f-JDAIulsJXc-ZGMVg4tcigA0qIlLoguHcA-415faGh8WtWShIR54HRE7Mk8HE2j7qRQzaJkW8kzHAlQmwToql_sUucpeQSMueH-dp3pqv501hHorNe1GKMqVX4NoV1G1dJW8gJPGNwGe2v6MRpPjGcwNQ7P83_TpHKIr-UEzM8eDV3xRLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkUwC2g8lq8XHotsnmS23LnYTp_9XFe7G-_Xg66ZHMdjQi50jbQB4yCd4JcVMCZAvvU0QCC_LAEhwunAwC4LpH5EUN_ofm5SNt-_KrbIEUa2HHX6tvRsstg6uHqXAuDIpzciLFcwErjjeGoAtJteJ7uBthLXOHzimAKLKPh4RA-w90tYfepx-Mmn1ZVAsUhZBZu2f87JKdUMby9O2woq1EA3Az-lTZxPGBqxiA_1qQHqx47X9mSujhoPgwqe1SU_NsgYkTACpV6ue81YF_mV8lQhSwG-70tzmgzqZsXYJGLywz8gXqj5_aVWWuDeTCOwZD0Sl8Z4-PzRHcePlAFVoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbpY_RSrqDFL03mMvwTragYooDYFMg3COScQsjcDc8Y6j_ivQHWKLEq4o9wVKrtPfqVkDNySWSH7ovjJ8ET28BOo91NhBDkeSYmKA7lt_FZxRE3YV6YESrnSGquUlykGVYhx4am-HWw3AvE-j1i2qXTpL_SqjNv2m1iJ9M6R5AzMnC9RjH3Eh8dgdggkyBbj6KMVzazF7uLMrxggkyN5I9GAyS6gGt-4LsaJbdmtDY2PkVotnwuNGSARDJFUsZ-wAsP0I_R7G9PcJUkQ1Jz2040309Z0CAroj4GT-MezJcma-9Lz8kOp8VbGEvMnOdMy_3h7FBI2fShysWnmEqD71A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v33HrpHLM7AW1N9zjcuMWSXgM7fx3ykGme5lGTGQW8aAdhdbP3cMGsPmPi8Xu5TWU-XB8OF_iFuhpGmLvy8n8MenTGaEIcGtM3dNLhCMc8Ff-UIoxbXtGiRZeNUTC_xBonSSabeFq1IrrxdGSPVxGrrKAGXmo-sth9d32GqcyxoiaZevR5OtI9EZTmokNfnDYykrmthU37ZZKCg7XExT629AfTLk4uSmHDImqtvzGyEV0poyaysdjy8HelXC6fq1LaRZN0i4kznDxgdXtpDAl8ylYeBuf5rJ29fnjx4R5WJdnDut4UBRhXjFtD6s9ELalg7zkJErQbet8pfwvW7Icg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roUoy4AovayEtHJKJTdkUUiY-XWHHbiJ40Oab-5EdeR0P-KJuBH3RRdIWEPPNsp_lRh34gXx7H1NXKo8WcTuJFei9VnJ5-pXLPrjBPJAyJSMFe1tyGrrLHTwi85Nsag1V6osaevCr0PpOq1mxscjNisYXDF4HUQyUoBcRy0QTdiJPb9H95X-soK-LgCB7hFM19hHSwO0LDCSyOAeYg7NZVmeECodw2LxlruNlIjXoCXtku3iV5q1jYMnDART7Qft_PqtIZwg4vwKS7rdBd14O868ni6HjJFm5xy-xV8FflDtTqi2wESmQDPbx8JcCCQCbM4QHIHQ4cI9qyEGilQtvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuPiSKowP6Uu93Ck2t5n0djbxoV7IDYnIH9s07AfZv1giJElku_azxwHRl0oOb0HxiOwwjiVDTn1E8vJcLzXjvTZ3bKXiFF3Rpep29KB3m9tYHbIEulas-wZ_PWx0orUdFMZ8O4VTTO7dsnyDlb7J5vZfRgB7oU93PlzZSXV1BUmQjTIEPmn-W9Sj6Rt_sXFNc0aLfn0sN5UZPqVaSzvubxfWR8Fqn70v5luc0Uf_dp9ji326tbueyIORT55u50KlRsBPHGp8H2aHX-pc2lMPgCwawNVVOIFrSTJU0Vjrf7gHuFIFnE8CsYaQFdH26BxAG5Ranmd5jLsxibSLdw_Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPpjlunOUjqQtorLfYcYMWakGprFY4vJW51xgd-tsB7MrWtCivqPUzkp-8RcQGvh8h2W_TupD0azr3rVA_4h1ntrkKcWsQY_8FNRP33-n8IKSBMb-1PLckUDTmE83V9lEwhoJf4pS_UuVwvNFNkJLeVjUAJ-1bid0roUAQRia6fNPRlws9lNFFOareTzh5KOP51oF8tBBE5le3MyZquoGuE2KxUW0h_-HMhlTLHGFijd74Ci-eAO9DZAnj2pMd4AMoN70tBub3AdbcUmqRy0tSSvrjA7XA62u6vV3osInCWdMS68r8BGl2PlCw6jXGbnjryGRW-8n-79TTA9bOl3HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am0fr17wPLUDqynjGbeMs9IS6mmzKfof6P930EhuZhE0q411UTqQSOL7Fyd5LZdgrrA6YoXpUs9KIAJZw_XoAGDs3WPtDfNMyw-ziEDnkPL7E79KSh0M47gOkPl7iLPxWRLLlVP-MeXTIg5FsTgBArISANaaqxSivCB3b8l0sbtGXATbXXiCKfsTR0R219tp0-RjTx5bt65pEYfgj7DJZhJ-XyuvlryBYG78uzMmXfwmaEIKZfJXFjA2wSopjPQvkFt1djCrl_vx12vDoUl_FllqmiptKNwmYYLNYePCQdh4m6MyOJAvOTPgiys0c0OEOENoOkasi06mEAswV0TUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_kvWBD20LsoZoVGR0LtashPvb1PVU1ikpHhyIPXhjxCmZ4G8KtMRdTbLQHKNa9Ajf4dHaxtn7T1UEsaaHYEy9bnsTh1_Tnota2BZDPGUlu4rC8nCG9_T3OkFPd1TR08Z0vVlLTzr7ejzCswRxVR8xf0SOuOeDLMKfLcxoHd7pvYoKTTSn3wP0ApUzDHTaheqhQIFfcEU9G_daCohXcrXLOkhHmvczpmJRddb8uLWB1hgPY3RoPBhqC7ETGIE1EKPbOMU8e36Yi9p9PO1nmjvjUdL7pjdci8HMe0Q-LsKqGWTTEiP4XtWqWFwRp9Gb9RIYTucdySuZb4ucFuqTZ7bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=fwk4uskha1Ba9_yW18tEWHqgJZ1CcCmu94KKXiLTtfuZbAkvWMAmB2qMXGFqQU82KIme__MtNs94iXGVfLhsOBzT1IzbM4ws7hOGEhJ9ZNxqaj1BGRW0tWnOhpvmHBgggFD2bYbuJIg63YUxL4wTNDTISXzuh1UknSWHdxueCWj-OO1gipMPDN7pkeOu5TS11vLMNmWjRpmqLZzl-WROque7wAd-I4iuBZWOAOJ--OjDNimZHoaiQbdOHM3j7VOU24pCKYXvXjiD2O7_DQHQKpz5ZAHihjPdh9no7YAzdC-knOIZMf4hQII6BjQvF8WjPYKfXP0-DUCP_l97ML8jzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=fwk4uskha1Ba9_yW18tEWHqgJZ1CcCmu94KKXiLTtfuZbAkvWMAmB2qMXGFqQU82KIme__MtNs94iXGVfLhsOBzT1IzbM4ws7hOGEhJ9ZNxqaj1BGRW0tWnOhpvmHBgggFD2bYbuJIg63YUxL4wTNDTISXzuh1UknSWHdxueCWj-OO1gipMPDN7pkeOu5TS11vLMNmWjRpmqLZzl-WROque7wAd-I4iuBZWOAOJ--OjDNimZHoaiQbdOHM3j7VOU24pCKYXvXjiD2O7_DQHQKpz5ZAHihjPdh9no7YAzdC-knOIZMf4hQII6BjQvF8WjPYKfXP0-DUCP_l97ML8jzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdeSEOKKy6QdmvADCwSauBngXE6vHE6BHlMmpUq4CAZ9o58S1QdmOsNQ-P5Z-Y7DGdwwsS0MJEtRwxBnzQDq1PEiwIhUzD89ho2hr4-s-hseSQ5O3k2ZThkELbLp-QLgV0sHy_cIZ8KHxRP7me-6v6EmevCetVnTtlAcjvGKSpd5h4rK0fiV5Lenl_YfRC-AbUzumihNtgvF1W6nP-8rxPgke_9Wit25mBtYKxpNOIOGLqRdTwy83o703qgmUiJzw6GUSQHMKtMVzuAGYB85-cAdM-NJfOssM0aejvwaELwrRRUOSx3nKD8iLiBtwjVpDJvTh33UoUi7HkIOAwRSDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrpwchvR5N2c-N9mNJfTXgMtL2cL2GzVGWkkOFtNgGOUzBUasLV72MfXKdVZWY6OTFmu3-3mSgBhAgJQ6sPafi_hD-UCZZ_DxXVyG83YRoNdFZzwVB1t8TOKflgZx_sWM45LWw_ol1jq8hs7qLU4qe_1-2v1_MzTK8puyK-DjdwXGcFcCNCn_l4n3-23SEPwpy9cdzqnpfGAFll9Ub0e9hmu96fCcUbznGkKa-h9V38qhC2ap4_5wAAz7drQxW9LvQlNvcrnsF4utai9jTchV2wt-kkMS-ZqNCySTvm632cb0pkTGetXHtgODPknNUylxNxlSs4RvqFXQMl5Un6lZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOwOTAr1Tck9hGfLzfrnXLI4k46BpI8sIShbIaQF-87rPq1xQRPagEnAfcYfichzy76n-2eo5cRytBcc86zcgIgij9lkXLrqy05jqJhA9CVr5mUXFBmXLGVM6tfBJogZUcHXPCvXnnD7AnKJrQe4sFjj8nVZDHqm3HeHGA-3yXTkVJRl_yi0DJ0susCL8o5br6uvEq0Ft3tk_bRduZBLwh3IpCYOiFG63JICwwfeCW04lwO8EXmsKizq90_oZEMX03SJFn5QZ9X-EtDxoOETNvJsAX1ntCfWJ543sew6Q-Sd1QWpoRyZZtp9ishWEeafBe_Nl_YGZdEyvWtr7JaxTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMVzDoCvtqH55ZeyB4qyqV9Gc1Jrukq-Mu2XSskvOP097CnA2a6EcceYIZwXXBitCx1dgdDiAUcOGxucoOXKLeE5Kn94Mr1pvQi0qu4rbxyb5Tm-X861DRcAtVx737jbpEcYrd-6ip0nNDw8txvtGB0fR_3T_ARsHOV3kemtXHpTQ7p_ldV1cYDvkU3DmYR3J5UbnDHW5Qkv9wB2Bsa0A4jYFruit7P2fQo1ulQkLdy3sRmyc9tBeeA-sMDfahYlWDZ0uHtOlAZFH8yN6dZoPnb1gNMa4iqHA2o-A4DfpOv93BpoUX_tRp1WQMFUAuhTbO-TPIQWc4SFIT7PeWvj1A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=ZrDWTf8KzMH9LevHN2RSESbfkDv7AzlupDCPB3T0sHkAkbZ5JurImMd-deQxgGwbk4YlDq6-6I9BY8TDi4N498piygUEN97TMKl2EVR5qMY2EKgWo1jB1d9dYFUjlET719qu52L__AdeOeUejegGINZ9dmRh6WzpVXC4XLUtAcvp8SP0EDJna9nYSX9y3DC6IRn2xg4MhSZNwHIVsHt0FCfPaHG58fWQIK4jf9YD5x_piKhNivunPsKYnxFKBucKgS4_Y_fyF6Pxcq5SUy-jyoiXOG-NVqDkZQZ0T0Ekj5-Xh4mwi01Wpe9c4AY3j1GMH0RrBA5nJHT-nClnpIPtEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=ZrDWTf8KzMH9LevHN2RSESbfkDv7AzlupDCPB3T0sHkAkbZ5JurImMd-deQxgGwbk4YlDq6-6I9BY8TDi4N498piygUEN97TMKl2EVR5qMY2EKgWo1jB1d9dYFUjlET719qu52L__AdeOeUejegGINZ9dmRh6WzpVXC4XLUtAcvp8SP0EDJna9nYSX9y3DC6IRn2xg4MhSZNwHIVsHt0FCfPaHG58fWQIK4jf9YD5x_piKhNivunPsKYnxFKBucKgS4_Y_fyF6Pxcq5SUy-jyoiXOG-NVqDkZQZ0T0Ekj5-Xh4mwi01Wpe9c4AY3j1GMH0RrBA5nJHT-nClnpIPtEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKcaOoEYD1IgkVUJqSdpb9Fi7n9j_am4gWRxamvA0rWj-kV1F2NRHveTNXNO6lKQPrWDBNvaQnmE178bIIxJwzg5QCRwX7o5RnKXFfic_Db3NvyXz6NFb2BzZc1Stk8Kw1GveGVZXIi2mrojvH0DtbBwCrNeBp5iy1MqROp2F7mO2wzm6aedK7A3yf8mKCsQhFfaygdg1SyWfZTvLiS429m-5k6OY3Ruh1eyvgWS1KoJorvcwLirw_sm9N_Lq19L_warrz0ZLsdaHEZJpUDRj7vcqAQG5A2Ij6QWSTL7VhN9M5bEZVfozC9ML2nKoj_DXyKJldPeORDjCoZbG1buPA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=tAk5GMOEf4_7qL9O_HQewVFVOw30obVmYQ748cJeSKHxdI7B5b1TQIEpXRiCsp16q5ZE4Zbq_YwewB_2gG6sJSBE-lAxxIGCCfPTMtfPWf7J-n980_4Mw4CHlceuhiKY82DmowRCt-kXuicbUO-0fer6sqqIDYe1lIUGDJj-HWRVBmY4qBGkwvJ3QlqlE5ZBL5tMNbgC071jD5W2hGcozgq6GLGIFAdzth7h1Jwu1LqEoPmcpezkweYtsdDO9IPn5QqJK2fPFjOThmleEl9qD_B3gxd1sR02D6XFdqCr58dvQfqpM4zXvGO5xutnemSa0Jl8v9kl1wFwJxQLek-kJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=tAk5GMOEf4_7qL9O_HQewVFVOw30obVmYQ748cJeSKHxdI7B5b1TQIEpXRiCsp16q5ZE4Zbq_YwewB_2gG6sJSBE-lAxxIGCCfPTMtfPWf7J-n980_4Mw4CHlceuhiKY82DmowRCt-kXuicbUO-0fer6sqqIDYe1lIUGDJj-HWRVBmY4qBGkwvJ3QlqlE5ZBL5tMNbgC071jD5W2hGcozgq6GLGIFAdzth7h1Jwu1LqEoPmcpezkweYtsdDO9IPn5QqJK2fPFjOThmleEl9qD_B3gxd1sR02D6XFdqCr58dvQfqpM4zXvGO5xutnemSa0Jl8v9kl1wFwJxQLek-kJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clPZ3EGghxzHHHGp3ySTP1IsxIK1R4-sInQCmmNmAjE6WZmjHKmu1Tto1U3eb3tqke1NxH-QAA6h_RJXFh-u5wZdzTKv_wm7jnWHIB5bfgb9zrVs5WyPxLkyYowaGWmCjsqLsANuW5j9Sxir-ytmtTc4Z5Xz0LalfiEu6PjhYDKzluy02mHaaB6TGqcn-kxda_-BQmK2OApdYEeQ3hjJkj77sVZLYT_12fevYMbg3LAbSbxT03nFcOUSmoL9efLaFN80FghZTfThW0UjoTq4i6yXkDG34mt1UMFhXnhYdWjAzbbimSKt43WHGESpDACvgDVM1S3hzsADqRB9iRRmiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyIecgLY3Dxw3WR0mZy_WstQYD-7_v8DsY1lqtIBXHq7Fyq0X4pPIFtTg4yjHdePpayq-8a9ucGGAxRY3LPknTFWXCU-WbHjhtnDSTQj1N58L-wu9pmtI2r9-hKsDRm7xJqLBy1iWoWIjpuSWzHprwG6supqLwh3pd6MOhBAm370cqJ1FIarRNxellx7mAKfkVFyDmD3rPtpMHUnxm_PSEjnHFcr11GHN_kNB9h-8sL62DrvuqIzLuFLW2yrQ8r_rDPwkPuBxPpYs8fMjgpu1XI7V5GbmOP_It8PqQSlSCGuZivm4D2_oKjLIKJNxceI9CvG7f1SpJoQj5dbITZuFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=kJPyxzhPqBf0POAdPFHGhbPdJwq-XasXMKicIHnPjhiDe8tcscCYqUKoAa54XkcWtzVyKa6r5r7sR4nD2Ckg0xgx0cIflMnRfgInQhe1ubk3bStvrl1FKeJoma8AOflo8BVmwFe1PipkUKG-K_UH3UF8PLh4rGTgLTgDovZqqVLInEXN4lwpi0T1eTszIndajDHCpyC5-PAdXc6ROL5-PU_oDgtsvheU2zD5vuIOToSru7zm6F1R8MDsa5ju4DD2qff92eXACje02HUcJIa-gogxWukfUJMN16v5enBPs00A1J5H3Crr5WfbkBP-n2v6XDTXd7LBawFdDtsb2K6UsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=kJPyxzhPqBf0POAdPFHGhbPdJwq-XasXMKicIHnPjhiDe8tcscCYqUKoAa54XkcWtzVyKa6r5r7sR4nD2Ckg0xgx0cIflMnRfgInQhe1ubk3bStvrl1FKeJoma8AOflo8BVmwFe1PipkUKG-K_UH3UF8PLh4rGTgLTgDovZqqVLInEXN4lwpi0T1eTszIndajDHCpyC5-PAdXc6ROL5-PU_oDgtsvheU2zD5vuIOToSru7zm6F1R8MDsa5ju4DD2qff92eXACje02HUcJIa-gogxWukfUJMN16v5enBPs00A1J5H3Crr5WfbkBP-n2v6XDTXd7LBawFdDtsb2K6UsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcBobQ5vCs2eA9YMsXdzN5_AKxG0Th7FnQraQpKBY_tHo0Dm_-vExigSWino4BebZofxw_WuwwO6AX6DWeNwZpYlhnQ4QOsIo_mCAyvD-El5CZH3puKMBSSSQffxjDQCHlyyOrTrQiod39sWuUH1YoRED1xasbqs5Lij9v9mHQX8yytEkhwSbZbGqCVCXXFrJnLmKZ58cn-FIo44xL9W5wNPUUX1brzQ5EN58V2LYlQAAV4W6tGcg8pasU9shui4P9TQNjMP88xpJIrQY91cua0thcpP859Q4J34AA0iLIG4velQrbwnWwTBWT0B7INj-3aFqtozI8eWPJcuZ3hSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkXuaxXxtyG7PZPiwxccUDm-8SSd19n-XoY1L4q1RPXApdF-PMleVm_Gk0xKVcjhY22tRfoqz7D2Wpbiwmezp2Dk6Xyk0XCwRPuTkoTt4IBXxEf3eqGFh198czndF0ggxdwOoSkQl-2yxyniBzzhV1n4c8ooczOWB977mhET_8Y68Hur34q-HCUA4bZ71BJ502rAd7gm66JLuaeQw1SnTgAdM2plrzpX9xMSgztNSRGIcHMJrVwCHVK3tVcO1LumOlIcywgZ1jqxG-s8VlQobg6npVCJPr8wLtcI8B6fLT19IcLq6WtugG0VmB2tmaXPv0vu0Wii3RFr1_CiLnxOSg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=WM3nDfKiUWSMmU0c39kpjojlQVnIEd4gyjHtRcSFgaXCyQNfGw0oJSt967p5GBRg7PHwhgz8dsIfLDxNU5G8CV8oOHJq4eQ7aqJkDet2_Gt2jGYgvvs9_PuhUHZMgITozUZwT8a0-7SVyH_dBShTNyo3UqK6DKWsa9qWExxRVTIjso7QinUS0J8SboOBQesznjQCp0_KKG85rCzMm-jLttZZNPFaZQIRK8o99qkHMVbeNmpYtQfjoN4f40FqHjE9TDHNFpE3KoJaftB3wi8xdAym5p2GVzhVLtShfUK7qg_McW_25KQKWlc87KTfal84KC1dH4PlkLjK1L6fPAOJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=WM3nDfKiUWSMmU0c39kpjojlQVnIEd4gyjHtRcSFgaXCyQNfGw0oJSt967p5GBRg7PHwhgz8dsIfLDxNU5G8CV8oOHJq4eQ7aqJkDet2_Gt2jGYgvvs9_PuhUHZMgITozUZwT8a0-7SVyH_dBShTNyo3UqK6DKWsa9qWExxRVTIjso7QinUS0J8SboOBQesznjQCp0_KKG85rCzMm-jLttZZNPFaZQIRK8o99qkHMVbeNmpYtQfjoN4f40FqHjE9TDHNFpE3KoJaftB3wi8xdAym5p2GVzhVLtShfUK7qg_McW_25KQKWlc87KTfal84KC1dH4PlkLjK1L6fPAOJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMzoebx_FdaVo08d1G2lJRXLPRcm94yiRrGpLVIobmBsb9twwP6vNCCzRAnqWV2ChHCsrGAnyS4rnecRBWqEvfvbKpc6Rm_47D4gIhvSF-T-hGraqXZVwswUythLMSEK83fmbH9j49F-uDSxC_f22LgrEXMOcCHwPC88TnDwF54bv_JLC9qENwg5WRxBbjyHjR5WvxNyUwGCXXRad0Gv9PPJ-XEcvPjdVZTmN-W5KSRqpSF098egLjWewk5k65RHqt393PYk-roih9KCD7jIA8Sn29yVKUnlWXgiNKtqI5CSPV4Vyd9Bj_DCv4BSIBTOJV6bOA_atAk-a4I6QXOmRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLIEkdGG25rDV_56dA74vHVB_tQepnQSF3o7PJLW28Z21h6JwPBx6gA7ymrOFuhVC6kCFRZDbi-yOWRSSBaEe0WaqxhQDP1IDRcObLaNkJYmiF6djEP8LvGGE0JiwXY1FvyHq-AK2jgQ2jrFyjofQF7WAlIQ0ZA2fOaM6hG3_lbVJ7pFAdPfETy-w0Ta4QjT7eyVmpkXaIEXvACpMOXYlAGpGOZiIoXGpq85iQ_-MaA450-RAG4AojyB7uS5Rx4mM0ZRc20aoPFuTXREwY4toO3LJ8tS_E7_qXegAUsOrmMBiYoAatA6Jmp0HuFbovvteBHMZ2ACGsz-Rp0DLhoo_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1LfNJ-OmxWEN43PbQuxvgRAo5G0QwooqYCKbVhvDBUqsieMKUnD5IrW7Cjg-lbi5sfoQUjTu0SOIZ43BDBr_l-s9cOMdxVwB-BFDDXnnsgoiFzWIVDB9QaP9toGbUpdi2eNcrhjf6529Vay8yo4LlWB6QsRyWjjk_gOhR0qcG_fUutWhtZQ0749A3S11U-GCD1pwTE7ZvLl7opOnQOydxjG0Lj4xi5dHM0jZxDb63cN4ng6veu9Dibz4oJEzcqm_b0rw7kb1UcDWFvmPHFcx5UeIEEet4Ir_dpnXyjpHkU28EV-Caeny76Y6A_zLimdHMCFUmFsvFmZ9EEdqTSfzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQnTCK2HGJTrUeuBrsCsLZWcVK6mt5QqjBXpSWimWF2_rE4Ic0EElUluBhphnq3iecUMgIutOG6qrn90xMa6ecbJJhqtgNarK5NK8kY2SjVIjGGgYCiEmOShl19RLe_KZWqOO198HKC5GTzyk-cYEjBuXCoypeTvBWqDNMQ8E-Aq0BzoWm79a28ZfLLmqkoAypZSYripruvPOVtqe9_WgJ2-ueCA1_wogCd7T0EU6G9PXaVXoeItFgQA-8vA4cBjnDTUYjBKqdrqmh4PAKK81AKnQvbzMY76mAF2w9CecXz2lVGbPEuartl_tjI0pkmjmcO-Qly1VxBr6lpQOPm9lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1vSBQQPlEPG5aQuoSzLFoIPOxu5QgmtVCh6YFT400zSWyNUimeGblAYN4zJieoR12a0pJWkSUw_mTVmjbJEqTv3WFNyQ9h4DEH6wOjlD7_ph7rBO-g1LjYDBlCLcb8anGpI7vvLjA5sxb8cM-Q5AeoaZ-7oIdUUgz1Xz83OIGxYHWUx8WZfhDqr6leN9kgppnBzF0Y0MdZfjeEj3TaOTTd6cIlSuwQA5AzduWKWsbKxUEUWa1oE12lGACani_w2Kq8Nk0EXVhcrPgOUKKEhoIWpopn6JqMcRWxGsW0sC6evohtFIM0N2wAwQieLCrILYXKV0mg3sN33wE7NQjZ43w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxIj4AkxqROrK8zj9WSC1DZo7YwgD_X7H4PUbfiVGH_TRMZVNNGavQeV2L2fXCzsVGKyXixuyUG4btwz5vXpQlZFzLSPn2hdXptLSWCutOgOAZAsBj7FIjujecVPw-x80oh1L-VxMTR5CapNuPONscMQ-uwq-ufW9rwD_oQv-Go9MYqLRnnpiknl5eYUnu210Dd5ZZ2rujZkqMMGET5ZCH7I1NH8NTjKj7JBDYXSJm5lvPTWFIIOTs_q5NY6fbQ_dlJgR-3v8dOHY4z9sFfYW8o2AIOBl-CSD2pcaXKHCj8Wp-Zxt7ijNyGLQVlqC5g7ZsBHnJ55oe2IUjXpU__kdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiIwBAKeU01-FY_ArFzCfR9zAGKcIZZP74a0SdBRGVvYHtdt15H4TDQy5kuaD0KiQuPQuBNDLjfR-_PV6siBGU1hfBC2a6AJFpcfoKG3WnzRdDe5TkWF1Bdk3UF9sn0Te4WeCO-1sFFyoant1XykrSb5YFkunJYLHKkepzTFTgpvWV-2OeFpJqC0tOKM2q9q2P3o75UJO1GTJrjk2pNcs0nSsERWv6n4RC_D50vkO8but7lKJ8zMHMAOFchpMVzZRT57OhV-6GKPtkEcDZI8eBaPMc8ZUgOC8esiETGaGXlgbEmnM6pAq5KYeqxGlxYI_ZAqwBeJeW2q-ZaW2A6UiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8pXl75-Hi1Jw6pwA1tuMyd5d3oMIgvADL1haQgMX9py8NHgKJzFSzjk654KaiXRTkpmLvdGVKSZebuFh1IwO19_JH22ltTJWQQhhAYj6fy8jyVip3UvDZcJ456xSdVVsMpBGT8PEZz6WFIqf16M-HiYeTVfcp7kB4ynNLwI857z_dbnlDUvCMJB8LVM5pv2ymYWpOy8Ed-mrc9D8yPOCSvZHtt39yjdCavEvUtUNm5kl2LExeTpG7h3kyGhaALKScVfUNiNih9JiJJ3RBWtLCrMpXLHuSQOEqW6t5oJMP1PpfLvkaqsyvPnXDT5r5enaqhgIYx0HB_eQi92R_2UPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0tK2nqSZs9vdnS1aphd0KK2Jprtl-ffYsBYVto7VGV7eovAs1uTIRU4hn00XV-FaYlElBF1kHPIepv9Be4QYVvFKiLi2KO24w6372-DJ2dU4nVAr5EjVH5rR2OcRQhIoV-W-LQVHYtgFW4WRMCnzQ5Ivij09V-mkZYDx9vBLU3Uv9dJktQIVCFtPvVUPPNXVbPDQ227p1hbW7zW5MEWumhZaUfsfS7isFoyDkhgu8p2l3NOOA7LQwn2DkgLVD4Ses8DSVX2O80_9DiTUL5V-XuobwgSyNpEb7EdILxAGsjHe2m1PG-MAPtltqlHtosdhLvdDkVkoJz-5BXCqkydrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkTAHRuqJgacrXXekR3YwB9LJEOugiyEQikyKiYbLqsBnSgezf_GXRUaAoJlcJeDeyL3rg8FWp4YHMu1104mqGUmQdy_7_Qc5kLFNj_BTBFqKKKGfn30nG2uRgehUmL93jqkJ_ebdCZSSmYGvbrJfhd3ZNst3jho1m3mdK6pf9We-b9TBi9ttW1ekgvpkh8GBaU0qBRyzMaVNKtKSPKd87mB0uMXjoBZyQtZqXI4u_AC6JR0cEHASmv6ejJVmT8CcaMQLRL7eIKLz8hI6qjY2OT6UswNcYDitLxOBGzBURP6VKE0cny9-j7wjjA0Ow2mBB9oOXnzeflGVkKnrf8GkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX5-F7m_r3cuPqupZxvFXFxhdR95XNTMsXJ-xYBUHzU-42bSwdVjfi5ctgtjc9_2opT_CriX9MTzrHGParkRumFJlyP0tVogtZknKSDOJD4_WDp38HConO1-GEe2zT-94hqhhHZHEmXqmPHwU1bFYv1DT-2wVy3rWOboJzQ-DJZl_6v3xJnHt7n5CflRLuAMa4GkHq7LUPp0dBbdn_8MQUowcMMcecM6Rr3UHSjB2CNvufEWjqwxDFMXc6QOgY66dqNYhyn50Femtl-P0ySCx8vaaw7mnlDmig5BgxeCXlbkKtPQFWA3xNLSl4VAp_jEW2bQsTQ-Zk9kYFmNh8kUDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVCABeGYoal5WT5ZX2EQeYoy_UHrTrnq0J-kQyC79ei4k4-ErnyX8hYL_dyyqOtRo8YcoRrHul06N8mCGGpAoGbJocSsQHNDepnQ0lw7DZ7S3_GNUTf7EtYTBWO5tIPSbw7nBA6hT8cBOjaBgAOckgLhS691ZiaEAjSHFmZGFX-jN_ta-dojCn85T4Jn-HyakwnnuyJebzh1p7_ecr3O76cEEHA_FhFYb2PrKBWJinzxITsa9TeJFrXMLpkLgCbwWDWy_Sthm8SC59x7qhRtWyjTuq6G7jH903ySo8PtI8MflA1yn_TIn1mXZXgkO46Idwx4adjfDPB7o7-3V_iH1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
