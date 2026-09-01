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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGoDBi_Gq6eTSHeW7bHVDiSvHwgA1wcqPK7yJ-Rur8Yc0lV4VX6ZlsQJEBd49rpyrYXuKqFGg8g-1CfvVZHKhkd6f3IkAW-iVqmY2BGqaAkgOke_ltPXK7aqttEhXfNiAU8MdpMrROJgbWnot1BnX5JS2FZ75vDbJZP8tPQC-NWTnsGyGFSPRPHoSsmewcG5waU1Vii7spBajK0zBhB3YrW-4s7HvUO2oNd5msBjbvZKoese2afmdsASQmyq7FejvzIkF4BIPODN5ksH4l7w96d5F_vn-cFho1okbqfhpZ8iqe9Eu2y-aVmX86sTBmsHGZkMzSz_Xb2-NSNrMuNiYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRYE_tGQGe8FU4Kd_mLAam2ZBaCiqfN8u6aV5xPIL8SyQuvlAn0jHJtDAJutPYcy37CPD0CLe_Ln89H4nQCsUN1NXwC0KJAaRvM4e8HcigXIz6a23zU9biMi7o8a5fIlQRHJHBlzfc-zJXQKKRcqaqUIPtZz5Mjj8k5n6DmVKBuNtaGTV0JgwzZXSxHyW5DRFMxVkQR3i4OdTqwRTuc9YUUmYhKvnFJK5Nvgb_kJp8mqWwaVsqHKNS5c-SsaNFu8BVlfpufQWQsKlMtPi0pCSzyAkgegWQXFDcIK2htaFmN-HWRepSB0WEr0L514ia9eYf3tngPojcJJnRIj6FbR7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjpDNNSVtM8nSr_VIiomFfVWTCSo4lM0gkKyudseUj1bGOhuuHzNZj6n2TqpHXqWl9uL9DzQPCF9csKKkD40hpk5NwLIUAeu8HHf-_BwvKMDGMmEcXWe2MEnjpLa30DXyOIiGit2iMV6LcrRU7WirgRdWpTXvtgaAiLR6E-8speeh0EsI8qxFeaHJ81xQWra93D03zUp1qK0buRKrtLjZppMLfEv-9L2yDwa-_FZ_K2zrR7lNMQcG7CinHEOqNOXw6kF4GSMCGo0-4iXp7HtXs640U7xhJdiatid-L0PE3NjYVkfm6pjDNzGORVKLibN_Pvur6WTQVNx8iVsw9DBfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG-LLpeLwlVq-mmmZxRFJi9jKDlHBaNQ_v5ojhZtNytNsnf8phVBzy5JKdqSelf4oWdw8WOKosZqJzE4TdomvfqraGQ4_3d2f8QciF2VUkfnjUISrhAkr-ZFRtMsk00lu2z5XDxnuoBjxiJVQAAzqelMWhAykVuMT3vwQLwGla-Z6JJqd4ul7pw6l-R9D5AuchOAY9xccaT_s_WA3gtF9xwGJzIr-dGN6q1WCVGYnu-ldlyJRbvQpfNk5_YxdPkvcS97hv10P4zXaNNYIvuf7xGfcYF8ot7_LejF3NdWIAJ58m0Zmzp1hAR5gs4nI3O2sN4V2t9ewRI3CbHTMmO1Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=SB77k6G_GMISM74Do6Ng8OEXEbb_8pdUrHSwbGdupltQ8Qm3_m1uV2Tsou__HcfAnTvqYpeiGxEv03FzQg8kU0InG-e0v1a85lomjP6SYGZQffZxxco1zk39pIOGjyIKkuu2giBfHlxnOPKQynKReEUPYGG63xt-lyt1aygRUjAcjZj-TI-mWFU8q_4VxZQlKsaFXp9UCNz5VRDajJvN9GMZIXWxFQ_lpy0r6hWbPxvELJTv0y3T6tnUAdTiq0L9UFu59FFvaV-nNjqnl2_EGIuOVvHEvGbzffRDIOzaauhYpuKd93YH_Bev3R1k81fFakJ-2hlk-hN2DR6kXgVkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=SB77k6G_GMISM74Do6Ng8OEXEbb_8pdUrHSwbGdupltQ8Qm3_m1uV2Tsou__HcfAnTvqYpeiGxEv03FzQg8kU0InG-e0v1a85lomjP6SYGZQffZxxco1zk39pIOGjyIKkuu2giBfHlxnOPKQynKReEUPYGG63xt-lyt1aygRUjAcjZj-TI-mWFU8q_4VxZQlKsaFXp9UCNz5VRDajJvN9GMZIXWxFQ_lpy0r6hWbPxvELJTv0y3T6tnUAdTiq0L9UFu59FFvaV-nNjqnl2_EGIuOVvHEvGbzffRDIOzaauhYpuKd93YH_Bev3R1k81fFakJ-2hlk-hN2DR6kXgVkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjjIjzHPjQJT00hPfcM_YMxGbzzqaWIQbQaWsvKoC52tNYSv6QEbADy_I2caFL2RWgxUVHJeqlfdG9F1ln7MjKJYdFL8SIFaTvATb8bsYEt-MX6q4msyTnEhetNTNc3aH-aspyfR6ZNw1IQYVY_tVwAZEqXGjVgpYcRJbWnGdR0UzOzxGAxqNCfiCnNyblfqe3cVMTOk9tolmcGzY6umVr5SC4sKgBNcozFCS2Sx7Yv_MKWca8mTMEbrJhsgKyeB36QiDq0C6Klv90cbvMLszM0VskYQ9_tT1yd4vdIK3rR2yxAZ82O7GklmPJcE90wUt4MQfEAqvYD7oukNDtQL3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=r1LM9R81CHAaXiggKjAdUAFm2CrLk_Z9lkARwzR9_j5M8UGasnlIaxdpspIO9G31YSm4_9As9HTJIIf_5Y5IbReiCN9QLt4OBuTvyJFX4BfmzSvMYV60WLQ20cr9l78d10PSrWaUV4O3i3LJAAtY2ETRgmfwr99TlhhdliivQm5qLaoNFzjcBnzTkAe5RDCjJpGWtGi_6D0ADsARFbgINtOIWOJbOxZd97YafF1PLwuicYdzkp6FcJdu5WgxHCN3V5fe-MzSal1GdrrMGbYzrzijfXCL91j5684_U2KlqxWZr3Bf7jPeNHsbWeDL8Ty1BfU9TNZHWJkFWVXCEcc6wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=r1LM9R81CHAaXiggKjAdUAFm2CrLk_Z9lkARwzR9_j5M8UGasnlIaxdpspIO9G31YSm4_9As9HTJIIf_5Y5IbReiCN9QLt4OBuTvyJFX4BfmzSvMYV60WLQ20cr9l78d10PSrWaUV4O3i3LJAAtY2ETRgmfwr99TlhhdliivQm5qLaoNFzjcBnzTkAe5RDCjJpGWtGi_6D0ADsARFbgINtOIWOJbOxZd97YafF1PLwuicYdzkp6FcJdu5WgxHCN3V5fe-MzSal1GdrrMGbYzrzijfXCL91j5684_U2KlqxWZr3Bf7jPeNHsbWeDL8Ty1BfU9TNZHWJkFWVXCEcc6wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2XV5HkZowEXv4Ycn_lnVoe3RiSQfz-S5VMu80Kypaxvdh8z91-9DwescGRp-tpXT8eZCZ55KfKApnkJf2mBVo4eVCLNJ4FofRNxA9tF1O_ddAllCguFRvwgM9a1LGoQRdJN_uGJQPW7UshAuEYKfyN7fayV5cJHMpoJ1QablNRrrmzdUPwjjSc5zAYY59lckC4kVKNdCpLz72f7hHUz3vpgbGAV4lcQAokrOWaB8lrDsUmfd8Plxef0e1WmEPH52oTbLi1CyWezBXHSZ1LCNphHNbK39bw_Ru1LpqCtcpC28XCI8ACQ-KbDDnjE-KqMXVCDALj4lOl2sw5uoBqWPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5mRyGS-jEReTHvMZW4qKxRVRQxrWg67GlnROtmQixr7cJk1SKGgsx8zu2S_5YgFi3c_ZfhtGEOzzUPKkiuknTW-FmLJV4w7g0fmlH53VeetRrEESao2ni6NoOG_DjCqj27FEOffAP7HPTTuWC1T-0MNd6SJ_U-LROcoDA6gTjubp2kyEMOSjl3vIKDPzz14m5v-ZDs0pxD5UOFMnGSR_cGcl4kf3RCTzutho1_LxIlQGziV7vDnmBz2eXst3HJF8IdiCRAclhFw5Yf2_bWfY0uTRfylXLIDqjbJu7XPq7dqYwZHXLrMGvUm3GaBjKOvrYktEil6MZCGxffmUWKlXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1jixe8UdcetvoNJhcURGAgqHuCQ9o6PSYKKDKECoFf6EttKI1c4XVHwZc6UB3pDHyWXceyopjniG1L87TDwnloEO-ZFFa7ZflsjVo08gaOzt3f8QdWAWa453wQWrfD-JEqt--VyoCmTzL3XOwx0OQ5cijMDjZxaaJ6BWSzWAoTIcJglX0MuYTng_231PJFqzbeN29E1QwnF4odKcZgj4NXYZXD_4SQlfBT2evM7DO0VrTY29hlsM16LH9-MlGnr7b4CEvkCOdVb5pQfYxWzLbuSIiC-lsi75ka2JBy8Nt7ctyU0OOwyHaci_6Y1IW_jj1Eimkijtu5lhLno4PTxlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXvWjtWcQnVh-82Vm-8UmsfKSDFNwloOR_uK3AmfhrdR9LuDNBK19Stf42GwZsSdUG0CHI6al4TQope5aGgEOf6Kyr_uVB3_3zgVYPcAXLPBNckaOvvnRp_8Q_wVkrMteOv3LnDujD7VM7_92DkUA-VZWeJnbW5g-ire1mxHwhL2WkarWBB1gpF9m8UMsPwmpbyp-HrMk688jwn2pbLHczGV0PG1T3wH8a-oIjbBAOPwh0O7XNzlz49CAkVrKQeduT03IzFAHM-uSu0K3Vau4_jl9dkPIm-IsvANLbh692wJx_AlXZIgn7bl_6UHZXivkbbtTUg0IlA_mfnQvrcyfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty77n-q0vacAeDVcYVlDhrHvDGs6Ly8O1MmqT3E4k0BjSGFVTTiTUJ8lhY6lDHs7tnCFYQ1-6jQ0hGxq4WWJdVyxW3pU7DCQSlTtQd9Lv3GEmFQjZpTpCSf7WIvvIfhGEpqhMoQjHVABcmvU63Um023OSEf-5oHdXMcI7_ms3wY6I4DGoB8oU28HIhqFzdK34JIXGsGtAPGJjhmcghfz8i_S4y-pE0uWDqAaNVQQgnsT0LH0BVW1GfeApE_0tFPoHSW3W6rvSL7QPvnAtwKZDMG-tYvR3ebXjkxHYNJuMOjaLrAQF7bM5qBKEzb4bfIQSzDBvZ3RdYVRtzuhL6NvoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDfDlAOKu6O6vZ9Ksa1e0T7R-X8bCBPDreCE4rtt6MOyfnb8Wdkn1yxk4qF4Z8hbatMm8LEfwZoC9nKrVWtHzBGFzatPX0B2ydsNHzUEimI_IKGbNP1RBAfp9PgVF0GlUbVocs8r0DU59ZyiUC3uVL-uM2m3EMTqvneASfhITJ0uNRvktExwIhXCen-SuG9lLvbODyP-YnVI0SBMhFogYGn8nu4yV86GfdJ_TL1DvSPTj4aP86jffXEJQ9Rg7PHXYOIco4_Mpd2GusWTXPEa5F750BAMg3YpHctYjMupjJAlhByFLpZGMLm32GLPS-KWc-mIE90iQToVG_bWqR1gjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=sV6el0buDwR-s2RImAvggXsuuVkSlr5awIEmF7hi1v0S6WwEw-3J2UXW4nDPwu8i92CTfdx_eh_tL2Y-jry0SoKWEdEX0hP7deZrSsDzKKI3eFIvm9gp3LewBpWv17gTV-q6BdCLjSi7itA30xqlmEaP0jk7kZ8qQFFU-Vd-2ShAHp46sUtqRwtELZoDkXJAuS8WRLxmYA0xX_nOdAUmS9x4LIpjC0nlf9Xycu4f5k2c0ZkaPnbB2QiVIyKM3aSdelSMlBn-AFEb98KuCoNKjWFqHdEisr83bdNDX9KLmigutvUv369C-iWcJ14ONoN3WROmKrC19IOURGMeqP1wCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=sV6el0buDwR-s2RImAvggXsuuVkSlr5awIEmF7hi1v0S6WwEw-3J2UXW4nDPwu8i92CTfdx_eh_tL2Y-jry0SoKWEdEX0hP7deZrSsDzKKI3eFIvm9gp3LewBpWv17gTV-q6BdCLjSi7itA30xqlmEaP0jk7kZ8qQFFU-Vd-2ShAHp46sUtqRwtELZoDkXJAuS8WRLxmYA0xX_nOdAUmS9x4LIpjC0nlf9Xycu4f5k2c0ZkaPnbB2QiVIyKM3aSdelSMlBn-AFEb98KuCoNKjWFqHdEisr83bdNDX9KLmigutvUv369C-iWcJ14ONoN3WROmKrC19IOURGMeqP1wCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v93wU4S4jbfs5iUUeKWUv-PJwqtMdnWVXgh29Qmw_2f06GQz044R5WGh5iJy3K0wfrCK6iq0g6RIcLiEYijuFn-KnRmM_B1zexcfzONWRnf5JhNh5Tw_3RgTXQ8hilbgJN1I-anMPpr2JUW6VhMW0RHt-YkCml6n_9MN4guyA5CA_VEMI4DEh9txIHbSaBPXAz7e449h1hiEtAaJWd11wPaV9sSvV5ZTSwV31To78G0wvR4f2jKy33PP5iCq62_5GJmOI57Yk9oPEv_tra2RV76C-HBWPu1ZApl0IEiRIK3KCw4SWqBA9EljqSGdDZMPQ-gao7jC5DeyzLcbo4rzow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=YxFVoFD3Hmz7QLxz-iYLgOcOk6xvwQyt0gvW0NiE05QOju8WSVj6ExMNj2Y0EEM3BPb_q1GWIUUx83jwZwygFJYIs9f1_ZahbFzmq3iJuFg8yq-_yErjRW_AUjCWdZIVMky8g1YPr9pkYvKR1beWNN03QZzUcwe5JvOXuOW04_JE1mB7XuItR0o4DTB-EpBZBAB4DJb59DB09dvh82BpWeDpuSBqf2MAyULpi52g2VbGLqU9goVXAhiAN6jpqmO5ZdNztYWI9C4eOkR9kVhPM_VXMxu6eRgJlIVjzvutRi98Pd9T0dAKUIUBYFGu-J8sdNe9ANd8xH7G5mPmxw-8Y7IV7dhI47a-LXW2scaGUiRivbB6Gq6K9hw2b1LmR1UVwEKEGLC6fj3ZFIdhjjxTbsEvIyIWWNYBFljwJ9EeWUX935WhxiJmGoobocO_I4MDIY1FJat5eO98xUL94H24bHQpAq360eFMse2rclMSXBMLYdoJSwgSaCgmTpLvDrb1UH901q16eeAZoh-1WuEFoBN6xGaZbflPipewLZ7jZVS18SY0zaNfT8k-OMjEol6EOr_XfiQj9gYV6JAoI9UDw6BHsTt8sZqKvI4b5xZtLGjjkQDbdXuBdSUD1tet5a3XFBaMgtVvwwHWKO_uMfYzQG1_uGBxjIwEjpMshh4TAYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=YxFVoFD3Hmz7QLxz-iYLgOcOk6xvwQyt0gvW0NiE05QOju8WSVj6ExMNj2Y0EEM3BPb_q1GWIUUx83jwZwygFJYIs9f1_ZahbFzmq3iJuFg8yq-_yErjRW_AUjCWdZIVMky8g1YPr9pkYvKR1beWNN03QZzUcwe5JvOXuOW04_JE1mB7XuItR0o4DTB-EpBZBAB4DJb59DB09dvh82BpWeDpuSBqf2MAyULpi52g2VbGLqU9goVXAhiAN6jpqmO5ZdNztYWI9C4eOkR9kVhPM_VXMxu6eRgJlIVjzvutRi98Pd9T0dAKUIUBYFGu-J8sdNe9ANd8xH7G5mPmxw-8Y7IV7dhI47a-LXW2scaGUiRivbB6Gq6K9hw2b1LmR1UVwEKEGLC6fj3ZFIdhjjxTbsEvIyIWWNYBFljwJ9EeWUX935WhxiJmGoobocO_I4MDIY1FJat5eO98xUL94H24bHQpAq360eFMse2rclMSXBMLYdoJSwgSaCgmTpLvDrb1UH901q16eeAZoh-1WuEFoBN6xGaZbflPipewLZ7jZVS18SY0zaNfT8k-OMjEol6EOr_XfiQj9gYV6JAoI9UDw6BHsTt8sZqKvI4b5xZtLGjjkQDbdXuBdSUD1tet5a3XFBaMgtVvwwHWKO_uMfYzQG1_uGBxjIwEjpMshh4TAYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0HpPMFDix2sDP_tBD8OO-RTwxEyDG0502k4__6lBvegw09hUuQluA21n71bBSxf_hKP_ek1-H0fL-K1y-nBsfTS3nrhEoJAPQAPZdBXQe4KJKxBXcKsWSbBF0L1IyLlWfrPTtW4MZBED1sV7eageLoQOnScNg122s74KaNX4nQHDwX-nc9vX3mWNbzqgYmXGBtqajMh49GF_7HUpupwm2qTJ50oT_vM07dKJ5YEauwhk-Wr65SPF3Q_qYG2zJyGkGnRLnyfXkVPB-GkppvMVNOP2yxnhKq4Mw3h7XafPsVYSAJUeTBBQd_OVeKrUATTcv7ADiP0RPAIPiYerJT8hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvXBZ3fRLVRz05tOEZjRuiqdr7z5ZKb-CqOZmYqbeQxqZMxNSTAcCqQyuI6kd78tMC_7wn2GaNx7_DTqEfDyFy0KPuxwflVmJcQWAAFLwJbQC6nEVIlEZlDkhvH5Ih-PP5ITeIqrIheq1RdSXSJnbE9wKGGeQmclHSfCFJOoluunAocaR0ZuHdTryCuX14RrcjSnkl31Y6oOyUCjs_IM5lsJ7RfUSILo6pZR1HOdwyV055cWY463-U5q4Na7mGY4XoVfBVqsPtn9OcxCN-hvy5orj4F9WYFAY9Vq-ScEeIX9Yc2mcMS0nesRnGSaJVuzPNlPj8Hk3uq3BnB-Fm4hyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQiEx6qTd7_DuJIc8O49yC44ZYuKznoyFewjCHrNx8b0hzBdKWW4VTNyXAWxd5rfeip5ed0Hssq3aZ0e7uvpeh-R5XxWxLkD2XQbCL8n3M_9d89POJtEomHHAfYkzlloN8o4tsKTqbt_Gvzxs31fB5oac-CNsqv_O5QefM58utYgwKMmiFw2lHONdy4VY8yxSYuQW7n_rJGgeTczn6FdKDKXZKonpXzVXZoZszUv7TMp96FmG04JdBCRx6GeMxEovTbqx8NN-Mkt1WelP2UdumlTbrjtfCzE6IHFCDMv-POtWz--xrk6H-m9nkLObUQJj5S1H1NoNp0VbVn0nH1aSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYCYiiX4QYsKfrPI_49Nz8Mg42bQqM9G5RxzgjHHDIxR2lc2x9D37Lp0Bw_f2wmkY-viip-0pWmK2SDpIVjagK0FVExOVXJD6bE6CFJP51eyIaheTTD05KbU9AJN6Pn3rrUtYuHp2kCH3iB6D1Vt8mZMSwsot_FVtoSV71-mnYD4Zzj0_3EswzFUUf0k803e5Ob_YAZQikron7tTIGWQcr_-5I1U_SV4R9h-pDy3cTMZMsnWMrUqFYnqQxdzliA5YQSGzRvSf-ekNNmM8Cp42PSOEzUHUGfbhrxJFz7tq0CdpuspQz9x64QISEe-TZTWUo0AkJbTPdjcPg4pA82B8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzektEzp1uL-Scz31D9OH9wLAwGWwBcnrD-kR8RA2Gj7GTS_gs3PY9LaUwBC2xKywGglY8YZZEHcFNzcN42p4sBsHNMxhwHUBfP9-oJ6kDAtaZKkYtbe2TTKN4Rq3vwyx6a_5daYkxQo22hZCmRv5zaCXcnPmdh2pZTjym00_LPeUaBZHsQdOc74ID0F6rE3txyYazKVJccQezx1MA99kLDu_Rz7CVPSL7mIdfljX6tvrA_-sBmNh1mKpbBKUfT0zWmS-sFd1aM_-C0dfd5bvDEert3vbpUBEWbZEJAwxeqrac1SsZ2eZyPwGucxe2of-kzO5MYlyjeOqX2w7r8zRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMnu7p-Klfe1ifS88FtAbLC1SJKaYRi23hNRoiTEi-1qg4ma1rhT8O6Wpzi8371QUc_dKIFbrQ0mg2xwGceyV-YlpsCN0HjbgSS38oRHNe29WAuGp6nIkIIGRBmpIs_8nH2vf81l5uyqBW01Yq_OQ8KX1mV45iwBssDrYO12zY0SetnC0Ci5jGCoYaI9Ud-CVYgiI8cqvDQQmQ7OIuEUgoJNjRHtU0-otyxroz9_dSOKb375Ae4Bn93x7pUdrBoIfObBTVaiXJuhMSQZDv-xlyIRBC4NkM_G0WiyrANHdPkriQWYoNqjVmeGtYtrZBJiJavJH8MQ3qaH8S9T9_lxRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=DteEdMDnBMDZ4X-6qtO9yUGF1tkREYHN0m0M-SaCLZTGZDN5ApMnV7p6q4FeRdVuuPdYzoQplO0vfSGPfKQR0RNXfz-MmJkmDzJrbWG5gNfpyjc-EqmpaYbDcohgq6mC78ab44pSMhfOmm-9pLcM2qWdwnEJL7pzb381qdt8VeH5nYxYMvVmhRcHCoi9TdBiZWqaB9AiI7AhpbD8gRbzR5OjSXztSCpMyQHzMU_TMr6ZN1Pu_CbDHQ91kKp5_RWxXWj4mW0kvbfVd5kX7m1LhX53w6BnywTK8csikjJPYooeCE9gtvu-mXATxVrTeRxKdffZkT06DtBKOBzqEu4HWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=DteEdMDnBMDZ4X-6qtO9yUGF1tkREYHN0m0M-SaCLZTGZDN5ApMnV7p6q4FeRdVuuPdYzoQplO0vfSGPfKQR0RNXfz-MmJkmDzJrbWG5gNfpyjc-EqmpaYbDcohgq6mC78ab44pSMhfOmm-9pLcM2qWdwnEJL7pzb381qdt8VeH5nYxYMvVmhRcHCoi9TdBiZWqaB9AiI7AhpbD8gRbzR5OjSXztSCpMyQHzMU_TMr6ZN1Pu_CbDHQ91kKp5_RWxXWj4mW0kvbfVd5kX7m1LhX53w6BnywTK8csikjJPYooeCE9gtvu-mXATxVrTeRxKdffZkT06DtBKOBzqEu4HWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NovrRmebNT6FeRRllDZxC0MtA54UJt5qEQ03sCPyw9dcK6xkojtZ66VMQR-hgJMmD5XQU2jtAvQdnv_DVPMvunGzRIDp-vv7Bj-2yIIrwbXvd1EjhM-uiIlW6ijLnz2z4wd-0kCMtXykaHmLG80Rh2RD5SL6deQjKIqO3WDxuQh22kTq_WWpCKUBlyZ7FaP6iToPDl0j-n2abQHJLJ1gyCpNWb2_c3h2tDVyjuoYsufqSBCyGVbMv5egdmTcwMKEDv41eTFtBArof1JV3cHSNk-w84rk-eIH-NtBsQJkLdflIzMOfcGbvREIYTR48SvLQXpEcvtv82qsAdtjs_nPDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyaQjyyZHVnySnN8z-mz7N4T75hyFamV4ytCiYHIahJ4cKIvfAJKTMjwOLBVa6q0OJaCkuev8nNojOIqejNXSz7TsOowHwyIY_SUc1_70dqNcPkl0GzqYW2Bxm1jn5TB6COM0TFAqS-gAiljtsbSNTELqjY9wKmfisWYPz9LJWX_ecliaeZ1oClQohOS-UM4RmjZateXuerpmg4E9HyAU3bgOYpNrExFVX9Z2rt4LCekQCD6wdwUJwE_mv0oZZhFaE92ox-yX1XOHmnhDf7ksadUe7CwqbiiOQ2_vaNBCAmwvsgJiC2WRXDVHkfEIeZcpNaIPzSoD7aQA-8jZGJAaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7IiPujsC3-W01vFsDWKDiJVg4l7G8wSjHuVRAGtCEnnEcQBzI7ruHxSb85aB7TE43FYpGn64rznCPUId46VFlPOuzSOCFfUkGT34_-jrMsJaaROHxxu6KfQCocrl1kTzi2W3KJAbo22C95CIaJKdLSLCXB8CpNt9LqxB4kPdbzG9ySZGbSgrpVQ3IEGxKRLej8SJW2WugAMOQuSOMtY1CyFOEpslmeJ01di9227isZ6pg6hn2DwZYOklyB0R9P6nPjiYqKLzZfTKvCNRDqXgV9NQRNeFkwBEMhT7qHFBWaAUeU7tkazK5DpFOK7wb2NI5Wjhec3FOABcc6g9m7hrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYPJLl5WqnVZV80mJdGpgUSnXR28hKRqFGuGrw12Ks2tV-SRamG10LTOMCrCurbxL2hVn8bLbfy3QCwcFO48x_hf9N0G6XtLzQT9polBT-iZfKVNOg64kjwioBiMlhO6DsUr0HvJr4dlHadF5QRDsP96k-tm99iTrHV9K_04kbuO79GHd1ktMt2HjFSi9gveCHYYRyJKlhNebqi4PaI7RSMTd8hNG79mdyPKmncNpSqUUN1xBW1TGGV01vr_2LDuOKNmLz1dfkgvnm_TSdslW1jGpyw9VXEwtF99o8_LfiYLYu4E45W9s0mvyZ6okjBZUnWaY0uhGd4O1YbmDbrv2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhRQOxG7TtSEFoVbBEIIuY-k186HLkm8dCw3BSTOIFBwgaysNMXZM5_4UWMOU3n2oUFtMYF4Hbi-coxtocgvZluqYNmsQhTzAkDvP6jGQZrgnQL_S0D_fC2gQr-R8w2gnlUznWlORWAqnhloVpi-Xqje5N0Bs-8jzn3Ei3kq9KicUJcmHvkkLXYg9E_XqNLovbX4Bx8cPNm01hiFcfKc9iYrz1dMtOs-KYw1SKXj0SHxvAcq4ClaLTKEeYdr7t_sPZM3-MM0xF0uAJCwq4HL1wSw7lO1NipeBHt7pgzWOwAaOXt1hIGAmTjDLxH8qdHrfeSON5aDiSuxotMcbklMJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM3YzBYRJCYdiJJfIVDvyN5QzqGVVYhz1VzKYEje7dd2A-RV_XPZzBoyIPST9l5Df6i6CcO1wsNfrejMXCrklPLWhj2etyyNgFIYUFrH8mGavPRFwq9a-0rbOJj_dq-a3rCdkwXV2QjEbuw0W2BqVxNlUhDQX1-5nkccG5VGxOGJGD1FXxJfC3EBwpl0GiXjbaylTtb0Yznip6q1SoHzfsfZFCXAOHi38sdudCqlmmaDhe9yD9LAhpZUY-RjBpxn5H0FPkU9WAJ7z35GVYgzEixx22b6h8SPGNy-qpe7W5Xkf9O0jp0X-DHpxPjjPSkf8-MoTsJsccl4iGlOFBSpAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3bPUn0wuIG0gMDqJD2txOH60_caZ5f_ecl5_MbZtXYUyUSBkzddYuQ4RZBjzqg2CE9sSGTcLojqoWOZnMKr4g8_6e5iZAyxeA7SKR0JJ33Aq4KnI19x9vpNIFOR8_a3Q1h8hDIybYVlVHq6pHWvdStX1CGcCAcf5B7oddE8PM-7EKfxy0v-LwuD1aufWmWLayLF7o1XY3y3zEz2ugztcetJbB03kH8zsl1aA_CTaPGZI7MrYz86U2nO8QtPFYOzw2TbmOmXAVZh8RhHfJlxDrXkPVqYYH2AVVzEdU6uu2mhnnMCQVJvsnzQjsUvABM07urHWeFEFWOb56yqpRMYgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOo-H43nXjPlmFCVWDCA-WJ0WclYZyWA1NdTMyY8_KTRGkY1TpXcPTYU4DhNgngeRdiGKm2OERD4ASmZB7w28Eyykd7VUEYCHb0C4fW3wppcdBvfk5C6xcXWQW5mc5sEuk4LvEXQui7rEqIw4XsPef7fa-sjRM7KMWyfxdGjQ26BlkzRGIkgPOvZumEDrrcnjE7yqYIuz5mVqeg6ykJHk4GIquzCuSbwYcbeocSFufL8qP0MnfBjyM-fxL4qDJlvM-Ig7JcpPufVXuIJv27mvb-PlTY2YbwmEdNN7j5BSGxqihNi2_ts3R-lm8U5JRg1p6EqY644MnRCPQ0mBwQphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuVp_1SJyUHJhUWtKR9ZiGE9HCC5ikbsqx1NegAgR7ajYmsHcek_-Owg60ZPA45DC5iqCUdBZ7x7JBiYP3NbPhWR9Aqdc7Z0xS68Lpeh9yMW5NWJ6s3MxpHVhpumHuV0G8X91P5ciokef-YJNbDLWyCqz6AzWn6IyhSMRVr6TXceSjMJfvhQGXBi5VHd6y6WsFNZACiJL0kOU8pZE4EyI-XIT5HMHWdTYDjvMbf9V8Tg_QXe00H4iv4qrvwIaqTJbLfov61Oa-MQ1pP2LKVdKYNF1KxBLHp3KW__0roQvXBYH7_TyIJ3s2FI7cqq96qaIOclax-HaqiaBvAcebSXzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=ot1YTUmZDMCvAoSL_eS_6MLfknSLJAcg6WivZdmSjPwgE78i2plfo_TdkOuV9PdeTBu6FS-RkHOT5RPay5cfF5and5HYNgkUSCFFSmHcGqmkHuWg7ZPCJenFQgMKTSfjG2YTCGxMEQtGaEXI7dgydUQLx4p53O4_Zw-Q451XB9w6CwKRImT7fxmJ6mX2MsUnz80r3O4oLLfyrhKKl6kqDhWCAPnXRS3yRZRuXNNRTDMPFUVbbkpbatyYPEQnS87bfCEXO9HmQBQ_UaUgtJcHt7DMdFqK4tY9JhOxQ0GeL5LFRn8YRyB5lVctvku6EIeUtXwbeB8IGPhBjBTCum6bgxRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=ot1YTUmZDMCvAoSL_eS_6MLfknSLJAcg6WivZdmSjPwgE78i2plfo_TdkOuV9PdeTBu6FS-RkHOT5RPay5cfF5and5HYNgkUSCFFSmHcGqmkHuWg7ZPCJenFQgMKTSfjG2YTCGxMEQtGaEXI7dgydUQLx4p53O4_Zw-Q451XB9w6CwKRImT7fxmJ6mX2MsUnz80r3O4oLLfyrhKKl6kqDhWCAPnXRS3yRZRuXNNRTDMPFUVbbkpbatyYPEQnS87bfCEXO9HmQBQ_UaUgtJcHt7DMdFqK4tY9JhOxQ0GeL5LFRn8YRyB5lVctvku6EIeUtXwbeB8IGPhBjBTCum6bgxRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDm5qWt8zb5Dlw5HGdT_FDmPpfEhIEk3s_FqUyNDFs_ZJ5zK-vL29zdvW9aW4eOWnk9IkiEyfeOKbrNxVNDrP_ZSMatddHOqP3B612WSPbhWMQrk5z-CTrJjaUHThziNVzY-_bY16LZHq859xxDROenhnyMtOqymlzUYPy-KmfjW7ryCXy8fx6EDR60utepTa6PQUB_1_n8SgvkKvDbceC5Skj58F4RQdybUx2KeMpB6tzS8TKVboev3lNbYWos6CLTSB-XSxFeA66nopm4ahQKTP1a3ReNENsk9-0TRTS6oe0yhQOI32XUKO7JTx49rAfPGe79LCUL93tLBlxDK3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpKp6jqXMPDRZG94voVsg6v_lF8p7uF32-_5DsECzOupKw1ITv-SPCqIyH4tKE5jKPmLrF7IaKgicaj7SZ4fDVkMDlwxwHQrdnewEhT-D8-hPLIm19_WQBQOrzmspskV2hzvNxhNKqFjWUPAg3neA1wIKZooCAK7b3UV0mv7HH9C3loBOBcZj_C88Uuav0bA3BXDdg_hpFtU2x5RezgEyXuiKqz4xkwS3m4WZBLY7xzUnZHA80NzZDiniO8SqCEVAlLtdWjxQ-DfC1KZDE3nM07WCx7_BYpvB2aaZzc6DLsjGNvMnDQ2agX5QXSsCT9XdDSJav4tHYqtdJbTM1DdgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9XgPLfSPpH4qJZgpCsvVijrd3wkyYUzudBLj2n88Oy2ei-TUq8AS7QvylXYUrLhTEnFz3vseZatxT0ulmgUDZscTTNNEPAq2bSuArRcIEv1uhj4KgvkOoP58MJLgw9GRpsHZ40rnjFWusMzo3GtSuXiUI1vxcLRhLT1X-LJkAAJgBT5oZQPViqEldVsHzWPMP53vaGy_l4oim3s1KRvEF-otZx2ytfeZ_mvPLOEWtvoFiYdvlSrzZCO9W0_QjEUbpTcIelUe1AU0JtM8NQSKn8p3mfk3gh5kby1yJlM_SYQFZvlZYtX7CqPNu9NP790upmS2Z2KCpviXOMSz8oUWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1V31b94I5wkSCjVj__FRxQkwdPF_rucztw6OB-g3b7naQtne6IR3k-ZG0T4wutxKHZDwMXipcMAWGYxgVS6DrivJ3hy0X5NFBD6mlYOatPr_m3bM7TLnAjyusx494D7U-EBiq2SL6dGxblOSLbxEmuOozZmbspNAutBugd_IFPmGbG8dIpaZZrAjndfqFNAYiYgsLgC1zxBF1hIVQ_-DVbavTvMag3NZxCfuzpXYxkPFVjWFr8axvIiNe-XpCa4JbFdgEYxwOsbokeRkRjhbo2Z7fvQpespgBZ4mi5LrmTlu1QHDKT9Epb3VqVdkkKbK-acmat3f9XztnbOeeBeog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=pEiOIqj9styMnmggtKQq7lA_2bO0BxiQZ3h0xlyvQGLE0Awii_r94Z2G2Kt8Xwq47ICEyqhDg5Eqju0gtviP6S7yQQwJ38JIVYuR0zQNEcJ5jjgsIkIv9IbfSGqoniPaS7ZmV-pRN8sJqlmD_tG_XCUmlftUmm304c00RPuyAj2ojm7v51e6J6vpw7UP8MGSroc8d8zSF1eFpcytR4E_2g9sLAergrZNMJ7meojqdMxByWQofvMsSKzFDK3UdCN0fFJyDlw4tVk7xML5KYdIxIL4zlTcv-_9jpdszLkr9iiJrZCvm4gbPLnb4bkqGj0Q4Rxn5JWRKr3tQNsV8Q5tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=pEiOIqj9styMnmggtKQq7lA_2bO0BxiQZ3h0xlyvQGLE0Awii_r94Z2G2Kt8Xwq47ICEyqhDg5Eqju0gtviP6S7yQQwJ38JIVYuR0zQNEcJ5jjgsIkIv9IbfSGqoniPaS7ZmV-pRN8sJqlmD_tG_XCUmlftUmm304c00RPuyAj2ojm7v51e6J6vpw7UP8MGSroc8d8zSF1eFpcytR4E_2g9sLAergrZNMJ7meojqdMxByWQofvMsSKzFDK3UdCN0fFJyDlw4tVk7xML5KYdIxIL4zlTcv-_9jpdszLkr9iiJrZCvm4gbPLnb4bkqGj0Q4Rxn5JWRKr3tQNsV8Q5tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbiwwVBXoE2suF1KD21QqMkRwYlOaXIXbGV1v98erJHsRswd61AlBMj1bRKR5VMvlAcqSQULTwRXiDJmlzWOzbVnjd8W3jlMyoFop1BRtJmbBYerJSmNuhHh9tubcp1oQg_aGJYpe3uKU6M054g8nx6cOBFuhYSyKhabDCWdo9g_9GayspPaJt7EKqfg0uQOSmbspOoVpIaG9W24b2jbtKLLuzJO2Jj6V7oeM3DSzkItklkBVuuHxxlsHjdh4_IluUiPe-Fx-XJw88_xFz1oehTqqqiaCzSkJWzb0gdFWIKF0tO-m8uUhbjsKKB9QonaHYsrfgG2ril4NsF6C-pPAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=knwLovPxPR8_tpXF0MhGWV95fH-BvgC2OSfVmIbAOdZMJDAv1rPjFdwPk7i9LvBCpTfVM-ilXwRC5c_dif8dK_xM8moXuMJPlLkeRk612FxZBezGNFD9gzl4Eg0GBJEKEWlTE1GssPD0j09K7Nwyj3V6qBraBGQzcTJYzaDCWflKhYZ7AcTAyiApryXizyZJxB2yfqQ7wBScLo96CZDIIzCYk1ajCWQAITHQcYrCDJP0xXb1qgjUW-LEZC2D4IXKqUYAqAJx85m3VPdLtGXXjhXRem7TCh89Uobwl7zIUCtidytcB9QCB-H0kyH0pX_K1JfTqPkkqkB_H-Srpl0Zgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=knwLovPxPR8_tpXF0MhGWV95fH-BvgC2OSfVmIbAOdZMJDAv1rPjFdwPk7i9LvBCpTfVM-ilXwRC5c_dif8dK_xM8moXuMJPlLkeRk612FxZBezGNFD9gzl4Eg0GBJEKEWlTE1GssPD0j09K7Nwyj3V6qBraBGQzcTJYzaDCWflKhYZ7AcTAyiApryXizyZJxB2yfqQ7wBScLo96CZDIIzCYk1ajCWQAITHQcYrCDJP0xXb1qgjUW-LEZC2D4IXKqUYAqAJx85m3VPdLtGXXjhXRem7TCh89Uobwl7zIUCtidytcB9QCB-H0kyH0pX_K1JfTqPkkqkB_H-Srpl0Zgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZnyBSzTsCCzvg4jgUj2K966jRMP4sQgJu1XKXOyIAlNpSRd6tDeDVsUgaj8JF6I-qQiTHMy50PunqQM6Ur1mqLhXeLECKz2-ozvf_RceQxT6s8NONvSi6GDH55dKkecLM9nGwsZSaEfpjWSnTM2Stf0P7N8EOWK_DqNdl-d_b-umN6BsL9ChuUtxPtxfKgcSY6qd0z9ZzstexagWkZZ28PxmOcbYwzWFbMbHE-WAHmEmP3Imqdimw_6_8MeWnjwWILYa6aaAIMEXqG_gjwVCJ9fCIe-YRuyP7Y3SeQ4UJ9FbrU1yfHEGsPw2e3k2gCb1SvaHQ-Ilyfo7WOEhWIO8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnoWDfuZAaZAKjmaZs8oglARBZRzcWpkhBK-nh70sz9WMgcIHrVcwzexBOw3qyWCEivZFBXwlAfDA0HhyyuWOvbUz_AJ67WP9Gdh53TfO4BO_6SVbNGBMg64QhUlXR8fl2thPEQehf7qeKhHvyp4x0mOq2ykfOgR1zrxDrckncoMcuZ9WxIuMtYn3kxEoIzzPxPM5bhaW1TqoCLA_0HqQ40DypM7LS6yCh8MX3m_pHJxh4jNHttyYYSaIf3vcRvlLJT4HZK1eWlIZGH2sBKUPFnDZHWOg5XFWZ_Op9t9JTvnwCrs7lide43gwzwzX0xdO7_RjmxsRoX-ZoXpYqxLJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=DkxGGSxsorRxHzOQ4Vmouazp0pdrAxQsXsR3DZQOMNP_YLOW0RDKbLyV1xcfUd2zd4Njta7GGA3pe70cT7iPaKCxfgJyndu3sSr_Kd1zZAghhzuMvi4-w2ZdpJARInzmRPnGuKEe_UiBr-dXzR3EJmyaJv1fRCiw3seqLVs5HOWJ3UP--B8p_p0ZJfNotzDjQF28CULd41yC08HOD3J-Hq2DIzi2sYI_6j4sa-kuGKbqDy-G4zNLMKDWWSNbU65dkAXdTyez0OgIKoX7l0HOoGvPI8GQKb30aIONkV87fTOm6-AIOUZFmevC69xl942Z9z-9Nbo973rcGS1QnMJa1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=DkxGGSxsorRxHzOQ4Vmouazp0pdrAxQsXsR3DZQOMNP_YLOW0RDKbLyV1xcfUd2zd4Njta7GGA3pe70cT7iPaKCxfgJyndu3sSr_Kd1zZAghhzuMvi4-w2ZdpJARInzmRPnGuKEe_UiBr-dXzR3EJmyaJv1fRCiw3seqLVs5HOWJ3UP--B8p_p0ZJfNotzDjQF28CULd41yC08HOD3J-Hq2DIzi2sYI_6j4sa-kuGKbqDy-G4zNLMKDWWSNbU65dkAXdTyez0OgIKoX7l0HOoGvPI8GQKb30aIONkV87fTOm6-AIOUZFmevC69xl942Z9z-9Nbo973rcGS1QnMJa1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfmYoSQdd2PPoWBSlo6e9BRIe-ov8lx5dZ-cmF5YEEr27fxQ5HhT9Uz8ZnZcHeXeq0fHyXgFzI6aKWBD8y3s3860pd4xhe7YLWyce_KVnE8DT3eog-vn2vwnmeY8kO0IxkCVO9Jc-SkvHzp7rRFHFg7IBrMHpwfdfrEbcU-afeo8E3m-3yvbWzWGcwynT5wFpxDtlDAXYhPvNvktiXsCEsIpIech6Slg5bovQBQBvcHwWYrxOD_QWWxFfHWrerGVSOCUHAW2_os1OruB7QrN7xRXmZf4cWIcW-dLFwsX1wZ80Gm9zIQk6sKs62yVy0eo-CUTnw-kCmSnqlrxnTIUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS6Ql9QuX6oZsbuHA4sJbwTYfuH0zpuQ0mgVHz-8kYVkGgmj5bE3tmtNRBawkvdMWet-jdGqUNBMT1bG-zvICJjFkpJOfpwOWn-P2pN-rh7t6HIwkUjuBav90CH9Y2tY_QOxIhFensywQ8AyaV6dofff1bk2Si4JW2YOJDSnQyxSDNiBSFusf9LyZLIP9Vn8Ds0WJdHGh_1292ARhhvxuy9lxaac4-_YQIxyYj5TMG0ohvxd-TUJiVw7un-ICP1lxqOzyYwMMKMZXhmn5nIF34XkQdjXcsMaD_fwYWtqWts0od7AUQ5zUbc6PJYO-WZBpZkVyyPtqC5kbo_VMn6Oew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=Qj8pivO9ZOowpW6lnjmPd_oH60LYiSFg_FTZCQ-3w5KtE62Hucaorn_-DhI4N3NYiijVis99ZB-1UTcMSaApTuEhmRQv988AiIlRkq06ifw4To2QF3JqZwPMqWNqPokfELcZlOaDjg_vTEfDm0l_mAFYp62gTSz66CawRw1jmJNAobuII9cOvtH_emeIowxoshYqx0xTqqJ15-SGwV1pAQOh8X-3H_z7cErAm09GtmYSJTCz7asUFNnwi_hMQf5-_N4GD2FTVax3p47YnU26X7v4zTULMgAo3EFkvyefZkwsyJb1VjwtlD7DU0FReQF9GLolXdMWPeZoLpQq6r97-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=Qj8pivO9ZOowpW6lnjmPd_oH60LYiSFg_FTZCQ-3w5KtE62Hucaorn_-DhI4N3NYiijVis99ZB-1UTcMSaApTuEhmRQv988AiIlRkq06ifw4To2QF3JqZwPMqWNqPokfELcZlOaDjg_vTEfDm0l_mAFYp62gTSz66CawRw1jmJNAobuII9cOvtH_emeIowxoshYqx0xTqqJ15-SGwV1pAQOh8X-3H_z7cErAm09GtmYSJTCz7asUFNnwi_hMQf5-_N4GD2FTVax3p47YnU26X7v4zTULMgAo3EFkvyefZkwsyJb1VjwtlD7DU0FReQF9GLolXdMWPeZoLpQq6r97-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0np2-F_P9DIU3JqZQuqGOjyHb76zZ_LFTykQWqaK0gUUnj8qBUSvC2_8kVpfTo2CQTKa1bSdg1Ez7G2Tk0antFBKcvTKMhG5xyiE4KjgOS4T_zRtT7mbQM_wJ2sfNQ0hY6ZJVJO_nhmwDr7OM6jL6oM9-XICKbLtcQkYCo_eFCvbYDfxqrHG1Y_IRHuuv0Q4hQVq5S3N40R_FVX6pkFRY8bYtAU2XTDZn3gJj4eVfkm-Twia0w1zJYhuRpHeHGIuSjzNgJo65KDJt944RFN03EYqw416KFF4rMZMZvs-hly6brRMV5Z_KtJ5GQNOIjoyGTklDujIvL1K1CN3r7A1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IECv1EdEcU90bMc2JDBFXedEpGtxs4YIplf2XaiXzRno6METZTBoYEXIzFwndVEl1GV1339Ks6Jmh1ZpTlQb5M5GPIEZc79paMfgDDwUinpjWw6rpxmieggV5jzoLMh6Mw8wV2vCQzeS0itjDHQQbEP98ChD7NQ969kpufrV59YAN1lGhkkE_BIe9ACD2YTQZd4OjeElupYEDke29-Z68PJS-ePCef1HFyGAhrkFG07GX3cPt81BVnUHzeaDgdP4sHvlihFKId9T0i0ov8EG78Kt1DL457QBvt33ZlLaLQ6237ZCk7ypkO5cbWQu76d827MrmXbI0TOiSNRdV6UlXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv1-RA4E1G24NiW1-LpyG3r38uVUL9RwI1M-byglRzYZsrUw2hAEaTB2p-dRxI6b0GV3oVRxGhBgXEzup6FpiJOpii5u9zYc_vVgheIOSCNz17PPYrn_l7xCLvjbbFpK-tvEx1-d-8lJhv8_eqnPLKmdvJHg9Ve7wQfWuLN6MJqTxsT_jC7qdeZdky1dr1XVHcgirLOXepbirAWwndFh8HhdyvwET8fuQWN4lprikxLXFDd8OPYQgvFKsoRfp_FfDbbRSSE-WN8uU5hf_78MGaOVvZki9dAFgdEiLiPI6hLA48-YxykLDYQ1u_6eYPifKiAVIYwDcvQzOZ1tqWn9-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvox6Rtv_PF78hvqHpF-eV8PZa8vxSU_hTiNpflYK8sYunt2uMI1gwUUDux1P6UvwLM8xjSMJLEUrMSc4A4E01-5j0NzVFpj98HU9sFWqM51LQUCug4NUVCt548xnGZC2cVJgbbIXZgSgTGTojUNei_zRLMefnOBu5DVCcMt5kzwQ7gkTAJSzwvmD6_MwZQYyPlTTLL0ITcyZj77hp8fCW26fwz0lOsvXYb8B4n9o13x6xSqtabM6R8p3UIwBoJw76IM5bP21QIgqIrgG0UUnZSj6nDoxq8H1OdfMym4Igxyqb8Jx0jUWDSyi-7zoTKXaAnN6-17dMcmMIrbtaA6NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqt09JTZTUQp4vL6XC0OOMAO7Gcvcb8k6voZ7j8n0KDkf98KL3o2fB215e-SAdPy5BM47pxo9X24FyH4_EIwk9V4zjjwUOw4FjCEHJnooOCVXpNNS1vLpC--IonLYT9novJOtsf_fnIQ1BEGhgwIMTYufGabb2tJsNKXSte7zzyajkF2OdzwnjxNcS1rPwV_3sLPPh2ClLZyB4BamUqgeyzg1AzlODsse0o6mkOT9_awo8Jg8sfCe8NHoCMX0mXvyVJ9loDZSaLZ7K1v8V9ThpKCT5vTMDn5peg2TNhBJJULMsbHke6gCUXb39JL7CTfH59ZEjgoJImqmAYEqZx9vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCsOA5DHHJDgEmBpL7Ke3sit-4y9Jb1c5i9zGYOCo9uT6V3ENuJGtKiQKo4Zz-RgagLFp2LgMepU0gHiLFo0SRNTPX2eKlFAmRMKxCg549PlE8hTN1TBOgITdNxBTgQsH9RrMPPMhHRI0huG_MgAhmheATfmC8qa1pv4yEe2RI0uZgBCI9SKmH8GDVoMI2-M7J2CJbgzyDG22LugpQGdIW4keLlpQAcTu9yUTcmAMrlZYD9LRwDbjSwPfVDoiSdbASfONgqQzWERjB4_ycKM59bfZNxpAjkqpQLPG7O69H9NqF1EbSZ2kSbDXrNCJsELSzxZwdyv8b3xyq-8WM6TUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcpdWf8l20p2u4TYjIO2OXRevpDKwS3ToZ_z7HTZSxgzaTuy-8O9lbZqkTvJVGfmFmBnt5fzfP-ckmWXj-hDTQ70ujNyyDRKzKORb6QZkb4obMUf0p4HNFcxkKBl7im6WiizZKCkqMhTY_mAfUG7buB4jq_eCihGPxvddxrbAWSiceG1oZ4hh3yQAWxsC6JOI_CpI3NUApyBJ1sKH6L9Ub4rxvNGwkdVr6hKPWPpbI9t2iSqyQ4wtRukOEsaZx8ye342l7f7Zt3WFVa4e0YItTtXDovQOXzbgGzOUAtfZqnnCLqz75yHdtLs11Q26MO220MXu9tJGmcQnz0LtnuIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBXdGTZT9Uhsfd43LmCkupLbKoUr_sKdqX0-i1mCkJSwajPFpYDNS9_LUnOzJtlCrX-9ZS5_FDgX4XUJCXhoK7uNG-x-pLqWJ8jx-q8FM8pALt_PgfTGc9DCKOuaYQvNEcoo2CEYiwsL_17gm76ZxAUGbHfnuInIY2Er9tEAOO57H-dRjbxvKeAUr2ptfMoIE5qerA9z3JTouFIpeiUxMEX5a6gS6vGC8Gr3V9PtjJ6FuqxPDYq1bqnhuF_y-2beQWO0iAW9rI9sQnrMSWYVmhyQ5BPoI1oDhAoaQyH3KaxFf7w6CQykJByXDsLcbdvSqISmlPCvg1SIKnrtZimovw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiAqZEQDVSsFKL-HckZMR_XWE2bppIPEBUeLUYX1Risl3hvKQ7_OBGFjT6rUSTefPdTPlgPvYYlbwPmjJZIqi6pA-BwNXoE7ZYhuHC0c8PulbbdBWG7qB8FwccXhS7eX_55tQWGdPdLEhtLjsj1nvnxaLh40Bu8084Y1OsqKRvag42O4gmM3ZjVehdbt8jjy6Bs8GsFmQUm2i5ISK2JC1EG_o98agyUguBRZ1Oay4ZJFmxOdL1A8-IYP6NzhDxprK4UkKf5R2tLC4LbJ1KbBp4Os_whur6jpsAJLrzZ3scFffiePSQt1nky55xyl23RbR4F209sprHVb2jb9HlIDiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmp5foxGbdvvEvntiqUmTbOpUvQWJzo_-ztwLPURz7e59Z-rJmf64qEwfL3dFLhTz5q8k3Ugd-OKRZx8qyipUdZIqMr4ALhw2c8eLWDg0bRLlNLD7S_G3EA2rsmXuYdRslQBYfv0qPQ2FB2E5mYm6rxfajBMB3cwF4P5A1gaP8X4RlNFsVSzxA-laq_fPDHUUSvwpuTlmiZ-hbmfQThWEDNcjyDIRnFmc4ztDqMXF1E0K80hdMYmrMsETYI9OKc0B1mgoCXjA202W0S43JXPq7zzGWi9cwxnfsi0ygny3i39W6tbM50601C_yK2WQditb8rklRcg9EhlFw1tl9rJww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYH35aM6ifrBzb_-_NU2Gop1EWGJ_BZhYLdcOlpFd81HwkugcqUMxPyLPx9uhilV-YSemeAYjaxPHXj48FDg3RKJ2szCRs0AgLvVVedhhJIZwqdM8r2tzZ4HYZ1iNja6t8Cn2A3SUyqc9KyYSW4PBK_ZJD7mDw0oEJXJ2ueKdrop2a-YcQFK5GIfxeQRlAvyOi2jmLdfCJg3IgFTKL-xOSlPwJKE8bbpTmVBJvwFqW4kC2kAKtmdqZvukGxoY4natcswFRpE7IJ3ubkrRFDM2tO8iNet5H2pnnL-c2pdrvtySIcBbFEO7aI8usNrV5YrpuTqLSx-KatQOOldSUybjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqmGJR4aNT7_6-egQ0QvGE5aaJwvHvVkdGV-U46jmIjtpUU5KQc4edosEQMHVXzDC8Q9lTQFgKW0iA_NEOFJYx1OboSJCgM9hcg-N2ONYDQAxpil4MTN7EvSq2LZRFCMNDImJP4QGlD-9nCTMu5s9vbqrWeq1jBJfS4fg_5mHlprJLg1OvOzfSitK8XJTMAtVhlICIt7H9NAVRCwGHaBCzp3q8dADPEoRQpotTF0xx2IMCUIhXh58aajLpkirsFW8Qqg3d1Mwb2OPxy2CJGCbH3N3aQUtOYR1uSIHVhW9OKqoCbFyTYq6eopweEUFLMIsrm5A1vpnDOWNtt6hgwUnw.jpg" alt="photo" loading="lazy"/></div>
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
