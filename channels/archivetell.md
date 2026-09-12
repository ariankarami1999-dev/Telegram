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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-7724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRvewno-kbNb9wKq8L9neFgT2wJ6nhroqbUQZacf3MR_e_Z8pjP9J4ps5e2F8-Ll8JPHHB_uUhVqVfs02wy1Wc2omhpGIupW87nLNSdH-n2F-Xobi2TJSlfrYo2AXAnEikKxljC0xh_It0cFV3C3V_KpzZanPSWP4-TnrSwLiyFhrSr1Zy04IrGMk9JgxD2bdewVA7_MAfe5hCAtBi4wYnD9ALb2YpBbfKmkOUQDmt8vxeWk_3bfN6xoDMCtociBg4FX0vkxva2SWznQTCN76YugJaHMkADf6Pl68hE9zoxWn4YLo7uQBn9cHv0PJb3M1MdgnrMkQCE8BGW1WkbhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل‌های GPT-6 Astra و GPT-5.6 Sol + مدل‌های ویدیویی، رایگان
؛
getunikey.ai
- یک API چینی با مجموعه‌ای بزرگ از مدل‌ها و پاسخ‌دهی مناسب
▫️
چه چیزی در آن وجود دارد:
نسخه های اصلی GPT-6 Astra و GPT-5.6 Sol ( امتیاز 88/100 توسط hvoy )
مدل‌های ویدیویی، از جمله Seedance 2.5 و سایر مدل‌ها، و همچنین لیستی از مدل‌های محبوب دیگر.
مدل‌های Claude در آنجا جعلی هستند، وقت خود را هدر ندهید.
▫️
نحوه اتصال:
> به
اینجا
مراجعه کنید و از طریق جیمیل یا ایمیل دیگه ثبت‌نام کنید - نیازی به کارت اعتباری نیست.
> در داشبورد، یک کلید API تولید کنید.
> آن را کپی کنید و در اسکریپت‌ها یا برنامه‌های خود قرار دهید.
> ؛ Astra، Sol یا تولید ویدیو را انتخاب کنید و از آن استفاده کنید.
base url:
https://www.getunikey.ai
⚡️
می‌توانید به راحتی و به سرعت حساب‌های کاربری جدید ایجاد کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 527 · <a href="https://t.me/ArchiveTell/7724" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMbnrVecEs_h5rwWFFotpCn6I0VKUhwo6t8QZeVjg07MHDvT8LeyRV6cmmhGcXdZD5ABs-WH_UBva1qUMWKc9utzNVLNNUHfBmd3udcF55yTQOSLhdwv_j6Zli5V4Hq1Szxs-OoCVKfG6_bzsK1DQxiynRkVz96CH_65A2HrLZynJ5q1SLU3ebGUBglcp2sWx313qP_6xDs1Uc6UjRSRk2z_z1EqphdtX5rrl9rRISo0DYNy1lOUaFdVnG1kpRw5o5v7e9JPoL-CNQK2RPKQKNzzjC6MdS5pxzNnsjfPBefhyuAY2p_wHzGwzXz4dCBxtRmxZwFI9B2ee4Tnv02IoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 790 · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 972 · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWamXdTKIYHFJyLZIuPtGbuYxuJyAD-01EC-X55CWR_NAFCCBzVeYpNDRLDYrlD9EHOWRkDtP7pryUEwnM3twdkPcOM0B8GglHufqyedYIQcMN5NcLPl6a6V8XinEDg_oxXPR_jP0dDXkJGFzOe213UXXPXApaBOAzFnd1a8VmUSfQwpJrk9EUcWOAtOD5m2iumQc5IrnPJwDnO1a407lz30gWR1Y93uA5HnoBzNGutNhlA23syTKjVIeZn_XW2f7WSBdbby71d8_mnU__fvgACn_DyUklSILGK8dR7_MBBJdvTUoiUQ5w273sNTXwCHWNd8nraKewcUUKka9Vgn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFUxSs4T4dUW857WvIzN49zm9F-rLNAhjwjPWSomsavt3GikjOzriOo1n2C8maq4IwhltMrWM1fyAmOW0AJuBJnGHdMRnRVPfMkC44bosybD5EQaZR7il6-CrFVSXaYTxRyEHls2AJD5U75f9kozvKI-XTeyAT5-icexOpsulH6r7-oGkQNZF2kdbSNVTjPKrWGwZzE59A6c1umKeF2uU8-i-H4awIwJCC1ePkJwJVYbAX_qZRxhUKFiSSfW3DEd00L3TJrPyYWRAlvknfPH7q2veGUXdOsPKdE1v74tIvAz_LDilMzfNy_9be3BTPmteatUZZ9wHX0HlBoDzl690w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1bAIpgpzYPA5oh-6N8wpL4miAlg6gW7D-sHjHlf2n1IKHJIid-47zQzrrjfE7-hjMFUL-e4agb9JNv3SC0yidb4qAZgpZpy8xnpldIXn6dYsxwtCI6ZiVmNgbCq1DE2jQuQtJERZ3lAvbFNgt0eYZamA_wQt1niQKgxCHb8xdL9bWQUdjJrMYJPwM5HDNarkmIITlHUHLV6cpu_BveZ5sCiZgxtVQCwm_y05xVjbndYedyarYd-_MVG7yMjqjKbYRWss0HQpNfNMbzjNtsK-tVDhwcp_dWBmBzJNh8F8yX34TEFZK6TWeopD66oJCnP7dYQ39FDwwCdqw7_rub9oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiBWFckm9JQl-nH1wpIt9mCIAtVjc3o8coRC0A9TqUknj3_xvFr1nBTbcZz_KGqLSC1EgpZP_8uVjUb7XbR1ey9dBARwQiJKfCUIUBaqoUNsqcM5S8ncLAcsQBTe2B7FSGtU1kuLsrT0kLxwE7ixWEscVC5mvYQJA01gthPy7LvydowU_L4ZSpZ6e8I5AatZ_LnoTKWQu4Z8JpG_9e-F8kVjD43XJM7N8uHfY-SlSlXLlUOJSlwsk2TsEo2yjER5AaN_s4njGdjxG8M9SRRilSd3oI5k_jQAF02qyHQchr0fkIxMTXhXw10Jbn7sBPzQ66lT03ZVydz9QOBZb6hXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVNQ1qk95X_vNRBPVrZZWO1nvxoDTIGRME4sfQM4A-kw8-DOcRUkF_HADiPzOYEMKoW7kswMhF7qlAwov-28sNLRq6Dzh6k13V531DJKFaBGWgH3c6qZ6VY_0oRRHKb05O3dcXOjpJUaxIdD1d7tRIPvfH6BYrkNqqBkYZFnVJgv9QtYtYnE61GcjNyCgQvASjzeI9DXQVgSCsVNJFosQZi6_n7ZAsjo4L6fW1fGMSq-8xZRsdjhsSI9ky1xL7Y5Gqmc4M2NqNKsMpttP8cDxtyEHD7V5mJGcgAeKebB0PcD0OAmWNHvDvA1zXYaUut52tVmDUBgTUU8r98g1HOFvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGAUNxzy0P3CEtnlLAWXN6t1qhjD93S4lY8Y5WOr7lXO-HOa5HFhwfA1yecUUy08ZsJhcJetFsESkB_VQTi3zdHOjApTZS3VWFS2EMdsVJGEUUdEd38bth-9sT46iSmsUJcBtJExKY8kThX9yMtsO90yVGSGMArnIeaBSEkFiDaFtQy0kzMZG_gfDiSmEkPz4xnGCFYQBafWOkLD9PoEOQMHSzbiC4frJXJ5OZ0MXUfavYeL4rP2Dr0_cF1mEZv5jyKqlsrK0fkTcUWC2yF1VGf1nF4AgKNuA_so1yslKsP4PhU885H2tgb1qOrOWyfbMUTX2-qdNtVqPK6LaYaXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=XoubXtkPjyvf7ckofV22L637N9Myjxp1Ii4QWq9Am1Tzeoqv6fotKjRp7GX3wR6xa--6vX93gZ7KG_IChqRP-DytpH3P3iCEjUNEAhaItfVKH0ST8FHGZD7y-twR18kQJC1tBjN2tmFI2Y2Yr9sE_mJdgZWt5NgyJyKjk-X1ntY0iZI9s0K8oJrUgPrpyZNUr1RcZKH9QGjv2rJ5jLsGCif7lPRVd1LbLdLhtRVQGpCVBiNudluSOFX6vKjDjwAkx3e2Ht_ueg3oCts4NBJLMGHpzUj6Kab6t2z_gLNjQ_ib4yA24hIzQIF_V4LosKHOwkomgcH8ZI3DuZfl1QAT7lQuSrWcks75-SOynzXnBoiXrPpcobSx0O8rbzhQDX6vBaw8Yl-FZrL0XuAyxS9rv6MTIiPORa8lgUloJwkx1MKj1THrlDGsf6zz_O8GRu_n9KhP8JYJcGrbi5V9rd8GCl7IdjiCcAgPDmHZ7TaBjYYswgX_4q2dDJuN0VwLVYi-p7D2dGTzoUJlZjxKQ6zMP5EpdwFsAWTBYJdii_EIScxmiz4aONFjCKwZDvsKmJCj6zmosm-K21FMHOIVChGV2Nt1JyJvKEjVrh9equUM1BPBg6PZ2np_wWx6KeLhC_KTr50bGy98u6HGLjwNb4kdNBe9RoaaSf0r6jscm3AJKiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=XoubXtkPjyvf7ckofV22L637N9Myjxp1Ii4QWq9Am1Tzeoqv6fotKjRp7GX3wR6xa--6vX93gZ7KG_IChqRP-DytpH3P3iCEjUNEAhaItfVKH0ST8FHGZD7y-twR18kQJC1tBjN2tmFI2Y2Yr9sE_mJdgZWt5NgyJyKjk-X1ntY0iZI9s0K8oJrUgPrpyZNUr1RcZKH9QGjv2rJ5jLsGCif7lPRVd1LbLdLhtRVQGpCVBiNudluSOFX6vKjDjwAkx3e2Ht_ueg3oCts4NBJLMGHpzUj6Kab6t2z_gLNjQ_ib4yA24hIzQIF_V4LosKHOwkomgcH8ZI3DuZfl1QAT7lQuSrWcks75-SOynzXnBoiXrPpcobSx0O8rbzhQDX6vBaw8Yl-FZrL0XuAyxS9rv6MTIiPORa8lgUloJwkx1MKj1THrlDGsf6zz_O8GRu_n9KhP8JYJcGrbi5V9rd8GCl7IdjiCcAgPDmHZ7TaBjYYswgX_4q2dDJuN0VwLVYi-p7D2dGTzoUJlZjxKQ6zMP5EpdwFsAWTBYJdii_EIScxmiz4aONFjCKwZDvsKmJCj6zmosm-K21FMHOIVChGV2Nt1JyJvKEjVrh9equUM1BPBg6PZ2np_wWx6KeLhC_KTr50bGy98u6HGLjwNb4kdNBe9RoaaSf0r6jscm3AJKiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=HxrgPMb7mqvpO7pcYJtRfEC7U1blS0Aynv18dxNiwELO4d5s6NXehXdKwQ8nnRbVcv7wTBP9k3-axZR4v2aPtgGEdwSh1uKr8k1eIkDVS_DJE3M4Ix_z7-VXHUkiqxr0wl3H1v_cHoex8C7lS7qD1xy4MIUTc0ktc1je2vip1dUCCZWLNh7xHVmhtoZZqSqQ44VjMZpUyMkn9dirWOlwBo3ZUhytb1Gqq9bMb6-3POV_u5u-2h4ZSnWwGmtmnwnm7fc-goaccE6nk2IirmEMD6TvpbdU_EvrAmWNBUwB4JhLTRajLg7sbQx0rn7Ffyx2NrWchT2jM_3yzZOmN1KE-yBdWfRpMO19SzYd55FQWqV2QXCDx0PTcrZPeXO3ga5LZKos7Y0M9H_ImFVITtR0qqJEPqMLDXFFbSST3vM1QG6_vYepl8_dmYAluZ0bWuQ4NZBgmTIx_guCLXD4L23qNYS-lBvPUuI-MVkI_IRL35G0rTy_sF4zhKw1_iHlI4BAz09_OCdQyzxw7h_VWuVeF55fBPESrVjsgKvpWLsYW_WyZsHo8Jxv7CFHm72IbcVPM5Z_ZtLuQNzs23-rQifwtTEgPSR5sXwFbkwO4wOTaG55pf9iAC1Yl91hjMQcrYP_o-e_jiYfwXTN5kovm0Rgy-NSezm3xY9LVNzbUEwayCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=HxrgPMb7mqvpO7pcYJtRfEC7U1blS0Aynv18dxNiwELO4d5s6NXehXdKwQ8nnRbVcv7wTBP9k3-axZR4v2aPtgGEdwSh1uKr8k1eIkDVS_DJE3M4Ix_z7-VXHUkiqxr0wl3H1v_cHoex8C7lS7qD1xy4MIUTc0ktc1je2vip1dUCCZWLNh7xHVmhtoZZqSqQ44VjMZpUyMkn9dirWOlwBo3ZUhytb1Gqq9bMb6-3POV_u5u-2h4ZSnWwGmtmnwnm7fc-goaccE6nk2IirmEMD6TvpbdU_EvrAmWNBUwB4JhLTRajLg7sbQx0rn7Ffyx2NrWchT2jM_3yzZOmN1KE-yBdWfRpMO19SzYd55FQWqV2QXCDx0PTcrZPeXO3ga5LZKos7Y0M9H_ImFVITtR0qqJEPqMLDXFFbSST3vM1QG6_vYepl8_dmYAluZ0bWuQ4NZBgmTIx_guCLXD4L23qNYS-lBvPUuI-MVkI_IRL35G0rTy_sF4zhKw1_iHlI4BAz09_OCdQyzxw7h_VWuVeF55fBPESrVjsgKvpWLsYW_WyZsHo8Jxv7CFHm72IbcVPM5Z_ZtLuQNzs23-rQifwtTEgPSR5sXwFbkwO4wOTaG55pf9iAC1Yl91hjMQcrYP_o-e_jiYfwXTN5kovm0Rgy-NSezm3xY9LVNzbUEwayCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIshc9OMdGuFRjWPVOOSRGbgGAeQVjK5adpT9lVjGdY04ZD78hInuyGm6VsZyApkUiqrcsKdWuVykFb5wfoq-u3ZZiwPatqY6fQtUPnkcmIbXtuR42LnH3j95C8hTUu2u-_lXgMdgzMfHtEEcPFFFDfMummL4ibM9swd52icRcbDlWP-bTFAMVlifR_9CWHYZssE9DHJK83RcqqUed-la6MJWlG-qw_F6YACQEkC0VUDmcEuI24o1HITfLg8CVTIOzQ1GHw2v0usFF8J1nxncSkWFO-SruPNKu-63BAmHTayFFkCupbZkcqBhhUtCsTE6KGarwAWbzSDL8mgddgq9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=uX2zU2eBr-sSm8ksEICpm8c4m10dIucZAC0UGPukc78JFklwpHjacSg0U9F4s-rvvATjfRrZ9zNx-REmCgcVQY0CNBk-bhRGXMvHdOhSZIx_W87WkbOku4doVShpszNlxy0yHoZ5iAVWYQ-59egYdZ1siYmya1WZFKf-2RJxd_v5MVk12xdBdFfRv0xk0SpsvPqQdV7bwtFPCiRU_Rg0KDabaQ2mTlmLaRCheEpAbETnpAiPwLspvPUbX98pUuChJytwAxWB0cHtsa4EMQ0sT5Ki9ppwXLzURqRb6i-x6AhowAZRgoRTOuW0ZEY04WThVOPWgYUs0mIH5xvuuZ0Rag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=uX2zU2eBr-sSm8ksEICpm8c4m10dIucZAC0UGPukc78JFklwpHjacSg0U9F4s-rvvATjfRrZ9zNx-REmCgcVQY0CNBk-bhRGXMvHdOhSZIx_W87WkbOku4doVShpszNlxy0yHoZ5iAVWYQ-59egYdZ1siYmya1WZFKf-2RJxd_v5MVk12xdBdFfRv0xk0SpsvPqQdV7bwtFPCiRU_Rg0KDabaQ2mTlmLaRCheEpAbETnpAiPwLspvPUbX98pUuChJytwAxWB0cHtsa4EMQ0sT5Ki9ppwXLzURqRb6i-x6AhowAZRgoRTOuW0ZEY04WThVOPWgYUs0mIH5xvuuZ0Rag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxdewS3JRIPFQPZ_lZo9I9Re6g1PwED_4b4Hemm9mHyb4PJ6x7Ieer2NiXYoTWC7tKgmQ-1z2eGHbBnFuEK3PWCFxM_zNIqBrk59bRbQGtd6T8-LLSjYOhpvd6obbnKYMXEdEk3IrTajCgyYimq2jEnj4H5ufiIwEKowI3AMlLkDpm8KD-XSw6D8YFnCdRRFSnjyt0uBToocuUVtjwGpDuTVXJHC6MmanAl0rHt9v_zxKC5cN4Ww_QNPZuZiBbnVKCSF_pb0jr0vdGIqYPB0abnAQwghCpR61Z3rsCX2Z5n65wJ9z6_vWP2eNkBeVrh95n9Ma2sSPFz-uMqhlXTNGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=qTFq66AnDX8GIOqE8PS1SG04eGIunabr4iqXaJiiDd__JDtKEl7ooqLGPE8ovHs3RicnfmZrCM39ZrGjvmOyAJAdpvQR5rkx6Nxb48grZ8Ec219VwY5u4whETp8XdKdXDCPNwNGEwqiVGos_8M3_XdQG63SG9qJ5IWbHPzifCJVIGZDcYOrHbo3CZK8UpAMW1tqz3f36V90e7Tk-ZQQKXVJmun6YV4M0T3W99mea0CWS1TjBG3dTvdF5a5GILyelT4zz3D8Qqt7Gu0-zrYdrWJBqrR1FYuVuUepwGSxtBmxObkA5SX-7UFEkccmEmlpVoF1t9pssBrrGr10E9NOw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=qTFq66AnDX8GIOqE8PS1SG04eGIunabr4iqXaJiiDd__JDtKEl7ooqLGPE8ovHs3RicnfmZrCM39ZrGjvmOyAJAdpvQR5rkx6Nxb48grZ8Ec219VwY5u4whETp8XdKdXDCPNwNGEwqiVGos_8M3_XdQG63SG9qJ5IWbHPzifCJVIGZDcYOrHbo3CZK8UpAMW1tqz3f36V90e7Tk-ZQQKXVJmun6YV4M0T3W99mea0CWS1TjBG3dTvdF5a5GILyelT4zz3D8Qqt7Gu0-zrYdrWJBqrR1FYuVuUepwGSxtBmxObkA5SX-7UFEkccmEmlpVoF1t9pssBrrGr10E9NOw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyVHDQkRd61CDRQCR8SM8NArdzqKwmDeEZHw2rN1bjdycyeGt-wkkg3D5NXyzNQ5rh0LEw65e-BfQGW_1Ea6jXpq1agHro8BZ9LvFP8Ym8YXIj5fapwaAe6WOwKKSJKnQM4TTtlFjRJvDdXFkB_0VRzLDNTqMRCyQANu9S3IZ4xN2Vc118DfpaN4NJy0w-raF5XhIJcRYYGYh8rgDbT0ziW8UF3rxNFtHTf8Ie_yozrWCynA-MOE_eOBPAqu8K3bDsgu7xMa0PvsULvRzTd45lEidk7n6QaYYPZUQGP_pUMbzxqI-Uu9D1hhqKrjYBfeAV0kmuB0xUh-IbSHogoIVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzRnCgGI8065uVcoRIZMRTXYppxiBa8ss_NqBIX349XcBNTHIKGYk0iSQVnx7ghKjjmePdPDK6CbtcMsDGL-Nqa3mNMlZ08eQvEPnZ7q9bOTXyp0_EwT0phPs_GK5dD-8oR8VhgAW8n3gz0T5gJNG_iy1eWENA4FtS4SlFxgpmfFEJ2ZuNDuHz2n1KWDHhAywJ8BSOemonMjMZx7PC0TrVQNNPIZZp2UG0GeUbtbY5Hml1f1Er7vVRV4YQHZekHTsVwkDMdnbUzoDH-qKy85TfQVsjBqTmgc9J_LB2R7e_SBm_jPfuJ4kGnIwM7aJRvlyh8EmJ0m293YCdE4hA1QaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVWOeLvgvR0jCMicgoc2a1-xTijZF0W6LELe6aUeZIE2HouqY-tN7sVZJBp5WwgWVmeRYhlqfp4k3Mz8PJJAM2eT8wYdTiTcY4072t9KDkF99hwqhHpLBVqqiGJm2pyIhZGSPTpIKsayVs4HecUIpgWwWwm6swTRy_lyhuh2Hn94_aK6Sscsnb8LqIwPVBCcLWOReVapKfxiquo2S364JsEyi4Acfhy7WjMBvdZNgIKPxrXXa7FK2ET-RBSIty-r7AXKZfKOXlAkDWRy4ZCUi_wHRMJFa9unApuifcrv8506HhTbO87uS4o0cvkg0ZOqoH7qAnO7pL8lL57Jafk6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfFjO1dOW1I8BsmgV8uAfBJ3ces8Fq1lBw6ppvQQ2xyYwLBxKiAszRFo7D7pHxfTcZnc9rNF-KhixG5SnBya1sVvmmJ7qM4z9APAzaMxjwrce9YBLlMS43j0XixKwlzZhM5tS8IeQyaVCnpdc2V3-s5_LuaBOJymDheaSIoUpC1N2glV0kJSR8jHt7L3gFP7ws07AZS07qktEqpwD-PT5ZVZqZY7t1FpOCluLvgo4Gtb81FKn8CFwynJOxN5BqrxvByAYTrpbi99t5FMVY7q-ZoUx3C6kT73OEdOnSxEnZya9yMx-8ybf5wlUaHlTZ3lz1J0TeCZMgyQ2zIJ3ALJfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjZ89G0BWV9hAaLtf4UMesjte5pPC0MUwFKfqqVaFijI7IE5BwriH0xV2FT8UU6TPC-1u7R6mNeRpwL518wMUIGUJxXmzxM2XTQ2IOFzIzoQHr1veOzCzJ6pPm5wtLmdzxmJ2msaxKqToOZeebghiQxW9r1ltW58DUBYz9CM31r6xxA1caZEAgOwi5cTx1wTKv9bYDMucJ2r2uK4-0BJlN8X7GKdeGpNvDi1b2Hdf4tdzJpIQCFVItDEikKUMOWUSCf0g_yP63lEMq0QGWW4o7MV1zV87Wx4DfJsbdWRumVVUJO3kH1Ujz606yz7E6KQ-xaM2QTAsPNPMMavwWXsMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=UiYCU2GfOqIJLEAiploKfKhGsVBk41L_hjbF_58t3Lr6BYNK6ZTVQcm10Yc6eFgUQGLzRLBDe8MlmCn95PzLbiLnjYStqKzl2R1tKNuhlP76n0CrKvesreh-Q5JxWOMlGVVIum0it2LeNMngPjZL8mohXyOqpperAbOIWxg0eNznRwsERAZzJKuX3_Le4s6TN0LqGDQ5h-6TutyWB2oSxSIAzb_lAQ3zsb2_LChHg-mvxYaeTGRZja5k8fwvaren888o_TU_uT50kVGGg92hnh9U0gWHBNtH_Wzv9tAw2gGc4yI3BFodf94ACL9tEMT9Xxn-uLTiZ4SZ2UzyKBIsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=UiYCU2GfOqIJLEAiploKfKhGsVBk41L_hjbF_58t3Lr6BYNK6ZTVQcm10Yc6eFgUQGLzRLBDe8MlmCn95PzLbiLnjYStqKzl2R1tKNuhlP76n0CrKvesreh-Q5JxWOMlGVVIum0it2LeNMngPjZL8mohXyOqpperAbOIWxg0eNznRwsERAZzJKuX3_Le4s6TN0LqGDQ5h-6TutyWB2oSxSIAzb_lAQ3zsb2_LChHg-mvxYaeTGRZja5k8fwvaren888o_TU_uT50kVGGg92hnh9U0gWHBNtH_Wzv9tAw2gGc4yI3BFodf94ACL9tEMT9Xxn-uLTiZ4SZ2UzyKBIsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxhfIA28bX92kg4kr4CLvh4MOdmjjzXodOLrbgysqi3q0HHG7DuBwgrY6SCOIp0jn7srmWLtYqu4tlq0P5Vu2X7bcfwHH3naoMJsIzpgIbX_B_vyTClU1pGAw8NgTaWBrdwxdAFqdBlyNoVGq6JNxUcMeyPzIdBPGyTKCjKzweAo8_uDl21YNdiKWOvKfwI1mAzBH6pzgKDH_-3Sj1oY3zGX-bjjysy5SoCA1WWDKWqVcCARHiwM55cEMtVxt_W5mIak3HkNSUFw-Tw-bo14q_OaV-qlMxLBMqJqS9NJ12sm3_NZaoEn38a7E-jDkJoHiBTg7KuAywcWmwM_nDc-ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA7eiOIuy9x0qwvOxKPADJGeL0fJSwufdh5tH9hoCoXx97qFILSKlXEe-OErfuL7T29wyQC2IbUMHyudqmbCwvpz92xxUvggWKkfe5kHEadXw1qugrfAE4iPIxx07xUKE6o3LGTJsRmcilZEXXOZindUGea1SlYoEaMLyX_iye2m5RVRKuAyDKWl3a8aso1zfFUEEOIGSDnxFNtwhFZNHW-NfVgpyvGQknSDMO5wAbJ5OafxkFS52P94CpeIMplzr0BTRN-zZ8W1VgsgPIkDSiXtkJvb2RmMhK5hIVQRphtvpjZAXDg7glcyVI9qFuyh1VrbWLoqT5BW9C-_GNGMYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds9-5R6Z9hHCs885BL0ONhlEl6QTwodHgwZCPOIiD2SSUNkJNLlnNy2VMF3heGx_CB2AntJPw0RB9CboJjaO4OIpUyWxv05tFKS5VIyLctijBTIL5wJ7-xgnR2MkU-vMjFF-EOYHd2pGDFLoS7LUFxgl3ESeY1sdAzGE7gLW7pFb5NdvVFhXERj8WdrhsiIhLdHWd-4USocKvx6cdPhnhEXusAqi0z0xQm1muFtl8iGzZ217DYFxKE34VIZNjSR7lSImlXhTSjDnEnqz2lBtkbdIlXCqk2jClPyOY_Ad-8Sbv9hKDAOk7TyC70jmUYVT37O_iGErpVs6BxfK3T4FdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnB0UtrYJeDQXYJWRDYrqtxR6CFYaYR41J7QLW_abunyUlCJHg0WzwaWvjRVHSdsD6M2hvZSuMBgcdx7oC7fX6lF1I_qpoN0vzYAiPnfNn9Qd_Qd-ej_VDR3on2khZ0Nqsx4zbRkupR9dAdIPPOo3lMm_GbOyK9Q_SMVBEGYR-3EhHtXCYORuZlXarO1LKBCgRRZunWBsvtojVktoqaZkXEq0uWmYVm184obnSzyaDu783-hgKRvegPxYdKAN0dFuGGWfjEAXbE8jbp1LrkRBQM3LhJ7QE9SiMwPf7JQzJYuIJk1w65QDUOvTObPZE5vb2g7C_ZMhRy60aiVF4oGeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkzvFJxDhQ1qvDXl590TQ9OC16-uTEDhbCZmBKR3WSXPvUuXwFYB3AzA5jidwuqlQI5a-EHy_2RC81CF72RDhYknzpDZmpa5i8RUpN3nCgH2jiujj3VFbsCZbf_8jFt-oRbXaad-jloZ4d-a86a4Y5pK1dpTIkm8xwns2EaJhBdQuk1Lwuem7be-f9omNPl09ZhgKFG4zpxvCs0Mwc5kzi4XMpRc9n1pHa3D_SjMbWhCW12eBRnC4ql29XbZGFq2mLVivmtTszgFYHAnihTlI2V7bVCebxIwxa7sw4ewube4AbOyNjFpgNW0-UO6THW9GyXI6x9aIMPNPguxe9vcpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcxaTxcHXSZD2lu6d5HNzUCYj_UG5ee6wYOGJtpuVVqlNoRj9_dLHhgTYpK7uc4X-1ByoTZ3JT0Nk_h2dMuqiPAY3NU1hxO7QtLBR2YpIJx9maeX053adI8HHQ8sOwIN5cCcW_z8Kp9k0wZASDgzGD2AUjoy9F_aelVvVMPMRKvEVz4w7Cfz6j86aQiW3VjAK-gOiDjmspWcNXQRDzs3H-A38FG6Te01NhTZP67y5MhJU6-Qh9ztkpuKUNAItxhYN9IqFD0UfpDcEULqoH5yEG-S42JIb5cXIZTdH_I7MUhY8g2O0R6lSxqTQFoDIXzVJmsZ-UdlXOTCudg-6yF8ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPB1GsvNYd0IDOyqn-SojT-hpgQHsB4pi0vAbhDDCY1Rs0g2RQVwEC-ANSJWB0mcwOCmy8k1NwdLrfnRGOV5HdJCPUIg6KiLzCj6JG9dbpAcfQAkiKt5dd4tj84dbRFYXLpdVAuJt4kyFCOTUkG7ullpE7DJdqazntJKxZquG3T7o7IA8XEzkZSWPu_wQVDoJiBTUnD5cCD1YAIm4A_BnPmPW2tpRBMKzfdBm_8e33765l-ziEv5v71QmBFu6DlMDUQRpR957Vz_p6XAxEx2-Zh7sCFH0XYbD2VDoqRdjXYB3CgfHJHI5ylOWNNO2mp8UDmtCbLIhz9gMo8HK3jRdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VLxSYHJlokDIkOZIRI6icyfDNln8qZkhEf7fUzIJpzUqqQchSPYpuDPYr9jRYuH2rFyhxd1rMUy1Vr5QRjtzc2_9p4ZZxL7zc1OoBrtNtAZuibS7N-RhX9Ff1BCV3e4JAwzpf3nX80ZZQjmlUvy0pwzBxEyWjI5XoCFQTEuwHM8Jh35nl059MPL4c9y0Eq7Za1Ed8alpmljp3v5_GYBagg5FyHSUg-IRLa8qBy_BdqCUp4v5GOZkyKrp5nbD2p4gOHHczQmMpr_6v0qHJdng0vGYkdLAyt0_gyjTwiMiah76dgCG3HOar7hDDpIMmDGfmBcEKrR8Vf6uE9MQefaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu_X_xlfernr4U3y73zFczw1_4FIRbZwR8q-WLtaTQQWaoFrGNJQ6wRljvFj4ELZEBrTP89CF9R-rZEytXWEMLVqQqFyjylOASYvz9lRXhdhTkMcI3Vgl4kwPPIqpLGh1S02vM2cTIhvQKxLMfeKKwoA65NHgP6m0Lx7gMBCf-6rtpDqhV2NT1oWria5BNkZZs0ntbRgS9YfWXTCTdRshTyOVWtvmsw-IJkQKePaXBOmf2Pcqxmo-pxNrkOPnxAHBlBcay6IHo6QsoVhqo13fN0EP5PfL0A3VpLC8L69iw6TbN5wqZRxqX6hX6gwf6oOU8ZoXaJuFvyIxwxiSRB2WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVpPL_PiGYl6-sZbDwW2IzFJCLu2AVM4Pz7NxQg2HV8PgLEb3YPZh1d8up67s8olMnhJUf7187kj1gYGgPZOXdw6tlZHA8LpLn9Om5yFeZ2YzZ8lD947HeZBLByeEQvsxtbRh7UagJCSkd5O7btrDC0WKh4HCITvfphbAfeWjeI03lC1Hxm4EYWBqyOp-QoikihamtFiPoHTmQqTQ7r70-Y38IOGxvu6fKkLuxgi6wA7Uy1RJpzvbe6jGdVbjisulIQQZ7WTU61pa7reV7LlcLHoePUrIJjTVrpYrCZYH8f7OG6qQMpVzGQCZS_T_AqzKlp8YOq1z7ZJhOLOyI9dDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJ_R6k1OvD5NC2VD-fMhQbpsQ5ioLzQ0K9ehn_8atHdWQN-j0zmPXUZPdSJF0exvaN8FOqmJ1zTouxi69v3WrYu3FiKqh45IwvsUmuU4YmVJbEfIhW51TSqjGHyOqArg_s0-qHX4OlcbSlTSMAwqUBSKkot9e1xEo8WU3kDpjvwP6-Mor7wELU6j9MGCInILM9aLKg0sj2fe9fmLONr-8fBUT7k13gDuyIT9a-mET-0NNcexVNZyGQLqsLqBTFuJTedac4LlMn9v02bOFIP4AJlFCMMwXxJE6IvyrIXu8LfaLknKflNOn-MYobJs7XGh1tHsDSDVFSxkE9P28l6xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtcXZ-AFyIb3j344ypaK-jk6wFPjfX9E1pyA7Ne62GQ48i71dO-YainxE-W86NA4CCkfVKM19xdkekqpPpBkmh4bGDcBGOxjO7zALZJ5P0sWWxGkGGR85xNNDNxXPVlLCoVXdyX9K3ooJMubjurUVVcW3VJ9CJMCbRl5a5ScWOFiSf8Q3lGoSYMYeV31yVhSAIHE-g-h_gQ1g0JetM-1xqxfXjn4BbAXcq1bRWUXfy5bEQ_HO3G2tCx33XIuREHrpXohFSTFlF0VSGfVHOWn9iOEw3aFcdgL_jKvM7Xs6gJbm7LVkmlnVyFG_yv590JGAxAaxTtcLcJWVHvJQ-IjqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcSkzF22IRaoJnuuu0VUhfeNuBRWCSCB9RM6LpuP07xLe60vrMMqIj07u6JxLvGDtZnBNSWh-qE6AtfMRmylI85LfcIKMaD_vQ0cdtOpwUiKYQs-FTyFwxaArFbfvr9fb8FmuwDC5nxAjW-ZN4vyu_jkyrGaYSoZFaTYxVulxqTVLw_rFKVqaODmwWxMr9iBCSObVOrKYy1IuY2frYe1zgpYCa1Yju1nwC6MvNEnnhdfNAnhWUnx0jMyGY2A9pLjJZwt-YszaoZloj5HIdgSaetAJPYYGJ3Yhq5LtslSC-ZIDfCqyXzth_s8h2vyLtwyYqa5PImk1r7aWSz22xp9pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHUL3GKy79hLb55faoJFdaVRk7axR96RRA49yjWCkw62AJb6lycQiMbtEYFdyPsW3I66pEuYLnufJdacXbYw1ngzrZnDObBjjmNodvKlNPb67jSJpE1aY6Sm7uPpPKGZLxHCTKCEKRQXf17RM1ZcBcUwj4AGISIXkNVPLrnPG6XKkxgUgxflaflm6wd5fl6-0GWrYh9PmSY3pEkXOK2CQ7MvV0GVp2x4fjHGCMnv-7-J8ySz3ozIw7GZSUD0akCq_pqFH2S-A8-fS0QWzmnZpTXoPUNoRsaI4OBGDzKLdTtGZSpz9wGDrAIhZ6bQmsGLneyvfgtSyNqfOqpcOyPWoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXG-4EkMifYZC2ElfUU0XOMGWZgBj7fuMfQkFSfPpHHwsL68uZjyBgZC8TQJzq45vqne3KkMGzlEBRlGEs0Q3Fjj630Q_7zohvfpz_FSQkOxn3P0zC0970cMUARP7aMuIx4_ieR_O0LS4UmCIJrSYUPOHX10cL70Pa94NwU18CkZHVEm__tgZJMYWqXS71UjFnhT5ZLl0iDrNiJMCYmoRwsB6QnfMue2f4d2jaWYAznzNG157RASaq6O7aqzrfvvBRhtECezdjhXft9sg0wfr4o15phr-Z2xkYBXg4MI3sek4wZ3uynp6bxaOv-blAIK6jHwEAXivl9oLiMsUNt4lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhf1X7NqoWkI1fgjugxI3SFnGnKaKF1rlkuiDz5s6kC_HCVnOJMOukM49qQgrKc3Wy0wc5-Dvay0qvBuM7sa9-9tkjc2Ze3zLE3wlMPBOX1sp8YROM9p4BEf0O08m9NydqGWwEsUC3FjLcwIDsk7Kr01QljCsgEOgqIcdFusrI77IEDNZnh3wQdH3BfDj5HNrYBtqhDRdstpebRBTg2mqnnaryoti8FTU_9n_JnDd3F8kKpeONaWPeCx5VyhlIZ1-vhPUTRA_wJGodqdq8c0zAMFxblgv6fwI3HW8wuN_L4ypsu5UkeTgrCM45psHKvcGECYC5c1QtANd2Rvm2MCLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKTOFkTQPwSnRIwAe15-HApiwnLqFKwsYakBbe-bNj0iL8GU7FuwqplVghEQI93RveNpLKLEiWCS9vRXofHaSsPOZF5ztVRrSp3gCJIBgJl_WeLcJJgw3oGNCD_wzQOqqgk2Ntv0HCQ4PR5QH2Dxy70Aq3ex7y2GnnyU67TWN6buFtvbk6k9z_Tv7zPYlzIIixd0vSH_wkcqLbOHiSuyo7zkS1tQIim8SEt7dKEn0excstYdK7QTwB0vlooVR2lZNfduuR9QuYrJoGbxz-pXSQdtITM6Kkge5V40wvxprrUuqZjRbnPyzpk057PuK0Cd2z4CVVB6QuPDqk0mtqLRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG_w43bxl1FWRKJTCW8otDZ2QEPQSuH_RTOnqlblwtlMVrAKqKfJP0lOjljto0s1QH-oJDJEi5iUO4_1MtuMkUasC6NYxh0H0lJy180EIUeUXjkEKOhLUVB7iEYyNgCuabSofIM-oIQW4HZj6XvNquelsAifLhmfOAo62AYTmoOc4Jtfo0Sn67fpX_p1NCPM51HNs0liCs_mK3uwXUm5ZF0DMxzj7MgyHJrnBCnCOo-PWAMRf28pqUE2t-slDb4DkAQrrAl6PhRGXJ7imi_emi6sw3zp00a4mIVEr-j8GyAQjhUdj8dn3rUF1PS---uXVMSH8BGIKUhSUS5Bza8prg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDYyzfLH7GlsyLtChmW2PnwQ0EUiFABeCHvBXh7lyG4OwDc8I0lJQ2U8xlaKOlnsp2OzVRese9f6thXspVRm7gMhHr4I5NwtVV2usXxESz8T0VYGkZOofhv8KN0TSd3QeawMSA2O54tvGCGIxuT9T3bwecU7tqglWxTVpWsQTw9jcjdt2_YX6-8PKuKAs6XR2VjNCr4EzGEg16NnIbDqky0rJKLiRiz3JC2oHmuqjPY8dkE5abX11XTMHj-SZ7Lu3J6IxHx_Kv3S1lMP9C9EooYV1YzWzpcxCsDGpMJhbTY635C76pFu5RUh7-ENESgN3FYKRO_aWg1Ju3Kju6oxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=fe5rutMdJHbZjEleY3GHOai7BSngbXeJSuSPONkj6-sCxkIogtpES0tYS0csYYkmMjRWtrGDbR2Kq9CjGkh_X3clI1bTpAxDd7yvROb7epVYjtI0xpJbrFlPKWaC6Nmhldk11Jg5uh2fAFYNJrr6ygknBdOPjzfl38AXx5SQyK6s27e5VKLC2nchQKMPnNe1RgmmjodjIET3ekbTgz06iA8IW7JidIRE8Br1kcqmGq8K4-jkoah3OYONUsECjisAyl-iYk--a2iNXl0RSEY10O4tUOlzWJar0U4eLmp1cCBuMjYB0A1WTUr4Sm9Lh1es0bh98rZtl8LA0saFtA6o_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=fe5rutMdJHbZjEleY3GHOai7BSngbXeJSuSPONkj6-sCxkIogtpES0tYS0csYYkmMjRWtrGDbR2Kq9CjGkh_X3clI1bTpAxDd7yvROb7epVYjtI0xpJbrFlPKWaC6Nmhldk11Jg5uh2fAFYNJrr6ygknBdOPjzfl38AXx5SQyK6s27e5VKLC2nchQKMPnNe1RgmmjodjIET3ekbTgz06iA8IW7JidIRE8Br1kcqmGq8K4-jkoah3OYONUsECjisAyl-iYk--a2iNXl0RSEY10O4tUOlzWJar0U4eLmp1cCBuMjYB0A1WTUr4Sm9Lh1es0bh98rZtl8LA0saFtA6o_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P64MhjFlrqdY8JLcDwNGl3Y9Ui0boJR2IEEMBo1-RSwbULnvgy-611EpFaauiyMQ28UNP3LR7kb8F4vxG2QXiYpEfYgYkfUejDityR4-sZ7wd_ox5WWB3zfhX2GVqc_7zcj4xeH2hRUImONqiwvZX9efmyK0FC-NFYODKsJvhgCyRN1VOcjaOl0eOgxfXWcEZwG7jCYc4qjdJboteDZeQDbIi4xlASdHXxiqjThi9dba876Z8vDn7g4RnBYEYoEDFPsYVMTLcVUGlqvd5eE1XSw3qLzAoP3PWbwjwffDgwY21c-QeMibDnF3nt7oEnShSwiSasskhL7nBnZmUXzVIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiIIbMMV02Lcxsq6HPHy9Gk22QxVzosy15puaGT6iamWCL2thL2FWNLJisGJIg0T8J8eAEvzNItL8g155GzBox6H0yfi5JeWFOtaSx413P64XhYYwu0F999bweGknxfOuYO-B1_G9li4BO4Plm-it8LHH89_tse6U-JfxLsZ-wM3BHUsi5WlaZjMAAEKv4R_I8PHRmA5PqJAN7G84hFAqJYRhuW7qR2l-0Q4NRiyMuUI5tgBd77qDKA4kzdvkUwvQ9gPrQF4Ba5wESMgtC982Ymp66pyjEqrYJV8NVHrWzBvl-6NXP9cIeFlTQ1-9BJnhhInwxgAmF2FOq8uiwJ78w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=C6XpxJXLI6HA4iVSqmuiZEJF7BBvt71DMIyjtTLNv5HWgzKygxcetCkpkBo-Sm2Rc0xw4eDGwhPNXfbgck5nDaxftwSCSFT40ACGEtGRVm2x1cHcvh5oOSsdsTeR_Cg7ptAbTECrDNflfFR-ORxG8E-ZuzewBJfBnOeh_PLH5G_BGlh4XdWhSIvFfMUMgElk6DakGVY1fyT9yN9hrNPvLWmiKZR2z-JQ_iegqWg9LJn4rOi-niUJ3wfIq3FBe8ytMITN2QclFYvWmpU_6zPoRRhXNE4mk5tq5s7ujJuDRWOuKdcf2tBGqt4K5T-8jy67rn2WzMensNTTtoImSRpvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=C6XpxJXLI6HA4iVSqmuiZEJF7BBvt71DMIyjtTLNv5HWgzKygxcetCkpkBo-Sm2Rc0xw4eDGwhPNXfbgck5nDaxftwSCSFT40ACGEtGRVm2x1cHcvh5oOSsdsTeR_Cg7ptAbTECrDNflfFR-ORxG8E-ZuzewBJfBnOeh_PLH5G_BGlh4XdWhSIvFfMUMgElk6DakGVY1fyT9yN9hrNPvLWmiKZR2z-JQ_iegqWg9LJn4rOi-niUJ3wfIq3FBe8ytMITN2QclFYvWmpU_6zPoRRhXNE4mk5tq5s7ujJuDRWOuKdcf2tBGqt4K5T-8jy67rn2WzMensNTTtoImSRpvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=VIfCLRKytTfIxt5902rYSkM0PHoq9DPftdvE59q_Ck2NiZfriuQtH_R04fiJp3JnEuPaGjTp99feQQjWihDPboGpGW0dBiObxRrLHPSJKunLCDYSFOx0Y5AyAfufWZgMbMMwnVBVIJHvL8XZedjOTbMHT-lrTAf0d6d3n7z2fDUiMrHLJ4Y6Esm9peN1uR-o29Sb4mv-maUW4gEMRfQTYqp3S0A49xZiO2sAuk_aYdx1TnB18WtmOowM_1A32ibzTzUl7Q1GU1ro6xqjd1uX9ri89N9MjKB5ly346wg80XogDOMCZ8twhHks_P84WE_PMJxyvxbeRpFgbx-nqcIKbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=VIfCLRKytTfIxt5902rYSkM0PHoq9DPftdvE59q_Ck2NiZfriuQtH_R04fiJp3JnEuPaGjTp99feQQjWihDPboGpGW0dBiObxRrLHPSJKunLCDYSFOx0Y5AyAfufWZgMbMMwnVBVIJHvL8XZedjOTbMHT-lrTAf0d6d3n7z2fDUiMrHLJ4Y6Esm9peN1uR-o29Sb4mv-maUW4gEMRfQTYqp3S0A49xZiO2sAuk_aYdx1TnB18WtmOowM_1A32ibzTzUl7Q1GU1ro6xqjd1uX9ri89N9MjKB5ly346wg80XogDOMCZ8twhHks_P84WE_PMJxyvxbeRpFgbx-nqcIKbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=E_SAujBmAhIiGEIjM6CTighJ4VWO8xpoAPfIlRSq4XgCrzrDDsDw67dBeMrOdidDfTEl0VDdfgwXGwk9V1WtHHaz2kMU_o4U6QGwk7BE70FyUmHi_uz1lBIwX8c1RDkeGtsQLgFWPmSnL-CF7f412u2X9yWeHjr9wqjQMM6pUo72ObJ5aVeLBMK4rozb4a-SWcs_AlVJ9-onPQyJ7yDMTXPxEPFSy_Bpg4pTUY3ulGEwzDJEoJG1AZnjwOifY-Y0feyxrQDMCIvhgAkTa7gjPWwVrWfkpAsEI7Q1JtJsSkJcGJQGdzDVjnQcSWGVwoQnInzc8QdJeDQoY6f7BhSj-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=E_SAujBmAhIiGEIjM6CTighJ4VWO8xpoAPfIlRSq4XgCrzrDDsDw67dBeMrOdidDfTEl0VDdfgwXGwk9V1WtHHaz2kMU_o4U6QGwk7BE70FyUmHi_uz1lBIwX8c1RDkeGtsQLgFWPmSnL-CF7f412u2X9yWeHjr9wqjQMM6pUo72ObJ5aVeLBMK4rozb4a-SWcs_AlVJ9-onPQyJ7yDMTXPxEPFSy_Bpg4pTUY3ulGEwzDJEoJG1AZnjwOifY-Y0feyxrQDMCIvhgAkTa7gjPWwVrWfkpAsEI7Q1JtJsSkJcGJQGdzDVjnQcSWGVwoQnInzc8QdJeDQoY6f7BhSj-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcuejKy2ly4_TlgbNwt7FG2V4Se3Gnx5BSG44U1bCLVv1ypqmTwvP5HHN0yL-ennLX9xhRoc7RlI0WZyJTQm49o1GsC5deG23thMfruMjVhRKqr6Bos3W1dyVGobuTFvweG2fq62RsAiHI0O2DSFOHwMXVfo0nLAwD6NKGhmHPdFZ_Pb4vSaldgh23gX-E6YquC0b3uRb3-jsQJRtGqDEgwKiLEhCc9BzRi931BHsyNoIoG56K-qXRXJKTOWSseHbFTDVqgRck9PNJcVJmuu3kkp0S4upiLluQ-NjaHiO_GpHeKpEFtrD2wY9Q_yM89QvkbXHlWif8rKhQvSdI47hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=uvkJ53a8m5iWwh86-BicVnJo_7iS6J0BqEugaO8T5e-kTQK0hVSjKEv6A9fIb2DNcxXB_kxJFrpNhBqyEh9-4N5cDb_QgM1tL98xs9GQCaF7XOrwTIvqR8kY3vhfA52uDr3ilmGwA4G-CuLDFk-XWZk4aX_qKqgWA59bkDGIU4J8wVOXMDh8cPxugnrKiSiFmcCibXrEtEm3OOpAeQ3AdITKCpNcE9hTj2qHQZnvbgtmcmbDr_kh2DoQZBBnPlNAA0kRxg9rxWM2kEB6Y78EcsW4Npue2VKYocgJucdaa3BS3mYzjhftJQR7IFZPOvr5DeXhYnuX9prow4aJ_Ikm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=uvkJ53a8m5iWwh86-BicVnJo_7iS6J0BqEugaO8T5e-kTQK0hVSjKEv6A9fIb2DNcxXB_kxJFrpNhBqyEh9-4N5cDb_QgM1tL98xs9GQCaF7XOrwTIvqR8kY3vhfA52uDr3ilmGwA4G-CuLDFk-XWZk4aX_qKqgWA59bkDGIU4J8wVOXMDh8cPxugnrKiSiFmcCibXrEtEm3OOpAeQ3AdITKCpNcE9hTj2qHQZnvbgtmcmbDr_kh2DoQZBBnPlNAA0kRxg9rxWM2kEB6Y78EcsW4Npue2VKYocgJucdaa3BS3mYzjhftJQR7IFZPOvr5DeXhYnuX9prow4aJ_Ikm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR-DRVPP34MxP1VPw6aR1BLvPBhyXTez20sBzsH0tLI5HQ_VDn_Uhz9HyU5RuTAbKULh1IMrhyE3nnQvhEV_RAuGdN6bHmqEq5CgXMNNvwk2GkSLe0RK8bimD9qlmTmwWkScVddHBqFL7sBC16rchJtCySKvZugtxvo1aFKk1ntbTPIdbvwhsjdr9yVC4Rh-diB82MpvTMwD9WvToCCJ1Ajn1HRS9493Gb75HNOzqD3p2uaqeoOwVm3noQwMp-3OwsThsOA-vrDmdzG9FbZtUOej9TXK3QOdTcv7cfvAwwStm1PBgBX7Tdn0X5BzgzJzZXzyYCo1Cxwnmgd_IMkS5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeXtqqGe6a6M8Uh1Lm8ifJeyMGuGVHmj9E-cKKpZpnqQOyUngwhU1r4P_PK-r35uJx4D_Ksb9xfscJOwxpA0YiDvdXBDwiifqgsQueBpHitHIbv4P6gtPd5vZV8IYedKMshPiRmlFDtDD4VahRcDotBJpYu6GHa7Fm1tF1JizwEHXbJgb_EKnRLuiymI4jqeZu_8oMlpA6pYVZkFvXjmFmIw12w5LNvGIpuOh8n1livpV8JgfXHqOK3mxOs5BdlFptkOLzolSYz-B1inzqDc-3J9nFh0E1vxa8T50-8Zx6kQAVgNQvUO7R3cWXqY2FcF-NfLWNXs-_S1CDDbc0DfaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffMCt4n_M5Qn8W5cCx6aNiqb3y5gbnpNOS9MFsMrxFJsehjv2rQGUo0_o92-KqO4Ie3vbrpZkVEPnxT89TSsW61OVe-XcVcj_PS2f6etVj4_aZds-Rc-Q4vXyYJqCpH4rH5svce4GSFeg_wm21_ElPAFriMPR053INijdtVQOopfTapz1IdE-8hs5t3qPiYGbc-2_R7gNj7u1r9xWgcsqbVBbB_GH7Ng0sFnoumitP6HmR2-X9Aslyf5dQ0M88pSbMDjuBqbyn3DSTfwluJQ2rfgKXzCQf_jn8wXy6Bgkku5Sbov55M6KvalZVWp7Mub3ZCj8MwUuROC0E6_YyGIXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITiNz94HrsRtbzjlPNA698mMUIZBt6nVs4dlvwJ9qwxCyiplwb2XL54Ul6ik8zg2LoOIepCM26tCtX9H1Z99GRbPTi3i_e4FkYI-jkoDfYJ5xXQppqZbzT0Pdr_-P1k2oL2SzxIb8Hkki97sqbQsW7byj83_xxpfhrLl8qzkhFV-08qFqDjwsjlCBRrhaL-mX-Ys7A4oovHECvq2zw4SrdwQ4bn2wH8oyrDsn2wjPSAPNjK7tW8vJMwzhHENZbRrYsClzpiiOsczVTI-x8EthEHu05uOi_L5Ix1ANwmUfedltzAuys9RaE9OolOghbdi-sMMDQEcXCgtlruADbdwcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcP7OiDm1PH6ynotL6fRtmGO7BnW7SpKDnvi4VhdXi14Jk4e_cqQujnS6mCmA2GRpOWEIWdqWZonkF2YgFaSOProL0EDXdCIUFLJtOo3OspCjKeMLe6RImOUIgDZLwhOZN1fAvxpncEsP2e-nKqLfQ6nHNoY0ADtOyzuiUwTmoABAN9IWWTdfchw1lyTXvzwTP1mCjAsOPBkSsDR0rqXoEKGO4Upv6fof9cZTyopqnySYrrmU7U9XHIvEFqhuNrhI7r-YA0aLPjAbSsPo2T2WmEhlQwZno_He4LNTWC37NjTecGNkkKnBaoJKKsA708wpK-UtOH86dZVksJ_8e9DjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOKAy9A-tVxqrrwToO1LK3Z7n_TaRQHsCTSRoZQdPWVj2SwGFQoQPOcpWCBIvWsFYIJK-JRT2mUhPB098IP1HoMF-JrB5v9YsGQlIwcZn2udY3csL72mEBP7r7BygX6T0QaZl4RjN72n6aL8KziDYo09WpGVKyIsf4SZuN923lusC_n1vxb_u9o-dsfe90JjCm4pA1yfBUFDa_JI27iBBsSf2H_5K9dwnXtm46iuc9Dz1qnxQOt1HIcGdiedDTjettUWqJLmy5i-kolEwAIaKvTIR_7GbmLpxW3xaoUx9L2uc4Fss3KFocNNvOTtiTzhQi6UNTvK_5int7DUPmRxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCPGi_awcbujV5JxoJQbLNlOmkmvT3-Tek2CIFEdT95-SAAROxW2-P_A_cqjvbE7c-QEW4SDuKatHax4rZ9Gu0dooiai622pW7Ciof4T9BI_6dcDlkWKJcPyXcnmEw09GZ5oHEohO2nGn2kU1qDH2OC45ybMkvzPXKgR-9LR83YhhkmM06BdJvb4_LVRU7aXkN0IpImMK_kOnjpzSl4f_yGHQRewgxr8Xhx5oXreYVzXLJzIq6rl4-qtclfwNHLUnk3rshRWthi9Eclc1cUpp2TgmXb5AoT9seD-Gqv_C0aKh5CUMMiJ9A-Hgjq2g-TKF1xaEHtTHbtSpFi0O6te9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZPgY30DTtOCrNj8zywRXMgyBqfm1oKaXis2Iw5HgiButNwp86UCC4Et4zOEeG2tzpnidGthyR2E1ezz6jjZGeWNJyC7xTSr3L2YdE9g1wn-zPDSNGV--Q08-a9ngSJbEZd57BYlH5pO2QaEcbG51LuNGqz_XIRmJsJiP8AR6FkHq1sihFg2YW2z4j_jOTVcCcAdHAaB5Z9jKwWV15TxItN_egJiqCIdQWo8tvL_6ufv7RDfALivUXSHVlbIqYQaCa8QBeWke7iqQ8hOXF-W-_7zkW_DNFmk5JNj-xjZJq9Wpcu2OUIrOVy18Ree8yJUHu2NZEA642gYvcevCmkz2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFNN102pScgiEOFhaqkTYXOJmsMlH-rYTl7PgjqyRyWLOWLo_GAPXiYd8APiL7fEyitexE2SwXrXM6dcTb28nAB_hxZCEN9QUaPmoTtdFlA7O9EF2tm0ULQH31FWrF75Wmo3HM0q6UfOQqK7XOzzn1fJyPrKfYNWcxbesoiehr_8rtdxyBsPrVDrQZLpjDiBe6HeKcNn87E30R6scwggwLs12AF35-oABXhmAkcMYXlAMwhWXLlsLBkSmqaGPnpcMCdVD_DB6vTyQWgCjIrIkGbO67x9NG74Yqc-TjJVG1PkFQQPX6lksYpZ87heXEWraOWjE-S4EadHTHEvA_ymQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
