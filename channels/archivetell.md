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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8m0JWbOhctAf_HMNC5D31kv4qcebW6_-UHWkGTCUgW24OAxegon8jWm0npAc2DG_RHiMsR6ct2D7jiQqrG1njjwZydYXAB4sAHh17u68zouU_UpNYC_xO0Vr1uL0MOZLahthOcU-UnmfObJT0oxxnAKhxIqSb4u2zvU61jcRyKTE--iHf8ZOORMZ-pJX-WylSR3fed3XI-GuDvSIN6T0DydsrU5wIHhxush2I3JkT7W2Yc1YWSwwIMAHQcuR70oZi5KcyIwdeIEYxEiBJg-txg5urObKvADeJ2gEXQrdPiZu3YmifbcxHgaWvjXF0PV5XeJ3gUvlJ2rneOStt7YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZvFpkxLHs8g4rNTIFEGd9TwoEvyf2cdXjyE7THBpzTHqlPYaH70hPRuv8ti1LNCejCOW3-__g1YsjrSWluzc_RLJtXUNB2zLQG9arkLryMNxEV3AUTbbi99Qr_Ru6X-CaEX2FOTqA7Scob7TGsNnRz3VZj5apy7CLJau_ZMJf-V9VG9mPOfqP1Yeg23w5nVDy_KepN1g-KocKZg4nYVjFEZyERqwMBqAh8BcmcjpCytEagb4S5GO4TCkRTV7_rMHBwJgwfspB-ZeP2VKJXYtKIUGK-pm1GScv3LCaf-RmimI2d0mcSKQILS4l7wI4CW9GLDd6lwgI3YIX6NT_i6sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiIt1vKvgfncPe-P1NNBRdz7KH-yD9ej3Z2AG67IKf09WsK_DW1XwG-GH_EGOJjjZoyoL-YublZVNyCY6Vyz08LZWAiNeN8ldtCBSViiWa8PL3hVZ8nf-rfT-CxekzrUyOhSgEfSB6IbdQS3w7hL056HkEaf3OpZKSD3an77YhdlbjO7xw_kBH2_4dM5fdebOLw0KwkPUBDtIdIVC_KRX_vFH_K8RzQrCvInMxi1Nh1DGandQ07OLhHRdn7ZSi-AZkW2TJ2ki7_Zw5DIa2Ikc1v18FkeQ4B2EjE5yooBKgyrW76GoidUk0zJwsMeDtxdscLW0QA-PF6uT5HgWZIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjkotzWLXnm6OlqneQHAEx3H8lGAIYl-HQQ_NjAzo4xNOsQhzyulIBsYkoahJRuKReF-X0gxOCv4Raft3lOy0PzGXRD0IVIFzszbF6T-x_WnIYRpAAFBGMU5mcXrQ24VMK5biYHZpaQf0fXvSdlESwAP__5cmIV7mt2a6y-zQdzTwK3l-cCOTUH4ioeND7KFMuZWBXH_nP3ydu8Rs1jq9_IRwsrU9M9H9c_rzZMtCqu5htFDK8PIVYZ01duWjgdMQwwVevypswkGnjLPUqST7NMTDNPkZOJIsVOAnrvAMpd31bwIpoQ7mSmvJSxw9OlkJzM4wWiHhC4atgHAWP78sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f63bxLfZ5uE8rT6IY4xOYSLiqdXB4TMn3v7i-rpt3anA_H59ebFDf-YLZxeYf5M-LIdP8xfI8SYmGVwHjCVAQ9griX0Li8aMNQYFN48Fyta9Eiq4ffhWvX004eckdVi_PibWlMwBrvGzXGWg318UIqs5Ca8rjwRjwRIfp4tyPSpW5V6llVlTKCpSbbn_80TrvrOJUayxSJVq6Yb13aKa3aiQWuF6NciocbNeQHJxRWGM6_-hC6RyQAovvBnQPqZ7Bs3uDQiDcflkUrPgWo2usizRYQhhwOu7f3wsNpeV-9KbaJOpxCuAKtrDu2AUOqXF6MyQg8XZHcIj8UoeeeCG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg4bISS5cRaiHGd9jWTIyojQP9ApWUBW2eKjMSSIUIIqHB2H3_MuREXbDfirPqaubYtfP_zdQHjlNnD8Fm_xlTvqCkzDrLGqg9D9QvH9ojtLHztlGT7JHjATh3bmjxNz6pnfpHNGOX1VcjY8hj0cCFQuIrOWH2WZXMpM6kIJ_kAVHqAJI3DnRDoEYWQhs46OX6t5wHtMjpuzzAANajL_5YMRr6MqQ6V53gLlMZF0A_HI69oxPDHv6EL0gTH-4XOFuTf-ETUZEsU7ixiK2z8i6nN-_86mNbzvFfnxb1ltAG4Jo9C1DypA802p71qc652ayMO83iNodmPAwRB_EhSY_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFgmyuKRzod_GUzr70tpTWBDVqgIkfMM1SLlRT5sTn8EG-XUfrjE8lYKKd-nDZ4wsLJyapYql1mEOBJ7uZpyHeirYM0RetjE_2W3ORLJtOFfPtDLuqxtH496qR7XJb5bnpgInzV7pWH9C6AyjdD1VJ5dLlxGDA-ch3zqEo-_yaowpowAxpcpBWzBc_w4LbDCQ7ymfUqtheGons8Xlkd5aSl_zVTlzN-RmNIKMe_erY9vyRA2rWM-chhiz5UnbTAG78-hBQ9sY1As7k1BWz52Z2NdNKmt8CCvZtq3FtpwU59RMWHpw14-bMH2hStzrGZAc3FYDsVT_kmJUKFGnz4LfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkUQUx00pBodkHBRnncZ6Q4YzWhK9bmKeMFXu-wtC6E05I_0JGU8kyS0yEAuEceHvt1ZH8aA2oceIgT21T51Vb3OPXuug-nFhpEdRtgOPXGV8mDQcz_w58UHLl_5SBtJGvyz-juTKIZxEyanMwiZq4cy68-AWRgUC5ZmTJrmzA81_uYT0ZRVumPn8enm2mvnVQhNtZU3DGcWWMz8ziOqjngE-j8lR1-uR0C5E93_UyKkZCSz5IN6TGb-CaDSBNnldLF8uWz9OPUEZacujir6HJDl6N5WBbhMGKFmjkcgchr1HikclbROpQRWw-u47rour_rW5a68eh0QbTG3APDHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnGTOYzRgm30Tb_q_yHOUV-kkwoc1779yCqqBiDgl5U1Zo2Yoakqd6C9FlC23j64TKpd2TPCAFqa59HBudgpjJm9XRGjpaVBNVfS8lgtoIi16I6Rcg9IHaLyRwQm4moyEAGVyHwslGzLR6KJz1Bls0eDCjmLD2cA3nxqxI6Hehx2XInOF5cn_XFb9hp3RXlBsBjA1M_RJkER1zgG1FHzSNV994nAKAX_2Sv9EGTGFwfQ6JgSbuML5L81bFRSN1lCHA0h6WujiWXbNPRvQaOSAzh0ukQAiTXGu01tHA6fU8SprHPVNqPSrOXkwGpR2TTAAstTN9Wt0Yez2qDPsTdTVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2EZ-8DPLl1SCkqKSY_dIJ7YFOBCxzK25I3JLALOzQjSVxspiui7BhcFVSm0yrizG_WTKjPjoXBUCm_7AxjiI3Ui51gbxvzYEml1KWmLpcAyBB_KWBJxbp8So9b2hCn6UJTga6-Qkffyiv6r4ufqlHYKF4p9RtHMxwXXBWihzjhhQe_R8kFxsjP9plVkuO5Gb45e9ry3EWScO3abJGaZV6V0B2hRNOvGMwWaFVvQ0RP8KRjzggffp-5QSBKPa1bcpnP71wEqjTtQfzAyJhDRXMdhqQZkhkWZX7dOEWAyDtWYs6-uL6WrjC8NDArXe28PISrJV8-NVxStm1o86qyjTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv_pNF3Xmfc3ZrWvXJXaINX972b9NMBoUZHvsDpgP4kQj-QuNdBSjR_-LDkTutCOFm2qNuiYkAlKUJjbfgDHDsYTdXFTtiHdoLhmeA-P8cwKB9w8OAK9kMFkc3mQn2w84LJFkAMZ1ZX5zLmzF9HtOz2h2nKh303F1T842pL7zEmxG4aOwlwbzT9RriY09tz3kwg1QCkEO3TebazgnSL1Lj-y1Lm3HPiGwnIJ85YBpTMoFKC6iCkBWuEwpphMnbhCn6JoBNWeS3JaFS1t5G0ETb7rA75DIziLqgbO3chJfEwityz1v2LR1LYz48rl7_bhKIqplYluUt0T8KwgE4DAiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPdzLJfrf9yIJNXbrjHLKsx_cvBNCxNDTDqGG8lz_tIFC5T0O7QfSo2uOOV0kEx1SZUhAfu8Ty0a4jcTpBwCdp1PpWrH7iwf-GKwDxIruuNIhK33a1zrHqF8nacyx6GDqYjSIasaAqAalLe2xtFTsY9jmVDqiUERvSnNkIE9E4_4fsLA3q3ZK4aR-tztnWrb45sv8a_-mEY28b7SN2LhENWozG6WQ79seyctRArr5bknSoZx7Yr8sXwBRVL-zqRLX0Aw5VCjSpJUC_N6mSM8m25b-WJCmKq3Gstdpaoo3Dx2RxIoM5bj3xfXUWG8OaZZl1DAtOZxhFRgygoQQeTxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnqytkRMY0HkUBE4aOFvxt40YBRlYyFZKgdfE3NMFJBSuM7whMPtIbzaSSM-i_5dSGnMkX4WzbYwbwU9sN_X_j80VN3Uhe7Z3OCSWa8WNwfu5hcBaXJjSFMYr-w8LWxDPUsF1nAu-qZKA-PK2L3PHPZaHY-dIyc6kJKdMaiQJLYTx2Ynwk53I2lzAc5Mc_egZDBhSgVAfxYQau6fOEJ_dAMzTvO3EknWaQqtukpHnXW__WGiQ5gHg0Gwl7oW24d_GlTpPmvE2BRr7XqsDv-FnjmVrwR_n1tsrYPoooE7yCpO3hS-W7U_XCQnj9uicb9-jzsZk6knnIJQIr9ZMVSoNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN9zvhBxVUOu5Jf86Xqf7t5GUGy6i8mpra8wUsIlI0YD-uU0fiZHg0RDBQNdDlhPuVaSZJjcUhDik-0x8o3qWeAI3AvflpptQSZUKXjXV-AX9M_cpZB7PM6ShIWTk7GFJ8_oRy63SfsAA9iCbB6vbtNcZuLIz-iSsrmUdGTDeNcQrEClMW0bTfHNthojJtUQeVjX2e8pIARWx6tztOr3OI3fCWDGOp0qJ5bst5osW32gLBKTsJsSRHmo3J5l5tiAlmNdKbnwyFe3nMVbVlW9MoJnca8cc0qd1WLSan__ok8M1KBTL3KiwVpLy1hAhBBU6c5TBVmCgy5iDFBeKonqhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwxiUQ3Q1bRoL6Jwe84smv9PWscCjWRieMNJzSDy0Ee-wMv8ybaR2DOMSZLrx6M34MlJ9t_xsqTdRYEZpkMZs9lMu3Da_WEUip67fDLeMAuuesCt4Juyir8aK4cd-F0GQqznawPIuGEQhbtxBksKEwR32U7mdOy7Z7XI1pQKShlMX-lbayqJ3adv_TLYTDLKpynHUr5yuB4rFtwuVSKFnZF9mPi0ZxHpNbQEh1W_LF7Riy8oGP58Hve8MidMYbNNJGRHTZDJfWTx9kyiuKwOfNjtBPnD27GwpfBhGoaoWWO2BSYiD4ABeXDkOwOUfWy2fOjTsdr2uCCzanZ64p93kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4BeCeoIUFZvfPhzYTq8rkzQi7nPEuOvNvfy1-6DZU5I5zGMCWa0QmcE_LZM72PTo75kjypdm0c10FWMmbBlJDzzCDs8i6UPmCa6OkQWbTUHdeqGmDl05aku44W4hur4Pk3Eio4oHf97R8vvg45j34poAj5dTtf9ekHSgxtKZudKMcTa1g2hsa06lgQdjt6HCKritSGD0oR-4m_eCGto2mXJN4CcTvk7CpLxfUEpiOujUOEDiyCkETtGpxxCkBQUSOBuPF98ISrsRw7SbVA3YSL8MKmykuptbRaGamHysSa51jfXylGd7tp9TwAwdwGM5cUoNBkyc4fT88K13xpETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNZFiwZL08lxOrbKuXEUlvoETNnnxxnIgWPE-y6WUzRk_pwIX8GzSmdgTM08CZMwbzd8I782o54bpuulhyp__JOax91YirhmGtBpPdgnxqXov89fEQ282b3YDs6nnzD4yTCTfwO0wYlnaIam_z_fEkPq1K0WqLbxaSwk7OZPFjb__GEGcToew96HBQ0bxehyebEAWTlX63oaaG3vi2ISIV7mmZgy1c1u-Z2m96dFB2mGWOFLkhjH8-5i8e0xTqkTD-JRoIhF4Qc6YbCuFfbab0-z5-7-OJRhMFEEMVdU6HoY0t-a2U1oOusmDZz_2tq2fVVyhH9svSsS__JkveutLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boCkc2ZWOX4-fNP5VUf2Y94gCIf83LYnhfVdXpro8laJ6WaxBJm8mnevCIzYDjUaH26PYC5VVcOIhCyZKhFq9UCVyoEJIIsRtWZdhkBtCqDJ1BSZ-EsrNswU6iveBvtUytaqwmcv8ue9tl6dF1xnFcdM05E65P3JX5OiTjm9PVBw7K2oRkZr-KRS9AnIyhiWx1ZqrTQirocqyRwvDkJFphrYAsiWvSUKCuNlmbYdrI-wpNBrftQ7-7qCqoviBunmUxbgmRtsrFpwJvQYHmLSt0vZSR1firKkcueBUvgrDwT1HNDZbtEfXursQz_9-n3upIbgTRB_-GZRGLtkuRN_4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcLzhEmPbnUzn0mqe2KeS3xqiHfZVfJEfNg_KDb9MmZU8TVWcJMi3yr2K4ubd_I_y-oLw1lhyrn9BJSllA7EICuWmdmP4phlkTRRG-cf-YgK_mEiJV3tNn3Scrq2YC_nkCLA3VmZButG5zNmp8QElvsmDrqJGCnCylmxTM8XUUm10LaD85LGHrFwNpJTJP0rPJj0wEw5rKG3DRR7j5M2z7l_WkChK13rarV_tyoOYNOE3lP9dbXh_N75BEbpVRcYSt4r0rqlTKIqCbjVYc32b5D5TnhWIvaa5C8RG4NeA_i6fY0q3sHPpfMYzbswMn--MKhur7ciLMOy_rS3BHkdLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qL1WZkAtvNHBlI9UA5EdbHrkm8PumpkcfIyVKHhrYO0heMJl9kJjr715Zjr06IUO81JWny21Z9V7xc1tfnYJVwfuiGk-YJWjvpj6g9PNlSaTVNOPn9qbD9lio1MsV6Nmea5NH_0afT0PKi8_CIrillfm7KE0Y8D7Hy5duKFKxrp9rkDjZv_H8lbLfQfJ4ofszJK6-CTPxXGkykK6E-FOXX22I063mU9B45vh-6v9REzsOw0UX1H3CY_m8_UqXWVGgz6jcpPfFp3WU8xEhWcEJ6Yn7oXcVRfQZrb6zS-tuIpKCLqz2KV6wxiz-5Nc_bqQfckzTXq1w9BCLbKdXE71gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPJvYZYY35cSQB6qYYLxZsVMSpWEtYQykzh2HvI_-mY1jwQklJ0mtA-6jeSmpE4Qxq3WRQMsiCEprSFGWEonXQWgsnS1PJ_IZIQHxDPYF2Uz_moIfrirYfPhj9Fj2o7t-OmQmXiudMvTMaUVTnZEd0mLcUbwfQno8QRXM3Yk9zveoAdDf7eGvrfL1cC_hmcvu5m1PKUUh_EjPdBPvxDTYFPqVyvmDQaJWK9BOWiSGs7L0k_7PvJ8IV1DxfZRHEiq1w6FKwb9d9auuhHfMtuGjqq644SAGv3sbgrHZd4gSg-ge6rmoVNhwND4XQA1qQnmdU79b5uy_64Zy6ZQJ2iFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eA4BOY5ihUtNkLIMU1tYaCY4M_NqQSAXD11ru2Zh4ORLmqJjvRgWbvOLV-7H2_NN7E9Ezn62JjNFj4ds7Agmk7H1B1myIxJDqyFRyrJNFIakz_Lfjm64kNd5HnbgbRS_gyzpHc0UmA0Gqnd7_WuhahZ2XP_nIeqWkWvd3nhjLDwWzEcY5tzISKNtOyA5ifpwWBKVZHcr2MPI7MuvR7GxBe8pbm5z6TQ1PmuRrNLnUttkdW3Goi7hC5jae1Pzy1EEjlY3XB4tE1sI2FOXGzT3cL2cY5KxWL2IIMiTSbkUgXQUyNjCs5GN40OTlNF3ERL1eyRF6CMjcaQ2afzBWP3ycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7U5IlP1W5Hma7o6aBfGXjt5VvWFs6UAwN-AxSOgDOh76WWhLgnH1CucMmmZuMyoCufD19s_NbDgnJRUjos0MLIOzgc7x3B4U8YG4cv9Wn8qT-aNh8KRR0NPrc9qaRvsv9BzLIXFdgWmrqcHVG2FPRM8blSbC_94XUUE97hfdNZfHgTQwQJF-jFXlS_Epv3HeqfOZ6VJxvCjxYIN8D6EoExDeMyy_zoCppCJNNiHGkb2-sDariBx21iOpXStj6RUBz6xsGc3Mk8xWZH8E3JOZo5DAesbyepiO05TjIavC8cJnBlrT1Od2vVnNffYA47jkASf139ObsmfPfU6JJeEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_f0vdapIL4_SCTdl_QBQEx8qiKmqao0io4wz4u_lS6JcnUZ-lBTwLC1PoV8tqjNWAarG1E4aUKr3EWcfufneWl-wapvk_R_QAXgWoIpN_bKVs5PA-AfNysSnZYXQxHNO5bgihQ2-IrZIVK5Eb4B5wr7n_zdQtvejnYhpfBZ9rwCZ8ePQgQ2FXkk8uL9E2mwhfNBE5L8Q0UnrO_61309HZbJiLs_btSr5meb79Gpt8kx4aW18BI5PIP2JyCVnB0a59dZqYvyaU7QuOfOt2PHDt2mOnEVSd8h76LJJ4iDyfK-BpEKFP4OZzmnEaI4a6u_YsgwamkFJZzTMpTK4xjK2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIg1yetZJ1SwiTu5e6OlsVqqhHDH_Tm8Hs9WOIROYvpxLHumNuVYpR0S905arfb8TkvfGY1Nd1G8nj2GRLjCpQxOhFOTUGWNmFbS4vdcMBu3JiKcRqyqEjdwW0Fth566EiVhIO3fNVNIZzJDkcDa75uw_4e9UREKJEilptrf000oH7swIsTRidRuf6hMNLyKmXv51UxylHUrbcNQwESIl1CIYMkPQK8vs7CSMEeM3sRkQBdZq-QaxDwvT0wgUxPDxHeWrosyG99svSs7Qu9MpGF1qFkk2Vr79GCUdAya36mujGg5KpAExnwfDplbl6UAy-4pXUDi9dUs4Q0aCLqy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb-sphuonPfT9EhAqUV0JtQuzbYO6wCeKkI8Sb_lVmKQo_qzbg6GK0rQf8l6nDYQulTZRLxi6XFW497gHcv0xqG6b33wVNvgNafULnQV1ILGSv6gHjtmeEEvK9fwlwK6M2rq5nNAglq61AXGUPQsD8PA0p2rtmdR36YajemHNZ9COqBt3a5hqYASg1vAvIW3Ku_CKd-8kGG6UposrH1LUEhhnPvFlraAJUe7w2sTAt7thPN8sCk2LWWpkjTiwvJ7rtLk_5HJhvmlWjtAHEwDWWiYsOuIREfrDvAieSIqmaQbXsRzII8zJH1syEgXP5g08kCUQ887DWn4Kbk5MeNodA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0X8FehcUQr9lDm1r-pqhEDTGY6IJ7AEo-E8XfQjbbzuI4HlWC8xVEjk_qbdIHaC5so74-rYSF1jiAzIXBPNMTiMXWymZYb_YMIQYn-jOmJ0hjFYr1AomlAGUB-Pu7sFDH0YMgkc-hKBGxXEUZwjRkiCHBFIRCvpPPcG_e70wtWwxjU6oDt5nbsXemrgJkO031A4Urt3eIYaB7zH3ciqvOu94LHt-5dATiqAjZT1ULEpPtVd4Nk5JaCwtbhAKSmZmW6t-dnQDGtiMdim2WJPjvhyg0pu46leQfdxXxCDuhRuGCRiuYVUuTvglKKWr8vTCPo8x9Axje3x94xpbD5PGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIbdWdKhAbHEbuWHBod81qadQassP8XAcp6VjA2TaEsIvO_7LvxgF5jqnF1qvBqhszV4904QVc4MoejVwzbrinwxgCjjhBmzZfRB7kSgFN-eJZ_4lv-e5EpzM6iJ09JOEV7MMmYmysOdblRwcGv-ZaDv9-HEuyacu5ZRiFOK2U8cIQ4wMQ3L9C1CTeRdAJRFCzrcUmRpLxe4soFJNoXkVLF01USnGo75Xvksxw73VVKF5HqJYzSG8UXTNqTIL-rOOe-q6hHvNaFRW3uq9-Qn0ZF7f-MwYS0ggraQ6EX6p_kNYLQL5nBJXnrLvbDB-J-VhV7zlSMRwFTrD9KZkxaK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7Z61W_lGU2KtFMuVuJcLED_01nVhhZD2AiD_rf2vnO1ffgHf3_3RqijeWsXTJBexxBz05aSileI1oZKphPCqIi50yQvJPnwxts49hbD_rk4WI5xJeyh6-3DH6CoHKD0nEIOlt2BWdknAMRtT8bzmeYJ84t0Exugwbl6Z4flYD_Uwv335-Vr5Ow8lguxMfnri3WdHfsIr_T8A_eQ0qMgaZtrh2y-_o2VipjLV5VUo0GCuBkrN5BHyK4rt251GabN7-NOCv3bJbOv7NTRxJU5XW84wRoljrNfdswDtNPTRQk5g77LSUXThTrO_P79XcVsHmVBMDyWJ0TGgScjvr4RvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfgggfCoe5Udf5HlEkxlIK4ysZxXpzZ9tFN5savWtK1BqUUj-m3FhIj1h-G1aTdOybG_lqF5zDH8hhNLUjpBMbrXrTGWIK4rgnfVX6VEJCD6gUmqFI1LiboczEjaQpUkkNx9qeGH1b0BRi2klfuRhYriS-Tvs9KpC6jUIU955UQCDvuLcvbnynHNPtqgvCqVyZKDu07HWvKW55R3iOmcT6skH43wzO0MxPQ1TOR9CmprOSk2RPOCGpagPYH71xxGM02bQT5YRMuVtp37idiyM773gA8lLqU2jpS9IvnsyL2rXBRVFNB8h2OT3r4mghhCg_AOIsInRcHfmFyDrmGr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H39dBMIezgizdbkD4pUdp6uBbyuf-GJKJfN2mMxreHWeg4mfw_I-047_D0QBN98ZX6shz9RQX7yDSMsQOPL-W5lX_XB836BEgutVRV8qOzYYjG9tNtw5rq4d6k8PARK3EJghRJMGY2YsyRetB6BFnnrs9ELyAqy0LKGP-wXlqcNzyKSQhqBbYED54ykvjP2ezvXdaYrTWoo3SvJY_T0L22t4s9yJgcO671hRgP6-UoQysr2byROl6kY1KdN_M0JO3_DPFK9_nRoNZKoObsfzctRO2JSTISsWH_VerrDcEDUmGz87WbVHwkp8TOdIkqsStrP6_1hbEiLaRnKQojCOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzjAcvQ1rVvJp9C2TZNdfognN2Eg3CiKwTlB7vVZlNrR6LxY8QRJRfLXPHa1tsPBmVbHEoBQw79ngJJkhVgoFB59pQRUCE_YLWnXKqrCfu5-gjG0HwdI3YqYtLp6Fnrlrmd79R26rF11sA4aik3vAIs8ZoQERW6_KWIzloqQ2a7JPIK4cAcPnzvT5my51dwvtPCSfJ4TlbrqJKexqJMSVuDG8PdBTcxclmJerCESgVkZ-YcdlciPY8dJUejT3xytIu7bH-a2fPz9WDe2FZCoIEhj8rJi6TWGxR6RzkuuvHxhj0FWQpIuDHbkvuefaK69Ot7saG5Si6iZtpBg1SHq5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA-GpI3hFDsVS2y5UBhpNd9Uq1XKAKgF8bFS6l71M1-p2hYu-poRDzBRt7yYkkGJ7LN6gfhuK4LN528c6OYkMrWQdtbS2SICvrjzyG53DyeVPPESXF57Sh-Wo7GNEZK4aCxbvkl2kODJsK290f5enGpBxplC68hwPD9HUE4PaIi7OOZcJTdHa4sMVkSEzDayLXwOmA2MH9wLZm51qIm0SEv0VYS2HLpdTOw2mMmJ_OEcdazJDIWYZqr0MGJYBF2_vWDwmBvSxVs9p9Mxh-0PqVXHafH3yVggQXk-IiBWax0bS4MCPB1eQp827KIfk-pubrwjb_uSogUlAH2fSGdn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twiuPghEc5G5Hs-R3J46R07scxXvXdwIdevJ6WpGEFkWLyNPvp1ksH0CI6JuErE6hTi1DBC4FuUWbwmS8XR-qH3Gs-ie8KxPiryWrBykZTg0pIkKw2LMiyhMyT3ADnIV1OdEzsu_fJiqQ8HnKlLOuisozp0jTO98SJM9JE39hXoq93I1fDYaErnG7Q6Pbh4UGwoYBVu8MK8F0IjnSNPctpLvVcb2-tah1Du_adD7xMqRNSto0OQAZ-R6Z6HBFnM_4d4zWab1ZTEAiqtXe6W_wkpwe_1EKyIKBIMnTc9u0KlyH6cb00cX4Ant-05Mtzz7LN5Tn7cR8YXEQNZUNtjavg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnJ-W_oBVlehBwao1pco1XRJZpL1iDsFSSkIbG81Y43QyWPSoLpYvLgqYRkzsE4XOqLSey7AiAmIebm2dHzZmyDcWBM_D9QcwZBmqi4NMtGgqOJEIxUfu6NGSD8FEcSgRJ5L2MyrLoXAkDaOeNEG1csmIz-yf_goh1lvoHNounJ8GNlNzsvSBaLfww9YcDVsbS6EQx4aBoiC3sdlcbGbv6BWTN85t50LVSCAmMcVSnUdksoDuFTIUrLHe9GiJrcSQgnVGw9qq2BiBvv1QgQxTH4FmxtFHj17CdJJN0AZA0_rwzFNDYQ628jygX9HX-yYYsepu-7yyWWvuIAxLHbfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auw74zOWwOPYrcniaenGkJMu9ET0gnfteCl9ba06O1x4S9X4ZsYXS17XHYKIwCLKm3M6xULu6je3Iz3uApxlr1iUlg7UWPDcIdSWi8H-FES78EhUXJwr4lGiF9Wsw5dmx8VHdoag0kOn7pGYQim2zc1cXcd56uIlfQjwSEiLleriheTzil6FWpt1MmptFkndCtStMjEUeCbmet1N7zs0GuzhL_GxxaE9GJw75Xck8fM5BMmlTvVZQghrw3plY_ew_8-6utsnUQS2wxNHsxWtOIVSaIE676DjCEUsLthwmLZTcbUasseuqE6qISeooJYai_kq08MNycqUCIM6AXNwcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKNS_wXJkzgX7145qfrfLNGKEDvnbR3blRZxGOP_T0aSbZyYkSTANnuSYujA3O0J_JQYwaX4cvPGsOOc07TZvQtmEFlaB_cXTTwdfwtDuTr3A46SrPnHY2nuyj3jfwQIi0dfA9W6Jcb9IsCxGgXdVEdW3bnWySdaPiCOfbXcZJGzydhUyMnOGWLrxCz13thxa1pEOHhK6M-i3g5b9ML8wYgpLlJaASGYloEZidOnXjCzx34WFAFlvwfM_npNSu9yIVAwa0R6Ab6Cgfisc32hTlM3FffGfK8OMvL1bPzQOrxeDNY8x201ECfXizzUnECvSui58kAaPKkssPS615saLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gs7N9ux6m-7edaYKJ0nPhPW6ojzLRdfKMWaPgX6TmUFiJF8ZevbLEN9ShTTtIKPSda6CWwBS1ac9PoRkAttD1LW3iOnSSiWEp_PHW-NHh01SNc-b1CaGiXIN3neuQ3rEa2aLD3guOKkeTCKk1M-XKLKYEFcIfO3NEzGqoFPCMDE71exeRldBvi4HooBjhJS2Es28yZzR6T8nDPko4YF_Fcxnsl2xyC5am-s-sjRTM8E2tZ007-xzwuuU9Ix6rPrG08aDdsRwjFPAQCrpnY9pc5NyHdo7Pdi_saDxXlnsz3bwQvgwX4cC_7RqfstsUHVwsg5U2wKCRNb5zYQ9sMttQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=Na7fFPVlClau6G2Knl8ewkvCevwUo07mZXiwyR_eA6RQNzapoHsIJhsGmplMHfzZ-cgneFXqYMviGKxQCRklPyGpbwuZNuo57RMyo_1TverFCUjydwRL281iq87iA2NcFuQe1JJ9n6sVVP-KvUpWpEC8vMk3S3Jv2Mlbv0E1FlQbZmTTvEDAig-tPSqyH6sVJSjI_hEmQ9Mv6YJ1EceSZuiZ7W2feEHVMXAtxf0pNFmV2HfgdGKZhjK2cfY62B95_qnCQgDjj_q7fzYTqnBwb8_cOvO85LNAf8hsG0ZTROIWUcWXuxhkfkQe3KzjJ9HkcNM4VXnH7rhdhy_tii-5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=Na7fFPVlClau6G2Knl8ewkvCevwUo07mZXiwyR_eA6RQNzapoHsIJhsGmplMHfzZ-cgneFXqYMviGKxQCRklPyGpbwuZNuo57RMyo_1TverFCUjydwRL281iq87iA2NcFuQe1JJ9n6sVVP-KvUpWpEC8vMk3S3Jv2Mlbv0E1FlQbZmTTvEDAig-tPSqyH6sVJSjI_hEmQ9Mv6YJ1EceSZuiZ7W2feEHVMXAtxf0pNFmV2HfgdGKZhjK2cfY62B95_qnCQgDjj_q7fzYTqnBwb8_cOvO85LNAf8hsG0ZTROIWUcWXuxhkfkQe3KzjJ9HkcNM4VXnH7rhdhy_tii-5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4gBWZy8W3I2Y5PWHokUqOtQxu62tFA_TtKxpglBH1da06FcJH0qtqO3VFdxFNvpMyshHT9AWnFLr0tVSPP85q2_2rzSwS_nn85kjCg6S7r8X7kVcCN9CpCDMkxvUYP3j5GXFgle5zkJrVbABB1b6d7UJ11dwgNeGKKchj8nPpTOX4sS0_oI5N_rT6nqgCc1CJWI60lAIr_w_qtTR2sjjLW70KtqzNj1wuqSk6GKj57rvIsZcTnoFjUwOgskX_Ief_gTTpArreY_uZ6HkNPvf3SuuEOwY3pRGfFnHz6m9V9UXkugMC-4bYyJFhpK-mHsajaN2kNMPG2LWRwNaPb5hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro5NQTzqGHnlOVCXq935JP3Dl-KRtyKIuYbdQ6cOlyKG47dAmoVyCZwYQCnsqjORBpA8qtKpFTkPSfy8yhrDafe7KN2ffUh6SpkYXaR92Cz1FAdjKJSWsN-q4wXdbrZeSZxvHm0dv3ytoBZ8s6-FUzAAV5Q2Xa4jLNCcvWyDQXD5y4COvOg4Uzrf1IR_MqvSiA96j0IpeGH6M4o_XmpaCtErIcsBvHWiz-JGiK3e2oIanI9rS1_qbqXQPuEeSH5AFdubh2mS6Vyo0pdPpElQqSMU4tOaHRWso2tCO_uYHpeC_SSJEyqmboCu8NfMT9V_Xz0VsQ93UOywmYBTj_EtHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFzGuK2HQJ8Ewn_mQbIati1njVqfaZAwD765onHOiDkgcqqJkRbQ7bU2OizKNUbUkpB4sKfgEVJwJFlS0GPv1qEXG4xKPNcqG358OEQ_8qgjVhMnrGEZFko4e84qjfB77EecpJ-mTE7BPdXkfVHLyR69m4rsl69hrT6lpsmBBH1j4qq7cMaz8msocbI3XROoEkuPQKAdxkYajZRKoQR0517jwYkZ-OlXFUslB5lH3VeY98qsOzoe9ZTkGejk76BEG03qVpIk2E-aVGQZIpgNfwcerhV7tD2YvTNS1AHbHFhXQ9UEDm9MoZbe2NIhwh0YkD6c8qkafln___E_JWQgiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFrYzc4YA4LnVRNCJ1-MQG_P1TAux5XlWf3NXQTtUSXNZk5xMOGMoUGxydxJZ1n_pWKWxWNrmyRo6Qk3KXjSKZ33I_kM8MojM-g3ufS_mLRuZVa8WEBxWvpYrGMRUVkedgBfZjgcYZ9_bS8pvpQ2I64FXYQugaTlf6WN98Xgvfst2IKF94Az7v_-p2YgDTza4uZ6Qbbcx2-jq_Yl1YDTfKeJyhqE-Lb7ugUxobb4Db_O1rI3K5IDdQia-6sLdpWV2dgqccj_lNTr3cmIFCo3zQ-53ORvpsr4TjMAqQFcv8SDgDpdmYsdjVEmyQz7UgAi3_Yv3Hsz-jgqt4F3S4PZsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8RsbF1DVQH1Jlhh11_-wpdnw-v_30UzhB26iERn6cCUj_4nOmSXFKM2RddL4jEcgqnUCqvmFwzzxWpLV2QVOTa_ipVGGF6LQqkMnIiRb4SBFoHRm3wywBEj8JoyietDXlQ2eaTcbeL9g2ilcc8xTiG_-IndCDf69EfDH5Vh9vfaEQVyXKlVX30vz_Gr7JfzC2uUCjB0JHJmPB5fFUR7wai2NkfDvdif1-qk4xabsAnGYW2JVnsCaDep4rgGzFsVgr4xHoHpeHBwwo6uKFe302nj8oN0QW-IzCDb05VlHZsLvOyg4GwsIk-KaOFZ9i4Rxw8vJnNuKqvPIwsHxGogQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6NTdLZiHMDmDreileTlzmV_sLqsht-or1fEyrd9ETwQFC6lzC9jCIvWONeGqpcwRt4Fq0_zEyMehixAKOsSPaUmWwwyX9__y8FzKcSzWgSm-Bx9_uGFFRL3L4gZUHhaw2K-VCYiiKw2vEzCzfPEIkOBII4tXtOSjT1Ivw81peotzXf8sSVve2mcEyQmEVLqQtOp0Ef33RrE9LAmTeiGdwMz2eGbkSBju5_Dc-dlermuwHf9WcOCn2G84Kb35jfkqIRYlNo0JRr0-H-AWdW_ShW-PAEjydCaokoqYGS1tZ6s1ki7A05rgETcVleUO-DAO7R4v8wfja6oMk2IP-605w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0SM9FJnx2kGEVhXLy3PtugoMrTLDjnBGStUb9d65KDN_Iz2xM4E4cgQdZ5ynmB95mKUKdvqeUWdHXEQ1U3996Za7MjJGTpMW-pu5zDOC__pfA8K2fE_rCfV9tdjwe60evQhOVPSWXGixGavi4mamqg0Kjx0NMIu-jFnrHaaVjQs2vwXLqZXDX9gpAYDVbWNmZahHJ-bMJQwqp_E4Gdu6s_CUXoBfS-NahnxKx150iaklrBHqkyoQYIc7uAgab5mfcbgSfmL5iFyuCYUkS30wgcojATJ4R-mOBk4Nd6D9c6DrQea6mGDjZ-pVrmYRm5Y_udr5puYZMva5JgzUSgKGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrvMGEumSQZwMO-Bj8xQkJ_la8xZdMZBgGxBo2wNhcXI0oy2aorGlbnFtWtnkzjIR90N0ZFrZU8WZSlefW_UGeQIEbFXT3_nda5W3ujZSEqE093IvYX9jmVZS47DpRqPYW152fWf8x2fOfOAykDOOT-Lj0V79VR2uH1_dL74pluli1SHWqQ1IZUcBJ7WrM0wgniRdYN0WGO3lQQgiH0uX6nlJgqeCM_tOlrzADT_z0vMpIBfbw9AZGUFqw6audJXkKzx68p0u4gu-22t8UOzp2NUoGyMgmFj9Ml85wQ1y1gJ9FEFIxsw1hfol9LPLo60tF7inl5DUqUvOanJhDjm6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FughVCeFkehUE0z0xHDe3QjwlqlypTy2itT7yl1FIdHBezKE3jWD0dfRiD-jZQgeYKwsUdUT0prrDVhaxCsvvAG-eqMpdm1plTeGUBUzyBck2PirHkUKvTaTIWwtzt5IjvbDt8h1mRJoD88lQKxlCZ4xHfGLNCQ5z3_E7WJqS9XscBAkXG-EQ74HtzRiiNm7s4e4E0r7p9OaySNbrBmhBVWEf9wJuiRJBiaW0FP5EXN1Gfui-mLwfWA0XH_2n5qJKQ5NpkgA5tKaRUDqlMxr04pAsxgHKoTEBFnFHEto2x4XHj3nYnjhlxWvjzr_QWBSXw67JM40m6vl3grsSuP9Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElKfp2LZ7E2Uqv5_dKMlIU7u1mlmBxw-NK51zOcbScvemHnn5Ah7ITCNo3ke8PfRXKo0t_0brK1tXuwFUJ5WOPBK06qhtQjMvQXx762LFAiWYrz2j1wk3AG1u2lHuGQp9i0grLU7WF5zLeXworymCG4hbStCVQbQuINs13Y1KtpkD0xndxLVp_2ELJJteSGNcX2WviUTJ1MYQ78lHNHScBrVomaMhwMZOzspyb7rG37J2rKqlrsPo3oUJnSma0-TSXUl44aZn0MMg3mx39fRM7CbWXua6x0QTYT5o-0IsFKA0Jf6dkGcUbQ-np0apGQTAGfTVTJ7VRnVX22dJz6etA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYH15Cc1Wut2JsIXelQ4VLR3xMc4PjqEk5vIiGLAn6vT95k2oswqL-b1WcI_udc0kYB8XZFtzARrMUS5w8wzSy52vt9GxTGmJOJF4QnR5dGRApDacBjYMigC2XiiWOiMh8jJZVcUigclp18oGNIjbGP-W3KzZeJuTxwSclGXwqik8z5xoxUET4KZdmQMtFIJpij88sKfhXczV_RfRUcDGB3_lgnvt2Xko_0QbKUxb5t9JjztRw87SeDtXapXEzWarnY3zR1pFaSQt6n3F5KfdCCRB1KqLjNhtQLOhNr23r9-bDm0i6cUT3m9C5F0-gxZej94fmdDGr4r0EgKB2M7vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIbMYwvtjAgdfobhNteD3kyNHl2rBEK-8PhYP4fQKo87FJOOu-X-gksHW3LblITMa2uOL0ELk8ujSyODtUsIrF-SDQR5pRF8svZvZfacXUnr2QeyqZNwrm1YVYvCaofs4gRnKAP5jmNpD7yEOqeKeVQQLCsj-ad14aNzb8IhR6vujz_j7PG6nfcC-Cc0UOyq8jkRqan1tLjpAnByh-jlSYThadl-34HDe0OINz_6sml83nCIKOjpc7Ad3eagLBNDSejXccKjROwYx8m2yuw5uWwW2LFjziKZ3Kg5SXE84tZadLFtPE3k1nFNStJMclQvDaMG8k-3twVoYIS3zC9yng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKMrZjihZQRTD7G6-UpQN9JyReR5e2wnGuiTA74zfpQBdFV2sYH3Ms16FOsSfO9NCeP-U4eIg_QOEECvLredWPCHAcLwX6JGsk3KjFIuusQDySLdA4bHWbkLkXHIa5SKNNDUbUT5eQgFAP9PppASOfixTpNbES53jzjGZczAVswmbbqKEX8Df7ajk1EKDMEos2Qfv2ylCtGU0kIa0QwSOOHGgIckRq94E6EUxR0V2EPfxW_WIKi7GQR3JkMSQ7ZZSg1ThT7xDi0JdY3WsT6nDx2JTbhF9WLG25dLcHaVR8CkEtorz-ZdC6snHz2ou1pvKlh021wTT8tfORUQmnQ7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE_bxR8Hs6zbfPMp5rw01joD95gPpWiCwHpBphyWqIh9rIiV0zGt-t-ODUKX17TWKzl1EDAG6edKBcG_kREynzi1OR1EWEk5aRoHaqcHfMRcOsJRghoOLJO2hcfKYbfhuMo13RYAPCWDHGCPmpD7BSkarQczPHKJatYTsKpmv-VSIubgy4FJ42oeSpsbej6c5_pWOpCiiSRq1ZSR7jIn0Mj5uOO13qom-EARcTNs5mGPlDGySMI3IY4I6FEmenoIcZpUeWEVDINWYvwbe6Xumdb-SlCzTg7pTZ8B411X4N8NUCxFdDhVI9mCg0rMIto3vHPUrJC3rF89fbeHQgcQ6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxNqOR6HQj6VQ3r5ifjxQpFhGcBDBfkNeTrxDc-s6dcJlz_Z1OCrJja501wIOKxcf8cBpdLJsi4M7ZR9TDbkbtKiOIN4bSmdMH2qUtTsNOqg36LqlLsJzbP3OJrQ24FcsZTyxW5Rj6Uhplf12JGoG5ubyR9vd0cz7CgiWCzUGpGgIrOcqjUhSV02xYIrDhFNgYXPUb42udBuItPp2fy2Haf1Cduzb5bsqQXjcbf8ETf6lvj6qPyMAYivt37K61FLpaxnQuE6ytsD-TECYaaecgW2wHz3CoeplJyYsnyfD-2Zz2zZQwxMijPxJqnzodvoiWnLOb_vRXbwGqr2YAwohA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n11T2AAuUsf7_p2IKw8HjEIr3a0LMaRXavjo1F5V8ntxkniVutwdpMv5DSrTrS-Jfy9oak14EAXQGqKqbZWUlymF5sEdsBbKraAwKCRVSJy5-t1SeRiz2L7PW_52F97xZV0BmXh5D8hmRQIfMWeuXM1mPGrRvn7BPZ9ClOADzgbxuMUrswbhBBU60G8u3iLVEUHYAmc9P2_ZuKGT9XJf98OxJY5nc8Oddk9ABGmKmMBIXE8mNykM2LI2pO_xIXSJpDVZVE38V4nhdk-D6DZT6h7wrXogMoGkmS9xduNboyeOtluOh3wKPzYKoYlPei83H766plWgIs0ezPFKYlwh0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONEMKrLYyv3rx12j_JaPW1vGyaXMpY4bvLGKC5UDWLnIC5MEhPnPT4HW6-T2p7aQzG7Hx8dV-KFOcMtUyFcAaqxbFN81SeemZksFiHof4_7nzGqd56tK3wGuLOFm9DKKl_geTcqDluBSFMQmh-gbvv9S7ReV9IC3r1XdCO_DInGJuDbjUv4wRmhhRt8tjGI6uwGVWJj64nhEM3rp_mN2dM2ujlKi2imgi_HP4u_Y40_6jfED_wh4YBJly25wjYDXRzSCSS0ivQcuAv2QLNPYWI9abikRpfAGCHtSu7RlWFsv3Jxnvg7RM3LnLlHPr6eXoBYvWp6EPSAKxURfD-2veA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHW9p7xgE27UheRHFQ8Ci7A_nnWajiFSTZ85ww7GbMU_7gxjyL7BjPXjBU4_6GVWtcLB8p0I-34U-63fWL35Sw4gB9Ka1A-Y-L7w3UY9kSmsfrcppOARS38uadn5r7RAEo0vCRHnktmci4EJPHjAJAk-K1q4dU3vaKAS8eZKQgfdr3LmXlH00IfMjJ-OYt0V4P02O8IvIv01bmWhQnLtx-KLjR4P7kngNfWsJJnrn54lzGbcFTHRzxRleMftAbVl1loTYhdiPLXn2qliM9CD2EAe1RTh-bOWHypP36f5z4KFbw4DfWPPZr6sYPZGaRJZ8RmCYf8FBrPnCjPFTFN5Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfVU_wm0tIyVM1-1BjvuTM6xlyB5j30NX-jNZ4Ep83QVZO5I2Mm53skyfXq4aetyIyopmw-ETpvFFxpl2tqIvn8_-ULEm1kndGy5sAh5PHVY_tRtVlMoQoa8fIecNMuX5EyUkNz8iHnfkHDmF5PxBgKOnFxKREb61vUn3jE2Yqr_YoF1BdG2vJMjXVytXJBlgkXQhjBD8BUX2v_epg-jcyn4EgOpgzRgZroi7G3PHFwYGZQKDzeD48lnvzx-zMzWWQBYZwNvzKErFh0JekYQRfao_wic476EHY9U_gMXf3uxKKKsv-8hV2FFFiIshswLRHy8oZcC01mixzAODkC5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9T5VJXtjFcvUoQ51Za1qEyyIkX-W9abGqPzU68wcO8fy0PD1o5l-LJqBlSoPRhgR5GSS_-iUD4798GfRTokR2uOifAR_c4tMPjn3_NDzhlbklwaXhtD3gbe1r93yHBWa_OXTME3HK6T8umuq6Apb_ddY0BtFU43b8MMAAwL-DvdGG5pwmbZi6JbMfCLZYCiasIOGgtnbih2c_EX494f7sq7TGqVcK5w5jTKmp8utoJkifKBIEejS-ctOKTCnkaZVcXyXiVWDfx8gfekCpYtYut95gVS9t3yyozJVGoAMGDwI9-XwEsKLY3DQAhwPdq8t1kMXCyKX3y2AQ4qTJrNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLhMNL600Adju7zBUCTVQT7dHUvIklZxTnK7z8AG8q3YN3_hstQWlPg-W9-ATYZt5ZxVCKTLVNEXbflgljgeV1zo92G2cdeTxB9iSJzqS2X9q-UMK74I9v3QxJ2oZ3PA7wjCthIuTCkHTQdSZcAeeBVV0lpeZrIwY4Ol3O0RrrDghQbTQF_NhwTFMDqb1NfbsnL2ydmouH4Se4PciSeyCQcIlkvNFc_7KG0LSsKYYmVJPtLG_7-vOVfdMrXzpC31MP_AVxJIpGJuUY6tewP1hMD5Ip1leVG2ZWoYHD6uvHiVavssL4YAjei68KM_POG-vh1LFgJr9sEfw2DnlVsvCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=tQizk8lzpcUE4CGNpGAXRP7FbiZ_G3AapCpTShXISQw4gEB3_7hjquC4xHU7XhZI5LeWT0Mf9YYRKrd5T_WdyGALirrc3gMK7CsyLCzqj9frwdhKuu3TEMQ0atYGihhjLGSGhlfvvjCW5A5FGSe4_UbnY2Ghxw4KXRrMRi9FsP7nTy2D_NCynPJp5KA3MdA0XyMjzB17Hbi_NkfvWcBwHal_yBGn62MK_FWFcmL6CSU9rgoO8e9y28wXowzYfQfk0wAnl6nZTWX94sNuF7dz2_HckZCYSgLGJX0DeYqSPdfd-u35Xfks1SF8gS46-DWn0VPCvLYGk4n22WWG5uzjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=tQizk8lzpcUE4CGNpGAXRP7FbiZ_G3AapCpTShXISQw4gEB3_7hjquC4xHU7XhZI5LeWT0Mf9YYRKrd5T_WdyGALirrc3gMK7CsyLCzqj9frwdhKuu3TEMQ0atYGihhjLGSGhlfvvjCW5A5FGSe4_UbnY2Ghxw4KXRrMRi9FsP7nTy2D_NCynPJp5KA3MdA0XyMjzB17Hbi_NkfvWcBwHal_yBGn62MK_FWFcmL6CSU9rgoO8e9y28wXowzYfQfk0wAnl6nZTWX94sNuF7dz2_HckZCYSgLGJX0DeYqSPdfd-u35Xfks1SF8gS46-DWn0VPCvLYGk4n22WWG5uzjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJOS7Jx5I6gZOSJwMBUAP4U2-ZQkPhqZ7B-EHAK2SYLl0AeduDeXc7Qofu-97kg4gj7fKGHLDSQr7uMuuBP7SehWGWVZYcbpmBR-1zo0IVbko7_f0hPEGCE649qe9ew5Q1GplAnQ2LFLFHWGB7jbSZBxntKiHL3TayVemMt3xDbRFIGybOfjqsC7hbND-9aZMwQE_XTEtTVsbPI5WYBJRta9hVG6tOzmFCWf4d0j5_KerTBKNMq1WBGrmwqFt0RIIJOvuCKIako6ap1LniY9e8iiAF-Al6jXXH5oSeOLtPekBMI-uDM0U8MvSe7TU7jiDVxbGjR-jkD3SZ04pfK33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI-fV8t7ni2tE2FFYotS6CdppSshIqqQWf4rHYdH-MWfLM7VnKYXcoAou1NVnR0QcAcjyyg6IlDAIWtsjFueBBpncp-9zwR2CfSpSiygSNd8Gko1ZHZCCSsJIKstFLCThWbNTPtQUcVeztF_zMMNE1hetmy_-Cdkl9WD5RN48W-XlJcVK4VXUdN27lQu-4DpXqt9ft_Gl6bcjxzEo_CJIk-7iY0B1CBLJAdedcd-zDXDGmG4vYeq4heSGbfOC69GleFjAdrpl1PhDX24n7oLhJTUojcgu8zL6a8R1bRQLPVHwFoi4XOWE5RjAgo0OvGLc4et46bD7dg6DWCEJrncvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWW3nXCZrbC9sQp0VxaDuCpdmC8CR_HFzPb7XrdaLXu6Nm8ksGm5eloazy2BoqAms5NBFxZNG6zPApcnhKEWDQtqzhZz3bLFbK5_6kOcraWIs4lUnIJPQibOhvsVaPf8TPFfkOvpBNFFYjuasqJteEKHJ8QW9eOKSJN3NZ9bL0HndLibmGDiWR0APHR7DN-4CeBQZ9HfLGZ0yDTCkLQUkIWkbJCpu7XQ6Hb7VgHRS9V-6C8uVJS6wljp91xQFKm1uXevnAVjhAXRrxTDFRT5lKcgkpqaXxdAHzfnSNIbJ7BGwBfRjG2lS6CXtsocKsewILc3G91AJGDZRiOt3Gew_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=Ii7jD8jAajGdRtQ5UW-pyYB86X8w-xBA06iLK7N5MTj_bR4Qsjs_6Vr8ZS37eHcwb8ClEP_L7RMTS2LJVj6XrSFKSbjH3LCB055lsb6VoLBIdv8phcHD5PDKlfm_Sw9SWPM1GNDSl4bz4MnO0dcITxiYfiHa72NZhyT0uqZkUCUphNZFIE7vsdJt8l6p7f8FUtzNjE8-uZSQUAEtmFSKKP_FwtC1MAbtreUsLI-tL1sOAMXSVrsAUfzsOzD1mopXegriPuV3dzmzVPEM7yTQ8Lp6zf2_aD2JG_I76lDoZ2AcCPw8tjHyCyvt9Gwer_27A8iLN9st25-ZCVRr_tlhsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=Ii7jD8jAajGdRtQ5UW-pyYB86X8w-xBA06iLK7N5MTj_bR4Qsjs_6Vr8ZS37eHcwb8ClEP_L7RMTS2LJVj6XrSFKSbjH3LCB055lsb6VoLBIdv8phcHD5PDKlfm_Sw9SWPM1GNDSl4bz4MnO0dcITxiYfiHa72NZhyT0uqZkUCUphNZFIE7vsdJt8l6p7f8FUtzNjE8-uZSQUAEtmFSKKP_FwtC1MAbtreUsLI-tL1sOAMXSVrsAUfzsOzD1mopXegriPuV3dzmzVPEM7yTQ8Lp6zf2_aD2JG_I76lDoZ2AcCPw8tjHyCyvt9Gwer_27A8iLN9st25-ZCVRr_tlhsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1vDaVbq-ookcQtoId3WlcVctR86W5qNy1sHTAf4XuU0Hkq0nurW3boehW5NJRM_pusDNuRbHt61D8QbxKNcW4Zq7LpnYD7qcPpaIYNh1BEurHlROVHcp2azhQNrrvq9rC8KjOM4HvcxVrSromUHr8KcFkvn8txIHvZRwBadsggyq9xZcDILy6n9DhcOphvKZ-6Cu5qD8-HUJLHzQlyR7dJpQYepgZWqH-2ksmAVsDbv6WZIJxuGlsV1nFFPyOxbqkownxGDmas9FxcHJp-yuhRM9vKaKcbaxOIpqHFzKix7bZ5cICbUS77779fTza6l6BFi31B7THpcAUKkUVpY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6t0jj-E9s5DtoBb-cUJJyc-xP4MxGxfwT9nMs5_Zbv7SIHJiLHBEOLAZliVylF1Jg1izDQyuHFzI0TU54NLC37V9tG4iHyJEckl-19iusV40yBWKX09NlMSV6qUNIng9_TzW6wNPdedSlDRIxB3fMpxmB4TwS89q2-DefCiAyfAmMGJkb_D6kP1Tg-XV4Iej3tKiEetElPWVvYZ9Hr-BW-HC1856L_32yDJbvavI9VLt__Yfg9sjkjZBh8MifDiFFl6tjUSgqbggCVpTjdaMSrvLD64W5_PymkRGraRPI7T_13RWHXT2hoJpfQ0xa2h9tjfBgU2VDV1weAPYPisTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miSDyAlI12hnHludw54sJ03X4zX9ZWFnqKRDoZdTxd_sgOXc5gw912Jkl5GCVCGBYKIvNGABFSWcbcRJWVNhvOcqpcaaTDVqO5EqSmxgiC8zdd4z-p-ZnLhRD5si0wGiDF_tKxTEv4SZLu-uFMk2YMn9yRGRFHQbwv4WJrwlYZ5GlwwzQymWvO4BML5pQEZBw7oz3eSEz7xI0Va62G8b0w2qU_kMpGk_ZRNoFfTYAU5nxLklaxxryR94ICxz964lVgxyWfYomdVE-HJaqFRzewGTyt1tjsOaxFUac-QPQL2hMgKbeedMs1iv8rKoLUjZn6D3ku98qdiFEfYwq1sYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e54GOcbdPi39RvkN2EFzHGajAW62S8GpiPzJ8vNROAvayK7PgvTm7XWPnAebLL7QEoaCquUgh5PPVGKGRRd8iQ2vxIj39eWNdciST9hU3ogIm_RzOtsrbVnlK6UuNAF-gSerpXcfIAfmkE53uEkWVHLMKRGnhaox8pQ8xrGpPO5qqURIdid47jT1kR90DBmNJGcWdQtfbwWVuVVpdmYwmqhabxRteVCd6EEJmsQRQDpU2GALAFBcHKxULwz-42jE-NSts5eIR27LYWo1SYok-n7rUmCEgDGS0ecRWLsfUihtc0NIlj1_Vu5rpQija3ImDl1oWouScS3CfiAsXfJMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LW6dugnJCCp39StKD0Z40Pml2KozrDlXjK5XihAtIOT1AVPbdr-Hsh1thvGZ1XygZcY5nKPb6zbYGoPNuNm9jEf8rx2bDDqMdR8TxYl0f-cqBsbsqS3KRf11qRaoseZFnJj-_1D-vehCs7mH9LXGnTvytqSP5HMhmdt6MHTwW7I2N4GnANiAlPu3bUJs1AdtHTemrWqjsibdfErH1I6rDCFxfdttKN6Q5Xo8VY4lR4yw7segtOWTs4OIPgWNz61ITx-4ErLdrhw7sRNo3pk9kCbfzUQgGSjH6jo2-ob9HmH_UeRlkXwjHP_qXuubyMGK0fRAD_atmlHIf5TGI3S3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtZKtflxjpNLZMhwbPixpz3XUG4Xlx-ixyT6VaNUvg5pDzmdo4zVwrCAITuK9m6yXUn0802Ob8nlvFjsjXjhnHwx79lcKrX1_x8r5kI_ascf0DYq2l3kUF86n_WODAkhma2aISGd2ZJZQ9NXvL2y6jQVuFyeOp4EA4RiQNxeKVet4Duo52vWvBvgDqhckCdg0Y1RDR2wqcvkyrEy5iYh8J1Wq2RHHafggedLdnjVeUHuL2E9keoBDerROJhoSIUzaTfTDdsz-Q_RMUoi8YYojvCBQH6PgllMkAPfNCsApMy3PHXPd9KbtEyykLk97Qy_qVzZb22D76GaoCNc6tVGZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Fg2WAVU-n2u2tT0vVMdY3T7QkuhJGWd5psLP-0dKhq3N95GGkht7ywHtU4OlIDj1e3wZgGHSQ1fzCWLsrRdRMgJKwaCBmXEQZapyRp72TGvSczKTLwxJVJybMylp65nWWdpfM_l9NCwE-6f8y3zxokRBlY7kd35z0dCKSCMCVKkyiRr5wHsXNR842TOYp2wa4ETL75ShBKcqcX67tiYSYaHizgO0whP1iGAOEF_RtYmgFL3HAu1zQiyST3MUGipzf9ux-PeXiEU91gGMAnyD0UrWCCl7jltPF3ZcdqhJROFrA2xNoklpSX8l1DTVZtG-CSx45LQFrrn-pTG48J7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=d7Ydxo1aBAineqny2BuAVTHZQN6L3td1sOqlC0ctrINbJ9KeXELBmrHHukGwuiXcbs281GKkj5KGvoQbAv_n0ZlGKqioHTvHGMpo5XNm6urE6jTCGEcQUGLheSNJu5zf0BaFqs-BUhOeX2H3E2ZB_KDANw063k0gmKLtUHIGg8PKHwyuKFVoq3JBFqB0aPeCRPE_ao39EHRIuDJ_QSB20Gm9JPMCwqN7NPX97T_nHXPiFOpSlrjcYiU6VULzok3UnO4hx89Xl2JCWboEryDooUwVoZux8fZVU7_JnD0PN3tj8ONnF99-qPX74d1qhTJw6HBSQlMsWi9mJ_IOHcfHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=d7Ydxo1aBAineqny2BuAVTHZQN6L3td1sOqlC0ctrINbJ9KeXELBmrHHukGwuiXcbs281GKkj5KGvoQbAv_n0ZlGKqioHTvHGMpo5XNm6urE6jTCGEcQUGLheSNJu5zf0BaFqs-BUhOeX2H3E2ZB_KDANw063k0gmKLtUHIGg8PKHwyuKFVoq3JBFqB0aPeCRPE_ao39EHRIuDJ_QSB20Gm9JPMCwqN7NPX97T_nHXPiFOpSlrjcYiU6VULzok3UnO4hx89Xl2JCWboEryDooUwVoZux8fZVU7_JnD0PN3tj8ONnF99-qPX74d1qhTJw6HBSQlMsWi9mJ_IOHcfHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OihhX8yz9lewJVUXrBm6ZOv2qLWzNgInsKUEPlPqGtKvVIVbVtL6jPWJk5BwlPRX4D4SJM7WDzsu8I2F_xJiqYvybIu8aa1PhdJOubX8BAoLxIatI393q8iWgLwXN1YRaNcgL61IWxfT8H9qGJTTxKFr_X0Q7Vk-fUdztaRMtd5yMUNMDSfCQkB-Hq7OWJi69RpcxFSLUdgPvzdvDDnQlyF9UQ1I_iT093OdctFy43SQBrB7QlLvegPrSNBxWcz4kDkazR2QJ--cukE0Q_SmMZA-Ox-xX4Y4mmogg5Xzm01rlZZoqe6H3VpHrU6Agaz-Lg5XJySq_OAg1wSu01Mdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htO5Zf2xdRJSuaiIBioIO-kWJaYzxMrYUQEgShRqI3Tm5vS6FdH14T1P6DQ4UPqKqeirrlWesZIqSOj4dlsiuOqxfbygMZ0uo_wgIqxsoqt6mmc4u7AUWYMVKMocMFcts8qhaF5JSc9JrbDXfOvcQZSQSxPAC_hFvRSM4LrbLeTP2zmt5CvPh6Ij6AuH2o_G8PJoNbSHj-A5-wMYcKt4LwhhHvfS2BwhDsq4MuB5hBkD5aP3rV8jjk4ix68y-GlufOU1XC1XVzvhkSv9tPf8Zr50HZK62By49szMWuab3RL4l7nGC3jUByLul49PaFTVt6x_5AvmgN-D86zIPpIH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
