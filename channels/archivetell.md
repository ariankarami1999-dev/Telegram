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
<img src="https://cdn4.telesco.pe/file/YuSlRbZGYlrwGtrJXIYHhseK9nZoBr9bmHpHQYCqWK4gKe4EtLqAiVAmRV4xXJkw7k8KjCzbvruEg7BjomooXEGWm5pmIqbUr2GbHaNcC2YFo76KZa5ELczK3hkcVLMN2BiWbebpHTLqEzY82CRYm-Om-ZhQkqchQXF5C2NWSoAXScx8nRL3ZsxggXPC5JmPIXomWX4rqd3tcFQH_BIDFTOiJX908IlDvVNWfkgbeDrU1aYvqcKl56_FwaF1jHD8OIAz0KqUknegn1VrZo3TfrMTW-DxdlrZbz3WUpmrtX03oZeJy0EL-7-SYyKbSpdz8HK2KBZLR_MgMRAPr84-UQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijX6K_tbfYKNbzy9kQbQjYWp3MYfbFJaEwO2qfk-ibFq577RRht8RhTbV8gHbc8MaTltWYY1DnDRdVMQPRnxEPuvWP89q_ppOLsuZ96C090XqiveO6FbjbbXirPr9skuz5g9fYRjNvo0TTtfAMcPRw1TnYu-SQI81StR_OrDBscH30sf3Qv6NqBfnw232d3jqX4pqgjQdRtHOUW-8abkkICU3LhgrCKokx8pGs26HCNNLg9yG8J-_ff24l8_3MgCTptZiloGnnMJmv8Ff4OicioPbmfRNHEkwYP3uthX232EZG5CZdRaQUa9K9PZ9Mr0q7tKm80XXowCy-tVavRn2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF-szmxIQtpSrP1r9-T3Y-3hC6_z3gyF9pdlj2XrsXDzGrLoZK_cvKutCEGdCclucBVMhhdm-ud5plDl7mQTGMCO2Q0w5uiUfI0hP2Q1l5hYNT105fgU0E0yfSv5Sjgv0up9CnAbSW3hXrOC_ym28hL3Htm2bwrsCJYMajo0o1mF3cV1f8Vij82e1mSDonWa8RvWdfZFo6Tz7k9nJAeUyfIznUBFF-NKiJpTL7W7wZb2hImG8xnLRhr2iIDOpgFS-jNSVprRAX94FJNJqfRjGs97jYcpXZg_jLlEdHXwOrts8hP5rvMi7ln9mHfbUu9ENSBbe1R25UVuMfuknriFvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoN4TjuNVTo8ZVLvs_2RhfbMLJNZfPyPtsN0ZmL3lGZDiLbL3XEO6pMWBszEgdYrak9fDxuEaKX_TW77IbpXM3iqu5rbI2uZl32SATKQBvg3faJAzZauHfMKD69jdVjEWNx5Pa_2Yew5WN-E8vJqohjxb22Plg5GNrzYYRnafTKe3umDHMxhdF0iLi78U3xygQfvA61uHu0hXOwDb_PluJ_eCXtl-2VkwO8KbiM2VlivubS4mQ_Vmwe7n_lQP5cvPba9k5qI5bcyHFwWs7BYqzirijhNEUhHttyG5nQpfNU2IndNibC_KWwanOEV6GeFhNK30tR9M6mWiVlxTTOPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avEAj8xVHtivy9PRO9fChk2xoRMQwWLOuDptrLL2BfjZUJDmcuZNuRsDNw05hoAwRVFidrw1DpA647ctasbuj6hwNFWsUtyETPEEGQ8RvgUOeJ9GCahNVmrWsfCE7eyaKYdjwyPnr9-Dg2TliTWuXuCR769ab3hC45WBYNwwPjhccrmgY4Prg3GPxMgRCOlfcP9pCJ1muLP-uN7GxndkUo57fRfA199C06BYgwzCioRm5FCaWYsrAw9-3NJqD7oxildha0aXKCXI_HQOHytn0_wAZegnXeWNWb18D8oa-ipnOY3uUJlzrXSt2k8QE-9nH2D0TYd6izMfbYuCb1HJWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FltTDLmFavCU4dVsdkafl3rLrG3i_dqJsND2DCXKwS6zsBRxo38Fxg5HXrV_yrNjd9y50B1NAI2Mo4H4PUSclyRQRTTa57mmng5KKemYguTl4OdO1cqwYrrdWZ_v5foJj74dErYeau-K17mXB2N82sFagw56m6sNmIKjNJHhICilWEIv__WFGgcLo_r7h17KYTqIeG4xyYNcQbA9YkVwY6tOjY2yJ4lN2sGshMkcIftNDNcy6MphHqsNoEwjTiW0oUv2LKoylso2SqbNCVBdr5PW8y7vaDHl7Gnp2OmC99NLHAWdgwjnWG5yj97_47lcac39pT1gGdarwqY-2I17lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTsLl1UNcXbMnlGUyIaVsJui1p45Kodtbo3x5E4xwIZjIdYbxz19d3TZjK1GO2SwANFlwlvFKYGtr9Df9ORrna8UfrOp8J9zm6pPGhS2s3mdadma6DXwlEnOSm7yb5n5hEDdgn-66wr6Jd9TOsfiUG95vdNY00HFSbD9bLQklM7jp-HxOwhMHFq74HIVoZmSk2MKh8trKEZfLrmF55mE4uKbDbgcKB53XN_9lanypLJjo_1XkQbVPZoAhOWpB6LCpKFmyvPtuvmMLYxaq6G_lwCBDbZCDBZEAwdj1HVL6jSRiP-Q26kv7q8HHeFqyTOP1TP8nUTAGowWBi7lj10Eig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7vtXAxi6qhMxjvpT2l4gB_uFo70B7kuig_GshNj8CxCKg7Kxt5LDwW_zoFtYJVGHjbFFSxqVxqIuZXtvkIdq64QGwPIxrvMNKv2oL76YpGq77dQSX2_mtVPS7KAJgA7dyhQINncASOXllMo5r2DaYj3I7w8pDDZ8FXgmV2m79fwjbeN0pS6Agyno5mMEzLR09jW-83O6RbloFXdle7Npz-ANIcaNgpa4Rr6BzRIdsi86k15x9LdG0LIsUBBb1TaclhWDJsC1VjiXx9QHxqlrh0SMnI7OB7Da0AS0e22KSfJ31ssnHv2ErxD4KO2AbWZmLjHH0G_-CWUjgNjl2638Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnDO5wpXGCelV_6xINJVHjVHCfUaiAWzwuY99VB15YowXERGvdANW7MwqQN8OCD6s-0zuFECDDV74jIbqOiK_emTwMoQywK1iJ30n5eVl2wOXMjiPCfT2LYDat2C-Zmp6_ns97sR3lujPzZO83YTpfSBotnRgoA-0_ekOAMfgwmtFoOvJ-t4cf7e1ZpQv1BNUh2ilE1-O7yKqqNc-CURgNwtxyZbBkEJVYzSB7E0QehIfiyVmnZNyeA_PxC34R9Znvn1pEmWZR6wIKnI1KfGx_zg6QwC0z9g4ow4pI1xew8vedaacuE-w3arm55r_xzsgUjf7crev5G0Uqi2Irj01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=cBvVhNyrKQsS6ERkpP3KAkcH2K725FDtCOJD7XLNK-SBY2KFXqkExbB5WJpCgm9ZUdeHMtiuvaP9un4JNBRxfEfuryMI3KA5Fa3sCUfmDZL1XwApe0u8fnULqcLd6sPYQpt2g8ShxtHSmBGxGBT3nZwbED4CxNyxQg9FelAvI4IiformXinWhtqZmIkjamtS81D9wXK6hQwG7gExzGN8b-trFcqpsbugXPXQsd4-U0mXKWhb0q8KOkMaYAbVWzaxTAVcPrvNGXqSWt5LRLK1m2VbzU3bKRyaY1MW9wdosD3KTd7LR2-vp-mLQ3xu3DQZZk6EPPwsnBy7dOjtTP7N7hWe8yRKMV84TgLknGOxiTxB--fYnJgm8c78e7NFmpV5GhXvVQJY5XzP6disvVvs651y5WYQhZlCtqZP3MEmCvJweeVWmnQ9xVMCrbIelJcNptaVosT9lkfesWTPkHk3N1YOw2NWaVQW8LxBHPW-ZVi6O6W2FBkPaEFeC1Pcd8ef4dQDxYEjLeeFkot66nhUzPxvZlQBlWRsAk_0KjM-VN8md012MC-TLBZKtO_sJ-9iGsQs6lH5y27ckLGZF6_fuWVfHvTubsntXsErnwvIb665VbvAYMSx31-G9xV-NXtDEafFXy4byrZNvLAll-yV2lUoIWVPKwBV3KX-aEzKJ-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=cBvVhNyrKQsS6ERkpP3KAkcH2K725FDtCOJD7XLNK-SBY2KFXqkExbB5WJpCgm9ZUdeHMtiuvaP9un4JNBRxfEfuryMI3KA5Fa3sCUfmDZL1XwApe0u8fnULqcLd6sPYQpt2g8ShxtHSmBGxGBT3nZwbED4CxNyxQg9FelAvI4IiformXinWhtqZmIkjamtS81D9wXK6hQwG7gExzGN8b-trFcqpsbugXPXQsd4-U0mXKWhb0q8KOkMaYAbVWzaxTAVcPrvNGXqSWt5LRLK1m2VbzU3bKRyaY1MW9wdosD3KTd7LR2-vp-mLQ3xu3DQZZk6EPPwsnBy7dOjtTP7N7hWe8yRKMV84TgLknGOxiTxB--fYnJgm8c78e7NFmpV5GhXvVQJY5XzP6disvVvs651y5WYQhZlCtqZP3MEmCvJweeVWmnQ9xVMCrbIelJcNptaVosT9lkfesWTPkHk3N1YOw2NWaVQW8LxBHPW-ZVi6O6W2FBkPaEFeC1Pcd8ef4dQDxYEjLeeFkot66nhUzPxvZlQBlWRsAk_0KjM-VN8md012MC-TLBZKtO_sJ-9iGsQs6lH5y27ckLGZF6_fuWVfHvTubsntXsErnwvIb665VbvAYMSx31-G9xV-NXtDEafFXy4byrZNvLAll-yV2lUoIWVPKwBV3KX-aEzKJ-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubrt0coaOf3MyMBDs61ZTmiUIBXv-pMfzDiJZwXKLIq7at1-g1DzjHE9V1vji1bf4e3bXTKjyjZBwV-fO4VyqSxL-TYp4VT8sImNkAoOzBdUJtvNPxRnLg5uCcSpR8UGaNh5bumPuLTLtAzc7IE2KjUFUL0_zVDBAyE-A3HtOQh0veOVZzedSau2LCBZGpCa3lFeOxBwAmFTKv5Hq09kgxZJKBLcLy4Wnv1PiQV3YLFh_h7oMASOsXnI2aKu5rNZTHYfGHHvErRoa9Co-gHYnSkAGk1l6VUbw52Yy1jG0HWmLHBRD2dWFYJkkeH8UVs696H1MllqtqHd2MVfTweFOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=peBMP9wr6wFRE-M_VJGhcyD3SCG0kLlF_vZfLV3_i92n9wKh0ggBV16MA3QdPVoWIa63j9B1w1m_ue8JrLSJkI5FSvsdgO8DbEZ59aO0EWrK49Rzb_hd_Yq_YJAsqv9zXD-hQ3C1jBc4gYrCJQVCpuICknbctpw7HSppBTQlAdI27Jg8s3lO-8u9Yfyup4WrK3oc-TX3iMreYC_yrrOazxGsnD71zbLY0mjtwuKWWhLXjDz3b09gBq4HWXrrEOMQHKCk0bN0EwXg3RgsH5c2tpf5IjuL7K_Y97ynEkpsddUeLwFjQV724QpPiqndKYuj0SkBt_-LrVDE0Aus1UZn1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=peBMP9wr6wFRE-M_VJGhcyD3SCG0kLlF_vZfLV3_i92n9wKh0ggBV16MA3QdPVoWIa63j9B1w1m_ue8JrLSJkI5FSvsdgO8DbEZ59aO0EWrK49Rzb_hd_Yq_YJAsqv9zXD-hQ3C1jBc4gYrCJQVCpuICknbctpw7HSppBTQlAdI27Jg8s3lO-8u9Yfyup4WrK3oc-TX3iMreYC_yrrOazxGsnD71zbLY0mjtwuKWWhLXjDz3b09gBq4HWXrrEOMQHKCk0bN0EwXg3RgsH5c2tpf5IjuL7K_Y97ynEkpsddUeLwFjQV724QpPiqndKYuj0SkBt_-LrVDE0Aus1UZn1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgcFhDfGtySj6kIby6TcVUy2V1VGfXedYSllXXpOuYUCKeLswNjKIwJlVLUgfON30S3wDpYxLXEyjpmKXMfZSREwT-Zk4VvqtY9SrtYrSUJs0tW7d-yI-wGTNxzkylUJJU1aFztk8oVob3EyBWcTfD4z1Eb6GnNeWemnpmt4d73iVM8K9WVwNRNc5c0BvQz3OhqFb8afrdzmVRWP2gk2BdZhczpeSyNZXp4i35C_FEp-3fi15ulGgOz7XhMFRhRWhzEN9WBn3800yayNtUws4i7hAqjHLu0HT0-36sSsY-nRiCNoOMgRJcbDlDzWIC8yq9y4ahygXI90YSbzqw5ogA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=kQs3dtc1LW0NiSm3MPMGIIuH7mZ4Pyk81yziy_ozQwNEkDvbu5rNfyYdpQP0dfn0QyhJcEXGrzxMjHDEGxL8G4XhPZjUPzCHLrCVi2YDIRseeaO0wmHMgi0XPRg3iHiIoxXlRAbJGpE-8S92CIMCG2z4cjHDShxZD7Z0UYa19TGvIqGBnmQBHcp83CMEglrEdZIrsI2DQibf5GqcHBCkgyM5XR8IpGK-YDdc7m_QJXGmhmCgQztpX2I18f60IMzhzhM3PE85NZSSeXXJf9f0msguBHbVVciS-cYipJq_1TBgmc5XnCzUwylliaPVn00iIV00W64OU9YwJwC4UeZiYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=kQs3dtc1LW0NiSm3MPMGIIuH7mZ4Pyk81yziy_ozQwNEkDvbu5rNfyYdpQP0dfn0QyhJcEXGrzxMjHDEGxL8G4XhPZjUPzCHLrCVi2YDIRseeaO0wmHMgi0XPRg3iHiIoxXlRAbJGpE-8S92CIMCG2z4cjHDShxZD7Z0UYa19TGvIqGBnmQBHcp83CMEglrEdZIrsI2DQibf5GqcHBCkgyM5XR8IpGK-YDdc7m_QJXGmhmCgQztpX2I18f60IMzhzhM3PE85NZSSeXXJf9f0msguBHbVVciS-cYipJq_1TBgmc5XnCzUwylliaPVn00iIV00W64OU9YwJwC4UeZiYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1CY4eIDlSaqT28sO0Qx0PVy7oFRSdl3UIdheJFWCnXUM0_XGgoniHWVS9t8_L_GG2Aoh8Sgn40KfeyVXFT6-qjwznl1U_WaZ4CetCH6BqQH4CGPGZyBQpVFiYzN8nlyHUfnOUeJf8ctOcjujnF_1TysvF-JvJ_gMomkXeP8TgkQ-E41JQDwzO3eqlfynLJuL0jaEI_Ryy8y97bGLu1Hiv3PbNWpN0eLTibtxVIZZb9EzQjb_7sX39wJ8xn8EQHFt1ZOX_M1dUp26QcZu_kOzg8DivcyV1-vzLtTjVykpKJQ7Kd97KuT9UclvF8in2O6OcxEbHJAP9aY0sC1LXWR0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2oZ3wRRP3WsaIJlqnZ-OLYEYCibDUvK-mOjflTi7tGSfHe5qifCN-WmdC1BP5oUjjlPf4_VE2tLUPbcO9XKhMC2XDNLM1xnus5Ik0C7asxoEOuw1tmtT756HDU6NKzJADWCERRS9azBNHyFQKQkOk5EuPubXa8OPcrT0e1tJE4oefOE8UWf7HndrcpD8UwAH8S3UvWrTe19kUaj2sRa5bYDZlHa2-x40tC7dGR03r0R3idkqik0TBNF7fnnc9oWT1gSUyGoJkSz7xm_ns62EyI1KQ7_xf8RQNA0bIz5vYFwgkOsABVMpenDzEq-I8iAdrd8a5TYAcfzb3xEHBVw4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNfCxhhN9tliavNlXDNU08rqebOqei3gV4ZmNczJ9gr0g7dRrFZTYMspNnJ9TPawNg1YBFy1ET1bf9gxTnnQfyD6x21Xvz7PZyB4Tgj4i8lwYtn86FnKz1xL0l8d5Fawrp3mbQ514S2tjv6KDPMz8sMMIVbkOQrFPKX3i2mxpfLCenitv3nw6Y-ITCdOCnO_KE6tZ7jvjS5rDJnyExuj46lT4-OY73Ww9UnaVc-BSPSxTI0FrPPP9sZYFX-sAe1dX3TLR4bcDD7C576Zkg6HDogg-qXJ9uJdhvmlx9MJNxNoIRNKHad1XHf3SlyjxWAp4ii_Oi6lEJWNqVqYka8xzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uab627mtmR_tLJdvSKahQycDBBFVGxHJ1_PC3a22hGigz52XLZKQpmaD8YTEJgn9V-_AmQUpcUxfLW0e4uVZqcXJvzu64SuCfirNAuO9Ofs95wO04iZ-CZe6u1Lo9rjZHTFRgjMy_4wDBL6f6P3BJmMCAC6K2STrySlSqsIlqjKUHr3SbdbadVFjbcBF_RmzvmT1Tvvi6KyMNVtcShZtI79w3ajuHYYKMr-dgz6_lSRCSw2jOKFj21YlXBLWM6NqxGe4W2iDRdZdvPtRDy8IN6BYT_Tun2Vj2kurVsV4DQbuZ_4MbO3X8hx3hl-ph4HBqHk7yDOZACEbY-hpPdKLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MD-5TO6icT3MfSrC7Dh-Js68K3zY_AQ-AyXYNEPlyZ1s25q9zPr5-i3mJtr0CmT2JFlf_VAIDWbs8T7NJMeaBvM_YUgzS8k8hKFcfEzNKQbMBQlH6_yd0ny2L7wOaN0BdthEoBHQJ8_SqyFXQ957TtnMIP06gZ1gutQtYA3d_fPxLYfPbUucGGaTkWWm9Nt7WfQcS1fStJnKjrt4RjTyMi92eSSI7ZOqF6RaCIt_T05XmGtqnl8x1p5R_D5uvgYAJ8vy_SaY8lvyIacAbM7d-OJkng5NzghrgZlMq3-EDUytNn5PzbN_x7CU3onLJbKIjRtvoUdeiFcQK6pTAaKa3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FypUdmoLtYJ5ArWlXGRDEPFQU6Ell1iL9b333tMdtZF-lBq55GQ4mFm49v4K4TibH5db42j9Ti-FrGh8JGdF7i80YGmjBMjXPdtm-p0QTotizwUeNZ3zj4mJ4YBLsSPoZ4p-E-w3TbaOA1-eo9avWfn6zzdgajKS8gseyPqmn9eIedA9TPX2vhmxztpBgEbx3ImJu4W572WAwdt0cX4qPadfJKQI22wUNHMmmW70SiXyA03qMvn_ZhX5EVmh6-1FBO4J7Jt7PQ7Dxq4Z71y8d1OA8PxM5XTKGNeQf6oihIzxwFA-UVstzPtlXD-DNpOQTwZsytWriQXUfZ6_KVvhMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=l-JYHCp5kwHvGK0uqnRhmzLsVSeuizB2QC4iGJNiwD_y35CLb4ne17Ir-ld5lbRFQO5M0p0KN-YJczJm28mJDfNP4wLbg81znjvWAwxAnf74rSRXpJfeKwyoU8FQH2ZYjKUamdbijWv4c9lNtCL7AKpm2UJXfTsCb9Yu-Ta_qGU5mIjuVk_8rMkCcEMD_KantHDjGShejwtgyqLJlkMknym2oD1VT4wPc1O8-pxtY-yKCVmtgIZwjH-d5hx3bRMVj1tQNwI_Z_eRH2B0SwAn-yab_1cpeNiLcdeEGzDajFEh0DoSn2EyE0wvOQ_TPKJsSL1WLm1gR3g6lZd28P9UEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=l-JYHCp5kwHvGK0uqnRhmzLsVSeuizB2QC4iGJNiwD_y35CLb4ne17Ir-ld5lbRFQO5M0p0KN-YJczJm28mJDfNP4wLbg81znjvWAwxAnf74rSRXpJfeKwyoU8FQH2ZYjKUamdbijWv4c9lNtCL7AKpm2UJXfTsCb9Yu-Ta_qGU5mIjuVk_8rMkCcEMD_KantHDjGShejwtgyqLJlkMknym2oD1VT4wPc1O8-pxtY-yKCVmtgIZwjH-d5hx3bRMVj1tQNwI_Z_eRH2B0SwAn-yab_1cpeNiLcdeEGzDajFEh0DoSn2EyE0wvOQ_TPKJsSL1WLm1gR3g6lZd28P9UEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3RwYn_ov-NG5m4qrUPnSRum-AvhJ5z3nEgPTJl_-bXA5benHIsPP3eynSDjjkHgpwDPAiMu0Ly9RIoyB--Au-h4VN6OlfoC4CjZ226L4I_KkhbYepVIVK3gKuojFXO-dRgV4tNgd3qTmgz0m1BkDbzp8acQFYfDZCo-EiSm9i7D1EnpT6T7ZZ822csCR-HcOMdprOUuuRVM7DukCUqOjKLb6sLh5-hNhIGzHImnz70Fftc1HOUx0FKCb8pEfs7wm38_7BUighjwZ9eHd9iv9Dru8xAYfspuJcrgMActwD7v13kI8J_mQU5vEBqm10050lMR_S-Nnq7fWw34upO9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6G39-A8r3HD7bghaxXQrNZ9hBpq4LvIXT7jYrL9_ufchAbXvm05EPfOY7GABvLfYwPFfLhRajkcBYgXdPNxVVRP8FMsQbvD7CvoPaFzxev4YyXQXUGweXQE5q-ttPs4sd9DRUK2mkEnv4VALTb-V3RQzY7iVI6hd-jltIYnkUP4aglarNkDc1c-scevVlXrmZqMvfzIsuK1A8t93ee-N-Uo3_cBgdl0oonjOLpNuRGsB0X_WanwVe9uE4caoEM_MHlUXzo4U1V_fsBN23CgW3FmEc5ExLeWkM4IDJnPnJQO0n858f7zEJHRi8Lo9F0mGUJN_hsj7yW4-Riv7Cn_tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha6E6HPcwaGwe_-nDQgzePmzAX5Av_9j1Z_8Y9bN5vQrqZ4rMFf17H5sPXrf6CYrxDH4d61DFukRPLpEgekhzmIlWisv07PrAuFj5fYLTOo0HyguI2LutMtQ9lwAj0zKubdWHIEA670dyJE5TZaBXVmPRbqUy2iqkXb76VWH16FKHZMA0d5got-OA4ebiQmNvEAA4aRvJK2O_m5NKOPbFOgi2yF9N8EWuHwzaG3arkzoLukg8UOJtluwOoctCvOcd318xWJKxslXTTR8TuYrbqrDqBb3NPFowSFxNGrXP0BdnJ806RzytqwxsRAwLAKqNta_YDSr-xgmb1Q9ma2Npw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJxE-ASYZLh4Ica8b_TqgL6V-GaKArw6Ss2geoBas-JfdABcmm3dIrckn80MG779-G-K-UZcrYYntYbMCV68ejuvtZ0CZap_4NT61yHDxZ8kSkU3hoNAVBw6E8Vyhlxf0e46djH7hlnJTg2pm4kizod1p5L1sEeutIshYBX3ldL8Cul6Wu0Zb75cTSx3v731h_tOy2fIq73Kh5u6EBB-qgXq6C-c5BjHxYKKRsdCwrOzHtq28xU4zxAB4SVHpkXwc3iUxX3qAfZKreuAFaLMYzXQNbf3a4GkO1eg5GaiDydxLZSlMMXlXuIETQmo5l7uWTVYQDHXTT379KJeYGVElg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd2hW9yu0vAWC9V3PtTfss0-uW7nTFLpndTvGSpetz2PHt9p55WYf2_06_c5P6AFjs58xZBmsrcclI2xAaT3VPutYzut6lOGTKlb8Hg16IeBUL23Zs7W32yQ_OqFexhg4W58d-BgOalqKOG9vugpAJHGj14V2GrOrMoTw82Lg0HYiubWKU_d2IFZhdlN4xeUpC0wc7Hfqrc1zk_zRPJjEnm6y54MIDCLF_56zIbEo8enM_K-F0sNrJ6VsOZzhm09AklLWHrRoDQmOpsklsocEhueYZLuRJIPZ0dybVrUDblUE-mvIJ2LXkP8VZXwH1_s4MqT4Uxa78EbnhAZm9Kw4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwXRns4lQBak-Ni3oFHvwrQu4yJQhNGSvMdzyi4DLHwdWdw8hUhx-SYNBoqL-pkYAcahJcdff7kWfselkJV1PrpBCaQzippDsr4Xcb6hiXjXTtUE_lwNvf2eJGXvpLYJVAbfOZ6ofeLzzPRU2zGvPGPx9iKbsmlPHIhDptRF3XDvPtGEX9LWkjsvs27Fqt-RnqKpr4GZ7BEgJDiwYhznuv4yLYtKkQ3gAD1Fg3stLq8exAtMBWh8ldl6X_N0U63EXn2aO4Ah0HdQUO47Mz6rYXVP-e265imEOPRdK-CKGWjew860f_B0jU1_UVB-yqEjm8sXR6CuHlqsL8p4NCU0zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F44liwW8VHDDB3o677MP_hZ2iyxK15rvsaB8uagc0fzWSh5E0SFhwDn2KuSdBGRWCevauKMi-pr3C6Ul6-_U1nwRG8p7rzzr2d12zj43JZZCz3bg0eZD1pHdHWl05JAEeeFiYdKKpzRpF9_q26M0koDgGYBL97d28k-whjqw-IhGaiCQkXlcyfv5IGAnCsKJPl7W8BLwa9prqCACXSeL12XHap_0y_72fff7RX9eQ2R64XOrz92Bt63VzF83dJtaOT8p1T3pIPkgnh5JUjync5cYN7KSSoTZsws2yzXr0oDwVe28CS0XTzjs20_DyT4lmNdVlTW1rUbE-MbpWqorVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCxZ9nhhO22hG42BdJ2Cq6QxlCTu57EkjoXX4YIVWsL-n727Qp118_jPXFgtuRGqWEPQfyQKNPfbxiSO4vyxGJ99gKteuuUR1zZLKWCJGO6K96ZI83C00Cqu7Xkfcc1QRH7HbKZVaohBJPnN-NGFSOSEiz7iRsd01HkYpNOWYC_QDKW8wy8NWvKX9VBR8qKS0uoESS1TduMu3xiTqPA8e1Ys_6g_sf3Nm07d7mPbtGxijdOrTLKvYVgZ03UV5bHyNlfX2JCRD7vbdkkwCyjZbC8XB3sujUOcgvFknvvp-LwMNUQBopua6eVouvwnURKopQq75ube2brb63Z-mwZfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU0NirpMUvWzrTuBx0FB11V_1uht-Ci6U_E6iLEVywyAT4D3NyJgR5bu9RJ_bmMKNPOsx9HxvwQNFzzsKsNcqvM-jG8AdXmlMIcAUAGa4Niu2CYOZNOrRlydaOr707aEr2NgbtAfeXXUMbWPDpzkvvMxSWwzXmMcPoVILbLdCEmXOqRnX3BvD9VZiLmsl_R4DyDZ-e9_KADpeI0kyMglO5RIEZIePIAl6O6nZTVFQ9UwFwzgq6VAJcfGnzyRJiXSYKP77SjfyULfE9n4D_t2K76eOhdRFzAXg5wpULbxts8xVdnRuIb1Tsrv0iPI_dneF-mMfHazKw7fqk1qKBE2ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWD_0E9ROxG3ZZmkVIuWRDaw7CYJJcyJy0Sa-BFa3GlGlGBy5PRyoFlkW21NphkFek9vYX9tm9RC7f9WEnK2ohTtsKFcS_HdFuWhoYjpASVlEoGGvTTZcaS8RL17iBE2DgWpW8MR_5096uW7gcfGRfOPVGBKMVLtuznUtZF5c5rG0Faj_eyYPnZq230cBHDwyP7ARYRAVvEKYvdVBaEB4zGYNpTzmABUuRHmF8ihKuqcQ3R0hkokDW2raDa74SIpJiPw5Gvnm5ly3yqDQM_1zjbbNK_SpOU0otsBle3PYgL7VKrvoMVXi4-N0cKJtTlxncCQB7XVgFlcqobm4SfIuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd4yld-w7rDywLImyVyBD_yZHeT0LBd-fGDcz4vpQMHFkzKsfeWgnmEYIKF-HUNeT6IROYJb55pwMlJ7NQ6bbV9TPQfKAsx0ZPv2AgLeL6wwJb2Mo9tQJ5f1YKwm-6KVQA-VDdQbosnxT1xP1Co2wRG5kiXLgufxVYQutBgpSF3qFB19Zff-ia8h9nM5zpbuekeYgp36rRMHRwYnyede7I3NBXAHttQQLlP0wTtaAoygKQN62gEDvOi4o92fN0LN8I-mHyE4KeriyWSEQM2Sgv5knWkEJaQWyc_prchAGr0i1rmrGYGvNGsqv81CR5hr7yn_Z0qT6ifx3tHJY-yM9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEfh46D8LVKiadUDjMI5CSPzEumvFBSe162HSQEC_c0UZZPDHjsN-X6ioUVjNIpK0c5wt0PkW2XWPyP_gma24kNAI5ESDVQ1twvwm5kNJmxUFYx13HrVWOGMh_wDpyeDKHRhFsAEdFR7RQzjGDzIQuTx8iKu44EYo4cmE46b-t492lQi22dgNYOhMxhUxFFBF64xvcliruZHJFLZxlx43R0XgdInvqHXQWNOHvkGmNqzjaVLEtjZAN5qv5ebG7FhsiPUjamvvw3i14AebhYmGGSmIXgGcIJp_Y_HA0GklLuMwTZglL3pBu3uqfTM6ODYSLWEDYT-pnppkysvaM-24Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZyEEb-1TNSToVTW3JDDMHmwpG79yZT6YhEeraK0-8YtQ1KFwxz3IJ7gBQV841WZHRqgkGk_N0PvsOfFtquR63joUDMALGJTmzPnadlgsfQt9UYkiOByIl2fFIxJUrGblti4iJKNyGT94MyRkQ1T-NO3hTDXi4cGPPDjb2LB91DA6q_d_eFz3yzfy2USrSVI-nOcu1aGUxS4pSKh3o0S5jLjXP8dmxB7KZg4LYVfaCEDsh9TOJYLmLrLnD6P3whgYRMgQtSQFg5WFk8Ibrsl-UizrqopL8UXPL42AoyvnUcp3oWNq7Tj0zgB7V7PZ3QEmKaKinPO0Yw2_-EKX_xEfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTQVb8GNNbb9CZOEUS40jl_XzOWI8eMInyWKxjUrMuha5IaTcP_VHK40V9lHlqZUkZBoJ-OqTn0rZ--E54IlCcvROfW4eQ0gPCpcYHTPAmF077AFmL-BXTPHzHYH7tDyoMsdVRB_DYs7nz_L1tSW9lSWWRS-pc99ogbLTpGQjsqIHauGgv8spoIWkthkWNsetxXLRct8QxbqYzcUpCyFAXG9wjvxttPBpj5Hg2N-Fw5_RtPlHxLgoxqjF3A8mDEQXew4-ezMe9UVAT_fSNElAi7W1CpgQqrEdsJsToUY4s-HGjeCR84FRdwl9qMqUf9FbtdsqsQ3G-L3YZ0gOb9_wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0lH47xYKCEAUdjh6UUYUzl_Ea7GtN2UcG2LsLdReGH5j4Xs9Y1qPgjTpHaqPW8mFWUCC2I9FbBpjvLyv0I6_CuUM3uuZgZHe4GpE2O86E9oLpPDsS2_SD4T_5EtJJvkTmNEfI31NOmVLwdjVEE3J-mnyix3t0zDHTtvHfkw9fBeuv31Wz6U1qdELqLlfikKCF5xWEivbic4vepL9N57ZOMRUZmH7GviPujVkk306ak0XTVsw1znK_SmEW4XcMYg0iJyCUZ9BPjHjDfGPzmh6mJgBroBuhnUKWgzPVUlaX7MioMzQo_4fZDF0wlL5hO5_8iTuP5YJ8nMNtMlmjyang.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2f2xu7VCS9Rsu1zPjti4fZdatYd91HJQZggwNi5IV2hF_xlaMtA_W56aeZEp85QH687KaxweRErNb4rYhd-djun8O6HgQ_89BQdtgmWNqWdZ21okqELmBseTxbUvDHUJ728HlEytcEubsjZD_eep2T7V0ScNESX8KjBTQaIMPVM0ZcZA98RIrMrVz0YCEJF7-XQI7d0cZh5HoTz4m13lJ2HS4uCS8Bi20qtjBud3-OUIw4XtdDKL4muPz-9vE_wZ_UNuof-hS5Cgcvvv4_2sRarwSgrOjFHbIIfPTQ9yAHWL09JEGtfuqMcx1Z45PyQdpytfKCfEPVcnVT3Y6V-cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdQgxFVPYRF9kxwUGeE3c4LL1lbQYBRXnwT4qx7StLGVdI88i6wIxM1h1zpX9PBXpDS6IQZqcNWTxAauG9yaHiKjlow3G5kwt5RcbXU7g7PwLAt-cFRQtVh-BKHCetrhNIFUF0-oWBLqqm9iYbyCXCWuvolljjwaXMdg6ah2OHvKBuuQ3I1_7tHSP1bSm4p-0mFojcoPHQMQ-f2suG9vI4wyC8lPchJ9enKKtfMKEeBEbWw8dpzvPnGViZX9321l64YbZ_kF205CB1S7QOmVtMlzv9HeRW-3PxOXoGYiPEABIJO7vc6nrxyPeDakqE85juNIh4vBT5F2EldV63BgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRtO57vrQPBBYQXQrekKASD9RoOlXzLcrB9hSJXNw3UPF5uBDV-2BLiTSgJ-zD4z0w9wcMNyl_MOMnfgFIBqNkIK2vKbQI9Sgqq2ljVgwlDxSWMm3yi52ptVqfKSTRodhG7Hk5G0qXvcC-nyWpDlIGag7RxJLhmikIUOdVSW6YvyHmwqEgJAOCWVV81tKt_C-g3Wp1J27SZD6_vOEf82clCRNActHRZCxNDf6sc8MV13hbrA2eInpKm6j_MoifY5kCk59v1-XaR43O7-JajLReiFhHZLRkQSNRM59uyNYkM9K3fJuqF44lTJXJd7_yYr3wyLyf8gAEJOYOI_DJAcGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcyMVF54w9F7F28JZ02FiLWE9kx36M3IzqJyu2XLouq1I9pD0azgrglke7Qtt92OvQnYlOq9hcHpSdANJnzI5BvXBfkjTmLU52o2brvfsT-5dkSHEs_gSpjvDwD2o2AhahPv1V7BZRw2L4k-9foyw83VM2ROgVQb1YMLwSQSc_-zL1HmSqCJWzULHAFbGL2BYUYOVF9MqlfLiQG8Yrvp5XkfzPrw45ErZywBiPX9ZmZDnH_Omck290yF0bHQEttQ_284VBKYL59PaTZcjfBCgEPa6EDCA2Wbj16DlpxtvUybbmx9ZMzR5ZrTViVW-Y1yxAmW2aTJ06nwNQlJlRykoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=XufL5B-a5WxNW0uh2wpMmNc2_GXtZtsgwlHX8hIqtjW83A-WS1jep2X9KO30meVH7ZtmaRtkVc6jRoWT6a3VNX9FxPo-KcOF3awAQIdO34a5RScdpWlx5OdKoSm2wMAlDId6wwRXU4rO0DH2lBImUEhj2n6gUvsvna3TU1sq4nD2-g1Swltvkt3kK5wP4o2x-_jzRGZZCzL_qIfHgcQziNnXhzzeoS14bu9wEXNINO6PqFGTareAVpo4razjyFSgGZnY5sQAe9MRQbVocFsmhgtCHCUyRyQYudF3RKy7RmQIsWfLUIyv3Q9NYgaaIHoJMnb-fIbKCV9_0gW08bpD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=XufL5B-a5WxNW0uh2wpMmNc2_GXtZtsgwlHX8hIqtjW83A-WS1jep2X9KO30meVH7ZtmaRtkVc6jRoWT6a3VNX9FxPo-KcOF3awAQIdO34a5RScdpWlx5OdKoSm2wMAlDId6wwRXU4rO0DH2lBImUEhj2n6gUvsvna3TU1sq4nD2-g1Swltvkt3kK5wP4o2x-_jzRGZZCzL_qIfHgcQziNnXhzzeoS14bu9wEXNINO6PqFGTareAVpo4razjyFSgGZnY5sQAe9MRQbVocFsmhgtCHCUyRyQYudF3RKy7RmQIsWfLUIyv3Q9NYgaaIHoJMnb-fIbKCV9_0gW08bpD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6A0dydiol9jc4wRLVDX452IW61dRDmRnUU_fnkpTfyjk-eIJtd-xVHmIVleqRDou3x1j7K6pXCghbkGLSSEv8KjtnFTBjUAT_VMcG59Z8avSJv8tioI3yWMQir0Ud-srp_TIeBG_6uU1tHwpEk6_i8lE8phlf7h1ab6S63w-sj4yuEebRE4mtegNONZ0quOg7oBojCW5GGMsE1W4uXERzD38zjvPnVETWl2QlgbRbDMy9Qdp1Tm0yZpK2WULWIo3qlv-YSZtcIMAKUP6PMUwhjoLeeQfO8fs15fSygg_7R7AZtLU5MkxrfVB6aqUzLm5J0U2yjFYgx6UloXCINciw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9IiNpdDRm6TvZrGi4jwWCaNXdB1HAC88qYk33GvkfXVTFsMiWYdKrYOaszFLHdzKfZhnxsVrbVxtjSSGHK1U2jsuHv9XE9T3JiwkO7WR_YKdndiXXHdjB9tbrPIF0BxtcC2PCPQomlHvvugqTu6KjdFrBs-s3PN4dxQtOxU1VPLIrYxHAl4sYQ3nF6GyNoiSClYSmowvJE9HW778YWuAJ0FC1sNrDjAeiMwma4puj55kfqzZvjE7TwdSYeFitipJSQRKAxSbTjqrwZknwslTeC_9HEtyTFBfiZDgSaPe4qXZMffmddpIbB1XxM-xyaTiLUfpkUUDyjXGFzsLrdXOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=T5SId4OogTNmj6gIjwDIFp8QA6xQuRdXRMltJty3_n8He8yUU9st8kJjOBUxdwKRS3qvYEN7pBzbkgX-69nYC3GT1MTuUdK3Wds7_GUyLInthEPfx6K3t1xmhnPzRvqJd0O7UpYHon1IScjfIMja_m82kHkK3ux6rq-breGkIainuAZf8CDE6cq9qfQj-Sr2ZOTVrf_wbCfEn8ZaK9Hbckj8bR-Rdt_Z9rgWaK4p300n2y4r5qytWsOk8CB6GUW67OtZprGRyAN81g7MN2m8hr0r3smJz-NQAyJfGgh-fCajJmaC6py2XysBHZ73ZY8ePAk9XvwdvuTxIh9W5lVULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=T5SId4OogTNmj6gIjwDIFp8QA6xQuRdXRMltJty3_n8He8yUU9st8kJjOBUxdwKRS3qvYEN7pBzbkgX-69nYC3GT1MTuUdK3Wds7_GUyLInthEPfx6K3t1xmhnPzRvqJd0O7UpYHon1IScjfIMja_m82kHkK3ux6rq-breGkIainuAZf8CDE6cq9qfQj-Sr2ZOTVrf_wbCfEn8ZaK9Hbckj8bR-Rdt_Z9rgWaK4p300n2y4r5qytWsOk8CB6GUW67OtZprGRyAN81g7MN2m8hr0r3smJz-NQAyJfGgh-fCajJmaC6py2XysBHZ73ZY8ePAk9XvwdvuTxIh9W5lVULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=eDSJO8uYpbkJT-SZKZNrrA60F-oJQISejUoU6Iv4cNCD55NtQIfm43rBPJd3zU-jyBooGutAwxCS0X_0OJEb4h3D9F3qaitUr3aZXjyhlFZhN1jzv8H_7A7pe6jxHABchgZp1S7mc5rTBU-f5Kl6pYMk2Tv0hnGx-J1MAD1oYDw8ExU4LDSN-NeBa1AOIHpwumd3hTlZriYwDFfFNu-ZZpOzUEMAJDci-Lc-CWADiNzDxEWCgs43IAXhJ3Vp1iaKbUgW_sWxhNVx33OJFH01vTED9KxY7W6v5Xfrb3eaKHa8PRqbc4HLy5D48UtBtQ6nbz-9xTRUG5exHan8SaCgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=eDSJO8uYpbkJT-SZKZNrrA60F-oJQISejUoU6Iv4cNCD55NtQIfm43rBPJd3zU-jyBooGutAwxCS0X_0OJEb4h3D9F3qaitUr3aZXjyhlFZhN1jzv8H_7A7pe6jxHABchgZp1S7mc5rTBU-f5Kl6pYMk2Tv0hnGx-J1MAD1oYDw8ExU4LDSN-NeBa1AOIHpwumd3hTlZriYwDFfFNu-ZZpOzUEMAJDci-Lc-CWADiNzDxEWCgs43IAXhJ3Vp1iaKbUgW_sWxhNVx33OJFH01vTED9KxY7W6v5Xfrb3eaKHa8PRqbc4HLy5D48UtBtQ6nbz-9xTRUG5exHan8SaCgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=Wvu7JPVyiLwDaxkuDCGsz7qqlPgooZTSBA0lYWnUnnWaEFZTjrXvu_OtLLrPI6UGhTOiWpOtBJ8104wWDKBTKHNbKswW4lD2vTOSW-IVdP9BhyZBUB5y8sFweSsYj1PDq0B6JkN5A07kJz6fYgz7wH4yegOLwovbE8-ZsXmJfB1__Wg29zx2MjWhH9hQFwwQl0mr8cpJzE1pMF_WfgMt89HtmT-h-4gDKxee_N1NF7mTnhXLxbXWv8ExLdncrUF3xsjHbrMBLl4O4Etn3qTCwMlR5SmAoTAqd7Y8tYYRoEInjtxEYmCtUKTR623DyTKaZmXk7zXbdbhSOZu0wNB1Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=Wvu7JPVyiLwDaxkuDCGsz7qqlPgooZTSBA0lYWnUnnWaEFZTjrXvu_OtLLrPI6UGhTOiWpOtBJ8104wWDKBTKHNbKswW4lD2vTOSW-IVdP9BhyZBUB5y8sFweSsYj1PDq0B6JkN5A07kJz6fYgz7wH4yegOLwovbE8-ZsXmJfB1__Wg29zx2MjWhH9hQFwwQl0mr8cpJzE1pMF_WfgMt89HtmT-h-4gDKxee_N1NF7mTnhXLxbXWv8ExLdncrUF3xsjHbrMBLl4O4Etn3qTCwMlR5SmAoTAqd7Y8tYYRoEInjtxEYmCtUKTR623DyTKaZmXk7zXbdbhSOZu0wNB1Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU0aCRQF1aKZuwLIiNEAIGHmSZlbqelVr6QfDga37Uca5nmYybk1DiusTLTkXyjsAeXBC_SDskhPiEs6ezmvzNMXX0q6BJ9e5X4ipERQwSboZsSa2JY-9ybWi1a3Hq_0_MB-Ga3jvtQ31G1LayQVFyk76rDzLk-muaE0DrtatAAb6_yVRDRKfA2-cTibXeFVVwvyluoBbMLFyVO49jKdccMiZZXi13Fey9whbdJtEBN76OLTUMbIhWafXdSbte96aLlrOLjppiZ-n1dFWPoHbq2-_tNhoSPO3H2T05LO8fRwpSDVL_N6-ZZEB03E5wWU78hOtaDc2fm16JPLw3qLRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=NYxW6BvR1VcON57s4SdgDfo47lDhhCzKfSpK9nq7dTwfiCdjGL2geSuaiB3k4UAmwGmpmjU7HRi6N7_AzXCv3-vBLgCVpNXYZDkqisS4ZUB-VK8DwnjhUKpC8b6B0wbtdYbI0mlU1Z-87ydaNWSxDbDd-nttGHW6ceBe3tRsR-EyVOm5B1muKlugsABWsffwXTqL5SRaeCmvE7DcWwm3hriAZ_kRwKU2T9DA9mBYogVgWWqLJG8dJreAmceggG9p8fEZ_-LFQuOiNqiKM26NGRvDJny4OjMlEv94AspNyDCuRUqrTq4MUbfTIQzllqZcAzlgcOHHztCvDa9q9a0BKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=NYxW6BvR1VcON57s4SdgDfo47lDhhCzKfSpK9nq7dTwfiCdjGL2geSuaiB3k4UAmwGmpmjU7HRi6N7_AzXCv3-vBLgCVpNXYZDkqisS4ZUB-VK8DwnjhUKpC8b6B0wbtdYbI0mlU1Z-87ydaNWSxDbDd-nttGHW6ceBe3tRsR-EyVOm5B1muKlugsABWsffwXTqL5SRaeCmvE7DcWwm3hriAZ_kRwKU2T9DA9mBYogVgWWqLJG8dJreAmceggG9p8fEZ_-LFQuOiNqiKM26NGRvDJny4OjMlEv94AspNyDCuRUqrTq4MUbfTIQzllqZcAzlgcOHHztCvDa9q9a0BKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVNbwASNr60OirdeXEqaHJGPHWPXG_aUY-TXZbjqHZfBTxc8aaFfbiDhrH-81QRA-2YpSiPAlExFyQGJLpvWQNFekVLBuppMCJV0aLJ39mv66f7C2zf8FG85397gmCNVEQc89is6ps9atRz5bfBKCJQ0hWUQ_BqlnUj_Tn1f6B0bdzJZ4nK6Bi1iYBDQA-DVsF0PLdtSCVnHn7wpA8TtnP5fw-gCKLEIWbpWusCr_xfygAga2UBzDYe8ER8Dwv8ALvXBybYHQZzAAtfA8lw-njeZ33YrB-DJJHFrf7ubtEzm9E7f0pDENj2_LnMPcClnWhJWDpJFb08bpsWsH7fsjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGll6JIf-CVXTFxJri2vKkShghAP7U1b9_RV4vfYqB0OobQ_9wnpJ7n6K6ltxd5Ag27C9imEvw9-2IJ7gRyN0I-gVQvW8U9u_YBARVZ542KuRYcRbO50zVSV77AZyBiajRq2-ppkQ5YmmCq5-m4jq03N9206Wo-P9pMLukoCsglZeWLprYzhFPs02Ryo3TDxaCVo3Ncc_FISRrv4nNossqh3aet1BmLsFwolTgMnz-ldjqKXiZt9_GEJufq_sC-4WAhnX3NKMjIlYKvgTLx1gXekRi3J3eAs4KywPk5wwpCJRZ2sXr-DocOtKDeCn7V73VVfQM6n8_4b-3p7C9jvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxHX2BoH5WnHCCup_me_UfLGwH4oaeOsgfq0Cz2KiMQO_n4Z8X1MbwLrF1HwcfILJC1aMnn-Habb7t9DIBZ8ASWJlHFCaSBkaQ-2nZldeCicny1jIGSWf4fbO96ebN90Pf46_EaU3RjocllJSGcy2QbrRvorJ1HsuI9FLDxH_T0HPWdZNnn6uqIZMG7KFNNFCPzbifTzz_-3SjC4X1wDt10gvZAqErcS7h65Ko-kfnM3kzpcJZagocujb9hfzHnf1OQFQujxX5IfE6kBgbV93tqmweB4l5pd3JLWpQLfFUbU1uIJKYme6fhJ0vTq5BZbA0F_8-AEVqdydEupfO8UiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvmcIAIuEGzGyv3Lx6wkayCstasSSCg33SpnyUlZfjIwJTGYuvvrJ4FJL4qF2nZ0INCBIqM-Ai1Eddkl7BYe31M32qddWUNzD9ktN3TUh03IEVYv0u-Qf0EsCPwr4MJ4HVab7brGshqDjnIerxwLbhOe2Xv8Xx0hmfTxESEEAp9NKBjbIveAemRs2kXf_X2yitMzVU8sDna1y9v2-EIDfXUMUBXfbPUtCClTOSURdUq2v0Rqai37irnYpzO74f2vjVi6Gd_9q_9S0-PrwGO8EJlc3A15PbL6QG_zrVT5fCu7BhCQz_nmrVtPN5qVDbjK9nL2PY1Ds7HIeywAyvPnBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvQ6yoyCkCME2RVvC1ed0x5czEEnXpCU0qXuOPCCKC148HTzDxTK8y6EnmIzUbJSh08Qkn45siNT75j59sd81sASEXzIwY2-QPW3QEu3QZXZJrV9lIACIYQAdIStKquGlp6NB-3Kp_mJZfApV6iUua203yDuPSh7XoSFTqayGn0ah-v0yRXgOCWGUu3LIgxxnwfJNzcvMzYJCLhgm9KRTVC-TC5arvTtltZT6OYJcOI2zqC13EA5pN5qPcGvOV5lSenw5KaxPZR00GU9e4LQiuw-sXShHy-DVi-dcB8bJOpexaCyutpc3ZNg6NVfasyZVdR5lb2KKBLov3UMHArwfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnAI6ihrMps1CNjK27CeCiQu8llgrbVVbAF6j6cAzsvIlIwAEnC5uuz09hGxs-iKQqg7JXr4NA_Uw2F2TSYyS2cM8AWuRUGFBT1y2w3uhxrUijkM2PM8EeqbrIbM5ltl4Ni2IV9epC7J4ijhPyuPGxe4MXK3XrmqK73g_458zGzZPMI5T6mSvZpoXflIRBRQC1CQwFGxdwlmCh7ATLzQwUK4LMnqUeA1wO7pPjBzGiQSCW_79dFEECWGs0-LAfB2aoqIbv5qk6Lwv1fDOP6KrgyJow873I8NxbjjYo8NEpG5KxV96R6DaRoBWbkRrmPH34if6A1SwBjSl2VYvZfONA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYaP_dStyWv1XGSQfVKXX5PC8D9sc_L0U7I4BWJvfo1iIUkf7vTrmhP897rjEnwFayDlexwyAosSlk7nip0QMriWwgNwUsKS53oqvuLgivrdnxkuT2e6RevadAxpWJ8ympvP1a20O2GpMv0mvZXAmSPLWWPj9GK2JZ2_O05_k6VuakTzMLGrQh93DJgNhO6c5qVB5zfTT9-78po6_qwKBxW_eL0f21ocYdcLRgvprHcnkB0UyUBVAIpnphlrv2GqbboZcRis60qn3yA6PAL2PUIjr0D5EksftHRFyRfR4UgPfKzH7iSZqOaUiwVVkIDgBHtx1C3MSZf-Od7mVVOzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS53SgxYLGBsnMWWLg_YSL90szDTDKnQ6-Jl6SM7RwJ7-l3qIwBEt0T-eBj0JmQGzpJDA4XOtBL0Lxl6wI7ec-tE69aeG5yxr8EWdb45BrxIa_V6MXnU_09F064CiW-fH-ew0YCWNNwnyN5Z9hPjTS-fn-Hm-Fe5KQMjWlG4dfTXb51BGO6T_fIFrhwJX9Ey_oK2sqtEO8jj4fv3xBD8vHoWHRgThsIMnkGsqeFuH0uwt4IS-DD2M_6wBXPBLDY2IumZnRqJLR-tlJq6xYf9XyTvHMe2-rnoBDkPT0ynfAl6O9-f0rP7VwX5NO72czpqNSqMt3TbTIlCYEKa4rKXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZlvGm9d2mMN2YaEMiNKRaxFBPovb650x-T5QeX5jFhgP9yPdbojsGKyoNNHEeiDRg5JcAzPN1dYXvHoCy-g7qXaGuOEfNKqDiw-rMK6fOS-XozTVh3T2xXwO-5dUWMUldGkB2dAd0WDjP_Bv6VU3E1jebzCjVKsNO5bw_4VLDMqrTp3-s4GvS-G3eBVLP1JIQsm0C4c8m6BwmF4GJIEEZHyJHKgBKcKxnMaGtcvq6LtceiJfva8_uKmdE8zZbD4jDvMemiO02PBGXPYhPkjtUCuv6yqohwDJGn-yAjNg06XVpA3xDnikbqoBl_eNOZmSWmOD9CfzHENcePRLIpGQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAtaYTfMrbe2HmuuIIi8eJ8bGNGs3RqJ03frn6_pOxgquQXKm5DdFB8SPzY6qTR7tW5MvgkcAUn-OEiMMoF2Bn1li4xvX_eyoDSrdHUJAg4ZENb3t4-lYfgtnAk5uknKdhJHuGr2zhD1cjvVqsr0wHUwXCoPtmccEUcJP6bmoMnkeb51ZVB6ZxDpZFVVOMgsSuETCAuFO3ksqoctR5n3b79m7LJH7Re4il_oe11Euaz-J3oz8Y4YOKS5s3tbrjeqrdqukV2iJPYSG10jiMP0pnQgNYSmD0VMT7V9hfwqlOOFXH34d1GgcwzqNQVhjByTkusknau9gLxDi5xiMPR2hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4qJt1c8TMHW8fPVAKpaCxZMGcEUm2rvFmktH21Y3mLgaDtrjjJZm4UICziOOYIw-5P9FNGvnwZL9pKbIxq2uNduyrQAwV8hyAZz0aCLQ8UeEDnyiS5sxj8xg6nklJUgUG464HkMxxCmp1M9oTrGG5SuD40qglIuu3an13MITrt2XITGvZhMoDM2T23PFfuKWN-qRPy-h4qurdXEeFTwqEWDpi9tDvdjO9WLZBumsGPUPqP19V4M7jYhCrDxlZrXF2aQI_Xv2R8jRgpZzSPiDn43N-uu2ojkUs0LCUczFFKUmMYoyionYr5R5IqGXzKXflNVsZyZhb9LORJnaNGLfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkm3DKYcPnT1Wkw_fJ9yROfhIeeN-RoDocj6CTIJnsNjCLPjtx1ZQVg3pXuyMwcMeqh0bI5VJZuClf-qPDgFg1WRqX2ySWTNUglKZpNa61NDsZI60LmvlZDNiSw5ymPEYuKq7V4W4vkadnt57aOrqCjunNpJlEsOmTGW6pYTDihKKbxTKjViJRO-ERmN5czdM7cbt4RDVaX3N6l_9iPthavRoKg7JGUjIATud4AxCDozAknYPDC10UlgMquvTu-96n9JVu_C2yGsRibJ2BtJL0lCNxOBeuuelHMoGldaacQqMW805fdKx7Hl1wSbZbs0reWXarWjJBTCajOJCCLVJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI-y9l2gwCfV-fD3w_J8Tw9tL_7Rzttn-LXdawAhOzySLWkyxlE_bLXhXDyJYr-1k5cQelhuCgdLhviy4dhqgGx-JwNt7B6kkhd_dHSADrpgbiaKXtG4RqfdFD5PwnTwgbqSxHJxoLkQdm_4Y4PS5unWI_p71Zy3qfpYpLcDxEdmMEzQ6EZbzPzm2SxFVqaWqGh93tKfR7OvwzSC3qjzGJDsgh3i2w80-Y0r_-GgOV6euoMFh_uM8dan0zBFeb_HBJqIfrqVosm2_0SFTDtIt2Q9VKBK1PhC6mSHXhYKTMLiCLbIowbTWJ140PIsdqYhw06pFWZcwKwah4GcPV24yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4prOn0Rej-pXpbQCisBtBWsN6Vghvttc6_1ZTYRgxl5KiOtXDgZD3w2mI0RLdBdSfq2WS9HnNBlozTMZs1OhQ9LHN_QxKoy8wXPQY5OvPGtEVmik-LbjkIYvOBdbZ9Sj-_HUwOUr_sURbvb28og3ASpowk8GNV3j7Zz-45_4_NQi4RHpQ4B7DoNLew2VC6sBrI4_V5YoNlDMFN0kKmWGYzNDG4vT3HVA6fmLh1rzb0y5WaFEK-tYWjPfe_sdVLQlG7dOMR-VvqV4qVGdz99S8HJKGvByqZPCAnzfOlMvRrAtd0zkWSLWkK_SI7hkLdMZXlh4ro8kzTE1UBjIC4E2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hympMWn--0ESnQ0eGyY9u5PZi9wuRJn6AW0SLzOrnM2MDSudvyRCeuO5zSlSmM7jk-dEi5Mjp5wJlcC35VTfrMNYNr6Q3pEnwQBKGe3fmZ-r7DD-HbESOzb9Rg8UKQEj9j8AyGS8Z-yKs4GCOIjPHFfs2qPlipRu_DibNixkxkA_gU1ik3XqIdq_XrbEhKPeZVohsLoRfeUk3vmt6LsvBKzr3aRB-djEg6pfcsgvT_9kXAVNsWZsgx8VfXiCKtV1mwZqEHUCyOnfRgrJXmKrL8uI4GSIWQ98W-qskm_BEatO_tS5qr0hnRnkEF8lQZYJavRm-s0shIAK12FoeFnktw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yen507IWW_iKOqsVAOAwMxY9VWTMc2wYD2yGgi8tF5CqH3frQrxj2O1vvPnes4bjT1tQPQlg__YWk0FzOI9AdbBpqpcHbUlBMI7HQb9eC7bQEY2_soN_fQZ-YjzPicQ9ZRIwQbouoGCpJAzdwSQiEdpSno9UEPUa3yuPT-TjAyDdIKU2qVDhK1_NRL8u6puqZKcxRRBM2gKxMIiYLskuxbbmx-P0Dic0ixgyvJLq6hz6knfkj-9qLnjVM4W4HVA5poBRttEVvqVMoEZB09nwuipgq1ecfcSVjPkQU2nDV5iKQxDRjHS5n1w79VfzBxXFu3O8BKeUF0MUKsjVZFZz0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkZpswKs5YyUlJxnaiPPa5g_f_vni10WlGB1TpHNgTW4PVgJWPcEESSaBP8QmrBR385FUJY3HroFNeSlcnnju6DObUVlgY6rRQmvAj7PZHXS8kOUD6Tj2jiM17X4hL3P47xx4C3bNavAgFGUatQeLioAldwOjmPQI0-NTASm2bfr_j9gLyZddKVf6MEv9M4-3uOFGw25_LWZp3x8u9XLkuYrPfEvMOWkCwLk5gFAuLgEDetHcxSLE8PMJEostxWaXrTJNSkfgWfYo8sJhDUTaz7L3u5d-uA7PmlUEwqe-FWsuAd1ERg0zIiMK2np9Y2zRXV2TNpZXC1aQSY6L_QYfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmJIYKcxzk3YnsaWNoVUp5593y7EYfb4BRkusriy_a3G-vHBYXEbQH2LVgDMARVBPzSRV6M4tl30zXVn4cSKgqicI83KlSvL7oll-f1cxBvUNP0nw1_z32H5vTg3M27mVesja8k8B1LKLgEu4UCGE8dm23DlZhc-okH_gu2KfKoIuRlwMwdVUEqYB6bIFZfZNOBXLJznoDNOsX_2G2slEXJYE9UnQg6m7Xj9DFCr8VMw2L9K-LDDBem-1MT9dzTr4xfz6ZyKtCxe8nwKXwYi105xznaNo0RSEahsG9EgRUryiGei2gJYNoHv8lUFvKxMj9P-t_A5yonTOaBgsyXK7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=M42m6tgCqCPGhwVOyXUehlIbGfWwl5Y4yU36GKBYO8fWaUYNiI0Bkp1e-M29_xIFd7K-7gjo6COTwrjDfHE8o9f8UMlihQ9RduucWmUjvq35HelZVr0xBdn3qPtJli1wFS-e4v6846cIs4_PMEeDVrhn8gqft8p182Ay2AOdNN5i0CsUfpNrTr549E4f0R1T5B5U7Gb6Iux42lwAMHMaFligC4375JCi8kNE2DLuQPddu7WU3FAzVZbCoKoz0IPi2vej0v1KtpG5WSqdzVZhaXXTL__1Os7tGHT1EXfZ7BpJp0tPc_4-D2O413A3GIQ04wBnwjPpOtGQWN5AA4iwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=M42m6tgCqCPGhwVOyXUehlIbGfWwl5Y4yU36GKBYO8fWaUYNiI0Bkp1e-M29_xIFd7K-7gjo6COTwrjDfHE8o9f8UMlihQ9RduucWmUjvq35HelZVr0xBdn3qPtJli1wFS-e4v6846cIs4_PMEeDVrhn8gqft8p182Ay2AOdNN5i0CsUfpNrTr549E4f0R1T5B5U7Gb6Iux42lwAMHMaFligC4375JCi8kNE2DLuQPddu7WU3FAzVZbCoKoz0IPi2vej0v1KtpG5WSqdzVZhaXXTL__1Os7tGHT1EXfZ7BpJp0tPc_4-D2O413A3GIQ04wBnwjPpOtGQWN5AA4iwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDXVzhHEnx9McajFoOxDoo288RU12lc9ov4QrJ-Q3AzN9qNaALMADsNJidN2tF1iWqc-uydaaHjRCYbRdAxqteUa_5_I7aMLmyJnQWsChqF0oPUPK1YiyxEvu8Rqd3dlJLhMO2v7C8d4K6FVuXCIvV3cdTT0DvuE3IE3C22-1-KX9tqzY55AlGuu92jh9pJf-wuAM3a-6PiJ8GHD154g9hASlrCMIahZDWpyIWe3sf4vCqzBgWDuFx5A1XcV6gcJdp3asdky99bdkH9aKK3iEakne7-GrL-KBOmlU9jjCDSLQuKhUp6hW36vNyaIgi1jU_NYgZeFNq45DdVP9qIXaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=kWd602G43b3nnlgFOYh1vOS2txhlX0JR3yCn2mF7OGh7ZAO4cpwR0tWrjc839pFPUHzdez-zm921AgvXMGcmK0hkOqYLkOi3RWycqDJ5RHDbrrD005VZ18qZKinzY_F9qwhO7HllXiXf8V9nDn-RGDxAD9ZUirTi0EG8RrM7t-_1KMr6erno0q-kajbh7XcZdykRgZgvKhtPfBk1AxX6B4pogmi9p95T7YZwi4ujbrC4YNZYxk0WrjIa96XKk0mLB8p9s5L_UEDaKdSTcFPYdXHAVNT_xDCj2Bk5e0a9Sqz10JJTyouJaFpwnRRYh_TkwcbxM62ei6X7hBTPkwVtew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=kWd602G43b3nnlgFOYh1vOS2txhlX0JR3yCn2mF7OGh7ZAO4cpwR0tWrjc839pFPUHzdez-zm921AgvXMGcmK0hkOqYLkOi3RWycqDJ5RHDbrrD005VZ18qZKinzY_F9qwhO7HllXiXf8V9nDn-RGDxAD9ZUirTi0EG8RrM7t-_1KMr6erno0q-kajbh7XcZdykRgZgvKhtPfBk1AxX6B4pogmi9p95T7YZwi4ujbrC4YNZYxk0WrjIa96XKk0mLB8p9s5L_UEDaKdSTcFPYdXHAVNT_xDCj2Bk5e0a9Sqz10JJTyouJaFpwnRRYh_TkwcbxM62ei6X7hBTPkwVtew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO0mniIAbLeSlfrR521P2oa3KJRbpzdfh9a_yYgJPmw7cQT5iYdhPa8L61rtYgtjiFL3a63Uq9lcRpoF3AnQ0tb8C07VvjAAaFDkfs-pfwcJ23GvddHzaxUc76WvR2K0o71QVYZEf88w4gXv34lOmVVttKDf3xwe1s4axkj67m9ig-z19euO1JQDhH0skAdgolL9RfwY2zKHcO8TN0ezJ0HQUFZVKPc_B9iQsM0fUdpP_exaft8mRBLRRDnWpA70VQQy_lsoBLjmIptfI5uA_YMyja6G4GunYDq14SMgGqG5CfKfGW1nsXQZZgq7C6kHPvIMr5kvp022xGhcRTwyBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
