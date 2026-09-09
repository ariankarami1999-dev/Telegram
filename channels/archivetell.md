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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 330 · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 558 · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 706 · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmpLEVR7v4j-ktNPEmExIVo10SjXlMp7D_GBn8efNSrO0jhiPiAzeMBfZd5ExqFf5M7oeBvtXG31rQcWNzx6sX-a_Y6aIhcUAIdykVmpkmVDomWTgYm8S3aQPlpcUYqVqNR9UF8L2bE5Jmv8H5sc6HzZYiysQuc-tWUeUHU3foL6EQ9f5VrcMjBVooDVJCcyotkWjc4BehB_27svfUwGtrfxOxsx-C_4tvw_AISNnYjRbF7w48x8VdMaRWU0ztzQn81YgWxfZABS_6qgpsnNqXAubc6NDL1DGP2cOnKEH2-zNI0IC_PGbDDqEf4EvcppDtHx1r1uIfPTemh6UHmfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 912 · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAE3Sm5ay9M3cWg_rjBnwQCbK-aTTNiL_X-HugsAzs16y3e_NMrT2WmnpEgvNokozmZihR8wleFYIWgqbFYNI5eQDJmPT7tNzcbzqj_7C8yxygtL22HvXXfkVpo6uyc_kJG8gSxE40Ryi8S7Vw9iZZ5GtABn2OKqgwoXOitVXBzF7pWibm8vYTCaQQipQeePFfB3rTe5ZqzsWGP9XlFm9xIYGaET-N7_TXxZjs8VaRHnkcKyCietjDK1MZb1T84e_C4DHjDfF4ZLw78zVU5m-sgSN_XnkM0s6VwpZyF24W3ngqa7ffJ5ywUSlpxdkS3TFDlrXwha5D2fd5VUcFWhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=BEzFFtJ27bdr9Qx-erY_TfUbVcIEKp01O067tqzm27Ksds-DU5RC--KNioBRd8CgttqKx_mfE2tIW820foZUYyqIE1Ud0d0wfEBp8H7FMsrayWNmu8Ecz6W5HrqTKbs_iJltKZcC6ZQGVFbnd0uOHZANCahObSF1J11Nqk_Gg2u0xDvVvVq1n46Mz9ZwwoeJRDaPwFVwD6_e40it66ymjWexkYZBSYus5tEiGmS0SZdBqAutYyxBp-0z3_krjG3xVbi_pwa6UP0YXVXkcgzSMZV7sY2VxSqHFtMswz8EyxqtIOmcE7v4DOrkWQ5mA9wLlUdgn3bUDiVNksLiQ9vC36M7FUiEOKcg-2mLtccc8f-qIfA07rWMH87fUkyCBn7AZbRYObSATcn6lCR32x9Nh-6D9sUzAtpwuaZ9jqqFN6LVWtjdDQ_B5VOk5_FxQv7Y7-LArUAzTdn6x0L-tYAeAhCQRjMkB1LEG2zwqslVK0Oxxo4ZTFPkhYA5gagNkV4E96FXc-x8o-tCdCkBvHHV_NHL7nlza8Hx-JZBaC8cPvitstqrUd6E_kVidTgMybKOn0uH82xoELDrXrXOcdah_Xxjd9vrKbzsf96Lwhd2EWqtIkIfe9cecDFhzL8Hcxc2JSxrIQ0EjbrVmJ6WBXkDYXhbrreKDQGvliU-JrKH1bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=BEzFFtJ27bdr9Qx-erY_TfUbVcIEKp01O067tqzm27Ksds-DU5RC--KNioBRd8CgttqKx_mfE2tIW820foZUYyqIE1Ud0d0wfEBp8H7FMsrayWNmu8Ecz6W5HrqTKbs_iJltKZcC6ZQGVFbnd0uOHZANCahObSF1J11Nqk_Gg2u0xDvVvVq1n46Mz9ZwwoeJRDaPwFVwD6_e40it66ymjWexkYZBSYus5tEiGmS0SZdBqAutYyxBp-0z3_krjG3xVbi_pwa6UP0YXVXkcgzSMZV7sY2VxSqHFtMswz8EyxqtIOmcE7v4DOrkWQ5mA9wLlUdgn3bUDiVNksLiQ9vC36M7FUiEOKcg-2mLtccc8f-qIfA07rWMH87fUkyCBn7AZbRYObSATcn6lCR32x9Nh-6D9sUzAtpwuaZ9jqqFN6LVWtjdDQ_B5VOk5_FxQv7Y7-LArUAzTdn6x0L-tYAeAhCQRjMkB1LEG2zwqslVK0Oxxo4ZTFPkhYA5gagNkV4E96FXc-x8o-tCdCkBvHHV_NHL7nlza8Hx-JZBaC8cPvitstqrUd6E_kVidTgMybKOn0uH82xoELDrXrXOcdah_Xxjd9vrKbzsf96Lwhd2EWqtIkIfe9cecDFhzL8Hcxc2JSxrIQ0EjbrVmJ6WBXkDYXhbrreKDQGvliU-JrKH1bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=snCFzFBmxuaICiZlzDnw7C-sPX0QAnIxK7cdDd_-6TUjPRwHzd0Sup4SrxX-OVKtORsX0spHaWvq8FuOQc-AnB3YqKfbPoMC2iUGogEG7uvM6sL6V6MaHKGcu2EvA4rN53J0Hq0DV5x0UCN2XpnwFvliZvMlp5Mi-fDby0I42VQoWiLW-U8-_6FcEYkPtbDs4_SMm605zMHoZbSRC5SOqUC6-7jnVMaJfIypiAgAc0tcpgAYcOR6if6M-RIuaagxXE00TT8vibJRjn8SDkLFJ2ZPDOnHcGTf--t_uJFildOUMZvrZkdCXYelYpT0jTXi-6DP28BX93SW6WIh3IeJgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=snCFzFBmxuaICiZlzDnw7C-sPX0QAnIxK7cdDd_-6TUjPRwHzd0Sup4SrxX-OVKtORsX0spHaWvq8FuOQc-AnB3YqKfbPoMC2iUGogEG7uvM6sL6V6MaHKGcu2EvA4rN53J0Hq0DV5x0UCN2XpnwFvliZvMlp5Mi-fDby0I42VQoWiLW-U8-_6FcEYkPtbDs4_SMm605zMHoZbSRC5SOqUC6-7jnVMaJfIypiAgAc0tcpgAYcOR6if6M-RIuaagxXE00TT8vibJRjn8SDkLFJ2ZPDOnHcGTf--t_uJFildOUMZvrZkdCXYelYpT0jTXi-6DP28BX93SW6WIh3IeJgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4yjj5cz1pPDWKvMImwm7whXU-cui8q-zi6kD1Nm4DX2UI7dUCANx_ypI0Lt5RQ2KNGZNg36DHIquJQ5Dx2SO4caUTa8d57Ntk1KDpKTNo1IA5ejtBSLLZmIvVpl1CLu3dIalTBtUTNLLznp_LTj7KRbB211853y0MLPu8j_ACmIEPOPl8M-rJwMw3CDzgIWE1dSe3vA2wEvEjsnmj32hgHdUt1h73BeDI6FdoAVr5lGhc9kOlr--f4dnAKfGau7xHJojd0uM-mTpcvFYn5sHW1bzf6PlQKkw04aQf1acTnqYLCKQ-qef812uko8KM--GiWvQBa8xuClFrk0aypqBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amg_QX94P2k5HvtpDely_S-CDxtNeCsuFW2GjW9HFet4TpdFwCkHu7uG3UVlSGFTAZqRsz031rLrRKCNJKJ3-JY5ls6i19P2xN069CgFQYw8IwYo1evp4IWoiypk0yHkHGQrLlbL1EIxQV7moryGBvkfxQ5oF9Daf7rlkfpo-gbDMffKDPTxPnNeO9GQBsiCmhNxnkQ6uzBI2yig4Nc6utZX8C-TI2cC1yts6uA-C8zBUmpavgjuc-5c5_P8nxy9zsjXWR-ghTDGJFTvty5RmTgb1qKJR4weoueVXlFVg_ppz3txEBvANITI0deSwQ-6lICz9xa4KYxME5glYE_z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mS-rK0XIV__3FewBioU7BZmdfxfCdvt_h3p-ztw9Tzx_POhar7UzYkCHa-b38ZgG5Xa4Ay3Aw4xMwBaxw8zJvyXSickubW_fERVGDQLpA9yfcpBXN-WD_CDjXoAXXt_v0Jd_jWB0gY-H2doLCNszyExgqs7GD02ZjRBHz-JSGLrqK3IUuzRXx9ho1krm4nhA-_VBD3T5On8PGClxW1SGLJnYcXMNI4c9lgb6mpUUeOzErNphA72d8oVeYkTxN6-gYkpu509trdemkUAlYVBclRDT_5za-U1MTglCzkKVAadb76042neAaUpj9xLTuUjczGUJQX7ZhlrQb7KVTE6pKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2e1h_u0YubY_kJ4KObVm30y6jrwDPDEXIsswIkKO6NSzntm-L-iurXDTsM-0G-RmEdPNUVBxz176-_jiujXEAyFokOZQObmqATioXtRKJSq-SPIQmbKAtyrXv3prRgZ_S2-IDaoxMBhZk8_fvUwAmM4_EA0VB-ttSd9u5nKrNAZB_bqaC8JxKuzoOxKkDi6lbQRxcgEBErq0mkzRlT0bOqPMGh9yg8-pi_wN6xoB9FKJq23wruyfwFKyM_MG2PKxRL5bz54FbTP4lDAjJO4YgzrLvWzDDupQdGj1_J_3UEu7MrulmeUzHkbnDe0U1RQv6eG4BCUJW4hrhJzUlZcrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8TPFpEnvTxoriu8P6_9PV0RaeaGUbPxuYdJQ43GWVqzIX24OUv7EYQeOd4UivKS_WSZ8XFN8eOp1kzC9VmtpPmsE977mEzqjiixCsTmFKzBTP6-4mg_bQM1Kn-C1qOjgHW7q33Ax1IkAcUrmV3SnTP5rA0mRHrdEN3ag76L8QGZFnP1rNKcZ2njlrkqYdEod5wYngxly-KXh3N6oF-1lIpDb-UP2mxIBAFHWKn8IHgoNNq8TW_fnaSmZk3-KbZbuYfrNC9IHPvwqCK_XPwVzc763RbiV2yTVMmhFtK_ImA6LRQhhirI8VRwc_LMf3YgQL_HqVmsiufOqrNI1cSElA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=oJC7zb0z9DptsZmMq9-c8wEcedYG4kiXEAWmdeJfDidzQ4YtvFrQndr3hAiQW0hIV5N6tebvXs43H5nxhpKmYtruS17A6ts2_IdKaxnJVdmhOAHPX6dSqxq4iouwdy4dkDadWGMXXHMQzzWiJ21I67fGWKo01fqDCXOuw3aK29XUFl6R38aR2Tls9sF_aBthD4g8CwZPeIyExbxoqTOcYI0ia57wNL3ri_sNMrKLImQj6A3_v3FWofilFzBsJ0yy0E2HW3rG4cRsJUdhLmOt8j5NophZoKhJd66AcFc0k4w9Pxjqz0X-Ez_fBsBbZmcXjUyIsVtkf7SHRVNaoVwh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=oJC7zb0z9DptsZmMq9-c8wEcedYG4kiXEAWmdeJfDidzQ4YtvFrQndr3hAiQW0hIV5N6tebvXs43H5nxhpKmYtruS17A6ts2_IdKaxnJVdmhOAHPX6dSqxq4iouwdy4dkDadWGMXXHMQzzWiJ21I67fGWKo01fqDCXOuw3aK29XUFl6R38aR2Tls9sF_aBthD4g8CwZPeIyExbxoqTOcYI0ia57wNL3ri_sNMrKLImQj6A3_v3FWofilFzBsJ0yy0E2HW3rG4cRsJUdhLmOt8j5NophZoKhJd66AcFc0k4w9Pxjqz0X-Ez_fBsBbZmcXjUyIsVtkf7SHRVNaoVwh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj5r6zRrhw_YOvYlZM-K1uLBxTNq7e_DR4rxns8iRZGUvmWF7cxnBSX99oaWUpUuGslvkVyE8FDFoa0ZSEKviPI55bQn5o8mJ3ZJCGz4Fbgb3HCFC9gCdFg6u6gnK_hDdDVPncoWmIHgu-P5V9PnwTMw2OMLx31975_ZcJvzQDQbqssIgxkCyNqEe86KYEY2TdENQh8zTmkTkfm_87gMtKOXdXHWPRluDZMsbY_l1AWhfPqIzHFK806tmPLr69vgwsq2f2fTAwKgnlT3208sg2VaeAZ2x1PkigNF0u5DiL3FvIWVHpOp_9O5KOsAh-cZcHEZR4Tdaj-LjOv3W-t11A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy3UGGaJ3wZyDbnGzRNIc2BWM8KZpsmucy2xx0AfQLCzfMXnycc9XdAEGldKQkNcWjX_HzepD601GKAEO_lQ9rl0LoNgHZ0vn71-p73VGOtMXzZlmWsaEA6-FfrirVLxbgd2QHDSHIDJ7ElR1e5V5mXNv4hAnaN3w82f3x9cVXVKUXsmCFZU4oIJES_FsZTqaaTwACU7Uo71vhIzXfm1PKDRWxDt1_7KwJytvEs2YZ1vKRmUx7VYOHMcIf6F6bo7k5e0GB_mMPB7NgZJDyOsa0Hgz6Yajg4t093z6H0-Inbnsdl2DQXUtCmM-mla_-ZYuggpSdeW4qZXxg40KGgRCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEwNkDpSbk_yeHTnzOse8kwbsmDEngap7_FF4Ka2nsBVEH065-DuQDsJR85HIsXkMHJJn0PhncSt-n35tKdluM_ZocLOu7KfkEPHum-zb-LiFZ5pCFKSKthdPkyPTr8Ui_telZLCV7GMRKjuL9UbGQAauHX2IlVCDSM5p3x5nCnNIhxQ1_EyGrHrBBRlq3tcP7FyVZ9eaI_HHJ3f5AtigTRAh242ymcoXFZWHBPW8TN9K1p8s85rYNoagiy-vG8NJD7RoH1Eicv6myBxXANq0namar7BsoXNJQa6U_-jgwUWr81M0diE7bPdKMU6eZwHUR6VxsWqzW_OZtjW6-UorQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB1BMDQrZNJoVRz5VMlUM6pI9kXVtotAfXmHFJLsj4aT7mQ1Vk9jeC5HNQMlDKLwqYGjYhJ0Rqgg6vvTfqVk2QjhrqJuUbyF5lY73mMtUwANGHGaAKKbVVLufwNQ3CxFEGYVqM315pTlIPmJgWbWzpGxluK4VVUexfEmG4g5h5aDT1OY98DxQ6foTP7A8Jk3YtlyDG4VJRDLkNd2c9JWUNtJor4N4RW6PBShuvAu80FgKm70h4zBS44A-EtkwrajMp2SNw7VOAJQKVwgeoyQyMK9WSEHd362aggRTS0maJXKB8Dp3ZxFHTel6ulRP632oQQkITKI9BRh9Potpr6heA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5yPgJY7CuZ_ZY0dmyve-QX7aKfrT6QK77R7YXsQdyLnuOXun3VVJCwUG2VkhGWdiPdc97TcI7VjQqx0Y4Yt_D_VmPjZI1csVJotYuIKPYBW_1f6H7nP7rLsY0Bv3gN1ki4ATVue5VQzeBRfiL3Htj31etWoWYDW0sPDQrcPffKzdd8QoR9bvFVA0tH_gBmac7e1rofqibBuJQALitphfenXe0SB5cPg3tX9ALOGYs-u7ZRigLLpSACXoh1yI74MM6HCNuq04IoMdcOHL3LPhX_-rN0aaNNT2-F2uxafUuK7nD4x7Kp197Ur-InPtSv7KE6YRfVTkNICzBV4mSo3_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTyerGS1keyGsWAEyOkvqrMMZ9koR0bTUCclTQOq18I1amOOAGHryphz52EmfnQDilWlFh913gLFOOIMdSsjcMJsHCxaInJF74IUz4-skDEPbifIoMsLjltn548GH7-u-9imy1UdT2Sxl-3-sK_AIHxRQDunlPUEHGiC2cxLe9X2F6hKj7e3M2DTtsm6lksYcR8JKrEoAvK-qVuleK0EdpLHnApsGtgpf_mfzRhc1_WPFG2Ok5AJyCb28pBhQRfUGy5tiXvgnVm0M29lnCG_5_hZB7LqLvpRUsjx-Ftfs3t2brhzzSzwOpL7zd6lEp3jcJuDWk5eQvvQxTPbACW72w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeJsYGNSRQd8IgZEkh0_0O161evTciFZUj5uDpugCWA98YsmWD-e2U1TPj5w7gZKTCY5bY4CESP_FZZ4BPNAt25eviUesBSNKaUVQBS-zljuYrwEmOZHpYBYMkqwgtduP44c1KKR8UWBfHPPbH4bnEYy2F1cIjazEThLlO5Q4BIB_KajdkGFjWW0VcFpAz-o0UXSsuLHPrDgrWcKo4Avj5LKoz0_OPIArj6TxLHNS3S5b6qOisUiVEgMgR9YRM2lEDxtWDOarHVEicJMSQTFsuvZBC1dTRPUz4WXJ2rN17j4Dg8vwv-geBb5mMKtJ2HXRGquB4hQEiUx0t_s1qKTMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1eANf12WcePJoCK9jHa2Lx0xS7yUm3EcGVmdYwHcBrFWmW85E09A34Z7F2nQH0W2RHqyilulhrEeQE5aRTVeI689JanfFwqQ6YFHRUR3pSQ7zy3R52LvHqQZBP8LTV6-sGIFZ_iFpWUlSMDmVU3RFrT_mSCIQx1q9OOkvLwE5ITlPXxgTiwxCqKZWpHjlX-j34pprFlLzYc5EH7Xucqz00BH1Rwl4t3vJOkXHBs-rSVd_22kQxbcb4h0m7uR2JYjx00mRUVPUgsjSDdRY0A3U5kcN76rxOCb3kyt_z5Q-NkQcAwd0besexqZ1sjyp12c_UaAeEqU_H3AR-jWW826w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv7-vWMK4kZft0JtT5wZ8fN9da6K38xA6HuJOLC_8C9kJ-LV5n9cnnKBqQwyVZoNAjmOXWNtJIbux_qfKD30Zz1ponxAD5idTr8I2iWaPb6Gw4sPrUEDq45O2dgOAgxnLg0agqzQryowc44yvU3VXjMsDws08djI4ZtP804pmfyZY8bXvqZIsAqW1fpAJNSmB8Iz31NLRsk9pvrXnL41KxVf_DAvfwTdwn_-dJ7j6USapfCvybZWx2atO5AFsGMoGdYUstp6vaanu4zhYp02gq5ziLCAx4qVqNI4QuTXdNjkH7dganDMU3zQxHmd6opdy2EusNMifUaNAdIlIGCKYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxSK6PfarfSMnMuB2SOZ2bFGsC3Iv176qJCupgHBfq6m86nFIu2E2KqrbrNKY0fBbhvIoWHIDXfJ_RhP-IOIcT4qYrs8_TzaN6LnWbCjn7B2qW6n_tw5B46PGmgLxiBwS9U0lUYstfA5r6qO4hlqQ-VbVOxFoWXVrZV6m2n6jR5SbXJF9GqLaKMEkXAgTiuFfjpI7rwcVzFv4izs85y7KN-2ugceNrq5wDo6D9-VqMK-TEVqBeOnqunDLzpz3ayaE6UNPv6J2n6ozjylGc0Ixmqf4AHyVkQVoask6_3wbtA5c4u5xzBwiLLDvhBn_B3IzUGEGNVy_ivynlzxhmoWEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df8CEbXrU0qwDwxlrg5epny2YrgIEaTRSHYfkFeWJgSjeNDZC47-5jY2Xpes0vzC3-uh0YXOsI4SL9k5QxGo3fDGAz1avTOQL84pALCodI8vmDrVQSiTAiZRD6KeXGJliNTcXwlXtVGLyQc_IcWAicLmKKCXeGLPGSI_7LcNtbeFNYMj8JRMoCFHtrrQUPTUcd8gnxeQR2yEAeAnKKXxr31zrpzHdBLgM3Nayq_tL3Qjfr-jT-zsRlQhpBsGaJ_cSp3qHsIZiVcNn_GatCAgaThpFTxgFkNH2lyIgw6ynC-BMgdrVZyhuZ0pgsjvY_MY33NOEN3cB3B6SiGWTb_5rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpNDeuMALDI9PCeo8PlCeiwAmHIkLBYsQ6Sr2a0pcXKuWWtA6h8zL8bmc7zJWmxGpCDJ3XqBHeBrTjg27Hs7lPJ8BsvI9CIv6MFzJfewnS2NLck7rd8lTPqUMMJIK-vYFJi363E5INwfRV_5Ow70JUF8p4kJldw2LaVJKiNF82mHaQyQwJpWOWWEB9nDuUcP5irEwA7TulA4PVgnetRZzdjMYHA9osAZ6_0Qab_k7JXhUYXOV8tgIZILzrxKBIBpCWh03TWH0bHLj-Y2AGCfU9QdLzVG189eDqtn-Z6SbcGTFfDfPqiMRZf8mLR30Pmptqs2PzbntFs29d-v3jbmnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt7ILNX0vwi7dNbaTVUcyuBQAkIyAOQ6c9-umgKfurZzmqmVxR2kBStga_zBzjh2-QwbKqjJGIcejMAJlepk8rKrHQfMXSL35C9BjBsJYB8UydpU5-hY5m0nlrm4zzqDtwokHOPKe1icwJAc_De6H6PrvQuxBqqda-rRA1siU5383w-RwlZX9vPhLr-46xH74qXISNybn5NC5DuJQTs6Hzk7iVviBOSKq22IrijBf0rRvdEWC5QL8SQHsMWJI5JRxlUfGuj7Klci2C56waLFdusgxTvh0MKyUqK_k_E3Gp3WDBiFgkVK5XyAjX6TIPnwM8PYBRFT5Ep1fFbFVKQ1wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFj8G073yx9W-ozLyTKE6zdAdb57MKpPiXQYA7QEqghtN_f8R-n1p3y3RBx2rLsItzWKpZaDa_qEnaU0bgxSny7X8ePEsTTp3_Up0QWNOnF4IguDuZrANbkiUOvfiWcpA7Iy8cemu53pNQelPITxZg7hg94aM0VlRJEU0MUWQKw6T1iRSt3N-vfNvG4IRERg6DmqWwJoaastMTCLn4SqC4_fxfHuB5eJRUCIDPPr3hVADO45dhupe8rdSdB7FgPZOAW6obQSGIXfRusNhtBiqypBrr651XxefbhCZAA4T9ggAoFD6izTnuEIpPQRP3ps8HZdlv3Z6W2Dv0-ODw72pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgt-lirPmlmFSIyX-SxUgRiyhNpajgJFd8SxYkxIN_48RBRM69HF1hx_tBXLHEzlQ2Qm8m_5gEZWmVeAWo4RBYlsi_M7CzEXN3uuiHCK7GAdufaUBI9OT88hFvDg1JXCn0WgALCJUsMpZ0Ki1BdMw4toDdAyuDhqPRJuQLD3kIWQS3cAYxbEfzL7lmJlNsrDaklopMqNYQ5L6gi7atdOIK5BeUN7dqZcHLbBE70ypg68esHofJeC7lPnGIw2WZ9Dprj_wSYs_3btSrlQILr2Wgr9Lx0d38dCjvABcG4aALIbjSHBFK1syV7n45TlQ5-5g3O7obgIX6VipgF09mcPEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdgPTaTZ0h3hbBOmz61hXrpscpDAS7OtBxKgFH5rMsKQRBY4WEfp9ZLrSzF0-OcnUcmTmh62OFAxBqwz-3OOvqZvj-Br667M8LUWRIeXmgKCVkzF6lDDPbXt0F83ugfTCjKv1ZMi2NL2WM5IzlOoOnovSU0lw8vUfLVmFLQrCWeApeGsQc38U-VFf2jql4GZgW67_Vv4U0wVbpw5luIH62kXBFAliiJrg8iD-pjTpFZ4_1qM9pcXLl6KeEbvQxM9I-nCmKIiF9sUuMxXOA0m4ulSFl7_rXcD4aOT9vs0up9tPZmKddTuwc0y5iRTwLznLzwKpcYkzhL7AeJXQqNnuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_H7Y0NYmC6QizsfeSYnim6by29S-CexZe9-qRvGWEkBAS9LnlJBDCva-bOQfLsBiLyc_fJpYhPtqkhZz6OnJW5Rf5kYogMl1bnrtvOIg8aat8Y-u9ZrQbnbr-S09HE_ivpyejY-0QH7TiYZ6XBuCyy8UzHwjXJ-qMjdnlHWELt_X7E-hS2IYaRJsziauXJjGqAUgDWdNOMPiXXSLznDSzX7a8OcLT_4fZg9pPSOy0yYtV8CoDyiZ0ieTAB1F5EQvdRhL0M0u2oQAytNaTZoePTtWueQRU-11ui4mwnr1A454-7PdmqMo6K7zsrfubjYkG4PFXJKe-RUvAJxqzQQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_hI74KVUJO-4QrEABtzJ8kPJqLJ8A8HYP4m-Fx7mLxKSksTnsYDuSPBiCXTS8ETnzIWSBJ2x96DLmdYIrqkCiMIv2NQpzn-dhe3nyNXgCNSCySRHv59Nt6toEcqUPvhNZC7kN75slmHR0ISDpGLuFAkrGnR-P3Kzfbos0yDQ9pOdJcuHapYlV0ikLhld3XmznZyYYvgDxxHel8cobNs26MsSiWoInPucJaLzdG-jjiWcMSsCxnh8KB7sQqlZ0fznz0x0_OPOlHBM_Jaeb2afE04cxC_CG7E9X963GyAvSgR3c7ozdK4v20BzbIHth0knuRyqARq6P3XsfqzeLMt8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUavpLUY1-dKUVG2lGdoPE-RVQmPMYScCxpoA-NqkRfelyNzlkmqgucnIBtnHStjNshcDLrZR2X69zKg9zVRuc-JRz_REuUE6T_s6mBNldXsW27vno33FNUbrewdBr1j6-pIEmYlNV0QTwYweTaaVl8MC9vJG8UMvIXXzZUNcCau4pTntYaQmaljSeapjdjBd49umYPMBusnjEu0LAyAODO-12qM0nhdcY9qcGYlpkHMf3dE-5uTWc10r8ghUSVSXCDg7epl_CkOAEK0FqIa2QKvuViNzfLV3kzW8rJvySiOGR2368-KJWC1C47ta15Vb15xNUUrWJOeBcjg-oyo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=mHT1xY3olxotqRrr6YUVRiny78SSRiGVXDiwuIjC7zvFNdD6PWykCHCql7LQV3wFwdyKZszwN6dBSvjoNtAZ6J6qlrID0utk-A_CF46uOyVP0MitP259n6O1lnf6sL2mPrxtvloMVKTEWGeqY33igyN9VVzHUpBXQLoRrPiIS8fDjoCJO12zipwsFrQfsbFW125lN8Sk-Fn41EzmXDJ8mjxVorzqimJIszQkHs_Uwn-Ia5gHglXQBXQGjIUsMhxWqd7x3MTAm3yMzJCuC19zYe0gMiEll3iaAB5rWg5Kq9cM4cpgue7FxrMGYQZJvJQaPC1WXwxLOHnbVqk_aUDPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=mHT1xY3olxotqRrr6YUVRiny78SSRiGVXDiwuIjC7zvFNdD6PWykCHCql7LQV3wFwdyKZszwN6dBSvjoNtAZ6J6qlrID0utk-A_CF46uOyVP0MitP259n6O1lnf6sL2mPrxtvloMVKTEWGeqY33igyN9VVzHUpBXQLoRrPiIS8fDjoCJO12zipwsFrQfsbFW125lN8Sk-Fn41EzmXDJ8mjxVorzqimJIszQkHs_Uwn-Ia5gHglXQBXQGjIUsMhxWqd7x3MTAm3yMzJCuC19zYe0gMiEll3iaAB5rWg5Kq9cM4cpgue7FxrMGYQZJvJQaPC1WXwxLOHnbVqk_aUDPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIE_7sWAQEThXyJ_EujeUY7hZo5FkWVex5wVXE9mDOoKrfHXy3jzLysRkLBsUPVXWx7IuHA-zkyxIjhlgHUVUB2Hiwqs2NPRAu-A_ID7wYlBquJelsim3FhkaDBLW7m8mOTBUb7wjKs2UJrA0k5ffKBDuvl9XHafc-HuJtm9gMcHcWSWND7Z7BlUZMrqYVcxmDMZGZGAf220zkD6RAS4Yn5lVFCtvrScnWIld7tdMDPDMtaf0oqx4oRkyet5QHHYBY7U0J7j9sFkr8jqTZ9oTdEv3CaSKrWeQBzlV7nvBJKAXnaxBTWWjTVNxK7tBUrJF7PrypbCsgBKT-3A4FngKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZBOvzFFUr6pltifTYA5lto7BKalcBNBwIakk4oAG_ksADBLotVQhUSdnCTHIL7KA3fXS-QzhnY-hqHZOQEvNY1Fld2YRv76ILiNIM1TjJOd-SRRMFeIzi1Lwzd8uSskUZWor3rfTTX3yUJAmKigJtiFMMR2-sChy_LLLCZKu0F551VxeaC33jtw7mfl_O6LgNy5fF8kdofEuzH2-SbBNlup5z2EtO2RU0tYRGgUNiL-Qy9nGX3QjGr2wDveUh1VZUlYqVSftIE8OQRvIAkEG7hUu483mNk1kzzinac8uvbkrYWndOSpn-u3HlrWQEZDey_81YnyJfQkiph9BlPaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=ihcaqMlh04MTvmm7uycBEmGEKPZzI_SWsaAZAJWf8C9htFAqw8gFwl19JkH349AJkdADQD6dVJvo2YZ8Md6FqTEGIFPiJV52ub4LDguY7x2Le1XiTzXXqjgs6WtyIRUHoGsE1RYflTlNekIMDI1BPqwASvKdQ2C1ClnCWoVri_mhAwD-xPwgknnTCqGZ_-WM8qzG50RSkoVYcDIQvizC4tel3C4KVkJCwHX29_J5bbqdz6tOb1Sa42eWRO8zVLa9CIQ-blIhqQ7lQeq6FskVOAlx8MwTwyaS-Pcwa9OvbXmuGLO2QG0NRcrBKv7uXJJGWO_NVDHLgTuHiG1VRJYc7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=ihcaqMlh04MTvmm7uycBEmGEKPZzI_SWsaAZAJWf8C9htFAqw8gFwl19JkH349AJkdADQD6dVJvo2YZ8Md6FqTEGIFPiJV52ub4LDguY7x2Le1XiTzXXqjgs6WtyIRUHoGsE1RYflTlNekIMDI1BPqwASvKdQ2C1ClnCWoVri_mhAwD-xPwgknnTCqGZ_-WM8qzG50RSkoVYcDIQvizC4tel3C4KVkJCwHX29_J5bbqdz6tOb1Sa42eWRO8zVLa9CIQ-blIhqQ7lQeq6FskVOAlx8MwTwyaS-Pcwa9OvbXmuGLO2QG0NRcrBKv7uXJJGWO_NVDHLgTuHiG1VRJYc7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=u4LAXIT1sEAewbd7JVlJs27wBPKb84cSjS1dPPbReU70hzGKBg6fKvtjKAag2Dxd8huAuSUX1zN61E3oxQirE1I0G8MgnYRMhTkv_bB8L-CZLmw2nwOynuYfTTy5esrLzmfuXPSwL4q6in8aHTw_eOUosIEkws0VauvKhzXzNfncTfOmelrSCjvehIQt9TGwkKR9-rF6lLQJk-KzKDvGIVhbiyUJHTf4f5JCV_UHacJ8thrDOoCapTFrmrC_cQkGyf00Ld0a896HYfI2-sbc_RUu-XiqHsjGkU8fK0fidc0iDCOUpKKlKh6vItmOr59TxLQWidXOfuulWw4qBf3dtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=u4LAXIT1sEAewbd7JVlJs27wBPKb84cSjS1dPPbReU70hzGKBg6fKvtjKAag2Dxd8huAuSUX1zN61E3oxQirE1I0G8MgnYRMhTkv_bB8L-CZLmw2nwOynuYfTTy5esrLzmfuXPSwL4q6in8aHTw_eOUosIEkws0VauvKhzXzNfncTfOmelrSCjvehIQt9TGwkKR9-rF6lLQJk-KzKDvGIVhbiyUJHTf4f5JCV_UHacJ8thrDOoCapTFrmrC_cQkGyf00Ld0a896HYfI2-sbc_RUu-XiqHsjGkU8fK0fidc0iDCOUpKKlKh6vItmOr59TxLQWidXOfuulWw4qBf3dtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=tv0lM5aRX7yzC_6Sri_oPN606r9zmKIenug-RFtZ3P6lJbDAWZOyY8RpVSpjRw0Mvt_3LVO4xtzY2k1XyHYDgX3-2jZ-syrQD72qlpGtwnaO-clusT9heBYUd0CtkRWTBcuNi2fBdERPgcxUnoofxqZ6ZzS3EBPD-wPRs6LpK21ZTkkoIaxqUXHf7E2yDSEhjU_NPfMYQgyjhK3KWimAGBck4_UifGhkeQ72Wvtn9xdLrQDmvtSCWTW7YIejbgPAn2Q4yAkZnvDvtHmkrwPF-ISS37dHlkTiWM7DCk8qMg5hWsSVjTUR-Sm5MKNZJIlJt1MaoTWo9pxryqWKxM949A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=tv0lM5aRX7yzC_6Sri_oPN606r9zmKIenug-RFtZ3P6lJbDAWZOyY8RpVSpjRw0Mvt_3LVO4xtzY2k1XyHYDgX3-2jZ-syrQD72qlpGtwnaO-clusT9heBYUd0CtkRWTBcuNi2fBdERPgcxUnoofxqZ6ZzS3EBPD-wPRs6LpK21ZTkkoIaxqUXHf7E2yDSEhjU_NPfMYQgyjhK3KWimAGBck4_UifGhkeQ72Wvtn9xdLrQDmvtSCWTW7YIejbgPAn2Q4yAkZnvDvtHmkrwPF-ISS37dHlkTiWM7DCk8qMg5hWsSVjTUR-Sm5MKNZJIlJt1MaoTWo9pxryqWKxM949A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrSBJIrn_dkY9sfgkUhI-Ydpygq1xP18OYQXnq0q0CO0ANUjYN9hwWI2d2Es5gY4jeF-NNaDzXlbLB46sW3tNcStk37E_liQygqeGSNxK9Td5wOypai7799FJX4JVOYGJuUmQW_973EtLK8OwFK4qaUa6VoAKrJBAxuOF_NgDHkuJFBE_PIeW5Tu8tyHCljIfO60fG0PiSWB0fgDyC2l_01V-xHjmRmg1JzVr-AxcfP2di4fTZXIz10DG-v90pmoY-eXO95jXfPhpOL_imkagM5EWkb0oScNxBmysS57krMhr7nu_Akeq8SAfc1qFQzVFjKmay6Eicvg6AjBH492Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EQ9kzo70gQc8ZiMqwVrJXitlcOhC9qbdWaMgXxTc2uOwDyYWGC3MrpyZYK7SpeMo7h6S-XJO1r8RBOT6_pIzv-FbvpRxFVGcnVXzQu62HTNuLJhcvQM1dcvO78QxVloPdBP3jkAjeOL5YlZYx5mxb2P8yg5N0A5ytdj4ZV01xt6ZDn3D95GFtD3mqiwSo0ufpSmmoFqpBCgggQnkiedZcSI3OLxjHLGCwBLtAbDdbkuHsW5mlsgo9en2Gi9cvfJuFhTilnwY19nT6gsbVZrQvqAlsF08TvsRGa1ya2KSX82Ly5r16Fw9PB5ezX2lVgqb4BW-jzc5PMWHr9Q-0uY7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EQ9kzo70gQc8ZiMqwVrJXitlcOhC9qbdWaMgXxTc2uOwDyYWGC3MrpyZYK7SpeMo7h6S-XJO1r8RBOT6_pIzv-FbvpRxFVGcnVXzQu62HTNuLJhcvQM1dcvO78QxVloPdBP3jkAjeOL5YlZYx5mxb2P8yg5N0A5ytdj4ZV01xt6ZDn3D95GFtD3mqiwSo0ufpSmmoFqpBCgggQnkiedZcSI3OLxjHLGCwBLtAbDdbkuHsW5mlsgo9en2Gi9cvfJuFhTilnwY19nT6gsbVZrQvqAlsF08TvsRGa1ya2KSX82Ly5r16Fw9PB5ezX2lVgqb4BW-jzc5PMWHr9Q-0uY7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6uqOc5beVW9M9whyk0uCAslx9lfQeMVPxLouLuNWh3lXTVPT6_m3bsOyv1e4UmxMvDdtzKuyA9FaBss97tUBgU20c1lkgv-UVfCxiOFfMlH2QU_EE1DLVFgpnMTXrClhBai6mPByqaeVcd_GbQyX3guPX3nsVUsc18Tz-Kh1_eam7zFM8LRPTKenEd6yUYpou1sH5D9wKW1I-1rJb0Cja1ZYFCaHNCDpim2aXpc1acqpmNVC7ACmezzYrtOLRR1P5Hfc8MCd0vNbg7vwJSQ2FF0l54svClo8vY_ADI4o80eeqwxMFPTBv5kbJlCMakSocffUYjKxSThPV80yhzRWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSZAxWi5psWHWo4nh7dHWjga5M5a5ehhy3sWnDb0pkZKhUfjGTEadaXC3nulAqp5hA4knzO09zjzsaXP3lJ3gleUpJ9H2iysECMAnFNlKFH9y-osHXz_K9AbQXgXScFPshryV4oO4ZmjrTp4BD44WYhGy1fqdUXbvbC46c2H84N9hyC5oBLVqx5R91fryfv9xFeYWoyq3gn_sOtUlhh8QKLw_1Ux2x6sGrBU8-uc69QNrc1Ddmk0JP4TgHF8ziQQr8BzJj-W8T57zYGjmtIfQGoYVz9WQH8-Uo84Jd7N1-CXYQ0ATT0zOWPLmBclU84lrxT6FQPcpmZ9GRnFeXRi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aopNVOpUGKY7il7mu4QrorUd1D9c7qRhZftQyT0sVKjIyp-nSUt6p_C841nIzsST4lY3xmQJKuUltUw8vJFmZcC68fvNFA7-qZ32Sz8ZScMnpZf8FyPRhhJVnRc-mG34biFxpBNY1Vo1tBIVYTlCHpe3ITDW5v9oWprNNojpS57QD15BQ2acnl83PP_mki3Ye3YJ8xwmSk0ZQPK8acmJVbFraB6HUzVrpdww4T9icxdK4cnWxrveet-QvDJscznSgIrJPqtO-_fwkYPwPsqmEMKhJWr0ioi3x2_tN-QlntCo9lx9Cye-wKTv8wHYZuw4MF72Vb7pshe8fj8s5BfvBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGtlNhQav2RMzPfYdDxVHZwdBQprxp8EVXttHhwhbtwktOMLUqovnnnpTctCfONxPnuPAzJD9xmbU7POvXNnuMaKvhnX_hY2j7qwqP44ef69AQqRBtPcj2w0ghkgGmlOdleyXpWU5pstNdKMILoPmZzLM3PAHgmsABeRxLP5DqVi-lts6AWFTCkReSYSS0pT7w0AVLXGltAXYBfKis2nxNgSKF5euXMSB-FOcZXo6OzExdKNzPKS-a80CH_gPmgqG_Krwh6M5UZP27hxHEhmO8NMndzkAkUH46yWJhTaF2m_R7PCRCs9QZ_zhi2lkMtiXCaYATjU3ZD5jvnxJIgPJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-LjwKCmNmTe2PcInX-zA-AKbQwGv-pNvgNlUa5lAnUZqPIfBdkuMcsCBAdkeS-Q0PSvN_-kGxtf9Ew0IMTqSmz2RQYSZx0_VhtcaQU-NLQTlbW5YObMRL-KhoI3cO6jrBdLIEpH9WJVKX8f0AYC3yRBewCU9E8hgP90MKSYbkWmYZJ_BLAXJak6Ykr8ZiEeh7v5NWe5OXXfI6ENTzTqE3mhxfdpBQQ6CmVfp35atX6R-iInmv_p-k8-k4BYWRTcpfaKGvpbaGwETq2GuhLWFcvgodddxiMs71cL0tiWctBeiarVAy7zV1Fd70dMJMq6BPM27RF4hHdqg0M8eHgyTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ_hnspnMesqsbX18vP1edxgJENdCuznRaP19koFGYi1g7bJ2_TlCUK-IiaBxGuZo3XGcOiq2QaQzsm8HzMYtwPDdSNAZEx-M0h9bI-xf1nDVu_pKDCRSXGJRco7F63TQYTmv98h4KRigFdMjkgy-2WsDuOMX-znTagcSJRQqvPccDKrnL_mT28yZW3SC0yyycMWqm7x5cBydvQ43kTmZZzFqz5lZXNH_NkUCwro-FMv7MhyGtnhx53JuFEbhEFM_mdXqpuz0dO-4SK1CnNxkEYbc8mQ_Oh0kbyERaDTtFxXWDk0kL5_P-m31ZZ6F3VXH7Moxm4OIK-xkc4fWET2yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvSubC1veu9OewpGl7gKztvR6CcRbtG8GSsgiPXtcGf1ru_9IosGGFySa-uBJ2AGgnWbzuLfHaUOf46Q0LoTrVkKyFRIFn4FUC5umbIFCEcRVP4UwOE8VrS-mWrpSaGAAvrwYlWSon1SJ89FdW5omHqWYCr9WMGXPqpQDBxmo5HArWQPx6b6P8O-sMiaWtwGKvDVHNyK0LfzVVMIf-0u-k2cTp8OoD9pZIi29uWbrUnu33cvZF3VnzPiLmjwm9yoNDCDMCMrlw3rjrvGjfv2_qLcPcB4sZpWDMyi0JPP0AXgq0WsR_IFlIUVhk3nJ2euNFr-Y9LXkIrPKHrx0XH3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPTizGxmwkVrWlnhJaLzID6GK36mdDULA6dcVSn6SjmpCeQ87Z3lZskSU3qBf5UkOMmCjRox0PQsPzDdblqWOhCMHjy7JajQLbFjwWuUla8hImsJT_ype-e-EDzz0bEoVR9f9vU9UGd4cVXD4hUCbQiqR0XGLCjh2u8WxOlo45G_qFXl4th-aHI5wZy1wuKdlkgTySo175kkOdRhNiIO_HNfbw7lyf31zvdd2cfxU4YFjhFQWfXDWG7o1nn0AfuNcIPiskYcY3W9eAOiGkDfdvKnXJeECzu5cfY_RO62FHSfSYa6BSUSJqyXEIfEV5JDTNfar23yMQcLvcOqOOS0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiOAbBmu6gAjVP7NXI-pOrrtQ_9yqWK_7Iy7wdr1Y4q7OnNDcI_LrwEsnOQt7FigFSEa5-I6OtjvvapKnpvQFrzWb1F8E8M-3GmdSLrEPtwxBJoogLx5_UC2VgHJBflNA8ZG7_GhTUCFY5jepYhEM9z5WCXB5xVvu2ojwNYXD78iBlE1vW_1XsJzHBezlztrcwQ2nwIpphLx_WEtgBFvcDbgWrzOUQLbEYR-HeATJWYeTUz1-uT6vgZQ3UTetbhm35CU2FzqFc_d9xzDDTTc53Z4au1IRFyJnE98g4QSceMXTTb-EPHNSUMJj4H32JgM6QRfsmkO7SvSqDmsNwrjLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfuRWyAN6KzQJyqywhwF4Af3ViD-5wc3fvNIPr9ECbGrTAiUOF7LEYZrjFAhujDMmUhF8utrRvOxStvuUevrMNB3IL7kiobYSjU6H5ZpekjKh-aRl9G_dh-HqsGvs_L7iDVcmn1xHgps29uD3RE8-5UJ0BgoE1XIe8mdI8IZYJZaIvOGUzO1U7F0XoqbdJf-yjV5v5ukCQqOg5fBOmoD4ml7FN5jjS4FaTri0gYnNDYZc4vTrMIaHkYgGFjLIrIwnJVjAWaOmfJyxxERhOcpIRjwYCD_KrUnW_IsGDjqhBFIh6ciO8gxDRS1bRbu-t-QeAUc7hYCUcsBRcONPuVvOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQQN3T0kx1hWiysy2XIEeBx_uI9wNalA8TuQtt50uXiOo18EKIhVzlTiYE67jvXNMQfDHs9kYhsLza5p7xxK5wr5xd3LlV_0BRc0ysYzTrxLcStyiFQJwBSenp7e8Qe5YzzzngOJY6eC8LAU8UVlar6zTfoH81aohOXfw2cXq-RGkJ1Z1IqZ8AXggAJykq6sOWnXrhiteDQfNwPQUFA4mGYP6-oNFKrjJ2AgYW12ct1emOJO2pwZtNjPujFHrQL4WVnx9RX77H3YsZtzgfd_zWplZaI_qcsfA4wdSOVwvaBItfzH7V2Jg-ONPhxnlOc7oPuLZGX8kcpuezFe8HgL0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfHF_xvUpD3nUUooa8Kbxwtwf6xTRi2zC3QlHdWVc05ePGj3F72j23keOLAk3oNsE2Hy3DQI665E21223nOXWGaQFYB-jbeDvAsLtZtjNHMJk_OEo9Ijfwfh0WAYUViCaaBZgD31vOQQQeUoe5RAIwtIXJRbDjl4Oswx9JMu0YV1_ImY6j8g8SMvS_h5LL03AFIcNld-apMUfvNJw_8CSpH056sP994SHWYf9xyWICN1bRWiELVWMzNUkQjV1MCjSfX9_qMsTAVJP49X2dKkmn-3Svglsy0NZB6cr0FY2nF-pNMmKHBGLkoZIvJkWpxzQ3X53MlIYqYIYGe2I9ZT1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E172hdq2b6tVbSWeGZ7JUp1sJjLqd-c3Tf2KXUCoz5jTlKAdAYysshfjyYCfNut6C4zbWccnabFpcteLJmmbbuuvaZ3PcwggrPrwCBxogXc7VDc3zmG5X6WLRyNU3rfYoSHcB7pcVs7keecNog6nxrtBcSbArzF5q5NxxX2kIE1Xss307CVnAj1SJa63q11XpOP0CraG2i8lTuAgvDsXur_E09WqkPh__yvyZmDlBXyr0lkBGKfjYANtmnrORQ8dHqG2xSSU8S4oP57h4PpbVXyio3MujigJbn_lJL3RfnpirN1xrMLNii398NyzKsf-BIXLZz9QWz9lq9cvS7SXjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI4djF-tZxo3Io-oqZjzgzw5QehlzW-tG3GNoz7v3kZur4m6JoIPm8MVnBUFQY7DpsNuY-RahSzrRL4Pdksc0Y9pAAFrqytOQj-t1S3J9J_AaPt9haJvMymXXHWV1t14MH2Yd30MDIAHPSG0R1-aFMVpAcCfhEGFq3qCgCgPgKwC6Mels2iCDjYmuTfd0f_5h5EyesBDgwIMGmpzpOM0CH8i9eKKS71ZSkoxDmljVt32f2T_zlvsFiugeVGhJEdiZ1ZT2sMinAmiSFrPmht4i-2VUjT92F0_jhEKS6Y_pthkXjgsakIlE7AHpn38xrgj9PybyE45GzEud1pl_yDf0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxqkGDEkMOoV375MLzvQPvVvP3OyCgjW_IvN3RHBXDRuMe-suqUkwSUc0LGuvOlDxVNpGSTiEqgk3bmdT5DXhgIsVPgeHw0t6Gku12Ex1GbEzNvZBLqWESp03Kik9yZwarRzB1Zch6PGlhp7dIfOFBeshGKoUB939JYBq8CmyzUbWxGo5-gSyuXpfkcBx8E_ERrfa1qTlwWluK3XMJm9KpvlF5dKuuOTCmbPivsdf_gk9STFzSPbkM1PtwVGXiB662IWbDclj3Pz5lqY-I9-XupF7_bK8IYNbA1L5I0k5auGmz-6ihtqPyusutas-AjqgWQ5zGA_vXMSX1P7k2Hpgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMrhfHJOAQKki7FgJ6fCaBOs8zDHnIMca_0cUtCGck--DAW1tn-cG0fFMdB9K6-7tG5GYzlvqew8x09Q3IHw7RWP38gT48zMtQWzLn96QemkBF7H4ODgieIzLLHoSGtZkuEBkNrEiHJE44jYOxz-0lYeOumcFhfBKU8fxZS5bSd2DB_iYlk2z2vu06vtHWDHr2swWR9FR-6bcEztu5AfLn_kR5CarOU7UJOq0NRfklfSXsID7eEONijCtvMRwmbjABFiAwuSYZBghh4C_ItSGYsT3HRVXiVOtPGqA-pfrvaI0vMdvQs6_Ag28Qe1o9eUdy3EsXTMV-eeOOEJtY57DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReELwPR1AvX_EifZ38ZYk-ZNGLyGMHeAIBMH2ZPsXcJ8aswYD3ucwDzN4sBUSMkfOQqptrcGXBnwq_T0DpE2xISwv-va3vsl8dx8XCZpB6cdrHrupTXwgn5BjZGl7YbRN6q_PR1BBGr7TGM7u54UU1PPaZP3a1B5sPCIsfZhsRbbXIobUNsm0ta9KnlSqnplBW64hLiXr3DHoMhX4NAIofnBgNvdDYdSukr8Gp71jE_ZvoyWvP_dqN98EwC3dHqx67Ktl05E3TPKlMaM4ARSwA3-JjPRfmxPLSq3PHCKtuD-NNt9DlhNwNQGxJ0KhFsPplvHhJbSAqyQ2R_U48dyLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc6MRlzsIdhKb7chRbzwYD_ustwFhcLXrmoKh_Ni9e98hbGdPmmtmFK1LEEQjjcl-Y348ksCnrPIbVVl-kp2W7Vth1cHV9cWN9n6dec47tRXsgcNOXSkmCxgMcNIJQeOL2ASFkpDREcrsQ7k9SmwkxFFN7xEI8cwonBqqSwZeKQC90uC_Bbivs5IYa3b-pfCK5yfhWhRhuIg68Xn3nPV25x96TnqN4VDepG3uJddWvpBSq_9nIVFzxhaBqjwRiqx6nWyCbL3gtT3x4_3ZqZJKnrnBQ9WqDwblDyTYpKIvwiqoj3YJAklfBTNd8b4qGXd2hIGY79JYOJjgze-78pvpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=K3RiFIJeqwMqpNoCPDqxJjTMV81ExCtP3A2KOz7jmApRFxloVsD5Pa81lKQo14ojFxA99AGAva8vQ1A8S1tAViWQ3iDW377VX6PHtRkkb_uvnySBgx2oQBi5O_8URMDGfCwk4BJbjQRawMo1icSbOvH8OdOWlKXefBf7C7e-yt1o9J9CZZxwLgvSd22mXzuxQr1PvRPbDW3BUcnJWZEi5_vkmaTo2dVESyG1lseaMa_XS_3M3sCOnKHcXX49c07cgYWdNMFJbEWoo_EzMdjrJHhsZNtk1s6tRBHU15cKOrPoK9--2L6QWnRyMl6eh6GIXdFNkWAKqJ2vYVLKKoF7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=K3RiFIJeqwMqpNoCPDqxJjTMV81ExCtP3A2KOz7jmApRFxloVsD5Pa81lKQo14ojFxA99AGAva8vQ1A8S1tAViWQ3iDW377VX6PHtRkkb_uvnySBgx2oQBi5O_8URMDGfCwk4BJbjQRawMo1icSbOvH8OdOWlKXefBf7C7e-yt1o9J9CZZxwLgvSd22mXzuxQr1PvRPbDW3BUcnJWZEi5_vkmaTo2dVESyG1lseaMa_XS_3M3sCOnKHcXX49c07cgYWdNMFJbEWoo_EzMdjrJHhsZNtk1s6tRBHU15cKOrPoK9--2L6QWnRyMl6eh6GIXdFNkWAKqJ2vYVLKKoF7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezIZJNx_7uI4ZdQquc5WD47zz6UXZoxi87Vh6STkp2Fa46Ti2uf6blbWQqY1USM569pMbAq558fO9ntjg1OR223DogzUqoFR8lNMxjeIvlq9sjgHsy_Z1O9G53ROEe9zrUwfcP8CZ2kFpTwinMcyuZeC8I3ReUyRVjZOZcYzw78xZ4YJ3JlQFVSrjRPxzpQPHtAt_DiOnLblOG9jhqZiw_0V7YWp2cEyYeJD17JJto1KfpD1DTMrnweIUdDHRHDNu9IS2T4mQ-B7agGKtA09x3ELrf7RnILOSgP5z_5rgfr98vOzL-Q3zgTijPOnEwhGqH8qIcoAiHAxm8NRJL2DDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=U_Nb2ufMTiy88T0P7FBFGYRt53vaVSu8J43eLn5SxRc_q2_73Ytl4RGKksZqnXKgraZrPQOJh-lXGE_ty6-JEtHia4B6jGyby8jR6yQq7GwVzw3Dp8c6azdetyZ6-ir6ZiiKwXwVBER9rIJWF_JNe_NbLGsX4ZkDSbAmFEOfF563nqge1JZFFKaqhY0Gr-FixFGYzpQOh5WSTO_z39CEnbZgacYVRTm3m3jmbTGtXGCWD36oqn5MDPYBdQPzasCG5T7oYfXSwr2MPulJyM4w-mH3H1HV_rQSjS8I6kMvd9PU6GJ0acqfyElO5zZX5UiNUCDo7lSM3mtZLC0YJVR0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=U_Nb2ufMTiy88T0P7FBFGYRt53vaVSu8J43eLn5SxRc_q2_73Ytl4RGKksZqnXKgraZrPQOJh-lXGE_ty6-JEtHia4B6jGyby8jR6yQq7GwVzw3Dp8c6azdetyZ6-ir6ZiiKwXwVBER9rIJWF_JNe_NbLGsX4ZkDSbAmFEOfF563nqge1JZFFKaqhY0Gr-FixFGYzpQOh5WSTO_z39CEnbZgacYVRTm3m3jmbTGtXGCWD36oqn5MDPYBdQPzasCG5T7oYfXSwr2MPulJyM4w-mH3H1HV_rQSjS8I6kMvd9PU6GJ0acqfyElO5zZX5UiNUCDo7lSM3mtZLC0YJVR0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyCiGr7fXJgk5UsZM0sSxrC_UhoQ7N3WFG91t5FCmCmQ-BKr2nzRz83d9ggxkI9kI06tmJORp77yKMLmga5Vs3dlbq5XvQjI0tIL5sLc-DQmY6Jese6c0mjA6a_BAcd_jh4vXmMuV3_cCrarSzBWbW5B4lPHJ59ylv42VEqFUt7USnCRlurmEcox1zTZk26pHzmZVz3Bx4MhWQzm-QX9AKg5ZMnwRiIEXDSSHvVNNGFyL06hUo7jdkKVL7XaYn2FTsWHG7KG5CcbkxZ0TVRGTZ4R2Re2v140DJV6L7e9WcQ86WSBO52Dm4YCZkVw8R_7KW2tjwl_gKSkcHhejyoQZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjJUpnBIYbkKd-Is1siGvq1L7kFShXbhsIkOXVVph0FW3Z-9_G91kygVhCvE7eHgIu9v7b45NgafE6hSQJAq3_Eouv-TtYZF6bcmAzFi69M9S9tiKFsQssZZlLz5p6srrBeasck5mAFFdxNvFnfoA-5lStn9BCtjCX8qVxdgPPoRJlIDDeRTFoPkkDcpzghgM_50isktcwuFKu2ZZqEOpHGVAjbJJeCI5Y3YpLBaEEA0FpovgWwlZQ-9bMTnvJsIa7hsNRhpBgKlb_WCft51gQ2Mh_QUJLAiXLlq4r25tBw-sBBbKuAFDSR7fgzYv_nOfc-G1gQeOoq9qAKlIOxJzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgN6O2avTjBd2VZOP6UNWoYerrG-_YWbzoSXhRHwQYMdFoeATzM14cZ8KU0yNiwLwKnGmZvpesGe27L65PgA_W7zJC2hh3uI8DsQU85GeU9JCM9_Bs3xIyDobYTy3RbC2JjuBWjRoJ-q-6Im-yM6-LWmURkaoHJWeTOOLPWbbVLlORdVOP9E3bG18R9xQDVboGIBlqZQ1qWhZjnOKcVYYugsrOa43IjRUwNY2fbmI42wjPKmPfRR222c3rkVvGTC5nT-8IBhqE44Z_b9DqXKsk4pRLgfLJcG60WjN-XfJxWNSbFbMqoQLGmdzESNj88pua7-YQCzWL7iR-dFsYPVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbvM5rCErejcCMYedqQsox-V1mySs0p1rHiWcl3WH46iul8T5fopd2bCg9pHXFAJyZ8viT6oGIgT1xDx0ZhXvqSN8Hgi7YCA9m2INOu2RcY88b4DtXvHa9tf030rpmYMvSqTXE8JznSZCUKVLBbd2NWfszzSE4mJU0d0-NPPLoQCsrmWvHQ0gqNN9KrnnPfoaki1yVntCkULnDnERADdUCFpMDREpak8uOtMjUYHARERjIXcc4MJvoCPJcJvElCOaQEH0N9YtWQCIaOKOZacYA4H6tkHLY0aovilmnXLnlhKfF4jLVRw6dnUX34k4Z7sk3txk9VeMCyWF75uh2QCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OY_alHpQHJT3nbny2MgFUMUsQw0W0xVr51wUxj_iVUC2GQcO37ilQ3wYt8D7S28FP0CB7p9gcISsl7kOUPQcuzWl5NCvMu5hjwAfWQIL4tV6xNo1YaHvwqgfF0jzcg8bwrXp7SgjQkxSB_OjGC3DdZ-fZUZ7F4vOapoo5f8ep40SDokl8CCdyncmp02nvPbbTVbdcuVNS-T6yRz6Ew_VzMqykm3zV5f3TEHg1spoMISVaREZDnTrcN-4kRPVlbxl7s4rBuKpM2QV5U6Bn8r_wu1TKbmxNjgH7QmQ6ZRVusw8UvkMLgwNSI6V719QPe0rKbvU0eIiI4uaSIEFy6Oqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Chhe7HoPAVLbNTnEl9vh7luEa-ro_LvzWxYv56ZkxipFVfwwLf5RP1QruG76M3rQ2b1X5Yiyuo99mvTzo-0tuM9Vo_fNzomBPpLwgpBG8upWW-mI4-AJ_fBtY4_r-NSLelONPtgpFA8S71qkgwCRo8OSO7tQr12p_RMZbN--yEKEasZYFhkvPLN-uHBSxI4wGykznE6sDywsYcB2TUoIBbrL23k9-1Gj9uy00udqzpT00Bjis6vH-UYxzYIZ-R-IW_VoF78gSP8rwuE3RSUWoB8X6BFIZRwGV2AL4dlkUbtqoaF5kQB_Pe9kQC624Ih-bYxCJVFWfczvPBAWflvJTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1vp0J6aEoLFwTnpbWbKm4BYZzCwHJlsTpzQ6VGnnBnl1lvVbV0zqe3Y1uVrQMDdvfmfCkX8Ydiu5chhcTk-3nTpnL5DHkOgUdJ9gZyySgBska7Cl6Eqr3hcB58T38Fw5v7qPP89om6IeZa4hOaBzpt_u50GsyecME3WErZbFCYKTPxGX7kxRde3V0OGGkSG6WvOZDaAZClFxqMxYJedxADNPBcU6TsIcP1Nv07BmNmrmSXGIyfOSPk2uQIrO-qWe2hOmR9KbrsK2-la3AqGtSDZ98mFNh8h8CX5S0AorD3fp6QgwLuOAlugrcZoS46zZKzCxpWkgAcCCcRcuVnxsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
