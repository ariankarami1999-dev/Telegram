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
<img src="https://cdn4.telesco.pe/file/XROqgw2auoE9G_lRVDCna92JjdNk_18VG-lbaJ7dtnOqjxSe3TG8mPZonB_UCNZJIRtdQ4LhxXnK24O8ojdKfqznVMSgB_HBIjBW2ZiuR65mHjlPy7VmnBdvOqvtp6yHb_n6tR6ZxUZvD7Wv2SQbErPhxuH7bSUcdycnGJBjJOLTSa9nwzFjPvaV7q_JTgHSzq_C81bROeqgNB8pYAB5zU5TxVXGJSDlcavKqUGxiwahRUjjqo1W7YbAFDJ5woi4F95dg-JDKKgxWlN6kyh7knoxewnAbF9n2TFeOBi2zUkn6erp2aDwqtEFRj-CQZeD4oOwefO98gmHrxajjOj6aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 06:08:05</div>
<hr>

<div class="tg-post" id="msg-7589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPremstore</strong></div>
<div class="tg-text">🛍
خرید اشتراک gemini pro تنها با 299 هزار تومان در پریم استور.
❔
چرا پریم استور؟
🕖
تحویل سریع (زیر ۲۴ ساعت)
🔒
بدون نیاز به اطلاعات و لاگین حساب شما
ضمانت کامل 30 روز
علاوه بر جمنای، بقیه هوش مصنوعی ها و سرویس های دیگر در ربات با قیمت مناسب موجود هست
🛒
شروع خرید از طریق ربات :
🤖
@prem_store_bot
🌐
وب سایت
|
💡
کانال تلگرام
|
💬
ارتباط با پشتیبانی</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/ArchiveTell/7589" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/ArchiveTell/7588" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3dAqSkKW8f40Y84SL2HO9noI0vVmMy4cs9v-Z0d6aet4Mj4RuOagGzaTx0piT3jQCtiA8UR-qLOUNEuqOS7sXp_d3gEdlwE9z2acpokK8ndpGWeVgJmILMT6k1QERb88Qpaa1xqeAfK2CxAolMddE4PXKlKE3I4IpKJMT9z2O2QC9tAcJm-slYALydapkHU0NRv9jDw5lWT-mGRmLOV0Kt07WKCuEs5Z_fCevQy4Zsn-e2Wq3VZ4nx0hqNJITs-GNHLprIUKL1KLNdxg0Y1DiQ4jP8XPhaLk16RqWSkuSgPKa9HrswmB80UXzt4NshNtaCu40aSUW6RIvvd4-nB8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw8nDkTgMVo5URgiGaOqR0eXufbyATemYCdP_KhRtvbMXmH6W6vpC8zunwqwoSqkQeIRmuiRWZLx-oksmRg7I1tkuwgA5X6jvZ9AwU304Dm9fP2Kdza9rR8yMaaOZZHmOVt8QhgwTh9Sb3ESeC9oRhIkcDQCSILr_H97if4OvvTTPZQxtVxcis6OK9gEge1ZO6aZDjOMZ2Y-YZBpsD2mwkj4QFq9RWjlXL0UsZeB6qO_qWsovRU7LYl4ev5yxR3nOwFR7fodDop3gkmzljXFl2Vk06UgS2aBbvTbrQk6bd7QU__RgrEGZ5Ne8kkhQX75yNKC9QrvB_c2Rnv8Ul28TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJap-5FwdPtAdqM5UolxD19YMKFQIbruzKb2RB3m4Bps8uTOo6fGxv-g8SI7esujMh-yXaDtmquxDuRSqaXWTHqrzZwzDVFTZS-WykrSeXJsVOFTeqGekclLr5AFET12XUwrf4NQajLoNiijNdybG1wmGmk43qE-C0g3rjU4Rd9ThLlZRq2PV1CD3eyXQbynxLa80AusipKwcH6yNX5ApaxDNSSC2K-GAgLqAe2KCdXz5qlCux6y9TdC22FtDETaLgmSKN8m2SXTXNrGWe9-Qca7o6B-uN-qpOyj20UPynlSphduAJ5RPUX84qve2jEwcW60HHAp313ApZFSCWMtXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=noARjPFhFlXX3ZydluS7g0-q_VuxiEpGsV-3UH_Jqnr38TNEaoeOL_ouepUiIr3x8qzFsWDSZcRcWT_4VoUTOud7Rf_eYwbNcZsGOzpI0uraRdafc-oXYvzC9tKMDTFrPOiiyhUgJN45MZaOF5hvzwqgE9fmznqWg1c8DMmMJ2nAaGp_EDNw0PMxvdQjtbGuuPQMh9bkMLh4XHnFHpXrqpYbsXMMHBOd0ZeqJ9V4M3CWziTFquKrdY9zDo57GQfEoESDDhRzLmknIxKvjrlf539Q_XPcE9CjUjgBFWSOf8g22BNryH0-BGIOA2Gq6Rfkx4cmWNXYifRTasJM01-dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=noARjPFhFlXX3ZydluS7g0-q_VuxiEpGsV-3UH_Jqnr38TNEaoeOL_ouepUiIr3x8qzFsWDSZcRcWT_4VoUTOud7Rf_eYwbNcZsGOzpI0uraRdafc-oXYvzC9tKMDTFrPOiiyhUgJN45MZaOF5hvzwqgE9fmznqWg1c8DMmMJ2nAaGp_EDNw0PMxvdQjtbGuuPQMh9bkMLh4XHnFHpXrqpYbsXMMHBOd0ZeqJ9V4M3CWziTFquKrdY9zDo57GQfEoESDDhRzLmknIxKvjrlf539Q_XPcE9CjUjgBFWSOf8g22BNryH0-BGIOA2Gq6Rfkx4cmWNXYifRTasJM01-dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtNnLQ70h-J-l5cOZlKmuuoefjeu2IG4yEaQYSANQ_raqCzOIFtLax8cmpoL_VU1Kgy-K5ZuKykg-qG9BT9tGqx0VjFu6weSfs-t3ZRwGTEDQhZXWX6s5MdeE9BdrW-mp42RXtkWosptqz_D7dgEP0iT1vghfp7G76z02vT3l46730jgc66xipoSi-Hce8kCBMqX5x4Jykpx_Ee79KnJVF8VKK40uxaS85bJGB26pLOUAMkpneSHSjkMpwbFMUpIZ2q0SU_r2LQwL5Q9IqOHiMEnw2N8dJatZj_hUPT6MfTnAP-OGUcifZUqmh2TbucWDOPm3ocnhcTSVGzPtxOyRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=LQL_BAyP8X0mGQF6sDENpJX7b937oJSXFsauvBeav0vo1skYoHE4JHeVs0j6SuTVvHGqJKaQTUok3Rsz32BNI5MYeZmqFGQEBg15hb1wB_dqqW7FtOaQmpTG-rNCtBj7oWcdJIm467Bsnzdw8S8SXG013Qxl0Tt68Z4mP68Nya0xREMqmBGJ2L_kNhR4XTUQa-edxZOrb7bMH1Lx1Pw7jsxKPVWC1Kq_uXM4lFxAU4WE_42qlIyEOI7xLz_A7P_LeIhMBJNhrC7fd37adw52GZGJeMZj6S064ev1HOeUMWC0b9QOQAfcl9LtsEhlK0mXzjzY1tsIIBzch0ren82yww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=LQL_BAyP8X0mGQF6sDENpJX7b937oJSXFsauvBeav0vo1skYoHE4JHeVs0j6SuTVvHGqJKaQTUok3Rsz32BNI5MYeZmqFGQEBg15hb1wB_dqqW7FtOaQmpTG-rNCtBj7oWcdJIm467Bsnzdw8S8SXG013Qxl0Tt68Z4mP68Nya0xREMqmBGJ2L_kNhR4XTUQa-edxZOrb7bMH1Lx1Pw7jsxKPVWC1Kq_uXM4lFxAU4WE_42qlIyEOI7xLz_A7P_LeIhMBJNhrC7fd37adw52GZGJeMZj6S064ev1HOeUMWC0b9QOQAfcl9LtsEhlK0mXzjzY1tsIIBzch0ren82yww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzmvIRFpqmrmthAGW2m7yTTB_zNHGmwo3bwn9X_LjStTR3gwrcurC9zbpoUc1Ymiy_zgNfTPLPEffYL3guOTjz9oW2T-YCbiYDi_ZBIYWTucuXob_iPURJMQj08pGfb6yINDE4RwBNlr8DMPtF5jpEFBmdnrUZQAp8Dxtd4qZZaTvuHy8JVofJinI0mtRO26Zo93Svs9junJY4us1xkjW3QsUkpDgzRSDux7LOkSmySBrKCAqtJz1LnXrnphtxLOy9IOmfBmQb2NMtS7SBtygRML4cvwZp348pioYvY_HWWj8Oco9tbBm0P5WVMSlTpR2UcbJISxxjMaXM5tM8s9rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-jjxTRGP1dc4OWZskxu9cH59gFwc1wVKDSYYJRHksYJvz19lR9BFSDtx7uWvzOSY4vAtXKe6B1KLY4bWA1XyfjrtvRg4C2LRqWCWdIeCS4bfejKvldk9eAxmqdBBCZZV7YUHG9FsIUxolwVoTU2ti4NtpvUpIvUXPlqMaIAjBErjHny2UOJYIbloOspFqWTakqbkaKshbE72FzqyKka5T9dV7m9ACSPrjl8bbLvROkFUfTondjIDIGMezlVpDuqgTd7TAuinkGkyGu9zfUWgz4PYLhqXqzhOrbmWy559_INRbzE5wuclxx7B5ZOpXCYDDjnCkypE3jQApDGAa502Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6Gy4xKY7Pr4-OX9Igzpk_2rC7ASYrUpAexoW9wmmN4k2bPubEp6lA72pKAyAljifrCjyEyEkZIjtsKH7qiP8RrmIW7c6kX3M2NXogrqb99WPwZXeT203cCS2tTP5bsj7XL-mjcZIq2yWnmcvXqOl0z7R6h7_SZ3EVmOpLvCXld4LiR13StdlrweHZGTm7nwMWY4BztpS-d-NGagy6on9Glao8yCO_1olKPGWZpgR2eb4rkYnKZhARcTFVUaWKvDzCIEIDvkd_g13PIX82eV_Ln7AVbVjLawRN4UeqdWufTKF1RASu7CpHc_Vg56CrMhKwd0v-3lsmD4fjPoQ5Kfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRTkbKejV8rUWXd6OW7trNAFV77eNU1L61YdOQk4y0Nzs6mqaj7IY_TRKwhQ9BTfUXm3Tg7LRilGtQPYq7f2qAPJVjOa3tQD39vlQ3rewqf-UDx92TOZHdUtN1Xvn8ITsfGOkexc8H2TtatpCym8_JlYGVLRIAW8NqCp8BJIFc8v_lfh1uBox9Bgj-fwb9oHWwvDLhVt_z5PCK5RqYIsNaq0hKdGgF9Ltl8kktS7KzZk_ztmbOOgAH--ZzWOJzk2bhGScxEieyF8VEkuR8lz0NsEwfyoXySnIcNXkbIh9a6Y4yEeOehWXVFVJjrICzvQMKyHJ-1ucSD4Q3X-dhar4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuVNiahKFIZ6isD77prKG2vuU-PHtkspHmCuaNyT_KYXO53YCPoZC1eed10MZn0T7-A9kQkMBqyV7QMX0LUZLdh1rDG8yIl4dmsWgnONsDD5VWD1b9MqpjM_T7ZUBv_58IvEPoXoda31o4qyT6W8UAy0k8mewWl-5kflqlvmsK7Qbdb26pvUe_B6OGwDIee3KsrWAcINfd7SDQcz_qJIVaMnwEUrQO5z7AjnGHs7ByvUC_Wi2SAYEEtz4JknII1QWurUjK-FpUPwK7uN2jYqmB2xfd-MjmhibEthzC6Swdelsz57hINnaL5LErJYGFtQ2vT2NHYwbOlSuEekHOu6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jlt6LEdlMdwdRfvtjIS4SzCZDDAD7x7Phzq77LYSOMwoAp-D5yqfS-iHbd7uaRhJfwvpyoh9b_nyS6SZLOZ5_0lsVqNMZxqKcMxN5bqr_7njUkieZYvphTfHkTuNb9TO_W8qPJ4BMq6lsoJJhTrIdBrjK4M6KBftkXd-iUz6AXXUdt03Ohi5HCLxeA_c6OTFCTSvCEMc2ypi9FQKzZdsxDLk41QIGdgO5K3xXE3gOCdRCsIyqqErqy3dAm6yFzvC4M8zixVSLCR5N-iPBrr6x92R8cNHANRNI3PdZMHELR37g9UeByxJ-eEuaCdNsriMsiihZ7-7DcR7dAGY5gwGYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuJ6TpexhSR25XU_7hjkP-C-H4zeI0fozwuQqBsYa6PwBI3repscBzUnA2JisBTXgnTfcwaI_2cR5b_87hKbaE1kG0_WRgo8NJlIJqYh2CldCU7YpwiJBLY468bj_YvNn6c2CcxSEuMAFKL6-sFw8Fx_fYtjnc5voukD_bmZTf1vSbNwmmhHWLpP6ysUnrvbBmEEDkTIbMWv2Sq5qxMsSf6XVqyFkVT4et8W9B-HTpwjXpiONopbnmL7WmpJSdLmAEL3TCIIUuBY9mZCrWRlBwSo6yc3HfC9uB5j3Sg-f4WvZgsGcOFkKZm5JTu_F0Ghy-laSdRE3bnE4aX4AEKUKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJEHYh9LW_c7oLIT-ghDtwCZMApPo2KL5bnPlxzaCbaDUS8lrbbiTeM4qzFcVj4MxWO-4x3ln7I8WcU_epbkXNy4ZbPICv1rBAz0PRirWrBH1fee9LO4lL8j9wrFS6ngBXvfW2kKyLuiWuEVATxVO4Y5KvaKnzpsyafCCQbRRqujj0oJlGsXwcrQGZkFRXbEqBl9y7uEYpA2D9OEuExlGwZ2yskVx6tupxTbkVcfHamsA-Qbi5dvX2Yatlf36rpBSmC7DRsLciYaCWNBT-T2u8WPO7bBd-XDCmOnjL2nbNpeUT8dC6SF6CD_aP4GfOrXAPb58wasLb1FFKSbeZqiVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh9MwNNB-MLkfqGGkKn5ex3RYmb_fqTQohXa-wDDryKFRe0K5As00_UoqDSJgxgbrJQK6WHna56Km7g7PUW-cwN4pgHLZ3i7wa8z1KXaBrNvgrpojo7GxhlQ3hjAeaoJBIvw7gf9TNxDpu2QbR7bPb1OkuyiK2Rggir3srd8EeV__KXtR6f4Ssho9UjSwghKA8SYpzfG-pmG5SJEhG7Fn5obwAXGgpha5jn1__pF1h-cg2UOnmfVYZNF47oH383fK4bct_5gvRl6HzXndoiwDMYHiNqgej43uLpqGG6iMfNQG0LdVWC0Vg_-kTWZzTJ5mR0oAw8FvcIP7Ys-JrEXsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbt17Wp8Uqi92ue90Fb46SO0BFDGkiiwmAF9bzbnrjeYShi6a-W7IqChqujHthAU7w8h3p_qn1zjoO9UgZN_VqIpGbSBaEXo4ujbfVCKTg9mJ52ypLfSP-nAVlv3sh3CEsRmOpOmip8AnIHn-W6-pWT7kFABWfG4iCwjPQNcJOsW_9g3Aqg_IsBVD4TNhviChsK5qe9bLBoyZn5tyM3AhQoF0WXepGvV5fMSNa6kG07BETe0nPlVrUXxYlFZ2BiMtIAAW_CIK3Fn7j1y4ijdq4c4mff2qH7idXNLqugf4KiGx0tRPGn2KvlICDDM9jUUcn7rNUJ2lMuWN9Y6PYSQLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE0W9eJQ7NbvzfvhtPySWRWmQLqEqH_u3wh2S3jCrwzS8S_Rc3jqWS42kaIXxyTRKjyLs-4bvHqRZagjsTxaxGBRN3E0_h2MXRp55GS8JgrD3tMk94JGGOPhYNNpw6bRwh5MseG76dsfvoUJ8OqrqKOxPF14eyaL_ObSLN-rG4WBPjV8CQslB7emoP1lS0mKPtdVQkTbg96RDwfmeyfxSc9njj1ObxgQp66UmtYuxUzZQam-zlRbQXcYgm1FGgC93Wbup4G7k9WQRrudnlKl158jDEO7AaPW0YLZ-W17nBGq4uRXiBOX99fRYTsXWnylq0aqp2FykER9QgSaeRHJ5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyRFjJMXhf4sUoskiwxOiuPpJ6XZNvsKv8Isk_fvsz_VrL2uuv8thh5JrC3pIKx7u32wmnfQjhRafYDJK4S7HEkghg1ea2pzmamNNgDxaVIWSXjJW15WIWjnQZHCOw2_Q8LJ680-rs7zC2Ystssd8PkBcfanp4NeAEIEVj0WYAmnzlO_qXbXm6ns1mX4ZpkMAoWpQ35Cd8wy5iQg_9PkCVy5tol4uO8Ppm-1x6FS5uNkBR29kENDqQ-_OH_AK_ISdXGJ6LtR_DXT0JNK5CTPtE_DTdIa0_jPYFkae8_0l6jnGumwzg1GV8p_9lVXv0lBQ1Oim4FYhcGzMOmgSVNE5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpP6XH7aPAE0ZNEsD8fBZSpHJJjMgYI8ADjFkCcW9BY6hjhfjZ0Ouu1pv43bZdC_-pye8K43_yApjpTzsKzADSF6rBBKhyOhaveKa96riwOahXzenSnkdU7dixwXgpfD0BqBym0_Tj24QHDjqdtRG9s3hvZEpT-jYHpZJZzgSSQT2PgAjD87KeYrBNb9abW8D-p8jLzuI1nWPPwt5Ok9p_4soyPXI5nrclgqf3IBPSP7JfK-0u4hrqo75BjU9wEpM_q4exOk3CmYnUC27q_RwliLF11qbXqZxBTyQvcr5cNXjKBm5wYXjHpkRGk_5befgFtyvpSwW1EnV2PE5K4PHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=gMoPq4yKQmdGdwS5S1rP-yJGy0ZyWdEBkgfkHaB_dfmV7nLgT5O1jZeQpyioMWORRNRQI5VHkvO4z-f8YmRQgBIE2T3b2kblzw77O-QTvoifZu08Te2CTxpfDpIwwvijyVqsJI6hppah3Dcg08Mnyb2MH6S7HTW8L0oG9NH7LR86bpzNzjVdD-T1G1N2GBgdF1iYvgkD6mbRwLbI6oNzqN9NEmAjOGHs5WTpn_j8Lx1rblOtbaqHtI114p16znZUx9GZmVBXv9bhSWj8n0jZN3-8IPgdmPwTwtVn65xX1KgKT2q_uC4q9y8dXL7G1RZnoXvkjtrI2ldFkJERtbVXug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=gMoPq4yKQmdGdwS5S1rP-yJGy0ZyWdEBkgfkHaB_dfmV7nLgT5O1jZeQpyioMWORRNRQI5VHkvO4z-f8YmRQgBIE2T3b2kblzw77O-QTvoifZu08Te2CTxpfDpIwwvijyVqsJI6hppah3Dcg08Mnyb2MH6S7HTW8L0oG9NH7LR86bpzNzjVdD-T1G1N2GBgdF1iYvgkD6mbRwLbI6oNzqN9NEmAjOGHs5WTpn_j8Lx1rblOtbaqHtI114p16znZUx9GZmVBXv9bhSWj8n0jZN3-8IPgdmPwTwtVn65xX1KgKT2q_uC4q9y8dXL7G1RZnoXvkjtrI2ldFkJERtbVXug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=olaV8mulk9rxF_Y1jSc3qUOVgejceMxNzwABSXcQ1phOIdd9oNDVaTJKtkxBG_gf9HoG58n40xqQ3HsANKr4WZjFAXikELb6IJCl37PLrIqGTN-CBr2PzbPDN-5PzpM1e6gl24I4oBkwBVg5ovil0OmLNO1fWtKR97YD_945IzzmWbw1c0z3HpJLHho4si5HRSr_ImsyaRILHn0dxj6_FJ9T4Il4_M6vzBoQXDyl1PE8j4MEyTeAP5hskHRlMR-2yTKzAYkQhCz5cUoqbr77ii2EQeE28Rxn2EW5J778afGp1Nyg-b5OGLQavGmP2b4sLzmzVb0saHLY9obD_O10Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=olaV8mulk9rxF_Y1jSc3qUOVgejceMxNzwABSXcQ1phOIdd9oNDVaTJKtkxBG_gf9HoG58n40xqQ3HsANKr4WZjFAXikELb6IJCl37PLrIqGTN-CBr2PzbPDN-5PzpM1e6gl24I4oBkwBVg5ovil0OmLNO1fWtKR97YD_945IzzmWbw1c0z3HpJLHho4si5HRSr_ImsyaRILHn0dxj6_FJ9T4Il4_M6vzBoQXDyl1PE8j4MEyTeAP5hskHRlMR-2yTKzAYkQhCz5cUoqbr77ii2EQeE28Rxn2EW5J778afGp1Nyg-b5OGLQavGmP2b4sLzmzVb0saHLY9obD_O10Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCaeYb9fZKvfuiw6AgTzWbt0zLMe0wR1lZ5K_y6lFsG21ZVV__XmWcAT2nBxujUjhIN5K8wb2jpDlzUzzIHUozwOvnOzYth-6uleutZyH8j3s_JreSV1O1d3PUca05vufmIrfil1_tdryk4EftONB522bo6WxAxSKoz8JR-zUiD_JcM6qiWvYU6Oq46lFl_q249vP1Ron7-3JD561D1_Usq-AX6ppnwwCQbjmsQdJuwRoxfjR0zS3Y1BhNHOuul8nymP_RX6S-xqQQNEq_mpctSv-l_DjAEruzufhrXDErKheDfcPT-nI4X8KaDJ4eZk3sM78V1dXNOKm3fBm9WNVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebw4Sqq3usiw30cz-omqhEW4gFPtNPUD1dAvRQ53t5zQugq0EktmXx35qGtn9r1cgwXJQqQC_fC08rt_2p_tqhZ-QSVVrfaF72cJjd2aJeNZly9_Sgih2l4TkSO0FLczsruZVsIWgDH9w2iiypyIjcQMS98SYUpfZguDRQQbkPyIU7huHYqwRdzSm66l3VNbQ9_1CZLm_WydjBWGzKf_wwmCNxnsoBSGSifp_-4Xy3dWyQz48qymeA0kT2PMv5kwbY31Y-wxT51_60B3L02mC2enYvDGJPa2P7aMz58T3g7HA24lt1gcWNDkz-GYDwenF1txZFknr5Sqbi3CDZNdIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmlMMWTWJkeJH9Np0aDODAJn8GoPbXmr8VLQjNrIGfoha0IgddEKORGC04LnoLWFXGoVnfRpi9jSHQfgT5UuWsGkea4rlOztWpSh-8dktSup3Zs4QUVisR0TCKExjEIlOVphXcpjhJSo8_5ENWSEt4QuTETS6LgjCV2VnodPogM61o1az1jYmIGbLD4dXldGaPxg-Wk24YUw89r_2BDBpuYgqLFfJM7AUhuaHeYMt4nepLXPsFCfoS25QtjCOOnS5CxGbvwBfSm9oB2A7abwxbnApF1CPXkVjewOv0gyupPEL2H3ZyqUzfqngC4fUKRZbHUT0bATCCDv9_T0epou0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=l9VSwZoj20mNcaFEqzHx1g4lH6UQsk-gHIYDPsLlHUNfGIeH8qoOm1Jgb6UlK-jJJ2xWqReJ9xtjwJXe2YWeAXzmnHBrCwb9WmfMZGDonc-6PL8mtlH-32UbovvGr2a2-HKwR5MifRdye1PUN2vVA6nB_A8bQKKwDqH7MUE8VAJIeIc2KYdBfkf_sC4OFTtCHM4GJuBtvS6aRGVwsmR8QW7KPVFPDpux99KF6v4mTGCqDkzcbsz5felYDS3AfnQCYJ__k_wpYVprzUegAkeq7i8jxCFQIqvty5ylDAuaQLrjcOfXKyWSmGDaKfO98tjGoLOFmIesv50pXOHY8GyKv6rY60e68cFA2p2AezQKU3-chocj8lGawe0qTylvwYSG_KWWmzTxPopdVz3qDGHNynsWqM2gL1P48dofdMMGYFvnnepbmHlyXvoSgzNwEtZidHLH1vwCkmDxw8MRwtE8lvq177o05AKOFt1AkTviF5NCL5aSzIdDHjO6nrw9RsyUuZnqo-t-PtpmUvOrrOs0_l2262SIs7L5q-uXSmyPBQiDUdVeU6LYgv63w2FKhtz4YB6ZvvdQB9OIZvuX4sP3VqEoMppI9F9VHSpBlgGnTxHfFIdLIzKE0Jx4vaiT6-Pdyv3VwXt1U9RwCpOOkubWiWUpjXk6lBrFK8esbLCYP8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=l9VSwZoj20mNcaFEqzHx1g4lH6UQsk-gHIYDPsLlHUNfGIeH8qoOm1Jgb6UlK-jJJ2xWqReJ9xtjwJXe2YWeAXzmnHBrCwb9WmfMZGDonc-6PL8mtlH-32UbovvGr2a2-HKwR5MifRdye1PUN2vVA6nB_A8bQKKwDqH7MUE8VAJIeIc2KYdBfkf_sC4OFTtCHM4GJuBtvS6aRGVwsmR8QW7KPVFPDpux99KF6v4mTGCqDkzcbsz5felYDS3AfnQCYJ__k_wpYVprzUegAkeq7i8jxCFQIqvty5ylDAuaQLrjcOfXKyWSmGDaKfO98tjGoLOFmIesv50pXOHY8GyKv6rY60e68cFA2p2AezQKU3-chocj8lGawe0qTylvwYSG_KWWmzTxPopdVz3qDGHNynsWqM2gL1P48dofdMMGYFvnnepbmHlyXvoSgzNwEtZidHLH1vwCkmDxw8MRwtE8lvq177o05AKOFt1AkTviF5NCL5aSzIdDHjO6nrw9RsyUuZnqo-t-PtpmUvOrrOs0_l2262SIs7L5q-uXSmyPBQiDUdVeU6LYgv63w2FKhtz4YB6ZvvdQB9OIZvuX4sP3VqEoMppI9F9VHSpBlgGnTxHfFIdLIzKE0Jx4vaiT6-Pdyv3VwXt1U9RwCpOOkubWiWUpjXk6lBrFK8esbLCYP8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLcAKM2Y_C3_NS2la01QC3ctw26ck8J3k2-I3Bl7Vb-nKP7W2MN932plHwW77wmQ2pGPk-gLzB-urtuvQwPSDQD9YacGzfnGXTB72ZN3OKtX8TbujhpTDlbRvwWYvIBZci9NYFNqEQezJ1gGCTEhVDPADvEei_tZrStx8B-60RRyFCLv3DwcbbDpv3BfENrO8nzBHbR2xVCw5tK60r79kCkRvZAZUw7kJK1ZmlCECMgqL4LICQ7QiZUYnnWlyPsZmlzxaEl6BCZHGpBXARj-a292RDrbrL0LwDtNDNwe34VyL__641MyZM_-oY5yUJy5_nB7D1_cqjvicVFBLKuVwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyT4vuAxejOTHD9Av-sDQYpfhxW2E3thWHcj3Bhu30WjFtbJmmc4xeRY9Bj3RpozAQv_HTuGn0oCtm08Dl2wdhS_-E-vuoCTWb_tmGrBXkEj0vRgQnvsyNRnzSSMk3O8jOBMKNVBXPC5EX3jcX052dkbWuKXeNdJWkVQIu2kvcGK0LuLQzGADe8v-HalOYezgNb8Fh1D12GnoiuCDNowre8tKANyN6uQQZOQgDwoS1jBLQOjOSQXH72Gnwv_LBntpibTdszZwo-cvdI7dNjO0isbLLAZabtjqZGY61sar_e28mQKyr5-8Zj8-pHj8VdB42ANrjVp5rzxRmXNNBYFNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7FIlP2RtOYe-xLXUKB3SeftGnD2vVcccyE_i1Cix8wMj5XJC2attrS5vlCVnMKKKjNYBIJDDxwjc_4_1i9P2Eactb1qiHExHVMFBiVWdVna5fc6cszhfz-Q4tAKKLblNDwLrP-ttKTO--bNXLqvJsumP52qzBtVHMqGznIdJvw6m1sHVjyrl0wsGNKodRAUF6UocYmAfrHiQMgKYLW3enH8SGREQ3g19k279MzJMyUery8P8nqizAN5uzYG4arzdTMZ7eeL7YXb0utvwooJMfYZOAE3dYOXxZhWPx3e3Zx6NKPcRReTIm3bFUzQcpACrittc0UHBMUYKLg_HH4DcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeLtvVIDZS-ZfW89JnY51UV1wK_kCLkl45S__iw_U6S72c0WXYEkzyEAHsjqmhWRratxGljXfzs6Dz6hzULseNPA6_hxztU9tbHuJe7ZAL8t7iZnOeTudZHVknUAjEDtWSh_0rXpJ17XpUCjGCV6JIiYT05HR74XmgwvHXqfGstwDXIOPBGu2n4Riq5IBiJ73zroCssXX1BnB6yHR_7BH96IRhReCMKDp6V4QBmjhaRD9h0Q9rFqa68pJlVEa7XT3c71l119FvypHkh0A6Lm-8M8B0TKVZYyQxX5rUFqcwuJ2g5rmONrLljFXbqMPxE__BOooT5Jhnfgk16ZmiGQtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3utcEEE_u0Bw1t7BAVGsdbYZDNTFFkDVq8k4LoeeGot8LJN2ZYPOrTsmKqiBT6ddAej9-5hVW2VUDaVFSUzCi1DNTWYFtwCc1i77P97oaSgef8U4azVlesPou5QgMnrWPnGCkzYnlAaZ98dVAQtuPfItboenAuNpbjiVmOuj1ITk4IMwv9qe7Dx6rubzlYv9wb290mh20j_PIsBT8sTs7Bcu2OwMQ-LYvLFruo7js2epGiBBdzm7U0sx5iuIJOn9d8cMcjMqnuufwvqkxT-f8VBvikd2ZDxI-rJLrMbkJxtNT9LULJ8Kl8KasGRvMystCUlAukE8XP-SI3YYIqjLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyf4EFUgdzqENNs9qxcicab82m0GxyOufMfhxYYS-b05vh354DfvEMEMoX-TO-721d0fjlBJPUF-uTtTrH5JgTyOp9MRBg36I9Z4VMpxYNkP325iMy1X0SmrP0YDanQKxSQE52XsST6zmly6eIVlna7TkSUJJBZ6U-TBkYtcx_ymSvoMcFqpafgtNM9fmf5jWEDK13ZxZrbvu5_iJ5ntqe76L8DD5gZn8f76aqf3aXfk_Xxgy7o2ARU6SEhwXSJhmS52wyanp6CitfEvkSCAUEl82W43BlKZD8Ef0BZNCQa5rREzBaCRBR5M6UuW4rVJOPL8J5cnSu5H4jRvU-kd9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=FxMZPsU5ozRrw7jlUILQvQznhxi73azteQ6l3_JDE7aDvQgoahscXdPLaRhDGgMUZTkIIcVtrkRRJnxIAmDAjMOPsqzZtT17HV1Bq3FK0gXXz12FPZFEWSXuh-9I8ZEQmNPW44iZOPMKEG2f-psDe36fCd12naVf_Yj7DYPeb7-edTwVfU98xbR9GXJQZOx2ifLiO9-tvpOyab_-mI3wUirGPWleyiC-CCfZuH1IAOavY8ghppnHaM0dYsl8zc2QK1NhnVY70lxT0yz5L1pLu_TnB6f1oMBi3tRjGscfY38QFRVWmaF8aPOhqngOKRF31CT6eliuM3-Bxm1d7DfqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=FxMZPsU5ozRrw7jlUILQvQznhxi73azteQ6l3_JDE7aDvQgoahscXdPLaRhDGgMUZTkIIcVtrkRRJnxIAmDAjMOPsqzZtT17HV1Bq3FK0gXXz12FPZFEWSXuh-9I8ZEQmNPW44iZOPMKEG2f-psDe36fCd12naVf_Yj7DYPeb7-edTwVfU98xbR9GXJQZOx2ifLiO9-tvpOyab_-mI3wUirGPWleyiC-CCfZuH1IAOavY8ghppnHaM0dYsl8zc2QK1NhnVY70lxT0yz5L1pLu_TnB6f1oMBi3tRjGscfY38QFRVWmaF8aPOhqngOKRF31CT6eliuM3-Bxm1d7DfqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjMAm12eJhJKBEKdDKTvHoqTz0CPjDKExoK7CyUWDXLCJvFDSmGmWslN0tSKp4NrG95bhXltJ3_-5ritkz07UCAIAETaNBCnYQyrDCf1PHdJX3sSPuJafQjkETMFVGf3blHNTgQL85nCTVGrQnFVF_MVbDo7cDSeFp8ptS8UwykHmWvzCp0qChtf_L-ZJwP6MTm8W7z_IOdZimesR4TnMg1KGNVRhgfryduKoL5lMyen1TBT1fqQ-1xmphsIZx69bMfvz9KI5dqZCuIzZ19LVxCA4-SIPtVwktENSoybKD_qmt-sS8FzlQHPiFd-yt-FvxFmE0hISBe7ezjnEb6QHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSeHiQE-iTp_G67jfy4ZX3EznVS9kn3uMpwobyaleRVX6lFrYhzzyecAB34hzXoLOnOnetyt-tiMpp_y0QYMdvesZ4Y3oGpVoXN9TG1GyQqrGY7_ihi4E2ZMm1NGix7qRqay3PvOsQj-HXhB8mQ-RwgC0Q16w5uLbtHS_QykTIxNE1aTSl2R22QfBWz2ui28Kx1jTv_1PQzPyGD4l70272IXmK18BlgNagHvPhDUCvviDA8oYfrSkuccZZNlODBHpqfrVXKR3tAAskbRTwAKcwreQoC2AihhBwVOVRgGC7E_sg6_WLQiht7J4lnzYwKowSAL_6ujITU_1UMCxd05vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L48Npz_UEyjL-H2TXNDWfn7TRYQNr5YIR9y1mZLUcuBXP0IFjaAYyHpg4GTQAOQ23weKZKZGYHRF0hI9l4D9IW7yJ1hFWzmr70X5rFoAm127T7ohq3Pws6V_boFmkBUPZV3faQriIVT0ijQFf6dn29wK9nG_ldhxfjp1WhjF1i9IGHpfQZE18qh62QJLtQHyzXjNVdkor6rR8KswXiFJWR7hvu-VYYIHq9n7g3ZDXsCu26fGFSLs2jvWmlzMHuflwB5tM0OdPKwYGf1IEA5tL7yPx663RriRS9R0i25uUVd7M20SQbMCe_Gu06Ngb14dJhjzQJR4nL0SuXVrq5heiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uozpVTJcq80Nofurb747orPoz6-uu4Lgun0RM55WL6Wh1syCMGqb9GX9HWBaJpNv_9w19CizblfC7hxz1Uz7nVZ41nNYxyS8MolhVuHWlyOhKPNjcNkzAyjWZogeVYMhO4g6DA_ynBE6JM3IAwMGWJurmWUpHo0rnCmGNHSEsiFY-rk5N4GxzUiI6_oTBbK7f5hlRo5E2Au1xdUoc_e2w6kYmPLPFkelZ51Bs4rjLytQjlvxrorJyieXC9Jn3tR4YM0wHOCwi2c3xbbwCHFDKIS6YfxZ6m-6UCAlyr5yUAfP-qd6l8NOcpvG0LXzokAn_k1APTDqEhmo-hjRlbTfUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAsDqbv447qLrmH2BT6vhuKtZf0VdXNtIRfcNz65KoVw-9jyhNstHPzujHi5Rng5W8pX13vVGz0xVolJkMcoZmRbU45OWbqueExPYlfTm8w2TXoQNexWAPwiGMslFpF93skRbs12pG7i414SXUB6xu_bwoLCtSTstuiAPXmW116QuvSAND6XX5X9VW-cQLXkwYgOKPcr-s8_815pX5nn84GbgioCSAI9_le_2_lL1lPw3bnJ9FKz1LVYxZOLiNrfCzTNDfjankXNigWCALP24jrA0GzeB2LA4UWdk72tG1EfPcBQGxPyur8uQOwTyZnRjS1bgaK3WvtYUnMK2w_Otw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYOYDl2vf9CICDD26ZL8DO19-elrNiRxw6QVodPJGbg46bTCzoU7RKpTOBP8NM6SJd41vFJcAiKbOyzqYGnmPKr0nteKIK5n3HQXHPK8_XoapYMSzdo6vkTtoPBPV9ufVMXAbE2PbzlPLmd-GFlZvdN7jm2bFL3UVL6aGWkp1FirZoXrVWwGwjmOK5QcE5dh-uDx-JhgFkzZZi9r2G3vt7kcoQHyhyJzk_7qZ5sZ-3aeXAi0o3vRVUaJfqa9ayslbkhBvveeNGSmGcExMXXZtkhvda1G7il3ixPIshM1Qql6DjxySNPOcEhyzHgI9QqaqVtzCCtyEbqC73dUCX_qmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc0SymAaRSYywguz2FVHhU651djf7hA7DdWlba_2hAF7LDHGsQTvBy5dEVcRACxX-xfC_UFk2t0asId7A3VfYDZ6DONXcZLMPSOZmvfNv0QM6i0rHoHkp7yLCzG_DkWJlMAuap6mqcHvtMAiruQBtf67cGLB3VM2QarMw70rFMBn0AUon89TuJY0OGokPivZ91ttpJkdp1XWTEQOl3_Syv8K2IR6F5kG1_tXkNz1_zkIwo9RgA3QNgXTulIGvFn54XT5wvC3amky2EYr6PnX0RXBlByHQx4TEtjifVyO0QeA1D1ASFPoF1k48Qde-v2O2lLgx08YJkMKRu5cnZCW-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouMHjtYNWCtpH-HB8X-bGAgE38pdMbJ4QkUzL2bSzvyG3dx0mXGbFGLZHqL8f6lJQJFlDGea6qmkeJYxKwh0-EdMYPLzoFEmml-OW-rB9wTlAM9GdqChsRB9enhJPzwe6_H2Uip0FEM5VS0rjzSY__hw7c7nyKLNUh-pwClMa0TUoEBv_KE1pW4XJNhppdmJrfXSNcf7GQp2rjO8EyzpM1QgIveQ8uJ98vjfomqlKZkBoJNU9Urq1UntYB-SRinat9bIdQphA_fT-YWuskkbsP1gGwcrxBbcG5IwKPNJlQNI2Gf5zf2t7mAX4mf_n9ybyrBeyzRLFTKtV1XiAqq3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mevtO0aKXys2Akl1C3LDgGBA_sNw7kZ4Ddc-61VJ5Wagxwo5FoqkL1KZfWzeLUPJw7Mn8dhevzjO-78VfDc3E9ssOKLnGIE6KbSuL2w5kaXP2fbXDruS3L7JbI4hmSc5Qa0mm9niP8aVOhA2Ij5s0GBXGOlWrwThtXLM-KL5FNER_XRo67LpQBPCRyyYXDPKwOUXe46pyQF_VexSWRNwmM962kAAoTy-ea91YDfOClBWG0KlTeR3Sca3n8xXxYu0zmdTLxqvVIvyG11sjLWJr1AejKQNGEMZJvTvfAaNRA_9MJcXFm7SMya-EkT3WQWx7MXOB3iMnR-xAXcb7swqcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=lAIDpYCeJnAduUG6mgnl97MMoOXbDUeQ44ns8JsIjUkcRlAsHZg4hql9OQWOSRkIxDWF7uhUBts1ieg3BmOa2zoB6F2SFItxObJTSBgFE3d6edy07jBBShnpvql8KA7pH0BrkH5_Ue_ie4W-O7NQ6YoGIEbGE3cuXqKAHBGn3XN-HHbMqUqoebv9d2YxafQmFagBwlmO6QVEzvgmiuNuaEtvSBzCpdUy56-zxY1CSJwlS-4Z7-1IIXs5pI1qj3yHX6WUuYqoN_44ggAnEr1aRcj7O6LPOjIpGM7xrlIw0csGELICDmF94qs7oUoVgF7B2TkHdtEFL7Cif5pS7dv_wIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=lAIDpYCeJnAduUG6mgnl97MMoOXbDUeQ44ns8JsIjUkcRlAsHZg4hql9OQWOSRkIxDWF7uhUBts1ieg3BmOa2zoB6F2SFItxObJTSBgFE3d6edy07jBBShnpvql8KA7pH0BrkH5_Ue_ie4W-O7NQ6YoGIEbGE3cuXqKAHBGn3XN-HHbMqUqoebv9d2YxafQmFagBwlmO6QVEzvgmiuNuaEtvSBzCpdUy56-zxY1CSJwlS-4Z7-1IIXs5pI1qj3yHX6WUuYqoN_44ggAnEr1aRcj7O6LPOjIpGM7xrlIw0csGELICDmF94qs7oUoVgF7B2TkHdtEFL7Cif5pS7dv_wIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8LaMf9oZgUTyA4L5H7a44o0HmoXJddnLD-ZWfZtIa0DWqcPq8ooXzXiiaPam7SseIsE45C99PZj5-8qH6MhVIXEz0VXYQQk8jvlgzs9yKH7m8mkrDtdDVI78FVtpTLPFmdjLa4w6RVEKNQiK4NIX4u1uNTdu_zxqzNImHwwoyBnR2DKEZbAnKrMrfa5rfOcE1R8G5zBuN2Dy-E2Xw8YtatqrwsDYMQCnG7QxSlf_lKuULcMSI2ioPFE8htjhE6_nEOQhyctXwRwo_tWslGz_2dhbb31YkyvK_a4v_f4qX-R0mqokAUQvzkT2aWMRyVLI6wn01ArXSXbnJuDg9ohxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5a0ekIamap5irDp7nHn7R-hkDTxNRaBBOJiOZ2Yt8tJSzc1CE5KpdP0cVTkCpCnTF1vcsD9IcDIU1H5zcD2zmWXj5Yao5JcDQvRSzDcwk8y9CzMfcu7rPXFIO-YMePhLPN1GNXjhoL_Pmhe7IH0DG9f-pPtXlOb3o0d22S4mGtGMC_R_yy_w-76N9Z5wbksrZr0SRN6SLdfrL0HH7htSb41aOxANcxDFr_Nipuprw7A_gkJeMMgj1Mt_BCiM_IAw8FVeuSv8xV5C2lu7HMH9HD5vmrWjK2yvPv3YZxQootL7GkbqkH03I3bO6HwuDNGJpfDhABBRuD4qRyXfZ1EKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj9iJNDpCZCHAbvwu3wV3ePalNWmme9gkMIa0W0UZVYYVR8rmu8zNxqFIprj0AcKSw2V30LqG3YYbZD17m2uvX9Zegfv-xFpDED9M28nLUlefi1qJIfbxPXBZzKGKY7EtzUWIt5byZh2d8MdYj67G01fadmy6fimxpNoq_Gh22gK5ZSwsCQGs2UbnaeAbtU58LOhXzBIXGtIKI9j2BpatBN2SevYZCKUOsltW30RPBizmlsYxIhCbe-LulP0BVpFZqRleDE02lBwRyRB1T3_Fhl47VaMmy4Jo7xG0-tsryUR-medNJS0deCp09n7-2NCXuSE5-cTJFKsyXRLHxd1mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH8CrXBwDNEJ6SW-bnZ0P6AnoHDFfG2kAKgITesqrC6xal9l6kOXLp_PKGY7YmswCFv6lQK1yc92ByD4sFAXaYAqpmjQY6t4TGKWTAMl_XBh5L2PCQuJa4lxLD7wLmosBMHmybHf5Nnd3S-cEY4veIBUHmlRpYZl2ibVBh368K7sL3c1UP_qj0qSbBoJfMFOZKYk9ffn9MsG3w3ULVocxPBsddQI9437sIXoYy7nGuRkcLKDwnMCXpBYxVvuN8D3TBRtcnZWGrZWdtvKmoWPjlmZskLpIA2Pm0NnCgCELbrHOCRWXTkTBp9LjRC8tgz6nHHHOXzGTsUErkbWO9Sy_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=SBETceBAY_cmFcW9sPrrjjZ70PD3KPyXUVIz55TUoarsV0x_pNE7VUtcRLJpz00XmU6io_vR5YS_nBf8W2AOYqWD0WP3EvvqY0u71R8aotUqUYSeE7XvFLkFO0uue4IOnCS36n2zkI5XIIQXPRogqVx_Wp_gXaJwBMAfOcdf4KGc0Q6_MXdBTkyhaDfHZEXwd2W4OUn2QnPGuQY4azIlZ7XcMPx-R6YUtdn0xDhNHyyHvTWq5WjzCrm-1rjLx0FDNsTdJqvczBsNW9_5Rnu7h8RA1sItqH6eLoA4cofRptVVgUnuHBrRm01PyfFtR8gUWi0OVs-78vHLQ5sL9efpjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=SBETceBAY_cmFcW9sPrrjjZ70PD3KPyXUVIz55TUoarsV0x_pNE7VUtcRLJpz00XmU6io_vR5YS_nBf8W2AOYqWD0WP3EvvqY0u71R8aotUqUYSeE7XvFLkFO0uue4IOnCS36n2zkI5XIIQXPRogqVx_Wp_gXaJwBMAfOcdf4KGc0Q6_MXdBTkyhaDfHZEXwd2W4OUn2QnPGuQY4azIlZ7XcMPx-R6YUtdn0xDhNHyyHvTWq5WjzCrm-1rjLx0FDNsTdJqvczBsNW9_5Rnu7h8RA1sItqH6eLoA4cofRptVVgUnuHBrRm01PyfFtR8gUWi0OVs-78vHLQ5sL9efpjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYxW29kEZiT6eqD_PDtQqLwd-e9R2TTMNiBuJT-jo1aCL2EFon1XA0ij0vHaUgmcUzkywrnvpG7Nrsj7p2jXMni-6PuSMcNcihQAgjFOXbukfReaqnbIKxtCYcERZueOOjsvq0SY8Xeejo2vXAWqvfMvsQrHkXI9bMZVKLKjxw21c5nhnUGr8X0hHj983Dks4OIh40KIKKAd26b-gXNFhIDHJcbnCRs1fHa5MZvSIbFnIOPflAJKYYocmlVp4tpvcccc09iSSVdkIMwMSIy1H6dOCL4CgFgoFcbXwqKQ0SRvuphJoDMjbHZ0907f0wRp-rlfA1IN0ZHd5j0wBI5Obw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=PLD25xo_p6o5nzmxEUcncWk4ff9o0dP7u6CrS3DApntR8H0ITks6hIIe-7blrIxYnvLZbiBWlFPWGXrlheaNMwy8ysRRNrylCJ6S9gDC1ITtjENxGJG66pGrtHqZKBvFSVvVVme-TSG02af8k12uJptFHTyJl66ip75QVXiauzWFTV7gU3gzLWkTODlVUshymYTy3d0WsuZl0NxebLMMvHEyFpl-8mHW-aCPdIuA6YHV-3-AVakz8RJF4DHRmYGvmtpQ_mN7oiz9Ut2r_B6GVORf7GjRjEi4Y41osoWt6mQdqFZn3wrE8sZKH6X0rlJJxreQw3qWLgMecrv-AVQJFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=PLD25xo_p6o5nzmxEUcncWk4ff9o0dP7u6CrS3DApntR8H0ITks6hIIe-7blrIxYnvLZbiBWlFPWGXrlheaNMwy8ysRRNrylCJ6S9gDC1ITtjENxGJG66pGrtHqZKBvFSVvVVme-TSG02af8k12uJptFHTyJl66ip75QVXiauzWFTV7gU3gzLWkTODlVUshymYTy3d0WsuZl0NxebLMMvHEyFpl-8mHW-aCPdIuA6YHV-3-AVakz8RJF4DHRmYGvmtpQ_mN7oiz9Ut2r_B6GVORf7GjRjEi4Y41osoWt6mQdqFZn3wrE8sZKH6X0rlJJxreQw3qWLgMecrv-AVQJFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1YFnBE136Qv0ZpbHcJf1iKZUCFCKPduuKNLK9KvRDQs4Jx0DhJGoNFTMzJJ7e1vKzsCtUroGtwB62xjRCesVXhwPWBEdkTNpqq6VsHJfAQikulfhOV2AoArKhGzum1IqrvfFvyI2yj5zr4uSqmWavQE1AvouwEUd3BFOm1_Va5UarskoCsAl6zYonHNJ1dGeep_xuTXsbTLnzTNZxMot6I4PZa8N0LmmjpO-hjdfRiGmhgJKcvO5AupaFDMc_NiRrBDw04UXMtxeYm96nbc5XXgf_-hbMhhdawlGPSD4g530L1xU_La1tqaGCb9HhIrAPMEbVQu1C3B4yRv76fZFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDDU8sNhkw6kycAXPfQ2H8Yrphk6n57MaQFgOqN6NmSprbm7xxkFwoOAWcgDCw9SlThAmcXIFTchP_Jkko5UaZlIpRK-3tkLSpBYuMC6yBPTvFb7sUEovtxOoGP9iOOO1si9elG6RcJuKYRGzhqp8hhSQmUIAi-9E6IQnSukhvBtrcJTtesnrqx16GmNLLq8try_s4syLnsCsnIaJK2_opyypMedRbUT6S58o9UFk3fs8go8hIsxT3cRCi7X_K7k2Ryip97-kq7fdgN5IqGoGTgzYgh8eY9q4qNz4xDPcGBOppdrkaXKospTNCSq4pmU_2_E_jSo35wh5JEs8drCag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=CYS0LrqCn9YyV_6AoVbOPbpulBgMwolwN4NFV64ckRLcq2TFdxAATESIw3eMbi9F0fE0uLK0ouoj1_cyiJhcGtl-i4Vh8szkI3l1jAKIJx0cTCmZ0hR1RF_nspf26MdSWR4dfcLWQ5652He_TBiaC-nF4mwF6RTCXfDYrWglz03yMTOEzTP6fTAQ05X4xln_8G1mVKGjHHj1iQvcHSosRx7jONcB2ktwngHgiM4GANlLvxLgqAT5e9b5xAEziHen62GbXvsIbad0_4cVxlr0pxqEkY1jGtF2Gv7gATryOp2EaIfDPH3bcQdt3nvHLQ64Lhd33Al8H8NaojL6Qk8muQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=CYS0LrqCn9YyV_6AoVbOPbpulBgMwolwN4NFV64ckRLcq2TFdxAATESIw3eMbi9F0fE0uLK0ouoj1_cyiJhcGtl-i4Vh8szkI3l1jAKIJx0cTCmZ0hR1RF_nspf26MdSWR4dfcLWQ5652He_TBiaC-nF4mwF6RTCXfDYrWglz03yMTOEzTP6fTAQ05X4xln_8G1mVKGjHHj1iQvcHSosRx7jONcB2ktwngHgiM4GANlLvxLgqAT5e9b5xAEziHen62GbXvsIbad0_4cVxlr0pxqEkY1jGtF2Gv7gATryOp2EaIfDPH3bcQdt3nvHLQ64Lhd33Al8H8NaojL6Qk8muQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wxv5Hx55S329skliiOOuSdZPpIqkzk0fg21bQvUFtADL9mWK4sVfvFWsEtLJsCfKmyJnUDSsPgNKKsIc9IWIDlIWDRlO1lOjwc5QPq4iKZ7a-WaARSGjQHkTZvQC1fJhgfwtb11WaDyxNtd_O4duLGTbkQphCd9C98JJ_Qyep8sPFCS42CkeGtULBtA-wWHXN81pPbKV1Bd2zGIQQTyzd5dharv0cDPa_CoekW7-EPD0PNuM4L2gGxH6WNdYW8JLB1_PfmlcRGhxSAKddj15Jbv5c2ew_9CqipMZrpM6ojgVN5BfZL2yn-pG-LlDe9gA7brmbCYvdFKcuVyrBKFRSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNkTtpmHHdCnwITXATOEcdHf3oPTjzYGy6slNhokVVrAq3nQxDiXbey6j5BzTII3HCQXz0yXKdBYVEdhbSTBLWlBQNWMg44aDUySCGdIW0TTyE2mmc9m2EPmXAcLwjZRBT9FiWqtW4kDU9VLyqeLPF4irp194244Y-pMgqtETT1ey_BkCz29BymTJVfYsHxFzVDS71JTiZ17JC4I_fj_r8rBCp0FDfFJ9jI7YMf9BHMk44HqISqiPbuRiSyi0p2709sLlZLTrIanvLue10HzPBXPw9T9l9HbXLuoNQ2jH7TdVXl2LNTbNYdmi_oPbVT8KnSdSyaRu5h5Ekgr4smN7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=aW9qSc_dUg2XoCnq5iAmAuNm7Br18VWHXK88N8N8fzc3-EBbuYKq0WhD8Wz-X42VQoW_EPMj97iH_SJEcoohraZis59ymZ_wFHCghJvk2fs5MlZ_2ecncFth1SwNyyTCo2KzamB6MfHfJHCir0Ja9bFpsz0IU8EIXOxOp6FXiVKniwaPTyGQwtJUjng6J8CAaZuVDpVkAEdHn8t7zy3YlJCFb1kNA14jic1UFj3BRsaAqFQvIWBoKk-_p9nukftVaVQp_5vVHZzODkJu5fLovPK0kVPrLPtVKohBb7S4sdOxo9lkdj41OQRl0YUbHdLKKQbbEMwZl2Q1VrGb9CH5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=aW9qSc_dUg2XoCnq5iAmAuNm7Br18VWHXK88N8N8fzc3-EBbuYKq0WhD8Wz-X42VQoW_EPMj97iH_SJEcoohraZis59ymZ_wFHCghJvk2fs5MlZ_2ecncFth1SwNyyTCo2KzamB6MfHfJHCir0Ja9bFpsz0IU8EIXOxOp6FXiVKniwaPTyGQwtJUjng6J8CAaZuVDpVkAEdHn8t7zy3YlJCFb1kNA14jic1UFj3BRsaAqFQvIWBoKk-_p9nukftVaVQp_5vVHZzODkJu5fLovPK0kVPrLPtVKohBb7S4sdOxo9lkdj41OQRl0YUbHdLKKQbbEMwZl2Q1VrGb9CH5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVtwKnpTPShTIk_gtBJ9Fcx1exlz6QD_6hUrs0zh6Wv07Yvo7nLK95h3hnlDDkjDHPZDlKEu0FX3qhYnm9QGY4w5E_DkGo_5IiT8hbxm9vOwZcVfwWKLxhkCLWR_jguMdeT31KCUP0ZFHLOVvcTI7WIZDv75rsb3C4LS00jgnxHquDF6_jexe7oTaawq2aaB-jvWhCkDEhAhwz9gzwmnObw9sCCbnXt1W0Fj7tO7ox3TqFYpUpM8ghsaKgKr4nvKwfE9yS3PROAGprSCsjZrR8cVzK6RPqUrpRQluC4VcHc21KFXx82rIEz1nTe7kssrilVJolMCQJTEiPuVnRGOig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoGhV3a0YBMWQwP7CrtK57nrudokDvvDJeZASZDDEn_J17_ZtxnWF0u40UBzd-K-ZvuWzTiV2Hh_4ZRCormYMqj7EAHc8x9aXD6SLMbDnBsiqf7ZkpyS4kiZI2BkgQudb3znMY-wc7yS8_BSuHSEBzVuklmAZWtyBPJ_-pLQvT30uK6rhtUxjeVKWNEVT_Yr6z9qcTdTwSK1lUoGJ4AuZcqnbOliAa3BiYuErHShuaBQF-de6jNB7864zyZQc2-QdS3Lo3Dfr_4GeKCkMy9Q-fWC0KTvWB3cWe8NBdBTyWl1I0qmVbKPMZFylAfVOWJNxZzLGeffAvbPn9Ma53AwpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDkDLLGKCBrv4itiXfbSr0rzsJTYwprCTC6lV5jLtIWlfuQDGC9P5BVq6Y2Vd5PQoUhE5ImVxbIjLG-KyseyMuhEwJB2r-mxarNCdfoHjOP370GeWrYLD-qJBEDk2XGu2QZXVpVWc4um9gOjnu_5-cv6fWULRqVQSdGetbDf8GVEQ1M6MrMUGnWosjjjb59UpT2k6kIQXCG5T8JZSkICXMMFyeRitvlvLkR2Kx4kJZrlSocP-kLCJqGipH3Y4PyEaInh_MN2bRGB8pLB9F6YcxiRUfVG6H9Lg-6r0fKwfuTdOQoQwaAms8SnGfzpio_mfEP3YoytWAwVanwnoxgytQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz3dJcToiujmer8EAiyhgIk-3wHUhbmJbkY9xXlbYpYs3CNCbG-Ngc8v6d81bEc7qOHy9mkj96jN192NDkPXol9VdXwRQMG6OV3rUNiqYlR1cKIiu9ipr4gAQhVxBUOTvQDb3s00oJimkow1T3dGszAHA3iXDtiVLRR_Evx6zzIxBIAXxIMC0TL5ECLA27tFvfRDKP-9L2ztyEXhFSWK-lxtMQ3V9D9cwkTk1LEc3e9rRv8SR6ZKUwSyGoNc0pczsSSsidbxZtWfMoSK1hIkxmSX61I9G_rIDKliacAIfPybyiyZb5InL2erwwlezlLTE8YkvLSWF6zOVbJ1RhS-Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj8jr4bzz2tgNUrOGm1V40pdc50KdJAXVRCdbq1peY3M_msueGIT00Q78U2o24meP8KtgJdYd8g66KfZAZBMEWk8f1o5nQcTLS2DT5Xb2Vvc2-yGB0sD8fOG_P87Y8Ezrctk5g5eqAGdWPY50EfoQFJ7dqcfcS5e-JrfhsHwZjKl3EYEV7CimNoKi8sEFo70PV7N-sRa5f-66Bjon7k-zWRpHu60D_YCXiHWx56IhbCbwM_R6qqJoQYobL08AF2BRoy6ZxXPtWK9Gw-gTYiEIZv0v33Pn-z-UlPC6lI1npktRuw2E5aZVUNi0iWNoYlJ2LJEVV-ku_HYh-ShADk5bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv8FUcdAP9qouj-P_D4j1rn6Ai_3MDWmM0ABElESFmAMVxIlJP86suy9V5VaQ5QHOn35sQ4RJG7Q07RF9ZoeKezZFCVqUGmaMi8oYHL6AX_oD9Q19dkPE2aUVltShtCttuQ2DHm4TbaJ5xJf5r0xFm1RNyOOYUz0Uz3IWJmhu36FFOgj67mpdSeTK1I875gG7qhr99aVR2ucHzthuSgbDsPHqLrG76nPfS8uKNaPDXB_kepQox_4BI0gQqYFCJ3O9NnTSpajjddqQOahG4jQVkltcKRIp4Tzr6iAddVGpPYTU-ay5PgEjf21x-TLn1H7eNl4Wg7ee2ZA1dxwyAZ8DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJX2eIoUctTJLxT57l4jefukovejINDiaG5nDe0_dBEf0AjuX8iecqW-zpqfTI4pzkI_4GlKqBGH-SCRVCyjEEiY4NsOwAljH1Vur_C5wkOHtUFaZFFMYeB12zplsIfpn9Xfos5FVnGrYrA3R0XK2wZ3NlEAPJwlhUf2lLGd37AhHydPNCAKxeLrvhfLZA_kZncO_1rdx-kB6qtFIBqG9kjyLAmmrWn8_cY8BR33Z_FZW5z8kWvG9jBq8atLREQiNuprk40v3ZuC4B1oni7EKtgDg9k19EG8HMPRnZqnaZWLMjOs-B_YGUbR5tuWK88BfxX3Gd1X6cOxCbHi5R7VqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4z8QdOyBoHkhYmLXSjkOAzpB0hMdXPl24xXGz1GEvGhsxQKUsEpMQ47_rKMNzH3S2TsbKe-6nMFxYVnQi85Os493BJXLl8opMV9rETGcm9327esXbZ4QHcVaNbDv2fAkkmdjIYIWzwYDZ6dfHlrhxusMSILfARLvQ8PK7vUU514fj-o3uL-xQlPQvrdEit7RCBl7mu2Gsgck75Rt1Aw5sIRkRlHeN5CJuRWaakkACt_CllsgkAesqXNob3ta6OPLDwmwkXooQmdG969YMsNWY8Fi84J5Z4fkwpTxUut0LSNaiZkWRsrtsxoLYR7-GzbnT3cfyAOJdVuVwr9Mir4IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-xsIKslmyaTCOujqmig0sWM8YPNnRqgAKcbSFBpSUif2NVlGP2fEvGP0lvli78TuF9CSzh7wlopRvl1uUuujNn6zo12TZqCeh5sR2cJihgWtr542ABQA6y9RKKGnD4XP7NH-apFYgVLlDVUzZYueJ6dWbEUu6r5zwlJZTW_Mc0GA2XnQof9E3bF5vNFdgBNMIHdZxluZoybrULBeou6vjjUFdzWU7DONorIfPGL9L8u0AOGfosivJjcSSQ6jxr4Rb-1_2CbRnR3q0PLgbzgQqnnOu_BBe6loxT-a5E8_lEsbb7rm-aMWA1QVGUW155T1mysGVVUdXzKv91lOtYp_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB8iiB86tmgjCosgHi9bbDBCM1BfGKy3lhw3d-hbWWvDczOQJrHSoOhNZEvoO7QmlVf8HcLUjqmmNSTRb02-YHFrjOTiznOMXZc6UKW_50YVlC7gPWyve9ONLY7N9RKjW0Z9TRhtXMx94YUD8J0HjwKRC58AGns7Fc1I0Zhv5siazuyuuROY0KWBD1vjavyUKUBoM-H8Re7Ir02nfkNg1Pf0z2mzItUwDfeeyEjBu2SZh5JmGcB6ExD2hRaiqtzzL13v7yVUBiu5hearBR3Fm8QjqT5eMuEsCERDx6PjvIyu-788Ib860xaSShu-hZ6gSTVxm291mXD0MTTLtGHaTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBxKrdT_Umnr3v3qbGH5dncYzjYTvFkpqHEmt6Z754vzxZCSBEMk_IKC2fWShi_FjA9bvfCl9sND7qll1RxeCZQHaB_L8qCXVFgwRH-M9gobka5j2pyVdHorB03GsvGUkkEW_86JMQkQ0QIViMRugK54uovH-em9i2_M4MFPa7-MefyyJZzDsZC2j5haIYVC4W_Drmso1CgNUEHP9UuzOvoZEASuQw9ShjAB3gYlhBHdTVTN2Onofj4J9ZjVkhM2dKNERl6O5DtNgPdlZryig6vZAnuj9s-MeIm5kLbaDD0Zls6LpB3HMpI3SzxOLHEvvnyAsltkweMS7C8eRpfQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3Run7yTzOPD702ao3nj_SPs6nnyPHUtZB5_NK5aZAzA2II-acIc_kHuoh-k7tlfDLuGRa5Afbzz__2OtlJjVsRUj1cQKVgI248NSvCzRYG7de2wrfgia1fu4AdxQWBcNHzZGZ5hrjH7etmGnEAWunpysglEDwqW9sba50tBcHuYG_WNaKCw98DIywBBXRrj3mBUz7mO29YhJX0lKh28QCUaKaOf-gingnTTxHvS7iC7OzoWrUh1vwD4v0z0I1neel6l39XwJ5AjPQPkClQ_wULPYh2snHiqmuLBsukZKB5DovZThdg3VKnYUTmz0aiFC3L4EM3bEfOdq5BKuu30IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSIaikfuVUqBe1XLHsTY852ClMxBEy8kla1lsdauytcyCGJSX7MHWaXgFK6mzatjnTQ2Yk9KFquhCxVy59WP3V-43_vIySpr2OAx_RE6bdycdgwNfHYr0xmzvR0_a5cEqsfAvyYKaT6VtOKkBBRWFUMNQZZSYqyJn8GlnXd2xTI_HTzPXuTjuZxEEfexUmFnXOa2HgQq_ROa3jiAEMqRMgi9wFh8ZLhPlDHqCZIPV7qCeaRpFN9Tq8HKhyDhP3LU3TeigwmDS7drI2jt9ENhCq38BjbtBw7oD37Gb9Yb6HPceTWh_Ih3PFRvI5MvUNdM0bueX3NF9BWACsExbphKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekOM_4pndY2QDdDFaUEJ4VOfCvBXUo3uHG9gHB63pV95x0T1py1e8Xv1CRL-ecVNx9gwaeDCqpXju_HFVOHHWw3dyL_3VQlTSe0Y668Nyzqxd62li4DaMDBg_0uiEZI80VkyUgeEHIqRKks-K15d86v6wU61-89WvWvqbyoKnk9-OId1VIGwpZ5CIzo13SPY3YL2ppdPsCaHShdR6g-2iUHpWkWBe5sj1LnM11Rfp6mQNKeJBkMawISrqWbVL8X6DdSZN-bteDJFz15YJP1zPzrTcml654My8hYsbpd1CIY-AD3SdilKRbWl1voKaHM4SK5Fv8pIe2RXYaW9GCe4AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
