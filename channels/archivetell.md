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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 20:55:21</div>
<hr>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu7zHmYcKz4JUtmJD_ovau5UePp5GV3i4f8zmxu8M0MPDLFijxwqD0amKUpe7ctd-vCf2wbyImvjERc9TNb-hqVTDQCxjldXLG0baU8XgiBlGQJijb_oEmH4dxDdFdQz2AudcHyJ1elsEgk-6rKpmkvPjXt2drkUXVGMSdqoMozjIAHGFX7-ZK3ceT22MAVCUDuYv6DFPL5NnaDeDIOCt_2Mp_vfmRZYQXrS4HQ0c3Opy8JqTIly-9nDWkEwWA14imQHvM9wjZEFvip9y7NmkF1e_OzyR43zkKC4XUWJOPIbd7P7LMN9PuCPrG_tTvGK38qtH2SkiYnOjxPrccXMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7462">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7462" target="_blank">📅 22:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7461" target="_blank">📅 22:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Pd1kp9rkTUXAXYD2uber-tb9TWBw-38XDsseUms9Rdl2VQkAG88F3yrg7Wc8u0eAtsSvhnoqtCuieNVB2NtcQuQNWB2r_7P9m7RMHSI5ZTCKz0QszuEg4WwobCY6XZ-vBiAolpSC-eU25bVsd_DioFTxcFbALmON3xYMyqlcIatFmPVrPzGKOVoUBl-cvD-vfcZPXMIC1LT5_Q5cGEa3pX6-IXaSBr6ZOc4gHIwJOPEYVNFS8tYUU3IzPv3MUf0UJwv254F-7EaMkZ-DLHeXNdbID9Ksb4Sb5NRGR8lM_5sMphQ0feHCcyBIw-3BzjmR5AvTOWZq8V8vkcooIwfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR_UAfGc507awRuTVK8DNXCg6FKt26UHVvcf6M2bAl9twwBrx7xPhUBbsGZ-0SFsXdpxoREW9fRkvvjEETjlVvcsa6iTtWtjf9nN27JdA_fNIHfCg8HxHKrCtUt9iewWjBd5uFzIqB7yU5PzAPA9HMGNQlpk8Rcsy2w21xlzwOrFUmZ-h0i7SaWgYbvRJZaeInFggUpChqdBHRuZW6Pmg2TqmX7SR_8HM5uLaj05agZgv-wJKiRQEzhIaCOYuN9PqE82U0zmkBLkwcxXRUc2pmN9YnQYQDqYDpjF_8ERghqp6kXeVoELm16HscI3kNyIcBX78CIEI3-3qJ2NoL_xUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4x5vp0rOC-8UXTnD3aP2DQYYRZAkoK11SvecZ_p-YQJvni1xyMoywp0EQVKGrIrhBS0ozSJT9WMN5RcxMOCKT8H-YdoU4z3A27651qGdFHDWRYAPGXcJfBBYIcQuoHMMDg9e9SXpdrJVNyDkFjdcDxcx3q6MeBVI4fBmzSIYeXHms9qOUlf33hbk2qESfeQTq3lRGDSg9AIR2B1ny-y6rkk_Fk9okf6DBDn3QXxs9ymAvPGddd1HTa10pOJedIUgjiCgswxpQGGiDTd0kfxIlaa4TlWli4CSsXGjnEE1yJVz1ggYVNyTRp2WVYpx0mIWT8-PhHaHUIZriCKzDl0Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnrAh7fIAJZQiWUCybmlBc-jVrbNFSIW5_6lcOJhuXHTQt1e7V8qiaOZue1c79y5dqB1-GyWudo02iJSVhxZhuQggwzcvfZ9wPKhRea6qKfdOJieYYUOhyr3-wa0YVqjxYxbOvoBiYONGC6l7d3h7kHqDuigU2XcbEv0hrPH4WnvYRGVLBjBe6vro9rtqUz2EZYeiBEj7_LJXP7KdWbL1WMvDqKUpnC0FyKLocBxmYsKmj_6vQ9-1DLsZoILzc5KNngQw_iX3Dg8qznr9M_IGUFxKHam25yZ0Oe5KAuFQilKh5gZRv3f-9jsRd2gbtKrcJXybJ5gpSN7-xzu8xvrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZdqOPjC8aX0Z07A3peUJjYLBMFdMCyzjG3nXZp9aYLPCOHGOkmEuN3stNZMfL5LG5EIgIgHK2NhMlrKBedvVRf7Gny3IXOyqYKhaFX2dUfdT8gjrHSA7ByZXK8MWPnAQ2gXAmgaaWW8Qubi80CwQsdddqDVlv_ntAojrsfnEalrv6WRRHgj6k7RPAworzBqYNzDhYyFitB-z365vNkZTYk2PsQ3O3yPXjWbhhBuaXxfSu_dMAmAXOkct6rsShR9QIg7dKUPD5Qm9wuNNl21fUdOJ80swI7lsx0sWervLMLT3CK90FKFY8mERyTVwuO2TshdSh53H2rsBFrV0Vfa4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=hYu4K-APP9iLJMkfkV71nzmB3-smQSAkZzRA5zJZ705SDTuIyt9iHFSSCGFVHzNvUi9dIO1jFNvui59k0Ct8BAgk7yTDljLf1umPvTi7HHmqsxVMOOiSHv-S6_DwoWHKCc8UIwnJvfu7Xy5qD0sf1_vlrUBz0WuY73snoVMzdpMaaZ9y_kPI-0ahFrgBVGKvIPZYXRPNMidcq_CVZCCKlLH0kpdggUwmOtwZm0DBqFLz7tBo7R48dZerICzSRZYGv6IzIuHqPpHMMzDGjNRiZNA0fnvWHTyYBg-QiQFik_a4g4Ft58ONC4lJQChlulJ51sbiN2TqkUOUYDeZV9NVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=hYu4K-APP9iLJMkfkV71nzmB3-smQSAkZzRA5zJZ705SDTuIyt9iHFSSCGFVHzNvUi9dIO1jFNvui59k0Ct8BAgk7yTDljLf1umPvTi7HHmqsxVMOOiSHv-S6_DwoWHKCc8UIwnJvfu7Xy5qD0sf1_vlrUBz0WuY73snoVMzdpMaaZ9y_kPI-0ahFrgBVGKvIPZYXRPNMidcq_CVZCCKlLH0kpdggUwmOtwZm0DBqFLz7tBo7R48dZerICzSRZYGv6IzIuHqPpHMMzDGjNRiZNA0fnvWHTyYBg-QiQFik_a4g4Ft58ONC4lJQChlulJ51sbiN2TqkUOUYDeZV9NVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umKFiRPY6Rv4zaLSDsUs3-7LciLSa32RIfW4Lj30X3A8RTntK1a2B-4xCPsxpSqDuDZA1UwCyLhfuDa5YW1qqOM20Ta37NGyyt-5YI9RPJkTQxF14mSYBPetESyjoXcGbfSrOAe8kFvwOvyfvsHC0NKEU2HHLnxEv89oOs2abv43YXoqv8xdVEuzNG-BIHe5OuZI6Ylm4sIU86m7xSmiBgfBpNJxshd8jbMoyppoRG2JGN-q8MpM-lLdRz9chkh7jW6b4s5V9C-C9Ak9LCuoxiZVYVL9v8tbHXHzWdEIUBYfkbrJuOD1x_iA51vIuSiEczu7RuHsbvfeXXzMhNmqAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=PGNyKnhCWazGCJM1YPqq0x8yD5G6QMKy225gFCRtsRqCsY4qaKFg3ryyzyCYUw4L1dX1SHhM-ItzdwnoLZcaar_4SASYPARI3NNs7a81PaXl0vcxu3ysgZbSFskD2U5GAOHhqZV1zAnWlTNrSbp6U31247jDB-vPSCl14gLisT_g1wtfPDGJTN0EHMIORtRqE1VhbXaVNervJ0cgAc83kWq4nlPkB18_YZXJXqYU1hY7krlqKiSGVzYNFwqiT77ighnEI6oxsLcH3ro8fuZdz_C60YIurHD_ih4tkCRbPpgJJOFG46WKHCQ82ITYSt2iiNlO4wQCnSHQSFZ3CU974A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=PGNyKnhCWazGCJM1YPqq0x8yD5G6QMKy225gFCRtsRqCsY4qaKFg3ryyzyCYUw4L1dX1SHhM-ItzdwnoLZcaar_4SASYPARI3NNs7a81PaXl0vcxu3ysgZbSFskD2U5GAOHhqZV1zAnWlTNrSbp6U31247jDB-vPSCl14gLisT_g1wtfPDGJTN0EHMIORtRqE1VhbXaVNervJ0cgAc83kWq4nlPkB18_YZXJXqYU1hY7krlqKiSGVzYNFwqiT77ighnEI6oxsLcH3ro8fuZdz_C60YIurHD_ih4tkCRbPpgJJOFG46WKHCQ82ITYSt2iiNlO4wQCnSHQSFZ3CU974A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfCQm0AS4EKkYn0CvqQBNUuwk_EKYa-gIIe131Mc5xFmqQnbuw0NJeK8eizc6o2PxKSnbsjQnmRtpYKww2mepGfQFa5kT8hy5BOcEMSmHrz2_MuCJGMLWu7gkEpmM6e5bApWwKc-SlLwUuFU4h4KzpTFr2SOdBg5PVvkaMDWg4knshxrb7RQWA5E0vb6sv61oeOYBkSP6ic7C7vhKd26VyZBMYEBeSRS0rhQCm2t4gVQ_vORRO59yuIMz3EPb6StQPulcoFiI-Cevtir_Z8vQcuM-I6XDrQwqmPuUWo0Rwf9XUc7_6_gqjvAtcyw-VtRWXsRHz4I6Rf4ticDfvtruA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eywOSzrSLCKF_0f1ZsqOXZGvN7HKgME8j5z6-5N-5L8MCpMKLNwoojlSiGtp9WsHoivKKGrLk1De5-KTbmljRAsmzsCQUuRlRZbHLgJ5N2qO3zWoQCY6kyQtzmnfjEYT31gLLROv5NfkB2UU6rLKMYXJGnlnUTe8d5lv4NXJPBPPdbz_dJBX9UKhLUVoiRF0cXAK_0DRwMP9Q1G7e7_RaPszGOxNbWk3GFWcuGxGJiWUgI2Nn1UYOnK8k7tibwvPMT7JkPmz9kXLr0uB6CkEXCsHrcM_CeCTqKHIaVDdEl_jAS9RVuqrQfDGaStB8ECQv2GSDNo3-x105HDGq0Ef_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA1_xQv5brje2o4dHwa1zyiaZXdJqQIDT6K7RzDjbYLxXtgOMZ9vvh5cC4BNIyZ-b1WVnx51YfAybDC-HMrXv-4V5WwLi7-wn4pNPKvz-jJ5GYZ2XbGq5XPzqyDS2YlS1LedrOG_uS004YvyDQra2Wxx7BLuL2KT61rRv3lBl6TLHcENYGi-QEPZ6Rkekgk9gPnMT5AJKDGNStkjMm3DuygfSJaPP-qbtuGzyyHFDzRMiW8D0_UyR0J6drfwASoBvhAkpM50wUDMRoXRzrs-h2F76XNlN_C2xtOz-pgzL2uHTsUQhYe9Dk2RGioFT3B7dCsjp4KqiAKOfvCIyRNuYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhKOFXwlvOl6CSIHKgIuBjGQ_hCQjybE_uB-kiI1rQdBd7QDYuolE4W3mHmg9CsuXNFYVfcHRRmvhw211If0JtXLHELDzbNVYp03VtX--6_hS31dfOtKewDULIMY4tNHvcrI7t2da8IY_J8JAqxUnWubkHcFUWOQO1Jab154nZMBvATssbIWYjCk_jS1tUCnDwyGDBiq3Oj9keIdYdmq-oNRYCQqj88LjexAukabt0htvJSFKKOMvR9UWRtIz1Q_lMMmTCgeWA8W6x7gEDD3svntCjNts19YdeCVqEmUisrOWQkgUa-6KQnmoQJ0KjiAy3VJNFH5uAVn1QtZSXrbnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCRTqB9WllM89HKXThNLcDwwFP068peYfsWtA3T2sHtz7Pe84vpTzJ0t9_T27S06HOcv1PWKzgme34bJcTEXUmut99eDdYb5eLxqdeIXeLOpF68-FC8RBruT0KPow5aN9-xWw_hPJiQYXzFlaJQLbaJzRxpn14tyX_0p0_2xnaRqKSiQtdz9goY4k0XughFf-gCw8OcG0mUTLOaVlRmkpT-5qelusMZVJzblCUhlfmGu3ERcHOYaqsCkWaFgAT6uZbWlZAVu1vAH-_CGX4IsLuEbW8r7K6eqRt33EOIni2Q4Rj5pKvf3k2oqwHf0V-7le9M6aN4qSIbEnhNmaEHgHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuDoSntcB8n8KDrPZfYSi0hZuyHMp4pTdx84o_SVOnKL8Q55arGk6ZVjzhQa28VM-7faPa__t9tvR2t1lX-zlMoJVvUMI9wmx35m4hRCYbrBRekeRdbMrhPfMt3WOyoq39m-wvXFF2pckpn9vo8N1PGCNPnxIJdeZVuDN81HOtRQOqgdI0crehnfR_dWfRwcFXHbuOjLO8_qTubUhygTSbImun1fxDtXiYP8VyVCPvwlDV_q0l1KzmOntouqhrZfdtokzxZXfP3UacfrltCbg526szaDHN76vu_kCZIkRo-Dm2dDqpDW-kKIXAJwa6cS8R-Rm-v56q7ytsxDwVfA0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkOsfM-s60t5NmA7unr8pfGPpNC5v9abu064BFoAa3UPwSHwItJYPMP3nO-nEw7IMvaN4kD3FijAR9nYQDBT_6MBrJuhCviWxF-chPeYvTWfR4Hh1FBSLqRt5dPyvZjOV7dJBG6YGJ7On3u99aFEbhtpp_kcjuG_F5HnT7bkFsLBQbKOOrzjHnJ9PNYLDpXCp9h41FRIce_qE2SdRtK3an86WASWK27IIQn_pkVrYbIJNErZr-7sZ2NQASloNlWoS5Gl3im8FJQ1rBzuo18D8oI2dFlBoE-9PuRoDo-rpBxC4LpT595-BfMfPZR1Y4Q31Ch0REoR1XCzs9Jdet4d6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2opTmZMhxsswfZZByG5mh3u7kOjmCO-LrGBP6e4gI37U6cbU13Xa7lS5CFGCup2LumffXUL2ZJy-jt8K3u4N7AzMTLyymAAxlMFfdKg2Zye6nC9RlHHTow1URfPrTKISJ-Jc_0c8ifdn-OU0skqsIBts043j2oW5yiy-91t2TCD0shFgkDwUh7N6VSO2X--FwGz2lxSNDpRLs3jZ-JSYSLnRWl5SZC84cpu72Gpz_6EmeQkhz6Mz4_iERN_q5r7Q1VjEEUqvZdR8riCVodHacp7i3pkciBP926KqMlMI69AwKiT2gNKCvBQZXHRqiEJfQbfPLBbdikjjM5XYdictQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVsbX5Bgl1JntU227ftSjmJ3MueGzq-nkQkJAaGB9lAdIBO-Jh-jGySMXomddEhpPfOT29Phoh-slvrRp_wgPejntt-X4YdvqUt0pznoV3RVp5U77vfm7TbCVB2OgxGP50LPKyajZ9WnqL5k52y9Wh3BtERP5VeYQ1TvuvIBRdrCOmT6KEbxKQFB-bBNmfTZ_9co79ozoTY-UnWbszEJWq4M7vYvkbzOqLJ1wlpEhyObKCM640f7TGqAqsyJLu7f1eYe7RsOUr4dCYIWOSrTR7gOHsYJrJkDx_sXm6fvrdCIFeNQPfmFu8gnNf6aPmc3S2g7yxvsUUtYuZrqxQg5Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFmeOtp7T9ZiM-WZRWCAUkVcxOH6zXkd-GEarWi9-cFZhaLZ_FSLFOeDCQvkIcv1PQ1x_aSvrQXzTsFW6jmVWuCzq4FqhhhOgD7AEw2f2H8Cc9AR-oagn4fab6J7IL9lLk9iIuAilKb5XmRb9FctHLlDsQimF1Gy_OS-xh0CR7pQcGVxDBdAXbYf1pPPURygqsB2FJfDOJhza2SYxMc7kvPb5nfvYnj-8eTCVy4FEBh5AUJrhNPmYDuLSHF4p4_dvvtxF8zc-uTEonpd84irsVnY-0Sw0mbYmrmdQPe5zuac4xttKmiSRNCFuv1bMysETfWQwpRF5MU1BHqJxJcUgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk2gioQPzePyZ4GXSnVryKKItsTdk65kFOc3nThj_gzXy9ua8ksOL_MvxpluEE_-UhlvEQemgEhfV3HXmQ_FcpdJCjFObUr34wWRJLEL-58MlzVCnMtgCfG-jAvy9x0axLecg5DtzSV6NUhITSY7y2HIeujZoqgeLdCE1JU3_R3rJpc4Y9MXJCOza0BqP5mUCe6rZXdba4D34oSKhJq77fd3_tV9_6qjj8FbMUQvYAcGkRvnuiv9NCJx9UaQ9v89FX1EpwWzEiGd52_TXUfDlhQmZI6QYgxvz4YTIuVGYdZXZeHXxxOSYfJAaFKrjYOH5GyaI2pBxGbSZWI_wG6LNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyBtXdauxv3flYYrv9ud6Br89BkKjI-81tBximm4icTIiG9UumExC5_2LrSnoZbcFx90-PFQC84CUex27b_-2M6JgLR17yeLxDbShg0-dQI_KN6ShJpD3y6TBFj7Yc9NkfiwWCM2Zsbx8ERzm2omHwCjbDpSY-eZsVbkZXDNsS8Tto93TPQGGVoSwGIBuzno_7FzKc3ISmS-Jp_7Lqas0PVla5blY75yoR_kbEqG8yzXJ1IzzKJd1KczNPjdAve23bBmPBqtfQ2E-pDBkl5zf_KbTpYWJlDC98eLAkuXbbWOQkQhmbP0FQaTZGPOHpTAL4I2VPiO5XwWneMtph9A4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdSq0-hd3Z_JYkruGBrgx_PT3zCawbvDO_cWQQEfp6OaEe_NFqjlU9xugH5IsR-_c-mjep5m61u5xmRthyDdYYjFCad7uDDw26tkWdBxWiN2uMdi0l-OxWV_3c1SP-Bzj7pj8V8UiIDr2xEo2nyelXMo_7wpLvTij2w-tyQBGOuRtlsEqeqpJ1DOVu_C1BsHnzbHn4nBM6Thc3x5HzLU6l-qtobxjF13v5m_hReYN1eFpq9X4cS-caEF9QUjWqKL2kD-Fna2zWvn23cNH1fsjdBxFnlecaeeUizi4-6SMnoZ4tuLWFgWjkr9GEjy74N8WsEebz6qvaV3giIMqMyn1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3JnRsWYAkydnoUFvhTh-Na0jFmxDg5SbWJuBC8GeUcnTHg57A4_RRHbZnKZW9UjFJFjz5uEwWAONtY4_puiA9u0aXsPixyctXlNOE-yDcZtrhlbhH3merxQvSHM9ouoGAg8Zc5IZcImNpbOnPo3Q2wCe8DV8_tFsJZEpx3jzpOpps06cXsuhNSw-E3xEGEyqwH3iZK-xxBOoVd1RYNFFKQHjpIRhfqO8AI6oGOuHd-kADvM5xQKO5J4wD6BKmpXuWItW8pE0uq1G4-3ePYj2nPJEP40mpiIzKvjCGBIoKnDyCIYTbNxbwRefUPH-7JQ2gei_y6hl7to3tFC46Yjqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyI0dGvx-QpdBVBVWRI3Oyc5KVQYuHQHO6efql_mq-v7QjbnCPTr5W2PAVe8xS9ozjjlM8q3audBd4MsPQgAQKRuWVolBfYeWqItyJhlokl5gDSEvthU_2Xz5e9p9wDUT4peDFlsh8i_az0rxVnoqglEAwjdTPOrkk6G0YAtXaPIVX5eLXWVdtU_-Ubk5GJP3K9oT81Vxt4AbpmKKJDlp77kZgSaclHhdnYC2loQwexIEyNl6x4Y4ooTs_u__lVydhOgKXlhVJBChISIH-PGU5lxmilw28ktPWyeqKBptKi_7Zt4zdSkmeJcYYkVs_7l4k2vR5K5wRhsrTu28iYgQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqVfyoA7EG_Eb6ckJwQADIRaWQ3VuJ9GDu4sIf25ATepg8Y3iGGIcaxxNlMP9YUi_40962aheukKMgC8vym2Evxi3yaIjwdH_MfMT6ZOe4unpHuhLHS3HjSiVbJaont6qdQ6GK_yFwEgIcFFfrGUPegTlCFAhJz9eYFpMcKpyUQ0Je0FezjQZs37lURIP_vxMSB2BTLmEXq-IKadFm-FWO5J2CSNTwaKwlEFRkDrPy6cJEYVTcgZ1BCHEGZLyr8obJPiOskcBGjgZ368-7f-k1T7zvkSarqPotDDehi-Az04JLLRUGKukVrA25TSV145jmEmSVOYWmek7Nf5WkVi2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZfz5X5evhaDwD1GAe4FitdPDA5krG08epYE7E3Zzc3e76Do8cfvBPJVjDAynnfemvREQ1SuvqZt6UqNTxeBL-UHw40TRfr1ajzgZAJpBxUfoN23rvjdVcEc8Oa9r2AnApw_Ogi6LbHevqQ9rpSIflGsiHUcJbUwafoUelX_HXYDFUAp7SZMFN_u1WNyPA-BZySuhIQ2JzvkOqv3yIT6dp3LWdCdLEF3MttcgpzBu2jWu4YpYeyzthbDFINGld5sJxxv3_JO3LuS-JL8NCKHx4HUTl8hFqDlgHvMAKPwKCS-5lNT0WjCH-pPZLRdBjLIkxWhX3kwCG-U-VhdbNDg-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZERfkFjdtemned_Jzzi3jYV1d10Z05e2ZwouNGHp3tE_tWr-XlFqnXQfl1TUM04tVlEva6M4ezZ7Rt7Uj8JXGdHZhBKM0UfMHEmf2Mzs-pK4gP6D1qh7hBXJEfWgi-iTsdgYDwHT-5RtaDHuId8LT6DEEmr7hVh1aCus9-hA8Dzr1EXdqE25HixCyvs_feMnrHyEv4bOWJAfpD0lXckxBQ9ylq-YuB-fmlovSFGlD_INLTQugfu6i0a70Vk0r9D4bRG_cNF5AZstswHjNtkcJ-lqUm9FBKqQtGu3Xg0Q6Z6jPpCMrpjupImacMDgbHjlDfFeUfYUC46fHBwiyQmq_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=FkpWL68GafqzjGwafGt8Kh8WQOlSpNn_cLAHsx6zmROJAKLK_QeLfYBn59-1HqZ38FUNDBByfDUoUbha29VK-H8ChJQqfmH-PrMoLyBrcBSfRTloMZr7ek7Hn850J52YVckdkoOdP9vwWCDC-0dxsBt5LLZDW7KsFBBpjSV_aYrq8pEBKR-aiNQZCaHBdbl-SehZUn5MEo1i-ICUq1p5m7SH5HZA4yb0tQO1oXOoF8sK8s0RT8wSncDNJgRYi2yJW0SQLx84GpSCjHGHxNmTxwU5AqOCyquNmwskiQYOKnZm9cMa0RVvp4WeiiKq_Zd7TrFQmAlxdwD6IKKmrVCCMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=FkpWL68GafqzjGwafGt8Kh8WQOlSpNn_cLAHsx6zmROJAKLK_QeLfYBn59-1HqZ38FUNDBByfDUoUbha29VK-H8ChJQqfmH-PrMoLyBrcBSfRTloMZr7ek7Hn850J52YVckdkoOdP9vwWCDC-0dxsBt5LLZDW7KsFBBpjSV_aYrq8pEBKR-aiNQZCaHBdbl-SehZUn5MEo1i-ICUq1p5m7SH5HZA4yb0tQO1oXOoF8sK8s0RT8wSncDNJgRYi2yJW0SQLx84GpSCjHGHxNmTxwU5AqOCyquNmwskiQYOKnZm9cMa0RVvp4WeiiKq_Zd7TrFQmAlxdwD6IKKmrVCCMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=VeaUEAUjRAZf5cgbG6dqjwrPOJEXpD3M3i3g0EDf0n2TaN3Pn4M01K5nE9liScka-XCj47EzMCWkupENyc9n_wGomx66eflKUv2uMZZ5OKhlppftG2lTA_eyltjYDyNR9Cgc49rwSFAz_fIbD5SBmUPkCYNMbY_aPXbCvSrtLUEGCEVhh2RTwqH5L7NdJIk9xVcFJyvmUPNc1mw7kwCyWwdz8xWptrLOQS1I9ZgFPYfcChqQ9OgFGt4npAmLiGyNtUW1uHzpc4VXsZqNPppPQKcAV-G2pdLH7P-CXobD4ZcTeRjQg87Bo7qhUogfxDnhA9rQf-kAAyrUH9H8KtL4QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=VeaUEAUjRAZf5cgbG6dqjwrPOJEXpD3M3i3g0EDf0n2TaN3Pn4M01K5nE9liScka-XCj47EzMCWkupENyc9n_wGomx66eflKUv2uMZZ5OKhlppftG2lTA_eyltjYDyNR9Cgc49rwSFAz_fIbD5SBmUPkCYNMbY_aPXbCvSrtLUEGCEVhh2RTwqH5L7NdJIk9xVcFJyvmUPNc1mw7kwCyWwdz8xWptrLOQS1I9ZgFPYfcChqQ9OgFGt4npAmLiGyNtUW1uHzpc4VXsZqNPppPQKcAV-G2pdLH7P-CXobD4ZcTeRjQg87Bo7qhUogfxDnhA9rQf-kAAyrUH9H8KtL4QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnPcdfNaoyy0HHnQJfzroQ9F1JMJylWXhC-HBR0sGAUpyCEuTR-HZ2241t6MNvhTvT1q2aHvkiS64_2mgObKLsubYCuNYNYJzfQdnCpdYM1WptemdMXoHnDONVpoC1mry13Y5eNwRSfQPfBSoNvuZoH6IWPfb_QyIfbqnzHWdRtQ3k1P1OoSNffs4stHxP4L9ph4NwEJ1t6sqfJhm6KoFYgNTBDi4JVwJDS8RsIetRm2RGJb2ZPk6M69eDRrp-9zROgy6-FjHI94GRisnnUQva8AYIqhFaNgWfBFsEO6coue-eJzBDmQoXateVT3Js8ucdN0NQ4iAedh5JO6y4eBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2inU6iTfXEWFMqkMBqEDe94P_BTfvNCdTB8HcFpuJgd2iOQ626LDqd_5TR6jwz4akROXoJZV7R2O4r2ZOUnVZ0PmwbGVV38kXfnXP4A1XOkSf2PczxOGi0aw5P41pZcE4YvWlLGQ3kdF8jsYVp7R031nPBl9Wc_yHQTUJqvklVMpfBqnVxAVfEuTJWFVAdTgxSJmRYJQqeueWviiQQ-bNturhdie6GPS4IdZZmJrUIc27AbzdAU0ojYT2fHYY9avIBhEpkJZJDDXssZcdTQgiXLcVrbatOGJneQIddXeTuxwgS5FZLvkgcj8Q3NZAnci1foS7f9HGhUiQkeefaPU69nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2inU6iTfXEWFMqkMBqEDe94P_BTfvNCdTB8HcFpuJgd2iOQ626LDqd_5TR6jwz4akROXoJZV7R2O4r2ZOUnVZ0PmwbGVV38kXfnXP4A1XOkSf2PczxOGi0aw5P41pZcE4YvWlLGQ3kdF8jsYVp7R031nPBl9Wc_yHQTUJqvklVMpfBqnVxAVfEuTJWFVAdTgxSJmRYJQqeueWviiQQ-bNturhdie6GPS4IdZZmJrUIc27AbzdAU0ojYT2fHYY9avIBhEpkJZJDDXssZcdTQgiXLcVrbatOGJneQIddXeTuxwgS5FZLvkgcj8Q3NZAnci1foS7f9HGhUiQkeefaPU69nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Y5Iqf9cSwZqBF9FfW2ng9giqVVF2LdYts5Z2FbxxBCMCqW-JsCw1PXVgNM87WC-nYdilJWXCDwJwirF0zMhYH-b5fo0mceseNA8EaVtjccq1Og7T1WmuyDRpJz8WeCIQafub2XNIcFUxq9UTVGkm597WBPT3dha6LfWf2Co5bW9kjW48gEYCMEyJI8MtkUOw-evx79Sd76MEuYUQBBqfrymGLjB4CvnVVfSYL4QSs-KSwoO0c4WyqUWNKwxRKygCQY-I2GnoSIoCQ7oV3kxqo5EZVla_1RQnCypHq0JBxhyPDqEv8TvIIPxtalFKWDEGpr1PILbgtiWVvFm5ikFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taq-95ZL0XCrQnH-00vMd2agS09HJdS3fVN2uDjizxtSg7gvwgt-Nv_7gS1wyy7W2nslJjWLKoAAJSO6x6-C_KXJ3J6AfHF-MbZl1aagyjnwSIvf2TJcll7XzvdKcaDqs4RjG0Bk3rui-43C33K05WfsDd_-Ds4laoUBZ0jAkzX_g9lbEpBR3TTvOOT6ZFQ979_Ehr6Gsg-yc0qWJLKgRlrqwtg4JJM9O26_le6-SiM2DD0pYombsKNaM_HIDEFmTQUV_ZiFtUcLHbZg5cxLOLJ5p25vXWyhTYpgzdg6qPtybHzCj9wGRCPuxy29JCKjkFtb7FaI2FZnJPEiZI3PwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do79ZFRs8bqGoe8Hb9Cl6rlQSEF_sZOo62zhBdIw-tcMTVYL8LBidPmoUVSVUV_MF4eXEsIQW4PetRlwNuq2MbgEY__eKMISZkzrez-RfmMP5Kk0GMzuQcjmaztqtGG8YTweySbcqa-KfTcFA5pRq4GxDRESbe3MQLhfJ928EYMJf8WZ7x8WLtx8yr3XR1CmW05PKuKS8YWjxUXnGSmhq1SkJSk3QVGCpSvQvxyX4KR_QDMfAlgJ5TJZ6dAgTjKWbTnlUxnu3PyxyzwzCDGy6VerFcPHUzWll42xQe5VQgYtxtMljCf6Bah3D5vdGky-qggoxFDp20PXEd-D6S2Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLUSAG5RgDwsk65ecLuv0xXahz0OXuIBUKRqEyQdYiFwQ-qi7A3SzbymdoYbWUHd9Tc21GaFbg9l8iL9fIen0ZrdTEFtW2eQzLHpQ8CvUzeGzlPlR_KlYrH0z7TT1Jrqlh4c-aJfO6GnmCDh0higv4EjuyF2N4oKbyNOD4awMC34Q8CP95TxStz7ZrLM2VhlVQkdM_c7fG3RQgjyq6AQyJrIpCfGvMEmIaYyeHxQDMYu0LwdOXJ14bKJtwA5mCZFDMwCY-sPh1fMAf932WOmcO2pLigNtX7ZwimxWMO8y30v2ommLnIhQFWslo2eKK7GxWEBu6eMe4lfxub4Fptimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH33Dau0V6i2ATtTVeAxm7b3jdfU2NjGe4frNFC625AT5Q1VkpTkBl46q7zYIUyGgSLlZab5SOycdumM27xjOB2MWG5LzlbVZrbQACMB65W1gmtvNurDLNIb_p_0-Cgu_I_-i0vvSwEy8YmWoKNEU8er09I1MunfkIkE1v00ZNKkpVA9BEdH-hLtNUctmkJHPd9og8-xO9neMpctFhOLEBlztsTFyI0n9NHmqYl0NfHmgpAgqmz0N59NicVAJIiJGOwP9h-WAREnyOokwLY9sLvL9QGdh2N_TM9-tyMfmZYEPcpk7okPgDRwRA3g8qK7fEmXXHV3krci52PIJ9UKfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6iVoqhHJgSALHr9SWozlozbaTQR4h9RLd6aMH1gevABCTiIjio1WqFUaAhAeoZdnmyRLS5tjegvBxHicRT0BnlamBjg1H11AEF8NQ1VdsCiKL8_RyAnzRzQo-NtXkh--VyEGHb7W8KPlMwkhcXtmfKWsTZu3BKmYcxyWo-nJpNrM8gfH6_njsyoq2eTpHgGol21jUt3Gyb7jGH6Wet3r41rE6UaAq9-wcwKUXmdDcmIm3aHYW2jlTi9ZuHZY6KlwZ7Qnn18CYXdLom7zqlfJzU0n0awfI7wIFMTi1sWTqLBJXHJS7MeOg4AcJE96GG8uMJdsSUfC8-WnlNN7KkTKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k15yjgRfkSnNG2NACZpOa0tigNz5f9TnikBDODzVlimr55GNgEAzPiawCb-8T5795HCD71sczTDSVxYh5RlOGONsEnOsOBMSUc4SU1vU2080qdvn__u1cO2RwESdRpLeFRbcsINVqQSMiMiiyMJA5LCubQgp7qx4kffdK5U9SUITbKczDa4tuo6ngPpuZIHG3GbhnpRVfgd8LcZylpvTtrER4XuKa2FzChqo0mrIpTzuhJpOW6gR__EX5bAdBbZHLs81Mejjy7v4WhNQTGEqkCbhOfeWtfw1hovCp9VAMXc2mMreaCaZiKuA74jjbF3XjB84mqKVQVrp5NqXYTiOUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8u2c3Vmva5yxTyAvBBLdroBWv1Wehh4VHajKv2s1iRyS3kywWH5ujPEmNQKKFy2bhWCc9_4-QD-PtBIturDMNXijH69w_V_3MQIgVSViRRyYPoE-y1adLCBzPt88IkD7S3V3-jQ0FwSoYwald9Xcafn-iTTK77IQ5SZMlIVen8hm8W3FUoe9_kgoodBV_AjIzd04XNlpzh-K55qygRmufoxmCGR20FKe9xE_GrIfBPSPqgCHWRjT2RVls-B5ynKrCVKv4qONYuG49NfKCKdssNLPEaMtxfzdN8M8dZtqnoVaax57IPoLpMpFDU-Gj6IvSbh1DUb5lXGsUHEor7Yjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdgtB_l5PhsFooQl9FBrgKCXa_0cFHaWzYNvBjYJ2BOedkTbjbbrsKc_nQruEhLJuoVGzhxqyJ3XvGgyNIomH-KjAkXTz42rRZIeEYz11gcorlChBLS_HQOIZszPfpq0PiGnWt8FgXYlyufQBj2P-WUcbh_EkGoLVN3s4DNeUdR-5IK3BzTfic5CGAJbsUn8v3alh61LglNaBtF3z86CNt6JcYl2a5xEq1f1xbeV1Y042sEM7k44ey2D6_01HXB-pZjoowkw0yVStPwMA5iyhSBuvUbMyp7q3ecypurK_rkxCEmXKlh8TaNwtsyyA95wlKPq7F2dgi8mbQ_eKPHF5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juXkSJ15QLAUgJ2uLjbpitMjODNgRsclZu7wHxbnK1V1VQ7HBgp3IBQV185XtlNiKNtD2Wqu5AjxaYIXTfDxsLniMmG-wgV6Tg8OViIyQ6o4Ur2UJ6xOv0cefqnv0LEM5-IIkgKofgAqW-KS6qVJs1mtOLu8s6HbjmwRJTDcIgcC_exqV_iZA8eHaEz2pdgHp2KYatkKwEZpF1O_DBoM4kU4Iekuw1hS0dNFtCAflNP5Ln7Z3XPrMPisUzQIgvTQKOfvQ_HWwkuK33TwbkzUOswH9o0yGzJTRvIG6SgbcZqp_T5PcBJ4QfYDr5gAcbMwtf8vQuwd7nOh9YFBcAcSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx5tz07P5Hl2N1l4v5bFle5qAMgD9EpWaNgvl-Do5KgZHPFXVgGuLKeYzD6fmaiD_d4oDo8cRGn5DzxjAmsdQeQNJN9r8Zwq_t9GrOPvHDorpwtpk_uLNcRU1DmxRAO1NqoXVB-uX1aD_9b3O9qgrlRCdA8Cm6GrwvJsFR7BW0Vglj2jxolkuo1SS9B58ymF-2-TMaltNMiZ0mfpncksk6AgDPtaY7VYeeg0TgT-SJb-uxthkUfBfbveWKJkmnxp_T_O8EJqMTKpEkBGtHVVdKPuOh0Wd8oQgIk0pGpFVoHlmE3gSWpLu_NiKSdinegS2EgNewqdpTtfA2mztJxh_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WazhnZ_9tvDciH9BV6UrVuhUgRY8ysLnnfTEHZXAYsNqowcWuxxuGhvEIHnqerfZMBmsBgeu8o7wBhZYXbR9FS-MBuqpTlccvhsauIGRhur3WS84mJgkUFA_LuQgOICHMPf3CiU-Etv-EiYiZZm6zP_cXDNWEUSXRXvw3jzmTDPDgX7KCw9uLa9qhPpAvLwdRWSPXF_ujJWlzldVDqK6O9u4kC7cApdLz3r6jQ5Waf4cTZPXfBdbZafHB24h1mst6eJdDeCJ1SUf8pvyLkalk3Uk7usfzn52P83_1pGS1isvNh-4e9w3MJIWd8GyemHbBOZlIU6GldV0du4pKfhq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ng510ha17ucOTo6Hyx8-fF5IswDgLCB-9lpI4e4ID_-wz5IJ4AqOVji7zbSLudWN_8SdBXRWBekpPsCXFoNkA7fvmFniXmvb09PMvPc-KbfRukUJZ5MsIFCKSwnGlzQPnFTZIggp6U8Zr9rOHAIO9HCREgusXqViUTA8kcenmJw5T8N8TFD9iU3qvjZrDafTBf99zAVR4fwAgUgYzlt6pbK7uSIlMMGMrlfU8j-Kod5HN3raxdTXefq_QO-2moCNAHs-3Wgzt5JPfuAQbKYjuK6EnIogZ6hvwkIYgS53lS46W-SdnucWyqldI85pGl-qNuXMTZp1hfJ0caH-6aouzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFW76LnjB8oVW0WHSWdz9tCVpIjNuwa8j5Y69P7390j-N4V2wpPosKkku00K2QAXVezpfmzIfzXNsPwlOMgIBc2amFx-zaVcQd1SNZjTGTa4-s-vl3zmJK4BJsB4OzgVhib8S_gm4q-MFtW2g557P1rSVfPNxcRpKhHqQ30KLXE1PSa9cI6mC87XAjA-RzKCVQ6p9SfxG7yOQq_IV7x27Pf1S6wILgYyc-HzdnjoJOyAep6xrv6zf16et7LPHj45dhM1nUTKlAnGI-huUZLi-uDwuArgw4yHzoJfQwjM6nF_FeNjcgr0AbOmRpr7RAXErAXaZesrSekz3AHjQB4F6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp_8t4AYy4g9eZs5bu3l_-cYyaGPjJRHrYSw1t3_KkZMPQNJSfEyV7MTw5bdyJrapV2OVfHCaf2QS5dN4N03bp0aDYcpd2YNtVLKN1HE4tCGpHYShsPE2qh3OaepbsuX6Wt-4Ts3ajav0pPM9qQhMwz1CjJVGOallPqBPYakQDZQJCQMij-RGZ-q3dOzD_78vloChmq_3gG1o1GWpVkWsLdvRlYCq3rn3piXUBI8_rPf2uA1_pQ7j2Ht5TgDLT0h_cWl4cvjd_IHTwvr-n5ZdCjPWCCclXd6FL4fRP96SpvAGEErgj_I-PKY1mKbtY0nW3J3MYbMHA6BZObeUVUS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inm7wL3GMzpL3PmTHQwJ_IVtCsdOci_baCJwXEwekzgAK1BSFMykP-3AACmzhAELG3eHsZeeHN2bGmjoYcIyGpNb_fKrAI6XsPDje_mB_4vPVsEwelOzSpTfz1IrKwXrS6jlAqF1ZpiXgZDdKZJ4zSmk9Mx0okyAxhxXwZSImNVK83fjFan1HJRA6cEsDxkMM0GFrivf-oanPbJkMv9AQIjGwI2MlIePKwMKsNRB-j6xCv0w6QcOE621UprhmSFpYG6Nch80i0jLdsMk0IT3I5S6lZCLMPdUB0D1wyUgzi_rFlOMCZJM__qPx5aHLVgeSDaCCBoFjJ0jBl02_erJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdNnXgbO9JWAiceOMvP0uewxcHeRRy-ZJW8l_zwdl8bgf1ZYkAXdtlFPZ73j-I8w0WjoZeMcHVHqP1W2OFfOyNKgD8QBBQs7VvVf3OaQrus0Lz6yApkASj5P2ZfZCYFxEkUNTMv-wv4wPBUr3gLKUxHhLYWSc9QFeTdoxbZjq2YsHwb7cjbeBFOkuQjQytPxNq6IpoGYNjgLe_DzamHcSpDJ3GxawigEs3D17R2v_wy480ZHRw-mWnL-DV0D__tlDkY6bpcDXJnj0xe54oSm0HtVZubYhDu1PCjt7KF1_S5IJ1ri7RObesXj4gDx7C5LZgT3Ura_WxHzDq9Een3RYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFkFlEUzXphO69c5lsCEQCf1SDg0PY2DDUCXe6BG8QUMYHJ3rzgJWtw-drJhBJRFkT-0jf7aVML-ZnA2kJh5ONpYKSzl58UFydUCpUMgoeJvNfKkSdeiv2JaAyXxaRog1Rmsu189_G5cotkqLUk0BGnLkWaUGYJX1TZzIe5ym-ot4vg4a9S5xJ1RTBdbmj_quTizDwjzN2JqyA8HWd8QFcX45YPjK6fgvSbBtP4jAXb8GUbJtJ3ICxsIEobcO7715UVHPfS_ly0LggjWOGVIF7d5opQkVHgSin070pmxT1QFl0qVVm1k54KrfY9oToEkexpAcxME4V9KCwXcLnBxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kw264c5Au3KxT3FXvA8u4u6yf7WJd8_xI0D2t5Vrca50R6rJh8wSrs6gEqKbJPhvipIR9cff2gMlRD8H1T_hDcUcTdkHT_gVjX3vAgxGZlgMEzSLM6ey2oT095HeR6NsXidlzlsg49LmH-duC34SUhk5PgN4lXnkozlji2XuIiFeUPD92ItnznbYGxB6dUENDjKZ-g0ecOFubkRrKSM9j3to5q15JIxeg5CW7T0ssWKEdseLRnmrxqWg6ZeeoSERBANmzGGygt7TDj5B8id5rg5A6AVg9oCmIU63oK8Rd5OLwb2lnodibyj-ClCOl6H8-jidhH1CVvbRLWoDm8crgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
