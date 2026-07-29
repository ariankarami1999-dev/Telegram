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
<img src="https://cdn1.telesco.pe/file/OhC4DYwG0kE4iEnt-hQFT__A3jCAa1lNHSXTmMntQNEKg5sPXuQdy9u4gKe8OOfE6cVyIyYl7DPnA2sHwwy2sU1B23xLPkzzirZfNbD18UuIbUhY7CuJM7esnQneWD0E8AkHNxmnswHAL_Sb8RUj3qDXgU0trVcqSlUc_OW3dBPUQnH3OkoDNO-ockY9k5qYyLWGmkihaDKtb9xcTcKzjliENYw_H4xxTc-8DMOlL8aPmJr_qV70hwem2HWX1F790xt5Q8oANxbOn1fHn5ghlRFyMrSv97NG8qMkPcVJYnzu0P833-fpb8soDEu3DlgDbm76TWPtOnhbhiy0JJFtBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز: منابع می‌گویند ایران ظرف چند هفته سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد
‌
▪️
منابع می‌گویند قرارداد شامل ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی دوش‌پرتاب QW-12 و FN-16 است
▪️
منابع می‌گویند ارزش این معامله ۶۰ تا ۷۰ میلیون دلار است
▪️
چین این گزارش را بی‌اساس خوانده و پاکستان دخالت در انتقال‌ها را رد کرده است
ترجمه ماشین:
۲۹ ژوئیه (رویترز) — سه منبع آگاه از این معامله به رویترز گفتند ایران قرار است ظرف چند هفته نخستین محموله از مجموع حداکثر ۴۰۰ پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که هم‌زمان با بازسازی توان دفاعی این کشور در میانه جنگ با ایالات متحده صورت می‌گیرد.
این خرید که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد شده، یکی از بزرگ‌ترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است؛ جنگی که ضعف‌هایی را در توانایی ایران برای حفاظت از مراکز نظامی و زیرساخت‌های راهبردی آشکار کرد.
با خبرنامه Trading Day، تحولات بازارهای جهانی را بهتر درک کنید. از اینجا ثبت‌نام کنید.
به گفته منابع، این قرارداد خرید بین ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، شامل موشک‌های چینی QW-12 و FN-16 را در بر می‌گیرد.
این قرارداد با شرکت Zhongqing Baoshang International Investment، مستقر در هنگ‌کنگ، امضا شده است؛ شرکتی که به گفته منابع، به‌عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
ایران پس از ماه‌ها جنگ نیاز به تجدید تسلیحات دارد
منابع به‌دلیل حساسیت موضوع، به شرط ناشناس ماندن صحبت کردند. وزارت امور خارجه ایران بلافاصله به درخواست اظهارنظر پاسخ نداد.
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین همواره در جهت ترویج صلح و پایان دادن به درگیری نقش ایفا کرده است.»
گروه Zhong Qing Bao Shang مستقر در پکن، شرکت مادر Zhongqing Baoshang International Investment، تا روز سه‌شنبه به درخواست اظهارنظر ایمیلی پاسخی نداده بود.
ایران پس از ماه‌ها درگیری، که طی آن آمریکا و اسرائیل تأسیسات مرتبط با برنامه‌های موشکی، پهپادی و پدافند هوایی این کشور را هدف قرار داده‌اند و تهران نیز با شلیک انبوه موشک‌های بالستیک و پهپادها پاسخ داده، نیازمند تجدید تسلیحات است.
این درگیری دشواری دفاع از مراکز ثابت نظامی و راهبردی در برابر هواپیماهای پیشرفته و تسلیحات هدایت‌شونده دقیق را برجسته کرده است.
واشنگتن روز شنبه به‌طور ناگهانی بمباران‌های دو هفته‌ای خود را متوقف کرد، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت اگر مذاکرات برای پایان دادن به این درگیری پنج‌ماهه شکست بخورد، حملات از سر گرفته خواهد شد؛ درگیری‌ای که در ظاهر از ماه آوریل در وضعیت آتش‌بس قرار داشته است.
تحویل صدها سامانه پدافند هوایی دوش‌پرتاب، موجودی تسلیحات پدافند هوایی کوتاه‌برد ایران را به‌طور قابل‌توجهی افزایش خواهد داد و نشان می‌دهد روابط نظامی این کشور با چین در حال عمیق‌تر شدن است.
منابع هشدار دادند که هرچند توافق امضا شده است، برنامه زمانی تحویل، تعداد سامانه‌ها و دیگر جزئیات اجرایی همچنان ممکن است تغییر کند.
بر اساس طرحی که طرفین بر سر آن توافق کرده‌اند، تحویل‌ها در مرحله نخست از طریق هوایی و از ارومچی در غرب چین انجام خواهد شد و سپس با عبور از پاکستان به ایران خواهد رسید. منابع مشخص نکردند که انتقال از پاکستان به ایران هوایی خواهد بود یا زمینی.
روابط عمومی ارتش پاکستان، ISPR، اعلام کرد: «گمانه‌زنی‌ها درباره دخالت پاکستان در انتقال تسلیحات پدافند هوایی از چین به ایران کاملاً ساختگی و نادرست است.» سخنگوی وزارت امور خارجه پاکستان به درخواست‌ها برای اظهارنظر پاسخ نداد.
منابع می‌گویند چین و ایران مسیرهای زمینی برای تحویل را بررسی می‌کنند
کارشناسان نظامی می‌گویند با آنکه ایران طی دو دهه گذشته سرمایه‌گذاری گسترده‌ای در زمینه موشک‌ها، پهپادها و رادارها انجام داده است، سامانه‌های پدافند هوایی قابل‌حمل اهمیت دارند، زیرا می‌توان آن‌ها را به‌سرعت پراکنده کرد، با تیم‌های کوچک به کار گرفت و مرتباً جابه‌جا کرد؛ ویژگی‌هایی که آن‌ها را در مقایسه با آتشبارهای ثابت پدافند هوایی کمتر آسیب‌پذیر می‌کند.
یک منبع امنیتی اروپایی گفت مقام‌های کشورش از چند قرارداد در حال مذاکره درباره فروش احتمالی سامانه‌های پدافند هوایی دوش‌پرتاب سری QW به ایران، از جمله سامانه‌های QW-12، QW-18 و QW-19، اطلاع دارند.
یک منبع امنیتی دوم در خاورمیانه گفت ایران به‌دنبال خرید موشک‌های QW-12 و QW-18 بوده است، اما او از نهایی شدن قرارداد اطلاعی نداشته است.
‏QW-12 و FN-16 سامانه‌های موشکی زمین‌به‌هوای دوش‌پرتاب و هدایت‌شونده با فروسرخ هستند که برای درگیری با هواپیماهای در ارتفاع پایین، بالگردها و پهپادها طراحی شده‌اند. قابلیت تحرک آن‌ها امکان استقرار سریع در اطراف تأسیسات نظامی، زیرساخت‌های انرژی و دیگر مراکز حساس را فراهم می‌کند.
تحلیلگران دفاعی QW-12 را ضعیف‌تر از مدل‌های جدیدتر خانواده QW، از جمله QW-18 و QW-19، می‌دانند، اما می‌گویند این سامانه‌ها همچنان می‌توانند لایه‌ای مؤثر از حفاظت کوتاه‌برد در برابر پهپادها و اهدافی که در ارتفاع پایین پرواز می‌کنند فراهم کنند.
دو منبع اطلاعاتی غربی و یک مقام ایرانی گفتند تهران همچنین استفاده از مسیرهای زمینی را برای انتقال محرمانه‌تر تجهیزات نظامی و قطعات دومنظوره چینی و کاهش خطر ایجاد اختلال در انتقال بررسی کرده است.
این خرید نشان‌دهنده تداوم اتکای جمهوری اسلامی به ترکیبی از تولید داخلی تسلیحات و تأمین‌کنندگان خارجی، با وجود سال‌ها تحریم و محدودیت بر واردات مرتبط با امور دفاعی، است.
رویترز پیش‌تر به نقل از افراد آگاه از مذاکرات گزارش داده بود که ایران به امضای توافق جداگانه‌ای با چین برای خرید موشک‌های کروز ضدکشتی نزدیک شده است. رویترز نتوانست مشخص کند که آیا آن توافق نهایی شده است یا نه.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77606" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUdyX-IQuSqqBaDnujA16dDmbi8SDMh_btFToQtcD4XLBuKcDNS2Y9PbqXSh3nKAPNvZVDkwDeqZQbRBrNoFy3KWn8uPBTlAlefEjyQDHHmJ2vLeM98cOC0UyCdO-0okLdcJqVE-dxoCckJdac7OLgNqoBgWCRhrOV-2-dDh6MnbhyBJzkRY1XWSFU4GJiBGCF0wrsHaP4SZ3R5ev3KBnDLFIhpbgFzp8ryjZqzyRcxBmB8FAPHtfQ_iLsiNn-LBbFWDmfeMyoKO28RrHt3AxADU_-i8FrEloAh4Ow05yX1pgfTkVk9HZn5VheHr6tZPPln6yqgEAR6rQsMRH_7Ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی ایران هویت خلبان کشته شده مجید کاظمی رو پس از چند ماه اعلام کرد.
نوشتند یکی از ۴ خلبان دو جنگنده سوخو ۲۴ بوده که در حمله به نیروهای آمریکایی در پایگاه العدید قطر هواپیماشون مورد هدف قرار گرفت.
نوشتند تلاش‌ها برای تعیین وضعیت ۳ نفر دیگر همچنان در جریان است و مجید کاظمی هم با آزمایش‌های تخصصی و بررسی DNA هویتش تایید شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77605" target="_blank">📅 07:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZI0ZFtthl8GtGWf8JXhV-slZjNg2O9x21RK17oLxRHCHUA7kMzpSA65ed7HrVXkW6-ybscnbDtL5f3C7gAAlGe3plCME58t_J2PHytyFL8DWqrMTpFX8TKdnE_VWlI0m4Lw7T8SluMlR0ulE0IhWEFQoR3mkoKPtS6NYonh73NeZUnA-VOTHsTLYKp-M7kvUISr1Ev1bLdPsUrcwX3CDvjgTjaRi-rXfty4qDGlLeOI4UPYHx1hJwPZ5JIk9e7OIRkzq-GM0uV6s7eMfuvMz_Wmq-tVMaD2gUrMscuLMYc3JSKKhLBrdYzr741wwHt2CPp9VOx2apUINZNEA0xvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران، صبح چهارشنبه، با انتشار دو بیانیه از حمله موشکی به پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن و همچنین هدف قرار دادن سه نفت‌کش خبر داد.
نیروی هوافضای سپاه اعلام کرد پایگاه نیروهای آمریکایی در اردن را با چند موشک بالستیک هدف قرار داده و هم‌زمان نیروی دریایی سپاه نیز گفت: «سه نفت‌کش متخلف که به اخطارها بی‌توجه بودند مورد اصابت قرار گرفته و متوقف شدند.»
این درحالی است که پیش از این، فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار بیانیه‌ای اعلام کرد که تمام موشک‌های شلیک‌شده سپاه از ایران به طور کامل رهگیری و منهدم شده‌اند و هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77604" target="_blank">📅 05:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، می‌گوید دونالد ترامپ، رئیس‌جمهوری آمریکا، با اعطای مجوزهای لازم برای تولید موشک‌های سامانه پاتریوت به اوکراین موافقت کرده است.
آقای زلنسکی شامگاه سه‌شنبه در گفت‌وگو با شبکه فاکس‌نیوز گفت پس از دیدار با آقای ترامپ، با نمایندگان چند شرکت بزرگ تسلیحاتی آمریکا نیز گفت‌وگو کرده و امیدوار است زمینه تولید مشترک این موشک‌ها فراهم شود.
رئیس‌جمهوری اوکراین که روز سه‌شنبه در واشینگتن با دونالد ترامپ دیدار کرد، تأکید کرد مهم‌ترین نیاز نظامی کی‌یف همچنان سامانه‌ها و موشک‌های دفاع ضدبالستیک است.
هم‌زمان، سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرح گسترده‌ای را برای تشدید فشار اقتصادی بر روسیه و ایران به مرحله بعد فرستاد. این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، به رئیس‌جمهوری آمریکا اجازه می‌دهد بر بزرگ‌ترین خریداران نفت و گاز روسیه تعرفه‌هایی تا سقف ۲۰۰ درصد وضع کند و تحریم‌ها علیه نهادهای مالی، مقام‌ها، الیگارش‌ها و ناوگان موسوم به «سایه» روسیه را گسترش دهد.
این طرح هنوز باید در رأی‌گیری نهایی سنا تصویب شود و سپس برای بررسی به مجلس نمایندگان برود؛ مجلسی که تا پایان تعطیلات ماه اوت تشکیل جلسه نخواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77603" target="_blank">📅 05:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbqNApVMjfF0OJN9WCosC5P1olCM3z84agVw_Xqtru1NJu2WDJQZHDZ9z-CVwPJaIn6u-K7C63dUsmr4-rpmVsgDrMBtJ9YOE6NNALAFRtrXapAeNAK_9tla7GQbXZkFlRVej9vBJlM7JUf6MSioibR0NZmDJHtX47_vm4_nZ1qjJo7YtGV2mtSX4gW9ZeQstWmMSHXWLBcpsTreVzeBXnO9-IxFO9OrJPOTOZxanPHX-y_ezK7dQyN1QRQ8fGQODEO8VjunSh_VC7MlM8Zf4CJZHVHABnrVCAf_XvO-XZ88IqnMqfPkotkGSGTcKWrcKmPPX9m93jDkUrHW67MVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، با انتشار تصاویری در «تروث سوشال» از دیدارهای جداگانه خود با رهبران اسرائیل و اوکراین، درباره دیدار با بنیامین نتانیاهو نوشت:
«نخست‌وزیر بی‌بی نتانیاهو از اسرائیل، همراه با من و نمایندگان، نشست بسیار خوبی داشتیم. بدیهی است که موضوعات مهم متعددی مورد بحث قرار گرفت.»
ترامپ همچنین با ابراز خرسندی از دیدار با ولودیمیر زلنسکی افزود: «دیدار با زلنسکی از اوکراین افتخار بزرگی بود. موارد زیادی بررسی شد و این نشست بسیار خوب پیش رفت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77602" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjUtbngdEC9A_NFtx5Va7dGI8H7r4vnWRKOGdVm11x1WzdpHj4M2oGSlwcpsYk-k-s3qnsD1WGiPnp7mkUrKZzjj_y7Wbp2ezp0deo-T_COjuK5e3wn9p2VPIfUuJoq4-B7STmjJ2gDkON0EbDuvcpNWOLaZC7beS6fjlGYdfhEt6C7xHlZHj4cGatXN7NCzGDr_yH6HM73X8d0ODnH96XDOqxwYjpEfIG8TJCijundOlykKxHBB8gzJzFR1Y-dNF3DNYMNmEE0g8B667_OyIYhfntyq03iVnMVc7gkW-7HsFzazYjStZvBeAdmlKaToXt2o4IEhu4-WGrbVxn3W9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست شده در اکانت سنتکام
متن پست، ترجمه ماشین:
نیروهای آمریکا و عربستان مواضع تروریستی مورد حمایت ایران در عراق را هدف قرار دادند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده و نیروهای مسلح عربستان سعودی روز ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند؛ عناصری که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان هدایت کرده بود.
جنگنده‌های آمریکایی و سعودی در پاسخی قاطع به بیش از ۳۰ حمله پهپادی هوایی که طی ۷۲ ساعت گذشته به دستور سپاه پاسداران انجام شده بود، چندین مرکز لجستیکی و انبار تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
حملات ناموجه علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، شبه‌نظامیان تروریست همسو با ایران در عراق بیش از ۶۰۰ بار تلاش کردند به شهروندان و تأسیسات آمریکایی حمله کنند.
سپاه پاسداران و نیروهای نیابتی تروریستی آن باید برای جلوگیری از واکنش نظامی بیشتر ایالات متحده، این حملات را متوقف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77601" target="_blank">📅 04:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfxtDZt0O3TTVEDlGMazw22EDdpcnOhCM6LvxykLmrAQCt47EYR1CswfWaeivrHoiiK8okdhEyOycATubzn7WAQx8EhFi4SWzWuwRPL6kfGlSseXbuu9x_deRatSvibqV9o17SCx228uexKzhrV_FCqnftL3PL97Olyweme85mmKOSb5CYsY5oXNUA02w6P8X1Oqdk-9xgWKEm5pqArHqtaKNZFEIsuQAEZAdBKGXV4d6_822xCLKJvFOPL_yHuMt55yOr19QuUF9wi7jcmja4RyIMrOpRmzgwF1hHN4GJBacv1rgmBxXM3s1Pa26IQpmcUJL7ThFDWxNxTAtSSmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور چند پهپاد را که تأسیسات نفتی در استان شرقیهٔ این کشور را هدف گرفته بودند، رهگیری و منهدم کرده است.
ترکی المالکی، سخنگوی وزارت دفاع عربستان، روز سه‌شنبه در شبکه اجتماعی ایکس گفت این پهپادها از خاک عراق و به دست گروه‌هایی که او «شبه‌نظامیان تروریستی مورد حمایت ایران» خواند، پرتاب شده بودند.
او افزود عربستان سعودی حق مشروع دفاع از خود و تأسیسات حیاتی‌اش را محفوظ می‌داند و «در زمان و مکان مناسب» به این حملات پاسخ خواهد داد.
@
VahidHeadline
خبرگزاری صدا و سیما می‌گوید که یک »مقام آگاه نظامی» در ایران، در واکنش به اظهارات وزیر دفاع عربستان سعودی، هرگونه ارتباط جمهوری اسلامی با پرتابه‌های شلیک‌شده از خاک دیگر کشورها به سوی اهدافی در عربستان را «قویاً» تکذیب کرده است.
این مقام که نام او اعلام نشده است، به این خبرگزاری گفت نسبت دادن هرگونه اقدام علیه منافع آمریکا در منطقه به جمهوری اسلامی ایران، «خطای بزرگ محاسباتی» و ناشی از «کم‌اطلاعی از اوضاع منطقه» است.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77600" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/alYgGVhBIsxPno2Sm6dL3E9xYWr5YEF9ZRFExaukTHfdXKmkpu2b3XA3gw6jwA-kXViLiJgEAaNb5jEqztP_M9_87KvmXMgaglKX4-y_e_xpfhIpDhcqnJ4djW7663w2Tya3VCGQersn9iaobnM_e2hPxTwP08z6D-zbMdJGbsRl-90_V9uBmtvzNAZXqwCyDT4fkV36MsNxiQAZxazWriWRTUnbRLa2xtOPYHJ0sn1NKdIEIM6NOJ6VZc7zLAbUbWl9WHHUa-vUuX5wd8mpCIkDa_xIv0Hrtk4Nx55F7_nhTtHsHNey64AhpOhb8JJ36jVbd5MffJylQsMNgLPTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرق آمریکا [۱:۱۵ چهارشنبه به وقت تهران]، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از ایران، در تلاشی برای انجام حمله‌ای غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند.
همه موشک‌های ایران با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنان هوشیار و در بالاترین سطح آمادگی قرار دارند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77599" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eQuqu7tvzuXnDkiT-vUnlZyio1UmBCWFKG9U9O6T_2odLDJ18HI8Qugu1J8bjp54iL2xMI2ss6pJyJ-C3rNwvQpSANHfoN8bNd26QRZgwQH9CYnsYhPtyHqiyPc54_hw8cT5_Ag41GlUn4ckace4guxUrPjvAZVK-F90fMMQfw2f157vemlbtob61zLix19wUBOIBCBWGYkEdpZt0uyqV3wac-9S1EE3ZIZkdc9KueNUXdXv3wGT1HMofNO-RWZwNhcZWLTjWQGsjlRTugCQMq_eIqeXqfnXntB4O-hFI7F2MiJBrX8oBFrcpfnueMeivtkMQtTKNBGGQMtaKqPTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NR6e0fWMSF_X7ejrFhFkZA2lCY43837sOIDv2lh8Z5d6Esb6--mrePiqHcNvnqDyvUjqkECfIPPz7uGWVHuSXJVN7oXWgbmFuoJQLcGC76dFAuX0_MPeusFtHdtrbTdVkRwwrVORDXQl5gJH1neJzSUKY3mhhS6cHYElmj5w0JSJaQtmHQ0Ckf1mbPAVR27WsBxJdSAUUYh_5uStGmw4fLaBHOa82in1mCojFNQ0NVSRspeGRKsojg4J7-6AHXTTeycFxeTasG-EE0pEhGwux5a0BRvgY1o0BlbY6QlS764AoJY3wh6ZbI8AuZy454usD-2cDYDfoMijn05hgfHEPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=MrHZidcklreG0X1c6uj-kBCfTLTuQV5kK9eG6hLNolE73Y2jilUASSH3uNaSY5-_zJHZB9bQ6X6SUStAMuDgjU0wHYqcu4VbCcsIg5LsAkSZDlFpFbvM05PJ_qz2Rl76h6iX6b4fxwNEf6aLYIpEOz2WeHgP8uaK_zHp75-nq7iTa3UncEiZGC2jVVM1rpzbTzorTZZhwbOTmAgoe7l95mkw33UxZVCjmQhcEfMFFj8JqFeXRqnyblDovfdOquqSbPiO0SzHWqYepVWk4aIzTJuKaEwcbMNoa7AIbdZhrhbcujd6ImWHgQ2gDGqd92-AcaiaJWlc2TjcfcCCszeUdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=MrHZidcklreG0X1c6uj-kBCfTLTuQV5kK9eG6hLNolE73Y2jilUASSH3uNaSY5-_zJHZB9bQ6X6SUStAMuDgjU0wHYqcu4VbCcsIg5LsAkSZDlFpFbvM05PJ_qz2Rl76h6iX6b4fxwNEf6aLYIpEOz2WeHgP8uaK_zHp75-nq7iTa3UncEiZGC2jVVM1rpzbTzorTZZhwbOTmAgoe7l95mkw33UxZVCjmQhcEfMFFj8JqFeXRqnyblDovfdOquqSbPiO0SzHWqYepVWk4aIzTJuKaEwcbMNoa7AIbdZhrhbcujd6ImWHgQ2gDGqd92-AcaiaJWlc2TjcfcCCszeUdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'پرتاب شدن چند موشک از
#خمین
'
تصاویر دریافتی از شهروندان با شرح بالا
چهارشنبه ۷ مرداد حدود ساعت ۱:۱۰ بامداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77595" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwIt1A9526N3MTmSXfsrR3m8PK1JcTUABGnE7lT8xvA9HMGSz_ojqlUbZdf-uqFP662sP050wGjD7rUViTXXldWSyxEKOEBaKvp4BIR0iQTn3phfhGU8NYIebvc9f-K96_BG-0AOs3VkP5u4rW_hOfmNImUJfyt3rcsqFh1FSDWTZiNZxN-5VmacNe8F7EhpK2R9Exww8wYkgP-TgL9OBQDshcLdWXDBd31GPPEU6dVZtRB2zagTr0wgwLqNgf_nuHhIK6TmDwTrc1V2trCmvheUUWQxFVOVN8dRd1q-YW120qX9iu_rNGRB2dk5D_lJzTKEOFN7_fGeDaiEy2bcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
از خمین موشک بلند شد
سه تا صدای انفجار
همین الان از خمین ۶تا موشک زدن
۳تاشون صدا نداشت فقط نور قرمز بود
سلام همین الان یک موشک از خمین رفت.
داداش
خمین موشک زد
ساعت ۱ و ده دقیقه
وحید داداش ۴ تا موشک از خمین زدن همین الان
از خمین موشک زدن
سلام،الیگودرزم،،صدا ۳ شلیک موشک اومد صدا دور بود احتمالا ازخمین بود
پرتاب سه موشک خمین
سلام وحید جان
سه تا موشک تو آسمون لرستان از سمت اراک دیده شد
صدای انفجار تو آسمون لرستان میاد
من ستا موشک بین نهاوند و بروجرد دیدم خمین نبود فک کنم نتکنستم عکس بگیرم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77594" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=OXTMFmc80-GagjtoahTJ5UvlULu6WQ33RP7fTIqCYJPCCfiI2AKGMM363slHZP6CfaBFC3VIjSMdUt9R1Ca5SFNBpBx9sP2iMM8oyixYysHsL6LeLaKWg1lIa0r7DN7MT0AMUqUgo9q5RxC0vorNZYvdTopiO-i88CXJb8LdskmrGxIQg1uPoQtwZ50r9VwYoRhVHm_89bpR3l3Zz-CIb7KBEjIozK7O9buvqH8Ghfd0F2qdBmMEBQGHNUesoLDN3l5IWiuFDOJcnUz2ugCWc_Ml5h2KeQZHEf7iMoMUdyKWUcFmlJt-agZTt_w_pMC8K3GSDsLiNa1a_DpUUXBO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=OXTMFmc80-GagjtoahTJ5UvlULu6WQ33RP7fTIqCYJPCCfiI2AKGMM363slHZP6CfaBFC3VIjSMdUt9R1Ca5SFNBpBx9sP2iMM8oyixYysHsL6LeLaKWg1lIa0r7DN7MT0AMUqUgo9q5RxC0vorNZYvdTopiO-i88CXJb8LdskmrGxIQg1uPoQtwZ50r9VwYoRhVHm_89bpR3l3Zz-CIb7KBEjIozK7O9buvqH8Ghfd0F2qdBmMEBQGHNUesoLDN3l5IWiuFDOJcnUz2ugCWc_Ml5h2KeQZHEf7iMoMUdyKWUcFmlJt-agZTt_w_pMC8K3GSDsLiNa1a_DpUUXBO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ادای احترام به لیندزی گراهام، سناتور جمهوری‌خواه که ۱۱ ژوئیه در ۷۱ سالگی درگذشت، در ساختمان کنگره آمریکا
به غیر از نزدیکان آقای گراهام، صدها نفر از قانو‌نگذاران آمریکایی در مراسم حضور داشتند.
برخی از رهبران جهان هم برای شرکت در این مراسم به پایتخت آمریکا سفر کرده‌اند.
سناتور گراهام از ایالت کارولینای جنوبی بود که چهار بار به عضویت سنای آمریکا انتخاب شده بود. او در سال‌های ابتدایی فعالیت سیاسی خود از منتقدان سرسخت دونالد ترامپ، رئیس‌جمهور آمریکا، به شمار می‌رفت اما بعدها به یکی از متحدان وفادار او در کنگره بدل شد.
او از چهره‌های شناخته‌شده جریان محافظه‌کار و از مخالفان سرسخت جمهوری اسلامی ایران بود و زمستان گذشته در جمع مخالفان حکومت ایران در آلمان حاضر شده و سخنرانی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77589" target="_blank">📅 00:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdypodmENWeJuBgGTcSt0qGVWTGyQJG5qbQgavngyzTxYCASQIJYWktPKGleyXrcqkltZhdZ4wks6H56tiJFt0jpV5HdieLG_bYjt1pIxl5zxk4tfG7j_o5zM9dmHc6lMLaRciVouWte8pBlf7zm5u3fbvUpkOJFN6KQXm3McU2FDwXy63xG6aUmRp02zSA_NZNE2WZD4t4KfSXSjKsRP8rBQhitCooQgeT9T-S6hkfbvX1F2kUIuqCJhaNlNBrv1ipn496MKY5MrJveRdVM6GcyVVSDZ_jeq7LDgI_KHdD27Qm6o5Qf6ZDmDE7-ZH5-6tGQ2LWbqFj6wB78RyYuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
این حکم با اتهام «محاربه از طریق مشارکت در تخریب اموال عمومی، تبلیغ علیه نظام و اجتماع و تبانی» صادر شده است.
به گفته منبع این گزارش، مهنام نواب صفوی دو وکیل داشته، اما وکلای او به پرونده دسترسی نداشتند و امکان دفاع از او برایشان فراهم نشده است.
همچنین دادگاه او به صورت غیرحضوری برگزار شده است.
مهنام نواب صفوی در جریان اعتراضات دی‌ماه در اصفهان بازداشت شد و اکنون در زندان دستگرد این شهر  است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77588" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ABvj0OMyCphUzOB7nz8ax-bwXxPViqEocU5-4hZbaH9k6wLHuBB8_9iqeTbtesjgodc9BqYZkSsC0HyFz4Q8yYXkKT7qss9IDJ-URN8U_XDvIxTl0nTDLC3R6lt9_e8ZBGcBhxrKctoF0Z9aN62KqLYU41lvAomYtv93I5-fY7KqfFK454Had6XnZ1l-Ey9XSKw4cVzQCLUUkxWIC0Wj33B_a1CdRuDsxC60NOL78a949f_WP24LBcBT1gh-CdEJs0E8yVzD9fS38_kuwyMltEnnWwyIO5Fi_cSFvirhnFd1zhAtfRMjdGNAWJlAE77_upezQoYSBgqyydZ_qi7gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:  برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.  بار دیگر تأکید کردم که تمام اقدامات…</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77587" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=Ve2gPbdwbcOpyLftOB1tCHB9mhCPRixaxnpsqLJr4HJpl0wJBdOpZi9lQjQWTlJHXpDrdqivvj16zW1dTxcwuQ1r-AtC0SHBA2-je0Af_dAOUXSDDgK8ipCD5HD1QxCz-5NTb-UuGFStg1N-DvqsWPu0zuLKeHP8eymGZULfq9UNpmAKBZe6QpRiXEjkLXfEpS_VuAxpu6PWA6jES7QSNIarNgYJdZjGbFGtEf-UknNWWFLzVAMKL70w1VOxGr8bpfkMvOVsYrgMMj4eynXmRjxf2TXcCmOoYbOKmT3W2ZAkl7mkZHVTTFceinncyv9Eqcbx2NKchxeY4z7jEojewg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=Ve2gPbdwbcOpyLftOB1tCHB9mhCPRixaxnpsqLJr4HJpl0wJBdOpZi9lQjQWTlJHXpDrdqivvj16zW1dTxcwuQ1r-AtC0SHBA2-je0Af_dAOUXSDDgK8ipCD5HD1QxCz-5NTb-UuGFStg1N-DvqsWPu0zuLKeHP8eymGZULfq9UNpmAKBZe6QpRiXEjkLXfEpS_VuAxpu6PWA6jES7QSNIarNgYJdZjGbFGtEf-UknNWWFLzVAMKL70w1VOxGr8bpfkMvOVsYrgMMj4eynXmRjxf2TXcCmOoYbOKmT3W2ZAkl7mkZHVTTFceinncyv9Eqcbx2NKchxeY4z7jEojewg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، روز سه‌شنبه اعلام کرد تهران پیشنهاد عمان برای تقسیم برابر مسیرهای عبور و مرور در تنگه هرمز را نپذیرفته و در مقابل، طرحی موقت برای بازگشایی این آبراه به مسقط ارایه کرده است.
غریب‌آبادی در گفت‌وگو با تلویزیون حکومتی ایران گفت عمان پیشنهاد داده بود مسیر کشتیرانی به گونه‌ای طراحی شود که ۵۰ درصد آن در اختیار ایران و ۵۰ درصد دیگر در اختیار عمان باشد، اما جمهوری اسلامی این طرح را ناکافی دانسته است.
او گفت: «ما گفتیم این موضوع رفع‌کننده نگرانی‌های ایران نیست.»
به گفته معاون وزیر خارجه، تهران در مقابل، طرحی موقت پیشنهاد کرده که بر اساس آن تردد کشتی‌ها در یک مسیر از آب‌های سرزمینی ایران انجام شود و بخشی از مسیر رفت و برگشت نیز در آب‌های ایران قرار گیرد.
غریب‌آبادی همچنین تاکید کرد سیاست جمهوری اسلامی این است که تنگه هرمز «هیچ‌گاه به وضعیت پیش از جنگ بازنگردد» و هشدار داد هر ناو اروپایی که به گفته او به تنگه هرمز نزدیک شود، «هدف مشروع» جمهوری اسلامی خواهد بود.
او افزود عمان همچنین پیشنهاد کرده بود کشوری برای مین‌زدایی از بخش جنوبی تنگه هرمز اعزام شود، اما تهران با این درخواست نیز مخالفت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77586" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=UkqVKTamb26UJWomI3bCMHPJqxiWuOACBT6nsihH9tDUyUUtTdpGh1aH9hLnFIVbyKNMbFWJkr-8bWyurTWk-QhEViXODv1-pFQ9XJFVTju5f2R7nKPzRjWCsS4XahARnoUOEFkNw0Dcykwj4qv91BXf-QnLplTfkZfALtIIbFDv31YglE5FLyspWeEPKYeHGYjWN7Gao64-S_DQVQuIdRIBtSfex1dblVw8EHF1_swZaolfT2-Yh6EKVCT4IrNmccS9bIKsetetq7K_bdkHIGUMTeHMmJhGuJFSSVSnOjxCY7hXwnLa1FfG2cgE07r_Jw_p71DjiqAJ70Rv9RBcCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=UkqVKTamb26UJWomI3bCMHPJqxiWuOACBT6nsihH9tDUyUUtTdpGh1aH9hLnFIVbyKNMbFWJkr-8bWyurTWk-QhEViXODv1-pFQ9XJFVTju5f2R7nKPzRjWCsS4XahARnoUOEFkNw0Dcykwj4qv91BXf-QnLplTfkZfALtIIbFDv31YglE5FLyspWeEPKYeHGYjWN7Gao64-S_DQVQuIdRIBtSfex1dblVw8EHF1_swZaolfT2-Yh6EKVCT4IrNmccS9bIKsetetq7K_bdkHIGUMTeHMmJhGuJFSSVSnOjxCY7hXwnLa1FfG2cgE07r_Jw_p71DjiqAJ70Rv9RBcCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی که در حساب اینستاگرام خود منتشر کرد، دیدار روز سه‌شنبه ششم مرداد خود با دونالد ترامپ را «عالی» توصیف کرد.
او افزود: «این گفتگویی بر پایه مشارکت کامل، حمایت متقابل و درک هدف مشترک جهت اطمینان از دست نیافتن ایران به سلاح هسته‌ای و همچنین سایر اهداف بود. این یکی از بهترین گفتگوهایی بود که با رئیس‌جمهور ایالات متحده، دوستمان دونالد ترامپ، داشتم.»
نخست‌وزیر اسرائیل در حدود ۹۰ دقیقه در کاخ سفید با ترامپ به رایزنی پرداخت؛ دیداری که پشت درهای بسته و بدون حضور خبرنگاران برگزار شد. نتانیاهو تاکید کرد که «تمام تیم ارشد» ترامپ و همچنین «تیم ارشد ما» در این جلسه حضور داشتند و این دیدار «فرصتی برای تبادل نظر و هماهنگی ترتیبات مهم برای امنیت و آینده دولت اسرائیل» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77585" target="_blank">📅 22:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/czcM7G6T72tHwQP-9abkaB_nZh_okNcCByM2qH-pT2Myv7qxKdWvqfrRCcgXjDHhAtUYiE27lTHXxgIi-uFiyzmgH5vhFiDYWJKJIwNd3FLf-oh6iVUmFwiyOnLLti1RA4p3VqoKf1J1tzFLdZ-ezVereRioA0nFjdBUNNF44eymLz09ZvNFTdYh7LaL0A-nM0JTkMKxryB2_fsQNFvf08aE-QZhOazAvCWTSGLtXt36UBVrCbzeRytA76DQML_i5cd1Ma4nHTMWhZCYiUuvr6UjQZMssRCol5AAf426uG3EGeO4N0t1xl6QSIkTJylsKWcC0qiYhBQXHWnxfAI74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:
برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.
بار دیگر تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن شناورها یا افراد غیرنظامی را نداشته است.
این موضوع درباره اظهارات ایران در مورد تبعه این کشور که جان باخته و نیز یک شناور غیرنظامی که در حادثه‌ای اخیر هدف قرار گرفته است نیز صدق می‌کند. هدف ما مقابله با تجاوز روسیه است که ریشه اصلی همه این حوادث است؛ و این روسیه است که مسئولیت کامل همه تحریک‌ها و تلفات را بر عهده دارد.
بر ضرورت خودداری از هرگونه اقدام تنش‌زا و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین تأکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77584" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F1YIMhPqed7p-T8qp4aM7J6_u2sovcObn17iWrZVKgl2Bg-KofF5serxzaBHck2Yg2iRcz3tY3WXKb-ijb1jhJuCpkUWbLVEQ-LsiZxvq3_LFTd2GWkx-tEUEMBKD2G52fAxudyamYFhgLGXXS5mCqe5nKPFix1M5dVbkPvTknUOv3NPdL1blY3yCNqL27Lzy4ghp5jxQxcqEfsSGBX44xz6dvXYeRgMG5g2hufNESpNls8uSjmCSrQIM9JxbP0uEzivEO3TmlgMWMz20P3yrAiSomE4nDlinPTu_xVHDLbveEih-x2ZrZHojuxS7-hs8xBN-h0UMINuNI10pD5A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c6Uc5vO3pQsN4H-smcPHzwkzC65geZjsiYdVHVH-istrnerv4YXrmiRDXRCxMehQI-3-0icbZEx8f4AZfS2Tv375V6rtv5eSaJOmdJtsmGYzvdV-YSQ1-uUlc1-_ha-WyJDFZj8PmSrU7i5xqQe9hoTIHhT19Np0xOxNMSwlTxSB2O6AeQ8CqvXc3jileKf1WfIkhR_W_k0RLMls_XR4cIysSmuWvRy-z9SAgUU3CLdNOtqkkjO0DwqzZRt1e_NQZMF4KMaVbLoZy-PEweUZfPQIebJVtQtVwq3X6QVa4P_9_9i8S1KhXKEMdMgNdsTAQKl6pfNOCUIsNaTc90wpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YJqHkUzQSTOH0tUAMpAwAIT1p1Pk6bDzypeyQWJgMa5ItCiZJGSAW2H6dHyw6kRqUT5PQ3_FMM_2iAWpkvDfWaUj8jJdLb8id18k0mWpFQVIXjddOEkie8lIaX1QQLeR94pKbYIDpTn3xjoN7pGMQB8l5NkcSfcHPJjpx4l8iKedna9K0MAACo9S0sAFDPO5HdjrJptypGfnLZlcc9Y4zhJjbVqsDSTx9-KL4z4TghFhz5PvGEkT4Gj-awAcTy7PmizgulRIYCrKoCHfD-_Zevo-_JD8VvsmqJa0_bCMQPCo1_s_qOG5oLsi4b3wg8xFW0ZVvB1Qi7C7Z_ziA2a9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v63m4XkEFF8qm7ONpY0tswzFUtC04evZ_-wIofad-lJdB3XtE_R35o4B0mSyN7AUNqqD5TL7igUIAd9mrXWjiohMCXFLkHnRCccinQxUSJ064GleipDth9oyj0iTJzQhyJCeXdq8vvlbDwETC6oZMt_zkyNXlSngvvXE8Q-drLmEPl5tup2ZAJPw32dIkgz2dMs8R_YsobaM9dqF0n2bPMIpCOoAlUscJCaGVO8BhZuWq7Pz-oKavkE-jJD0mo6CZ7VL1fwkK0X4RyOXi7w5Du3ZkwNHpdy8O6Zrj_G5pZoqikdxhacLAFBlHTYmN9Nv1d4lgq8UnKIaEUe9NOANDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fTJXBM4n5R0CiRG8oMN3FR65wXhRj58W50Pj3zYXayvymR3zNZT1iCDTtbWDU2rSucPdmTIPJwEe7lGpUi4jnsdPVH4PeLTlDxBgj8wMCcwBnWX7iUIB_WwQgcGfYn6jW33zqWIiL9QL1yqtQikRS5xnG7j71pQLTDLsbXFRA9wgqL1QzYAtBFqDTi-E5D-I8nmCcSivvVuU0RlrJ8KAg-kCva9NE8lciLTdvLvz4lDL5QdWfT-gzkv0TCUxggAXIxlyo-_X-xT7BF6n1OSOZW0Ip9lENEgVUIDxhQ82byUmZWWuUaJ1esBZU_R8b5L2ED1p3Bjv4eigIUuDO91uBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lcNPzyrDIffzI23I2E1wJo1zZbFxu64w7KKqm2gfHLz1oaE_fI8kfOFP00uXym3BYhMqBNHIf-OCGgm_YB_wBSHWMkaGVgfqKKQGzNIcDfH-_1HqOCtQ3b8-CHl4iOE4DPAXyIrekzE1DKBoG0lXh3-e6f3kR7g--pPgdE8185iZlK-H4C4lDREW57zKdN4H0to49og4Evk43ZnDC4xl7G0a0w2Bejs_jNC0EgXgjjHkwAzO0RuBeq6n0hWAzvslvITbo29dnvGbxVlsWVLUSWVxU9rn2s6DZnXVwLRyylYdPi8CGLAnZo_UkiWmhNhBbvxIjq8VPDeADE65knjtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bPKS5bjtHYj_EBtP8QowgTHDkh-ZFTdH85bdjuX4c-PXYjB9ybovGi4hxOAnzxsl-6HK4RS7x3WTkAQFIpTj7OVuqdG3y67u7hzLGZexAAiQ20fRrmFRMcPer7U3Gj--zfen6u-BSIcp1Kj0DlXnKfrC1_i_RSJOesLCSdBSRJA6eOVrCwgwVtjuEaTXr0jZ7RhpGOvg9fzmzS0EI2jg2BIUN9L_vBJUDR1ZZEvOGCVUOKBDP-mLu9l3iwQCuiN_uco8BYdNkvxJ42HzZNnfcBbw-odiBHCKJ_iJfONg2hFdwu47UyE7eWspkaQdoZk3gsr3RXrDjiwR2_OuVTitoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/drPaJWMXd7ShZVRvK_mF6IUwI8oKB-jX5yluXf7cYXB9V0c4TqIGSrefS05kHhWj5h9sGNLdgnjCVIA168evfsdOmhCKlzl9ukkS_p9BGZVw3VF9q1JF6o25PeCbIt414X3uRRl5I9m1Eq-HJKDcSDIHaCQcSftCvGO3YlOuw3D8EwS30xJdxs93yQExO74ZUXGplPaPiclaVW0J-rInYNTFbwGbOFbgSM6R95Hg0OH1I-girohFQYfFD2BPzvrrXY8dY5ObhP_j7JPhUBSfprEFuJbKo7OCKc5j1Nn5H7iRk6-FBcytPBNR1DuWEBovtw2_Anp1RmWpzX5a9UpHvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل روز سه‌شنبه ششم مردادماه برای هفتمین بار با دونالد ترامپ در آمریکا دیدار کرد.
این دیدار در کاخ سفید و پشت درهای بسته انجام شد.
دقایقی پیش از نتانیاهو نیز، ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، مهمان ترامپ بود.کارولین لویت، سخنگوی کاخ سفید هر دو دیدار را «مثبت و سازنده» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77576" target="_blank">📅 20:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RMnAVc1emMfqHl5JBKAg-NC2Wpf6moc3tYYJz9LVFeTPI8AAJl1__F2RKumopTNYIr_kBLiTQMjccGGwMsgTfAbmihQzHlTJw1YtJ5c7EmEt-cLmoIEQtnpk5v49Gh_ndJB8AdiSpdOd83sdyfI5KmGQoMOSxTzLfZ_DVJnrmSnxVAujW7cj2ceibebMjNmjVSFH8Z0b5MmQJfs5oaYEtdVwLoy7iqBUMBHC1M9oqWwNeCuOe-d-nDOVfaYmf9BpoGMgos2XqbmcsKH6-ySrQsy_6RlqVJzDnnPtYbu3BMH5gPDweu70vXFSKH9LJ51kukE14sbZ1EjZUSeAvOAUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gnyG776ndYoEnOaMHmHleEL44yFk64IAjZRzBBNBzFQBaw7qwn1F7Qg6WsvW8QQFYCoEXjvHUC7KG5TlKlfQSQSPmsDLiI6r7bnncQG9q5D_npUH8meAC14-2NddAwkjHYHwvVyHiSQxwr57KvJi27i6jvVOpxwZvTf7WX_Kkv3J_9bpS5o3ukDnjPjLgYaJ9f8-Ph39nQPiIX6YxI-SWWD_b2V7mYLLX73cXATUi6EbDztxsb8S-7BMvUcoLYfIGZornZOtR02aiOgT24HTMlhk-K19cWOpr2oR5LYTxPoFnRLrl1SCRK2Ho8eXh1ync4uRaO3FW-es2a51bm5cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StvnQB8egFzBFC5alEb--I34_fXup0ie1OukkfjNuTYGC4oqNfnGhYVOsg5s8lL7Qcb_cMlHkHkWrzWfn5Sz_1IgnifcbR1sVqwRZGRAo5f8whSUzhyqKcm422-t1kDiwmWCMNA9bN45MY4x_J093-sji_fpAXr2q7r1rn7GYst8eaa--gulDl5pyOt5QhdZUKBCdpxUZO2gux7OlmXuUdGfsd9p4RROzzz1gYFKlPJp_pz0qAc8XE6rz3JbFthpxXfirNN74VldM6Gde3XER94-EVAFq7IJ4h2LUMB6T2RcTHrUHrQNOea9CbgABpuuN2KKzm-t0SptQHuiYCi_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eZ-P1mDStfZr6fEqGsA_jLC0LaNLrjjYZ4mqx53h4bV0jTvRTV7tOf5LnOhNzR8jV63wi48sbsl1YrCiqawFm8dHkUXWgMCX1tyTDbDgp9nnynOeH4ZsK4NmrKCE6OBEoPjk1cgKzy_0xQDB8pwCC4K2o77G-OnLHNrb4cMzvTLs4eqWyEmOUTZl_drQ5Pz7KkRACq0yjIC8tCJSr_pGUPDqdxo_2EGHkulAMIQ3K56s_FG3044GAztd-M44N71INHrVeo-dl6z-I5Ckqn4gKn0Wt_NBjXW6v2flu6Mq4XhBtNStYGPoW1Vkqy3it24CDBt4DQSGNUwANjiqJCuT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B5R4_1CYQWPnDavqD1cIhdK7rN5MHa-x_E9pWX1eCCyt9MQkciBZZSP8ZAXYxcHBWA65cyMcdjB5soA8YeaGw558v9jhJgogA9AKhgOEM1mNNkYt57s4FrftXmAIBxxwDE32WyRUTP_xdz3ka1YbPXougLZ8MgdK-WbEVdioVdlsIhS9xJfzo2Z7TSPe-RAWKrM_rCojibw5KZxVp4o42oPBwOq_Fxxrs_7ZHYM0HQYqHTEmBn27YsbewQEY4h5qDd-yBKmdnDct-EAs_Fm3DykSFgt4NLio4xDB6oXQSUihDpRLOJYSkcyZTY6kAwhDah9OsBB-fdgo1KV59XJTOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی در ۲۵ تیر با شرح: ترمینال مسافربری فرودگاه بوشهر و باقی‌مانده‌های یک هواپیما
سخنگوی دولت، امروز: فرودگاه بوشهر دیگر قابل استفاده نیست و باید از نو ساخته شود. از یک هواپیما که تازه خریده بودیم فقط دم آن باقی مانده است.
Vahid
سخنگوی دولت جمهوری اسلامی می‌گوید فرودگاه بوشهر در حملات اخیر آمریکا کاملا تخریب شده و دیگر قابل استفاده نیست و «حتما باید از اول ساخته شود.»
فاطمه مهاجرانی روز سه‌شنبه، ۶ مرداد، در نشست خبری هفتگی‌اش با خبرنگاران گفت در بازدید از فرودگاه بوشهر «بقایای هواپیمای نوی به تازگی خریداری شده» را دیده که بر اثر اصابت مستقیم موشک، جز بخش کوچکی از دُم آن، تمام بدنه آن نابود شده بود.
این نخستین بار است که یک مقام حکومت ایران از تخریب کامل فرودگاه بوشهر بر اثر حملات به ایران خبر می‌دهد.
@
VahidHeadline
یک توییت به همراه اسکرین‌شات‌هایی درباره اطلاعات یک ایرباس ۳۱۹:
عمر این هواپیما 24 سال بوده! سال 2019 هم خریداری شده بوده.
iranimerican
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77571" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_tlczmcM-_dDLIbLIw2_tmoDp_L0F9xIvV_FhLhi7J1DxtvgbE5zLraW3QCMUCwSAXnVpMts9DejdUOY_sGo2FXi8bCMnoX2JG5EbhhYYevkMeoQuRNF0P84KgPR5ipEuwV9Y8T_Jf_3HwNKMv9-dkPCmxNcIcQk6mI610s3InUvsvwZtEZFwYZo6Cp9I2lrV-NNjJkOHUHxg0CIjIFvFzbXjfXO6ab0ezzR1xSjBc3pFeE8tV3I8VQa_po1PR1tI0Zx0075B0X4R5jJusvwy_olAsw46GfToFSCAhvmIaYOd-TLGsTpstCPbPFvW5jbodpQWLlsxmdrD7JXc7hZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های نزدیک به حکومت و شماری از مقام‌های جمهوری اسلامی در روزهای اخیر بار دیگر بر اجرای قانون حجاب اجباری و برخورد با زنانی که از این قانون تبعیت نمی‌کنند، تأکید کرده‌اند. هم‌زمان روزنامه «همشهری» با انتشار گزارشی، از قوه قضاییه و نیروی انتظامی خواست با آنچه «هنجارشکنی» و «بدپوششی» خوانده، برخورد کنند.
روزنامه همشهری، وابسته به شهرداری تهران، در گزارشی با اشاره به انتشار ویدیوهایی از حضور زنان بدون حجاب اجباری در سواحل کیش، مراکز تفریحی، مراکز خرید و برخی رویدادهای فرهنگی، این موارد را نشانه «حیازدایی فرهنگی» توصیف کرد و مدعی شد که ممکن است بخشی از این رویدادها در قالب «پروژه‌ای سازمان‌یافته» برای تضعیف ارزش‌های اسلامی انجام شود.
این روزنامه با اشاره به ویدیوهای منتشرشده از ساحل سیمرغ کیش، برگزاری نمایش‌های مد، جشن‌های مختلط، کنسرت‌ها و تغییر الگوی پوشش در اماکن عمومی، خواستار ورود دادستانی و نیروی انتظامی و برخورد با افرادی شد که از نگاه این رسانه، قوانین مربوط به حجاب اجباری را نقض می‌کنند.
هم‌زمان، شماری از نمایندگان مجلس نیز بار دیگر خواستار اجرای قانون موسوم به «حمایت از خانواده از طریق ترویج فرهنگ عفاف و حجاب» شدند. محمدتقی نقدعلی، نماینده خمینی‌شهر، مدعی شد «برهنگی و بی‌حجابی مانند خوره به جان جامعه افتاده» و از مسئولان خواست اجرای این قانون را در اولویت قرار دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77570" target="_blank">📅 17:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ijYRfv8i38Fuj5XP-TYkO9Md2dDhqQQVBcdhiwJ6WG2v3CFetgbJfqvDEJ8HBwNrOkqUS5VLVmWsIM_bX8rvRN1jxxnrb81XWRnUY3LjY75Ms1aVgKvtXkMDg8PocEQyy6M1XwbaO8ktlbzj54tvX6F5euVTh3ytdByFsuAFTxhlsoP3m85f1Y51OvqCEQOkZF-zPZBsr2n7arIgwI96Vlibl06zn0fFKAYr53wpO1DJiXuXCXKI9Qg1W5MMm0UV0EHC1JIBVHCbxjrzVjja4DlqPRBGwEg95XZB7HJ7DNM_iuw5WFD6gbqR1GmJMTManIK6c7D9tIFG3Kq3tstxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=jHL_VZuoUzHpf0-DW_R2YYQi58uUWZs9h6-9XHDlCjOzn94kiLEoQm0_oT0BfbQ-iQRpMkwflE4ghnJnDxZO0gyrgB3hDRf9jszeGL6-WbYnkvR3PBqpTolfYeBlMLNwR1duGicxW0dnrMU0Hc---hb2qk-P-7F-gRBlO1VDN1S1S2E-oAcRA2fJQR9YyGBcXKJ4by6MywMeGNMaqVenor91CXRHEd-xttr1DvgHxWUCK7k2zgSReMaFKCH818Qo5kHxMBsYosgY2fn0d0N1QmcGwBZWznvBL-NBxUsaIXOV1LnX0TAUSA1uHfmxG5m-yq9Yj671UTl1mKNvqeRlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=jHL_VZuoUzHpf0-DW_R2YYQi58uUWZs9h6-9XHDlCjOzn94kiLEoQm0_oT0BfbQ-iQRpMkwflE4ghnJnDxZO0gyrgB3hDRf9jszeGL6-WbYnkvR3PBqpTolfYeBlMLNwR1duGicxW0dnrMU0Hc---hb2qk-P-7F-gRBlO1VDN1S1S2E-oAcRA2fJQR9YyGBcXKJ4by6MywMeGNMaqVenor91CXRHEd-xttr1DvgHxWUCK7k2zgSReMaFKCH818Qo5kHxMBsYosgY2fn0d0N1QmcGwBZWznvBL-NBxUsaIXOV1LnX0TAUSA1uHfmxG5m-yq9Yj671UTl1mKNvqeRlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران تن به توافق ندهد، کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق را می‌زنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، روز سه‌شنبه گفت که گفت‌وگوهای خوبی با ایران در جریان است، اما بار دیگر تهدید کرد که اگر تهران با آمریکا به توافق نرسد، تأسیسات زیرزمینی در کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق ایران را هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز اعلام کرد که در صورت امکان ترجیح می‌دهد پل‌ها و نیروگاه‌های برق ایران را هدف قرار ندهد.
ترامپ توضیح داد: «من می‌توانم همه نیروگاه‌های برق آنها را ظرف یک روز از کار بیندازم. تمام نیروگاه‌های برق آنها از بین خواهند رفت. فکر می‌کنم حدود ۹۱ میلیون نفر باید بدون برق و بدون پل زندگی کنند. و این یک توازن بسیار، بسیار ظریف است.»
او تصریح کرد: «آنها می‌دانند که اگر توافق نکنند، من این کار را انجام خواهم داد.»
دونالد ترامپ هشدار داد: «می‌توانم بگویم ظرف دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همگی نابود خواهند شد و نیروگاه‌های برق هم ظرف یک روز.»
او افزود: «اگر بتوانم از انجام این کار اجتناب کنم، ترجیح می‌دهم از آن اجتناب کنم.»
رئیس‌جمهور آمریکا همچنین با اشاره به تفاهم‌نامه امضا شده بین واشینگتن و تهران در خرداد ماه که در درگیری‌های تیرماه به آستانه فروپاشی رسید، گفت: «ما دیگر نمی‌توانیم اجازه دهیم آنها توافق‌ها را نقض کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77568" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnOAJwslKBKbrusNK_FH6C6G_mP8g0-0M-Eb-TOkId8sEFpJhCw6Ix1woA-7Z_k0c6H5RVbzXN6tc3xOMQAc56DUd9jwbYaF5wsR_5kkN27JpFWpcJoV1K24jU-RGNmA8r4u4auSMubm4-FUq0RJIEUm5QEP4ntttSB6LeF1t_n-_Sg2dNkSZ10WLJbVoA2jnDZ7gKbU6A7J1KEayyIaInSteEMZmcoY6RnMH34AD87LMqYKY9tV9uTJuhlORWw_QFiaAR-afqNa3PU84xjkLDrga5PLFUimi5NQOsXk844AgkMFOaxX_fP49sL2zWuvwmcJuJ_M_jZjZnkz75ugvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmQFZsaeC4ERLYS4dKbxtrxMwmpJpgjCyPy8kSqmrP_ljMheZPeqodam1Fl5BbQjXOI9Xnr2Su1IAyeVEGkAFbkp4M70OC1kz-0uh4n4SfN8UyLEI5Oah7AOKOHDqQHpwK8TgbrErh1wMf4-Rt4dgiPjmddm_K2tRju3RchQsSoWJ_2Cn-iovne_TfIJp7EK1b13Szf5dEHv84DAa38mHI2apJgXrpI_XK28Z8i0n3sKE-N8pTNLPDql7vIAhLWwnJ8_ZWPeE_7MfRXJu3ZrJ_eKJw47tt1zdeGR3NmVlCu9inlG3mVqEnsw1T7iSc8GGd7DlRYVWVoM_l1571U8eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل روز سه‌شنبه ششم مردادماه در مصاحبه‌ای با کانال ۱۴ تلویزیون این کشور گفت که در هفته‌های اخیر، جت‌های جنگنده و بمب‌افکن‌های نیروی هوایی ایالات متحده از پایگاه‌های هوایی اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
کاتز گفت: «ایرانی‌ها می‌دانند» که این جت‌ها از اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
به گزارش اورشلیم‌ پست، کاتز در این مصاحبه گفت: «امپراتوری مغروری که اسرائیل را به نابودی تهدید می‌کرد، فروپاشیده است.»
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در کنفرانس امنیتی کانال ۱۴ با اشاره به دیدار دونالد ترامپ، رییس‌جمهوری آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واشینگتن گفت آمریکا در موضوع ایران منافعی دارد که فراتر از منافع اسرائیل است و افزود: «بسیار مایلیم به ایران حمله کنیم، اما آمریکا موافق نیست.»
کاتز با اشاره به آنچه دستاوردهای اسرائیل در برابر جمهوری اسلامی خواند، گفت: «امپراتوری متکبری که اسرائیل را به نابودی تهدید می‌کرد، در هم شکسته است.» او تهدید کرد: «اگر به سوی اسرائیل شلیک شود، با تمام قدرت حمله خواهیم کرد. ما آماده‌ایم با توان خودمان به ایران ضربه بزنیم.»
وزیر دفاع اسرائیل در پاسخ به پرسشی درباره واکنش احتمالی اسرائیل به پهپادی که روز سه‌شنبه از عراق پرتاب و در مرز اردن رهگیری شد، گفت: «ما می‌دانیم چگونه امور را مدیریت کنیم؛ آماده‌ایم.»
کاتز همچنین گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، «درک می‌کند که اسرائیل از مناطق حائل در لبنان، غزه و سوریه عقب‌نشینی نخواهد کرد». او افزود: «هفته گذشته از غزه بازدید کردم؛ هنوز تونل‌های بسیار بزرگی در آنجا وجود دارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77566" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjzV6-sJOfOpJZdASU4P4cpkOCz0Fd0SodGHDZknwXd5sQuIYeM3U94kVtCyM7b9o3ZoIqwl_G9xWFJO-uWT3UwBZwLnXtEZYvvC3eRxuH9mjiPRzjf264df1s3arvA4m2YtK1Fcdj_Xi0PY6IAeHmQ2MiaqkHijj0_1A0-N3TkRDgaLsnppUSOFwlgR-QI6YiG7NEFW17oFGfFovJWsmjDq82r85A1mmRQyh_2ewP6GKaHvXybM5GHg2KpWRnBRkt-ACDuHCUDip41XFRGnQa6Y0aqlkqLRJ_yL7vHZNy9S31de4kpbXYsEoAZh8fAhr7e2SpJM0wtaggQMbp9mcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه می‌گوید که حمله اوکراین به کشتی ایرانی در دریای خزر «باید به‌عنوان حمله به خود ایران» تلقی شود.
دیمیتری پسکوف، سخنگوی کرملین، هشدار داد که این حمله نشان می‌دهد که از بین بردن «تهدید ناشی از کی‌یف» تا چه اندازه اهمیت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77565" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFExAu33eTzsm1jAT8RJl13A58QDIcyV4PUFR1Q4L5BZgb-6rUdsFc4_MzXCEYp4lsDcWE0bI9URax_5SVvHSAz5ST2w9ASLOQIRkWjL6zePrMWdv5ItGiF3el2YYlLd9Bguuo1MGd5-eTkNi37BES8JZfNn8RraL4y4g3g7enuwOcNfh3oAsaXXmbX2UzUoJ2YciLlAp2nDWJRxYGHhNBiCuicaF7q6obqduPmgiqMAZL_weR2uLX4-pM5GESxX_GBNUf7QNWXP4soNkILbZJlEifdBvPmGZTe-pqfwK1JVI6lvvl0yjfeSwVhK5R3usy8Yp_6ZxVCKaJj-A-OElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس برنامه‌های اعلام شده از سوی کاخ سفید، دونالد ترامپ، رئیس جمهوری ایالات متحده، روز سه‌شنبه ششم مردادماه، با رئیس‌جمهوری اوکراین و سپس با نخست‌وزیر اسرائیل دیدار خواهد کرد.
دیدار ترامپ با ولودیمیر زلنسکی ساعت ۹:۳۰ و دیدار با بنیامین نتانیاهو ساعت ۱۱ صبح به وقت محلی برگزار می‌شود. برنامه روزانه کاخ سفید نشان می‌دهد که این دیدارها بدون حضور خبرنگاران برگزار خواهد شد.
با این حال انتظار می‌رود که پرزیدنت ترامپ، در لحظه آخر اجازه حضور خبرنگاران را صادر کند.
برنامه بعدی ترامپ پس از دیدار با نتانیاهو، حضور در مراسم یادبود لیندسی گراهام، سناتور جمهوری‌خواه فقید است و نخست‌ وزیر اسرائیل نیز در این مراسم حضور خواهد یافت.
پیشتر نتانیاهو اعلام کرده بود که موضوع ایران در صدر گفت‌وگوهایش با پرزیدنت ترامپ قرار دارد.
دیدار ترامپ و زلنسکی نیز پس از آن برگزار می‌شود که شامگاه شنبه سوم مردادماه، نیروهای اوکراین شناورهایی حامل محموله‌های نظامی جمهوری اسلامی به روسیه را در دریای خزر هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77564" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GAJ0hCH6-A7R_7Yc5aXWNIG0E5UxjzKcriaaqSdcV-TikCQsf2jsDnHfp22OaEK2TUq6s3KE3YS2ZJ6MijA4sV2ry_FO0g_Tg289b-ZydgdL71S5DxfclVsOK38cdpkV1C4TpTMgmAFNAJvd7_DHvG3vegr3p_ni0TLU4Nb2_jkwW5qioID3CGixc7uoOnOv-_0d75FdOlvNzR9QxaKBwb9HAJt7Osq4isbwDmBx-5j6FFui3G1MkbtL0X25kIwq1HWUICcvOBeYAvEdxeyNdcRgic0Y9Qhoyo8klcUIqbedaoqWrOfWrnwet-BfKNMZBQ45Ff7MBnk5VfdEoWMSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاسین سرفراز، بوکسور ۱۷ ساله اهل بجنورد و عضو تیم ملی بوکس ایران، که در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت شده بود، به سه سال و سه ماه حبس محکوم شده است.
کمیته آزادی زندانیان سیاسی خبر داد، پرونده این ورزشکار نوجوان در شعبه چهارم دادگاه کیفری استان خراسان شمالی رسیدگی شده و او تنها در یک جلسه دادگاه، بدون دسترسی و حق انتخاب وکیل، به اتهام «اجتماع و تبانی علیه امنیت ملی» به سه سال و سه ماه زندان محکوم شده است. این حکم حدود پنج روز پیش به او ابلاغ شده است.
یاسین سرفراز از ورزشکاران شناخته‌شده بوکس ایران به شمار می‌رود و پیش از بازداشت، در رقابت‌های کشوری، آسیایی و بین‌المللی موفق به کسب عناوین قهرمانی شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77563" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f473hTWC0ns_TRXrx6Ya807KXmJKjp9yelDSxboTrnhVac1vxBcMFTPLQLvkfzhRgc_HZLJTxNQATeEwABtG_VOOdYXJBeNFHOsm7u2-kNYQAi5JyK-7N-eTDv39rioELXDNObvFriObIF5g8U-M23-dkTxBsfwrbyO_PtuYzZoWltZsufejBwbCLcsqmB6BBn7PX5cKaHW-ssQRsguWtDGNLlrPBUFNDyjTC7riQo3RMtI-G9OjWfjZBIGfSAw_51-PR63HloqfVsgbcvnjwFlto0NRKlE26ILD2GwAb2rlVDOD55G-2V6FHEKUUB9OWcSjkW_od6G7wl4ZMPyp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز سه‌شنبه ششم مرداد به نقل از یک منبع آگاه در خلیج فارس گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
به گفته این منبع که نامش اعلام نشده، پیشنهاد عمان مورد حمایت کشورهای منطقه است و بر اساس آن ایران کنترل انحصاری این آبراه حیاتی را در دست نخواهد داشت.
این پیشنهاد الگو گرفته از نحوه مدیریت تنگه مالاکا بین دو کشور مالزی و اندونزی است و بر اساس آن، عبور از این آبراه با پرداخت داوطلبانه هزینه در تأمین مالی ناوبری، حفاظت از محیط زیست و جستجو و نجات همراه است.
عمان پیشتر به طور رسمی اعلام کرده است که با مدیریت متفاوت تنگه هرمز به شکلی که ایران می‌خواهد موافق نیست و پیروی قوانین بین‌المللی خواهد بود.
پیشتر مقام‌های ایران تأیید کرده بودند که مذاکراتی را با مقام‌های عمان در زمینه مدیریت بر تنگه هرمز انجام داده‌اند. سخنگوی وزارت خارجه ایران هم روز دوشنبه تأکید کرده بود که در حال حاضر تنها مذاکره‌ای که ایران در آن دخیل است مذاکره با عمان درباره تنگه هرمز است.
دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که این کشور «مذاکرات خوبی» با ایران داشته و احتمال توافق وجود دارد، اما او هشدار داد که اگر مذاکرات به نتیجه نرسد، حملات ایالات متحده از سر گرفته خواهد شد.
در همین حال، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه با همتایان عمانی و سعودی خود در مورد تنگه هرمز گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77562" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t_6xtGPApYpVRHxQV41HSYdGdwFh0Bcq4bYRwlCIGZYoCWGAJSXDhW6yHDUNnOaKe96locB1qGhfRiid-v8K2rSeCOjQMskNAoeuTMAxczZeP6viauEmWmZ8qoATmx3YhI9QjxUbQIeb1vYdV8E6Oi_HeDyagOgql-n0L6YitnSB4C3orHls_2vM5IQCL_03r6faG1VmWnRhrtMZ4Z7uY3RG6vVhHSPwJHsxuvnPtcGYSxRh_pdQQFcI8_UcmZ_G7yaeWszAx-dTJJln2t0JSJhOCUDafO6eJKVRy-xE63LlHomf3pSS_EHJIVwjqDsWcFDb1jomo17C483uB6OQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J0-_AkqfBV15io5FcrGhEnl9pC6tw5F5zs_8QoBqmUtJM-St83Ny8IaSI8EXzYFfHWHK213Kcij4hkC40n-JRtNuj7vCdSAyAwhg3rfyr76MA0O_ovpHW-P3YsVdfmW5yVAJzbtcjOcIGDzcIqI3zza6ikGC2iHS2qOZ8H3EBR5a9R_9LsBtOraxJoADRv6EP6lK26nMD1mG1oF5mtAF6N41zXrLLUCR7SfPsWoVPmxtrImHMzw71mkRSxYxHe702_NP7DDa07oo1H2m8Pn3dBh_5BwIlv6wBylVIDXjjOwiShEorSgB3_KH-xYGo7isvHOIOIeorPYJF9ljWQhNDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قائم حسینی، امیرحسین ملکی و علی دشتی، متهمان پرونده میدان علیخانی اصفهان، در آستانه اجرای حکم اعدام قرار دارند.
از خانواده‌های این معترضان دی خواسته شده برای آخرین ملاقات به زندان مراجعه کنند.
قائم حسینی پسرعمه گل‌محمد محمدی است که ۲۸ تیر اعدام شد.
این پرونده ۱۲ متهم دارد که علاوه بر محمدی، تاکنون سه تن دیگر از آنان به نام‌های عرفان اسفندیاری، ابوالفضل سپاهی و امیرحسین صفری نیز اعدام شده‌اند.
@
VahidOOnLine
شروین باقری، از معترضان پرونده اصفهان، در آستانه اجرای حکم اعدام قرار دارد.
به خانواده‌ او گفته شده برای آخرین ملاقات به زندان مراجعه کنند. شروین باقری نیز در حال انتقال به سلول انفرادی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77560" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TMnKybznfN44oLiVsPj9LbF0uJST0wKOv7pV317p5I-rjYaC83lC_X2Y0dc8uy9m-ExoosBcrb338bUgdjfuV8LI86h6I9iN_8evql5Tk4tBBR2ClXxDijOB9uQVPPG8nnI8v63UPx96uDCVgUXmQwPL2G53HrfxWSICoFFN3p7z4QJZi_10PP0taicUuMv61JDSxr-yfdrR4af29uU8i3FWol9MsoYHjS2qhRDt2N4amkDpo2QJgudnJDXgQsRo1tLxGQKMfo7H8IZtQOWeGl4C0w2u0MWiDtN8rXZyYNH5JG3jdJL4b9aenQfbOmUdHet_a4ICPhSypijxWeBm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی بدون نام بردن از کسی نوشتند سه نفر از پرونده ملک شهر اصفهان اعدام شدند.
آپدیت:
بعدا ویرایش کردند نوشتند: دو نفر
آپدیت:
قوه قضاییه جمهوری اسلامی اعلام کرد بامداد سه‌شنبه حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو معترض بازداشت شده در اعتراضات دی‌ماه در اصفهان، اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77559" target="_blank">📅 05:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=B776bD6KfnK-rZ1w-ggWQr0f90FKBstiGyrAj6kXUWOb6NlNvyWZ_wiyrXNMV9YN_lfoXGtk9d9tZEvSPI1u3nRRNWjjEey_Suv9KzBTXINHcL78fgb8Znltn1DFMjwXUiKwRIspOTOwHUcsoTPc7-VF2lRCF-M50ScizijaSqkpFVba6hvngktz9mrs8FYA5NcI6vmj-bqf-6MokWEfr-pJtirjkZeJs6ixkvaw5vmGBvxgEkN9B4SyVBSuowB81y9OUcXKnCJIBkWsRCtfwljbpiecFqDQSYvbqpo4_91nvJjjja__hNyEDXi6OZZeM0wxyV5Vcf9bYP8RFUp0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=B776bD6KfnK-rZ1w-ggWQr0f90FKBstiGyrAj6kXUWOb6NlNvyWZ_wiyrXNMV9YN_lfoXGtk9d9tZEvSPI1u3nRRNWjjEey_Suv9KzBTXINHcL78fgb8Znltn1DFMjwXUiKwRIspOTOwHUcsoTPc7-VF2lRCF-M50ScizijaSqkpFVba6hvngktz9mrs8FYA5NcI6vmj-bqf-6MokWEfr-pJtirjkZeJs6ixkvaw5vmGBvxgEkN9B4SyVBSuowB81y9OUcXKnCJIBkWsRCtfwljbpiecFqDQSYvbqpo4_91nvJjjja__hNyEDXi6OZZeM0wxyV5Vcf9bYP8RFUp0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار منتشر شده در شبکه‌های اجتماعی حاکی از آن است که خانواده‌های زندانیان سیاسی محکوم به اعدام و شهروندان در میدان علیخانی اصفهان تجمع کرده‌اند و گزارش‌هایی نیز از درگیری یگان ویژه جمهوری اسلامی با معترضان منتشر شده است
این گزارش‌ها می‌گویند نیروهای یگان ویژه جمهوری اسلامی با موتور، خودروهای زرهی و سلاح‌های سنگین در محدوده محل اجرای اعدام مستقر شده‌اند و اینترنت در اصفهان دچار اختلال شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/77552" target="_blank">📅 05:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kaQDjlOGJHq55-ORpbQ1GO5UC-3Iv897NfQ8-sa2vTWFj8zNYSF2hEZrALxGnUx8BbtrFrpJB8a7hPzFiwi1LnBz8l1bHuRrvKEEiTdRvG_mfN7GHWEN0GQTk8uH50xRb8FEXFjuiZiTBf4zvdfM76bGLSsX1OsyMur7olWMJ3n3oPZfhZ3mzDrwGcL5ANgVRD6ZftB47v03yl47Rg8LuufbrsQQn9lica_P2iW2RfJU3BmbFUCPYsoslB-1pMvFI4HeCcpecRftmqLa9OjGuMCjQOLDGX21Yw9AipGr-kLCBIhP3dld18FxbgU29fxacNYVb7c5k0ijOrCSg28AIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sSQZ5kjX40fluoCXK345yQu_KlJwnob6A8KeNuYCfR0wmbjipKg635gbh3nw8ufCzBTKJrU4tBjDw3dRt1IAVZNzb2c3toXbObVxIgmgRf6lIphMRd_syhec1vJZI5_GojraFmO6lZ3VGRrLbU1wSmRH0kBd2iVmkxqwbH9eRU2s5UsmcNyj9Sqg6Iyina6AZ4poIaPOH4sBp_pyzo3SfoXfDkg6w2XXncFUxvqGfpemFrcmSsQyFqltVaIL05vUeml_FxAYi_MIhgyChUjusJWQkq-9_vBmGImBE3fUPEFYKO5HsJKFnK9BNJHQDy_JBEsp2goELyPI8vr7ikKZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mFRK3Dc_X70C1KNldsdMLL8MxYOkM7OXDwVJtPMF3LXin72wlrr__UnCIzsoFetmWyDNqeiFhSYFDtP5Fk_XRF7xD_9jygmxpXPMe1mpXdEauCs2xtazAxbyOSLKvpAcPk4FnS8C-ZN73bxpFEXgdRQg3e_E8uVF-0AvZbhmuVS5HP59PY1WD-3LXB21HqjXUhRDJ6yW_6Vo4lak2ThqMfvLzwPXPqb78GUkzgP50X7hGYO9JX62G3mSjB5WwiwjCylAeYsBiIxWTZNk5_yWKw6OdIJXZW96sj9iO4oI0fGpUx-3KbCTfzIXY9iTIdqR-9cQ6VLiq5atUJAtlmA5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GyvVeoDi8flEnYVDBOI1-7xoCri_OhXrRuTG0Vh3Bre5bPf4uyElsQ_RKSNjbpN8AYF8JFS7sXsqQJIwLpGCFYiKbbbGQHl5lJm_rwy1dBcExq_OSPBsOW18ail4HzccyxNP43cMl_9qg0_58HvudskE7JtIvGKp23pUkmq-VLSlUZrByuLdy-hW-L_IF0Zuju6md_VXJ7KhFfpFz8KSCLQ-Dh1Z0TGow5mT80r_xcOgLxePEzEE13e_SsGQeV8rWPzl7_MMbJ_iit5tj_uqDonNDjjm8wR0n5JmJ4hevgL-FkDKghhkfD01ePHkjmCekFprXv_kdhZK6aPVuZkHxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faf260cfea.mp4?token=czzK1gJHzMqQyc9Zu3dqg01hbnjAybEPU3pDkd9bmjO4qKFfwHZB1Mm1qhEr9gInBwQ-M_ZX6tvNSL1AvCUhqvIJpqqDG7QaUqa92CMsrxRhNA0eRL1E4TY9Ds4uCfRBsD-1DhNokCqr1FmUCFSEzGnelqdf8OGq0RkTtTYa_9x1zXBm2__mnKCDNnjzpOr3XRBFJBNaPXyVso-D6hsWFLQSopryTuR7GfPwiOzQ9ewxwad59vlaENz_SHt_sQ9ndw6fNZqsN_8SAbwKLiMody5pCqAO2orcqbNKPvlhVhb6H6KaJaZLMChX9W1Kp2betCsmdlPHAkr6mU3dOCVoUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faf260cfea.mp4?token=czzK1gJHzMqQyc9Zu3dqg01hbnjAybEPU3pDkd9bmjO4qKFfwHZB1Mm1qhEr9gInBwQ-M_ZX6tvNSL1AvCUhqvIJpqqDG7QaUqa92CMsrxRhNA0eRL1E4TY9Ds4uCfRBsD-1DhNokCqr1FmUCFSEzGnelqdf8OGq0RkTtTYa_9x1zXBm2__mnKCDNnjzpOr3XRBFJBNaPXyVso-D6hsWFLQSopryTuR7GfPwiOzQ9ewxwad59vlaENz_SHt_sQ9ndw6fNZqsN_8SAbwKLiMody5pCqAO2orcqbNKPvlhVhb6H6KaJaZLMChX9W1Kp2betCsmdlPHAkr6mU3dOCVoUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.   «علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای…</div>
<div class="tg-footer">👁️ 484K · <a href="https://t.me/VahidOnline/77545" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=XJXmLkgnS3dsZzwCjadocp8AFykiRo8AsCy4xd6b599m6Z7fOhZXOO8n6pY2He3JEEoPgIvreUD-E_VbGA1Wy8qbRAObJHOut9JBZIkCR3ldV28OubIMN9vcONiFVlqC6kD75iKEWPtVyQ3k9YOdsQSkMpL_sbUKq4rFv4t2LlcyZ-doaBFdIrOPe7aNge2OK-a8GV30628G9enMx5ojMDfR9BmbZQ4ZlB59ofOF_QFS9B80rAKMZxdSl9yPUgIcX9i5CgdwaK2yrimuAx7Bw85lI_XmrNEH5BLSeVClWh019R9mRXYAdoxC1v5FhTJd2IpQsAjLW-cl0XKgs_bn_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=XJXmLkgnS3dsZzwCjadocp8AFykiRo8AsCy4xd6b599m6Z7fOhZXOO8n6pY2He3JEEoPgIvreUD-E_VbGA1Wy8qbRAObJHOut9JBZIkCR3ldV28OubIMN9vcONiFVlqC6kD75iKEWPtVyQ3k9YOdsQSkMpL_sbUKq4rFv4t2LlcyZ-doaBFdIrOPe7aNge2OK-a8GV30628G9enMx5ojMDfR9BmbZQ4ZlB59ofOF_QFS9B80rAKMZxdSl9yPUgIcX9i5CgdwaK2yrimuAx7Bw85lI_XmrNEH5BLSeVClWh019R9mRXYAdoxC1v5FhTJd2IpQsAjLW-cl0XKgs_bn_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از سخنرانی ترامپ در میشیگان:
- آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
- همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
ترجمه ماشین:
ترامپ: ... ونزوئلا.. پس از آنکه تقریباً ظرف ۴۸ دقیقه پیروز شدیم، گفتند: «اوه، حرکت خوبی بود.» خب، همین اتفاق اکنون در ایران در حال رخ‌دادن است.
مردم هنوز متوجه نمی‌شوند. ما نیروی دریایی‌شان را نابود کرده‌ایم. نیروی هوایی‌شان را نابود کرده‌ایم. رهبری‌شان را نابود کرده‌ایم. تسلیحات ضدهوایی‌شان را نابود کرده‌ایم.
پهپادهایشان اکنون با حدود هفت درصد ظرفیت قبلی تولید می‌شوند. بخش عمدهٔ توانایی تولید پهپاد و توانایی تولید موشکشان را نابود کرده‌ایم.
اکنون با ما دربارهٔ دستیابی به یک توافق صحبت می‌کنند؛ اما اگر ما این کار را انجام نداده بودیم، هیچ مذاکره‌ای در کار نبود.
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
آن‌ها قلدر خاورمیانه و قلدر ما بودند. اوباما ۱٫۷ میلیارد دلار پول نقد سبز به آن‌ها داد. یادتان هست؟ پول‌ها را داخل یک بوئینگ ۷۵۷ گذاشتند و به تهران فرستادند؛ ۱٫۷ میلیارد دلار پول نقد.
او تصور می‌کرد می‌تواند به آن‌ها رشوه بدهد؛ اما آن‌ها در عوض با خودشان گفتند: «این کشور چقدر احمق است.»
نه، نمی‌توانید به آن‌ها رشوه بدهید. باید شکستشان بدهید و ما داریم حسابی شکستشان می‌دهیم. اما خواهیم دید نتیجه چه می‌شود.
اکنون مذاکراتی بسیار دوستانه در جریان است.
نیروی دریایی ما در اجرای محاصره چقدر خوب عمل کرده است؟ حتی یک قایق [نتوانسته عبور کند]. آن‌ها می‌گویند: «دیگر محاصره را نمی‌خواهیم. لطفاً، لطفاً، محاصره نکنید.»
---
ترامپ:
اکنون قیمت تخم‌مرغ بسیار پایین‌تر از زمانی است که کار را آغاز کردیم. خواهید دید پس از آنکه تهدید هسته‌ای ایران را از میان برداریم ــ که بسیار زود اتفاق خواهد افتاد ــ اوضاع چگونه خواهد شد.
اما افزایش قیمت‌ها ربطی به من نداشت.
---
یکی از سخنرانان همراه ترامپ:
۴۷ سال طول کشید تا کسی بایستد و بگوید دیوانه‌ها نباید سلاح هسته‌ای داشته باشند.
همچنین چندین دهه طول کشید تا مشاغل را دوباره به داخل کشور بازگردانیم.
---
ترامپ:
نمی‌توانستیم اجازه دهیم آنچه در ونزوئلا اتفاق می‌افتاد ادامه پیدا کند و اقدامی که انجام شد بسیار قاطع بود.
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
اما هزینهٔ عملیات ونزوئلا، همان‌طور که گفتند، تاکنون جبران شده است. به همین ترتیب، در برابر جمهوری اسلامی ایران نیز با اختلاف زیادی در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز به سلاح هسته‌ای دست پیدا نکنند.
وقتی کسی می‌پرسد: «چرا این کار را انجام می‌دهیم؟» پاسخ این است که نمی‌توانیم اجازه دهیم شما سلاح هسته‌ای داشته باشید. همین تنها چیزی است که لازم است بگوییم.
اگر قدرت سلاح‌های هسته‌ای را درک می‌کردید، دقیقاً متوجه می‌شدید که چه می‌گویم.
---
بار دیگر می‌گویم: ایران هرگز سلاح هسته‌ای نخواهد داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77544" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ویدیوی مصاحبه ترامپ با زیرنویس فارسی در پایین همین پست
متن بخش‌هایی از مکالمه، ترجمه ماشین
:
🔺
خبرنگار:
درباره جنگ ایران؛ آیا از پیت هگست، وزیر دفاع، به‌دلیل توصیه‌هایی که در اوایل جنگ به شما داد و نتیجه‌ای که جنگ پیدا کرده، ناامید یا عصبانی شده‌اید؟
🔻
ترامپ:
نه، به‌نظر من او کار فوق‌العاده‌ای انجام داده است.
ما ارتش آن‌ها را تقریباً نابود کرده‌ایم.
آن‌ها می‌خواهند دیدار کنند و ما هم داریم با آن‌ها دیدار می‌کنیم. خواهیم دید چه اتفاقی می‌افتد. این احتمال وجود دارد که بتوانیم به توافق برسیم.
بدون کاری که ما انجام دادیم، حتی حاضر نبودند با ما صحبت کنند. آن‌ها هم از طریق واسطه‌هایشان و هم مستقیماً درخواست دیدار کردند و ما داریم با آن‌ها مذاکره می‌کنیم. می‌دانید، ممکن است اتفاق‌های خوبی بیفتد.
فکر می‌کنم قیمت نفت امروز به‌شدت پایین آمد. تا حدود یک ساعت پیش هم بازار سهام سر به فلک کشیده بود. اما نه، آن‌ها درخواست دیدار کردند. اگر عملکرد ما ضعیف بود، درخواست دیدار نمی‌کردند.
تنها دلیل اینکه می‌خواهند ملاقات کنند این است که ما ضربات بسیار سنگینی به آن‌ها زده‌ایم.
🔺
خبرنگار:
چقدر دیگر در برابر ایران صبر خواهید کرد؟
🔻
ترامپ:
وقت زیادی دارم؛ وقت بسیار زیادی.
تمام نوار ساحلی‌شان نابود شده است. تنگه در وضعیت بسیار خوبی قرار دارد و همین حالا هم در حال مذاکره هستیم.
می‌دانید، آن‌ها می‌خواستند صحبت کنند. افرادشان گفتند: «لطفاً بمب نریزید. دیشب و شب قبل شلیک نکنید؛ دو شب این کار را نکنید.»
می‌دانید، گفت‌وگوهای خوبی داریم. بنابراین خواهیم دید چه اتفاقی می‌افتد.
فکر می‌کنم احتمال خوبی وجود دارد که اتفاقی بیفتد. اگر چنین شود، خوب است. اگر نشود، دوباره به همان کاری برمی‌گردیم که دو روز پیش انجام می‌دادیم.
🔺
خبرنگار:
آقای رئیس‌جمهور، ارتباطات با حوثی‌ها درباره دریای سرخ چگونه بوده است؟ آیا نگران...
🔻
ترامپ:
حوثی‌ها؟ این مشکلی بود که مدتی پیش با آن روبه‌رو بودیم و همان‌طور که می‌دانید، حسابی آن‌ها را درهم کوبیدیم. بعد از آن دیگر هیچ مشکلی با حوثی‌ها نداشتیم. اما در حال حاضر در آن موضوع دخالتی نداریم.
البته ممکن است دخالت کنیم. می‌دانید، اگر مشکل‌ساز شوند، احتمالاً مجبور خواهیم شد وارد عمل شویم.
🔺
خبرنگار:
درباره عربستان سعودی؛ آیا نشانه‌ای از عربستان دریافت کرده‌اید که به پیمان‌های ابراهیم بپیوندد؟
🔻
ترامپ:
هنوز درباره آن صحبت نکرده‌ایم.
🔺
خبرنگار:
در صورت گسترش درگیری، آیا نگران کاهش ذخایر مهمات هستید؟
🔻
ترامپ:
ذخایر زیادی داریم. انواع مختلفی از مهمات در اختیار داریم. می‌دانید، بایدن مقدار زیادی از آن‌ها را به اوکراین داد و ما اکنون در حال بازسازی آن ذخایر هستیم؛ اما همچنان مقدار زیادی داریم.
از تسلیحات رده‌میانی هم مقدار زیادی داریم؛ بیشتر از آنچه در هر شرایطی بتوانیم مصرف کنیم. مقدار زیادی داریم. صادقانه بگویم، دوست دارم مقدار بیشتری داشته باشیم، اما بایدن حجم بسیار زیادی را به اوکراین داد.
وقتی من رفتم، انبارها پر بودند.
وقتی پس از اوباما به ریاست‌جمهوری رسیدم، او مهمات نخریده بود و ذخایر بسیار کمی داشتیم. من آن ذخایر را بازسازی کردم. اما به‌محض اینکه رفتم، آن‌ها مقدار زیادی از آن را به اوکراین دادند؛ ارقامی که هیچ‌کس پیش از آن ندیده بود.
بنابراین اکنون با سرعت بسیار زیادی در حال تولید هستیم. کارخانه‌ها در حال ساخته‌شدن‌اند و تجهیزات بسیار زیادی تولید می‌شود. به‌خصوص تولید سامانه‌های پاتریوت در حال افزایش است.
ذخایر زیادی داریم. هرکدام از پیمانکاران ما همین حالا در حال ساخت چهار یا پنج کارخانه هستند. وضعیت بسیار خوبی داریم، اما قطعاً دوست داریم از برخی تجهیزات پیشرفته‌تر مقدار بیشتری داشته باشیم. بایدن مقدار زیادی از آن‌ها را بخشید.
...
🔺
خبرنگار دیگری:
شما و نخست‌وزیر نتانیاهو درباره ایران هم‌نظر هستید؟
🔻
ترامپ:
تقریباً. بله، تقریباً. اختلاف کوچکی داریم، اما در مجموع تقریباً هم‌نظر هستیم.
می‌دانید، ایران طی ۱۴ روز گذشته ضربات بسیار سنگینی خورد و آن‌ها خیلی مؤدبانه از ما خواستند: «لطفاً متوقف شوید. بیایید مذاکره کنیم.»
اکنون در همین نقطه قرار داریم. خواهیم دید چه اتفاقی می‌افتد. اگر به توافق نرسیم، دوباره همان کار را از سر می‌گیریم.
🔺
خبرنگار:
رئیس‌جمهور زلنسکی می‌گوید روسیه تصاویر ماهواره‌ای پایگاه‌های آمریکا در خلیج فارس را در اختیار ایران قرار می‌دهد تا به آن‌ها در هدف‌گیری کمک کند. درباره این موضوع چه کاری می‌توانید انجام دهید؟
🔻
ترامپ:
بررسی خواهیم کرد که آیا این موضوع حقیقت دارد یا نه. از پوتین درباره آن سؤال می‌کنم. خواهیم فهمید.
اگر چنین کاری انجام شده باشد، تأثیر چندانی نداشته است، چون ما آن‌ها را حسابی درهم کوبیده‌ایم. این‌طور فکر نمی‌کنید؟
ببینید، روس‌ها تجهیزات زیادی در اختیار ونزوئلا قرار دادند. تمام تجهیزات ونزوئلا روسی بود. نتیجه‌اش چه شد؟ چندان خوب نبود.
بنابراین ممکن است تجهیزاتی داده باشند، اما اگر چنین کرده‌اند، موفق نبوده است؛ چون آن‌ها دیگر ارتش، نیروی هوایی، نیروی دریایی یا هیچ‌چیز دیگری ندارند. بنابراین نتیجه خوبی نداشته است.
فکر نمی‌کنم روسیه چنین کاری کرده باشد؛ دست‌کم نه در سطحی گسترده. اگر هم کرده باشد، بسیار بی‌اثر بوده است.
....
🔺
خبرنگار:
درباره دارایی‌های ایران؛ گفته بودید دارایی‌های ایران برای پرداخت خسارت کشتی‌هایی که در تنگه هدف قرار گرفته‌اند استفاده خواهد شد. آیا ایالات متحده مستقیماً به شرکت‌های کشتیرانی پول پرداخت خواهد کرد؟
🔻
ترامپ:
نه، نه.
از پول ایران برای پرداخت خسارت‌هایی استفاده می‌کنیم که خودشان ایجاد کرده‌اند.
به‌عبارت دیگر، پول ایران که تحت کنترل ماست برای پرداخت خسارت‌ها مصرف خواهد شد. خوب به‌نظر می‌رسد، نه؟ بد نیست، درست است؟
همین‌طور هم باید باشد.
🔻
ترامپ:
بسیار خوب، سؤال دیگری هست؟
....
صادقانه بگویم، با بسیاری از کشورهایی که بدون ما دوام نمی‌آورند بسیار مهربانانه رفتار می‌کنیم.
می‌دانید چه کشوری بدون ما دوام نمی‌آورد؟ اسرائیل.
بی‌بی دارد می‌آید؛ خودش این را به شما خواهد گفت. اگر من دخالت نکرده بودم و آن تأسیسات هسته‌ای را که عملاً در آستانه تولید سلاح هسته‌ای بودند، به قول خودم، به خاک تبدیل نکرده بودم، اسرائیل چند ماه پیش نابود شده بود.
سال‌ها پیش هم اگر آن توافق وحشتناک اوباما را لغو نکرده بودم، اسرائیل نابود شده بود.
🔺
خبرنگار:
نخست‌وزیر نتانیاهو درباره فروش جنگنده‌های اف‌ـ۳۵ به ترکیه با شما اختلاف‌نظر دارد. نتانیاهو با تحویل اف‌ـ۳۵ به ترکیه مخالف است. آیا قصد دارید به او بگویید...
🔻
ترامپ:
نه. ببینید، ترکیه برای من متحد بسیار خوبی بوده است. فکر می‌کنم او [اردوغان] کار بسیار خوبی انجام داده؛ در سوریه هم عملکرد خوبی داشت.
او دوست من است و هیچ‌کس به من نمی‌گوید چه چیزی را باید بفروشیم یا نفروشیم.
ترکیه برای من متحد فوق‌العاده‌ای بوده است. البته ترکیه طرفدار پر و پا قرص اسرائیل نیست. این را می‌دانید، درست است؟ او طرفدار بی‌بی هم نیست، اما ترکیه برای من عالی بوده است.
ضمناً ترکیه کشور بسیار قدرتمندی است. ارتشی عظیم و بسیار قدرتمند دارد و تجهیزات بسیار خوبی در اختیار دارد.
🔺
خبرنگار:
آیا نتانیاهو از شما می‌خواهد با ایران توافق کنید یا می‌خواهد حملات را ادامه دهید؟
🔻
ترامپ:
بی‌بی واقعاً عالی بوده است. نمی‌خواهم بگویم کدام گزینه را ترجیح می‌دهد. او نخست‌وزیری در دوران جنگ بوده و ما در کنار یکدیگر عملکرد بسیار خوبی داشتیم.
اگر امروز به ایران نگاه کنید، قدرتش فقط هشت درصد چیزی است که چهار ماه پیش بود؛ هشت درصد چیزی که چهار ماه پیش بود.
خواهیم دید در نهایت نتیجه این وضعیت چه خواهد شد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/77543" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: اگر مذاکرات با ایران شکست بخورد، آماده «اقدام نظامی شدید» هستم
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه به اکسیوس گفت که تصمیم گرفته است حملات آمریکا به ایران را متوقف کند تا فرصت دیگری به مذاکرات بدهد؛ اما تأکید کرد که اگر دیپلماسی شکست بخورد، ممکن است دستور ازسرگیری عملیات نظامی گسترده را صادر کند.
چرا مهم است:
مذاکرات کنونی بر دستیابی به توافقی جدید متمرکز است که تنگه هرمز را بازگشایی کند و گفت‌وگوها درباره یک توافق جامع هسته‌ای را از سر بگیرد.
▪️
مذاکرات عمدتاً میان ایران و عمان انجام می‌شود؛ اما قطر، پاکستان، مصر و فرستادگان ترامپ، استیو ویتکاف و جرد کوشنر، نیز فعالانه در آن مشارکت دارند.
آنچه او می‌گوید:
ترامپ در این مصاحبه گفت: «ما در حال مذاکراتی بسیار جدی و عمیق با ایران هستیم. اگر این مذاکرات به نتیجه نرسد، بار دیگر به اقدامات نظامی بسیار شدید روی خواهیم آورد.»
▪️
وقتی از رئیس‌جمهوری پرسیده شد تا چه مدت حاضر است به دیپلماسی فرصت بدهد، پاسخ داد: «زمان زیادی نه. یا باید سریع پیش برود، یا اصلاً پیش نخواهد رفت.»
پشت صحنه:
ترامپ گفت روز جمعه تصمیم گرفت حملات را متوقف کند، زیرا کشورهای میانجی از او خواستند فرصت دیگری به مذاکرات بدهد.
▪️
ترامپ گفت: «همه کسانی که با ایران سروکار دارند از من خواستند: "حمله نکن."» او تأکید کرد که به باورش ایران خواهان دستیابی به توافق است.
در میان سطرها:
ترامپ در توضیح اینکه چرا با درخواست میانجی‌ها موافقت کرد، گفت: «نه چیزی به دست آمد و نه چیزی از دست رفت.»
▪️
او خاطرنشان کرد که پس از توقف حملات، قیمت نفت کاهش یافت و بازار سهام رشد کرد.
آنچه باید زیر نظر داشت:
ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
▪️
ترامپ گفت: «می‌خواهم با بی‌بی درباره این واقعیت صحبت کنم که اگر من رئیس‌جمهوری نبودم، ایران تا الان به سلاح هسته‌ای دست یافته بود و اسرائیل نابود شده بود.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77542" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxu8eD4WIURdy9zrh0pegnZLETkq8vbdqqhBxx40veaaWJKAMTlewslyZEtKd0aPTLrjzKy99oJgiZToucY9A2mOPpQQcVmXgBHS56ZlRJ8lFHLBcV_BLByJh237tq018MaOTJnm9OALIfaG4FzviaUQDak04ILyk9dsDWXYTAaSRGkW8cqgmuA8BQ2E4rLUcu27TF_rVMV2ekIcaHsYxgfYobGDRwwn0C2L8uK9otgpiHiAa08gu4K3FiRtFRhoIuzY1JqBtIPVqYATh9X8j5PcEkaT92OQ9O6GzUftzUGn0XlQFH8EDgSRK-P_jW8f3CQw3oYtHlqqvIhH22tUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای «حوثی» یمن، وابسته به جمهوری اسلامی اعلام کردند با استفاده از پهپاد، تعدادی از مراکز انتقال نفت خام عربستان را در مسیر انتقال نفت از شرق این کشور به بندر ینبع هدف قرار داده‌اند.
«یحیی سریع»، سخنگوی نیروهای مسلح یمن، دوشنبه ۵مرداد۱۴۰۵ مدعی شد که این حملات در واکنش به آنچه «نقض حریم هوایی یمن توسط پهپادهای سعودی» خوانده، انجام شده است.
در مقابل، وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور تعدادی پهپاد مهاجم را که به گفته ریاض «از سوی گروه‌های مسلح مورد حمایت جمهوری اسلامی» و «از حریم هوایی عراق» به پرواز درآمده بودند، رهگیری و منهدم کرده است.
به گفته این وزارتخانه، این پهپادها قصد حمله به تاسیسات نفتی در منطقه شرقی عربستان و شهر ریاض را داشتند.
وزارت دفاع عربستان تاکید کرده که براساس «حق مشروع دفاع از خود»، پاسخ به این حملات را در زمان و مکان مناسب، حق محفوظ خود می‌داند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد. این وزارتخانه از دولت عراق خواست تمامی اقدامات لازم را L«برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی» انجام دهد. درخواستی که به نظر می‌رسد اشاره‌ای غیرمستقیم به نقش جمهوری اسلامی در حملات به عربستان دارد.
همزمان، خبرگزاری‌های نزدیک به سپاه پاسداران، از جمله تسنیم، با انتشار تصاویری مدعی شدند حملات ترکیبی پهپادی و موشکی حوثی‌ها موجب آتش‌سوزی در تاسیسات نفتی بقیق، یکی از مهم‌ترین مراکز فرآوری نفت جهان، شده است. تسنیم این حمله را «ضربه مهلک نیروهای یمن به اقتصاد عربستان» توصیف کرد.
با این حال، مقام‌های عربستان تاکنون وقوع حمله موفق به تاسیسات بقیق یا آتش‌سوزی در این مرکز را تایید نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77541" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJxAODDhtZSCZxwInt56TOXBDpX8Qu0Sa2deYBMG0-vWlOkEoh1stQAS5A1plhyUR13nGWsfcpVYgT3NRQFz2C5KwE90YRNGZHv9pX3cRMXMnryv_leoRVKbHpDaLcnumN8Izw7PgVHFqhxX8reBtaaRBaeyNme1JJX_Gke_0KdsSDJILCqmXIYzosYCPx0_dC0cLVLxewSqb59TiPi9wdd1KTREAfnTIYx99CdOc9gWWpvIzwfTr-IdG0qePsbn-690cI_mvdd9SFcZEtGS1ZDwx1TTzBOKmvxfQCLfiTqdIVr8lEkN8HesHVpJ_ipA9PkEV1uVuHpVsbTQpMDS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر امور خارجه اوکراین  در واکنش به
پست عباس عراقچی
ترجمه ماشین:
تهدیدهای ایران ناموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین سلاح برای جنگ جنایت‌کارانه مسکو ــ سلاح‌هایی که از سال ۲۰۲۲ تاکنون اوکراینی‌ها را کشته‌اند ــ به آن دامن می‌زند.
ایران هیچ جایگاهی ندارد که خود را قربانی جلوه دهد، چه رسد به اینکه بخواهد تهدیدهایش را با ارجاع‌های مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات می‌کوشد توجه‌ها را از اقدامات تروریستی روسیه علیه کشتیرانی غیرنظامی در دریای سیاه منحرف کند؛ اقداماتی که امنیت غذایی جهان را تهدید می‌کند. اما موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنشی قاطع از سوی جامعه بین‌المللی داریم.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77540" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef1qWuO9KumrVFYAEk3dr3IXAJr_NH7Nck0zFl8eMiYPFZMT7vOi94EoTHbDnMqnnqthF0KDk5Q3t6Gw_-zSs7aUKvNST6YZWzX9zu3B3XT6CLDNcToI6YGe2APJoXMVpaZwLiIpoVOgZB5CpcivfWZTPHW-Jmq4d6Y4uqwPc-DzJKiYEcYsKSS4B7--s5GhX1t6mUdO8_0mFASYBc8JnyZRfwMWk823a8G0GO3C7OBEW1eOl6CNQIXu_WwhPF6hmMiIOZjN9yQxH0u57BkhsoDnApZHbi43wa6oeD8qRzcSLyZSXOcBey1pHV_3qwHWdYKLNJQS-rZ4hF0gB7rdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی روز دوشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور، پهپادهایی را که از عراق به‌سوی تأسیسات نفتی در استان شرقی عربستان و همچنین شهر ریاض پرتاب شده بودند، رهگیری و منهدم کرده‌اند.
این وزارتخانه اعلام کرد که این پهپادها توسط گروه‌های شبه‌نظامی مورد حمایت ایران در عراق به پرواز درآمده بودند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد و بار دیگر بر حق این کشور برای پاسخ به منشأ «تجاوز» و بازدارندگی در برابر عاملان آن تأکید کرد.
این وزارتخانه همچنین از دولت عراق خواست تمامی اقدامات لازم را برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی انجام دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77539" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQrh_ZZPh8oESYH30qdQlSqnjc3ZSlqQC4kAZAVfnatahDuaUVNwYdMZ8h3ICt-RkzIzMDUnhbQtjRBANoXDTuCUFadJ0k_6cvfuGVSfNuXCaDybN0-Jbw3GEPZCisU8k2vUKNEtKOMSZq-pRlc8VetfWXDoO-dT8g9t88v_cfGPwZUtPfJ7tRbnqmtffSWQ9C9vXF81wPqcaaWKtD06w38PNDBQzHJ70VTDRfU-TKfFAQmBQ-0Oe7spQw1eY1_FQnbLvp0xBweAKR2KCRgMUp8T1qiSBDwwH32z5F8XRpx74wLFD9xn4JD9rk3-z9iaTOyQvTFz0tmDfS4AgQFECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح اردن اعلام کردند که صبح دوشنبه دو پهپاد را رهگیری و سرنگون کرده‌اند.
این بیانیه مشخص نکرده است که چه کسی این پهپادها را به پرواز درآورده است.
کمی پیشتر، تایمز اسرائیل گزارش داد که ارتش این کشور دو پهپاد مشکوک را بر فراز مرز اردن رهگیری کرده است.
در آن گزارش نیز درباره منشا شلیک این پهپادها و زمان دقیق رهگیری آنها توضیحی داده نشده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77538" target="_blank">📅 17:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThYHJ9TmiSZpZX-xNPyeuMZsvSKQ7nDPEl3CH5gf-eQPbmM9SwuKHzjhGMhdcJT-Or9hEP5SAajcqLWldHgEwblYHj-4wPSbHaNicfZ66rChKIZhkoA4d5iRyva3GXJjdk-ALn3AoXbVLI9-5GkVZl_oMLWZJCBvOQrcSccz75bNice47axYUrF5ZVR57bDKlX5yKBKLUhdXRGIFwMaJqJKE8lhBeNgHA2DMLPbQSHkFp3roFnfBYzcLEJA9oOtLahJEHw0XEYDqkORn0Oz4zS7e9ZvUHmc0hCdYrdubvuSpsidwvzhouUyBllo4D3qCLRLptuXfe_ynr6Gaasewmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«احمد الشرع»، رییس‌جمهور سوریه، روز دوشنبه ۵مرداد۱۴۰۵ در گفت‌وگو با شبکه «الجزیره» اعلام کرد دمشق با مشارکت چند کشور در حال تلاش برای دستیابی به یک توافق امنیتی با اسراییل است.
الشرع ابراز امیدواری کرده که چنین توافقی بتواند زمینه را برای دستیابی به «صلحی فراگیر» فراهم کند، بدون آنکه «حق سوریه بر بلندی‌های جولان» نادیده گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77537" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce_xiBnNeS59KZg5f9v_mZTlyRbi4cSETEhENyZNE3xLh93k_10_y_8ZhzHpzvun3R6x6y-Fx9Hvvnuf-r4qknB0m6y-VWzhH8IJ0_6pg69KmiklZwa5g3eRipaIMk1M7ub0S_778ZjEtrZ0qUlnCHO8f1Q1GCqgpGwwgmMhxP3c5d4ezkCB_7Q3nPmz9ObyOQzIb2-ykz9ju9mEAa7drayZ4wAyOpZ8Ohn_naZ1jwF_PkXU0s_kDBxRIW7IItssiKi2rA4sGCzOEbKNdVyE1jwc436Ero1UgrFxrxo3yq2E4ofCujrTUc9eWyAQSDaGbXPxHuLzAAQwrWpzIk3OoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل، می‌گوید هرگاه دوباره به نخست‌وزیری برسد، «فورا» قطر را کشوری «متخاصم» اعلام خواهد کرد.
آقای بنت در شبکه ایکس، دولت قطر را «خشن» و «سرطان یهودستیز» توصیف کرد که «شاخک‌هایش را در سرتاسر غرب و حتی در دفتر نخست‌وزیری اسرائیل دراز کرده است.»
او همچنین مدعی شد که در دوران نخست‌وزیریش، اطلاعاتی را دیده است که نشان می‌دهد قطر به سپاه پاسداران کمک مالی می‌کرده است.
این سیاستمدار راست افراطی که از چهره‌های اصلی اپوزیسیون اسرائیل است، قطر را متهم کرد به‌دنبال «نابودی» اسرائیل است.
آقای بنت نوشت که قطر «کشور پیچیده‌ای نیست، میلیاردها دلار در یک شبکه نفوذ قدرتمند جهانی سرمایه‌گذاری کرده است که صدمه زیادی به اسرائیل وارد می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77536" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWxCTSGoPu13dHkOZezvhgIVwEpeog4Zj7dWomCOJIeZrykSp8LMuWArhFHdU2-3yILvfT6VMI6f-jtMpYw89akO5Ve8qmCHaxAQIi6spn9ulk7nSoDnJlAVtB1tn8NYWHSXzCZ9Bd2RFZywW2pw1rqSr4lMPVEF2y66EPqJk7DDUL41K2hOfKPKanAoNt_ccn7XtzVJVXEjQmqy9FeaxbXLLc0P1RKuZqiS9eKccU3o5xMKr69xHeJvViEq3zQSBWvibTqFy7x2LbdMclsiyX8r2WKhS9Sdsa7Ry9A05rAPxjbPIWEJytEM5sCuOQDZ4i4Fy-8wTVJFigPqELxpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع بریتانیا گفت کشورش از اقدام تهاجمی در برابر جمهوری اسلامی حمایت نکرده و نخواهد کرد.
وس استریتینگ در مصاحبه با شبکه اسکای‌نیوز افزود این موضع را در نخستین هفته کاری خود صریحاً به پیت هگست، همتای آمریکایی‌اش، گفته است.
استریتینگ روز ۲۹ تیر و در جریان تشکیل کابینه اندی برنهام، نخست‌وزیر جدید بریتانیا، این سمت را بر عهده گرفت. او در همان هفته با هگست درباره امنیت دریایی در تنگه هرمز و تعهدات ناتو گفت‌وگو کرد.
او گفت با وجود این، زمینه‌های فراوانی برای همکاری دو کشور از تأمین امنیت تنگه هرمز و جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تا سرمایه‌گذاری در توان نظامی بریتانیا و ناتو وجود دارد.
استریتینگ همچنین گفت اروپا روزی از دونالد ترامپ، رئیس‌جمهوری آمریکا، سپاسگزار خواهد بود که قاره را از رخوت بیرون کشید و متحدان ناتو را وادار کرد مسئولیت امنیت خود را بپذیرند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/77535" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rl-EupEEX4icthfNmjmf-yK2d8o9rn6g6GJ1SrgNQNCS7weGDHZEq48Cwx40ZECJbIYMUsQS62Yb59YEhWq1Yes_NN3Vppr8CfBUyaqJ89xR3bZ9aaqEXVCPVY8vwMkY2PdpJjmRltiMXMp77LWcLTzIc4S_shYihsKeOk5Z7LXu_7fjxMIALLIKSsrdqkJnfJK-teAP9OTHfr6TxOMGD3uTNyQLz2uEQKDgG4k4ROrDh9Jr2ARir5LUUJhFbG0SsL6LQK0DW1HtVt6hWDqIbAzGLsF02hBa-U_5FbGJM6JHyPniG8V11PnLLZKwzOuuo3G01GqqTdpzJBjspvXAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77534" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKL8Cf80u81PoP6ZgLudVwEyib3VfGGBWpfYvEcXdb9oMx06STS3l9YZNI0605n0DsIBNE7dwZLWTN1cQ7aDB1RdvsZQ2W9E0Yqkap1Ji5l8QVBd_5tfNGHV7Kbufam7OUytW_vwXQbO8YSEpAnH6J2MtNylmbYuZ1xxDZehk3KSRqzMQIiVZidIFoIZPs06zFBMfWmauWn_JepUWzsPbKC5N8cT60W3q-ZXkBdwEEHmV-6-m5rG9SzxOL7a3RRWS4IW9Mr3G-7j3WxbhW5U6t5ZNyihbVvpVq8g5HcLO727l2mzgghPW-YobgiLPp0ACI-Vz4j_OuLdgfcIiBwrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، دوشنبه ۵مرداد۱۴۰۵ در نشست هفتگی خود با خبرنگاران، گزارش‌ها درباره درخواست ایران برای مذاکره مستقیم با آمریکا را رد کرد و گفت: «درخواست مذاکرات مستقیم با آمریکا اصلا با ژن ما همخوانی ندارد.»
او تاکید کرد که در حال حاضر هیچ مذاکره‌ای میان تهران و واشنگتن جریان ندارد و خبرهای مربوط به درخواست ایران برای مذاکره، «خبرسازی» طرف‌های مقابل است.
بقایی با بیان اینکه جمهوری اسلامی هرگز از دیپلماسی برای صیانت از منافع ملی خود گریزان نبوده، گفت در شرایطی که آمریکا به گفته او همچنان به اقدامات «ایذایی و تجاوز» علیه ایران ادامه می‌دهد، تمرکز جمهوری اسلامی بر دفاع است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77533" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZZAHkHktwrdwrCpYyXIs1QDBPaYqd5Y2_Qt4EGjEklSRFzoTFRFPbGTM6sdf8Bh5J9X84VHQu_9wahw7_c2EyLjXkZK-BZeaK65cnRxjWML72OiyRWuuqHfnkDzmTMkXqt1K0nSdZV04h9qyFeitL1znt5WXhpamy3tKxa6Ijg9gcII9fveQfJowB63LwG_efBZzlXY099YaEseavBSOy5mB_PaEvMUIDbCxE9XlJiAjj0URmASCLp3hov4ljj_A4QDCF8MfDjKlJCnPAdPJk61eBsSDg3nS4npaJMl94Fz--ZnXItD9L8UfcyVl9EpATD4V4vG1W64WOAHWZ-uNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون حکومتی ایران روز دوشنبه پنجم مرداد خبر داد که سپاه پاسداران در بامداد همین روز مانع عبور شش کشتی از تنگه هرمز به قصد خروج از خلیج فارس شده است.
خبرگزاری صداوسیما در کانال تلگرام خود نوشت: «در ساعات اولیه بامداد امروز دوشنبه ۵ مردادماه، ۶ فروند کشتی متخلف با خاموش نمودن سامانه های ناوبری و موقعیت‌یاب خود... قصد عبور از مسیر غیرقانونی و نا ایمن جنوب تنگه هرمز را داشتند.»
اشاره این خبر به بخش جنوبی تنگه هرمز نزدیک به سواحل کشور عمان است که اعلام کرده تابع قوانین بین‌المللی برای استفاده از آبراه‌هاست. ایران در مقابل اصرار دارد که کشتی‌ها باید از مسیری که سپاه تعیین می‌کند عبور و مرور کنند.
خبرگزاری صداوسیما همچنین نوشته است که یکی از این شش کشتی‌ «دچار حادثه شده» است، اما تاکنون هیچ منبع دیگری این خبر را تأیید نکرده است.
روز یک‌شنبه هم خبرگزاری تسنیم، نزدیک به سپاه پاسداران، مدعی شده بود که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/77532" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD8kPJr0l3Ge4p43Ja9FmfiBl43KUFXP9IDT87_uyTPGIU_xKltoFw_irCGkNAX5dCWEbKkHsrXzqqPhaxCa0tHRkl8ctngSja6NnYVArrziqJ7zh6idvsHRDP36_s44IDyn6hCZJKqsDkr1eb4rfDoleuj-rV0nps-02ef3Zf6umPv7aFPWxv1aV8OKfdaUfHHYuLjnNTSusftciomrug8SVYNhnxUAxLwJLHsxnBTKmZi-NxwWSMVTT-sToHFdY8rcd-wyHjGbS7Po6W77T72dXpXaOUXzJrLEOl66-H-3HrYVYS6Gkh4AiVTQzSfwhCAvIme17WxmuckmgOBsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت امتداد گزارش داد حکم محکومیت پژمان جمشیدی به تحمل ۹۹ ضربه شلاق به اتهام «رابطه نامشروع» پس از رسیدگی در دیوان عالی کشور به طور قطعی تایید شده است.
الهه محمدی، خبرنگار امتداد، به نقل از ملیکا پارسا دوست، شاکی این پرونده، نوشت شعبه نهم دادگاه کیفری یک تهران این حکم را صادر کرده و پس از اعتراض و فرجام‌خواهی، شعبه ۲۹ دیوان عالی کشور نیز رای صادره را عینا تایید کرده است.
بر اساس این گزارش، اتهام مطرح شده در پرونده بر مبنای ماده ۶۳۷ قانون مجازات اسلامی (بخش تعزیرات) بررسی شده است. طبق این ماده، مجازات رابطه نامشروع تا ۹۹ ضربه شلاق است و در مواردی که عمل با اکراه و عنف انجام شده باشد، این مجازات تنها برای فرد اکراه‌کننده در نظر گرفته می‌شود. به گفته امتداد، دادگاه کیفری یک و دیوان عالی کشور در این پرونده تنها پژمان جمشیدی را به تحمل ۹۹ ضربه شلاق محکوم کرده‌اند.
ملیکا پارسادوست با اشاره به قطعی شدن این حکم گفت صدور رای نهایی نشان می‌دهد «فضاسازی‌های دروغین» درباره این پرونده، پایه و اساسی نداشته است.
او همچنین تاکید کرد اجازه نخواهد داد آنچه بر او گذشته با روایت‌های دیگر بازتعریف شود و گفت از ابتدا این اتفاق را «خشونت جنسی» توصیف کرده است.
پارسادوست در ادامه گفت هرچند این حکم از آسیب‌های وارد شده به او نمی‌کاهد، اما در شرایطی که به گفته او اثبات خشونت جنسی در ایران دشوار است، احراز این موضوع از سوی دادگاه که رابطه «بدون رضایت و همراه با اکراه و عنف» بوده، برای او و دیگر زنانی که تجربه مشابه داشته‌اند اهمیت دارد.
او در پایان با اشاره به کاستی‌های قانونی و دشواری‌های پیگیری چنین پرونده‌هایی گفت با وجود مخالفت شخصی‌اش با اجرای مجازات‌های بدنی، پرونده را تا پایان پیگیری خواهد کرد و ابراز امیدواری کرد این پرونده زنان دیگری را که با خشونت جنسی روبه‌رو شده‌اند، به شکستن سکوت تشویق کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77531" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f52us-iZ1GfL-DynTtQgJXDDAjZIHZGsck-nA5tBldPomg-nHfmlZqFygsmy4k7M0wFY51TwE1KU0umbn8c7qAMD4tyKb2xCXH1XAQgW2sYkEVPlShvbcK2L2f5sjCG6m7FEfOj30t7PBCGEAuYL_INFrXd01A1slvSDuJnKCp0C4qId8yPB1X3qT9_M3ValotgJekh8cyb70SKycWDgt4t2hrL3KxEiR28TKlVJ0k_KXjFLQq6lmQHoPnDeKNBV8RzymzskNGkUsMmDqrtoN_vbcvtfjQa9eoQMGbi9R-eA9_wa2Tv9pcRi5IdXlXDt3SY4EeTrvVsUcpjTlAvNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش خبرگزاری «رویترز»، همزمان با ادامه وقفه در درگیری‌های مستقیم میان ایران و آمریکا، بازارهای جهانی روز دوشنبه با «کاهش قیمت نفت»، «افت ارزش دلار» و «رشد محتاطانه بازارهای سهام» واکنش نشان دادند؛ در حالی که داده‌های حمل‌ونقل دریایی از ادامه اختلال در مسیرهای کشتیرانی منطقه حکایت دارد.
بهای نفت خام برنت بیش از چهار درصد کاهش یافت و به حدود ۹۲ دلار در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز بیش از پنج درصد افت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77530" target="_blank">📅 16:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Weu5Pn1Vv-T9ahHCx8bhWJgvAi0BT8yXF07xF--vX2EckNS-TLgZizUCGVvs-7loSSFqNX3SMVrCrTCfEppif-fenhUcBonS3-C_EdFAkHAnztxodxNdIvF6vAztenhthyBQZlDnasP839ZjqLp4DaY1AdeftkoVkAJHj4utKDGKAM0UQ-ga8kKa4JuZfuMrnk3mlf5KY13BclprANkwddLa_Yurkx3_X1VLGaVw4U5LW7oUs8qC9SeR0_H3Da9xeVv39EBTYblGsuqVLrpUukhe1D5hiLqaZM8KkMbByA7EA4lt4sxFVMVK8OzVRRDL4HaOb3Z4PlyawX233S_DVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در بیانیه‌ای که به روزنامه وال‌استریت جورنال فرستاده، گزارش‌ها درباره کاهش ذخایر مهمات این کشور را رد کرد و گفت ایالات متحده «بسیار بیشتر از هر کشور دیگری» مهمات در اختیار دارد و میزان آن نیز «بسیار فراتر» از نیازهایش است.
بنابر گزارش‌های دو روز اخیر، ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، کاخ سفید را در جریان کاهش ذخایر موشک‌های رهگیر پدافند هوایی قرار داده است. این موضوع برای او نگران‌کننده است، هرچند معتقد است پایین بودن ذخایر مانع ازسرگیری عملیات رزمی گسترده علیه ایران نخواهد شد، اما خطرات آن را افزایش می‌دهد.
چند مقام آمریکایی نیز به وال‌استریت جورنال گفتند دریاسالار برد کوپر، فرمانده سنتکام، معتقد است آمریکا می‌تواند با محدودیت ذخایر پاتریوت و دیگر رهگیرهای پدافند هوایی کنار بیاید، زیرا در صورت تأیید ترامپ، افزایش حملات آمریکا توان ایران برای شلیک شمار زیادی موشک را کاهش خواهد داد.
کارولین لویت، سخنگوی کاخ سفید، و شان پارنل، سخنگوی ارشد پنتاگون، تأکید کرده‌اند ارتش آمریکا برای اجرای هر مأموریتی که ترامپ انتخاب کند، تمام امکانات لازم را در اختیار دارد.
وزارت دفاع آمریکا شامگاه جمعه کارزار تازه خود در بمباران مواضع در ایران را پس از ۱۳ روز حملات هوایی شدید متوقف کرد و تا امروز، بامداد دوشنبه حمله‌ای از سوی آمریکا گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77529" target="_blank">📅 16:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQElW-Kg_GgWDT6WUNw6ElNS-y3zPb2r9rvJaxarkCxpKD_Mt0WAcmT1TSZzbIn37LweJg0ZD6QtSypqn4vQknj_3WnflKbYqh1zJioGiXIGBSt3vCgeAJWn_tnAbs8UXOLVSeQirljbROQ6qZVXct5d0P2CvXxP6R4hycxFWxvIOjfapQ6mKMt9GYbB_IHy45aC988nDfcQRREBkQfcPqiov01OvXVxXK5TfBry9_r_Z3bn58GvLmmn-bkiqUVykFur5wBH25LFcRL2BFYIFJBulaWJR2QJgo__phP3ZQfqL2aSavFVi8zxzj5vXeDpBvQ4xdYkJMKDsozl561YAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.
«علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای حکم آن‌ها در صبح سه‌شنبه ۶مرداد۱۴۰۵ بسیار جدی است.
همچنین به ایران‌وایر گفته شده است که «سمیه افشار»، مادر علیرضا سپاهی و مادر همسر ابوالفضل سپاهی، در همین پرونده به پنج سال حبس محکوم شده و هم‌اکنون دوران محکومیت خود را در زندان سپری می‌کند.
اطلاعات موجود در حال حاضر تنها درباره وضعیت این دو محکوم تایید شده است. با این حال، از آنجا که چند متهم دیگر این پرونده نیز با حکم اعدام روبه‌رو هستند، این احتمال وجود دارد که افراد دیگری نیز برای آخرین ملاقات فراخوانده شده و در معرض اجرای حکم قرار گرفته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77528" target="_blank">📅 16:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KldyV6UsnBvS44EAOF6Noh3rAK3Hms8_z0JMhST8vIvR8ZAxoPuoUvg2adKbyzDXCxk-nnv4VD8Kg9YLCEqiHq_EeMJrbd7dx2V38dtCjXIHC1uT8_raqQ_vhUqVBZU7YgFPmwZxnabbSvpuqyzK-90hWwjqOTZT2V-mj3aUVaatmktQMlY3k7rtEV2B-bWwcBfwAm5hMU_PWFaAReMUqWpc29kCdeG58EswDSFYV8pugDEx8aruV7ZnDNFcuUsf25pRB1Hce1RabmAN3MfcgbrGU8VZkTPTf9mFc1dexzfIJgdFQ3EVcXqtohnz6hyEmd2sZHNHhBWnguwcJZa9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aSbGMc_EnlLAJC8RUmaGKdz6-wdPR6uJSpJUUfi4Z2Vj4v5zfB6fwCw_j4XPsQNIKFX_FiWJZ7GYQeCpze5CZO20b_2tvMFsAtij_Wz1J_xw0yK_02fPY7N-qzVH9aapQw_mA4uryvn7uBxpdaDtB_XFKxrtEXonqEOel-WRiYVfCHDzCZNUVrReGslcMW0-aN2b9Q27E-UwOvLbZ0Id0erPaoCfsoqv2p-NjhTnFIW3pRSnmdqzyextIlfVn4x3gudziNdyDwaltIWrW5KNWGIf2c3sxovzmSeXd5DqEc1KtQ8iAM784k6elfIemC2nP9Dl9vFLfpVNzqlsFizubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZD6UGxm2pz2aI4BfYXWXbt5OmXAUz-iSrKAGyBEYwHIsXeztr0qPQMcAsnD55TSbvbdn2qREBycLgnUsHTk0uHfZFJMQYBVGN14KsKRWeERj4ucclp7uu7bMDiDq_rAmkVDwjJH5mUzEXSDXPSqQqNn-HbeI-OKCF5hM0WF3eaiU2iRK9EtLalSXSzZcUH-bv_1Hplk7v94GKx_phSw4FBfYGuU_jb_1__fPFloD0sGT_88zRTnnvsiuT23prxYQ9lc7Ez8bmfRyB7M932qcNSoV80HgO7UIQZQ-tDhVS5-f4A88_79idlXRYdVnHKR4H3X-KPC2SlJBXTiYQlagnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P6daMPdyTnj0PNyoRW-8KMqup9pPl7AGmttNRRUtOk7ZoR7D5A0BqSEQANFxsijBEqiFqaBxhHENI48OYckHQUPLg-xDUUn_tFFvxHD7JPyYtKtQmkzZo_ycgrWgucRwgx2pyjYKyFvQXGgNbPS0nf4Bid2Hbnbhup7mx2TQi-UXfKsvBWiJH04Zu4G4MbnZKbVaSuIZHzuePFEggYkx7PIz_6jS_xshpsdAyV9LNzBagRvJx3bmw95HwWeGcK1Fh8gYW-kE2BSS8LMh2PdkF5-qpk4L1boM8siXYNt9Vo5BSFcwpEpLnfNDqy4KBKNzUsBBfEPh_gLsJEws1Qc2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vd1AGCukXlAxfsR6O3e0pO_mtbuEiquFYuXLD1vbe92M7UU3JM4fYN-OtPnRPLNt3U1YCsBA4w7EBXY1pYrT9XoUYvgCP29wMHjtMF986DgvD3rz5pMVJSS8mihk-MYRNqTMlu9kKt6OGU8kfl-tGqYwjcVVHv326ECDEayQdfhPvIKSqEjJkc_FO0vJYeirRJNfveWFD1e7uMlQ1aPyNyYd3LyUwKCVw_ZQCDtdxs-aZYaAHxp5WFNeIY1q_TYZ9PKffk7U5MmCqwsBffaVrCQsCEQfbTCoVPvxi0qvuyNK-ddk3CwB31bB53xB3VIwgya0bDe2A_kK3ET9qLls7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HE3L1GdJepEHB5AonApWQWW4rCbnj1Li7Xr0Hnh22lMZWqEKCWUM1AlA0IS0yiVnkSRULE876C2bXU4UrxG5oPY_k9pj-0chZAJT0z8mNQiH1Q5O6lbn8pJoxah6rToiCtqm8zF1AMXB5LJM7tfSy-jd27k4yDcqaSRwnJ7q1oN3vtTtehrp-VzkRUnTxtp1lBj6Yd9VP69sw1WoaKPVgc8OqcqD6_ylOIPnA3Wqchn2iVprjPI8gcC2Sk32VquAjVM6W-pGkCRswEMf89q2gidLqIcumfIf9gwCSJxw7a8tlisdMEuDHJGSCVV9yraudLGtUFgfA2-YtEIWm8YloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ely42GumuXdev1C4iZ5XzrDDz-9g7Wuog5Tve2NFTe2t0c7pBcFtWhwOgXzksyk2W8gw2NUTFj5389JM9VIGBAUxQPr7pBo7SYAA6aMAmj7hZ7I3YYpx4INL8ms69k5nrjusMO13setot6oLKpY92wBWKhIbi97yFdVDa1gx6CQEVwAtvchh5R4oP3m0_EYw4eqg12G_8Gi_Ui51sEeiJeL-1PHhGBl07lWizhFZswpD1U9Yjf7slNvH9mbxc6fvWZXgHMGd7KPboeJ8hAkwcD3T9dbJ711vWuXvtzwtTOwsODwmr3DF_YkXPTfJGeUQMXFHtF3Vn3LmmoTousgVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KO8BvbYN1BkblQq-xp9r7t-89Sv6oAN4j00aTFILXJrA9Behp69Oga2nBDBrDs68S0DR0842-cCNE7DxJbe3z8rl1j3QsdDim5pdc_DzyoCne1CPTWK-0Sf0xFr6ubCCeK7ICR6sR-6pIX-1c76ZVyfgoBjrGyJzT-WZ-zLYrNuqM_Z6A1TZ8QSvs9KBWxCrNauZ5uquMr4G09wNkgkrCsj8gztYzjdrM0xj1rYWUNaeV1bampuXyHjc-_CCa6GvXf2ao-0edwzS4gTeiKf9l4y0U_rKblssCkn9r510l0Iz0u2TfB0LPJRJoMJAsEbvSphC5oaFrkXC7ciYsu7-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s3f4y7lm6SeXKL1caRmkunD0x7a2_O5UGu4v79nyGYsAqYaIfMZ-h2TQu2mBETGgAxdLQaDsxf6kHCAt6j_ALwAZ1Px1apa2md-PfdDkooig_l4VhUNI3vrFs7eZggBu89nBY_LFs0vI7_jvHj3gDPDUXbr7z0VwT0jI8cE3HbEUBh4Vb6AgpqRnB0G1PIyZpPCseLJe0Zeg2a0e-2vpblPOaxrk4mIWKxt0DC2TZbMM4vUNGb8PfHwlh6iuBpDfFF5rudihYmaowmFlHiOoWLIYuXLhMmwZlEpX9aelKOjIwYLLEf4vAjYbv-_2hMI6QfJqSkN0yvrNZkUFQO3qlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه تصاویری ساخته‌شده با هوش مصنوعی را در «تروث سوشال» منتشر کرد.
در این طرح‌های گرافیکی که با عبارت‌هایی نظیر «این نفتکش اکنون متعلق به ماست»، «خداحافظ اتاق موتور» و «دیگر موتوری در کار نیست» همراه شده‌اند، صحنه‌هایی از انهدام و آتش‌سوزی ناوها و نفتکش‌های جمهوری اسلامی ایران و حضور نمادین او به همراه نیروهای آمریکایی بر روی شناورهای توقیف‌شده شبیه‌سازی شده است.
او پیش از این نیز تصویری گرافیکی از «حمله به خارگ» منتشر کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77519" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f94T7pNKKls77hdQCUEXaVVdtKwrnTU48MUPyxCm9rmEhy8DhYuQYJzMJQg2WgHYwf7KYSrV4swKrNxEJPqchHSYS2QKxyqXg95YhhzxYw3XvIqLufWA3xbhykaX231IUsW-4AaMWcZYNmtC2w3GLDmNW8rHRy3Jg9FjCxlugIZVaz3rs4jrUz-Lrq8SZXGg-0DvVSUExaXktCVH8tgzQqgnNI2sN4GGRXvMJrNDaKS0Xo-KHrs9qDUbHJUkPrQkBbhYc2Cwrh7L5vHKmqBCkzQ4kXdgyWIaXRfoptNxeOPDbT1bfpAQV9i32vYuPoKXx4YyvIxyM33pXW7Qm_-STA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NrHAZM2LmK6y4ecLzuGjcj3ZP_Tki4li6oTfAlSLKfVTH6lENwoNjZDuDzQ2WLSTl4kIKV5Bn9lB2o2aUZjYwY0ji-UCC93_B0ShgwTb4hrOxvs48Pxgk68ARLjycWAQqdxqBLQ24AxT-e64WXTpJ00Cffi8gwxovovfwKzj45yW913_wwmVu0OnZBvJqhIUmvW5Nto3e5zIRfbEfqfpMgw_Bc5HUBbYfZ-HSfRit6gRBFu9J51uWJ60OImU4BoomjqqFTUDmrlcUv6nrs3Msq-TtnkixGMuNfVrQA9f45T1MU07myh3ktqFuV03RKI2ni2IMuY2BN2dl2STcZO_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6JT5PKrsRaihIXacNqpu26ecgd0OUwxjf3fR4KpipiZeRYKLMYcRxtKbdLobG6asq1lQU-F7vd9YFGtFJoc8FKfnuarH7tXiJeGpODMnn01SA1jj97bz3ElKQVKJTUcZ4KdFcZge-POCvxMu-wIEmNO3MmzuYXqJoPQ9LWDsW9zf9wybhcVCNuRy1QAbP0h2g7PPOgF_3C8gEZVzLmqitXrUGWEwbbeATod_FBYbHolo9oMv3rZlzv1X206dbwTrXXaot0H4YEoAJGsXFeuE2cYWuoroROXrNxlohKNz3XLWyg7PAtHi4cCYB7CcsI4pUmdtiSrf-QbD0SPjASALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nD9KdDhOBpapFgFmDtu0wnj3r8ztSFB7ZVKyfUHm1AuTZAs0agE67oOg-Yl6q36HBDw4zQKDMlA9GmzB55pXlNjW80LE-93KPoYKrXnG1acpRVzONTtTGiMviQWogoZ6EKokL2XFcCx6Muy-Cdyd-E159U3nS5_d04LsmKLZJXbKnNubzwCpTtFl7nweeXwrL5FURL71gR55veqknYaLSC_qTo9K99SySO6zzS0ynhLK9DFSrz3ehODmEfr4yl-xHUpq0aXGovQvEsJgzu0LMCUYz2cZdqGIfRKd4RA4KtIOWIJD2CFpDoELl745fqv-JGo5Nkzptcwma5Lun73S5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OvX80qKmIvOkYcBt92AzMejgOekSG5GpPTtLr1NeGIQw-yKGFze1xOmpn6PqyebtvqoYkd_Jlnjt9EtaiievTFE0D47FEXSLN3F6UEo5g6NCTV0s-zhYXTjD7ZUkk9sQt3rTJit8s_GvA8fE172ci9ldJqIPWpFK3xNIAm6O1fT_weiL9epA8rFCCgSorQGZRcpqwZLO0fTiBuzFe698eQsX6GM24t9fM2T79hGoJX5ZwXPQrATioJjDzdLIu7K4u8MUC4kbMfhsUUAxa-m1IcFhJbsi2OQ2nyUw0-zOiEZQUlr-wocBA2q4401SUpLA4xcxUGudQ_jKgon0qoJM_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حساب کاربری خود در شبکه اجتماعی «تروث سوشال» تصویری ساخته‌شده با هوش مصنوعی منتشر کرد که یک جزیره شلوغ و ویران‌شده در میان آتش و دود را نشان می‌دهد.
روی این تصویر عبارت «حمله به خارگ» درج شده بود.
ترامپ تصاویر دیگری هم منتشر کرد که با هوش مصنوعی ساخته شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77514" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcT6VzLomvjeOBUb0RSvVXoX_lwQHYGtkMKTEP3Q2mnPhv-4dxZ1mhKR5s1KgHaH4tB5gVcBNYWD0KUcNpVQLbv8uG2sPpP8OBmLU_BOzzDMLZd4uv5hYUuhg0RhvmRWrRo5l-T5ktrOBHyR-Hpg-G9p_P95fUaCOaSOkZulNxewR7mgpJR2hhNfwotDpOmmGexTDZtRDzmw7ue_Ldu3J_ZmretMjnAYYuSYL1JCYE4_9GHY4ybuu4tXVM2P6xM2eEOBOgQtpcofss2Mbjmb1w8wQW7C-CO9I1GLxYl1y7Gadm2dDKPIIruA7qIEFcGGg9n8Pvbj9Ge4nQFzb8pZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از منابع آگاه گزارش داد برد کوپر، فرمانده فرماندهی مرکزی ارتش آمریکا (سنتکام)، به دولت دونالد ترامپ توصیه کرده است کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا به اعتقاد او این عملیات به سقف اثربخشی خود رسیده است.
به گفته این منابع، کوپر ارزیابی کرده است حملات دو هفته گذشته توانایی جمهوری اسلامی برای هدف قرار دادن کشتی‌ها در منطقه تنگه هرمز را به میزان قابل توجهی کاهش داده و بیشتر اهداف تعیین‌شده برای حملات هوایی نیز از بین رفته‌اند.
منابع آگاه افزودند کوپر به مقام‌های آمریکایی گفته است در صورت تصمیم برای از سرگیری عملیات گسترده نظامی، آمریکا می‌تواند ۲۰ درصد از اهدافی را که در عملیات «خشم حماسی» هدف قرار نگرفتند، مورد حمله قرار دهد. با این حال، او تاکید کرده است اگر تصمیمی برای بازگشت به عملیات گسترده گرفته نشود، ادامه کارزار بمباران دو هفته گذشته توجیهی نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77511" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gierOCv6Vngf_zwwpsGfvhkqx_MRZo9pFLVy_Y7YQx61bK4Y4biO_EcgZyngIZHYJSj6AvP40j32uzfxm9FlZ55uDhLlol0P3w4kbfCX0OCdVDsbQE7KoScO7Q3L766gyIbvP-ZevCkbv812KQQCEi-sIO6BI6Emb9Ar6L3hSkQYqMCn2Jro3HOJGbW6509LwkrsISGVSdBerb8tT0IqR7Jx9JbDshT-Snke0vHG-APVJj7n2u-1evCMe2WhOvG_y0R7Gn-BCvw2szAWz61bRv2Nk9N0D4w-jjs-gXZBv7FEGSLehN-07E5NlvDgZj223QR0yffzoQQFgRuzwKifKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران با انتشار پیامی در شبکه اجتماعی اکس، حمله اوکراین به یک شناور «تجاری» ایرانی در دریای خزر را «نقض آشکار منشور سازمان ملل متحد» خواند و اعلام کرد این اقدام «نمی‌تواند بی‌پاسخ بماند.»
عراقچی در این پیام نوشت که ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، با حمله به یک کشتی «تجاری» ایران که به کشته شدن یک ملوان ایرانی انجامید، به گفته او «به خواست اسرائیل» تلاش کرده است اروپا را وارد جنگ کند. وزیر خارجه اسلامی افزود که در گفتگوهای تلفنی خود با کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا و سرگئی لاوروف، وزیر خارجه روسیه، تاکید کرده است که این اقدام نباید بدون پاسخ باقی بماند.
ولودیمیر زلنسکی پیش‌تر اعلام کرده بود که نیروهای اوکراینی در عملیات‌های دوربرد در دریای خزر، کشتی‌هایی را هدف قرار داده‌اند که به گفته او برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77510" target="_blank">📅 19:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpTTIJNejSK7z6Ho5QrlmZotH8632H60MyjVZPJY1V4cpZ-3LNRmf2XLMW8CKqpKgdrDZfYL8UOUwQr1BZwyeQYpHtOuLW9W9hezGpsKsdstfN2cDDvT9Krkuq_j--EYq4l-2MheSMIR51YbSKxFP7TP1jwIXFuKjrAtrmm-A2w03ZnClIKovG9jaHQMJAt5UqoQyBeS-LQmP4i2faPFY3-mZq0LO0qVn5wUg0epijNA0KhUKr_vmOZz4BsmoEdC7RnxzFmVlyu-JVgNkndNJSdnDLgCaZlpP1Vcgjxb3KKBhTgmK4aAkrdvG_Y30wr68__veNil63fr8uQ_sm1haA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، گفت درگیری با ایران زمانی پایان خواهد یافت که حکومت جمهوری اسلامی سقوط کند یا آن‌قدر تضعیف شود که برنامه هسته‌ای خود را متوقف کند.
او در گفت‌وگو با شبکه فاکس نیوز مدعی شد جمهوری اسلامی باید به این نتیجه برسد که ادامه ایجاد «آشوب اقتصادی در جهان، کشتن هزاران شهروند خود و حمله به دیگران» هزینه سنگینی دارد. نتانیاهو تاکید کرد که برنامه هسته‌ای ایران «چه با توافق و چه بدون توافق» باید پایان یابد.
نخست‌وزیر اسراییل همچنین هشدار داد اگر ایران یا گروه‌های هم‌پیمانش به اسراییل حمله کنند، با پاسخی «بسیار قاطع» روبه‌رو خواهند شد و افزود تهران در صورت انجام چنین اقدامی «اشتباه بزرگی» مرتکب خواهد شد.
نتانیاهو درباره سفر پیش روی خود به واشینگتن و دیدار با دونالد ترامپ، رییس‌جمهوری آمریکا، گفت قصد ندارد اطلاعات تازه‌ای ارایه کند، زیرا به گفته او، همکاری اطلاعاتی میان دو کشور بسیار نزدیک است. او افزود مشتاق است دیدگاه ترامپ را درباره آینده درگیری با ایران بشنود و گفت: «در بسیاری از جنبه‌ها، این تصمیم اوست.»
او همچنین اعلام کرد که «قطعا» برای شرکت در نشست مجمع عمومی سازمان ملل در ماه سپتامبر به نیویورک خواهد رفت و گفت قصد دارد از تریبون این سازمان درباره اسراییل و ایتلاف اسراییل و آمریکا سخنرانی کند.
نتانیاهو در ادامه از زهران ممدانی، شهردار نیویورک، انتقاد کرد و او را به دامن زدن به نفرت علیه یهودیان و حمایت از حماس متهم کرد.
او همچنین گفت از کاهش حمایت حزب دموکرات از اسراییل «بسیار نگران» است و مدعی شد شماری از چهره‌های اصلی این حزب تحت فشار فعالان سیاسی به مواضع جریان‌های ضد اسراییلی نزدیک شده‌اند.
نخست‌وزیر اسراییل در بخش دیگری از سخنانش از موضع دونالد ترامپ درباره عربستان سعودی حمایت کرد و گفت ترامپ به درستی تاکید کرده که در صورت عادی‌سازی روابط ریاض با اسراییل، تنها باید با یک برنامه هسته‌ای «غیرنظامی» برای عربستان موافقت شود. او افزود آخرین چیزی که اسراییل و آمریکا خواهان آن هستند، شکل‌گیری یک برنامه هسته‌ای نظامی در عربستان سعودی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77509" target="_blank">📅 19:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77508">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhXs17RQwMuTbvaVtcxNbMZ0CIAGgcY1We2cAHBTstiuQTvD_xlfaM51myeY_nLeczqOeWWSTUiTZDnkdLOHqGpdZVCro-MOy34v8Uo6dGRNEQpF-1VvNwa3olKru_QJZ6bSeR4Gzp46SVs-kE2PtNskKS235-wD4K34QSc6jt5oYk1CVcFWG28zmg8cwfnqnY7KddQj4lsqO7GrxkaxdSZG8csW0KH0LSI6tCYqeU_7afs1vtaUXPdlvZOGiteAB8v8Nks8DFvUKVheLnUV6VrXHvjcGisOH6AkhOYoVTPokiFsMcbEs23KbwTMzSqmer2A0hICC_Jh1lx_5Xg1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل، اعلام کرد که دونالد ترامپ، رئیس‌جمهور آمریکا، حملات علیه ایران را به‌طور موقت متوقف کرده تا فرصت بیشتری برای پیشبرد دیپلماسی فراهم شود.
والتز روز یکشنبه در گفت‌وگو با شبکه فاکس نیوز گفت: «او دارد به مذاکرات فرصت می‌دهد؛ کمی فضا برای پیش رفتن گفت‌وگوها فراهم کرده است.»
سخنگوی ارتش جمهوری اسلامی نیز گفته که در پی توقف حملات آمریکا، ایران نیز حمله به متحدان واشینگتن در خاورمیانه را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77508" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TklC1gYRtbE3IH3sXLOg452d0LNw7q-_VnRGP0f9oDKj0x-llPE5lMtasmybCpbEG_HvzgQcNQaEqZwgBGUpkvv-kJV3hnfRRc2wcgflIIggkTLQh3o_SqZmNXVj3rMGS5bMpg8pc_0yjh1-sLYGE813fZ35xt4xZGL6XjKc2xDv51FQcXdhHdDLD1q9ORGOsYZgtQNp8SSoBVJ8DHXN8wFsQwP1jomdkp35-exAfY3J51vDdTk3fETclHdiI0eNK8qHxOTuV4xppfKquRC51euzpp1PJz5LK5bpew_XcrLmT1HAL4SHoqSIsMbhSNzwRoBnF8R8-N3nnqHG1AWb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز یکشنبه مدعی شد که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
بنابر گزارش تسنیم، این نفتکش پس از خروج از مسیر دریانوردی مشخص‌شده از سوی ایران در این آبراه راهبردی، با مین دریایی برخورد کرده است.
بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد که اواخر خرداد بین ایران و آمریکا برای تمدید آتش‌بس امضا شد، ایران متعهد شده بود طی ۳۰ روز در تنگه هرمز مین‌روبی کند تا تردد کشتی‌ها آزاد شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77507" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E18ehsqkhEA2CVSOxUjJFqwx-GPpdOsgLJ4N8wHVcSqWcprTFCnx4LSfgHoUuWZwJ_p7vfoWI64ElzW9ncj_w-nlpoyMq0OysJUUHqX8m4lBlFB1wVZyLRb0cTEZW3qoFaaA0HxpCWqFD-XK3HyhxEVqCXsLAiOWIK0nz1IKJ9O5hbP5enrFhEjZebdtP2vIMcOmEwWVP7ifk-MwgZU1hEz_OyJyU594Hyiy-JG8DsZS139zCXCQlWZWcoPoQkzxMI-xwvPtJgNWdSFvQMe6XVU3n8AtRFRVEm2Uxz85NkcH6LsPhr6sSSbWIsUfbVDvJu9V-VZC3b4jag_3PbEdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری العربیه، روز یکشنبه چهارم مرداد ماه گزارش کرد ایالات متحده آمریکا و جمهوری اسلامی ایران پاسخ‌ خود به پیشنهاد مشترک پاکستان و قطر را که با هدف ازسرگیری مذاکرات میان دو کشور ارائه شده بود، تحویل دادند.
بر اساس این گزارش، منابع آگاه در گفتگو با العربیه تایید کرده‌اند که کشورهای قطر، مصر، پاکستان و دیگر میانجی‌گران منطقه‌ای طرح جدیدی برای برقراری یک آتش‌بس ۱۰ روزه به واشنگتن و تهران ارائه داده‌اند. این طرح با هدف ایجاد فضای مناسب جهت حل بحران در تنگه هرمز و احیای توافقات پیشین تنظیم شده است.
العربیه نوشت، این پیشنهاد دو شرط اصلی برای بازگرداندن دو طرف به مسیر گفتگو دارد که شامل توقف فوری اقدامات خصمانه و بازگشایی کامل و ایمن تنگه هرمز به روی رفت‌وآمد کشتیرانی بین‌المللی است.
بر اساس جزئیات این طرح، مقرر شده است که مسیر جنوبی دریانوردی از طریق آب‌های عمان از حملات نیروهای مسلح جمهوری اسلامی در امان بماند و مسیر شمالی از طریق آب‌های ایران نیز از محاصره دریایی آمریکا خارج شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77506" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxrLPZi6-zWMIfE07nozcfMPo6bN1_m1SXan9xoIcigjmIc67hxT8_I2JhnSDwStjEZVGPQRdqPlLwpX4RDgaghoMGoDeO_VnaxzO8OK52SKWoepRilC9cTx9ItoWT34uaM-G-Sh5ygvb8z7elV_5Ipv8q2RrLNou9rDP7fOflO2C9eSYiXqasozfXPDXvT9Ko3qXjy_yaEFRZEfLREKOzHKdiUUQfEGUCagFczgO4nMFV3dhStR5rgqMMgWpMkjS55hoXovFIwdKqvBGJfi_xsdPPezvxFaZ-W_hxmVX-DJUFHuj79SBnubrwZBBM7amxpYKJMmPAssnnXrnVvXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان اویس‌قَرَن، پژوهشگر ایرانی علوم رایانه و استاد دانشگاه واشینگتن، مدال آباکوس سال ۲۰۲۶ اتحادیه بین‌المللی ریاضیات را دریافت کرده است؛ جایزه‌ای که به دستاوردهای برجسته پژوهشگران جوان در بخش‌های ریاضی علوم رایانه تعلق می‌گیرد.
کمیته این جایزه می‌گوید اویس‌قرن با وارد کردن ابزارهایی از شاخه‌هایی چون هندسه چندجمله‌ای‌ها، نظریه احتمال و نظریه طیفی گراف‌ها، شیوه تحلیل الگوریتم‌ها را گسترش داده و برای حل چند مسئله قدیمی علوم رایانه راه‌های تازه‌ای گشوده است.
پژوهش‌های او به‌ویژه در دو زمینه مورد توجه قرار گرفته‌اند: یافتن مسیرهای نزدیک به بهینه و نمونه‌گیری تصادفی از مجموعه‌های بسیار بزرگ و پیچیده.
مدال آباکوس هر چهار سال یک‌بار اهدا می‌شود و ادامه جایزه‌ای است که تا سال ۲۰۱۸ به نام رولف نوانلینا شناخته می‌شد. نامزد دریافت آن باید در آغاز سال برگزاری کنگره جهانی ریاضی‌دانان هنوز به ۴۰ سالگی نرسیده باشد. این جایزه از مهم‌ترین افتخارات بین‌المللی در علوم رایانه نظری به شمار می‌رود.
اما اهمیت کار اویس‌قرن تنها با فهرست کردن اصطلاح‌های تخصصی روشن نمی‌شود. بخش مهمی از مسیر علمی او به یکی از مشهورترین پرسش‌های علوم رایانه بازمی‌گردد: چگونه می‌توان کوتاه‌ترین مسیر ممکن را برای سفر میان چندین شهر پیدا کرد و در پایان به نقطه آغاز بازگشت؟
این پرسش که «مسئله فروشنده دوره‌گرد» نام دارد، در ظاهر ساده است. یک فروشنده، راننده یا مأمور توزیع باید از چند شهر یا مقصد عبور کند، هر کدام را یک بار ببیند و به نقطه نخست بازگردد. با افزایش شمار مقصدها، تعداد مسیرهای ممکن چنان سریع زیاد می‌شود که بررسی همه آنها عملاً ممکن نیست.
در چنین مواردی، پژوهشگران به جای یافتن پاسخ دقیق، الگوریتمی می‌خواهند که در مدت معقول مسیری نزدیک به بهترین مسیر را پیدا کند و بتوان تضمین کرد که نتیجه آن از حد معینی بدتر نخواهد بود.
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77505" target="_blank">📅 16:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQveKJHe02lOfRfbP_pJAsUrpfpQoV3xbGk_gKvp_BiWcdba-xzWsrobRMAR56RtWYFLj2FeOqWOfpHVAl-mwwN1fPlEthyfX8OP536MsvG7UifW77fZNPEOXSHo7Hp84CobE3KUQkocl5wo_rfN9xSwUi5C66-yn35jZzOo2HWztBvpBuy_Grp1CgwLqsnnBkCdC0pvFe0-uhXVpzq3uKwM_6uEJhjDI4A3fGOU42bBdLoEBlyZAdoyElyLtK3bTeSIHFQ4D8Bos2JWNoIhHcuNJXDmZvSSr-G8FjTR-RtCAJAbWmjdr3Zc1MrQhEPKKFCwPKFWRKx6T-IZQS8WAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید
گزارش نیویورک‌تایمز
درباره کنارگذاشتن طرح تشدید عملیات نظامی علیه جمهوری اسلامی را رد کرد.
استیون چانگ، مدیر ارتباطات کاخ سفید گفت دونالد ترامپ، رئیس‌جمهوری آمریکا، همواره گفته است راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر جمهوری اسلامی به اقدامات تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همه گزینه‌ها را حفظ می‌کند.
چانگ افزود پس از تحریم‌هایی که اقتصاد جمهوری اسلامی را فلج کرده و سیزده روز پیاپی حمله به اهداف نظامی، عاقلانه است که این حکومت به سمت توافق حرکت کند. او گفت در غیر این صورت، طرف مقابل می‌داند چه اتفاقی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77504" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77503">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lj8MvM_wpqfAV3uPrxxPEtfBXx65v-0AWIlLUUkLIX8GuyeQUjtYepNAq3TGpf2W6Z2UQfPbUmFv6al7gFjZsA1ob_7-idCRUuOSLt92_bsV87s4IbIYnZNoHNkYGz9vHRI-SskKiaArryXBUApfTwCYtUeBFRdzOThmREmWGtSW66jGO-FKF2SgwzYR0koyx23FI36UtcLecQZcWQhrThwbIy-zIgGxBir48UL_xzk_M-Lpz1Lh7i93MgC7fNnnzGXeZFjpXWpXANd3SP1kXSN91B_pVytoH8nucCiKEug58k4MPLz0PdXN4pw--lA4atJ7FoHJyAfKJ3LIydysRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، روز یک‌شنبه چهارم مرداد بدون اشاره به جزئیات از «پیشرفت‌هایی» در مذاکرات و تبادل نظر تهران و مسقط خبر داد.
این مقام جمهوری اسلامی پس از آن در این باره اظهار نظر کرده است که یک هیئت عمانی که برای گفت‌وگو درباره مدیریت تنگه هرمز به تهران آمده بود شنبه عصر ایران را ترک کرد.
بقایی درباره این مذاکرات این طور توضیح داد: «روزهای جمعه و شنبه چند دور گفت‌وگو بین ایران و عمان در سطح معاونان وزرای امور خارجه در تهران برگزار شد که طی آن دو طرف در مورد اصول مشترک و سازوکارهای عملیاتی برای مدیریت تردد ایمن کشتیرانی در تنگه هرمز با رعایت حقوق حاکمیتی دو دولت ساحلی تبادل نظر کردند.»
مقام وزارت خارجه در ادامه اضافه کرده است که «در حال حاضر تغییری در وضعیت تردد در تنگه ایجاد نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77503" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77502">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vp503spqIBDJ1hX9uzh2m4WSPpEIrtKNGqFTw4cHbjs_YSI-1MvVNvA-Px6ma2X6hw_tgIazigVqeK0IWBi2m2TdMmf_zu5yXkd3_bzqm9hBNW9BVXShqxugtxYw1VHvDYm8IujjnyhOlPk6eWya-auT05S4yxOKNn9z_tB10RPEDlrvvxXJai5gL2cBUjFAuOmWYbfbVQFA__4sNm5RbaRGaFZ4paTgtTA86rtyvexYh58TpXNyVaJwYjxL5vxxNOvWPXslk2wYROjBMfOiqAfUUNnDAFBNGMj2xC3LWFIz5GtSAFLir8lf-w0k0pPHHiIb4e8u5syxzpC0bUkzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که سال گذشته دختر ۱۷ ساله خود به نام فاطمه سلطانی را مقابل آرایشگاه محل کارش در اسلامشهر با ضربات چاقو به
#قتل
رسانده بود، با حکم دادگاه کیفری تهران به هشت سال حبس و پرداخت دیه محکوم شد.
در قوانین جمهوری اسلامی ایران، مقرراتی وجود دارد که پدرانی را که مرتکب قتل فرزند خود می‌شوند، از مجازات‌های سنگین معاف می‌کند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77502" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C9VfoOCvnw8dM9PZOKEEnD5-1ZqJzv2y-qeEcCikcUXTbMZDrs0W_HL7TGf9bl1dJh69HuaNVG6d1BQz0yI4duqfokCqNsTFf69YhkdvIipFvO4lrO4dEdnDOXW0a-qJtoKGI_LBr8zSk7Y66e9d0uIU-kzGfPka3nJG4pV2jUeFnlNyXgWc17BFRjzhYD7m52ANSX3yPN-tlQXGoT9WnTRHd07lIAFR0lTtmxbdNyoz19-Y3uuVhR2nqVH46hw4xOEx_CfK0VLBbQBh_Ep62r-JraK8aqOQzcDu11wBeADIWS5icGoeI4wmgt8bvIhoZ3ZRGizyIMNkGXHLCYuaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: منابع می‌گویند ونس و کین درباره تشدید جنگ در ایران ابراز نگرانی کردند
ترجمه ماشین:
یک منبع آگاه از موضوع و یک مقام آمریکایی به سی‌ان‌ان گفتند که در حالی که دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست روز جمعه کاخ سفید احتمال تشدید جنگ در ایران را بررسی می‌کرد، جی‌دی ونس، معاون رئیس‌جمهوری، و ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، هر دو درباره این اقدام ابراز نگرانی کردند.
جمعه‌شب، پس از نزدیک به دو هفته حملات هوایی پیاپی شبانه، به نظر می‌رسید آمریکا کارزار بمباران ایران را متوقف کرده است. یک منبع در وزارت دفاع آمریکا روز شنبه به سی‌ان‌ان گفت: «عملیات فعلاً متوقف شده است.»
به گفته منابع، کین روز جمعه به‌طور مشخص درباره ذخایر مهمات آمریکا و دیگر پیامدهای منفی احتمالی ابراز نگرانی کرد. یکی از منابع گفت کین به ترامپ اعلام کرد که ارتش آمریکا می‌تواند گزینه‌های پیش روی او را اجرا کند و موفق شود، اما سپس درباره پیامدهای احتمالی آن هشدار داد.
هر دو منبع گفتند نگرانی درباره ذخایر مهمات، یکی از چندین نگرانی مطرح‌شده با ترامپ در این نشست بود. در حال حاضر مشخص نیست که آیا این نگرانی یا هشدار درباره تشدید جنگ، دلایل اصلی توقف حملات پیاپی شبانه آمریکا بوده‌اند یا اینکه این توقف ادامه خواهد یافت.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت: «با توجه به تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزهای مکرر این کشور، عاقلانه است که ایران برای دستیابی به توافقی از طریق مذاکره تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77501" target="_blank">📅 06:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNiwQM5gVkP4_x5U7eCcGeYnI62d2z-Kww7hpxCHAF2o0Cs3aAFP0NOSFxRVynoSQM_BLK8IUyBMrXk8crDSZqzEsTibE3AH7AA4QWRZlUldK97Ikxb0rGP8UA46FGkclDt3LgBeOybIOsfLifrAndoK8jcNeNWGGi2Cjwa9W63NAtvdM0d1AmbVGHVe3D117DkoM4pKfSp3kuS-cNkmqhKMuyRWclPqcXmA4rqfaaq1oYqQHnx9W-Mt9H16sg2eftBoWeslphXDOGkkFK1hueGrBUyYR4tFLD8vm6Z_9IlT1RXdKAuHikuZRBO2zjgD34raFO2xb82n2jYsQPO4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز:
ترامپ در پی ابراز نگرانی مشاوران، فعلاً از تشدید گسترده حملات علیه ایران خودداری کرد
یکی از نگرانی‌ها این است که گسترش درگیری‌ها ممکن است ذخایر کاهش‌یافته مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
ترجمه ماشین:
رئیس‌جمهوری ترامپ، دست‌کم فعلاً، برنامه‌های تشدید شدید حمله نظامی آمریکا علیه ایران را کنار گذاشته است؛ به‌ویژه به این دلیل که نگران است تشدید جنگ، ذخایر از پیش کاهش‌یافته پنتاگون از موشک‌های رهگیر ضدبالستیک پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
به گفته مقام‌های دولت، تهدید متوجه ذخایر موشک‌های رهگیر یکی از ملاحظات متعددی است که بازگشت به عملیات رزمی گسترده را به اقدامی بسیار پرخطر تبدیل کرده است. آقای ترامپ و دستیاران ارشدش همچنین از احتمال گسترش جنگ در خاورمیانه، دور شدن متحدان کلیدی در خلیج فارس که در برابر حملات ایران آسیب‌پذیرند، فشار اقتصادی جهانی و تشدید بحران‌های انرژی و پناه‌جویان نگران‌اند.
به گفته دو نفری که در جریان این گفت‌وگو قرار گرفته‌اند، تازه‌ترین چرخش در نحوه مدیریت مناقشه با ایران از سوی آقای ترامپ پس از جلسه‌ای در روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه او رخ داد.
به گفته این مقام‌ها که برای گفت‌وگو درباره مسائل عملیاتی خواستند نامشان فاش نشود، رایزنی‌های محرمانه بر کاهش ذخایر موشک‌های رهگیر پاتریوت و دیگر سامانه‌های پدافند هوایی پنتاگون متمرکز بوده است. یک مقام ارشد آمریکایی گفت جمعه گذشته، هنگامی که یک موشک بالستیک از پدافند هوایی آمریکا ــ که در حال مقابله با موجی از موشک‌ها و پهپادهای ایرانی بود ــ عبور کرد، سه سرباز آمریکایی در اردن کشته شدند.
به گفته این مقام‌ها، ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، در محافل خصوصی هشدار داده است که ازسرگیری عملیات رزمی گسترده علیه ایران امکان‌پذیر است، اما ذخایر موشک‌های رهگیر در دسترس فرماندهی مرکزی ارتش آمریکا را ــ که مسئول عملیات در خاورمیانه است ــ به‌طرز خطرناکی کاهش خواهد داد. سخنگوی ژنرال کین از اظهارنظر درباره توصیه‌هایی که او به رئیس‌جمهوری ارائه می‌کند خودداری کرد.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت رئیس‌جمهوری «همواره به‌طور ثابت گفته است که راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر ایران به فعالیت‌های تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همچنان همه گزینه‌ها را روی میز نگه می‌دارد.» او افزود پس از تحمل تحریم‌های فلج‌کننده و حملات مکرر، «عاقلانه است که ایران برای دستیابی به یک توافق مذاکره‌شده تلاش کند؛ در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
آقای ترامپ درگیر این بوده است که در جنگ نزدیک به پنج‌ماهه خود علیه ایران چگونه پیش برود و به‌طور مشخص چگونه تنگه هرمز را دوباره باز کند؛ آن هم در شرایطی که با ازسرگیری درگیری‌ها در دو هفته گذشته، قیمت بنزین بار دیگر در حال افزایش است. دیپلماسی شکست خورده و به نظر نمی‌رسد تازه‌ترین دور حملات گسترده آمریکا توانسته باشد ایران را از لحاظ نظامی بازدارد.
به گفته آن دو نفری که در جریان گفت‌وگوها قرار گرفته‌اند، در حلقه نزدیکان آقای ترامپ، افراد بسیار کمی ــ و شاید هیچ‌کس ــ معتقد بودند طرح تشدید درگیری عاقلانه است. یک مقام ارشد آمریکایی دیگر که او نیز به شرط ناشناس ماندن صحبت کرد، درباره اینکه ازسرگیری عملیات رزمی گسترده بتواند ایران را به میز مذاکره بازگرداند، ابراز تردید کرد.
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77500" target="_blank">📅 03:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=l4gNTsFC8Pqox0y24P0zfwy3Gc8SGPhZLTY_htXQsDLiQ904fInZ59RfMQ2RJ68TyI0K6OXPWPQMI0axvV9HQVxJZmObJKDEtmMmgABOBJvvaDoG81lvR8VWe5OOE_D_b3TF52MQrfupup8oXkLv6fxSyOlLXvlChUnCOuLU2VWO2nXmvKHOJu9JPO1coNR8x93NAQzbh-rLXJNqladwwvUEgFj6R2omIOy-5DyUyl2qUZINJf_JkBPyqwP_Qf0_H7TaMB4ODvyToaXq4BFDDSQCsbBs0qViOrQUy25Tvh45UcETRtnxnUqAd5JSrw2vOJImdKsDGOkSR2-1hIe0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=l4gNTsFC8Pqox0y24P0zfwy3Gc8SGPhZLTY_htXQsDLiQ904fInZ59RfMQ2RJ68TyI0K6OXPWPQMI0axvV9HQVxJZmObJKDEtmMmgABOBJvvaDoG81lvR8VWe5OOE_D_b3TF52MQrfupup8oXkLv6fxSyOlLXvlChUnCOuLU2VWO2nXmvKHOJu9JPO1coNR8x93NAQzbh-rLXJNqladwwvUEgFj6R2omIOy-5DyUyl2qUZINJf_JkBPyqwP_Qf0_H7TaMB4ODvyToaXq4BFDDSQCsbBs0qViOrQUy25Tvh45UcETRtnxnUqAd5JSrw2vOJImdKsDGOkSR2-1hIe0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین: 00:32
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است. تا ۲۵ ژوئیه، سنتکام مسیر ۱۲ کشتی تجاری را که قصد شکستن محاصره داشتند تغییر داده، ۲ کشتی را که از دستورات تبعیت نکردند از کار انداخته و برای اطمینان از تبعیت کامل، وارد ۲ کشتی شده است.
صبح امروز، نیروهای آمریکایی عملیات ورود و بازرسی برای راستی‌آزمایی را در نفتکش M/T Charminar با پرچم کومور، در دریای عرب، به پایان رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام روز ۲۴ ژوئیه، نفتکش M/T Lavine با پرچم موزامبیک را در دریای عمان از کار انداختند؛ پس از آنکه خدمه آن چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی
🇺🇸
همچنان کاملاً هوشیار، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77499" target="_blank">📅 01:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS-bYZJx-xvtUt2Z0R2ImG9CZNjqmj0FU0Y67zprtJQIey8tjOGuJAO2U7D1pVtpa504f5GQJhbGz98p8KNSkDeli8ChsJREOXdTrxaE5EWWF-pziPdZWltKVeA13_IhFeXGJIwXVKvUd_yD2yupzbBlHZLb6ZKquSKggOfVF8BVlIp5nhhe6x_rSzhY9uHz36FcNuX_gMeTjkCnAP-gIaRG84JZUPp9fq5qC_GgKrw8nsTHaTQBu_zK7IwBg4HtB1T9ySG1MR4rG1TldF0YBag8BTGQRxdq-oN9BKK8nKXvG7ODlnSL3t95Am9uZQQ1x99D7TKpPfE2UdMYmKwqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه هشدار داد که اگر دولتش به چیزی که در مذاکرات با ایران می‌خواهد نرسد، قطعا حملات گسترده به این کشور را از سرمی‌گیرد.
خبرنگار شبکه فرانسوی ال‌سی‌آی در شبکه ایکس نوشت که در گفت‌وگوی تلفنی با ترامپ از او سوال کرده که آیا در حال بررسی ازسرگیری یک جنگ گسترده علیه ایران است یا نه.
رئیس‌جمهور ایالات متحده در پاسخ گفته است: «اگر به صد درصد آنچه می‌خواهیم نرسیم، قطعاً.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77498" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ec8WUuwfuX7fulwR81Dfe8C9y3m6t9RaHgWCii6aALyqDaviYVuo2I9xuT-8xhZ5KayUDJTlEsTsQYxYkbUELl8_gKTLGv3MVGUXz8bs5wSaoiL0c_rCpqfBMhQtVhE4LMzH6mqUJ2c8P3JpI_Ps7eAGnvwvG1ZC1oCHMcXYjKVcp9MH5itc6AaX-Vz8589T20vp2kQrKcoYdwkFgn0vEEH-HEHCf8LpFcfXRanUJBBGtPso5SggvCB5ichgNtTI7UI2uMjl_acbeceanbeYMY5dC4aVeLuV-Fw3XkyNziCp733r6R3Y30SNnVv2_KkN9n4S15lmvIemsK1YNRy0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77497" target="_blank">📅 22:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJSWbr45ZiaeeDnPa9x2mfDhJI_Wrof8Sug7JL-cLiQhuMdNJ3GAe_d4QANmkqf2qgaK2ZhOHo_LG5uQsBXvJdRJg2G2TlHf_aRPbI_DR7crr6YCSOM49DiS8q-arb4howlpMzRaZcnT9GQGbiP7jZxEDseJzCxSq9Qlwd_JBkUpqjXkI8V75NKuUilhGvYR0YCJxPzQQQkoeC_aQiRmzxmOVlz75UG3SdgUJ4_2GlKi3eLx0upnNnAw_-PcRjmQZSwoptc8TYJuJz9WrDxnte6CX-L8yQZR3kaKHpTnyO_w5Pn4Q7FJth2tYjmpkrBlS29U6RPPsPHcD1GPdhLfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی پری، خواننده آمریکایی، از استفاده کاخ سفید از آهنگ «Firework» (آتش‌بازی) در ویدیویی از حمله آمریکا به اهدافی در ایران انتقاد کرد و گفت این استفاده بدون اطلاع و رضایت او انجام شده است. او افزود که از این اقدام عمیقا شوکه و خشمگین شده است.
کاخ سفید روز پنج‌شنبه ویدیویی در حساب رسمی خود در تیک‌تاک منتشر کرد که در آن بخش «boom, boom, boom» آهنگ «Firework» با تصاویری از حملات آمریکا به اهدافی در جنوب ایران هم‌زمان شده است. کاخ سفید در توضیح این ویدیو نوشت: «به ایران هشدار داده شده است.»
کیتی پری روز شنبه در شبکه ایکس نوشت: «از اینکه آهنگ "Firework" به‌عنوان موسیقی پس‌زمینه ویدیوی حملات نظامی در حساب کاربری تیک‌تاک کاخ سفید استفاده شده، عمیقا شوکه و خشمگین هستم. من این استفاده را تایید نکردم، از من اجازه‌ای خواسته نشد و به هیچ وجه آن را تایید یا حمایت نمی‌کنم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77496" target="_blank">📅 22:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fsl4-NjGf5KLIsWobAiBnGyLWvg4_aeQu9ykkFQ_HZGYskgLlGdUHbDW9yHLysTZdVcLyzytC5Gr9ZlsDWu-kFe6SBsoLnterxI4COMvBUn30KlfHVMaoYj0S7z_aBBF19g7HmLiDsAsR4WkDmpTMBdyk3deQoQMQpXNTD2Q0W8Py1iFwD8rRZNXTHRn6J9NN44g-bp25DgDiOCJmFyI4t2SgowPcnLFSvSQIdEhk3cqhXfyuQW3hSkgECKt7CKwosiieFWuqqNLTwVTVxoPVrugCtnueoZD039C1hzKgk46n6WW88vLkKngmKktHE6tC6DkWVjoF_4nOrlN8grvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ دستور داد ارتش روز جمعه در ایران حمله‌ای انجام ندهد
ترجمه ماشین:
دو منبع مطلع از این تصمیم گفتند دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه به ارتش این کشور دستور داد حملات جدیدی در ایران انجام ندهد؛ دستوری که به رشته‌ای نزدیک به دو هفته از حملات روزانه پایان داد.
چرا مهم است:
دستور رئیس‌جمهوری پس از آن صادر شد که او طی ۱۳ روز گذشته، هر روز حملات را تأیید کرده بود. هنوز مشخص نیست که دستور روز جمعه ترامپ تصمیمی یک‌باره بوده یا این وقفه ادامه خواهد یافت.
▪️
تصمیم ترامپ هم نشان‌دهنده تمایل او به فراهم‌کردن فضای بیشتر برای دیپلماسی است و هم حاکی از این ارزیابی که سطح کنونی حملات آمریکا ــ مگر با بازگشت به عملیات رزمی گسترده ــ به مرز اثربخشی خود رسیده است.
▪️
اگر ترامپ دستور ازسرگیری حملات را صادر کند، ارتش آمریکا می‌تواند در مدت نسبتاً کوتاهی برای انجام آن‌ها آماده شود.
▪️
به گفته منابع، ارتش آمریکا همچنان در حال تهیه طرح‌هایی برای بازگشت احتمالی به عملیات رزمی گسترده است، اما ترامپ هنوز دستوری برای حرکت در این مسیر صادر نکرده است.
▪️
کاخ سفید به درخواست اظهارنظر پاسخ نداد.
آنچه خبر را رقم زد: ترامپ طی دو هفته گذشته، هر بعدازظهر طرح‌های حمله ارائه‌شده از سوی ارتش را تأیید کرده و این حملات ظرف چند ساعت اجرا شده‌اند.
▪️
روز جمعه نیز طرح مشابهی در اختیار ترامپ قرار گرفت، اما او با آن موافقت نکرد. در عوض، به گفته منابع، به ارتش دستور داد حمله‌ای انجام ندهد.
▪️
اندکی پس از صدور این دستور در روز جمعه، ترامپ به خبرنگاران در کاخ سفید گفت که می‌تواند حملات را ادامه دهد یا حتی آن‌ها را تشدید کند؛ از جمله با «نابود کردن هرچه آن‌ها دارند».
▪️
اما او روشن کرد که به نظرش «راهبرد هوشمندانه‌تر» این است که با ایران «به توافق برسد».
▪️
ترامپ گفت: «همین حالا با [ایرانی‌ها] در حال گفت‌وگو هستیم. فکر می‌کنم با گذشت هر روز، جدی‌تر و جدی‌تر می‌شوند. ما کاملاً مسلح و آماده‌ایم، اما در حال گفت‌وگو با آن‌ها هستیم.»
▪️
ترامپ بعدتر در روز جمعه، در سخنانش در شام انجمن خبرنگاران کاخ سفید، گفت تصور نمی‌کند ایران در حال حاضر آماده توافق باشد، «اما من آماده‌ام گوش کنم».
وضعیت کنونی:
دستور ترامپ برای توقف حملات، چند ساعت پس از آن صادر شد که یک هیئت عمانی روز جمعه برای گفت‌وگو درباره ترتیبات جدیدی به‌منظور بازگشایی تنگه هرمز وارد تهران شد.
▪️
دو منبع منطقه‌ای مطلع از مذاکرات گفتند در گفت‌وگوها پیشرفت حاصل شده و ممکن است توافقی میان عمان و ایران در تعطیلات آخر هفته به دست آید.
▪️
پس از آن، رئیس‌جمهوری ترامپ باید تصمیم بگیرد که آیا توافق پیشنهادی را می‌پذیرد یا نه.
axios
:باراک راوید
تصمیم ترامپ هم نشان‌دهنده تمایل او به دادن فرصت بیشتر به دیپلماسی است و هم حاکی از این درک که — مگر با بازگشت به عملیات رزمی گسترده — سطح کنونی حملات آمریکا به نهایت اثربخشی خود رسیده است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77495" target="_blank">📅 20:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=obogmCdFKHI8671UnB_Ai-dDZZxoFE4dTEZPztwHZlWr3EfGjmatYl5mTyWCKzMCaSDGL9vDu1oiQRknmUx7Jg0AmGKWh1mP4Tf19GlyMUQ6aHLUiENrgQDbUzVBiOI3rHHJeKRxa1-1PrFwZad2_0xnTsBOxD2kQib5RCtp_MeVD16e_d8BfZQ0g92NIsauNLpCObhnDn2VvQJGQmiPV6FwAdoBV4RSmNaAg1Rbn4MZ-zP09ucdpTrfjinwLla2Fu7zxdqZMoh3khh45xI6xpaF779e8qLKp-R7NnDBswsg5WPOHVOE4bCBR1zC0mInBXO4v2bZHsz5_sw65p5c5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=obogmCdFKHI8671UnB_Ai-dDZZxoFE4dTEZPztwHZlWr3EfGjmatYl5mTyWCKzMCaSDGL9vDu1oiQRknmUx7Jg0AmGKWh1mP4Tf19GlyMUQ6aHLUiENrgQDbUzVBiOI3rHHJeKRxa1-1PrFwZad2_0xnTsBOxD2kQib5RCtp_MeVD16e_d8BfZQ0g92NIsauNLpCObhnDn2VvQJGQmiPV6FwAdoBV4RSmNaAg1Rbn4MZ-zP09ucdpTrfjinwLla2Fu7zxdqZMoh3khh45xI6xpaF779e8qLKp-R7NnDBswsg5WPOHVOE4bCBR1zC0mInBXO4v2bZHsz5_sw65p5c5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: تغییر در قیمت یا سهمیه بنزین قطعی است
سخنگوی دولت مسعود پزشکیان اعلام کرد که تغییر در قیمت یا سهمیه بنزین قطعی است و دولت برای مدیریت مصرف این سوخت ناچار به اتخاذ راهکارهای جدید خواهد بود.
فاطمه مهاجرانی گفت دولت همچنان برای بنزین یارانه پرداخت می‌کند، اما با توجه به ضرورت ایجاد تعادل در مصرف، تصمیم‌گیری درباره نحوه عرضه این سوخت اجتناب‌ناپذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77494" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxaIa9SB00MjhYAJLrXqvz1SiqbYfUZrhuULtcJIEfHCM0BT2utPVtrAwRxaJmNN68uZqz42fLiKCjSAHi9sQ0kNsYBfn7ZvNF2kSYwiudpcXH4-GIScBC_G1SXLt_hbI1Vv9b3VAMMr6Ic_FIkZD5YoCAdu5N6EgL2Ky9ZZlvL8UCYU0LuM84NZ8GjvlbwSeW4sB_EJB0CIfw4sOsR5GPkSCaK_AuTq9bEASMkNRQcIUIW5paXFn5U472jn2w2HKN2MMKeYEEuuFmaA76CDI1O5nEjPgY3vVa41ZBX41mqizyImjx5NaqZ7NjdMdTxepHXWXmBLP-yZj7Nc3QWcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت خبری وای‌نت گزارش داد مقام‌های اسرائیلی برآورد کرده بودند حمله گسترده آمریکا به ایران، که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود در حال بررسی آن است، شب جمعه تا بامداد شنبه آغاز شود، اما با پایان روز جمعه به این نتیجه رسیدند که ترامپ فعلا حمله را متوقف کرده و فرصت دیگری به تهران داده است.
بر اساس این گزارش، در پشت صحنه، قطر و عمان فشار قابل‌توجهی بر جمهوری اسلامی وارد کردند تا مواضع خود را نرم‌تر کند و از وقوع آنچه یک عملیات گسترده و تقریبا قطعی آمریکا به نظر می‌رسید، جلوگیری شود.
این گزارش افزود مقام‌های اسرائیلی همچنان معتقدند تفاهم میان تهران و واشینگتن عملا از بین رفته و احتمال دستیابی به توافقی دائمی که حکومت ایران را وادار به پذیرش خواسته‌های آمریکا کند، نزدیک به صفر است.
بر اساس این گزارش، از نگاه اسرائیل، فرصت تازه‌ای که ترامپ در اختیار تهران قرار داده، تنها به جمهوری اسلامی امکان می‌دهد برای مدت کوتاهی زمان بخرد و تغییری در ارزیابی کلی اسرائیل ایجاد نمی‌کند.
@
VahidOOnLine
🔄
باراک راوید:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشدند، بلکه برای حمله‌ای دقیقاً هم‌اندازه حملاتی آماده شدند که طی دو هفته گذشته هر شب انجام می‌شد.
BarakRavid
رسانه‌های جمهوری اسلامی درباره این توییت نوشتند اکسیوس خبر «رسانه‌های عبری» رو رد کرد ولی باراک راوید خودش هم اسرائیلیه و علاوه بر اکسیوس خبرنگار واشنگتن شبکه ۱۲ اسرائیله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77493" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRrTUn9qzuDIziOdOtg03ozm8snP8Nn7Ff71xNXOugmW8N0u6ioIip5vYxvFGUkGx54c2ECFs0ORLlZnOKV538a9pTxcoQZsXRYOOgj8n-bPW_0uXC3k-WrJoigt5BfiyCvxROgu-yRsx7s8a6MUm5GQu7XF-JM6r9Z9A34BcH_iV-UVBEJ53PX61B6ym7tjZp4VI59uc7sGJgzSwznUiHtixCMZJ06zIyZYT3myDNe35Dk7Lmzj7DylLmfdWh4xVuOJpznX6KJenVYh51U8GCmcy0Gb0l0bDal3BN4DtBe0q5wRqrhHQzyNAH3DN0a7-UjAkcmj60-NqgySFSZilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.
زلنسکی روز شنبه، سوم مرداد، در پیامی در شبکه ایکس نوشت که اوکراین در حملات دوربرد شب گذشته در دریای خزر به نتایجی «بسیار خوب» رسیده است. به گفته او، در میان اهداف این عملیات، کشتی‌هایی نیز بوده‌اند که «با مشارکت ایران» برای انتقال محموله‌های نظامی استفاده می‌شدند. رییس‌جمهور اوکراین اطلاعات دقیق‌تری درباره هویت ناو جنگی یا کشتی‌های هدف قرارگرفته منتشر نکرد.
سرویس امنیتی اوکراین (اس‌بی‌یو) نیز همان روز گزارش داد پهپادهای اوکراینی سکوی نفتی «فیلانوفسکی»، متعلق به شرکت روسی لوک‌اویل واقع در دریای خزر، را هدف گرفته‌اند. بر اساس اعلام این نهاد، دو کشتی باری با نام‌های «پورت اولیا ۲» و «بگی» نیز در همین عملیات مورد اصابت قرار گرفتند؛ کشتی‌هایی که به گفته سرویس امنیتی اوکراین در انتقال محموله‌های نظامی میان روسیه و ایران نقش داشته‌اند.
تا کنون نه مسکو و نه تهران واکنشی به این ادعاها نشان نداده‌اند و گزارش‌های اوکراین نیز به صورت مستقل تایید نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77492" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=nLP5DD2g5KKW8f_fdUSVi6dMAzivn0-RJd3icagjbHndnoXWQ2I9upSY9K-iXX0LjnowVv81t9QcVZa_fJBT-Dk_3rBZ3sgZ1kOOvschkXjLMfoUFg7JKyY3sDOIgTpupWgyuSWmC5DbsGdhYRJk4sZs2247VA32MFpmjM_osNVf9JeYWamCn5Sa-PwsLbpbzISZJVldr1nXWxWA8RpuqBmSXaD8yCsr2zq8sTzBHceRUxqGQUYnEcCYDdkm70f5fs5fQvxkOh22xD9NaaDetK9luvaLisETSSNYmMGBuUj6G5x8yXkxc5WMaIXzca0tOkdhyGH8XRE3sn4Hkuaudg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=nLP5DD2g5KKW8f_fdUSVi6dMAzivn0-RJd3icagjbHndnoXWQ2I9upSY9K-iXX0LjnowVv81t9QcVZa_fJBT-Dk_3rBZ3sgZ1kOOvschkXjLMfoUFg7JKyY3sDOIgTpupWgyuSWmC5DbsGdhYRJk4sZs2247VA32MFpmjM_osNVf9JeYWamCn5Sa-PwsLbpbzISZJVldr1nXWxWA8RpuqBmSXaD8yCsr2zq8sTzBHceRUxqGQUYnEcCYDdkm70f5fs5fQvxkOh22xD9NaaDetK9luvaLisETSSNYmMGBuUj6G5x8yXkxc5WMaIXzca0tOkdhyGH8XRE3sn4Hkuaudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید، بخش‌هایی مربوط به ایران، ترجمه ماشین:
... آن‌ها پرسیدند: «می‌مانی؟»
گفتم: «بله، می‌مانم. یعنی، فکر کنم بمانم.»
اصلاً چه کار دیگری دارم که بکنم؟ ایران را دارم؛ این را دارم، آن را دارم. همهٔ این‌ها هم فوق‌العاده خوب پیش می‌رود. اخبار جعلی را باور نکنید.
پیش‌تر داشتیم صحبت می‌کردیم. گفتم: «ما ایران را به‌شدت هدف قرار داده‌ایم. نیروی دریایی‌شان از بین رفته؛ نیروی هوایی‌شان هم از بین رفته است. ۲۵۰ جنگنده دیگر وجود ندارند. ۱۵۹ قایق؛ قایق‌های خوبی بودند.
در واقع گفتم: چرا آن‌ها را برای خودمان نگه نداشتیم؟ می‌توانستیم از آن‌ها استفاده کنیم. اما هر ۱۵۹ قایق در ته دریا هستند.
آن‌ها هیچ راداری ندارند. برخلاف آنچه می‌بینید، پهپادهای بسیار کمی برایشان باقی مانده است. هر از گاهی چیزهایی را به نمایش می‌گذارند، اما چیز زیادی برایشان باقی نمانده است.
ضمناً همین حالا با ما در حال گفت‌وگو هستند. آن‌ها خیلی دوست دارند توافقی انجام دهند. فکر نمی‌کنم هنوز آماده‌اش باشند. فکر نمی‌کنم هنوز وقتش رسیده باشد، اما حاضرم گوش کنم.
ولی آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. نمی‌خواهیم واشینگتن دی‌سی، هیچ‌یک از شهرهایمان، اسرائیل یا، صادقانه بگویم، خاورمیانه با یک سلاح هسته‌ای نابود شود؛ چون من قدرت سلاح‌های هسته‌ای را می‌دانم. آن را می‌بینم؛ اجازه دارم آن را ببینم. نخواهیم گذاشت چنین اتفاقی بیفتد.
بنابراین، همهٔ این ماجرا دربارهٔ این است که نخواهیم گذاشت آن‌ها سلاح هسته‌ای داشته باشند.»
[تشویق حضار]
«و اگر آن را داشتند، از آن استفاده می‌کردند. اگر داشتند، استفاده می‌کردند.»
---
ما دستاوردهای بسیار فراوانی داریم که رسانه‌ها هیچ‌وقت درباره‌شان حرف نمی‌زنند.
برای مثال، در دولت من، رژیمی قدرتمند که زمانی هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شده است. رهبران سابقش برکنار شده‌اند و اکنون دیکتاتوری همجنس‌گرا آن را اداره می‌کند که با اختلافات داخلی روبه‌روست.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 490K · <a href="https://t.me/VahidOnline/77491" target="_blank">📅 06:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=fVwAh7WdDAniDHDOZflKsggoDCN0IvHkYU84l3zn4OURhQu-DqfByGwZHF20YI52CNI8gDMKua9LikJ80isVJQ9FxsoOwf7Pzy8ApnJg3DBlMNiNlfPlG4dDql-kwPUihPDhnJiWTGBmRbqqqprGE2ydDkc6tuqhT-K_4-jO-wnHiUdc3710pfKxVl2C8_55qvRnHdUz1KqoQ-VZ64-Ukgxs8se03EDtHHgTjkaxSMhSJgLbFrpEzsyotuO4yAozv9yTYLJWcrqEYY1iVg8wGtYTgocoVpZeMj47EsSU80O9mGrxtNiIb0XkmP23RL1DOHuEX_cDLJb1KEmzPFnLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=fVwAh7WdDAniDHDOZflKsggoDCN0IvHkYU84l3zn4OURhQu-DqfByGwZHF20YI52CNI8gDMKua9LikJ80isVJQ9FxsoOwf7Pzy8ApnJg3DBlMNiNlfPlG4dDql-kwPUihPDhnJiWTGBmRbqqqprGE2ydDkc6tuqhT-K_4-jO-wnHiUdc3710pfKxVl2C8_55qvRnHdUz1KqoQ-VZ64-Ukgxs8se03EDtHHgTjkaxSMhSJgLbFrpEzsyotuO4yAozv9yTYLJWcrqEYY1iVg8wGtYTgocoVpZeMj47EsSU80O9mGrxtNiIb0XkmP23RL1DOHuEX_cDLJb1KEmzPFnLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم شی‌هی، سناتور آمریکایی [و افسر سابق یگان ویژه نیروی دریایی]، با انتقاد شدید از اقدامات جمهوری اسلامی، حکومت ایران را «گروهی افراطی و تروریست» خواند که ۴۷ سال است کشور را تصرف کرده و ایدئولوژی نفرت‌انگیز خود را گسترش می‌دهند.
او گفت: این رژیمی که با آن می‌جنگیم، اهمیتی به سیاست‌های حزبی یا اینکه به چه کسی رای داده‌اید نمی‌دهد. آنها می‌خواهند همه ما را بکشند. ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
این سناتور آمریکایی در ادامه تصریح کرد که حملات موشکی پراکنده یا تحرکات قایق‌ها در تنگه هرمز نشانه قدرت نظامی نیست، بلکه «دست‌وپازدن‌های یک امپراتوری در حال سقوط» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77490" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77489">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fCbKce81_Vex3BTyzHvPXfDiIReZmEkru30tozIpVTzCSYh6xYHRs9dJxR8xyZhhNFW_aYD1C4CXIpv9QzfAE9aIbm0ihpOqVjG_8TR97d5fQ9x_OhC0RZrsBACTQqja-xBAvVqgN1ClpWgMDt0Ley_qz03K7jxJocVwdSjmKx09Za4ZyF38LcZVuy7PPZsyL7cm7BsTTW-8KXHBcGA9CTVN3ZPwHJwqjIxkISaNTwB-4EidFW5u1cTd7F19CoIA6BNC5vw-UV_oNnUhASTvpAqnHB4t2ulAHWgZrG57oiHu1BZ1niMb1nyVsZxvfaALp3_vsZ7DkTVBUaWwrGtrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت فرانسه در تهران با انتشار پیامی در حساب ایکس ادعای روزنامه انگلیسی‌زبان «تهران‌تایمز» مبنی بر برگزاری جلسه محرمانه دیپلمات‌های اروپایی و آسیایی در اقامتگاه سفیر فرانسه را به‌شدت تکذیب کرد و آن را کنایه‌آمیز پاسخ داد.
تهران‌تایمز پیش‌تر مدعی شده بود که در ۲۰ ژوئیه، نشستی با حضور سفرای چند کشور اروپایی، ژاپن، کره جنوبی و نیوزیلند در اقامتگاه سفیر فرانسه برگزار شده که در آن موضوع خروج دیپلمات‌های بریتانیایی و هماهنگی برای فشار سیاسی بر ایران مطرح شده است؛ اما سفارت فرانسه با رد کامل این ادعا خطاب به «خبرنگاران تهران‌تایمز» نوشت:
"به خبرنگاران محترم روزنامه تهران تایمز، دفعه بعد، لطفاً اطلاعات خود را با دوستان‌تان در سرویس‌های اطلاعاتی ایران که حدود ده دوربین برای نظارت بر سفارت فرانسه دارند، بررسی کنید. متاسفانه، هیچ مراسمی در سفارت ما در تاریخ ۲۰ جولای برگزار نشد !"
FranceenIran
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77489" target="_blank">📅 03:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DkUl83dg4X5HzgoIJke5X0lw59g6x-uIDhe2s4RexiviYFM_yY6gQPGLymT169SKCafMkCmr1CuWbR9t7GL5KVAT67bHxkOOQZpj6WUV8HYAa8Vez3KWWv0x-ydpB2ato-st_ogYG9nBz6m64zzunnmTmRkzrl5idOP_fOLHSEQwNQabJFoG8SwVgU7kgi3QYZU54wONd_c-hZzkr5WE-r32UrjQcAeAORF39E-zOsIgDnQKpS9Dj9TteeUJoaA3Fy26z7lDnPM76W78OFDbrWm2AKgTHIog3iTPeFhoyedLvs0wkOSxcUzYK9hhcqAXSm44IKGw_ZQjNJXBkqXlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریم خان، دادستان ارشد دیوان کیفری بین‌المللی، در پی تحقیقات دربارهٔ اتهام «سوءرفتار جنسی» از سمت خود تعلیق شد.
نهاد ناظر بر دیوان کیفری بین‌المللی شامگاه دوشنبه ۱۸ خرداد ضمن اعلام این خبر افزود تصمیم به تعلیق کریم خان پس از آن اتخاذ شد که روند رسیدگی انضباطی به اتهام «سوءرفتار جنسی» در پروندهٔ او به مرحلهٔ نتیجه‌گیری رسید.
کریم خان، وکیل برجسته بریتانیایی، بارها این اتهام‌ها را که نخستین‌بار در سال ۲۰۲۴ مطرح شد، رد کرده است.
نهاد ناظر بر دیوان کیفری بین‌المللی می‌گوید کمیتهٔ اجرایی این نهاد رأی داده است پرونده خان به نشست ویژه کشورهای عضو ارجاع شود تا آن‌ها دربارهٔ آینده حرفه‌ای او تصمیم‌گیری کنند.
کمیتهٔ متشکل از نمایندگان ۲۱ کشور عضو دیوان با اکثریت لازم به این نتیجه رسیده که خان در ارتباط با اتهام‌های سوءرفتار جنسی مرتکب «تخلف جدی» شده است.
این اتهام‌ها از سوی زنی مطرح شده که در مقر دیوان در شهر لاهه برای خان کار می‌کرد.
طرح این ادعاها در سال ۲۰۲۴ باعث آشفتگی و بحران در دورهٔ مدیریت او بر بخش دادستانی دیوان شد.
تصمیم ارجاع پرونده به ۱۲۵ کشور عضو دیوان اقدامی بی‌سابقه در تاریخ این نهاد قضایی بین‌المللی محسوب می‌شود و می‌تواند در نهایت به رأی‌گیری دربارهٔ برکناری دادستان از سمتش منجر شود.
نهاد حاکم بر دیوان در بیانیه‌ای تأکید کرد که تعلیق کریم خان «به معنای تعیین نتیجهٔ نهایی پرونده نیست».
خان پیش‌تر نیز به‌طور موقت از مدیریت بخشی از دیوان که مسئول تحقیق و پیگرد افراد متهم به جنایات بین‌المللی است، کنار رفته بود.
در این بیانیه آمده است که کمیتهٔ اجرایی تصمیم خود را بر اساس گزارش یک نهاد نظارتی سازمان ملل، نظر هیئتی از کارشناسان قضایی و همچنین لوایح کتبی ارائه‌شده از سوی خان و فرد شاکی اتخاذ کرده است.
این رأی تازه‌ترین تحول در روندی است که نزدیک به دو سال دیوان کیفری بین‌المللی را درگیر کرده است.
@
VahidHeadline
کریم خان ۵۶ ساله که به دنبال بازداشت بنیامین نتانیاهو، نخست وزیر اسرائيل بود، به سوءرفتار جنسی با یک دستیار زن متهم شده است.
پیشتر آسوشیتدپرس در مجموعه‌ای از گزارش‌ها به اتهامات جنسی علیه کریم خان پرداخته بود، اتهاماتی که خان آن‌ها را رد کرده است.
طبق اسنادی که آسوشیتدپرس دیده است، خان با دستیارش وارد رابطه جنسی شد و سپس تلاش کرد مانع پیگیری ادعاهای حقوقی او شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77488" target="_blank">📅 02:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nb2TLhq_S6bL_n6kyuwsuVf7CNXRNl2HGSPEvVNa1EA23mcCiOUpY3uhis0vCt0XlAtRAR70vqb4eNvGjlHIGyt6nXLoSk7tFtzuujW4_yyUxrbjMSOzw-nOHGB37T6ZG5GcCpeFuTUsS-SREwvX1MbO7qFaBYV4C4pGFzjfbMS5ZFP5Vz_MExKOGLr4k3wZJ5vHjQVfkQUBY_epzUv_gVeL6OeaPkr2wr20Av7utxVL_j6hZTx8pHi1GSu9uoODRmBdrynlrS3Yk275M9wtebOW-nQXJydfT7rJJWBZHdqO4aCTR4Uo2pSa6mmJVpTrQw2NkUkflS-6deRJzC99VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مشترک نیروهای ائتلاف، جمعه‌شب، با انتشار بیانیه‌ای اعلام کرد که در پاسخ به اقدامات «بزدلانه و شتاب‌زده» شبه‌نظامیان حوثی در هدف قرار دادن کشتی‌های تجاری در دریای سرخ، عملیات نظامی متناسبی را علیه اهداف نظامی مشروع این گروه در استان الحدیده اجرا کرده است.
ترکی المالکی، سخنگوی رسمی ائتلاف، با تاکید بر اینکه عملیات پاسخ نظامی طبق قوانین بین‌المللی و با تحقق کامل اهداف عملیاتی به پایان رسیده، تصریح کرد: «بندر الحدیده هدف قرار نگرفته و تمامی بنادر یمن از جمله الحدیده، راس‌عیسی و الصلیف برای کشتیرانی، ورود کمک‌های غذایی و سوخت باز هستند.»
او همچنین افزود عربستان سعودی همواره در کنار ملت و دولت یمن باقی خواهد ماند و هشدار داد که در صورت تداوم اقدامات خصمانه حوثی‌ها، فرماندهی ائتلاف برای حفاظت از کشتی‌ها و منافع ملی «بدون هیچ‌گونه اغماضی» مجددا دست به اقدام خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77487" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWlcTXhuwldPRGHIj3tD6hH6lhbyuk9Pq_jQ51CYk6VKmDMj1cxi-h0kok76gEYb5tBsiP94LDLiR-82gcmjHDEYMzFSa3LS0JqnGc35SFDA3AmAcAxzVHiMHh769vq4yUjTKBNdZLqyOWL8oYXs7QayToiTE_ST-yXFH8ASs-A3wVnQXLAVzZjAShbQpsLa9Y9TxG9SOyUM4pn6mmjLoyCGHzTBn8zHw-PveiQnWgmsnwnVy5M0jb_DcWfo4zVisO-BrgPP2QQQjH_As7P5mp19xRE9U31lnvA1H8f5otCW7i1sR4YAdsGoUDYeFcfzkfR1DS8cLXMJ2kvJwLjOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
اربیل، عراق (خبرگزاری آسوشیتدپرس) - ارتش آمریکا روز جمعه اعلام کرد که به یک کشتی تجاری دیگر که سعی در نقض محاصره بنادر ایران داشت، شلیک کرده است....
...
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، به خبرگزاری آسوشیتدپرس گفت که نیروهای آمریکایی کشتی M/T Lavine را در خلیج عمان پس از آنکه کشتی حداقل چهار بار تلاش کرد از محاصره عبور کند، از کار انداختند.
هاوکینز تأکید کرد که به خدمه کشتی هشدار داده شده بود و آنها از دستورات پیروی نکردند.
سپس ارتش به موتورخانه آن شلیک کرد.
این دومین کشتی تجاری است که از زمان اعمال مجدد محاصره توسط ارتش از کار افتاده است.
فرماندهی مرکزی ایالات متحده اعلام کرد که 12 کشتی را نیز تغییر مسیر داده است.
....
apnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77486" target="_blank">📅 01:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین
متن زیرنویس ویدیوی بالا
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه دوم مردادماه در کاخ سفید به خبرنگاران گفت به‌نظر او جمهوری اسلامی ایران در جریان مذاکرات با واشنگتن «هر روز جدی‌تر» می‌شود، هرچند تاکید کرد نتیجه این گفتگوها هنوز قطعی نیست.
او با اشاره به اینکه مسیر مذاکره را ترجیح می‌دهد افزود: «دو راه وجود دارد؛ یکی را عاقلانه‌تر می‌دانم، اما راه دیگر احتمالا ساده‌تر است.»
رئیس‌جمهوری آمریکا با اشاره به حضور مقام‌هایی چون جی‌دی ونس و مارکو روبیو در روند مذاکرات، گفت موضوع اصلی «پیچیده نیست» و تأکید کرد که ایران «نباید به سلاح هسته‌ای دست پیدا کند.»
ترامپ همچنین مدعی شد در صورت شکست مذاکرات، آمریکا می‌تواند اقدامات خود را «به سطح بسیار بالاتری» برساند و افزود تهران در شرایطی قرار دارد که «عملاً مجبور به توافق» است.
او در عین حال گفت عجله‌ای برای رسیدن به نتیجه ندارد و تأکید کرد که باید این روند «به‌درستی» پیش برود.
@
VahidOOnLine
گفت که به سخنان شی جین‌پینگ، رئیس‌جمهوری چین، و ولادیمیر پوتین، رئیس‌جمهوری روسیه، مبنی بر ارائه نکردن کمک و فروش سلاح به ایران اعتماد دارد.
این اظهارات در حالی مطرح شد که پیش‌تر پیت هگست، وزیر جنگ آمریکا، در نشست پرسش‌وپاسخ سنا گفته بود چین و روسیه در سطوح مختلف در حال «تسهیل» اقدامات جمهوری اسلامی هستند. با این حال، ترامپ به خبرنگاران اعلام کرد که رهبران هر دو کشور به او قول داده‌اند در این موضوع دخالتی نداشته باشند و افزود: «فکر می‌کنم به آن‌ها اعتماد دارم. آن‌ها نمی‌خواهند باعث ناامیدی من شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77485" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rY4sWp7mdplWkBi6erq3qLDalKIbu2JYReziJEOWtPzk6saoTUPOmGgED5YlHTWo6CORKDxN76fmMDI5l9yXd3NS3MzegmAZC8Vozcpdfskv1ol8HfETz8c-pVgJr9jC49HklT0yWD1Fva01UZ_Z1NSmfx-YdjUS4qCPfls4gCb_tmiOvTd5xWQtXYrlahik1EisPQcIDNV-RNxWbTbNpLUxz9BAulbSj-4py2DOLe5OiLN5QQ09N28-sF_0jHyGNkN5vTkbYlyCY9lS2GWMh4Z_EQLiGuPYnqewEdl6wnW6RrmtN7SQjpLCLVCKNbcCE_B710MHJtMrPWeVs7BW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون روز جمعه دوم مرداد در ۶۶ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77484" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qW4n8USeb35KqjMZnL2TcYNcGqRLRLGSwZmYK1cSet0e0QvvZG94WEhMyaL8JQUDH_IbK-c58bXRwRG4FRIHLSoBdBODbb9leCnkg4YotdNeVzc3nCoH3QMR33aMNHlBiUvlTXqKYotuHzCqVBcJXt6d5bg3u-aAjQiZbtcoPL90i0BdKOnzIN1_4X6rLD7HyFG_KE5IFqbMBaj7S8h96CUWueUU-ncQMaWwIEeLGzEpzKG2gA5rFs7ZDcZHKl-drhGflsf__EZHTb0rWz_OwXLjck0V5-3FqoN9csT4AwpDc3uy2F59rdeh8kiQE-8eXEiO7E8kgzfSsFx_fsh2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lc2UcJd21bpHQNVQYqx7VHGwOruH2FceXfjwIw6Ab-5i5UhY5lMZiov0vEzlfK6dWGMVc0ubgvbzwqHSHP_IgfNw2ECE3oxX8HngdxmgdxzlO-olrWciS0xUpldDfq-V8HZBFrRnTtdSUsQt3NVLv2umBQW2AbyIFx3VTUFNG_gASkaB0AW4klRloGdeWtks5QjuFUXLKhjjZ0fQRQws1zjhWuTJEfT1CgAVkREYsXyF4ZgODEUtDW4WicCVZE0WWB6HeG1V6CPijSW5s0XPz5BdvNQthIEGxk7T3MdTH5Zis2y5pEi9_9HW2hW5C_lZ8hZSKauZzo4N9oV0g-KX-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده روز جمعه دوم مرداد، از اعمال تحریم‌های جدید علیه ۹ شرکت و ۴ فرد مرتبط با بابک زنجانی به اتهام دور زدن تحریم‌ها خبر داد.
بر اساس بیانیه دفتر کنترل دارایی‌های خارجی (OFAC)، این تحریم‌ها فعالیت‌های وابسته به هولدینگ «دات وان» (Dot One) زنجانی در ایران و چند شرکت پشتیبان صرافی‌های ارز دیجیتال او در ترکیه و امارات را هدف قرار داده است. خزانه‌داری آمریکا اعلام کرد که زنجانی با بهره‌گیری از سبد سرمایه‌گذاری متنوع شامل خدمات مالی، تجارت دارایی‌های دیجیتال، طلا و پروژه‌های زیرساختی، اقدام به پول‌شویی و انتقال مخفیانه وجوه برای ایران کرده است.
@
VahidOOnLine
تبلیغاتی که در کانال‌های تلگرام نمایش داده میشن به خود تلگرام سفارش داده میشن و صاحبان کانال‌ها ازش بی‌خبر هستند.
دیروز ده‌ها بار
تصاویری
رو دریافت کرده بودم که نشون می‌دادند مجرمان تازه‌ای حتی از آوتار خودم برای نمایش تبلیغ‌شون در اینجا سوءاستفاده کردند. ولی من امکان جلوگیری از نمایش اون رو هم ندارم.
تبلیغات مجرمانه رو میشه با کلیک روی اون سه‌نقطه عمودی که زیر علامت ضربدر در گوشه کادر تبلیغ دیده میشه به خود تلگرام ریپورت کرد.
فقط کانالی که تا سطح پنجاه Boost شده باشه می‌تونه نمایش تبلیغات رو متوقف کنه. چیزی
نزدیک به غیرممکن
.
بوست‌های این کانال در
سطح صفر
هستند. حتی نمی‌تونم رنگ لینک‌های اینجا رو عوض کنم چه برسه به استفاده از ایموجی‌های اختصاصی.
باید هزاران نفر با اکانت پرمیوم کانال رو Boost کنند که برسه به سطح یک و بعد هزاران نفر بیشتر از افراد قبلی دوباره کانال رو بوست کنند و....
این رتبه‌بندی ربطی به تعداد دنبال‌کننده و میزان بازدیدکننده و آمارهای اینجوری نداره و فقط باید هر روز از بقیه التماس کنی که کانالت رو بوست کنند.
یعنی حتی اگر به سطح یک هم برسم باز برمی‌گردم پایین چون باید هر روز بخواهی دوباره بوست کنند.
با روحیه من سازگار نیست.
خیلی زور بزنم، برای درخواست ریپورت سوءاستفاده تبلیغاتی از عکسم می‌نویسم: ریپورت هم میشه کرد.
از این رو محکوم به سرنوشت مشخصی در این زمینه هستم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77482" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YUyO_BJ8VVB0qiuEpczxFq7N_9wXfhMokM16z3ay3_UET9JWAXr5DloqcU6fReTpz7-GnftVhBISi8OeQpPFe_sCOjll4OjeEL4fdXX0DoEgYmDOhNuXXl7dwrVZUjNWp1DVVHJvufycQLhkY7jbbttvefQzavfJ4sIRkkVMgU0kdQgrSCnw0a4NTQqgsar7LUB6jLfi0Q2XVR86KleW_p5nhkKrbLf1aM_xZf1ZxfjlEYUez_rUDJp1E2wyFh7iDA2tOLfGz88ETqWPx80Tb240iNuIHzTKKiXbdVkRG8ACePF-B9wfjjb_Op5cmny3V4Sb6ZK01Mex2Jb2ebKFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رئیس‌جمهور شی، در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت — و این اظهارات شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، حرف او را باور می‌کنم و علاوه بر این، من نیز لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین جریان دارد (روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز برقرار است)، به من گفت که به ایران سلاح نخواهد فروخت. او می‌داند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را پرداخت می‌کنند و اینکه آن سلاح‌ها چگونه توزیع می‌شوند، هیچ اطلاعی ندارم.
بنابراین، دو کشور بزرگی که مردم اغلب در ارتباط با ایران از آن‌ها نام می‌برند، به نظر من، در این موضوع مشارکت نمی‌کنند. اگر چنین می‌کردند، برایشان بسیار بد می‌شد — و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77481" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRClzuRPBerSa1ViUWrYO96g4K3L0mD4IElSLrthQ3tMOaJjkhDOBSrlVptmoNCN6issu03O4tmvkL7HLXAUbqLsAMbGimrHLeOYWPh4PTQecCWO4lziJmyUPOmMP6aVEEm2v_kGAiaX6jTpuAIy8wszN1d3Gxig1s0Hkq--Mbj2IjjUaXYK1hzX-hRPsayACpvByEUMwYMuDrhBjlI-yd37Tll3GZtJXJTZpFAfXIOrCQ-HvrCglpbA-I5gUd2RT-rbznl8eXHQ3dsGhbEEJ7IDsYEoIuaVNUy_U0lZwol_ihZH2zvO7Go7ZWYnI_y_q4soK7S3075ONaE_JZhdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای اطلاع‌رسانی دولت روز جمعه دوم مرداد، با صدور بیانیه‌ای از اقدام سازمان صداوسیما در سانسور بخشی از سخنرانی مسعود پزشکیان در روز ملی صنعت و معدن، درباره اجازه رهبر پیشین جمهوری اسلامی پیرامون مذاکرات، به‌شدت انتقاد کرد.
در این بیانیه با اشاره به سوابق مشابه، از جمله پخش نیمه‌کاره مصاحبه رئیس مجلس شورای اسلامی، سانسور سخنان رئیس قوه قضائیه و پخش نشدن مصاحبه‌های وزیر امور خارجه در طول جنگ، رفتارهای صداوسیما «گزینشی و مبتنی بر سلایق سیاسی یک جریان خاص» توصیف شده است.
شورای اطلاع‌رسانی دولت تاکید کرد این اقدامات وحدت‌شکنانه دقیقا پس از پیام رهبر جمهوری اسلامی مبنی بر لزوم «وحدت کلمه» صورت گرفته و نه تنها شایستگی این سازمان را به‌عنوان «رسانه ملی» زیر سوال می‌برد، بلکه تهدیدی برای امنیت ملی و انسجام اجتماعی محسوب می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77480" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhBA8CiggYUB8nOrsdzS3uMHRcX4u7O8K8_8qiJ2NCrn1fKb2CzjbXydPRzEhriRR9XiSQlDnMaqcuOSOZ7VrMrlmhwrO-SdBQtMFzvbahsTqB7RPAVdQ__1lT14tXIL04rOzKfgkW47Il_xFLrNdEF_l-rEffJkca_G8hX0FcQTyCBKI1gL0gxc3vnPgKMM9C3x_Maph_c5V4P59bZO4fjbjQpW5-JIYeHHUnbuhBsYRrWDYt0INhg-HjDaDptm6-yiKBXrvjjGjEIM4R39uU6ymkbn_Os5HyVQlWvyValz8dfib3vYRSCYIfktSomnXEzdOAMIgR7FRIP1aMiVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین (شاهان) علیزاده آذر، زندانی سیاسی، با اتهامات سنگینی مانند «توهین به رهبری»، «تبلیغ علیه نظام» و «سب‌النبی» به دلیل «توهین به آدم و حوا» روبه‌رو شده است. او دی سال گذشته نیز بازداشت و به «تبلیغ علیه نظام» متهم شده بود.
این شهروند ۳۸ ساله و مهندس نقشه‌بردار، با قرار وثیقه آزاد شده بود اما بار دیگر در ۱۳ تیرماه مقابل منزل خود در اسلامشهر به دست نیروهای امنیتی بازداشت و به زندان تهران بزرگ منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77479" target="_blank">📅 17:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-bc5BvxGbrjQDqxidZWbF7VaFnyUvutTgJiIFNkiVztHBXyHNXYajdXjaQk_cP9B_uKyM2upUlHA1qedGsoRIs2vd2vfPXZO-pKAtz5IYh_VETHDxIW8endgoUUepWagcvM_k1vgklm9IDTkfOA0-C2v18N-klWSWsHuxZJa1AlLXWR_DGalngwWLkce_MIHNaXzFw_-gfJXs8YNvIkwMFM8jLykkPYd5fZwQm0eO_T6lIRjarxE0oKZh8jgFl-nWTg_JCb2IQ1ceaGON7hzyWC8NbZhtbjIMJKZVMcwH_thImMWabVEPWKMeldCcGbs4jd70vqs0_a5BSg31anOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی وال‌استریت جورنال روز جمعه دوم مرداد به نقل از «منابع آگاه» نوشت که دونالد ترامپ، رئیس‌جمهور ایالات متحده، در روزهای اخیر نسبت به این‌که مذاکرات با ایران بتواند به صلحی پایدار منجر شود، بدبین‌تر شده است.
یک مقام ارشد دولت آمریکا به این روزنامه گفته که «ترامپ معتقد است تنها چیزی که ایران می‌فهمد، فشار نظامی است» و افزود او در برابر تهران در «حال و هوای انتقام» قرار دارد.
این مقام همچنین گفت رئیس‌جمهور گزینه‌های مطلوب چندانی جز ادامه حملات نمی‌بیند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77478" target="_blank">📅 17:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCtMDPD5VnnsS6Q4DcEEnsU_NYKeEnvEWH_UGfXHTrdjqE4bklnG2ly3TkTket_rV6gsGzP32q9upd_l0ns7ls0Bjay-gQRu5NTc0OtSlAcdI9yVBRkIiO8SFUhOBhoHpcdd9IKMXTAXTtlxIzP0o_IyAsBap8kPFs48IccdFgqSOflqteEToIP6cWhkpg5ICUuNSWxBOaka-WrvKOddOUpvPjlRyU5c3fucZTOd6PNC-dhqwxMa2ihpIvEmOcG6rF8Kk0606qvuBKi3ISgEo5pkpwkbOlSG9qwQVDBnImoDF3wKHcvULapSdcdALzr9n2gmgk0v4pvYgqWOYHGDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا اعلام کرد نیروهای مسلح آن برای حفاظت از کشور در برابر هر حمله‌ای آماده‌اند.
این موضع پس از آن بیان شد که سپاه پاسداران انقلاب اسلامی هشدار داد نباید به بمب‌افکن‌های آمریکایی اجازه داده شود از پایگاه‌های بریتانیایی استفاده کنند.
سپاه در بیانیه‌ای در روز پنجشنبه اعلام کرد آمریکا از پایگاه فرفورد در جنوب‌غربی انگلیس برای انجام مأموریت‌های بمباران علیه ایران استفاده کرده و افزود هر پایگاهی که برای چنین حملاتی به کار گرفته شود، هدفی مشروع خواهد بود.
اندی برنهام، نخست‌وزیر جدید بریتانیا، هفته گذشته در جریان این خبر قرار گرفت که لندن بار دیگر به توافقی با آمریکا برای استفاده از پایگاه‌های بریتانیا در چارچوب آنچه «دفاع جمعی از منطقه» خوانده می‌شود، رسیده است.
یک سخنگوی دولت بریتانیا گفت: «نیروهای مسلح ما آماده‌اند از بریتانیا در برابر هرگونه حمله‌ای، چه در داخل خاک کشور و چه خارج، محافظت کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77477" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZjYn6w-0tlOFG9gtUvbAFHyz-n6ctX-hzqgMN2i0H0Q3qy_IuAPHO4YaB8yJr4c3HU2PRKgw23TYAS9oq-fSteCNaqqO_UAklP89kf7t_xCp1s7f0Vi6B5x5g-TFDK8F0VMWOKqMIggixb9vkOBCpmAwwuI327aznNBi0NpzxWI7DtVgNkmLfXFRX5yhCut3WoU51_JaoRKW1IOUPv1ffZJpRsweec5sLAnmbk_I8JnXKMu_AoJQU3TuUKgvjSYz5o_diUiR2pKGvx5-veGt3PfYU3M1yukrAW1xkp1b5uwW1yGjVvTGvXRv6FjOYBFTILFECFRTP3lO_JoKrg1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران روز جمعه ۲مرداد۱۴۰۵ با انتشار بیانیه‌ای مدعی شد در جریان عملیات موسوم به «نصر ۲»، ساختمان باقی‌مانده مرکز داده‌های شرکت آمازون در بحرین را هدف قرار داده و منهدم کرده است.
سپاه در این بیانیه ادعا کرد مرکز داده آمازون نقش اصلی در تکمیل اطلاعات ارتش آمریکا را بر عهده داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77476" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OvXfO0hcukzmJP1irVvzworLBeAWiSaqxqP89ThWjbMwhosmtMbJHnM7MbQmrfqEZ9fM1xpKAtiWIAa3gYDWvlsnyR-YV4CHDJ1d8I98lkdmuxYh8Mjxqkx_RxlBVxVRTcfRQlp28rKqthBgaxV16mLtdlxuZGv-SEhtKW5bhjdxezFxvyqJ00vqnnkBrnP__ZV462zWsqS2WMr_HhPvBLNSQQqGmuof7KPypYLPVubu6MWsEqmWkIlcI7whVKLbKSwPyVUSxd0dhgFI6879kgh0fkM3xDfYr4xmAIZF9O0ZAw4S54U6fdtOmOATIi-vc5JHt_e5Ee--u_HDW19KoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nMDaLz9DhZNDCueus1rP7meZKknKVIx2105CUMDnoiFZ5j3QRn7KvEmbqHS2WIoVEtXroVGG3JQ1N6NMNYYZE0Kvz5Lff9KL0gPfVTsa_h9iLQVnxFaZ2ao5Be-L6qT_y2SB_7dtY0l3U72NUcZoMQXNO19A-mHzNJnGF7lLfwl-DwVXkp4yeSfiAhngd9MlyvV1rGIOTfDDAWDMOUO_LL1JVN4zU4B6K5_lPTWUnhLDsYrVnzjSzzR2tQRggua3zLTHKQ6FC6dFbMyVSvf_tau0OJo40IFY9TLf1SQ2tQyawvVuv1-AARoaZ2hXrF896E0b1Q8wT9KcpLyh5ScoPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه نیویورک‌تایمز به نقل از چند مقام ایرانی و عراقی گزارش داد که جمهوری اسلامی ایران پیشنهاد آتش‌بس از سوی دونالد ترامپ، رئیس‌جمهور آمریکا را رد کرده است.
بر اساس این گزارش، پیشنهاد یادشده در جریان سفر علی الزیدی، نخست‌وزیر عراق، به تهران به مقام‌های ایرانی داده شده بود.
آقای زیدی در جریان سفرش به ایران از جمله با مسعود پزشکیان، رئیس‌جمهور و محمدباقر قالیباف، رئیس مجلس شورای اسلامی دیدار کرده بود.
جزئیات این پیشنهاد آتش‌بس مشخص نیست اما مقامات ایرانی به نیویورک‌تایمز گفته‌اند که این تنها پیشنهادِ روی میز است و آن‌ها علاقه‌ای به توافق موقتی که مسئله کنترل تنگهٔ هرمز را حل‌نشده باقی بگذارد، ندارند.
@
VahidHeadline
دفتر نخست‌وزیر عراق گزارش روزنامه نیویورک‌تایمز مبنی بر انتقال پیشنهاد آتش‌بس آمریکا به ایران از سوی علی الزیدی، نخست‌وزیر این کشور، را تکذیب کرد.
دفتر رسانه‌ای نخست‌وزیر عراق روز جمعه دوم مرداد در بیانیه‌ای اعلام کرد ادعای مطرح‌شده در گزارش نیویورک‌تایمز «کاملاً بی‌اساس است و هیچ ارتباطی با واقعیت ندارد».
دفتر نخست‌وزیر عراق در بیانیهٔ خود مشخصاً گزارش مربوط به انتقال این پیشنهاد از سوی آقای الزیدی را رد کرده و درباره وجود یا عدم وجود پیشنهاد آتش‌بس آمریکا به ایران توضیح بیشتری نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77474" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=EeMd_qSz2ULHnHx--s1-CxIq3joUej3pmi08KJaiKC4rRgYf1JArA-WWEsQDC0HWwKEQymR6_IcyQHJZ2WBrrxtYo-vMd-JQWn8us2uB9p8cSNkprnV9nTohQN1URaZGibjvhVUcwxS4uOFvE8cIk2BeUb1pVBf-PsrAH1iI6_tXrLHeUB2IdDDmrubCX6DoX-pJcTboWVOxFJyUiUQYDuMl-q3tB8NWA5SnB-5sr86Nmazs4PqW5V-Va_i0dshfiyLh3vl64abpksryJH3uSlJbk0MiwWTWyKT3xNszmsGVRr5t5xltymPVOG-9x42jdNbnEhwP4NPO_kW0tLBOuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=EeMd_qSz2ULHnHx--s1-CxIq3joUej3pmi08KJaiKC4rRgYf1JArA-WWEsQDC0HWwKEQymR6_IcyQHJZ2WBrrxtYo-vMd-JQWn8us2uB9p8cSNkprnV9nTohQN1URaZGibjvhVUcwxS4uOFvE8cIk2BeUb1pVBf-PsrAH1iI6_tXrLHeUB2IdDDmrubCX6DoX-pJcTboWVOxFJyUiUQYDuMl-q3tB8NWA5SnB-5sr86Nmazs4PqW5V-Va_i0dshfiyLh3vl64abpksryJH3uSlJbk0MiwWTWyKT3xNszmsGVRr5t5xltymPVOG-9x42jdNbnEhwP4NPO_kW0tLBOuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار گیلان از حمله موشکی آمریکا به مقر نیروی دریایی سپاه پاسداران در زیباکنار، در صبح جمعه دوم مرداد خبر داد.
باقری گفت: «حدود ساعت ۷ و ۳۰ دقیقه صبح جمعه، بخشی از تجهیزات مستقر در این مجموعه در حمله موشکی آسیب دید.»
معاون سیاسی و امنیتی استاندار گیلان همچنین افزود بر اساس بررسی‌های اولیه، تاکنون «هیچ‌گونه گزارشی از تلفات انسانی» دریافت نشده است.
@
VahidOOnLine
مدیرکل مدیریت بحران آذربایجان‌غربی اعلام کرد حوالی ساعت ۹ صبح جمعه ۲ مردادماه، یک نقطه در شهرستان پیرانشهر هدف حمله هوایی آمریکا قرار گرفت.
پیشتر اخباری از حملات هوایی و موشکی آمریکا به اهواز، قشم، بندرعباس، تهران، امیدیه، اندیمشک، خرم‌آباد، خنداب در استان مرکزی، نایین در استان اصفهان، تفت و شیرکوه در استان یزد، فیروزآباد در استان فارس، کنارک و زیباکنار منتشر شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77473" target="_blank">📅 17:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJlPvWVU2ilDHyA5KhCSEGIXIz6Wvzhe5pVSDpf4ChBH3YCSMk42BjVX_dZ__WMVoICWhRVPhOQACtwlRgu8e28IE4ZpOj-m50xl8I9mE8ZtJW3MM9ohz7r9sd1AHOoFvJ4zmOUYRvgrJy089I35uVq3Ilz3_jBZNZB7dqS_cVSnzVp6rIpZ-dWBn5Pbzy8Lwmjwr583h4Z4YHCtbgIJg_10AyKxXWRsO1DkpUD8_1ud_R9AyJpaF3y44Mlyx9TO30Zzx2U8qZAgJww_CsFz_4O_4fzpeGqK2vrj5pDN3hnv657chG65OeKhwMBueu_GiyzkkOYWV12jQ2qG2szh-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ID4c3GWO4_oyIw2IwC2s2aB7GSF7NyvTBENI7lzXR5mRa4kY2GRmWcCPkVqFnbFezdKaF1r5Ke9KWi-qvej-nJys1CW6k2uSXP0_qFy-tScUb9EQsNa3-DK4heVwhusCwQmS7lCi3KtQHs4okuG7T2-XtehPvwkAmgeZE0a_jL_1Sj3jZXMnETXgiY1sPzPRdQEO7ouWqe34oY_VLj9aSMTSbZRoqDxSJryCDYEUqaIDP4RvHTIbAPftBjHlUAOOmtFd1n1Autb3CDQodQ_qCYPGKnHL9R0mDyXlWdA-cvGfJ01tIPr8HxUaFaSsErKXBE7elHzGDmP5xYAaKjhRIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عفو بین‌الملل روز جمعه دوم مرداد از مقام‌های جمهوری اسلامی خواست که فوراً هرگونه برنامه برای اجرای حکم اعدام بنیامین نقدی، ورزشکار، را متوقف کنند.
بنیامین نقدی ۱۳ دی‌ ۱۴۰۴ در شیراز در ارتباط با اعتراضات سراسری بازداشت و به‌مدت ۵۳ روز به‌طور قهری ناپدید شد.
رسانه‌های دولتی ایران یک روز پس از بازداشت و پیش از برگزاری دادگاه، «اعترافات» اجباری او را پخش کردند.
این ورزشکار بعداً در ۲۲ اردیبهشت امسال به اتهام «افساد فی‌الارض» به اعدام محکوم شد، با این ادعا که از کپسول آتش‌نشانی علیه نیروهای امنیتی استفاده کرده است.
عفو بین‌الملل می‌گوید که حکم اعدام برای بنیامین نقدی پس از «محاکمه‌ای به‌شدت ناعادلانه» صادر شده است.
این نهاد حقوق بشری با استناد به الگوهای پیشین مقام‌های جمهوری اسلامی ایرانی در گرفتن اعترافات اجباری «تحت شکنجه و سایر بدرفتاری‌ها»، ابراز نگرانی کرده که «اعترافات» بنیامین نقدی تحت اجبار گرفته شده باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77471" target="_blank">📅 17:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SR7UM9Idj25URj9SBpy5syjFn_mxrvnSJb5a3cH9NNUzpAI5UbBOSnfLV_1x4b6bWUGxRRJU2iNojZCLTRFptmF0gawuigPphPVHhaT4GQEHTveIHlUXkXf9SA4Z48Uiow-WfA2TWCaJhcTzrlRBOfTXHPa4C83j8QxKQvd_dQfjigvTbM66-D9HhNaN8Xujr1yrH773Iz6xKdagE9iIPJSLgoXIgo2XmeyoG6ut-cES0ANpxZNtuj-6MMXwYwHDuk8NFdQ6TrEedndjfISXLiPa4dGx05GKeqrTlmSbdQYlAiKdI16JuyqC0U0c5g3tWtpQbACVLwmTcpH_zZhIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته بود:
از این پس  خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
واکنش عراقچی، ترجمه ماشین:
مصادره دارایی‌های یک کشور دیگر برای پرداخت مطالبات نامرتبطِ آینده، بدعتی آتش‌افروزانه است.
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به یاد داشته باشند: وقتی دولت‌ها مصادره را به امری عادی تبدیل کنند، دیگر دارایی هیچ‌کس در امان نخواهد بود. هرج‌ومرجِ متعاقب آن نه زیبا خواهد بود و نه مسالمت‌آمیز.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 486K · <a href="https://t.me/VahidOnline/77470" target="_blank">📅 06:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mgATeaUozFuGxwl6LzsHvJGuww-Q2UyM4gel-Ke788sGfbkMYg_9qdbnXTej51Gp84on-lNid306zysrabEzZkXwGMZbM1u8npFfUrzw2uw6u6vb05CW3D1tpnlOpqezazGXfJRTNwPZuJJpynSkrspdj7sbluSphyMkvw6YAo9WM3ehlfUK5hNlCaOhu84lFstC7YUzzgGcmM7eYx4ZMTUdqQt1MhQ5ejIcyiNb2T3fKsOUpKdfwCqAw8p88_7vXRdAHnLz7Ff4w0TtN8WJ4LfFL9ho0SIjf5NkcVXY-7aVViHMckKI_KacotrYws7CInbdyF6VMUsh0geWft2Wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/suOOttA0ubmnvOuhlxHI5fW_fFE5WvgZhyEQHNKt_FeUqBt4CJaMQ3kEp8bfpus0QxKutKKxSibMA0TH9Ubv6nVEL0dgtWC-K5YZVHXKtHLrqcSWqEf-iKf2b5K3WVFhO2XUOKJcNTnC9qSzw4V48634S_9933zfiYSnwvmJLjPaBvU7nmzDKHNsPU9-w25eHap1NUJSmcvMfwZo4TMl232ptFxzwY1y7PrpoCUfhXAXMW-9l4u7W1lmldJdUJqpi9zMzo9hy9vkkl_NOwDAAhn9Yf4gaey0jd6HnSz1PbgLLwkQYgQxNvJjEuuT8-04uprpLoK2KHgHw-jIIL6rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X8z2oztjmCrVfAjodBRsqJqBl8AF6ojHHWOMpH0PicH5vdkFcxs6g0KU8MEHxPYgyUK3EKgdtyL9Ri51-U7f_UZYMgQIi_4h489Q2gPlevo_tV5VBnU1nTfgiNN7sQd8p4y7FXCaeM7DfTQryi_Q-Yi-wqP_HrVX1TSXjRuZho4h5FZXjMSRKfoY9EBhTBakVMeMFeObDJnCgFUrsvEn4IBralCmn5xr9liRMqIzyCFVxVnY45b1IOINFn86d3SQDHM_mX5GD78raBQlFjS7oBa1iJh_DapuV2I0ScdppVpmMS7ZY_4K80Ye1no-hp_mdxzlpNuYO3TDdgRyOkF5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nPwmSMw3RbIrCnAACTCl1SdZcw6SHKUYrNo8QWI_Eggjc2kuif7pRIfCWqi51NyXHzCfKLOXMZRg7eC-P1_40gXfnnliNWnxbXyaNbGUBoA3CmbJQcrQVLy49oncKtV6VrbHEGMNqugEUvZqAWcuh27OEWdxBexcl5NpFeeXrC98FV3CQ9hHNydIbpctbDvRi2AQ5iX94maWjohxvnIeagnx65ydPrzNog0ndr0Ue8QuYCO20pjrvhoff2FjocJs8JR_4TGPUGvwnuAF1FALznZ0bkmr1Sd7CeWtT28B49heueRuVe1JXMQYr6NdI92izLN3A6Fo9smMA9qlgiPTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dbvxdjzNkjAJ_70LqHjLdJjQOT9B6_GBcAbxeW-6p3Hlp0-FCt1TPqnWxKYSv9DEJSLljNlGdd8s06Q08EX2udxRUujWaCnKjCdHGOCwcoUQXB42f2ttBMC4Yqxlv0mbbFvQZC_MH_jyDOw2oQ6dEQldvsa9KguVU8Wvee7Kuu_4PfxxOV5k2Ue7O_mE5Lk1XBYHvs2SYZJv-4tj2_Na5_wFKOPCyMEiJ3DB1Zg3uV0rZ24jX1A29foJ0j5DvDRA-yR8EDdURlgVYBc3uVMykdPixy20zr2enG9HN9R4ym5n8yq1htuMlMyz9SXTHTyeWZPgSx4ZVVyTc2kfmzt0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iprDn5efgB_y3XMQ1XIVvcrvQi1UyBNAzcBv-UHO74itGlChMFXT1-ICII65Y8mLNQdpy_wAmzFFHAaZW4id-V-hLhw9ZGKop-86fKs2OH301fJ90yApFh7btm2DGYr3VWzhsUsimyhGDZIUwEkJruuzVCwIFKkIQLuQQfv5P1PbYqNsZpXw1cgQNIeuJ0Gu397z9HUiDXajtzaNFktgTJzj5lS1HXPnWhD0oaCyA7M0CVDmC6D04cH28TJKZWE4J8GMeTm9iQiC4OyQwMvEfkBmsXlZ-zZTVMz3zJNnMr-XtMefTrIaTIkBKF-auyHw7tf6fFebQIXIKxyfW2tH-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=py093oXMaKuodshbvyZAAxV7ogYYTavLeFFz2dXGcmEuWMDYDwG7sRzMd9IAA3gZRLm_ZJ_2SBDcuI-1xPjQkS8qZyeA6fsCADQos5VFtzE-KRr_SFZ98Q5eSZIJFGXP-JEefsJHJphLwv7W1GSgfm983YX4Hm00m1Yvl2CYE1cJRgJIqVBzTN938BIxKPsjkG_y-jlOKPfLsxOKzeqDCmin-mQ1_1UlIqjTYlmxAsVxpFA7IaF5uV62zlks5ghdg1vcmBCV_MJ6bejfI93MuEMJzhNEUIBpw9i4agrRYFkFTMjcwlCysHx9YP1y2OcrbYHUrM7WXMu3fYakRfUXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=py093oXMaKuodshbvyZAAxV7ogYYTavLeFFz2dXGcmEuWMDYDwG7sRzMd9IAA3gZRLm_ZJ_2SBDcuI-1xPjQkS8qZyeA6fsCADQos5VFtzE-KRr_SFZ98Q5eSZIJFGXP-JEefsJHJphLwv7W1GSgfm983YX4Hm00m1Yvl2CYE1cJRgJIqVBzTN938BIxKPsjkG_y-jlOKPfLsxOKzeqDCmin-mQ1_1UlIqjTYlmxAsVxpFA7IaF5uV62zlks5ghdg1vcmBCV_MJ6bejfI93MuEMJzhNEUIBpw9i4agrRYFkFTMjcwlCysHx9YP1y2OcrbYHUrM7WXMu3fYakRfUXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: پرتاب موشک از بیدگنه، خمین، نجف‌آباد، شاهین‌شهر و...
تصاویر بالا و پیام‌های دریافتی از استان تهران:
همین الان از ملارد موشک زدن
همین الان ساعت ۵:۵۲ از بیدگنه موشک زدن
سلام وحید جان همین الان موشک از رو پرند رد شد
سلام همین الان 5:51 از ملارد موشک شلیک شد
از بيدگنه موشك فرستادن الان ساعت ٥:٥٠
شلیک موشک از بیدگنه ملارد ساعت 5:50 بامداد
۵:۵۰ دقیقه از بیدگنه موشک زدن رفت بالا
سلام وحید جان از [....] بیدگنه الان موشک هوا کردند بعد جنگ ۴۰ روزه این دومیش بود
سلام وحید ما فردیسیم همین الان از سمت بیدگنه فک کنم موشک پرتاب کردن و صدای شدیدی اومد و لرزید ساعت ۵.۵۱
5.52 از کرج موشک فرستادن ردش هم تو اسمون افتاد
اشتباه نکنم از بیدگنه
وحید جان سلام.  رد موشک از سمت اندیشه  شهریار خیلی صدای مهیبی داشت همین الان ساعت  ۵.۵۲
آقا وحید سلام ساعت 05:50  از بیدگنه ملارد موشک رفت
سلام. روز خوش از بیدگنه موشک فرستادن
جمعه دوم مرداد ساعت ۵:۵۳ شلیک موشک از [...] بیدگنه واقع در ملارد به سمت جنوب غربی
🔄
وحید جان همین الان دومی هم فرستادن ساعت ۶:۰۰
سلام وحید جان همین الان موشک از رو پرند رد شد
شلیک دومین موشک پیاپی از ملارد
از ملار یکی دیگه شلیک شد  6:00
دوباره موشک زدن از ملارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77460" target="_blank">📅 05:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=ctCTLzkK9KitljIxyDAjedNbBIFE-FNFuseK9Yq5ea2lXSOd8ducpFJc-d1I364I6GXlELD9IYnge4du_6EyGPhPdjFAF_I61oSxaDNlCmXDXNb_triWx6eUG8ca3hxb6oYlVApqudrHjkCcGzUxGOMaepJz8PBIWYBzGUtrVr5qUMrDyQ3RwlHXJNa6XLQWQdg3m_gV8XgBd7mPWfe5jLAjSJzwqNPjQExWuOuWGuFtcGfgzHlWV81ql59ZS8NI_pj2guuzFUzsNi-p_F23Cg8Tnl2VHd6Jt48HCgywWQ__TW_sw1_6rifwHEEBOfZfvYo-icCJzWDYnf6Am6oS5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=ctCTLzkK9KitljIxyDAjedNbBIFE-FNFuseK9Yq5ea2lXSOd8ducpFJc-d1I364I6GXlELD9IYnge4du_6EyGPhPdjFAF_I61oSxaDNlCmXDXNb_triWx6eUG8ca3hxb6oYlVApqudrHjkCcGzUxGOMaepJz8PBIWYBzGUtrVr5qUMrDyQ3RwlHXJNa6XLQWQdg3m_gV8XgBd7mPWfe5jLAjSJzwqNPjQExWuOuWGuFtcGfgzHlWV81ql59ZS8NI_pj2guuzFUzsNi-p_F23Cg8Tnl2VHd6Jt48HCgywWQ__TW_sw1_6rifwHEEBOfZfvYo-icCJzWDYnf6Am6oS5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۹ شب ۲۳ ژوئیه به وقت شرق آمریکا [۴:۳۰ صبح به وقت تهران]، سیزدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندند.
سنتکام مراکز فرماندهی نظامی ایران، تأسیسات نگهداری پهپادها، شبکه‌های ارتباطی، سایت‌های نظارت ساحلی و توانمندی‌های دریایی را هدف قرار داد تا تهدید ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از تنگه هرمز را بیش از پیش کاهش دهد.
این آبراه بین‌المللی، با وجود حملات اخیر سپاه پاسداران انقلاب اسلامی ایران، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با پشتیبانی نظامی ایالات متحده همچنان آزادانه در این تنگه تردد می‌کنند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه در حال فعالیت هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77459" target="_blank">📅 04:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان همین الان صدای انفجار خرمشهر
درود خرمشهر صدای انفجار ۴:۴۰
خرمشهرو زدن
سلام وحید خرمشهرو همین الان یه موشک زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77458" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان یزد صدای انفجار اومد
سلام یزد رو الان زدن
یزد یه صدا انفجار اومد ساعت ۴/۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77457" target="_blank">📅 04:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">چند پیام دریافتی از فیروزآباد در استان فارس:
سلام فیروزابادو هم ساعت ۳:۴۵ زدن
صدا اومد فیروز آباد فارس خونمون لرزید
نزدیکی فیروزآباد فارس چیزی شبیه انفجار رخ داد و موجش بد جور گرفت مارو
الان صدای انفجار فیروزاباد
ساعت ۴ صبح
انفجار مهیب
سلام  فیروزآباد در خونه داشت از جا کنده میشد
دوسه نفر  میگن پل احمدآباد بوده که راه ارتباطی هستش به سمت جنوب
آپدیت ۴۰ دقیقه بعد: صدا و سیما
شنیده شدن صدای انفجار در فیروزآباد فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77456" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت 3:43 صدا پدافند شرق تهران اومد ولی کم بود
ساعت ۳:۴۵ صدای پدافند شرق تهران فعال شد. از حکیمیه صداش میاد
پدافند شرق تهران فعال شد
سلام صدای انفجار در پردیس تهران [لابد انفجار شلیک‌های همون پدافندهای ضدهوایی است.]
الان هم پدافند زد
پدافند پردیس فعال شده.
شرق تهران صدای پدافند
[+ پیام‌های دیگری که با تفکیک اسم محلات مختلف شرق و شمال شرق تهران دارند فرستاده میشن و دیگه نقل نمی‌کنم چون همین محتواست که هی داره تکرار میشه.]
آپدیت:
بعد از چند دقیقه تموم شد.
🔄
ساعت ۴:۱۰
دوباره صدای پدافند شنیده شده در شمال شرق تهران
🔄
ساعت ۴:۲۲
پیام‌های دیگری درباره شنیدن صدای پدافند در شمال شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77455" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BZ5M9nVoAGcxs5i9AL5ljvhj1tbeITaZZbtAjdNloMcSbhi8ryogbypRIx40MRXLshMlQWWJJlpOMbvOT_O4sGF7zxLQ2XKslmoXppuRoPaQECvqZmI1ZKU661TD1fthRMKWVJ6VZPliAiAWaXC7hoFjjKtyTw0hw7n87Sh9VNlsgTMBaX3ZfKjnVuz60nhhNbU7JrAGwn8rAFqGJn-9ofbCdQ7oqtCuOV3cvvWbaUbVN-zu1_cjeTB4rRgVX80DV-Ekk0XfP5FMB74mwq8VPKrRLOCr2t6bI-6TK9JxtWuewqDay9lFTZmb5O7GgvtKTIx2x1Ko1imTNHUilOlaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: تفت در استان یزد
پیام‌هایی دریافتی و تایید نشده درباره مناطق مرکزی کشور:
ساعت ۳.۰۵ دقیقه شهرستان خنداب صدای انفجار خیلی بلند اومد
سلام خنداب و زدن 3:05
نزدیک خنداب صداهای وحشتناکی میاد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی گفت: یک نقطه در خارج از شهر خنداب دقایقی پیش هدف ۲ پرتابه دشمن قرار گرفت.
———
سلام وحیدجان همین الان پایگاه نیروهوایی انارک نایین را زدن
آپدیت چند ساعت بعد: منابع حکومتی
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
———
تفت از یزد هستم
از سمت بام تفت - شیرکوه رو بد زدن
خیلی صداش بلند بود
ساعت ۳.۳۰ دقیقه تفت صدای انفجار امد.
دکل تفتکوه رو منفجر کرد
سلام ۳:۳۰ تفت استان یزد صدای انفجار مهیبی اومد که از خواب بیدار شدیم. از کوه های اطراف نور و گرد و غبار شدید بیرون آمده.
داخل شهر نبود
سلام وحید جان .ساعت ۳.۳۰ تفت یزد صدای انفجار شدید اومد و خونه ها لرزید.
صدا از تفتکوه محل منطقه گردشگری در حال ساخت بام تفت بود که از اول جنگ کلیه نگهبانان و پرسنل را سپاه تخلیه کرده و هیچکس اجازه رفت و آمد ندارد
خبرگزاری‌های محلی میگن موشک بوده و جنگنده اصلا صداش شنیده نشده
آپدیت: صدا و سیما
صدای انفجار در خارج محدوده شهر تفت در استان یزد
———
بروجرد انگار زدن صدای انفجار اومد. دو انفجار پیاپی
بروجرد زدنننن
صداش وحشتناک بود
بروجرد صدای انفجار شدیدی اومد
دو تا پشت هم
آپدیت:
در بروجرد فقط صدای عبور جنگنده شنیدم
اما صدای انفجاری نشنیدم
از باقی همشهریان هم پرسیدم نشنیده بودن.
صدای جنگنده شبیه  جنگ ۴۰ روزه بود که بعدش خبر بمباران خرم آباد اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77454" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE4_xsQq8K_MVzg56-Rctaw73bQhLEJkM0mj5SDdvjLZont60qsELHrm3ty3FQIbZxJR9CN6LK9umMq1EGCE9MaJ8sDi_YzqddFYbnTB5ABVYNfBBa8RMmDC1cun4JuSidOPl65oNTWpbA6ixHwvHQgyFqHmAhEGF2wXKAPDd01UqcpH2E_IBxJ0jrovXd9XWB4CsNq27PqN4v2AFahrZCHoKzD2rnflJs71VIezLTAHD2TKB_j-_uZVxNK3oExumG9ABXrfhWgoBJxyU_fgTvOdvpl0qlAGFWm-oz27AgXEGfCIl6mtr_v6UIbLfk6AVY29pSlesXbTB0pvn48kRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد که ساعت ۲:۵۰ بامداد جمعه، نقاطی در اطراف شهرهای اندیمشک و امیدیه هدف حمله موشکی آمریکا قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77453" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیام‌های دریافتی:
خرم‌آباد ساعت 3:19 دقیقه صدای انفجار شدید.
خرم آباد الان انفجار شدید
همین الان صدای انفجار خرم اباد ۳:۲۰
سلام خرم آباد همین الان ساعت 3:19 دو انفجار شدید
سلام خرم اباد وحشتناک پنجره لرزید
خرم آباد زدن یه حالت لرزش هم داشت
خرم اباد وحشتناک شیشه هامون لرزید
سلام همین الان از خرم اباد موشک پرتاپ شد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان گفت: یک نقطه از شهر خرم‌آباد دقایقی پیش هدف پرتابه دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77452" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWqwn2H48tFLMXi70dhwp49a6xUMqsIjNMbouQn7fUyKSUw8RvLNsKljj2yAA5_CqadPFupWk0u-uA_g5E6Psi4EiMuOcpfZw_6w5x79Z3XhwDdrhNfieSUqXRyVppgJ_4vZRvCVyZiCZeRjkfO3mxSrdkp49uf9y2uiM9XKGXvHvsznsuDrDHIv8MDditbNTgTv8I4hQJbLxuDR5PlIiIKkNhZw8gJws2hbPB14Y12e_vqLHVqXJ3ltOtomEJ6IpL95YecSh56K8Od4kSPRenehEV9MyJNGZUkB7BbVmEEVr4hxB4hlXN1wn4tdgiwgr7pTwV6XKDmV_U36sYWYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77449" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mv580JQ6A1aVtFYSF0J1Cho69Y_VL1JL3s3XYauh5T0mkC-h6HbS4Yjs99XruJYOb3ahU54BX2UFxZoy15p6CfGBDP97KVnhe75W701XUUByNGUGSuR6gIT4MlH-UCmnZwcGVLcmJzUfRd42HzqUVHMNb2mQAML2DaL7Ah6do81WAWtk2mUPbYYqUMi_pM_XFbPpSO7I8L10ANFfaYiZqsMZ0Vp92OJmB7qnjkCdlsq0bUnod8ydptkeZveaL6kQkL3dVioMfzrklt8dAfepVfDuuET4QgskAvSZVqSjAfPT5Fg-tZs9rhgVxJ2zZWZ4GnA13BiuW2G1DIulsIvl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: سیزدهمین شب حمله را آغاز کردیم
ترجمه ماشین:
نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا [۲:۱۵ به وقت تهران]، دور دیگری از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
این سیزدهمین شب متوالی حملات است که با هدف پاسخگو کردن ایران و کاهش تهدیدهای سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77448" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=rOsV3aW3y2rvC2WfZw6fU8zXozlUzV0Q8TfH1m0GOU5kaoyWvxS0OH9VDR5XjwLm8McusH6n9df_--o2KH3_MBXZ6cipgA2iMDGt0JFREIlQKCR0u-cOkKs3yjYOL1xGoAGcOq0Xu1uFVimpjW6O1zwYR9QmRRaZnZ1yStVAmEPTZ2dcfHwkTaPCZFCVE5mfOwv2mGe76PEcKM3bcTSxNZoWorGr_72pyJMAIjGKlXTznfzzSFzXJwVLgW0mZI3oQevtijqiyfvj6dvkHbolCE_RIaQc8GeeLNkm9fqn-rsyRqmas5hnjq8Qb4DGxjlGa0kusSsUqgSPTcDLldSQjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=rOsV3aW3y2rvC2WfZw6fU8zXozlUzV0Q8TfH1m0GOU5kaoyWvxS0OH9VDR5XjwLm8McusH6n9df_--o2KH3_MBXZ6cipgA2iMDGt0JFREIlQKCR0u-cOkKs3yjYOL1xGoAGcOq0Xu1uFVimpjW6O1zwYR9QmRRaZnZ1yStVAmEPTZ2dcfHwkTaPCZFCVE5mfOwv2mGe76PEcKM3bcTSxNZoWorGr_72pyJMAIjGKlXTznfzzSFzXJwVLgW0mZI3oQevtijqiyfvj6dvkHbolCE_RIaQc8GeeLNkm9fqn-rsyRqmas5hnjq8Qb4DGxjlGa0kusSsUqgSPTcDLldSQjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
داداش
بندر
زد
همین الان
بندرعباس
سلام بندرعباس همین الان صدای چندتا انفجار پشت هم اومد
ساعت ۲:۴۱ دقیقه صدای انفجار بندرعباس
سلام بندرعباس انفجار های شدید پیایی غرب منطقه ۴
بندرعباس 2 انفجار
سلام وحید بندرعباسو زدن 2:41
بندرعباس ٠٢:٤١ يه صداي انفجار خيلي بلند كه مركز شهر  قشنگ حس شد
سلام بندرعباس همین الان چندتا زدن خیلی بدد برق قطع شد صدای انفجار بد بود
🔄
بندرعباس صدای انفجار بلند ۲:۴۱
2.42 چند انفجار بندرعباس پشت سر هم سنگین
3تا دیگه
٠٢:٤٢ سه تا ديگه پشت سرهم
صدا و موج زيادي داره
سلام وحید بندرعباس انفجار وحشتناک
دوباره داره میزنه خیلی بد میزنه
بندرعباس ۲:۴۲ صدای انفجار دی در پی
دوتا دیگه پشت سرهم زدن
۵ تا انفجار شدید  بندرعباس مجدد منطقه ۴ ۲:۴۳
سلام یه صداهایی میاد بندرعباس فکر کنم صدای انفجاره اما دوره
وحید بندرعباس ۲:۴۲ صدای انفجار بدجور میزنه
ساعت ۲:۴۱ در خونه دوبار لرزید
غرب جزیره قشم
بندرعباس همین الان هفت تا هشت انفجار خیلی قوی داشت
آقا وحید بندر خیلی شدید بود بیش از ۵ تا بیشتر.</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77447" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=BZ3m6CeP5j9WSUGJ-Sl7laC46dRtJmAljnefWHxdYROYKH2vt1CPBRWwbwuK6-dOYaOG8K3VH_mCSo255rvsj95DleSd7hkTm7RezrOHCKO8AwlDNSAJxjhi6vQePkCVZUbqsUeNZwnnuNuOm_OAhhNlGTnhnysHNoRxChAPmMXb0D6LEDTaPv4AKLCe6uP4Y4Ew2M-Y1Ai5LId5W_HnsrqfUMp8mULaYzrzt3FknB0HlGseHR8Xr7UYpnLS-IXh-VllmqvwHqrlrQpC6_FuHYe6fdsaiTm_l85TcxiTJnLwk_waCjZpfQiT4Zyw45OxE72ZE8p3h8Ma7HsdpqbOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=BZ3m6CeP5j9WSUGJ-Sl7laC46dRtJmAljnefWHxdYROYKH2vt1CPBRWwbwuK6-dOYaOG8K3VH_mCSo255rvsj95DleSd7hkTm7RezrOHCKO8AwlDNSAJxjhi6vQePkCVZUbqsUeNZwnnuNuOm_OAhhNlGTnhnysHNoRxChAPmMXb0D6LEDTaPv4AKLCe6uP4Y4Ew2M-Y1Ai5LId5W_HnsrqfUMp8mULaYzrzt3FknB0HlGseHR8Xr7UYpnLS-IXh-VllmqvwHqrlrQpC6_FuHYe6fdsaiTm_l85TcxiTJnLwk_waCjZpfQiT4Zyw45OxE72ZE8p3h8Ma7HsdpqbOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌‌های دریافتی:
اهوازو زدن
شدید زدن
سلام وحید صدای برخورد اهواز
اول ۳ تا خیلی دور بود
الان هم ۳ تا نزدیک بود
اقا وحید همین الان اهوازو بد زدن
اهواز انفجار ولی دور بود
اهواز ساعت ۲:۲۰ صدای انفجار اومد
اهواز صدای برخورد اومد 2:21
وحید رگباری زدن اهواز
ساعت ۲.۲۰
ساعت ۲:۲۵ یک انفجار شدید اهواز
سلام وحید ساعت ۲:۲۰ اهواز رو زدن
داداش اهواز صدا انفجار قطع نمیشه تقریبا ۲  دقیقس پشت هم داره بمبارون میکنه یجایی رو
اهواز ساعت ۲:۲۱ خیلی زدن بیشتر از ده تا
۰۲:۱۹ اهواز زدن
آقا وحید اهوازو شدید بمبارون کردن هنوزم ادامه داره
ساعت ۲:۲۵ یک انفجار شدید اهواز
انگار یه چیزی خورد زمین و ترکید
انفجارش طنین داشت
چیزی مثل رگبار
انفجار در اهواز 2:25
سلام ۲:۲۱اهوازو زدن از گلستان اهواز پیام میدم دور بود خیلی ولی کاملا صدا و لرزشش اومد
سلام وحید جان، اهواز رو زدن
خیلی شدید بود ساعت ۲:۲۲
سلام اهواز شیشه ها کامل لرزید مثل یه باد شدید بود
🔄
ساعت 02:24 مجددا شروع شد.
مجدد ۲:۲۴ انفجار شدید
یکی دیگه دوباره زد
انفجارش موج داره
ساعت ۲:۲۴ یه انفجار دیگه شدید بود
۲:۲۴ دوباره اهواز زدن
وحید دوباره صدای چندین انفجار
اهواز هنوز داره میزنه
اهواز رو پشت سرهم دارن میزنن
درود وحیدجان، ۴ ۵ تا انفجار عجیب در اهواز رخ داد، انفجارهاش با همیشه فرق دارن، با اینکه دورن و صدای کمی دارن ولی زمین و شیشه‌ها رو میلرزونن به یه صورت دلهره‌آوری
سلام اهواز ساعت ۲:۲۴ دیقه فرهنگ شهریم صداش اومد هرچند کم بود صداش ولی مشخص بود بمبه
انفجار ها توی اهواز همچنان ادامه داره
خیلی شدتش بیشتر از روزای قبله
کل خونه و پنجره ها دارن میلرزن
اهواز زاغه مهمات انفجارات پی در پی
اصلا تمومی نداره
۲:۳۲
۲:۳۳
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77446" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
