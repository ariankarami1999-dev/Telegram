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
<img src="https://cdn4.telesco.pe/file/dX0oWOuu89-Z48s_Yi0UCAKCCBknH2JM2iUil9Da5tkZB-ZI-0rIHeC42nGZAnwfhEzVKFHiH2qifBBQeUiPUQQej1eklRa7HUPaC9_n1pVfQE2LWlevAMJtAxWqE9QQ-XR1caM4cd04pxXe6LJlCt1LALZmgAcfFcA8wKsRwnk_t3vYFIyJaZifdGTebO6quIWMOiTwSmvBOVKqvqfEaYVwRN6RuTxMUOfnUqqu3rLe1r9bxsHvM7r11SrwfOYvfljonvMdXeIaj5qvyFVq15H59X8vJ5s39ijcwCBk1pZREnrEPBHTTq8B96OuWW-DPtS3E0pAM_ZjYtQK0pRrpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-441470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT6UPJGS1xhYrqXvTCmrFgfHiPG_4xIdCvdqqR_fviYTqwxbPuo_iigcrlwq84u3GFp3t6iui2EFR9FHGkoii4DG9A0eKt1SZ9BGomsZnnxvO_m3OYC4XNCwBdfNo_SBilX_upTio0XqKHQI9JFZySXJXelo-svy1aLDt5hwDvz-PwUHfebe9EJG4IlPLthICJHwVK_kyq1iGM0_wlOzULWfhnems-ImLj3KEUIgI2HCvwpF6sUFnQqPIFqHpt_E5-8N9ugBinoduXJMUdSSPnxTbY2Ud-8ENn3zxVHXOAhzXBhmTcPt_v3nOjYXCi5VrvroSnRCH8IDHMg-WnmiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: رفت‌وآمدهای میهمانان عرب به تهران به‌خاطر نگرانی از تحولات آینده است
🔹
مهدی مجاهد تحلیلگر مسائل سیاسی: بر اساس اخبار منتشرشده از سوی برخی منابع غیررسمی، در هفته‌های اخیر رفت‌وآمدهایی از سوی برخی کشورهای عربی به تهران انجام شده که به نظر می‌رسد بخشی از آن با هدف انتقال پیام‌ها و ابراز نگرانی نسبت به تحولات احتمالی پیش رو صورت گرفته است.
🔹
به نظر می‌رسد این کشورها نگران آن هستند که در صورت وقوع هرگونه درگیری یا تجاوز علیه جمهوری اسلامی ایران، مبادی و مراکز آغازکننده این اقدامات در منطقه مورد پاسخ قرار گیرند.
نگرانی کشورهای عربی از تبعات هرگونه درگیری با ایران
🔹
جمهوری اسلامی ایران پیش از این نیز به‌صراحت اعلام کرده بود در صورت هرگونه تجاوز، مبادی و پایگاه‌های مبدأ این اقدامات، به‌ویژه پایگاه‌های آمریکایی در منطقه، در چارچوب دفاع مشروع مورد هدف قرار خواهند گرفت.
پایگاه‌های مبدأ تجاوز در تیررس پاسخ ایران
🔹
کشورهای حوزه خلیج فارس در بیش از دو ماه گذشته فرصت کافی برای انجام اقدامات عملی در تعامل با جمهوری اسلامی ایران را داشته‌اند و همچنان نیز این فرصت وجود دارد. اگر اراده‌ای برای اعتمادسازی، کاهش تنش یا ارائه تضمین‌های مؤثر وجود داشته باشد، باید در عمل مشاهده شود و نقدا دریافت کنیم.
وعده‌های غیرنقد مبنای محاسبات دفاعی نیست
🔹
جمهوری اسلامی ایران در ارزیابی روابط و مناسبات منطقه‌ای، بیش از هر چیز به اقدامات عملی توجه دارد. اگر قرار است اقدامی در این زمینه صورت گیرد، باید تا پیش از هرگونه تحول یا بحران احتمالی به مرحله اجرا برسد؛ چراکه در مسائل امنیتی، معیار تصمیم‌گیری اقدامات عینی و ملموس است، نه وعده‌ها و اظهارات.
شرط ایران برای بازنگری در بانک اهداف مشروع
🔹
توقع جمهوری اسلامی ایران از این کشورها کاملاً روشن است. نخست آنکه اجازه ندهند سرزمین، آسمان و ظرفیت‌های نظامی آن‌ها به مبدأ تجاوز علیه ایران تبدیل شود و دوم آنکه خسارت‌های پیشین وارد شده به جمهوری اسلامی ایران را جبران کنند.
🔹
بعد از آنکه آنها به وعده‌های خود عمل کردند، مستحق دریافت امتیاز از جانب جمهوری اسلامی ایران خواهند بود و در آن صورت، خروج این کشورها از بانک اهداف مشروع ایران توسط ما بررسی خواهد شد در غیر این صورت، محدود کردن جغرافیای دفاعی جمهوری اسلامی ایران، خطاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/441470" target="_blank">📅 22:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ بار دیگر عقب‌نشینی کرد
🔹
رئیس‌جمهور آمریکا مدعی شد: با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و تأیید شده است، من به عنوان رئیس جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران را امشب…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/441469" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441468">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1vpq5v_tj5627iQdZk3-iAV7-QCogSepjIfmGsXlDSKSWO0rsegdJehvphWqsV-8tXVCP79iHBOFMAUjDziKcyACYG_dhCsUGxItRVlRdoj91EavV6PLizhvW6VW15T5VC4DDnPfXu9AetJYNAaF5PpJZKdqixB3zULavQ8-SvCEP4tRpp6ZQdmEU5rgdheZTWFh-RzcQZO43vjydPO9rgyIlOuKclKwzDecpNi26kiHkBYtAKax9puFPhIT1iG553r3z4A6xQtZPEW_OA6W31CHcVLrESYtRKeP5aSLym7ppKuZFbr0Zw4SsgK4gFi71DMAzBNb9X8lQafjbTLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: آیین تشییع پیکر رهبر شهید انقلاب در دههٔ دوم محرم برگزار می‌شود
🔹
تشییع پیکر رهبر شهید انقلاب به واسطه برگزاری شایسته عزای سیدالشهدا(ع) به بعد از دهه اول محرم موکول شده است و ان‌شاءالله این مراسم در دهه دوم محرم برگزار خواهد شد.
🔹
این تشییع، عهد و پیمانی دوباره با آرمان‌های امام شهید و تجدید بیعت با رهبر معظم انقلاب، آیت‌الله سید مجتبی خامنه‌ای خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/441468" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ کدام شرکت‌ها در کشورهای منطقه، شریک اسپیس‌ایکس محسوب می‌شوند؟
🔸
الکام اینترنشنال: شرکت دبی‌محور در حوزه الکترونیک دریایی، از سال ۲۰۲۳ به‌عنوان توزیع‌کننده مجاز تجهیزات استارلینک فعالیت می‌کند و یک مرکز عملیات شبکه استارلینک در دبی برای پشتیبانی از مشتریان…</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/441466" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شرکای استارلینک در منطقه، هدف مشروع حملات ایران
🔹
هفته گذشته رویترز در گزارشی به نقل از منابع پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته و سنتکام برای هدایت پهپادهایش از ترمینال‌های استارلینک استفاده کرده است.…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/441465" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شرکای استارلینک در منطقه، هدف مشروع حملات ایران
🔹
هفته گذشته رویترز در گزارشی به نقل از منابع پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته و سنتکام برای هدایت پهپادهایش از ترمینال‌های استارلینک استفاده کرده است.
🔹
پیش از این وزارت جنگ آمریکا نیز قراردادهای چند میلیارد دلاری جدیدی با اسپیس‌ایکس(مالک استارلینک) امضا کرد تا این شرکت در توسعه شبکه ارتباطی ماهواره‌ای جنگی نسل بعدی آمریکا مشارکت کند؛ شبکه‌ای که قرار است سامانه‌های تسلیحاتی، سنسورها و زیرساخت‌های جنگی آمریکا را به‌صورت لحظه‌ای به هم متصل کند.
🔹
این مشارکت گسترده اسپیس‌ایکس در تجاوز نظامی به خاک ایران، سبب شده منافع این شرکت و شرکایش در منطقه، جهت قرار گرفتن در بانک اهداف ایران مورد بررسی قرار گرفته است و نیروهای مسلح ایران می‌توانند به جهت رفع تهدید تجاوز مجدد پهپادها با استفاده از زیرساخت‌های اسپیس ایکس، این شرکت‌ها را مورد هدف قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/441464" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0245725c3.mp4?token=aAxEPTS4A9VnGFLjqO2voqHki8JWekUVfmbf-e39GgfZzaUPU0HRiSFxZkNyz60ODyz3G97-9XSNu3BoXdaEhKd6h0QI3XyF1EghUtgoVmjAJwRum_UjXz2zWvv6-7q1kKeZ_EzP_-IYYcq1zPSGqK9-zvEOr3eWsjHVSSg4c3FmGgtt3qsoS4aXsV8s_WS1LmhmciQZmbMM5DIyi36nUPMXppc4YieKv4TQwzY6hugpFNo4jdPUViOgUvyn79900ALNzRs9MCZ3_ftf9RbYYli56efNgm66sEwgo2SKzja6cUIgDutJSebR9iiXxgxVlnazDJGrmvwMxlt9n8ldDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0245725c3.mp4?token=aAxEPTS4A9VnGFLjqO2voqHki8JWekUVfmbf-e39GgfZzaUPU0HRiSFxZkNyz60ODyz3G97-9XSNu3BoXdaEhKd6h0QI3XyF1EghUtgoVmjAJwRum_UjXz2zWvv6-7q1kKeZ_EzP_-IYYcq1zPSGqK9-zvEOr3eWsjHVSSg4c3FmGgtt3qsoS4aXsV8s_WS1LmhmciQZmbMM5DIyi36nUPMXppc4YieKv4TQwzY6hugpFNo4jdPUViOgUvyn79900ALNzRs9MCZ3_ftf9RbYYli56efNgm66sEwgo2SKzja6cUIgDutJSebR9iiXxgxVlnazDJGrmvwMxlt9n8ldDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج قطار مسافربری از ریل در ترکمنچای با ۸ مصدوم
🔹
قطار مسافربری تبریز ـ مشهد در محدوده ترکمنچای از ریل خارج شد؛ این حادثه تاکنون ۸ مصدوم داشته که ۶ نفر از آن‌ها توسط عوامل اورژانس به مراکز درمانی اعزام شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/441463" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZEoPug2CoMMHXJOSGB4Xh6B8GQ19oFe03J-4hcT7_v7nZTBzN0oPiqBFPrl3iQPbEkU8S2UtOt7F00iwkEbYyT0pi2ektRPw9Ozz1JGxNgx7vp71Ofq9M1aSPhB1qXPPg3p3aDaXTU1tSUjW5E_tiBFJZena49A159D1ACO8Sqm08In0w_pF0a3FzY2AfV7B58rPzGbAZSBrgFXgdKdd3pReKF0vTG6vfS75zKwTek7fPovOZnBKWCBg9tvM7rvrDI93TwfE1hjBgRehzBKY8-q131SlkmLTE74NNeAkZO9CljeJxGlggILF_ipyVgd5PsaroYoUM1aoEMDeMtXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«صفا با خانواده»؛ بی‌مسئولیت و به دور از ارزش‌های دفاع مقدس ۱۲ روزه
🔹
«صفا با خانواده» سریالی به کارگردانی منوچهر هادی، تهیه‌کنندگی مصطفی تنابنده و نویسندگی بابک کایدان و پدرام کریمی که با محوریت یک خانواده معمولی ایرانی و در بستری از اتفاقات امنیتی و اجتماعی، می‌کوشد هم سرگرم‌کننده باشد و هم حرفی برای گفتن داشته باشد؛ اما در نهایت نه چندان سرگرم‌کننده است و نه حرف درستی برای گفتن دارد.
🔹
متن «صفا با خانواده» از یک ضعف جدی رنج می‌برد: کشدار بودن و پرحرفی بیش از حد. بابک کایدان در مقام نویسنده‌ای که سابقه طولانی در نگارش فیلمنامه‌های محبوب و جذاب دارد، این بار در «صفا با خانواده» عملکرد قابل قبولی نداشته است.
🔹
با وجود تمام ضعف‌های فیلمنامه و کاستی‌های اجرایی، بزرگ‌ترین مشکل «صفا با خانواده» نه به نحوه ساخت آن مربوط می‌شود و نه به کیفیت بازی‌ها و کارگردانی آن. مسئله اصلی به محتوای اثر بازمی‌گردد؛ جایی که سریال در مواردی مرز میان همدلی با مشکلات اقتصادی و توجیه رفتار مجرمانه را مخدوش کرده در برخی موارد زاویه اشتباهی را برای بیان اتفاقات دفاع مقدس ۱۲ روزه انتخاب می‌کند.
🔗
ادامه نقد این اثر را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/441462" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ6ykwVu0RMKiiye8fmAQBLRCuPnKXilEFWvJfH1Nqyk9E_f3Qt1Nb1_6yKN3X_ku1DzvPthe2SA0PXw7XopYhFOuozX4z3PSaKyfukbRF_1k16E5ouVg0Xddo_qZ3202iGs6XN6tNwUPyosmVfcFRsRSqcB-yQfTim8WeQi7p5hWOZ44dQEwMzx4eUFQtiQtJvNCw1oWXgQMSqqoNDW4EAAPElQVb8FHjRF-T89wEHVVgklKJEAI34P-shu8UWbVDnZ7xXklIJGF1R0-Zb6vIsM9isFL-zQ4_E4S3iZrWwl7zqPLyhvqMryxx3zYPmpsmL62rg-CrMRQrs8I3BJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فرمانده قرارگاه خاتم الانبیا(ص): اگر آمریکا بار دیگر حملاتی علیه ایران انجام دهد آتش جنگ علاوه بر منطقه، فراگیر و گسترده تر خواهد شد
🔹
آمریکا از یک سو حرف از توافق و مذاکره می زند و از سوی دیگر شرارت می کند و این تناقض آشکار در رفتار و گفتار آمریکا عامل…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/441461" target="_blank">📅 21:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjFM8FaJYHiFqvs94X7SJF9W4Gy7Ga8L_Xij1KSD16tnZ_IzZTXpDMvQPAyw_3mwKd3mGgrpA2VCbeUNeesT42NeEGbG863zggftFMU6EiegC0q1_pGlnEzbVyl8hdP37fOdViC6rzRvR7pI2j5WMtnXNTDQjLFdIraXBhKps8Q9AleQUjKls9-yLwTWdnnW-bdCL7hkdKOwmZeu4NomLhcxFc7M1HkF5zLjFITYbkhouthks7EM2sZCr9M-lzFADIR1zdq5PRmI7KhGnPaVvkgeyy7XnBciLxpZbBW1ZkoRfVuls6L02L1hPD0Q--n1y9D15hPgez9kJmVr1bEntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: با اتکا به خدا و اقتدار نیروهای مسلح، هرگونه تعرض با شکستی قطعی و پشیمان‌کننده مواجه خواهد شد.
🔹
امروز بنیه دفاعی و بازدارندگی ایران، فرسنگ‌ها فراتر از دوران دفاع مقدس سوم و هر مقطع دیگری است.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/441460" target="_blank">📅 21:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
کارشناس بین‌الملل فرانسوی: همزمان با تشدید تنش‌ها در منطقه، کاخ سفید با نوعی فروپاشی پنهان مواجه شده است و آن چیزی نیست جز افول جایگاه آمریکا در کشورهای کلیدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/441459" target="_blank">📅 20:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441458">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_DNLHfsrmddFynQr6dXbtIgqU3nzIFNhWum7T3Q5fNSwYtvVa1AXs6VJ2R9YKN1tryXXVvxeYrUT0EJKj-wokHT9Y9hWw8gw_FgXnMtU5tx3TCKRxuOjSt7dDXQXF8u4Ao5BFc1lBLQUYkBZkWgrxevPO1FjRf0SaYqVHDMkTCkPURiecV0R96j6HR1RvRvW9QZBsJhscZHvWgKUoEVjuUp7zBtNJpOYqe0vygypVzjBSZWbF0oEIb1uAY1e8khzHRNCYEHsobnkmxDmvEVaTWOTzA9XBMNTnL0Min_wcqidJHE1_d_q6ArAM_O2o-N28B5xJ2j4gChkxw8yp62oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط بطلان آمار و ارقام بر ادعاهای ترامپ درباره تنگهٔ هرمز
🔹
رئیس‌جمهور آمریکا روز گذشته ادعا کرد که ارتش این کشور در هفته‌های اخیر موفق شده ده‌ها میلیون بشکه نفت را به‌طور مخفیانه از تنگه هرمز عبور دهد و بدین ترتیب مانع از جهش بیشتر قیمت‌های جهانی انرژی شود.
🔹
او گفت در نتیجه عملیاتی مخفیانه بیش از ۱۰۰ میلیون بشکه نفت از تنگه هرمز عبور کرده و بیش از ۲۰۰ کشتی تجاری با امنیت کامل از این گذرگاه راهبردی عبور کرده‌اند.
🔹
با این حال، بررسی داده‌های کشتیرانی، اظهارات مقامات آمریکایی، گزارش‌های رسانه‌ای و داده‌های موجود از ارقامی که ترامپ مطرح کرده از جمله عبور «۱۰۰ میلیون بشکه نفت» حمایت نمی‌کنند.
🔹
پیش از آغاز جنگ، روزانه حدود ۲۰ میلیون بشکه نفت و فرآورده‌های انرژی از تنگه هرمز عبور می‌کرد. بنابراین ۱۰۰ میلیون بشکه معادل تنها پنج روز از حجم عادی انتقال انرژی پیش از جنگ است.
🔹
شبکه الجزیره در گزارشی نوشته چنانچه حجم تردد دریایی پیش از جنگ مبنا قرار گیرد انتقال ۱۰۰ میلیون بشکه نفت به عبور حدود ۷۰۰ کشتی از تنگه هرمز نیاز دارد.
🔹
نشریه تخصصی «لویدز لیست» نیز تعداد کشتی‌های عبوری از زمان آغاز بحران را ۱۴۲ فروند برآورد کرده و شرکت «کپلر» که بالاترین رقم را ارائه داده، از عبور ۲۶۴ کشتی خبر داده است.
🔹
حتی اگر بالاترین برآور مبنا قرار بگیرد با سطح ترافیکی که بتواند انتقال ۱۰۰ میلیون بشکه نفت را توجیه کند فاصله زیادی دارد.
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/441458" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۲.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/441456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-61.pdf</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/441456" target="_blank">📅 20:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
قرارگاه خاتم: پاسخ نیروهای مسلح به تجاوز و شرارت‌های آمریکا تداوم خواهد داشت
🔹
توقف حملات آمریکا به مناطقی در جنوب ایران بنابر اعلام رئیس‌جمهور آن کشور، به‌دلیل پاسخ قدرتمند و کوبندۀ نیروهای مسلح جمهوری اسلامی ایران است که در این رابطه شکست دیگری بر ارتش…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441455" target="_blank">📅 20:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441453">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a60b1aa8a.mp4?token=uWCFeBVSNZJhKTOdUnvRSj-nNp0tzh7Kfy2mRD2wwlh8Hyol0juxue1YXHjFvYOgxtuLSHP1xMVRvTRZnqHyIoRgQU1PKYUoAh5_w0-cBnWcvS3p8Vu8bTbgdLszmClse_0onjgprXvGdwnse6NIxQDye6dZqozyvvoxjJEOJSlqmKzrndMC_EJ0nXR9W3YRDV--DYv1waOoFsItRLHx3SwxWxHiCPQOHfFWVkSngSTTSGarXWgZJUkqt8jm_Jlqqj8MOgYindj5RreoW_6xMsuYf8uuJjAu7ZoFZn1QFO7URnee8AFn1oP3lZbUBrzaj3whriHv-EZ_iuQMHPVmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a60b1aa8a.mp4?token=uWCFeBVSNZJhKTOdUnvRSj-nNp0tzh7Kfy2mRD2wwlh8Hyol0juxue1YXHjFvYOgxtuLSHP1xMVRvTRZnqHyIoRgQU1PKYUoAh5_w0-cBnWcvS3p8Vu8bTbgdLszmClse_0onjgprXvGdwnse6NIxQDye6dZqozyvvoxjJEOJSlqmKzrndMC_EJ0nXR9W3YRDV--DYv1waOoFsItRLHx3SwxWxHiCPQOHfFWVkSngSTTSGarXWgZJUkqt8jm_Jlqqj8MOgYindj5RreoW_6xMsuYf8uuJjAu7ZoFZn1QFO7URnee8AFn1oP3lZbUBrzaj3whriHv-EZ_iuQMHPVmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیفا آزادی‌خواهان هائیتی را از جام بیرون کرد
🔹
جیمی‌جامپ برنامه‌ای که هر روز به حاشیه‌های جام‌جهانی می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/441453" target="_blank">📅 20:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP5M8qiyE8wOPXdEp2MXSt_92CNrWlhBUWvKOMNG_qriPrpO6P3ijcOAeuIuwLkUluhNCZ2YC7XhL97AVtkRw8c7nK5ZjFKlvihYai_XujBWI1LPuO0S3-Jweybb0QZBM4DUIh7uT87sEO3wAMuTpg6CQ7tnigHWV-43QXDnXCNJrfF4hd5ag9uyE_T5JvQa4uLBUE_rH3aAT1Zk_nwD8nekPv4hh4_pRThjYcMp1dOvQVF8UCGW41XrtLsCUBumKu6pkREN7L1d0aY-xu3e21qLM-2Ftw-tlJFbfpV0hFdRg9Mq4oQFWkawwGyTruRFT720iTeSE38PVr1bVraaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان با سرعت ۱۱۹ کیلومتر بر ساعت زابل را درنوردید
مدیرکل هواشناسی سیستان و بلوچستان: طوفان گردوخاک امروز شهرستان زابل را با سرعت ۱۱۹ کیلومتر بر ساعت درنوردید؛ گردوخاک دید افقی را تا ۲۵۰۰ متر کاهش داد.
عکس: ابوالفضل شهرکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/441452" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd3378cff.mp4?token=B2RN2v1vCf34ABqi7jl2OnBT2oCnOVWGUZVJQwvwRwucRn-MytSoRToKZ10yrzVZZh9MHYiSlsbCeI3tXUCRYvDuZwzlhMruenG1iTJvmbyLxcG8HjjF5GndVKpSJ0ad_VZiyiubLvY9TWzCBuAltQIAlAFBwaHQVQqrJxSAVJHnkqUmghhX6YNAFWeYZDt6QdhV5Y8Ihli08j2tCtK216MjiN4fNwzhClMM16XMgp1NVY2siF49gxhln06zst1j7C8Bf-F0Y2w_zMBY7btR1vent1iINDwZGZ6FWhY7C0PrJ1D8lBzsKXiRvGe0QF_eKTuoH7y1RYp73dtzi8sjczO3PpNK00LSVwgXS9d7Amc5zlvLwrPYo4bsoByGiba3cQOv25tfTdBjJ-IbAsspGwYbFZz3TNlVN1YhzAIKNWkozoAwFlQkG7xEyLaBmJETqdNv7m7St3bxlPV_HtlwcLEFV4A2_XKCbicYJPnVQyOZ7azzAJ9fq65wdJZPU6s8ZF19rQTaFKTCkIGfVR2WxOnTm4USWj24G8b483qXUy3jtmHE9FGObI1gm6cSUx6Zx4dUTbgrlYCdB8i6yDkbAUu0RnQSz-tH022yGZocvhlHIil8DDrsoWZEibpYoNETaM2rSPu8zN_m25IlZQd8y-aYoMSeLWlrMrpRo_zcx6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd3378cff.mp4?token=B2RN2v1vCf34ABqi7jl2OnBT2oCnOVWGUZVJQwvwRwucRn-MytSoRToKZ10yrzVZZh9MHYiSlsbCeI3tXUCRYvDuZwzlhMruenG1iTJvmbyLxcG8HjjF5GndVKpSJ0ad_VZiyiubLvY9TWzCBuAltQIAlAFBwaHQVQqrJxSAVJHnkqUmghhX6YNAFWeYZDt6QdhV5Y8Ihli08j2tCtK216MjiN4fNwzhClMM16XMgp1NVY2siF49gxhln06zst1j7C8Bf-F0Y2w_zMBY7btR1vent1iINDwZGZ6FWhY7C0PrJ1D8lBzsKXiRvGe0QF_eKTuoH7y1RYp73dtzi8sjczO3PpNK00LSVwgXS9d7Amc5zlvLwrPYo4bsoByGiba3cQOv25tfTdBjJ-IbAsspGwYbFZz3TNlVN1YhzAIKNWkozoAwFlQkG7xEyLaBmJETqdNv7m7St3bxlPV_HtlwcLEFV4A2_XKCbicYJPnVQyOZ7azzAJ9fq65wdJZPU6s8ZF19rQTaFKTCkIGfVR2WxOnTm4USWj24G8b483qXUy3jtmHE9FGObI1gm6cSUx6Zx4dUTbgrlYCdB8i6yDkbAUu0RnQSz-tH022yGZocvhlHIil8DDrsoWZEibpYoNETaM2rSPu8zN_m25IlZQd8y-aYoMSeLWlrMrpRo_zcx6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ وزیر علوم: مجازات قضایی و انتظامی برای کسانی که در دانشگاه پرچم مقدس ایران را آتش زدند
🔹
کسانی که پرچم منحوس پهلوی را در دانشگاه برافراشتند و پرچم مقدس جمهوری اسلامی ایران را آتش زدند، از لحاظ قضایی و انتظامی به پرونده‌شان رسیدگی شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/441451" target="_blank">📅 20:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441450">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN7JvXtqe5tf7VttI4xqwwSRrOc9owJZcuws8u-gUkyJmS5iv4gdAGfvj2590S9LyV4OxPxA2RFMAg2ScnEtHeky_MLOKmrp7rD7lxqTYI9W1l00kzEr1EijT4iXSsYS5uZwC2o9Dz12eNDa1IqUqZruU_yzhAZFbBT8h5xHAvdJkld7b3Iwh7SkMNDF35-iqQZVW3gRpKQVenT0oteEWKsKBn63JmNbnoukW3FS8EBYJJXJV911-C_MEnfpIfBZeQ5Hyx3-Aw0LszDflHtWBi23bZ68eWWa64obSgsVXhcSd00MIuuxCe2IHUOnSg9tUep7fhsZh1SF-N8bqm_wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم تشییع رهبر شهید انقلاب در خارج از کشور برگزار نمی‌شود
🔹
دبیر ستاد تشییع و وداع با رهبر شهید انقلاب اسلامی: هیچ برنامه‌ای برای برگزاری مراسم تشییع در خارج از کشور وجود ندارد و تمامی تمهیدات در داخل کشور در حال برنامه‌ریزی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441450" target="_blank">📅 20:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKWwsWgH_3aevHduS-U36zoMeZm20TYvS-s8whIKRrB34V5LXOTLDoRNlgV4YbjGMBG74EHWT-xMdjseKhdxqJz71ZB6folqWtPQJtG6E0RKSkm4_hsPVj97kaSpU0bBavkr49ujl-8P5OH8dIPyEFJK5Y4zyRU398cDgI5MUr3VVrKNCa3jvzIcx5BcQ4JFDYYFLY33bF5soXc2_aJILdtgZATy4iAIDy4VS5q8guzYjtf2RBJhFHdYSGZ2Xcep08CY4-C9_DOOnMw_xNmEYeweX3EBr6PmkRtOvUx0yaWer4qtIaHCpgmk45iEfpKYYKySnbrl1O0uzFCz_z4oAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: محل استقرار جنگنده‌های آمریکایی منهدم شد
🔹
در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا، برای تنبیه متجاوز صبح امروز با ۱۲ فروند موشک…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/441449" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_jgd7HkMbKYFAU3Q6CZHZjIN5TcZoNqBcK4nIUblcy4KppT8AQ1gEd_zD5YxWBq6zW7Fn22BgGQD8ptGGQY-D0e-g70WyBqNKcNhIgrg6UGLeiZAARqhiDUfAX6j2gRLBgibny60wX8jLKImSDVTYO84fkjvOZK8xz5CNGS_DisHSUzoZYkz0yPBjqx_R2_oG1qCWOiZF_k6kEHxGAaL4zNgsvQ_6tz4kP_805zFAGwBDYpGDIeGwfn0TaNYXb9H-mnROqyRfbtR5ZmOv4nHTFE3R4EOwMn4NMZN9iEPVZ8omtXSMzC2L9EKiKiex3L4hT6MkXElsyPfELFL16TKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: پیروزی نهایی از آن حزب‌الله است
🔹
فرمانده نیروی قدس سپاه: رژیم صهیونیستی باید بداند که اشغالگری، تجاوز و جنایات مستمر علیه مردم جنوب لبنان هرگز اراده ملت مقاوم لبنان و رزمندگان حزب‌الله را در هم نخواهد شکست.
🔹
جنوب لبنان همواره سرزمین عزت، مقاومت و ایستادگی بوده و خواهد ماند.
🔹
حزب‌الله به عنوان نماد مقاومت و عزت امت اسلامی، همچنان در خط مقدم دفاع از لبنان و مقابله با زیاده‌خواهی‌های رژیم اشغالگر باقی خواهد ماند و وعده الهی مبنی بر پیروزی حق بر باطل تحقق خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441448" target="_blank">📅 19:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkHZjgKrVK7vIZ4jlbJgCEeiuaprO4vEICGlH6LgdPrOLCnD8iVZi1JTr_XoZTrRZiRxdIi6DAC9HKdgsEMjHnmc-N7S495M7uDYECZNWkBgcd0z0e7iRXUUgBGsglEJIIiTXRWK1SuAe27CqumU_PHQwwuKLOl2ZIb0cG2uZwZUiGJOXpwnW_ib5Zt8IY03NAW521q93ik5XBNtgQ91oCAI5ilyf9DrC9agd3BmhI6Upt37SLJddjUVe3fyIIyYpNTIacPxcCgHv16XVPYTqchdU5INZtK7MdIETRJGP3GRQ07UJiVHFSA6fq-hUVpm4bXm8Brz6zzUyRvIdImKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: تصمیمات بدون فکر، زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند
🔹
این کارها مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.ایرانی متفاوت خواهید دید! @Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/441447" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جنگ روایت؛ چگونه ترامپ قیمت نفت را مدیریت می‌کند؟
🔹
در حالی که توجه افکار عمومی به تحرکات نظامی آمریکا در منطقه و آرایش نیروها در خلیج فارس معطوف شده است، کارشناسان معتقدند یکی از مهم‌ترین میدان‌های نبرد میان تهران و واشنگتن نه در دریا و آسمان، بلکه در عرصه روایت‌سازی و جنگ رسانه‌ای جریان دارد؛ عرصه‌ای که می‌تواند بر بازار جهانی انرژی و حتی معادلات اقتصادی کشورها اثر مستقیم بگذارد.
🔹
در هفته‌های اخیر، دونالد ترامپ و برخی مقام‌های آمریکایی بارها ادعاهایی درباره توانایی واشنگتن برای مهار کامل ایران، کنترل تنگه هرمز یا از بین بردن ظرفیت‌های نظامی جمهوری اسلامی مطرح کرده‌اند؛ اظهاراتی که بسیاری از تحلیلگران نظامی آنها را فاقد پشتوانه عملیاتی و بیش از آنکه توصیف واقعیت میدان باشند، بخشی از یک عملیات روانی ارزیابی می‌کنند.
🔹
به گفته ناظران، مخاطب اصلی این پیام‌ها نه نیروهای نظامی ایران و نه حتی افکار عمومی داخلی آمریکا، بلکه معامله‌گران نفت، مدیران صندوق‌های سرمایه‌گذاری، شرکت‌های بیمه دریایی و فعالان بازار انرژی در مراکز مالی جهان هستند. هدف از این روایت‌سازی، القای ثبات و کنترل شرایط از سوی آمریکا و جلوگیری از شکل‌گیری انتظارات افزایشی در بازار نفت عنوان می‌شود.
🔹
برخی کارشناسان رسانه‌ای معتقدند در چنین شرایطی، تمرکز صرف بر پاسخ‌های سیاسی یا واکنش‌های احساسی به شخص ترامپ نمی‌تواند اثرگذاری لازم را داشته باشد. آنچه اهمیت دارد، ارسال پیام‌های دقیق، سریع و معتبر به همان مخاطبانی است که آمریکا در تلاش برای تأثیرگذاری بر آنهاست؛ یعنی بازارهای جهانی و بازیگران اقتصادی بین‌المللی.
🔹
بررسی تجربه بحران‌های پیشین نیز نشان می‌دهد هرگاه خلأ روایت از سوی ایران ایجاد شده، طرف مقابل توانسته تصویر مطلوب خود را در بازارها تثبیت کند. از این رو، همزمان با اقدامات میدانی و دیپلماتیک، حضور فعال در جبهه رسانه‌ای نیز به یک ضرورت راهبردی تبدیل شده است.
🔹
تحلیلگران تأکید می‌کنند دستگاه‌های مسئول باید پس از هر ادعای اثرگذار آمریکایی، در کوتاه‌ترین زمان ممکن روایت جایگزین خود را با ادبیاتی قابل فهم برای بازارهای جهانی منتشر کنند؛ روایتی که بتواند ارزیابی واقعی‌تری از ریسک‌های منطقه‌ای ارائه دهد و مانع از شکل‌گیری برداشت‌های یک‌جانبه شود.
🔹
در این چارچوب، کارشناسان پیشنهاد می‌کنند علاوه بر پاسخ‌گویی سریع، اقدامات رسانه‌ای پیش‌دستانه نیز در دستور کار قرار گیرد؛ به این معنا که ایران صرفاً منتظر ادعاهای جدید واشنگتن نماند و با تولید مستمر روایت‌های معتبر درباره واقعیت‌های میدانی و ظرفیت‌های بازدارندگی خود، ابتکار عمل را در فضای رسانه‌ای به دست گیرد.
🔹
به باور ناظران، نبرد کنونی تنها در عرصه نظامی یا دیپلماتیک جریان ندارد؛ جنگ روایت‌ها به یکی از ارکان اصلی رقابت ایران و آمریکا تبدیل شده است. در چنین شرایطی، غفلت از میدان رسانه می‌تواند بخشی از دستاوردهای میدانی را خنثی کند و برعکس، یک راهبرد رسانه‌ای فعال و هدفمند قادر است هزینه‌های عملیات روانی طرف مقابل را افزایش دهد.
🔹
یک کارشناس حوزه رسانه و انرژی در این باره می‌گوید: «مخاطب اصلی پیام‌های ایران نباید صرفاً ترامپ باشد. مخاطب واقعی، بازارهای جهانی، بورس‌های انرژی، شرکت‌های کشتیرانی و سرمایه‌گذاران بین‌المللی هستند. هرچه این پیام‌ها سریع‌تر، دقیق‌تر و حرفه‌ای‌تر منتقل شوند، اثرگذاری عملیات روانی آمریکا کاهش خواهد یافت.»
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/441445" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پنتاگون در وضعیت قرنطینه قرار گرفت
🔹
رسانه‌ها از قرنطینه پنتاگون و تخلیه طبقات آن خبر می‌دهند.
🔹
سی‌ان‌ان گزارش داد که تیم‌های مقابله با مواد خطرناک پنتاگون اعزام شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/441444" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8559da74.mp4?token=NfvNz4pwLbV8Pb6JZ8hQHz2sphqR3v-GP_V27YCY37ceVlMruAXulR1LfUnOZKVHbaZYrfNiCwgJ1abh7Yowk4nGD_4Pesxvc0XLK9jINWeHMpXVy9B_x4AZdR9ZhBJw9lqoLhwfO3wzIff15h61uuJeEYoO9J20J1N7TEQbpOEAs1i2DBE_vC35avjVLOUuBqiGfOfKZpCoMmc3Z-qq0HY1qcyMz7VhHoKbg0Hv9hCYifxobGt9uW3w2JzE2wpXhf95JYPpSk7LnuPYh7va5xU_rgcYPOhMuwKFDs5wv6RPzq9Bhj0QroGGnEljx9Sli9h7Op1AeO7s1UkhtXA10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8559da74.mp4?token=NfvNz4pwLbV8Pb6JZ8hQHz2sphqR3v-GP_V27YCY37ceVlMruAXulR1LfUnOZKVHbaZYrfNiCwgJ1abh7Yowk4nGD_4Pesxvc0XLK9jINWeHMpXVy9B_x4AZdR9ZhBJw9lqoLhwfO3wzIff15h61uuJeEYoO9J20J1N7TEQbpOEAs1i2DBE_vC35avjVLOUuBqiGfOfKZpCoMmc3Z-qq0HY1qcyMz7VhHoKbg0Hv9hCYifxobGt9uW3w2JzE2wpXhf95JYPpSk7LnuPYh7va5xU_rgcYPOhMuwKFDs5wv6RPzq9Bhj0QroGGnEljx9Sli9h7Op1AeO7s1UkhtXA10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ هوایی شدید رژیم صهیونیستی به شهر النبطیه در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/441443" target="_blank">📅 19:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa82a40ab.mp4?token=eFcRwabjVcD3BE5ybBXDzoDWtk355bEExmMKEj2_ddZ0k9VG3dBbKAj3b9Kkmq1-0rxazaWq9JXIc7pF2qiBgqQRFJMsBnqd1eCtlA55wlQS2F7MJzok2OdruyMyz0KrYsx0vHK0cGJmkSLzY3Ep1Rrv4Ze7XQOlMpRRYYuIe3IZWSV6Px9B-dDGl-74UxcP_vXojQGHaev-_s2rxn0ZmJUM2Sik8gGNLqQJM11XoHgxjn47mRkEprJQjxDpnflaPDt6FabBEmNb61ZPq5eq_BqtcoSlgxahd7wtcLs6cvPOxwCy9P_Ngdr_DvmGGntM_rPRGDWgFNQWf908k3RsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa82a40ab.mp4?token=eFcRwabjVcD3BE5ybBXDzoDWtk355bEExmMKEj2_ddZ0k9VG3dBbKAj3b9Kkmq1-0rxazaWq9JXIc7pF2qiBgqQRFJMsBnqd1eCtlA55wlQS2F7MJzok2OdruyMyz0KrYsx0vHK0cGJmkSLzY3Ep1Rrv4Ze7XQOlMpRRYYuIe3IZWSV6Px9B-dDGl-74UxcP_vXojQGHaev-_s2rxn0ZmJUM2Sik8gGNLqQJM11XoHgxjn47mRkEprJQjxDpnflaPDt6FabBEmNb61ZPq5eq_BqtcoSlgxahd7wtcLs6cvPOxwCy9P_Ngdr_DvmGGntM_rPRGDWgFNQWf908k3RsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سردار رادان به تهدیدهای ترامپ
🔹
رزمندگان بلدند زبان تهدید را چگونه پاسخ دهند، تا جایی که [دشمنان] مقابل ایران سر تعظیم خم کنند
.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441442" target="_blank">📅 19:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrQoBTjQS3McmoFeRrFJ_boH_zLxYHPqeJ4L6QhtDJpk0QdLoR0KECeHyU6X9O_ohhkEiSDPmDPuiZH_72sm1qmaQfT1bgJ-ZOIVqGLBA4RLmlbUxqp8gHQsrqZTGoobQpG6aWFyR_V8F0Ee04vbvuaSKa6-CG5Ag5bCyLutJx5hPO2ULGL_x-UkNabiOXWkMGWTgLvcVa3Q1rGAItNoDCXdHq_WripPfqVkv1W5yZ1Tz8MFBBzZFsGbnAkdgHhTfS2F4U4AghMa5nUJKWyQoPL8ztHsB_VxvkNJIHi51VC1AhO_4J0AZkvjOto9mAM7okXJ1j-iCkesM5-DGYnCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر موضع ترامپ دربارۀ کنترل بر جزیرهٔ خارک
🔹
ترجیح می‌دهم جزیرۀ خارک را تصرف کنم، اما مطمئن نیستم که تمایلی به انجام این کار داشته باشیم.
🔹
موضوع ایران تمام شده و ما می‌توانیم فردا نیروهای خود را بیاوریم، اما نمی‌خواهم نیروی زمینی اعزام کنم!  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441441" target="_blank">📅 19:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ukl20IhzRwBh2ubt4b5pEVTnz3bqnyI3N1sLbjQnWuftB75mh5sdJ61M3BqJ5cLUmAT1t75aLiQ3M3P1JvytqMQqfUleofN9LRyTbVbXBXNXFaSMxTVRl9OuDqLqNJ2A_lXhQ__41c8DPF7ycTFeTZPzZqwmip8FSzOU3DS2Nwq15-DtRpSUesXgiTdJR5xpckcQO3BQodswPJhEvfTtsURRShoP2LO3Ezwx2odT9fKReyyplhebrkI_DY40f5ydcawZEmxPYnD4AKEC8o4jdya07Z3si_clmdGzZFzNkknoT2p_0r2s9vwGPyUF7R552q84fToYBQmYTE585v-m8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برشی از مستند «آن یک واقعیت است»
🔹
این مستند، گوشه‌هایی از منش، اخلاص، صمیمیت و نگاه رسانه‌ای شهید سلامی را به تصویر می‌کشد که به کارگردانی سجاد سلیمانخانی و تهیه‌کنندگی مرتضی کارآموزیان تولید شده.
📺
زمان پخش: جمعه ۲۳ خرداد حوالی ساعت ۲۱ از شبکه مستند سیما
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/441440" target="_blank">📅 19:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=mSBtwuIgH_FhJErI41nsAqZmtVmpKheGjt4qPcIAnw1NWNVYa5mJp4l-EBkva15Z8FkLr5AwvjXq_ZsVGlPUjUupMN24xLM3SK1W26z8Kp-vRM6_VqOyXDy8lHitRKPTKeilAFmfT0pPr9baDVDP2cBDcBLYWPsMjcMiZZycDAuNXP0MTHNShPhWHL6qbRIQ2ghCjDYAk-oaIr5-T_zvNOLfkTP6UssikPeKLozNCnEwEWppT8FGy6l-nYufYJ_77MyZIUSRwQLNpLsLaFYV3gRf97haq5WNLpiQNDRCh_EpUdKlh5d7cm9I2PHxjFxFs4zex3Kc3_fyTVUX6mjZzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=mSBtwuIgH_FhJErI41nsAqZmtVmpKheGjt4qPcIAnw1NWNVYa5mJp4l-EBkva15Z8FkLr5AwvjXq_ZsVGlPUjUupMN24xLM3SK1W26z8Kp-vRM6_VqOyXDy8lHitRKPTKeilAFmfT0pPr9baDVDP2cBDcBLYWPsMjcMiZZycDAuNXP0MTHNShPhWHL6qbRIQ2ghCjDYAk-oaIr5-T_zvNOLfkTP6UssikPeKLozNCnEwEWppT8FGy6l-nYufYJ_77MyZIUSRwQLNpLsLaFYV3gRf97haq5WNLpiQNDRCh_EpUdKlh5d7cm9I2PHxjFxFs4zex3Kc3_fyTVUX6mjZzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
⚽️
جام جهانی شروع شد؛ وقتشه ردبانکی شی!
❤️‍🔥
اپلیکیشن ردبانک رو نصب کن و با افتتاح حساب، ۱۰۰ هزار تومان هدیه بگیر.
🎁
👥
هر دوستی که دعوت کنی = ۱۰۰ هزار تومان جایزه بیشتر!
🏆
تیم ۱۱ نفره خودتو بساز و بیش از ۱ میلیون تومان هدیه ببر.
⏳
فرصت محدوده!
✉️
عدد ۶ را به 7007666 پیامک کن
📱
یا #6666* را شماره‌گیری کن.</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/441439" target="_blank">📅 19:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocOtKelDniOXFCJLoHH0ED3mrdzUHoXNacChJEttcy1QVn5nYxxhAV5lRjY5GBz0E2ScNcYAlKha9jCRzmdRqTSv6mKpoAnCL5DUAjM5ZcA569uQSZGAEfUF-SMUGMbVQCGPyEbc8HepsfmgKpoqTcf0WBgLYu87KTfwIzw4rw00HQ8a4ZIO79W2jGlgFXAsNzOCg2p8RFX2bnIsuwIF0OChzbq7tIC255o2Ykt2ahkim4yAolK8Wp55KzFeqrbnTvmq19q2-GUQa3hGhjHXfnOq48Wo3Vb6TgJpTVeObgXw9ZdYxGtYtsW6RsHBhHl4uwly27kPY2NJykhXjKCuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
گزارش گروه بین‌المللی مطالعات مس می‌گوید؛
🔰
کاهش چشم‌انداز تولید جهانی مس در ۲۰۲۶/ بازار در سایه محدودیت معادن و ریسک‌های ژئوپلیتیکی
🔻
گروه بین‌المللی مطالعات مس (ICSG) با بازنگری در چشم‌انداز بازار جهانی مس، پیش‌بینی رشد تولید معدنی این فلز در سال ۲۰۲۶ را از ۲.۳درصد به ۱.۶درصد کاهش داد؛ موضوعی که عمدتاً ناشی از محدودیت‌های تولید در برخی معادن بزرگ جهان و تداوم آثار حوادث عملیاتی در سال ۲۰۲۵ است.
🔹
براساس تازه‌ترین گزارش ICSG، کاهش برآورد رشد تولید به افت چشم‌انداز تولید در جمهوری دموکراتیک کنگو، شیلی و اندونزی مربوط می‌شود. همچنین معادن بزرگی مانند گرسبرگ و کاموا همچنان با محدودیت‌های ناشی از حوادث سال گذشته روبه‌رو هستند.
🔹
با وجود این، این نهاد بین‌المللی پیش‌بینی کرده است تولید معدنی مس جهان در سال ۲۰۲۷ بار دیگر با رشد ۲.۳درصدی همراه شود؛ رشدی که به توسعه ظرفیت‌ها در مغولستان، چین، ازبکستان و روسیه و همچنین بهبود عملکرد برخی معادن بزرگ نسبت داده شده است.
ادامه خبر در پایگاه خبری مس‌پرس
👇
https://mespress.ir/x6R3
@mespress_ir</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/441438" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/441437" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441436" target="_blank">📅 19:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmeOhoRTUW1b_xUsu5NPuQhfdWhjlpNl4_WTbYC6TEi8d9eQnmHRTsBpyrAKy3WwV4P5iMIGcwjsXh0D0sg6_-UgJoiW0WIThfb4iGhGCkf0xxm5s0T5TOp2qP7ojbzxcu6B3LC7_Tc4dBfGVcuP279nnHJWHvWNIEeOhRbkrKGuubL5TQ7tZlcNMlkeNsCINV6zroHVMnc2Nx8EzyfAkjN6hVxMEZPTQZ3-tlqWv3VF5xX3LJd3Jz-4xiwLM0gumKFzKDFCMbOsyrvlwdSB_KtMbgXn31iSuRjdiZJmzWtregWBTFVBaLGhjatXly7ptUJQl2RkSXLQhCP8Krwf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون در وضعیت قرنطینه قرار گرفت
🔹
رسانه‌ها از قرنطینه پنتاگون و تخلیه طبقات آن خبر می‌دهند.
🔹
سی‌ان‌ان گزارش داد که تیم‌های مقابله با مواد خطرناک پنتاگون اعزام شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441435" target="_blank">📅 18:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c4af4dfb.mp4?token=I_04__VsvJ73b-k-AANxSrNOCWET0vguPCiGaX01gr8ufeUhG0dBtJiReGIi47rPCom_CCsZimuTJ5DpCLeWeyqmFnJaZeVR4HQW4RLVkWp1ExEVKXOQ27P5f94hM5KJBSgrGFwpTza0SZsIbQ1x0HkRZ6ndV9hMKMLotPyo--4o0VjHF5JPH8wW5MUCUNm3cD__PF5GVEwn6jOLEXw1MJPUKyn81bh8hPBKwSvdvU1m22nE8R59ISL36NHLhn40mQ3EWwZkCcud2np35PukVDZRIGOXAY6eOlOnBoXbj-CofgU5x3vl-cYY3NqrKsJEuVlsrjIBK0ohT-Kn-8i0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c4af4dfb.mp4?token=I_04__VsvJ73b-k-AANxSrNOCWET0vguPCiGaX01gr8ufeUhG0dBtJiReGIi47rPCom_CCsZimuTJ5DpCLeWeyqmFnJaZeVR4HQW4RLVkWp1ExEVKXOQ27P5f94hM5KJBSgrGFwpTza0SZsIbQ1x0HkRZ6ndV9hMKMLotPyo--4o0VjHF5JPH8wW5MUCUNm3cD__PF5GVEwn6jOLEXw1MJPUKyn81bh8hPBKwSvdvU1m22nE8R59ISL36NHLhn40mQ3EWwZkCcud2np35PukVDZRIGOXAY6eOlOnBoXbj-CofgU5x3vl-cYY3NqrKsJEuVlsrjIBK0ohT-Kn-8i0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سردار معروفی معاون فرهنگی سپاه در مراسم گرامیداشت سالگرد شهید سپهبد محمد باقری  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441434" target="_blank">📅 18:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e475b32.mp4?token=NXAYFRAdfGl03KNOOvFLu8zaeH6DC3QdwU0qKHBrNuA3UFHgFHd0Si5BH_MtxnzBfbKY00x9iuRCPhlXNEAwV5aNWDaTdmXbQxmWnCFpxxrpJOomKGL0yHVww0aktoIYX4F9GXzc1mlWVMSbVqxoknx3sN99kcgrdZoaelZwmC2Efy8YLzp6R2xZLwTpDvBee8PnM5lDV52RH6lnQCIZQ8CuTHEt8DxhVVeRh7-dxQ_kKZYr5LuXD0MI4MfSTVnIFWMwc7IDPW5YuuSArT1XEaKHW4hEBMK07Ad3_dtQrOT31HHrzWUkxvZN8r9lIJHo5Qw9GOjeX8SW080D2He4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e475b32.mp4?token=NXAYFRAdfGl03KNOOvFLu8zaeH6DC3QdwU0qKHBrNuA3UFHgFHd0Si5BH_MtxnzBfbKY00x9iuRCPhlXNEAwV5aNWDaTdmXbQxmWnCFpxxrpJOomKGL0yHVww0aktoIYX4F9GXzc1mlWVMSbVqxoknx3sN99kcgrdZoaelZwmC2Efy8YLzp6R2xZLwTpDvBee8PnM5lDV52RH6lnQCIZQ8CuTHEt8DxhVVeRh7-dxQ_kKZYr5LuXD0MI4MfSTVnIFWMwc7IDPW5YuuSArT1XEaKHW4hEBMK07Ad3_dtQrOT31HHrzWUkxvZN8r9lIJHo5Qw9GOjeX8SW080D2He4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف قرار گرفتن سربازان اسرائیلی توسط مقاومت
🔹
تصاویری از عملیات هدف قرار دادن سربازان ارتش تروریست اسرائیلی در شهر خیام، جنوب لبنان، با هلیکوپتر تهاجمی ابابیل توسط سربازان مقاومت.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441433" target="_blank">📅 18:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be371a0dc9.mp4?token=itY7iiIsUNYREb58yt3wuRZvgQZ_h5BN17_d2t6nQt5RfliXCxXisOlKiZ6xf0ECr_jOCD_iLognJTXsHctiUkHjS1GrAuCsaT8ynPwP1d3pKsbMzdfoQ49reWwAShvAd4yjkKoAfGquKZNHVGQ7yOwt3Rn6nq7anTY52EU1O1C85G_F6fFm8qgEDHrd-yM1M1XEraeeaq7lwwYsRWHrDPQkEUebd6-hVVK7V0h4CY1B7nkcR4qnoxrWay54j1Bq_Rm_dp9mtAnit2XXJIozp4RcyLPtaMswtdYa8Tj1SmFtjZ2xEfpZeWvX_2ueTQsOGQf9DEinPX0NnkTf_wPzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be371a0dc9.mp4?token=itY7iiIsUNYREb58yt3wuRZvgQZ_h5BN17_d2t6nQt5RfliXCxXisOlKiZ6xf0ECr_jOCD_iLognJTXsHctiUkHjS1GrAuCsaT8ynPwP1d3pKsbMzdfoQ49reWwAShvAd4yjkKoAfGquKZNHVGQ7yOwt3Rn6nq7anTY52EU1O1C85G_F6fFm8qgEDHrd-yM1M1XEraeeaq7lwwYsRWHrDPQkEUebd6-hVVK7V0h4CY1B7nkcR4qnoxrWay54j1Bq_Rm_dp9mtAnit2XXJIozp4RcyLPtaMswtdYa8Tj1SmFtjZ2xEfpZeWvX_2ueTQsOGQf9DEinPX0NnkTf_wPzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت ۲ پهپاد انتحاری به مقر تروریست‌های تجزیه‌طلب در شمال عراق
🔹
منابع عراقی از اصابت دو پهپاد انتحاری شاهد ۱۳۶ به یک انبار تروریست‌های تجزیه‌طلب کُرد در منطقه «قوش تپه» واقع در شمال اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441432" target="_blank">📅 18:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7ebf4797.mp4?token=KdLlpeFpq6vOznQGRIEQKmIMtCJYwmrv9ilTdsH1Fn8JG_nQo-vzL8-ZgIVFv_oMN48ak5MoTyZAiVN26AnFbL7nBgSVrGmzR6zikq_dyP93GC3jKmgV4m6hdqggkxuQOq1X-qZ10TfL2YC7VuNkxXSgIos-CmZTsuCMIvRymLuV29Hj9zzQBwpc5lZR-A4DUDiL5MWBlbZ1MVGsABPmpY3mvfxlK3a9WpRH413fYFGT4oVRDDobFH5cym_Bhy25SPZsnLEaIwCk6WFvuvbe6XOZcYGkQsYslPiwOb1G5W1Rsb43CQtoFHu0x_zNW715TO6gAlbtdzTkeQKpi2oqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7ebf4797.mp4?token=KdLlpeFpq6vOznQGRIEQKmIMtCJYwmrv9ilTdsH1Fn8JG_nQo-vzL8-ZgIVFv_oMN48ak5MoTyZAiVN26AnFbL7nBgSVrGmzR6zikq_dyP93GC3jKmgV4m6hdqggkxuQOq1X-qZ10TfL2YC7VuNkxXSgIos-CmZTsuCMIvRymLuV29Hj9zzQBwpc5lZR-A4DUDiL5MWBlbZ1MVGsABPmpY3mvfxlK3a9WpRH413fYFGT4oVRDDobFH5cym_Bhy25SPZsnLEaIwCk6WFvuvbe6XOZcYGkQsYslPiwOb1G5W1Rsb43CQtoFHu0x_zNW715TO6gAlbtdzTkeQKpi2oqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سالگرد شهادت سربازان سیدعلی، شهیدان حاجی‌زاده و محمود باقری
🗓
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۹، قطعه ۵۰ گلزار شهدای بهشت زهرا @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441431" target="_blank">📅 18:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d03711bfa3.mp4?token=JoAD7o1ug0iykHmatIomiNONfKj9mgwdQh9Po0OpEttLZPyvZr5P3yWR81oOxvGwZz6ZHVzkhyZQckJTuS_mWV7VWJu7nNqWSOTX_AI-s--RlwPX0qdHsgxpWDwO-VD_kaw2Xa7rGIiBEwYOUELet7nSlzR24BF_4tbHPaNsG2ZfDufAa4DAJC2Voj7RTWOICu7Hnn4T-FDwny5Zydg8jge2R97pcitiMSOB-qEBwiY3M1DEcNogX6sRHIkH2LbqIZqRG2KR2-nTc4kTHQ2e4DIgzbvXv12Di8KtvWt00YE0ONIJlXu0Gl5Ro_Tp_a7rlHOAJBOrqEHIpF3RvrNBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d03711bfa3.mp4?token=JoAD7o1ug0iykHmatIomiNONfKj9mgwdQh9Po0OpEttLZPyvZr5P3yWR81oOxvGwZz6ZHVzkhyZQckJTuS_mWV7VWJu7nNqWSOTX_AI-s--RlwPX0qdHsgxpWDwO-VD_kaw2Xa7rGIiBEwYOUELet7nSlzR24BF_4tbHPaNsG2ZfDufAa4DAJC2Voj7RTWOICu7Hnn4T-FDwny5Zydg8jge2R97pcitiMSOB-qEBwiY3M1DEcNogX6sRHIkH2LbqIZqRG2KR2-nTc4kTHQ2e4DIgzbvXv12Di8KtvWt00YE0ONIJlXu0Gl5Ro_Tp_a7rlHOAJBOrqEHIpF3RvrNBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
مراسم سالگرد شهید سپهبد محمد باقری و همسر و دختر شهیدش
🔸
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۸:۳۰
🔸
مسجد امام صادق (ع) واقع در میدان فلسطین @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441430" target="_blank">📅 18:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a412b1ff3.mp4?token=X6QO6ieFB0rk37TLoNxPeFbtnVJTHT6JtiicXyyGYOwJRAs4a-7uWr8TTZ8R51uTEW5SWZy_KHrhKgbpgp7vxWM0qtgRLSk-jmnSZ6YaiFFvwcuniTmJ_QlxwXueCKtEMpFomMwp8im4A2ZSL4-Dwq30Rkr6GPSNauiJ_RZyDxjF4xT5JhHSiRV624Ge6jynWafnrD36QwO4bdP4w3SOdrDqNi6-_q-8Y_9Iv76ESdMPbS0DDlUq2XmUrM1tk14V656_bj8056UrF5rH2lBREMTHnSIl4XJadQeBxKb2UbkQDe7WaD8aGfjziFVRBr6okKIXWLZhLOA1BFaxwI6uAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a412b1ff3.mp4?token=X6QO6ieFB0rk37TLoNxPeFbtnVJTHT6JtiicXyyGYOwJRAs4a-7uWr8TTZ8R51uTEW5SWZy_KHrhKgbpgp7vxWM0qtgRLSk-jmnSZ6YaiFFvwcuniTmJ_QlxwXueCKtEMpFomMwp8im4A2ZSL4-Dwq30Rkr6GPSNauiJ_RZyDxjF4xT5JhHSiRV624Ge6jynWafnrD36QwO4bdP4w3SOdrDqNi6-_q-8Y_9Iv76ESdMPbS0DDlUq2XmUrM1tk14V656_bj8056UrF5rH2lBREMTHnSIl4XJadQeBxKb2UbkQDe7WaD8aGfjziFVRBr6okKIXWLZhLOA1BFaxwI6uAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله یک پهپاد جاسوسی اسرائیل را ساقط کرد
🔹
حزب‌الله لبنان اعلام کرد که با یک موشک ویژه یک فروند پهپاد جاسوسی «هرون ۱» ارتش اسرائیل را در آسمان منطقه «نحله» در منطقه بقاع (شرق لبنان) ساقط کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441429" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441428">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454bfe434.mp4?token=PeGUHYdEkFz8TcO2rE0ZfpTwXCm_nv9gP3yVF5NDQvN_AFaOS4UkhzMPooR7cf8pAr54i1XtVMNF9DAeU52OzA3cuw0fOP6KWATDst9xq5gMAlnM49ekKi1q7MVuc7tHUeEEiTN8LX-Gt-2E_YiJQZalpuXMOEnBshREXPTVLwkFAonpS9tdJr0s4197FaUJFM4-rdUswMNHp8fNkwfklohEjuvLWmTE1-YnuaFHDOuIXwONollFRVM14mK75ueI7Jzqq7uZmiWEqwe3mt7POrd493sWcBO-cKCKArzh34SqXVVzx12q2roXuQ2WQGg2eJcYH9KjUS-NFJVyFBM56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454bfe434.mp4?token=PeGUHYdEkFz8TcO2rE0ZfpTwXCm_nv9gP3yVF5NDQvN_AFaOS4UkhzMPooR7cf8pAr54i1XtVMNF9DAeU52OzA3cuw0fOP6KWATDst9xq5gMAlnM49ekKi1q7MVuc7tHUeEEiTN8LX-Gt-2E_YiJQZalpuXMOEnBshREXPTVLwkFAonpS9tdJr0s4197FaUJFM4-rdUswMNHp8fNkwfklohEjuvLWmTE1-YnuaFHDOuIXwONollFRVM14mK75ueI7Jzqq7uZmiWEqwe3mt7POrd493sWcBO-cKCKArzh34SqXVVzx12q2roXuQ2WQGg2eJcYH9KjUS-NFJVyFBM56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج وطن‌فروشی مزدک میرزایی
🔹
کارشناس شبکه اسرائیلی اینترنشنال: اگر تیم ایران بازی اولو ببرن شانس زیادی برای صعود دارن و واقعا دیگه نمیشه جمعشون کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441428" target="_blank">📅 17:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441427">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
واکنش رئیس کمیسیون امنیت مجلس به اظهارات امروز ترامپ
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441427" target="_blank">📅 17:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441426">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnqjVB2MiEcklZ5oK_LO8TBe1Okg9xZM_IhaA9by7LB0NONrphhDcTMHxb8pcewGVHyxmJrknRcjjGpbNB0ls38AF3Ng3IuXvU0tZIC6WJzFERR9dhDIJ_ghpelqwpsTlEhpvyBEW6rpO3zwxZrymDC9oCdkSNdY-6I7g8kS_gKj9WOviAXNQpGM2GbMwajS7xtg7bUwomRUh5eRclAHgbTssYHysxlDhSEMK8m3Q7ta625epTZW86IpBTku5dmooFVabMxLn-DBr8q---5IxJOnD8BUTKur7_ZH3rT7SRba7sfbEMyy5XjKrQqq4KGSQClaQzs-2TdliLShVpT52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ترجیح می‌دهیم خارک را در اختیار داشته باشیم
🔹
من از ایران دلسرد نشده‌ام. این توافق خوب است و ممکن است بزرگ‌ترین توافق تاریخ باشد.
🔹
ترجیح می‌دهم کنترل جزیره خارک را در اختیار داشته باشیم. ما هنوز به اندازه کافی به ایران حمله نکرده‌ایم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441426" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441425">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bok75Z7dOFi7CEtdQB6KZWdRFgTNZ3qbJ6c5dHuX3afzxqjasG97XrftoQzoq_3gcvAYjfFpugAGQk0nhpI0rlDr0C-Dt-kMmCU3FP9yGKevxxuSz-Xh18-z0cF8afmmf8SjF6SoIJusRVoQbe4SlOsf3JkutY3NW9ZLuPP88-6KCaronxQWXejT8fzIrFvypfmCaVLc-hhoRuM1HZY43e7Icki6SItEkKFcXdpU8tDW1fxbLE84WmM8WOqI56W1mETSh6ohZMMvtVFOaFgr83LekK-yws4P2-D-fDBLPOi-pkPhY9yvYf202-C_UMhzYzopa-bIGfJvrHRKy4XVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه‌گویی وزیر خزانه‌داری آمریکا دربارۀ پول‌های بلوکه‌شدۀ ایران
🔹
بسنت: هر خسارتی که ایران به متحدان ما در خلیج فارس وارد کند، از محل وجوهی که از حساب‌های ایران برداشت می‌شود، جبران خواهد شد.
🔹
هر عوارضی که به نهاد مدیریت آبراه خلیج فارس پرداخت شود، با برداشت وجوه از حساب‌های آنها خنثی می‌گردد. هر حمله‌ای که ایران انجام دهد، تنها پیامدهای اقتصادی و مالی متوجه آن را عمیق‌تر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/441425" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441424">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZcLAnAWdey7lC52zjVKHxy9x7NIDQ12Cz-tw61aZjjb5icYXhqPjW-PyLMLPEew2afhgtwnBTUPXUbHWzupEWi46qpfZduyFPLiIkhV6c6OczzE_-BZ3SMFyWnVdBmr7EAEcTTPSi_aD0GF9ctbNP4a8MTaL0WxPQmTXJ1KD2Zushz1S8EA2n2wdvwnli3mK4qz5QddgQqMVXlxW1ZBrDjnsmFUDG3D7TbbvULvrbtfz_fZfHQUYWyQIHdzX4YpfuJVH-hgmdmS1cxRSebk4X6ZVW0UzABF80lyPlvDMLcoj24GugJ-gd31qtdUcUsCVRfdpQ3SM8kRr4Plr-UUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آمریکا امشب هم به ایران حمله خواهد کرد
🔹
در آینده‌ای نه‌چندان دور، جزیرهٔ خارک و سایر نقاط زیرساختی نفت ایران را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت. درست مانند کاری که با ونزوئلا انجام داده‌ایم. @Farsna - Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441424" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441423">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تنگۀ هرمز تا اطلاع بعدی بسته است
🔹
نهاد مدیریت آبراه خلیج فارس: تنگهٔ هرمز تا اطلاع ثانوی بسته خواهد بود. از متقاضیانی که مجوز عبور دریافت کرده‌اند تقاضا می‌شود صبور باشند و منتظر راهنمایی‌های آتی بمانند. @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/441423" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV2xzK1DId3alpt9VZWiUkhqx0JU_R61_ZGN9aLObcgXuqofDK17NmopYLBuk36VLiGPR8yxW7EyijqP55kE7o3YOe9WoHogp4Y8-5q0IkxSX9qSU6dubELyWDUNg7WgvTKxdxpnXrddVTkTqohvU_qRqimgKXWoTTlYu4LBJcCIy25euRhMHTvLfXHw_puMf44jm_6duNOaWpBQ6d0GCx-LgJ1y_fLKCiWXcsL2whtidZw9jVbJ6mnvmFCuWItisbeOGGf8WZtkRTBxbr8BZ8HblQ20bqJVT5pnDxYQ1_Rn6OAzJQiTppp5EeNDbYMAPkWuCoqehvkHDX0QIVeIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آمریکا امشب هم به ایران حمله خواهد کرد
🔹
در آینده‌ای نه‌چندان دور، جزیرهٔ خارک و سایر نقاط زیرساختی نفت ایران را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت. درست مانند کاری که با ونزوئلا انجام داده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441421" target="_blank">📅 15:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441420">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piUwlhlAGTKwzK1WDT9LlLjlQycTgHxrTixXaVKPX1X6AF2wU8ZtFQWoJkhd9nsnkfJpL7JsJy-yqwK1P90wFj85ilOR-mERzrz9NpCcfi2xdpTTPbOJMGlJdVX13xvbRQx3dNGd5laEQF0RuJUW5f2VICpm2WPPrpbSJllh1YPHAk9W5ZWp8_50benPlUUZtFHmWkRkjhV26GfRP_biQt-IFhZiY36tWctRRdzibH_T5bCB6FeIjxGK9nikNy2_6wzfwOT2JlQV6m231a_qYcVa6yrIC1rW4Tuqzw6yoHJTEzW2UV9peBTkhNDA1_fbnKB1ZFYU10AwINe2HMN3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت‌های ایلان ماسک در بانک اهداف نظامی ایران
🔹
قرارگرفتن کلیه منافع مرتبط با هلدینگ‎‌های اقتصادی تحت مدیریت ایلان ماسک در غرب آسیا از جمله کشورهای عربی و اسرائیل در بانک اهداف جدید ایران درحال بررسی است.
🔹
این اقدام درپی اثبات استفادهٔ ارتش آمریکا و اسرائیل از زیرساخت تحت مدیریت ایلان ماسک از جمله استارلینک است.
🔹
پیش‌تر کمک نظامی ماسک به ارتش آمریکا از مسیر پروژه‌های استارشیلد و پرتاب ماهواره‌های نظامی در قالب اقداماتی نظیر رصد زمین، ارتباطات رمزنگاری‌شده و انتقال امن داده افشا شده بود.
🔹
ایستگاه زمینی استارلینک واقع در اراضی اشغالی، قطر، اردن، امارات، و عمان در کنار سهام‌داران اسپیس‌ایکس از جمله زیرساخت ۲ شرکت «آلفاظبی» و «مبادله» تعدادی از بانک اهداف جدید ایران هستند.
🔹
یک منبع آگاه به فارس گفت، ارتش آمریکا با پشتیبانی شرکت‌های مرتبط با ماسک دست به جنایات جنگی از جمله حمله به زیرساخت آبی در جنوب ایران کرده و جمهوری اسلامی ایران حق حمله به تمامی تأسیسات مرتبط با هلدینگ‌های تحت مدیریت ماسک در منطقه و اراضی اشغالی را محفوظ می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441420" target="_blank">📅 15:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSXYBadXGklI_e41zOIeKVs8Dd0m7TUpaKZ-G6ywcPC1SckKFwNExJmGK8LGggPjubnvN8RcFAOwxdw46xGElIz_wEy1iVSeu9nkFlzZ_uHJp8Yh1lmVThOK0OgXE4AWVXLmryLKayG_xDnnai8p-koMwXEIwyGLjpoFTU2Xudo6FrjHYjQU07rEjWoInQzlr5s6A0gEvqyjf7Ucvh3leC-fjm_37ZIEb49bt4Mt_BOffcdeAoSQDrf1qnuAW62ncxQHCvW0W1zsBEnN1A712ploDOYvtFl9hDEvI1MX3e2Gc4sQ5d4xwPCIi3vjHH7bPpDP7qlSp6CIFTyMufu0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: آمریکا باید بین پذیرش شروط ایران و تتمهٔ حیثیتش یکی را انتخاب کند
🔹
رئیس‌جمهور نامتعادل آمریکا خیال می‌کند با بمب می‌تواند از باتلاق و بن‌بست خودساخته خارج شود اما با موشک‌های ایرانی، بیشتر در منجلاب فرو خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441419" target="_blank">📅 15:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک منبع نزدیک به تیم مذاکره‌کننده، ادعای سی‌ان‌ان دربارهٔ مذاکرات جدید ایران و آمریکا را تکذیب کرد
🔹
یک منبع نزدیک به هیئت مذاکره‌کنندهٔ ایرانی در گفت‌وگو با خبرنگار فارس، ادعای سی‌ان‌ان دربارهٔ مذاکرات جدید ایران و آمریکا در میانهٔ درگیری‌های بامداد پنجشنبه را تکذیب کرد.
🔹
این منبع آگاه تأکید کرد که جمهوری اسلامی ایران در روند مذاکرات بر مواضع و خطوط قرمز اعلام‌شدهٔ خود ایستادگی کرده و از مطالبات اصلی خود عقب‌نشینی نکرده است.
🔹
به‌گفتهٔ این منبع، متنی که پیش‌تر از سوی طرف ایرانی مورد تأکید قرار گرفته، همچنان مبنای مواضع تهران است و پیش‌بینی تیم مذاکره‌کننده این است که در نهایت طرف آمریکایی ناچار به پذیرش چارچوب‌های اصلی همان متن شود.
🔹
او همچنین فشارهای سیاسی و تهدیدهای نظامی اخیر از سوی آمریکا را ناشی از مقاومت ایران در برابر خواسته‌های غیرمنطقی آمریکا، فراتر از توافقات مورد بحث، دانست و افزود: «علت اصلی افزایش فشارها، ایستادگی ایران بر مواضع خود در مذاکرات است.»
🔹
این منبع نزدیک به تیم مذاکره‌کننده خاطرنشان کرد که متن موردنظر ایران، به‌دلیل تأمین منافع و مطالبات تهران، تاکنون با موافقت کامل طرف آمریکایی مواجه نشده و همین مسئله یکی از مهم‌ترین موانع دستیابی به تفاهم نهایی به شمار می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441418" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441417" target="_blank">📅 14:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1ce80cae.mp4?token=QNX5y_OFWoLX8KsQU9Yvm1GV_GgxlrpLBO5UNnL_gpi2Nc_nsGCZxsC4-j3TuULWLeSnxJunm72l3uBznB7z0ue-KO9isBC8uMdsSWzxxo9_Byr9zWH9Hgd-6uMU3S-NmWt703RbgfhJwqGjFGK4coPtI9Kl4Ibz9Am0o2jS75Ze8m8qRAQb0qAyBI1nGDdDBB9BZph7Fx0NRg4ucVlBTMH5UjAP9wsyESGC_3sD1sRRg8Sl6KWgDJOzGWnCdTabhq2tuzDjpCzId1dvlW5Pl9kUnSMr75hB2N4E-1KoCkFReBQi3ha3nFpSGXTIJFUuDRtlK2OG4KXirOD0nKJSqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1ce80cae.mp4?token=QNX5y_OFWoLX8KsQU9Yvm1GV_GgxlrpLBO5UNnL_gpi2Nc_nsGCZxsC4-j3TuULWLeSnxJunm72l3uBznB7z0ue-KO9isBC8uMdsSWzxxo9_Byr9zWH9Hgd-6uMU3S-NmWt703RbgfhJwqGjFGK4coPtI9Kl4Ibz9Am0o2jS75Ze8m8qRAQb0qAyBI1nGDdDBB9BZph7Fx0NRg4ucVlBTMH5UjAP9wsyESGC_3sD1sRRg8Sl6KWgDJOzGWnCdTabhq2tuzDjpCzId1dvlW5Pl9kUnSMr75hB2N4E-1KoCkFReBQi3ha3nFpSGXTIJFUuDRtlK2OG4KXirOD0nKJSqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیشب کدام پایگاه‌های دشمن آمریکایی مورد اصابت موشک‌های سپاه قرار گرفت؟  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441416" target="_blank">📅 14:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7090843701.mp4?token=SeR5Zx-qpZSdAI47idbKjZ6E3T0ng5wOfT22l5dTk-3y-YXENd3hOyD1WSFQl1P35BA0xdhVjK2IpYVvzfTiEHQ3tk5MB9sPCK75PiZsZpYQNtLiBnrjftBMv411zIvSx9638Zd_j2K7NdoXOEI0J-PiO2YKMPyOT5iNJ3Dz8nYD70bTXAU7VYJY_9vcxnudJ5HZXIoPAuZhaIMaVNLlYuCE-EEi_RCd5TOJxhZE2rYa7YamJML94QN0lpGZuhHCehMH3xONmH-OeMadWjxO2ACokh7y0ll7s9Sc3T5W3NgO8b0cqrOxftJ-V1_xJemKbpiy7SjQRLsK1jWF9idU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7090843701.mp4?token=SeR5Zx-qpZSdAI47idbKjZ6E3T0ng5wOfT22l5dTk-3y-YXENd3hOyD1WSFQl1P35BA0xdhVjK2IpYVvzfTiEHQ3tk5MB9sPCK75PiZsZpYQNtLiBnrjftBMv411zIvSx9638Zd_j2K7NdoXOEI0J-PiO2YKMPyOT5iNJ3Dz8nYD70bTXAU7VYJY_9vcxnudJ5HZXIoPAuZhaIMaVNLlYuCE-EEi_RCd5TOJxhZE2rYa7YamJML94QN0lpGZuhHCehMH3xONmH-OeMadWjxO2ACokh7y0ll7s9Sc3T5W3NgO8b0cqrOxftJ-V1_xJemKbpiy7SjQRLsK1jWF9idU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: محل استقرار جنگنده‌های آمریکایی منهدم شد
🔹
در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا، برای تنبیه متجاوز صبح امروز با ۱۲ فروند موشک…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/441415" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با مسئول سیاست خارجی اتحادیه اروپا
🔹
وزیر خارجه در تماس تلفنی با کایا کالاس، تجاوز اخیر آمریکا را به‌شدت محکوم کرده و آن را نقض آشکار منشور سازمان ملل و حقوق بین‌الملل خواند و اعلام کرد که این اقدامات وضعیت آتش‌بس را بی‌اثر کرده و مسئولیت پیامدهای خطرناک آن بر عهده آمریکا است.
🔹
عراقچی با انتقاد از سکوت کشورهای عضو سازمان ملل در برابر این اقدامات، هشدار داد که انفعال جهانی موجب افزایش ناامنی منطقه‌ای و جهانی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/441414" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260f3e4a1.mp4?token=XzmA0EvqwXNY693WMrMcEJXOAfaKKYTB9tCV5kRsqu-iD3Qcf-vryb4FwDncw5yl9cMiC-iB76we_v-uKF0ne700uspqo-xPc02xKLnE_fSemwqkAtM3KJDktQCdxGmbuU4CSN0pu5pMMZZD5rTjsfBjgFfi55MO-44VHa05K80NdR8Mmch1hYtau4iHrs9baMJJIIGuIZ5fwt6J1ZHJBbvdEQWMTIAFdhv6A1prenQpIQKZ9wlZ0Ut8KQwx2Ff-UyN8GzPRbBpAKbeNw285xwc_qKXMKbNz1GPVdd5VG5JYIVaUIfZOmLumN4g-ZTP-T0SA6LbBHkfno1dcQamTwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260f3e4a1.mp4?token=XzmA0EvqwXNY693WMrMcEJXOAfaKKYTB9tCV5kRsqu-iD3Qcf-vryb4FwDncw5yl9cMiC-iB76we_v-uKF0ne700uspqo-xPc02xKLnE_fSemwqkAtM3KJDktQCdxGmbuU4CSN0pu5pMMZZD5rTjsfBjgFfi55MO-44VHa05K80NdR8Mmch1hYtau4iHrs9baMJJIIGuIZ5fwt6J1ZHJBbvdEQWMTIAFdhv6A1prenQpIQKZ9wlZ0Ut8KQwx2Ff-UyN8GzPRbBpAKbeNw285xwc_qKXMKbNz1GPVdd5VG5JYIVaUIfZOmLumN4g-ZTP-T0SA6LbBHkfno1dcQamTwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار شادمانی فرمانده قرارگاه خاتم‌الانبیا(ص) به شهادت رسید
🔹
سردار علی شادمانی، فرمانده قرارگاه مرکزی خاتم‌الانبیا(ص) که در حملهٔ هفتهٔ گذشتهٔ رژیم صهیونیستی به شدت مجروح شده بود، به شهادت رسید.
🔹
شهید شادمانی از فرماندهان دفاع مقدس بود که عمر خود را برای…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441413" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441412">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
حزب‌الله: تجمع خودروها و سربازان دشمن اسرائیلی در حوالی شهر طیرحرفا در جنوب لبنان با موشک هدف قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441412" target="_blank">📅 13:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3w2Mrp0BgwyR5YwUyK34tOAexxkAWSV5xKOq51_1KP-bvuYR5pTkFukYQB4JqLkpLsiQKSfDG4V0_tA7Ma0K-Bb1SCuZd4umL1itdxBvEQBHL-7lFnnGukvt3ZQ047juEY3osPmEHtqECSBSBEykIJrYBrBaFFwS3MAbaXRplzLwMkjmftyn1y9wWahuHu7HQB0eo3Qkerqp8fTgK34HTll_Pf5qTEa6l9u7gI0H_Jtce7VPbSAQ0mK2PyXttqEO8SsZNvt6AK3EhhTpeuVnKMSuwi3HxZXtEUORHgsl-UzbR8J9l9kGTtzxBMDXaQFgJdlcrN-M2L2IM8gyDx_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTiMVcs_JhmKyQ68tKqskkAUckht66oqHHxiuZ8TV1nEyMtg4TTKeHdrOz8hG3V_uZqSIA9iDIDfoOMP-p5Ogl3Ukrh4Uhe1EJwV2EcRTTFEFS8L0YuaiGFAvMtUGJB59Jd00dQ2_3yPLKk7BayiKft0-bdjqDZVupGXae-_It2nowhkzJXEGYLe_2BCuoSY9w3_u_14gPNBtSjlBLRq36epcFAxL2vXgPGrl4FDUbYLRmJ4ZXYuPfepnVWpt6ROJ4jmu15F3nptTRhpoJ_bF-Mk7bn6VwaMoKCpsxDdm8I1i5nA5_UmkJoF_JmkLjJQ8mXDrNomVOENJbJW37CgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaJxnzMb_LdSnE8dnnmnikaykO5uGtuWvOUqagMjH8TXjEV8zmKaucB23672PW4tFr1McNWsLA4d9lPok2Ruk1A55FxxPwIMc5h9XqjPdqCgpSP31DtdV83kBq1HnwYOk5Kekn7Hp83c2K0rkltztQezMS95DAdMU_FCTmlWZ-nYiYNzXbTPnlQnbT6tCVLHy-JcC8saz3HiGqy1XTLkHoWgePdJZezGNXDo0Ot1jrUsFJimR0OgUh2qg6UswQ3sBgqJUDy_3F-AJ3YZ_D1e57KcEca6TGnXMVxa2YmdchC2Mo1TqYnbePla9OKOVYpcHN5YapTWgSffZD_b8qjHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZH3jP4ft2aLTLm7wspOUYr1940zTqfv0ZmfxnuMPTItm8HWzXWW9PisaDnEKQuAk2dgvjxDPX275YSJID1uJivMS-QiejquLFt3hPuExVqCWinEbDaiH0cMUqXhb4kN-OypR34G3ar8kpKgBX5_2U-6J0YrhlZQ74DNunZH0jTaCx-Vthx5i2tgRokGsJd_gwulnBuke3Ie1YzfWD5aQOkbTkU9qul7-ZdNP0IBqPoZtogJmdxlP0mye459587X3PRwUDOxHVFnZrZAyymo9am5W5rwT2-_QIOm4QB-Hg0yKbvGN9QnlfUkpdC2WZu7579RPbZJKQ2O0xQSWeJ6Rug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HP4TOfrdSECQ4tZlU8fiHBRQ2c2ewGNBgCJbss-cv5GNR07HD9bFvCPDVZBhg5bLCESeTQzs-Q7MMEcyBMgJRXvMOPKVZL9WiW74wfjQyv6iKtv7jvVu1PyzTxT7bq_sHXlUVa4D58zyYEkBI666hblUcawnmb3zBNgy5vcdpe4loqsCryVLwlxQzpNs50WvXlJVdCMHejZm8SkRerJPiW3_eyOpcqpRhq1OQoZ-Q4HjmQfynqiLpfMU1Hp7XVtf9yRcU8PB3klf4b91UWqp1VHL_cnx5XlLf7gqgQnfzZC_aEJ-XknQj9Lvu518OnLQj9553ltLwjJeWOqetviWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2tWdCs0uUSWTzYHXvqZTOnT5A1u0zeAkKLDT5K0Qmy4x-xz3MfO4ztY-Az5qLOH9yfTIEt8c7qHiCIzeJyO68DyT28xSqtUJEBSY0IvkTGLQlhdcnSUqOTmAcfezHynuY16Yps1UOcWzNrjLFbyWCrN2BRmP8toGUZMC_MyzU3uFFc_TDs_O6nMrKTJOzN6EsAuHolb62kGMtnC3BSWkNpiubGogOwcZIKqD5nAI1QepqAnm8t86FIYRYfknUARo4jgeFdIy0NiylfOHIxrWfrMNP_LpgDJGz8ZfW4UvbCbZBJhSY8D97LT0WXcnErlsovPC8NkDq9aKjTl1a0I-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2yviyJEyJvwpQkyDaVawH8LrWcMzZ2zTzQtcZTkM2eCcVsl_I7NfxwvsTGPXils6ew-GPx1ZPGCb_mJ-d7YPl71lWl3Mpelo4eSD2BgEBVeYyrpBhaOZqkoMxnrTnqqoti6_nmhAwyXKWFYbnhRkwYOSBpIBP-ANOntUQOzy3JtgBQw6G0orZVSgH3g4FL2DqNvGxFmK3VDOtVcQo47tdiCOYEEi2g4cWssUk5vcmnq7Fk_zLagrm2Np270AV60Kf6dozMt4w4CBYZR3gaQMtRpMxGnMWkuNkWMIZPC8KSo82tSZJozuxIpe-uCPvJ-BeszjfAQidL6L5f7JoN5Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شهرک‌نشینان اسرائیلی، درختان صد ساله را در نزدیکی الخلیل در کرانه باختری بریدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441405" target="_blank">📅 13:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYCNG-grQLgpQkME3sV0UdSW_whRQ6A2L2G9M9jKGGjdirVKHCAKXB0Nr8fe5GpDXoqGDwem9Q_it_g8nKYAGzaDxn_2nUMPF2Kr7cfNg4v3i6EQVaHf4o0dRvMslLEhqh6kaGclMGOAEIwxWxuuMvaW6XgvHW6ANEVOdpqZtVbptIrO8h9kvkBWswdMBB3nSOt7d9mvDoRTxXhKcrwASxUAO64IuCibC_jjummw6U0PqpmMR0q7pr0kfuXCc1qo8v6RZy82YatzhVPj9ujjb4S0iMd5EW4kPh45wKLVinEeMBjyuTSs-gCv98ZU9fLTIVJr9E5lDXx7b_wO647UIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rInyiN3j6-kXBDEAtNq6B722qqShdgtvOLC779sy9-FTgmyFSbK-quKS6Ykp1OsG1hWyf_CNULEXuNzQgjGu_E_DE9V2inXYRGJDgrMW-6PcG8cTOrAdXh_mLEf1va9Im1330TOZIFeLz_y5qISd_NK_nviaPepFOlZtHHNWVFRvxbhZvq0ydhF2RTzxDFW3W1i6ROF_UbgxLJs2nlIQ6Zaho-JGpCw6V88naTWuIYCLhxKT40J8ZakSbZN7SRB6rlwgyIkI6mSCy7EhEmKQs59NdkTyVEPB5wzN3s3sbcW3jy9hGkprcK_B50NiqvVOO9UTkqTKthpRnoA8pVTerQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
بقائی: تخریب مخازن آب آشامیدنی در سیریک، اوج زوال اخلاقی در سامانۀ حکمرانی آمریکاست
🔹
سخنگوی وزارت خارجه با انتشار تصویر روزنامه نیویورکتایمز که تجاوز نظامی سه‌شنبه‌شب آمریکا به مخازن آب آشامیدنی سیریک (هرمزگان) را اقدامی عامدانه و جنایت جنگی توصیف کرده است، نوشت:
🔹
فیلسوف فرانسوی، سیمون وی، در توصیف جنگ نوشته: جنگ، بیش از آنکه رویدادی در سیاست خارجی باشد، تجلی سیاست داخلی است.
🔹
از این منظر، حملۀ آمریکا به مخازن تامین‌کننده آب آشامیدنی مردم، یکی از لحظه‌‌هایی است که ماهیت واقعی قدرت، نقاب از چهره برمی‌گیرد.
🔹
قدرتی که دهه‌ها خود را با مفاهیم فریبنده‌ای چون حقوق بشر، نظم بین‌المللی و مسئولیت اخلاقی تعریف کرده بود، هنگامی که مخازن آب آشامیدنی مردم را تخریب می‌کند، نه فقط به یک تاسیسات غیرنظامی، بلکه به بنیان روایت دروغین خویش شلیک می‌کند.
🔹
امپراتوری‌ها زمانی سقوط نمی‌کنند که دشمنانشان نیرومند می‌شوند؛ امپراطوری‌ها هنگامی رو به زوال می‌روند که دیگر نتوانند میان آنچه می‌گویند و آنچه رفتار می‌کنند پلی برقرار کنند.
🔹
زمان زوال قدرت‌ها، لحظه انهدام دیوارهای قلعه‌هایشان نیست، بلکه لحظه فروریختن اعتبار کلماتی است که سال‌ها پشت آنها پنهان شده‌اند. آنچه بعد از این بی‌اعتباری اخلاقی باقی می‌ماند چیزی نیست جز همان که تی‌. اس. الیوت گفته:
صورتی بی‌هیئت
سایه‌ای بی‌رنگ
نیرویی ازکارافتاده
حرکتی بی‌جنبش!
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441403" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سازمان بسیج: نیروهای مسلح نقض آتش‌بس را بی‌پاسخ نخواهد گذاشت
🔹
بیانیۀ سازمان بسیج مستضعفین: ما ملت ایران که در بیش از ۱۰۰ روز سپری‌شده از جنگ رمضان، تاب‌آوری‌ بی‌نظیر و بی‌مثال و قدرت تمام ناشدنی خود را به جهانیان نشان دادیم، اینک به دشمنان علی‌الخصوص رژیم آمریکا اعلام می‌کنیم ایرانِ سربلند و نیروهای مسلح مقتدر آن، هیچ‌گاه نقض آتش‌بس و تعرض به حریم خاکی و آبی خود را بی‌پاسخ نگذاشته و نخواهد گذاشت.
🔹
دفاع جانانۀ رزمندگان اسلام در جنگ‌های تحمیلی اول، دوم و سوم، عملیات‌های غرورآفرین در خلیج فارس و شکار پرنده‌های متجاوز آمریکایی، گواه روشنی از این حقیقت است.
🔹
امروز نیز بسیجیان غیور، آماده‌تر از همیشه‌اند تا در سنگرهای دفاع از میهن اسلامی، پاسخ هرگونه ماجراجویی را با قدرت و سرعت بدهند و دشمن را پشیمان کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441402" target="_blank">📅 13:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22766b2a2.mp4?token=h0MexuQ5fEKC3NAlDtw3ueatmGVREeJxZmpA3yMU58Q7MPXum3cBfBGSf_DUPTiBVNlGdIOKXbbBXjYeL0wxxHzA_h7kx6fMj1tk-5vGIf64I1mKEg8IYLBIrcKZPs_t1K_jI69NWU_67aqec_cf926fiagMNf-5DWaqkMRpfHLRrZiHIzK-Xudfr2iqe5BkjrQg4Kfo8LWy9iGUQ-nvfvpurYu0Wp9wbadZWUgvjoUimo1etd9JkxxChb9GEphM3ruEllzhYVrW4TGip_0vYIOSy0EhMEer_QEf0DwiI4VzemGH0aBkX29fnhwCewGcZkY0TmoGjYn6YzKy0gUBLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22766b2a2.mp4?token=h0MexuQ5fEKC3NAlDtw3ueatmGVREeJxZmpA3yMU58Q7MPXum3cBfBGSf_DUPTiBVNlGdIOKXbbBXjYeL0wxxHzA_h7kx6fMj1tk-5vGIf64I1mKEg8IYLBIrcKZPs_t1K_jI69NWU_67aqec_cf926fiagMNf-5DWaqkMRpfHLRrZiHIzK-Xudfr2iqe5BkjrQg4Kfo8LWy9iGUQ-nvfvpurYu0Wp9wbadZWUgvjoUimo1etd9JkxxChb9GEphM3ruEllzhYVrW4TGip_0vYIOSy0EhMEer_QEf0DwiI4VzemGH0aBkX29fnhwCewGcZkY0TmoGjYn6YzKy0gUBLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌نوشتهٔ شهید فرشته افشردی، دختر سرلشکر شهید باقری، که در میان آوار‌ها به‌جا مانده‌ بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441401" target="_blank">📅 13:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
حزب‌الله: تجمع خودروها و سربازان دشمن اسرائیلی در حوالی شهر طیرحرفا در جنوب لبنان با موشک هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441400" target="_blank">📅 13:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حملهٔ دشمن آمریکایی به یک لنج باری متعلق به اهالی سیریک در دریای عمان
🔹
فرماندار سیریک: بامداد امروز پرتابه دشمن آمریکایی به یک لنج باری از شهرستان سیریک هرمزگان در دریای عمان اصابت کرده است.
🔹
این لنج باریِ حامل کالاهای اساسی، ساعت ۵ صبح از شهر خصب کشور عمان به‌سمت شهرستان سیریک در حرکت بود.
🔹
شناور مذکور که در ۵ مایلی بندر خصب مورد اصابت پرتابه دشمن قرار گرفته، ۵ خدمه داشت که با کمک شناورهای عبوری نجات پیدا کرده‌اند و به کشور عمان انتقال داده شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441398" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdSsgJ7juTHCmPtk-Q936ffj9FTlKrBnz-349AnSAnAdw23FByyh76D7Fb6UpKnccYUtVTqJOGWzufV_-Dp0eY_VuG2qPkLWz385ZH4ePWpDZRY2-NxyDlAIgPVIWC2mzud41QA217PUJ3IGankt5lt4cZmnuXsz2ectmoA4Fre-JC1Fr_Y4FZj7k0c0b-Pb9jjdm8amzWAZBwnoHt8bZBMCdeHPH0Kt4acjt-vmIPscfklNTsrIPPKMH2GT9ayL_8Je47juoVlNNO9qbD6Cu_XrYWt-vnSvR5rIySo0KPUeIWPLiL-jzAvJ8xQT7mkX35LuV36Ktt5vAuzi5vQW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناجات و توسل به امام زمان(عج) در سوگ رهبر شهید انقلاب در رواق کشوردوست
🔹
زمان: پنجشنبه ۲۱ خرداد، ساعت ۲۰:۳۰
🔹
مکان: خیابان جمهوری اسلامی، تقاطع کشوردوست
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441397" target="_blank">📅 13:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDDIuuYemMr3SMWdKSfBxj5mdVihkDM2NWBtNFgVYqpbUfmhfsxcQXyFYZi4gO548v_iEdvtsjTDzUzAqBNRT2D-fVQhk1DiFn4X-FJh41Zxl9F-zzqKRx9KUC_DgnZy7rOVYo0hOPd5S1CxAGtnkyPMw3lW_BDnG6z_XuLkY7cmTPiIex9MJVqOP3QxUY-qItu6XrfXOu7XPTjNZPQilLCOyvfXncESljNHeEwab7rI7vPu7tu5YHxROmrsnskT9emCqAIUntS5YUzfiMJcdCRI56fr70WmBv4rS5LhBP3y8CfH9Aee4kJDLoVNxFcwAhdmxF3eMbHjgjQD9iPcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کلمبیا: جنایات اسرائیل در غزه مشابه دوران نازی‌ها است
🔹
پترو در نشست شورای امنیت سازمان ملل: اسرائیلی‌ها بر سر مردم، حتی کودکان، موشک می‌بارانند. این آمارها قابل پنهان کردن نیست و هیچ منفعت سیاسی یا اقتصادی نمی‌تواند این واقعیت را مخفی کند.
🔹
وجه مشترک اصلی تمام آنچه امروز می‌گویم این است که ما در حال بازگشت به عصر نازی‌ها هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441396" target="_blank">📅 13:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_7_AQ7c3UOiJU5KMgltBuBMHVlsQuigSAuY3PomPISJ8mEWq6cus_e7OJIyE2TRRF_RKQ9i5qa-arWu1RhMsbK7OCRb8nJArFnfwT80qVylHjZbP6wyDCc-ZMbNRLpTRg7zQzH-RJzhzrYtJxlT-DU41gVs5GKNytDPqjr1TPCFRNbujcvn3brI21bmVjbd-_IC5VrTjH8z0EZewuT43Hn0D5nqQQIVE846cbHNY8PTC0oh29VbYHTsZXpp3E4mGej1noCH0ioCEtfcNYNsq4pGjhlzDdhA0nRh0swdir2DzfGN0t9N9szSzhl-anadgLRSvKSxLraeTB-vygZipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز تا اطلاع بعدی بسته است
🔹
نهاد مدیریت آبراه خلیج فارس: تنگهٔ هرمز تا اطلاع ثانوی بسته خواهد بود. از متقاضیانی که مجوز عبور دریافت کرده‌اند تقاضا می‌شود صبور باشند و منتظر راهنمایی‌های آتی بمانند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441394" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441393">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705688d463.mp4?token=eDFLIOE1y4OmpIxP5c9wCa79L4UaBnQXvErhlxmaM42oYwLXdePp-EXFu7dY5Az7F0yxsAGaheVLiWkGpZ0Lgl09_TX044mIl_Ijdkwa0EsptqlMc1RtgJ2UF3GaWN0KRrSV5tmQtBWxkl8ozHqw9ILTC2_fUxHHbB25KV9I6kl_S62jah4EBycb_kV50ToRuYbil5h965XVbCIIUnsGNNmWVjoUleBGwCY7KmBa_Y-bOndEf9O9KNe0Rfg_gAnpbIEtqpgmA4qzh7D2U-nU2Jzb7AXBMM37hVXakldyBZHvl7nVqMXmQ1WS5WOma45gOY1gO-nIYrMsU3AyrRHegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705688d463.mp4?token=eDFLIOE1y4OmpIxP5c9wCa79L4UaBnQXvErhlxmaM42oYwLXdePp-EXFu7dY5Az7F0yxsAGaheVLiWkGpZ0Lgl09_TX044mIl_Ijdkwa0EsptqlMc1RtgJ2UF3GaWN0KRrSV5tmQtBWxkl8ozHqw9ILTC2_fUxHHbB25KV9I6kl_S62jah4EBycb_kV50ToRuYbil5h965XVbCIIUnsGNNmWVjoUleBGwCY7KmBa_Y-bOndEf9O9KNe0Rfg_gAnpbIEtqpgmA4qzh7D2U-nU2Jzb7AXBMM37hVXakldyBZHvl7nVqMXmQ1WS5WOma45gOY1gO-nIYrMsU3AyrRHegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط بالگرد ارتش پاکستان با دست‌کم ۲۲ کشته
🔸
ارتش پاکستان با وجود اعلام این خبر، تعداد دقیق سرنشینان را اعلام نکرده اما رویترز به نقل از منابع امنیتی گزارش داده که دستکم ۲۲ نفر در پی سقوط این بالگرد نظامی در کشمیر کشته شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/441393" target="_blank">📅 12:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fia6_-WesMMtCyH-PXVfbwQZo_QFu8MSxZOYN13YmjwJ8LWWiggfxHN3d5Bf9OQk1j4v8koeV1EUivrUamyJKSWEU2A4fFY8Io36XIknREDyw5lWC8qiKiyy2UWL_f4Ya7loxr_ZPeYgjaAkvADJn75LwlmIrYB55dlLTgMjR9u8uMxqVdVy9Cwspy_b_XkNxCE8NVW12UZ8nIxgALQi7tku8NJ_KM0OdXbGGJAge3PufX6HOyM92X7MownhEJmB9-ycdkf5H27j_tHHbNxwcfAc0hsfZ1o0qK1L7r0gR-Tqzxsk1mWP1_UmNX9x2x_RKy8mJra0S2nQXxxQG6tqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBI1BQ0j-f7nyJHIQ-xa4DA2qChcDC7tBI0Js_xYpH3ofE-9H4asSOjh6VH5S6BPRTfZKFPtp5AkwofWGyGoKsNeePAYExmDLkhnUofCYYA3VLQcxj_Iia-1dun6tt7639NikoE3Ka30eAWuCvYDoc3my3L3nvykMDCF3XSydur6w84P306b4ftEujGzBN31HwLH0z6nQ5zl7Qn_phgIEc_1hEnt37Ume15d9uz82IYm62VT_duj3WTa00KKXr_oJKYsAfjWsVECmm4QD_7wnTVz-wCPhJGiQecmTLshPFYBe8y_zf2D4P3CYiqWiXwGsQY638Yd0MzT2lBrGtvxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-X-F6W6QiWY0DuRBiTL1z7ipfVwhErtc7uMQgBSltFEZ2AUFHHrn2CuhVY2Wo39IkXKxduKuhEDVUO5sa9wajyl3c3FXrt3M6zavvSrO3zFDDU5LlyUxbTNLjU4_fr7YrMskWm3xKQp5V-49MNJZxM97bbIeI_UKkChcjk2RelSJKusbeJSjMHmineJPVq-t5lLOJhGvDgtCIOiJ0dPCTjTcz_tdHxTMvKkBvq_clzMrWM3otMTIVyuYlUQ9qF3NmgodemBFURmdUJEK8OIQhoIdoqzmveNqwYKEUt4vfM8g7tl9j-v2UiLjDPnu7uDE3GF9QrzBqjYHfi2HR2T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyjNZKxa8gmzvYqQvdLyjYh9g-y_VauKgVXGZRz78IOZ0jnZ5cT-LlOjmSHt4vttX8SldAFFT0hKVDclnjurr7cTW1YeD-M5RASZtOtep6-fSmChMBfiYRffsGTUAD4m_8wlJiJoYDfcXP_yHzHyrEb82o-FSgMnCA-bKHL4LgK1YxR84U8oQNn655L70Cd1j2zz5f1i_koU42a6jSULOXdfuhvDwn0sDsHG04SLALhOg_xSAlGp9XxLnBjbGfWCrDEUtF2d62I4b-WEEnbhVNmWDzehEZedUpbq2lcb_FE0Ogt7fBgC7c91SaIGt7E8PYDzC_LAIVfUV5Kz5Su2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYRYc5NcTzLkGKkCZUI4zaSh86_EmQULtarm2eOIxEEQE8w0eQjN5fWzMM8m4msNR5l_9OShUanVjDHb_GJQFcyMXkWg3H0fpxcqv5w2lSK0f4kY8cM6J0Tv0XpZjS0z7h6xedYMIH3E9jHsVQZloM7eBG937QAZPa7GlTsbMZdUvXVTlwdZ_DUc1eUhmyM52MJ9aYisChlKSJ3QkWuIa4LUIn-p3EWoiugiXTBaB4PDHv6mAnBszBecP7pKRTQQPH5l3p9hxOOwQAg5SwHGXp4ArDXF_SgaLcS46XtA8ooCz6GufiSxL7APjyg2WLUTJIRxrt7wTxe5L8YneQyLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR7WkNFNmw_KzXtu5FQq3WyO5tBQ-vLDKWEcZVQPpubvLbxjivQZw41RmIj1hyd4kb0UN-1T7tp46VS2yDZXvByqOmIUel6aFDH_Pac1kN7EtcXRGFq5ewm17jg88ZL8omwN4VVzd3at2PFsQytG86HRHR9kfbpYjC7b-RXytc6QX8PpnkZ67OJES1k1ylEZxg0R0CEyFyIvyyU9Fidtmq-IJaxKGPNKXQ5RLXDbrgYAPvUHThQ4WiK4RC5USulkKJLCxbhVumbo1kZboq968wg485VkX_qZ5Gl5IA20GS8xjHVxHd27dEVfj0Scb3rO2vjfZdshsmrvey-Wn_DXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNQwVgQF3nbSRSSA1NQdRXuIH10Nvcetg6t5XBuMOIDw0-RY8PZuOJFrwpFgGxRpQiDIAIJvVERRYZ3XDFBBPFBASO5db90ekNpxnvznauDzgI1yU6dXRsXN6BvG_RKCF7kehc28ZnyHcAc1N0BvcwwvYmNSh8Xv8bgkOo4lG5IkkjmhBjVKno44ZjoEjxunsc_N86hQxGEJxR9kALE5APbx0kKmRagEJZ-mPMljxQeRynWnnYUZhapQIypPHP3XhCjbPV1p-m9cS8idUnfHfDKlwNimUJR2J-fe2aStspJ9202PvWhpdmBVjjQuznZpJCC1-XJDJ-0a8J2G8GEbWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین سالگرد شهادت سرلشکر سلامی در حرم حضرت عبدالعظیم حسنی(ع)
عکس: میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441386" target="_blank">📅 12:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پرداخت عوارض در آزادراه تهران-پردیس نقدی شد
🔹
از امروز دریافت عوارض در ایستگاه خروجی فاز ۸ به باند غربی آزادراه (عوارضی دوکوهه) تنها به‌صورت نقدی انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/441385" target="_blank">📅 12:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0GcYxVD3XrJRDgi0a2WUDYn3Pg9L8unXVD9t5_APGJrVUOX5J81mEp6q7Cc8PvLeTDN2fPUFq4k9iMBwnDvBcs697BPJB8kqItuum4cJsUT7be5rJQkJadR2ryWebRyXtGoulq2jOR9sNA4mHcGFUlnvIX7rQk61k0FNAdup16QK6WErU3NvvSq_3BIw62lMQWf2-UHTvSWkNPcZHK2E1oOhNZpMU0ZdNYncaL8hfun9xeb9uAHm9s0ghx0J5x7lLkbWojJ0HvLLUp3hJa2GaYUWZUcBPM8aOojgjYfg68ifc4jiUhrx7cm-tC3K1G0Na0duGwnvjbiSZDXOf8igQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
سامانه جامع متمرکز ارزی بانک صادرات ایران رونمایی شد/ تغییرات بنیادین در بانکداری بین‌الملل بر مبنای زیرساخت‌های هوشمند/ تجلیل وزارت امور اقتصادی و دارایی از نگاه تحول‌گرایانه بانک صادرات ایران/ قربان اسکندری از آغاز پروژه‌های نوین و راهبردی کلان خبر داد
🔹
‌
بانک صادرات ایران در راستای تحقق حداکثری بانکداری هوشمند و توسعه اقتصاد صادرات‌محور از «سامانه جامع متمرکز ارزی» رونمایی کرد. در آیین افتتاح که با حضور مدیران عالی‌رتبه وزارت امور اقتصادی و دارایی و بانک مرکزی برگزار شد، قربان اسکندری سرپرست بانک صادرات ایران، راه‌اندازی سامانه مذکور را سرآغاز ارتقای زیرساخت‌های نوین بانکی دانست و بر تقویت بنیان‌های اقتصاد دیجیتال در دوران پساجنگ تاکید کرد.
😀
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441384" target="_blank">📅 12:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0dZoAUEvE87GYGMesVfvpiyXY4sbv8Q0g-_Wro6WWIY-6HxOOygb-kbeNgqT_WZ5KJRrM-j-Sb5rbOlwTFam9zfI4W3g8Z7MEyDDQcCpUSSX37n-DOoMfPhw0ju-jEYdJd99LDYvwO0RF4wDU-cj-rzPAphSJGRVo_Svtb_we-Ufx0IKPlfbchRn6CypYE1GSUqEfKd9qoerMuIHTTiBMJRrqBMn0rDiECbdr0YfWXU-APu3hh7N8uTBA_JsYZCz1rynWMMmJu9dhVYPkBeed7jitO3dRvW2b8Qpxqg5PDpb61OjA6k3ipc3zQBe_wrCHoJTna04YLFIw0GwhR4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
جام جهانی ۲۰۲۶ از همین حالا در «همراه من» شروع شده!
برو توی اپلیکیشن *«همراه من»*، بازی‌ها رو پیش‌بینی کن و جوایز هیجان انگیز ببر
🤩
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک  PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
3 کمک هزینه سفر به عتبات عالیات در هر بازی تیم ملی
پیش‌بینی از تو، جوایز میلیاردی از همراه اول!
🔗
https://www.mci.ir/-9VEQ3HH</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441383" target="_blank">📅 12:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441382" target="_blank">📅 12:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b1aee46d.mp4?token=NjnuhDIPglSMc013wxuOMrkKLFZ_r2oHFlZffZO9Sni1MIs2qFU68YFg-W4NtYDjUl_oBI3piCZnipCTiGzLvU8Z8uNQrww9h7xhG3R6-3LxEn7J8xCW-zE9hllSDRMaTf6NDoLbxSH64puN0M2D1_56tYcUK5FBOhbE9vxaJmv7vqkT-CvJRipLpy-MiXfKwhuX69aqVBwws19Nf3RnRgtm4jafwABerhwTTnDjUY6NyrWtdSya4tQIMCMgeY4ilWO5T0aPKRebUxWn2O3wF6f-tUzA2BPbm1Rg3UJJGz_nlW5DUxdPbH2s0_QIqIzrzRhkORRZK_Ae6LVQQ2vTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b1aee46d.mp4?token=NjnuhDIPglSMc013wxuOMrkKLFZ_r2oHFlZffZO9Sni1MIs2qFU68YFg-W4NtYDjUl_oBI3piCZnipCTiGzLvU8Z8uNQrww9h7xhG3R6-3LxEn7J8xCW-zE9hllSDRMaTf6NDoLbxSH64puN0M2D1_56tYcUK5FBOhbE9vxaJmv7vqkT-CvJRipLpy-MiXfKwhuX69aqVBwws19Nf3RnRgtm4jafwABerhwTTnDjUY6NyrWtdSya4tQIMCMgeY4ilWO5T0aPKRebUxWn2O3wF6f-tUzA2BPbm1Rg3UJJGz_nlW5DUxdPbH2s0_QIqIzrzRhkORRZK_Ae6LVQQ2vTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: شهید سلامی الگوی یک فرمانده تراز انقلاب اسلامی بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441380" target="_blank">📅 12:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
دختر شهید سلامی: شهید سلامی معتقد بود اراده از موشک مهم‌تر است و ملتی که به وعده‌ خداوند ایمان دارد بزرگترین قدرت تاریخ است  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441379" target="_blank">📅 12:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwJuSm1-X5nrqZ62cQ88ust1_mLTfwr5SwL6Xp4XBKulv_omDoUziaLWcyM7B4Q3ySVHXRF-sOpqYBioRk_Gc5CHWAy-7mqwk4FwwIyNKDlwXC-hsfC_9yVllc5UnQL-PFGWeVYwQsuLrE-3n5TX7w7DaX7b8rr4ZywU4bSQ9EAOF4sFhXdbSEADdpwJIUbVPN2cXPkTtahVFToJZWchJNauvirJg958SodOmqiZ09RKQKKmFH6vj6jH3iZHPTWVUr8MpI3moEIN25TXZxTftweP1516Vq5FkpJ8ViZLkDSYTPyh181zGpcTW-oKM4wS3dUSFeKXq7ex8--pVoREbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود موشک‌های پاتریوت؛ آمریکا متحدان خود را دست خالی گذاشت
🔹
خبرگزاری اسپوتنیک روسیه گزارش داد، در حالی که جنگ با ایران فشار بی‌سابقه‌ای بر ذخایر تسلیحاتی آمریکا وارد کرده است، متحدان واشنگتن برای دریافت موشک‌های رهگیر سامانه پدافندی پاتریوت با ابهام و تأخیر روبه‌رو شده‌اند.
🔹
«برایان دان»، از مدیران شرکت لاکهید مارتین، در نمایشگاه هوایی برلین اعلام کرد این شرکت نمی‌تواند هیچ تضمینی درباره زمان تحویل موشک‌های PAC-3 یا پاتریوت ارائه دهد، زیرا تصمیم‌گیری درباره مقصد نهایی این موشک‌ها پس از خروج از خط تولید در اختیار دولت آمریکاست.
🔹
بر اساس این گزارش، کشورهایی مانند عربستان سعودی، ژاپن، لهستان، آلمان و امارات که از سامانه پاتریوت استفاده می‌کنند، ممکن است برای دریافت محموله‌های جدید در صف انتظار قرار گیرند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441378" target="_blank">📅 11:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c908e597ac.mp4?token=CdWYDN-2qanH0eO97eO2Hir3I36IQGxup84ZSH-pSj51h1DYelNFTKVT71-J20zY8LM_46_MSTmZ2UeoUTLxrvDC54lm7-lLEeye4NsQvAK8sS-pSCi0pwjkpEz-Z2vYBsKQZUPjbAKxHJBn3Llpp5sC8i1vpx_unjiryA4IdnJdjiz3yST6-OkcFiXwj1uKCjEnzrv665b2otdyJzLm0VbW8zi9OlAnlDX85bh017tLQ7lNz1WGyZ9Kp_FfAMuyTH6effQNO59dSdCmjQhHT_XWH6f-vLFioKvtGDYPrV7V5n5CYiMYNONtOHgbAujzseRFopf1C_ZC1DPnBkA7kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c908e597ac.mp4?token=CdWYDN-2qanH0eO97eO2Hir3I36IQGxup84ZSH-pSj51h1DYelNFTKVT71-J20zY8LM_46_MSTmZ2UeoUTLxrvDC54lm7-lLEeye4NsQvAK8sS-pSCi0pwjkpEz-Z2vYBsKQZUPjbAKxHJBn3Llpp5sC8i1vpx_unjiryA4IdnJdjiz3yST6-OkcFiXwj1uKCjEnzrv665b2otdyJzLm0VbW8zi9OlAnlDX85bh017tLQ7lNz1WGyZ9Kp_FfAMuyTH6effQNO59dSdCmjQhHT_XWH6f-vLFioKvtGDYPrV7V5n5CYiMYNONtOHgbAujzseRFopf1C_ZC1DPnBkA7kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری مشهور آمریکایی: ایران به ما آموخت که قدرت آمریکا محدود است
🔹
کارلسون: به رغم داشتن آن ارتش، با وجود ناوهای هواپیمابری که از ابتدا تا انتها ۱۲۰ میلیارد دلار برای به آب انداختن آنها هزینه شده است، ارتش ایالات متحده نتوانسته است طی ماه‌های اخیر آن تنگه را برای حمل و نقل به روی سایر نقاط جهان باز کند. هیچ تضمینی هم وجود ندارد که ما بتوانیم این کار را انجام دهیم.
🔹
بنابراین ما قبل از هر چیز محدودیت‌های قدرت نظامی آمریکا را آموخته‌ایم. کارهایی وجود دارد که ما نمی‌توانیم انجام دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441377" target="_blank">📅 11:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
دختر شهید سلامی: شهید سلامی معتقد بود اراده از موشک مهم‌تر است و ملتی که به وعده‌ خداوند ایمان دارد بزرگترین قدرت تاریخ است
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441376" target="_blank">📅 11:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwfYvWpqVmzumabmYIEwiFbOlEUMguGQZdqLdvInyLJ5qNb0DoEvgPRVjo4O2Z0-s-eW0CRUEq4_km-HNaM1M-UQDGqjLOqfV4vRn69xId9FWX2WrZI--fAuyGR_wD_gio-yHg0pgFr-Wal-EnMP_SF9y2YRol_GZB7Xt7EQ5Og_TX3sztn0mfBISdnBoJdd3J1XsLY0ZJm6g9usED1_dOxv_mcIOmkZsuNFxGdtsVCzidQrinFU-aplRr9pN_rS033pfzOkn75Vww6t-DFPQcy2dxZ7P6RcNquFEp-tSjIoBI2NJj3UgPA_GbGAeq3xQgs9VXBs6NuOqkCb_7dHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار فدوی: «وعده صادق» تجلی نبوغ مدیریتی شهید سلامی بود
🔹
مشاور فرمانده کل سپاه: شهید سلامی مظهر یک فرمانده تمام‌عیار و برخاسته از دل میدان بود که با فرماندهی مقتدرانه عملیات‌های تاریخی «وعده صادق»، توازن قدرت را به نفع انقلاب اسلامی تثبیت کرد.
🔹
نبوغ بی‌نظیر این فرمانده، به‌ویژه در مواجهه با تغییر ماهیت نبرد تجلی یافت؛ در برهه‌ای که جنگ‌های نیابتی دشمن جای خود را به رویارویی مستقیم داد.
🔹
شهید سلامی توانست به بهترین وجه ممکن از پس این روندهای جدید و متفاوت برآید و عملیات‌های تاریخی و ساختارشکنانه «وعده صادق» با فرماندهی مقتدرانه او به انجام رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441375" target="_blank">📅 11:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزارت امور خارجه: مسئولیت آتش‌افروزی برعهده آمریکاست
🔹
بیانیه وزارت امور خارجه در خصوص نقض فاحش آتش‌بس توسط آمریکا: حملات غیرقانونی و جنایتکارانه آمریکا در ساعت‌های اخیر، نه تنها نقض فاحش منشور سازمان ملل متحد و قواعد بنیادین حقوق بین‌الملل در احترام به حاکمیت ملی و تمامیت سرزمینی دولت‌ها است بلکه آتش‌بس مورخ ۱۹ فروردین ۱۴۰۵ را عملا بی‌معنا کرده است.
🔹
از سوی دیگر تداوم استفاده ارتش تروریستی آمریکا از قلمرو و امکانات برخی کشورهای منطقه برای تدارک و اجرای عملیات تجاوزکارانه علیه ایران، آن کشورها را در کنار طرف‌های متجاوز قرار داده است.
🔹
جمهوری اسلامی ایران ضمن یادآوری موکد تعهد قانونی و اخلاقی همه کشورهای منطقه برای جلوگیری از استفاده ارتش تروریستی آمریکا از قلمرو، امکانات و منابع آنها جهت ارتکاب جنایت تجاوز علیه ایران، بر عزم خود برای خنثی سازی مبدأ و منبع حملات تجاوزکارانه علیه ایران، در راستای اعمال حق ذاتی دفاع مشروع علیه تجاوز نظامی آمریکا و همدستانش، تأکید می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441374" target="_blank">📅 11:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtTZ_QLMoXgHuh2Y69TJMFKVXDl9Vc2DzCBbjlUoI3VQrwfFEZdBPTKzr41kfDxDev0Hyj2GVuSesNJeivit6ovgNQM5ebssRvXNnpoCFYq1xTIiInRtLWU5Ki_V5JenyTx8NjlTyYuL_umV2rERQ4_AkeZpYg9QyvE5VyZPQlEcUQYvdaLIREZYL-rpeiQkf3AjeE3DGdbZPPtm0-adazmldf3VCdtgUgPFmnqaGY450bqZ7c_dOlgzR_cXua_Xm-OUd__H8nOwzkUSZcp8EHS7aipdIW98fmso8H8OxeqN3mG8MxzX-du3JVbxzK_5TBqKGwYBUpbY-9tYPmFlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور باشکوه مردم در نخستین سالگرد شهادت سرلشکر حسین سلامی  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441373" target="_blank">📅 11:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
نمرهٔ قبولی در کارنامه دانش‌آموزان شهید میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441372" target="_blank">📅 11:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2959aec073.mp4?token=LXqttSk3d_7hxYmkvn_G0OmeIU9FaS6PKGIWVyfYu6USJQuStogTM_tfQgCM6C_Af_CDpkiV1I08qn2Dr0qIGNjFeGSXBs7rugXm--ORizCdANYx0GRAzfM1_7jvM5bZ4DzTkMd0S8gQYSb1XoJUFOsPDSHNhsXAfjc33Xj-o65vFgKBSBpeJ-a_MY5aH3Th5HQQ54hruPUE9KI6Qb81qpiq7gLYB4jAugOwo-uVIQGkk5-PrpPZ3uet1epXw0I_jyFgv4RUynSTN11BoFOQ_0Joju22KtcK-GT4YUemtx9FzAb8RGeOGhFJF35mObmCqAqyKDz4M152MNy1h0rIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2959aec073.mp4?token=LXqttSk3d_7hxYmkvn_G0OmeIU9FaS6PKGIWVyfYu6USJQuStogTM_tfQgCM6C_Af_CDpkiV1I08qn2Dr0qIGNjFeGSXBs7rugXm--ORizCdANYx0GRAzfM1_7jvM5bZ4DzTkMd0S8gQYSb1XoJUFOsPDSHNhsXAfjc33Xj-o65vFgKBSBpeJ-a_MY5aH3Th5HQQ54hruPUE9KI6Qb81qpiq7gLYB4jAugOwo-uVIQGkk5-PrpPZ3uet1epXw0I_jyFgv4RUynSTN11BoFOQ_0Joju22KtcK-GT4YUemtx9FzAb8RGeOGhFJF35mObmCqAqyKDz4M152MNy1h0rIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سالگرد فرماندهٔ شهید سپاه پاسداران سرلشکر حسین سلامی  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441371" target="_blank">📅 11:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تکمیلی/ ناتوانی پدافند آمریکایی در اردن در رهگیری موشک‌های ایرانی
🔹
رسانه عراقی «صابرین نیوز» نوشت که انفجارهای مهیبی در پایگاه‌های «الازرق» و «موفق السلطی» به عنوان محل استقرار نظامیان آمریکا در اردن رخ داده است.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441370" target="_blank">📅 11:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO4LquoCdObm0uAm9n889znLexS1LJfurvVmu9K0_58W3Rlf5j3krSaW18zdF0IDPESVVVsQlAv-HWjsEZUEgSxIjWXv9rf4Xqd_rojzmTyJ5BBRfqPXhANJa-5kSJHZAkiC8Xx_xxwvFIOVEg7Hgtu9YTQt-Tik-u-wL3t7yTr5eF5t0YVorffhan22RmUokg_Yz71P4qfAZTG7a-dMYp3qcvEVQNdB8P1nLdnY96Idf38clPhyQ-5yUzONVvXUw3b4a6Py2IuHPEWpoPCmdf3N3MREIDzpPvFuIlTkED-_JNe36xyTMzPreZJluW_zbo6VWQgadkaULIiBHr-Bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: انتقام سخت و نهایی در زمان مقتضی محقق خواهد شد
🔹
پاسخ‌های تاکتیکی به اقدامات دشمن تنها بخشی از واکنش جمهوری اسلامی است، اما انتقام سخت و نهایی بر اساس صبر انقلابی در زمان مقتضی محقق خواهد شد.
🔹
فداکاری فرماندهان ارشد و شهدا جمهوری اسلامی ایران را به جایگاه یک ابرقدرت در جهان رسانده و این اقتدار کم‌نظیر مسیر پیشرفت و پیروزی کشور را بیش‌ازپیش هموار کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441369" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie7vvjjYdwA31I309-6izgmVWoQKOdHd4epkCjos5XBMHFrBfzikXLIbqkCIIaUAhEiaIaiXJB50Ir4oV-3Hntg2G0fkOP7whLV35Pfb54ZJBdJ0AilZq8510AaAPljqXUSNKymS-I5PK6GQx7JqgKjgf1kLR8OEbIxBAeBfGF50OgVCu5j3Qe8ru2cgudReAsCFBg6GOgsZqh2vmSzmIW706BX_uPSXnvJ_7astYL7cvDbfjTnFF43m1TSSNY4qu5qUxXd4XJJ8lIdUlGhxv27WntkF0KC61mype87BAdgOQT9zKS9NzY15V6O-pnGHTAyHHjiRj_pGbbV9RbRnpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی در یک نفتکش در نزدیکی عمان
🔹
مرکز عملیات تجارت دریایی بریتانیا: حادثه‌ای در فاصله ۲۱ مایلی دریایی شمال‌شرقی عمان رخ داده و یک نفتکش دچار آتش‌سوزی در اتاق موتور شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441368" target="_blank">📅 10:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۳ مصدوم در حوادث مرتبط با حملات آمریکا در تهران
🔹
رئیس اورژانس استان: در حوادث مرتبط با حملات وحشیانۀ امریکا در استان تهران ۳ نفر دچار مصدومیت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441367" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیا: نیروهای مسلح هرگونه تهدید علیه کشور را قاطعانه پاسخ خواهند داد
🔹
پیام سرلشکر عبداللهی به مناسبت نخستین سالگرد جنگ تحمیلی دوم: در آستانه نخستین ۲۳ خرداد ماه، سالگرد آغاز دفاع مقدس ملت ایران در برابر جنگ تحمیلی ۱۲ روزه رژیم صهیونیستی و آمریکا، یاد و خاطره شهدای گرانقدر اقتدار ایران اسلامی، بویژه فرماندهان عالی نیروهای مسلح و مدافعان وطن که نام "سپهبدان شهید محمد باقری، غلامعلی رشید، علی شادمانی و حسین سلامی و سرلشکر امیرعلی حاجی‌زاده در آن می‌درخشد، را گرامی می‌داریم. آنان با حماسه ایثار و فداکاری خود، برگ دیگری بر تاریخ عزت، مقاومت و تاریخ‌سازی ایران مقتدر افزودند.
🔹
این نبرد نشان داد که ملت ایران در برابر تهدید و تجاوز، با وحدت، ایستادگی و تبعیت از رهبری معظم انقلاب و فرمانده کل قوا و توانمندی‌های نیروهای مسلح، ازحاکمیت، استقلال، امنیت و منافع ملی کشور دفاع می‌کند. و دشمنان با محاسبات غلط و متوهمانه خود، در دستیابی به اهداف شوم و شیطانی‌شان ناکام ماندند و با شکستی راهبردی و خفت‌وار مواجه شدند.
🔹
با گرامیداشت این دفاع مقدس و تاریخی، اینک در شرایط دفاع مقدس برابر جنگ تحمیلی امریکایی سوم؛ حضور گسترده و آگاهانه مردم در حمایت از آرمان‌های انقلاب اسلامی، نیروهای مسلح، بیعت با مقام عظمای ولایت و رهبری حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای(مدظله‌العالی) و خونخواهی امام شهید جلوه‌ای ماندگار از وحدت و انسجام ملی و پشتیبانی از مسیر مقاومت را شاهد هستیم که با گذشت بیش از ۱۰۰ شب حضور میدانی پرشور، با شکوه و قابل تحسین و ستایش، نقش مهم خود در تقویت قدرت بازدارندگی کشور را آشکار و در نگاه جهانیان تحکیم بخشیده است.
🔹
با سپاس به درگاه خدای بزرگ و تجلیل از خانواده‌های مکرم شهدا، جانبازان و ایثارگران جنگ تحمیلی ۱۲ روزه، تأکید می‌شود:
🔹
نیروهای مسلح جمهوری اسلامی ایران با آمادگی کامل، هوشیاری و اشراف اطلاعاتی، هرگونه تهدید علیه امنیت، استقلال و تمامیت سرزمینی کشور را با عملیات‌های تاثیر محور، دردناک و پشیمانکننده، قاطعانه پاسخ خواهند داد.
🔹
بی تردید، راه شهیدان عزت و اقتدار ایران اسلامی بویژه قائد شهید امت امام سیدعلی خامنه‌ای(قدس سره) ادامه خواهد یافت و پرچم استقلال، مقاومت و سربلندی این سرزمین، برافراشته‌تر از همیشه باقی خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441366" target="_blank">📅 10:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">زلزلهٔ ۴ و ۴.۲ ریشتری در نورآباد استان فارس
🔹
دو زمین‌لرزه به بزرگی ۴ و ۴۰۲ ریشتر دقایقی قبل حوالی نورآباد در استان فارس را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441365" target="_blank">📅 10:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa1658111.mp4?token=ZTxh8b6XIfShLCipEJUhCcp-rHMZMVfJCgQkYVMpZofeGzWc4pYmu8G2iinPg7uenwVEu548ZH8ydfcH-inqo4LWk3Bx63t4IG_K30s4t8TOZfWLh3aeDug6T7GOenLLkoUSAU4ar-fvWjS_7SKW3ONbhoZ3lzL9YlAlkR60UpNlTadyuvZWs5uCHtryCYbf6zHnWvTZL4T2kj6hFGk_N98I3CjrLDjLjN3QZjuN-YYFkMb4hkjKkxPRfJauq7retRLlwB5QvG45DYZFiJwnOd3iiem1e1pQjgYbP5Kvoq_KExPUv_p7grUDPPj_cM9h9C80-b7pHj7cWE287rT_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa1658111.mp4?token=ZTxh8b6XIfShLCipEJUhCcp-rHMZMVfJCgQkYVMpZofeGzWc4pYmu8G2iinPg7uenwVEu548ZH8ydfcH-inqo4LWk3Bx63t4IG_K30s4t8TOZfWLh3aeDug6T7GOenLLkoUSAU4ar-fvWjS_7SKW3ONbhoZ3lzL9YlAlkR60UpNlTadyuvZWs5uCHtryCYbf6zHnWvTZL4T2kj6hFGk_N98I3CjrLDjLjN3QZjuN-YYFkMb4hkjKkxPRfJauq7retRLlwB5QvG45DYZFiJwnOd3iiem1e1pQjgYbP5Kvoq_KExPUv_p7grUDPPj_cM9h9C80-b7pHj7cWE287rT_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: تقویت بودجۀ دفاعی یک ضرورت راهبردی است
🔹
ایران در حوزۀ نظامی یکی از کمترین بودجه‌های نظامی منطقه را در اختیار دارد.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/441364" target="_blank">📅 10:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sirXGeR9H3NuZonXI-df9P9xCDXZV76oJipAVB_uJSehHL7Jzqq008AOIDX_8pqNE7f1P92lfeWf-IZPjn27RJcFuNi8rGieU0Mt8dmNbFo5481o_VFGHeG1KagmaKl9SmmD8QqCuW20ttU5qKiJY2Dl6EzbXqt82fVjGz1Dtmr2yrsaxCWfSbHN_sjwZNTxR5WmFaiS8ymo-yHx5ZB8JYuXjp7LKagRJFUpRGtsqoHFdKYwzNhraKKCqrUYnz0RpS7glgvRLrwjesP61PvnXAZFl-zUGxvFOj_5wc56qbSqb6cW3z7Lcd80WtOKxBvVxjE57AW4I8H4ffLzfOtbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMfJ3_L_L-_x409KYjrSX8MDH8LhbE1sFTzuVl6dMGjsOB2rGHYzrukPCAxPZirGdfH5fbpSi7dJed8d-ctYsiAlID8VMjTgPEs4ATxjo8x1xPDlS5fzhFMxaxp97wj6uOUavCONuuC75XBULlF4c4b1l3TdgXukUqqtBBsgvTU192ntLQnWenNtStBxgxYyLZryOH8vwxnw5xsEzMT_JDKVI3Y1cDNwuOqc_Lfpwax1ygiJCNXY9k0KVVgbin6FggLtvbgR6ehkdOrrvIOtd__qpxykRTp_8gFAm2liyZn6oTHVimh9r1JFoY18icNorNd_IGzuxYCij7s5exuYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4LoqdFyFlKEu2PfIJcYs78Tzqw12djGmmD5VD0HeOOnAX_xCfh8eBloUxROVAY1I0df4iF4J5QWpOgmAiA1WW-Eqsa8G9mAGMeyxrMW0DRzMOwWgUyyvQK9XE4X3C_8YqhzPSicy0rLP7rMjub7bdoY5GEtqb41I_G7Jnyv3QwRw35rU6Ww00qxif1ii-pV0xuE4AABF9Ck-gyZXM5l7Y39H1zkCLO48Bl-DFu4WgCco_e--q1CDDP_udW0AlI7UI6cyKzX3PEjA9NvB4k942gVTZVoqOsPy5Q1JaakY_Mgln2g7Hvk5F1K129jYK9dds2PCMcCwHN0Rs1HMaItYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6nKj16tdEt0lzhHuNsuucZar-AcQZUoNJnmjXc7rAlK7BLKY3EhtZ0DESfWtBqoJUrDSuyhV8E6rdv2h_p7k_uXtMu9KbtSjnP4psNEajQPSOjBDYqOHCir_ZIm7aonbZHM-qRY6bnThT_V_J-pXI-xhAOzSvMshqEl6I9NnSRRBVPyxBHTZc-dqVRzL2I2ek445ypwIp6gklELhlx308LrrNRQX9auUaxSyBG8_YisdnA3CnVGzSt5vlsBxmscQ9stmMENj4C7V3BjA1Ihimi82xubUfNL5Ba8D1f0cFl6nmawlX8qLMcoLWcXNlzDL5OHzQGdjQlXB1pSxgigGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ohy73996aTkEXzwQ1R2t8VltEIj4MFrff-r5VsI4wm4wikS7BM7AD-Qo4O1X4tQ75ZFrYZ9EziHEZiLNBXrLrfgE-2mgrG7a14haKiflmsWB7Qyku69BjlVm2Jn1e_-qyi11SM-7wPcNRUjMIm6Ou--mjue_D5Ad0AifRl1K4ucjbOyDIyak47r4I0H7Gy0uejRLsXOyh0O9ZlJd9O6Vm-5Kr83oWesqNRdZgCecyHDH6n0yApn8_rgcUNmhzYBdw5rt4eGEoJQ7xZ7ozaFnH4dTvDv4ixnFOyysJcq6PihkeaoHnatMp1zXsVfJ0fN07VJdE-RchnskFqu8HkJ5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuCYixDMsd-Jrad97AEosmJHlUiiJpZYHS4L6agBJP-WfIsQKdNINWNxdhzCBrFNXO-3bfOFJHtlO77FBFEDuN9ZZ3PjhevnQm2hvSDWE1egtZK3TDio1S51qFJMPfddZV42h29Gf-bTTljeZvxR0aXHeT5QZPIYhDmA5ZuHzjTDIaPfyZ1Sd1ev9HWacipodnZpD2DvYYhl8EpidIIchOLiQaGDLOlZGqQRN3wqI2MBxhNyoZvHuBzLro5jAiXx_Wtwt9Zd1xGRavkbE3vY0aIN_06nziQyDmfb350fvEx3xDW0eO_ZJaqwdWojm2J0uqmOUoSsbA-uNb1attIxlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هنرمندان کرمانی در صد و دومین شب حضور
عکس:
مهدی امین زاده
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441358" target="_blank">📅 10:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irLsbFBA1qcx0cHkAWimHmmOBbjMu9bxh17iBMg3VTlre_cGd0m6oNUsS2DyuBDc31KIPtzqvXkrmVEiURC_mIkE1TpktP-KQVmoTK721cxulr04uMW8gATggaJeVMZMN3Zqn-rs34ly3bbntTus6RkYHGOknUNsOSlYGhOYS-XR0i28WoiJYwYKY8Dm5Pmphwd5VAglTY-P_bNxYaJyMYP1rcQobN6DCtg33YXtDqU15XSfcfooCoa7B0q7JD2g7d7w1vrpcKWa8jipJ6DyMjjZg6bgmWnh9beZnbSUOhvYiMHzsLDBehwEWoGqjubQe6mmCeRpCPKgJXAJPMrBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تنها راه مقابله پایدار با فساد، حکمرانی داده‌محور است
🔹
تکمیل پایگاه‌های اطلاعاتی و اتصال داده‌های دستگاه‌های مختلف پیش‌شرط تحقق عدالت مالیاتی، توزیع هدفمند یارانه‌ها و مقابله با فساد است.
🔹
هدف اصلی دولت حل مشکلات مردم، ارتقای عدالت و جلوگیری از تضییع حقوق عمومی است. اگر این اهداف به صورت شفاف و صادقانه برای جامعه تبیین شود، مردم نیز همراهی و همکاری لازم را خواهند داشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441357" target="_blank">📅 10:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11307c379.mp4?token=iTsa75DsBrDpAvfgjXoYzpJEQWkR_bJMgHfK5NBWtEhDn38f_9i6yMGrsJ_t0aLULDpRRUpHOEvTUQ5dAeHU9pLzso8xQ2BV0n_Kz1apiDnVrxU9AkuTqc1L2m6YdgP80Qnx9ItqtjGCWA9Kiq8GBTyM97Yu0-q6bMzVeBOq7KPj3LxVAIkuVeXs5UZFSgymWXhtwGWxupLRV1SzXfVnTCvHtegFBA4bfE1BdyqrZWkpwTBrCnQb179RCu-XwtFwfkGd3R_zuZc6phUETUhcINbpe1-iVVnrikPrx8GA8OUXg-MwitwJphklNCG9LBEMo6ZbetLs5yizHSpKt_iA3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11307c379.mp4?token=iTsa75DsBrDpAvfgjXoYzpJEQWkR_bJMgHfK5NBWtEhDn38f_9i6yMGrsJ_t0aLULDpRRUpHOEvTUQ5dAeHU9pLzso8xQ2BV0n_Kz1apiDnVrxU9AkuTqc1L2m6YdgP80Qnx9ItqtjGCWA9Kiq8GBTyM97Yu0-q6bMzVeBOq7KPj3LxVAIkuVeXs5UZFSgymWXhtwGWxupLRV1SzXfVnTCvHtegFBA4bfE1BdyqrZWkpwTBrCnQb179RCu-XwtFwfkGd3R_zuZc6phUETUhcINbpe1-iVVnrikPrx8GA8OUXg-MwitwJphklNCG9LBEMo6ZbetLs5yizHSpKt_iA3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سالگرد فرماندهٔ شهید سپاه پاسداران سرلشکر حسین سلامی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441350" target="_blank">📅 09:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxw9xLd_VSC-ul5w0JYhyp3Z74X0xvT-yC4gcBtucIPptX7yVlxEx_N9j6VmOl-1OZ7jGniT8W9CpO8oJ6R7J_PdTetTdOuBghxo0BFloDKwuXQd9gqxy5oZM_eLkL3BgztIDxom3H2QjVAG8CskwSmCjWWDWajCZA_lTbRI3zR5lywkMy-c0pm0yujTahvhjrELsFljmWCKMJoJ26SiYZ2vpqlJjgtbI-ka3EmZlk_pxkD6WHSxjvAu45Vl_BG2YhQyqVozZ2ZuKFSBRhQTAzUWPdbkmladQl__xk2E7WmHE4wvSDufXcwEIClxJQBsWK3N2xFxPJGS_ES4j10Y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: شاید در ایران جنایت جنگی انجام داده‌ایم
🔹
به دنبال حمله تروریستی آمریکا به تاسیسات آب در استان هرمزگان، نیویورک تایمز با انتشار تصویر ماهواره‌ای مخزن آب سیریک از احتمال «جنایت جنگی» در ایران خبر داد.
🔹
این روزنامهٔ آمریکایی گزارش داد: «هر دو ساختمان در خارج از روستا قرار دارند و هیچ زیرساخت دیگری در مجاورت آن وجود ندارد. برخورد به ساختمان‌های دورافتاده و برخورد به مرکز سقف، نشانه‌های احتمالی یک حمله دقیق تلقی می‌شوند.»
🔹
نیویورک تایمز با یبان اینکه تحلیل تصاویر و ویدیوهای ماهواره‌ای، دقت حملات آمریکا به تأسیسات آبی ایران را نشان می‌دهد، نوشت: «هدف قرار دادن عمدی زیرساخت‌های غیرنظامی می‌تواند جنایت جنگی محسوب شود.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441349" target="_blank">📅 09:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
فعال شدن آژیرهای خطر در شمال فلسطین اشغالی
🔹
جبهه داخلی اسرائیل از فعال شدن  آژیرهای هشدار در شهرک‌های مسکاف عام و متولا در شمال اراضی اشغالی فلسطین خبر داد. رسانه‌های محلی نیز دلیل این امر را حمله پهپادی جدید حزب‌الله اعلام کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441348" target="_blank">📅 09:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اژه‌ای: بیش از پیش برای صف‌آرایی در برابر یزیدیان زمان آماده‌ایم
🔹
رئیس قوه‌قضاییه: مشکلِ سردمداران آمریکایی و در رأس آنها رئیس‌جمهور فرومایه و سِفله‌شان آن است که هنوز مفهوم غیرت و حمیّت ایرانی را درک نکرده‌اند.
🔹
همگان باید بدانند که برای یک ایرانی مسلمان، دفاع از وطن، نه صرفاً پاسداری از خاک، که حراست از شرافت، هویت و یک میراث تمدنی سترگ است.
🔹
قیام‌اللیلِ ملت ایران که از ۱۰۰ شب گذشته است، گواهی بر عزم راسخ مردم و قوای مسلح ما برای پاسخ کوبنده و خردکننده به هر تجاوز دشمن است.
🔹
آحاد ملت ایران چون کوه‌هایی استوار، ثابت‌قدم و خلل‌ناپذیر ایستاده‌اند و برای دفاع از کیان ایران اسلامی، هم‌عهد و هم‌قسم شده‌اند.
🔹
اکنون که پیش‌روی ما، ماه محرم، ماه پیروزی خون بر شمشیر است، بیش از پیش برای صف‌آرایی در برابر یزیدیان زمان آماده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441347" target="_blank">📅 09:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441346">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9406979f70.mp4?token=afxL3JdBnltyx2LAC_YCUfRb7MSe0ALgbOSktehCQxaB8_ETr0SbK7zdfS5PN0ssYcvFDVngYEFR0ui0LMRIM-7EvVL5yL9aWDGEe3mHGLlHJ6trCU9HR7838W5kY_oj6UtgYnv0rThr34r6NuGyrgpjJBe6Re5Nx9EomBV0trlTUtoboKYxsOsYa3uw7FcGpxiYkDCpzEkS5ZhFle9eChW2VMU2YOnOS0sO3rwGixlEVAJ3hOwhrXT1AQOG87cZFJj_hzdemD1gZ4PicMSThnU1S3Hw5g33t1ZeRV84-kfm2BwvKFU6ziN9DhrmcRtgWzhcVLrp1yKwiI7vHAMM8hd9qpAim9sdtOlElRXzcHzrOzxiejyLCP0NOsyqeHOtvhT0YTb34ZFhANvGqtf5XThmXoZ3ixg5CD7uI8FU-zR0yUOCpo5qqTyWk_bf2DUv9t0zvuuM9FFGh1wLpQBDQcUtMus0vmO3jtpKyAv_JMwnia65ar6Be72zghPCHsVytc5j9ayVytfiI-vENMLHzWa-ob2qRVRuKUrrZXYX_dRxfYbP2t9dQmSm1-LcDgYtAbKkBQUybPjxEqxAjOQ-Xf0dYoDdBuhD44SZNERA-Ga2vAbm3DhM9WD1g0P94Q_SyDgigwnP5eRRWviGIlIfWXa5jg99Q9PGqcQoUvAe5pU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9406979f70.mp4?token=afxL3JdBnltyx2LAC_YCUfRb7MSe0ALgbOSktehCQxaB8_ETr0SbK7zdfS5PN0ssYcvFDVngYEFR0ui0LMRIM-7EvVL5yL9aWDGEe3mHGLlHJ6trCU9HR7838W5kY_oj6UtgYnv0rThr34r6NuGyrgpjJBe6Re5Nx9EomBV0trlTUtoboKYxsOsYa3uw7FcGpxiYkDCpzEkS5ZhFle9eChW2VMU2YOnOS0sO3rwGixlEVAJ3hOwhrXT1AQOG87cZFJj_hzdemD1gZ4PicMSThnU1S3Hw5g33t1ZeRV84-kfm2BwvKFU6ziN9DhrmcRtgWzhcVLrp1yKwiI7vHAMM8hd9qpAim9sdtOlElRXzcHzrOzxiejyLCP0NOsyqeHOtvhT0YTb34ZFhANvGqtf5XThmXoZ3ixg5CD7uI8FU-zR0yUOCpo5qqTyWk_bf2DUv9t0zvuuM9FFGh1wLpQBDQcUtMus0vmO3jtpKyAv_JMwnia65ar6Be72zghPCHsVytc5j9ayVytfiI-vENMLHzWa-ob2qRVRuKUrrZXYX_dRxfYbP2t9dQmSm1-LcDgYtAbKkBQUybPjxEqxAjOQ-Xf0dYoDdBuhD44SZNERA-Ga2vAbm3DhM9WD1g0P94Q_SyDgigwnP5eRRWviGIlIfWXa5jg99Q9PGqcQoUvAe5pU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خانوادهٔ شهدا از حال‌وهوای رواق «کشور دوست»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441346" target="_blank">📅 09:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441345">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در محدودهٔ شرق اصفهان
🔹
استانداری اصفهان: انفجارهای کنترل شدهٔ مهمات عمل‌نکرده در جنگ رمضان در محدوده شرق شهر اصفهان از ساعت ۹ صبح تا ۱۵ بعدازظهر امروز انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441345" target="_blank">📅 08:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترافیک سنگین در جاده چالوس
🔹
پلیس راهور: در مسیر جنوب به شمال چالوس، حد فاصل پل زنگوله تا سیاه‌بیشه، ترافیک سنگین گزارش شده است.
🔹
در آزادراه تهران-شمال مسیر جنوب به شمال و در محدوده انتهای آزادراه و نیز در محور هراز مسیر جنوب به شمال در محدوده سه‌راهی چلاو، ترافیک سنگین جریان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/441344" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8ptp4bRzZXrhU60V-aL70DiietgeYSLfnaXOurz1jWHSX6ZAv4WvwrkxtSs9FJcj3ARzMzMlQpsTEJnCc1uC-gxmHGzDI7klds_1UIdLtS51rmx_4aTCmvrbPA715ALonGAjbMRYtoMa1WCD_Ssfv5h2TgBLuQ9toa9WoMCYc1VV2PdRNPCDciS0a7akLiISSu2nSWF2amDEu9VxsOflI1JxzBRF_m6JHJ4EAOesdUCaink8WoMFPrdM-eZjlrD6M89jVgUyFq3ZAA63ZH1ia4EjoY8YisAIsstML9H2Xzhs82QWBlCLPW6mIBBLEpHnNQRbfS_sCLoD0I97HPJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۹۰۰ کیلو تریاک در جنوب سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: از محل نگهداری دو محمولهٔ موادمخدر در یکی از روستاهای ایرانشهر و شهرستان بمپور مقدار ۹۰۰ کیلوگرم تریاک، ۲ سلاح کلاش و ۱ کلت کمری کشف و ۴ نفر در این رابطه دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441343" target="_blank">📅 08:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsEXzjSYcDOKQXsaqtVuDu_4LMuxCqHxIFfx4URSbEHSeBFcwa2-QjAzlN6L16E_US1hCBYCdoPqwM3yS03eulIqoUVh1LTiRtoAXCj035Ak3Y_RLYb_sJ59jxF6gWFxcKwIh19DyGe5Z325EnJiXYLOcS0T5RicPzme0FIwpGZU5MRzNiQq92Zrpa-NtYWEPBDtv103SgYs5sDnnBWZwLDg24Rjn3EuibJhBbfx9_PNTEfn9hR_npJUw639xNpHolqzIgahZQh4vil6IgVvwnVQi7iUrNJujoM2wZsUeUb4NyYTuSfSSzzHaw6P_g7RlHMHOwUecj0Q67IV5oBEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N48qaJ8IQ-bFj878QNejea5_ndDkSI_R0GNS6GWk42BqswYRLeSyWOGhHCs45gLKevamIfkV-k39HCfy3MtszfxcSS6X4AYdUjhALv53QTV1xJ1abH-8v__MDnjYvF4YAXucInjMfW7-806B9MJZSUY2HncOcDMLluqrRzC2FtdjUvHYGJUsyz5EEz2UbIrymFDPN9hqRBtsY9nBCqhWEuDumDlZbMItz_UsDxD7hAeSQa9cSSRVURxsjRLf0auQcG_KOrF4KOtv9ovpgjV8S2Uss15Py42X1VxBDzdUmRHgSkqeKfgIh-OpI02tPUr3mJHYJHhZr-RomxqypFFoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LpJbwCxRjKHytbfW6UoDLFvEdgQpv7Gn3W1OSjT2eroBL-QbiTPBlRctzwinZGw0xSchYtuFKwPU3IolcG-Rs5PdqMocLVfUyetKneXc4Ilun34qz7RODuusxNm7fJjG0pZiDpaHyoBAaOQJOUCHGLu0m7969H7mn__-rMJisdpWHCKrszJGalTxu0XTeuwWRdlDs2cR9Xkd6GzsejZs9exGgN7e8WDsQCH6ZEAV6yjaS0FD2gUuxtM8_uRykYRmSjV9_5TOaxe2IKDyjDmvMXKsvzmbMDqW-mOXDd8V6CD_mzHbnsf2SrzmkQLXlJ0eSqIQ0Nh-p4XDYnxYvNAIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5HzZvvbadGfIJvY4Apt1kUeiEHzmRRfhZsNnpSJMqPqYx5wSIsTHUzbgXtYaSZnz-PE0iaajwZmZBl7apPgj3hFr1Mi8F1fuKARHwEG4OqwXHwC9kBG5lXqVcDY1nGuki9ZG5Ye_8kSpRAb83agIH2cZwiUy4FZZsv3ewAC64ztONiv7EjDuIjnynVyR8igzaYrzWmH4W6pfYsRWLUuZC0Hv97GhGHlrVHrk-1KGSKdwjbN2vrurbot0NMO4absZMc-o3vHQMgkPVehRIUE93GX5rK0PKPnXl4Mg0PkHUsFHNp4I8CPf6VUVOGVQ09lnutxRNiDnogvAA3kgedl3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ9jUXjqdk_upmItkjKRRHIfOr8Ln-6eVpr8znHiKvCHVB8z8WsLxWCrEjR2Co-nUtVA_1M2ClFYMOqXkhSThEYqip9TSv1AzmjbWPrKj-Knd6jROiB-LeYQumI82KFIFtD2g0kbdUd0pSwNqUnCWyKFA5CQKt2SiaV6lLX6VksWtqjuPn30iNsqgXX01yMU1OYRr6kkROIxzAWxhbMqlzDWhBhbt_KeugmbV_eXOWkkcOqDYYrbIj_39Qzw8j_sD0Krg29SoUu6w6EMAk2yRNFSmcPW5Ywdh3aWY7ckb608MFHBHu9iBhUz_3nat4mJyDPEx5g2Nuvmwy2aXoqwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sq2AvvkvC1ZWCacbae-mBuyx5JzClKFimGEJM6mSzJbD_mTeKmsPqw0u4ucEfF-RUNjFZJUMK_LS3Vgr6xuJF4lKk9Cy8v1U9m-PkmB441oFGOgyqga9tVXcA1W5ULec-V186ZCqKWC-t7c-k_8_k4eELBHlsw91E3eg9L2YDukf1pgB2CKqL9xfCl3SKqRIzc2v5xz3aXHdJbhTJ3ILeyD-wA-kzv6AoEsSeKMyBp-6jwu1t9OJTmsMX0NRkJEsXqp0R4S9tmH_9W4OmUTvcY52TFiOhq-AEpUsrFNxMSfNWju51IRf6G609h7QW-lkQ3xztfw6i70QCRzLvPcyAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هنرنمایی رزمی‌کاران در تجمع شبانهٔ یزد
عکس:
علیرضا رجب زادگان
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/441337" target="_blank">📅 08:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAmc0BgSpZ_DPY0LTg7NkU0cAU4W2cU8qcwmPuYKwCfSuoLUSx5U31jbU4I1hoFeDJSvSxxS7gGQ2CTIxyZ7BJs-LIGrr40bbHPyzQ8taVo13YPn2CQAz8m8WYljBE4yVvoyIcQw4YsTe6Y8JBDE2pWHLrckVRA3W6Rwn-aYA7DuMYVRnoMKCeUDK_n9c2UE1ykHhHL-P-2rKHv5L877uX184LjtBdnKz9Cuge205fl1TXXRqYaOZEub1yystLcFHwmDjVFENY4faKMos170_rCAgpYbKH8pkPtJaRI8F80ylhGX_CmaZbYBreUmpu2EbPc2lCrN7nPJkDRnum9R7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنرستانی‌ها باید از شنبه به مدرسه بروند
🔹
امسال نیمی از آموزش‌های دانش‌آموزان در فضای‌مجازی سپری شد اما این امکان برای دانش‌آموزان هنرستانی که دروس مهارتی داشتند، فراهم نبود.
🔹
حالا آموزش‌وپرورش از فعال‌سازی کارگاه‌های هنرستان‌ها با هدف آموزش پودمان‌های جاماندۀ دروس کارگاهی از ۲۳ خرداد ۱۴۰۵ خبر داده است.
🔹
قرار است فرایند آموزش پودمان‌ها ترجیحاً ظرف دوهفتۀ آموزشی به پایان برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441336" target="_blank">📅 07:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فعال‌شدن سامانه‌های پدافندی در اردن
🔹
منابع محلی با انتشار تصاویری از فعالیت سامانه‌های پدافند هوایی در اردن، همزمان با هدف قرارداده‌شدن پایگاه تروریست‌های آمریکایی توسط موشک‌های ایرانی خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/441335" target="_blank">📅 06:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
سپاه: محل استقرار جنگنده‌های آمریکایی منهدم شد
🔹
در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا، برای تنبیه متجاوز صبح امروز با ۱۲ فروند موشک بالستیک محل استقرار جنگنده های F35، F15، F16 آمریکایی و همچنین تاسیسات مهم ارتش تروریستی آمریکا واقع در پایگاه هوایی و مرکز کنترل الازرق را هدف قرار داده و آن تاسیسات و مقدار زیادی از جنگنده‌ها منهدم شدند.
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/441334" target="_blank">📅 06:35 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
