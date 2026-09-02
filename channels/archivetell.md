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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ7KMigY5TYhdjIGH39vd4f1u98ggWjKM2wyWFXp-wPuBdwUOrTp5q3RyUy2uY_j1nLqiksQ4IuqgGGZpSbax67DMOnKK_rNa3__8K4ASTUPCze-KGtewtrS4aG9PS4PDEGCOnjgavwVBv67pmdg9gjkDCLwqTBAyHV9aDXBxsgPTcD14LE59JNqvmltX34kZ0tT4AamcT9MC9w0H63js54-9lwso_JEJcC1IexuiOT69FZjMjwlU31juDU-_hxKZwONffdYqUr2J3W8Y337TJJXJrLC4iBjb-w9wcphbf1VpB1lta_G87nxkm3w86Rh1dDpY5EfT8ZssMxM9oc9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ0t7f3JBcfEKFielgdVz6Ixt7aMAWKE5hW6mPUjzP3sTmSRLkepEx80iub8_zRbDfNkEJDEUkW1BaCxOeYsaGspOYv03CoTqQy9al7agZKRBQsEf6fKu9Q52262IOMlA4e7zUAemDUFszn6seMrKIyfOWCK0A477A30vso1LUsPerelMGOJBuQx1K83Y4zGnbzyHBRinjCudsYCogOBRP6XB7XmSGrUMV6LJr3y7V5nds5TM7WafYSoB1ljrzPOneSpq-l_qHx1S_Xsn9-EXNLzYdZUOZa1CPhjsntWc2L1xATZrO6YB6sMqKItZlvJEWO_-49IMnyPOvA5GQ5nUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdgxiUY6rBgxR7MY1vVEk4f769MKP76CnZPZTaqJIQh15n-GHqpENSNaIvK8s-QkQtXanXIqIQP8bCx4nVNZP4XChyg0eDlceSp6bNCqgZtOEu-52ngPzmiPyRKXdvIlejtoqzJ_Q3GziFwp7v_6r5kVn82TydV7mRVEyMXTxf1CdcUdn2CJN-K5IwgI0OreCNOvqv1B37gOGN1iCZufpZFRXAtS5cur7Skst4xtWreKcdUQB2LTc8-_v-2YNSD3zmOXninJckOsKY8WHEKO62nPxajxabxn7ejTQRRLzTysaPzmna0IKeS6dRlGuxEuuWd7eOec7iEVMuMbUUwqMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW7lAjYIxJ-lYA-sn96cV4zF8xHeI5c8RHOTKnIPT3a8pA7jD8-TMEL9sBkrewBEIQhj1Nc0dhaq3bUBtB60FwJG14nCL3LSGZhKf3mXh0jIZzwHivJV37hXURtReoC05dDQHjxmZ8T_upQkxyk-ONtLYaiu3BvI8JIjh-AzadlhFSGbdJnGUDoaoQ5RIHrC2SamrHuUB8HejnR9zGSZM7guH-6J0JKTH7fYDZI7d_NAUREqmwTvEyeCQtceYqq-TwgvBNhWhmGzHrdD_WsWoSCnY7pwecvoFCnC7Y_pahXGKWA52U_RRflEhWCvi-mOwgmdl44eEuEmlIBriH-awA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1cIYoHgjrAYPcbtJNq2-UxFcOl0tLD7iKZhi60_boBiDpln-waFhvp4-WbMpv2ZIzDqlxD8kPHGd4Q1FM2BXuYDeqdccfpU1LwutA1_FJoTegU3H91XIre4C0bmupWdM11lw3yK3CZvvM3ZtsxYvsPx5dANrTaTwyx97OI3RILnYgCXLfXLP1OzKbqq10n6tFhu4ePRUQKoMXBMEyyLDvsVS-FrTu0KoOh-t8aQMDXlKf14TENtk4PTkSgYwQWMlxmNGx8sclz-VJw4hNxCNVqgKlrWjwW6c488w3rE1COmYTm1W5otDsQzoNGNfVmymiO36WZ3mwM-f_KQESOiUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lna8bl6AXLgS4ihg_d0VrF9Wc5S8pClYZDzTPPUpPrP6Ci6Ns1D_22yv4yDzmbuBpF03CJP-t1mhHy3YQxfbKfaK12vQwWET6vSQrRNfxlkY3IuuU8wvl2KOWj7PPbDn0mo1DK14D9ZPcV6PQfZei2q8ZXlDi6OiXXYJBcRhwr8s598UDdP3Wffs7pjPts1k1ggDxaXoao0rnsdBGnS3sGyC70dfz6smR42AUYzZDrrtk1cLHjik-iqFmqHYMH7NTLVRe_dk_5yxQRJDTcw0-U0njnSR_cF9uEtYeVg190qtHsKjbL46gxaHX-baB0o-g2KJ2HBo6LLxgQ5-F39-5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfVpqL-0AdtE-Rzptov-Vbr2oYzPEtWRs_BuuKCOQcP7iX2pd1lHXHw14bwJznW2_wyJ2QEqS6GI3axl82fobcLVJ41mGvDKfs_KLgX6XLVvoXVdO97YG4ecVm7NPDMEmHYSWLs97-VFJXmhcBjchVrJxqaoArVRfNkZEwxNDJj98VDBbQjM1Yh8NZZ3bt0ub0tkuKNyy2XfqEWSTu2cknXdekI95DcbUEuIzURXKe4X_U6m9cp3P_7h4n3EBNWTvuxavfXRXnsdkCLCn1eMIrSAy7ob6op8iwPNWGidKafr4X3piuEGn2LqkeKPgDVisOPox02k9_X4Phr5KBG2bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk4xEMM7V7gyYU6FeW_rrvMtWpNnRHYvMMhtvb_sO9av0fW5hjUOCDtvBfv1VTKcU4JErgvCXJzxMwlYQFXR-iFifx1P3k-JD-ZkixTgCa9nLP4NalJrxHhB6SMVlcXx5Z-Rz4LwpqfL-ne3Dwp-NomM1YbTqMgqf_xSZ9E5W5nmrtgyH6w6-hTJQ6-Zz2ZfKWDAqq7vtjvkxfqJcLA3TUkx3eM5A8KVzbEBZ6R5H_rIZOvirzt8TDpuq2EAz6EBlIhz2mDAulEkWLoTWaSqnvgXjpMb7lFTodV1Jfb4kb7UAWcA6f1aTjKS7ggdYPmM6v_Embqtn3fc7DbrIbmUaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbemo_jLGZGYkj5MIaM9YWmm8Cc6p9cEiceGjMXE7pB3zdZBPiGJXHK1063UQTekYRNuybwas_kBqbjox4P54IWT_OkK7lQrd8Xt8kzWd267aDXmYBpp5CPVuOTgtBTRtcqG-mfaq0hmYg8Ipg32TYxY0jsGIbwe8wYHON0lq359pcwkvGkqjCdWN0kefasYueb9W8OUX1tJ4ByVPF-dG_KLdLBDplQrSc0tXU8rwj2JTwmnTs-UxhIHKZa2102LIQP1HNkmIsSVKEBI5IHo1kpVP8OED8w46251K41yOe1c9P3oHRUuFevKQ9kELfkKYFLjqKdiyGXOsLhFk2TtZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-JFEbNBAs3bh73xnNNWo0SNx1x84rbP89eVq1sBdQMEFSIpI5y1MX7PZNP2Gk4kigH_yAh_MTSyQwVlvP29jlBC-EDRBcwvQF_ILsjFKGqnotK29efzeDxEbnwJL9J3-XnWhBM4BB-KfsfEqPn5qgfyOq2dOkzr79-phVyRLDcdpRK4PXf_m8EfwzjPKyOlv8RWsNzEcggPoO-DKwz9lt72B_736OBwwNjDQ8WweGmVP7291ToeT2GnPihbJJISri5j-Inpywb778Mf1Zvc3Q1586TRWlCf2DofMr8VqgqdGLF8diTotP82gntDM5tJKKq5xRkBU1C9t-gAe21v_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmP2MnZXWTyCF2Gp8JqjZDdegbOaajEeNOm00AWe7Y9u_wGhR0MBGLRi3HsAeS2xRGgGJXQNuh4xnnB8l-_45gHOgHz1KQf_zSIfsQCAPUliNUgmjFtBHvonnE6TLlsLApAO2NVxy7TghLcUNFEuMQHlazy2yRObKjfB0tM7I3gXzdaCpNekuntvVt04nZubkJ-vb1nuM5_gN-1H-w-xsqRqAvflFt2Iqw-sFeLsocUiJx0dzxAeDVWtkzTm4fqrPbAsRpj3NBVfRJQbqRflSI2lDfl5xuXY8h3vdRS_YOOnSTZ65hF-cQlaezf-wbpQybQG1YHIjmpw5MX7JJ8ZYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=mO_EqC00VKruymc9FVFmUr5XkhNaUBS2ikozOAvsJIYO_twtEZ0wU8nRymqJoSqdzyISd1IxOyJPDVpU_5ApQ0x3Pw6N8SPx0cF-hrHsjWD7fGAJN5097-5IhLXcCqS0LZeZ3Jd67JF07I5UJzisDeJIFLUr8nBZBbVtTb35T2s_2jD85Y0mul00FjPjwhAGw9rfj6ZvJbZ6AR9vLFFv-XYY0yURuQnrtPlkAeAVb9awzas8EZynY0cw5LrGIoESQNk346WWRDO63XgB-RUanVJJqybPARqO6IuvxrApp_tqzEygUzSn5qRDiRIaPi0kAP-RKxtBF4BCrGidglpZeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=mO_EqC00VKruymc9FVFmUr5XkhNaUBS2ikozOAvsJIYO_twtEZ0wU8nRymqJoSqdzyISd1IxOyJPDVpU_5ApQ0x3Pw6N8SPx0cF-hrHsjWD7fGAJN5097-5IhLXcCqS0LZeZ3Jd67JF07I5UJzisDeJIFLUr8nBZBbVtTb35T2s_2jD85Y0mul00FjPjwhAGw9rfj6ZvJbZ6AR9vLFFv-XYY0yURuQnrtPlkAeAVb9awzas8EZynY0cw5LrGIoESQNk346WWRDO63XgB-RUanVJJqybPARqO6IuvxrApp_tqzEygUzSn5qRDiRIaPi0kAP-RKxtBF4BCrGidglpZeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=jX1zx-YTVDmHpOeF9p1oC_W3F3QQfrDYA6nM8PCp7T0VmVpEJcP4Pr94JJ_-tkYMX3i9TLU2K1HYvnFPW3r_vgcLSYxSIHqtfVqTa_dw3OA34o3X88Pla0oRJgUJx0MKiQcdkyKWjV0vjTFbI3noOnhLQ4Zk2cnwkeSRBgaP-49Dp2KtitCokjadER9mjtuBWlw1CtW9jjijDGgeRtjoNLdW9V03TewpA2S-vMr8bwQxljai8g57yqodkkU0C093H8529ChotSpiM9CBJbJn3YpLA9JvSIFh62BJJh9tNR1GD4sQWHOXjN4DfvcldNTipLwbnBPObn-cs03lhi67jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=jX1zx-YTVDmHpOeF9p1oC_W3F3QQfrDYA6nM8PCp7T0VmVpEJcP4Pr94JJ_-tkYMX3i9TLU2K1HYvnFPW3r_vgcLSYxSIHqtfVqTa_dw3OA34o3X88Pla0oRJgUJx0MKiQcdkyKWjV0vjTFbI3noOnhLQ4Zk2cnwkeSRBgaP-49Dp2KtitCokjadER9mjtuBWlw1CtW9jjijDGgeRtjoNLdW9V03TewpA2S-vMr8bwQxljai8g57yqodkkU0C093H8529ChotSpiM9CBJbJn3YpLA9JvSIFh62BJJh9tNR1GD4sQWHOXjN4DfvcldNTipLwbnBPObn-cs03lhi67jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dergm7FpaDgScWLOTHp71mO53W4C81K-3sslNIx9pcUoq2V2lO17ikcxB9N7oKS3A4FiGrcIjuqG_IEDI8W3ijUcQoDHykRfUVv3o9OiJSR-4U7w7gFDGMjvgdbyVzINPrPMekvrSgP0AY89-TJqg_xd3ed0VBLk_R1vqjC4yeiByCZ8FMy1By9qsds3zmkRrzvVnWaK38W-RAxK47gKgzeJJlab1l4CZB13iy0s-Y-tIumcRh47VpIJx3LN2BqcQ3mrAbC8UdL77wUr9oX5ea5Gupqu2MY5L07gBoU2rHnQLXOOqOdAcHKmjO64UdyL4n406gRE6PH7hX_MtMUdlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALKL27lVpXDbvX_FlYSN-MFdWR26xIIqtVobRX4lJ7NVR5q1p4DfQ6i2KO3bkXZzz3WiL11-8AVwCs2rrLdyw05NxpE1oPMk0oa-rFlMGGv4RtdzR_6wJNw-cdgsNTPPXG3wzNydF1HvWWBLmqrLtOfex2Vxa1dOSWCbHHIbYDEcad_-DTlGkDM5-SdmSiJZ78iSm2yuStiYHm4fH1GG_F-2_tTbDRRVdHHsXs5uhGovCBx-M_9kqwGBJl4yWAmGNd3pdsFEkjCgqVOLdq6SwrWllCbgINfBroABsel_zxSTTKaifQHknvk5fsCEA_anr3Klx1S-F-ifKjyQGQqg9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be411_wPfAq3XIex9fcuwWfL_J9Shu-Z4-Y7OB7w4WZqyqCigh20phEeF1N3QLtCpPxkFF96kF-dvP9goYRWrrbqq-RoPfl-UPTswR8Y1XUTHFqW4SyemgNsTztrvrS6W2d7GVmLk7CWCiTLsiV8TM-IaUJqZWmlseKMGSWIRZFhtehhIbLLFjf6vluP8tCB5_5b-WoFqIV2td7U3RmoYoIZ0yQMul9KXsSfNWlmaICX0Ijby6H3eO_ur_4XDT6BVki2vuKEolS1y4C4RbaSby9KDxjaiVFtX2awZTZlyC0kov-Dov8Z4J0sJTcyTwcoAprfeMXk7tyE573FZU4Omw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=itDSHrsVoxyHDcjrERJrU-HEhdrnrn90SRwZAUewm4p6LM-IjSEnnQmRDaoaI0G8F5hSqjvU5vFAC-9s9bUVFF_IzvgJaNIeDjaj5nirLPKd26p9ZcIkPCZHUFAIXhfKlNHx6A3RwxD9ihIeUFoCrMc8i_PQefp91GMLv9dNBJW-tF4BfPBCJqqTiAN64oL64SafVfXhB72kLe6RMDJ8tkOB9KanxfM6jrock_7YWo3ib-vVi_7n-QXYJ2Jp0UeXZ5UHGIWfnJglVrV7FY1m4qUS_g21VINaLDNMKPK_mOZUkA6uT2xHmJ6H4aAcnscBGRwQ4VwdZXVwkcNQItzAe1hy8ribDfTD7UEchXv0h3AAfCNf7i531USXkalWr7bDcyxGDOeQN3R3M_vmg__EuP-5nwPTgWPIOl83a2LcvJuyh32Hd1QhEbnlZipfqra1kWc-mkqhPJgMbsubzzJxblFbtwF1a4Nufo7-viN_7YsAUTN5cHL3iMLTN8Pqpf_IXCEtecy_oMyEm61eGSrsXAiH_pH95oZEb6xpjL-H0zONGVWdor5ZrNWERAFsT1PFLshQCqJkbEiH0a2YMO9EnMJBEBhbwZ-EilAV2Bo0UGZtfEaG8Nq-NGG1YH4i5vNfpjKFI0obbLfv0rP7PHB-em2UwG87t4q821nhKQWwutE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=itDSHrsVoxyHDcjrERJrU-HEhdrnrn90SRwZAUewm4p6LM-IjSEnnQmRDaoaI0G8F5hSqjvU5vFAC-9s9bUVFF_IzvgJaNIeDjaj5nirLPKd26p9ZcIkPCZHUFAIXhfKlNHx6A3RwxD9ihIeUFoCrMc8i_PQefp91GMLv9dNBJW-tF4BfPBCJqqTiAN64oL64SafVfXhB72kLe6RMDJ8tkOB9KanxfM6jrock_7YWo3ib-vVi_7n-QXYJ2Jp0UeXZ5UHGIWfnJglVrV7FY1m4qUS_g21VINaLDNMKPK_mOZUkA6uT2xHmJ6H4aAcnscBGRwQ4VwdZXVwkcNQItzAe1hy8ribDfTD7UEchXv0h3AAfCNf7i531USXkalWr7bDcyxGDOeQN3R3M_vmg__EuP-5nwPTgWPIOl83a2LcvJuyh32Hd1QhEbnlZipfqra1kWc-mkqhPJgMbsubzzJxblFbtwF1a4Nufo7-viN_7YsAUTN5cHL3iMLTN8Pqpf_IXCEtecy_oMyEm61eGSrsXAiH_pH95oZEb6xpjL-H0zONGVWdor5ZrNWERAFsT1PFLshQCqJkbEiH0a2YMO9EnMJBEBhbwZ-EilAV2Bo0UGZtfEaG8Nq-NGG1YH4i5vNfpjKFI0obbLfv0rP7PHB-em2UwG87t4q821nhKQWwutE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzjshYZByk0WGJT39Q0RweJFekjkgyKuRmvHo9uJjfbjTK6Ux6ecpm5Sd3lfPAEn6cFna2t9Yhu1B1_YEZIXXhGhMVp_lEgZ7-odvuILBhatyQxnRUnLvnsAvGvudIE4jTNQFWS1ZaB8dSIa4V8WROn0Gssck9Fa4OHq7bbPAFWgwkcJsH4OsI4qFAYyU6OqqlpCu8yjex_h1UDEIDKQ_V0bGSWnU_Cd5JiOACa85VI8-LuHCIuCHwE4nKPmjDXEsa3HomuKu3OnyLUinDuwoLfnD9zcLgRqp6MdetkdeUicvJFcxM3KSqtmzTDcyrRAW7WVH2uSQcCjYy4v6wHFBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbMLFloy1ZZp1bocbvOdFY68Lp6--DSk4mljY8nzYKbTAPo_A_2-X0_C8rUgsVI-TSnon76XlVKJBUpT22RgEdEmma_NNmQM27z3N_hSk0yMGUxAKaZRlEBTt38JJoBUfOoJTCBBNmjB4AcepDvUTlJgxs6foaz1j4yXv3cGPw2ILz8Qvv55qjfU5GSc9C0_7a9RMqsQMdgUcve7mesZLonjVqnaCRA-6K_FNjzwxd8WpEuhGBBaIFWxt1ckaFhRclPuiFg8U_AQ83pdpyVY997PZtV0_XPH-Z6sH3PZPA-oNFWoNcm9__BIscb17LW75msHSsNbTp6hON1PuqFTUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_VyKU-N-dVeR_Fwpy4va6nlXTdFagBHHC7__pESOU6yIaFaP29McjhHrBxK_4mhsxLqrma_dQAQOjwnF7lWSQHrdTg4SAyCedfKqbaxF-NORr_FxEwIFWo8jxCfrv2Do6ELAXTYMcGjQiyVgO6PuFteFvhyZXofcyfRdk90IT9R479sqLqr-nhPacH5qur0KBHXCi6BrjHfylgyoqkVuCvZ9jnkK4GOOYcVIRSTXr-5lXYTpEPqI5HRZfqaykqd3tl8-g8Z8fpHo5UKTtXt3Sxq_Cr7aVdr2IildnDJ2eEKHwoWs5fprH26hr_vAcflTrSsXaTjSa_VS57WijYFxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8G7aWd1mqn_lvWn7bRWfSs0kiKcED7Ge5nvUTIYB0f0Z9M8V2feuhkXkGzeRbbocZuCm38M6EerzsXhiE9TMbBtwaVtUkYmH0Bt1nVN_sHVTccCQbvSCSP49fSF0HgstYY8Whixuycogs-50efnpxspDocRZcktgjKjvNviUNE0V840CRfsY8_ZXIwiA1y3YY4w-ccgYIi6Zx2FCQjjm5A8TPzqL8dPAgYL98If-3fZkLXSECWMw168UBgrtm1SevwzSen3NqN2mPfI-FqBzMc8iOVWW4IH0GSAuvryNiyMKZ_2dOkA5Hy89rKYBH9lTLs_YB_8n12sPR8LhjoGfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJlzYw7WYjFAGFgFNwayGnDGgwpcmHwkre7wwrUigOU4y4adpQpDHiQ29Ih_FN5hyZSlB8qBoDfTdd3GzTUPMq6EESZ-T-0Qr8YuhV5nuW7Xf3bHUz-425QsdfGI58_NT_mZX8Tt4XNH_VlCNAoSot9j9cGcIX7xJ3lX4vIZO3338dhXFM1powN78MHt7Kd19dbEE5QArykz2wWbzf7lcrdF83Yy7em0KH0S78YH_pEYMEp4dbaDOjHoYhcHztBo4VDmRMP95wrv9xVN3hjJhA23gRACa6ScE969Go_R8wrTIyvuuWsbHGNwBQbUZqad0C5CUOIshZeq6sz1fTxd8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcfgS4ieb-Jb60hW_e_8pO5UgGfZTJxVTuSnYqvsLgojPrbEBk5r8yC4VbDdlhdCefWwMy7_qT2qlZRdaxC6XNfmIv2AX0EefXuszBRJRvpjI9yCpWwOZi4i6m8RqJBjs-lCSfRAHLIAsd2gORZtkX104hZpU9-cK8V0hFNUW37lRettBGWO7DUWoGEmbglXKdcSLopi1gHtLt3IFwClMTFEDYTWikijoQ7gjJLH5qMiSPqtZuYJA4ygN5U7LTvm30jxkoVewxRp-5K6CBSM2f4dZskhzItxNbRcN3N4uTe38N0NKpKxGm7l3H9_Zl8x8oXB_5wMH9ln40ybiLROww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=Ku0JYwC-CZbgJfIRL8sz7fJ8mmIgg8V0jbFxnDDAQsobA3rAweWTLm7xtb4TMlFZdLafZDiNJCG_5E7kTYgFGV_NC70qFtNWh0OhNKxzF7nipzYPXvb9ADQRg9ZfQNxbU6ZUKYpMcSOP1iAVxHtGmwkUjVo_oCAtsE4-fORhhwqTvSDKq04K2BtUv0E83pbZ2qhPffVIZg6kIKqwH7dQSnaXg6WIsskYrXAUKxivNEfVY68AoHS2IDdtWbROMBgo4pA0w2Puj73xpoyX5vY40wUuq2vstpoY6qaO6cqYI2Xn7dacUn6t7DNICFvF9YRB9YyQ8SudCexkMWzRX7EvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=Ku0JYwC-CZbgJfIRL8sz7fJ8mmIgg8V0jbFxnDDAQsobA3rAweWTLm7xtb4TMlFZdLafZDiNJCG_5E7kTYgFGV_NC70qFtNWh0OhNKxzF7nipzYPXvb9ADQRg9ZfQNxbU6ZUKYpMcSOP1iAVxHtGmwkUjVo_oCAtsE4-fORhhwqTvSDKq04K2BtUv0E83pbZ2qhPffVIZg6kIKqwH7dQSnaXg6WIsskYrXAUKxivNEfVY68AoHS2IDdtWbROMBgo4pA0w2Puj73xpoyX5vY40wUuq2vstpoY6qaO6cqYI2Xn7dacUn6t7DNICFvF9YRB9YyQ8SudCexkMWzRX7EvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUv_ISPiRo5iHZr3KP4mSevY7vGbUx93gQIyqdMm6W5nsc2vi3Ft3p3G_fnMTC-GgWWXWmmVQZeCJna5YTrLPK0XIbo7khTJfkTWU_dwYA4Y672MvPDtBG4P6-ViwV3bkQYKJeXbRH-oFGalXSPMqM6noAy6R7AoLve18PSKX4wvHMY8pSFM2Lgxqkbe3FbHT0Brx6E7Hgl_05cHj3XG8ymkD6Wgsb9nocRBlOzUZAQQDIe5IYSRfgVzKrcQfBy3bejxbBq3SPp3R6MkJPkPqA80sh6ji7-rNWhU7bWhxTCa74ZfzHunfGDmtzORTL2aMwr4lZG7x0Yfx56n662aPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN17R0RZ8tcfgdFMDRd8Vz8Abd8BJfvuBpiD_IHY4FP7kfyCdlzESBPnAKilb7HiEuvuBBbL9E3DvSUeo6UVAJ1tfXoDn4oL0cRgn97YF9gfQg4l2UUJFApjp6a8I0Xe5xBNOlFMFj7IN0_k7a12Qktnx2uJuEZDHN74oSFan4qSOkHM5wD1btIjwC79N1en5uugUMoIHmUa0QSVCWYauctpVM1g4hgIdc48m9h28Py4upZpFwWgAjZ2jP9VgjzJ65mWYIOuqS-hJpdDV9Y20S-5Vkwu9Je83HeJJTuM2wqzZtCnPDGoTMGxZKrBG1Xn1znrdlbEWwPPcU0cRRkhTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoaRsByaiGFlcTaoKV5hOcgEBVbHG_5eIYQ7bTkS34SDa7XljvRCLUMi3g7vk6dAUKjseF3heTiCJt7AvYBI1mFbAoSstvvCoI1R5CB5l-VDQPHplFSp6_WQJfgbv97bS7Tt8h4AFtZh3EBiL-hHIhaWAW1poKSEohk6R_mB6Qhf6GV18ve1ymRwMIIczShbhNKuqWMtZeQrI0MVEjjnOZsN7punyPy7u7YDA3LJ6gtIUSwBR1M6WQ1Fo3X4qjMwU_dILZ-1sew2BUxZ2jceebe5UCWnIchUDDkZOp2vO2-UqkHSNDdbMy7XsiT05G8-g7c6IP1Id7CLA0sK9NcNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-5dW0mTTJkMlZkaCpolM-0yrJcKcewNjx-FVfRpKP6p8j0FDPsGf-QaDB3zh197O3zzZ5YsjjSLwFJN6cHogZNPwIMjIstQO0ySWcJKzDZ6gdFKFQnPOVuWsdrjNx4xjrl3Jm1lBdhkEtN1LadsFwGWXC29QtBc_iT8uGeWaiVnlX1p5-l-Ns7rJvteHW61xwRFGi3Vhs2dX2sp3GzScbofQiMRliRRk1Uyx05j6w5BC_z4CG4BrzidjOUxTQWptXSz-1ZLrEKA1AvFv0Tnz9l2Ouo89eGe9bBsNfBBC_wmNxu2j27T9ETfwZC1EP9tmwkrwLFSizyShL0EVixd3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcubX5gqc0diPyZdZC3UDVBJuj6spRTToEznzhxeRM4CN5QRrZ6M9zLbccGZM5YxpQCDCQmhew2_1IAaQHAIcABoeh2fecQfMUGhoT1Mqf0P9Gep0iWoxK_839uNpG6KEGF-NJaeaf85KTGA0mwRtBOkRDrJ_aZTs37q9Y6xuxexgKQG-ThojwMY3SnugkvcaiyR8eqye1G_zRwbkCjHFlZllplyYr9SpV4E9eWkDj1Q-F3ANmvulHgWhf32_TskEFrmMmzyH95D5_Bn8CVRYj-CUBskvUmVjohXOEVnrdgK-3CbbUm4_jrmQJFnQb1ev0e2-4-YSzNEbGf8DXbZNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiM6eIgCFalI5xyYd-_y7HVGF9F5O-M7IQCTYkB1QFX7FTp-bSwRLZc84utE-cokCde33CjzZJslXamBmUoVMPW6klYKB-tZTk0BTZsQbmqnoKNgY_jw_K-w8XbRfO_pfBjuXOEtdYl73BcIXDqCa-kn-eiZMotvxSKuFaoxoa-iK4-q4p2ftl4z5FiAB9N-C-IbiphIqmrWBPjNgADGxz2F54vzr_0mrYtqFJVaYKgAjSnl6MxpW-XWWXUKem6mOadjYPs8TgnFgDils31wkjgiq5EpcScwZqO2AGGNDCe8pRp7xZuAZM67WVz6-gA-naPf-LNtWtlzOwncD1X_vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuTIj5cR7Gv6hFPb_2d-Hinf-cVfA8oeOEHgzhGJzT8N3qBcjQn6UTQq7hSkSB3zwMRmYpcY8ZIk-R_f11shoJkVKfaGVk4XIH-cvEZ_p67BBZEt9nmZutT0Zx_VvyInEZm7A88TXN6gksJCR-CmFGQIRWXjGP1tRkELRykyz6Gn324fYot5APBkJh2HeiccLNLRgSBemOk9N32zUvYJCiAHC9MewFg3YrPsLt2jCuOXsj5_93c36bouNdqrzd2aMtB4SrwCeAr2BwyLjH1EZYHX9JT5DsRGu5gfZS9bjS8TFWV8TbyaZMvwaM3fobHLta1Wj44VJvHkSsPcvb1Bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSSKxmiy-uMIyxyrlMM5P771x7QfFzvsF_kuRpEMjjl4WSDzHxDRsmZko-VBiz5KX-fxy9hKt5rgTq3btc98FUd2fImYqj0iiB2KrkIA6j5FndsNP3lGDq4cEHyb8O0cCLL_8G_Mx_WUmCbhKSBS_3NnW3bjmOwq8P5_Fv_OTN6cZEYYYSzVB8LbLpf-RqZsfAvmlD2Grm1wzQKm0gmICDfkiEWPRODvHwsPf6Ea1F1JD5HC45Tj4myub5spDAgOAaz3_KhCOW-OBRqmZ0EOj7AyMt8zntjnctE8D0XUwT3DO9CFX60m7CnUj7JNaccHpRimzLUKtEhCzuEvD2osiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=rAt33okdQQu3KTr_QmKXwWtGB6bS9aWTYAS2i6FXw_iOM-Hdu36Wu6XQdCWjSwSt3VHmhcTJZM-QOCRk8E6XUQVfwx2GTcecOSuzxVANwb6m7O_zwC93Cr5la-QmeKrYMVVpOTN6SHfI_FfTvuIFB8we1JUKCm_cxQGEPtKsx-od7Pusv19BtnouB7a6N5gokWT-x0p7abXsEXTIPPZGw2enR9402h_si7bYFxwVcZzBSIL4v3QkfQuHuoNq1MKxJwy3zFA-F3JJiIN2y9ZFlYR9idILfJH7RljxIqLZB2zuiGrQGR_NrVxWp_CX_UOJ5aii0_srTG80F7BgcIstkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=rAt33okdQQu3KTr_QmKXwWtGB6bS9aWTYAS2i6FXw_iOM-Hdu36Wu6XQdCWjSwSt3VHmhcTJZM-QOCRk8E6XUQVfwx2GTcecOSuzxVANwb6m7O_zwC93Cr5la-QmeKrYMVVpOTN6SHfI_FfTvuIFB8we1JUKCm_cxQGEPtKsx-od7Pusv19BtnouB7a6N5gokWT-x0p7abXsEXTIPPZGw2enR9402h_si7bYFxwVcZzBSIL4v3QkfQuHuoNq1MKxJwy3zFA-F3JJiIN2y9ZFlYR9idILfJH7RljxIqLZB2zuiGrQGR_NrVxWp_CX_UOJ5aii0_srTG80F7BgcIstkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8YzFeSL8fKZcGB1-AQn8j2cs53_1HK1KmwXJdLrQ4grEWJukOq8Oz1HwHbtxn9LQYrgLkWQrjz_LbH_v4R5EecsdXb_iffV3xwxsT9U4cg7vHHprcLKxJBieN8XgTOFr5czRfayBBMVc_TQ1RH6c74d4ue--QCIDzO2F6QdrSze1XYKJHGAKCTvYkjUCmw4VHxkA9y6OUt4kMEQaJv71W5hw0bDjBeXFJP9izVymm_49jF8qH1AxPkw7An4_Y8VMr09NGSagvin0C2SSM8oC6jTcCNBWAiMzhbTQkHDzm8URpZu8cdt3HWfQ1vtHK9atrDK1M66TaiVbzg22OVYCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iru9yvt5LTeoFvjY_KGkc9lbK-FiVM1d6YHmbJl4Ui5O8BvmJLxENGZM07NDQvQSopAtscKivJ0WeIs0YYEGQ-EVVp5TbY-9sQECZsHhFVbnYmzGqpAEW8tczw2dIsjgJ29wTLnKyCughVdpS2htS6RWGOLKmyFu93lV_GUzRzoMkT1nm53mWycauBcGub7L4kKiQXj7P2ZSt2323vHOuNbk6zJjcHau6AJ_Whrev89a8RyV_3VAR_dP24aQ9NRiBYDdNtO0Wwok2t3RdaBDoDkzjS9lIjshhFcXMd6j7jKjvbmpiaTYENWFEcHcnO89xgW2dy8UUz9UIAzg_T-J_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfRrOHmS1rRF9RS1XD9qDOjiPbkvjct69zCQh5Uoye-eOUTMiQi1Lo7IZK8dNDCZrz_1AhmvyP4GZuRdrcNBaypefAKg85gbOpEQFgq-UgTbTzBQGTmBEX_2QnkwhE1bK69rdgUFHbb0kPYKFx69YY6s4vOtwW4yNs-J5o6r5dIvWuzJBSdRxys_b3LUbjhEWJkJLSB5TDH8w9SeQYXNaF_jKdNycUZ-MsRDj0lqpst2QtlJzM6_aXBxv_JKmPj7UF0KvhV8cGYg11X8_yKn15C9lFjJWqxn9FXm5E0HSjJbJTVlqxshtyZVCEXIhx0adv6QMT887QWnr75XHpfNDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIu0CteAQfg1rT0FOaAJ2EmTI2nJDHbqD46s1lk_NOkTv2fJ1jutMp4nqueunF46GPhRDMCMMRTFIOq66oZb890QmxLFFv25AYRyGI325CCMnqrYvcesFoVvajJDvNNtMNcys2BaPj-TTwFNo_jQX9amIjxT19cXzTnv-YRbLF85p9vGRZlOu-mq0MPnjVd9E8aziSvqQydRZJTbEHiwRTi_9NwF7m9oVKmaANrxtKTuea-KZEw4E03C34YRgLfujLlzlSQVjNSJLFl1E5PGKL5ml64FPxJN1-uISEdbSEqCDyoyb6ooNUOQFxfsBB_2a8ZRms6P9f27Zz6Ezpy94Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=bNNuOP4s8GgGxvZ7ILjwtgQqTb6-Rql4q9ymGSAEx_Y8IZE8HC3V4lj37ZHSfTNmBJToDurt0qp2qPq6RyOkDdJDcZ4nmB5reQvbnJMLA6ez0asupr6De0INP5lL2xdDqIwfXEalb_FE6tjiJXR7C4eoLMRTFR3BePN8uZtUX59vrnVBQE1y-cJs86fhcwINFopRCjOZeMYVWDrEPN1tCe5iWq0ff7qCiETVpIitQOrbI6jGp7TTmE0ehhKr4F9N4UfT1YzEGh02TNVhrq69zZvabmkQ8hd-E-tq5Kg-09b4vcUbbAV6bnHwNgcQkWPVf72JRp8-kpc3ckjld99hcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=bNNuOP4s8GgGxvZ7ILjwtgQqTb6-Rql4q9ymGSAEx_Y8IZE8HC3V4lj37ZHSfTNmBJToDurt0qp2qPq6RyOkDdJDcZ4nmB5reQvbnJMLA6ez0asupr6De0INP5lL2xdDqIwfXEalb_FE6tjiJXR7C4eoLMRTFR3BePN8uZtUX59vrnVBQE1y-cJs86fhcwINFopRCjOZeMYVWDrEPN1tCe5iWq0ff7qCiETVpIitQOrbI6jGp7TTmE0ehhKr4F9N4UfT1YzEGh02TNVhrq69zZvabmkQ8hd-E-tq5Kg-09b4vcUbbAV6bnHwNgcQkWPVf72JRp8-kpc3ckjld99hcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs_h_jtbQP118CvsNKvaSlaeM1PBhFABvaHkMKhV4tY2HvH3RkghmzHRYeifT4DRV7oVpNtBIqd7IMi9XvhvlkFrO6IGpXH44zoMEHRn-i4dYyleYY_fXrYBnHGyqcr9I1t5HPYp75S-V37bSxyvbqASEIpUnzFpd_-JNSAHMl4hnTq2Ho40C85RjWTE7tznZx6kxEvokzFM-HvSwBNdVS2RSTtp4oWC_L95FJ-Pmngk3nwhLyTgogXYMiIoXCoxW6LalZc31_6krFxvIxxSV0dupyTJdkCnf8eV8fyvWIMMN9x4qA_PJFDCxvl3wlNB2kvDQk1VzULdOEihZdzxIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=qe8T3bnaY7yY5TGdRKL-Ih5d452himeWzatrYr5EhD1_ngWH9k0wc0t86GvxA8hobQadAhFxPFClg81L35wpxPTUwyV7RJMEl9fbX2-70e7CGL56t6ndqc5hQmcBSo-jObJC0L-WkJmyC2ydSFZB4-HWW6FyqV5vH0ARmQTx5n5jl6i5ECjgFRoVFFGxQf-X39tK6ihaHp4OUFC2b1W5IyoZKVa1TN_XIVcCEp2PGNmtTPvF7xQH_ZPmeJrw_H0bMaLOkAwpit6OyDToTLMJne_-AvaqkEZl-40rOQCgChXKcmu_z-1ug7jItRN1BZc0EwZlZ66CE4LcOUJqyIjOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=qe8T3bnaY7yY5TGdRKL-Ih5d452himeWzatrYr5EhD1_ngWH9k0wc0t86GvxA8hobQadAhFxPFClg81L35wpxPTUwyV7RJMEl9fbX2-70e7CGL56t6ndqc5hQmcBSo-jObJC0L-WkJmyC2ydSFZB4-HWW6FyqV5vH0ARmQTx5n5jl6i5ECjgFRoVFFGxQf-X39tK6ihaHp4OUFC2b1W5IyoZKVa1TN_XIVcCEp2PGNmtTPvF7xQH_ZPmeJrw_H0bMaLOkAwpit6OyDToTLMJne_-AvaqkEZl-40rOQCgChXKcmu_z-1ug7jItRN1BZc0EwZlZ66CE4LcOUJqyIjOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl4THq4EY67weMKYl5PYebSHWd47dRuq3ybAHi7iqFvTtaeAIJmlQ1TQG5NOM4dWjl8PvhLhYvfGsjSBWFgR-lJE3FpHB0QBZHwfe7gV1CckhkKkE7V1_gGv-eO4qj8TonX3iUE9J3B_IelYpXY3Vr05e9bmWjihgTbxQrAKcOgJt-xo-9vmIftaMl3nLbNyjmfnvIgfz2qnlFxjRmXcqVtrITKLJJApOvxwqFbeo_SqkBPByMoGeYcqTIikXot29-e4sUrAj_lyRYtC3vOMrWysMUI6XBko1mvcP7J7LKN_pE9wsszMq3xHApyB3cNE6aVtZGG_0Xv8P0dsYBKIRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3jrQSLh6bzlmMLuFC-c5SnuO4vtLb6hmFPiMmNKg6-iZ2dzPsQ-0qNTMh5sChoFJdS8Nehe4TxsVSYyhEzwsxgLJsq8Evvfg5A2GNXSKa_ZKHTQVJpUyOBHnEbcSX4e44sMOLbC2WcD1RyWM2ClvHmWOILv9ElVl7ISlwvxsDbx-Ll-VxPG8u4m7h0U93w5ctfm6py6sgWYA9KCAkpQdyHkNezK0KnjY8ZVhdCJFNKCRU2dgy8CppsSxPoBvUGMdZHxAW_ZveJJA3u6PJ5msjcQrrabCIedDrl0sH4vHgtcDuaMojfB8ydGtH7nMrm2PgqMK0cnDkYzknwxrW9Ovg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=dwUAvQZwRNJxKXZfWtaNwJajCSU7uhsyp61Zxjq2p-jsjN5jFaZ2t4EjkkbfWzdko9aXCgCdenqyW8pQbWOS7s8OsrvmlAit5fAw3fxZhiWw7_uzuFN_mwS3Mds4AX-mFhApi1rOoBJbpiYDuUYiNAMhF5BIjb1onUtfaPRKLyL94CsgpglCmkDlcBm77VdbfYz2PNB5CIwwFN3544BiBPK1WtDA30kJ04bb5u6qYAbErlRhdrALCzYFbPta2AWlj63eZTM8ttg_KI24o9PBR1Q_PJh-rabioWarI4eQ0f5RE6ug1MNuGCSQx_W3DXsBQLDLvlVRev-z3E2KozqsJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=dwUAvQZwRNJxKXZfWtaNwJajCSU7uhsyp61Zxjq2p-jsjN5jFaZ2t4EjkkbfWzdko9aXCgCdenqyW8pQbWOS7s8OsrvmlAit5fAw3fxZhiWw7_uzuFN_mwS3Mds4AX-mFhApi1rOoBJbpiYDuUYiNAMhF5BIjb1onUtfaPRKLyL94CsgpglCmkDlcBm77VdbfYz2PNB5CIwwFN3544BiBPK1WtDA30kJ04bb5u6qYAbErlRhdrALCzYFbPta2AWlj63eZTM8ttg_KI24o9PBR1Q_PJh-rabioWarI4eQ0f5RE6ug1MNuGCSQx_W3DXsBQLDLvlVRev-z3E2KozqsJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9h139EwUopcr8sE5puejl_h4NGvCqVC_iWZtTv7AjhyuWwHM5gb8804xVrn7vbiFslLlDIJP5DCv-YQUlrU1reSrLlj6lOKFOka-g06me19zaIARSmJ0maJfNq1G_psp786DaH8CmVZlgjBuxYIHEjx66BsZX3DYA_hCfMInd9h8rOwXfnVQV8K2J-1fA5NVlcUye86E7iKf9OFlyEnBBmBZBNaLnEvce1pW-KKrAGzSP6E5JfEba6NLcss5TMBKtEHWF66c8lE52aGQrqFNi3dHQ1T-zPaGNmo2pN0QrafX_EUubGfMGi0wlS7fDzRd1YHgeKj5qGkqtpRgVeC6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpn70a0gXPYxVooAOdrQNuxinuK-bL-A-zN0ug-fc56F1mh9U1r-rYJc7BT-ztYkweWcGaICfCQcCRNtvitKZ9_o52bZVUBZfN1ySKh7Bc-LS3dttU8-S0esU-wOkHGqZYdphK-PwUdcsMn2XaVap1mLChSwYGAv764vouth7FtjEaKx1IIN9TMoi0WXmzftq4sDFkBZDaPB0Kl8w6ZrIdBWuRU7TCvwYZ4_kJoGbq7ft1lcOR3H9W9cbqvMCSHh9nGQ8uVycH8oSs3gxZgzfmoRBluSSjeSw7sUhgDdud8V0jf-bABIqJpofJK6HS2nOsd18aPNyPEBe-XPSLYGcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=l1bkpIjd2OGxTafUqbMqKMOfVRtrFyhRe4ewZ746y5vMbwNf1I65XIK1PQd9wdw1LBm6vqkO0DbeYlppUsE04-jbG3Rmj_vPu_TlR-16R5OrdhmUD_k3WxwfLbcPB2HoNi62R5E8MZNQcTm7r2TSoz05-37WTcZpN0NIKL-WIn-Vr7B5vQDIciFQ68yp3_1pVJMai1E7Mkyk-A7A1iKBTL8ZrbHskzKQoVKeEmoYCspwu4wcPxc0cw7wIgx5re61pbqHb2_l6B-D1W0iveSpJ3awOmOX_OpJjvid8XDqSppk7Ju_dcGe-4sqHEnoewEHaJ-qKTKjTmpAdVP1iOtwjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=l1bkpIjd2OGxTafUqbMqKMOfVRtrFyhRe4ewZ746y5vMbwNf1I65XIK1PQd9wdw1LBm6vqkO0DbeYlppUsE04-jbG3Rmj_vPu_TlR-16R5OrdhmUD_k3WxwfLbcPB2HoNi62R5E8MZNQcTm7r2TSoz05-37WTcZpN0NIKL-WIn-Vr7B5vQDIciFQ68yp3_1pVJMai1E7Mkyk-A7A1iKBTL8ZrbHskzKQoVKeEmoYCspwu4wcPxc0cw7wIgx5re61pbqHb2_l6B-D1W0iveSpJ3awOmOX_OpJjvid8XDqSppk7Ju_dcGe-4sqHEnoewEHaJ-qKTKjTmpAdVP1iOtwjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N008IH3Yu7q3EyyriqIVkSQl2uTs7gN1zb4562WnFBDMfYqzfgTMZsZRUFE-JJCS6bA4ouMMFM2u6lbqZgf1OaTfYBDMFpswY_Lt4S7sPsNh8Vzs03FLvkRlh5BcC52CAb1iG5vUIXcMexZmFprh-vwBDaZokByHjeyythwRuuzNJGWOfSMqa13iBaI45ak40emcxf33ipnvoIAVqjiFSmDQY6P2TIcuVrPTXMHeEL2Q2yh2uRLxDy_DvdN9sPaRBtCRPx5wT2XvyKzHaTOgcj1J0en6N2_hnG7ron2zXsI242Mmw74IuxzpJH8-4g-rC-34awJy3BbcxORgrYkk5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMZ_b0FYAECEIKyz2ATFilxG1ZEkMd_W9vw3dSVmvTtJZu6qdxYjtjPVthesYgAB6htlsZDcY_vpBagu6M8NR-kEE4zZL8lqPVTzjuy_1rouzwbn2SQjXgZ1cHQ2hU5vmOeMCMHzOR62MmAW3gp_WsRvSwn6hngsZpLFf9hqYwKMoyHl-3kHVkflZF3237fidLvn1IFfmUo4kVYUvwv_zUmff9E9PXcmryakXKGFUWkZ9gMlaTRURFDEqX72ZQVbWd5UJrnKheLP3Lj75ALVJH9SX4oGraOgovyWCkye4h5N4u4LaO11M9f9c2Dt7ZdhRtnEHQFu28Cgs_dDiovTsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLdzg4Ut6SDjpGoDFu-_CGLJoHW4HcsE1GqU6FbWv6Yqvcx-KsTyngZVN6vctV5997Lyp3Xo7PaURFP3lkWB8Is9dAJhuLWMyKzgzN92dm42LctrjOHQjGvVAYW6m_8Qui4zHbu2GgZtX-1DC3_kVAhtB3KdRraSsSnJIcKhOcdyn2xoRqCCOvOrIGH4dVc4r8MAWaw__U0Da8VBUQPjsluBEvxQoIMWIq4ma8PKUuN_hwa-w3LwO0q2vrLdpUWYYctZnXUagGOdkZ-VwP-QLFXrPvD4gog2abAL6v-zoLOUJavTQfjuwKU7piEV1yA6s0D7MAkhAJWPnP3v36eO4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luFWHrvIMjyWHgDHP9s81X3Bg8dS1ZbUGcEuLOtoq5anUJvOi8yXv3BlzAS2aRNhZJcTem2ch_S9Wkd1tJAQFrRREI8Hnyhg1_8zaBj5nLuv3w17M7pAm5awsRlAepI4B-WgETwlOmZSa-dznu06pT2QvjboCEgv7EUCG23LFbNJ2ZBFYkZV6dl4mWWYx_kEAmZx6N1OzBoJcGaYe96FQ5FHVuiZZWcO_pFJg82YvKTD_2kRPIo6m_QnW6pjD_JT8RSQ_1IpbUwZaFwKnu3co4CVng1NF801LzJ_q6_f3psZ3RhmLWSAGnDJWrSmbKNbphEDLMB6jmU0qgcrlXUkYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIpAqWzGm-IN2mPgT8ADvuMMuehX_PMFSwdABQVEYKsLjnqpGZvYA1ZmQGt_ZR6yeUOVXqFVo9seVTiW-UXm2jJdzUSPmcID7x2ZIM_rZRHRv-s1tLQXUvchvrVxwJaaUMCxcuzv5Dul94k7PHXmY8U-fi_QDuT6QSeq_NFG826ZU7CbR94j0l4yY7Fak6IPGTJ34GBfbVU9PCa_QEniEuukRLlnaxaAaox_0-2qDIZSnQd3WSDoejknyCxuchPjw5d8zTaRXYXViyJrZJ0PTeny-3vBvT5Sj_p71ABU9Q1C3UcNQqAnJ1_TygTN-iTlECjs-95dvPFHdSV--M1ptA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE3VsxlPVDfvDJrOICd7dRgvh0osydQO9yqGlDWPNmUiOPzEpbg4yENRp2JiUO-zp4jYvPI_qWkbdxILjiiCH0wnapy4EydPNhwOyBmWpQK_81uWbnOCELC2pQ2Q76HQKlObTLcV7a686_2q285P_9q7fl7A0sjH6eXJQfDOUx2tKs9gm9vLUiGZZ3X4VTUF0yWoR4wSXlzWBMgkCnQ_mu5NGGmixjl6PoI5t5ZW52NcRUmDZBSgKYWebaeP0uNtcBSE6mPETYEd9NiybEd-bGvjEYYZAhit42ADZUUGzRQgTjR96yvxi3ApET7rnt3VdoVdUDxj5USJqv_BlVUYcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7U-2qyg4npS1iATKmQDd8QVUtRCpPgQTA7fHW7ukVS6-Fa38g-Lw3nCsKNRJDaOwAr8Q8AqiOwYD7eMfVxI5XsZvc69CewoY0SN5g-xr8xx5bhs9OVxiDCi9vEU-TClY73hTyPTsEFengG17S5_CUzLary6F5yomQMSFSZvpk87A1A1zmXQHcVfk5epSd_wfaqeelrekUTRecsiDBKN3MT754bFrOT0yn73M1F2uU7W3_Um-zooeC-6og8udVTMkVvOAEc8X8HN64Ytzi9aEDa8prWr3HMPQkDbVjZVWkgOnu4HLfuL-pXVBGM0jIgUEr-G03k4-a1RSov8XCLBBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZOn2dSEq22E8on3whwT5QPK9zwAM0DYDntOtVogekG0u03KPhelbS0uViOVLC0o_baNt5Elh-qfMnunQlXTDeD_bP9CdaKMC0rpG2woXbkrIM4ZOYX-FB6Y8uAur7Bk9R_QMQyi34WiXlRkg3Axr2zxlHrYkRI5hx1qd_bAwSkfo-at3atZfuTnoBL8epRBUj1UBuqo_ndzl_2me7R4TYkfw3By0kIb24caO4mfkpo6FG6TsvZLyi8kx1SzuMixqoRrqWdIuBnYl-kfN_G2kk0L7BBpqXo7NQGwDSBWwQ6i_RwWXldkOUN1k3rJ-73B4bHVXnmv6b968cKPkHnnKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz3B7U6aTNqwBMlvYuHTm8ZRKKiNg8gfBiCXsQuBI6tGtN4CM1iKOtdaphz6Xxt6i6jVylg9TlVcYZBpMWdXH_413uhCJNq774iBbI2oO2XnjoAypzZWSknFRMJw5elHyk30BwGxYlSzw98UzkV437lWcyW2F5exPGZGxY-L780d2PaUuaBCNYZafJrSAoAJfwfSXlqjgCybp2Dqv-vtgqQ4n27-x7hRVEevwY6Oq2rTvGoYmemSGzCAGE_m0Dqp3BsHiSlRVOvT0oAzRk3ahh6PGAtQFNIrGT8XB4jD6KK_P9f0ukIiKy9mBERPeRKt0tSVjm8uOCj3w_bQE-f1xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
