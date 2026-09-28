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
<img src="https://cdn1.telesco.pe/file/TvKSjq4IrTwK9nepvfb3YZ_WSi2PVE-l5iiVW6Cl1N8VUOyzXk7oCrF8-NFMW4fIRey9086dwxMqVxTiF8A5wNSMf1zT8P02aIKPUv8uCYQS06-MJ2VIZl1JU82ovbSfqK47auJT3RPcZZvC38MtKFQ2ZFM2R9keRs0VDBZqOFb5HyPUFgeagdLdk_qdT9YbpoVvjGTdlhFgJnVTLrGnUycXPz8nn3gjiLbfOzlE255Tuj2_QHP1aewoGdBZzgZQQW_UHVv9LkpuVS1gJTPjM_-Ww3ZbaU-b7Djlm8-U_8hYngQWaakUSTfh3R6Bvmr0Qe8jgTzDD8TtH1KgSmDezQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eK7VAxPSKlCjtXxN5E-e7i7yYADPOpdJmMDqIlJMFKk3eSOFRg5jwSACcsGC_IC-BUGJ8MeRv68w8aWh2ZdMHHK5O3LRLTq12BYII3fJsu4s5VyDXWu6ikbF-iFYmDHMrdKjbz86yvpriX84Hm_fBAZgH2Lta1PUy5326JnbpMDaxqOW_FG_RNZgI-8Pbcb_Flj5zdGre-IaNX8QGrtylcRLYorFbuNkfP5Jv8qDCyzoE6EPHXiMODf7a1YzqpFHOFn2_BKuBRQ8oBnVUFOhsQhNCPUd5eI7yXXHwpVHX2JPRmpsNb7GWPPq5Zm1m1sA0qFJ1r2H7uldFYtBScMwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=pFAqZf4OqrKswkcZRxQOcJEYO-fnKhO-gMNP7iQcq20qrVK-DpnOIBodq89UlOx__4LchEmfLYyZ5y03bispCQ5JjsQczFq19sXoN_1ge7JzldbL8M5tsIZvvv1QjLQxh-WpXZOS_norfhr-vO10wXOtsp9W2YkskGRjPGNPiVtkGS7rib_b0CNyiEd_GiokTvBVNpEv-Y5R7sEU6HjufAdNvzCUBisNEfWdDY8MsFJ2YMOj_phC1uIZQbaUHIrYnfxxNfF8cm8pRz0puPdkzZnXEhbjfA9BcrPvS7sw1QsQWqn_4ZjVErBlYJjG_-R0zaaMCk9Mt9_QWZVmlcvn_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=pFAqZf4OqrKswkcZRxQOcJEYO-fnKhO-gMNP7iQcq20qrVK-DpnOIBodq89UlOx__4LchEmfLYyZ5y03bispCQ5JjsQczFq19sXoN_1ge7JzldbL8M5tsIZvvv1QjLQxh-WpXZOS_norfhr-vO10wXOtsp9W2YkskGRjPGNPiVtkGS7rib_b0CNyiEd_GiokTvBVNpEv-Y5R7sEU6HjufAdNvzCUBisNEfWdDY8MsFJ2YMOj_phC1uIZQbaUHIrYnfxxNfF8cm8pRz0puPdkzZnXEhbjfA9BcrPvS7sw1QsQWqn_4ZjVErBlYJjG_-R0zaaMCk9Mt9_QWZVmlcvn_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز دوشنبه ۶ مهر ۱۴۰۵، در کاخ سفید گفت آمریکا «خیلی زود» در جنگ با جمهوری اسلامی پیروز خواهد شد و پس از پایان جنگ، قیمت بنزین به‌شدت کاهش خواهد یافت.
ترامپ گفت: «این جنگ تمام خواهد شد و ما در این جنگ پیروز می‌شویم و قیمت بنزین با سرعت زیادی پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست چنین کاری را انجام دهد.»
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت آمریکا مانع دستیابی تهران به سلاح هسته‌ای شده است و افزود جمهوری اسلامی این موضوع را می‌داند و حاضر است به آن اذعان کند.
@
VahidHeadline
متن زیرنویس، ترجمه ماشین:
ایران هرگز سلاح هسته‌ای نخواهد داشت. ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام می‌شود و قیمت بنزین به‌شدت پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست این کار را انجام دهد. هیچ‌کس دیگری.
اگر دموکرات‌ها سر کار بیایند، مرز فوراً باز خواهد شد و میلیون‌ها نفر درست مثل قبل سرازیر خواهند شد. این وحشتناک‌ترین چیزی است که در عمرم دیده‌ام.
بله، آنها حاضر نبودند جلوی ایران را بگیرند که سلاح هسته‌ای داشته باشد. گفتند: «بگذارید یک نفر دیگر این کار را بکند.» البته این را درباره خیلی‌های دیگر هم می‌توانم بگویم. ما جلوی دستیابی آنها به سلاح هسته‌ای را گرفته‌ایم. آنها هرگز سلاح هسته‌ای نداشته‌اند و این را می‌فهمند و حاضرند آن را بگویند.
وقتی جنگ تمام شود، دو اتفاق خواهد افتاد. اتفاق اول در واقع همین حالا هم افتاده است: ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع بسیار بزرگی است، چون اگر می‌خواهید آشوب و فاجعه ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. نباید بگذاریم با سلاح هسته‌ای به ما حمله کنند. برای همه آن آدم‌های احمقی که فکر می‌کنند اشکالی ندارد، من با آنها سروکار دارم و آنها دیوانه‌اند. هیچ تردیدی در این نیست. آنها آدم‌های بسیار دیوانه‌ای هستند. همیشه این را به خودشان می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.» اما آنها نمی‌توانند سلاح هسته‌ای داشته باشند و ندارند.
پس این موضوع بسیار بسیار مهم است که ما در چنین وضعیتی قرار داریم. این کاری است که سال‌ها پیش باید توسط رؤسای جمهور مختلف یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم، اما ما با فاصله قدرتمندترین کشور جهان هستیم. بهترین تجهیزات نظامی جهان را داریم.
و ضمناً، اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات نظامی تولید می‌کنیم. چاره‌ای جز این نداریم. شرکت‌های بزرگ دفاعی در حال گسترش فعالیتشان هستند. مثلاً لاکهید پنج تا می‌سازد. ریتیان هم تعداد زیادی می‌سازد. همه‌شان دارند مقدار زیادی تولید می‌کنند. اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات در راه داریم و به‌زودی واقعاً تولیدشان شروع می‌شود، چون این کارخانه‌ها قرار است شروع به کار کنند.
قیمت بنزین خیلی پایین خواهد آمد و همین حالا هم، می‌دانید، اگر نگاه کنید، فکر می‌کنم پیتر، این صددرصد است.
پس ما ارتش ایران را از بین بردیم. تقریباً هرچه داشتند را از بین بردیم و هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ما بدترین تورم تاریخ را داشتیم. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که در دوره بایدن شما برای بنزین خیلی بیشتر پول می‌دادید.
بیایید درباره همه این چیزها، می‌دانید، همه‌چیز صحبت نکنیم. در دوره بایدن، شما خیلی بیشتر برای بنزین پول می‌دادید تا الان.
و کاری که من کردم این بود که وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاق‌ها برای جهان، برای ما و برای بقیه جهان باشد. اسرائیل الان نابود شده بود. دیگر اسرائیلی وجود نداشت. دیگر خاورمیانه‌ای وجود نداشت. و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا می‌آمدند. و من جلویش را گرفتم.
و این آقا داشت ۱۸ میلیارد دلار در آیووا سرمایه‌گذاری می‌کرد. او می‌گفت: «من می‌خواهم از آمریکا صرف‌نظر کنم. قرار نیست ۱۸ میلیارد دلار خرج کنم»، چون ما یک دیوانه و یک کشور دیوانه داشتیم که با سلاح‌های هسته‌ای این طرف و آن طرف می‌گشتند، چون قدرت بسیار زیاد است.
اما هیچ‌کس درباره‌اش حرف نمی‌زند؛ هیچ‌کس درباره همه آن کارهای باورنکردنی حرف نمی‌زند.
باز هم، خیلی از شما... نمی‌خواهم بپرسم، چون می‌گویید: «اوه، ما قرار نیست این را گزارش کنیم. ما رسانه اخبار جعلی هستیم. اجازه نداریم گزارشش کنیم.»
همه شما حساب 401(k) دارید. لازم نیست چیز دیگری درباره شما بدانم. حساب 401(k) شما در مدت کوتاهی دو برابر شده است. دو برابر شده. ثروت شما دو برابر چیزی است که مدت کوتاهی پیش بود؛ تک‌تک شما، و این به خاطر من است.
خوش بگذرد، همه. خیلی ممنون.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">"ترامپ در ازای امتیازهای مشخص هسته‌ای، به ایران پیشنهاد گشایش اقتصادی می‌دهد"
اکسیوس، ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، آماده است در ازای برداشتن گام‌های مشخص از سوی ایران در ارتباط با برنامه هسته‌ای، به ایران تخفیف تحریمی بدهد و دارایی‌های مسدودشده ایران را آزاد کند؛ مقام‌های آمریکایی این موضوع را اعلام کرده‌اند.
🔻
چرا مهم است:
پیام آمریکا به ایران در حالی مطرح می‌شود که میانجی‌های قطری و پاکستانی این هفته بار دیگر تلاش می‌کنند میان دو کشور در حال جنگ به توافقی دست پیدا کنند.
▪️
در حال حاضر، دو طرف بر سر مسائل کلیدی فاصله زیادی با یکدیگر دارند. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار آن است که ایران با امتیازدهی در زمینه هسته‌ای موافقت کند.
▪️
با این حال، این پیشنهاد پس از آنکه ترامپ آخرین پیشنهاد ایران را رد کرد، روزنه‌ای از امید برای دستیابی به یک گشایش دیپلماتیک ایجاد می‌کند.
🔻
تحولات اصلی:
میانجی‌ها امروز در نیویورک با عباس عراقچی، وزیر امور خارجه ایران، دیدار می‌کنند تا درباره پیشنهادی از سوی قطر گفت‌وگو کنند که طرف‌ها طی چند روز گذشته مشغول مذاکره درباره آن بوده‌اند.
▪️
انتظار می‌رود میانجی‌های قطری اواخر روز دوشنبه یا روز سه‌شنبه با مقام‌های دولت ترامپ دیدار کنند تا برای دستیابی به یک گشایش تلاش کنند.
▪️
یک مقام آمریکایی مطلع از مذاکرات غیرمستقیم، این گفت‌وگوها را «مثبت و سازنده» توصیف کرد و گفت ایران «نشان داده است که در مسائل هسته‌ای انعطاف‌پذیر است.»
▪️
اما این مقام همچنین گفت هنوز اختلاف‌هایی وجود دارد و تأکید کرد «تا زمانی که به مسائل هسته‌ای پرداخته نشود»، توافقی در کار نخواهد بود.
▪️
این مقام گفت: «طرف‌ها همچنان درباره زمان‌بندی تعهدات و اینکه چه کسی باید ابتدا کدام گام را بردارد، اختلاف دارند.»
🔻
آنچه می‌گویند:
این مقام گفت: «تردد در تنگه هرمز همچنان در حال افزایش است و محاصره و تحریم‌ها همچنان موقعیت ایران را تضعیف می‌کنند. موضع آمریکا هر روز قوی‌تر می‌شود و رئیس‌جمهور ترامپ همچنان صبور است و کاملاً به هدف خود مبنی بر اینکه ایران هرگز به سلاح هسته‌ای دست پیدا نکند، متعهد است.»
▪️
این مقام افزود که کاخ سفید نسبت به وعده‌های ایران بدبین است و ایرانی‌ها را متهم کرد که با شلیک به کشتی‌های تجاری در تنگه هرمز در ماه ژوئیه، آخرین تفاهم‌نامه را نقض کرده‌اند.
▪️
این مقام گفت: «آمریکا این بار به تضمین‌هایی نیاز دارد که نشان دهد ایران جدی است و صرفاً تلاش نمی‌کند از شرایط دشواری که در آن گرفتار شده، خارج شود.»
axios
🔄
آپدیت:
ترامپ تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=L09715iH-v45vNJ2SWmniLOqIuDv4mHLVGnQGyLmJxXjJWDZkcOOcdviLp2s04975l5od5Aj62SvHufT5djHzB0dy2LX7dNvz8qHz-78ckE3UqfUGURX9JrplH9LyZOMztzNrnKR1KbI8nAOCGgNaCLF8q-Epp3gUX4obzvaWUFcv_vp1rlp3lLbt16TB0-SHp88u2kNVealgEjxBAHje73j2JnR93tnCdIOcEmf5aJ_7rxf4ZnyNCCxNE58d51tknjGnTWGJgiDZ0oAgA_9VGaagaCuH14RJfk2tHM5CvvrbuvrUnUnElmjyX_-I3zj5dKlPJFaOqJnpRpeqXBumw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=L09715iH-v45vNJ2SWmniLOqIuDv4mHLVGnQGyLmJxXjJWDZkcOOcdviLp2s04975l5od5Aj62SvHufT5djHzB0dy2LX7dNvz8qHz-78ckE3UqfUGURX9JrplH9LyZOMztzNrnKR1KbI8nAOCGgNaCLF8q-Epp3gUX4obzvaWUFcv_vp1rlp3lLbt16TB0-SHp88u2kNVealgEjxBAHje73j2JnR93tnCdIOcEmf5aJ_7rxf4ZnyNCCxNE58d51tknjGnTWGJgiDZ0oAgA_9VGaagaCuH14RJfk2tHM5CvvrbuvrUnUnElmjyX_-I3zj5dKlPJFaOqJnpRpeqXBumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUbRt9Xn0Jxj7uzlGw255xd9MpJZWR1hCw1gr5mWy4uR0YV7uUTGluUCEiBCM_Q9QDWOCqwZrt6yzvVesi03VBxofFArRDCfcAvYOuxHwd6xxvRJcEBWgvHGfWSk36686CfK102fj0jr9_V-tYcJlWH5l0JqPz2rC7M4Jbk-1zES7e5FgNrMDaCwSfIlyVewErkIgCjFwIDH2Y6P4MrJ5sOD27rmEvl8q6Qx40uyEOJ0VI93_fT5REm9uVX3gJc7Il4YB_kV0WSZ1BlBgZzgRJ7HBPnJ9brPWSsJZceOp13usUz3R4aGjuCDDbzT5pYUlePSnuCdKg4ejIN0hLyM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRGMQHkOULSvitDyFCCfPpNf9fvuTaIfFAPryd9dSXPMGu4HxjO7ryrNHeyZabReudUqWcOwIvICUnl8sqTjed7vGHQ-JH2cK7dOReyA674M3n0ybv5j1Bv72LZGgJtnyTsg7TvTYbySEa2v3ID5fmWMiFTq5FppJIpcLZ3pwlmZ32dIQiRzbCoqznBWna5qOpLGV4DpcEVVkee4QSXqdmwDlsLXGtdR94gioMVFiF3yUK83uRdubaQnO_PS4qtkHY8E9fyiIGdJHpLaUYacBbBB23FbSB0fM7zrQRG31q5YQu-rbLDzAIaVIntEgHtsBMHWHMkDu1QJXvspN-wMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارز در بازار آزاد ایران روز دوشنبه ششم مهرماه تنها در چند ساعت بیش از ۶ هزار تومان افزایش یافت و دلار از ۲۳۶هزار تومان به ۲۴۲ هزار و ۵۰۰ تومان رسید.
سقوط آزاد ارزش پول ملی ایران، همزمان با تشدید تنش میان تهران و واشنگتن و در حالی که تحریم‌های همه‌جانبه و بی‌سابقه آمریکا علیه جمهوری اسلامی ایران ادامه دارد، وارد مرحله جدیدی شده است.
سایت‌ها و کانال‌های اعلام قیمت ارزهای خارجی گزارش می‌کنند که روز دوشنبه، یورو به مرز ۲۷۶ هزار تومان رسید و پوند بریتانیا هم رکورد ۳۱۸ هزار و ۶۰۰ تومان را شکست.
@
VahidOOnLine
قیمت دلار در بازار آزاد ایران ظهر امروز دوشنبه ۶مهر۱۴۰۵ از مرز ۲۴۳ هزار تومان عبور کرد و رکورد تازه‌ای بر جای گذاشت.
اما خبرگزاری «فارس»، وابسته به سپاه پاسداران، افزایش نرخ ارز را به اظهارات وزیر خزانه‌داری آمریکا، کانال‌های تلگرامی و فعالیت دلالان نسبت داده است.
دلار صبح دوشنبه از مرز ۲۴۰ هزار تومان گذشته و تا ۲۴۰ هزار و ۵۰۰ تومان افزایش یافته بود، اما تنها چند ساعت بعد قیمت آن از ۲۴۳ هزار تومان نیز فراتر رفت.
@
VahidHeadline
به نوشته هم‌میهن، قیمت سکه معروف به امامی نیز روز دوشنبه در کانال ۲۴۳ میلیون تومان قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFSLAfg8Jyr1sZJoKyYNA6gPZYHDkVZ7G_ZNtEvI_F6BXR0IL1ja3GdQY0_FoLJeTN8aknUYZIFct4IUQZ3HzZSVZJ2U8IYvf7PFNtMttO1Z9SfKMzPp_EgHrl9oW8jRQHNijpJ0r3dPTevnu2Xrwc4C8MmzsixcZoOS42HaIwo7GfXP-XpoheIRk5YeYQ-Xp_G0aA3xYwI33zV-5dqa_UMuzMlFpSwG0V8L2jPXY8qlfFiMDf3KQWQinsqvcBePSL2hMQF_5yLjnXocB_XPzJ_FQBclwXRSO8PJWwq15t1U7KEbeiHwiw201V59mSDuIVqIuZmTs-Ib3CPTJiubiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=dmSP0OboXSZ-4mRkoc4ODu61w2ywdziljlFLChHmwE3ddLC2-LzdVeCZ6XaF2RQJstQEM-rt9-SIAOh4QH1UyTWCb8pVTGo7A-nXKqvI2z-WnnRk8uEW6nvzmL6_m2PL-A2s_f77d9fjGWVh0VOozn0sBKIdqp7kE37fzRNrOoMkeJPC4RF1w7Xb3dYN6kDS_UbSfkBOokLICX3E1aOQti4mYOttVBCuypyOsnT9gHM4xJWXZebHOY7lIvmNiLSetJtTpSxUIgNRyLrirxNTdXPnhK1FBvYCGoPaodm0L8yvdex7kB1lZ_CObFPnGHolsCIS4OK9oMNNW5Zrfk0Wpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=dmSP0OboXSZ-4mRkoc4ODu61w2ywdziljlFLChHmwE3ddLC2-LzdVeCZ6XaF2RQJstQEM-rt9-SIAOh4QH1UyTWCb8pVTGo7A-nXKqvI2z-WnnRk8uEW6nvzmL6_m2PL-A2s_f77d9fjGWVh0VOozn0sBKIdqp7kE37fzRNrOoMkeJPC4RF1w7Xb3dYN6kDS_UbSfkBOokLICX3E1aOQti4mYOttVBCuypyOsnT9gHM4xJWXZebHOY7lIvmNiLSetJtTpSxUIgNRyLrirxNTdXPnhK1FBvYCGoPaodm0L8yvdex7kB1lZ_CObFPnGHolsCIS4OK9oMNNW5Zrfk0Wpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"از او بگو به دنیا.. از او که قصه ای داشت
او جشنِ زندگی بود.. سروی که قد برافراشت
از اُجرتِ گلوله .. از شر که می‌هراسد
از مادری که او را از خال می‌شناسد
از او بگو به دنیا.. ای شاهدِ غروبان!
این رقصِ بی‌سران است، این داغِ پایکوبان..
یاد آر اگر رگت را با مرگ می‌خراشی
تو بازمانده‌ای تا او را گواه باشی!
دیدی که بر مزارش، رقصِ پدر کدام است؟
این هلهله عزا نیست.. آئینِ انتقام است
از او بگو به دنیا.. از نغمه‌ای که سر داد
از او که نیمه جان بود در کیسه‌های اجساد…
از او بگو به دنیاااا"
monaborzouei
Lyrics: Mona Borzouei
Music & Arrangement: Reza Sadeghi
Producer & Concept: Sia Davarnia
Executive Producers: Mahshid Hamedi Boromand & Farshid Rafe Rafahi
Director: Carlito Brigante
Video Producer & Director of Photography: Avid Eghbali
Ebihamedi
📱
youtube
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8mpJklpicZLWLjXf8LaRfHIRwno-MZk72PxrpRrjXmhiJZW9DVPI2enRuGQy9NR8cYwcvuvM72wZBVJWTCNbkBRDkSTHiOudH-VixFdSyQ9Hu3tUxYBtqBBn2n_7430wqfd2M-tV76z0WGgROiAEjkT5FTzHyEWvVVcHHFCOu_9WN6GO7mA--xKJMWYh8RmfYtvd3fVxLJ4eI9rbCIJ8ETa2h6a18CMAxb9kUs53OD_lymTRh_pnDTidf0dqUb0vtVVQjD6S8yR7eZm5Tpg5BhqLgConZVgUUL6P8jF9yi4XVrL_4mql5bwusM7MzmiVc52tBsfTouN2540tvlqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز یکشنبه پنجم مهر ماه و یک روز پس از آنکه اعلام کرد پیشنهاد ایران برای پایان دادن به جنگ را رد کرده است، در گفتگویی تلفنی با آکسیوس گفت انتظار دارد مذاکره‌کنندگان آمریکایی این هفته مذاکرات بیشتری با ایران داشته باشند.
ترامپ گفت: «انتظار دارم این هفته مذاکرات بیشتری با ایران داشته باشیم. آنها می‌خواهند به توافق برسند، اما این توافقی نیست که من بخواهم به آن برسم. این همان چیزی است که شاید یک سال پیش با آن موافقت می‌کردیم. آنها بیش از حد روی مواضع خود پافشاری کردند.»
به گزارش آکسیوس دو منبع منطقه‌ای نیز اظهارات ترامپ درباره برگزاری مذاکرات بیشتر در این هفته را تایید کردند و گفتند انتظار دارند دور دیگری از گفتگوهای غیرمستقیم میان آمریکا و ایران از روز دوشنبه برگزار شود.
با این حال، آکسیوس گزارش داد مشخص نیست اختلافات میان دو طرف بر سر مسائل اصلی قابل حل باشد. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار تعهد ایران به امتیازهایی در پرونده هسته‌ای است.
@
VahidOOnLine
پیش‌‌تر:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه پنجم مهر در حاشیه حضو در مسابقات گلف جام رؤسای جمهوری در شیکاگو، از رکوردشکنی انتقال نفت از تنگه هرمز خبر داد و تاکید کرد به محض «تسلیم ایران» و پایان جنگ، قیمت نفت به‌شدت کاهش خواهد یافت.
ترامپ با اعلام آنکه شنبه شب «مقدار بی‌سابقه‌ای» نفت از تنگه هرمز منتقل شده، افزود این میزان حتی از مقدار نفت منتقل‌شده پیش از آغاز جنگ نیز بیشتر بوده است. او همچنین گفت قیمت نفت اکنون از دوران دولت جو بایدن پایین‌تر است.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pstHFO0-dts0AWtLLzxyENizgY2_t3BT9pL94tQi-32ToEiNYb8DdGdiDXGeohdOo0RBH1e1A6PUu_xMpjgN8C1TOwkWpqKh5NJN8k7rwQh2VHnmLKHGFUdM0e6xHM65fHHp9Ol1W4gRYT5ur2FFTQndQst093YU-aj04OEUz3g2AL7YGt4LnzMxTBiWIalelDAbfNkDO3fAYOM0EC-Gz0hu8Ydgp4D6D8fhECZAhlu8UhpaN9hyLGerTBBH7aGOshgGB_WGJ_0uQoAUapdIqjwWoJurOxFbNPHytJ1KkIEcM-sEwYCsQBBp3p9YnHDMekzDutx2ln2C9MCIwlIofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iw0AggihPAiKgo0HqCzrIZ11e1AJf7qHrCpHKiFA4cOZbYze2RckcZePInRMbr5kAZQR1l-QAFC4bgsxedorDEcllSVIXH8tm8RcTSGoASbZkoMHGGCJtJpjGbmNLRlgWtaCXMSxloDXRslrvWRiUJL3n1_hrewvUJclR0mhNj2Gpo0Q2aiSZIS-Scrw34ZibP7ThHbUHrGBPEbB-T9g11XPoz4GlgLx1xpgK7kwUC7cjfDd38L5vliJdYWBN9fqyeZR7vQ1_6SoA4EhrtWvMnBR_ypluW-QsocSj9m03_aeeBnnMTAM4A9CJLp2A_c9HDGI7UEw0KG7q8un2Fki4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، می‌گوید با وجود اعلام علنی دونالد ترامپ درباره رد پیشنهاد هفت‌روزه تهران، هنوز پاسخ رسمی واشنگتن از طریق میانجی‌ها به جمهوری اسلامی منتقل نشده است.
او با اشاره به اظهارات متفاوت دونالد ترامپ در روزهای گذشته افزود: «متاسفانه از رییس‌جمهوری آمریکا حرف‌های ضدونقیض زیاد شنیده می‌شود.» عراقچی گفت تهران منتظر خواهد ماند تا واسطه‌ها «نظر قطعی» واشنگتن را اعلام کنند و سپس درباره گام‌های بعدی تصمیم خواهد گرفت.
@
VahidHeadline
عراقچی روز یکشنبه ۵مهر ۱۴۰۵، در گفت‌وگو با برنامه «میت دِ پرس» شبکه ان‌بی‌سی نیوز، در پاسخ به گزارشی درباره احتمال ازسرگیری حملات آمریکا پس از انتخابات میان‌دوره‌ای این کشور گفت: «ما کاملا برای ازسرگیری جنگ آماده‌ایم. در برابر هرگونه تجاوز جدید ایستادگی می‌کنیم، حتی اگر به جنگ آخرالزمانی منجر شود.»
او در عین حال افزود: «هم‌زمان آماده دیپلماسی هستیم. انتخاب با رییس‌جمهور ترامپ است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=ZTmhaMgV7AWgxkzILMbeZImqU38sTaUKdEo_LLKGS4Y55ckNM2HC76OOwvDyHevUTz0yBIylVfpmlkzHOo-1Bc1Iiiy-_aoMZWZ9bvW0IA_rLXaqf0Uchb4WgmLOwHkgcRZmwiIWIhjRiOwk4N_QRPijbCLM-anuy-5K_p4oEp4aKovRe4MCrBdS07FJSAA_fJt0Ng2czd9vJcusNoOP1Ft1-24V35ZrqKupFSd1-vtEsU8RvafFsof9j58g3237GJR9NJzeDJcNK5a2nUatrPVZHRo1iCFwSB6cY7oQpWqkSiAKjYlDTo7l2X2MiYoGhktS6un9310ISVmtyGtuZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=ZTmhaMgV7AWgxkzILMbeZImqU38sTaUKdEo_LLKGS4Y55ckNM2HC76OOwvDyHevUTz0yBIylVfpmlkzHOo-1Bc1Iiiy-_aoMZWZ9bvW0IA_rLXaqf0Uchb4WgmLOwHkgcRZmwiIWIhjRiOwk4N_QRPijbCLM-anuy-5K_p4oEp4aKovRe4MCrBdS07FJSAA_fJt0Ng2czd9vJcusNoOP1Ft1-24V35ZrqKupFSd1-vtEsU8RvafFsof9j58g3237GJR9NJzeDJcNK5a2nUatrPVZHRo1iCFwSB6cY7oQpWqkSiAKjYlDTo7l2X2MiYoGhktS6un9310ISVmtyGtuZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: دومین زیردریایی بدون‌سرنشین آمریکا را در تنگه هرمز به غنیمت گرفتیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی روز یکشنبه پنجم مهرماه با انتشار بیانیه‌ای مدعی شد که یک زیردریایی هدایت‌پذیر از راه دور بدون‌سرنشین (زهپاد) آمریکایی را در تنگه هرمز شناسایی و به غنیمت گرفته است.
در بیانیه سپاه آمده است که نیروهای نیروی دریایی این نهاد در یک «اقدام هماهنگ و پیچیده» و با استفاده از اشراف اطلاعاتی و جنگ الکترونیک، این وسیله زیرسطحی را که  «برای جاسوسی در تنگه هرمز» فعالیت می‌کرد، به دام انداخته‌اند.
سپاه این زیردریایی را REMUS 600 معرفی کرده و گفته است که آن را به غنیمت گرفته و اکنون در اختیار متخصصان نیروی دریایی سپاه قرار دارد تا اطلاعات آن بازیابی و بررسی شود.
رسانه‌های وابسته به جمهوری اسلامی نیز هم‌زمان ویدیویی از این وسیله زیرسطحی منتشر کرده‌اند و آن را به‌عنوان «دومین» زهپاد یا زیردریایی بدون‌سرنشین آمریکایی که در جریان درگیری‌های اخیر در تنگه هرمز به دست ایران افتاده است، معرفی کرده‌اند.
براساس گزارش رسانه‌های دولتی ایران، این زیردریایی یک وسیله نقلیه زیرسطحی خودران (UUV/AUV) است و برخلاف یک زیردریایی سرنشین‌دار، خدمه‌ای داخل آن حضور ندارند.
این خانواده از سامانه‌ها برای ماموریت‌هایی از جمله شناسایی و مقابله با مین‌های دریایی، نقشه‌برداری از بستر دریا، شناسایی و پایش زیرسطحی و جمع‌آوری اطلاعات دریایی استفاده می‌شود.
ادعای امروز سپاه در حالی مطرح می‌شود که پیش از این، در ۱۷ شهریورماه نیروی دریایی سپاه از توقیف یک وسیله زیرسطحی آمریکایی دیگر در نزدیکی ورودی تنگه هرمز خبر داده بود.
سنتکام در آن زمان اعلام کرد که آن زیردریایی به‌دلیل نقص فنی متوقف شده و «حاوی اطلاعات حساسی» نبوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LeUUVCJhYh3sHC9Crlup_6Md5YhB_hYdnH4X4toL_GHaRLWVkPId8OR5j1rXbFwzoAPtKt9Vxf7d50l1gaIHckt8yDkTHG9QCK0VKlOirwcqP1AJOI61byhJgaAqXYDI2niOR2MyNvuN77CL0-LtC5-ZogAZxESHYmyRzZ-E7RX-LUcOgDqiD4JjwtwuoDt02K9iIIptzWvNRB1Yyh7H8MgKV367IJGTJg0Epd3lp_JqCTOzDMg9kCbuxTzsEalarz1UJZb_bmbRrYnOVtRZtlFrOEew9-EJQs9SqDJtesQoU4rovv5oPwYBikVxTLzNUPZ54qFzaZpDAZ_NjNn5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ipn-BydvORSxeET4vAuR-NsIWJWp_lfoLZePoSPR1MdlQ_TVfgSSf-WInBAX4iGVmxjVjgT2NKkIVgjJOBvFyi5gPUkcCRgPvAgdltM2rdeXVBUeLFutOfeg0IWUUG95OjhD3tpfKnS3goQmnMz7m0K1JWOalksiG3e82KPQIQRRFgS32xtJUC1eLJii7LoaLYhJTlHcLF3KWiaI2SM9PvBKCH9qUDtOtfzAGqseRoBoWRrQUBJ6uZ7B8rVv411oJQMy-pzpKxUOraCpdnrwIGOeIdMyiZbdbyIMnvdkGFw0Xxw5_6XIawxNsxhPkXxdIPA4578opDBbc_rWLrNIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d5P_y16KS3Nl4NnJOv7CfGyFaG2NgKIkIX9BPwV51xMN_v1S6kdGA4g7LSJT7bnbmzaAqFlpceu0owvVZNtnIx1aUh0jbKoejSrq2TvbfwgZpPkpIRDin_a3EvDKhGuD_gMT01yEui0ed-ju5nIbyGxda_LG3gLpBsHdHqRalQrL-ciNH_e5WPeUY-RjYsP5N6DYseIxxyMS7rpCkj8RlmwTi11DCATZh7MDQOGueh7RdMCuth7AR2gclycOKdh3ZgKNZHk4COzI0TzxyMqINnBgRNVOsZZWxvZ0WpwIg_olG50NsZTdh0PABndim3XKly7iq5RRvhYcDzfOk3OAHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمید رسایی در پرونده شکایت محمدباقر قالیباف به ۱۰ ماه حبس محکوم شد.
این نماینده مجلس شورای اسلامی گفته است که برای اجرای حکم خود را معرفی می‌کند.
دادگاه به استناد ماده ۶۹۸ قانون مجازات اسلامی، حمید رسایی را به «اعاده حیثیت و رفع اثر از ادعای نادرست از طریق انتشار تکذیبیه در صفحه اول نشریه ۹ دی» و ۱۰ ماه حبس تعزیری محکوم کرده است.
گفته شده است با توجه به اینکه این جرم قبل از دوره نمایندگی رخ داده، حمید رسایی مشمول مصونیت پارلمانی نیست و دادگاه او را برای اجرای احکام احضار کرده است.
@
VahidHeadline
عباس عبدی، روزنامه نگار و فعال سیاسی، به دلیل انتشار یادداشتی در روزنامه اعتماد به یک سال حبس تعزیری محکوم شد.
روزنامه اعتماد هم در این پرونده به دو ماه توقف فعالیت و انتشار محکوم شده است.
آقای عبدی در بخشی از این یادداشت که ۱۶ اردیبهشت ماه در روزنامه اعتماد چاپ شده بود نسبت به انتشار «اخبار جعلی» از سوی برخی از نمایندگان تندرو هشدار داده و گفته بود: «این افراد تحت نام نمایندگی هر چه بخواهند می‌گویند و کسی هم در مقام اصلاح آن‌ها برنمی‌آید.»
در پی انتشار این یادداشت، دادستانی تهران او و روزنامه اعتماد را به چند اتهام‌، از جمله «ایجاد دوقطبی کاذب و اختلاف میان اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» تحت پیگرد قرار داد.
@
VahidHeadline
صادق زیباکلام نیز در پی مصاحبه‌ای با خبرگزاری آنا به یک سال حبس تعزیری و از باب مجازات تکمیلی به منع هرگونه فعالیت رسانه‌ای، مصاحبه، یادداشت‌نویسی و انجام مصاحبه به مدت دو سال محکوم شده است.
@
VahidHeadline
حکم یک سال حبس در پرونده حشمت‌الله فلاحت‌پیشه نیز در دادگاه تجدیدنظر تأیید شده،‌ اما به مدت پنج سال به حال تعلیق درآمده است.
سیامک رحمانی، روزنامه‌نگار، نیز پس از تفهیم اتهام و صدور کیفرخواست با اتهام «فعالیت تبلیغی علیه نظام» به پرداخت جزای نقدی درجه شش به میزان ۸۰ میلیون تومان محکوم شده که این رأی قابل تجدیدنظر خواهی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky5do7uQUZQKe99G7KtE7ST_-G_-M0Nw5G9fg-pQML5WHFp40H0dp35DdlBo4FVz8PJAsPU5HDUFtfB0qzW7GjFqYexzMG72WvNP7bw5TWESm273tfqDQq74HzWhy9puUdPJEYonxIcRjMamrig3kcs6r_gpFTJrk4scrKdRcvC-suwR3oZFR2uoenku29gNGHbvuf4jMZy7llUreHwdjhopJ9wugJjoX6j-LBCD0ejC6xetCutpXZhut7EKSAAQ6TL1zDf5OZdLeqVR0u2qT_O-hr8pvRmm-EM9wad9MJd3zSTLG0M3nu1qH1aSobj6TWCclcW099wpeDc7NEneGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRbLk5azPKHyvNqymUYMqEodlnGtS7dK5i24ImbqQD0Vaz39-a6WYbbmmeah_IAuyuwTAlgTDU8dsx9arzmx11EdmoVgbFl7UYQZSUWw5YAYawk86cztwAAlG6fL0Aqd_h5gHHr-qaRcrxsY56ekiMxuAPUW6hH6vh8rQqHMnE4VqqLEyFVGtoRNgqkxf6lePVVk4Q5RdDQ0ngFoyFsz8FM4iv1hpKFgkkXMwW4bvKp8iOV-TlSwWcaYUTqsB61D6wg-jZ41Orotfu1vLHq9KWYC9Ej2_sFGFm6CB4LtVX5jX5qpw9eoMT2xvEDSPoqXhDmpZMcDU6wy1bArLlGMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت آکسیوس، روز ۴ مهر ۱۴۰۵، به نقل از یک منبع آگاه گزارش داد مذاکره‌کنندگان آمریکایی در جریان مذاکرات غیرمستقیم با عباس عراقچی، وزیر خارجه جمهوری اسلامی، به او اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند برای بازگشایی این آبراه شرط تعیین کند.
عراقچی در این مذاکرات شروط تهران برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای را به طرف آمریکایی ارایه کرده بود.
بر اساس پیشنهاد جمهوری اسلامی، تهران حاضر بود تنگه هرمز را بازگشایی و مذاکرات هسته‌ای را ظرف یک هفته از سر بگیرد، به شرط آنکه آمریکا محاصره دریایی بنادر ایران را لغو، تحریم‌های فروش نفت را رفع و آتش‌بس در سراسر منطقه را دوباره برقرار کند.
بر اساس گزارش آکسیوس، مذاکره‌کنندگان آمریکایی روز سه‌شنبه در جریان این گفت‌وگوها به طرف ایرانی اعلام کردند که جمهوری اسلامی کنترل تنگه هرمز را در اختیار ندارد و در نتیجه نمی‌تواند درباره بازگشایی آن شرط تعیین کند.
در حال حاضر ده‌ها نفتکش روزانه تحت حفاظت آمریکا از تنگه هرمز عبور می‌کنند و میلیون‌ها بشکه نفت را به بازارهای جهانی منتقل می‌کنند. با این حال، حجم انتقال نفت همچنان به‌مراتب کمتر از سطح پیش از جنگ است.
مسوولان آمریکایی می‌گویند طی ۷۲ ساعت گذشته حدود ۶۰ میلیون بشکه نفت از طریق تنگه هرمز منتقل شده است.
در همین حال، قطر و دیگر میانجی‌های منطقه‌ای برای ازسرگیری مذاکرات میان تهران و واشینگتن تلاش می‌کنند، اما اختلاف دو طرف بر سر موضوعات اصلی همچنان گسترده است.
جمهوری اسلامی خواهان تمرکز مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا است، در حالی که دولت ترامپ بر دریافت امتیازهای هسته‌ای از تهران تاکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=DDyLhNT26ri-GVmG52Td5ioNY5ojtatP5vGvA27e1YQHHgn3i4pm08IQ1wIKAl7J6IejrqKEQojUBKmbCoQgBfbXVbk06yS_fwcV92BliiNecxfLQqUCm4Ok9fWWfODQGErsQ8UBqpS-Pf2qwItCGS4QaWDazji0R3rGTbvdGiwStRZ5cngeZjGDFzbR8f28JkLMsO8pyw7bctGUJbUAPC_BaVIxKTjEDBYFnDpA1DAgjM5wjysRBkhM1H4XK7GqRE4DzkSphDZmDAMnnTEZXiWNy3rRhW02LPNzs3NS_uL5dyVzej3BjoTRqOZHKJRBjlNER8U_ABINZRXHk_cyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=DDyLhNT26ri-GVmG52Td5ioNY5ojtatP5vGvA27e1YQHHgn3i4pm08IQ1wIKAl7J6IejrqKEQojUBKmbCoQgBfbXVbk06yS_fwcV92BliiNecxfLQqUCm4Ok9fWWfODQGErsQ8UBqpS-Pf2qwItCGS4QaWDazji0R3rGTbvdGiwStRZ5cngeZjGDFzbR8f28JkLMsO8pyw7bctGUJbUAPC_BaVIxKTjEDBYFnDpA1DAgjM5wjysRBkhM1H4XK7GqRE4DzkSphDZmDAMnnTEZXiWNy3rRhW02LPNzs3NS_uL5dyVzej3BjoTRqOZHKJRBjlNER8U_ABINZRXHk_cyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه چهارم مهر تأیید کرد که پیشنهاد جمهوری اسلامی ایران برای بازگشایی فوری تنگه هرمز را رد کرده است.
ترامپ پیش از ترک کاخ سفید در گفت‌وگو با خبرنگاران گفت: «من پیشنهاد آنها را رد کرده‌ام. آنها می‌خواهند توافقی انجام دهند که بر اساس آن تنگه را فوراً باز کنند، چون به‌شدت در حال شکست خوردن هستند.»
او افزود: «ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم و مقادیر عظیمی نفت از تنگه هرمز خارج می‌شود. دیشب ۲۹ کشتی از تنگه عبور کردند. آنها می‌خواهند توافق کنند و من هم با توافق مشکلی ندارم، اما آن توافق قابل قبول نخواهد بود.»
@
VahidHeadline
او بار دیگر گفت جمهوری اسلامی خواستار بازگشایی فوری تنگه هرمز است و افزود: «آنها هیچ پولی به دستشان نمی‌رسد، چون پولشان را از تنگه هرمز به دست می‌آورند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ywk8_Sy5F6VBFecRe2qhgR6DtFMXRAkj6auYN0NMyH27pWQcq5wmVtIspEWpgwa5atVzxh3jNxaWUe1XRKr1CTd8XP_7g38ilrSUaeWnmDDi3RT37DeGhZslNRFl8hfcPtyPsXzMgmzv4LdoXaXaM845hwgAtP7UEMdtLFGUhsSBEHLNKWd02RcBNrDGTp-PdvKJ8yZ3EkuZtlOlMQjDv9h5OCBnstQwsJxzPeYk81QX7Pusy6RK7f3NssiNF8-Rzj1Vzu_5ij9xLFsb2nVruChnein9t6re6u-vBbgDFkmUI5ZNjkon7U0O5QIxly-Vt4XJ9H5M1IJewPwLAMGhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=NdTcPxVTpuLRXb-No1iStzn26IjBh9AEHsv0J0_h5Ti8s7JAs_8IPzrFLVuTlSf29H3y1IG0zftx5iQyaJByiaJdY5YCJmO--NG8EOofFAJ44CfNxAzoaq1728w8CxDBi011IVBxcCgjGOc0nmU8dZsBC8SolkX_qzZxbaiIruo0V4V8tIF6G516WmatW0GKbz1UViAUtx2nGu2jmrrxzlmtOqF0RE04aF9NT7IDth0_aSofdl_YTi-iwWo67MnL46YIebHWh10sfODjsWaXDjRWPF88PAvqmL53KCfdL5d2Fjbn9gpxPQf8hffS9pJmXdwJXtNPV2C5WNP4zyfidQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=NdTcPxVTpuLRXb-No1iStzn26IjBh9AEHsv0J0_h5Ti8s7JAs_8IPzrFLVuTlSf29H3y1IG0zftx5iQyaJByiaJdY5YCJmO--NG8EOofFAJ44CfNxAzoaq1728w8CxDBi011IVBxcCgjGOc0nmU8dZsBC8SolkX_qzZxbaiIruo0V4V8tIF6G516WmatW0GKbz1UViAUtx2nGu2jmrrxzlmtOqF0RE04aF9NT7IDth0_aSofdl_YTi-iwWo67MnL46YIebHWh10sfODjsWaXDjRWPF88PAvqmL53KCfdL5d2Fjbn9gpxPQf8hffS9pJmXdwJXtNPV2C5WNP4zyfidQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayzd10KPHyRJ_mN8P9EVbjyI4nha7tyBiTCYMBjXvS2VZqvGM1Sq9ydhJwd1cionIPGWN2zgst0DACI1oqGtDaM4rDKQE9whos7bhjIzmqZyRQtb42KXG3ND6frErON4VHRY7qOBIMMTFIzHaSLmEh4gHERvUuVNY7J0qJt3rfX5kTCpqyISBL2QYCCZMzWb4NYl3-78ILK4T-YWEcG0udf0vUhQGiU3ivxcsdq3YROkxs0JYobHBjI_L5trziJLtGNLIEF4FCcdLW5cR587XXJvE4lQ9wLibzG38O9e6t79sRolGIFimV9pr0nZRzX8SzlFP5BdkEyak-xtSStrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLpXgu3MiqBNb_bMhKQiGOn1F2FPJ7m2tjSatfp_j3DLp8ApDyb_G3RbRgMIOgGxkVtk1Us65oIeCPXn-JQLbrDVOmJDGp71Dv3P2yTYP3nrelLXGpZ-q988P0F5PSstzfl9rdzGNgvC1aGKMwYs-ujSZgMo4SvblJh0hyMw-7igFnQsO-QGmpOLnh4hdHXyh9uF3ibRi1icxT_CB9WZroDjyA9McBSlNVFWJ7GQhVpBG6FOy0wEHS1qIgJHjT-yeor_kmSt6Va0edDDSSURG9MnF0ZdqpjicSP32DI97N1HtfLiDW6k8rYac_yk4OLeALCLug69ZQOoiw1hkzuC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ubc0VfJp58Fc9fRofqB_QgnzT4TXNaqrk8hS--DxWxz8BQ5TALcz6FQthtwdDXtjnEp_zFjPowP825Z23egypHQwv3bPMQS2f5_DYOQ-KRndf02UpIRAMkSe4KzjDIR-L6Ww1MUe_VPpY4ICtNXGMP8VP1dxOoOgmhaBsG0pFxZ8USoC3o4LS-FdSI88QMaUuwyOPJqjHv7ru4IgaG4TvttNCVrGvaK9ru3v-63VvxTgXIKNPR7hQdwRqnOfMiKnhEHiaB_Qme_i2KhtC6CGnzJYWsdlflkbHq-tS2nD9v3905K9HcQijvjJY8KRUw8HrVw1gF0wDBG5bi8c6eJtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=k_J8St3na47jnvCTkwmZGeu0xwQTWNKtQ_CIP8_31bs5hfUBWWCgcs9XKuqoHzhPL3yXV3JFLxapTjEQ7oo_mQMEx0IgPz6EBZa3LevSq5MAN31i3galHAb-v6kOqAgKkGkF3L_m43CDIgtUPTvPGu8O4XzX5ckEoYsyF03SBgBLWSQEeUmlsG2_Z0c7c8CQjkByo09WEY-DL3RzkGNkKuuLDgMM7QhL5onjUjzXwa_DHS7cpEXEGsoJfNHtOdT4e0U3gIWTnyBPmzFJfAo_uCkjRLT1ZS1vkzgUyzcBQvt8TEA5e5JtL1-DJRnUjEb4ibrFXgPu6n7rmcUESkTgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=k_J8St3na47jnvCTkwmZGeu0xwQTWNKtQ_CIP8_31bs5hfUBWWCgcs9XKuqoHzhPL3yXV3JFLxapTjEQ7oo_mQMEx0IgPz6EBZa3LevSq5MAN31i3galHAb-v6kOqAgKkGkF3L_m43CDIgtUPTvPGu8O4XzX5ckEoYsyF03SBgBLWSQEeUmlsG2_Z0c7c8CQjkByo09WEY-DL3RzkGNkKuuLDgMM7QhL5onjUjzXwa_DHS7cpEXEGsoJfNHtOdT4e0U3gIWTnyBPmzFJfAo_uCkjRLT1ZS1vkzgUyzcBQvt8TEA5e5JtL1-DJRnUjEb4ibrFXgPu6n7rmcUESkTgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در  دو واقعه جداگانه دست‌کم ۲۰ نفر کشته شدند:
یک دستگاه اتوبوس مسافربری بامداد شنبه ۴ مهرماه در آزادراه همدان ـ ساوه واژگون شد و بر اساس گزارش مقام‌های امدادی، ۱۱ نفر از سرنشینان جان باختند و ۲۴ نفر دیگر مصدوم شدند.
@
VahidOOnLine
برخورد یک اتوبوس مسافربری با تریلی حامل میلگرد در محور بیرجند ـ قاین در استان خراسان جنوبی ۹ کشته و پنج مصدوم بر جا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAGN-UPaj0ge5JMU7TphFWTRnndTIRsYSa7pLJswSsXS9O2sCnS-17Um7k2qXqzG3q5Uoat2s2QGUKZ703F1i4sEST96FDDLz9UTrPHVR056qGJLeu8buBNDEuXQXGLanz8YvgS8KLVg3JqjcvBta_-Fumqi6sYucTnCumqr2sQ_PqNcA_9qnOvbVX4ZELJnGTvC2uf0M1BWiger1F7Rc5uqbV_cgFIIwxn4M0koYenVMk3Hlu7yeJb8q5GmnbshUZsQ7rmSBER_aHnoCZECYvXe4sl4LZgSwQtQpp5a8fFTYvhlvXZLKW4XfFjmrcPdOlMpp3HnLMmIyEeaXgucMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه تجدیدنظر استان قم حکم ۷۴ ضربه شلاق پرستو احمدی و هشت نفر دیگر از نوازندگان و عوامل «کنسرت کاروانسرا» را بدون تغییر تأیید کرد.
ابوذر زمان، وکیل دادگستری، روز جمعه در شبکه اجتماعی ایکس نوشت بر اساس رأی شعبه ۱۶ دادگاه تجدیدنظر قم، پرستو احمدی، چهار نوازنده و چهار نفر دیگر علاوه بر ۷۴ ضربه شلاق به دو سال ممنوعیت از فعالیت در امور سمعی و بصری و ممنوعیت از خروج از کشور محکوم شده‌اند.
دادگاه کیفری استان قم پیشتر این ۹ نفر را به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» محکوم کرده بود.
پرستو احمدی در آذر ۱۴۰۳ ویدیوی «کنسرت کاروانسرا» را که بدون حجاب اجباری و با همراهی احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا اجرا شده بود، در یوتیوب منتشر کرد.
قوه قضائیه پس از انتشار این اجرا علیه عوامل آن اعلام جرم کرد و احمدی و دو نوازنده همراه او نیز برای مدتی بازداشت شدند.
در رأی بدوی، دادگاه پوشش پرستو احمدی و همچنین تولید، تصویربرداری و انتشار عمومی این اجرا در فضای مجازی را از مبانی صدور حکم عنوان کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A93EAKwRiBZ1KdOQFAJMGrfmsxFcmzFXA50kwtCkYGkIAkS1zMOSJ5F-uLXzoepAGk_V4XkNU0NR2OxRv6JeXWqgZqjWhP8zZLUomou-Hd_3SqvGi4OA5n_-So7mV5IGjjOw9m9O4Wfqj3ecTLSjAxrsLFeOs743Nob3hPGfJBLsZSamuTlLLhg_NmqJjyWWKmMqde2reXtMIAwZN5l46hkR8uQCk4oNIUUZhQYT7TbWwTJHRzcDgxKwjlwF3DE4VieYkz7d4VwXnunj4J0TxYspTNhMrpH6K4nD-R86PFSMPc4ZjYdjvNLt2rtjM2pjOW9myzcFh6B8hTDb7F3zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7no9r1MlrOJbRFUdD1oF11kgC78QFiTssq3fsDMCjIlYAjPUukDpk0TEqBrzJpORxaqColC1OfyPTCTxVbyrmKPw42nNVsZ2rhcDbVk-x-Y3t9dHAABB8BhIvzzScQONIMki3zjHROd9JA9Dycni3Yj5OP9hSvkMUz6AW9-jfpso2JqgKrnkRNUhgYbRsBArXGrpPFiQT042fCYBhEmcjAyLihDlWnHeLJJzNaJmuRFxzgXnCW8Dx9-vkKuQz96J3lM8Qh1vSLN2Behs37OL04fF8nAFhYRE-Z5SW1kWxqGTR70lMt5WRmymPPeK1hqj5iJS-b5IjOUDWOcxYkpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW3PRLxK8OfeS5qBQuzSblH4avQoWYMV4iEQF2R7zxM47cxX-gdqKOQPwv5_-zO2_6ONq8LPScjz1-R3K89S469QGP-HLOF9inbeDYlKcK9i0vXU-zqyVDCebpvEOd5i0ubdt3UoLbSgH1kwWlt9rhlC1SwfzuqjYtZjA3UPWZHHd1FZseGY6joIApSKRW70uQCVb2h_dJsImEClQCigx-zQO8teNg1SdRtgN4hiNPm6C-ZGePLjC_hjApJRRCSJFAgbN7ncobdvl6rRhzgAk6qwrDO7Uj1XgMEw78P7FNUVgm8-rcS1OeAHqnk2DQeKa48FNM2Fdk9Y3COJGnIl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgd_fH_NGt8VBh3TlyjBEq8OURZ5rduohOlwP77sPrfAslIwdbj9AOUXqdmD8Cwh15MvoDH3n5WPAARNAnUO5yK5FgJG9MW4j030y6qwl3-5Dtu8VXXgeEu3Db9ymnbaoQRckw7QRj3E30NK4KSG92ExteBSGO41N1hrNoTahrwiQoa2A7J92idP-05UuICLYgncWRxqHaK_EHYJknKoqkOgwfXAfegmKtdytWB6ZzdPYOjEP9bFXAhtn55J2527H9j9QWlNuIVa06KRCbJbHhKmp-lZcSGmCHTmYqc7XB0rYLevFmfi-JbGKhYYVpXcpCr3lK_hkcyawpSeIbgB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itYpz1_tz29yWobCirTXBnf_8UvVAPYQtDhorocrAokxL_5AH9KzhbRDJxrUW4ns-xu5eD5X2KjKAq-5gF0KGSSk68PUuTt4SezcwcSMwcuWkw6GEdrAVQzCPK_xOaEP5-E3EqeTOeXzvZtV2JE0Oc-piVzPJDjL2u0rtfEf0auFkh2--Rb0lRo5688SHrCyNOuWXeoHImFR5fzmvJOu9D1K1Yxby--un_Okd5D-WBIFiEEKHqq7KQRoKxL9MIeSPfUlYp3S-Xo3mMIUNg9HgFLnMbGxIDtDZueXlADXSGxh_kDPVsNFfnG-PMuDKl48Ip9Pg_7g3HcEZjX9AGwaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0q7xAuA2niJdFhFKdRBHDnFavDXKX5zP39vH5iviFmBnq0FJZ3bsbb7sz2cP80D-ePsulObZtzxfJLld5U6gXVMt-J2O_Jmj2Uy16HM-Iw8ZRCwtFlhlSeVShqtKR5765Yz2p9vE3jVMLoJsFwlBboLvDmpmyDDFzhiBxiNa8JwHOPsoSTGrpETtTbGa7D8ciTwYufPiwIZ_oFvi3pMFb30kK7PTs6AZHGMh_bFqlJx-hZaCqddCXryVh-zOgc48AyTvwsMAjVE7K20SR8bi9cI0Hrx-1Yi9taYrfyy9jClbmyI8PAralr5-n99fXix_EXE5MMZaVtIlKBBDbAvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laFPuL9kozepkstd7yM-BG9RMS-BGnM0EqFJL3hNuWRFFwWWGb4ZwmHHkJP0-RijVJVX3hlnCdIGoC6cx-1ih6g-nfZtLeBzSTvDf_PU1WL2Gy8yn3n8BKwsZI6vRq1uJjbyAXWT158waeS97kx6HGdP-0zyyZ0BdyLM11C3CzCjTxZUm5nkrbvBw--pXhnPq6Dr1NrbbSxUMVDvZdSv0rViZQGvgFrUNXXCwnz9ApU7V_HnMwtcEML4pZnvbVITrPlko-7fvAiwSUpfnuFTo6uGsketisi1i0yLzmkYRXG3LLTmQZty8YTIGaJqCYq1aWCNeqIKaUKanQV3GLjRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bt33ZoZFomYd9UhVVBgwNCVmtZSNNICTDLX2OEEPCJmVDThZJ5WIteU3_pSVEX881MvSwHIyTFViyC23aP2fFXy9E7jaCyJBGnGto508O09NbG5emr4521c3ltMZUETmV5Ya3aauVIU9OLLJAWDg2d92QWu4lvErHMhGTf6ZifNRhWmhaV6y7ojWMVTu1eqjmpj42BaPkE111CyY_WCJ-imod7gE361DqUcCmwWOvuZ2HcMEzCkTKVANAUWN55qdc2_2j4qI24fzisquMLBpr9YKY50cx1HVGahRQGbDqzVPtS4MQET8sCOQnBj3rmuJ7qIDrM6-SWj5In70FJClcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQi_znShsRtkgXZ_AlXH6q3qZv7wqEBEpcBWbid3hq5K4sC-ZNDtNwdT3GnT1bwJwHGlfGNEkWh7fck2qwIBEWR3TboiPBzHSUGIR7J3aiWRNa5k5FvrHpS2bLxfREVt9Nlj0wjuWPN-m_1dOBlHlqbsSYV2sy-at3MgcON26oSK78N2AZDFdLr0xtd7erYDOUPY1H4lnV3wMwsbZJMrIHSPPNcpAbUcIxwFy49sbzM7n2WTSgxZZ8ruJTlbqGl3XFC4ZZnjzCJsWBFcxl91xwmrKWW1Q3nwKbdKu93jJUK_n4R1CmtJObFD2IgDbnBDWQfbVFgRSA6UJzN1Z8a8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=rlGGf1AthMoBKoMuGJIjyUaTwse-jqQWdg8OVlIVnh8EDUvM4AnCmAB5xoDTBGeet4cOvuz8eaHlVdZ_3Iw4rgM0f9Xi5jKASPhCqnYddRr3HFAVM8dLh8kGPd0wXaJkxBmCu-MsIJI5fxkMOCK9FiT_PjOBU7bY_F2A6PVzN0g5Erm72ZxHjqklnk14CxxT3AOUz7O2Vq6m8VZ3qqgfYe0S_Ygj2ONZCT4b0WwfGr0KTECYb9Fsko_JWpx-_G68Aj1iQe8GOJ1Q1QJewfZk4XaMtAZSDmiDUOl1rYRQslXtAMxBMVEkXnu_HFvV6Z7qNMHd1jgBWbc8Ck9_CYlUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=rlGGf1AthMoBKoMuGJIjyUaTwse-jqQWdg8OVlIVnh8EDUvM4AnCmAB5xoDTBGeet4cOvuz8eaHlVdZ_3Iw4rgM0f9Xi5jKASPhCqnYddRr3HFAVM8dLh8kGPd0wXaJkxBmCu-MsIJI5fxkMOCK9FiT_PjOBU7bY_F2A6PVzN0g5Erm72ZxHjqklnk14CxxT3AOUz7O2Vq6m8VZ3qqgfYe0S_Ygj2ONZCT4b0WwfGr0KTECYb9Fsko_JWpx-_G68Aj1iQe8GOJ1Q1QJewfZk4XaMtAZSDmiDUOl1rYRQslXtAMxBMVEkXnu_HFvV6Z7qNMHd1jgBWbc8Ck9_CYlUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfihZSwrpf-Li6Qo8WF-VksneOhgtKgDtTe0_a6GJxjEdBM6_cKwoxjgEUrEL29msaG53uRKHIrctkdONZk8JAfIKtVgOJLccSDiBdevlf_aBD5f4bCdZGBVgFkz28ZQDDOdjvBNQX8vTdy6Kc2kHRnmvmhsotfM17kewaP3L2XnvHlvJQg_2zKjICTpNW2-azrG2MGAZeiYoosgDKF8hoBM5Rr0qyrhDwoeAs0Z_4kFsN3o96TAJNKf1IZYAP4IwhO6Ld4BePu3wbwMT7_2AVlTejPwtCA1BtxTi7UxNDH8trUAclF2w8DO8-lrFav_OHJOJ8C4t73kamp-qaNzmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسعود پزشکیان در مصاحبه با فاکس‌نیوز، از آمادگی جمهوری اسلامی برای توافق و کاهش غلظت اورانیوم غنی‌شده خبر داد، اما درباره محل نگهداری ذخایر هسته‌ای و تضمین تبعیت سپاه از توافق، پاسخ روشنی نداد.
مجری این شبکه همچنین با اشاره به کشته‌شدن معترضان و حملات نظامی برخلاف وعده‌های رییس‌ دولت جمهوری اسلامی، پرسید: «چه کسی در ایران حکومت را در کنترل دارد؟»
پزشکیان در این گفت‌وگو تاکید کرد جمهوری اسلامی خواهان جنگ نیست و مدعی شد جنگ به ایران تحمیل شده است. او گفت تهران آماده دستیابی به توافقی در چارچوب حقوق بین‌الملل است، اما فشار برای وادار کردن جمهوری اسلامی به تسلیم را نخواهد پذیرفت.
او با اشاره به توافق و تفاهم‌نامه‌ای که به گفته‌اش پیش‌تر با طرف آمریکایی امضا شده بود، از تمایل به ادامه همان مسیر سخن گفت و آمریکا و اسرائیل را مسئول حملات و کشته‌شدن رهبر پیشین جمهوری اسلامی، فرماندهان، دانشمندان و مقام‌های دولتی دانست.
بخش مهمی از مصاحبه به میزان اختیار پزشکیان بر نیروهای نظامی اختصاص یافت. مجری با کنار هم گذاشتن وعده خودداری از اعمال زور علیه معترضان، عذرخواهی از کشورهای همسایه بابت حملات و اقدام فرماندهان علیه کشتی‌ها بدون اطلاع «رییس‌جمهوری»، پرسید چرا تعهدهای او چند بار نقض شده است.
پزشکیان ابتدا به آمار کشته‌شدگان اعتراضات پرداخت. هنگامی که مجری دوباره پرسید چه کسی تضمین می‌کند سپاه از توافقی که او امضا می‌کند پیروی کند، گفت قرار بوده گروه‌هایی برای هماهنگی، رفع سوءتفاهم و ایجاد کانال ارتباطی تشکیل شوند، اما فرصت راه‌اندازی آن‌ها فراهم نشده است. او همچنین نیروهای آمریکایی را به شلیک خودسرانه در منطقه متهم کرد.
مجری در ادامه پرسید: «چرا رییس‌جمهوری ترامپ باید با شما مذاکره کند و نه با فرمانده سپاه، ژنرال وحیدی؟» پزشکیان در پاسخ، از بی‌اعتمادی عمیق میان تهران و واشینگتن و خروج ترامپ از برجام سخن گفت، اما توضیح مشخصی درباره حدود اختیار خود در برابر فرمانده سپاه ارائه نکرد.
مجری با اشاره به آمار نهادهای حقوق بشری و گزارش مجله تایم، پزشکیان را به چالش کشید و پرسید: «شما جراح قلب هستید. چند نفر از ایرانیان در ایران توسط نیروهای امنیتی کشته شدند؟»
پزشکیان بار دیگر آمار رسمی منتشر شده توسط حکومت را تنها آمار واقعی اعلام کرد. او گزارش‌های خارج از کشور را مغایر اطلاعات حکومت دانست و خواستار ارائه مدارک هویتی قربانیان شد. در عین حال، از ضعف مدیریت رویدادها ابراز تاسف کرد و گفت استفاده از سلاح در تظاهرات خیابانی پذیرفتنی نیست.
ادامه گزارش :
pezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ویدیوی کامل با ترجمه ماشین
بخش‌هایی در خبرها:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «می‌خواهم با دقت به سخنانم گوش کنید. روزی، و شاید آن روز چندان دور نباشد، مردم ایران آزاد خواهند شد.»
او افزود: «حکومت آدم‌کش آنها به‌دلیل دروغ‌هایش، فسادش و بی‌رحمی‌اش سرنگون خواهد شد. این حکومت شرور سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو در بخش پایانی سخنرانی خود در مجمع عمومی سازمان ملل متحد، بار دیگر به خروج نمایندگان کشورها از سالن و حضور معترضان در مقابل ساختمان سازمان ملل واکنش نشان داد. او با یادآوری سرکوب اعتراضات در ایران، خطاب به این افراد گفت: «زمانی که رژیم ایران هزاران نفر از مردم خودش را کشت، شما کجا بودید؟ شما درباره مردم ایران هیچ چیزی نگفتید.»
نتانیاهو در ادامه تاکید کرد: «اما باوجود سکوت و ریاکاری شما، نیروی مردم ایران چیره خواهد شد. فقط مساله زمان است. یک روزی که شاید خیلی دیر نباشد، مردم ایران آزاد و پیروز خواهند شد و این رژیم پلید سرنگون خواهد شد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «مستبدان تهران؛ می‌دانید از چه چیزی بیشتر از همه می‌ترسند؟ از مردم خودشان؛ مردم شجاع ایران که برای مدتی طولانی، فداکاری‌های بسیاری کرده‌اند.»
نتانیاهو افزود: «از معترضان بیرون و نمایندگان ریاکاری که این سالن را ترک کردند می‌پرسم: کجا بودید وقتی مستبدان ایران ده‌ها هزار غیرنظامی بی‌سلاح ایرانی را کشتند و مجروح کردند؟ وقتی هزاران نفر از مردم خودشان را کشتند و مجروح کردند، کجا بودید؟
آیا تجمع‌های گسترده برگزار کردید؟ اعتصاب غذا کردید؟ آیا مقابل نمایندگی ایران در سازمان ملل اعتراض کردید؟ آیا در دفاع از مسیحیانی که در ایران و سراسر خاورمیانه تحت آزار قرار دارند، سخنی گفتید؟ نه. چنین کاری نکردید، زیرا شما معترضان قلابی حقوق بشر هستید.»
@
VahidOOnLine
ده‌ها نماینده حاضر در مجمع عمومی سازمان ملل متحد روز پنج‌شنبه ۲۴ سپتامبر، همزمان با آغاز سخنرانی بنیامین نتانیاهو، نخست‌وزیر اسرائیل، سالن را ترک کردند.
نتانیاهو در واکنش، نمایندگانی را که سالن را ترک کردند «بزدلان بی‌اخلاق» خواند و از دیگر افرادی که قصد خروج داشتند خواست پیش از آغاز سخنرانی او سالن را ترک کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «قطر میزبان عاملان کشتار هفتم اکتبر حماس است. اکنون تازه‌ترین کشوری که به عامل گسترش گسترده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است.»
او افزود: «اردوغان یک مستبد است. او نیز میزبان رهبران تروریستی حماس است. او هزاران غیرنظامی کرد را کشته، نسل‌کشی ارامنه را انکار می‌کند و روزنامه‌نگاران و رهبران مخالف را زندانی می‌کند. در واقع، فکر می‌کنم در این زمینه رکورددار جهان است و البته رقابت سختی هم وجود دارد. اما فکر می‌کنم او نفر اول است.»
نتانیاهو گفت: «او به‌طور غیرقانونی قبرس شمالی، بخشی از کشوری عضو اتحادیه اروپا، را اشغال کرده و به‌طور مرتب علیه یونان، عضو ناتو، دست به اقدام می‌زند. اکنون می‌خواهد سوریه را تصرف کند.»
او افزود: «البته این تعجب‌آور نیست، زیرا تقریبا هر روز خواستار نابودی اسرائیل می‌شود. او می‌گوید قرار است حاکم اورشلیم شود. نه آقا، نخواهید شد. این کشور ما، شهر ما و پایتخت ابدی ما است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=pFFTWx8tBigeXpiqmYmw_XbUGMkCv3cgAU1dD2DOmBWgLGFk6DIv9twDhbo6gb-N5Vur-iqBD8Tp1USAGvZRLy5t-10h04qk4L63X6-MBlgjSdUuq51w6juTIfHQO8tULLAIgwSHivSGPDWgvOuSl0tNyEawxmYUsFs9rjRQHxxzDzx-BClZayK8T7kfv2GT39vBxMkJbwoU2ANvX_d8rDNZezEixY2ixJrmblPD7YDc6eXN3gTQwd0_xPyOCSCxiK10nyrC9kB_vwVOlBeHqi1E3NEyLrweuUiPqS5LbRfqwaJryn2im47gNvnvKtUx_p8euuYkOAjO_09k_PVI9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=pFFTWx8tBigeXpiqmYmw_XbUGMkCv3cgAU1dD2DOmBWgLGFk6DIv9twDhbo6gb-N5Vur-iqBD8Tp1USAGvZRLy5t-10h04qk4L63X6-MBlgjSdUuq51w6juTIfHQO8tULLAIgwSHivSGPDWgvOuSl0tNyEawxmYUsFs9rjRQHxxzDzx-BClZayK8T7kfv2GT39vBxMkJbwoU2ANvX_d8rDNZezEixY2ixJrmblPD7YDc6eXN3gTQwd0_xPyOCSCxiK10nyrC9kB_vwVOlBeHqi1E3NEyLrweuUiPqS5LbRfqwaJryn2im47gNvnvKtUx_p8euuYkOAjO_09k_PVI9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبران دو اقتصاد بزرگ جهان روز پنج‌شنبه، دوم مهر، در کاخ سفید دیدار و دربارهٔ موضوعاتی از تجارت و تعرفه‌ها گرفته تا تایوان، هوش مصنوعی و جنگ ایران گفت‌وگو کردند.
در این دیدار که در کاخ سفید برگزار شد، شی جین‌پینگ از ایران و آمریکا خواست که در اسرع وقت مشکلاتشان را با گفت‌وگو حل‌وفصل کنند. رئیس‌جمهور چین همزمان از میزبان آمریکایی‌اش خواست که به‌سرعت و از طریق مذاکره، جنگ با ایران را پایان دهد.
رویترز به‌نقل از منابع آگاه گزارش کرده بود که چین در گفت‌وگوهای پیش از سفر شی جین‌پینگ، در مقابل امتیاز احتمالی آمریکا در زمینهٔ فروش تسلیحات به تایوان، پیشنهاد همکاری در اعمال فشار بر ایران را مطرح کرده است. این پیشنهاد به‌طور رسمی از سوی پکن تأیید نشده است.
تایوان از دیگر موضوعات حساس دیدار روز پنج‌شنبه بود. چین این جزیرهٔ دارای حکومت دموکراتیک را بخشی از قلمرو خود می‌داند و بارها با فروش تسلیحات آمریکا به تایوان مخالفت کرده است.
به گزارش خبرگزاری رسمی چین، شین‌هوا، آقای شی در کاخ سفید از دونالد ترامپ خواست که در قبال موضوع «استقلال» تایوان، با «دوراندیشی و احتیاط» رفتار کند.
این دومین دیدار ترامپ و شی در سال جاری میلادی و نخستین سفر رئیس‌جمهور چین به واشینگتن در بیش از یک دهه است.
شی جین‌پینگ عصر چهارشنبه به‌وقت محلی وارد آمریکا شد و دونالد ترامپ در پای هواپیمای او در پایگاه اندروز از وی استقبال کرد.
این نخستین بار در ۱۱ سال گذشته است که یک رئیس‌جمهور آمریکا برای استقبال از یک رهبر خارجی به این پایگاه می‌رود. آخرین بار باراک اوباما در سال ۲۰۱۵ در آن‌جا از پاپ فرانسیس استقبال کرده بود. موضوعی که نشانه‌ای از احترام ویژۀ دونالد ترامپ به همتای چینی‌اش به‌شمار می‌رود.
کاخ سفید همچنین برای پنجشنبه‌شب ضیافت رسمی شامی ترتیب داده که شماری از مدیران شرکت‌های بزرگ فناوری آمریکا از جمله اپل، آمازون، آلفابت، اوپن‌ای‌آی، تسلا و انویدیا به آن دعوت شده‌اند.
شی جین‌پینگ چهارشنبه‌شب در بدو ورود به آمریکا ابراز امیدواری کرد روابط پکن و واشینگتن باثبات‌تر شود و گفت دو کشور باید «شریک باشند، نه رقیب».
پیش از دیدار دو رئیس‌جمهور، مقام‌های ارشد اقتصادی دو کشور بر سر تمدید آتش‌بس تجاری به توافق رسیده‌ بودند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از گفت‌وگو با هه لی‌فنگ، معاون نخست‌وزیر چین، اعلام کرد توافقی که افزایش شدید تعرفه‌های متقابل را متوقف کرده بود، تا ۱۰ ژانویه تمدید خواهد شد. آتش‌بس تجاری فعلی قرار بود در ماه نوامبر به پایان برسد.
در جریان جنگ تجاری دو کشور، تعرفه‌های متقابل در مقطعی از ۱۰۰ درصد نیز فراتر رفته بود.
مقام‌های آمریکایی همچنین از احتمال اعلام توافق‌هایی در زمینهٔ کشاورزی و موانع غیرتعرفه‌ای خبر داده‌اند. آمریکا می‌گوید چین در اجرای تعهد خود برای خرید ۲۰۰ فروند هواپیمای بوئینگ نیز پیشرفت‌هایی داشته، هرچند هنوز سفارش تازه‌ای اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=c5bvl6PgwbEAI_vqsj5qNvgH1f98j4HnEFn1YnHqo83O45lR21hc886M9LsXmMP4QlIdQN4YKfY26_89tSkLxCXSqhNE_e34XvVa59od3mKjWudX69EAAkAeuagIsX9Sr3UGm-4pAFYJFD2Ln85M52n4arj0IfLf_s4oHkLz_IbkE6_hW4Gb-3HbZahIJmR7NuGvR2TtikVTP24sADC9ZRUCVOJJ5TOgKhtupyAWnOxIEEGq_O9VzxvyYudH2o-k4UBjLnJAyV80W3RaQHbTMtEGbNnO_UYX4uTWE2vMVWW11iLpr7xv5J8bGOrT-JVLxAxCU3izmdWXT7LDs4PGWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=c5bvl6PgwbEAI_vqsj5qNvgH1f98j4HnEFn1YnHqo83O45lR21hc886M9LsXmMP4QlIdQN4YKfY26_89tSkLxCXSqhNE_e34XvVa59od3mKjWudX69EAAkAeuagIsX9Sr3UGm-4pAFYJFD2Ln85M52n4arj0IfLf_s4oHkLz_IbkE6_hW4Gb-3HbZahIJmR7NuGvR2TtikVTP24sADC9ZRUCVOJJ5TOgKhtupyAWnOxIEEGq_O9VzxvyYudH2o-k4UBjLnJAyV80W3RaQHbTMtEGbNnO_UYX4uTWE2vMVWW11iLpr7xv5J8bGOrT-JVLxAxCU3izmdWXT7LDs4PGWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=JsHH4UJZH80VjOOG8cTtIG06KtwAcC1MnqqaZJmp7KTtsoPkQ1_QEsHUHwWBHGiy8Tc7NN253wvy0vvdgQlNAg3nAGNNcwbqFdIhyzFjVj1vdIFCui0eLruMDMkanGIo9l6pULfpv7Bqqn5We_B2-D5Ex4PJaBVvun89rcqS-mbq6WFvgbN2NDIif9KCDGFcqLf8FcS4dTYb3t42AiF6vsbHYSnCcszl-m07yI39sRUl-dizJxvh6N_m4bJ-MQK_sEXBAB_spJ0gQP3864ptjyC3rcPoWbP1mSoItZEHrgY90ANBOkBf3UPT2Rialkare3R2gRLLuAPVPhkSOftedrxkwGt6kdqQVwCmw4aDShcCyNP5LN_YFrl5jdkMOB7Wb5QS8gX0oa6cGsLvRcUqKwbXUObTwsXTAOrWT4cyfgaieJT6OZaHx6Cud7aPAhevh7-FwcDWwlKdIztk1GO7Ype20FeWSs2YNBpSyBZD6uu4fKINVa76TSJNuDSXLhRi2PFeDu6KPaJpspVBBcF1b9dylT3zYHpP_qX7HjJRsu-r7gXRXt57UQxVoG4ZUsS5PC1VDYUTk34QXRjRznwKj_RzfJHqeViE4ryxQMpLJr6BsGkquEB2b5Hxx2GQqZk1FcplSIoq1CMFkq4uw1EI3E8iNwn2No3a6tHBmXPbHhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=JsHH4UJZH80VjOOG8cTtIG06KtwAcC1MnqqaZJmp7KTtsoPkQ1_QEsHUHwWBHGiy8Tc7NN253wvy0vvdgQlNAg3nAGNNcwbqFdIhyzFjVj1vdIFCui0eLruMDMkanGIo9l6pULfpv7Bqqn5We_B2-D5Ex4PJaBVvun89rcqS-mbq6WFvgbN2NDIif9KCDGFcqLf8FcS4dTYb3t42AiF6vsbHYSnCcszl-m07yI39sRUl-dizJxvh6N_m4bJ-MQK_sEXBAB_spJ0gQP3864ptjyC3rcPoWbP1mSoItZEHrgY90ANBOkBf3UPT2Rialkare3R2gRLLuAPVPhkSOftedrxkwGt6kdqQVwCmw4aDShcCyNP5LN_YFrl5jdkMOB7Wb5QS8gX0oa6cGsLvRcUqKwbXUObTwsXTAOrWT4cyfgaieJT6OZaHx6Cud7aPAhevh7-FwcDWwlKdIztk1GO7Ype20FeWSs2YNBpSyBZD6uu4fKINVa76TSJNuDSXLhRi2PFeDu6KPaJpspVBBcF1b9dylT3zYHpP_qX7HjJRsu-r7gXRXt57UQxVoG4ZUsS5PC1VDYUTk34QXRjRznwKj_RzfJHqeViE4ryxQMpLJr6BsGkquEB2b5Hxx2GQqZk1FcplSIoq1CMFkq4uw1EI3E8iNwn2No3a6tHBmXPbHhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی قلهکی، از منابع "نزدیک به حکومت"، با انتشار این ویدیو نوشته:
'''
اختصاصی: «تاجیکستان» و «جمهوری آذربایجان» آسمان خود را بر روی پروازهای «ایران» بستند
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه» _پایتخت تاجیکستان_ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🔻
پی‌نوشت: مسیر پرواز هواپیمایی وارش از سمتِ ایرانوبه مقصد «دوشنبه» _پایتخت تاجیکستان_، ورود به آسمان جمهوری آذربایجان و ترکمنستان بود که پیش‌تر آذربایجان و ترکمنستان آسمان خود را بر روی پروازهای ایرانی بستند و پرواز نتوانست وارد آسمان این دو کشور شود و بالاجبار به کشور بازگشت.
'''
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc4KwISvo9xbvMF2r6Z6Crg5gT1mgZHr79FfoOwhJgM-yIKmbn43LEX-YryzkmXvSGvDfAIjpTFK8nwnadLeQCEuZuQhgQz0dQlqGAr2jdgT9VkGU-dEJC5OfcpqEs6Doe8_WDR2-o_aoo5gp4FXsTmuVmjiEhXXa6LABM5puBOzpLSv8JPRW-EB81Basm4E0BkAvQ5apM-zMZjkDLNmd5gANTVPxc8l_4OQQA7-wYYGuh-1qOGhAxFzlqdqYyZiDhajZJIkcP-ev3vontvSRI7hte2eGAMartfohoLSsVLuMgBzFSzCXAcI61eB7HeovRMKHypFZFOvJ7TtZkJBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0HovreGe7sjjTC5T80g36ERYsoiL_AlqGfU61bUfokDl4F-csU-E_RcczQI7uF79mMQMFfDLHRwXb7bJlDzlGkLV_nEiTEtFV3JmsD3pDoL8YTLH9XNhALJG8iQMh6MTZwtWDzDnbrMnSp33R35k3Jv183zDSbjmOM1MizQjeB2BfhKDK5GOXgiyW5KEeAy95QlBzEpyUCvsM7DJDoAuJoIZhjQJ8bpZ6CgDQJFpW9Z5-frB6Y60PhHuvTkP1FWmT7c2orPxzwni1430CRoXKg2dHPLNVAzrcQJKV9OsuOWnca6ZGXGnG2pzJK3L1I-ealbzERzEgGWVq43HI2ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRRuChV7tTpdT7_PhnTTXXtjEKgyOApZ7aRsBmS5vJjfBNRz5kAYfnuWNFbtTjKnR1BNnXZciimHyMPp_bClAjH7W7xWUtmwtjKKVjqxWArCXTI5t9WVFiDbkD4i7IhlIEL98qc2QEtecnbMGT4u65XfpPbXUKdYMGJwYKHV-7v_HfPiVLOMffJIetCJ0ANdjOl08YEmUQtIer8FiO44kaIcX6Byd2msFw5_nOZVa3TZ9GTaZBM_nr0YaDE6X96jg1OelCqA_AdiNRDa9c_3lp1UmmuZVIboWktsgBR6L_vCcZrKg55bUq_t2VwaVPKHQqL3ZsLyOmu-bPNWuPia0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG_QI0z6OM8ULrU0lt3OoRjtPp8ZL0xyMVquR7s7FbXNAwPxI9hCN-hR3yd7z_20La2eK54ugt_lW96gjzFvhIJLXDQfBaIBRhYb2gknNRTPA7-WMUZmYuxERjPSB-bFBBnkxOQ5EBZXHrt407Ff5aXS7KzAIg7u37E74rM7M5YNJ70Kciwk0Z2lrAsl_F1gCWc8DoYyMhvIXbaIze2nHyvpbiCLdM8_KzOj_0v2ffKeYLiWZO3R-waG7PvQAQsCpyUB9PxJGhem--MU1ONtHmNFz0XXY9H1ah2QU1NhbmV89SIFpYy0q-bYXTZddXzZFXqrv1OIJ5ErMZoMEvx9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fE_mIoI-zuDsEmyZvXtxoGbE6bJCwH64H6FGISn0U8p7ttogNcmNRUKsQumxWgkV_-83PbsArrO262CsfCTxr6LjQ5BrFzHojeTWZJGREah4n89Uk0S5clRdBPImzs7_toqOsTv6-MwmJc2tiSCm2pRX7LX1or97MC5r_XVLWMrw2xh83tu0nAC-GNYO8DIx-FSdBraqwh4NsWZu4O14YOlzhJSJC1awZEyXWvMbQ1BIbjpi3jiiE_GePwJ1RNurKOLJ299YFrsLtNxqkS8E2f_E7sv9iASh6eJuN-fLELEGnimDrZGhMMgPfX-4fCalU7YX-mNW5u_HL2CUqBA15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCeaIG3bTUx4RBLwjpEBtyh9UnchJBEt062pahSpSYmsiJrHArYPQxYSeUme3zp4whxknZY4UAgdmz2lK9_tx0dIvmcHtDXxW_aXmTafoPBUbV6ylX6NguqrEhaV7ex4GOCS0ZinZyl9EJiF6CVFyKgQiEXWEejk0oBncFMLK40kvmxjZLP8malRt1uPpKCCanyBpyrncREykN5ZNXg9Bm-f64U4RAz5QhnKZGt4LUvQHye6WO0DFxI66Nth0EZ1cXzeieu855ZXNbq9Tu0ClLWvpet-p16_njJ6mPB2C5KAKokR7TegUmgQO9RQ_gJpov6AocpR8mM3FwdeLtfoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cUqL-yx0i8L5_FsQuvd8XnTLXQuGYweI7_j8fmT99-atu0zU3JP1CHaK_mnBhsfaT_CWVaiWly4KyJtItKJV7FR0AMGXGoV1olh9u9AEGiq2g7iI7pAKOhCPF0g2BLkkcL8jeT2EU1b0HdTsuOX3EO0xw3mvDfyHfZARwgYAyXxK9arYTK6gJ9tI008ejgq6dutBlMbER5rFiwK_P5HrI1o3eThYvqAVwgl-pRpmaY_WYuc7BVnMQHECmA3MuT0tZFu5xNFpY02YjYAvhZkKEgy-KdnndjaGXX4mhKmO2gdbKqyJA23wwWu4gqEkMN4btI2y3BqgIuY3QF_Wh98jrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=d4oa8TwYqffbuGhF-D9GrmHVN8KM7sBymyKdmoF0J_w97jjqGTEaIV2-1hPUUJNJUUNVsd1mAzsIgeIAlZ-toLZbFoZKJ9Gbfyc8mFQxRLNax20iTGa3xiTlGJStkAL6oqjaex3EBK8EpGd450HthnZRM4n8dumJJozrIRQVOG6J-qkvLk-4UoTCab3uWufpw3mWGhpp7ygB6mDI10TkFHBfWgaMKZ8AdqvvS4BBQq0LUf5Hm2TZEvKqXmzFVZE1Pe5onniLLBYd9EnVdkqoG_r0JbtL0pIZk6Kvt5n8TcGv0B3tq5RjKJyFhVdLXHeAUx8i1NIZ8K4wfTyEtLw5uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=d4oa8TwYqffbuGhF-D9GrmHVN8KM7sBymyKdmoF0J_w97jjqGTEaIV2-1hPUUJNJUUNVsd1mAzsIgeIAlZ-toLZbFoZKJ9Gbfyc8mFQxRLNax20iTGa3xiTlGJStkAL6oqjaex3EBK8EpGd450HthnZRM4n8dumJJozrIRQVOG6J-qkvLk-4UoTCab3uWufpw3mWGhpp7ygB6mDI10TkFHBfWgaMKZ8AdqvvS4BBQq0LUf5Hm2TZEvKqXmzFVZE1Pe5onniLLBYd9EnVdkqoG_r0JbtL0pIZk6Kvt5n8TcGv0B3tq5RjKJyFhVdLXHeAUx8i1NIZ8K4wfTyEtLw5uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9-uGYwF2icR8mW_79_-GOjs3F1iXZMx8ZnxwBMMWCIFZy9EDqxZ58pGat1z7wa3873mGyw4zSAJs0Rb_A9snvhIw6BuX5BWtzQVarIHK1wUC-869RZLU8-3DPWD6S7ixwLPoUP5HAVYEJAmRUFA916lpXPlLPG_-XVkFe13LDZ09GZtt1jJJvWYFCjYMIbymoEL2twXZhgGPkEiJP4Osfs-RlUrSJu40CWqYW6C2nghHRuO2uUFRm09W-pmT_jJDI7H522GWFg8tcKR3tpVAWBW-OUa3Dnalw1m37gJVVNL0jadENDieeppeJ8nielBftvNzo_tl-DxCeGJfAg3dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=RvNICjmGIi-eLNvqEq3MQxM6ErafogpYhe9CS1IWlgoUVJgSsqDVMbLWnFRoVpba87tZ3k6JH3YPwUV97r0qxZFy7SQtr6EYKWtptDDokbIng473wegcnvWV6nujfMlSWrOqXwgW1C7JqcufObeKyO0eRZkg9Hn6W164cbQUuC8RhRYz1Ur_7q-7aiMz7T0u9cgBgwQQVDPh3FehbQekDQvuCnGe9yJuNK1YGqlOZcJxx7ciaJqm-kdBJZxRdhvGsjWVjGDF9OBpckc-oRrXHAcQP3emAtBySIcqOC_agZxPz2-jpLzJ22JymfaKTXZTviyC6vssA6b8BM650o8oIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=RvNICjmGIi-eLNvqEq3MQxM6ErafogpYhe9CS1IWlgoUVJgSsqDVMbLWnFRoVpba87tZ3k6JH3YPwUV97r0qxZFy7SQtr6EYKWtptDDokbIng473wegcnvWV6nujfMlSWrOqXwgW1C7JqcufObeKyO0eRZkg9Hn6W164cbQUuC8RhRYz1Ur_7q-7aiMz7T0u9cgBgwQQVDPh3FehbQekDQvuCnGe9yJuNK1YGqlOZcJxx7ciaJqm-kdBJZxRdhvGsjWVjGDF9OBpckc-oRrXHAcQP3emAtBySIcqOC_agZxPz2-jpLzJ22JymfaKTXZTviyC6vssA6b8BM650o8oIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=VjetPSAZjvUbKnZX5NaRLmAJXq_RWKZGOFktgTlUTPFmiMiCsQDW7w3rgUWTgRVNvyDBT1hd765Jclglribi_L4a8klFEmSR79sYTgwlsIfBRylmDkTOiQSB8M-6JSNp64gf9UkK6Uc8hDUdNh9A3lwc3OFuKAdG9Hq_TjxLs0zQSH4typ20f4nGc1UP4WLhLnMGCcQgwNrhqW41aB4oHab33Sp_arkaotv5yYG8WvFY-IGl0yd0RzTw-eW2yG4r7t3upYLLCeG2hu9E5xixDMfFF-YGJ_QcropsK1_2eHR_0On_JM9jx7Axt9nIXNU0OGb4i5Vcl87RakXAUj33iA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=VjetPSAZjvUbKnZX5NaRLmAJXq_RWKZGOFktgTlUTPFmiMiCsQDW7w3rgUWTgRVNvyDBT1hd765Jclglribi_L4a8klFEmSR79sYTgwlsIfBRylmDkTOiQSB8M-6JSNp64gf9UkK6Uc8hDUdNh9A3lwc3OFuKAdG9Hq_TjxLs0zQSH4typ20f4nGc1UP4WLhLnMGCcQgwNrhqW41aB4oHab33Sp_arkaotv5yYG8WvFY-IGl0yd0RzTw-eW2yG4r7t3upYLLCeG2hu9E5xixDMfFF-YGJ_QcropsK1_2eHR_0On_JM9jx7Axt9nIXNU0OGb4i5Vcl87RakXAUj33iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGlD9PxIUTOJlQ-In1JVtyYI1bPNVPtYfyxQFllp-JcVunrQrOeRe333Hj3FDd6pef4-di-wJKwDNSYoBPhyWqSCOvzkWo62c29LYR0Q4jsm-5K1ttj2JX75xj0YqHGOc9-0iVcQbsDBdrIho-b6E8vloqM6K9V6PH9bYyVVW4KT8JCkUtDeCIb_riqfYCDlE5tYIqSifjqFh9H0OyhFpdpzVGB8zZR6VNsf2siA10ResPMdVr-6zSESaQXhEom2k5-e4VDbl63VfswKppBOsMT49ro45dFaUVxjBxX9KWy-pslr4qqGE9yedgxVdlvdGMVgl1DjYV7YmsIE0ww1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=mHftFDhh3ItdzPiwei4pignCANzlZaQgoZ2XCRTLAuNzOerysDqpwN3IArfgboEUqD3euHBXj25eRGYq54B1yJ2n1qmX3-pkE3E4zQ_ezIKywOAbgIVLOEWEf8ELOXJ_1bGMzjVLxOVhLNBf15wnteobFAJ-PB29oKv4z6FOpkuj4SKC825CKYyCceiyUDrMn-7-NLRfkDLdWJM2H9H9w_afn6j2rEm15fBzztCC6qSBjWt2ctWQqHaLKZM8W3Vs-pVK6I4ZRfu9MdRgkYd00gJFRPLFGhytze_g3ZI1J5BBHcCOWgHld8c5pWier6CWCaeNJwukIdJK9PxMzAdV7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=mHftFDhh3ItdzPiwei4pignCANzlZaQgoZ2XCRTLAuNzOerysDqpwN3IArfgboEUqD3euHBXj25eRGYq54B1yJ2n1qmX3-pkE3E4zQ_ezIKywOAbgIVLOEWEf8ELOXJ_1bGMzjVLxOVhLNBf15wnteobFAJ-PB29oKv4z6FOpkuj4SKC825CKYyCceiyUDrMn-7-NLRfkDLdWJM2H9H9w_afn6j2rEm15fBzztCC6qSBjWt2ctWQqHaLKZM8W3Vs-pVK6I4ZRfu9MdRgkYd00gJFRPLFGhytze_g3ZI1J5BBHcCOWgHld8c5pWier6CWCaeNJwukIdJK9PxMzAdV7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd2k0lcZShsX_9c5Dxvc8baeGqWrqVAFwSyXRMZJKYLKfJc79lApen8uufVeLu1JGTE2ghnfSxDHp8kLKuQUlKsqTUH0B5DjOoNKVGW3q_LWHd6RT6vNgnu1ga1YJl9TGiE89_HtDUfQ6ryrYTpmDDIQenm0aBRm_2st6433f5n2CUcMbOz3FqIMu0buSza3AsUHc5LOfaWMKTijAr6JTdXVscokNBJGHuY8uOzoUcMz2bHy-fvIY7J8Bwa7G33sIJ0ky4ZPuC9YXLZEJ1ZdVj3MSuHZZXPb15fR_XBmAYckMVBmMe9tjmBN7aDqzLGDgtmrIF4BgADsFMMVbheueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=C4gawlaRTwtGkw8D4OxZnhM56KdYhTf5wEdJ0DLIjsgzwypFvxBmopd37IrtnIpgHBq6R9BSw7CxwiC3lZKadpqYqMK1atvjbVCXE0mh5hdE_YusAsMfTod1_2YzL3qW0eW6ZlgewPrkUhKXh_zeBtDCTWMnimY42Jpnyx2ciPZDThpBFRCmHeqmU8adPiQ8Jxt4OobYxG9K0UOjWT6Llc1VHyod0BmnHvyCKgnaZ_0l0JHmqYkRc0azDLWnuiF9SEBYVh6b9oHAMaNyER5ruubxdiJ0ebeVY3dUZ493r_TBpAaUucABbiFd1YPq1pjbzkupGL5CRH1Q_7I0SnbZelogjZldpHEEnyolcc5edt9p0HoQg0RxrSWPXz_90o1hOxpufk0xqSipdlyMRPY8lAZaixT46gCW_Yff_kF35G4N8feJ6_MKz4i6G-FgMbsyrt34FbL7mzRuuQULBL_6GMuiHX741dsIJEAccNfBDO2i0DDp_RrbUFJLrEQrH8kt_2DzPbdHYo0rRzqH00ftkoxRrYgFTvshF504qXy4Xmxz0ZCmPE1xWrwFqYiMRBosG7jvw8rPDIFl6Qu2rjB8KLClJhEyiwh7GNJVRV5YpqwukeNZEiZKc6Plk1UAqznPFr6AW0SZBy2ZsD4FTRDlK0aqr6WzpZBLlP6zs4W8xo4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=C4gawlaRTwtGkw8D4OxZnhM56KdYhTf5wEdJ0DLIjsgzwypFvxBmopd37IrtnIpgHBq6R9BSw7CxwiC3lZKadpqYqMK1atvjbVCXE0mh5hdE_YusAsMfTod1_2YzL3qW0eW6ZlgewPrkUhKXh_zeBtDCTWMnimY42Jpnyx2ciPZDThpBFRCmHeqmU8adPiQ8Jxt4OobYxG9K0UOjWT6Llc1VHyod0BmnHvyCKgnaZ_0l0JHmqYkRc0azDLWnuiF9SEBYVh6b9oHAMaNyER5ruubxdiJ0ebeVY3dUZ493r_TBpAaUucABbiFd1YPq1pjbzkupGL5CRH1Q_7I0SnbZelogjZldpHEEnyolcc5edt9p0HoQg0RxrSWPXz_90o1hOxpufk0xqSipdlyMRPY8lAZaixT46gCW_Yff_kF35G4N8feJ6_MKz4i6G-FgMbsyrt34FbL7mzRuuQULBL_6GMuiHX741dsIJEAccNfBDO2i0DDp_RrbUFJLrEQrH8kt_2DzPbdHYo0rRzqH00ftkoxRrYgFTvshF504qXy4Xmxz0ZCmPE1xWrwFqYiMRBosG7jvw8rPDIFl6Qu2rjB8KLClJhEyiwh7GNJVRV5YpqwukeNZEiZKc6Plk1UAqznPFr6AW0SZBy2ZsD4FTRDlK0aqr6WzpZBLlP6zs4W8xo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zr8i1tazZrKS4--qJps7yZj2ZBmk9S0s-KF67o5VIUJeyNsUovdTp-MdFFPw042hM40b9s1aXh3sImx9oPf0-9zoPdZno4omhMiBTY50_ixPK9zOA8VkSm4Zxd9PWrA5AKq9a9DFu46PfZXxLjaibkuil47OlMP-yYAxI4Hj4wb7fiaSFXI7SGIC8aqziW4Ped0TxfOXYo2Ufyp5uiUvn3Sl_MEu1D2ZGr7Xk6Ae70aEmJLzevj3A5ZPeNydrSEh5VHoR5FS0OFaW-5jjzReu0jvv3Zjq7SXeZ_E5Vdv5kirsT8ULb9UDvQ0-TAYm-MngzXibBbgcdvvDrnHepP8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=OWy-km-XbYfNIF-8lQrV_Y1VQ1v_kSgBiF5jPe--1oGFdu775Psc_7t4ocDTBrQAXUerBNcUNwUPeRsNREVajaAIH3pcbBkIQtqX5lgqaiJWb91Y6TZaDz5ndGFBEN0BDVgujTVsKNTiW-yM1QsKyO-l_ldK97ou03VqDehn2-P2HPz3di1kTfdcsbj3YN6DStQPbaPWW5TN3OmbQh-JGN-o23LInxRLHqRgEsTejc-mvZBxcZOALFUtTba1uXjl9HCFpChyZx8TaFPwa_FVQo1BfrmZ-uD2fK_NPBcHqc6QmYv50qtCTk6n0g0iB993iLshmjuOM6mvMSmo9XyoQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=OWy-km-XbYfNIF-8lQrV_Y1VQ1v_kSgBiF5jPe--1oGFdu775Psc_7t4ocDTBrQAXUerBNcUNwUPeRsNREVajaAIH3pcbBkIQtqX5lgqaiJWb91Y6TZaDz5ndGFBEN0BDVgujTVsKNTiW-yM1QsKyO-l_ldK97ou03VqDehn2-P2HPz3di1kTfdcsbj3YN6DStQPbaPWW5TN3OmbQh-JGN-o23LInxRLHqRgEsTejc-mvZBxcZOALFUtTba1uXjl9HCFpChyZx8TaFPwa_FVQo1BfrmZ-uD2fK_NPBcHqc6QmYv50qtCTk6n0g0iB993iLshmjuOM6mvMSmo9XyoQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6eKeiVKQPjfjH07-IKTNtW8UAlBieB9etCh7etMQtjpXQLk_sjECZivMPW1vkhCSiKDKWHDKPMZzzW0FPMcN40aAX1rFVMNZ4hibIwUojdDhr9bb8bRODcz__h141UW9l_oIZtIMvFwS9vdlxECoOpwK1NVOyNYoXd8yooMnh55ZngakywosCevWjtWuKcYnvITeg_pgfKxYU2a4iG136kMukLyUpprWI5mjDe_ocg_S1GEWseSvGy2w1jP8NgLyVq8SZDKQKQODAzEZYFzp-eapyiWqjUt2NiidmNE8pM0MYpaTkMDbZvtwCsD11fBLMAqGITJYaseqeM6lu8U9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kg983LLkV0dwVak4Z_lI3w00kIMIW9Okd0ONI8Ka4XDo5_JjCPFKkRDCeVJ1zZNqEN-U9y_3k_nXYtaZ5XTcirB4hDESHDWbnXyy-j6-rzPg2wtFyH-c-mtakIH-tsGf7786eDV92RJf8UJ-NlMwBt0ht-XBxMNoRBix7CQctF4isB2NQ24fyz1QXCYioqkDmfW5_Qo9W4vfbu7xwwCp1dOm7Mu5jb-092e03wLL86cK-IRYR7ogNM5TnL9QrIe4yjzP61moxI7oUTT6blGWf-Pw2rJplKnkN_EOcVPWec_LQwm6627oC1fGznXHp56S9XGuSQ3epSnyfYFVFU30NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSyYCsGZcQkBc43zlUMWIVnvELqysdJlM5npcoFDjSq-eGv_lbEZws8FhywkFEyqqzLb_jxph4ulnTnNORBg-oo6g2XTpsNHJTGj9Kx1-IZsVM_zPQn6uYAfk7w8qqcWILgDb1IiSamjuhbfora8Igw07MmecySo2IzhI1mFRyXxi27ZFbuZA0WJsgSBHJKOwHQO90bk9TqnSCoujJrk8oAUcpxCQWMaAQk3mqbR_RzITVVlI1nnTDTAlHMkfoORUVXrupasuVeqDuTSfKjtpfGFCe5owzvDSe-wkjStz478kb2Sy7NGRs0Eq0lRbjK9Dcbc_TmdmtrmSkff_Feing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Khf3U0njlNDi01-0qQP0wsrddEaU9CwA8kW3A9Oscjm4ejmuhpFCnFYBOJHeQDMIGlpgDY4Vhk06Q9rfooDizwEMZJjZy6hp6-UEPtzdWz8xQ2MfoLiJf-rAmZ8AgKPlWAxxugrC8hyzpD-IiZOQokZHWTJ22oKK06PhbTSWud_FAhj4b56SILK4IOWGmlneX9HFm8Dho8BMP_NNQ4m4DwQWqgKirQa4L9X0Y54ijlTNgCkt1nNN3idJYWAfaaogNgkA8IXCv7HNDRIbR1wtz8uj6e3yOin9W1CvAve6TpdR3soj4aNnPHE-EBB-vzfgn359hpDiQ2twwopYP8I5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwKZZFEVeJfX43Y5BiarY6BvhIXmQnQUUCzTs5c280m7GjqqlWdZhHawVxMOO48uRivIrr3Eo14f2_25WM2UPQNH1C7OcGt8c9lZt0XMr9Jf8ObdknMyyFAYmlhnCBvR_Qx2rSMsAVM4bIfC24WMAn5WeU_hNukpMpOeRc16m84sUezUY69SVxLt779tjf-45DDJnkS03NwtwnuM9NWey-E1-gAzlJwiTsLiYmFSwcxd7U7aOI0xY98KjF0bJJs3-Qd6yWOkFgLYS57cbV3oha4fhtWWrwI_fsff80rAHrgDer37V4lB-mKYkDEZ3Uy-y7wC83JRb9XE48rFh4UjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpxDYUb8iaOrzs5pe29LhNOPj78l82vqAhTRjQdL3o30OFD-r0oDT8eSFI3vAS9LVF3pWftcUFWFB-iLjJ9QAh6LsHP2Qs93yogX_udA83UgMZ3rSEdjnzatqV4co8kKFYhtwlfOrmWrxpvTg8jxfa0HSZZ4pFOjcL8twTOzWjCAIjysc4VftQYJFMeDX0q7k6oG6uhu4p3G2uqnk1XxqK43h1SqO6dvabhwSaOW2fWCxs0ePOdGbgfIN60U0TYGzVyv1sQTaXDY8h2F0oURQOQiWsg2Q-Do3eC4pk-KpwoWEokwdQKUsI1RidUJnr8mSowE3p-1IrJRv7n4vIcYnduM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpxDYUb8iaOrzs5pe29LhNOPj78l82vqAhTRjQdL3o30OFD-r0oDT8eSFI3vAS9LVF3pWftcUFWFB-iLjJ9QAh6LsHP2Qs93yogX_udA83UgMZ3rSEdjnzatqV4co8kKFYhtwlfOrmWrxpvTg8jxfa0HSZZ4pFOjcL8twTOzWjCAIjysc4VftQYJFMeDX0q7k6oG6uhu4p3G2uqnk1XxqK43h1SqO6dvabhwSaOW2fWCxs0ePOdGbgfIN60U0TYGzVyv1sQTaXDY8h2F0oURQOQiWsg2Q-Do3eC4pk-KpwoWEokwdQKUsI1RidUJnr8mSowE3p-1IrJRv7n4vIcYnduM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=Zg1-iI15yD4taJVphWZctVKmEq3xIBwWP3Q_yjXD98Caakfil_BSNBP85qLNOV0z3TyLybiw7h3VCPwjls-OW7RLt1tSorN5Mq2dSeQ-6UGIfC5aEQ2Plc8-a9uC66hCI9Zmk-g4_5lZZcmftIAt7upttcERDVc13yJnRUr4LDERwJHYdNJISlReBXjNWclgAwQ9olSfyoKHv6_T6_OmAYZAmJ1MU2-xDOtbuczRc62F52bUYKIsUEO08Fk9MXoqqAt8ezmumMFC5MSe9yM5O3vZosCqoGW0O6VmUHj4NglNWn1qLNdEWRO_vE0lOLGroOzd1HVNeou9TjUIBoqu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=Zg1-iI15yD4taJVphWZctVKmEq3xIBwWP3Q_yjXD98Caakfil_BSNBP85qLNOV0z3TyLybiw7h3VCPwjls-OW7RLt1tSorN5Mq2dSeQ-6UGIfC5aEQ2Plc8-a9uC66hCI9Zmk-g4_5lZZcmftIAt7upttcERDVc13yJnRUr4LDERwJHYdNJISlReBXjNWclgAwQ9olSfyoKHv6_T6_OmAYZAmJ1MU2-xDOtbuczRc62F52bUYKIsUEO08Fk9MXoqqAt8ezmumMFC5MSe9yM5O3vZosCqoGW0O6VmUHj4NglNWn1qLNdEWRO_vE0lOLGroOzd1HVNeou9TjUIBoqu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
ترامپ: ایران در پی ساخت موشکی بود که می‌توانست اروپا را هدف قرار دهد
▪️
رئیس‌جمهور آمریکا در سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران به ساخت ذخایر گسترده موشکی و پهپادی ادامه داده و مدعی شد تهران موشکی ساخته بود که توان هدف قرار دادن اروپا را داشت. او گفت هدف ایران این بود که در پوشش چنین توان موشکی‌ای، به سوی ساخت سلاح هسته‌ای حرکت کند.
▪️
ترامپ همچنین با اشاره به حمله هفتم اکتبر گفت عاملان این حمله از سوی ایران تامین مالی شده بودند و افزود حکومت ایران «چنین خشونتی را جشن گرفت». او سپس حکومت ایران را به کشتار گسترده شهروندان خود متهم کرد و گفت چنین حکومتی نباید امکان فعالیت «در پشت سپر هسته‌ای» را پیدا کند.
@
VahidOnLive
🔻
ترامپ: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند
▪️
︎ دونالد ترامپ در سخنرانی خود در مجمع عمومی سازمان ملل، جمهوری اسلامی ایران را «بزرگ‌ترین حامی تروریسم» خواند و گفت که حکومت ایران سال‌ها در خاورمیانه «مرگ، ویرانی و هرج‌ومرج» گسترش داده است.
▪️
︎ او گفت: «هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند» و افزود پس از آغاز دوره ریاست‌جمهوری‌اش، مذاکراتی را با ایران آغاز کرد و در مقابل پایان برنامه هسته‌ای و حمایت از تروریسم، پیشنهاد همکاری اقتصادی کامل داد، اما به گفته او ایران این پیشنهاد را رد کرد.
▪️
︎ ترامپ همچنین گفت که ارتش آمریکا در عملیات «چکش نیمه‌شب» برنامه هسته‌ای ایران را هدف قرار داد و پس از آن نیز از تهران خواست توافق کند، اما ایران بار دیگر نپذیرفت. او سپس ایران را به ادامه انباشت موشک‌ها و پهپادهایی متهم کرد که به گفته او امنیت نیروهای آمریکایی و دیگر کشورهای منطقه را تهدید می‌کرد.
@
VahidOnLive
🔻
دونالد ترامپ: تصور کنید حکومت پلید ایران پشت سپر هسته‌ای حملات تروریستی انجام دهد
▪️
︎ دونالد ترامپ گفت: «فقط تصور کنید اگر چنین حکومت پلیدی روزی قادر می‌شد در پناه یک سپر هسته‌ای حملات تروریستی گسترده انجام دهد. این واقعیتی بود که باید با آن روبه‌رو می‌شدیم؛ واقعیتی که افراد بسیار زیادی ترجیح دادند آن را نادیده بگیرند.»
▪️
︎ او افزود: «در حالی که دیگران حرف زده‌اند، من عمل کرده‌ام. در حالی که دیگران از صلح سخن گفته‌اند، من آن را برقرار کرده‌ام. در حالی که دیگران تهدیدها را نادیده گرفته‌اند، من با آنها مقابله کرده‌ام.»
▪️
︎ ترامپ گفت: «من از آن برای تبدیل آمریکا به قدرتمندترین کشور جهان استفاده کرده‌ام.»
@
VahidOnLive
🔻
ترامپ: امیدوارم پس از انتخابات با ایران به توافق برسیم
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت که آمریکا باید فشار بر ایران را حفظ کند و افزود نیروی دریایی آمریکا تاکنون بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت کرده است. او گفت اکنون نفت بیشتری نسبت به هر زمان دیگری از آغاز جنگ از این مسیر عبور می‌کند.
▪️
︎ ترامپ سپس گفت که در برابر ایران با یک «تصمیم بزرگ» روبه‌روست: یا توافقی حاصل شود که به گفته او به ایران امکان بازسازی و تبدیل شدن به کشوری «بسیار بزرگ‌تر» را بدهد، یا آمریکا مسیر نظامی را در پیش بگیرد. او در عین حال گفت: «فکر می‌کنم درست بعد از انتخابات به توافق خواهیم رسید، چون منطقی نیست که آنها توافق نکنند.»
@
VahidOnLive
🔻
ترامپ: نیروی دریایی و نیروی هوایی ایران از بین رفته‌اند
@
VahidOnLive
🔻
ترامپ: انتخابات در تصمیم من درباره ایران تاثیری ندارد
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران ممکن است منتظر نتیجه انتخابات میان‌دوره‌ای آمریکا باشد، اما تاکید کرد این انتخابات در تصمیم او درباره ایران «اصلاً وارد محاسباتش نمی‌شود.» او گفت: «تنها چیزی که اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
▪️
︎ ترامپ همچنین گفت برخلاف ادعاهایی که به گفته او مطرح می‌شود، آمریکا با کمبود مهمات روبه‌رو نیست و ذخایر تسلیحاتی این کشور با سرعتی بی‌سابقه در حال افزایش است.
VahidOnLive
🔻
ترامپ: اگر توافق نشود، جمهوری اسلامی ایران را نابود می‌کنم
▪️
︎ دونالد ترامپ در مجمع عمومی سازمان ملل گفت باید تصمیم بزرگی بگیرد که اگر توافقی حاصل نشود جمهوری اسلامی ایران را نابود خواهد کرد. او گفت فکر می‌کند ایران بعد از انتخابات میان دوره‌ای با آمریکا توافق خواهد کرد.
▪️
︎ او بار دیگر گفت جمهوری اسلامی ایران بزرگترین حامی تروریسم در دنیاست اما اکنون دیگر تهدیدی نیست چون آمریکا برنامه هسته‌ایش را نابود کرده است.
▪️
︎ رئیس‌جمهور آمریکا بار دیگر گفت اخیرا ده‌ها هزار معترض اخیرا در ایران کشته شده‌اند.
▪️
︎ او از اروپا انتقاد کرد که متوجه تهدید موشکی ایران نبوده است.
▪️
︎ آقای ترامپ بار دیگر گفت تمام قوای نظامی و اقتصاد ایران نابود شده است.
▪️
︎ او همچنین گفت دولتش در ۱۲ ماه گذشته بیش از هر دوره‌ای در تاریخ آمریکا در زمینه نظامی سرمایه‌گذاری کرده است.
@
VahidOnLive
🔻
ترامپ از همه کشورها خواست ایران را «به‌طور کامل از نظر اقتصادی منزوی کنند»
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل از همه کشورها خواست به آمریکا بپیوندند و «انزوای کامل اقتصادی ایران» را اعمال کنند؛ تا زمانی که به گفته او تهران حملات به کشتی‌های تجاری را متوقف کند، از «جاه‌طلبی‌های هسته‌ای» خود دست بکشد و حمایت از تروریسم را پایان دهد.
▪️
︎ او حکومت ایران را «ضعیف و مستأصل» توصیف کرد و گفت اگر کشورها متحد بمانند، به گفته او «تهدید ۵۱ساله تروریسم ایران» پایان خواهد یافت و قیمت نفت نیز کاهش پیدا خواهد کرد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp39mIlcOOHukDGPCA4RvBUqhrN1_kgLl0AianLy9mqbITf2WSB9NahR4mRWs_KV1Ovw6g0lhsyqqUSgRAmUdJX4yUEWRnEtey2tVakhPrLP5Ek_rSv2NPiI2RFo7OJMvWP05vSaR_Ouw3DPUniWu3ZP8Tuk3y3ZxZwOHX33QhpzcOwEPZkGgtvmuF4WOKY4HES8XtZDuh7VAD2r678cB_3iQWtFVal5Gvxt35_NOYFAysVCIZFSMg7MWRMGr4vWe_KDdPNsgHhL8cUSPQ1feQKSWOYqDCaIEo9gzYqmbLKgrt6fcr315O96kK_czGcs7HuVKYmLSbquAhENWKCJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد جمهوری اسلامی گفته است تهران پیشنهاد کرده در صورت کاهش فشار نظامی آمریکا و برداشتن گام‌های اولیه برای پایان محاصره بنادر ایران، تنگه هرمز را ظرف هفت روز بازگشایی کند و به مذاکرات با واشنگتن بازگردد.
خبرگزاری «کیودو» روز سه‌شنبه۳۱شهریور۱۴۰۵ به نقل از این مقام، که نامش اعلام نشده، گزارش داد این پیشنهاد از طریق میانجی‌ها به دولت آمریکا منتقل شده و بخشی از تلاش تازه تهران برای احیای مذاکرات با واشنگتن است.
براساس این پیشنهاد، جمهوری اسلامی خواهان ازسرگیری مذاکرات با هدف رسیدن به توافقی برای «پایان دائمی مخاصمه» میان ایران و آمریکا است.
این مقام گفته است تهران در مرحله نخست انتظار دارد واشنگتن نشانه‌هایی از آمادگی برای بازگشت به مذاکرات نشان دهد و اقداماتی را برای پایان محاصره نظامی بنادر ایران و توقف عملیات نظامی مرتبط با تنگه هرمز آغاز کند.
در صورت برداشته‌شدن این گام‌ها، جمهوری اسلامی آماده است ظرف هفت روز مسیر عبور کشتی‌ها از تنگه هرمز را باز کند و به میز مذاکره بازگردد. این مقام تاکید کرده است آمریکا برای پیشرفت دیپلماسی باید «جدیت و تعهد» خود را نشان دهد.
کیودو نوشته است پیشنهاد تازه تهران به تایید «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، و شورای عالی امنیت ملی رسیده است. مقام ایرانی مشخص نکرده که آیا این پیشنهاد به معنای عقب‌نشینی تهران از بخشی از هفت شرطی است که پیش‌تر برای مذاکره و بازگشایی تنگه هرمز مطرح شده بود یا خیر.
براساس گزارش کیودو، شورای عالی امنیت ملی ۲۵مرداد تصمیم گرفته بود اگر آمریکا ظرف ۴۵ روز محاصره بنادر ایران را پایان ندهد، جمهوری اسلامی گزینه حمله دوباره به نیروهای آمریکایی را برای خود محفوظ نگه دارد. این مهلت اکنون به پایان خود نزدیک می‌شود.
هم‌زمان، یک مقام ارشد ایرانی به «رویترز» گفته است هیات جمهوری اسلامی در مجمع عمومی سازمان ملل در نیویورک اختیار کامل برای احیای گفت‌وگوهای دیپلماتیک با آمریکا دارد و جزییات توافق احتمالی می‌تواند از طریق کشورهای میانجی در نیویورک بررسی شود.
مقام ایرانی احتمال دیدار «مسعود پزشکیان» و «دونالد ترامپ» در حاشیه مجمع عمومی را رد کرده، اما گفته است همچنان «امکان حرکت به‌سوی توافق» وجود دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyjYEz04VlkZEMmYWGGlv5KqTIDCZ7SWySOqQP0Gx7nSfK4BcAiNZkbEdcdtAzaRBuvArq022kPODpr7u9Zi2NFBzRyf8VafcWqFJiEiWI8IZa2AOy_jewYPDY42HhVMfCFQ2Hb-1FMDGs_XXj2_dAa2IHT29XIR8453Zaf5MKgltVCw43VEyRrchgK8oq2i_qTT7mc2GqHWvqLpGeGvfPQBemnhkVRdoPvqJO4CMyBwmgHx0A-1Jdtqh55a_gDwot_OAvGfVVUKpOIVzeM8_-JyoAEWSwfJwG8BHrd0-52GZ2pCzqwalxx4S_89aqqw7SRX0Y0fAnU1SOj2OLRmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpF9UmXQdvv0MTuyHB1QJnRv3_6HBja_XHyHXfQAU1CH8FGscKdZ2lwkLMD-HLUrk3-zFmeLMkYojMz1YvqQn6FmjI_4RKgtg1ryhilOmT4H8STjqlw9UEpYo5OOREYB1BCaDPpiXGQB9bPZcKYhYD4j2CQhcujdC7PJkCGFvSF9ufDPKC2sg2vZBdNpE7CYrUoUz1cizbvbHyF9zz3MCBj2hrxieXgxqpj8sWZcPFxO5KvzpamCe8RPxjNsjBg5VEzvKWqKYXlMDOzjpj2kjOuAB7-uHVEVJveayuN6ZaJ1p4afyriz3EFvfHH-ZwQw05Xe5wWzDHpWoMGCgZE7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzutZZLjchBL5H-jhqLRFWQUdS1d_53OfeWZoFyzSHE2kCAGl7kCxgtslMyqQKTPEQt2GY0HA4i9B7FKMACkDO99fQMZeFMnno8Cp5cwLYTuV8N1RadeWs4Z9kpa7SGKSINzoWDWBvnAbhXpTxZlvyo2xyehTJbpuRYqJrZsOEK344Pexl57Zqm7seqMX1Esf3fUfO31RyCiX2HX2VSwR5WuozYHOST47QwVRIbRQOZpUuYS3SkA9SZWDB7k38dL54bbkeYKhXC7KPglpEwZ__r71FHGZEGgbP8wezjhf7bJ785ceQ2Q0HuVG7TlejHMTxJlnCiC97Ke8FsJ-tX2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATE5np9Dxakc-SPivmPuLKzG5i38miLSwcFF2YAU5WMp2EcKkDovIbZsBJRjYPswymzxT9Y5gsEGxTvReVESnH7Bwkd1fsXMypPQtNgOjuVUR7exPWX7M6P-SIi9PLpV5NKM3OEWRHW10CwiVUqNLPsrcEoYnpH7aJwOQ1ZfO9hTlFxR8LfkOWuao0gv5DSWx6zcPt9YUqaZPn4-NZg7367VK5pi6B9HxXWBxU4M3xngP1VrLwYYLjxiAwfSDAvEfrXmiW4LfwQ7Ry0tkVIFNk6RsOnRlCAYUD_msj6_vxOxxXZ-tIYrBFsiO7AsZE09FtFERrjy3A9-HGdRyGOlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSp3BDQaS6q8_1Lw5NoXyxw5kdW5JcA8BlrHvbrFnzcfkdvfQ1ozAwmeA8Wvk9DYDuZ1XaWetLodbKvSPLeyvWGA-AxE1qs_5S3T4_Qf_M1ZsWX8GmcSbDZ4nHXJ9nX0ZuB5-CKyLtZ7IKyHF1EsnzPYbfs58yu7bkCXcR_ZK_KwIHoFBOPUvuael0yrkJfctUrPY_RGLBU7GJM5u_tsUJkvy_1BY7ffykscvQrUhhHIQMRMPIyuyWIZV-YCqjC_aTQBI60UAvEuBiercvgd-6oKHqaHLddhpO2lhW9vuEUnLltXKlp4s38trbvGqTnJ3-LCUjW8hJpeOZwOAXvMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqwgA2wrRuMhqnHiM9FnFALx5V9HdZ4FvYz-pr3q0rZonXtVH3PPykRdyFVXV6Ovn1XbOkpTT5N7_Bovl2K6UrNe84SXs-syoqpK0yyYYcE4sP64fQYorryvO080kJjdWUVG-Bk_zycHLW369QrutIksp43U7BJL5bykf2aoZ1zfhkQ4WKrurXzq0ntmZUQ41eUoOyanhiCI9Q1Tgy1eLOjl3q8Wp7JYszDNEPKMkeBu58pKanxJ63RZ8L2s_Xzy2awF85mTh8P9lSau-5UdAfHKXsWfIvc1ql2Pw3q3mwj7sn-lGN5JQW8Gy-8W-96MBy52K9KqKPBb147y_Tr3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9o4MrcfA8WTJ7Ha8PBi-PTgBBjfCMXZYE0NAndfO3m9rpbJTOBCyZRh7JEjL8wqmnnUpvwVXlX5aOj58BtkkWQpuZwmGjOGgGNUEK80-8CjGDJIEx8kY0qwOUfjXSKFzrbm-UOyNMX8NMbuNy1JkRkxNtomqgBx51SwpilriIEkiv4lD6Uw8FV1hVRocTrVRKGGzvfjXavjcOaxnIy5ldY0wWPl_sCzMfCe_XD4fcJq-Xvbn1b1UPbmltH5F2_7Qie0K6QM6Mg-soRoqkRQ6CGxP5NqSKcwxGihT6vt2VvVkR62tvaccpkycqh5FxRPpuNDt8uQs0jMJxtrm9ICbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzdMqH-gdqYXVLWzQ85tIZ0Nrd3_yPXTu28O-8r7C9dvcTb9edh1xmwpR4jiPutyoP0FAJmPbNT2LNkgaQgz1WkoegH6qYoCVQykOWHEeThG4eFpM2s1Apxlszj7nqQNDY6ZhV9bkLfndp4fAKgQmtQBKOIiioJ-Q6XXnOWbzBGfjD1wAi6sEiqVt2iXp4gh-gIXYhGUCx81qZ_qnMjVtMoPunsSWQtJ_BOJWSzGi4gDZhKbSrIuzf8TfaUgUuJyJcsz2mxnKnZ8cv5WQZ0DVnwPoNHTnchsSIF7o2sUB9955j6RcIV-M6_P0KWS8x7BN3mp5ps54ryllExI34YZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU7nN5iUOATutG99GBafSTmwtJVwheHV786C8RwxxPCSOfInw4WEjZJXqyqgUORVQvfgJD3SCMcEdUbGQ8VN8Ri2wCB8LdGpYGOhv2kAORUXbAIRLlTA1XZ9y7c5tXttgojUM8tKafDopTZm5G6UKET5A-EGt39QDuOjyuxpqmA5BqmDKZZxES8xEL_ewT534-s33PIp6QiaNGXjA2qqS5Z-ju2ssXl4bQwstFOBqWtIkxkZRSlxsfYRtGyIg8e7frG0kq-Gh33GpJhSTQa-oEgSeZj0EMxTO86LJzJorX7lSC-jrUInI964008YrSKn60fCvIEo0aBr1mpkB6CgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5KofuTYWWYtD92vOkYyzLsUteukUB0jtg6ZFiiIdHaVxBUSNha6mv4ZSiTf_aIaMBLaxdn_yByoe0qsgsk0vbcXlwdF5n4q7-v7IfNmmCsfx59E2J7FZxUKeDYRxB1TvyIsZ8jy9rjjrns6enYJwx5d5L4KizZ8r5kS2zuMo-CnvzIQS1xUVVegSzINyNaLLAEtAK-29L0xLMzcxyvJunOt-2k09C7nHBMraNoqqjUBbRCMdDtImLdywXkwVn9-eEf8G539MSiCYWd1TM6LkFD0_ts1E_jZ1qSjMctL16ABNcIqKPr_D80AchCFNRukcFHFY81sqBzc-WiE-oKuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=gX59bt0ztNohK2IDL6rV7ZqKEtfM1jnjPI_39G5nOAbPA1gYWEMOKXvV465xaZ1bBrAtrD8MndK14qVhNqGPc2Kesi5LTT9Y5-pFvAAtpXMS-QyX2tLlmS3L_a9T_5mugi7TAeYYdgoT3leWlgfR17R1Sdmy3TCDccy-lKl9ph7frAgQz_TxxI0bgHNQJBSt-pERM8S5Ue2pzUBOS0BMwKJz92OiOnGgW1jhXf3uHQCg-fSdtOTor5wVtmcLkWHkuYAcnxIBnh3g9ulynKpybMJgB_RHgTI7QRG_NMxz5F0YZCWWAwWnVnwVibDt7D7IIk_gp68aqySWS_-YavQXzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=gX59bt0ztNohK2IDL6rV7ZqKEtfM1jnjPI_39G5nOAbPA1gYWEMOKXvV465xaZ1bBrAtrD8MndK14qVhNqGPc2Kesi5LTT9Y5-pFvAAtpXMS-QyX2tLlmS3L_a9T_5mugi7TAeYYdgoT3leWlgfR17R1Sdmy3TCDccy-lKl9ph7frAgQz_TxxI0bgHNQJBSt-pERM8S5Ue2pzUBOS0BMwKJz92OiOnGgW1jhXf3uHQCg-fSdtOTor5wVtmcLkWHkuYAcnxIBnh3g9ulynKpybMJgB_RHgTI7QRG_NMxz5F0YZCWWAwWnVnwVibDt7D7IIk_gp68aqySWS_-YavQXzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cJNV9iafV2jtcYX68I-y1OFrstT-0cI2s1HoQVwNZ_ec1czmM8_LTNOG8SG0l8n0P-f_3hASC4n2AxvDRAFwaRUL1WLasdkvdfFUzYTL9RnZ2E474v3RbAKJmg_6rW6ilzgAkCYNmMlRU_xZgGaM5fbop8hR30rxxjBEvBRmpDYikaNa9fSEJR8AX_i18U0JCqGLbMf8-KE6q-1A7aZx9cQ3rom05tjsQyx3UR0RjLmlT-pVokxkEchW0lkfpEF7ZiodO5G01nOkv9mxwtwHunW1OUDsqrg05rGncPns0zfscw-c_cUprcyD76jUOxULY3elinrdALjLpt2__Tn3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fZhdbMIBkziIMb02HhDcEr2FvA1qxVC9QaP6wxWoHBUmc9pueTZA9t9vLdRPVDT2Ms31HCF5mL9x2UBi9FEPGtnELtW3nlUpyXNPbfApVlwynotvNJ-U3uncCbwiJkRSwzP2R6NzsmZgGwm4ncGbuOBeC29w0e6z2jSzcu0rwgAmCT6RvrGPAqfvoCihDffH0mgNMPwHlBFmZ1QRyK97SAy_npxIuFuoUmngYdvHVlxS6EKCNIfato7H58S3hVGK20wkh89IKNAIYmlM630Zps0Gfa72gAf16SdQ_mg-T7wHxdF1AUNcCz3iY7FbFHTdv2LMwwPGuS8wW1U5TnzwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cWNXcAirzgM-AelEOM-QisIgiC3J0pBlgYtDqwgIdR3HQ13xJOiGl4pU4F8OtQqpWJbAchtIS6L_cFiuw-a1CstzRpZoGZFUg7qnoWPyZid8mbs2BtUsbpBrqUfK3gB_ypaczrt5YCh50AzOiELHZHasi0KyHcQlqCGKXlLyGTcG-tByOEhu3tD9ijhmLfP2rdJPMOoAIg4-GdYjlehHi0xjHAWuqEkxN3uIyk-j_umY8MzHHEIrmdfKVhPFPL7WKUz9tA_Ezs5fosGcMHd9eKhtGLWK519uW4dR9inDH8j_joyts3F5cUNMnlenOF_P7x0dN3t2fN8tBok73TFHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eAIekIZPrqHU96E5F8qyFBBA4-iOW25UZR3Qf_twGTWGXwLnxczurh-Voi70pxrXHR0Q3XtHdqwp_QxGH6gDBhCtZGRsfgQLjaniIRsLzC_AA6O9xXbuqBl7wVuYKT629kiLxSV187hG63xBjvO2pUThZiFK1F1CbP4fzW3M-rCj8SyZ5yYwWHraOtPi36JMNu2yt6O_6yhfB_yriZI6AYJ7sBrgHhltubI2FuW30Dh_FHalZW4mDkMOQl-5ZfclLlNq4AoHfMd7_UIOC-er5OljIVjNGEtXYjAOYSCYYmSQqvpW6iqC1YHr2EcujLFtLjBDpH-T6qaYGpQRDH8BaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJQkkQ7O-BwvFm3TyQn4dsgkYoQwxCvdwWNl4RsgxnoTTbCV0G6cHtfBdSwd17PM-dVgM2GSyW8XwdX-BEarZgJs56V4mg0fUoPuWvQiXdgG7w2pfbiCKxquxMa4BFXmzkndAh3y-5zpn8kMTWtijkUJEwFKZfGAxk3atWZ4CMAzK2F-EHNu5TYMYNfhIcVzBh1PtKd3BaFTQREyDcVBaLlesw0j8qhj6Iz5HBCWKBrX09kNar5P3eIR13zvWvzXAfwBF_PGIVfHH1iqgZ9CVNO0Cz6UYVCh0LQfu8kkKLMSFAun0rTOmj3i57sE59bb9qCGM0Ol5ambuN176dw_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHrAyvZYc6aQL9lKI6_X35xrD126DX1cyVaDERBX479efZ-wU276oQjBvGDeO8Eq8MoHsKqGK-4lOzR20lBwEqW2eU8zI-vbg8OkIOCsdC_Kjx7doikmoQMyhw6OGIq0NqA8CU3FkDaeVYFplq_chShDUKbJeD_JeCzOT0J2EJu1gOX_K29b-kG6MyOVK4tnR6uxPcLOR305fIBaZXkZ8P7RHHDaua8ZsvO3djqC7v85EkenaPr4Wa91iccodbbziGXp_YCWYOH6sbvYj5OtYLAaTrbYHe_3WMxDhEN2GPl50VYecjjTmvwJ7lWdY8bYXwyHAcBMl0JK-HhYO9X5Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui50bcTQWbtReLj6IU7PsocZcJINKzoXjkdbuDvudxuKdazo36p2Tk5e4OJ8kmefpbw4cSKnPzmeMLrZyY5jrI1VYe0YL340XdQlJbZNwylYnGszsBqXgEPNSoNGiuGPnJ2DJHPxvGYz8aoScjZ8f5U5GPqedhCzs32ivATkfg7FPtgP8uUliQzQGi6rxe8-hucyxpDLDijr7z9eoVO9bbDqaB_jO80eMLiRPkm0-BBTdu64NhH96JdJDS5gMGcHGIQgy3sM7fS77LCGw1PLHIx2aWkg7XUveGxCV4D0N3UDI-FMsEHzy6oSnrcJjEH_SSG7jEFrFuBn3gM1MRC9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwxgyLNA725lxq3ZYDAS74noqv8gJ2qvgWgNTP2OhVIXQSIn6m3eYeK5wNBo3R0XNu56olRNZsM5iUCf7S8VJaZesBzRIoUOPao689nGmjphWwoEI0XEhvAvxFn1XpyAkt_B3AIi_2oY7-PxfUbIC_d34h2z1dCdWfLSrdngQTNrsm2mck2EA3xKwg6EDH9Oj6oaYOMVxUY74BxvbNDD9l2Y0lpIECClVFYlVbVHbvcmttJDQuqjDLSZFmd63mALNEc5jhgLlGf5eyZyty919ZlnC6FZGgsV_G6vsd6FXxtNV3BlYAEXAGPyjIjPspaPwvWF_9-K3jFhV9yO8oETbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pU7LUaqEtZYYlH1P7eLlggH-CjqF2S1pkb3O8JyBNWx519P_jlQXHmGfxlmnSP-eW5Fnw0_sefhI1m96XCReNJOSNsib3vmRoytGwsh4A2ZX6sAdfe8QnOdYcYt9kfchu9dYAzyQKPQ22DzRSAiWQ_vr73Ldw2WlbCBqqFQELNhO1PqYnfKoeYTTwkAVnpq3PTPA-iU0kJFRC1TIXE5P8f3IbYfJ9egI7MECJhAakLe4-J7xC5jvtN_IWV4BhdCTeTybxwyJRKGa4b7y7PkTCh2ZUC89Zkoy1SIcvfeCg-OPPOp0wvXFu0IgWxjF3pgdCKwmRMfZQqeDirvtb2tjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONWmsGffi9f9XEYSTZl4uBYL29rqnn3ivF79EYCsZP7rACVi34a0e1XUzwWxcC-0_RxlOju8k3ioBfvIRXMSQkbbKGT_RYZx2DT5RiQrFnpcNEVeAxu4m_qn156daNmZAU3AupgdRSN8-iLKjgl7UfCm_JIDHmdrek9LZE_uCGSLUdCln2hEizdY_Bwl81lO62tcRKR9dlSL4A-bLmj0XOtsBihUA3UumGWuYvSfOx66-PwevqGzci7MiX3qUkDZgvt7Xx_afDn4pI-q_c5Fa_B16qC-Zfjv_Y4Pk0bxgLJATVNrIo6lx5o6fVj2cWTjXA3sJihoJW6z3r-gPruyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GevX2Q9UVCgZvz-XrjCMRUZtUtF2O6nC_-Gy72TRJXATKST0tgiSiXNPRgNNqZWrX-76wASQRHzT8-nj-JUe2EWOFR9F2cG_ieu2LtZD5iRR8_il7SdDY4KHQVKFJvv8kBaGaXf9RsAr9ySh0ZjTEa4P-gZokHphVJtyxaJEpC3-FelmZ4MYlnOvG2t4oknZg_BnMl57ms1a9a8ZX6QZMj_GEsDXhmcfLQv7oubthQDGgg9gDrfE7aA9LL-s6aS3a9kecaaN87z3x6Kq5ti4EXfes1wpoxuUSBluD6JzhIIXbIRyovySL0EM5rt7ohS9c4IizpM1a0coGI05ACSHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HN_hD3tQIsqnLxfBiB4bpU6RZvYcwN9RcRJ0ixNk_pGSuexRO9qwiaDkU008KIQlKCTztd_I4w43a3kN4OwVxS02hTVQoqmKak_6uh6gLFLfjMLRAISPJr61IPOsE2BeqvwjSO4TpzqNMNwmPnX5vQlciG_Fi5xdRz2HLi_6PGH1LKCGUv9owDHQMrCCa4nJzuEVKngsr_D-sEI20FnON7sl1jps4Z3pjiHbKHA--K-xKHQ2G9xpJy2LgTSG8DGPBVwYtFi4jGH3e9j0a1xa3JTPnW9MtR1lxosHNl55b2gcNAKnBhm-T91cY4FTBCXMpqdIcZiRXPQzd93qWgcigQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-fKEVpEh4M4lp1GEa53o-HnZOpc4TNNTpqBjwF7Op6LfQYxjz8jKFTWgEwJ_v6zvz72_cMHRf3UtYsOz8g7WLE1jFhvmsl1NgXBp9xY7lblBtgoRI9AdT-2Jtam7NrSH-fUEDem6lltAUHMf-jo0FVeTLOOtjx7Ch0e5ZzLOK4eOxztKOd1nUOOuum1-vSk2nYafPiVXn_s1ZqkaQzw-bQChfHAUMPIEF8XNs3PgiHTv_tGR5t8ITsbgyOcQNAnkKKrOqqMfpUuy0kIhTA5duLMIWXQ1shoz2Dmfwy3mLpIRiVxQ4aoyiJ90VQGa1hoPqaixS6vrxDc3hegfYCZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vias7ZErHVgI1FJXV0VOTopUXmAbMwpMtj-vVGUrVYzsu_OF04rt-mAJ9hF66_FX9jDzSd9Nhazw-pkJdhC1KYkJrerMtQt0BV5TNbIGIj0jZvGFVCPIQIdFKVJjQTR0S8bmKq8YhZ-mDSqB1HzPLBVkcssDTAn4vR2A-yMuyF_qNk0fzo_CM7JofodkgRly09NAgyeGPqGhMc7_WFFNBiyAQtN6SFkg05HRRxhVEHCXpM4DpMhtKNdgY2GQkwogyZk3PihGaR-H6JuSbQRNv6kCcmId-Ko-XiIgIghU4hS4ZF3afnV-LhbqPLFabB9KyqyuMIwTR5p0cMUXPeFeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=FF5qEFFi1OidPBBvztOnYZrW6Dx0zokhnUYccQHDIAyCz7fQ3Ye1pI7E5fB8l6DxR7L7cHcnAaDLFzO76zsKwO4X4ekop227RvpZt049ZOP89RNtP6ibJnFcD08ZYyvyTyUrZRfuG_ulCcAFk9cjC9GYdJ8QCK9pCZcGwdMv09Hyg3V_6UiWnueq97b8eUxgDWJSb7zGjmg7I3trUaU2ir1EHU_snTKe_HY0OcihPGfmXxoyNqlG614bxBmcnBtUBK3A0AQMUAu1RrvrDO03z8p3Z2DaesyfIzm7R2-GUvl6HyGGSi4gioEg0OSL7YWF1T_iiwnNZrQ8PUXb9OD3iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=FF5qEFFi1OidPBBvztOnYZrW6Dx0zokhnUYccQHDIAyCz7fQ3Ye1pI7E5fB8l6DxR7L7cHcnAaDLFzO76zsKwO4X4ekop227RvpZt049ZOP89RNtP6ibJnFcD08ZYyvyTyUrZRfuG_ulCcAFk9cjC9GYdJ8QCK9pCZcGwdMv09Hyg3V_6UiWnueq97b8eUxgDWJSb7zGjmg7I3trUaU2ir1EHU_snTKe_HY0OcihPGfmXxoyNqlG614bxBmcnBtUBK3A0AQMUAu1RrvrDO03z8p3Z2DaesyfIzm7R2-GUvl6HyGGSi4gioEg0OSL7YWF1T_iiwnNZrQ8PUXb9OD3iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fz-wa6FFY7ZunyHKT_3wBqpRJ3NY_CT3L1eOn_roWiSqN8NraN0tuy6TA_VaJhi36l8o7BXEZGio1auVZXvOm3LHsoJ1_9N0hzicfbrMi7PfJfe2jlBHBNwQMJkIPSZ70iz-XJ7u14ZbT5vjBcGChjX7t40pVhHYlRLRjFFu6mSIAJmVO82bTh8ZBa2eJ22vJuD14oTRXAkWV-tUYcvnoA9-7WcwRbMkdSKxiTDgfrlcQ_TDqZ_ZMXaf3rysulzllOITrjG0O6I6fYcc7WbINBTcb8umEAk7AJA1Q2Ed4MIcc0--WUtw7acrpTAMlmPrEpLUlDG0egw4MycgOTZcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGQm2KXmq84-1ILinPCVBVFOG4lX0Rz1nNUb5S_2Ol9us15bjlqge8rJC4lg8vqiiKQ5biXPFZhYqiBspkK4bcBLzOSL9e5giq1-NIQY8-jc98i68f5IDQOo7GkHSOkuYdS0xNKqlcicQO2Rox6O8nhcejTsopIqo3cjuNyIpjDfs2CBDRxbT22xEyNroARI1dIYuESKRkEjuhJvIjzbGi6RQE_HHbo2lgoif0RxRLv18o30JroCxJbn7wErhQRdNfIXUU_EKtGLI4vwQT9bpXyWQVSc6SxdwC1XWBezBy__C1GhTHKbq2WYzBmdjP7T2PhZzUPb03Sc8A6Idxe-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8qEo6kS7D0usxB10obj3tGsnGlxQENtDN16lY31oywOhQfN0WGpq2nKSgUcaUCXjWr-Ur70Y9UNrqXVDb2VaOKeQPXMC6mea81hT8EnFt2YMTAvYZTUXAcr2zc9Bzda1XV4dwHzmGBGvaj2YDT2ZOYmrFYy_qDMsa_LqWorFS-xAMHmcjcvEDo7HFFBNqhNqDalPCxpOajcFKlnZ5bPVjQSrcULkH_6aVxn_vUUyISCZ-qgNIcnrMv_vdbw4VMKyg4Q_s11VOOFefRrUF1P54KG-mK-R-OG_M4ncXJDJIDTeIhVhy0mTU9m4tXDqq_R8kS-T8mMP5gHcFbrgcvECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPTOAQ8SILw47-FJd_uNATE_oqgJG-SJUl8jYC0q2b8Fqi2EW5CDRNvKIzLqp2orVXfniA9Gtwmj4y-DNniCopfy80fy0huO7LSo7s49QzJs08pfsVB7LDx02_QQUbcrohWhcRibAeG4utTpV1oJqBrsGiaSP8yG1OgQl7VmZY6j9mrg2RPH4nWqGBcA0J42ynp7Hf1ntYofkLVD00cPyaCMnND8gUGzUVI-hl9g51IEZeWIb1TSyDkg60bfz9ov1zrj86f9rrqA_TETQIb0_LHzZg5INbz-yUGYvsb14UoaaTt4RngKlMHvjb3zhBdEYK9b58Qn1MSHxatM66iaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=qwmzkjtYVZBu7y0jW7lrhBkpe8IqIC4B9ZvJU49K6D5qz4rm-povLtE6rJ74I0MHNKZInm0XbEa1a57E7CPn5hgwhBu2NEEWa6bNl9sPJXVZoXglFLkCHIo5FbQX_OqnG4wWVeUctOIn63lVtK1Em_cddJx0oIBMFqddwLRPNTJ_8SK9KnCNPohKjBIkC1hY847hIwmaikza4Pos7KVnBtXvrpUXoBeXavVLBQF84AoEyHD1CMaIllp-aKvWotJh4XOMSmjaZclGfY5ZZsHE58_GtKWLzYOwGH9AV5pnBvYAKOooJWQpL03_Jw0s5TC9z0Fbzh97niMxa_X1ST87QA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=qwmzkjtYVZBu7y0jW7lrhBkpe8IqIC4B9ZvJU49K6D5qz4rm-povLtE6rJ74I0MHNKZInm0XbEa1a57E7CPn5hgwhBu2NEEWa6bNl9sPJXVZoXglFLkCHIo5FbQX_OqnG4wWVeUctOIn63lVtK1Em_cddJx0oIBMFqddwLRPNTJ_8SK9KnCNPohKjBIkC1hY847hIwmaikza4Pos7KVnBtXvrpUXoBeXavVLBQF84AoEyHD1CMaIllp-aKvWotJh4XOMSmjaZclGfY5ZZsHE58_GtKWLzYOwGH9AV5pnBvYAKOooJWQpL03_Jw0s5TC9z0Fbzh97niMxa_X1ST87QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-ZJxbeUAvcRjSPYwMDSBz0-vT9Pox2eP5raF4AHRwdG53zduO98aKBBKRrA6MtMBqnEKdI5SDqhgHCOg0BdWCZX84QBFVFfRsQpSlk_o1wdHfcBepnqOzBuLJ5J53-dwjGPXwnzNefpEl5BEBEtfFc1x0NoGKwKwP3pYeG6MO5GSmj6Jm18d4v5sEWFsiI-mvDqcFNa7_h8YqQ9Bq7PRncP18gZYhH6nfQBU-MXvD3LTKnxgw7JLU6yYNuFZfVp9yjySMhRxqk1pAG3rvTA_t2KpHGY0HkyudcOV4KXha4ymmKbUGmVaJ1GXdWY63LVHBDH3LOTuqfvOEBSqO9Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nMsyg1TqpXrlT6zc189yT0oUUABw2LFDiVNKH3kg3ehS6i7PkbTpzdytr_-QoSNeGO46yRNMSx8Ys1gQKI43Ht-1i1opyG2B4vHkZaXXfmBr8vKbwzBvhArg7fRwMD5lDlZlZsbU6Q-msd5v5pGyBUgbr97H-4jfc6Q1M7Z9rygKPYBO3WMcoUnYhatlAShRv6TbXE4GSrs48a9f3XjeBdd6GkNPaRjCkRZBIuX6rVEqGhaqxemaOi0nYZ5U_xOYrlGtrawBf8da4390LBYASj4eeDWqF82aWxc4Pfn3JON24miNoqht17hNEfiRmQ91-oIKbghvDjCOGJ2kuzeu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=VaTzk13h5FZQTZMjUXS4tiuFmgdzmhxUOYD3LlWALwDrV7RAK1c8a-67ml--zpqL0nt0oRRrt5KCa0jQqgVXiCsg4T-kFt87FbnrtnqHunrJurHV5GNrYw4VRXnOSJufnRcoKcQaqNa6zSXgp1K8NO62_ius4eCYTgyDuwfxUcBtp3qB2-KXtMdtuwuldpbhmk6r9uDgSoW5Rc8pr69ckZJ_EkLJ8LKDLlU44CB5ccsZhR0tyWx9JXjzmWSyQ9KDzYorj3fOowTSIegUU_lRhmcVs5h2pHykiPN8GGUgWly35xyqX8v0PSG3pRahib5122BieAebQ0eVxGa68zVX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=VaTzk13h5FZQTZMjUXS4tiuFmgdzmhxUOYD3LlWALwDrV7RAK1c8a-67ml--zpqL0nt0oRRrt5KCa0jQqgVXiCsg4T-kFt87FbnrtnqHunrJurHV5GNrYw4VRXnOSJufnRcoKcQaqNa6zSXgp1K8NO62_ius4eCYTgyDuwfxUcBtp3qB2-KXtMdtuwuldpbhmk6r9uDgSoW5Rc8pr69ckZJ_EkLJ8LKDLlU44CB5ccsZhR0tyWx9JXjzmWSyQ9KDzYorj3fOowTSIegUU_lRhmcVs5h2pHykiPN8GGUgWly35xyqX8v0PSG3pRahib5122BieAebQ0eVxGa68zVX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5Z1Aie1Rr5z98HsDSvExvZ9aE3Jdip8OYFKcjfALKS4xYsOXy5dsdOpRq-agc6CBj0uTkglwehE4ZttNFjuA3SjH27LIxWtKbaCdsKX8mAMPSFrxI9WCEsXOtph2ZXWfLmIzCgk4KLDDkDJp0BQuAeQj9WCaxU60L2qKQVLfmMC8y0GY7YcRk_WGixzB5ZRu2g3eHsEKiEFpkIZHdobAUDtIbrgMXlsoM-hzBw-ThD8NZMZYguChMpM_zfILCZE3aTlRcisV2N9Y8cFgAHLOddgh0JBrMnvto7UZHH4hCj_q6RL88ze_hyM99ktyxUtoQga7bo7idY9RXFSpoPd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-0oYyNiVWcXFnmg4y141uexnNivtosiixMiWrpMGwAx9liXVILdCOBYNCueYDvKSVI6_h6S4zoeHV5lqcHqicgmkB3RxfiDqW1oVCDsQhFdayipfjsTp3ma8KbnK5-p4x1AqGIdotTEQ9Br24p_uOGLack-6EDKs_D3QpQQO8FiKVxzaLUjGxmHUltqXopCjRmZaDgNSmXSkbsAHHBg23U5lwRBXW80CqJIWQNLSfffm4rh_Jukt5PA00Hb0dsi4-3LaAlozehzN8xOVIEVhIigt74Lcx8oEFhLkocuLMCA9s98x7BkJd05_Zx1a24t01g_OQrG_Mbq65FEVxi6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDtyoOMZDZoF87EEaFSDmZ_n0Xtn5CpsWwjMrpZFXjKTwrSmhPIgQ4KonO-2X_17IhCsO-fD6bZsNrqmVPuqLyatEQEdkA_b0ybTtXYEHqdaYzqIH6o2adKKMA9HjIeQDBv6QTyAEI4EzqgwZwIGhKsGH_DK31bGzmc5GT1XnOQDMH14PCOZhQaTh7NcowpNWeYTO3EZPThj9f07uS0Wh3TGssfxC8lqbCGq3DVYZxZe_Spq8VNpj09Be0M7qVZFCpIRJoq8mG1SyFsqT7m4BaV-DgDyTOIC8Es33wMZljF94JpNM5N-DsW1HkSBZRPl_IG6UArqL_2D3qxw4dzgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOzqkbZCIrXMdv1WsgddS-YIrXxOzWZ3YBF7rzuant380rcGup3qnYwWeu3v-bJcBD2YhcZkasqIgmxE5eKYrk1-gwTu8_awkAaFMv28pmHCmEAvGYTcvKs5UX_lo_IM5eRU1N9yK86IPduCUdDAW4qZovJXgBg6gJ8mbeaekS1nfHyWLrkBdD_cdbS79IPkDw4HkaS7Kat0q4gskV1quIMalU-WHvwAoyxVn3uFUGsHb49oYm8qHtkyr4HF8RtDS_c0qH5Zo8VVGiYuQIiSWmre2hz97xlXup5qduUjDM2LmMtn1AsGzbKsENFvminGfqPPHs8s9RJvwxUmPg54vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNWOhdA77DW6JuptDPHdsNGEEhBsIprSY1cYlm5YEvhn9pVU_FGluYJxYqWlB6E-Z00vxlQL2AFjwW_cyVFJcQVSMBePL_15qC2kaLTa0RhRSLwg0MgT6UhcHEs1rhI-L7SjMHp2lplR-RCAnPvkWJHvP68NMMW9r9pElHfRJ6mA_4ZGlvCOJ8shyCDD_xIfaZH9nxWvQVpcjydfiMkFcg4O33saefCSqmPGzaez2ev3jEyUHsVpwqSvtWief3EAjed75xxgd40NUoEBa6VkSwdlnNUXAV9M_m9qRdtfohjHE3PsSiocdSRypJiZb7-uvcLeO5uF6a-AfNuh0wOigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=NPYwuzj49YFUd_f4ymXR9a8XZX90j6cMBjiIYbGRxyQbcvoDiQQpYImDpT7NYCiFTuhFHMDbLtTHFfbPI-Yyo4Ka3UfLZpv0TQXZyzmvjUjej5Rr-XTRTs_7x492mGflRae7HDD_uowTDkXZ6eB0u-kerlzG3CBSQMTpg0CMV5pUU8zHlpvQFqHHBYx28qxLMSLLt6ejP-sEYjyb6JbVZRron8W2oG0xpiUjX6DkHlValqxfcoM7RtD_C50aKlGY6OTToWwLwDg-covASl8JpmHjpg6DRDc2K3vAr2iIPqgQf_hL-IpNtbDcK_zeaZIxZ7ucGAkpgicGsVoFTGrj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=NPYwuzj49YFUd_f4ymXR9a8XZX90j6cMBjiIYbGRxyQbcvoDiQQpYImDpT7NYCiFTuhFHMDbLtTHFfbPI-Yyo4Ka3UfLZpv0TQXZyzmvjUjej5Rr-XTRTs_7x492mGflRae7HDD_uowTDkXZ6eB0u-kerlzG3CBSQMTpg0CMV5pUU8zHlpvQFqHHBYx28qxLMSLLt6ejP-sEYjyb6JbVZRron8W2oG0xpiUjX6DkHlValqxfcoM7RtD_C50aKlGY6OTToWwLwDg-covASl8JpmHjpg6DRDc2K3vAr2iIPqgQf_hL-IpNtbDcK_zeaZIxZ7ucGAkpgicGsVoFTGrj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=ttCbsW8J5Gj3hgBAo12b5Fr5TxF7M1UJ8etpXv1DLCSYJRrzco5YsS-Y-xKdyOdrnjnNJyfUeDR1HuOCKjTNQpa2VMulnHWsN5uyoQjld-SBW4WWrm9nGN7leCi3VKKMln4Yfjq9sbst4FrFo2S7eiETEn2PLph4DJWeLj_L-QUGYhRUySAqEaIkERPeCf9ifTZDW5zgo0yRxhef9ijAnWicZlQ2AWfIULL62NiK28i0j_J8uZDfpACrsrTJBwowSQ1Bp0TVRQtgv5FqxPDd_u1Kml17gEJBaVzOLMD83B27kBah6sDAE_aStwzigzmtRbg5eX5YTG7iVme50lZF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=ttCbsW8J5Gj3hgBAo12b5Fr5TxF7M1UJ8etpXv1DLCSYJRrzco5YsS-Y-xKdyOdrnjnNJyfUeDR1HuOCKjTNQpa2VMulnHWsN5uyoQjld-SBW4WWrm9nGN7leCi3VKKMln4Yfjq9sbst4FrFo2S7eiETEn2PLph4DJWeLj_L-QUGYhRUySAqEaIkERPeCf9ifTZDW5zgo0yRxhef9ijAnWicZlQ2AWfIULL62NiK28i0j_J8uZDfpACrsrTJBwowSQ1Bp0TVRQtgv5FqxPDd_u1Kml17gEJBaVzOLMD83B27kBah6sDAE_aStwzigzmtRbg5eX5YTG7iVme50lZF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
