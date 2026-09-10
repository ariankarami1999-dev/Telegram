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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 00:48:50</div>
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
<div class="tg-footer">👁️ 872 · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSLcw10sLEeJSCa9bjZgByQ96FGfCJlsan_NaCnp2K81HvHfyzB6kk_pU2XVkLAKypLbXcWSr5nrOW2vCjBQCOxFeJpKCC54QvlHY4Ba6Wy-pkP4RVECW3mLmtagOtUySLMOe53wAIRKXPJTioqrbgiUIajewBijKre2HF4IRdM5ut79EB_QyQEac4kM0UDotB6253WJokH5HFvDkXhvtsm7idXPg_rr7slbb9WGjlbORw2L-htkDZiAAi98iDp2_HbDrVYa1q-PYVOjVkuGwgPjAvKdz5AHBRkzrOtPE7lig8Mhc6hNNcrqlba406NR5Mn84IoXRCSTiSRbs5Cl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jetTvBlTTDarUmfdZ9V0cAtS4chluUZ7J6Nefl3uuUxl8OuUBY9Q6mNi-GZeYmqhRA892vIsozK32PsgpdiF3GzY90jkcYN6yQ1zOfXCz563ORhjVic0tOw34VEvZM7ZBAOzQcyHQaR7m_G9x4rtQ5T6RtfaEWTjQm6YalMQJfDRTJ-UcCm8RUHs6ZJVbKLn-SUbkHFgzgGqk__AhbZjbf4Hgb7kRJchQ9kNmazab5SHlOCuuclcoGYv3uuz467vK0CTYSuBZ0SPeVZFQrdkiMITrVOYjg-l5O9sD11TtB1pNddKBMOfRDcCSulnsxPUb9uCEmRoVH-i_MKEXjaz5w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=bH1JWXSiWc-c7L4scOr8nCRerId7BsEA_WPdfv-IskabySDzowo8_UjcUmX2x19CMdtsm__Eqvq3w6ELzOzAt3TJkJlVXmtcvvqOuJIxo052j3pvGM4lfLE8d_P1LiadrngqhsPhqubUii592DDrmu_HO_6ogyqdiAqezjtQj3KJINyyNemr10Dy5qK3JO74sLScStyoXuyjA1HK0akFUhI4SqhUGpUO58SqjFprnLFm74JCEh-H77VsmgykIQLWabyobsW8p0JhIWlOuR5kCxjUE01tNjSe2YJcy9Uh-mexJNU2l4u_YShFYgDUZnMWVzSeQI32kzqYxDJ5FBKrBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=bH1JWXSiWc-c7L4scOr8nCRerId7BsEA_WPdfv-IskabySDzowo8_UjcUmX2x19CMdtsm__Eqvq3w6ELzOzAt3TJkJlVXmtcvvqOuJIxo052j3pvGM4lfLE8d_P1LiadrngqhsPhqubUii592DDrmu_HO_6ogyqdiAqezjtQj3KJINyyNemr10Dy5qK3JO74sLScStyoXuyjA1HK0akFUhI4SqhUGpUO58SqjFprnLFm74JCEh-H77VsmgykIQLWabyobsW8p0JhIWlOuR5kCxjUE01tNjSe2YJcy9Uh-mexJNU2l4u_YShFYgDUZnMWVzSeQI32kzqYxDJ5FBKrBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOxqCvmXr_BDQPO6Atlv3hxERB-p7-cwaUGsNvC4ncWODsvt54t0bEMa8I2t4ILJ7Txp0FA3IrP7U2IK_DLytcLL63JDx9J7YwZrNVkdQ_rjHuQn49iTkl6wHFh3fRtRbW7O_FX8MSNlhvGlKZyxmz7tZ_6Hlw_8eBO4hC21HEtA0zBlsL_JCenyuKr9MHkKQipnsm0pF-ecwm5aJZ-Ayy30NCoZu3yZQEAeZzWbJQCDeJlToB8RCvZklp6QcNcUERaaMYabPD73t-tnClwXpGrHwSEjyqbqIfLeZri7H6l8Ek1G1niDS97nG7ledw-6VkfCdDEnGkx8PDcBX7qSOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=KEQtMIgirmBwOFHO_H_JoVimIHxVqguCyfj29j8-w4JtowWyPp8jINYoehZH2yD_rwHaZDmFxRuZ17PwM67iY6EzByiNOXtcKhPMlG67_YeRm4cYWP0CX8am24DnTQg0EkTdWtBPVY02Wbp4mGXx2EX-6xjE5vcngQFaSKp_FI9d6QyJyAI2kTKqZoe97ITR3SUgfVzuIyAORUJpjF9x5NqJGzXjyXXCenP9ZvVBqh_gTkA0WfsKQavKNTDyeBgMWvptT8zSFTocnmdRyZUIWqCFAbEOVHPPOllZSezancJeZzikTJvwbKhVcwRb7pkYAt4qR4nVc-xuUt3JXDavzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=KEQtMIgirmBwOFHO_H_JoVimIHxVqguCyfj29j8-w4JtowWyPp8jINYoehZH2yD_rwHaZDmFxRuZ17PwM67iY6EzByiNOXtcKhPMlG67_YeRm4cYWP0CX8am24DnTQg0EkTdWtBPVY02Wbp4mGXx2EX-6xjE5vcngQFaSKp_FI9d6QyJyAI2kTKqZoe97ITR3SUgfVzuIyAORUJpjF9x5NqJGzXjyXXCenP9ZvVBqh_gTkA0WfsKQavKNTDyeBgMWvptT8zSFTocnmdRyZUIWqCFAbEOVHPPOllZSezancJeZzikTJvwbKhVcwRb7pkYAt4qR4nVc-xuUt3JXDavzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt7thDmX7VA_Zi25R9K2N4cYaNjA7g-D3PnbLOh6Ank4ixhvbSo96fKVlnPWdC8JfuPzxhO2mNW6KvTIuD9cYy84R-3kysjALraeNDzBKo9Lqju1HiFvVSGmUSJNKBvqbNnmHdwDDIcqwmQeawma53BV9aIVeSWeC5K4a-0LzECB8A891lxYFrEOEhW-FaHwCBRGiFsYk-OmFA6zN3b6ByYxi96cNP_kR2LMVw4KqWmmYfmE_rP7LoAu6AJG-KEs1g6bpBhbyFWxWDChM3RqAda-mnxHEN4KUyTV4L9xM7wFFrjCa8igAG7t0ZiFw2HfXz-QA_THgWU7erTwB-ctuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uab627mtmR_tLJdvSKahQycDBBFVGxHJ1_PC3a22hGigz52XLZKQpmaD8YTEJgn9V-_AmQUpcUxfLW0e4uVZqcXJvzu64SuCfirNAuO9Ofs95wO04iZ-CZe6u1Lo9rjZHTFRgjMy_4wDBL6f6P3BJmMCAC6K2STrySlSqsIlqjKUHr3SbdbadVFjbcBF_RmzvmT1Tvvi6KyMNVtcShZtI79w3ajuHYYKMr-dgz6_lSRCSw2jOKFj21YlXBLWM6NqxGe4W2iDRdZdvPtRDy8IN6BYT_Tun2Vj2kurVsV4DQbuZ_4MbO3X8hx3hl-ph4HBqHk7yDOZACEbY-hpPdKLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKBHrQffg1_yw1MpQKFMgHD4zCIgyYvR-l9SRXd4Sr4bEn5KN95LIlQKPnikPGwT-3Ecf897y-PFW-flhPqeSNj8LB6-y_CboDjKPvcJ06VRzL2TGtVK3kVruN2Ad_ajJixNp4bOeGjFcDg6DcNSmslPPYZF5vP2IX6WfpZrC7-Gs6TW5wa_DHuoQLyzHyPNAqNX_aLucfnnDmqARakxkbpfG4ix8QYArQ6nWtxyYtIug3Oe19bBvZhBjs0ZZjw-HXC2eYDF1Hhdpz7V0m7CxM08VtCJ7W-ApfqUeMSwOLLCZXneUMXkD-4SCbI7-8vctQy3wt81Kf6ij8tEvqN88Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=p6us-AiqhQJR-5j2ZsIvEAX3WLwbmhXlgfTqI3XND3Ycqti5qGT88GYxLYNCDRIa7blgJ1uN6qEGgS_VVDD8gOaZWruDMXbJHEAWUH1vK_KBwdcnrMwGqCMT33b8OFC2xrhMJHKs7n1xSGCLTF9Yo4YK-PppiP2w1SGNZ68bE6A8j1kX3ALdYOnLC9Vi7zVCRlk8_6kfRfo1XQRuThWiGCohc44_EmYybB8ZMtLeTFj0TyDdYEZvuTCcPMTJe5rTsc_QPdHyjXN83kPA9BBVVKiSmGp_i3KZYCi1h6qSg4fhPJkjxCjJIFh9Zv_6VGcZI8FMhQqdSQT9PoRqAHTrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=p6us-AiqhQJR-5j2ZsIvEAX3WLwbmhXlgfTqI3XND3Ycqti5qGT88GYxLYNCDRIa7blgJ1uN6qEGgS_VVDD8gOaZWruDMXbJHEAWUH1vK_KBwdcnrMwGqCMT33b8OFC2xrhMJHKs7n1xSGCLTF9Yo4YK-PppiP2w1SGNZ68bE6A8j1kX3ALdYOnLC9Vi7zVCRlk8_6kfRfo1XQRuThWiGCohc44_EmYybB8ZMtLeTFj0TyDdYEZvuTCcPMTJe5rTsc_QPdHyjXN83kPA9BBVVKiSmGp_i3KZYCi1h6qSg4fhPJkjxCjJIFh9Zv_6VGcZI8FMhQqdSQT9PoRqAHTrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vdzi46QUAzSdm1vqCtv-G87NwMTb10FBQHQmBLo6AAeAMX8EYQYSblePpchI2DqvQOaFzEi6lObbxPISk7RSefQlaY6E9q44i9cA3H5A_Bsji5diaCqivmu3WBznfE9E2km8POXKhL9wJK3mREwp0q6q7P6Dl3g0QKrSixbvYmLtbrxqtrNJlv2vIlplvk_w1SwYlnB8PQRWdlJukuazT2krAoApUlVb6C-mKXB1vQnJ2URiaIx1NSQu1pD4Qy6pC-Afqy3tdZAXa66n0bjqXOt9XA0XhE0VxDThzHz8NrEItj_eZTJuZf4SLkKGwEITpqE2rzITmQsMoXodtOrhPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLwbMfi68YR4UEm_YIyKn4vT0iXY9i2D9tjMr3iAjLN9FJsvILrE1FyFaVRxQAnP5CCDsl8X04qDIrjltLtnePYeQ6XRgOP6ox5yzrl16WT6BlBOKIK-G5pdStSss2TjdeFKxs8k6qrFCufDet7BDYI1T6mD7yibie4JCJqRPL1AElQXB7uss1x4qGiPeKklV2QaYc5t3ZRnJgLQdxdQBdHwYg3ltdsxeGCfFUxZtpSuaKz3QqyPTh9T6vLK54H3TLv5MVI05abID0AR1ctpyjxr54TbZItPjPo2juIQ0Xhh4RxHCwnbRnBQJ9FqBrkC4yMJSxVmqo0gazEQ4zpVww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9SUmUjeFxQxFdu-h0QCs7W5VZpcdGMhc6tLnmXRXcBJJ8z--bq58VbeJr8Ds1Zvtc7kM6tePM4AB2RoFDL7NTJWgEPuqpBCnlFQDSnuhl8TyfkrjdBoYVpLzYL_rc6JEidlCCyPNqnyyxpYNt2HlXj6BOi9ijgV6E3759Xo9KVM3BrnfXiprlAUNjfGVffY6HjZsCoYCmLuLD6AVaFZOuSJWID3V5nckO9UsiBWE0VouhC7GhKntYfIQqRh9GgpmVR1OSSt3dM0c4qL6t7Z5qpC9jEC9KpA5NLKH7F9t6-T9Jn3qGoMuTN3Co2G1hGitd9PFUMyf9qrQ4-6v7w_9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk7um6rcRaaWnvsipP3Rjmq45Aj-5R9Vy_D642KbkdB2ildmJ1ej49FOpdzb_fPKfITMU7BjXBtSU4PVQxuXScGr8Jq7w_8DKV7lq3an5Qc8BUZ3TWmp4OIc0Jg7PgFXxinQY6ConczEXVyVgEtcZgnMf_-gpfo1yRjKQKc10xS3vkASOvudZ-Qobs9RF7JxgObcSIp2tH3IIqF5XuNoAHXp17tUha4zbIiNMq9VC0CUE586rkTle4L-6Rxipck_mhXDCSSMooMlvmua558lr6exwg70W0fL3wnHymK2gFWhtVl4iimJjdCopNWfTULGS4c2J8BSrjrL0eP-KM8GGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOxss1wlhq2EisRr-RlEkgTkywwTtXMMR8ee5hieODhUlSFCANbGKymg0sYz5G9Q0k_P457voggXnKP4Ch4p1hGei8OrxFcitYEGl17A4Dq2vp3RGO-NHzIsledw1RM3GqPqIVDZF2NwhDDyKJATXmpJx1BGtEi2u1o-eWAr-YMQuqgWpyfvCKwH5VoREdoFOkjGIkc-BoKewHFWbCrEwojdeSTIu243HcNnZd-TZ88FHNq93k3e9uBhicirMJgkt7LPnU4LdtYGJpvLe6fP_f2DeIZ5-iY5mcg0ziuG7qZX_irw81_EpONU0AfdES-jOESc_MIQaLORQJLPGXvVLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR56CHRb3UJI8LSyZ41oTUiY05fUdG7Oc6JwbaxFSN-AKPqfNyKdTy82WWcveh4YANr26Bcvek1YMMNrsjlbpTUcrMA9Kr7B8QgTJy2_6fUj5gpLNBWrRi8itdnkh9B4yM4S6B-ZiAJzArx_7xcHSsEGL6ZA-VOs7fj5D7VzzK42J-SlZjgTuQ6GuXQzsTnhVCoShrDjO1O9tjv5I_GQ0-J9gBLFEs-KIsUz4igtVjUeHX4or14_GX2Q1t8bAviIixIn-8rOEtAGhrDfZcUv7PmmS1OVO-CdEtFyPl1AoE0hZI5XMW4LUqTJ6kUyiV7tqbQdAcWZjtw3nS_RAbVlXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOfDF6UPG9iHWurjKcQ_HUM1HAdu3kTVoQnge_IwueL9g-Xntj4CcrfVdN3wDPlv_LlyOo12NvB3c46qZDLLceRZrOTR-c6a22s9MrgvUXPC2pS3Ir1fwZLV2ceHl-nen-P3VpQ5ZS-CD7BTweeeoswloA9Z0kdaU4HFNBMjq38TiQyQZh39-LD02wswysO7qx4Nqo5NJhBXHcty0UKgmy0glc886I3qKXXX1-z33kn-IbeQ3dQ_5A0mdqSUvavBGhIX4f61PWL0uYvw3d_bQcyAZRyiuzWvEZtrmKexU4MWLomUtMSGeLANUnaP8sADrV4ppL1g-3Me63MDlBFHbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUvWwH-L7AjHHrEwuigNReDjnKVqaO9CTCTJPOMOKIG8IWR_IgiQ7rG2HZbZFtiENC5mHpy-JuvtsinOGeRKigYrLHRg0-c3ijEqCMxmy5lfvEJiQoXplNVPzFBX9Kpdi6CG9Ze4MrBtqzo1J0v_-2FVP_fIEGoVZkS9iDBJW0vMrKPbd2sRcc_rb1nIqEl9rAwKZO0aVsi8SIjsNJs1zgUh_GWLh_ze1KIP4L-U9pfAIbOzT9ZbeoSDlWMLzHTe57jYF3nRyIHomeyl4LMB2GXFJ9Su1jr8X5JkOVNyNRq1tF6F0mB0Yig2G3hKtOAX6B8hChinRKdwyWDCwIx3cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk2mswbw40AnYw112E3WLKtGMmzSj3MF7owTf8EcfQHPL67A3T7raLa48v-IsW6K_VSdVHLXPP4fmEapCrIEwLxTFuV5mRNhIp3lLlXjfZk2h_PEWJ50gC7UxN16SCGtFJObvzJFLanV3_P9_yWbJsmgh6bY1HcuUL6lTwsPwQB6mYQUzvAYhwgNI633K8nbQE12CqSPUvatnaRismIpWEVdqa-hlKLELgI_72BwFC-mU1i3et_utCa1AMrYfb6pnmS-NRQTHHSqQY2HZcKTOfkTCbryV3g7y966ITux2PG3II3Vy9xHrYfmpHkKjVwszECUBOeGn0P-kLcKkGC_7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKrILGOPQ8LsYTdkMDC2jjLzY4704JsL8TiiwSp0-5-8pd4u3D46psmKUFPRx0UaUcDzii4MKkhiaNqXxdwB2N7CnZsnXvm0oXjS9RGdz3y2ZY_vXbuDUhWa7_nGIkwBvHjhnVC0Yqi28-B0JHufl19HAQH_jIZxtEmNFqihqLfyFi8X61d39942wvXj1rdOPrmRo5eNwn8mO1nq1NMn2aZfFpN1ygn9N_1dfFnVMIxEx4c2XIBPEaK86iiO_TuKzupkw5ytad7R0rvCIxnGtk26jOrY6vT1BHY5-oRKcFvwAt0rupmDtcBcL-eKr6az_OugchJAfB4VlqpCeo4vDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHKztxSimPv8peP-QL2YGwr9G9k8qoz9REncC-q9am3Lx74gGA1sYgT3FMH1m3t77EjpKwsZha4OoUALGCVKf2KNVwHMopcn-s_3TA_LZMxclnJyicCZ5UN9XUaCPwfhdLv25E6VPdoc4bQl2tr9i4uZT08PUp_0r-OUgvTZ03M5_3MTYD1yZyKiCqlxbyAXSCClZy0dJhZjtaTmW4MvDey-N62n5I7QDtU72sh-zH7UjGnDcHgxckHdiuhY-4tW7tvRSQspeiNSygKkawkyvxWVGdM92hhoDXSkPag-9Dca-3zGM1IftFY7QUABBMtO5fvFDeQUKceVuM3EO0jgHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF_4INxn6RYyhazbx_UX3allDYEmv-UaRKj6h5ZAkVPuzOxvrQ0yovdmzq6KAuhxk9JgAnJ4PtbIxBWHDWy32oyzTlysq3ahd5Zw_noANoUIRacqaO_Y8NrZcP3EXzpsXsUn-2O_BWC7qTw9QEilEAOy3s2GmC_fHdT9IDyipmNW_0FLPEFn22B124APEkEaiBZoehnw0mGahqzgud4KzHc_zEonAOyQv3vX9EptKwW_M-Uce65kyR3g1NbDdQzLEJyXBavMRGFdPbM679jqVwUSntrZ4ksD7AaOgVuwHaqzb0J7x80TLxuaqP_TS4Kk71Kuh8KaX6djXt8I9ez7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvpuSEGDcDdtBCcE3TfSPMMSpCXxYuoQrRQpIMWA_I1ROz6Em69v3Atpuqhm_z5edcNyb8XHE0mbjweHO_ZZJZYAFwm7XYemHgxTzMKfMAHJhHfvX009--7qUAToRvjQB_E6dYRF9sYDeZ4IqwFgRo1zoqJb7D5ybHBcw5cguUgKjOoUea7BtB0NwKxEYmXSCPugFzHZUEWkXBEpAML6J7e-cCc8cIHd8FWXNX6XlyLgHtphGvZngzGyO1yibV4sHD8nb_uKwK0M98RxdHl3H4opIUd68Ss3i04aYMxPXQN7iitXXuX4CnT3Hsah1g-OG1JHHV0iQ6giEcTTRgu2zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8sKA0GpymbbVELhqXeSYVrgIj_SXG_P78BmkkUEN0utdLcuovpniW6q2C8FdlY87afpuolWJ5f9GiHh4PA5vX2AzNZ6HSU8XPgtxNZ_QYxPccpmmCiGN4yj8qGcbrN71UrydRVysF4pGtlUbLgeBudb3ORJEIuSbVcD6PPe5Gub1PxeNgsipW0AASifAbzJEeuY8xE6XILELyeRB3TmFYnY9xmKKso0R-3xjNlA5gC4jcRMd_Zp-x0j__agVV0eofwG-OLry5p6dur0CeT0yRr0WNmNA2GbzfI7l0RCUrRd3gsQhK6S8gp1OWCk4pBMTYNForAUD6yfP3gXfm9HmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NADgElV1bbktkUzJWOyIAEADge5ZSypIsXkeMOhCZFiLpirO_-6FqIqqXiNrSHiScBzV4qy0tA0S6BPg4Sln6aPvSufw-HmWqNbHnjO6zKlhw96GH51Rz1CrvQL9EyCYOpQtItWiHDVPY2Q29Hs-sh8DzANYr02DoAe_yRTht7dP0V4PrNRDS6Q3gICqFx93-kPNgewgeE2nQlWJQrp-E89SybSWU8lKC1bjYvHadgailNL7eIkK-Pm-Cy7TbZJBusl04CagVCQmgQU_cZ69CsKYbAfEiJJtFPjCgSv7Xb2obXvQnhxN5EfDNNyiDMIjHdtn8y-8Mh4Y2yyH9WhS8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ankefK16FQqgwQLscTYLhRAPEZJATCVChWT5pWE9B3ojxD91YK9yf822ObTJS0JRYVDN4LSRcIajFq77mzrnWmvk9zAIGb6aCMgxjuFkWvsxoneY1unT3aeOIgEtqbJE746g_OQ3WPa-_-aYUEwi5Lo2hGMVQ4VdoxZp1pHspJxtDlyHZy8QeW1P-ay1P9adHloETzLF6Dg9ZF7q61_3mgxYsl1WIYfm9YB_2hYHQLC5zo_w0ODaMEsY-828QEfROO7MnMpsCJsKPpLHY-yPRxQYgt0ngSEIHQ_eRgh7qFspcLm-usZNWS__edTro77T-ydtNUcRVPI3ayiFG0JMhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=sj_Zh4KqQ7yvqgwt2ss9h_wy3wPHYQn82zK0KxrDf4o0VkPJVI2XRhOZwX8fkhjlUSJY15-YA_5oP3k5KxD0JP018sbyiiYU2tNlqTF7Up8ZO5xnN2HG6903vN0OBF4XYoZEnA33aks43c0EbDljVb88oJ4jE07c_EyF89NISMa8Nuq-3bf7qTojkUNyvoESkn47EfaFR8hzn1G7HqEEz38H8ymcetHqcyKhyTySph2OOQ4VZM4i1OU7HkccT_AfeAI--IjPDFciwcUwwVxDY3YJ_M9f7lHqswChoDPxRlIYxrgmlA1xd9pSlWQAbZeB-awroOrWVloUWWLFcGNSRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=sj_Zh4KqQ7yvqgwt2ss9h_wy3wPHYQn82zK0KxrDf4o0VkPJVI2XRhOZwX8fkhjlUSJY15-YA_5oP3k5KxD0JP018sbyiiYU2tNlqTF7Up8ZO5xnN2HG6903vN0OBF4XYoZEnA33aks43c0EbDljVb88oJ4jE07c_EyF89NISMa8Nuq-3bf7qTojkUNyvoESkn47EfaFR8hzn1G7HqEEz38H8ymcetHqcyKhyTySph2OOQ4VZM4i1OU7HkccT_AfeAI--IjPDFciwcUwwVxDY3YJ_M9f7lHqswChoDPxRlIYxrgmlA1xd9pSlWQAbZeB-awroOrWVloUWWLFcGNSRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=J34Rnq5JsTUXG07lTnqWm7BD9260v7zRrpdqrXk7Yzz-JMo2lxKwWJqrGJouio8itaqEULzljtxehz9cwrbA9kfUdTtm1Ju2ojOepIRnVZGKAMLnAkXi6niDgUV2x-4_8svjal5fHB1a_C2iHzTb2L6XVahPDL0R6wdUPGEudhmCE-sAhMyTBtpo_eKrRdDIk6ozRWdqJ2FqOc0PzpO37unG2-BMS0hevbwJu9XjdAJtohyQjkPjKvj9RF5o0urGNtJYwsAOWJ-66mqJKtgMjcd0C8jVSOY8d-pYg-HuPjphQvN1LKCNuvUl-pEGEnnqVxlz4e5GK_bzM2Ez2yR2IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=J34Rnq5JsTUXG07lTnqWm7BD9260v7zRrpdqrXk7Yzz-JMo2lxKwWJqrGJouio8itaqEULzljtxehz9cwrbA9kfUdTtm1Ju2ojOepIRnVZGKAMLnAkXi6niDgUV2x-4_8svjal5fHB1a_C2iHzTb2L6XVahPDL0R6wdUPGEudhmCE-sAhMyTBtpo_eKrRdDIk6ozRWdqJ2FqOc0PzpO37unG2-BMS0hevbwJu9XjdAJtohyQjkPjKvj9RF5o0urGNtJYwsAOWJ-66mqJKtgMjcd0C8jVSOY8d-pYg-HuPjphQvN1LKCNuvUl-pEGEnnqVxlz4e5GK_bzM2Ez2yR2IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=SsXz8TsTQUP6iW0_hlJ03fFe1Xb0Kq-uUDcBvJZmBIzuf9ApkYKoEI9rut4ug5ZO-esvv6Wwif0VFHtQzkoOO9RggrG-7GYwpefTL_eaJIaYSjIUorLyLlKOHm9JED73ZMxV8b_cDAg-3Mshf0w6J_qIp18BBEOZVXWMlLN8yAIh8l-9SNQIJN03xDvAgyRxPHuOty3EodN07z4y44CAf2OCyCaEBzkmCI8s1jphfDs7iqJSi-xM2N_B_0F65I8AUCVdfV2FFbq_zx5JA-UHDuggCxoK-4pXpA5aylFxlmDAI0BA6xuy3kkB-8GHiaWm4hI-PJ7AMgsvTdHgSanoaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=SsXz8TsTQUP6iW0_hlJ03fFe1Xb0Kq-uUDcBvJZmBIzuf9ApkYKoEI9rut4ug5ZO-esvv6Wwif0VFHtQzkoOO9RggrG-7GYwpefTL_eaJIaYSjIUorLyLlKOHm9JED73ZMxV8b_cDAg-3Mshf0w6J_qIp18BBEOZVXWMlLN8yAIh8l-9SNQIJN03xDvAgyRxPHuOty3EodN07z4y44CAf2OCyCaEBzkmCI8s1jphfDs7iqJSi-xM2N_B_0F65I8AUCVdfV2FFbq_zx5JA-UHDuggCxoK-4pXpA5aylFxlmDAI0BA6xuy3kkB-8GHiaWm4hI-PJ7AMgsvTdHgSanoaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoApYCV5U4Aji-uos6Op4bEWCYQ_-acsQDDFJWANSw8mdxHgysr90dyTbbAb_fAI2e-jPu6u-VmDDFFvzIg1VDiMjhCbZOUJwFMSdH59m-X8pYeXkm--PHxGYXOyBiraUaRo3rFJYtn8MwghRVHhYWkam_ixxc-r95zf6BwmTEBz8qfu0-j434lvccKwAo8U_3ucF1CN7mVANeD-4iGCffqbFgx8J9cAw5Y2avc4yFJDk8Ofbvp5-earlCYspyZWqvyJrxzWXrtfFls1uzfSRPkkqD-hCUZobpZAYS0sOJmzxpyIKEVSJOtYHZVtmitu5c4wGJ0i93rou1HohBMnWw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=SdB_Ip-hRDHXLkw1yDpwVTAR608hrOeLJaxHifBRJnV7F7J40ZYWnGWP1acj7JnosOQwUcPxanp6K6rdbzax5jyIxvYStGqLjFIC8FyXe56CbWDBm6eFr-bnsX1zcMo4Dcaj3QLgsqdfcQHcWx1Goby4nw0wjuO4nXx83eyCpNRz75zCWJJg_1UWwKEce3inaZt4oyhBds862ju9KDeSEUp55ETwRGLXK8nfmYf8ukznTBPvWa1K7yQjHL1mgGCvLfQJagXGY67LT3S7fzTvliOmPm8gH08DVOe9AYaHnBw_Xk7sz8AnXnnlOVnzM4tLebJcVNPfpc0NadpWANmRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=SdB_Ip-hRDHXLkw1yDpwVTAR608hrOeLJaxHifBRJnV7F7J40ZYWnGWP1acj7JnosOQwUcPxanp6K6rdbzax5jyIxvYStGqLjFIC8FyXe56CbWDBm6eFr-bnsX1zcMo4Dcaj3QLgsqdfcQHcWx1Goby4nw0wjuO4nXx83eyCpNRz75zCWJJg_1UWwKEce3inaZt4oyhBds862ju9KDeSEUp55ETwRGLXK8nfmYf8ukznTBPvWa1K7yQjHL1mgGCvLfQJagXGY67LT3S7fzTvliOmPm8gH08DVOe9AYaHnBw_Xk7sz8AnXnnlOVnzM4tLebJcVNPfpc0NadpWANmRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnqMhiPcPRae1DXZv1DFwEqrLd4ON-Nz9AuwqmaDqzNVljPGYJL_cfdKmJcPfFkBWn9ktJzIrqjkGYIMv25fGjKGRSr6kS1t1gnuxHsNeQR7MNdEA7uWWqtTR-BDVXBEuXVeTWIC3TagITv7xrSx-z24thUd9EHcGUAAH57K55NEScWuSkOPRCUfcmXTv2Wy-gatXigS4eGdnFLdz2MjpXlrc6DZEq7opCSl0Pm9stGsYY9W30PJ6sQBEzNQWWgL29Vp--HZkQm_0H34_O4WrWXTcscayh0jnw-RZXgIavIWOGB6GxMZaXky7o8Ap93BfSn0xlFff05kI1yCPLAxAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxjPFWx9JhNtFlAdEFSeF9s7pCW-hn0CQTiXVfPF9WaUIUl24hHpsrKGmqBHEtv3oxwJcWxEYUtxCO8vbQwiU3ENPvkdn6WGFDNo8CV1EnyWDOU58d0NPNHSj2VkBV2TlI3ID6SaMMIj0lmaukaSgiTtuUMdF9a5OhtixYSFWaO8bL03csK55lqW_DrG2yJqD7uKBuccVVjUFQzZjNJh9yBsUnQ8BjeuFi2IegFAVQGa5rUnQudzTL9eDqbH4Qw47xzm28Cyq9CVFj26zRg5EsMYYwN5B4WtM1ylCEU9sCxJMA7YFCXIdZ0Emfb_YZMVUpkxRXZK9f2UqwvLvOl_Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWDNPb_TS3luNPz9ML-4ZWNgYRLdBi4IRon8Ch0ttEhlGHl9pUu-txttGNvRFpp_jvA0YGEDaReS2nu1L8jxIFSXsfVkXX5r5ksHlQK7oyqMEt8aNdqzuodxxzBMcONl2kQPXyFm3CeMmz-WYxGPAR0Te9Cw0U-8cde1XWjopWDo4wPqBtFHvdA5ZKhRzc7tLPhemD2hE79yncVxVQrrQdSR32obtWA0Cg3jBRwxDy22hriJQE9B-_3Dcwz-NdGRdMX3Fi20MbZ7sa1xyM--Ut51CN9oZpWMOUU3m0xYqxh3BoWuyxQb3isgt0MYjbRbJr30l8QrEpdhurHpOtybzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clIowJ9a-eehDm6Hi0A7mYN321FP-b1R7qNUw7f8xSAaBhw8LDuixwuT38qu6oD3ZpPjWWohvRWIKBpbcRrUUTNysUf2d9f_6nuIXxDdnsKMYjfCPsk8kjXyp-hxZ_WJDvKDwuul1S4Op6m8-dve4XSRkj0HQ-vtRdu0XIEOq2f57lq_dBnAkuZ6mhbwSBeCTSYxjevAtQFaab7vJdgeBiEhp0-w6-c_K9NqRtJhtS_UhmXBNrk71Bc1-gAIBfqfiAHY70csyUJZlxNdj8HBKNu7zApL9v1LNrY-xw5MNR9OT3tVd_VSsfP9msA_FwAe-RDvFVZ5dvZz9D3Q3g4rZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxsjzm9zLbJRyGyLTNQXnycQlOo-SOtueIFPdF00XtDouAPVxY2AlLelWxwSLaRb3WYoRnKf77gXFmm3r61MjZjxZOCzRPkYtSlETKA86U9IBGaj6LhEj-t4w4zoB46uv-GdRQhjM2otXAgtA_5_5VZJi2HnNqlqM73zsquVFGsVwVSBP8UP7rdJV8_7h6gN41LdZuSqaZNynTipiw6yzhvOzDHgj9DyGEQG9YVlv0MebHri1o9LuX-puEYSGLtMATqoP-LqSKmaei105nUP3FZgcIVp96MHXJHI0WcE2NDzgD-jX337IBDiv02d9XnsQhy-CCqFzrPm-XjREg-aaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQoYdEd9G6gDzHR7f3PygGUKlypLLUc0vGQTAx33NkWRUSdLeKZMScr5JPl1yX_PRC48we3YNevsaEv5Qo6VwH58JKJt37S2prAy4yB1OSHnlyoqJKmwK66OYaiibLbI5_uI34LKsCKJaZ9sZFxYpiYp2p3dFCp4-rlLVSUTZK_ryGWT0A92iy4H0o15CqQvFBfRtY76uenThr7yPzJajmZl0B8piMnYjpaGW6TA1hlCqiTXUBB2oSnqic6z4bDpDFoQADiN9aj65YHs8Cf5JW5dIY--3GqTdfMaAF5sWExsvC7xpLIRMrZvpbkaPNzDi2MGFrWHBWcFByXhDU8-kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7SnBFGWwaWCl3mIGt3LpWfX6PP2oFswWl26EuGQLfwA5iwarJ5RSL-nq-h0NhkCYb9TnYvJxOaRGbUHH_IFF2PZtcb7r4UWBkLrSn22zZ3-tp-9_r4NNaPZM26eQUJ15iNQgaO3rdZ7e38-T45XekQmo0K2VfrA3tRx5mnUONy7jC3KfkJ5ZcBl8viBuwGsv7Pyoqp_hE-vpmsHdnL_4aiOK72PLbkKNHU_5GsMmC9opwmyuvSYf_Ww62Ib7xxktSqm1m61_3uJhdM8XvmyImeZN8nQKODwl5AMeweCGUtCWvgL4M3n6oleJhZKboFkcvNvbrFFJxMb32iGtfWR5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP2MHIPQ3swA5AEw626hCp8Cf_TUG7J0AzSvmRczPIIDcVTldzU_AoT2WJyKuYJogV2NgP--L_oOhkj7Sky0_VHBSi3H2E3jyDKY7Lnwr4VKZPvsvTitwrLwwWURgjD95SRGooUcT9SNQyaeb4liGQC3XkewE8hBRflTYkeqObGavvzdqAmkLfoKJJqnNwOr764eB2y62utYhu2ofSLi7MsNcYpR3p54ohMiIR_49zKyzRllw4rbf_g1CJ5hkbYLIWzKa0gQ7KGpIWjku8Gz0diUD0tSMc6QGgfzGDOI-f5Rdf3xB4nRENVir0bKewc-puHBRRlLt2Pi1w043DFEgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhEFiDXlzkJZvrFNOdhxvj-B7oaTRvwe7nj-_rLcidVxmysNDX4aNK7_leLQVnGEO2aRIiT2hQr1JmY_2PBHr-Cvx2vI2uWH0dFUm7I-U4fOdknTL2NxpZOHSXSnO9a2Z5rPaJRpH_leMeiPOt-SkWkJYFl7sctGbei-WF7FbHZdgnaRCR2LidFEBTMre4-gyMWHnms1wt2AsY2iBJChpu4Z3cgCPNMS33NwshLy2KOd2ytzUplUUE1_bzcndXigu6TFQgYkH67WyAv7qHRJOyiqou16bbUMmhwbQ6y2S-DvVKHIIlv6iXoGT5RqK8NAp-lVdh6PbeLKOGHvbbqJ7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ARy8R5DveKBkSFEsOuyFRg8-n0WPUng9N2oAcCsYp-dYcFQfGrH70r1QRHO37S5OZBJPvDGRqtQM-VmcC0PPyojuX-1coJzn61R8iRhqG_4E23Gocnrj_k2BstnrWfO61Z3EfIwDWJukgOXz-6AkEaJ79OrGam3vmd_ihUvmQf8Dcc7Bav-fQkOCWmbsFfn6h4VCBlGCHcElqwB0M9WVuo6k5x4024nUdKqR4S4hejOHbxOMYxMrVWxb6pbMI4Psnbak5jXalxr5NdLAwQD16dTcvIqg5XUKC6K5cQB072ZLOoamElydQYlc7qnNEcB71_PZekmzZjt5m9kWzlPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbtvctyCUn6R-P0AiHwAWf_-lOc4P053YGjC2Nw_8nLHjklaW4pP_a8M4n_GUB922K4btoOSsRcA0iRb-Q-I1rnoduH1hvrgqQfTunCgg7da9K4gYucxQ9LJFcKVyCwCkmjKfe4M8g1nCY3d5wKrPIFlmcvpnLB-Lz6lpVZzdHOH4tgXD5g4ZS8udq-RJWInfONlUdmKJH2H5ixUrfqnMqJSg8fCYB3WBK4Ib5_1tBe7j_PT7BRU_F6_HM4Tn_mAoJXH7ONbCyf8O7R8yebX8eOPJVFYHl75EtrbYgu1D1Yf5cQGvkw8wpBComVyvHKQSyO2eS47VQWpzCYDNjRPfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMjrD7GTVsTXtTkqHrhIhO5aU0HNylUodkvycGLA0zLJIilbg0mjdUVeczNWRCM0WTcPe2H1aMvtQRpRso_B6mTbGXnKAYacSQrKaYXKofbxIpZYXmXdA1PF7l7loDGMWfj1IBLrHPuEqpeMHL_RbHvz7FfLlNWUsoSmWcQVlmICBI31VvqjZXQBxHptlyAkr4cUa7tO-Yym_w6CyTBthHUfpWYOGPQwwF5vuLwt_rMwDPWtUbKByQ1T1aHbVecDz5SErLRQn0O5jDwD324YCOmftKa4XE_I28VAjzEoyrUoMZJiCwpC2H1VRbto7R3uyHabJ905oNi9-qxy7ObE5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkpbKK3S4T_bnAdsvfklq1RVEpI8TWKjA2fl7bUdxcKiqqJbHbPxnNz_fxynAFDnkROe-Pwbc24cGl14bSti3nrkhqUiUIk3xzSrr8Y03bPvlYqw041bVz_LQm8s64eB_E-8J6MgdyqjPua7oPrl23Szi1K0-5JMbeTwe5Jgp0INGnajgl0ISkphT1vbdhp_4BCGXNk-9B4CST77Y6H7si1hFwCBQKe_JkWoUuG-KQbU0fSy1yf9h_DME3zFMz7D97_ZU0moMAM846HxUiqjNUqJailmc_FV_0-q42Yq2uMIxf4mY2dVdBL9_hzvywt-oZJJhWoS53BRvLkJ8v6igA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY4itqET6LUU8d1YFgN3L-5G4Cc3GxYqj2CYkOcy7QVaTmW8HLTanhSkCw9Y26_JTOAh82c_8WClo-Dvp6bRgqkSmaoLllnPqvAaAdmoUoYL-C_6svHEb5FiuHVqQqaz-ybRwqdDrTk5LqqM9ALPDKeaXewLLOjbv9oyIZfN2OvHZEFdsl3gmWpT996BVg8-g3PJWIUkHMvUwRD0aE0XG2KssK4vlDSdJ5Uo888wRgfQCWwo5CFarsBnUT-lkFNU0dteu0n3soy_QtZeZWiZuUzbtnz4TACQ5sgVuGzOeIKjMzb0ri83tdpj6uqJkFJV8BA3DWh5h8BcdjV72STwQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ij-Cwi8PO1HidHhNE-t6DoFykVMRuNYuOZqJZ4slm4VIzjxg6Fx2DeamoIDbd3N4aA8SBhQaURw480enMSJG2i9xHP2l-Uri9jcasxNl7nnn1gTEFgQ_8gtSVsZ8WZEXclH03aqFS2HUoEwZ9qqY4hwu4kp4lTEacrcSnxDgX-pjQOrLO_3LFARe_xfzYfyVLoXbM0mSs3Yu9aR3n_4CkIt8ywoi4AI0AJKLOurczLN4UzOFeHK9wu5bAqN7wvbFgbYKKs2Onsae803cqS9nJk6cHqJcdo6D1MBPhp0WShuH3p5ozgQdM3-QFHneM75nfrBjXYeQvmkX57Oz2lW_VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jarl7PIBsAgOm_GbIquHftJVSW9tCkT0jbXyzXYZnQ69xd0tBsWqRsZ7veV2XZn-MuPIimxiH8Pzyzl4OPUP2Pqjmmc-PHejW1F0GdBkS5chaBwJAss4grAeaIt2_B-FYnHGaYglK_ZTbIkZyosm5NLReUQvjdxPN2_Usx0DQq28ODl4ha3CKUcTQOn9951EqUf8uE-9DBcZXh5ajvPuIxcqVrXoLWXBeIOVvX8jlVpuvW1eHli1ajUOpsD-3J2Z_OOqjppjKdrRhAemS2Au6niA9XQgLM1QuQTQFlqCrs_f3OfN-YvZJ-8HcTnlleu8fVFeRZydKDkrzkm2rj0_XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrjwpMSr-Z9HQvwoodqtvBWEQYYeWuTn3le8tRlmM7fqfZHJ_LZDZ1s68VB020dn4o_jM-fX9F2FG9Z0yaG8avLiP34sAmOzdjqhz2DzcgkO1BD1wgWHYFi4CHXXEZfaZ6l3E-ng1JGCwCx420aykr-FxQSCht_jaK26k5oNZ1VWFrnr_8JAdBDLU_8KWHXNZ3iFlK5jajOP-n_qz2Ay-_IWjM6RSbBPqO8s8RnIfjhlPG6_nyKOI1wQCuasVsAOwiZQeM-Mmsc8jyDy5pNsb0UHa21nTmyOZ2DeK-4sBY2sG4vg6HTKO3FMBurVjS_xWA7nQK_LXwljEk8dCqgDnQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=jTCS-IiS6Md1pBkHyNPt95oJL5FmrjEd5FrdghRD1_2Ot47PHhugEC3crxvwxFnkW6n0bjyZc9SkfRlrDzIKFOlrkeFMk-1Q5uWdUF5J2vFHqCVEsR4wCZQp94YyxQnGwtFZMPMN7iISbtBUbMGcwsyro-MRHnR6VRaNaGeXroP4ypjkPIHlHdhMQLSAgMbyT5M9rq16mdhgS3dnB73E2WQv0SqLC8OKKTqItrM9vwhV6Ou6-bQWGWnppd5VLvK7vYrkFgOWBMHqWBVKjgHiSA3PaE_S_3FT7suges8H5QmRlVkpNLGzwjPtOHtjyUq8Y77UA4B2RF8f-yL0elpw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=jTCS-IiS6Md1pBkHyNPt95oJL5FmrjEd5FrdghRD1_2Ot47PHhugEC3crxvwxFnkW6n0bjyZc9SkfRlrDzIKFOlrkeFMk-1Q5uWdUF5J2vFHqCVEsR4wCZQp94YyxQnGwtFZMPMN7iISbtBUbMGcwsyro-MRHnR6VRaNaGeXroP4ypjkPIHlHdhMQLSAgMbyT5M9rq16mdhgS3dnB73E2WQv0SqLC8OKKTqItrM9vwhV6Ou6-bQWGWnppd5VLvK7vYrkFgOWBMHqWBVKjgHiSA3PaE_S_3FT7suges8H5QmRlVkpNLGzwjPtOHtjyUq8Y77UA4B2RF8f-yL0elpw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdlN4K-Wwv-HTNdmQgjarlNu10pT9CJ2RUwfH3ouLPjBDToa_y10Bd8nktxbuPLoQto-nIHVuD4zuCzedws2iATM80x1s0MglQyKhCWEPeqFk-lgAfP40UV-BS1Gcwoqt1wnmgAoLOW5rnjYA0hOO-J63jN2Jp1jehzld3MUhWcP6MSc5IVSPQAxn9fuW0s3knis6ZL-ozifIBroxuzUJgDh9aRiTgrtE9vOzfAESE8QuvpW7tAV6UTJnWGDjmPnpBnFpfACIF4gbrdo7gbJ8g41hGlpGr-NknBOu_-RGLiJgRVlBdtV2iu5dWj9n_CbkBFSIMAmIoLsg2Obv813Uw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=cYfCeIdHnGSJefq_OJA-ksYMydwOkUP2fgYYEu6xXZUN7O1dTumNVuMJIvG_cIK9Wcx8jmo5q3OAiqn2Vw4-RYmGxpMJFELDxi9JN9IC_zVxbzJ3PeMSa7WPgT-Tv0gvsG-5yUWzxv8POQXl3iv_S6FGwt0wC5gfB9LRvytkTVBzwpS7UIoxxOg1UeIfDOywC-opbQcW8eGHcxysLawC2xpKG3eVcY1twLZMXs7MhSom4oY_WTDTeelx_yaNWLFUJH2wEsjjHC5xSGM-tP2pxxrGf6eyQD1UCUBblH5b5QxJvxotNP1kyci4W9q5xmLlp6dsn1kjfDwwuqPN2m_UrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=cYfCeIdHnGSJefq_OJA-ksYMydwOkUP2fgYYEu6xXZUN7O1dTumNVuMJIvG_cIK9Wcx8jmo5q3OAiqn2Vw4-RYmGxpMJFELDxi9JN9IC_zVxbzJ3PeMSa7WPgT-Tv0gvsG-5yUWzxv8POQXl3iv_S6FGwt0wC5gfB9LRvytkTVBzwpS7UIoxxOg1UeIfDOywC-opbQcW8eGHcxysLawC2xpKG3eVcY1twLZMXs7MhSom4oY_WTDTeelx_yaNWLFUJH2wEsjjHC5xSGM-tP2pxxrGf6eyQD1UCUBblH5b5QxJvxotNP1kyci4W9q5xmLlp6dsn1kjfDwwuqPN2m_UrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5jQJL9iqw42LeCtrY2hU-vqPD92Vc9Mu6KzrXrExo_9AiHNZyDOy2HKk_nkjsd1mvLsv9nLK0LRqYaYcDY3rdnPSi_Qxmz1CHR9Kofx98XwpQNEELbvtnOu6e6r80Djf3bB-P_PGcMtMttz1jt8uz1I61PsGFgZuPwkgphra46uTOriC5wDpgAs2hq01wxsRS37Ct5cbcUk9lwMAsdZINg5XUbVla58ws1Q2EpluvzKzR1SpN01Hjiy6msN2wejfIkpmynBAPs3NpkFKptM8GEypJjKCV7oYzG7dnnOYQJWLXIf38tHI362lq0DZgH69pu4RDXKNYWkGPmHJFA8ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCDrWROEJR3Po0DIwqkz31Cpo9DriWAVVW5uMtfhhhph4FZYyPt6izrj8MSUkdZy8pzOCiLjjzVGc0-6EbRt38U-hIUtbz0c7CfoFzz7DJBqUPbgBNAtU2g75fdLQNtkYkS1vrn-xLbh3vFVJyI_vpcatP4t-xe2E3lR0Y7soJFL9avqsXYqQQDQwZxew6HAJ1-U3sI4n2ktd5jvy5GniwQpZztbHGLt1luJbaSqDI7Y6pcpIghfX4cdQhiUZVmgv2CivWBMVBiQCKN2dG193rZiHm7gtTJoSLT188eW1D3WYFK3TfWYQVM5wibVCz-kANA7sUHjg0ARiRQDubO8MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jG6QDQFaw-A_l6rsFOTpeAwsQpet2waYhQEMd3bmVoVWu5CGCbRVnU4uAAtZpknfk7F-LL_njLkej19uowOb10WbNOkovJM6-GqIlIvel4WcnZgcbiUK9i50Iy0__-9Vpnp4mFHD2uZzjAZRJAXG6R2_MgUYSDGhUVF1iAlCUvGvdNqkf3u57ipIDft2_dKu68KF-tZRr-q-HQeu6gqsN0d7ESlkBVx9Hn5UygzzpgDzLnbDy-6AtFv9-pdqbc9zCRLONqjE8b-Y6fAYeuucjd80YzkhZHfM025m1ND601J3CHFXmoyOxo-VtyeltbiL3T4_X3UXUdSjbTpQi2hBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maupjvTwGvNBF8lUyjhtbPcAbxOOcULcQgyFOT-JeRnge-aSgzzbvzR6cXUc68I6YagLOFyKy5LS4pNC16AStF-Tuj8ueVwOodLLiaOWzRG7MwPwm8EYXoTWfUNtwVESIPnTeuYFqGBIcDefrvyM0S-HydPSR2vkAn9bJyvbSG-AJPa3zTEgdA2VIIyhFVmribp4Naa-h7EHjF1xYrquoaAy7dRixjhEzBvuHUfy_yh4mtkuurWHtRyA9T-4Kw3UeCmEdN1SE0mDOCpFNKCSOELB02d93glPcctBMnnnudga-6ALI9LIOcOHOnp04U9peIjANxAP_tCXDBUVKhXMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4daaBPYh8j59SoxgcuHAMtv8Wdp6GqqbEh6I-ko1uL61KX_I3uDkm6AymnE3pP_i63_j6BYzbvTkY7i16g9nqC6DSP3PWx4s5mw1Cos7nfS3FsCgF0iyiXva_9-gYOgCSjSLQtMGsQTv6F3-AnP85l3HM1ljN2X6-0SD3WTrEZcKSIzUME57selVoevIsi5MQ7wTVF5tOcdANKMZbQkN4zCZEtWU8HaIcmSWFP09KyI0EU2mtgaV_4uEIcydNh2r83IxqI2zdwWYwQUNIgE6ZhnN8zyfgZkYLSYQu_BUHf17K36mhS6jx6f1WGBbYChefFi8RntbKNdJ9_pjoCs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFH_R7mRRBT3bvDXjJy2xi8D75gA5pBtHR0KMsZsobQGb8XxAEto2kU8K0m2gcW9bwHTDiMOqWOvQEBsJbVdTsc6S4possmVsEkEu0pX4k7XW2gDTrVGj4VFTfcEvfi-0obJ5KGNez2uz19v9IgP513LTtwb5uO-Suo9LoaSphEdRgEHq3VaxxYx2GRhxxC0xKQQ5UghHmOcJ8YS0V7gdjt_hqK7sDts3j4HCIuIyo7buQP-fNdzw4koIneXQzUe1qD-rjd6aabHCY5rEMX5SAj8B4UbjpgrmoO32E1MdRKv13lqy8XMcsX5es44lvdqqSKFtEv2MU4Zp6qScQNiUA.jpg" alt="photo" loading="lazy"/></div>
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
