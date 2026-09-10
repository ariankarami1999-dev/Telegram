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
<img src="https://cdn4.telesco.pe/file/VqSX_y7f4SDAD06lTyaTC0I17ByndEjiUyC1UhTCg18N4o83gieCa-1e5IQOgNEyZ9AEs49a4q1LzDaPM49z-1TA64bg-7bwMtHJg39_5zDjJVSY7D9re32LK2grhmAOznI21_srn1WZ-LVZ7Bg0UXEw60UNjwSTLWXWDuQkEKwMf-pOtuRAcJmglu1I3v9-GqYexH4czoZwxC9LsMPp83NV477eK8QDkeq7tqblhXEuWWdmbDvSfwEELltKkqfl53xA_yp9N-M8fQ0ErdCrs2ppH_jqUN-StrXwqLaSJtJ2co_3f6yJUGuBc_hXPcLAW1-NaMEhRJ8Zj_nMQn16xw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlMtykgxfD9-P9JqWIJPT18e_SIiPLo73bHW-rSPH8uki4SjWZx1Kep7Dv2Cou4qRKl3Ba9Oxqhd4hIQYPFaHV_wh1HyU74MAHW8fNF8vUoC1jiDR3VDNQP3W6Cd9O4kcxmodd4RU2R0P6mmRZaLu_W1tZcWpYkFt83o1kN-C2_S8rLyyCvi2shk03ie7wPZ19rC37oR8ewa6W9q5hJK8pebQsVd_LxMUV24nqtp7GszaEldR8Lya7j5upAFq0uJ32YKBjlQU6FRrBs47nUx61rl2rCIUGzJ0AbJ62tq4rlTrtWhVaNSuEzo56lUO4NvTZ9U4mcA-3XcLRjnMqTXeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 812 · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENUDQDtnGx54iHdIFRNs5c46j-kx-sAeFze3zQsLcq3iGq2l0i_fz0dqf3zJRhdOVG_5CxMT8XnB8UhCCXFnFLJTLJH2h0gCD-V9Ueriv9cwbLnu3JAKjn8dVzZucAx70heVR2PX8JRCi7sxcRYsSEodhVFt7ltHQ5KIbVE13_okzg5VESJt4mPZluyEwo_tc4fKAtcEi-Y-suUo8lfWXXpSf-FWw4DOknVgXwlMtdn7G4-mZYklTFAy97eN9KEl6eZF9sj1skRr7t7KIkX-ZBLenz4QjK9czPIkT8AbCJ_pF4OyOqU5sLR_dAV3_gqMHPHkWKqRGgkXgDSKOjqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW7-UZZJhEhyHYzlyHCpkAD5K7QWUG-3_KBs2C9ILv0zOLG5vL5LkO8BOL666naTZxr0jyGItjaWmiJKj1b2wsG3PTJlbG1dTEZ0T18KDIDDX6uiqX1XeMmGzkBbSuzrX3pDgbIWsyUQaOJo442a32la0q5x18XZWDyVBKx56SPfYX23Ao5baZoK6Mjom8UOxDtQ2G-rw8cfG0PoBnugBq1BolOuoc4D3XdEjJacna_PmkyWC2wir0t6ErhKE2HUW3vGCCw2lq5boI_ouSEwLGtFkhXmLoS0RZNmZDkle6umBEGL3Kz01-2uLhXw-xmUNSSc1Ey3WYt5l0G328IfHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmpLEVR7v4j-ktNPEmExIVo10SjXlMp7D_GBn8efNSrO0jhiPiAzeMBfZd5ExqFf5M7oeBvtXG31rQcWNzx6sX-a_Y6aIhcUAIdykVmpkmVDomWTgYm8S3aQPlpcUYqVqNR9UF8L2bE5Jmv8H5sc6HzZYiysQuc-tWUeUHU3foL6EQ9f5VrcMjBVooDVJCcyotkWjc4BehB_27svfUwGtrfxOxsx-C_4tvw_AISNnYjRbF7w48x8VdMaRWU0ztzQn81YgWxfZABS_6qgpsnNqXAubc6NDL1DGP2cOnKEH2-zNI0IC_PGbDDqEf4EvcppDtHx1r1uIfPTemh6UHmfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjlR0hyO2toYAwbKpF9SErZ8yaTeXfGjdRphtsjV9FxIUkZLlvUNxzxJiqOxG11OAoss47QQV2co2PNIVHgVw1yn0zWjERjhb7gHbTRkAuaifRwhzGkYjecYNYcleLB6RTtdrsxPFpJehraap3sJP94ap5_H7aMcT_C-ciP5HhJrqgSETuvFoYJ44OQsx7MOyx_T5yQwei6kSGFTpDK-00zJQUOewSeSZEstPaaMhHIJXZH2fJ_5vUt45cRtoha88FuL2_Y6UFPBkqTfUcgEgQ4RCfk3ZVbqKCKSNJNIXprltxy3KTUJ2Zvcpy4-AXZIhPF74kdKuwQ9R7L7QhuiJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUnMbGjTqo9uiGyJbfVQs_3rvwwpKNC225YhL3JmZztfS3Kq7tfuVKbImCvlk7sjgD_ldeajpAyalstbJ7YI27o9N4_tSNsc4RFPcX7XFIDUW-HVVB-bihPcTswSNbQzPA1QBCmoV1RYyntmC-KllQBI_XDD9r6TEPIlRhSsde4j_j1AQDVB67eIGOj30ydIY3MC13BM6BFgnyIrzkwQtdUy4WZsP9MCZaSXkbxI2cdvb452RducXB7fHf2fATHOwPBzYXWendB5YgVJn0qO9e1lnkERAxhG7VsX1DoP0ZTubuyJVSwC2UvNo1SOg-tMiSGoambDsCafZof1f5_j8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pptx5QNr4onD8RVfgxvu3CurGpsUZE16TzN4ooukfjpaJCDIyvHBk8K1OVA_18opOCvz8il4RMce3ce3CrCr8dgJIbjxWeu-1wzlK-DEbYRIjJxqRwwaLRFhi5mAutzfopTYjvt2VJNNRPn1-3Flz4F51gw3yRIbmbZyOZkVzSPDtLhjlR_TAcCyYapOUlLV9_67VLgtYjUoj6VBe5QPfURgFpcWWTwCaFFmxyiDvw8rxi5IyGVhkWklHXiUch27yZ2IhrKFVALUI3nce1rR6kh_QJucLTAvGOJhjbOdcqRBWVPv1rXo1B2g1b9SgL2omAeA3I-ny_nNIvljcGq6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=WCRcdhTOdkObqAcUWeeln8sn0i_TRf9Jjordxe9hizWK0b0TZsxlw32rtjgI3pYySy6BFLUICoXT1njUyV0RjgBs04Io5zx5ImZPpENyOFoaNJAdT16KvstzQPYl6zBXoiCv1W2kboDvnjp2pLkI7QxPq6A7cRG4MrMZEqRY97h4syFw2xPF7GHCSC1cBpdJ5sntI9pBkRjFcEb-QbnXgT_k0sPGAB5nl1LYnJOjALBx4zg0WIjpO7mGW6hYGmcLO1BgzkN3JqDL7U0Z7Ic-Ev_LUTL7eMYWB-wZn8qOLgkseynGritUzqLLKc2whWaJj7Co-4S3lxw0ZEDDyRfph3XZpcH6gBcBUpkGMNf9yq9-9KAq-xKtOoS8g7M5Atlsy4bKRxdSDpbK1YeZBcKyQW6cgZYnJHU3E4Bq5zAlwvpypaFY2nHm_K7eH5x0NQszn2Zla-6RBp_cH_M4p8JORAxmglicHSvDBEAedxIooS6bBJQ-_BdgrrNsXBis44yOyydm5OF1_IRUvgtv1LS8EXcUJXtMgnMHKLhrAWyjUK8Sng_H_J3V5l1qqOGV21Yv95lYEiKgzVhUhBcie883smtg-PsMy3dp1O1Uj11FMPvAvR8-W6bBejd0Of3QIRrNqxRtk2OQTjxPSijRx8vLJ7OmPbCgM6Ty3pxgsE7xbUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=WCRcdhTOdkObqAcUWeeln8sn0i_TRf9Jjordxe9hizWK0b0TZsxlw32rtjgI3pYySy6BFLUICoXT1njUyV0RjgBs04Io5zx5ImZPpENyOFoaNJAdT16KvstzQPYl6zBXoiCv1W2kboDvnjp2pLkI7QxPq6A7cRG4MrMZEqRY97h4syFw2xPF7GHCSC1cBpdJ5sntI9pBkRjFcEb-QbnXgT_k0sPGAB5nl1LYnJOjALBx4zg0WIjpO7mGW6hYGmcLO1BgzkN3JqDL7U0Z7Ic-Ev_LUTL7eMYWB-wZn8qOLgkseynGritUzqLLKc2whWaJj7Co-4S3lxw0ZEDDyRfph3XZpcH6gBcBUpkGMNf9yq9-9KAq-xKtOoS8g7M5Atlsy4bKRxdSDpbK1YeZBcKyQW6cgZYnJHU3E4Bq5zAlwvpypaFY2nHm_K7eH5x0NQszn2Zla-6RBp_cH_M4p8JORAxmglicHSvDBEAedxIooS6bBJQ-_BdgrrNsXBis44yOyydm5OF1_IRUvgtv1LS8EXcUJXtMgnMHKLhrAWyjUK8Sng_H_J3V5l1qqOGV21Yv95lYEiKgzVhUhBcie883smtg-PsMy3dp1O1Uj11FMPvAvR8-W6bBejd0Of3QIRrNqxRtk2OQTjxPSijRx8vLJ7OmPbCgM6Ty3pxgsE7xbUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=HW8MjV3e8yhdpuSalzWP7e3zdiC7IJxF6Z7iw6zHEXWXiHBkPCCoxHTeL43XbN0AwmAaCdWipRcAVNJZpSYDWmyGMK-7bGD56g1VGPzKjNohNmPb2L_YY-sh-0yQN_iEqwnNr1YvQD578xauxCXGZrrntkvflTc8QT5x-HjlKb163cGEqpp3kLcwPz0IsYm9BNAMULZ3J6W1kBXBovWhnPFdPq2tIaMzmWxGUuLNHRyGFPH9YglB2IAU5tGyF2eveyWRAGVkBUNIRY7GcfBkFKKF3wJviRGj3iUaLm1W6KCfaJLxY90uGsLimGwJkfqf4NnA7laSR91EzWYi0RHgvCrY5n-JoNzB01PYDtX5M5Cg9K1vlSkVdC5KVA17W1yI6yf8aLC3mlq3VNt6diGM5Rw54_kOr95yjY7ZrAanpk9MYC0LetN1sVC76GQskEJvbMfQ0IFT-RzYdA2vsKhCUJiCkRaZdxLh1RVh1IOlMM5Bo_b4F7zPVVDnrfArahppC-YxsL9M41nzDPkpolYgiYooP78ONIQSN22gA3VfMDUwV5xeW9adiXcBtBoVE43wTiiGY2iYObnQxghI_Fl0SBl8XGZuLc_WQdENMdi0lle15eGuByQQBAcXVd20wwsGlFWfS7PpO-lqWvnSUOQauHN-hbXrFUQ5-_CRd1VlMx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=HW8MjV3e8yhdpuSalzWP7e3zdiC7IJxF6Z7iw6zHEXWXiHBkPCCoxHTeL43XbN0AwmAaCdWipRcAVNJZpSYDWmyGMK-7bGD56g1VGPzKjNohNmPb2L_YY-sh-0yQN_iEqwnNr1YvQD578xauxCXGZrrntkvflTc8QT5x-HjlKb163cGEqpp3kLcwPz0IsYm9BNAMULZ3J6W1kBXBovWhnPFdPq2tIaMzmWxGUuLNHRyGFPH9YglB2IAU5tGyF2eveyWRAGVkBUNIRY7GcfBkFKKF3wJviRGj3iUaLm1W6KCfaJLxY90uGsLimGwJkfqf4NnA7laSR91EzWYi0RHgvCrY5n-JoNzB01PYDtX5M5Cg9K1vlSkVdC5KVA17W1yI6yf8aLC3mlq3VNt6diGM5Rw54_kOr95yjY7ZrAanpk9MYC0LetN1sVC76GQskEJvbMfQ0IFT-RzYdA2vsKhCUJiCkRaZdxLh1RVh1IOlMM5Bo_b4F7zPVVDnrfArahppC-YxsL9M41nzDPkpolYgiYooP78ONIQSN22gA3VfMDUwV5xeW9adiXcBtBoVE43wTiiGY2iYObnQxghI_Fl0SBl8XGZuLc_WQdENMdi0lle15eGuByQQBAcXVd20wwsGlFWfS7PpO-lqWvnSUOQauHN-hbXrFUQ5-_CRd1VlMx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6RhC-gIwsu1OSyivAxPjLnQfwaq6J9nHHvXwZblZ0Sqlwq4jBCXGIfu_nHLSqRs-FHOE5eUIHieyEt1CE9sDeVO91MBcdTw3WDiRa3KCqNZJiJ5H0nw4-rORFlHHi5JMWCXkKuOq0XDYxcmKoz6ySH4GJBlhaEsFsVmF1Z6JV6Pwc7kQEtUqwznsVZvCOw_zWC2KoZs-UDSgMKxEYU26XWbD2bpVxZq7UAWOwsaYbq60eoqO3nmBmtthdabeNI0CR2iqqrSQV0T1xmqNGxl9P4ZL_2T4hx7XBiNe3IthitfUIz4J5ZgQ1Hjl8q_WgOVpeOy0e5l7xLQKNux4mrIwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=WHZ-HrRjzKEwQp7fCTsPDqaIr8d-JIpL11czJ_oV-Avl-STqJOKlZGjtjgB5H4GoqzSMN-M1V6QWwtFe1PL1Xfm9ZV8mB8S7PN8qyxP-YOftpuNClnQKrjR6OMc2ya-UBRTzUJdqtyimbIeibYm0a4uABSktxRS-lcpc47xRpR7IzNgdCyMqoXob0rqn23OKBcTMkifj5tIja8Gol5DG8ZdjvHspMrP5YJ3ieWvL12kEtn3N1UhDoji03-j5f_LzrUpJru5pf55eEjcAaRtNyfwiMVrbGqjTNuQgIcSlhwSEeEqFtYpilIqqH3SSbHdnIrLYlZHESML_32E8omDyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=WHZ-HrRjzKEwQp7fCTsPDqaIr8d-JIpL11czJ_oV-Avl-STqJOKlZGjtjgB5H4GoqzSMN-M1V6QWwtFe1PL1Xfm9ZV8mB8S7PN8qyxP-YOftpuNClnQKrjR6OMc2ya-UBRTzUJdqtyimbIeibYm0a4uABSktxRS-lcpc47xRpR7IzNgdCyMqoXob0rqn23OKBcTMkifj5tIja8Gol5DG8ZdjvHspMrP5YJ3ieWvL12kEtn3N1UhDoji03-j5f_LzrUpJru5pf55eEjcAaRtNyfwiMVrbGqjTNuQgIcSlhwSEeEqFtYpilIqqH3SSbHdnIrLYlZHESML_32E8omDyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd5AF47Ex-aBTpg9scbc8FVSMXK6UB5DaLp_VUxqaA48VgymLW9aGRi5GoaNdefqqtmqq7ZCFipWIes7qTtjMU_ZMGf9fYJbbV7kiJdOSkEskDPjN311-035p8Y4VsC4IWkjXoDq1lwAfJic6jcLuj6mRHzXQ-rMISZ81kL39gclf32JsbaDllbm55ecMjPMcj8Nxp0_sDmRj7CIp039_lTaaWZf7sxa7UMRejeI2Ha1rB5mCrvojTEVfWxlcjXTKFj_A7UZVO0wPwuuahdta4b-hsRMCPFUI9BKal0hDaeBg8fJAdHo9mOQx8OXOUrVvsTDXlOnm1QhJRz4wPhRbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=phDrldBqFvAPpcCEcjeAJracX9DXo45BQrACSaoNdhblMH2yaECiGI1iWk7OL0t0AkqKdJ60vGOtz2xCYprgUtbB491qpOxAOaKsFUOhjFjsaFsABsKuNV9Fk7Fo0t6YrDSLzSYpFX0NBXzUGCsaV4aMDm4wxXeRnTEBwbqF_OkQyC_D37ERlBv5aQoyBx0PtBAE_xGUyJC742VPFMsE5DhBmH3n3VgQm1N5ssdHPK0Cfnoti5VNk2zNnIOsgquZiOVAwEh0FNFy0hipJ-RcXf-lNZk7LzNJDofKqD3-FlDE6ZS6CgaJbEr80LYw71KDpuMmMgCe23DIHlRFhGR2uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=phDrldBqFvAPpcCEcjeAJracX9DXo45BQrACSaoNdhblMH2yaECiGI1iWk7OL0t0AkqKdJ60vGOtz2xCYprgUtbB491qpOxAOaKsFUOhjFjsaFsABsKuNV9Fk7Fo0t6YrDSLzSYpFX0NBXzUGCsaV4aMDm4wxXeRnTEBwbqF_OkQyC_D37ERlBv5aQoyBx0PtBAE_xGUyJC742VPFMsE5DhBmH3n3VgQm1N5ssdHPK0Cfnoti5VNk2zNnIOsgquZiOVAwEh0FNFy0hipJ-RcXf-lNZk7LzNJDofKqD3-FlDE6ZS6CgaJbEr80LYw71KDpuMmMgCe23DIHlRFhGR2uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEyTRZSLzJEMeQGjyc4hWC9wAQFEmJs493U_-jc9Q8VIXIzMoodD8Ndr3d-UfF3POK-dgX0FEowgw5jjOVstDNAevyE2IVzmVleuqAhioK7xvNMJKTIBcZsimYcRbPC4DeZ0_fnpxeMnCTSp-ZtHbFMlnlEDu67dansNvGEh1E5kAP8Tg8f2Yl4Q68SCIQ1enFaUaynpfbYBn-50iZcoalasvTjSQKFEtEVlWdnCg-lFZVhD1u1tcDQbZz56Spp7Uj8FJQ9sAG_2cQDg-9Vw5gHwGPXrFC0ZloUH2tSlejv5JaS2pwQBrdXQ2oVyGnjJwxz0haq5YEKUS6cQk-4Oqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwEYd5DWP37TV0TW2axF15QIZ5n3-kU7_r4BTWsACNM22IG73KBc0fb41QuQFMRs9I9pJn5cIkcBvSuz2xjZ0zZ316xJq5ELbzSQr2dHniEsi7Is63Gd_SjiACRHTeQ2GVxbFNoqgihpL88wyLGUXQpTh4Dkl4WlrWnXDQMSsMaqMLZ4LQKZIShFZQsQpsR9gEf-4xivwNfP1i44I-q7CdPpVPx3HPpvnyThdiOvItX3-riVHQ45xCKEF4WBHKpBKkpRuBaTkrM-Oxgj59P91Luv8xMmyleCwurOhYivJwfjxdcAg6-L9F2GM8ksNlfIWFUpneCHiYEXulcM_hf-5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5aHXS64zLl5_OLQZBC2XJyWgBbHWh_QmYEDcQVhlVpqVl3fci0SwysHO8CXVXYOVgXD-vAKMxkGz6VAFPZWRlN2_fZLyjc-4JsJjotIPwghQn8lW3CC34m8NhP65rXJ8zP86APKVx66vuEdGhUv-mukayRHBWVnO0Lba5smMRL-6eoxP9kuuhrWYepKx7QekiEoowWyyGuVa-aNwgChHB08sfP28--Pe8i-ZHJIQxsb_inHFyIKRaZm0OdWq3JPzetKKGEqg2i6JQ9MFbF8MDHZTnErtqLlG80okzcZp182GRrShWzZw6Xwiq_8NLe-2ksSInJa9tlHOhtMZ_iIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAc8dU31mVXWKXbbSVXxFigdCXkg8Om2OXc_P6usKFi012NHNa1OegBOAsXd2fsLy6A4A2_mzoPZeurJ4PsRuKdsHXt_SYkJvXkFgim2Xz9sxDCQQQ_cP5brcn6LExU9cyKt_mmNGw4InvvnuC9IoOwm0OrKQeUbNw5Vx2w4Z1iFQeX5uXmfeFD1At_DZ7THiVqN4rGZe5R7krPLDD_ZoA7KDIbZXNzx0AyeVesOwIGb5qAdWDtuQkG1mupdTsty2oBwANzALPSWnO8qleQIrAH2G4Qrq7l4bNHRjD92LV_NTO_2_XV-qg2VxQVtkosJJaQfPt19tzw6C09cMl_U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnSd7HDl0gYkOKWPpXrYahjiNTfbBL5lYXv8kr5ptCstGV7GEY-BzWHzFpYtDzr6bq9OX9cBd34NBhwvHv_Hj5Ggi5F6_ztk7e4dX9-fRbgijmeyiHWwSvF0zfAaNQYwdYFg8olmzh7tIuxAC5qqTgKeaY0LH2UdZL7L4Fc7xD4_hbcikdK0UW7vzOFx8RZtVaX_f5mUJEEAKVvJhHwnqQkXXSEwbG2AXiAw-BqUp3itWxVKZuHbY7jjE9HzEeSpxt5D8JPF7izFSdkxEov_XcVx8rruHEt_ILgQiCnuxH5XoxJvQNxTGor-JVgHzXTfQU-w5xoZ7NbWO4jrRuC8kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCCInWlN_hU-MuHFZvf94KE-GPpxsrn6_8OgjJzT_ElqfxCMsDQhHMSm3lPfjlpwZzqpzm1wHPKZsePxLRQCKo7QIqvM8ZfVPO8WU-lkvVJXkExNElVYUUuqGWeJCznIaslQ4Oe8zss9cMxfBT5TmA4KaMSRA8Pj46FddsB8_RLGvRJSmyKuG0zaNAXMZ2HemumSJrM-cwYt8XAPg2ezg9fDXgctdkiPVrtJN0sFWSGCtCspgnxRXN8R8LQLeQefPdUR-GYF-iwcFUWzIVy2JnvIeF4GqzfmvEZFmEZrDiuJ-URS00QcF5gs5nkEnIv1TdBfKZb9JIfD8BSwPJwHCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=H68mUl0idgYudqHeWuKRP6Nph1g3bQ0Zu0lbn_uwjno5Fc-6LdAGOh9txrsNwJWwJZOVK7wOAsMvysTYZ2i8vObCxIhR2fcco0m-J5pps8qv4QuZl7b1U2Nl74MMwR9vadlkSLK1HczJ_iH23vTeH1NGynNeKo6dMh7TPvV3e2XOFdiBwgBxukGYEs5-fkUeAiP8sABPMrpVt1ntUkhzMjegOVz2RHsGDoMfszZuaGnT388iKu3z2P2c0PIPYiAPrUQ-Cu0jobZ54kvbzD6F3nrQ_18YtQ1ESpmB0jz4RPd4LO28PEiSJM3KFpXCAYTT2t76X4Y6Tu6o9q0mKqFcXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=H68mUl0idgYudqHeWuKRP6Nph1g3bQ0Zu0lbn_uwjno5Fc-6LdAGOh9txrsNwJWwJZOVK7wOAsMvysTYZ2i8vObCxIhR2fcco0m-J5pps8qv4QuZl7b1U2Nl74MMwR9vadlkSLK1HczJ_iH23vTeH1NGynNeKo6dMh7TPvV3e2XOFdiBwgBxukGYEs5-fkUeAiP8sABPMrpVt1ntUkhzMjegOVz2RHsGDoMfszZuaGnT388iKu3z2P2c0PIPYiAPrUQ-Cu0jobZ54kvbzD6F3nrQ_18YtQ1ESpmB0jz4RPd4LO28PEiSJM3KFpXCAYTT2t76X4Y6Tu6o9q0mKqFcXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkJlxOLhzhRzyF9nq8g-EUoonH2KMKgm_nJlXIlgW0RMdxHI9Yx8l4x3M1Rf039jMb_9_uHDU12lij-ARTjGIJtVl18qmDILGR6JqPIVzvxUmC8aNipbXGbwGRP1qvpq_ixQy6zWna1uv0lbWQ5GsUBl37BalqXrO9wT6dfoRDWapbtqb7hI9-K0sBcn__-PDFD0jt1xCZ7kI1Pyi5O2dC6Aruev3dV3HNjbrD5FR0MGVuCQWrTq6jLCE0xUqQM442PwrfZjy_sKoLfT6-YIksiKvePEzna6cCYPcmrVzXU6YwAmc54H2BghWEZzdxbmBdEQxsKoNj7U7DLweHGERQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNVwz2Zm9ypRAztN0u2e076TSHQ9bq4CXp1KMkWMn9A9XK8BA_aCvsDQumGi67EAvLy855RXBs-8bO1bH90mMNF76v5-WeoMSiqUwocaMtza10N5lVgFnuq5Le2lq_Atax7NYSYi-CChmtMeRwGLqZas_dOEsz1Qdy1o9Zw_VDE4_OJpe3pTpRLCo8jlH3s1Qf7nxvNlF0X34OAG_3s-S10McB_Yy3ukAo1OpHFo9kkt5F-zzF4muXpRCYityR3uV_PCkr8H5aEAjWOCe3sTegprVsXhkXKmJOCQul08oIm5DlBk7bIXDYlGzx3uMfxycJWXxnaCPAo3ic5D0E3Ouw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPqPAa54o1Xktti2qMBex9Ur8VSYgyPeq3bxVRo9YOZI5w8_sA8xFeKsBsdeeWQ7SDZp4DuTabtAbUlVPXtEaTT6Sg7xikYMp_FpllqhkBYocFQM1XqTE3AO9D0M3gTyJ6H8FOKfU1kaied46-Q_BdF72WM_tVESJW9wIFM09zSaKBnbhvfefU30GF1xLRhFtUYGnuuSSS46UXaZKm32HB3870SxSYflK8SOSO6XAwn2Z_65XPKyza0LqXw5snvK7jtydCPlkd5HMzmZovsy1_39f6eCrMe20SyuTfKLWqwlAHxhMPK95xIiW0feuXRDkb7uX1L6fK9ktjEro2d38w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6SnFvQ5SB0Y3OSSuVBsL7C1xCE4PKR0vC0cIYvayK8fi2KN5LOTEGGyvseRHxt4YLqrGpnjsR_4sf2B_jrt0o4WB506AMQZV5WHUM53wuwB80ppXPYHMOMLXB2djQyUkIoKHi0ea-9nlKMZij6TIWSuBtJAp0Ntzn4eGrpe08Ljsrl9nDN8dGmSEkrqfMx0OC4p562oMMk-wu8xJPHCdvoVS12qpSoULJU9J7WuKAc1kZnyOZAGAfnLpbzcal0B6vj22ZqnKlqFIjOkKre-o2ZmkP4KjaKb5Z55EpN4QdX82tBQ8A3WDjTy6zZTDdOai30J-GpibyWCbkaZQvIUUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-aLMSoJn9LFZnmYdryycy85_Rd7_hLYMh2vLfKb6e6ywVTeejV5Mpj9BZLqEjNJGuoFiIvbKcrhKeWkJx8uP3bwHFSvzT29fgxhnkKVGGODVHxlBJ2qKmjHPYLUpY8WxK9yXfxQPxEW3i3v6v53I1GfBD74bAUHyk8a3_mT7C4buW5pZM9P-LljPiTBs32HYlTK1WDooZ80_NZKSMZpPjCoP-kkK6Dm6hEyt7YQCoA5hH0dOou714fns5bkl8o7ryZ-pRvbk0pYZltjaN027BY_FbAIvz-Oa2zerV2F87JV-apnelbzvsTXPvKGf9NwMV0iEcpP6sbNIXCqk4W8uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eifK1IUiBNygH48WF3fq_rGvgMXp9ZA7gPVFAndIkVd9he6o317_nRQhT-pUk9BTj-tPW1s1nvAHmFQxISfjpB-jpj5duchvmbjs-mwR5sB9rp99xDfUVDk2K-_75240s6N9z27eX-J849ZZ3Vffbe8O4_kXnmJOzcsWfNPOPMHVtPQvrWskOP5vRbIjmvscZUY_iU-Ww0e1q5MhE6hHl8U9Hz1xA2QRMBNMo_-8pozOzcMZyWvlab_Hnm4pqM7Nse_m2v7YFhD_c0M481DNO19EV9aJ6JuK9nU2MDpzGtO1VdBhqeFuiXOixsd7C9p4yHPQpk2NlywsT9p8wQpVnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZErfydJwfo1SzVykMquvzOWYo5j4Y9uFKeYwIow2xldhpjb-0qoKb78uo0Qo50hdQsfSnqmp0rF6OxCBHl0f-ofFdjycM8yOCAMVEpCB6Oq0FlhjoFrimQVKp1MFmnYr7RyxDGzGubnpW3nk4dT3XTKBOHM9gIPvo26qgqiCPFa9N9DAV0AyzLbhtg3U_f1eerih9BdbcA58vgUlK8VQ2eD_rW-RLnBa_G3JnHpAvuHqeQ-a93zpjaMdPkUukaoGyBXpnJ8BJClyfINoUFc7nlJ1Nsy3O8CU0_VcF4th4d6aMnXDOaEJKN_TnqBvcqAkkK57ChEDTR_Zv4-_89-ucA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI85LoMxIfxMDhs5am9JMCn5ac66hbEDXBRKICrOGgEiopNpq9EkOWJjJiiv7qI76RaUzzdJyy6tj-t6KcjGohIja4VYfScgjS4ktwxJTbiThQE9BzimUGD-yCZLknBZSdaZgVYXmFO4qB0-TPJTOFIRL8NHHhhDKqqUVKucqGphn5YsuL1SiLxnr9EUbyYfyXSYSCSqu4p--kj1cuYnAdLOkLT3LONYIGhCr6r9Xo2rvETXBea9uUwn4jAJoS7W48Jsqmc9FKhat2d4IgLj5uAwEWymJDVW4y8dzH-Tl0anQwr4ic8KKAaWYIN4f5ib_YcE3p2Bm5ISZ5jG8SWIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIuuJJhKmiSz5dYkBGqYXbvpeAf60C3DwwnvLh0WUWniGc_8RSQyKt2WCywR-zBtuRrrrSX9WUnbesnoWsDNZqr11lGBIFDCU8pAs0l4hTZ7NDzBdwPNcR3ryNaQs8FfqkBwBeFjrXsOUFc3A7vSMIO3lENvk4KRtZHL21vWBgKinKn9qxzIq1ZajJsVkXUF2dxOeGHrWEtUKI579leWkKB9VC-OYGYl_D4qlhwt0vUPZI8aBl_EsLnMzw6WAdNx0yOUYpSjHFwekiKH5ZsiUldhmg7zn-luNlJSikBi1WTymSXawi-m1nHp8sNiRiXFz6fO7OJ9etn9jDfg5Y-whQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyNkQ0jU19HgPm0kdOOuc95LyIE-e7XZjCac7DGDFHVaBwLW9h7FUO7NExUatqBP4WuYT38ko8bBQwMTmIRxPJz0K9pK583dAgCf3lvtk59fUpXoXseyFpTUpCEWsaBhwucpc9M7qx9EanosE3T_wbqBcT93A3QmLE7xaECMMBKhH-PxyjloqSBJ3u7aTuLzeuOeGECMIi7i82LtU4pMIs-4jaJnQHgIARRY1ufHMMlprUzI18sggOxvkN7t2FSfEqn__3kksU5BCeSPo1Ke60Zy15IZcD4aXOhLwpVuGcER5tfy3oTM62qQ0H1jxYPF4EvSxTEAydX8SmSTFxuGDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEPKZXTAAkprGhh0o9K_2WbE0FCRPV3i-xmcXCT5PrWuZed2P7qfbthk-LtegRiYmVoocynM0B5iT0iFBt7SKNscwytmg5PJIJbN8xssULOdTJuOIzV4cIX1fKxUMqqQUTuyveVmbkMKC0uPx_nP_yHLbySIkpPsHU-iSr3bT1rwzUujcGJjFX6ZflohL71V3D7lvi1afqlNJFTLBoLgIVC_GL0pgE9gW6awRlxC9ATMs6x3kGb13kdP_7X5aeXyQ8VMg_PleLGaEBfKNcKm3Ujhi6n2J5PkqMmS2n3CfGNWU98wJJZ0E1vkLh0IdN08IQDReoPgCpM7W06bT6X2MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqpsshkHMUR3u5JBa73GP1n3zrjqiMOl_l-Nxhr8-nDZBzpi2855vbuiBl1vXXEBoB83Uhuu-MivbhOqqd6myu_y2gbDDggMhHcCOgZ--y0o7XuLNMrH3dzLUD0BVH2maiOuVP1Zrb-gF5H2r3fjkZMBbCl1gZ_qB9GoleYZzwsyTbRrBTEqDp43humW9YKOfWOaEWW-IjzeK-SZXyzar3R0cWBi7dkdA9KSvbpggC5y01geqGWFuRMh652GnRT2of2zrKADI4dRGo_-TqlWAtbFIcKQOR6FBvs5go6QPcUvuki5s3Nyht9muxyg8qv1ydVKvxutBvKgvN9Ccq5oNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWxnjLaIzSBuG48tdVat1Hxxb0p80bw1J2Muk6U02NcEwjrcFgMmeNNTZzKVFvh_uqp1CrvxxBbDO1yBkxOavZECbXTz4o-6h1LkP4-2XB0-_hIERHz3D2Uz37IG1PlAI23dxAwk0tDLHp4cOUq2xj3BzEIw0mmS1Uv6njJfgr0MHHDzUpE7yVsm9R9m5F-xooUJz2SFVAHyV6Y2tQTRk3rk0luzpolem1fnTgy0Qr8fYxxGR3KKXhp5uZPHAQk4cG5BvBCx5kxqPPblUJbhJ-tOkVSAWyYMhU45fnEZezPugNB0WNEZP19aVimVGj2z5szWIeDBj1930abS8G1iEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S271obPjCCbqHBCOjp_O0CxbYFm6Ezncr5p4Z18L2cn8JFN5bvZkIoaxyoRcEoj5yewm42b6XN3esd6dIju6tuSPMjtyeAOsDi0F9Isp5utiuQGiENvfSZwtNuWFd4oZZcPcJ4HBnwNsA5ErF7MhTmf5z7qdqAcu_U2bVu6V_gNYMxFVyTCt-AGFpsa7J8YzGQXeOUemP-SDs09EVpBZqhfyvhjErw7qn7kTQ-kk3W48jOCQ86yDkg0vMoPafzm5AUeKdzRyGYv2iTOSwdxhBaqB_eIMNWk01gU9k_h4ha_cP_ukOK4_iDzIhtFxUO2uzv1eEaQeV6tHnCyjEe-POw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIhprV3CSCICB076RcjFm3cPjjzviv46iXZ7-vJtYlx-ldYrW_DJ4VV0OqaHkm6Uz--6gsQ9Gmp2Q6s3IDXHSsJMFIA5EUVGkQ1jcwuBRS--No4c43fRUnDYL8KuFSeh7THeUP4yuuqZzp8_lllf4DME2dr9Q8aNWc_OsmIFZrlt4VGcMTftFaGojfcApXv94q4kZKHSvAPyKzx9VfHl5Xq0WjFEVvQwEcaCzS5RuG0Aj3j15DKaiUVZnrbdR05phgJOUgonw1JGGL7Z02hM_VVWiq7V5A3o28po-FMQ-xfgxKieSApM3x7NtwW5g9JCD_ZHZY8MSYxQ3qOWWJ6H1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRG5qMwPaNvqwleJ4kOz7f_ObNXmQHBzoEVCHIW3cjgfjDii0jeSdcr58XfIBOFhyKvf0uvMRcFuC6fq9apkHzxg7NL3Zkm6WzGctal0tngphZA7nR-MrmpYlCANLrp0LyXqWMuTD2fn1MipfIHtAFdDsLxFhewv7CfNY-lGPvQrRu28JR14DeScC-WuWqYTjnmt_saTGnVH5v1c9h8PuH5RhGk2q-9eIVNO_rulKd0qZX2F99hT6CRnTgWZYCQhVcsfNFQa9uCV_TRN4LEJq_X86BJilue_WP2n1fwMkKYTOlVNFpwtVINOxKIFBWoOsF_Cms6KMiM53mx3B5CqvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlxuaFWKat971BTOZJ-zBNiDq4rCo6ziAoiCaH36hga_vFGGMJkttHRsJhtd37ffNvpJjCrFBQRB3Wln88uVVxQgPB2mgGQ_mq-QcQxhvKnqEUHpzVBlGNNM1EPQ40KngVOTfCT7WjIwmAJe7FpRd-o7i78upkL3S3AvJYvzbYI8gZeeDp_ZaeWlN8XAaSr6QO55jiG8BRe8Y1oUJu-qokS2pCZ3-BJzs0zNeN3p5VdrebpFoc-0mE5oyqX8Ef4jQ4mPlaweZG4MfrBjU3Suc4FFrNmEcYwqOpUGoGTLF8-T3H2-fkH9XTkWwxow3I0b0dyxageyv2B1j_UrussZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po5BCwEsYy57G_-usJzt_L7AQ6fIzmmCnXy2eow4gqik8EKnF5UK4RqMusJVvV5rXcM77n-mB9tPO2tsKuSecBCw0hsKe7OLihoL3BW9Nf1e6s_7aXfKAMxzYIW-tZ1ItNiWAI0IcNtb-7TyQyadL7RcL-KiWjX2ceXuiePo75PtdfkWFBs5MbRMa104hyHtL4fJi55pR4xfAgSMRVgU5FMOBrAwUcXWADjbUXhqJkJilysuYM82jRZIP4EhsUAYKTxOHQSICmWHDvIcO7Y5y5GEddXvJyYBMynshARjE-MTsPFFbE1EInN6OcjrVFh4x6-T8FDhXTOkhdYJMzERiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ0ef0dOQAA6LWfUhsskIMYPBNuQGaOmz-kvtCOYSk3cXjL1FPE0jAdRKuahnHMXqHQKMBjepK-KRS-ntzsT662A0FkKt0CWX87ol1365jqWRA--z30jh5BGTD3S0EXaMLpd3674G-Lo7JgLe4s9awFJuJkE2sv2yc6kWHp2anWxt_QkBjNpLwfomxfOGi6WjtBJ2hEtD7k_K1qZvwyiC0tCCUKGVBnQ83Sea3Y3wHRzdY4fWXv7DTx3MHB5uzP9hva_TXeDCCky6v90z53fllTH7J5MrGLcD5ezpuxkQhFLcFDfaj3IgGAHVcItlilfb-gkIGcmoDdKcZctRDyUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=PBprDXMMxGYVQgnY9U4aPGYUNFqHhfg0XoiAT2aYUChXkeN7A668DoiRHgYryVfVuUrge4zVREEDrXhpRT1dg1K5RnUXr82gYxPzA_08LpJFG2twOVZjpRvkA4wzwm7vWY2csPYcT8iRBMgCAdOcipCn4TyZaw88AXjwxZz9V1sj6WmXuzjyUf7wI6PkoiYPRwDMd64Pa5FrmcXbNBb867_O1rpLnZhK5u_pPChoif15H0oIH-N8Qao0QulhdDo8J_9uk60_5il_fnrCdHVMVfYBVT0xOSGQ1qhRgHYa10R8GpHrZTYxb-eKIF96ipRoiBTONsLB9T4b3LBxMAgG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=PBprDXMMxGYVQgnY9U4aPGYUNFqHhfg0XoiAT2aYUChXkeN7A668DoiRHgYryVfVuUrge4zVREEDrXhpRT1dg1K5RnUXr82gYxPzA_08LpJFG2twOVZjpRvkA4wzwm7vWY2csPYcT8iRBMgCAdOcipCn4TyZaw88AXjwxZz9V1sj6WmXuzjyUf7wI6PkoiYPRwDMd64Pa5FrmcXbNBb867_O1rpLnZhK5u_pPChoif15H0oIH-N8Qao0QulhdDo8J_9uk60_5il_fnrCdHVMVfYBVT0xOSGQ1qhRgHYa10R8GpHrZTYxb-eKIF96ipRoiBTONsLB9T4b3LBxMAgG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUXpOi8pNhB_Xl5H5EiyqU4Q6nzxpRS0aSO7PFSGEmLkY0du5DEoFh_d0Tfr4JKOn5KLkukb2ofLx4Ty29OHiG6IA10JSNLlSEZcGrAm1AP2FlLz33IuZIJv2oVgHjU8SUFPmFcJ8fL5QFy1A9xQwhZzraeYbFzGZtjFpwXZp2aEdgj30fxaTjdlVVaxqBrPbpaZMhICxNC25JArD4En2MIkdRFdLDYmDnZwV207bIb4N5Seyw6yP_WBY5NijhenyvrOkFw1XhNdsg-4sELrki3xaKr8hIcStqlnIC2e8wtZvkNuCJ9fHSzIeY8qXSFLuGiC-5wEsqd0MLrCixjg-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd7wHwj0aiHu4gAQfWN26vBSDqTRWslTS9WeGuMLqJCbc7tgt1bl3BrYoNDNY3Fg_kqMKvi49HTKpfqi8wl0Pc_VZHlKO6C04CsRMZ7ByGwV6jS9fP5FGyYazN5N9j7GfpRaYrb9PawKZarGmhu7U5pQzwpcjwT2cIobXaDV18qCsPPYFX-VZSrRAeebKI_mB3dELXaR3fs7oePNw1c-IAeWoEgFh4kCnvY1HOHRzPw-q2gwkYIO9WHmG6n8RLIquyKjKyp_tORcw9vI1346DtosDSVLIpsNk5Y7P_Npa-0CG3yuRu9MGcTk3yP5yor61nLZYdr58i83vg6tVRHyqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=Pn5BieH3TxDP2Jg85j8JUhBvOklXWOPRWQ8KEMssL9c77w6S3KY11dKiWb6CAO8Mt3k9s_JmiP_z76jLY5cmcHRezQM_lERFt4SByEZKt8ip8r_YJQ5Cmwh6kvOWJhteC_4QovD4W0__a-TcmOjSyavQ8HqxcX1f26SDEi7bP98eZ7tlds1myHQ6DW6lKn2-5Uv3GkhvSvI_kAaTahIoxSU9mniVLkEbXvSYQrLbtfUDtvoNMhvOeXjQwixtzlvbLYszZRImYpwHXAgaUBKRFNq7G7owW3v_9STWbsSM2fbBHt_AyKvaigtYa0l6KTHBWx9tBjottmUR03Wm9u89Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=Pn5BieH3TxDP2Jg85j8JUhBvOklXWOPRWQ8KEMssL9c77w6S3KY11dKiWb6CAO8Mt3k9s_JmiP_z76jLY5cmcHRezQM_lERFt4SByEZKt8ip8r_YJQ5Cmwh6kvOWJhteC_4QovD4W0__a-TcmOjSyavQ8HqxcX1f26SDEi7bP98eZ7tlds1myHQ6DW6lKn2-5Uv3GkhvSvI_kAaTahIoxSU9mniVLkEbXvSYQrLbtfUDtvoNMhvOeXjQwixtzlvbLYszZRImYpwHXAgaUBKRFNq7G7owW3v_9STWbsSM2fbBHt_AyKvaigtYa0l6KTHBWx9tBjottmUR03Wm9u89Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=oYFRjPDhMeaSzgnPbHkL5hbXpcVhrHHJEnP8Hi9_Nq2b0oHrkWzYn46u0waHPBGGsuKAg4Np_sRgC6SIF1G_lKCrss70naVvgkGgcOS4vW5ithNu1PW9Nrut2ap7UFY3aiIqDMGRfcoZM4yUDyIBAzzlPc9J1v7RVMmU6WMGIe7RAEZxcLGXaIo02-Zs9m2F8vhtnHEJfSSzxdBlbgIoqkLDnGSLkxk-NmI54fQ5kBqM_dNBAhGdB5CM35ETKkQ3aeLR0UqG_vmW1OV-6TU6VNXckumSR4_GmNlSeP8pinIw8xWchJA7pOtydLjwEPnjOFkQc4AuY2YLqGZqtB9thg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=oYFRjPDhMeaSzgnPbHkL5hbXpcVhrHHJEnP8Hi9_Nq2b0oHrkWzYn46u0waHPBGGsuKAg4Np_sRgC6SIF1G_lKCrss70naVvgkGgcOS4vW5ithNu1PW9Nrut2ap7UFY3aiIqDMGRfcoZM4yUDyIBAzzlPc9J1v7RVMmU6WMGIe7RAEZxcLGXaIo02-Zs9m2F8vhtnHEJfSSzxdBlbgIoqkLDnGSLkxk-NmI54fQ5kBqM_dNBAhGdB5CM35ETKkQ3aeLR0UqG_vmW1OV-6TU6VNXckumSR4_GmNlSeP8pinIw8xWchJA7pOtydLjwEPnjOFkQc4AuY2YLqGZqtB9thg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=JkdJkCKolXYvmLCulE7rtKJk15hi1uP4YXLPLrWkr-XtQW5GkLmuYuUClQ1w0_3TjDSgK0VtM6CvO-iX439RKAcl3nZwDMsJyf8KZPy__mAvNnzaYl4i3t4qkIg8G4G7Bgm67oxX-1oe-QE88hCY4aDMQI5QCOXKZmWfvlmBW75FeZ6xwSZ8BYHtY3Tyg63SiB7NVbMSCOVwmlCSuTiKyRfETXx9ReRgP7OCXDMxKlpsFQ6S0NxuS_VC1yqGIRBuDaz5xS8bO8Tysr5xDs5Pa1abGOobrS0N0Me3hjE6g6fBuJjGgfEP-eV-ipbJSb2qyKBDijUUNBJ5VEos2Urf4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=JkdJkCKolXYvmLCulE7rtKJk15hi1uP4YXLPLrWkr-XtQW5GkLmuYuUClQ1w0_3TjDSgK0VtM6CvO-iX439RKAcl3nZwDMsJyf8KZPy__mAvNnzaYl4i3t4qkIg8G4G7Bgm67oxX-1oe-QE88hCY4aDMQI5QCOXKZmWfvlmBW75FeZ6xwSZ8BYHtY3Tyg63SiB7NVbMSCOVwmlCSuTiKyRfETXx9ReRgP7OCXDMxKlpsFQ6S0NxuS_VC1yqGIRBuDaz5xS8bO8Tysr5xDs5Pa1abGOobrS0N0Me3hjE6g6fBuJjGgfEP-eV-ipbJSb2qyKBDijUUNBJ5VEos2Urf4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtMUIDJ1zSX_BVScwXXJ0Ntktd7IEcglMBBRlgzgGIqZbOqu0cTLACxe2n2ENP532MOLb9GJIKzYgi_xX6P6HkwYyg4LAln_bQppVLsa0Z5CSSeGvNd9cHGARKu3hLXPYDAZoUiSo-W4Ih-v8OEDm-eMV0xm09WxOkqLravrHlFRpd5CHriWL5pkjlnOKI2Jgr1d6OUsTI5pxMBio45Q1-H0HtgxInAc87YwEiAR8KxMAB1fluBXvfG_4_qj7Jll4SK4C_4Oin0REzVOU7GezwzEdVXscYeo5qxbPlrfFHQxESnOq-sQohkgom57jk7wdRPEGnyHOxBqUEjapNtWWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=PY44d28iFE3RrFSNRA6ZolTjIOvPRWumlwhvXANh4JxCdh39TcuUsiTAvQ73ybFvf-Q6mLg-x68cliuMilmYVvzg04lFIwADPb_kV-lAEWcB1JyZzv7sl8AjvGYZ6w6iMtPWevFkKWFHUexdLPnVDhyJogRXPjivtV3-e2OY2giuv3Vo22S915ODer2BRMj7oDq3gnmTJM2phyydlKBZEJGM2XevjxMFp2lvPqorxbI758SyEDmC6ioRsjxx-6m2qodlSkwYSUq-_ke1S5IaD5tJn_8nLJZE6cn6Ny3pqNGtpbi9eMRMZcLQK5gKlb2KNEOxNSdZbI2rjkJR4NlI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=PY44d28iFE3RrFSNRA6ZolTjIOvPRWumlwhvXANh4JxCdh39TcuUsiTAvQ73ybFvf-Q6mLg-x68cliuMilmYVvzg04lFIwADPb_kV-lAEWcB1JyZzv7sl8AjvGYZ6w6iMtPWevFkKWFHUexdLPnVDhyJogRXPjivtV3-e2OY2giuv3Vo22S915ODer2BRMj7oDq3gnmTJM2phyydlKBZEJGM2XevjxMFp2lvPqorxbI758SyEDmC6ioRsjxx-6m2qodlSkwYSUq-_ke1S5IaD5tJn_8nLJZE6cn6Ny3pqNGtpbi9eMRMZcLQK5gKlb2KNEOxNSdZbI2rjkJR4NlI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVa_Ark-b48AFICu2HyV8SPyhMvukU3Q722j5-hmhNd6MxovnXhOINCBJh-yjVDQbj61uyvYirqPWYa3JCXr9UuMZkkABGQYDIwvnNs915q94WRTmoaHDMWCdaRbm6xhVrR2Ax6N_lF7Fy7u1qzgeCZJiNc_wMPpTEpZn_0cf0VjQBPWz8ZMoWblO0WudbdK6ln6GCWvyyJmrTO-vTzqI_i6P8f4OFQgJ3WGN_qj0EfCAnnCT6VmbxhSKvJ0WWahyrqEl7X1fLt8KFe8e9wkG0Pcucn5cfmXAGyv2PNFUVBzG-STJyl0S_OZDU6EIQRqWJzV7xGxDzq9dr9n095BRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiiynxVG5E1-oknrDioCiIIqQ3hpqlvoAm9r6ibegYxouCerxXDJoZJA_YuDN6J74SYUJniLA8szyrC4_rDgVtsxkr5RJpOOOdozmm_GZGxK7QlVKAQwUUzsN8j64GvlovBVl8hSgn19Ie3tusOYG-4k-iAz122F6DGIHrfn8T04JAe2VIWShIp2Shl-_r8wUgCE00ZLGCRbKxmf4FPLgkzp2Wqf63ZEPcK-NMMRyq-dUYhIrIpKrcAt7wTexitWXY6rcd8vHIRWmxsc6fcdM7t5PUMXSaOeopLG-b5Q620N5vHVEomwnnI94bCo32fIctpJOuJxGgHG0aqppP-F5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHcRJx3cXQalDs9UBvKVbqD2AJH7IUWkV9KWaTTk_vUevTpv4j9qSF6OvM_Wn4ANKGfcfBDBAOynIydxrtXoe-MF1RpqRjRKcjYLOy5JXNa8YDMuRRMa6j9pML356esMf1_-fuJyJXB41gUUFO0AzFfvwS4W4iG59VcKU5yPhIM2KxOic5jX8FAbUMs1Qma7wPTPUcQnV-cVvJHRjKltmKmu8Ey9s-2d29-aXp-Z6LlEpCYdGhle-ABLfC9HKHdAtv2rkkbEZnjVyU2M7E2JcHzOUtZDOdnG8aog7da2CzH_mXTO2ySARU_mbeGdmNkF2JQFZwfiH7vZyOTUfJwFoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH6W94bcGjY7xfWm0qZFOlqUFH4IpT-C6P_v5UFXcvBq2ZNGWeDAhfPW-kUUS0XDwHP3SK54x6ZClI63zPuRUc_abE0LuHY7g5cj0IxtuuDKuC4RhdA_j9DLKyvHm2NSpfsqFf9d4x9A_HVjkBmiGXsT8Wp4xi8adqjp5FCda8RWAN3m5-f5AI6eSr-3zhlpMViZOunvIe9qR1p3epNyuarPgjdj4BDH7ETT2vmzNoJU1XV5o_so_4eSFBO877qZVs4IUgJlFbJUPnORb8dDOPx5l2yW4uEAzQcLL8zlihMfUklgDASl45_cTIt5lvMe5juB3zg3gJCx_qnNFa8RmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d88Ow_iLF799F05Xful9X7agdbR--7fcDG9FNS2cAAFhLn3IXGIFmOGcYegs-yQEwXlszaa86uFlboy3cuzPINSV9bvmqlHwPJTcdPq94WpJkvUA6yBN4s4E8YHei-mVmMfIqCXkKPPiDTmCTVZfv939u67sNpK375V3pL9oUZZUq2TQg5uImaZX3CjXSrXBbIZHLQd1QtC_aTYixDLs761VzTmc-mipvAsTvMx2WqvjYc1jdUlSnINNAFlUO9Gr6owRWVz5MN6sqjjTP9h6N_YOQ-vHr4VGeolKVkBvkbuPBEgesV1wVZvafsCtxqkzPJznOF9DRCwVFOEhCkhG3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHdEmtkdC3Cb-vkjT52h7NZsB2FYHG-3Q-FCk5Ob-xrVwCYHs7xt3hCjf1epii_0Et-QRludtvmk9u-NaIonOGR4jVueDR8zyMjj2-xQOHUqCTdECz_dy-0PvVOH4c4kkTSgKlZXE8PI5vAjPSQyZBuCp5X0V5m_9r4U8InOxjmpdTWiFRjG1r8NEGtzFf0Bx_oximg5qnaveS7eXLOvE5ZaMa6CR0RvdFlCIXCPLZ6c4vfLvL-Afy7lVLgi919cAFZjjBMo8E73rYA4YQtZF4xk7LAob0bMzutudsalq-bWKYuXzQH36JkAgovKXJLjdYk_buUskiiQz98O9PhBqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNfnhTlE5l2PhfUwnx2oCGM2l2Ny7J8mmceRF-PbsrMuN8AOdrxa2H3h9Gdzd5Wz1zlCUk5XK_-iSYUF0aamRnV-JcScStSjmvot4i_JgNGWNURuS8Va05ckws7FeHdgjelgVL7-mR7IigzxfJqn7d5YPdBtTvxKqpk5Z4sEp7ucJ6MxPGThIBk92xKTJ0SGVrXQLj9undQcuJ73pENkq1E7stgPvlBqavg4pTTKMkC_bHSPGP8bjUgUwtjxg3s239cIXXhZMrefTTQNRuW46MSDL473jtixLnP4lh2_FMorCgSO9Rnq-k-NLbezuXfP-mJXx17oudfo3SqdYjGc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIF4l6pFg1jRqrbtYCwNchcLHPBMpUdC40ezX1k3dEJmDla8CppMH-LWDfzqKjAGYeqCpQOOQipR1nEAiXrkagNjmRXKSVjhV4KxCoyrrCrMZKTAkXgog4NBxSVVCyrT6LkdPiui3EomYbkWXruwUuRcrSuKMAlU3avB3H_IdxjPe1j6i5lQ256KJ1ycJSU2OVPQk2wT_DiOJFELafP1uf2FBAOA1wOpu6nmtqAQtIvUvY-btuoMBJq1Zbn6HbKiQhRMialAkp_C3CvmcSCshDjC6lxi121cecvP2kP-3EXFCuAhT2KnxAy-1NJdxObDfymd1C0EW73QOkxiAsOK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N71KI0CF8maMd7OcoAzCoBiE3yNLd8Ga48V4NpH0K_-qowu_y3_V2g90swGDk8I2RHWk8hYTTw_Ss1osFt-oHtXkMb4DiYqSUK7XX8AwDA9-Y8aNcGOK3G9arVg1i3s9JxaizNXCV2R558dYW8a9VtUMXTqOxa1_hCwU85v_4Dza5o5SVXGVJanuZIEZ5SXlmzuuLmT7Dm7yw_yaDSD-Pv7A7OafYIWD7lh0HpRNDOT17jo8fQUrYdqKDask9LbaHT12oJSQVrcV5W1TrQtrA178OhfTElGVJ7uSrZrtO3hncjyI4bP_jdH8AoSzLFtjEpmH2SpjgY1bR4nkuEDTbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN7iuu3R4S74aK9esoLVsXuwxPisQyeqMuE9UiIZgAknMcrnblpbSl-x1P8Sf_RLw4pdytNLMzVP0wZdtYDNK9OFcA0gzk68nvhEAf8tUi6JZGDNWc_3nGLrVfRa-cG0ojwqPohCYvYK5b00TlJSQovQT1w_zNhZXE64XIwYZyxI1Ih6hYEQEVObRMkN_K3fCPWj1QM0krBOoYATcc2RdWG0brt_i7wl1C6HN4BnFqxXMNatmLeOlA2s9MBu_0yA77WJ__suSOXbO_6RaIbELHoVcpb0e2YNRuj2Ct0XmRlKFSgx8xy45oVVMgvX_64fFKjdxYGYqFIX8s9OR0JX_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlrtj58SXqMNrb90X5RIBTuP4oCwfafr_wzRflEvUX5l8EGTcuZW9nv4fbyVewxUGYzXv1mLFkhETuF3zB-e2Uo3qzVrC5DfxNKWDgnZsVoFvPLfKqWGkK34dO3xYe2TgHOuz8zxBHTFFi8S-9igM175MgZR-Oa4ipb8sIKKoyOh3Oto7OCRGDdToHnPa-egqkGqrnarzK7e6Edr2iNWpjZLBirC8j7YE8zApTtiLqK08iHKsNsWy1DyW2KNyFOAcZBlshzksHs-bT36b1SQRkHb0ja21hVES65we6lB7VmOxKPtheLiu3HSsGV2RfumeYwW5hncAXUHvJh2vXuJaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7u1PjPlLORgVYEeF-2MLcCG1ctsavbRUn6q_dT9_ddCNefqYc_eP7cZjiKcrrVxLKZL0bLoOOk55bLEDItGaoeEXUVsU1OGh3il05ofLoAZjpr2XZ-EGIDWLPYq-B6qTz9gT2l1pcwY1Hs0LKM8NZNzSzolSATnBhuLcI6nssq8hW4_Y5NdC2Xk4UMzP2g0oD5129vZi1giJkh-terC7S2ih8EHO2OgKxNBkYifCVJG8Q05gLftz8N149ZqzVm7cyfZCUFbkbQ5ZEKpSeHwg040h__ETNzMUykzSwk1sij9NXwdFvIzS9MmmdQ5H3HKk00q04-fWEhoZE5KtagsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS1cnueIBU1SQtr2DgGA2ypfDXIpVmIzE3S5IuA97HApTPGghIrbiFvmBpw2O2EZe1taQYwOORZbn3JoiDYi9A4chVMCm-6LEW1F82alSkGP3QTjU1RIva-0DJgZ53A2JJvshdE-yF9jtg4NIx_glcuP-2QGfuXsl02S9IENgL5BTM0V0cFfsaXtPySaJ8sQ60kNtqSt90gUvkoE0p3YjldRgcnOoVilOlE3G-ik0qG7pG7WGVszOwpVH7eapEryPFzy5DR6za6JY-LlJiu80_gIxx0ZOt_TJ7myV3JB5jV4tkP7vsdWxRUnKrb3Zh4HO4fbsP1zJEJAzo_OTvhikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3V70vTqLF9sJhWxHlmPyfP3NC9nW6NJOUmEXUkCo3FLnn9SpuZ-e-WrRoM7ZSMSJ0HKLdGBMIlbhFhaJEcc9TG2VVWYj6-Y8sjSrHsj6oCKmGT1KYj4vml2YPjYrpdRKNQYgvzfyp0Ak0NLlukga0XA_zbV1qAXRRlsNkASSn_awHxEsfXkZ2AqRuTMyVN9NOCLzmspQZJMp6VwJGdHLS9_PPv7J1ls-O3IxnDc8GvMdQcSf2Wz66BuV6laXqmvmUimblCLqEYWNk5CxxOgyWqfSRy-KTjGpL4M-_NnOeqlbPlu0DVug4xr-xw9VwkUVI_58wA_8XqOvFCpD5al_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSWGK7bSvWG44Ax8or1nXbs-bQu1HFiqMzXtHBOxOxcRKUoKOXo5AiER8ZbEgRr-IVGTe2z0JHaM4-178olLhkuuzqg2y_UD2ingLJeAGkFGFQD1HTECwZqCAtsb7ZlCOfTQyDF2MhXDlSPTgf95lCWHmD6uuVWPb65JA-XKuVksNIrHh7II382Iu8g6G0Vrlclmqb1ncUvrbhVwNTNPdyQ2oHrsPKOXpRcgn8TNp2g6JZGXEzguTgNEWNwR1Z_kbA1JKVHOmV2f0l1PtKwmtUk1A07_9L-GjZH07ZMkB0rO8bKxED73QNxBkUCq7h8PZgihGTt_rfW7icEc8b0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhi13nENmI2AQuIueh6ltF32QO2FIBpIUIKkYLlXdFPyVeyAacnJw2leR8mWVqvLac_xecgsDyawLhE0EtSpQHij4PT2x-OVhOnCf75rXXSNU1VmDSrt56HU27apJfRaj1NFpq5bqgBYRA4UmL0Buv245T4iE54IE58-bknTA-iuXkUl7a6pCpPdcD6GCMXW_44B4zId0s8RGruAuUW2pTfRnaALHsFoK8zE-kC_y6ubKRAwFJD9jzmcXPSr2CZjSoWVsAb9P_ULnNzf6uWcrF9LVsxKefNfhZWALmfn63USNGs8IWkHbXFb570pnkPB4aSalFdVovsIG8fuI54WPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE6AXCIuWtL_-pbBgRNAQnvfUPCIgiggFSI-oTJt4aIaMJK_-tczRPivrpFQqVjr8q6EIorLCk_FCUlgakmsLe0YtltFnws6U2obLHowR0CPI9TvR1P0T_j6mKZgZhcvNM-yRmXCTjGLuFiMDrXo2blX8h3ZKTeROg6h_2LnGJxN8iRc_F0DrvxclYBmaePshsABTOz-dfFzrvjX_oJIKdVFj7kOpTxy4RvbP8aChkno41ZjC11aMxH_q-PANf1-4FU2En7pbWCbMlt57KwrX6RHzai8xALWwqbAM-sR8a8J-q8wwAfJ9OqVwyxsAycftIER190LE3qL5EreDp28qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTGws1mtEqvGKYNQa2HPL8DoBmVK21VEFiMKk_ieg4ifn27sEiZPTGq31_TfOLFEz-PgjtDfBtzsRc-igZ8k4AYXttVHllgTSl3t_4O_lUHz7jl2qM4Bx6hgrcjrjo7TVoDmhczX7Z2h1-lxDJ4Dc4DitwkMC0C5VAgPb4LZhrq7zr6svjeWaYWw3nc_LUfwVMo2-3FA2UfFQuPLDc60yfqHL412zf7jPYmEUdqEjsqsGP1tQ9xwagEcKVEqXbT2X6WPG2FZP6TRap_mhW0_ldXd02BsD2f36ogaPy5Gt-bF7Ny2ptzOOzoUMLNm1JIS-bCIO1O99l_Fa0l05BSFsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=FJ03jBfoDPVC6XUreHhCChML1aO12doQ31M_WHYNwE4gqurfom51QyQa3v8Ybs3FoPV8Nri4-0l2zVqrezu3pxn7wBz4gIkpv-OPuip3CPy9OugWPXEDKfQq6Hu3JOQ3qo_mz6CPAU8HDLH2ZBHgcSjAdEPM6u5juxSIiamJq1us2sDBURRmY3HDpWn8jdsxZYoLESGBUQumfxuRZupYtcaIud4272jHjf0B1rqyxzHFeY0KOWIHt6P9MNWOCvpdimLnuelFnNptA46NzVX3ufpChY2UM1equuvrz3P4kNHr6qAosot_8pjOIiurmeWhjdVGK1cvjg0flsF7G49eAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=FJ03jBfoDPVC6XUreHhCChML1aO12doQ31M_WHYNwE4gqurfom51QyQa3v8Ybs3FoPV8Nri4-0l2zVqrezu3pxn7wBz4gIkpv-OPuip3CPy9OugWPXEDKfQq6Hu3JOQ3qo_mz6CPAU8HDLH2ZBHgcSjAdEPM6u5juxSIiamJq1us2sDBURRmY3HDpWn8jdsxZYoLESGBUQumfxuRZupYtcaIud4272jHjf0B1rqyxzHFeY0KOWIHt6P9MNWOCvpdimLnuelFnNptA46NzVX3ufpChY2UM1equuvrz3P4kNHr6qAosot_8pjOIiurmeWhjdVGK1cvjg0flsF7G49eAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoDDQAiZs_opa_CDKWf9lp2WdqHo9eBTZm81S03N3t0FOXXCo9-mFS2LTwikazeLtxn2bWAz4vHawCfc3L8Vitou8FOhxg4MN9RCM5A8m6295Uz6nPwcJ4W-21z_W54FwA5Dx-hSJa7zK8Vo5C8hXw5YDMBTPhz879POjxW7y44hQBpMCAV0pdXyudsxu-m-d50sAFOj2POkJqAObifRwfqNsih_16hccusoYur8q3EPIgSQkyIGP69snpRc4tYjoZj9Du8EjZDVUAilvgCNXhP2aNYejo88Zb4t-PZUjt5-NlXGFe6-mOyABxJIkaogBIkbzifpMNEEfX1emhxJrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=dh-E_wZ60wyl4bmklMw4fyBnTK0ndUBIT_9Nznd-cLokj7R--tJoM0xH7UbdfO9IsZ_Zm0DCsrsSaYj6POsh5X66n1PGIDUtsaEsevx8vm4CFzEBcyJjmAQFP8U_QI0GB_0LhaKARIhqxiKN_07ji-ZmI2iVXKNcq4ggP6FFlHHMFAZ9rsRPzWBWn7U-rNwKx3T80WhmnSIv7w8nd2kSDW9dZS1X_65JJbSlGWjTrbc2znFPMZrmCpKkneP7SJ7b8YX8tn1vyHOWT_eWTkT70NgU-7TmZDu2Ku6j8MK6aUbG67_WxOnvUpVhrN7IVFJcT6-MYdNB_1eMs1H44uwrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=dh-E_wZ60wyl4bmklMw4fyBnTK0ndUBIT_9Nznd-cLokj7R--tJoM0xH7UbdfO9IsZ_Zm0DCsrsSaYj6POsh5X66n1PGIDUtsaEsevx8vm4CFzEBcyJjmAQFP8U_QI0GB_0LhaKARIhqxiKN_07ji-ZmI2iVXKNcq4ggP6FFlHHMFAZ9rsRPzWBWn7U-rNwKx3T80WhmnSIv7w8nd2kSDW9dZS1X_65JJbSlGWjTrbc2znFPMZrmCpKkneP7SJ7b8YX8tn1vyHOWT_eWTkT70NgU-7TmZDu2Ku6j8MK6aUbG67_WxOnvUpVhrN7IVFJcT6-MYdNB_1eMs1H44uwrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYHl7eVWgK_a70b0wQ0lQv4AgUbKHH4SpO39IuhdrsHtZSXmmp_bVl7AkW5PZNmnCPGuEjpOwONWklg4Dzoi9stjWPzUFASMWf3ynz5H57VXIFUUsPKwHh_qqis7vkvOTXnPFGAU1XUP6wiyH20XgXWoROMXAfIxhxly7YdwXdHYT-N9WWKwvd8D-clb-dLQYhotPAK0GkbBursN2ZPHY8jCw6FfPRr-MUQhNKZlqfk_EHhRMeGNgRGNPVsSzJFKpd9bj9Rk_GYmTo3bZCQBFCH0GkCcNIrKct88-1Iec7VjrHPVFDofn_cGanyR-PCfM4Ria3lQyQos8XITX5ENvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-c6pFTN2gEMlER-cGhiP138Awtfznkm0w993cONSsaAMcZstgvzN0WTKCVNruONYGvtLRj28OX2ybRhTWSgOVSkCFu_uJkDCbQZeQ2rkSqK-IWyoRJMtjNscJopETOdG-mAhT3R4fLZi8XurupjxI2Eykl09kOsQXQM0euwdQ06QOc_XoQj8ZMxqnyLFfAhZzzJkco51rT0ofX4Vqo4uuwdetjptbio8JMbDhJ-c23H0UftgrFapBDJ2PvdMUZ_gqI-sJ3vwq3Sgo990mxvecQCJbErsORELLBOSMjvhlUWEBZfnwBcKr8qZbs5ElIBELdvu4fv47cuQSiK8EnERQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4DXiB_9dN6-nosuYT9Ps6XFVbVOTejL6zjrtBpYLNFYoC84thDSILvvGtiH6j_VCVdbVSTF8iWiZiqLIEELtEL6NgJHQgXzoBncS5eR-FMF1YRJENq5FbVmn2xS3Y5_-LTZkpGgc5s-5o2x65BhENPn_eqM5cjtkSbDmbPTx0v1zgnTR_TFoV_6Znuzwo8qfb1iGwEs5fXarJrnJsBau_V1zmbMJ_2rHlfSyxWiEIMEIy_w2UgAsMJJGGBc48aj2YHklg536-rjT-WARXgDKWvACknN-nCaxY_k8Cdb277cdblzKQoMMTOknZRyufiMtkQsG5ArdOC-oar7pi66rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4nAsKrIVvYTe6lN97wwIssRN_ZVqEurpMPU73P2WIt5M9rdbEZRAcNn7EbX4FHZfvu3ZIFI4XcPTbQJq0Fkh3OBvdJISjBEoRCkaYxTYvSIvBPl0Oy8K1b6Nz77I6yTAL0dOIoJtO-TfV62-Fa3LWnUiFW-op9Shbuw71r4Vt9MYgcXJyZSJFtvPQyeJ6hPcdT-T38nJEhgL73kUg_egEXHnj8q7g2zIabKps22YkK8UHcZd0ADbfTs5UThOrhNi2jMvX9bkF_vs0rqNsWYod3g3JmLO2SOvGrek5kCbAKB0qlhwJde8ZlZpZZmmNFdsNhlV5yw5byk-zCvij1ZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRrzdqO812sKTRMMPBOPcuGOJp_ofIlOjQ92JAlp654k5OF6gYxkh5wvyFzaLAPvRao1ZbpDdK_dIXDTe9OJwGum8JMqGicfNw9vf4idk5DO9-Q9Q_-vXk_6R4G-M0cS1mngLPuDXFbH2hwt7t4vrWfuvBJBbtNrf85270jtsshHa-wBp_9zovsmefBjeWfnbZCmcLKBBrVRPzCUsWld2eFNPDVrX0yeKa71woBTkioIt5HkmEAz9CHVEaPYS5sMviUdaIf4x7xizW_Xe3IgEnyq7TTikLUgUKgRNmM0z7lHA2bLNT2UCGImdBXve7sQ4tWCHqmjOIm1RLsqdld9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgkXse2Va-ELhcWjchxmxM2wF_HxamoVLVziA2jCfWW8QY30xrvUJl-AdfFmivElyTXVqUjV_OU7XzDzSuCXWEEXNpdCQehf2m3fC54ruD-6mb8lY1BqBWPl1DUmd3WO_8frhffC19s_3gd8Kbv3F6aa5EOU58VMwIPGa3VMeLBDWJPpFHf-Xk7ctlhbHQJJ2qSf4pbgfmoSdiftLstrOnJ6rcK8pxDAujATEwAX_F2S0RUHCF4SxLfs95oCGNEbyzwz2xsFjTbjAwe0WEQ76vK01JNExE2Rr_FGbtl1GXO628U8Q7J_WW-8wlmo2S9ltl3F6ltKtAI_5Yn7nKXBig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgM4Hzuz4PTeQOor1SGVCtsG5VB6pWQAZkz733GfBWABYnqjjxvHGJGg9z7SAocUX2HcRqvCxhKNktKuaJjuw5KlmNu-j1Sx7oiHHfiHTWss-2oBWX3-8dYagKxPiDSODz_0XgKJQRNbcB7llNvwdqHhk2vG24hUx6DsnO7m6l7POtn5S_EuJkWuLy6tjODYxP-8KN_FbRq4KjIgNVz3dG8pkrfTPheGGIRULA4pLMJXrBGFmNrczPhwb6LsnERywVwd3FJ3om94f3PJ00edsxe5Kx6gB7m1NPEBrTQVSIbjT6iBTQJt6boS0At8bvNzHuflAvOv3r5tMAMre11pEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
