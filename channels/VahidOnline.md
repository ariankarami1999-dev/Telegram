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
<img src="https://cdn1.telesco.pe/file/O15gZhAjeYi5FE_heJX9zvB4GNzDwNKlfpqoEtyXjOYL56p1jyF4J-zYUi5vpLFwI40WZN3JXQNl1pw4xsxA_0tRgMvpCARpnhi3ZUJHDg-LwctvCzICWO9bcs4go4aPXFk3F2K4h9-_cdsUUamjhkpi6tFd9GuOjsroF9ZTfv0HDsrc-MHI2HktOYbXgndBFp5CyR6mJ_bUJdNIw2Uwcm3yhfttVCaGhVk68WyYVvdYyx8kTkXa1KasxhVEtAnNEkUmBesOMChbghIrKse8cIgKmrC2ZVxDxXFFEpdP5W9wa1E8UnjYvxbI0RzIPZxXBmv-AbUjwVPays1STXZA0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 02:22:09</div>
<hr>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lQmVVuO1QHQ-79RwaABTjeBYi3JDKN3zYqgza-dAfLfVZBJu3CMO7kPrHmIneJLq8nMGJ5b0SxU0BiBuK6m8vN7tCBdmh6ekGlJDQq9oD9WvEiKgY2fZl-bGWPMvVoF-rwAFqQJ6KyoL2d9BV7P-S6BbCK6__rqF9xSB7YTn2nQBLJfevKKmABwWEb9lTLQ30jGHZLMMNIHd7rWkGulB0i1k8dd9Smi7o24E6xpJmAiAvaA6r-DvYFitjW7i7n7cvY2dVR0gXPgYrpOr8DBLiYRnagkH2nCRW-l9omh7sVyZWIPJB4ZnrBjJQo_KfARp7LyOx7zCs4weEQl0m2ADFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EfHCfQAdNnvWcJ_3H5orjBqzao2H2PyWt0kc4RUMtuGhVBaS3cbEiTQ7c4LOnjCvh-DYX_vDIsJ7nPDjcWvxSOpSFS0ndSpYlWK8lAFbmsK5DMnWIHV8vv8VW5A9AC6tBCBSyyns3mK5lPt1clihwq2Iqzsa-pC0pSIamnME371VjLQLbU4ZBBtOpquTSiPNP3dtOfgTob95ELK75hKoG5PHoCYNxuQ5HZhLDQJOACLT7ECRuSl9wMrxxgB3bFtHnnXs15WXcUt4Qv9jyrIole9LQzekenVDnMIAPHdaVJC67KIbrfi-LkqHwyXl6sWVRsB5vCp1xRGhvY4BTzd0TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری دانشجو گزارش داد که در ["حمله سحرگاه شب گذشته ۴ خرداد"] در جنوب جزیره لارکآمریکا و اسرائیل به جنوب جزیره لارک، عباس اسلامی، قدرت زرنگاری و عبدالرضا گلزاری، نیروهای سپاه پاسداران کشته شدند.
براساس این گزارش «تعداد دقیق کشته‌شدگان هنوز مشخص نشده است».
@
VahidOOnLine
گویا این واقعه مربوط به اولین ساعت‌های دوشنبه است. یعنی حدود ۲۴ ساعت قبل
ولی به نظر می‌رسه اون دسته از منابع جمهوری اسلامی که این خبر رو پخش کردند عمدا طوری گمراه‌کننده نوشتند که مربوط به صداهای شنیده شده الان به نظر بیاد.
ولی این توییت مربوط به ساعت ۷ شب دوشنبه است که درباره همین خبر به نظر می‌رسه:
دیشب یه قایق سپاه در حال مین ریزی در تنگه هرمز مورد اصابت یک جنگده که از خاک امارات بلند شده بود قرار میگیره و چهار نفر از نیروهای سپاه کشته میشن
YourAnon_Zeus
حالا این خبر درسته یا نه نمی‌دونم ولی مربوط به
صداهای شنیده شده ساعتی پیش
نیست. من هم ساعت سه چهار صبح دوشنبه پیام‌هایی داشتم از شنیده شدن صدا در قشم و بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/VahidOnline/75716" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LX6-FqjvTlzQul_98IDgeuvmtTyAKSAOOfcVaR32HCZ5IUZ5DKmvEGo6F0XiLcFhG-ioImuQAV_28Q9ReSFcWPf0bxjyzMcP0wUoBOo6ftfmSZNLoZ1VroNsMSiOmJC2go1N86OY48xRnTQRw00YKUOnxws3Z1hVWGpikxFuPBKdxHjRrVLildb4RCochY-w93gxwtMD3D3_01nS4VKICUJcBdL6v4_LRu-7oxlsy8VzNS_FpmqmdcqvA0DLBhFUeTMGTOg_ONfRiptRvjdpyy7p1f2RcO3Pdriyg2n_zqmrQTTzSdtEhOCeBQUmMQ-MlmzzGrCIfDrkLDhwtes-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
غبار هسته‌ای، یعنی اورانیوم غنی‌شده، یا باید فوراً به ایالات متحده تحویل داده شود تا به کشورمان منتقل و نابود شود، یا ترجیحاً، در همکاری و هماهنگی با جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری نابود شود؛ در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، شاهد این روند و رویداد باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/VahidOnline/75715" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی درباره صدای شنیده شدن صدای انفجار:
بندرعباس سه بار صدای شدید اومد الان
صدای بمب میاد.
بندرعباس ساعت ۲۳:۴۰
همین الان ساعت ۲۳:۴۰ صدای سه تا انفجار شدید توو بندرعباس اومد. نزدیک پایگاه شکاری یا همون فرودگاه بود به نظرم
سلام وحید جان
بندر عباس صدای آزاد سازی پول های بلوکه شده میاد
بندرعباس ۲۳:۴۰ سه تا انفجار شدید
حاجی۲۳/۴۰ سه تا انفجار شدید شرق بندرعباس
دقیقا صدای انفجار ۴۰روز جنگ بود
سلام همین الان بندرعباس صدای دوتا انفجار اومد
بندرعباس حدود ۲۳:۴۰ دقیقه سمت فرودگاه صدای سه انفجار اومد.
درود وحید جان
بندر عباس ۱۱:۴۲ سه تا صدای زدن اومد
بندرعباس، ساعت 11.40
صدای شدید انفجار و لرزش
سه تا صدای انفجار پشت هم شنیدیم بندرعباس
بندرعباس 11:40  شب 4 خرداد صدای انفجار
بندرعباس ۵ بار صدای انفجار
ما سمت پایگاه هوایی هستیم نسبتا شدید بود
پدافند سمت فرودگاه بندرعباس فعال شده ساعت ۲۳:۴۵
آپدیت:
رسانه‌های ایران شامگاه دوشنبه از شنیده‌شدن صداهای انفجار در بندرعباس و همزمان در خلیج فارس حوالی سیریک و جاسک خبر دادند.
معاون استاندار هرمزگان اعلام کرد منشا صدای انفجار در حال بررسی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75714" target="_blank">📅 23:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=T2OmIR4OSRfxoApcf6YRSoptynVn2NbR6BO0DCzQwj2nOkzDBIGcxQ4tWPstdrk1C3ixGjrXe4tS38ImGuEhRjZMga1xYKX7dAwUOYuTVJM-ioO3RFi73Rvmdy3tuSaqRDYylHQtDNnc0q2saexiUAdVad1FbPXnZOcskpMupd8uAkZLynHPssOFe4Xj6KBv2JGYhBCqXNcz4txCuoTi9YqKjRWmdOtKudLePPjzXq2dw64yyUCIx9AqCkA6Zif0E0CW4229NdDm24FrubjiqMjcUfq8n0TFS1gf1vowsOlf96nQNvBaoCzmiLF8pNjCmv9zI1CnhuolexfHP9Xi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=T2OmIR4OSRfxoApcf6YRSoptynVn2NbR6BO0DCzQwj2nOkzDBIGcxQ4tWPstdrk1C3ixGjrXe4tS38ImGuEhRjZMga1xYKX7dAwUOYuTVJM-ioO3RFi73Rvmdy3tuSaqRDYylHQtDNnc0q2saexiUAdVad1FbPXnZOcskpMupd8uAkZLynHPssOFe4Xj6KBv2JGYhBCqXNcz4txCuoTi9YqKjRWmdOtKudLePPjzXq2dw64yyUCIx9AqCkA6Zif0E0CW4229NdDm24FrubjiqMjcUfq8n0TFS1gf1vowsOlf96nQNvBaoCzmiLF8pNjCmv9zI1CnhuolexfHP9Xi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه خبر داد که دستور حملات تازه به جنوب لبنان در تلاش برای «خرد کردن» گروه حزب‌الله را صادر کرده است.
ساعتی بعد خبرگزاری‌ها از چند حمله شدید اسرائیل به این منطقه خبر دادند.
نتانیاهو در ویدئویی که در شبکه تلگرام منتشر شد خبر داد که خواستار «سرعت بیشتر دادن» به حملات ارتش اسرائیل شده است.
او همچنین حزب‌الله را متهم کرد که با پهپاد نیروهای اسرائیلی را هدف گرفته است.
صدور دستور حمله بیشتر به لبنان، همزمان است با خواسته دو وزیر افراطی در کابینه اسرائیل که در همین روز خواستار تشدید حملات به جنوب لبنان و همین طور پایتخت، بیروت، شده بودند.
حمله اسرائیل به این منطقه در حالی رخ می‌دهد که در سوی دیگر تهران و واشینگتن از جمله درباره پایان جنگ در لبنان مذاکره می‌کنند.
حکومت ایران در هر دور از مذاکرات اخیر خود با آمریکا، پایان جنگ در لبنان را نیز خواستار شده است.
حملات متقابل اسرائیل و حزب‌الله در حالی رخ می‌دهد که دو طرف بیش از یک ماه است که به طور اسمی در آتش‌بس به سر می‌برند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75713" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nDk-jYbmRVddMb1BP8JJfzLM-WxhRvtFcqBJk9KNrZhJOwjk-GWlw7S6Rk933CpMLk0XTS_np9R-cTd03DwDWgytgGo0vQz-sEbP9Ql15ovUQnVhxkHm6FDFGmAUIlaGV6yQSM6TUC19N3n6BOYnFnCisjLnWNCLk-m0ui5TsMQpaJPeSkzUm4DgoJsGWnEeasr0kGYDWC9GowR8zAReuM3ZmpOvuNHYydQDkaNuN1S84u4ny5RPYxaDBauqM0PVDfLEs2_hjQzP5Mo1Xs8Q3JvNH4L7bp1mmFpoXE0w6WUbxmguZbkc3ZO4sewm_FTu284yJgnCg1NCyshi-3PpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره به نقل از یک منبع آگاه
گزارش
داد میانجی‌گری قطر به دستیابی به تفاهمی میان آمریکا و جمهوری اسلامی درباره دارایی‌های مسدودشده ایران منجر شده است.
این منبع افزود با توجه به اهمیت بالای این موضوع برای ایران، احتمال زیادی وجود دارد توافق میان آمریکا و جمهوری اسلامی فردا اعلام شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/75712" target="_blank">📅 23:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdEKhL0_4xOE3aUlG-DdD83KLczlW7t2z4MFQLsL9LwioJFFiu6IiPQUNxlowMJp-mF4OK4MRUlAzKzKtnSkcvR2ZQKUV7e8FxzF5XreChwad-RVLRCEYxx1QmxvZz_HmHoiJIyzO8EU9XYzcx9cu9AkKz6fPHI1wr9Wf11Wa_hHXUKCwKN25u_45JZ-BiMbOCe3F_Gc5C2KQduyl-4yKcNYA9Q4kQ37bM8gOjSpnizSSGa1mE1fcXeGqVXLRLq7rYUgVvIm96utV8queHLq7s_jYqIT8v3xxAYVLmDZ7tYnjjEnZV1qaWIkB1s6AGu8BMSdkNYxPJzRUG1R3NF3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پس از انتشار خبر تصویب تصمیم بازگشت اینترنت به خانه‌های مردم، چند رسانه در داخل کشور می‌گویند که مسعود پزشکیان، رئیس جمهور، این مصوبه را به طور رسمی ابلاغ کرده است.
رسانه‌ها در ایران روز دوشنبه از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌ بودند، مصوبه‌ای که برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، بود.
به گزارش سیتنا، پایگاه خبری فناوری اطلاعات، بر اساس این مصوبه، اینترنت عمومی باید «به وضعیت قبل از دی‌ماه ۱۴۰۴» بازگردد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75710" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iByIIe3DLAvyZnsdGS8-xtq46g0UziuJBxHmF4ujwux9791EF0HMTOj6KxmZ74Td8R8mdYfUipvRwF5MXkJXcQLsxZ8xWuJcXPv00fN5v89mJ_8Greu3KUh5UftauovKAR_cAqppYNCuK-72gY9ruT8p94YL-9AMVpAhqgNxSloDD0nYG5AAf6UeYeliME7ssBSDNkavpl4RWOngDi8YTwXKd2ygc24-Reg5o_eU4M6BHybyPgm1-xZrpKmDL8C_3JcU2XEfXcMiKwOZ4JL_Jvln8m3gFjPjMxnSNWNmdkFqWFcGcZLyNIc_m-GojWTiKhZv4Y2S9PM3bcpUrT_Qpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از منابع آگاه گزارش داد پیش‌نویس یک یادداشت تفاهم اولیه و نهایی میان آمریکا و جمهوری اسلامی در حال بررسی است؛ تفاهمی که شامل بازگشایی تنگه هرمز، تمدید آتش‌بس و کاهش برخی محدودیت‌ها علیه ایران می‌شود.
بر اساس گزارش العربیه، در پیش‌نویس این تفاهم‌نامه آمده است تنگه هرمز بدون دریافت هزینه از کشتی‌ها بازگشایی خواهد شد و عملیات پاکسازی مین‌ها نیز انجام می‌شود.
این گزارش همچنین می‌گوید در چارچوب این تفاهم، به جمهوری اسلامی اجازه فروش و صادرات نفت داده خواهد شد.
العربیه افزود پیش‌نویس توافق شامل تمدید ۶۰ روزه آتش‌بس است و امکان تمدید دوباره آن نیز وجود دارد.
بر اساس این گزارش، آمریکا همچنین متعهد شده محدودیت‌ها علیه بنادر جنوب ایران را کاهش دهد.
منابع العربیه گفته‌اند بخشی از دارایی‌های مسدودشده ایران نیز بر اساس سازوکاری مشخص آزاد خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75709" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/paaG3GHZS2c4ytrvOVe0Jaz5fQFDdb_Bw6rKoN5oprXsn99sb76_EF8H2NGoIidyMC4Inz-ohVPjjU8YSyL7vcEyajBfw065ZmVmsnlLwI35AOm_3z5t8kvSznKVjhMojgJOc9xNJ99_2DNpEAqUV1S30bxUJbM2CAjMW1D3aS0kcAmiwDNoKlG7ZEfKIPW9rCQCpTlWeqqHiqVOTWWTvkurmjfDj9PVQ5OuF9NvOoaC0TiMOGgK1JxLMb7lyWJb3F7nxKujhWwBc9O_dCLsSps9Qvk7fx84Ex9zsitgduUGQB9qDBPRtn6JYa4jByIWW7ezRJAk3PtUnUrwL4rjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VoZBNQTPBzIy6BfhbZKUNNFgoaQpdjFgzXx89uCSW3OdMtnFvLc9Ty4YlU9v9WATsNQIGxo2eOU7REpqiw8QsYW0BCxRqWlJ_NsGhgygg_KMYA7_Extxh2KROJSPmzpv1EflfPgilAMYN5nO465-bkqLQ3lWEZZFC-G6Yng7m4hWWJYR_LdOcrDqIJbnRjGMqcHfG_plXPFGtSPYx_kQITv-flwOo4k3VqW-_f7kxtETTLiqcmoywAu_LYtk3JelL0MAaK-lkvUG0RlCpWT9zDciNXhtNqgfO1QxPKInTJ9briGi7mGYotLI2ZwXCpwLKXWNa_pEJd2G2_zXGVqMOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، در پیامی با اشاره به «میدان نظامی، میدان دیپلماسی و مردم مبعوث‌شده حاضر در خیابان» نوشت: عقب‌نشینی در کار نخواهد بود.
او تاکید کرد: بیش از هر زمان دیگری به وحدت و انسجام نیاز داریم تا آمریکایی‌ها و اسرائیلی‌ها مایوس شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/75707" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JHYqzapz0i4Yw1_WFoCIHmRN5-aRgRmOB3KPLbGjdZT5bq0_rTjZxjR6JwHFSK7UgZF56XZs1z7RzpG0Pdrt4zEIKrUG8nJY9WTFZI_stX0NsdOLVDmDx-1pwcldtZ538uSn3XNwWWDBTt4ZWun_3qEDe4q-lmDL57a13tE1OnNrw0-jltJRR4r-MLlm_Ak0qWjhmW8ndfDAinUn9tNHmcUmhBBvBqs30sW8VWmFvFebKgWueTK-95JNeeEUPJQynT5EgLVaZ6HLS6lOWPjQU2rye29jN-SFMAt7rRjPNs0C9f8cMDZ8eApBJ_U3DzYb949oAfjGndkIHOvIjSLUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S7Bi5xIRES1J96C_lCR_O1yTcUwP2ws9brD5SPHCi4hyh97k6ydol1yKwhvnxhZIbSB_o5GLvu203a2n5Pr5uo7mWifaZHb3NN3XVN3JtkcWgipJW-ZdX68P1ckajKfrzKhRdFXDYbEAlfLVxgpITcZaEKaNmVpcTOsyKZsj7Wcfx-sw0yYHA7dw7bCMPPLGGl2LyMDLoyb5UKzAnkKYz_ayqbptpIdsu6ArEpuibE2vRAr4MjN6Hkhx3wRBzQMK4brqT5Z-DaBa7ONHFV6LAib4OnqBHpqlX4qf82P47CGs4NkHqJu41ogLW_KSN5Yfn2Nn2hzzfv2e9MlQsV3Yhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ از اکانت بقیه بازنشر کرده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75705" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DTgXMIXUI4wiQTRSyf9ArrAhcjX05lNAqs_KqDtOV9Bk2QioWj_e_rL_5og17LAGWCvVqn7OfKc7795dgUcoLtnVE7YmoSx463OnYfI9bNQ02VFenaVYRnteinzKassQpuMeUQ0PfZvtjTTperwRaAyJntSWPp-JlZkLREb_fWjCe4xg-8Nd0GhTDaPPOioMg-ipcAmwICL9a8c3buznKP6LVbpEaHstpWk1PqSC3Wu3-YrBJxSYEwsVxvmJ4jhY9VzWiT9DOCCE4NiRe6X8Hw9-XzAhFnWJiV9u98s_rUcJiUaMuXVOyMPwI0bRyD-JBVhAQ-k0gM6HIymiyv85kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F2pldae20c_QkyPZF-HHOKyjRt6QVx9GtntU08ukCiOMQkMfN2Pls39ZN56kABczQsFem5h45E9BzmOftWiGCNDEki8ct09tzJPkmBQZm7zI921jQZmIAPopx-5Gi8nlntbS-Z4mpxGU6PZyskIPHm4fLBUvyJ-Asda_HGD0qTi86G8xqW8P_NGWBnx-_f6gMpavoca0kSDvp5p_-l4vvTLRjANVaMkz_lPScPn25NUKA0KHTlw0R3y5uX-465nLnJHeJUcOz7LubEHY9Uup-XSdQGhEU8NQzkhtZGwJ3FDZXz_5Bl_B_J948BvbPDmUppTcOufk5qkdYFNeC1MkHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه در تازه‌ترین پیام خود در شبکه اجتماعی‌اش ضمن خبر دادن از پیشرفت «خوب» در مذاکره با ایران، از تمام کشورهای دخیل در این مذاکرات خواست پس از حصول توافق با ایران، بلافاصله به پیمان‌های ابراهیم بپیوندند.
پیمان یا پیمان‌های ابراهیم طرحی بود که دونالد ترامپ در دوره اول خود برای تلاش در راه عادی‌سازی روابط میان اعراب و اسرائیل آغاز کرد و موفق شد تا چندین کشور از جمله بحرین و امارات متحده عربی را هم به این کار ترغیب کند.
حال رئیس جمهور آمریکا روند توافق با جمهوری اسلامی را به این طرح پیوند زده و به گفته خود این «خواسته اجباری» را با دیگر کشورهای عرب خلیج فارس و همین طور ترکیه مطرح کرده که به‌فوریت و همزمان به پیمان ابراهیم بپیوندند.
@
VahidHeadline
دونالد ترامپ در شبکه تروث سوشال نوشت که پیوستن جمهوری اسلامی به پیمان ابراهیم، می‌تواند به «اتفاقی تاریخی» تبدیل شود.
او افزود که در گفت‌وگو با سران عربستان سعودی، امارات متحده عربی، قطر، ترکیه، مصر، اردن و بحرین، تاکید کرده لازم است همه این کشورها به‌طور هم‌زمان پیمان ابراهیم را برای عادی‌سازی روابط با اسرائیل امضا کنند.
ترامپ نوشت: ««کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یکی دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند که این توافق با ایران را به رویدادی بسیار تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75703" target="_blank">📅 18:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NlhYAMwxa857MtnBlLA7B2zHvWQ7VYX-vmi8n4BfBnjZMncodjkB0qogm0S8k6I8I4fwKloV2LbCd1fu1Q1lDW-8W9yVO8ALEmTbdDrKAryOTDrq9KFhqtqzncQCb_Kn9nqHdpGD5sOJoCUKtCZ4K74M_OV07j6YK0f1U-GqTpvk-_ZEDpV3S1CMFTn3eEfuZWqRz3jCSI4b0yg-cFVMppTpF3GRl6zFljQ-UdGtxi2_HNXUEivMNHIklteUyGbVUXs6OpAdGcBM_1IMsgDaPtdSbz46dagcc7WgBX4qw7R9pkSjDLgx7Jhmnrpy2VZfJROold0HAZ4zM0o2gKg5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cu5k6LKgnhFLjDQSUncJ8gsXgMwDyTNN93-JAgNZvF6q8Ut8U03418k-78OPFt1Xc-gqvNVWa5HluhqI_yBLx-Oxe9bNQ8ZRHdgfviDDPOWk4_mdRWxgpS_lyOlvHJIq1i-qjI75K3mPTFfi0Pi68lWRoLWlszUYssfi7Y-m_f1PlmOKIDtywjpFP-WqZn6tGcDb9IhlYwfSVUiqWjm1XeBJSaLLnqW6gBCf8CcIpAzBIcmv-akVhwuNumlqPL5xn-0K5cL4ROTMFGHPbF3eYVT9fMpz8atHW2cwdSxvE4shc1GQITby06vkzqHtigXxISQfRCBEhCkLL25oWdSSwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری‌های رویترز و فرانسه به نقل از یک مقام آگاه، از سفر غیر‌منتظره محمد باقر قالیباف و عباس عراقچی، مذاکره‌کنندگان ارشد ایران، به دوحه خبر داده‌اند.
بر اساس این گزارش‌ها، رئیس مجلس و وزیر خارجه ایران برای گفت‌وگو با نخست‌وزیر قطر به دوحه سفر کرده‌اند.
رویترز نوشت که این گفت‌و‌گوها عمدتا درباره «تنگه هرمز و ذخایر اورانیوم غنی‌شده» ایران است.
رسانه‌های ایران گزارش داده بودند که عبدالناصر همتی، رئیس کل بانک مرکزی ایران، برای «بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات» به قطر سفر کرده است.
هیئتی از قطر هفته پیش به ایران سفر کرده بود.
یکی از خواسته‌های ایران در مذاکره با آمریکا آزاد شدن منابع مالی مسدودشده‌اش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75701" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKj1jpsK78ACke2k0d4_0OU_JnvGCwkxklfRueQJ3hklcTwf2Fhk_dCBeuNXw4zi3m6IDgcRB9i8Y-aCCrRyYuLX2xuk_tvRFO6S1EQHd6q8hKDoLfHLhZMKstQD6DtsNmRrQRuVJHt1swmXGSB0y8kD6V_3G41WZdHmF5Fe-5wbz-ksJ7KUXf3gn5Yhq1T-TRipcKTvvleSWWRCwZhzQn6J2NypfoJUUi6zMetQNpiQNK_hoFBQFNQbz3JsiuRS6zHmFkCVEDGd9XCxZgGYe_ktrfSoxlDPBRohVGLkFXlDMl34l8I5Or3naYX60OZS4TmAYcsYtMwn2UAj15MkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی در شبکه اجتماعی تروث سوشال گفت توافق احتمالی با ایران یا «عالی و معنادار» خواهد بود یا اساساً توافقی در کار نخواهد بود.
آقای ترامپ در این پیام، منتقدان خود در میان دموکرات‌ها و برخی جمهوری‌خواهان را به باد انتقاد گرفت و گفت آنان «هیچ چیز» دربارهٔ توافق احتمالی او با ایران نمی‌دانند و حتی دربارهٔ موضوعاتی اظهار نظر می‌کنند که به گفتهٔ او «هنوز مذاکره نشده‌اند».
ترامپ تأکید کرد توافق مورد نظر او با ایران «دقیقاً نقطهٔ مقابل» توافق هسته‌ای برجام خواهد بود؛ توافقی که او بار دیگر آن را «فاجعه» خواند و دولت باراک اوباما را به گشودن «مسیر مستقیم و آشکار» ایران به سوی جنگ‌افزار هسته‌ای متهم کرد.
او در پایان پیام خود نوشت: «من چنین توافق‌هایی نمی‌کنم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/75700" target="_blank">📅 18:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsJT-RIh2QHN_ELKeNr_VrxW7ATqG9I2Hl26JWl9llaD3Dh2wJ2XbKyvW1dkguc9x12XvqvKUWidwMsJ4knYQt9Bbvq7VIOLIXA0KzhDPQtyiyMjA9cRxP9el_BZtycaFYDDITQo7Hl2EJ1qrD0uUhAH2dzn0FAo9c3Pk1uPC4n5x-TvPeGkgjB8CovzbbycJT8AirvGK7qQ7et_tezhevW5-tymG3Il2JPCnkKjZPstaHH-LAt1PKNfygyL7TqDvY7-sySVK70szWJIqcvJ7jjMSguWpRuyakFsPrKPvWYweNoCx3ZATkq3gad8suUpbPBkWb7gMamG8jHo4Ku7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌اند؛ مصوبه‌ای که هنوز برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، است.
خبرگزاری فارس روز دوشنبه چهارم خرداد گزارش داد چهارمین جلسه این ستاد به ریاست محمدرضا عارف، معاون اول رئیس‌جمهور، برگزار شد و در آن «مصوبات مهمی» دربارهٔ اتصال به اینترنت بین‌الملل به تصویب رسید.
فارس به نقل از یک منبع نوشت که «برقراری اتصال اینترنت بین‌الملل» با ۹ رأی موافق و سه رأی مخالف تصویب شده و برای تأیید به دفتر رئیس‌جمهور ارسال شده است.
خبرگزاری تسنیم نیز با انتشار گزارشی مشابه نوشت مصوبات این جلسه پس از تأیید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ خواهد شد.
در همین حال، سیتنا، رسانه تخصصی حوزه ارتباطات و فناوری اطلاعات، به نقل از «یک منبع آگاه» گزارش داد که در جلسه صبح دوشنبه «بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴» مصوب شده و در صورت تأیید مسعود پزشکیان، جهت اجرا به وزارت ارتباطات ابلاغ خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/VahidOnline/75699" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owAgQ68AQQFa-6416vCBzD7Q915GySjVZqyHVybEBcB7AevyOKwukPQDtlZ-0MLMcm8QRzuqCz9aGmLRTSScVJaiUVp3vU8JvHQTkTUyaeqGOO8pFvL2oGO9O8-G8trruS3cwmgReMgbPzBLJUht3ZDfTZQjBrZYiiII7O3VO_cIQmw9wv6XH0CEdf0CqehYX6Ht0jiSGsqlrlcdBv-9SP5LTsq4URO16CBnMe1IDPGJE09aNRaHPRKmZfDbMpiwO9VJD0yxmFLOPtscjaccetm8X9MPuplPmTXuB7zzVRf0UwsPQMtBqUXgIfvYUZicAS1W7epg3tdomuQ0ns9XHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از «حسین کرمانپور»، رییس مرکز روابط عمومی وزارت بهداشت، گزارش دادند که جراحت‌های وارد شده به «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، در جریان حملات اخیر «سطحی» بوده و مشکل جدی برای او ایجاد نکرده است.
کرمانپور گفت رهبر جمهوری اسلامی تنها از ناحیه صورت، سر و پاها دچار جراحت شده و این آسیب‌ها «منجر به قطع عضو یا ناراحتی خاصی نشده است.»او همچنین مدعی شد که هنگام انتقال خامنه‌ای به بیمارستان، پزشکان از او خواسته‌اند روزه خود را بشکند، اما او تا زمان افطار روزه‌اش را ادامه داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/VahidOnline/75698" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1_K7poIOjSuZ_75zXYJrn1Irv74QzvgPvGvb2jaftsF6WFzG_fTWBF-uPNEOQZlVNBeGDuPYLN0Yq9yCD2yvndallnGfdlCvUP-gBlk_GgmrOHprUHDnqXVvqiUyzhZU1yO7fNKk9vF-_uy_FW8vGIs3GurlZan52hiCvk7oniCnNUDNi8JZXi9NBvZwL1-9WzsUJIknbL7ZIq_AralQMNkT8SaRDz-nhnhlOyX0I0bElzL8x322cOrr0oztGQlBD2G2KF2KW4-HXUVPG9STNfVE0a6aJNfuwkxLC_Kd5HzeHwhqbjV9M8Yt6Wp_zuEbebdFAA4VlnwNFz64JTuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید که سفر وزیر خارجه به نیویورک برای شرکت در نشست شورای امنیت «منتفی» شده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران، دلیل انجام نشدن سفر عباس عراقچی را «مشکل روادید» عنوان کرد.
آقای بقایی چهارشنبه هفته پیش درمورد حضور آقای عراقچی در این نشست گفته بود: «این سفر به نیویورک احتمال دارد انجام شود و البته ممکن هم هست انجام نشود، چون هنوز قطعی نیست. دلیلش هم این است که هم باید روادید صادر شود و هم ممکن است اولویت‌های دیگری داشته باشیم.»
چین به‌عنوان رئیس دوره‌ای شورای امنیت، سه‌شنبه ۲۶ مه یک بحث آزاد در سطح بالا با موضوع «حفظ اهداف و اصول منشور سازمان ملل و تقویت نظام بین‌المللی متمرکز بر سازمان ملل» برگزار خواهد کرد.
این جلسه به ریاست وانگ یی، عضو دفتر سیاسی کمیته مرکزی حزب کمونیست و وزیر امور خارجه چین، برگزار می‌شود.
چین این نشست را «فرصتی» برای همبستگی و اجماع کشورهای عضو توصیف کرد تا «تعهد راسخ خود را به حفظ اهداف و اصول منشور سازمان ملل متحد مجددا تصریح و نقش محوری این سازمان را در نظام بین‌المللی احیا کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/75697" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_SXiI8n1CpO5UfIXI4M2FT2T5f9maT2h_WSLL59TXnlhdTOEpL4Ei8fj7thIMY_InkR4ZaOCrnJt79iaMqMKhFBH3XjohShX69A3Kgu9J4NQP_y6RJ6SJGzZIRs1aWJ5RnANgovg3UHECQPCH6phQ-PyuoD7YkmTHD6sFCuP1YL5JLqIro_8Ao-dMM6jDexgOEg_cCHAoFdA_1DGYOW2hIpoADyVe2p9rYKixglcmn1S1phzjfsQK6xBb6ceT32lYHPvyRE8kQPuy5P0tNNdEITpRrpKF30pldKeQ2KD8WxYO6ThD-qlmvwfElOMO7dkebhQPb9ngUyViwxlECi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۲۶ اردیبهشت‌ماه ۱۴۰۵، «جانا سعدوئی»، زن ۱۹ ساله، مادر دو کودک و اهل روستای تاریمیش از توابع بخش قطور شهرستان خوی، به دست همسر خود به قتل رسیده است.
به گفته منابع آگاه، همسر این زن پس از وارد کردن ضربات مرگبار، تلاش کرده است ماجرا را به‌عنوان «خودکشی» جلوه دهد.
با این حال، نتایج بررسی‌های پزشکی قانونی و تناقض‌های موجود در روایت‌ها و اظهارات مطرح‌شده، ابعاد این قتل و تلاش برای صحنه‌سازی را آشکار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75696" target="_blank">📅 18:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDRGCKBIqmc2T2oioMB3-BuUTyTlQgUhk8iIq23XsY_5qsDegB76Yw_Jn9sKfGyLLF2GiuaxzfziFjYIKmDUpTqMFBJz30dHlzUf2Qr2uSqBS6if84Gln75hajjv7wAnhxrv27h4AaPCD-00raG2DU6LHOYm2zH8m1wbZqid1JOZQsEFpTddFzXyfv13gELUD33pKDJRWYqq3zGBTbgTtFnp3vorEtks1LoZaJaO9FrfMm7ZlUuwRlag2cZr7g8lJ-gM3peaAXOA3S05qhazGb9B2RQROZqKD0P5h8iTzSX91328zwRflRvvulMGZhcH5oDhOkC6sic-YdXjdgTcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایالات متحده، روز دوشنبه چهارم خرداد گفت که واشینگتن در مذاکرات جاری خود با ایران، «هر فرصتی برای موفقیت» به دیپلماسی خواهد داد.
مارکو روبیو که اکنون در هند به‌سر می‌برد در جمع خبرنگاران گفت که مذاکرات با ایران همچنان «در حال پیشرفت» است و خوش‌بینی محتاطانه‌ای نسبت به توافق احتمالی برای بازگشایی مسیرهای کلیدی کشتیرانی و از سرگیری مذاکرات هسته‌ای ابراز کرد.
او که روز گذشته از احتمال توافق با ایران تا پایان روز یک‌شنبه خبر داده بود، گفت: «همه ما باید مطمئن باشیم که یا به یک توافق خوب خواهیم رسید، یا مجبور می‌شویم به شکل دیگری با این مسئله برخورد کنیم. ترجیح ما این است که یک توافق خوب داشته باشیم.»
دونالد ترامپ، رئیس‌جمهور آمریکا نیز شامگاه یک‌شنبه در دومین پیام خود درباره روند مذاکرات با ایران اطمینان داد که توافق احتمالی با ایران «خوب و درست» خواهد بود اما هیچ کس درباره محتوای آن اطلاع ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75695" target="_blank">📅 09:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky88I5LtU2cxKdTUlwahvcR0w9tLKVckGBwQi-fzmSlEk8Ab9YMaI2fYvsQKbiWNR1NsUbPeRIELYbiwZPEFRmzvTFeIMiX2zvwrsFzbSksvqM3uBqaCpl719VkrnVvq1Q5O5dtVrh-As85SQXqe_ndIBv7zcrSLOTxSzn35vyAWjuZkvy25oRhOXmGtlxipefiJnnvudMDoEj0yA86bfaClaUK7m1VLB-PzqCwCAaUs5cHm0RuWEhq4La6ozvnTdns98ZRpObzBiIuoUHy9gdFgy3fsKUdraWigbAg3HFh9uzOl0XswFzSpSkB6LEDAUOR6fOBeHlN9gkZ2EcRBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم اعدام «عباس اکبری فیض‌آبادی»، از متهمان پرونده اعتراضات دی‌۱۴۰۴ در شهرستان «نایین» اصفهان، صبح روز دوشنبه ۴خرداد۱۴۰۵ اجرا شده است.
«میزان» مدعی شده که عباس اکبری از «لیدرهای مسلح» اعتراضات در نایین بوده و در جریان حمله به فرمانداری این شهر و برخی مراکز حکومتی، به سوی ماموران امنیتی تیراندازی کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75694" target="_blank">📅 09:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scyt2bzi2cgKMxyNg_wthPL6-qrZ0oYXwM3Wg3zg4mC-ioZtmhsO_4MHtSTFvK7ycSOZtGuNi_HNMZwGIP5GtkRw4N6D1I-vOxWaDxgg4Etj1yHEj8_b_7Vsu0bRu6N5qtz9G1mi2MWdI0g57SJTF3M3e-hT84E216TAIFztVniJwd6DmAuX3jpWGfHZ6AWQ--wditsRHpsxt2h5mfd0qYSugSfm7pmJG9Tmixo-AM3vKxiTB4wKTsrEvpGXm_OCjbMYsOwpXDTtUYtgP-JCQdlq2qDoxS0Tb31BtybBjKjAsvzpmJLE246rR_xgAvkuvK8KxUAgZdLpO2nuFV7lmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: مجتبی خامنه‌ای در مکانی نامعلوم با دسترسی کم به دنیای خارج پنهان شده است.
ترجمه ماشین:
اطلاعات نهادهای امنیتی آمریکا نشان می‌دهد که رهبر عالی ایران عملاً در مکانی نامعلوم پنهان شده، دسترسی محدودی به جهان خارج دارد و ارتباط با او تنها از طریق شبکه‌ای پیچیده از پیک‌ها امکان‌پذیر است؛ این را مقام‌های آمریکایی آگاه از موضوع گفته‌اند.
به گفته این منابع، مقام‌های ایرانی که مجوز همکاری با دولت ترامپ را دارند، برای برقراری ارتباط در داخل ساختار حکومتی خودشان با دشواری روبه‌رو بوده‌اند؛ مسئله‌ای که یکی از دلایل اصلی تأخیر در روشن شدن جزئیات توافق احتمالی با ایران و توافق‌های قبلی بوده است.
دو مقام آمریکایی گفتند وقتی آمریکا جزئیات پیشنهادی را ارسال می‌کند، دشواری دسترسی به رهبر عالی باعث می‌شود گاهی پیش از دریافت پاسخ از سوی آمریکا، تأخیری طولانی رخ دهد.
سخنگوی کاخ سفید از اظهارنظر درباره اطلاعات مربوط به محل حضور رهبر عالی یا روش‌های ارتباطی ایران خودداری کرد.
یک مقام ارشد دولت روز یکشنبه گفت رهبر عالی با چارچوب کلی پیش‌نویس توافق فعلی موافقت کرده و دونالد ترامپ، رئیس‌جمهوری آمریکا، در تروث‌سوشال نوشت که انتظار دارد ظرف چند روز آینده پاسخ نهایی اعلام شود.
مجتبی خامنه‌ای، رهبر عالی ایران، که در حملات آمریکا و اسرائیل در عملیات «خشم حماسی» زخمی شده بود، برای جلوگیری از حملاتی مشابه حملاتی که به کشته شدن پدرش، آیت‌الله علی خامنه‌ای، منجر شد، تدابیر بسیار شدیدی اتخاذ کرده است. علی خامنه‌ای از سال ۱۹۸۹ تا ۲۸ فوریه بر ایران حکومت می‌کرد. مجتبی خامنه‌ای از پیش از آغاز جنگ تاکنون به‌طور رسمی در انظار عمومی دیده یا شنیده نشده است.
یکی از مقام‌ها گفت اطلاعات به‌دست‌آمده توسط نهادهای اطلاعاتی آمریکا و اسرائیل از داخل حکومت ایران، امکان شناسایی و حذف بخش بزرگی از رهبری ارشد ایران در جریان جنگ را فراهم کرده است.
منابع گفتند در حال حاضر بیشتر رهبران ایران نور روز را نمی‌بینند، هفته‌ها در پناهگاه‌های به‌شدت مستحکم می‌مانند و جز در موارد کاملاً ضروری از صحبت با یکدیگر خودداری می‌کنند.
یکی از مقام‌ها گفت: «تماشای تلاش آن‌ها برای فهمیدن این‌که چطور با هم حرف بزنند، تقریباً مثل تماشای یک سیتکام است. آن‌ها کاملاً به ستوه آمده‌اند.»
شدیدترین تدابیر احتیاطی از سوی رهبر عالی اتخاذ شده است.
بر اساس طراحی این سازوکار، حتی مقام‌های عالی‌رتبه حکومت ایران هم نمی‌دانند او کجاست و هیچ راهی برای تماس مستقیم با او ندارند.
در عوض، پیام‌ها از طریق شبکه‌ای از پیک‌ها منتقل می‌شود که با هدف پنهان نگه داشتن محل حضور رهبر عالی ایجاد شده است.
یکی از مقام‌ها گفت: «به همین دلیل است که می‌بینید برخی می‌گویند: "رهبر عالی با چارچوب موافقت کرده" یا "منتظر پاسخ درباره نکات نهایی توافق هستیم." هر اطلاعاتی که به او می‌رسد، از پیش قدیمی شده و پاسخ‌های او با تأخیر زیادی همراه است.»
رهبر عالی در قالب کلیات با زیردستان خود ارتباط برقرار کرده و به آن‌ها جهت داده است که درباره چه موضوعاتی می‌توانند مذاکره کنند و چه موضوعاتی نباید مطرح شود.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75693" target="_blank">📅 03:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yd4b0zAjQO7yf8wm-BQzf9dJc_0mq1PSmpkgyG8_Kt6xmC-uxx0KoVCiW9hcHw4OSZlOzK1kmPiR8ArPIH6lvaXVnKCQNdywP_cFYNy6wqkwM7aNW8IaXVLIbj4mYz_9vSRCv6m2NcCKVX-HMlOjYJnGxyZP-h3a_EZTUUix5-PuM6ZHBr3YvTM6sckWZXP9ZwOQZCGoYmhXVjaRIYLAGE0_uerHwB5TuQlePxViXdo2jf9DfoCKi32URxubKZHWXG4LcaJ5a7kmHzGe0q8vw9THxc6eFmZwB2zUinEAGFIrx7eQnIjTnnEeEeTPYzDtr3D5vzMKHKuQ1z_j6OqJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I2JdVn_hv-_S43tJVxHG4lb4UxXT_JQKXGEt4ux2svaw9G8u13Lev3Vmus_rxu3IhfirKPtZdewHIUZhDLswgnBqmac_Os19IY0WuOPPVufi1XuZP6iiJHutE5JL_F4QPpVeGdmwcbbAlxAn0BvzoeowmieD5_jldLAbHB81BuapCna1vcHA0j2h7OT5BiLZiHjndtI6Ofh0HQ5ZnjxohVeVdkupySSVB1o8N0JcIZ9v-N77isBj9WLzwah0Ts_na06EeycbqiQBVMemiX2_f2xEYKMLH6kO2LFJ2AGpiKkyaXYGNZVCrdFpCBPAbVGvvbd6LO7qj99Xr5ULc_UzKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با شبکه «فاکس‌نیوز» اعلام کرد که واشنگتن هنوز به توافق نهایی با تهران دست نیافته است و هیچ توافقی امروز یا فردا امضا نخواهد شد؛ این مقام مسئول با تاکید بر این‌که آمریکا تسلیم خواسته‌های طرف مقابل نخواهد شد، افزود که تمایل و تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، این است که یک فرصت ۵ تا ۷ روزه دیگر به مذاکره‌کنندگان بدهد تا توافق را به مرحله نهایی برسانند.
بر اساس این گزارش، یک توافق چارچوبی با ایران تا روز یکشنبه تا ۹۵ درصد پیشرفت داشته است و اگرچه دو طرف بر سر کلیات مربوط به ذخایر هسته‌ای تهران و بازگشایی تنگه هرمز به توافق رسیده‌اند، اما چانه‌زنی مذاکره‌کنندگان بر سر جزئیات و «ادبیات دقیق» متن این تفاهم‌نامه همچنان ادامه دارد.
@
VahidOOnLine
تسنیم، خبرگزاری وابسته به سپاه پاسداران، روز یکشنبه به نقل از «یک مقام مطلع» گزارش داد: «هیچگونه خوش‌بینی به آمریکا ندارد و رد و بدل پیامها از طریق میانجی پاکستانی نیز دائماً با در نظر گرفتن بدبینی به دولت آمریکا صورت می‌گیرد».
تسنیم به نقل از این منبع در ادامه نوشت: «تا این لحظه تفاهم نهایی حاصل نشده و چالش در بعضی بندها ادامه دارد، اما حتی اگر تفاهم اولیه‌ای نیز صورت بگیرد، به معنای تغییر نگاه ایران به آمریکا و اطمینان از اجرای تعهدات این دولت نیست. آمریکایی‌ها سابقه بسیار بدی در مذاکرات دارند که بدبینی ها را تقویت و تثبیت می‌کند. پس حتی اگر تفاهمی نیز صورت بگیرد ایران در طول روند پس از اعلام تفاهم، اقدامات آمریکا را زیر نظر خواهد گرفت و در صورتی که آمریکا در آن مرحله نقض عهد کند، ایران اهرم‌های خود برای مواجهه با آن را حفظ خواهد کرد».
تسنیم پیش از این نیز از «کارشکنی‌های آمریکا» در بندهای تفاهم از جمله در آزادسازی اموال بلوکه شده ایران گزارش داده و نوشته بود: «همچنان امکان منتفی شدن تفاهم وجود دارد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75691" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mnadlp-glmC76PS6Q7ZyeW1Vkb7YQuJnMS3jta5THLEToktRYLkOQ_2YPQhHlNKChtBhbaoxfOcKC3zDSvl1jeJiZJsH8kw8svgF0X0_C8AB6b9od2qDwQEYWp8S6Z1HD65I6krwiJBAjnQvwzj4b0jLuKHeAD9CcdoWkqt3lgZ2yiITSsfa4aKkvifCVn5zVY8hk-3KDsxajVErNl5__qA7ap8W2XlzC5oBlI9ktwcmDgNtF4nIZAyB_75AT_MDJ7FJMY8XQWlv4-e-aqKxa8XLXvKe5XhOZgwZuok2c9ip4eoPymcbEKIOyB6zxgGM70HBsTsdw9t8G_Z7kNsMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری حکومتی تسنیم، شامگاه یکشنبه سوم خرداد ماه، به نقل از دادگاه انقلاب تهران اعلام کرد، رای اولیه پرونده موسوم به «بچه‌های اکباتان» صادر شده و طی آن چهار نفر از «متهمان اصلی» به اتهام «افساد فی‌الارض» به اعدام محکوم شده‌اند.
به گزارش تسنیم،  اتهامات ۹ نفر از متهمان این پرونده که به دلیل کشته شدن «آرمان علی‌وردی» بسیجی حامی حکومت زندانی شده‌اند مواردی چون  «وارد کردن ضربات چاقو،اخلال در نظم عمومی، اخلال گسترده در امنیت کشور، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور، توزیع کوکتل مولوتف، وارد کردن ضربات سنگ به آرمان علی وردی، ضرب و شتم آرمان علی‌وردی و فعالیت تبلیغی علیه نظام» عنوان شده است.
بر اساس این گزارش، دادگاه انقلاب تهران متهمان ردیف اول تا چهارم پرونده را به اتهام «افساد فی‌الارض» به اعدام محکوم کرد و متهمان ردیف پنجم تا نهم نیز به حبس از یک تا پنج سال و مجازات‌های تکمیلی محکوم شدند.
@
VahidOOnLine
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی چهار تن از متهمان پرونده «شهرک اکباتان» را به اتهام «افسادفی‌الارض» به اعدام محکوم کرد؛ این در حالی است که دادگاه کیفری پیش‌تر اعلام کرده بود انتساب قتل به متهمان به‌صورت قطعی ثابت نشده و امکان صدور حکم قصاص وجود ندارد.
خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، روز یکشنبه در گزارشی تلاش کرد صدور این حکم را توجیه کند.
بر اساس این گزارش، رسیدگی به پرونده در دو مرجع موازی انجام شده؛ دادگاه کیفری به اتهام قتل رسیدگی کرد و دادگاه انقلاب به اتهامات امنیتی از جمله افساد فی‌الارض.
میزان مدعی شد که پس از آن‌که کمیسیون پزشکی قانونی و اداره آگاهی هر دو اعلام کردند تعیین فرد وارد کننده ضربه مرگبار به آرمان علی‌وردی ممکن نیست، دادگاه کیفری سه تن از متهمان را از اتهام مشارکت در قتل تبرئه و سه تن دیگر را به پرداخت دیه و حبس محکوم کرد. اما در مسیر موازی، دادگاه انقلاب همان متهمان را به اتهام افساد فی‌الارض به اعدام محکوم کرد.
به گزارش خبرگزاری هرانا، میلاد آرمون، نوید نجاران، مهدی ایمانی و سید محمدمهدی حسینی چهار نفری هستند که حکم اعدام برای آن‌ها صادر شده است.
چهار متهم دیگر این پرونده یعنی امیرمحمد خوش‌اقبال، علیرضا برمرزپورناک، علیرضا کفایی و حسین نعمتی نیز هر کدام به پنج سال زندان، دو سال حبس به اتهام تبلیغ علیه نظام، دو سال منع فعالیت در فضای مجازی و دو سال منع اسکان در تهران و البرز محکوم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75690" target="_blank">📅 00:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbsMZTNV4isyCBR8zHIYlnKecivhE_BTtg56dc2QZlduasRKw9m1a-wV4qgods6cg0NUohGFbdTj9j6L4q3wG7WdoI2kxmbVc8hm4cELepWWUXvNgjFgwYngg_XlWmWfjNj3FBkgF1DLjw_BFVO5dfyrtbRF-mVHlXN0rXNHgSOXNbQYGVhpRK_wi5Sck6uHMx9P7ARJzMXZMDstjKBg8roxqm3TORnYxJwa0AYtDaR_sSMSRldQC7Xat-qI0dHuEW_HEqlVMOUtx04FrxUELPWD_ogqn6mPHr5Zw8JvqYz9YRTVS-_g39-pTnwm8dn3NMi5S_OADbkHtmG4zBB_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ
روی تصویر بمب نوشته: از توجه شما به این موضوع سپاسگزارم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75689" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWUJEfawyVqrFLxIA5rsIt-kNrcQTmMv63u3rhthX6DIqnB-i5eDPhnPOg8eJMD_sgS2r15eFR7njH6j78V0sCIV5xvTRs6gdHRRWZSrJ4JpaUeI8aEI-8yto8htIlnGF3DtLOLSY41syqr8edVLbHLL3BIaz5eNN4jzIraKqf6nAPfhw5YVrPl9TmdzTEuWNlOLrhgwrs8lhD3TspNdMMXOgvkKP6WRC9HKnSVARiL7iXrXGLAv1lJrkHpg7n-G8EnIViGC2n_UnBF2FfNWIuXTF0yCi8Ae7Dbi-2OpaMkjWdHH9gqQENX1HwPEc5r-unbUTqTW91JjdCr6UWB35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در گفت‌وگویی کوتاه با نیویورک تایمز گفت: «ما موضوع را به بعد موکول نمی‌کنیم. مذاکرات هسته‌ای مسائل بسیار فنی هستند. شما نمی‌توانید یک موضوع هسته‌ای را در ۷۲ ساعت و روی یک دستمال کاغذی حل کنید.»
او افزود: «در حال حاضر، هفت یا هشت کشور منطقه از این رویکرد حمایت می‌کنند و ما آماده‌ایم این مسیر را ادامه دهیم.»
این در حالی است که آقای روبیو ساعاتی پیش گفته بود که ممکن است تا شامگاه یک‌شنبه خبری دربارهٔ توافقی با ایران اعلام شود که می‌تواند به‌طور رسمی به جنگ خاورمیانه پایان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75688" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AFv_3SGTLFVLyYxX9J0D_Joo-DSITy2JS3IK6kbcctQ3GMh1XtyhmwPKXgY3tCeZ_UQSmDJg3sJ1DnYcuOKr14cxsuGiu8VwPf71qdVue5lmZszOrnO75-cH7GMC4_l1_jJ-2n6Fuo3A-OYaO4lcXuNnZFU9jslvV8jk8TyyDJi4MBPydmuATWMpQ5inNlohpekqO0pu1KePGGATNw-9ceB7DzkJQc4CfaZD4M1bB33J5mtvFCKks1JnJQUHsr8qAXyNGwWpiNI-vTsxaB_he5QLTT78kxKNZLoF1yCiYIjr1QhKZKHlfXvtEpvD1Hm-BI_-IfjJrOXkycxNr7St-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر توافق کنم توافقی خوب خواهد بود
ترجمه ماشین:
اگر با ایران توافقی انجام بدهم، توافقی خوب و درست خواهد بود؛ نه مثل توافقی که اوباما انجام داد و مبالغ عظیمی پول نقد به ایران داد و مسیری روشن و باز به سوی سلاح هسته‌ای پیش پای ایران گذاشت.
توافق ما دقیقا برعکس آن است، اما هیچ‌کس آن را ندیده و نمی‌داند چیست.
حتی هنوز به‌طور کامل هم مذاکره و نهایی نشده است.
بنابراین به بازنده‌هایی که درباره چیزی انتقاد می‌کنند که هیچ اطلاعی از آن ندارند گوش نکنید.
برخلاف کسانی که پیش از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد انجام نمی‌دهم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75687" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOgEWLkCO2yYrQSw_961yW__WO2eEkK_KnQq-ybgQzKaNHguy8xZ2rqe7Drmds5wMpv6rroREnscos8AuACqG5pYeRD6VAqM1sH9eHPA7NdcGiM6obZjAcJhKLC9QXq84KaG5FX3LwyasC59T6XEgWbsNBwdD-TcV7S-UelEkZBG3f1h0WrFKpoyVsAAEgdCo0tHU5SNLOoNhw28PjGhnbhQkIlQPw4ZnpuqRPrsRCf-0htiYMwp0i3ofZIWjv5B_cnqcCw73BepdNdnRvf82T8vKOssjBC0rUwCgOLt9-oj50c6h-hdUlTb3WwrYHZekwXP0ySjAd-WoRjzWuU7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آکسیوس، روز یکشنبه سوم خرداد ماه، به نقل از یک مقام ارشد دولت دونالد ترامپ گزارش داد، «چند مورد جزئیات حل‌نشده» میان تهران و واشنگتن باقی‌مانده است و به همین دلیل توافق میان ایران و آمریکا احتمالا امروز امضا نخواهد شد.
این مقام آمریکایی به آکسیوس گفت هنوز بر سر برخی بخش‌های توافق «رفت‌وبرگشت» وجود دارد و اختلاف‌ها بیشتر بر سر عباراتی است که برای هر یک از دو طرف اهمیت دارد: «برخی کلمات برای ما مهم هستند و برخی کلمات برای آن‌ها.»
آکسیوس به نقل از این مقام ارشد کاخ سفید نوشت، ساختار تصمیم‌گیری در جمهوری اسلامی «سریع عمل نمی‌کند» و روند دریافت همه تاییدیه‌های لازم چند روز زمان خواهد برد.
به گفته این مقام، ارزیابی واشنگتن این است که «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، چارچوب کلی توافق را تایید کرده، اما اینکه این روند به توافق نهایی منجر شود، «همچنان یک سوال باز» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75686" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiBRZhMdzcXXYAN_YbKHcaeYNaZlMPOqNYdQwgmyrPAVV5xwVtMc3aA6wFTNMzIYccUcA7XyuzWT_uYRvSjRTcvRPhXyHu4W957XqXHL4Ee29mSRnbEizfoPYOOrrbXUWAt-e9Rv58xsW9dwB7pfT8wrv_xbJNXZ4PxN-h6nH-wnk36VxPZuxxLMpCA9_uJfRgFuu0HlFW_Re64IU5T53IpL2q937lmaKEuYg--6-AbjeDRlDKOSZneqOrJD8c8YRB6cG4pS4-QlpD25a9ki6MKGksFvjhpq-ZhAoKqV-HLiiT_4h4-4iGz2nqWg_Q6KNa0dyDkDiYoiZeCZNGA8fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او و دونالد ترامپ توافق دارند هرگونه توافق نهایی با جمهوری اسلامی باید به‌طور کامل تهدید هسته‌ای را برطرف کند.
او گفت این به معنای برچیدن تاسیسات غنی‌سازی ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک این کشور است.
نتانیاهو افزود ترامپ بار دیگر بر حق اسرائیل برای دفاع از خود در برابر تهدیدها در همه جبهه‌ها، از جمله لبنان، تاکید کرده است.
او همچنین گفت سیاست او، همانند سیاست ترامپ، همچنان ثابت است؛ ایران نباید به سلاح هسته‌ای دست یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75685" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7LW8eqYIIBGQw_J6r75yS4kkq2RziombU_NqwL-bRXCacd1Nzy0j9mBiXCUkSvktpAp20p5rpXECAazBoPIPFG-0VXwhr-V2VGXLCk6A9B7fS6pcrULpjmBSCF_gYsqwkkYDKAB0T30QIRoGEPh9K8XnO0CXDcBW0zxMx-69myJefEkAwONZF-jWhySXQAWckUos3AJj7CUcg9-WkrJeNeLsaMJwQvDy6ATv4bFfYC3W5xm0vepbguH1h1iibGwaKUhcVy0UzqJ7zd6TZfqIicN4flclP6DyLHpnKoYoK51v7prwbzW8VEXi8XHVIRXS6DNGaG346Nw0286-wvZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ سخنان پزشکیان را نشان داد: آماده‌ایم به جهان اطمینان بدهیم
ترامپ اسکرین‌شاتی از
توییت
خبرنگار فاکس‌نیوز رو پست کرده که نوشته بود:
مسعود پزشکیان، رئیس‌جمهور ایران: ما آماده‌ایم به جهان اطمینان بدهیم که به‌دنبال سلاح هسته‌ای نیستیم. ما به‌دنبال بی‌ثباتی در منطقه نیستیم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/75684" target="_blank">📅 18:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEsme2KS3OnGY8vps49i2hHpoH_0Ei5nDtQmJlo7NgJkO3Rx6V-3AFC6EwrCX7ChFSdp9RetPiVok3lTrYM8CfW5uSHRqiOENlfRv10O-F_nWoQqtKdszMBAmaiG6ynCNfsZZprllIi3ZaYF_4I8RWDGValh5-JUK661oV8teFkirC64RT--8UnWLvln73yTYzWYJoKE5EewRGkJfPfPF3u2TxRQz-ccrc8pXXIQKeblCE5m8XGYKXTcIjT0Og0FEM8uMW7S7RESaERJYrev63bQMEOIxHcUjMwdWPjx7LqQ6lQx4v7kjW4gXpc4ZqaoXWH2I1Ruzi3nsX29WQLHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود؛ توافقی که باراک حسین اوباما و افراد کاملاً ناشیِ دولت اوباما آن را مطرح کردند و به امضا رساندند. این توافق، مسیری مستقیم برای دستیابی ایران به سلاح هسته‌ای بود. اما درباره معامله‌ای که اکنون دولت ترامپ با ایران در حال مذاکره بر سر آن است، چنین نیست؛ در واقع کاملاً برعکس است!
مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگانم اطلاع داده‌ام که برای رسیدن به توافق عجله نکنند، زیرا زمان به سود ماست. محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت برقرار خواهد ماند. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی نباید رخ دهد!
رابطه ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و ثمربخش‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای تولید یا تهیه کنند. مایلم تا این مرحله از همه کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر کنم؛ حمایتی که با پیوستن آنها به کشورهای عضو توافق‌های تاریخی ابراهیم، بیش از پیش تقویت و گسترش خواهد یافت و چه کسی می‌داند، شاید جمهوری اسلامی ایران هم بخواهد به آن بپیوندد!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75683" target="_blank">📅 18:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IjDctJwey62sljIw3BdSpoJ4H8Q213jZXrOEi-kxkHSSLsOGGAVCIvni5A2XnHth16Cl_odFcMfIgKLCEYBN5-53JRCdiMNdBknW39lY4sqRIrGjPhSQHj6MrDEorEiGBeAhvgkrspmsUGJWKkzJeOwQuCVj3M-x3sI1lGE0a5yj2v2pFguzBOU07TRyG0iNmwy0v3ABBl1hojl9BhMzUY6Va9psBhbVhlFtDHqS_yjk9TPB7fZGyRf4yKlWXISi5l_Cbst1cfm8Nvje27xPD7MU0wNI2AE89pqqEiD5tallh2WUEySk3LyCrhuQPAG58FvZwn5juV_rOuZSBWzYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته با هوش مصنوعی را در شبکه اجتماعی تروث سوشال
منتشر کرد
که انهدام یک قایق سپاه پاسداران  به دست پهپاد آمریکایی را نشان می‌دهد.
بر این تصویر، واژه «حداحافظ» به زبان اسپانیایی نوشته شده است.
این تصویر در حالی توسط رئیس جمهوری آمریکا منتشر می‌شود که رسانه‌ها در انتظار نهایی شدن توافق احتمالی تهران و واشنگتن برای پایان جنگ هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75682" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQRxm5mF8NL6oIDeKhCQO9ipc_C1rAHS3xP_gBrjpDuQyyjlgnZKJNHvIPCLuEsYD9qkheVbYIzKiwCcEDz3jrsNYJd_f7OMCCa869NSX-HJnMm1DaFpZwLGEG24AqHWEOn0WNDffdD3cvGwNLIKIYkPBGq26zRJYktdpC_eHB1Hln-5vECuUSxaeoz-ZvulHeenBTUJtVYpxgFBP9GCVr5NNZT_kFfHXAqbxDot5XI-3eoxd3GLbnFw_tmitGZiEe1SKDYjYz4xp4sr7e8Xwx5W6K_KtTFsPHTAZt0qo8tER8PqNtAXu6lVLzjfLrQTUqSUcthV1tzG_d5xEmbdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان گفت: «مدیران دولت تا زمانی که مباحث کارشناسی درباره مدیریت مصرف بنزین نهایی نشده است، حق اظهارنظر شخصی ندارند.»
او افزود: «اگر کسی از این دستور تخطی کند با او برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی حاصل شود.»
او ادامه داد: «مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.»
@
VahidOOnLine
این دستور در شرایطی صادر شده که شایعات درباره افزایش قیمت بنزین، تغییر سهمیه‌ها و تشدید سیاست‌های مدیریت مصرف بالا گرفته است.
همزمان، ناترازی بنزین و فاصله میان مصرف داخلی و توان تأمین سوخت، نگرانی‌ها درباره کمبود احتمالی یا فشار بیشتر بر شبکه توزیع را افزایش داده است.
عارف گفت دولت تلاش می‌کند تصمیم‌ها به‌گونه‌ای اتخاذ شود که معیشت مردم آسیب نبیند، اما واقعیات اقتصادی کشور و تحولات اخیر نیز باید در نظر گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75681" target="_blank">📅 18:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IpXONBxvYfNuL8V1QtLhwhBDtfVRPFnT2rJ8bZljxvWjPpVnT0LTRuIJT6X8t2UsVYwX-B3Kab4drmI60qjHiEbNv9TgoSJSPpSBZ5pFMJVeBS79h9UsG-V1z_ida_kpSNHaZpfT-3l-VxrH6M-S-8pF4N35fd6BFQK6SOATtGDp8hQdM9UDiM_bodn949B8JZfDUpw_aZki3c2akkFPisNeojQJKIXrRliBdnlRpUfaJVjFX5UqRevDr_PxBvXihWJJrDdjNrP60bpjcTOV1Q6XXCDAD66POu_OXoh5Iyx1hRKbKabJDcG9JK8X9G4mGaTMyHO-GRLlxiAnL0Aa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F5gfdNJittiErEvSKmodnbuHSwlCPMws8MbTIQuFrJ7bBjAKh1zXdgdiyCXj0wDNmpapVsQSuOMswA_gIyiUdybwoQ7BhEW3Ol6rbI6GgzK-XdFFEFE_b3CvA2rsT75IM_Kc7KNBl2TROOQMB-tKK6DpQq3Cb3qyDcH_bJRS3J2rrykz2UNK5mFpKwhL2iDGLcjYAxN--M0vS7Y4vJcGD84evLOEM-JAfItBPBEeadW16gL9hE0ILh_ip_TuwbcXLdm0f7CMiFnpD0FbaKE0iQ1TmnhWR8WBvVtNygv2LLxZpZXvtloFpm1ZSpjeuoE61iFUQBnQ-PPh75A_dw-oxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران روز یکشنبه سوم خرداد با اشاره به توافق احتمالی میان جمهوری اسلامی و آمریکا، نوشت:  در پیش‌نویس توافق احتمالی ایران و آمریکا هیچ بندی درباره «تعهدات هسته‌ای ایران گنجانده نشده و تمام مسائل مرتبط با برنامه هسته‌ای به مذاکرات ۶۰ روزه پس‌از امضای توافق موکول شده است.»
فارس در ادامه تاکید کرده است که «ایران در این توافق هیچ تعهدی برای واگذاری ذخایر هسته‌ای، خروج تجهیزات، تعطیلی تأسیسات یا حتی تعهد به نساختن بمب هسته‌ای وجود ندارد.»
این در حالیست که نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت که شنیده‌ها از جزییات تفاهم اولیه «احتمالی»، حاکی است که واشینگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط درآورد و جمهوری اسلامی در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است.
این گزارش افزود در صورتی که این تفاهم‌نامه مورد توافق قرار گیرد، بخشی از دارایی‌های بلوکه شده حکومت ایران باید در گام اول آزاد شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/75679" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZMq_COEJ86_ziAUoOHJpoAlDNT2HeHbV6otJ1H6L2N-kuQrLLaaAmq5v0m038M5jw0Q6EkaWDPWPBwZn-zrAJjg9HRzaPcFOPTDF22Ojsx9lyJEgExgcUzoz2cwNZ_lVSuu1Ws9_J6Fq0Z3ldZBAn-wuTpANdt7RI3e9_0Xtlci6LPwggF2qDNhKu9_JZLOVyMvy73gCdeVb2ohRNtLg6pb9lz0bKECXVb8LF9dH6yDKa3vC_PqKis5fR-beHfPoCb2Kkf-OOrjmLIjn7vXK_O0lRrHqLGbo6pZ9l5AMXe89RayVFfw6K_289NotAn2tR9LaaWols7-Q2iaxAcubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=eV6StcP1szRrD8tEeg7R-U7anYRelOEQz7C7d4c-VhrEAHnDv9FL2dTZbEniJgpuETrRrjwnHCdkO0LJkzOMP58iW7Z_2JEjS5Q44EXD2csarTf3B71z4SoLWBT2-uBRUlPffVaB83nYJ-0YFQKXgKVhZ6-DjErH8CLG96z3ow4OucO0dtpMwgLypd0P4HMBouwJ1rLXs9l0BrRHln_FI3YpFoDPYggYd2a7WYs_LANSDinFGDUDWrMRjiVEzZWbVDbQ4Ry_oFXDEecPdrCEUf01s-TbAjgxl_fzi4lSyVH0YsDjPw6D2JTshbvRw1A_pFQ8VBbXEw1hgOq6AqAsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=eV6StcP1szRrD8tEeg7R-U7anYRelOEQz7C7d4c-VhrEAHnDv9FL2dTZbEniJgpuETrRrjwnHCdkO0LJkzOMP58iW7Z_2JEjS5Q44EXD2csarTf3B71z4SoLWBT2-uBRUlPffVaB83nYJ-0YFQKXgKVhZ6-DjErH8CLG96z3ow4OucO0dtpMwgLypd0P4HMBouwJ1rLXs9l0BrRHln_FI3YpFoDPYggYd2a7WYs_LANSDinFGDUDWrMRjiVEzZWbVDbQ4Ry_oFXDEecPdrCEUf01s-TbAjgxl_fzi4lSyVH0YsDjPw6D2JTshbvRw1A_pFQ8VBbXEw1hgOq6AqAsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه در جریان نشست خبری مشترک با سابرامانیام جایشانکار، وزیر خارجه هند، در دهلی‌نو اعلام کرد که طی ۴۸ ساعت گذشته «پیشرفت قابل‌توجهی» در مذاکرات و رایزنی‌های مرتبط با بحران تنگه هرمز و پرونده ایران حاصل شده و احتمال دارد تا ساعاتی دیگر اخبار مهم‌تری در این زمینه منتشر شود.
او بدون ارائه جزئیات کامل، گفت هنوز توافق نهایی شکل نگرفته اما مسیر مذاکرات نسبت به روزهای گذشته امیدوارکننده‌تر شده است.
روبیو با تاکید بر اینکه دولت آمریکا همچنان راه‌حل دیپلماتیک را ترجیح می‌دهد، اظهار داشت دونالد ترامپ تمایل دارد بحران ایران از طریق وزارت خارجه و مذاکره حل شود، نه از مسیر درگیری نظامی.
با این حال او هشدار داد که واشنگتن در هر شرایطی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و این موضوع «خط قرمز» دولت آمریکاست.
به گفته او، رئیس‌جمهوری آمریکا بارها تاکید کرده که ایران هرگز نباید به توانایی ساخت سلاح هسته‌ای برسد و دولت ترامپ در این زمینه از همه دولت‌های پیشین آمریکا سخت‌گیرتر عمل کرده است.
وزیر خارجه آمریکا در بخش دیگری از سخنانش به وضعیت تنگه هرمز پرداخت و گفت این آبراه، یک مسیر بین‌المللی است و هیچ کشوری حق ندارد عبور و مرور آزاد کشتی‌های تجاری را تهدید کند. او اقدامات اخیر ایران در قبال کشتی‌های عبوری را مغایر قوانین بین‌المللی دانست و هشدار داد اگر جامعه جهانی در برابر چنین اقداماتی سکوت کند، یک «وضعیت خطرناک و غیرقابل‌قبول» به رویه‌ای عادی در جهان تبدیل خواهد شد، موضوعی که می‌تواند در مناطق دیگر دنیا نیز تکرار شود.
روبیو همچنین اعلام کرد آمریکا طی دو روز گذشته همراه با شرکای خود در منطقه خلیج فارس روی چارچوبی کار کرده که هدف آن باز نگه داشتن کامل تنگه هرمز، جلوگیری از اخذ عوارض یا محدودیت برای عبور کشتی‌ها و همچنین رسیدگی به نگرانی‌های مرتبط با برنامه هسته‌ای ایران است.
او توضیح داد که در صورت موفقیت این روند، نه‌تنها امنیت کشتیرانی و تجارت جهانی حفظ خواهد شد، بلکه نگرانی‌ها درباره برنامه هسته‌ای ایران نیز تا حد زیادی کاهش پیدا می‌کند.
روبیو در ادامه گفت هرگونه توافق احتمالی نیازمند پذیرش کامل ایران و اجرای عملی تعهدات خواهد بود و مذاکرات درباره جزئیات فنی برنامه هسته‌ای، روندی پیچیده و زمان‌بر دارد.
او افزود هنوز نمی‌توان درباره موفقیت نهایی مذاکرات با قطعیت صحبت کرد، اما «نشانه‌هایی از پیشرفت واقعی» دیده می‌شود و ممکن است جهان در ساعات آینده خبرهای مثبتی درباره تنگه هرمز و روند مذاکرات دریافت کند.
@
VahidOOnLine
روبیو گفت: «هدف نهایی این است که ایران هرگز نتواند به سلاح هسته‌ای دست یابد. ایران هرگز نباید مالک سلاح هسته‌ای شود.»
او تاکید کرد دونالد ترامپ، رئیس‌جمهوری آمریکا، در این زمینه موضعی «کاملا روشن» داشته و گفته است ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
وزیر خارجه آمریکا افزود: «قطعا تا زمانی که دونالد ترامپ رئیس‌جمهور است، این اتفاق نخواهد افتاد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75676" target="_blank">📅 18:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lJqQcCLCco2df0zRCxQTfkqPahD1JAMKv4xfa1lQdn1k7_unSRJPtlvFiBvAEuhhf-oQHBhHTILBcLuqxvT8oEZ8byGGi-LlpQPepv-DE6cOapnzr7_IDQaz6aOhNvNxPUX9yJiWNV2lA5-lhCj93pQxkbI3atgaz2T7jQpXIXjYLN97xDB2n-vjuGTEyTK-ujebmwjAoh9ek-D1qwh4r-qTHlAFmTEe2-WgSCP26QgTi48pt8g9SNRO_MQj54JqZzQaZGdgcJ9Q1QPInXEIG28Jer0fk-P2ZQcM_6jM1TVRVC7pjKBaDa4VstXF6Ixm5eLbpBVewmZvqyTIqtks4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد سرافراز، رئیس پیشین سازمان صداوسیما و عضو کنونی شورای عالی فضای مجازی، می‌گوید بخشی از حاکمیت ایران با الهام از الگوی چین به‌دنبال محدود کردن اینترنت جهانی برای عموم مردم و ارائهٔ آن فقط به گروهی خاص و کنترل‌شده است.
او روز یک‌شنبه سوم خرداد در گفت‌وگو با روزنامه اینترنتی فراز گفت جمهوری اسلامی تجهیزات لازم برای «قطع دائمی اینترنت» را از چین خریداری و وارد کرده است.
محمد سرافراز توضیح داد که در چین اینترنت جهانی برای عموم مردم قطع است و فقط به‌صورت محدود در اختیار گروه‌هایی خاص قرار می‌گیرد. سرافراز با اشاره به الگویی که آن را «سامانه نیکان» در چین خواند، گفت هدف چنین سازوکاری این است که «روایت حکومت» بر کشور حاکم باشد.
او همچنین اپراتورهای عضو شورای عالی فضای مجازی را از عوامل پشت پردهٔ تصویب طرح موسوم به «اینترنت پرو» دانست و گفت ذی‌نفعان قطع اینترنت «یک روز فیلترشکن می‌فروشند و یک روز اینترنت پرو».
@
VahidHeadline
پس از ۲۰۴۰ ساعت قطعی اینترنت در ایران، نت‌بلاکس نوشت در حالی که دسترسی به اینترنت جهانی در طول مذاکرات صلح تا حد زیادی قطع است، کاربران منتخب در لیست سفید، تصویری مصنوعی از زندگی ایرانیان را به جهان خارج ارائه می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/75675" target="_blank">📅 17:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=QRkTIt8HCZIFT9lPZ_299tBN0RKDi0x7CSX_53fgE24mOkglSesIPwQMHp_rf4ocx7oSkZet9a-5HnVYyU3tp2qDfcFM1ahRUeiufAJafMIpmcuOXFJAy6Ud8NAPtLgou9x_-O2y1DZv7ewN2nOzy3o6CDClMngrlGvEqtnSrmP6c9QtuAc_ezRWykBFHx2_zL7vL-kYriPqHcf_tafSnC5V8c0mezgarS_0w82stgUGVQezQ1hwqeK8mudssP1olX7Eotw8pJitCrmYDDnUJte4Vyv2F4MOJOpNAH55vgvZkTBGLnLp4nb9DVctLMhnVX6kxMv5KgLKH_toD5VDfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=QRkTIt8HCZIFT9lPZ_299tBN0RKDi0x7CSX_53fgE24mOkglSesIPwQMHp_rf4ocx7oSkZet9a-5HnVYyU3tp2qDfcFM1ahRUeiufAJafMIpmcuOXFJAy6Ud8NAPtLgou9x_-O2y1DZv7ewN2nOzy3o6CDClMngrlGvEqtnSrmP6c9QtuAc_ezRWykBFHx2_zL7vL-kYriPqHcf_tafSnC5V8c0mezgarS_0w82stgUGVQezQ1hwqeK8mudssP1olX7Eotw8pJitCrmYDDnUJte4Vyv2F4MOJOpNAH55vgvZkTBGLnLp4nb9DVctLMhnVX6kxMv5KgLKH_toD5VDfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری بزرگ در نزدیکی یک قطار که از گذرگاه چمن در شهر کویته در ایالت بلوچستان پاکستان عبور می‌کرد، تعداد زیادی کشته و ده‌ها نفر زخمی برجا گذاشت.
یک مقام ارشد پلیس بلوچستان و یکی از مسئولان این ایالت به محمد کاظم، خبرنگار بی‌بی‌سی اردو، گفت تاکنون کشته شدن ۲۰ نفر در این انفجار تأیید شده و دست‌کم ۷۰ نفر زخمی شده‌اند.
تصاویر منتشرشده پس از حادثه نشان می‌دهد که چندین خودرو در نزدیکی خط آهن آتش‌ گرفته‌اند و واگن‌های قطار نیز روی ریل واژگون شده‌اند.
گروه جدایی‌طلب «ارتش آزادیبخش بلوچ» مسئولیت این حمله را به عهده گرفته‌ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/75674" target="_blank">📅 17:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VRzNt9DuBbFHme40WkpEb5mnRbLon_-vpPIZL2mqDm662mPQREjrlBaCf70Fip13ToA_oEuOjWwg1jWJZsZMNKFctJqVNvE3B_UlX1zrFVShc8koG9NpO6xfkptjkdxBUWytetWzzSkCOctkL9Nzh92vKtOwwla4BX6A_Xootn918a63Y1zhZwFMR-YGzwm5uZY58ozr-zvd3Gl-DmViqWW1Cnsgxn2Bll6r_LvBdNFHud1qRqJ9rxqprtjOEcw04wTWOFoDi9vQwo9xdsgb3VDirUCmsVTgVgtc7adR5KU_RgH2NwMUbRGVF2mHNCvIKXBb9MOn4vOdRFzui6Zw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه جمهوری اسلامی، اعلام کرد مجتبی کیان به اتهام ارسال اطلاعات مراکز تولید صنایع دفاعی به «دشمن آمریکایی ـ صهیونیستی» اعدام شده است.
قوه قضائیه مدعی شده کیان در جریان آنچه مقام‌های جمهوری اسلامی «جنگ رمضان» می‌نامند، اطلاعات و مختصات واحدهای مرتبط با تولید قطعات صنایع دفاعی را از طریق پیام به شبکه‌های وابسته به اسرائیل و آمریکا ارسال کرده بود.
میزان مدعی شده بررسی‌های فنی نشان داده سه روز پس از ارسال این اطلاعات، محل مورد اشاره هدف حمله قرار گرفته و به‌طور کامل تخریب شده است. قوه قضائیه گفته پرونده این متهم در دادگستری استان البرز رسیدگی شد و حکم او پس از تأیید دیوان عالی کشور اجرا شد.
بر اساس رأی دادگاه، مجتبی کیان به اعدام و مصادره کلیه اموال محکوم شده بود. میزان همچنین نوشت از زمان بازداشت تا اجرای حکم کمتر از ۵۰ روز زمان گذشته است؛ موضوعی که پرسش‌های جدی درباره سرعت رسیدگی، امکان دفاع مؤثر و فرصت اعتراض در پرونده‌ای با مجازات اعدام ایجاد می‌کند.
قوه قضائیه گفته دادگاه با حضور وکیل برگزار شده، اما روشن نیست این وکیل منتخب متهم بوده یا تسخیری، از چه زمانی به پرونده دسترسی داشته، آیا امکان ملاقات محرمانه و آماده‌سازی دفاع فراهم بوده و آیا متهم فرصت کافی برای اعتراض به ادله فنی، درخواست کارشناسی مستقل و پیگیری مؤثر در دیوان عالی کشور داشته است یا نه.
این پرونده در بستر موج گسترده‌تری از اعدام‌ها، احکام امنیتی، مصادره اموال و رسیدگی‌های شتاب‌زده پس از جنگ قرار می‌گیرد؛ روندی که منتقدان و سازمان‌های حقوق بشری آن را نشانه استفاده فزاینده جمهوری اسلامی از مجازات اعدام برای ایجاد بازدارندگی سیاسی و امنیتی می‌دانند.
@
VahidHeadline
خبرگزاری میزان هیچ اطلاعاتی درباره حرفه این فرد نداده و مشخص نیست که مجتبی کیان چگونه به «اطلاعات صنایع دفاعی» دسترسی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75673" target="_blank">📅 17:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XifUoqZ6BUeYD5i7uSS6uTcuCJcG9-78nz0qQ7N8y9-PzRhRZOpLY342zUjBRCfvAheczvtjIUXZ066VJJwS2sgKqpxQDrSuS2uY-LhRpNR4q7pPnh6CJeCPpXINODPIWopjxCu9TkPB07wCLzdjeMlJ6FQFPCggm-w2iispTtlOUVstaR02oVNzY2kIwu_anFg1UeDc7VBEFPf2gHokXYTLUQ-d607TlkYZdwzd06o-7MGS4gUs8yq67YGkzVKgsPeG58kd1tqCzUSrCXBAtPXTSkQE2juPASRFhiiHEvy8g1DsKO7uXzFRw47yqqKr1my9PiSqevp787cCnqavdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: جزئیات توافقی که ترامپ در آستانه امضای آن با ایران است
ترجمه ماشین:
توافقی که آمریکا و ایران در آستانه امضای آن هستند، شامل تمدید ۶۰ روزه آتش‌بس است؛ دوره‌ای که طی آن تنگه هرمز دوباره باز خواهد شد، ایران می‌تواند نفت خود را آزادانه بفروشد و مذاکراتی برای محدود کردن برنامه هسته‌ای ایران برگزار خواهد شد؛ این را یک مقام آمریکایی گفته است.
🔻
چرا مهم است: این توافق از تشدید جنگ جلوگیری می‌کند و فشار بر عرضه جهانی نفت را کاهش می‌دهد. با این حال روشن نیست که آیا به یک توافق صلح پایدار منجر خواهد شد یا نه؛ توافقی که هم‌زمان خواسته‌های هسته‌ای رئیس‌جمهور ترامپ را نیز پوشش دهد.
▪️
وضعیت فعلی: هم ترامپ و هم میانجی‌ها گفته‌اند ممکن است این توافق روز یکشنبه اعلام شود، هرچند هنوز نهایی نشده و همچنان ممکن است از هم بپاشد.
▪️
این مقام آمریکایی طرح کلی مفصلی از پیش‌نویس فعلی ارائه کرده که بخش عمده آن را منابع دیگر نزدیک به مذاکرات نیز تأیید کرده‌اند.
🔻
چه چیزهایی در توافق آمده است؟
دو طرف یک یادداشت تفاهم امضا خواهند کرد که ۶۰ روز اعتبار دارد و با رضایت متقابل قابل تمدید است.
▪️
در این دوره ۶۰ روزه، تنگه هرمز بدون عوارض باز خواهد بود و ایران موافقت می‌کند مین‌هایی را که در این تنگه کار گذاشته پاکسازی کند تا کشتی‌ها آزادانه عبور کنند.
▪️
در مقابل، آمریکا محاصره بنادر ایران را لغو می‌کند و برخی معافیت‌های تحریمی صادر خواهد کرد تا ایران بتواند نفت خود را آزادانه بفروشد.
▪️
این مقام آمریکایی اذعان کرد که این موضوع به سود اقتصاد ایران خواهد بود اما گفت در عین حال کمک قابل توجهی برای بازار جهانی نفت خواهد بود.
🔻
این مقام آمریکایی گفت هرچه ایرانی‌ها سریع‌تر مین‌ها را پاکسازی کنند و اجازه دهند کشتیرانی از سر گرفته شود، محاصره هم سریع‌تر لغو خواهد شد.
▪️
اصل کلیدی ترامپ در این توافق «امتیازدهی در برابر عملکرد» است.
▪️
طبق گفته این مقام، ایران خواستار آزادسازی فوری منابع مالی مسدودشده و لغو دائمی تحریم‌ها بود، اما طرف آمریکایی گفت این موارد فقط پس از ارائه امتیازهای ملموس اجرا خواهد شد.
🔻
مسائل هسته‌ای هنوز باید مذاکره شوند
▪️
به گفته مقام آمریکایی، پیش‌نویس یادداشت تفاهم شامل تعهد ایران به این است که هرگز به دنبال سلاح هسته‌ای نرود و درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالای خود مذاکره کند.
▪️
به گفته دو منبع مطلع، ایران از طریق میانجی‌ها تعهدات شفاهی درباره دامنه امتیازهایی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، به آمریکا ارائه کرده است.
▪️
آمریکا موافقت خواهد کرد که در دوره ۶۰ روزه درباره لغو تحریم‌ها و آزادسازی منابع مالی ایران مذاکره کند؛ هرچند این اقدامات فقط در چارچوب توافق نهایی و پس از اجرای قابل راستی‌آزمایی آن عملی خواهند شد.
▪️
نیروهای آمریکایی که در ماه‌های اخیر در منطقه مستقر شده‌اند، در دوره ۶۰ روزه در منطقه باقی خواهند ماند و فقط در صورتی خارج می‌شوند که توافق نهایی حاصل شود.
🔻
نکته قابل توجه: پیش‌نویس یادداشت تفاهم همچنین تصریح می‌کند که جنگ میان اسرائیل و حزب‌الله در لبنان پایان خواهد یافت.
▪️
یک مقام اسرائیلی گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس تلفنی روز شنبه با ترامپ درباره این شرط ابراز نگرانی کرد. او همچنین درباره جنبه‌های دیگر توافق نیز نگرانی‌هایی مطرح کرد، اما به گفته یک مقام آمریکایی، دیدگاه خود را با احترام و لحنی محتاطانه بیان کرد.
▪️
مقام آمریکایی گفت این یک «آتش‌بس یک‌طرفه» نخواهد بود و اگر حزب‌الله برای مسلح شدن دوباره یا تحریک حملات تلاش کند، اسرائیل اجازه خواهد داشت برای جلوگیری از آن اقدام کند.
...
🔻
چه باید دید: به گفته مقام آمریکایی، کاخ سفید امیدوار است اختلافات نهایی در ساعات آینده حل‌وفصل شود و توافق روز یکشنبه اعلام شود.
▪️
این مقام گفت ممکن است توافق حتی کل ۶۰ روز هم دوام نیاورد، اگر آمریکا به این نتیجه برسد که ایران درباره مذاکرات هسته‌ای جدی نیست. از سوی دیگر، آمریکا معتقد است فشار اقتصادی بر ایران انگیزه‌ای برای رسیدن به توافق کامل به‌منظور رفع تحریم‌ها و آزادسازی منابع مالی این کشور ایجاد می‌کند.
▪️
این مقام آمریکایی گفت: «دیدنی خواهد بود که ایران واقعا تا کجا حاضر است پیش برود؛ اما اگر آن‌ها توانایی و تمایل تغییر مسیر خود را داشته باشند، این مرحله بعدی آن‌ها را وادار خواهد کرد تصمیم‌های حیاتی درباره این بگیرند که می‌خواهند چه نوع کشوری باشند.»
▪️
مشاوران ترامپ می‌گویند اگر خواسته‌های او درباره برنامه هسته‌ای ایران برآورده شود، رئیس‌جمهور آماده است برای بازتنظیم روابط با ایران و دادن فرصت به این کشور برای دنبال کردن ظرفیت کامل اقتصادی‌اش، که به نظر ترامپ «عظیم» است، اقدامات بسیار گسترده‌ای انجام دهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75672" target="_blank">📅 07:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1sKrRO0DifHEPy60Z2vdYWlBrBiob8sjx4PWydtFhk9LmYe23hbuVLK_YiCEz60uoXRPTRpU2ea8HuAAwWO5cG-rbSft5r8F5bM0qeWZQdFBdTwNfx-4hswkM4b0zdREpARqXaq8ufGXqFKUo0ibhwgk9fPLwXBJ7tKhHMRUxSPuCVrvQtdz25cAlxOkDgUmhLt3ZEzA6Vhp9F53SVlQFF6SMC6cWbh_CNJb7N4LR3laoBnCEpMWqwrCNQhHMLqljigGxK3pUQnoRbmsnRl68IQh27kg_DmhZWkKn7rdiaZ3uGjIlVNgptamB0ZzW-vnSSrymMFve--rBn2p6mjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWuKEzkiTHBIeFPjFK1M6XO485gHAF9rfsjsyBXGln--hnDE24JPdhYmRR464mtsnC34-LqZtsJ37tfQFzHAMRkQGymMhbmOVv_ATP4B-cjTAjLRc5SNXJX6sjRWbVpRkoE7JgiQewxw3aMaAjwV_09VraNHq9uUYz5tZVB6lKPRy-x5aWRxE8hI45OO9QgNxJZH4Eed9CHXneYiL86cZDk8CqHIzi_CYVi6UN84Qyq0NTOcp2DpuLIkbBDWyF5GwEQrky9cPm7Kmn7nsRzSybgB2qxk4CVadD3iNeFOvWvwL2hJeL1zWKpwEchf39YnhUGDzPsp6Kc_5w80QkGdcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی در شبکه اجتماعی ایکس با درج تصویر سنگ‌نگاره پیروزی شاپور اول ساسانی بر امپراتور روم، نوشت: «وقتی ایرانیان مهاجمان متوهم را ناکام گذاشتند.»
او در این پیام که کنایه‌ای است به محاصره دریایی بنادر ایران توسط آمریکا نوشت: «رومیان تصور می‌کردند که رم مرکز عالم است؛ اما ایرانیان این توهم را در هم شکستند.»
پیام آقای بقایی که به نحو گسترده‌ای در کانال‌های تلگرامی رسانه‌های حکومتی ایران بازنشر شده است به نظر می‌رسد که با استفاده از سنگ‌نگاره پیروزی شاپور بر امپراتوران روم در نقش رستم استان فارس بازنقش شده است.
آقای بقایی که اخیرا با حکم محمدباقر قالیباف به عنوان سخنگوی هیئت مذاکره‌کننده ایران هم منصوب شده است با اشاره به لشگرکشی مارکوس یولیوس فیلیپوس معروف به فیلیپ عرب، امپراتور روم، علیه امپراتوری ساسانیان، نوشت که لشگرکشی او «منجر به پیروزی رومیان نشد بلکه به صلحی با شروط شاپور اول ختم شد؛ امپراتور ناچار شد با واقعیت کنار بیاید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75670" target="_blank">📅 06:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lb7-s_AiJYfTgR8BaZfoIgthsLLLyTy3fAY-BbWcYIXawPdjJgCGXRmNEZL1fxumqqBn9NJpqfN9r_6rVo4zQUWuBeQSq_FruXh1lRLMMyRmGm1CDan5_mj-Tbi2LdJVniruPnZ4ldOlQ_4O0C1BssQoRdVMUn90lrvKoWbQ9o8u-8OsCE2zzNhMWoSJytBbUDYlYioZKMJ4JX4-qhsnx9I9U1TWVunluTN7wrdqekZ_98sg9xb8K69sSV88ig-7exzALk_Uk_ZyUEPBSoeQGbksAEkbLaQcd5bKbaPBsKN-NXzsWJV7R22duHBE1opRhFjP4ARACNQR7eyVSdCKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است؛
مقامات آمریکایی تصریح کردند که این پیشنهاد هنوز جزئیات دقیق نحوه واگذاری این ذخایر را تعیین نکرده و حل این مسئله را به دور بعدی گفتگوها درباره برنامه هسته‌ای ایران موکول کرده است، اما یک بیانیه کلی که ایران را متعهد به این کار کند، که هدف دیرینه ایالات متحده بوده، برای توافق بسیار حیاتی است، به‌ویژه اگر این توافق کلی با بدبینی جمهوری‌خواهان در کنگره مواجه شود. تا این لحظه، ایران هیچ بیانیه‌ عمومی درباره توافقی که ترامپ اعلام کرده، صادر نکرده است.
تهران در ابتدا با گنجاندن هرگونه توافقی درباره ذخایر اورانیوم غنی‌شده خود در این مرحله اولیه مخالفت کرده و خواستار موکول شدن آن به مرحله دوم گفتگوها بود، اما مذاکره‌کنندگان آمریکایی از طریق واسطه‌ها به صراحت اعلام کردند که بدون دستیابی به توافقی بر سر این ذخایر در فاز اولیه، میز مذاکره را ترک کرده و کارزار نظامی خود را از سر خواهند گرفت.
براساس این گزارش، بخش دیگری از این توافق محتمل شامل آزادسازی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران در خارج از کشور است؛ اما به گفته مقامات آمریکایی، ایران تنها زمانی به بخش عمده این دارایی‌ها که قرار است توسط ایالات متحده و متحدانش در یک صندوق بازسازی قرار گیرد دسترسی پیدا خواهد کرد که با یک توافق هسته‌ای نهایی موافقت کند؛ امری که انگیزه‌ای برای تهران ایجاد می‌کند تا پای میز مذاکره بماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75669" target="_blank">📅 05:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCJErU6jieaPhlHmg8510_QgDaoIoDYn4Od5exdENt8tbMk77RzukLP5ydFDvrtf2AvB0TsNomkeM4VLERZwlUp2tfBGO0RKR3F3BEbq_HBEbC2Bg_iXIf0G3bnk16jcOh2edyVl9UvrLolNz2nd0H2MRd-Ip2QEUHiv38n0ScXlcvJXNOE5xNmqsVfg0w_o8OWppScHrY4IcPcnED7j6jWSa8RMBmlIARUGRUk6Q0L6lB_3s8jrLlECuaG7SdiPVc2JSny-5zj0g1axXMRWaSjlBdCeLh_hZOpV1Qxad6jcQPHv4HZvAbmVkMuyIiA-81qyyfAUas3GJBZz3R_Z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان، ابراز امیدواری کرد پاکستان به‌زودی میزبان دور بعدی گفت‌وگوهای تهران و واشینگتن باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75668" target="_blank">📅 05:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gr-Lo0UnEL2UyoLXVheNHLxabS7XbnvXlo9Go8GYhmnkpLsqK14NlYpRpzA8ipX__uYcLmdECBzUfHlULqtGOhQimxQOBZ3K6SC6YmBEYaq1qArZT5LHmVKEoz4BhfFStODerIGPy9r8MXvekA-HX2aeqwjWF7nZPs2Mzg53dWDizMjOWbWqIE85R4vGVO5dpKReVlkNkrg_1OpNpCq-e0XW2uzj95ykBVjh5pvuetnRTpQuHLRrEjlv7ImjOH3lJfMHdUmi4UTlfenTCDIyfC6jNXJLYt1OZSKhpXRsKG3FNqq1ZL_GlrKFq49vi-52AJS8ZtMP7_C2L7IeJKkTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jMinB4JOe8gjxhCjhjMUHjUan3ycQo5V-pTLwHYegMUDZ3x-xFGm8tnl-GtIdb5S6F2vjfXxvpi46Ex61OtcvfaybW6qvLoYvx-StUrpZb16o8Wq6_xigKPxOqKuCL9eICP27zMX1G_eQM5zi0ChJG_Cmy94rdt6vsD-xF8uVV3aO_0W_Jy3Wwnp5dvtZ4hECoC9MtiZ-gK4j7MYcVyr6VrrFQrC__kFB4oYGjWkCRqXs_HaU8aWEAe0JJAnVFgeX4f2I6EKVQrMpxHDZhC_hWFWYP2617zXPnzBYSOS5YCggVahj41PF84XOI9LgidWMWzhKUcHYEghooQvuUoheg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت‌های تد کروز و لیندسی گراهام در واکنش به اخبار منتشر شده درباره توافق احتمالی
tedcruz
,
LindseyGrahamSC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75666" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7119557db8.mp4?token=EO5FHWeR7WbCOoeNC7Qr8HEQs5fqeEbjKpnUsQB1lpZUkhBQrlAkQTWZ632PFEPrHKmJEzoTjQYhH6trZ2tmXf1SwsRW7vKuti9hof2ls5QMyNDOmu63NfodOqH2SYc1pTES-PZdfkjSq-F0BVfCRlc0TXWfqIFmEYbfHKer4sI4thzz54JqDQmNYrMl_SKyQbylqFVyos2pxopzeu_wMsszZISxfYH4dEZKQclccxajXXQQ718KDv_NxNaWA-fPAnCsPuvaQFJkpYGuywzzPB0mdDHLxYuoC70FLe-cdBHmk8RvbqJlk2L15F9-SLxABbLKBJn60lqzOwL4j8c_jg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7119557db8.mp4?token=EO5FHWeR7WbCOoeNC7Qr8HEQs5fqeEbjKpnUsQB1lpZUkhBQrlAkQTWZ632PFEPrHKmJEzoTjQYhH6trZ2tmXf1SwsRW7vKuti9hof2ls5QMyNDOmu63NfodOqH2SYc1pTES-PZdfkjSq-F0BVfCRlc0TXWfqIFmEYbfHKer4sI4thzz54JqDQmNYrMl_SKyQbylqFVyos2pxopzeu_wMsszZISxfYH4dEZKQclccxajXXQQ718KDv_NxNaWA-fPAnCsPuvaQFJkpYGuywzzPB0mdDHLxYuoC70FLe-cdBHmk8RvbqJlk2L15F9-SLxABbLKBJn60lqzOwL4j8c_jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنبه عصر، یک تیراندازی در حوالی کاخ سفید خبر روی داد که طی آن دو نفر از جمله یک عابر و فرد مظنون تیر خوردند.
سرویس مخفی ایالات متحده، در گزارشی اعلام کرد که اندکی پس از ساعت ۶ عصر روز شنبه، فردی در محدوده خیابان ۱۷ و خیابان پنسیلوانیا، (شمال غربی) سلاحی را از کیف خود خارج کرد و شروع به تیراندازی کرد.
سرویس مخفی ایالات متحده افزود پلیس سرویس مخفی به تیرانازی او پاسخ داد و به مظنون شلیک کرد.
به گفته سرویس مخفی،‌مظنون به یک بیمارستان محلی منتقل شد، اما در آنجا اعلام شد که جان باخته است.
به گفته این نهاد امنیی، در جریان این تیراندازی، یک عابر نیز مورد اصابت گلوله قرار گرفت و هیچ‌یک از مأموران آسیب ندیدند.
سرویس مخفی که وظیفه حفاظت از رئیس‌جمهوری آمریکا را دارد افزود دونالد ترامپ، رئیس‌جمهوری آمریکا، در زمان حادثه در کاخ سفید حضور داشت.
@
VahidHeadline
آپدیت:
رسانه‌های آمریکایی هویت عامل تیراندازی عصر شنبه در مجاورت کاخ سفید را «نصیر بست»، جوان ۲۱ ساله اهل مریلند، معرفی کردند که به عنوان فردی با اختلالات روانی و عاطفی شدید برای ماموران امنیتی شناخته‌شده بوده است.
بر اساس گزارش‌ها، این فرد که پیش از این در ژوئن ۲۰۲۵ با ادعای این‌که «خدا» است یک مسیر ورودی کاخ سفید را مسدود کرده و پس از آن به یک مرکز روان‌پزشکی منتقل شده بود، به دلیل تلاش مجدد برای ورود به حریم کاخ سفید در ژوئیه همان سال، حکم دادگاه مبنی بر «ممنوعیت ورود و نزدیکی به این عمارت» را داشته است.
گزارش‌های تکمیلی نشان می‌دهد که «نصیر بست» دست‌کم در یک پست رسانه‌های اجتماعی تمایل خود را برای آسیب رساندن به دونالد ترامپ ابراز کرده بود؛ او سرانجام پس از نقض حکم دادگاه، نزدیک شدن به ایست بازرسی خیابان هفدهم و پنسیلوانیا و گشودن آتش به سمت ماموران، در تبادل آتش متقابل با نیروهای سرویس مخفی هدف قرار گرفت و در بیمارستان جان باخت.
📷
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75665" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1m2uGG4gEUFOFDT7v0gbsPoX04ec6o4HOSB5a6BgbaL_HReWXIC8ujHT_1pzIp6AtcXH37puWzYKooVVFAiySrwTaFhu5ZByevAtiBa1c93VJm1GuYKu761ONQkixk1jvmRB4x8fHmHFgg8Si3VcWeJUHKxmmeZAy0ck8aFj7_NZMGTuH6ofHTGAw4WCqb6vMAhgfbnUZD8MKPBFBINTPSidWEzLGCMsnzVtSmStAwVghNbdorN1jQIbk2gadf-OyHc8Dehrajny8de4qVYBxU4w9tnEBg3xrWFVh7gBDwR-awH5or-KoqeC_Y3qtYiyyf9oFo0LSQdul7TAqBJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس، خبرگزاری وابسته به سپاه، در واکنش به پیام دونالد ترامپ، رئیس‌جمهوری آمریکا مبنی بر نزدیک شدن به توافق با ایران و بازگشایی تنگه هرمز نوشت: «این ادعا نیز با واقعیت‌ها فاصله دارد».
فارس در ادامه نوشت: «برخلاف ادعای لحظات قبل دونالد ترامپ در شبکه اجتماعی تروث سوشال مبنی بر بازگشت تنگه هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد که این ادعا نیز با واقعیت‌ها فاصله دارد؛ چرا که بر اساس آخرین متن ردوبدل‌شده، در صورت توافق احتمالی، تنگه هرمز کماکان تحت مدیریت ایران خواهد بود و اگرچه ایران موافقت کرده اجازه دهد تعداد کشتی‌های عبوری به میزان قبل از جنگ بازگردد، اما این به‌هیچ‌عنوان به معنای تردد آزاد به وضعیت قبل از جنگ نیست و مدیریت تنگه، تعیین مسیر، زمان، نحوه عبور و صدور مجوز، کماکان در انحصار و با تدبیر جمهوری اسلامی ایران خواهد بود.»
خبرگزاری سپاه در ادامه مدعی شد که برخلاف شروط پیشین ترامپ مبنی بر گنجاندن برنامه هسته‌ای در توافق، «هیچ تعهدی از سوی ایران داده نشده و پرونده هسته‌ای اساسا در این مرحله مورد بحث قرار نگرفته است.»
فارس همچنین ادعا کرد که «مقامات آمریکایی در پیغام‌های متعدد به ایران اذعان داشته‌اند که توییت‌های ترامپ عمدتا جنبه تبلیغاتی و مصرف رسانه‌ای در داخل آمریکا دارد و توصیه کرده‌اند که به این اظهارات توجهی نشود».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75664" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeMg0vKDXTd__swCR3hl6jF8nVcos29oTN-BOtpPQKS_Acuw8zfdY6WCgILbea-duL4SoxzHcUYl_SS--frauIeTcIlcmQww2HqiVbLxNMpxwhG5CiENBGSc0lLxArj17Ho2FjMGsyFk9bHT09Bb-TM914Agg6TVYdo1mh9RjJdMhsVS61MzmOPVDeOeu9KYX0--GmkbS6eiQAgLP4_ujvGnQ3uBq0Zx-DVWuA0fCfQufcnAPkRmlbKKbWzQTuiksiYoX5DqqaNCQ01E6ZFyweDLQwSpZcfN6XJ7doA0CaPI-DTwB00faDRctvJ9jaBcWBX74N0aH9NQk7PQzWQsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار الجزیره به نقل از «منابع خود»، مفاد کلیدی پیش‌نویس توافقی را که قرار است میان واشنگتن و تهران نهایی شود را اعلام کرد.
خبرنگار الجزیره مدعی شد، توافق پیشنهادی شامل «پایان جنگ در تمامی جبهه‌ها از جمله لبنان»، «آزادسازی چندین میلیارد دلار از دارایی‌های مسدودشده ایران»، «رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز» و همچنین «عقب‌نشینی نیروهای آمریکایی از مجاورت مرزهای ایران» است.
پس از اجرای این گام‌ها، طرفین یک مهلت ۳۰ روزه، که با توافق دوطرفه قابل تمدید است، خواهند داشت تا درباره مسئله هسته‌ای به توافق برسند که در طول این مدت نیز تردد از تنگه هرمز تسهیل خواهد شد.
به گفته این خبرنگار، از نظر ایران، مدیریت تنگه هرمز یک موضوع دوجانبه میان تهران و مسقط تلقی می‌شود و گفتگوها در این زمینه با عمان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75663" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLoTPN6kxxgJS4kC-j3oukLDMAacfoNNf_2ba3vquVlRVgF06C_iUOVWRCYTR1jYZikK3Qc55wcs77Zf9ygp6uCfGlKts72O7WoyMMToCdmmCaGjigbFV_btZItkRjAyq1VnSNdH-WTZiWdZBPgXTd6vHW-prWHhVnKRhVi6SNy3Uik0BCL-cRjFOaUXIJCUU6QXE5S4pMd6Mw0QLsbLQ4N32Hw5a3s_ZKdreGq7HOwEqBaXaaHUTumom2Q1NEoBxtm3it7BqhUrgZ3sNCSe7Lo8cEYPf1_2bDcVhJUllTjTYTWQ87Cmo3HQpwCfQYfTIeNNDlT-UMLI228-bX0VNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یک منبع ارشد منطقه‌ای» از جزییات گفتگوی رهبران کشورهای عربی و مسلمان با دونالد ترامپ خبر داد.
خبرنگار آکسیوس نوشت: «یک منبع ارشد منطقه‌ای به من گفت که تمامی رهبران عرب و مسلمان حاضر در گفتگوی روز شنبه با ترامپ، از او خواسته‌اند تا برای پایان دادن به جنگ و مهار تنش‌ها در منطقه، توافق را پیش ببرد.»
این منبع تاکید کرده است که «پیام همه این بود: لطفا به خاطر کل منطقه، جنگ را متوقف کنید.»
به گفته این منبع، مذاکرات به خوبی در حال پیشرفت است و میانجی‌ها امیدوارند روز یکشنبه یک توافق چارچوب یک‌صفحه‌ای را منعقد و بلافاصله آن را اعلام کنند و پس از آن، قصد دارند ظرف چند روز مذاکرات را برای دستیابی به یک توافق دقیق و پرجزئیات آغاز کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75662" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RT0sJRpN7Wg9W3vhHbHdphsUos50KbdMvmJ_BlO2HXpeXm79bf_GYgm51NLX4OZnVbzcPLJJVQbHoSumxGpGuqDbwp5StyATkpcaG-F32v5ugR_mOHb8PRX9chQm0ZaVGtMggcbu4Lrm7pZCyg_SfMtYcJc1kMjYP_qO03sU5gVisihCRpPyjCzOx3WAs6l-nWeu93Mq1eWIrH3C1fb2-IQWJn6fUXPrjD-43-5wFi-pT_4Nyhpi32xYdNpQhpyxFv3CkQ14e1KOJkiTHNr3TG9U7Q2qrRfEZFt77Mr0V15RyCDAmeCsoj7CVsbPtY20pnsHI_RuiZQaipwzVLPAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: یک توافق تنظیم شده و اکنون در انتظار نهایی شدن است
پست ترامپ، ترجمه ماشین:
من در دفتر بیضیِ کاخ سفید هستم؛ جایی که همین حالا تماس بسیار خوبی با
▪️
پرزیدنت محمد بن سلمان آل سعود از عربستان سعودی،
▪️
محمد بن زاید آل نهیان از امارات متحده عربی،
▪️
امیر تمیم بن حمد بن خلیفه آل ثانی،
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی و وزیر علی الثوادی از قطر،
▪️
فیلد مارشال سید عاصم منیر احمد شاه از پاکستان،
▪️
رجب طیب اردوغان رئیس‌جمهور ترکیه،
▪️
عبدالفتاح السیسی رئیس‌جمهور مصر،
▪️
عبدالله دوم پادشاه اردن،
▪️
و حمد بن عیسی آل خلیفه پادشاه بحرین،
درباره جمهوری اسلامی ایران و همه مسائل مربوط به یادداشت تفاهمی در ارتباط با صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده و نهایی شدن آن منوط به جمع‌بندی میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگری است که نامشان ذکر شد.
▪️
جداگانه، با نخست‌وزیر بی‌بی نتانیاهو از اسرائیل نیز تماسی داشتم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به‌زودی اعلام خواهد شد. علاوه بر بسیاری دیگر از عناصر این توافق، تنگه هرمز باز خواهد شد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75660" target="_blank">📅 00:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_ArDcoRH-gCKdASF4IPo5VRIWtvK9XOERF-Dg7KqxuL_FDU_JX39h3N0PSVM4AGUfxTGIpfT6qyVLnRWHEMqk050fBD8os6W8YgTbi_zM87yV8Y_82o1vCR_s4n0QLcqnrEk2LyTk_OsTAhRRHXKMA-DkeeByIhkS4sMsOO1KWxjHMqaxuOpKgOJ8fmaktkM0WUdkyg9Tdpz0Gyu3abHi8MMOz2OVmbG9zrzErwVvL-p-_NXr7Ril6-G9ATTgGnGB5fy44nqlTnOZACImenXSK2NK8tBNYVQo5TbtYe2sAdXXhXGqVq7cTmScdlXq6mHAwamDODJU2Hs4a2y1POUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز شنبه دوم خرداد ۱۴۰۵ در تماس‌هایی جداگانه با رهبران عربستان سعودی، امارات، قطر، مصر، ترکیه، پاکستان و فرانسه درباره توافق احتمالی برای پایان جنگ با جمهوری اسلامی گفت‌وگو کرد. همزمان یک مقام آمریکایی آگاه از روند مذاکرات گفت واشنگتن و تهران به دستیابی به توافق نزدیک شده‌اند و اختلاف‌های باقی‌مانده عمدتا بر سر نحوه نگارش برخی بندهای توافق است.
به گزارش اکسیوس، چند تن از رهبران حاضر در تماس با ترامپ از او خواسته‌اند مسیر دستیابی به توافق را دنبال کند. با این حال، این مقام آمریکایی تاکید کرده است که هنوز تصمیم نهایی از سوی رییس‌جمهوری آمریکا اتخاذ نشده و او همچنان می‌تواند توافق را رد کرده و دستور حملات جدید علیه ایران را صادر کند.
همزمان، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و پیت هگست، وزیر دفاع این کشور، برای شرکت در نشست ویژه بررسی توافق احتمالی به واشینگتن فراخوانده شدند. ترامپ پیش‌تر گفته بود پس از بررسی آخرین پیشنهاد ایران با تیم مذاکره‌کننده خود، احتمالا تا روز یکشنبه درباره ادامه مذاکرات یا ازسرگیری جنگ تصمیم خواهد گرفت.
به گفته منابع آگاه، پیش‌نویس جدیدی که قرار است ترامپ آن را بررسی کند، حاصل مذاکرات اخیر میان ایران و پاکستان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75659" target="_blank">📅 23:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bof2-QpLentTMsdyGvmNXWRZu64IuIlCVgCyeR4Z7V7NtWftSx5IrgsOGE93aAa_iVceDFO-DeHTqfSLZEVnCOyXilFf7TeUvXqSDi21plBe8wny47tGt8peEfMOCbye1yyb0ZvG4yZyzn1a-hSXLwsYt0ALyh5XBlPRqMEbLQwAlnWNDYeeAG8KAiAyuosa8Rc1jtwZ4FuKyLabbPYofJL3RVIpvzk3pTUdcoBJoGhaMeh3PwfXl1d5ex5KSeodfd2Cl2khbtOTTCmlb66tKW_P4IsU56zwqWM85gMBOMSmjh7nIfB-t824AEcLUE6togiSYToXUmjlR7t5ceJumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ۱۳ اسرائیل در گزارشی از روند گفت‌وگوهای ایران و آمریکا گفت مقام‌های اسرائیلی معتقدند ایالات متحده و ایران به دستیابی به توافق احتمالی نزدیک‌تر شده‌اند و گزارش‌های اخیر و اطلاعاتی که دریافت می‌شود، «در اورشلیم به‌طور فزاینده‌ای معتبر تلقی می‌شود».
بر اساس گزارش این شبکه، مقام‌های ارشد اسرائیلی گفته‌اند پیشرفت در مذاکرات برای بخشی از نهاد امنیتی اسرائیل «بسیار ناامیدکننده» است، به‌ویژه در شرایطی که به نظر می‌رسد تلاش واشینگتن برای رسیدن به توافق در حال تشدید شدن است.
این مقام‌ها همچنین معتقدند فشار برخی مشاوران رئیس‌جمهور ترامپ در روزهای اخیر افزایش یافته و انتظار می‌رود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در پی این تحولات، نشست‌هایی مشورتی با وزیران ارشد و مقام‌های امنیتی برگزار کند.
نهادها و مقامات رسمی اسرائیل هنوز این گزارش را رد یا تأیید نکرده‌اند.
ارزیابی اسرائیل در دو هفتهٔ گذشته این بود که ترامپ خواهان توافق است، اما در نهایت به دلیل اختلاف بر سر مسائل کلیدی، موفق به دستیابی به آن نخواهد شد. با این حال، مقام‌های اسرائیلی اکنون معتقدند روند کنونی ظاهراً برخلاف چیزی است که اسرائیل در هفته‌های اخیر برای آن تلاش کرده بود.
این گزارش همچنین می‌گوید چارچوبی که دربارهٔ آن گفت‌وگو می‌شود، شامل یک توافق موقت ۶۰ روزه خواهد بود که ممکن است بعداً در حالی که مذاکرات درباره توافقی گسترده‌تر ادامه دارد، تمدید شود.
روز شنبه مقامات ایران و آمریکا و همچنین پاکستان که نقش میانجی را بین دو طرف بر عهده دارد، اعلام کردند که در مذاکرات برای پایان دادن به جنگ پیشرفت حاصل شده است.
روز شنبه، روزنامه اسرائیل هیوم نیز در گزارشی ادعا کرد پیش‌نویس توافقی که روی میز قرار دارد، شامل تعهد اولیه ایران به خودداری از توسعه سلاح هسته‌ای و تعلیق بلندمدت غنی‌سازی اورانیوم است و سایر مسائل، از جمله سرنوشت ذخایر کنونی اورانیوم غنی‌شده ایران، در مذاکرات بعدی در دورهٔ آتش‌بس بررسی خواهد شد.
این روزنامه همچنین به‌نقل از منابع آگاه که نام‌شان را نیاورده، ادعا کرد «رهبری سیاسی ایران پیش‌تر با تحویل اورانیوم غنی‌شده موافقت کرده بود، اما فرماندهان سپاه پاسداران با این اقدام مخالفت کردند و تصمیم‌گیری دربارهٔ این موضوع اکنون به تأیید رهبر جمهوری اسلامی بستگی دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75658" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S2gpO0D3LeTjJeoLCOK4qyvNOdEYV4Jx527gfH9Wybf56BiRTvsaO9-_aS8pu5tWUGdDb7q0r9LVv3j5HWeZjMAKp9-2yN7CLsyqn32eMw3RiLlrIl-KZyO73SuzZ6v6wPovk6GpYDF2IS2Vu_nOMDMOMKiKmj9bbkFn-V2Zy8lAo813R_NmQ_l_ahXcNoFLTKCynQ-z282y3_CsSQI4oghx2NwN-x8Jt3nLzUei-7K0vpLpd88_FYcrox2vQVdwYVrBBkY4WL8GfuGb2tVqzOrS1lzcDV9hZHR-psNxGhYhbSGBQ-1ONHOCas6pcf9f5946fVDMnRQ0m2KJrUStQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه و نزدیک به تیم مذاکره‌کننده، با تاکید بر اینکه اگر آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد نوشت که موضوع هسته‌ای، پول‌های بلوکه‌شده و کنترل جمهوری اسلامی بر تنگه هرمز، سه موضوع اختلاف جدی در مذاکرات است.
فارس نوشت که تهران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
رسانه سپاه به نقل از این منبع نوشت: «پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود تهران به مذاکره این است که پول‌های بلوکه‌شده ابتدا واریز و آزاد شوند. بدون این اتفاق، اساسا وارد مذاکره نمی‌شویم.»
در ادامه آمده است: «اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگه هرمز است. آمریکا تاکید دارد که تنگه باید کاملا به شرایط پیشین بازگردد، اما تهران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که حکومت ایران با مدل خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75657" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqBiA1vF5vYYVlzu7MeIxsojN4JGkKobDXsdYbV_oREipvqNfQ8p5DJ28lZQYShCZ5dHQdteTO6yB1MCmilMr6VW5cBPAbD43_GexEzzO2iG2i7uK8P1POVwC7ZL6CU_Y10-D7C0nepVii81K29IJsvDiT6kPRFSOg3eIsuglzOHrlcNwrCY59Oko5ayCRs_JEmDNf0JCK1-e55JHd0oafRrh5BpoM4EmX-GE1EHaacfAGnyAhxlfUfcjmWlYdrTNcwzsquLfZyFCHXEVHj3R491FGPfQZIa5GygAvdmYQegUOPz37Kn0Y0dvrNj_zYaQJT9A0fQQQGexWizZ3EU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به توافق بسیار نزدیک‌تر شده‌ایم
ترجمه ماشین:
پرزیدنت ترامپ به شبکه سی‌بی‌اس نیوز گفت مذاکره‌کنندگان ایالات متحده و ایران برای نهایی کردن توافقی که به جنگ میان دو کشور پایان دهد، «بسیار به هم نزدیک‌تر شده‌اند».
منابع آگاه از مذاکرات به سی‌بی‌اس نیوز گفتند تازه‌ترین پیشنهاد شامل روندی برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های ایران که در بانک‌های خارجی نگهداری می‌شود، و ادامه مذاکرات است.
آقای ترامپ از ارائه جزئیات درباره این توافق خودداری کرد، اما گفت که «هر روز بهتر و بهتر می‌شود.»
آقای ترامپ در یک مصاحبه تلفنی به سی‌بی‌اس نیوز گفت: «نمی‌توانم قبل از اینکه به خودشان بگویم، به شما بگویم، درست است؟»
👈
آقای ترامپ گفت معتقد است توافق نهایی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و افزود که در غیر این صورت «اصلاً درباره آن صحبت هم نمی‌کرد».
👈
او همچنین گفت این توافق باعث خواهد شد اورانیوم غنی‌شده ایران «به شکل رضایت‌بخشی مدیریت شود.»
👈
او گفت: «من فقط توافقی را امضا می‌کنم که در آن به هر چیزی که می‌خواهیم برسیم.»
منابع به سی‌بی‌اس نیوز گفتند آقای ترامپ هنوز در حال بررسی پیشنهادهاست و هنوز تصمیم نهایی خود را نگرفته است. این منابع گفتند او با مشاوران خود رایزنی می‌کند و با رهبران خارجی، از جمله رهبران عربستان سعودی و دیگر کشورهای حوزه خلیج فارس، گفت‌وگو دارد.
آقای ترامپ گفت اگر آمریکا و ایران به توافق نرسند، «با وضعیتی روبه‌رو خواهیم شد که هیچ کشوری هرگز به اندازه ضربه‌ای که آن‌ها در آستانه دریافتش هستند، ضربه نخورده باشد.»
آقای ترامپ پیش‌تر ایران را تهدید کرده بود؛ او پیش از آغاز آتش‌بسی که در ماه آوریل آغاز شد، گفته بود بدون توافق «یک تمدن کامل نابود خواهد شد» و اخیراً نیز به این کشور هشدار داده بود که «ساعت در حال تیک‌تاک است.»
مارکو روبیو، وزیر خارجه آمریکا، نیز روز شنبه گفت ممکن است «بعداً امروز خبری» درباره وضعیت مذاکرات میان ایران و آمریکا منتشر شود.
روبیو پیش از یک شام رسمی در سفارت آمریکا در دهلی‌نو، هند، گفت: «پیشرفت‌هایی حاصل شده، همین حالا هم که با شما صحبت می‌کنم، کارهایی در حال انجام است. این احتمال وجود دارد که چه بعداً امروز، چه فردا، چه ظرف چند روز آینده، چیزی برای گفتن داشته باشیم؛ اما همان‌طور که رئیس‌جمهور گفت، این موضوع باید به یک شکل یا شکل دیگر حل شود.»
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75656" target="_blank">📅 19:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XPi5z9dbRY2TSEVwb31tLB-pj6qUMGra8mFBCv_d9SLbWX-hlWcPnoZusAtBLKQXmhFPdcwZigfRo11-Pk6U3I6idSyPKYzkjfKAKdcgVVNzYRlyy4B2Y9syiIp_KnS7OPjYO7hsFlFCG0_uu-RLFzZ03nQW9SpdBGJXijhvff3gUZbxCZVwsAaOkl66Da3WhH0y9Un7VtQhEZpYxTNqZEvlkEzR0uO65Noya3rqR2SfyB4Sih0PHqF-4lBIZeSbgDDkDbFc0-2ec-EY7TydonnZx0c2qiKyMI-oCAZkY6_tU8CfAFpITVaXOetc9hv1uXfJGPu20GCJNMve--WVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز شنبه دوم خرداد در گفتگو با آکسیوس اعلام کرد که اواخر امروز با تیم مذاکره‌کننده خود دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند. او افزود که احتمالا تا روز یکشنبه درباره پذیرش توافق یا از سرگیری جنگ تصمیم‌گیری خواهد کرد.
ترامپ شانس دستیابی به یک توافق «خوب» یا در غیر این صورت، «نابود کردن کامل آن‌ها» را یک «۵۰-۵۰ محکم» توصیف کرد. به گفته او، قرار است اواخر روز شنبه نشستی با حضور استیو ویتکاف، جرد کوشنر و جی‌دی ونس، معاون رئیس‌جمهور، برای بررسی پاسخ اخیر جمهوری اسلامی برگزار شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75655" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuF0FZl9CTU1dCVAvZK-lTO3arT4-j6PFH1chwXLBuLw1LoTbwy2sxU9IpbHnVVQSf8zSFitHZoRBLd8JO_Qx_A137q1qO0dWtn5xK-8vU1cGaIDOqI8Wxc1k2aXGSYUcuDqZF3tz36MpoAZM040r2RR5zQiILNj7lepTxeUiOAZcJ0E-ej09G-vbO_Lu-xYA97u88f-tbTS_1qAsXAWkYN7wBi-ZL78ujER-XxNMWvYsHVaxDCT4wgtIrgFW6_uENNLz-C8jWIDgpoh68c-efI24e2BEkyO3NZBn7pBm8ZfR1cvYt2ZaFOABqX4kGHyVQd3u1BwwaXE253Qyqwu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، رسانه وابسته به سپاه، درباره روند مذاکرات تهران و واشینگتن، با اشاره به اینکه هنوز اختلافات جدی در بعضی از حوزه‌ها مانند تعهد واقعی آمریکا به آزادسازی اموال و موضوع تنگه هرمز وجود دارد، نوشت: «با توجه به زیاده‌خواهی‌های آمریکا، احتمال عدم حل موضوعات بالاست.»
در این گزارش آمده که در صورت حل موارد اختلاف، احتمالا در گام اول یک تفاهم اولیه اعلام شود و سپس مهلت ۳۰ یا ۶۰ روزه برای گفتگو درباره موضوع هسته‌ای (بدون تعهد اولیه جمهوری اسلامی) اعلام شود.
تسنیم نوشت که آمریکایی‌ها در متون پیشین خود تاکید داشتند که تهران در همان گام نخست باید امتیازاتی در بحث هسته‌ای بدهد و موضوع تعطیلی تاسیسات هسته‌ای و تحویل مواد غنی‌شده به آمریکایی‌ها از جمله مباحثی است که مدام در متن‌های آمریکایی‌ها مورد درخواست قرار می‌گرفت اما حکومت ایران اساسا بحث درباره جزئیات هسته‌ای را در این مرحله رد می‌کند.
بر اساس این گزارش تهران بر ضرورت پایان جنگ و تهدید در همه جبهه‌ها از جمله لبنان تاکید دارد. و این موضوع باید مورد پذیرش طرف آمریکایی قرار گیرد اما آمریکایی‌ها در برخی از متن‌های پیشین خود با این موضوعات مخالفت کرده‌اند.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/75654" target="_blank">📅 19:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgl2ad3QDldxt6vDZB5d0Rqm_lALSmCFsKRQWMmjZgOp8NnO7kwcCnk-_ipKPv7Jdwt1OSxoXHQ3iHcODqgcwJt8Hs3Mi34Om_yTZWKKhn5Eu4waaEby49T7ljsrxdvl1HWYDkYGYck1AjbWi-Ostg1KnWYvEhwROhaWJRTIRadHVemgW8qY8FD92jSbJfMvAtgO5WlhMRMYlzU8rMfkhauxR-MLe-LuI_aZy3mXYUcnbCB4-QRnHUjIi2ZpS93TE24rwkjItX2ASl87dkrtOOiRWDbYPo7pok-maqGe8NhdrQ4e3NCySr3TD8SNCThqzgnBVYfTpGdqHzDZ-7OqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخش رسانه‌ای ارتش پاکستان (ISPR) آخرین دور گفتگوها میان میانجی‌های قطری-پاکستانی و مقامات بلندپایه جمهوری اسلامی را «کوتاه اما بسیار پربار» توصیف کرد.
بر اساس بیانیه منتشر شده، این رایزنی‌های فشرده در ۲۴ ساعت گذشته در فضایی مثبت و سازنده برگزار شده و پیشرفت‌های دلگرم‌کننده‌ای را برای دستیابی به یک تفاهم نهایی جهت پایان دادن به جنگ ایجاد کرده است.
ارتش پاکستان جزئیات بیشتری از مفاد دقیق این مذاکرات ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/75653" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujul3pZPQ2FTeTikq7kgac21-6iC0-UtPUMFqjLfiPsJso53ZmylqsmE3MKiySO0i-VFqzGyuPiqvy2nvasfa8BJHpqPuuaX8F4zN7EjgClekakswyAGN-rvkqy75nsfA4CJl5V96I6b_MWsAc5PPXmQ9S_606HM6VHfOsaKJXSU_40mt94lwD1UjPB_F-OgaXnh7iPp506JkVvu81py_q1rx3S7_JJCNW86ZGSgQcm6U9U0AOAo0enA3CzbN3Bb1Qq2xTs39XK_9yl4XcKJ4-8LNszIMdnYCE8dINSJuJzivSxDIi3oaNrlRxjpiMBONAAC6NQsUgXjoXGQ6GHH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز گزارش داد که میانجی‌های جنگ ایران معتقدند در حال نزدیک شدن به توافقی هستند که آتش‌بس میان واشینگتن و تهران را به مدت ۶۰ روز تمدید و چارچوبی برای مذاکرات درباره برنامه هسته‌ای جمهوری اسلامی ایجاد کند.
بنا بر این گزارش، افرادی که در جریان این مذاکرات قرار دارند به این رسانه گفتند این توافق شامل بازگشایی تدریجی تنگه هرمز و همچنین تعهد به بررسی رقیق‌سازی یا واگذاری ذخایر اورانیوم با غنای بالا خواهد بود.
فایننشال تایمز افزود که آمریکا همچنین محاصره دریایی بنادر جنوب ایران را کاهش می‌دهد و با کاهش تحریم‌ها و همچنین آزادسازی مرحله‌ای دارایی‌های مسدودشده تهران در خارج از کشور موافقت خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/VahidOnline/75652" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=bmuhw3A-hOlwr42w-A1lLapPwQ0RVpa90DBmOC8wiSb5QPQ-cU_kBnWvyprwp55pNrecZqwx5yZbnG1zrrPL66B2F8fpEjHcXsp215RcmoeVAlvroVv1S-XK8UbpHMu3UcKuYGGfuSNaQ23jHwKZJ9EjNOpE0Beq0LU6fuMpEgH2Xv4ALt3-45_GtH0VaiCIVGRiFKf-tPntjPBWugU2cUhjZHk5gdLfRXOf26ZkI_zcpZyZSwdqlErFPqXnM1NFYkfu7Kzy-WKZggnQMPYxTnxv4BnvKP8n3Xzln2NmIYjBp94bwbHOsf8K5OCHL0_fq1PRFNLsZf9zkcxMJWQ40w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=bmuhw3A-hOlwr42w-A1lLapPwQ0RVpa90DBmOC8wiSb5QPQ-cU_kBnWvyprwp55pNrecZqwx5yZbnG1zrrPL66B2F8fpEjHcXsp215RcmoeVAlvroVv1S-XK8UbpHMu3UcKuYGGfuSNaQ23jHwKZJ9EjNOpE0Beq0LU6fuMpEgH2Xv4ALt3-45_GtH0VaiCIVGRiFKf-tPntjPBWugU2cUhjZHk5gdLfRXOf26ZkI_zcpZyZSwdqlErFPqXnM1NFYkfu7Kzy-WKZggnQMPYxTnxv4BnvKP8n3Xzln2NmIYjBp94bwbHOsf8K5OCHL0_fq1PRFNLsZf9zkcxMJWQ40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‌ویدیوهایی از اعتراض دانش‌آموزان در شهرهای مختلف منتشر شده است. این دانش‌آموزان به حضوری شدن امتحاناتشان اعتراض دارند.
دانش‌آموزان در شهرهای خرم‌آباد، یاسوج و دورود مقابل ساختمان‌های آموزش و پرورش این شهرها تجمع کردند و با شعارهای مختلف اعتراض خودشان را نشان دادند.
در جریان اعتراضات سراسری در دی ماه ۱۴۰۴ که به کشتار بی‌سابقه معترضان انجامید در بعضی استان‌ها مدارس غیرحضوری شد.
با شروع جنگ آمریکا و اسرائیل با ایران، مدارس در ایران تعطیل شد و بعد از تعطیلات نوروز کلیه کلاس‌ها غیرحضوری برگزار شد.
چند روز پیش عبدالرضا فولادوند، سرپرست مرکز ارزشیابی آموزش و پرورش در یک مصاحبه تلویزیونی از احتمال برگزاری امتحانات به صورت حضوری خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75651" target="_blank">📅 19:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuqk1Ifyidu-0HxmUTwY0YTKB9pvzrRjmpC6_BIVmUUsIPk2ghAlmD_anvuEGNrxALciGsG2nAxP0qPEqXt8mjxMNvR1xOdnCqsSI6QyeFpwU1Fuf-gxfiZ-5ceFhewzJOu3y3RJc6LBefS-7_WqVnLVGIXBvOqrQGJj_zjZt3EQRvgQsTn014itYlvyHUto_5cVpmwYNZt6uAm4TqtZbdMMODX0wHUeivDOtgQdfLeU_tc8o8CZeTjTPxyo0ATOjFKQLD0f6RyblR2Fm1gjUUi2gkioC5uqUack0niSNFbREIM1JiZ6dg_2SaizBLvmeOTSKfC1UD4rjDN2_YaRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام جمهوری اسلامی روز شنبه دوم خرداد، در گفتگو با شبکه الجزیره اعلام کرد که تهران با میانجی‌گری پاکستان با یک تفاهم‌نامه موافقت کرده و اکنون در انتظار پاسخ ایالات متحده است.
به گفته این مقام، مفاد این تفاهم‌نامه شامل پایان دادن به جنگ، رفع کامل محاصره دریایی، بازگشایی تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
او تصریح کرد که به دلیل پیچیدگی موضوع هسته‌ای و نیاز به زمان بیشتر، این تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود؛ با این حال، پس از گذشت ۳۰ روز از اجرای این توافق، درب‌های مذاکرات هسته‌ای باز خواهد شد.
این منبع آگاه همچنین اشاره کرد که قرار بود فرمانده ارتش پاکستان این تفاهم‌نامه را در تهران اعلام کند، اما او جهت هماهنگی با واشنگتن، ایران را ترک کرده است.
او با تاکید بر نقش اساسی دولت قطر در تدوین این پیش‌نویس افزود که ایران هیچ امتیازی فراتر از آنچه در این تفاهم‌نامه قید شده، واگذار نخواهد کرد.
@
VahidOOnLine
همچنین بر اساس این گزارش، تهران پیشنهاد داده غنی‌سازی اورانیوم بالاتر از ۳.۶ درصد را به مدت ۱۰ سال به حالت تعلیق درآورد.
@
VahidOOnLine
🔄
آپدیت:
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75650" target="_blank">📅 17:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5ZKhg2cxyPEWcNbNuhCk00TgRJlDJsbCGep65QsGXPqbfExfzJS40Tbzb9ZWvkos637JXunwRNqp2dANYmjVMdBJ8nH0wFPnk65c-p2lmOKT_VbRSUqArQBCO1OSWDY_Z4LAKIN98yL5-C0Box7j91IB6lcTHRCZio0qgyfuXR-9VkrXTAtEjOiECR2Vy9b1AesSJil5MjD01vHkdbjdidtKK0fjnpnx1zX87eGbWYTnH-9N9Xk7FITEO-6iA_xGKGkGSKzfZqp5tLHk5hLeuU-qYZmPamzcQeb1_CaktJmjbe7wjmnRAYAiQtc3XpRkLvw11WQh0coU6_ifuAytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه گزارش داد جمهوری اسلامی دو پیشنهاد به میانجی پاکستانی ارائه کرده که بر اساس آن، در ازای پرداخت غرامت از سوی آمریکا، تنگه هرمز را باز کند و پیش از امضای هرگونه توافقی، پرونده تحریم‌ها و دارایی‌های مسدود شده مورد بحث قرار گیرد.
دونالد ترامپ، رییس‌جمهوری آمریکا، پیش‌تر گفته بود که حاضر به پرداخت غرامت به تهران نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75649" target="_blank">📅 17:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lF4DnJLHHDM3mbNCzSdVqQ-EwsaVAOGkdHJajS-kiQe5S-_c4u6OPtxuihv7Ds_GQxcS6JytgYU47Ud4Q3F9yx8HGOI4pnmtIA6mMqrMaxldKSqpdVuAWHNDevBKC09Vj8YWbZrSRP11zzAVVqsZihaIwem1XMeNBgKUNzSThPlcH4ayaW-p-9IDEEkKVjvIVJI62ve2m2A_jciqLlFUnpHg0TfxPrfiAmIwelG4fgVXz_frY6rhFhNROpOHgzmqPSt-MLPZ0uvRPa6xgzbvtvEX0UtFIKYjsrSGRgKO31YCiWJzS0Ilt7oqWFxKGbyeNUUbaZVK14o__SwMeqabNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری از نقشه ایران را که با پرچم آمریکا پوشانده شده، در شبکه اجتماعی تروث سوشال
منتشر کرد
. روی این نقشه نوشته شده است: «ایالات متحده خاورمیانه؟»
ترامپ توضیح بیشتری در این‌باره ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75648" target="_blank">📅 17:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=hj6GzX9HvvNh6tvDU1o3K_iC-JpjWlqnHXZ0Q-KBzqvflm5YlGVaKmG_xeP-Q2ab0LY64p2fHpPAEHHfxXljBqaWa3rV_NMUIteIJ1BXJafYiXKlbnYhEovrG8g3gUPRFf4zjKdklhMX72swat_pMsnzjbJxDBYzgc6jhROsMTDbdr7JESOkMr7HbMbjq0NktA5o4pjxkgglOcbd-GFDJnGHiCgHfX8qtY7gHf_uA49iul9jUSTliIfv7X0x_2wf9fQMsuL50UUp7MZAjnClWxQFc85uChlyaLe6iEbYxbGwhTSdXDNldKZwHSmOn6BQ1VjtVfutaMS87MXGIPDdQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=hj6GzX9HvvNh6tvDU1o3K_iC-JpjWlqnHXZ0Q-KBzqvflm5YlGVaKmG_xeP-Q2ab0LY64p2fHpPAEHHfxXljBqaWa3rV_NMUIteIJ1BXJafYiXKlbnYhEovrG8g3gUPRFf4zjKdklhMX72swat_pMsnzjbJxDBYzgc6jhROsMTDbdr7JESOkMr7HbMbjq0NktA5o4pjxkgglOcbd-GFDJnGHiCgHfX8qtY7gHf_uA49iul9jUSTliIfv7X0x_2wf9fQMsuL50UUp7MZAjnClWxQFc85uChlyaLe6iEbYxbGwhTSdXDNldKZwHSmOn6BQ1VjtVfutaMS87MXGIPDdQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان مارکو روبیو در سفر هند در پاسخ به سوالی درباره مذاکرات با ایران
ترجمه ماشین:
ممکن است امروز کمی دیرتر خبری باشد. در همین لحظه خبری برای شما ندارم، اما ممکن است کمی دیرتر امروز خبری باشد. ممکن است هم نباشد. امیدوارم باشد، اما هنوز مطمئن نیستم.
سؤال در مورد موضوع ایران است و همان‌طور که گفتم، پیشرفت‌هایی صورت گرفته، پیشرفت‌هایی حاصل شده. حتی در حالی که الان با شما صحبت می‌کنم، کارهایی در حال انجام است.
امکان دارد که چه امروز کمی دیرتر، چه فردا یا چند روز آینده، چیزی برای گفتن داشته باشیم. اما این مسئله باید حل شود، همان‌طور که رئیس‌جمهور گفته، به یک شکل یا شکل دیگر.
ایران هرگز نباید سلاح هسته‌ای داشته باشد. تنگه‌ها باید بدون عوارض باز بمانند. آنها باید اورانیوم غنی‌شده خود را تحویل دهند، اورانیوم غنی‌شده با غنای بالا.
ما باید به آن مسئله رسیدگی کنیم. ما باید به مسئله غنی‌سازی رسیدگی کنیم.
این‌ها نقاط مورد نظر رئیس‌جمهور به طور مداوم است. و ترجیح او همیشه این است که آن را از راه دیپلماتیک حل کند. ترجیح او همیشه این است که مشکلاتی از این دست را از طریق راه‌حل دیپلماتیک مذاکره‌شده حل کند.
این چیزی است که الان روی آن کار می‌کنیم. اما این مشکل حل خواهد شد، همان‌طور که رئیس‌جمهور به وضوح گفته، به یک شکل یا شکل دیگر. امیدواریم از طریق مسیر دیپلماتیک انجام شود. این چیزی است که روی آن کار می‌کنیم. و شاید چیزی برای صحبت در مورد آن موضوع در حالی که اینجا هستم، در طی این بازدید در زمانی داشته باشیم.
EricLDaugh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75647" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is4QaHjzJXv8dpe4IVa8QtTJIxYkCrR8Y3Pqkv5IXduvkvmUaq6RFaJGc90XkbaW9kvTxES0uNZRiQwgevMbWsfGn1neT5ZdulB97v9yqHjFKxDlK0VPoqOxlWuTdAtNypLXiEOpgULKbqfwmHGR19jxy1I2PmZD-8fnOICr-xdKHY2cYT7Jh33ZrTV-pG7CoYm87zc6ra2ab2OMdtutytbV36gffDkdztt5KfWYXT2vRwmuY7DYLAIybF9J0JasMJSIBVAkr_2lt43xbmrYhZdT8J6VhnBgfxT1DAWNJo02s8mQATblOKWbkX9StFwRrPHACeQsnD5XHtPipKPUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در پیامی به شیخ نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «جمهوری اسلامی دست از حمایت حزب‌الله نخواهد کشید و همچنان از جنبش‌های مطالبه‌گر حق و آزادی پشتیبانی می‌کند. تهران پیوند آتش‌بس لبنان با هر توافق احتمالی را به‌عنوان شرط مطرح کرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75646" target="_blank">📅 17:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpiaNm1pTsdLBDrIVZwSespOauIJs8nJ3OhSiOwhInNP4jORlP7JzKm89QvjBz3C1vqE9Vt3dkGca3Q5tlCm2KV8ZFoz7xh1RXFriBecMFmGMkDqPp-LQTZZrMpAyBPkvftVe9aomW_3WAwHMPrh9SU9clsFalZnfZAFy9QcXRJfCBPIpezdK0knZP8Ejgee4gIZz6qAj4HZd65HnH9GhN7Ig1dEBrwzeYw2hz8O0jl1OFb5SJHjPbyV5jDRLBDCzLWvY5UWh3gcHyh5Qq806KnTGb-ZEQJL7Tmh1zCi9N4vkymT4g_5m8QpQUk087XrRpFerDUZgCZBveSkxz5lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز قلیچ‌خانی، کاپیتان پیشین تیم ملی فوتبال ایران و فعال سیاسی چپگرا در ۸۱ سالگی درگذشت. او به آلزایمرمبتلا بود.
نجمه موسوی-پیمبری، «یار و همراه» پرویز قلیچ‌خانی به بی‌بی‌سی فارسی گفت: «قهرمان ملی و چهره همیشه زنده ایران در تاریخ بیست و سوم ماه مه ٢٠٢٦ مصادف با  دوم خرداد ١٤٠٥ در بیمارستانی در حومه پاریس درگذشت.»
آقای قلیچ‌خانی، پیش از انقلاب، علاوه بر تیم ملی، در باشگاه‌های تاج، پرسپولیس و پاس هم بازی کرد. او تنها بازیکنی است که با تیم ایران سه بار قهرمان جام ملت‌های آسیا شده است. پرویز قلیچ‌خانی بعد از انقلاب هم در خارج از کشور، مجله آرش را با گرایش سیاسی چپ اداره می‌کرد.
او فوتبال را از کوچه‌های محله صابون پزخانه میدان شوش تهران شروع کرد و بعد از مدتی کوتاه فوتبالیستی ماهر و بالاخره کاپیتان تیم ملی ایران شد.
ولی هنوز طعم قهرمانی فوتبال را درست نچشیده بود که توجهش به سیاست جلب شد و از پشت میله های زندان سر درآورد.
پس از انقلاب از فوتبالیست حرفه‌ای به فعال سیاسی و روزنامه‌نگار خارج‌نشین تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/75645" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ojT8e0mXyQarEInrgQz7hvmf8MwBasFWihMkGDwGXHrE671kMtBmTHTzJM928uHn8Hq-VUu4HuhvkLoY5Xqo_xDjsIVtAsoMnrpdjK77KIm9E_gXgD5ErKLZMVIbwqgkOGzoC7EnWnDVUVys33hrpJ71RHTJeYYfhr-RwTPNDZfChMuXvz_bY-zFUEqxA9m33hYBcVTEWxJliRaKjfa7wNIQ0dL3tYrsZHrDDUkTSoMOFGJ3CUoVciuqPNQ4AQq1Q1TvkRnbzHnagpq2LQ7wsFTVv6_cKLZ9h2e7W-gG1YoerLlv9vPZdPJvMmlnIMMJEMWd5AahrO56zurZVw4Xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gjuZVMMgMxoctJgVn_OAb1pk9hp6utWXS4DixFBM1z4jOTnKqWiCUNRVhjIQnQF78iOn1MWMgNEm7ocDRGJfndB5dnnR9ASV3-tvtTWbyBX4Iyu0lnisOMXV9AKB48snIIc06XQt6leS9PFVRTMWxVfWv3Jw20rH4HRSJrMOnFE3advj--d1c3ZPJhD5ObeqFtYLAClhYCsURKchGwJpGGlC2mZ_zVsme9vT5CHJE_Dtg0RlfBkVPAa5F9B8yZH710Ky5THcgONfAgsIlo9boC1MGzbOuonBfQEd3jKOF6yPM8no5z7Cvx_QbXCXqdb9RefoSF7aD9xVtkb5vrzzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IoVRvgB1G_yxbx8mK8h9sMqSG7DYXAfm7rexomry8RK-eTKm_kY-8PrNgiwXxTt4nJMLR3lXel7VDL58QaqFlm5BzLnwymghHeexHRMG3132Qse9XkZP6AK2XINQBrn6DwAxZJL_vYE2_bXM-bHEoxcXZxT_GL384VFxPaT3yS83j4ULMGzAWd5Jv_1Lr_OvLgj-3udgBZp4YJo0fhiIfZKyAQACuqB8h1XxzhVTMIPtLsgnG7NadD9FWl57am2KdNzFFa6lyRagMGSQdlrSFYZsBOsmYoLXuP_OmBvIU2l6-yg3qLkMRcoNv-5BH4qR3mvnmsMfbmCWEjMjN-U3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JUY_TjR9Q-PRpFCr4AIzrw4lXYlXX9TMH6dM2JcJSFNUYqod4vhS7FmwWMoqBbjHBhcScC2GewxgvISJJLOerXsN2xkcU-Woc6poAnagVYEJBusPgkVEtvFZJd5vF9-CCiDWYpiNg43ZpTnQxutDqsAwfdEYmTpLYCKUNTsnB9BQr3kdSaaCsBaImO6WEpE8fk_U1K-aewC92hMdlQIayvm-onJ6_6Nv4Cw86JyeJEPRCEDJzGpwdElGIU0lSTkgyQuopzwJjOKDHChh8-MxBzJOq9dktIswnZIk9QaE8Sm3fBSz3QREO8zCRgrIxZxUB1bcn1_Im3nmvjugTMOJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xnz1uFW5C9SFa_MSDjg_q5GakN7qlFsII8mBHGydCuVL3MlEc5-AbbKiVe6vnIv4oBQ5SVNsCwq8V0dI7wX2R9J70MS1_OGTa1kqjwVsKogXzKIuZrlSODWRXlEuAZ_wef9g2kLqM17tEP2NoccyRZB3671rVGAUF7vzXlmIChAipdBM2ZSMVt8lRVbpGy5icD5OxvB27V26AHxx0M6IeLHFLfWOVieoFhFPteVT8RFmaZq_Yo8Rbts4SYafv54xP_SVvrNn4FKjzZuoyVvdxTu90EYtwqX9BM3pFr0zb-dRtyRZK35TheMs0nNj0h0cQJnTauN_iblbZnCm4mAWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WylFxrN3CnzU7CDH3eX-OjmkcU4nqtq3rcJEx7FTIkshHTDIskHVSXNfdQlUD8NVfBvTk5sjNRDQSwZOt6cUj3VpgzYTVsBCTJv6uho47e4Ev5M-9mvjVkIshzbokjVamhdi0aWZ_ZCGHUYy89l2Ol-lSnmdSl2mVZeOBl6HRHQpO2JO0nYM02Okl-KQ5QwPwCzXAft-C-GVde_783wHNJPSbEjeFoXAXRhP3Pk_8nOx4H6mCShwbDtkdY4wp_sXO21QLjmDj1thUxBJYDjMMArqXKX22U4hf45R5LdkbUDvqqDvGXHq5Y0JwNZfWkoKbL3p_ch7xOMHgh0FeH8UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mPnzCOtsvaSP6naNeXSWy1gK0bOXITVeQxPUsl_BplaFZAwTIzrOd4Y-nGiiczHS1rGZxM-EzqIP-q2oR9lwX2p3vgdsuXhvOb_r_QcpTBQodNBdaEW22kmx9N0H-tTld_eOYKdVgJEgEccpfdROrNhvbHx-VaMxP0e0tzF6THIfySYRrLRNc0sc1KrpvfDds-MDyvMC7UvKT6JsS_tnruA1X6IMhUFicsKInHqb_7GKK3uFtngvW_UZN6hBbZSjhu-vWzVFPQj15Tw08QPNVlnTQcCKEE2b3_3GbbhGOfIj4IQ4SMdZrLZSMpwAoi4lRvZmEQV8agtG5hxuYYE4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fhXUHghMcVRcSjufQdBrocEerz0IKsXBmzkZng1D2u9n0FJXLVmMOxMvbLp4xu-gRM2QpzzC0l9fQfZt8R-kTAEqpUjMV7xs9vBklNDlpT75gFH0bMEiA0wN6rwyf4Nogm3MP0Al6n8bqglosaBUj952-tZ5FBUKpX37N_j1ueYFNV5o-AYUePwx-wUpIkidbFm-BlB3hpBmF0QaPTznAXanVHgs509oc3v1ucAvHU-EEcVFYdij4CavcZ7tcAe7UH6ia-E5VmO9cd9_Jq4u14TwO34l5PT0xXYEjGzY1jlWlXMVwix_FWw2o8ueiZqn9PjEWrKkZ22HxLixY7p6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlUxRe1OT2pNMuZF2DqRFLmu09qEpWU1kkBUrZDiyKwOtCtEZh643tJ01UjJ-MuC11mdogxFCuFOAyZNTDAbsB1keylWgQ6cqV3hodQEYC0rttZvxsy-D5ahLV9t0xd4OpRwOo4kDF0JO2gqCp6VZzohl-ps35moy4CbIa_U71J2JEXz8d6jynlxvdNZPo2YYoz4B1_LYD06axzchAt-uwmJrqrM1v8UAXR7Bjqd0mjyxwMXPM2HKlcJqNbEmeR1ZA5NgVQik5C99DeDN8vbAKjzqG5q-H_gfT6-tF6a9PS2k19e8jUjye3G0Qgm4ePVzb7wdE0QNQzmINoBuYAxuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EM-ZVFVyeGTdOaRwAdYpGm0j_vhkCUUvovgfgvlYkM3gsyzOQ9tvGApKT_fTfIun-KYKn7UvJtkzyUFe8lM69tomI2JbD-dYbK6wYV4jnlpa9oa_62PLjWZYAl9oxlhZYxkxVpWrpgasXGLETyLbvDP-xUuKAQoNgpPUh_vxlqDQK9DcCaRcor1CeyFvTK7sMgWiC77-mN4wzjsUb59rTnypWhKWGAOtWt5dXR5fMIMogJKmMu9zW7A2IWAAlE2IT-d7y4akLgnpaB9V_tqL-zBandmuIeVzhrowjlYAZlhTrB7mU1V9UImvuAqrI3pMzqd7TL7lnBr0aH3cXUJDnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد عاصم منیر، رییس ستاد کل ارتش پاکستان، پیام‌های آمریکا را به تهران منتقل کرده است و بخشی از این پیام حاوی تهدید به ازسرگیری جنگ بوده است.
در این پیام‌ها همچنین تاکید شده در صورت موافقت جمهوری اسلامی با توافق، حل مسائل اختلافی در مرحله بعدی انجام خواهد شد.
به گفته این منابع، آمریکا در پیام‌های خود تصریح کرده است تهران باید اکنون با توافق موافقت کند یا با پیامدهای منفی روبه‌رو شود.
@
VahidOOnLine
شبکه العربیه،  روز شنبه دوم خرداد ماه، به نقل از «یک منبع بلندپایه ایرانی» گزارش داد پیشنهاد ارائه‌شده از سوی تهران تاکنون نتوانسته رضایت آمریکا را جلب کند و همچنان از دید واشنگتن «غیرقابل قبول» تلقی می‌شود.
@
VahidOOnLine
عاصم منیر، رییس ستاد کل ارتش پاکستان، پس از سفری یک روزه به تهران، ایران را ترک کرد.
به گزارش ایرنا، او به همراه محسن نقوی، وزیر کشور پاکستان که از هفته گذشته در تهران به سر می‌برد، پایتخت ایران را ترک کرده است.
عاصم منیر در جریان این سفر با محمدباقر قالیباف، رییس مجلس، مسعود پزشکیان، رییس‌جمهوری ایران و عباس عراقچی، وزیر امور خارجه دیدار و گفت‌وگو کرد.
@
VahidHeadline
محمدباقر قالیباف در دیدار با عاصم منیر گفت نیروهای مسلح جمهوری اسلامی در دوران آتش‌بس بازسازی شده‌اند و در صورت آغاز دوباره جنگ، واکنش ایران شدیدتر خواهد بود.
او گفت: «نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ‌تر از روز اول جنگ خواهند بود.»
قالیباف با اشاره به نقش پاکستان در میانجی‌گری افزود: «در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است.»
@
VahidOOnLine
شیخ تمیم بن حمد آل ثانی، امیر قطر، روز شنبه دوم خرداد ماه در تماس تلفنی با دونالد ترامپ، رئیس‌جمهوری آمریکا، آخرین تحولات و رویدادهای فوری منطقه را بررسی کرد.
بر اساس بیانیه رسمی دیوان امیری قطر، این گفتگو بر «تلاش‌های منطقه‌ای و بین‌المللی برای حفظ آرامش کنونی و کاهش تنش‌ها» متمرکز بوده است.
«امنیت دریانوردی، حفظ ایمنی آبراه‌های راهبردی و تضمین تداوم روان زنجیره‌های تامین جهانی و انتقال انرژی» از دیگر محورهای این گفتگو توصیف شده است.
به گزارش رسانه‌های قطری، امیر قطر در این تماس بر موضع ثابت دوحه در اولویت دادن به راه‌حل‌های مسالمت‌آمیز برای بحران‌ها تاکید و اعلام کرد قطر از همه ابتکارهایی که با هدف مهار بحران‌ها از طریق گفتگو و دیپلماسی انجام می‌شود، حمایت می‌کند.
این خبر در حالی منتشر می‌شود که رسانه‌ها از گفتگوی تلفنی وزیرامورخارجه قطر با عباس عراقچی خبر داده‌اند.
همزمان گزارش‌ها از رایزنی‌های گسترده کشورهای منطقه برای جلوگیری از حملات احتمالی آمریکا به ایران خبر می‌دهد.
این در حالیست که شبکه خبری العربیه پیشتر از هشدار واشنگتن به تهران مبنی بر از سرگیری حملات به ایران خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/VahidOnline/75635" target="_blank">📅 17:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75634">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAbMC8ITfufPtXqeNW3kpQYaHqoogtEdllLmVv47XoDeK4vwleECVspXuqER8wuVWJjBESf8olDxagz4Pgg6BZ0PTCZywRt51uhazyVxLp7mlNLKwCWf5TXcpmYXpaWHjEAU_q68gzkyatXIkxIDPg5qxJ0Pm-PuapfE_Pdi1WnJgp214RtjMoKo6a0aQ-Q9Ggizm03wO8ma7lEisxWRk1eQVu0XX68kNzJ2FPhqXa6jZ9kHMa-Bub7u1njnCetZseX0magXzxyURJiVedGy1fDu7dVoM7QPGPutdWc4W9MOKAjMi4sRWJKNrAnvF0AmYK3lOkseQ1N27lTTs3yR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان هواپیمایی ایران اعلام کرد این سازمان هیچ اطلاعیه رسمی هوانوردی جدیدی درباره اعمال محدودیت در آسمان کشور صادر نکرده است و شرایط پروازی عادی است.
او با تاکید بر تداوم وضعیت عادی پروازها گفت: «شرایط آسمان کشور همچنان مانند روال گذشته است و پروازها طبق برنامه انجام می‌شود.»
سخنگوی سازمان هواپیمایی بدون اشاره به جزئیات اطلاعیه هوانوردی (نوتام)، افزود: «نوتامی که اخیرا در فضای مجازی منتشر شده، تکذیب می‌شود.»
سازمان هواپیمایی کشوری ایران روز جمعه یکم خرداد در اطلاعیه‌ای اعلام کرده بود فعالیت فرودگاه‌های واقع در بخش غربی محدوده پروازی ایران، موسوم به «FIR تهران»، تا دوشنبه متوقف شده و تنها شمار محدودی از فرودگاه‌ها مجاز به فعالیت هستند.
بر اساس آن اطلاعیه، فرودگاه‌های ارومیه، کرمان، آبادان، شیراز، یزد، کرمانشاه، رشت و اهواز از این محدودیت مستثنی شده‌اند و فعالیت آنها نیز فقط از طلوع تا غروب آفتاب مجاز اعلام شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75634" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRzyol9L3zK14MTupd_aLk4VRO-rqxZFkwGwpKmqUeg5CGGZnCrkPKMGzUERLKHy1fSh5REEuUtpyRhNBp-MkucGMevw_-MlaC-XSpOUW7Z8mcY31CESBZ1kjsekbZkcy_7OrcvPAwY5AiUyVkD5_WOFIB--m1i8hZeP8HlbqpntFUUZUvYSZ3WTgJefbfTHnAHlDZ_-kZ_N_srlCWmaWfpZrRrpP5jgtru6itNJJOAOV_lNvh76dcKMGVMN_cU62zxMoIe3dTJSue4sECFqRyN9xzvYG4pqkYEDN3XA5ZZR1Fe_fZUc3Npp2Jo1PpAJ0hRMw0NBo1msrxIRJuuZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از دیدار فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان با عباس عراقچی، وزیر امور خارجه ایران در شامگاه جمعه یکم خرداد خبر دادند.
بر اساس این خبر، دیدار این دو مقام تا پاسی از شب ادامه یافته و محور گفت‌وگوها «تلاش‌ها برای جلوگیری از تشدید تنش و خاتمه جنگ» و «راهکارهای تقویت صلح، ثبات و امنیت در منطقه غرب آسیا» بوده است.
جزئیات بیشتری از این دیدار منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75633" target="_blank">📅 08:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1iSAkNAL2tM6dnEg_Mref-33O6j9m9r4jt_zi6XnUlpwOq7In2nUytSAiyvTI33m_JcLtQo6R5H53Btn6tz1ujQsMcRq9XmJ8ozZq5DAKpBey4hWXwFSGWuPGgOn0eRqQIbI0NVE8_EElNPgPTgziSeZRxrWPDfLkkPJijuirCUvWqhhoLAPMVvC8TkSVpN_oO8wqwefVdXhjr0rqiO3MoJYYxwAjnRExZnzZSTDrOU0Tq3-tiHPho4GsqaqszGXJCbdi2i1KNxzWzfxuHtN48_5codn7PbwZ6Oopf0yLUpr2Tu_ACbfGEl_cMj67EzShmk_qz9t0IJenkAJ6FfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ اعلام کرد که سیاست‌های مهاجرت به آمریکا تغییر می‌کند.
در یک تغییر اساسی در سیاست‌های مهاجرتی آمریکا، دولت این کشور اعلام کرد خارجی‌هایی که قصد دریافت اقامت دائم یا همان گرین کارت را دارند، باید خاک ایالات متحده را ترک و از طریق کنسولگری یا سفارت آمریکا اقدام نمایند.
زک کالر، سخنگوی دفتر مهاجرت دولت آمریکا، گفت که این سیاست «نیاز به یافتن و اخراج» کسانی را کاهش می‌دهد که درخواست اقامتشان رد شده است.
از سوی دیگر وکلای مهاجرت و گروه‌های امدادی می‌گویند که این تغییر احتمالا به «جدایی بیش‌ازپیش خانواده‌ها» منجر خواهد شد و قربانیان قاچاق انسان هم مجبور خواهند شد «به کشورهای خطرناکی بازگردند که از آن گریخته‌اند.»
این تغییر سیاست تازه‌ترین اقدام آقای ترامپ در محدود کرد مهاجرت به آمریکا است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75632" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucfgQaOyAOEnSC3D2VPuIVBEcmVU3KssSbNUBH1N_yjZo4WCrXg_-EJqBYEij_xESR9VGzMU3lQlx4ORo018627Pc2HRpw1-EMg7fl9HgZolV-PtVd27f1E8WRYFJjWoIHWbSde9ZW5XSl8q_dlyD9iiQ2EwCcXtvGgB30_1FjCznLUHmHyti-X_mJ_KihsPbeJpx7diQGTdAHqm8qVCi41AAGzFpymfAeCXdeZe3Qku1Yecz0eTisC2ZXdqiIBlBW4tHcqdyT5LGG5u4px-KO1KtB29zsW4pZgjR7VoZZ1GlliK8MDLKy-4m07CskER7NBk495DfgFoYIGku0bDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «نیویورک‌پست» به نقل از منابع آگاه افشا کرد که ایوانکا ترامپ، دختر ۴۴ ساله دونالد ترامپ، هدف یک طرح ترور پیچیده از سوی یک تروریست تحت آموزش سپاه پاسداران انقلاب اسلامی قرار گرفته که با انگیزه انتقام‌جویی از کشته شدن قاسم سلیمانی طراحی شده بود.
بر اساس این گزارش، متهم که یک تبعه عراقی ۳۲ ساله به نام «محمد باقر سعد داوود الساعدی» است و به تازگی دستگیر شده، عهد کرده بود برای «به آتش کشیدن خانه ترامپ»، دختر رئیس‌جمهوری آمریکا را به قتل برساند.
منابع اطلاعاتی اعلام کرده‌اند که الساعدی حتی نقشه و جزئیات معماری عمارت ۲۴ میلیون دلاری ایوانکا ترامپ و همسرش جارد کوشنر در فلوریدا را در اختیار داشته و پیش از این با انتشار تصویری از موقعیت این خانه در شبکه اجتماعی اکس (توییتر سابق)، به زبان عربی تهدید کرده بود که «نه کاخ‌ها و نه سرویس مخفی آمریکا» نمی‌توانند از آن‌ها محافظت کنند و انتقام تنها مسئله زمان است.
وزارت دادگستری ایالات متحده اعلام کرده است که الساعدی از مهره‌های بلندپایه در حلقه‌های تروریستی وابسته به ایران و کتائب حزب‌الله عراق به شمار می‌رود که در تاریخ ۱۵ مه در ترکیه بازداشت و به آمریکا مسترد شد. او در ایالات متحده با اتهاماتی سنگین پیرامون هدایت و اجرای ۱۸ حمله و تلاش برای ترور در سراسر اروپا و آمریکا مواجه است؛ پرونده‌ای که شامل بمب‌گذاری در یک بانک در آمستردام، حمله با چاقو به دو شهروند یهودی در لندن، تیراندازی به ساختمان کنسولگری آمریکا در تورنتو و آتش‌سوزی عمدی در معابد یهودیان در بلژیک و هلند می‌شود.
این متهم که به دلیل وابستگی به قاسم سلیمانی او را مانند پدر خود می‌دانست، پس از کشته شدن سلیمانی در حمله پهپادی شش سال پیش آمریکا در بغداد، تحت آموزش‌های نظامی و اطلاعاتی ویژه سپاه پاسداران در تهران قرار گرفت و ارتباط نزدیکی نیز با جانشین او، سردار اسماعیل قاانی، برای تامین مالی شبکه‌های تروریستی خود داشته است.
اطلاعات فاش‌شده نشان می‌دهد الساعدی با وجود نقش برجسته‌اش در شبکه‌های تروریستی، حضور بسیار فعالی در شبکه‌های اجتماعی نظیر «اسنپ‌چت» و «اکس» داشته و تصاویری از رایزنی‌های نظامی خود با قاسم سلیمانی را نیز به اشتراک گذاشته بود.
او با تاسیس یک آژانس مسافرتی مذهبی و با سوءاستفاده از یک «گذرنامه خدمت عراقی» که سفر بدون تشریفات امنیتی و اخذ آسان ویزا را برای او ممکن می‌ساخت، به راحتی به کشورهای مختلف سفر کرده و با گروه‌های تروریستی ارتباط می‌گرفت.
الیزابت تسورکوف، پژوهشگر انستیتو «نیولینز» که خود ۹۰۳ روز در اسارت کتائب حزب‌الله بود، تایید کرده که روابط الساعدی با سلیمانی و قاانی فرصت بزرگی برای گروه‌های شبه‌نظامی عراقی ایجاد کرده بود. الساعدی که در زمان دستگیری در ترکیه در حال سفر به روسیه بود، هم‌اکنون در سلول انفرادی بازداشتگاه متروپولیتن بروکلین، در کنار دیگر زندانیان سرشناس نگهداری می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75631" target="_blank">📅 04:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK-VZ80ZLLyY7vsH0LTMMfxaIafVZp62BwhrqW_o-cVDTJP8KnWQv-rgqLh9LL3Ec1w5QB13UzZXdOL3-oklTJxN8Tbun13i59Xd_h0JnV0whSUxF43WCkJ7suUrXuurMwPSDikVbJweq_NptqWUK1bDwRotOhLenUL9d8wRCBY0-thMh_VlMcX1a3dQqQXWRAOTFGxrSin6FCcsb22fwQBduOTC0rSFaMjxtiypqIfunxPIFg0OfdUP_sDK2xfP4Opb3YuYn6P4sgYxvg6_qMzIIQzFfPyw9Ne4Cyh01mcMhg52oC3zaMrLBuLNUb6w7kiCVpoqDcWn610dQEXfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس گزارش داد که آمریکا در حالی خود را برای دور تازه‌ای از حملات نظامی علیه ایران آماده می‌کند که تلاش‌های دیپلماتیک همچنان ادامه دارد.
به گزارش سی‌بی‌اس نیوز، منابعی که مستقیم در جریان برنامه‌ریزی‌ها قرار دارند می‌گویند که دولت ترامپ روز جمعه در حال آماده‌سازی برای حملات تازه بود هرچند تا عصر جمعه تصمیم نهایی گرفته نشد.
آقای ترامپ در پیامی در شبکه‌های اجتماعی اعلام کرد که «مسائل مربوط به دولت» مانع از حضور او در مراسم ازدواج پسرش، دونالد ترامپ جونیور در روز شنبه خواهد شد.
او قرار بود تعطیلات آخر هفته را در مجموعه گلف خود در ایالت نیوجرسی بگذراند، اما اکنون به کاخ سفید بازمی‌گردد.
چند منبع نیز گفته‌اند که برخی اعضای ارتش و جامعه اطلاعاتی آمریکا برنامه‌های تعطیلات خود را لغو کرده‌اند؛ اقدامی که در انتظار احتمال حملات تازه انجام شده است.
به گفته این منابع، مقام‌های دفاعی و اطلاعاتی آمریکا در حال به‌روزرسانی فهرست نیروهای آماده‌باش در پایگاه‌های خارج از کشور هستند؛ همزمان با خروج بخشی از نیروهای مستقر در خاورمیانه، در چارچوب تلاش برای کاهش حضور نظامی آمریکا در منطقه و نگرانی از واکنش احتمالی ایران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75630" target="_blank">📅 04:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgk3yIYrz6U-s4xHilckciWrx1GglvxijDvCngXe3g7zPuDPyXejXrSk4zWIVQJRjTGQTX-W5S9kJhYT-3zBDg9pY6XWD5dqGvq1dFVJaik-NPvXJTD4bubJ08p7HOu-8lruQoTQGCqi0qyFWwWQLV0PR4nBRrdFTAcopTHZwP5pyFHkugXcT26UqWhM4OmaaSRQy5cnXUr2EQYkNyJHa5Kh2wcUD90AicLz-WHzQrW1aA9s0zh0AArdsmNQBpzQneeraiujnQdc-Q62aHz_eWsq1ard-1HPR46Pj2r6rAGqq6zDIIWo6zfAPLcSiAzGvPOK7P9xVoDcA6h03wJlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه با تیم ارشد امنیت ملی خود در کاخ سفید دیدار کرد تا سناریوهای مختلف در صورت شکست مذاکرات و احتمال آغاز حملات جدید علیه ایران را بررسی کند.
در این نشست حساس که با حضور مقامات کلیدی از جمله جِی‌دی ونس، معاون رئیس‌جمهوری، پیت هگست، وزیر جنگ و جان راتکلیف، رئیس سی‌آی‌ای، برگزار شد، ترامپ در جریان آخرین وضعیت دیپلماسی قرار گرفت.
نشانه‌های جدی از تغییر برنامه آخر هفته رئیس‌جمهوری، از جمله لغو سفر به باشگاه گلف بدمینستر، بازگشت به واشنگتن و حتی عدم شرکت در مراسم عروسی پسرش، دونالد ترامپ جوان، نشان‌دهنده وضعیت اضطراری در کاخ سفید است.
منابع نزدیک به ترامپ می‌گویند او از روند کند مذاکرات ناامید شده و به سمت گزینه نظامی متمایل شده است، هرچند هنوز تصمیم قطعی برای از سرگیری جنگ اتخاذ نشده است.
در همین حال، تهران به کانون تلاش‌های دیپلماتیک «لحظه آخری» برای جلوگیری از شعله‌ور شدن دوباره جنگ تبدیل شده است.
عاصم منیر، فرمانده کل ارتش پاکستان، به عنوان میانجی اصلی، در سفری حساس وارد تهران شده و قرار است با احمد وحیدی، از فرماندهان کلیدی سپاه پاسداران دیدار کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75629" target="_blank">📅 00:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE2W-IyBM_1Yw4UiHO7IMi-QE1r2mELCEZK2p6sDremfLtgIa0R2NZpXTewPlJE3o31hDTPHmrGq4gWoASJsLEqfMVlydQXYUpkue5e-TKQyGMXuotAPXbk_Z8A9VulyFpmWODW3XiqzBb4Se2lNrf6a8tvtvkU0ww-tO9oCq1zOlk4CkZxA12NfSnq-OT1spDLSG4D64rjQ6fj2PxztKEkRNq0jHsG7GiQ4dsDsB5adfD9skqHhpbLR02j3Vi3XUUydS_Mr-razNz6d_25W822pqDJwZIgYSQM4P3_xaNHnjAj_lc55GIS6jyJTLKlI4PqJhQAxKO2ETosuKOJwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع نزدیک به ترامپ نوشت که رییس‌جمهوری آمریکا در روزهای اخیر به‌طور فزاینده‌ای کلافه شده و احتمال انجام یک عملیات نظامی نهایی و گسترده را مطرح کرده است؛ عملیاتی که پس از آن بتواند اعلام پیروزی کرده و به جنگ پایان دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75628" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuNsq8O9g73Q-CGS0G3LZl6l0hAkcwI1_f4JGm5WNmblMh3bjOaJGI4YOmwtNdw3jdm6d4yHDKT9mjQiMN8qOJP8AaMvl9Zn-QL6GhiO9CGbzuVVDvALLjYiVsGOMyzJXAonkscHTBVvnDi0wZv2t0voyq-y-d64rmhNpUOsFeR0eIy59ZrW6oNCOZA2X-FKP4a4foEaV4i5NKYzzqytPK3nxB6RqKjsM_5-nA_3iH_muQwZqNTsGG7xqPaxiXSyADWCAgU9q1uokHeUEATvikp-xjFCkdEtSAZYdjQiUFLVB3cdVcV74YBW3sDYLs4B6NcthGcXZoeEeaf0FfOkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت مذاکره‌کننده ایران با آمریکا روز جمعه گفت که موضوع پرونده هسته‌ای ایران در این مرحله مورد مذاکره نیست و از اختلاف نظر عمیق با آمریکا خبر داد.
اسماعیل بقائی گفت: «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
او گزارش‌ها درباره قریب‌الوقوع بودن توافق با آمریکا را رد کرد و اعلام کرد: «نمی‌توانیم بگوییم ضرورتاً به جایی رسیده‌ایم که توافق نزدیک است.»
بقائی بار دیگر موضع جمهوری اسلامی درباره برنامه هسته‌ای و اورانیوم غنی‌شده را تکرار کرد و گفت مواضع ایران قبلاً اعلام شده است.
@
VahidHeadline
سخنگوی وزارت خارجه ایران حضور هیئتی از قطر را در تهران تایید کرد
اسماعیل بقایی،‌ سخنگوی وزارت خارجه ایران تایید کرد که یک هیئت از قطر روز جمعه در تهران بودند و با عباس عراقچی وزیر خارجه ایران گفت‌وگو کردند.
او بدون ارائه جزئیات گفت که کشورهای مختلفی طی روزهای اخیر با وزیر خارجه گفتوگو کردند اما تاکید کرد که میانجی اصلی میان ایران و آمریکا همان کشور پاکستان است.
پیشتر رویترز به نقل از یک منبع آگاه گزارش داد که هیئتی از قطر در هماهنگی با آمریکا وارد تهران شده است.
قطر و امارات و عربستان سعودی سه کشوری بودند که آقای ترامپ روز دوشنبه گفت که به درخواست آنها فعلا حمله مجدد به ایران را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75627" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEOTVpjjIBiIS029a89Emzm2SqDWolDBzIGXxsvTcXMnvapoaVpoDAdM7-agJQrYD8ppNafJ9AaLNHXhMjthx_ySz796LkxhQ5OGNMt6mvk7W6TweR22b_GxBCTgb2hPHzS_2bZKYa_oAHEZpetq7RVRsBvhzna0aJK4f9PD8zetP761Fn9r-fp2nBAdM-zDBgYQUKiAoINH9dcz5jpnkFLRPCMYBpx-WE0Xh9lZSYbtgoFEaNx6auQvl0DzhfG-OeS5avut_jzP2KchvfnPjCRrJKHEGyhtDEh4pMsHViHIwafxHllQgoxoUIZ514fUQfqj2LvpN6UR-7L9-UfH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از عاصم منیر، فرمانده ارتش پاکستان که امروز جمعه یکم خرداد۱۴۰۵ وارد تهران شد و مورد استقبال اسکندر مومنی وزیر کشور قرار گرفت. خبرگزاری آسوشیتدپرس پاکستان نیز به نقل از منابع امنیتی اعلام کرده‌اند که عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75626" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o1vVxbRbRh--TMhGblvYd-b61LXKW0528wwJ3xkjUzRmHKTZKQrJ7MWu9nmEiPE-PwtkkA5n2z8hSJ_leW-GD3vflzsOCFvxXXWfK6yUD2taGWURVQOn7HQ9KMeqQnOLzy1xgwXqKv9gH8kbPBbs_MvN6hXoHkLCKBdezpFgCPzKKEA6Y6IHQmKPmlsgLmZGf5nFcNE5JFiz0Dj8dPCzPIMGI_wg7sHwSBOTy3VHwjhVj8g2b3JJW498CXHiNws0iwxMo9FDdmqs-S3Akc4sMQxqHEzDQfMAoLub48E9ueExF2sYVAK2Dk55DdSP2ADvzVfn9PKiF9Zi4jmp42qyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فاکس نیوز»: تولسی گابارد از پست خود به عنوان مدیر اطلاعات ملی آمریکا استعفا کرد.
AlArabiya_Fa
پست ترامپ، ترجمه ماشین:
متأسفانه تولسی گبرد، پس از آنکه عملکردی بسیار خوب داشت، روز ۳۰ ژوئن دولت را ترک خواهد کرد. همسر فوق‌العاده او، آبراهام، به‌تازگی به نوعی نادر از سرطان استخوان مبتلا شده و او، به‌درستی، می‌خواهد در کنار همسرش باشد و در حالی که این نبرد دشوار را با هم پشت سر می‌گذارند، به بازگشت او به سلامتی کمک کند. تردیدی ندارم که او به‌زودی بهتر از همیشه خواهد شد.
تولسی کار فوق‌العاده‌ای انجام داده و دلمان برای او تنگ خواهد شد. معاون اصلی و بسیار محترم او در دفتر مدیر اطلاعات ملی، آرون لوکاس، به‌عنوان سرپرست مدیر اطلاعات ملی خدمت خواهد کرد.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
از سوی دیگر رویترز به نقل از یک منبع آگاه از موضوع، نوشته که او ادعا کرده کاخ سفید خانم گابارد را برای کناره‌گیری «تحت فشار» قرار داده بود.
پیشتر اختلاف دیدگاه‌هایی بین رئیس‌جمهور ایالات متحده و مدیر امنیت ملی‌اش، بخصوص در قبال ایران بروز کرده بود. دونالد ترامپ در فروردین‌ماه هم اشاره کرده بود که از نظر او، تولسی گابارد در قبال برچیده‌شدن بلندپروازی‌های هسته‌ای ایران، «موضع نرم‌تری» دارد.
خانم گابارد بیش از یک سال پیش، پنجم فروردین‌ماه ۱۴۰۴ به کنگره گفته بود که ایران در حال ساخت سلاح هسته‌ای نیست.
مدیر اطلاعات ملی آمریکا که برای ارائۀ گزارش سالانۀ نهادهای اطلاعاتی ایالات متحده به همراه رئیس سی‌آی‌ای و مدیر اف‌بی‌آی در جلسه استماع سنا حاضر شده بود، تأکید کرد که بر اساس ارزیابی نهادهای اطلاعاتی، علی خامنه‌ای رهبر وقت جمهوری اسلامی، درباره تعلیق برنامهٔ تسلیحات هسته‌ای ایران، که در سال ۱۳۸۲ فرمان آن‌را صادر کرده بود، تجدیدنظر نکرده است.
با این حال خانم گابارد بعد از مدتی، موضع‌گیری خود در این زمینه را تغییر داد.
تولسی گابارد که مسیر سیاسی پرفراز و نشیبی داشته، پیش از پیوستن به حزب جمهوری‌خواه و ورود به دولت دوم دونالد ترامپ، عضو حزب دموکرات و نمایندۀ هاوایی در مجلس نمایندگان بود.
او هفت سال پیش، زمانی که خود را برای رقابت به‌عنوان نامزد حزب دموکرات در انتخابات رباست جمهوری آماده می‌کرد، گفت که در صورت پیروزی در این انتخابات، ایالات متحده را به توافق هسته‌ای با ایران باز خواهد گرداند.
خانم گابارد در آن زمان در گفت‌وگو با شبکه تلویزیونی فاکس‌نیوز هشدار داده بود که ایالات متحده در آستانه جنگ با ایران قرار دارد.
تولسی گابارد نخستین و تنها مقام ارشد امنیتی یا نظامی دولت دونالد ترامپ نیست که کناره‌گیری کرده یا وادار به کناره‌گیری شده است.
در آخرین روزهای سال ۱۴۰۴، جوزف کنت مدیر وقت مرکز ضد تروریسم آژانس امنیت ملی آمریکا، که مستقیماً از سوی دونالد ترامپ منصوب شده بود و زیر نظر تولسی گابارد انجام وظیفه می‌کرد، در مخالفت آشکار با جنگ ایران، کناره‌گیری کرد.
@
VahidHeadline
خبر یک ماه و نیم پیش:
ترامپ قصد داشت گابارد را اخراج کند
به گزارش وب‌سایت آکسیوس، دونالد ترامپ تا آستانه اخراج تولسی گابارد، مدیر اطلاعات ملی آمریکا، پیش رفته بود، اما مداخله لحظه آخری راجر استون، مشاور قدیمی و نزدیک او، مانع از این اتفاق شد.
دلیل خشم ترامپ به شهادت اخیر گابارد در کنگره بازمی‌گردد؛ جایی که او برخلاف انتظار، از جنگ با ایران حمایت تمام‌عیار نکرد.
طبق گفته منابع آگاه، ترامپ از اینکه گابارد در اظهاراتش اعلام کرده بود برنامه هسته‌ای ایران پیش از آغاز جنگ «منهدم» شده بود (موضعی که توجیهات ترامپ برای حمله را تضعیف می‌کرد)، به شدت ناراضی بود.
همچنین استعفای اعتراضی جو کنت، دستیار گابارد که جنگ را غیرضروری خوانده بود، بر آتش خشم ترامپ افزود.
در حالی که ترامپ در حال نظرسنجی از مشاورانش برای جایگزینی گابارد بود و وفاداری او را زیر سؤال می‌برد، راجر استون در تماسی تلفنی از او دفاع کرد. یک منبع نزدیک به آکسیوس گفت: «راجر معامله را جوش داد و تولسی را نجات داد.»
استون نیز بعدا در شبکه اجتماعی ایکس تایید کرد: «خوشبختانه به موقع اقدام کردم.» با این میانجی‌گری، گبرد فعلا در سمت خود ابقا شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75625" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfgX4cNk4mIrYr0Wj_R_no_Fyo8zBJv3s2Y6HyGWE5CFH3arPpFU5X3WBkPpN2YKRpHTeSvXCxuvn7VdHR3HQvDk5QRSaGkUFR5a3S9R4Ldhe4yTke4W4oDXGtJdyVzWgKdoMP2CfOTJ78GNMKN-wGbz92WlE4jn_0egbuW4DCMgNgabxWKmaSOfDbhn5MlBCBqBMz2xzSdVq5NnWKX9UdU_EG1_tizwEuMu1yzBoyJ9ebWTjJO3TMYDUhw7XI6OM_d9AvUiCcnHW2ySpPDJQcuHAMW4J_aUoSaAo8s2WV9wtgLqsO-cJNfKszwUmIyp3LxYvmzHCz-oNkOQm_DrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست
ترامپ درباره شرکت نکردن در مراسم ازدواج پسرش
ترجمه ماشین:
با اینکه بسیار دوست داشتم کنار پسرم، دان جونیور، و جدیدترین عضو خانواده ترامپ، همسر آینده‌اش بتینا باشم، شرایط مربوط به دولت و عشق من به ایالات متحده آمریکا اجازه چنین کاری را به من نمی‌دهد.
احساس می‌کنم مهم است که در این دوره مهم زمانی، در واشینگتن دی‌سی و در کاخ سفید بمانم.
به دان و بتینا تبریک می‌گویم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز:
ترامپ با اشاره به مشغله‌های شدید خود گفت: «به پسرم گفتم الآن زمان‌بندی خوبی برای من نیست؛ موضوعی به نام ایران و مسائل دیگر را در دست دارم. این از آن مواردی است که اگر در عروسی شرکت کنم، توسط رسانه‌های اخبار جعلی سلاخی می‌شوم و اگر شرکت نکنم هم باز من را می‌کشند!»
@
VahidOOnLine
رسانه‌های امریکایی نوشته‌اند که دونالد ترامپ جونیور، ۴۸ ساله، قرار است در پایان هفته جاری با بتینا اندرسون، مدل و چهره اجتماعی ۳۹ ساله در یک جزیره خصوصی در باهاما ازدواج کند.
بر اساس گزارش‌ها، این زوج در ابتدا به برگزاری مراسم عروسی در کاخ سفید فکر کرده بودند، اما بعداً تصمیم گرفتند مراسم کوچک‌تری برگزار کنند. دلیل این تغییر، نگرانی از واکنش عمومی به برگزاری یک مراسم پرزرق‌وبرق در زمانی خوانده شده که امریکا با تنش‌های مربوط به ایران روبه‌رو است.
afintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75624" target="_blank">📅 20:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rr7wyK_KCpkbVNdgBJf38k5Ce3MbA4YcTO4SYPnAgZWl0yqtvFVWCIIJbUMr8vqYB7DxSt8WjNKhb4VtDlxIEo0429eJ1z7-E5tbavo94ROtOuRWmNgwwYdtUDz8n8uK5-1vRg8cXomJcbGdbFnZ13ZMRQdgWMXylx3PwWrDQLUgCUdgGXIkZQK6IKKqEg5Nc8HKRwhccgiLAJYN-j9imtIlg-n8Upl20-X7wIRuBSk39e3ap-RdDTLd7fMVIOcQH2Gb2AToNL8rNI7BANH-fU_XgK9bVszGtxkkfH2P93M9nPBPj4IvdneAi_ufV35ShDBU0j6FrPHw0O929PYyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkStVXPS6rha_DXrznEveryAvJ9Jie6sH0lkOzJt9rdnO5dQhI1iMxO32VVlqYlwlflNdQOdYKyA7SQeYqOKBxLS5qPudt9Rs60DksMMI_BXLivfZUFuMrU2WwluP1btAA-e5eBP3utHzMyg_TW49quzu93bNy1kEIoxSM0e2_yrS5wCezqp2Mnwl3UrkM2bdzLkzY4S25fr59Yg9iXu3hCWK4B-EO9hEEeSwIFPu6xH-q1qV0XSVhEfkoO87RXwOUi962ShsSe8oJvp7bypCtu2F5s6zBI6qtJrlNBG_2wNHHcB9quYXRWqoZlrkFmh79UG44sHHUjHJweRqxZAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCb1FswRejKIoknuwC1pcCjp3OGH27dmZVMAQiyqv002SPfeGcaLBRnG0hULwUBKOsvIl-wgvLObck8tcDXU6KRoZP2ryGrdWhE0CW3fKEt_cRTo0Q9ch7Ccuc6SC3nWmrUsuvumOKPBRrnMgQx5zb8Qw7h_H30h5DbsLs3Q6lFp5Cj6AVGYub5yhjlNi04GJVfzzehl6Nl3kqV8jzAWu3VvcFkKYUsTeAq2W7EPdOwM-tv_p9ydoVVoC50uoQv_4Rq13vKcyEwDN65q3KhN32VPZoOfBN5wlLYU3sMUdqFEwKCuEemEtAWplYzxvJhOY-UDPyjywTDp_L4ucVb9VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند تا کنون ۶۵۵ مورد اعدام را در سال ۲۰۲۶  ثبت کرده است، که ۳۴ مورد که از آغاز ماه می تاکنون اجرا شده است.. آمار واقعی احتمالاً بسیار بیشتر از این رقم است. جمهوری اسلامی در حالی این اعدام‌ها را پشت درهای بسته اجرا می‌کند که  ۸۳ روزه است که اینترنت کشور قطع شده است. حاکمیت با قطع ارتباط جامعه از ۹ اسفند ۱۴۰۴  صدای زندانیان، خانواده‌ها و شاهدان عینی را به شدت سرکوب کرده و نظارت مستقل بر وضعیت حقوق بشر را به‌طور خاص دشوار ساخته است.
🔸
از آنجا که دستگاه قضایی همواره تنها بخش کوچکی از احکام مرگ خود را به‌طور رسمی اعلام می‌کند، قطع اینترنت داده‌های فعلی را به شدت محدود به منابع دولتی ایران کرده است. بنابراین کاهش در آمارهای ثبت‌شده، تنها نشان‌دهنده خفقان اطلاعاتی است، نه کاهش کشتار.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75621" target="_blank">📅 18:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ADAfuHF9kzAQg-F5y-Mtrr-Euxa6TzBXPU0vPxW_xuqoVHQFBvvLnHd_3sUt0i44Uq3Igk4o0bKFU6jSJyiDSBsWZvayhW4IkeShWNU9EndzCd64bw3gaEzXeZku3j-AYpQbi1Gn6g-95bACfIAymLa9DHHoCstoeEh9qoMJmdiX9RE6IzPkIsncVaAFp84fJJIu_Yb8qO_Z0Sv5HkDP1llfmpZ94F6lF7YfpEqOg88vKInxHm4S_aDFggmMdQyKFTkGWJuh0lAUq0N4PMoiKbmDhf_RUmuVwBlnMHpn4r70r0sIjTJgMOJs2Hpi3oFzD4y-8KkwWcguXvzXJGDAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر حسین ناصری:
MNaseri23595
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75620" target="_blank">📅 18:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2rAEu8-OooYAqoakFdpggFQjLpzaD_Ff1tMKh1JTpouGi90JaNsZGhjT4auRpuUHhyFVvGwOYH-eIlN04S7tHKQteaFnVpoGjjS8QDLQ9p-em_iGuOgxK34fjwAGmlaMYCq0eD8Xch2ezddtP8S1zSWUWoY0N70EiaWidF4FYz2FeQLq_y65sJn7Q16pvi4N50T-3x98caSHN_3_Y4PhmFsFDdbagKJy9oJE3Fh1wvjMhhiUKv-tDO8tO_x7LEy0EHjNcVix7CTBvd4eo2cpu738R7nN6OUBq4Sa-SKiqhTNi8MS3aBVsb8WqqmB6697VttMyuO1keatYj-Gx6Vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های دولتی پاکستان، فیلد مارشال عاصم منیر،‌ فرمانده ارتش این کشور راهی تهران شده است.
خبرگزاری اسوشیتد پرس پاکستان به نقل از منابع امنیتی گزارش داده است که فیلد مارشال عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
فرمانده ارتش پاکستان چهل روز پیش هم در تهران بود و با محمدباقر قالیباف و اعضای تیم مذاکره‌ ایران و آمریکا دیدار و گفت‌وگو کرده بود.
این در حالی است که وزیر کشور پاکستان هم برای دومین بار طی هفته اخیر به تهران رفته و در حال گفت‌وگو با مقامات ایرانی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75619" target="_blank">📅 17:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75614">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c-raVMDgx1vjwtH29yRo2k6jpVEHZI8xuszmah0sYjoEzeBSF0dc6NxzoVmneh6nx5QbOek13EKPk_7h38vwqnjzXjMK4wHETWdl28DqyEIaqQ1-5axLlrCu34wWNu8KlOaLzv9P8rHdpPBEEjJKq7xy6juj6wpyeF9nsbnFU37x0hcJGCnVPLadsGYh1TsKqEEPdBq6m0IcbyLHEcrrO6u7vFGUY-naGXN87AR8U7Yw_kgY0o8PvTuba7-Gfz5lyvddv2ynjVcNPxa1GYj1VuGe1PddEIx4SNg3q23fr_yPJk1NIctgG4gZnIWOGv5HDlHn_TbfZBm_Dc_BqroA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PvjBK1nq4Tpvgyv6I8QFUeSUMLumAJG1qwn839QKRC5Zyiw8pMK_m4OvuxBxt-jDbFgFEpbI7uLDEKhrApohPFSuW9qFBK7YWo7ECOrWZecZbQ26B9bT-_BA0TTurr544tSkzEWunqT-mb15mNJUdBzvMg2KJBlTgIX_ruTsHuTI_NF1cpmdZhFV-viuPUTJ6g_L1u4Rn1QLXI-_dFcvRCKzUQIW12lXzBl90Pf0JBgtUVjoUUHMqsxpw55cUqZ1zLUOt7LGhF9S7czJgchJeKRkUGvuCehamI_yN928ynlQy0rGiHhxI4KCWgJqcCSgQrFLfc69FKIsobA3svOCow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=RDFiSO9wwZXROcJjsfssshCxSht2naOOnhD4NRiWd2isGtZ10SJhZdJ2_BbL4AnafNhPa7IzAglp2TAYEQ63ncm4A784pMOW_THCDjxCuBthRYRt5Msb2x1QBIYxNaP0BX_Teyl91NYEb25a2ME4LF9tXImencW8XKYBeeFFjHd4f4UMW7xkWFQMa5G0Wq8SLq4Qy1uE5rVNFJ7u27WN9wH0ulnlCArgNqjSFBK_by2o62ICB2gyNV2dYLSnkC1WmBbs9izrCiADcG14yaTb2FA5ieveJL2NzV5L0MWpExBJ8XmA4tmXWdqeprG7XKcyf3iHjsDV19x8j20zHBgKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=RDFiSO9wwZXROcJjsfssshCxSht2naOOnhD4NRiWd2isGtZ10SJhZdJ2_BbL4AnafNhPa7IzAglp2TAYEQ63ncm4A784pMOW_THCDjxCuBthRYRt5Msb2x1QBIYxNaP0BX_Teyl91NYEb25a2ME4LF9tXImencW8XKYBeeFFjHd4f4UMW7xkWFQMa5G0Wq8SLq4Qy1uE5rVNFJ7u27WN9wH0ulnlCArgNqjSFBK_by2o62ICB2gyNV2dYLSnkC1WmBbs9izrCiADcG14yaTb2FA5ieveJL2NzV5L0MWpExBJ8XmA4tmXWdqeprG7XKcyf3iHjsDV19x8j20zHBgKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در حاشیه نشست ناتو درباره مذاکرات جاری با جمهوری اسلامی گفت که واشینگتن در انتظار نتایج گفت‌وگوهای در حال انجام است؛ گفت‌وگوهایی که به گفته او نشانه‌هایی از پیشرفت داشته‌اند.
او افزود: «ما در انتظار نتایج این گفت‌وگوها هستیم که نشانه‌هایی از پیشرفت دارد. نمی‌خواهم در این باره اغراق کنم؛ تحرک محدودی صورت گرفته و این مثبت است، اما اصول اساسی تغییری نکرده است.»
وزیر خارجه آمریکا تاکید کرد که حکومت ایران هرگز نباید به سلاح هسته‌ای دست یابد و گفت: «برای تحقق این هدف، باید به مسئله غنی‌سازی و نیز موضوع اورانیوم با غنای بالا رسیدگی کنیم و افزون بر آن، موضوع تنگه هرمز را نیز مد نظر قرار دهیم.»
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، جمعه یکم خرداد در حاشیه نشست ناتو گفت جمهوری اسلامی در پی ایجاد نظامی اختصاصی برای اخذ عوارض در یک آبراه بین‌المللی است و تلاش می‌کند عمان را نیز به پیوستن به این سازوکار متقاعد کند. روبیو تاکید کرد که این اقدام «غیرقابل قبول» است.
او افزود: «هیچ کشوری در جهان نباید چنین چیزی را بپذیرد. من کشوری را نمی‌شناسم که جز ایران از آن حمایت کند.»
روبیو با اشاره به تحرکات دیپلماتیک در سازمان ملل متحد گفت قطعنامه‌ای با پیشنهاد بحرین در شورای امنیت مطرح شده که آمریکا در آن نقش فعالی داشته و به گفته او، بیشترین تعداد هم‌پیشنهاددهنده را در تاریخ شورای امنیت دارد. او هشدار داد چند کشور در حال بررسی وتوی این قطعنامه هستند و افزود: «این مایه تاسف خواهد بود.»
وزیر خارجه آمریکا تاکید کرد واشینگتن برای دستیابی به اجماع جهانی جهت جلوگیری از اجرای چنین طرحی تلاش می‌کند و گفت: «باید دید آیا سازمان ملل همچنان کارآمد است یا نه. ما می‌کوشیم از این مسیر به نتیجه برسیم.»
او تصریح کرد اگر اخذ عوارض در تنگه هرمز اجرایی شود، ممکن است در دیگر آبراه‌های مهم جهان نیز تکرار شود و افزود: «این قابل قبول نیست و نمی‌تواند رخ دهد.»
روبیو با اشاره به اهمیت تنگه هرمز گفت این آبراه برای کشورهای حاضر در نشست و نیز برای دیگر کشورها، به‌ویژه در منطقه هند-آرام، حیاتی است.
او در پایان با ابراز امیدواری نسبت به نتایج نشست ناتو گفت این دیدار زمینه را برای نشست رهبران در حدود شش هفته آینده فراهم خواهد کرد و افزود که تا آن زمان کارهای زیادی پیش رو است.
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست ناتو در سوئد درباره مذاکرات با تهران گفت: «همه ما دوست داریم توافقی با ایران شکل بگیرد که در آن تنگه‌ها باز باشند و ایران از جاه‌طلبی‌های هسته‌ای خود دست بردارد.»
او افزود: «این چیزی است که همه ما امیدواریم و همچنان برایش تلاش خواهیم کرد و همین حالا هم که با شما صحبت می‌کنم، کار و مذاکرات در این زمینه ادامه دارد.»
وزیر خارجه آمریکا با اشاره به این که باید یک «برنامه جایگزین» هم وجود داشته باشد، گفت که برنامه جایگزین در صورتی باید عملی شود که حکومت ایران از باز کردن تنگه‌ هرمز خودداری کند.
او گفت: «پس باید از الان درباره‌اش فکر کنیم. من امروز این موضوع را مطرح کردم. واکنش‌های تاییدآمیز زیادی دیدم. اما هنوز چیزی برای اعلام رسمی درباره اقدام مشخصی که در حال انجام باشد نداریم.»
وزیر خارجه آمریکا درباره برنامه جایگزین در صورت امتناع جمهوری اسلامی از بازگشایی تنگه هرمز افزود: «نمی‌دانم لزوما این می‌تواند ماموریت ناتو باشد یا نه، اما قطعا کشور‌های عضو ناتو می‌توانند در آن مشارکت کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/75614" target="_blank">📅 17:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRQuYu14Og1MwZK-a6Z84diseoy7xh7o8hDODFinFlrpyDBU054ZTDsyKuoJCFsKURr8-kjRJ2ib9uBEqbqgz0FWryVO0a7TATE9DoWnznrnGDgwOQfJWwcl7wSD08G5rm8ZIiAgPJ70lIiz-_LPGJmrKCazFlVZXYTIQM_SjjTxYpkFqZNGFZ5z081sCNi-SjTJ3rLXKYFM7PJSm1HUQrZYJQgRjWKDhIfPJR3SW5c4NHq-EL1dPw8nDyaHGgVyE9TDCfbsh1XsMa05HcWyOgjKosQa3Tr4kOJlc9uyxwkFCfbuQtF8GReSrY-gvzh0_laJE-SueNw7xornnA96fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKvXAYriWJRC_7OSGE1FdBYw1DXvE9NtdwVcKMjC_tn1LhuYf5k7ZdMisY58GchvEZS_xxxxdvIcA9iNAJdNjc_NWVhQU2k7_TvZYdPon9SbEVjcEncy8USNZJ2JbbOX8olSxVNRSWg26Xf2PyNG3_AWpehud3iqAPzRoffvVNolrE4lqK7BP0V9fLrWbob1PLbAMUNGZJ31psN1KBpKS4wcS81nHyXcak4jL6go_suEhPM7lRnDLBg-4JkqFARtsKiNobD4MDpI3yUnxcuYu782ZGLIsIUZDOEtci_kp0TEeWEFtoPwj1cDYz8bImHxpaXP1sJGhd0J-wZRce3ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7B0I0V1oIydzSzjJSrzeDdOkXAY96bsuoovAC15MMHmiElrn1wDpU-mxkKI4_a-YHgedA--2qffewgQSJ22tDapkWFkKGUrPd8d_J0ply-OqG37sn7Rd-WImMrUGbJbrTClPasmQ3bcn9aTPPA5AS_wvQWjM35_JX828mNNWJQCtBL67ydRY7pbGYbPNVIXxxElOhM48ssNEc1w2fu2XHIgwL9lXPG1BnUC-E2TgS7luFFSGMXLD7q0CEV57KhaiVZnLbwThNuhhIFgRrBkQlpFYw01yyx3ILPNDxAksUen07VH2GBm0VRycDsEl-kng_9fRflKrhaNaQKXC6naXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اطلاعیه منوتو درباره پایان پخش برنامه‌ها
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75611" target="_blank">📅 17:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QSktHkfMiHzHsblJiLySN6l8zdrhsBS7qMLid57O9rWcrcGReoLDHGz7_Q-x2uppIHRG2jThdItbUgwqN8QlbNDdkw1KpBGzxU2yHe0Ikj0JaDjSJG1812Ua-qe6E8Dii1vTodCaTSlW8gp3vLPlL1BXy5pYLiHHJPCahLbAf-bhPoazXmXpJNcyb8g0v5y8rs3x56-3277b-Y0DmaPt9jCKsoi5Rh0dHAHsil2nUsY2Gtxi_ueAMnpHVsOQo7ZyKPUcfb5ZwIYrHgGe4rCCmAtxephgPo9BambHqrgVUZsTmKK8h7SIlfN5nX7TPFYnctbmUyCTiTCTuOO8u6k1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ljp0saEWxOLSW_0AmC8ilAiPN9yeh6pWAgO5n0IE6FoLdjf4lm4ZeQag3NolP6FreVcdAIRBMhGqHuRyBMGCPtbw08v6R1woCZEkR4e3ZwbwYgBx0Nv1OCiAQpNBhw97E3RkEVvbjNFxDhAcpdqL3giekoPJfdwMwUUkL1mMHPeWo0WC9YYNYOyDqn8Gdpxx1xy74CnE2ulMaehxP4VQdEQi2er0HfgWlNAJkjAbSsItDLjFjdVac7-aCzdGmczAXKtmHtsylrFv8C9HkOthZOn6STdLC1lut5RP63fqP07c2Hq08tYZpCQ4zfK3Mtibu5N58TgcnkYttTPII_s6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QU8v-GfdZQmtx3GgVxq7fpjIyG455szK10LkeZMD2zpEInQEe9S3OXGj_CmYpJ0Umh5qj4Zdc2CScYnGKqX6zbAzBu3Q3fReMsczAQA8qGakgbWaYrVrOKyeATkg53Wsj_rcVzUe4gEcjBV-e-s6ZFOFwUWEMsSJJNk92qbQpTdvjOPbegJbV1VdqcpBA8mIqlkea2WtD-V9-GVsFvcKOj8RV2tVzOVUmyAfjsC_dIAhvGbXqqrNQFgk5iFeLs8pFAZOHfz4ZlNxU0PrkEIcSC973epy9PTDLzkGQb-ha4-2g9-XFLk3TGtTtwiLEmJdMu_bBWy_wbSvtdPHEDVXmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=mj3Qx4u_cLJE_vwqSlrRf2zkjakvcDauTd9SL1_MBxPeEG4crhG1-oBAmGQRpx_bea2Nojo1kM0akq7Fk2sXqazhnln84zTrqh-ORhQR044Ps9j6UfHMtq8XiJdlHzEVc8HkkyLnD-KvkNQ5FtkgMor6wIstgb-Hd1VSOcdVwZ1HHYdKjDSeFWDZ_VgdlNH67yWuRVOtJ7EIiXG-8Mey7YfVbyCB8A1lhuEthbRIFGdzsSy2uUzTPpeN0qcVoqBhP6J_u08z6Du8HZzdHHv3okW3-BBV97OrQV4SlVfpDMOW0kXZROf7ZNrs6-kgqg96fzy4IqRmLZiH85FrMIL00g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=mj3Qx4u_cLJE_vwqSlrRf2zkjakvcDauTd9SL1_MBxPeEG4crhG1-oBAmGQRpx_bea2Nojo1kM0akq7Fk2sXqazhnln84zTrqh-ORhQR044Ps9j6UfHMtq8XiJdlHzEVc8HkkyLnD-KvkNQ5FtkgMor6wIstgb-Hd1VSOcdVwZ1HHYdKjDSeFWDZ_VgdlNH67yWuRVOtJ7EIiXG-8Mey7YfVbyCB8A1lhuEthbRIFGdzsSy2uUzTPpeN0qcVoqBhP6J_u08z6Du8HZzdHHv3okW3-BBV97OrQV4SlVfpDMOW0kXZROf7ZNrs6-kgqg96fzy4IqRmLZiH85FrMIL00g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم مستند «تمرین‌هایی برای یک انقلاب»، ساخته پگاه آهنگرانی جایزه «چشم طلایی» هفتاد و نهمین جشنواره فیلم کن را از آن خود کرد.
«لوئی دور» یا چشم طلایی، مهم‌ترین جایزه بخش مستند جشنواره فیلم کن است.
پگاه آهنگرانی جایزه‌اش را به مردم ایران تقدیم کرد و گفت: «(مردم ایران) با وجود تمام سرکوب‌هایی که در طول این سال‌ها تحمل کرده‌اند، هرگز از تلاش برای حقوقشان، آزادی‌شان و آرزوهایشان دست نکشیده‌‌اند و مطمئنم که آنها هرگز تسلیم نخواهند شد. مطمئنم و یک آرزو دارم که می‌خواهم اینجا بگویم: این‌که روزی دختر کوچکم لی‌لی و همه بچه‌های ایران در آینده‌ای نزدیک در ایرانی آزاد و دموکراتیک زندگی کنند.»
به گفته خانم آهنگرانی او با استفاده از آرشیوهای شخصی، ویدئوهای خانگی، تصاویر اعتراضات خیابانی، روزنامه‌ها و صداهای ضبط‌ شده، بیش از ۴۰ سال از تاریخ ایران را بازخوانی ‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75607" target="_blank">📅 17:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImHTDCYdGfTvZHso93oEOrRom4FxyA8q_1QPvmLPWpjv-T8aVgBLGBUcD6l0WMp7BXp3wP75ktcA2WB3e7XEfeC7gwn8m-QUF5KsPVleG_FrZ_kmxdKvEWkqwX0E6RkjKACTOh7ND7GvQf01X2ZlQ9V-eCgDOr5H80oiDJxJp9oTBfkqxjgSPA8Zs8z0PxJij4tza2gMhugInvfDkwYpZUbiavJSWoxyte_uzzhNewRrbFockj6rmHJWmcHKMW-1zE0xFwfdBX2XI3FPEbwPcicWnDv4FaIcUUWmyvYgMiY9xUUFsB7onWMCOjNRPLMgEHqDTMP-DL8Qlgoi15Gh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عرب حوزه خلیج فارس از جامعه جهانی خواستند که طرح جمهوری اسلامی برای مدیریت تنگه هرمز را رد کنند.
به گزارش بلومبرگ، در میانه مذاکرات دیپلماتیک سازمان بین‌المللی دریانوردی با ایران و عمان پیرامون بازگرداندن آزادی تردد و امنیت کامل کشتیرانی در این آبراه راهبردی، کشورهای عرب حوزه خلیج فارس طی نامه‌های به اعضای این نهاد زیرمجموعه سازمان ملل، نسبت به طرح جمهوری اسلامی موسوم به «نهاد مدیریت آبراه خلیج فارس» هشدار دادند.
پنج کشور عربستان، امارات، بحرین، کویت و قطر در نامه خود گفته‌اند که به رسمیت شناختن مسیر پیشنهادی جمهوری اسلامی می‌تواند یک «سابقه خطرناک» ایجاد کند.
سفیر ایران در فرانسه روز گذشته تأیید کرد که تهران با عمان درباره اعمال دائمی عوارض عبور در حال مذاکره است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/75606" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75605">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxMA_08-YFlVqCslmMPs9VniSDKrPRdpsEnaoDwBYIktcdp_unQEEBaSda0cVuiCjdmlMheNZd3NWhNcSgM5FMeoC9pb2kLtHGdVAvYNkkRxfjH2tfsyumvTaWOT_ZjIgqGv5Dd7yqV7m-IxiKLi0icxhTUvbm9vg6swUfNHi_85I3hPQ9AujfIa-AukEB9c7UUhMsb69Vvz5xY20WCwVLY7OD6Wv1HS5JbcZotRL3WQSX65SKf1eItcfDTZXtum6Ub7vKybCWAg8_NlC5cpy3_SonXaDBVaqXqc0kM_M4NLAznHy3Em0J4nxwMqHku8j5upFS3Gwq8RmiwiPtPD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد بین‌المللی ناظر بر وضعیت اینترنت، نت‌بلاکس، صبح جمعه اول خرداد اعلام کرد قطع گسترده اینترنت در ایران وارد هشتاد‌وچهارمین روز خود شده و بیش از هزار و ۹۹۲ ساعت است که دسترسی کاربران در ایران به شبکه‌های بین‌المللی همچنان قطع است.
این نهاد ناظر بر اینترنت نوشت با ادامه این وضعیت، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شود و هر ساعت از قطع اینترنت، ارتباط با جهان خارج را بیش از پیش به جایگاه، همراهی با حکومت و برخورداری از امتیاز وابسته می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75605" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L15MGbw1Rbs32Y2WrfI9MJBGKdxueWAPJGoSHmnfgq1-nuenO0qgk_Hk-SqvEFGeknx2q9y7ta0mLuI1vgkE_iHMP5De73087SKEyy89TSI0BWqmgVcxRmC8e09iBfADGWTRAFGWC8kaiD38EeDyC4JjH9xrWuBshEkWRfFrIo3A_NLxg_--1H3ZcY1pBeG2lFmqvGCKLi-vT2dHnLH9gf8hSkQ9xwrA2M-_hg1yIJZLDbnx1obiVNbK3pZR3Ir4m8mkzPqxl-n0zOz2gwqKBcMChlZjRGCRocnqosGAPqvfuHZ22qAZltmKdFHaEUuWj5CRxaGpCZStfkRQW-niIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور احکام اعدام محمدرضا مجیدی‌اصل و همسرش بیتا همتی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، را نقض کرد.
هرانا خبر داد که پرونده این دو متهم برای رسیدگی مجدد به شعبه هم‌عرض ارجاع شده است.
این دو پیش‌تر به همراه بهروز زمانی‌نژاد و کوروش زمانی‌نژاد با حکم صادرشده از سوی قاضی ایمان افشاری، رئیس شعبه ۲۶ دادگاه انقلاب تهران، از بابت اتهام «اقدام عملیاتی برای دولت متخاصم ایالات متحده و گروه‌های متخاصم» به اعدام محکوم شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75604" target="_blank">📅 17:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=aKWLgLcfePymUGJQtMM6PMz1yGH6CTQ8okcRJB8NGPKyv0npv1etmR4loSsmwG5Bu5kOYo09gdTHFYy6Z3_-1cZ1vIOnzVq2eBgKse7yCEohE9916QPD74QG-nU99iNvEBdfS5VYOZJFAwPM-_NJSTaubornZRGynXl75d0ZZkGFSjJnpob5p7e6P6VXcmubFeKVGG_M72otd7cTxALqIfFx4zrgdVIYViSMmr82JbteerjO4ne15N_4ucoHwbGwxnZoYtk1c-LyhYEcUg16yVmhcLZ1V1k-f-9tnJyceYZTzurMQp-rKcwGJR5icJ16ZQCb8lZRTkGpSaOZDiCwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=aKWLgLcfePymUGJQtMM6PMz1yGH6CTQ8okcRJB8NGPKyv0npv1etmR4loSsmwG5Bu5kOYo09gdTHFYy6Z3_-1cZ1vIOnzVq2eBgKse7yCEohE9916QPD74QG-nU99iNvEBdfS5VYOZJFAwPM-_NJSTaubornZRGynXl75d0ZZkGFSjJnpob5p7e6P6VXcmubFeKVGG_M72otd7cTxALqIfFx4zrgdVIYViSMmr82JbteerjO4ne15N_4ucoHwbGwxnZoYtk1c-LyhYEcUg16yVmhcLZ1V1k-f-9tnJyceYZTzurMQp-rKcwGJR5icJ16ZQCb8lZRTkGpSaOZDiCwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویرسازی از مجتبی خامنه‌ای
وزارت جنگ آمریکا روز پنجشنبه ۳۱ اردیبهشت، با انتشار
ویدیویی
بر ضرورت افزایش بودجه دفاعی کشور تاکید کرد.
در این ویدیو که ترکیبی از صحنه‌های واقعی، گفته‌های پیت هگست، وزیر جنگ آمریکا و تصاویر کارتونی است، تصویری از مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی نیز در کنار یک سامانه موشکی دیده می‌آشود در حالی که یک پایش قطع شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/75603" target="_blank">📅 02:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSDAYnb-QaRZHOsaFe0CrnVhruQ_RhiVzjbBsX70LRDFn-hyDS52gnSPbqbCL_j5GdSLrEtrCn3Ba79pfQinxO_57ZLTKPFBw8YEElByAmWfOiWDNFtZGBCx4U-4kVVd77KARN6vAk9eiBfYCqRy39L9s9Ks2g-5v6MCGUbWFG26cRAJsevxn1AIywqtLu1-fsVdtgEtfUsZYJ6RlVJm2SnB3zwuE-UYW4lY-SieCoh6nLU_srLsjO_SDdZPBKBr2TUMIcbqC5Nkd4TTOn_hYwyRphqI_R_Hsd0bfUihfdMUDMu467NJCNFeFkak2B639pU-pnAcKeA32swkpH5eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
در تازه‌ترین تحولات بحران ایران و مذاکرات جاری، یک منبع بلندپایه به «العربیه» گفت که فرمانده ارتش پاکستان امشب راهی تهران نخواهد شد؛ این در حالی است که پیش‌تر گزارش‌هایی درباره احتمال سفر او در چارچوب میانجی‌گری‌های منطقه‌ای منتشر شده بود.
قرار بود عاصم منیر، رئیس ستاد ارتش پاکستان، امروز پنج‌شنبه در سفری رسمی وارد تهران شود؛ هم‌زمان با انتظارها برای تحویل پاسخ ایران به تازه‌ترین پیشنهاد آمریکا برای توقف جنگ و دستیابی به توافق میان ایران و ایالات متحده.
alarabiya
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/75602" target="_blank">📅 23:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=DUb_mXKJ1h0h2WGrormfbKMPvlXD3H4XjvDi_IJgq0S3DRLRuJW1GLRuH5E1tavWy3I5r2UARGclVa1RfZRO_hBvAaFJSCSpglVizNCcRl7VnB5OaFtgels2o1Z5dADAxet8UbgoIgIhHM9EKUNRssiFlGlwlXMr3WvKcrpbUFSP0SGm7O2X5Ky5hAq1Wk4cA1b6zpVhdr74Xxh2mlcoYegecCNxPUuXsWh1wlEpndV46fC4Dv1Aoz5ZreEH7cio9areRvKBO0jqAYANtDN5Sl4Z6KlHKQxfkMvW9LiDLHgEE4ZoF8CRgGMEaP74I8b2GNISoQY83HYzilCtp0U--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=DUb_mXKJ1h0h2WGrormfbKMPvlXD3H4XjvDi_IJgq0S3DRLRuJW1GLRuH5E1tavWy3I5r2UARGclVa1RfZRO_hBvAaFJSCSpglVizNCcRl7VnB5OaFtgels2o1Z5dADAxet8UbgoIgIhHM9EKUNRssiFlGlwlXMr3WvKcrpbUFSP0SGm7O2X5Ky5hAq1Wk4cA1b6zpVhdr74Xxh2mlcoYegecCNxPUuXsWh1wlEpndV46fC4Dv1Aoz5ZreEH7cio9areRvKBO0jqAYANtDN5Sl4Z6KlHKQxfkMvW9LiDLHgEE4ZoF8CRgGMEaP74I8b2GNISoQY83HYzilCtp0U--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفتگو با خبرنگاران در کاخ سفید تاکید کرد که هیچ کشتی‌ای بدون تایید ایالات متحده اجازه ورود به ایران یا خروج از آن را ندارد و نیروی دریایی آمریکا در این زمینه عملکرد فوق‌العاده‌ای داشته است.
ترامپ با اشاره به خسارت‌های سنگین مالی جمهوری اسلامی در پی این اقدامات گفت: «بر اساس پیش‌بینی‌ها، آن‌ها روزانه ۵۰۰ میلیون دلار ضرر می‌کنند؛ رقم بسیار زیادی است و چه ۲۰۰، ۳۰۰ یا ۵۰۰ میلیون دلار باشد، آن‌ها در حال از دست دادن پول گزافی هستند.»
رئیس‌جمهوری آمریکا با تاکید بر لزوم آزادی کشتیرانی افزود: «خواسته ما این است که این آبراه بین‌المللی، باز و آزاد باشد. تنگه هرمز یک مسیر دریایی بین‌المللی است، هیچ‌کس نباید در آن عوارض وضع کند و ما اجازه چنین کاری را نخواهیم داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75601" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/011b067e31.mp4?token=dX8qICj33TGgV8uPpAYd2g9dlT9BNSXNsTubibYEXQfvYHbfU10hExeaQxL6r62DGP4UooU2CaeIust7WfDC-NxAAR0yXdQlfKUicmarV1qp-d1-5oqW-nJ6z6VW40q-c-xrrhQBofTfHcAJZdLjIRUK2MPfZN1mIWrrzNtrLJKW8RSYS_JKvfHigdzsLozu3MUh-vZECiGZfAlSrvI79Qi_0FtybLQ0IGim0mgLZ_UYnaoLo9BnZY60BXcikojopeDAERO8loQn0B-KKJaHYwy9g7vOUJGNUaqgUePNfR5xnj4eDfrV5UKuewWRAvrO8pK60B_C8BtAzA6Tjxd5mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/011b067e31.mp4?token=dX8qICj33TGgV8uPpAYd2g9dlT9BNSXNsTubibYEXQfvYHbfU10hExeaQxL6r62DGP4UooU2CaeIust7WfDC-NxAAR0yXdQlfKUicmarV1qp-d1-5oqW-nJ6z6VW40q-c-xrrhQBofTfHcAJZdLjIRUK2MPfZN1mIWrrzNtrLJKW8RSYS_JKvfHigdzsLozu3MUh-vZECiGZfAlSrvI79Qi_0FtybLQ0IGim0mgLZ_UYnaoLo9BnZY60BXcikojopeDAERO8loQn0B-KKJaHYwy9g7vOUJGNUaqgUePNfR5xnj4eDfrV5UKuewWRAvrO8pK60B_C8BtAzA6Tjxd5mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی هم تلویحا وجود یا عاملیت داشتن مجتبی خامنه‌ای در تصمیم‌گیری‌ها رو زیر سوال برد.
بعد از شعار جماعت در لحظه 01:48 ، یک بچه میگه: مرگ بر دیکتاتور!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75600" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=PUGbrzZGetjj-JE2fl_hWtr-2vIzFjjQOCDf_oqkxQ7OR3KPI0mA_CoT8BrUph6IEl8z46vLxU49VOqlZaROI2qT_QhoBhB3vmdDx1pW4LJssVqOkB5-npwpzOZdLgay73ymUCEfJ89-q6GRmKnmnhMtB0C06bhua23KRbgiI4ZQO2wsd7ai5sW1_ah0E0fHgnQmltp__19QN_W92AhllGzz4WPUnIYeeWXOewt1gw6cE2caiR-GIGa_GYdCwz4E4YuBuQvpZ9H5wnhp8BP82RR35xrKVgjXPW_q_hByyyLh_dPpmqHzea7xrNneJQafKgKXoNGPIp702_rmr7K2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=PUGbrzZGetjj-JE2fl_hWtr-2vIzFjjQOCDf_oqkxQ7OR3KPI0mA_CoT8BrUph6IEl8z46vLxU49VOqlZaROI2qT_QhoBhB3vmdDx1pW4LJssVqOkB5-npwpzOZdLgay73ymUCEfJ89-q6GRmKnmnhMtB0C06bhua23KRbgiI4ZQO2wsd7ai5sW1_ah0E0fHgnQmltp__19QN_W92AhllGzz4WPUnIYeeWXOewt1gw6cE2caiR-GIGa_GYdCwz4E4YuBuQvpZ9H5wnhp8BP82RR35xrKVgjXPW_q_hByyyLh_dPpmqHzea7xrNneJQafKgKXoNGPIp702_rmr7K2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، در کاخ سفید گفت: «جمهوری اسلامی قرار نیست سلاح هسته‌ای داشته باشد. ما نمی‌توانیم اجازه بدهیم.»
او افزود که در صورت دستیابی جمهوری اسلامی به سلاح اتمی، «در خاورمیانه جنگ هسته‌ای به راه خواهد افتاد، و آن جنگ به اینجا خواهد رسید، آن جنگ به اروپا خواهد رفت.»
رییس‌جمهور آمریکا تاکید کرد: «ما نمی‌توانیم اجازه دهیم چنین اتفاقی بیفتد، و چنین اتفاقی هم نخواهد افتاد. قرار نیست اتفاق بیفتد.»
ترامپ درباره محاصره‌ بنادر جنوبی ایران از سوی آمریکا نیز گفت: «کنترل کامل تنگه هرمز را در دست داریم. این محاصره ۱۰۰ درصد موثر بوده است. هیچ‌کس نتوانسته عبور کند. مثل یک دیوار فولادی است.»
او افزود: «هیچ کشتی‌ای نتوانسته بدون تایید ما عبور کند. و نیروی دریایی کار فوق‌العاده‌ای انجام داده است. و هیچ کشتی بدون تایید ما به ایران نمی‌رود یا از ایران خارج نمی‌شود.»
ترامپ درباره اورانیوم غنی‌شده ایران نیز گفت: «ما اورانیوم بسیار غنی‌شده را می‌گیریم. ما به آن نیاز نداریم. احتمالا بعد از اینکه آن را بگیریم نابودش می‌کنیم، اما اجازه نخواهیم داد آن‌ها (مقامات جمهوری اسلامی) آن را داشته باشند.»
دونالد ترامپ، رییس‌جمهور آمریکا پنج‌شنبه در کاخ سفید به خبرنگاران گفت که ایالات متحده خواهان دریافت عوارض در تنگه هرمز نیست.
پیشتر مارکو روبیو، وزیر خارجه آمریکا اعلام کرد که اجرای سیستم اخذ عوارض در تنگه هرمز از سوی جمهوری اسلامی، دستیابی به توافق دیپلماتیک را غیرممکن خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75599" target="_blank">📅 20:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=JdAEUwmTsd5qfrM_M0ov-2cTCvvqdd2oBbZ8f7gw35lYV0t8HO0coqZFMB56bU6wdjLoFqwRzyNdFhbz5nyfq_T5Zm0lHT3R5NdVLK73q34ZvAflxq4AWx9n2g2gZDNm8timGJFHaGxGTNar2GsbizBn9zTaiN2zRY5za_h6V03OsFhCh2QwnhmXqXOr7vqzFE2o7KC4h6jxmWNSnVFpIodVgVOuZSQR_AivZBPZvh3zHD6EOC2c9s9bUCxy5nytTaj3p9nPlEDVBcZQsUEey5I3cdA-9p2BYS4uROYMrcv9UkrYda-mkOW5hZ2XZ6RwTG9O7eDzteZw2zHL_0lcGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=JdAEUwmTsd5qfrM_M0ov-2cTCvvqdd2oBbZ8f7gw35lYV0t8HO0coqZFMB56bU6wdjLoFqwRzyNdFhbz5nyfq_T5Zm0lHT3R5NdVLK73q34ZvAflxq4AWx9n2g2gZDNm8timGJFHaGxGTNar2GsbizBn9zTaiN2zRY5za_h6V03OsFhCh2QwnhmXqXOr7vqzFE2o7KC4h6jxmWNSnVFpIodVgVOuZSQR_AivZBPZvh3zHD6EOC2c9s9bUCxy5nytTaj3p9nPlEDVBcZQsUEey5I3cdA-9p2BYS4uROYMrcv9UkrYda-mkOW5hZ2XZ6RwTG9O7eDzteZw2zHL_0lcGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز پنج‌شنبه اعلام کرد اگر تهران طرح دریافت عوارض برای عبور از تنگه هرمز را اجرا کند، رسیدن به یک توافق دیپلماتیک میان ایالات متحده و ایران غیرممکن خواهد شد.
او در گفت‌وگو با خبرنگاران گفت: «هیچ‌کس در جهان از سیستم عوارض‌گیری حمایت نمی‌کند. چنین چیزی نمی‌تواند اتفاق بیفتد. غیرقابل قبول خواهد بود. اگر آنها همچنان دنبال اجرای آن باشند، رسیدن به یک توافق دیپلماتیک غیرممکن می‌شود. بنابراین اگر بخواهند چنین کاری انجام دهند، این تهدیدی برای جهان است و کاملاً غیرقانونی است.»
او همچنین خبر داد که در مذاکرات با تهران برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران، «پیشرفت‌هایی» حاصل شده است و به گفته او «نشانه‌های خوبی وجود دارد»، اما واشینگتن با «سیستمی روبه‌روست که خودش تا حدی دچار شکاف و چنددستگی است.»
وزیر خارجه ایالات متحده با اشاره به این که مقام‌های ارشد پاکستان به عنوان میانجی مذاکرات امروز به تهران سفر خواهند کند، گفت: «ترجیح رئیس‌جمهور آمریکا این است که یک توافق خوب حاصل شود... من اینجا نیستم که بگویم حتماً چنین اتفاقی خواهد افتاد، اما اینجا هستم که بگویم ما هر کاری بتوانیم انجام می‌دهیم تا ببینیم آیا می‌توانیم به توافق برسیم یا نه.»
او در عین حال افزود که اگر یک توافق خوب حاصل نشود، دونالد ترامپ «به‌روشنی گفته است گزینه‌های دیگری هم دارد.»
پیش از این گزارش‌هایی درباره سفر روز پنجشنبه فیلد مارشال عاصم منیر، رئیس ستاد ارتش پاکستان، به تهران منتشر شده است. خبرگزاری‌های رسمی ایران این خبر را یک روز پس از آن منتشر کردند که وزیر کشور پاکستان، برای دومین‌ بار طی هفته جاری وارد تهران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75597" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVsG9eat84Rj_oLMqqxO_LSFnV-p664brU7lFnKoU-bPqeOwbcveUFuRMRpdGKiiV-xyw3nVbWGuq-wQeZrNFhNd4WrXVjcZ51q17kNCCKmqK3uASI5YO-frHIfD01ZBltRUtN3tT_1EqQkK6dCeah8Rc68urulz3ijOLsc8Z5uCQW4YiDCI-BVka95gA2bGx77WPB1xhRJpu5an9GGbbmkLxHILUfMeKPmi7SDQb3xgOOPV4TVEcCJxiuTbg17c3sZQbIh9ljbcQpwwtbrzGy8zeS1RBIDMpAWd776Ww9Hqfuk2dFxfColUDMBht7aRmqxpACU265AvPLVQEYLOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس نیوز به نقل از یک منبع آگاه از روند مذاکرات خبر داد که کاخ سفید گزارش خبرگزاری رویترز مبنی بر این‌که مجتبی خامنه‌ای دستور داده اورانیوم با غنای بالا در ایران باقی بماند را رد کرده و آن را نادرست دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75596" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P764Bm5jfUAQKWkeVYICxRvwdGItTR-xro5N6KPxSbbTtmKdNi8lF2-slN44I9U0I4e6Ye9lmuiUFCalng_8qb_mZak8dQ7lHnImCJLpgGas-aYEIqOvPDcMSUnbkbvH49srQDELoq9qJQD_F2t-7ikf6Dy-_sY4QIUH75mDKrK2HltRkg4XHIVicmU9JIbtek87D-8yoVWkVwyL_BZ0FrrNc9gH8oWebc9g6Ds7HKFbSaR28s4EhXIEeS5E4Fo0BIMCQHF-F_Zwj0aTX9drCy7J8An5SFAM7Vb2xoGuDzpkOr2xC8apfNprj0OJsvQRYSn7GFy7BGqgPjDi-EF0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تحقیقی FTM هلند در
گزارشی
نوشته که توماس اردبرینک، خبرنگار هلندی نیویورک‌تایمز و شبکه NOS در ایران، همزمان مشاور شرکت آبجوسازی هینکن هم در ایران بوده و برای این کار ماهانه تا یک‌سال ۵ هزار یورو دریافت می‌کرد. اردبرینک دریافت مبلغ را انکار کرده.
طبق این گزارش این روزنامه‌نگار به طور منظم کارهای جانبی (پروژه‌ای) برای این شرکت آبجوسازی در ایران انجام می‌داده است و نه تنها کارمندان اعزامی و بازدیدکنندگان را در تهران می‌گردانده، بلکه گفته این شرکت آبجوسازی را با وکلا و مشاوران محلی نیز مرتبط کرده است.
FSeifikaran
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75595" target="_blank">📅 18:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0uEyirBSip70NCTvXOabg0IdxhneNga_IYA1NPfatWP9cr-vi4fR01C1YPNjzqtXXn4ynqZjSwOPzLn0AHwfV1aEMiRh-mnOZ8KiFiO5cvuwBU0mebeiJVyBhXfzQyC57nwxsOmFGOwlbS4qEuHpfwOygfB2tYg_YQE1I3AD8ci1enp5kJODqAdAjxdZMhA6EDlsyjcvyyNu6pyAKTIVgyoql5s5Erc2WATN_EoRsnq5lZUkhbwrmnl3avI3TZcbR1Q6gX0SNnZJUU0cTuKN50w0WIH46jWHKAoh95R5n-G6jHCu1AnrBHlC7gARLqD0gNiT6CzA3LrYrcI6j2QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انور قرقاش، مشاور ارشد رئیس دولت امارات متحده عربی، می‌گوید که برخی رفتارهای ایران در سال‌های گذشته باعث کاهش اعتماد میان کشورهای منطقه خلیج فارس شده است.
او در پیامی در شبکه اجتماعی ایکس نوشت که کشورهای منطقه طی سال‌های طولانی با «رفتارهای زورگویانه و تهدیدآمیز» ایران روبه‌رو بوده‌اند؛ رفتارهایی که به بخشی از واقعیت سیاسی خلیج فارس تبدیل شده است.
آقای قرقاش همچنین تاکید کرد که شکاف میان مواضع تند و ادعاهای دوستی از سوی ایران، باعث از بین رفتن اعتماد و اعتبار شده است «و امروز، پس از تجاوز وحشیانه ایران، حکومت ایران تلاش می‌کند واقعیت تازه‌ای را که از یک شکست آشکار نظامی به‌وجود آمده تثبیت کند؛ اما تلاش برای کنترل تنگه هرمز یا تعرض به حاکمیت دریایی امارات متحده عربی چیزی جز خیال‌پردازی و آرزوهای دست‌نیافتنی نیست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75594" target="_blank">📅 17:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=Gak5P0ZoNkWRUEqS0lTWfQBS3MtdFPGOb0XAdl1ANR_VOkbCz6vQW_PMUdFxbqvr2O4oCQ2EMeSfHCgya4q9VZnCYGF5QOeHqZrkwVV9PWbx3O6-rlnSzHS_mE2YvbTvPdT6mvc9lf_tU3VzaiGLBbUD8qcZ5wft5xmec1tZ5wJzES_MIcLhSYrFuj5TX-7dHANhx1sojnPZ40FWi4U2vuilj8LQJFMFYtyqTIC2hcelOmOWTJzGvNib5P2KvR2PDoSX33ppLciTFqY5351aeIUkAfPUJ8nf4EnkOHYTfd2078dzrM3VXnNe3hJL1RGk94MI_f61cr8qFybTRqInsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=Gak5P0ZoNkWRUEqS0lTWfQBS3MtdFPGOb0XAdl1ANR_VOkbCz6vQW_PMUdFxbqvr2O4oCQ2EMeSfHCgya4q9VZnCYGF5QOeHqZrkwVV9PWbx3O6-rlnSzHS_mE2YvbTvPdT6mvc9lf_tU3VzaiGLBbUD8qcZ5wft5xmec1tZ5wJzES_MIcLhSYrFuj5TX-7dHANhx1sojnPZ40FWi4U2vuilj8LQJFMFYtyqTIC2hcelOmOWTJzGvNib5P2KvR2PDoSX33ppLciTFqY5351aeIUkAfPUJ8nf4EnkOHYTfd2078dzrM3VXnNe3hJL1RGk94MI_f61cr8qFybTRqInsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بریتانیا از توافق تجاری ۵ میلیارد دلاری با کشورهای خلیج فارس رونمایی کرد؛ توافقی که در بحبوحه تنش‌های منطقه‌ای پس از جنگ ایران، به گفته لندن «پیامی از ثبات و اعتماد» به بازارها می‌دهد.
این توافق با شورای همکاری خلیج فارس شامل عربستان، امارات، قطر، کویت، عمان و بحرین است و قرار است سالانه حدود ۳.۷ میلیارد پوند به اقتصاد بریتانیا اضافه کند.
لندن می‌گوید ۹۳ درصد تعرفه‌های کشورهای خلیج فارس برای کالاهای بریتانیایی حذف می‌شود؛ از جمله محصولات غذایی، خودرو، صنایع هوافضا و الکترونیک.
در مقابل، بریتانیا نیز برخی تعرفه‌ها را کاهش می‌دهد، هرچند نفت و گاز کشورهای عربی پیش‌تر هم بدون تعرفه وارد بریتانیا می‌شد.
فعالان حقوق بشر از نبود بندهای الزام‌آور درباره حقوق بشر در این توافق انتقاد کرده‌اند و آن را «عقب‌گرد اخلاقی» توصیف کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/75593" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_XzjPiwuKGIiipX82kq_69C06QPPx3oPotusT984FttOMYdxtw6y8u50KNuE4Pp_KOpeR5iXZefIf-8hCxJVGT7KIxiNIeUZFv-ya60CjeMbRLZ1XRSxGyvVVHzGT7kUcL6Cnve6V4XxcMBtCMLQ4U562UjvcC4LDlyGnpkc4i6UO6E2vRs1n0ymNn8cOPD7zprsZvU5qz5JRm9c_47cWHPR6bTDPmuOWKXPm5u3fNSEZg3yr4VwPorvJQtSg6_JZU2PhlNJuUqqMEiFNVN6sjHnMFerfl6XUyt2xwDNQF6bwvOsBMJ4uhXUhjQ3p4B6euYF6eTqN9LyeKosmJ6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی یزدی‌خواه، نایب‌رییس کمیسیون فرهنگی مجلس، گفت در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد و محدودیت‌ها با «ملاحظات امنیتی» ادامه خواهد داشت.
یزدی‌خواه قطع اینترنت جهانی را به مصوبات شورای عالی امنیت ملی نسبت داد و گفت این تصمیم به‌دلیل «مسائل امنیتی، امنیت کشور و حفظ جان افراد» گرفته شده است.
با وجود اینکه نت‌بلاکس اعلام کرده خاموشی اینترنت در ایران وارد هشتادوسومین روز خود شده، یزدی‌خواه گفت بیش از ۹۰ درصد نیازهای مردم در وضعیت فعلی برآورده می‌شود و مراجعات گسترده‌ای در اعتراض به قطع اینترنت وجود ندارد.
او همچنین گفت در قالب طرح موسوم به «اینترنت پرو»، تاکنون بیش از یک میلیون نفر دسترسی دریافت کرده‌اند؛ طرحی که منتقدان آن را مصداق اینترنت طبقاتی و تبعیض‌آمیز می‌دانند، زیرا دسترسی به اینترنت جهانی را به گروه‌های خاص محدود می‌کند و شهروندان عادی را از حق برابر دسترسی آزاد به اینترنت محروم نگه می‌دارد.
نایب‌رییس کمیسیون فرهنگی مجلس همچنین گفت شرکت‌های صادرات و واردات، مراکز علمی و پژوهشی، آزمایشگاه‌ها و برخی اصناف در صورت نیاز می‌توانند برای دسترسی به اینترنت بین‌الملل اقدام کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/75592" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dT9DUcxe6BufG0BLLXMueBgyZXqfYNYr3MLYROMCZDZwwkbeByz9iKcbr9E3O4_hejvEks96q0y2l8Inf8Bu-iiLvjFkxmprwPbxfZFdGusZRf9sRVZWt-BysgoUCHlsO9BQs0V1bUJjV3ZjHiYiKBwoIkanaREA6X84Y-IcHNB3Qxybw5jYxXB6r0_H-27puwbtBpQSX7giuLpWjqK-TRNyM6KraGtz_8MgJfTcw5L7eusYbAat6uT8I-i-9dQ4mjafbdyCLidZUQLh1a6H6lva_BCPWO0vyn41stl4YUAdL25l3XvgU_Bmwb_kJh9VuWl-Ueja1iqGLdVb82DPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد در حکومت ایران گزارش داد مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده ذخایر اورانیوم با غنای بالا نباید از ایران خارج شود.
به گفته این منابع، این دستور موضع تهران را در برابر یکی از اصلی‌ترین خواسته‌های آمریکا در مذاکرات برای پایان دادن به جنگ آمریکا و اسرائیل علیه جمهوری اسلامی سخت‌تر کرده است.
مقام‌های اسرائیلی نیز به رویترز گفته‌اند دونالد ترامپ به اسرائیل اطمینان داده هر توافق احتمالی باید شامل خروج ذخایر اورانیوم غنی‌شده از ایران باشد.
یکی از منابع ایرانی به رویترز گفت دستور رهبر جمهوری اسلامی و اجماع در ساختار حاکمیت این است که ذخایر اورانیوم غنی‌شده نباید از کشور خارج شود.
به گفته منابع رویترز، مقام‌های جمهوری اسلامی معتقدند انتقال این مواد به خارج، جمهوری اسلامی را در برابر حملات احتمالی آینده آمریکا و اسرائیل آسیب‌پذیرتر می‌کند.
@
VahidOOnLine
دقایقی پس از این خبر رویترز بهای نفت در بازارهای جهانی نزدیک به دو دلار افزایش یافت.
قیمت هر بشکه نفت خام برنت دریای شمال بعدازظهر پنجشنبه ۳۱ اردیبهشت‌ماه در بازارهای اروپایی از ۱۰۵ دلار به بیش از ۱۰۷ دلار افزایش یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75591" target="_blank">📅 17:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFD50JQGBiGu6tP5SyQ_tkYN95rttBY_uDP85rD6zDPaylwx96HlRrjLoNdjD_D4hZGioOHM_yvCokyh0pVHbXbChz6NEAYpgwui6TwnpZ02HKisdYcjZ_pRNvkNTE7qEcWnn4heHNNWuyTYpx-iTBTxDGccdMPwhjUHYXf45gMAvgfuuyH7JhdyE4g7K-NHgP03aT9EItHD2XJSDvSA6rcEJn0_jCT-GBc4AM6AjIioa9ehDbGxvtwbOpNeYm4RLxKk2qxdpryvp0jm11w3xvT_kthabLf1YaVkYsKgfjdROArBTk0BAohzbIzk86-EtFSjPy0yvF76KPlYcPZKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی کابی‌زاده، شهروند ۴۷ ساله و پدر یک دختر بود که در اعتراضات دی‌ماه در استان خوزستان بازداشت و پس از انتقال به مرکز درمانی به دلیل منع رسیدگی جان باخت. او دختری به نام حلما دارد.
بر اساس اطلاعات رسیده به ایران اینترنشنال از افراد مطلع از خانواده او، مهدی کابی‌زاده در اعتراضات اهواز به دست ماموران بازداشت شد و سپس به دلیل بیماری خونی و روده به بیمارستان منتقل و بستری شد. با این حال، مسئولان بیمارستان به دلیل سابقه حضور او در اعتراضات و بازداشتش از رسیدگی و درمان کافی خودداری کردند که موجب جان باختن او شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75590" target="_blank">📅 17:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hxmplWvq8u63-cxDkOIkukqJuSV-zAmuyOv5vn46fMH73owRDsTR0x7vpO-BnJ_Z5Jkcu-k81oXSWhdrCKzACi6Bf-Y1T0gNfMoPeQ9pbxT3_wM_FSaovnjYuafdiLHxOTU_XpOI3yxLg_Lhe_k57dOQitRGp7xfogdfJsz0ejHqh-1p9hvknv9N0ebh3LVsyNjAr6Kyf8LXcqIqv7oGV1C3T-TMObY1f8z8fnz5zrO2PiqXzhZaTqSE2TazBQwJsywiZFutB9_cCgrv3ybVi63jpnI9-Nqf90n3himPECI1wR_-jLzd05ZzSmURgNmcYElisPrTweJJgg1D33MqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی دو زندانی را به اتهام عضویت در «گروه‌های تروریستی تجزیه‌طلب» و «قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه» اعدام کرد.
ارگان رسمی دستگاه قضایی ایران، میزان، هویت این دو نفر را رامین زله و کریم معروف‌پور معرفی کرده و نوشته که آنها صبح روز پنج‌شنبه، ۳۱ اردیبهشت، اعدام شدند.
میزان نوشته که رامین زله «پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند».
ارگان رسمی قوه قضائیه ایران همچنین نوشته که این دو نفر «اعتراف» کرده بودند که «برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور» با یکدیگر «همکاری» داشته و برای این کار، «سلاح» نگهداری می‌کردند.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75589" target="_blank">📅 09:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/622e876399.mp4?token=YT90GTfASOEeaC4ZwaL6Dlev_IYfIqGcmAVYWJz7ZNbEFLQI_WyZA6PpjVxwPQaRxouQrIx2izhfURuTlioIRf87YFUA0iteVCVNjh48jlt7mOaXcyHdWwOtYb3nK85o_jHx1yi9odlHhqzZKkxvKqrEo4-ShEOJ1Y9WDBP_OHAc4Sr1IjGMd633g-r3ynH3YQxjDGpsfmlCaz_lnCZ76kK8a1zGrYH3IZuyN6jt_-LyXXzdj2iXy58USXiCivdpg51aU_e6IBUE589jZdvZzdTzb85GZ-ol-FWH-5oMCfHvgX3Wk00PbDOUd_vDgsBlgvrREapZQg0XDvw3uBJSnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/622e876399.mp4?token=YT90GTfASOEeaC4ZwaL6Dlev_IYfIqGcmAVYWJz7ZNbEFLQI_WyZA6PpjVxwPQaRxouQrIx2izhfURuTlioIRf87YFUA0iteVCVNjh48jlt7mOaXcyHdWwOtYb3nK85o_jHx1yi9odlHhqzZKkxvKqrEo4-ShEOJ1Y9WDBP_OHAc4Sr1IjGMd633g-r3ynH3YQxjDGpsfmlCaz_lnCZ76kK8a1zGrYH3IZuyN6jt_-LyXXzdj2iXy58USXiCivdpg51aU_e6IBUE589jZdvZzdTzb85GZ-ol-FWH-5oMCfHvgX3Wk00PbDOUd_vDgsBlgvrREapZQg0XDvw3uBJSnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'کمور، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75588" target="_blank">📅 03:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lFUqRofyqXDyw-NimchxsyE62zb0J-M0DGZtIw_Xx-xi4HqGc-d8mG-aNokTkH-y39dZfNgkz0h9JG_JiWHDyBC_R_0wyjYSALzm3ufjQO_j1iC1W7iG0vZz8pZTrsJTEFQZY0fAgUP_ri5GvVxNtXTo8AyOmiJSN7jxeW0e95QcfeG8ei_K0Xy3o-E-Z_iC5vEcezuWsPutB-7kvWDmtojO3qmEGvfqUl9b8-kvyzGkQerSkRn3eKRCp17HoVU42go9rbmJwaAL0fma4kEpCxjqaMtsXnzfvmrsp7mImfyg4i8lPF6l865uBWjWwtdxQFciB7DQ431G1q5sleOwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی کاخ سفید در شبکه اجتماعی ایکس، روز چهارشنبه ۳۰ اردیبهشت در پُستی، عکسی از رئيس جمهوری آمریکا، دونالد ترامپ را منتشر کرد که زیر آن تصاویری از «دشمنان خنثی‌شده آمریکا بدست پرزیدنت دونالد جی. ترامپ» دیده می‌شود.
در این پست تصاویری از علی خامنه‌‌ای رهبر کشته‌شده جمهوری اسلامی، نیکلاس مادورو رهبر دستگیر‌شده ونزوئلا، رائول کاسترو رهبر سابق کوبا، و ابو بلال المنوکی از رهبران داعش که به جای تصویرش پرچم داعش نشان داده شده، منتشر شده است.
کاخ سفید در مورد کاسترو، روی تصویر او نوشت که علیه او کیفرخواست صادر شده است. در مورد مادورو روی تصویر او نوشت که دستگیر شده است. و در مورد علی خامنه‌ای و ابو بلال المنوکی روی تصاویر آن‌ها نوشت که «کشته‌ شدند.»
حساب رسمی کاخ سفید افزود: «عدالت اجرا خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75587" target="_blank">📅 03:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CJPYAIfA0_B1MTTHf0lK3S1GM87fksY9aS9JEsD0chovBkKLRkrL3lFUOccNtevCfmTO7s1qah7bPMOmIEUdj_8PN99IAhtUAHZnRbmgPmFHCQitqO9NGfPz_NUcEWUdqr1-3mWfjM_-TstJzCEwqhGNTbVdFHNT2KMUS5VVeEOND1AhSu7XHQ00uA0DhyOD8LFxBGQ7J5wkbojy49kR5jE19Amnz-4t3GmmV39XFSkrrRms3blohpfDTGsKLFiWUAm_m_nN58QkT_AT8O-aWMzkANvr0Xt9RlqWht9oA5RQWMbu5fjvqVHxR2zD68b-rTgrMSkQpS2VOG3CprkAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیل هیوم به نقل از «منابع آگاه» نوشت جلسه چهارشنبه ۳۰ اردیبهشت در کاخ سفید درباره ایران با اختلاف‌نظر شدید میان مقام‌های ارشد دولت آمریکا همراه شد، اما رییس‌جمهوری آمریکا در نهایت، خلاف نظر وزیر جنگ و وزیر امور خارجه، و همسو با دیدگاه جی‌دی ونس و فرستادگان ویژه‌اش، ادامه مذاکرات با جمهوری اسلامی را تایید کرد.
این روزنامه راستگرا نوشت ارزیابی مارکو روبیو، وزیر امور خارجه، و پیت هگست، وزیر جنگ آمریکا، این بود که در این مرحله، بدون اعمال فشار قابل‌توجه، از جمله تهدید به حمله و تشدید تحریم‌های اقتصادی، نمی‌توان از جمهوری اسلامی امتیاز گرفت. در مقابل، ونس معتقد بود تازه‌ترین پیشنهاد تهران نشانه‌ای از انعطاف است و می‌تواند زمینه حرکت به سوی یک توافق اولیه را فراهم کند.
منابع آگاه از این جلسه به اسرائیل هیوم گفتند که استیو ویتکاف و جرد کوشنر، فرستادگان ویژه دونالد ترامپ نیز در این گفت‌وگو از موضع ونس حمایت کردند.
آنها پیش از این جلسه با رهبران عمان، قطر و عربستان سعودی گفت‌وگو کرده بودند.
به نوشته این رسانه تنش در این جلسه زمانی شدت گرفت که ترامپ از ونس و فرستادگان انتقاد و آنها متهم کرد که رویکردشان به جمهوری اسلامی امکان می‌دهد زمان بخرد و به تصویر ایالات متحده و نهاد ریاست‌جمهوری آسیب بزند. ونس با لحنی قاطع پاسخ داد که دولت باید به دنبال پایان دادن به این کارزار نظامی، بازگرداندن سربازان به خانه، کاهش قیمت نفت و تمرکز بر مشکلات داخلی آمریکا باشد؛ پاسخی که حاضران را غافلگیر کرد.
اسرائیل هیوم در ادامه این گزارش به گفت‌وگوی ترامپ با رهبران منطقه اشاره کرد و به نقل از دو منبع نوشت که رهبران اسرائیل و امارات متحده عربی، همزمان با تاکید بر ضرورت حفاظت از تاسیسات حساس خود در قبال حملات احتمالی جمهوری اسلامی، از پیش گرفتن «سیاست‌های سخت‌گیرانه» علیه جمهوری اسلامی حمایت می‌کنند.
در مقابل، رهبران عربستان سعودی و قطر ترجیح می‌دهند از بازگشت به درگیری‌ها پرهیز شود.
این روزنامه همچنین به نقل از یک مقام آمریکایی درباره تماس تلفنی ترامپ با نخست‌وزیر اسرائیل نوشت که نتانیاهو از رفتار جمهوری اسلامی و احتمال وقت‌کشی تهران ابراز سرخوردگی کرد، در حالی که ترامپ بر پیچیدگی شرایط و دشواری‌هایی پیشِ رو تاکید داشت. با این حال رییس‌جمهوری آمریکا بار دیگر گفت که به رفع تهدید هسته‌ای حکومت ایران متعهد است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75586" target="_blank">📅 02:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GR5JkaPe-F3ct-URa9KgpxoCSn2KzdvQXiGjftC_dpA2Yj075ytejInpPVnUpHOc_A9XBjYWYaTktFfLgrafB_Q1K9MzoGTpW7EOsgPkDcH4yDgxA-j18dlHDpwnWUTIWQwJgXCQ4HhItEYS0UdKc1pBAKeyX2mNLutqz-8295PFxotc0DQ623P5UMpBPselFPYuNkUpvaDz3fpluN2uUWeqBgrTW2-N4OkJ0s0bPG_39Td5hCcrAQUKGbb12r_PuBY6FA8AxOdZxykifBGvbNGq_GqMp1MpHUB1mwOIZe5g97UaYd7uy6vsi6zeya7f_vN4xOFEXGr25DQImIEmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=W2R-le4DikTq-0ZO2rFSSpFal0aM3UQ4X08i1r9YE9i-SjHSbgNn68Zo6VcEWTCAGnky5V4a5DG9uw4l44zuGNK5HKjTL4TCakf-j4XMzbMoJvQ33u6CVT3lwLfA5vZAjMbvbqgtkUChrJYDHd3TAhxOpyfdQQLhxVWiDMaqYfSxkrzi0b5Af1rokFEISFNT-WA36pYJm9FMGsAOmImREyYnlzUcfumPYl-FEu4QyaIIR-68HloeaLoypPVJ7J9wbEV141M_Z0bmL4GMxrpQkZN_LyCLEua8btRdjep_ysSHokP6s51hSiJQAVqXDJUmKRVpCQOyxxHJUyKCe7nrlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=W2R-le4DikTq-0ZO2rFSSpFal0aM3UQ4X08i1r9YE9i-SjHSbgNn68Zo6VcEWTCAGnky5V4a5DG9uw4l44zuGNK5HKjTL4TCakf-j4XMzbMoJvQ33u6CVT3lwLfA5vZAjMbvbqgtkUChrJYDHd3TAhxOpyfdQQLhxVWiDMaqYfSxkrzi0b5Af1rokFEISFNT-WA36pYJm9FMGsAOmImREyYnlzUcfumPYl-FEu4QyaIIR-68HloeaLoypPVJ7J9wbEV141M_Z0bmL4GMxrpQkZN_LyCLEua8btRdjep_ysSHokP6s51hSiJQAVqXDJUmKRVpCQOyxxHJUyKCe7nrlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه چهارشنبه گفت حاضر است «چند روز» برای رسیدن پاسخ ایران به پیشنهاد واشینگتن درباره توافق پایان جنگ صبر کند اما هشدار داد که این پاسخ باید «۱۰۰ درصد درست» باشد.
او بعد از سخنرانی در جمع دانشجویان نظامی به خبرنگاران گفت اگر پاسخ ایران درست نباشد، تشدید تنش به سرعت رخ می‌دهد و افزود: «ما آماده پیش‌روی هستیم. باید جواب‌های ۱۰۰ درصد درست و خوبی بگیریم.»
ترامپ اعلام کرد که آمریکا در حال حاضر با افراد «خیلی خوبی» از طرف ایرانی مواجه است که «استعداد و قدرت ذهن» دارند؛ افرادی که به گفته او جایگزین رهبران پیشین ایران شده‌اند.
این اظهارات ساعتی بعد از آن است که سخنگوی وزارت خارجه ایران اعلام کرد تهران در حال بررسی طرح پیشنهادی جدید آمریکا است.
این طرح توسط اسلام‌آباد به دست مقام‌های جمهوری اسلامی رسیده است؛ همزمان با سفر وزیر کشور پاکستان به تهران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75584" target="_blank">📅 23:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dq9fm8gtSo2fkYhXirbmbPT1EvBsl1yVw2gwzw1LBJMVcEgCCNFkiM_jwIQ0oEOKOvUp9uq7iDouVlICt1eXOv9WTHLy0igcduDhzC0lck1piCH3SsHJbcayY2ujl10ppn_BFLlH-vcwvXriGRjaKJxNNnO6FwEVS17oEEwX1Ag1ra2dTa9oCoIf9NyhOJUKmiL9zUar-YYrcn4tWnJRd11mZkATu-AAs867DxinvWxEl_Gc4oYE8p-iE_PKBSjuSHqUJDcLZo1CafY3NmPrCIGuIMi1J2dsAdInDAy6NhFIBFa7n1ctNLR4Eqk8gmzVrxBnXj6DYh3ggGB12XyXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A6Td4Uo_WZBrcrTaecR5dXk-bAzgiVrHm2g8AeZKDInuqM2IBf6cHosAoAutjfA30Pc7PJXdImc1vGJd3_xJ6BTIVoSFwjhQfnIhsYliMkmITOEfWFqTwmQnsKhRzrGJPjBBkwudF_9BkcLngQpn5sKHrsnUqWvtW1310jRDPBr2Aq2pPBcSlyOop5bTIYK8WkS_P35WeLIgGuCP9h013MdIn5x79Yus8JujKwsJ46-LdWqLQBPl1F4mrviTqD-YwZjf2q-vslUDLvUIwIf6vDjAEuqjhZbYPf4Jbghv4Z2UUz8gOEhQr7i-mYCU6yLYS-KkaPcPtHvLh7CsCdkbJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس در گزارشی اختصاصی اعلام کرد دونالد ترامپ در تماس تلفنی طولانی و «دشوار» خود با بنیامین نتانیاهو، از تلاش میانجی‌ها برای تدوین یک «تفاهم‌نامه» خبر داده است. بر اساس این طرح، آمریکا و جمهوری اسلامی با امضای این تفاهم‌نامه رسما به جنگ پایان داده و یک دوره ۳۰ روزه را برای مذاکره درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کنند.
به گفته دو نفر از منابع آکسیوس، این پیشنهاد با مخالفت شدید نخست‌وزیر اسرائیل مواجه شده و دو رهبر درباره مسیر پیش‌رو اختلاف‌نظر جدی دارند. یک مقام آمریکایی وضعیت نتانیاهو را پس از این تماس، «بسیار خشمگین و آشفته» توصیف کرد.
آکسیوس به نقل از منابع خود نوشت سفیر اسرائیل در واشنگتن نیز نگرانی شدید نتانیاهو از این گفتگو را به اطلاع قانون‌گذاران آمریکایی رسانده است؛ هرچند سخنگوی سفارت این موضوع را تکذیب کرد. یکی از منابع با اشاره به بدبینی همیشگی نتانیاهو به روند گفتگوها گفت: «بی‌بی همیشه نگران است.» کاخ سفید و دفتر نخست‌وزیری اسرائیل از اظهارنظر در این باره خودداری کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75582" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
