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
<img src="https://cdn4.telesco.pe/file/CU0HsoIjcnpgLaI2qR9Vpb6fNscKa7SN5ozPBbOZdisVBY-8Zl_Zeq5PDXBppymM6TNtpi23tpTCqKeb9pRnjU6d2VezY3_CGEvCwzH6ps-QXQEIM8uPdfo-BsSt6h9l0qPN2-WKFtLBg-tOAmWe6FXXb-HqsF97yPx7P2ABCIp2x2Rnf1rCmzLuBnQWlASKxn5vSgaLKWg3sC3sWwaDI7qw9A7UkoVSMlBgaQ093lKP-7xRXVKEomWg3289D5YjL6376KcCwcv2QG99PhHZq1UZ_431BZUAq-fYbFAJYjg_yHE7Ov32HycvMFM_xkZ7Ik3PJz1dBvOBdoqr39TUEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 00:22:18</div>
<hr>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfTnTyII-2CrdqbOssJII5S1u39OBLSNXvYmOcRs0df0A9m1zTd8cy9dHpykxwMLVihsnsKW-cBhBwxAWXfHaU9OF1X1z48tQ6h0axVtrkI8z98gmh-Er0XYgge_fqjRRpgMXGzcpskA8n_e1OB5tF-MKy-QLtmp2MAOKXSJlbSUP9p5rRtBd_JxHJB9sOn6rUAXmMxL1g8GsF8E5sJPWVQQFpRluCvKIrrB0qDdGPdA0XiSf8s_fNk6cWhcmo8u0XYCamSqbkqcE7DoKMffpoOIVy4VCH073lPT3PqYOL8nYuVg7ne20k4FEdvNzWcaxlweMtVEnF5DCDSugSq2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 159 · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmuNlDH1vnWEMK4lDtVjTvPw2M4PNZTByL0OJPzILRWBUjlrQJrWPH_lxg4L7oA1YvjXBVMSJYbFXGHdMvXXRl7cFmQ_Dwc1P8_HPA_9EekXfTXRz8B4FmAx5XJengnvFawbnYX1wjP0B5_o_sjtMc8uOCBvoX5qEqhSjPXNVr3ES6xzhgxfi7XKxmfBT9Qj_sMHliRIaw5zZzQgTW571wSwuydNDuiZ1McHuqLEQFeSKCs5rOIHJ2B_7sr_8EY7tYdx_XYJLtvSWY50gdeTZ5_udvpk7IX0ivfFNpqeQoTxBvyGxM64mkReHLjF5yyXYMaH51AyiuRgx53unxzEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 530 · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صداى انفجار در تنگه هرمز شنيده شد
گزارش‌ها حاکی از شلیک موشک‌های کروز ضد کشتی به سمت شناورهای متخلف در تنگه هرمز هستند.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/21011" target="_blank">📅 22:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درباره دیدار مهم رهبران چین و آمریکا
دیدار دونالد ترامپ و شی جین‌پینگ در ۲۴ سپتامبر در واشنگتن، در ظاهر یک نشست دوجانبه میان دو اقتصاد بزرگ جهان است، اما دامنه پیامدهای آن بسیار فراتر از روابط تجاری آمریکا و چین خواهد بود. در شرایطی که جنگ ایران، بازار انرژی و رقابت فناوری بر اقتصاد جهانی سایه انداخته، این دیدار می‌تواند یکی از مهم‌ترین رویدادهای ژئوپلیتیکی پاییز باشد.
مهم‌ترین موضوع برای بازارها، احتمال تمدید آتش‌بس تجاری آمریکا و چین است؛ توافقی که در ۱۰ نوامبر منقضی می‌شود. مذاکرات مقدماتی اسکات بسنت و هی لیفنگ در نیویورک نیز نشان می‌دهد که دو طرف پیش از دیدار رهبران در حال تلاش برای حل اختلافات مربوط به تعرفه‌ها، مواد معدنی حیاتی و دسترسی به فناوری هستند.
اگر ترامپ و شی بتوانند حداقل یک چارچوب برای ادامه این آتش‌بس ارائه کنند، نخستین واکنش بازار می‌تواند کاهش ریسک تجاری باشد: سهام و دارایی‌های پرریسک حمایت می‌شوند، فشار بر زنجیره تأمین کاهش می‌یابد و بخشی از تقاضا برای دلار به‌عنوان دارایی امن می‌تواند تخلیه شود. در مقابل، شکست مذاکرات یا تهدید به بازگشت تعرفه‌ها می‌تواند مجدداً سناریوی جنگ تجاری، تورم وارداتی و اختلال در تجارت جهانی را فعال کند.
اما مواد معدنی کمیاب شاید از تعرفه‌ها نیز مهم‌تر باشند. چین همچنان اهرم بزرگی در زنجیره تأمین عناصر کمیاب و مواد حیاتی مورد استفاده در خودرو، نیمه‌رساناها، هوافضا و صنایع دفاعی دارد. آمریکا نیز در مقابل، محدودیت دسترسی چین به فناوری پیشرفته را در اختیار دارد. بنابراین این دیدار در واقع مذاکره‌ای بر سر «اهرم‌های استراتژیک» است، نه صرفاً تراز تجاری.
برای بازار طلا، نتیجه اهمیت ویژه‌ای دارد. کاهش تنش تجاری می‌تواند بخشی از صرفه ریسک ژئوپلیتیکی را کاهش دهد؛ اما اگر نشست به بن‌بست برسد، هم ریسک تجاری و هم تقاضای پناهگاه امن می‌تواند افزایش یابد. هم‌زمان باید نرخ‌های آمریکا را در نظر گرفت: اگر توافق تجاری باعث تقویت چشم‌انداز رشد آمریکا شود و بازدهی اوراق بالا بماند، اثر آن بر طلا الزاماً مثبت نخواهد بود.
ایران؛ مهم‌ترین بخش پنهان نشست
ایران احتمالاً یکی از موضوعات حساس مذاکرات خواهد بود. واشنگتن از چین انتظار دارد در فشار اقتصادی علیه تهران همکاری بیشتری داشته باشد، در حالی که چین همچنان بزرگ‌ترین خریدار نفت ایران است و روابط اقتصادی نزدیکی با تهران دارد. گزارش‌ها همچنین از تلاش آمریکا برای اعمال فشار بر شبکه‌های مالی مرتبط با تجارت ایران حکایت دارد، هرچند واشنگتن تاکنون بانک‌های چینی را در موج اخیر فشارهای خود به شکل گسترده هدف قرار نداده است.
برای ایران، اهمیت نشست در این است که چین می‌تواند بخشی از اثربخشی تحریم‌های آمریکا را خنثی یا تشدید کند. اگر پکن حاضر شود در زمینه نفت، شبکه‌های مالی یا دور زدن تحریم‌ها همکاری بیشتری با واشنگتن داشته باشد، فشار اقتصادی بر تهران افزایش خواهد یافت. اگر چین در مقابل، بر ادامه تجارت انرژی با ایران تأکید کند، یکی از مهم‌ترین کانال‌های فشار آمریکا محدودتر می‌شود. همچنین شایعاتی درباره کمک اطلاعاتی چین به ایران در راستای دقیق تر کردن هدفگیری موشکهای ایرانی منتشر شده که احتمال بحث طرفین در خصوص آن می رود.
از منظر بازار انرژی نیز موضوع حساس است. هرگونه توافق آمریکا و چین که به کاهش تنش‌های ژئوپلیتیکی منجر شود، می‌تواند از صرفه ریسک نفت بکاهد. اما اگر ایران در مرکز اختلافات آمریکا و چین قرار گیرد و هم‌زمان اختلال در جریان انرژی منطقه ادامه پیدا کند، نفت می‌تواند دوباره تحت تأثیر ریسک ژئوپلیتیکی قرار گیرد.
در نهایت، اهمیت واقعی دیدار ترامپ و شی شاید در یک «توافق بزرگ» نباشد؛ بلکه در این باشد که آیا دو طرف می‌توانند رقابت استراتژیک خود را مدیریت کنند بدون آنکه وارد مرحله جدیدی از جنگ تجاری و فناوری شوند. برای بازارها، همین تفاوت میان «مدیریت تنش» و «تشدید تنش» می‌تواند مسیر دلار، طلا، نفت، سهام و ارزهای آسیایی را در هفته‌های بعد تغییر دهد. برای ایران نیز سؤال اصلی این است که آیا تهران از رقابت آمریکا و چین فضای بیشتری برای مانور پیدا می‌کند، یا اینکه واشنگتن و پکن در نهایت بر سر اعمال فشار هماهنگ‌تر بر اقتصاد ایران به تفاهم می‌رسند.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/21010" target="_blank">📅 21:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ممکن است برویم یک نایت کلاب اما آنجا شربت بیدمشک سفارش بدهیم !</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/21009" target="_blank">📅 21:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محسن رضایی :
دکترین هسته‌ای ایران تغییر نکرده، اما خروج از NPT ممکن است</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/21008" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ztvR0riC_d52iD1PO-1wte1Oz6MK4lMdDrY2suUAjzgu_ti1-nIe-hYfdu7jH59U-tkeHICFX1ApOSnP8tuIByZOUXPYBPrPBeignP_9xC1n8vUnkR6xvJbhtd2DD8wJ9aYSLUxVGyUcja5bH383fumaIMXgYjiwSgrJxdsatWxAvnbFO_Y1_tx6n7powQ2Wi9hE8b6kmCxOUgi3eztmeU7nOsA5pFnx5NUqKBTjg78JyB4qjwoHzU1MeU5bGitw1qcC1cAFyuQ2ojwwGmwKyRE1ehmwPGz5YlVeKq4v06BauirkI9FiJJv70rJoNGfJcyEPkYwvB6jG0hNeykMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/21007" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/21006" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/21005" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو  با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.  این نابرابری،…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/21004" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-wnKN4Y8JSFr9OlSxwZtP7NN8wRyO03ZBTiV_itkzGLlnoqtxA0d4nezbKrUIGljNBBPsQN6kRPW_HOaGmB-rzljYBdo4xVX15rA7JPvkG95qxcqHnlSfUNQiBWao2CSXZwQ1Iw84sWPxtswguUs0N7WZmDoRyHw8_Z5BDrLGy0-tjLgzvn5K2-x5oslxX50HbbqbwUUPunhSQs38kdASpyMnUbJaD_1VjRY25t1KR-ldFDu990PEqMG_KFmjS77DF8E2E7C7_hztDHvLYpSKvyfR22sL-RtgJapKk8vDXqxihHdLaV8H-6VlSdm0VML4cG9xPZo-GN4CWUkZZ0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو
با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.
این نابرابری، چالش مهمی برای فدرال رزرو ایجاد می‌کند؛ زیرا رشد دارایی‌ها می‌تواند مصرف را تقویت کند، در حالی که افت بازار سهام می‌تواند همین اثر را معکوس کرده و به کاهش تقاضا منجر شود.
🔗
ادامه یادداشت از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/21003" target="_blank">📅 19:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محسن
رضایی
:
خواهان
پایان
جنگ
میان
عربستان
سعودی
و
یمن
هستیم
و
معتقدم
یمنی‌ها
نیز
خواهان
دستیابی
به
توافقی
با
عربستان
هستند</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/21002" target="_blank">📅 19:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMPPr8PcmrVbXW89MLPXrkAVo3L_VreNm1B6Pl-nQrNNidsyRGS7EaVjXr8hpPYzBiXn6N_Q1hywmyQe-dZJT6hSqa7Iosnzg4dRr8c4iVpGVlvB21loysgZ93MI_zjsCUHtUthzAQMK2_eiTIOr8gWmrz5YcSx3AOHneEq9SVL_rk7TSwi38cPCSV8B-X5KoWhytkgfbX1knHv3YnQiLkhHub4O5jyULvV3km9TL1ypFAaDwkTDslBPq15IQpKZljdxgWxmeHF9eNoRFOt6TaOzY1NbF6RkEMPcuGzK7bMFE_eXDZG5FIvnVL4CYtk-9QprjKq0V8EN7cn2zlStvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نتایج احتمالی انتخابات میان دوره ای پیش رو در آمریکا</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/21001" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">WW3 is loading....</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21000" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20999" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:   دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20998" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20997" target="_blank">📅 14:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qggfcxyByXbfb1fGnwbNZj9oT-JCzBfrxQHMNLHEQrI_gcUFWVzLibsHFDQktir3jda49Y0w7IpkhkvxiR03PUdSJrgTLXQKDzWaIxG2y2J-xm_jP0gcDa0gkXkFiqPs0KKku_u-8_weKaCSMeLLL9GiwEBhc9rnA19BWF_6kaGKrFljvL8lTbwLN83JSNPlV2yuyJ3AQLGwrOnMz9F4pouu7xOQ4OY8fT3b4JuLdtiR-zWGgV9F8TN_k5xm_qfn3fTMsYtacgbFSF_VCTsd3pDF-6V2dtBknuVBva24RP-7OHgN099OS18dnY9XWGbWgq2K9hNrlySmxFSGLsGNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش های موثق، ترکیه چندین پهپاد رزمی و شناسایی برای کمک به سعودی ها در جنگ یمن ارسال کرده که دستکم یک پهپاد کارایل توسط حوثی ها سرنگون شده است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20996" target="_blank">📅 12:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/20995" target="_blank">📅 10:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آمریکا بسته دفاع هوایی ۲.۶۸ میلیارد دلاری برای اوکراین را تأیید کرد
وزارت خارجه آمریکا
فروش تجهیزات و پشتیبانی دفاع هوایی به ارزش
۲.۶۸ میلیارد دلار
به اوکراین را تأیید کرده است.
این بسته شامل
سیستم‌های دفاع هوایی برد بلند، پرتابگرهای متحرک، رادارهای ضد پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی
است.
اوکراین هزینه خرید را از طریق
کمک‌های مالی اروپا
و
کمک‌های نظامی خارجی آمریکا (FMF) که قبلاً تخصیص یافته بود، تأمین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20994" target="_blank">📅 08:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله موشکی حوثی ها به ریاض پایتخت عربستان</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20993" target="_blank">📅 06:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20992" target="_blank">📅 01:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20991" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMHc_j3engXLekZ49gFfp2PPQKPLXHd9jfu9j9DtAFWVUc2Hu20HBl-DlyW1K9zZXvCQ5fchRHxjuaRFQnmALersa2T3o04544VJvXE0DFQYIjlYQzNqsxwDeKpKkt5dDVGka3u9EyEQ6A8voncuuXLn1MAGuNcu0h_MzasugZAe7Iz-7Ge2siDmhoI7JLd8034i8CEGGE3bgBReqQDIZ16bUgAf3qvQAEN-oNUe1btzuKS4c2qhFFShBAKK56N_8G-6ZaBav2FvRFBwjqexnboysZCXI_bDHAbzCNCJ4uvjfNTwOb_gyah1XGiUuCUiGT_eQJ7GJUQrzEBeM7AZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلامتی همه پورن استارهای وطن پرست!</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/20990" target="_blank">📅 00:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DazUgVxrKgrUZSF3AL_IrJQtkjBh6TFXFwjtW1eoHM9ljriE_7G_TqcAw5mBp6fBJPvTY_dopXQBu_T9OsOHqFL0yvuNzVMMyiURrelJx0P1ymzwfGtGLxrIMnmmZQEsw_yvPrloRN3KKuYSNwvAEPidyEcUqovcqdOukbfLJADWYQlZXeaPumvyJAbYluKo7c-dxavHpLuR0zUU9m_je-KBOT-tcorCtIqwak4SiZlTiftOZPF0wUdvyqPxQ9w2ETm5SwxPRZU-VmBHSFYO_3VBm5D3TTebVCU6VbfJ1XRBBvtBHfKIGcS5WdWV0X6MxZwLbwPggGTGX107t68TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!  فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!  همه شان را زدند.  یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20989" target="_blank">📅 00:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAL_qR_3MuitHEmxSlWVzbrBomEc5d23A15vLK0hKipuSCbp_hYkxAeM6uQxI7tQ-Jjbl9TZaAR2dtq9BIRf5YLLuvcoJPNT4pcD4-aHvWCI1KQWRT9fmY9_rt9dybRJyfgabag1OwBn-Q_6URPFFxI_nz8YmDvgSglkzkRnpibmpJgOP7KkoVisgLmLdLVbu_KCmp0SQ0IC0pxBskU5pm8Sr7jQCkqUXAdxiLOXJIvWfJpS3LbKLQCM_AuWu4wd5_iPAz98HvJAVXv4yEXV9hXngHDCTI2JmGnXZXMEVZhJCMMMXAChpYw18Bm1UmnWt8zIqe2MB7Wiorck845B9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته‌ی شش مقام آمریکایی که با اطلاعات داخلی وزارت دفاع در مورد آمار تلفات آشنایی دارند، تعداد سربازان آمریکایی که در خاورمیانه و در جریان جنگ جاری با ایران جان خود را از دست داده‌اند، بیشتر از آن است که پنتاگون به طور علنی اعلام کرده است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20988" target="_blank">📅 00:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!
فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!
همه شان را زدند.
یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20987" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار در طائف عربستان!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20986" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20985" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20984" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">العربیه:
وزیر کشور پاکستان طی ساعات آینده به تهران سفر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20983" target="_blank">📅 18:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران
انقلاب اسلامی ۴ موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20982" target="_blank">📅 18:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq_kbE3okcl5WX_CjC-IGCt40N5w6hJh_zKtdj2A9epm8wOtRSfOQV0s9WR3NA7fGJafB3ohpQwFQx0VXUOA0KHGksZlNUoVL5HSnD-K8iygc6-rtLmUi9o-kgYktWohaDWUF6QInueXFIZxwIrR1Hth05IcwforAWPGYLy1D2TKqeMyPUZ-vdXjAD6MpSDoZTouAsbg4eygg2WinfBqkK4ZoMGd3vB1mGlS7kM1rlSTbplk7q9XwgfUXjxkaF06H02IiCD3tJbCcOPPS4D6zuDicmdwR1dwATeEQsVbg9CJcEIy4vGiRTYY1_p3nx7xfQ2RieSjTy9JchZ6ZLE3AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه دکتر پزشکیان به جانفدایان:  کمتر مصرف کنید!  (پسر پزشکیان هم دیروز همین را گفته بود)</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20981" target="_blank">📅 15:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=JenLroLrdvFxfVtDMl9okRP-TOm8CNZxdUgvnIfPM6JrLxsuSsjPbUgdt_gTPmkcVqC5GMDMZuYq-PNMUeBqEnwpSHqnui7Nn5NzG5XAjIEj7yIHHPpmdQUs0GTzVQEnOGmu9By6o4ApCRNsaj8YinmLhEkunwVrwVjeDIK5Biln3TKRyNgqFApMVsOZjCjfdYMAOSlr-_qfYjWj2JnwAEtVv5VVTl-9zorE-gyIUQZTgbva09994yR9m1tS19gAC8LgCg6DJUGHeS-HH5CTFMJY24BqIR3J1ov7VvJgOVqJcKPLO-7EeZX0qr2Vlgu4pxh1HNgfiLLIrjPWdplDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=JenLroLrdvFxfVtDMl9okRP-TOm8CNZxdUgvnIfPM6JrLxsuSsjPbUgdt_gTPmkcVqC5GMDMZuYq-PNMUeBqEnwpSHqnui7Nn5NzG5XAjIEj7yIHHPpmdQUs0GTzVQEnOGmu9By6o4ApCRNsaj8YinmLhEkunwVrwVjeDIK5Biln3TKRyNgqFApMVsOZjCjfdYMAOSlr-_qfYjWj2JnwAEtVv5VVTl-9zorE-gyIUQZTgbva09994yR9m1tS19gAC8LgCg6DJUGHeS-HH5CTFMJY24BqIR3J1ov7VvJgOVqJcKPLO-7EeZX0qr2Vlgu4pxh1HNgfiLLIrjPWdplDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اروپایی بودن همین را فهمیده که یک لامپ را خاموش کند!  در حاکمیت قانون و مدیریت عقلانی و کرامت انسان هم اروپایی بشویم یا نه؟!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20980" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:  امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏   ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20979" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:
امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏
ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20977" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یادداشت بسیار مهمی است و نکته اصلی اش این است:
جهش بهای نفت و افت قیمت اوراق قرضه به تنهایی موجب تسلیم شدن ترامپ برای پایان جنگ نشده و احتمالا هم نخواهدشد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20976" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جی‌پی مورگان از تلاش برای پیش‌بینی پایان جنگ ایران و ترامپ دست کشید
جی‌پی مورگان اعلام کرده است که دیگر برای جنگ ایران یک
سناریوی پایه (Baseline Forecast)
ندارد؛ چراکه قیمت نفت، بازده اوراق خزانه‌داری آمریکا و قیمت سوخت از سطوحی عبور کرده‌اند که این بانک پیش‌تر انتظار داشت عبور از آنها واشنگتن را به سمت دستیابی به یک توافق پایدار سوق دهد.
عبور از خطوط قرمز اقتصادی، به خروج از جنگ منجر نشد
در آغاز جنگ، جی‌پی مورگان بر این فرض بود که افزایش فشار اقتصادی در نهایت دونالد ترامپ را به سمت توافقی برای بازگشایی تنگه هرمز سوق خواهد داد.
مهم‌ترین آستانه‌هایی که این بانک در نظر گرفته بود عبارت بودند از:
• نفت بالای
۱۰۰ دلار در هر بشکه
• بنزین در محدوده
۵ دلار در هر گالن
• بازده اوراق خزانه‌داری ۱۰ساله آمریکا بالای
۵ درصد
شش ماه بعد، چند مورد از این سطوح شکسته شده‌اند.
ناتاشا کانوا، رئیس استراتژی جهانی کالاهای جی‌پی مورگان، در یادداشتی در روز پنجشنبه گفت:
«شش ماه بعد، بسیاری از این خطوط عبور کرده‌اند، اما استراتژی خروج نه‌تنها روشن‌تر نشده، بلکه مبهم‌تر شده است.»
او افزود:
«برای نخستین بار از زمان آغاز درگیری ایران، ما دیگر دیدگاه پایه‌ای نداریم. واقعاً نمی‌دانیم پایان این جنگ را چگونه مدل‌سازی کنیم.»
هیچ نشانه روشنی از کاهش تنش وجود ندارد
جی‌پی مورگان معتقد است شواهد چندانی وجود ندارد که نشان دهد واشنگتن یا تهران در حال آماده شدن برای عقب‌نشینی هستند.
به گفته کانوا، هرچه درگیری به جای کوچک‌تر شدن، گسترده‌تر می‌شود، دفاع از این دیدگاه که اختلال در عرضه انرژی کوتاه‌مدت خواهد بود، دشوارتر شده است.
در همین حال، عربستان سعودی پس از آسیب دیدن خط لوله در پی یک حمله پهپادی که از عراق انجام شد، خط لوله
شرق–غرب
خود را متوقف کرده است.
همچنین شبه‌نظامیان حوثی همسو با ایران پیشروی‌هایی داشته‌اند که می‌تواند موقعیت آنها را در زمینه کنترل یا ایجاد اختلال در تردد نفتکش‌ها در بخش جنوبی دریای سرخ تقویت کند.
ترامپ نیز روز پنجشنبه به Axios گفت که در آستانه تصمیم دیگری درباره این موضوع قرار دارد که آیا عملیات نظامی گسترده علیه ایران را از سر بگیرد یا به سمت پایان دادن به جنگ حرکت کند.
ترامپ گفت:
«یک تصمیم بزرگ پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»
بازار نفت، کاهش بیشتر عرضه را قیمت‌گذاری می‌کند
جی‌پی مورگان ارزش منصفانه نفت برنت را حدود
۹۰ دلار در هر بشکه
برآورد می‌کند، اما شاخص بین‌المللی نفت اکنون نزدیک
۱۰۵ دلار
معامله می‌شود؛ در حالی که در اوایل این هفته به محدوده
۱۱۰ دلار
نزدیک شده بود.
این بانک محاسبه می‌کند که به ازای هر
یک میلیون بشکه در روز
کاهش عرضه نفت، حدود
۴ دلار
به قیمت قراردادهای آتی نفت اضافه می‌شود.
بر همین اساس، کانوا می‌گوید بازار در حال قیمت‌گذاری ریسک از دست رفتن حدود
۴ میلیون بشکه در روز عرضه اضافی
است؛ آن هم علاوه بر حدود
۱۰ میلیون بشکه در روز
عرضه‌ای که هم‌اکنون دچار اختلال شده است.
تصویر کلی بازار انرژی با حملات اوکراین به پالایشگاه‌های روسیه نیز پیچیده‌تر شده است؛ این در حالی است که ترامپ روز دوشنبه گفته بود کی‌یف و مسکو توافق کرده‌اند حملات به تأسیسات انرژی را متوقف کنند.
ذخایر نفت همچنان یک حائل ایجاد می‌کنند
مهم‌ترین عامل محدودکننده برای افزایش بیشتر قیمت نفت، حجم نفتی است که همچنان در ذخایر نگهداری می‌شود.
ذخایر تاکنون
۵۵۵ میلیون بشکه
کاهش یافته‌اند؛ رقمی که به‌مراتب کمتر از کاهش
۱.۶ میلیارد بشکه‌ای
است که تیم کالاهای جی‌پی مورگان در ابتدا پیش‌بینی کرده بود.
بنابراین بازار در برابر یک شوک طولانی‌مدت عرضه، نسبت به برآورد قبلی بانک، همچنان از
حاشیه امنیت بیشتری در ذخایر
برخوردار است.
کانوا در جمع‌بندی گفت:
«خلاصه اینکه، فعلاً هنوز به اندازه کافی ظرفیت ذخیره و عرضه پشتیبان وجود دارد که قیمت‌ها را مهار کند.»</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20975" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛    «ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20974" target="_blank">📅 11:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛
«ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با ایران، هر پروژه‌ای، از جمله پروژه TRIPP یا هر طرح دیگری که تهدیدی برای ارمنستان یا روابط ایران و ارمنستان محسوب نشود، از نظر دیپلماتیک، مشکلی ایجاد نخواهد کرد. در اجرای هر پروژه‌ای، تمامیت ارضی و حاکمیت ارمنستان نباید به خطر بیفتد.
علاوه بر این، حضور آمریکایی‌ها در مرز ارمنستان و ایران نباید تهدیدی برای ایران باشد.
اگر این دو شرط محقق شوند و همچنین منافع ارمنستان در نظر گرفته شود، ایران مخالف اجرای پروژه TRIPP نخواهد بود.»</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20973" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20972" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20971" target="_blank">📅 11:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcKBZsqSI7ThXj52JsQeX279imdKVLZ7etVIx1jUxrlCzz4foR2GpHk7ezgxxpysfhAZYHm3Rhbo3ndCMb41bE7mNnT13RcnLHIWwepXkPWBKpnyN35GLWGow4WbYKIa7QEc92fMbltxVBsOPks-oEWhh1Ogb8oBXApPH4EX7tAonlO_SD9VCQZxHSOPRhucACTKmFePzDLIKkWzHUThk82WaCv3OXYr1bJEQpPudBiTCTa-qtxlDCFah3_3IRREjugFkTXcJE7rPoLZrqFQ4-IHA2ETrDA3x-FeLOvnbF38zzigggeSV3-mjJk0S_20t9axukMKZiYEn9zfyN1BwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.
پس بهترین استراتژی برای امروز:
خرید پس از یک اصلاح سنگین 400 پیپی است.
محدوده های پیشنهادی:
4366
4355</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20970" target="_blank">📅 10:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMw_5l_2mX8CYCbwTJIn77osYk2Y5H7xcU4i6_UwRiYIEtUxu0UytevaIj53kbH6AmZ46ct3gEQqTjGmcN2L8cU_s2vH_JO4WPC31bM9QTZyDZH5XZu5O6W1e10KUCqdnv-moDT1sJDg19DWrTcxVHz2ET7c1xEg1yD2iKDEZDu3Sx8X4jdN-7UgALdXeB3KG7idQVoMPGNjSryT8dxXF-OONvKHkKlIAuQLhzTyOxJQZuESMdkSNIXA-LCD9IUTHHIOfESUlunr4t_lStWSUp7USDmTThkjkk_e6zHZC_k7EVmiLuWX4u6lw1u0q6_1ju-lx7aNSda3XKgsKRaq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد و انتظار یک اصلاح نزولی قابل توجه (دستکم 400 پیپی) در طلا داریم.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20968" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر دانشگاه تهرانی ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=Wjt1qJ-GvcsGOSbTyFIkiTKBO2e-QmI8RhD-YXgg0qVqjmlm9ZIlUhfKhzTRm8KVkv4KTur2_VUuOUY7tZpbeyS17vxiEfgsLOPCjfqfVgQ3s0o_M_4LiJdBpa39FcFc1fJ3Pp9zDEkx_d-P7tn0mwkAhfUoBIv_qFOGR8sn_c_ca9MkjHscX51Nt20rjHEgaYZdz4Vi2rdsUNhl3_NAm8GhcWzvEjrbdDWYomLmUvihNpB1ka7M8l_pRfxspeiwjPmF6cLgk02mcaBd4r9GK9THDzoBHudei_UPRpc7hP9i37_M5bq4iZL2HP7eG3txn7x4o5RWf-zBBOLCJHVYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=Wjt1qJ-GvcsGOSbTyFIkiTKBO2e-QmI8RhD-YXgg0qVqjmlm9ZIlUhfKhzTRm8KVkv4KTur2_VUuOUY7tZpbeyS17vxiEfgsLOPCjfqfVgQ3s0o_M_4LiJdBpa39FcFc1fJ3Pp9zDEkx_d-P7tn0mwkAhfUoBIv_qFOGR8sn_c_ca9MkjHscX51Nt20rjHEgaYZdz4Vi2rdsUNhl3_NAm8GhcWzvEjrbdDWYomLmUvihNpB1ka7M8l_pRfxspeiwjPmF6cLgk02mcaBd4r9GK9THDzoBHudei_UPRpc7hP9i37_M5bq4iZL2HP7eG3txn7x4o5RWf-zBBOLCJHVYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهریار میگه آدمهای پیشه‌وری بچه‌های گرسنه تبریز رو جمع میکردن و می‌گفتن: « بچه‌ها بگید خدایا نان بده». نان نمی‌آمد، سپس می‌گفتند «بچه‌ها بگید
#استالین
نان بده» و نان می‌آمد.
اینها علاوه بر بی‌وطنی چقدر کثیف و کودک‌آزار بودند که با روح و روان بچه‌های گرسنه آذربایجان بازی می‌کردند
_sheshgalani_
@uttweet</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20967" target="_blank">📅 09:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خریداران جهانی سوخت روسیه در برابر لایحه تحریم‌های ایالات متحده مقاومت می‌کنند
پولیتیکو گزارش می‌دهد که واکنش جهانی به لایحه تحریم‌های روسیه که به تازگی توسط کنگره تصویب شده، سریع و شدید بوده است:
مسکو هشدار داد که این لایحه تنها جنگ علیه اوکراین را طولانی‌تر خواهد کرد. هند قول داد از منافع خود دفاع کند و پکن در برابر آنچه آن را «حاکمیت گسترده غیرقانونی» نامید، مقاومت کرد.
این لایحه که هنوز به امضای ترامپ نیاز دارد، تحریم‌هایی علیه رهبری روسیه، بخش انرژی، صنعت دفاعی و شبکه حمل‌ونقل که سوخت‌های تحریمی روسیه را جابه‌جا می‌کند، الزامی می‌سازد. این لایحه همچنین به ترامپ اختیار می‌دهد تا تعرفه‌های ۱۰۰ درصدی بر ۵ خریدار بزرگ جهانی این سوخت تحمیل کند؛ بندی که از پیش متحدان خود واشنگتن را نگران کرده است.
از سال ۲۰۲۲، چین ۵۰ درصد از صادرات نفت روسیه را خریداری کرده، هند ۳۷ درصد، ترکیه ۵ درصد و اتحادیه اروپا ۵ درصد. اتحادیه اروپا همچنین در آن دوره بزرگ‌ترین خریدار LNG روسیه (۴۹ درصد) و بزرگ‌ترین خریدار گاز لوله‌کشی روسیه (۳۲ درصد) بوده است.
از سوی اتحادیه اروپا، منتقدان لایحه استدلال می‌کنند که این لایحه اختیارات بسیار زیادی به ترامپ می‌دهد؛ یا برای ایجاد استثناها و معافیت ها برای شرکای بزرگ روسیه مانند چین که واشنگتن به دنبال گسترش تجارت با آن است، یا برعکس، برای اجرای انتقامی علیه متحدان ایالات متحده که ترامپ از آن‌ها خوشش نمی‌آید، مانند اتحادیه اروپا، با استفاده از خریدهای نفت و گاز کشورهای عضو تکیه‌گاه (اسلواکی، مجارستان) بهانه می سازد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20966" target="_blank">📅 09:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به گزارش برنا، در نخستین ساعات بامداد جمعه ۲۷ شهریور در محدوده خیابان دانشگاه زاهدان تیراندازی رخ داد که این خبرگزاری دولتی آن را «حمله به یک ایست بازرسی» توصیف کرد. برنا اعلام کرد در جریان این تیراندازی یک مامور نیروی انتظامی کشته شده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20965" target="_blank">📅 08:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
نیروهای مسلح ایران به آمریکا درسی خواهند داد که هرگز فراموش نخواهد کرد</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20964" target="_blank">📅 01:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله ایران به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20963" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک کشتی ترکیه‌ ساحل اوکراین توسط پهپاد مورد حمله قرار گرفت.
بر اساس اطلاعات اولیه، کاپیتان و یک ملوان کشتی در این حمله کشته شدند و ۱۳ نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20962" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20957" target="_blank">📅 21:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20956" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است.
هر احتمالی از جانب من وجود دارد.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20955" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">— اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف، از جمله شرایط اضطراری بود.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20954" target="_blank">📅 20:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:
من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20953" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz1Z5TvnVir3Ud5EMV-T64WQMWUKGGwscxGvzyGKg_HkOEYUJ087QhekkGz3zln5s0N8aEvA1pXnkL_37dqfNRWGYLpAakLnjDkQbXOAKcyGR5o9di_acGIxu0kO9enjpQZhIh5FNNY1owdq_w8HMGc-l_JAtTuAM1NqZFPTpw5ZETpGdLwKAjdbmioa1yrW9fPPr2oKYSeWZNJFpKche9qrhDi7tDx_YhKQ10jlC4FmmCh2dQVLjtUIrfPgIsrUkMYFYdWW6gwSwTO49BiCDHmQhoIwqivWwruGFtNvRG-2VpzldCjMd7MRLRq3FOhFW61Sg97VHQn0K3kpyX6G1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mK-MzSGjuORSRqGxT4WSS1kLc14ddhn5tKoF0i3DUL7tRTeSG6f1fhyVpN8fJzkg3C16QLRewMrBV8ct5P9Jge8DBRAfv8UY3u5Ju80Ap0mp6WznU11pNy31XL2jnq8XaMnqRevPL5GkgCvcQcjCpMQv1S2Q_j_norZmbrBdXZZYlPWHuO2JnC41NMI-QIUE1H3s48XznikcMJAFL6geQK8UFFrMt_vbdJG-wANLAJXsfZtm0NI_7XX-hn9JQL1kE4kjpU9Mw8w5SuiZss1Auibk_lAyjfA8JrypMQXvegy1kbphLdX3jTsDsacd3blGabvapXW6P8yGI1iRvhE8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLgwQ4EfLG2Hwp1AF-zIini41vguoLjbC7oi8k_TJpeDFcoLWjDYH8FciSdVyrh-0wtUJ90KJaWJDPTCQYn8i3RJ6qQguArzHh1epyeSEcPouTsxBpx4OjLs_BTR-k111ZZ6Wuk0wXlS3Clp8COCdMcgEjIB8jYGz_lFifgRkLhlR-HHcj5cHMiSIeARVd5d6K3FK1dNo2oBs7rWI7694thfM3Gg6oRS1mgDH66EEfg56uUm1lF07RQUTOweCpIMQugSkKvDrxexHQD8WTK27dRmzXLeNeoNhK0ifyYEYJra7QpgnyVOpCcFjTwQb6fXKhqy4b6MvA_bPvundU4gWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7KE4MU7bZMzmmxzRjdM4wGeUVIVggMSqHMucEQHsorYIQdRgtEH1uqLp-Uk3SuEKcDVUhGc7VTuF2-b9xHsTGAGDryasAk0rC8Zg_kZd659XstGL80QEXHl1x3ujFOSAAGwuKb1Mmv6xUJgSmoeXoHBuVDhibQVcksdBgsJLFnuZIWSALIXqYHAo4-Fq4uvCoNweD8neb0vEcD8g5M07Kb3P-wyz9EpYfpSx6f--u5kVOu89WziUaeQ5EtF6xUgsD8HqSo7ONo_8wFhfaOzo5mhwOeyS8cFmT6EB6aETXt3R6uuVOV-kIbKsraA0YXWqvPdTqPUFda4hjM_aQN2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5wwURlDXGPLzE7YKQ50hmYA6m0wC5M-p_Pm66WoigOFudVCUNP6dZ-Ksc-BZHJz2O1dv1R0HyrtWg24zbuVrBADJHvLRRSDHSlyWZ3IDnhHYRykDI_OBaMme-LfdHgwNzQXNxGi9QjFmNiqIW1gTv888WT9X3bKzNUK9ZtIknUsg0PtVXAo3WjfEEomcoT7bUzuj3adD45R16GOCkNJGAvH9l-9DkGHcQbu96lBXdEKJ6ZLNtV2pOmBz_-a-lkNbx7Y481gRTwKTmTO7AhIxd9tH5HsbfY2GJM8d6-qeamApmVZAoQqvGtZrJhe1sQDES4iYmz1UY7hqJtvngVW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-1hXYCXFuGTU1bHRSW4pyfMFO6JPMdRvQaqZRa_gQRg6Ty9-5YbzCRB8PsxjbmOeGksSqKgLAWHj0sIcsC14djkJ3EFy_zYj1nqrlBHtNvCdW7T9DFBnlBH3UrPg5thoJuz075xBAF9pIRr6vAPOomaQtxrLz2t5CpCnWSGKrsV9LFTwd34BpW4EP8I2cs29ZSA1-3ix5Nz5nko3CfVHwPkmT93DjlkX6MI7tav7WFzx78KhVX3-8qR56sgF8eZ4mEzWjENo-yrQNpIsT4vD_lkaRaXJqkhnbUrfiIXth55tnPCg6-fyFP1VBWbHeEfe7QVkEwNbrVXu1bn8QxQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYP6AurT2NsOKrPRiJvRkzoYXGR_XoGoMfymcu5d095cFk1vv2Sw6FzAUSpW9j7wGkXTzj6Rf2pYXFHtl8yPp2X7gUF10gemRTUoN-_6Yokb03mPeldTyC4SMqAjUBLIv_TREiiadneAxsr8t144DoNesY3aXmlKZI_gkbtv25SctaSx1ljag1wfHqgpwWEpwHQWPHGm7K1qvJgLNFUTJQ6p8nbhWzvtDmVP9OAMQ5X7y2QylWA6Tku9vBdUEuulrSgONH-hRp5RQCsz4h4BD3oLVGKLgBE91ctaQ2u1laDD3cIrbZivI67f5v3Z82bO-wDV7ovwoRCalj2G-z5Pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac7YPdGu_rWaQrvQPwcFhdbDY3tVgoLIaKPZ6Lb4Y00gn4-SH-5krqph_cjJ44wVRTS_IOmBXO5b7hw0dIECQQCdtPC--s6DO2aD5jTTmt7gEBxLqRCYb3Lm0MziO4cwrccg8VefsOeOh1Cw2M3KcdoakIaAjzBHayUB6Fn_01Rqi0hQsSez22Ikz9gLjKB2_lFrUiOQlhy4xUTKJjW44x3CSmKJc2fp1KWtVdHbsG9JysYl2yoqkFSPrTHFIo2UJ3gxp0pbgbBKuqWH6EEO9AsPtsaMma9t3Lzr0FER3YKbFQD9q-ziFlvpkYAaSe_fSYcWDWaSlQSPum0ZGKiYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=uXLeacSXegpttmv0c3NJxSAXMWaWagP1HJqYeAS6JjZM2y26AAhxTyPkm112DaanCda7hxYGQGcOAqPvUAetmP7-Qu3hLjmpEJybPROu2a0fVnWaMBy522OiWRyo1gDWdvW4vIWnvuofDAy-kderKD-NzMNI8O9T-jeQrFJn83tvPhNgNIBnyDbXavM3Uz6WoVN08SB64J-QOQCbMj8J9PX1zhKRj1IMr-z-w19FTz0-nhuRB8xYUyJ4Q0npa5l8Cve7mEbaW2KNzVDffnrh3NvalQWovhkphrqlWjpkk8iyQU_-a-XFwyK8DlJ50fWBJUSHssZnstGwp9yk8LU7Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=uXLeacSXegpttmv0c3NJxSAXMWaWagP1HJqYeAS6JjZM2y26AAhxTyPkm112DaanCda7hxYGQGcOAqPvUAetmP7-Qu3hLjmpEJybPROu2a0fVnWaMBy522OiWRyo1gDWdvW4vIWnvuofDAy-kderKD-NzMNI8O9T-jeQrFJn83tvPhNgNIBnyDbXavM3Uz6WoVN08SB64J-QOQCbMj8J9PX1zhKRj1IMr-z-w19FTz0-nhuRB8xYUyJ4Q0npa5l8Cve7mEbaW2KNzVDffnrh3NvalQWovhkphrqlWjpkk8iyQU_-a-XFwyK8DlJ50fWBJUSHssZnstGwp9yk8LU7Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lec3fTJUPkQcRIIO5K0TZqXuL9cWRWodYHTl1jPHkhJUHBJtnm0uOY5NRzMnOJhb3l8NKeMaPrvAmQ0oOC_wTMqaB8xWIx5IyYqqUjGtK1Tbq0ixiRrzf0FP2W9s7OT3M5S_nSjEbVugyEhrmhEnGL-AjVyuXlavuOMdh8tincORBwPJtKRRC1dx4xSYXSFmXC2y9GWLdLl-eG3Xlv2ejlHi7TKDvMvlVsiwIBLldotAT2plyo_os9sNtdeZ8rV0PVxEtkNW3hzbisMR_e2mZPI2ZRr8GyH1vCxMttxN7IiH5ml0d0oGghG1fdYV7qAqzGrGoFjWFrV_TsDyhrFFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDNlmUAzpnx2UEUqWf-tsmHbZTt4OUKtCdvT9Bh0gnxfGMQxPPpRFLpoB1YBTQsNZF1osbw9TzDjfdg6VInPwm0MDitwvb0qk2Zp03Y1ySo9I_bq42NsHOUnfDYNfRZ0L8bQjKHUkIjaldfWHm-JHAGnWbveSxYeMCq4yhsOPkvRgK3BmxQxgnfLHxlAgCyWjbZSzz3fynsjR_e7yJFo808BW_kOHDoP2BItDL5qZmiwIs6yQml_UnULGB3Rgjnqxl6vmPsVDbtiUWBFST1qv0uv56OndPyHdgoSddj_yIot7tOWtgYZzRiuJPDhFvJAj_9DFakvaFUSuWD97LGRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1jU8Z0ZNS5P06aCvNIsIReuQzjk98uFbKTKTLT4ZE-CqnWMDRHBRm6dltpx2c8kqhg8ndCD2xwNLzXroDjGUdU0N3PgahN8S_7d0l8PGVIci_-IPvugt6QnJUwx96otP01_QpjTxqQW0f0QeOYjz8B84NGPvlTlGpIvXmyw2FNM6qnbhtrSmDdIqS_6k7ONDo8-lTptCWocZ_W-K-Jwq_9gxZ6vn2jdqmemvNR81mqd-DYMSVmShBJT9XXLFSajh7pLGen3FjP60djEGbdYslyl5iHH1wBmoBvUkQtBURrgh6NLjfPyLbFHBbuxgtVCRZCS_7daMeJ2JCEIEFgAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=niqQg2wfkHQMIOsOzhcqtHT4EdImoP6VFXpwoMVxT11zlb2h4nLqGpY41Bk-EF49SfvsoEbrjfhhqMX606lX4ynQ2oyRHY24fZuo4xiPDK3i6wejoFZTUVxbaWON6CCo5B3ISm-cG_1b2HQNAtW49iFnzvEllEbZONV8A5nAmHve4C5-RsZ5TcvXTfCTBLOWvkMpp0dxkwnU7K9C_GPJYBhL1z2wnNvs6maExL8twL-oCs8P4F4WQ8B1KH4Z1pOSxt71J4FdgndBrsbax4jqsoi69FTGi4T5N_-uV10BHEn3uYV4WeotrFpJ-LJA2U9yqUqqZWzB4uh8NMxZ2zuDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=niqQg2wfkHQMIOsOzhcqtHT4EdImoP6VFXpwoMVxT11zlb2h4nLqGpY41Bk-EF49SfvsoEbrjfhhqMX606lX4ynQ2oyRHY24fZuo4xiPDK3i6wejoFZTUVxbaWON6CCo5B3ISm-cG_1b2HQNAtW49iFnzvEllEbZONV8A5nAmHve4C5-RsZ5TcvXTfCTBLOWvkMpp0dxkwnU7K9C_GPJYBhL1z2wnNvs6maExL8twL-oCs8P4F4WQ8B1KH4Z1pOSxt71J4FdgndBrsbax4jqsoi69FTGi4T5N_-uV10BHEn3uYV4WeotrFpJ-LJA2U9yqUqqZWzB4uh8NMxZ2zuDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqsxQH49RzWWJlkDNG1b6zUFlrKtHkOtAUwj_PaJo5-qTWzZIA29GlQbPOlwlbA7sI8nlYRmJ9zqK8ZcFXH8Nz7WCjxBHB7uCsO9nOwv6arnaPHQJg5VJXeXD8nSf9icaAYty4lVnAe2d-WzaxXv6yt5XOZaO6xHKwBVjJzVJnQXHg2TqMFWCH342qoQhItgpYsXPepf2pQsdFcXL5sxU0K4XlSfOYQdHjRN6ePCwN9bJwFTIO_H6MdWXzIvXHWlm-dmtkQabTsGDEuxe7r6vpN-_y2TIbOzav102kHD345SeJB7934Y2bRz1UM2Nk69JOJE82o4OmoRetl_BhC-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP6mzScDdXpZK7fS4tkLgI4_6O9oybx0D7qRfdXVMpLWQIkqJNo9YAXY8uib8HtZb9T_Kp8imoSgs8ibBMtzvG-v5xQmZ9kVzz1Ks7bJqBBku1QARqa-ufr1HKnvlrXVNDK4O9x34bwxQcld-EqKmAhaTMOdpbecOjwvuX6QB30VBg7zxskaFQJ7EFjKovWRM-J6MD0no0bEC3Qp4GSGzcbaBmPjla-A7kZR2-E3dPhc73p7YOn0qpOtFV5LmvcT4FJK2q6aMwexd8PT-qA3BvASO9TPKJPkGVYBktHF8B8C6NXJFa3lzj72ViU8X2cmgAmkqXTls0b6QgkDAAEK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gpfT9e8E1F0KynkfaA6lP4qgZeLw2xIP8aDucLbpIPuqn5ld8fSIIiAOWuYIUvuzQCpui1fdrSR5OZH_DWsz8VU_Iy0SkRUZBDKayGfCwqCB6J9j7gTvNpLoZJ6pZPOMpzHOPlk16Bt2hvc2bZvXqroHymAIsLC9ARkWEjSaQhyF3PjMz_dT0vFETCnZxV6GRGJWoRJWzaIZlmPb78oB5ZAERT4Qibbbk1J_ioPwvwmYulBWcMvgECqmTPyquuhJzpUB5M77L79l3EYBV-iF_chPOdmjxkhPKJ4AyZuc_Cjsl8ptS9VrsCRgI0DXIiEeJk9xrk8Hmrb4KspSP5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkGBd9NVsRi6hjoiK7pr2uM54LwuvAzNJIqbEjO8UM0ngKcs2-sqPXMahJ4BdNhYn7gb45hfl3TXOz5cIrzvJr-1-UgX1lU13PoSPM__Zw68sEvcZYDT3ScFlqez18ljGjjDiyK8efEfxYzTcSuSrlkRtg4wfgic90SmqKEYZgnIL9CZ5xs6E5H3hJkGRLLH5xBTninLMwDV6e8xiNl-Hczc0F4Il7ZrZEnXe6FZGOiix3rcqH1YK8YHj6VZwQG7hz5vSUJ8Pnyv7vbAqalsMZ53oCHrQywg02LDwB97Tc690UTJk6WA2W79kgRZ6u3-j9LXbPLDNH2ul_qmUaC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4RCzaLhyRkClgp0e2xA-e2_abrhk76073mD9QKlFvrZrz9YIH-6dzz2OnMnnA9078lag-3gbN7IAHluszCydlDrQNsr1rjy9T2tVnNaZH1pNxRUSB-ObvLw_eM9gSPqxdAAhTJCNoEUJlkF7q3ZzBDLdHLinG7DY1mK25qUvtc2Lu0BxzUjLYqeDaUTBOtatV2oojMAVMhW0S-Gq-YnrG5IMjXq0A05bNrZyOfZ1dGpUKEw5TtjKRhd7cQtFGDbLTNs2hZ99dkbhzwklLfK_LgZ33WZKy9_qgYjHAjL_-4k6YnEMgZ6UH6AzeLIm6M0X1RHtp0trdJ0O-SmYarLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
