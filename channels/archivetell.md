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
<img src="https://cdn4.telesco.pe/file/osJpVC6zqCiI0Z6sCw-SGM_z0QUvluwNmGaY_JvYyc69tqnkcv6kORZYf5EBhCiJ-18PQmlK4PbSvPvw8GXrbFIGmIHtqgzVc-OdOR8AGoTd5smJQmCmrEVIwyMhkLwR-VxM_xpE_6e2TFB5QHMDIwdyPwYcjOlNvQybOTFbw2fDhmjcXKvJsesrAw_1mbT0sYk4nrao-5f9KgdDJoWiKTnb9fdFx0gBKZjin_Xrkiqx7xuPOwRV0_KNx0E0jgkbJTjWwF-lyE-JAbtmPwiebjwiLuItllWuOVJPbmPXT9gNEhi7Fxh5032Z_r83YCCaVdsRd5_YLco6_AIl5AvNOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9rTjq_t-aFluiCag8o4GHYgpY6_lMap8zf_rt0Nykz_vYM3HpdYpYpC7GPrFtm7lPOLI3rujZ9Sz5st_aVMlF6bV5GrBlY65TTKxC1DgFZpNyvzcSwqwZkhHrOfhS3KrYThaHlLDUMhWwvo3cxevDn_5XKs0BDXtkWrNSS9UfHlFf8fnfjXtEkVjW07Fz_i28psCOhPwh4RCXv1Lm75Hsa-pak_RSN71qU-piP41ZoxHTKDsuszF2GwqjQaEEO0pdsHg5Rdf81psr-B5DoNTDAezQrxdao0cQN3vskQoQ1cbgudNY2jn2SiJseQSJeElnkjSzvOJMuB8JTDWNrgyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 818 · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENUDQDtnGx54iHdIFRNs5c46j-kx-sAeFze3zQsLcq3iGq2l0i_fz0dqf3zJRhdOVG_5CxMT8XnB8UhCCXFnFLJTLJH2h0gCD-V9Ueriv9cwbLnu3JAKjn8dVzZucAx70heVR2PX8JRCi7sxcRYsSEodhVFt7ltHQ5KIbVE13_okzg5VESJt4mPZluyEwo_tc4fKAtcEi-Y-suUo8lfWXXpSf-FWw4DOknVgXwlMtdn7G4-mZYklTFAy97eN9KEl6eZF9sj1skRr7t7KIkX-ZBLenz4QjK9czPIkT8AbCJ_pF4OyOqU5sLR_dAV3_gqMHPHkWKqRGgkXgDSKOjqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYaLRMKqBrVKS0tYN2-qPGLJY0nw2_xNzi9nXNKs5M6LWrnvaCFIDzvEoL2oRBOOiDzUwL0UEtCmyWSCX1u192N9d8fGaeZztimO8KtSFPki9vzD12JZPyHSUR7B71wTHuAsReUcXwjSbyDFWnoi9BLCwkM0f5x82nV1gh1-I5pnZoO1c27-KYiKoyF2ZZEx2jOq1lJL7Ye8D00_0VNbAZ5PDOCBaBlPjFCWZWGrK-yWxjjZ8G7oisfzr88Czf0fxEUb4B1Dpa5RUfvRNcTFNeAjF6W-N7alqerFXm_nnd_07BT1UqLTTJasPoJBxGTOeKXKOCAYZSYXLKFP48Mj7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSLcw10sLEeJSCa9bjZgByQ96FGfCJlsan_NaCnp2K81HvHfyzB6kk_pU2XVkLAKypLbXcWSr5nrOW2vCjBQCOxFeJpKCC54QvlHY4Ba6Wy-pkP4RVECW3mLmtagOtUySLMOe53wAIRKXPJTioqrbgiUIajewBijKre2HF4IRdM5ut79EB_QyQEac4kM0UDotB6253WJokH5HFvDkXhvtsm7idXPg_rr7slbb9WGjlbORw2L-htkDZiAAi98iDp2_HbDrVYa1q-PYVOjVkuGwgPjAvKdz5AHBRkzrOtPE7lig8Mhc6hNNcrqlba406NR5Mn84IoXRCSTiSRbs5Cl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2r9aKhmVmfF_FasSj1RASPgj-ckdf9a7kJ6_VreOajzdRu-wQkJGiyXmpCZHbARXnCZ-lh1hkCdgGWsa-osfnbKZH_FcUCVNBHwUytt0-hZsAo1v8etvcM4EVuMBKcC_8ccTDJbsMb34m1KhHfeuIuLpEwLO9pM__hewJyr4UwltSDsvl-W4uEqTh6f2204VMmjKvIZDOkfAr_TFzX4ihKQJDFLyCuzGqXNQ1FSf0DEUjmY7ACG0vRlDmoVJ0CzwjwkON6lsAdxQx4skU3irRFrLmj5qC51hsguu22XruoTHslN3ye6gGPJgoFtF_0PAiXGXIIEK_m-DBFK-N78iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pptx5QNr4onD8RVfgxvu3CurGpsUZE16TzN4ooukfjpaJCDIyvHBk8K1OVA_18opOCvz8il4RMce3ce3CrCr8dgJIbjxWeu-1wzlK-DEbYRIjJxqRwwaLRFhi5mAutzfopTYjvt2VJNNRPn1-3Flz4F51gw3yRIbmbZyOZkVzSPDtLhjlR_TAcCyYapOUlLV9_67VLgtYjUoj6VBe5QPfURgFpcWWTwCaFFmxyiDvw8rxi5IyGVhkWklHXiUch27yZ2IhrKFVALUI3nce1rR6kh_QJucLTAvGOJhjbOdcqRBWVPv1rXo1B2g1b9SgL2omAeA3I-ny_nNIvljcGq6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=OAC9xvnd0Z0LnVtZ3NGQnZRUqqYh_EOcoHl3ZPMU9ful9hLWEdC7mA6196lo1nWrsyqOm57bXJnJrV9VTamgYPI-pMafIuVJ04HhsoVxHBd-UZATEJcPfv2ZC6ZY7bdG_wchQc2MkdcgnHJ0BijPQdPv5c5edd5sQInWkmaKEwf44YcEJKrTjbSxeyiingv-Y0u8ap3uQ9P5CnOprl40lvKJzCf1aZJ9UhA50ow7nB-jKugwBAKXARph3qcLO9RKqH7tDJ2M-vmLcw24D72JGBeFOoadKDkzGJRvEwFlRE9lKchGW7MaMmYBawNS46mPZ8nMfkaQbKgxT9jMU6jN1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=OAC9xvnd0Z0LnVtZ3NGQnZRUqqYh_EOcoHl3ZPMU9ful9hLWEdC7mA6196lo1nWrsyqOm57bXJnJrV9VTamgYPI-pMafIuVJ04HhsoVxHBd-UZATEJcPfv2ZC6ZY7bdG_wchQc2MkdcgnHJ0BijPQdPv5c5edd5sQInWkmaKEwf44YcEJKrTjbSxeyiingv-Y0u8ap3uQ9P5CnOprl40lvKJzCf1aZJ9UhA50ow7nB-jKugwBAKXARph3qcLO9RKqH7tDJ2M-vmLcw24D72JGBeFOoadKDkzGJRvEwFlRE9lKchGW7MaMmYBawNS46mPZ8nMfkaQbKgxT9jMU6jN1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbTL-toAuohUt-bVYc59maqqs9nwa_ZZwuZdByY5vxarVf5z8GFJuGmab0bEASbCXG3w9Ro0cYxb3W1Gx2HyR_jZzVzm3lwfjMzD335RHAB36ImABirkskF8mITzoZOKsfodKYFFdQzlgMymoLmNEQSjChU4jQxHyp0SVZADmnVbceXLSS9zj-7AIGON_m18zpg7COJ-kO3YJjjJU5vldAIUJAmX2VbdP0q7Nl-fyR_mIifo8LyOn5yr98I-ow6FhAR21G7xuNsU6nZVCZRm4FLm-gQlVnbXSINPIVS621yGCsJG3QG5NBTUdI6Ebg2EyGW1HKh1cBeNxoSB-1jIJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=oRDtJuXE8HOiZXRGpZBCo9gEQxAklQ_HBh_5bkU6Q9OncVGv1kwx-kXVfbY35_WqfDmbgrk734TFwnIa7-eWgy2cVPmGE9hZes82dY--TiFbuzI-dwXogPHNpoQSGEcQCRAl2eoJ-R5TVOpXu0oCZg-nmPvlYUm_-qlAYT0CWpDKfeluBhJXRm0RS89ZYlZgTluQ1rLGaUYvyMSr4BIrLfRfX0pp3rkLC4vuBLOucqJxchfB5xsiLBSsezllXfk9W4aVy8BqW7KpPDxmtg7gJXrh9Fs_weuSU0cwGmWI70SYP1I4zmzMhj7vqkth6JwqngXqvb84mNCvIBl0JLageg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=oRDtJuXE8HOiZXRGpZBCo9gEQxAklQ_HBh_5bkU6Q9OncVGv1kwx-kXVfbY35_WqfDmbgrk734TFwnIa7-eWgy2cVPmGE9hZes82dY--TiFbuzI-dwXogPHNpoQSGEcQCRAl2eoJ-R5TVOpXu0oCZg-nmPvlYUm_-qlAYT0CWpDKfeluBhJXRm0RS89ZYlZgTluQ1rLGaUYvyMSr4BIrLfRfX0pp3rkLC4vuBLOucqJxchfB5xsiLBSsezllXfk9W4aVy8BqW7KpPDxmtg7gJXrh9Fs_weuSU0cwGmWI70SYP1I4zmzMhj7vqkth6JwqngXqvb84mNCvIBl0JLageg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVvw6-P8-jKKlrkUl8lHSXEVJki9z58OrCY8D6ApO3xooeVoPldeC9EwsqurjsQDrepdDMg6hSdlfqyFZZmIwnmjWomz3myxJwddE3X8-ewktpQfmFWZImN74HYG2MNE5PaynFVxvEY2v_lbFPCUb-h_QA1XlwzcK8EbeJrO_-fy7msZmwd4LGnwXLJZH7QhYKOf5XNBoETNGe8kavBPW4iTuMi5bWjeOGkU5ihFAs4rE9FXAdP9PipYlKP67-4KhUVlnkNWya2atvYK1L6WH4OC4v1KeY5jfuSMtkyv4xp-Ve0EzZUhNRhVqQ0pvC1TMjLCxV1ZXJpRo5FB9oi-2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVAKXx45HfmhslPgndZEnK6xm9pHdW7z9YeZW7hbjb4zguac8p9R9W_D7hClfDZh8TZOJn644sKJnXfRNeI_wyFdf13KspO-x98FeEV215YTU9I972-BxCY5jCLj-E6pBcLWKP4TEehI5N4jTD4Ah45rAuv-uBlZA3pw-bMJ27LXC8ijlyFD1SMgoJ2HeQRzhcOliQCiJ99YcGhF9IULAi35jNxdG6H8NPQv0ypWmOT6K1MNE8XFReixtEFTosnioFcsFmRCkYVi1WuqkTChZeEukVEggRq-7MhotXt4ait9dljk6WDsPty6lHdJgid4JZ8SGjctTcKW-kVKraCu1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXQhDESpMS5KP0WdjfVDU0LAtnsLPjBVhnMCfC2pmXiwIuEjfcv4s7ap0RODFq1ZN2W8AwJSzU_Aoh2pyPF3zCakQS_ZO2FmxtKKjI7o1Ek1WyPzbE0pfwRCztl7A8X5EEqtLgrKaJJi0TCIVYMwMO8U4A7iFg1Rp-QhJPV6QFUGicZCCMoLlnHx4rvBhxOtugWmse4gO-CSGEwZigisWMVoSJIP1D_fczGV8_U578OXd6oTYUkX2Kbn61TdWRA_or5mLTdDbe9Mhz7EngxaJmdRuyX_7tqile8fImnvZiDhxRHc41-_tkqQrvipV74lXhVP53uskVCWJeVSvOWy7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAc8dU31mVXWKXbbSVXxFigdCXkg8Om2OXc_P6usKFi012NHNa1OegBOAsXd2fsLy6A4A2_mzoPZeurJ4PsRuKdsHXt_SYkJvXkFgim2Xz9sxDCQQQ_cP5brcn6LExU9cyKt_mmNGw4InvvnuC9IoOwm0OrKQeUbNw5Vx2w4Z1iFQeX5uXmfeFD1At_DZ7THiVqN4rGZe5R7krPLDD_ZoA7KDIbZXNzx0AyeVesOwIGb5qAdWDtuQkG1mupdTsty2oBwANzALPSWnO8qleQIrAH2G4Qrq7l4bNHRjD92LV_NTO_2_XV-qg2VxQVtkosJJaQfPt19tzw6C09cMl_U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Um2axMFpii29Pj5bleKv9Z36F3DgWRAQyZimUHXEfQA2Phg_1ggy1kpsljxCg5lm6G-jYgYrPx8RyJtSJoeipvYQa0CfYz8vTWp3Z4UG1AxwV4rNi9TEC9yR5jN1f1J8LBALVXdSwXQCCXfjShTOeoTf96dc820e8JF17m5PKmvSaumPolJ3NciBmYTQQr4-TCHIo0Wf88XVoZYGU_KwEPdzqJSqjbpphOPQswZcZBnRt89axeyeb2_QuG8tOh7rkOO7Cr5CkwPye4Uf6FR28hPU2SvLUPurt1cNkNDmy1xLkLguCUepeSQJuft3m-QUrNp3tJmvI6wcE86idSZuBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0U34IUZvR5Fw9bzOHvRZnfTGpyNLoJFH0vChnMZFQdQTUnEX5oJRxSQY_qBuIkk1Tf350QkKu6H72iwd2NLoygrz6h4n4uYJOmjh5k-3vqNo7Rvl_YzlnE91864FoPG261noQKxUPG2yMMtO3VxWtg9TimiwR5X76Tt5vI0x7CVI5QzQ9dsNZhMsrXZyAgYYflMNSWlTAyzkL7sXxl90vcw75LnmX6FzmVSwz8n9h84rVke7kLPiYC4zTxpWG-66wIPnaepNWpX5jkpmgwQnhP66oRC2IOb958Vw-lHEFU_kC700MaNgrevm4dLgJNJviEQt-bq9J_SnSDpzuknRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=TyT0Ikammy5c4JJUPfj6SUXHgt0y_lS9bXBQGfHgrl4iCcvAYtgvkJPdg9keEpHAGa9C8CskOtKMwEYgGICR200yCx5XXbqRee3U-WUy6qKuIrPjscSpVg47ccAZDNuh-tBFnlzZI2FGh_mDiSkgjRb1ukw71C7_7ik_DqViL9tJr1p7lXrhvaq5Jk3fAV30NG3A2alGipLcfYH3MGygJSQGLIyum8mBqR5U9S7DUf5-vKLanOp2MvT902Vsxe5d52ruQGgVbmWb2cE9Z9keqDXmU0D-H-qTg8nKirmxbmZA-c5oYhDv6n3y1549wWBgGMN8FYno-96M0pgdEehQKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=TyT0Ikammy5c4JJUPfj6SUXHgt0y_lS9bXBQGfHgrl4iCcvAYtgvkJPdg9keEpHAGa9C8CskOtKMwEYgGICR200yCx5XXbqRee3U-WUy6qKuIrPjscSpVg47ccAZDNuh-tBFnlzZI2FGh_mDiSkgjRb1ukw71C7_7ik_DqViL9tJr1p7lXrhvaq5Jk3fAV30NG3A2alGipLcfYH3MGygJSQGLIyum8mBqR5U9S7DUf5-vKLanOp2MvT902Vsxe5d52ruQGgVbmWb2cE9Z9keqDXmU0D-H-qTg8nKirmxbmZA-c5oYhDv6n3y1549wWBgGMN8FYno-96M0pgdEehQKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TunCihqGykm4OTNcz3-oPpZCabE5_ZscGGvvW0bHTW_v3HFVl83HsfCwHUswvDB2lrRxbCose-OkpkrTu32mR39p4rLjkDzvBosToYFQjB1xlf3YniInhwZa2OYnqqYKJa3bYpicHiEvn1lo6lO3HexgnSMQKf5Idy19MmjX5BC1QA3y8qpaDvSJGW04b1780-75ANPnQ67rDWBA3u4ss90lUMJUMCbfOChpIlx3roHtTRr4Jnf9cg-E2C8nGsx2rcbjEx72vxah4VnmxJeoesFlLBN2ue9piXQK7VEjmiurkzmjfFzrTRHQbRDBHID5TroPIhWbCgawfzvEquuCqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa0gREciHdwrb2xJf9SfljzxxZONwLckz2M9EQGZCKM8afmrfaeP5haOLbo0AXCuUEKxLyXJlaUR69xyht9_hnYIVXUpiREYVG-O0tvYqgAJO7bBIMRqVSHMYISo3xpCo784trvUImojMT1gD48hABoD5lNq30gBUI5F-eKn6PGKV9-BY5EJAURfRAsD250Qnbd04OIW9lS9bBBMtveIRoygzB1lD-yjPkVDkBLT6QvABOY8OGNI1Z7iSkeLRd-GfWUWm5f-6uw70HUySIgD5GICTQ-UowyZl0w6Wr4g_LsfkHTUaJJAxw22uO0Kh98y1rMNWXs1mWj3mOgPcXy7gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qizv_PGk0ybRRACq3MnpPENzYL8XmEzUn6063Eg0yfhYyCOfO3ZOyatWfF_1JfztJvW7PneGZd_hYXP9r9qQU7zCYKCWmO0NNpgdjyzEPqi_T3iBx4l_jHI7UDpLKhPBZUh-bzyBIbDApf6F-fqUFLOB2tLgYsiIYkDj7cyG8e3hI9XixSNJdphZgHkzgregWYRT4-iMrkDTpR7mNjI92lze1LfMGs1Bjj-PlLxNWACpeCVSZYxVJaMcmSmj2sHsXCX-gZXF320o4MRISM0JX7ZEk6nj3SVbfSqMi3w6vhuzAjwWn5KrjThP37we0I0XBh0FOFn3H6vpoCe3814eRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO7_CGKEjr2lh3BifgELHLfzZbeLflzGJ-xgq9i1Mgka-vurimJsLF-6lQUfOrY_SYLsfAzfqKk7eZT86LqBZkdTnBZ9IpTeIifnTPaHUNKE8O8IIweopw6_cbvTvG5sMYra4Ht4ZzXwsgcWZEZocHBwIBLXTNGr8ZoMdWHdqEN2V5y5huy6T5iJCjn2k0ZOVVB50PNq2tO-JQsAvWmKz65lHTUlW71k8rHHb7tEd8_XAxKJD5AzEZ04m5myzg0T6VOwMPPf9kf1E2X2pJ2dJPYZkusEEPVdSuX5597oKfsWfMf2JlCb9OJ6fFnXbXdgGZwHhd0ldqd5cYvKfIrCgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlDfZJTyj5ZG8ZnML8EHUl7YlL9-m5-2EfAkNBZ2ZYn0FCtPv2vCpWddMuJhIDfZ-_7uHcL4-q12rN8SBDZpoIQcAXJUc4JZc4Up3IcZrIKVJEbtAoul8Wk8Hpg6D-x2AszwK7IZEuZ9x1zc2N86F2lVY_b8XzNfqtHT7z2r-xCt3kv7JEui2VfIbp8ihaZwvr4H9vaRaPGj8cRKIgjC3H_J6OmJEjy43LDz5v0hnQ9093uHQEvbcTy-UUCEx2kQuC6qhA45M3AdUM6kpFK7AFz13YJ4tQHf8q6XYm_ARnGyadKz7eIcfVHQhRoppu4xC-NfuBJNOZ8TFwVPLCrvGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQJJHEDtEgUQHE84lpOBUpihcRnfb5APBuZlnlaqvUhMyD_mgm66g64vc56ZTTOxzg5okeNjm_4sRUMmsgV8RXcaW2voqpnMvjZK8LepShpVzhXejE7FvUb2yggA0bfymfl-Ou0egKlJRa4tKpla3grUEJpjW13073ujH5xAow36MnxEWpSMo_ce6e_ImihvpETUgecgKg0S_nOTWfS0_s4aA1f9n-OeqhYra-n1qHsw_KQ26Dw2d_eYZgSv0P0jDraOBdHr__ZA5ozDTN8rox4DvGplpdUMdTF97DjJGEqE1Oq4n3y_qN-b_FXm7A8cNja6sH6olB1oRqHkyCb22w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3DDjAYYEpC9ny9_vRTSpQxttj4DRBJbfLipNvt5kDi39vOka3oW8IPYPpscBsPD00m0qKo3g1A1bCizWD3VmXVzIlhnsvpM9emufa4qgbOsXKXkFEgQhTbVZfyMsufgI6R8c3uCvf4W219MJn3h7GqtIRBtWl8ufboCcZzFj3EhfiTg2KA4U6VHHI6ZH7tmFw9qVDufBcozFbR2qvltycXI8JWhp9tHz9ypvgYE-HetqOpZQbbu1kFoIMO8Ug0Fn90IJ3Crm5nNKItCikM7wltnL_purk9z-miEMl9hdvThSOf5bTUVFCsXwt7gkp051OG1UvUCgHXmuCnESPOX9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAWmp9I6Rn6Zo7-wRK6O_ZQHHyXWaCiBgzyzcgWRIUxFlJm4GWQYtnZJPM0lhPnuhjrgEFZiC_6R8tcgQM20zOQxd_RY5aWzOH509hn8cbEIkJe_Qqa_eK1aVoL5qopJVuEkLEotz24iqLdoddQavX2fHpo878xf8WmrwnG_ERyU6BIoDb-aqtRAUp5alUbC_G8U-2RL3_dGC8_wH4lvDuNccr6NMlFVDC8kTwZztY9tcDb_qHMQU95qQykahwxpczis1SLtow-Z8yKI_BwSc-DrISLmgaVIvclinDGNUzlmihZC1GGlsN_Xu1mUor-cxpr9FXM3yirW-aYk8LvbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsmHShujpr9SdTWcQQgXoFjxwAwqRWbLf_cf6IHXldcMZtYftoJXrrD-Zoxj6yCj_n3-KyfUir3bTxdu1vOwetAH_QphW4rJfeWI0Hae52jcuSIU9L9T2vQ1tkvjdY5o_6ry17cbzfWPrtjOa9Z8ygCjAy4navZdKQ8vx2mMOuQCXmdySw8QXWOx4MXq9y_1mPIj4qJOFAvC_ToYweyPz9FkHGSmteov6PxykgEtQds6Ay5w_-ln2r0ZbrAT8xZm2ss5jsv77sXyW8hiMF0MJ4K8d3BgJ-mTg5yPrhv2Y82Ir7teq0XEQoQb0ZnlyDHEfzY4VEzu9KK853iDnFBFow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLXtXB-BZQKEKD1qEcjIjVlOYg-72TLVjARhVRFA2xhCk1TL5YNF9c7tZHqIcXQvykgzwfsKUyypScGeuVB7SnIdqEC93VQ8RJnWgu5TIpavvI2EC91kpZhrD7f3BPA-4q67neGTPep43m2udA6dtjGBnpmP9ItnLfLA1bimbz-f_dcA_KFe0wNrYWRxXOOlZaWZQ2Mrq3ML6JPbK7JTJ4dCk4m0F5fqbucGHioPl03NG58s2rpEid2rTw7Iv85OHFs-IzrEp9PlHZPvxcq5WDHOb4IoIyQN8OOkB_U-w0nSUpu-LKMrZQvruBTYRTwc9yU_-UqJ7xfsjl_udfKCJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI1QS6SCplC82u3ZoSpsU-1WdUiDKVJLdLqQcBlXAfhqbU2SnBSKiKA1NDzL8A9daK8JjY_j2Kb96E0nF-Ce4XgDni4eQWjSV2wZhPXMCRYciWriosfNhy_36hxIhbS3QnLDMvleNyPx_UUK-hQa9YASu0ew8ulp8IHYy-zVnOu5AR7UJXSH4KSzhS0VUSjIxfjK0hLrdPjRs6_z3WFjfgTRsmmTYk4xBvMnpOJS5SvMXjxUh3KnRtbBlLL0Jem6IVchSBBIYfLTv0brHl3yJqno1vruESQGgG0cthulEIGaEaJv75yV8h26IiW0XLKMk-Zf3sAaGFAM6B7VWvCawQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy3MzA2Gq1U-NwRNEaN-Epn6TSsidxDsKFgrIZeA_iuM7ZexWAfzBeKXGUvsbqOe1czQrBmWCZMTnnSbrelc7MMP0hjVB9kGQ53yjO0DH_BWw1VA5pj3ndt80DkZMS0NXSKX9m4DFL2YwZPAIH7_jt4_nrBRnTj3dZgTm4ctNbkhxaqf_WYIWEnIgoeIztiPalvUkKow9EUddLc5i4VD3hjNlkLtd3fRxMwcvChqDJA2gchwPezGLqMaVjY8qh5nqkKvvdG8Ndz5kSAv1pmJkielvMOHuOplEY1kvyvJRmHKGXIdYj7LLlIoKe7GIlzsvdlnpPPAMEbMam6kziilvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7xh-NiK-4yiZX17ynSjqSfvYQfDQokEbvXslbC1w4IUZPTAyiidtEQFIYtfqIA6Yr1sbe7fwC26czDkFiKBalL5r1rPw1zhVr35IPiZQn5BwVJw6kFXDBG7Vi4SKnO05ikeVvCTvQNOuSy1RzUCInJwthnQLDVd-y0AGCM-RSie5ZYbFjQpGorT1iCQtf1BLtWeg-GkDulKKVLIxdZ_fE2CXKdRuBDsmrvtCjVvuFDkkglAO9o9-mDSnhY2Rizx1KznwV-awpUmjNhhIB2fKWARw_kWRrnXpmOWoTIN2JIgKYyfrmPISlqrOGzFRORUQDGaDrbrWYrykwnXSmPTTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iziR3Kc5Pu5luJTtgumPEIc9kEasiQKVBdJ518eT-r9IzNIS4Ar-7kozkIPbG4y6t7w3JDJxSnr7BQp-URaAdaeYAvy52QEF24Yt9bLnlWv4BNIJxcbq3whKlZoo1cGE35UbkeQseEBhT4dIdNI6ynqvU2NpYN6evO6z2ntTQVUbF44BFS3gD6PlwuPubH5E6Kb5zvTAl1RJPQOyTVGU2qPqAWSwgJq9nX4GgRvsur-xk5sxtRt7JqIKZXzakVzx6FzS4adzvURrhevl92m5MPvosRfp_NDQD20LLgvNIezgrZ5XuH_oDN33Wf6CBXh56pDpIZAb-jcdo0QGns2vGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGYjrbwd3zj2-WUAFx9Uk7Vs4JQGGVKSLyXUvt0l4kD8Q7kroDAG58m0KPI3YQsMdP7Sa55oA3rQBwK9EQ945zas8e3yla9CtN5GaJcJd4b0qcD128J5nhi_bRD4klOIQ3WDOSMfsWLiPR1IZZPIeOyj_hVfhSBC-MMtDafQEacuko87NRnxavq250wuVLtorc0u4dueyDBVr8ClZ9f6l6T7c8W0HYHQtv7Ew4PoKdg5JbE1Ct-7_muG5MxIT8_5iagJVVUsajP3a_zY6WCksL4v216woQkUDJ8sbh341aOVbdDhARb-Z7HqYmR4D15TXIzsgriKlxPvOAwRj8xkLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VslamzJEkHW6jzQ2xpI3l3dqoHoBj5Ob1cGz-NKb2vrEO9ZVx0XrKgBA-3EaFz4K1YZ8p-EVXj6PkQ1Jqroghor5c93Y01bXfIQEDrV3-gpDYM8SGtdMZENS-B-Ux_VMnwbEEXjzRqzDEeG7kgeq8GeNTzyoy7DCJ7AtvPyQUNYQ_Y739v1kMT9-eMGkvsbYiuboPFHg-T4HwFSaK_dNNypUN1qi5sA5kAZoCJgGNhDpQE7KyKNQ93uTAvtu201eJhE_jPdohhplWIG8CGe7NOSNcvLlGP7ZpfRKzsflLovf8I3GtoQjTCKiiZRSrOaiKeh38_bQbssIkiFtYMNTQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twgNQAwEtUV4zrpd2Ty3rmPrfGu3FUBgbhibGCYW3kozMhZElRBrd_JP3gsUVCirjhY17qLwn2i0BKCRdS-IlpCHPvZceZr3oFYzF21HhkzyFSnZEdN5krRwQbxDIX2S62gBtvUSHZnHesjdGpTovpCkzuHBwyvB6acxk_5OqvvWn4Y5A1zHFTE2XB8SQK6tpdL72SHnSik58-IBunpekofAFL-I8fkCzflfOsFYlgZmS78JeNV63HJvke1II0yB3EfefIuXXQ9Bng7zZKvXX2wNGF0LEXUtOfFlt7hPa-8F0yuZI34oOtU1UJLBQjG9HpAED_f6wCJT4IKeVszSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HowgwPgmqocb4Xdh3fBfk8RsCdhmVcIqs9P0-5-Av-RcQwcEHuEic5tOheYXAmzD5ryGryyyeKBoBM4yZ7J1Jo9TqMT9WTeJt3ljxGwPGhq94UU-v03RDAgPOILeijzZcjbVjhsjMsg5gtnaAYspzl7nh6GzSmIOBi-0sr_gQZ-2GxxWKR7XJsrO8fS8MJoFVfXlUDTG_olrcwjCuRhAbjrPqw0nFTB85bArtzLkbKaYzYaTUVj_tV_Qn92BAmgWSOp7iCveUeYVP-SJAik6YTOC3_4Ds6RlwxHiQD_D306oEpZPTP9DAToYe0cp_Kk83JyRD0-k7wAeN_GJX-tVSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJNI4-I6LP4pLBwYt9ifaEmmdTUQe8oIbocMpSRjZD7BzQzTegO5t90zP7MLjGJzfVOd-4_Cl3jXIXsSJEyNnkDk-K8XFc_0mLK-CTdpbYdOWQ4eDTYcdC7wc1Ru95xr66HkEKXK0BREj54dzFWd5Ef6OvySdjKK92DOVUMoX3Shs1KVz8SN9OPX6tYVbVDlUHqf-KvGQwNuTvWxFHTvcfxIHh04VXHM-YAoECgTxwZTwhsVRPYojCP0aW54QgLieYW_vQKVw1AtMlxYEJUj7qrZzvNVdJdyjTxEgM5ZFWxvqqKxuSCYPcy5wwgpUoDf0maSseVFBgkaRZ60Ih6-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=KYZfBkTjHCV-sKsjIuP1ayx14Tkqm9Heg1Wd_6-J4m2rNB1zi-KFyfNmggMuHLhv1oqT3dLYJAl4h106pzoTvTx20KqvMWwRVbleXQjmE_IoiEGYSiD0rDYuuM43S3yFMD06-bTkCo8eec9jMFsiZBdwKlXcFgKwxosH3Y9ctdDnSHIxbYBGHg1ONgYAa7gyPvSdENXY03ZvhHfDC8or85vcHTIETtQwyeCXqYs_hq5_NG5lXDHslwyy6HEuCCzwQk4uY5l097zLwXnIvc490PGr-HpJYQ34nabq4brIFOWut5TgFUvzSoUi4EdMJ94HiXZEI6q0kqDyeUNbOl0Beg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=KYZfBkTjHCV-sKsjIuP1ayx14Tkqm9Heg1Wd_6-J4m2rNB1zi-KFyfNmggMuHLhv1oqT3dLYJAl4h106pzoTvTx20KqvMWwRVbleXQjmE_IoiEGYSiD0rDYuuM43S3yFMD06-bTkCo8eec9jMFsiZBdwKlXcFgKwxosH3Y9ctdDnSHIxbYBGHg1ONgYAa7gyPvSdENXY03ZvhHfDC8or85vcHTIETtQwyeCXqYs_hq5_NG5lXDHslwyy6HEuCCzwQk4uY5l097zLwXnIvc490PGr-HpJYQ34nabq4brIFOWut5TgFUvzSoUi4EdMJ94HiXZEI6q0kqDyeUNbOl0Beg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT2LfJPEzWw3syVM1tBZRy_iQYUzdE5CkaLOaT1yO2thvOsNA3V9JMoxVWYwl5EyygzXBXRvqp-OLa06BnC9kLnM42uuz-cZZbWyReJA9ZY_rVR_wtPSASMVHzlZUeVcvxXgq8v_wbm6SVMdIe4RgFQwwhQIhoukmnTi2KbWuQX0qkCwPq_SasAJyLvlOUwYs-hVkkr7GY8HeV6oYEeM6-V8XENX8OXEP1bYFR3H7bzs5w_lltox3uZ_wnGyCwSvbQOt948p9q5SzaQn1TqYNz4V6CQSEbBaAvx4bmFx9YSyxLvJcj4NAc_2bfVynaYqqPMebgFDDAQRs-nSDSrKnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH90NqvD4gguKM7h8tOKvL7meRBQI4-3lDf6DwCOOQ0N6o1NNW0RFb5n6Etui3bcXWX2FaA1BHDmhkP9-NrcFzI_a2Y4ofzVUhP2rfd8hQtsDM8ZyolrPN94vfyDTltt4d_U0iSxeb6kbT34smCKkWe3LVyq0kG9Tl8g3L_439L1ZNo0lZgA-rl8UWiVVHm8Ak4XCX8XGk0i338KOD9CpzmLkruZ9Vgob46BJP8G1jOguSUrIYRGJju9ohlbXjRet5MducUgybbDB23hRlDG5cXhY6x6IpcK9svLcVMVaryH3OXMvAq1XqFcm-Djrr_rK1AiGUmOp6qJXiQvyLC8dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=mD6XfKxDrF959vzEh5aShnyo1XNKVlkyJeF08pta4LSzrrxAbV5L7-b3Yj6-A2ardObJvT5BdAtsqWQMGcwDIzEI447ezuM3stCBb8UUGWaJJJypJi2uWq1UonXOCnEme_fEO5NAqeihGbc3vlQFCDqq_4W7F74L1rH9jnCdvYsFxEkfv9_eluOl9MnGH9rrVcDbVdr-5gMeCb36Dz-f5IUDFEZn1PuMQBJHs7o2QJ8GrGP3Z1zJhg3l6_1HApfTtoU7cOsHbDu8obk2eSp2co5kN8_fGPcMTJI3ihfFQitguohAKcIR_6d8MKFWoIOoRJY8re9azPjmVHtC1js1BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=mD6XfKxDrF959vzEh5aShnyo1XNKVlkyJeF08pta4LSzrrxAbV5L7-b3Yj6-A2ardObJvT5BdAtsqWQMGcwDIzEI447ezuM3stCBb8UUGWaJJJypJi2uWq1UonXOCnEme_fEO5NAqeihGbc3vlQFCDqq_4W7F74L1rH9jnCdvYsFxEkfv9_eluOl9MnGH9rrVcDbVdr-5gMeCb36Dz-f5IUDFEZn1PuMQBJHs7o2QJ8GrGP3Z1zJhg3l6_1HApfTtoU7cOsHbDu8obk2eSp2co5kN8_fGPcMTJI3ihfFQitguohAKcIR_6d8MKFWoIOoRJY8re9azPjmVHtC1js1BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=gSrb1I9im-vgEq1HhjE3aMhxBH3vSkGZw6s5gZ0-IUYKnZBHC9vqqucRdK9g_MDwS2gk7qcn2KmcgWD8FfR7Rz_G2Mk-Rh5VPrnhdOJgMuX6_1TyjZVq7M9n8enc8Si5b6f_aJSOhRGED1f24hhpZpSDUFbp6THBXqtugsHYJcdHX4XlpiTHl5NKRQErOWSFGzqfswTEbwBdVi7ojwnEIQItbroE20eXiyhoIpduyMrnUY1wkn9LsB_4KWKvlWGyROBKJhR_pbUS6oWh6XvqUuwge0pZ4TFkiztBIi-9aENqIyS9vQVVppkS7hQPbp8j7XIdYUKUwDujTbAypbmubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=gSrb1I9im-vgEq1HhjE3aMhxBH3vSkGZw6s5gZ0-IUYKnZBHC9vqqucRdK9g_MDwS2gk7qcn2KmcgWD8FfR7Rz_G2Mk-Rh5VPrnhdOJgMuX6_1TyjZVq7M9n8enc8Si5b6f_aJSOhRGED1f24hhpZpSDUFbp6THBXqtugsHYJcdHX4XlpiTHl5NKRQErOWSFGzqfswTEbwBdVi7ojwnEIQItbroE20eXiyhoIpduyMrnUY1wkn9LsB_4KWKvlWGyROBKJhR_pbUS6oWh6XvqUuwge0pZ4TFkiztBIi-9aENqIyS9vQVVppkS7hQPbp8j7XIdYUKUwDujTbAypbmubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=c-YW-eIYOFttcGSjvQ-jhLVEbdzfE7GlI91nmcrqz4g9HYELBny4iDHDR7T7BvJJ9etYepI57KD2hofp3YMLKkS2cY3ljPiRE6IB4olmFJ-LmDtPGcZ8fF8kuxezP9mnBdKCLU6ZySkC81A_7xCRyZQpln0C-e0bCQ3RnAJIIAPHMrxKE6c1TOcNwYo28BKQ9zcWM_2s3rHILZZRDXY2AyfpPYZnWba_LvKrn-CEml97BrQeOwa_so501peMmNM-RuYvQJD3-MWGbutuUbOQ2SYM44NydhqgtNAY82nTKSf06ZMKOyaTeueWX_4l83CUAIZXBFkwCiUJboacVvBrVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=c-YW-eIYOFttcGSjvQ-jhLVEbdzfE7GlI91nmcrqz4g9HYELBny4iDHDR7T7BvJJ9etYepI57KD2hofp3YMLKkS2cY3ljPiRE6IB4olmFJ-LmDtPGcZ8fF8kuxezP9mnBdKCLU6ZySkC81A_7xCRyZQpln0C-e0bCQ3RnAJIIAPHMrxKE6c1TOcNwYo28BKQ9zcWM_2s3rHILZZRDXY2AyfpPYZnWba_LvKrn-CEml97BrQeOwa_so501peMmNM-RuYvQJD3-MWGbutuUbOQ2SYM44NydhqgtNAY82nTKSf06ZMKOyaTeueWX_4l83CUAIZXBFkwCiUJboacVvBrVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX5OAZRxGxdO_0Ww3dXsHJ9gGjCAqFhph5vQxh7BdcjmTHRiKWybgRBU9ZUBqtzjp733JPCqh9jB02vGoFc8KlsHFAfVH3gpIg5syEjJ4ppNvktUhjfC-bAnvIcOXJY3EcKG4p_sNi3Vr8ms614rOz5kdzp0MU8mfSChlmYX5BU1Tz2jEg6SqivgWrekKf_IS25zaf_qa-uruNwaY3X2y8pLTMiWEUMExwzXXrNKX7ANkMusX7L35qYGOQSsFdiR9HcmjHghwzwn3MGmngUt_rkt4MkuDm2_bz6O4iv6be8oyS7-8ZTQl68lKKKbl8MC-w8TZ9C0AGBdb7jpb12r4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=U8n3YD6RJchkUkhAmnSN9l1n1HcON88L4KZwaSGo9c9jFxaHqMzeTZ-O3SjO8PVTQSk2LFTmjb6QiSwrPsOxkZBVucxxKXLF_7c_ZfeqrGPm1TKp26w51EABKvdw_25_6IxuzBHrmZt4UxmoPXRizybSG3U711Iuf0rTuxIzFkAXeg_ZEa_tMPqcZLPCcwILpNIVfGveMWIUA8m4BSM3j0-AGKl4H9YC5ylzEvirAMPPcGorltSZLIOwTOHEKhp_lkOfQyigVMIGksKnq8_aMcrp7oMrHs69T7Qoy47yfQ0MSJ3lYZdrt5HMn8oWbIcr3gAVoRrJ-AKN1Wetrde3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=U8n3YD6RJchkUkhAmnSN9l1n1HcON88L4KZwaSGo9c9jFxaHqMzeTZ-O3SjO8PVTQSk2LFTmjb6QiSwrPsOxkZBVucxxKXLF_7c_ZfeqrGPm1TKp26w51EABKvdw_25_6IxuzBHrmZt4UxmoPXRizybSG3U711Iuf0rTuxIzFkAXeg_ZEa_tMPqcZLPCcwILpNIVfGveMWIUA8m4BSM3j0-AGKl4H9YC5ylzEvirAMPPcGorltSZLIOwTOHEKhp_lkOfQyigVMIGksKnq8_aMcrp7oMrHs69T7Qoy47yfQ0MSJ3lYZdrt5HMn8oWbIcr3gAVoRrJ-AKN1Wetrde3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0uAX2ZF8EkooH7GvQprFmGm2eJcTEjSeFZbsWIRKjFAbf3C2RPALDuJU8hxHH7StDxfdS73KSD1WSskd7GV0cOqFhpDQB9BQWrwduBwf6WeL1mnwpsEnFzeocoI8gIMQ8TVr1I2S6K0jvYYcwHxAkf4v24B8vkbnpkGvtqg-uQF2GGDhJF4ApJB-iXBBHrdIupD5q2iYNBxlkvJ-RdQXLTUrlkRV4KN4C7o6UDvCwFDbtqsOFJfcjSeGfeurHbr6vcKw5CAAz_L0QUw_zXoXajxMz0AkN598M6sf5LX2EgKc4wE05FfX8f4zVk7pxDy-xcLbTLk1vuEm1vQwS2cHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miamoVqsHIcMQtQdxe73hzJuziKKNYcyLQ3LSKPnratSakxE9b745S8o5Fl0HitXuYakHhRXfHL7-w9BgYGvgUdqbIxQp_QbMUknL_OSYjytNvWyTIDK70h4QLP1oh-XHhRmSHWJgetT8X351Yvlqa8pveUldfTvDFQc8aFt6fzDAFYb3NAaKnVCB7ks5h9YGzJLfGDsaHD2Z9VjjgIXyZVBVaxyv07tSoSEh2y9Cd-bLnMokoy1b1D2SiuUwzvGVMBteB7g4HGvS-H8LMrTUOgEKObT8NO8pvuHCNI0JP3X0hJA-OL8kJ6yU3-kLU8QkKe0vcjrEeP42qKLIdtzWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl9LA7Ih5HF2YTQ52Bj3fAR4P_8u0Db3-ucvRfi7dyG_9snRnEWnEMs_L-C5k-Vkc-pf5xFR2C4cQB1xsQIuWuGQ5jlHOWlrZZ9W-MQRVq459eOiMsK3TwgyaS9bc4TWsNkfTuRMG0WppFJ3z6hysbZ6aoByjlJTeqrCSPu9ph9cqkGE6M8Q1tDVgVUcQ1eV4CwP5f3DIFx-LSJBmDiRoCbtZqTauhd32nK69UCLxkMuaSTgtJyixGUC5RC-xakZwXJb_8gNhKvv9p14Jglt7e44Y-_tuFNDOgNT2OCf4jpjRwOi3-fdlko9MS7ikQcShQf6rx0OAAbMYR2MNNwzbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU-a_sWuT3Hg48lfYESWIFJUg0Zv96EiEUNNiZmFU1k7xSMtB_Pqu776MjGo7cmxE7RE-_323MiiFKpdfAwP7whfjikDz_Bn01_ww4ijyZNCzPxv1lnlXKIDn1dxz5EsFyLAVhge9HmXaSvbskgBP46PVhsIdXrgX69IQxtyrAlubIh2WM-69WaW6g1vE_BwL2a0I9wHKKmsQM0uKb2Cvth3ml0BEfB2bbHype1rtdWWDE2oX-TMQl7Tt_j7V75tnRrd6dLGGcRdfM37PGeoDmm2Zd_fYOMQAmHLZkiTHeEczxNRQvHZHj8z0gXTsblABexSvHcmkmazT6ATApe4AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_bAg-EjT77L1mQSKvLu5fWuiOBGxLOhn0xTkHraGIarqBvOHZAGWfakMCJOF-MgnwRnAKasSOk1vm0xLlAHZVk-OoAOk8QvOhyd4d32JHG6IDZ0dF9mfbqwTaJcAkvMOCiB5lAbxRqNuRPk8AVf9u2-c0c7uSPUS8c6O5vhdsEltxOdYk6lqUjtp5kBq2R5c-uXuXTy3PxUFUTesOFz7b8MTz-2LmOFXRnxtp3wI2xVaz0UwKrvFWrD8yZhH0RYFSy7VOphWk7_s1ONCehq43AIuyEyAih_wkhzd6KzPSVsBLdTV5NXHSqWUxnZLvZjE_hgR_hufkhiiUHdJQzfLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf5fBQWFwzGcR0PRNFlrtnb4GNQ3wGVcG-3qI_7orraVjaT900kgs5nik7A0xI2YErCJgA8q03Nm9336BQMwtfPW7lqSigLUKIaUl228WKXUQwNYgj5BpAbqALRA43mxb-ttLtd51QVfDobkJ7CyIDY-dweggnYIK4mZVsZCW_xkbF0QGjujFgHwItp9I9Ax9arf6C_OL4woWNAZJ7N-ikbOd4v8kk_7RKhn4hvDusBFMDUh__2dPXewmRyxzQP1T99xpgSdz2bDpjiLo5WGndSPda6j1NLXXz5Y3DbTnlVhT2Gdfo9AupyFFhG-gPYtveNrljOa5UW5lgyVq2zUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMhJBrFZWE6zmJoDznEBAErEunOpd-LUXYiHEhhDiTtznAFFgLDraSTn0z-XXBCzxEZgzTMOLfE-GEPF7K04232e4HZ5FBmVedLiXng7GAzcCD6p8bnsz-GEHBnnPmcXCiLiiwzqUbndLZpCihiYqNWIgat_x_hIyO83Ytv9oAA-BSyGai3iDyeJqfX4Dnvv6u2-ixycdIEKE16v2eFs4kmoSpLutEAH6RU2reKb1nqgUPjPubLiIH4kq_8KeSkslv0GndgZlbkxl4ZHe_-41mXs5lo0g1LHDGpFExWg31hU9ZZMwZwiEBuQSo96Z9ZlyanxllvheTFYnJWpG0KWDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OImq8_QN8o4rHmJYOTEmj8QJJBgMYccc5gQzvNrLLLxXvBl8ENZni0ZyQoGHEbX59LaPI702iweNY81rzzPg6QWyTd0pwyD_7SN4ccSPexuuCwj9ZO7HNwG0iVeC8TU6DvS6W8ZAM1WeGF7anJR7MJf-wL31GzyA2psDRHfU-VxGjFdZ-8PlpvGzo9j-d4fVqxVecWpVscFg3NjImhlNntOoGQdZKAe5lXeODeWch7bF9Pfs71zZCq7vZgVATtPtGkm0W2o-LnHdHKTPWovuRATUKKW0mwCyKEuRgvoiG7ZdDYMxQLRX2g2LkV6aBVt24nPz0x4JkyrPVf2amsaB0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2k9neeWUzU8Qtb_nR1otA3eaInQ981TQKhUbuCccHDDFYeybG9INzppumsoI03ITfyQyNP3jp2nEoYqKRBk1PvYxwHEvsLrSjbd2Oq7nsV-JIWtbYhppOEa8C-ZADUOEmLtdhNuaasnC0GlxLjESAcoXkXJU5sBGQ9vwe9HW_ZSTenVEfJp2PpPyvfHuBvhHXrw60NSTk3hPNc5ahQfZqqQFRzoO3WgvdIeTEpedrGqRmT45rk9M4kGu98BTgmZJ_GNiJPkRXmQ2gNCpkUsNywuTrkCo-zsNMsCP9UwV2nOVRTWHE5pwpXNTJac-WprqUyntKMkCYW7aYrroe9lGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtLv0wAkFNpA7G2SZfQI_sqB9QJ7-cN7rWq3mc76o-qed1MtQm8u12dp1ikDFYylc-dA2Ba4IXdSElXrYqtyDJT4bNq2QxaSTY0Fk0fdE0BoCvazAywhfg-WXkBP9HMHNc--6u8h9UTrmnGzsZzHxr10e1o_JVrtLOh4ZQQjtF7fuQ8Sp6xUdt9FaM1DYKEoFLRLUdUpwvzjCJjgYLfuyV-o_WZMPzs30e7I4Hezad2c0EYnT3gJfYXSNNba8egWIH9hBFiqNIJyvqPfh4DxWrjKFZXt4ndjrsqxmASQUasaVaE-7bmcgNptFmIdeSUTHGsh5zVutPGD0P6_6c0NXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRPIbLQw4YJlamQKTHpMjFS3pRPE7qKYRVIJwcOfjM5sxwfzUq78mKqXDZPOy9Y0BWfj8lPJqBGSiV-mZelJenpFOGONn7B7qfo6nEPC0hvVMrgavpxqbdHTpJ9XAbNWDnCSsZFngDxutLx5t00uOln-aNU2XbmO03VJFqZVuitf2u8IGmB2YEpeOiZ3T2qZN8cpIkAmjG3eE4FnhRK26Gvq0R5Ntu6XanCP3xNFzuXS1YAOBQtic96XiIp6fNGS2I1bmKqWcWKlCsnCMeM7w3ioN267R3rTE2bAFMUUdrVL1lydtSNndG4h2esN6sW9JEg9993c6Msk9SYOVWWyVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXkI2QU2FQH24eVGA6dR7x0aEglduq7zerjfJu2gNC9Ol-RpP1r30nBSaWt3wHvdjGW5CrLSUQCIRVaYRMrjP1k36ycVmwNPpEPyWlU1nCXHbm8fmzD2D5uU1ESXkFd4m3nZ1qUNbDl11zOCgqGsgD4LFvz3iQCd5Fp-QhkcZ2AckfjusW1Y1_9rzPXSoHwc18w1J_nWc5rwjb6VoDswyDVBFMSsA5k_zY6s7p_klgFEFOl6J4PMsuDq8CoZpUpeTgQGz9Ute_HN4E9E6PmUX1zkS0iCv2tc0EpDDmJ9VUP41pecUZdeSScoGOQrJQO7SzgO6j3ZKQou13LgABogQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMt-aUtO5tD8KUPZbvn3CwCfxHk77HPm1P9tmGNQ1quCHqBXo_JWIR5hTOg4t1pzHixer02thZEdZSA8a94oCTMEFYFdJIbPiga72sjiu57VqvUPqXerK5Rd-tv3_-huJWR9kmcmtdq5DjkXFG_v_DIEe_tIVkNAUJAkKs6uWfN17wN3vVQcW1j2Tlf6lhAbtKU-rYqFKKFsXeoyf_CQGszvhgDfgNCD-LZFSIyBx8VpgS4w8Hx9n4GHiUeWWFu_KQ0_Oqx8EUUQdRf9F9-ju5vcZC6Y8dzbERtH4-Uywy9mlYbN3We3Man0p2OMXxbmKhout3zKZJ31uRkcAYP3nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX5Wx-p5t0JHeukwIJXimhrb8Yz48WSS74ClKTV7BtLHRgUHLwT1Eb64NsgWk5DsU0pDWdaGLNmjvLcLrxpYc2EbHK32r5HOXlh_eoShhmqp6wlZNU4MdxS25hNjSRlTUQ-80NJ0kKsDovPpdCYwZsqcOwC8JGhYvPVcVeKGoUjduy7TQ34cRSBdvbjSvoPJD9DCX6ucuDIyxFalHXsaTd7esR6Fwr8ekZ2U194DgBIDLjNbU_dCe0svZXh_I6V8qpiVtkOHoSL46Uj2srgUYQN_XGkZea0fP3_FwyF4CRycStwZvBrC04S85rtDpwgNTsg5Nw6W21milHRA-PQg_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKYGjCHHuLhuVFXT1SqkH8wJGaAXIrydeNl3yR_5JIy26xGf3x58-agbMliqwH-HwvgN0gU5pmEm23_tQnND9RNbA3ME1cndUG9EUKkylCY9MJf-N5bsNx8Sp3KbdX5ivKG8fJLFKBrtAeapfMLQdqHLBoM0iBBGHCkU4L2Ujf4ad0Lqu4tPvtekX6fgPxEICyFSXoopkAsmGiXPoIITX-YsWklm-MFxtk2xDiMTG226-27hBLKW-nDhxW7KupqNt-8pN5pqyTV089NtjHP8PPAS0qxWdncvJWa_FI1q7WqDjaAZOjoWTXOPZ9fTJggf8d9epLxA__ie5m16XwHITQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3wfv5QmwBemnZWIX1x6bPpv5VxEfgZuCB0JIuPT7YXtRSEdeULJM7-Vto_Wgtq2igq3d5b2M4PgMfqTuVss2-UYmtL4mJDr5eA74hnYrtMMAg6KWHp2GS9FzPoW0r9vyzr3cmKLl1oFgIMiNYNX3iSV9lEEtGo-UhASc30xfMa8hBuDSEPSfjYM5RnggKPfFI-n1PUn_Cba6qbwL7Eg8GIAbNZEMAkuHGi6I-PRXJ4BctPz6jx33zYQUbT9hY2KvoDw7nQjBPoS0TOGkOe0YgGQvHEFmT0j5UDhVgBPWxmGMH75QI0LUrvA7x59VE6PsMU9488WjqBQs5TrmoAsXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=CLtJaAMNjx9oGvaYMSo8Q269F9wFXDFci89qPmDf9QVRKKsWmI1JDjn3RXXwfewGmEaDUl9u9Y3FjyVx1-QS_Jjt4fJ9hKI6s6Iix2j_CJ3U0ktW8QX5e_Ls05zYnfgvS_f9N1Kb_7axmx-3sbPvlUmcfOKyPcgUo094eXiTYxZEvLEjqCt33_MfO76LWFuMADlnCxzPiAdYI_ls1PNqHefDCBVCMRMVmW-RbT_rQ2uBTlTBSJ2GEsjnvxEiSXZqUqAyaDhF0E9bJO0i-CiA4hHtAzAoRODk_Gp0O5jb7hrJq982j41o57BZi_ZjWGlAvyyl19UYYeA1BeDqS4-0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=CLtJaAMNjx9oGvaYMSo8Q269F9wFXDFci89qPmDf9QVRKKsWmI1JDjn3RXXwfewGmEaDUl9u9Y3FjyVx1-QS_Jjt4fJ9hKI6s6Iix2j_CJ3U0ktW8QX5e_Ls05zYnfgvS_f9N1Kb_7axmx-3sbPvlUmcfOKyPcgUo094eXiTYxZEvLEjqCt33_MfO76LWFuMADlnCxzPiAdYI_ls1PNqHefDCBVCMRMVmW-RbT_rQ2uBTlTBSJ2GEsjnvxEiSXZqUqAyaDhF0E9bJO0i-CiA4hHtAzAoRODk_Gp0O5jb7hrJq982j41o57BZi_ZjWGlAvyyl19UYYeA1BeDqS4-0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyzkzVmyTL8qAKX40BeGGC85tO1e-MQMDakpkIHwxQ0fc-oVBkMbpoLeV94O1uFjCPcd-tFFJoX5rx7S0Een8KWEJIEv6L-kT8ImyOdBrngSWKwSbyD0dzoi-K_x6s-lwBhLR3Vxx-G-wfn0Y8pdN6L8yKYCGdzjSKBo6RZtM1PwaHccTvJg2AJO8H9Qrql3Cd-xHGYnR2YbY78bOwmo5QMdw3jlkd5RiEXHrkDgS4vW8jMMAEVQEZEfX2icJMVZkeqfNqkiewx7-qSh53za3JB-oFx5-kFeQdjC9JmZPfIXrcoZOTKIunmZM5mJjF7swlBSlzV7fspxAUctGb6L2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Qzri6uYkBQtZ9jkMSU79_AMCsXf-sQJz_cD842RiLMjiI2Y_VXBBRT8ERbiEt0u3yuq0PLoxxPrNILdQZusmTAEYOjGKo5XYeTPEp312StnRlWFpxKBcOMphSu8j7MKp87qCZdtdjKGbELQUIQVSYrktcllTT7XKB7Q58T5BHMRiKBKBrPVUZ4FWdBm9bN_T_u_omaAQNPyqoAtzBhwbamq_REIQFpMOsOnXfGFJnHOFLmKtO0A4BiZEYC35gGed3Dxa2wwW1bk3yf462oxCTtynbC-hDTa_GquSQycWsrRZxmxgieDnyAmHOc4M_lTDO4MRL6nXtZ2g0Itjoo5fqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Qzri6uYkBQtZ9jkMSU79_AMCsXf-sQJz_cD842RiLMjiI2Y_VXBBRT8ERbiEt0u3yuq0PLoxxPrNILdQZusmTAEYOjGKo5XYeTPEp312StnRlWFpxKBcOMphSu8j7MKp87qCZdtdjKGbELQUIQVSYrktcllTT7XKB7Q58T5BHMRiKBKBrPVUZ4FWdBm9bN_T_u_omaAQNPyqoAtzBhwbamq_REIQFpMOsOnXfGFJnHOFLmKtO0A4BiZEYC35gGed3Dxa2wwW1bk3yf462oxCTtynbC-hDTa_GquSQycWsrRZxmxgieDnyAmHOc4M_lTDO4MRL6nXtZ2g0Itjoo5fqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7Poh-JhnNPpExMnniF-Kg62dTq7E-ZonpncI2a_2ZGngI-MQJmfs18ohzFlS72U72j07xH3XzJgl_r2pWnc6ywdgVK0BVheq5o4W647DdWkziaK2uGa3ulvEpIIEp8hoA6eiZ3Fa5WthxDsBRMxApVGZPNWqypCzRzZVRmUxGQy2ZhWwGMxdo1XKoZDar2SD9x5T-toRFQMH-EPtyyjvr3DwqGgzXWa8ZSy7Ocbtyuif6_HgUJfD6nMFchpFIYw19nPKjPJyUHs4I6projmUYH-FMN9krWqG3zyqAOMqHsYv9ksIGxyRcnRsDEG14k_FDG19tIXlVD97o26GApI5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH9L9rRRsqx-BiwZTNBCM_TOjPGlZVQi2iXl2rqLUbnTl1lp3glHvqRGhuJ56BUPpnzg__o--VZK3_BnPlGlVCRdKr4bkqsyBSUNAghIH8XcgPN2GFLmXR0pgT1WOPmOSlrhOwvLTB8ifGgp3aA4_1pD5qt1v2M00B1nR0S7fe4LxopbLLp6ygXnsD9lApOeDQIn9wkSlc3kTgNLV-VCOuZj_0whakO3stfiNJ8sFCrMrF4cg17uXcagoZ08-vn-o7qI9gLEyfvRJ7qvxdV36bSXKE16vEX499345YgPCZY6UGV1OgZpX5SLNC1IIDzgoh381iqT9vcc0hcrLVBN5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcgVNT4woCl_51dc4KyxUjTVnqX-nKko6gq_saMqffV29RloPJTTRpqjpIkrk31IO1yiOpFLDqS7q4fXB_CDxFl-QuPmx9egAMcO08P2Fe16CnMF8zi2FHmmzaPA8P5y5iEdH_pIRrDOsShSel9hA9TeoXkbot21ECqiQO1lUQN6ooWeR9zKuA7RMGEuzEbEpIWN2b00KvF5J8ESDuzI6BR4oVJq_1VHcZ3_QTXiC6ZS7clhOJfSaJhT1ixDHvP6M_ZXkNv4e4Lp35FN6QtwcTX1Lz123nJP5L-aaVtb79ja5HjdAZqJT4hl1URvClZU-gOfVSdDr3TgOotZBcmZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvVkaLJ5kRBkC0CW9wsrbXSb-Pum_1f3TVaOXLcpEQQ-1rOlrcEWV5Je_pb9G2wag8gTYUHM9bHHpgaAmq4ycCnNk7oaIRNPXQEScIvB_Y9_E9gVpwX1CVroSfR5HiAxHV1QcJ1TAzqMHWZk5jbEZiiyKHAPTbmTojPZ33fAFBhP9YuICFysu62rKVIUQ0VlF2X-tHw5hgvG57nalBlwvm01SET4Xm35gVCPCTHHpJv34xzamrFIYwgWVrUY3m1_SXBQXnzLP3HfQZfNTm1mGXfLnfpjWcGP2TNkbX1P7X0eq-_9I5k6joUT8bg9VIVU5h9F_nngnvqipV5D32w5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2cpVifFwChanfH2l-W1bliqoW_zynjqH_C1ImOirTXVNx7rYLmj97Dk3EXyB4IbLOP8EWDAS4wK9Md05a560QmhCs63klAP_E8yzb-vllSUuBXqBygxHHCLZwm9aBOj37lJrRi4xIW4YE4M8n9wQNMO_sT6qMr7KB1_nPS4NOjPg4pmXxwX1voHvgvkIX8nwXh3PNNd3TPSEr7gxR6Fclli_8_27xgRI8SOem6CBFq3jZw1I5gPqIiP0Z7xIe7vNvGAxf8v6kKJ1W9AkU_xuRvct3C20rGxMSfzwGPqhL-dYWlD3QG_xhk0kAPMtTN8x0NYRwc-0xT2aNJGMNmu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ttq_ISljz_U74A9fOhX1VU1zCh6B7sdtcT7cZjVl4O_X62elJR45pBoMz-EvRdWKe4odF5qXEH5Weh96OuDAqYdsneRiARVUK0p36kcX39nbaGvnD6gLkVeP0sBTzl2PSGHIx1G31Stp44nTa8YzT4d0evGB0lSB5EN63bViscp6QiUR0g1_rCdQWEYIHsQbSJUZf25uQrX6ahDBMKCA_cQ_M3M4eXC_s6mfPHU9dLWrQZagNOXo0oEY3PxKzfilVPAXhtnfM-lgPVP5Xz3ztNpv1IQafOyRvO9RyFQbpNAS9OO-3-f1ybQn7xlaXzBDImjo_r_WUPMhUFqydJ_5Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
