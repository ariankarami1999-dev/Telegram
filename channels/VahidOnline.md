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
<img src="https://cdn1.telesco.pe/file/suCSh7dbnOYzOdgQe1eseY5m30z2ZPXrkgUq9wvlq9KykNbX7c_UQghK-fylpS3X-gjCbnA0vUKSv0ESPOq14yw-68p3wG0RjiXJTuk_kZZhcNIsI2FAFkZGpjdiZP7rFR-EvIDfLiY63DCBwCjmU-b261WAPYh9a9kXPf0grSgACaxtiYSNWMYSKH_W69Su0H60fSMX0qaMxsbbyLcBnjzUhasmPA4oOs3S-R8vTxrElfZtjuHH2MmAE7VmIpxkpd3gae3vXcNZXw_noVjdEaUKPfSutEoA4B9B1IgVRDR1pv1fC5oIlpIQe0sDeVTo01RAWHgHNrmH9f3uVf4rvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 10:30:28</div>
<hr>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qqgl3e3B7Ya2k3sxB0-S7Z84jQo6Y0mQE340MfaQPRaRlK769o6_l_57YiQubStaCHUtr4SNNl6bFkb_jxvS5DTw6WQjj55BZnk-mhf6scK_PH1Oi-B0GvZ9F9t_hC6cN0yuT2jbINdqBiERhVlpApeWeDbHjd5efDQv9a9Si13JOmAWt_2X-HMMpJvaOZPGJOn3R5IZq3etvMIkD0zVlzy2rpQw1gN50PPXltaALtbO2_6sZgri6hRgZLSRKN4hxUYxjAB05erzZ-O_PGZuwkybl82y2eMHgi89_ythEB-cr7YdSHk6pL10vHOwow8VSmB4MJJ3b-ZAvNCL7gA5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cSsHGzWh23ZjwYY1oeY07QlVs9wJL--0POuV5K2VTainZGbsLiwd3WyL_ifk6iQ0iYQQyLeKbNMcqqk6iMIzTOCV_FrF3XhoWOC2cBKpRRSBGc6BVYoMKVXsN8jz6-mXRSF2HcYnlW0_UGpWL8Ksri6ESFQKXrIDg9j3k_6nE6RlJAiPFvJgJNdgzfh_qvlktBaHr5I8BnNipfXTsYGkKaFMuXnjSRB0KssEBP6bTi3i747pSrORtNd32wU7X0jlLzbCmCGybSMIoKpnS9fI8dkCEUM6eTC8D1GRLDNtGzg0CdKdWs4ZKxALfGScaajuQKaMWx6Xsl8j1JzwUW1wxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKJjGkG1NaLbk2BNHCuvIOyOJKGmuWeGXDK6PAkpAXXDP0j5qhCZ14Atv6r4I1TlRZjAyfKD683w7YrR1R0VjQCaRyAXNDF46EvNco9oDhfL2NkmDLA528z_uw0mNjPN3cr-v6n0qvprShzAeu8hP5Vd0O60dX5_UYi3kW6JdEeVKB-QjsiZQV7r-awUg-5IOBkhN9stQzZNWWtuYxQLMF7GMQcx95XL9gQ2gGS90BWD3t-vW__mDlxDlke4fe5NjHfJV92KKLnepdb9uq-aBbXGtYhktTVYKpHgPvpYjj7Y3qSLqmtz4iPHTGn8M5RNPHgT1xM7axh4UrLGRIgm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا یک بانک مستقر در ترکیه و دو شرکت وابسته به آن را به دلیل تسهیل انتقال ده‌ها میلیون دلار برای نیروی قدس سپاه پاسداران و فراهم کردن دسترسی جمهوری اسلامی به شبکه بانکی بین‌المللی تحریم کرد.
وزارت خزانه‌داری آمریکا روز جمعه ۱۳ شهریور اعلام کرد «گلدن گلوبال بانک» و دو شرکت زیرمجموعه آن، «گلدن گلوبال وارلیک کیرالاما» و «گلدن گلوبال پورتفوی یونتیمی»، در چارچوب عملیات «طرد اقتصادی» به فهرست تحریم‌ها افزوده شده‌اند. هر سه نهاد در ترکیه مستقر هستند.
وزارت خزانه‌داری آمریکا همچنین در حساب رسمی خود در شبکه اجتماعی «ایکس» اعلام کرد این اقدام بخشی از عملیات «طرد اقتصادی» است و هدف آن قطع «شریان‌های حیاتی مالی» جمهوری اسلامی در ترکیه است. به گفته این وزارتخانه، گلدن گلوبال بانک و شرکت‌های وابسته به آن ده‌ها میلیون دلار تراکنش برای نیروی قدس سپاه پاسداران تسهیل کرده و دسترسی مهمی به خدمات بانکداری کارگزاری در اختیار جمهوری اسلامی قرار داده‌اند؛ دسترسی‌ای که امکان جابه‌جایی بین‌المللی منابع مالی حکومت ایران را فراهم می‌کند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، با اشاره به کارزار دولت پرزیدنت ترامپ برای قطع منابع مالی جمهوری اسلامی گفت مؤسسات مالی همچنان درمی‌یابند که ایالات متحده در اجرای عملیات «طرد اقتصادی» جدی است.
او افزود آمریکا امیدوار است بانک‌های بیشتری نیاز به تحریم نداشته باشند، اما این مسئله به این بستگی دارد که جامعه بین‌المللی به سرعت حمایت از حکومت ایران را متوقف کند. آقای بسنت همچنین تأکید کرد ایالات متحده به همراه متحدان و شرکای خود به اقدامات علیه شبکه‌های مالی جمهوری اسلامی ادامه خواهد داد.
بر اساس اعلام وزارت خزانه‌داری آمریکا، گلدن گلوبال بانک برای فراهم کردن امکان انتقال درآمدهای نفتی جمهوری اسلامی از چین به ترکیه ایجاد شده بود؛ درآمدهایی که پس از انتقال به ترکیه می‌توانست به پول نقد و طلا تبدیل شود.
وزارت خزانه‌داری می‌گوید این بانک همچنین آگاهانه پیشنهاد ارائه خدمات بانکداری کارگزاری به مؤسسات مالی جمهوری اسلامی را داده و از این طریق انجام تراکنش از طریق حساب‌های تحت کنترل نیروی قدس سپاه پاسداران و شبکه‌های وابسته به آن را امکان‌پذیر کرده است.
در اطلاعیه وزارت خزانه‌داری همچنین به شبکه «سیتکی آیان»، بازرگان ترکیه‌ای، اشاره شده است. ایالات متحده این شبکه را پیش‌تر در سال ۱۴۰۱ به دلیل نقش آن در انتقال صدها میلیون دلار درآمد حاصل از فروش نفت مرتبط با نیروی قدس سپاه پاسداران تحریم کرده بود.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، جمعه ۱۳ شهریور در شبکه اجتماعی ایکس نوشت از زمان برقراری دوباره محاصره آمریکا، هیچ محموله نفت خام ایران نتوانسته با موفقیت از تنگه هرمز عبور کند و به چین برسد.
او افزود نفت خام در کشتی‌های گرفتار در داخل تنگه انباشته شده و امکان جایگزین کردن ذخایر صادرشده وجود ندارد.
بسنت نوشت: «مسیر حیاتی صادرات ایران در حال قطع شدن است؛ نفت سرگردان، ظرفیت محدود ذخیره‌سازی و درآمدهایی که به‌سرعت در حال کاهش است.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78233" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GI63JacYQg-7dSS9hc6RMBU19vGrCDSEIeUXEP5FezPr7jo6_foO2vOS8k0qHSEi7zTJnTzJpkN1i9Hxf3YRIBDVbXhtgO7CY9gKzJYi-f10qqgyqimp-0jTL10VZdW2-cWV01tIhUZHcsnQF1BQCDJFX_Vpxqf3lRogJzYFxcS62jlnSfIzo88JMTN5A_V5ck9VpOWegpuFSlEzumxFZX1H8uKkig9jGjCX71rG5aYFCieRFDMQ5TWzcTSqIylXFViqQiQNItFRi-bZ4MTLPsAhbdK9d40vJ5_fGSm8mnJnzo8k2LrKzRy6XleQrKa8TzrUni1Quxl-Idb_xL7X8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
دیوانه‌های چپ رادیکال، دموکرات‌های احمق و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ جنگ را برای آمریکا ببرد.
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه ما پیروز شویم!
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ چیزی که گاهی از آن با عنوان «سندرم جنون ترامپ» (TRUMP DERANGEMENT SYNDROME) یاد می‌شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78232" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBWx3vPWnLweiTE6WUUexBtozUI0cuGzVMEuqWBeISntg2W9x0bzOne1QiVCa49mMyBxQsNsUuryVVbZ-ChsQZ8bTecCc4erHkemHXBjChuqqLpSp0nmP7-YQgiauSUy8X9h-Pg866TDW18BWJ03iH0xetnF_Rjv11PuOA77yqCImhoVXKngAb0DstUeO477_iOFddl5TPou11bD6g6Y2MSMDxvWoNOFe8kt28i6uxW2YtSycTT8kGsSm_df9vNFFqiqxsRO2xATM-UlwDkX55hHE-JGKq5-TBtMoVecYJBHNnUrw2UKJ1jMEKc_I0gknf5oq2tonkelrlMuOmW2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «فایننشال تایمز» روز جمعه ۱۳ شهریور در گزارشی اعلام کرد اختلافات میان ایالات متحده و جمهوری اسلامی ایران بیش از پیش بر سر آینده تنگه هرمز متمرکز شده است؛ چرا که دولت دونالد ترامپ بازگشت به یادداشت تفاهم اسلام‌آباد را رد کرده، در حالی که تهران خواهان احیای این توافق به عنوان زمینه‌ای برای کاهش تنش‌ها و ازسرگیری عبور نفت از تنگه هرمز است.
بر اساس این گزارش، تلاش‌های دیپلماتیک برای بازگرداندن طرفین به تفاهم‌نامه اسلام‌آباد که شامل توقف اقدامات نظامی، بازگشایی تنگه هرمز و آغاز مذاکرات جامع‌تر بود، با مخالفت واشنگتن روبرو شده است. آمریکا اکنون خواستار توافقی جدید و فراگیرتر است که علاوه بر وضعیت تنگه هرمز، پرونده هسته‌ای ایران را نیز شامل شود.
در مقابل، مسعود پزشکیان تاکید کرده که کشورش آماده است به محض بازگشت آمریکا به تعهدات خود در توافق موقت، به تعهداتش عمل کند.
با این حال، واشنگتن بر اهرم فشار میدانی حساب باز کرده و با تقویت حضور نظامی، مین‌روبی و ایجاد مسیرهای امن، سعی دارد ثابت کند ایران دیگر نمی‌تواند از تنگه هرمز به عنوان یک کارت فشار بر بازار انرژی استفاده کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78231" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZaXdEvJWH1bpdORqov5-JKzzS574FzvfSdltAgQG26KsB6yTkU3Q7m4qZ2yScTczED12cZEGiKIgNbK9oEb6jCoJmBiK5X9DUj3UgXC82oo9SORu1_XmgyreK8f6X6QS1Ea5LewLXPenzMtBVnhDmXbFEiab8jiUOEiA_8OvWVZYTOUQgz1VHW_wV9hAIyr1cQePPg3vBul7nIKbcVAAYW7KUDAtatUtpPVA4QK5YJQNqdXbMWnM3QIu6OEvNLDE_faBsWuIMitgg7rPF2ZlQUw0Lc0VnAZf3A_w0hzVLuO99Tabst1ij9qGJm1V57qWOzumcFVNAlD2czFCw7zug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گازوئیل در آمریکا با ثبت رکورد تازه‌ای به بیش از پنج و نیم دلار در هر گالن رسید.
انجمن اتوموبیل آمریکا روز جمعه ۱۳ شهریور اعلام کرد که قیمت گازوئیل در این کشور در حال حاضر به پنج دلار و ۸۵ سنت به ازای هر گالن رسیده، در حالی که یک سال پیش قیمت آن سه دلار و ۷۱ سنت بود.
هر گالن حدود ۳.۸ لیتر است.
انجمن یادشده این افزایش قیمت را ناشی از اختلالات در حمل‌ونقل سوخت به‌دلیل جنگ آمریکا با ایران عنوان کرده است.
گازوئیل، سوخت حیاتی مورد استفاده در حمل‌ونقل جاده‌ای، کشاورزی و ساخت‌وساز محسوب می‌شود و بیم آن می‌رود که افزایش چشمگیر قیمت آن، نرخ تورم را افزایش دهد.
قیمت بنزین معمولی در آمریکا نیز چهار دلار و ۱۵ سنت به ازای هر گالن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78230" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1OiiUl5YHU1wNfpEWQotNqc_6xRgVTiCzFZEDPyU4c2IEYrXFZGXtbkTuB28kF_DGnObsxEoKnGwltuMS1-0M0U3PdpYkXoWSGx94vYD_nDOanhzLljfPEI29VQFnf9TLlDy4ue0Hb-Ni2bGAFIYB0DsGeNn4VLJVSIR1FY4U6h6E4oGbLVWfREiHhfkKr8G24cB2x93lNy3Nr-OAcvD2J10UKr8jxgNrw_p6vcKZ8vO0g08k3q0qFSoB2oEIPVLqJ-9UlgH_pvLkysHyWoxIAALB8z3exBnfMHwMbgf3Dxrkl0gGTAq_1LJVOgFmrP1TFSuusfrvEe5i24GrMaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌هایی که من دیروز دریافت کرده بودم:
▪️
آزمون Pte  زبان برای ساکنان ایران لغو شد
▪️
موسسه‌ی پیرسون هم تمام آزمون‌هاش رو برای ساکنین ایران کنسل کرد.
امروز صبح روی سایت اعلامیه زدن یک دفعه.
مشهورترین‌هاش برای ایرانی‌ها امتحان مدیکال کانسیل استرالیا و وزارت بهداشت عمان هست.
و امتحان‌ زبان PTE
▪️
ما جمعی از پزشکا برای مهاجرت استرالیا تلاش میکردیم و هزینه ازمونمون ۳۰۰۰ دلار بود
الان لغو شده بدون هیچ توضیح خاصی
دوستان هتل و پرواز بوک کرده بودند برن هند پیام بدن الان میگه نمیشه باید کارت اقامت کشور دیگه ارائه بدی
خبر:
موسسه بریتانیایی «پیرسون» که برگزار کننده آزمون‌ زبان انگلیسی «پی‌تی‌ئی» و آزمون ای‌ام‌سی (شورای پزشکی استرالیا) است، در بیانیه‌ای اعلام کرد که به دلیل تحریم‌های جدید آمریکا علیه ایران، آزمون‌های داوطلبان ساکن ایران را لغو می‌کند.
پیشتر در تاریخ ۷شهریور۱۴۰۵، تعداد دیگری از برگزارکنندگان آزمون‌های مهارت‌های زبان‌های خارجی، از جمله دولینگو و تافل، اعلام کرده بودند که این آزمون‌ها دیگر در ایران برگزار نخواهد شد.
پیرسون در اطلاعیه‌ای درباره لغو آزمون پی‌تی‌ئی آورده است: «در پی تعلیق 'مجوز عمومی G' توسط دفتر کنترل دارایی‌های خارجی (OFAC) در وزارت دارایی آمریکا، از ساعت ۱۲:۰۰ بامداد هشتم سپتامبر ۲۰۲۶ به وقت شرق آمریکا تا اطلاع ثانوی، ما قادر به برنامه‌ریزی یا برگزاری آزمون برای داوطلبان ساکن ایران‌ نخواهیم بود، مگر آنکه بتوانند مدرکی دال بر اقامت اصلی خود در خارج از ایران ارایه کنند.»
در ادامه این اطلاعیه آمده است: «آزمون‌هایی که در حال حاضر برای داوطلبان مشمول این محدودیت برنامه‌ریزی شده‌اند، لغو خواهند شد. به‌خاطر این مشکل که برای آنها ایجاد شده، پوزش می‌طلبیم.»
سرنوشت شمار زیادی از دانشجویانی که قصد مهاجرت با هدف ادامه تحصیل به کشورهای اروپایی، آمریکا، آمریکای شمالی و استرالیا را دارند تحت تاثیر این اقدامات قرار خواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78229" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=TYGkFcotnYemihsfsUE_Rz3HZfo0uvVqKGv9cTGflwNDQELRCkaOkFU_lY3Yxwp2I37mkbXr_Wd13ZgYsZYfkEqB0Nn2Lm58kCsIX7lHEq-5NI6702tu5CMa5GH304PWNPKaSkYNlfwBTESPRT3GgmCy1HqZ8aZWv2bSgP-PY2OGsxri1J29DsRmn0bxDZNSt8AWp1tklsDBj1hqtb7QlMC6swkLavZtsA0wArhwqhI-B6rew05nz8gguVz069Jjv_rtcB4ntWHt5TMf1wRXdNFIPYj9MhmUUl2mf7UW1ar6cT3ECIEJBrhRIhjl0bLIOjLoSL1nLnq0kcTdWYdz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=TYGkFcotnYemihsfsUE_Rz3HZfo0uvVqKGv9cTGflwNDQELRCkaOkFU_lY3Yxwp2I37mkbXr_Wd13ZgYsZYfkEqB0Nn2Lm58kCsIX7lHEq-5NI6702tu5CMa5GH304PWNPKaSkYNlfwBTESPRT3GgmCy1HqZ8aZWv2bSgP-PY2OGsxri1J29DsRmn0bxDZNSt8AWp1tklsDBj1hqtb7QlMC6swkLavZtsA0wArhwqhI-B6rew05nz8gguVz069Jjv_rtcB4ntWHt5TMf1wRXdNFIPYj9MhmUUl2mf7UW1ar6cT3ECIEJBrhRIhjl0bLIOjLoSL1nLnq0kcTdWYdz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
الان از اصفهان موشک زدن یه دونه
سلام وحید جان
ساعت 7:12 دقیقه از اصفهان موشک شلیک کردن ( از سمت [....] اصفهان)
همین الان [...] اصفهان موشک رفت
19:13 از سمت [...] اصفهان موشک زدن
همین الان ۱۹:۱۲ از سمت [...] اصفهان
فکر کنم [...] بود
بالسیک شلیک شد به سمت [...] رفت
از اصفهان همین الان موشک زدن صدای وحشتناکی داد
اقا همین الان یه موشک از سمت اصفهان شلیک شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78228" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qXFLDx5UdAYCLYUbVRqDHtTa88z3eMXF63DS8GM_OkIr4y5DqK9QjJd00e1lXOFep4oTXsK8OGWaH9XupaEoz6xXSQmiXlM7TNxsp49zqrcQ4gFL7dDAkANHbMtAzFwzP8RX-FRqB5bzYeXI4hst8W3_hWbniTTgmZKuxC59dudlHQGlcmykyyOrUrXtqx9skJzXIMnkSlpBY1k01ZHWaQgIHw1lSzSki_LfatB51RxiUuYAjz6s6EEoXTgXmiUzAOhCSxFa7oaTes_Nv1vOUksC-imAFTnQzim7AXep1pSZK4kN6wnaI2gSXGTVCsEtQSL8Z_Yenhy_dRI9tMN1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JuxCtqQnMsk7l-yiwUCaG-o7grw2VABKPTZEDChorx_Xze23ONYtN7W4yQliYBwwIrS6E1odlUeSvpFRwCAoPX0BD5YecQ_iNV7KnEnB28L_3KHzXx4oqBhDD2ywajjTTpVwH9SPczo2Bs-QBu6v7Y57qvlcLgF4hs9G6NK6LFJUrfhJDzM6CJRC_x3wVDvBnUXyBgiBMkl-AdltSuXsq_jNi-DGxa5ggLCyxqRgeNQt0tn6HtLt06pazKWH-qQEhSRL8uB-SLt2ER9S98xSqqn7FjEauNqrVizU0ra3zJ2Hn2bSq9COURVGB2wgRVCcN3gPnphMSugO21IB0NWy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dXFwalgcD2NwsvflSnphUKr8LN1HqnVndPAT3r3BtbkzeB_6Dw7m_tlROyc-2rSvxga0lUtJnGPh3QEJU6wmcLMNhdEZKHBQyHevI07-v1z51wHZRfMI3uqPEUC1Dn8vTn5JHzaC2iym2cEuejnaEVa2VtpZhKVSILO2T_B0HBa9BIn_Kl7pI7fTw0vqPnTUO5qq9ZGQa7llWrSYFwqtQ9KPNtwC_RVrsc314wDDQXMq2lQvReW69xAL0phPiK_6DiLP_GZ5nF3K6WkOiChVcSVIr9HSpc8xHy8VtMhyH8p70S8TNkXAsD9Z6yLT41vA61lsw_P-bbsqT8ytMyGwGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IXblzcFcgqr00hB6mTZLFuNjrpyWJmDgZ6Gze9qcJbPFhzHpUf5fv38fia5fD2OiFJ8kVlWqy9ZCwFegnNEC2skRxcSDeh2uFG1qVFdygkSdPQbSnJ9VLDYF0K2_A7-jusDB9b6FlexpVNJzXqdEBSKCImvR7aQIs2o0b7t8SLcO7OfSapH0VKgfC7POHsxp5DcO5AqtwJdf7hRk0pdi9o-mgsFPAYjIHmnYNbOHUnMkS0Zh1L9dsfhkGbCI22InKn_Gvq86sVg8I4GhEwjcvnVjSy7Nm7amzzQj63Gcf4LLqJykkzC_EH9VPl7PtRfFxjUGO23AAfqqp6MWedWWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gnuQEyj2SLBCwpWWaQIWX6eCOKh5jncEyV5xM7hX3SqajzJL3a_19U79YO77w90aXrLe-KxLky-8T_-wkT7B5GIeVNd6YvoKUDju9pQr4EwQeXd80gIQMU0dzu_wN72EEu5Tl4x0iR3fCwWrvYQN-6tLWM8IIkNeh5Afx5BDUOW7uM3HfUoeZscufTCvtXzFqIy5e9x0PaSZ9NlltfG1-5_Wu9KOwQcxWu3aHzxwn6aAKSmzOzr6aIcHGIkPW3NbGyvBu5O4rEKDt8Z4bNYinEt_LBohknJ9qsCIxkcDQp9kTc2FauqU8Ea6j8S_MR8uv-vRKbFFMJYV4bbHBtlDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b7v76Hme5f-4qDHhiceL3Ptls-MlRwif_N7xijcp1T6N_kqwWW5EOeYzSe7mBtTsTW6WBcNrk___yjpTQNmzpz7BX3Sjn87kQnoHB3Nnt8hgxg_2-dSi15l-4ISwiTy9uK0H4A-eurR6u0MiBImfXpXNkTKU4lTTtZx8tKbZ0dkYfhIhmWFGlgKtonEBcPxoWnOgExe_GTkLVPcWfeQ44Ch9MfG8gXtdM-uXml2L8g4gVvfjKgZ3a8V32KEdZj9n7ZU0uejtvlwKQoDC91DnspEtHPOHi1BA__KFOY3rf4032G_U5tHBsLQQzTVuuSVxm_7UKMnVpjmfOjbemq7ePQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hc2y6KaSo5pvYlupJZVPJ2_xBeLMQ7GZ4qcerGxKsOWhD81WxatnBUt9_Pw6LfU6AFJkg-ZjYIO0U6EunWCfdcWhk4730UatQKHpKO49Q8Oe7wed21vZt1LAU5r79g_J2lCfPhVznrZAoQbn1kLHG1EyxDFUGtalyM7RuFQQ5m5eyfeSf24cnAvVKdWqt5YAl0nrcJMMtJVlZByFbP_QXRkldkeofQzzxb48orNxcY29HFN9fkVTmNYmiMsddm3UaRdbS3DQTHurS8NC1P06e9o2hLoV4gbHbfT94esV97tEJLOme78wL-28WTUZKJCGH6h8PZPLWWcodr__CuejZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXsr6PhuJI--_vJZovpqnCSDIyxvKWexXvi2T8JtAWyQu3SCCu3cwwJtdLICyzH2XSFZ7hMjqEBP_U0Wr5JiI35G1XxIfHDTu7wBCtiu6k9i1HpRXSQHEPOfYXwlw_JDv5A7Y3K8fq1gOSJXB6qJXa_MKt_D8JRR2NTOXS2YJVUbm4QI2USZPCaMCo9u-H1wbZzY1G6f5Asw1SOqiULvgQWNbdh5Z6MAeQjaPs3okDDyHreuhJ6wKKKPrkJPM5lBqg7PJZUizQJnGAMxg-VkBTcr8_-kXE5-IfcqUhGa9WFGL7kcIUy6ZjNUWIAGrSbhp_hg0fB4Py92GbdTBmLyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
برای آن آشغال‌های خائنی که حاضر نیستند درباره عملیات نظامی ما در ایران گزارش دقیق بدهند: ما عملاً مقادیر نامحدودی مهمات با کیفیت متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنچه بتوانیم در این جنگ یا هر جنگ دیگری ــ که وقوعش بسیار بعید است! ــ مصرف کنیم. علاوه بر این، ما در سطحی بی‌سابقه در حال تولید مهمات هستیم. در حال ذخیره‌سازی و آماده شدن برای هر وضعیت احتمالی هستیم که ممکن است پیش بیاید. این مهمات را برای خودمان، ایالات متحده آمریکا، نگه می‌داریم، به‌جای اینکه آن‌ها را به دیگران بفروشیم؛ اما فروش به متحدان نیز به‌زودی دوباره آغاز خواهد شد.
همچنین لطفاً همه بدانند که دولت بایدن بسیار بیشتر از میزان مهماتی که ما در ایران مصرف کرده‌ایم، مهمات را کاملاً رایگان در اختیار اوکراین قرار داد. صدها میلیارد دلار بدون دریافت هیچ هزینه‌ای به اوکراین و ناتو داده شد؛ پولی که اروپا حاضر بود بابت آن بپردازد ــ اگر فقط از آن‌ها خواسته می‌شد. اما ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
از توجه شما به این موضوع متشکرم.
رئیس‌جمهور دونالد جی. ترامپ
truthsocial.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78217" target="_blank">📅 18:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFInElQKr9en2s1zPMdgCs9BJFr0smH_tzWDoZdhqdAqmWT6vT_VYv93yQJhRkyOZkaDPbHps5aTQARBw7bJvliP05zDY6AoKJZ0ZMu4J05DYkZIUbuxxTlCMCFvsEPv28P88HLyvxnl4aedcz6KE9gpOngFhi7UDNG-UHdNhcxs3-Ot3alEmcpOjecLnTeLfd8VwS_czBdoLY980144UHOVYj7j4UvZaDPXzXHhvqZqHuXN_TBK9SG3ALXYB5cOUkz_2H8w6n5lNpD2ipY8NJeI1AnboMaZm153yA9gM9vPN3pKNy4rjCPr5iLVYk1XzTvZGAHlPMywYU4FRu6Nsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رئیس‌جمهوری اسلامی ایران، روز پنجشنبه ۱۲ شهریور هشدار داد که «ماه‌های تاریکی» در انتظار اقتصاد ایالات متحده است و از مردم آمریکا خواست اقدام به ذخیره‌سازی سوخت و بنزین کنند.
او تاکید کرد که «جنایات جدید آمریکا»، دکترین دفاعی خود را به تاکتیک‌های «نامتوازن» و «چندلایه» تغییر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78216" target="_blank">📅 17:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qu2f6ZGRpfbnoEF4IGMPXVwOehPKtgkyWhb09UraMyDK7cL6zS3st-ouN7mPInDGpLis98F_oWk46fa-4Btb9VAH_yRPzXnfrls8WkFn5GsZ_DN6to_d-ozUquNrefZhuTQR9h-oEO3rSnzA9QTcDgYKkWLp-J8L5YVmpRNs2wRb-WU63vPRKzeps78QAapCFxtqD_wLkaibSW9M0jpNcdNqM8XtU5xR2quElMDWC2Qz0XNoqAkXmSPKohliYDaXN9gMBynyoMOKptlczWqmDCRYpW9MFmellej8HQANt0GvizZy7t6XuIaNc5Zc0GI-u_jsKfbnoK3pGOXDF0HXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">916208
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78215" target="_blank">📅 16:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbKdKcWFv8CUzkudPYn5fUGfJmwff9y1uo-0dj7HVOwfqrAuXWjD6x_zo_HsAQClnWQTs977oqPWUvf8dCthmiLMHQsVWXcZcUHuTqyjcLGSCFFj4dK0PcPK9LM1wasgXgWQ9z-jn_65fHP0uKEtxoRl6IHaiEgJQ7_aONd8v3NwNyYpk02S2P2pGY5M1NySotic_526uZPJK34MraLBDNFOYZsoeY2TlzM0e0WYIx4QzSmXaSZ8vHrmla3SUyzCro-om6_dyevPQ3yRZWxXZIN2XyOuPFpRpTO3p_M0tuan-sE1U1NpglRzhohz75_-tYNLttp10gwltYBUxD5lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا با انتشار تصویری در شبکه اجتماعی تروث سوشال، مجموع حجم نفت و گاز مایعی که پیش از جنگ از تنگه هرمز عبور می‌کرد را با میزان کنونی آن مقایسه کرد و نوشت: «حجم نفت هرمز بازگشته است!»
ترامپ در این تصویر، مجموع حجم نفت و گاز مایع عبوری از تنگه هرمز در زمان پیش از جنگ را حدود ۲۰ میلیون بشکه در روز در نظر گرفت و میزان عبور این مایعات در حال حاضر را ۱۸ میلیون بشکه اعلام کرد.
این در حالی است که سامانه پیگیری موقعیت نفتکش‌ها در جهان، میزان عبور نفت و گاز مایع در ماه گذشته را به‌صورت میانگین ۷.۵۴ میلیون بشکه در روز اعلام کرده است.
بر اساس داده‌های این سامانه، حداکثر میزان عبوری در یک روز، ۱۰ میلیون بشکه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78214" target="_blank">📅 16:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JLNUrbulDVy_gqHfItqUX0q0bNSQk6_gp0rz6zWgzATOjjh7h4oQIIZhJiVpKxQD6kjB87lK4RV2U_hAq3DNQ8Ucukhwwsuz618bAaHCIs6Ej7PslCvNvWBxYgYbytHa6DVl2IAhqIlqGU0gBcNRTbyKc9WGaVICwDxGq-Ar83qlNoDUUsNgfgdWX4AkICXzNlWB5L9byQYZPFERs7UE_G8EiXygwpoR7SAtQZZYvGyNSNWEWg0nkzZ6xIi-lUNp8Q3IR_HmIgsIn4EGpm-Lkzy8A7qYO8z8muw7riywW70eTb4hTbXesA3YZzT1n3zcUmgQ6NcrQxVNHQ_Ca3jyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WHRPBeT1wbvwu9Ac6ZAVYIl3jxumvQ4BbSh2ujSSA8_c7NN6FCdH7-1d-jFGXiqz0IMjF4o1n5OL1V9m6FiMcHPk5HO3tZa2XwgLPfLLZfo4qnglHNosNofIg7xo3BuZuCQi5_sR8y0xFdsaNIImD_DJ7zCVIHDLQDdINU2OhST4n_S6ldSnRSli-5LmAJFe3LZUfMP8RrpP-n1jn2-4rEIEpByrAsxzC6DTJyCGtdbhGJoiddvKzRhokIubLaKXbFVzYvrjX0m8osfcB8EtMlETJYVu1UhijNfd7LQjjt4NkWihoaMhcPGAU2dtigl78Z8WwnuhADlnei7b4tDTCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=bUNgkTRKga8u7u7w4HEt-Y7lDz6quCYueU47r3SzYpehZmksO_T7gCdjP4K2WZAeuMni_1EIWpmdcJoGn8eFkGntn-TNTNQE84kcfWXCNdOmytydQcaad-G5grMdRt4aScNyRCRPMkBxjiQMzi8sPD4ZaEkkCa1vExLYvEG8TsDBG6Iq1nb4r_Fr8gqYXM95a_Cop4yuntKAiWigPx-FipEDDcBTxQHLfzZJWRKHmZ0dd0PmeVjESjvWf8YSpliuPut6NV08uT2bGGYliIUUmd2rigihvTnyxStvjdDD2sht9QNWIo51G-Y11-3pshdsO0ugGDNs3fjm5RgF64Oaqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=bUNgkTRKga8u7u7w4HEt-Y7lDz6quCYueU47r3SzYpehZmksO_T7gCdjP4K2WZAeuMni_1EIWpmdcJoGn8eFkGntn-TNTNQE84kcfWXCNdOmytydQcaad-G5grMdRt4aScNyRCRPMkBxjiQMzi8sPD4ZaEkkCa1vExLYvEG8TsDBG6Iq1nb4r_Fr8gqYXM95a_Cop4yuntKAiWigPx-FipEDDcBTxQHLfzZJWRKHmZ0dd0PmeVjESjvWf8YSpliuPut6NV08uT2bGGYliIUUmd2rigihvTnyxStvjdDD2sht9QNWIo51G-Y11-3pshdsO0ugGDNs3fjm5RgF64Oaqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">dadban4
:
"امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه.
شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند.
ما مادران نه می بخشیم و نه فراموش می کنیم.»
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند.
او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد."
abelbalb
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78211" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f407m1JcH1cNHk9hHTgQR3y2F6ySi_g_I1rx2szqizkqxUEHkJbmD2YiBveqJDhQoF_1YyCcmgtfLFdmi6YscUmNrqKqX6uFvxpzM6EKA92J2QAZZ1TO-qX2yvr93-z4Q7qJNl6KsBhcPRT74vpapZUP9zNwYsD1Uq89XMM0n2kX-jzRWkaE2yd47BTcVmByiu8SAS5xoxG-C3qDJVUiZeWAWB8yCDOWRrHIzt2oR0E6DbIz5Jo7sTXJcxR7iIYjGRTMlXJsg2R39gpK7NZH5H3At3CrEmojPO3hhiCnOfJ45sKx-I4vI7LIPqJDshGNqa4wwLH6KPoNzR0vtz7Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، از کشته شدن سه خلبان ارتش جمهوری اسلامی ایران در حمله سه‌شنبه شب آمریکا به ایران خبر داد.
این خبرگزاری با انتشار اسامی و تصاویر این خلبانان گفته است دو نفر از آن‌ها از خلبانان نیروی دریایی و یکی از آن‌ها از خلبانان نیروی هوایی ارتش بودند، اما اعلام نکرد در کجا و چگونه کشته شدند.
با این حال، اسامی اعلام‌شده سه نفر از هفت نفری هستند که روز چهارشنبه ۱۱ شهریور اعلام شد در حملات آمریکا به شهرهای اهواز و آغاجاری کشته شدند.
در جریان حملات شامگاه سه‌شنبه آمریکا، به‌‌گفتهٔ مقام‌های ایران، مناطقی از جمله فرودگاه جیرفت در جنوب استان کرمان، عسلویه، کرمانشاه، مناطقی در استان خوزستان، شهرهای چابهار و کنارک در استان سیستان و بلوچستان، سیریک، لاوان، قشم و بندرعباس در استان هرمزگان هدف قرار گرفتند.
سخنگوی وزارت بهداشت صبح پنجشنبه از کشته شدن «۱۸ نفر و مجروح شدن ۱۴۲ نفر» در جریان حملات اخیر آمریکا خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78210" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dNc0Iwopz-1tgTW5CQPC55vfrkpvlnUYE6EITfrq-2kjy4ZxH3idCW5PMFNT2bK_dDiwgsG9b5AeVjz5yw3T0-zb3bOxO2i_QL7geHkWfxhDi6ULzOIkrQo38A0L3KoUy3llsdZlMjiaOPWXw3vS-O4yatB2lhx8Oy17sQxbrIQD9x1PFasu3_bzMeq4mlUSGEFKXD6hNKJ8PG-tLcfTswxqx3wtJAbEc5pgfYEU59Wc_sDqxmsY2NVQz4XHLOO7XiciYjzn458xeC35qZ1R33vjNl1d6uKW3IkxkmZgC7EoiANhfAmPzFXJPWpcVdwrXNh5w4g4OI3t06aUvoxlBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78208" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F9wCUSTKYDnJ73dSRKSom5WtbwS-OBGCvVkiAZ2ij2sFzPQ7Ty-mqEEWXRQDADp3sJVQX3JnKEFVJMfWJD4BRzBDvXr7R2EakXSHdITDeFktys4CRhJz38prAC6ykkw2AIUlVlk96CowNWkTUP0MKWhA7D7w3paz7UA-18--AIuXzKVm95T8MuSeAlCsm63xjDLG4fSIjYGoVnbLVIx2Nf5SW52v3lVZTX55fLsNgrCD7Pzz96Z2doWV9umn37MnxM3kDt1kg5sLlwoFvOx5UfYvrqpdi_ztATn7VhSbbCkVC_V-umHBYfzk7C-vbuwSFSrpVXsOJnc-W0cW-pXUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، پنج‌شنبه ۱۲ شهریور در مراسم روش هشانا با کارکنان وزارت دفاع اعلام کرد حمله جمهوری اسلامی به این کشور، اسرائیل را از همه محدودیت‌ها رها خواهد کرد و این کشور حتی زیرساخت‌های انرژی را نیز هدف قرار خواهد داد.
وزیر دفاع اسرائیل گفت: تمام زیرساخت‌های ملی، نظامی و غیرنظامی، از جمله زیرساخت‌های انرژی را هدف قرار خواهیم داد و ایران را به اعماق عصر حجر و تاریکی بازخواهیم گرداند.
کاتز همچنین افزود: فشار اقتصادی و نگرانی از قیام و سقوط حکومت ممکن است جمهوری اسلامی را به اقدامات از سر استیصال سوق دهد.
او گفت: حکومت آیت‌الله‌ها در ایران به‌خوبی می‌داند چرا پس از آنکه دو بار ضربات سختی به آنها وارد کردیم، برنامه هسته‌ای را نابود کردیم، خامنه‌ای را کشتیم و به توانایی‌های راهبردی آنها آسیب شدیدی زدیم، به اسرائیل حمله نمی‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78207" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JH1_Mx_3lTlBvH3A2ZcJbOmU054Qj4RU3kP1VqS69yvhZBpSduD8MrSb23iuclIOXVvrYnkqIHzc7WAakuiXaaGtFqOgKcI9V1MoaXRD4rUcvgjgX1eFP-jKgo0RZKv0r2xB1X05ZPRJANrlY5pN9xVBDcAzwfX5qrK-CyPf9xJA-GTrrUwBasSk5rnyZ0iBBrjSdk4ZE1YuFmgCMtDpTTWjtVLwNcb0AO20gdyHTxRE0Y0UvtRcsKLI52yt1qk8XkaehA-H18S0Smf2GxhQ5qGaA8dARSiHtvW1nXLugTudVw3-h-sVgr5PrSEN5WH4wsNIh8YZC6GlFWpP0-TKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خودروسازی سایپا، روز پنجشنبه ۱۲ شهریور ماه و چند روز پس از آغاز ثبت‌نام طرح فروش فوق‌العاده، با صدور اصلاحیه‌ای رسمی، بهای مصوب چهار محصول عرضه‌شده را به بهانه «افزایش هزینه گواهی اسقاط خودروهای فرسوده و سایر عوارض قانونی شماره‌گذاری» به‌طور چشمگیری بالا برد.
بر اساس جدول جدید منتشرشده، بهای مصرف‌کننده «کوییک اس» و «سهند اس دوگانه‌سوز» هر کدام ۳۳ میلیون تومان گران‌تر شده و به ترتیب به یک میلیارد و ۳۲ میلیون و ۵۱۰ هزار تومان و یک میلیارد و ۱۲۳ میلیون و ۶۸۸ هزار تومان رسیده است.
در بخش خودروهای مونتاژی و وارداتی نیز قیمت «سیتروئن سی۳-ایکس‌آر نسخه وی‌یک» با افزایش ۱۱۵ میلیون و ۵۰۰ هزار تومانی به ۳ میلیارد و ۳۸۹ میلیون و ۳۲۲ هزار تومان و قیمت «چانگان سی‌اس ۵۵ پلاس» با جهش ۱۹۸ میلیون تومانی به ۵ میلیارد و ۸۱۹ میلیون و ۱۲ هزار تومان افزایش یافته است.
این در حالی است که متقاضیان در روزهای گذشته بر مبنای نرخ‌های اولیه اقدام به ثبت درخواست کرده بودند و حالا این محصولات با موعد تحویل ۹۰ تا ۱۲۰ روزه با نرخ‌های جدید تحویل داده خواهند شد.
روز چهارشنبه ۱۱ شهریور، بازار آزاد نیز با موج تازه‌ای از گرانی همراه شد و چند خودروی داخلی دیگر جهش قیمت داشتند.
به‌طوری‌که تارا اتوماتیک با رکوردشکنی و رشد حدود ۱۰۰ میلیون تومانی به محدوده ۳ میلیارد و ۷۵ میلیون تومان رسید. بر اساس گزارش فرارو، در همین روز دنا پلاس اتوماتیک با افزایش ۲۵ میلیونی به ۳ میلیارد و ۱۹۰ میلیون تومان و پژو ۲۰۷ اتوماتیک پانوراما به ۲ میلیارد و ۹۸۰ میلیون تومان رسید و محصولاتی نظیر شاهین اتوماتیک پلاس و سورن پلاس دوگانه‌سوز نیز به‌ترتیب در سطوح قیمتی ۳ میلیارد و ۳۰ میلیون و ۲ میلیارد و ۴۱۰ میلیون تومان معامله شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78206" target="_blank">📅 14:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtl8SAaQ0JuH9zYNBoLTf8QrUFCnLa6_4fwk7kljxf_N7WENCQaSbfT2ivFoMQSXDHf73W0RLJIlcsDi6KWzVXchJl9wzONyWwNIAyEx0JxlZ4x-SIGY6Owc49_N-cm5D5D-xUw_H-zrFc8bpur7WvX-7x4DGgKAW0gEQcSj_CQ5pCvJDtkLT0JO6R4HmRKwBXhfcJ7C_q8wzrPoPdGk7wnBMLWPWJTxw6meDZm4sd7vKkifD6mdwQ5n7V-YVCtVyzwHlC3dbooUqj-1vIBIsgGRrkZnE46OHy6BgDAZOkARK1uRAzMnsuKOmLCID6nc0aWBvqDU9LwVUMS-rnF2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین شریعتمداری، مدیرمسئول روزنامه کیهان، پنج‌شنبه ۱۲ شهریور در یادداشتی نوشت که ارتش و سپاه باید از «اهرم» عبور کابل‌های فیبر نوری بین‌المللی در خلیج فارس و تنگه هرمز برای «مقابله با آمریکا و متحدانش» استفاده کنند.
مدیرمسئول روزنامه کیهان نوشت: «در عمق آب‌های خلیج فارس و تنگه هرمز یکی از شاهراه‌های فیبر نوری بین‌المللی جای گرفته است. شاهراهی که بیشترین ارتباطات اینترنت، تماس‌های بین‌المللی، تراکنش‌های بانکی، سرویس‌های ابری (iCloud) و حتی ارتباطات هوش مصنوعی و دیتاسنترها از همین کابل‌ها عبور می‌کنند.»
حسین شریعتمداری، نماینده خامنه‌ای در روزنامه کیهان، تاکید کرد: «سخن با مسئولان کشور و مخصوصا با ارتش و سپاه است؛ خوب نگاه کنید! کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78203" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AxJceEaeigjxX-bbBsC0qCHUWsnI6GWC8AmDNqQTQs5qxuTVEPHS2qusTGo6PSClHTrXFFZgHee585c9dnD8V26cqoHH0y_Fmjcd9JXEDLDrzyuH6RP5_fC5RIHQzJnYPovv5hvNRlFjJ1JUYblshzEgUzyKW9tvNvLBgKiTvNbISpmN0DlTzylhBtkD-upq9-mZ4d4jBExo5Fky_G815PODerNVJ5BKBIbPeDa5vXLfh6Wfgiw9iqGxLOMOB8SFauT8HeVsLasjTYzEofu2JXI_dhIsNqR0w-qIwpwNjchoTU4YeMpNPcCZbwJiL28K-_tIXEgnvlEiHuwMUxwgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه افزایش نرخ ارز در ایران، قیمت پوند بریتانیا پنج‌شنبه ۱۲ شهریور در بازار آزاد برای نخستین بار از مرز ۳۰۰ هزار تومان عبور کرد و تا زمان تنظیم این گزارش به ۳۰۰ هزار و ۲۸۰ تومان رسید.
در همین حال، دلار در بازار آزاد با قیمت بیش از ۲۲۲ هزار تومان معامله شد و قیمت یورو نیز از ۲۵۸ هزار تومان عبور کرد.
قیمت سکه امامی نیز از ۲۳۵ میلیون تومان عبور کرد و نیم‌سکه به ۱۲۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78202" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rL28gbSmlb8uM-CSXWwoLfcczn-OIUWM2hsaFqV9QFrSPuVBpnT_GJw1bcWfdcHOQDkBGlQ52L7S6LePcnSYYxS_5fAcUMzFNyEIqhtjvUHzVzOZWST6fQOQPP-xpNO73rmXGQcv8zakjd1nz7nyIQk5I_S82g11PNSJZb2C_p3O2dVVL2vg7tjBM1uHrjA7XJexUiDvVWjDulRhGaTVcheZ2rRKDf9Sb6z-OHUs0RJ15bbt-b76kRpik55Tz39ZZ3JstfmFPgc5ah82QR1tYxqwzb7gaXsL0Ca9JnGdByIE-L5fzvw0gV7aoVR-8DGvXHJI2QAdulxxSul4BKwhQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور حکم ۱۲ سال و شش ماه و یک روز حبس، مصادره تمامی اموال و دو سال محرومیت از کافه‌داری برای صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای «ساعدی‌نیا»، را تایید کرده است.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ اعلام کرد این حکم به‌دلیل حمایت ساعدی‌نیا از اعتراضات دی‌ماه ۱۴۰۴ و تعطیل‌کردن واحدهای صنفی زیر مجموعه این برند صادر شده است.
براساس اعلام قوه قضاییه، صادق ساعدی‌نیا به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به ۱۲ سال و شش ماه و یک روز حبس تعزیری و مصادره تمامی اموال منقول و غیرمنقول خود به نفع دولت محکوم شده است.
دادگاه همچنین او را پس از پایان دوران حبس، به دو سال محرومیت از فعالیت در حرفه کافه‌داری محکوم کرده است.
قوه قضاییه انتشار مطالب اعتراضی در اینستاگرام، حمایت از فراخوان‌ها، تعطیل‌کردن کافه‌ها و فروشگاه‌های مجموعه و تشویق کارکنان به شرکت در اعتراضات را از مصادیق اتهامات او اعلام کرده است.
براساس کیفرخواست، صادق ساعدی‌نیا با سه عنوان اتهامی شامل «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های مخالف جمهوری اسلامی» و «فعالیت تبلیغی علیه نظام» محاکمه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78201" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geJPll6trN8T2_-c6O6edppE5oeqlzfhG9avRvmQBtV3pX7fedQqMfkO375MQGTthOX3lKCUmDi03tyti2D5e3L5b2B8NWCkS2_jAoioJmucmgCr9zHAGf83y2td_egRnS-lhyzugwvQY80XkurjsG3IkzN7xxtcSBTeGAAYpxf5tOXXjlgmk0J437KOib4WorQ3gwFRaJvy34KQ9GCnkTuzkDMLhKhPJaJHMh_J3HMJJSQJaaN65gbRQxFhGMpfeEtBHoxd8USgNiS773BCFq6mMxvm7-D5sPWqnQNBx_uEUpDmqLhSyV4n5keC_SYTHwAaqbY7j9HnNTMR4wluVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sABx4B4UiygK8KlsICRPTzySNOViGxBnPj_ilmEFGQxne1SGj87XORpaQ52suAFY6EcDxp57isqrNVCU79WdzGQioeq07CajetT0WvsYfR4aCYWViFfw2RMYzc6CuyCKmex53tOCboJQLK4sUzZZvK9FYnvvyyruGbHZAD8jYgKB9pI1oHJ5yG45toPKCVGHoCCnGlaAX9s6uXM7mTV40j_lFfo6Hu8ZP0fcHR4rjFzx_B54IAr68Hg2_uB5rG9yyrx0uMEwUtpPbSEoyAHhOCTqtfnuC-TatjAceYfcrcMSBd2au7BivsvM2MMeV2M2CRuZSkBWGDasnzGUxaJLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=ja9nH5rMAZobUxg920cDJs-0evzVSwt71-oHc8d2pMMB1Qdv8bLkk2TDpGqStkbFFb8qs4XHGvig_unNa-CnYA4dRfX5FFBSQeWGv5LCNqwUJs4iUG_cxeLpGZ5zWctZ_w5vJPVOcjIAVJHdWL3qVGigCM3-AcXOZAvjjzhflTW1E930nWAoDFJIZZ5cB2py02S_QepbLQPx0aa0kE_LhYoAz6W6xrKbd4Ljx15CWA9jyI3izEdMJE13OTwZtwkCqnbCuT18NvINI1Jz38a-YkjCIQNw1kSB8mkVDd19aFExsg7_6lKLIJW2lbGFNHM2EEyImTXndXVhyoU9IdWmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=ja9nH5rMAZobUxg920cDJs-0evzVSwt71-oHc8d2pMMB1Qdv8bLkk2TDpGqStkbFFb8qs4XHGvig_unNa-CnYA4dRfX5FFBSQeWGv5LCNqwUJs4iUG_cxeLpGZ5zWctZ_w5vJPVOcjIAVJHdWL3qVGigCM3-AcXOZAvjjzhflTW1E930nWAoDFJIZZ5cB2py02S_QepbLQPx0aa0kE_LhYoAz6W6xrKbd4Ljx15CWA9jyI3izEdMJE13OTwZtwkCqnbCuT18NvINI1Jz38a-YkjCIQNw1kSB8mkVDd19aFExsg7_6lKLIJW2lbGFNHM2EEyImTXndXVhyoU9IdWmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفت.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
آپدیت:
حال‌وش روز چهارشنبه ۱۱ شهریور ۱۴۰۵، به نقل از شماری از شاهدان محلی خبر داد که پیش از انفجار، صدای دو پهپاد در منطقه شنیده شده است.
این رسانه، علی ملاحی، صاحب خانه و پدر عروس، را یکی از شاهدان معرفی کرده است. او گفته پیش از وقوع انفجار صدای دو پهپاد را شنیده و پس از آن، ساختمان هدف قرار گرفته است.
شماری دیگر از ساکنان کوهستک نیز از مشاهده یک پهپاد یا شنیدن صدای آن خبر داده‌اند.
منابع محلی همچنین می‌گویند خسارت‌های واردشده به خانه تنها ناشی از ترکش انفجار در یک محل دیگر نبوده و یک یا چند پرتابه مستقیما به ساختمان اصابت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=fxEA9Iy7s7JufIXVqzS_C-aTKA2Mem8v4vVGDeEv2ARfnsdYtK78jRQ9PgX2hlk56iglNqH6__bPIiJpH3ulvdf8-j_xdw83q7IRgDDKQc66e4ST_ns8h-I2Irvptt467D1g6mP2ludD9s8L6wiyagIA9lnQgpnBEKQCcFdqUACXjjXXaeEiV2vXCC85j8N5nZV7zzfu6ciF27sPuVOKdz_DhoqyYGmDEP0g8FL8r1K02RazP7dlzZ1u8PM9hXBeSiISjRzu4AOijSUdHej3ah79XfMwaJxfKzjZnvj3Jd8XkwLBWnLx3TZN0BjPME-F80Gfc6vXBJdp4X79NT-A-3z5DFGBo6Af4XXp8b4MFbHjWZJjnh6_j_v4iQhQd-sezIHIX5aOvZDTuFRqVzJmqSHiyVl2Lu3W2LV9eeB5DpBukaJP9Uhq2l0etsKRWR_FTU93PPe61Hc0S3Itd_dB3e28_lroz5ukAyD2Sb-5GO7k8yjpx1I6XFPzJu05CAq8CDhoPRDQzQ60UdGfn3H6-rCkH7RYn_IUiTa-TXptRsUkAYT-1HfcQcmpOnHaSEYJMPz6J9LmeCZSyyNT97Gfeh1DPvhBS3teDH5smqz_BDnJVmdD7cnlQALRG4r99zC67IElivXsNmpUP4yT8YJNC27rhAz_6s99leVY9sdXqgY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=fxEA9Iy7s7JufIXVqzS_C-aTKA2Mem8v4vVGDeEv2ARfnsdYtK78jRQ9PgX2hlk56iglNqH6__bPIiJpH3ulvdf8-j_xdw83q7IRgDDKQc66e4ST_ns8h-I2Irvptt467D1g6mP2ludD9s8L6wiyagIA9lnQgpnBEKQCcFdqUACXjjXXaeEiV2vXCC85j8N5nZV7zzfu6ciF27sPuVOKdz_DhoqyYGmDEP0g8FL8r1K02RazP7dlzZ1u8PM9hXBeSiISjRzu4AOijSUdHej3ah79XfMwaJxfKzjZnvj3Jd8XkwLBWnLx3TZN0BjPME-F80Gfc6vXBJdp4X79NT-A-3z5DFGBo6Af4XXp8b4MFbHjWZJjnh6_j_v4iQhQd-sezIHIX5aOvZDTuFRqVzJmqSHiyVl2Lu3W2LV9eeB5DpBukaJP9Uhq2l0etsKRWR_FTU93PPe61Hc0S3Itd_dB3e28_lroz5ukAyD2Sb-5GO7k8yjpx1I6XFPzJu05CAq8CDhoPRDQzQ60UdGfn3H6-rCkH7RYn_IUiTa-TXptRsUkAYT-1HfcQcmpOnHaSEYJMPz6J9LmeCZSyyNT97Gfeh1DPvhBS3teDH5smqz_BDnJVmdD7cnlQALRG4r99zC67IElivXsNmpUP4yT8YJNC27rhAz_6s99leVY9sdXqgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=NoPwapgwK3c2Gv0TPLSMHygIJ3ayjTSyVhqU5gsucZveH7x9IG52N1JWnFOL0n6ExniE-cGHb9P9WIhIhzc-S-X1pJ9O2GR8Rnk2aAVrf5CdjhTNc7eYRF39lpXEzZUruo3eiRuNFxng3cIbupFWdNggA_i-eHrKWteqd8rDhHExpMcxd5jkT4F-TDhZLHwEMTCVkLU60hWus-qVFgjExGVnrtMTHtZxkOz6AJp_XzffXCDnfpkjkUpFRrX3g3AzSQUxYtlvswAOV7ftGAHyx00_kMZB8wGo5jHj2EDXwr6sm5jIzN-fK9LcJhtXWEwufrfeAUZIJFH2p5zwa0JUbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=NoPwapgwK3c2Gv0TPLSMHygIJ3ayjTSyVhqU5gsucZveH7x9IG52N1JWnFOL0n6ExniE-cGHb9P9WIhIhzc-S-X1pJ9O2GR8Rnk2aAVrf5CdjhTNc7eYRF39lpXEzZUruo3eiRuNFxng3cIbupFWdNggA_i-eHrKWteqd8rDhHExpMcxd5jkT4F-TDhZLHwEMTCVkLU60hWus-qVFgjExGVnrtMTHtZxkOz6AJp_XzffXCDnfpkjkUpFRrX3g3AzSQUxYtlvswAOV7ftGAHyx00_kMZB8wGo5jHj2EDXwr6sm5jIzN-fK9LcJhtXWEwufrfeAUZIJFH2p5zwa0JUbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، و دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، روز چهارشنبه توافقی نفتی را در کاراکاس امضا کردند که بر اساس آن ایالات متحده کنترل اکثریتی بر ۶۵ میلیارد بشکه از ذخایر نفت ونزوئلا به دست می‌آورد.
این میزان حدود یک‌پنجم ذخایر عظیم نفتی ونزوئلا را شامل می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، این توافق را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده است.
بر اساس این توافق، آمریکا به ۱۷ میدان نفتی ونزوئلا دسترسی ترجیحی خواهد داشت؛ تأسیساتی که برخی از آنها پیشتر در اختیار شرکت‌های روسی و چینی بوده‌اند.
همزمان، شرکت شورون نیز از توافق جداگانه‌ای به ارزش هفت میلیارد دلار برای توسعه دو میدان نفتی دیگر در کمربند اورینوکو خبر داده است. شورون می‌گوید این سرمایه‌گذاری می‌تواند تولیدش در ونزوئلا را طی پنج سال بیش از دو برابر کند.
وزیر انرژی آمریکا پیش‌بینی کرده است تولید نفت ونزوئلا تا پایان دهه جاری به بیش از دو میلیون بشکه در روز برسد؛ حدود دو برابر سطح تولید در ژانویه، زمانی که نیروهای آمریکایی نیکلاس مادورو را سرنگون کردند و دلسی رودریگز قدرت را در دست گرفت.
این توافق با انتقادهایی نیز روبه‌رو شده و منتقدان دولت رودریگز را به واگذاری حاکمیت ونزوئلا بر منابع نفتی خود متهم کرده‌اند. دولت ونزوئلا در مقابل می‌گوید این توافق به این کشور برای بهره‌برداری از ظرفیت‌های انرژی و جذب سرمایه‌گذاری کمک خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78195" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVXaocbOCQgIx8q5YCv2O2CAIFBQEvu7bQxSTblPkWIbaWAslDLv8bi0p9mp_VNzhM77zISJXjY_jpOhXBLF7NFZ7aoFcpoNTLMLLDjXHMCPvygBL3NHZp50FIZEqhgihrR41cTClGQANFgovHW9mlwfCqfqC2CbE2Mkih67VwLmAQ5AKQ4f-FJnt7J64e26kSye_l11IQ4G6jpaK8SAlgHQf8lQo69W_P8Z9vf8FoEcD8L_wDn4AHVORWDJ7nB8avTf-B43rt-8xd4oD0d0-BCN7EoCAXpp7bBsbY8X5n843p56PXCuYNToSgOrv8p21z1_Ako-N8Ii0tJvwf_Bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=jpZ0GuyYKk9PiMuYj4lDeFmFgMXpLzqD0J27WvEK4AMtdqq_qPgjGRy-LfdwvGNiOZSpxDbn8ryiQw9FkT0IJ6Xz0v2tjENfEEzAHZB3zQ4i2SDRX-5ubmp6SUgw9P634AR6L70l7yVSTWYtEzutp2hjKhue634eimUpLsH4BmB09ZfNTiw7PL-618Q_52XUth9rYYs6qjlI5ih3I65GnKzsKv9UkDkpj96PbemqmiS56iU-p__gq8dgbIoR7sP9hWtW0yqOJ5EfBqv_rE-8ZizMASjv2Qkbz6u3ojwR49fu1qKDUIcAqc5DmXClr2PL1edo2NjYEAM0bZ-VxwyqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=jpZ0GuyYKk9PiMuYj4lDeFmFgMXpLzqD0J27WvEK4AMtdqq_qPgjGRy-LfdwvGNiOZSpxDbn8ryiQw9FkT0IJ6Xz0v2tjENfEEzAHZB3zQ4i2SDRX-5ubmp6SUgw9P634AR6L70l7yVSTWYtEzutp2hjKhue634eimUpLsH4BmB09ZfNTiw7PL-618Q_52XUth9rYYs6qjlI5ih3I65GnKzsKv9UkDkpj96PbemqmiS56iU-p__gq8dgbIoR7sP9hWtW0yqOJ5EfBqv_rE-8ZizMASjv2Qkbz6u3ojwR49fu1qKDUIcAqc5DmXClr2PL1edo2NjYEAM0bZ-VxwyqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با شبکه نیوزمکس گفت که ایالات متحده لزوما به دنبال فروپاشی جمهوری اسلامی ایران نیست، هرچند تحولات درونی و قیام مردم امکان‌پذیر است.
او همچنین به مخاطرات شخصی پیش‌روی رهبران و فرماندهان نظامی ایران با افزایش فشارها اشاره کرد.
بسنت ادعاهای ایران درباره کنترل بر تنگه هرمز را رد کرد و گفت با عبور حدود ۱۷ میلیون بشکه نفت در روز گذشته، کنترل ایران بر این تنگه بی‌معناست. او همچنین گزارش‌ها درباره وجود مین یا برخورد دو کشتی با مین در تنگه هرمز را تکذیب کرد و رسانه‌ها را به بازنشر سریع ادعاهای نادرست ایران متهم ساخت.
وزیر خزانه‌داری آمریکا، با اشاره به تداوم خرید نفت ایران توسط چین تاکید کرد که تنها حدود ۳۰ میلیون بشکه نفت ایران روی آب باقی مانده و این ذخایر نیز به‌زودی به پایان خواهد رسید.
بسنت روز گذشته نیز در جریان سخنرانی در مجمع اقتصادی جی۲۰، تاکید کرده بود که فشارهای اقتصادی یا به ایجاد شکاف و دودستگی در سپاه پاسداران و احتمالا مقابله مردم با آن‌ها منجر می‌شود یا مقام‌های تهران تصمیم می‌گیرند که به میز مذاکره بازگردند.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با شبکه آی‌۲۴ درباره حکومت ایران گفت: «نیروهای ما می‌توانند هر لحظه در آنجا باشند. ما این حکومت را شکست خواهیم داد.»
نتانیاهو درباره اینکه آیا منظور او از شکست دادن، سقوط کردن حکومت است، گفت: «بله، سقوط خواهد کرد و ما آن را سرنگون می‌کنیم.»
نتانیاهو در پاسخ به این سوال که آیا رومان گوفمن، رییس موساد، برای سرنگونی جمهوری اسلامی فعالیت می‌کند، گفت: «همه دستگاه‌های ما تحت هدایت من برای سرنگونی این حکومت و شکست آن فعالیت می‌کنند.»
نتانیاهو گفت: «در نهایت با سر اختاپوس، برخورد خواهیم کرد، بازوها را قطع خواهیم کرد و محور شر ایران را هدف قرار خواهیم داد. این کار را با قدرت بسیار انجام دادیم؛ خلبانان ما آنجا بودند و هر لحظه می‌توانند آن جا باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78193" target="_blank">📅 21:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqCi118eKev9jkkTzNGNJ7sKHfasxn_bLf0wJxYgpPi99y1xt0qfXzFEUF20ss6wTIBXXRLTDKzOCAXbH7v8LTThHcxID0J39Q9JTUcrB4BoQqOqfG3s8Nnc4nb4znUPo8q5TZlEIAnlqUYL-Dm80RNMfANmbL4Vg44F2RJmFY5renfaQMTod0UuoA-LRhwbHSizaVBLpC7qBoQBwRXn7W85Wyp2ceIAdq_mz_h0Z2PAOntu9ruU_NmE5cXpIQ2O_oejrFJXVaOZL5GMekHOlfh2VKGZAAyRCp256tNmnGhMHn5xhr8by6JVUBx9qHRY7WU6HlLNgLnRdVkwtXnGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی جمهوری اسلامی، با هشدار به ایالات متحده گفت تهران در جنگ جاری از «راهبردی جدید» استفاده خواهد کرد.
رضایی، چهارشنبه ۱۱ شهریور ۱۴۰۵، در پستی در ایکس نوشت که تلاش‌های آمریکا برای خروج از شرایط کنونی نتیجه‌ای نخواهد داشت و افزود: «به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، پایه‌های شما را درهم خواهد شکست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78192" target="_blank">📅 19:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HmwwNdD0IPxTzI9QSF7xfq46k7tGCDOdF_L_OSts8cdeMynY3Lv-Vua3V2jeSIxdzzpirOsIi8Z3pcwdHNnkYo4AuNqZNRoCh7T9vivW4mM0K5nDyX7Gpm2rbofSk7-NKld604Z_4F9d9sQ3SbHofbdH2Nxo-AyAcVoDE0FqjVGPt0p8BCMSaglqkb2sdwNBqIIOZohit1xtlegmvQtJrG_ykgymz6RnCXkHAUOtq1vxvzD97FnFUxcoAiyev3UsC2lGedfXDJKiP9Xk0reNlaSHMRhkuTFr8sMlk6KYfAT7Zu3bHVPeTyms9DdgzfJc8f7sgMQiKDVNen147MTA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حالا که آن را تحت کنترل ایالات متحده آمریکا درآورده‌ایم، آیا باید نام «تنگه هرمز» را به «تنگه ترامپ» تغییر دهیم؟؟؟ درست مثل خود آمریکا، این تنگه هم «داغ‌تر» از هر زمان دیگری خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
Now that we have it under U.S.A. control, should we change the name Hormuz Strait to TRUMP STRAIT??? Like America itself, it would be “hotter” than ever before! Thank you for your attention to this matter. President DONALD J. TRUMP
realDonaldTrump
در خبری دیگر:
ترامپ در گفت‌وگو با پادکست «دن پاتریک»، درباره حملات سه‌شنبه شب آمریکا در اطراف تنگه هرمز، گفت: «ما اکنون کنترل تنگه هرمز را در اختیار داریم. ما آن را کنترل می‌کنیم. دیشب ۲۸ کشتی را از بین بردیم. ما آن را کنترل می‌کنیم، آنها چیزی دریافت نمی‌کنند و ما کشتی‌ها را از بین بردیم.»
ترامپ همچنین درباره حکومت ایران گفت که جمهوری اسلامی دو هفته با داشتن یک سلاح هسته‌ای فاصله داشت. او افزود: «اگر آنها سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت، خاورمیانه از بین می‌رفت و آنها به شهرهای ایالات متحده حمله می‌کردند. چون آنها دیوانه هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78191" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAy6zwP4SuF-h2cblUdiYnAj4BkS3NeJJMYJ7KNEsJ5B0kOCRReUxg8v6f1qlSBuRQUv54gyRm4QU1BwpM6g2aDCUDMRcT5tqmN4H9uTA29Zi1Jkxhm9bmVFSStc2g06ImZLBJLdJKQ5lArUAtG6an5G0qFk0-b1J8UVvIDI-1VPXEbAXc7yrWG7bzIhRTGofpbb25O0meOMxrERrm2tIz6IMIYsalzU1SSuk35UWgXKBS79_ccjR7SSHYY0RNjz0ETm_cG6QAXIclpzsunRdlMHkEg7_76MwHPKFSufbgFGt74IQteKemGLkcRw0exZI5Nyp3NOWoWFUp0d-p4e4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی گفت: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
محمدباقر قالیباف، در دیدار با مسئول ارتباطات اسلامی حماس گفت جمهوری اسلامی مذاکره را رد نمی‌کند، اما آن را «ابزاری برای مبارزه» می‌داند.
او گفت کنار گذاشتن مبارزه با آمریکا و اسرائیل به معنای شکست است.
او افزود جمهوری اسلامی در جریان مذاکرات، پایان جنگ علیه ایران و متحدانش در «جبهه مقاومت» را در ماده نخست تفاهم‌نامه مطرح کرد، در حالی که به گفته او، طرف مقابل در متن اولیه ۱۵ ماده‌ای خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و فعالیت‌های «جبهه مقاومت» شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78190" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFdIcJWFKBPvuqqgFHfO7yQ_6VAVmt_e8nfC7xv7wpuCC1I6qWMHbt0MrL82hnRJplYX1yWixdpEJGGykUTHBVJcXmu6IA030dc29mmM5N-bDFXbuHyJhZIeoWsUFdT5zzPexJphXCBev8v_a9kDU5k_ZUHQ5d-gR3rc07y18bY6fhlYJvNm-7fKI9ZcQHAB22a82BWZMbXZ8tYoldLDgnHm61NAiCdBluliqfFyhmh9KhQXlb3f2WvipV1ZqCQ_nRRuyDtmnLu4tyK0sdLah5HB_b9dQQudungW8rQUWDx_m29zP3aZjhsqH12ULuFwDvlwqbyDhJZBoEKL2c1foQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آمارهای اعلام شده از سوی شرکت ملی پخش فرآورده‌های نفتی ایران، میانگین مصرف روزانۀ بنزین در نخستین هفتۀ شهریورماه از مرز ۱۴۸ میلیون لیتر گذشته است.
بر اساس این آمارها، بیشترین میزان تقاضای روزانه در ۸ روز نخست آخرین‌ماه تابستان، بیش از ۱۵۴ میلیون لیتر بوده و در این بازه در مجموع بیش از یک میلیارد و ۲۰۰ میلیون لیتر بنزین عرضه شده است.
کاهش شدید ظرفیت تولید در ماه‌های اخیر در اثر حملات آمریکا به تأسیسات نفتی ایران از یک‌سو و مشکلات دولت برای وارد کردن بنزین از سایر کشورها از سوی دیگر، باعث افزایش قیمت بنزین و حتی مطرح شدن احتمال بالاتر رفتن قیمت این فراورده و افزایش شدید تقاضا برای آن شده است.
مسعود پزشکیان رئیس‌جمهور و شماری دیگر از مقام‌ها تأکید کرده‌اند که دولت توان چندانی برای وارد کردن بنزین و بخصوص عرضۀ آن با قیمت‌های قبلی ندارد.
دولت ایران اما در عین حال ادعا می‌کند که تشکیل صف در برخی جایگاه‌های عرضۀ بنزین، ناشی از هیجان و بار روانی بوده و مشکلی در تأمین بنزین مورد نیاز کشور وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78189" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IlVyu0YdsfduSPEbfrMNiNZEmor4OnTAx1xinKzE57s0qRbF0EhPQYN_wUuoYOTR09LqHqvCKUvQzKY_yvM6PYcahq9h84ztsecU56SYmL8byvDYXOz7x-PqdjhfWbx-RDckmR2FGrfBdswUy-4kSy7vEDhcKsghroTaHeFwC8zVljotUFdc-0jFoeggNINrmeeddNxpQ8y1F3xQ0Y2MVnRsQtHdiFtwqiC9YrHUY_Z7IUzK-ssPBJUql_LxZR1uPNwauv2vsk1wzfZMTH9sa-T9I3Wik1Aqa3V55yYCEOyKgOaUWc4ppJVLhGruWpcjOXFY-Pdsef5fYaz0rcTm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در ایران بامداد چهارشنبه ۱۱ شهریور و ساعاتی پس از دور جدید حملات آمریکا، رکورد تازه‌ای ثبت کرد و قیمت یورو، پول واحد اروپایی، برای نخستین بار از مرز ۲۵۵ هزار تومان گذشت.
وب‌سایت‌های اعلام نرخ ارز قیمت دلار از جمله «نوسان»، قیمت دلار آمریکا را حدود ۲۲۰ هزار تومان گزارش کردند. قیمت درهم امارات هم به بیش از ۶۰ هزار تومان رسیده است.
افزایش قیمت نرخ ارزهای خارجی در بازار آزاد ایران از زمان اعلام امارات در قطع روابط مالی با ایران و آغاز برنامهٔ فشار اقتصادی آمریکا موسوم به «عملیات طرد اقتصادی» شدت گرفته است.
در دو هفته اخیر پول ملی ایران در مقابل ارزهای عمده خارجی بیش از ۱۰ درصد دیگر از ارزش خود را از دست داده است.
روز چهارشنبه قیمت سکه طلای موسوم به «امامی» هم با وجود کاهش جهانی قیمت طلا، ۲۲۴ میلیون تومان گزارش شد.
عبدالناصر همتی، رئیس‌کل بانک مرکزی، روز ۱۰ شهریور ادعای کمبود منابع ارزی و احتمال فروپاشی اقتصاد ایران را رد کرد و گفت بانک مرکزی آماده است برای مهار بازار تا دو میلیارد دلار ارز عرضه کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78188" target="_blank">📅 16:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZMdUl6TjYr7ieuFZHhZc9i_jSufYjpMEtVzaZBKHDCAyiQq_prapHtkmukBgrJd4WPHQ6eSyqXBKMQ4-Hz3FtVYuVSrbm50CSKt3DxbyMGH06JR95kgRAVL3r4_gPLzkR7S7kpuyKP486TBKQfDfCYKLKkRXkPMoNx_lQzw8wQj_6WHIMZj0vnnpro3NMp0GEKgN3rDnwvlNHbfUKX6Hc6KquCxKRhNzYy-9Up2z_oWH048YQIeVbWGRBpOJCNET4iICH2gISWI3TyrJgiAOam_v6c-Bl7YDCEYc4Y5oO-ZNlDUBNoQHs5mFYB-0P81870O_ypSC0DeRrr5dRqlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد که ارتش ایالات متحده در جریان موج حملات شامگاه سه‌شنبه دهم شهریور به اهدافی در جنوب ایران، «دو نفتکش دولتی» این کشور را نیز هدف قرار داده است.
بر اساس این گزارش، این دو نفتکش در نزدیکی سواحل ایران و در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند و پهپادهای آمریکایی با شلیک موشک موتورخانه‌های آن‌ها را هدف قرار دادند.
فرماندهی مرکزی ارتش آمریکا، سنتکام، در بیانیهٔ رسمی خود پس از حملات سه‌شنبه‌شب اشارهٔ مشخصی به حمله به نفتکش‌ها نکرد، اما در تصاویر ویدئویی که از حملات منتشر کرد، صحنه‌ای از اصابت موشک به نفتکش نیز دیده می‌شود.
اکسیوس می‌گوید این نخستین بار است که ارتش آمریکا نفتکش‌های ایرانی را نه برای جلوگیری از نقض محاصره دریایی، بلکه در واکنش به حملات ایران به کشتی‌های عبوری از تنگه هرمز هدف قرار می‌دهد.
یک مقام آمریکایی این اقدام را بخشی از سیاست تازه‌ای موسوم به «نفتکش در برابر نفتکش» توصیف کرده که به‌گفتۀ او دونالد ترامپ برای بازدارندگی از حملات بیشتر ایران به کشتی‌ها تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78187" target="_blank">📅 16:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0TXkUTysQYpp6tDBjX5KdHS363xP4Oa5Uu8XrxzEl92xKVxrheBScMpsN4BaoXaOyoJYJC5vKWh08r6wAzRRRP-CKyLGMlTntQSdGhPqioc85gu4y9oaQQSWjbjtx4TRmgL3GV_bfKVz2AMcq4XD0sWZxGkPpD4av789Evsw8vP97Klbt0R2aWCJrvJogvVwErwnKEqDDZqsdE_IVTKHyRRAO9KVBPNaAr06qw-IT8q_BY1DImSMZVJKpiDY4KfXIPyLv6KS8_gCOU6MJbZZ29C-HEeE_eBqqTjJ-gahbGhrxpXxAK5CqPLqRVJXt1hHq6Zz5MKMcVMM62qJ2u9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fm2gOg19vDB-R1AAQbHIgvuUJO7hCOTpZS1_jHHZkQQxKGNI4wZZHlrKfvPETQyDzEhM_cSE8BM0pzAxlaZEF7_XW5ikdVbDPSaiUplps5neIVyyoGtuhNnxSPm7NRAsz2HJivT69JYHAu3SWPLeKFKwD3Yhxw-MsH1GGiKp4U9rVqCy36eRiI1RL3IuOS1Wm-WkZHkShfEP0GOHBycDMeBLiCJIBfGp4kFlc3L-ITjotiLStQAEisTm8zaHJyH2ewWt-bJNsaaCHyqAb-46RHApaG4MB27VfmjFCsLlS4PqkOllBcrNzrw1MnTSCG-qRKLvwEtC6opvNf2rPDYtxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=LmRV_BNTfBmsenj330UOtm9osYwYSSIr77TgsZHSpvsRH67iNuMtQB9dCrUjc2QqxkkbIfZ4VRvpAP5B1a8W5NEai90mGJuEMK9JqHnRYkgWwaKw02jYR145tPEroyH1AnnbfkPi5xVgpMACVe_p4HYNMLul6uClAo2E-9r1bLVAinEOCs4z9ENs2_agXZGnqMqSUAm0X7cVMx5di0pO6l3XV1LxAaBqgJIbHn0p8f1TcRvvQjWPwMd1HCzD8cVm1qIh1zd15xsUiyIQPexXXEPmDjr2myRql7BybWwVHj12DDF3D4VKhpESIj9ZQRPDRePLRP5ObVEJg0P9nVHeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=LmRV_BNTfBmsenj330UOtm9osYwYSSIr77TgsZHSpvsRH67iNuMtQB9dCrUjc2QqxkkbIfZ4VRvpAP5B1a8W5NEai90mGJuEMK9JqHnRYkgWwaKw02jYR145tPEroyH1AnnbfkPi5xVgpMACVe_p4HYNMLul6uClAo2E-9r1bLVAinEOCs4z9ENs2_agXZGnqMqSUAm0X7cVMx5di0pO6l3XV1LxAaBqgJIbHn0p8f1TcRvvQjWPwMd1HCzD8cVm1qIh1zd15xsUiyIQPexXXEPmDjr2myRql7BybWwVHj12DDF3D4VKhpESIj9ZQRPDRePLRP5ObVEJg0P9nVHeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح چهارشنبه؛ وضعیت چند منزل مسکونی در کوهستک (هرمزگان).
@iliaen</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78183" target="_blank">📅 09:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05113c6026.mp4?token=nqn6lnuCpLnct1D61pYwYBx-sVDydkoYpMIgG5BI3yr5-yNuJt2dWkU3rTKWz-WoBQQjN_m5md_kgQzoa6ww3usKgPo6OJxS132EaodjpxRjwGcVSm3etReArRQ0boL0tGMVF5m-XJiQGvP2hLwyuo9_If5g8yWn7hh1X5HH1v0qkZU36ohY5ouyY63OPFUJDLs3FEp6rMUaYboNLjW55u3Iox_SBrjq9IGpuZDjlHYuA_HuAyieePRSZo9crQyfFFlA6n9YlDk1tLNQhLy8ZLCxRwzT7_CGkdYbjqL7dUeA16hQDlL4FVCN7xmwdHtJh_PSTBho8a0_MvmMCR6Avw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05113c6026.mp4?token=nqn6lnuCpLnct1D61pYwYBx-sVDydkoYpMIgG5BI3yr5-yNuJt2dWkU3rTKWz-WoBQQjN_m5md_kgQzoa6ww3usKgPo6OJxS132EaodjpxRjwGcVSm3etReArRQ0boL0tGMVF5m-XJiQGvP2hLwyuo9_If5g8yWn7hh1X5HH1v0qkZU36ohY5ouyY63OPFUJDLs3FEp6rMUaYboNLjW55u3Iox_SBrjq9IGpuZDjlHYuA_HuAyieePRSZo9crQyfFFlA6n9YlDk1tLNQhLy8ZLCxRwzT7_CGkdYbjqL7dUeA16hQDlL4FVCN7xmwdHtJh_PSTBho8a0_MvmMCR6Avw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روستای کوهستک در سیریک هرمزگان
ویدیوی منتشر شده در منابع حکومتی از مکانی که مورد حمله هوایی آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78182" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tWgIKE1S720ZA7vqxgTPbRpXev7prVIJMwnZdygvnG04pBIuAJSSxR3CNHQx7jn-UuzDB0KDu5n84AFNl__ocaBzJHUpm_BQJ7-mdvgeCeUju_9vLhpBsb-w6cpRwPAidUWjbsCoOq5AwGr1FffrhE92n0h1U7YziVY4YqTy-yz9XjIvRdx5e5191zj6wauwlLyAD5rMEyVpET3POdI-hIAZOTOOqhixAxuVAlfsyC2hSPm2KYCHrv2hEEk4tH-CmTzFDtbbR9XhQn5reJYbZE91195f3GzS_jDeXzjhzLLcz7aC79pgVeAzAtqivMdql_jynULRLHE_eNNMCuO9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من تلاش نمی‌کنم ایران را، آن‌طور که ABC Fake News گزارش داده، به پای میز مذاکره بکشانم.
اصلاً برایم مهم نیست که آن‌ها توافقی امضا کنند که برای خودشان هم ارزشی ندارد.
من موقعیت فعلی‌مان را خیلی بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در ایران کاملاً در حال فروپاشی است.
آن‌ها فقط دارند روند اجتناب‌ناپذیر را طی می‌کنند.
مردم ایران چه زمانی به پا خواهند خاست و خواهند جنگید؟
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/78181" target="_blank">📅 04:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=C3xDqYCxBx3f9B4_-Mi-YLHvEdFWeV9AXh7_rQTdXFUuUF8Mx9nnRKub_vMatPUXME9GFZmSW7RGzZF4uE_nwbIzPYJhOzdZO8MZz7twYynE-9ymCr57Bql4g_gbHeqWE5iJF1LvO7E2g79r1HNmZvjZp5893uclj6GyeAgf1cxmOtz0L2Sl3C3dx1xmG6SOG8Q5TYcnI2u4wl4TnkakxRfvl977mTRrvgjS_HVE1yxGASoemFj3UFuKdFW6BQuDg0LrEqtF0Rpg-APffGZVxTAzuj3m15nDS-Xw375Sp0GCYCwqiukrMnT_YzFLVl5763Pj0lO7XBmbYKFysVBfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=C3xDqYCxBx3f9B4_-Mi-YLHvEdFWeV9AXh7_rQTdXFUuUF8Mx9nnRKub_vMatPUXME9GFZmSW7RGzZF4uE_nwbIzPYJhOzdZO8MZz7twYynE-9ymCr57Bql4g_gbHeqWE5iJF1LvO7E2g79r1HNmZvjZp5893uclj6GyeAgf1cxmOtz0L2Sl3C3dx1xmG6SOG8Q5TYcnI2u4wl4TnkakxRfvl977mTRrvgjS_HVE1yxGASoemFj3UFuKdFW6BQuDg0LrEqtF0Rpg-APffGZVxTAzuj3m15nDS-Xw375Sp0GCYCwqiukrMnT_YzFLVl5763Pj0lO7XBmbYKFysVBfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شروط پکن برای سفر قالیباف به چین'
حسین مرعشی، دبیرکل "حزب کارگزاران سازندگی"، گفت: خیلی روشن به ما گفته‌اند که
۱- تنگه هرمز را باز می‌کنید
۲- عوارض نمی‌گیرید
۳- با عربستان سعودی مسئله‌تان را حل می‌کنید
۴-  با آمریکا مسئله‌تان را حل می‌کنید
بعد قالیباف به چین بیاید.
قالیباف در اردیبهشت سال جاری، با پیشنهاد مسعود پزشکیان و تایید رهبر جمهوری اسلامی به عنوان «نماینده ویژه ایران در امور چین» منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/78180" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">منابع حکومتی:
روابط عمومی سپاه:
🔹
مردم شریف و انقلابی اردن؛ یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن، اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78179" target="_blank">📅 02:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=YXrq98VRfEsfVMveygxDZl5WMEfZaG1IV4-bNyiN1qa7n3T2UwxsOK2jEm0CfD3OwFi0xuXF7kPbqVR0VbHFjSm2F-YPp6V0nGzCUbMSKwG1_2bGszRu9OsTNty8y6Mu2TLnhXYW4jmwscxb7qmWPGJPEMhQxYMuWaQhZrpi3Gt1HYgjBv6_i8UK1su2TqQ6Wp2_jWMEloWDATPQAOeIiBHqt8Z4twjkGll8vWHZ_IYD2YF0nht1U_uJYNfSFFoNvJktevOTG6kGBfH-wY8ehK402LgfLPKRjq9rqlx8MpcUcge-AaNRbngbqRTzKyoytc8r-FfnZ5p69G9WFw0aBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=YXrq98VRfEsfVMveygxDZl5WMEfZaG1IV4-bNyiN1qa7n3T2UwxsOK2jEm0CfD3OwFi0xuXF7kPbqVR0VbHFjSm2F-YPp6V0nGzCUbMSKwG1_2bGszRu9OsTNty8y6Mu2TLnhXYW4jmwscxb7qmWPGJPEMhQxYMuWaQhZrpi3Gt1HYgjBv6_i8UK1su2TqQ6Wp2_jWMEloWDATPQAOeIiBHqt8Z4twjkGll8vWHZ_IYD2YF0nht1U_uJYNfSFFoNvJktevOTG6kGBfH-wY8ehK402LgfLPKRjq9rqlx8MpcUcge-AaNRbngbqRTzKyoytc8r-FfnZ5p69G9WFw0aBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متنی که اکانت سنتکام به همراه ویدیوی بالا منتشر کرده، ترجمه ماشین:
سنتکام حملات به اهداف سپاه پاسداران در ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، توانمندی‌های مین‌گذاری و مراکز ارتباطی بود.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتیرانی تجاری در تنگه هرمز و نیروهای نظامی آمریکایی انجام شد.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول فعالیت هستند و همچنان هوشیار، مرگبار و آماده‌اند تا به اجرای عملیات‌هایی که فرمانده کل قوا دستور می‌دهد، ادامه دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78178" target="_blank">📅 02:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XnC_sbuZfhQL3awvRkz-vbjbrG_sew1N0lZs1F-cvnRAj-kqReagVoA93EDxS9_aVha1ezmNN7tbrIb_475l3xhXKWrY8nzR0p0cuGjvUuWi8PVa3M_yhvFlFP3bifQsfZJM0Uml4GAT8AyR1fhHqjSp5SSjalWr9dgSbTPcK98wHSuyTI0oimWi83pqg-EiuubwGHcwJF9VBkfZKGqrTVrvrFvoEEvmONO_uDjOPp7iEImGQmFSGPPPKTnzXYgYd9t2y8U4EbbJrl9IqkICrT_wcLJppOlzXMhpjomuHUsGVYGJvBw0V4bVPVClx47SV_T2kuVoVxoKVdNwC_5dDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gmpUo2hkMkG9fnrbxVRVQsSXrLFUJSHtVz0KquMSViBNzdB__c0sQVGazO0zsGsR3iXVGZRadQXiRtKbJl7w8Ko-CH3OX5ArP8evcsQstkJ_L8laor7AHoxSloe0eLP7ou1Z4xEKihA20Ilr2tNaUrFilZ2Lbqg02znB3eTsiwQku0dnaswGhMoRnPE7Ut9zRlqSPdUveJ-_EbexfFVJ_XX6UKHFG-JbwrDqkGSLZE6fzNJ_kqqUT-NhKJCgSRRqG_s6bmOLafRh8UTieiT9H_UGK85MPFvlICh51NRd2OgAWWaZrl4yggJWq6Wh1jk-gIdarcUAtgi6ZXay71lrZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">"ستاد کل ارتش کویت" در فاصله چند دقیقه دو اطلاعیه منتشر کرد که گویا دومی فقط یک کلمه بیشتر داره. ترجمه ماشین:
اولی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادهای متخاصم است.
KuwaitArmyGHQ
دومی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم است.
KuwaitArmyGHQ
ادامه متن:
"ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، این صداها ناشی از رهگیری اهداف متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی مراجع ذی‌صلاح را رعایت کنند."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78176" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78175">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=rkXUs-SmceL0FKlKJFeM_2OiNQ2p996FhLf7AbY7dqNRJ3QWpyjOdI7kjzkbo6gzgIYiffEg5RsBKB2l9jccuVXB-McEOLa2ue6vIT4Ke7dNAIn343-nH1QHkhm_7jSeBYmGEPRtIo3TGQCxMx_6p7wMnLsmX4yJ4aci07TtG3Ejw5tsJsCIF-3GhqRVfZWAUWj0txQqDfQvNuhQKTb8a3Wp9yWx08nX4_MrX-vjEfUexochFY3HEthH2XLkPfwgjY_tsahZ7kp60cwRSGpGnSLIwP_j9G7ljbADI93CoyhR2dmabasrCS6tFINRwBJNohL-63gh2whA5wJgL2BgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=rkXUs-SmceL0FKlKJFeM_2OiNQ2p996FhLf7AbY7dqNRJ3QWpyjOdI7kjzkbo6gzgIYiffEg5RsBKB2l9jccuVXB-McEOLa2ue6vIT4Ke7dNAIn343-nH1QHkhm_7jSeBYmGEPRtIo3TGQCxMx_6p7wMnLsmX4yJ4aci07TtG3Ejw5tsJsCIF-3GhqRVfZWAUWj0txQqDfQvNuhQKTb8a3Wp9yWx08nX4_MrX-vjEfUexochFY3HEthH2XLkPfwgjY_tsahZ7kp60cwRSGpGnSLIwP_j9G7ljbADI93CoyhR2dmabasrCS6tFINRwBJNohL-63gh2whA5wJgL2BgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان ویدیوی دریافتی از شهرستانی در استان ایلام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78175" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXVn4EEE617q4LXbcYpD9iPKN5c01iEeyJwulCeTdB8UxqHbAwNJ4RDx0KUH_dkDkgkxO88EY77RcH-gP-HPiwOEM85N3H139GduQVB-zFioUm24pUIhZcHdLd2LYZ_pOFuQNomdBCnafZBxrGoWhwTWwkfL0GmyOYL9squoa24a-CVRRAFA47-QWiY1hzfjSg72qwVg6p1JsxXtDWnS13N18jFRS4P-ff-iyJ1hE98vrbGp8-SPjoRK1jwKvnXg4ZaRxpSVhAj9F-0xxK2crUlYPOwto0Dj3K02a2e33wvFcfeLzzMpE7Rb0sZvNdMZTaXylEdDluyLzyx_CTzpfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار در کویت
ترجمه ماشین:
هشدار: خطر قریب‌الوقوع
............. تهدید امنیتی .............
همه موظف‌اند در مکان‌های امن بمانند و برای تضمین ایمنی عمومی، از پنجره‌ها و مکان‌های روباز و در معرض خطر فاصله بگیرند.
دفاع مدنی — وزارت کشور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78174" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=pzoRdnC4I08cZ7nu1_jXXHLi3cIa_0MR5hlhXokr-Nk0e9WXJex1bt3bSvjYKyL3FzC2dtaXiqwj_VWR-fU4KY9pDIP8Wy1iiupdzGzB_YQ5C8SHnNEhaZAS24RhrQD2F4PNxa4Dojr0VH_mBYPy6K4-jKlROPn-sa-AItcsuQvYU9OlE63e720sg3gNB-oRvQO1weOLxI1XuP2BBJB3Q_c3lLw5g2KMFCkSOYJ8Mr5bMmq3yOX3Pp89qTFv67hHMv2nxlY3mIc4O-GYg84jXqMf4NaTnIEuzlLvy4W-T_VxDcti51jmfpHjvVEAXDaZOgo3ZV9VuHdnbxHeEyJ3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=pzoRdnC4I08cZ7nu1_jXXHLi3cIa_0MR5hlhXokr-Nk0e9WXJex1bt3bSvjYKyL3FzC2dtaXiqwj_VWR-fU4KY9pDIP8Wy1iiupdzGzB_YQ5C8SHnNEhaZAS24RhrQD2F4PNxa4Dojr0VH_mBYPy6K4-jKlROPn-sa-AItcsuQvYU9OlE63e720sg3gNB-oRvQO1weOLxI1XuP2BBJB3Q_c3lLw5g2KMFCkSOYJ8Mr5bMmq3yOX3Pp89qTFv67hHMv2nxlY3mIc4O-GYg84jXqMf4NaTnIEuzlLvy4W-T_VxDcti51jmfpHjvVEAXDaZOgo3ZV9VuHdnbxHeEyJ3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس راهور جمهوری اسلامی ایران:
یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78173" target="_blank">📅 01:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=JaGQm7s4ibRMHPw7VxbqO2X5xrtXo83p3dOghkmdvBUfWCw0p9VIM-vbbBwKoQ_z-9hYzdBdgshJsSQ9eRRto6UiHe-uIhIzrMAT_XZ0VtngUY6noyE2tfzojN1V0cA3ub4XJ2ZwX3BLb8z8huGQqDVsri9IXxtc9bv82_RkHn4YKd-vOxExVAWTKoiRfMi38HBMpUxymCQvq-iF3Gcysp9YkLcYmzWG6WdXkKic4wuDAvdB2vY7tDInAvOwg4DFldN3cvSnHsrjJXKdKEGxZPTsK6H7UfrT4cF_DloXSe2BNDPJi8_jf33cDOSMCQb7zmjNjwZnX4ntITkq2_maEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=JaGQm7s4ibRMHPw7VxbqO2X5xrtXo83p3dOghkmdvBUfWCw0p9VIM-vbbBwKoQ_z-9hYzdBdgshJsSQ9eRRto6UiHe-uIhIzrMAT_XZ0VtngUY6noyE2tfzojN1V0cA3ub4XJ2ZwX3BLb8z8huGQqDVsri9IXxtc9bv82_RkHn4YKd-vOxExVAWTKoiRfMi38HBMpUxymCQvq-iF3Gcysp9YkLcYmzWG6WdXkKic4wuDAvdB2vY7tDInAvOwg4DFldN3cvSnHsrjJXKdKEGxZPTsK6H7UfrT4cF_DloXSe2BNDPJi8_jf33cDOSMCQb7zmjNjwZnX4ntITkq2_maEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پیکر بی‌جان
ویدیوهای منتشر شده در منابع حکومتی: یکی در
#مشهد
با خودرو کوبیده به تجمع بسیجیان
سه‌شنبه ۱۰ شهریور
Vahid
دست‌کم چهار کشته در برخورد خودرو به تجمع‌کنندگان در مشهد
دقایقی پیش خبرگزاری‌های ایران گزارش دادند که راننده خودرویی که به میان تجمع‌کنندگان در بلوار وکیل‌آباد مشهد راند، بازداشت شده است.
خبرگزاری صداوسیما گفت که در این حادثه «۴ نفر کشته و بیش از ۱۰ نفر زخمی شده‌اند.»
پلیس راهنمایی و رانندگی مشهد گفت که یک ماشین «هیوندای جنسیس با سرعت بالا منحرف شده» و پس از آن به میان جمعیت برخورد کرده است.
گفته می‌شود این خودرو به «تجمع‌ شبانه حامیان حکومت ایران» برخورد کرده است.
هنوز علت این حادثه از سوی مقام‌های مشهد اعلام نشده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/78170" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j1TunI-wT_E-daEpLGQAklmjdMJfjkwdHdqmRFlxfI5mOp-mJVrGFaIMj_mbyX9CpO-miOh6Qn2RaLQbsL-ob4AYhWA3pLWXA4F6xmRvIOwhqYZqZg-sKqBizLB1BW4PVdpC0ZymLTVZNWiwE7uom1UjWmnCFiZ-uqqYiUN7yryrrnaOWIL_-bno9sTBBfqCycmXEdGHaLxEY5ZNds9TyE1Z19JQHljJtJc4xef5hi39umh8sH1P8ZqrOM21t5Ng-ZHLHA8Uo0RrbeK9ZqyYzeW-IpfyZQjxF8KOPZGDKbinSYxkczAmKU-4mqqWPbvjdU0VQBeojIoTr_eBEMA1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VK-3WOdIuhCHBVJBxH2mXZo8x5OQcyYQK5eIIT3Ccf1H5k9G_uAHJn55BZn3SQoOIUwHjPYYsgXxi47KxGD5ouw6ibFeCDNuCdakg77K3X2KGjHfMqt4tGe3i-SOgltpSz8TRaoAWLobqUe40tr6JQDWLHikcDc19HhkHmE-1VmfmG2re3Dch9GgxyLx6OoGr_R3x_Nzt45De3Pqan9x6dAurwPL5UMB940I7-hClOCOORanHS3ojzwYUIpl-Mk9rZQd8P7DoK6n93sYpIcbQw_0rmpurR42x8DOPJkWoiAwuFEG6jBfgo0BpTsWVRFWDIzcp1s2bhGfWaKUBjzz5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت دکل مخابراتی کوهستک که در منطقه مسکونی واقع شده بود.
@iliaen</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/78168" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=l7R4kqkU6c-7Dq6KbsZihl1W2CrypteTDs6QaF9zqD3hc4D9_7hqSuHOvKsbHifH77ZX45x_6ab68813LGDoTO3SgV69DK3mr4ad3sr7nUUfbBrRrl4jZafRy2s1YZ963ENnVkv_HhfvB65y0E3ulESiJ_DJMqcz01PuD4J8NBbL-YMpMk56wNYtkSrn5ZF8HG83dS9sFSzZhWFvfqet7IM2AsFlfQQsJBELSwFKBxYWpxbaT7AeNZy7CxHGETQdcqJhZ0klAIoC6tyuVhaUA152W1pmm0GmZ6iGauUEdsmFFbX3UtfzvGPv4_Qa6_idDw8OzGBVvhSXPRV1FPaOSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=l7R4kqkU6c-7Dq6KbsZihl1W2CrypteTDs6QaF9zqD3hc4D9_7hqSuHOvKsbHifH77ZX45x_6ab68813LGDoTO3SgV69DK3mr4ad3sr7nUUfbBrRrl4jZafRy2s1YZ963ENnVkv_HhfvB65y0E3ulESiJ_DJMqcz01PuD4J8NBbL-YMpMk56wNYtkSrn5ZF8HG83dS9sFSzZhWFvfqet7IM2AsFlfQQsJBELSwFKBxYWpxbaT7AeNZy7CxHGETQdcqJhZ0klAIoC6tyuVhaUA152W1pmm0GmZ6iGauUEdsmFFbX3UtfzvGPv4_Qa6_idDw8OzGBVvhSXPRV1FPaOSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: '
در حمله به سیریک ۴ شهروند کشته و ۶۵ نفر زخمی شدند
'
ایران گفته است در حملات هوایی آمریکا به بندر کوهستک شهرستان سیریک، چهار نفر از جمله یک زن و یک کودک که در مراسم عروسی شرکت داشتند کشته و ۶۵ نفر مجروح شدند.
رئیس دانشگاه علوم پزشکی هرمزگان گفت دو نفر در محل کشته شدند و دو نفر در بیمارستان جان باختند و «شش نفر از مجروحان در بخش مراقبت‌های ویژه بستری‌ شده‌اند و ۲۶ نفر هم در بخش‌های جراحی تحت درمان قرار دارند.»
@
VahidHeadline
در همین رابطه یک منبع محلی به بی‌بی‌سی فارسی گفت به گمان او هدف حمله هوایی «یک دکل مخابراتی» که در فاصله «چند متری خانه محل برگزاری عروسی و آن طرف خیابان» قرار داشته بوده است.
@
VahidHeadline
در پیام‌هایی که من دریافت کرده بودم هم نوشته بودند هدف حمله یک
دکل مخابراتی
بوده و در اون حمله شهروندانی در خانه‌های اطراف، از جمله در یک
عروسی
، کشته یا زخمی شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/78167" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=Tpxurri-oLYa4vdjS0UbJ5kUjkLKnKCTqGqZg5GGb8TC6IUjYBoD6abWu7nlliHIvG9-AVrac05P-dt15FmBuOsJvgcEJzyeTXLaGc3ybNym5j4M37r_8fPlpbm4n9QrBoZHuPdqXZtHfAaIOs9ZDc-pnJqB74wl7HoqkxX5u31KTudxgjhZB1yelNjj86olCJJFauSywVIWcQVO1IvvrKZ_DXy6RWM9tB4i-m4x5t1ymrtlC5F1M7CqbvEcMSILFRKQTtcGMB_DFtWOFJhzR9VJrECG68KxlZfJI6FeCbqjZc0aFUhPLTuLlXw6Ta_MlqTzmrpsp6ONDJ6BaroplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=Tpxurri-oLYa4vdjS0UbJ5kUjkLKnKCTqGqZg5GGb8TC6IUjYBoD6abWu7nlliHIvG9-AVrac05P-dt15FmBuOsJvgcEJzyeTXLaGc3ybNym5j4M37r_8fPlpbm4n9QrBoZHuPdqXZtHfAaIOs9ZDc-pnJqB74wl7HoqkxX5u31KTudxgjhZB1yelNjj86olCJJFauSywVIWcQVO1IvvrKZ_DXy6RWM9tB4i-m4x5t1ymrtlC5F1M7CqbvEcMSILFRKQTtcGMB_DFtWOFJhzR9VJrECG68KxlZfJI6FeCbqjZc0aFUhPLTuLlXw6Ta_MlqTzmrpsp6ONDJ6BaroplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از بیدگنه
سلام همین الان از بیدگنه موشک زدن
سلام از فردیس موشک فرستادن
سلام وحیدجان
ساعت ۲۳:۱۳ از سمت جنوب مهرشهر کرج صدای بلند شدن موشک میاد.
سلام الان از بیدگنه موشک زدن
از کرج موشک زدن چندتا
از بیدگنه ملارد بود احتمالا
درود همین الان صدای بلند شدن موشک از فردیس کرج اومد
همین الا از ملارد بیدگنه موشک شلیک شد
همین الان از بیدگنه چندتا موشک شلیک کرد
سلام از ملارد موشک زدن ساعت ۱۱:۱۲
+ ده‌ها پیام مشابه دیگر از این منطقه پرجمعیت که نمی‌رسم بخونم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78166" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان از کرمانشاه موشک زدن ۱۱و۰۷ دقیقه
داداش کرمانشاه پردیس دقیقا همین الان صدا اومد
همین الان از کرمانشاه موشک پرتاب کردن
صدا انفجار شدید کرمانشاه الان
وحید همین الان از کرمانشاه موشک فرستادن ۲۳:۰۸
کرمانشاه الان موشک زدن
کرمانشاه صدا جنگنده میاد وحشتناک [صدای پرتاب موشک با جنگنده زیاد اشتباه گرفته میشن.]
10:08 کرمانشاه موشک رفت
همین الان از کرمانشاه موشک فرستاد ...
سلام وقت بخیر الان هم از کرمانشاه صدای شبیه پرتاب موشک اومد ۲۳:۱۰
کرمانشاه دارن موشک میزنن، هنوز ادامه داره ۲۳:۱۱
موج دوم موشک از کرمانشاه ۲۳.۱۲
آپدیت:
پیام‌های کرمانشاه تا پنج تا موشک ادامه داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78165" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام‌های دریافتی:
الان موشک از،یزد زدن
از یزد موشک زدن الان
سلام وحید جان
همین الان از یزد موشک بلند شد
همین الان از یزد موشک زدن
وحید یزد همین الان موشک بلند شد ازش
الان از یزد موشک پرتاب شد
🔄
همین الان دوتا دیگه
دو تا دیگه از یزد زدن
۲۳:۰۸ دوباره از
#یزد
موشک زدن.
۳ تا موشک دوباره یزد بلند شد
سومین موشک هم شلیک شد
ساعت 11:08 دوتا موشک دیگه از یزد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78164" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KjG37JvpNihF9yRK-pVD4zbcgCD6lw8kVGHVJGb_ky0bNi90D8emmeT6VlUbcWN70Yl16CezWgKfqT2kzMi9KK6Z3w3zYyKTEDfAL1N2JcW2fFPo6F-5MBz09K3SPDUUs50U5BTdMKceN3KqJy6BR-ClbKkRvnRIao_ATu4s6pws6KE0SYi45AnrrbKbX96l-2ftZEmPnlkZT672KZpfF3LtB1RR0D6P3THKWeOXdWnAwdodZszKUiIUPmez9sYRvry7WqOYB9nXunlLT1Vym41up9S9yaDuiYAbZLO6wXuJnF5s1aj64pN2BxKbHp__cOrwZRcmSSvRVXyoI1j38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fHxnUeDveYNoVzVnDI9hqu6t1w_2XUgwcZNBWwTc0BtJRpr3VnkLLoXVYuE9Lv_mjcVbtrdBXvPPWJEX-qyJq40QaCuDCPYQ3X0FR0G1K5n3rP4hNG52QtjKDBEpsH7G4CdCzMnX_NhJBRafVPfYEk75ovf197zBX6pbXjDQQVNGhgidtkUwh4b4aKgWy124ZcpiP-XtyYRyjmBVZdzaakcIYge2EWXLUXVwX78jPc0ISmpopPG4MVEsBpkE7ahOvO4rP6DbehjeN9Uq2Jauq3S_B-u1Ki2qTNPaDc6NsKx1xJ4VpZzieiEUKtPaU9yboLko6okmuCp5hnNBZlJAMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=NPve7YIYRHUTpHWIDS7bHeHo7U95jdqtZMBy4d7r308uyfI7zYcAq2cg7i14_62bYrrYdsyxeyTb6ssvtToNzcQPEpi9NMXjV5TqGV6qifOEhrCLRl5QGBz9ch9OuguCqGV0RxOV57ycnLgcQp2W59BLDqEJE2e0WWp5rybZOvg_VovWEpv989v8LBiypLd7kW3chsIVVDZ6ojZKuhXh9qcKaTPEY0TrprND_LMQCSiEjFJoXZDxBzgUaBeaHqvpzpeKwZR24XwCg56nLyKEOm64rh-aEztKlBS8JIwCgvvyp-3XrjV3EHftV5Ac5OpiCmaf6ZcoqSB_LPy9a6w5-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=NPve7YIYRHUTpHWIDS7bHeHo7U95jdqtZMBy4d7r308uyfI7zYcAq2cg7i14_62bYrrYdsyxeyTb6ssvtToNzcQPEpi9NMXjV5TqGV6qifOEhrCLRl5QGBz9ch9OuguCqGV0RxOV57ycnLgcQp2W59BLDqEJE2e0WWp5rybZOvg_VovWEpv989v8LBiypLd7kW3chsIVVDZ6ojZKuhXh9qcKaTPEY0TrprND_LMQCSiEjFJoXZDxBzgUaBeaHqvpzpeKwZR24XwCg56nLyKEOm64rh-aEztKlBS8JIwCgvvyp-3XrjV3EHftV5Ac5OpiCmaf6ZcoqSB_LPy9a6w5-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی: سه موشک از
#خمین
پرتاب شد
تصویر دریافتی سوم از آسمان ازنا در لرستان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78160" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=YdqFhKzZ-KKCQRF2dqr1oSEUB1jkb26zQdL8t0xYvzGGDVQalGL7HUi6hdf7lYUHqFREW-HyVbbyCgQDgC8qr9PrC5sU4gDg1LLtjgFKPmEzP-XnGBO7-29c1V-l8ysL0WGe2mWg84_brrgL2ntQyWeQZOXGw2sse3JsgAAWc5Vw-unqT-sFcEOGfBtjWG6j-3Ex0tiWoGbQVcXvOQJ6tjHc7d9mSuaH3WmEMMgYiPw4daCHe2s1utN0tSUO70Sxpev6bBosh7aQGW48x88RswaTyALG0hFoVZdXoxMBoHdfQXjEcqbNoikqFdXGVUTTpjLMuaXLsSSwfwsDFYPQ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=YdqFhKzZ-KKCQRF2dqr1oSEUB1jkb26zQdL8t0xYvzGGDVQalGL7HUi6hdf7lYUHqFREW-HyVbbyCgQDgC8qr9PrC5sU4gDg1LLtjgFKPmEzP-XnGBO7-29c1V-l8ysL0WGe2mWg84_brrgL2ntQyWeQZOXGw2sse3JsgAAWc5Vw-unqT-sFcEOGfBtjWG6j-3Ex0tiWoGbQVcXvOQJ6tjHc7d9mSuaH3WmEMMgYiPw4daCHe2s1utN0tSUO70Sxpev6bBosh7aQGW48x88RswaTyALG0hFoVZdXoxMBoHdfQXjEcqbNoikqFdXGVUTTpjLMuaXLsSSwfwsDFYPQ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
خمین همین الان دوتا موشک زد
سومی رو هم زد
سه تا موشک از خمین زدن
سه صدای شلیک موشک از الیگودرز - احتمالا سمت خمین باشه
شلیک مجدد موشک از خمین، بیش از 3تا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78159" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌های دریافتی:
قشم دو انفجار شدید اطراف شهر
شد ۴بار پشت سر هم و شدید
ساعت ۲۲و ۲۸ دقیقه
۲۲.۲۹
دوتا انفجار بزرگ بندرعباس
سومین و چهارمین انفجار بندرعباس  ۲۲.۳۰
سلام قشم رو الان خیلی بد زدن
بندرعباس ۱۰:۲۹ سه تا صدا
چندتا صدای دیگه هم داره میاد
بندرعباس دو صدای انفجار
بندر دوباره دوتا انفجار
وحید شد ۴ تا
وحید جان بندرعباس مجدد 22:28 صدای سه تا انفجار از سمت ساحل اومد
ما خونمون بغل فرودگاس
شهرک صنعتی طولا قشم یا ناحیه سپاه چهارتا انفجار، صدای سوت موشک قبل از انفجار هم اومد
۲۲:۲۸
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78158" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T7VCqZJ3zjcKJlF1v32wj43dofpK5EtBqYr-lUoI_jpBZvCwqsqP4mvD5ZxoiRmgcedZV0iwKOvAW-4sx7dFNnLrEpcyv_8QxaH0i8H-laLfRRnRASHqoda65L2N8quIhdplBR3iMqUN9QklUzVoivyZFBHxAykrPh7RPYO0thYBCBevWDec1j1_OxBysR86bwaSHwE9Cf7PeyA9gGN1JuXX3JfUCkZiPGOECbEGty1oCPYqsC3LySkYOlBZ6yWBPBMnEcbFAPoBP89dzHtIIgcIRHM4btuVddDeL_KxPBfS2qqGBeO1fAUD4KwzbRMfYJkd3ArJJAHSWKkKfjUbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، روز سه‌شنبه ۱۰ شهریور در گفت‌وگو با شبکه فاکس نیوز بازگشت به «تفاهم‌نامه اسلام‌آباد» را رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد».
ترامپ درباره پاسخ جمهوری اسلامی به حملات آمریکا گفت: «اگر آنها پاسخ بدهند، با شدت بسیار بیشتری هدف قرار خواهند گرفت.»
او حملات انجام‌شده را «بسیار بزرگ» توصیف کرد و افزود اگر درگیری برای سومین بار تشدید شود، ایران «به‌عنوان یک کشور به‌طور کامل از بین خواهد رفت».
رییس‌جمهور آمریکا گفت حملات اخیر، سامانه‌های راداری در جنوب‌غرب ایران و نزدیکی تنگه هرمز را هدف قرار داده‌اند؛ سامانه‌هایی که به گفته او ایران در حال بازسازی آنها بوده است.
ترامپ گفت نیروهای آمریکایی بخش قابل‌توجهی از شبکه راداری ایران را منهدم کرده‌اند و افزود: «آنها تلاش کردند رادارهایشان را دوباره بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریبا آماده شود و بعد آن را هدف قرار دادیم.»
او همچنین گفت ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» به‌طور کامل برای ادامه عملیات در صورت نیاز آماده است.
ترامپ بازگشت به «تفاهم‌نامه اسلام‌آباد» را نیز رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد». او افزود آمریکا فرصت‌های زیادی برای دستیابی به توافق در اختیار جمهوری اسلامی قرار داده است.
رییس‌جمهور آمریکا همچنین گفت متحدان واشنگتن در منطقه خلیج فارس پیش از حملات اخیر در جریان این عملیات قرار گرفته بودند و رهبران ایران درباره عزم او دچار «اشتباه خطرناکی» شده‌اند.
ترامپ در پایان سخنان خود درباره مقام‌های جمهوری اسلامی گفت: «آنها دست‌بردار نیستند؛ آنها دیوانه و احمق‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78157" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=msvuVPHt3EnWwUWKh6xZlx-7J5RRulCcGoSPZwCyO0A7bQrTD_tw0e-pe75ozsKNu7g48nZwOkh1kIdNf_UZeiZQJKTz8lLp0Y20uARwFYN2QfYR_DmVmo5ApppWVmAPBIHA1AZwJPpmfDE0Kto8Gx5lL2GH95-KUZ1y93druQDI2AieSv83jJiUv8JXgQjMNJFJdlNm6sjV7yM0RLbhuqEBzekGZQNlm0MqTyaoRkozHVYb2nR_tlgjOenU-qc4_d8R63ftpQ-18N3VcJc72sL25f0lsyPREw9CtJf-lI_CdiASu2TQvctfhCP7nlE_T9pL8_-jupo6N9QWtAbVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=msvuVPHt3EnWwUWKh6xZlx-7J5RRulCcGoSPZwCyO0A7bQrTD_tw0e-pe75ozsKNu7g48nZwOkh1kIdNf_UZeiZQJKTz8lLp0Y20uARwFYN2QfYR_DmVmo5ApppWVmAPBIHA1AZwJPpmfDE0Kto8Gx5lL2GH95-KUZ1y93druQDI2AieSv83jJiUv8JXgQjMNJFJdlNm6sjV7yM0RLbhuqEBzekGZQNlm0MqTyaoRkozHVYb2nR_tlgjOenU-qc4_d8R63ftpQ-18N3VcJc72sL25f0lsyPREw9CtJf-lI_CdiASu2TQvctfhCP7nlE_T9pL8_-jupo6N9QWtAbVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
پرزیدنت ترامپ به فاکس نیوز گفت که امشب شمار زیادی از رادارهای ایران هدف قرار گرفته‌اند.
پرزیدنت ترامپ گفت: «آن‌ها تلاش کردند رادارهایشان را بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و بعد آن را هدف قرار دادیم.»
رئیس‌جمهور گفت اگر ایران پاسخ دهد، «ضربات بسیار سخت‌تری خواهند خورد... اگر کار به بار سوم برسد، آن‌ها به‌عنوان یک کشور کاملاً نابود خواهند شد.»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78156" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه‌های وابسته به سپاه از آغاز حملات موشکی و پهپادی ایران به مواضع آمریکا خبر دادند
خبرگزاری فارس، وابسته به سپاه پاسداران، شامگاه سه‌شنبه ۱۰ شهریور به نقل از مشاهدات میدانی خبرنگاران خود از شلیک موشک‌ها و پهپادهای جمهوری اسلامی به سوی مواضع آمریکا خبر داد.
همزمان، خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت «عملیات قاطع نیروهای مسلح ایران» در پاسخ به حملات آمریکا آغاز شده و «پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشک‌ها و پهپادهای ایران قرار می‌گیرند».
تاکنون مقام‌های آمریکایی درباره این حملات جمهوری اسلامی اظهار نظر نکرده‌اند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78155" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwAkqWk3cEo9JAsqHb8LMgoGTzFiq8ZsDZVAc8VX49MsAJrLU9dyy4nC74dW7a_LGnCK7ZB3DuToz2ngihXlWOHx9RYvx-_2qbSv9GkM1uF2-7cm0W6iyijrkIC3NDzQ7yba1flu6GlbBOLiUxynkzf9e57Vl91FWrTcp_kixbNjmY1KwN_HQFV9l5gD6IYui4TvucDo3ZpsZVU7cNkXkSpvMDKTALJiVIsmV_YWCCEN-5c9YzKrGcceR3jHu4YMg0Ok6Szf8o8UkO_sDABD9Y4q8IvZbjbBdJS2MMevtFhj8oTLDch-oma-c9IEwf0e1wnefVNXwDevjpyKS22TUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با تری ینگست، خبرنگار فاکس‌نیوز و در پی آخرین حملات آمریکا به مواضع جمهوری اسلامی، هشداری صریح خطاب به تهران صادر کرد.
ترامپ با اشاره به پاسخ احتمالی ایران گفت: «اگر دست به تلافی بزنند، بسیار سخت‌تر هدف قرار خواهند گرفت؛ و اگر دوباره چنین کاری کنند، دیگر وجود خارجی نخواهند داشت.» او با انتقاد شدید از اقدامات تهران افزود: «آن‌ها دست برنمی‌دارند؛ رفتاری دیوانه‌وار و احمقانه دارند.»
رئیس‌جمهوری آمریکا در ادامه به جزئیات حملات اخیر اشاره کرد و گفت: «آن‌ها سعی داشتند رادارهای خود را بازسازی کنند چون هیچ دیدی نداشتند؛ ما صبر کردیم تا ساخت آن تقریبا تمام شود و سپس آن را زدیم.»
ترامپ همچنین با ابراز بی‌اعتمادی کامل به مسیر دیپلماسی با حکومت ایران تاکید کرد: «معتقدم توافق با آن‌ها حتی به اندازه کاغذی که روی آن نوشته می‌شود هم ارزش ندارد. ما شانس‌های زیادی به آن‌ها دادیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78154" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صداوسیما: فرودگاه جیرفت هدف حمله آمریکا قرار گرفت
خبرگزاری صداوسیمای جمهوری اسلامی شامگاه سه‌شنبه ۱۰ شهریور گزارش داد دقایقی پیش فرودگاه غیرنظامی جیرفت هدف حمله آمریکا قرار گرفته است.
این رسانه افزود اطلاعات تکمیلی درباره این حمله منتشر خواهد شد.
@
VahidOnLive
اسکندر پاسالار، فرماندار عسلویه، به خبرگزاری فارس، وابسته به سپاه پاسداران، گفت: «حوالی ساعت ۲۰:۱۰ شامگاه سه‌شنبه، صدای یک انفجار در شهرستان عسلویه گزارش شده است.»
فرماندار عسلویه گفت که از خسارات جانی و مالی این انفجار جزئیاتی مخابره نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78153" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78152" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=QyZsB61pP-bQw2rNP8VHafZJC88w-oChDy2CX2Ba7qf-QEbtjQrQLi67kMNIrIuZoBFoZlMsqwHY9kMWasITk77El9X4UFlDTG-BgrfiSYRBwpOxreYPyIfEJU064i5LVgtmnaCriDhAOW7-xdyeLUsvEAvS5OyiSzYlrhGCHSKMwPqoVO6G49bWS_2-0MTMstsmm9UN1lo0K5WshqzlLaEXXPxqw8bu88O9lVPnae_Gqg-FBGgdklBrMwyaEToeEQD8vPB_SqzvkdM5sHl4Jo1X_GppVC-8jlnVC3GD0wDJmSjuGKyu3hn7ZG_2kGorvCNrPaTgtgElUeUWADGS0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=QyZsB61pP-bQw2rNP8VHafZJC88w-oChDy2CX2Ba7qf-QEbtjQrQLi67kMNIrIuZoBFoZlMsqwHY9kMWasITk77El9X4UFlDTG-BgrfiSYRBwpOxreYPyIfEJU064i5LVgtmnaCriDhAOW7-xdyeLUsvEAvS5OyiSzYlrhGCHSKMwPqoVO6G49bWS_2-0MTMstsmm9UN1lo0K5WshqzlLaEXXPxqw8bu88O9lVPnae_Gqg-FBGgdklBrMwyaEToeEQD8vPB_SqzvkdM5sHl4Jo1X_GppVC-8jlnVC3GD0wDJmSjuGKyu3hn7ZG_2kGorvCNrPaTgtgElUeUWADGS0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های زیادی دریافت کردم که نوشتند حدود ساعت ۲۱:۲۵ از
#خمین
موشک شلیک شده ولی پرتاب موفق نبوده و برگشته.
ویدیوهای دریافتی: سه‌شنبه ۱۰ شهریور
Vahid
آپدیت:
منابع جمهوری اسلامی بعدا این ویدیوهای دریافتی رو با شرح هدف قرار گرفتن پهپاد آمریکایی منتشر کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78150" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی:
صدا ۹:۰۵ بندرعباس
وحید بندرو دوباره زدن همین الان
صدای انفجار بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78149" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4X3SU8zwQvenX7ABQNl-rnWFLoK0f6XgS0LPpI-rTAEsnfIDQ57-m78PyMCSlz73wV2TrNHmPB_qTX3QCfEoWepevRnsBzHd2DLF4qeo653Qhl9q3fsciGkEJ0ZKq9kPgfWwCl2B0nbbvidEUC66eDFuRLmrQYpSGkEqii3UC8copuMK0AwSvV7to3NARzv4P_e2t9pl6Wrg5-acbJEVZ6foJqq5_fWYqMx7788MeyTye4x001wmpTo5-waT92AMORHigAUwzxYQcXmOnZz0_tTzFBbL3MgV7Mkm-0haJLp24vElpq8TjQFDOmhjE9z1q1-t6Rs1t-nFtK09aI5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر ایران پاسخ دهد، حملات آمریکا شدیدتر و گسترده‌تر خواهد شد
ترجمه ماشین:
ایالات متحده همین حالا، در حالی که صحبت می‌کنیم، در حال حمله به اهدافی ایرانی در نزدیکی تنگه هرمز است.
این حملات گسترده و قدرتمند هستند و در تلافی تلاش نافرجام ایرانی‌ها برای افزودن مین‌های دریایی به تنگه انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (همه آن‌ها به‌طور کامل جمع‌آوری یا منفجر شده‌اند!)، و همچنین در تلافی شلیک هشت موشک از سوی ایرانی‌ها به پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به تلافی بزند، بار دیگر و در سطحی بسیار شدیدتر و بالاتر مورد حمله قرار خواهد گرفت؛ اما آن هم بزرگ‌ترین حمله از همه نخواهد بود. آن حمله هنوز در انتظار است و وقتی به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78148" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی:
سلام صدای چند انفجار اومد بندرعباس ۸٫۵۰
۸:۵۲ قشم یه انفجار حس شد
بندرعباس صدای 2 انفجار دیگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78147" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvtw_X-9Wrxu4dab2qExUPUrPLvSo_CqS-LQNcnzDAM_R2Q31Y68gDJs4q4DIYo8s304rmUVI2k5mLp9T7gAgrs4N8reVeVOgERaDt6cICg6CopKrjp1VrypMgwhMEHDQ6PCYSvLpL2YBMi_pyTI_Wr3Q3vk34I7ksubTrRO_zmp4LmB41KdTRNZ7VipvTyUyAPmCAsmxukdhKfQNeqIU0SY2Q1_mUUVFHVXQoB2cdn1Xmsj4nr31BM92yKFTLbDs_SmYyqo_468EjxMQGlrvdws_UxFL3TVYDrjuHv5Wpx3QiZw5pjgM4SGZapIhTJsFCDi40WSCa3xCFd-D_gsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۱۰ شهریور، در پی شروع دور جدید حملات ارتش آمریکا به مواضع نظامی در ایران، خبرگزاری آکسیوس این اقدام را صحه‌ای بر گزارش خود مبنی بر طرح آمریکا برای حملات مداوم و دوره‌ای به مواضعی در شهرهای حاشیه تنگه هرمز دانست.
پایگاه خبری آکسیوس به نقل از مقامات آمریکایی گزارش داد که دونالد ترامپ و مقامات ارشد دولت او در حال بررسی طرح‌هایی برای انجام حملات محدود در تنگه هرمز و مناطق اطراف آن هستند. هدف اصلی این حملات، جلوگیری از بازسازی سامانه‌های راداری، پدافند هوایی و توانمندی‌های موشکی ایران اعلام شده است.
به گفته آکسیوس این طرح که توسط فرماندهی مرکزی آمریکا (سنتکام) تدوین شده و مورد حمایت پیت هگست، وزیر جنگ قرار گرفته، به دنبال مهار تلاش‌های تازه ایران برای تهدید شناورها و نفت‌کش‌هاست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78146" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/As1rbKPeBbokpw0pCE20epwTf7Hr5HD44sVLRyTc-rPzogSGKQib9ElF9EZcKGAh6puErVxL_55JQ2JoCQCft1SsYHmcx2Pu_xwAyNlskFUls_j1OaP2o20mZfbi74-GBbYLYLkFpBSUI-_0IhbcmLyiqB2E-GAUjQXgWfVGhWPuRXH0Lw728iH3Nj1q9zLUkSSynHdXjcT6KCxGuswX2PWmJ1-ExZ46-CE4ZTDD4ySrYnIfr4EREvDaanvMeJigiwXrzdUfZGnfCMg6poFJEFdKsn530H5PI6RafnB_9NAAJz-Eukmr-hwC9Ydt77mpWx5B8LRm_nZxm2vTWlvk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سنتکام در این لحظه منتشر شد. چیزی که پیش‌تر در منابع دیگر پخش شد درست نیست:
امروز ساعت ۱۲ ظهر به وقت شرق آمریکا [ساعت ۱۹:۳۰ به وقت تهران]، نیروهای ایالات متحده حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران را آغاز کردند.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و نیروهای نظامی آمریکایی مستقر در منطقه انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78145" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_WCgY9bEhAUCvboPteduvpoPT83IBbqTn_sza5KIq_6TA9rv4Th1dknzENebVaEj0Oq-Py-PFSzJrG_b4hNhFWJkgPEdqXxpaXSG8qeMwymnjGZKcwxSVgZj1YV2OllFXAOkmG5UCu_FXE1IeJfc_FmgKdGTOSOkcM432KvAMDT7gQm2Z2Iy_zncKA3zuQLwwkT7yvsoWaiWKWVVtWFJjMnX14ezcX_I3M2VikOWr2HtlmyIZxp6KWLqRr1e_HvsJnw_Zf-XsNp_YcJjd2hqxouY9d98ZoN7vXPnn3yZFB4x6ItI4AqYYg-ZeOURrA-lmP-PqrIA81yXboOr8Kspg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی از شنیده شدن صدای چند انفجار در قشم در شامگاه سه‌شنبه خبر داد و نوشت: «دقایقی قبل صدای بیش از ۵ انفجار اطراف روستای مسن قشم شنیده شد.»
این خبرگزاری نوشت: «دقایقی پیش، صدای ۴ انفجار هم از سمت تنگه هرمز در قشم شنیده شد.»
رسانه‌های ایران از شنیده شدن صدای انفجار در بندرعباس، سیریک و چابهار نیز خبر داده‌اند.
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، می‌گوید تاکنون هیچ‌گونه اصابت یا حادثه‌ای در هرمزگان گزارش نشده است.
@
VahidOOnLine
علی خلیل‌آبادی، معاون امنیتی و انتظامی استاندار سیستان و بلوچستان، در گفت‌وگو با خبرگزاری دولتی ایرنا از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78144" target="_blank">📅 20:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78143">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیام‌های دریافتی:
۱۹:۵۸  چهار انفجار پشت سر هم
بندرعباس ۷ انفجار شدید ۱۹:۵۷
دوباره زدن بندرعباس
صداهای پشت سر هم ولی این بار خیلی دور
7 صدای انفجار بندرعباس سمت شرق پشت سر هم ساعت نزدیک 8
سلام بندرعباس حدود 10 انفجار
7:57
صدای ۵ انفجار  (۳ انفجار پشت سر هم و ۲ انفجار جدا ) از فاصله دور جزیره قشم شنیده شد
ساعت ١٩:٥٧ دقیقه چندتا انفجار پشت سر هم شنیدم یندرعباس
شیش انفجار مجدد بندرعباس ساعت هفت پنجاه هفت دقیقه خیلیم شدید
7:57 بندرعباس 10 شهریور بالای 10 تا انفجار
بندرعباس ۱۹:۵۷
چهار پنج تا پشت سر هم زدن
دوباره زدن ، شاید هم صدای موشک از اینطرفه، صدا اینبار کمتر بود ولی تعدادش بیشتر بود
بندرعباس انفجار های پشت هم صداش قطع نمیشه
چقد زیاد ۷ تا انفجار توی ۱۰ ثانیه ساعت ۱۹.۵۸
دور از قشم
۱۹:۵۸  ۴ انفجار پشت سر هم
احتمالا بندرعباس
ولی از قشم به خوبی احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78143" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
دوباره زدن بندرعباس
الان یه انفجتر دیگه بندر عباس از بقه بلند تر بود ساعت ۱۹:۴۵
یک انفجار شدید الان در بندرعباس
۱۹:۴۶ دوباره بندرعباس صدای ۲ انفجار متوالی
ما شرق بندرعباسیم، صدا ضعیف بود.
سلام دوباره همین الان قشم رو زدن دو مرتبه19:47
وحید جان صدای شدیدتر همین الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78142" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های کمی از سیستان و بلوچستان:
19:34 کنارک انفجار اول
19:36 کنارک انفجار دوم
سلام وحید جان صدای انفجار چابهار همین الان
چابهار داره میزنه19:33
شیش هفت تا انفجار پشت سر هم
چابهار صدای پنج انفجار پنج دقیقه پیش
سلام وحید تو خونه ۶ تا شنیدیم شاید بیشتر بود
کنارک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78141" target="_blank">📅 19:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔽
#بندرعباس
پیام‌های دریافتی:
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندرعباس صدای ۳ انفجار ۱۹:۲۸
بندرعباس دو صدای انفجار
بندرعباس 3 انفجار همین الان
درود چهار صدای انفجار با موج انفجار بندرعباس ساعت ۱۹:۲۸
وحید بندر سه تا صدای انفجار اومد ۱۹:۲۹
بندر عباس 19:29
صدای ۴ انفجار سنگین
سلام، هم اکنون صدای دو انفجار در بندرعباس
درود وحید جان بخدا دیگه دارن میزنن بندرعباس الان دو تا انفجار محدوده فرودگاه ساعت ۱۹:۲۹ حالا یا زدن یا خوردن
سلام
۳تا صدای انفجار مانند الان بندر عباس اومد تو خونه حس کردیم نمی‌دونم چی بود دقیق
سلام بندرعباس الان با فاصله های چند ثانیه ای صدای ۴ تا انفجار اومد
صدای دوانفجار بزرگ بندرعباس ساعت هفت وبیست وپنج دقیقه شب
۱۹/۲۹ چند انفجار پشت هم قشم حس شد
احتمالا لارک، هرمز یا بندرعباسه
احتمال بیشتر لارک صدا از سمت جنوب بود
بندرعباس الان دوتا انفجار شدید
۱۹:۲۹ زدن
منطقه بهشت بندر صدا واضح بود
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندر رو زدن
وحید جان صدای دو انفجار سمت اسکله رجایی العان
دوبار ۲ تا دیگه
سمت قشم درگهان بود موج
درود وحید خان صدای 4 تا انفجار پشت سر هم بندرعباس از سمت بلوار شهید رجایی
خیلی شدید
درود وقت شما بخیر
ساعت هفت و بیست هفت بندر عباس صدای انفجار
قشم خیلی صدای انفجار میاد همین الان
شروع شد ۱۹.۲۹.  صدای ۴ تا انفجار دور از قشم
یکی دیگه دقیقه ۳۱ دور بود
سلام وحید جان قشم صدا و موج انفجار میشنویم
خیلی دوره ولی بزرگ احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78140" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db6862775f.mp4?token=sOzdBzZcNpbCR8jw1LTfcEd2Qiukr-THR4p_2bqpD5qxKOXruTNKzcgU1gNSEZEdckuUUIuySD7sJM1Z_hlXeMu6ZgFcveGVOTm2KTMExohZdhqHYsGSE-Vai40BX0lk1slj9S07CLNQK7-cB-RyP1n3wRREp_o0SWJjcZgoaVfhcxez2sHCgci6EP21sC809XFk9mU0P52EWJXWhfz-KLaN8B7aiKV-YM1ODEKFFL1K_5tmhfqBL4QqLc8S_Qxy587fBniEDs7LXnHbiNIX4I9QG5MP7ZELIg584yip43waFPAL64oG_FSNOzCnX4dd9sgdjqfXtCPMR4EyVHuEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db6862775f.mp4?token=sOzdBzZcNpbCR8jw1LTfcEd2Qiukr-THR4p_2bqpD5qxKOXruTNKzcgU1gNSEZEdckuUUIuySD7sJM1Z_hlXeMu6ZgFcveGVOTm2KTMExohZdhqHYsGSE-Vai40BX0lk1slj9S07CLNQK7-cB-RyP1n3wRREp_o0SWJjcZgoaVfhcxez2sHCgci6EP21sC809XFk9mU0P52EWJXWhfz-KLaN8B7aiKV-YM1ODEKFFL1K_5tmhfqBL4QqLc8S_Qxy587fBniEDs7LXnHbiNIX4I9QG5MP7ZELIg584yip43waFPAL64oG_FSNOzCnX4dd9sgdjqfXtCPMR4EyVHuEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.  درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید…</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78139" target="_blank">📅 18:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u45i_4MBwQoHniUPFGY2M82VdmSa1SnQ7Ez2Bh4Ip_YDFuKz4SR8cgoBvoCG7afNstlG8g0YFdLzsbhFHnLPwkcamTdxSMgBLX2SgmpP0etHIc3c8HaG3WC4FrYUMSUapNwVgXKp_fIi-MbfuKsUvfFKVff5I3PKEM34TnPxo2NN9HdZUgSPOO885rsA8i7NcuyJVRXyfnIJ7QSEu8GPgsIbXYb5edFa0T15ufGe1zkCutl91rC6smqQrGci29xC6yewDgNoSnjJaN99ieRjINP6aDKIUo-vaT7-A3gZPv88i78Lb2pPpBukHCWifFrMI7jv4qYxG2_KiLyxIvXEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=n6YinU1nKt5KIIl0tF0ejkVZWPr05E8-LN6Gt0dcPKFgfW-HS9HrW6TJeW7z9z9cOQK6O6lMiFegn99JplpxwT3Xa-aHIdIoy6PCKMyf4xhNs1Ddz_ewn5whIbwqhnuSDkB4jF0ozmVqaVIb50SaY54-F7UhDs80b8Xs-32W4Jw8yNEyu4ow8tbiONcZ_5v2LHWUnPfPcG4MoX18VSvgN0RM94MQzp6LVwGTWMAgNQl_FhWYFuGnuaeW0NndhzPYY3aOtFIlvRdy0G2C_SsSGt_rrZ2psPWiZQyQkQHD9Wpg9ZbM9ILdX0pl4sJyCEe2DnV5-3rm206CQ4FMWc-PYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=n6YinU1nKt5KIIl0tF0ejkVZWPr05E8-LN6Gt0dcPKFgfW-HS9HrW6TJeW7z9z9cOQK6O6lMiFegn99JplpxwT3Xa-aHIdIoy6PCKMyf4xhNs1Ddz_ewn5whIbwqhnuSDkB4jF0ozmVqaVIb50SaY54-F7UhDs80b8Xs-32W4Jw8yNEyu4ow8tbiONcZ_5v2LHWUnPfPcG4MoX18VSvgN0RM94MQzp6LVwGTWMAgNQl_FhWYFuGnuaeW0NndhzPYY3aOtFIlvRdy0G2C_SsSGt_rrZ2psPWiZQyQkQHD9Wpg9ZbM9ILdX0pl4sJyCEe2DnV5-3rm206CQ4FMWc-PYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا گفت: «جهان از رژیم مطرود و یاغی ایران خسته شده است و ترامپ به‌جای مماشات با آن‌ها می‌خواهد یک‌بار برای همیشه به آن‌ها خاتمه دهد. مردم ایران این فرصت را دارند که به نظام جهانی برگردند، به‌جای اینکه سرکوب شوند.»
IranIntl
بسنت گفت: «ما سر مار ایرانی را زیر خاک کرده‌ایم. مار هنوز نمی‌داند که مرده است و بدنش کمی حرکت می‌کند، اما با غروب آفتاب از حرکت باز خواهد ایستاد. رژیم ایران نابود شده است و به‌زودی خودش هم این را متوجه خواهد شد.» او تاکید کرد دونالد ترامپ قصد دارد این پرونده را برای همیشه ببندد.
@
VahidOOnLine
اسکات بسنت گفت: «ایرانی‌ها تلاش می‌کنند از تنگه هرمز به عنوان یک گلوگاه استفاده کنند. این تنگه برای آمریکا گلوگاه نیست، اما برای بسیاری از کشورهای دیگر هست. این وضعیت تا دو سال دیگر دور زده خواهد شد. تا دو سال دیگر، تنگه هرمز به پهنه‌ای بی‌ارزش از آب تبدیل خواهد شد.»
بسنت گفت: «نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.»
@
VahidOnLive
وزیر خزانه‌داری آمریکا: در حال شناسایی و ردیابی دارایی‌های سپاه هستیم
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز سه‌شنبه ۱۰ شهریور در حاشیه نشست وزیران و مقام‌های ارشد مالی گروه ۲۰، از تشدید فشار اقتصادی واشنگتن بر ایران خبر داد و گفت آمریکا احتمالا این هفته یک بانک و هفته آینده یک بانک دیگر را تحریم خواهد کرد.
بسنت گفت: «احتمالا این هفته تحریم یک بانک را اعلام خواهیم کرد و هفته بعد نیز یکی دیگر را اعلام می‌کنیم.»
او افزود آمریکا در این زمینه با متحدان خود در حال گفت‌وگو است و از حمایت آنها برخوردار است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال بررسی تحریم شرکت‌های لیزینگ هواپیما و دیگر نهادهایی است که با سپاه پاسداران تجارت می‌کنند.
او گفت: «ممکن است این‌ها نهادهای مختلفی باشند. ممکن است شرکت‌های لیزینگ هواپیما باشند که آنها را بررسی خواهیم کرد. ممکن است هر کسی باشد که با سپاه پاسداران تجارت می‌کند. ما در حال شناسایی و ردیابی دارایی‌های سپاه هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78137" target="_blank">📅 18:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=PRB3KjVa3PhJHmart9P56ohZoHzkOCdiAqHVTd6GhyXaMUcFCmK5x4-GB3-_QhTvt071B20mHxjiHk_NBFKu949Y_3gi9HPde6FGy-h3rAWrHxIQWVxv0kFlcIOU6MAPdPK46Epc68jnNAZ99i97PV0hZc3zAGl6UAtIFL21YouP3B5621Pubi9UwbGAvfw14qVUH_m-eOnTgY2xtw3OnEwlc_yy86CHjqs3HXcy9ZoErfo_Luj13NZ67xt9FDSX3uCHx75IqHmUrgdHO5lPkqZ-To3cW4yRmi46PI2hZUSpC6wnJzTBlsbQlkkYNBG49CzagGS9uWIkQ2jifb4ADg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=PRB3KjVa3PhJHmart9P56ohZoHzkOCdiAqHVTd6GhyXaMUcFCmK5x4-GB3-_QhTvt071B20mHxjiHk_NBFKu949Y_3gi9HPde6FGy-h3rAWrHxIQWVxv0kFlcIOU6MAPdPK46Epc68jnNAZ99i97PV0hZc3zAGl6UAtIFL21YouP3B5621Pubi9UwbGAvfw14qVUH_m-eOnTgY2xtw3OnEwlc_yy86CHjqs3HXcy9ZoErfo_Luj13NZ67xt9FDSX3uCHx75IqHmUrgdHO5lPkqZ-To3cW4yRmi46PI2hZUSpC6wnJzTBlsbQlkkYNBG49CzagGS9uWIkQ2jifb4ADg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس شورای اسلامی، سه‌شنبه در پیامی ویدیویی با تاکید بر اینکه محاصره دریایی در قوانین بین‌المللی، یک اقدام نظامی محسوب می‌شود، گفت که اگر محاصره را تشدید کنند، حتما پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد.
قالیباف گفت: «اگر دشمن اراده‌اش بر این باشد که ما از خلیج فارس نفت صادر نکنیم، هیچ‌کس نخواهد توانست نفت صادر کند.»
او گفت: «آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد.»
رییس مجلس افزود: «دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است.»
قالیباف گفت که دشمن پس از «شکست در عرصه نظامی و دیپلماسی» سراغ جنگ اقتصادی و شناختی رفت و آن را به جنگ نظامی خود اضافه کرد.
قالیباف افزود: «هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78136" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYHQjgNcELjO2tLjZWbums6dKzvQ3MyDhvKz8WkHPMCHiZ3jfEflQ-s_kWpQMHoh1jn7pNhIAmfUN3LQ0fBM_E2kKzdti4QfLAgccZA-PBzHYe-egcCwcycjWt_-jCxwh0XhmapJZDY1vmHUSkZFvoEZegGeETKLB1iuIa93e0s7iGFIptyXpJ-dNC_1hU57N_1XCwVx2kfSYkYk9Xkcf9wUT8RKr7zSW_X8ERPozgdcmzW6-wpfyWQU4cFZvD8ZlMnjtcnObm03DCrGMLJAZMPVQtD_jeNWUbL5-WiX2TxZdRsT0HnW0qOFbvENbmZrGqrqD4uhnr65Ncw79LEhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با انتشار اخباری از حضور «حجاب‌بان‌ها» در بازار تهران و سخنان برخی از مقام‌های جمهوری اسلامی در رابطه با لزوم «اجبار حجاب»، تصاویری از نصب بنرهایی در شهرهای مختلف ایران منتشر شده که در آن‌ها زنان به مجازات قضایی در صورت رعایت نکردن حجاب مورد نظر حکومت تهدید شده‌اند.
در این بنرها، به تبصره ماده ۶۳۸ قانون مجازات اسلامی استناد شده و آمده است: «حضور بانوان بدون حجاب شرعی در معابر و انظار عمومی جرم و دارای مجازات حبس است.»
در بنر نصب‌شده همچنین به مواد ۷ و ۹ قانون موسوم به «حمایت از آمران به معروف و ناهیان از منکر» اشاره شده است. در توضیح ماده ۷ نوشته شده افرادی که در برابر «امر به معروف و نهی از منکر» مانع ایجاد کنند، مشمول تخفیف یا تعلیق مجازات نمی‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78135" target="_blank">📅 18:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBHRShLBUQC6_a0pjgPoJJ3Kqi9Kir2O01aKUY62ERJiTRKesPweJZ5tf0kDNOxwxH68PIGlWrc5k-pfUSPNMF0IYqvp5kwC72uekj9GWdguRMHoghIZ49rk4w3ExpLVvRYLXaxX5Y7qj4bQxsEpQCa9Kq5r1Bi7YIWhhJNYe00SgANXV7q8prxNbF6WSohtt8HKygO3ZMxeYbaPXqTmvJSiD7w40o5ed0sA2ZQUo9kNqhZXS3vjbpm59B9MC4o0MnHtf069py5b0Du9bYk5jIPLkkktM9EYwpOJGouis3c3zmpDzvr365gXLSKCCP1sV_RbmqyoZoXTUx9uRBBYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران به ۲۱۳ هزار و ۷۰۰ تومان و حواله دلار به ۲۱۸ هزار تومان رسید. هر پوند بریتانیا نیز با ۲۸۹ هزار تومان معامله شد.
رقم امروز چهارمین رکورد پیاپی در چهار روز کاری است. دلار روز شنبه با ۲۰۶ هزار و ۴۰۰ تومان بسته شد، یکشنبه به ۲۰۸ هزار و دوشنبه به ۲۱۰ هزار تومان رسید.
همزمان با ثبت رکوردهای جدید در بازار ارز، رئیس کل بانک مرکزی در سی‌وششمین همایش بانکداری اسلامی گفت ایران کمبود ارز ندارد و ادعای فروپاشی اقتصادی کذب است.
همتی در پاسخ به اظهارات مقام‌های آمریکایی درباره نبود دسترسی ایران به منابع مالی گفت: «این ادعاها به‌طور کامل بی‌اساس است. ذخایر مسدودنشده، منابع پایدار و درآمدهای نفتی و غیرنفتی متعددی در دسترس بانک مرکزی قرار دارد.»
او افزود بانک مرکزی هفته گذشته ۵۰۰ میلیون دلار به بازار تخصیص داد و اکنون آمادگی دارد در صورت نیاز تا سقف دو میلیارد دلار ارز تزریق کند.
اظهارات امروز همتی با موضع پیشین او فاصله دارد. او هفته گذشته در گفت‌وگوی تلویزیونی گفته بود: «درآمد ما از فروش نفت صفر شده؛ یک واقعیتی است که نفت صادر نمی‌کنیم.»
چرخش لحن پس از پیام مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به مناسبت هفته دولت رخ داد. او در آن پیام گفت گاهی بیان صادقانه ضعف‌ها کمک به دشمن است و بر ضرورت «تبیین و روایت قدرت و قوت ایران» تأکید کرد.
رهبر جمهوری اسلامی در همان پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/78134" target="_blank">📅 18:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D4NG8PxxMmYUeTZ7i-4QCL7yW7FYJK41SyIrEUmDFavRWFD9PGGozbB24fZpmsQ3_Ydl87H44GqKYT5cNvHE-g2_E3FqNtnoFg2oV2bLJyeud_pIOCfJiL0nE4SfTEKFy_L-AqOT9bFxI-7wT83oyKBCDPTYtVHNpmFsR-XBz4u0ruorSVPdsnBGdKwVHPp2eoehkYprfdndXZOuoHykNz40HaJS5-zNkba1p5CsnbwkNyaFFtCatCElDDEyGkhU75KsQE1oIz7ZjBstx7a7s0-OAsSrSbeFoU5kSL_fYF8mRKF74BqRrHdrB0bzMFz5gRidEc_9hDL8N6tMpINJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت‌های‌ ناظر بر کشتیرانی جهانی می‌گویند دو ابرنفتکش حامل نفت عربستان سعودی اواخر روز دوشنبه نهم شهریور هنگام عبور از تنگه هرمز به فاصله چند دقیقه از یکدیگر هدف اصابت پرتابه‌های ناشناس قرار گرفتند.
به گزارش خبرگزاری رویترز، شرکت یونانی امنیت دریایی «ماریسکس» روز سه‌شنبه دهم شهریور اعلام کرد که ابرنفتکش «سیدر» حامل نفت خام عربستان سعودی با پرچم همین کشور حدود ۱۶ مایل دریایی در شمال شرقی خصب، عمان، ساعت ۱۹:۵۲ دوشنبه به وقت گرینویچ مورد اصابت پرتابه‌های ناشناس قرار گرفت.
شرکت امنیت دریایی وانگارد تک هم گفته است نفتکش «سنگال پراسپریتی» با پرچم لیبریا دقایقی بعد در حدود ۱۷ مایل دریایی در شرق خصب مورد اصابت سه پرتابه ناشناس قرار گرفت.
پیشتر سازمان عملیات تجارت دریایی بریتانیا از حمله به این نفتکش خبر داده و گفته بود سه پرتابه به آن هنگام خروج از تنگه هرمز برخورد کرده است.
بر اساس گزارش‌ها، خدمه این دو نفتکش سالم هستند و هر دو به فاصله کوتاهی از یکدیگر متوقف شده‌اند.
داده‌های شرکت کپلر نشان می‌دهد که هر یک از این نفتکش‌ها هفته گذشته ۲ میلیون بشکه نفت خام عربستان سعودی را از بندر جعیمه در خلیج فارس بارگیری کرده بودند.
با تشدید دوبارهٔ درگیری ایران و آمریکا، قیمت برنت روز دوشنبه نزدیک به سه درصد افزایش یافت و به ۹۰ دلار و ۴۹ سنت رسید و روز سه‌شنبه نیز با ادامه روند صعودی به حدود ۹۱ دلار و ۱۵ سنت در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/78133" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXGd8oj-4J6C7sYntxZJxn-uMjoUYltmBDU0zFhcSGH33tpzAptC6FAoh6-nAzEE5uSu_KzDc0yZSsEet6s1dlOZ6wzBXTvVsuji0Or1iJdx9SbI78rnpAIGvtenelRW_Qc3qOxl27NPvxfDEB5ElsuOjvGB4Sk101JRY4VPnfCMnZ-BaBmzhoNCtYQbrpQk04SUU6bjvCzsG3NNf9jG0OxpYYdRzq8X3YS_mGFo17ZsSEVdXP9ZCHnQ3v1Twrl004aFhe7HtSGlKfkH47RF6092oqfu2wr6YKDM3i2lSi5vU8MS1gWaAADNcsCE4NDHomNUDRpB36jthqvN0mqxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران، از ساکنان اسرائیل خواست به کشورهای خود بازگردند و «به‌سرعت فرار کنند». او گفت با کسانی که بمانند، مانند بنی‌قریظه رفتار خواهد شد.
نقدی گفت: «آنها باید بدانند رفتاری که نیروهای اسلام پس از رسیدن به آنجا در پیش خواهند گرفت، همان رفتاری خواهد بود که با بنی‌قریظه شد.»
او افزود: «پس باید به‌سرعت فرار کنند و هر کس بماند، بر اساس شیوه‌ای که با بنی‌قریظه رفتار شد و مطابق حکم تورات، نه بر اساس رحمت اسلامی، با او رفتار خواهد شد.»
بنی‌قریظه یکی از قبایل یهودی ساکن مدینه در دوره محمد، پیامبر مسلمانان، بود. بر اساس روایت‌های تاریخی اسلامی، پس از نبرد خندق و تسلیم بنی‌قریظه، مردان این قبیله کشته و زنان و کودکان به اسارت گرفته شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/78132" target="_blank">📅 18:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nJ-70ek_crZGdluBEvpXQ3rdIv2SSuPyqARj-0NwA4rBvUb8D6tYvGoexTgrsgEzR0qohfW1r7kA096fDZKlwSG_22mZs1FX6LCjzN6KPfkhkVtKLJuNZGthe7du6FAejNhCZGcnXnxm_9yrSh72lNPemQXLbupwzfFFG7j1HYXijJIsKa00MaIu4eZZHFrvazNPNJv7zHfU5BgFTXvaTUekc9huFlvrkFejSTZGGwx6EtRw-XM467k0jOieMHwMHraWWrSaZaxhoqlKqZ_eEnJ-GiOEda0b6lc2lUlPpR0GPRCo1Ux7PUUQjKtRSG8tvOFJaeEzF9L9ux21BzCQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y03O7Ly3yjg9F_qmvUuRDJhzk5yHxAu_JjJ4YQiXWMrhlYLzPvIKiM7aYkgapdtYRFQupIkpPlCexDBxXgprgYKa7qQ-7-jek1vQieqxjbUAAYV-V5vPM_Hk-v1Ik9ACnbgecureLzU05pjVj5m0B3nIW_Sjf3jlw7ACSkmA5sZkMWpEDoF7em7lN5735cCpdqLk5RYLbxgdwVAZMDw7o-QuX1569BliiTGOpv2n0YjDQQJnTSlsI7nDqgy3zToVsbauxBF99nxy-EiqGUIUgOEn7xV02Ng6RpPV-UxMdMwVnqoTbyVcEHPh8ED7ff9XcWxsmeojmWYy_3cXlTTM4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«کانون صنفی استادان دانشگاهی ایران» هشدار داده است اگر قانون ترمیم حقوق اعضای هیئت علمی تا پایان شهریور ۱۴۰۵ به‌طور کامل اجرا نشود، از استادان خواهد خواست فعالیت‌های دانشگاهی خود را از ابتدای مهر تعلیق کنند.
این کانون در بیانیه‌ای اعلام کرده است تعلیق فعالیت‌ها، حوزه‌های آموزشی، پژوهشی، اجرایی و مشاوره‌ای را شامل می‌شود و تا زمان اجرای «کامل و بی‌قیدوشرط» قانون ادامه خواهد یافت.
کانون صنفی استادان، سازمان برنامه‌وبودجه و رییس آن را به «مانع‌تراشی‌های سلیقه‌ای و خارج از عرف» متهم کرده و گفته است مکاتبه، مذاکره و رایزنی با مقام‌های مسئول نیز تاکنون به نتیجه نرسیده است.
این تشکل صنفی همچنین هشدار داده است ادامه بی‌توجهی به وضعیت معیشتی دانشگاهیان می‌تواند به افزایش مهاجرت نخبگان، کاهش بهره‌وری علمی و واردشدن آسیب‌های جبران‌ناپذیر به سرمایه انسانی کشور منجر شود.
مصوبه اصلاح حقوق اعضای هیئت علمی روز ۱۸ اسفند ۱۴۰۴ در شورای حقوق و دستمزد تصویب شد و قرار بود از ابتدای سال ۱۴۰۵ اجرا شود. این مصوبه، تغییر فرمول محاسبه حقوق و اصلاح ضر‌ایب مبنای پرداخت به اعضای هیئت علمی را در بر می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78130" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=IFGm_SpwN13WCBRju3jxSjp_mtcLGr2SIGfJZiP5ZPanMNAQCpwPXkWuKYQH35BAtWrjMHBgJbzZ4upRPbCtQLaQhx7OuAuTnJVSP6FuYsPdUvpMMAPGD2ljAvff74J-4HgCidQmNshmExIT8n_Oe7hF4cuLDoJsCojU_99-Ek7RgDnzNY101j4BTjScA-lcEFoZ55LQ3J1AJOaKL6tzyytSOreVL3Sk_ftuRq_SR35_b4AFwHHlX_hITlrm8XnG0A251bY1vM_md99b1kGj9XlcSdsF059np-0SRrzWsGZxxTyHhw5EEsbdtxWcLsxPdYNX78ZlhYk2GJvWbOW1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=IFGm_SpwN13WCBRju3jxSjp_mtcLGr2SIGfJZiP5ZPanMNAQCpwPXkWuKYQH35BAtWrjMHBgJbzZ4upRPbCtQLaQhx7OuAuTnJVSP6FuYsPdUvpMMAPGD2ljAvff74J-4HgCidQmNshmExIT8n_Oe7hF4cuLDoJsCojU_99-Ek7RgDnzNY101j4BTjScA-lcEFoZ55LQ3J1AJOaKL6tzyytSOreVL3Sk_ftuRq_SR35_b4AFwHHlX_hITlrm8XnG0A251bY1vM_md99b1kGj9XlcSdsF059np-0SRrzWsGZxxTyHhw5EEsbdtxWcLsxPdYNX78ZlhYk2GJvWbOW1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، روز سه‌شنبه ۱۰ شهریور در دیدار با ولادیمیر پوتین، رئیس‌جمهوری روسیه اعلام کرد که اگر ایالات متحده آمریکا به تفاهم‌نامه اسلام‌آباد برگردد، تهران نیز آماده است که به مفاد آن عمل کند.
پزشکیان، در این دیدار که در حاشیه نشست سران سازمان همکاری شانگهای برگزار شد، حضور ایران در سازمان‌هایی چون شانگهای و بریکس را تلاشی برای مقابله با «یک‌جانبه‌گرایی» آمریکا توصیف کرد.
پزشکیان در ادامه با تاکید بر تفاهم ایران و روسیه در زمینه ضرورت چندجانبه‌سازی در سیاست و اقتصاد جهانی، ابراز امیدواری کرد که این فرآیند به شکلی موفق پیش برود.
@
VahidOOnLine
مسعود پزشکیان، رییس دولت جمهوری اسلامی، در دیدار با ولادیمیر پوتین، رییس‌جمهور روسیه، گفت: «از موضع روسیه درباره جنگ و تحریم‌ها تشکر می‌کنیم. می‌توانیم در برابر یک‌جانبه‌گرایی آمریکا مقاومت کنیم. آمریکا حق ندارد تحریم اعمال کند و قوانین بین‌المللی را نقض کند.»
پزشکیان گفت: «حمله آمریکا هیچ توجیه منطقی نداشت.»
@
VahidOnLive
ولادیمیر پوتین، گفت مسکو از هر فرصتی برای دیدار، گفتگو و انجام رایزنی با تهران استفاده می‌کند.
پوتین با ابراز خرسندی از دیدار دوباره با پزشکیان گفت روابط دوستانه روسیه و ایران در همه زمینه‌ها به‌طور باثبات در حال توسعه است و این روابط مطابق با «متن و روح پیمان مشارکت جامع راهبردی» میان دو کشور پیش می‌رود.
@
VahidOOnLine
عباس عراقچی در پایان روز نخست نشست سران شانگهای در قرقیزستان گفت: «یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود.»
عباس عراقچی گفت «آمریکا باید به تعهدات خود بازگردد و به مفاد یادداشت تفاهم پایبند باشد؛ پس از آن می‌توانیم از این وضعیت خارج شویم چون همه کشورها دغدغه دارند که جنگ هرچه سریع‌تر خاتمه پیدا کند.»
مسعود پزشکیان امروز در حاشیه نشست شانگهای با رهبران هند، پاکستان و آذربایجان به طور جداگانه دیدار کرد.
شی جین‌پینگ، رئیس‌جمهور چین، ولادیمیر پوتین، رئیس‌جمهور روسیه، مسعود پزشکیان و بیش از ۱۲ رهبر دیگر امروز در قرقیزستان گرد هم آمده‌اند تا در نشست دو روزه سازمان همکاری شانگهای شرکت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/78128" target="_blank">📅 18:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UW2xc_xPKDAHvD6tn8ExBwJaUH8UoR3s655wk6xPVSIKgSlpxKiGJjK8S2v-eYfmGlVKX3mco2JArmkxhETW69_-cchjBBAhwCs8xc7nYd6MRLcphplnCcT6KV4Urf8-PP13uTarq-jHqbHUKnoKEg9zag8feoQO3X4f6q5UYOZdJT-ub8Qu1oOvfeWFPkInOs7seNWS-rAoCGH_iQXHCeYZLxZ9NI609kkTuNpORVktZfJ26t944tkTz42eu5H5tnE064_5nMYMYw1TfNGjqUAiLOaG-YAE1L_-cv-9M9Qa2-nZoZvfUi0BzGftLJ9l003FN7Jrl9DZiAWVDzJdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر بختیاری، پدر پویا بختیاری از جان‌باختگان اعتراضات آبان ۱۳۹۸، از سوی شعبه اول دادگاه انقلاب بندرعباس در مجموع به ۱۰ سال حبس تعزیری دیگر محکوم شده است.
براساس حکم صادرشده، او با اتهام «فعالیت تبلیغی علیه نظام جمهوری اسلامی از طریق هم‌سویی رسانه‌ای با معاندان» به یک سال حبس، با اتهام «تحریک مردم به جنگ و کشتار با یکدیگر به قصد برهم‌زدن امنیت کشور» به چهار سال حبس و با اتهام «ارسال فیلم به شبکه‌های مجازی بیگانه برخلاف امنیت ملی» به پنج سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/78127" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FY2_SmmtH17zuhO9r6nJi7H1urCCppwgJhVIn5cMDVVh0yI82QBJjh7KMon1Sl-boq02SlPfHe3EaqqwYsEh9n8dnx3YKLec-25VrFbQUq8xen50ENLdTFtuy3AUwn43-5yQnRDCZrPtjFaPHr7rafbDUxGffBiCE2ub15wCWi-JVmYzSqAz2oWkvbbCLlDzNsqgbG3LO0SFpBBRwQEGfEjhCfuu2nMuOEnhgT9cBhkqxgr7eecF_pDC1EjmrD2Xfx8VyJcLQsTnZPogdAZ7j8gZy9Uj7nwe6HocSbx7Kbs4JPzHz8vajmB8_AsCpxJjlq7CeLTKPw-79sfmoNnIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=nvUPLPxEExWkzEt20UUoyIv9E6PPU_psRAc18K0eJRgtZkXuJ105Z-ULfk4TzhEwd7fFbOIu6vLsAzACYZZOJGmW8Wab1qxAasLMo8pl9_EpMWD5KCzFuJGUQpqVMU2dg3PTx_gg6-5vbXLRkf3AmWNoadpkV9OX4Z3wHuaPeaVUktOZbcsvO6CGkv4ZYZ--oKWonLOFl4dXXItv8azanTmudj-ws7vrECSLwnWQuMNYLQsOa_iMUF8pYmg0EPCnbeIUVhBVwYh2EW7ptq1KBHD31cFpkqhpXngH3nx_iuaELHEKLxL_xK3bqSF0OaKZISn90gT12Lq7GXK9mSW4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=nvUPLPxEExWkzEt20UUoyIv9E6PPU_psRAc18K0eJRgtZkXuJ105Z-ULfk4TzhEwd7fFbOIu6vLsAzACYZZOJGmW8Wab1qxAasLMo8pl9_EpMWD5KCzFuJGUQpqVMU2dg3PTx_gg6-5vbXLRkf3AmWNoadpkV9OX4Z3wHuaPeaVUktOZbcsvO6CGkv4ZYZ--oKWonLOFl4dXXItv8azanTmudj-ws7vrECSLwnWQuMNYLQsOa_iMUF8pYmg0EPCnbeIUVhBVwYh2EW7ptq1KBHD31cFpkqhpXngH3nx_iuaELHEKLxL_xK3bqSF0OaKZISn90gT12Lq7GXK9mSW4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.
بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی از بابت اتهام «افساد فی‌الارض از طریق اقدام گسترده در انجام فعالیت‌های سیاسی، ایجاد انعکاس خسارت تصنعی، تهیه اخبار کذب، تبلیغ علیه نظام، برهم زدن امنیت و ورود و خروج غیرمجاز به کشور» صادر شده است. حکم مذکور در تاریخ 1شهریورماه ۱۴۰۵ به وی ابلاغ شده است.
آقای زارعی دوزدره‌سی که پیش از این در آلمان به سر می‌برد، در تاریخ ۸ اردیبهشت‌ماه ۱۴۰۵، پس از ورود به ایران توسط مأموران اداره اطلاعات بازداشت شد.
پرونده وی در مرحله تحقیقات مقدماتی در شعبه سوم بازپرسی دادسرای ناحیه ۳۳ تهران، موسوم به دادسرای امنیت، مورد رسیدگی قرار گرفت.
وی نهایتا در تاریخ ۹ تیرماه همان سال به زندان قزلحصار کرج منتقل شد. این زندانی در حال حاضر در واحد سه، بند ۳۷ این زندان نگهداری می‌شود.
علی زارعی دوزدره‌سی، حدودا ۲۷ ساله و ساکن تهران در جریان اعتراضات سراسری سال ۱۴۰۱ یکی از چشمانش با شلیک گلوله ساچمه ای آسیب دیده بود. وی پیش از این نیز سابقه بازداشت و برخورد قضایی را داشته است.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78123" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YqwhY-1DUp1459Fb1rvgzZx0-QiVaKvLEcVUf6-nkh3r0n51NMWhoUadMBQ6Qty-RT-UFKdn9NFzZBmQV1FvNjdXL8NANHjkVe1E-m40LTLenS6OJxLX4ZY3lU2H-qsRddVSU7-e28aed12PQmuDNz_a3KvtoaBKNryPl5-wveDQtanCyF0HJqGHlxdZtxAknPbr8D8lGAVyjdhcPQMW3vG7vxhpgz8g9-3fVNz69djlOmZgpESB-CX-2s9SNMCaw8msyryUPGV8j83o1pECMqskjRCxayGWPINywywJ882v7bUxtfIAHbZAJqEIWeWIktEcN-3PT1D21SEKnxT2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک نفتکش در تنگه هرمز «هدف قرار گرفته است.»
براساس این گزارش، این نفتکش «هنگام عبور از تنگه هرمز و خروج از آن» هدف قرار گرفته است.
سازمان عملیات تجارت دریایی بریتانیا گفته این حادثه در فاصله ۳۱ کیلومتری شرق منطقه خصب عمان، «هدف اصابت سه پرتابه ناشناس قرار گرفته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78122" target="_blank">📅 03:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78121" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f2IQBQF-DWjDwrkGN_pFpKtUfJvXr7OGU8y9ux7urES_MoRVy-4K1__b5aGFjA-W-D3htWeNBiH5S1EikMmvYSL4CpAA-4S0URsbp9sGXGJSxQh44uQL92EPC-F6Ip-kx5XZNeHDok-YQDRd7oUx6XuHSNHEiqcGsRv-3X7Ut8_t0P4DTJAejcKRjBhcDJIHxrpY_La-EmzLZdfHoKysaQHiEndMOQ6aiMKAGaUGUorQ8t38QKOWWsef7WrFenO68_OR0pmMqVTJCxN5xfky4qk5M9zkYlxYOMPNeLqeRl9901FRrjRMbmbveG9CdhvLuGxJ7S13YbIt2v4-hfaKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه مقام آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهور آمریکا، و مشاوران ارشدش در حال بررسی انجام حملات محدود در تنگه هرمز برای جلوگیری از بازسازی توانمندی‌های راداری و موشکی جمهوری اسلامی جهت حمله به کشتی‌ها هستند.
بر اساس این گزارش، این طرح که طی هفته گذشته توسط فرماندهی مرکزی آمریکا تهیه و از سوی وزیر جنگ، پیت هگست، حمایت شده بود، پیش از تبادل آتش این آخر هفته با ایران به تایید ترامپ نرسیده بود. اما او ممکن است پس از تشدید جدید تنش‌ها با آن موافقت کند.
یکی از مقامات آمریکایی گفت ایده اصلی این طرح، کاهش خطر حملات تهران به نفتکش‌ها، شناورهای نیروی دریایی آمریکا و هواپیماهای نیروی هوایی آمریکا است؛ به گفته این مقام، هدف «کوتاه کردن چمن» است.
یکی از مقامات کاخ سفید گفت: «رییس‌جمهور همه گزینه‌ها را در اختیار دارد. ایرانی‌ها می‌خواهند توافق کنند، اما همیشه یک روز دیر و یک دلار کم می‌آورند.»
ترامپ عصر دوشنبه به فاکس‌نیوز گفت که آمریکا به حملات جمهوری پاسخ خواهد داد و «آنها را به‌شدت هدف قرار خواهد داد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78120" target="_blank">📅 22:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78119">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDdcL6tsEZIIYpVisZGGRESHhjQnsSLi1IxpT1k78V80FnZ-C9dAF8AQI3bfDH2JNkhbbHwzhoKmml2-RHbMAbjpP8MxhXUl6KscODdJ-yPGAZt2_tnxRALCcE0l_c2LwOdCkL3SiP7jn5ZAaI2XWRjFBaFYRPhjQzinVkFK2XmjxWCqkjfvahI7NrwkmWWDV2R8KXNa3Br3FRusenwpSKTzbjWqW6rO0hro6ch04iEkBkw5ZbU6jIwXR3ms-myqp5xx_vZOVr7PNWTx9j4WkJ5CUgjGtRfl1_s3_a2fewDYc7PW2Hf4IC76MTFMXGMzYDWmTEL44SyoE7MA6I7-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح جمهوری اسلامی روز دوشنبه در بیانیه‌ای مدعی شد که ایالات متحده از آسمان یا خاک برخی کشورهای خاورمیانه برای استفاده از ایران استفاده می‌کند و هشدار داد آنها را هدف قرار خواهد داد.
این بیانیه ساعاتی بعد از آن منتشر شد که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد ارتش این کشور به حمله شب گذشته ایران به نیروهای آمریکایی در اردن، ایران را به شدت هدف حملات انتقام‌جویانه قرار خواهد داد.
ستادکل نیروهای مسلح ایران در بیانیه خود گفته است «ضمن احترام به حاکمیت ملی همسایگان»، در صورت ادامه حملات آمریکا، نیروهای نظامی جمهوری اسلامی «پاسخی سنگین‌تر» از حملات شب گذشته خواهد داد.
ارتش آمریکا اعلام کرد شامگاه یکشنبه «نیروهای مین‌گذار سپاه» در جزیره لارک را هدف قرار داده است. در پی این حمله، سپاه پاسداران از حمله موشکی به دو پایگاه نظامی در اردن خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78119" target="_blank">📅 22:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LE2SunMxhT8sPzmrgEWpkIo8WGuEr68rAZ3FZbtLuqgC30KUQLdHTgaWt2H0K7BJVgFirQois3I2y9hSPXzE9FD7g0Xe_99fnO9ZVrVo9g6S10kjuR7auKbm_OavvfCtRBHAH9UuylZSgyytHqUlILMw7_aDfC4CyIFvJx-XTsnaDqHrvqH-3jLDXR1oLHOoWHwm6TEoyLLOZ73ZZ0ElcodRFio4JD8R4VM1Mj04nkgySVKlv_YyfdXmgYnkCwWvpWy0yY3tRBLIKbHmJX79OBjCyGKWts5zPJihhN7pbuP1oYJkDeK0wD_uF_a35ZxuaN55diNW6M-yPgNcizocbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه عربستان سعودی روز دوشنبه نهم شهریور در بیانیه‌ای اعلام کرد که کشور‌های عربستان سعودی، ترکیه و پاکستان توافق کرده‌اند در قالب «پیمان دفاعی مشترک مکه»، دبیرخانه‌ای را در عربستان سعودی تاسیس کنند.
بر اساس این بیانیه، ریاست این دبیرخانه در سه سال نخست بر عهده دبیرکلی از کشور پاکستان خواهد بود.
در همین راستا، وزارت امور خارجه ترکیه نیز اعلام کرد که تنظیم سازوکارهایی برای پیوستن سایر کشورها به این پیمان، در دست بررسی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78118" target="_blank">📅 19:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=IgSIGdRNKwIkW7ekahuYw-zo-S5Wk_6cBQwwxOPn5nMoXhrgTxb3crHLFncQZWOTu_5bEr3MwEr2bH5fAh_rOpCrkvQJ00R8sRgb356E5Yc8o0gSYn-WEKFSAh5C1va0LXKIQdp4cFfURwok9Y9ZQk31DGnzWkmhj7hnCb9UX8WB7dPUqaMB6u0LILSqm-NfbPhlEOIgk1s4R06zbgpjxBSmqRKmputO6hCDyx53QtBMusMybWvG26Jqkyg5i6VDT4-14B1_WCDpeeaYyPMJCoDcPs6tpN6M4L6A2LSe8080_T5UrHGOnT9PTpyavhCrXbe1Ho0MarWmNADfyCvc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=IgSIGdRNKwIkW7ekahuYw-zo-S5Wk_6cBQwwxOPn5nMoXhrgTxb3crHLFncQZWOTu_5bEr3MwEr2bH5fAh_rOpCrkvQJ00R8sRgb356E5Yc8o0gSYn-WEKFSAh5C1va0LXKIQdp4cFfURwok9Y9ZQk31DGnzWkmhj7hnCb9UX8WB7dPUqaMB6u0LILSqm-NfbPhlEOIgk1s4R06zbgpjxBSmqRKmputO6hCDyx53QtBMusMybWvG26Jqkyg5i6VDT4-14B1_WCDpeeaYyPMJCoDcPs6tpN6M4L6A2LSe8080_T5UrHGOnT9PTpyavhCrXbe1Ho0MarWmNADfyCvc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا ویدیوهایی ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.  ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»  این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر…</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78117" target="_blank">📅 19:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=NLxx6NiujuVrYWw61Y3wkQ8hU3F3yjRShecCusKIkr7ASv5qfOyDisktRqh80dtE2c3PqPoyntSVUjBRQ9Gak36yzNPa_G5srJ0uPVe4pKyPcnkIs6eqnyi90exjlwzySjW98vO5QEGIZpHX88AsuQJqMZpSUTFkR0UmgJ7a5McPsl3bXDN0_CkSKBIxY9Ywcbyy-bgP0rGFKI6-SLPmwN2dXcow3YwYnbbKgNPQhp1iSzUy1hsblGPxS1WU7zsbWlzLLeLsB_3csAT-Si3lWVFFkaNfm6KhUIckM8JFdn19lPsio_KKmpZJQzIbEDTlhQqS1xVv9cjaQyoqCtsbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=NLxx6NiujuVrYWw61Y3wkQ8hU3F3yjRShecCusKIkr7ASv5qfOyDisktRqh80dtE2c3PqPoyntSVUjBRQ9Gak36yzNPa_G5srJ0uPVe4pKyPcnkIs6eqnyi90exjlwzySjW98vO5QEGIZpHX88AsuQJqMZpSUTFkR0UmgJ7a5McPsl3bXDN0_CkSKBIxY9Ywcbyy-bgP0rGFKI6-SLPmwN2dXcow3YwYnbbKgNPQhp1iSzUy1hsblGPxS1WU7zsbWlzLLeLsB_3csAT-Si3lWVFFkaNfm6KhUIckM8JFdn19lPsio_KKmpZJQzIbEDTlhQqS1xVv9cjaQyoqCtsbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه نهم شهریور ماه در حاشیه نشست «جی ۲۰» در اشویل آمریکا گفت واشنگتن به اعمال فشار اقتصادی بر تهران ادامه خواهد داد و ممکن است نتایج این فشار طی هفته‌ها یا ماه‌های آینده نمایان شود.
بسنت در پاسخ به پرسشی درباره زمان احتمالی فروپاشی اقتصاد ایران گفت: « مسئله این است که ما محاصره را داریم و به اعمال فشار ادامه خواهیم داد. ما همین حالا گفتگوهای بسیار خوبی در اینجا داشته‌ایم و فکر می‌کنم این می‌تواند طی هفته‌ها یا ماه‌ها رخ دهد.»
وزیر خزانه‌داری آمریکا افزود: «اقتصاد لزوما نباید فروبپاشد؛ فقط باید حکومت ایران به خود بیاید.»
این مقام آمریکایی افزود بسنت در حاشیه نشست گروه ۲۰ با همتایان خود دیدار خواهد کرد و برای افزایش فشار اقتصادی و منزوی کردن ایران تلاش خواهد کرد.
اسکات بسنت، در ادامه با اشاره به حمله ایران به پایگاه‌های نظامی آمریکا در اردن گفت: «به نظرم آنها به‌صورت نظامی دست به واکنش می‌زنند، چون از نظر اقتصادی در حال شکست خوردن هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78116" target="_blank">📅 19:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=OmPZ35-8PKbfjM2_W3fXS8rw-QsnWjkpzLqDABYPd9oR3iEAFkstCjEhMLn7BYN2b4czewiRwa8YdiQu8PjyE4BGZDviKC0f-2xn_ZjV-pODd_aHPVU--Zg-JOd7-gfix1ZrAvgUMVJDoQ7p1PQZkFCKahWC1QXwQqrus4BtyCHqxCDHFLR4YkBWJJFrWFoU-64tsGaCVVyaycMxJaKo3qLkp_AHBXxLbqfqXMfS9zIm-glKpN2LkMv-LYBiMt-oicsp_bA2ptHXnY1E1j4czc6fTNduZ5DCKwgKCi_PRzLdDDrMd0RBKt677XmYe2mbm4dpVkZXJR4YNWz0DvRGuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=OmPZ35-8PKbfjM2_W3fXS8rw-QsnWjkpzLqDABYPd9oR3iEAFkstCjEhMLn7BYN2b4czewiRwa8YdiQu8PjyE4BGZDviKC0f-2xn_ZjV-pODd_aHPVU--Zg-JOd7-gfix1ZrAvgUMVJDoQ7p1PQZkFCKahWC1QXwQqrus4BtyCHqxCDHFLR4YkBWJJFrWFoU-64tsGaCVVyaycMxJaKo3qLkp_AHBXxLbqfqXMfS9zIm-glKpN2LkMv-LYBiMt-oicsp_bA2ptHXnY1E1j4czc6fTNduZ5DCKwgKCi_PRzLdDDrMd0RBKt677XmYe2mbm4dpVkZXJR4YNWz0DvRGuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز دوشنبه ۹ شهریور ۱۴۰۵، شماری از شهروندان جویای کار در شهرستان گچساران در اعتراض به روند استخدام نیرو در پالایشگاه لیشتر تجمع کردند.
در ویدیوی منتشرشده از این تجمع، تیراندازی نیروهای انتظامی برای متفرق‌کردن معترضان دیده می‌شود. برخی گزارش‌ها نیز از زخمی‌شدن یک نفر در جریان این تیراندازی حکایت دارد.
این تجمع در اعتراض به نحوه جذب و استخدام نیرو در پالایشگاه لیشتر برگزار شده است؛ پالایشگاهی که به‌تازگی افتتاح شده است.
@
VahidHeadline
نیروهای امنیتی و پلیس، جوانان عرب معترض به بیکاری در مقابل شرکت نیشکر «دعبل خزاعی» در اهواز را با ضرب‌وشتم و تیراندازی متفرق کرده‌اند.
در این ویدیو، مردی که در حال فیلم‌برداری است می‌گوید: «این جوانان همه گرسنه هستند، هیچ‌کس ما را استخدام نمی‌کند. هیچ‌کس برای ما ارزش نمی‌گذارد. هر کدام از آن‌ها با اسلحه کلاشینکوف به‌دنبال جوانان افتادند. ما کار می‌خواهیم. جوانان گرسنه هستند. ما هیچ آهی در بساط نداریم. ما کار می‌خواهیم.»
سازمان حقوق‌بشر «کارون» روز دوشنبه نهم‌شهریور۱۴۰۵ در گزارشی نوشته است که «جوانان و خانواده‌های معترض که به نمایندگی از ساکنان همجوار این شرکت دست به تجمع زده بودند، با طرح مطالبات خود اعلام کرده‌اند که شرکت نیشکر دعبل خزاعی در زمینی به مساحت حدود ۱۲ هزار هکتار فعالیت می‌کند که بخش قابل‌توجهی از این اراضی متعلق به منطقه و مردم بومی آن است. با این وجود و علی‌رغم حضور جوانان بومی دارای مدارک تحصیلی و تخصص‌های مختلف، مدیریت شرکت اولویت را به جذب نیروهای غیربومی داده و باعث شده تا جوانان منطقه همچنان از فرصت‌های اولیه اشتغال محروم بمانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78114" target="_blank">📅 19:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QH33fmNWMf1mA8w1hogo-fo2Rl-IF_Wd94D2ObtHAH6fZq_n04La_ZbohaGWhmJsN4XDcB99TIuV6rRrPEeKCIa09oXvCg8UYYMg87i_Nd3ZRdqBb7RxAOoxHdVDzLlS4iBajQYLC5J2iyFuPcXRBSl8FmReN1sApX6e_tUJTBXq3fF6joKJ3oCsxXUpyLr4YgHxqUIThOXh8fM2WSgi9zeuUIyAxnyfjqKa5novc9szeN4ZHPpSjeQ-KAsjU2EeBzl-MmbiPYWXU_1ceS6zdHSGr_WoFF3dO_yEVlIE_o-BxxBVF18kmmw4u-WgDMlPlJbuSdzcvgIvlSVtthMkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rial2JkS3cBLG67_8GY09QlQHgnlFRU9xsaLJ-fU0ExpMUbLvnBtPdlldzIuso8O268F8POO2CSC_CAILezubQ6D3PQc1o7EwsxPyXaiv_DaWCK0gn93sJvpLGfE_4T1fYx1c88Hp60Rwb6efMGTjuBQoh9h6CzTM7OXOzzHlFeVtgPunLOnbmwAm8ToWurRSCQr6UhVOgSyPE6n9KKC1PSwLsaCRL5e0QYz2-I2QjiHQBy6xSKf0VJGqUmcLHdAg7XpXS1sZBHlyeuMkYW_SSfvzLhghOZlAN62viESN7qIMtol2UfDicT3ynBGB2juAxePwVHm9KKkk9-eU3wZYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اژه‌ای معترضان را به برخورد قاطع‌تر تهدید کرد
در پی تشدید بحران اقتصادی و رسیدن دلار آمریکا به مرز ۲۱۰ هزار تومان، رئیس قوه قضائیه جمهوری اسلامی گفت این نهاد برای مجازات «عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است».
این تهدید پس از آن صورت گرفته است که دستگاه‌های حکومتی بروز اعتراضات مردمی را پیش‌بینی کردند.
غلامحسین محسنی اژه‌ای افزود تحکیم امنیت و مقابله قاطع با عناصر ضدامنیتی از مقولاتی است که مردم و مسئولان درباره آن اتفاق‌نظر دارند.
این رویکرد با پیام مکتوب مجتبی خامنه‌ای در هفته دولت تشدید شده است.
خامنه‌ای در این پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با انتشار گزارشی به حضور «شماری از دانشجویان زن بدون حجاب اجباری» در جلسه رییس سازمان امور دانشجویان و مشاور وزیر علوم اعتراض کرد و خواستار «واکنش قاطع و فوری» وزارت علوم و واکنش نهادهای امنیتی و دستگاه‌های قضایی شد.
به نوشته فارس، انتشار تصاویر جلسه‌ای با حضور رییس سازمان امور دانشجویان، مشاور وزیر علوم و شماری از اعضای شوراهای صنفی دانشگاه‌ها که در آن تعدادی از دانشجویان زن بدون حجاب اجباری حضور داشتند، «با اعتراض گروهی از استادان و دانشجویان» مواجه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78112" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQiA1B2ZU9VH4rkDySnPi6vgEiEhM8eByH2L0u9A87Xl1-qPGeeflsch-YIYeDrFAUcAlod0YCK38MnNxAAYt_O9flTiC0ycyJ7na5KsPQ2_mKyzdMFedaYlJlczozbQ5jZQq9kinrxUY0S4Lopdi9iakAp_fBfMxzzllkgQWkwbMxAqlxysbbItxOU4MO7kWd2oeSwwK9acbN7kjPhWQQDH9yypz26wiUc2aq1f6S17iBPSsNCP4To6hWmnjsegE1IFtwMmg-09Sa8f--1vCmxRv2HPio5lLGlpryNd1kCqC9OnAnKj7cDp-NNwyV0RCctmWss-XDRNh6f8pUU0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا روز دوشنبه اعلام کرد که به همکاری با ایالات متحده و سایر شرکای بین‌المللی و گروه هفت «برای حفظ فشار بر ایران و کمک به کاهش تنش و ثبات منطقه‌ای» ادامه خواهد داد.
در این بیانیه آمده است:‌ «اتحادیه اروپا از تلاش‌ها برای اطمینان از اینکه ایران فعالیت‌های بی‌ثبات‌کننده خود را متوقف کند و با حسن نیت در مذاکرات صلح شرکت کند، از جمله از طریق فشار اقتصادی بیشتر، شامل عملیات طرد اقتصادی به رهبری ایالات متحده، استقبال می‌کند.»
«عملیات طرد اقتصادی» عنوانی است که مقام‌های دولت آمریکا بر برنامه فشار اقتصادی تازه بر جمهوری اسلامی گذاشته‌اند.
بیانیه اتحادیه اروپا در آستانه آغاز نشست گروه ۲۰ به میزبانی آمریکا صادر شده است.
اسکات بسنت، وزیر خزانه‌داری آمریکا به خبرگزاری رویترز گفته است در این نشست از وزیران دارایی و روسای بانک‌های مرکزی کشورهای جهان خواهد خواست تا روابط اقتصادی‌شان را با ایران قطع کنند؛ در غیر این صورت با تحریم‌های ثانویه آمریکا روبه‌رو خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78111" target="_blank">📅 17:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3skWQovf_vHLyme6UAD_it36DTYgmpD80jUg-dVlbbNqO3d_s9porApGm3OhT5vDRnB8ZH1x0zhQjy5txgTsJQ-0oGTd0FQDJjGvi-1lsVPmJPJrg9VZsoM99Tp-0_PhyF7ekQQ9AJ-Rws7rPKVPX9Nn7bqnlgDnNZxYwjwCERiDY8PzUBc89TpI3aLB38ltEzMPEvUpceAcD5ndHkpWab7DZoOmhT4wwnrCFFBnwBW0pLNjowxaJe_-yTeVwfCrQPhqqsWj2q9UDyzvHARiV8ugeDZU5OZ2EhM5z33kyRQs3Yx0rqpUUIsITTaKq2LKvdqZKhvf6IRHMZ5U-5tPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روند نزولی ارزش پول ملی در ایران، قیمت دلار آمریکا دوشنبه، نهم شهریور از ۲۱۰ هزار تومان عبور کرد.
همزمان پوند بریتانیا از ۲۸۴ هزار تومان عبور کرد و یورو نیز به مرز ۲۴۳ هزار تومان رسید. قیمت هر سکه طلای طرح جدید، موسوم به «امامی» نیز از ۲۲۳ میلیون تومان فراتر رفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78110" target="_blank">📅 17:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M5nVxCQIJyGvIZF42tLYnqJx-hcLujBXMe2TgO7cl7mKzPAEQF-jCIhBm4lwFfxMVwdtLkZeOWl9114nTGSoh_BcUZmfCEYuoUO8Va4N9n5rE7RmBjW8Kegm4OJh8XWy6AOZiXmngDsKUPCflHjmzGgiw_Elqrk6Xg6bsb-PcsvtQaFyyrgxlCFMCpNTZh_wpX3DhemdLyKYq1W8pkslOXJ8DpJWmvDFJeZzBRO2Lg3Y5A9VFMQLbTVtTqJqSzdE2IWRmytxs5lEVhvfI83DroddXY1SYLhXd_mEVDj3qDf3n_zyAj9ouR7E5CdDT_P7dkDFWvyClzYwinqx2szfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران (IRGC) ادعا می‌کند که یک ابرنفتکش هنگام عبور از مسیر جنوبی تنگه هرمز با دو مین برخورد کرده و کاملاً متوقف شده است. این ادعا
نادرست است.
✅
واقعیت:
هیچ کشتی‌ای در تنگه هرمز با مین برخورد نکرده است. این نیز یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه از طریق انتشار اطلاعات نادرست است.
CENTCOM
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78109" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78108" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QkTzJ8la7qxf4tlKEFUufLvYNCV2PB9ziNQ8rSVLG7KQ94rd7uGSXcsQzLwuuGlsc8f0EJSGjgkS4-e-gnapcw8UExEEcw-K_HJSSlikKyofDUp2xJNjS-voR0E495hWC6s3svPOVZYc3YTSnmAd2PnAEOdU4l7sDcPjZlx_yJNA8zN38kWMN6xqpczAgz8GoW0_wVeD_dWJkWRbOgu2eg7P-IA2IrcBCq0azdkOQDF9uQlfQ1DONDQaMg-iK9_oL0jQSsSddC8imMJbeYvWJaE2WMrz15q_kFI9Fqr7P7FN0eb7m9G9_iVGOnx-pjcNGVoHgWUY0mChjhI_0KeCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه نهم شهریور، در شبکه اجتماعی «تروث سوشال»، جمهوری اسلامی ایران را رسما یک «کشور شکست‌خورده» خواند و خواستار محاکمه بین‌المللی رهبران آن شد.
ترامپ وضعیت ساختارهای اقتصادی و نظامی ایران را «فروپاشی کامل» توصیف کرد و نوشت: «ایران دیگر نه نیروی دریایی دارد و نه نیروی هوایی؛ ارز آن‌ها از دست رفته، حقوق سربازان و نیروهای پلیس پرداخت نمی‌شود و تورم به ۳۰۰ درصد رسیده است. رهبری آن‌ها در آشفتگی مطلق است و توانایی اداره کشور را ندارد.»
رئیس‌جمهوری آمریکا در ادامه با متهم کردن تهران به سرکوب خونین اعتراضات داخلی افزود: «تنها کاری که آن‌ها بلدند کشتار معترضان خود است که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است. مقامات تهران باید به اتهام ارتکاب جنایات جنگی علیه بشریت محاکمه شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78107" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
