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
<img src="https://cdn4.telesco.pe/file/TRKzmWwH2Iys8N1LVOLYb_qkl1XOVNkN5BnCRsourlFuCOFVyHiUJEy0b8U5YI-u-KBJhKQBouch5XwndF4baw4xAR24KHLnooJF-1QBLSFu-MQgBvODSagR58FehTXqdDh_7nor1ofsvlQAPfe8zz9mYygiGQ0WLtqdO2ndVhiDDvs-0_el-lH9gnEEnKQhyS6ZZoB4XusEcLSjL7IwocmC1Vzwpo3o8zcfIfTHkoStdBkpaPGpOzLhjhGBMP5kQWLvLWeWn5KJ9h96knuR6FuEnpb5b8HkKLlcLOygSVshoixpaFGoGU2OwvveIxNl1h0yl4-bsU92XM1tyezNgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 20:52:02</div>
<hr>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFkSwyBfA9P6QC0Iar7HHSAmc0SqJUx_h2Nz8INA32pnGTNXNs7ePeX5uKANtvOXgi5MMpkD1rzIAYK0ToOfAmJJDsUTNJjh6hBpS1zmkuqD61RtswqtSwh2T0cyXjTN4mYVj5hFr4Z15nXk-KtfFMIGiO8Gt_8tF3GWhjhWc242r7IJS2SByP_FhKIP3J8_CBEKyzT2d0AoI8z0FSpEXZZPpzNLHITat-PkIZeey8ag3s8PYANOCyJiQz-3x9h2J5ayFi4ZEBqzp_tOh57nB0clLVbUuiyvQmjc1gNTwuqzXOjG7XX_NZHMw5sfoTYjQvCnb4JgJdViUKRYWqB-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwuasiaRwnO4_HGyViIWr25uC3kxzTM0DqLBmXYtK4tv7bAdg77x719kASjpXFxASOqJ_YP1ko9Zt2gQKgq-fdv4pw6y2gS8J1ppoN1wOulxmN-EEulDVbIRcAVtNQ_U4rEuYgbNUpcLMNVWX3XCbnWZpKg8dzRSyzhhpe_EDOskag0IQ5gArew_SWD3GVhboVGxr7pfkPilZDqiD-2tU8DQUS1SLd7zqQqXM8KPs7Fe6AAWJFpiibP0TNe2ysepu03MdmQOfYqgogcSGteIMaqFLBzErdx_sYWOuOSV_Y6oACjeH6Rd5_F_IU2P0Q65h-LyU6nKooZcD-xoDBbHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7451">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7451" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXupO84-FV7u2kQ4CEd0ljjPjD_D2_fowm7gWEmpk6RkkdfksRB1vhaLxbqO1kwymTccEJoKfkVr4P_9Z-bA7FEvAqalLiuG-FYZ8QP0ptiZNEqZVQlL3pZlXcO-6kI-lqZsyniuHnZVfO74xiybczV-Hp8e1jaXCu09Gv2bJeFaNoIV543LTuiFXHJy7gdfzGX_0gaOKiQ3K6KdjBeHj4IQPBJY03fShCOWvGAckpDc0SmYA4xVsigGZCmopQYbZpuRSyAPtsj5N49JiPLsHPM4_GdJcwxdLHSb-4wYYYdia-TVAFHTqim8A_3EeE91wVXQpgHojv30tQvQXHle5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syzNYuq6zdnzv9S5NZHVgZO6nWpQnMuHrbfqVdmCicqRkwvnDbQ0dm1HXsYug2qBtHnPtpTH2Mc9cAkmxjBoe2kXssAFf44-8ieBEVhfBQkJhgDCya-RPd-qA5lXcp6uHz3f38QtW0GM9Eehg4gMbtaWDR04GHxTfaeh00pWd9rwTGAdEGdRjOy07AXspHLjx2QCaACpfoJjdUZN-o5ZktesffRkBe4PPbU29d32AGJP8eQ5G46P5-L2BB3tVeKFaj_hZ9mSsGYBshuuG9djLt4kOa4onRFP2BbBR-f02zYi91c1fidOkvVCojVy4w6JGXOOPLOQSvYeKWC7rLR7eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwxBsdaab3m77CP-ydCK1DlxNuiX-f9RWy2rzSxVTJZaO0Rr0b_HBdQbOchpI3jsvDQ2wbjgJ_ezcJrSz36HCwJUPWMyjoK3evCKFcLxIDgESvssvMg0hgO8X9mnKhyHgdOP_iVwIeQU5CRCJEmddbnWo_K9-Ov_NKvCAcIX7YSsxS6C_A4zRcqpvRCWHxC9g3h4OfrXEzc-at1kWcCGmRFQLDWHTF9RnRcyBoRHAQ31ktB-HbZdUhqrreEaNJXVAvd50eqdsV0Y04Kx8Io0Od2EU4aLJFB1Gzb8GFOi9nZhu7m2CNJwvTnaMfD1_AxeGJD30IkifVscbHFsX2MLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-KHcou5hm6e_HbtaHRd3N5Eo3z-3RGaecRS-_tD2vr2M7g3op0YzogcHE8ucBhjz4y6sKls1DBros6IeACvPgqoOx4JzH8CFuHTm0ljYOkGbCInfP8iS-CgUJKfPe5L0LcMoTrRJIiqHjpwTbplRGat00abr313bfyVsFXQWQ76m59mBvwO0s8GIYRLgSMWAqSGgNbUoyonD3Y7Nco9Hib5YLGb7jlhcrvGmr6zlFbu1c1n4Rn6c2DE1OvWLPT0lvEvtY7VEiuMqCddfPJmndrxvpkMYOPJBt91wzOxhN7HVtM8PWeHiVc7vpqJ9MDkJl-ubczDIlDp2Kn3wNj-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=avS5KxybmTbZgv-YG-Hgtu2JBuf_Dft1zqjNVcb9m5GCOtQXZFCZFXUN4ZwmYcrVaCz9IM2I3DBmwhfnHDR3kX02IAC8xCvTIz708ubHrHasadRNS59cDmIuNYdinOzi4xRCUVqfMAq8rHG2TcIt-TH6sBxxpX0KBO3fkpIZGC9dlSKNfg-tn0V40frfWJubZXf5iSwWTYTYh9SQcCK_2tUM0tlhwBJP5-1DF8q9bliutSoVMZGxlFBpY_xURAfndTEQ12al9x_AmV9CDCFqM8Kua0V-Npn6RIEbTSn5UAy4oOSydCSJbYJDV5sxIkcTgEGacyGGRZNoWVAIm_ZZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=avS5KxybmTbZgv-YG-Hgtu2JBuf_Dft1zqjNVcb9m5GCOtQXZFCZFXUN4ZwmYcrVaCz9IM2I3DBmwhfnHDR3kX02IAC8xCvTIz708ubHrHasadRNS59cDmIuNYdinOzi4xRCUVqfMAq8rHG2TcIt-TH6sBxxpX0KBO3fkpIZGC9dlSKNfg-tn0V40frfWJubZXf5iSwWTYTYh9SQcCK_2tUM0tlhwBJP5-1DF8q9bliutSoVMZGxlFBpY_xURAfndTEQ12al9x_AmV9CDCFqM8Kua0V-Npn6RIEbTSn5UAy4oOSydCSJbYJDV5sxIkcTgEGacyGGRZNoWVAIm_ZZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezcxHDfUpV7kJI6Sb6dWSOJR1UrHaabVsIk5446gJN4itK3n7VFxFARtGrhIUWp1yLbhZBZWCjuOv-hSa1iirItt5oeSr-49Pq0BisM-OZL3nDZogZYDZ5zA61mq-dskI8ptFKzQZPp6q_B_PxE2tRH42jnefF_TYL1oFBufSpap4mXvkgAzR7j0NKB5OJiE-T_7KK6gfZj0MLGu7l3YUoZ1FPfwWj_O6pz6Up0Zlk6TRz9TAQ8JJ8R4Voot29bte6q9U01RbJrh0ao6lQyyinc4Po0Ogh2utJUydpAit84u3PE0jVBreKkxXnO49HTnaUQ8IxKEiLdUMuSic01c-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=aFh8j7LfhlDxjGY22W7p_O-MmX_MluVVqd8wAk64Fy3Mh3E5yNYV3AdPK7cHBSNOj0dx387291MI5fmW6dUbTiDC-Uuqr-OG_0NG5D5mcS_P9Pniy69SpZdFUrJ9vptNyVqU51hUe9Z2eOpkBegj1l2bbFPYPT3NSXdMv16dhjHVmkRz1OEpp2OgDlNaL80GEbBTFUKGsnXd8KKRjqmoYnhntXgfn_XIOX1wvzBgsB7hwHJ3wXY5Wuq9lOoqlT-shwLrXv-0KFiI37FJoBsPEiGiLZBXJ0ifdQsgyRplrTqjCu1xvlRMXCTe_r_LMH6If7w2wF4mBa38v9ra85t2Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=aFh8j7LfhlDxjGY22W7p_O-MmX_MluVVqd8wAk64Fy3Mh3E5yNYV3AdPK7cHBSNOj0dx387291MI5fmW6dUbTiDC-Uuqr-OG_0NG5D5mcS_P9Pniy69SpZdFUrJ9vptNyVqU51hUe9Z2eOpkBegj1l2bbFPYPT3NSXdMv16dhjHVmkRz1OEpp2OgDlNaL80GEbBTFUKGsnXd8KKRjqmoYnhntXgfn_XIOX1wvzBgsB7hwHJ3wXY5Wuq9lOoqlT-shwLrXv-0KFiI37FJoBsPEiGiLZBXJ0ifdQsgyRplrTqjCu1xvlRMXCTe_r_LMH6If7w2wF4mBa38v9ra85t2Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFUuJ-M15hg50t2U2pCofeNxqvwstlg2sD2h0a9QM7zpRvTvEd-XNUaViiXeQOkb2es1vZvzFcziTG9mTs-LYJnPlbszYdupFuIhEN8uE6VWm6bX-GMJkin8EKAOdi8BiGOgmuMrlYaDv4DM465n92yPCVz6k-q322OltI67I01tph7KfRVW4-gApJ6gbeNrazhRQydiMQVZ38qU0PKaZ4V_eIu3tVY6e7rVzYfabktbnLii6bmLnIGr8S-hZqflF8e6kHa6TkLBBRv9KbW6SJBFET0Vpv5uPXBtaHdRewzwBfHNLLaYQ9c104cUIMrYuS-IjVBjmZPbGXr4jI8FsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIc6q7o5fYQy4lTUjZUAf23wGh_02WKp6OEPAoDjYyAHpFnR5ggYwavXTKn5jOG5FBN7pANcantTjBPaEmnf35wti7hWi7RLUT2tDHqDARgj__GPOEaLCveEH1sca7B8rf6fA1X33QWMpjUrAw534c3iLFMiFUFV0YjilH2FKjjAzfD_nD7_-8DRYWchX8N709Dk_vvU1iD-FZZ3PjlMDTvGyHEhctsdmt5z_-i_hrYHk8-wRca8inOfZawDgJ5JuVCPKr6Q3D7RA40ja1GuoxgGhB4taVNJIdjdnTMKum3VRDoEW3ueIibvmBgeGyuu1sfy_Y8jOaXMRWLjTT6NLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTfp76GYBrtEQxwO3NZiFTnpsAuuNbHTFdKJZ769RKq1aE-0KYFa8UVwlxCEApQ2_UQ__6JeTrUm7cMnQC-EFRNzqi88x50A1CE1dkOr80bJD3FrzlS_eYRdXUfzqG2ARWRLDifDpUc2A8Cx-GmjkQOT-tTRWbyXF5DhH11DV7EQZi_ND7Zpr6Ql-H4Fy23KEIYVSzKyLymZWs88J4YLEnh8xYUnLT5CzKueBbqzOxM6Mm5CbjRBhfbky-gZuN8pVmqblLR9EbwazAhO44FspA2XWNNq72edQc4dDR9NskcptbeTpA06VkLIPPRAds_RDplALBd-A-8sP8DHOfRrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=oi6hxY8zwKuWYWfyAOxjHjXOdKZX58LU7eCEf9nxODvNux6RsLp4LF05Uqg_eWvJA4UBbwvILGfm5RAsLsMXCS4KXkS8P_lsJ8KEIgRC0MDI9Zpw1KOStRtEBiNjjIo2Ib6yAQ5VznYvKcj2hYf13B978_f1AMnDACXbpGSjtDBKCgJ7eQkdfYs7R76TxARNnLk-HL2cxnEaWy7o2ZeZPOSyeumdMYiR0lcY-_Xf6Un6GRw9aR39vR8UwEd07tgGAJD8L5rKBn7vrwrR7yyOABCe_HV1Uec05x4qo0Cs8ZB75lM4mi9D6gpMQIGQrFQodP9Kz3Fh5UNYkFOeDJCL-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=oi6hxY8zwKuWYWfyAOxjHjXOdKZX58LU7eCEf9nxODvNux6RsLp4LF05Uqg_eWvJA4UBbwvILGfm5RAsLsMXCS4KXkS8P_lsJ8KEIgRC0MDI9Zpw1KOStRtEBiNjjIo2Ib6yAQ5VznYvKcj2hYf13B978_f1AMnDACXbpGSjtDBKCgJ7eQkdfYs7R76TxARNnLk-HL2cxnEaWy7o2ZeZPOSyeumdMYiR0lcY-_Xf6Un6GRw9aR39vR8UwEd07tgGAJD8L5rKBn7vrwrR7yyOABCe_HV1Uec05x4qo0Cs8ZB75lM4mi9D6gpMQIGQrFQodP9Kz3Fh5UNYkFOeDJCL-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8-JPbNGZOd43vtUb7Q1gaJxczG5Lb27278GWCvsh4zF4mvC6OwbuA4TAlC4466GNXQKdGGt6f8moGw97APIawA1uZH_ktjlQK7zt36_YBwUfcT2IfKCBrhdBflIbFYegdj2i6awZW7U-9SJK2acoZiCcn1OF6aKJQCTDSN9GSw6vVKD7cTz2u248rCs_JVGdQFCJgxCerrkuEzerZ1KMuHM4-imlZzwfn2d-a2oM3gJyxn4Ih_2G0ZNAKPI4aaRCpFrysbytrLFzwzJuk40FqzvR_bgo3ng0dm3RwVxKWZz0wcK3XAkTQtqAmtRNylyETp2RT5IwHh1IXxUCVzusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔗
📥
دانلودیار؛ ربات تلگرامی دانلود از اینستاگرام و یوتیوب
فقط لینک پست، ریلز، Shorts یا ویدیوی یوتیوب رو بفرست و دانلودش کن
✅
🔹
دانلود پست و ریلز اینستاگرام
🔹
دانلود پست‌های چنداسلایدی
🔹
دانلود ویدیو و Shorts یوتیوب
🔹
انتخاب کیفیت دانلود
🔹
ساده، سریع و بدون دردسر
همین الان امتحانش کن
👇
@DownloadYaarBot</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_M_gmC2Kas2LUHh335DySuF2pYtjzENq5xSbFaUQzCYJ17wwY51j674rEsylSJ6PY4e8L7EbtpdklucGxhJVu1Z2l_LgNvjy_7Tf6e4lPIJrRkoFNossLr_a5pANc7tpJ-D1jIWfj-Xlqk-PaCWOiE1i1AxU0_wgoknIa44UHYSr5wnX_23_3MzS0qdK6F5liKK4eBLwtFDKFpNfr9FNx9uIdYxmlRYYDJtI38IOgrywMSqUGOX6jcjkcTg-39UuOmnceMnJlicQ3lITV-CQrsdqcTgTMrPg_LMtfApkqGf1FCoY0sXIYu4cSz2I1evSCyLIKPvlpMURRtHfP94jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAF3by1wXaU2bHyTWajEViHTtzRju_pjwwTUJbTH3_kGucnD4cfBLbZiuPK7ULLk9WmOfb7z-dB1WnOwb8q-0Xk9id3fLwGtcx-WeXAoQSuc-FLlFM_qxoIMLMeAok3qRpwRPngEdbDebes9hqAPDg7kPGkO3f33l0FF_LVX4vfKk4npgxZb8AeMkVtBEkHdTbcFvmDdotda5ElXztiq_9HCN14c0Su_2JrJxy18Io0Gl0tyfVJKLVcfDWeoQCucNzLVcVWmotrGb6XPGGBv1ecg2Uml7nMqyMDiTrL3dYG5jqYakMHeCgqDXlmbQQX5NRLGqIlMG_XzORrErsutTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUwLPcuyXrH60pnQsR43VgOzwpiLfq5nAQn9S-95KaLnbBpxer05eGDQWtp40RlWiBibRzHZ3KVBjjP7NnJM7O7GLaijsiDgDx_WDRtzJjIHDXQ3Uxg-zGqmnbPTIb1ZPO-Ga7i2_eOhfvnqiFpli6yHaM4qyQ77oZ90Uj2Okn2tvMfIcqAXO28CO6jMEpRTTaeZV8zTDM1n6cM9HJgxVz54A4_2H5igGAfNaOmSA0P1V3sr5QgY69I-QxUkZgateXVFF9yQU9u1FYHgg9nl-60JsVXxr6Es3TdcFr6A-I-d7KVFNK1y02CG9nR4mZySvYgNKpe0U98ZlJxrTGHidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuQFi5r4e3x1r2GWXXaUW7JyLOEG3EGWEas7VSfrzzv86DKCXhciV74sko9pvdtgq-fFxXkesoD3f2NFcglJg8FsLcR5Syr46a4DaDtc22qbdeSks7NnbNNyhl_KGzrzyNKgnFWpDTNbM9-TAJ1sNAXehzFKmV55Qcysaks0VoTixUac6WdAzByfdoaIQ_NnEMpVC9oO1oKDSVZkKFGA8rlqSlrDa9nFdt2G8IF3iO9-CnrH0TZy1Fo2uw2Yb1PeZtTe-p9TAgbpPoSUjG2RY3eYyZhj5kWHnLoXHDR07MGFYUmOgIJsh7Z7VEmJ8PVveU1pyxqA4DiiXIuWab49Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S34Z3jH89AG48PVlr2gCwRW1u3SKkR_rzO99N0AXZ2ARO9lbXq3XIJH-lfHPlPb1ZnJ97yimRo0BsmRbBWmoHwKKvIug4YruossidvHiNirk6mkywBGT9GMSHAesI0lcz05yNMfa54XV2YuFvzyw6N2_UAa5DYLWfD5RVmwTP_vShHC3DIZRDgpF6y9XiJr5Lx3H5Y764jdD4LEFZ_bxMrMTIlEsXhNaB9UQqK_gamg_mMYmeM-9SV9IUHyDUw109kOoqWZGjaPMeQ5Go9IE0ad3VFVYSPXvxa37iSf1YNSWGHOwgor2wKqjkGdlI4JzCATm2O3Jnt-qf3lTLjRKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwgiCvYXkDgUZ0ka5tDXmAeoKrz-YszTa8MQ76UYbw0h4GGURM0_dEOMJWoKKnltmMd3fA1VsF2-EJiRIV_lnmnrcb93AWxCUfG9WMs4tjzpX0zx9rATLKv4xL56meawKre9uooTUoN4XZxAGNqNFWGUOlEYbguKCZpbNdluXHRVF02ef1KwYb1QfCulQkFIdm60PX796Jd8xdn4Jrj45q-yjMNBLLxJQ-d4huAotn3AH4crcMZSk0Z3h3qHet2CsaKW0BRqo_LVGM8UUWzue7fUfiM2zv-oMhlftPWt5budN0sPdpAusb7D4DV7Gq6vUwZp-fVSe3sRNy9RoyffzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru7td83M0XyBvQR2PTAZ5EKnYg496VGmRYBE9xCxHO0ghG4amDpSk3mIMIyxHhp6XMObltru1caH3h1l1kAQ0595I9bUZkdei-kvc3hBaNUKADSC4oqB1kPfPnSqMz3Ju8uRUeFVW1cfgFNuLKF-DZjMw5MzM2VZEfsekJmCNL3uaVBxPxEKWBsLJD5Hrah_DNFRlZpoRlpSzVzVIB_hKTJydYjNMJGYRSOQlaGdy0cBriUu6oRTvSM-7sCgbCAhbCw4NzOtVp95FWvPbshDQst6MiCOXIJyzYdZO5qZTlSsJ-VtQX-YPEB8ZRgkI-ThfCW8TWdDKK0xZe-JQoRZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZd1nvHVrxj4Z-e51DRtV_DM4RMcSA2_j1J6sZEMwqRe6X-Q_9bLUJVm6-KZrZy5UuBl6Th-gF78eRf5HJvOhxHe8WTfNqv5USjav4-boYSEEumVKxxS1flTgxvl6AwQTBZ2sWmey1NlyxtaOPUEOZxu052kS4D4v43bhAxWCfpRRZsDJQprBSFNnZNhtQcyNVvKV7yVj-Icf6IerY1aGZiu_KNV-Q0cWRxuO86oxPwskPF3E1kkGSscYD1bozRny7QqvsfuNrcKf41KvkMpemBiC28XbFHUxpe9Rqh0VVTNt-GuvMSxREGcJkMaOaLeamfcQ-49RLwsH6a9fYRnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rORcB3bdI3wQi-fUO8DGz8ed3sSwG4Dy1y3kXrDi8nCkRqzDPVJgQfwFxn6RVcxs0Tl_SO96aVOOwunuGgwONrTLhY_yBDB1y6pSLoeIJXSDkf3GrYt7QVSR7Eq7x4G4eK6s15uKao8ELCZTUfemzHkqNb9RXlC5o7Chl85OaWctzhD8p4rLqDbBq6GrBqxdDG6k0yOfeM3gonztBwLKaR4XW9zgNvqNQRtNlCjbP56oDAbdkfA-c4ZiCnoQdjoMK3rBOEMecggJBoRhcIXVfnaoe6ZmygzjbaYsyHhe0uTzzRU8JcR6QDMrzybfAkrhXcx4i-W1_-PtAl53r1LlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4rb2cnub7INOTRnOi4tXSNnTaQzHcfpT4De16YBS-5bJBuYsAxLW8carSSliZwAK8HHar_dZLcXRSDZnC9N9DJe46c9Xlgcx9LS2m3CkufMdOMKmNYkSKo13tjxdeOMYie86M7PJP-tI3pXJQndVmGlFSduVOZibyeexhk0VAZg3ZEBAfY3RzEfWrpd1wHLPvZHKSTckvqxmdQq1BysbRjIwtWkJ-YFfEL5pzbeUvfTDITBXQ-4PNz_YKmW6baJrXp1kVEhV6pNv1LZudHEU1f61wtPuBHb2ZoMl2DMd1iYzuT6-0cJPUeCykgOyzvha4vdAWbPZksuWYsJ67nELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWsRO97-FUGGApt8z99rw8yq5YPKsYnHpQSurZFs5X1f6yp1Bol6uuXM4LTUk-kVYROfQ_5M9SNnlz6hXCU13dQ3BG47R61wY1RPbBl8Ii1EGjz9y_wB1RW1zg0bih_5xTOuIKCpJQzPwCxXcakAfASiKb_o8XDdu2BDyr_FtKNBPiCzwiytpDOuz9RzUOyhbqsuHYJgAsqzsuRDYu7_T6bRwplf1qbiC_8YNbSfJWX-B87N1WBGjBMlcfgvYA_s6Jr-be32WMW9KNow4tpjHF8u1-8sSaHhpe6kZ7QDvV5FfNMI_JywJ1kuDmCdXAiFuaWYHYwUwgxXCFRiWe2IZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U01SYc4BDjGy1BhmG0P-Ud1sHgjru9AC5QsQuYe5nIZDmbuQuwfh01XJtslRAuXg3pX_G2b-59OXrpiRI1kikz91Qvtlx3FFzi0wviUBEDvwpwuieCcABfSUKlKfEAGCSRpLgxvDkQi2UhTORGK6tbajmcHyJ0h6d4Q8bQMb9gvDK9XFg9b3EQpUbnQmk8Y3sLrliTPIHDOIWfXJhHAL2H_S3n_cw6ej1u1izcc7MIA18Wl9hPPnQf-7EcHD2BMm2-U9IP3-KuIm9OiGxp3C6Z716bnslea-vEB4Vmhjvb6i-MSXJUJcq6jIXutsxn7tEhqP1CDS8BpX_rekafmeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So9Wiims3wxPddF1Zmh2uN8YYPFLcuZf83n8s89tMEgSvZAQd7LyR7AIQndrqYIuLMy59L70wRI3Labr9iAVBzwdSExKIDNOQ-CxmE-fjqNTp75cZ42Imgq6Uqrt_XkJ6mEj3VEznkQUJ48aZnWaYxHH78iCQrD-wG8Ok4ds53DMAvSBal3XYQ3sYgkQ0t4kcnofF8SRjSK61k_gWR19r3-wX75Sh81lbPAYUMksa03mEiCBRg8YPOLHKXy-MCnrTznLq0yDWrPX32ZEEmKx5AITi4KiLN-DWZF7ZvQPf5v3JDBOA4g5FTl8B8-ZZf0MbTQSP1W83Bv81s_T3mbm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=TaiEBNqwxgiB_V6AGfDjf9WQBa71W0Rv2yV3Jp9n09tuLGj5xo0t31Y522BUoZhfn1_hI5VgOCWXL925c8VNzd8xES__vphDe3_zxtmHz2D0AJ3GxyEdsCxHfRoccvTF-lzp3-zvRVkesux5N0Sr5IqUWkrZQR4QSTDrC_T9-SfcEhDnrU64AqlaDkaQVyv5zdFKCm9-N8TvVFBVtzvSHQS1Q7moYGrGJMlg9V1U-h5Xvm-klRTXk5NwLtrV1sypaRQfa6hTOkK2oyhIk1oYywFLrStP5nePM4kYql5J7-NcEsENvyYSlVkRQnS1amUNCdxUylSz01BMSWUd7dN7VSSA2ZhRj12RdIb6zadI6TW5rj9RjQNKhGWdWR5dt4cupbjnI0sgI3CAXebyDqepp48_I2qpQWl5IQdR2C8MVJ8jJIQoOa-frGQwcu3eBd4DsO3vlDWQJXvWE3tfg2xjZwjFOKkm28XkIf9dpqV3yHAg1k-yJxM35FMEQ6uRNLtSSBoFbSJtJ6RxONXfmrB6EVn7BFilXhjTojwIgRr14_Lbs-n5-cQF5184rgyhu8xl4g9kaI2a-eElwlz6TYh1O5KOtm4AM4Sm6LJGQSAcxsxKTuBrdIHFUtR9rLYyAUOYcTFGoaeNVDeEHDbT85AAEd2-DzdUh3CMHbLqTXSv3gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=TaiEBNqwxgiB_V6AGfDjf9WQBa71W0Rv2yV3Jp9n09tuLGj5xo0t31Y522BUoZhfn1_hI5VgOCWXL925c8VNzd8xES__vphDe3_zxtmHz2D0AJ3GxyEdsCxHfRoccvTF-lzp3-zvRVkesux5N0Sr5IqUWkrZQR4QSTDrC_T9-SfcEhDnrU64AqlaDkaQVyv5zdFKCm9-N8TvVFBVtzvSHQS1Q7moYGrGJMlg9V1U-h5Xvm-klRTXk5NwLtrV1sypaRQfa6hTOkK2oyhIk1oYywFLrStP5nePM4kYql5J7-NcEsENvyYSlVkRQnS1amUNCdxUylSz01BMSWUd7dN7VSSA2ZhRj12RdIb6zadI6TW5rj9RjQNKhGWdWR5dt4cupbjnI0sgI3CAXebyDqepp48_I2qpQWl5IQdR2C8MVJ8jJIQoOa-frGQwcu3eBd4DsO3vlDWQJXvWE3tfg2xjZwjFOKkm28XkIf9dpqV3yHAg1k-yJxM35FMEQ6uRNLtSSBoFbSJtJ6RxONXfmrB6EVn7BFilXhjTojwIgRr14_Lbs-n5-cQF5184rgyhu8xl4g9kaI2a-eElwlz6TYh1O5KOtm4AM4Sm6LJGQSAcxsxKTuBrdIHFUtR9rLYyAUOYcTFGoaeNVDeEHDbT85AAEd2-DzdUh3CMHbLqTXSv3gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud7AEzRgsRC9Eis-adarIMJhxh1MmXxoHKt5HQaxAG31xUdbaRJwm2thSL3Fx_4oYxuVwZWntJTtrFz_5vR0zz6nOMe2FgR-_cvV0FRn-RODChBfxxN0xkuyYBDZv7RSyPKUv2YdgA9f3-UvqQdA2PAlSriInAh-qRJq8xSB7LixoM3G1sq7Yt_Vo740LSgPidllKFI24-o6KATEuNPUG3362HMl2gyzys1xST2la6YtP6t0ME-lrxzxZeUkdoMB80E0UUG44N824K5Dls-7BnfkBfGPAGvVs-4fHxNysxu6RUkyRFDTHhZRfdiQGuuxJwJJRxktSO6FJUmdADB4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKrdyeHo8Nophry9bLzyfkv6hwpWM88wf4W08fieiD87_fBMpmwFbcqj-H4uTmsbUKasb3M0fP5TzE0fnzLoCzyusDpbapyLantuSVYxCErb_LDtlRUDxD0d4aobttoja4f3rjr1H1Hej70EmXSkj0nzX5Qhy5pFR18JsfDfnAxxDyAzzjAnry2AaI4Fvv1DO9w__F8VHAwr6MxuWCY-wY46L48ZhGRq4i2aDQoo1jMCwzRm2-whwQkyGuCXlUGk2plmnwdO5cUmbXaNgCQGP9cDskB-hs4TS6VAo5yUZyThD2yI10Q8N8kJOKhPb1a1FLc8BpxSO6ATZgISVG9RUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsCdKAkoay6qKq3uUMiWyLxQ8Zx1-gZZ0KRq4-GwhyYLBoVAgHU3RxYg4ijpmxvd07rmbBEH3AKxIcJd-6BCWBsh3_8dPG0DXFKb-HHKKsQvpvqrgxWTBF8sch8VdIXcsW_ywHkdip5cxueVy_4NedZjM5ynHI0AJsmHzP22QYBBu62I2aZMLuJtprt1hWLTiF7QdpxsaQEz-q8Xc6dB1L-ndHMKVOQUlRHZC4kaBl6uCOD3V_LryyCNtjR3qeixHpdkQPprf9t0Z6XNDA_6ASLAFvBzDNzB3IHlPbS8vqAo4WLJKUET_sHoNxMMbv42uoRt_m8pZDQzGpxJE-tSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBAGRKRXg4Uyv2ArRMqyYqCUnR7jhZCA3XBlRQ1mcROsINuNVlnCP_JXguGULjaeM149yeoGqyGmc9sVcU1Ft7ahm6nIbOgy1IVjkSI1qjI4MMtkD51DQxy20BViBXhqwmfcHytlfj66q5OHvthQBwR7pxIKtL6UOq8P5dwwt7L4Hk3hSRbQsQK-fGkX0AFh088z6NCA_HrPxL70RpTZkRYQAt1rf9_24CTr-N-6oFpxTpbjhs93olYEWDAmEqCKeXTXuilQ41F6MH3xyn4-B_Er52zD2HEzPmD59HXKDRaOcDPBdT9WET0hXS3eGjUJ9NXkFQSlKdsqhAiag-5J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXQzPhGzAfmL_VwLFsAUWSf31DQfdMj7NrbK7OyBWCO-024vTv-ZCQK4rIjG_sFujyyficC1FaKyxjr6dhWyhvoz2F9flaQ5UdV-TLJtJxEAFGmg6pwSNyARTjkIZ9RT0ItCH0ftsbn7biI1cpiQvY72qJKojVSNe76qP7S3IRH2S0_ATFg0CxL1bgF6WXd0PnJUFttYTkK8FLNvpudFDQYBgWGm54hCmMoCTxm5efa1W1-aBSOcEqULna7ABSkwFWCKnS59OKGa0-AHSefVYJZMV80yrb-s5Qq6xrhsL4flwytjNIn6QkWTG2y9amVDjS1fy1d7120BuHSQo3owaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlxRFaWyLRtfN5ZaT2vrxDMHJBZqSNh7A25sgSWCNOeE8611i04ze6Uk1cYd4j8bJbeW2mYwvIMMgo7ibcMmzzj6babfz0Uk-KGHB9tA5pxxPYkQt893FowZQvmQRmMssO76WdRbtxvRxJlmet_RypkYIqwYL_K5UXAaN32636QfteqU-YEy4hYW_LkSqMGAXzUIilvmhwXcUXl8T3s-tRM2B3NYOputpz4F_FfgGDK50qgO_vZB92eTHBV9TLaiOM5_3scrtB12FhzDY4Hr9CrbKgqPGiK1yw__173tl6Y4FJWNlGKgbnFIXw7vBcsqqjNJHo5BAeGP-owzyzEHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU2R2nFvXWfRho7-25uJ5ghgL-fSUlwyPlvZpwMrDbEtYoVio7gVftc_Ba78D_q9R1unww9ZRmKVGSOtuj7s3JEvewtQfreWYYN2xZjRKmLydVA4U2Sl3QmV7ryFcf7tqB0TSGZv_vpa5nLulJ4GE6xUg_-vKgN8TW3oMrlHxDwmA0ePgt9ZNWb9SwsYI76fTLNewI2OqZ0lLiaC8kpRvgfMGSB4sUxJ3a-BnQb0TyduhEMix7PlAltjBHQlHjbSlzo9VjWrk1bYCmN1nC8P-wclIgatfSs84gWTCJR4Wx7m3JbU5MqKNQrOl1N4qbjKQ_HhZhFp-18pIwE8h7sqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxCspp18imTI46V2a6TuH4yWCttXf9gUFXj4iq9DhdeQ1SSDivufcsPb1V3EMAMnHGwhHyOMYm7qUqbkgLVXQ06tOkZ99UODF1xMwIgu9g8bfnh9OXPh1Mz5QaW4YXH9j4GYGwM0ckCVtOVl6S19YZRAfKhdE-d9Hm-stFFo6FVXHDAevPSfFDOvHXoSu9UBdMXmIQ1B46ZewmxDaup7L7zJIj0qTuhQY_IWLnjwF2a2hYVJCr3ABplwKRniFh8mKivN06s16zYteFF3JsIb4CSJnST2TC096uJuaZLPuDGvP7ch9vpue_TgyqcGkV-Mw9SQr6OMdDTa75dKDkvi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjNxhOmItEKC32MKYJ8iUHPIUSY9IagmkkZeaCZK4Uwwxqdw8CWenOyfsZp4DButGHgsYa5r9zAyDLRUP0dINwGHgMmVG6MGFlgjtlq2TxS4PXf7tMFXcY51pVTja7q7-rWBZYnYqieV6IFqcpNAPVU5hzspQS-w_1le0-80XIAf9tw1x_HxFKOMfVXZCaIKC-9ardf_z0GEY0WzbiPU3eUM34I9Up7YCzXfZ0_zLDgfnkx-33W1LtiEAYCnTHLhjslsGHRwhXRcXp3gXKXSFFL0w7U9rMakYIcLXq23-iSS0aDi4wK5lZ0ykyW_QR8bE9Q80QK588srdb_-GbYwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYbj3UrC6Rdcal50GcO0gg3_Fvzi60ZItDIcLbnvb-muVfP003S_S-jROAwYAnanzZ8WvXlzNHUh01Gqi0p989beh1FFCOa7WGQUvy8sjN8-HucCK4Kxb9YxC6AXgDPsb4Ql0F_9xTRD13-qp263Vo38taL-CgZQL6kSoX2L9euHZuSaj9hDKJaZBa3wpRlYzvdY-jTU-bEFYZKoHMXE-z__H4D3_iMaGxvmKV0Q4MPXvmziQFl-OmVzWMlIySELNND2nPk0ZjAHIseGfsIpIVTpJnj8_dfTg4nW93OqaJFKf2eN6hngwJPEImJHUl_xX1_LcK8_oVdX8K4yOftrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=SAtJxmokKbuVdwvCBQroDwbns0zhhATgEwlvHEZYbPxW5bQsLPBmFeFbknHekIRDdOBSGcdtMoqv7xdkDPPyfG8qSb35yaRxmj3v3snyy7aWWM4c92eWqDgfCCFtDsVUG4Q0i4YaY6uXds43NDGDDzd-nI4gCh7z3dxOU1VwMca-53cnRRQyJu-2AdChg4uNIdDsLmwQf-QQxys5iy3OJpE2wIdiy5syuZKFzedt7EyO97dfZOOWt71N_EU9bYVmMEpxqKpryQMAlnw1hPNA1Boa1mjfWNcMXQgsCli8Or0nfrIdT2bRMj_jQwqXwBmUAKmTQTMc7_RJGaMQKDCywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=SAtJxmokKbuVdwvCBQroDwbns0zhhATgEwlvHEZYbPxW5bQsLPBmFeFbknHekIRDdOBSGcdtMoqv7xdkDPPyfG8qSb35yaRxmj3v3snyy7aWWM4c92eWqDgfCCFtDsVUG4Q0i4YaY6uXds43NDGDDzd-nI4gCh7z3dxOU1VwMca-53cnRRQyJu-2AdChg4uNIdDsLmwQf-QQxys5iy3OJpE2wIdiy5syuZKFzedt7EyO97dfZOOWt71N_EU9bYVmMEpxqKpryQMAlnw1hPNA1Boa1mjfWNcMXQgsCli8Or0nfrIdT2bRMj_jQwqXwBmUAKmTQTMc7_RJGaMQKDCywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=v4PD_ExTnTwVdenRHjd7ZBe5TVeyjT0g3dyEakd9DPpachukn_gSHyeddyAYAwSuuGaESuF2zwjkCobhVyFQ0jW1I91c4OSWsF9Qy9jBt8WNml3G_nQ4ozbHRHbpwyed_U8AIrAabYoO2sABxmNapigz0vPvHGJ1CdFfQ_XqjJL3LLWXWCVSfeRQLowa-dEzoFCJq5j4JpdSikRnoilAAiSVC8H-MLMrBAXEH3I3qhGrAx7OOPaeH73VYCBgiN2EoDLfgsliTdVXJA0Uq3Dhnfg8oTtzjllgKwcM8aMKMR3QmJyX22ebwbwGqZ2UrxLatb0SZBAb72VoB9UY5057Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=v4PD_ExTnTwVdenRHjd7ZBe5TVeyjT0g3dyEakd9DPpachukn_gSHyeddyAYAwSuuGaESuF2zwjkCobhVyFQ0jW1I91c4OSWsF9Qy9jBt8WNml3G_nQ4ozbHRHbpwyed_U8AIrAabYoO2sABxmNapigz0vPvHGJ1CdFfQ_XqjJL3LLWXWCVSfeRQLowa-dEzoFCJq5j4JpdSikRnoilAAiSVC8H-MLMrBAXEH3I3qhGrAx7OOPaeH73VYCBgiN2EoDLfgsliTdVXJA0Uq3Dhnfg8oTtzjllgKwcM8aMKMR3QmJyX22ebwbwGqZ2UrxLatb0SZBAb72VoB9UY5057Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVp9k2Q6Y3e219PeF6mPXHttmlcDDkg00BwreuawihA8jVjFrbh68NgL65M57C2X0xomRhNc4sdr6y-ZedtCcHNszQiy_LsscadJnMLzSpGXizVkWTRgI9epITO-OP70oC_WhYdXMuTaVUKf6roC_sWIKDcJLYzW3uTw6wH0__FQX42RTw6FmWVmc38v2CbKkiYmx64_NTONu_ZHwR4C1zbiSJcf8pa-t-pA7OhTW_8rvqINq_2OLA47Erpi2NZNojgQCGAApJ4r2FoXN8Kx0FrMWrSHWkcSKhNMMNysEkWS9AZk0OChFIvN9n0YMDyoapvLyRKdAb5HJA0DDfWyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2I7UJ5b8blXyuVm-w-7-ik5c9E_f7ZGdPfA2p6ftJr_9xghGT3Ty3CSngl6Uqv8w1i-jacJzWWgHKHE1PVqcRyYjtMyBSYw7XEmqdQDv08XSnnlgXRuGxMknDaPjChQMPxBHbGhVSSc2Rc1cTdD7GPuG3t8eU2E1yl_zUlsqetwdWi3Xkdp6KyHtSGAM88LuQunwdCik5v43uPxLmNggcCNz9v0N4IB_k0YXXzriuwh0ZFaHEW8Hkn3b5lniNDEs_hLbbwgP5_6uDpB4EqaVYFB7zTV1s18wR2w-oKEDvVoBzQfMWfeshL2sCABUccyDkPSZIGI2A-yoUzm5Xaj0IoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2I7UJ5b8blXyuVm-w-7-ik5c9E_f7ZGdPfA2p6ftJr_9xghGT3Ty3CSngl6Uqv8w1i-jacJzWWgHKHE1PVqcRyYjtMyBSYw7XEmqdQDv08XSnnlgXRuGxMknDaPjChQMPxBHbGhVSSc2Rc1cTdD7GPuG3t8eU2E1yl_zUlsqetwdWi3Xkdp6KyHtSGAM88LuQunwdCik5v43uPxLmNggcCNz9v0N4IB_k0YXXzriuwh0ZFaHEW8Hkn3b5lniNDEs_hLbbwgP5_6uDpB4EqaVYFB7zTV1s18wR2w-oKEDvVoBzQfMWfeshL2sCABUccyDkPSZIGI2A-yoUzm5Xaj0IoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1wuRQWkXdy_2bZjdjfKYzUfjaOslnnwNkEB_n4Soz0yupJqGd6azszZXyZS8TbAafuAso_HZLE976yPehT3jb1GHDYFCJtdRspjrN50--A7oebT3plH3c8fSEi-7YyczJZvFvs8Gv7V46P6xdfxGCsMrYU1oy1ctfNZCcCeWEGoqx73Fd5VJANOfAHe_3_9zcPL-mDbUHApaRjEqwHe_QctMAl0zzal45NlHfiAh-3Zc1ZGRnUqfN5bEioFIW-KOKddC0NqEP90UeIQG7IcsomRexY6YRxnRUEJQtUn5yqKcVrmoMIkSwgMnQ3LlmzvRuNL_mMEdJxo7BYimVPVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEqpjdXi7phaJw1eDwrATweH9IKF8j8wmjO9ufZPLjjf6fUsF6GL508AQ2oCCT-LjZo4PAvMkjpZaoAvw3ki2C7shAnDBtlApRi-mNXUKKwUee1Ne4bK9P6aV8I8fb8XB0yCXZzH_R-f-PnJr2y09JamoorFC6zWBEg0qtE00OFDh1pOKdvvkQgrVcGBZ64tttTxemdb19IiOq11n4DWIumfOLWxzff6SmKm9pSaMKWeypi5bMwfINOfKrjcTNOevfrejhXIh9Gda88jx5JOfDLfM1GYfA5kUGLyfFyTKubwuOCZg8MhJ6UChJ71x0LzyjUAyNFiMcjYFJ390GJwEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbInmsP3UulhOH58PMZu4I0r9ZjN8QgTAq5SzWdRsyTsEne-MSxPMG5iNC4N1S-VW7RPh81A2CWPyEMPZYHyZ2jlz908Dlbmw9iVRv5Tq8acljuLuGvDHzX8_SQxGOArymtDKyUkveY3492K8H-nWkkxc6wQnIY4G4SmfkwqaeZe4ukO9Yu4DPP_Bs9emtKKGn0QPE4tNhmCnbPjjl2APbZH-AvCeDzuX4tNgSSSeS7394VcLNzzuYMTRL8ts7vxPM_JazoHu6EJnkjXLTKwWROk9Kl6qyLYy2Z5j0xQgVdv7kDPvke16N6H7QwKb_OgLCkW7MHT-B9-TgxIIwKDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVKhlkSg_M3577dPDX7SJrMM1rlzZXBtS42KYTNizRfrBetDfH2T-pocjn9JEzHfzkOQdTwGIPQ7T4AY_4IbAD4f4bYVK912JzOqK5aE7MSiE8KnQxvqe-wRlLL-Bx2W3piSQtDPlK12u3G7tR5jXj-SkYI0nzd78Q5nF8lpf4sbCfY4bH0i1YFJC-4al3tSfuPkV1IknSfpqcuSME6sgZzHI84ObiY5HizrAD70-IfBGYgH64DWxNC2tU98YFW4emkpR4ttVPw2aGiwTHJzF_0DAfHG2w3lckEp7fuKISKkHWpkYuHW7nLsTeXSXI7o7U387PC3uNugRXNWOV6_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLt1laQJbuS-zBRvTXOvDF3o6m1PQQn06AATTHHy2NuodctKoFlt9yU1qWSF--KghGbL35bEB2U9R5o4uEj9qTqeIq6sTcmN3dO1ComV2Xokn5Sy2fCmHGnWgEkRVuNWU30VHpiekvFkZf8TafsyoNoWCtmJSjJiT8TtAbxmG470leUdHg_fp7Rxc9iSzeSKGe7XHT9Wa_LPNQ_OVDXLfT08p-KUDe3fo4jrb7NWu7a5B2XavHXGw2w8-eCZ3H6xSXyg9Ahoei4rV4Q6nYDD7FLmFWEb2xA9eIMN9Q0VNtE4sJd8uxNcC7qGqPPx0YRlPfDHxQQHK2GtGqtmYZmX6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGDVvry8uRqy0XYPa2G09KdPJmPzZcZJTs7HvZpnzD0y1b3cVq5z6DinNtG1_GpWWvynfjgtuB64jN6trjivsmRS9Kx7kRDY9BZJ-SbpOfadOPj9mt3D9t7YZXCBpGsw0SIVPlHO1CLi2YnuHH-7WqxDDJFRDAlpbrUG01MdaYnfE2Yuv0ODPL02p41Z7upZwT1IOxaAMkDc4H11YAN3m1pEOdXDhrS9nv4-7uiFou94OUYRgh5-I9rbHE5dA0JD_MV1vEq70amyIMIRqz7x5zkXU365YTUcuy62VlF5PHRpd7JGNLEQBoOdLF8iEI10s6qGX3NqeoZponi36fdRXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htYUkf0qkdr_jiQpRsVOUB6k9x3cF5_6HKe8DSXdIAVHDlv6pRAhoN5d1NKn5JshgLmF1PXdCN7oJDRKzNEFu1ItOF66AfJUvqNaxDaBwwWjCk_lcJxbhoZGAPrG3VfrdHeUSALMy7TXJZf1Ug6Yt5ZVwqrwwKXk0L6r5yNB7SCUuwst6oQR3s6IH3EG19Usno5MZMk6WAPgoDtnYGHz37qdh82TGDGIbMra5HSxdYDVKKuGOgVskP885ao7jae0Ugh47VsJ-Gnq7FoAwtQC60zs741BBp7wvRHBt0meCQ0j4MAyF43fzCiB9WbgeuGv8TfgBBkDnsOniE8LnYBW_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnglUr50wVLalLwEKKkNfx-CkCAUp0Oq4U7PswviQsHgt-zIjYlg14ldmst2zqRlNPCcL5k0HCVRBZiPa94fW-eldBfbPVp-wWnOuEwbIDN3fmb6bRqx8rdCI_g9D95YKL_kuXBI_WCsykWO5nEHUoMqlPyQOyCLiSZdglWKE7jSKLx2D8AsJZ2_OZWhMGOL_U5dIQ07Qwpj7yH5rZ3x-xXF8kIOnZJLsx0RZ41JaCWF1vkZHAkIDe6nxFWF8VYslHFe40YsbTNplcKd8k_tMj_Gla41taYj95w2SREHpIKMj9yLmL1JuHSya73VGs-0fg6xLzM1hxt_csmlz9CIYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5dfGvtczm50RJXTxrDn_ejFSCSUqjpITx8byiZwvikT7TjZ1yOd_sL1bKiZprxsn12la1msTIBrjD37o1SIChuZXlYAeBkDds26sdu9lhv3gwhlCS5qmLZehZPY83Gojqs1I9IVlALY6VpmIqj3jueU40IWOshdft4wR7Q9fFHCIsY8mns6wxxTN9CfDflRyjQPUCoc3l6-Kom6cMmyPIOgYeP0WKMZUixaewNBxFTYYR2p0tOhZu2OMRC6hS2x7QnQSWNxH-A5tr0Ehhw9yd_e3gFqShFxvncWOauq8OUoYtoH2Qo56dLclqrW-VdZNNYUmrzMFJOqsq0X--Q32A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJw-fGEsf5fByxU1AWxMRnfJ-pwoqn56pWBXdku7uf9fZN02DSmbLFYH0b97EL2ddWU5UhHLZOqivQReairJFmJYJVRGyh4l_AYM8IIN_MgDvgH-e08Styy4cHHbdO30nZbVw-WzRrFoloiBFPVBt33o4vtIKclGydcrkGDlsz2DTPz71TM6c5_NxFBqcdr8hk948VEC7-QiWSaqkL8ZDeiuNf1-adjDQLcVNMhh-zGtMktesl2E0_U0eaqbLDYmfjuL3qLeYiQss4c6HGVMV-bo3bthCdN7Bj3SSPjOu5KbVZwReGPJSHn7XtG0jDG9Nz7PpNjTiS7iOnhKQ9vTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McMygvIB-5IYP-dWikfkg0vhq5AxbN2ls5dE_3C4Yuk7ARKPSpK2EjW0o8cXyo39sq5r2tfk_OekV-tpK8wTNMBcMjswvK7fOCWLdjxzMaSv0jNF-c1walC1-ThO-lQtthTcRCdB3Y56DK7s6ptiSa_2exl_FrcQwGMiTmRqvvLiilXujzDFYcmykcEjIx6haGua24IoCUs8jd0pdLpPZaXWNYkYI4bBIZBF2-7UqmbesGHr08r21h3Uny_RgWAGotKfcRC46vT4443PIE4eEzHrywExsoT0plGbAbaYi2Ur22CLm_kLbRt_4YgOViSDHvYdZMRzQK2L7DjX-D49NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0mh09H-RcEhyScJmBe5H4pbXCi_7LezuPCXVJNNlMjec3XbNkmXQ-fQal274u4Q8ESuwobV9b-uKQ8Di4K1I7IYQxkbsBWxY0cXo4srxJUTgFE-NgsY2hjfHZ8-HuyImpyFiNoLfUxQQoE3RE62WduiARTgpI7hyN4qY20VbDCjvcz3tYha6544YphNo9ALa0AX1XAB9fSM2-ka6Y23sLRY74uhSZxbyncz0gkys3xb5FpNWKKkp9PkC1KZJOlt9WlmdWKODVsikHO-zESgjAJKdSfoL499nMzqR5eqd9I89hgMQYLEd65HzEIIHvy9F_9LZON2nyIh4rnOtlQGiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCZ14ofzMjqr7MlV2k5wcKsDo8uvZhFhv6Ecgn6HFVubF0G6ekmb7mrPXoQn5ZSHbY7d-YABA428qaTgz6ZA6ZNE7xfGM6attOya21UdIIy0gVX62_OGMQoVOzoiIDckYC4N1VI6BpZ1acVG_S_jshvC7vYrfNoqntog2uF0A2m0wcLQ9oeO3CN97o6GPEKMW2tacwp1P8JhUXHrqgOH5SPlboZnvG_yO-DjPFos6u5-uXXgPP42wevTJsNptsZlun0C5f0MNxRGLseApkmvexBU3J86qSB6Vf-ZSiIUnvs58TlUWR0R1JOBl8_kRfWwH2qQZZKv0zTWRUyvHTf98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0b2xEL6652bCbzfDU3C1aE-Xm2l7FesgWjsKMQwZJUONxYpUccQh9RZqX9uczeQx0vUYW2-Q5Nx6v2ZvwGo82FA_cnKNXuLKWSq2MBYX1BH8M5IpHBgjlEmV4K-YO1nT41E2BACW0mhsW9O385KtwGMZIeSYaorFI5T7XVbgB3i9T9rqivAgU8USC4vEM2jl4N18gdK1v3XTu5aeL4n4B6IGH_aEa9siShe2SiJXGhRTxGehLmbo0xMd0LEtCZjF0b-y7K7rXf4tBmksCUNe2ybp6rhyfAaFlV_lu11SzosNkQH5qthP-RmzwThm0NbUMhuyPgJs5Jw0BIf_gHedw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIQWGB6IPpT8aTnpJvHXukG-kj7Zeu18BzzJvCZcuaGPkQ3ZYKQHnaKLxz28_2O97rnSZbbbbcyZ15TeHPWsrnHpiaKukacgxXEgYuxRA_Xxq0ALglBRbkAoQ_uZOtCERFcFDuFn3iW8Nz62rw07lNfFTtetq0sDiGKXEpi8PehnOFT6McrwNduTv4yIbPjZkdtRiCdLZR9GemztSZqxS6BJbyGjKf_-EhzAL83-HRICslk4oOmizLfpWThuNSe4PfjME6Hl5jwS-uVSJ1IoTjqi7K_5wTFSPrCgZl45x-_DRuTbQzxygTDH9P3A6su5oH0KwDYNK4vJtu9k2OP6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8rfGT1WymJVbUfGtX0mVcSn6rgFoqd7V58JyzbX1nfyRlU4EJ880AhKl0zNsatASBYsqJKT_50Fv0mGD4Bu1A6hb98nY1kEd5ZWHOVatENsGp2JmmBfz9W_oatv3tqh6oslKtrIHEEJ7gddBtkWku8RQhJbGgtwz_qnxpqh4vPrj0YyiutHuDQUgHSvKS0o4dxY4K4W_iW0NxOYR8ZZBYqiK7fNigtCsrYHWejEDez1kn2i6GKtHz8aIIgHManTrV0G6tfz5Z1UEERXUXNa3p0OOV1yCxiy20RXymM9dbYVUQVf9B0BcAEWyx5g5w5Ggz0nZvaxfyoPqQGZ_h2a5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3dcATpCgki5AknbW705G2_CoSnhwQ9CAmBleWbnCfQsCci4rG73SgNkQ4m5NRNg-tPmUbQQOY9a8pzLNtuv38y1RQHIF8ii4hoPGma0D22XpJYiOZD9Xk-SxkonSNRH3j13tgcXzp9G6U-ANVCNvCxyUOJp99U__Mtz4N3BWz0VeY8_BxE81ojgFtOdC0BdB4dEhq35TVnQaiBevsufXEoXCbDRqri2pyXcOabqehougP9PapWVG7REIUtFvF9DrpzE9me_PYreK4YtuNVUpDLfSXIMKe94gMp5JoL_3_S68u-_auBKXZzVdSjnhS5sqMlLgf63s_atUOc9z-VJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPaej5ghP3pIOaAr8TYiUX3aULE4oQ6UGnVCzRRcPa_YcliFZtaDRHwPuo9aPeSRLollCfYt43arEl8VGIQ0sBsH2yFmiDIKQ-FV-cMc8kSmorGRstzs-mXh5k2-ajE9q2ChueggkR3x3LbQ4RKD5DIX9LcJiu7tnDJN38yxZbgDv6-saflKHNWCCmy_LObDk_w52GbMycXXVWmgBDAZS5K4JhuT4-fMLAO4Hxn71cpgZ_JZ-D9Nxetp7e1IoOQgmBm3kO0ir9hEBpNChT-SaoXXXIWJjVxF4c_g44VBD-AxVR683bIObRsRx4GSVf1kdfNXm3Vd7N5KFsgKy0If2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQhHftL4u-sKkUllpQkBLWBSUaFx1ho-VUKrj2q84S129LePSsbue4uYqIPK0lfyZ82JKWk-bDSYllFOpSdtMp5gp3RT4HyzmiINx92_h7k52RV_k3MSZFOq--ApyWs7inBgHJB-NhVFPkXMUt35H4ZclVBqFtCtcrke0tj-Du8bhvbVmy7r4CzsC6NG_crT-kr1tmVP_h6hMKO2SI8yf30Bx1rMZHgACnA3njxniGijALkBP4P-48nZy33vb7ZkILCumhRjPNmuVNGRwCsX9_wvbipgsm7f73MLO6cKoy7mg2ukgAHcBMqoyPnvDppgTTOcjS8sGt8cmD0tJoNIpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm0K3qm2O_IUrx8k3NcYylJBHwGLQHNXM2r3HXyTybArQGMKyE-akmcFIrFfzqhpkkALiG4OQ-WNZ8U6ZwOyyKJqGapLw1MPRjFvRE7rF5R8QcH8-NBWBjP_rK4WO4ZNTOCj_QF0aQKc2D4DtqWxLCzMaA7-tVr8d2N-sXPZhHNY8slqPfvRmcq3rWMsMQaxzVbSDOgB6wctxbZh2GRf8EWzAD-eXvjgGhx1aYLdr4tH1uGzBWXeYrkFtzEMNjx0iqpP0mEnKXcyT1JZMRNOehceb71W9cr1QQzZebb0zm-Df3VYuMV7VPD2XNz_9nRcafU8IJvMQ8YwlOWdfUFVMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw7R8OM9lFrYrHm95ae-60raR0VF5ezybwxHkKj_-zOHu90tyzpwoNx3xhCsztfOWadzxiJC6JfR2pWuP3w1SBC0nzbIXZC3ePt8WTxTeG4z8vGHpsWpN5qhpV1N14WbN30RVh7IKELXmik-D65z7GxtN2Biceqw6PJdn_BCKw1jzhjD-LK2HEscG4QD7ygGMDBO_3plFIj9b-NdWFGk9T0CRVEHjSswoZHfpGo657jAwrpmeuk8hayw5mqoEx5zuiiXudloORuBx6pkJVvWc2jz2-ZFBnCRHnFX0yATCAmLYdnWgPzQ77FxGmkjryB1SmLCrrqvP5ZohJTT5K2Wtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKm0VQL0AA2ZaNGfu7QICUNysbPBzxrq--Y9V0SBSvo04Z3Y5pkVAgMVQ8JLwtroF4DKeAt2Va1bPcFuCuFxYZqzUYVakSZ-MCvbKBaxS1TEMka6BfCymhuAAQ88m5oz21GbIWFbTi2T0cB2hWqENNOqGN-GpYFIEpjX5T7SEoFY-195rCpbkB_AukHmChG0PJIUAbu-Ch84zRNzqW4aTJhcx5npeJyVEXtLpLtKoJBD9Q0KZgti9UuYJsWbPH2-Lq9-AIanqObmEfuVfdtdUq_Jtq2YhOzr4MLERpTTXQE8zqtu3BCVfAdGhcDbkPKZS-_vMF88jgUuQgqlgVWvOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fH9Y-IP7uvosY5UBGlnno9JREgHq2mQYGiAjAOYPEWB4qnfOfS-0vPeTqEKw1lKYE3K1sy4MghL4diB-_0mSUN-YoX-k9MVc8K0gqjLze65JGPhVKmBdTfCxa14iv8E-fFifZ1zRAfJa-9g8pSP7KqpeMu9dkg7g2m8er9x_SBW1DKBNkkkh93tY2DEmfItud6WsYWh0iw9SNV1bSOvx_zyAwRPEQeQ4NuFiptA-cH6WaEh0J-ktdQOUh6S9bV-7tjV0h-tf9nNFODlLGbnP741EDK9Af6k6nk7te16fN1ij1Jtg_ocPVKAs7owE_MucEKEaD73CesUC_gTqt8HNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1affCAIA8Yjfcnz_cFeJVGj_UlZIPLNFlvb46azZqR4DZm8Onn1ypvtaDIgCaJUNinp54E5lPDLGwNTIPWn8_S2NE4jrGUSG7g74zgnBxr7M9x0z7Prn8Y2YSpPGKlWwQTIo6V3FtD0xluVYTl4Q89GIV-7awnA7NyOG5727j5-X15AwiLiA0Q89zvqpjqyrygLCbyzT4LvxRNq6A8eiP0toyGzoVVhjFzLhX0zGCnFnoJ-lLeOJr4FdjlH7TKijgnB1_cpg8ZXYtclVHq484tZ4F53BWb_dgWdySq-HUHvVcZa2y7MRUkJebJQAdIC65MvrPXWFwRS3RBhwChq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2cfVbxThoRh7a_EC9kYRp6NUWQcunJA27rpKe5av3Rmxsl7rYayUrvNS1x2v1ubvSeOcoRnq1cuef-HP5CzPuUCtmAD-K1Nl9gydSiJVd6Kf9B5bnV962g-TPNeGnJcbNa8dH_SH92g5nZGaI-FtkRHiNkNIEBH9_7BC-kGzfVHldB2c0QEU29vsEoGoY0POFiRmV_ud5ZK0qIBpYyXg40O8T2RwrfQ2EuKd_ypVZLjUsalcZRUQF5zJpVPr6i5QK4FYiqlv5D5XC-2R2bd0SiA5OWuistNi6tiSGTnStPO82W2Dl7WTv7vq-eeyJlx79QeZkfAfS67h9qIwpG6NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
