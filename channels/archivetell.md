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
<img src="https://cdn4.telesco.pe/file/IR48cxGjLYbgxtud1ZDVJX89Qyp8JjBnLV2UIQMz5H6ZGbF7nLu1jRDln808-pQomCOcZu193cbkDi1pvtzvgYqY8_KU7DNQaksvg3z6tgQg8PWbGXCzOS22rYWPEm6MvspZdLSnUsqFih9w4s3EduUketBDea3xeCdQ_WM91vaWtarsEbK5Vi1cC--zS_i2TCt26T7z6fGx6hmFRHNYbaKa5qEJ60Cr9fIMp_TptnRxaS8YirQnrmnad5ap1R1yH_igt39AxcltqDHePR-cv117171oRHrmdT4_J4qnYz3LULZOOPBSjZ4xVomyfrTAutTCRbNrV80nP26b6wk83g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 411 · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j3gpuMMoffZeK029moaKfq6RzHmQUveJkY64uUdSKp2njjvz9q-uiztrFYhMro52hnZUvOnf4WH7xw6lK04e2eXZl9pFA_YUWnxGdg198B7qlq5GRAD0o5AzFwuwB1drNEPyWxK56DZRpEtGN0jB-ThNu02U6u9y7mjcE0uKLlPmx38p25wsYuTiLVDLibPjjpmQUA0KdcfNhIsiJB3DCl5Pk0ayK5X09Kil4K4YJ8TyvgkoMduYUjRTmoYqjRCzjC_KKtLZYRMYNZBIhMHUw_s8vYJWrKLutEiDMmu6spHLIMar9eDx7FMnJDrvHjt33pAwy3c8l2dmlXrgcLOEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 651 · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WThqnxyhVpo_-R2TsBnB0SVHBqVcfocs5DuwUI61qky2CeJXiykAPu0uyokl6A-P3sqGA0OGs7BS289y5kujEnyz5ETyolPQWAtl3dwr4EWhzZCKfrpjlz21bJUjaiRd5FKxydZxZ0qF_UcJmH8LgmgoabSocOP4BvoK3LGlY8Zfw2rw-VO3OpYlGrsm31eGNcIKnH8-PE0rSrsNQXkSMe6x1u8lZKy7GxtXGfYydoLk2R0h15WFhSL4kmgzE5BbvoSqxNaMs2PBv3GKyGLlUhkLjOlWK5Q5_nsdlk7o87XwEwoGZlUGlsB0fw-2tkfvxj7QmvJtRhKtKvbFLt4Yow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWamXdTKIYHFJyLZIuPtGbuYxuJyAD-01EC-X55CWR_NAFCCBzVeYpNDRLDYrlD9EHOWRkDtP7pryUEwnM3twdkPcOM0B8GglHufqyedYIQcMN5NcLPl6a6V8XinEDg_oxXPR_jP0dDXkJGFzOe213UXXPXApaBOAzFnd1a8VmUSfQwpJrk9EUcWOAtOD5m2iumQc5IrnPJwDnO1a407lz30gWR1Y93uA5HnoBzNGutNhlA23syTKjVIeZn_XW2f7WSBdbby71d8_mnU__fvgACn_DyUklSILGK8dR7_MBBJdvTUoiUQ5w273sNTXwCHWNd8nraKewcUUKka9Vgn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKsBU7SuQZEBp8ItWRlHQ7IZ_dENAuLEA0lGcBL2Hw7Bqp44MReW9_GgKx-M5xOtTwyOD4NTetW9zUPmVE30kLWkJ1UR5jlb02bBbJIAL0pQIYrhv0RRo67arANK3pihXdZvi1W6jrK6a6PGqDwuC_0T8X_C_ZUw5ImpdnGmTU1Uyl50Rb9TpwNuj-zrR-EYa8UmQIE85fheY41XWyEkeXOot_sDWr6J1bRW2CnLezgqZtvCe0j2NyfQokhV3W03tsMrUZrNZdD2Y58gi2FME2KzuXp3eD0xV4PALZ7b7mYU7rJ2b6ehTj4fn6njlTTkroAYwJfpk5M-BR9oqtBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLdNBzZhziyrT7wwbkqfJbLONxHba86hPCOBgkh7bd5WvyYuRphl6KAY5jFBJcuRE8c138oRUcCy_z8ebAjwcog0aVW21ImDHXOT2nh_HLULHdDfCBPYk3lIQZhnhX094kN-7LVjR8yBEqxcQtAQefvvzinTBri00j8S-YTNqwnuNZoMcXO8VANj--9pSPL3fx2i-jb5EE-Z8mKqWGOUE37klfA2sSl3PAnBp0VKZdcAOiVn53klrg1oqIMioQYqrHnoQ_O2YrrWof6sFy6wHwozEVPlEThy59ym4svCiQte0olT8dDhEhaalspBvgb--tQfti0qYPER4FJXLeF0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPRIMIUM STOR | KYC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GooYm63CNndqdmKA7jT59SgqFFW50zeZeu485cusCsHZ6Ab1rctJtAi0eVWrGR0kmqK3WAWgzoTS2z0YubpCJ4Cj43oiH30AIE7_kjmx-6F_3GdRHHsSU4zbaa5DCHB3Gswfy9FFlJwDza05EC0iHsWYNq9fF61a3f9k2OztH5xL1OGHQHI2s8Y1nZIVISJ9Yg0mpQs1GZ2MmNWxrzMSwewwsLtzlBny1wEpSNXtbkIlFxSKOiqHsw6gxQ0-2YfgLF450wJae8ElSUsSKBhNRsXH6r4g5lDa9z5Bj33Ci4KPp1gxwk-Brm-YoXQnDzyP1Nd8ScKyn-u3KZNTVQ0TDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش اکانت جمنای پرو 18 ماهه مخصوص کاربران چنل ارشیو تل
موجودی محدود!
این افر مخصوص مخاطبان چنل ارشیو تل هستش!
فعال سازی روی ایمیل شخصی خودتون بدون نیاز به پسورد و لاگین
18 ماه جمنای پرو + مزایای زیر فقط 1.5 تتر
5 ترابایت فضای گوگل درایو
آنتی گرونیتی+جنریت عکس و ویدئو(1500 کردیت ماهیانه)
سی ال آی اکسس
1.5 تتر
خرید از:
@PRIMIUM_STOR
علاوه بر جمنای اشتراک سایر هوش مصنوعی ها هم موجود میباشد</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7714" target="_blank">📅 22:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7713">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7713" target="_blank">📅 22:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhwccVpbUAAX4xpVzq1WqUcke9HUMPpLvVhXiudWrZ0e22jh8yE_jxrBnpTyjRjHSxhpJtf39JTO-KNwF58tpfRygW2a91bgjG6hq5zM4cQJqJtq7sr1CZATmqhg3XcNkkXlh6Mkhk-qLgp-FQKEan1KzkYj0Sf0YSGFH0j7NeN7mFIi5iTZBBJUeZzLjYrRqZeI6C6t9gh0_B_Smdp6pvIooigsH-d1GWSsC0jd6vcI1q6mnoH8TFOQJTNqguGxNuu03Muu-fKQgnoBqvsdsmacPHnlAMCPZeAuZACZWjciG73e8Vm9-o46BacvhM_ogLM2zk6j1DmZwfgA4M2fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmBP3fMr8CDBX8hC2dAkp9UPtG6NAwpT7PuzT06afYR17q7wo50crkaWqvfkJDiksi2ZWeqAdZ6wIPQ-epGhmhFelct2QSfGDBX3gTWl7f7-sT-tu1v2rihN0rjiAAMGoH-vvJeCPIZOxZY1QTLgylEQBjLgmAobqhdb-14EkySxQv8huDlKF6Ib5uLZx-GQ2axSeC0xqEFm75pG4hOFt9620H_b5u8YoK4Vp7JJTj2dXpXX2oJKhFZcIY21sXDhYcFCl--0n4IFIFDqRwet1JBkCiFyRs7BSWnlEjgvzwjVjZBlV8gfxbk9iLiHB9paQ8PRpDpVKFgnBiJCuTcSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN0TtpXG2yILZ7Ol9OGmvBAT9-C1B2I_4LTsuWG-C4crlXx2l-lWz3t-Wp4rOlVEt7uf1hyW1oq-jCJG_Rs99u_Cpbcm_U5WhuM9Vps1h5GrYf9OyIjkVgZIFyvXoR7H4KvDIHMp6QJPDEnGSFXN_BDkthtQFM3WYO2i5ieVp96WC3_RBK0iPCoIIwY_9qfvnBv53qydeZsLS0IRuNmdfijO3y-cQ1QgFNpiAvobk64jFexv6mgzwD2w3rbiO5HL4GTojw2TJ_45yMnDqSYbWY6dPGsIbmQLOEsCCtgCf9nt_4zm5wq4AcmVm_7tQPPYXSQBbjd8ANh-4DnrpoTOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-2V8yTwxwCwHU76C5ss0EK0D48txwiZ08DZj9jbmv3ChzudwPMZKFXWP7sacgiR_MArtx7Qh5pSJrSW3vEX487CQF4f1qIxBpgGzjB_38ErUaSGfJZwhYWmLWqW7jbIS4R5BmcS4PXsPq9tr1aQ3f4Fljkn4tHwNltIr-Qv9kK5tTTl9gJxfx0rLoRbAhRk1jUFZB78bELHEXUX26PiQKNH7ALhBPMMhXiEKtnxG-Pyb8JM2oYMZabGolRl7NiLrrqfEVnCY_pLvf6WxegQgfBRb_pAX32PQRgqyWwuQqsHVTD8tsvUFs1DR8WBN9Z8QiunYy8HdsHQxOyVQdYEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw8-Gzl7S4IIwPg77D6brzAQb0feA-kw3aRvCT-VNb2TBkl_-ObMzsiHtcqg1v1mPVU33cwNmfqKSnDCk_bHfEDZNzIF5f_w4eDR1P7DPz4ymWuXVtXdu8S7axi5SUgsNMKEwdGucP6BAabCsb7mQo2p1sR8vyieFHCFdCW6dzNLdfr_4HdfPMdl8sh1n7g7uZoPgbwB9BXxOKCt2kdg3u_Vc96C8QjGpTuci0GSHgqTaFM1KqxMvztPSsfiW0dUuvrQL4LLmok_OZ9i4-OhkCj5t5b2bG7Xpvj7675V1XKyXXxmtIQx7R-VSfJL45WmVOxkHKATk1yxhT5Za0dobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avEAj8xVHtivy9PRO9fChk2xoRMQwWLOuDptrLL2BfjZUJDmcuZNuRsDNw05hoAwRVFidrw1DpA647ctasbuj6hwNFWsUtyETPEEGQ8RvgUOeJ9GCahNVmrWsfCE7eyaKYdjwyPnr9-Dg2TliTWuXuCR769ab3hC45WBYNwwPjhccrmgY4Prg3GPxMgRCOlfcP9pCJ1muLP-uN7GxndkUo57fRfA199C06BYgwzCioRm5FCaWYsrAw9-3NJqD7oxildha0aXKCXI_HQOHytn0_wAZegnXeWNWb18D8oa-ipnOY3uUJlzrXSt2k8QE-9nH2D0TYd6izMfbYuCb1HJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL3PoQN9TgSYt_yn7sbempkYSE3skSuZN32C7z3fmdVUN6CoamvZJ3JDhip4wu5ewVAwh56Rk41P5RydYlbm9eaQojD5NykJCpFhszDfvynFW6-scA4HB96wXhuKt2Ly43B0uOJyFJgoiEdoQfR3zn5DZJpZN94COCu8lCrhkafgFXbzeTHjD2VEi171ImhLVTi_7j3ZBScFF0SkdRlba4XpCUucRo_gucBXeUjCe04xAQdeudKBsOn0h9Q3WCkH7gv-TmY2xf13fv7sl2Aer_rUc3z3oChd5d2jPE0NopPueSdTnrSDYrP9pY7Wn08JaeeiT4c742qxGHoa3NrOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKCtRE9kk7-zH6j-DHe4SqV3EP-FdFWeLWiGkhnlvCIwLIJltNBc7W8hjd_YCKbdNAlRksEZMd43f-_qvm_OKJg7TBpkd44d3XdpkcHkYz4OKb8q7DQMF40mWfn6PcvhZNcFApTFHupLoZ3GjNi8q0beQq_b6OqEfkNNuR12Da69lGCL8SbFpuSk_SbSwmCacq2iSWuKqN300S_O70pk82qwsuF25tZ2S1kIWJKh58ELFga2ADKH_VqD9tHDPFSEbwO2cuvPV5LlX5o4sCImDrFMXV2uvchX7rFI77SLxSyXUFHi_HnWJAPNXtofRdFKRy6cNPh7mgx9LTCTLXcsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2ZfaTzF9wpm3q8J6yiC1R4fG0RYQwdGeis54yzeGpgjbhVQ8PpYO-r81LlVJDuHvo-3KLdP2X8pvS0iaUc9QcNBD-Z88dGCXaQIZBxtjSR06S348mpRgtOiMWrSkJHI1Q9A-nTWNnXEZ9p4rLbe70trG_0qPBYbf457y-23sVWxQfjVidsUzWN8zLTrbFCnoxbaAj575KYwmxLQINFpb1zQ52UIn0XxHfxJUBQ5fK-xR92CKQER20NV6kmkwUMcvnHHlh62523JlsC1WpoI7M9rX2hD27M1ilHTX88kAe4VKwVovKMIrQzRXGjDuz4iA1oE6OSP3A7fytpHQtLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRlIXiHv_8RtMbyK-xzN6DmfQ6MVWiTkFD85j8obCpJ_uWQ68LSoxPriGDE3e7Ie2Rpgb1x86YVCEYxI9B0adNgC1A_5Swrft5HI9gX5LnZpd5HrIrciBNHg1nqjc7J-JlxU9Ti_3vghdwppejp-ipTvtmqgtK-Es5xrmWuoVZHyuVpXenX3MuJAA4DU_FHO53Yz9QV_PQ521pKJzQzgIE58US0WHmhA4hyd2c86DT1YcOCosbb3tJOYybvuh3w6KFSWovk2D5DCUy5qnLQsZZc0xZAUypOF5G5LFU8ixgPh6rBEfRUG69Gbyd2n8zUP5bf3ezusGrh9G2G4zi2E7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=lklY83_IcgvSAgpTRuB6JvUO5Lo3G4pM5omZAEXYHizT0tui25s0fVrP001C4THYHRONvK5okbdVn4oAPk2KqWT_6GWoBXeMqqG0W9jQHTRGNWGR6Jr2MxS5DSJcffdlzUpAsX2lbo8JnUumcktNMafe484CbYXqiRREn5T_g-WgWvDvK7YD2hrkVAWVJDqExZ3EjwDWcjy2A-c6nY8vlf8Z2LChcFdHZg_ikSnGanKamloqYbpfPw4SGF5o8bc9TqqON7kOWdaXK7wd-4ArK74VJOQJUN8WA4nwKW7zNuD5WE3ikKF3XvfLRiL72sFHeG1xh3sGMOeB5tKZYJromUWx--hE_A0DZCp2_gV4PndVfJbWsBjqCRQ7nM1AHonkPsrV5GZiTKIvDgziaeB0Yubh5nTVHQwLxfIEu6YYgG-7Lr3fJbqdSHn0zNP3rqqmv0UwOiy0gKxSfJ1WjeAEAs80d5geqsD09rY4X0rqVrqVR6QO3biTJxv2dOlZWq5X9Q7JxNYjW6tJ1M6f6HAxD2_S46XVN-wx0j_59AS46r5yOZr55wO9OzgagQJTEa79GE7YbO0TLnkpqxswdD5W2NKkZT5PERU1RYP6amlBXZjBXCIUa5Q8XtcrOguqFy79aW9ncvGeAHiUTnQFyb5EltohMp-47I2bgQwNxfj7RGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=lklY83_IcgvSAgpTRuB6JvUO5Lo3G4pM5omZAEXYHizT0tui25s0fVrP001C4THYHRONvK5okbdVn4oAPk2KqWT_6GWoBXeMqqG0W9jQHTRGNWGR6Jr2MxS5DSJcffdlzUpAsX2lbo8JnUumcktNMafe484CbYXqiRREn5T_g-WgWvDvK7YD2hrkVAWVJDqExZ3EjwDWcjy2A-c6nY8vlf8Z2LChcFdHZg_ikSnGanKamloqYbpfPw4SGF5o8bc9TqqON7kOWdaXK7wd-4ArK74VJOQJUN8WA4nwKW7zNuD5WE3ikKF3XvfLRiL72sFHeG1xh3sGMOeB5tKZYJromUWx--hE_A0DZCp2_gV4PndVfJbWsBjqCRQ7nM1AHonkPsrV5GZiTKIvDgziaeB0Yubh5nTVHQwLxfIEu6YYgG-7Lr3fJbqdSHn0zNP3rqqmv0UwOiy0gKxSfJ1WjeAEAs80d5geqsD09rY4X0rqVrqVR6QO3biTJxv2dOlZWq5X9Q7JxNYjW6tJ1M6f6HAxD2_S46XVN-wx0j_59AS46r5yOZr55wO9OzgagQJTEa79GE7YbO0TLnkpqxswdD5W2NKkZT5PERU1RYP6amlBXZjBXCIUa5Q8XtcrOguqFy79aW9ncvGeAHiUTnQFyb5EltohMp-47I2bgQwNxfj7RGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=LB3gbdk6zqVmIT8H9rBiH314JXShMKQplPbAYcGgvzltPzZuh8ElAkKm8ozr4IdLPVt5I1yWL7mSI8eHJkhRMQCpdO-69d-co6ReAQhtg94SVWPPAm5kTv9vclVNwJdQ1PHGwkpvCpW3FSr85bRRicY6TXGvaqokcV-vK5Njac2Nv2mk2LlmICCBr2J1szhOLcy6mySIcT51_APIdJ0d8OqRcQHXQdoSjjlXakBA2sDx9sJ36fYNqjuZMlMzXASm1nmYB3S1eivakUS0nHQqJktmc93vhc7lkIg4R0Oo2O-jDcgLq-wRD27QVlgZpKl80oCrYfh9QWdoUAA6g-n6oDnML6xMZJsefM4CyKiF6mMwY1YXPiQccCIAwYyRm0aXB09waoH7EsnkEcn_RMjhYIp6hFcaNyppVCJZ53x-A_fhsVVijktTdLGAAEi6IDOcQb-pNRNynJ0z8VbojAJkVUEaumOMPmAPFAVkaYIVeJug8yyQqqOQjYlS2MeVg6odSFKIEKSSrjwrkgCLLoCe_M-fMF7iBTyL9JGmoQJlT8fDmpwjsD4Ds3RsEOd1TDRRuM_Q639CKLBTcNSeoxQP2MqlayUL7f12AFOnahivpdmO-1PdkqoEjDKka5xApGxiRh4-P2k-IUfuQR9NdvBB3KuSuQr98y0FARvb72AjJ9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=LB3gbdk6zqVmIT8H9rBiH314JXShMKQplPbAYcGgvzltPzZuh8ElAkKm8ozr4IdLPVt5I1yWL7mSI8eHJkhRMQCpdO-69d-co6ReAQhtg94SVWPPAm5kTv9vclVNwJdQ1PHGwkpvCpW3FSr85bRRicY6TXGvaqokcV-vK5Njac2Nv2mk2LlmICCBr2J1szhOLcy6mySIcT51_APIdJ0d8OqRcQHXQdoSjjlXakBA2sDx9sJ36fYNqjuZMlMzXASm1nmYB3S1eivakUS0nHQqJktmc93vhc7lkIg4R0Oo2O-jDcgLq-wRD27QVlgZpKl80oCrYfh9QWdoUAA6g-n6oDnML6xMZJsefM4CyKiF6mMwY1YXPiQccCIAwYyRm0aXB09waoH7EsnkEcn_RMjhYIp6hFcaNyppVCJZ53x-A_fhsVVijktTdLGAAEi6IDOcQb-pNRNynJ0z8VbojAJkVUEaumOMPmAPFAVkaYIVeJug8yyQqqOQjYlS2MeVg6odSFKIEKSSrjwrkgCLLoCe_M-fMF7iBTyL9JGmoQJlT8fDmpwjsD4Ds3RsEOd1TDRRuM_Q639CKLBTcNSeoxQP2MqlayUL7f12AFOnahivpdmO-1PdkqoEjDKka5xApGxiRh4-P2k-IUfuQR9NdvBB3KuSuQr98y0FARvb72AjJ9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0P5qtxvAaczJ35c5Zu1aOSuiq59-va0hEzhLl_HFhjVuNr4VOm9kITRQxDCQRthco-eKIuuhh7fvCp8lZx4_pQLH8Es-F3DZi29IncRdCbNSYpgNTUsgyyCblqIcok7yMfGuuHiWz39zagT2ed0hfTdzjpadyFEzJxzVwT-_X1VMovs9waPR81yMvRynsie3UvXc3ZKITjT_evT4l4uNmPAzWqPy6s3fD94I4ZckNQLsF8gihRNS2F0tF3eVmTJFRnXihTisEBmivtfH7Z6jnSa2iMH8r8shd9bfOyOD4rIlBYFPB5NCPgrLVa7pKTClR88mT9YvNwm-B0MsQwt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=R6YuKO2qnYTj45GJtMnUY-lD4XbD1I4G4Tvh-Bzhr0RPcbcNtL5zjOUgf00EIUp-cPpIbY98SMrSNCgbfacofBoE9Q1oYmdF19JsrK4abZmGZ-vlWNwanMZ9T-RN5PaxDeBuN_jl57DrYjSpbbNp1QGda6VSE1g2fkhq_80ReAIX6ciQe7oWIibQtzBbUQvsvBMGedrTTTzMuHr9UsNuNwGVqrBFsqBjV1FCWwiFKzGIeIDi0JlcEdzxFUdnRkgEquw19oLqeS8BBf856K0DU3rlA60nWE49tAj7WHNc2wrm-xIuh6A-0ODZoWW3zY19kMxdAgnuQqoafEZFsmmVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=R6YuKO2qnYTj45GJtMnUY-lD4XbD1I4G4Tvh-Bzhr0RPcbcNtL5zjOUgf00EIUp-cPpIbY98SMrSNCgbfacofBoE9Q1oYmdF19JsrK4abZmGZ-vlWNwanMZ9T-RN5PaxDeBuN_jl57DrYjSpbbNp1QGda6VSE1g2fkhq_80ReAIX6ciQe7oWIibQtzBbUQvsvBMGedrTTTzMuHr9UsNuNwGVqrBFsqBjV1FCWwiFKzGIeIDi0JlcEdzxFUdnRkgEquw19oLqeS8BBf856K0DU3rlA60nWE49tAj7WHNc2wrm-xIuh6A-0ODZoWW3zY19kMxdAgnuQqoafEZFsmmVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOs0VgMiJ-QjV7zkKP8HBzdPASgq84YOVFnzOceaoJSL5shvZff1Eq1Z2TpzAeMN6Vj58tZqKJsN31sbfTVtJR_O0NiD9Y0ErEfloCkF8efFHZhwSaIuT4nBYnPZPb1PwmVxWSVuonjV9qiyDxDYNH1njCHYejPn_crI_nv2dzXMHdcgP_Yqq1JoKEYaN3YKc4AJ5pkyAk3148FbRhHrqhS8RVi4Wq7YPvACIprkeY9oCunAZjrNdnaKEzQRtl0CxpcFou0j78PmMr6S4_fj11G9j65sM-Itm1A2d3nKyiAtB4OQ_UZ3Rd1Ircj1IYYvtxK-T3YgqHYFRfANXp94zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=sdxw-eV4xfe1JwBc5CIWGTOA2atr_qlMNva-74I_63ES3Wv34jx0nROYjGoF0WUoLHgKE0CjdP1EGfW26vGQL2SzLG16KHsr3qasKDKnWBpJsTBKIb8HB6GIafxwWya_FqQll-D1u_cb2OtyRvq-JCRPYEmgHTMZJltDWRoIVGKmMqJJFfQARwOGUTUWf5saYNo1F-2zgzfBNCEc9PAsufeE2AsCWKdx_JP2KLTYpSZF74mtvFW7uf_yrrLvSPAqJhWqsfFpOdfejXFJMAJwVE2yft5Ck4pou_Y0r6SfjDwrJZtlT2WgpPcZwK3al0_7CpiDMZx7fL5kHfowORpjjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=sdxw-eV4xfe1JwBc5CIWGTOA2atr_qlMNva-74I_63ES3Wv34jx0nROYjGoF0WUoLHgKE0CjdP1EGfW26vGQL2SzLG16KHsr3qasKDKnWBpJsTBKIb8HB6GIafxwWya_FqQll-D1u_cb2OtyRvq-JCRPYEmgHTMZJltDWRoIVGKmMqJJFfQARwOGUTUWf5saYNo1F-2zgzfBNCEc9PAsufeE2AsCWKdx_JP2KLTYpSZF74mtvFW7uf_yrrLvSPAqJhWqsfFpOdfejXFJMAJwVE2yft5Ck4pou_Y0r6SfjDwrJZtlT2WgpPcZwK3al0_7CpiDMZx7fL5kHfowORpjjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKav_5wrmA40PROvSf2lrORwqGCqzShAaNrjUE9oNNqUfllbUnmS2h1rbKF8AJjJcHaHZ3H4TRBgHoYbExh4xrxUhbERYCwAtJBV-9ubgU_HswYfHhrEE4FaP8FIryAijS0Y7HedMtpEgjYxnvgGZXN6KwG_yqMaNFRZm8HVLtcpXjhODAYomo8Ge1bCgfd17ssz8CGPZzCNXaueaSKUEB8wkhK9LgKK1DPmDDjlgSN-zBY-_8MKJP6QiCXnDdnjQO_NIgsaSluV66SolGIAqG1vLXF-n_zWax1PdK_W6-rtNIwlfOeLoQ9Fvi43-urGotpgRHTG17fC0Z-R2Oewww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahw2e33u1LlyU8xgRC_W8Sjw0VsISw1IJhFM0J_DmlwYcT8eakKhi-5jCvsGkP28voq80z8GsYzOtk80sHuRLcQyV9iZXflIZu6vM84b1VeWMMXldN54zBxWXUp3fjXK9bxIW8MwH28ovgKmATpVRw5IzTajfUD0unyjnAZDOCYJTUofnl9sDQxvwUi0wp4efrpxAvm5j-ug1aCzSIL7f3XMWvYmuHevJjk_dGudrJEPcJHP4aMl_Sb8gU6ckMODIOBr3P2vW8gTaEy0VC3jC7_MJMSb5U5_sdGyRzGvqLPtiSWivzdjp1xPVkcnymJk1f2wvSPjbTZsr8ZRKKYV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNfCxhhN9tliavNlXDNU08rqebOqei3gV4ZmNczJ9gr0g7dRrFZTYMspNnJ9TPawNg1YBFy1ET1bf9gxTnnQfyD6x21Xvz7PZyB4Tgj4i8lwYtn86FnKz1xL0l8d5Fawrp3mbQ514S2tjv6KDPMz8sMMIVbkOQrFPKX3i2mxpfLCenitv3nw6Y-ITCdOCnO_KE6tZ7jvjS5rDJnyExuj46lT4-OY73Ww9UnaVc-BSPSxTI0FrPPP9sZYFX-sAe1dX3TLR4bcDD7C576Zkg6HDogg-qXJ9uJdhvmlx9MJNxNoIRNKHad1XHf3SlyjxWAp4ii_Oi6lEJWNqVqYka8xzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVWOeLvgvR0jCMicgoc2a1-xTijZF0W6LELe6aUeZIE2HouqY-tN7sVZJBp5WwgWVmeRYhlqfp4k3Mz8PJJAM2eT8wYdTiTcY4072t9KDkF99hwqhHpLBVqqiGJm2pyIhZGSPTpIKsayVs4HecUIpgWwWwm6swTRy_lyhuh2Hn94_aK6Sscsnb8LqIwPVBCcLWOReVapKfxiquo2S364JsEyi4Acfhy7WjMBvdZNgIKPxrXXa7FK2ET-RBSIty-r7AXKZfKOXlAkDWRy4ZCUi_wHRMJFa9unApuifcrv8506HhTbO87uS4o0cvkg0ZOqoH7qAnO7pL8lL57Jafk6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swiBe5WEOvlg5ysIS6hsQLDKZjPRMxFEm90L5YLuxUziT1kt5UZipaNNru4gxMJ6GMq1WROr71x4-mFmw9j53vmO0FdlXDj7nrwvTx4E0UG3PNI-hpsMcN_1Q7Rkp_RDNb4n5Pzvi8Yda5LZQJ68RPcSfgrVSvAMUTMoODiqyag5JviPtlGkQ91bogF0Pa3DVONXbkRJiMLiV9n0ebYperyQoeMqwZxLQvV1hBm7NhcKsKgyoMLzRpG5qq8kEIYo7GZ2Vj78fjV6Nugfm0OgDpld7ZGcDY5LbILYF5Hj2-nBuN4dHttND5udq8AiKxDhcR3d9-9nUm7ZH8mbMTykPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6kn1kVN_Q6TWikGf278S93uh0EHkjZGO319HluJ3Qa9X7JpbFg4GKL0aamkzrAC-xkI7dCyIxZvdCkrvsPupWb3XBlT4b7sDme--Hj8p3F5R7fXwVAdKbsLt58jE-m9la9uUASDRNHFBLNal7-wXwsYShm-gmn4dKI1BlXSyIlefLsh6UL0cjptMCQK06xcP7Je3e0BnOG4aHY-2GsOR-y5fcJ6ztdCvmR1mPnpDPO7PKZ2To8XKAQNXTvTMhDw5yZx_VaswPqQt6dO0ThTCdWvTUSU47rBoPXhg3JmSHaLOoxwhwWo-9cUv_Ig0IOTPFWDPFOZXkpAoteICcuL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=K7b4_c7rftZVvcpDBMloYSk6VEIslkgG45v1vQNPI1gic5uO9uCKNCz7ezPXuZm32oxi9NuEXADE8v0YScraAav4l05d-8Nk2ol1dALGHsvahLe6bbpzU2FX3IkamdrYozIx_8aphwwEH1Mr3PpyaH6bCYy-iP3hSFu1rdyZX0WpwHQDzgHGmyd3mU5kaWwAy-A5OesHDT2zFnA35q8o2AXl1_PmqYan9btkWIkVrhzL3UZiF2Y1QapnXLD9O4Z6Xc68hjrV9u53FQZKcqZd_gzhGFL3aLuYR7mlz74W7XV3b_qdJvCsMoEQzMiD02FH6Ua6BfjdD0yXBA_ys4KpPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=K7b4_c7rftZVvcpDBMloYSk6VEIslkgG45v1vQNPI1gic5uO9uCKNCz7ezPXuZm32oxi9NuEXADE8v0YScraAav4l05d-8Nk2ol1dALGHsvahLe6bbpzU2FX3IkamdrYozIx_8aphwwEH1Mr3PpyaH6bCYy-iP3hSFu1rdyZX0WpwHQDzgHGmyd3mU5kaWwAy-A5OesHDT2zFnA35q8o2AXl1_PmqYan9btkWIkVrhzL3UZiF2Y1QapnXLD9O4Z6Xc68hjrV9u53FQZKcqZd_gzhGFL3aLuYR7mlz74W7XV3b_qdJvCsMoEQzMiD02FH6Ua6BfjdD0yXBA_ys4KpPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifwEerwXdrBYkwD5rkDxt98N0fBEvGHOCd8RhR3UszFkNyGW8vxBH_iTpfvwCVkW76Z0_fjGE8edVnMDhZNS4r6TSa-senBVblXxrdQztW1k4oJlCjZ13iJqsBQhAZ_nZUa3GQkMoAFF96gcqcv2MWTzoGGfdRCkYGsM7ZqxDc5272MlpvwBYSgxY2un7UM7hG2MW_hko_4AMTLzHGZmMS19K6-gbmVS_ykGNGYHFNS7G1cVlV3nougZomkW5X15iY2QsKqjFmBbMFmbWS54ITkjbuvijo3EpcsghmmLiPQFGDEybpC0ZvFc4GP6tNVftobyXNFpf1CKmenzpGeVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeRx1nKTwTc9Uk2FApSndeR5iFhG6xwR4fFAV-KmBzFFn_ChMxgprElqn5ftWCDz-iPwFuXOpkpbVdWh41JDjelggQvyt8ArAYUXSfTKC-qadB2BUyuvmB80wQ1kiF6jtFMDcURyPRppGmTj-PUphJYXB1P6UB6HMesobT8evlNVHYmkAZ2-YE8YPEumUT0iVJYI-3pqwkKhsfmttUuGImP8OqSgLKxW09HVBpniNE2uVeseTBguSPd8ZKR5tFe7S78GR7BKP3SSKHXYI6z5aqI5C8tGTlHDFdEFivHBPI1U-Gknjqo5MCP_7TcWZkqsXhS8VPhS5j5kze_PdmpFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCf03Kc56o2b3l0tNjEy0S7qr7-NKZp7vcbpBb-Ao4A3e99KNAfnAvhqL_8ULwL4iayRs96KjapQrL-iXb_05CRbpOvbQFudIFALHqKrLsE5V2GQzeTIrEhYW3p9RRIG8xV0Tn9MaEEkUah4loIiJWQbI5uARoBN9U1Trm0_5J725d0QT5VX0x3TMQ4kGFjqBvGk5bjYB1pUxJNdGT9sPmNYdyCF42xIp_Qd1fNQIdYQsxj6K3gwPiWuMDuaIRz69-xLi0GmW4GBwiCIUtRWU-MvTHI2TAsctIL94x97bdHKCb3DSdX3DLACBAeTl5fm641aeZJ8LkMLLE2f6w-b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEb1Wrh9QibyxqIF-yuUpRXFmnybG7kZYRnK1oQwaTHYuGwu-QR1DoffnCC8xdPovqIfiP925443YHzcA06vjpyzquwrSsViIa0WC5P2z4b5BNPPVEUbtoqWDsjSapXfPQF7Fl2W3TUNA62w_HFsFgxqAEyJJfVa4birDVqWbJE9zboBO-0GndvJdhykEnBSSEEh-xTKybbWU9RFWoipDMI_W2BP6QDSerMO3AkwJLtRsAlNpPJyytlJ9WfL-qka8V0AjAs5-8BA8309u1jFTrhSsEtAXW1IKBk1Uct1hUaF3Ei4Xpyrg0UnK_esGt_J0UMG3-sChMPbopTcKGxeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyGlayjZ66FRvzj-1mKlN1q-8kg2AV8oc3H2ib4rFVPWLdrJZV13YKt-S0hHvahPpQ-E1yau_C8tLh3BPTiTaud2EeFw_AJbG2npvz721dbAUMLLHQhAG5CmM60Pe8RMYZqvu1ASMl3u0ZkuNL8udduCdMednik4Rqx7nDC-ndmIMRRMDq5mxYTR89N62fDLpmvBb88DP5dlxoVjXmqScQOXuCyo3RmKmiOHr2iSOihYWXuWtnHQAHbF93QI-Q59Phq71twdSljimW88eYywqeeIRONel12HMgbXJtcOo93DshrKNMpO69N1J74rBrrlVCFzll81zJCHNEDkhvy08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMAVngUN9Pa5H6ZQ5l1fwUc67fZVa3Vg9wookdm-k-IN8N_tsrfcPeCthzrNSQx-tHt-nNQyGeTrsSSeTwYflUfF8FfW5aJKuipGn6a-Y68JH4sBXrghEKrzcaJITU-2xAvvNv2OlZzySw3GFl69aAf9AvA_YfU1oEjvsrZ-jdcwZFTdJKfA5Rc9io80NYdsRjiK26clYyeGiduPjIo3AF4cu-q88VDRG_Vo5yX2R_IyOVXre7AY6TBF5VmOSxkvkcTSBoP7WqaWq-3CjO7OnX3p1H8E9QbMHTBiJGHx2GU1e-IqloV2kpjBZNK0CJbOTMydW-O9lbMcQiW7qx8lGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucA56Y_H53E8LmqcpEXoPs-SUUs2tUEz64-9OwJjE1RK-TF6CRobBXXEe05bcfdhbllbUBBEn1UcrOWqcEjL8qFXatnCzWhYZ9EjyVIzeT1Z1ZYtPxGRG-LuAxG6I8bg6GQf1lpLq8srjrh9ies4GZ-D016_fIGO6RwUm4b8UPkGI62WgdhPiMEtqvc2wf5-vYb0kINndvxYJ0l1INKTtRfTzBZccDDmEhHmN7ZOU5UrXG3p-bbm0chNDJRhtOVpwF4hAmpUVBU-Pwj__z06yDcfz7DZA1jtYmu9BbNJntgQaM1TFmCxNHPy_bu3B8vU1hWvJt7D9Lzag5lY_VsDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVOCHWfwjW3JNo0LhV376jB4WpTHM0gpgBFLPQKU3RfhUS0R_eFWp05VBSfdoa_I5Y95i0bjdC0EX0CVFYUvBD1DtXXX3xxfCjOmmww_MfZu1bjn3nvJUWCzI-TOSqDwe_LCFMpd2l6Xsx5wmfKsaahcVZRY9uiIjMCItHyEbeKikK9GczX99xoVdwk2UORUXZWzM7-MCVIN2z6PbvPcblyHH4cNt2XWx_8pHWy76oUH7JACo68_WB090ADx_PXg1waD-R99_BosGFXsgmLB29au25nWVbuNKZsa58L52zfrwxJwfmgC1LNJlXagt6Uaos3l334vkBQ5xykOGgqB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLEGuLro92aSYIWC7phTaX3RCbN8LmBXXlIyusg5AuEEpPyDS5B8Qgh6xHOwUeG4gyIBCKuGr9SBae-QQDQGzMMEQKRy1osRZFG18g1yx5Boj4_OOMYTodTHrOGCm1FsITNLfsECdR90mamGJ04dGF6mcqFBn7FYPvoWwaI4iClvrPjsDxt5JPf-s9nvh1NNbNQajumanhAS9Pghmry529OQoAf3I8iaopWzXFAc9RuUpwY0x2HaRaqU_UluuXeIQ6zOk0OZr9fNd9YbAE4svCw-ghRGiBb37NKJri3Kvk3wxcRKIB3qjBL4hOdgWVOA49Uut3sFVfRkhcaD9jXiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ3M-DJtCcPfAfbYPelHt598MFRUpDPfGG73aGWvmLXCIIgTWmQ0ZfDuRMx1oeVwYMI178hg-oHQ_oE2a_BAG6ZOGgcpR1KmetK0FTUyE6asYkJQacRTBYU9oaDis7aVoGCcCcKjOk5tr5lLNPsjQZ86Yj3vwDyjiDdZzb-QkHu0fgHydEjAtrx_IS_YOdUtmdn52URVP0vECCD40QgI_a_3enaPwTMN7QK8VGJFCee7vRhhvObAedwJSdrKtA61Rt5I1t9LnTYFQOVa-CnJM-iWL0UyGGsRHHpPXuqsJSY1llC6w9LfMzo-1Frz6ns7-B00Ok5bMNw7bhCGq4Q0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubbOg7NnRz3rAILalzIR8rPtsEN-Q0dlklbaUTPLXW_Oh5ojlwuzH5c45h9vn_2K2Lw2kl_nGmARqBwbMjajiFwJ0RnaCtVHjnlPjpYSApXyqG42jbh_VMkmGnUZr3BP-xT-rSKBHeNd-Htdodp5qojNBWq4Gt27XLlrStz3LiWDrk1oPYdzA8hH4QcZx7efnb3MqAIUsLgRPJpbTIqpyn6Mll1GVCzDQ86JHm8ZE7iUH-gTov7JvB8eMplq-XX6loYXMWjz-bJd5-xjt1OORYqKtAuZiveW0smhLZRMaeiiyyNGgKxnp5221ttzDTfaDqBbRQmd7tt8cI0oSBU3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCFBpQWbywV9K2rJGZSqAj1HlUMhON5O05UyP9zU7_63IEAKawzE_7MqPXmpKJifr5G3mdzX7r2Q1RMYCWq8RdRtoCIA7uRUDsSQOlAoh8PClI36sAUrwBouxOdXdKrl6TTpAZfcsnb0U6gpm3vB2sz-2CT6-1Vmw58J3PoxQyWRwsva-DIj4A5yDzVn2bibGVXYbUiGyEBaIq2nXVixrTHQNaxImWBhJnIAfqDmxVkCPMq4_6Wzjebqy16SlsXzawDe3SNOKu-u3YqvXYzzTemWKL7W71NemmCKNkWu_-w1X_4D4YiX7pJj6V5cV0ytQ1bmFtFRJ_pXnGdbM1vnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGmYvdYEGAib0plZBx-czSm7fGYejoBiNUxfZJ8A6GJkRnvCeFYcAzlsPNMelxVWQI7IBLNhjLy9uAMreQJavwcg9Zc5sBm0a0s8Vjd2CRZMDfBT2yzM35R9KJ2TAEPlIiFkI-Puv-j4yGgHDBxS3GmCki3_aHnGEY7WBOQKcQU2fKKhDz7XvW44k6Uc5ApcdJ6w4PEmo1DaFgF9MhrKxQl4Hwcxyof6-1F-IDusio3irsNMOpme-1i4CihnCzl9JRlyKVBEeWuRZ3rdOKUGXipIbC19eZQ6Gk_QvyXPaCtX-2jouUexhOf3fj8uX0PhgK3iBCW3wcsVgvzpaPieyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLImdsxtEANDgPLd41JA3kpjsi_9iRpXkT5LCdix5UkaTa6W-CG-Eu6swBN8ART1qnpFtWZrcndUcyGzib10iKAdNlFy6cHsBlhWfeQiUulwMb2ANNhh6xVr49FKdhcIlc0fGKYXFW_mWxabpVy4U8UjMJFiTi5lKB51FIhIb90dwpOoCPQWFgywUQbuco96aGvhA57Q_Wmb2nsKtRnh6CXY7qcNkFC9AvUHXEHF25ic8u57CVekx_LemcKUScTQWzgd0pxgOl21vWt7Q3cxducTHzanmBazvh8bwp_sCFK-tDRza0VwS-CENKzkkn5UWbTxoifGiQ5fX8_FnLk3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh_HLVtJzGv8NqR07kbatiPxdec1JRyNl4ukiCJoJPaZ-Z-4TZ_3zd3e0bqD4xai8MWTajdvzCMzEenl7BfwaV32O5AfGRwtjij4mPv0zAGkNatIm2IFcaE82sGO077Qt-ttPUxVw8D1KfdT_KS9SnNmNwoDIqtf3HJRNR3eCsqyDQo3lbLBMUTjSRADto1hsNp1YEQdzBZ_9Hrd0tB1QTakf8wB3C98_vM-x-T0dvwwlAMRTB-xJcksszxxCeVOnoHs32C8C8xlMyrso_75Mc-lMuMvydQ5VDx8TRLhaGSkV7hARrebdFtgP9z29wLfne3YgHYSIPiGsjZBQG8R6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWhVX_wgz__CtraIFl3kJWWr0iihnMhazL7MyINiJCLj92XruYSIsbJ2KMZKJrJpivitlUnUCVgIuLdHWqRolw2DUYg-xPlCHufZO6_fysN3U6UGaCK-Ag9a2LUOBpEPh2nt0UmQN5xZMEYOHwhWU5XEEajGHbG8-Truyk2N4h1kd6VfOfOXZv6wYTikaAm-LgcwF0Y2PCPYXvvaCrV8cJHPGjUvwWdELD_qrIJrL4fDQqsPq4tjqzBLaYlp-mcextO-Td5j97zawA5B84-6f3vsSeTcTIja615ztJqWM5uj4WPLq2mTA6NfNKIIaSQo5CD0xD4Yqq3H_PdpTH-UUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkI7ascP6O4l2aIUHcUUJTuyntPNtHU14q7s22hCq_Sj-mAFwZPobmrVRDXU9pqk0EHaEixR-WIQE_ikoPEPn42Pm03Zvm1GMrdASqBOWKxyuw9378N5wMzrpTmAzfzNZWHINZkyIlbAIeeMcfzyQjE-QuAy1LgGY5yHFJTzDVHP-yPW9BndJVSvGNY9gY6uVY4sH_PpFSb4KRzHJ54gqs3jIr9T9YHEo7JgG-cL8FwmaQ6-GANvCWYMA5wi3oJFIRtgd8qj5_S5AfZSzxEWIDSTSa0ei2_EEvHc57UrPCj9CzyIrOpKqBwHnf1PamFbEkRNJF04kXK9ewHdve3s_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVlzS7VpDjrphScPXzVryveYMR8srOsWy8z1v64WPxjojd9rZFA9w0I4LzX0EXR_cPES_ymtMbCeKM1-T_AOOP2oh_xd7MRF4jcd9bzs7DFlR7LxQeQMoXCp9COZPvb0Uag3wz5Vj2cODuxMguah6Of2JslnoCpBOJLgobtwcJODo5IbjxLYC4UlCSJgl0ziQAIQFBtEyYjINEFw5jODspCKpyTmdOHkXEffZ7urHufA5EMf_MYXCL_fTni-vpCeOYijucaOr1xofeG01jXyBxa5ZhQPQ1-8FNgpDZ3pZryhM5VhOFkBMSdC8MSt_qOJ_j6y-Ggm2GGoeYpw7W25Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp8wJMtDy60_8G1C-KKuJU84TJp8TFQwxKjohkMc8XVDzRcwl_29aM-JmZ98V35fiMsRLY5rBUr5uJVbAnGmoTZEbb_I7-H3pcDLFjgXOzvF3hM6NDkIuwme5g4NE6o-w92uQ-NfW5I13hEc5tkV9i8PmHPVDeDfEyD7AoNihvdZqbJpncWAOPBZTTFrxSbYpIl82qfLcKyXTQ4gx60FyzZi6UAjCbG18fmTuUYJ48QVyR_Z81bhLfeXp7HqYcANLy4O0HivoXvDr5gAipVn-kj4Qpk9s-NkSKXDRPAflJKj4JVmX_Yc_t4R62XIj5KJ4YUf0aKQ3BHM69VTmXPXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=THfAVo6fcb0JBOwlRZ6DBwwQhEJC2u5iKoEx8S2rT5Z9XE6ZsmsTUpykcEcyngrG5KbBCl6M8SeCZYHpLbdxvYKeuowsYJJRzBiJYNprhUJcWFbAn6h3vAQifD_zzkQroveafScj4vaMzsT5juxVGkPpQuw8uKxGvZD_NsnVlQQV6Pej1YNP_mLgPOJFoOqau7_sXWmpNWKUeafn9oxQsSi--RQoDIkSAi3Qj6ZokPc5MeHye83NNtARMzM6fEsrhV1_0mONq8L8iHz-tuomy8_sBGmRcO9uSMLXwE6cU6nKO4oZAoa_HnZYRnk63J1heSBUhiKruupBwCIiOBBNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=THfAVo6fcb0JBOwlRZ6DBwwQhEJC2u5iKoEx8S2rT5Z9XE6ZsmsTUpykcEcyngrG5KbBCl6M8SeCZYHpLbdxvYKeuowsYJJRzBiJYNprhUJcWFbAn6h3vAQifD_zzkQroveafScj4vaMzsT5juxVGkPpQuw8uKxGvZD_NsnVlQQV6Pej1YNP_mLgPOJFoOqau7_sXWmpNWKUeafn9oxQsSi--RQoDIkSAi3Qj6ZokPc5MeHye83NNtARMzM6fEsrhV1_0mONq8L8iHz-tuomy8_sBGmRcO9uSMLXwE6cU6nKO4oZAoa_HnZYRnk63J1heSBUhiKruupBwCIiOBBNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozNfEJFLIBqb0a0ytg-h1PC7MKUwGjjDXx_di4l_GEbz-e2n8bC7oEGMeOVm7fRMpZl1nIxj731bTCakaA5Wn0B47xg-Qw8g9ncT8eYObfB6iDU0ysK0Cg-EqRatH-iGhPG4kfZwb60QhpJRXc3tI7yXTF7ppamcEwnr-nfaziKt2emzzodnNHmE_UFblGM5E05pEpPCZC6xmtuN8GdDS2b1xjLAq8YTMa80OIXkQ7bmhaglrlLoFZ9uDB9sRjT8XAabgpI7AmmgyFvhquePzgdEyCS1tz11SdDoVCGgCmvspK-lB_5Hqr1MEatvzOPg4lDHWKcrWyWtcDGjFBwEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nboQnOXuPC6rVABiXY7bQznUbKR2moprbMqv3Zn2FVIus2b5xP9ObVAOyjyR2kNHoiQCqgvnk-fWdE_WQGfD5CpHmdGLt0lRyJJyj73sIsPxvyRkdoHZ4HhaPkerl4N7UuXK4YuKMmirx2Kq4uk1_B5kG8L8XN1mIonsETv3aN4nK0FcAPIip9PUVZctza4uLYjl9y6QkGN-PLIXZP1J0VkQbbUtpL-wM82r4hkx7xhxnvYWM7HBKHwvPGyN5fLpq1rqODRKTrB34CKVgpqGMsfSTErl2ptKi5eOCbQaMeOTBcZq3qIhOls_Rgu38qKpkCbThz6mIdNWtQjGkhjrBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=N0i_rTjq1NJhxabzixOLJR8MxrHJIU3sQm5_nz77NA1x6UIJvTUdQjqZ9HX0hZH9JXyCl1h1q2RhVBJd3shHr4iwzKIUcKNhbwkCali8gPtbM3PiVDUCySCrcZeJ1_cVqRGsHFjzLtKUhkBee51KPqzWF4dhkIvyDAEwb5wrKAHr2xt1q53hGox0-rNuiw-_OB6tPEZey3x7n3gxlHgNMY5_56a3JWoWjztu1Zqmrj2fhdpJ1y9RwLV3Ef5cZQDVopJXNngZdTaFGmZnPoAqTxBSyLY0bbfRlU2gCZ_L_GOEIqz6IBCDt9rGJzemwe3R1g_XUOUqbsZ3i9hHYxQJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=N0i_rTjq1NJhxabzixOLJR8MxrHJIU3sQm5_nz77NA1x6UIJvTUdQjqZ9HX0hZH9JXyCl1h1q2RhVBJd3shHr4iwzKIUcKNhbwkCali8gPtbM3PiVDUCySCrcZeJ1_cVqRGsHFjzLtKUhkBee51KPqzWF4dhkIvyDAEwb5wrKAHr2xt1q53hGox0-rNuiw-_OB6tPEZey3x7n3gxlHgNMY5_56a3JWoWjztu1Zqmrj2fhdpJ1y9RwLV3Ef5cZQDVopJXNngZdTaFGmZnPoAqTxBSyLY0bbfRlU2gCZ_L_GOEIqz6IBCDt9rGJzemwe3R1g_XUOUqbsZ3i9hHYxQJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=dadwnoO0nojEkQzL8uqwa41T7uNjNgXLibMv_i_Bprgj9I_C409GrXQuyAw03jeregy1qwqpqjrMh9DVkH8IvB69gz7ymioZV9jvva-nBZOD3OdwIvaOSsZGAPDQ0s4B4cP2HU-ZHNvWanDwbWR3wYvOcU7mWuS-JBWJY7FcJfiVRWNNIg1LoYwnEwiMz1TbboTXx4PhF8kQUQAVJQDmKi1eL34bCHEcwoPtKY0Ch5_joOFQH_DP5MBOuNHe755avcojM0ZKKTF_hN5OARivpaJ9U77spSjD4vZ8jxjjq7gy3hjb4RTd-9kHns30P9M-etn2cMrZWOZ3T2Vi2x-n1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=dadwnoO0nojEkQzL8uqwa41T7uNjNgXLibMv_i_Bprgj9I_C409GrXQuyAw03jeregy1qwqpqjrMh9DVkH8IvB69gz7ymioZV9jvva-nBZOD3OdwIvaOSsZGAPDQ0s4B4cP2HU-ZHNvWanDwbWR3wYvOcU7mWuS-JBWJY7FcJfiVRWNNIg1LoYwnEwiMz1TbboTXx4PhF8kQUQAVJQDmKi1eL34bCHEcwoPtKY0Ch5_joOFQH_DP5MBOuNHe755avcojM0ZKKTF_hN5OARivpaJ9U77spSjD4vZ8jxjjq7gy3hjb4RTd-9kHns30P9M-etn2cMrZWOZ3T2Vi2x-n1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=jcro6h6KpDxUaCi1bcc-7aB9DXOAJUtq72aMlQ3Mdu_6LzAmsGaZfO9Pc7MCGOiRHnTyWBOwpaFPXjN1Gk3RhWH9hE00-yKJiqmmsOziuW_2zmNruI69xF4nG6bCQ68K6GSEYDIDmw-TkYBEBks-3sv3TngNdnqSGMIEx4B5dcE4anXtysoBQLht2aieIoZLtEg7g-3I1RB__x-pPfYs698mcVH0MvlvUVPqjz3-Z1FaRUUiJ7vvXpEr3MDrxpPI7hvSQ5IgfXbhUjEfJuQQiR84qkVGrdeNEJWvGTerWt3yZGuz1drDiC30Zn-h67UTgdEkHLtuBHgcJTieNQYv3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=jcro6h6KpDxUaCi1bcc-7aB9DXOAJUtq72aMlQ3Mdu_6LzAmsGaZfO9Pc7MCGOiRHnTyWBOwpaFPXjN1Gk3RhWH9hE00-yKJiqmmsOziuW_2zmNruI69xF4nG6bCQ68K6GSEYDIDmw-TkYBEBks-3sv3TngNdnqSGMIEx4B5dcE4anXtysoBQLht2aieIoZLtEg7g-3I1RB__x-pPfYs698mcVH0MvlvUVPqjz3-Z1FaRUUiJ7vvXpEr3MDrxpPI7hvSQ5IgfXbhUjEfJuQQiR84qkVGrdeNEJWvGTerWt3yZGuz1drDiC30Zn-h67UTgdEkHLtuBHgcJTieNQYv3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrHNrzZsoK-FZJ6ViVflENlZlOiL5b1BhlZE1cUe0tbb3poz9Rc3y2R2f18tr_FQz8biKp9ODXmbaYn5VFYJ8lb0z2qjQMS_MrAa_MVuVeWuQ5K3Iydh8sTM6Lktrshy7Qn5D92N5UdzhwrSLrbRxYjNE9DDfFldde88d4rh9iBRhmQOwW6W-FOSwFGc3KnLoAht-CCFh59UStUoKtxfETjvs5EfiK82c6nidgIjstyukZchzBcbjQnBVL96LCLuogJfijb3r_Bdjm1h-URVUaalnmlBDesl96h0I-IXa6EIdN77bXOU-GOLoollVNVLdQn-WpMJZzGOlrTEkN-upQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Zbx_7vmxaczIsM_3D4bvyHRvraiVh7jdd70eJpfYVaDYZJhFUufupgfdkcAAvXdWZeWch43AC4M9PAy3JurdvfC1Rff3Ic_vpd8MkHfp4s8aD9OsWMFC_N4q17lmA6w7CeeID1pDrVDgsX9H22e0RiXwYzKDCEpnQOixCov7XF9z31IoDgdMXQVP9dk1yVCVVDvPuN9xj3tquI6KwBmTEKbLGSdcZSY1okLc2Q4HLXgmonQcM_O-drolLrP10KiqS0zsn1qnNuwwtW2V8oxtFuDpvZkzhfQb42P9ohtR_aMdkHcDxMzdbREfhLzOy8jH5uaAzMVRnpg7LhGXvSHw_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Zbx_7vmxaczIsM_3D4bvyHRvraiVh7jdd70eJpfYVaDYZJhFUufupgfdkcAAvXdWZeWch43AC4M9PAy3JurdvfC1Rff3Ic_vpd8MkHfp4s8aD9OsWMFC_N4q17lmA6w7CeeID1pDrVDgsX9H22e0RiXwYzKDCEpnQOixCov7XF9z31IoDgdMXQVP9dk1yVCVVDvPuN9xj3tquI6KwBmTEKbLGSdcZSY1okLc2Q4HLXgmonQcM_O-drolLrP10KiqS0zsn1qnNuwwtW2V8oxtFuDpvZkzhfQb42P9ohtR_aMdkHcDxMzdbREfhLzOy8jH5uaAzMVRnpg7LhGXvSHw_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEpP8ODH3T5mb0FB0kg6Bm1V-4E2nimugFzZOxHuEpqyEo7pgB8b85LY_ZGeeBU39tOyd3zPhRppmCznVLfGnZJE9dM6A6H-TjJNYu0-uMVvZwNNn8jCWfn1oywhU_FkbmexhacO_39EL3U6b8rxlYFk06vRXQrg9e-9UBI3u5YWsvlY1CT_naIz0aqEgp_JLy4_kvYhu5AQN828-TRG8fsXkRLfGKigDiFGdfeFqLq_RFjNGqqnbgP6CzWyqouVmaT_jlFnf4-mlBFXMykWXJsVYadaCDZ25aQqNUiqwdn5C3CD0C5DLrqoDDhRx61forxrW7wXcIkZOux6t_vwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCxCzTqZvRBH9fQO130b29anAAMTGfTLRIK3DpxiOZmiu7cu_WdTRoFa9sXBt9AQPAwf9m0XaNwWC6IkDs1Oc1lpEJhtU844HN530BkFHbX8KPxwoHCu68OmW7_TKPYXVXlz3rVTAUxdZL__rbuERZyuEWDpD_S-99qXkBZfCzMqa6moGPXBA5VFyFLz4Vp7mIQ7sjoSqDjykAuAKdZU4jl_yE4GRUV8jMofrDr3PZywDpGGl2woR7HMdhsE0Sx9722YAiklosD5AQuWIdWHOE-TwzNKkAEGeHWf8FPZ5v86Er3Ab6tNLWGE-0KAr7wlPHv869zfldMHQCR8TxDGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9yDGSyylLpXfbE3OHZFYPlcqY830y7gSh8gOjqr6GZDuo0WOpQq2EtIZGK7SYYJ-LMhZFP_qDktye76ViODMx072D61TesIp7FE_5QmBzVWDqjsmk5gsGN17kzxJP9kFsa8DZ4ivUQbxQ-28q9jpB-JcnuoYzsqniy6JY11t1Z2WnmMEj38QqZJMpfxOjy3McbuCarNZ-QKiFeN7782FFnm83QDaXHpqTyV9WOd4wrK5e6hPoVlNxRriBP-8biE76SNAYKKrHC7tIOwyXNGnFKZwQBvCN6ELHKGOTV0o0I99WTgsaV51yKkaKsbDRTiHbll22XUFs1Hsiloq27JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOUUGi_kRqgiy1_pgZCFHRQnwnWWTy6O68sl9lzShRkK-eN4uO_pwm82EqyTZeLNMSqON2Gf21Ru2RQG-hLBMShc_LtJXgUd6J0NchskAEPRqkRlv1ocjumC6mBHdZVmuRTjfpQjK0nl7QzON6nc7eDnQacMNdI0wOh63SNd596e3tj3pfE6ZFNvZ7BFaqpDqFL6sLasyRtr5S8SA2LDZ5w5gPr6sy_DAvKwFLd5SIAv8D1yhnHF5T2a9MFptZhze8cCb3_g9YiuUERmqCbWZ1gHB2NooVNWLuv_50IoVI6hrllQoLGCoKCNXuuGfFrPhGv9ic926N63rbreblH34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvBsiwJ68SohoP4ii1q1qjYZZ4-G_UA-grjfy3c-FcD_POEI6xB7w2xSnde42vpNu2NnTyH1X55Vz1A2pkYX8tULCFX9xE8IcPTwnqnXROHY5J9z1NQ3KOYpG-W957pD6Zz0-q8cr8V_R0SH6v7zuO0gR4JHyqGgyd6bpr84naHfSjUxyoXSDAHVEXcUrt8S9PiijR38LD7b9equfJr5mLQEHSetzUyqiqX5RWHcx3AvZiUFz7d_hx7R2d3B0JgJPwcBC0r_P7M9-MxUZjT8JjZofLa7LqlN99caw875AQRrJ002-o6bEYexpymB1zv79HjpPG3wGyPQl-Gtjsukww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R25QzyLqpsevlIq_56qZg6hILEJBVjRIFmWhF--V7D4nWl7Q1927m9Gf8xCR1IWJvYm9sOfqLJqSRWr3qtgkfAfMezKf2EnxJz_MPYBRV_XjJEZ6o-Q35Oj4KDrghsa83IDXbBNNMANb8-YWk6LMZcteFD_eu_Za6xoxg9ZaxC8n0GbZ7e39JLV-HUgsPUkxkVspoVbY7jLfIH-bwPNLGoUbGuF9D7HZ2Qsra88JlCyTHBTou5E3tuvRs3Bq3GY7pV79JD-McRhzE09wHL_h2gTXebVVIieD25lkSSuqsjwIkcyfnKrOF4UhkVUIIi3dw1hnh3_CGYHrRZdm6gVn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqGsQKgNXcTdbXKVynxUvYUywIx9pzVWhOu_sR3pa7E2p9Mvf1EllaQO6EDcn_-tWWCWmr6clGZmFqfpuMFU2Ys5WBVyE-OeogzObqKOjeIIwms9nG7dvuT1OvP1eFPafpcr0Uc8KV4JZ7BUu7uU4aJRkfGV05-RF3FObeT4MmMbJdK-fTRO3Pi6wEK6iEaPYAg3Wa1oLMO0o1fya6tTw7YtNW2rLAPV8VvZv4HJn9hDwWhHih01CsxiMCpU_2ld-6wDu-abla_MTObeonl8n4gH0D8uaoHnrNHFi-C77yLWm8NmrsIQiJKJ4bHRq1WKd_kdCQVuhT63_uv6cOyb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDSybuGHDooygk9IZlVO9T1SGHGPypNE6EUS5oqO4b-oqTHK1vu7ILrSqd705Dls4qu29i95xJxYY2ZQjCHaeOyIcRm-hj4nZj34Nn_rKHXWTwdN02U8hpEsu4YD2HoPnQTR2R8-d5a4FzVJktBSCpEevkK04KddF1RmZWEL8g-FE8fbF7jAyhPXZOEqZKE00raE2Z3CTO1P_GS5emvP4r-CnqumC_xS63f1nXW2LjqPOvx4upegaIi-H1kYElfclQoXnV94ipwc_PnmeNnocLWqxTsHo4pZ-krfERwQYied01pS_HPI3XuKBBCvnQ6r5D2Leosk9uqPE57NWelHFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPr8t_002c8-9uWEQA4aK_xEkG20vkvmFa2sk1i2Jve3XiuEXbrrExejunUe0KMoruMq4-d8rGS7ryZjnht2O40oynneNV8qFaFcKDXppObbmywGkcnh16BLs95IE_xgHpAyaxo2oI1Yblzc47pMp3PLFw2MYmz4_1BMy4L6gSaDUaoyhc-W_6LMO-LAXvGRxTZPH5wBsRj44UhJ5RK_s-T5u3I6EIJq2VU5UEzEG6m9eXozp0HvTErguoE7Yxao1SeEjQKFqIE1hXpR4gD9x2rt8NHioJQRkFHOICn441fgdVOkFyzud3-28yXAKRxN4-txBZP0J_QRKOpDKdoSCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0EXr2Ra3Z1InTajUVcL9l8q5aMa2gvOEG3873JhdNWcl51woy7Yb5jyzpbYxup9S553YVF3cXjlnAwpik3m17VmMEGmVGeQOIdYlw1xVHt6RFChFUkaWqfGuPyLi6UgwIzSB2sA1gvq_5va-jEhrS-5oVYMpBIYU24xVPe1LLtNgIKg6fqK_XsMaAkJOtG1j2b8FCC9CtrxA69B5sbX95l22H3HgyTi3Y6l9dCzQViif1schTB1Z9-KWVVfjPYcHHsfT-TqsGf6dLR3OGJVjIgpLYGHdzmSsQtyEkY37lNrvzb-6rmoL_FBjfWjz4mKAGpfDViJFcMZ_T4QrlnRtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgE9NP9mm_d8uSDHUNVNCekbJ9YQSf88W9kw38GcZmmlVAeyDVMsm6YL-6nVaxdXQABiHh6jJgb8vSta4t0gTab7YNA_Gqg5t98uyuqo9OtXX3KcEhU-G5iJrk9fxP2_cOQTUvdrQoWkOrZUELlMaMLVJVLcInyQod5scbLpkBRH9PtFMhNumyT_YwAWwSyhSZ_YJ5fPpVhtKGf0_3pQ3yIpkY6HG_F2C5V2-5kZzz-bPZ3ZC3mFqxu5rhDxQiorlXIB9WyIksp3Mml7nHUi_NGmjsuHGbyaOrqdVNKAoHiOD98FzV7efCvZgCaNG_G3DXWeNDffQP44qowYFYirYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
