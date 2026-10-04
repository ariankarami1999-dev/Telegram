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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
<hr>

<div class="tg-post" id="msg-7982">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 860 · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8m0JWbOhctAf_HMNC5D31kv4qcebW6_-UHWkGTCUgW24OAxegon8jWm0npAc2DG_RHiMsR6ct2D7jiQqrG1njjwZydYXAB4sAHh17u68zouU_UpNYC_xO0Vr1uL0MOZLahthOcU-UnmfObJT0oxxnAKhxIqSb4u2zvU61jcRyKTE--iHf8ZOORMZ-pJX-WylSR3fed3XI-GuDvSIN6T0DydsrU5wIHhxush2I3JkT7W2Yc1YWSwwIMAHQcuR70oZi5KcyIwdeIEYxEiBJg-txg5urObKvADeJ2gEXQrdPiZu3YmifbcxHgaWvjXF0PV5XeJ3gUvlJ2rneOStt7YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiIt1vKvgfncPe-P1NNBRdz7KH-yD9ej3Z2AG67IKf09WsK_DW1XwG-GH_EGOJjjZoyoL-YublZVNyCY6Vyz08LZWAiNeN8ldtCBSViiWa8PL3hVZ8nf-rfT-CxekzrUyOhSgEfSB6IbdQS3w7hL056HkEaf3OpZKSD3an77YhdlbjO7xw_kBH2_4dM5fdebOLw0KwkPUBDtIdIVC_KRX_vFH_K8RzQrCvInMxi1Nh1DGandQ07OLhHRdn7ZSi-AZkW2TJ2ki7_Zw5DIa2Ikc1v18FkeQ4B2EjE5yooBKgyrW76GoidUk0zJwsMeDtxdscLW0QA-PF6uT5HgWZIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f63bxLfZ5uE8rT6IY4xOYSLiqdXB4TMn3v7i-rpt3anA_H59ebFDf-YLZxeYf5M-LIdP8xfI8SYmGVwHjCVAQ9griX0Li8aMNQYFN48Fyta9Eiq4ffhWvX004eckdVi_PibWlMwBrvGzXGWg318UIqs5Ca8rjwRjwRIfp4tyPSpW5V6llVlTKCpSbbn_80TrvrOJUayxSJVq6Yb13aKa3aiQWuF6NciocbNeQHJxRWGM6_-hC6RyQAovvBnQPqZ7Bs3uDQiDcflkUrPgWo2usizRYQhhwOu7f3wsNpeV-9KbaJOpxCuAKtrDu2AUOqXF6MyQg8XZHcIj8UoeeeCG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBytDFWkqzJt-ANNdkTMMktjc6BHo20C_a2i_IlSxCarbMcW1qB1GqAT7Rqqqjq6UkP8Mi3szBKAn3QNTt3lbhq-4TrvVNHYKKhOS2uCtf_JnS_I2aXO-OeWYrcw0NcggSErouw6l2QJCd1nKg3WEcqO7Cs5LHiWV2ls8D70kiuKnntwodgvolim_tF5m0qpwM6ORw0OcwjvqwI8r9q7IPOO4H2IqVLIA9VAx5-14wU4Jla87bWZ66mqXhG1PY5CmA_9yr-dHEw7jlAHuAJ_YEmz9_sJV_qqEBXVevUH-hz-Vlu13VW1kZiZnmePuOVmGIEmlqtcAqVhd9Nw41Y86w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F30bISSvKTACBsLXQuope2JOUfWa8TMnVELHwPCpKM73g0TBsC4PHT3XK2t-h0velMf78oeAj7aHHFsF6GGlVFy-YfmlsF-giBh_ItaCLTYqYceTQmEWxQh4iL3r0tHIOVXjMS968i9Npg8ZfFQGSi5ROo1FNgOLC8cQviwDOqyGbfQ7zCHpI-O57VBQ0KAVVGLcPtMu3c5tx4f8GrMSO8ckChRZ6NqQkmkF6gtiY5oGtpFPG5EzuRYLZbVfwcrgYoKRzHaVujrlt7A11f7a2P4Fiw3v9v4aq9qNfC8Cpo5pjN0Lsb93oJv0oSOggaWT4r36WG4hv2BlT2_OWUPhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPdzLJfrf9yIJNXbrjHLKsx_cvBNCxNDTDqGG8lz_tIFC5T0O7QfSo2uOOV0kEx1SZUhAfu8Ty0a4jcTpBwCdp1PpWrH7iwf-GKwDxIruuNIhK33a1zrHqF8nacyx6GDqYjSIasaAqAalLe2xtFTsY9jmVDqiUERvSnNkIE9E4_4fsLA3q3ZK4aR-tztnWrb45sv8a_-mEY28b7SN2LhENWozG6WQ79seyctRArr5bknSoZx7Yr8sXwBRVL-zqRLX0Aw5VCjSpJUC_N6mSM8m25b-WJCmKq3Gstdpaoo3Dx2RxIoM5bj3xfXUWG8OaZZl1DAtOZxhFRgygoQQeTxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PG9eq7TM6sc0nP0rKIjVFSwz1sQEC_pQpxRVp-h2Qd9xbOilA4fVRolX0hKxe05QD2eI7z4pTLnwsfd13Mqag8SMRKYAO1fQH8C3-I488rxXgGDg_BTVR2yvhme8yJnCsYP8vOqhA5AnUkbw5Hs_HGOfSyqkBnMSF8yOlzB1XBeyI0LFhZGQ7xoLsYsyuGRcKK10PU2Jyn7QAeclhjXO_JNq4jOezj3IH0HcLzR2I6R6_B3HXDGh4-NcYCdsQ_S55Pmy21CFBe_rE9XjYv1ByzhHcOewDEOAFdfGQKDY6Z4gDZKxdEr4ZvcvhH-iR1ezS6CzlC2AOjvmWp3zsAvrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4LQ_A8motggM-ILkDzW-QXh5wbMPtbrb-NVadyV7kxXtoSDwXQ_ocg8wJzQBE8AmbKTI93IbSoj9uJsX-R1ntx-EAX6vmY_ktz3PALxRB59wnHb5XNSIPlAKmu2c47-acZ4VJUcuM_Ld6Wx4lDERketulNUz5l5uL5ATZrxbjYraW_hi6ZdTl9EsGI19bPgxYOsZR0T68qS6UeHjfF-hR23-uX2aCQwevR1NKGmM5rboOYyEkHBc0_0a9u8NYdxOcPBSiIeRJGIH5eBNZ3_pEn0jNvkYPkdPG5kAMGEzfvtidq3J4Ecz4BUV76q2W6HFuJQu5DQl6wAwhNGoRnSMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1MvtjasllORk9sQGVumArmyFl0lbWwjNDwVjvCXE3hY7dpuw9Ks-JtiKDj3Oz1IuwCbXWJfJird1juSgg5_UEeMs4MgW1UflKbzZgGzCuatgM-K56kjiPlCf1Jf2AvXuh2Em63EygC8xEVGOMKVnQh8LretNuOsNnNLROPE0HsaU5CSceJW-OiS8pn1_b4bpuaz1ZewAxbfqpr2-DXdO-zeNy0SgQMJoUjk1ezzdhsxaaXuy5HUnHWQnJHZz0o09WiCLzcYd15MaZiytBm2PCb7n5M2b-Fy67-378WNWacGDVhjEpeh3xNt6dYwolHxcMs5eCCZrmNliR6ake6uOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4BeCeoIUFZvfPhzYTq8rkzQi7nPEuOvNvfy1-6DZU5I5zGMCWa0QmcE_LZM72PTo75kjypdm0c10FWMmbBlJDzzCDs8i6UPmCa6OkQWbTUHdeqGmDl05aku44W4hur4Pk3Eio4oHf97R8vvg45j34poAj5dTtf9ekHSgxtKZudKMcTa1g2hsa06lgQdjt6HCKritSGD0oR-4m_eCGto2mXJN4CcTvk7CpLxfUEpiOujUOEDiyCkETtGpxxCkBQUSOBuPF98ISrsRw7SbVA3YSL8MKmykuptbRaGamHysSa51jfXylGd7tp9TwAwdwGM5cUoNBkyc4fT88K13xpETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNZFiwZL08lxOrbKuXEUlvoETNnnxxnIgWPE-y6WUzRk_pwIX8GzSmdgTM08CZMwbzd8I782o54bpuulhyp__JOax91YirhmGtBpPdgnxqXov89fEQ282b3YDs6nnzD4yTCTfwO0wYlnaIam_z_fEkPq1K0WqLbxaSwk7OZPFjb__GEGcToew96HBQ0bxehyebEAWTlX63oaaG3vi2ISIV7mmZgy1c1u-Z2m96dFB2mGWOFLkhjH8-5i8e0xTqkTD-JRoIhF4Qc6YbCuFfbab0-z5-7-OJRhMFEEMVdU6HoY0t-a2U1oOusmDZz_2tq2fVVyhH9svSsS__JkveutLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAB0PlfxUNOb_odazAXm91Xe1LYzGMuyh0BBZAaHthdGk23TgJXD_d4VPqZZ7irTDGRn_B4tB3qaKyf0ggvdEL5R3qZH7pTOE_AtS_Q_r9cS2AkjWt3b3ub5fgv5-rhnSbhlh7oBiRELpKf74EV6Z8XuLA1Z6RKibXj_0R6ShQ_JZOxCri7tK8oCUYMRxxeUsrzD0KyjBiSjoJnX_hVv4yQ07z5VMo6IkKgI6EABckOonI4Opd7vKF8tjqydX_D5hyoatocDXOCyCuhsxDE0-cn3LExNat8U04B-oZFy8aeLvtT71wlUa5G6IAUQnfi28EST_puBkgxif6Ow1QiSSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qL1WZkAtvNHBlI9UA5EdbHrkm8PumpkcfIyVKHhrYO0heMJl9kJjr715Zjr06IUO81JWny21Z9V7xc1tfnYJVwfuiGk-YJWjvpj6g9PNlSaTVNOPn9qbD9lio1MsV6Nmea5NH_0afT0PKi8_CIrillfm7KE0Y8D7Hy5duKFKxrp9rkDjZv_H8lbLfQfJ4ofszJK6-CTPxXGkykK6E-FOXX22I063mU9B45vh-6v9REzsOw0UX1H3CY_m8_UqXWVGgz6jcpPfFp3WU8xEhWcEJ6Yn7oXcVRfQZrb6zS-tuIpKCLqz2KV6wxiz-5Nc_bqQfckzTXq1w9BCLbKdXE71gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LINkbfGRvV6iTvVdgb3d-S4wwwncq-xX7hXqKTCJExQCJXAUXBSooQROg8RE1PHNmB1tqq84lKmltiFFJTOWq-mY3ADuIFWygWxck0dTN1qjkVMdbrJWFfagqsCzyzfEIOCXYbcYl4gXSLC-NhuK6mA2zLRNaRxbqN6lqciU1YRwNzN5dMP0V88ZklI4RuRD_NL9LM3ZacYr82xD4XUj2ZygumRzK_phow3Fa3OO20RwYYeui_EIST1psaH37WW3OO0CrR6zd5v6YoxNC8ohkOty47V0IURM2-QaGvwhewib4N6jdzb3E7iXICiWe69ydwCGeWdTwv6q3Qfu32teVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QK5erk15b7ZqoXw0DJ5m_oZV3iCmooANohbi3TpHuSNaLai-9Ybahyv--5p3xb3zJVv6v_GDs3tklyhttEoSE4KLXkB50BOory1IIbfQKclv1dpb6OvEMtCPSINPAOVAlyiJg3AWnu2CEEHDxjzf49XOKb1hy2K2ekoQ4nfkshERRdn9a8i-3xzcu9SwrJDLQai9lTKLgUhyiB9cpTbFcp28Y7Ga4Nfe1NHpG-H9v3bKVtEyH1nkH2QpjIsCJyWto_29d1NTkvPsOKLUhNqCW_GWXCmJEpswWA4a4hLkFzVki-NQlWJzQNDapz3kp6n1JPAFW5EllJ2Qg4JQxfSBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAfGq79abhmzpX2t4h7ABmx5sZkqcDpqGWD_uwoan9llNXpcSrjBiI8UsjCfLaPsw0XIlpN9cGEyI7-SzdVgPI3XR0AGdym-Rc7ccrHa40vFd8cW8ydw2utDmJv3plV8Sj0NWxv_qIg4tOEyXfudH1RObPhcvfTbDBUxIkXNBeAxMu1ETg8Trqs85EbW0W6EyuTOBPEKDlYx23sqI_gGaoVLlhyTZK6QMuIpSiNzHd6aTQBg-rCBhzxi8HCXqGZn_6wHuLjAC8WzIP5J5uSNy-JsrqlUUgUi1-vkIHsxwlx6_ujUXYWR1fwRx69maCBANT7KaDqGCz2kSfleO0XmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiE1Fi_yESTMnYmN-P-N86yjdKKc-28gi6giGLI1BEqX_rd2rHU06nmWh5tjNTpdUAt-YYbJNx1ujEBDcB0OK2wSF3PMZ4PoxaJC2-m9usD28gUkGgtuQJ-o29pEczlGG_ztkyiixJ11ow_0RDpbblIT-hLEv440FFiQ-wBcH2ZznJVnOIrtoSHVGyi63mkrdvXZNsKorWT6CjWo-Zmx46jqolhaa9cyjYhH8QtxfS5cG3ghVh2MO8Aes7d_xvhQrYnJqhSZhPKL_0EaZmCSw8w1Rpvguax3Pomce8J8k5FUn4a1AvqWBmc90WhVzJTqU3tSIediRfK2dlQfmz5UVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhC-F6lrIZC9VGjqj9DfoLeEz3I6pjIa4PVn8y5mkVn4q39M0GYm--gpN5eNj7JaX1a3mX9ChguLt9sW9fb030UHiNLttOCY9I2K7JMzsdu-MRSgasPayx0C3flwA5RSrWUxTRtZpTDO0I8L2fhe3h_pN6ELQmExu3ihLnzF-uKBj3QHehoE6pgHU7mS0NGqavQ0gGV80PQ68n3bODfuAonDW6f0CEQWufS64LxwKoPnPPRt8P4GqSgNkbkhMVPvKtSPGs-R2e5pAwLdBYrLFknzYNTLGvoHo91UrgPPg3OXYrCL8cNDI_4TEIs_fO1acok1cfscGGcMeLH_gWJIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6Aa43mDBrGIFk73N-tnUPWUK22juOJ71K9yK78a5Is9x2WrB02qnyfm_HeZgcHo-HEXlyri-kfeNVVExv0FPatJCK4kRwA0s1yPN67040TAbVaIIYuvKOJC8biHK2iWdh6HJhRbo5i6yycIAZDJqa85ctZskz6Snk5R9_ohL4GO8BSnwN3H4Acu42fn__FNok8_P4f-Ti6tpUyXJ0Rj-Rb3hFO4PJkSqaQTuntV9NtoCFyqLiGg1ZQMAXgi6V8OdysXpkyBA830IwM6LTT5lmjcE2WZ04QiYBfhZra2r_B9aPvyPpjEO6VlbHIs3kOrwbsPVPCP9gx3diIYMnwuhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcyk_UYE7P2iXqqQ12qND1qI5tgfhhNl8ZHuaxzq9KVQmpij7E2QxGVxLR7Yo4ROMihR3eDP8dpzcUwdB8g7I2BJBpQTligdN6Jt22G70VUjVhIdKdohSMJ3nS7TM5Di8jp-OIgXhUrwbnaeye108DOYH7VNndxjyRb3q669PnUSQL4gzyh3OoB6WLjdyry2y36fE8X3-KuNPXFDwUtZISUYJ5vjokv956cN43qJf-ne-d-Psxqc-Iqm9Hrg1vOuFKClzHuz7xJnPrj9ed5dsoXMFVlhw7ochKcOqlp9XNMcn44uvHYlo2r8hzRpofcsTM0k9oUrz4Au0CUTN4b-lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYc3Ac_Fi261M5aVFXuW2i5wYqGhUsJswK4w2Tp6Nue35zTUE5ACmELO_4w62tIS3bDY2PBZinxd1e04dx85MK0IOXwSztJQaxeqDbKyFBc3t5hwe7Caw8kbXdXtye5S2vOZmWOwmtvRebrHDlroK-EWGLIkKv4b2XSwGixDdNrmCOgP-y-6InGAfMLa1eGt4tt9nicMmR_3P2Du8NLQ1NmGgihFVdwMEVItuC5jB8_2H_Y0nHDdmI8eQNd2aG7hPvSamnd2YfAJxb6eCzE3PvyV7_ZIV8sjdZpQvfbBp6na1qAevZCbSqGSoqWEt8mPx3g5IU-8RUDPswobcP2h4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-GnxJvDsi2m64OXCOmJDZIrelSd8z8aseTHYEyWhfoHaEnAnodrk0P1DMX3OTiMeXIJXzXYrZ1hcc7V03HUskjt4XtDmAF8cY_A7Yatv1HGBS4Rvhg6amSPPTI8NBTAw4fVarU6uGA2Vb58WaIhqK7TTKlubFsEnSASGJOujXGh_A9vjScIju_Ufh4arfJNuxlVBqS33NsxbXaSSSIy36p2SwexkPJuV-0rRPDyTQ1HUBU_iFmSG_Tp47lUX9d5SJhPym7NsuJSZHCVmZNBM2OPW7ZYQtBwNEdf5JaNvNxNhjxImOQxash5CieLCU3Pu2yHygFFDIyaXSrpLfO2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KH-NRxU8Npwxxbuds7n3Z_fFKdErJDs-jewXnn-B8dplBQZzXzqroN8BeRwZ_aBhetfzP_binIodd2U6wSU5xF33r5LxJr2as2lFr7pZQkrjtYNuqxGh555bnSeU0IMYuhAwltCNJM8p1DRX5zQltOw-YqHL09iCL32Hk38yJagCBEDNSW0Tjq9IOxUiqNEivC0wOcfdODMvW9u-4bXer4sWPQLf6VYoY0F1N2eWqTLACXtTtR5zOw2SDYI-GOHNFzOE4e6359ymE11AANoyISAbt_PITp05bn1PmA4G2IwI7XC-7k_XgOtN2p2vNJeT7LSAzfqK3xTyiKTvE7pTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDOWvgc1Vmxb27qRuDpaTRprdbNZkWW8LzAiTFSIwRX8x6ODjdQwG4y_KvQOHl2LBOIgKusm_0q5tDIPTXxlSl4Xetp1y0YJ9robJRoOLIYdDRfA14DLnZLOe2fCRO3BA4nvxmsWpE4chVAzg89_l61q_xGPNfV6i9Hx7t4KL74MjenHDkMYgm4qQ_5VawOEKIv-SCmsEn6EzeLw6xYDDl97dfNPdcU2wPyvnhmbyBV0S-UjHcp-x88Nrh5SQQsnfuzCYk-kREZ7gNxoCJtOg5qS_iMSjQbaaBRym0fBZErW_Olj-nyb-5kEhVFxJ3Ag6MZYNJkCTT45r2sceb_j2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0NdeSbqouMJ1jcN2EqZzYTUroB7WD-BBVdAHTCIlCVDU2ywjldpHwQKkvTzHMesrAKx1Wjgj3NgewBqhtgZ22eEoWR2Jou8QflzuwXJv_l1VqDqAG2zKC6GT20AjGJgAMdG51E-BjSRi-xdNnL6M0emdhhvBtrNYXTLBzG4xZYRo0wVO_TFIyVlHb7UqJx5XiKZ6sJVKkh6feGlAIhFMTnPOKgCYzxRJCVwaDNSmnWg57iBWG8M8ZidTu9cSFFztnSNwuIOkRnKFS-22yQMybgVWU09BNuWWnQKqQljjo1ndqE_mH_5Z72eZK476BmQ-8YTjbME_lAsKgp_QozH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRFQgSU3WK93_9p1l46i77LXENVRN64jYYhziw1wh4zZABfHXQRKDZugVltBqCU0YB0T6OPBV_BNsDdBYKnQDiUHmIK5Pr0l0csRKe4ktIx93VSLs8U-JdN9ohEVZVww87Hpg1QIEhESCWg0cnxOfFf7k52xg_r1RPF2O9lPj7oi6Sl9OsWsIigR3GMRk6x6bOMvlIK7tk0ZvwVPR9YFdC4FtVCDLWB0gNXcPyh7_IPLJH97fPWv1taRhJAAdZRnS2VUsaHSzGMEskrgS-VPNSLVPJK_0qDzU6P7s_ujUmUYwHHhsfkEXkEBIurutDDnBaV2BfdTBBPOQRFSAuvQTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwKz-S-Avyxvc81kA4RU4wigRvTmo8MLKwGrVoAYfOg9STNiEQPPtqDzRcXEosLY3EBnKdDrdanQWW2_9za-jKAr1pYhBQF3J6QG6pW5QRYji4do3-gIJsSD8dm28uiiLw2tzvy4fKf5oIEu6PMGCpYPhwLTL4peCz3zVzNrtb-jOT62e2iUWCGziadjV8jpk_3a6-96hSWmg1xg-WjHr4FCc0fFHMAdSNp1VisWDlRciQD539hSN1WYFvne-pIU3elWGFwmx_4vCUABx0ueDGPqqc71MA0ZgJMWOec8fbeI5YvuKnfwjryIph730V7kmG7UlbQIDZUIJJ-6DdPoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-uPfl8c-_O5bJ0X6NHn-DGxV9IftvZ_vLygodhfh1zm8ENcQuaVbAOB4Zz4PaHfFvGKA8IA1xJK45kNgFvtHgvPw24caTkjRAwGeUXIF2238csi3MC8jZjHhg86UplgtuEqTvjmFTA1Oglc06RmvK7YRvOk43rIxGnndw7BV81yUyrFrVB1sc6C5V-_VV_4Vq7Ubkw5_M03kt9Ov0eHR4qHbANTd4qwoLqj868WKIPvfPqfh7SaZ-eGk_9U7ZsP72jbTplfwh8P1lm-3yv6uniPBGI6xxMBFWGkFPEE7LmZbDnciB7EySPp87-MRoTXST5dsaAtNNaSyxkhaPskOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfAVh_tgZwP-x8im4OJXwaXSJvjJFi99Zx01khfFro7e9fxT0SjgPEOcGAO9VQid1QwW39HAEtLs1etH2MYx06f2fGe_JubDfuKet14J38n_djsVrBJ20oXcIzgqo_8hiJGV-WEz7kAfIFoGRBHeVOxIO-1M-dMRNqAyFzI_Dy2KY_L8a0oaLPvajgf11PwGzah06fJIrD3Ny8pxbbiUXsD7oGQUl__Skyzp-S82e-YiEIgtXiWR2lNjoysbwCXEXV_0LMOdxFFeK6x_K7xzjAVqYII0gQ7AbXtukuhzYbbpkzStXQJkuW-EkhEoU8oSwNhoU0jo6MVqFEUn25VsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js3M-SxrW_EUdI2PffBck1TqYz0nJxZK73ddXGsINTJ-NxFFQz1IRflct9at04PeWSQp8K6w1hv4EEhRqPFSrIS46OEg7_WxfsM_W5DpjXiGDLrlYhg9ibIa5aIPvdrKR9QRTIoKw-9KZMgm7wxFFvufQ9zxzK_ozifZcJeDrNQgaR1XTyBeueSdUz4iyoaDTEaS9cknpnsN1cePKA688snTYXO6tDJLC-vWZ-SL1i1vKkx5hqLKpg6ggYTkc6beshjUFFinqmC3Gld7QE-Y_CPQQDxaUjmmA1HJps9IZu0-pl2ZjRznpVoXUlOhLc07VY3c3s02RW392BoHwP6yig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_PljYO9mpZgCFqX5E-03rqaykeMmZ7ieq-0hdYQhA0Os0VBxNr3TNdvWV5p5DxwWnUqyfMF-zlv_im4RR5guGRNKiTVO64lc-zioXkgWXVktgb11_s93LNjZGjViIjbny2gQ4MFKDdtt-z6bxdcDbsL6q08YOJ9V1_Z3egSivh8yMw3Tt1UQDJcThcs4wRcjValgN24mY_0UJPMhWI--zDHfEIOozo_W-UkIfivtwpzjPPi5xQUnTpAODS6poeBZhLjmwjC8VBIxA-JmaH1UhtMcig4PsN061vmIHE7hFR_MNN1qIUb2cBODc4hPfJ6DuQDgS0C6nwXqwTPldVuTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=nhaM_NMavg8qEnVa_FTud8-oRN_FYkgYBuuLhPzfcJuq4DRxZxk3NzFHkLGyAsqHrQBsyZ8nx1_fOlGC-1-vAwKAgzGUU_9FPb--URzno3JP5Vj2U5TYAuYMfa6TRVskIrAIY_p3REKCl-MaKTl0eDXwjeUXCuynYj8WtATNpoHszafSN1DDhS0gHshBuKCSg5taWZ8yqZSmJEQtrqXhla9cZc5PncPrtMn24OhK1tzPdD45HFui5V07x2OkFMVbJuzYOtZ-qu20lY5VgrXucw5-u4_viJQVqfkOnZ_LnmaKk9k40UaJyCi82iqqVvzUOTlhzzWiNcDeVB4sIhWi4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=nhaM_NMavg8qEnVa_FTud8-oRN_FYkgYBuuLhPzfcJuq4DRxZxk3NzFHkLGyAsqHrQBsyZ8nx1_fOlGC-1-vAwKAgzGUU_9FPb--URzno3JP5Vj2U5TYAuYMfa6TRVskIrAIY_p3REKCl-MaKTl0eDXwjeUXCuynYj8WtATNpoHszafSN1DDhS0gHshBuKCSg5taWZ8yqZSmJEQtrqXhla9cZc5PncPrtMn24OhK1tzPdD45HFui5V07x2OkFMVbJuzYOtZ-qu20lY5VgrXucw5-u4_viJQVqfkOnZ_LnmaKk9k40UaJyCi82iqqVvzUOTlhzzWiNcDeVB4sIhWi4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nItd70gABmHerJR1erFtmF09MF_yyyZjaCedu1k6ZAI_Oxr-yA2-o5ypf57taCYlVs2sGq7AbgSws2sQkW8Ql_n1C9PdAAdSw7K9BHnFL3xXBFU-773EQxb47iuMD9eXp2cFgI_quniuVqxdnK_-z3vnKJTF1bBUQLmHvUKuvnSkfGDquVFR9wtwnpMKpyM8_19Vnml9xTDuiC7YCTmXm0KEF2yAua0dJQ6xvbCvITqXQ9NPU7Y432Cm51RHvA1XvfJhmXBjlN_MvKNcjBjMAW0UynLmSVFPXoc8kMmzzcK71N7hUAGluN69dXyOeSL-Xr0wsH7VzLoRhlWRDgE0nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA_WvDg2ty0wLduIw-qf81wUDdhQTvCW9fAuZfBnN5c5grMqOphPi3TFJ5tDfQCqjzVRH5W_lIGtJUWU8lk1rkqRWmEPHHtZSLMxfkWqwdKGwnTduMMJRfzQOF1dEW1KuerV5zzvsbsIwQB-Gens6oLyD8UNpLoql0uTLb96sRhul_z4_jTzauCk_YcL-sD2CMyGjspGgeILKS7EiGiF6wyQZ_fYnkgRpOEBB-CP_CJgG2czm5DitJz2TubbkrggkxsHNv7_c0IvcFQEpyPdU4WfXyTxk0lan5Yb-pKaaSistM259OX-diHcWTn_0nG_1NmT9i80qx4PbL67WxmrRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKWeSObWPvVqIYjaidHKrFx6WVmn45qFURjlaFko0qb_hYNwHfGi3pCpNV2u0dZ5x627-c4ggAy2a0WcU451von7stzXGAy2dQ73A_iUz_kPcKoBuvcKACb6QowraLPxkyDJq4B_zA7uo99QaRrEHLC2ZchXSkrG2zR1gLjITUqIsqo-f_ATEziUPdIVJKcudgOaJTEjWuh5GDaiJxGJXym5N9wzrYtyZQzQUB6OGH4Ss9W8fMIrqmdWlVWLG_sTp3s0HD4JbQ65otMIHbVlIEwtdcg-rMwaSZpEMiqHcLsIpAUis6vMnfkSjj7TIfvssu8ACcrV1p2csLeXvZJy8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbT1qbgbYNRFh9nWKGDR71YDyX4cbRfSP9IwuLmEAvZ8_Ab7BDzVv_XefKrt8MWUKbPj_XL_RdbYi7_b2-XOBw9z6GOLYXgT07U6BroskQJmo-XBBIbkao-TtP6dy3DS7k8OEk5x6w_ff9xQp1_i_1tOjYhZH-WP4FX8JaIqqVqzl5tUtCs-qhYh9y62cb-0SPBExaMW22i44mlv2whDWybNXdkZhqvlSl8N9uU1z5Jiky9srr-lAH6MJ_rFckkTsWf4I2Qm0XCQHVf6iw0XHLkSwWmDUON0BoejuOjrHbpe5AclOUQO1Oyglu2FwsFXSYZAAQIWgyOsWTbJiBYEDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOoryYBDosi7hpvX_zpXvdsfKpZK3wjq66hh2MriORGTyJOE6zOBxfgaFT3sTChpgkSrQFRcoz_9lXcfrCAfHm5lZRTTAxsMVvRT0Ids5I5jbax_au803u3nGn3VGRoGSRhnCdkzfaqxFv9WTaeUnUHH4Ua3HZ59mxCEyuYyxeYGkdYP-nBjp7H3NCkiNMNWV_dM8_pemM9sjX04JYlFB9CYiIgCdCSjLGqNfIGtmLcKghcLCRKnNig42MWENvIsOV2OREzrISBBQ-232cIUO7HvbSCT7HmW3Rpa9jm817z_D76NK7Ai8veA4P2yF_CmicwryZT1w1m0cnsf2zUvGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaGobIIvZtcyZHleFJqIchgB5kkO1w7aAIPbsJ53oYfa-Pl8LnsuEqM1CYsfw1Fie8CGuLcKxWRUzl05Tviqr_eV6WjiGa-Hb1QfMMrkkR0pa1YDMsHxhdHaJRiBXHYUTwadPMsHWVILqoPCgsnMfp9Sc4sRHSWPUGVh8ev4rXJEx3P0DVYm1--yrZ33f_u0b9XWA1z61hYrMo7bemxMNVt43Cl-IVNFImiryIXjSyGC1_3j207Cdzey00rDP52JJbGtDEXSqm8pA2_x4Zg8UnlqnJjPmKAAdMDWgonuWukynC6k0it0K76xo11ie5x6TwKC9cK7qxPF1xa-CrS1_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKMRn9zP5cIz3U4jUZWin30YWunk1Yms5A7ziTWjkqlTACQVeeDEfWF11MJ7lszrgaMIsluO-DGyHSBcSxb1KzkDj8w5cCRyzDbZ06I_cHAzbr64NykcRSndg6ZBcgeXhTncGEt6bDjCesoWNS3Dd0A_UUUmiQyyhvjUb4t4FhxVz4Ij60wBr3av_cBhLNPJn4PoMj30-XZ3V9DfRmBNvqRDcJMK5V5UlGCdZItVwo-wJlB4VL7KuJ5jMakfAv2kaz0g3H_X7abdHjCNCxzDsIdk79hFPQALI_J4vcA9R815isXazUsIFPYCuMPwAXigHLjM_oSyAA2JhONtD6YANw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEKdBG26GD78K9ugXcP--3vSOYzVW9qDQc8oAygPkE49m_W7wb9j3jCBNYLhGlPMSx362CcOlUQb4oHF1nZ4n5qNS8Rvzs637HQHR_Sk_Dx_UafAsFEwYRh5iX0waNouoyBxIaZMtqd2NL30Y7ftAQ9dB1lKst7CJB28PWxqFTZ2kPO7z9y5bHvGYrih7p1qo8xbFmbrgohqM7nLHhpGqR8-ERq_ihJtWGM9wHb8yW3l66s7DsJiyTBYZS5UCrplHZr2F3zwqf2M_iu0YkFmYaR0U5iOanuCiUC2HtZtkryzPd35p9jDCPoCpmMbKiyt3-WjXjvkKKc-DGaSwKC-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uukFdc5xkYe6ucpOwjFb6deHEVkQMTHWqWlXcfK_tU_jep2r-HuS9Y3FcFYX6lmntU2ftJ7XgoPnxYEq9WGODsRmlcIePhUIvVe84RIAFjzedMrtF6r0gqm3BGhDoS-sC1g8UGGyMcizAU5IymDkg1K4Fk3hRjKMuD88Z5VDr4xOZ1rYZO28e9xkXVawj5vcJt_S52Gh3HZzs6ZHwiYDh7_tndnW29KgO6YHs8bX3TUDtpQmMePzO9JBAOp5cx-vP_CcT8-V2LZVwXgxV7m75rK3nvYx0q7q_gkyysxwoMH0MvjW3G_N4JqKJs780x6PHPz2w55KYgASpzW9kKzlMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an1Fa45A4guF7k7BadTnk2VFf16DsXbrjg2I21rMshfuzxtokh4bNy9QJH1dOBlvaBNl7vqMyaI7K8Lnyy6pgqSr4hIFMaFHoNmLJZy537an-wmkzn95m_h__kfqMp54PTrZN1WPhmMLiF0pfgZwZHoSOwFsctT-90JHPYNypRFofp_BXpFFo_sq3G19fw6Z5bxk48KTy-BCeYsk6jAceuYAvmR3IGkBH-pW6vf9W_PeXDKjbaS33_Kq3CFfOHYBPvG7ZPqwV4_kk5pgpkl5yClSLSYzOtaDOKlDWooGW_rPKNfX8a5DLT18nOle4VLs7TYEdANT0nAP_PswwOH5hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI3zF2AvnmpqpDe2Tbh6_29X1afUjZ2gSfW02f_wxcra2-U_A_ncYf6B1Iob-3Bbbd14aGdc_oheMEJKy8y_rQ8fFuVbXNDc1u61_VnEXF66wGbw1VVLPbXP4_vOnibtIWeHnaJ0AhXmdiuzmIHxU_bUNG1iCBPrArmnJoLyBBzjPJ8abf4UeSrbkaGQ9vnbUoEp5pwHAr7rlH-cR1Cbxc_xi89ICK0SHoFekw8NOGPV2Mn4PkqAbQKlnurvr_cP8JEp1nXgMkErXLwBU5k5Dd_grr0MMIz8o1zzCbxgkjEW7X6eSjhmmNQW04QEXXvHo5WI0hk5PRN7BljmPRW-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5afE35CUXmitCKFvhcz9ffRJpyVsUHTxKr0sTvtEGepUrxlwbBJ-yDYDDqY1BdS1hyqYYw3zxCMaJ80_akJEEPIUAt1wHI14H_Elc82BWQqHfcsVaf-TjMBBXo12AzXYpQsEV-DJO4rlsy9wSH3l8YLqlU85Q-8z7ljh3KzjVU1Rd_y-XrqVgxTblhNwdaGHHqcCvRPnrB1NhoG09irrzIwycJv3lCf0qjb7fSKTm8h7ZK_5Qu6lxRVXu1GHOu0LP7_sFRYG0I5xaBnW5cPWgPlB7t-c05xPP_iHONgHTxOCWpvsYZEUsU5TOm3KvEF6NV7ExlVl12qQuSmuvoRkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMsjRWyTYmWE2cK4lqNm9VxxXOxntAZM5zhm6yIpFXR1sZVRL8ZnAovQYZcppHQo6HzZL-kOimxfC_u2dpLmt2M9v-C0_-Ci4cK2cP0XW6jY-tA-ZiM_LVUU2l9o3Fm-VvF14SB-cxFPzgfRfEiDi71x4LTylPNpZV4gfo-WLFJUy8kYomtUFueYgVGSN49dh_hs3gqSJ5D5gdttXhR397hPCYaISNKhx_UMbz6Z0NyO99hi_JePPNC3T6Pios3aBolFz-_irb7kDBeXykf5VmUiwwEsMUHhh5r2LL8gbIdAxySkIdt7oYhr2I5zHnqeH2fBgqLuEY1kE1QRVXDtdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZ8BHKqfVmpOLDGBXfYeRywByfjka5yEiLk2G5UA89vzCUUH1lKixUCv_fgbO8KArHYyznE41CnHO1ClzvrZgt3bEbnhFli3aAI4hEP7JJdvX6fbmMZ_JOJoUlIqg0-8RE1m1gfpufP-8zUNKaZA6LtOVPPviYc1Jds-k0u4mw1YSvaRYO1X086ZmKbYS27eQYQpBprp8ydwgcbH1IQLqkn0hyT4OvVHm947nj05N70tdJ0tc4bokvumzdwNvk3TuKVTJBr4K0ZhrVmSIk16RpxCIfUDhcJhiiKFhEK4s7IjVTyz_AHDaSwIigU477oef6y2szciqMb1Le8wGO8_Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfv0H7ADO-PeEW91Gg4ZNS9WPhKWGxrHg1otTRWEB6nXTey2cO89n1-Dc4Q5GPMOmVU8H0slCozAqcU6uvaEhWVUpw1xYa1Aqsnm70EyHt57fRQEShkZ9YliSfM-4WuAPDCO7EH2N7F1V94SnoBvvv_T7aL1M7c0OwHFPYNbgl2VkqzvgBAQsIbccGtbckt3dgcNh8equq5McnW5yoxTFHTfzsL3wDjfKLej__C5kaFVgXa9QOtzbHwr8kF_az7rM8_jl-78t9tQ8LoV1S3KknJHo2tKfApdF3YS33618LA8tfc1kAMDThpT-AGskwRk3-VjoHf8K21emYice9ZWLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSeoyAfddnknV_T22he8qRO_1uWap89zA9WIyQb1o-DJPJifmGb4YM8Qe0aVr8GIz162pkIqyqZGB1ADrF4Xv4xi8LwN4tss-PsDDL7z-DiLJFr6IXx94U06Fuq2cOtyNo5i4OUtO8WcVzdYlrbrJb9j3yQAMUIKcmq93XD9_kj9wF0RCXtPxKDQG2pskNdJEyjw7eczkfivZas_oqydOOlXut_ZMGamVOUrMxl-mPI3v2ljxpO1jI0yHyDF2OKxw_SdFRJQtBS-WzDkMiFfxcJ3y2rosHYILEAkumvCVDngflWhVqC1UvogBVV7GM0P-OINkRsjFkYZxMDdF4YAvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhsxr7Om2AP6Z_ZScYBR_Y-297nHwgW26_UxKmJZXiiVlygipvbPUXo7liszpCSpBr_1Fc5GzdkVzjZSpRnya9iIy74RM6vXD2-jVGKH9FJIpMAzWElULIKNVPu4GCK38pdTRl5rqFs_7OgA0inXBHDlmzg5K3DLt3sAZwUZFPOEThxjy0h49AVrS-D_-TWwcfhWYgCDp5bnygmM9b5aFOX82oUGlh-4lWhC_NzIoLmNBd_n4-uSdNyj9TNgMxf6w1jVxJK5L1Jr9drjMFoRMgLm7k0bjkMNr1x3wo8vLQ1UYVnwWEtCAxTsa4JJslLJVuz2f2IAXnDaJJeNd6h3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSqr90mfKV39f6XelkCv1yXXxzLZF1SoVpq043QboDHXV38F_Bjwq8nHuxbi51y2X7jTqizfHOlUMvVuPUZP632MsAMrpUiHTNvThPC0PTqEManGdW8VT-VYxcFh9lHijywJsCD6I1KDRARJ6GsqTrfBH1Q_yMrcV2cYsRi0Y9Jv4L6cwz8E7Ed8lLN8ra6ySyjn_gF4a-KUPG8Mw3QT7kWHksENBsvwv2We5okhbPDsDJTmryzld6Y2IWQf0dqswzY4Tfghw92MvzhWmbmda4YEz7pgBY-R9wJ876X-At7CZouZ32dn_EL2pCW3zymfRNAO99jYxeN_oromQk_QXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv4kwFQxnhVvF3e04sqmrdki3Dwm36GkAsgIHELG_sRJew2Ntn8LGyhJ5ViTzQ1GMHHRlJA0TjQ7i26WJBpIU439fVVcWg8rHhk8xOdNrTs84fZpuewtYGn6ldfMMD_2Q8e5I_c63Qw4Dn2DvVo9AszLIfWQolLpsPsDvkmDY56noIqR9IQDs3WoRipmWWffflx7R6zrAUJ5DYfm38iQeiAVWiv6ohA78usghTm1tRPZL-ySgbHiYDzsJh3Ws4HjTiEGpyaf_G5HKlXuZiukKKWVyQXjfFN9JChOjKt2wgKF3jsw0Kjr3EL7EynVjE0Ze__-Fyf__RUc8y81mGLPyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=Hgbld5R9NFipHGKzCK5ZIrzjxVbClzBDq4dH9bUY05HAu47iYJCpR9ZvOCWhCR5YBe21dfMMXdiEJJNX_YsawW5hv42DPzafWrsMMwhRpaBW6ONxdOo5wHWQ1jUIynrHAJxSTV8zraonkEhrqTtq8QWh9KtWj7sv_5A48GDcy9LnSFEWzs1uq295e3928sAHWSisQzHXgWKNrPxIJ01WnlPwCVlvyRjhphi1Q6QQ3EX0WHNfZK_ODCU4n_Wc61RO4u6VPf3-kiMse33PYNAIiT3oIx1XztrdDTKR5OGp478S85lBiCyFIbWa8OrXCAS9uvtHyqwUgKc9_poQbw5vwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=Hgbld5R9NFipHGKzCK5ZIrzjxVbClzBDq4dH9bUY05HAu47iYJCpR9ZvOCWhCR5YBe21dfMMXdiEJJNX_YsawW5hv42DPzafWrsMMwhRpaBW6ONxdOo5wHWQ1jUIynrHAJxSTV8zraonkEhrqTtq8QWh9KtWj7sv_5A48GDcy9LnSFEWzs1uq295e3928sAHWSisQzHXgWKNrPxIJ01WnlPwCVlvyRjhphi1Q6QQ3EX0WHNfZK_ODCU4n_Wc61RO4u6VPf3-kiMse33PYNAIiT3oIx1XztrdDTKR5OGp478S85lBiCyFIbWa8OrXCAS9uvtHyqwUgKc9_poQbw5vwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd-8F_uB_rLeqwSLKg2wE2lYZtbJwnFLNAbE7aKlxJxf2urlnVQf1H6O_4Yl7BmMUaWOoC8MlF_MBXFyp98CceJRkcJK7Pdi_eDD9IXCV_kJqwZwSrCluCqpFRpTqCfKRI5TzvmpPc7OXumQn_ZZ75OHPcGXCuTuMYs4nd_Kp_IOc3ffs3af4yIrhSCHG9iqKdPtM6XiXUJw5EnCmyPd_W4oZ02DpbG8MROM4MX0rRTDshSVEr4FzuIcYJdk1JK76RUC555zIzlteBpetPXYlidf4f7egKMArRo5ojZjZy8Y0wsXM_P21I63CJcncIXTiDjC4-5PQVZLViNIgRFHpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiFkgfEwu-LyD8moKUDmcN20w9Sy_p3e0ZjkRpqDYjLVsiKrTE1SRfx6d6JPZ5US2pXHYSHDZD11Emz9Lk8tr7L-u2sQ1WvLs2ysx6KWWKXffEvsqw1pLQHc54I7F72TgWChkgeOFnb6MDNn60fAgObRhTtgI5slz5VbucWjM0RojQbYV5yiWBbhofYtdypE8wVmxeD0HWj88SNyTtC5IG2Gpm-qXbrzFQU_kWvpWOKiIMu296lPqfwmOGKza_3DiZ6TAoLIo1A6sh4bkgqrFGdJ6wyhE6MV6doX0wagfmKWqRron4mq8wSqEFDRaVslk055y6fIdUlCpUxyF2Z32w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgn6QSURCLBQljNJJ77HM7BvGfUF6yqvvXy8HpO4nAY6d9_AvXXoJS485lF4sw_gWF-vtSnou_RRm9jeKTmxynYTu9Z-4GXI8nljw3jL6BP0PiNb58OpRrL3PduNfeLjGbnJxQ9PF0p81VoXznnvTIh1oWAqnfmvrlCTYPefFmJaPGNzlcfDomVLLwixgVGyVpC60UXqEURF8c6N7Xehzs1oNcc_kvBaHgheU_rgQUZ9j-OqkAm29OGfeYFKIXOibQEvd-3MhxAjHn4SFn_-ZZ5pYMuP5SyHOrWm4hWYQCkhLI0lwnn7lNSp7tncT6sRABqUnkHI-0il74fKBrlvbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=sNKT5htJsdVuNwVvPN-DyzxM0y7PdX1jmn-IFEm_vG9S6T7pN8QNk9XMytE-OCiJ2CYZrXZFDBkQ4owTGRWAgeIiGUx5jrnFbSz68_r0ygX90Ds4AI0yGca_BaN7QVAPx58ZE_NP10Hy75d3eN1siCKF4ScB6Do_ODmxL74h4fkIxvAEy2xMGagBqIv4-oQfGSrPbSqbNZwjPLTXGZWE59q3DXk2-4DBtHAnAM2pALaylIRmIq4p4oTIcaSCrZal1hTJwTrtbHmDfyvTXHwILF5xtrErfbpOeicNNlhn-8Tr23U1w4RJWqhx94vRWN3YTSrwywTL5ssY0jnN_vwOWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=sNKT5htJsdVuNwVvPN-DyzxM0y7PdX1jmn-IFEm_vG9S6T7pN8QNk9XMytE-OCiJ2CYZrXZFDBkQ4owTGRWAgeIiGUx5jrnFbSz68_r0ygX90Ds4AI0yGca_BaN7QVAPx58ZE_NP10Hy75d3eN1siCKF4ScB6Do_ODmxL74h4fkIxvAEy2xMGagBqIv4-oQfGSrPbSqbNZwjPLTXGZWE59q3DXk2-4DBtHAnAM2pALaylIRmIq4p4oTIcaSCrZal1hTJwTrtbHmDfyvTXHwILF5xtrErfbpOeicNNlhn-8Tr23U1w4RJWqhx94vRWN3YTSrwywTL5ssY0jnN_vwOWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hggCilBGiY03RvbdQcasEXKnHOaos7yP3eRNwi0JE3MtW-3ni6xXToD2S4oZIySB1i3Mv30VvTOzpevIHGVOsIw2f0MrP1877PAiw4NQobOknWv-xzSFzq5XnP3OP4-ZqUCilfSAFVJOnFgucw_QAb6mut3FJFkZoMvEVRlTHyKKgJZyRXS5ZokIi6c5zCKaeXDTx81y4NXZ0OVgn9Flu-GQ1BJ_tX-rvaZrAZMGnXYSWkAZ7fCUEjD9y3gXQT0yw2Vlm1HGU8QsuyA5RDTK-mRV9hS4MhrjWZHImOl2cEdIwGgkP8lAIT4Z4kajQl88sYG5JHdvEKx5ty_HZV-HoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfZ8zSQDUe5j5DpNYZBmDXGL3mnngJiiAuM22h0rY4zliFu0RKxmmPSdOWK9TcRH-H5mCWPBefcBup7IXJDb-lZOYePBoerSwi-ObcbuhLV8PTF10fpWvUvV2o-Qv1H8qCw_KIRTgOCIxRdqNieYtNwQdCQ1xENiSfxTHX6yqe0ALjmwRdjrspuIlawJHbxlyFwUgT1fb6mdq3CB9FqXNi_6lBCIWX9-lBXgh_bQzsLPvqAsbBcWuzwP3UrhiHRjMIodLqz9eeeLcwXWL1U3GQPSNKYNlMmX9UOGB7vP4jRNKFhFlAqoEKQIYAaR8_7IXH-ImgtS4WOt1fDP2dXlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5rSb5uWjpbe4HHR3Q3cvXSTq67AVak2K6WLLs3UeSjaDmazfmzC7czOTgLzUuB7nrnM0MrrqyI3M9XodBucLjIUpQFb-c-F59UJWF3ysDud3-plI4AVa86lV6a9nzfM4OnM1CSh7mOZMyM727N_-sWddXnGQnGv_haN5ECiUV0MnjNGot6ApJUDhf0fmw8K8HYhJ85GdSW8P8qzWEXehzdJwRpvUYizxErX1VVMavfunHo0SBI4ZU0Hfl1zwJHnU2hrmPD2RxYd2q2qN5ij42EkVKWDwFdWzhSap5j3rTxelVO2q98-2MhQK0_raFk9VZ2hm-rLO7QXJrfF8kN5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSC_ZpZJaDW7RJFhfRDSw09ipp41PVUQjbIvK1zlAYknoWXEnC90Y42VQlVn3QE9fmEMeItZnGP7b3aHmP-7vFymWOseQalvkiog5C3W8Tqw8yTnVJXRdCMekO2MShMMcWTygZbz5MJgokAAxhamuu-KJclJoZnPIl4g-xB7PchmSQh9LHyL-vLEyzhPfEqZ1YYnCti8Co7_YIqXEv3IVJ4Tb0yBCNPBZI0-J-Yyhi27a0hF3BBf7ZqvpuTaL-xFzPVFUFaF-6DbGpri-SrfJsdNqDTPa642PDqoZQvqzsvfq6jj6lCARIqYCSpp-0vSx4KRhoCJM5kChKK_FUsugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgrtR0yNlAjpd6kpCY778e-pe8d0hakn4bV4FlH5OafMnSJLz6vEZEy0O6nVTuiLEMm79U_VbZufio-UGvLUIWpIEeVk2AkzBAzAYXG8quWUTSBnA8lZaPqPVTrs0Bs7esjs9l-AifhTfwj7PZ-zCfvcyV9L4-jwzf2Yj3nMQBphzpUcW1x4cLJnfYWAwFbVU-hNX4vvaMjFWURzDwVOl7eDEaU8kxVjltWxZkcdIHxB74UFqXlyKRYGsby9itV_n_q6_CwBgHAGgRyBppUs1nfpkgNYqQKDEhQqvNlOdQ0aD09KvKiJsLYH_J2XHA0uNfKUJg5EKdrHW20B2ABbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgM1kdNCq52XkEJlx4pswLoP_3btJA_ggoHv3z8FDRzOwA42EsIQ48KQSkZyPdJA0fbhNFgTgyG3Hv7xDrKm5hmjMJAgrYdnS6kP-OLYVIxDbKlYw5oTkpUSaUklIp44OSasIc83Ovil2E8mpts1CJcbrEsf_fvVgjJG6aDe7WVUDfr-SoxwY-OFvL99B4JNr0VmcgZNfPuzxM_3zzz4BlIm9dS5-mQgXyYiuWIHMQS3V0SVzJPA1tjwJWT6h-qOqnqt8K2H3LbnrJg_Mxb84IpSDrvlLtco390ZrB2NpjT0fj3MnKjbH1iwlq2pIoyOI-gzfuE0meHUWHfLL3xn3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KODsuGxbB29x2TbkC8bf9PXYGLbEYf4JVfyU_JrB0z4WRvLthR2BgAuweDpP1VTcGGmngRGakCvTVbIYymsqIR0mnevxTbq5XkDxuPHP7hpT119Fgo-TnUOQpW-W9VeZATc8URPr9tuqDODWcGLzlqEvO12_Sa-y50w4RjA3QmiU4kBVAR4taIM5c5O3r7Zgo1apgW3z-S07rZRKRSB1hfK-HbpT3BVRc7pJgaK_zvqvSctoCkHMFKfhvZ8FkUiQ9_X8jIeXTZVMu3n7ur4lattrZL2pynLAOH1NvBptqqzy5W0FptXFG8rfV2Q-qQz5GkpbQDLTGjvTSo-QSOj3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=iMs3D9WluSo5jTEzGpr8I6KhOfTPQTZaV_j9ZYweKovk2GKNDq0HjuHxXYA0dJp19g2HvavqsmGtEo5o6OMXEaHy82C4Ea9CDD9YLasZtcKaqsIMfS9f252oFtaqfgZfHRTNLi7Ml9CHjH7g-ao0kgPLS0FwJ1KPksZgDq20eSI_nFeObfCB7peDqcfVpSTUumj8ZlxOD2ApZ4Xm9YbKi_pkVuvOjossW5e5UB8xQn7QQwU_GcP79Py3o1K6HiPKzTEzqNzUcjP7n9VS4sMSJWIVKqI6Y6eDIHdoQ8LSvoHeJcO6VUa8BpUWjvR-_-F7KwGpHvIHsZDAziE5jayJsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=iMs3D9WluSo5jTEzGpr8I6KhOfTPQTZaV_j9ZYweKovk2GKNDq0HjuHxXYA0dJp19g2HvavqsmGtEo5o6OMXEaHy82C4Ea9CDD9YLasZtcKaqsIMfS9f252oFtaqfgZfHRTNLi7Ml9CHjH7g-ao0kgPLS0FwJ1KPksZgDq20eSI_nFeObfCB7peDqcfVpSTUumj8ZlxOD2ApZ4Xm9YbKi_pkVuvOjossW5e5UB8xQn7QQwU_GcP79Py3o1K6HiPKzTEzqNzUcjP7n9VS4sMSJWIVKqI6Y6eDIHdoQ8LSvoHeJcO6VUa8BpUWjvR-_-F7KwGpHvIHsZDAziE5jayJsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUGO0OipVhlGhAVLUyeb6CzFf9EqoymwBTbmyWTjS7RA_SYp1-jxX-QINyZSMuzqVp9BagivHs3hArGh1m8dbcf3HUkWZgehGwC9LR0yyKKv2eVqySXPAvbwJldsnmU-icMr61oDL2AUiVZJL8CrNoXEh5VJGkz2udk_Kg6SLL794kWdHCCC1UMT5686ydsZMQ4OGTeVF7pThTQRdJAl9A3WkusyBovqgmfNYQIjIipxNh7gMpntb7KYrKj2jgtZHtmIh_ZVgFyGUaZn7RtR373KD7KwAv0DuJ_ITuFSOCJXIb5RM0-6yW7CCaooL-iv8Wr99skXGOXNKS5GLdGzvg.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI_7Lr3H44_lQyfk-O74Lpy0HJNROn9XIrVpkB7Cl7wbj---3apntiSHCze3VurcoqO9qD4mV6XUTvMQAa3n91S1mYDysfyT0K7bjeJa1lg4KpF1suE2aXEOmWRiwf-SdBEByltEMZlS6ZzgvWdainEmHdEhN6CkEBRmPImg_VAPVxHJKsM2TwGRhTSQoD38LT5-OvZvbL_S-VWihfHshet7RqqPG99mGeOuo8yz5PT08MLqkc9ko_fwTKSGUeCysCaEwrA8I8MOGX_6uIuAopAYxaFnyu2mJakv0ZcfEkX6I166T3DZtrd9hBSy5LnLEV0_evyiBGo5CifAjIJHTw.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBslGNS1RJmP5S06UFbbIEL8-tCkwW-MtA90EHHAshjw98aIBq-2h3jmxBGay04kCAJtA4Tz3IOwZAbFblzPQqfswKFWEmbgfbi0PdxN-gwo2oMjujeORL_NbDCyNnsARwqdZaMXib7ezzDuEJm2_fJyObtyTfUFm-awNJKi5szBZuudHQCFo4bssjye9KNFjR7flRTskC4D3iKrmCy5xRCBYdAClkWouJRmAVPaZIlu9bUNZDIqHBcWuWKgJImpn-uCZcaGDnPOkZh9kalGpNFJW-sryqBQunJHKFMLbYs9pPe5B3SvLEK878UJLacYfwR03zQ_U3qDrPt6NQL2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
