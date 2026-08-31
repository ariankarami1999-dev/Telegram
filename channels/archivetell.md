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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn_3tvm7FrfO-09YwsW28aVmO37voQYa3QH0EeF9Umdb0nG-uGhB8lyHYN3bzawQuFc8GdUPc2lq1hFStpihgRrrCC1ukP4OG1uYTyrXQaV2lNZ1MRN1h77RGobwYfaKpAXbl334MokkAeig-NKtlBPIwO1xz7ek9hjZ_H5yZ7B85G5vtvKYtpyeLDtO7lNsaym2I_dqhYDGQfRwd-e_vs0LaZd6Rlo9tv0djf5HDm2nJdHGc7LVRceOqu705oQK9qa7ODuCVWuPLntQiFVdzgNsYJuYBS3-a5xOQHKCKntOIrxy8GjO4UMOdM7yYoheUHLwF8eeeznI_X1slN3tHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCizcKlYkVLdLYTkqpB9F3XBcOTVkjl3x2xzzqb5eDVmO9qa2kaECzz32waa02FxHlyULFBtmXkkckwp5LxawTdJY7Qq1JPUIDDAqKwOUIkF0fwA50HxhcPEGirNUVE44JJ2Wg0L-7wlfVeghQwDz5MxOMk-Nu4ZLizDAg73oOWtGgUQf9KmiQml_EyLrtDhR5f78Bu7F1TCk33-7NGDtv7_iBWKAXw0z9nqHomBEvF79H4JgDG8w2578opK-I_sDoCZO7FUcwEviag7ps5qCmFQwpe1bffTtRfQUVzVVi9S3jPlR1wsSgpVNtTVk9DfdJjHXs70FKbWwhKnAHqLBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxI-ctCbf3NFPWhWwOOA9CQlPmDk027_ZR4RpM7JBlqGrho-p0v26XF_g81ApOKyOFu92LmDhdoEllGICHfCC7yOVK6Fr8ul3BUlxyV_FrJA5h8xy09oqoitSMAoLsuzarb-rpPO-cPo145MjEKzajeTGFX9_mbBtyTckYm7XQiuNr2uLNvofrWRCNvu7xvROdRQMVuAfDfOGjoERChRJ4qjF87KPahq3Sxa0APJoiA9l0cUSPOQmUEDXCF1OWODBEmUqJ4oYBTTrV409zho2eOVl7m6o0Y4Lrq0Zh-BaJdOiCVvYfJ76Fkq6OVyPg3vk7pUitWOwnreNP0yErhuhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzS_D9Cdy229LE0peGijACqOw2WrsFB1p1ypCqCfEn92EZQqkPaPl89AzTaj2jIM-rguvv9y_ckPaxJzWaBRPakrU916pNsw2-lh98ABVd-iln8Oz0rg4zBlGgisxiTlxgAD5RgbD0BGIcqEMSrMG8okF3X_nlEmUyTkAHOkMPW9PMCg8YpuxEq9SYHYYQgk9XuFwegSuBCeyI0P-BYtIE2YZj68yojAD8UVoCgMj4vjeGZVQIZcRUJOLoWlMJopRNx9ne7Iigb0rWLI5cqfZL1sow8gJPqFtsG11aRLcvjf1zeIC6NSTmGewjdW9gBituke_szSMKbYGMyBWxeAow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=IuzY1CMN5pMBWtrcoo2swBKeTaNAfEyBkv4_PmCOScExddcsqC-48ejEFEUUH4GgN4hM9yoz0ARXidm3JIEv9ScqoAK0h_QeneunFac335FEhftppLqtUUkTKKc7HbpdOvU2EPwKI3oBaJwn6mAgAe_PS-tpH8E2Vy_88nirUmAfPDSoCc23n2MxY4FW5M1Lb_SmBzqaKuD1VOGJEhmC_T1D9X4TpCE-_v9dTsJrzHyGsV6YRpp5xTM36vHdGgcFs9_FpMhRfoZd-hn0L3K7Q__V5-TJLAvwF792hiSkMiRYUE8EGVlyYBPOjFCPqnMyM1DR8lZvCL4bAzB2dPnT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=IuzY1CMN5pMBWtrcoo2swBKeTaNAfEyBkv4_PmCOScExddcsqC-48ejEFEUUH4GgN4hM9yoz0ARXidm3JIEv9ScqoAK0h_QeneunFac335FEhftppLqtUUkTKKc7HbpdOvU2EPwKI3oBaJwn6mAgAe_PS-tpH8E2Vy_88nirUmAfPDSoCc23n2MxY4FW5M1Lb_SmBzqaKuD1VOGJEhmC_T1D9X4TpCE-_v9dTsJrzHyGsV6YRpp5xTM36vHdGgcFs9_FpMhRfoZd-hn0L3K7Q__V5-TJLAvwF792hiSkMiRYUE8EGVlyYBPOjFCPqnMyM1DR8lZvCL4bAzB2dPnT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=L1NNB-C2Cb65RNHzjqIlEA01Ggtip40k9HIaXSdz1G_YkhTb_G8AwZiUw3UouTj3JeAuItFru7T5DW3z3Gzcga-l_miCQ6q5GIef7jqJVtCM_lXO5eA2E5eMxpdw5mUW6FDK3ybQ7O3p03zuT6oREgYCUkUuiZZREMj-V3-v66v_lI_QRGpBtMvWsFBfhAe5LCUhfhbnnNR_ULvhsDDGKh8BKHuCc_7f4KYzK6kZVPwXbN-hdPaoypdB8jPHXrFNL_0xgOpzf46NDjhkUtZpHM9w5RO0gI77awqwbaFnlNDTatviWtPMCh2e90mjlvWt8PgTQ0aQsbSzKCn2RN6HmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=L1NNB-C2Cb65RNHzjqIlEA01Ggtip40k9HIaXSdz1G_YkhTb_G8AwZiUw3UouTj3JeAuItFru7T5DW3z3Gzcga-l_miCQ6q5GIef7jqJVtCM_lXO5eA2E5eMxpdw5mUW6FDK3ybQ7O3p03zuT6oREgYCUkUuiZZREMj-V3-v66v_lI_QRGpBtMvWsFBfhAe5LCUhfhbnnNR_ULvhsDDGKh8BKHuCc_7f4KYzK6kZVPwXbN-hdPaoypdB8jPHXrFNL_0xgOpzf46NDjhkUtZpHM9w5RO0gI77awqwbaFnlNDTatviWtPMCh2e90mjlvWt8PgTQ0aQsbSzKCn2RN6HmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csBa9xEa8aUDMhWyjMTSxNCMycclTINBAoZHASuZQA06HfLulDDf0XTQX3kQZBpK4Pdoer86pUVnxZTfPbpP34bE6lwzqXnR0QhNj3QQqRQStqTAJGKiVo6ZAuIcLcxn9oqZlmyt0moUhYVjjtoO27VI9Ll-dmp5RxA0GaqGgyA2fiz9LZVl1RLMfA5u-1ecW2-l-0eDQO6wAwfALCkVR57LwerhxKwz25-c4-1LDgwmN8EC8AKwLLvGR0JFR0QGbpX6AYlEd1m2-aABVvtGCkoyx2PbrNAVs1JTeKb3Nx_QDDd0cczvRSSqwisCz1cT0hsjtbgMOctYk8TqWytIVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1gPclb1LxLTbSUDlyYUqUWkSzuBp58Y9F9Pv80Fcq1OqQemKSESoVS8PpHc7BVMyuyPHrkiO4bQEq-Lf4Q0kjt4juccaWT6OBlkHfhHYAeJVWo34C-ddSDlnd3vhnowDr82XF05IiSp4vOfKljYop9eYdQOhW__qBQBPPsjbDlyDCT77-3FveMUg3E3k8rQzZogVYk4BFbzj3pWRUJrp6dgjKkSmBuYFwFHkoWWuCSyuc9Pvm8ZmGJpPVYv9bftmezD8MSbGdfIIBKHnWwFLVIt5AgHhq9_lV3iVmAOa5pFBF2rlSvL9_T1-odR7kHCazUOoHTd_gGD6H3NdDWwMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT_-gjzq_31NUs9pqqOJZoR5_8Mlp9hCZoMqRrTIyJMSgQfH1iIDD5e3n0J1d0P1nnq5xw3Ld2Ii0mDIxH_nTkNyNslik9pgMpSgHkc5uKMAMPiTaMvRpkERa6S_HOuhipXhCAu_M5Ew6W3Hs5RJMb59in8MDmQhM2VBXVxcwxCThg4LdUq7sLO_eExHws-omHBRinjr7AzZ9ABEx7_q7qjouwvsu1OE54oJTIX7XfMpEJHIKGl3kYjBYGMg-VMVR87bDFDWL3PjFnI1psnW4PuAuJZWOT-DbP0Pc1fpVewkRGGXwuYxjwGiljJ1dhx4_vZjwiV1T-_XZxW_rtrWlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=gaRkmit68JzzLYZTFg7KXddNS82hz7PKLqXdQwFlfzzrd8Y0Rke6p2B8eEPfaEE5FZQDj9Ib65Xsz7C0ztmUMtpQ8wBanTRa6vEgaGQ4Uuyp34wygxt4huKh8VPAXTVKDz96B4L96HrNckZDi012qo10NlL-dNa4gFpZkot1ZqunttJo2c4NOyZybxDynEAG9z88vuaZqY_MmkKSpfC049MuoZR8r5zp-sznEx8clh3HsL62UOC1XXzUPGw2D8Btk6jUXD5l0fcAHtasdIB2EMOPML1r8bt3jVX6IzbKpSJnRtGWrJT-e53FUGwb_KqZQf6R0Ah654lNQoD531feMTxKAHjggfFXbrRj_J9UWgPj9byaTPZnRmSonEnDXcVQqfsm-xpumcHH0NpacXL-Q-UZESVr1HbTLMbQNRX5L9xB9bvPGGnoqLVlhju_2JAFgKsyuXNBm6L4YN7UWVrP6bHG5dL1RooXwNOcoRuEaF2UQJsFkKYR-4oKxZ0IM2-LYQweh2WVFuFXJZVC2jDoLVjXE3B37VRnxsTDd5HrQh3WFNMj8pX0me61ZbPdkGAJHqw-gMgwRSnbOeAHx0ldM0C8yOGiagpgixcN4P4p329TpV1s5Ow5wllzUlmYZqfGZa408OSEB0v-Vur_HWqE2__ld3EzniDUHox8yjIUCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=gaRkmit68JzzLYZTFg7KXddNS82hz7PKLqXdQwFlfzzrd8Y0Rke6p2B8eEPfaEE5FZQDj9Ib65Xsz7C0ztmUMtpQ8wBanTRa6vEgaGQ4Uuyp34wygxt4huKh8VPAXTVKDz96B4L96HrNckZDi012qo10NlL-dNa4gFpZkot1ZqunttJo2c4NOyZybxDynEAG9z88vuaZqY_MmkKSpfC049MuoZR8r5zp-sznEx8clh3HsL62UOC1XXzUPGw2D8Btk6jUXD5l0fcAHtasdIB2EMOPML1r8bt3jVX6IzbKpSJnRtGWrJT-e53FUGwb_KqZQf6R0Ah654lNQoD531feMTxKAHjggfFXbrRj_J9UWgPj9byaTPZnRmSonEnDXcVQqfsm-xpumcHH0NpacXL-Q-UZESVr1HbTLMbQNRX5L9xB9bvPGGnoqLVlhju_2JAFgKsyuXNBm6L4YN7UWVrP6bHG5dL1RooXwNOcoRuEaF2UQJsFkKYR-4oKxZ0IM2-LYQweh2WVFuFXJZVC2jDoLVjXE3B37VRnxsTDd5HrQh3WFNMj8pX0me61ZbPdkGAJHqw-gMgwRSnbOeAHx0ldM0C8yOGiagpgixcN4P4p329TpV1s5Ow5wllzUlmYZqfGZa408OSEB0v-Vur_HWqE2__ld3EzniDUHox8yjIUCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZmPrFfICyo-ORmxDtSczzlhqdnxgbv55QH3TV3DfCQia1krcG4VzcxYaxDqq8nBx7QoQBeDjJu_Y8mWU9X-O6eSX0tIs_29K5fTTQuOL0ZEbKZeHa6OoQ_dGx2HaZMZhHUpkoADTO-2WBgmFuubf56ODsme-fG_fM_5km404uotNAoPvZuo_EBQh3gS0n1PKHSlMaN4aayBtccbE2HqPs5JYst4Vkp3Mt2-ZPq7jlJ3qlIal7dtOVpR7twLtk4_ZU4ZBVkjWx3kM0tEtOqGYG4KCUwbYL0f0ydhPW427RtKw2KnZ97Lq82d_uzlox2oXummzMBFA_TttSG10p9f2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZqvGJUcEl8G7qMjmWRN8-sgWg5To-3cEtFtNufvaoGvWCTGQ_GryMI3ihFr6U4xYA5FP6o5St9IS6Bb90I3-bgoB_xbxgwyIA-2dS0IZZhiish23hEO7BYXo8XLcGH-UJQAKOITSlNZ-rH-bHRpM87__njciqWACrBqc6Hzteeo0NXxec9CurmkRz49w7eylHpkXAY_bnX1K0HJWvfZD-QElp1dxQhwKPxDHNVq8ToGmSyuX-XQ08lpSW52MDRL1qJBfjLPqvl_FvOcZb2MpDwIYvNZSdSoOA8VnEf0Lkxm-ycGfZQvUGV29Uw_a1gVm4J-ub4f4iulcijf2xvvRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwbAuf2z8cjO2IpONIgPfLeFrgKYYAcdqRuAWebSJ-kSQU7pGgzn6Oo8TM92AqVBO5mBkJay5Or1tXOCjMm-TkBTP5GVPXE89seQbsyISbotORi2w2gONeJf1aLINB7sUz0lEtzhxa9qQNcft9TEvEb7mdEFl6lJ62uyCby-ck3paLJnCYbgKFUZJDJvjbq9ax-afVxenMP_T_r2hVdmV0XWlBA4q4WHNVRL0wdTzsv8_yFmx9Wis_0akCzIr_c89dCqkToPqnQAtrykNMicsa0y9PCZto162BsPol2O3w7W_9zDSJv8MLP3AQcEBuUWlhhDjJM4gFP1FfrH7wPEyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-_BA5LKChpWPYjgqsB1v33x1CqKUpP2g88g2O71v-spI_h8fD9O6xRoEvCS4e9PhH8uiOkVKRGaxwQK1kpPxJETSdovKCzLSexs3NdWZDyyTLWjpbqMZrYCXocITnu2cRhETlwB29DllDNClaOG0G7sgFdObMS6_c2IcEqB5zsmQyk-bxyu1PP-mAOpExV9snowAA8Ido6fS-TmDT_-twxAmrQeuI6FU2utVtyTC5acZeZ6-hDKl03RTte6ZSExtQ_RX-DE0P2sIZgjY_gsOK40Ba9O76M7hNF8jB5Q45ik8TxUWa4yBh3IYSrofY6ERgaRL3CqPOfUjJAbmEnJsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n__oyVdLRs6BRx8vQXENyQ7T2vvDl-_Er_7EZ-lfH0Qn8rUqitb8J7yi5PDQ7iPTtYvwKSkizKyXlO67HikxB_L6uGz5t0BdNMwVl1zpZwwCllXgggq07_5rrPMvadvSFvSxK9-0Yv_ypcg2AwGvNpNzYzuxRDG622bXPTUFmpWMjaanE7uqUtEECPBybLlTDW0c1JGXUjK6XYFjVk7Lsh8YW4igPUOb5aRMXc8JWC7gwR2ovRPkdmGCYlSZiplznrMnqrN7o_2XhNfvUq-I_HnhQN4jyMYpTEu0AlWk_J9pjARDyhlH4tvuEelnquuxmglkYLPXk4ENj21LIvw6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGSLGn1eOmABKN-6gK_OKX7KQBePxsARwozyn9Bau45VUhE1yUhbudycvxx_Wn33EUGAO1vYeEBE39QsGrCCR8mBC2dEKxJrJiNv5EDQjFqDXgL56ivHwjwr0pMGgyrOod-HqXcxkKHEstF_y7X2yX-aWC-LBPTSsvKCBsjmQyvazUe2jilwTjODNrLhvasGYk_UPbH11eiDtG4yb0jXrk9Go-AlKb3ajOdDdYsISdn2_WrIS2OEuAwwXRhuVJfFICSUpqZckPSsK6ryDLAR-Pza9wbf1A-edfW-t6R_-g2fQjLGtrtYYpDNAI1a5qLqBVODt6qLZ2Q_nL36P8Biaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIfNdL0gFhb0FJqt0zXOPygtNDoR6q1RhDTvUtvyz9LZ92rtcHesp9i3RInjdI41Hhv75aiA-fdSbSgG4yNRiQ4QbZLxTHWltNDpFWeJqBgh4bd2z0v5y--DkFzU57cU9kwQ3i6tgKxueBkSvy7rwLTqGPffhgScTVOx4enKIUBvJqHg3ldFSgY-Ob9ITvDPFoQVZ04YqDud6oq4qqxEU-sCkb1wkgbKCnhvFBDu9g2sitGNyB5-s0Tv1ktjDqR1IVuEA4-ZXEEMu6ZSFXYydEmYqnytXqWolxv5ZvZpNHfKlKVhSiChagGgftqbffLKJDCzqvDxX5ZZCPG3lGmRlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EMFDgfH-bkAVkdTiraxnVAn863EW0jmXQ3gHKBNRBEaneTZiMF41HMBgBjUmC9q4qIE6Hb2m72ZePWaZWkFeN2P6hGUa5hq0dV_MSa_L2HsMMdhJgqf8CpwE3v9smFjQ4t9qTlJ6TsoVZYq57Ryrzm9_7jUrLNSVzmOozbxhGZgjb5H5T5yL2MaD21hgvzUAZcWL96v33enX0iz7vyprUTzFm-4U6Mus_FUfx1oI3rm4aog3rLTmnWsHtLdnYEmp_EVp3Z1K4Ft70zMstPd0cRkpExywdbT3Pefmfrb5BhR1qLe52DWorXfLbrzWjj-lj87o6pjER8ULP2_LlmCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKjl4FPjkm-Dy61d7rjqP5fIWihZpg883Xko_m7UAiYKeQZTIVSVjRJPgAZhcPik6WEPQnzJPaK8HdoSEYXmCD_meXGYm1d6zHzGK-3GS0CA0wVeq1-gtnZlmPqTAL3SwCBHmnwoFLq3pcwnJVulMiBoQo9AlGp8KnPywk5KhydNcR8UytqYVoDbG7bxazRZStyUQuNpHk64qoF2qp2lvUZOX1WVnnrnIXQZaxKjyqPDUW8WgxVfv4rJJN_ysPR-f4Q05fWxbCY3zjRgmTKrrDRZjuNTvLmT5FUAjcAJRt2317--hqzMs3aaKK68-4ebTdcSuyZpa4fMK98sQXHJbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR-gCUkwWSg8Kg2s7xckjzCzzQ_fHEaXe3tCfrmQmQBY2p14wlR0E6Gbz2O0zTtcyJLxhalomabOL_bRb8vJrs--SV9T9_hxx5eNwGmpGVNwlglFrfx8yD2tXEfgXWAX_XMqKErsdetJf8Cx66HvHht7F71SKZLLaX98BnkQ7H_vMS5LMkkUy0fHsHvSaUsVd4UDy1C_OvY9v-L6UuBVoyHxMGF9MUyorl_B-pM5uPdzV6EURNkI9ZNskdeZEhmsnewC471P_SdXur9tFd1xBuQZqzeWNz_AI2YrvFfztut7Ly632ijjQQyS7HT3hIY4Eja4bZQua1dvwumO2SXDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRYVNUAowypEbOhzCozHj3DccdO67TvHpism0peU58X45YEr_qkEN5cZO-So3rPbSB3WK_H9D5gcD3JWiqT0C0efLMX3J-9LL86FcWmNeMWUAlTl8zYD0kq3rbNcqZiMlnrD_yQbjV0W4BwiYG6cJfvlm9saBvSyDgs7c_4S7Uuxducmz2vcsROyEbKub1nvoPmVuWH3qXGDyAk8jtiWSUS0udChY5Yr3FjxPqt_r6_m8y-2Y9LnDgFSv7FG8gq_D2lPITIdBXpvqPljyZbNBjJ_OJ36IKB80OtY2JLiFKr8t0OyPMVheUiicTL_xtJHdPtw-2Zqi7eWhWBo0dryCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=YD6tWbt4XXjuf6eVghkEIrVWG9cryumom3yOSXnzpClfObxTxbDEm0t_aMZVXnL9EHZBlXEDGoi2qzrx5_DweJv8XLcQuflTj-_blWmDcHQCYYKBlvoxwx2tT-tQUqeWW447EA5tcIN4dNsOvx4vfjM7jt48dz_39xMO4DWAZIkFQZl1_pxPyLN4zNc6Q375hnm76afVaDO65nk2B1aB5k9V_h6xJZebfFyCJg1hrqErPZnRCxkCFTPSeofAyjKBBJDX2vX3bTRcCAouu1EsOPCt_eQwok50OUpCXsWL8YjFsY5mnZCajsIgvTATUp45auEPGMxKf_eDt63RAmZ0h4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=YD6tWbt4XXjuf6eVghkEIrVWG9cryumom3yOSXnzpClfObxTxbDEm0t_aMZVXnL9EHZBlXEDGoi2qzrx5_DweJv8XLcQuflTj-_blWmDcHQCYYKBlvoxwx2tT-tQUqeWW447EA5tcIN4dNsOvx4vfjM7jt48dz_39xMO4DWAZIkFQZl1_pxPyLN4zNc6Q375hnm76afVaDO65nk2B1aB5k9V_h6xJZebfFyCJg1hrqErPZnRCxkCFTPSeofAyjKBBJDX2vX3bTRcCAouu1EsOPCt_eQwok50OUpCXsWL8YjFsY5mnZCajsIgvTATUp45auEPGMxKf_eDt63RAmZ0h4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLTf8SD7ksMSrQA68WXtLorrZ3aQwa-DQBkt7hkbTFRbHgMuPnwjW6Id3EyRyQ7pf-zHCCjtZxL7t10YcyV5I13uHPXsthPXjdGuxzj_rRrCrkm9J9d7c2NXY0JJblCHJ0LuL0FsXcJxsi_vvvRpGMawZJOcemJLXM6AQCRycHpreOvMJqhYDT6bWFguUSeef0wGnRVJzZUEDjSOEWiMNlPXjQUVsxVXmYHXXHxa115FDkbZUGeRqh3ysmErQDXEs_KF6lVi0nTh-48Hc2eNS7bOGKz41rtYgWBtWq2ZT54dqleD3tfhrWNQQFaCJdUZGgQjCVewm0s8WmU5dbkTpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezaJQ4SA0iNmBGpj1Jr18DtpSVCnUrBGTobWChZgWP1iTREmJDl8kSCTjlXLwHXwt0tGvpopgoTKd1a6C9kez9AEpXtsn0SFDCgTmqcTnNZBDtVHvQtBrttmWPt2KKYfNGPrSiDb-izrnPNRTq3viu32p0_Nbc-8rVLvCVnI-WNNn7PWOT9StmUgKhL1yI-8ZCuj0WhQl9LDfVVZogMH09SE85g81YKNpr753kKsuWmuDWDRe2NjCRX49unrVH7NysZRjSnOW69WPLu3zQszjmNqdMXPb-zJJP9dTo5TVKQ-gsb71Fclbc-31vw-uZUM9EYiro26_Ocdkmzm3rEaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruZe6EtoAO3pqVoSvqO31s9kFgo4F6urkDE60mYpe3QGs85BP16-qLqlmhEoWTKwBFUsxeN8LLwmHaX6cavyYo2F8nAbHlSG5wWfruI6s5XSCgJbg8a5KalhD7uN4CCcw_l8HCp109eEorIqQHS5Ay8eIKv7fwuZnyS4HVATl_nP_c4cMkyq94FtTrDMLrA14Gb9gezezIdTJ0Ymr8t-R4AlpGg7CkWWh9G1wmcwbHDBVztVKpNM-zLZkiteBmBp_z-T2C61G82aoEQllgs4t8RyOSfk5XlpafT1xu8BJ6X8YR6IRSUQJX4zRXw3EyL3lkELPNMtyQSrzlqHUsqrlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVVVkk3tWIpJpA2RAE5juT3BkJG8b95xwx4L5NIzKUkElcGNXl9smUDdxg9Yv9dTPPqwU7gZKNNY49toap2vs-Pl8va2P6n0jCiynppvZb2ULTZ62bM-PkODf9eSmQAZV6mMWZB_XzvyWtxRMGpTquMAFMzYWecvVCrgEaqatLn4CLLgswD1QVAwBJcdCRzyAM7dP-8FWcou8v6OxeEnh8qlaO9IMvMWpEll5nOuWV8Ai2oJUioJeceYz2-nGQmkWPAxRjd07AgEFsiWmDXwalajNvlaAUU9ZVK4zQAToJwJQ2A0Aap8w7lRbRq_bNkR4ZtfbOnp7mHouiWp8RL6MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=n1IiyqBqiGt5jcx9htT1BWZk35H6iPaSKGKM23yV1trFN3Vb0ss11kifsx30vZrbgGSCCESvizdRAx-2gN5CZlRGePX1UdjWY40CY1Fs6crrcWe-bv-YnmO1Gz9_KUAO4M_hhUo2yo_BZheKr58Ay6sp5fT3En3Qtb7sGvWcNSVokU1rsT29XGMDAVc3UJ8TvEVeOsPH3uEH0G93TkfPKrvrVRQma-yPOGpvn2KA5N_tH0HYYoJulBRBFD56MIgj7CLfMxE6ytAOuYAPnXuZnVuWSpgpKxVXFmaDyih41T_Uw99aS5ktdWKuqImTP71my2KHTylOmVyeNBqqX0AA2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=n1IiyqBqiGt5jcx9htT1BWZk35H6iPaSKGKM23yV1trFN3Vb0ss11kifsx30vZrbgGSCCESvizdRAx-2gN5CZlRGePX1UdjWY40CY1Fs6crrcWe-bv-YnmO1Gz9_KUAO4M_hhUo2yo_BZheKr58Ay6sp5fT3En3Qtb7sGvWcNSVokU1rsT29XGMDAVc3UJ8TvEVeOsPH3uEH0G93TkfPKrvrVRQma-yPOGpvn2KA5N_tH0HYYoJulBRBFD56MIgj7CLfMxE6ytAOuYAPnXuZnVuWSpgpKxVXFmaDyih41T_Uw99aS5ktdWKuqImTP71my2KHTylOmVyeNBqqX0AA2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8UBRmj8TC9AMVjVTUmQbmjMZIcaMz1MCAaNsOuLSKx8Tglt7DskS7HBGHTmVw3XPWD-kfIIha1hU0-HLDd9l2Dm-h84Reu6Awl-fGEkWguqoUmjoULGA49l_6x3P3OcTZMoPM3jptWZuGzzpPqinOuNJlE211ugtrFTtIuhbSOGufBSG_PmGviBU2z3IKyQmGGrrYyPSrUPf8bMClI-hCsIR6l-FjtmRtyb559AlFrmtFAqvCwl0b3r5MWUb6B-FhsQN99j3mgpPwtYVB9JLhz2sg3_rSq_-TTmcCNznaICADAhEOgvoRPArUTWPN--XYEXy62T-DfFGkgyN0rikg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=P6808ydHSECNhcQHlz_PlRttujXxllf5mAORxDYZMSpZ9mOC0PHMOpXiON2MnVrmEzHwaaUOBfioPC5d77WMjv7FsI8Ifweq62ZJMz9Y873ygZr4HZvCSaxVaG9S3m9mYH10hPry8NQQuGLKWNQxulATmu8BXGT6hm3EZ84DT6vHNPAYTqC2I4RBsPdDiJejKa0DjmioSKAoAqHQDudTlZWGCnXBWdsVGl9-ByKhNfGSjjdjDnGyIep8-Pb2EEf9Kd_5rZmDwR3Et0OVYztApoEu4j8gsY8VUUM44UrBYEK3dAqTz90GLZKxwM14sVMYxiEQZpp4QBqArsIlxZwv1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=P6808ydHSECNhcQHlz_PlRttujXxllf5mAORxDYZMSpZ9mOC0PHMOpXiON2MnVrmEzHwaaUOBfioPC5d77WMjv7FsI8Ifweq62ZJMz9Y873ygZr4HZvCSaxVaG9S3m9mYH10hPry8NQQuGLKWNQxulATmu8BXGT6hm3EZ84DT6vHNPAYTqC2I4RBsPdDiJejKa0DjmioSKAoAqHQDudTlZWGCnXBWdsVGl9-ByKhNfGSjjdjDnGyIep8-Pb2EEf9Kd_5rZmDwR3Et0OVYztApoEu4j8gsY8VUUM44UrBYEK3dAqTz90GLZKxwM14sVMYxiEQZpp4QBqArsIlxZwv1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuJrMyCK8CfvHjNETH92dV8qWkelpkVGmg0yMtU-GRA86AIrTmeehABETbMRiOq1ZhnNkEyvUR6C3HQri6K8wiAbroG6-dX4qc9YHGKz-g5ZC6ba94TMNICaH3VA6PGaoEAqept9XgXmL3JGAJnUYls2jjFK7sA7sbR1IUBp9SzrHGEZzD8tRksls2XeQGNsvrankcgAUclppeEUOeNlMwa3TvJrj3Z_MGizKhyQCp9N9bK2EsFB-47iXwoIg6yo1svMH6sasK36xdh0MQ3XJMWefsuOLRvKH2TEHcMLFpOR-5HadKt_xGorxK6xc9_niv-3zQCKoUQTyO2BbpQyrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G46bXu-b9EtsgfiTkL3FSnhmkNZ5FNe9VgT9yAE2WfoQjAsCW57JusvbQvMzagUVABqTBfIVDpSnz3NtwnoQt0Hf-kveXmtzeJxdzOH36K9tRCgh9_X_f-7Web8D_3raB3DelEEciNRwRvDZ9zV24386ujXqLd3g01vE-cphDmpTJMdKimAEAAFgfx02fdz0Pfdk1nxI6DZo-p9k8wkFNHDcBf0u7t6h1pZX0fUnqTejvsOAuECCLjdYNgPhlBastxDoNvCDUdBKzJbrswBMAo5MnsdeBhOl8jW_MFCnASvvmuBlu-fhxiG0FKYu9U4sjvl7ZbC884p0jvNFoTQ-cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw51P59vFHZjDid2CpAaR9XdBO10Xsfevu-GhtdTT7T9EWQMPmylK6EV6w65bfBUn9pbvWO3KIy_NAbI5RjFccW_eibbZOuNSX8C_TTjNtHDo0NngF6fk18I3xQSgztzGYa3gzJcgi4amlP8eTX2dyKnU5ASi0Pidl0yip0kvl-3ZT0NlytTHHAiXnJHxCNUyjLyAos_73nTTqxLIHt3o9pez-zkruwjlrLFRqZzeTRXXNyHv_5tEuHDNEu-ebrQXA5u6BdAa6h3ko8atA1MXU28Qav3BgnaE37z5nQZC0hHPsj9NyngiP99lSoRcUJW3l8dHWsE4jzt7XlH4xhyaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqMMeU-7f8uY_sewbClDVjw5rgFzo_sSoTOX2jr1pTB5DOOdkiioyTz1xksPREi6ThHHvVeFJG1mjOHp8204BxOzQUPGDPmhWiXoyewu5UHZ_CU_bVcavdcUOOgNpNfbvL69o4h2OyOX05EUJ5ElPpGypcpm0VN9GfZECPOioymzV4nVxqPb3jf7_uQM26PogiIqRonzNW2rihdahVU_aAHnHNqa0CdHcgiLuh-bUnKKcgjPtAiiZJ79XM33CBjm2yko3LPa75QjaLFDZm4Am6UUHgQZYmvWmNVbwHtK2bTTfN_r_blthReAI52aBWtHbvyN9SeTBbaIQROsjNj_Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ema2amUJdiGAk2a-DbWrm9T_jIsrhyhatmgmbTALUhjF8TSR73huc7RF61TZM9uQr598VLgnB-gYbWD-ivRFTYvK3erTgd7fpPf0IpULRcDx7ssAlUljdZgvbyb61XKeNsVPUY6Aw1R3UusChPTdNHjWam9TR6GyJJe9si1QCxrU8-lEeUDVpLhtOIK2QW-xCvXouFP3DGw0KFQN8e1iFEk1km7Iho7UirnZxeNzCBMNiBOEtl8f2TeBvfmll9i7sJaezEqXLpmiIjE1Vs45MIUkmzH7PxGWGiAMsB2UQ4V-NW4N9YVkkmWpgA8XvfUwZfgyUasuS0cxGbZeWh8hng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd2_LT9VrLxLu9BH2b4QkXI8ixbkC9Ndh3dkJ9IBdI3LqXJ-VOwEhYJoUs5zkx00W-CKOLeLrxgVgqMR5638h0oeIOArmNeh7_Cn5-u2wipXNUqMbtvahLUft1y3JLMrD56d3IkfI2lnfiXqSzSp-nC__Cpyf760ysQaSag7zcpYXHQXJvDCzTwR8WEl0r-UedimoodL5qc6pNqqEF-bIy-SIJztjQxl6NRGgAVI5ugf8D7NYhO21vFr_FQhhCnQmD8Np1GW3aMtrkdu3iZ_ipCo1aQ4he7M7dE79nKBqf3sFxxCJRooyOWuk6jGLrTQpdJhyV1_aVgZAiINlT6lvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiZrV_akjq3BBV9lEjqCpvlwQH2D7Mku67rvTDwyAVva-1Yzdf42jSmP_evZqlBO-4iLYhuK-XmLGo2_CYr53IZQjcKhxdo0TUlhrcgLeWoYIIpnGkwjAusX1p7Ac0Aly2ro8T6ubHumK0ipHjtnqiqtpWy-kjY8wUmua9vgzfs9YDXHa2V8EDO1sowrgZGBBFQ2N50SzgVTZdrNjKUGaIY-fFD-EdEMZiVxWdRNMo89R99LEPrBeEgctfTtInM_gd5Il1FRQVqERGT7ABq_RQVLq4A3suzf4klct5yo29ZzDOKAyxcs8s5Oyx_Fqw-7mrsPH_Jhu4R1XG6BMRU6LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqb9MHKqU2FVgGUsbhFBIU5ozdaeW3NputHjD43bCzBlJGcz5LZHisE9miOYWiivENE4xt1i6rtpafEeQBTfEF8tNWZJM_UDXD_fJF8PQUl0cAQ3PTfszwHgPS5Sqe3fDweXjaYkKnosGVfwiCcvW1kcjGjYVuOw11UJe3ZDfOkl-EBjP7feW_QfXdEcIrdh5ihHVWLVQuFgPyd5vTItN30XGS-oRl_CDZFMa1X-Xhicl8eRsKfWNVZm9rNXL3yuHIwLZi6P8WL2tj3LoR2-pX9_ewSBh3jMt4csgHZabyozRogUwppFy2r9_dpErC3DASVZ4WJtKA5N_FQw312oIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0zVFKVbrED0xwcRNnbsUQRs1gh9dk0eEA1NHdwd2osx9KLMb8yDAXfJ8xXnSzHHSfBpqf8FODK0AAdlxD2d9QcdVM4Y2O9_5p0bcT0tgjkpDUpjZN7Q_04FFq76oMA6mdcxDRqzPkzM2G9ygfQ_EI7reZXEgimcqydZoM0tQHfrQruh615sIXnd-WO2ShpM-9fis3kwZoDc41FRWpI2Jh7VgHR5k8LxmheA2Wxf-GNw7JOG9_kE7oWI5JwPL5edWLwr4ghN3XuTJ9sQY86CasyUMRWfx_WPk0J504m6WCOefOTyV91DHmzcvaiD1W6bqmhOfw7FnT92Di68QBw9tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5ARBqlJ7TGiutMKpJvwSv_9PQVuyhJtOinCxTC7zMfvSW6Jy2RwkW9JhdTcW7lWN1i3bcT1pa-ilE1ojrMeW9JDrnofH99FN0xtCazDUz69rraE_xeE3izmwauRNUp6Mz_EA6-pVGz7QzLeC4QC4QhmezKShc0O8bLesgVfFPnNjHIyb9IVC78L309Z7qdTs-z_iIY9A7H2gltmD1fzhlWvwjgCwrN2T5KlLoP-tnd1g0Ytl3Gbh_8W0hpQfhffwqaFJmWA4aDpxaqD2LOsRaF74SaFXd3Bc-oobC9hw_65GtCnecRLLedyOPXtJ6LKiyaq1maIPLEVGyMJdytJyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHvIpAZ2xiJgUmQeLE-kCI2fI-3gkVI_W_vxANaB81MjyMWHzlTD2h-u-ijeYR9WEfkhDGpnR01FscHwJtESvmD487IVSwuWaOVxFBzoUDcpqNG_MBMSqYHzNRVGw0JGn5wPhdHBxATiajOpFNrtrdWPgnSnk1JBFZV4F0zT1jexcfb8F3LrgZzR31DRK7qPbcV649y07DvRkn_1dBIjxpe6XuoebgSu1QnAkgNTTHZETvU9SUdNIHHjzI859L_RAeb-8SJ3yH3Aka-cypxygBHka8Wm9XzPYnaypI_NgB6QgNnCsCwv_PyzldbBubDeEHWLnpb4nVUlxwfe0ZSpow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOC5X69x4wZVC-52tCoMELXL4PWfyq70BX-kaNCKaIs6Vy1GW_mBVMVXt7UscO-185vDlZOV-ZYhia66fhXkw28AxmMBfgvEEQmXCFH7CTu7GsycqR8RlpxQn_tDwPnFLqM2h-pFkFEzJA1W9tFbvtck6N-PvF9BS52xHAdQWrJpPQbG17jV1VpLj0R50KzJamUBxZk076j14p2viisnbuhXQCXelf979KGsjEGM2iiP3zGs8oXE_v5TixKpcWD-wSNENi-mTFRbg3jywcAbVnKOamb-ac9-6x2XWxwB-qp2eU8BAryVayZnBs5ahbdAuB-IqwL027_6pN_VWTW_rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUMZpzAmfV4VIXVMtPDjIWaVjplB-NWsforvO-jcPlZpbsWoHN6VPdD7gMNVkY7M94wnLnvPHSJmLECm8Pkp1AFLl_TFYB9zMhLcDyUVgN2kDEqN2pZ5s5jgT2aAi4Qewd4lKS3ZJV8RoFYAkxMipb0ldfQ4G0eAscZ-d_OZ_jeutj6Bc62HVChGpPWEhRpjNTyXgyAqXK2J0jJPIuR8BwP-Vo-z9uYxdf4YPUbzUomT0hcFWdpfGmiEvIP78UPPikCVTl9GO9DMhDGW6UFkZZPMjd6D4kF6-34aM4Pi1M5Ya_VqGDSJewBaQ59S4Kq5HUivi2Ap-z4PMIW_gjDlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
