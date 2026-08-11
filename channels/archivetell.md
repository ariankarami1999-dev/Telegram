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
<img src="https://cdn4.telesco.pe/file/SmFxzGSzHFzCQqFP1BPMPVNLFAAz0v8SvLLTSXxA_j-7jpw06AoHlrCJViEoynvEchpOm7N1r-JgmqZuDU_UCvM9IBgPgjRuB-5WM3m3LIx-LEKztVRGNQikxQ3xvksmlsogjn7-4s4gmEMY2tQWSWlapDcV9T0th5y0H6vz78mXt-N-FAehk9_DOTzHOq5-qsubVvd3SDSkgKH1R-GmzKZ55s_mN2YgS5kaP66FL4vprqxN_6yiRaKgTgoryFnoT5pxYSHg_FUw_tX4Dyk9kcfje3v4xOJAiyUkCN2xQPR0dTfIUKErpaobz5zIQveF-k3AqLACgHKzeU79aU14PA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 03:27:50</div>
<hr>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcVSp-GwdgKd8rWE0wcE0F2JquzHgeAuyj-0yUpkcYB9bU6SjZ-Ves_B88hX2UWslAcM0XPLlqlmtNIM2ciJtTPl7daoIztdUAQ7c7vszBYeH9mt5ltUK4yajBqed9ddwsJJSgOhhvzTuOgVKJZd4TVq5QILzfMISVIOCYuT1PrcjRHlbAnPR_OYexDX9vpK2ACFmSdv5GG2qQRK1oJPhA9egl8PrPQ2BoLoP9CxIfHd3mHRCFrmHH0_hIdftQksQnjR8o6ECUofSbqlmzzOF0DtjX3DCq2-4x84TkSlfDq_d_V9zdH_dtuoPhE8CROt1lqsKQ0na7vyzS7xnz4e6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #19</div>
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
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7451" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIc6q7o5fYQy4lTUjZUAf23wGh_02WKp6OEPAoDjYyAHpFnR5ggYwavXTKn5jOG5FBN7pANcantTjBPaEmnf35wti7hWi7RLUT2tDHqDARgj__GPOEaLCveEH1sca7B8rf6fA1X33QWMpjUrAw534c3iLFMiFUFV0YjilH2FKjjAzfD_nD7_-8DRYWchX8N709Dk_vvU1iD-FZZ3PjlMDTvGyHEhctsdmt5z_-i_hrYHk8-wRca8inOfZawDgJ5JuVCPKr6Q3D7RA40ja1GuoxgGhB4taVNJIdjdnTMKum3VRDoEW3ueIibvmBgeGyuu1sfy_Y8jOaXMRWLjTT6NLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
