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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4jT53VP1XFVUOUE4NaVjmaLGzif8EYZL7RzVXYU8W1Ks7zxj93roKV9VHb5nWfzmLfTcBfJzCUdC7I5lf_TJ9GXSWaO2ekufcEDPIIOH1kxi1lPdFz_cZk2VQNKbDm02CUrxw3VDGaIy4WUHoaH5maV9KOQSYhCsdfDcOTXiZma24wh5GkBjWnbXFJretRXdt-h3ATfQT8daMN_LLGr2NUUOn9wnflxbq2rNArKguKLoRp_0AodzkWO3xhnmr0nhAoRfa38ZGxQESeBqgeGzBkJeZ01bRXndfDJcvvDvruc0PCxr1ULHuIGgaEg4NkW7g4g-sqkM52hOnZsqXgGZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 556 · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoN4TjuNVTo8ZVLvs_2RhfbMLJNZfPyPtsN0ZmL3lGZDiLbL3XEO6pMWBszEgdYrak9fDxuEaKX_TW77IbpXM3iqu5rbI2uZl32SATKQBvg3faJAzZauHfMKD69jdVjEWNx5Pa_2Yew5WN-E8vJqohjxb22Plg5GNrzYYRnafTKe3umDHMxhdF0iLi78U3xygQfvA61uHu0hXOwDb_PluJ_eCXtl-2VkwO8KbiM2VlivubS4mQ_Vmwe7n_lQP5cvPba9k5qI5bcyHFwWs7BYqzirijhNEUhHttyG5nQpfNU2IndNibC_KWwanOEV6GeFhNK30tR9M6mWiVlxTTOPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSLcw10sLEeJSCa9bjZgByQ96FGfCJlsan_NaCnp2K81HvHfyzB6kk_pU2XVkLAKypLbXcWSr5nrOW2vCjBQCOxFeJpKCC54QvlHY4Ba6Wy-pkP4RVECW3mLmtagOtUySLMOe53wAIRKXPJTioqrbgiUIajewBijKre2HF4IRdM5ut79EB_QyQEac4kM0UDotB6253WJokH5HFvDkXhvtsm7idXPg_rr7slbb9WGjlbORw2L-htkDZiAAi98iDp2_HbDrVYa1q-PYVOjVkuGwgPjAvKdz5AHBRkzrOtPE7lig8Mhc6hNNcrqlba406NR5Mn84IoXRCSTiSRbs5Cl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pptx5QNr4onD8RVfgxvu3CurGpsUZE16TzN4ooukfjpaJCDIyvHBk8K1OVA_18opOCvz8il4RMce3ce3CrCr8dgJIbjxWeu-1wzlK-DEbYRIjJxqRwwaLRFhi5mAutzfopTYjvt2VJNNRPn1-3Flz4F51gw3yRIbmbZyOZkVzSPDtLhjlR_TAcCyYapOUlLV9_67VLgtYjUoj6VBe5QPfURgFpcWWTwCaFFmxyiDvw8rxi5IyGVhkWklHXiUch27yZ2IhrKFVALUI3nce1rR6kh_QJucLTAvGOJhjbOdcqRBWVPv1rXo1B2g1b9SgL2omAeA3I-ny_nNIvljcGq6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=vODOg-tNrcMHlqiApavnqnMpx-MWlcI56za69HgNi2Jlfk_rOf-0UfC5r9w-0jou6ZI3lArb24TFOdm0yTLnrnSfoJiHyX1FGWvcvB9ceEh-Gbe5pvYvyOQBV-PubSh9HozsS4OGxjw6UHhhG0cKJ431AXlybZpQeLguhscxVcqX2FZDHhvBRps5r7rgdAnDn4v7KC7-Ln43e14FnsLr_EvP64B96KyVBmi8nFpbrZ5jQiYiEbMS4PXW9SgXNIAnpZOZsLeP5MXhuAhX-nG62HyzU3wawl4V3ykLRexpJCywyafJ11kivklFmHASKFk92z0LnncegD95w-5TRlh9R6Fr3v454xMpLpZhApHAMRZuKGMBYxLz6Ib8U03gTjZaXq_oLRmQUFTWnCQ2O5Y0iAI4EUQHW9YsvQqPL2IKURHJaxYFSaQDMX05WaIv5mpqWwozYlkOmw9vqy71F7g75TBL1ra9o8g54Wf5MkHUfCa5vc7Qjoz4g0RLyW84hYMq5W1XS0nJ3LewNi9J22Lb503MErbVw10KFaSCCBcaMmNHfsVDEWNry9qcMPaBTS515puUEcYit5cmZGHL5cELWMfuwpgU7joVzsCoucrOgUrEhBL-mghrMS0jkr9VvyjDc52_OUv-nKF49IZyZcZPi6jGoxOjmJGdRsAVYxa2H-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=vODOg-tNrcMHlqiApavnqnMpx-MWlcI56za69HgNi2Jlfk_rOf-0UfC5r9w-0jou6ZI3lArb24TFOdm0yTLnrnSfoJiHyX1FGWvcvB9ceEh-Gbe5pvYvyOQBV-PubSh9HozsS4OGxjw6UHhhG0cKJ431AXlybZpQeLguhscxVcqX2FZDHhvBRps5r7rgdAnDn4v7KC7-Ln43e14FnsLr_EvP64B96KyVBmi8nFpbrZ5jQiYiEbMS4PXW9SgXNIAnpZOZsLeP5MXhuAhX-nG62HyzU3wawl4V3ykLRexpJCywyafJ11kivklFmHASKFk92z0LnncegD95w-5TRlh9R6Fr3v454xMpLpZhApHAMRZuKGMBYxLz6Ib8U03gTjZaXq_oLRmQUFTWnCQ2O5Y0iAI4EUQHW9YsvQqPL2IKURHJaxYFSaQDMX05WaIv5mpqWwozYlkOmw9vqy71F7g75TBL1ra9o8g54Wf5MkHUfCa5vc7Qjoz4g0RLyW84hYMq5W1XS0nJ3LewNi9J22Lb503MErbVw10KFaSCCBcaMmNHfsVDEWNry9qcMPaBTS515puUEcYit5cmZGHL5cELWMfuwpgU7joVzsCoucrOgUrEhBL-mghrMS0jkr9VvyjDc52_OUv-nKF49IZyZcZPi6jGoxOjmJGdRsAVYxa2H-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=VB9PP3BtSJEp6qVEeEw9g15Z6JvYTCcNi_Zp0iVWVe7RjgGhhf2HRVe2cVoM6x4EC4pgPYgzNmqKF_3e763nFdioTQzCllwQl2GazYrAfwujt-l50WPp3otc4gabfkdSXobkrpv_48dI3vALgYsBIjTtoHC39HYvoHUFETBsYsJu1kMgIoEO3c5fGoJNvQoGqnkS6oGgak1E07xM0J0y2DBjl8bkGIu1Ab4APiTCS9txfNnxBC08YgC44Z6u9oN75pjWQrwRaNYp5_K_Y59BO_nhyJg5V2e9wb_8aIJE-6JJeU-nXPpfvrwvMS0VJ0-0NWx6zP0D5S9-ibjdWzcpxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=VB9PP3BtSJEp6qVEeEw9g15Z6JvYTCcNi_Zp0iVWVe7RjgGhhf2HRVe2cVoM6x4EC4pgPYgzNmqKF_3e763nFdioTQzCllwQl2GazYrAfwujt-l50WPp3otc4gabfkdSXobkrpv_48dI3vALgYsBIjTtoHC39HYvoHUFETBsYsJu1kMgIoEO3c5fGoJNvQoGqnkS6oGgak1E07xM0J0y2DBjl8bkGIu1Ab4APiTCS9txfNnxBC08YgC44Z6u9oN75pjWQrwRaNYp5_K_Y59BO_nhyJg5V2e9wb_8aIJE-6JJeU-nXPpfvrwvMS0VJ0-0NWx6zP0D5S9-ibjdWzcpxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV0LNvVsu_Orz6u-s6GIgdSsh1eFsH0bfa9o_alUzmPqEST3lTBQdH4M58GKo9ep9Zaz2IcL8LROHuMBwQUiBeIQMZa_KyWlXCm7NkYaF8ZwfnNCDfQ2o0OZBpjzYXZeWqBPhEcwWwGib9wqNJ1hqk9j4SQLUCyXnt-Tbdc3nO5evF8tAKCrQQDOU6sdbF9IOIRBbVDdGZ9q7WN3B2X0Q1t0ZcqvocJVuHPTGcASvcxuZn7WmCHjb_u_olPtu7_teQksaz2FuL58LZ4BJaFpkLMEdfp5WVa6DhY_GamolP5ApGh_moAD7m7REnb1g-L8Ygd1O0L1iqT36up6M_yDfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=LXh8J6RmLqntQTZuWs6EnP68uDldtp-UHzh_LJ-XL88U9Wa5-sha8wg4arce584koIh51JhINMmrEl4njJhPs7lqgGtzxTZfnlzwrkLMKnNFsvMpmTbO1xutM0k96wA63XmiQhddqJZJ7sBJvMo7wRhz79eXufFhYgK7zkLJoVRMOEmRrLgTALYN3j3zLEU4dxTbblMcnMaPNaLln8znnhs9NAUdPtohUne3Df8P0dOjayJUBQvtzn8DDQaA5m0glY4ASoI5ggEgJIzxQB3ZoGAeoGC4rzE-vBFOKThZK2sYousybNsQA5wE2gTzvQubL_mULRGFf8vmnOLpXR0_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=LXh8J6RmLqntQTZuWs6EnP68uDldtp-UHzh_LJ-XL88U9Wa5-sha8wg4arce584koIh51JhINMmrEl4njJhPs7lqgGtzxTZfnlzwrkLMKnNFsvMpmTbO1xutM0k96wA63XmiQhddqJZJ7sBJvMo7wRhz79eXufFhYgK7zkLJoVRMOEmRrLgTALYN3j3zLEU4dxTbblMcnMaPNaLln8znnhs9NAUdPtohUne3Df8P0dOjayJUBQvtzn8DDQaA5m0glY4ASoI5ggEgJIzxQB3ZoGAeoGC4rzE-vBFOKThZK2sYousybNsQA5wE2gTzvQubL_mULRGFf8vmnOLpXR0_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMIXFIs2ZJV5ztMVSNbByt5ZN1FNy3tyQ9Yit1jDDdbwifokDFFdwmhxkW1JpsGta8V_o6nxQ--c2RxgYwiXtpV0YDc0bvEMHrcJ9eGOHXY6s4DLxOiGJfzSiH_mreszMdXxfWyWRWP6TqP4rV1Kq24HxpWhIn_sMfBr5EcHGg0aj6r8KjHv10KoN6SYMBH6imrNgD9H32Q19J--qR5-x1h8zoBDkG8D_fBK3c3O_H2_-nc0f32jclMuiBg6ftygbevXYxjyI-U63FtvvQ393QUzk_dY2n7r3TctUh4hq0jAAFuPf2YLvh7Y2GRgXjrymxTiHKjP1zLdLgM9gwnYKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzOy7zR3SLJoCA474I1Lwpny_8v_r-MSCETKFWupwQdYKXMFvCMhq97xapdXBmx6RvbhL3x615m7G-THk8S9waweInKtSzVi_4sR_6YSEsaGTt9-0DijvG6hMZpXKdL3xLepNRfooX73TbtdRTGbnLR1f2oiqZXV-WkHFxjk2730fB54HIupAyyTfGESgY6_lXlo0i_rITXT2jkFCsUHgSqi_ieGHtmGfGWE8Vdwuw--7qytdwUtG7TsSKBya3eCHNrrZxx-H89P-ACURn3tkG5IkjIAgp5DZpV1l8iKOiKkl66GDbnfdXveERKEQX-tOVO01o1byWIlt4waVlzCKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vULSQmacqIZaWSaX_yxo56dJO5g3hSmEoa-EAMnZrVud2doVheNd-6BxYSo1DWH7Fnbhx8Hi3ohf_vHI3VTSAwxlk_T4hKz1IS-2i_7vLROhP4s65L_e5zfhoe1R_eRrLE1s3ZwSFzxY_vigFtjz4cYYX0j7WGY5okgBRZ7DFOCV1z6YmZB84HMbRo2xDk1uKTTQxHxzD3UOaRD0LctHor-gEGmi5OZI1zUBj7-3p6ZimP_yNqHWurPk8zBEu6vs8kGpnM41N9P6GXC01C2_pEuWWNho4lDz-KNEDxDNuGe8Wg3kkimDfsMWqKxJ5dtodK3ST0opyh8GQQc86icukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAc8dU31mVXWKXbbSVXxFigdCXkg8Om2OXc_P6usKFi012NHNa1OegBOAsXd2fsLy6A4A2_mzoPZeurJ4PsRuKdsHXt_SYkJvXkFgim2Xz9sxDCQQQ_cP5brcn6LExU9cyKt_mmNGw4InvvnuC9IoOwm0OrKQeUbNw5Vx2w4Z1iFQeX5uXmfeFD1At_DZ7THiVqN4rGZe5R7krPLDD_ZoA7KDIbZXNzx0AyeVesOwIGb5qAdWDtuQkG1mupdTsty2oBwANzALPSWnO8qleQIrAH2G4Qrq7l4bNHRjD92LV_NTO_2_XV-qg2VxQVtkosJJaQfPt19tzw6C09cMl_U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGlEEYGkyE7oQTcWe8vI30g3yD7VHncYcaB57imWqQ-ZPi3DARv9EpsMMr4riv6ldCbxrhJqB7YpCslJd78Md6cGlmXB9dZ1WY4ODdK9Kc4Cx6ALBcyF_mykTenFRCLZfOba9YX-3MqjLb7sR4tYgmRAG59FiMFNlmFvymFZhDe1AM2_sjm2YrlAboGs7f-gkx1syqYbzHRolbXVEERUsIcgln1EzkaNFHUOmeflke70gFi5PA7d30OMcHoWiYMZm3POo2yzdaImb8EvBkeTOQe7nIzGF3odj_8gCqrVx6oEOU5mvYjq1UHwbP11B3Yr15Fqec_0rcVY4Bda8gf4Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW2305rDWXrEBF3xNx4JnL7XH_0y-Iq4lVe0fPn0zwVEYKLxkw4RGK2r3jp1oeXd6lulYrhO1jk0QN_50zcyxTcTgaq3lp9qKeQHwZ8JSF7H1Cat-svI8lVRy1boMuXwVSXwslQ-VXe4eH7NPXoQPx0QLsIXAW4EaBxPrUbOZDblLeg5FOXg63tX6iGm3GKurwRq07JXLAdEekaOHa7jsfo4Lgyi-8sypPW8mnxMIfTs_ZfU8GoWljKv32UOrlkgheWskegfYKq4puLCkZbvC98Zf72pfa1gCmCx-aT2RUY48uFVy7bzEQ-5V7uz2r85Emg-yMJMfPyDL33j9WCMFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=GHhsEdj2ag4Qyc-BPsqr4sMo0U74II-MxuFIvrf-b2mcJE-EqEGny0UyqG8Blfv2UjAkpu2yS03EpUCj2De6t6Nf4s6ir6kbFkCiCA2OzfEpiMdxBxXTB-hYuRRWxAK5FnByGHUkUkjKA-kmm_IEERk5uAof5rvMBLIRmGSZbTn3P25HGJ34ZfSHMrLvNsaevhuj0grnPY6RG4DMSIIInFGl40waevQDa7PT2LlrRX6fDNJo5sWWJfU9VvztwXzWLx_EkL230-uzigCUrMm_cbuz5Mxr3av1EmiAC7r4HtVzFAFnGzPM13swCzBfbWnQmT-jZV8923NW1G6i3jWUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=GHhsEdj2ag4Qyc-BPsqr4sMo0U74II-MxuFIvrf-b2mcJE-EqEGny0UyqG8Blfv2UjAkpu2yS03EpUCj2De6t6Nf4s6ir6kbFkCiCA2OzfEpiMdxBxXTB-hYuRRWxAK5FnByGHUkUkjKA-kmm_IEERk5uAof5rvMBLIRmGSZbTn3P25HGJ34ZfSHMrLvNsaevhuj0grnPY6RG4DMSIIInFGl40waevQDa7PT2LlrRX6fDNJo5sWWJfU9VvztwXzWLx_EkL230-uzigCUrMm_cbuz5Mxr3av1EmiAC7r4HtVzFAFnGzPM13swCzBfbWnQmT-jZV8923NW1G6i3jWUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdwjQsI9UQcxBYzGyyyhEP-xO8keIr231NGukJsTunWgRteivmJd7WJpAL16DfmK937OIWAv6SvNtgTV_OSgqXjUv4dmxq_58DH4eo8vQg6C81pDgElZtk9Ju9WX3XlrVq37kyE9vRDH0RKIohiLunUhGl-j_IuNzEiOgNo9z3JLgr5IbsRpSDKnFMNfIe-jkLoWSGeE6eF6YdrchoZuZkoU_tlDeHE5xGRJW6SkIh7XaBAnalbuF0lEYsrtx2NY2Bb4JHqXUg2uQz8G-OZD3PJukTIcFu3WQoTygGMDTv1BHu4N613OUBNP71_2OfDgLAZ4UuETJafl1usluNu-_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLBoGoXyi5y-MJ-Xcd0itFVp24rdaxjhK3k_xrBZ7Zo26aXaPAGyN6tWK9bJdMdCXX2zeUrrji7BQR2nzlWTftvtRTSxL2FDFc7LJt2m1dwuPoaTZmpCdNYTvvE1dVkRxLL9k5NMhrmzOLKx9DmVr9gVLFczB-RS88VBLe2JBKXT4mNkZqWcBnSoy4JUx-Hwc72YyW7UFvq_VVDhTAyaYcWW2I_6pHgvtAJFod0jktGuregFWFTl5tmK7x2Wtw9qSHrpfPLFQdYTg-9vpQpxVOa_6BDcXbQdd7X4pO9WXU7G9rGMRU3y9WdecPshNPKFzOIibJt0tl4XntCNV_VD1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0BJr_QdKW98s3hyL4alV5N4_NgCwAzmkNdIjiBOaT1sUyANVX0nTUOn5rP3c38UO1qfKOf_Xmx-u6pWTnw7pZEfwTp_4tD8yyQh_qpsWB0b_DoplHYo9DloUcnw9biSqLWTKT8J0oAVWR8T2Zb1vJwGvxykgmMvJPrmOiepFifJTXbjI3JRzVtQJTUbktAA6aaODCcfrlDHdMG-MtTWAeG5EjHA5ngHvtYQHKpOqT4wCObahfmikaVUsVkyG3PwPZHMCn8yyZK0rVUVhRH6zH5hF5McWaJ6zawLW8Mbd-v_QfnIum5EhRZvXFSQtgzLiSNi5ap5rSBDtI5x1PNilw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAUY-tBB7PPKFmjcRhoXzTdrXfEObNkC7k0yfRQ43TZd4Hcdxjl1SeefsSEtViIU2RkgXGL0qn6iRsovSU9gscdn63UVEAuV-T3ustyfQhC83WKACZ7DzufwFiChjlTgcrs4qSLC7T9fltCw7aTaTXhTZVv3B2Qj7J7geH3fdco8Lyb-7DNG14knM3pEDmeTiq6Ik1aya0cagP64a_mWSZDfsQlTCFl73I1V4hvd1xrLeDP-MFXIlpeb8MDUECN1yb35RjBjT0ThzhNctlsa2eQQQXbRvGq3-xTs9jKbUGqc1l5iSdmmFLeJcWgWONk1wTiSuEJkXVDxb7mhZTb4bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bShAVpREYUhI8zqG1APkdyboDlvh4-xAwuL33ltFsnNwZzPBrX4DkZffBFLMWPftX9XMsdiSBXLZ4b_sviULoNSER3gDPFSGX3enh-ZqsNlwDIF0sCAO7eLcD0G6YS9RKEzgJWYh88zoIcDYg8k23Lu5_Q2obZXYKl3GoV54s8Yrdo1Vw1cEe_t4OuFw4TXMoaU7pnbwxMBCAQp_kluiNzeuZCkRj-iaHKeRKLwgmtgvLMLXp6NRkQEwLYQa975OcPD8l0VBdCkJInvp-7jEb6LTWGsvosiKndhm-SYZdDX76qhXf4e9P9mvJDpjyfgizdjpvHtMNdsgWOHRBEm2NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5ymDUD7CDs4Gouicrnrht5m4bt-uWd-zivpb1gnKle8CFQHOovQ2DNYWGT05Nf-ukWnO4-JK6UWk_Wtf0gcRKngCg9k5jOyz8aG7GqZ9aku0-a_as-SZ7fdBJZMEWzpG2uy_24Xq5D_WoxRzHhl2bMaIQLN43MneueBMJu6gxtuBbtpGPT1CFYybFthaxIkABfNy14gTqNgiYIFWSpc80r1PFNP75-pmBIhugLBAbwcdQ7CnJRhZaZoLV5s53JnfqpkTZY1-FMYKJfhU6Qaa1YFNqIU1UfXUkF-TlHa4mtccPJyNWe4DMI6OJZQc9ZRFrQwijBhsYezoQMwXV2nfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im0vIS3S_-LLNd41JKX8H-AvEvBhJj_Llyid15dL2FV_Q0nqoXfz7qgoWA5XadaY20rtubR6IJ0AQ3s4CPWzNBLQOFg9gQ2GWdu-1c96Y0Mrk9QrRsfhhJn0r6-zWu599-Z-fVVi7ifnIWyLkGrFcfLCSXnQRQ0yOdBcLDU2nr9BI5i-tMVc8FkGZfno7CdkfU-PGlWf4N-PErNe39lVr6zh60TkmO758jsqCljO1YYwAtCQNhtGrNePdyhySQG6phjutWuMr8hzIWTJHQErX0yRYOyI-ugT7BZfOZbg5tJX_d-k9k2Zxjy94ELqldKVqxZHbDjB1pkv2oW4JHCa_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTf6HLUq7CgwSio37tzJ_3_0-sfbtCOAOEzCQNbabcFrRWO6gm1YxFxkagimlRAKiwTcOqoCSReXmD9NaS-ksNpd3_Bv59uTRMEMDKp7ISMLZbUV1s26apGf6GUBEqDPuW0sCiEjKSo3HDtoIUZpPQIDBPvjeKw_h4U7EJGGCHUe4VkozFcZ4QIdcdTNmwJLqRJ1XmNEkIUeHhZkemZpwHg2THdsc50VW_Gf4KhNajzH0URJAexd0DnHLbmb6DP-AnukzjNykB_iblVCc2xkoIjjwGWcjWRopCjGRZzt_InzS1jcDrvhVP8ShVPbEoE6MpxTTRSViXY_B7XlHpAHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYOrILM11ouHxuGswrVY-hD8ZkSwsuuVYRLv9LO9dsuDmzb16XYkMG5N02BbaxyrdnxWs9ShCzo9c7aLT7fZOEhm7J_kB8wFhuanp3g2iG7w8Zd92oehefrva7ryNYnvKC94In68XvznoDlPcFN0R_q5qUeuh2F70pFPWiA1a7PiTNZyxXvFCjQsqqqTU8ZRjnq-TcakmDGzUgLA6GWA9_K96RVMaeZBQV2pfkQV9iaCb0a_2c3oy1AVhsUt4bsTc_UC8A0XVT_0nONX7a-L9vM1uyPVoU9a47Pf9npP8aVhwh40_ruz5bNkgVTXtRA2-7KL641lGDwxOB5Kw6BZ4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCVqFbC5nWEhEeTxzJoneLsEZB6dRFKiT5QDpoLsOSuT9EUwrepM_mpYPm9BdziI3mEAAHwWaWeXP-DQvlk_sipoy5sohBdBfJyXuAYjQMFustd6c9AUqbBMxZWFswKcjZjPXa5BjhVkyjB8yJwZ1baMEIIiuGlRCcGTZnCH9ZyYgr5fSpchKh-9B4uI0vBAZpF2fkILVhUlIrquALX3jlVkftc9Kh2HBKXCHwGJ4vN2YQ97m_o_QBL8LqpmefVkZ8moNVJP1KxpdMA8WcDQBwXy9NTJYxLNt1oZZF5RTrQcKWZ-_w832zXxEIiWKWmntDige38N73SFd9nISgAuFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFRckBymyV4olyL9VqgsHmBBEOIQ3DiAwEBR6XwFxILtR0vtfOb7n7j0f259vRjvIunDO29KpsMFOO7pZ5rbkeKMzIsCVcPRb1mna3PrvTFIKMGnf86Duj2ZzF9MhVybCMT-U6gsftiWXNku7RZ-exvQEbgC3BpelV__qB2Uy8fvBbKZND8YG7mpNFqpQsAlzMivFVW2oho6FZQP49BMzFHAgy3eGldIRnUZuo2orIz50mz8ww_ByoCkXQ_3EMR5pMTBemEbcBbwqsbctMSxLhZOggy-9Ay8Xyq5PBKFop0VnslpJsJlMfkKt-uy2MAJMCvoTJAzWVZpdf6P5AvV4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8yfNnWDjZUbc81OCtkRkX8s_3oyT2dW_43Jd8_7GMy-cw0HsmvNP7j_MC-XeCD5_EBKB2ETUf4K3sguRg1lSVpsE-Kjl9YFHSXuotntAYEXG69p1HMD4-NlVFUXgx2kaYm1URbLVwCAWCY8QPiuCzV1VwjOPaQ0_DcfPiXcnzd723ppQMAprVwPWb1Jmxhs5iOK4KFI9RAlq8w1oebTOGLpy6Sqp9wdz0Y_UHh7k4IKI-O9DUJHCUvQXlNb5O7Yv0K_L0rMUD7LpknvONDFXvn9h87r2vqsboyvVVAlZ99lCqxHF-DmTHk82Sd_neFTW1uydeOMEEHWD7f00pxkVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgp_Wj3IkwrKjaECjHVnmJVingCp26y8Yw_urUAryope5iVHQZXx2hOYbmQTOAYgzDJuwkhKeC8b7aDUjinFB_bPv2mQZNsFW_DkvPwEknJ1jx01SNowpvycagDDdbQgvhewYllnMAlRk85Kglk7OZXf-kKC_wJoBVK2UlQ2xJqJ76hogiuDLgWFXN8eD5dmMBEE-uV7M86HZuj1xmd8Up0NGfIi96DWDeVC_yx71UKgbMUtKjBcAB05Mj4dZk0oOA9Rgzz6n91V2ns_7sXko9yTi0ClGsgsfe2MJ7OK0AdbQ7e9pdxd2DXUDH_6Yz2xNPK9VMu3ppwdgVRIGAAQFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPyBoBrbOfaPPpv8XmIULKDNe9bPcGGuNZoBJeN_4gE51lUdGyKeT90lev97QGLpis444M9wfXKguxAEUOKzlGPVk3DDH_7-JQ6yNhXA5OI0-mPN4AgdkDRGtnbQQB4UMXJ3emGp6d6LQqUTUgXzUtWlhNzeehyqj4V_5hoKSplpeFMo1HublbbsA_ux4SB_3HUzT6Sym8sev173FCs6KAoHr0dV1U5Wi7Z1Itf_CkdElRqhbCAOKFtUWft_WufeWv0IRgIpTWOye9eR49eVp4kD3vId1M8-RxbgzGz8td-3YCdwymL7aJPcU6HAPdjROh3NVyt1feLME6kt3yxolA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa0AcHxvT_g8U9An3FyvGPYCE7dAIligfFF7UPTgTqFzx7_UBrkRXL8QtFaA8k4GJLf394ejqB0i55fGlwyWcR1G9UOGned_rZamwQLND2uUxE2QVjGnoM2CF5-yXnVWkL4F14M_NJz3fSd0PnlDA_PRQ04iwPMeQ9gGtsllpu-ZIJl2y6slNCvqxZVaAdTHJE1I0cwJYAq-I4CPvBsAn4o2GwFAsF4BbUgTSVf0yBOp9-rhUcqR1fIcT_wpjJtppqOIWb4BkzY25Q_e7tRzFbcDsmFifBH8XhOfy4QBK9OcN4RT9FWII8vX_4I5Gw68UDjjREPEqwebShTCGaG3Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np_RSs2Jwt_DlxP6EAKWVr173E9_UabTv6Cvx-couQ_-H0pTbL-q-PZ21m47xbbNC5shnPubbcVOpv4eT6TTOoG-Mr-2J4gkIcbO16jF7xMy7fGsi8qwTvnnGctTfa1OeakpjyyITqgkfAu-V9V0vv9JTIao_V1NbIcd873uKsPH_wWVF0fV9Lw7-JIeZmB72rTCXvvITy6Pr7FRush2zB47wewZM5r6rXl2S8sm5tLfjwTKDpjkrjkmhK8PtDTt6khBXdh50yUGOeuOjLmD-NjJaLH8o-HBMVkGuiqrzaKelg_i_y19_-ij6wv0OOQm1HazCktj4ihiRxmH3rgRgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMYhpBX4t7amhyt3ugk_Z9BykagNG5tGufY28gBtUVeS3k7yNmi7AOVQcBRaJfdzicmP4BNhL6uby0o0Bm2EFZGPmLUo-T9ubLCSZnHtVVbkXAzh44WRWFq73CrbuoGk-yiPLbvnhV53iG8p_s3TmQWo45KTgO_BliND2HvRjj-mDBOH-olWkXheSAfhjagvGsvtbcn1Ue6I486EPnA3ilElzaHD_PehfXA_XgZylODmBIv4lrdZ3Zzvo6cBpZFH3Idsp-Gy1o3sSXYvEIoFyZMNifILfiY5NKy2dpCnm0MtuSAQsTneB-HgLaaadrUhCxhbrnSaYbMCxSSLGjvwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRCQUv7YTQZqm0BiWaPwEcs1JHo3WZha-rSCYsutq90qVhIx9iaCLIoQWkEPCps95mwtkT9cLG7dF67DIiRRd1wXblILy7g1BOf3CgaVA0jylQ_vZFMXVBKOaFJTAwrs3RCuZwV01hiU2FjISvOx-e6JJx-sZoDMljpXz0Yz-N0SLBjF0ANTyGOKFuEs3Yu8LO5l1WTvGCkP08vA-AAxjisVVa2VonS6N04DteBeS9dzI26UWF1EwsEJEI3A6QIpHX37-eItjE450W6YHX-ZZrNyqikpoya9NqKg0gLHtTB_51IJjtAb4w293mUoD2qnMqlRZxG9KxB3ETUXPkZneA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcHRv3Gu8Tiu7KniJVZ17zyWnCvhTqy1VqV0xuqx_Ky8fBggJCn6MBaEdFilqdXoRzaEf0S6DLSHXPlx6j4eR3Lpm4Ni2KQce2fhEp1z_wyCcKDSafPsr-76ZHVSaVlOvChwbVwAgGFbe6YXX0IwQ8MtTIHeN_2RyhV0ZcG6xPd8oJLSC07WcYK4CbsPld0SBEUyXt7FurwU-3_33LewEOrw9frVdGygfc8bR78tiHywXhDy5aB_lPb6eqJJ5QkkbpDje7PwnGISSf2ppde4_e9C2W5o17UJ_T8Y8E1HhFdgCyGD3jl1vbexy0HTjDvkZVyoeoeAM9FKvkMpJ393IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=WWWPPGGam-epdEkQoCI4q46-Ic-y1P9Lhm7uRgAX_rtkxKsE756PoJwBY2B97PwP9UUkJAKXQ7B11bBHVqqNkSVdqCwsm5qzfC70wfku_aJ5yZc0Yzx1omUpsHC8cjdZyJtVUvdpT2a_XzxR7MVZjWZRr5Yl2Hbe_EgqxIVBxf3q1BMK_9Zf7LZVgtqv9eS1Ru6pXQ7WngMB49JjXcfqQqH1J-6RWvK0HTI4G2duuEPXcC5BygnpHa7fKuMaxHkRwtNgnE2Wt6tPcQONupFVcsFOz3Ok3bkDbA_3bDoP1fkTNSCPOzVkkytQ_VT8lNyU8HHtQvgNeQnHuvhqUHmzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=WWWPPGGam-epdEkQoCI4q46-Ic-y1P9Lhm7uRgAX_rtkxKsE756PoJwBY2B97PwP9UUkJAKXQ7B11bBHVqqNkSVdqCwsm5qzfC70wfku_aJ5yZc0Yzx1omUpsHC8cjdZyJtVUvdpT2a_XzxR7MVZjWZRr5Yl2Hbe_EgqxIVBxf3q1BMK_9Zf7LZVgtqv9eS1Ru6pXQ7WngMB49JjXcfqQqH1J-6RWvK0HTI4G2duuEPXcC5BygnpHa7fKuMaxHkRwtNgnE2Wt6tPcQONupFVcsFOz3Ok3bkDbA_3bDoP1fkTNSCPOzVkkytQ_VT8lNyU8HHtQvgNeQnHuvhqUHmzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2T-eZ6AVxubj2x_BswiXRBJyhM8Ip1lz-fyo0X9WQSsuNCDEI8EqxP0Xw6pjS3N6VfgR_fW8gkDMt63qNi60tFjYh0CF4MlQxl5S7D3ieuJvoOhaguK0OzCgMbOR_JWO4NngnafKnqYRT_lm59yhkbd36gEmj973udlRw-OFdW4vGvO6SsXngWxkWMnIkgNsGSSxdd7DlCV0cG6qXnd8VeeKuqtEq3rs_eDmwYFJlYw6uYFRVrmGSu_XyJJznMqA_QCIQmf2emCAmpy_C3sAEYPhkujjeDLZn6KqlzS3-5h2dqwD4GpUkqgJJj98T0rPIblveMWQOrworMPiu_zaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEH4mFjeqSzoIOdeN4CjO9i2Mmr2w3QMNDm1-r5MySQNACOg6CxO5RQ7ufuFVhPpUYWV2LvSrSbPBH7ITU4RFKWQ6vJi0wNBkot9_dJNbrGHWECWSQp9ZfWqmfB1T52uNUI7MydfDR9L_8O0gJHhNvnjOLlTz1DNHCkLbv4auMFrU8NKhBco8aI92OFugkmBkcU4U14Z6Pm47Od77AsRccIee5MjSFzYziQp02ty0ay-YT5EpAAnM5iOkeydruWLVcAXDHhaL-7GY-BGGie9_QdMNjtSSQlQcqYjE5PDBQNmCQJAX94BX1kNTR8OGIKK5iSmh1uNB7lxT0jE_pYFwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=tW7g5rNLiGmVNwBtiz9mzsRQaPcO50BMpP6SZS40m9Se7GBIRzaVLItta8_wvdVWvPHml1obnyICAervbLx334IuzDuSiuVRn91E_fJ1HgSCUUT1dFKpFEs5M_FIwhN5LZeWbRXyU2kNOHHgrWee_fRmXA2o7Wz73hfUYLBXIOW3CQ6OsjAFDoyjGrmEor9-xP7CQiCMExqPH-RN_mqabUdZaXorhsw_aQ-ocjjLGamYzKZbQOVr8IO8OcLksvww7vs77H3LpHTgTWUoQv9gQ4YNV_qma45vXtM7YpOfNSzMVE1zXwQDCZjRdHSKdZa-qH24xIW_brNM7oO0Vo8-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=tW7g5rNLiGmVNwBtiz9mzsRQaPcO50BMpP6SZS40m9Se7GBIRzaVLItta8_wvdVWvPHml1obnyICAervbLx334IuzDuSiuVRn91E_fJ1HgSCUUT1dFKpFEs5M_FIwhN5LZeWbRXyU2kNOHHgrWee_fRmXA2o7Wz73hfUYLBXIOW3CQ6OsjAFDoyjGrmEor9-xP7CQiCMExqPH-RN_mqabUdZaXorhsw_aQ-ocjjLGamYzKZbQOVr8IO8OcLksvww7vs77H3LpHTgTWUoQv9gQ4YNV_qma45vXtM7YpOfNSzMVE1zXwQDCZjRdHSKdZa-qH24xIW_brNM7oO0Vo8-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=F2JRY7TORgDEvRTWRb2TEvEGi9m1Dnc482CIVx8Qaca04xb_Y83nseQw9a9cGdJGRZlf3A93ZLP3e9Vr-n4d9i8ODMfXH_TuFbGq_VfwqHFSGte-q6gbW15or1KWQuRYB1ca3YivhRei88o2oL685_-6J_K6KkHWD2UMUW-lNjscOMGFtRmoheKPws4oYyjaTDyzUz5nbbWqjDQ8hYaw9LMqSmy8RO3myKom-SZ4ghkY5_J7QQljoU-9l19dYT7Pdi6NhyVPxyG8N4RuO8E25PrGp4uwNzmuzoAz1crKY8dhhAz9xomCMBnmk_1l-7C7Z5AR2ila8q-Qur7QB7z2ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=F2JRY7TORgDEvRTWRb2TEvEGi9m1Dnc482CIVx8Qaca04xb_Y83nseQw9a9cGdJGRZlf3A93ZLP3e9Vr-n4d9i8ODMfXH_TuFbGq_VfwqHFSGte-q6gbW15or1KWQuRYB1ca3YivhRei88o2oL685_-6J_K6KkHWD2UMUW-lNjscOMGFtRmoheKPws4oYyjaTDyzUz5nbbWqjDQ8hYaw9LMqSmy8RO3myKom-SZ4ghkY5_J7QQljoU-9l19dYT7Pdi6NhyVPxyG8N4RuO8E25PrGp4uwNzmuzoAz1crKY8dhhAz9xomCMBnmk_1l-7C7Z5AR2ila8q-Qur7QB7z2ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=KmxKjxc_uSOesfYpWjA1sN0cz97NBqRjswLJ0c_hKTU__0NAhkk2XZ5eaUW8o4r7m-0vdrl6lzwpXVnVVl_SRQTWxygQ_tI4jDtRXyi1zKNSuO2H92msb9F3seuQf8_d4TX_JnHzMYRJRpefUYoDSWTY1L-Bn6SX4aYhWgzrVPCKAFH3nG4dkJCHsBuPdA3Tu50PhC2UCtGJQc9ZaFrWbeAFK7yk9zCjI4ZxYoXrb6BKxIEEoCJmoeTrjQXfV1EjE5dIydNR6iTedCJ8csheYcL53rHl1gJCkedeBUKFBy71-la4I71n3N30G6hiCexxANIC1SeRWWSS8Wovtfuwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=KmxKjxc_uSOesfYpWjA1sN0cz97NBqRjswLJ0c_hKTU__0NAhkk2XZ5eaUW8o4r7m-0vdrl6lzwpXVnVVl_SRQTWxygQ_tI4jDtRXyi1zKNSuO2H92msb9F3seuQf8_d4TX_JnHzMYRJRpefUYoDSWTY1L-Bn6SX4aYhWgzrVPCKAFH3nG4dkJCHsBuPdA3Tu50PhC2UCtGJQc9ZaFrWbeAFK7yk9zCjI4ZxYoXrb6BKxIEEoCJmoeTrjQXfV1EjE5dIydNR6iTedCJ8csheYcL53rHl1gJCkedeBUKFBy71-la4I71n3N30G6hiCexxANIC1SeRWWSS8Wovtfuwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLYW5JZvoulw2nmBHRMctRxmHuXxYxvoSyZ1x4yBaA0PUZkt5yXGEZUJdpoldwKtScYuPM6VhyT-YJZYkr0hLowNeX2llucbQ2i4xU4MqIJK5PLg4nF3_VGEPNvZKSB5NydKQsDjWN3a7Mxc495j7tTLS18dYwSt6ajsDQwjp0N5WjfqMT_WOUVcoz9zyEVkYTmBu654A5ihjcXr7XzUbcbKFKAzsrvmGV60WsvhLwXmVkL3F1-IuO_2dQki1TqIYYPJKmHmtb-0p9J3wbrDnClgu9O4N9xpOaq8s5c9iacU59xeaXz2m9FcddtOTyv-5pGhoQyz5ByCsDihdeeghQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Ky_Zcf220il9H4hU5uLNWkcldrc7lkNipzNtAIjABHvTRiNPnFiT2YFqMp2dtX8GGLnUfe06xDVxTWW60mLYedvrAhqp5npnp1J5EnjJ9XVMyXgXGbAh4g2OQByGYyn0CvK_D9qLQi7JiQf7mjzfICh5N2CMdpyunfwv8VgJbH5tBZNU3rNSs7CH_EzC6YavaTtlQxhcqWH4pNjB0B7TnYi4tzFyiwj9PHRf43rTasQKwp3EqiUyYlXMTBctq6a64IGAoPLQlipc1U18pKzkcwNOaIgqeLgfnmEEXOt94IT47G1nws41Jgy5u7ia9yfGJj3eiwcWSkpfZyvJTuJyiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Ky_Zcf220il9H4hU5uLNWkcldrc7lkNipzNtAIjABHvTRiNPnFiT2YFqMp2dtX8GGLnUfe06xDVxTWW60mLYedvrAhqp5npnp1J5EnjJ9XVMyXgXGbAh4g2OQByGYyn0CvK_D9qLQi7JiQf7mjzfICh5N2CMdpyunfwv8VgJbH5tBZNU3rNSs7CH_EzC6YavaTtlQxhcqWH4pNjB0B7TnYi4tzFyiwj9PHRf43rTasQKwp3EqiUyYlXMTBctq6a64IGAoPLQlipc1U18pKzkcwNOaIgqeLgfnmEEXOt94IT47G1nws41Jgy5u7ia9yfGJj3eiwcWSkpfZyvJTuJyiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZpf6lqndymte79YBY-THFeh3rjy3w4OmHjGl0V8TGzAgaiXjMCaHO5Zoi4vjCjwE5mC5wWewhZhWdM63i0DZoxQy_68MgYg3OwUrwtgmMMZazpJB2_Qe7dvNOq1ycnITP_jrDpo0rkFQhBDhY8AeS9eeZwew9C52Qa57ofZVqqBWLQn07DMz3uB2pQKQzFJBuqF6UbeJ0WeGJ1aeM0HlTaFjAIiRzswxUbazEp1x2oGDWn7_daPkQaT7ofSEIoFgQhtsxqVm5W6BHAL37LoMwXlLXGHcTbW0Z-etsDOv_8caKhyp13tCsfz6-nLVnQOwuBdnA_D-NwbJ9ETRUPH_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGll6JIf-CVXTFxJri2vKkShghAP7U1b9_RV4vfYqB0OobQ_9wnpJ7n6K6ltxd5Ag27C9imEvw9-2IJ7gRyN0I-gVQvW8U9u_YBARVZ542KuRYcRbO50zVSV77AZyBiajRq2-ppkQ5YmmCq5-m4jq03N9206Wo-P9pMLukoCsglZeWLprYzhFPs02Ryo3TDxaCVo3Ncc_FISRrv4nNossqh3aet1BmLsFwolTgMnz-ldjqKXiZt9_GEJufq_sC-4WAhnX3NKMjIlYKvgTLx1gXekRi3J3eAs4KywPk5wwpCJRZ2sXr-DocOtKDeCn7V73VVfQM6n8_4b-3p7C9jvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf9NNYsZf2aZvzIKXUwOV5KyIOSs4ZpmMol68-DAClf84BNBlgmYAkL4FI1cckSC440NKrjFaQsbq-JyUsyYj5pUYq_qX4lLL-j4IAKEaV-68kMR_AdRiIvMpLVigNKbUMRRr4wexr8CCNjoBlUlk0RD2HzRzd9_18fkSmXEqjOnlY4LehEwYWli5RO2ANIw0uUCsN6FMgYWb6QngvbCyljDz6QM5M3_qFIVgsiVpwPtD3GOM9aGzB3wo7hZFbkmviUWWvoQ46keo06f0MwfgJh6ogKyjxITxvu7MtqGGF19QwG6xufWheznN6whyqmtl4K7ZiwpsqSDes-hnMjCYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxAGNOiAwtVmeTDDrEPiG0MIw5eSFDVoXwNbtujTP7OfPtepFXjDWQCg7uepqRPrrTZkchCyUrwnTc7FXLzux0kdG6DM65SmivWjWkcl_uUDYazi54c44PxFfwF-OLA4dPZldhfYA6kNoz0MNR83hBLXzyJZtbHGuo7myp75voM--e7dPr1a8ByANVOLMnQgHnXtYJnxx8I41SOzO6vSoivwx2D_fJvM7NUIh9r5qp1vUTmPLn_ACZXM6Fj_U6QYcwqrmeTga0Hc_y4Sl7yDtSjqYYyBuId3Fs-b6Et3KFey0RWapV820XgufmvAmvEP4UlumTVf1JUgaR3nNL7b2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdaxeIdJ9kV1jlkbwfE3bCY9OqxRuy4nqpDcLRiq5VMcgTiTLNjIVCoB-7aJKNRbFCPiIIrcQYAfw2yG9lSt_JNZB4wc986zEjjJ1JuXmuYf8YDTKVeMWUN2E9B6NJUMurqq9FE9wsTfiH4-cPA_5cxdT4W6YZ5pReBw9HUXWWCPbhCbJ2gRUpnmaTWEq5qMVZPZ2bFnfgo8CG8Cy9-G-8HWZQaYjcErxvBZbhdj9vpVXaKPpn6GjNp87CdZ7C5N7Fa1nx3m_ckk_RgZowWRb6AP_KfWFr7EIeC4AnvG80hBIlvmZhRQ0AEDrnxLGHkuGE_jhEGUFWLDaq3kZRxy9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI6518G38U1c3PwZmpGa41g--xM08sPwXO61mM_hOBNF1lpYv4ZVwJ6Uz-BBs7lia2VlFrcIGBJobUW0U2Pq1fG-hrbN4TOuCHmiXWNwMay93-QOmZ0Qn8knJdPla78DJbPHBn2jY7L2FZYp62Wh1dwSCZKAMW4_WEvMu6mUrJbfV4kD7BOlmI-6VkErM-QSXUEDSjA7K38_1Vf58p3s-4fdxdKKSDJPwarZsckf7OeZtugKxnVZyq4UXDT8O0Q7GS308nwxT6ehJlfOj3A0rJmjv-IR9X5FsYaPWvHmyLvKmVoSkQq0yZW_2-zgzX2AJh5S-K1I_Ux_kJueLJXmtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxDrDcpEwLCKHxgXxWt94x4y8zx0q9XH7nvoK2XC6ke_oA4D9RY80lJqpOUD7RRdp9OpCYveNtTQ_kjsnIuzpiNfH5a4AKK4HS-jNK9S53YyKIa5I24QY7lTnmmQjOlbaB1dfb2Noz3BEI9PcJ4xkHOIV3hmlIe09sDrFEkWMJq6h5oR_SEYIzxEyp5-jkr7vdMJe0SkWrR3RmAU47Td9WDB0VNwEqfi3VUTuAcJeY-0AwjRhmTI_6Yyl907rVEsSAipHBt2thm-QQBZdSAySqC80SNlWa5TKJD2Pvwfapk6zQh3wf2ei7zVnQ_A6aEUy5dULntMmVJWfGgOPut5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5iaBV_H4vt2WWEZSaMqJNSwaHe5jejEpd5RoZx7oKIR3pgbG0o0KrCjxwi2GxshnVQtzLBr6aYmq9Vl8LE99XHA6HLCTa3Ze04Q7j0Z5gfSDHxO0i2gIN138B3tYW1owtPo7zJ1mwhNSRkyPsr-hJeYelvzKI2PNLZCMFmNcUo_tAhrTWCTP5DJrV4ElRmP4fqnh6BRrj-5OAL4Gn8PJt0ZB47m18xjTbj1d3XjBlaltQTg23fTA0PqzMGFeUuLu9__hvXwd09BUxYUJ3aJPl0Lrwp5GIXCsGMifEXx8cp-gB9reXpF8z5mL-oP8I0iqv4ybjDo04cBG-m9GBkIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uixtwco69RVmxcb8LEj4RFBocEfw1a212R3nvr783TH2eNHLS3ESNrlM8Zesv_MgJsPJLQdkhWKYlEWO781bBnjXUEakO1fELrOVRCGgV2ft-krdYsI_N_1Ji8_lcZpO3SBj-Be5kWNw4fiFU652WbuHF4vJ7qXIUTZHlwrUoPSh4oBe85JBa8a3Zeo5_R6p3uMW0GaZXr-PWY148y6XSdBZr4G79waCItr5rn3WAlvhVH6DGiu4O4eQQss3W-z2oG-AnQzegt1woJ8py3VGwzP6TD32HPtMJSucbajZjRUyAJ8fWeo1YF8cIaE-DQJfwl6PRO4RzDPr398-_khMAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eisUAX3xe_l-bQXN3yyj6MpQGChHKWF8CdHjIoeu828xb0-QUuq3Wq9tp2lUNUIaSP2nSaKkEcd1E3gsQNw627guYvIdKiZXnGU5zGKKN1S8785RiRNT2q4exuZUMAW9-JtDeuy2RSP6O0dT58PCibO9URpXxtHnpyHIo1OzMuLKgmQRG8qMy-avMz2Jm0EFMmxmrMcoN5A7Q4G8ZMAjzMqFGFaoupLd6eQUkEEUWe-QPbgN1H-FOQnCqqcBo9FR3VbHL75vFt-4GWHF-8ls7eqnIjodD-ETE5BSsOHRvBwa17SwKo7PVXRkhYNQUxz2mqY5FkuH8iyvJ3VZwBMA8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhUOOHcisytIA3CmsufCxCopWv6dJpItgpg9ZtZ-AXql22PdthbtbDb3HISbydhfHo9dJM213U5Jzkw5EH_lJml87iQeiv-YIsS0fnZZtTzE-uFBY30eo8dKo2f6-XLj_TlXI7lloomD8rtGu0S7qA0ZtkxHIAeFyowq8ypFfjOhNVK2dOtdSLaoJcJ60ZRLFl1Nsg16fIZTasNX2tk0_5WEoXr1AcOJltBW5u8WgcAmeRF984bS_JIxRZcn6ui4F67YZg7BFPQQYeZI9Z9lCtJSLC_hFIbJG8c1iKlTMbHEYwqis2BjPh0rRkZ79JIJD7jhXbxcGPT_93yyyYH5mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtoYYlLHp9pHJEYITbP5PgAVYknhXH3j6IRAL9drZKtWB_DM9jSZro2b_om7Mt93JwcfzINd9-KQ8q9JIo1fUaYwu9juCa9LKgB4VYJD1gmR6yc1wWqNH7pFvy1puWYieNUfuUk4IR9GVojdGYFaCntmVwJMFnNzLnWSEvoOuXxUSoKucTlAnkMKTk9jrs9QLtnoB1xM2LuYHa7H_RWDjUBa4593GaHjcC8zhuVai8YDx6gIlnA4ZeLsSSduD6Dw0KSGDvkUZO6A1MwqG4PLz4OP_ewI2eVLcFsZBUm63xzVU9xELN9b3rnJOcL3TTIlhQ50SSKVIspsh1r3uoZaSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKSMfF4iVEhceWle496nDlgiliXMN6HOI420WSsWa2c9pm6mpiU50s4SK3GTaAWBdF9zaByv8AAU9Wf-TmA3monOfDrWdAOkZMc5yM1lvfiq--YP1AnpJn-FXylnZ3jrUAfoEWjCxk97sSrdP6zpj_MrCixtYFYgRS1TJW3Em4zmpORgTAbR_PEmn2qBqeW1Kjp0Xis_mDY6nhiUfMZk-NAZiWZQVtnWamG6Jr1J1AKvSuAQV-7LNAv6-fcr3f14EeF_NPJVneUIFL4iuz5n9AQ8L3svKxl26T1kRjKlKtMtHVUKaDUWW_dXlLetzusEr5-tcaeteMN9fhC3I801ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCsGpQ_6zDIvkPPIUW0nb26tdhpH8y-uFHgn7swY8k8-aKPOtb-IJYZgGLETPIOwipM6A16zXx0iiG1D8Jj3C_lSJRM2bjtAku7SZiWpRt0pv2M6pNbTU_AHDX1ZTix6JObER4xO8XKdgkqA5LSp5IP0_GxkxGNZkOLoN-f7JsL_7AhIE-V4WK4f9X3PPGkFDwYeWiSh4Rk7KIYE3P5oaJlSE1HMvGVUVLcD5OW8CMMhSBmYOKAkoUS7WBTWswDtArjTjzYHR7Yrb2YXhvErfvfnphAvxtNmkXsuOtAEM1-k36qLf4xcmM3mRHgppX1_CI5dMDMVEax38hYhxx9-nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp5ZET4twPYj5JvZmGo4VzSGNaxjmj911y4vptBG1lTwU_iAIxDZW6bKRqQAr_4RPtLWwMRmxryst5sLw0sSk8BBRyWcBczfwTExeY3U2ZPKBYJMVlSnDctZgLnim5XgQL_9HfaN9nhoYZX-jFYSA-fksyqq_oXfF5DRbgGIe9P7FJnWbuS6cskcOz0SLqgxfwLeWdDvnS3ZLgX71-IMtCyawgPmYmTFLqtBHACNmPVEs5zhEIpWBf2kGCg_yLWGW0dganeoH0wgxTEePuCOIhf798sSa8sb0TDgIUwBbltcNC0XoQ_T6Sy7gB0QPLnqOGApBIu0sBtDYWB8q1huyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv53IuxCaUeai7tfiwkHxi6_gFYRjKMG8Mo2LD8nnPeQRRTJFokJbGW2mRdhq_z39o5DxMztbYGiDGana-jXAPlbaSNvcpaU0CgI0OJXsF5ynjtW65iyrrBv1vR3BqiYIQKZVWOUBQtq5w2ukyF4PFaZifzqQr-hA86nM-EfKZJHVXeGnmHJBEDUq2Kx35dVZrHWYutEZ8GJhMODCo6if0xUauQjbQYSTvI_2ZPGE2fHxh5Bg6mQIWh0OL3ENqyMVdg85h8A_zA_qw8TiViCCqCC50_H-SNfdSMNU2Ihz_h-uTwyXCmUm_tw5rKkvYkg0MCOQo9H37lVG2o7vJdB0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqeezlKOvy3mQl2Zre52bPWiH3K_ULE7d3YvMZrQcCfPtDU0F3nIVHU3hqhj9vURh_IBztUB3eQWfkGrMHxGAS6gauYs1Wb_wdI1Pm5caampVqUk_IHcR3ajtDzp4UwuijBGtpB8cKqAY_tMHUuoqc4TZ6blIF8FNBqmCwahcYAu_Bol0r8vOP-QMfkauhVIAW8Oq8gvMvwysh0KZVpvI79RO_0zJvoiMKWHjJz4DihNZFMwy4U1JLh5IHd4uPhqbfCSoKySk7JeRK2YA-H1BuaUpADQSb_Wo2NG5MOJZgdbA1PLLz0jbDGGfVRLaiIjPjj28n5CyKieBO711r9Dnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcA4eM6Mf50htfu6lB_1VPXPYVhRBDoQ2GjhfkO38E_8zXUbQAN3WXGK4NysW6CQjKb2gsxJbANIdHKXGHtkUbFymQfdmVCqODMvEOgsUE6KXODzG6hs76JBZa7S8StfCC20KDJl75SjoD6nvRTrvec9OydHE62fz8HhzHb1-TmSZPpQRaGlpaXUMWpAfd3ECdSu8mZGnlZjp1bcQHNT3E1kkY00CC-NguxBndLTiQ2wLwPqmuzPX0a7pzueA67YjQr2afF6fhlzaSwR5e_cF_CsIQwzHDUapSPNni82XfUufQu0x54oOcsN1NRTP2VrrIwkpJlNS_y9rildKFxqEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=c5I-Tl49lXKYI-7pBYqGw9QS-QPKkzryx9o3gyI24HHEvY4dhJzZmYG4tCoNc5Agq9xYn2ZQnOC-YVjh60f6RezJ-QadauRsx7xyTmMpgyFlX3KW-hbUAAKCUS5x9S_R753n3IolFG0tPbPQ0HOsoMkSftHSccqh26EtOM3I3J6mCLHkHlfIjZeLfAIdCv7BEuuKhZ1mVLFeZh5Y1s2V-X2VNUITCE6FXLEsWD2HzarMCE049woH2ENKcCPcnGOYuoZ1p0u0jxMdIzQrFTyALkwccoNHcxUX5rk9S4dghyUGHZeipZ2TuaPJpNj6s0v7PszMVnwUBm2oHUl2S4UdPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=c5I-Tl49lXKYI-7pBYqGw9QS-QPKkzryx9o3gyI24HHEvY4dhJzZmYG4tCoNc5Agq9xYn2ZQnOC-YVjh60f6RezJ-QadauRsx7xyTmMpgyFlX3KW-hbUAAKCUS5x9S_R753n3IolFG0tPbPQ0HOsoMkSftHSccqh26EtOM3I3J6mCLHkHlfIjZeLfAIdCv7BEuuKhZ1mVLFeZh5Y1s2V-X2VNUITCE6FXLEsWD2HzarMCE049woH2ENKcCPcnGOYuoZ1p0u0jxMdIzQrFTyALkwccoNHcxUX5rk9S4dghyUGHZeipZ2TuaPJpNj6s0v7PszMVnwUBm2oHUl2S4UdPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg5YPSuggCyKAQjtCDD9huA_F92fJJlnoPJCTZo7dyoTEz_gJj2oOzCbBsY8mJpdlVLHWT6l1zsOaH8pI8Uw2d34fgrXG50xcL6CBbeADDFnIREHQQRpsIm6MebqHFiEO9Ahe7tcZSWje5QyfUdWgNRIl4QQanmtPYKg1omsUxpIZwIv9yjN15fhISpuYMZw1YBf92szGpcYnpElOP14hyCzqZMi37XDOiAx-qAhiAY6xYW9Vq8N23yHGovz0J1CkOmZcDfIlwLsxQilNxib14RLcWsSLx4rO5eTmVInYejKbtNurTbtDch-Ls-ZpehxYVDQvfufuPsJ_IzfkrflFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=HaalVpVtA9m8XtjFxASvGQN2F8PzOLkgqfGEay4C7iRtGsW5puYeef_LCUrEXfs0VHFH_bmPsR6z3Slsgi3p4OthAMM2vgvK3FSUe8rdYYTZf1GprbocQ0y0a7LyLPjruOoEJmJhfjnAnUJChujDDAyizG9ZkbwIjHJc4vXZSE96mvB70P6_Bz-g2WiMC5H-rDr8cF-0_wLLfDh_KIQBceFc6xwXyJ3oAMyGa2OyifqqTNb97kF0qyBnG7ENQTjbA8Z2ifNE_uVkJcJz58uDj3tjtjp219vMn5DSprZlOVpkrtESvQzFFS4pyNlGWiGpXVVOlaI7VsJFCZ949lDUnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=HaalVpVtA9m8XtjFxASvGQN2F8PzOLkgqfGEay4C7iRtGsW5puYeef_LCUrEXfs0VHFH_bmPsR6z3Slsgi3p4OthAMM2vgvK3FSUe8rdYYTZf1GprbocQ0y0a7LyLPjruOoEJmJhfjnAnUJChujDDAyizG9ZkbwIjHJc4vXZSE96mvB70P6_Bz-g2WiMC5H-rDr8cF-0_wLLfDh_KIQBceFc6xwXyJ3oAMyGa2OyifqqTNb97kF0qyBnG7ENQTjbA8Z2ifNE_uVkJcJz58uDj3tjtjp219vMn5DSprZlOVpkrtESvQzFFS4pyNlGWiGpXVVOlaI7VsJFCZ949lDUnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2cT5C8CW_Mc9z6vjOyVYZJ5Qmp4e5vpeyAVKUCLurLlVStJezGdBIY0OkEQB46L9aLmoZAT7Z6ciLWxVn17a4ceJG_prijkEB4MTxb82nwWFMInmo2fwD-Ey_B5jINORcMe8TiAG7Hoi_62p9ZGyCS0CC9LfS5TwXWl5eBePfLzLUZwIoeI5U1j5TP5RLvQD48yglVYNNOsOebwarj5AV6tzxF4lWqVog4B4j4l4AltBzEeXZiGaDPrIEhrvntYRB9arGvYydbEWnemc5fHKyhnLbzTroHFDPQTJZqsNZgshXNrWWFKo5WbtwDJbtUOBgXPTD5ugX_y60SyXbvfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFx96yTRgqDz5dVn7Wbf1Jjr3X5vUguqI96yQcPqMF3QgkAj6T6XR2_q1mWukvy2xEICtk9sA6tWWagawDB9KTVJPa6cLk1SNL0pMnJOtejmrbxpwFrbAd64hbjDuyzg_1-hBYFayavOSJe7rZK4QLvBtYG9O4J2UAYev-d_4dB1pHs91oI5BUeMsoDk-JrbMmOr7hWbnWQYiSoEUBMQC8boJDl2cmleiRFtjZz9_xqfkg52Be81wsYGoh11t-FRdg0v1Wz0r85hRVOO7grSg79npYKxfsLGBPrbfj1puLCh_1yn6nrYoI9y9K7pRf6Rqj3F4tKW6T3BW2T025cV4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdmYavDjNJ1kEXzC6IOnVLMh9BQUAGMW-aIPFkXs2m7ul2wsJ6NAvLl0jyL0A29B2acCupUbSVS75gxiwjKXKzzVF9BridF1rFaQ38tzxJeuj3Y5iSjNcufdhmFcAa5_Dt8RRjdM3E73sZxuqput2K62QQB8NJBOpMLE5hbgGT84dfzUoZYSmmntfTBg3DTaxW6R0FF49K73OU6eUtHRu1-MzdwT41p556PI6L1st1hxnDYy7FeakbEmFxHT1kQy6JE86_cxU44xVH2nyz51rMyrznHRUbgaKi10b7WuL22iZoWo-Fd4qmHe0JTrSjycjP8NOvhBp9lm1-wi2Peumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHzCbuzyOwtfpdxZS_4b1YqYgfo6HjBGO1AErYY6mRaRgLLMiQEMzkGhDzHDBtTvBnwIXjyewvgxi5w_q0erRrDsyaBwWic6QxPBvBij301Q_n3reteIOAKUOxcCepg9zMu7wwlnqe1wx-xRrYoIoitEIiBXYh_CZtLQlmbJV0FI6_-L0qGMwD-UJUjZFCdxBxNBvHZ8hDj7c0Q38VrP5yIkjxWxXZJKE6kUAlX4GHZLtD7HzrdXN_4NIZsBXM-eTuGJ-bqFXRixz4DElMUav-08p-1frP7pR6V52u7hX5wVGBFOAYPPl5QJKBqe4ic65az3ePxqJgGuMR34G6_NmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WT5smmvNpDQi8NcVGj7Du7CdwuQCZaNtWpXxgjS4anYrkDKdy8L8MOpMPElnUyejSVAHhkEcHuMtOOD8-ZjMpy31NiBUaO3_LjD_4Z5IXSIbya-m4e80kLruM9uoCSlwDDWprN0yyaseN9R5AOEGTZI5q1HorxCwvhPG5GaUF77CuX5glZFUu0v2BkVvE7sjJbvuVZdLzLu6ZCFBm2B1r95ISIBg27ahd4KIzXhTo4PV30QcsguaFOHSIyUf6Fxxbq4tq8tVWVj_vYJdwOsCe8alQuIjanJUerBObGJ7hPfTGULEtfDdt1Zl4A88ZW4_I3k3lfqBEwDkCnynhxKo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGJ0hIlMfoa0uNwHanedak_uumPgDxB33yH3WLKlthlObGF6KQYHNKElcaykTsu50U2nNzrY-yL2uuZBShoHPYXsKXJMDTlHAFxzy8hmMaRJRFIM-rmyEB84mAaioB_h9xMiJ94EhGdKttym22KGzQAL7vYiUoeANPy7cZmxJPP4P7---g94YZINprbkNttcfV6M47Q1RbzaopjaOHn7WRRiKIwu9JGZeWXXLBpwYU_Ewe4l56CBreOFd3PAok0jp-XqcWqnuAgwmwP0jkCUvpoUuYtAMe0s4jIwBDXy-Ot9GtCnlKpyanFYEXAonNtRsTl3HtL9W9MyZ6egdPdYhg.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
