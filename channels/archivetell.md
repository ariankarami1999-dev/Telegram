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
<img src="https://cdn4.telesco.pe/file/VVrrMJf82wkEn66OJq-RpY3q8RGLPgt4gWhwNfLlRUOqSfW4HIgEp0l_-2KTySKmO_qmjQfC15cLVzWqS14JzEpeu74IRJiV4tNvXIiQFtV6EOWWQW2xuoEjHsJldos7jGFC7TIi8oIyLpkZ2hCMCl9uKgyD8yGbxO-g7J9rDj21P6b53dNBRDLF1M6Ai9dflUtKKVXVF_P9v45Nn2o0BQpOeFrFG9LmnuIKLOIzxiunmx5r88XwsoaBMqai2Yt9Iyt0jhoyGsRBWIixQM9FGBOZlTmDkSvGlqtdCmZ2HMwGjgFD1Y9sguM_SIAFm8bhvRqThYCR4HIQ51AhlLgrGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2ZOyucn4ftF1UCTVuHpaqCcQCPVMxY9s7CxrFsmonoSDuRJYlSCioM9hcpuVY9QZgQffxntb-9CrdgJolBxFIch72II83rKjS0jGGAvXl21eBD3DHaDYoTyAdQ4ADeEWFr12yxqib0pHHzDr95o7JxlW4owTdngHGGOwAiVdd9fhz2gL08gpZjSbPEcX8jWRD4OfGXNH2TSsIv61OsxCNse73I9ILWXvVI8s_uSWj8p760qgTrypzswjNRGSEEeskeMP5CEr4DTI_zhQtryw-MDBiypKdXhO3xPQWgH0B3rZYG0gUBGO2994ydvXs7WOBVx7YA68y6JJvrf2VdE9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 848 · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnSbIZP88BDpzx_Ut1r4Kmgk8HRuNOcchyu-Dl9CWlMQkWwXhaknc0Gbd-QFZuP3b1tAPPOgtHvyl0EHKpqWhWk445kTa3Y7JFVAyZHR2gy0dgp3DIB9aG2RtQqWRXcgaUloXVHbkWcbl2KJc0VNGlp8FnJDMG6ObvzQsv54vGAIaaIh-fA7DqQc2m99XftZYK8TjNsnfWZKvv-gJNmWPMreO9UVK-VotfkYDhkHnNggNTXTqD6HwkLA2X2VMuf6J2l1dkOe2lURfiLM3-KBs-pE5ynKFTiQRGaEDeGEaANUttiJXhU26w-lkrJ9E9PmMa0BKvxh4m5poeIEHZ30og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7589">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPremstore</strong></div>
<div class="tg-text">🛍
خرید اشتراک gemini pro تنها با 299 هزار تومان در پریم استور.
❔
چرا پریم استور؟
🕖
تحویل سریع (زیر ۲۴ ساعت)
🔒
بدون نیاز به اطلاعات و لاگین حساب شما
ضمانت کامل 30 روز
علاوه بر جمنای، بقیه هوش مصنوعی ها و سرویس های دیگر در ربات با قیمت مناسب موجود هست
🛒
شروع خرید از طریق ربات :
🤖
@prem_store_bot
🌐
وب سایت
|
💡
کانال تلگرام
|
💬
ارتباط با پشتیبانی</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7589" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7588">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7588" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjC_XBTjAciRb-GCJKQBNWzKQMPgK3IXby86zrLPDmnVKZCfqF_YFYoflMiX0Wyanf3v5KYYln6NArOmJ29lo2EK98TIpauNTYN_TT04OHXYB_W0WcEkAhb8mwwHZnRYryXvfwQlKq4Keajo_7vmLefzVO2j0kJHpMd3abrK41luzxuwCB7UzGK49HRGtSmPf46tRweq12sidKPSXgPFfVrbPLX1D9zF-3woI2n7N6Z0phm5CKTB_Lr5tm3ey92DPiFaAqWFdDP7voQ-oLQ29QLYY1pqpkReJCnpRLNCyPexGNg3oBOlTudgEZUugeJS6Cw1yTu2j3smbYjfvdOjQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa30vTgLOwvt62-kPYr3UX2plhaBkbAR3GTWVm3svJoFsDz2FnYxCYsH2P9unvvO7r5bZwbYeQ5-VuC459LJaGf7abf7l0baDULZuHiDvKPyyQi77jCRVgCr8udkycwnFTcbnhxUtK1PMTGOohqaimW9-602sXSQ7CillNlQ0sZUAP4fzJoXb21F1sLrFFgdhJDw0C0DmdpPk894PlaL-aGl9PGYCZEbrdXK8rRdjsWcdBFUpXacx6MYJMAwz3WMVK21eF4gwrbiEiExkUVAAcI1N5HDXA14sA_pxRY1EdaXBR9fAhS9hqMot7Jlr3qZmLMQxK8GmJ_KudW2fQThiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5TzCmZy1YLZ2I9x6roNMkOjRvl33S5ZaDxgcyj4qW_MwOmUmjmzXsnBd_n3gy3muoJB-QrjsxO4UDkk-jbsFsJjbNMJyi4JruEsxnJmOlX-fQeELBSDb5t1SqWUInRUGTTybF99DlvrVWyti1LhsbLgkhoKbP-UtE1N2bUkQqb3b8kQDuAQPC_mOQZS-0VpHCwPKTPYQrTQ-iTF7gKAa5sIqwuva1tjM99jlzylh2yXNIis38qvDm2aIsQU4KTvpYR4ZF8UEq9YuTpfAd0RJFmy1L6uM1iHWJOZDIBgqQHoy7LWs7NbNzs1XaeDXH7IMj7vOznDy7qCSEXnItyOIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=QAvLbi20VSZibTe1cWJiIbdk7LtUJ_3u9YfiH4WsBNZwpOJTrLujxCXJwXA2HsJUrJwaENKVW41bYJ3wF2oo3Ws0MJRyT1GdRdDNNfwrFOAoDqCAl2E4orEULNtH9J0oubkPUn0xUbQge8E8CCpkL4miB7uBwdva9wo56LHDZTcOJBIZhvPKe_ZghVioM70u45ZhbLNUBv7OFyPSzi0T-yfN3z4IBe1ovIW1AnI_4tCzD6dyG3hFGWhdOKm2BWeuAiyaoP_-by9cMiqBLXRhY9TQweJNT7Cw4l6YCeyMQ-jn7K6U-3uI1CJvOwx8KY0f2x45yCUSQ873t2OQCithpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=QAvLbi20VSZibTe1cWJiIbdk7LtUJ_3u9YfiH4WsBNZwpOJTrLujxCXJwXA2HsJUrJwaENKVW41bYJ3wF2oo3Ws0MJRyT1GdRdDNNfwrFOAoDqCAl2E4orEULNtH9J0oubkPUn0xUbQge8E8CCpkL4miB7uBwdva9wo56LHDZTcOJBIZhvPKe_ZghVioM70u45ZhbLNUBv7OFyPSzi0T-yfN3z4IBe1ovIW1AnI_4tCzD6dyG3hFGWhdOKm2BWeuAiyaoP_-by9cMiqBLXRhY9TQweJNT7Cw4l6YCeyMQ-jn7K6U-3uI1CJvOwx8KY0f2x45yCUSQ873t2OQCithpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHJV5pSkCpG4ss9XQ9ACnLpnwmf2k7EOqeFmjLxFzmi9bjUt11tyRvZj5VZR4utgKXpzlVbZSTqjViEd1r_R6vYqOjG7FqdQtuYDuhyTTyi8_2J5SToehUXgAv8z3Drgyyk2VZn5lK9935hapDPb-ZwYqc_baU0cSU5y0ME0cbMf0J1I5xtuEdvBLqiEtvR6aWPKBAGfqv5IlNskMEejUIaUCv-vbugnuxb1Ovfa8Ra-4qly9ftHSU8GGXm_Ww4GcOiCIy6_igpkDhhtqwmU45allHuIIC5Kj8-v_mQkrs6C2mLBYmWTMQPNLAPYQjapazDRZG0pNruY9qbf12xQ3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=onel8S47sgqvvHTFTm_C7RRWyyoAh6kLzBVF-UL1dmecO1BXEz5egaqq0os64waedOeNHu86DMaV_GYKVrCcNE9KWe9BOpvxIXTZC7PuTwwq3GvkWla3DXIdP0Xa5uLnfZnohGNZ6Edgr9X6ykuQ-ETqfYHLyMAFjXioM89ePbav9oZbFtNyVqVWiOFf6mO5SdsKTgw3VV7i983ono1ehIA2BiHgjxFCWChV_8JnHId_c06LaAB9_9AlzZph3EUBqYOBseukMZy_UXnpcRTWDRDZcAXogTGryFhiziyWaWC5qgVCobYL1Xnyi7I_zfnPYC9qYfC7lVsqsax4EelBLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=onel8S47sgqvvHTFTm_C7RRWyyoAh6kLzBVF-UL1dmecO1BXEz5egaqq0os64waedOeNHu86DMaV_GYKVrCcNE9KWe9BOpvxIXTZC7PuTwwq3GvkWla3DXIdP0Xa5uLnfZnohGNZ6Edgr9X6ykuQ-ETqfYHLyMAFjXioM89ePbav9oZbFtNyVqVWiOFf6mO5SdsKTgw3VV7i983ono1ehIA2BiHgjxFCWChV_8JnHId_c06LaAB9_9AlzZph3EUBqYOBseukMZy_UXnpcRTWDRDZcAXogTGryFhiziyWaWC5qgVCobYL1Xnyi7I_zfnPYC9qYfC7lVsqsax4EelBLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2hzHK3ZSnw55aq3Ofq7zivYBueyHHyu5tutRIJkngBAo4gETW99i_PIStyXJpWlX5NeROc-gYUgKMkzTN3wWVy8TLI2QX6paZf2QGRxKSVOmrW8_ZzBWdMQULetjLEqevwVYQe1QvQMkLBEq3dYb0XnI7wHrg-k07Xa8PQtv09zvA73EDRAESsswA4BQoaLXD9tENybZ8mE2QnJskwvIb9YNeuKo3L3pscjdBqcLzZcoekBiZPsuqg4tJuihAXtNEbWcIcp6AjEPEM4pT3lScbrJnxxOXio53ZzblTxhUMdotg_ES-4HdyhVdkP7wVYoouf4-c5uvsfULDWxlmARg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK5JiHGD996b3s7POFfyE_pmZ-HwoFFMbHZGpYjLcTYdZJGAeRDtGql72TXrmDXaB4LJOAe1Ye_A8M7tnWGm_irmP2JWu1sVZ6R7p5HeUyUg1FUEl7Mgy2Fm8EpABkAW1ca5taOaU5meK7kaO0W4HP1u7hQs9l-P_0sEbjwNqRt7wMZ0rkKAbkv1Z9k8BjmLqKWFPdVaNTsNbnW8HKc4qEiBT2Rd3KaSlr3SpAdHSDcVDSeI1FE8R_0FDPPYMd9IM6Prek9wh2C3tCu3TKcOmJCERtsykWg7ZcUNM9MlO5VR3CuvV3nkkgskRULbvfaihO74b9kgrQBPNYPW0SaiTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsJz2vTmz1E9u8TZk8oJHpENWWYH3Z1AuFrZDWmETnnIBLrccUZWRsVus8uCXCTHi1UKgWSTdkUGUez6EqBbs3YPxgDy5wmrkoyJzszn7zUY9q31i_hW5a-Yhe5t45qWRxzpxUi-NZ0QCqUEcJ2qquejXsKMJC02av3tqq7AMaDnQMMkcvHCOQVVSvNhcvPr3zN4PlSlXUCuNktltBkWaRpfpcwwyjZsRk7qGho9JKD1wG42moskN0bjXxQEKQHEzyX8C-HsfH29uGgaumoQfakQOS0PBIHBLADhbG90m04STy18knnr2qRsJ6S3mmw7fgqT7RRLuMYrAvuI3pVUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxnJrl8rc0y9gzqIDrlEgekDzjAwCamWla0f1H2ypELhyzHv_VOnGItznIxAl6AVx5MJfVTVOSHbpJINJl8IUbzVUTi6DvgRUDWiF9eagZXMNmTNlTVt2YOpHpZV80xFacjgeMB9UWqAe1v1qAipyHcrVp4KWK5w1RTip87XOupKVmO92dR-PzFQT3qGF6X824gNqJxba4XP1Q8F_chzs4Me1xIaeBwGT1znE185WNvUK4cKPDapX9fR4At5qLEqTUfEHMfJeXpkFlX4InhNWCoGpR5epsj6ljlGC315NgDhbLLfFy2nDGqus8LZx6dS-Pl9mGhHytiassdIwu3wLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJoEdGu7zb1QzANUxs8glL2rjyGciO-3lIr14P3l-IfSTETEKtcFg1bK_Lz3QQCQdmb8ogDSxRb-DoxxXccPoDfA9Vpsdt-ZdWZyZPRvJH2mFUPsbApQCAkzH09XZZ0Cjlfyq1V8WrtwDKWEl4wII56ZoBlOuTAMsFNVOYiftdeqpkf057VVGomrZtnas-LuhQZNvbphi_JL5UUppoOJwQyLLg18g8HRMoEvBG8pBvL_QXVSf826u8O1-GArIHmceNklyORSzSL9djDfVQSc70vtiXx0oCh47aRSuM1aconq_0W29JHIlLWAlTd7ubsajJd-2d2cVVHPXUdXOMTr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZQIsmwIqd5cl-_PkaojZnTOEENkRm9ePydCxB-kHy1ahIL6nr66V9vRDFxK334KAW22va454_H1-zblXja5GZMBSp8NKPVQCWESxOn1WX4kaA2JnrElAF4zGj_uPCBa6qCMX-ZUemvq8_F1dpmlEuRVc8gaQ4z0GI7mk8Yrz6X8c9tAGXfkVUA-EFN3JQuhM802Zfkeka0df1_GDd6Kcc6gjJYi-JiDbXrj8Fl0DNudM3XxakzmfEy0DIFBKQnA66bF5UT9Jh2F_C6_ZBtjz_gYhI_yU9-QvsK6oVmeC1G0Y1hGhNAh0eDFTEyde5qednsv2Roy5psIchQgB00odA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBpFPM1guDdwUno1gKQjm1jX7oL1Wlc3zOSnd2WtzWZDTy81LNwOg_TwbjLDWpOWrDCWn55IVymm6kTPcc7y0TjkOKTJO19EZH8TA-ozIQZxGnEWwWZ-4DTxHyC82ISxz-m84DPE32G8IENz1DcIIO8KxYq5v4BfhJHNHCg5RmvrOzRlF3XTsGtVyGx3YsER1wF7bbolRwiOv8TzNmtbNJsLj6hvy6zSbkegqDt_wUnGVCOCqnOpGYL6U3VYUx7ojKIUNMaxI6_guVj_vcwCRBHx1FIqC7Qjr3mkx0eu66KHJtSFTgU5Kurt7wxnCrkBxk2GiAvsbDKPiRKcAYiOCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKnQQjdnMn2l3qcqiYudAJplmKRXTT1eY0WhD4O4pCCQ-_T2KJJ516EHkqhP1O-YAKOK4QGg_honfamjgtCDOHC8JVjADg90VSufjBimsKSnug9QLv_I1j9bvGFjZNoh7lqgf02kvHqam6-ovSxRWK7wCFbps6yS-5g7Wc38oNg05AVEt-RJ1simtQPGsW-3vdrVlVgaqrL4_8nFUzGHXdP8-79JR1vwZ6hUNOLsSjFhj4Hda_1riSxYkGWdSgEUFbv7r3lKIlwIgiFPm7mZTQMFja1YqFZOQAu1XlAibhE9OBVvFs8LjkZ3OV10-ylFEhzfSxstWYz_E5w-AaKIWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSyidNd2AdhoFZEbFFrYY4aOmBfhxGq6NyOzN5l-cn6i6c3MyBgR6HDqSvAi0LbKzGL2VeZaVc3O5QaQkEtXiXsM8nhYcMuP8DTZ_uCJpX-ZcN27Hd_62zXSuc-HQVrjeqDdYKxQJhTVw3CoNNwT8vReaJlh1TwkoqQt_yIj6WFSSKTATJ3q6cUtBIIGBit_1MSAmGuCQkVH5qho_DoX2jPnnjRPz5vIVVWVtAnzz0Qoo9OXgHnupOSLMOdbuC0-hQIGJxx2Yw2DUIpHWNOV6Mx6Kgg91D9eEVo3iqTr8DUXPRnphR3MUllXoxnkSLxNYzelhrXtK1X-6DxxG3voeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbt17Wp8Uqi92ue90Fb46SO0BFDGkiiwmAF9bzbnrjeYShi6a-W7IqChqujHthAU7w8h3p_qn1zjoO9UgZN_VqIpGbSBaEXo4ujbfVCKTg9mJ52ypLfSP-nAVlv3sh3CEsRmOpOmip8AnIHn-W6-pWT7kFABWfG4iCwjPQNcJOsW_9g3Aqg_IsBVD4TNhviChsK5qe9bLBoyZn5tyM3AhQoF0WXepGvV5fMSNa6kG07BETe0nPlVrUXxYlFZ2BiMtIAAW_CIK3Fn7j1y4ijdq4c4mff2qH7idXNLqugf4KiGx0tRPGn2KvlICDDM9jUUcn7rNUJ2lMuWN9Y6PYSQLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDIXhkeQlFHEJrqAjvi2dAS__Sl-j8yayuY-av2bapIESgoTDaCLqCeL1lpShaLVxkg1bxEc56JGTvmfuGMxZFzQUq6ZgZPefp9TME6kUz6zX_SHVc392Lauh4YKwSDVIxS53crQ4Q3mVX7EVs4l-L1AvBfHheqUI6GBRhHrzoalwW0uDxnoTtZ8KpPfXwJJur5fvRG6pFMrzs1ud_PkgPB6Is4w1IFl8nbuvrZLEE5vex4VdBv5oiPF8st77nEUc5_wSz54XT8sIQhyrhT65vvycHJwh8UNgsyBmIv8VQdoO0oM7gTyY29GO1mRn1qfYMzArOsDTxd7oG9ETVdLjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaGmQWVyBKFQU-i6kSmuQCmS2X-ZThUgVou49PCD5FXXEF5eMfQXOL1gMLypm2qr8npatcHv_gV2B3Mjly78WFcl1ZB4gJRZnvhLyeExJyPCCGT0gjpuRHnCf_iIXiBhz6OoCXnyRz0gAJsrNenJUARQ4AFek27zFReJjaN75JCZIRhk3Mk_ONzfZeR9p9W5NifraaV-4aArzZW4_MOfOrf6h6SWFxbAKlgs2Jr6ncoxxkLS96ZfvY8DcUXNM0N1xBva0A5GOZ4GYzYDkF1_4rIr5v8AJFma4yuamRQJjFEFqQeyBVdf6-lCfbvgwX-wXGtVGC4UIuvuegcY6at1kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpP6XH7aPAE0ZNEsD8fBZSpHJJjMgYI8ADjFkCcW9BY6hjhfjZ0Ouu1pv43bZdC_-pye8K43_yApjpTzsKzADSF6rBBKhyOhaveKa96riwOahXzenSnkdU7dixwXgpfD0BqBym0_Tj24QHDjqdtRG9s3hvZEpT-jYHpZJZzgSSQT2PgAjD87KeYrBNb9abW8D-p8jLzuI1nWPPwt5Ok9p_4soyPXI5nrclgqf3IBPSP7JfK-0u4hrqo75BjU9wEpM_q4exOk3CmYnUC27q_RwliLF11qbXqZxBTyQvcr5cNXjKBm5wYXjHpkRGk_5befgFtyvpSwW1EnV2PE5K4PHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=Ec32e6FNsD7Zf331WTT_WG49Alel-Gi9707TgZA0xKFBEPLXyW-KUe695k7A7qzX1cXH8YGwezwcSSS7qd4rlhaNozumGjdGWLhX4jzMXrhk1PpRrho8sGZDRmQL8Dr1AUkPSOMy65k0Sv47c0lsseExJ3ULdeykzJT8dbWwYiqDQY80BGf16mkkdu1rMl-gx_NR17UNtO6sduykFHLD0EG3o5og0k2_IizTcMsujCDtPWwA3yg3imhtILNcwsxfeAiJYoz9igbM1kjSew49tIvzUG-DIUsBFbr19bPxG-ACzB0VMm4-j48mQtQ9limYigq39KLyF_klTixIpvV5Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=Ec32e6FNsD7Zf331WTT_WG49Alel-Gi9707TgZA0xKFBEPLXyW-KUe695k7A7qzX1cXH8YGwezwcSSS7qd4rlhaNozumGjdGWLhX4jzMXrhk1PpRrho8sGZDRmQL8Dr1AUkPSOMy65k0Sv47c0lsseExJ3ULdeykzJT8dbWwYiqDQY80BGf16mkkdu1rMl-gx_NR17UNtO6sduykFHLD0EG3o5og0k2_IizTcMsujCDtPWwA3yg3imhtILNcwsxfeAiJYoz9igbM1kjSew49tIvzUG-DIUsBFbr19bPxG-ACzB0VMm4-j48mQtQ9limYigq39KLyF_klTixIpvV5Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=olaV8mulk9rxF_Y1jSc3qUOVgejceMxNzwABSXcQ1phOIdd9oNDVaTJKtkxBG_gf9HoG58n40xqQ3HsANKr4WZjFAXikELb6IJCl37PLrIqGTN-CBr2PzbPDN-5PzpM1e6gl24I4oBkwBVg5ovil0OmLNO1fWtKR97YD_945IzzmWbw1c0z3HpJLHho4si5HRSr_ImsyaRILHn0dxj6_FJ9T4Il4_M6vzBoQXDyl1PE8j4MEyTeAP5hskHRlMR-2yTKzAYkQhCz5cUoqbr77ii2EQeE28Rxn2EW5J778afGp1Nyg-b5OGLQavGmP2b4sLzmzVb0saHLY9obD_O10Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=olaV8mulk9rxF_Y1jSc3qUOVgejceMxNzwABSXcQ1phOIdd9oNDVaTJKtkxBG_gf9HoG58n40xqQ3HsANKr4WZjFAXikELb6IJCl37PLrIqGTN-CBr2PzbPDN-5PzpM1e6gl24I4oBkwBVg5ovil0OmLNO1fWtKR97YD_945IzzmWbw1c0z3HpJLHho4si5HRSr_ImsyaRILHn0dxj6_FJ9T4Il4_M6vzBoQXDyl1PE8j4MEyTeAP5hskHRlMR-2yTKzAYkQhCz5cUoqbr77ii2EQeE28Rxn2EW5J778afGp1Nyg-b5OGLQavGmP2b4sLzmzVb0saHLY9obD_O10Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCaeYb9fZKvfuiw6AgTzWbt0zLMe0wR1lZ5K_y6lFsG21ZVV__XmWcAT2nBxujUjhIN5K8wb2jpDlzUzzIHUozwOvnOzYth-6uleutZyH8j3s_JreSV1O1d3PUca05vufmIrfil1_tdryk4EftONB522bo6WxAxSKoz8JR-zUiD_JcM6qiWvYU6Oq46lFl_q249vP1Ron7-3JD561D1_Usq-AX6ppnwwCQbjmsQdJuwRoxfjR0zS3Y1BhNHOuul8nymP_RX6S-xqQQNEq_mpctSv-l_DjAEruzufhrXDErKheDfcPT-nI4X8KaDJ4eZk3sM78V1dXNOKm3fBm9WNVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebw4Sqq3usiw30cz-omqhEW4gFPtNPUD1dAvRQ53t5zQugq0EktmXx35qGtn9r1cgwXJQqQC_fC08rt_2p_tqhZ-QSVVrfaF72cJjd2aJeNZly9_Sgih2l4TkSO0FLczsruZVsIWgDH9w2iiypyIjcQMS98SYUpfZguDRQQbkPyIU7huHYqwRdzSm66l3VNbQ9_1CZLm_WydjBWGzKf_wwmCNxnsoBSGSifp_-4Xy3dWyQz48qymeA0kT2PMv5kwbY31Y-wxT51_60B3L02mC2enYvDGJPa2P7aMz58T3g7HA24lt1gcWNDkz-GYDwenF1txZFknr5Sqbi3CDZNdIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IprExEyb9VoxO1LBINLKtwIYn5FfYSSQGpiLXz7ghyWpYgOzaQR3KNScax6Wmqz1V9_FBAVP9HR1tAdVT7c4ii0Pg-189OQbGA-RIw4cRLnTQT38ewfy75S3axtMsILE5noBm4eRhj1S1sznf50r1Gs08Gyz6HWL5U8GLYAL9Yuas2MUzBKyLEgLSjIdN2DGafRwn5KEvqspNEMN7i9WnAstpARbumErr6IPLzpFyE_9dVu3-PuBCQpRzHZ1liZ6yiWIlymXEEKlgw81hkHra-H3ky5aWEkj3DYJ4kneG_rVuR8adtCwjpLWK9t7LZNU5-YVjX44O8akWbfHTrJu7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=kEup0tdK30XyxLQJ_218KmWkwHZSumSYANjTsNTR6tgNbq1afGkD9gHaQfQgv9CIJzhLZs0fSEYGbfqGuOHCsMyZx0WOlCZyNlavfKj0kYC_enExX1P8zYU-WfkkLhk7dQj5mKv3N4Y1OyJe0FOHIFPh8LJPfy-mmJlKNEvaxqAqWwGOxIdeHQQ7L24ciLvvBCfE7aI1cUeBmdwfnQBR7oxEy7Zw4ZyC0tAS4GB42r2WMzDYhN4gIDqdBfgcoUiHa-ApH6zW0-HmjO3a5m4TalQsbvGVXtO3xGEK39sisQTNReYqADMJ0N3ua0mS-0xAjrCYAW-v5Qcm-t3AlR8I9SKS1f6H_ufb82JQHrBlqeq91V--Cwox6DLE3yHgbfG_Xa8MFiZ2KFCk8-AaKGs-m2U3ot6WX7dnU0kgrsaOBEfYKkPsapRr3CUkUkkr216zi1z93JCdG3152oCVl8F3ME7HqzL2xUrwiJShDvk2AoUm4PiXG1vp9teuVo2ps_33g-cyaFCx3HTBd8laLHcTDh8dYN7x_UfhoWOmhnj0It5MdbxSOEys2ewjht0g2FESx-lP1-hMT4VM7aQlLXM4of3HT1sHwu2a_FXSt0o9RQuKy6rcCj5G2ojOMr1vbFSp54e_UK8na0MbJUEJAD574LiD7pVzUDGDA5UXmnSnRD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=kEup0tdK30XyxLQJ_218KmWkwHZSumSYANjTsNTR6tgNbq1afGkD9gHaQfQgv9CIJzhLZs0fSEYGbfqGuOHCsMyZx0WOlCZyNlavfKj0kYC_enExX1P8zYU-WfkkLhk7dQj5mKv3N4Y1OyJe0FOHIFPh8LJPfy-mmJlKNEvaxqAqWwGOxIdeHQQ7L24ciLvvBCfE7aI1cUeBmdwfnQBR7oxEy7Zw4ZyC0tAS4GB42r2WMzDYhN4gIDqdBfgcoUiHa-ApH6zW0-HmjO3a5m4TalQsbvGVXtO3xGEK39sisQTNReYqADMJ0N3ua0mS-0xAjrCYAW-v5Qcm-t3AlR8I9SKS1f6H_ufb82JQHrBlqeq91V--Cwox6DLE3yHgbfG_Xa8MFiZ2KFCk8-AaKGs-m2U3ot6WX7dnU0kgrsaOBEfYKkPsapRr3CUkUkkr216zi1z93JCdG3152oCVl8F3ME7HqzL2xUrwiJShDvk2AoUm4PiXG1vp9teuVo2ps_33g-cyaFCx3HTBd8laLHcTDh8dYN7x_UfhoWOmhnj0It5MdbxSOEys2ewjht0g2FESx-lP1-hMT4VM7aQlLXM4of3HT1sHwu2a_FXSt0o9RQuKy6rcCj5G2ojOMr1vbFSp54e_UK8na0MbJUEJAD574LiD7pVzUDGDA5UXmnSnRD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4BYgF9f9JU0t7Dxv5rXsqsyf76AY7tTuVyj5aV3IGCcOmrUG5VP3mGF4jJAEXQRV1rHmlBL9ZGEA2CXuOkHxBjy9PnU63NNF2aA33MuUMvB0wvtxyIV-4eFVGZhsrhQXGwAk0X7rlnNShycV2m4Vr2QSmJcnoTrZGMyPDjAyCGZnDvJHfqEBk3_pdWoKkTRmFJLr9h3ynZzIpcLkS-LuFxmVaWJZgqvkhj_IIf2FMTOM26RUvgQtCR4qtK15XPLgf_rCtWlOmbhZ8g2CTp-uMtwof8rPcsMGwOl68GTZsdbPPMfJPpdYx3QPZeylyVziyqFoIUQRV6_1lMOtcSyUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAm1FdrrCMMYd1n46sJ9GLr_cDDYPWsC2qiseghHhHF9tiTxRN9o2ojAuH9TSus-gmg9GK9pZxGodDiKLNjvW8sEOGc7QEJNTzL__MXoixRKbkTGvZY98Wm_DFg-k6wamUNRl1EtfQcpHbJWyncMArs2nv5Ks-XFZLA6n2WYyIQutbSVxGz7Fnj7CgeTCOJmTh9tR3QFDVKO2fECSSrR-q8-sCWz7DJLSDgUoPRmWnSAU-iZ-fh9sGk91rdnzedFexmOk2Xa2LSwTJYaLZsbKYMhhg61QERvrHxnrmO99nDT3yDNuq3VT6n7jEzTl8nDOFBVLbQorkPTMfwymNsPtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2lzBHkRWin-VEaJ2l8euA1bm2WazB4D8VsYQwC965LJK8kq9rMIIa4hFGc7fB0I5T3p9IOhQQNRRSQs7TIVsbSRxwJc7ZO-zHqs2O1AQlCP4Ug4_rwcpvcn3ztpqpzCtklIZ3YE6HH4486neouzSQ74BCVSKQM_KDQGbuHOSBWRbANC7dUMg_3Ebq31qpvduJZ1AfCuQ_70fnGiTjH5SuOZJRjA970N8FEUssnLyEgLtDXmGt3ZdNZFVbTnw1m2Gm82PoSc0ccgy1jEwPc3dvmqYAbj1EJgNEMPMwcxtRYFAQcLqMxrhfvEwCosTMgIOe5Qta2GC7rtIxUUYUXS5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWWGAcoKI54Aue-X3g0O6eGKCF1w1tUuf_bsZhTJqQaDZiwbUUle0SYOzqCxnfYU4vywNo8ja57mojWRxKozR0nkJq26bPAV9iJPNICBW_BFuLkbldyOEOFnsoq8xl7REWB2cBqZfdArYqd_25oCTUm9rOeHizXlooUFv8QtFQMa4d0DcXStEiZCgZXXTmqo78LvlFkgsDKxBMfmhRG0NBm2iBnmkAdp5KABWN51FHFhyzn80vto0Kfnp_cWc-YsRhsAr183_ywZ1OsDn7y2HjjdpnC_liXFZtvYoGouWZ0yTuxIpq-aVLA9laFT778lPwhngMrfkBocJb3-N3Jr7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru2ZBvxW-62DmZYjMg115TEHnaEgT2E4_4-kotWezf2hJrVBfFDdzwqPWYmv4U6pIv3V_WEQaCs9_jieLLQ5SNGqA2J2_0Eohn5xupOYhkA6RU6t34SoHgJYNswpeSg_wek1KcYoAuZQxkVarstwGWD5nf12kKg58K1POppOTPB7zXUlQG_DBldd60vLQqM5IOfhhp5692PIAz_5SvjzYLRUmYde-2mlHEvLrpTFCYTNq8MaGr1P7LsIqBDuUkQOc17DOVOHmqMgoLozVWReUBo4YYRIqYEY9erEE7DA4DbKas9uav7a0lOJOfyFrz9-3DHSqTK8mmXuYBpAOFlwAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPW7TB-LB7-oZ3GFrWNzFWnCb854VkIbhbQrHCc83fNYvLr4gPXU95gPgsQwSgwJ08YJNgTTvcLV4uu1Xm0-kyIm-01ap3ciArrHjuc8w5GBbQP5MlQUSMWoEr-l3FRjvFQSQy-7JH6iAJ-9xAwE7F6ZiBXnFNhd_1y8xrX_WOILbhTsTbUjXfe8N3yD0HfBDuc8T__kZ32JCQsxMCegT4Bd89pp072FmE-neBQYtbrQGfxts4wYCT2elTkp1S6VGtMqmsif53D3DBg0vkpt7TdZ0XwUtD8jK1w-oDEIX1WeVk5nzaOWoYNsb4q2aORsxRiGGR-kzbP2bOFlfKvjcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=nL6JVktnS0hB_zxcePW2Lwh0etxnV5Ox9IZsC_x-BQqVYVAy3JYMr-SLJSoZAlwFkdpFakUgCTMmYRAW0-XG-eTg0LdzL3Il1FWnq6Gn_5Jn9E6EFTrauB2ul2Sg4eiKooqIC3lmBbRNwPV6VmxQN_F3tmaHcYOoWc8NbCPFaK7Na4m1UKN0o2NftnrIeEonIOSlNzsS4P070i4BvlmOdAyRL2PUZ6fpYCJ6X2NfIxeKpgg6Lk3ZzyUNDWxQXf-Gx6DtOKZcpCDWlOXqwQKVEZNtZVFPCg0eolf-so4C0O6R8qp7n57XeZG6b79hLXpCR1sE6YvI5SV4x6p9qvr3kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=nL6JVktnS0hB_zxcePW2Lwh0etxnV5Ox9IZsC_x-BQqVYVAy3JYMr-SLJSoZAlwFkdpFakUgCTMmYRAW0-XG-eTg0LdzL3Il1FWnq6Gn_5Jn9E6EFTrauB2ul2Sg4eiKooqIC3lmBbRNwPV6VmxQN_F3tmaHcYOoWc8NbCPFaK7Na4m1UKN0o2NftnrIeEonIOSlNzsS4P070i4BvlmOdAyRL2PUZ6fpYCJ6X2NfIxeKpgg6Lk3ZzyUNDWxQXf-Gx6DtOKZcpCDWlOXqwQKVEZNtZVFPCg0eolf-so4C0O6R8qp7n57XeZG6b79hLXpCR1sE6YvI5SV4x6p9qvr3kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9MdupsTksa2rPsjfZloqCGhnsVpBV40D05iCKGSEPt9Dl3uHjzdVZgpYbatRW1pglXAqZC0OaxCG8_UrqYKxhq4pq00L7oPQJfy4XUaXGhwCl-RO457iCrVdUdfPSLvXDAljjouK4QKi1HeML2Ik0kbzZDUWk2s52rsPevZGI2D4ICYmBNvt3L_D61uV5j_lv2kLzgk53CJFJR9VP7aM4L4yxEOKRZzpRXPucmAl8DzdltHxYbKIvwnnMYMpYfg2XnAmM6_mMw8kYEkQKDmn01mST_nin6uhIKUPyYsZR3K0QM5xtsaQycald_Tv02qD7IYVUbWBjhEkoXBlg4j_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7liWwRp5HsuYiyVa-z3JnW_dAfwiGf45ZQRejTH8r-3ayBkXWTW2VgStdmnFNdUujakRJ1SUysUJo9GAUdbnT8eH52TbAumMFk3a84Iz-_1Kjy1v4apwhWNGhj83yI-2bxdem3A7xc07XU7tY17Nh1W4601YLY506szygg2n9wsgiDNofD3V8t1bNdjvQuXVtqPwJzlcnX20pItYClqb2-3j4WFB1YVUbNIFwV83Ttu9ni2uCuM0iflJKLMJMqwY-pkoIGVqiYON1bTU_XCpfgDeN2j2qrDioVnQJRbzQeyuc5qYXN6Osu0mVHNa00j2sYX2Smw4DHu7L5gs5OQHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n__oyVdLRs6BRx8vQXENyQ7T2vvDl-_Er_7EZ-lfH0Qn8rUqitb8J7yi5PDQ7iPTtYvwKSkizKyXlO67HikxB_L6uGz5t0BdNMwVl1zpZwwCllXgggq07_5rrPMvadvSFvSxK9-0Yv_ypcg2AwGvNpNzYzuxRDG622bXPTUFmpWMjaanE7uqUtEECPBybLlTDW0c1JGXUjK6XYFjVk7Lsh8YW4igPUOb5aRMXc8JWC7gwR2ovRPkdmGCYlSZiplznrMnqrN7o_2XhNfvUq-I_HnhQN4jyMYpTEu0AlWk_J9pjARDyhlH4tvuEelnquuxmglkYLPXk4ENj21LIvw6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uozpVTJcq80Nofurb747orPoz6-uu4Lgun0RM55WL6Wh1syCMGqb9GX9HWBaJpNv_9w19CizblfC7hxz1Uz7nVZ41nNYxyS8MolhVuHWlyOhKPNjcNkzAyjWZogeVYMhO4g6DA_ynBE6JM3IAwMGWJurmWUpHo0rnCmGNHSEsiFY-rk5N4GxzUiI6_oTBbK7f5hlRo5E2Au1xdUoc_e2w6kYmPLPFkelZ51Bs4rjLytQjlvxrorJyieXC9Jn3tR4YM0wHOCwi2c3xbbwCHFDKIS6YfxZ6m-6UCAlyr5yUAfP-qd6l8NOcpvG0LXzokAn_k1APTDqEhmo-hjRlbTfUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEyNq51ToEBHLb4A7qftL1WjMyL4yXmy4QzN7nWtyDJiKNzoc0XE0JNpjX5lhThp5PU2QvK_BBbaFYRPs_PI7lmqK4o7TAD4M24bYnyd_cSPC8kMmbjhNE-W_ks8WGR7_A-pvYrY9QY_oeSkXPtpCvwPI2nf_B0nmmU2l3shNdextFrheZfidyE6Pk7hur60ggiJbW-cMhGKEEJrUU3ME1Tsw-ilngPcz2tLP28FVszELzIo2nHOOM0V0x9JPXzWqUdzG78lwh0TrqOpyXSXe9_pSMPd-pRLurjPZBvgQj1kiCPrzjMNhQr0UR1KdbQ3Vg4Wc91F1YtzVqhDdmqhkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8DUClg6jgTKssVIoLS0TqFPvHyq9t0dvmBAMbazAeYTSq1UuQc9qfZ7faobSZFXV_HPBCknCEIl3x3Z4ur2DapbUg6KIBFplX_2rNxBuLFrQnjA4yT1QX7SxOfp_LdMgYECYoMqau0v1A0L8HsJFvIx9iN6ze-e0FShJkxO_e7Rf2pqAORnBhIfN5POzxSEGfVPsgpkD7db8RcxiFFc_xuq_1sgH8LGgYReCjsz3POi7-d_-E2QiRPowUy62iJ9oUT1upByavKKWJ7DIbY__dVl3QIfQBifQvdpvpekZa7kmPh7ED7nIlSwdghuoRCsdSaUN6UlyCs_ibkWMhPOdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMuCwjFNq8kEClIDXPwVUSNs5g0jIUFQ-TFaOu3q7VoWi0elwivUEXHoNdMhbawYUFeR5ii70xzJRYOABTooWhKsOYjnvP9HMnZorXZylisehhWDRciLczqvkZo0lLpfO5E5o9FPOlqc8vmC4vplHsZ9v3NIRxGRfkklIM748viIj8VmVe1QJXVTPld41lgIUfMZPuv_fvXQ7sR4WFw1DCL0Ff8MbfdRtq4_3Atokal4SDpqxnywhxSajkbv3gwVT8U9vOJ8GBmYN0_prGF4a9fHLhMPPgZNkYyQP45e60Ui1h65o0sK-vXyJqsgrfntga1mS3mHh3OgKNej48Ozog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR-gCUkwWSg8Kg2s7xckjzCzzQ_fHEaXe3tCfrmQmQBY2p14wlR0E6Gbz2O0zTtcyJLxhalomabOL_bRb8vJrs--SV9T9_hxx5eNwGmpGVNwlglFrfx8yD2tXEfgXWAX_XMqKErsdetJf8Cx66HvHht7F71SKZLLaX98BnkQ7H_vMS5LMkkUy0fHsHvSaUsVd4UDy1C_OvY9v-L6UuBVoyHxMGF9MUyorl_B-pM5uPdzV6EURNkI9ZNskdeZEhmsnewC471P_SdXur9tFd1xBuQZqzeWNz_AI2YrvFfztut7Ly632ijjQQyS7HT3hIY4Eja4bZQua1dvwumO2SXDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlNnUstQrSRJmcH9T5vAOwhtojnqC-tqW-T05pX5AGZ16hFT3L6IVyja1DPhTTyGZCTTkJw46s_b7Bdu0jPsd66CKdzvU7yIDls0-ac9p-_8XFoGw3FApuv7Bq_JGsKAAtPts0Dtok3OCT50eO0GjQ_XHPFs14EgxcCw6-gKHgeGN07cOLyHRZAeKRT7cjZvDNd4KlYTpv2aYza1hVvMYgKnQinTPlLErfNJdDKx12jTumT7EmQtr5uusC7AIXCSzsfip_k4QFevzvXBOExFDrdV_fyWDwwfZTGPUO7X_QukyZPfgpIyDMEg8G_wOpsygP_3zu5hFcnwqHeZ9e-Olg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=DUV2gCKcJcyEad82z9B58nwKJ0fbi9thVM3GhRFaL6Aa9sEBWhHlDDRLfUdS3I3d0LMblpbZMG2a4RtdAxSrwJs2u_pThhD-Ev6gqnX7g_sFn3ejYovRPyEa6Ejj-T1OqPJXLnsknrYKqp_32qiMiqZRDdLgwfc13Ur9UxrDqf26aUNEnQhWmYQ3hrgk5yojnV7QxClA0KAcQUR6q9YUFMybj7i540vNqssg2rrMv4kvekUkocVsPjk6emigRwS-i0PyoVrRRvMxPthNlNGggdrmNbPh1VceD3I7G6aTLUq3xZkBTk-j8Vv3M10Hcb3SjEhmOhao1PGQfamAYzpkv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=DUV2gCKcJcyEad82z9B58nwKJ0fbi9thVM3GhRFaL6Aa9sEBWhHlDDRLfUdS3I3d0LMblpbZMG2a4RtdAxSrwJs2u_pThhD-Ev6gqnX7g_sFn3ejYovRPyEa6Ejj-T1OqPJXLnsknrYKqp_32qiMiqZRDdLgwfc13Ur9UxrDqf26aUNEnQhWmYQ3hrgk5yojnV7QxClA0KAcQUR6q9YUFMybj7i540vNqssg2rrMv4kvekUkocVsPjk6emigRwS-i0PyoVrRRvMxPthNlNGggdrmNbPh1VceD3I7G6aTLUq3xZkBTk-j8Vv3M10Hcb3SjEhmOhao1PGQfamAYzpkv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suVhZFyyy7NuYQtK3EYIk74s1pUCtrRIy0idq0vH8XifDZolEE4F2A3cdeB22Cu-yFxroe6yMN0u_BnHE3dEpjxZ5X1LIVpOjZuWeYAvN37EWk6zxX43VIGT7NKwtjqiH5PyB2npX6YEwj6iGyxj8NM5TS8-RssJx6Repe29KBtH8rxP9ViczCxuWl_v_BI7C95fnDs0Rm0JhGbQ-0E6VQ_XS6sF6jLXtS6x83Mh7zh4AAJcsAb6_5hP8Eexs_VPnbLFBv3WnsAf6X7QZRM8yyp8aGaiXKLribdAHFjlSW9W5H-Y2p3qk61Rmdr5H4S5w958It3BmE-ZCXOYcOHcng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB96pWgCzrJG7L7_JyqgCcJKFkCp3rQi9nGv5Zp3ZpatOf0c3k9jWAuAZ_F1stT8pdTs5_1wKrp3niIPFkJd56PAOuGg79qkpbXjfZL9pJPzHAnlrYoxZCarLIXRIxPrbruZjBU6qc9Nl-vr-W1PJrVrwcjjpMbKAqxbtjnfbz3-wb7gfFN0tGpL7cwJo0DyWN2H_bluslLv3AdfxkKGPs4Erw1SjRkZHO45_Zmq4ygUiLeJbq8a_6ypR-7aEptcLRxLI-tPaUrav6hQaFqWEYgn52cUgudxqWEdjMlg31rsE9mbSLlSr4cHvvZ7Y7Xf4AkRZbxbOGGTvBUx2y83kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzlBx5u_-L8gwvz2iATaxsF9LRd0XzytBZPnUeB9FGo7zgmRVDu-s-RxGXybota5qrXZ-6Lvx57XFA-XH1RJc4p0NXOU9P1he_8sSUW5MAs15beHQfpT4k6DhH33Em-MQzzf-q-sgl0ENP5819XTJDKujzSq2T_LC--xmMBk6vPzhxXMvxfpuwYgqcl6emX-yZB1vKFUoWK3ePIYw2Qn9lcVfLMNKuZ5oqSLnJ0N9es2bvhpojX_jDrGTBDdZdqKl9JNMFPMDr25_LbAXoS3RzUAahSyJaDh83oKwt7T2hChg1r4mGPUgl10VFXa7H7qzoK4wF5B3ozqBV96y6ecig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpjERTrjyZ2v9U-8-Gqz9PhtdEoK5--5nDmMnUldAaJE0IHWoRFSv-2BFJZi-fC2cAYaCxLlaTasZLXwethL7UMv62SYMn6GwwRRAEyxD4ea2Yaa62x9Dgc7E-Knr5nH5nUWMSTbvAENSzpyLCWkyZdLxFA5c2wU1uLMSCS05oWud-O1zpErgkyxGPSXy5EU2H5LUbV5jOpOhQmCRti_FiwYmF-rppFA7FVRPscC6-_NVuvGV_SE_jOe9u9o7wvHXemzQTL-Q118YSYzQYZbkyXAGSKNhZblXlhAxjfYQJUbxZWhZ8SLvHMYwQGU6VJKB7pFNg5JNnyg13KG-G_WIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=YKlrt0VUdcGq1D5rLSzYlThaSMs-D1R6225vbrvfzzpAQdToS2YpcIiyCkhYFmy3SwxMgZebeuF_IEPYWLp89ylF8cpNYqoQEyeJSqGhenm9_8SK9ppuD4SeIYCJTUF_7Wu6tdtWwuIDvTXd82N8IVgBCLDh4JTTrgIxtHGn39kPtokHw0gzLOkLA4bd0PiKOMI0wOmxbflEQ9mn6PAamVIPMPrQHHkB60krKGEjU97qZ-6X78GmDx62Z0tv3WAo1ZPh0TSPAir2M2Jdk8VUFd7rvAFDM8wdDyhbfZPonxE0K6jdO88UZnsGCHyysAUN-tGVS9i9OvBePiqPKyV9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=YKlrt0VUdcGq1D5rLSzYlThaSMs-D1R6225vbrvfzzpAQdToS2YpcIiyCkhYFmy3SwxMgZebeuF_IEPYWLp89ylF8cpNYqoQEyeJSqGhenm9_8SK9ppuD4SeIYCJTUF_7Wu6tdtWwuIDvTXd82N8IVgBCLDh4JTTrgIxtHGn39kPtokHw0gzLOkLA4bd0PiKOMI0wOmxbflEQ9mn6PAamVIPMPrQHHkB60krKGEjU97qZ-6X78GmDx62Z0tv3WAo1ZPh0TSPAir2M2Jdk8VUFd7rvAFDM8wdDyhbfZPonxE0K6jdO88UZnsGCHyysAUN-tGVS9i9OvBePiqPKyV9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZPdkwca4B-U5SdkpvzgDd8WvtlF5BN5NMI6NB79-3sAQBGKFHbylFKK10j4Ds_5L6F0tLXjOsqWkvbUP9QhGfemhLOD0mqBZ82dEw2N2OWQqI_wwlqC_7vA7gxSjLmljTu-QpU-bl-lHiJfKOa6ABZEKeOvYKfFwMIVP6MB2IbsyZqpIXKGENKabf3uX5jddxqOp5N3tgadCcDyGj9zg2IaYeIxlrhWMk71gD4Z0DSfXoA5EP4ykVUTID_fE6VetLkjd_zex3DY1FoV7LIKgcmbqn4p-HbAkYbBVy6eeI2LsM7rrk9K48krQtnBNGN5K7-9TJi-_gtkTtI-OywkAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=dTUlHZydqtMiF-MCE6H7DqTMQmdfIVPfb_WBWU29k3nYF9bh2kfFs93zTbdnfd8xVlDr5WYs-OHAj8arP24Ev4rZ8PxleF98xC0K078ePS9xsMMJ6RuO-91_nD1JbBYWndNSGC7y9KEn9c018kWrQI23jPYttP5YF4EynRmfIC4dxu1iaqNti7AqBC5B_oX0Sx5atOoNSbLHmUsMUfaQKdrkGuzh3KXzSl125aI3myN48_6HbmIFIZq-gp_oLxOWYrO2o4-as1prdkJjmRmZr9whlupHKkgGGwemw_LE8BEvmHIhO1o7NVhLt3D1fkby1vw6sjydBzr2-P5GLFt3Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=dTUlHZydqtMiF-MCE6H7DqTMQmdfIVPfb_WBWU29k3nYF9bh2kfFs93zTbdnfd8xVlDr5WYs-OHAj8arP24Ev4rZ8PxleF98xC0K078ePS9xsMMJ6RuO-91_nD1JbBYWndNSGC7y9KEn9c018kWrQI23jPYttP5YF4EynRmfIC4dxu1iaqNti7AqBC5B_oX0Sx5atOoNSbLHmUsMUfaQKdrkGuzh3KXzSl125aI3myN48_6HbmIFIZq-gp_oLxOWYrO2o4-as1prdkJjmRmZr9whlupHKkgGGwemw_LE8BEvmHIhO1o7NVhLt3D1fkby1vw6sjydBzr2-P5GLFt3Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqI5czXVKaHLz8gerPNMnhyo_4RZMi4EzjWAdkS9_HRNX3ge-HA8VO6lblYGjemE1J8G_kWxpFb55DOO58MFK6OjUKwi56or_n2J42fQptz2RZsHMfrGopYQCQ5_QtYFpx3zRd4gH6XeOK3OiiWHYQbeK4XsKNsqOprVWM7Bg5Ke91zEpF3bfTE97vBqEVaoUWtocBGTpiu7QdoflUfJdWiPfoqYTe1IKLYhXWpmQtT80E83sszJ3C8lxJmJq6gQLsHKlCzwEKuEj9kvOKH68H-P6zJlJcWQmRfCw8_8MB6oDlfLuQjlacOZ895i0k-gBuhmlaa7H9SZipqdAuibnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISbtQz2AwLxppC3nEYGr3vI_7FNkVJPdAIXMAtXR2vgPkzncKdXI9DuS3yi-wsnlp4KPvTTx2pSdAC5UoDBBm_UkOkEnvaGUt1Hg4GroChB_03eG3LcUIDsx-VE1UFcyEeU2-Zoqa_zMEnO5chSISUJ8MA2t4wTpKNXi3kKU2kR1iu0UNF5M9UW2oSN56LN9ZAp2Gw6PJfohupeavENL3x63CaDCTZojdhbl2OI1e30aOtAHYrlPY7oIh1Z23fhrQxsVvGnIR_48XPhwiV78gV5RfoJV-fIZaPiUEu6zRVUy13M3OE8VK4WlxbvOt8CayJBNt-aD4az1TSd3uvKGtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=phXMTzWVvVJOpgO094Q_IGXDABgV0iKyaI9M0GM3LX6y_Uf9AWIdusAazAzCQzqpsLJxPwOF-NmETFouh9E75U6V2oegemzZFjdH8pDBpHMqvLKIKHg50DfAIBykB8s6aWV22x74BxOGS0eUIwjujwdf7NAJ_qagWWGJ_QN6CrR3jTNoH21yLkSpVdqQvBuAakCv0P6pq8IpHcVcNJCgvjvFHCP_WnlX2nUW5i2swCnoR6ahDxHVaYalltA5DOEghoApY8La6ykbd868PW3V58MVqLMc9Ne2oYZ89gcIHULVmXh0Zv-BZDwK5_C67ftME6Ppd2BZUR3mKYi8h_tzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=phXMTzWVvVJOpgO094Q_IGXDABgV0iKyaI9M0GM3LX6y_Uf9AWIdusAazAzCQzqpsLJxPwOF-NmETFouh9E75U6V2oegemzZFjdH8pDBpHMqvLKIKHg50DfAIBykB8s6aWV22x74BxOGS0eUIwjujwdf7NAJ_qagWWGJ_QN6CrR3jTNoH21yLkSpVdqQvBuAakCv0P6pq8IpHcVcNJCgvjvFHCP_WnlX2nUW5i2swCnoR6ahDxHVaYalltA5DOEghoApY8La6ykbd868PW3V58MVqLMc9Ne2oYZ89gcIHULVmXh0Zv-BZDwK5_C67ftME6Ppd2BZUR3mKYi8h_tzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XablOk1N5pFOOqUaE_dhDLs0EdiH7xlKo3B5tV4NVIlLqUI89qSKoQwVZebRvKfQeWQz4KIb68jMVj949aQh1U_vnUL01AfM0gFNnzf-Cr-vh52yJWsgNGg83IB_ZFEsLfWeFauGfIP87dhV2x5FHHPTO0Dm706w6B8ZupqeW22hK9jZBMeiJ-Uxr9m6uMQsMPLCEjx2K6toio0QW960KDv23w9PihOUPdeXw6qLTSB5dVCPRAyLPUzHjeV-yJcOrIUKwEet7-viHmbOxlqCTT_0FmQjeVy7-eyUuCDjgZHh6yBbggfw0oPK6xS46aPN1Uq61yvVLie6FDDDhUma_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_jlpJh4Fi1qxSKrS_4EDGcA4A5d6C41ELi4H-ktRD0GA1k-djT54uBVqqRDV3x8RlEDWjkUgDSbzsKEAWXsijQqLxvylVpiE_3YMHFyQjm9-TmCaani_SH79OD8PJFEnGaPOVBlcILJZ_9cSk6Tv-ZjfiN_IBoIXyNRcMxc1B0W7zAtqNBE83VxmeWny_h8AEDbv7wHMrI3mfnHkTcUMXKpHfqhPqaMoYyJ9P88GNvAN-OIglZUWp-XZ0llsA4BBvSh44-wAxIcsO_BWrqLfx1NBXZBmcKMwzZkNfNGftU27uUkDPjlUXfvOHOnXtBnS9dTSplXgZNQY2w97LPVFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=bDzXE5JAjvAcgsWEXH_fzcp2QZM8U7E-cssQtAJo2F15FxCIKrd1L_gud7afpIEdziMS-VOJX_hqM8CrrjhWcioYr5gZqVgXBj_p2lRDCi-f5jScWWzN8KX63yl_IlQGb4Ilmdgl1PxhOlnWFojH5OAW76ryYsxkeTBRLqYAVu6Kv295rMVqtEnxeuCJn_nLWS8Ff9PsEfU1pCZZPXafP1jfnwe3oBp2eDlePlbOI6qYtyH2KfKPqBryzgWDTQiIzRzeFe4fY1wIJ4M_29DuMNzJqCKZFWIvMBmQbhGy-vwzqieoVWO3Xq-9j5WofEjlNoIAVcsQWFXL15KmMFGURA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=bDzXE5JAjvAcgsWEXH_fzcp2QZM8U7E-cssQtAJo2F15FxCIKrd1L_gud7afpIEdziMS-VOJX_hqM8CrrjhWcioYr5gZqVgXBj_p2lRDCi-f5jScWWzN8KX63yl_IlQGb4Ilmdgl1PxhOlnWFojH5OAW76ryYsxkeTBRLqYAVu6Kv295rMVqtEnxeuCJn_nLWS8Ff9PsEfU1pCZZPXafP1jfnwe3oBp2eDlePlbOI6qYtyH2KfKPqBryzgWDTQiIzRzeFe4fY1wIJ4M_29DuMNzJqCKZFWIvMBmQbhGy-vwzqieoVWO3Xq-9j5WofEjlNoIAVcsQWFXL15KmMFGURA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKIqUMzgB1FuS9l1t4GtZCxo8kqDFtV8IaaUNJ8C2YrA9QWo0Uz8iLnc_WG8iK-TZ67AsMhZYLyNL53U9GvvSfRm2Yzd6SsjGVuOkfz40gLhylDsksXKJew7CnmktO0DAMYipGrnx7j0jG92TUsgmQR1pWiZK4OOjKA8pDlYRbJknURkCQ8l9P2S2kBDvaNpieYb07KxlyV5vFM3wooiVyZMcPev-RlM60xxHEGFAeUyq-Qd4rirYJbHlRz6-3c4e3qhAslRYOPxHgAD3QvR_78jpBRaQI1vAZ7ODVB_FLs8dTkuQ34GfNoBeenRCdW_rC6xQ96aq5HOcwqWSj0VPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkZy140pAA-qJslXLJd81JabsEPSF2ONtR07HEdNTBVpxlAu90MiI3B9ytYXI6fhJUZ0mBxtEqFqPuh2yJaOKNNhmlR910z68YMUlsygOcggEW-FhCo9yD9OWeNzSQXQDlHTHtTPpV5UK-coLu1z1re2FAfoTeTUgKZBuoJb09CzB41yz35IL5PjL_1LxjEzgsTD3waFJ2rCmDSEIXaygDnWgajT4pZgPjUPgxU84Wr1EMH-6RRL0sIp2OR15VrhA6yN0R85Ur7TJE7MSqbuoUcII1mSKEl0eC8A4aMia-mm5ckT6ciwhaTlHd7TXDpGqFzUSPfRd6HPvx4v-BY2YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZwq-5F1vrsXMgDjxyCayDqJnM-_VCgu-kU1qbsIcUiKkHdjbcZRlOIjW1dYXNMY54xYLXquoYS5PSm_Jord3rvDN_7g6yh73fzrUE2h3CuYu3bdZrxTqZ5qUwrp4XYWTKtZws3UHLKu7c_t7imgNakDJ5I91daF9LP3bOXz2LtHRcP88Y0k89UZjn-acgAThC7Kvlvr4rb9W_6XB0IZ5JL4L3zw7SS5I99ugGF2srljxokVMjhanps4SzL3RzbwAlD95Dcg4BW2DHy4P1U_ONTndNqs96ZgCDtUG5ELcIIMQJB0VlDswYUBAB5OauLu06JnRmeaV9BZdSpSp6kTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFOJ3BrXXlnIqiJbJ8RmfRFjUBjothWLVE4-nQiysBvkczbju5lPvIpzOqb22QkOJhJ8fjaEmPTZMrVaAbDhvN9DN3xGsZbeidPoZDnbyHoijuDfzq_gvR_Lfo5A1Bs6Vs-UCG4a8RvB2NqqQ6ImHlgqFj0N6bU0Z94mvZbfZmZXwV-SUVEcuI3NsFXAEFvlinSCXr0Lf5vKpCiugdFtyFaUzZv45CRetHVvEMGPk0TCZnb5ami6L9UgG_sg5qm2imCXUOcshNUMK9rugt59Fw75c6bVqM9199mJR41L1GYlvAfjOo_a8t-oTYvGRmD7_pS0xW7hxYcsoZ2AIrZyXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNrx6-2CHs4ExAFvB0etljZ_Gie6_snWeYJ12QVuer1OtritKJl4Nns9CJCw-IHXrbU8yh3sCxSUS9Yq4sRv5YdovtWBf7A9qpRhDvVQbgG5sbRBFRrPPALlfeExurHnvZaDPaIx0QZ7xT63-5qLdk_Dl44Pf93YQUzBC4mmvbPolcKxsYdQo1RTuaEgXSm0Rbdsqlg9DUHsaRC76E4NSsn4rPeXYuOfcTatLPWFXjvpkm4JRthuLopTAktoCGHjAyu8VFMi0dvCYcuK7r9pFTzJea-a9uqRtPeiFixRUV1p8jzyDYM3p9rCPVdbbb7E3jay8EpfNj6Oy51KLClRfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzmDRlzk6GCUUyQhXraN8mwuO8mtVzb2TYIfxyeDUjk3x9TUE819-Pss2CYcLwPfSdvrfD3yZXH2fqUWjTZoKArogMYU1FhhvSmQvw4ZkmY7UV1tuAldX4AuwmpeZXOuSe6KKy80kULk-6NPbUR7bclpQ4XRz588nQ5EGSTAaWfn3Yfkk5yZxDV9mf-Xwb9abTU1S9vc8oRt6mmBuF2ZK1QbUjo0VEtF71caGrP-rRemS_4CFYIFJnt7d4eQWphZx_xQ5768mDA93tpDmthhBD5hMuyXBiECFKg7yTIGiuLqpqWxFG0teEtrAdPsGa-X7xXCnQhrAkCv1WOAVF8jrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv5BXEKl2_mqV8AT7PpBy-6Z3DhXKBW3VnwHQDjGmskEpXRwdutdRcsD8Eew7yKh1eA9837u90Snq0KKVhvBEFkQICT5jZFdURCvMZpXuS3xNxzqtgYTMbyenW9q03EQ6_k9dKOm4AtK3HcC8vpwVdudRlt_1uEJradRAIxFT43T5ta9tfGk8_mN3rpi72QtKh8n63LSWpBJWk_QlouePz_ztpiPAguG7mEQ_Rjc9qqLY_q4dcNWNMyN9csLk9N5cmr-e8bLGzzymJZq0RwNFedc63a83jlLw-fqnUNgD0B7HXmau1o2YBE90X7FkvhaZrx2RwLFaJkNVawbVohVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qac6uhnopRy09LUu2SZcB-54KGwEfbkWsgjFpOQi6_HnxX69OMfuHrjr67-RWRkv4kWGecwDfA31pqI8DOpYliPHYvmp98x4WXMhmG8Bpb3VWUfj_ZfJYKZIxnT_wCZ4Z5zBZISPWbaHM08jX7l_W3PjFsmfwdgZZNsyOny1zT3DVNDA_Sp_vf-WAcwrhIKg_wC8ewK7MqaffRWgZjA-NlV5eKnCwhJ-U3YfVl6GVPx5uddytbqaP3g7-xOK3ySbkzCber_o2fNL5JO_dap3Em4s9K6wBP-EdzPYd0mRd9PYrfYadbQvz6fMEMNiGJkuOUVHRqsTSY_kkGOf9WSe0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW-lHZ-HMAH_QtEYX39EOO3UskDJrOu9rdO81Jb1E1kwhcBlAMF45MInLCRa84XIX0jAqnTvQJ-ozD2NEvz3GYnavVeZjdtYITu3RyFOWEH2e28pDleHSWVmUVnUVEZhQTduo495NzRXgUOnuHZ5-OTi8P_PQA5s5x_5HFV8DX-1xhuBSdMFa8xTJnl3P77AzEEJi3uK8uH-BLjetjIohElsXKyyLSNOrUyvhjo5jj1QR6Wwowh0cdrHod3D30hmYJ18YDTg50CbJ8zBbAEjASx0ANmf5WipTMXfSS0NJsKuAVfQQKHku42luRA0BZm6AjAGQR3QT8w9qLSIWp2v9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INi0-bH5VxWqY_w80HkAkO88ZYpS1wUviWszNYYankRr7qSym70LlaSTmpYPSpzCxd8yL3jps-f1AltYsvl1KmfdEzi0nKaITUWFmuGgsQZZfR3Xvq9GjkMc5yl7dRYm5jwXBXnLMjeRdBHQgQMxConUGLqVwItT9eyxsaw5Vb4SYmo3NpRvWC_M8lsd24InP4u9JI9jwi0fufD_yfTAtF19TEZDyhg9uFpjjouzz4Mau1TeGOdKfEl3fXO07Uz_jlXwW-VcYVotstH_oNaMGr7sUO1E6wIrzpynHP6qAuDE_AA31bnYQwOsqT06d6KnSkQkRi0qPxdY5us5LBTA3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN8hapXr49VarfYT3gEKJmMag2box66p4ANXd5Cm_6jAdlWww51cw6nU8CQIcmKD-9eDeMCtWVo8lYfB2GwwMBgcV6oCm4E6ZEqFGmF89x4ru79EViycE8uVA407Bry4UrVT2Zt5t8KCFhQqZ4bD9kITLZhQAWnC1jbpi0sYB7FFuqntxKnKuIzB91zQCHwiQs78jUwOezW6l2VmYblNMAD9pnQxpwF9l7RCx4I6exVWfAY7KwmTPBdh-Cn8WYMiLCSV71EznpnPQ7bX9ytJFbbGQH8PotjoA8RlwVAlFuhlJ8Jz7NfctGsqHF3aGFmbrlciyFDIHMzcu1mtAKiqXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK36G2nCJ2Ivuau0kMsPrg8bQNcr4DvnrDwTHaygeLPKEqeyByooeuxieLf8cSknjoMy7Q2tMG1Diuf_nprhxZI82UE9osO2I1eBNHFTUs6hEOPfZ-a9Kuy2nNNmDWCSTyNsZYWdHlnQukmJ-GCmhEbg5Zv3i-HL0rr7G8JESq8rcmL03wp28MS02qSfEbfJF_tnzVtdKiAndgjiMT3KAYAUntZdz7aUnuoUHezpNF3l5cv5J8sbkgiqupk7yuFRCknz5IZTZB-z2NMIICHHKt_hzx22dQ0MPZz493WHU8Hom9msgj87Rlphg_7sIBucpY9yXYvOasu3wkSudgpcvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRUT5zHBFfB03OY0rw29zw42zx51ACnLJNmEF5GgsChJQ5xh-qJXZVd-98H8DVshay2IK9iuUjHcMcZIGISQVg8PlSX2dUGLzPNXbv5JiSTiQVhlQ6qyMdjWK62Scefxq5RGJCfvkww3HqCSoLv7Z-l7GUjMRoG-Ybn1IJvYrUZP0JCSTjUJVfwo3fhIpfL_gJJAm2my7j_hQiyQi6DaDwXWJ7v8-EV1HwlS3gw1hI7WDq_pXSggGioDuTq7ZAf0-ttNoArhO-H98YRaULNMRLAnoHb7mVu3hx56SJ1ho9_owIdjeQMfpnoV0iIitBUrrQQtZ2Yz1CoRC7rddhiJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
