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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkMe5lVQaTHrrQyXRwM04GJLifBq7lrJcnGsI91Paq_M_NxvYZMPzsF2iMmogOwm5M-oJqL1nZORWtO3-Jct0sRoewUEoebW9O1Xvp8MKPziJ5UgX9fpCRRyo_pHFrKf7cazjRaTJfCPShDMFoZSpndAk3WTI6taGvRN6sTVaGbhRIvP2TAJNdlRPkunfty5N8KC3vA7Tua_T1D2cEEjjWetv61J1tM6DHBOKviFjdMb782DGY1sQWSj6o1C_UcKEQstrIZiGx5Vz4EpJPa6DRJg1dTH3aS18KNji198d17w__hGtE9FClI-WQGCsl70WCChGEby2DYYZQ9hEFFoOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdWYGX8n_NWY-4Q2CO0VBeefbYqug6lrFNllDEH8E94-vtQ8oO9wny_54zn3RGS7_IONpCI8U4xnvKhf6t75gw368W2LY-LboDRCgjc1LFGVaPm-u4j3qUXyWks-aTIc0E5xwjc5iePvWEZ2-DRtTkNc86nG9oRC-MBW_sPnO6rqowRIy2yMAS29cFxNorJijgZosq9zn_otGwwOV0WG3b5-rU0eAoobrb3gP1hQMZQsUfrEPUvdwRlG0KECoWlKLXAwVKjMeVJLEbS7Ci-4QgLSXLIm-JCwd6EdnE1VfA6xAm3ZtbjBBg-vkmi3LxogHDeXfAUzKYTPhGpJaLYC0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2-x7P8ElDUrZSTP6eP5zDVZzAyN3vMKMzm_C5OawJLAH0B5VCRmJ7r3o9Wdb9BjBY4aC20oUpu8t9D8Ri_aUTdZ_6ZG3ZQo_pP_pvRRh0tjIXLirlr51Rhgyi8wMmuBlhLc83QL26n7L-zKOZF72qzrBCURqawertlBDQPjYb0z1iXiMXzEYjUqjkMIO-IHu-DqMPpHbJB1WVOP3Trrl5vt6Sidq5EXrL57oUTNbkY1gEDWMylbl29ZU-BBvNIhtMjzaMPSdbsjWpuesP1P6apc4dxSo7Y6y5e7cZq5ol-XLemg82x3KI3mOuPaJWnIj5lMHCEjEL_H9oMHrh-PIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqnqInKe9FK9MlNoWB1aDZwImx8fLg-Kzx6OEztOSkNtS0dh1Kp9Wa3STzvaYBvKqgdhzJw8DNG72CbhnKlvJ3SvwYSq_6qnFHlweQxcmHQRX0YlK40nQs9YP2Tp9FM-KnpohCctpx-fNutl8XTnwgFZzU_K-Oueh5uaAUgFf4oDbSnCWYOl8v8wDGcyxMwoOwklcXphP_65-SGIY0TiAY-7ilE4N_K9SE0ZK97qaqJkgpO6O-dJUWJvgYOd5RZfOeruvC9WA8DCoyjT7RmQDNhEaVIS6rVZSCkSYsZduEBls-wg50rjVK31cWs2tG7MYRVT1YcTdjCO3ukIIGN--A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=pT32eX7wFRlBPD3-7LHhTPtLjGbNzYBGn-9BmPBdNGXA2X4-QCcm3YyMa6iAsDtikFr5_4sLeNJH3HFpb4i6VFcopX4fjRxou4NuCZeGuDYZj_kUXZ1j6yOWshS5-QKlNFkQzn2p3sT2uQ6uutgS29uNlCii-h8wCyUEzAG2KBZnzZ0PGbA8VRYoMu5jIhLvgP29KQ6LbkY8Kpzg4-tbYlGEQYUX2cl5vE8vCVqM8lOp16Cl4sMOTg7wh8x0D6OUuv3lorOWq1WgC8Q3VDLjfX-qHLW9yYsO6wdq85E4cSvRCXbSUq_KVacUU2T-E2jmmVGGlKwvKgu31CFTfeC_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=pT32eX7wFRlBPD3-7LHhTPtLjGbNzYBGn-9BmPBdNGXA2X4-QCcm3YyMa6iAsDtikFr5_4sLeNJH3HFpb4i6VFcopX4fjRxou4NuCZeGuDYZj_kUXZ1j6yOWshS5-QKlNFkQzn2p3sT2uQ6uutgS29uNlCii-h8wCyUEzAG2KBZnzZ0PGbA8VRYoMu5jIhLvgP29KQ6LbkY8Kpzg4-tbYlGEQYUX2cl5vE8vCVqM8lOp16Cl4sMOTg7wh8x0D6OUuv3lorOWq1WgC8Q3VDLjfX-qHLW9yYsO6wdq85E4cSvRCXbSUq_KVacUU2T-E2jmmVGGlKwvKgu31CFTfeC_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=HbgeOjVfyqdZGSfQqal01l8RQBtakpNodZis9ojAw_sO1EKeD6rw9oTEWQ0P4qWr2BzyOpI3_By5rz7Z6IvpTwm4ZXrdO41UlWeDR3b2pqCvQ18qZN5qE98C37z1u-R0JO8nuKo7TeU7ZpSUak-ZRmEbeX4Nrw84kk1CwCyIATBVRBHiPdcZddRKoA4v87j1_WBtRRCWMdoefj0JvGdsU7FfWJZ6_QcQMZ7bVwBedTdmuayow5ouKF0QQfw_O7-l3MNDONK6W-YtsBbhUJdcISGkdqc3bHpgmToeZFGLFATQrIYJ5hiVrce8c87KXX_kGbNNEH3Xjq8t0X5ECJkEkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=HbgeOjVfyqdZGSfQqal01l8RQBtakpNodZis9ojAw_sO1EKeD6rw9oTEWQ0P4qWr2BzyOpI3_By5rz7Z6IvpTwm4ZXrdO41UlWeDR3b2pqCvQ18qZN5qE98C37z1u-R0JO8nuKo7TeU7ZpSUak-ZRmEbeX4Nrw84kk1CwCyIATBVRBHiPdcZddRKoA4v87j1_WBtRRCWMdoefj0JvGdsU7FfWJZ6_QcQMZ7bVwBedTdmuayow5ouKF0QQfw_O7-l3MNDONK6W-YtsBbhUJdcISGkdqc3bHpgmToeZFGLFATQrIYJ5hiVrce8c87KXX_kGbNNEH3Xjq8t0X5ECJkEkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN5nNC3I541pcd6Dfz8w82fk-YFVwo10GvWhwGvmqsVe95NLPigkf7-7X9CBovvRcBbg4BPK55zcDaWgLg5vXBYaG-bqtBQmhQmaIU18C0U4A4obAmdU0fS9BUB9g0CbOhE7WE-8NjpvsJQkO3V5SBcpS9fKZGIQsnWo_LcmKSIrUvM_-KxYeoyxfulkfwJRLeU05HPz0nLERfzj30Lck7gwM_SX8bDNmh_S8upr_ToLlGaIi2RmBYc4PCv1Dmu-b7QKYNNVef1I9gg0c_vC-mXnRnSBoLNBLfPhiBPlJy01_UboCaB38ywjbg97N856iJT9Oo0ViCKji7keQk6ARw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnYUlXFov7Xvn3A6xJb3IMvorkI11g3YjOrSM-SCKUfki3gmbj0vDCH8WlGeFv5hbrfG7-TiqRP0iNpJIDou0KjHM-8pjHyiCn7w8ur0G80YobWjjAROp25UFudrzjEGsC6JmcCknMcy-wrPlIO2blVTQKtGwjn5zxFAVMI47NhxUwqX4X7LKKbpS79oIejlYQh005PN89TUYc5Y_LnSSqmV5_wuevTFa-kkd4SkSA3GVyi6JP9uCk6csTMFKZca7oJ_nqu9UsjSIgwN7PWLqsKSUmA_kzXUgauXce7MCid1fnLRMKX5ezm3x-EbTNSUx_Nh6XdRQ-u7IrGaqPQRLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CabZuPZ8FgaNAczikavOUCeRQMPSZRqhh0ikmPkhX_EGXWs2X3-TMoVV852blLbSSYgyzUPeUBMPZMYCKfS1nQ3kY2suWSjJHbD63jQnTdjPvAxkNqev0I5Ae41L9QGW1pQphKhZrNQ2y1OuzjWCle9j4MIcNkAlVY-32xBgHftF4g1Ngw5nVtihzdDBpG-umgCjxzgxkrB__x7Nhz9ODktP1M_NFEmLlcXos64lHvTHkXyzZcPns3uaLMAo4gjsmwRJ21im06yplfJF_xuX-GAmdhiH35JirFVqthPHl4nGKr71N_M6kTgFBrUTTNqUaFPOkUMd2UdFv1sXEDdXlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=QdiXDLG4qa0ykDRohEcdbvwhaHjLBXc7_wjd7e1cpRBXVC3R8Pr0vbtBO4QTXJ7mdIc3Ic1TllG4JZlW6oxBsW739gt_Ey6y0p4u5vRDymN37ZNiTo_FSY4_7Eff4PQuPH9Pec-8nypDUgeKV5-68EHK9lXj9gTcFyBOblxMX0dEQLs7CAxjQCpH-pWpH0nUTuf1H2SWw3845gWk5lSt5z-4Xm1nlnbVirqfP7hTl8xp59xpp6YgC98PeibrOyOX-3GLoaBl4ck43xo9Ioa0GwVFrTCdgI8uBOyGrOxlGL8ZQxkQVfEhXwLU5AEPqfghMJQz4jq8rDsOc_tkd9OvYIll_csYLZTVz3QVsRWHjLt-V71fqqQ4M3Qz1xTxstcawNVABbZAhorsDlW7mGeWiwURYHq5MUPFQOw3Eb6In-pJBFxkkfS-3-XU4f98_nPX0gTcWIGAJyKExr4VB4IsmEbv0q_NFbAMZyDjITmTqZh065LfwjzmI9gPdpUWyFCMM7Rfvx6IM0B2O6lcwmrVh3-i7tNvF8idLRJ25PZFcD-rl4Ah9yTxO27TiVYCM8dS-4q2IeFaUBIKXlqknWmfqx4JOFHW3-3p8w9RVAc47snmmLy8U4P-ug4hGmwyTE4Z6IS6Jf7stIXdITrJk_nitSjM9Bl1PP_O3HX5kHDYFlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=QdiXDLG4qa0ykDRohEcdbvwhaHjLBXc7_wjd7e1cpRBXVC3R8Pr0vbtBO4QTXJ7mdIc3Ic1TllG4JZlW6oxBsW739gt_Ey6y0p4u5vRDymN37ZNiTo_FSY4_7Eff4PQuPH9Pec-8nypDUgeKV5-68EHK9lXj9gTcFyBOblxMX0dEQLs7CAxjQCpH-pWpH0nUTuf1H2SWw3845gWk5lSt5z-4Xm1nlnbVirqfP7hTl8xp59xpp6YgC98PeibrOyOX-3GLoaBl4ck43xo9Ioa0GwVFrTCdgI8uBOyGrOxlGL8ZQxkQVfEhXwLU5AEPqfghMJQz4jq8rDsOc_tkd9OvYIll_csYLZTVz3QVsRWHjLt-V71fqqQ4M3Qz1xTxstcawNVABbZAhorsDlW7mGeWiwURYHq5MUPFQOw3Eb6In-pJBFxkkfS-3-XU4f98_nPX0gTcWIGAJyKExr4VB4IsmEbv0q_NFbAMZyDjITmTqZh065LfwjzmI9gPdpUWyFCMM7Rfvx6IM0B2O6lcwmrVh3-i7tNvF8idLRJ25PZFcD-rl4Ah9yTxO27TiVYCM8dS-4q2IeFaUBIKXlqknWmfqx4JOFHW3-3p8w9RVAc47snmmLy8U4P-ug4hGmwyTE4Z6IS6Jf7stIXdITrJk_nitSjM9Bl1PP_O3HX5kHDYFlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyrMdEMEv5b3Fz3WwtMv7jm_tTFBdACIGPJ6xN-YuXhpFge0RocC9ACQziTzGpbb46skYVnqqd9TIHhiqbR4X_ucVKV6AAHWG6afsKHMjeXkYxTYsA-uRpk8yoMfT0Z_gxAA8OEwjjkz0bxMDSuSzzPeC-06f6Pzawu_P4zG7XwvUIrCRTw9r2nMQ5en94p-2sdZaSkDZ7oV7S-BgyAYeQXdgRPfEDQtMoWrbw34zHaTvQWfbuJO7xVbq2P_yYBqM5dcUJUmhV6CzaQ_avft2zAJQzSpap3FKrnb5XMocrtF46rDw27LQsMtJx-4_W2AaUJbd-FGQvKsTzBTH_0-XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5RRdSgKvyDdBK8jdaZtS4CacF5kmFH6_0jTLrkSv_EIF1-bNvHJ9frLo3OlJ5C9i8KWd5nIIpGgc2rmp2ECFlkHU4Cs9PGfRk_BpVehHBniqEHbqdMO3nGc_EhqX9qb7GV4PurWR50h9137MeuxcR67v_prMH-FhxMsi8RssmZ5kky_sZfWasQNsWosvnn_0JkFAR2dxNBueGoTsM8R9uMAOQw38OO1HOSNq125Sb4S2iEHuudSEtCDlKvHFrdoAe_XUCd2EtAkLrlK42iO_-qGCCDb6H1x0EstF0JY8bp5LNsmMECJmdkEx2hfZhjrTT-_9zY7KFG6Of8NBnc62A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfsoxQ0ozaqN3u6krWpm-TOgujR8nycsJV6GQZxo5WpHs1q-ZXBk69GWCdjlPehwcUrSONU59eMqmLyev73rZf_V-XDkSjb3Va_DCu0E-aLfIDHa6iKMDO0L0Ai6-R-xSKKrsrcn3lYiVlvwOeN7OcPEsQS80KkperjE8Wo8kbIKZoiDtM7-ry29Ui6Vhyg7tZiZpyA-3UxrXCf8_LuVmfytSJK9IMYDt3EKB6ftOuTkoGEylFC51m3I-8imssdLeprEk97bQ9vOsJ5VlnUleUBduOLUbdpojT-mtvnIBQvZfxULspX4i-qVpSMqsr3RYpsC3MqjXMPTHUyiMiyZmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-hQ8RxfgPduLYvANDbqgDORiVy4MJKWGMkOVssVSkmDSM74__KfxgUO8tRk2gWAhHQjKzWpoHipfnHe9vrZCyKPmCrmr9BZxIGxtKYKRERk0atSHQfltmjGtP4lA-l-9yMBBxyKYsYgZwn2oyfIeKYbw0WK6sxIRdjTkDI2vwAEJFaIB7lTmOf6bHD1YaURI_ggtYLx9MW0asu-c56KHb7bnqzBcj4LoKlSiRL3oKzOcnPWuX5_SNIOn8ltpETnjgY_2piaA1RGskplSecGnB2Wyrw7ia2Psou7I04a7WwoQu3r45fbL_maFlBYZqIOjhiqFFo1dQytYjhY4GjiPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9rIwAcu2wwxIxekQz4ibilIZWEJaM_WQcgYNzFI08kHRYoCemNd906lRxybkB4P9AuR-hZhbXpnx60MybIbP5g4kZKQx9TNfJr9Pc0pDu6OtsXyOjfPomXgxuaEgkY1nTnqcKab3FNPDQPoOa6ZqULJi2KmwJdMS1_Gdd-5m2ToHkK6UCPv_J_wfyrb1UIQsfxSEW07qvdL7ucK_0AMswgwAh0OU5hX2f8c6mhtZ5ekO337uSYPVE1afWZHJ9dwWlskqhHcEWYG6582rgLqOUmuJacdWsELC9S-fE1Ebj1pXyUO2oWeqwpDQdahfsyC-7c5xTgq5X8SXrR3gMWMbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErF2JT33Ee6Aqik5rSMt5rFqIvAUNu74sTDAAkmYFVBGBpjZw9JAAyXV9krfIkigot0OgsAyJkALHF2pLSWF_icvZCqeSHHANSxHpwvXr8e9iDnINiBFISrOuhRQgZDMS4HfBG9ByuV6l6RT7dMYLeB36otk4NivPYF6R_IotV0TYqvl6nqwj7yQWjyP8EjpvBOgp5JqZscK5ZyUGdH0ExBWbjMTmKM2fwpAtK5cd-mhDdVQDNAMx9NRh3Xq5WafCmeW4hSyVhvZoO6UGjQuLeczjInjCqO2ebmR-g_TGgFT4QMQ4my-LIeA0OVjI4DJrxCs8hC5pSNkTMB8xZDHNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=Ws1owqZWNEEqA6QnlO2rM5TYqaFueGGpF4evyaucef-KajXMFo3hHzEG9RizHz3CcS005K12n0fTB9zTvVF6YUyGnONOWYRW0-ZUXEmMg-6G9HBXzwgUVXDiQPaNtYrx887XJeMQS4yaJrssOYLowxlwrIA8jbFY8QISP6LnqxaAOgCl8EjU6OZCQHFU4UZFF0rTG8rvTi4h9L_A1ncoey6wND0Our3WYjEKirrAggvNpvYBoP3lEXjvSgt_DWRs9za0sxFhNPeMIY3_rBRBhIddDInyjqBqw2RqV1eCNAjNMopv7JtPqSAt-rzinZdVD2Yo_5bkNE1y9eDDkQwcnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=Ws1owqZWNEEqA6QnlO2rM5TYqaFueGGpF4evyaucef-KajXMFo3hHzEG9RizHz3CcS005K12n0fTB9zTvVF6YUyGnONOWYRW0-ZUXEmMg-6G9HBXzwgUVXDiQPaNtYrx887XJeMQS4yaJrssOYLowxlwrIA8jbFY8QISP6LnqxaAOgCl8EjU6OZCQHFU4UZFF0rTG8rvTi4h9L_A1ncoey6wND0Our3WYjEKirrAggvNpvYBoP3lEXjvSgt_DWRs9za0sxFhNPeMIY3_rBRBhIddDInyjqBqw2RqV1eCNAjNMopv7JtPqSAt-rzinZdVD2Yo_5bkNE1y9eDDkQwcnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrbfAxrchDf9ve9mdzkHOLVMlO_m1yB5kLkjuyrNArwiFJibtyhWE-aL2ny7tsdfbjYZ57zlQUK0wRqZvhC9V_X-LDj3QFoXYReqmWYNNfSlXhPTpdLeXy4waeeBI8ZbFDK97aubqnYTK4KeKalHpNTODa76zk04k74Rb_xpN1TIQBg4iIon3IxMMUdzBEhocuH554x9AhmQwGGc630qXehZzrsGFcGuOBNxnDJjGH8gpwKBHAe8myqeT0Ym5Tk6xLdpLpfW4p_4LTbK5mRtfe0uBgj6qoeApekqg5o2zGT1p11WdoFOwgVtD2fVCViHzymopt0x2f8rNkKbKRGN3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFz3RP_KQsLrsFrGf5Evqv4WVXo7fIoCltXn40wOQBYPy_extV7tv39JUGiM2QGZ3yfqmuowFaqQvC32mvYPsUBRc5jo6DkO5uwubYP21j4qpxtZwF_B5aLL2agJOnrEFWY7Kx5y9AUsGrlFFdziJZ-fxw_RIJ3GVGeMXSQpXq1j6IJ2ItJI7210WEndeKc8pwXV0SgLRZcShZTmNQyUvmSN9IPiyc3Fe7xydxTQGQmqolPmoXSszA-73e_Hi5fDwQDiMKSrImtJBL0z6nUtKm8yws_ht1yFAXkoVIkZ2v_28g-nWN7O08AvLWDTdB56DMkU5Jl_syFdGleTTF5MbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzFSUnXsbFG_6BzM93L9K-uJ8HLOtx9afjkSwhgzNWceuRm3NgOxvcyWZ_6jUb0PS8n7hqF5ckuIPjq1cfs5cGmcoGwiHyOdc3amqitfToqB-DOi7v_mia__BBz8RFsyN8rymkVbGLTlT9zVuQ0l79VxBSOfufvr5_HB9ZmomM8tMg5-NRdqOS3GlmqXL9glX_EhpElfDMcw2YhAkqjVCAMJdGqABkoxBEWLR1KCJDDYdtec3J6jYLCNR4f1DsHoBlaegM4a9UJybtqHYW_1-EZtDhy3z7Xf4CTymctf_vlCcMKy6bDdGXFRiDQSCMnxXKmmtYytsB7RoEQDijMpuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDE-RCjkg7QN1g0UFdA4kw5fXFKbqUvYPJuohrOyJHwrPO44E45sQVH84qQRRHgA4U_R6Vp5pwMA8BZdF5NsmWLsKjgiMtN59pUnNmwqFXYRUE4dx-xKDEsaO5vmaBz3I2XlSgaJCYqsWroWDk_Q-bcNitk06zEx0B4t58sqWKXCP21d9WIgPYm2TTEzO8abWmSWo5HWbRVVnkhcQf7u4m5FHS--EsQqVs2XC_gRQm8RRrrmBk2GXp5gx0IrPgLBYtU3GnGfKHhjl4EGD3Bv9Wc0umZA-GIH08dmCGfoNGEcPK7S-yz1Jkd9rrh-2G37eI8An0vdIGWFPphPUOraIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiHaSadVNLxYMiUTEUldAUVYNZRJTox_iOYZg-6F-CgUCud5ZNSVkiBDZF0XOpVt1AAWa_6RldmjBv5ytRCsX5_bgoLFGWKcwoL60Ko2tTtCCCPfDe8GsNU8ZqYuQTWoOBZPvBRhNiQQzrfPrcr9z7QlXyhUVl-rxBvCU3l0H8Zpl1pyuYSMplsQNmj2kTPig7WYR5QKcPj4lCB6e1eE7nKt9bu3UcPuTDr6OlbDzZI7SpT5j40VgePSip-gkloo36UJT9XvSsawrbPf2Q9cfGa7A_5Xy_VDr4iGbD2AgSsXHDyie8Ng5pVc1z5vU7WFynXlrPmLQiPkrWt_MoR3ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbRlph_3uaIVpYekeybXMoXvPrxqYLWHatmC8_ChWPPYXdC0xQDQYOtlriZ-90tuZwtQP_APKcDfrAW5fF5l28TPe3wvhcrUulj-ExVORg761v6r39Q-RKP5SMWKCWNy12r2GOcbjkEZosA2N7zHpv4v-tvEpzCWagxp-wSeN3P5_wlIHe_bpjLj4oeCodJu9x_2npdbtxo8ov0qtIdKqzul_4fB7LyOxZTVKgRoiiOk5uvpo3h1u4oAepcjIzPmeTLroEAQ8vg5dD0BAcp8wq0fhAFI_uSpTj5OW_avcJ-vKMZkqta26i14ZCDzNB8Zx973aGTwpW5cSabuJtOmCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szeOogGy9j-1_-is6w_Od38NG4CRpmTfmNfYZGNjV0yW7SlJaDIMy5tzBSsAIeKwos3CcNRFYAQzvFeDcHJRvbeeGTl36HD9mEhHhA41IDYSuzWWQtDzsP2OHp3xNNkPL7Qsi3fWDGDJZLJ0CH96rxVZ6SFvVQ6kwZS9nb4IQelGOOTqOivGwSPNyDAloFETgmQ-8IAe_uFIvuCvcGPWQv1XIXp8bGwzywdCa14EdSqCJ--65mU1XORCaWtT8EAT8lCM_NX0QLnsSHk35KRrJnuUZ_1fPy97_TLrkFXIph6fzcTP4N5oMBA3PY3QjWbk6lNADAjQFksOJxsjih4BaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-2s6FGm1v1kDLoDjtfBKDn_Yz9GKjNdSl-MFYeixLWvSEq601VmRdZBEPL98hh4MWhxhY5nOvzZLvXqI8nZhrCvGbgWWrnptgVJzCURzBCkC0VSeqWNVlFGu3nnA82dGmr-KmBgkmIXjAV0EGFW6R8OCrxd8HSTbFPHMmYgwtUf2LoimtIoIVF0DUtue9K6v9C9hldctW0JiGJ76Rn-KbVEqrLP4GrCB2d09sah5YbQagnTQkkkk2Uz7h7N9vgDFl9OmLHbDXtVyR4J3Z6ThajagZPOPRHxLsEOsPxoheb6jEwojmgHXgleyo82TEXBwiy8vjRjKQ3aWM45QlxW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwRROqx871Y0jurFXYR6S3FJTq1Wl-qvSI9SqQOlnwmC7jttem5I2DARQRx-9bVi1Xtekq9eKK1oQDhH3lu1Hy2eSNOzYzQhkRHFqdfVEB6wMsPNDDGc1sSxOywWN2Jb0mWNGSV5j8arVKj7acM2ZtrQbC2rhOV216rAv6wqEefRxBC1FRi5dWaQ3p-ehYBYP0k43p9sZoW2P5UgkDf7lJhnQXr3gCluy2xGRuW_ZqyB-jRFBDNdgZQk84PnkxrY3dmrNLC2YZ9tkbvYzc5uPG-7DlOFIOEZ13nuRjl9l5cwgCVv-L9qIZ_2p477sxytQV0_Ltm_b_gn5w-aINQZXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=XZXs2IOOXWttjdudtAc3SWXbWpHpG8wtZKXZOLvrQzw9MC_Ui2JpB1RrOSADy1Vx874UCjG42cPu_utRttbQMlmycmnwMnFeiLLfzR4gZjgwPgfnxaFudapCi8milhYG2reDW-4sB0a2NPNXLXWT00p8O7hsmxhK9MPEQIuJSMqjdXyfeEJduS43_Eu75e_r37_VxkiW5pu4COGRJeoxOPmmQ-WpnM7D8jTyLPJKgRv8dufokVk6hQf3Cp5unxkGhE_1-WT3mefKECh0Ca-keYraaURJdsSwuNIhedq5BDAmplHCPug36uTYAkq7RTFhuN3-kfowiXZo37Y0B5HzJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=XZXs2IOOXWttjdudtAc3SWXbWpHpG8wtZKXZOLvrQzw9MC_Ui2JpB1RrOSADy1Vx874UCjG42cPu_utRttbQMlmycmnwMnFeiLLfzR4gZjgwPgfnxaFudapCi8milhYG2reDW-4sB0a2NPNXLXWT00p8O7hsmxhK9MPEQIuJSMqjdXyfeEJduS43_Eu75e_r37_VxkiW5pu4COGRJeoxOPmmQ-WpnM7D8jTyLPJKgRv8dufokVk6hQf3Cp5unxkGhE_1-WT3mefKECh0Ca-keYraaURJdsSwuNIhedq5BDAmplHCPug36uTYAkq7RTFhuN3-kfowiXZo37Y0B5HzJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f66uQ4vEIv1ldIe3ZkkYfGJw9vH1KICMeG01wflZ79J8ywLCO3Z5teXMMxgA4w2w8qHVrA0ZVnmq6UEZxyTSI0N8Kv7grYWm9Fx_k2AsDesGLmmJGvR4UBPIY8NelS0t1N-V6uNeAiNar_c-yVqiRtmEmx7tamOLlnkdEH8oo-GrNWSw-UV4k1dqLLXSSUUOVdV0_4RO9i2C4FOkk_BlTIqpRQNKIuSNfhdHOV4Zpq6bDmkmuAx4SMbvSryh-HoNBDoYGddyUil44M39sGoZxbk2IbkN-Dkzm9i1snPye79wrHQ9BpaFuZ5qMc5mcCs6fjGEAqMS1Pq7eWtrSnGbFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVnz7DGLy8_tiZaITpytL5ekTdJbxJ0uKOn_KDLvKRHe2NZckgZS9ew4HlyizRwZMIOtryfKD9TODJNsAhAkI4GfmKAn6exHPjcKIvTdQlG6tjDKfX6JuhoDvDDahEQPvnHiT-jeQAJtaW3sDzu56GmgkJ04XmGFKrF2XK-GldS-ru5d0Vgpa3sBzdaLi9iirC8JKTOOCQd8gk6vwVz7ANWPk4F_6eEcrIeF0HWwYnNCjJ6xkYigbCKdIkjvG6OBlGvjB20jrxfLGgBaYj5VsHmDSP_lgxSNt9cGZn5rjgsERcAYg0XrguhlVMg0JcvTI4MHWRFhgEHQs6CRjvq8zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9GY6e2hsp2BvT7W4w58ItoqB0WkRFzMLxLhDNkPSzBsEAZ1legka976BJ3KMwPGYswb02k5PTum6nEzNiw9vzBpurkf1VtrMAt6t7v4WoUIRjaQiGA074YdrJzzdXw3gNB_QtCAkVxsZzQEklPch003d8sH-jEFmISTwFyagIyj76y4MIJ40rILlRYy_1Qzoz8zjCkvlY35E3CupiM0l-Bf20OYg4BaaHCLU3CDbtg3E7LeBM9AV9u2GurYSBdwIZshCgRQsdwF8QZrSdtCS9jVOpagYSuX1DeyEbjcNU9EuBfAhfEjJuGsOJSTIk5DP_FYinB6Nd2g5-vNxaZ_ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp0b7M2pXgKSHdRuEMVlNs1Dr11wmH_tihDHFObaza3fmG5FO3k5_xedPHQLvE7Gzu5RDPoOXGIytVtKLQwepGu1qnVWyK2xXdEdr5t4-H2UUqneJP8JWn-L9a_SZS3MIoHYFLy1PVw-t0ktCyRwX2gUH22p43MccaoBO8JsaU_POziCeqkc4eb0GHlC89xtr_FDjkGjk3WteKfztwN2FK9_za9MzYGcZ7xSZRl7d3vsAKyokmKOJpy1mgG1o9Y-IaeGym4BIhKgSFZ8HrmcY7dqCGhRgh4eEWDI1ZR1q4G4NDIVcdQbs2wQdFWD1JjK72NQunMCrk3eNBT_iLhVoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=VwbeG43YL0MEWHJxklirfnYhLPxInlY2kFwC0Oq9FgmpjQA2KmAV98r8wFNVFQu20t_Kh6PnkdJSoIt2589QkFSPZ1Gjo9NX4iL8-zcjkLNKIjt-s11aOA48lJDT_teRsKACZxSrZatXwzvqg1gSy8kco5gh_m_GFO9oG_kGWW58Ie-tkqveNhfHZb0dSNGJE0EhUS0HPzx4E9CpSpCkjpNFRbVS34DLDq2R8DS5jeIjxBIC1150dpdkjXWQhDJiVh3Bk5lSDwFP6VDScbLaeHPQT1WzgmcTuPAYlLVcCZlyCmgoMnOcXolJ5C6VqenHWsuoHP3fak1mxMdsugnaqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=VwbeG43YL0MEWHJxklirfnYhLPxInlY2kFwC0Oq9FgmpjQA2KmAV98r8wFNVFQu20t_Kh6PnkdJSoIt2589QkFSPZ1Gjo9NX4iL8-zcjkLNKIjt-s11aOA48lJDT_teRsKACZxSrZatXwzvqg1gSy8kco5gh_m_GFO9oG_kGWW58Ie-tkqveNhfHZb0dSNGJE0EhUS0HPzx4E9CpSpCkjpNFRbVS34DLDq2R8DS5jeIjxBIC1150dpdkjXWQhDJiVh3Bk5lSDwFP6VDScbLaeHPQT1WzgmcTuPAYlLVcCZlyCmgoMnOcXolJ5C6VqenHWsuoHP3fak1mxMdsugnaqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1cXDsjqXkn-zhnrv85lhM9bYFlyX8uxDCx5MmkZDGfoLgx-Y1s9PnE1DEKLFfgsPuoeMSeCnaJCPVzesP0O55YXpkPYvYlMTbtcZ6bfv0CFK1eH7xo-J5LKogZOQav4NDGAlsaAsr_akYNk2KExHEvL8BPX5SOepfKmHa_kx8PQG8DRK5RcO6WXhwJixN8L7Aev5kDcj2jBcEs3LTNUVXn37cU6k7iqIvr9EaKGxm_Sr0NNpLkVAYp0FHlBznDjl5oF3v7ZZJaglrqUrW2ythPBTpu7yTZHvsOtfxp4vJ-_a5sGASA9LA3zeFKhFO_5catlXaw1AxGjR28L97FfDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=B26vPWizvGD7U1vcnFH9sJpSNqNeAa9kiXQQsH_uL97D4_u_n6VvaMOBpaX_v4sXpKyw8eJAIIPc68NJWtrwJadiujSQjKxj7pcj_7E2-as_xDeHk1xsKp7hjM8l10TVD3ZlrhQ73U-ezXGtJ470kBkUt-froIWV9_4bZYlzDPcM6B2VzUMSScIO9FTC0u7BrfibaOeHwAk0-9Tb8kgFXBNOkpL-NAkojFD_pMCxkkAbvdSNry2OG1GiHoKx57WpFwQZ6kxQacarcRVAXyDnBHGXE57NcjFSuJZ30FBWb1P2mZyerJ4z222cRISjQ8ypWuRv9pMXCvYkCMjwK4YeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=B26vPWizvGD7U1vcnFH9sJpSNqNeAa9kiXQQsH_uL97D4_u_n6VvaMOBpaX_v4sXpKyw8eJAIIPc68NJWtrwJadiujSQjKxj7pcj_7E2-as_xDeHk1xsKp7hjM8l10TVD3ZlrhQ73U-ezXGtJ470kBkUt-froIWV9_4bZYlzDPcM6B2VzUMSScIO9FTC0u7BrfibaOeHwAk0-9Tb8kgFXBNOkpL-NAkojFD_pMCxkkAbvdSNry2OG1GiHoKx57WpFwQZ6kxQacarcRVAXyDnBHGXE57NcjFSuJZ30FBWb1P2mZyerJ4z222cRISjQ8ypWuRv9pMXCvYkCMjwK4YeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LslySeJTqi__0dMw01YaiVldrlmpg7W59E9ytkCsS2GbYqqH1bWf3-YHAWyM4a7mnYQj_dTZs1w5bqfwEjunR5LhaCXFKD72-kXZAdWVHI3aAtlVa38Rfh-2ydnm-z1OD7YK75ckRkxW0g0IXKG2yzhhQ96sei0HI95j1lwWzaYti0bTAj85DSwADHIQxgtIa9FV4_oELg5Iw3rELTud8Ab70s6wAviS4uc3hyfva4UhxOedIfZ6AzluJdniQJIfhbyQSmTtDE8N31k68HJzd0VSHxYI_qgLblaTZfQ-ld8D3kY--LTeUutq03uC70Pnt7xmUUxE1YJs8D47DnEcKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrIZsQFchWIVXjizFQXcRYumu3kT8PocU1X64zFtLuxyf_f5gZpqzCceydpNdwMzXl47zsXKwYK7q5XobN8NkYdJL0vvwmguN5GIMZRojKpRRLNaMAANcrTjaurNoV4n0BAudKrmNuztaQBqBcHlSv2HFnTu19WYSe6YqinmyqJ-dBr0dPI7A-uf5e0b6PzpSXffGxN5VqodGu46HFggnI_V-4dUakYrXJOlqvBUtbCBRx76rNVlpyjVq7I19t7zBCxjx_TiVEeDhep83MlsJ4kbOqSWsUPpJpJq5HMoc8HWO-j7Sm5xZhvxBcfEg04pAmGXlIi-EVkTdSXP-YsmhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=Ukz4Y1I4yRiUJwoIq90tFA3GqiQW2EXabvwUH6X6lHnsZjYcpCEIcAlbsLb11Pfa8wfwjxxeBdLTbFMQF26S485bb54L1PJVuj4PRqgxIQRuggFvpuezxo4YMle3Qy9prL5_muYX43kMjRubgvZnKVWTxNGX0wZMosSUUKBO4kXQjMQMlXebN8VZDo4U-2vZ0K_nNBzqvMtkbz78D60Wrd46Sw7RhSimLK7QWDBqrUhNPjJLR4eZv3XUvtrA92v2xt9VbDhn9g96jP6bcZE_6uGo4DwgAbAVnf6spUZZne2HpR7A1ZmiJ-be6vGYST_twIZdw1qkebOCiHKtm3SBAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=Ukz4Y1I4yRiUJwoIq90tFA3GqiQW2EXabvwUH6X6lHnsZjYcpCEIcAlbsLb11Pfa8wfwjxxeBdLTbFMQF26S485bb54L1PJVuj4PRqgxIQRuggFvpuezxo4YMle3Qy9prL5_muYX43kMjRubgvZnKVWTxNGX0wZMosSUUKBO4kXQjMQMlXebN8VZDo4U-2vZ0K_nNBzqvMtkbz78D60Wrd46Sw7RhSimLK7QWDBqrUhNPjJLR4eZv3XUvtrA92v2xt9VbDhn9g96jP6bcZE_6uGo4DwgAbAVnf6spUZZne2HpR7A1ZmiJ-be6vGYST_twIZdw1qkebOCiHKtm3SBAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R06OuhCH84PxuuvyNfbeyDXKaXuOuxA8U-CxomtTVSrrYjlahXJGyClGtJ0QzQZCvwH9-lojzQUBwPFjpFicx1CdVeHfw0aICWj_EprBMB6tAPqgQfelQJKlaLmlQl0wc4cWNDrvNB2zNiXyb5boGsQJE9qXDy2YFoVqTNQkTRiDbmHtGeB7qNsjuBzl7hTePyPXYgTmlNJiBVhttSU1ls0LgSWr9kH-HmbKhsMODArnIoIWMy1U6D89a9-xl8HDcgede9UI30Y-_kIsqUXSxybvw22gUHxS2aqEu6KgPjS2TWIo6PVGAhCaj8zwg6_sq5P6sqMNXlTRVDLiQd3mAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQzbnu8rPzh6_H_T8rXEhj4w8jGfmc_1kDy3yAaIf9ipGLDExqX6f30xT8xccovoTTetkMxRlCnSFqUIwErOwZByeWN2HLq6mBVHDX6pmFoN4lkoByLXUbfYyMtkgA9NeZ-Dos4unWeLPkpTFatv215gqP5qNZnOB-Iu8sjKxDKwRhguhk-FWuJmwH933fQ8fFZ77kADUWRy4ks0NiWR0KrG0ZjrOXEoEwv8km5zGnVuK6hNUWsU935xk3dCI8Cy3R7yqmfn4-K5sKnyJy3eF32_BrgZ6tkF5MmUva2m0iOVIsJlIA7i5nXF7ZWns6QqS1IdrxmwNqviFqt6N5qiWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=t-xA_Nsl__0S_ePKkPtZo1O_jh_-WS3EyRO1UOrDVdgJm3D-hpwoEKaF22Cz8qYKvqtFmXbqebsR2VBMc2SAc5mBQmHN9Kh5jAlYpLrV8NsHxNbhShcfXGGzFxT4Yf_oIxj1ovmrI8S9Ud-DWkLgFK30PYD89ZuH0NDGGCQHJYXcCdq_h3QyC6mf8quWRyJ6x9b7FMWScWPMrpMuVT9KZLAWMncW8pM3QESMPrGwH6lDW8T5FrTSYL3mm2oDR6mVTdFCOYEDAjqDPLaXyBK2rhgNYZVOsBTudi9t-gbsa0BE_3mdDGY-GUnELYNZoJVpeJsdDUBG7sPd0bnOYzoncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=t-xA_Nsl__0S_ePKkPtZo1O_jh_-WS3EyRO1UOrDVdgJm3D-hpwoEKaF22Cz8qYKvqtFmXbqebsR2VBMc2SAc5mBQmHN9Kh5jAlYpLrV8NsHxNbhShcfXGGzFxT4Yf_oIxj1ovmrI8S9Ud-DWkLgFK30PYD89ZuH0NDGGCQHJYXcCdq_h3QyC6mf8quWRyJ6x9b7FMWScWPMrpMuVT9KZLAWMncW8pM3QESMPrGwH6lDW8T5FrTSYL3mm2oDR6mVTdFCOYEDAjqDPLaXyBK2rhgNYZVOsBTudi9t-gbsa0BE_3mdDGY-GUnELYNZoJVpeJsdDUBG7sPd0bnOYzoncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_uMv9PgiAjK8v9LqGBUyUSl8sJa3pwHkb6MZgChtFf2PN-SpUkDsVXP_Hc957gtom1iuaOzMj6mxZdoCM5WLsxv2T-kuUWdNwOlMw8OZTcREntnalFJHOVNGzo1AEG8HmrQbG1UhajHZAyCVaXFmDUqXx8EKQNRurY0LH7Ulhx2GOvvxwLGH08mZvJ6aYYGDcjh5-fmh0_TCR-XjOfeZSOMGbd7W4qI06Veib5EmOmx1pMkuVm1BbsvNObUu3aJsVywy_Pnwqq4fJF85xosSyU2_of0zhkSYPHSBONFHcay6rDKFoBYVJOnQA5FqkT201qtK0ewEw5fKdIX9Er5Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5C054w2y8hSCaLnsYOfBx8nJGtGV4FIDgX6FsQgZAxI1HyfAnyEf20MOUgw5AoJ5vLRdu4R0N3rGkKwKpz1H6IiLvIvcNSblRMgD1a3dIz4IEXhFOCfsFoBXIoVcCHn-TK67AyzgQQ4t1y4_b8YU55h0eBRFn-wF2Pk2atkbXa6FsRBfwgZWmMJ1YTcOdbkc5Evq7o9oDf0VZPxYOcgjjPcZFJo3IQLpQPIbJHu29hEyCrvuHXfVXRxuO_tUnwEJuD3LHPQXo0yeygxonSijP0wNIhT3aLtLOmS21gr2SvtkuBx8zkyF1evmM_a6PKm2FjbK7ImGNNfFZiBHehMbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeW67DiZwvNoLbtxiraRStM6n913UhZok1lFZQ_D0nPeaEp-E9KKv4PUs1y6qm5RzwnihhTpS7M-ztouyPhlv0v9bPNUdkfsipEit_4KaSLlneCckhoo-vUzJunYL0fmkuqQWpbGtgA0OrdwhwaTQ8dLxfwo1F5ncCiW1EB0c5oZtQ6BeQfnhxt3UPuMwju8AHg_8u_UZvQ53GFXTwKo45JsmGQ0zEo7zmVBZ5dSJ1VFP23M0LuusnjC4RKg3KgshMJV_ysP7aLIy-Y8aM615gnLooyIwLk5XfX9b8UVlD9CLF5voSZ0FAGWjyqIuruUeYA1XhXfxQlp9sdgMdA8aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg3jIZijK4jzdSX-G6pNY6BDv2yrCUovDIxy7_HXGbIMM-LG3yn8u22xKvveqAbXv4UhmvixdpST3BQYzqwjXstdLdnojQloXs71RSe_spkUeRsuXQzsHYIadywvGKd-zQMNesM68kp-lu6Tdv_FjE4sDnAHo2Kh11oOCAoc4pm25WISf20oZ_tioHnPkQx58FIYDOIfq_w3tBibbMexhQS5zWRS7MPTRCXGbQFWTFPIk8zqrE3i8Z8sM-8vZxMugvH9OeGYtfHJJPjc7huFTslAjR7_N900nYcjHrrVx6SYYj_I0IA7wdTqktNE5Rw0LxTE6fRh5KkDo92iGcA2tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfBsuSvV4kvNMbQcd3vi8XBGKxXTXNyda1y5UPhZIyWk52AhfapXejtAEH5TLTU2RzUo7XrnttOqcOogDE0PV4MpzX1yEiti6krywtnFEtVriK80qZ6eT1Js_SkhF5s_klfR_cNP6s0eZNUBxcXq8XR3VKPbP5DPZ2jqb2S0xcluX7wMIyygSa9DKnxkkHcv5KpayamnWB2Gej89Bc0eDxE_YFM22xeqQv1dnGdbOEZKFtg1s2oRmqhFi9pfKzCBNL0QBga0PPsgO36WtKtbBoRhb5oaVfD5kmkPoG9GRg_zE6xcSNOlESwIKmxiO0jW2CchVaal73vqZVQHkQg7Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGhZZ31iyA5M0UZq1BLe5ejTeR-3ckE3D4zqVvHjVFSQZdGAgLtbyGWPBXyHjS4Q_Uu5IB4b5j0PK56FTZ4Q7FJq_n--8q0PHG-_13zZbQNbkDgoSiuGEJo-J184Rzbgv0flOY-vNL47uOGAE5MRJq0hZ_g5nQAgLtA223D_ItBM3OPdkG3PjUNy5Jlq4aI2Mc1wFr47rYKjOERz7s4Q_RQGTw3kB3qETL53Vz2Iti4gCAg583Zls-ycMt9lQBphxHJWsZnYFvjTivqqGwwfh24zqqXAIV228rw_R90lTk5g6quhIR5-YLIODLEqvNNyE2bLpGXxPwbpOIas_9LuSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGm-o5OjgyauNn8-ojAhtTVR4G6KqLlEePvUjr8mtLmuECIxgYgXy7ziyWTEOkmj1jcGTsa5gfTNvn4xhORxulTVxQJ3_ePJ8JCzLu84hvdSWihLbdEQM89YBw-8yETg3duIS9kfzTPvHrFcfRac49qPD_LHnM8iZUCGdRsqv_vBA2e41Hs0OaWe6YvmoFB4hJy7JiErPwattSo5Soe3Q96aNzNVvWnJArmQHqB_TdojrwvkUV059QV4YxL-HY1cXjEzNG9fwGCpj8D4pM2DyU0U5M0W1J8s8K45gN28Xd3-VYQCAPNpjbIAUNxWboJUeJx1aGSNPLzefA57f_X6YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG022M6_zlMLwshIvTKE4MHglxpLrxZYPROkZgeOj3M72w_C5sk4k8xH0WgV9EHkrm6Gazu6wJhsc63eyLYhixvvfhm1yusvhOPmSXH11MU8hjMpQ2lLkSpFdGORbbIUKDI6-HvOqwPhkEbKrGkHz76D118mp1vlJ0WR1P4-giOOenYkDzndnEenDab8NSPMCY6TWL1OeUkFExNl11PlFXMe8844VozMFpU6x1SGcMQNFXqrvWvExAuTyY8puuwi1B7ZiUx_AQetqLMn1cJ8eRkv8CGH-2FkpJtmIoit04Jw24ROQXzL4nyuNDXmDKgPNAqG1uG5BoUaZNigTIhf_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GokVclXFqHry8bDTIJocEw_GFGdiwCjZwy7lr_--ApqxGYe7UgYiGNOLIUbp4un1ic9JzZ0fiX_Z3WlLEmj7NRhE0-aLbig9LB7BJmsjHwwH5j-Cde8VVnKX1UWuEoAH7Xokdy0CtbNaDzhZQ1DP-zOBas8echoEQzurpyCGOKINswauJvOJF-F7kp1RNsMdsV1_VwQe0JxqGevikbw60yWLgiCQiSPGi74nL1I21qKs8U2a-EliuU8qjrK9y7x61aGaTL5exS_wV05lMUKm3qkYT5sMO2medf-RiB-9mkWkXxczbSwtK0fyb5t1NJMRzWwkHGIg3VloMD1ys7jpwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXkR1Bhjepr5ZSTJjDv7iA0AZvj60fzrRLn_jVMD_C-WUxLiG7vGJrJqdumop6UOoal0PR2Sm5_EFfSRFypJl2dCB9P208_vj3rAQ_lQuo3mjv6jNbadRwBgicUNDU3VRnIeTbdB1DXGQaOAZ-9546gNfb49NmPf_I67mxuI16TdkIEb-qSKjl4lA1Y_E3qtx8mud1_78uviDJx592jY8XDopDfHkaD1NTjaoRo1cmgEY47gHHyJzqa4BL4JWnRirN8mMLtYZ0vEWHjtIBEGiNnO5TFAgMqjGklFBZyK87jTURpH8doaqyBkILi4zt2vOwG-GGUXKZDPrB428jghCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoLnUDk78kpeldhSxxdTZgEof5HQnPIsn40tgLlVQ8TApBrYZ6ULJ27Uis0YEdsWIp_00xFRnotviK0tcw6D76k1Iy9Y89wNLPptN9_Bp_UQC7Xf1p1q1AZvr1d2e2Kh6Vz922JayoWaWnY2t4SxxR5IiB9VxsyF_95ZGXIp4Hwu44zMkI88nGZpFgSW64qbXtpEbGwajXZr2K8kJAZVYSZWVUK2fQADWNDMx5S3mcsrmFlWVuvODt4goZoYV4v0pouV3m2UtxO-F_9RsZ-WeDgRDIo83w3e-rtlOZaA8Vr5nte2MMKiO_DcGXzRTRl9YzatsjYoVXyG69mPZytGfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEaO6jnuPf6AFuTklmcloXtfg2Qksw4trTQmkdzFiWcc25pN14ZsmBHGMawx0QxO8RdapJHq3LZVqD9QjrkFpDQHuAnM11YUW16h8tAuL3mSNZU9zS3HYgD5Q9MgopoiRsfstVHEeEvKIofLhRpGZUFObobfEq_G-Ix5a8Oon50xd4LVFbE2YEtXfIjuPY0Q1u9RDtTN3nLQQ6Zn5NX3gfgDOE02DCnYnOSJvbK3tO625cSKrGPgMQxuPTvOr-A5nUBwHykbR0-SWM5NEjTrOdh7e3762i3bfHCPv1mkVOsHi5q7GZS9zTICGzLgA4l3K5c-VcghNw5H_an80a8sSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzh5gNm5xyur0Uu0X8ZGB2x83tjXU498NT2hNstljeadsozw0EYwhoB5btwot1RXAcq0UoTrK8w-Hj3We6rK-gdr53ipDqrq51gSMnv1TQMcDFGOvdcTCQ8D6w6mik8WAto8chQ3XX-5ilVQKWRVjeISTvw6tGyVzFKZI6vftEWlu9do7O0A0VpTrICoDaAab7c8j7DQFXfQkIYBeHYPu0JViqo1m2ErWdsFIVHQ3h-LGiX24WIb-oGZG5bQHm1_AjOzv9nSTqJzLRj6pFJOcYIuac8jPu8VliRu01B2TLtHj-EJDVtoe8UlpOtPylp8JWiWiybgzEaO03hJHpyDQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFbc69gmiMlNfxoiSFqdFRjXIafNYtNCA-gGzVOJrH7O_zUuExPch1EdFAA2-myuUuLobDGJb_Kps-nTdBJgVdKmVy7sGNDsGC7_XqquADTgJMkUGliriq2GIpPdSVf-5pEhIps_QtdoV1XlvSrGuqlO8k7DSRaRlrYb5E17V7VF6Inq3WZg61m_hyaaD3LVWW3GuzasK70b9rxyTR3mYs8y6kl4GWIUC5RH4JaP-xbM4dNgazm6925J7kVBi7-0hYsddv9Gop11vNpBHEjfMhR1qR0RR94nHG1zLuNs0sEzJKA8ni45D2_Nlj810R560E2T4Lk43TPPo9RgFpeihg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
