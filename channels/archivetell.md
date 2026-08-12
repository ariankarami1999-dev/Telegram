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
<img src="https://cdn4.telesco.pe/file/vGktQLHAx5-aIAvDGNjqkVAma15oxs4OSBFeLNVqOxZpAkMjghUjdppyIalMUSEtZB42WtfVQjFApdTuKtmY5_xeoQucX-2VSgcuMGtnG-LSwgFb4bLGmIdSrWLuZZIUec3NX6r0nfdUaX5eyt8c2PIJQ0MLNUVrh0jpqp2LeewUjyksvNdTR4JxLmTknLTCuH58qIehc3pHVDg2ZIrV5Kl7T50uoJh9Z4HTX5DD_W3Sb1kj6czdZSDpn9B5saElFAfKIwmXkodliYOBGUO5q7QQERrBOP8L1OFPM9nALEH_BdWzKmhu2kFO0i-DkkC5gKUD-2yL7k0wSwo6rpgMUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 13:06:38</div>
<hr>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 180 · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO5jNfindPVPdK4SZaAVjBcUEu3H8BoKpD3TJm_iuVxSvXyhLQFv7gKEgFofEQUPJa51TnRkhG3r7r3gPlpK04g-v9PVVC3caoKPtfP4VSrdsceeij5vdQU1HNTLwxlpIk3LNbmb1xdIcshRJaRq_m6qvX1PPHhTc3KdbzS3xw8bOQCvMfx4C1cy8hIUFhGnjbKKm5SotAi8KlpTUEQKzzpZjdVRQXn3ma0jYqUZdwUy0ykfCO9AgnZEOdZ5xPF9IbFpQUFVtBhCktDuQtUMduPwoDAZoyIs4lboSXtRHR7-7ZeORR0gUac5E1eLiBxtQUWEPNmOehoO-3A7obDVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
نتینو | مرجع خرید اکانت‌های پریمیوم و سرویس‌های هوش مصنوعی
🔥
دنبال اکانت اورجینال، فعال‌سازی مطمئن و قیمت مناسب هستی؟
در نتینو می‌تونی محبوب‌ترین سرویس‌های پریمیوم رو با تحویل سریع، پشتیبانی واقعی و قیمت رقابتی تهیه کنی.
✅
ChatGPT Plus
✅
ChatGPT Go
✅
Claude Pro
✅
Gemini Pro
✅
Gemini Lite
✅
Apple ID
✅
Telegram Premium
✅
YouTube Premium
✅
Canva Pro
✅
CapCut Pro
✅
Spotify Premium
✅
Netflix
✅
VPN و ده‌ها سرویس محبوب دیگر
﻿
━━━━━━━━━━━━━━━━━━━━━━
💎
چرا نتینو؟
⚡
تحویل سریع سفارش
🔐
فعال‌سازی روی جیمیل شخصی برای سرویس‌های قابل فعال‌سازی
💯
تضمین کیفیت محصولات
🛡
گارانتی محصولات منتخب
💬
پشتیبانی واقعی قبل و بعد از خرید
💳
پرداخت آسان و امن
🎁
تخفیف‌ها و جشنواره‌های ویژه
🛍
تنوع بالای محصولات دیجیتال
🥇
دارای نماد اعتماد الکترونیکی
━━━━━━━━━━━━━━━━━━━━━━
🎯
مناسب برای
👨‍💻
برنامه‌نویسان
🧑‍🎓
دانشجویان
📚
معلمان
🎥
بلاگرها
📱
تولیدکنندگان محتوا
💼
فریلنسرها
🤖
علاقه‌مندان به هوش مصنوعی
🎨
طراحان و ادیتورها
━━━━━━━━━━━━━━━━━━━━━━
🎁
تخفیف ویژه فقط برای ۵۰ خرید اول
هنگام خرید از سایت، کد زیر را وارد کن:
🎟
کد تخفیف:
TELE100
🔥
با این کد، محصولات منتخب را با قیمت ویژه و زیر قیمت بازار ایران تهیه کن.
⚠️
ظرفیت استفاده محدود است و پس از تکمیل ۵۰ خرید، کد غیرفعال می‌شود.
━━━━━━━━━━━━━━━━━━━━━━
🖥
خرید مستقیم از سایت:
https://netinomarket.ir
🤖
ربات فروشگاه:
@Netinokhadmat_bot
💬
کانال مجموعه :
@Netino_Service
✨
نتینو
؛ کیفیت بالا، قیمت مناسب، تحویل سریع و پشتیبانی حرفه‌ای
👆
همین حالا وارد سایت یا ربات شو و قبل از تکمیل ظرفیت خریدت رو ثبت کن.</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7462" target="_blank">📅 22:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7461" target="_blank">📅 22:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9910KMnxLCkSjaVJ3PV_NI8NapwPHK8lJEwyGBpYMjlMxic96lIaLG9qWb6POhYhFMtKlA1tbdrlLxu6jCS-IPD86AJ5ZNl7YpYJRrR4eFIyfGsdJsfzwwu5Gsfl21L-MPcHdi2PAmhRVC9tz_sK0QbXHUxZpXQUU5MNuV-72VVggG16NcD_hE0LJ9cGIJuG5N1ICxv60CbS-mdUfgEkdwSruJlfqLFZbfB_3K_iF3UTAN6ZEDm4iV4EJ6NA8H-CC4mSqa_Kllw-_fF9D6S1W4Q2X2lfhzZdTyl0HILXQM9GoIQT-JkovGEtYroeYM_ofCcLY9R9n1TeqA2yE08Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlb4AHjpMCXyf-OVLwnE2SPGDOK_Xnbz6G-ifVFGfI0h3kqi34H_oJV7KVhGdiBv2aqKLPbntgSnUgkN_aDj1mcq2bYl1EiGNIuGbbu83G2bt5apV3KH2pjnimVOFo264r1IRebFNkMIYRrNp6d_1DbHWl4W-YgEniAo5kEj5FANE74MCmkqwPBemEE_P1_beAhs7HRO0B_w9fy5ZMCmo0N-dI4IcD0xarNk7TR9aVuk0d7RD1N7P09lwhee3JdyiTgzrIjT0Vp1_Abzgr9wPnqV5Jui2_ttZVRaxsyrMBqG4vZvUcs46B1YnlD-UXek7fQ0L4MV83BpBZpVyN-5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYq8Ndm2kg9bJcxMsSnjf9-KhnwELLIvOPppMA7hwOIpc5vf6k_MsbXjz8YgeCi1PzMo_Z4HBdkKe0AE94YTGm6lQIC7_2xfVjTjGW2DWu-CwEjbfF7kgm02tktDAKAP0g05JFjhhiTwqX2vxGyGeIuGK-Tx5A5hwIPSXkYnRygqd-L_Yi2CkH0pV4_uL2uzltjH9MxPM86GBfjZkGnej9y-yRS_g5vxUOKhN70ffDqV1jhcX2hmimBYo74pmmKuUbPZ-EMadMpYcf3GeEhVGp0lvqOcQmO6URO6Q0LWdoB4lrE_dzZak9fdXbxGswXr-O4duwBin-Vz5_pU7cL4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7456" target="_blank">📅 10:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU3bZDeOrrCmbCge8dp6tj3u3tmWMXjroVydIJ-0hENhn5sehDzSaTilrovILMRvC5xTIMYtpfC5ldwEIPFHMtevYU9BXQvkGc_8iQCgJu4T1wwdVJSESmJTx1yKjRI9zLak8L9Y7QQZJPHm1nV1BVX_CYqeD1UP31Xwy_c0WQUu7d7QHV871u_lWEqwT-qCIfdn504YuCAn9PYf5nUfCO0DvR3UPJsfhCLUAgEyL7Z7_x7XaVluSDabAyW1643OzcQ-fmjfLVbh6HJL14-qeTWevWwH_4BvtGq-XGqOfDAKHXa7yEROehZl3hVXIzXlthCNTLOlrC2G6Po1FqrmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH-VqIondvK-QIfzs0v1arxuz3_9cEXkx12CvHUxZzbiAN9ZlsEUanGn69ap2qAyfjLnprZRfGOlZ4rx8qy6d-HyvTYGgD5fpkKsBFPDeVNvnsrJuIHw68yt0U4OgeJg2AgUaSVR3b4L9EAmw1jqSWU0yR_BaJK7gpD1ooer94KaX99a5WVjd_A5gTpgQyW5P-nr1qyFywf4Ads3m5UKgDpQRUl1Wd-kKLafnFTRF2doAxpLg6g0ump6ILIPhgla6hjgEyP6P9qmIdTw6qTTyg9BeoQU4Rxp9zkyUAfYoXLVwDM5FdHl9RWTYvZSjpl9gRoWGMg7UY2EbeywUjr0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpnV3Q-zCyABhHAgGx4PGHgbZErtBKApGkCyVbLyCYUM0_61T3n_vmN2FIZz1Ip58rs_WuilrwpxV7eNbNgfuhCjFOwNiH8Nt3Ls-gubdF-RpT_pyxvwwxQNGinoZYZtldTVZ47EDvfvpFKOt_Q1bHJ-kNAiq5eDKpdWVXYsGi9_jHProgzMJh148sdeDTw508RVcZa_HOUegzI-QlB_EnYOc1D5KbIsm_fKoqNf4sX07ep-9IkSgtGnbC8ANLxZOhIl8T2_9RMnCTpev0gvD1Ej-I7e4PGRPpUarpZIQquWC0MjvVRrAfuWlXywfiUXnH4nAnIx9heX2vJDK2QMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7451" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVaUaULxwdCeOYToDdLQJ617Z5IyuzPU3vj_JVRz-ktVF_AK_s1n8_EuTA8MMJ3UOaW-4bGbjk91jzdrLLWKQvV0D4aqSId5kqEwJ0alEfKUmxMC_jUs_8FISmWIasrUCz7fzlykSk5jEEOPmFT0LXKXJ-ecQJjnJJzY7blfCgnuzWHxJtlcNmCn1HfM5po9UYvotn4rNaxqTaj2GvTjuMKkMqEOg4ViL03PMcyrLxvxcTw0nQAsywotjiT_tusv2kl7RvMCOkdjdJp31L2tMYiVC08dohRyuGy9ZsW0Uzj0qeypO5VAlJfBJE9Jj2Ekr5ALggKvcGZ1x48ZqNtcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iioUUDgjePwpBAkRf3tNoQGmvKMRP60rgrNwyMoSRuI5iNupwtOI49Om7ScQGR1wHCMy1uOi7_qwvYmWhpiOL9065ZXN1hPywQx_fib9HP0gMMYCVb3UUG8AERAV2UxX2Br4cizQV69Ej6_O0yoZIcNvuvs1hBJ2Ti5YVOWpuEi8HDzUT31MczrLprFUnuor9tShPlldggXgOPgkkWXOscJhkR_2sMM_FmVe4RA49NjKuc8n8F_Mse96nVVKCZmi9g1weq-EI3c2GV2saSIhQ2FElIDiKztlmQLyH7dD7KY-aRlYKdnfAjKRisBA-igzVsgytA3EFv9ODZm52QGDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbm9vBmVls4fuDVP6v-wR90Nl5w2ULSLYJ7fgl3gFJw-9ksGAel91GVjdPAYSQGzovz7_7m-fZATVqA5JRGuYvWpTkYD0Yf55GUSMJzH0ooYeBBsJDSDeOl-aJBpaZ1Q8542i8YgFt1Yx5H1UvL1HOBYpzapKpfdk24Dj84vrLb_xGNj2wGCcbjciHU585U1xAfX0sA5fgdEYMHsCafocAuF_V3SL7TbE05So-BEUXyMXC6p8SMGRxRJqxsTU8ear_zFeURSdzowBkpYeoG9FpJsomBSR_kj1SPXp1Y5XlMZyM2xSIYmZ7JkRxEGiPgdLUHNJztFPM0U1JcWVJSWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3UfC-C9WFaTXCJWKzwy48fcO4Y3zx8R5PtJq3X-mo86eiEzJ-xxfwgTEa17BCRdJryFCWkb6ycEZ8t-ZSLS78l8OwcVm9Mgpx31PdRyDsz484PAcn3D_N457sP6_QFvVAhbIebuM6zwxXyyydVsZMF0HTjkxzxYjLHGKA5g5eSOGYuXrmvJ_Vw0JYlq8-i3CvhoI3g7WvOWgaftqIo20JD9d6x_37H3Uu74gEIzUXrFXhmZjRZe7NCoyPHTfvcziN0-ESM0jBgGlvsRfTA61hIIzSrI80Lh-lIrr0evDEfHZDkz8KgPvyT7b4rn1bEp50HgxSEntoBcKxKruib3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=N4TPuw0oBsIn3TwEXzDAnBj1xMw-rztzGewEtG9kP3fIMwNELRC0fy_3bHeazMIhKaTvXOzPwqrqjZ-tjG1tfXhmQk-_l4KbZqq2OFMCn6KPQcCgNRT0r_PFqV-lhXRIJQJImqBL272_tdsiqu-WNKcuUICrOGqb1F1UAhphKiPwE3nTPp1o7ZQnKdVkqjRofi8OAjigF7nEt0oGpVpcEYn7wKxxU3-pkW0dlGJO1jwh5fOm6hGijvCf4w31Z2pQe0yG0ZT7MSXxsONbY_MycevVwOornGqY_Tfzvr2wSFQSbw8DFcRZE5OgjGpA4zfTAgArajTHzzumqo4Gses7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=N4TPuw0oBsIn3TwEXzDAnBj1xMw-rztzGewEtG9kP3fIMwNELRC0fy_3bHeazMIhKaTvXOzPwqrqjZ-tjG1tfXhmQk-_l4KbZqq2OFMCn6KPQcCgNRT0r_PFqV-lhXRIJQJImqBL272_tdsiqu-WNKcuUICrOGqb1F1UAhphKiPwE3nTPp1o7ZQnKdVkqjRofi8OAjigF7nEt0oGpVpcEYn7wKxxU3-pkW0dlGJO1jwh5fOm6hGijvCf4w31Z2pQe0yG0ZT7MSXxsONbY_MycevVwOornGqY_Tfzvr2wSFQSbw8DFcRZE5OgjGpA4zfTAgArajTHzzumqo4Gses7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu3PdsNuj9Ox3CQC1K0mwEVls_SUBZBWOWxXiP-ln0984FwNp8cZBQoNp0sfb3UTxcaT29rgk3NYnkGBKc_M-lJBOC0XiNap53lAtn6XDB26KmFfui3h6dVQEZazTrdmDUSaaKr5nWKg5PvpV_KeyEsJfKMrqq-F1V1lF_5VnAs32exqoniKOkf4opIobMYo4Owue5xL7cjxv1saL7aU2z0-Zpwyhfp5cRQS7rrndxH5i2vDezyJiPMoQ0CbjnRdbe-mN0ONWxqp7JPUN3KrUTEjza0amu3N1XV6GIy459404-6-oKf9zaLsGqamnxp-7R-8ng3AwQbGfh0SstSs4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=tjAl1QYLc0xCROkAioEFxjwdoUsTKW9Ob_kUkxjUJrW2dN2uMGvyuJXkwqwrW9_WNIJJL9mi0GnjnQaUmZfV30rJ0Lg3BwMMDPQR8LTh6dsJsjyFwNzNTKV8DOk1EpoxzmTfyOiaOek09RMFf2AWvqLlaPejMEi3ZnOw8MaD33vg5gtX2HTvjihBf-TEyMKmse1n5xw7YC7y3n_Qs0X54NPR9ng6gbnOni5rj6ZweOs612Rw4ds4ZOcvK3ywKWrXoUVyNOneiBtLFckYfPYe2LwQW8qGWjo0VnuU4rpu-g8wobsQ-IFcQBZNyc9b9NkHyTxU5L1Bx3dbVct7mWD5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=tjAl1QYLc0xCROkAioEFxjwdoUsTKW9Ob_kUkxjUJrW2dN2uMGvyuJXkwqwrW9_WNIJJL9mi0GnjnQaUmZfV30rJ0Lg3BwMMDPQR8LTh6dsJsjyFwNzNTKV8DOk1EpoxzmTfyOiaOek09RMFf2AWvqLlaPejMEi3ZnOw8MaD33vg5gtX2HTvjihBf-TEyMKmse1n5xw7YC7y3n_Qs0X54NPR9ng6gbnOni5rj6ZweOs612Rw4ds4ZOcvK3ywKWrXoUVyNOneiBtLFckYfPYe2LwQW8qGWjo0VnuU4rpu-g8wobsQ-IFcQBZNyc9b9NkHyTxU5L1Bx3dbVct7mWD5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNajILkMkZXvb4Pjrj6DX0R6b0bcc_JnYJfvVKlgRvnW6Ac4W0GGThL4DzYf4U3qJojrEpiZH4CO-4GbYX_-BzkD6E53UboH6bVjMypcGGHJCUw7NZKxYmnW-9Lnn6hZjZ_xAHc6MsJrNkkJb7zJYL576pqCCPSiMpqqqtb5qMkvI5vj02pAP2N5PjGTk9UNWRrgv9io3s6A7EQ6pWuTgV1xDeILJOpPsDRVsShZgLBykVunlZxAyNkaaHKuGAgRyFRvOa23wY3Jd38rqU75lyKVEqtGIid_WHn9WQ6hjrXpugKC7p0fflad_Bi9i4kzbuleFK4n5HOC3eM2n0Ee6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmfdn663oVbPhJLhOnVKk27NsTrjpHMVzhlngNbPxIKzckfXHROZ1yXoGt3XhAzRorL064348UiXd9cTart0zbebTvZRNfBY_s3c-4V1jLJePK9gTGbeq128Ta78OncFlxFs4j9phks302oFz2ik7zHPtH8kX-TfN5mkyobPsSvGAmjXDh6JHEkKv6VPQCIhXrFiIYelHDJ_MbmO2bqsPOCY4EGi5XwRXlovIbHWIqwOYA0_6irMfsDKWekAUjCEn8Kpz4uq7f_QGRjEYS72rBPLIZFmJH8owBuTI9TKOjYv1Mpjg2Mil9D_lkMXNhuDJUcZR2crTegC81H4Z_hAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkPj1DLaVxTnAisXlrt4mtj83PJDPHvKVY1V_FzOAfi6Ul1nzvoXS4V3mWI2gcpSl7Qsr7xjTD3HS5tORPWm0AdklTYWJkG3_TET8JpLc5GwJoS4BTpUogUAJM5f_jAOGVLWsjMLR9qnehjMNW0_lbS63yk5L-cUnEtSIzZoD_d5wJmIvKDBxnse4PAA9JxLe2q4zSJJYPZsW0kwVLMv4YjcCeQdlRFSOmrNCTMPoad0kVQAltKF8kIwJ3bwBlbBiFDssztoXi36w2L9doA7KIjcWpLfA_cW77Bx5xPkZSSfyzyDIyAS5PxWd_Xpsr6tNCwvDZNll-BzwfiP3TcLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=QRkWP6-44k7TJ02J8gXCe2sEtsqpOryTLt8ycpx6K66W8CqULMndsK84INgVNte4JLSTgU1Y54ZvbxtGTZJ5_TWScCY4xvtWDSUzMyjyP2dUFkekOZPGb6jbtTy5M7tUQDz4bkRnRXd2O7ixq7mpXHvbXKzw8f-vem1hgLzONGPUZSxOVfgPGVK26xy0YWv4Jx2ZuZygc30hoQZrz0qMNHuAZML2jX2GlCJOx7lrjAqMcQlyk8LmB_WcnKhTt2zb_7a6jKTz3soTofKJjG4SM8T0GdykB4808Aq-fqcwa6rQJPcITfKk13GD5UraN1tzA_IZ07TtuGsVc2viG26iqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=QRkWP6-44k7TJ02J8gXCe2sEtsqpOryTLt8ycpx6K66W8CqULMndsK84INgVNte4JLSTgU1Y54ZvbxtGTZJ5_TWScCY4xvtWDSUzMyjyP2dUFkekOZPGb6jbtTy5M7tUQDz4bkRnRXd2O7ixq7mpXHvbXKzw8f-vem1hgLzONGPUZSxOVfgPGVK26xy0YWv4Jx2ZuZygc30hoQZrz0qMNHuAZML2jX2GlCJOx7lrjAqMcQlyk8LmB_WcnKhTt2zb_7a6jKTz3soTofKJjG4SM8T0GdykB4808Aq-fqcwa6rQJPcITfKk13GD5UraN1tzA_IZ07TtuGsVc2viG26iqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fhz4ikEsf6-H80hbZNlkGdPO0L4KpPo87OIeO_bfwD3WXgzDqXjq38blw27iQQg1l-DlEXvUxlTFx_kZXXjPsNUo4sF9t4FOAXHjwDjwh8rXBc7w8iNaorcQWpY5XPRPjsToeVR_BspEGleHnvkY3Dp9R7TilwKl1OW7PMZkQ9lYSGk9b8bo0-hpEb5QZumlyRInsfKAXWBd9ZXw4amcKf6k60JIl0DNX1uHp_VHV2T6rpxqnyHKCgxaEFNPSUH8ems8O-RM8rC2hPKdvF3WeYiUByHa9gEUh9E2JsztxcioWK4XKNa2eEbhfs7JHaRSwG5Vdskvb76tO8qJYwQ9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔗
📥
دانلودیار؛ ربات تلگرامی دانلود از اینستاگرام و یوتیوب
فقط لینک پست، ریلز، Shorts یا ویدیوی یوتیوب رو بفرست و دانلودش کن
✅
🔹
دانلود پست و ریلز اینستاگرام
🔹
دانلود پست‌های چنداسلایدی
🔹
دانلود ویدیو و Shorts یوتیوب
🔹
انتخاب کیفیت دانلود
🔹
ساده، سریع و بدون دردسر
همین الان امتحانش کن
👇
@DownloadYaarBot</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tockE8YW_Jb1b_0G0b_Fpx4hcRl2mzVGhGihiHBVITuUoQcdgUsV5NbQyZVg3B8cHsaoytB0sRJTQZJdfDdNaSLnFUvpgP53ar3AYAsiv5nANchgsA-p_o8NTGoTQZ_dj3whuYzao4pKHyD0uTYak3GWbqCGhKdKBrN-K3EAwT6r8Y45MbCOPa-feNxim9udJGA77dgTRRUrHugJ_D4ACr60_YHhUsCI-G1aHNdsa-DLZvVHfW4LQsNLQUQ21oVNJPKpS7Zk0sGT-6UTHKKRcv-Ckbbm1bG0Raq9kBBDzqf26LL5O6ye49JxfveT6rNWuXFw-Z-swL31P4f2eE2mdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNANnUklbD0OIqvWhR5Bv0bnzWAvxjzxdh5x4qi1SOgG01ypV0dY3XBEffpZBWzwJSMhLzHzZOwxzUG12OUEJe4ood1gb9cYtZ3vq5ib24-5VIRRFJFlesWF_C3FwUXbcFsAHG2Xug_7qTnWGqnRnnlcc8cWXX45BFvYECZpI1da4_10QhNgZOAXeStLHvv3Xzknyv5J9l9quKDs5Aa1mmktERpj7IS0xs7Z0AoEiGRujDSI8q8IlIp6wteg-b2MZyA-AGgWkPIlEojDuJMpu3Cyqzm3ma9BmPgYJOLBWIo_AWwugbByjvC3QMl7FQoRdXtuTzJXuBPea-PfDUJs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXeoFhauG-ITPmDv9kw2qILl8M0NH8e-JqUx8nk9JVc25Th0UTmOQFSWRInJC0Y-pqEsp_428O7izxeP8HZ-ieVSDSOW8X9mPgYIsM9E0veKBxUjMiK-3wwEBEvxkX7SxiOhGXjd4fObk4lvJGaMQykJHXy-hqOyKQNN-5IvoQ-CUMIXwrW_IK6aaNisKGX8ydDXxhBMlZzyPGK1PYHAp_vi-t5fqHJjQWeAKXTtT54bYucY9O8FxQnsBlVDmsk5O7oFrWrrLjxioS4fWAOPlu5DBO6DcN_aTODHiAdTJ-39otOA1K9m97i8f6It8nTM_S_dfPUpInKItkABM95MXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt5z0E6gmvltcsPnC0mJ7WRGU3Rylfs8Y_bXk3I59MfzHcLNf1vnVSxm_vcPSKov5b4Ip6-x5ZTt5l7KT7PCyhWlPt-4mnj5CEoSSRV-lbxcxjlvRYZubYUIuaqZpVsdN6oH7uj-5cGh-iTdAAe8sz1xHj1RUL8hh0m1f50W7Dq3fBkkYrnCY7g0ecb0mKAG3PyzKMKimUxx5qTlqC32V6WhP5BXKpL8E7FoaIjxoYaOVmM3XQ8csSfVVY5gLEyhxB9bC67Kox51ZTGKelYrgCwhoLZVX6IJBXTuKi4cgGWrHXDn7Yrwflzy8PAqY_MkK0Yyj6WPAkCWHABEB6PEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCamDdno-4HCY_4JFI2yzGjsLPCxdpqj_Kr5o-qaDfgiFWfRHDREFtt8BV66ScnTcliFK8nSAvjZJGgwdk2CEnjvPGnQnKvPmE6W2OxFUv9l99RAcb2sHmFvQHd_MkCWR5l1cvWNQwIGoUkGIgncu66u8d7QMDEb8WCJlXwciYLU6Z8vYee8f4e80QkOQwx4-bptCFAuB5P9wj1nRtprCVngXRvcgkCx384dC_dTSHjoBdbKi1A5TC8rrrHk6RFAkeqQBjx6AjlkdEXPvuex6FuW8n3M2DgV0fFFMORKBxCypxRTsbZ5WmMipImNRiAMYb91BXPttQyTsURezsZLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-ToPpzJM4Q7_3q5SwKxQA-SQKLJfKzs7iXi_Uw2i7tZDhhFRQLWH2hl3Y3ha93UIzcc9-SYTj1RhIAsYr50lgbt5hr088A8HYzg3K88nwwYZMQmEN-P7x6r0wcsH3RYz53jfSXg8OXAmlGfyjN7X9KDCxrtfPKuKv4oIEDAzCKgdhUhqWA9e7Qcq6JCHnlpmgJrXjvcB-GwL8pJo1nJkSP_lvm3pmNnUr92kBTTmKeRN-NKEzlnN0APduZgXZNXykEMuY9xNOkRRkhIT2cwYbu3wVEHUHw9AaN7z67UOlVmWv9BQRPW7EwCZ04FpXE3gT_x2npFmu8i3JwSQnD3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js2GAszGxgcsk3xC3t84fJ-B9Wv_CopzQx4V58NTpL55ToAmJquHYQp6t0rH8zi1B29qf-_7Fnlplormx9VNAuZr0LUqyAtcObYDGE68uZdjz6kkDIeHw52-3L7zgRxjFSHRwOe0kfUVmCvUWF32XNTclWpzNML5XBghYCOQsarcSMZYZs57ZOvWDJ2p_J8ztrBntH5GcNBgH96etPzFFFggpevaceqbV92-inRk7-iEAmu_JTR5qEhdlRRJSyVYXOvllYaKdoZKPwqHRm_kqOKlc1o8iufPgAY7GF2bzBJqgDlg_TjxkA2qpCuCSQWdyFuNphP0H0XUHpbV7JPrGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG50YiVr43axaAyvIDU0eQE-9cZbf6QNmu83-6_xqECScuNcUIJD_ET4nm6dn5suY64g6bZB4G5kKG60z_ewI0rTKXuK7oROY3B3VI3OgU7_p50xPdxsND7ewZKNJ17m1vSGn6msPqFE_5QI5BLfKbxX07HIwPuQnERTakjBkooGMZ-oAECGXKU1E_S_nNhwam4MgTnW6ek6FxaVH8oVeHS_Lvj1OlqB-z2khgpHLrC3rDFDSPjBxIM7473ajjWMbJFUSVz7ij9457Dbp1uxJbUHgiOO4YK8n_4seYe_W5FuVx90xyjuYoZpRFtT2zelOsiMYew6nzBlf0mTMNBovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofobhgKCwtiA_efLVKO0iFI-m-3sSQBoUvbgfRnCv6r_mHGYPUMS5_XO79UyCVXwyBk-19VovcTRTJF1YQotMaEZ_ySRrD4gxo3o14fJ4LuGz3CDxJe9zxF0hyaA_qLivr_m-kcqJ7HsymoR5Kk1v6a1hVNZpdLEy805t6sjON7iT2Uws_fDxylrCwrdPMx76qyPX7Dz4W1ShfPmBTxQYBA_ZRt2ecGRs0b91kyNFF4YgoNepAisdflQcgwv6uqMLwdMV1oZFWVaz4NTJbBVUs6SJ33ryuE386Y6lNfjUSyut_BmS2iK87rM1f7vXNTkLrbrGzoMSjVjSpAW0MEbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuMiXYieyelaGsD2jgmwrImNpvAz_gXvTpKa15QBT6Gi-QuDu_yDOmyzZWnPy9cqLwzwXcepLCzRGCmeNVILmaiWOEBre5CD4IGaU7-qUdMZUtv1qQu79m3ecXltj8d5Eg-pf4S6aWFib5CdEOR1ptrbeWfGCn6ubhZSWknrY6P_jruBu1G61x0GGjAFV4nnZFj33_tNt-x818bbyKsaWSfq2FQkIsKiovKHJW6kkDmVuwhVdClCngliJFxQjnxRoySDkxscoXrpPce8PwVY_uc98aRIT68zAnwP1j-0HPeKrtG8tlKGn_9PAqeEjXlXxlzEQ0XMDPUkNKLjnc62EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsLkQXk_l1pnJIUUpjw3r4Yx1tWxYH-fNBU3efPUM0rhPLWqy6pBrE9kuzrp3ELRBA6DkTHXGw3dbWfxuBJ_mmeYwDjcNguJ6i91skj9JRBufR7CExM7tntq-5p6jaMVdSyMaq7du-fJ4IhERoGIKyHyxrZpM-X9TRA0DImVr4KIBbeTUko1sGq3kMiblMQ47f-prrJ1IQBmpxtEM2a_mGUXSVrS8tmADvto3PfojyY8K-lgXDtX6dYl2Y_kgUx3lmDS5h5Yu4qMkHz6yS2SG8vTxb6lvN0bdI5SkX_r-47JHAMfZA-r4kF4pZ09aryBQsUccuvFuroYqEkJLWg-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVPwDSx7XLcV3AhCbtZcQe2P9rinL3cm0UGYndGsoDeNhOzMMOZ39rY6sy23CRZoMgB38r4a4MZwYP5dQqw4GOdTNgF_3vdJSQMJkPAkn6HluxC2R803OurPtwigzyFbjTTcwNM5cDs_GzIEFicjmlqgKvq0TkdXt8nOne3cZwbgBnattSMSOHxBuG7qju3Z6JJqKZb-EJxokOjWIloNMCxM-xiiM2eRQA7u97yL54WLDM_0XXVZbNmHLKaSwaHOGs9-hYLzQN79inMf11LG9OuD0iEho2pCYb-h0PObFXvuT-mciQS9lo3duYhGenAY7Y5Dklgfc4T2895X2aM1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk2gioQPzePyZ4GXSnVryKKItsTdk65kFOc3nThj_gzXy9ua8ksOL_MvxpluEE_-UhlvEQemgEhfV3HXmQ_FcpdJCjFObUr34wWRJLEL-58MlzVCnMtgCfG-jAvy9x0axLecg5DtzSV6NUhITSY7y2HIeujZoqgeLdCE1JU3_R3rJpc4Y9MXJCOza0BqP5mUCe6rZXdba4D34oSKhJq77fd3_tV9_6qjj8FbMUQvYAcGkRvnuiv9NCJx9UaQ9v89FX1EpwWzEiGd52_TXUfDlhQmZI6QYgxvz4YTIuVGYdZXZeHXxxOSYfJAaFKrjYOH5GyaI2pBxGbSZWI_wG6LNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=X5g9C-WnQy7YvSmPbbEsds4aJB6iTZDaQmYXR0e32fXxCwYfGI7ksCfdroP8ZShObXkgA0XcgYls3xLiEfls7YkVCYjMBKoOqHcAtKfqDhF9k-ppJiQtnkhN8CzEEMCt8wwWZ4M-n8EL0Io5UHxe7h1R1kkjMmBQisRhwL9sLVr_KmUrob2nBZFSFUx5RTFo7MH5Z3ouCMwjvUk1x_kTbQ1ixaqSr9tooC1-QmncQ-U2L5upGLC34Yz6LBestWo3wCUYgpOv_YOChdNs4IO03D5X3OTs5pxzZGktApbDM6eTcuG1io2VtPNM6KZ3AyBxs7fpqOu0AvOinKlkD_7lCrk1RfeX2GHh2yD0mmKgnwqhQKzI2LcIORzHuxWbdCkgZ2EF-eXovTFd8z8DiXQ6gBxqp8f2dndYN-bAOHooSWA2VIHRSAPqe6aKwbAjdIQCYlqPwdDe1dOUPkOnEfQ2QLTJokLPQlFHvYc1jsLLhgikXsaSQ5aEOibBdIQTRRmHaUzM2HTpLc3sav-vaPB1BrJFHl8ZnDZ4elZYc5KAHI--6uohMS9KPhXpHJrSl6ZzIOj5KHg6pFPtWalUkk9N8MIlNyCU5aVX4i08cj8lK6tGC8zVarSPTdy2QsuwrT3O4q08X8O3k0NgybSALvKIyqMq77M_0W8UTINcvnvFSKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=X5g9C-WnQy7YvSmPbbEsds4aJB6iTZDaQmYXR0e32fXxCwYfGI7ksCfdroP8ZShObXkgA0XcgYls3xLiEfls7YkVCYjMBKoOqHcAtKfqDhF9k-ppJiQtnkhN8CzEEMCt8wwWZ4M-n8EL0Io5UHxe7h1R1kkjMmBQisRhwL9sLVr_KmUrob2nBZFSFUx5RTFo7MH5Z3ouCMwjvUk1x_kTbQ1ixaqSr9tooC1-QmncQ-U2L5upGLC34Yz6LBestWo3wCUYgpOv_YOChdNs4IO03D5X3OTs5pxzZGktApbDM6eTcuG1io2VtPNM6KZ3AyBxs7fpqOu0AvOinKlkD_7lCrk1RfeX2GHh2yD0mmKgnwqhQKzI2LcIORzHuxWbdCkgZ2EF-eXovTFd8z8DiXQ6gBxqp8f2dndYN-bAOHooSWA2VIHRSAPqe6aKwbAjdIQCYlqPwdDe1dOUPkOnEfQ2QLTJokLPQlFHvYc1jsLLhgikXsaSQ5aEOibBdIQTRRmHaUzM2HTpLc3sav-vaPB1BrJFHl8ZnDZ4elZYc5KAHI--6uohMS9KPhXpHJrSl6ZzIOj5KHg6pFPtWalUkk9N8MIlNyCU5aVX4i08cj8lK6tGC8zVarSPTdy2QsuwrT3O4q08X8O3k0NgybSALvKIyqMq77M_0W8UTINcvnvFSKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0OI4inSZX21o1TKuQxY3BAkZAG6dyHE-zBN9lQrH0qYtReZiyGH46paI_zD0K0FZUac9OxrRlOhT0xvivrwkoHdQ308Der9FspRp1k0KYj64Jbyrd7T6-0mAGU6bKzvFkhChHHSKqFbyUXmPbC7dD_XSpkWtagMtwRR-Otgwt2VLphQ-O_-TAXGK2w9SV4By4ZrrNycb82qhpm5wasPkBfVEzJiEp1_vGqLuwt8LGyDxvNMMaLLFjNRdgB8NNmQ4KlrTKv7A26LoqTyluNzEaJZJeOnUi8hqob-7Yytt_07UqwLB5g4b3n4PuGct_Y1gmDujgsXVs5buJfj_ODzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNa9YT3btMhOCPV2KHwmSX695eqTWfuSBNjFgTBtwFLrXiFK0KNuT4r5mSfacdAzWsSUU3UuDBl5P9Ar8DJJW7k-6BN0FArVGFs2GNGSRh4sFNmpmqI2FDGfjkiZEaPhjZ6iE1A12UdYbN3FoLBywfwTFGbT_ktseh_uwWQkuD79l9mYO24JZ8y8hjgDS01hyZslFQs9j-5kvj3qHJCJyzWQc9PRnsAjJFBn_TZ2SEjka7hdPhEU7pqFZjwV-4YRWXgSQ8HtQYK1VMO9eazbseeVdYZvoS2RZYBRabOOg7KfGjhiIF6Zs8R1V2xSo8o-NFqHNx_zijH1eyOvOtrTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3wyeHYzzn9ExazNaAG28J7D25nn6D33YAkO-OuSUVhDsdbyX9-gyTuXxMBOwOGcRBHm3syfm0ds_q_f8CVcNI2ahvmvMhm8t3iFcdCKWkDdVEVxeMwe6Ws_8U9boczvP0jVTAoPRyS4Lx5G0SDsNAzHSrfiz5vSZ6BVGeoKwg2KFR0tVVXy__C0VzUVJ_1Ocs-nwhNFOz3tfj2qHX2m9jEtXDa-QU4HghEUBZ6gB8Rho5A7goPI-n1H80VIVniO0ZzmdKGnUAgEV4QfSYQ3NJ6hgdiKO4G4YKKmNo1nVOBCoZlvSF0dd1gol_lkp-JVtAGL-J2eSoHta0uuZXsJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dshw74Tn0YAQq2o10jU7_XoPftVpZFvYbf-97HtzhPD07SBPePya0k96vD6IRSppTiDY6rt5wJHoveTmZZsi_eW1NEbCyNuvI33DJ71zaR5F51zm8EWF_cPDZqY9mi1BKFEGk3BoFLvq738LX7FFcA3AOHM5JtF9qrW_kI6J2RqvTnGBACLBXyJ0Gk16f99usAMYBP7gfnLNjqNBgxl0-dPwM__Y5h9IqiLzh6cdHMPwRusdH71kd_w2RGY0nd3zs0u9K1lqZXoDCsRGqzcUl1S_3OvK5adAMKGCTrwKcpuOxXrcO0meHyvWvfabDdhzJQITr2ZXbGuQ-yp2u6B78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMl_gngMHVzyGqh_ekV-HGXKZ6CjHXZLpS9IBjLfImSifVV9WdC93NntOmOWVbTNiKGXY-aCWvqYMos_lUx2amRIY9u_Ie_IeR9Zr8n5j5xvLF4esyJ-bupqkwgsL3S4WQu6ygaFq9AJFA0DU3OOWH9GjEfooNkKqd3fIBylCefKXOWMUC6O4al-269ARc5L7VpdyfitCmsKz46XBH_BYR9LATnB7b0k8AP3KsqK4jeK66oLORI25C6LHBUXtZ4sBnSAVM-9q6gBOL6X9FLjyN2CBagF6IEwApIdCsLQheiHDVebhPy1d7nO1l0qTp8b4YV1KEvsRDnfYkwbTaZ1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vklkp4ZjqkXJ13UD7Gz0e9POCVXG3I_FwRiffiDV0mz3b1o2JZxp6LIMHhL2tLSHUO6vAafXdDwL9p20rkFRZzhe0JC3MfJbxUxSr88ryC4LrLOVsw5bIbVoa6uR_vHEN_vcrPPr0cFhT-s9I0JXFINn2DMRt5XqDwP2s1fA-3ysjh400Kd_l4q4kyts-LcBVV6TyM5gWIIe2EAgRzmI0S2oafFGglAwUFYBUg-x1sWhDwSyM_FaszFoGhUwsKfiBafkUJCUM2TDvOR-2xnUAcySqRHaalzP3cnAcHbYP7pzK23xp5C0f25tGP-xJkSsZO1GVkSoUN9qN0VEAc9rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8rD0xayjsYzqjqQO49qPQhaYeKv7038Fp6_bz4JuVGoLvaSYwue07MHWXkw9UjUZHlxYLUW90h2aFXik-3vCPI2NtL6Q30mD3DpSsEcz4n1UYonatT3j6uxyAVCzDQnZac5ocZNxTzx4CgeMCIXUaAGgOPc0xxmOTIAh23Eq0ZePsYddYgVNxUsvJb_J6BGN-IwK5Q_pddIUGnJpKWjsi4vg6VOC8YI556WYbnU21fo6TdFBQ7Uw3NJnC0SWPBOUF-LrZq2Ljn6E3ajtaMZ0Nr-p6zwA8CXCgsUbaQ08AxR5PBwqLoop3P78HCMX8OpxDiGfGz9AFMnFOmlIq9raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM-r_q9m1YlbbxX5zS5kWVg32t61UOZQ-X4cxKBts_e6rGlqLxXHsVqayzm5kmuA_QiKxz474_GN7HZUVDugb69N7uVFFnPvUOUEeqmvX9r9_ck3TFyrmy7MP2NfajVt0-VYly9ui-ADjda-naCxLYce2Sc5rkwvMsAQ0gITmiSJujvhAbOqWZQjq7a8DrdId6lgKPLwRORUAzS36q9LfLlpuHclwpaILo-aVitMBHZobRbJrARZafdbHuassKYLWqh0gbYBBu8Tprp1b9XA3k9drd5acjJ0QEAEO-9cPsnDx5n08_Xics64seXtR5kQMEGTmKE1XwJ6h8jJoV6LDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JssL13nTEvYivb6N7CapdM_CsIYV3uQNZdrD-fzx2r2fRB2dbF_pz1h8bY41saSHWfUozp5vD2SalqXpN4pHlnXtLpAETDH3K36ZAQFUSziZ_A3MqJn4eCCkImDDUxkl2r6F04mGIpG4JUR2DY6R36eYj028oywRb6UXgQ6wW206AzUVEy5SZKAJiyvak0lWCEKMqWyExtEEFN7-8vd-re5rI3yo1jxutsQt6yBzf_brkHUUd5S5mLBUAWAPiNK6C4tP_r3iUfz98JPR0jz10vxEyAf7NVL7H6hMIsb1MJbOKoVUnzWzEtR1SrpX63EuJXCiLx7ufqqE7TiQBswnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCxCgohzEWp5b004UTbpBbojLSoL1I1CmmGcwPnA9ID7BZkH1LSJ6SXmIcWCgQAQq5V3VxUOPHUer68UUrqihsnvzaJnuFbeCa81IRLMd5DEVOgUqrL0rqo5qOo71OYPhJlyATE-nv9TvIMYQORgF3DtZNELN_mdZFnRk1zRHjF95ZPTjx1CLiVpop0mx91lFhpsrORLzuCJgxh11ie2uxiozb4WqqR60aMkcDpzHRYSEe-aq6K5lRzcV6o6yZuTX7lzEYJ0tyem_WZfXcOU9V3w1ah7qXr27N7xrdyIVVPzqzLCQVTgE0oHobIIDTTluPV0Crg6t4QuGk5WsEV5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=uZoKyxbPzeY7gGeile8CzrtdLF67b1ugk-8Y0vCyn0PU1vwiW7pVc0dq2htw3xHM61grS09gE7mBbPZAZNRFikCPgxKoGPwTXbPx-gIndoIBokkWcn-_BwbP_nNZ5NvCIMcQL1UY0VdOOGroLPkewFXoRIroR8WY4b1AQ9Iv_mvBaHjV8eTZGLBnX6KIE0K57xMAzCHNzV6h9AzladxrtuQJA01ImtVBFikR_ezaDCxsIBiw1XJLgt4HlwuN3vJD4o593Ersf505JIji1oEqLunsVTA_OS-35wRb_aKbqKNmR8BbsqPWvrpVz5nrPf02ryH-4VcH7raJPD7Elu485w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=uZoKyxbPzeY7gGeile8CzrtdLF67b1ugk-8Y0vCyn0PU1vwiW7pVc0dq2htw3xHM61grS09gE7mBbPZAZNRFikCPgxKoGPwTXbPx-gIndoIBokkWcn-_BwbP_nNZ5NvCIMcQL1UY0VdOOGroLPkewFXoRIroR8WY4b1AQ9Iv_mvBaHjV8eTZGLBnX6KIE0K57xMAzCHNzV6h9AzladxrtuQJA01ImtVBFikR_ezaDCxsIBiw1XJLgt4HlwuN3vJD4o593Ersf505JIji1oEqLunsVTA_OS-35wRb_aKbqKNmR8BbsqPWvrpVz5nrPf02ryH-4VcH7raJPD7Elu485w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=R9gsdaUhHfaDhi9mCQxvXfVqZ5G3wSxRhIStDnzqiXYS8w_oAbjOrOOurIbU2pLHeQ1Go7gZAE4Ybu8r1IjCbgL0DcKKZn7VyvCFTK-7nfDY4NOW0ypasfkYOpwS1uCd-YxUTuVdq7U-bQ8hqU25lIPrpfj4SZEFyvivoLzyekupzoxqoknfkFTdJwWbJd4A1d_aLdFrSKYPfUKnuqxqixVA5gi-pWpnWVBUXxSjCjy1hCVIgbdLg3D98AQn9wk6x1OFJNZQpPtjbizyh0ynaKakUIuPc528T0ROqw-7q77_Sojo55hELj31zElqwNTG4ttf4u_Bo5-SsmjSXCtDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=R9gsdaUhHfaDhi9mCQxvXfVqZ5G3wSxRhIStDnzqiXYS8w_oAbjOrOOurIbU2pLHeQ1Go7gZAE4Ybu8r1IjCbgL0DcKKZn7VyvCFTK-7nfDY4NOW0ypasfkYOpwS1uCd-YxUTuVdq7U-bQ8hqU25lIPrpfj4SZEFyvivoLzyekupzoxqoknfkFTdJwWbJd4A1d_aLdFrSKYPfUKnuqxqixVA5gi-pWpnWVBUXxSjCjy1hCVIgbdLg3D98AQn9wk6x1OFJNZQpPtjbizyh0ynaKakUIuPc528T0ROqw-7q77_Sojo55hELj31zElqwNTG4ttf4u_Bo5-SsmjSXCtDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnPcdfNaoyy0HHnQJfzroQ9F1JMJylWXhC-HBR0sGAUpyCEuTR-HZ2241t6MNvhTvT1q2aHvkiS64_2mgObKLsubYCuNYNYJzfQdnCpdYM1WptemdMXoHnDONVpoC1mry13Y5eNwRSfQPfBSoNvuZoH6IWPfb_QyIfbqnzHWdRtQ3k1P1OoSNffs4stHxP4L9ph4NwEJ1t6sqfJhm6KoFYgNTBDi4JVwJDS8RsIetRm2RGJb2ZPk6M69eDRrp-9zROgy6-FjHI94GRisnnUQva8AYIqhFaNgWfBFsEO6coue-eJzBDmQoXateVT3Js8ucdN0NQ4iAedh5JO6y4eBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2igDCjCYS1-E5brir73gEb2Up7joENQy5tuIvFth19EqM74or6CXhUbC-JeQMiugYHGVyEKw90bu2LeJa77e4mkf1EP-1TyDmVFQCwVa-WVXZmlaEh7L7sIfa7SWCdaVxUeE2re3Vu8BH4pmJ2jkAHxRuu-rrmnbUNnt_GLq8NcPstmD7R4TdfrXsEtuNJym_yhdO5widCpSsa6VWmhFCYwZlySWVy3_J7sJy5rAZScecjZsyjB15DOu21vEL4noSgQvIlsltdem9-2ca3N6RVy4mqaFdARUrs001-YBv7zvWlYuAFfR5vevWItITIseJOEU-iC92yYx0GtGpQx4jrjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2igDCjCYS1-E5brir73gEb2Up7joENQy5tuIvFth19EqM74or6CXhUbC-JeQMiugYHGVyEKw90bu2LeJa77e4mkf1EP-1TyDmVFQCwVa-WVXZmlaEh7L7sIfa7SWCdaVxUeE2re3Vu8BH4pmJ2jkAHxRuu-rrmnbUNnt_GLq8NcPstmD7R4TdfrXsEtuNJym_yhdO5widCpSsa6VWmhFCYwZlySWVy3_J7sJy5rAZScecjZsyjB15DOu21vEL4noSgQvIlsltdem9-2ca3N6RVy4mqaFdARUrs001-YBv7zvWlYuAFfR5vevWItITIseJOEU-iC92yYx0GtGpQx4jrjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window $🪟.npvt</div>
  <div class="tg-doc-extra">3.6 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرعتش از اون یکی کمتره اما بستگی به موقعیت مکانیتون داره از بخش configs پینگ نگیرید.
🇰🇿
-
🇫🇷
-
🇩🇪
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window🪟.npvt</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر vpn ای که داشتید یکم ضعیف شده و الان به زور وصل شدید
این سرور موقتی میتونید استفاده بکنید تا استیبل شدن سرورای خودتون
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anGx765iT2s8C_fHeDqt4OGsjplRkbpG4a0RgLt39qe-02eH7D53oindjFdK37_JiBMLmjkZ-04c5xCbogy7NujncUDhVRnX9EffKOuCdASzuHNzUZ3LKZO3ghIMUqCakhPCp-LtV5eTr7-dToeYNDstGibKGHQ3kSQnx5ZGzQB8UQeykO4-0iikmngYpIuGyYKaD7NY4jTCDo3u7FXCgPmXZ15d9_Inn_-yAd0ZYRtSB4re18xJYXAYwX56I8q5s-jJXBsa2hMkBCWffGUHbV1HI16Qz2BRbB8t8BlcrQl1dq8eewcmyyOOwiNOqHNsaTHQQeYF5hWzVBoX3tQ5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
فرار از زندان برای ‌Gemini 3.5 Flash Lite⁩
🔓
‏
⚠️
نکته:
حتماً با جیمیل فیک تست کنید، خطر مسدود شدن اکانت وجود داره.
‏
برای دریافت پرامپت کلیک کنید
✅
🔗
لینک گفتگو جیلبریک شده
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3nyQvU_tIlvzYR_ogFRIRnxRMNFefNSy-kD08LTFvWFzubk0exPmcHkJ1-cf-YV3LKTUpTd561CRrkgWWJ9bHI7VJLaybJSAcyE8H51nRsNmBmL-unq_LQs_vxfK9WqM2etLgOUzIjLwGGtzs6fjR-7TV6anPIV13m_BMW1AXg8AYB8BoN39gDtaY9BjEJGL-K_dQm7F28cckm7URD7nS9CqqmGhCF_0dPIa2HxPGmOhasoZvc5-k28YKQmEicPPVVMc1cvUTqsAbAsYwzpEbfCoZU7zl_5IbQC-wlrs9Dabrmn0ioIA9yr7M8UMMhef-MTaRxV5NUZMva_0neUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوبِ بدون تبلیغ و ردیابی با Invidious
📺
🚀
اگه دنبال یه جایگزین خفن و سبک برای یوتیوب هستید که نه تبلیغات رو اعصاب داشته باشه و نه گوگل بتونه رفتارتون رو ردیابی کنه،
Invidious
خوراکتونه!
🔹
پخش ویدیو تو پس‌زمینه (حالت فقط صدا)، امکان سابسکرایب کانال‌ها بدون نیاز به اکانت جیمیل، و محیط فوق‌العاده سبک.
✅
اصلاً نیازی به نصب اپلیکیشن نداره! فقط کافیه برید تو سایت
invidious.io
و یکی از سرورهای عمومی رو انتخاب کنید تا مستقیم به دیتابیس یوتیوب وصل بشید.
📌
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5UoAe3K_XzuAa1A_2E_cyaqZJTiY3qyQ9Mg1wuMv_q0xG7QbDRVyz2QwRyzF8dvsnZf9KbR1FjjCyOk9mdhDJf3njhf6D9hRpPDg3P_y0okXcqmzQ6zABzP0TclElSnNeyb50txFzBw5bZro1A6M7DUoh8Rs1_wVwup45PfqbDSU24_CLOiBrRPPCqaYojj9osLCKuiWjZ4D2gqdPVdxjksOYuRJtYMQxFE0lihJPI2aMpXjhyrbJlueqh-Vgrl3HMGoKpz4hxiFt_eKmC72yzyhcEkHK_G7MSONO0ELYMI29f6wJD4G7PxXz3xsIXYBr654BlnvLRlNjBXvq9hiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها: •
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه •
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان •
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب •
📝
فقط پرامپت بنویسید…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHEWyo1adaOF8grNoNul7rVuWcQ1lAeDatxDF63tnWrsG7yuTkQndoZfwu8sqY2Ky39Or1mQLtpA8VyYDgebV5C7ziZnL33FdAqjYKXrNWnAivukwvD9b6zeGE03bX4VgW8JixwdhRlYJCXVI-VqSruDm-5jLZaPtbfKGYoTRvEdy9ShWNuCI_8NloWJy-NGdu9xS7PfSx-VD1G23BRZZBG2hSHsTjl1UALZMVd3h0JwBGFEWSzhAtf4MYy5a3ANRwvwmWV5IqAChTKnbq-97lbUdzE6P7WiZExWGm3D0lQGOqqLlNCJHDzzwgBX2oMe0ze5uMFAaQCUkGrbKVP7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmuyTmW7CAEvVqEQ7TylGfRiZzVNEmjAStu9eUijbSdhq_06DEVujRNLViTAkrzVHOB2IlHY4awbDAR0_9O_ovt7LPaB24ZJll366bDaUz7jQjUJnhQJNYRkXScyCApPccjUhS6p3HObAIZpNk9Cj3MtqbhJ9gydwHGQTLp1ZD2rBm4CB-Y-buzcqgmtFCkt3VIhk1GPnaRBoaqYLFXFqlK2w8as7ebr_NmZt0qmtt--62QlWQA34tR30vnU5pcGCRVhmJClRqYYQMQ5KjRGjYJF5spEXgGoMKFe6MT93kIs1i9JisCmr7ju-3Y7mAvgv6e_cO0YWdE09l43BpYt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
فرصت طلایی: ساخت ویدیو با هوش مصنوعی گوگل
🔥
‏گوگل تا تاریخ ۱۴ مرداد ۱۴۰۵، امکان ساخت ۱۰ ویدیو با کیفیت بالا رو برای همه فراهم کرده
🎥
‏
✨
ویژگی‌های کلیدی:
‏
🔹
تولید هوشمند:
تبدیل متن به ویدیو در چند ثانیه.
‏
🔹
ویرایش منعطف:
امکان تغییر و اصلاح ویدیوهای ساخته‌شده.
‏
🔹
قابلیت ‌Remix⁩:
بازسازی و تغییر سبک ویدیوهای موجود.
‏
🔹
رابط کاربری ساده:
دسترسی راحت از طریق منوی ‌Tools⁩ در ‌Gemini⁩.
‏
⏳
زمان محدود:
فقط تا ۴ آگوست ۲۰۲۶ (۱۴ مرداد) فرصت دارید از این قابلیت استفاده کنید.
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6qZhEQSO8FTjNe1DOyfYSeWVgz8dgH8qwN0jWR7YDHVlVsmVlxvwhrssJWBWzn_Kfz1aOf3bWMfGqfuBllX064YV3WhgqX2S2yh5UjyrWBetCS7FwEbr_ubgiKSeBA2zN8JP9mbe_7RXO8c1RqpCM7C7XnZszdsVEw3QsOD2BDxbaiMpuNpYcR7g1bm2mLGqr6cl9mTMwYzWrgbHe9edOI8Mmuo4wObHqzNtNa9h_HVovejC4PF65fm5FMAcCWqVGcIVIcnIxx52jAijLTrduVRMGavMS-kkVVsQxlDQbm98fNPM9DKOvjVISeRv0cuekE-wfCfHW3tdcVZpma2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API مدل Deepseek 4 flash 0731 به صورت رایگان
🚀
وارد این
سایت
بشید و یک حساب بسازید سپس به این
بخش
بروید و یک کلید بسازید
✨
محدودیت:
هر ۵ ساعت ۵۰۰ ریکوئست
‼️
قابل استفاده در
Vega Agent
☑️
Base url:
https://api.p0.systems/api/agents/v1
Model:
deepseek-v4-flash-073
1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX0P8wNoAEtCCROToCET2V-rbCK0L5ITA8P2I6zqUtVYcCygo27-N18eVDVEw8Xqva17qX_A2dg2ScQ2x89OqhTiQ_T4pCmVPCFgJqHxzDQsWynTPT3nE_6TzL4EZ_S79tYaypFqU3GqBQdzieY3zsdnDEihEU3lDx3b0Kue7PAiD0AYGhusrNBueiIP318WFrafL_T8-h7X4LWj4rrKt8KzajoRvKcj-HCmL-kS7-eO10F7_-Nu3BjXhB0yEmudwNZsJYGjVx6QrPoDsUJCKpQ4nYbnZguzwBnwtQcjzKlOlJd480Y7NAMuamUEligbKtABDShNYo7i1iStqV6AOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttvKMTP0mzN70DbN53OmXM_QtWdDK62NfkUy8X5ZYftDmwRlJidG05WGPa-3at-NLSbhh61PxznQ9Z-nbi9lE32k9Offzj5B6WYDPfiYsDWBFce8-nVbmqeU_N6lQVrZ-OPR_udLrTxIZyCL0-g_RtGjlIzNX_Qmv-WbQ7nHmw7qNvzztMOPTtI4VYqMitkGt3gXQxAC3ta9i2zrqVYMaF6-o8_bZksIRMVVj3DyhZePBZJEqtHLpWU1GZstbnXjFFeLHl7eK1O0piYSQhqC0m6s0XnX26ykL1rXIiA4W6H46z-B59zRV-FwjprTAuIKZKG9mFZlbayP8IVg_klsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZQR96S8gvgzXQcHcHrRODnkiTe3KMyIMdOHeGC8tSL9RPdtNuk6NRpwfDZU3phODC341S1UqnnLpDLSIYXamQKH0J-eUvG8iFsUY1ilFiwTTth2tLGuOpmLJoyGgW32Q_opC1kZLXWaf3eZhI62OqZu7Cxa6wYAofOk6PZUBQdxMm-da-YAsDGfLqmbf4rLog6Ki9qL6dbTzNlTOlJ078wW5obqP7yXWRagbsfeQ6PTktap91UiZgWqV7eA5KWC4-5SpN0NesqIclF0hki6ASpr2Aky3LmRvY5LIBeR_PzQVwvHlOID3zNWWZ7oeLGw8scYHneUlUm4W-aMCeD78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw2faXAArnkZDSMqSFI0Ys1cXEKHrUamSw2UglXVmUiPhdrq1BWwToGby1vwNhnKiG6DLdZAtaVLPjXuwvG8l7VkNPj5yREu7RhaiInpIogAJBeKKLMw3tfNm82KRrtgs8BHJmipSUd8t4MCPyRphtohXqws3ERwGTBylAVb_D6-MxP7-WRxJ7xMMqm0-Nhm6n5O2SNp9j5bnyTDaiwwVHYIMF2s3IIAp0xAJ4WCF9Qk65hwyt6D0pcjzSDLmDS_LkWksH9v_Mt4GAZ7sOuCgwGQHXP-Z2DOM3sCsWfShm3FaUJjXBYYZnyzbcU8NS9J4B5MtY1m2Bi0bmRmpK9_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekVwewqE6R2SrWhaSh1z3deZSmP-3dN4ypNwGL1PrHHSUeex6aMeVwy1M9EkOBGJTov0wXs6lpDEgjX4yw-qAXE5ZEZ4MMVWDMXbVRYFnav83LZU0ZULZnQDWQu4dJNIKnMrCDRoytykOF9f3odV_W_Kd-WonnbRf26yimnnn99PyEUJWpdFuUfnP_z7SNPoWM9gTYbbJclEqA4QckTRk_tJICFPbhDwASW1lmaA4O38mKs-hGIeUfBIC6v1j8B3G9jQb9zgV_wd-0Omhu27zK7dG16e4xTDBG7pdY8KTta0Qxz9FM85xo6M_BnORur9-0r8vnPXO_ltw1eEdHl_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qdp1wD_b29rYDMnebgwahImsgBp1EX1dJmkItfTkGU0duygzn8IOkVaxCyFpJlH-mWLumhMTfkF32Y76AP0S21mWwBaF31fuUGqS99rqa-NvUhnMdlYqVXi8-0U276JGygDs_7gtdhGjOeTKGQKcRBBRBxhTru76PxsL3wLxMWrXcVwjoYDNPfZ9gXNCu5efm2mbPaE4tvaCmB70kj2UOvL0FuGalfQ6YCvnS3UYks5lbp1qo24HLzdg8Krt8nbllFanZaq5LMmb-vdfhuddDNMusToyPvsFKpJtHYT0J0uZ2GlBgczluzqsgJVR0ccAg4YKMz_j7aPsk2EtCBYpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC8y6xbIjIZUmnHNsutiKqsIwEWnGOpXGM2TIHqkGPGkTZF2nsMzp-e-ISxLT_eFjlSGkfep7cpJZwuqG155NGR2GcaYKo8IqMsnLpS8PSUlqj8GUZQfbK9e8uKUQVoEd_3IY_aPF2k_dbDdoj__9O_kMkjJgoz02Xzuwfhk4xO5hWUDj4cgtvMIN2A2Wjpl006O-t3bHkn4bSC6C469HYvDFucysZZeF0ibaKyvuMqpfzgGl73ld7ora6BO75TT_A-2OHl-2fJazsnWqPeBbFp_dHzaIwkDxIPDz9_I0wkMhvRwWeUQEBgrCU-nC-QYfMU5pmhCXyoAJtiuTyh1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnih7c9EQmSzXpZJsy7BBw7Sj63rI7y0ooJNxUFDSjCTM4Uw_csnfY8x-y0DwQpcwzMojdGRRPodHVkwqwOCxuryCnm9Ma0s3Ir4wYABVrurUV7tG_k_hwj2NG2sg8nWZB3xvW-M4A00UetpZU8wmfaF24nq4JwkZQP_Rd63ufc4fnNBKintYb4Aub0gf3F_H6pDZZ-19HcI3KcM1Wx5BOx01oJe6pQ8CkbsoFD9_gt1QcHEJ0vz7viahQrpnWiHA903Ai2g7U3QqnE_tw2eiVi_ujRJwN8920LMczMamekzayIkoB5ayxhQpIZ2HQnd-vydE_NmL4HZKNoWvPKa8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9LfL59EFjqMhNJGvpCYqAezoPa1dC2_olqwFHHF-sUdoJkam2KtAlg2gYJQiGSs882RKNj18mKM9sJjJSxTrPqpRimpZ0shnlfBo3VY0Duy74Z5pLLrwSBGZGRJhme1scvBvMmbbwUlx6ZADkXLEV5hhKjgyEZZfP6dk43qpgpNjpxXtbs6ua4ibW4Kzb1lKeDMhy1yLHY_Q70sePHERYqKCSd6LNITS1AlCEKhO1Q9VKLOl-K-DmG3-emcE3LHBjiBd-1q1ASB13KRLubRa92VAQL9AS3WBXruCGeQFGJAm6y4Y-g4vlr7lA-mfThgt-VVYgF1S97FgmGuow7ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3Oyvsn6SvEalHkGT1K9QA40Oys-xLZblOUAaUxjvKIVjwAa2h90eYTvb3Mf0RGyDT7YRpXxqoAO4NtiWalq6JJuixXe8MNyAanyTBjtF8rXi0vNAuJd6i_2LQQZ94X6MpdOJHvGHtJnJXKrh8me52nU7tCgeFgwTr44ripJPy3a1ZdSC2-29ifLLYU6zMxrsLya5JRAVdrY3YR5AC-Ia5yHQCKJXyWXzRT3n3wise8L1whjpry81UcgJANYD2uo9CA6bn9Kq2CGopIJLSr8T9mDy2ydu6mx4YBrXxlNUC7CgFiQcQcRzr3FVkkpeeRfeOp7xonnES-1Rp7aK80mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6DAcvFaHxZq-4v1X-vI7sc90YJNWibpUiqMOGknxJ6vArqI4gFBhXpgTOvrjZ3dXArXKkVxSPeDb8anaKKA2t_ohWlqaAzLf9XshQBe2EJEjIPoGThTBDgCIFAmWpY3KCKS6mWn1hP98GSbOYbFN7ec4or1kqOXws_Q2fzkjOh81Tmf7aSBM2xOHmLCYGOW9VmNVkRj_JHXOYD0KsjOsxfPGxQzug9lnOJF9AFbLzQ2aPewkIFwbsoiL7lisjN8H0UGjy10MsvOQ81KowVt6q47KzNNPu5RUpQ0CNASgiLEK1UQLnFJimh2oDniAQpS-IAgvX1D-HwZmMYO8PguEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cg9kfy0D0duQtcx-OHNRpme1CGQpF7-QGQhtan5qU6EZ0fRAuGd743g89rL1XTKzIintkp48Em7GRiLpqjXh9znELJEC_oA4nKS20WPemw_wr8sT8khe8scthR_2y5H-kEqX2cnmXT8U4UwtxPR1Vv8kerN2OCHuhtcUmExB1Tk7GwwXrge-qgpPg67fR8FMNJwkJg8QRA2jGgcDpqMQH4qRR99qyMfCEG7_9y7FOx_X5D0Ftlyi6qplwMboC5PcdjbUtwfSW3ZiTZc80B6trkyS6GS4nSxFUHpclNpOcf6mAzWY7XSBIg-3m_S_lWA8_Wx6n14yxv0F_WP1zaAQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvvcowzTjBHGLPRxY9Y4bQfAQj34YsLr3jkGVPiZw543XgiszO6r6Io24j1fDQcm2rjmd-UZKtv9HRbv-bpISw6bVcn6Xk9u5yGMksp5PANZ-wwZx_4VrfFRr6YftifXECeCJrl8n8qPrKXde0GmqCMC4NbzemjlrY40ybtCB6t3lcZSr4V8wUe40484KF6egCuigZztTPJWwyP3mOO5DPnffkAz2RScJ-uCvZplEtqFCQeNnsOUBOEjP1QJCw-IulHaC2vX-EOuqnANA4nh1Kw2YLqOlOLFiLV3RCZhzz3NMup10lIPp13W-DhhZXUFiqoOzByYzXeu7ujwULdswg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
