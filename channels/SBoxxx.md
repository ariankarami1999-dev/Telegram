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
<img src="https://cdn4.telesco.pe/file/iFvL30BFbhQ9ClRko5oSss88pc8z7X27-jE7x8_eRITLJSIlIp9ptk9CyGQiDMu7aegndMlxtbCzjsnwO6-bY4QpO0EZ9N8rJqu7MmcW74LVhO0-1gBYY13ytDYA2gFyR7UMUAEyO-zz7jtVSnSlD7LLNASoT_xlfDnjN6pW2L3T6HX3SaWGaxJLJPcSjjtOHc7wJZUuTSuvO0cSo9i_AVhXtnJQV41jbJYH51qOeZc1pl4_fQ-7ZkDl0oigQUQA2kBEyzZTVMnjiV-J9s--HqgK74RtwdmJZJMw1isY7KNi8-XSHRrzgmI7r0byQ0oxeWBs1MxIK60RwwptBSUz1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 09:42:44</div>
<hr>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وال استریت ژورنال:
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SBoxxx/20696" target="_blank">📅 09:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جنگ اراده‌ها در تنگه هرمز؛ ایران و آمریکا چه کسی زودتر عقب‌نشینی می‌کند؟
جنگ ایران و آمریکا وارد مرحله‌ای شده است که در آن، اقتصاد به اندازه موشک و نیروی دریایی به سلاح جنگی تبدیل شده است. تهران و واشنگتن هر دو تلاش می‌کنند هزینه‌های ادامه جنگ را به طرف مقابل تحمیل کنند و در نهایت او را به این نتیجه برسانند که ادامه درگیری بیش از دستاوردهای آن هزینه دارد. به همین دلیل، آنچه اکنون در اطراف تنگه هرمز جریان دارد، صرفاً یک رویارویی نظامی نیست؛ بلکه یک جنگ اراده‌ها است که در آن هر دو طرف منتظرند دیگری زودتر تسلیم فشار شود.
از یک سو، ایالات متحده با ایجاد محاصره دریایی و هدف قرار دادن برخی زیرساخت‌ها و نفتکش‌های ایرانی تلاش می‌کند صادرات نفت ایران را محدود کرده و فشار اقتصادی بر جمهوری اسلامی را افزایش دهد. از سوی دیگر، ایران با تهدید شناورهای آمریکایی، ایجاد محدودیت برای کشتیرانی و تلاش برای افزایش هزینه عبور کشتی‌های تجاری از تنگه هرمز می‌کوشد هزینه اجرای محاصره را برای واشنگتن بالا ببرد.
ایران؛ فشار بر مهم‌ترین منبع درآمد
برای تهران، مسئله اصلی اقتصاد است. نفت همچنان مهم‌ترین منبع درآمد جمهوری اسلامی محسوب می‌شود و محاصره دریایی آمریکا مستقیماً توانایی ایران برای صادرات نفت را هدف گرفته است.
بر اساس گزارش شرکت Kpler، حجم نفت خام ایران که روی نفتکش‌های خارج از منطقه محاصره ذخیره شده بود، از حدود ۹۰ میلیون بشکه در اواسط ژوئیه به حدود ۲۹ میلیون بشکه کاهش یافته است. اگر این روند ادامه پیدا کند، فشار بر درآمدهای ارزی ایران افزایش خواهد یافت و دولت برای تأمین هزینه‌های جاری و واردات با محدودیت بیشتری مواجه خواهد شد.
اما فشار اقتصادی تنها در سطح صادرات نفت باقی نمانده است. دولت ایران هم‌زمان مجبور شده قیمت بنزین در بالاترین سطح سهمیه‌بندی را به ۱۰۰ هزار ریال در هر لیتر افزایش دهد. این تصمیم از این جهت اهمیت دارد که افزایش قیمت سوخت در سال 1398 به اعتراضات گسترده در سراسر کشور منجر شد.
بنابراین، تهران با یک معادله دشوار مواجه است: اگر در برابر فشار آمریکا عقب‌نشینی کند، بخشی از دستاورد استراتژیک خود در تنگه هرمز را از دست می‌دهد؛ اما اگر مقاومت را ادامه دهد، فشار اقتصادی و احتمال نارضایتی داخلی افزایش خواهد یافت.
آمریکا نیز هزینه جنگ را می‌پردازد
با این حال، تصور اینکه تنها ایران در حال پرداخت هزینه اقتصادی جنگ است، اشتباه خواهد بود.
بر اساس برآورد لحظه‌ای دانشگاه براون، جنگ تاکنون حدود ۱۰۰ میلیارد دلار هزینه اضافی انرژی بر مصرف‌کنندگان آمریکایی تحمیل کرده است. این رقم با سرعتی حدود یک میلیون دلار در هر دو دقیقه در حال افزایش بوده است. به‌طور متوسط، افزایش قیمت بنزین و گازوئیل از زمان آغاز جنگ بیش از ۷۶۰ دلار هزینه اضافی برای هر خانوار آمریکایی ایجاد کرده است.
فشار اصلی در هفته‌های اخیر از سوی بازار گازوئیل آمده است. قیمت گازوئیل در آمریکا به حدود ۵.۹۰ دلار در هر گالن رسیده؛ یعنی تقریباً ۶۰ درصد بیشتر از یک سال قبل. اهمیت گازوئیل بسیار فراتر از هزینه سوخت خودروهاست، زیرا بخش بزرگی از سیستم حمل‌ونقل کالا، کامیون‌ها، کشاورزی و زنجیره تأمین به آن وابسته است.
در نتیجه، تداوم قیمت بالای انرژی می‌تواند به موج دوم تورمی در اقتصاد آمریکا منجر شود؛ از افزایش هزینه حمل‌ونقل گرفته تا افزایش قیمت مواد غذایی و کالاهای مصرفی.
تنگه هرمز؛ میدان اصلی جنگ اراده‌ها
اینجاست که اهمیت تنگه هرمز دوچندان می‌شود. ایران می‌داند که نمی‌تواند الزاماً آمریکا را از نظر نظامی شکست دهد، اما می‌تواند تلاش کند هزینه پیروزی آمریکا را بالا ببرد.
حمله موشکی ایران در ۵ سپتامبر به سمت دو شناور آمریکایی، هرچند بدون اصابت و تلفات بود، دقیقاً در همین چارچوب قابل تحلیل است. تهران می‌خواهد به واشنگتن نشان دهد که اجرای محاصره هزینه نظامی دارد.
در مقابل، آمریکا تلاش می‌کند با اسکورت کشتی‌های تجاری از مسیر جنوبی تنگه، نشان دهد که ایران نمی‌تواند به‌تنهایی قواعد عبور و مرور در هرمز را تعیین کند.
اقدام ایران برای ایجاد یک «منطقه محدودشده» نیز بخشی از همین رقابت است. تهران می‌خواهد کشتی‌هایی را که از کنترل ایران عبور می‌کنند، با تهدید به قرار گرفتن در فهرست کشتی‌های غیرمطیع، جریمه، توقیف یا حتی مصادره، تحت فشار قرار دهد.
بنابراین، هر دو طرف در حال تلاش برای تغییر محاسبه هزینه ـ فایده طرف مقابل هستند. جنگی که هر دو طرف می‌خواهند دیگری آن را تمام کند. ماهیت این جنگ را می‌توان در یک جمله خلاصه کرد: ایران می‌خواهد آمریکا زودتر از محاصره عقب‌نشینی کند؛ آمریکا می‌خواهد ایران زودتر از استفاده مؤثر از تنگه هرمز دست بکشد.
واشنگتن امیدوار است فشار اقتصادی، کاهش درآمدهای نفتی و تهدید ناآرامی داخلی، تهران را مجبور به پذیرش شرایط آمریکا کند.
تهران نیز امیدوار است افزایش قیمت انرژی در آمریکا، فشار تورمی بر خانوارها، افزایش هزینه حمل‌ونقل و نزدیک شدن انتخابات میان‌دوره‌ای، در نهایت افکار عمومی و سیاستمداران آمریکایی را علیه ادامه محاصره تحریک کند.
این دقیقاً یک جنگ فرسایشی و روانی ـ اقتصادی است. پیروزی لزوماً به معنای نابودی توان نظامی طرف مقابل نیست؛ بلکه ممکن است به معنای آن باشد که یک طرف زودتر به این نتیجه برسد که ادامه جنگ دیگر ارزش هزینه‌ای را که می‌پردازد ندارد.
مسئله زمان
در چنین جنگی، زمان اهمیت تعیین‌کننده دارد.
ایران باید پیش از آنکه فشار اقتصادی به یک بحران داخلی تبدیل شود، راهی برای کاهش فشار پیدا کند. آمریکا نیز باید پیش از آنکه قیمت انرژی و تورم به یک مشکل جدی سیاسی تبدیل شود، بتواند به یک نتیجه قابل ارائه به افکار عمومی دست یابد. به همین دلیل، جنگ در تنگه هرمز بیش از آنکه صرفاً مسابقه موشک‌ها و ناوها باشد، مسابقه استقامت سیاسی، اقتصادی و روانی است.
در نهایت، پرسش اصلی این نیست که کدام طرف می‌تواند ضربه سخت‌تری وارد کند؛ پرسش این است که کدام طرف زودتر حاضر خواهد شد هزینه ادامه جنگ را نپذیرد. و تا زمانی که تهران و واشنگتن تصور کنند طرف مقابل زودتر از آنها عقب‌نشینی خواهد کرد، احتمال ادامه این رویارویی بالا خواهد ماند.</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/20695" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد  تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/20694" target="_blank">📅 07:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد
تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/20693" target="_blank">📅 07:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر دفاع پاکستان، یمن را تهدید کرد:
اگر حملات از سوی یمن ادامه یابد، ممکن است مجبور شویم توافقنامه دفاع مشترک بین پاکستان، عربستان سعودی و ترکیه را فعال کنیم.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20692" target="_blank">📅 02:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNqiejiMkDw3M2wsCNcOgnKriPdFxNzRDET9A-_v4IPf70QRX0fxZ-aCWBgDVhvaBF3qCOLYOFQcWgV2kFUjFzDzQyBHTQBKzAZBXDoJ7I-qg-kDO6XJAyuTKHLpd3k8t8akgDzm7bzz0CiLZVmsH64eUVAvwNigasUidTePyk0anGkX1mg_W59yb4k81PK0qr3Fcz_7e225_K5UhAOFU7paq2sjK-7kNCq_Pfzw09bD_w66DJM-rNLrrd81uqsC5k6PUFjXIbh1lTX_zNJ3DBSqXjCrEpyMBGRUd7kR8ron5Ixoe_JeMb5Q875zGWoyBiNONMLpryMNi5GA05Y9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/20691" target="_blank">📅 02:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=TbwUxa-8teyO6IYV5_aa2ixwv9NwwSoODtaKysYvGamdeAVc_yUN4t5vJWUBOuo_zKZIxGHxrRy0_eyIoOWyV1_R3OATn2HygIakvbpzSd2vf2J-f0tH9NpbnBm-QpoR36-NnPpqUSYZGmYer2SagH4kmPm2okUZiURNt_tUc7BxHtdnzi_SrGLBrCW47Lm2cdU86qwBCC9mbPHeNlOXZgI3JFPijvyXr9beBHd0MR1LvQpnwNAG_ezbhGU-WCKZGEQSleEJ7kVPrt6QdIgBfUGXsRRtJWTzAViO9OtOxz14YPpBUn4Bgg4Cy1Ropdv9DDZ0HkZJw56uES_ShgOiVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=TbwUxa-8teyO6IYV5_aa2ixwv9NwwSoODtaKysYvGamdeAVc_yUN4t5vJWUBOuo_zKZIxGHxrRy0_eyIoOWyV1_R3OATn2HygIakvbpzSd2vf2J-f0tH9NpbnBm-QpoR36-NnPpqUSYZGmYer2SagH4kmPm2okUZiURNt_tUc7BxHtdnzi_SrGLBrCW47Lm2cdU86qwBCC9mbPHeNlOXZgI3JFPijvyXr9beBHd0MR1LvQpnwNAG_ezbhGU-WCKZGEQSleEJ7kVPrt6QdIgBfUGXsRRtJWTzAViO9OtOxz14YPpBUn4Bgg4Cy1Ropdv9DDZ0HkZJw56uES_ShgOiVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/20690" target="_blank">📅 02:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPYFTNsRbMU05u6yqd4ipQueMIM1qFeu8vS2LbWvYWRNFQlikO1pQgWagPdajrdHBOZNUj8xYvbHUpA9nzDlYV5GqfaH8AOIn1-wJl6d3RuHKfTNLcREEX4PoKomyn-wzjsfIlVv-RKTXMeu1llOOSYQyYqLI90LRZnJez4bKHCuTyEoQhvYprNB54-LHVVZmLesyW0VV1nOkps-6Gk-KuluShTlpJRgFKy1QafWUc1Mqy-_TP3zZyZORlFVcavK6WHb0MSXGpqoxDMqLnTP0p12BR6ybLzTE6hhgAvMXZMvpEVqHRlIdE1qUoyQYfALM77RVnqZZuV4YLVYauvXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20689" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، ۵ کشتی نفتکش ایرانی را منهدم کردند.
کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20688" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=cW--XMEQjFNHCBrL7UV_1-exVNxEFIJOm8WLBp2o2CQzpKlWRG0YCCmWf6qMneGEjs9vkYWoxyoLh9JFG2hJqOELm8NJ82Yfe4debBQ-Qyix7ESCfkbY2-FkRM2Dta77Ej3EbZD7Q_F3lS8fOJQWfSFGznXXRoQvLroJ59Xus5pi65fYR638mF8bptAqnEevYa54UZnSfvm0TVN0klDRM5D259GF27B890ScldZkNSCBcVrhyj77kWbIR-Vs-In0NITGTR3Rf-P5VL8UuXeIc6SiZdV2N9LbHv73K1wJ37dRiCKgQnZBct1A06Mm8dNyk9x6vx0D0jlnP7X6hCz2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=cW--XMEQjFNHCBrL7UV_1-exVNxEFIJOm8WLBp2o2CQzpKlWRG0YCCmWf6qMneGEjs9vkYWoxyoLh9JFG2hJqOELm8NJ82Yfe4debBQ-Qyix7ESCfkbY2-FkRM2Dta77Ej3EbZD7Q_F3lS8fOJQWfSFGznXXRoQvLroJ59Xus5pi65fYR638mF8bptAqnEevYa54UZnSfvm0TVN0klDRM5D259GF27B890ScldZkNSCBcVrhyj77kWbIR-Vs-In0NITGTR3Rf-P5VL8UuXeIc6SiZdV2N9LbHv73K1wJ37dRiCKgQnZBct1A06Mm8dNyk9x6vx0D0jlnP7X6hCz2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردنی ها برگ هایشان از مشاهده موشک های با کلاهک بارشی سپاه ریخته !</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/20687" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/20686" target="_blank">📅 01:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من تردید ندارم مرحومه مغفوره برانیگان بخش هایی از اثر خود‌ را برای توصیف پدافند اردن، کویت، بحرین و اندکی هم خودمان خوانده بوده است.
مثلا اینجا به انفجار در پایگاه پدافند و شکسته شدن دیوارهای پایگاه اشاره دارد:
In the night, no control
Through the wall something's breaking
اینجا به تاثیر جنگال و عملیات SEAD روی رادارهای خودی اشاره دارد که کنترل را از دست نیروهای خودی خارج می‌کند:
You take my self, you take my self control
اینجا هم از قول یکی از سربازان پدافند می فرماید از این وضعیت تخمی خسته شده و دیگر اراده جنگیدن ندارد:
I, I live among the creatures of the night
I haven't got the will to try and fight</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/20685" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20684" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20684" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آهنگ زیبای این شبهای خواهرمیانه:</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/20683" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اصابت بیش از ۲۰ موشک به عقبه و الازرق اردن</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20682" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسراییلی ها دارند اذا رمیت میخوانند</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20681" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">موشک های بارشی هم به سمت اردن پرتاب شده و در حال فرود آمدن هستند</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20679" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شلیک های پرشمار موشک های ایرانی به سمت اهداف نامشخص گزارش شده</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20678" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgTf0VRUiargXjeGNev6kdAOl9jsMp3d1t1UKnzMWrKRaomNEAo24AZpQvZJnc5VTD3h2to_y2OYmYEjMYXP7sJ214vQtGu-4eXMI-Bz2G6qlIPBC1ySBC_32oXsCDmseMoKuGaK1xmpT2Roy2wJfR1FRUNGD2H8lpq2DPUDBXuMS_VZjehnsC_DuR8SBAT3aMOni0Z1f_mnTEOkahi6wbsc3A6IsXm4ZY6wVV_M8F9-g8nTQGf5shCliFApg9TwAhxbVnkD6AX736wK_snpIL9_Cd_l7eWGObEqTT0L6OdCmZoY1vgFKURikqkWoKYnc0WcGItE5ehpdyYn2ZZ_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دوباره مرندی ذوالاکتاف به عربها</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20677" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فرماندهی نظامی ایران تهدید کرده است که به نفتکش‌ها در بنادر کویت و بحرین حمله خواهد کرد و به خدمه هشدار داده است که کشتی‌های خود را ترک کنند.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20676" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این هم رونمایی از ربات تماما بومی-محلی ایرانی در نمایشگاه کیش اینوکس  که اینقدر طبیعی ساخته شده که اصلا طبیعی شده   خودشان میفرمایند یک «داده» هستند و چه اسم با مسمایی که ولی خب.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20675" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUIEfpByaNNkjFdPY3yW1ptL7R0Tk-yi2v6E6RbK0CAfX0nNJlSC1py7oGB9_1LeA7ue_IEouL48zHWSK7-cFnpEuc_QeDJm3VAL5ZIG67Y9u1M5-LGaiBKwZ1exvDDGDkBdkHFLUPLdSGg1-9ryYpNk6j6xaIK-CncOdt6zpAJLu5fbxM4FEKnln_DMP4HBv7XD9qZ_ELPOFBNcjIU65DJFXAQi9Qav-Pzlumz6oyMR6KCVu5-Hqo0XD1naa9QOAmmKsmXrCwD6V1ppJzO3L0DmyJ475FaJw6ChhB7LjjzvngsY00BHutREtxWlH_dHxxDj_JDyKjWrgusQb_gWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش هایی از حضور ربات های نظامی اسراییلی در حمله به مواضع حزب الله خصوصا در علی الطاهر منتشر شده که توان حضور در تونل های زیرزمینی را داشته اند!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20674" target="_blank">📅 23:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار در خارک!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20673" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجار در خارک!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20672" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گفته می شود چند نفت کش ایرانی هدف قرار گرفته اند</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20671" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">باز هم ریزشی است تا 4355 دستکم .</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20670" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شلیک های جدید از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20669" target="_blank">📅 21:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مصطفی عامر از رهبران انصارالله :  سپاس و ستایش خدایی را که عربستان سعودی را پر از نفت کرد و به ما کبریت داد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20667" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKRyzn4amMGUp2u0s_CC1vzLN9_4_fjZWr-udat9TqIhduW6-2qGtsIEDHlnJmpdveQAMnwF14SqbuU_DtMirQpvd6wTcltkWs-JIpHoJgAoo3jjWQKfQvqYoax-lhwWN_nS-l2-1rkCVAX-NzSU0Zwus7LLka-xtf2kL6ww5wrx4m2A779tPAVghYJDK1eK7BFsGL_NQNjjy98ixflhC-miczqvH6XBMBJWJOoUJ61NfZDQuQ0BRGB7uMfIaQe9h1Ys1dqyZcF3UV_XjpJkCc-4EBaUN3KTwbyiZXbcUHve17Cz9_IhOvCumD2cYFDSuNdhAfzl_Po6osNqFJXpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">video_2026-09-08_19-52-57.mp4</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20666" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">video_2026-09-08_19-52-57.mp4</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20665" target="_blank">📅 19:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">video_2026-09-08_19-52-57.mp4</div>
  <div class="tg-doc-extra">1 MB</div>
</div>
<a href="https://t.me/SBoxxx/20664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ویدیویی از انبوه تویوتاهای نیروهای مورد حمایت سعودی که به سمت جبهه های جنگ با انصارالله (حوثی ها) پیش می روند!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20664" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20663" target="_blank">📅 19:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20662">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب منظور این بوده!  یک شهپاد زیرسطحی است  (شناور هدایت پذیر از راه دور)</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20662" target="_blank">📅 19:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20661">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هاآرتص
:
حاکم امارات متحده عربی ۱۰ روز پیش از ۷ اکتبر درباره حمله تروریستی حماس به نتانیاهو هشدار داده بود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20661" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAHJOp-F2TIxUtgWf5JLdg2BGjCuR8QbQH-C0grJ9rZ2okgUJibai-S51LX0dmw-nUiU_xOFymdBaRI8n-px2gknHi-xdv0zJdii9IKU_Z5YcH8uKJo5t7AFEQAYjPJrqMBa2HNOn51_iolQ0BULzDxxGTP_n3KOxu-zaRpL9nE9Wkoa-IHFo2p_Wz3eGtBNF9CMhHUkwPD86mYLpH9A2RmVEk2H1bmk2CQ9ZZ6-l-RzUCPWlB44Cnpa-tUaFGDaiWYa4_aHk-JD6G-drSQDCVEIER6t8CZ9VOiKHHqkZFc2WxJkZCMB0juemAgfajizwYVMi82oV4DT1Ae_9yyaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  به لطف پروردگار متعال، رزمندگان نیروی دریایی سپاه پاسداران انقلاب اسلامی موفق شدند در ورودی تنگه هرمز، یک فروند از جدیدترین زیردریایی‌های پیشرفته متعلق به ارتش تروریستی آمریکا را به دام بیندازند.   این عملیات در یک…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20660" target="_blank">📅 18:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
به لطف پروردگار متعال، رزمندگان نیروی دریایی سپاه پاسداران انقلاب اسلامی موفق شدند در ورودی تنگه هرمز، یک فروند از جدیدترین زیردریایی‌های پیشرفته متعلق به ارتش تروریستی آمریکا را به دام بیندازند.
این عملیات در یک اقدام اطلاعاتی و عملیاتی پیچیده، صبح امروز انجام شد. این زیردریایی پیشرفته، مجهز به جدیدترین فناوری‌های موجود در جهان در زمینه زیردریایی‌ها بود و در سال 2025 به ناوگان ارتش تروریستی آمریکا تحویل داده شده بود.
لازم به ذکر است که این زیردریایی به دست گرفته شده است و تصاویر آن در چند ساعت آینده منتشر خواهد شد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20659" target="_blank">📅 18:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو:
ما به جنگ نهایی با ایران بسیار نزدیک هستیم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20658" target="_blank">📅 18:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کرملین: پس از بازدید نمایندگان ایالات متحده، پوتین و ترامپ در یک تماس تلفنی «بسیار صریح» گفتگو کردند
پوتین به ترامپ گفته که روسیه هیچ «طرح تهاجمی» در قبال اروپا ندارد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20657" target="_blank">📅 17:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الاخبار: ترکیه در حال میانجیگری میان دمشق و حزب‌الله است  روزنامه الاخبار لبنان: ترکیه در یک حرکت دیپلماتیک موازی با تحولات منطقه، در حال میانجی‌گری برای تقریب دیدگاه‌های حزب‌الله لبنان و دولت موقت سوریه است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20656" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الاخبار: ترکیه در حال میانجیگری میان دمشق و حزب‌الله است
روزنامه الاخبار لبنان:
ترکیه در یک حرکت دیپلماتیک موازی با تحولات منطقه، در حال میانجی‌گری برای تقریب دیدگاه‌های حزب‌الله لبنان و دولت موقت سوریه است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20655" target="_blank">📅 15:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 25</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
سه شنبه 8 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20654" target="_blank">📅 14:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رائفی پور ورژن مونث بدحجاب موجود شد</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20653" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….  به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20652" target="_blank">📅 12:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa849e433.mp4?token=c5EvfJEIWqlEIMQU6Mvq1_5qK_qxPKM1fEVts1AMo0_Y96EtyXt9aj4lUAiHOA9aD8p9sdLwrg30-aB6bXfyRbWtToUSCHmHBpWzpxyUE-52MJItk4jryJ47l12K6gcmiY2fC76wsOh7sFAzaelKC3s6NZHlO47OAvFFy7y9pZ25be2F-Q9DxcZia1_be2C7RfMJCTvD-qaHDFlY2th-UCp0ioFt0IyFVRk0-7PzKBdNDsM2GtKuKF9b1Vld3rL6YvfXMUj2lxjRWtc6ShW6GAECc960C3scVU8ruWQMwE-ptgN7HAb1F8zWVX7vB4FYhgK3MZtcmwdbD_ytyETncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa849e433.mp4?token=c5EvfJEIWqlEIMQU6Mvq1_5qK_qxPKM1fEVts1AMo0_Y96EtyXt9aj4lUAiHOA9aD8p9sdLwrg30-aB6bXfyRbWtToUSCHmHBpWzpxyUE-52MJItk4jryJ47l12K6gcmiY2fC76wsOh7sFAzaelKC3s6NZHlO47OAvFFy7y9pZ25be2F-Q9DxcZia1_be2C7RfMJCTvD-qaHDFlY2th-UCp0ioFt0IyFVRk0-7PzKBdNDsM2GtKuKF9b1Vld3rL6YvfXMUj2lxjRWtc6ShW6GAECc960C3scVU8ruWQMwE-ptgN7HAb1F8zWVX7vB4FYhgK3MZtcmwdbD_ytyETncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی پور ورژن مونث بدحجاب موجود شد</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20651" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn0KFsl6n6B7CVeb-719CIHvoOw7DAbzQrZTBes6JKccyYF_J8vJOeDh3iY4423tZQeKK1P2H4FxCn8fVt2dd7PUByQNGyWPsFGk0CYiCPU_CFVRjWXgAFunCdf4qLx30zUQisdtimFZWpoIrgS5WopMCQsfz5maXhAYY1slWOvKlCR5dTFCQUBBzmQI3niakaQnTsqHqAPKsJRbitY4IU94_b6wmDxfkXERcICsbdDTdaLKoepTDQx1Xij1a-JrC10fFgt0uD8GnDo7NDVOrWkdFP4Rb_VsbSdINcql1dtaAS75TmyKole6cH5u8rhZaI-lfUZbO4QiAfsriu0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولکس‌واگن با پیمانکار دفاعی اسرائیلی «رافائل» توافق‌نامه‌ای امضا کرده است تا کارخانه خود در اوسنابروک، آلمان را به یک مرکز تولیدی برای قطعات سامانه دفاع هوایی «گنبد آهنین» اسرائیل تبدیل کند.
انتظار می‌رود این کارخانه در سال ۲۰۲۷ تولید خودروهای سواری را متوقف کند و به‌جای آن به تولید کامیون‌ها، ژنراتورها و سکوها برای پرتاب سامانه‌های گنبد آهنین بپردازد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20650" target="_blank">📅 10:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی از اصابت به فرودگاه ابها و شنیده‌شدن انفجار در مناطق جنوبی عربستان منتشر شد.
این حمله سومین حمله به تأسیسات نفتی عربستان در کمتر از ۴۸ ساعت است.
‎</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20649" target="_blank">📅 10:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">220 پیپ</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20648" target="_blank">📅 09:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20647" target="_blank">📅 09:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfe837d4b.mp4?token=g4fyri-og1U0axOr3dpAw31y92JDpnJJH8-zB0fSUNJ4q9N5Lmpf8MEZAfMv2Ns1FPU2bewo-z2m-KPgpJVRfdI9CkDr5NjQpx0o5tnPo37UPX6XdFQYMuXaWIn_MTQhe0z81731lXf0z9sZOqzKFMuDyFhlw_aPgEIEiPqjtpaGPvKGifQp1MlcqIAdm99ZYryXOJEwhEBim2rDdbEr4urMsABl3zfq_u-0TeE2YaXQ_pahxjQ9Zq2Zu2y8q7I1vgvjbX4Yi_XM7A47rCRqbJzdWDFS8WgkhWGm1cKQuhZ7JcZClGTBtWpateuMt5kmP-k_xs0DVmUzSy4Q37ulPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfe837d4b.mp4?token=g4fyri-og1U0axOr3dpAw31y92JDpnJJH8-zB0fSUNJ4q9N5Lmpf8MEZAfMv2Ns1FPU2bewo-z2m-KPgpJVRfdI9CkDr5NjQpx0o5tnPo37UPX6XdFQYMuXaWIn_MTQhe0z81731lXf0z9sZOqzKFMuDyFhlw_aPgEIEiPqjtpaGPvKGifQp1MlcqIAdm99ZYryXOJEwhEBim2rDdbEr4urMsABl3zfq_u-0TeE2YaXQ_pahxjQ9Zq2Zu2y8q7I1vgvjbX4Yi_XM7A47rCRqbJzdWDFS8WgkhWGm1cKQuhZ7JcZClGTBtWpateuMt5kmP-k_xs0DVmUzSy4Q37ulPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تببین مگاپروژه هوشمندسازی پمپ های بنزین !
حتماً ببینید.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20646" target="_blank">📅 09:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut5uLic38hfjQkyBZ9oCsEBnM44bZSNA7n0Tido7_4Lf7MqgoNS_k1AxvP136-KlqlBP6a-L3gh8sINmg935gBR5smW33OHhAAoWdZb94Y5qOoo924zEQ7eJABbo4ugubFWU7IMlOvJNbF0ww2HWHXCvq1Fq8OvpE2wDXbaJhIpq2oBdqnfNBGCgxKcFMxEcBsQwk1jktOKIUsuh9Be1lznmSfjqpbKG4iPSC-ndAvT6uLsyATCQcL-yaGRh9taOv8_ks07JsCIKQr5W8F6orVOoOKfprjjuykH7JK72Wv3OFhk1fbzN1AI-Bv6IUoVTtb_3vDNAc1CG3l46iCq-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت یمن</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20645" target="_blank">📅 09:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsiKacB_DBhlyVDbQYAiA-IudyDH0FIGl9CpVnGitFS404apVo2p9Qg8L38hN452OQjWw8cpjA8b0ZPsnKCWh9qpPyKJFhGflghCj4jtIgntQ2O4Oki4w829Aeo-QOmOnUH4hDVDAclS8KqYFMU5DS1tdzKTFE05Li-Bd6BS9FFE_rcZJ70b8RwfkTx6njdEzI7qlMa0oYYdXXNsWR_bisIff592xU3wMJFwQC0NdcFCRMJCCcsbQz6pshpH9OG5BqZ9wDVzaJTcz8nAmpgFkpi28v0eXZUWmeEQzPkkCQ3JvFWiwNaL7lgbxps4EGAgkLGba7rQK5eUqSEQFviGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20644" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgZRUZ_KljHjTkp_4vFXLaXZ8MIijLMbaQ4AFVbA3V4PS68hRl6GGLS4ZLbFfFHsQGo_t_ITslWricY7Qp6C8Tj2xyuRLN0R-kr5klIf_DKKwInWfgPorFXYjEsDKBa_0F0uKzLlv3W9_JUmhKKFHHPeoIJdDozKdZJysfLYBUGNboWo6ZqYPL1v8dYSnpbcbAWwv-5c8KxrDwIlXp01aRZJwW8u0v2GRHnKDHz-qtSog6Aut8VE81c2kyobAg0-3BSEyCRicIJKOC0tGnJrNJRAew4k6JXm-VM608hvyxFaojYUuSbggIbTT9COGJolw9zZlxuoJBhg4tjPIOmCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20643" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سفر امشب ویتکاف-کوشنر به روسیه قطعا با افزایش تنش میان آمریکا و روسیه به دلیل تصویب قانون تحریم های گراهام و متعاقبا انتشار گزارشهای موثق از کمک نظامی روسیه به ایران برای ساخت موشکهای کروز ضدکشتی و سپس اعلام ترامپ دال بر ازسرگیری ارسال تسلیحات برای متحدین…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20642" target="_blank">📅 08:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnsTnbT9OjB9X6IS17xI9QivKzFIhd9qAd_9CzSQKaAElR8mNEgCnRV828lruLv762cyWVCyqTcr1csAJ0WZkLQHgUmbm4gh9CcgyjmBAbC4n4dLfWIZPm7kujWzmAroz1gAmiWdGhHYWfaI1cmtbJSlaZDbUTbr31sHW_hQbGMMs4MhPmd8T2_tK1B3avQOJQyIMCb49s0qRTljXKsYKBNPaF4SpEwbN7YwjUtQEPHitB9Wfskx90oCYsMu2jAv7b8Ui4pKF0H-QZH-6jUTxu6XrTBiKm8ZwPEnMk-yFhF6qukbgpQ8EjRp3JnzkejmbUmvX6Jf9cCbVicY9iJGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران شرایط جدیدی را برای پاشینیان در مورد "مسیر ترامپ" مطرح کرد.
ایران به طور غیرمنتظره، شرایط سخت‌گیرانه‌ای را برای نخست‌وزیر ارمنستان، نیکول پاشینیان، در مورد پروژه TRIPP تعیین کرد، در حالی که لحن دوستانه‌ای را در بیانیه‌های عمومی خود حفظ کرده است.
تهران خواستار این شد که امنیت این پروژه توسط نیروهای مسلح ارمنستان به طور انحصاری، یا توسط نیروهای نظامی یک کشور ثالث که از قبل در ارمنستان حضور دارند، تامین شود - به وضوح، منظور نیروهای روسی است.
به گفته منابع، به این ترتیب، تهران تلاش می‌کند از حضور نیروهای آمریکایی در مرزهای خود جلوگیری کند. در غیر این صورت، در شرایط تشدید تنش، طرف ایرانی، حضور آنها را به عنوان یک هدف مشروع تلقی خواهد کرد.
این موضوع، اجرای پروژه‌ای کلیدی که از قبل عملاً فلج شده است، را به شدت دشوارتر می‌کند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20641" target="_blank">📅 00:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سارا خلیفه مجری مشهور مصری به دلیل قاچاق مواد مخدر به اعدام محکوم شد!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20640" target="_blank">📅 00:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ای لعنت به پدر مارک بوسنیچ که گذاشت آن گل را بزنی و بعد ۳۰ سال مجبور بشویم چهره و رفتار انیرانی ات را تحمل کنیم!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20639" target="_blank">📅 00:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سمیر الصبری، معاون وزیر دفاع دولت رسمی یمن:
«تصمیم برای آزادسازی صنعا و حل مسئله گرفته شده است».</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20638" target="_blank">📅 23:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک آزمونی هست برای تعیین قطب نمای سیاسی شما
این
گزارش نتیجه آزمون
برای من است</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20637" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارتش ایالات متحده در حال حرکت برای استقرار راکتورهای هسته‌ای کوچک است، در حالی که برای مقابله با تهدیدات فزاینده علیه شبکه برق و افزایش تقاضای انرژی در پایگاه‌های نظامی آماده می‌شود.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20636" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXDWRVcscRI5qdbsSO0OXSejgN7fYiHG3nEXKhFhhb3OKjmIczsb_Xpi1HE1gw-G1gaQsBoELk5aOf9BCivaL_9WEeNKjQNfyo16YDu4qjish-inmDEMak-MMhqiizcWmDg6-hLyYs8j60SEGHnorXbnCLregURpyF98oeyeMD4QFQ0zOZgmIBqvLzXaIcGrU5LnQ8VpkqdZ7ZzvcCZWw6DL7sawiA7zkdzwpi2f99kR-CgGN2GEGq9k40lEueD9pLOxTJKjjknfROFv5No95PYB6ceqsJmUwTMJNXMYIzI3II-UoWIVliFQWhd1OkBk6nOVfBQivc0t7pv5Q3HJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سارا خلیفه مجری مشهور مصری به دلیل قاچاق مواد مخدر به اعدام محکوم شد!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20635" target="_blank">📅 20:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علی‌آبادی، وزیر نیرو :   تمام نیروگاه های کشور برای تامین برق در آماده باش کامل هستند</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20634" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">علی‌آبادی، وزیر نیرو :
تمام نیروگاه های کشور برای تامین برق در آماده باش کامل هستند</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20633" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNsEQfZSn1oaHzQ6DOrXUyFqoXyDFescJkYPNxXNKOQW7mwM6TIapI6uRv7HmBIwRrDoEV0s4FMhXnnp-CY2yMpu0uj88oG3P_xy7DcHl_scc07LmJ2lOrGrB_GvXw0QXEMq4I3R19xorud69u-Phfws8xW98fcExPgJA-2X7U9YSuSP10Wzsh5ukdgB4529bYyrL3e7q7N7-CEe2cdRmPhoG2_xCMI-Tt_L8hlDW9AH03omgF_CFwZxfmtmpcHjAm6SP0sNT1ichG9OSdzBm9A8vG5zP7BhUMCO5GG2sdisnrekCNXNeTyhRTVEdINOcZKQQbosqqIb5__yfcmXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20632" target="_blank">📅 16:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20631" target="_blank">📅 16:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20630" target="_blank">📅 16:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">همزمان بیت روحانی فعال شده اند....</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20629" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حملات به تاسیسات شرکت سعودی آرامکو</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20628" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 24</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20627" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 24
دو شنبه 7سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20627" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بقایی:   مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20626" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بقایی:
مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20625" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20624" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=Xyn7nh1Kvwf_Q0jruhe6sIyfle0kYkkcQJvwNCpqpu4IwkULsRkmOvIn3L8jDGN8sSVk6PCAtXyu12yRnYAVhv0QfkgWWUwKhdFVjg72NbpoAlRKijD2FBUjMIdY1TErdHIJszPuIVw2ckN7FzEdPhKtN5qxVJNe-yjN8Kb8enju2SFUh0zxAS8auPXy2QLJyzSx3SDeO5AQpX3pk1R21dt7jzwUTulaGk82lijB9svnGDkp0WMZvDQt1LgUbsn2-GT3R2jHY3qys0jJb-oWBTy6nnA3gnTfTS17a6TG2MdBnSOFlM9C90fzY0AZ_yaFHCI_hjeHA8_o1WxtpF-HVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=Xyn7nh1Kvwf_Q0jruhe6sIyfle0kYkkcQJvwNCpqpu4IwkULsRkmOvIn3L8jDGN8sSVk6PCAtXyu12yRnYAVhv0QfkgWWUwKhdFVjg72NbpoAlRKijD2FBUjMIdY1TErdHIJszPuIVw2ckN7FzEdPhKtN5qxVJNe-yjN8Kb8enju2SFUh0zxAS8auPXy2QLJyzSx3SDeO5AQpX3pk1R21dt7jzwUTulaGk82lijB9svnGDkp0WMZvDQt1LgUbsn2-GT3R2jHY3qys0jJb-oWBTy6nnA3gnTfTS17a6TG2MdBnSOFlM9C90fzY0AZ_yaFHCI_hjeHA8_o1WxtpF-HVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20623" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در استرالیا استفاده از مواد روانگردان برای مصارف خاص درمانی قانونی اعلام شد.  پس از قانونی شدن ماریجوانا در بسیاری ایالت های آمریکا، قانونی شدن استفاده از مواد روانگردان طبیعی در موارد خاص در استرالیا پیشرفت مهم دیگری محسوب می شود.  شخصا باور دارم که بزودی…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20622" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20621" target="_blank">📅 11:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTWtyqOgnNYV62Uqrp7XyED8Suijdb5T-fcbwS9i6yUwl2OkLoqowjZC6AymrTUih0SC8m363V8k0Gzdd3_4VC8rMFUx6wL5FM9X_vkYSPMJXG0DUmDiCoKh8V9XOoDovMR0Iy7dleRPCt8ayp6-suYhCqnAeLuXL3ox1I-jS6UBEcuLz91ott44IKOun-b-Sh3Va2cMDAK3GY5LnzEdON_SPHchRvbKU5nn6PW5cLOZJ5PSFVzkhzkE9ooZkBd9-TMc2o48-arF_NDVXQzB-8IvcRMMPovYM8vux65hbuRALWgNvk3i3NnX9UjWZdELheLV92wSep-8lthV7GlENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20620" target="_blank">📅 11:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZuGF7U1o153GQIZz_iznfOPV4SKMuxDZccowmK1ZZ3wRfF5jVIauvF9mzMaCNLXk-toP18zsCx3G-6AB8xXAHnRQzPwDcYIGYUZ2UVZ2ZojVfyjhU0DpM4j0eb8_VZ3r2Kdb62u6-0TV1GxcBdFbbYsYBKl2Le1LTbA2QhizPXs9_gnQmqadZVHwU-o77gqu4S6MYN5J7cGf1OvvYFaBMov404Ph5r4wvn0JNZW5eupT7eOGthGSD1Kx7tQ9r22BW0bx9byq5XObQiVVWzDAxaeVNfKN_rfkH-kQNDAiT6hwHjTKhZz88Mlz0vZG28nJpLImVqIX7aBKW_F2jjETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای لعنت به پدر مارک بوسنیچ که گذاشت آن گل را بزنی و بعد ۳۰ سال مجبور بشویم چهره و رفتار انیرانی ات را تحمل کنیم!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20619" target="_blank">📅 11:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20618" target="_blank">📅 09:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">— به گزارش رويترز، پس از حملات اخیر ایالات متحده و ایران به تانکرها، حجم حمل‌ونقل از تنگه هرمز به‌شدت کاهش یافته است.  داده‌های شرکت کپلر نشان می‌دهد که میانگین روزانه کشتی‌های کالایی در ۱۰ روز گذشته ۱۰ کشتی بوده است که کمترین سطح از ماه مه به این طرف است.…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20617" target="_blank">📅 08:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4lIx0CxRWFDU1pCjJNolQc6JOCf4QF-oFCdn7hcqsjj-u1eCzQ11EhSDHcDYuDJSBe-HP0wc2rAq66P7lgEdr2PHO1L8TEq-iOmofMcp-htQcbFsKVtlEe1QD7Ctj4nLR26n59STw-EdDi7NqNXLR0nwKe_PxIKGwyCozzGxO08zD8V_rwOxV_lJvM8l0_P2R9bQGwU5vAeO-WuDSWX2hTLaZ9-wcNxaVvATEn9KuEc9mBITUwfYkbbvXyHdy2QHYvObPvCvErY8ppHsnCruCqtFp0Wpgdv4H8567Vxx7NIbuluAksk_v7da3Ls67bPocfqzj3NslRkwxTg-IOr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!  به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20616" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20615" target="_blank">📅 02:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp5vDhJiDix7MMOF9QPNFICJeB2oVC4PuuALrxfCvFbcFWS3FSwSsrFhSkJWqBqNu8wLdrWQczwEFvjT6IEP7UyFPQn1N6tGtUJZyB51tSMZOjQberx75AyCweYCRA5OytyV7OMPIsTSwCaRvT4hQl5HEOVcZN69quNioZCImoWD30xBSqooHR8tMZsGRppTHoFkCNT5pMrAKtrzaC7vRb-A1Qb1ckMcT6rfHTQ-frcmtfdWzwwVqzM2agFQRVuXF7jH1x7RtPinLrDE2QMjOQvcJhFlTl2OYzwkfcAlUL0xV-OQOoM4gvJddXskajUOBQZMuyIwePVBtWSJQs-Ofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه میان‌مدت ترکیه برای سال‌های 2027 تا 2029، افزایش 229 درصدی در هزینه‌های دفاعی را پیش‌بینی می‌کند، که از بین تمام دسته‌های سرمایه‌گذاری استراتژیک، بیشترین میزان افزایش را داراست.
این رقم، هدف کلی برای سه سال است، نه افزایش در یک سال معین.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20614" target="_blank">📅 01:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آیا ارمنستان در حال تبدیل شدن به هاب هوش مصنوعی آمریکا در قفقاز است؟
ارمنستان در حال ورود به مرحله‌ای جدید از توسعه اقتصادی و ژئوپلیتیکی خود است؛ مرحله‌ای که در آن زیرساخت محاسباتی هوش مصنوعی می‌تواند به اندازه فناوری نرم‌افزاری و استارتاپ‌ها اهمیت پیدا کند. راه‌اندازی کارخانه هوش مصنوعی شرکت آمریکایی Firebird در نزدیکی هرازدان در اوت ۲۰۲۶، این پرسش را مطرح کرده است که آیا ارمنستان در حال تبدیل‌شدن به یک پایگاه راهبردی آمریکا برای زیرساخت هوش مصنوعی در قفقاز جنوبی است.
پاسخ کوتاه این است که هنوز برای نامیدن ارمنستان به‌عنوان «هاب هوش مصنوعی آمریکا» زود است، اما شواهد موجود نشان می‌دهد که این کشور در حال ایجاد زیرساختی است که از نظر مالکیت فناوری، تأمین تراشه، نرم‌افزار، سرمایه و مجوزهای صادراتی، به‌شدت به اکوسیستم آمریکایی وابسته است.
ورود
Firebird؛ نقطه آغاز یک تحول بزرگ
مرکز ثقل این تحول،
پروژه Firebird
در هرازدان است. این شرکت آمریکایی در ۸ اوت کارخانه هوش مصنوعی خود را به‌طور رسمی افتتاح کرد و اعلام کرد که برنامه دارد تا پایان ۲۰۲۷ بیش از ۷۰ هزار GPU شرکت NVIDIA از نسل‌های Blackwell و Vera Rubin را در ارمنستان مستقر کند و ظرفیت زیرساختی آن را به حدود ۳۰۰ مگاوات برساند.
این ارقام در مقیاس اقتصاد ارمنستان بسیار بزرگ هستند. پروژه فقط یک دیتاسنتر معمولی نیست؛ بلکه بخشی از مدل جدید AI Factory  است که در آن برق، سرمایش، شبکه، سرورهای پرقدرت، GPU و دسترسی به مدل‌های هوش مصنوعی در قالب یک زیرساخت یکپارچه ارائه می‌شوند.
دولت ارمنستان حتی ارقام بلندپروازانه‌تری را مطرح کرده است. بر اساس اعلام دفتر نخست‌وزیری، در مرحله دوم سرمایه‌گذاری کل پروژه به بیش از ۴ میلیارد دلار خواهد رسید و حدود ۵۰ هزار GPU جدید NVIDIA Vera Rubin به زیرساخت اضافه خواهد شد. مرحله سوم نیز قرار است ظرفیت کلی را به بیش از ۱۰۰ هزار GPU و بیش از ۴۰۰ مگاوات برساند.
البته باید میان ظرفیت فعلی و اهداف اعلام‌شده تفاوت گذاشت. تحلیل‌های مستقل تأکید می‌کنند که رقم ۷۰ هزار GPU و ظرفیت ۳۰۰ مگاوات عمدتاً یک نقشه راه توسعه تا ۲۰۲۷ است و تحقق آن به تأمین برق، سرمایه‌گذاری، تحویل تراشه‌ها و وجود مشتری کافی بستگی دارد.
نقش تعیین‌کننده آمریکا
وجه مهم‌تر پروژه، صرفاً اندازه آن نیست؛ بلکه منشأ فناوری و نحوه دسترسی ارمنستان به آن است.
شرکت Firebirdیک شرکت آمریکایی است و پروژه هرازدان بر پایه فناوری NVIDIA و زیرساخت Dell شکل گرفته است. علاوه بر این، توسعه مرحله دوم پس از دریافت مجوز صادراتی آمریکا برای انتقال هزاران تراشه پیشرفته NVIDIA به ارمنستان امکان‌پذیر شد. دولت ارمنستان می‌گوید مجوز اضافی برای ۴۱ هزار تراشه NVIDIA GB300 صادر شده است .
این نکته از نظر ژئوپلیتیکی بسیار مهم است. در عصر هوش مصنوعی، کنترل دسترسی به GPUهای پیشرفته عملاً بخشی از قدرت ژئوپلیتیکی محسوب می‌شود. واشنگتن نه‌تنها بر تولید بخش بزرگی از تراشه‌ها و طراحی آنها از طریق شرکت‌هایی مانند NVIDIA تسلط دارد، بلکه می‌تواند تعیین کند چه کشوری به پیشرفته‌ترین نسل‌های محاسباتی دسترسی پیدا کند. از این منظر، ارمنستان صرفاً یک مصرف‌کننده فناوری آمریکایی نیست؛ بلکه در حال تبدیل‌شدن به محل استقرار بخشی از زیرساخت محاسباتی وابسته به اکوسیستم آمریکا است.
«دیپلماسی تراشه» و قفقاز جنوبی
اهمیت این موضوع پس از گزارش اخیر
Wall Street Journal
حتی بیشتر شده است. این روزنامه گزارش داده که دولت آمریکا در مذاکرات مربوط به توافق صلح ارمنستان و آذربایجان، از دسترسی ارمنستان به تراشه‌های پیشرفته NVIDIA و پروژه Firebird به‌عنوان بخشی از بسته اقتصادی و تکنولوژیک استفاده کرده است. WSJ این رویکرد را نمونه‌ای از Chip Diplomacy توصیف می‌کند.
اگر این گزارش را در کنار پروژه Firebird قرار دهیم، تصویر بزرگ‌تری شکل می‌گیرد: آمریکا در قفقاز جنوبی فقط به دنبال روابط دیپلماتیک سنتی نیست؛ بلکه می‌تواند از فناوری پیشرفته، سرمایه و زیرساخت محاسباتی برای ایجاد پیوندهای بلندمدت اقتصادی استفاده کند. این تحول از نظر ژئوپلیتیکی قابل توجه است، زیرا ارمنستان در نقطه‌ای قرار گرفته که میان روسیه، ایران، ترکیه و آذربایجان واقع شده است. ایجاد یک مرکز بزرگ AI وابسته به فناوری آمریکایی در چنین موقعیتی، می‌تواند حضور اقتصادی و تکنولوژیک واشنگتن را در منطقه افزایش دهد.
چرا ارمنستان؟
مزیت ارمنستان فقط موقعیت جغرافیایی نیست. دولت این کشور طی سال‌های اخیر تلاش کرده است خود را به‌عنوان یک اقتصاد فناوری‌محور معرفی کند و از سرمایه و نیروی انسانی دیاسپورای ارمنی نیز استفاده کند.
اما مهم‌تر از آن، دولت در حال ایجاد تقاضای داخلی برای Compute نیز هست. در آوریل ۲۰۲۶، وزارت صنعت فناوری‌های پیشرفته ارمنستان قراردادی پنج‌ساله به ارزش ۲۵ میلیون دلار با Firebird امضا کرد تا منابع High-Performance Computing را برای استارتاپ‌ها، پژوهشگران، دانشگاه‌ها و فعالان حوزه AI خریداری کند.
این اقدام بسیار مهم است، زیرا مدل توسعه صرفاً بر صادرات خدمات دیتاسنتری متکی نیست. دولت می‌خواهد یک اکوسیستم کامل ایجاد کند. همکاری دولت با شرکت‌هایی مانند AWS و Mistral AI و ایجاد «Artificial Intelligence Virtual Institute» نیز بخشی از همین تلاش برای ساختن اکوسیستم داخلی است.
اما آیا ارمنستان واقعاً «هاب آمریکا» خواهد شد؟
در اینجا باید محتاط بود. یک دیتاسنتر بزرگ الزاماً به معنای تبدیل‌شدن یک کشور به مرکز نوآوری AI نیست. برای ایجاد یک هاب واقعی، ارمنستان به نیروی انسانی متخصص، دانشگاه‌های قدرتمند، شرکت‌های نرم‌افزاری، سرمایه خطرپذیر، مشتریان بین‌المللی و مهم‌تر از همه برق ارزان و پایدار نیاز دارد.
مصرف انرژی نیز یک چالش اساسی است. صدها مگاوات ظرفیت AI برای کشوری با اندازه اقتصادی ارمنستان عدد بسیار بزرگی محسوب می‌شود. بنابراین توسعه Firebird به همان اندازه که پروژه‌ای تکنولوژیک است، یک پروژه انرژی و زیرساختی نیز محسوب می‌شود.
از سوی دیگر، رقابت منطقه‌ای نیز در حال شکل‌گیری است. Firebird همزمان در حال توسعه پروژه‌های زیرساختی در قزاقستان است و برنامه جهانی آن تا پایان ۲۰۲۸ به حدود ۲ گیگاوات ظرفیت می‌رسد. بنابراین ارمنستان لزوماً تنها مرکز منطقه‌ای این شرکت نخواهد بود.
نتیجه‌گیری
با این حال، اهمیت پروژه را نباید دست‌کم گرفت. ارمنستان در حال حرکت از مدل سنتی «کشور کوچک با صنعت نرم‌افزار و استارتاپ» به سمت مدل جدید «کشور کوچک با زیرساخت محاسباتی استراتژیک» است.
اگر برنامه Firebird طبق نقشه راه پیش برود، ارمنستان می‌تواند در چند سال آینده به یکی از مهم‌ترین مراکز GPU Compute در اوراسیا تبدیل شود. نکته ژئوپلیتیکی مهم این است که این ظرفیت بر ستون‌های فناوری آمریکایی بنا شده است: NVIDIA برای تراشه، Dell برای زیرساخت، Firebird برای پلتفرم و سرمایه‌گذاری آمریکایی و مجوزهای صادراتی واشنگتن برای دسترسی به سخت‌افزار پیشرفته.
از این منظر، شاید عبارت دقیق‌تر این نباشد که «ارمنستان در حال تبدیل‌شدن به هاب هوش مصنوعی آمریکا است»، بلکه این است که ارمنستان در حال تبدیل‌شدن به یکی از شرکای زیرساختی آمریکا در جغرافیای جدید هوش مصنوعی است. و این تحول می‌تواند پیامدهایی فراتر از اقتصاد دیجیتال داشته باشد. همان‌طور که خطوط لوله نفت و گاز، بنادر، راه‌آهن و کریدورهای تجاری در قرن بیستم ابزارهای قدرت ژئوپلیتیکی بودند، در قرن بیست‌ویکم GPU، برق، دیتاسنتر و Compute نیز می‌توانند به بخشی از معماری قدرت جهانی تبدیل شوند.
اگر پروژه هرازدان به ظرفیت‌های اعلام‌شده برسد، ارمنستان دیگر صرفاً در حاشیه اقتصاد دیجیتال قفقاز نخواهد بود؛ بلکه می‌تواند به یکی از گره‌های محاسباتی شبکه AI تحت رهبری آمریکا در منطقه تبدیل شود—درست در نقطه‌ای میان روسیه، ایران، ترکیه و آسیای مرکزی.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20613" target="_blank">📅 00:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20612" target="_blank">📅 00:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5V_ldFc2_oEkH8fd8WMmqUIu443iArDQ9l8xbDyMWG4cpNwgwH7R006wpuIENYZyQFOAoaC0EfYeOBNompXz8hcXO2xd1ex8K9MiM8Ey74zDkb49t5pwZ4eVFt-E3mSa7GsJap5F84Xg7yiB15NqXSjWLrV5nS4lfwBYuGlB0Q8vQRHrSVbh-yUFClNEMxRacmuacg9SvWhuqwAni4JejbVioqzi22nv51qF6LMpFz70ncLvmDN9Lymxe_t3-tb8GrtSMIBMQ7E2vhpskXF4kMbc2u3UjJ12p6dL_c-EVaiYENvxCAX71tMM3mcjl3-8Sd2sJLpAqz9cIICe5ckiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!
ولی همین که نام Persian Gulf را می نویسد باز خوب است</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20611" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2jK4ZTVlfUCGXQAHVEJZYfMI6FLD1NIsvx36aHegYz0Pa__ogeEAhCUhIBM7xvftSgN2cwu4TOMD4eKULNxqfVU6sEtpNZFUHYURUCeUR6c_kdHeXc8p8KKetB17NuZ5xIfLS_QG85I0x18Fry_HdwkQT1h-uoRrrMb2OSVdg2WKVHfw0svsPheuzc4RqxuDwRDmnpKet7gHbehbhInChBlSpBUZ6JBGSmcQAIw6Sz_nAQvqH2deri-13f3GHMZ8Fw4cBQ_rAV3sqVwvA-DhR8UdgTmyOANQpCTQw0346XRN4enaLPfS-KdUA1h_C1osqCOSKccfON7RsqIkUwngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20610" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سرلشکر رضایی:
برای داشتن وحدت باید به رهبری نگاه کرد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20608" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8b4oan8eJtrNU3Z4T3JcqkBmaIr0E81lFz9oTBR2bScTfyBONJ11CT0-AfWnvlF2DM4UWoJQmtk5QZo12kT_Y-nysOpjvRZU1IBMoY3snG0u-dDJQmhlx8ifI3vsLdERz-SEBkblqXz_HVpeyjE9olfq7czIB1NuRX7eSRZmjlFVTOdGrl-NI_TdRiMc1hQde7-lVIX7mOM0bxJjLHgngYeeY1dTMpyIr9yLAQQG9Uub7OFshgwbM1kW4u9YPfClXIBNqOakxfYFVF90NHLOQlWyeXJxEMdxxf0NIqlZ6D32UskmmVRCCL_sYEipS5dqnLD3QJUoVmPmUL-2HZxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20607" target="_blank">📅 23:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHLV2gI-jh77imacH0-hobATm-uJhg3LXn0ez2pJQPeynYMlnZ_xd7_TIAVJM_0mqsoSLdHrvcWogCo4UCpDh3Jrccm5h5QkZDiUp1nMoIK58kmYe5R488okDj2QoDvICxWqwPhNsaHsELxNl3sMuXcfLAIRy2lWntYsj77A7lreCldsRKiO80CPfRR_CXMGA_rLfyfOo_Cfu6QVPK2MOKUqe1NEm2J9t_fhhjzSTRX3j4KLPZTajjNrXReD3oZ4y7c17tRuxph_rawQdIk32aHqufNcfDIhnhENKVOyATZWKi67loqSnEKQJpst11i4Br6a6ABsMhVmnzJK73Zqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه ما خیلی سلاح های دیگرمان را تست نکرده ایم   مثلا شاید طبق مورد ۷ بخواهیم کوههای البرز را ببریم تنگه هرمز تا این‌‌ تنگه برای همیشه بسته بشود و اسمش هم بگذاریم تنگه ترمز!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20606" target="_blank">📅 23:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سردار رضایی:   ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20605" target="_blank">📅 23:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سردار رضایی:
ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20604" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfqXJ4Q2bgVvHZ97UuOjSxZR7o6ib34jNh2EL_wP34ff8Cz3wX3waDSjwbDZBQwQByg3gdo6nsAYxSXkSwvScYC6X6INrxeHG6mcEPrEsJuefTOYiQ6pvSMDkDIyE-TI2SQmxS4G9VJeNnHhDHpa5eyJWPKI4_Mz445DBlB6FUNAiABKPabROljCd1QVHv-GWxB3todGUamcz154x3YyPck2YY_QCppJqDc4jqrP7_7s0BTrGKNZSi8cx2h8qw1i4bv8LzqrtMprgH7tg1LMES2Ura-qxfoZdvDY7GZuuEueNywRWrWbFD5lIC9thPXhsTDylL4qN-wwPEU8N-eKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20603" target="_blank">📅 22:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1dwaqiNMFWmjLy_6WWsuYPvUBrRi6DHxQtiJ4zkM57HkMQiw6GW1cgF9vnUNXXeN-GuNoIIFnmEAOLQ-blO9QnNXa5fmmTM5MrAEtqgNFGCnWWTEcDrK0pEE5_SCuNpdYKRrO7twwFHaOfYF-OGw7jbnDwjmP0Z14Lr-bU95aNb1GXPGuqlONuXfe9zmJtlWv0D54Z-G1o5u1_m_qapkeRBJx3KgZZoI6mPWbjxDSXBimNwfti--vfHxCM_vaocAgiiutpx6hIzPH9vi_1_zDozzhp8Od0QvD5S4lAiPMMeIjic9ReHmsh0LPrcVAVd3FHB9phJlFAczCcIGpI3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!
به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20602" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20601" target="_blank">📅 22:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=R16jJ5hrgQ-J6-dfTJVEbk6WF4hZ8H2to_WQL1WsTOIglEL_fZeFzFgPkSNKjYRGeXa8FbwYQKnUc-48QVTz5Yd7VQp8YXc3375Ey-jLVSn4Kjt5YbGT48i84089gR9FMW6bX9Wo18dC1bV8GGXdHW-SpreCKe00bRS3ojtrEGeLk13iIKFL4vbBrG33GJAX549xczSLGbgtbET8j41KUyMfaFiYk_9qM8mOihSvJqnajopTm90PhUX6TmIDoQynPlwD2en-jxgE7W80gQ5Vc6ooAnyTKbNWV32OkIuh-FwPYyt5OHAe-OafuC3wAyUoOackEP7Z2jXiVowI-QOGLW6PJgtClmTckedM8lAd46kGxmQtBTaV8hMWydTXehF7H8mMAOrCbv_azUnu-AdnRIveFqUIMomY-15b7HsnMXo4Y-R07KuwG7ZfNmAEL4A4mtEmozxtGEeFQ01mtOZ9h7pEUASznCNXEJVxc2Csjx75xz7RMmUIBdehXHaaMQ914TnpAjYXYG2tZdnKVrX3kK7yJyk6FSLGp_8zO5c4x9NWAe4hV_63MVvi6ilatGbsvoxrosV8XkOIwawN1Xbn2UtdBdp_MNnpGpYfrkuh2KENtaxZPVTjKkR2sVvUM0cc57RrvXW-5z4nynxX5h1mdu3b1PcXg1VRrwdf50Y6y7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=R16jJ5hrgQ-J6-dfTJVEbk6WF4hZ8H2to_WQL1WsTOIglEL_fZeFzFgPkSNKjYRGeXa8FbwYQKnUc-48QVTz5Yd7VQp8YXc3375Ey-jLVSn4Kjt5YbGT48i84089gR9FMW6bX9Wo18dC1bV8GGXdHW-SpreCKe00bRS3ojtrEGeLk13iIKFL4vbBrG33GJAX549xczSLGbgtbET8j41KUyMfaFiYk_9qM8mOihSvJqnajopTm90PhUX6TmIDoQynPlwD2en-jxgE7W80gQ5Vc6ooAnyTKbNWV32OkIuh-FwPYyt5OHAe-OafuC3wAyUoOackEP7Z2jXiVowI-QOGLW6PJgtClmTckedM8lAd46kGxmQtBTaV8hMWydTXehF7H8mMAOrCbv_azUnu-AdnRIveFqUIMomY-15b7HsnMXo4Y-R07KuwG7ZfNmAEL4A4mtEmozxtGEeFQ01mtOZ9h7pEUASznCNXEJVxc2Csjx75xz7RMmUIBdehXHaaMQ914TnpAjYXYG2tZdnKVrX3kK7yJyk6FSLGp_8zO5c4x9NWAe4hV_63MVvi6ilatGbsvoxrosV8XkOIwawN1Xbn2UtdBdp_MNnpGpYfrkuh2KENtaxZPVTjKkR2sVvUM0cc57RrvXW-5z4nynxX5h1mdu3b1PcXg1VRrwdf50Y6y7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20600" target="_blank">📅 22:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">محسن رضایی:  ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20599" target="_blank">📅 22:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محسن رضایی:
ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20598" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ: ایران از خط قرمز ما عبور کرد.
در یک حمله غافلگیرانه، آنها پنج موشک با سرعت ۸۵۰۰ مایل در ساعت به سمت نیروهای آمریکایی شلیک کردند که هیچ اصابتی نداشت و هر پنج موشک سرنگون شدند.
اوضاع درست می‌شود!
در همین حال، ما واقعاً به آنها ضربه خواهیم زد؛
اکنون نوبت ماست که حمله کنیم.</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/20597" target="_blank">📅 21:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNGV7Bs8zPswO3l81YZzoyCANbDQWFyihc11WdHSIN3ldrpq2Tp_eQbgYRL9XZ4r78_QESD_LBuhACW8t99c5_f6dStJTdTy2tdvt-AJDpnMOjxiey0sd9ETHqGt6Vgj1jjl3XRu0gc4G15nOWaN9DPbPS60o64SsYxz2MkmJi44kUvpVAgz6GUDzAziPhzrQ_Mih4i5K2bUWHbTl0luIu_Je_aO9pRTr7YayuDdyInmpRVLFnmeb6YLWE1V448rJMiIITtsQb3Mn-qeBv6wzsiAX1NiS5Cx-zrzEbqiaux_sBuYl1hhcAho6HBL0XcAG8M5mafh9JQvTky1i3tU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/20596" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SBoxxx/20595" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام:
نیروهای ما تا دیروز ۹۲ شناور تجاری تغییر مسیر داده، ۳ شناور از کار انداخته و ۲ شناور نیز توسط نیروهای آمریکایی مورد بازرسی و توقیف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20594" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
