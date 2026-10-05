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
<img src="https://cdn4.telesco.pe/file/kYmTTZr2Mtk2V3rx2IfN9-MdnG6mnZus1SsllUABY792GXI0aZBg7DrLApwjjToqRjvdLneMO5ivcC36YyoZvwXMQ-EjK39ftHzLDuoeMMkW8tQ2gLaoSHorwgSQU51HnnephB4J1cnM6xySeIyQjt8mHjwA6ki4OYmhF6bAo70ymN-D3mMNn6Ow1QuPB3-QYB-zKTn8omVURsVKOXAcNGCgVHogPNBEj-WxxV9qV8M_UhMLmvqPw-j2jgRTf9WGOQUrnvE_i-Q3JWF1ho_7kXFoCuSKUuBHynGSQybZ1GYihoLznfKGJAryKE5SmigLziIf94xwDPX2re2zmnlOzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7982">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ArchiveTel
pinned «
قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7982" target="_blank">📅 21:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3NDqfJ8wgy1gPQJEKHOikUjQpeTaTt3QXyBbYgURz-eE6pXY0WSBxEiPMVJ5HPxZtyBQOd6fFvEALbmr1nGg2rXMHITd766bhUWXpQtwjjPbLn4Q8OIAd_bo2jNWhblT_r0l3Iw2MbdyxYyt0NhpmKQpk7GjUXXh93OZs-HQgsJbIoz7nOyk4j8Y8I0MMWEKclZapr7ElfOLCdlOIenSVhj12bmjoLX1dqxGqDGMULn0CjLQ5BeogiTvRttX8d_63Q1augaqNgFIyQhXBdVr7zQLyCz_Iqpn9hLjUrlF42vmSkbyZxnRsUDbr5aFSXujEh3_cy9-qXzs6LeXMfJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A00oCe17abIhBQDeF_AvdavuUlMkKyfk6f62kbKVFHUAgd_S-olyzvo00w8wpzMEqWJRliDbnogu8eZMqWWI8Mmh58IN41LIl5QQ-emVvx5QWwtaItbjKfPzo4A60p9spd9U_jTWg2FWgz64QoVJqEdgm0BQT3cUqOTWYXRMVMsYI0a9pWiCYpQeqgsqRHughjY2CfXYEe__XPBIPCNGZBtddSfVtWxfv1I6_OQo71OUBMqNwISueWkdH8sIXh2botwRpROBprpXaC3cNzr54orlf6W6povve_0iQX9_xYekMRSarJZy5CKz6vZaQd1feRpAhGmX1YuYu9HcN7ZJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucPOfIUZoWp2y4hcRxsw6ar9eHiBct5BnKRW6mi7jPoaqq6aEBXBjuEYEj_mHq66GnAhVym_ug77XPtqg91j8rsHdhvfaMTrasT5gB_EPgBeVrlLwP9XWz0Y01pWJPAKm2gqTJukUzzOVMqHNKX2txmrIRYeAHmZdBQaGJvayr8bYzs1u5T54jHh0q9qum5NVbPAghHpwtJTTvx7KWCrRJXWuBvpv4C1pRJroXaqQEGgm8Ca8RDmo-L8-AO7laG3qb68NUA45ncYNnNaXcXJxmNjXh3yEzUwpmIqBW0fQ6aa_3gNk91GT9xV6vaLlMjmM6AnpLjUBZpvLM_YzrJxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8m0JWbOhctAf_HMNC5D31kv4qcebW6_-UHWkGTCUgW24OAxegon8jWm0npAc2DG_RHiMsR6ct2D7jiQqrG1njjwZydYXAB4sAHh17u68zouU_UpNYC_xO0Vr1uL0MOZLahthOcU-UnmfObJT0oxxnAKhxIqSb4u2zvU61jcRyKTE--iHf8ZOORMZ-pJX-WylSR3fed3XI-GuDvSIN6T0DydsrU5wIHhxush2I3JkT7W2Yc1YWSwwIMAHQcuR70oZi5KcyIwdeIEYxEiBJg-txg5urObKvADeJ2gEXQrdPiZu3YmifbcxHgaWvjXF0PV5XeJ3gUvlJ2rneOStt7YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9KQIjrNxrg9zFRkRX1qBIsLCeOgm3Gvf0oHfPWD3E7_DOIt8boaNNJvXnEDsUz-KVQ-hopgxAUdCzKRMSJ5InmayQQlcZIZMt7qsXX80aapdAT66yr7hYTzqw-TbRhARN7X-B9AEjzIuTO47RfAfjPtB-lqMjkIrsbG4lyscypoflYnMwOgrHgXkf5fJ7XJxWbOXBaXrAvNq6rL1wR7rAS77l7MxkXejEibbY5_45DJfEv5PMHIzSJEeW-zFuw2TPEDghawnxz4veAC5JKE7ZFnwrkGv0oZ5PdFVIQxyt5XD8WIWm77Wcz7iG90mMPqYqQ5A8YXZrLvNxmpLp7pDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXhzzuKF9r6jVlq5_J7MdkHrPTwgHvEF4DpCkAZlc05qdv9zOYXws0owcCM2IeJ2oU6ysFdweInMfHkJOK4Vth2SsHkoppv2T5Gne61HCbRZMlUFKUE-Y8xeGujFJz7g0LXVx8YxE6MFsvEdrLWA9aGM0xpAJ7hqDrFIS65D4QTQG-iBkeltIX_ZCh08dUOJbqUSIWp24Dac5jXI66GCe2SoipzNtkN5v9nPSRMPOrOn6cUGT18bLEmr_0rLdZGGA8L956bvE32j4_Ii7N7uu8ixgnYmCFjFxcymCst15sjsktOKLYwOVsAsO-dxDttINsiof-YY_jpDH04XqGc7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG5c1XD2II0_yFkxH1hJwJnoV2dqWKZ-5n292Zu-aYOIkNOj61KvnCJ2hawV18xVP-BkRaQNv9Qlmt33y2A5MNktrrrMIj2xEo3mTINTPy9foMj4loQr2iuvi5Dl7IJ0kOFMTAQnHpfMcqQbR3iaadMxLh6jhKA9mcth3a9D9ZPIVqqjqFRDjQebdcoZMS2UMU8WGjnWchlJHJI__fy10RSdNhSt2K8t8JsJ4PiwLHqycvOA8lDbJpk0756QTgHBzSR_sjGHXccC8ep-bLhH1hXcoB0UOAjtDn6nWx-siJDWE7AE_BhyXFtgbdSF2t7fFynOmmzUD7eF0PPg6FjAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4jojq2hntNIHv3LNnUbgsXzgfoUFmeP4VTOmUTlZgGPLg4-uyVTbMRonek71mFl4PHfnLAuhIKRitslRoLMSVMUrrl59aFGsZH_68icImb2nXHED4RZq1yeqC4-BL2cYZHI8BzvAhmCm_Qeq8bb5q-rkj12zAF2_fjCNB0LvdwETpfriqx7vkWSgjBS2ZFXCrG8ncpU96uqOb5zOfyC0quTGC9EhDq7yyaWE_WmfuGLnElbx-WJi1bszI0CKlyd3cU9eXKpXDxUMLkXcOiiISlhTUosLP_lB-cxhuktrEJx0UTOhRfWdAYHGgfWXK8DbMV272fzHVfqqrSaM6yYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_03GwYPu8o_wlkleU2o-5utaJ4lgXkebj5ugjFyAj4emsl1tsvNq4axRSNjEk6bRJxP_3gLiPw5MectOH4c2To9bwr4shxm2RW6KOl6yMuSFdI-3Dadnbh5R6Tgb0n0eGwjPQjU3Wv84v3xay98DmOPAnZ-CwL44a58LWwsdhyAuoo7MVwPZDwEPSKpWWcb2Ah8K25IcCbGHyDOoTa2Ja2EhLbLXUgz_dfFmezJBciqjK-LdygWtTpCmydvw9Ujxoc5bSsJ7zG--6HESWul9Bhrb5oYxNaCnO7rOBCFbgyF5LBbmifss9Ha_aLGuMRkuVzXTx6zfKGN3hmFov3ZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEtGDTpC5tjqbvy5Rf_e0WpyQezcAng2yj-3Upsf8X9EBPQjA4XylXMIR2wtwEUTOUpCVeQsNKkfof0D56XIxca6PodoZRfyMSTG4iqT31jAiAcRY7E4h_1gpWfWKQ3yahCXzm5sdtuwEHBeJgArUKqt1lnB9RHRg_PydtmCjMBtKW4ieR8AvXNgvH7TvQ1DZ6zbgRfNAvxycjbFgOstLmp5rD8wIKLI-T21Al7nKgAihOAYHCFu3b24A3MmNCBz8UXX1z9ukv6yGLvGBYwqVqHTOet96TRQzRnmuE9s2iw86dIJff7q59Ltu3G_-TUdAxlunsbBsYQhrqPUBkadIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1P-KBcCN9EaAo2kUgcVsdCR3F_KaXwRQaJGGXAIuw62uhMKjs3fytSfGdFIgG4KyLAaCt83jlIaYXjMcVYX8BfPM9G0lfdCrIYrFOiTgGrszArnGbU9v_6RW6F-Sv1VP0AGA0O2SgQXx0PEbF_oNVEKXkwku32sy0fT-0t6tcS6KsBv1OUiyScPUqeJCNgNTuny3RHBwmkTaXWPe_qVt9acjIfCA2MwHDv4jDUe17uZ26eKHUu00Dl4yat-GYwrpTmAAmYeJa4s4jtNCyt7h4ZXadixFnW6qOSwtKROFpwi_mSMkDUl9sqUpKnzcRnPEG2jwP_NAFNYJIjf-vNP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ke8qcfHspnzH-Fqj5ExEQfw_23hR8yzUbTqgzDG28Ia8R90Qmc7SfQUUMZqO18oTUO8RuQfTcXeKlvu6x2cllnmz-aChWd2VW6JW6fiyYCbEFYC8JC4_5n3ICgieehcS2Ve3aLZY_CeoyUe5tptIBQUBWE2x_ly9GLzJzQUM2GEDy9lZIH-Z_w30Pmhg6oQ2qOQ4-HGtP4KBMI4PbxbdOeCCYrExC1KgP3KO11HcuMOSDFpYja3kL_6ItXcjHmCtN-7XY8PP11Ba-NvaWRF37UWlmYnnYq-GH5l_crnnnQX1auMAHU0Gtgy_5sWGB_FMNENvvcEqxvc3r0ZVzoYr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiIt1vKvgfncPe-P1NNBRdz7KH-yD9ej3Z2AG67IKf09WsK_DW1XwG-GH_EGOJjjZoyoL-YublZVNyCY6Vyz08LZWAiNeN8ldtCBSViiWa8PL3hVZ8nf-rfT-CxekzrUyOhSgEfSB6IbdQS3w7hL056HkEaf3OpZKSD3an77YhdlbjO7xw_kBH2_4dM5fdebOLw0KwkPUBDtIdIVC_KRX_vFH_K8RzQrCvInMxi1Nh1DGandQ07OLhHRdn7ZSi-AZkW2TJ2ki7_Zw5DIa2Ikc1v18FkeQ4B2EjE5yooBKgyrW76GoidUk0zJwsMeDtxdscLW0QA-PF6uT5HgWZIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJefVPokZsZ9p1Ri2HhKAyAlRgrjEFfgIwjPMi5KcRCWjojsWtz2lRnjTHDKZr48XuWcan_j-GCJfHqwunWjQkZP_d8LFd8CVHW7MfC2EfA3fnlP5krWzpHiJBJY8U8I1-Xibi0kBYd6pT0JbPGHOUicB8zLdgYsWBXIwzggs4itNveXACMPzFmn9EFPdI7UQHS8Ut4FlbZxnxnXhk8qXO1h5CVvANwKajt8kk8WMqlJkgaH5TnBEPJMahL21woMgYYy0dlF6_HBGHEN8Onp9S-AOWJFSrPefLdXXVTnkjeTihXv77eUiXyW4koMYhklp0I-ypy-IvaVEoQcBXHnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f63bxLfZ5uE8rT6IY4xOYSLiqdXB4TMn3v7i-rpt3anA_H59ebFDf-YLZxeYf5M-LIdP8xfI8SYmGVwHjCVAQ9griX0Li8aMNQYFN48Fyta9Eiq4ffhWvX004eckdVi_PibWlMwBrvGzXGWg318UIqs5Ca8rjwRjwRIfp4tyPSpW5V6llVlTKCpSbbn_80TrvrOJUayxSJVq6Yb13aKa3aiQWuF6NciocbNeQHJxRWGM6_-hC6RyQAovvBnQPqZ7Bs3uDQiDcflkUrPgWo2usizRYQhhwOu7f3wsNpeV-9KbaJOpxCuAKtrDu2AUOqXF6MyQg8XZHcIj8UoeeeCG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsxtrKHqRqeR1JIIcDGaJursFwxQC3VwqXrUBSmUVuhj-q_H9LmDH8kLZkV2V5i_xMz4DA6VeFhkiwuwoQ7ohPr1ZxIVeo5EYLUswmx8pSU9Difbqb4Dyv8Moh_NaEzhAKxR1FpxaydOVho6DA3QSmRkN1TOz7TLpRfldzE3EvSvNwXojaRaJIzsDf-XBwUHgDwynymCtArssy0TKvp9-Zdw3iPr5cCis0iIppuncVxI8rsc-MWqMo3CMEcmd6x1N0_cZB-3YbWoO5R1kRELgUBBJmSiNdutzSfIMSc7TA5vk-qW4ZjqaPFmJK016Fg4q6IH7GLhDXRIitCTQEowHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icD5zSPSO1pD3CcIXw42ulv9LRQsY0eL9eBvpHQKy9noiMPmaW_tXAvpq2MVboBFyVHiZkUEJnE1HGVihKYnd0hcVmeosnLFmifDoErxAGZlWgWeYzHGKSf7HniIQ9SEs-w3g0Gduy1rUbVjMuK7eAIGV4arlnizCFbAWdJ28pAxDnTsvTQoDVyaupEsywdD4PGfwAJ_xSSVdI91h-jxCo1tzsD9hdicvHpmGzv_tdK936k1kSeLpzFN1MXVyltVcVnJmXClMNbQzRPxPwNvMDQXaUtcpvTz65eKXerBoff7SCC_4pY7qJ9SqCWe9kTEKz1xCX3zYTtgXrKWtMXgHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F30bISSvKTACBsLXQuope2JOUfWa8TMnVELHwPCpKM73g0TBsC4PHT3XK2t-h0velMf78oeAj7aHHFsF6GGlVFy-YfmlsF-giBh_ItaCLTYqYceTQmEWxQh4iL3r0tHIOVXjMS968i9Npg8ZfFQGSi5ROo1FNgOLC8cQviwDOqyGbfQ7zCHpI-O57VBQ0KAVVGLcPtMu3c5tx4f8GrMSO8ckChRZ6NqQkmkF6gtiY5oGtpFPG5EzuRYLZbVfwcrgYoKRzHaVujrlt7A11f7a2P4Fiw3v9v4aq9qNfC8Cpo5pjN0Lsb93oJv0oSOggaWT4r36WG4hv2BlT2_OWUPhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhDPCyrBMOYqEBPyQhQuvD9lmfoQF-q-Oawc6ea4lHXmTyuFdnOJ2PAArqSDfyk4z4D_7_NRiXoBOCn05lbjMGBNhQxxbH51bLFHOD1lZ1_QVGYswsOV7K7Mf6Ald4tfY9Pkk2dB7XIZVGoHFhYLHpn4d71FmUmcx0_40izekDzaSov8cILzmT31eyS0Vy_D-0uAE6WL3oIOAPCaXQK-Vq0Y6b-FBrfQ50fu40ES8wLSxp2UMlOQGL_QR3lEtvrepqahqTJfParzu939GHq2qjiLVisrAfDmUd-aZRtEvM_WjFfvLF7vwWQITbvuoWJPuGS538EfFXIdkKu4e3X3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byM7HoE7J3lag9q2g15MCWLNsy_cp_rap4kisLVrbaXjDmy0HCx5jxtjJXBIA5KqmtqKRpW9VFzuDHTxFOT9I5JOv236o1BDwyNfUEQETyN1u96N3Oh0lkab8BRcH0DdolYAhY_XhWUoJT4X_6Nlg_iP_WJFO2IPtH4TQ253hQ3l1wLmkYFd07IMiNYFDQvlqXmSqgcpV8ZRJclX24GzC8S6MZOHQOPY1CwdHCr27wyjCUyHRFOJXJnTo40A4m6fWE77y5XNieFQmtUQKuUw4x6LRpXi8uJLKYfrxyQ7B0g6fMIYOuk7f-kYiaEvo3sk1JRaxks9y72GZIi8HhAKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDMTU0eN5X9PGOgT-DNjxOa4_rXIEqchhc2RYSnL7xzdVK5lNlaHfpSIUwF4XutbkKb90vGEi9tEe_CbxAAN7PHT7flrQDW96JlZRU6w6EpfvUsZ22uDEjngFD2EdIaEm_0yzjQKOmDkvyaNtKKBgunQM13-oX9wEwFq_HoU_7--SHQpao8Fo93GTqLxcCHR8zBYI8LW7YgEBiFO5RAdODCg0Lk1fKvQqFBd1bMR_BvWGnggawkrE-Hr77FYU6ygUJFsqHvkchyfxZ4TjmJnk-C8BcJdBItxlEvoVKh4aZqzqirxFvzwq9O4SEnMVaKQJ_KGGTjRM8IhQoIETB7iQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPdzLJfrf9yIJNXbrjHLKsx_cvBNCxNDTDqGG8lz_tIFC5T0O7QfSo2uOOV0kEx1SZUhAfu8Ty0a4jcTpBwCdp1PpWrH7iwf-GKwDxIruuNIhK33a1zrHqF8nacyx6GDqYjSIasaAqAalLe2xtFTsY9jmVDqiUERvSnNkIE9E4_4fsLA3q3ZK4aR-tztnWrb45sv8a_-mEY28b7SN2LhENWozG6WQ79seyctRArr5bknSoZx7Yr8sXwBRVL-zqRLX0Aw5VCjSpJUC_N6mSM8m25b-WJCmKq3Gstdpaoo3Dx2RxIoM5bj3xfXUWG8OaZZl1DAtOZxhFRgygoQQeTxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PG9eq7TM6sc0nP0rKIjVFSwz1sQEC_pQpxRVp-h2Qd9xbOilA4fVRolX0hKxe05QD2eI7z4pTLnwsfd13Mqag8SMRKYAO1fQH8C3-I488rxXgGDg_BTVR2yvhme8yJnCsYP8vOqhA5AnUkbw5Hs_HGOfSyqkBnMSF8yOlzB1XBeyI0LFhZGQ7xoLsYsyuGRcKK10PU2Jyn7QAeclhjXO_JNq4jOezj3IH0HcLzR2I6R6_B3HXDGh4-NcYCdsQ_S55Pmy21CFBe_rE9XjYv1ByzhHcOewDEOAFdfGQKDY6Z4gDZKxdEr4ZvcvhH-iR1ezS6CzlC2AOjvmWp3zsAvrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4LQ_A8motggM-ILkDzW-QXh5wbMPtbrb-NVadyV7kxXtoSDwXQ_ocg8wJzQBE8AmbKTI93IbSoj9uJsX-R1ntx-EAX6vmY_ktz3PALxRB59wnHb5XNSIPlAKmu2c47-acZ4VJUcuM_Ld6Wx4lDERketulNUz5l5uL5ATZrxbjYraW_hi6ZdTl9EsGI19bPgxYOsZR0T68qS6UeHjfF-hR23-uX2aCQwevR1NKGmM5rboOYyEkHBc0_0a9u8NYdxOcPBSiIeRJGIH5eBNZ3_pEn0jNvkYPkdPG5kAMGEzfvtidq3J4Ecz4BUV76q2W6HFuJQu5DQl6wAwhNGoRnSMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1MvtjasllORk9sQGVumArmyFl0lbWwjNDwVjvCXE3hY7dpuw9Ks-JtiKDj3Oz1IuwCbXWJfJird1juSgg5_UEeMs4MgW1UflKbzZgGzCuatgM-K56kjiPlCf1Jf2AvXuh2Em63EygC8xEVGOMKVnQh8LretNuOsNnNLROPE0HsaU5CSceJW-OiS8pn1_b4bpuaz1ZewAxbfqpr2-DXdO-zeNy0SgQMJoUjk1ezzdhsxaaXuy5HUnHWQnJHZz0o09WiCLzcYd15MaZiytBm2PCb7n5M2b-Fy67-378WNWacGDVhjEpeh3xNt6dYwolHxcMs5eCCZrmNliR6ake6uOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4BeCeoIUFZvfPhzYTq8rkzQi7nPEuOvNvfy1-6DZU5I5zGMCWa0QmcE_LZM72PTo75kjypdm0c10FWMmbBlJDzzCDs8i6UPmCa6OkQWbTUHdeqGmDl05aku44W4hur4Pk3Eio4oHf97R8vvg45j34poAj5dTtf9ekHSgxtKZudKMcTa1g2hsa06lgQdjt6HCKritSGD0oR-4m_eCGto2mXJN4CcTvk7CpLxfUEpiOujUOEDiyCkETtGpxxCkBQUSOBuPF98ISrsRw7SbVA3YSL8MKmykuptbRaGamHysSa51jfXylGd7tp9TwAwdwGM5cUoNBkyc4fT88K13xpETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNZFiwZL08lxOrbKuXEUlvoETNnnxxnIgWPE-y6WUzRk_pwIX8GzSmdgTM08CZMwbzd8I782o54bpuulhyp__JOax91YirhmGtBpPdgnxqXov89fEQ282b3YDs6nnzD4yTCTfwO0wYlnaIam_z_fEkPq1K0WqLbxaSwk7OZPFjb__GEGcToew96HBQ0bxehyebEAWTlX63oaaG3vi2ISIV7mmZgy1c1u-Z2m96dFB2mGWOFLkhjH8-5i8e0xTqkTD-JRoIhF4Qc6YbCuFfbab0-z5-7-OJRhMFEEMVdU6HoY0t-a2U1oOusmDZz_2tq2fVVyhH9svSsS__JkveutLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9lYHObe7zg3xomKY_kuIGo0HGNra4ZuANNiqelbkS6yEygDnBtBcj7PGLU61z-SLlcOFBP0q4z2OlgshRWwQ8rVxKgjX5N40MjQIkyuhUrWxFzzRRvXT4FdcHLo14SkrdvyVCif3z8wFDwO6OAjVrBmoy4Zm68LS3k-CEHWOzBxk48xJIpxl_DXq6VH8ABCUuJKapQK-QOys3cUo4B1EWtRWZhPJ2ZSQYeTMDCIyQs-Fg819NRwQBz81elBTentnO6SDkmv-HGmLyR1BLjin-G1jYHSJWdYBHOkVofzOGKwce1wA9qOnyb1qYfsAAna6BKMIFD5Ny8OXbJ3rsLO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blu8uSqwxms7ygDHGR4qYzDELtZHWy3WMQqHZoTNlMEbzl7NSnhxIREeIvyE9sBW90w00bfXNxHV9HFqpv-633TKOFGTa39OfKaWZk0WGUO3hpyq_VQnI-F3aqfA7LWMze9BdJtE1UNMmb8QH_qGyHNbPiYvAfsGPNl5WAIDLostoygqKplrAjzaV-kQhc8tK7pNXUbnh-FwGss_7DbXytz6ayQ8u2z3o1TmuqsJOzRHzdYAzrCzZZW_m_K11x8e0Ty6kE-WlL99REhnQS0FgjvZzSGBloe2Ya_aZxf3gpP--aTiwVC1JJaO7zsYAZn3i2zxGQVnKiSZCfy8VRBAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qL1WZkAtvNHBlI9UA5EdbHrkm8PumpkcfIyVKHhrYO0heMJl9kJjr715Zjr06IUO81JWny21Z9V7xc1tfnYJVwfuiGk-YJWjvpj6g9PNlSaTVNOPn9qbD9lio1MsV6Nmea5NH_0afT0PKi8_CIrillfm7KE0Y8D7Hy5duKFKxrp9rkDjZv_H8lbLfQfJ4ofszJK6-CTPxXGkykK6E-FOXX22I063mU9B45vh-6v9REzsOw0UX1H3CY_m8_UqXWVGgz6jcpPfFp3WU8xEhWcEJ6Yn7oXcVRfQZrb6zS-tuIpKCLqz2KV6wxiz-5Nc_bqQfckzTXq1w9BCLbKdXE71gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QM-cKX5BwG0vYb1FCjmy28vp4PjtKITtreSpQ_DkeN6wXTMbvWlW4dvke3MIUkV0e6DWXrRivybZqp9i_tbWgwPj2jXSVHWEsaisAwvTEXS0Iz_gKM-l7mAfygu7ZOJJm-T7V1kudyMIyBOfR7bPpcSHj-GLFeqK11QGEDWWjnoYPtyXmTt0ve5TRk4SLKrmlX1jZWkMuQPwzrqEwU6aYTnVXHT6E42xvruMTLbSd4JsgrZ6MdDPgkDNfT0vQw7eRgBNmzyxHP-LyeX02JnhGfG15SUzUGq48kjdzyrbKEAvDEzZojSNWJJpxNxcl0_oD2kOLDfzMqrZKKCrAJz-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgWfl8w2jwoiZOeZP-825w4nnwfk4_2g3iQibEJl_am6QgwIwtBEmFWTA6TRVOzTDmQS9uVVRsfillBub8XCubVsZvvBDTDj2Z-blu25qjSwTdUcZHKOiX9dpjBizMuF9VaicNtpFVHQ-x1rRNHNolw_nhw_GKRvO8Gmh5_esuMec0ALBy9Anhs12u2ZLE4Ev-KWQQ2nvWo9QmWCZuGFEIbLfUx_hj-QHna0GxeO6RsjxYPnbyuJVrTDUt_V-MBX0QQ-UbJeqJVHic2TgB4G15WZj_sibJnFLtoZYmS1Vg3L2Q11iUBWo_ZvFF0zCkgRK5EHmMxAr9aLFf1wSRkKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtNj6ptRpKQjlcY8-Q37bEHqAM8RNBJfZZ3yaJhUk_YO4JsD-JJAmuCWZ-hSNycv59xa3KDGS0h0kzbnypmvXL0jo6v04bl5ChSQrgTBqs5bkyVjSB_2XH2zykbrr-z8sD6jpFrO9lc45ly0lTflUziF4ImoTkSuINiy4eZFi_PFq0ZRqmJFoMvBt2bN6a8bj0FodEbqG6VloTpLJQrCl8tY63SHWc0qYF1yijuxUlC452p2rkAabUZRKHdLjc7Dkg1LMGUd97twa4uRhDnujM60PrdH4dQ3Pe4jGniN6WjPh64DtBrlmw2OAgdzk2X_uWH-SNnenenIwxUq1o5bsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uzb7yyHfSG8WsqM3OvW3Fz8CAQDLDCxNGvAIKUO6nGMlvw4U05ALliisqliJ7dzHE6FkL15qpqAYq6XSk7alg2hJ0R__xbY6g-xYWrcMDulZTiFrcEZU1qk7_VJGCSd5Wt-RHartSHLQJzMgybUG34Jy1ESaZillLzCsCPGk7b1pbpgV-LrMeuJrixcj7zo60qwh9iuJgJhb6HSt8o2sOZOJEyaur6m9x5GoGFccTIBmU9gDgXz025Mi04mW8Y1e57uHNgAcBkDVZjBwJHeLgfR1wF6bgk5zn5-NYgeBlVq4-HAKoR7pXYWOvixU1dGI8xYuyvAbhZmHIZ0WR3NWtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wljfb-o14DwnBbrunOp-HaFIxUPOeFxPiQG8pXZJAq1dMmC704Zr4os06vHHJn4CKZlxFbNtOb_uCB8N-NTi2PsvOkaZfyaKvkmKxyJPwuHW0tC1M4Z5h94o_y2lxsi9l2PPfbP-xxEWv5R8Ag6fb9PFPBoO9KRakrWMsPphtmN2Pb_rRtWL04tqcEiGQMXzsxdE960ooC_uc49kjxb8SIRIjxtLTMo2CHaH2GO5wm0qO3tW2VU2kYPWr0zKegTFYIyikHEruwi98rM5nrn93rF18R0bfVBqHQQQyadJ4rmqQzd6YyAMNzHp2Uqshk8-d9YVgTkddoeEScGKVYlI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELpqt5jgYM0aH5FHR4Vp267fH16YbDg2AzbA_B4A2r-nXap00YX7w7v5Oge-6KRWBSTu9T3I9PtIypQg70nGz81oaxuZkYWK8SoA_tRFC-RQDmokW1dkFY6Rvok3f1gX8ERk5PehmFvF0kupJV4nr8giJahCNmlSSLKcUTv67QvSu7suD4DH2OfFGhxmPpSIIg4iJgWX4kYybn3y7dhAtWVefZugyR0BFI0oZcdfKeZ77-qFuy76ZmSRAj-o51ciKgYONg80xDr6M0KT_J6JjMZ4LNag5trbVGzYomCpgtaAhpd-KG4gx0F5sK9fWEqJlU2zt3_enpfnsVxyicJEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbzn-3ZCItfZIWkI-95EhhMxUMPYaxccBaNl9w50SyMELc3bcq_33Bszdy6yUEtrhc9xhZ5TueijGNc1NoPGAaCiw72xuwmkXOFTAGsVJ8qTD-meir5gGxTdJDmc_wKm9NHnJdoKaW1mXuAb2BSFhaQ7Pdk0IbUdBwJlR0yij_cAirmXloJ5xt2FXk49FBvJlr98MDLUiycyOS2oCDKBqikiMO8gXOIC2sGWN8M113T5QmxJ95LiGUfh8cmeDuRAlrc3P0ab3riVqbg1IllZA5qxCT_fGAtRJEQJrf52JCBsAMRIjIGxtGt2ACh7ALAy8Huazzh_mCHp5n7ZDdFrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaqzOU9vOnWIBfTAwcFjQI-kDZIGPhA_v0R7_WHwhazPWTbeb3WWrAh8za_w7hfzvntPrUGEXStsENXrnMUUVfkxtJ8JDMwV4qbF1qU5wVA69bJ1K-tnAwuplDJfy73OtCtV8UVI-VtxB3OW7N6tGBr2_xA1qvppVsxSWLecl8nKOcqsPAdEDw4Hmax5zqE2LLj6Z2RnOagxOUwD9AG5j7iAABMKtqurfR06Tskimh770WJQits_hFXi3u4VVHxpi9rhcNP480xdXoFLWH_Y4v9jmYC9UIaudNsmoukXmk5vsl8HmimXwnKlp9th9Q9d71rBgg93gkoorgrQ-4Vs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdOUoBDT4rGP9NXKjw0Vk3CHOx8jnbqVvASDIZx_ZtqaiD_4zQx_S5gg8tfw4_LZySMtmE3Nx53OLnRE8OxKAAK59rroe5xWYk6vDXBh5ownDN5pvswUuKOQ1l1XUNP69MIq2iRghQlAlbKuPBZBSnB8QCQ-pK4QN4gjQii9fIDWr8_7OH-dPOkGjdDkzt4tF5tibWUyGUCWIIF3HmpaUlKcvUzpzjcnNXAbkyFIzVSGBeUmM4PXtk5bwpom4P1Tc3wk-P36NH0yCp_3ZqRI1SpyZMwaG6wHuTdVYA0FZlGkvKrN0iMVC5uZwjVC8gMZHjwhhXcEYwUIKyR8Z6H-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CN-Vy_ppH2nqJbR6RnKieDtSzvFG-NBmc57t0GO_X9i94uNtI9Hbve5yH9AIxXUg1FLdhyR37vCZyu6OSG9lHVCH0-nwHvaXJ3VksgoTn2smStZVdQPGGes7EyhhYEzuHRsK-1LP8ib22treb2tFolSl88_uV7O4JpinTmMPWyOv8cYnwYHtW447BlUcWyEeUByVEK69QHAHX-8KZyDBiYOOCxvLi_aoUNgey-eNUmhK06OfWnj1aVNzKBMsdX0NR6cT-ICactYPn6H2y1b4HCNBitkNXfBuZL1DYw4oE6jRXvGFYcQQL9SQgYqPlMSUrjaHKiuL9dsCDCpeE7BPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDOWvgc1Vmxb27qRuDpaTRprdbNZkWW8LzAiTFSIwRX8x6ODjdQwG4y_KvQOHl2LBOIgKusm_0q5tDIPTXxlSl4Xetp1y0YJ9robJRoOLIYdDRfA14DLnZLOe2fCRO3BA4nvxmsWpE4chVAzg89_l61q_xGPNfV6i9Hx7t4KL74MjenHDkMYgm4qQ_5VawOEKIv-SCmsEn6EzeLw6xYDDl97dfNPdcU2wPyvnhmbyBV0S-UjHcp-x88Nrh5SQQsnfuzCYk-kREZ7gNxoCJtOg5qS_iMSjQbaaBRym0fBZErW_Olj-nyb-5kEhVFxJ3Ag6MZYNJkCTT45r2sceb_j2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ms4Nz658sb2v6lbLww9kfFe4jxnnzqIzO4r7xfJhdr3Tz3J1xm7OVW_F3JNu8R3wD9nxBI1FIIt9K5QUxeZWwdw8BlolhU9nslwZTwj58xO2_2WjR3RIi6dWKdvZebSjqRyro7p8Z0WrQRuiY9O-nt3wUloYRkoXA0k_pgdLb_E5zDTbuT6GyX6bzuhFT4QKG-sHGCFDywanzLnjRSc_SvYbO2Uxwlm9Oe7dIFArMhhDSYdujYz8WJ5Ip7ebkb0pIzbfLyzdsf4ttc7NADulKOj4D97bYWH0VkK_fus--fcNl9P5f0bCqGAigFaCTeciaSBO4OEnmKxMLQPbWXtZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gddAfnjjaSO-XOl0VwZeaVM1u3_bzYekH4aDnPnl8YINvly4HED3v-vD_bw5GgdmHduhn6mFkKO9VTTTntrPqqJdOBNF_RANLvsbIIV-UEUo7JwRI2pl1PGUpqUXd1Y9rRLaRKnvZI-VVm79xzhuN2MeA8aUwNaYXoLQ_2YoregcmjN2ZxcpihLoJNf4seGVLLaL9zPDioYG1hx5eInHjLK0gLoOPpPndzFPkW9qELpRBDaeftE6kK8tcdX8Q_-kRREA3DAv7HTvoKhTDzRtsAwjbDf1AQtNbs-ohRynOifjtZqL9ewWAZazVKqP0ZcC9MrOMsprNJdTzE4MUmuZtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXHOmoiX64iAViRQ6z7MfdtcUuJowihK7dsmoD77w5cLaOCSV140_Gk7Ta49tJoCJplwYfiYz4IVkU_XMzyDf7I6BQ1hU62OW4oJQ4Xkoeu2ATf5Vajv-9Mn3UPpdNsMOCx5p3wOi51LqXKVpwqFGIG3wLzWiIqPVLVIwwR3TkQ3-7J4naBsJI154uQMFo_KClMs1L6TeRe3KIu3owAV_ZDL9u2i-l1BnrVoQNJVVUAfNjFwHXXveZc7d1dluBGKQ0LDckI2lt2p-0W5nYQWm8l2WJVGO_h3A1IyM6iK3ba180umcWz5wus0u5LinJgVcCeKUdjBBBtJFkbkYhPIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmxotO3MBvH_rImTcmtQUgdWHgGwIWlxvxUyb2KZ-fy7fRojaabPIPtcbTSWrLp5wray5NeYopZ-UTCJZyNtEdgZ-2lE3DzCkZgcshl1W5-uK2xbfxbBYKwpikiIowBrU5dRzbImkj8WROE9Km3lwn2P-MosrmuwI5HEarVPIrJlklh_DZEmtMj6dvnbot23Ukio3AvXkJbsiyNIEWl-P3lJaj7tFD3o5Dxs1J-oBfy5BTa9gXFlQMVRo3EZr3HuN23Op9_HWeGIMatuk4w2LFfQxrdHh_zGLz2qNWZeVDbQbGiJhrPGvgNRod4QBp94B5Zsk-JMxTw3ExIT6KCL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl0qimktoOVwd0xNa1pAjwMQK1lPq0AdHLHbAsgU0Nclzmxn-HNWWGjEqIRYBWLBaLl_OzRYn73iqL3KHax7ONrbSah2WIPoMxJOYWlC77b3Ps0ChKQYKSUkj9z7RE2cJ7mV3Cv-_clXMWvnfEev5XiyrK1be9hPYq2Ka12DS6pADHwAvgCvacsVH08QJ-vr6RLaFmp8Wc2B3-wRqiLPrSZrPceoGnYcTHG9Yjg4zrLZo3XtPMSJY1PkG-rDw7QxEyhQjkq6qYqRj38OE3vXNAkWUM55Khygejwheuft_ebRDzTYYxJVZvkpuCfLOL07FSkSqDcB1DYXSLWU__aCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jndm9Vz5hLsnuA8NKJbCz8ZQ-7avYxTobntc-PZbSPmD-eLWjAef-mXAHg5LAZA7ymVRG32Z6Zd9-xV3odqAVfOJG6bjtPjmoWuvxylvooVV52imwLL1vMzcdWejwi9sdf6_1AOujTZ0vkyuGIr3oaWN5eI5AoSNnNQ4_gryGcRvgH-JYG1Zhn9HI0-bP7-XUA6ihniHRrkY-Mr37SAgabwlmTMrT7NINtGy92Qe_wH0pQYAdiQrMDoxi781GcJ8R_51XnzkE1TLlj6nm32G0aSio18F5F3QzTvFlg5fW5nR1rGnyNP_JS5_vuXiSZpsbSeot5cpRlxb-E3bVpRsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4OD4SkQj2uFM7qjY7uY8-GPdNmPYlSyONA1TftwdSaq9dAFYnFbfFXJgqx0wAiasqi6jjgKSi2eXDnrnjpTvfUIJX9_89w6NZv2RetGDshnwMKhL9g6HtqvYJYQMYhK3JMBg4aIlK1j_XIB6rdVo3ArUx1Nd91nUOi69fls-00Yh9sP_RQCH1CQiDaBKyfIMjeedNdqYd26GWyRAr30IfX5v5R53LEM0Hs8frT5G4VjduSQPPhs4U2Dvz033pekdpUh1FYZr28PAfs9GBW4IfSJKcnhOnjRJrnV7mWWh5djFL6VRMj26fOv5AdBNDwczxqKHCXed4HbUhuo1Y89kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd5PXAICaj1Ty75RI60TpNWyTvCt1xXsIIFHlmQOEJ2XGm42EX8S0PYn773wdfUWRLeTpIaDOBkhgk71J41HWuqOrJd4VG58-B6MYx9dF-rBUDww5-SBcMXO0kvEZ2ZuSQpPIvsf06nXdSmRqnw621uZHS-AuTndRUZHAhwwLbJKKC3hxRpMCL_x0No5MCjxxmOW7wv_uN0fEHzeIoU8DSaWkzNMHImhRRC6psv7J4ho4mWaXoGYfaPsfb9Cl3IE1m51aa5nA2rIDja99Lzm_Gtgry2-gocSceKhDfxFv_FtvfVRQ7fpdBS2t3TEwUx_ePRjvHB6hZa-0JPyeh5ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=YLvhgxETa0jAjcqJOrmkB7KH7nLC0hpcl7iqST_m8ZYldii5Xm4m_Bvy1PAyTUEA3dCZm8Zc1Vi5ao9vbd6ZkyjmJwGgn7O1Swg2hDy-7abRAfn613foJT8pU2RBEOqkqRyv_mQiYvUBJYEx_O81PhEYy_j2qmZM0MtX_EErM9Bvnwbn-541wkNmqX9uyzssUaszT-TPNykTtcGtgfTtp4MX-CzZzd_B77JxzykdBQl_Gc9KOL4KuBouHp3blTx4TuHpGqtevi3Ud6QzcM-LGmkpKIguGEteIbkV2i89i8v_wAoinqiFDKPULLHGwBF-rqlP6k3Ujaj55_W6vj9CRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=YLvhgxETa0jAjcqJOrmkB7KH7nLC0hpcl7iqST_m8ZYldii5Xm4m_Bvy1PAyTUEA3dCZm8Zc1Vi5ao9vbd6ZkyjmJwGgn7O1Swg2hDy-7abRAfn613foJT8pU2RBEOqkqRyv_mQiYvUBJYEx_O81PhEYy_j2qmZM0MtX_EErM9Bvnwbn-541wkNmqX9uyzssUaszT-TPNykTtcGtgfTtp4MX-CzZzd_B77JxzykdBQl_Gc9KOL4KuBouHp3blTx4TuHpGqtevi3Ud6QzcM-LGmkpKIguGEteIbkV2i89i8v_wAoinqiFDKPULLHGwBF-rqlP6k3Ujaj55_W6vj9CRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxkyPeN-RLvCb3kq__wwn4OH7J8a5DYoNM5AHj40TrpsgEM7cxjctXYIXE02ns1PdTylQu8kv_Dqup7-W1rC_HTjSpDuBBH_uese9XmpxPdFyR2lYK-kd3QuVt6zsDb_PGKEQIm_Ucdk3kXb5U8CG8a70vEg5jOBQ_345KbEP02U6e-S-6IHvqBx7sqYBlMO_g3H3N21K2KOIVpiuFpaY_VeR9Lo13eMafGbkly9QY6RdVbBF8ztE6jl_JbFhpgH7fngl0eNYFeyr3o6fUJZWgOAvTUYo5UGdf6K_jHxT68bcVddffvh8aqspWZUx19I8lQxVPrefsCrrRAelSPu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAWgfdM4GQcwkO1fmrKVCppCXgX0WSkyTBdf2APLZ8JFVdkagYgsmapTvVB1w5GQGiz3RmiYCjC0s6CM31BmAdXAtszZDk78MIg0Zk8fBQnHuuRZYdjBp_9o2DG8HrIDnlJYlEPgHjXFEkNE5PAwsJOtxoH_IAj2C5OaKzVOoJZysH36YohMUH9CTf8XZLA7NFYyqcQ3JUI3Gc4denqMVzXmCbKXKPc4oL2EfX4VsVQemanA8eXxN7oWNhKwHnEaYeC6Z0wdecRt8moNUyvRHBgBbGVAsBG6q-oYtUsahNEKGt0tcW8tygd5SCGYZhofid8vkr8BfAiXRczJXDlZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmLfH0A8z0cnZvCA7572Xxl8yRqtja7B31z8_C08G0aOasyTvXQ5d2HPZ2ujIUBQ3GzXRBt9s_iy_XktDPVAldD46wOHTtWfifPCtfx9rKU2EGSS5KSnO2db5Voxoj9w972qyUaah3I2KMFJ5hIpt3fBFKSGNrMO-6TO09x_FZbLewNarMvuOOpIZ55r1r6dRs0hYgkTfMgcExSFJePOonLSAOby_dy5M6-wCAZozbe1pvRi1yGLTtnGZIMqprqbaq_H50FqPk94kiBP8qUDKPBIkon7CRxyyNQlT6i7m7fYrwL2aXF3_YwUQPTCA8Ibb52y2Os-nlMpL-_OE0Beaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVyVXL5a7l9ZDwfBZd3kFG8xwHwmH_JhDFkDXayGmXA1GLw7kWAjEh40N10LeV4qQDUYVhTC27W_SS7eMu-cfxgb7d3Fwc7TSqs7jmjDGBegm3hh8YfOjjDQ44XyuZPRH9yk0V7r3M0TQLJuSTw34hpD7-RNV1EnM4ReB27SpPHkH1bxTZZgErrogAU2X2q0_6ULs5mnuxaV8JPJxiQ6C34rV1OC3Mp4QJ2-ecXLOVTymKvNb_eBQWrkmHVlGPv783VUqnnmGaEBG88GhsCjoY3y0aPI0MaCNzGqmqH4aCU1zAhLeB4OY4gH9vB3XDnLDzwPV6WQqA4za0cJ3Ngniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9cYqDK4YZj_hfU4XReUMJzvZKFH1c89ZcnFBO46uMAlxfeRMtUxH4vKclz5d8R0mp_w4Dn_8qIh7OOJu2HQRnufFQBK-ARSYZhzZfAqAKO4DyEtlAH9LIy2lfDQ52LgUpuLxNXkzcr2ayBRxqkG7p9O4Xqa3z_dMOBNuNqa-tgW-LdAgLn7Uc3Ah4yyKYkrr9LoYrvTNx6QE-9_YFwQCJF9PySMObV7gmuBglDRD1H6x6mx9a8e15JCx9N2z9dNb-JeOUraRjWsK2E4tAYvNAVcdYDFvvHXVrm6lRbQCAVB1xzvIXetFa-MX5AgACXdncfyxyQvlEttGj2snbQsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKQ7uXJnh3uh7nltTsManXNy8fwxUpiSCwJlDI-12AMo2plhzsxniLfPnwzmQMg_Usr_pIQ1e3Ji2OFGQRblbvunBECRPUdBZM4WBkKS53x8Jg8qfecNNUsN6SbBQPTZUm18PkOlb-NPBnAl6OvIt1QTDhaoYchWA58Ab8XnGZtghyKFpSfv1Q8nHYmjoZDUpNGxP2vb2xRFoRN5wTgtozmk-flK0nWxgGcRH9HXdEi42pUahiLPaHfEc5eVAMBa6K1yFc5kj2IClV3HbG4tPdgPW17RSKIZlJ5Y3gh8RSLUcJGEeAmg0RdIag9aczElwK_ciDKQ-24HeZ0KUgqItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlbKRrB8BzkfkSWFpFVInkqrkTPsIiGh9_sWsxvjo2xbJI0tIx_e-plp7NkO9gqpfD-AixpIaTglHFmPGev7yQb-tPoh67wGO_SgZ1XiwMPYLGTYm89s-vDcnMqWKkAov-5SF08RMbqAsf5-sgJOFgm1QjR7ENsqDG96O1HNxfIDAiz8obiwbRwLgOQKjBKWG2MSRD2twjgW9IJo-t_cBsJCmoXmtdVEcQyOf6tiU03VTw3N20p1KSdB3pFe6eoimqWNmPtTOD7I63N2IuSiXB3N5LZA8COhqOmuaH7N_9_OaV384B8D5EM1LZ90J5JvRcXlyXUKsvFSJR_8dFquLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJO6ESwgpYzmcLzsiwORvDAtIcAJgt-MhPnO4Bxwiel5YSpvX4MaR1bkehxtjfjLq2nqLvl6L9cdEJU9QZLp3x1kjWZ1Y39f1lMk4ccYpQ368xp7sBi6En7vAtpdPyYLklOIWSq_0Av37YKAMwD94SPRR7_GWj2QYUcit2KZq0r73XOZ8mJDitscd7GiaExNZhGFxPJFXkQqF1Jsf0WIcttw77heR4QdHZoPZugguzDlT7uADWsZyPsjwYXPQ6Ku27GAAMPiGOkLB-NViVhRteIfOGDMefnuOIaH0J5BiCu-wysv-bVZIpf6DTpSAgs9WTmlDSTKEJAYvc5CZjddhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ94dsJGPb92Sz-b06NiQArVc_nYAG9aSlvC9ttTkj6_sdh__2thFGdy9Tn8eQKnzmBkbzmwhuoj8lWw6LRlUfffQRw082QHt1xqeiK3QNMKH2MQaz2kdvZKK9SRrEL5RBDTnW0a9Aus4kBYnqKcaENgpIgYaUxJQzXt_735OBdgxbJbQwXvIgZCSTSZsqqq2PQ9pPCrsporhaluVDM9MgXxZS7kx_JrLHkmy_5OTJqNnD9d8lCU2hyOZdm9Qqe-03U8flRQ4VpGlQR3pZhsOMKhxAWLWwDy2Atop0_7TVkITqwYLOZoRox8RB0gVMtxW7XdBp3omsMK5JcObQ2n9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ5AYuiQlhVADoCbwzZH2uW_3PCLACJSacQVSiqvsRPvGOjKkvNkdSDG1NLQxZLOgn5VZ3M6USI-tYmfaaLYH9a2a5ojv--QmpKZ_pNdmCQUqPMyNf2h18H3y9TIvBnm_nhAfBB6849j_8Wl2kbsawpTnN3tUyXnky-a51bmoEghxvZnHMMLu72AKb1t_BJWIgWHnRWbQ6GOAy2BtbGGC9ITu7HBx4EsYwSJAENjERVnX9S5W9SKVjzfiQyNMr0FdO4ucRtvZUqLBIl_SIYPy728CO3BzVEKeH_MjgeYR4kyeOIKK3KAh-JHeCtD2r85KsBqYjlhu0-CXRpA89JJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUTQnUJ2oKwpxIe0WaGWDhvODIXcVcRg1aI4c1HG1qASoLGphzMgTBGEd10M5sbIEbx27B_lEhXrIAD9b1b6P_3rgbekKcd4aPDxWORqkKr0CQofA0avn9L-_yGcFhTWb5eHzIa1xZsXvy-cfBGxGJNqNHYH03-LCXkwM63LufcANwhPUWhc2Y-1PSt6-pPwWnFRsviHZZAyqFcPHWYwAHjAxo39kBtN_wozy9fswveN46Zu73QWBW65oAYTmXjoLGtgzmfEZHRHkpunA7udwmawh4uRvALmB4yeOoj25iMRDQMc7NaRe4weNUEKxxcUE4M84klkHU-W_Sjnayt-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-dSeWQBgEwFVGXFMjTv0kHw-o3St4is_ca-M4GzNsBXseecru7meF6zUATh3AgZHLu-zfASDkqp0hlDP_uZEvOZwZ8LJSqF6htPAO4nam0nsKre6AET9PhOTH0AIFFj0XKYGl5GeYHcyj_kwkEv2kXRg2XvI2WFZny3q2l9lPuVw-SPFyRu5KMFPkmfIRYJGiwipwiqLqaN0mwnGAom1jc15LCrngYidUVz_UXhsbPkGByRNE9GpTrSFuRasZNm1cjQrZJx4KxFAMkRb-OUc2de3diVFvx_w6oeHzLSI57wnVvo8aowds1pUSkqYfMYItWsvf6UUHuAP57-RR9sKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icJUkDJwyEbv8zNHk8aAoX2gUBoDL8bcxX1HElSIWKtY03FZ_SEQJZdaTDqPrrzn3hkOIFBfoE6TIibtaYBnp-EwKpvMLP6rUzKvP4n-TMhXlp6Di-bN0nc41Unvsd0JHlKWqHP3y5PQMlUZ1cEV2vZSUmF7wxsJM93bWSzarLQffITXjZ15vNzClRdF70j7MJbOsBnjheCqDQZ-JyjTxpp76KfLKBhErVMjRCmIh4KfDSwxFljmQ8gFW0WNHH-JRPSxw5HwyD3Yw5MoCG1YuQNT5fdZf04Isrs0eD0fp_jem6SLIAF2iTgxiPNdC4qtJineflrlRJ8ZKoRT3YepIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjLhuIU2GOrx87avOtGr4n9vLeUbfDa2IxBV-S-LR56arrgxhejQYuwcej4E3S8b85nIaCwzwxh1OvbFVwTBnSk1cz8mrMjqQ5p2o-ckBLsxbH8--Gu9gF1A5OBrd-g8cB_8khFKfE7SlEEjLuMOATrGIh54N6FPrnWPjKARUWxVIDbwqPDtB8zdpDDHK3vFNgt5W_K4u7_emYBWkr1m7GfkyUMupGddGoldcsgAzdnFThl4m0FMG2uXL7pLr3Gj1KAT-I1H3D9e-q8mTQhLQ97DvjbvgCj4IZh531W_jAiPHfw61EWPGNwQpwM2vOPw4msseEp0ZbSDs0dmbDui6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfNYVTrgDaOFZAVhFQdrH4urm5_kx7AcqCsZrOPzZ1a0v4UVmfEf2ksHuxehVpVzvDrpJA9w3piKvat1NkcB126BgpWap3VSyxK3z48YCUA3fMJErvfL5sStx7jIQrhRCO0bvB5X3oZveLdZCmccG-U8qva4-wYlIkohJTs0FJknZFkvbSkCt4BMSAXBbzsMI09NNEOu5BPfq44_51gMHfgQsdVQAHksUfroaRNZV2dpbfQBcxVZr0mxJK_29IljKc4DMDUoNH2oWePFYMjPESFDYmt-gEhmGI9N74rwHTVkNqs5VJRymgA89Z9btszlJ5CCRsxDvEqJqKLTpRtXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGqpmLBJtKYIyBqtSV0mnYhSWKQzUS35ec4p965sE2SUBt8N69MviLAcfcYR05JyFYAgZEeBtHIaduo8EB1ZfgP1rwBCr9LvAxqnUuvX559aJj5-SfjaXqFF6qrPjATVKf7Hu3k3ozvs5SgdrEoP3rgCgc6xktUxPjefAel91a6xuyz3rhSRgcAzkSqzPVvMolPA4g_aez6WkWuO1x8OyB4-2hE7P1AElGzcJ37ayqPGDCPj7G7fvls809pAtsLQElhStvvUvCvb2jN3Pt7qe2fBOVYCf9WsV2oBA9ohdbMA3YddneR1hoRdZiH0uInNpyvB3p3LuLECBA8bO9P4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIh1K99uk971_J-qrN8tkpwxpnmv7idx85V_dhOR8gR0VfaSuDogYDbSG79tlUGUmDChJyo-rSpZ_QvMobh2fE7sjeEYMgNOkCNyXq41B3dCBgqVB0U8Jv2NReF2w-WkMKiBkArIjym0gucWqTmsu70DGiPJ-w_blCFPNMqRRob1Lm138osRGyZHa2cfcvt9g34bahJz2D7Ud2M3dQz5_A-W03rVLM6FbAEwVnUyEEmaqQhN2tKtM1V-6y4wYVN3a4Xka4HTjKLizSUN5VJp68VucQkwXTgxDHAEbQjo55Q7UOTPyi2JbXSWqjDwhzpHlacKrqM9zuLB7mJ9LPUTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK4OZBDP-LlqFT8-ydkLYv6Imr83PRwSXNwcBm5y26dqhDEMW6pR4V_IUfhyP9am0XscyU-JRg71ukL_zOS139QnueUD0KO0cnVGoL7fr_1cHns_aiT661aPS9vi4jgEIY9Z-kTgUEZ75EXdd6wgwRo2O2ZNQ6Vj0eitU4PpyM6ALSHo6r-0Ysfx4nPS3Z2AbeT2g53oR77wqG3gtj2j5XwiipialhY9JKTiVfYkj2fLb_3Y3jZHzCbMKeaqZ-dKr3AilqIm0RTgOxByI_OcajZsVLsPxHgkZLC8bBYCOIw2BoVbg1TPHo_CXk4y0Na5kFDsgtnDaYotj2N1eZKRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHd8fN8KrctOcRxru-6BgiFbYcMeasdZh8VcrRjHEQR0Y8iXgn6fWA11tDSjmidE38sRgqsZ-e6VXCK3RYwXET01CTFdMqe5P7kdHqFRvrHS9oUsBQDpcfE_RrFmUz_48EKGGKy8IFWO_QrfFhzrL1KUg8vsBPYCrlKqjDCYLDHVk7gRs57isTUVA4O3DQ9D_CLbgOzvek4C7tYELaEegYVaO6jaUxxxMP2MXWhsm7-XbwZ8C430hVAcaH7guHB48kqkKzdK8A5uO78se6tmcac-27OS0x1NN86-9a2idN5u-AlffJdntn5bXFh-sgNYIsICcx7itXSYJqsccMRn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7RqeJvL6HqHdg6ciNzBlyBDSiPeYtoiGBR8ZqknjAEHBoA6M-PkbJ77ltQvlQzw0edWjEMw0hNQNClnVktuy-_szh1x7wMXAOV0AY8624spIpQfhcBLfbQ7AuJ5EuS4FzWzENlzpVddQaOwqy9KKMy8L1VUUAwqLZjZIBJn75yeou_crNeyH4Np8Iwgfi7g5I8l5ExezVj4223CV_wq36TIIllNa6KeqDXvQEIJRHhWqMKddEbKSU6Qa79WnQ83_AMhqGLoWzLj0-QrlT_20GHf3ocdyfAJvSmMvUN6tNT73gpurSTddgl0tOSa4CeArVBWfUbYoU3a0X06pwYY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNNwJvCSyHPrHdadQ-0DPazvr4a49uiWiw3aWPMPq5eazbO7YtRLJB5FzBM5btIJdqedJDeA6FSFvOPb2KW9WM2MuYhfxPr88Wb2qR9G5scSlNOP4NmE_xv0HBgwEWSjmaAmhdC--vVfDkie1L-2OP6bPeqIZgrQdcJK9RYfFcDblFpB4aj_MjhPWB3wUwJ9Fke-utGxOefv1l8ZATEW3K2C23cmtgsdv5zpaOvkDIVZVvmhBtGD04dr61vWKa87MMR0Cwh21OjfuJjicon11BZplPz5ewuB9GpBCChPuQc9uxnGmIO0JSsU9PbV8U0v2gqELuMYmO6u6EudSWNerg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=TqmwYrQtXd6RBUElkT-K4LwALT4lEmMAHh28gjA6TfJV4OV4MXZdiHRdIYtt2VN2zQywHkh0N0gznHC3nk0Jf36FzI2_2TXEa428eotDMqrbmyDl2jOiPeEgLEt4hFrJpvHNCTIOQbUn9ZTgTfEga6qFBOzwGmIG-o-PzO_v8u3-CMTWbjerFXVG6_2Ptypv-NrdZPpjDW99w3B4VHvyeMJpvT7cvu0E14e-yRuGQnKKMIs-W-vkRxjqkVz3-wvJrReRe_Zspoptx9LJs4E_bixyrxl9hyJp2JulUVbWA1l1w2VteZyYqRiNbiw5FIU4oq94357QXWUTvGdCypS-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=TqmwYrQtXd6RBUElkT-K4LwALT4lEmMAHh28gjA6TfJV4OV4MXZdiHRdIYtt2VN2zQywHkh0N0gznHC3nk0Jf36FzI2_2TXEa428eotDMqrbmyDl2jOiPeEgLEt4hFrJpvHNCTIOQbUn9ZTgTfEga6qFBOzwGmIG-o-PzO_v8u3-CMTWbjerFXVG6_2Ptypv-NrdZPpjDW99w3B4VHvyeMJpvT7cvu0E14e-yRuGQnKKMIs-W-vkRxjqkVz3-wvJrReRe_Zspoptx9LJs4E_bixyrxl9hyJp2JulUVbWA1l1w2VteZyYqRiNbiw5FIU4oq94357QXWUTvGdCypS-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhmzzpPicytnfwpcZpWkkkpdKdyj2PC0c8ma82GrXhZzSgRbVLWFVH6AJchNnFm-JU-OrUQB_4gsvImmvKH3KUYGlSIfQSqYpDMHakrWYbs-0d160s5rNW0uh0zqFX3WhdAypC_x1qWffVHvEWNAdKDtrpxyCZGEz_-VQsD-0ap9DB9ZdxM9PF6_ITwvaOayu4UvPUJh2M8IeGR6Lht29ltXtMHO1Btj8wm7g1rIYlC9FSHq5cnHqbInNAhkWtsRtXV-fX0BIdBlQzwwhHYojzf2MUW4mRbxdtRkUtIIsIQtJ4eLIiOM0f32KlHa-SRn-09fJXZrKzZi7ZhP824_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7zCFwOwFS2WwBIQKyvEsr0PUvLp-48k5MYgmH99yhIG6oKb84laHb0Cbt5NrZSnhLscj9MMf1MqaIgzN2eS4GrCxf_SI2Wyle0BVycjTcoTupZhXPqGVHA5nhzNlraFSWZvRBm20NFXIR9Y0I4As_b8L28cBf9v8kJjYs3yU-z3Xx_lI8jPvrCBarF8ROtzpVFHcEqGUEfUWHHrwL11c_z9-ETjwYpor6CnwkRYncmpTrzS0DR7Uae3nBwlPtTR6ghYyOSk-itG_MCHc7D4R19IbmOMhYAlZJxgXLSF8jDNVRMlf-1R35drQPtuiIeXlxwp_sbBkbNIkH3OtoLmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoIWiBkHp2E7JhxNvp0uZjaFjYaH7EunBLJ7F6AojoBBK3CSN0uDc68_w7RoxCChfvfdxDVum1E98N-05EWkmRS9himHCwzPkPqKoJk3vW9kuKJe7BWK1Pdo07GtGfpY3NA8KuF6TU34Q58aue1Ev3FnG95U6Z_Mmt4N4zyt_LjrHM4UUmZ21Uv5cYIwxUy2g6ZJie9Y024WR9uN8Rkye7IopOjibo7CVGmpOntlx8jjqf2z1tLzGo_FPCbW6N2bA_6svAtQV-jTe-_l4SQJDN7HIfaQ8eDs3At-Mz63AvF0J5AWORPimbnkT5_mBAFB372lKPJrRUd6Sfz7OGyRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=MrScdvgOYnCqgu37YtGmu3qsHIwC4U-vSvixH3HkOQdM2sJOi_slggOHcsT5yrmwEMKodaG8mBwjBB1nLQoIsfhfulkCmmBAN3vcukLvwq_G7TmrkDrc5pLwlJe3r3r3k-ZL7rgQbuHLMTXy9b69TXBDQC84UH0Z18fix7-k3XrmWjo6MpgoEO-Y8rtBxTslqzozQQg-AwbTNc3sbxrho7NxhPHAowJlZ9TQMKqJ3AnhEVvbQBn3dZa_dYssMokshiFSDz2r4SgmHEDFhhI0fOdjza7pxeqbT7UvRWY7qaKXpnc9odNeJ41HNXdwEOPcrgSWsSEi18LG7GQQH6kwcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=MrScdvgOYnCqgu37YtGmu3qsHIwC4U-vSvixH3HkOQdM2sJOi_slggOHcsT5yrmwEMKodaG8mBwjBB1nLQoIsfhfulkCmmBAN3vcukLvwq_G7TmrkDrc5pLwlJe3r3r3k-ZL7rgQbuHLMTXy9b69TXBDQC84UH0Z18fix7-k3XrmWjo6MpgoEO-Y8rtBxTslqzozQQg-AwbTNc3sbxrho7NxhPHAowJlZ9TQMKqJ3AnhEVvbQBn3dZa_dYssMokshiFSDz2r4SgmHEDFhhI0fOdjza7pxeqbT7UvRWY7qaKXpnc9odNeJ41HNXdwEOPcrgSWsSEi18LG7GQQH6kwcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqAlItabmgN8PYMgokxWOHivs3_UA4EvtUbCfJOqSkKS8UIK0mFsQZeIHWHf7s2qVIWwyOwWAvjROvOEuZjrQJDzWVRiuLcycUZteY_kJ3K91e7mmzQuIhJj7L2HmmcvR9fWth4Zidmyc1vlmEqF0tUgTOS5hDX_6h99WsMTE5mOYLTAVLW_0BFgxpgiEHCvmYOsP0lCAnZHLIH_bEnbHeveHBIHneh1qMNZlk-eGzgwdfZEMfzoa3-aPgSfmZ8fD8lD9-kZW8SEC8YUnqLg5fUSMHz1wEUHYaj7tJRSjDN8HYrZllRRoIdjrGRpM8acO2eAaBIqJpL2vswN1oRBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxLQ9HU1r5zKO8FhzZg9pBcNvjKZloZTvHj_uDAi9U3UyVoriUv9tACPozmpyk7jFZxgOiVCZWK4Y2xIbbPdsxFI2CBwJEYSKjNdu4M7Fge-xQlZGZhQaPg4NXHOBzwbDonr4OQNILwj-uj0ZSXiyaqRGqJTOmkth47z1yWn7tE5fv8JmmzbURjyT2iwIlORKB05jFO8-TiJXK7oaif9oa7PrxW2PjOZwJNU6JrzzJLFahSCvjprXYrD1xwoNchAzIvxbmjnKZlF1hBsN5prZzl5xC29SPTuXFtgi6eBs6UNHeg7iY4jXWlNBp0TsBTQD9Sp9OlJog25oWDinST5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FX6B6aebqXKsI-XrM8jJtcH9WD1xJcvxn37Q5wUcZiEQpX7BV3KR_oeS26vUEBPrBmuRBjiq97OYlTtQbwmm-7bNpRPFFfQguRZjufyCZ16c8PdO07d5jVvLxUrmWP8Vm56HwRyn2JwAHY6LUeYKq4EFpJ_Fe0TTTM8rPhgxnBh-DPJHwd8z2QH2DLJ31KsyBAIYlFTnnQJBxXK2TTB_QSe5_bN_OFd-Lypvl9799jRrYKa6PrHtpHWPzqiUTy2VJddFbsd7JLLoS30oR8UmPA6EdjTW1WivjyeUqPsfoI79ISIAw9DmO0XvGedyTxPFj2i-q7Wt5ErmIitOhyAsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDKHfKqFnEoeOoI_aEu-kXM1f1X0fNWa8W4pRpODMCnRqJ1v0Sj4S3sxSzDm1jR2AricXOJyVOkJLZRS4DrJfmm3SswFT0bRVVC6eolNOJdBKyZffCgKlgypGzGMgprlBh3_SACbp5cC1qPNoZ2WdOOFj1G5v8sylNqvmMWrw6ITSl8VVZjmYMDSLFfl0d0a5SzB0UgFE2Wn8XiJnauS4nSEP9IBvpWZ4ldjCg16VSRuMwmArfxZdrlcFH3iawWypnjT7GWU3hpWovtsGugKDXJdR86z9U7rdxLC8iT-B-sMLK2jgQdhE-cIZwLDCC125--qdnG3vub6ZlZn63iosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cty0DnrjlL20qhHs7CATKPYXtA7K7dX_FbOW9P__uaf2fHTX76VDBwGyRnws6RZrDUJKtysULOTqK23fMrWkY8bc2jBfmKyyKaX3iMkst0dH25bAPIp-1SwadlvkpdeGoQyYBPRixQvyJ6cN8pTGUowvzLKA4S4lFDwQwu7rrzMwKgoW0vwu9UUtB8c_2h_Kwu_GZharwqoVoRKIlKHd5Fs1ZSOgagm6QWFXSEZCuOg3AjFfsptMh5YyIDzkSIkNVlEXrFlNlnQpHKtXEIzl-qFy6OrTjoLB0z_hGdLjwVho3N8goPiA7_C45_fFyDxQi8Wci2F0OI-SPUJW_nIJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsR0DnAx90QbKNdT2KAmZzzT1uisRE2b01XIU9dRiqFODpmFuUM7k7z_FBFOpGTU6_So34PXgmBXOZ2hRUTcpsg9wZQYsxJ0Q5qDbRkAI3e3PmP96moOwkFcoedNjjsnACS1jj7vlDVZ2aX6lLsLgKUUHR8yw7IVRT0EcGJAF0EHEQXKwbKRJc2Eay3JSFwtb88nhtBwvr3fz1mXs7wILTBmXearQxxguG2FSWpxIWvdWO9Sh9J7aVr06zPquLN06FVeqnXtXMcX1o9dnnEJLLA5-vuIcvLBwZhFsCBGbAW2nKs_bBQTdjM5d03mJzBp9TxF316pzA9G3pYQvQ42HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAjtGryntw2Ls4-uNW7zhX9ixhNievVbJuwkf1Vj6e069GBeyW34Q0KbrHxEKBxZI6nABzzdkf8MYkHnGkryyCuZ0ArESmWw6v-dA3zPsH2lUI6t4eXwQsqFS4PUOvq7g2PJc9bMsPsZQo6wtHQwIGGd6N8POvM-sr70062rgcgu0mSG5wtVJEXXjzDnRY1WYDUroHyMNzNoDxnwUmbg-CvPrHJF-qhpggZtVMJ6597ej3B9OJi-3M5E_VjaTmil7QQZMs_z6nHEfMvQK7Q27qR8xz2XSRUbkReppz4wvNFh-2mpFxCldSuiFvCeyzMmh46WDmNs3in8IeT7NzVK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=lBGBEHra9-4WmLZv4uPS3tsfzGfDZGfygnq6lTaVJLNWXJbSaUtiVZAJEaSz-0AsDhGDysonbPwoOSS8e_zlPHCJxT9Z4md56Rq_2pRc48RYT6d2Y75Oy6V5wZR6WYJdSy77Qez6T8AtrB1vNbNwTIUK1pUgcx7hsTExaM8uw6_lPEUUsEpBrycpu64YftuxEGZ8avSLtsZzvvfZu3uNqqMP1rzbTTnfW104TIUo-MksMGhWIgXy-07XGcu2OOykjizmHsY5cjeeroz7DESO6YsLGMAojK6CmAoKq5UgJNafFMVsiSeklTDCIGSgK99E2HPe7U2i1qu16WY5OGwXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=lBGBEHra9-4WmLZv4uPS3tsfzGfDZGfygnq6lTaVJLNWXJbSaUtiVZAJEaSz-0AsDhGDysonbPwoOSS8e_zlPHCJxT9Z4md56Rq_2pRc48RYT6d2Y75Oy6V5wZR6WYJdSy77Qez6T8AtrB1vNbNwTIUK1pUgcx7hsTExaM8uw6_lPEUUsEpBrycpu64YftuxEGZ8avSLtsZzvvfZu3uNqqMP1rzbTTnfW104TIUo-MksMGhWIgXy-07XGcu2OOykjizmHsY5cjeeroz7DESO6YsLGMAojK6CmAoKq5UgJNafFMVsiSeklTDCIGSgK99E2HPe7U2i1qu16WY5OGwXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA9Qj2qvYqI9YBKV7-JB60ljhlzSatO_07vEpm7TnU4DvupBLnghnHbsfsmXTDu5lDYjcqxgAfJJPhFce_2OoML8T88khtdC8urEnXNi4PqPcPdNJckkwSG7LAOiVKTSKXEzsFGhRq7U_579HTZOMSFbmzgAlTROgVuZiJ4il5QgH8RFfcZ6L4L7z3TbQ0pjQiTokeRlkKpfy4InSX82GPXT7GpKXIj8WcuCjJCPZ51AcbSQUBC0_qdjj4hBSYNeXDfFDlq-e3jNUIF1OiEY6qy3vFXZ7hU8ECLTHgSWoVuXnNhFUQ-__59rfweSULC5av6DUH0EkLGVFIbnIGZzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
