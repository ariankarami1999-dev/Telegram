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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 526 · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 766 · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 827 · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8m0JWbOhctAf_HMNC5D31kv4qcebW6_-UHWkGTCUgW24OAxegon8jWm0npAc2DG_RHiMsR6ct2D7jiQqrG1njjwZydYXAB4sAHh17u68zouU_UpNYC_xO0Vr1uL0MOZLahthOcU-UnmfObJT0oxxnAKhxIqSb4u2zvU61jcRyKTE--iHf8ZOORMZ-pJX-WylSR3fed3XI-GuDvSIN6T0DydsrU5wIHhxush2I3JkT7W2Yc1YWSwwIMAHQcuR70oZi5KcyIwdeIEYxEiBJg-txg5urObKvADeJ2gEXQrdPiZu3YmifbcxHgaWvjXF0PV5XeJ3gUvlJ2rneOStt7YIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffh7S_Y7j3GacrSHdbuJFgGj4YPwYAZMc7PbMcrkkflvtlpkwi0t6Mn5DBnc5prdrk0BqMTubPOHDuGSItBk3N0KPiWFFTrAegcAAIcvOjDixDWWBJ4opXhiqkpm7jzwAwRWBrT7Szq2_0QVTDFcjgjS4krEBeuSiouwOPap__m2Xn0Jsqr7A0OuOZzMkazB2ziyuBsKEAQvvuVJbrzuh5vomTVNHZDBae17hqreuMabTagC2uGtajCPLainP3vA2b7l9gK2SGqsRFkue1DTciSNPpHm0JYIbfDFa2a62GgeocE-wRKm9TUPrTzEK_57FP1Imhny4gomSTT8nzvPoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiIt1vKvgfncPe-P1NNBRdz7KH-yD9ej3Z2AG67IKf09WsK_DW1XwG-GH_EGOJjjZoyoL-YublZVNyCY6Vyz08LZWAiNeN8ldtCBSViiWa8PL3hVZ8nf-rfT-CxekzrUyOhSgEfSB6IbdQS3w7hL056HkEaf3OpZKSD3an77YhdlbjO7xw_kBH2_4dM5fdebOLw0KwkPUBDtIdIVC_KRX_vFH_K8RzQrCvInMxi1Nh1DGandQ07OLhHRdn7ZSi-AZkW2TJ2ki7_Zw5DIa2Ikc1v18FkeQ4B2EjE5yooBKgyrW76GoidUk0zJwsMeDtxdscLW0QA-PF6uT5HgWZIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnF_tlZXrXam_xfo-D85QtTdxhqm_XTddMDJahkpWqYE09wca818AcHXBlgxEZ2vY-KQzkK33513c-61eO9Ri1s0EzW6aSvW9HEJhKnzDi9gbHKu8K_1mZ6uTUfZTVskKGkt1Kktv6h6NbE5v_OZN4h1WgIjvHDcLg47Z9eDkEjlQMBePShELENWmb3PyOFCJC4f5fHpDVvDRlwLol8_z6t46efVL4SjUvd7CcJEI3-ER9AKih3dcBvDaPQRmVi5OSYRW8dccoun384gJKa0XkEbVoNvCw15qmA5RMoyZT_n83Iate9yi119sdgNTu6hcDKRodVdo3ohYo1kMyBt0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJMpDPrAZjzjzCoHSoX6Tuwzkks9e-ITaPFkp17V-0LUTQ310W5NLXEUSyOezoC7zxHac3oUPyzqvL0izM4QYbAWepqepY1PKBaYzqcGIOiWhD1pKab0jrthAag2Vfw2dDe7uv7v3zjtB9QKYIQmHz02pbM-GQpi0bmqLVgL249XYKRUrBnzdjEcru4zdso_BqNWAiO7gh3af8gWvfRd15ZRDHnF2aLL4scoH8IuN0QmbA5kuDk5Tuqjy4WE84f71Y2qFY4-mvGNk0uw7Oy98yBYkZXt1xJYrKLbzCn-3YBuWkvpS6GQeac4pKSaZ6fYW_JUfyhjiUzJAIx7gxcjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH16oU_QuvRScdViDgGA6QM_WAKTIyvYFeq7ni3HhLKC3BzgmiHZTCooq0IcRhFLeJnDRlGP6QLDvEBCWoQwdpGWZj2BYVEMsKnhEng-48941jRwdvkyD4_KMOs0LcKaWX8Xnutr3onH3sexIGxjJcU_bklMutnmSsP-GxpFOMLcQc_ts2PtpbhY8fypIRySJuULze3Oh3Es91t19eI9rwEV93y4ycmarMsRm5hr6yEXCs9Zb1WSSc339V8gjUmD3eggOq9uwBYWkxMe4bGKGObQiuzfajeTIJIvYZVvgG6Dx7RH5KaYu5nMuXMVttSGS0X8a42UiX9QJQKajdgjRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0zCHXIs7oI5ni-HFfyGOyvqI9wo-CPoCb_qHY2RkrpjTU6tgqrSE5IvGvSFIKdf1HSaICJfMDXy4xVSS1Fo-zCDRaFdkZDUj5gxWKHyDIJnaMF6qLxaUcGz9DmJQaFCbMEFE-8YdFXfftxd-D5BnkO0Hksf6WxICuugagwolqFOhDNXDxaPeXwZZMYAVI50QlYicxU7AQFjfDSGoxWXatmXK3Av7VJiVaWAbo9_Qg3ZoKIW4SH285_BpnHm8qajrhHMap8q2-lBu5YG514gGroQKWkWcypE7rtt2cLRPLu4Mtt2uOgVqC1fycntFiELQdEGi3ByA7vmykENUF61Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnaU--B8m4Fd1YY5tEIa9T_haMBeIeYzMNmGrlZ6TcjyncXy6MTJ1Q3wBK1ghhYtZObvC0OpVi-RQcTpCl7ZBjcz3r0dwAdMwtmeIZZlxDwG57hlqct-Nka6kp3zoF5aAPavU18BD2SP5_JmBhSU_QObyB4A4hk4NytuODy1svSmTxvGL59Qzm41TRozEUfDf-5pArlVJ0qjyT7DoQBexM1pfRy-sshscjo-zlEoy4KL0sUQCnSL-INXsj44ljSTk6OJmsuGRx-UnXMz7QN_bJkBr_fnRderMBYumfbmqEfejVcGC8YTdh1yLm8IRMQs3h8fcUSm3BGaS2ixWJELbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV0wRTj4Dk9Zj8gHRBNdDHhuLodKW7rhMK3MQvAyaAVexGyeDcbZI7qpW_6xjZwpOKTm0dBl4H2InIZPKZ-pAPbKql2coUIsJXz4Iei37wlnILs654n4rF1K5qneAPUrzLNYpo924OZi3zMYwQNi4Bjtke4oxp8H_YWqWA5cV8gLBzgrzsB5Tce-nfwUxzLmPjaNi5r_v4e6suRgC2uQT8pPIIxPtq5D_ovS4KAaTZmM2o2cLOgcRbLS9CL8PwCQWJGQIiXI9vDiR554Q_BoXk0r6D51XElw_-3GZ6m-EyBQ6VaQU5hfsJhPjxTXiGyAnEEeftGt9HguPDWliZk4iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlsLLe6pQMf_-JO61gDAtsDk7wQnudQYsXbx1Yi5mYlgKJvnVtEjBTVkvvo6R55f5LCd1Iu_lV4DFoGisazoFpdGCg6f6hzMPNUuhEmk4SasDyri1EEhkQi60Rs3kK53OUpFi_upzAcC8GTi02A2jvIeNultgaL5Yy7Zewh8oj2bZ5Kg9Z2bLqDJnalY9hO1KSEPNqFLoLQNX8-PSwNEmeARLumJl6zsmByxocBdDOkXBa5exKY3CYRNHGwz7FLI7SpKt3omtgK6yuLqCQDqzdGOBV6XwxZ5sNXOmIyAG6mnqbSuqLkb5YzpJYQ_OzbQjsiXh3EVZUXdyHu10xNc0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVgbxQVQkjbko0f9rk4eg6gs3sUuKN-j5VmQ7VRmAhK0y4k7A3qxnWzQgOXxmWgi5h3iTJ7liE-d_kG9WfkatvqyrejYFnyM9q3jtYxetl3VNKt5OIGhuzvjrnSJo7MTdQLZMNKkyYkS4le3Y6jCObkz8qpdDUrc-IrfLx6OIrtqTpFWIUwU1Y7pXMfIjP_ShwHV6MxTMhyJzInGo-H5ttk1k59RAp-kVY0jeDrTaZucrSAxe3ZTSpfbBtH5zTRQU3wvJcl9ZW9XGrwJtvZbFX5iVSSG6AXLVtKN18s7rg4M17nlZkHHlkAg2a2WaQmOlK99ieUtHgTlDITJ2uLb-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJOUarxqWRBbAoLrlees1iKuekn766Vn7su_HywfTFcut8KfK5RvVyt5hU0QYs8asAKP0Bl7CG0F-_vKU7ClsF7t2jPeHaSLb_mJvQMZqj1ImWcTYCZyTKhKbQRqww237HdKEy40gk021SyUFVRWH0KbnaRNM5NoQ2pMHLV8-Pa4DhDRYhcf21ydnU3tNwGhNO_xjV0Rg7tRHb17KGmdxKq7QBtK5IFjGl3KTLqSQlMJV4v_T4rr9vOOcH3rDuP8-tehBUCtlyw0ZVfS-ksK6N1f31gsSfEuSz4bMWACjBTVnTX_QU6SevPU62p2Hj98jVzLNObTZnH_o89iEBMY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMcWIB1yE3_trdXtYTKzqlpZykAasK_NFkvUHpygtIYo1L02lKXWtBwUa62Cryy9gjimWyqAlKJkVwqDHKrQJqkEzurgNYP8xDBX63SvB-PeQGemEWFpquhWlGgWIgCoA77GNv0kospCKB2ZefBmeQKbkBOXHyZvWTCa1oxO7Y6MuxPrc0ObRncDrSTJD7QYG-Z3ZwGZRJvMWoohxqalJhCQwvnVzlVtldUqF_NBQ2g-BvTSSObkTuX1kGLMqZQWqrWrZOh2ewiUAED2zSh92thi-HOmeFBMQ338Dw0ocDGOQkW5QjWeC122v_vfD-xPzCIescMpUll9S6GYHiVWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnlGYoRn3VMmJ3iUweHInDMux2b9rbWfkZwbiTczUPFoHFTtxUExhhrkAZmRGOdKI0hNZ7pOrapn3i6D76kcxV1_ypFuvmlWKy1wgPm5iQvi2hcEWJ_BPWN1MHkUE_gkpfE6s_viR0mxY3VeMgKcsLo6G2n-B0QK0qASJImykXL3W_6i44iJkCuTNAfNBIrpNyHnj7TLXsj6MZS127qp9sXNKnOOHIoLW77gvpuTmHyN0l_8IbEC7pKEM65-eHiej3PCZuv-7RI-efWZUOh3yyAOb0iSa9HOtgBtQ1SIQSHWW_9Siaq_3KZHpOs7z4SZhqa80r1yGEDmKU5KOHHLmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKBdDzUUPNIDKk1PxJsGH5pAoim7lA4mkmQUkoyJkjFHqVpscxdzI0RX6TUTl961q4-wClKTN_ru78USncL141CP1_A14dWymJ3e71NnGTqJuFALO2RudYMKIhlb9HhWt9aR_vcvLMglT70CZwaXHnPIXhlDpGiZX3AolivhCOZqe1cpCxj8aBpM05KU5oGOAsxgJv2PZKkC6pBAa0AkD6bZIqvukc_nN9ofjn6Vcd_s3-N6wqZgLSqoG5Cmad2dSDOyWjxsU43yXGgAxJS8ygcaZGZ6iLvySTN4MePqNDQCRK5dELbr1QxQgLWPxDYlZtF7LDh7ZTHFI4bfbxdH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOhEQaV0psl8lf9fR80_7Z-3srrHn3dlkraiaF3L8J6zH0MpLrwPbqEAcPep1Dm-vwNhokyYJnNIFGk4HVSEDhewr-tY9A-4HsCzKTuIAqlal-YWL9mT0xIrw1yR3eqLNn41oO06QLT7WpmG6O3C8xghfalrXrzRfvJ45zcYl7aprHqH3z1I5fw005xHy3EeS16Zt41ujQaiGM__5YfSnDcFOUJreRjw_U3UnwzWnTx41ejzStHC1l2xqE30tD5QN99qnqRJRseMFqxmY8UooWAXRUa3UbdgjFV6eDJSEGNG6ufIVX9bS0vndLsjp_FW6IXopX5DdNuLJ58Y4Zh3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OgxmcklOvW0qlB3P7CLCtch7V88HaT7xGuwaIkDmf_JHLZ5Zvs4Lro0hkh2E4Tt7buxWKwOOj8rlWw5CZ894sfV0ynupb_stzNy-zkBOecCVFlJdndip8amE3G-vekYSPRExJUcYe36hG7QF_E_CCFZnkr3DNDQd5K_QgJ7acNuCf7-czQXZWhstNEnlnffqcQr13vA_1V4o1BE6mdg66OnwrTH-bOkLqMQT09Q5ZOQb1RuVPOgTHXjQkp7cDyuScEyaRevqEZmXT_X8z5VXMAk7iEj5C17GCHe2U1K3IankBfcfjrRudxzfIMniIrJINlkGv_eHB-JmyNYm-calUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlCIqx7EP7xmu5eY-wX2e6mw3oxWVUJ5YboFF4_kDDpaAjctf7FBpoKQSHAADePem4igtaoj5m-UjhWxTrsb_eDV38S7HIvQ4csG4Bb0A6GyRgSZHa3fnsc2Xo9kdz1WxFB1VN3b0xWsnioCDHHMPR6mnBAlmPqwlumfC1jKebr9owr40rpCFaa-SSff-QmuEsihrJXwwKY-MuonURlMbWI5-B-cvPIlUipSMQ0Bk8MvViPA4gmbYl9wYthcBg_m1MirlvRz1uUcyliU23uvrcLzpgsA-PgfCRPP18ZkHtPdiUh7tfjzK6F2TOq2yTLQSmYb22EWvummVWYFY2BAcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYzAiHbqDpiaXzVIY-R5IuoyIti26d6bTreVBqTe7DqdnARUHFYEusbLMNMUMFWJb_DTrPPgprLtOhYpDv691wcvaBsNF-e9BK02UJVGvSzjMhFgNiP4azCsLkMsr4M3CeJJQlMBtnM2wxIhzkG6Cc7vz03CDtVwHqRQxrtVHEyHbtD9yBMD8yhc9IsUf0ZxKWJiXQXZA6Op1abDdAQgVDesNW2GJg4mbSdBRnwTO_5D44UfJZ7W5zU8KkcpFgqUWPORKij-JfYmIWUT_GOjb4A4tLTmgDICgDJSIg2BRLQRPCFxmDtjALHLBVCrOPjwCu-CoUeVIfVyRmXYkyho4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6DmT86ewBUl01tkkWAgtnjjPRmDgzw3fb95x4qlrNRh-soYcccuqxa649LOcMlSR3vKe8N9czhUA49ljAkm5aJSXyvx_cCdUheeyGvLeAHs2S9c4auHtF_U4v68NpBnBvJK6wgqZaHj8Fc1Ldh7CxyF9Is2pmtXJUHipUCnUIyA2oH7U10PEI8tWSdmXQ2EqEaVamUm8rsk9B8n6Bg2emyYlqFDUoCJyCAF_OpEAy7CXJO67fIV4wEno4K9bwUvYjuZjbFNBb3xlZyc0FbqbDGPxpxb6gE8EWIz5HYVgQyQgLy4rNI9k-VsVPFZq7vqPPK_jXB2gFptwbAjhWeEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZNWKdFQ7ZdpqIkeMCOhy4k8iwUgZsWNdi-UKwPVP3WtQL9lcNxp7AEpqleTznbMjv7-JcsmK2QUCUDtoR-kxxZsu9Cgsx_W32xbqHegScNEbHCDZj0PkVgIIdV0cG8lTnwRSx14169f4S5oeR6N4BHLr86nYx384BJzGGFNw-RPXm8q5Qyl5tyieIK3i4TAUutGwe3o_H2o1UF967Asf8fuhG3qVObCbE5ITpNGY5MYFs1mKP6Vz73R4GAKYwnk1L_nG7sHUL_rCCkJRvunffJrsAzhD9vGKBfVj4_slVpR2kRrBLgqBz83SDHTaTNu0kfH488XdMvwLpXpCnEZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TD8UGINyRdFjfC_b1ZeTctzzJjo9r6-JXk42kUmuXf7UHwYskIY41JzVDMmdVtKZAxDTqQ90Fsv0Y7O2B3PYG1npvaMHGYMzGFesQ4U2QWGMedzsJxqsoXGbfUGnwILv_8fI191pMzO_ZhGH7E_RXt339CDy9oDdHJMpezHvzSHNQmxc5cVZWYmjPACg3hPmQaHsX472_31Hz2e6zX_i-iSukO0I74P9FFg9gUlpEaqJBHk9QhpxXwz0huOxfxkxsd5xiRFHRW2mK1c3_Nepsjz40Elw_1MfEf8-AS7rYmQuOXtlsoslogNpREguh8ji8E0M2CTpvzXrZGD_I2B3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYeIL7WYO2BU2SiZim1jeLoyUNh6X59r4as5mw9KrqL8_L6AUNHTOqRAMgBeVtflII1h2BRnv-cF-CrPjaiFHYYZeqDskQnyOyxDkmchmr6r434R1AcKkNrMPBzcxayVl8yuquHAB02QgS2S2X-z_Kfcc4e7cczCoyo5d2yyqrTOV8mqdk_aIuokKlpIQyUTE-WBxzTyDED72d9l6fo8x0JEydswvd9XBkF6r3AbfBCBVlT92y9c4tXKtnxxymtjwwCYpgnlbHaV0AKdgPMSK5MXSXm9EKDTYcg9uawnwhaPc-tfZFvxqeg5yJTe4liIIGN2K2I6q1b-a7AUz5ObDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aM-U0a1DaBJZk1ddBkv6HKXeOgbZUx6uBEu3oDmCwgC7iSCAhFhgdPsoRm43TKhefi_Ecy5bVqo6hPoZQ8g2re2WP-r-RY4RhRi1qEi8-NAMMBykGRxP0hSYEawUsm5_RAjzifrVReuhV5NNlBaNoYJasoGSiYZBInpTsnJ8CmiEu4uMS1VndzOsyp1e60IZs-8YNDx8MrNyik7gbel89eDQerfOLC_NLAUgBMhtf2coJo3tqK0JP61FKSX2KinMqxZrglqZN2I23azbFFQ_CMprRB3d20amo9s75m5NkknrmygWqTRKGm40RfCckbAK6hEbsck930zQi2u7eaO7Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjXeUcefwLK8B05a75sBHkvnmGhWS9S45lRlYVeMA03gyN6rCRQH6YI_8CWdHAKkkFT3KY5LYp36Czh49A-dds0J0v-dh_lP2A1jlIkundjU8pQgaSU4pBdxME_rC6nCuxWkJ9eHv9DceKxkfm-67qn9gaEwzs-GZmy2sguLryIynqbtBe-SKOMxLk0UdlzaQwzlXT3emN76g6Em20LINhJkvGzeoD1fpcsnFdJluEGOOAmEu7NI40Tu0PYZNDnfzI241bVDWBgUc5Nflf7BbrByp27G3MBC8vJX4urLO8_XzFn4CCws_BG98kzS0MzDt_ve7UMcjCpOFs8BUfEcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmDK6sEbcdr4kKbSz1_DTCC1H67H6CMs1xto6Vh-Chl7o42t2T6MqSOq2gf61BcLEfXphYytShjO8hwqf4BQUkspNrT3vz2lfaIO_T01QQ5NYKmWT6BbNsGdCHxaLzTBeER0YrLKaITKks5nU5DLuz89ltcP6rXGAg0h57-Ds3eiXasdtvNYEkVkajhCRVQ8kJgYU-CEM7sZPpzHKEWgtxiBkmbeUUsxmurQl_f38BVW0_gO32mgGmg6USzrmhqlsVI-OyigzpHtkY7aH7u5gtS7a_2PFoa6Xx6e8I5oHFIsF9M1FCHwnc5h8OI-OoX_Mhbb_GBW3z_hDKTf4lNgNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDiBVrIPtYlZ24fsTEvdvn4pWh0l4C-s4lMR0UuVbf6TF0z9rTr1JaNMhNojxk4bsdWJ8Ak5-urAKjjt1Ok9x1zGx5LY7co-YhjgwMlX2LlcAfIRqApAxUGEoPrInq9ikmjS87SDEZc74FUC9EJuTwdhOoT3XRSliTcAW_kgFnDt8NfGlOL3oyKKjZwdTYH3nq6QODBibO_cL0Z_iOP3f2Fa01P6PncvP6UOt_WQPH_VIlCvaW4eOLK3nC2ZzriaQXmeHKPL52nP2q4kK4m_wc3HyjnQKGPsCq-ejS7jlvFg2Ecxu1jCfUG9Jcj3SSuOuOre1rMcahVAlzJnNeCZTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0jG_ikOZ1PjMQekUJw4tQTgH10VKA3lsEzZBL9qFhZ3AlkEZ6HtkwLBsubCpNh_NkGua8FiGuSmiJNScam3WRMiMuGRPAVHOcMo4CHhAZUvJ6fHT7soHlCdPkjXYzaGv-DUwXRfl4QcuO-pmTF-UphFYR_TvHVprlzMSTyuYoGuDhhnj78uoE6nZKT0ihsbT6fQtE3GFWIqEiJK1tuI8bG3Ix2VlrowxRgLCgyuaBLZnY-jt0QgBVQsZ4EuxYBdIZGIpO1wWTIF4HRamAqY5fkQJrzx0o6gkgMfrAVYcbbdLT3s2B_PJUB7ptBMRUjrZqDOhhxKf7E8HDnXbQk8mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvM3GTfBSKqV-MmLEeEZZBPGiPVKycGOzpMiQ6bB3nFmgj3Go9jXP_wNEt54R4bFNozDEJQQ3Ogr_h4SUC2x-HMDBptbn12jfQpLwv--EjLcM-6qJpNPfObOgnDmuXaeLfD0aJQ8DglnBe8q_xK2T_etQolp4TYznUint2iZ8gtSl-n_M1WGCqlixsZ4A8qhl14zbTeuSacvlKAvYZKchgR9KfDtcvgwobnWVa9nLfNkOx8adFN5Cbp-Z5R2e1M1eEkpBNvOoUCkCsOwgMfgREFR3GBKQzv97ruNeryRmr0rIdQHiAmHvNA-C7qlPTpDA-ibS6GeF5rHfD-N5RA22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N37hpxVNmvWSCoM8HRU4xpbEQVK1CxAvCFVgR93q6PNJ5M5sP9nSzgCmEQDwrBPH7E2_L-zOGSlRqdviAXx_T30_SHxBCzsW0f1pbfRL1x-Hy9Dl5KplIJMBj1l5V0hRLA5zWhyCzlg4eunDIhtx3bRljbewb-G_-neh9JMSL8VzxwMPHu3Fs3i6Oe48QyB-h0f1SQqe-2Z1efXeoumYn2vHzK9Krp82P8Hl3NTfBOdVm6oAUlKZvH-Zk19XGf50SnMcnxZtYRHZdsOAJgwnMnLw84F4Z28vgTF5Xis213Iw1CF_bS1aJi_A5NljfbTrgDFs0TDtgFemo9QuDdgKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuSL5bQkrBDw1TE1MfoRH7ImNZbBTEoHyO6Hnd0FHkWJyEIo6w7v18r9Tbf7UmeMWqpbpTJO95IM2yTmyCAL4Dh9W_3Ey--TrJV2vVdHLKjoN36leyo7TmTvvb0LDxJ0e0oRESfMbkwSsDt-4ZkDwZJbG_Q9EkRhaz6z5RyMpRqGvJz1rcxHYaFkN1qOFcz0nTFkSEjoxjTTKcvHj9fL6129QKyCcHmtXoDI3dhqdXb-267bbWvoPbZskXeeAzaAbamzKGBcrlwvFiPCta0dh57tE-LYtF9iA9W9wfn-w0t7dyvhv3u_geM0nb-uEFJl3vaL7S8oR8VPcAFBMuGKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKVowzDOdG5Pf4C-QEUy9PLGHN9hKeEJkIxgDpV5ZHKUlTkqq5l1zgrnuBzcF-u-fXBQfzQCtD-fMzrrpvXKzANK6WR78W2XjLUhhk29F0SfbEPYmHrUfD4bXuOSDjdiUzRRFGI1vJxPfMhV3v25pKYhHa5ShAZ-J-Ss7AvSEGgzEKnRKjf32oYvSuxOLbefUvIM7OYyHJiL60q0mkQxW2OUbVI1P7RAQFX87zt_fy3gvb5pgf-a7g5-qptUe8p37MGnghWzrK4MZzIJVETMkeZ6C9OoNwUUFCoaGLd3LK6-bRl9LqTx4aWzhbTyIpE__FdY9FFZgSReCjSE645S6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANb7Pdm0pjptOGAUgmYe9oScpHkOQZm4pqsXN3aiLtvDIIsPGmRy5GqhT7MJQeFoez4BsHsslXeWjJZq0EeNovRnGMJ6p1v2rj3WzUQRHi4gOmlEfEOHy0DH7MvSWM7QgY0TLwKVnhdQzlCiR2k_Y4TVACisCPc0RM_d9CC4m6XO_R6o3EseNGrE9_kJ4GowQR0AXchr9XpBGlHkQns-LQTkT0_2_sltWa-anD_xcsvb6xUt7-7tpC3TW5fk_TV7dLbW6WXgqLoWEqLsZg7OryqwbSNau--zHGXAD0sBwOHhmH3OvYrxMLA790y8hvk3DNyTaI7BifN9ZriEwO7cDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UysKoZ7yU8bd3upugHbF8kVKhkqo1ETN2EiBDulYxbMxmvl8SMH1ewKJeYzt90YxdE7SIalG3xe3skq62iQZX2WIEv-QUui_44Zdab4Cqtzq-sLfvM3q54QfdoFxhgYzy9IXlEwkK3mNe0BjM3t9EVF7iUPBnKdH_TB5adcWmwyZ3cQ6zxB9EC3MkdMBq2gekSqOp0ZqHRtZnpOE7xMN4Oiw77kCEMhLoMBR3qBbI2Hg6XzWd5a0njR8fdpZrGEVGfg55jkhQSa6jpdCgzgWySlxIPCxbTp_83lu-MfLLuuihxn8rGbaTbexjSpMnKokTLI0Ty3DeGapheF-bgEcbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR5ajLRoEQCwSGMds_KjKQmxeRj0a4cAHEkSqj8LqIb9E29Jxuqh-me9SNu9SttY0IEJtgNfl9uqrzSWCqvo2Wqa-toGfJIwbAX4SOX03WYgkiu0_szb_n_Lt7lav6RnwAI449W_du_PhhXdeWqRPfti8aCHFsSl-njdgw2uWYUS02567iLyXZq8gr-mEiv_EFTATos4ZPelpPyQ_cV4B8BEh4YoMFUXdr7vlJtxzomBSvD4aDYS6zrPD6OYnkleGPqyZPuuZaEY-jjYEDmsic0iR6L8-BlJ7G9YdT5P8W9LhSwDzVljJHAGolH2Ol5APCfITWSZmDGaYgARDEh4XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUsA5POVbi_X_2dpkr1NL2Q2wXGN0WzD0dNlG0MBBuyVI8WDne2zfect0aYF3i6cYQWbOn7BoxzhMbiBPnxLQN79Qes_KGowaEZSf6QLHDz0OhBT6XY7TRQ97DjUAb0FrafbPpsVR3GqNKo6HUES254HDxccDjtaGv2pO42ViTD49waG5lRDF834Z4qNV93512UIHOLb6nBe60Rm1ZNAv4Vow-nUlwSp2FDBfQTP0FtgPezIXCpzQk2OTt3CCFoyToe1E0Eb_eWUF3us4jN28LJjwIK0sKAb6yKU4mcjS4Z3gRF4L_pV7A3vq9KktkT9v4WtnZdPMofqC4irN-H_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzImAYM0-Dz6tRIXFD6NUwUzxpB_V1-NyF4nkH4gXtfUApoitNg788JrPMRX5sff85JxPVQL4hhUa3I18iWyzvSa0OaytbLfhMNJExkkQnW5WS-iQq-WOAEArbK1KTyH44uEvpr7rlqKZMPNv-hLphwigG_Am3c4JpE7boBdga8xW7CxQEv4dKQqq3mEcfx2dmxfNTfkm6foHg0TD0FDlvzN7mWDsQmRqhEN0SJpipKwGy3lLPhNMXh4D_if5XvlO2alwMYgeYF4miEXdNIJI3WXYCQ_5Gd44FplXieFTqhe0UoQBy6cPAkWGo-s3gZVkKwi2ucnt3Xl5UTcFV_GUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdNPBQTJL9fIUgGkv1M_XzpXX83GnR0wDw3LZlFB5wjgZli8UoANo0ctE_Ws1aTMxwWIvgm2iw5YH7StEkrLQB_TJrKJIatXYYr0yDhh0-ARDi1WzDahtiWZeAB1_LLyRyvmZWxFLhItBf-H6Mw_13aD5fmQMH8PGxjLFppfIaSvbAEW7v9rPQwsheM14IS8P-n7vaxbVOFXD_1ZXm23MqQM-hnopEx7hcA4ICh_GjjFUYcwq9Dgl45r64rkz5Z4agp3f0S2-0FQfRlQkp8oO7i7Vr-4H8mZnLlBJTst-6qw5q7FyA3aNcnna84zXF6yrPHEsFgVNEg-djGJn-e0vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snCod2mSvc7s3NNPOBqELwWVcKRL6OwHdZ2D6bbtfQInAmpHYlGP485-Xxbb0Aie1pKHqedj0Gr-8Zg1HXcc4d_YAOs_NREdrOwumr2G_oipSaXEayQoQW9w0T4IJ4mii-DcNWmGN9DFOkfiCLR-f2P0DXHNm2zM3_iq-gF9GcUX0BHiDHzufEHoUQPGq2Q2RGZM-JQ66fJP6GZpVzsaeI9Mk2UFFRepaum6UpkYAHOzT7ywEg7PVfQk7dDjhAefgnyMBvOXQnowZ08Tr7o5PxvBu0kitkiMBjMlMNk2y4avVUAPjZum572sgIho9C5dhiRXlQWYme3xFklWs-JVog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=Du96tC6hbDIHzTxjEepLl2gtORujSS9fYHUFBHZTPZfGNELMMyuMjj12KzXBEwogahzOyR031I5UaQ-DoxNSMaZLi3JnX4yuFEr3wpHzhJfJkvfVC0-FWPPgsUh3azbsWW72wxz9bC4p3DbyNIdriGs5v1D2cGwEn8tznmuvMwfTDQUsCy1R-y2fPurx2su6f40T50xcvaKgjWrnU11SIBn4Hvj9j2-0vx3IgcPsk7fEVh5mlpbyZJPnlN7f-wYsrXOwJle7_fQvsHXk3BfHpppOm1RdjM0s2JPEBSsQ-L2wGpCnaDzmMlXozjLmgOjjxOhPFwwaC4TauukDQr58cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=Du96tC6hbDIHzTxjEepLl2gtORujSS9fYHUFBHZTPZfGNELMMyuMjj12KzXBEwogahzOyR031I5UaQ-DoxNSMaZLi3JnX4yuFEr3wpHzhJfJkvfVC0-FWPPgsUh3azbsWW72wxz9bC4p3DbyNIdriGs5v1D2cGwEn8tznmuvMwfTDQUsCy1R-y2fPurx2su6f40T50xcvaKgjWrnU11SIBn4Hvj9j2-0vx3IgcPsk7fEVh5mlpbyZJPnlN7f-wYsrXOwJle7_fQvsHXk3BfHpppOm1RdjM0s2JPEBSsQ-L2wGpCnaDzmMlXozjLmgOjjxOhPFwwaC4TauukDQr58cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDlUQEptymroD8jiZS5K_TSzfiPPFor8mfpYMKZb3_GULlR7Klv5FlrhdRoWzM4aqDH4xux3ZXtXQxfC6oNiodyCxJhJGYFkVWy1mhMoKgxXSk_XHU4yjpOV9M4hzXCc9sflo8eLyb2YbPzizorc9bIn1MrJo1auCIJwC0VWtiR9WAbQt_GDm-Dg5-_rK4ymFKKSSPqxbOqvfXJJ-Nc9JNhAFmrdEDy8Vn_Ovcp7BFpjBPtUWc5JXax8X5SiXNqsgXJy0BWiYmstFjQjCK4gPzPALGDXExrf564Q68PBI4KEceVBIPCqucyxbkxxLuNR0LYeOhskU6NoOFDKyfJUgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmoQooSAFjPOfJFySC_cnObTH-SiwlE5Ptr7RsUtY_WGhyLEO4gQ8EUMnQauu-UyJ4HykH30eZ7hpx695Smm3h1QxiO8uhYeB4VZd7WXkHKp9irK8f1aZdzYv8yfmJAfAXN2N9Dlu23axaVzSGQmThvs1h2wkEsgwfpHqJXwh17_9DKtUOSxMe5K-MpM3uSJ7cJR1zn_-mSPySzGE8xCRiNbb0Kyza0vYiiov73P-m3yYTsXJB3tOhwOu0dRlF5XeBU8G5VqGg99isnxw3zk4aO0Xx6Hn-RXNv3scoL7PUfcIun-Cj1Zi0uLx4EQ8UFX4OUNZEsM6Y1FB_wkMtRyCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSVgKQK_T7wZati0G79-4IcF0RD-IogcfqMWqjwY64OlD4b_sW6DbG9jOZ6utGucM2GvElf4pkBWdizMHMRz01vGGgNOw2XvXIFHojjbUl5is1xer3fKFOON8JcQxXAcpmhffhcjCxKE8nWZbMF-vIXCOWby5KJ9pP6ekrGxgef_oLcAK42cjoBkGmWLKqF4M1CMI311dmKo6ShAHZ9chbWsIbvKgxjPnbMTdxBRwE05CRXC-2v-4VE0_PE0Q3K6fi-NJU1Mt-PNEARjaIgKGVtxlUcKLYFzr0AZJb1115BBzA5Hb--kbB19FQcM-QHU1WEMKz4ygv2CudmClgH-fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ0fZez63JDnt6DxRYq0gK1FovD8FXrVCm3avJxTD-ot9EY4_UqUZIT33bxIt91zH0aEZn5fCL6J1yLu4UlttoIDDzI2yR8nFmaEJgLNyAtj4OR3QBQoiGt2xDEVbMXfpC8LCFIvCD1V4V-it6FdXmJSuAPAe0a4iGpFj8mzqLcG2YkQSklKzScBHb40_-sLsyyVI0ghVVbVY1y26e-BzDclOCRNv_OuKYaPQ6FACVbDx-PIG1CBld6-60RQslxLo5JeCIM5WAu70ELfyAWkJTI5DcLcUmqFiKEseifGJTb6q-1K3iha22K7YFHSfG8LJmxAFLnh6Orl0I3taFoXOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLfvjgGCBypO58B02yZrjG9LkKWoN4oT41lZkzHuctNupMFdFosd3pK8Bh9P2Ajw3hn1cu4fvuP26Fz4IHGqoNCX2bKAUdWwLEhWhRXKZr-qTAvvjki99fy8ymVt0oRGzhcGfbs4PBR20DQuZDVzrDu_WL4cMb4tOCBvWYIOHsIbWuHRSaxHz_jVLGQcLxiTF3y6y5mf6_KzBTzL1sS1ACXN3EV1XYtuRDwGE3A-4H6d-heevIA3LctY8mZ-6GqQYsZC351n0U-j-mdOxohRw2kY5C4BTpv_e9ZI8fiyPF6rQ-oD48Tdyil8gmZjRPhLupolYuW0ZN9x7KwMq7IMAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJq-Kd1xwHjKgM7ir-_HaMQCt21eommmcIljCOeDbC-k-S4-6oT9F8D0-ZWxVFRDiTLECxR4On__BVS40DphEqVtbY-ANEZ57T2TbTaRCX6Z9xYdECTROpM4zj0aeq3qtR12WWGAjFLxrdAD0DSrcSC1ymSCJhK0qlKjwvafQVRehSX7UjfelNBFWEmikCVAz75hMnCwyRR0sa7yXPjCnoSRcmqBD1IAAqDCJQ12XRBURZTeVwySSSv6z9kO_5ei3-Ra5-agr0Buuhr8BJSH74HJmc7PZWBGonJQtrYmj8QFZ0p3H1AmVTbkYrJGS_R0cXmPpgywafN4geRPt64jJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEPjalc7kenoR8Vmuq7vNdS6B5Cc4M-hZR0Zzj3w7639q0Cx7LN1wegM64NFk2MLKdGsOFu5hUPaL0wZLtVPi-lV2UXN412mSxYafw3nQ0hrZIEE7yaTeyvQLtXrQiEL26ECzQWPmnSC8aN_NhBdPVurSCqVCLOgyLGzu5ef5epvDOfa8xCz6WZWySUZATqNkLLVAD0Z5naXZ7xSIetzjJrZUJN_Iice2LSY2AunphPM9MekvjM6m_4LflzKOBfEs4eB3nBzOCDSs6BTQNymyjbE6BdnxH5oylwXJ9VTK0RKQt78OMmjhnzS1GRtPE_rwsH5w_90MW6J6xL8Xtpaag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5n14_JfjUYbU2I_e6ycwYlQu869XhOXPepnHHtBSbZDLp7ziMjZpdnFaStTevXQBS_qi311YG3PxDS6iMajOQcImaQntvH9bGuSg-f7hAQbsocQPQYB33-ARVPVN-ywC-aruh6w2jpazsK_odqEa0BaMQSHYYj1Vuyii-KgJb83v07HVLgTT_clxGwt0_9IU5Smt9nk6YJa7O7c1HHe5opbNLtacJ1g6QnYxzoyNSwYnl5-V9NogVinAIFYPRSvw3H-_Td9nU2pkZRaC6jIUkjupE-TU6sVP_BSrsPp9U-bi9ocl9mEGQfJuvSYukBtoosAaLAGmIFhvSe4rxSdTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0oh0dSIsc5FNUd4aR1mj5UosDyj6Lm5oabVXXLCw5wSqYp-9UVMwsmWvG6tQCCoPItU4DdNNigeon8qbUY3vbFZ_gME3O3iR-0sWjvVOGIaxGocC1arJ-V7ts6iU24isO1ybD2L8Kxe57xsUwXmetSlI4VpVSezlhvn1YcXpKoPXvt_Grsl3n_w99PgWZBl-1hgYYcGMWVNxAoKii_NRb2ppEwAoLugrPafS7wnA6luagQXjM7GTx_LevWZsy-JCJ_IN8nkrQC9aMJ_z4n0G8cR-h2mkosq035u3xmrbYG6_yltwiI0L_J2xuiOdNnjCFKY4oPfGukOTjIccXsWVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe3yOM9eqT3WE8urMT4WJ3JvbCy7L9pvVaaV0YMaGGuqyp53cp1hmCDlSGkrjRLnyjTc2rUX5ubqr91Ef7-L7WPiRYAVcLScklqZvT17Ts8J1Wg4lhrnAL_J-vqP47eJPCRQPuFYtJwKOLlqTARfIAsI0p3_QpFP_N4WBS-4QgGDHM8kRlpL43eh_sTGTHrzj6wr5p_5exZKxUCVQiexlEVcHqKcXOjl_Ktn6Q5C5nUgYQfgNxoDBIouWECpmh4lqot4blxxoKJXWdQ3PN1Gsq4vnfaxe_xfS9XgNrYI4v4Msjj7n4dYq8u2gwJkodJQxqr-1ZZxfENLAcuMGvsIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5iYKxUUhurahtoQMt55pYq4wFs0YpQHwdDaFM7LkUfWIKIBY08DEEvzchUyWpM9XV9xkm0Q9Xx5Q8fBgO0OahANzXoo4DcXBlEHlOOfX5up5r1shKB8AZ1SMP-tQ2VrpNXd22QkicG5CCCP0P0hunIuShvU5ItjR5G-zVnxKf6GBCEIPsTEZMTJgCqA_WkyxK0ReT11ScY-opoiGQui7l_0m1FWiJSPUM1Q9tKeibsWuQIbRLnqBFupm6HsrgmmBXDpxeE--rWKNB2vEXOe6WJG0RRrj-5hklu4qvVaXFVbCAW6_ff4UZlscHreirLpb_d2tm7LgauBu5nvOwn7rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpbO3ehNu__aylVvkSIXDQxlE6btsnccC7Mkb5r_OYxUd3X8dUg7XyV8eWmVdu6SBudbkhReLEpfF-BzB6bsCRNYfzrMPJD9KudfPNrQRTGIrPlnyK_U_dxvPx_I5nW-Prv5-eDwvqquJDhs3xfYGtNhOrFBQRSLoTWsoJiWNTHbkXGkrVvCeuwOk53dG37e_sx6lKows9CcW08kGqPg7T2gC9eUPZ069y08StwMIAfhalPVGu1C8MElXVaKt4jiRxmeSvpUetuzFD1o-lK7abBBNolSyB4pwIgileLkZVjyi5YxUKItUEKjWnQCDp3Vf-6gsZP3NBp7Ul8C5It1kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0_XgN9atTP-0iqzqlDkSeXzysjz7NjjbwQ4sue8FEra9XgJJkJzaihHAcW3JOQ0T-x-ZPYDk-x1sF45xBT86mN5T18E_4tFgbik6AOnjMtDVvOysItbN28E1dV7WXvvcYB4KgjwWRAnU6bC3EgL72_peGXu9noUq8AdfPbA_qvSSrw6fT82hmrFjbv9QadhPygw_l0as-O_b1Lwwbs8Wu9LOSkODSuDoP6SPnI5rV3eLx6s-JMxRhZSFpjc0KAI4QHuz46cJt-JjbpeHsbaQZE-YFJCoL6-t30RnRiXeYyBnKSGMl_DMxZTpkAJ8rVY6VHHwRz_rdQptOgBYDxdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOAqewISsviKG32JebA_DlnzUYe9lOtugHrYwqBTJP82FlaO-W9HqnwvYM15yKx35QWQLeImHLRp5qL0cdyfrPoooghH1w6cA2Uy9SD0KiDP8Oog1BNuav5iQ9Xty7nh5NNZNpIjbx5PsM9YXcqbaIbPtlB5u5eObYRur-wx8I9NVK04QQZFXwNgxAPtk5EEKTMNM1HvXgimHBWQg8LnjbmwTDZsWEI9g-2AuWI5yhVEzCOcuD38lxbp2G_P7SaJVNPogKXkvHrT5LZ8Dzu3ljcLf08F7_akU557unscD6mhbhTCJTGTmLDZWgQ49ZORvL1Li7gG5fzZfUCMWFEbnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTrfTL1eaDdq-eU21lxcih-b71l2XeHt3fxLbRLBjbAf1_4uOdxnrRkHTld0CQYpcvkPU2GW6f_cviHKhIY-72uWFqahxr6NSunNQ4sX2mROwcroAO0MJ-_CSNFaOa8Fft-i_fANsvYF_XF4i3VzhpFy3Jq0k7Bmcf1kxQnj3JTRis8heJlMnZfUiO0HD0T_u9e0f_skTQMIN_hfMUUnKgZRhQRbsXl1VpA-BtRqYmYs8I_g4jg_i87slMp2JQue2U8oRsT4d_gh_0rzZ3XzA_XcHjHE93iuNQ634NPO4oTOo_FhojSsELg3XBkL8JMmqe7aUF43fbG4h2qwQtfW-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGBQLfvkbI-AbrDwnQVn0EtMQBYsqps9Y9198a69mm6O3fZwoVpBnM_wvrCZPMuoz4FtDNR7AyzLkRWJhT70yXnzr9OXEfVDOwUwMPckt8cH7S7HRK3qbqOoxKDuu1ukSkQj0-DD6DdcMRronr5RVvUaJxFu54S99zQB5zwCQ0oAjoKCQZUWxqqWiZtsPK7iATQJHYCYA7vQC7DzxyNlGszD4Srl702kCU5SwnQcUXrDwFbPUQjj79fSP1ZGN3veUsSzuBaZUGGN_Cwyu3GrIYW0z9AO4aTvDjj4YexzVouBYXJgAL9DVdgITHU2ocQiZy20oGYEcMLuLISi5gBThQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDWsR1jsZ7aY68WuKSDR8LlUJlIUOUNHCz2dC3uyvNsTdlTcCeRrqTlrpLyMp8UlczE2iRV9jJuZDHjlgrJbne9ElTPAVSwU_nAJU29p73u4M_Vq__tQTaIZNwsmJ2HxuXW1X4jrWuHVuKVmOl8hTnWz_aB8xsFm0t_2CL1GRNcgEjnEfxtoGJkdrL8rcQeWhqrN_-B0r2Mi96_QXGEo_bjqeERuzpkKC_kXTLNFzsJLT6P4q7kVUqFZXbYnWvneIHWg3Y1mKSXe_XaGaLyqxWlspo7iWfKoAozyNLvetqwuzS5YUrr7H9Hzmd85PwR-7oj1NW9Cfccpa4cJ_YbTFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqnD6Q4Y97zacNALnbEuezvEjTLPDS867xxmQnhQCotVJEvV3GeGTPKLi2qkcb8XucAnQLIBY9cBuYKEGf8QYkKhnj3PW6v1tjkNRxxE47ZKwHKs6Wk0BGye2o_h9eUqCh_smlwlu6DQXU3CaiiWLyK9ENiUOos9xE7xu2sVKHtatT36ZbKatYrVLRUkUGtkemWCObqJ3MsirmsNJ4EkSar6mU9v_TU61K4ugIe1glLRH6pj3Jgxjrlwk9z1Libgd9IDqUYgHp7C5wx4byUelElIketcFk08f6XLdXpEtK0BkS1jU8DyXC9Q1pXOZ5NjDfcGtWWkKUmb1zUhBlA1Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAlElvF1Eyn3d1ciiQr5pzVIbgYjRf655OPtoqT3dXLQ3U-uNMzOiVJw6r5E1T9e_DT1PPIkjtfX0J3r0A2o4eEsVvYVJ156sS916Sy248Je-rChIGP78m3VDS4SNLPPYEM3Ox6fdzcsUEFPBgMyPGlFsAbjYdqnqHz10DH08xmtUAoC9hx7ZHQwK5v5zc6Rf9A36XnfiLaJmib33yQCF54_TFrDFZHKcwuQtliJelAKuDss5exikVgusfR9cpaWiB-kwQ4e89qV4Qtoo-EGqhCY3bw6l3TWFVHOogyEtxkkCA0qcuhMP-hwYknccu_2qZIC9_viAmsBrRDk8AN1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Snylw992FZGo8Iax9zKiwLNVsPZe_pbK0DTYDQ3QLiNCNlYW6h9Gwqu6Da_M45B5P-ZMjb_h3vNfCluwZrRxgQ3OPMYhkg05mkRguMZ761O45gSNpCImjepTIgHUmqRvS46MHJF-EDjbpoOoegPajxnRdogF4ZpJs9JN4yvkZ3Y1QH3DucU6uMxQ_XiRJQggQdyFkJ1VIyTkbvKhihf-2kq0bhe59QbqdjOF3zTQeGS2BJ_NU4wPthvJbmcRNLhRZFRNuzU0GlgBN_wfwv0hNkNv3mMAx9bZZicG007aIsMJAUQaeEHGYKJRWTBXn98sem-1Nq3sYdaWxph5ICOVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iA54a2LOaIIpXJj49_NZ0ohhFk7CQaZ6Rwva8p3EEqdDHSYqDHyH2TWFSDNRU4i8kXNKMPocT6AqQ0kdnzkBKGK2k3T9oo_O-GZAmmFiag6aNh0Js7beDLxWBSPDBYgm6i0kB0r9EelV2p3Ed241PGcrRJsm7F43KRep0JjJ8XTNEg7Y-vn9PVbJ0CDfniX6rPoXbU6lLOHtK1orpWwKUp8Joq1dT0ldmPG0VdNNNUwhrcr1pkodZqfVG4j9yszyYo-PUHDhoa3CLHiRpZYs18iPAjgrGcKGNOID-dLNpRLBeZnw7-w6sr90pENiuFiU9eT3LO4j4HgKzBLlHsj8aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=XX0b-4-IpvXCZmIFXMBLu3dOE4FVpZgELmJu9Qfl3PTLmlpiVxXleWd7e2Uo5p1WPluW8rtJjlovM8E_zHYwdL6tRA7VBRTdcUIwuTQZjU3hcSwqkZpCs2BPrY2R_2tEBQbd-9nEYQ9Vba8o0KfxvP2PsqnxNxHzB5CIVSnOgkPM6rkT_CcQWQqyfFWkFvuW36crCgaXcM8nk04DiYGl6C5VRqQZ6naYtvWRiCHhuOxFeHlHijZO388umkG7Prcph0ZH1lr5F-Ko9vWAh3HbUJ90wGGKhYtp8M92UydSxlp2Pk_1GinGkWxbfP2f6Hah4UoxxSXu0j_px5yov32lXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=XX0b-4-IpvXCZmIFXMBLu3dOE4FVpZgELmJu9Qfl3PTLmlpiVxXleWd7e2Uo5p1WPluW8rtJjlovM8E_zHYwdL6tRA7VBRTdcUIwuTQZjU3hcSwqkZpCs2BPrY2R_2tEBQbd-9nEYQ9Vba8o0KfxvP2PsqnxNxHzB5CIVSnOgkPM6rkT_CcQWQqyfFWkFvuW36crCgaXcM8nk04DiYGl6C5VRqQZ6naYtvWRiCHhuOxFeHlHijZO388umkG7Prcph0ZH1lr5F-Ko9vWAh3HbUJ90wGGKhYtp8M92UydSxlp2Pk_1GinGkWxbfP2f6Hah4UoxxSXu0j_px5yov32lXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3ACu2wCnz44aKOWlnqlup3iMuDiguG5tP63uVtHmRxUsalKhSTq8k1FREjrNWB-aYT4nJvwKI0IZkpUUM_Lkf-klEHCUDuHHZ14Qb4jNJ2JQhbCA8PriEirWbFVJqVqpqOyFBG7nDDc5y1xpgWLv1BBx-s3aUrNBFsF2OfciRvXOJm_CZB9QAB-shgpb4xwCrgbPEXSwlHjTNy2BYBGkxEFObVFPvNlnD-vyBFj2SNbnW6l-ZDShEhn_SHR7XCM_AHxCzjKUoQlBg2_rxY48lVSoPzL-mIXmYHZJCydu7vBokeARY4LU5fu9qHLl9RxOx1-5duQKMAoNlX9MX9qcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpN8sCupY7wxEHDEAVERXubSetjZFsNSWNqp6wbkVXZ6eWeEPBAddNy8zQSlmQ1mr4ux2JZRUXam5GGNuHWEq__PmXSknDFD8TrNrMGUIWSeJm12e_3qvXpcarkDFnV5bAJH0RGRCxT4ivDH1NSTHkrxwlOVDVLrS7O1htwW1hg2AFAxW907WJ6wkdGwnXeZx6N6aGMZ3JJC4qXbePV5yBl1gy_urDDaUciTbTRbbFDVbLG5T8v2b4tjJIYdpaJYkAbropFAlZQ9VpYXleNcKhvyR3lFpZa_a_9VILahTFPaxvBZ78XSZTgYMDQEHPmVv-9EdsuT4QH5oZen1C_2TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUze5CGm0kddYCd5StsCLZp35V2osZSY-IK0jewPia4qJey9e0aeLOaNu74Kz-cmF_V11e6X3XZC0eC4dkAkSRhqDqzyPNdjmiA0iOvn53QIwi90RoGNuk-5NgN7Ynb35iANRHn2AT5XoMUUKDe5rLkE53kikmrUisuFLo_DgHKF4elLiGurgqWXG6yvAAnRBaZucR_DujXJ5AAuBPDi4sbZCVoLl_JCtx7eEDwFZ5IwSJa93dzVMdpvXaEcOlNvbEPXtm5nwcWwxQS-iBg9tVpbvlk0SIp_jK9QCwbgV0CzrrHN5TrE-B7Vuev_wiOf91zN_Fm0UyxVMpOITh1Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=qq5zZ9w4_TiMQvoSN9rFOs5J55kUp8USxe7O5ukaf96ms_LaztoofaRKX6KGwD65OCu1-db__ifCg6068CtaUsWbjMetfngHudV1DcLZkUCG-eRn8ZThjW8PawdG4YvkSJwYvucbNy7Hs53pCTs2c2uLidvkYf7sgpjkTF0oTPh0HbHjISmMR1oYGgGRstf1F8tWCgw4p4kYhA5fjFe-hlAgjrhlgkcBFhlVNcE_31yFTBioq2Acp9gfx7tR8slTc7F0v_eegZndtXgbx3r4Twwqfn4XjmixcpQGSVQZnCQsSmFrlcZB8ueGGxdIvHSp6nNMxheAPBEE4lzO9D9l4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=qq5zZ9w4_TiMQvoSN9rFOs5J55kUp8USxe7O5ukaf96ms_LaztoofaRKX6KGwD65OCu1-db__ifCg6068CtaUsWbjMetfngHudV1DcLZkUCG-eRn8ZThjW8PawdG4YvkSJwYvucbNy7Hs53pCTs2c2uLidvkYf7sgpjkTF0oTPh0HbHjISmMR1oYGgGRstf1F8tWCgw4p4kYhA5fjFe-hlAgjrhlgkcBFhlVNcE_31yFTBioq2Acp9gfx7tR8slTc7F0v_eegZndtXgbx3r4Twwqfn4XjmixcpQGSVQZnCQsSmFrlcZB8ueGGxdIvHSp6nNMxheAPBEE4lzO9D9l4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OICgjMu7qfcbaqQIDQxy-814LUNHe8z7DzvHzkEgN_JFZEYBiyPHCaLVIajWr3niN9324KV51nBD5Iy-ESY0aflz5eNzOe9S1MSWU5wUAUFXusNIw2MkTPi0_CsQ2lnhBtrzv8eWtyAoL5CqxknMdenvuED3mBY8QTjzgKl2oH7FHKZtlGXx8IyGh4GuBuxS_rz0F_FcVj3U_fFIEN4xIfMwWAZRnO89RM3ZdZD-WWlyFa_r_qH3cIj682AAqO-O7kjBDZzvA8w_RbitE0bDEU46rDqLI9L747_o4eZeDKnUH1u-tLjxkoPZUP4mcOHVcCYh927kSHVLZsqgVYC2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgVN38XEyWkPwZgHCNKxuNuRRorEbD8H0pNhWg2QUQphnpVWtk_duQQHOxaWp9LewftZHuPCDfr8-WLKBnAJHH3FoxOjBdnaxCqBQEdfaUiGmB2I-FUanzm-5t3P60hMJMVLRW9_EiAVv98db0HsmC9ZH_Us77QIBOP9WonYUux8_NBN08DU2S3pKLcAXSfJS91jE-aaPfRevPntd7MTTHlYP85bXKc0Y8l1Hab0M_ssb5Igpa8a6Lz-EbXkMwoiWPg2nbGwZT__1UxFBmietCR4Z3xEUd0aAvLT0WZTORAgTaaqrw0skkDXCdpbuUJqYJddKvGP0Z25MdcfHk-IQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fblBpD3zwloTEITbH9bPKlQxpd9NrAthNHPQ_7qyd7fAnQ7uOJR3PuxnwMoLr4rClishpTjbDXI4ISl310Q3rrk3qoeXAFXAGr8ASQpvwgLSoAc28L4SHfZHteYEC-SZlT2btCKE2bcT4qnv76cyM7upztXbuerxZxEQKH7io3-vnVPdCF0f7cNhcBj-jWVL5RA4uZMnZxKQvRVdAj9WJNkJE8ciQ_5JWF2shVzzVZgEDht8dkJlKHU0lwOS0IpeGY4P94PJeHufJFY6hhCRZqPjiU-u6cjb7Wx0ln6VBeMO1r_YLD6A0ejVMXA7X9xpQHtLM4ARtj1-IWZAd95H3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzsX36bm2ICioLFORAgxrJieQ1EhDJMVy3xZDetl4BB6r_1dE65lWvXh2kxrQjuSlLHx0QDjlz59tqmPgcK_cjQgqSjaZZzFRN6_IiUlY3ko7ni6AmTPvEpDvAo8FlJ2YehTbZ5mVPgiK6eJOcX4JPv4-AC-Bt79Y1aVUQLRmokFA7Dpai_DeFF2oqXklepOf0nOlz9M6mAB07i9YoWIN1yAL86-j4RMfW8jMFkyFLbjiPT3I0-pJx_8KgjGEnw74RCmOAVoDAMywoAtjO_pKCW1jS1GMg9tMiV9TzmDnoJebI9jgHSCaxiyOrB6NdcHjlkau0RPudXAOx5SXHkjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_193wIOPcYd2uRMOebaQKH-gFEqYMdjev_KRG2bnTjdeRIzc0t1zc4RuaN6w2qFsrcSeouOgYO2XYHspMDGiWOwaUrtDsCZUnlgtfxSwB8KGaEVTcVNbwcNgtiOnnGBlFWB2EIsIIxio5dZhRXCdac66J1Pg2-TRy6W1C0XFEsueDsOQBYaZknJYateJmod9MOwRU0zPNVRXyN3fnAF04kOKD8rj0-OekQB5EV-YsT7BdDRoteQWQrE1FgSzeLxYa_B4PYdQ8hLAPWceRGq9oaHcen3tB2WqkpNKk5_kTe_LlUHtv-hR9hm0i3KHJPvkzPaIalIisCXD-gGkz--Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEMlb6S9iXFzpeAUXym-73r6gEn_mQnIKBZK-FWDVbGpZgHJngAu490zVQ30P9iiIysvneTUreOrdsr-19GUNhJAve9sclx5PTSQ1QSXF-iIr_1eODVdIVrxl9VCV2NMsw9K1SGY9YKm7fQAvkMV-zCdxd1C4MM470kgLLdN-vHDL25b5tCc8u-owcA6RVsUOQMPmAdjpyPQU3M9C0LVBkgXcBIDwRw04Lt0U_5UJ27HSDcLUb9FbldSydl60e9O3hfj4uti9OYwxrsARFw2drncftwZ8fRMA2DGQJasN3LJfvA5L5jGdOKJ3IYmHaVaq1STO9mYyaR830fJVFzWOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvBFoG__6GTNetuhZoTf-dTJM_XOkkbVzNDfhI0Bp-WZGc7PviytH9qEdw5895el89iz0zLZG9DvcJvEjaIFrfhQVZlbmQInTbiSvs69h-8z8QNgcC51NAgVacrGcF5Qd2NwBhOaLwwomQIg14F9o-u0lqQMG2IO5XUsIR_TTQ5E1de3-vMCfZ0fIMv4UFRJmmAnd-yLe8DWaK2Di3q0t8Vr-mxSmda6LD50GhWVnsh10FXz49_IJcBidEdsFs0sjSuf5fddmI4VD0_dV59UqaGke8oYryFZUGcDiU7LHWkG-5PsjCBbIHziRNHKWB4iIFUMtrRK6ryt0ReRc4r2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=E6OrAxlnKvKCSBqBn2Mt6HKPJEQUP_7pqCfgxv2KZ5vywS5E9Xmbs6BZjijIPK8pjW4RU4uiyq8_9j0X2gqLA9V8vqlKiBcmRzuALJC4wZVeGN12gQL6QSqG3d1KdcmHGGtnuF4_OvcW8ZU7FHW4Bjl2KL9mUbVpuj_vXR7lSasslbZzadkLUM_moBmWBXr41Tt8mVJ2pPUHBXkdvTa5UcVzj8IsUkRoTd31bt3oJtnqAWiaR2__BsQQi0HkplfIHXnuhupNC4CN2zkLHs8zF_jPElzfayW62CXrdw-vzwGb-pzOtzt7GCmVGt97GYYzxJGzFaVKOOmfnce_ZCTANA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=E6OrAxlnKvKCSBqBn2Mt6HKPJEQUP_7pqCfgxv2KZ5vywS5E9Xmbs6BZjijIPK8pjW4RU4uiyq8_9j0X2gqLA9V8vqlKiBcmRzuALJC4wZVeGN12gQL6QSqG3d1KdcmHGGtnuF4_OvcW8ZU7FHW4Bjl2KL9mUbVpuj_vXR7lSasslbZzadkLUM_moBmWBXr41Tt8mVJ2pPUHBXkdvTa5UcVzj8IsUkRoTd31bt3oJtnqAWiaR2__BsQQi0HkplfIHXnuhupNC4CN2zkLHs8zF_jPElzfayW62CXrdw-vzwGb-pzOtzt7GCmVGt97GYYzxJGzFaVKOOmfnce_ZCTANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLYa0fWmMHPKIxqYX23X6u7_LJqlFNYtnk2bQHystPy6qi_UICmcbY25UBlCAKA_6B1jt-iokZPjAw8lA4gI75J-JKp4YtLesevkqHeot6klXDUm3fkd0GYh1dTTSiSTTz582L_Y-XEt1N3IeXsrXcnBpACUI1DE26Lvu-vTt3HyNyaP0I6LAm0PXkOX7lLxorZ37jbmjUQXZYuReQEXt6L1_-GZDL0epblg28OiEiLz5n8QBV-JA7zY8Q5guG51ZEvEHP86M9uv_SNBsKXOQcjtHPaGvQhlurEUfZ5WMWFNFE4XQuSeUks5klJevw1IGleO4o-7_koh5pM_f7Xa8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th0N2Plscxn87S0N67Z7nJ_QsHp5y5x6thTslFNJWOvfYvW7yCaQ1M8-hcvd64HlDaoh4g3m6Evc2pjkzEhTYcI4mxAwmBZQxa1NZj54lMgUTJ-hz3o5cDIRKq2gNgAE1RDhpG5ntuWnwlgi9k6nbO3TE0izcVIHH4P3wn7ET9EAwWzf9H0MBe6Gu2uXWp_AM90cikmGpzh7TPOQx6wp5WHHmqAnfIZi3t4NlcF1SWiAbd8s4OTzQC2zRSa8spp7sRk49qVaN91i9R294FyrT8yw-l2EwOZOe98b1-8iAUzITTtrU1v7u5-clbnyQMZTX0-4k-C-Ka9UHskSKo2bXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mevCvJ3IKR4AqRGVCD0DajR0afaJS27d1iOxVF7HJETACNnHzhuASgKp4hTwPZ0lpPul3xdQxPyHivZ38dXEzfw_Z5AQt88EFbGLM1Xqst-Vm0tIiUfbyVAzeKNoYnse9VjPBgAlurM_HPGfHyvLn8abA5LRQNVIGKFG5xhIOwZA6FW-ysmZB_PBUXsP9M_HcObG0gVnNhHcO_vR-XmQ38mLUMJwZDkOTnZIFBKdtOsLtdYjiPbxfNKOwhzjjtFbqnQSpFFN5KVAGh8YSC77U0ln9g5ok0BUAMgvcM_Mkc7e34_mbcono0TPH7cColzoZNLPrPKHEIhMqDxp3l51cA.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvNESUC6tv1pBrozPq92njelBuj6tW4CX6rQ5Sa0qP0bfEj2ns5Yc6tWITUst4UVjoFkBf_cfxcNjcSWSH05ynItCYaTAnFjsVT50EXSQQaMb85Jj3c0c5jTsrpJSEiNdAm6qxnpjcENOv4nqMcyBdRZEDenwqHyy2ZUDYz26eT-ztnqz6lcAQcpCpVqkuLGEg372g_-t6HxxWdg8V4P05W-da9B9octUcOfsv--rYs1sRVbTTumax8BoMtfwKPgonrzbY6zlH0rSFJhHOE5-bTYM2rUyvfJ_BbcjB9dKku3EFPieaRCgQn_ikg-IfSIRwjfFMJVao7HRqc-dvd5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz-MDP5AvxOZKaiNBHCMiGZ1OII6QrYKCpNni7AW_lgIgJKUbw2pDxZvfHa9ltcgbGPYzQo--jZsisD0QpAgKotj7HEPcdf6cGltVwNaU7nrthIz4Uh_sV66o6tVr7YzXQvOEaDURQQI_PwyJHYZZbfmTloG9NnyFlBX5J-xydQitU7lv3gxtwW5n3FQOSvdbfolbjfniYO66k5zo2dsZmTbhpnE_A4LS3P0paqPtHA3eRcUOU_wSCey4eGFIcbFGSjwff98ALbplBhzruBsyeDXGE_7gTElQJplRvyfdhilv4a72qgWVgI9wvKRL62Zk20eA1OV6wEXrq15oFHD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCiszYRc69UarJM-Be2p-52unPUUwq5UqY6W2yLOQaqDZoRDTcb5KLIlcAWfsUoPk5CJD9y0Qo9CtVIXAA_9A01_m94Zk1OYN9ekoo21tCRLjVFcbSZRDwbfmB_lkJfqiTjnLZWRKUUIBwEDicJ6-_PaU-pfEWINtuLnyeA5jgPoDVkR6XIQVb8Y2sf8ory1bAD4acjtR-l9kcZ3Jiz0VY1KCbgr44M4nwRpAcJbnzOEjZj76TCnqwS3VCWutnonydptFSdg6vnM5TOPga0YlF7-R4Eo3mcy5CkkT7W328iFdW0UI9i1S5k4N3i2IrKSdn7nb_85CKiTZGcBDe3ByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-OwWU1NsFimB_DiTX9HiEX1vsD0xv5x2JgwG0IqVDH_8vSlRAyDPpJbLVIE6MtgW1ICXuYYFzC7ETi9qiD0NZkXFwMNQNieDpIdf7oA0fNBT6R3Q0i6S1MWY7PfddadyhWc67EH6Z3yOZlaJnL3R8tcUdoXuz1NGuMhC_wWHiof3SAL2-4HnvRljuUjTYLugQBtPoeUHl6YeKOThFvlmjSUbFUaOimN7ykq8gBNvDcuNVz5hwDEySC0W9__RFBo6AxQcwICHNEYs77Bm1YcZZzCRBHGFgVclEOT1BFmUzeAVK1EMyJiltyc4j0HqZwKXXqmfFspJSeDMWsoy2Ly_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
