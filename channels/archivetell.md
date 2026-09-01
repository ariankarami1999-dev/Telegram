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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 843 · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=ExPoQ_Vos_oqWlAkPg-FkpWZQmVRcHIiBPB9PkRvGh64jiBTmJjdB8Cc9GVy376ciVG8rL3RFG-2_gLBjvu9SMmySVY3C57Gjn8gRneU60pT3w039Ax1kFuClNU7-iOGhQAIAq3c2rPXLLXhFS17gJGMyJPnxTyvTIeZqpa3FECB1vbSmdn8wdxLnuQ9cGrD7jVf6lF-aNzq_lWbR2HD76jUUWJd8YGQyMOMrgcp_oefxOsCaRA6ekZSJUc72IeS2qlob_oH_7RRsgKfoARfxPJOhZwzXOLXxYL9EJi0RawzL2kFf0ITtSO7HLbvY92v-gTvf64yt5wiiV2BS41LH1Rm-awSr_cwhAwXTGSF9j6fXIWzPGz4FK20oFH8UPq5ze0sD2oik27LX7L19MymIFUWyLv6dOD7H48Bv0SZLEYmoowbgsW9ASbwi1vgy8E-NA6nSAa_szG0_DQ79xG6NJFYowReoBsjfDP1NCyln-fqbtdn2POxyric3IF8qNy6a7nwaXpESZR9Lg3yIuc05ZN7iZIJdYWwfTbfwEcVOccZOux5kVFQaa_xuLAJa3H06Acg-3mBNYfaCqS3nnMphxXe4ZVW_Pq8GvvKJ6PA1EXl4djc-DpiN__DHTbPDIOnYfS7z6ZAS-Ba2uDDaiUj16igI8tFCN9-W2bqa_9qg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=ExPoQ_Vos_oqWlAkPg-FkpWZQmVRcHIiBPB9PkRvGh64jiBTmJjdB8Cc9GVy376ciVG8rL3RFG-2_gLBjvu9SMmySVY3C57Gjn8gRneU60pT3w039Ax1kFuClNU7-iOGhQAIAq3c2rPXLLXhFS17gJGMyJPnxTyvTIeZqpa3FECB1vbSmdn8wdxLnuQ9cGrD7jVf6lF-aNzq_lWbR2HD76jUUWJd8YGQyMOMrgcp_oefxOsCaRA6ekZSJUc72IeS2qlob_oH_7RRsgKfoARfxPJOhZwzXOLXxYL9EJi0RawzL2kFf0ITtSO7HLbvY92v-gTvf64yt5wiiV2BS41LH1Rm-awSr_cwhAwXTGSF9j6fXIWzPGz4FK20oFH8UPq5ze0sD2oik27LX7L19MymIFUWyLv6dOD7H48Bv0SZLEYmoowbgsW9ASbwi1vgy8E-NA6nSAa_szG0_DQ79xG6NJFYowReoBsjfDP1NCyln-fqbtdn2POxyric3IF8qNy6a7nwaXpESZR9Lg3yIuc05ZN7iZIJdYWwfTbfwEcVOccZOux5kVFQaa_xuLAJa3H06Acg-3mBNYfaCqS3nnMphxXe4ZVW_Pq8GvvKJ6PA1EXl4djc-DpiN__DHTbPDIOnYfS7z6ZAS-Ba2uDDaiUj16igI8tFCN9-W2bqa_9qg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD1-ml8wciFlFPuJAaqh45KGJvEqn0gAEsJw_zll1jlLtCHFXes7kNpUv3ULDYNvnzIBr9YlSdse-n1e1V6DCKwIMJ22Cugw9u7P_oIUijKICGMRGQG0cNe20Gjb8xbpehRnCEgRMNEM_LDxQCVj6sMloSMFK3uXVd40D5tlUl0xSvjih18D3E4ShObOh6k0FT8gxcKYIDejiYsOE8ECbaalI3JdfRbxibOmeG-Txi1hSS_OqMVghNsmJ6c6PueSVaBxwT3k2WtdGpDaJmdD-XavTY-_tHx8tUh9Ydt-PNcCe_G8tgQPowXeJnF9qm3NX9_wdesWp-IHteAT7ePxFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bisa0-sYVIB4dA0wdhFP84nvOO50wBMIrXdp1rKVm7gW7TWm6GFBP6ouGkGr9BztM2KhpF_05M_lQ5RjS7s289mid1o90LIWTx7NtYE9kPIhS_MtTw7SC7JGQxkUI5N7JMnVC_YDafu49BrR6Kbr-KebQOwbtN9-I63xMY4fAleS1Hl19P8jg9T-hER_B18HtxHCXH7q0ADk5qI0_Z3bJDr9kaZXA7owrq4-pGUJS2BWjzWwln8i_2S9MM2-K2R96XJB3JJQnVtimUUp0LDOFTqR1n3eaKWFnB-y3xceso-cbsLTcb_KOxJxgu5c-mxlCa5s6jn9n42X5eWtMo3xQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlNw-TWcOOf2sjjxhZBeA01xKREqVAjqZ-x3hA8lBaoxWJE-bu8qJar1Ait8DOngNHg9telALGt2YiH1vxqAEt3JX8-WRDMYwrtyGjVRcoJ3VYx0NDJU2lqlk7zq0iUl2HFJAWQ37aijiHRHUpO6dAVSzAdLvuwkP9iiL3DbLBtc8tT7FXotesjlS44-SuaOXNC6KZyirDYNQpbp6-kRfLL9Jt6bEM4Vjd9Nd2VtlN8tfc1XVOgK6ssD2QGYN5qDx9-F_A-0SPlUQj4By-nXIFAvOc21iEbqioJCKtZNhEJqOmY9cbRaiz8zXoN1rIo6-ty2hllgeOaKOm30DslZQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCt-g8gz_359xalYcupQL7tGUJ-JnxNCBx9SCDCF5Cd3sxzYlDNMDgD0c71WROlomR33T9XIo_iO0szma9GUlxaKLbmCKMIW2gbEY6sFeeI_60CifzADwN4leX5Tt1ZbfgxZeNJXA5SmEnz_KIsWIaCqAGoc2kLz6zLGqJI-bKjvVCUpQ-OBarPdpmP3RrspNHMCHsmHonYXTx--YfbKehKlgPOpGXWjdCkOcGHcivkL3sSkBjRI_6RgCAyHZikm6qrLUI5fnE_pQtGYaDSw6ywty-NQrQAFkZ5kfKe0BLJNy_bzcP5MJd7oncXmlt0E0-2VM41dS_LytyBBG4gRtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKtQjSkuWXP6n6b1v9RE6izu1wTrsrA2XfSam3yclAWDGED33KBHomAqLVEFHeW_SUD1-Dm68gpbgDzsrfAU-Lc_7TRQ8pFn3D1BNrQjECqvsqWm4NYXjIxjEFvz_V-77P1YYCToc9OMqet9nuhzZ5UW3OnrP7DYGXdvyTyiw6xqn38jzXdU2_AXqPJJgy_Av1cG3u0DvMQel7MMw2vXq76aD_rdxJRKp_m5Dm46WlHhCpwzWJJrGciYaLsJ2xE21G3qSVDJp7Zax42FwYVttdkfkA6JnV5Ei-qJFgf59WLawYtTGp5nrqCR1SkFZS2o5LmuiSFzhtnuqFuGseA1ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=qBB4nOZaNptkoEEQv3hLparV3GcMx3kbLFkqZCt-7OAZ_CYKNAjAzFfnzk27F_xUQhGFUVkvAfom9oAA67N0CK-vO7-zsGTwTHu611dh8eVTetzTzE8PS-psa3net48pXPv-yFY6rkp5IuZ1imw5YVGRUpll_z9kxEbLXntKSjeJXMaPoXInXmLYSDuWOgx3wCW98GlDDsCy7b6O5MOHPzIexW7SBr4LsRnJogBtxFhTvHBRrHKdl9M6X8jwMAM3SI9txDxj6IpflB9i9F7-3uB3G2PqwFhSkY7Y1TyKykvTVD_BGuPxMoHa8fSVAEvM6St6fyajx2bpj0pSre3Mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=qBB4nOZaNptkoEEQv3hLparV3GcMx3kbLFkqZCt-7OAZ_CYKNAjAzFfnzk27F_xUQhGFUVkvAfom9oAA67N0CK-vO7-zsGTwTHu611dh8eVTetzTzE8PS-psa3net48pXPv-yFY6rkp5IuZ1imw5YVGRUpll_z9kxEbLXntKSjeJXMaPoXInXmLYSDuWOgx3wCW98GlDDsCy7b6O5MOHPzIexW7SBr4LsRnJogBtxFhTvHBRrHKdl9M6X8jwMAM3SI9txDxj6IpflB9i9F7-3uB3G2PqwFhSkY7Y1TyKykvTVD_BGuPxMoHa8fSVAEvM6St6fyajx2bpj0pSre3Mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQB7bEl_B4GQm7MNPcajeymxHTkmcbhjwMcJsm020Fq6Z1yGvsg-IyaXB-7rxXO-zvvaNByVC8SUHu_BHXl437Nv0GipptGqEdcbcf47TRmaV1pfmy4HDUTsDnCd15-8ASM6DHWiv-r6OfMjGNw7wRKxmbrew6Z5-ovRfDGIX5q9avVzle_ISE01_Fm7BUQjjUGAb51WHaGBrfhqoG1keLsrARBw25kdl3r-t445QXbNFdjYJqPSRgYbKHWzFvBlauwczjIizG949STCVVTSGWQTmH9clu36iGM4i3-SWPTjnVwIDWiPZed8eFpo5lJXrGDdmsY24aQT61XoeWUkxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoaRsByaiGFlcTaoKV5hOcgEBVbHG_5eIYQ7bTkS34SDa7XljvRCLUMi3g7vk6dAUKjseF3heTiCJt7AvYBI1mFbAoSstvvCoI1R5CB5l-VDQPHplFSp6_WQJfgbv97bS7Tt8h4AFtZh3EBiL-hHIhaWAW1poKSEohk6R_mB6Qhf6GV18ve1ymRwMIIczShbhNKuqWMtZeQrI0MVEjjnOZsN7punyPy7u7YDA3LJ6gtIUSwBR1M6WQ1Fo3X4qjMwU_dILZ-1sew2BUxZ2jceebe5UCWnIchUDDkZOp2vO2-UqkHSNDdbMy7XsiT05G8-g7c6IP1Id7CLA0sK9NcNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzMJZWUFzeMVk8BylI3SEqNmhMZ72VGM_MT8_D1pFdFw5WMvub68sfysi_RmTwpXSlfZJGH65s-ioJvqkwbqofAnMMuwunTt670jfauE0PEkva-LmwRv_DzxtX1tOd928OJtyBtvMLP9afXYM4upX-7_KTXePdcmqxh4kkDo-WMjTk1-cgSAttrqMykIERPnD88rNGz-r8n6-GU-Rf2pOwMmRT5EeMVGvMCs1pDMKmOL_iOP3BXkfc9Ma79ueu-FJgVAIXZMtqgsTDoFj7OjYDQvvnNKDRdV95UjTCcy6yvLAFPX7ndcFAy2Oy9c-hm9P3OcVIbWFv3FoQemrumzHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEfOYqxYi1vWbPMd_MLdkKc7hPFPsNcIqBAE0AsSIeuk0sq-6PXbSeDjOU0Cu-tFkIqglyGiavx1UFq6VDnb5DfHXb3yPFFbmFJ806D5A9IpoY7yol0YoJ5rd2fNYsFQ8z28eo-SLnk33XQU625QmYxGBKBOuPYEyVEL9WUZzsa1e0UCHwkmye0ZpJOFdcMpnuaAHW3wSwyzRITpflUKrGyM_ugSMQJEo_NX0XOgdZbad6tFtoo-W9ISHCY8u3ZJIFa2Lg5tkVZoVJQLChCpRk2Dpd68NI6LamobWy7ukrMiyOxozQ2NZ3oq0NdJ0BGMGW6mk_vrhzjpoV_OtKCfdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT3ufA1U2sqML4cobo8Kixm3VilSORHgrqzMxw60KWiG2UHM_gmCeVM066t0Q_nr7p_zMYSulyFUEhZMuntjRerg9AXGv-JUxQ6TT83VX1k3qeQcmTgdgYBkU84pYBsOSeBK9KbWu7LCnfqfQD6H7wUDDf2veAQa18zJDTnpsbGaF0g9d5SIVsp0X5MykCaNNbivB6PocPBtbUC-8ax-yw9GsUGXDSC4inWIYWEJwdP_srzWq-xbXs2RnsOn_DFm7nOfecrx70_8bzUD8ofBfAvyZ-1Ysm2VgVkgLZFgrtZvyMyDbg5EAUodglsHXcxsSq8VDfq9cqmgAHqdGi9aaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4dtyVCO6dh8HxUsgyhuRwVrc9z4moxaEdh1V0Uh7cgwiN22VRufWRvV3j8s5iN0P4z_UaiqP0Y6pZ4kisY5m3qS-d0SnG4rh8D5bT0rj4F5dmISAi07h-TFDCjpFVFmeHeGuNHCDKLdlpuqyjF8lqjBBD8eE8jfSCNvykmVXHU0OMjjnhOU2BQyKbO30MjigUxj5Y7rE2IPCSjNj35Y1Vd807Tif6Gy7-l_UHEDHBop4zMDI-qXCn2I1clfE1MhEbjBvfuy6mnooWhvD4GQg3JHF9H9eaKBfTUZaQ5BHybNOEofeCSqCKtdR5caFS1ayzJd6lX-Qz7GutrhFHdAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzvBtIQ4_NtutNqsRZ5rb1pW34WTTWC-qTGZsXFyTF1KF_3dDZ5E1KRjrBTgoDuDkuPFzCtLTKiL6SCUPDrs2pBgnxfaDTHYFbP6sSEIATFHQIjq5Y4cSifMnmgG20iUZaXjfus85QMLefgBRMcLIdWcy87m3b5AAjJGgbO7aBC1yafQG_qSK3Sj9xTB3q51lFL2sOrwsR0ZmUtzddroi4v-EcDoxqBujI-jcXMCoueGHISysVzlCHbbZw6gt3mEsnodpsHCnDk3aeXZO1s68ZdYQiklBJJSm40OtLNXLeT_Dl4-Fd5auohVYf885CANI-IzV5YJ0vOJpdyl-Mjc-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=V6RN7D7BHGjDEPHvR22mjHrghJwXYNpQON5HtPkSy4UPVoe8Vn1Dnx0PUWY2C7sytdV73gOmWgCxGnJoP4USv8N_SMprClaw7-3ZhZ4eBdqpi_DSJflFDLe1jEu0BCy2De9uo1glXZ1aJzihApIeXCCQ8QF-8L7ecorCdpeq7K5cIzhhVAZQVtgBnxppLkuByc7g_EfXX4_dlUnu06bcrHWNAsgT-HIDG57VpDz59LZY6pAtySpyjR5rXoxiQNTxjtgqq0mFIqU-wYVEkAN4YGk3aLxZbhbfkRZ8iSvM5BoK9fzXk9Ey9JiCZ1llFYVZg2nqLNYl9dCC6ptxR7rDxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=V6RN7D7BHGjDEPHvR22mjHrghJwXYNpQON5HtPkSy4UPVoe8Vn1Dnx0PUWY2C7sytdV73gOmWgCxGnJoP4USv8N_SMprClaw7-3ZhZ4eBdqpi_DSJflFDLe1jEu0BCy2De9uo1glXZ1aJzihApIeXCCQ8QF-8L7ecorCdpeq7K5cIzhhVAZQVtgBnxppLkuByc7g_EfXX4_dlUnu06bcrHWNAsgT-HIDG57VpDz59LZY6pAtySpyjR5rXoxiQNTxjtgqq0mFIqU-wYVEkAN4YGk3aLxZbhbfkRZ8iSvM5BoK9fzXk9Ey9JiCZ1llFYVZg2nqLNYl9dCC6ptxR7rDxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiRhKkMgUtYOEWCV5taOurh65rtZN67kuVaTw02V4joUoHrLczfVFmM6UquVLGaMQrzgFd7kzRn5-ZdQPRTgnf9J0gcrM5eJzEEaQr-RUdWHx6K8022QlVwf2lxN6NAP1GVddtRtxmabVkcJMYFj2Wcfe7H9MsvqbGrv_5PO4jx8yuqC2HlDpnyg0ByM2mKanu0NZng6Vo9UhYidiEaogJGla2LtjD7bIhmFexpoOxUQG_VOYv8yinPlDpxNyxOL7NPj5XOytD3xBuXYi0O7Z4Rxf7n_f3LZYt0y0jh1GzbI1uQTyDVi3qZCrPCvhvCHLH66IabdyciW0Vvp2R2gpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poaeB_dQswccSoQ0eZ8oJmfaJrYU3ZSrnPk7g5dJh1IJOEb-jV22wnahyhJ_NHT2IKn_aDVUKEFu7uXxjv94RxWxGZE1hG2YzGGsDlS4CLGnqJRWL1QlzT1PO-hUjsBdB_SO3ZcsxVHbZQp8-iMpldOvUC_NUx00zNzuIwJeMyWUIoND-lTleFC-bNgwvD6byu1DLhbjnKuUJ5u3YL0IRpKSQxmuzdMh4TpQyAckvKV-8XpBZ4b8MPQr18SzhdTcPLmpTWKXBdtDQvpajgvMiYBSMlJH8s3ddkWfClBTqDh0gEbiRCcMqEoyGI0IoJ-p5pkvPNww4y31Fjsw7JMy4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwcIqLb5W0oRd10rM4hHwBGEc2x5aVHVIgZgNKrKJZLsqN3sPhQMHOln3ufAFoOiXbipAzwnlRn-39Wyvkaw-LELCK6mYkqjnUp5Vqi447tRvXiTw3hPJBJilsvS32EYaVxjQ13jgle7u9xbHk2NiIqjB7vs7582hauZ7q4YKL8OgyGyq8yPKQg_HDTPJC7rx97NhZ_m_wH9_zKuGTYn8XifYzh7KwWjwf7wzqaQoC22n1bkh5CC4lF_aGhOHf4Jrg6a24ceo9J7F2b4UOy2s-9ayxMTuwy_ah2F_r-aHLBG1uPMZn3hXTIOC30NQJJg5GE0VAFujOaV9qUcK3qqLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tleROYbe2etB1LARjQMVMvXU49KtlR35EjuaIsa6EI40gDEnRtgw4b2l2oU7r2y9TxSnB_ZjB3hvNbAshkxQkWxeUzwsyzqSe64mEnqOc4IN-TN8QWNL0_uU9zbX7d1stPRO9HoOAFnbG69AxBWYYhbhjWH6kRJWMKojTFxdJP-AHNc0CN4Vqkb8E8xOkJIehWrSiMIUhRXxCJJUuBOYoOUukoaK7ACa6nLegDDGqEHbevEYkKGd00ht0xBiVpFDnuW22fnVIP-7dzUM3rzbLUgnstRattIp9ngTdVY5Qdyughd3gAtJqXSz5poF5hq8CJTvagjvNoWgB__XZsO5uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=T7Y51T-1EdrJBnQ0o5Y7yn8cPSB4hofUOYEWnhw0eba3tMIwtjhcQ5_vhasLdUKphj5rCDSkUv8eEuL2XYzNWrG6xTgQnLjSnpgcdYUNl32tfwV0B0r3Dr8X6xMVHbu0911PZu7uYuHAfXqbuONaV1j6t7M7rdF2L-ELOHBK13vXN3CaQRJuromlYO3TBSqx-Sxa-w7ADc1XjfDNtLYX7VQRXpCXF7zt_6t9cIpPuml3OnNBgjhSEhdbahq-QpuhVe03ERlt0lmXSBFif2vbs7ubSZlM0guSdqpeLme_WQEQBkiMdJL95kYjGtL9_CoKn4-dLT4-scKnZslxYI_8VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=T7Y51T-1EdrJBnQ0o5Y7yn8cPSB4hofUOYEWnhw0eba3tMIwtjhcQ5_vhasLdUKphj5rCDSkUv8eEuL2XYzNWrG6xTgQnLjSnpgcdYUNl32tfwV0B0r3Dr8X6xMVHbu0911PZu7uYuHAfXqbuONaV1j6t7M7rdF2L-ELOHBK13vXN3CaQRJuromlYO3TBSqx-Sxa-w7ADc1XjfDNtLYX7VQRXpCXF7zt_6t9cIpPuml3OnNBgjhSEhdbahq-QpuhVe03ERlt0lmXSBFif2vbs7ubSZlM0guSdqpeLme_WQEQBkiMdJL95kYjGtL9_CoKn4-dLT4-scKnZslxYI_8VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prf8miC2CUn-BmJjHXGcmxW3-w0vuMWoiIpxF4T7yKV0T9Kj9qR5QJKNn9HmEUQmYq3L7ZED_f8RkhifRHQQccOFzE0w8f4VAyilyDyPn28S1_LJcKaztu-JWJCCY_JN3VtQ7RjxxD_29ixm33jdyHDvg-q-NoOWJc9HpRg8jbT2mH0V4ReyDkoX6uiUdpKUafRLmU1MNSxbPJkLFx627a1m-Z6m8ilUUArQf_zSh4Z5kxs2YLDinw_d4sLO8-TIPxusq5EykDywfVH8bCEqbFpwz3bA_uRFbcC4M-tX2epEXV0-pQAkhwgUGldYJpu4q32nMplkkoi-TWBnenwCKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=tYkWYnOPtkUP04KEL5aCsT8BF31TnTmHtzBlcPCOhfgAvfStykmaEw4Ra4vZEz3xAKPjCFBPmUElPKSXPgtlE_eapi_FcZM5hbfJ1nFIwdRx4QoX-7_QDIPYJUCHBHa0E36uhUS6quA1XUaWGMLxBpGiixjJ7QoAz4h4GriVLlqNlytqdv2E0t93VDjqf7iyfDcd6zjvp7x-pgs-KzfUyrYy9H-BAadONlDuq8ZmTuEN7dsbUDBmNrqSauPCupBR_hPuJ3rGW-h_isOzaeKzfraIbSVphOg6nR6wrMcBHRfypvx-P0pMQ2JCbOvP9Y24miAR5n9QTLU1aNRXM0EiTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=tYkWYnOPtkUP04KEL5aCsT8BF31TnTmHtzBlcPCOhfgAvfStykmaEw4Ra4vZEz3xAKPjCFBPmUElPKSXPgtlE_eapi_FcZM5hbfJ1nFIwdRx4QoX-7_QDIPYJUCHBHa0E36uhUS6quA1XUaWGMLxBpGiixjJ7QoAz4h4GriVLlqNlytqdv2E0t93VDjqf7iyfDcd6zjvp7x-pgs-KzfUyrYy9H-BAadONlDuq8ZmTuEN7dsbUDBmNrqSauPCupBR_hPuJ3rGW-h_isOzaeKzfraIbSVphOg6nR6wrMcBHRfypvx-P0pMQ2JCbOvP9Y24miAR5n9QTLU1aNRXM0EiTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgpfUT8egHA63E2eOdGz2E6ABG8NWJ5vowK60nj2snbuMEqwXSkkstyPuU_tgF2Fxk0CGfUIdo8GylAg3uv9iKGnc_DU42i7gg4HlhAvOf65je3z37tbJVtpdRcBumlvJYcdi2DlavVw_zjs5VkHfdXxgx-RNX5EEMAUJaD9Bvss813FiyHUt9cVTboweZnqODXZ9y6Z-kY9Z8b5oc5NZTGFQPk1kdbQKhXN45BD2cxUwJh-Td8kVINFl0nVjRtYLA2azyPazscbUxMsnjUKXhA-xqLkf4YKaU0gAmPAgrV5EmJ-LW3OKq7T2RHAIs71_pQ398wB6E2Q4FcbWDlvBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knh9HiEu4ykgtldJupCOkAB5QDoyxEhJCFVw4hR2mklby-2uHQlUYD_Vmhw4XCHo75C0K2cHGoRHxnrMK7GGkHtmeJ6DrYHr_MKMtk1A-7fG8W1CFHOY6BdzZ1YDpUk1ROAcQQHrsP1hsz1FUmATxxBFe54v5bq5nhAQZcO_xEFqVjy135KXN8C6wuCbs_xL-k5kqGCUXPP-bjlGZsacOAMDVn74cASB0YjsJZ25LSxU2ajefiaRt3_8SWym5mMMmX3NrO8HWcUngYteHL3Cu2HkV4XYR4ryr4i9ctLuDxoNZ76o_yam7OIC_0Dom_q7sQFO-TYqga6QB50B7_RrKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=v50Yr9RdwrHjbvpnLxucWHK33hlNpq9yK8m_q5mUQMH4R-Hh337IBSMwh3snN66C197VpynyC7liJSyvT3fKNfmqYYlcUOM_IDiLDIWIfw3eJSFQarfUAaRz7NBr6mq3EdIEAaiYDQCwyp1JHNXrGbPr8noQ5rlqZ9GQtvDcNaFsBesuXZG_Lyfa2j85NT0dj0auoeK-da7N69zOphiOTqAkrKSbhOXtx9hNuT-4VVYZs4BppdT7lXaOkVwitHQ5ygV6bbb62TraACsrh3Jba_OqW_nYoVRu-YcMi7CaeSFgxev7UlC_ZQVNrV4ATQtDlVx2UwppDHAeu1IpVGcMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=v50Yr9RdwrHjbvpnLxucWHK33hlNpq9yK8m_q5mUQMH4R-Hh337IBSMwh3snN66C197VpynyC7liJSyvT3fKNfmqYYlcUOM_IDiLDIWIfw3eJSFQarfUAaRz7NBr6mq3EdIEAaiYDQCwyp1JHNXrGbPr8noQ5rlqZ9GQtvDcNaFsBesuXZG_Lyfa2j85NT0dj0auoeK-da7N69zOphiOTqAkrKSbhOXtx9hNuT-4VVYZs4BppdT7lXaOkVwitHQ5ygV6bbb62TraACsrh3Jba_OqW_nYoVRu-YcMi7CaeSFgxev7UlC_ZQVNrV4ATQtDlVx2UwppDHAeu1IpVGcMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzmil0DWcXPV2Zu-ht-mYalri8YVk2oTtPyrqXaG7r_SdGgn24VYL6iih9_lpI7kAKInrlVqd6hsdAIvfUEzP94V0IfzX9JMCqVc_XOhMzVF7l1bcDhMfex2ruM8-nJkgDuyQNsufP4FX0JOnIZ-6KA2aGBnlBmttPqnfh7svky85z5P5ewoOAwVdxDKLn6P7NCvIo7DVQp8tlDd7Hslnyi90OsGSkxTjrl3g07R2PzP90cok79AG1nZ9haywQY1kzCqB8-Jxce9sE5cYU_7vs6Kwfjwpx1LSX7eMsPnVYFLiPDhcxPBUK1sf_MWJZVcdojhcTVR4y7oAVCzh91Zug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAd1C98aEeu9Co-xHECeaiE0Q_uqLfPaCDTjJO_3yztiAMoa7u4VRznt6zezdn13FvxeritUgG6ns_-iT67MWsP-7rOwDr6UMKsT0jqa5CvSE40XVag65kMnp0Cqr0QisgZJiqFNcGewmo6LKkCFID778cKrArSwUQbqlUqD6x0i8RFGBqlHTCVy1ekBuhtvTF18F1Zb87ScWRp0fSxRzCVrZUs-9XEnitFfYr5r4jM4vr2Zbf0dZE5HBufz-EGxz_TEq3xUXaHZjLT-tiYH4lCVC0hYgHsAHfemSY8udgCTPraWofpAU6hQ4ZP5XhS7Ly3pCNplRX3QgE26bFqUXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Sabb8SOR7DR0Jkft1WYj_dXJsFENyxKp9u4_wj29d4dRZm_NZtaGWsuvjGexl-zEedXjqkH2PnWRliBSJKeOMegAMDyEK6jIPqDT8o54jGmulesdRmVDMStKVwRQWG5cOMcplP6D3R27GLTOF3_hZ_SMvQe_L6pkghRsJGL78jQR_cVVtMTLrSA1WZy8B_xsDV82UpU_wHZq0pp3IdyS74woqD5iT2Bcw_baHO5qtCV3FPB1KyaztyvnBdgmRIORmkcfU3FDslcCEf1qsej4I1MPI2w2E-z0xOAHw7x_rsB9hyHQWhTPGE3VArGBHRYW3KpM4Hgn586aEAzDLcsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEAbTwdnwubOi-Z4agIZqf2Meon3Rma3np0AKfWoSs0bLeTYp1N4sqJcAvrNJsSNMC1NmxzpU-qbgbey47d6D_ONnEdzwGxel9RMYIM2as74WFWcE9g-J_deZXIfZMLTTX72H4wMExy-0aj0y3DUo3YvJrUCHuhfBYwmEeyXC7vDWR2yWsriaVsRjIuFx_qMKmUeez1MlR3NtcfnkttXPNnQpfkiEgIT5Ro23CRHm0Y_RniL4uW3AQwKuBT0kc6pihZ0TI7aAjBuLfx48fBSXiQhIqG_6BTS2_2o-6udKsXdgRbaS1hk-rf52zLqnHcXuU9Yyvwn08BiwXd5KpmlEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGVNk4gLo3JY45GN6eGCPxdzZAMaOXSk-eg0bSv_oOAT5WOQMTeB82nHwoA6SYqkoIk5xfxAp9JTkoMPxJBod4nmsAnW_nECDrBmaSUXhsLt-Zk-VriQH568tRBaKekg2R9U51ZMX85mbZg8ahs1vgu7xFBTS_Z4I6QxvRhLwEtwPT3wa5SbmSrQuRdbmrZOLwsZ2gMqIUIiklykZnGWeZ-OCKn6z3amEV6KDPgZxYhJh-de5oaTW9yb6IbjgI6EuJ8gIjMl8Y1jjhgnIBIqc6HnKvL8cpQIFxuRwwkJKz3CFTbVDh6yqKpv2HfveSFwi2Q-1MnL8ezIqO-mUULq-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obea2-K5zwMFz8twR4AavVjqP4Lh5p-VVsAQVuMxzmP79n-FbeP1Dj2qDTmX_tAECnIOWT93aXQUeUJt6qxa7tlNsm4ECX4eMHY4ac7CfBUdjY91qeUheywRXPdqcY3iV9S1TQIVEDQ_vUXAmjCrsceKl7YoW0GkIqSHjPC7lcs1GfGp-9e_3vKyV3-mjRGE7Fk5he7W_4R8gjaM-a6qjUcDII3nX_H1h4HX9C4iPph2m7gK7P9D0b5lznOn0_xk7_35hsaK2VbhzR0zLUC9xc7iz9cg0DW46YnanGj_goody-37PwNofIkcSnjU9SxkPES8p59Frs0YvIHunk-57A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6cEa_bYwbtUoi4Noz5ozZt_fcuyMcJ-nALIM8S2sshwXy43AqvXthUh1MAHMacQ88hY3v2OYzIpn4NTLHSrx10Q_mzA9gh2ogI8RcCk4eRpbO5vX0qrBSXy6VjCe-15cZiTlpKuWeJfgacZakpHqeEJT4pKiVOTQOszimdFZjcewKb5TXB27xQ1-dZhRGLKnfpnRabYZ7o_MT_TmGrWNs882rh6CgNOgNbdPV31E927nGVz_IRWZ_vdnqEfTEXIQSU5rWYh2mpPVtUc10zTogMMLV3wkjsP83qLTJkaXxCBF8QRkEVo7vFD8P2hPqoNE04kDm00obeJ3VeaFKtp1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o15fU0E1XCcA3XkVlTClZBe6S1hVBVfXdXqKtFbnVrka6GlfCMVT_tEwbPHlh0_rTKVrStwKr1AmvBXI6EaIG7XZKFlrjZWWcFlW2lB4JTv5ljhCszZFixTZ9R-uRZajNSu-Q5ql64Gee0iF0dDwbS978MCZzPHNQSmVrSs8Qomb6w-ghhh8M6rrBnReO64S02x_6TvslST0vqOKkWO0Tb7fZtpaI1pJYqYXkONIcXCjVQpHkrvPiBN6LJdqWGHyS_UWEDSZsrHVBuMniqSh4KIFgQz7EgoHj_UHu6NjLm8rlwEvli_n47uR6rRDDzfvxB7qxV7vd1tHJANItSjJjg.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
