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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 04:45:16</div>
<hr>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENUDQDtnGx54iHdIFRNs5c46j-kx-sAeFze3zQsLcq3iGq2l0i_fz0dqf3zJRhdOVG_5CxMT8XnB8UhCCXFnFLJTLJH2h0gCD-V9Ueriv9cwbLnu3JAKjn8dVzZucAx70heVR2PX8JRCi7sxcRYsSEodhVFt7ltHQ5KIbVE13_okzg5VESJt4mPZluyEwo_tc4fKAtcEi-Y-suUo8lfWXXpSf-FWw4DOknVgXwlMtdn7G4-mZYklTFAy97eN9KEl6eZF9sj1skRr7t7KIkX-ZBLenz4QjK9czPIkT8AbCJ_pF4OyOqU5sLR_dAV3_gqMHPHkWKqRGgkXgDSKOjqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmpLEVR7v4j-ktNPEmExIVo10SjXlMp7D_GBn8efNSrO0jhiPiAzeMBfZd5ExqFf5M7oeBvtXG31rQcWNzx6sX-a_Y6aIhcUAIdykVmpkmVDomWTgYm8S3aQPlpcUYqVqNR9UF8L2bE5Jmv8H5sc6HzZYiysQuc-tWUeUHU3foL6EQ9f5VrcMjBVooDVJCcyotkWjc4BehB_27svfUwGtrfxOxsx-C_4tvw_AISNnYjRbF7w48x8VdMaRWU0ztzQn81YgWxfZABS_6qgpsnNqXAubc6NDL1DGP2cOnKEH2-zNI0IC_PGbDDqEf4EvcppDtHx1r1uIfPTemh6UHmfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So9L93KoAs6QfRKYXkGXSPOPtZS_h82ddM9xz6syeof7-7CH9ZeKWFn_JYM6-O8vTxTwaFwkoF-hXO5xLqYQVMDewyKMm2uefnwk3rm58ZRNa660ScYy_XTxVntJOwz9j2jeoY2AX6av2EjeUURAaTgDAnIdUqVuW8fYBpio4Xg3_ac1QVELiHbvff5Rg4Izz-r4MaHtx_OT8jmNXPvquINcjvbsNDiRYijme26mLFglwsy8qaiO-Z39Hsgw44BqDJbiPIsp9eMdmxxtijuwTI-91uvZewX4Bs9RNHlXwDhd7BwsExKkO94C68_L5nPcEd6lb6La91ux_eocuhuNVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAE3Sm5ay9M3cWg_rjBnwQCbK-aTTNiL_X-HugsAzs16y3e_NMrT2WmnpEgvNokozmZihR8wleFYIWgqbFYNI5eQDJmPT7tNzcbzqj_7C8yxygtL22HvXXfkVpo6uyc_kJG8gSxE40Ryi8S7Vw9iZZ5GtABn2OKqgwoXOitVXBzF7pWibm8vYTCaQQipQeePFfB3rTe5ZqzsWGP9XlFm9xIYGaET-N7_TXxZjs8VaRHnkcKyCietjDK1MZb1T84e_C4DHjDfF4ZLw78zVU5m-sgSN_XnkM0s6VwpZyF24W3ngqa7ffJ5ywUSlpxdkS3TFDlrXwha5D2fd5VUcFWhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=OFfUo69yjSuYTpEiOePJ1RX9vnEgqQqdGErwIYHDw2xJiS8ewvkI_oZZL0LWc-bXV0sCEMbRVV58e3fdgAMBBssGr0XCxU5pdi5p8-UzwjPDIS3JW1Loxnizvfn-rE1ZyORD6nwbhlcGyUfCcMjMNpbTvSmh0ON7L-Xv4c2suNmqGsA-EqIhJYsKVR_wPLXjIOTz3ew-YhdJRpEk9HZ7XNK06z_wa08CeqkeDpp2cIWAhsoZRHwbkejs4hXGwKJW3oXAfoq2WNRCuxuxywwaC0BkA0JUYmCHja7pUynlljDDDjMgCfwQZDCNtPYTGyvW-VrgfgIDng7kneOw_YtO4nRnZYw_azox4s8eWo8wHKO3fbem_tl6Q3ddVwDevV_9PU4aD1soYOB_CecdHRy4ujNFqiHZzjhABIXlU4KU4Ku6ML1kMklllyqt3twbepV0CqPFIXRAkpuaW_tylhoxiYjTI5OAc1te0BlpkxTfeiO0QU4YNXrlKcf7jcZ20SXr5MGCdKvl2NBNJHnbSYy0Imp2memcW20HmUQqXoGA6ymVU-jfKeFofcy45xWQS9zyPacxQOKzTVI_R1EyUW6DzotdrclVfOFqfzyYTwFA8cxWR8q47FsJzSp57XWaQTvhoerhvGXnp5feO5u9bEJf4eSGdEuOVM3t5ryCYUCDVzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=OFfUo69yjSuYTpEiOePJ1RX9vnEgqQqdGErwIYHDw2xJiS8ewvkI_oZZL0LWc-bXV0sCEMbRVV58e3fdgAMBBssGr0XCxU5pdi5p8-UzwjPDIS3JW1Loxnizvfn-rE1ZyORD6nwbhlcGyUfCcMjMNpbTvSmh0ON7L-Xv4c2suNmqGsA-EqIhJYsKVR_wPLXjIOTz3ew-YhdJRpEk9HZ7XNK06z_wa08CeqkeDpp2cIWAhsoZRHwbkejs4hXGwKJW3oXAfoq2WNRCuxuxywwaC0BkA0JUYmCHja7pUynlljDDDjMgCfwQZDCNtPYTGyvW-VrgfgIDng7kneOw_YtO4nRnZYw_azox4s8eWo8wHKO3fbem_tl6Q3ddVwDevV_9PU4aD1soYOB_CecdHRy4ujNFqiHZzjhABIXlU4KU4Ku6ML1kMklllyqt3twbepV0CqPFIXRAkpuaW_tylhoxiYjTI5OAc1te0BlpkxTfeiO0QU4YNXrlKcf7jcZ20SXr5MGCdKvl2NBNJHnbSYy0Imp2memcW20HmUQqXoGA6ymVU-jfKeFofcy45xWQS9zyPacxQOKzTVI_R1EyUW6DzotdrclVfOFqfzyYTwFA8cxWR8q47FsJzSp57XWaQTvhoerhvGXnp5feO5u9bEJf4eSGdEuOVM3t5ryCYUCDVzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfeWUm6t0dSQWYgn1eQLMK5UtTU_ImUuscakRaOINDQVNQacAJkGloPnqfmg56ZEvWXVtdD7RUZjbz7qrOj0ld1wlzBWE9mLhc8V0ZqM-ncXkqCe0_Q3nIYJ6PcxSFYdyFNJDHvcDYPgFVHkdYcJLUklL3Vy09ZblDP8xY0O83Lkbj6IP2NdlRXjYjb3kRtGy8HLHqWfD92kn1fnSyozTymjb-DMAZvXTaoHvrfnbebbLrYdr-xoHbn2lYLehrYs7aB-lBiVnwKXZ6xm9ckDOS4YIxeGrJgqYuU8H3KIbmY1voJ5gPwLfEecCgYNlMKB6-XL7eSPn_lKAtlD8oehyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=ZWyNYC3XWf7dI0DGAg1TrtbnlCWIPSF1MoMQszn1Bx8zl4zVsRGZS8TcVRUocko4nrBnTYL_wPMTfOTGugQuSYcw7sMdYKACbinbtdpNdpeKEExKNmAHx3xJlED-t-JHXzqRx4xlTcBaKAKRstuS9ZVe2Cczlr0hzZkDl6p3PD41_AfWCl_g0t9yfI4zZ9jOZEXU1puivcdOcaOj88ypS_iXvcNfvogtqZOK0ObamroZdgaJzjxo6BMTYvaiV5aULokaG9lVRIh397vVnpXGx14_c9Z8np8wA-4Y2XeO-Fl4-zdHBIaU0SVk93Qa-E_t_SmXHJyiYrUtXifJSlmg7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=ZWyNYC3XWf7dI0DGAg1TrtbnlCWIPSF1MoMQszn1Bx8zl4zVsRGZS8TcVRUocko4nrBnTYL_wPMTfOTGugQuSYcw7sMdYKACbinbtdpNdpeKEExKNmAHx3xJlED-t-JHXzqRx4xlTcBaKAKRstuS9ZVe2Cczlr0hzZkDl6p3PD41_AfWCl_g0t9yfI4zZ9jOZEXU1puivcdOcaOj88ypS_iXvcNfvogtqZOK0ObamroZdgaJzjxo6BMTYvaiV5aULokaG9lVRIh397vVnpXGx14_c9Z8np8wA-4Y2XeO-Fl4-zdHBIaU0SVk93Qa-E_t_SmXHJyiYrUtXifJSlmg7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9SEUGZSyjOLMzV1q7zBAWWm0Qe10N15li1iv3pCDfwHYWTheHY0g6ewhy4I450ArWToIGdgEavKP8ts_b0XoTmgCC-F-6rb3dxbzJeK4wtBoWXNg1R6oMXcWN5sqHo08oVEgiptMiuBkvZwD-dh02y6IQqDAn8kCUpsXOdvCSAgLzoTpU76D5yGbbLZcBEHkDnnPvQr-N3CZ7Ct6NOIE8FcZDqmG_3sh7WJbIQarjr3oqnksVv1xckoOsSOyyWiKzvIG4JF4O03VF1uKLBrdnFAyHodGEUZ_INTPhJ39hPztVGmaPFMdG-BhlKkF0QmEasxTSPvU7fksK1UHVVbHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsmJdAC8Q72zbZBqOJ6WaLt1JoxK038n3OdfvbgclmWadutYx09HYMXPkUt5MLgFivqVTzN48xKM9iIdA4iNpR7tBgQxeHybOmFQ_YxnCXF5sa41hJkdvLzlYjiGfydiuqf3U03_6L8EBAmiQzGNhMLMl_iJLAzdr2PMNKyZqgsST1nKvXEQyLFW2N68RSNnpmJ4ZKMzcX-a3IeZVt75VRxNCsyt9PHbnOVw2PwU3QF2kYYVG9cLgZ2-nRx9FaSJzPOzqNVi5MZE0NuYCuI06ZKYhPfwzxCvQCHY9EYBqrijqrkvryqxJf-3vybuVaq7O-R4a3PCChT_m38Wm7seMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYLrK38IkAy7ekFWcbyYeFWR9gamPaR1bOjfAfuEZ9QXgBeLPzme9c00wkL3qfFGnUZM-e555ZG2fWpk2cpMApHTkg_dxETTMDqr7a5NKfSpeLZgbOYfT0cDXhHRP5R0eYz5gcEh3M4q6-Ph7RFtKWtFbrxH1qL0t0clydoJoNQCNpuVS0GT9UvvxEGc6Fkb-bAZtHhkHX2LCAuSzY4pJF9JQPdCdTrqIZ8i4CwSFxRkom_bLXXjSkD8tW72rZpCKM3D31PRrGUdCEvOugyOHHceAeFgHRe0_2ql7u9AKytr22LYBdE0B3J5he83zKnkuZTUejnb3lI26ozBh1TV-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYH8OdpyfQgHlKJ6f38SWyLgaZlkKyb7_ncqEwjmWRVyOYNYIJ_81br-3HqiA6T7heCkWfiEpzIRY7B424xUmiLLED5xtw4Sv9txc3rYqat5S575owzNcfu86Hjo-xl9du09ZyFmZ2X2KtMngLI3qSJs5LQZ7hn_6Yse9BGFek-9ypx1nhzfV1FeZ67134UqPrROEAJlc1Tp3gjUaUyuQipM4Naq8yY6wk7AIzcVqJVsmBdPuZVD-mCF918YqQQ2QzmXwjIg7iW8ShCPZxUxDSBgXI_QRGmSxaxvaAMHzR2qZ0kADxzxEZit3OSEVJZppUaXrDVnLEHMtK36_YZvgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-FhAAtFuEqTOEJ2slTE0X3gUny-rgRMMizlm_PkruWhBisP48vH1BVaWd7Nq-Nlivlj6AB673RtX_kdfYDncQ7xDxOEf6v_P2Z1e2pzsxjsTi1ZRI4elag9n-jE96TedITrt_D_r0ysPt6XeYHqppq1Zu1Sxz0TZSVkhkAldbYWeH6-v7l7WcBgzs-Qjo2sG1yZgHeNzhdJzsT_tmTb_CWz204m9aj3JR8m0H8lwGsLbhwVsn6MiqISdClo-_PT8kE5q54rNNqXtRFg-Orv27oPUo164d5lIs7gA62fLuVIDpzcmj8AjD7Me992Xr1F31IsWHRZfw4RtmSQAAt4FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhEOW9nG4juw6LFHlYmieJCwA62mQXGJmQPa-2JiBudKzEfxHLxFRmIHy0FdgQopInhf0oLUqbwR8Swg33l-wHCcE_9n4jeR-dfXa5Q6OdxZhlFM9uP0gY3D9fKmKjKWvaBIC1YWUvZb4gjFjHJIt8dHOim1DCbbxTQ_Z0kn-felJYMu9_Jo0j4xlLtDwMlCn6jmYAFAiNJDW29vVuIz3AD8MVuOnQMNOZBCVdpJucp9Ls2u6vhvNeuY9FQRML9czg1Ra5NxjhzOEQDIz473O2UUJZ8nqG2U9ZrL639h2y6P6vxMPAp5-CDAvLqvxw05IdmGzMsJvFxEas3Oq_cVvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1eANf12WcePJoCK9jHa2Lx0xS7yUm3EcGVmdYwHcBrFWmW85E09A34Z7F2nQH0W2RHqyilulhrEeQE5aRTVeI689JanfFwqQ6YFHRUR3pSQ7zy3R52LvHqQZBP8LTV6-sGIFZ_iFpWUlSMDmVU3RFrT_mSCIQx1q9OOkvLwE5ITlPXxgTiwxCqKZWpHjlX-j34pprFlLzYc5EH7Xucqz00BH1Rwl4t3vJOkXHBs-rSVd_22kQxbcb4h0m7uR2JYjx00mRUVPUgsjSDdRY0A3U5kcN76rxOCb3kyt_z5Q-NkQcAwd0besexqZ1sjyp12c_UaAeEqU_H3AR-jWW826w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knzgspsnp7j77mLonQAe56tDYXg6tHV_qbexTTTnMdUVfnzk2Zq5yKDsw7yc9tob6WXi1a6SNX7rQrf7HrK2sK52kyzQ0MWWy32f1K6B51O0rZjUbF4VZDkrySRDH6wKJQni32_L4jdczYEpPyok09mssQG8y7xv4EI-rO5XkFiFR7tYuGg3evT3S96Zr6QJ_KRHzbspz-B4F1kxbPklIBjygLZmwoy9QIuEOwhBSiQjDwnannPAABuIByj6SdVIUNb6pRFB38rwxBgtTTXTxKEIHYmheRuTRZm6dAx0VbKPe-dY-DJzbmNv4GBo2-R0CmOYfEnkIEEqKjh2AeTo-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtmHTF952iiuSZwEC0fzTGK70_iQJ8PXOs4l16XmI6SdPqxjVh-6kUfsyHvI_DL5AeAIPa866Danod8gYUTtweKtZ7j4d3H2wLegPlRN7cGEdi-mHLgHml9cm2OEXN0gUtzTcGiVxM91d3Lp692XLtkmKPUzeUswkTNp33vHPq_3lB5ZXAIFq_H70nYi6CemImQ7EY4nD1rZXZzOwPSgD6B2HAnmjJBOcffvpDot6Y-zPJ8prZOatsoQCinxFzMlqMpqfuA42t9wE5O_1XLf6Rapu85eZVyGv_VDnqqtO1AUpQUroQiXKGfGJg_SDFXkgLHoFsL1beRwo9Y7329J_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXclqAp8Y0N7CaXYSOQ3XWn87vptVEkLJox9huf-mApA21ZnaoB2YN7H2OcadpLuGyFoC2LobT_FQjFmgpeu11fZOqAUVYyon5LebXMuYgpgMJY0jdJqJ-ngptigQl7QESozIko0RPx1_BH5YjJ6DZrBsGaA8xc4gtA6fSlwyd5n827GNLtlNBSr44MMRuDS_-TSSI1cO64r9Y-RdWhKzlhbzOYlmzgV32MveW8fwVt51jznvGvKuiXRIz-4w2J5r2VSB5MIp7AdSCY_xvP_XMXCZJsxU7Sd439RpwyppEFHDqA_vp0akTKSiaokvDLLCgPP5XP7gk2SgLuVgfcggA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd0Dn8mm_IXaiddFLYfbTUlrdL9OMAsF_HP7wPOVigwtbw0EpxaL-pGpU9BRsh_JrSR6kRYJxlPnS4IBk0TPw1z5iaoqCV1TKAL1CPjkaKSkKKb3KD4_Y8BQX7QYEusS3kbZqNMFP5_t-ourIcYY8CVbLG5QTCgluxKtz-IjBL9_WU7_aiowiNJkhqkrSVjRTM-j4R1y9uPodUMf6y-GIzwZlkiUopsw7n0FtygkWDlgfPGvcOROKtgsaFLXSw-80n19EzKkIbPn2n2WjJJIkjwIQ0lXuCBJdXm1Qymlbh_odZQkWRyjLlW4BbJF6ykW2G1jDNGaHmbOGVhl2HwYxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhQfaGAy-lsDUZHVxNZe6gWFK8mRQpfWlkcUEQNxyPdlW4BwGMcSb9VKU70bmXtsEnyfI_Z7fchrTHNBzQa24HsyG-zs047cdTaf7dOZf8qxVdwg7W97Jd1OPDIsW3oQCHEB5emN1b0fvuyeFBjxYDWQ2Pke5x_32iMERw8kiE99oG92op8UOZ81_QUlbGSFuIr4QTolrXmtFTu57eOvvF72hyc4-av-0Yx09WdW0RxtZAeNDeqYERpcypnfiUGSak9ZHehhEN8iN4GZtFGR9PxQ7v3eG7dIDd8_KwiEtxzYXoXw2tDWuesMDVFJ9HmfzsgcPWM6M6DtSJfDkXQQYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLlhV5bSEkiuXXSwUVMODGKjLPmfTG6RTYC9PTxKGyEa3GjPiDomuISoCWAGtDaKOAaANEnoTxl4yVBItO_jUlwEZIDNb8LPA9tqjK0_5wRe4BcqsZUiLX3Z_Wj7LqnViatE3TOUuoXhwPSydCJ57G1SNV4y6haT7wxxN4SL3d2qhGX_eF0RNGwtKx1K4V2aW9J8Al43fSWFy6zbJCTI6Kye86HPcidtQcrAU48r8js5IWMWyNFdbrVFP_BPb3RiCg0ARVCfqsyRN96J48P3PRosz_ELV3pWSD1jFZvXl7ETtdnctwiiSYnWYdwYvF1XcQ6kuS1YFUFcc3I5m92XAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrE2z8mC1csuXwrCNQpY0qpVtdoK85gxFDaP4yAKid05Z1BTINQ-gaqROZxy5zBFiA4ydrGABJCWIj4wNQoQvnDqqMGQ1FIxAI8B4c1_8WZ8O0hjamP87rSZODLhSSAooO8_G9DE1C6xBX7w-8_pjILqtjD7aFQAxye6CQGahm6xFzp_yXrESU0KcaaAoOlRpNkY0C6WS1COo9c9xp4TgUQbf17vg7noSB-G9M7LTGCu7xgmw7TmfSv46A_RyLOuqIGO-5tJmR-pmW4kpg3kSiCZBMMwmpTij4pMoWDoh4ToUPd0G09OIyIyfCW2ZTBBzpK3xMLCLJmZHQe4YXJtNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8xExiC2JjQNBajggNG02RkG2vHoFqPFFwqK1QSVVKvdhrZ-uEYRVkKDxjBH46hw5geTuCYM3I_2XDBGobqR4qBZFbOiZ2ZGMXv9U4XpwoAmumhd14k4i7Kpb1jpu1u1QHtBYI0eq7RFKBCm4W1m1i067e3hrQIFlfmTXLIc2Qw7EQ4r8HxwITNGZt2iwxoUZtg6eD7Jka0Pw0zE-sLea4JM6Vlr-XBTGoKQLrxYIDybLsRPnmpYm58DupoO1YZr619TQQ5BhfRdF_PpqmW7vd-OIH-Thww4tyXhZqs3EhRsUyGqklLKCNZJYo-uY6KYvVbidr7MJSIinLQvzB5E5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5nFVzAJijGYExWeIHYGul9pyQccGrRUBH76Ar5IrAO9HXrL3Ud95YqMc5GR_Osvm7PE9QmqRcgNlUKFPA6B_bPMxsLAYq0aed37zGO_ik3xi8vmaEbHtzMOrD7ydwQdeV6z1Ulo2AMIFxYgEJsov1M0nAwapg9jaUeSQ-JC18lfXbdo06oCbtX9uLXCZCJ4peaNBZygQw6zDEKZb79R6jBB8MthybEA6BkCN-NhMfrIkPmJVE5MUOjieJVUmMgA2097mu3UXkPcUltrQ-Xtun7GFv5_qyYrt-Wc0QMZ38EQ-TFKoiM5VG3X7zHOeitmQP2pJwTvz9n3ZlaPMJcvSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH2IgpC0pNq9khxdykQwqjbKEGpkWozWfh9vsO4KgbE4_5asijZ-mqyQgayHp_EzvsNvdIbiW2AZATfR0XuNLcuTkBPP_is1Z3fg2sF-0Y33yKHwotuO85Qaz_qryMXtKfZYVrm6txgsqyQvgBdTxbUHhlWiV6vTYWkoZcDvH2gcjcnl_QaAiofeUmMyhJKDSc30IGNXW4ErjLFiC-f1UYrIDfkwhGxhUqcGFqAn2b1AeesXGQclnD8SxVxIwOCwPyxqqJqJdbYmPyeiZvhFNrKJDMxH-YQ4u0ls1qDnmgGUb9ztghZbrZVHDfYRw3DSildYWa3f7HLNutyTJAWykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=mvX9c0Hn71xV34MhqG_8xzH8tUi0MOavkwUfUtgZ6zcLgMXxLao0B3sgK-3t2di5aIjTjkLDv1GeK9mQ6MbV_-3cWiU9hbjc3IHI_xkn7fOAywYmhNQK0WJY6X8sgkkQBvf9DKnsOhUIoRNcEnHrurE6rfDyLIu5Aw5TN2OxaM1XUPm8YxXThdTUnKKovSAm_MFktoRtqFIJFCa2OJafVqddOawy8FM9ztO6g832SMITeXTrOtNxB6sgFw4Qk1kAr1t6lJjd0FyoEcGFuQ7x9wM6215cDd13yt7wR5k1X25bRZLcapPvspUv4Q0NJqg6i6VELNjsohBsqleTIGlsOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=mvX9c0Hn71xV34MhqG_8xzH8tUi0MOavkwUfUtgZ6zcLgMXxLao0B3sgK-3t2di5aIjTjkLDv1GeK9mQ6MbV_-3cWiU9hbjc3IHI_xkn7fOAywYmhNQK0WJY6X8sgkkQBvf9DKnsOhUIoRNcEnHrurE6rfDyLIu5Aw5TN2OxaM1XUPm8YxXThdTUnKKovSAm_MFktoRtqFIJFCa2OJafVqddOawy8FM9ztO6g832SMITeXTrOtNxB6sgFw4Qk1kAr1t6lJjd0FyoEcGFuQ7x9wM6215cDd13yt7wR5k1X25bRZLcapPvspUv4Q0NJqg6i6VELNjsohBsqleTIGlsOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk6csNBQPrmjlT0SWZpn2KdiJU0ndh-tvIH7kQQvGx2OYdptJR-vELKQcMCq4Cdqy13W51_YfcPvfUMpkLkVtd4JClbAcvfsZgtF_91z0rwSkiy7BYM41yhAHe2qKey2KShNIYBvcmyfgj3DNAJs8-HfUL7xx5Hy9OuTe3R-A-xEtWQ1RpXXpMcJoVV4qZl1X3jdKRu3x5rcGNdoCnfCwQ1MAfxMqqjrhkG2p0LhNjWe41Eeeu8LfJjYNmGF1czdxC6Cl1OnNmpbSJ9lzpdAj0UlrhMufr6BW7pvO2q0aR9i3LQRALwEEwAz5H-1Ycnuk9J0pWvMAX5OL0IVxxKDSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd8OzfCha78N-a2rtcp5_1fw4hF4DoFXmD_vntD7AJVg9wmz2lnolb8A5lY5_BNNljhZeuFAghzvHBZx4AVy0ZmJ1X1MC3sS5eHq057uzYB8_kUMRhCQ81GWWkyK5P4ItHJ0teIMbk4mFLqgcdUHuo_hHfTa8tUtrEMUojtmJFjXUfLNGsltykkzH8EqL_9x8PAqoDMwMncYrip8iu98rbRUUN9oU50bFzUUHcKaE269vuZQZhhZqwEMy3J2EiUlmGI7lG2N37WEai-q2YjnaWyreG2A7uHFE5GFIYtoMnHKqdzyOsEc8K0SNcCjx56wYODfjhs6Ue7-0MKHmOTx9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=g93GWmsv0Kln5-R3yKns_qDosxBB8ApQV8w-9yb-7ypCeMSpOwjdTfBrsypa6k82Zhpl-MeBFA8BqzrtcJIhAypuuKfDqWOYa-CtwwW_OpQjCE2DtU7u3w44EStD2lzm7Ott9PJC8fPXNm1TBSgbfedJ61GA6xPU3ofOHPog56Q8lArBGSUuSDtFGH6sW6C46ZQbHrhXXGeX4lE7N0MI_pwPo_1b5sLRmKUcHpVgZWjSpgwsaFrMbxWNuLWDo1lMliejSROEdZGbGEvdiWZy2vv3bA3iEOHydSCXVC6hUnkyIeaXUbM-MVoMpnYJTK4pOn0pjqtnVsoRz0uHakHqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=g93GWmsv0Kln5-R3yKns_qDosxBB8ApQV8w-9yb-7ypCeMSpOwjdTfBrsypa6k82Zhpl-MeBFA8BqzrtcJIhAypuuKfDqWOYa-CtwwW_OpQjCE2DtU7u3w44EStD2lzm7Ott9PJC8fPXNm1TBSgbfedJ61GA6xPU3ofOHPog56Q8lArBGSUuSDtFGH6sW6C46ZQbHrhXXGeX4lE7N0MI_pwPo_1b5sLRmKUcHpVgZWjSpgwsaFrMbxWNuLWDo1lMliejSROEdZGbGEvdiWZy2vv3bA3iEOHydSCXVC6hUnkyIeaXUbM-MVoMpnYJTK4pOn0pjqtnVsoRz0uHakHqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=lJyeLOCbUdQBgKjHsWTtftFKQmeqUSH1YzMm6v-Kx3kwmX9EwheAy8sFSoidAEupxQ_EnPlDikYLqTp3wjE5FMxROtc3A5lKj0ZSh5Vmsf8qOrOftoAx94UjyOaAiQ80ZSjaMYMrkwqu7NVPTOMJ-2PREG2V9SE__4i6VZzJU6iZG5xMWBEH6mIDGELuyutvBIAmvbvI2MiaB6FOwSp0tyLAyoJdvWOuyWviu8XuVt2wBM8t8HiFWMFulJQHW6BMoU0KZWBF32AdRxlf89pVhm52Yupp5qCrii9L13NQfYC9yIiazGuLInj_Er01W2DyY91kI9ippREpQSamCG9y1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=lJyeLOCbUdQBgKjHsWTtftFKQmeqUSH1YzMm6v-Kx3kwmX9EwheAy8sFSoidAEupxQ_EnPlDikYLqTp3wjE5FMxROtc3A5lKj0ZSh5Vmsf8qOrOftoAx94UjyOaAiQ80ZSjaMYMrkwqu7NVPTOMJ-2PREG2V9SE__4i6VZzJU6iZG5xMWBEH6mIDGELuyutvBIAmvbvI2MiaB6FOwSp0tyLAyoJdvWOuyWviu8XuVt2wBM8t8HiFWMFulJQHW6BMoU0KZWBF32AdRxlf89pVhm52Yupp5qCrii9L13NQfYC9yIiazGuLInj_Er01W2DyY91kI9ippREpQSamCG9y1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=ZgpIeTZ5aASRn6ENqIEU5bTIKppaFdXBmIN060RAJEw7PBnTZ5aVKdsSyFor63gSJksOMWjy5VYc464MK6pbZ8fabb7Y99l5fab4AWhJdakjlCnvll5vPkb5D7tbgRx5b7OTH97fPwcu5yyI_oG_KWa1Nm3lmtXi85S4FSsONRaL3dWYMR9C6AvsPwfwX3HNok49uspPrpMBnNeypzg8iRFLSt4CFBQZ5L_FJ45DgbEsDuAD6eHdjZFV76Rhvfw1WRMhqC6UKLt4RC4nhvvl_dHRG6WzGd-AWbuB_5rgwI_xtetmVzPi2LxcU67jPHfCa0Lh98X8PimaKDp2CM7SCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=ZgpIeTZ5aASRn6ENqIEU5bTIKppaFdXBmIN060RAJEw7PBnTZ5aVKdsSyFor63gSJksOMWjy5VYc464MK6pbZ8fabb7Y99l5fab4AWhJdakjlCnvll5vPkb5D7tbgRx5b7OTH97fPwcu5yyI_oG_KWa1Nm3lmtXi85S4FSsONRaL3dWYMR9C6AvsPwfwX3HNok49uspPrpMBnNeypzg8iRFLSt4CFBQZ5L_FJ45DgbEsDuAD6eHdjZFV76Rhvfw1WRMhqC6UKLt4RC4nhvvl_dHRG6WzGd-AWbuB_5rgwI_xtetmVzPi2LxcU67jPHfCa0Lh98X8PimaKDp2CM7SCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra1fGYOIug9W_b9DgGp5-JH1xJdTuszYwrHyoI-kRf_oqw_WYwxYwWWypjNXgg09ITqjh1cH4XEhlZaMlIu-M_RD6Hkj_nNc4HKRiCgV4-mWCJm23L00XzWnIMzvEaFbOq5MHrGuTNF5UjqFDIBTafD4n0zyq4q5jF1DGfHDNQ3NP8Txltb9UKa26V91wwocRdCGd7rKGH5dzrpwGAUrgbQWqSvnYXGd-CcQt0qEHSAV6DhjrarOaeegojkMvhiM7sRv2ZFFBPdpst4Hub-zvxUX3ESGI2PcvvdRqR0Pu-s7tXi1p1h-23l0r3t7u03jFXPG80iELGoABtsfuldhHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=oTuQarn6dEPpx5fImU9Ih5wwoI4kHf8X-Zbv9JodwUZy2adZEYAlTKBmfC4bRUmMehvnk2eO_K1AVbMwVmthVpU4mqUpu2DsH0wtMPEuv_YnFktFKh0a9vtTjBVo318dw95K0y2gDBzVdICHwXYXHvo99sqzoFbwjJbd09QTCpLXwjBX9h73isNPCBcP82RLLyM978U8spew67moYb1By3yNfN3RvQoBYueWWNuuWh8Q9ffUF2439yth6THt7xnUbJfTC1eIwIjGAYHe8et1Xd-iSyBmq_qyIZTpkyjHyfB6kf9BlH5RpCPnS7Kt1T2izoK82iw2tC_pdmPCzQj6xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=oTuQarn6dEPpx5fImU9Ih5wwoI4kHf8X-Zbv9JodwUZy2adZEYAlTKBmfC4bRUmMehvnk2eO_K1AVbMwVmthVpU4mqUpu2DsH0wtMPEuv_YnFktFKh0a9vtTjBVo318dw95K0y2gDBzVdICHwXYXHvo99sqzoFbwjJbd09QTCpLXwjBX9h73isNPCBcP82RLLyM978U8spew67moYb1By3yNfN3RvQoBYueWWNuuWh8Q9ffUF2439yth6THt7xnUbJfTC1eIwIjGAYHe8et1Xd-iSyBmq_qyIZTpkyjHyfB6kf9BlH5RpCPnS7Kt1T2izoK82iw2tC_pdmPCzQj6xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUdJ1kpnb5qbzAvgK42j_H1zj48-fJ0NrQpJO8cBC3uRPQIck0BwnFR17D1KUHpD2xnBTCArxixPpLAG2s7oEFaKreTmiKOzZyDSLzpSnMq9cwe5IW60fKPQSzmpZN7IWSIMoBppDF-Q4crqOBBIwv9eUQecNAM7AAeEjwIyZV7QryltoGotR2BkYHtRogXvWGT1t6GKqGvtB6wdihYuEtLXyMk1FnIS_3omBPn-FAhEfFO3KdMEo4uav647CtnYayhQEUEuBneyEsuxrgynbWyGrOFOG0iM-FBuGWGZXaIB2m6-e6WR1mAL3uwo75DqISEeHEx5TiBIRxHL4pTYuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiiynxVG5E1-oknrDioCiIIqQ3hpqlvoAm9r6ibegYxouCerxXDJoZJA_YuDN6J74SYUJniLA8szyrC4_rDgVtsxkr5RJpOOOdozmm_GZGxK7QlVKAQwUUzsN8j64GvlovBVl8hSgn19Ie3tusOYG-4k-iAz122F6DGIHrfn8T04JAe2VIWShIp2Shl-_r8wUgCE00ZLGCRbKxmf4FPLgkzp2Wqf63ZEPcK-NMMRyq-dUYhIrIpKrcAt7wTexitWXY6rcd8vHIRWmxsc6fcdM7t5PUMXSaOeopLG-b5Q620N5vHVEomwnnI94bCo32fIctpJOuJxGgHG0aqppP-F5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyC6AL8IH2dFPtnCDNTVnP4U-nXnqDUHLo3Hre0DHE-UItSipqbda2rOwCY-iTmA0GqZ89yiS74j4a4MU66sXqm6jYwcKXJ_zB-Ynl-PpEUVtMELOZmD1w3BtmD4ZZ4vVSNxVyyUMrNuF3gs7vGB87Ll_UQZzCDmqp6DIRIwfG0qoZ0weIORBzFMrMUWHmL4XSqnE959P3vR_611YRSnwgOUzZulXDRzPoeSrBhZObZNeUMs5wD7vaEVIZvJthcJGzYm4WiwBSM3i9I-GphUQ9wHdmYxMljiVS5vXoa8I83ks4_x-7azCr8wJmCSHnbjGgr9D_RgOxzWkHordBoD8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFdDmq_VzuDqu7ErxKb5pt7jn4b5vVmBWSWv-Wnnfk2dhNK5FIy9CyKPvFBHy4JIicElrfCiQItLCnNukp97t3WfZbgJUwAs_r9xLwaq_PON27lMVO2lhBfAFSQ0rYWcSB-dfhKQn3CBm2InyhQkUq-I-V4wEd8eHGR7bsZb-OLrTAnEEcLQjKiHElXXx90BlHTxVwCez2l9Kd1Kr1qg2jwIVWJAi1Dgjx6U57UoktyUTellm29T0XPyXZhwW3WTUcjtlWlBi9CynFRHY8y_UlOVSI82rj8jeWOOx1qU1_jv70qgI_JPsOXb5KaTOVGSwXnJgbrw64yKAy5w0YyMUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhciqbTr5k8lrv15dFBTMcPTBebzKY7zOZqOmYgDEpY2RpxtEN58bOZnjiqqZtzwfzu6CTjcTw8v6R3QOJ8FN7Khi_QlrVrehukFGLkvHZ8hTvmGjGU7ggyiLcRqL9o7UQECv4Tpzy2MjshWiYgpUDLHhg850dEV9NPDEHI93OfjtNO7jINVu9AXAG84drixmxwlBTpBniAXADhSWkTrNbK7f8a7iW3O-Dd-NPnB_CW8wiulVKDEQRe4PEiudazyq_YlOI6FUtLSSVisTHoYDK0lyYMew5CnYDqUikZTEIo7Vl0rPVeAYfHlsxV6aCZl5oxWvA3IM_y5onwafK5cRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWlA0gdwkTKWrhMirJHTT25aYKtEWUQezMW8aE2x2XlZfahlTEtBZe-tpa7zeq3EVehYh4purz0_LjcYjxSG9g1QLoekLTTmvSRXC2Xvby6YBMz-N8kZXpoLo4XKyBa59j4fqDTuFzsjZ6o6piXm7mzz3KGRC7w4IqOo9-JT_ron948_bMpU3Krox2aLegIG4osDLsDmNgtHhL0863IHfacUP-QvcpJY6Kwn0zFDdcBLby22q-Dx-e7xQoz8nlpFjqZgd--pq0gGhNFRYm7jZkRKmBEYsrq0DQDfA1LaJz3u6lnD_pmnv6INlOulaVzeVqZtndI2Jfk0qTU4A2Y_1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEEv3mR2pHBav08v2Yhhcr9490hHWD6kEgowm_oPDn_cW8RtDguXHWWw60XfhVxRBOlU6rp-kbKZeOzuiIs1nNopJJ-1e--MVLTzHKQ338gSO1u8evai8uHXIdayXEKRi2LaJGuMQVnd0_msyrFRUE2pZMc15NMJ9EhYVNJQfoAhAFyRAwPN2bm07lNYehZHp_N53UeoQ_1j78G9rJbz6HN6-OiEiT0PFgEMsmzr9cZl9D8UV2GD8fs3YFgaUYBZUEZk558HmUYk9pGMstLXL67P4MTzYjeeRlctJ5FSNd0l5s5-HhnoR956QsBOYjwt9F1S3hGAuMZB-Hf0uf7GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0jYR_ijz4Cc3ngzQyiAlJT_coxwf0gxDE3C_ASy683snHNCax4-fL7UdnVb2aVFyTBjeJsJsmWESn2iQC-N5Gft9u78V5pgzLBQLQ1oix8-EaMrUzSpTHr8b-7fc97kZFF4LFKDJD5B6MPMqHDmGUC-plHd0whn8QWj72SJ6vMg6ulit4faJRsLPRnErtadA6PP8ZutdePkf_SfJYWMw0gYjm7BBFSPTCcRPq3M0pDwGSXJb0bmHjBfPLHhwNjml43rVphW-4ZJKAKj20y3_16oTIAJBwDy9PzvU7pesHz7I5Mj3EWwALzE3e43VtL6cP9_GVP9_xpVFUp7oklSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgDf8gj7IFToWwn2rPwmrcqCoO-oxtni8Ngdjscdqdhcg-D4EmbjdRAD52SpH-F1sCDAsR26scLR1mSTedTiOh9gDvHjrkRSnQBRL8_WW1zGrDw8yk3MEizqA7lIAM1NKf8kIHKdHVeLk3ixZZVm85I0eNVV-cldjlghgtR-6izEJi2DMSjIFSTQ8QVkC5ADlAUOvF60JbJmXhpRdc2rBjFuxP4hT32HMRD_j1ZPD9YTTIB3PlHnBj5S9zXpdNJsRtg4KOt7s3ysk5-QL9SXVqzJ-XN-8dONzz3O1h3OduY1bj0yXj3-sMeV8LYx1_cGbChPGCHCuTDqKlcGwHHOLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6QjbOfdftK5dowbAz2ENhbbtcqmzW6WFRXnXfK3vFc0tGBS9EZtLtEj7aPJmshxprxsURhvhVdurVJdoQd1IGz2b9Itq335RAPRmoB5xZuyZSIeKirCcWyr3qegKKyV34HbLEluq1NbYOgSXBx5ohZ4f9jOu1UJ3vfJAG2WY1xX2dlEp0pFtc1dT9cr8E1T1uR5TkYZI2ghLZ-MIrbZOlEqZL43FG100c-R9vNr8aVWFWPfmko2LlBJbUaple4Pn1KMumUX_4x6cGttMEy8Q0ujMEDle7WUi1oyNhQ70a1RD8OFYqEBlWYS294GvzvJURd6pZVEIh08oKtCZXhxqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfyYwW8buYPxJV83dtR0kUoiU2sBcjCB9Xv9ruF_oLA99AVCGcJBznNuhVweppFBx1mhIbb9Q7_GTDxvxEsT8Ja_dJsQFoh_hm_dKMHVnGfohFJltaZ2uWYGkqHYxRCJZA-A-lz0KqXLFA03sl_dyUW9gC3k9Lwkmom40QPHk5KQ9UEHnSwFGJcngSTnl7KosJdkCPd8vFtIw78QFLVKoGvpb6J21bzCC32InTi3Zv5TI3mYhMcqZCb4TvEigknecFyNW8bP4sKTAvsXxWbKRtCzqwthYWmlqQpz5x9lioV3puCrMmwFVK6VYuJ_wwqcBpvUgdA6yZBT6xmnSfiDQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK1tUwEgx8SIrB9PFyHICPrwi0Ntpp1ZjQnynrgCHPspuc0b9xL8PJAfdLf4oF6pQ3HcrCqGnZ0vpnRjeVqBw21zTnueNfqtwmz0U9WfoEDNq8KSgNs13hHaOmmsvQVRgj78DVNmW8i3UDj4WXqNm2OWOm7ASip8YA72petc8Gzd0564P684F1fI15ZXL69cqVkafFta5QNjeeRdfO8wpSssKC6cw-0mQ17440lBgm-DZ6rcvWPYGuo9U1_FUuQphgmFw3qihemBhYfNq4jXRnaatNjd0PsfWiD1e5r4nbYqFBZ0ZKrK1ImKBL8Y6Gpn0iaIKKT9sGm_ip82NVW97A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liF7Qlww7ueUDqP5TcOWcKSvyROYJ5YTKMg4g_BjlIgQ1VZtcfqG0l0dYEgohBksoAeehLIm2eDGaQMqO42Pm4XAO6zZDIA83TrS1P9yui2zuXs7pW_M1kxVy0-_8kdQye2aCh3uBwraw5mZyk0yQRCWLSNaPYy54J39VZXR2_Kkn_SdTcTDY6jm9aTzELkLzzs02qKCmrQrip6g28CvTTu_GOOXVAyTrjd-1SK-ROWC_ex4Xd2T1ouKLqZgx_v-9_XltwVKABg579TYlTFihYfrvtQqCARxtWok9d3zhIv6wO8qoHq4OSP2fpIGZnWun450jMwV2666kTVGVLvIpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REgCV_IXPwITdUUVmqr6YuVKt0c8u2Nll4TIbDvx6OF-mb8F4fiv2e_dHlyNgQzjJtA0ZJoMwmXerq5KDT_8H4TboYtpMODDKt6T8pahO5VGcd0lSn9g4DTjFct8M1CCsoPLcMAgAOQoIu0yOeDNaEtAvZibJUFm4IC2yIP6R5wdGo4nXuVNVUaE9coMbhHGbd7MgL6F473EDMeoIwl4EpwW2zQ8pXdoCJwBL82ff92J8tWAjPXnrJg-QckqNahAv3wcgA7z1Lst1mXFzx8RPqmBqfVsaqzjMGH3Jxly_Kgb3RgClLb5-YKIqDUGSP55UmQpa6efki-fbXPuV82ZlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck9WIQvgatIIdcODTnqXNjLPHGkpLviXapA1ot6a_MS0RbNOfL5h9w3DvGLN_El1CkgE0WJFOzIW0AVZcftknV7GaydzXgUx8lOAGBtbiHXTFuFOHixvq3e6Vw3dfNCsvxb5DGelmWTM2N1gks-VSXnFQefWm7QJxKts5C8wLI_Fv4QKY2DIz_wd6lZcIN173j4lcr1x7BHEG4ciqOrXmcEs5D0VkZ43WBk5SDlr49f1NYFxEKxqWcvqzT1KaKndT1vL6I0uq34b-w6uuk-KYsD98ZLxGNKONyUWNem31QVU8qhMOkoQvJJ2oqY4_0-vdId5-alGPL5swbZdicPZSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvUldgq4Ax02RfWmyP6z25KfGR9gHPLpfqDOKCM8Y2urjKt_XIdXufNTMxLMGunOgZ-lY2h3XE6JtQls2eoiEfXbACv9mLE84JGLGpZ5h04Dar8QCQEjDbOw_17VczNJJm_418gvDPG0AcYyi4QmBw-z-v7irZ_VkBvJ5VkwwPk5jVV-i4RVz3EylgN7aNLe219FUQ65DGIVqh-JXcAabCLU05qVn2PeXSWdfcLWA9n7NIf1kZLISN2wywL4alE0cfWjOmSAwnH3dzdfqZ3xZlxfg6p3j4miMOT4j0JV4ic0tTxHhIlbmFmhMrIUBZ9QLpTsfXxwyphi9TiO1W4sBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sk7txWDbpfGJPlvY0gMI87xY2zfs4iM7qN6QErjpGee9UEn1WVlRxGQANbW6l13WIsvLu0O6IfSJdalu3Ao2ZY3Z7ca89wc3U4BjU8pD3M0dh0GgjBGShr932t2B9T5c1VlGU4vE-k4wkalQ-q2iO6y4bE2JXDnCviuLWDTaU5OtS1yM5mlm02x3xpIIFq4wi2gi7XW6-VoiJu0mZxyEPNIfmD_pSW5JUDm_UsRgPcKLgwHxgZu_7F0Tyfx6Z0CLpKnsOibd0mtPsW9CPvtyKtryOC7eZQFmIzRbhvd4aYwcVASCv8_0QLcquxH0ovAcHIxvHoqAaHpDS1m4-xixnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=ZHkl-w6MbGnyBDyyKMFBq_1mhVL1gEGkUAdZ84XNqQYJ5fexY2h7S13r4GyE2geRyCINhJ_IEkVTr63yzBC8193peUQH27Yd7RSAxZEU3SMBoLnYiuj0xsrB1TFKvggPF0znVUv8VxaQuP0XAXEgJYU6WuRsCBiXeUCLhfqyZLfKjA6p0j7-V1nIhvOnweBGc2CpO0tTsP8nhb4OZ1UtFrEHtPQrWXaAvSt3Das3iu_ck2jAE-qXzsVDETxkYb4A9TTACG9BBIptvNpoxn1vw5qh1qT7ed4G4i8Q6nvnVQA-_HPtfYqlRZJBAWZmyr0z_9WNCE8nyaqMIOguE3iKzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=ZHkl-w6MbGnyBDyyKMFBq_1mhVL1gEGkUAdZ84XNqQYJ5fexY2h7S13r4GyE2geRyCINhJ_IEkVTr63yzBC8193peUQH27Yd7RSAxZEU3SMBoLnYiuj0xsrB1TFKvggPF0znVUv8VxaQuP0XAXEgJYU6WuRsCBiXeUCLhfqyZLfKjA6p0j7-V1nIhvOnweBGc2CpO0tTsP8nhb4OZ1UtFrEHtPQrWXaAvSt3Das3iu_ck2jAE-qXzsVDETxkYb4A9TTACG9BBIptvNpoxn1vw5qh1qT7ed4G4i8Q6nvnVQA-_HPtfYqlRZJBAWZmyr0z_9WNCE8nyaqMIOguE3iKzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5ylXmlEjbp8VezEnH2B55D_dbQ_liy-NZJvzMkDb8iv6srwT-okslAAu3UCkjgeyC6wvWX0OXHWcGinLU35WehnMTQhO95CihpnuvVb9P-RsDR6ZqXs8due-MttuEChsI8ix-Db3_Kb7KMbamWHP3rZ0tTYsbzKRw-VgASBcjqw470faK1Oj5vphH83TXpHWHQkC4F-On2tn6yIi6cOn_3AFMPfO-KU-8y2GmSer82BGXUgVSTZRvL2ewlUybjMrGkW7En1_Ep1Ujn8P_SL81QxPuguzRNRrn85_gi2-DFkHDtzncx4TMekmvFUlVxIbmh8VR0Z9MQD1Bl8riKaWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Fq4v20Lj5j-jRKo_RYLmDSfzC_K7mXdWjn8XOVf97GJRlyT3HnTTKuGbCkfRiHLvAWKJdNkTaKLMNqKiKet3ZMeyy7I_POxJpwNdO7TgkhuZHyU3E-ugLizykmg-xB2irPNtAidZv5tXl4x38kXaSS6rPwqOCDvkl9Y65JG8OLWBQ6j7CxYapLfyelr3Fx27vI5YCUJe2zbT0iyKkHQbO07DhaWoBM0uTG0Vslj7X-YQ7Tmm7HsEe0t4bV0XCC1SylE1JTzeu1o0yiRBx6wyablj1_Fv9iDsYlZUAtIOayrLk_WVw-RDB4nMQR9xlimxNpiH9V4CN265Yv202DImAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Fq4v20Lj5j-jRKo_RYLmDSfzC_K7mXdWjn8XOVf97GJRlyT3HnTTKuGbCkfRiHLvAWKJdNkTaKLMNqKiKet3ZMeyy7I_POxJpwNdO7TgkhuZHyU3E-ugLizykmg-xB2irPNtAidZv5tXl4x38kXaSS6rPwqOCDvkl9Y65JG8OLWBQ6j7CxYapLfyelr3Fx27vI5YCUJe2zbT0iyKkHQbO07DhaWoBM0uTG0Vslj7X-YQ7Tmm7HsEe0t4bV0XCC1SylE1JTzeu1o0yiRBx6wyablj1_Fv9iDsYlZUAtIOayrLk_WVw-RDB4nMQR9xlimxNpiH9V4CN265Yv202DImAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEpFok60ZGmgvk54Z8lxHo9Wyfa5HeBV6tZKcLUZwk8NwIFQ9gZ6alpM5jJLNi_nOAySRT85REKmDaLTHRKnDT4mqp2Bpqo8fUS2xCFWTTQb-IkZNCuYmVXY_IWHf6KO-x5IRQ2vZ1x43bv7Fuhqto7Lqtad_CfBHKc5ekm2XI8uv3vPaFLPoONBh0oVcGbZrhZU7XFpADJML6nMgGvWCTHRZWdvgjN1QF45jiyBGfWsAdJlF3xtFxf5AswCtTHKEcOGqEPDfHz1lHHPB7ZgEcDF8vWmKOJKUcA4afh3j6LvPizWLsd8KpcZPNbPkKUS5p7y1QgIw6zJ1CPNzpY_3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF8dRiFhhKdXItFbgSz8T8ieC46qej-_aw7eMe3VKwqKR9Y1tpZqa-YNZxpdHNi_ZlMVx-LkoD-M2iFSwJhuQVhhPvoWoIaHNAynSteVNlz_TmuWGDzIkZLFtgaK5yXJ0S06QtadRlD-m2PbIkFMtK85DLVhfAwqBUzbqleJGaazBtL-NpsdWzzWxutPOl-gkdWGxlCASzplUrRKONOrYP_EuzfaNDASchvOI6FpMXzo7pAIZH70wu90hTz9FCBbBrdynlUlo7jdGUEwHCJok3_6rtW7PmAzF4Fs-QXgrTRmrkByMxq1tFlQ0UugPBGPy0QIJkN-5StCa3knTsJFbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVnr0Ac66cyESoUfcBe64GQAXns7kTIx9jpPWkXYisS1fjDZlcW8RtorqHvJ6dueS249WZnCDK0-a9l_2lnJXo0gMrOhNGYgLQw-MQPUkTrgDgUDfcwUFU7350c3BG6eHLZeQK6CcVZsOdpPv8aMmBNOQPAljCwJiU_l_16Qs6io1-XvEEmXahZs2WRfMvi9tpCyInT0hXnWNu0zfR-VY5RZSpfNiuAnphlErUj4UhXsMWC3-xzgg9O2Dt0wrJfOJ7242uD-IIKUbl8xQYhoay1dKoTJbntZtmnpSknEhqdp9wjRHhmGZrj7xD8US2-yKPgrKEuiJKNxXiP3uCH9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQVec7Cs7J_1mCRH5z5uTymWr33C7VvkBBuaAFg9XignmZi-UjpPXsjd-mi7lFN-ShPsK7WOr3Id-hSpzJ42WEVqEhsuFlKX7R2aDUcFU2fDsQhZnmS65wWqTZWNQ_Ls_jwwh8VDtcFSPNk_396EYkOVz8CKPLe7By95QognsUOECoatgHUWX8kTDQVjI3fkkwtzHhEgtJaaV0SRc1kkOwghYrJCvaW3NddtVjlB6g7NrlToYFcs6_nIPmC26iwXi_KNXjgiUsWCXWqu1mf_4C4Fok-GizCOJKqzALw_rmPUQsgGaQt2GNuDrFjReNfTaHBc3n1TucFVdsY8T7NPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRrzdqO812sKTRMMPBOPcuGOJp_ofIlOjQ92JAlp654k5OF6gYxkh5wvyFzaLAPvRao1ZbpDdK_dIXDTe9OJwGum8JMqGicfNw9vf4idk5DO9-Q9Q_-vXk_6R4G-M0cS1mngLPuDXFbH2hwt7t4vrWfuvBJBbtNrf85270jtsshHa-wBp_9zovsmefBjeWfnbZCmcLKBBrVRPzCUsWld2eFNPDVrX0yeKa71woBTkioIt5HkmEAz9CHVEaPYS5sMviUdaIf4x7xizW_Xe3IgEnyq7TTikLUgUKgRNmM0z7lHA2bLNT2UCGImdBXve7sQ4tWCHqmjOIm1RLsqdld9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgOi8Vyz_zi5wLdqLugAogXNfV78DtSK81NW5iEAWLsLY3H4v3RFa6Ox0ZGCpGzPtIbFm6hRDhDbCrJOlobxrv_rHwGWWrDpP9HpDPWEi112LVkrYcIVLDH5_k6e87s372iOj-CAm2KtFehpS5csB929Fhpet9Dgadwji5P6oZUzd2AqX6oUAi120GJVh1b3jNni2JVsLCPOMELzZPRxDu72_LbkjkUIro-xRSVdkFbN9txqD8gf2MB2GcV5b2JgCODFIbZc7QCcl_uD0XntyYV9dO0H7bgJrootAo1OPEdoNuT41ZaWKXoKnfQePsWrnxBfAxqOSH50wSRtBUl0Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqzM6-LG24qvm8j0c7bq0r8unEKdsk-aZ7okAsCFsEoYotyapM3GonUe1hpOI0_HNH7t5E9W2Z8NmULYLcn0mit2t7rdJn0xaGvM1N5CKlzpBc0I0Dyr_fp23e_NkmD1lH5EQAVw1ykcKzkPIndUTKXqrijAHGOTAynrCKi5Qv1vGcTw7qrrfvSDNEgvV8QatNB7am0EZs9ILeJXDm30n25ITHbTWt1bxm3SY-I3uub1qq8yrFSw1zjzeT4XCbC7pBUMX4axrAcJoR94J55GI4q-7uvFNO6aZbL8v3t0Tmt4z3P7VYelwwj7XNH4uuovF_9JJ_T9xbe7fja1BJcIYQ.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
