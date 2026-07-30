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
<img src="https://cdn4.telesco.pe/file/UfOLw8wz2SSj1zYvy0gstIFzHjBkCcvlDGj3L1masitDbd7J3ajmiFJ9hKQVKpy1XMA44f5zTcPf_9aCNIoAo7b-l2ueCFqDGs9ssh3Dn6DZJYO2p9ckuhHbZNwSs94PxgvA71v9oz7rI0ntw653Jr7eI0yw95oD4ikMBTnu1zt_YIIViPixudNxbaE3OB8kx2BwVGR3wNtWH-gHVKwYsHFX9JcnS_8Cpkpb0JVmQxBxL4TO-pLtWVqu1Xw42aIBR7ISmY01vvffA5JW_5AgB9X6OofU7B-YrRAB_1L85mlWAX6ZmKb3H8feLxm5OO3DEVMQ3EiU-9udfEqbqcru3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 975K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: چرا سازمان ملل اسرائیل و آمریکا را محکوم نمیکنه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/alonews/138750" target="_blank">📅 22:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
به نقل از یک مقام ایران: ایران هرگز آتش‌بس به سبک آمریکایی را نخواهد پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/138749" target="_blank">📅 22:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUbADb_4cBzOuvWr1_hZrP63RdVxTWRYGes5cyILZK86uVY5-qs535h1cRGg1Igu3oo2s4LIo1h4vsvm0uonmc7cwmPDIiEbw7hUYcCFylCVNUfoObTYNwNBsvhhH6bYJV83JhvS3WA3xMRCJNb7nAen1lYJUAZsBQxl07xsNNBq43my2_zcl6VCYVg7QpKApeMgaVHW5yk6-ZrjL4MiK4hZ85ZWzZ54eiockR4_YVmNucIPKlD0ETG0CaPf4ib-fWav3VTxKX1R1F92laBuao5eLrNqt9z5p8m5pb0yV36deFBiQDCjly_bznLhXXDp_glOIYCZTmnU2iAXvtLQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سعودی در نزدیکی مرز با شمال یمن ماموریت جاسوسی انجام می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/138748" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کمیسیون اروپا: هفت کارخانه بزرگ هوش مصنوعی را در سراسر این بلوک با ۱۰ میلیارد یورو تأمین مالی خواهد کرد، تا تلاش‌های خود را برای کاهش شکاف فناوری با آمریکا و چین افزایش دهد.
🔴
در پی استقبال شدید کشورهای اتحادیه اروپا، تعداد کل کارخانه‌های بزرگ از پنج کارخانه برنامه‌ریزی شده به هفت کارخانه افزایش یافت.
🔴
این کارخانه‌ها علاوه بر ۱۹ کارخانه هوش مصنوعی موجود در کشورهای مختلف اتحادیه اروپا، به بهره‌برداری خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/138747" target="_blank">📅 22:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=EdHHjx17Ym2TJbuMsPVktVFXaaAYeGWwP9HDNb1zR9vu9AzGmol0C-11v2teeWkhRnpj6JIt0o4kFAeG4xT0eOCM78x5VBWVctwapT-Nc7OAhEwJs2hsdYWpg6Qntd5ZZ1-1a-_CQkx0YncyJ-oSsS8NdMNGtRYzFRW4Ak6auxxMrOO52EDWOY0uFFexqLxnlOU4V9MxzRLe_M8eaELxvzpLI80hAdfNQAcZzscHgEqS32gSoy7vhjREKL4Jr4w74onz8f9Cm4czQMMvdCFftxI18sncsjj6Y0gw47uEqEwcb47_XszAN3PVIoZDt56q8lhramo5z2rWeoGPulaMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=EdHHjx17Ym2TJbuMsPVktVFXaaAYeGWwP9HDNb1zR9vu9AzGmol0C-11v2teeWkhRnpj6JIt0o4kFAeG4xT0eOCM78x5VBWVctwapT-Nc7OAhEwJs2hsdYWpg6Qntd5ZZ1-1a-_CQkx0YncyJ-oSsS8NdMNGtRYzFRW4Ak6auxxMrOO52EDWOY0uFFexqLxnlOU4V9MxzRLe_M8eaELxvzpLI80hAdfNQAcZzscHgEqS32gSoy7vhjREKL4Jr4w74onz8f9Cm4czQMMvdCFftxI18sncsjj6Y0gw47uEqEwcb47_XszAN3PVIoZDt56q8lhramo5z2rWeoGPulaMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش ایران اعلام کرده است که مرحله بیست و ششم عملیات «ساعقه» را با هدف قرار دادن تاسیسات آمریکایی در بحرین با استفاده از پهپادهای «اراش» انجام داده است.
🔴
به گزارش‌ها، این حملات به ژنراتورهای برق، سیستم‌های ناوبری و ساختمان‌های اداری و پشتیبانی در پایگاه شیخ عیسی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138746" target="_blank">📅 21:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد:  بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/138745" target="_blank">📅 21:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/138744" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=Kav3-Ipx4e8fQPV7WfEaTadnjNcuqjEVnKuerY3OhL7BvAlFxlkXpnjVGkaxrSzG7bOAqFpZ7jkGY34pJ-6kASMu-3m6Uj_8bppCHuhAdg2FK1MmRrZslmy5JQlF_XH_UC5m5FhqSAy1fOeNgwFcu_Y2lpAhIVat7fLV7pZ_pxxNwY4cfCpGQfOmdHw73y3YInnxoRGszmnc1Elxk1IVoAe5-YycHVnnq_p-iXReUR-d5m0MRrOkAJ_QXFlN5N2gjfVWW9xLEKska7m99FHLeDK9bJW_HE5yHAoTPvqBPmEafByviE5DWtgN7ssQXBOkoJP50voDSQ_l2FM3RMrPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=Kav3-Ipx4e8fQPV7WfEaTadnjNcuqjEVnKuerY3OhL7BvAlFxlkXpnjVGkaxrSzG7bOAqFpZ7jkGY34pJ-6kASMu-3m6Uj_8bppCHuhAdg2FK1MmRrZslmy5JQlF_XH_UC5m5FhqSAy1fOeNgwFcu_Y2lpAhIVat7fLV7pZ_pxxNwY4cfCpGQfOmdHw73y3YInnxoRGszmnc1Elxk1IVoAe5-YycHVnnq_p-iXReUR-d5m0MRrOkAJ_QXFlN5N2gjfVWW9xLEKska7m99FHLeDK9bJW_HE5yHAoTPvqBPmEafByviE5DWtgN7ssQXBOkoJP50voDSQ_l2FM3RMrPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: انتظار دارید جنگ با ایران چقدر طول بکشد؟
🔴
ترامپ پاسخ نداد و رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/138743" target="_blank">📅 21:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
گاردین: عربستان سعودی در حال آماده شدن برای حمله‌ای بزرگ زمینی و دریایی به حوثی های یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138742" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgOSfpIMN8KYJe7BSWn1rDCCPeG3JbrIR5VA-6d-t6fRaoxe4MAe-CogNfy7fUm04YMx3kgGIBq_7-nY2uZTUJvwI2g4QMhN-u2bWFsEE6mNwtuxZZUUo6ecAsByV0RNIJuUGDTqXDrmjK6dDCXRlf9Dgp9olm4SbSzVag-BrJIWsgrKZudoNvtXohyIKh5t3SACtRSCpbIk_xH423Ctdedf2yTD-RDei1YqhEl8hLF_Ap0lGaR5R_XIGExdwaZaV2tUu6sOf9big--rvXKc3dpHS1iOP2Ce5FPfSly2Mm3cryjDQ76BpoieW0yRFdD7ChYrYyWL2dMfFA61luGw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گلایه کاربران از زود تمام شدن بسته‌های اینترنت
‏
🔴
بر اساس گزارش‌های غیررسمی، ضریب مصرف اینترنت بین الملل به ۲.۷ افزایش یافته. یعنی هر گیگ مصرف ، ۲.۷ گیگ حساب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138741" target="_blank">📅 21:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOo9iPVqGwazQLcMn88vnbcmpa9zJcOs01xKbHG6eJ3YFQoLQCb0VUcwgrQ46mvJlArbRh2_2wyGmg2ukp6j9Q5jrWr-eP-7hEu7XyOINuPWRQUjoJkpA2anbEBGWH3Ff2HaUKwUHK7xKA9F00g-oQSeRLvW3ZjCVxfDSC1n_M0gTQZ5fvIe32bXO1Ze6gKTaAcA0jADsAcbLfl-c6QKHLTg0TUgy8YM8vrOkKYxPBj6lqYtSbdo3miy7MlXMgO28R30NCXcbKfHWza_LadDP0fzxWEdpo7a9dKl3zJH1kqUDKCHq_qzFXqHMQIMmEXpB8By6tFgBlWK91PimEhzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خارجی بستنی شکل باب اسفنجی خریده و از انباکس کردنش پست گذاشته؛
🔴
و اما کامنت یه ایرانی زیر پستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138740" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گاردین:
نیروهای سعودی در حال برنامه‌ریزی برای یک حمله بزرگ علیه حوثی‌ها در مرکز یمن هستند.
عربستان سعودی در حال آماده شدن برای یک حمله احتمالی زمینی و دریایی برای شکستن محاصره صادرات نفت از طریق دریای سرخ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138739" target="_blank">📅 21:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
اگه فیلترشکنتون اذیت میکنه پیشنهاد میکنیم یکبار امتحان کنید
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید (برای شرایط اینترنت ملی هم اوکیه)
(همراه با تست رایگان‌)
خرید وتحویل فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138738" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scJwI2elfscniN_nlSVOaqNQFvPTceXZLn1BWZHHjgy5SZKlaxzE-ZjydD2dPHj-Z49knT3gAyoyLlpAUi3jTSVI66ElpjQZxCIsSGThh35VOQkEHDUiGxa0M1zJ93fGCyGrEatpExuKUPV7iykb4XdY9rB1n6eDeKMSD7TuAARHKZclDzIW1-W8f5TFF9EOpVcwosvo6GXH049bwUbzH-mLoQGteUN_hBzPYL9lUTZoG1F2cnNVrDWEEqbMcOtJ6bkllOsH9PmmWECP1BxX7hiDzuSMinUqDWJ2J87ulvohD9SRUrlvDY-7RKi4LEb_xb7qmsjEOTfvygo9DdccNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
تعرفه سرویس‌های مولتی و تک لوکیشن SafeVPN
📆
پلن های یک‌ماهه
📍
10 گیگ
➡️
35,000   T
📍
‌‌20 گیگ
➡️
50,000   T
📍
30 گیگ
➡️
75,000    T
📍
40 گیگ
➡️
100,000  T
📍
50 گیگ
➡️
125,000  T
📍
100گیگ
➡️
250,000  T
📍
نامحدود
➡️
400,000  T
📆
پلن های دوماهه
📍
10 گیگ
➡️
75,000    T
📍
20 گیگ
➡️
110,000  T
📍
30 گیگ
➡️
145,000   T
📍
40 گیگ
➡️
180,000   T
📍
50 گیگ
➡️
215,000   T
📍
100گیگ
➡️
390,000   T
📍
نامحدود
➡️
550,000   T
﻿
✨
ویژگی‌ها
✅
اتصال پایدار روی تمامی اپراتورها
✅
مناسب استفاده روزمره و شبکه‌های اجتماعی
✅
دارای ساب‌لینک جهت مشاهده حجم و تاریخ انقضا
✅
تک لینک اختصاصی بدون نیاز به بروزرسانی
✅
حجم واقعی بدون ضریب مصرف
━━━━━━━━━━━━━━
مشاوره و خرید
🏪
@safevpn_secureSupport
✅</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138737" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ارتش ایران: پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/138736" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGF11-xJdA8Zo4FOkbYmM5RvRdhn9PKRBLAygSEhqKXPhYDRvb9Hpnji_5aXGL3iD8u9n2fInxk-ISmV69iTiH4-1DxD8DVr_sfP6DDP6JGwDoCdGfPn5SUcnAVQHoj7CDML_1AJra6blvcDac4TinSEUN9P5NTnmdTp-EqJz4a5eGp3c3q6IjyYY34Tdfj8rBzFqtjXaeWJ2sX0eA72VC_Yag9CwVUlonsTqkvwgqSpF9uWJAf2oJy9Hr6Ar-L9BPFQiodyATEK6IaKwqL93Vitw2UDj9XhzmHx3eudLudg-3wm50ZxMLPHbF11TdTMH2yoeOBKroTPeNRaQBn84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله تایم
:
حجم فزاینده‌ای از اطلاعات جمع‌آوری‌شده توسط سازمان‌های اطلاعاتی آمریکا نشان می‌دهد که روسیه، حمایت‌های حیاتی مالی، اطلاعاتی و نظامی از ایران ارائه می‌دهد.
🔴
این کشور از افزایش قیمت‌های جهانی انرژی و کاهش تحریم‌ها برای تثبیت اقتصاد جنگی خود استفاده می‌کند، در حالی که درگیری‌ها را هم در خاورمیانه و هم در اوکراین طولانی‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/138735" target="_blank">📅 21:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نتانیاهو پس از بازگشت از آمریکا، مستقیم در پایگاه هوایی نواتیم اسرائیل فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/138734" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=pk23CaJ2XiADpe4uLc9rOndTd4HQsaVzYia7XnjDcxF2rfW1gcdu5y4ocbU0XBkikYMaA_p1FowLnQpWFDzNwDz2agsy7Zgzcoa3y3Wz8lhwq551bKYOcehj4gG38TYEWVi-alA_SnKpNQoYxNfS2bxgnjVcUJzjrW8VGr42AC7bjrN0G4lMq24k0-WQ6db9KL8ABhGkk1M9msxLYGlQvWbA9LqokJtpILtcR8Jz8_GlV3KNcUqRi8PjxVjGdTS7U6_Bqerf_aNebIcUkpIzW_JcrO9VWx6eqkY3NVOzLk8EYvAs1yMuaqK99GeukMRvM0lTIIIgCzuZRIHgPmOLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=pk23CaJ2XiADpe4uLc9rOndTd4HQsaVzYia7XnjDcxF2rfW1gcdu5y4ocbU0XBkikYMaA_p1FowLnQpWFDzNwDz2agsy7Zgzcoa3y3Wz8lhwq551bKYOcehj4gG38TYEWVi-alA_SnKpNQoYxNfS2bxgnjVcUJzjrW8VGr42AC7bjrN0G4lMq24k0-WQ6db9KL8ABhGkk1M9msxLYGlQvWbA9LqokJtpILtcR8Jz8_GlV3KNcUqRi8PjxVjGdTS7U6_Bqerf_aNebIcUkpIzW_JcrO9VWx6eqkY3NVOzLk8EYvAs1yMuaqK99GeukMRvM0lTIIIgCzuZRIHgPmOLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق
🔴
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138733" target="_blank">📅 20:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138732" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=lpIQGxUYHN-NSZEDVaNwjwRwCZbxMtcLcjBkO73hzvdvydWuLfb1eMGwlF4Gj92QG1N5WthcGwri1XF9eDm3oz1IMNek1xq7NB9ifLo8OyFFGwmHoCMabKSERsZoRT2brMFr2LCg8l0DSVpO6ectScl_hQkCp4PyVAzYrhv2_7kpX7tR1Z8oFs7pKGQjidEiAGio1cBshyNZJI52njf778HJS4iauNEtE6pKcAUmFV93dSHU4IIA66SxqPmVH1c-JPOlZrvE3ZLD12XhW4BoK4vyz7ueoMKzPS5thJZmspGhPXiLq35110TRbjnGr51zSED01HxUEycIgW27FYXBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=lpIQGxUYHN-NSZEDVaNwjwRwCZbxMtcLcjBkO73hzvdvydWuLfb1eMGwlF4Gj92QG1N5WthcGwri1XF9eDm3oz1IMNek1xq7NB9ifLo8OyFFGwmHoCMabKSERsZoRT2brMFr2LCg8l0DSVpO6ectScl_hQkCp4PyVAzYrhv2_7kpX7tR1Z8oFs7pKGQjidEiAGio1cBshyNZJI52njf778HJS4iauNEtE6pKcAUmFV93dSHU4IIA66SxqPmVH1c-JPOlZrvE3ZLD12XhW4BoK4vyz7ueoMKzPS5thJZmspGhPXiLq35110TRbjnGr51zSED01HxUEycIgW27FYXBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
المیادین: اوکراین از طریق میانجی‌ها در تکاپوی کاهش تنش با ایران است
🔴
ویدیو منتسب به تهدید ایران توسط نیروهای اوکراینی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138731" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDsMHjM78W073JnuQ2bp3N58eQ_HkuCjDhmkf5T1sQ7MaixcKamcyy7MrlnxL7EJBc9v-YUvWhTwVaFc7HQV_L6y2BEdRYUHqv_q5QOVIvV7G912DeX58Mb592aS-kh5eFboZgjgtW0qfY5ZngAZ4_39kpVJTdeSzY9mbIOj0XLQ9HR_SKuoHHd1cqfEo9nJj0oHS4eHE8LU3EDDbYSrdNdbkiHyOYFFGnwXQM8n7jhs5YWNX9-n2UZVG0DOlSGEHYHpoiwyYut_VKnkwVU68zcXgDfLrIR_bqQN4EjBTKCm-UBuWmFo0rKjU9ga-oKew_79fm0fTTlsMnfI9nfGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دورف، مالک تلگرام مالک تلگرام با انتشار این عکس نوشت: روسیه، من را به عنوان یک "تروریست" معرفی کرده است، زیرا از پذیرش درخواست‌های آن برای نظارت گسترده و سانسور در تلگرام خودداری کردم.
🔴
طبق قوانین روسیه، من از "انتشار اطلاعات در اینترنت" ممنوع شده‌ام.
🔴
به نظر می‌رسد مقامات روسی در مورد اینکه چه کسی می‌تواند چه کسی را از اینترنت منع کند، سردرگم هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138730" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_0GukApawE-Uh5_CEz1YI9jeUbjelU2ZLM8ksEih6R6y4HjVY098AajwqDljh_BOcgmHpt6SuChczT_YIpv7_f8uEwWHrzZi0NWCVn4AcK-lP9wskUbcZkcp7C-Ym-DGDYhMmqbNDYTXjU9LVvLRSom3InmBnB7q7I4cZ3yH5USeYSaVwk5_9mHJBStOhwwYbopN6jRiHQMK8ixJ10QcbQxPtpXGRWWXCMzlIsUQ99olHM-xyO-bTBEkKH7UvWWJdRAtfS_YM7rugmge7lKN-wfsMdf2J64bb5JB4E7Wo5V1Fewj484hAt5nFIPAI7xfO7NsGOyGL8jcN3BdIPdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک کمپین خود را برای تقویت جمهوری‌خواهان در تلاش بزرگ انتخابات میانی احیا می‌کند
🔴
ایلان ماسک در حال فعال‌سازی مجدد کمپین آمریکا خود برای تأمین مالی عملیات گسترده مشارکت رای‌دهندگان جمهوری‌خواه برای انتخابات میانی ۲۰۲۶ است که هدف آن تضمین کنترل کنگره توسط حزب جمهوری‌خواه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/138729" target="_blank">📅 20:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عربستان سعودی رسما تشکیل ائتلاف بین‌المللی برای حفاظت از تردد کشتی‌ها در دریای سرخ را با حضور ۱۴ کشور اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138728" target="_blank">📅 20:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد: بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138727" target="_blank">📅 20:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6bbb7af4f.mp4?token=Sh0Ez37fEt3I-rOU0-vLIEt1OsCxjtHFEddFRVUPYwXK7SgITfcOdQPwCLjkarof2K7PVlwhmU4FOsoGtIkQyqF0YiTLjM6MIaimfHZc0WKHVkjbUKNzx4uuTi--dtL4F_qSfPRBV8ZIoaKY5RceocCot5sFYaKFWXCb-Asl3FEzKbhFvbmJDJ1tIQAkEE0AIGpHrR0xUcaKiweHt6yl3gh0T5E3HyeAkVIRjy00pzaqp7qoOENJr70uE_h5BXd8udpLY3RwdNbDtPJJ56iwiTQOtNf-4wumkaHjPOTwAGaahG2hROlMKPO4lZ3ayMMgoiAQu659HLex4BkkMZIQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6bbb7af4f.mp4?token=Sh0Ez37fEt3I-rOU0-vLIEt1OsCxjtHFEddFRVUPYwXK7SgITfcOdQPwCLjkarof2K7PVlwhmU4FOsoGtIkQyqF0YiTLjM6MIaimfHZc0WKHVkjbUKNzx4uuTi--dtL4F_qSfPRBV8ZIoaKY5RceocCot5sFYaKFWXCb-Asl3FEzKbhFvbmJDJ1tIQAkEE0AIGpHrR0xUcaKiweHt6yl3gh0T5E3HyeAkVIRjy00pzaqp7qoOENJr70uE_h5BXd8udpLY3RwdNbDtPJJ56iwiTQOtNf-4wumkaHjPOTwAGaahG2hROlMKPO4lZ3ayMMgoiAQu659HLex4BkkMZIQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلاد کرمی(وضعتان چونه) داره واسه رفتن مردم از مرز مهران به کربلا تبلیغ میکنه :
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138726" target="_blank">📅 20:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd220</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138725" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138724">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نتانیاهو آمریکا رو ترک کرده و الان به اسرائیل رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138724" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
( فاکس نیوز) هانیتی : اگه نتونستن جلوی هسته‌ای شدن ایران رو بگیرن، چطور می‌خوان تنگه هرمز رو کنترل کنن؟ هیچ اهرمی ندارن، همه‌چیز تموم شده.
🔴
نتانیاهو :  نمی‌تونن، اما من خیلی خوش‌بین‌ترم، چون روحیه مردممون رو می‌بینم؛ اون‌ها خیلی شجاعن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138723" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138722">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
الجزیره: سنای آمریکا نسخه جدیدی از قطعنامه اختیارات ترامپ در جنگ با ایران را بررسی می‌کند
🔴
این طرح رئیس‌جمهور آمریکا را ملزم می‌کند که در صورت نداشتن مجوز رسمی کنگره، به درگیری با تهران پایان دهد
🔴
سرنوشت قطعنامه مذکور، به این بستگی دارد که چه تعداد از جمهوری‌خواهان بر خلاف موضع حزب خود رأی دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138722" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138721">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وال‌ استریت ژورنال : مقامات مصری، ایران را مسئول حمله به بندر دمیاط دانسته‌ اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138721" target="_blank">📅 19:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138720">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نتانیاهو: زهران ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/138720" target="_blank">📅 19:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138719">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
زلزله ۳.۹ ریشتری عراق در مرزهای کرمانشاه احساس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/138719" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138718">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe1662f40.mp4?token=t2oF5JsvB29OA8wKBOJrzeKgAw2PPuPjjhreLRuQPtzNarYmv58DgPvZzbtsNv3sj-EcUQUueS5pTJQQKUGNwBJyqEFuzcxzpttrq_WqMvqFomoxxDAiIXQFiThqucU4pz2jECGN59NPNN8NeNoipOppuFYIi5dw3Us2vyqaxpUuVBXOVmGRR8N2UrxNJvjX4HXdlbxnAO3Jp8U6oov3xsdqcxiOpP0kjqauLz4BorXGYtPu8bPggGlWKPffHPayQZgvZJcPgZrj4j_X8KJm7obo2QciqjZs8mU1H-NlxbknZZy48tjvRaTY9qjEeC_ZEhbRZGMSDtDZBENkRLQ9D48sA8M4-tOyNTy2pTby6S0uCsOGd9rafhSrshvKPaFSnmYwrBAdep6g99FgQz8VwgPt3017kK7HQXZ-W0Kuex5xevvkqCAPEoUfCRhXFzCGXkAPdtaMK7WS9ES_f7N-os1vjBy0XNHuhjMnBj0Q84d7t2Iofg-2bRz4kIl1wUWdV4PvCmnSzt_zOqBshCk-BkOPkPHaWyTyK-UhXIm2Ndfg48dTXMb-ZyimoKAALF37zEWDKb-acrDnEWOj8cQw_tjGclexKNFWFF9MUDA3nH3as4AqsUmMyMsmBy1IRQq-foLU_7yqOtD8KJX-qOG0ATa2OIdquaGyvq0KjlnbDg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe1662f40.mp4?token=t2oF5JsvB29OA8wKBOJrzeKgAw2PPuPjjhreLRuQPtzNarYmv58DgPvZzbtsNv3sj-EcUQUueS5pTJQQKUGNwBJyqEFuzcxzpttrq_WqMvqFomoxxDAiIXQFiThqucU4pz2jECGN59NPNN8NeNoipOppuFYIi5dw3Us2vyqaxpUuVBXOVmGRR8N2UrxNJvjX4HXdlbxnAO3Jp8U6oov3xsdqcxiOpP0kjqauLz4BorXGYtPu8bPggGlWKPffHPayQZgvZJcPgZrj4j_X8KJm7obo2QciqjZs8mU1H-NlxbknZZy48tjvRaTY9qjEeC_ZEhbRZGMSDtDZBENkRLQ9D48sA8M4-tOyNTy2pTby6S0uCsOGd9rafhSrshvKPaFSnmYwrBAdep6g99FgQz8VwgPt3017kK7HQXZ-W0Kuex5xevvkqCAPEoUfCRhXFzCGXkAPdtaMK7WS9ES_f7N-os1vjBy0XNHuhjMnBj0Q84d7t2Iofg-2bRz4kIl1wUWdV4PvCmnSzt_zOqBshCk-BkOPkPHaWyTyK-UhXIm2Ndfg48dTXMb-ZyimoKAALF37zEWDKb-acrDnEWOj8cQw_tjGclexKNFWFF9MUDA3nH3as4AqsUmMyMsmBy1IRQq-foLU_7yqOtD8KJX-qOG0ATa2OIdquaGyvq0KjlnbDg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شان
هانیتی
: اروپا قاره‌ای در حال افول است.
🔴
نتانیاهو: من با شما موافقم. و می‌دانید، مطمئن نیستم که از خودشان دفاع خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138718" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138717">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سنتکام تمام ادعاهای سپاه پاسداران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/138717" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138716">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v0XE6Nu0wgAve9opcMCvFZk-2jj_wrS9HaKYYBy0JzieAl4x80uhe3CDezeNcq7Y6yQOL-bQgj_psYHRAoQ6ck4KEHRhqJofYuU2D5k5xycs4yQZfFDEr7dgiYcGyfkO5Jwd4Ak0JZqh7y5HuCSvXh6hZbyrjhkcCSTQLDaI9vzV0ZbJwddO1jRm6y3mjTWLxTbvchTGfLRYvADyNurE_1jhQWo28FQKDMdqp3V1sWaen8wbNavqk2dSw_jjyxza-eHgWTp0AkQ30CJlL2i4kW41kaDLeVPnzr_A-Gal4y2A0zhMs2q4FS6o8G3t2-GFsY8XZi1zX8uBt_FNS8aMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام تمام ادعاهای سپاه پاسداران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138716" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138715">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qUwydDkOg7HQMl6PpLpgb6Q2io6gMAq97sk6n1PkHBAT3fgRlX2EvIfNRvsf6aPcI4gWvt_8dUYcuHlPi2nS-hlRpy6y8K5OKAgTYY0njhy5XB6j2vlZLsqbFwcVoBqjYxvLSxXPmJoJ8_VqrewOt1bQKvrdBhneAwWcRPLpoEMZzqQ8FHuNr7OdyIJtnCqvRAIYy6hh0f1mtVa3qDUg6qgToC5dnkHVq_cztC2l8qsFOEx9QPejI9s--7u0V5N0Ryc5BdOBLH4dK7kdJmJFEAFbWrsRr3W9O0QjJx7X0BnoKsdKhyl0NigqgYPbBPhh_eR4p7Yjit1uoQzNnswTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138715" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138714">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGLksFHrKlN3XlfK8jFJWLHpwgH1heQucoojoibU3dAySwtf2ORBk7UyktmoaZjajDuSPO3lU-mBO9ZTsTAG2mrxj_xGlYEKCHGc6-QqLMtSILzegoTCcT1Csui0DOeKN5IckrTGIpAMSIomYI_en8f8s4m1xSCmo6uubNAXRcPrjnTpkirotYjistbq4szIT7VGc6NoRUOr9DCyjFdC_ycr0ilUyAbTfcFcqMlveAnJUWylx40FhQpTPhcEBnLdTAlcD4-jhkhKerRm1SDC6lZxzz2JFLkH0ThLcZw_9J3fyG4zsvqILW_cnwd6Rgp82kI8zROG6Ed8Sk6lz1Fd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: تاد بلانچ یک ستاره است و همه این را می‌دانند! او پتانسیل این را دارد که به عنوان یکی از بزرگترین دادستان‌های تمام دوران شناخته شود.
🔴
با این حال، جان کورنین از ایالت تگزاس و تام تیلیس از ایالت کارولینای شمالی، که هر دو نفر از آن‌ها را من از حمایت خود منع کردم و اقدامات من باعث پایان دادن به فعالیت‌های سیاسی آن‌ها شد، از رای دادن برای این نامزد برجسته خودداری می‌کنند. این نامزد در هر صورت، به عنوان سرپرست موقت باقی خواهد ماند. به یاد داشته باشید که هم کورنین و هم تیلیس، به مِریک گارلند و دیگران (که تعدادشان بسیار زیاد است) رای دادند.
🔴
من هیچ اعتراضی به این ندارم که به طور موقت نام تاد را از لیست حذف کنند، اگر آن‌ها کار درست را انجام ندهند، و پس از خروج کورنین و تیلیس از سمت خود، دوباره نام او را به لیست اضافه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/138714" target="_blank">📅 18:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138713">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJscOglPKobap4lJxJhC0pAg2WIjc_YCuh3XyWfLlIjYSZaGz33zzVr4rCq4qyegvnfz-nS0N346iby4rjHAgIgorQmDb5LIjhrUsNq_T40jC1tnem_m1GZZRVflSWaq2crvExqViLqi1rqHsIWjb59I0xDUeh7FqsaAluw-zzoD3EMd0eg1T82hFP3OUK3nhLUgFW6x68wIECkSXU0i1SJwrX215Z0iLsNJ58F9Of00Ykox7qMWjmzYpxfUNIxydJ2UOc9TzZHeMSk66xAnQg0ptJmUEZzs8f8qrp_HDHmICQaxxG3SVJr7mkL1GIXiHSx2X5D4NifkQSLD38IJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از صنعا، پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138713" target="_blank">📅 18:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138712">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04131030f2.mp4?token=TpzYPfyWHChIlGOZUBbOFTt43voOPxWjIFtt_vFANAe6FvEizIOQ3ZjU5FxKRPrX3v-9SfL7LkP0KSU_SgnsVnyml0zhSrMe2sl98uZdtpodF_lELWWCKU_eyhB_NRLTstnV7rVmsJ4wE6yQgfdDQ1kjPgvx4NBlXwAcVjAFAh3vZ_HC1p8BT7JbhuoiHM2-_GO6_yELho-psOCbTZyl-ND44zAmwlIGpWXB-4ix3_PmU_1GN8kOJoAAJkCbbtYhBAdiZ5Mg_RGxTJ2-PgyPiH2Fwk-lsUHwUmdAYKhAgVAAhIs_tq_zrh-ARNBHU7Zba-y8QjrGdxCP9OFjAImf8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04131030f2.mp4?token=TpzYPfyWHChIlGOZUBbOFTt43voOPxWjIFtt_vFANAe6FvEizIOQ3ZjU5FxKRPrX3v-9SfL7LkP0KSU_SgnsVnyml0zhSrMe2sl98uZdtpodF_lELWWCKU_eyhB_NRLTstnV7rVmsJ4wE6yQgfdDQ1kjPgvx4NBlXwAcVjAFAh3vZ_HC1p8BT7JbhuoiHM2-_GO6_yELho-psOCbTZyl-ND44zAmwlIGpWXB-4ix3_PmU_1GN8kOJoAAJkCbbtYhBAdiZ5Mg_RGxTJ2-PgyPiH2Fwk-lsUHwUmdAYKhAgVAAhIs_tq_zrh-ARNBHU7Zba-y8QjrGdxCP9OFjAImf8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالملک الحوثی: حتی چهارپایان و الاغ‌ها هم از دست رژیم سعودی در امان نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138712" target="_blank">📅 18:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138711">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اکسیوس: چین با ۴۰ درصد کاهش خرید نفت موجب جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
‏
🔴
چینی‌ها استفاده از ناوگان عظیم خودرو‌های برقی، زغال سنگ و انرژی‌های تجدیدپذیر را افزایش دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138711" target="_blank">📅 18:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138710">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به صنعا پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138710" target="_blank">📅 18:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138709">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64267a25b.mp4?token=TH731S_HoAqBiIUEoKSbweP9FCD7-su3xRwWcsPgFYmKuECyp0jUkLYWsgcRcJ3mRSojQNDACkOrMjKbyzqrcfq3uBBv6eqEPUDNm38Ru5oifn8xvDQxeJgciJXFMxARjQGFnxUoyOhE7Ie4ti_t1mdkHq1bDCgXA7h0UsrEyR87Ukwxv9vH9Ltb_vVfgKLe6n0RfavINo9CVXjwxby_V9JiEqPV-oCuxsCbVVgVKjRM2SsWISF_JVMNj0-ZQ9IGLTqIABRuhteeTVY5a5J_jAed3feraBRSgOzrwhz5L8u25VQUvri_vzKa3590fK0Nk_W5dCjJj6FEdWoqO3mIHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64267a25b.mp4?token=TH731S_HoAqBiIUEoKSbweP9FCD7-su3xRwWcsPgFYmKuECyp0jUkLYWsgcRcJ3mRSojQNDACkOrMjKbyzqrcfq3uBBv6eqEPUDNm38Ru5oifn8xvDQxeJgciJXFMxARjQGFnxUoyOhE7Ie4ti_t1mdkHq1bDCgXA7h0UsrEyR87Ukwxv9vH9Ltb_vVfgKLe6n0RfavINo9CVXjwxby_V9JiEqPV-oCuxsCbVVgVKjRM2SsWISF_JVMNj0-ZQ9IGLTqIABRuhteeTVY5a5J_jAed3feraBRSgOzrwhz5L8u25VQUvri_vzKa3590fK0Nk_W5dCjJj6FEdWoqO3mIHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمران عباسی، عضو کمیسیون آموزش مجلس: یقینا در مهرماه گشایش مدارس را نخواهیم داشت. تمام تلاش ما بر این است که در اول آبان یا در آبان ماه بازگشایی مدارس را داشته باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138709" target="_blank">📅 18:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138708">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به صنعا پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/138708" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138707">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جنگنده‌های ارتش اسرائیل شهرک «النبطیه الفوقا» در جنوب لبنان را هدف حمله قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138707" target="_blank">📅 18:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138706">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NllvpJEKVEC_hTgT1s-igfjKA7UkGFOAczC8P3rmq9Rk9yK_Tw9vajsP0X7LmcIwoIEUMuqbwq7iCDxhPzKCHBGjwv8jJQ_gpmS7Hv_3wc4g7PIJUnD0oy7uIRlXeRLY-HCGxBESWR-MyqkNFqsTSvFeXr3jH9CuXPjdi7sg7tS3wk3wZO2z_5JXRpA4xw-oaTASZPz35gRAZTNhLrmwNXWD__Meh1yfqbuatRKW5iRNYF7PKxNLtUiKgRL7VPffrlbWxXuiIyK60l4KgmD7O0QT9eER_BCj6I-N5M-dWc_4WKHt2VKVipLcdiyOHB9Qive0SQdM_R-tceXTlwilIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبیل فهمی، دبیرکل اتحادیه عرب پنج‌شنبه هشتم مرداد هدف گرفته شدن بندر دمیاط در مصر را اقدام تجاوزکارانه غیرقابل پذیرش، محکوم شده و علیه امکانات و ظرفیت‌های مصر دانست و درباره توطئه‌ها برای گسترش دامنه جنگ هشدار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138706" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138705">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فاکس نیوز:ارتش آمریکا ، امروز گزینه‌های مختلفی را برای انجام عملیات نظامی گسترده‌تر علیه ایران به ترامپ ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138705" target="_blank">📅 18:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138704">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دولت روسیه صادرات بنزین، سوخت کشتی و گازوئیل را تا پایان ژانویه ۲۰۲۷ ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138704" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138703">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39f1520ea.mp4?token=aFTbwi-XU6i1dDw1byUoVqCSbtjPmDaA4x3Uek06SznRcOuuiRejqo5ujk5-bKQD8OeMThoBL99o0QhB1oo1nYGd9aQ0bIgyQfrDs2rnd4MntGoPpf0n2-EjSuLBKMqJk7Fwv0keutEi7gzTDDG8mqxCjT4lJrTK5vZaSrH30boZ8Rxd-TvKGHRcYX1_SDbaqKeDSaN1gWvmNfbvmGtQ_BhLWshsyg3i3Wt3Uqeu2ZhJAamqf8yj0SsJLBTIPusR_cd-gMX0cM1vL6QwA3e-8vL5FIok1vAOr2cT6z553tXAuVwwVlSHj1rk7scB3gC2GHiLBuLSs5TNVB8eLdqfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39f1520ea.mp4?token=aFTbwi-XU6i1dDw1byUoVqCSbtjPmDaA4x3Uek06SznRcOuuiRejqo5ujk5-bKQD8OeMThoBL99o0QhB1oo1nYGd9aQ0bIgyQfrDs2rnd4MntGoPpf0n2-EjSuLBKMqJk7Fwv0keutEi7gzTDDG8mqxCjT4lJrTK5vZaSrH30boZ8Rxd-TvKGHRcYX1_SDbaqKeDSaN1gWvmNfbvmGtQ_BhLWshsyg3i3Wt3Uqeu2ZhJAamqf8yj0SsJLBTIPusR_cd-gMX0cM1vL6QwA3e-8vL5FIok1vAOr2cT6z553tXAuVwwVlSHj1rk7scB3gC2GHiLBuLSs5TNVB8eLdqfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالمالک الحوثی، رهبر حوثی‌ها (أنصارالله): عربستان سعودی همدست ایالات متحده، اسرائیل و بریتانیا است و مطابق با اهداف اسرائیل در منطقه فعالیت می‌کند.
🔴
بریتانیا و عربستان سعودی پیش از این تلاش‌هایی برای اشغال یمن انجام دادند، اما به دلیل مقاومت مردم عزیز ما در برابر توطئه‌هایشان، شکست خوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138703" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138702">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436447c59d.mp4?token=VRvgPeGumcbnZtOEL5gtSwYAapXPdB1NiOx5YB9Jm94VEIAOoUf-wxOMj1EEh2hDXcmEg2USa5Yow6u-3Ub8sX6RN7f9pdEtutaWBlAduJLYzzIsMT1Ju_hMgegEFkVElCrzcq5vAmp7CRVMLuoUtwHLhPVn-pb8TcW-KtfVEqh8-O_KdD4ZUEWDdhbvkmX270u5QYGJGt-T8rXXqo4iGkUYyiazG8zmvN9wQxioLiuT5rMLpjB7lwmWmtlHv6Q2FsFxRQMrpFiYMZS8-yQIUlonxUM34v7A2foFFfwSBm-DyUdxpLuBOOHFs1tcul0xZvilUNyQNXgWtyhJd23OeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436447c59d.mp4?token=VRvgPeGumcbnZtOEL5gtSwYAapXPdB1NiOx5YB9Jm94VEIAOoUf-wxOMj1EEh2hDXcmEg2USa5Yow6u-3Ub8sX6RN7f9pdEtutaWBlAduJLYzzIsMT1Ju_hMgegEFkVElCrzcq5vAmp7CRVMLuoUtwHLhPVn-pb8TcW-KtfVEqh8-O_KdD4ZUEWDdhbvkmX270u5QYGJGt-T8rXXqo4iGkUYyiazG8zmvN9wQxioLiuT5rMLpjB7lwmWmtlHv6Q2FsFxRQMrpFiYMZS8-yQIUlonxUM34v7A2foFFfwSBm-DyUdxpLuBOOHFs1tcul0xZvilUNyQNXgWtyhJd23OeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایران شب گذشته موفق به هدف قرار دادن پایگاه هوایی "علی‌السالم" متعلق به آمریکا در کویت شده است. هنوز مشخص نیست که چه نوع تاسیساتی در آنجا وجود داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138702" target="_blank">📅 17:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138701">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df21da311b.mp4?token=A6rvhcAMcNZtxKr1ID-i1YRn9LznJL-Ki2e0B_UP1WFZDOowPVj9J03ekEf2_TRKbmdN4FeTcjM_1e3_GKiOMY8kRt9rEpu56Dxn7fw6z1z5mMfMe3PMkxbKyhyglY7_ME4fENOXyfZRUHJXknEcSZcYPi3q2mNhsLSe0vSBzF8OXOwdIhZy0Eb4go3egLHeVnb8nlGd3ohtfI8u5f3nVHqzxLs0tfOxRcJuHHSI1Cx3SidskuaPGj7Kqh4a0CsGw-1ix2bnvn19K1l9FEQUFmmZjp4YJxojjXI9x7XkM6R7EgtuUpgA-Oi2yN-FvWGd8T8llUsgwLlBLFNscARqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df21da311b.mp4?token=A6rvhcAMcNZtxKr1ID-i1YRn9LznJL-Ki2e0B_UP1WFZDOowPVj9J03ekEf2_TRKbmdN4FeTcjM_1e3_GKiOMY8kRt9rEpu56Dxn7fw6z1z5mMfMe3PMkxbKyhyglY7_ME4fENOXyfZRUHJXknEcSZcYPi3q2mNhsLSe0vSBzF8OXOwdIhZy0Eb4go3egLHeVnb8nlGd3ohtfI8u5f3nVHqzxLs0tfOxRcJuHHSI1Cx3SidskuaPGj7Kqh4a0CsGw-1ix2bnvn19K1l9FEQUFmmZjp4YJxojjXI9x7XkM6R7EgtuUpgA-Oi2yN-FvWGd8T8llUsgwLlBLFNscARqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته پزشک های اورولوژیست؛
این‌ روزا بیشترین مراجعینشون مردهایی هستن که میخوان به آلـت تناسلیشون فیلر تزریق کنن تا قطر و اندازشو بیشتر کنن.
این تزریق معمولا بین ۳۰ تا ۵۰ میلیون هزینه داره و ماندگاریشم فقط ۱ ساله.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138701" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138700">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaZ6EHV2S4ZZVL1JTSTx1hG14eOkeyMF7EHJtw9RTH1YHtXlYb-G_iG7omjtDJBiAUHTP9NHbF6Qksapt2QVnGyzLIf6yCNPjnMqf3R6rcdV3p8VbABLU_wuvET3H_FqmuKqnEd1rcsIf-ZYT55B2FW0t2YVP0dzZJCD6AkN78n-k_2YnSNipxZM8uySDTn2QfvICkWZ4gragfILsqvKzk2KBULrNT8JcSbZlwu0HMXDHLx4LxUARDzmXt4_WJOnLBUjER8VGrZAp-DyUp8V8NchiI0wJW4ZSJSr-pfqgp1apvRd743yPIi8RU-mva1BpdkpaiGW58Iqartd-AwU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان از تشکیل یک «ائتلاف دریایی» برای تأمین امنیت دریانوردی در تنگه باب‌المندب خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138700" target="_blank">📅 17:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fdadc251.mp4?token=O1wZPp3oeNPl4QngrUQv-T7oaYXbPKpn2S9tAjFNwOqFY_AH9rPq9mbV0zn-kvYmIMCc20Aa9IRKHH--JscE-Zy7ImPU0eGWW2ylAkUUs_6pfV8qvbGKEf6huUGpIDqBIAdt-sZ09WazpzEmCHr66zlMcCEaMGqawR8BXQZ0YIkMUKhy3DQrX3WrJM1nBJj9UcLjJegcPWTVDCidOkuWG7hJQxV0OTdmfZWPzVi85NNUgNuH_Y_cQ9b5BluKeCSZVGprC2ehxQg8Re3wZyNIomtdHfd3w-LrE87RCXkyxWT4cLCExIxIo2yjJQlq6Z3ViICANyabwV4b_7-V8Q5mpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fdadc251.mp4?token=O1wZPp3oeNPl4QngrUQv-T7oaYXbPKpn2S9tAjFNwOqFY_AH9rPq9mbV0zn-kvYmIMCc20Aa9IRKHH--JscE-Zy7ImPU0eGWW2ylAkUUs_6pfV8qvbGKEf6huUGpIDqBIAdt-sZ09WazpzEmCHr66zlMcCEaMGqawR8BXQZ0YIkMUKhy3DQrX3WrJM1nBJj9UcLjJegcPWTVDCidOkuWG7hJQxV0OTdmfZWPzVi85NNUgNuH_Y_cQ9b5BluKeCSZVGprC2ehxQg8Re3wZyNIomtdHfd3w-LrE87RCXkyxWT4cLCExIxIo2yjJQlq6Z3ViICANyabwV4b_7-V8Q5mpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی یزدی: جوانان مردم رو اعدام‌ نکنید اونا آینده سازهای کشور هستن، ظلم‌نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138699" target="_blank">📅 17:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c24356f8.mp4?token=PZM8YPAMSdqdwZewMszSdd7c0oZSYCWhgLx_nGFPnxY_tBdEOmp06siRe2zIJuSfNJYakJ2L6VY2A58WBWjjjkST6qGIoMFVKkH0EDuAlTjr8VZCOj_wFTKBMTZu1yB79Bls1beGEPu3H9OjXTnRjxeQCZUybS4KXS-Imz1W3xxldCyPCGo2uaSKnI6IETzk3rO_3rxOvVGTQTzWJsGxyNVztf32fpWRSXUwFxASrka02pcRRwAWafPGowpJTe3FQ3JKauyryqDQaDC78Ndf2tdn3V99CXytP6wOkXZZJLRXP6pdsjITIZ_naMoWz31AFnaPC5kFn20dXRVsnQu6Zrquf06kTiVbLSMovpeTkZwryqkvBt9fzlNXYnGx-4k6tTQiohA3_Op552DE5-b2sgn6F0Ge4n8fo_A6sHhtxoP7Fj6N94-fzO7ecCOX44GPwnmHxN8aESNzZsbrdcHbw1IA_EIlXOkcnYy8x2Qn6PChgcVUTM3xRv7veA1tS_P5LksDiTqSx_7Bhaw_g9JhHkXtLAz2YsgJ-8Kk0QnrQAk0PiqYelqjcKHNzQ91P5EOAC-q6lUtEo4eF5av3qwGRoAjp7lwShNCL-Ryw2ByiEBFHChm5e56peMY0ZkobME9QKBhnhKEjquVGEdU5B33x8k9sMaqOkHjH2ZfolA8fhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c24356f8.mp4?token=PZM8YPAMSdqdwZewMszSdd7c0oZSYCWhgLx_nGFPnxY_tBdEOmp06siRe2zIJuSfNJYakJ2L6VY2A58WBWjjjkST6qGIoMFVKkH0EDuAlTjr8VZCOj_wFTKBMTZu1yB79Bls1beGEPu3H9OjXTnRjxeQCZUybS4KXS-Imz1W3xxldCyPCGo2uaSKnI6IETzk3rO_3rxOvVGTQTzWJsGxyNVztf32fpWRSXUwFxASrka02pcRRwAWafPGowpJTe3FQ3JKauyryqDQaDC78Ndf2tdn3V99CXytP6wOkXZZJLRXP6pdsjITIZ_naMoWz31AFnaPC5kFn20dXRVsnQu6Zrquf06kTiVbLSMovpeTkZwryqkvBt9fzlNXYnGx-4k6tTQiohA3_Op552DE5-b2sgn6F0Ge4n8fo_A6sHhtxoP7Fj6N94-fzO7ecCOX44GPwnmHxN8aESNzZsbrdcHbw1IA_EIlXOkcnYy8x2Qn6PChgcVUTM3xRv7veA1tS_P5LksDiTqSx_7Bhaw_g9JhHkXtLAz2YsgJ-8Kk0QnrQAk0PiqYelqjcKHNzQ91P5EOAC-q6lUtEo4eF5av3qwGRoAjp7lwShNCL-Ryw2ByiEBFHChm5e56peMY0ZkobME9QKBhnhKEjquVGEdU5B33x8k9sMaqOkHjH2ZfolA8fhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طی رخدادی عجیب هزاران مهاجر آفریقایی و آسیایی از مراکش وارد شهر سبته اسپانیا شده اند و در شهر شورش کرده‌اند!شهردار سبته خواستار مداخله فوری ارتش اسپانیا شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138696" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=jkhKW94Y9RWlgWuwRk0yWDnrfg7xQloCBU8LnlVgl7Xf3oYqva8s6B-fvbZMKfxpADzcjlGPqKEgbhudBb3CI-K239RsUsZzWqwqL0W1fjbDz_iopo-WM3g6eoNKbhjvs5NJHJIoCHHOFFxSxXPSYLRJFEc19MacDLLokQYZteiyFGnvczwKXAY-KBb2gCDHxwP3sGJyvzkSh36CJ125XPfQRfVRl5wlv9bR2tgrHliRJbrP5ihjvpSpQubBFfC56lgx1z3-R3FVgZEURc0qIPK6nCHcQZH7N8YvnDtQRJcW5lmnRQnuzf-b9QcK87wJ6WjBf2b0odFBCJO9XYoLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=jkhKW94Y9RWlgWuwRk0yWDnrfg7xQloCBU8LnlVgl7Xf3oYqva8s6B-fvbZMKfxpADzcjlGPqKEgbhudBb3CI-K239RsUsZzWqwqL0W1fjbDz_iopo-WM3g6eoNKbhjvs5NJHJIoCHHOFFxSxXPSYLRJFEc19MacDLLokQYZteiyFGnvczwKXAY-KBb2gCDHxwP3sGJyvzkSh36CJ125XPfQRfVRl5wlv9bR2tgrHliRJbrP5ihjvpSpQubBFfC56lgx1z3-R3FVgZEURc0qIPK6nCHcQZH7N8YvnDtQRJcW5lmnRQnuzf-b9QcK87wJ6WjBf2b0odFBCJO9XYoLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید ایران توسط نیروهای اوکراینی!
ما با شیاطینِ شیعه صحبت میکنیم، انگاری یه کشتی که زدیم براتون کافی نبود، پس دوباره نابودتون میکنیم.
شما برا دنیا، مثل کونِ خوک هستین، ما و برادران آمریکایی‌مون قبلا حسابی کتک‌تون زدیم و بازم ادامه میدیم.
پس بهتر از اون رهبرتون که کشته شد، قایم بشین.
مرگ بر ایران
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138695" target="_blank">📅 16:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkgqBuuI1PBiakxixbN_pRZ8x6a5zWutZI-egSX6CVhpdYtdogdeEOnvtt6xXqrfUuEpB1kLV2xd9YdFT6fTQfSN7HjC2AeIXZ5L2S48hBXMP7YaCaXQpJ-R0XDZ7EV7TQjm-d78U3aMsOk4znZrZW6ogZLYZRAey1qHq2E3NixK0LhjuFDMhOndSWqx2GK4tFFfXmq8Ln70He_v8lS33gHLpX5F4t8SOcCPQiDYJPGE2uPVAk3XNOUl-q5N8tZsTZhNEni28NoEua1LsaUvczH3ocQp_S3od0R8YjpVRzubCp55jKQgctHG96qin4fZIUa3skHU0ysOIgCNXgn0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3KgiN_gDbau01n_S4QZhwMJGLJcVFheHifdRIybq3zi0RHjR6FPyNbs1UQ5ZtzYH7iTMUbygSOSP3Zmq7V7bPmBTzvIB7PqZ_nW_hXBAJOk4wCPJvy487U2kukxkkIc_Sr6ejMbS3R2BKg0WlALhGP1hSTAnRfUcnPYdji52W5vF-CoMesK08qf_e7c8b4S8ZfBPMcTcn3nIodNyb_INnZFrVna2Jp9CyUwtf8nztE3RAkbRWAM7tldm35zg1WIR4AoZfydPxrVm_AvPY3VeCPQq7wfXxFu0DwjsDaJEiN2hMt2BGuvP00ZBZPmEMmfZKzqj1CGOI3SgVJ9zjOrtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پیج اینستاگرام "افشین فدا" بلاگر مازندرانی بعد اینکه یه استوری با کپشن "هم‌وطن
❤️‍🩹
" بخاطر جریان اعدام‌های اخیر گذاشت، امروز توسط مراجع قضایی بسته شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138693" target="_blank">📅 16:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بهرام یوسفی، فعال اقتصادی نزدیک به دولت:
ایران و عمان در آستانه توافق بر سر بازگشایی تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138692" target="_blank">📅 16:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اکسیوس:
چین با ۴۰ درصد کاهش خرید نفت موجب جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138691" target="_blank">📅 16:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q3rVK-NG_gN9yrdu7VyL1rhosteE5H1UG64GkCyhTvKLkLME9HJvs2uUxgtW8V5rZy_oVmjHCL9nQRTfQFA_XZ_A5vfyJhi3a3CzWNXiJhoi2pzzbU1xLO58GqxUhjKlDxQ6pyMTr_d-rjZfeMP9tfHSv7Wl-LbBLVjsfXrR6tzpUsWGg-sPpqiKZYTkkqQAjrvHNGIMenf94cbz2UQmiO5_IP9j18sC9nu7uuwPEGHTmxDtb_gPtW1flfYGNI7_JH2l3wBSI7JxDU3LxTopNXNgPWLHjqy3dLW0CpUCg_XaqMJfTQaipjRcwGGiGa4RzdTO1aQ9qEvMQ10YdNY95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jjU0Iotv54KisJBNsUuw8X6REe6WRtVVNYCJe2e8Mz8xgltZkWn3nhdSJx9wb2X4efDAt-QTEEv3IrMjBSLIGVxdGalKhnHSKQ7RctkCQmHZs3m1J1otvjY1PSRGbwKE91daNWa8KwIBBQDAxu-1sJG5vy1RWGFSbsjGOPK-X6UbBNwWY9DorLQimKjXj5D0FCfBomZIoDWRYlEax9Ak8zeO6_YNHdzZzAaXmBXH-ubDfLpKROnTZdHOi3O3hq46FfT1WmWjyX8WLPs1HG5EL49inVexT1tpQvrqa0dEAo55eqbmX-Qy7fTFDdX-Wsq_2KkVAALTdr9_GmLtnBuNtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9118459d29.mp4?token=gwFcqZZ7pvcTkK6HAqrFF3xfil3wFOYcz3dbuLmEyJnuPZ6ufH9aQV0ajt9O3Li9KDa_yUMOnElO8PgEj8SCu9zacwm7rP5J1R9XkmYfWo51rUHV_sDGtp-smr_LdV-G1xwcrfnmfQ2BuBu1SQcEIZjxdcQ3uUaO3AjGFXsJvZUnc8rYBot9Uq86fADwnT9nYdwhfo1JPj1UX0Q4amDoWiWrolmfSoW54zwWRDMM7J_d4shsYN8O2Ae1-pPOCfdM1rU5Emt1MhXImr8QuGXfB1XihqGuhFCSWfC8BYBF3E3IbLVhMLjguWu6kZewjIx1HNrWr4ajDQ-_o5QPXog2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9118459d29.mp4?token=gwFcqZZ7pvcTkK6HAqrFF3xfil3wFOYcz3dbuLmEyJnuPZ6ufH9aQV0ajt9O3Li9KDa_yUMOnElO8PgEj8SCu9zacwm7rP5J1R9XkmYfWo51rUHV_sDGtp-smr_LdV-G1xwcrfnmfQ2BuBu1SQcEIZjxdcQ3uUaO3AjGFXsJvZUnc8rYBot9Uq86fADwnT9nYdwhfo1JPj1UX0Q4amDoWiWrolmfSoW54zwWRDMM7J_d4shsYN8O2Ae1-pPOCfdM1rU5Emt1MhXImr8QuGXfB1XihqGuhFCSWfC8BYBF3E3IbLVhMLjguWu6kZewjIx1HNrWr4ajDQ-_o5QPXog2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حکم اعدام بنیامین نقدی در دیوان عالی تایید شد
بنیامین از قهرمانان کیک بوکس بود و کلی مدال کشوری و جهانی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138688" target="_blank">📅 16:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت کنید.
۱. برای دریافت جایزه پول واریز نکنید
اگر به شما پیام دادند که در قرعه‌کشی، مسابقه یا جشنواره‌ای برنده شده‌اید، اما برای دریافت جایزه از شما خواستند مبلغی با عنوان مالیات، هزینه ارسال، کارمزد، فعال‌سازی حساب یا آزادسازی جایزه واریز کنید، به احتمال بسیار زیاد با کلاهبرداری روبه‌رو هستید.
برای دریافت یک جایزه واقعی نباید ابتدا به حساب یا کارت شخصی کسی پول واریز کنید. قبل از هر اقدامی، موضوع را فقط از طریق شماره تلفن، وب‌سایت یا صفحه رسمی برگزارکننده بررسی کنید.
عبارت‌هایی مانند «فقط چند دقیقه فرصت دارید» یا «اگر الان واریز نکنید جایزه شما لغو می‌شود» معمولاً برای عجله‌دادن و جلوگیری از فکرکردن شما استفاده می‌شوند.
🔴
۲. مراقب تبلیغات وام فوری باشید
بسیاری از آگهی‌هایی که وعده وام فوری، بدون ضامن، بدون چک، با سود بسیار کم و پرداخت در چند ساعت می‌دهند، ممکن است کلاهبرداری باشند؛ به‌خصوص وقتی قبل از پرداخت وام از شما درخواست پول می‌کنند.
کلاهبردار معمولاً از شما می‌خواهد مبلغی با یکی از عنوان‌های زیر واریز کنید:
- هزینه تشکیل پرونده
- هزینه ثبت‌نام
- کارمزد آزادسازی وام
- هزینه اعتبارسنجی
- بیمه وام
- مالیات یا حق تمبر
- خرید امتیاز یا افزایش رتبه اعتباری
- سپرده اولیه یا تضمین پرداخت
پس از واریز مبلغ، ممکن است دیگر پاسخ شما را ندهند یا با بهانه‌های مختلف درخواست پول بیشتری کنند.
برای دریافت وام به حساب شخصی افراد پول واریز نکنید و تصویر کارت بانکی، رمز پویا، کد پیامکی، اطلاعات حساب یا مدارک هویتی خود را برای افراد ناشناس ارسال نکنید.
وام را فقط از بانک‌ها و مؤسسات مالی معتبر و دارای مجوز و از طریق شعبه، وب‌سایت یا اپلیکیشن رسمی آن‌ها پیگیری کنید.
🔴
۳. برنامه‌های ناشناس را روی گوشی نصب نکنید
اگر فردی از طریق تلگرام، واتساپ، پیامک یا یک سایت ناشناس از شما خواست برنامه‌ای را خارج از فروشگاه‌های رسمی نصب کنید، بسیار مراقب باشید؛ مخصوصاً اگر فایل ارسالی دارای پسوند APK باشد.
این برنامه‌ها ممکن است به پیامک‌ها، تصاویر، مخاطبان، اطلاعات بانکی، رمزها و حساب‌های شبکه‌های اجتماعی شما دسترسی پیدا کنند. بعضی از آن‌ها حتی می‌توانند صفحه گوشی شما را مشاهده کنند یا کنترل دستگاه را در اختیار کلاهبردار قرار دهند.
برنامه‌ها را فقط از منابع معتبر مانند Google Play و App Store دریافت کنید. حتی در فروشگاه‌های رسمی نیز نام سازنده، تعداد دانلودها، نظرات کاربران و مجوزهای درخواستی برنامه را بررسی کنید.
هیچ بانک، اداره دولتی، پلیس، شرکت پستی یا مؤسسه مالی معتبری برای انجام کارهای بانکی از شما نمی‌خواهد یک فایل APK را از تلگرام یا واتساپ نصب کنید.
🔴
۴. فایل ارسالی از طرف آشنایان را بدون بررسی باز نکنید
ممکن است حساب تلگرام، واتساپ یا شبکه اجتماعی یکی از دوستان و بستگان شما هک شده باشد و کلاهبردار از طرف او برایتان پیام یا فایل ارسال کند.
اگر یکی از آشنایان برایتان فایلی فرستاد و نوشت:
- این عکس‌ها را ببین
- این آلبوم شخصی ماست
- عکس‌های عروسی یا مهمانی داخل این فایل است
- این فاکتور را بررسی کن
- این برنامه را نصب کن
قبل از بازکردن فایل، حتماً با آن شخص تماس بگیرید و مطمئن شوید خودش فایل را ارسال کرده است. فقط از طریق پیام سؤال نکنید، زیرا ممکن است حساب او در اختیار کلاهبردار باشد.
به نام کامل و پسوند نهایی فایل دقت کنید. کلاهبرداران ممکن است فایل‌هایی با نام‌های زیر ارسال کنند:
album.pdf.apk
photo.jpg.apk
invoice.pdf.exe
ظاهر نام فایل ممکن است شبیه عکس یا PDF باشد، اما پسوند واقعی آن APK یا EXE است. این فایل‌ها اجرایی هستند و ممکن است برنامه مخرب روی گوشی یا کامپیوتر شما نصب کنند.
🔴
۵. در سایت‌هایی مانند دیوار پیش‌پرداخت نکنید
برای کالایی که هنوز از نزدیک ندیده‌اید و فروشنده آن را نمی‌شناسید، بیعانه یا پیش‌پرداخت واریز نکنید؛ حتی اگر فروشنده بگوید مشتری دیگری دارد و باید سریعاً پول پرداخت کنید.
در یکی از روش‌های کلاهبرداری، کلاهبردار هم‌زمان با شما و یک فروشنده واقعی ارتباط برقرار می‌کند. سپس شماره کارت فروشنده واقعی را در اختیار شما قرار می‌دهد تا پول را به آن حساب واریز کنید.
شما تصور می‌کنید پول کالای موردنظر خود را پرداخت کرده‌اید، اما فروشنده واقعی تصور می‌کند این مبلغ بابت خرید کلاهبردار واریز شده است. در نهایت کلاهبردار کالا را تحویل می‌گیرد و هم شما و هم فروشنده واقعی متضرر می‌شوید.
برای جلوگیری از این مشکل:
- تا قبل از مشاهده و بررسی کالا پول واریز نکنید.
- معامله را در محل امن و به‌صورت حضوری انجام دهید.
- مطمئن شوید نام صاحب حساب بانکی با نام فروشنده مطابقت دارد.
- دلیل پرداخت را در توضیحات انتقال وجه بنویسید.
- از روش‌های پرداخت امن و مورد تأیید همان پلتفرم استفاده کنید.
- به رسیدهای بانکی ارسالی اعتماد نکنید و حتماً موجودی حساب خود را بررسی کنید.
🔴
۶. کد پیامکی و اطلاعات بانکی خود را در اختیار کسی قرار ندهید
هیچ‌گاه اطلاعات زیر را برای دیگران ارسال نکنید:
- رمز کارت بانکی
- رمز پویا
- کد پیامکی ورود یا تأیید
- رمز اینترنت‌بانک
- اطلاعات ورود به شبکه‌های اجتماعی
- تصویر کامل کارت بانکی
- کد بازیابی حساب
- کد فعال‌سازی واتساپ یا تلگرام
بانک، پلیس، پشتیبانی سایت‌ها و شرکت‌های معتبر هیچ‌وقت رمز، کد پیامکی یا اطلاعات محرمانه شما را درخواست نمی‌کنند.
اگر فردی گفت برای واریز پول به حساب شما باید کدی را که پیامک شده برای او بفرستید، به هیچ عنوان این کار را انجام ندهید.
🔴
۷. به لینک‌های ناشناس اعتماد نکنید
کلاهبرداران ممکن است لینک‌هایی شبیه سایت بانک، سامانه دولتی، شرکت پستی، سایت پرداخت جریمه، ثبت‌نام یارانه یا دریافت بسته برایتان ارسال کنند.
قبل از واردکردن اطلاعات بانکی، آدرس سایت را دقیق بررسی کنید. تغییر یک حرف، عدد یا علامت در آدرس می‌تواند نشان‌دهنده یک سایت جعلی باشد.
برای ورود به سایت بانک یا سامانه‌های مهم، خودتان آدرس رسمی را در مرورگر وارد کنید و از لینک‌های ارسال‌شده در پیامک یا شبکه‌های اجتماعی استفاده نکنید.
🔴
۸. اجازه دسترسی به گوشی یا کامپیوتر خود را ندهید
بعضی از کلاهبرداران به بهانه پشتیبانی، آموزش دریافت وام، رفع مشکل بانکی، سرمایه‌گذاری یا دریافت جایزه از شما می‌خواهند برنامه‌های کنترل از راه دور نصب کنید.
پس از نصب این برنامه‌ها ممکن است بتوانند صفحه گوشی شما را ببینند، پیامک‌های بانکی را بخوانند، وارد حساب شما شوند یا انتقال وجه انجام دهند.
به افراد ناشناس اجازه مشاهده صفحه، کنترل گوشی یا اتصال از راه دور ندهید.
🔴
۹. مراقب پیام‌های فوری، تهدیدآمیز یا وسوسه‌کننده باشید
پیام‌هایی با مضمون‌های زیر معمولاً مشکوک هستند:
- فقط چند دقیقه فرصت دارید.
- حساب شما مسدود می‌شود.
- بسته پستی شما توقیف شده است.
- برنده جایزه شده‌اید.
- این موضوع را به کسی نگویید.
- برای آزادشدن پول باید کارمزد پرداخت کنید.
- سود تضمینی و چندبرابری دریافت می‌کنید.
- ظرفیت وام فقط امروز باز است.
- کد پیامکی را سریع برای من بفرستید.
کلاهبردار تلاش می‌کند فرصت فکرکردن و مشورت‌کردن را از شما بگیرد. هر زمان احساس کردید برای تصمیم‌گیری تحت فشار هستید، هیچ اقدامی نکنید.
﻿
🔴
اگر با مورد مشکوکی روبه‌رو شدید
🔴
پول واریز نکنید، روی لینک کلیک نکنید، فایل را باز نکنید، برنامه‌ای نصب نکنید و کد پیامکی خود را در اختیار دیگران قرار ندهید.
🔴
ابتدا با یک فرد مطمئن مشورت کنید و موضوع را از طریق شماره تماس، سایت یا صفحه رسمی مجموعه موردنظر بررسی کنید.
🔴
اگر برنامه مشکوکی نصب کرده‌اید یا اطلاعات بانکی خود را در اختیار فردی قرار داده‌اید، سریعاً اینترنت گوشی را قطع کنید، با بانک تماس بگیرید، کارت و دسترسی‌های بانکی را مسدود کنید و رمز حساب‌های مهم خود را از یک دستگاه امن تغییر دهید.
🤔
به یاد داشته باشید: کلاهبرداران از هیجان، ترس، طمع، اعتماد و عجله استفاده می‌کنند. چند دقیقه توقف و بررسی می‌تواند از خسارت مالی و سرقت اطلاعات شما جلوگیری کند.
#امنیت
#کلاهبرداری
#کریپتو
#وام
#دیوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138687" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JouFbVHB-gNLaHjwobe1CvE-V4Sf1Sy5tK_zBM3LIqzDaal8Uo8Fuagzstp1Dl160RJcuyF84nMJ5dd__1W341ClsiKzJGgll-hpiB39Wfs2HvaYbhkeFDKAS7V3NYaB261VNG3-6FWt47zX0hdwDvq4ESap5MY_2coL37uXU__V3g11AcT_iLxOK3VI74Cg2tUuRhJBX35wwEptI_LiK59HsgVjtJQWd46NpipS3LqVQB_6XEz9lKoWssMeDNt_XRnZ0lMQeNHoB7-E0Cyz1xJFjWYHabQOejdzCgK_j8fbABS6pYhhCAyIEgI193okqLeT07Cfb3B4JmO8Gq2SNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVqWXIxeUQmv42DvkBYCIcCmra-NyDLr-jsg89IQtja7RhNoTYPFukanPuP0__tJcxGHExx5Vs-fKK8fRfJmxqwnbpyZxNV9SukjC1jeBOTf9ysrzfADZnJ5vZp3qlxNqP9S5-mbjQVxK0m1yVoEYlzlsjTQW0CXTb_tdGviqmLdpVcTiwvJIQFBLZd8zb80OdVJbIMfpsVVL_UQyjamx2qS5zx972oq4TYsn0gvxfu8yQTq7RpCNdEHsOjYYIL5VaE2LkdIZy3ZykSIUXzS2nrqPiheXaIDzAPH7diTTSo4wdNkltmLZecovgX1PXyzgBCIpu61QuVCQ2JdTlzGcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjPcVqjJwMJAymLxBTDy3VXxM468Qj7EzjnQXsF8MLYvhKa8ybv8weTiNsl3BmP6pjmYwGHD3EPM2BcbsvZeh8g8beyXTrswIIqfXK-OUNFe4lrSdawnxO2IwIGOhdZoNDuW8qV-zR52_lqKZeoPsoD5I8qsXnH1ecnWh8e39cLyudkKI6Lhm2Zs-eVcqCMG1OBAQOMcFimt5Qw8we0eSrJhFeMRxj3vJKmoBgZIARmj3bojJ6mCQieJjAW2l4kyzo15hfCmXy0Z9Wa9cIUBU_4IqlFUH2cmNPBpFpo_wv4i1ZI4UVK4Rt1ptBuyoiRH0MjmDS7mbtuJ_oCTBkufmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرود چندین فروند هواپیمای آمریکایی در پایگاه هوایی عیسی در بحرین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138684" target="_blank">📅 15:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzoLF8MIbPFmJPUJ1Lyr6SzDE1dnGRyAii-7YaOhpdOrOR9w9lCT-3m3jDF0baeyzw_yKgG1g--JwGzMREQGB_wx7-i3jWQMA6rAzdT_lARuN-AQZUM3KDLdp-96XdG2H1x2Orw0evKCvg6URXO2HigXnoaDbRq2SlwHPQRcwxfZ3cmChV2rPfp4R1DKj3CwtXrAx9bF4hi0GumNjqGeTmfo7FNb02D_4Hz_huV8PouwyZkXWdu6bR_U1e-c6DyyJw2Ehak6QQya2voxqogZAk1K7r3rjB0buw755-OI_c9oBrKWkewgt1LvpVlWxYVoW50mC0-2w6nWY-Q3r-VjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرا نمیتونم راجب این ۳ نیروی حشدالشعبی فکر مثبت کنم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138683" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138682">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت برق فرانسه (EDF) راکتور هسته‌ای «گلفش-۲» در جنوب این کشور را در پی موج شدید گرما از مدار خارج کرد.
🔴
دمای هوا در بخش‌هایی از اروپا در حال نزدیک شدن به ۴۰ درجه سانتی‌گراد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138682" target="_blank">📅 15:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138681">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نخست‌
وزیر لهستان :
دلیلی نداریم فکر کنیم لهستان هدف بوده؛
🔴
اما دو شیء وارد حریم هوایی لهستان شدند
🔴
یکی قطعاً این کار را کرده و مدرک داریم؛ دیگری هم مدت کوتاهی به مرز نزدیک شد و پیامد خاصی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138681" target="_blank">📅 15:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138680">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGnLtFkQHX-su7jLPCZFpHakA9LPa-tLKMkrAy_sSuZyXB2_HndCsEyawKjF4x_-I36qWmcAvzfYbiB3H-3FYf0WYKOexw1sB60rc1c7HI5Y3YwRZxql02_yQ0WYGb4JFFZcTNox6ThFCAwvAxXZzdNPkVqejpxWDWwwuIygb0a3SbicGcYEVsgs2rLlHS31e6p1xRT8ghyBoUm7IKshZx0iHvGv6ADOmu0sumv2UE6WHVuhAiz25wxUGJMDVNs7GpSUSfCNKUi1jrHKFtPXBNjVR3enRQ-39p1eHR3h0omNFL28CTsUkPILQSs-v9THHhuwptMJKIHL4hSY3UYuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی نماینده مجلس: استانهای دونتسک، لوهانسک، زاپوریژیا و خرسون و نیز کریمه را به عنوان خاک روسیه به رسمیت بشناسیم!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138680" target="_blank">📅 15:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138679">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بلومبرگ، پاکستان با ایران مذاکره کرده است تا عبور امن حداقل یک محموله گاز طبیعی مایع (LNG) قطر را از طریق تنگه هرمز تضمین کند
🔴
نفتکش حامل گاز طبیعی مایع «العارش» که از اوایل ژوئیه در خلیج فارس منتظر مانده بود، تحت این توافق از تنگه هرمز عبور کرده و اکنون در مسیر پاکستان قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138679" target="_blank">📅 15:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
به گزارش اکونومیست، بخش‌های قابل توجهی از توافق آتش‌بس میان ایران و آمریکا عملاً کارایی خود را از دست داده است.
🔴
این نشریه افزود حتی اگر دیپلمات‌ها راه‌حلی پیدا کنند، احتمالاً این اقدام تنها ترمیمی موقت برای توافقی خواهد بود که از ابتدا نیز شکننده بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138678" target="_blank">📅 15:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2eXqRwd4g626KtVyv1iy4jlvOAgx9AKlbuSbE5c4cjap_C7TG8SNaaqZiuf_laqkRZkvxow9ago2h4M_kWmno6GGr9YlsOzelp0kVsxf554Rwf9biyfZS5HXmZYKKtn_xM2_HZZAlGN-6GPkPgMSc_yiYzp0P91vUV9Nh1wCXU-uTtzLE5Btuh99efTuAtvCZOPdO4JzE3jKLOuhzEvoPBUqsHVwbHoD5Wn34jo6XDvLaakwX2u_AfhFLKSsn2W1gOOLI_CbSgUwGIBaXhszRXiphdECazg4wnVmpEJtwdqIajZcJ-_DfS7sJUG6MYs-EE2VIzG5RODkOl6X68QPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: امروز صبح 6 تا جنگنده زدیم
🔴
3 تا F35 رو منهدم کردیم و به 3 تا دیگه خسارت زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/138677" target="_blank">📅 15:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138676">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd1748f78.mp4?token=vrfnFhT1M_eo1xRUzoDpYNFIefedz2ceyqu-dNlveS0iVBSYw_T2SF-eQ7yFdJIlzrQOb9Q9Bu7hlZqChSsZ8gWFPjUfCvTC9TTN2oelfqmq2bjclriymJLQeOMoSjBeZNsPgNnSxF9CSKzUZXiT8ncnhCTTQ-N-NG5HpaYCb7lFgvduUvBx1fQAhmQl4epJI2IXrjwJ-UcF0S9MUtd2gxTxI14KkbiWsl9RncKnjPhjOwrKkw8C5lrQgVKiGljp4-J7tAFkMYCf6NGww7iYkB_M-NOS0CaPHmc1XuL8mZYLKRchqmvHaFFTvgIiqb66WYJpexMA4meKXzsducDe0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd1748f78.mp4?token=vrfnFhT1M_eo1xRUzoDpYNFIefedz2ceyqu-dNlveS0iVBSYw_T2SF-eQ7yFdJIlzrQOb9Q9Bu7hlZqChSsZ8gWFPjUfCvTC9TTN2oelfqmq2bjclriymJLQeOMoSjBeZNsPgNnSxF9CSKzUZXiT8ncnhCTTQ-N-NG5HpaYCb7lFgvduUvBx1fQAhmQl4epJI2IXrjwJ-UcF0S9MUtd2gxTxI14KkbiWsl9RncKnjPhjOwrKkw8C5lrQgVKiGljp4-J7tAFkMYCf6NGww7iYkB_M-NOS0CaPHmc1XuL8mZYLKRchqmvHaFFTvgIiqb66WYJpexMA4meKXzsducDe0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین در مورد رویکرد اخیر یک شناور بدون سرنشین ساخت آمریکا به یک کشتی جنگی چینی: نیروی نظامی چین فعالیت‌های خود را مطابق با قوانین بین‌المللی و عرف بین‌المللی انجام می‌دهد.
🔴
ما توصیه می‌کنیم از نزدیک شدن خطرناک به کشتی‌های جنگی چینی خودداری شود تا از بروز حوادث ناخواسته هوایی و دریایی جلوگیری گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138676" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138675">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سپاه : تو آسمان بندر امام پهپاد زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138675" target="_blank">📅 15:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfuloE7MFy1hygXhdMAsPWn6c0XAba9JbdfnPJ2pz44e9zur1HMoGwgwmM7KnjupmsIFAU4zVcf-wZO2KhZWB6FIzpEL-SLZSk7mx9uXmfJMnbrFffAyOtA47prbkSBz7K36WwOysQO9YllV5SLAkWbBfmgKMD8TvjyQTVqgssfM9zJJHtGjEVyoIazyopQY5JsbQvW-2LWKUTK2uYoWAuY-4jL80hVg9CfBGV7CViYGl-zLKSg-W0lxAYxvASqbBcpqflCFbxq-vDoUjpkkXwGx9p7e_ejR73669Xjve7hNvr-2RQeYad0V97rX5Xr73XMLlABc9ysHiBC8l_wXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ از عدم پیشرفت در زمینه پایان دادن به جنگ با ایران و اختلاف‌نظرهای موجود در دولتش ناراضی است
🔴
برخی از مقامات از ادامه عملیات نظامی حمایت می‌کنند، در حالی که برخی دیگر هشدار می‌دهند که حملات طولانی‌مدت می‌تواند ذخایر تسلیحاتی امریکا را کاهش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138674" target="_blank">📅 14:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ایران: مذاکرات با عمان درباره مدیریت تنگه هرمز همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138673" target="_blank">📅 14:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
صدها چهره سیاسی، حقوقی و عمومی اردنی نامه‌ای سرگشاده امضا کرده‌اند که در آن به خروج نیروهای ایالات متحده از اردن فراخوانده شده است، با این استدلال که حضور نظامی آمریکا حاکمیت کشور را تهدید می‌کند و خطر درگیری عمیق‌تر آن در درگیری منطقه‌ای را افزایش می‌دهد، به گزارش نیویورک تایمز.
🔴
نامه بیان می‌کند که حضور سربازان ایالات متحده «اردن را در معرض خطرات امنیتی، سیاسی و اقتصادی قرار می‌دهد» و احتمال کشیده شدن کشور به جنگی را که «در آن طرفی نیست» افزایش می‌دهد.
🔴
برخی از امضاکنندگان گفتند که می‌خواهند افکار عمومی را از سیاست خارجی دولت متمایز کنند که با وجود تنش‌های فزاینده منطقه‌ای، روابط نزدیکی با ایالات متحده حفظ می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138672" target="_blank">📅 14:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رویترز : دو تانکر نفتی که حامل نفت عربستان سعودی به سمت هند هستند، از دریای سرخ خارج شدند. این خروج با خاموش کردن دستگاه‌های ارسال و دریافت سیگنال انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138671" target="_blank">📅 14:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فارس : کشتی کانتینری نورا از خط محاصره آمریکا گذشت و وارد آب‌های آزاد شد؛ این کشتی پیش‌تر در نزدیکی قشم دیده شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138670" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سپاه : در پاسخ به حمله آمریکا به قشم؛
با حمله موشکی به پایگاه الازرق، ۳ جنگنده F-35 رو منهدم و به ۳ فروند دیگه خسارت سنگین وارد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/138669" target="_blank">📅 14:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f178e085ff.mp4?token=lQt8P6fPUxWgcxMoa31ldE5TWsXJNNoQ4wuFO9Kb_91SHy7LmAw-k-ODm3l_F3mp8xNrWmih9xtAszPZyrkNVfEQZVsnxrrj9vryIbqrsmEgEzMI3s1EHeFL2coIIwTuSpm_cmk0j7hch-BgcLC1JEJn1O_alzR8XHmI26IKzdvL85qkRkuGgCt2pcqzlzc4kcyxyZzXGOshC8E1dlsiAIhj9SwLEfkmUev3awEnrrJr6tUtyzgF--6v3OLJ1-yI6qmYBwRRC4jrOOeRUdUfClQXExG_BJx8iWWajLljZX5eED_W99nRJIFhtWVcyuDYaERlumjS4hAZnuYPZTuBfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f178e085ff.mp4?token=lQt8P6fPUxWgcxMoa31ldE5TWsXJNNoQ4wuFO9Kb_91SHy7LmAw-k-ODm3l_F3mp8xNrWmih9xtAszPZyrkNVfEQZVsnxrrj9vryIbqrsmEgEzMI3s1EHeFL2coIIwTuSpm_cmk0j7hch-BgcLC1JEJn1O_alzR8XHmI26IKzdvL85qkRkuGgCt2pcqzlzc4kcyxyZzXGOshC8E1dlsiAIhj9SwLEfkmUev3awEnrrJr6tUtyzgF--6v3OLJ1-yI6qmYBwRRC4jrOOeRUdUfClQXExG_BJx8iWWajLljZX5eED_W99nRJIFhtWVcyuDYaERlumjS4hAZnuYPZTuBfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ارتش روسیه ویدیویی از هدف قرار دادند 3 کشتی تجاری اوکراینی توسط نسخه هدایت شونده گران ۲ در نزدیکی بندر اودسا منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138668" target="_blank">📅 14:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اتحادیه خط لوله دریای خزر (CPC) اعلام کرد که یک نفتکش در حال بارگیری نفت در یک ترمینال شناور متعلق به این اتحادیه هدف حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138667" target="_blank">📅 14:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سپاه المهدی : تو حمله موشکی آمریکا به زنجان، ۳ نیروی سپاه کُشته شد
🔴
جمال امیری/ محمدرضا چراغی/محمود ملاجابری
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/138666" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138665">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7319df0d.mp4?token=Sbp7OTLcPA7pACGq5tKm1mMkjXSfE8K0qsGWfx2FeOmypYbt_KiwZ4Knevuadmp_4CGrj5Lz3nNl1FrbsfU6gcFJ1axtfAIZzKfKZXlpKvOenWonVBoEeVa7V1SyNe6M04vuK9bDC73mVwIDsaRaKMkKbbfD9jjW4ZxwXfI0GRKFzQ-1Pr5elrVznU9Zba-7dnnxHbV-9tjVsHFmgFT-_ohdVvjicYScp12prrKgTybs_sHKlshDikgMS8_XViihGW6JsL-nNw9OMyBeT3knC_K3BHNN2nexaLIJcwwHCoVv0TLbvMY5G5kZjWUkq3dRVlUDDshvch0IZwjCdhlnGkCuddC068mBwoAMvEa6KJpz0ITqKXLKWVc_P0A3te4X7pMwglkeQQXitF1Jlu80q7tIkddWDoXhX8UY8NnuD3tMMQSB3XnuY9yH7yESCrDKRdjRNm2eCzQ_PyXQjifB-PpoAacqRIf8A9uW6dV38TRJRfc3slyWGM2x1dPXG4PpgsrUATvnl-9Ylj3CP7HM7D-2ozYJRcLDc0zQ3-Dx1G_8Udvu7s9MLzfFDLSURXTxkMFRwrrkNpXYV6FXUMSef9IhURcECYSdLd_pe2t6mIeFq9fm0DQ38b8FWqHg7Y2voyuyMfyM7xR9CPqaPrwU5uKN6HMLghI4UcrTbS3OAxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7319df0d.mp4?token=Sbp7OTLcPA7pACGq5tKm1mMkjXSfE8K0qsGWfx2FeOmypYbt_KiwZ4Knevuadmp_4CGrj5Lz3nNl1FrbsfU6gcFJ1axtfAIZzKfKZXlpKvOenWonVBoEeVa7V1SyNe6M04vuK9bDC73mVwIDsaRaKMkKbbfD9jjW4ZxwXfI0GRKFzQ-1Pr5elrVznU9Zba-7dnnxHbV-9tjVsHFmgFT-_ohdVvjicYScp12prrKgTybs_sHKlshDikgMS8_XViihGW6JsL-nNw9OMyBeT3knC_K3BHNN2nexaLIJcwwHCoVv0TLbvMY5G5kZjWUkq3dRVlUDDshvch0IZwjCdhlnGkCuddC068mBwoAMvEa6KJpz0ITqKXLKWVc_P0A3te4X7pMwglkeQQXitF1Jlu80q7tIkddWDoXhX8UY8NnuD3tMMQSB3XnuY9yH7yESCrDKRdjRNm2eCzQ_PyXQjifB-PpoAacqRIf8A9uW6dV38TRJRfc3slyWGM2x1dPXG4PpgsrUATvnl-9Ylj3CP7HM7D-2ozYJRcLDc0zQ3-Dx1G_8Udvu7s9MLzfFDLSURXTxkMFRwrrkNpXYV6FXUMSef9IhURcECYSdLd_pe2t6mIeFq9fm0DQ38b8FWqHg7Y2voyuyMfyM7xR9CPqaPrwU5uKN6HMLghI4UcrTbS3OAxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از رهگیری پهپاد روسی تو آسمون اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/138665" target="_blank">📅 13:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138664">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIe4kaq0mIYCbTBlj7RWF8z2w2q_T1NN8J_UBa6rryvxEmBx37QyHn4e3_4gj42cLfCo_trYBfSwKfYyp6VC8MJ1MmiGrlY0480ncoxhqoWTGQbT1_20digLvdj4KysWgcJ0avGlH4fK2pgFAANs6asR6u7O-By8-PhHzzYeBnN1x5rM8SQ4z9BTy3LSHwUsC7GFturwOuCPdQTwsUdrxhBeuREb_W5QfZRqgXZtAQ0ceMOSKdLmLs1u0qACxB8F6CDodrTohfwA3upwI3dX5P9Sf4_h1Z8oy7-ZZ3x8XIgPOVsbtqmdpUH0F9_P-m6qBUzvmVBSwLyqBg7QQoBy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهار کشتی نفت‌کش/گاز‌کش از تنگه هرمز عبور کردند و از مسیری که ایران تعیین کرده بود، استفاده نمودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/138664" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزارت دفاع روسیه : لجستیک دریایی اوکراین، در حال فروپاشیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/138663" target="_blank">📅 13:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138662">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae07c4c25.mp4?token=KPTo-ZrUoD-WPQSNykuA9OkPRhTNaXG6CfjABcfzPSbH-8TeC5QkYM984QVDjccKCGocGiIFAO-O3Eh0jj1YY_8OcX2F3tpbNQ0x5QkfxymZuqrFx0cqvjsrtq_KC85mexSiJU-JSQqfkJoDjMUN3U_GQANZoGsuJKt0dhIn89pG8LLi8GFzV6XaAHHWivAfTR6UEhCmkUvnl0ttIm8NCJaHQCTqQL67F8ySkQxY_-UlQEUsS1nzTBv5EvSRjYYMpcaZUEZPDZ8dd6XuP-CK34jL1cugtwiIf3jWX_Xfubs4DrSFHLmLO2LLeJBT6--rsfgIHbl6GLjWakN6K1qXHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae07c4c25.mp4?token=KPTo-ZrUoD-WPQSNykuA9OkPRhTNaXG6CfjABcfzPSbH-8TeC5QkYM984QVDjccKCGocGiIFAO-O3Eh0jj1YY_8OcX2F3tpbNQ0x5QkfxymZuqrFx0cqvjsrtq_KC85mexSiJU-JSQqfkJoDjMUN3U_GQANZoGsuJKt0dhIn89pG8LLi8GFzV6XaAHHWivAfTR6UEhCmkUvnl0ttIm8NCJaHQCTqQL67F8ySkQxY_-UlQEUsS1nzTBv5EvSRjYYMpcaZUEZPDZ8dd6XuP-CK34jL1cugtwiIf3jWX_Xfubs4DrSFHLmLO2LLeJBT6--rsfgIHbl6GLjWakN6K1qXHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی بزرگ در یکی از انبارها در مسیر اربیل - کرکوک
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/138662" target="_blank">📅 13:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwFnxytaUcfyXrTmjIaSKcOMzUDhCOgNONMV50zZ6QBonl0m6Ob97Gqzj_v--k6kycm62UQ6J5r0ru1o7U1e1udTGi2yjLTdElL46imm9URKn4eUTJoa_MMPBNOKjIddNCOL5N4GsD1nkdczehV7w7T-IrRHtoFH7u5ydaTMA2zZqJhvOMmHCfY08UJdQ1f3vXvG5eF6aNl6xDEj5DS5WHLJ939mX2RcxKGyTq1Pp4T1WQZL9K8qHVpqOc6xuETxdor6f4TRbUIsVmazA10_iI8cWi2Jq7w0rNWNrbNS_LbdN7CgS0SwnSN6xG58j8HP38v8taWBkswzjSZD8U_3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله کارشناس صداوسیما به وزیر امورخارجه به دلیل جلوگیری او از حمله به اوکراین: هر ثانیه حضور عراقچی به عنوان وزیر، خسارت محض برای منافع کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138661" target="_blank">📅 13:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a7dcb61f.mp4?token=Xo5D6g7L5G37O4dc2CeQN_1t7xhF2k-ArnDe4HctmGZKI3SQCKgAl2jSqGvr3TQL8EpOsKL_w2RzJ5zUSX-cGBt0zTYELjvPWUHkQvPR4qcrcM3KIzK5KIA2N040SnWUFQ-ROXUJiR0ol1HZFyS2y3G4GjzI5xY_S_2nNMks6fSysPWTV1v6iimw87HJwaAKguRmLjthZZFKKNsU2fzIj95ot83CwFDFP_uLmk_Cezmrp1CYe6I_n67MLEowKTUiL6rVFXoNSymjDDhHLaZ3LIE17V0x66evjVe23YAC69odz1k_HDp_eJ06Ij01iSulQ0RS5-u5kyDScMjKFKKVtjt7AlWBmMzkqSwYqHLTMCtfRmFIGOtUL06T0SZVy5zAkaYawxeOJkkBM02kLcu116oOMAgVyX17lqw_0bamEq9h7uUlo0uAFmXBlsX_oSzWlEPyhXqJ_v4IIb_j0zt-XzRfDi22c6yQDJdKdERK6grhnAUwTLJeqCw2puCKwPbwKiMapsrMutO_OQ03dKRwE4QhUqwxBsSIY3h3kF6Y7tbOmLAdaDOnyezOjQe83qkx7rOy9aBgDj4iZNZmerDl_7YREoT6ULsNrSSxauLaLUHkX3iUyAqG8T31bNINmj41kDc9GWP6zwncgeucjXi6bx5u7FK0e6Oda7uQ43S5ptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a7dcb61f.mp4?token=Xo5D6g7L5G37O4dc2CeQN_1t7xhF2k-ArnDe4HctmGZKI3SQCKgAl2jSqGvr3TQL8EpOsKL_w2RzJ5zUSX-cGBt0zTYELjvPWUHkQvPR4qcrcM3KIzK5KIA2N040SnWUFQ-ROXUJiR0ol1HZFyS2y3G4GjzI5xY_S_2nNMks6fSysPWTV1v6iimw87HJwaAKguRmLjthZZFKKNsU2fzIj95ot83CwFDFP_uLmk_Cezmrp1CYe6I_n67MLEowKTUiL6rVFXoNSymjDDhHLaZ3LIE17V0x66evjVe23YAC69odz1k_HDp_eJ06Ij01iSulQ0RS5-u5kyDScMjKFKKVtjt7AlWBmMzkqSwYqHLTMCtfRmFIGOtUL06T0SZVy5zAkaYawxeOJkkBM02kLcu116oOMAgVyX17lqw_0bamEq9h7uUlo0uAFmXBlsX_oSzWlEPyhXqJ_v4IIb_j0zt-XzRfDi22c6yQDJdKdERK6grhnAUwTLJeqCw2puCKwPbwKiMapsrMutO_OQ03dKRwE4QhUqwxBsSIY3h3kF6Y7tbOmLAdaDOnyezOjQe83qkx7rOy9aBgDj4iZNZmerDl_7YREoT6ULsNrSSxauLaLUHkX3iUyAqG8T31bNINmj41kDc9GWP6zwncgeucjXi6bx5u7FK0e6Oda7uQ43S5ptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/138660" target="_blank">📅 13:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhTw-d84NUTBYEn5hIA72Yp4wcsuK9jxWKyaIYDU1E6p4LshPlRtwfZ6AZTQP460jhsXr7c6xJt8JfdlwCLicCbMckLSEZ3Cr55PGWoKgB2YBc1KhTVsgzC74BaX1l55CAGyLmTiLqiZEWdkaK5Ua7KywlcI5F5Sxe5H8Qfguhl7Ih7WCIswJ8nJim7jVhovje6S1TpYxe-MGpJxCd92_iWPgS17iavfF3TT3TxdrAnVNwlEQRT9WNVLk45f_H_CeKuyGA1XUC3XXyoD-J1R26BVCeO3LDXTgb_17vBcHtdWYJ0frmKdbvMe4Tnl3hDSl2FYtHEUwQe0b7d8tz8IWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عطوان تحلیلگر جهان عرب: حشدالشعبی وارد جنگ شود، پایگاه‌های آمریکا در منطقه دوام نخواهند آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/138659" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از فرمانده ستاد فرماندهی مرکزی ایالات متحده نوشت: "ما طرحی برای یک کمپین هوایی قدرتمند علیه ایران آماده کرده‌ایم که می‌تواند تا دو هفته ادامه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138658" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138657">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العربیه: تلاش‌های میانجی‌گری تاکنون به نتایج ملموسی در زمینه توقف تنش‌ها بین آمریکا و ایران منجر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138657" target="_blank">📅 12:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138656">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfe0b1f3c.mp4?token=BkOm_QAOhuKrj--6WXH3-qAVHs8s0tasGWzx2F1riPkgwWO3zOlYdfm7UrDidlmVk1KXgT06GyZqrfnWk6FSNkk9E3oQGBlM3BWMIy9TT2j5M5tLfZe8Z6xOpl06Q_3sJOFLPOG1kU3yVTdzjOU9k55Nq7DozSKPLbHxzYKv3oGqPyz2Rl2KFggHxaCZQb4Hor4Ywn2kqisCI4rANodY3EWcAclGxL9_oWvyJnPzB_ZSA63vSbJ3ndXiIKy5zIyxJNeR0tnf8SWzFK2gwscr8E-e92clayMLWJVjZFYlaYBz5pTnKw0cnBrTAiSjKTFt1_CUHQe8879Rb-OTTjWgYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfe0b1f3c.mp4?token=BkOm_QAOhuKrj--6WXH3-qAVHs8s0tasGWzx2F1riPkgwWO3zOlYdfm7UrDidlmVk1KXgT06GyZqrfnWk6FSNkk9E3oQGBlM3BWMIy9TT2j5M5tLfZe8Z6xOpl06Q_3sJOFLPOG1kU3yVTdzjOU9k55Nq7DozSKPLbHxzYKv3oGqPyz2Rl2KFggHxaCZQb4Hor4Ywn2kqisCI4rANodY3EWcAclGxL9_oWvyJnPzB_ZSA63vSbJ3ndXiIKy5zIyxJNeR0tnf8SWzFK2gwscr8E-e92clayMLWJVjZFYlaYBz5pTnKw0cnBrTAiSjKTFt1_CUHQe8879Rb-OTTjWgYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه دستگیری فردی که برای جاسوسی به
ایران
متهم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138656" target="_blank">📅 12:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138655">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نتانیاهو: ترامپ درباره ایران سه گزینه پیش‌رو دارد؛ توافق، ادامه محاصره دریایی یا تشدید جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/138655" target="_blank">📅 12:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138654">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbc8eae3d.mp4?token=gktJuUhpcagD6HwnkgcUU5g5hg0hEWMx_eYlK_km_9AFIH_bYdY1rARgjPZX7ivlZoHiWVLQqvqlvdWLMi8BwzIuKi11t1RenaNL_DcECmh5HeY93sU-vYlcSpbf_C70aAWm4ZZ3Ie0P4TZRAXNYggikyJ8S4441kUaMjZZvI_T00zDJg3hoWev40vMuhHAiNVdxhF0HVgkAzvrVPaRIz6FcNf0uiGRI8YAlGTBupcjntfdbrKBB1s9oHaxuKiNaUPRE1mk50K7ugzTgedwFDeX-onHol6vwzyENsIkqbl0Szj0q0WTL1inqEqArZddldpVXZfV7duQ-D-e0WNbOhb0IYIuMCqMRStcuNHfKAAJ2PAsp8owZUWL2hwfbEDhQcGR94yscPLUr6ItHe0xiz8czRhKBSbJUjv38Pw8x1fneipBFsAgrI1NgxE4Tdpa7eLD9Co6_Ba8z098yDWX2HSMUNEFxzyhSiKmY_gLvug7HOlcbACBu7U8J4yjHW4XAXuAujzyrcbKnu35KzeW37u-CgCCvLNeL-bhPNEgDNoOWNscivMOViUxgGAcCYZ8H4ynjcynFvPTym6sh-1PFTlidrzx070KoFw7Zp0PaDWJd_hsBtk_6UZI5VikoyltUBxfIitG4fmZVcbZJ67sbmsHOOeqsNLwttm_XFDvAJ4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbc8eae3d.mp4?token=gktJuUhpcagD6HwnkgcUU5g5hg0hEWMx_eYlK_km_9AFIH_bYdY1rARgjPZX7ivlZoHiWVLQqvqlvdWLMi8BwzIuKi11t1RenaNL_DcECmh5HeY93sU-vYlcSpbf_C70aAWm4ZZ3Ie0P4TZRAXNYggikyJ8S4441kUaMjZZvI_T00zDJg3hoWev40vMuhHAiNVdxhF0HVgkAzvrVPaRIz6FcNf0uiGRI8YAlGTBupcjntfdbrKBB1s9oHaxuKiNaUPRE1mk50K7ugzTgedwFDeX-onHol6vwzyENsIkqbl0Szj0q0WTL1inqEqArZddldpVXZfV7duQ-D-e0WNbOhb0IYIuMCqMRStcuNHfKAAJ2PAsp8owZUWL2hwfbEDhQcGR94yscPLUr6ItHe0xiz8czRhKBSbJUjv38Pw8x1fneipBFsAgrI1NgxE4Tdpa7eLD9Co6_Ba8z098yDWX2HSMUNEFxzyhSiKmY_gLvug7HOlcbACBu7U8J4yjHW4XAXuAujzyrcbKnu35KzeW37u-CgCCvLNeL-bhPNEgDNoOWNscivMOViUxgGAcCYZ8H4ynjcynFvPTym6sh-1PFTlidrzx070KoFw7Zp0PaDWJd_hsBtk_6UZI5VikoyltUBxfIitG4fmZVcbZJ67sbmsHOOeqsNLwttm_XFDvAJ4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اضهارات نویدِ زیادخان:
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/138654" target="_blank">📅 12:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دولت عراق در بیانیه‌ای اعلام کرد که هیچ مدرکی مبنی بر آغاز حملات به عربستان سعودی از خاک عراق پیدا نکرده است و از عربستان سعودی خواست تا مدارک خود را ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138653" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/452945470e.mp4?token=MER6z5pgGHqm1XFvsutXKiZkbeO1vm4AtN3w9AmTHC6iRIqTfOlI1l5guysKeMuu5PunN-q-aKHm8tdTEfMVYRay-o7jwQSWGrVAPs8UJ_V5ajTEl04GkMsWR9DDhcyM1VnbLtT8IHl_nIjxbFrgJ9b8EDOuwcejt0LFikBqNDZm8anrw_MpZc08IOVlUGO7f4eiNffwmyXwbmpq9vcwYxzO1S-vomrsY6mSemxHJYK03W6qqmXeZL145zxrT4JKnsi4OtFOnDvyka7UF8S7rni42vjoK5CK5TdOkJQm3nUGlKYh3BMoRiAX3TM0NHKnmnl3m92PQPjX9IoerT2YWg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/452945470e.mp4?token=MER6z5pgGHqm1XFvsutXKiZkbeO1vm4AtN3w9AmTHC6iRIqTfOlI1l5guysKeMuu5PunN-q-aKHm8tdTEfMVYRay-o7jwQSWGrVAPs8UJ_V5ajTEl04GkMsWR9DDhcyM1VnbLtT8IHl_nIjxbFrgJ9b8EDOuwcejt0LFikBqNDZm8anrw_MpZc08IOVlUGO7f4eiNffwmyXwbmpq9vcwYxzO1S-vomrsY6mSemxHJYK03W6qqmXeZL145zxrT4JKnsi4OtFOnDvyka7UF8S7rni42vjoK5CK5TdOkJQm3nUGlKYh3BMoRiAX3TM0NHKnmnl3m92PQPjX9IoerT2YWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم تشییع نیروهای سپاه قدس و حشد الشعبی که در حملات سعودی آمریکایی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138648" target="_blank">📅 12:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد مقادیری سلاح و تجهیزات رزمی را در منطقه «مجدل زون» در جنوب لبنان کشف و ضبط کرده‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138647" target="_blank">📅 12:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138646" target="_blank">📅 12:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59dcbe8179.mp4?token=RTilSlySozo8rXLbBTG5YneUTXeo-UlLsx9EG9n5PiqWvYMSzIBGEpqlyI5BGN8fJKsCQAI8EPh0qxeGW4DLljpYlHl-iJSYVQBSH0hFgi6ARrxUiFrbKZYGEWvGYcajILMbY-riHWkRGpz74F1fjQahzwjHuB1JQ0dZQgA6S4m_KfPIHJ0dy7nYgsWCAig-605Mh8YCH527VTIWZQJHYLe-mky-rX6rWDV6H-aesi6MUKrsWSr75Idx6Lmj2P2THWl8GNrle5n15z0qye52nvUnUckTGpW6yp9oYVF07MKxRrp3dT6kX6B4j_jiqET41LvcOIPw9J6-fNavas010iYlu2o9V7jOJU3zGZPx6V9H3D1rAHNHuz3cOIxCizf0IdPxMfAG2yqYSa5mq470pTqwhzYZvy5LQ-AlxQNSxKKgmf2I7wKv4VPXW_vDYQmj2x9e71_Vd02NY_v0VwLL2wvq4EOjLN7lVO7c-uTdZ3HP0adj4ZBD02IY9B27ZAVNyBjCBjfQ_iY7n0Mf6eeKpDwueRl2861XojzGsg6hAE0F17nHdeFikBKEaT8rZVMNzQ9juDIMlQiiNxA_qL_bHtu9j7ud1aBO25qdvwSMLgAKscFA316GaqU7M0DUJYZvl0TZye3P0XNzeiaLzN6mHySgpUsaqeNU_xNh2eXEUps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59dcbe8179.mp4?token=RTilSlySozo8rXLbBTG5YneUTXeo-UlLsx9EG9n5PiqWvYMSzIBGEpqlyI5BGN8fJKsCQAI8EPh0qxeGW4DLljpYlHl-iJSYVQBSH0hFgi6ARrxUiFrbKZYGEWvGYcajILMbY-riHWkRGpz74F1fjQahzwjHuB1JQ0dZQgA6S4m_KfPIHJ0dy7nYgsWCAig-605Mh8YCH527VTIWZQJHYLe-mky-rX6rWDV6H-aesi6MUKrsWSr75Idx6Lmj2P2THWl8GNrle5n15z0qye52nvUnUckTGpW6yp9oYVF07MKxRrp3dT6kX6B4j_jiqET41LvcOIPw9J6-fNavas010iYlu2o9V7jOJU3zGZPx6V9H3D1rAHNHuz3cOIxCizf0IdPxMfAG2yqYSa5mq470pTqwhzYZvy5LQ-AlxQNSxKKgmf2I7wKv4VPXW_vDYQmj2x9e71_Vd02NY_v0VwLL2wvq4EOjLN7lVO7c-uTdZ3HP0adj4ZBD02IY9B27ZAVNyBjCBjfQ_iY7n0Mf6eeKpDwueRl2861XojzGsg6hAE0F17nHdeFikBKEaT8rZVMNzQ9juDIMlQiiNxA_qL_bHtu9j7ud1aBO25qdvwSMLgAKscFA316GaqU7M0DUJYZvl0TZye3P0XNzeiaLzN6mHySgpUsaqeNU_xNh2eXEUps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار ای‌بی‌سی: ونس اخیراً گفت اسرائیل در تلاش است تا پایان جنگ با ایران را تضعیف کند
🔴
نتانیاهو: امروز صبح گفتگوی بسیار خوبی با معاون رئیس‌جمهور داشتم و فکر می‌کنم که آن را حل و فصل کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/138645" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138644">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
حمله ایران به اردن را محکوم می‌کنیم.
🔴
در هر اقدامی که اردن در برابر حملات ایران اتخاذ کند، در کنار این کشور هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138644" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138643" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در کمیجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138642" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
گوترش: جدی نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138641" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
بلومبرگ: اقتصاد عربستان سعودی به دلیل جنگ جاری که تأثیر منفی بر صادرات نفت داشته، به پایین‌ترین حد خود از سال ۲۰۲۰ رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138640" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
