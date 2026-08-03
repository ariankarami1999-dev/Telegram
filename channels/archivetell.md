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
<img src="https://cdn4.telesco.pe/file/HzrFbZd2VV1kC9tW5uJzbLE7CsN2rPde1YFnWb3KcjgcoE8AWRbBdGYRKQfh9hq6IGCSVy96-1jP9NstZjOnCBhz-ZhhzjYGShxjpNw6oVVNmoapyGqk-7ol2Z7OL2DsmHjJ6BRAbFXPv4MVKtzlZxIkvF1ylOcVBq81oHIywuklTk4WXoIH2DxdFqEb-f6HKKKIBtBGqoF3XlZEWmGvEiT0KsYh4L4HePiZwi1dP4zh-awsvh4ZjZNdcpha4Zsz3f9okccy9qdVgp4Vrq1INIpY7DVENyRwN0rUlkXKc9xCpXvYItzq-EELUPzdhnne9Qanww0Cq3lzQqPSUrkbZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
<hr>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 128 · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOPc-YuZtAa6pX7dYdIeS1QQJsIMeGF4BSCXpiBtOI3cryHue_G22Tze7MoXcQ8yTtWlxf6WzLIWCfV7jEU_N76eHOHGU3VCPbskg8Zz4ysYM3kKS1Mz07vt00hmDfAup6pxtePlmHYSX-nh-mHz2cHYe2CygMsYm5n0Ia295OkZTUhIZI-vNbQL_Bwd9ygJhUPq3G92oPJGYo6ww2iO8uQTVy18qzWn_8gCCvzDKHi0CVwXnT8VrO24eJqsryA9_lCbMaIvyPLs1zdjJF78k4pR4qySjjQxwhkF4TXKwB_DL_t7nfFhmsk9ZR9YbCVr7YgdoSvCF4Upu8WsZ7PbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2L9eCfSJrdqxHm0miUZdkJn6HvcmkAp3nTc3DKl3DNgLlrC5jGO5MPpzB2rzo60ISWKk8z775xH-uAXVR3O4GvqT-jVjFjMW5AfvIVT7Etb2XKA7eqUwpzak1YdlML_s_BwhRgg_AqGdYpDzuR01UA5L8Hi4qXrj7Ac3e_8z0FJRjcJ0OFk8dbw-9mA1lGRmZRtsOVkZXsAwJrLZCFK9BF729ibNPQqDrMEsYaDvC1cyId-bxrA-kwhNQWIR4pfVIf4mP6tYIuc01bpBnlelRYiljT7b6FCl82pipE5BgqhateGi7B5FOUJvr2u9LEzro9BzzPxcUXqwniHe7jwqp_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2L9eCfSJrdqxHm0miUZdkJn6HvcmkAp3nTc3DKl3DNgLlrC5jGO5MPpzB2rzo60ISWKk8z775xH-uAXVR3O4GvqT-jVjFjMW5AfvIVT7Etb2XKA7eqUwpzak1YdlML_s_BwhRgg_AqGdYpDzuR01UA5L8Hi4qXrj7Ac3e_8z0FJRjcJ0OFk8dbw-9mA1lGRmZRtsOVkZXsAwJrLZCFK9BF729ibNPQqDrMEsYaDvC1cyId-bxrA-kwhNQWIR4pfVIf4mP6tYIuc01bpBnlelRYiljT7b6FCl82pipE5BgqhateGi7B5FOUJvr2u9LEzro9BzzPxcUXqwniHe7jwqp_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 719 · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">​
🎁
هدیه ویژه: ثبت‌نام کن، درجا طلا بگیر!
🤩
​با پلتفرم معتبر
طلاین
می‌تونید به راحتی و با هر مبلغی آنلاین طلا پس‌انداز کنید.
🥇
خبر خوب اینه که اگه موقع ثبت‌نام کد معرف من رو وارد کنید، همون لحظه ۵ سوت طلا (معادل ۱۰۰ هزار تومن) به عنوان هدیه به کیف پولتون واریز میشه!
💸
✨
​
👇
همین الان از لینک زیر ثبت‌نام کن:
https://my.tlyn.ir/register?referral=XWZYLZ
​
🔑
کد معرف برای دریافت قطعی هدیه:
XWZYLZ
⭐️
XWZYLZ
⭐️
XWZYLZ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7366" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX4bu6b8oPhKKx6dMsdo1_h6EJXfeV5X9OxBQsb3ZRQM3IeUwP78fQgDVWnpQ35I1gr8gB4f_U3d5qdjwzQzwrHkLdnWj2l_mHpvzAw6ajaO600nyam5Pe8EJOdk-1x4CgA4fLu-_fbkut4fpKjT_U9pVZnQEDKl4q-reb0v3nCU3W1ALsQTyGFRduSL9c46lIRAVF02NV0GDxLmc8BAW6EF-NaS8bIqIPo6vFM3nh9AuoN0c9dogCIXlkPR6ccvWsKYFBEg6lOHxuL3M0DxqFn45ty6bve2T7XCRK1pbAuPUn0O7ItsiQyhE3pmdz3bEJEE8AX4Vizc8Pz-XS_Cvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbHk3wKU8EgVpKb7tuZKgO3n986yttAY2SDvl2o8oBYR9YJUTpkQeCinKXQ-3DID8K39I9d2XnGn6yXFfGnSIWEPxUrdJHN9-u6iS53niG4EKReMVSBcjaBjGxM0T1Y_9kg7s6jVLcTom2kceptYjJZIIkZA612_AHhxEd6qoKXYi_597XT3TH0s-TGy5pCi5at-6o2PH18gSRSf2LNLrCy9_qv4aNKPs9t7c569Y8vOQvh-Xv1d_TsQsicRpi8p9LzYhBt8hSy9_A9Ux08HiftCQ6dypybCfOx7ZFX4C92OrzlboU4WiW9gDf7CttsXRFi58CEFFcfr8LX5_ei9RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0j89rXL7ogKrSIh5qonibX2zjyx4nrKYu7RLVONiM_RAK3lwZEbMLu9b7L2RcsVgRg9bGDYxAQt8SDuZ79plF0u5bw_UXbINqFzAIoaidyRjh3yPr4BAy0aGNWQq_adcB82WRYaCu2gYDS5BXe9f6wz08cJdRcnwjXD5kigjnio0dCh5E7gJSN_pGM_yhGJ2Yo4NcSntX6SupmV_ijhbDA9Uw1S3oHUUczk_Xiv7W_c2QE_OX4J36TU0-KBJBf5VKZ7IT3qnpFqkLuAbJFa48SInInTcakN63c0NhJQXl4rWNPbZ4K8PeNUA9JrS-RvzvuKEkZBtRVMMPN0SUlU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k26p_-C1PNEbymqRH5ND0M7FfCaZD6YJgq5hgwx-vroGqboN_szSaDYxQMdVUeUkpJHponmfsy7Lhp9Vkv4zahgSTNe-6fZ3L5iOIHDpkV3bHWkc6GuBw-KCBWaMChjmxpMCyOnOnuVlJvNTbwvkd3LA4rpCWR_7nPe-9csWE1usvyNOQWHwfj-ImHGf_fxxm4S9wWQqbypJCfW-34wEHnecS3cbPjewAn8Pf6SkCEDmMBDXr4BcQq46zQJeelXdE81wm6EAFOZ9w0WTHGLs8k8472PidUYoYErMZVRrBXD6ODsm_zqFS0k6DtSkdLWy4k4p08E9FiNjPGVfLhzUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgfFpv6pic5LwKSC7FyM22Jx1shrzjoMxwJGKHqPDLNkZZagsVJUNrfIUq5dMkAga1KprX7phKaEU9bB_LqSzlCAEAEx08BMA-h1r3ajM9JrmKz60M9YLYHJ0Xi-57jePtbhT4jixq2dbn5b2A12FpdojDdNeQf29Z3TEfsl6FafEAaKhnHda3QoQbQyTy1Qw8qbFStH0dqjvhuL_SBnixLkucsK-P_cFbOovfxVhp4FEmjP1OApXRqck2HH4v3O8yFwwszWV2YCVMoAQ3T7anWIpXJv2uiVQBGq6o1ugi_jcS9cd8uKdKeNWEJAo9HFw0gExvFgehO7odgq_xbNKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwYcy50yWSsCNa0RYB6H8VgZHQuAJwp4pk04K2RhlY7RcAIayH7Xyy_bS3iRFU0JUE3FbfcY95EI3eI5AeM49Phl1Kv6MdZav7S9M43fBj3bjDdYVIRUQMKdQGNGHiGYM9LPIvEnIyJ6fLP_Bxlk5RAmdWG4Yz8EeHBCfK_QnM4XJqbb_-bQqDDtGfixKtBxo3NL3IHkVxyAW1-dOUDYvIQsYcDdr5psC-8yO2P6QMZDv9ABZyzS1MLYIFBYpzBD5Aj3b7lOTpvzBeXgl6nL5KRJRAYTaokDoCODyntJTv0b_HDrlkmKxwVSqXRgn-mZ3lsTIIr1d6I7f8NAkZw7sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFMeuou7koJ367AOIM9X5iqxuY8-U2M2_t8MSMLk73H4rXJ0CbHxda9PQOil3rzy3db934-HZzW134-Y5Sd1cbh7m7IZfVCFTQFdbDAWRBcUcKlr-D6IP7hHjsWSuxNfTrMrR5IzCDpvSO9x4Eo9bDJyLyLysrhm82o_k-P_tGdbCBrGyIop6DL9rzZum5l2t2yD6kgZcA4V8QT2wI6xXJk9jWVFfF5HwQ4MD7vf5FW_pHyzR9P61kcix86e6bzILXGL9QE0dDUIzJug2ts98Rx3PizO3IP5bNviWjVSXO0MK3ZbrHHpwjB39Xm0u8_vNPJIDe2z9-sJirgbpMM5ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4ubatD19uIdu2sECUtk7cW4S_XhmpoIqouRmgtNh_rwWGtlJFW9pUz258MRJK8xax8dWlmTC7Y_xBcEkdOMFH8vkvfkrJaLJPlYLSpHDRXmylnfzNgnlXcJc_Gp7ELIuapqWj_gjN8UFR0x2EpmTfERsRTQQMropS2vjlW8lVWQiLJGjYuUN_hLlkWuS_cbYmXGnk2a4u8mHL8N4x_jP-WOjadwDMJ8JzUO-5mW5CPsY2X0FSOGsUte7zo-z2xVqfrQV4V-XKzKaiucrg2dFcoj_yAugFj6EDkyHzKnnQPVj2puyjigiYER5nPf1hbivRqgSmvSCMvAsss2D9Wapw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQzsw0AJZ7jcTXJq3LB8ESFdyhq4vbk-W-kDLFKyqr5S_b9RVpsknYmcucNWdQFqXgcLmtC_oDcNfm2lVfdXJ5iFqxJdi5KfnBRoEQ4YQSqBn0bkMypq2iOd3EcLDKR6sAybWl1fIf4laEmu8fuSYmYQeY82GW-QqL2ZXBdI1x1u9u3UnJBzD4TAMt8CmMQhQQ_W2MkUNdkYU-UAbfHTg8aMUeUw8yFhRiHmIumCahBmzZUQ2E8bpgt6mX-7Mf9jEWGiZ75GOnq2TpItFExgiqC063sVYqYeHPZDtNNjWMjVMHTvOP1CFmUwBnWJwMl6tYVW4ku-VCe5BZXUndWcvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9RS_33EQhcPuyq1K6-L9O4Y1AnP-xTX1hkBb9WYOg37hANSQX8IPcB3SjcRXjsPBU3LiDuz9CuUhS9r1VSaksknoK2-bZeed4sY0mHWRNJWWwjFC3IA--HcL1HnSH5qzMX1b9svXq1RvEWlMuJVr-JO_sGfdg4gWWsh6Y_fH-L_R_fcQgdzfxMhfTHnLfPRvzd2kTeLn-w8m9b6KpxmGGfX-byv2ll8j2Up9-CsVCHqp55NjBokexfd224IMF4iN_xeAgMopKo0iIT7FFCNpcTiL_ufoq4A3_5ImhREgXP9shB9SRcRwom5onyJ_8Z4yhKtvj0-9jGgyTffwKUh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tljn68U2iLz2xZtQsqzc7keqj_4Y3aLDr6mIBB1qhPQWFJd9zwSIwmNWFrfNJBubI0Pb-MWMs7E-0oDSJqLiMJQ-k6zm_OtPfx3kBVWbNv2R3K8SkWyPHldhO5bXbjt-z_ZFNB-w5UE3Bso2sm481NskDT022_pnLjjjpHWlHzD-lDYtf0zTNA0pZDR0uV9gA_r1aiOhjTOL2ZAVgol7YiZSy87a8eEJtFRtUZmZ09ER84E-HH9TC6j0fnY0uzbS7FIkWB0aKm_KbGRKarWpujpTgbWenfafX8l1TE8u434m2XXAUcnHJ7Kf2QdmkAY_P1H5B5DcdL3VTnl3i64RrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT7qRBHeS-K-ycBLRzd7w_kwetoEHrkgUDjk05Jnx8ZA3NhepMPtXlxSnKc2U5sJ8H5Q9qZqQhLwTrORLVNJQbwbQZlGnBYqN5kIUQ9Lex_MIEXSwQeny0qnUg1tDEdSZEtfuDYnVahdmo5mAcuEFzNvCLyXNr-xbc4jBDKQoqIQLhHJgdqtvXUdNjZQC_-eiJpl-qHK9lGKkDxfBrHgieQ7HEsFlT-ZlHZA0p2smtaSQXWDXHA8b0-GtZ9874bl3dD_e0FIkYXoZyPeATu1neIf_HWf1SA5T88t-bH-dhQBmgyi0dotHvjUgpUTWUK0Me9z7RS00nhHRmgAGBdcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVNCw__TZTn8T-TahiAnW0uEGNcLmonHYbdiRtwBrqPSRqTfIqX0mIdEAVyIjhOhZOTTsAXtDqeKyBNMH7ERRtlgr7r1HVqKC37FS8AuwFjpqFdxp7KBh7EVxCXoH8h9shBxVJzVwAEz1aDRuBQ7lKQCy33TDziQm6WQaDhygzWvC8ZZDueA89aD0jX7D0clYQTFpRJ3HelVunnwVB50UypwMRXBveNhP27f80aVRThFMBJDLZmNnZ0Azog5pk92sgKy5BH0V-7HVt_Di26wY1_Ka62Ra7WuFbvRmZ2UZhIPqYuRAQ7xVRKhy40dI9tphRGlyE2A7-wzsJ9inmGTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9LgG7nlVe0x2RFORAsoXthBf0IKvsWbmjgrpX3ymMSGdTcNnON3CWGTC2zeOm-C_5wc-CLY9_LL-J9mhunJ-q1T_DjD4UXcCacJis_t-d2Hjq-0LY0OADHlLIbY1uPtK8KJF7KqiASoK08WNL2VyB_FMzI41IK-Q8zsLy3xMou-a0-PyzjIEipFbaPutqX1rJ_-N2i6a6CAoxUKZbrcMlDX7MMp-KfeJQGCVwzFEtjnhAEARTbtNGRakc4ydLpOpPQPTw2EKqSpvZeFUx4ivXGgHyfutGD0KJv92g5ZKe-EmsVIPupVmlZgDhy-pAZ2j0oLuRFXAIo360cAMumu7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXaoz5xdsY7JLyX85a0zpCPwyaqhgw4jq0lC6mFf5unjMmazrkn-TB0gqu03zOEK86QCKRnmTjU1oCE9u3ssEgCP07OfceMlJ5CHr3XsyfgHM-64C8nQE5CUBop1ISsJvaeC-rvndImpE4ro0ing37-kzn_sSyuUVHbQJe6PSu5QxRwPF4g9mTf7-vYUvm9c9R_P47C0xLi_lgFrewpqyE365IeFzyxuszors9gOXn2t7KrvAA4ZTSm8cwX0BJzaB6G1B7Iecv_8c6LzB8jIgVdOExtXYBs5RApa92U9Hime9Me72sEIaYxupknG8A-Hc9gJVsN2wdn-AWfrjpIJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5ZmKQCND5F4SvSYi8d3mOS8Wqg3DcBbd29v24q5FrHtHfIdL0TSM1VeblYOwZPOWRZj1THOprHJOjxeaBzl26ZMowQAR46vxAGiKHFXtqYl-Lse_IN0QyEkM_IsBM4lnbg6JVMswjeGyYhUIN_xK7PsCoi8SFIBdInYc4s4yfS1TQ9aXvz7GxGAzjaZ175xh2XJsLu1AYxTcAXcjGaPwcJnBTytxLtDPBe9DP7cScCCzIyfa70pe5h0ZKkGp7hMM2Zifun7R-ezBeAbwf0DNcEY4Bi5vf9ct_uWk-CrwMkwaiBtarTowtIRfjepGhIQrwNPdNNVZCakaGbOwUv-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP37e4zyM-Z_zEwLywwANEzwO5GZNLQE_I_0FT8TbI91-MJxJp2yoSH4OWIzgX_k6Dmi7_SKbNNO5OJAT2dIZ__vkyNaNEqS4_9zU2NPbg-ReW6t5J6w7gR8ejMIum0iYmnXfx-Lnh71S9anThJKiDzwUASfkYra6u3pwVL73xFUqYNOAis08Stl9j9g0iK8g2bOjh4GWeXk3mfV5cMmCj4_oN9Id_Sf9A2A1Vm4zCn_YWNRj-6tRZXptgAuCF6ml7B7p_Zahzj4zHpK6FGkxWlVEHN95v72kofV8NAqANbzJxDHwlpVEjf1paEW6R-Lhw9Yjitp_QqilNGl3KRhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBxx20pZMDHdPJVmf-aPAqfkVKTKNsxvixnz4wu-8DcFcSPOd2PeDZacYM-8rceXiMCVIYZ3DMwj741ZqVAbYbjChCaBDUtO9gJjnr5weWkOZuAbUzM-fsNNr2QlH04qeui4oMGIMspkzCILCv99I-k_ZsDd2hw09PvctMxIkhF78e1j-5e6erueGuHg83G1LG9o5GO57O1ri4F3Bh7U4O7_VNgdjeXlgMEb5sl4Nugzt8TIoA74kHDZ2Kg7AYdhfJF9OahsZDaJLgz_Yf4nkzrCZJS_7XKopkQbIhUWxOVtoyU2d6S3jyFardFpCv4P27b9uHuAGlsZKsHrCDoU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVsGZaqPenPDkjAQPTQMFmomoevOKu7snABSPFvHs3EKJDPf583wYWfm_5nu1IUZ76KTeId2DG4O3fZlh6C3ktiDVSCQ2RVIhrgNGOCfUJMvRv8mygV1p8KM8EWcx5qpTGYdSJ6LKOLgPjvtRcp8tOGYU9gdu1wY3I8_JWoiadSBYE0SJU3ebP3oktpvCZYBNAmxRS7gQ-KgHJj6GzxJODnlVFxgtth44bbETkaNrckkh69sPHf2jLo8n2peE-wf7SnUkTEmccd0GJvFfZs5YXzSbdwnYnm9iHrbjt6ufvc0Omwc5nFzJcMLo-3gcyuTh0nKPsa5BjSLn3wzP-RtWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojcHQo_uOWNOaGTTxMLypzrEqXzJgYJsLNhvq7TYMMMnm5EOtCDsh3tMRo7AXU9T9mX4y4Fpa6uMllEqZnn9MDCEnHuwLR-5G-ZyU0dAuyzt2YdPUmWXOFfkQx1YbdpX5RdLRF83DPCLFCfa0ypmud2wuySHhkeg-QaQuA2S5UhZKZH6ec8ukYw69klKv9-3KB-2VlSdIjSr5PtSveHXr5fKJTdBcXd9dkb1T6do1QSAnyyiOnHrvLcpedQC_HsVTX5-DX6ZJBHhHdj9IPMQlVvOCsplakLAsjUqfxH7VMHWNJvLYa4-yTPYGJ3frjIm8ajIEmCOwwG7_hc1uWHzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvSVhJWMJFg2FzW834y6qBhtgZz12LJGkXHk8eHy3XKNKnvHk8MVprzNARwoUQ0yqcyD8CdpWCU0VKlgjpQ4Jn2x9-P-q4I7bihowhI-ykbEAG2A-HRgs4sNPa40NdICPG84N98LwsP7YfRoFWrn5z3Un0_VpxyxmajwFvPhJ4Wb2LWmjn-ZhjsYzBYkPyZF4qSVDFKScPtmrcDnlBWN4dP_cLEQ5xiOQxvjgERmKRpi-7vpiQDw3tGClHS5TshSMhG9-EE9PfSVsmnUT0VMITYcSNYPOTn2UqAV4sIOfS0bmqP1auB_ROtQm0Lzf9iZJ3jc94O1QVTE8wxMw0La5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hykn97nqAe4LhbqEMQzLBbL0SmcIHSOxerKJ7mE4zXPklIxpREZ8YCr9TmZVB9ZmXz1Do_T3GPXSvNeP1lGdKD60os6NGlc6kL-lHzh_GdtFF1jbMtxoswVwzzQLRq3ScX292tDQ_nIXbr5gNLt6WK971kf6eRA4tK9EjuerzYdeCB6AQediLTkBU6YcLlUOb4ECU_vPyXqcMSUKfC6hxEYTGjU4huw1-0YxkjK-DVBvmZmLokr3kOWY-8W4W3HubFnTBbkuoFTMnJzrz5euaymacbQEy7o_Piz2STwGIc0A_Q-olYT945UJDgL3GS10EySYe3Np5gzTKORlNJ-lWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F08AL13IEsc4slnnVeyuh8cLN60GfP4x90jyqvk5GdtQcLrkrFAK9Mbnzi6FrzWJMJ2b2rdYX2aaCPT0Xrc2JQt8nW2p6PmRGej4kcyjG9OVy-HWcBFzfg7Q1b-Fg0rDU--kwUweY17zDiSNCvcXbEzw8lK52GkxZ05vLstv2afw9giYnRo3aKuxhFJ1bZvxnQG6B9DhE-NU65H9sgknPPysn3T1cC7QEzXwyi7eaTDy96wWC_UFIrCV1UwW7imuQH9KrJFBcBPPKdTyvSYwIwvAMV23jD01cSxdp3XPsL8wmfhbCy-70nHMIxlWGGs8FZRWGHFpn0yUNQzXoHTrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/preqa88fCG58py4nydr9ddTiKfUEH5XbT8cfM99lcYLMqzPWMxeJgId5c7GgK1DeFnaWHDYJHmWUhDCErjSTN1k2MkwunrB7bZAG7n2Wzr_fOngaEsWnIivmfZ7XTsYcQjAQwuVXmdAUZR814myvzkHI89nrZHdajasuPv15UxibWnzEcLrGvpzv6ZD1FRX5ywWhHhfr1hblW4jJGfttGsUiG2fk5PUmWWydBLlI1gsmdRlzdaAkxC7vFfRg5DDybq4Tp3nJDd_5SwLne2l5-C1-4Hqgt-V-ffZe8IAERmmWuB-NbMJ4EYnuCPMuxLwbV8OpldpPKTBBzUcT9aDVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuEXW5c7EC3Nfu6ognnZEyszmS4RzMgYZMr057Ko4cf8FZmjpZGHPIvgD0MuL4GoWgCNnmLwxxyJQbxR_Qm7BJFF8gAbfmdRw9SsaiI3w9ShFzS_8Vt_ISusqXqtxbxq5lIozrqQPUjVyiJr_Me9Tk-tT2XlgNYv53__9iBAqlN-I44BKl74yqTRhwwIbGaUnfHxl7MZhIW9ZSlkA7hm-EnHFtZxMVypTego5qBPir0w0dhutZwHnl13G1UdqOjYt1spo_zUPVnsl2vO5k8rm4Ga6dQSuRHyPGuUbfV2T4gqN0p6vg-K9qLELJ6BSaEh676BxljsBVdsOETE0O5_BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8LuncGRXmHjAdmUmAiigd3n5vbrKHb9l-_yllLXlUS-3OrSWES15L4TqdPjpmF6o9HuLKnBCyMDxniqyKyCi8oLu34ia1z5FIEYuSPz074zRYVyUfRHUY9KD1xyE57lnYnm0__2etZsYO1jNaWh79z-1-SdJ-3loxIcPyEA8j3MUmwvo9qkvpS6eB8pmEL7zhJPGBZRy8gFMmXf1RHhJqz7stcWKTMwJvzTm14bii4urnX_ALs7KTR9pkjNbI26TjkufxoImE4iMasaOZw62uUGt1LOpmpxDMvcw7vNoepwYsGBrc_d8X_-b867Kq9sxyphTknui1e_aHOxnUsOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش شدید قیمت API مدل‌های GPT-5.6 شرکت OpenAI
💸
📉
شرکت OpenAI هزینه‌ی استفاده از API مدل‌های سری GPT-5.6 رو به شکل چشم‌گیری کاهش داده؛ اونم به لطف بهینه‌سازی کدهای سرور توسط خود هوش مصنوعی (مدل Sol)!
🤯
✨
خلاصه تغییرات قیمت‌ها:
🔹
مدل Luna (اقتصادی):
۸۰٪ کاهش قیمت! (ورودی: ۰.۲۰ دلار / خروجی: ۱.۲۰ دلار به ازای هر میلیون توکن).
🔹
مدل Terra (متعادل):
۲۰٪ کاهش قیمت! (ورودی: ۲ دلار / خروجی: ۱۲ دلار به ازای هر میلیون توکن).
🔹
مدل Sol (پرچمدار):
قیمت ثابت موند، اما حالت جدید
Fast Mode
بهش اضافه شد (۲.۵ برابر سرعت بیشتر اما با دو برابر هزینه).
🔹
راز این ارزانی:
مدل هوشمند Sol، خودش کدهای هسته‌ی سیستم رو بازنویسی و بهینه کرده که نتیجه‌اش کاهش ۲۰ درصدی هزینه‌های سرور و افزایش ۱۵ درصدی سرعت تولید توکن بوده!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR3_hjKNAHMhyNqr3oBGczmo2XjLTXljS56uEe5nbmM6gXB6yOTN2rPXqAr40pL2fm0sJ0vbCaKguis8FxQoqDuP6nEWH_c2M-qE_0SuwVfA5IGAIqTbougujrNdueyWppZyNgraag8fnNdlxiXPnBb6SA-sWk_4ypXUt1nR6I-zIRqnflk1ntJwCBPf0hRpPjExZTASgAF8cEsETSydR7SJBZadQoYXIDVy5DvYv_wCwq2lYd_XarUbgdNC93_DYZ2BTWMEnch7yamWz1ftfwpgQuEOfZtzRJk4SjVpF2HnI2grVZeuoJAY2gKWhLXnw2ynNur53MJc5HSvc9B6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت ۱ ساله Pro سایت
Beautiful.ai
(رایگان)
🚀
🎨
بچه‌ها این سایت یه ابزار عالی بر پایه هوش مصنوعی برای ساخت اسلاید و ارائه‌های حرفه‌ایه؛ فقط کافیه موضوع رو بهش بدید تا خودش کارها رو انجام بده!
✨
نحوه دریافت اشتراک آموزشی (EDU):
🔹
مرحله اول:
با فیلترشکن وارد
صفحه
بشید و روی
Claim EDU Offer
کلیک کنید.
🔹
ایمیل دانشجویی:
ثبت‌نام رو با یک ایمیل
.edu
انجام بدید (می‌تونید از سایت‌های ایمیل موقت مثل
tempmail.id.vn
کمک بگیرید).
🔹
اطلاعات دانشگاه:
برای اسم و لینک سایت دانشگاه، از یه هوش مصنوعی بخواید اطلاعات فیک و رندوم بهتون بده (سایت گیر نمی‌ده و قبول می‌کنه).
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpqv-cEWisa9x5rQnAZHWfu-ZECp2rwpbaLU2NITbOCKBM_mI8Cvxbhq8tM9JOZVQapybI7RDX2eBYflLOlF98HYXMbPqb04RAD8mZyziH0lQuyvylu7eTeI_cl8bXvZapo9felcySN4j7mZkKR7CoPSa8-6Mj2C_NqFgfrEmY1m-JYvn59qA3Yyavih7RxH7J9hFxrn_dYAbO544DoX5t2aTPw0-l5gNOt1H-ETSiJu92OOvXL43q2z8qu8KVvvUEK56vJZxT7NFs8G6r8aqi6IUCmTGd8SJpSAmdu6oN46jT_UT0NnXDqHsnCTyWuvLftV_FeCcvPO8sn9Mwh5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی ابزار PDFx؛ ادغام و تفکیک هوشمند فایل‌های PDF
📄
✨
پروژه متن‌باز PDFx یه راهکار خلاقانه برای مدیریت اسناده: ترکیب چندین فایل در یک فایل، اما با حفظ قابلیت جداسازی!
✨
خلاصه ویژگی‌ها:
🔹
ادغام و تفکیک:
چند PDF و عکس رو یکپارچه می‌کنه. این فایل تو برنامه‌های عادی پشت‌سرهم نمایش داده می‌شه، اما تو برنامه PDFx دوباره به اسناد مجزا تفکیک می‌شه!
🔹
کاربری آسان:
مدیریت فایل‌ها فقط با کشیدن و رها کردن (Drag & Drop).
🔹
دسترسی:
دارای نسخه وب و دسکتاپ (ویندوز، مک، لینوکس).
🔹
دستیار هوش مصنوعی:
پشتیبانی از مدل‌های OpenAI، Anthropic و گوگل (با API Key کاربر).
📌
[
لینک مخزن پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiGfQGh3yU-jRyexQl5UvsagUVv4k544R4pjdNYIRGDdMWecod3jJ14IA4zYF7kKcTcOa4QKCCVLNE8phY-HrxA8j2PrnYQbur5Y3FrbG3Xk4IuIKncnzhxhNP0VxQGf48hOzkNeBGFlI-Uvc135G0znY6lnq9NCTAQCXu_XHYygqlck7_3ZNlHPV5W3QhtyKW143sA-QKhUAgxBo-KfEcdHAA_9-rEq_Fya6P2yeVwMvI853ZdlsvWS9BccVaZ5Bk3pTaQHJF7WgZdNbierdlpKaQkZHgEXC4HAUJZ03MuQfzhISBZoXGcOjwk60cpM4zylmQ9LdhzRGkcMSw6--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید پنل 3x-ui (نسخه v3.6.0) منتشر شد!
🚀
🔥
نسخه جدید با تمرکز روی امنیت، پایداری و رابط کاربری بهتر منتشر شد.
✨
خلاصه‌ی مهم‌ترین تغییرات:
🔹
ارتقای هسته (xray-core v26.7.28):
(نکته مهم)
ساختار
finalmask
تغییر کرده؛ اگر قبلاً از این قابلیت استفاده می‌کردید باید پروفایل‌ها رو از نو بسازید.
🔹
امنیت بالاتر:
بسته شدن دسترسی آزاد به فایل
openapi.json
، امن‌تر شدن توکنِ نودها و مسدود شدن دیفالتِ آی‌پی‌های لوکال.
🔹
لینک‌های سابسکریپشن:
تشخیص خودکار نوع کلاینت (User-Agent) و قابلیت جذاب چک کردن وضعیت آنلاینِ کاربر مستقیم از لینک ساب (با اضافه کردن
format=info?
).
🔹
داشبورد مدرن‌تر:
بازطراحی کامل صفحه اول پنل با گراف‌های تمیزتر برای مشاهده زنده مصرف سرور و کانکشن‌ها.
🔹
پایداری دیتابیس:
اضافه شدن قابلیت بکاپ‌گیری زنده از دیتابیس (بدون نیاز به خاموش کردن پنل) و رفع باگ‌های ترافیک.
📌
نصب و آپدیت با همون کامند همیشگیه، اما
حتماً قبلش از دیتابیس بکاپ بگیرید!
#3x_ui
#ثنایی
#پنل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkRlW_bVZLMZmWhY88OsJmIEPm3OrYIUONJrkfgkuuDDcNK5llyye3LRbtLQNjOj4EobG0dCkB8ScBgrdD2aWFNeB1gLfY36pBBJ7X-WfKkWShfn3V-0y1Zzuz-TDJkdi0b2odwY8zpBgY6wQ3gN_a8q8jAMAsJAA0v5LIPrdbxjF25jZLExJ2KPPKzI2mQdppQaKDksHPWLf-3arjZBIfIkUfIF2ORywHqM2g4dWEj5vmPPQpDNz22QUs3TXpFo0BBbUu99gQpykt7lTN1FEQpJyLml5RC5RgzfkhJxtgJ9imotttvY3-dsFNQBKTEPixrGQmtXGGNW07OzVCXChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک ۱ ساله ChatGPT Pro رایگان برای دانشگاهیان
🎓
🎁
بچه‌ها می‌دونم این طرح به خاطر تحریم‌ها و نیاز به کردیت‌کارت و مقطع‌تحصیلی بالا به درد خیلیامون نمی‌خوره، اما اگه دوست یا استادی خارج از کشور دارید حتماً براش بفرستید تا استفاده کنه!
🔹
مخاطب:
اساتید هیئت علمی و محققان پسادکترا (Postdoc).
🔹
شرط اصلی:
داشتن حداقل یک مقاله در ۳ سال اخیر (در سایت‌هایی مثل arXiv).
🔹
تایید هویت:
نیاز به ایمیل آکادمیک (بدون VPN) + کردیت‌کارت (بدون کسر هزینه).
🔹
مزایا:
یک سال اکانت Pro با حفظ حریم خصوصی + ۴ دعوت‌نامه رایگان برای همکاران همون دانشگاه.
📌
لینک ثبت‌نام در سایت OpenAI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StG3VZsKsFD4FJMt3u0Fyie4BtngkC9ZxT0Du0cfI0RuOW97Zf8dvUDpfc2kKoQQmNG7Zuhd-_Mf6FPjg13lyEAFCAcQggkKZMlqA6sJxy2LQK8FtIQB-iQR9csWxigLi9zGTYCRpDBunMl9GZUr0abUJb62m2oCOxAD4RXl3lPToULtBYHm_VZuBOYZKd4KSgvYIscWtSrOihe_U1xwH0s4BKy_Opo9ia8DVClio5KvbLFK2OvqxJrKcBl3_Td646yoa7kzV8fWTbkCqkc3-53_EDC0qNQA_AHMWPa3_w2y6Enkp1k6Dt0myqsdFA4FAStZTU4TyBkhxd1TMxGIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از Grok Voice Think Fast 2.0؛ شاهکار صوتی جدید ایلان ماسک
🎙
🚀
شرکت هوش مصنوعی ایلان ماسک (SpaceXAI) به تازگی از جدیدترین و هوشمندترین مدل صوتی خودش پرده‌برداری کرد. این مدل مستقیماً برای پردازش سریع «صوت به صوت» (Speech-to-Speech) طراحی شده است!
✨
نکات کلیدی:
🔹
قدرتمندترین نسخه: به گفته سازندگان، این هوشمندترین و قوی‌ترین مدل صوتی است که تا حالا توسط این شرکت توسعه داده شده.
🔹
پردازش مستقیم (Speech-to-Speech): ارتباط صوتی کاملاً بی‌درنگ، که باعث درک بهتر لحن انسان و کاهش شدید تأخیر در پاسخگویی می‌شه.
🔹
رقیب تازه‌نفس: کاربران به شدت منتظر مقایسه‌ی عملکرد و سرعت این مدل با نسخه جدید gpt-live از شرکت OpenAI هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تغییر ظاهر لینک سابسکریپشن 3x-ui (پنل ثنایی)
🎨
✨
پروژه
MiTemplateSub-XUI
یه کالکشن عالی از قالب‌های مدرن برای صفحه اشتراک کاربرهاست:
🔹
تنوع بالا:
بیش از ۳۰ تم مختلف (سایبرپانک، مینیمال، شیشه‌ای و...).
🔹
پشتیبانی از فارسی:
کاملاً راست‌چین (RTL) همراه با دارک/لایت مود.
🔹
جذاب و پویا:
نمایش انیمیشنی مصرف ترافیک و چیپ‌های پروتکل.
🔹
مدیریت راحت:
تغییر و نصب سریع تم‌ها فقط با یک دستور (از طریق اسکریپت اختصاصی).
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSnTNkU_zRwup7IB_UwvZM4FwQx4AUuFXodhIQQhcus5x6TPgBKmWkeGhBK-eWHAAH9Ukk-8OanHH_s-ZlZYNFnTat6bCJd7sQHKD5jUWBKsFQwI-1yqXAfDdB1nIglLjIxhqKIVkf46AJDK9-SDCVTLAm9osiHb2eUQ94Sov4iCKD4TIbWGS5xUQohDVwiWM6Qzi2gCH70QD4iC_tSrhgu4fZ-KWLn9oD4WZssWWcctuUbPy1VyuA4enWktzceXpH8AjCMuk8AI3aYXfPxezZFLe3C1PUymDzs02kgoyyjxCMKGzaYC4v6AM6ark-S6M7Afrzpb5XUsB9biaAYMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ابزار ‌Onlook⁩: انقلابی در طراحی و کدنویسی!
🤯
‏اگر طراح یا توسعه‌دهنده هستید، ‌Onlook⁩ دقیقاً همان چیزی است که به آن نیاز دارید. این ابزار مثل یک دستیار هوشمند، فاصله بین «طرح» و «کد» را از بین می‌برد.
🛠️
‌‏
✨
قابلیت‌های مهم:
‏
🔹
ساخت خودکار:
تولید پروتوتایپ‌های حرفه‌ای همراه با کد تمیز.
‏
🔹
تعامل دوطرفه:
امکان اکسپورت به ادیتورهای کد یا محیط ‌Figma⁩.
‏
🔹
سرعت بالا:
صرفه‌جویی چشمگیر در زمانِ طراحی و فرآیندِ درکِ کد.
‏
🔹
رایگان:
دسترسی به تمام قابلیت‌ها بدون هزینه.
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdNKdB3_-od4nn7KqFTsWQao6Mah5xNzN0_XwO8misj4_50NLqNJuwnFoYI6VvXu2CGDngnsST4aTdB1AeOi8wE_EOfItlY0TD8tgB3W9sizixgn8XrnL2ETQ1Q30uOAcUGruMALRM1xHzbsANbrqh5kd8WG8fnMrm9EPoqsgF0zM2Laiae2_-VzXdDjX0riLz1H8SXMj4oXXFH1zLTK-SicEwEqQP0xUXPJOMjFVzPfTbNtppk7SS5F7WBBAh4YXbzm11YiDqQZh38EnHa2MGsqdHraLd2YOHzPkqgP5-jqn__3UGCbSrMozsz-DIsGLP5ArzECkWRoNpkfIRtJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
گنجینه‌ای از هوش مصنوعی در دستان شما!
🚀
‏اگر به دنبال پروژه‌های آماده و کاربردی هوش مصنوعی هستید، این لیستِ طلایی شامل بیش از ۵۰۰ پروژه متن‌باز در گیت‌هاب، دقیقاً همان چیزی است که نیاز دارید. از چت‌بات‌های تخصصی تا ابزارهای پیشرفته‌ی ترید خودکار؛ همه چیز در دسترس شماست.
✨
‏ویژگی‌های این مجموعه:
‏
🔹
دسترسی کامل به سورس‌کد تمامی پروژه‌ها
‏
🔹
تنوع بی‌نظیر در حوزه‌های مختلف (از بیزنس تا مالی)
‏
🔹
مناسب برای یادگیری، توسعه و شخصی‌سازی
‏
🔹
پروژه‌های تست‌شده و آماده‌ی اجرا
🔗
‏
همین حالا از این مخزنِ ارزشمند استفاده کنید و سطح پروژه‌های خود را ارتقا دهید
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7307" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7306">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-SsbVSWuvgNZK_6TG0xSybkgCqtp0ftsoqDdYiu66hdMVu82Gnzw8OFHnUkheaa80rKCLu03LQjMINMKWP9Ff7El03T8U_Ptft4PY7iEPpOy1sRm5PDS6uBmtoucPyd0532VgjIEEYmoNMcU3aPvSV33BGizNGsspI8vouXbJDA40-8Sy3qIkzxxjJqKgPYN47LUBzs5cCzr-wBP365zG4XSjmGiYCjB1YVfDW0SahIpTEab-2r9JkSftlirFc6KnEkHtVrjSa0aYCV05PobC8HUI7I6Brq_9_dJkIwAWbT4DGqSShP1SqtWVaWPVr_ddtyXudro2S7vs_8m0NUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhSN0SVhaqKTUWOueOOvy-NQEbehdO4nhx9HZV601t92Vmp4whk5tF7KZZ0nb0pQsXZlgfbzDLPNG5VC9z_ZhmLBXPgM8o0DpnmGDTpOG6S77Mx_HGSffFdeiWkBk1_ZpslzclrADSd71oa8-TPqIlv7lPiSPdzEtE79we5pWIXoMA-K-HU35-KFTYMIVL3uc_rqNo_GuB3miaIs9iBF1mKwzLaz9LsmlDN0gA2sVFrkvPIUHesiOkEU4EyB45gAxEc9jZUvVElmqXfyHLWycpuVpbdbwUNlZ9-bUHgv-CkTQUIM3len67ad3oHjptBTAmCBezoq_BQDeAyLO1cOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOA83IBf6P6PieKvxE_upnlJl914Y1UbIqQEB45U1ZKDrEU55SVzl4zpf8BVGgFyhRqL3nxBbtrraT3CdPzeGVFHPeEig12LQQIQyqXEbWF42JOQYD0paLdaaMQw99ZhuP1AJIoLFw0vZHEtzLQ77e2vX-EiTkm-CKnBwslOmvzmAYTNteh-DdExdNvgoUUlOT7RBdZOoIOr94um7yczbzWnbDBV5qleCRQoWAmILc71F5norbky6ECW71FIYGMXpJr7NVzT1NjTnrKyiRWV6Jrg-8x9BeYl4RQ_V0m9uIWz5ud52hMYprx6kY3rRGf7tuihf1dHlHLsRfzNW9UcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌APK Converter⁩؛ پلی میانِ وب و اندروید!
📱
🌐
‏این ابزارِ آنلاین، پروژه‌های وب، فایل‌های ‌HTML⁩ یا بسته‌های ‌ZIP⁩ شما را مستقیماً به فایل‌های نصبی ‌APK⁩ یا ‌AAB⁩ تبدیل می‌کند.
🛠️
‏
✅
ویژگی‌های کلیدی:
‏
⚙️
تنظیماتِ اختصاصیِ اپلیکیشن و آیکون
‏
🔑
مدیریتِ حرفه‌ایِ امضای دیجیتال (‌Signing)⁩
‏
📋
نظارت بر لاگ‌های ساخت و مدیریتِ تسک‌ها
🔗
https://gentsergame.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJcZEQkN7APVMlrMPkrAHNvsO9FJp0s53PDE43U4jocRdN3uwzXm9TnI4c1AqX9abv67h5UWlokbRJxzzqLKNluJTdvR7zQ0g7hnTd5cLcl9Ab-ItV8_gN6xmoEryzbA9ClRRDcpR_-tv-v6gtcXj9djJJ6lDTN2AMfHbeVNtDSS8Toi33OJe7XnQt_4s93e-4CmFmqmoHGkFiEHmnb_bdaLZqdh1Y_1NS4PNGxSUFDxAjv_TJl7kkTCJqfKGodMckX_mg9UkRz-gLHIa9oys7ErRykclPSqKXaYhDRT1v5dBV7fjmVr0jcWpy7akUZclVTGYmviD7MUjDbBrefcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
انقلاب در کدنویسی با ‌JCode⁩: سریع‌تر، هوشمندتر و قدرتمندتر از همیشه!
💻
‏اگر فکر می‌کردید ‌Claude Code⁩ سریع است، ‌JCode⁩ با سرعتی ۲۴۵ برابر بیشتر، استانداردهای جدیدی را تعریف کرده است. این ابزار نه فقط یک دستیار، بلکه یک «تیمِ کامل» در سیستم شماست!
🐝
✨
‏ویژگی‌های کلیدی ‌JCode⁩:
‏
🔹
سرعتِ خیره‌کننده: ۲۴۵ برابر سریع‌تر از رقبا با بهینه‌سازی فوق‌العاده.
‏
🔹
مصرفِ ناچیز: هر سشن تنها ۲۸ مگابایت از رم شما را اشغال می‌کند.
‏
🔹
معماریِ کندویی: ایجنت‌ها با هم همکاری می‌کنند، وظایف را تقسیم کرده و کد یکدیگر را بازبینی می‌کنند.
‏
🔹
حافظهٔ هوشمند: با حافظه سراسری، هیچ خط کدی در سشن‌های مختلف فراموش نمی‌شود.
‏
🔹
سازگاریِ کامل: پشتیبانی از تمامی ‌API⁩های بزرگ (‌OpenAI⁩, ‌Claude⁩, ‌Gemini⁩, ‌GitHub⁩ و...) و مدل‌های محلی (‌Ollama)⁩.
‏
🔹
خود-اصلاح‌گر: قابلیتِ عیب‌یابی، بازنویسی و رساندنِ کد به کمال.
‏
🔹
تجسمِ پروژه: تولیدِ نمودارهای درختی برای درکِ عمیقِ ساختارِ پروژه.
‏
🔹
مهاجرتِ آسان: امکانِ وارد کردنِ سشن‌ها از ‌Cursor⁩، ‌Claude Code⁩ و غیره.
‏
🔗
دسترسی به ابزار
‏
📂
مشاهده سورس‌کد
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfLo26NEuBbAtz5-qlk30r6Zequ6_H0V362lxwKPbLhNibDxVEHVneglmDP3bM5ivgFpO6mExg-aHmToWJt9-GSLjYdGkBuedcNJ6u-GF0oBPHghJ5WLzLhWtIiC-be0UORXbO8i865Rlv6c0PS11L5rzbngpRDPJeC-RohJx7zDZVXNM_yhH4Bh-UapmZ8f29R1lP6hsGG_2jy3eOBdKHWAXGrwn8Gn5b-sjwjy9IsnSFhosM9pMkiwyKOByhIKwHI4noap6JlzX4M5NGNafOdcZvnHQpFop8k7vuP-SDXw2r4vbi5ORw2ayH605x3049xEFjI9RzQJ8H6nkpyQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
70 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Opus 5 | Opus 4.8 | Sonnet 5
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
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
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o24O8KtGbnJNEXUSAIQnoPxEisF46myfL4sECLdo85uD3NFg6EKpzhbQ5YD5NUwjuR0siisr1jNZFrorZM7nzBkhpWWwdE6XGtiUclq3WU99mpA8BEDqgS0IRl4w0W2LDw2h3L8FVRnk8ItC2IWwibuEFTHYq8_MiepNMegkrVzXVe9NhLLWG65mjaeRR2FuQ7aywlBZVqyWhlQW4ntu5DSIcHZJJWv7GdTSG5ZmaXcZjTBX9hbyi6fmF__C_2pJHFCpCWxvsYT3RJA7E7QE6wiG4ScfwtC5ZDAVT02owmMIIcgZgCp19pXK7VJOb3-vui7OD1UlOZmN3i9Uval7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام جدید و عجیب علیه پاول دورف؛ حبس ابد به خاطر ربات دوست‌یابی!
⚖️
🚨
یه خبر عجیب تو رسانه‌ها و کانال‌های روسی داره دست‌به‌دست می‌شه! ادعا شده کمیته تحقیقات روسیه (СК) پاول دورف رو به خاطر عدم حذف ربات معروف «Daivinik / Leo» (یک ربات دوست‌یابی تلگرامی با بیش از ۱۳ میلیون کاربر) متهم کرده و شایعه شده ممکنه سر همین ماجرا با مجازات سنگین یا حتی حبس ابد روبه‌رو بشه!
🤯
✨
ماجرا از چه قراره؟
طبق ادعای بازپرس‌های روس، سرویس‌های اطلاعاتی اوکراین با ساختن اکانت‌ها و پروفایل‌های فیکِ دخترانه تو این ربات، در حال فریب دادن و جذب نوجوانان و جوانان برای انجام فعالیت‌های تروریستی و خرابکارانه هستن.
اتهام اصلی دورف اینه که چرا با وجود این مسائل و هشدارها، این ربات رو از روی سرورهای تلگرام مسدود و حذف نکرده است.
با این وضعیت و اتهامات امنیتی به این سنگینی، به نظر می‌رسه فشارها روی تلگرام دوباره بالا گرفته و فعلاً نباید منتظر کوتاه اومدن دولت‌ها در برابر پاول دورف باشیم.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dockerfile</div>
  <div class="tg-doc-extra">35 B</div>
</div>
<a href="https://t.me/ArchiveTell/7299" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!)  با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز: فایل Dockerfile ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱:…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!
)
با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز:
فایل
Dockerfile
ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱: آپلود فایل تو گیت‌هاب
۱. وارد سایت
GitHub
بشید و یک مخزن (Repository) جدید بسازید.
۲. اسم مخزن رو
railway-3xui
بذارید و تیک
Add a README file
رو حتماً بزنید و دکمه
Create repository
رو بزنید.
۳. تو صفحه مخزن، دکمه
Add file
➔
Upload files
رو بزنید.
۴. فایل
Dockerfile
(همین فایلی که پست کردم) رو بکشید و آپلود کنید و در نهایت دکمه
Commit changes
رو بزنید.
🔹
مرحله ۲: نصب روی Railway
۱. وارد
Railway.app
بشید (با اکانت گیت‌هاب لاگین کنید).
۲. روی
New Project
➔
Deploy from GitHub repo
کلیک کنید و مخزن
railway-3xui
رو انتخاب کنید.
🔹
مرحله ۳: حفظ اطلاعات پنل (Volume)
(اگه این مرحله رو نرید، با ری‌استارت سرور، اطلاعات اکانت‌ها پاک میشه)
۱. تو صفحه اصلی پروژه تو ریلوی، دکمه‌های
Ctrl + K
(تو گوشی روی آیکون همبرگر) رو بزنید.
۲. عبارت
Create Volume
رو سرچ و انتخاب کنید و به سرویس متصلش کنید.
۳. در کادر
Mount Path
دقیقاً این عبارت رو وارد کنید:
/etc/x-ui/
🔹
مرحله ۴: تنظیم پورت و شبکه
الف) آدرس ورود به پنل:
۱. روی سرویستون کلیک کنید ➔ برید تب
Variables
➔ دکمه
New Variable
رو بزنید.
۲. کادر بالا
PORT
و کادر پایین
2053
رو بنویسید و Add کنید.
۳. برید تب
Settings
➔ بخش
Public Networking
➔ روی
Generate Domain
بزنید. (این آدرس پنل شماست).
ب) مسیر ترافیک فیلترشکن:
۱. تو همون تب
Settings
بیاید پایین‌تر به بخش
TCP Proxies
.
۲. روی
Add TCP Proxy
بزنید و پورت
8080
رو بدید.
۳. یک آدرس TCP (مثل archivetell
.proxy.rlwy.net
) و یک پورت ۵ رقمی (مثل
14841
) بهتون میده؛
یادداشتشون کنید.
🔹
مرحله ۵: ساخت کانفیگ تو پنل 3x-ui
۱. لینک آدرس پنل (مرحله ۴ الف) رو تو مرورگر باز کنید.
۲. با نام‌کاربری
admin
و رمز
admin
وارد بشید.
(بعداً از Panel Settings رمزش رو عوض کنید)
.
۳. برید بخش
Inbounds
➔ دکمه
Add Inbound
رو بزنید و این مقادیر رو ست کنید:
@ArchiveTell
Protocol:
vless
|
Port:
8080
Network:
xhttp
|
Path:
/assets
|
xPaddingBytes:
5-70
Security:
reality
|
Target :
www.samsung.com:443
|
SNI:
www.samsung.com
دکمه
Get New Keys
رو بزنید تا کلیدها ساخته بشن و در نهایت
Add
کنید.
🔹
مرحله ۶: اصلاح و آماده‌سازی لینک نهایی
۱. تو پنل روی
QR Code
کانفیگ کلیک کرده و لینک
vless://
رو کپی کنید.
۲. لینک رو تو نوت‌پد گوشی یا سیستم کپی کنید و این دو قسمت رو جایگزین کنید:
آدرس بعد از
@
➔ آدرس TCP ریلوی (مثلاًarchivetell
.proxy.rlwy.net
)
پورت
:8080
➔ پورت ۵ رقمی ریلوی (مثلاً
:14841
)
تمومه! لینک اصلاح‌شده رو تو نرم‌افزارهای V2Ray بزارین و متصل بشید.
🚀
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7296">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrO0ISPV_veYRD5dLwqbNcxLVcOwYhdJIi1e3Z-P_Jd4bTGgCQ7eqAfITYCwZ206QF_BWryMyJWNkazX8XujjXTcwyBA_aYCQWbVx_WPAZ5uWQpsOziLWj1XC31EA_gFokXawD_NXCuUHABW8OzREJgRcgQUoevUOt6xPUNkEIcYsHqAvkrACG8cq5kikm_BfjnMAjWV3A_6wPsFO7G_mi4j9jMtZ32n2kr9FRrWS7dPTu9pVhau9XeTeNS2b5qIF1bbKgGVKSfBOEX1DyWHHK02IvU1qQyi54tdP4ikuIazIP6hEnCr5Q0e0NZ1Qh7zhFnIxSsCa7J5dTFvUvhIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
تبدیل گوشی Android به وب‌کم با VCamdroid
‏
‏با
VCamdroid
می‌توانید دوربین گوشی Android را از طریق USB یا Wi-Fi به وب‌کم مجازی Windows تبدیل کنید؛ مناسب تماس تصویری، استریم و استفاده‌ی دوباره از گوشی‌های قدیمی.
🚀
‏
‏
✨
قابلیت‌های مهم:
‌‏
🔹
اتصال خودکار از طریق USB و ADB
‏
🔹
اتصال بی‌سیم با Wi-Fi و اسکن QR Code
‏
🔹
سازگار با Zoom، OBS، Discord و Teams
‏
🔹
اتصال هم‌زمان چند گوشی و جابه‌جایی سریع بین دوربین‌ها
‏
🔹
کنترل دوربین جلو و عقب، وضوح تصویر، فلش و تنظیمات رنگ
‏
🔹
پشتیبانی از Windows 10/11 و Android 7.0 به بالا
‏
‏
⚠️
نکته‌ی مهم:
‏
‏برای اتصال USB باید
USB Debugging
فعال باشد. عملکرد برنامه نیز ممکن است بسته به مدل گوشی، کابل و سخت‌افزار دستگاه متفاوت باشد.
‏
‏
📌
دانلود و مشاهده در گیت‌هاب رسمی پروژه
‏
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7296" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7295">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT0AdP0xCczXR73u3lma2UIkkiyJ5Z8CQBYFeqyDU7emA2pIWwdEHDKyJVUTenpBqDvicgI1dyOxx3hz-Qegb5MR4G7u-3DrOPd5IgLB3Q177p5Bjf14Kt8GHj22NRTm54As-mzzOPPM7maIO4563VT541-GMyFmq2IYhlYCsOxdK1sESxP49xR9j399zO7XAolsw81UsirvUYUdtfYp2TSjHS4FCh8S0VqQ6hLtDzAl9yMVRH_hJE1ceMZ_vRVQVR7KTodGGSMHaIoXX5vnmZgAKYlI-Rdxv8JQTKakuGMcMcL6hFdQsJ0zWT7STYay8h4Dle7Fe5oQPbVBWNOo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
Shotcut؛ ویرایشگر رایگان و متن‌باز ویدئو برای کامپیوتر
‏
‏
Shotcut
یک نرم‌افزار حرفه‌ای و کاملاً رایگان برای تدوین ویدئو است که روی Windows، macOS و Linux اجرا می‌شود و از طیف گسترده‌ای از فرمت‌ها پشتیبانی می‌کند. نسخه‌ی جدید
26.6
نیز با تمرکز بر قابلیت‌های HDR منتشر شده است.
🚀
‏
‏
✨
قابلیت‌های مهم:
‏
‏
🔹
پشتیبانی از ویدئوهای 4K و 8K، HDR10 و HLG
‏
🔹
ویرایش مستقیم فایل‌ها بدون نیاز به Import یا تبدیل اولیه
‏
🔹
تایم‌لاین چندلایه با پشتیبانی از رزولوشن و نرخ فریم متفاوت
‏
🔹
ضبط صفحه‌نمایش، وب‌کم، میکروفون و استریم‌های شبکه
‏
🔹
ابزارهای اصلاح رنگ، Chroma Key، Motion Tracking و Stabilization
‏
🔹
پشتیبانی از زیرنویس، تبدیل گفتار به متن و Text-to-Speech
‏
🔹
قابلیت Proxy Editing برای تدوین روان‌تر روی سیستم‌های ضعیف
‏
🔹
نسخه‌ی Portable و بدون نیاز به نصب
‏
‏
⚡️
نکته‌ی مهم:
‏
‏Shotcut بدون تبلیغات، اشتراک ماهانه یا محدودیت خروجی ارائه می‌شود و به لطف FFmpeg از صدها فرمت صوتی و تصویری پشتیبانی می‌کند.
‏
‏
📌
دانلود از وب‌سایت رسمی Shotcut
‏
‎
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7295" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7294">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AADalHFggKQJCN48e-0nj5IsjViZ39jgXHC7qK8Z6yLw0uDu2c5t_BN3XYM-Geg0pJ6RcQj5bg9t4owlQ5ERkh_VNeuKGXWQ1U6GN4mxz6pYj9FgCuBjNcgLPEco0Hyt5aAF7zAo6VYcFW8M5Cr6ePdwmXhheJMYerjjrJrwL7CCoH_PvZ9uf2y9WAPuocPK2eH-XWUkEAGL6GPSmd0W_Z1oArl3tIQ93CkOSXCjB5JMTYV8xB4V4GQ5tr7G1rLD6WlItjhTfHbKMHUmTnOAWUX0hxdoOPD4_jXjnZeKmyQ22ys88eX1LR62rNXHDloIKloGs65Ao4Zbh1UVz9z6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌CocoLoop⁩؛ هابِ هوشمند و امن برای کشف و نصب اسکیل های ‌AI⁩.
🚀
‏
✨
ویژگی‌های کلیدی:
‏
🔍
جستجوی سریع و دقیقِ مهارت‌های ‌Agent⁩
‏
🛡️
بررسی امنیتِ ابزارها قبل از استفاده
‏
👥
جامعه‌ی فعالِ توسعه‌دهندگان و کاربران
‏
🔥
دسترسی به ترندترین و کاربردی‌ترین قابلیت‌ها
🔗
http://hub.cocoloop.cn
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7294" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7293">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=XT3Sha1LwLbuwiWZlHGsZXzn3nbBcniDo2zrGIHxe4_DKYrylUQ6zzCqBsVxdPO2dcCw9y51m1Bz2rWj4VX7j9YITSi5IzSB0O3KD2VW4wS9v-2NiFayUoUC3sRsXKNYBbPG6nEJ649989MGYT6NuSYVRW5aISysd-hdEeV3FFLR5yid4xlWeYp3GrFWbUOziEaNHELFIXhzfUy4_G8_lS6n5OxlQgmCAL76u6eY6xK40M__mMmylY6YvrGfXFwvFNV3xeNL8Wmzhq5FGoN15gZK-6769OBhMS52X1m7ynT3Wl9sQBwLtqZZr8Gw6-eL1T3m2e6OesuIHRCPL_pliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=XT3Sha1LwLbuwiWZlHGsZXzn3nbBcniDo2zrGIHxe4_DKYrylUQ6zzCqBsVxdPO2dcCw9y51m1Bz2rWj4VX7j9YITSi5IzSB0O3KD2VW4wS9v-2NiFayUoUC3sRsXKNYBbPG6nEJ649989MGYT6NuSYVRW5aISysd-hdEeV3FFLR5yid4xlWeYp3GrFWbUOziEaNHELFIXhzfUy4_G8_lS6n5OxlQgmCAL76u6eY6xK40M__mMmylY6YvrGfXFwvFNV3xeNL8Wmzhq5FGoN15gZK-6769OBhMS52X1m7ynT3Wl9sQBwLtqZZr8Gw6-eL1T3m2e6OesuIHRCPL_pliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ابزار ‌PromptCard⁩؛ کلیدِ رمزگشایی از دنیای تصاویر!
🔑
🎨
‏با این افزونه‌ی کروم، هر عکسی که می‌بینید تبدیل به یک پرامپت مهندسی‌شده می‌شه تا بتونید دقیقاً همون سبک رو در هر هوش مصنوعی بازسازی کنید.
⚡️
‏
🛠
قابلیت‌ها:
‏
🖼
آنالیز هوشمندِ تصاویر
‏
📝
استخراجِ دقیقِ دستوراتِ متنی
🔗
دانلود افزونه
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7293" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7291">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آپدیت 1.0.4 کلاینت UAC-SNI-Spoofer</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7291" target="_blank">📅 18:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7290">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkdQYq1oTS9CC6_AgF0WL7J3OibXXkiMBd-PWRIcjyXFUps_F5iO65aruN-Vo1CP3MScrBDA94kukJYRivAUQinkI6OuVH_gKJOp2iFnjxsMWiWrQRAHLxuVzHM6G2_qU1Wv2tJJxwqSDWvcl28kfdq7YI_JcAoilM7Jt_IQo6q6A8by4s_-gsx0bOXk_sZHvCwqC0SApmVW6JBH6XZ_LSZGwjBqAn086l2O4Po4SgvGIHeHcT9IXA2sc1tDWIsxuR-oreo2Q2r4noD7oEE__yh7z4emRn4BNdJghLXsNHgZxFgQkpU4EAWRjs7znTpkKmnh7ge7qsmfjz37JkQ2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  ایجنت روتر (سرویس API چینی) امروز علاوه بر Opus 4.8، مدل‌های GPT 5.6 Sol و Kimi K3 رو هم اضافه کرد
🔥
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7290" target="_blank">📅 17:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7289">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-rJg1uILA0YqL3HUIv4pTXZrZSqwol2_F3LyDWSd8gbt9lh2VIwwu17oQhr8vBCeEls6Av2s-pBeBDo_c7r95By3Uc8CvnO4pZWX9qic6BF-cA7oo733aoYVELlAzHjObkN6gVSYt1YMHp-2vW4ic35vg4FlnRSAPFOx5kSSm5PGxFzVvdNqeOuGiy_R0-n7UUxK4cl_iBpSwyJhEg2BbdFLkvOXniSM1-Wm8DRpCVoPM2TXPe1kDX7e9FI-ty-JrP3zo4qex_89KEFxUkZDROxoERAiqtNxxw-XsI0xwEjs1d9MIFMdPxUacocmOgKce8uAk_YAyTuaicFvY723Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💸
جایگزین‌های رایگان و بدون اشتراک برای ابزارهای محبوب
‏
‏سایت
NoSubscription
مجموعه‌ای از نرم‌افزارهای رایگان، متن‌باز و قابل‌خرید با پرداخت یک‌باره را گردآوری کرده تا برای سرویس‌های اشتراکی، جایگزین مناسب پیدا کنید.
🛠
‏
‏
✨
چه چیزهایی پیدا می‌کنید؟
‏
‏
🔹
جایگزین ابزارهایی مثل Photoshop، Microsoft 365، Chrome، Premiere Pro و Zapier
‏
🔹
دسته‌بندی‌های هوش مصنوعی، طراحی، برنامه‌نویسی، بهره‌وری، صدا و ویدئو
‏
🔹
فیلتر براساس سیستم‌عامل، قیمت و مجوز متن‌باز
‏
🔹
ابزارهایی مثل
ONLYOFFICE، DaVinci Resolve، Brave، LocalSend و n8n
‏
🔹
جست‌وجوی سریع و بدون نیاز به ساخت حساب کاربری
‏
‏
⚠️
نکته‌ی مهم:
‏
‏همه‌ی ابزارهای این مجموعه کاملاً رایگان نیستند؛ برخی رایگان یا متن‌بازند و بعضی با پرداخت یک‌باره یا مدل Freemium ارائه می‌شوند.
‏
‏
📌
مشاهده‌ی کتابخانه NoSubscription
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7289" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7288">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید ‏نسخه‌ی جدید Aether 1.2.2 با استفاده از شبکه‌ی Cloudflare WARP و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.  ‏
✨
قابلیت‌های مهم: ‏
🔹
تحلیل وضعیت شبکه…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7288" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7287">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQaPacAvi7ITZODHrO8QnszX_aPXmp14PRQAh3pbE0J5C8yezVEXWSF7pe8byn0pk8XBjSbzl25GNXt31UxlsR_8C4A0mdxT3dNWLpfKeDdzx9_DOWycyOA-cgBBd2VqjkL5k8nQkwGT6VU_YK37f_HBTovEOT5OirAvcGYDL611bZ4mzwtclD-a5J-08ncVjOwbhZrM3ISU4hr1OehUaT1FRyDPvKXDw0mu4BNxk3u4IXxY3ZaaeyJeNSSLP9TZz9yoiboxHD3g_AzbNj44Wd7v7rsmtIgyfCli29dfSxrDxb9gMs1VSjroNJfhqlfERo7rm7iXO5SBG6j-DbVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید
‏نسخه‌ی جدید
Aether 1.2.2
با استفاده از شبکه‌ی
Cloudflare WARP
و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.
‏
✨
قابلیت‌های مهم:
‏
🔹
تحلیل وضعیت شبکه و انتخاب خودکار بهترین روش اتصال با
Smart Mode
‏
🔹
مبهم‌سازی ضد DPI با
Noize
، TLS Fragmentation و ECH
‏
🔹
انتخاب خودکار سریع‌ترین نقطه‌ی اتصال WARP
‏
🔹
اشتراک‌گذاری اتصال با لپ‌تاپ و گوشی از طریق
SOCKS5 / HTTP
‏
🔹
پشتیبانی از
Split Tunneling
و حالت Proxy
‏
🔹
کاهش مصرف CPU و رفع مشکلات اتصال، قطع و تغییر پروتکل
‏
🔹
حذف آپدیت درون‌برنامه‌ای؛ دریافت نسخه‌ها فقط از گیت‌هاب رسمی
‏
🔹
بررسی امنیتی کد و رفع آسیب‌پذیری‌های مهم
‏
⚡️
نسخه‌ی
1.2.2
بدون حذف نسخه‌ی
1.2.1
نصب می‌شود و تنظیمات قبلی حفظ خواهند شد.
‏
📌
دانلود و مخزن رسمی پروژه
‏
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7287" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7286">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟠
❌
اوپراتور های تلفن همراه به اینترنت بین الملل ضریب ۲.۷ دادن یعنی مردم اگه ۱ گیگ اینترنت مصرف کنن اونا ۲.۷ گیگ ازشون کم میکنن و اینطوری بسته های اینترنت فورا تموم میشه و مجبور میشید زود به زود اینترنت بخرید...
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7286" target="_blank">📅 15:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7285">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ظاهرا رو بیشتر اپراتورها فرگمنت رو کلا بستن، البته باز بررسی کاملتری انجام خواهم داد.
در حال حاضر برای دسترسی به اینستاگرام و یوتویوب به طور مستقیم و با حداکثر سرعت میتونید از MitM-DomainFronting استفاده کنید (فقط نسخه وب).
* اگر از قبل از طریق فایل certificate_generator.bat سرتیفیکیت گرفتید، سرتیفیکیت شما بعد از ۳ ماه منقضی میشه و احتمالا الان نیاز دارید که سرتیفیکیت جدید ایجاد و اضافه کنید (در نسخه جدید جنریتور این مورد اصلاح شده و دیگه سرتیفیکیت منقضی نمیشه)
https://github.com/patterniha/MITM-DomainFronting</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7285" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7284">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO6qDk9KjiW2gYrR2W6qDUgqJp7GRsEuB4ZKMNvKyNjIUxvYLwTga5vFnsDFA6Q15PX1gF3-uCJev--GLtVvcvylyUi_EFnjBBkPbs9y2guxMK_mfxHNlsHRO2WnR_W1a3ZT_OTLJyYZuXq08rQHVvIjYfJylb_VTWmjgYRmYHyoSdnYIp5obVu6XEB657U2nJJ6a5XLBRXC5NgndORnfwKwqO9xoCutfThrkG_E1PdmPsBhEn71aaCjgIVyz7W8GKlsOFgO1dIoMfAlc8jLNE-1H7GlmDrqIBCFXYaNvzjYHdxYUPb1_lv19MajSC4D7d_sRFRh9dEKnrVnfCCWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لو رفتن اطلاعات جدید از Anthropic؛ مدل Fable 5.1 در راه است!
💣
🔮
طبق جدیدترین شایعات و لیک‌های منتشرشده، شرکت Anthropic توسعه مدل جدید
Fable 5.1
رو به‌طور کامل تو محیط داخلی خودش تموم کرده و احتمالاً تا ماه آگوست (همین ماه آینده) معرفیش می‌کنه!
🔥
✨
نکات کلیدی این شایعه:
🔹
زمان عرضه:
احتمالاً بلافاصله بعد از رونمایی احتمالی GPT-6 منتشر می‌شه تا رقابت سنگین‌تر بشه.
🔹
قیمت‌گذاری:
ادعا شده قیمتش هم‌سطح Fable 5 باقی می‌مونه و افزایشی نداره (هرچند همچنان قیمت اکانت‌ها و API برای تست‌های کوتاه و چندتا ریکوئست ساده، سنگین و گرونه!).
🔹
وضعیت رسمی:
انتروپیک هنوز هیچ اطلاعیه رسمی منتشر نکرده، اما منابع آگاه می‌گن مدل کاملاً آماده‌ی انتشاره.
باید دید تو این مسابقه‌ی نفس‌گیر مدل‌های جدید، نسخه ۵.۱ قراره چه ارتقایی تو قدرت کدنویسی و استدلال داشته باشه.
#هوش_مصنوعی
#Claude
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7284" target="_blank">📅 15:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7283">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqg8byEyiDh5md1UD6cKYBYJkod3jZSvLdPAmFOx6_k9uaLY3rsUmIu1JlekdsH3YszrgaogBfxcwm4PijW-nZEmscgCDZhD-MrX7GoDxr0mnzgXf8fk1tBt9T1DShVWmsbflq2cBMcXzOUYdQobdgHRTneRt9W_iprqbTMUC6Q2gDCszzQ46UGIMbxg4Y4uAxk_DEou8vinHfCJJcAOsAyIoUBZY79Dhd9IpE8P2lP7zDoTBaKSqia-ZUpp6rQKCNNXyWZj-M3ssOXpnlgn7_HdXpXag_CLW7n-5oLqzpRUKZ-t1KJt74n6J2Ai3Va4gzjGRvwnyQKR3i8asUZMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فعال‌سازی پلن Professional برای پلتفرم Figma برا طراحی رابط کاربری وب سایت و برنامه اندرویدی با مدل های زیر :
GPT 5.6 | Opus 4.8 | Sonnet 4.6 | Gemini 3.6 flash | Gemini 3.1 pro
برای دیدن آموزش کلیک کنید
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7283" target="_blank">📅 14:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7282">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVU6GmQICGlLprP22MY4G6fqiZT0vlfF8eMCBj_9Z30_l61TA0RPPlCIyM_XJOa7xhitwljuFgMMzd8mGliT8ZacKfpraQlXrOXgnpLlnvSDpzG-5ADzibHq99CBJzRFAbP1Fe8TYO_HWknN-v_4l2ThtIRfgzzzABHHBPue_z8h2MLsuuOUPdttWICfHeZkMBHG6idYeS-vb8EQjdJsDbdEqDK7ospdfsl0y_rawp9-MMprf3d8-ARc613wJ4aHSUyGSgB8ndbQghh0j2QSm26tIg4Qrdq6BO8A8QvBWs_ygOq4uvFdKQoNA-c-eTBz7KzylpZ6KyvzjKAOa6sP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه
low_delay
(تاخیر کم) و
high_delay
(تاخیر بالا) هست که با توجه به وضعیت اینترنتتون می‌تونید ازشون استفاده کنید.
⚠️
پیش‌نیازهای مهم برای اجرای این نسخه:
🔹
کلاینت شما باید دارای هسته
Xray-core نسخه 26.6.27
یا بالاتر باشه.
🔹
در اندروید، حتماً از
v2rayNG نسخه 2.2.6
یا جدیدتر استفاده کنید.
🔄
نحوه آپدیت:
اگه از قبل سابسکریپشن رو داخل برنامه‌تون دارید، فقط کافیه ساب‌لینک خودتون رو آپدیت (Update Subscription) کنید تا کانفیگ‌های جدید (نسخه ۴۶) جایگزین بشن. حتماً نکات استفاده داخل گیت‌هاب پروژه رو هم مطالعه کنید.
🔗
لینک سابسکریپشن (برای وارد کردن در برنامه):
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
❤️‍🔥
@patt_channel_x</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7282" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چند دقیقه دیگه قراره یه آموزش بفرستیم دوباره از همون متد باحالا هست
😁
❤️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7281" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چند دقیقه دیگه قراره یه آموزش بفرستیم دوباره از همون متد باحالا هست
😁
❤️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7280" target="_blank">📅 14:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7278">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABVY_WDgCVaBYv0NU2-VsXtbzEloS9Z2ROSf2ZzoggNHCJbpKu0Bzil9OQTgl-ubC9jmNHhj5wezc2wbawbGijP1A0fjFnyc-xYej5sbG9PBXYcdpgNSJWLuqRY6H6kPyyt4Nu0qpmNBD0RPss8LexakgMVI2SW9ffMP4b4pelXO2Ylf5XNOxOVyYGY_7YB9DCXoFHr-woxPT4hj05zUQVcBR57Z5MiQeJQT02s3clPjfIwK4rn0olJZdRvmbHJiZ1Jen76EeQSgmcfSYKBKpRoRsu4-uFAscKFihUnNYfognrJNVtTLmQ1GTw0356kDUOyqWIHfrn-3JFZEy9J2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی ۱۴ روزه به غول‌های هوش مصنوعی!
🚀
💎
‏با پلتفرم ‌Lumosel⁩، قدرتِ مدل‌های تراز اول دنیا رو در اختیار بگیر. این فرصت طلایی رو از دست نده:
‏
🔥
مدل‌های در دسترس:
Fable 5⁩ | Opus 5⁩ & ‌4.8⁩ | ‌Sonnet 5⁩ | ‌GPT 5.6 Sol⁩ | Kimi k3
🛠
چطور فعالش کنی؟
‏۱.
از طریق این لینک ثبت‌نام کن.
‏۲. برای وریفای، لینک ربات تلگرامی رو کپی‌کن و استارت بزن و در کانالِ تعیین‌شده عضو شو.
‏۳. دوباره به ربات برگرد و با لینک استارت رو بزن تا پلن ۱۴ روزه برات فعال بشه!
‏
💰
مزایای پلن:
‏هر ۴ ساعت ۱۰ دلار اعتبار و ۴۰ دلار در هفته برای استفاده از ‌API⁩.
‏
💡
نکته مهم:
‏برای استفاده از این ‌API⁩ در ایجنت‌هایی مثل ‌Claude Code⁩ بری ، و از یک فیلترشکن باکیفیت استفاده کن تا مشکلی در اتصال نداشته باشی.
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7278" target="_blank">📅 22:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7277">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به به
🔥
🙊
دیگه جای عسسسله لامصب عسسل باید بگیم لوموسسسله لامصب لوموسسسسل
پایین کامنت بذارین پستای وگاس لوموسله لامصب
جعبه شرودینگر وگاس ببینیم از توش چی در میاد
تا دقایقی دیگر
👇
Clock is ticking
🫣
🔥
🎲
🪄
🕦</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7277" target="_blank">📅 21:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7276">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏دسترسی رایگان به هوش مصنوعی‌های قدرتمند!
🚀
‏می‌خوای با مدل‌های پیشرفته‌ای مثل ‌GPT-5.4 mini ، ‌DeepSeek V4 Pro⁩ و ‌GLM 5.2⁩  کار کنی؟ همین حالا این فرصت رو از دست نده:  ‏۱. در ‌Boltch⁩ ثبت‌نام کن. ‏۲. کلید ‌API⁩ خودت رو از اینجا بساز.  ‏
⚙️
تنظیمات اتصال:…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7276" target="_blank">📅 20:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7275">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHhM2PA9-_ozxD5f1xbzUP3MOpkG5pOUVReq80SQapnvzKrqD3Z1gjE3xXh_J55XPPS6v9lDhkBhi5BeuprxUL3nhPOLn6uAn42LYMMml_9un0N89-6dgTO5G8oaHrNkg78NeQDxm5piF5B15_2YMszzHOXk3wuIRd-WdLQqBY4mHIBSiU2mMh-eLJnBS3VuB1QVUkMvNrSOk-swp_6Y8RdXMNMK06mNCrI1H7z5zvATV7l2wRCZvq0EvluXQfiZQJONLW4xMsGst6VpVd1Fzkr7PJUjwsgjwiQKMhivuOd_SL5Pgj6d5v5W00-EL5rP-6TWHpoWkgHSJ90-D4HElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به هوش مصنوعی‌های قدرتمند!
🚀
‏می‌خوای با مدل‌های پیشرفته‌ای مثل ‌GPT-5.4 mini ، ‌DeepSeek V4 Pro⁩ و ‌GLM 5.2⁩
کار کنی؟ همین حالا این فرصت رو از دست نده:
‏۱. در ‌
Boltch⁩
ثبت‌نام کن.
‏۲. کلید ‌
API⁩
خودت رو از اینجا بساز.
‏
⚙️
تنظیمات اتصال:
• ‌Base URL⁩:
https://api.boltch.cloud/v1
‏لیست مدل‌های رایگان در دسترس:
🔹
free:glm-5.2
🔹
free:gpt-5.4-mini
🔹
free:deepseek-v4-pro
🔹
free:kimi-k2.7-code
🔹
free:minimax-m3
🔹
free:qwen-3.8-max
و چندین مدل حرفه‌ای دیگر!
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7275" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7274">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان گلم
❤️‍🔥
این پایین تو کامنتا اعلام کنین که چه چیزایی بیشتر علاقه دارین
بیشتر ازون پستا بذاریم
البته برای همه سلیقه ها پست میذاریم ولی بسته به نظر شما سعی میکنین بیشتر اون سمتی مانور بدیم
ایشالا امشب یا فرداشب ی سورپرایز خفن دیگه داریم</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7274" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7273">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyXbE18Dsq2tA04Sw4USP9likOTRyYSyRKlt9jFyNvX7AstY8LB2IL6LcvNhEDm5Ip9POepw1Utr1uL6xzLxfBxqS2RpkDv94tfEwQdFmwRbAH_3iaJY858tQU48oZhgRCSooqf0IHaw48Ra5qsD9TvatefqaHqbqFkcpNz26xrs9iyw5GpiwL93--IeJ4g-fGyWvbOXymePH7VgKqq-aihanvAQC3VrMZfXlnBBD979B5r0Dbetz2BA3VXHz4EFZjW11fVd0c8m9XwGwNZjLeFhVDvCkIoA7B0x5R1TVEyuYwErczNo3-1wwNHLbvZEQTdTI_Fjk2CWT163v8Ye9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
یه اصلاحیه کوچیک درباره پست متین و بازار سیاه APIها
بچه‌ها متین تو کانالش یه پست درباره بازار غیررسمی فروش توکن‌های هوش مصنوعی گذاشته بود. کلیت حرفش درباره سوءاستفاده واسطه‌های چینی از اکانت‌های فری‌تریال و بات‌های ناامن کاملاً دقیقه، اما یه برداشت اشتباه کوچیک توش وجود داره که بهتره شفاف بشه.
متین نوشته بود که از این شبکه‌ها و پروکسی‌ها «برای به سرقت رفتن اطلاعات مهم استفاده می‌شه»، اما تو مقاله اصلی (نوشته Simon Willison) اصلاً چنین چیزی مطرح نشده!
sometimes through stolen credit cards or chargeback attacks.
یعنی این واسطه‌ها برای تأمین هزینه‌های خودشون،
از «کارت‌های اعتباری سرقتی»
استفاده می‌کنن.
هیچ کجای این متن حرفی از دزدیدن اطلاعات شخصی یا دیتای مهم کاربران زده نشده.
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7273" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7272">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noY-1I6luYfHqiL5Bv8_WNlC_D1ifXQa45bnLEbABlI40IBdH1x3o5ynKvktqkv6IyUMf_MzwVgxoH4Qre4bei7_hju2arQ6HKmYNtQDkp17FtPNy2CXU0Kow5rpnZs6lXilnE67_4bmCe2MOtH4zRn9VEfCLiqGEYgH52ClhSqVEnrVyF-HbIf2fP8YmtDHzyN7fW1WPqJL2C9z1RlUuF_u_gtGPeNo0bAd_JicVmNYxy0xTpo_QoGlK_MfnZz7ELvFlWjokeNaBJCECSZ2kyoCsMEdnDeZEPndoZvS2tHko8ToxjsRfMddCsWzViuwCiLxnlfwGnOMCRkaeGOsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سورس‌کدهای کامل دوره پایتون (PY4E)
🐍
🎓
بچه‌ها اگه دنبال یادگیری پایتون هستید یا دوره معروف «پایتون برای همه» (Python for Everybody) رو می‌گذرونید، این ریپازیتوری دقیقاً همون چیزیه که نیاز دارید!
دکتر چارلز سورانس (csev) تمام سورس‌کدها، فایل‌های تمرین و متریال‌های آموزشی این دوره (نسخه پایتون ۳) رو به‌صورت کاملاً رایگان تو این مخزن قرار داده.
✨
ویژگی‌های کلیدی:
🔹
دسترسی به کدها: تمام کدهای استفاده شده تو کتاب و ویدیوهای آموزشی در پوشه
code3
قرار دارن.
🔹
متریال کامل: شامل فایل‌های تمرین، تصاویر و جزوه‌های مرتبط با دوره.
🔹
امکان اجرای محلی: داکیومنت کامل برای راه‌اندازی یه پلتفرم آموزشی با Tsugi (برای اساتیدی که می‌خوان این دوره رو روی سرور لوکال تدریس کنن).
📌
[لینک مخزن گیت‌هاب پروژه (py4e)]
#آموزش_پایتون
#Python
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7272" target="_blank">📅 11:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7271">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-IhxH3OlLP8KgH25Wl3NAp8wAFY68hTUHcEFcg4L9D11PLB-B839TG2Fxwm5UVe53buid9xUC8Dj1PNUB5h8Jy3j_8uoS_c98-9SyFLp6FeVZV1pAH96TFH0rX8KXOcnwu2CeF-kaXJn4jTxaXtUKcjjnasHxsDlb_Jan4053K5orxBa_YFKWfEfYo-pdg662r5nGna0dxJ3yAdh98t5eys4y1j98CDux9g68L85mJL4zZ4NMfH1oMdJY11RG6h7HOWxRywA5Wm45NTrFJPQMWoMHqdeEY8lRNjFjrZ9btybBdCPghQGre-Rb7bXgK_yH5mlC8pneUxTgusTokU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار PeekVault؛ ماشین زمان و کاوشگر آرشیو شبکه‌های اجتماعی
⏳
🔍
بچه‌ها حتماً براتون پیش اومده که بخواید یه پست پاک‌شده تو اینستاگرام (یا توییتر و ردیت) رو ببینید، یا برای کارهای تحقیقاتی (OSINT) نیاز به بررسی تاریخچه یه پیج داشته باشید. سایت PeekVault یه ابزار به‌شدت کاربردیه که مستقیماً به دیتابیس عظیم Wayback Machine وصل می‌شه و آرشیو پیج‌های پابلیک رو تو چند ثانیه براتون می‌کشه بیرون!
🤩
✨
ویژگی‌های کلیدی:
🔹
بازیابی پست‌های پاک‌شده:
بررسی و پیدا کردن پست‌ها و پروفایل‌های عمومی اینستاگرام که الان در دسترس نیستن.
🔹
پشتیبانی از پلتفرم‌های مختلف:
علاوه بر اینستاگرام، ابزارهای اختصاصی برای کاوش توییتر (X) و ردیت (Reddit) هم داره.
🔹
خروجی حرفه‌ای داده‌ها:
قابلیت دانلود لاگ‌ها و نتایج جستجو با فرمت‌های HTML، CSV و JSON (عالی برای محقق‌ها).
🔹
بدون دردسر و لاگین:
فقط کافیه یوزرنیم یا لینک پست رو بهش بدید؛ کاملاً مستقل عمل می‌کنه و نیازی به اکانت شبکه‌های اجتماعی نداره.
🔗
لینک وب‌سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7271" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjIMUZPbclaexnbhozT-J49U1rCtWYjXYJXiG2HibotmYvyPa3ujRxsK2U3ZLbjCu5UYNDUIDWjMpcEJPtHn8WtclOzwzS9ecvFSMTN8wtChqVJpPCdHf-dzbPTwj4ju2Qhgz_IDk3BY0MD3QZ-ZlRXlV2-z-FMJrjS1f-aou9QNBuhEQ1jLcHahIuOipJhryMiPm5kX6Psj2ozWizsN5WzQVFpr78MPKj7bFkJMeREmAatqQJDdveCeXfa8FmU8N9ZvtFWDidan8JUFLoxsDjQGFR9KxhIM4yh5OC56PhIGNEthrWcVy68Gnbbe6XZvqhnhqkTjmErx2BkEI95hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر Lightpanda؛ جایگزین خفن کروم
🐼
🚀
بچه‌ها اگه برای اتوماسیون و Web Scraping از Headless Chrome خسته شدید، Lightpanda رو تست کنید! این مرورگر با زبان Zig از صفر نوشته شده، نه فورک کرومه نه وب‌کیت، و به‌شدت سبکه.
🤩
✨
ویژگی‌های کلیدی:
🔹
سرعت بالا: ۱۶ برابر مصرف رم کمتر و ۹ برابر سریع‌تر از کروم
🔹
موتور V8: پشتیبانی کامل از جاوا اسکریپت و سایت‌های مدرن (SPA)
🔹
حالت Agent: تبدیل Prompt به اسکریپت اجرایی (بدون نیاز به توکن)
🔹
سازگاری با MCP: اتصال بومی به مدل‌هایی مثل کلود، جمنای و OpenAI
⚡️
اجرای سریع با داکر (سرور CDP روی پورت 9222):
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly
📌
[لینک مخزن گیت‌هاب پروژه]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7268" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">config</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ المان کی دلش میخاد؟
😁</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7267" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7265" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtptCz_jisWc5n856UUHkngB5ocLMH5jLDpOMj1GLIgII8MdVPvZsdlx8YzAHVSWPLa0sA0ozIcsC_4c4UVsgbGldszTkJSpFz6kgqPpDoxRmezSli8oENoHifzo6s9ij32XZPZ9Q-ECWa3TMg9p-t6RZy-8imRkwEyFZWSOju6jP-MwYOOilXsaq_dNHYHzVL9O6nbafmxczjSUqmXd1J4z_mQoYP-VjqRpG0kxhkbJncty3JVK5J3G6m_0TSC2AH5ZQmJWyniMMSwhHyd9B1VB5yvKQfGZsSqlb08R32p3qT40Kr2jzkmcaNI_G6b0qpzw_bvPimh1y3CNeNplvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7264" target="_blank">📅 15:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من نمیدونم کامیونیتی تلگرام چرا انقد دشمنی زیاده
همه سنگ میندازن تو مسیر هم
از حسادته از فکر اشتباهه از چیه
فرض کنین ی کیک بزرگه
به همتون میرسه
انقد دیس نکنین همو
وگاس میاد پست میذاره
بنده خدا داره کامنتا رو جواب میده پست ناب میذاره. تازه و درست حسابی، اونوقت یکی میاد حرف بد میزنه. هممون همینیم داریم تلاش میکنیم کیفیت رو بالا ببریم. احمدرضا من وگاس، اس و بقیه دوستان
خدایی بده این کارا
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7263" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7261">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7261" target="_blank">📅 13:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7260">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-ieKICDuYXs6gEFwBB1JIcNJKXJ2egCmrR58dSMpg2Du2Ojz4sBx_rzWUTupiJpD67fTjVq77hesLvd-u1yvmHVhPgmXKT1srwgmB4mWs8epTqyuSels9s9xUzE_RVoSbdg00mtmQTSt8_n0wmF3i-IkpGflXU4GR3yVbdEt9pC7pfzXuTGnfg25PqVz58f4UbMOBZ-BYC_r_h-ef1Y103Pqn9GTXzIRVkniwVlfmJ7nLmbFBCAjC-Yfz0iEO1_PXMwnhmmhSoFTYBC7ckX28mCe8S4znvwPO3ljIB5sMXEyA3jcxZcOlM0DY06I86bQodbIj3mceuAZsYH-BAWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش
گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن آموزش کلیک کنید
✅
متد به طور کامل بسته شد
❌
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7260" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7259">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5 Opus 5</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7259" target="_blank">📅 13:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7258">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔥
6 ماه اشتراک رایگان از Claude برای برنامه‌نویس‌ها و فعالای اوپن‌سورس!
🤯
شرکت Anthropic یه برنامه حمایتی فوق‌العاده برای کسایی که تو پروژه‌های اوپن‌سورس (Open Source) مشارکت دارن راه انداخته. پاداشش چیه؟ ۶ ماه اشتراک رایگان Claude Max 20x!
🚀
❓
چطوری این آفر رو بگیریم؟
اگه دولوپر هستید، پروژه‌ای دارید یا تو کامیونیتی‌های اوپن‌سورس کدی زدید و مشارکتی داشتید، اصلاً این فرصت رو از دست ندید.
کافیه از طریق لینک زیر فرم درخواست رو پر کنید. (نکته: ممکنه بررسی ایمیل‌ها زمان‌بر باشه یا حتی لازم باشه بعد از چند وقت دوباره درخواست بدید، ولی در نهایت تایید می‌کنن و به شدت ارزشش رو داره).
🔗
لینک ثبت‌نام و اپلای:
https://claude.com/contact-sales/claude-for-oss
حتماً بفرستید برای دوستان برنامه‌نویس‌تون تا اونا هم استفاده کنن!
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7258" target="_blank">📅 13:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7257">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5 Opus 5</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7257" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7256">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5 Opus 5</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7256" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7255">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmKO4NVZYu696RQs8gSEZeN_PIju02Bk2SXbdqaBk2yLE1KwEWh6bSyvUFlc-UrDNStPb6xoLxAdEW6dH_sAPmRcFQQoA5LLf4adhqw9yEhKOIk0xFNTpmhbyzQW0-FiRR54M5qx0NwyczwxEfAWkZeGJXms5WR1MKay8pW9evOymTjiIi5qzlAETK9w8VVhrKZw1GSkdXu-Py-zhLo1B5kuI29vFO9c4ZYRMpzNlKf9uwUrbCYSMw00f7MwUJoKKm3bXZCaO2z_V-5RbHXg3fT4Cw_CcEZ77Ef6jduqJe-_bMozaTBO4m-9z86XUidTq2_3iBfmqE3m7hwIWnTLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5
Opus 5</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7255" target="_blank">📅 13:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7254">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ثبت دامنه با قیمت پایه در Alibaba Cloud (از ۰.۱ دلار)
🌐
سرویس ابری Alibaba Cloud یک فرصت ویژه برای کاربران جدید فراهم کرده است که امکان ثبت دامنه با هزینه اولیه بسیار پایین را می‌دهد. این طرح می‌تواند برای راه‌اندازی پروژه‌های جدید و کاهش هزینه‌های اولیه…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7254" target="_blank">📅 12:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7253">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ثبت دامنه با قیمت پایه در Alibaba Cloud (از ۰.۱ دلار)
🌐
سرویس ابری Alibaba Cloud یک فرصت ویژه برای کاربران جدید فراهم کرده است که امکان ثبت دامنه با هزینه اولیه بسیار پایین را می‌دهد. این طرح می‌تواند برای راه‌اندازی پروژه‌های جدید و کاهش هزینه‌های اولیه مناسب باشد.
✨
جزئیات تعرفه‌ها:
🔹
دامنه‌های ۱۰ سنت:
ثبت پسوندهای
.xyz
،
.shop
،
.store
،
.online
،
.icu
و
.fun
تنها با ۰.۱ دلار (۱۰ سنت) برای سال اول.
🔹
تعرفه ویژه دات‌کام:
ثبت دامنه
com.
با قیمت ۵.۹۹ دلار برای سال اول. (این تعرفه نیازمند ثبت حداقل ۳ ساله است و قیمت سال‌های بعد برای تمدید، ۱۲.۹۹ دلار خواهد بود).
📌
شرایط استفاده:
▪️
این تخفیفات صرفاً برای
حساب‌های کاربری جدید
قابل اعمال هستند.
▪️
هر کاربر تنها مجاز به ثبت
یک دامنه
با این تعرفه‌های ویژه (برای سال اول) است.
▪️
قیمت‌های ذکر شده مربوط به سال اول است و هزینه تمدید در سال‌های آینده به قیمت عادی بازمی‌گردد.
🔗
[صفحه ثبت دامنه در Alibaba Cloud]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/ArchiveTell/7253" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7251">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYkoXs7w9FI5ALxQHTY_ns-ouFXFRTb-Kf6LhmyIzJSGbMTi5sbniULE64r4iQlKxFtTlnPkxQGmLkd22GzPf5S5pIEIzVjQ8M8tLbn-84bMM2saFmAB1JZkoiJojKBEt_sneCzpXQKp_Ue7FuRsSzcuvogF-AtfyoB0Lm00QlzDu5ewP1jMB4siCykwUiijo7crQX2Ljv4OVH8B0h0KTemnlm-wqwtGjanzIUXKGiv18bD6OVOQF5s_WyF-eoW5ZYAw9eAFSZE7SkKwnPkXuyHDN7y_KUxCBWNro-KmrBmy1iZgpLtPTEQWusQjcrQDtdV5ud1B9BUNEOt7ohUftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پادشاهی Kimi-K3 در توسعه وب
👑
🚀
تو رده‌بندی جدید WebDev AI، مدل kimi-k3 با درخشش بی‌نظیر تو کدهای فرانت‌اند و دقتِ بالای رندر 3D، غول‌های Anthropic و OpenAI رو کنار زد و قاطعانه رتبه اول رو فتح کرد!
🤩
✨
۴ مدل برتر جدول:
1. kimi-k3 (Moonshot)
🥇
2. claude-fable-5 (Anthropic)
🥈
3. gpt-5.6-sol-xhigh (OpenAI)
🥉
4. glm-5.2 (max) (متن‌باز -
Z.ai
)
🔥
🌐
Link
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7251" target="_blank">📅 03:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۳ تتویی که همیشه برای آینده بهت انگیزه میده:
Don't stop:
یعنی متوقف نشو و به مسیر موفقیت ادامه بده.
Round || :
یعنی اگه بار اول شکست خوردی، جا نزن، پاشو و برای بار دوم ادامه بده.
Oh yes daddy:
یعنی پدرم تاج سرم، هر وقت خواستی جا بزنی، یاد زحمات پدرت بیفت.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7249" target="_blank">📅 01:15 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
