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
<img src="https://cdn4.telesco.pe/file/XD7btWRptX0P08WZ5UdmjUoXde1n_vOwDYNKmPhyGYoBor46Ilxnlo6hDQv7CHnC_So0-HBQHFeSi_9P6-1V5gIJe0N9vE6edl_jCg2V6P_zEakAl5-sHq1NY_rmuGaD6XUL_9YYPfWHuELOscB3FmsuhQWtzBP9Dmbo7IrBOOTwsI1f2igzRdVWAADVbxU504c5YZPUDIENQG5eCoMHUBWBedYVaybWB4xBu_MuwLCBOBjh51ms8IwS2eHwGIfNrqoCc2RKPhhhO6X59uMvL16NXZh55T6T6n8QLGdZD3UEcb4NtCT_mlSMpsA3yr7Xrvm_wcvrhK_ym6KjudPbUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoB6-Svf97C2xSv_3s4wgksYp4O6bhmgQ5iYzTLPKOmSUFv2Vk3pGbLn4OQLag88rFJocJ5mdeXHHYLzuk91-cUC-YODfzdgYL0lMVk_NL5aBXVBVyFPz_BAeaIg3bhA1xuA2l1XILJpkehwGLviVT_bBaKn1ZMiRughJI0lPSz0oee2wIiHxHrff_hFwex1L1ICC597QiEr8WEUedw165BVhfjEoZkHm1qZlS1om2M0nhIDzY2UPS_0yFRBp4IPWXRj_ZzJkDqIuNDQ67GWMbz8Z5atxQVCOLC6irAC1Bf5FLX9OG9OEHmy4vjSGUjNwH-ZHkmvHLipJq4BR6BBPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj4fjdQDEobwuKormXqc3UtabA7H5-JG7XuPYll5Hn6JfmI5LMx0YYjYVXqbwJHVSBnC2XnK2z3u9iJMFWfO_Frags48bGpfDyYmAw-hEL_DyhqH2VdUfBBc59Hbe8cqUwJxpfr_MR-TaGOYkwc1drUyRtn2sdMUBCEcANb216mMZtW4NcBSg69_B-Lufre7LbBOAkGnHLS_l1XUUzfqU5_eCcbvSU_mY0TKkT-GqAzxhXogqu0rkroF58r-vOISwLo_3hdPqTYBwCHgDZH6OyMy12DU9kTXOzq0w3Wbue9ZebxtnXnIlbo-lSkEThFIYb2OTKmSTFAuIjMepthxPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFl7unwTySQqUOYZ-piHc4rSpcSCFz7jHEOhWHtj9lr1PBL7UnZn3yNOSK3AqFcJDczrJNq3Ak7COj8aiKebfCcsLSnvdYhJQfrGTn22VrmdRH_LSgDxjgy3I4MoOOa7EW5FKqIDn5FkPAdzfTeoCCJb9rT9IrHXeX7SqTRhWpogWPb_AAOqBcgBboKo5fi8EtZr2uubSoqEieGG_gYcYOzroXCExouun8H8NTMU82AJhmaAe0yJffPnGnrCVyCJIZ7vMPFYrLS5LxIxmPvKwb2MdJNZRbrMul55tp_kb-25eQ-amYxS7TDI-KxPMDbKgcf_lckRbQqwY88f1qH4Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT1Sm2vbO6q2aK-o0tW3x9pI66gK3Jj57NLZeScHt9QyZ9AJJlvr1XlPuC65WvqXlrhdDkRS6TybJzX_BqdYsPQlgJ3I7S1otPFTUhP1Q94Kz1AQtVDunWzTI7RkadG1rgOcV2Jb_MGpLBlxdSrE4BQSxVFl7-3UpVt9UzslhilqQTz02vGotYq7a4mSjrR0EeVfCVSSFrl2X_45sQlrFcnt2-C43E4N4gDZgGaOgH3TThft_nLs7SBwqdcZ7iF1U247YarcqzfT_RDCuJytnFdMnbY_bcU0KJmxgoNljQT12xF9yWbBF6YtsXWboTUeiGH9zYJ1Arnkmmcq_GLzcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtLHSqPeTbaGz9lgeHs_jji-ibSyuw6d3uBod6hbu-mgUnGhVFATFK_TD2QUaC1aHtD74XF2LClBHc5m3Y3yp6A_FjF5f15E-pP0zIyvBHv83Ds3u-Pywwh7ny8B4VawtvJmirPz6438USr4mAPfSFS1wh7jyFMIAh1rx99ZGsYaiX_ROg7QuTcr7hJDXkSTnQvCkycoTmK0JxM9Noiv2VJW0xQHU6MRiLN_auV0pJYCSl_efpKfLmPYY2WawX9f19q8QFMHxKwiT7_8v1cP1QfD-6SnbOLkJz1cdmC4mYTRhgE3KFUwnPByq4yMs8K7PDWRVYttEQqycKuC9x8-8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDcpjSMG3zNzJr_lSba45N4msLbtT_-IHQ3u6P449QYtkMXKP6wlynuvDsf5qZI9p4ASP2cAPbNKaYcd32DknujucKYo28ZyfXxxajaQLYMaC9TCZ84flrlfEaT8Zo4SnjO5w-1m3qr05_nP_osjz0qlC_m0IuU4MAb2Kk-EdHEDlm-rotEu9ZqgoQJMg6gSIQXHIEPX4vhh1YpMC3DAfqM18TSeZ23mvI6q5wTECLrNp0iHsun2mH0Cm0_WXaVQkIutzGYP6AbMlM0IQL_PzLRqr9-YDTKsxrJiVSEGAwdHlgoLORprwYN6fRenRflrYS0MnbzGnw4yN0AwpY1L2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGx4J1NAhQBiR0NHLriuQbEp6McFfyaY9zpEa97scR1u8Cg0LWptfXU_n9DO7afk4QhOKkP4m0V4vyjdLYTkKZSCIMVW777Vd1AZAhaov0EYoRLBuUW7IzQBNK4BnuvPrx9OnpaZ6X-BF_nrhzM6dSDtxMw1gzyA8x2hJ6X4C2RqfCVfpezqccjL1f19908NhomtVi0C9-vg1x8oR7641azzIGsha3tvbFWKaS-w5IY5iy0nYp_1dR0NNt84KRNJLzTktZzWklHvuzmgn5skZxZwn_-x2u8AE5yXYCUlKml48lhUIM2MgTNf307X6vojtQZJVBH-U5Sdp1OfEZlofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0nUPC7sBnDYJJi7AQeYnKn5OSCHBuqIenlhh4nQb1SJliyepWy_nPFT81aYQEEmgkBZCcrgpCy6egEY3z-FNuMC98ol26oyo8avxqSpcDJWf5Fle3tKen3ZUQ0iVsqiXresnbcahHPqSQ4DOXX69PnuCoYW3C2A-tKdMMQR0nbgBvlXlW0f_ISrBFHm7TSz8NzpkjPdiP6KedaUAlVPw6uZv5qjpqt0jEIoVjyU63HQ3tUjTkICrw9XzzctWaLHrm1HwKfldjd9GXXeWt_Mpu2TGt99kC-c-k7M6GxviZ4iupoBzoIb2K3NZZxQk6I3c9WxWwaCNE9ZO4oKlLQPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZszeYgNx0-SMtUslLSUNPLfKnfZc2FQOZbbKYqXI_UZWTqAht7RUPUwZbYJZ3p4SrUZH9KLRUdvN7pT462p_XrdE0lVKOLt5cmg2SANYXa5wbpWuhkTgstyWvfcfQOHu8q1lR-N-nJFGH57C5kHMhqTz6NbpTWjQM1d0KRW0oKO6-qX-M8k6Az3YsqIzlKaq9-EeJ7u8L2NCu1wg8gt06X4_3rSsjuJZxKAyafc9Ck9QRztglaoeDATulh9ju_co0ycJEewi4dOE5DNWMZ5Z-pn7CpLTmMQjq3VMKN162js55OjKs7r0MvJe-AMbfim_S4y-wlJLr3u4cy08IsIo5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okhJvmcVbPJV1lFB89YN54zkII6UMgM7KCgu9ZHu8JUn5MjYv6TVgatUcoyUXiPjeRWnAE_FmqGMJMSwcn_Kdqqhsfj_Dmz4IB9VjnpjJHqwDqk9fZbDAIiOMySzfcmE7AlpIR4ybxFOd5wldZCNTLoYNMc5uph62Q4o3N2DyrMKNhIHiy6mx611tYODvABFvr_Fatz8Vd5Oz4V07t_ri2cQvj6wR5iowxs0HsPexGAphJu4xy5PfXlRYT_5H_yyD7Y2ooYwhA1Gk8In2X-J4I_EPveKfNygus2l6SEFLdV8eV2pK_kBqKKLQAMgIyV9sqPGlTe6cYPGjlwR_kjWbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7NZK-_19bku9dds-sJUGjJAb_b8nktah8vZQ3e9wV6XKgdu-CmJG0lSIe8nEuVX1ubaedOLImqJeMldEWlt1_ApHy_8RBc49Z5qbwpZkqyC2na0OGIj5PiJi23wCB9knJRFG5Tv0CI0iyeme9Q7zb0K24oeCmgJOu9AUeFoYqsgDGp0YBszccvSskQpzGr204Z8PVY5gopq7e7WECg2lq35bScPRZaQ4DJFYDyBjnNibM5JS2FRw33EjclZyFEYcB1m9HiALIftlcOPIJcc47bmX3gxzfHlbZ3NZ95A36QqS7wVYs-qGJCRRVwde43DQdb-CXNFstptkn6LdTt4Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3WQZJBJVF8aBACLUxqcEJs0oviw_LWCCd6iW3gZ9X7tndI8VGsbLz4BSV25zXf16DVX_bso6gnaFHKWqOLG2AmgiWQL8-D_Mz2b4Z0ZawRWk8Kd4cbuJd7owIg_MwDQhBk3q0ypAd91tPfodOBeUPfIMAFnWfRRuO3HBC9L7evWu03vmn9kbJu6GEJsjs9QLtn2ZXy1lR0HHBDt3rwDJp9N5343uQFZcjX3YAC3Z0b0WZIkwkQv17mv_20jtE58_7OBhyLHzquP3xXQtedSytC9eu-DNdJJOIX-eJPylJX9VrZ4LC8JlLJ9LWHzKJ41GcGwq0_LuVXMoP_HGJ0l-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2rdHHoNEgLyjEmg2olO35GMblekXIzMay9azzpUGiNoCS5hk0__fOI8Tvn-E4HzdrtV8Rm2rtMXHW1D-wabsnHt5wZpDd1NWpLo8XGf_fdaV790WLLi3hM4BUKm7Q1lNKAlrPfTj5jhkF_zBeDaBbHTS3XbNBLfViMSOPeRWqFV-A8YA6Ck4uSJ02rWfDNO_OV3-RwalBl9kkg59xAqaiJ-sRHeFnGngQdrX_wItAxBrHruCscp-jo3E6biqOztltfEOvl9LjcXF8L1FuoXzYtqxqgGI_tj4E1lU01eLZH_hZDgaBvc8QhgJgk6opHmI5dEr9dyxFjGtmJv9hpj2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDglCAHcNpLd3QZvuBpC2LiLaDxBpklUGLoyHoArVHbeYxrlR9rY2CADAfBXTLe_8HW6o4DRnnVi60R-4Bq91vEMcz56Eo_HPxORT63pKHf40gv7pJeJ30j9PR0jxy8pgHvckJd9mkXEQnSKz5aDUxavVmsZDFYwGMyW7DRs8EUV9aVO22FK-rplB0CparD6Vehdn9LVsWUdqadfIIW5wyoK39ijxC6eb5GYc19S6D9AHNdk1DhLg6BzYvyVltg8Y2a2ULYsn6pmvtepBMhkKQFj9m5xS6NOIdf9WQDU85m_3Ed7g-Ms0Fe4N6u_KL0CEzDCFUIR_6bpkcUjEV2lRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSk7lMPCEvCXM2z7jbygeXkxfwhSbZQQ9HFkNAgbN31ptHdSjXcfrRXAr8Rwksz1UXgV03d9lCCUhAwK37XtsScRL1ZaZMNnn6rGlk71smspR7u7XWfn_EyRWKOl7j52KRmpwTe3h57mNjPKucbHmg8_swWalTd7dBGzK1UbU1dkDOGMdMktIrmHsai2mdUHExNcBq1EDGCUaouojf1elkFy8_saCq-D9-l66gc6Bg-CibHeT8uTbV5Rp4RVgZndWKrU5-YUwVmD98Bv1dPyFW7oEJvvsqjNks7TPdifdazNUxaiDbfaKUUrXXHINm4eTe0tkEM4YGG6Ps3duBdMdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtEKcpui6jc1OozJWcXab4KV-p0J9Yx8GQrWPzl6anx_Q2XEahN9_s4BNf4ImOJLun7iIC4rGs0l2TKqzOzK23_DS9rZIx-YbQSyQMtfTfz1keBVIlh3bVKCjACnYT4J_FLhbJiz92N7uyorP7_-BM5nB190PsmphL2mZNxpTZ2Vj_fuLdhqrVBT3L8L54EOgRc65dwPPG06fqo2gR8wPBWCv7qn8g0HaOAHidBu3Kp8Ww9cDYfVadYngocdek-VjqY4CnI1gB3TMTvmTUUmpHPyhlv2UG22oBQ6K6WYrUo2eb2FueZRJQNebQO75eGKHmXUGU7H8KwupvbMPGvUCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=cQXvTJfjUUmKIpEFUhzEx6ywPYUobNGgJQUcpHwrZWxkkzupZiK0A8LlCixDYI2tTOXxxYoKnM3K-n-9LAnHbAAN0LrIi7tfYAoY531d1DvngYSSCCfOnXYznopLhlat-84dz1Nl86pfs1x6Hdra8S0otEhfrXxTlqR4HKDkSgewt3Zt-uPkhV9nKmI9OgEwMTAUTuQVoiZ7PY1WmUSchsL9CNJkyFKgS36M-QksEVOoXShfd_4pxdfNonmB0mnovbLGvnWi24-Iuakr7dSHw_BQ1l8zrlPEHv4AOyF_hF7P8O6JMkKUOz75qR7Z61edx7jkbDX9J_UYXmphqneuEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=cQXvTJfjUUmKIpEFUhzEx6ywPYUobNGgJQUcpHwrZWxkkzupZiK0A8LlCixDYI2tTOXxxYoKnM3K-n-9LAnHbAAN0LrIi7tfYAoY531d1DvngYSSCCfOnXYznopLhlat-84dz1Nl86pfs1x6Hdra8S0otEhfrXxTlqR4HKDkSgewt3Zt-uPkhV9nKmI9OgEwMTAUTuQVoiZ7PY1WmUSchsL9CNJkyFKgS36M-QksEVOoXShfd_4pxdfNonmB0mnovbLGvnWi24-Iuakr7dSHw_BQ1l8zrlPEHv4AOyF_hF7P8O6JMkKUOz75qR7Z61edx7jkbDX9J_UYXmphqneuEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=uNGQPoLLqDt1RsBaxJ5KLrsAKMNWO_jWPnDYcuMZWjCJTPccPZgoWj4jmGlGGfTmU-rwSBT7-L6zT4o0alPBC1WIbiyk2MnH6LvpH2-RVeSZpyBRefgKe-m1hNNpDfTyRAi9_hKrNTDp2-ITQQCvDgQCwG2MqPwKeLrSixrIW7qdfW5-1-l0mMMJ5MNr1wtxq0e7m2RoCdxD-h7fHfq8q9pfXE-QuKRAEfUs_RAPdFR1rXNYj02ZmaV7_2CufFfC_XpCXj4Qo-3jNf1HfiUBAX46I80P0qdsVO49nI9RwBZKBj3XINMADHr9XYnb5avJvQqEBaM7-6HukRIm3LSJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=uNGQPoLLqDt1RsBaxJ5KLrsAKMNWO_jWPnDYcuMZWjCJTPccPZgoWj4jmGlGGfTmU-rwSBT7-L6zT4o0alPBC1WIbiyk2MnH6LvpH2-RVeSZpyBRefgKe-m1hNNpDfTyRAi9_hKrNTDp2-ITQQCvDgQCwG2MqPwKeLrSixrIW7qdfW5-1-l0mMMJ5MNr1wtxq0e7m2RoCdxD-h7fHfq8q9pfXE-QuKRAEfUs_RAPdFR1rXNYj02ZmaV7_2CufFfC_XpCXj4Qo-3jNf1HfiUBAX46I80P0qdsVO49nI9RwBZKBj3XINMADHr9XYnb5avJvQqEBaM7-6HukRIm3LSJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0RDPKT3WfavkvEsYYG8F4RLAvGZ0-t6blxB4xw_bsGmoGAwdXH1Rkr1aDDPMKrLK0vaUS1Xzmta7SgKBwGcyFRKfK7r7gkTr9LBKVOZU91XMnripMd2vA9vUy95JKb74Y4U2163Xhj1f49D8Gjiq_He_oLSbGIQLdC0jDgsNqMyOAbEhFhp3iccAFp21Qzvw77HFxVIaax0eQ9KxBHAnz8G1-spH70Q824xUlKoEcpcSDcFWl0zoBdumLY3fMwsr5SIMXeU064bXWdRrZy6piEMTTQx5y-cC_FoV66nzqb0WiYo1ZIZVl6s7DrGwI5WR9TqT5FClJzF_S1KmOglpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8XAW46jSXRgCeI58VRk4ni4Gt8N-6xo7PsnHPg_mPfyQsioyPDUVH86_gvoV2btTvfIMV9tUHGffS6yEwWSxfu-gxgwYd3fxCgdEydSQcePI_xt9fja1Dj6dgRinvlV-55_4iZEDJQHfGrBUec7Od6bzMpfejlfG7tKna_7ac4U7WRgW5_a-83Q1nF20ifHsCq0tGaP7Hv1uz0pvvTupiRaif4Y4qGDWbaXlaerWGmi1rwZLJNf2ACWuVVefKvzp8GnUnpCQTkYN1Yn8wJc9wA--5kLcytxZ6iVtBUcnihXrwJNcSrjIg2xmBgXOkAgDq-ro8VRgqbOhMurgF6Qzg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=MYt1FGJ5D_R8dNar_HrE60X3Tu5nEbQ3zTXRkVksKM_swhK5ALX63eZv3LYI_u2ocE5IeS5zpr1DnrJTPALftEwS3hek6CCdpJKjHym8SKIkc0atZnrD_kaiUyPKUg9MJqzE-FceCJWzd9faDn0BXs-LQGWpm-9Amddw1wbfsyhYqO5oYlMZmKctCr1wpEDgM5mDGI1pElO7NWsKWl4nVsb9mtKGVjJ5akaS04OUMnN5UOmiM7fSvQs9OGgV7ALGZq2hJiX-NE4x4pFVtqrZ_Q6gzyVZ3NsRyTesk_34IFSu7z-SgLII8ytokpzVAnvrdGQfI3-gCUNaRzmc72PZLSFzJFLrxc3shWFQHtMlmckzqYk4RLWDEb4mPESKXRWJ-xG7K7ED1hSNJf2r3qNgbDlR8KzVItglJwdcQmjF91ZWY8aylDtOEB0zw3GJW25rPZxKWFmlVPqjLioI6kbXy8SMkLteNlqxzDKzG5eqy7QZ-sG1n_Erux3ARE4GxlJYcaWnAqFkc2x11cCfenUob64cov1Q3fJNqn_4JKYy6F2Mrh3Hi5UzqT_2JY94DtKN2VnLT-Uxh5g_ASvZxGAVTz3_x7ATNTEY6YV5rYJkLxn_OMXiSLnvq7zUUYbbNApwofE2rvC97Xn7lOlP2WltJPtwu4rbCukw06cmJMUljzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=MYt1FGJ5D_R8dNar_HrE60X3Tu5nEbQ3zTXRkVksKM_swhK5ALX63eZv3LYI_u2ocE5IeS5zpr1DnrJTPALftEwS3hek6CCdpJKjHym8SKIkc0atZnrD_kaiUyPKUg9MJqzE-FceCJWzd9faDn0BXs-LQGWpm-9Amddw1wbfsyhYqO5oYlMZmKctCr1wpEDgM5mDGI1pElO7NWsKWl4nVsb9mtKGVjJ5akaS04OUMnN5UOmiM7fSvQs9OGgV7ALGZq2hJiX-NE4x4pFVtqrZ_Q6gzyVZ3NsRyTesk_34IFSu7z-SgLII8ytokpzVAnvrdGQfI3-gCUNaRzmc72PZLSFzJFLrxc3shWFQHtMlmckzqYk4RLWDEb4mPESKXRWJ-xG7K7ED1hSNJf2r3qNgbDlR8KzVItglJwdcQmjF91ZWY8aylDtOEB0zw3GJW25rPZxKWFmlVPqjLioI6kbXy8SMkLteNlqxzDKzG5eqy7QZ-sG1n_Erux3ARE4GxlJYcaWnAqFkc2x11cCfenUob64cov1Q3fJNqn_4JKYy6F2Mrh3Hi5UzqT_2JY94DtKN2VnLT-Uxh5g_ASvZxGAVTz3_x7ATNTEY6YV5rYJkLxn_OMXiSLnvq7zUUYbbNApwofE2rvC97Xn7lOlP2WltJPtwu4rbCukw06cmJMUljzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0-B9CgARoHza0Dm9kPJBBTsial_q3yYGylcQqZmjjsO5_ecZogElvy7MoeCek-eW_oftkjn20l90lMCjWMqvc1t9WzP-4iemHHtwU9picuxgmcOV1R5oSu6VabJuIhSku8pe558oUqGyqupHCBtWw8R3JpybcOlYVmiCcRWi1xyD5LCRbKNJWXISVqPWB5dhPnv65LWGwev_Pg4r7V8lzItOkSQdJ7Iy3YOpxcwUOXl8DwyFydJ6SZ0dRdpvSnEYtHAdYgMWUv3E3lX3Om6RDSL-K9YVFuVZwhKvaZN-xyD5WFiSYB_v3RJbImLfMYx0Z2M97PKmZJASRhg-B394Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjudnHCr7nKtff9LKoHx4p5bNQLoE4xMwv0_azgjVYBZqQZLLqeLDw_cj70C6OoltayDzGXUfXBNMgwJxrx6pKxQ6j8Cv-LIoCgCfe-Hedjrg1oa9STCjSRCGMOFks6AQYjnz9wZUHsA3mcgpIaVN_1q3JphLD3p4oWkvcm5F7xZ9bUwEmT43RMj7LXFcPfJ3U9JmBYL-g3BmgacysDqhieBE9WoCxUrAXlg5s49HDe_2HMB2qQ6wN2KcTez3BNy9S9HPCINw0TiyNnlkFMBasqlvmboPCyqJTqP68TDeyCwatXuErWCUR6dv19E2kBX61vdwKCt5ue2-u6GVHqO8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iabdDGTOZ0Vf1Q-u90JcFZ94eY-2CUeIHlMeY1ZmS3cvjiTkPwe8vKf2_Tt15jRRcCUyEE3EqE0hIs8vTl970QEhrbNhuNmT24l-uMAfe-rkYaMMIJ1IGP55RkQmPxDNRl4VcX-MNrboQagPPiW2F6EZm5BorbBbBsx0f1m1sBeV7xbcNfd93b3YCeaE_6sGPQBe88Mka-xMJ0uABGYNjgbzdO59j_fe8zQLZC_bEcrLDTX8Pv5dnxgNBNo3ExJJxL5fLlfZpPOnduut1xKy8Y_3jrhuz0PVS0kgF5mPQmk3jg95c_dZdkBwSXP_-_Hu44Xcxi77Y7Eq-DsvKZB11Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KniBMm6OGPFkcRyH8rVkJ6lWjUbVSMcpfLuQS8S9eUlDMe5oGUdiLi07_tk9UOykyGEKAuLKP9ZNr2oUuC3xrBUGvpmCZEAzVp46Q5noFXGa2xb6dZw18QupRvRuSSrPObluvL06Ypelmjp-3jBwZI8rUwJdO2monNmjUmT5Gty90fMfjjDbkQfQS7xLIwiM9ZHf7YjxDCmBzN-GU2POscK_Hz-efn0dukeQKKY4dQ0yE9BbPML52G3evDKByHoiCZBfjs5Ml0birMivbdJYOjZnyM5jUNvgCE24ZpJu2SV02haF6emyVvq2u_8IsKW23KGpPr7bRJGA2hcDuEfo8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me3aYsDGKu_QE3fBHK0fNKzngExhV5OVXJNIwTmmzuib3rdhvdmn_JmGe5e755O50iNYtq2V7p3QawbTdSiaI2fB2PclhKzJRebXTzoloe4G0bzd1_p-fIDT6lxAEmqiVhSx7jo1cc5rEJp08tLSFfSWuLvd6-Hu9Tz71vid-vZPencBzg5kITLvVYED1MOLvq8zF0xOf7P_XaCrWB7sp0ZvQG8BzPlAJdxcJ1Mn25Ju-SRhR83r9EK-V1Xvkyzg8MVSAJ4cb0OeQTPon796C1JxZMYVeYc2eRxFWaRB0CHdGp_plxshGvsnLv8d0M2Zhgk97W2FKUexLx6UZZsmzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjf-cY2qk53I1zqW8Go34yIO3Frq7YifGKbBmKMCUtNcczz21CMusAlK9aOF1JDN0hqmW4GUd26JAyBtRl4LPTZ5usHbrgZerfDI5Cz6bD4BxBlP1n0FM8gOLBNrAcdULkbKHE2z3TEtq1cQvupQC2l0teiaKLrMdjvijjvFr2DGt6E2Bfs78_lpH44fV23sLOg4y9Dl0pI-umZRCujsreVmZsYxo6luOg5k7uvnN9n7X2ilPYavXzJGoJCY_KC_-xpE_t7i1IzgflWCNy5VSxe_O99ycXQuv9dbGapbiCr9GLsuj79Fgr_OSRgX-fOrxJuVwQ4o2cOuq_OiIRBAag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ZPj8hu58iLbck-P-dr_Io6ntSDgTk7jpF79gxciNOo1GMS7ep10OzpmVfh-ZJeudFr2uOcjWc8l-FaQYHpld0hYUNwrqExL4BsueTjkfs9nhIJ4yRrSV4z0iZamiJVpVIQGUehblSyXOv9Ec-CwmNLjTIbOGCmDnxkQ-DG7-NJoQe_veWiavTOjydseWz7KBwBd-gg6caTrOtYKFM3auhDzUKYFNOTKjT0C2UeVX7l6n-7CWnfiKsYzBm24l8eN5KJzwpOWqc7hL_rF6S87xxYJBTBiBL01v_8fRarn3-sXhaCbur_1X52vNxACrlTK2sWxuLtVllTs0Szf1EHvoEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ZPj8hu58iLbck-P-dr_Io6ntSDgTk7jpF79gxciNOo1GMS7ep10OzpmVfh-ZJeudFr2uOcjWc8l-FaQYHpld0hYUNwrqExL4BsueTjkfs9nhIJ4yRrSV4z0iZamiJVpVIQGUehblSyXOv9Ec-CwmNLjTIbOGCmDnxkQ-DG7-NJoQe_veWiavTOjydseWz7KBwBd-gg6caTrOtYKFM3auhDzUKYFNOTKjT0C2UeVX7l6n-7CWnfiKsYzBm24l8eN5KJzwpOWqc7hL_rF6S87xxYJBTBiBL01v_8fRarn3-sXhaCbur_1X52vNxACrlTK2sWxuLtVllTs0Szf1EHvoEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlIAEASxmKKyyavVcbwBFEFnm7_VCsgCpS_P-evMOmTgmpAxPb_X5eZzQfaOX0AGWVzJ8KK_zDYCqWTycgqUBAbyLOr7bNk9Xbc3nfzve7uhXxcorAj1ntiPGRELWG7446BEW4jd2BES8296lW-TMO7cX5l2WLjF3RhZY_pHuFA3RrRCciYqUAkktNXnWWAM2ZmLL9zGO03BUHUleN3TaKs-6VdWlyi7ZqIHHelNNUVQWts-iCuONu-L53M-rmyulot8qlTjmh-5TlgQC0Eity9_mVYG6lXX-9ur605q9VmnXUfDUEtClgNcsN8-46Zop-_Sv98Nm1rXs5cgavYVCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf4JLbzI3XjALOmWz3qEJcJkYWWjb_2mfkXWzPUaaw-r2gavHuJPfYeqTn9Ld0de32uyqP5bpDa1jW3_8-3cjVo8pTQU2ff2N2r13k2EjivxIeVuiAGJDJZ9AqRQHqDD5q61gkViQLnTktEQIZVEc1Y0lKYQkkl720sDP_BKZLNaNzSvr6JTWLZELDOo-q8Lu-_cLcnXZsfTklVDrDdHf_6wkqViR90aPwXTJrQ5dF-FXkyjrUd8VfG8sD8RtEaWUzqvYPgaPzDDwRe1p0bH8XsZUYjsgBvSav92Ha5n09-P5X_TwHt0PGYkVgOaSt64MzrQ9MTbnaeWqeFhr87XOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoaRsByaiGFlcTaoKV5hOcgEBVbHG_5eIYQ7bTkS34SDa7XljvRCLUMi3g7vk6dAUKjseF3heTiCJt7AvYBI1mFbAoSstvvCoI1R5CB5l-VDQPHplFSp6_WQJfgbv97bS7Tt8h4AFtZh3EBiL-hHIhaWAW1poKSEohk6R_mB6Qhf6GV18ve1ymRwMIIczShbhNKuqWMtZeQrI0MVEjjnOZsN7punyPy7u7YDA3LJ6gtIUSwBR1M6WQ1Fo3X4qjMwU_dILZ-1sew2BUxZ2jceebe5UCWnIchUDDkZOp2vO2-UqkHSNDdbMy7XsiT05G8-g7c6IP1Id7CLA0sK9NcNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4AnqE9MyKV0LpQfdSlvqtOWQIcl7c--2Eyl_CpRvAgyXHXOB9jFDWGnDx6wIqUirjqBEye5AezuUiFPTTnW7nb0A2tR6xQ56QhS3o9NWr-om7ePAKuC0B8oW-tzKoQbPegDpy4RCPotO-4xl1t9a5YpxdMQswq25FltAW2dSXwb4C2n5NJnsAmjLcfzQYzNtSJq9qcih8HeBXIZ6uP6wH6zJvDEagTzvByZNzEDmalUK6IaQ8UwLT-qWMi1dWIYoSqJMGJWq0F-7CZvQhUU6ShMD8v7w_mOTW9lKcKtaEwMAWil9r0RbBTbuaGlDjvA8YjyPqCfyoRf-FUPyy2Wrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbSPeBH1l9XmehCCY2tlZf5kwZnbkLiGhS4dBwKG8cso6P7W6boGuj8KAOrriG6fpZtMFTVczy3Uq_D_majtPcQKcHyPMPpjp9QDHqgrYCctWaZnz8S0h_HULjOJwthUrAEZdIKxibhpLPo4G9Ry7dOCQpSCsOODG6eNL588W16FvnVYGHqrOlcovClwZNdbJOFeG_TGym1zgyAjuWcgLvks9-ePupccOcSh73VSS_gODZq_8TI8iYuPaJJHMKoUSIL0oPirl-2pHBl8D_XyYvjfEzgICiwbbcrml6nuh7fbKWK7ZVqscunflAx-gWKvBkf8gNosxzX56oKdWxP2Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoYrzaDsHGelN75uk0r8pbb8pv6MVxAKdFbZk-Sos0vB_IRwcvga_WlPry-DYuxDb7DKaMNqCUM3VS183BkOWt33NSe8vR3nh5Bva6IozRr8LUnbI-xe-x9ZJhdfF0J75ZOJHA43uqt3oklu5G7_tWCznARtOEZNwL1P11mU6jSruUXEoSxXcpbUkjxT4_7fGKA1ecGQlY6ko9j-gnFPhwaSJZZIv1_hshKpJHbfmuTUsSJIHO4kYjyodl2j3JRl9kgtpavfM7f73nB_pKfTHyq5C7NKOMsjdoqtBNs412YfbDBuB-z8Bc-aIoKPoK6uO12W2dhyHafbR_IHF0kgwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4dtyVCO6dh8HxUsgyhuRwVrc9z4moxaEdh1V0Uh7cgwiN22VRufWRvV3j8s5iN0P4z_UaiqP0Y6pZ4kisY5m3qS-d0SnG4rh8D5bT0rj4F5dmISAi07h-TFDCjpFVFmeHeGuNHCDKLdlpuqyjF8lqjBBD8eE8jfSCNvykmVXHU0OMjjnhOU2BQyKbO30MjigUxj5Y7rE2IPCSjNj35Y1Vd807Tif6Gy7-l_UHEDHBop4zMDI-qXCn2I1clfE1MhEbjBvfuy6mnooWhvD4GQg3JHF9H9eaKBfTUZaQ5BHybNOEofeCSqCKtdR5caFS1ayzJd6lX-Qz7GutrhFHdAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmCbrxbl0UbqThZkyGEYeITKKQoKyNPe5zKhgeVTsh1fww9VXwBihJoCTgPYunFJJtA5V7y5fuJan1dsREpBH4KmIIstas07HqopKAbsitNP9819nYrRre_70gIZFusJQaAnCw-Tayslrn6Sotj6z42V14c-2sdr6YCS_-M5puffdseSjGxG09QCVzatG4w4xGHRxb9L3Z3pS6S6WWeprE5DnqjZQFmbfvNGi1XaakeJaZbKTbtZzrJo_tIr2RNtel5qfeigTiHWSlKJEwA7kfCAp8TQMBtvPqBE1iMXvBGe5rh6fsFyP6J9QbP5CllkBQye-saU8_YX7BHBsq5JYw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Wy7NmbV4LbB4AVtUuei8-uXFEEVRZVkHSo3-4BIq03jrzoaQQzVekRdeN8RhjE80e27AtgQ-lmV1vQJVg8b32EptmG_g92AXjenGRgJfNA8z6TntaMGzRb8d0Co3q2A63BQjL5cq-7uU9Tub_e5BuL5dR1bkKsNC_8975UYv7Rh4u4n2UQjUS3PXvH25sbPsLq4JNRQ1S7e3bJ4qVFuWIxMEoofzDmzfOb0Om-3AFzf8fe5suM1TmqpP95QSyvbGvCoWbpnjMgXtppsKYY4oeJ886mU0KyXEyrGF-Or-Dt3bxvXBJczC2a_9hc4rHgOwF-yezcR_dDsHR5CqBWrI9W7xFp-E0R2MOubHoIU_Uu_3PrIPH7HKYj9pV7CVg1QO4H-uc0L6JiinbXueijsnc_SOGTcr6tk8hZ9eland7G144jwb7-lK2Et7g46xZUNID5LiR-_Y45C5xuYIdJQlJVoYs6w0Ewi5Jhp-zlq6GYpuwx0GxtnFB1swd9XaTgiWS0wCX-pWi_OPHXjhBuevpMAc0UF-xTj_rHMTnTvCs5v6PwZqLbJu6TMd9hhQy8AVBWKYWD05TpbLKj1xvuVqSplEpefe3gBumYtm3Pl3oVL7kWiUmKmxY59hgRsOc6l0kM_jzvk8P-PXUEfXCokbkqPQCe2Kg4WkRTaCyIO7oMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Wy7NmbV4LbB4AVtUuei8-uXFEEVRZVkHSo3-4BIq03jrzoaQQzVekRdeN8RhjE80e27AtgQ-lmV1vQJVg8b32EptmG_g92AXjenGRgJfNA8z6TntaMGzRb8d0Co3q2A63BQjL5cq-7uU9Tub_e5BuL5dR1bkKsNC_8975UYv7Rh4u4n2UQjUS3PXvH25sbPsLq4JNRQ1S7e3bJ4qVFuWIxMEoofzDmzfOb0Om-3AFzf8fe5suM1TmqpP95QSyvbGvCoWbpnjMgXtppsKYY4oeJ886mU0KyXEyrGF-Or-Dt3bxvXBJczC2a_9hc4rHgOwF-yezcR_dDsHR5CqBWrI9W7xFp-E0R2MOubHoIU_Uu_3PrIPH7HKYj9pV7CVg1QO4H-uc0L6JiinbXueijsnc_SOGTcr6tk8hZ9eland7G144jwb7-lK2Et7g46xZUNID5LiR-_Y45C5xuYIdJQlJVoYs6w0Ewi5Jhp-zlq6GYpuwx0GxtnFB1swd9XaTgiWS0wCX-pWi_OPHXjhBuevpMAc0UF-xTj_rHMTnTvCs5v6PwZqLbJu6TMd9hhQy8AVBWKYWD05TpbLKj1xvuVqSplEpefe3gBumYtm3Pl3oVL7kWiUmKmxY59hgRsOc6l0kM_jzvk8P-PXUEfXCokbkqPQCe2Kg4WkRTaCyIO7oMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnWVyImg0lpx4jpazdo1pumvHfZ20A1V1tqdU9rx-HQqUMI_dx_-zMdngcH5Lj_mFItggFBw0lY4khZkWWt4_VjY35Q3_FpbwNvTvDVj4RlT8TB9e3znUY60hCIe9Bwl7UkxqujN5sbACEbahHg0XVvHw_MJIRHBD87ZcFwVv9CLnzD-Z-Wg41tlfDnDp0pxGTIL-H0HOrRI6NTRIKcOtMdhvPMj6dmU6mJlppytN7ufiqAP0PajU-r3E7LRbw_y1-wXmk4lie96kdkBpJOHX5HwOh_Su4wuTRmEeOJ9_vNdejYgdrxvW3I3Ik30HWxYDXc1vzC-Ms_s-4-G6wUs4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzrmEj5Hy6foIIXsZ3kaJy1YYW_QZOBStVkMiFc1-vYGADFleirf3jiCeVWthBVH-9T9zdbX_XbwHeVnyCehE9flcFfbMJDr7gBKAJJXlYQfm9nECe4jrVnn_PzlSGR4MOHcJanhB5gOJYFOuSNTQ9PvsJGV8oM_9ozATxyepRyZJbJr4xB8Zta8m8QnA2gmXzIj9-HFFmGIppZTgz0VjyeNLDmEuOze9JwnxWIPmvJTzNUVirDE2XWBMWdOrMP3BCe9Mmgyu3ZwKcJdWJUOgX1u3OBfjar18SBxNv2Z7YIKqrZ8JbY9t4vbeKDMMNTjuPr9HX3KDWmiewhKpJjHng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-xQiJuibeJ0PG4qJHy8usLnCleThHvAEuPOmEqDID_yw6pJeoJHvwsaoXIE6SV2kXi17qYOq1CfRcu8CEmpI_XLFOe7X32C0BkqZWO4lRTNWvv7TdBfoaDNy8p6CJU8yuNTAUId7ma5n52nvWzShO-rq_Sd6D37aY6SP_K43PlMBhrQ3fNDY46nZQDYYSzU0_zTZVD5PRZt3lFvD2J5X1EduDwp-iRL5rne8wlBnoY1tQwmHoRWULH95ZxxljfSsIrBxKoxhPsoT69lpwqZFLLn155Bs8GL5WqTStg0Z7Fni49MOaFEhwUtcytddONjWwallieBVlv84xLIkz-6jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ-L1OvfvVJTRfFnsZa_uhhbtxWJ1GbWIZhuHrF-9ZnYKU-3w6J2KQkC0gu-7bXd-0mtRSBX0DfrBlZMwo4lVIBNtLgrGO1m75sddFg__BURzwI462pIG1ODrEZhZ_UGKDdNKZaGD9_lmes0-gpCLiZW2e1h5e1Xl72tRWbgv-u3YYZY_wTha-BxdKbcrzzVxfsrOdRUXyOAxoP-WjckQD3B3qpPMvMPXB5COTcFz37yh8te9zWdPwHBUEtbBnJ-4dAOgUch4ew4Srb0uQW9w11BlHuT5tMyCJ-8N_XzJsryrBy8zxJB0_JjPugn0JSAJLPgXTttpzApvxKBhmmYEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=WRXW20GuETa_txo1v0b4urHA30X0VvXszMkKqjD_q7G47So3nenDQYlFEiv46Du67fLkL4dwUpcSB5WkbIZJyBx6u4UflVcIf9S4xEVEREEA-uJ8VxhgbF3wvKcsPWXdLQzdY4PfQtRUEcX8UC-50a6ciUN4ONscnCNqcQCVlWFEwPVFEhH_4HE5p3xHa3pGk63aThteaDnHzb79WwvGvYP22gvArovoYQWM0v9n01sNGcu3qAo8clfzJYlWD6DEnbUMEntQqQcy-T3axM-C_oKR4OUBN_aylC-lL0FoLATOjy2aC_sLlyKK9_jF2NxCdIvdYSjKSPC54hRoT2jS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=WRXW20GuETa_txo1v0b4urHA30X0VvXszMkKqjD_q7G47So3nenDQYlFEiv46Du67fLkL4dwUpcSB5WkbIZJyBx6u4UflVcIf9S4xEVEREEA-uJ8VxhgbF3wvKcsPWXdLQzdY4PfQtRUEcX8UC-50a6ciUN4ONscnCNqcQCVlWFEwPVFEhH_4HE5p3xHa3pGk63aThteaDnHzb79WwvGvYP22gvArovoYQWM0v9n01sNGcu3qAo8clfzJYlWD6DEnbUMEntQqQcy-T3axM-C_oKR4OUBN_aylC-lL0FoLATOjy2aC_sLlyKK9_jF2NxCdIvdYSjKSPC54hRoT2jS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmAMU4OX36l9H_sRkrIPhfxplzabfcU5JZuQilb3vNt0j5sfHmKxKunE6P5tQ9_wUCFmiyXv_eC1TYjlB15XcrggHVYz8CTnLZsH0cqqpVWTfJiFtgtpd3AdB90pd-W5c6T6RcmlSJ5UFdNQcj3qF-dPY60MxQQ_hjrVIu079F10uCfGlWKtakOCaLIxi2isVTJ8Oh3t70eZ9EANDt8qq18yWOOa_RJlmM-m4i0hKb3IS3Vk-fu1pRly0dlOVmcRDnKrP1wB4N-qOuq6ZUzj0KimTquxqOxEgJnpOBRsyOPKWqyX0Aw175y8tYG2B_HlC3BkwZzaEnvQhs91rLKXHA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=Jv_GlVYz13b0Cq8RvlCOynJDRXxgS-OzY-Nm_xxxfkzSrRql_6pZh6mwVtyq4dWksHi70_4hCI98LOTUmFNn9LVqzWDx3reUD7Qsyx73faLte7SmIqdlw4IsHyJ0dbsnCIK8x4NgTxDLRbZuSCdDSek9ODfjOVSADny9fVUHohzGxSyGeYYs4ekmqDxD-yGTMbFbvZt7UJNyaesQS-pTr5wwa_pQVHpcmzbGHLeNqz3Qxwj7rkIOk9r98jBuPpAlvopx0KrxOqGiCbVQtPoouL5RGEcZ46zEWqr2IUMAAOTnK7a_ufpqR8CHkqv19RLak1swmXbM_7OPvt2gTk6ydA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=Jv_GlVYz13b0Cq8RvlCOynJDRXxgS-OzY-Nm_xxxfkzSrRql_6pZh6mwVtyq4dWksHi70_4hCI98LOTUmFNn9LVqzWDx3reUD7Qsyx73faLte7SmIqdlw4IsHyJ0dbsnCIK8x4NgTxDLRbZuSCdDSek9ODfjOVSADny9fVUHohzGxSyGeYYs4ekmqDxD-yGTMbFbvZt7UJNyaesQS-pTr5wwa_pQVHpcmzbGHLeNqz3Qxwj7rkIOk9r98jBuPpAlvopx0KrxOqGiCbVQtPoouL5RGEcZ46zEWqr2IUMAAOTnK7a_ufpqR8CHkqv19RLak1swmXbM_7OPvt2gTk6ydA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL6WwRbEwnxJeNcXPFSTFwFxKgw6S59WTfL__Cmdl17EIWiRmA1PGt9cKr0nQitjZNWFokQrC0R1masrDtcBq8wnf7wA1hmVyFk2uByyLp4A6vWIj3kTbZQoyuD-ekJnyTb8YZXCdWazxaJPlS6QhQPAlMsTQUhgECDD7VLhEyZCyyDskAwhA2X6IHW4RYSs0Rm-J3dOvnC7vLgTzb1vNdwTYA6Pfp_GpNQzvKfT91URoGLXru3zrSUsDWc85XHpJ5Um4bvbVOiurO0ZU3jI9rYcq8ry-qsoVVFQlOQMRQek_skw2qScYQjuba-Pp5cd2xFmbTuZ0zF76Pla8qMQYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPOpIiarVjuE9AymrTz4WYn-yQQ0gnkdL9JbKQiuSOVRAGraABkTpA-0yl17bUkwqAmpraBJ-IA0jHdEFICj5arwyxURhbqzeSMG5RIyPN6djVO4LXzSq2QtkmdNFm75nXYhTKWz8HYtVzKLaaxyGd2cm9WQNQANyyz5YXhavkUm4lzrTFnEbrsybOcHifrJRakB3G_G6P-bT_wxmPZJ8Hr6fmN9zpO_BsZIhLpHyTXyejBeL6LzLtojmU5Y9FlAjli7G9_GBWg6WwmFzX476lXzZlzKG1SWhnvDxzMjBo2QXpUT1zMrpBUigQ8TBYrXjRrb1TACoNETTw9d-qtNmQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=ko6Dn_ZfrMtxO22fzxtWtn4SvLlt3t-VvlumRdK9hRMnjCyRHLBw2ZxvdPPSkB40o8vAKuq8ADnKus5FmLA2k65NKJSJewGfyzsXDJ9qgRZ-NgtL971ZQSwrg4cVYXgN18eOcl__BPzXzeQndjzMJ-noT-3oX16CDbgLeiDaxgAaINXsdCSBpVyI5__YvDzVm-QHUSSmta8beMFqsc3qUVrS-j17xdtgxxLhi-xE2AaNR3mHKxsK5gV_Rz3xU5UVm8d4b-qomN6_k9jw6KRUdHwm__ai26YguEW7FiCAFYdJ_izw8K6-y7XqzTQEIbUZTMJr9j-qbnVrxdJHN_B24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=ko6Dn_ZfrMtxO22fzxtWtn4SvLlt3t-VvlumRdK9hRMnjCyRHLBw2ZxvdPPSkB40o8vAKuq8ADnKus5FmLA2k65NKJSJewGfyzsXDJ9qgRZ-NgtL971ZQSwrg4cVYXgN18eOcl__BPzXzeQndjzMJ-noT-3oX16CDbgLeiDaxgAaINXsdCSBpVyI5__YvDzVm-QHUSSmta8beMFqsc3qUVrS-j17xdtgxxLhi-xE2AaNR3mHKxsK5gV_Rz3xU5UVm8d4b-qomN6_k9jw6KRUdHwm__ai26YguEW7FiCAFYdJ_izw8K6-y7XqzTQEIbUZTMJr9j-qbnVrxdJHN_B24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT5vGiEPozHD1ktsmAYLZJ9e5FDUnTLgUT7DiCyZ9zlB-FHh1oh7HiXXqJ8OdwPo4CibCRPijHmiZxJCoBV1L4g-uG4lKJUxd-bNK8TZUrrFC3QOnuYl7DXlGZx58Ea38OJBkPuE-5C0xKbYgTT5N06hMYzJnPlOciqZ7JsUTM282StnJxUmjC3MohVWYe_c5FiCEwL40wErw1PrLSDzoaIUNt5dKnOhVKBX3RKcRN1TmNrvi9Crp9J4U7CM77xv5EeeYKgLAFxGBG6XzzrtGylV6rU5goaQuQJouLYmUt8nsCPKP7gmzeuSuDR00SoEo035ZcS7Dt_V_FqurjPyzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4mf4LVHOdrx1PsU8310BlS5gEcUQv5dEm-4_NXKy9Up_58MkDzuNzzRusD-CVTtPVyU_q8ilWCsKL0IuwFw_zRuZXGbaT8AEcG4DBCMwuLAc02JvYf6v6XeBDI4aSqeD9cqATPHOWT2cK9r9LCjgoEVB_epbkdW9m8sbsLzFfr34W7UEyHHllcGTcJYm0YCkTmbBf7xuJT7yAkDBv4oE7jMWE22DohFuedao7aOIGfjtVHbEtyho_9n_Stq7IUJot1L8HCMgheV-k5NGvsMtBqobVCOa7r_xbstwaW6CgW0bQ0EnOLlMf3WmYCju7Y9oL4ny-AxouZI_zMYutvsTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=m2oPdeaIERRmIV3N09X5idYqXpNd5v_hPF9FVtMcB8wvw-0P71tZZuMz_o3zQ3xw3iEQNfnGVM_zpqpxsqcp2dS5Xv5Ih0vwpI4aN87Wxwi160m_mqQf8aza7DMzjFRsBKyc-rvtEb7sekdb9t4TLQezUAjlauQzqf8qzVZOZaBM2gU8XoOeu_RNjaeYRI5xvzAyGoqV_dq64CmAeOaDqYy9_ZBdZXdZGLxyCQrQb_msyOZ5O5WxmYv4MPVK1SIBWx7nCUrHHSyZJYtBi2XOcuHCvCFqFq-p8W6py8kkLRl0Uf9WRBY8ofYqs11zmIqXy4jia_Qw2KZIauQ1ltgX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=m2oPdeaIERRmIV3N09X5idYqXpNd5v_hPF9FVtMcB8wvw-0P71tZZuMz_o3zQ3xw3iEQNfnGVM_zpqpxsqcp2dS5Xv5Ih0vwpI4aN87Wxwi160m_mqQf8aza7DMzjFRsBKyc-rvtEb7sekdb9t4TLQezUAjlauQzqf8qzVZOZaBM2gU8XoOeu_RNjaeYRI5xvzAyGoqV_dq64CmAeOaDqYy9_ZBdZXdZGLxyCQrQb_msyOZ5O5WxmYv4MPVK1SIBWx7nCUrHHSyZJYtBi2XOcuHCvCFqFq-p8W6py8kkLRl0Uf9WRBY8ofYqs11zmIqXy4jia_Qw2KZIauQ1ltgX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOCG1BlIxzpLMQWkVPtLCWAaw910VTgcft1qfzsslaPzTfT4YeavSm540TYDQ24_DquNU2e7QM7QegA0sBVaceiS2GjTJFld69NTmZ-TMoMnLXJxijb7fUFdaBk5XkddFy03SL9DLKEqS3NtnGaldv-44vxAe0phw2Wf2KXlKcpECwijDnG7qIlA8c9_qol4_bJIm8NR9nCqehQJ_qoNIbLbl3oHokjZOfP8mqMuQp7xAUHq2kTlXUnUnLd4UBxHTddW_Rs5eawvR1V--3R8VvE2KRlCd_OIdir3QhV2k4HBA5tQ7sJliItUWbenPoh4zJZHynZNKXuerm1El5Gwcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxDDbBrTHb5Xa3u0Mpays8Y7Fb1f9m4w0bXz4LI_2oFjpeNdptBZsoP7NYaxwK240x86F-dDpwC9ZT87bIMbxLBUrDjlwKUQIVlyNWYzsQILRjGqlvP-dNW4DGjJgHsM3mlatO1EjA-T1yK4HTRLoI68EV2jAplSTF_e4ctQOayFCT-U1WOiU9JssLYxXhR9RN8C5yXNJoFbvW-SF-_8wnB8QL16L60RxMdSOACnVZuIvnlOg-4WNPDNNjClTEuxBKrdbplKlfbPyMhMUun6OUbW3hp-nBkP0vekXocVNImViY6GytzOUQoCSqE4QOyoPNsHd62yfbdxzczDYQKqZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwcwvft22TOcKBuIa2sOOotwkTOoQGaswV2Nkkk-3kG9EyzEFha24MsCqMoETGowedPxurAuFrDQBU8Jrhl8jLoTIh9SGioOzD-nN_FcU8Y4a9ApUTHI9xUhzedu8svOAldPad3VhlmhasXsvVkz9z5hwGcKrNZu-KCBQExXwZj6KHSDZyxxhkGkoLPr_DMCaq1ffD_L6SY_yRpy3_sFQP1rIxtrufD1HXzfaKaCuSE1NxCDXgP9ykAMkCvY1uN0DJAiZC35OH4yCDuIjI2ZtM5fBZExhUBV2yNM8Uo9Rn1QKXO-yRLf5USvHeOe1PqZ0LkwInuNeDQmi_zSTNEWZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF0ccIRVBkBKO14DG4ctt04QN1dcBAXFfQ_GSC7It6ycCM-NBBKO563nnDSJS1QBtyKgaUzxVwWYwYFWlQofLg1sGqhEqxAtO3o72Ufa_Of9TjMZK1akgFaV95o4nJ4xdrHiU3KbBHcpJcTaPvCFctTm_ditLTf1SaN6Uj4o37XUAdz_iKPPTlcXl0TS2ZAakpajfCfI0uDEdok9OeDgEQmZkeNQVn1j8cwd16svPCZdCL5LDderqOZn46W6YvRGXZQikZGPwS0xijwRwbxgHVDMN8Jp2Lna754hyOWb5mVT2MIcKBu7-9PLeA0oIQ6740ZWzRgd6ajHBaS5oHQ_jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOO4QoYwIamts9fHKlFxgzuY6fihAK8VHdBtx9imvKNbAcEhB2Axw8ag_iCh2GMrfq-12qMqnLbnUTlSk5CJVVOUMlzwfusUlFvpej0cDEY97OuST_OiUkkUJPhUNKprvXcti-UE5tNQZcXYzywzNVDTvesV0FhWQ5YsDmLV94B3_KqAF69kX-EWDupb3kS2miAE_fVJQIX4nanSAfTUR7fZZBbjM5UV9zbYGJRpsJMPePZ5HjMc3_wzLYD4xcF-sF9tDYxWtdlz5ER0MgvRXMG_JFNZBeuXzl6-URhWnmWuwUFQ41vEC32L-96_yZlIhSH2OOFrhY0ahXzdywr3dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Di8CWeITZFNWnjX4eavqnpzDpn51my2RfjsknKvMx8yjZmAlC9OG2dXx9byA4IXHLeG9k8jxVshMb-WTreubeRGst69ThmgGr43HkyY9K6fhgXqddzs-Jr8xXdl0VqAJKPC01ZEQabVAIG9oUvI_Af9amDaKESoUlxYw892PtDvtSxJMGU6sSnizEq-onqkTrjZx7REGEokdXKizT-hxLeQVWORToQsQI0T7xzu5BNW4M2SRAtWeLOqK72peee8a-wTs318j44K8mcgbsfBj9Pn0o3nEST3jYbqwKrkEFyHi9VFXICIYTcVMKZjVtlx2eZoQfkRzXHnWERlj_PuDLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7hiB5GfpxlGRq10IUOpRl7f4s3I7nhQZLoYxcZRQYeSatVKOq9yvZvFWfqbOWahBkQr_CoL0neT1qTc-kTEtBg-6LPJNpg35n49Q-WUeIGwEMYVpvFtPyVOe0Zo6zRH0gJXs6evaQjqtcX8aN-Af1MkTv5pQ-D9JlOSVMqGeRF7SZLiJxw8vpYsNd5UVpymWTyiqsYwCMkcoCmixH7X7adWsM2lhI2Ts292IMKGZjeq5qyfSiV8Es0kBVyb3FFpYTFldGIpMONnjTTKuwAwIjK3biCugSLPBj60ednJEJ9yZ3gbo8G-GWpnb0eenRbacLQig5sH3kuxtx9oJCCBAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksDVxtM-4QhTZxD0F2l4Yn9VTG_4rclgqzCPjtnpNiWKzVGVxCRim_oG4npo_m7oQJia41G2657eIGnqwvsIdyKgP71KTB_XS7LRbPUWBANIfA8B_eVxSGVsAKwcrPwpA65pDtYtADf6RK_dgHIN3EVpfXpzjOtLTInM9fui3zFv2MUVtGnZDbOlhwJ2_jRDjcjhT2qr9msdgNhHnpVhkHgSABqzGXsF1pcakfqnwUAvsf0T6VIE4sZWe_oP1EOuB8QgNhcoePnB4_YkBCRTkBkjFaDkSZEGvw7R_zeEh7bQ-wFtnQRBkuJnxvajpfAibH3imNBvC98TXB7BFalMAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJx-Lv54EObi5aIPE-gbkU1Dt0AH2whN4L8LsGXV_EophzbMkp8_0pUu3sMZMymxHld4iQWZixLvN6maPG_3C95nw8lRxWSo5Bxak_Ud7kdvVoGxuxzCeHj64Klt9UeEsw0AxIPi7i8JcrpL5VaMFhV-5izVkzTtHj0v50QUeZmCvBaRFq90AEFIyw4SAXz5eFDoDahLWW570CA0sR1gDEJqEAtF2XDotbsEmk0OildYi9sauID4G-cpzbDBbYDTnF186pqVH0QYCYGEK6LwUEKUJD509ohnVLjWMKV0hC49SILbm5r1zau_WaQEiLOneAQ3PKNl33vhdsETEAersA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz7i47FCOapjz_cnct9tTwBTNA7Kohu_Rw859oHwmyv2EdixJUF4Ea0yqz49TDLWH5aiQKarivMCSIQ7z1V_ZlbhI9y2UQTQ-ioV8xDFAVD_gxoTr7pLElwIVnOSN3MXxbiHfHbuCLlpXDmV2anmkYULc2H9NJ7i6D3-4XYVj9GrqlI6Z65pND6HK_pukWHJWMTR1rpP7PiCA1AT8ZAVpZ4QrHsgQ1lMUVfwFlxyOkSZ73BdB4vcn_7IAcNaHWVrXYSnGlqaPnaUIaY9fI7yHAiEdOxEnV4Rb7xNZ7ekqOkJH9AL0JiKikLL3Ost3To6TcxoIDLbUVINAfJELZKvmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN2SWzj0FlMKDwQ9LycRMwlI7V59rzqOgTxRg4yZ-sS1cW2I4peZnYyUsNwdhvQjs1VSz82yOA0udcqEz_RGXTJhJepOBlWf9_TRCsy3qQbu5Mug6g82BtHSrZTUu-cI-Tr4PZCham9I1aZTYJg9YEJoxC0RRWzK9goh7k0oW9fp72zOvOu5PjHC2nEDNcjeZ1g6ZslVxtOU5oG6XtOgHb6Afvf4n3k_ZQ5snbXENJHTnJLIpPXAD4ru06hRmv5orNHumOyNPk6vkLNIt6ZDYXBqZsJvfcNDYLXYHosA82TE-BPKf5foSdR4NXI-STtCLu7BbcaWDQl4FJJfNM0afQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NetZX6CZlUqmqf0-Z4BBpaFCeX462WfMWCzQbyFFLOXVhq4vEAuddy7Sfft0Ts21FwzIQGERJeM3AROxI0rsBq2ZB09KRmJkdceeTV65ThoAUPkrWMjtbZRYFzf_yB_EXdGYBftdSU3_HiIwaY1VR-bI9y3sO4YsDHsotJGQRsFms2HSWEv87yupNTrmX0ClP34YocRf4rTxGvbzxqOZgWFZh7mLg0Pzx_A1cugkt2kexNUQ07PyjGoBe4NnK5Qc6gizG_mhW7xA5d1sgEFjgCbr_4mgZbBs8l6MD-l_FQ9sFmkIqA2wJnDZaaGDBbYAdGY258F_RT6ALpbNA_a58g.jpg" alt="photo" loading="lazy"/></div>
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
