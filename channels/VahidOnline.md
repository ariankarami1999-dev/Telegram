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
<img src="https://cdn1.telesco.pe/file/VzEF1Xud9r6HS30Ooi4Ui70K7aEFoMFvgrcix-ownm5PgJgVYXd1RsOBdg1X2wLFPzzjYAGERhnRYPL01yamPLd8NGLj8c2ca_T2YvmIPgEacevWuq_pAGO1I1ryhLw1Ecuo5Sga2ndM7JQIA3cuy4ReRNAqmRCDHhp4TnhWkv-yBsh4JJ-EuJ5VMDD8zxqQ7TN8qCryYr2R29rKxnsVs7qjDN4Tr82kxT3RPY_KcWxV_DTxOGVtBfKqfAv7t1xbZ5joQGv60qNNz1OU-rIwUSf2B3W2wg-HftQ9IOL86FigL9uJe4-LUkG0tDHln3Pl8NNjh5etkHTUuObJyHMr1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 12:01:29</div>
<hr>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=QBRyFEMAB7lUF_LdpNJbfz_qfV9v_Kmp3yZMh8ZnmZnMAzwuJLz66H0IR2mRJ_IisuwlTwUmqkdc2EJxUN7nQhH1s2qjJ7_KycpUxc-zhJGWgRwBIykCYk5HV6K8Pi2TI1VxYPKFMQX3haI5gGOnhvdfVeJd67xnHKaedeLd3kTcyImjs8nh1hULLvTbQ_IyqTqY1z2uHnfBlJmzrnPWQgqt9C9ikZD222jED5EhaXWKvK5IdQeDKHLv3y0Uytibq3rYeliMakjR_FnlewXb9q_xlBX0zfQabMywgSfbvTW1Selm-vlEZHETu6cMqfC4TLYKELM6uRHkpA46-l4oUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=QBRyFEMAB7lUF_LdpNJbfz_qfV9v_Kmp3yZMh8ZnmZnMAzwuJLz66H0IR2mRJ_IisuwlTwUmqkdc2EJxUN7nQhH1s2qjJ7_KycpUxc-zhJGWgRwBIykCYk5HV6K8Pi2TI1VxYPKFMQX3haI5gGOnhvdfVeJd67xnHKaedeLd3kTcyImjs8nh1hULLvTbQ_IyqTqY1z2uHnfBlJmzrnPWQgqt9C9ikZD222jED5EhaXWKvK5IdQeDKHLv3y0Uytibq3rYeliMakjR_FnlewXb9q_xlBX0zfQabMywgSfbvTW1Selm-vlEZHETu6cMqfC4TLYKELM6uRHkpA46-l4oUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا با فاکس‌نیوز، بخش مربوط به ایران با تشخیص و ترجمه ماشین:
🔻
ونس: ... ما با ایرانی‌ها در حال گفت‌وگو هستیم.
تلاش می‌کنیم میزان نفت و گازی را که از تنگه هرمز عبور می‌کند به حداکثر برسانیم. در حال حاضر بیش از هر چیز روی همین متمرکز هستیم. فکر می‌کنم می‌بینید که قیمت نفت امروز به حدود ۸۰ دلار در هر بشکه کاهش یافته و گاهی کمی پایین‌تر هم می‌رود.
بنابراین فقط تلاش می‌کنیم مطمئن شویم آنچه را که از این درگیری نیاز داریم به دست می‌آوریم.
اگر به عقب برگردید و به یاد بیاورید که اینجا چه کرده‌ایم، برنامه هسته‌ای آن‌ها را نابود کرده‌ایم، نیروی نظامی متعارفشان را نابود کرده‌ایم و آنچه را می‌توان توانمندی‌های نظامی نامتقارنشان نامید، به‌شدت کاهش داده‌ایم.
و اکنون می‌خواهیم ببینیم آیا حاضرند آن نوع تغییرات بلندمدتی را انجام دهند که برای داشتن رابطه‌ای بهتر با ایالات متحده ضروری است یا نه. اگر هم حاضر نباشند، اشکالی ندارد.
ما همچنان هر فشاری را که بتوانیم وارد می‌کنیم و تلاش می‌کنیم تا جای ممکن نفت و گاز بیشتری از خاورمیانه به جریان بیندازیم تا آمریکایی‌ها بتوانند از قیمت پایین‌تر بنزین و انرژی بهره‌مند شوند.
این همان موازنه ظریفی است که باید برقرار کنیم.
آخرین چیزی که در این باره می‌گویم، کیلی، این است که همیشه سعی می‌کنم به مردم یادآوری کنم که واقعاً هنوز وسط بازی هستیم. این ماجرا تمام نشده است. دیگر در ابتدای کار هم نیستیم؛ وسط بازی هستیم و مجموعه‌ای کامل از ابزارها—دیپلماتیک، اقتصادی و نظامی—را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.
کاملاً مطمئنم که به آن نقطه خواهیم رسید، اما هنوز تا حدی وسط بازی هستیم.
🔺
کیلی مک‌اننی:
ایرانی‌ها هم از راه‌های مختلف این پیام را داده‌اند که می‌خواهند کنترل خود را بر تنگه هرمز محکم‌تر کنند. بنابراین در یک توافق فرضی، وضعیت قابل قبول در تنگه هرمز چه خواهد بود؟
🔻
جی‌دی ونس:
انتظار ما این است که همان میزان نفت و گازی که پیش از آغاز این درگیری از خلیج [فارس] خارج می‌شد، دوباره از آن خارج شود.
ایرانی‌ها به ما گفته‌اند که قرار است همین کار را انجام دهند. کل ائتلاف کشورهای خلیج [فارس] نیز همین را می‌خواهد.
اما می‌دانید، ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف مردم نگاه نمی‌کنیم، به عملشان نگاه می‌کنیم.
می‌بینید که برخی افراد در داخل ساختار ایران درباره گرفتن عوارض صحبت می‌کنند. ایرانی‌ها به ما گفته‌اند هیچ برنامه‌ای برای گرفتن عوارض از عبور و مرور در تنگه هرمز ندارند. اما باز هم خواهیم دید در عمل چه اتفاقی می‌افتد.
آنچه طی حدود یک هفته گذشته در جریان بوده این است که ایرانی‌ها و کشورهای خلیج [فارس]، به‌ویژه عمان، درباره چگونگی تضمین عبور و مرور امن گفت‌وگو کرده‌اند.
البته یک مشکل این است که ایرانی‌ها در آغاز جنگ تعداد زیادی مین کار گذاشتند. بنابراین آنچه اکنون واقعاً داریم روی آن کار می‌کنیم این است که چگونه می‌توان سازوکاری برای تردد ایجاد کرد تا کشتی‌هایی که عبور می‌کنند بتوانند با ایمنی عبور کنند.
این طبعاً شامل مین‌روبی هم می‌شود. همچنین شامل تعهد ایران می‌شود که به کشتی‌های تجاری شلیک نکند.
آن‌ها به‌شدت آسیب دیده‌اند. می‌خواهند این ماجرا تمام شود.
سؤال این است که آیا قادرند—آیا نظامشان قادر است—چیزهایی را که لازم است ارائه کند تا ما راضی باشیم و احساس کنیم آنچه را از این رویارویی نیاز داشتیم به دست آورده‌ایم.
این هنوز مشخص نشده است، اما فکر می‌کنم طی چند روز گذشته مقداری پیشرفت کرده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7BA1n_f-D5LC9xE4WhaL5pSsVpkgZLqK8duwATYzT531Pt8EpKDl2DSZdeCD5ASRKB-JdJKsbjhrTz_N_sHgc6YsOijBm9EOZ9Mid83TdATJQhPLEck7NkVI54HH1hh2khGo8MNT7Pxax8hCF0r0fALnxhacNLWaO_gYGr7UXLUejJ2v_L-yFGvx_pRwY8o3NxYgLi4mWHthIoBB_p29OFw_wvrrs6ECtexXMhmLLLIlSX5EjoudeVOZ8kHqRNd5JqtZlFizFeLWNziSiaSfJP2OrMX3N9HVoOHEJcsMnxBQZyUavkaM3UfowdU1rSTu4nb0t9utS_GScVQCJtpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6M_fMkZY56pWF-jkn_nNgw8Mx8zr_B_kgchtaEgpOAx09F0EUP9EpsjMpUJJds1AT6qu6LGwKkAIRnPF7NJNIDHJrsazTHUP9pY9ZH6Dikk_c0dOvh-GI2doOLlYZSHigEXnVHW4EVxXIcXvm8uw81Y8GV7XVTsHzRLTI1zaA_KWGaYCsUInOWYrFEwNOpnxjd84rHI5fRbBSo5A4SYfAKejVR2b53lGWVHrpewjjmZ_0wQl7KLsTEkahz0Eh11VAlbN_fwYT0Aa06CLR-CmX8L5_pBshX10rhW3x1wBgko5iKMWCWpwvFuXp6lqibZaEi_m80VNAUePEzwX-YBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1QYLV7vpMyZZEKYLAowHd4jEEII2YG_ztRS6WTwKPQ86E43cUscxQaQn8eOpZby_HMamu6v3RXGjan_-1WRoLHyRXIghIbiJMWPI1TeTpYonGvgvCCn0DjKDH4wNEfmWO4q92nJFeiJEWurz6JPvk_AwwWHwImmXVOytYxidIlF7-jnb480TWds4L83mGnBzuASMx21LZTimuFLKXK7nzXExy0g2080ycIMsgymLH1JImUNX9cBpCEU50ksB-JRyI-yFyT6FpOTJwg0m4nTvFsr93IIYsjiVFlCrvi_qZHElW4S4wWjDKKENnyNaQOupcMqpBFJB4vhVl4g9v8Deg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که مسعود پزشکیان، رئیس‌جمهور ایران، با استعفای محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkzIcngkCaLzUgss8ifINT6PJWP7o50jYdwTmHYsSzs7Ui8nE-uJvDb5AMeOLXVoIafx8eE7W11XqY0G1cavHrmgmGvnBFxQkPhIjWPpd4tT3OYGqNr9cWg7TjsXlxHPc01X_lhq-nfngadTMHmFmERMQfqYCTbeUoq3zfuWXIxiZKtIj8VRBVR2AhX5VLWqKLDp-afxncP8UE3x-Y3YqT0ekSiISzcOdMu8hL8v39i4x-7PPPA5XyL0IaH3H4z40asYfQA2iwzqJLTlDwTJG9Waz4TRiuUaFeRwckOIzlvkrag-pakqNt9Y2r5_BLQ5TvhESXiJh885Ltxja2jUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kjk_DtcNswGf6wxf7dsv9-8tGXMGhpf7t6BviOoAvSuPwrG1iEhODvP-80uM05SClfKeaGHNrhl3SBvLuJNdLAxnJEh8tl2jmf5GM7FSuIxzZ-mT7ONl30NI0vGglwdx8XqWUNF6IpOs4ouBoBKOtZwBtboMZlAUv9nCUdKbWWbbIgrSDEo_HDkvQUg6H3UDKQ79x-D3V57hdzrB6V74OI03M9dXVT53UZyIh4ctvcsRhXYx45ErMKzJX0l_7yd2Qca-X6gfj03QAG7tJ0pP398QxJgfoGHQKJnZSh8LEHqzXWWzpMdsleVArRSIYMGoa3cAq2Xwbh6l79zxOfTkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlBEk9_zUcjVlIz_sv4E9m3S-CYlLNzK5nzZ8d1xZsnWz5sIA44l4Pjvj6-_oSZm-RLvdP2yEm2xgBVS7LXhx16zlN14xbf-eqlSL72AYDwW2YIARe74lfUKLrIAammmop89peO9fnBtZApP3d0WB8-mPFikw13tIMop74Lb9886pqYHO3z5OVL9foibTR0OUFO7Ev94T-RLXr-BMaaztZ5xCrS01-Gc8GpTf2SzQvEgcuQlDoPDIAKf-F4xCD1gQcnUrrqWyV2NE1ou4i8iavjSsioOiec0ihb6VWIedLNXbrja5YsawjXyWuxXyiu_yalnTSom8h92oMJWko0qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgT3SMVgbjqrPqqzo7bfiopylaoIK6k3-6rymAhyug8cJi3_FC4cpmHnJUTcaziD-Aom-di97xRslQuAH6PY_gQsNBVbJm-loIEO_YmvudVjB1aM4Cc-VzGqTpaS8YAj5IY41lRa3qEATxiyoQpEPSPr6VsocIljaGO6jpEQFj2MoXnWLfW5Jpp-KnIBWx98WDNL9_nz9MonqVDvrETjTgNaUfbA2S0p1dvGIeDXKJbI7LpGJjTWLhJ2F_dSRgE9NrPIazw12Kmk_umcECqa76rFp3-z_ceCFnFn3IOvbqW81Wpc8IhCYmpy_HQS7TIDoZmcCyqZbFgGQv-tfNVNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLQVLKY-w48ZE2VDG3MbVFIH_v12CCF0uQpa2iWvJNL6zenTqNxgYiEWYHXpXmwyB2MWej8LUnkF5DFnORcyyBxmq9EjMxq0KJDqk-euT9L0So9J-TV-38rR1hUvcmMwefds1UoIQRgU17ITGJGkf6wZbfeWdrNUbEd8lWIPx463eF_b2FWf_TTB2H-0XSCRSIlp14g0hlvewKij_0qoeObTV6Me5S-xfkUwSm2X0R3XQH26JwM4U7F8G947CM8vFQTpFboMIulfL9Hz_TpLglWS6T5X_aG8gkXBVtyzXxMVpaXstsabFz0qyJg8BSv0QGApbU1Toklx_AmfMOx5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvJ4vEX9_vys1BEppnRsDwIJS6gah7AnDFk5BzFHzEyzS219jIth75nAypgboKQdScmpFUxC7NAdveibvQZL2lMQkLa2PBjCDig1zntxkRmBU0IajiXlVUxKTGWgsre5sHT5biddo8C1LzFk0NnquJmdxFPK9650nnPubpsrNxxQr-r6yEcS5NU3dkgVpBboQ7HpnbUleNl8TRdTlUFQmml5rogRIigZ2-S_zNq_tR6CnaN1eOmtuoohIKZDxaPJs3XV2HreN6t0reHCdUBmfc5BIPBb9eImliJEbSV3UdXNxPRNj2zgRywA6IKiObSUSSrWkmvFENPTo5lngE9ieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqOrpxQwd8y5j_NQ85bOQG8JIyg7NA_SfalJLyAuKE_JPrMPxx434DYwpwx8A86OE1YmpJv0_yjNOphbbt8fAJBUkRlRRpv0H9r9-yVn2Q3Q8IstT0y-Y1_T8BRSaJ85063ytbzz3JKVsgT4_ObrQOHIqq5ZjEszo7sXKkk277zFcVmXyS8NOhsUrFGEvVe51XON6vePGbf_zLY2dYJBPD5_gslJZvJqKzXmz9EA7y41bkmibKPkVzmSKFQXPqKGTdFPgQFLO68SCs5ZzjKpTpn5OS32DtM3R3OBwq747jkEUSs74ViuoUOeJ2NKzDVXYo7JjXKgYfR7NEwvKo8uNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQgTYP_nGOBZJ99jgqGc2pdJGPJ70MPRLmKI7WS4ItMgMwszBxilTSSIOl7TsnpXP1UHITsVKqgPN-QkAZLuqt1OzEXVWMwTS_mwaJlIw4rEti60eDElQEy1HMI1cNR7I9X7s-9l85DNMWIcGBatRw2p3Ug7b7NvJvQqAftjLYHJRZlhhRZOvbRfN-p31yT1Chgt54IxbsoRQVJ8RZ_77ZOLn9jqLYlVFu0Y4aZIfSHCgw4ri-1KhHn6fpgorRLFKvuMcobo93Njw91prqR7SAF7xb6VHcacLyDKYeI-IspjUqSPResoIxbCQMFJUNjaBgzeVIEJtn97lFeV166_Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی
قوه قضاییه روز شنبه اعلام کرد محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در پی اظهارات اخیرش به دادگاه ویژه روحانیت احضار شده و تحت تعقیب کیفری قرار گرفته است.
به گفته سخنگوی قوه قضاییه، با توجه به روحانی‌بودن محمدباقر خرازی، رسیدگی به اتهامات احتمالی او در صلاحیت دادگاه ویژه روحانیت است. او همچنین گفت خرازی «می‌تواند اتهامات متعدد امنیتی» داشته باشد و در صورت حاضر نشدن در دادگاه، برای او حکم جلب صادر خواهد شد.
@
VahidHeadline
در حاشیه ساختار قدرت در جمهوری اسلامی، همواره ردی از «خودی‌های دردسرسازی» پیدا می‌شود که مقام و جایگاه رسمی ندارند، اما آن‌قدر به حلقه‌های قدرت نزدیک‌اند که نمی‌توان حرف‌هایشان را نادیده گرفت.
نسبت خانوادگی، لباس روحانیت یا وابستگی به یک تشکل حتی کم‌نام‌ونشان، به آن‌ها امکان می‌دهد از تصمیم‌های پشت پرده خبر بدهند، مقام‌های حکومتی را متهم یا تهدید کنند و سخنانی بگویند که واکنش و تکذیب بالاترین سطوح قدرت را برانگیزد، اما خود در حاشیه امن قدرت باقی بمانند و پس از مدتی با ادعایی تازه برگردند.
محمدباقر خرازی بسیاری از این ویژگی‌ها را دارد.
روحانی بدون منصب حکومتی، دبیرکل تشکلی به نام «حزب‌الله ایران» که وزن و جایگاه واقعی آن در فضای سیاست ایران چندان روشن نیست، و عضوی از خانواده‌ای که با حوزه علمیه، دستگاه دیپلماسی و خاندان خامنه‌ای پیوند دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu6CQqRWkrlxdxUGeGJUoo43WlBvW5YlLerQFkuJTy8HtkUk2xBp6dtUFmLWsP6CUFfJ4EM15SyY0pdDkX_7TbfqygAPaFS6PTFol1lZCklCrO0K1ZBBfFkbHPzXQs_rXwjUO2reBROFEikMPYncy1yIgR-50r62IfeE4JQSlIwxgC9a_GeVNDthvML7x32a6vsvLlYdPRoTFN_kx-0hQLY5rqAgHEdd7V_56utfe3xnS0M-0bkOeaoKTb7VOvhnhNKf24K5_WcnFbeJGL14s3AgRnW4pmyL5S-m_lsy68R1kelS22ddMwVIMEER0vXWar26VDxm-Tq3lPrGANmXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم روز شنبه ۱۷ مرداد از ربایش و قتل حمیدرضا رجب‌زاده، از مداحان حکومتی، خبر داد.
تسنیم به نقل از یک «منبع آگاه» گزارش داده است که رجب‌زاده چند روز پیش ناپدید شده بود و پس از آن، ویدیویی از لحظه قتل او برای خانواده‌اش ارسال شده است.
بر اساس این گزارش، پس از اطلاع از این حادثه، تحقیقات پلیسی و قضایی برای شناسایی و بازداشت عامل یا عاملان قتل آغاز شده است.
با این حال، تاکنون اطلاعات رسمی و دقیقی درباره نحوه ربایش رجب‌زاده، محل وقوع قتل، انگیزه عاملان، هویت افراد دخیل در این حادثه و جزئیات ویدیویی که برای خانواده او ارسال شده، منتشر نشده است.
@
VahidOOnLine
🔄
ادعای دقایق پیش تسنیم:
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های تجسسی صورت گرفت و نهایتا، خودرویی که رجب‌زاده برای آخرین بار سوار شده بود، شناسایی و مالک آن دستگیر شد.
🔹
این فرد که در ابتدا منکر هرگونه ارتباط با این ماجرا بود، نهایتا اعتراف کرد که با تحریک شبکه‌ای تروریستی در خارج از کشور، به همراه 4نفر دیگر اقدام به ربودن حمیدرضا رجب‌زاده کرده است. آنها در ادامه اقدام به شکنجه و قتل او کرده و تصاویری را هم برای خانواده او ارسال کرده‌اند.
🔹
به گفته این متهم، آن‌ها با وعده دریافت چند هزار دلار، اقدام به ربودن و قتل رجب‌زاده کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پست زلنسکی، ترجمه ماشین:
ما از سنای ایالات متحده و از همه کسانی که از اوکراین حمایت می‌کنند بسیار سپاسگزاریم. تصویب قانون تحریم روسیه و ایران، طرح لیندسی گراهام، قطعاً به افزایش فشار بر متجاوز کمک می‌کند تا این جنگ جنون‌آمیز روسیه علیه استقلال ما و مردم ما پایان یابد.
اوکراین قدردان
تمام
حمایتی است که ایالات متحده از اوکراین به عمل می‌آورد — از سوی هر دو حزب و تمامی مردم آمریکا. و اکنون، زمانی که پوتین آخرین امید خود را به موشک‌های بالستیک بسته تا جنگ را طولانی‌تر کند، و زمانی که ما برای یافتن موشک‌های پاتریوت به‌منظور دفاع از خود، با تمام توان وجب‌به‌وجب همه‌جا را می‌گردیم، هر نشانه‌ای در حمایت از حفاظت از جان انسان‌ها و پایان دادن هرچه سریع‌تر به جنگ، اهمیتی فوق‌العاده دارد.
فشار واقعی و قدرتمند آمریکا و تحریم‌ها علیه روسیه بیش از هر چیز دیگری کمک خواهد کرد. با هر گامی که برای افزایش فشار بر متجاوز برداشته می‌شود، دیپلماسی نزدیک‌تر می‌شود.
از همه کسانی که این را درک می‌کنند و از طریق
قدرت، صلح
را پیش می‌برند، سپاسگزارم.
ZelenskyyUa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gbc5zyN3hacpo4WaAUFY8K84a_2WXYaRLJuvB5rcgqKoFn-qjvmi2ALWw9FHmdC743dW2NfbcVg6q4ch3Cv6e3wm2JB0Kzi_H_QMPKs-JJ603KPEp4VqVihXacGvF3BJZmli-C6ENuttsHbzPTJmGpO7R4fqrWcRzrbgdXaG9TAqplafP_hlXZGdV9ikPbw2y-Qqv9-83f-mWW1DIh8f4e8Hk8rfxx5B2iRbBLmNN6dCQSCgOCdpAltANo_QcbMea5YDHl4zY8cDMafb3Mnlkd4-l7shDsL25Tvh-Wm7HN-YctIRaqMqN7gCsAYFeRjspaNRDMwjlMK64flxBThb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده آمریکا در گزارشی که روز جمعه ۱۶مرداد۱۴۰۵ منتشر شد اعلام کرد که «شبکه‌ای از صرافی‌ها و شرکت‌های پوششی مرتبط با جمهوری اسلامی» را هدف قرار داده است.
در بیانیه منتشر شده از سوی این وزارتخانه تاکید شده است که ایالات متحده در حال اخذ تصمیمات قاطع با هدف «قطع شریان‌های مالی» است که حاکمیت جمهوری اسلامی ایران را سر پا نگه می‌دارند.
این وزارتخانه در بیانیه خود نوشته است که این اقدامات با هدف برچیدن شبکه‌ای از صرافی‌ها و شرکت‌های صوری انجام خواهد شد که به ایران کمک می‌کردند صدها میلیون دلار را به‌طور مخفیانه از طریق نظام مالی بین‌المللی جابه‌جا کند.
در بخشی از بیانیه وزارت خارجه ایالات متحده آمده است که «تهران از طریق این شبکه‌ها به درآمدهای نفتی دسترسی پیدا می‌کرد، تحریم‌هایی را که با هدف مهار فعالیت‌های بی‌ثبات‌کننده‌اش وضع شده‌اند دور می‌زد و با استفاده از شرکت‌های پوششی، منابع مالی خود را پول‌شویی می‌کرد.»
هدف قرار دادن بانک‌ها، صرافی‌ها و افرادی که این شبکه غیرقانونی را اداره و تسهیل می‌کنند از سوی آمریکا چنانچه در بیانیه منتشر شده آمده راهی روشن برای اعلام آن است که «هر کس به ایران برای دور زدن تحریم‌ها کمک کند، با پیامدهای جدی روبه‌رو خواهد شد.»
وزارت خارجه آمریکا اقدامات انجام شده از سوی وزارت خزانه‌داری این کشور را نشانی بر تداوم سیاست «فشار حداکثری» دولت «دونالد ترامپ» علیه ایران دانست. سیاستی که بر «قطع منابع مالی مورد استفاده حکومت برای تهدید ثبات منطقه، حمایت از تروریسم و تقویت توانمندی‌های نظامی‌اش» تاکید می‌کند.
@
VahidHeadline
پیش‌تر:
وزیر خرانه‌داری آمریکا روز جمعه گفت که ممکن است «امروز یا فردا» توافقی با ایران برای آتش‌بس و باز شدن تنگه هرمز منعقد شود.
اسکات بسنت در گفت‌وگو با شبکه «۱۲ نیوز» با اشاره به وضعیت وخیم اقتصادی در ایران گفت: «فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد توافقی برای برقراری یک آتش‌بس ۳۰ تا ۶۰ روزه خواهیم بود و تنگه [هرمز] باز خواهد شد. قیمت انرژی هم باید کاهش پیدا کند.»
او با تأکید بر این که ایالات متحده هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست یابد، گفت تحت تاثیر عملیات نظامی آمریکا و اعمال تحریم‌های شدید علیه تهران، «آنها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی مواجه‌اند و دیگر توان پرداخت حقوق نیروهای نظامی‌شان را ندارند».
بسنت همچنین درباره وضعیت زیرساخت‌های نظامی ایران گفت: «نیروی هوایی نابود شد، نیروی دریایی نابود شد و بخش بزرگی از موشک‌ها و مهم‌تر از آن، توان تولید موشک آنها از بین رفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">#توافق_مکه
:
وزارت خارجه پاکستان در بیانیه‌ای اعلام کرد جمعه ۱۶ مرداد، پاکستان، ترکیه و عربستان سعودی، توافقنامه مشترک دفاعی امضا کردند.
توافق امضا شده تصریح می‌کند هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله علیه همه آنها تلقی خواهد شد.
در این بیانیه آمده است این امضای این توافق‌نامه «نشان‌دهنده تعهد سه کشور برای تقویت بیشتر امنیت جمعی آنها است.»
وزارت خارجه پاکستان همچنین در این بیانیه نوشت این توافق با هدف تقویت صلح، امنیت و ثبات در منطقه و فراتر از آن و برای دستیابی به آینده‌ای امن و با رفاه بیشتر تنظیم شده است.
همچنین رویترز به نقل از یک مقام ترکیه اعلام کرد «توافق دفاعی میان پاکستان، ترکیه و عربستان سعودی ماهیتی کاملا دفاعی دارد و هدف آن، ایجاد تعهد برای حمایت متقابل در زمینه دفاعی است.
این مقام به رویترز گفت: «این توافق علیه هیچ کشور یا طرف مشخصی تنظیم نشده و کشورهای دیگر منطقه نیز امکان پیوستن به آن را دارند.»
به گفته این مقام، این پیمان جایگزین یا لغوکننده هیچ‌یک از توافق‌های دوجانبه یا چندجانبه موجود میان کشورها نیست.
@
VahidOOnLine
ابراهیم رضایی، عضو كميسيون امنيت ملی و سياست خارجی مجلس شورای اسلامی، عربستان سعودی را به طور غیرمستقیم تهدید کرد که پیمان دفاعی مکه برای آنها امنیت به همراه نخواهد آورد.
رضایی در شبکه ایکس نوشت: «سعودی‌ها باید بدانند که توافق کاغذی با ترکیه و پاکستان برای آنها امنیت‌آور نیست، همان‌طور که سال‌ها شیردهی یکطرفه به آمریکایی‌ها برایشان امنیت نیاورد.»
او عربستان سعودی را به «گدایی امنیت» متهم کرده و به مقامات این کشور توصیه کرده به جای آن، سیاست‌هایشان را «اصلاح» کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=XJI3KkX2__51h-5x75OQAt_Nn3uQHrwF80i2blLE3jdnFFWpihGas6VdfpQpiWwalmjTPOTFSefQfg7lDxb54ic9F9brVp8ATHZYon9ZVv6S6RA1FgTtDLc-qsDtKp_L2ArK-fx6Oi34TQlDMGc_26gMdBgEscizGux2HdVa-jHGEEpSpPLgiLhtEyUlV_rHSp9w2yZ8Uj4jYutxYMeWX6qDwdqsVu9oMQEW9L29Jq84ctw0y17HlBJmyJKr8SWpR0dLkxWDdmMU719Rmdc61gKlgA8vzGJ5cN_FLJ8M8ZaDipl38O0EXioDHEE7jzT5Ia2TLLGJcc5dNRxP7hbBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=XJI3KkX2__51h-5x75OQAt_Nn3uQHrwF80i2blLE3jdnFFWpihGas6VdfpQpiWwalmjTPOTFSefQfg7lDxb54ic9F9brVp8ATHZYon9ZVv6S6RA1FgTtDLc-qsDtKp_L2ArK-fx6Oi34TQlDMGc_26gMdBgEscizGux2HdVa-jHGEEpSpPLgiLhtEyUlV_rHSp9w2yZ8Uj4jYutxYMeWX6qDwdqsVu9oMQEW9L29Jq84ctw0y17HlBJmyJKr8SWpR0dLkxWDdmMU719Rmdc61gKlgA8vzGJ5cN_FLJ8M8ZaDipl38O0EXioDHEE7jzT5Ia2TLLGJcc5dNRxP7hbBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین:
🔺
خبرنگار:
و آقای رئیس‌جمهور، جمهوری‌خواهان اکنون بحث زیادی درباره قدرت خرید و هزینه‌های زندگی دارند. پیام شما درباره این موضوع در آستانه انتخابات میان‌دوره‌ای چیست؟
🔻
ترامپ:
سؤال خوبی است، اما پاسخ آن تا حدی ساده است. من بالاترین قیمت‌های تاریخ را به ارث بردم. بدترین تورم تاریخ کشورمان را به ارث بردم و ما کار فوق‌العاده‌ای انجام داده‌ایم.
قیمت نفت اکنون به‌سرعت در حال کاهش است. اگر به اوضاع نگاه کنید، تا ۷۵ پایین آمده است.
وقتی آن اقدام بسیار مهم را در جمهوری اسلامی ایران آغاز کردم، اقدام بسیار مهمی بود؛ چون آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. در غیر این صورت، تمام جهان منفجر می‌شد. ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. مسئله فقط ما یا خاورمیانه نبود؛ برای تمام جهان فاجعه‌بار می‌شد. چاره دیگری نداشتیم.
قیمت بنزین در بسیاری از نقاط، مانند آیووا، به کمتر از دو دلار رسیده بود؛ قیمت‌هایی که مردم سال‌ها ندیده بودند: یک دلار و ۸۵ سنت، یک دلار و ۹۵ سنت. سه‌شنبه در یکی از توقف‌هایم در آیووا، در یک محل قیمت ۱٫۹۵ دلار و در محل دیگری ۱٫۸۵ دلار برای هر گالن بود.
بر اساس هرچه می‌بینم، به‌محض پایان جنگ، خیلی زود دوباره آن روزها را خواهیم دید. فکر می‌کنم جنگ به‌زودی پایان پیدا کند. تصور نمی‌کنم آن‌ها بتوانند مدت خیلی بیشتری ادامه بدهند. بله، بفرمایید.
🔺
خبرنگار:
آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
🔻
ترامپ:
نمی‌خواهم بگویم که توافق حاصل شده است. تنگه در حال حاضر تا حدودی باز است. می‌دانید، چیزی داریم که «محاصره» نامیده می‌شود و نیروی دریایی آمریکا آن را هدایت می‌کند؛ ما آن را کنترل می‌کنیم.
اکنون کنترل آن با ماست، اما آن‌ها همیشه می‌توانند به چیزی شلیک کنند یا مینی در آب بیندازند. حتی اگر فقط یک مین آن بیرون باشد، اوضاع را به هم می‌ریزد؛ چون مردم نمی‌خواهند کشتی‌های میلیارددلاری خود را وارد منطقه کنند و تصادفاً با مین برخورد کنند.
اما فکر می‌کنم عملکردمان بسیار خوب است. خودم در مذاکرات دخیل هستم و فکر می‌کنم اوضاع خوب پیش می‌رود. ممکن است توافق حاصل شود؛ ممکن است به‌زودی باشد. بله.
🔺
خبرنگار:
آقای رئیس‌جمهور، درباره مهمات؛ شما شب گذشته نوشتید که آمریکا مقدار عظیمی مهمات دارد و وجود هرگونه کمبود را رد کردید. در عین حال، یک درخواست بودجه تکمیلی ۲۱ میلیارد دلاری برای پرکردن مجدد ذخایر وجود دارد. اگر کمبودی نیست، چرا این درخواست همچنان مطرح است؟
🔻
ترامپ:
چون همیشه به مقدار بیشتری نیاز داریم. منظورم این است که مهمات بیشتری لازم داریم.
ببینید، دولت بایدن مقدار بسیار زیادی به اوکراین داد؛ رایگان، بدون دریافت هیچ پولی. میلیاردها و صدها میلیارد دلار.
خوشبختانه من در دوره خودم ذخایر بسیار زیادی ایجاد کرده بودم. نیروهای نظامی را بازسازی کردم و مقدار زیادی تجهیزات و مهمات نیز در اختیارشان گذاشتم.
از بعضی انواع مهمات بسیار قدرتمند، ذخیره‌ای نامحدود یا تقریباً نامحدود داریم. در مورد بعضی انواع دیگر، وضعیت کمی محدودتر است و هر روز محموله‌های تازه دریافت می‌کنیم.
همان‌طور که می‌دانید، شرکت‌های دفاعی ما اکنون بیش از هر زمان دیگری در تاریخ کارخانه می‌سازند. برای موشک‌های پاتریوت، تاماهاوک و همه‌چیز کارخانه می‌سازند.
در عین حال، انواعی از مهمات داریم که ممکن است به آن اندازه دقیق نباشند یا در آن سطح ممتاز قرار نگیرند. نمونه‌های ممتاز را هم داریم و این موضوع را بسیار دقیق زیر نظر گرفته‌ایم. اما بعضی از انواع مهمات ما بسیار قدرتمند و بسیار خوب‌اند و ذخیره‌ای نامحدود از آن‌ها داریم.
بنابراین در وضعیت بسیار خوبی هستیم. بااین‌حال، همیشه مهمات بیشتری می‌خواهیم و باید مقدار بیشتری داشته باشیم. ممکن است مسائل دیگری پیش بیاید و ممکن است هم پیش نیاید. امیدوارم هیچ مسئله دیگری پیش نیاید، اما ما در وضعیت بسیار خوبی قرار داریم. واقعاً مقادیر عظیمی مهمات داریم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWtGIytA5a9g7473xd7h4YRg_8cXFqfuHaLBmGMXrVi9FXr10ya-6B9kg248upl4ivyClKyaF1ejaXy6qvZmMWzznxGjL_L3LMeokfNZJ5XUG16ylhpZNSVa_JnkJ6YEFEX4_A-9timiZ8g9WxyploIF9KVPSmRsulsVXkXIzW5fJwtuvBrud6LC55H9h5kyei2I6Ost7s4yPiMC2sgmYqAgLxQzsBz5UO7Xw_RRcLtNTR_F0g4ViPupuvBq7HEu7ifqnZrZ7oeVkITQ7GV8DyDBQFQ5PysMG9E2rLkCbuvDjEcD0afR1HzSwxkxvStr8m5sySZu2rhQ5EGwQu2-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5u2sypVO4ljUF16lO-XPB9U7vb7hQNof9UIwQa2DmZG0xssQSCjzJhjg8ymPW7jpitWd6EQ50nOVq3R2vTVq_XSQg9DOhxlnu4FP8as1EchuytToyoa3Y2gBZ3hOs2f9q36KiElR957TrTjOctHN6uK38zlj4Q1mpW4PvyioBU10t9KnnGMxTvYY4bjyiBcys2vw_xDKmQAdXKaLhzV1FtiZXXKKo1v0QcNNYdQjiYjSd0sW4dGFP4bIrMtPwkW1KOx9dtb2cpOEHDSsrppnTTY6AX_YVql5guNiPyvVjmDIf3uSJJBcFqYf7Q6J3hpi4kfP2rf3-ABkWNmg8G35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
همین الان دو صدای بد انفجار شنیده شد قشم
سلام ساعت ۲۱ و ۴۳
قشم دو انفجار نزدیک شهر
سلام وحید جان الان قشم صدای دو انفجار بد اومد
صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن
وحید قشم رو زدنننننننن [لطفا صداها رو تفسیر نکنید]
۴ تا انفجاررررر
قشم هم اکننون سه انفجار
ساعت ۲۱:۴۱ قشم
دوتا انفجار یکیش خیلی قوی تر بود، اسکله بهمن بود یا کشتی‌های نزدیک اسکله
بندرعباس ۲۱:۴۳ دو سه تا صدای انفجار [که لابد همون قشم بوده.]
همین الان صدای ۴ تا انفجار اومد قشم
دوتاش خیلی شدیدو نزدیک بود
دوتاش خیلی دور بود
سلام وحید جان ساعت ۹ و ۴۲ دقیقه قشم دوبار صدای انفجار اومد ،نمی‌دونم چی بود ،خونه لرزید
ساعت ۲۱:۴۰ صدای ۲ انفجار شدید شهر قشم درب و پنجره ها لرزید
سلام وحید جان صدا سه تا انفجار تو قشم اومد دوتا شدید بود یکی انگاری دور بود
🔄
منابع حکومتی:
🔹
معاون امنیتی استانداری هرمزگان،: تاکنون هیچ‌گونه اصابت یا حادثه‌ای در جزیرۀ قشم و شهر بندرعباس گزارش نشده است.
🔹
بررسی‌های لازم توسط دستگاه‌های مسئول برای شناسایی منشأ صدای شنیده‌شده درحال انجام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77764" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hxLyNn1QfxkXGHCUIP-ov_awot-FGLsFBqFMFYi_HTJYh5Cl67uuhadGKRmsGJEpiEooIq6HNmW9aFy7ldQeOfinEJsorcE3QuPfqzC7xnJIx83IeEoVhva8fao3epcMMpPZIcuqlIpHbVhr1KEUrNPTIhjpvgQ26-IJCn-JgWYnmIic4A3L5mkeARg8BLShSVHXKTI1XV28N_KivxfnRKy7csHD23EQYpD56IpRqfS6t4CjmcHCQ9itBKR8V_3Lvwdx59YY9JbjghnDSdlo-8vh5Nbc_Hb1UydbKIurCnHN85qtuupNIPS0qp6up-_gge-0iz2MLYzQ72aQCaD55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اخبار جعلی، طبق معمول، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس است. من از عملکرد پیت هگست به‌شدت راضی هستم. همه‌چیز فوق‌العاده بوده است؛ از جمله حمله ما به ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد نیکلاس مادورو، یکی از بدترین جنایتکاران در سراسر جهان، را به دست عدالت بسپاریم!
همین‌طور اوضاع ایران، که برای هرگز اجازه ندادن به آن برای دستیابی به سلاح هسته‌ای به‌شدت درهم کوبیده شده، بسیار خوب پیش می‌رود! پیت در میان نیروهای نظامی از احترام بسیار بالایی برخوردار است و اصلاحات عظیمی انجام داده؛ از جمله برچیدن سیاست‌های تنوع، برابری و شمول (DEI) و افزایش جذب نیرو به سطوحی تاریخی.
این شایعه را «واشنگتن کام‌پوست» ــ یکی از بدترین رسانه‌های این حرفه ــ به راه انداخت، آن هم با وجود اینکه به آن‌ها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این «گزارش‌گری» جعلی آن‌ها خیانت‌آمیز است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77763" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDFhZ1YZLJASr25bKNwSl0RDlp--HGZR93_bgdzahOFoIQSUR5knpqpbeDEZcJIXVfFro_-oL3HSe_WQSb-hBLOG7HTjbJGpE-I_AvAaL3-DUibFLJKw2x5M1KOU_mx_22yhC4fLyfXvtbHIeOlpV36eNLABZx50Wt1T2DheZmf6eKEycN4Y-aSBx2yp4N-ijap8MEm-mnsVJQ0-OWpLXNfGBGPhny_pRxqUfv1VbnqbrNPOYSZvcObsNT7qxsDsf6DjikyChBDz7GYeoVGOC5MTk13BORGD91gySubVfrUqSPfceSI7x5ap06uobB5HDUiHHcxw2OVSNkUbF8BAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
ایالات متحده مقادیر عظیمی «مهمات»، به‌ویژه از برخی انواع خاص، در اختیار دارد.
افزون بر این، هر مقدار که نیاز باشد، حجم زیادی مهمات تولید و به ایالات متحده ارسال می‌شود.
شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات تولیدی در تاریخ کشور ما هستند.
کسانی که این اظهارات خیانت‌بار را درز داده‌اند، تحت تعقیب قرار دارند.
برای آن‌ها درخواست محکومیت‌های طولانی‌مدت زندان خواهد شد!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/77762" target="_blank">📅 09:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CGpSrlX6cPhsQ6kEmVJEtyOY1I84RCga6oV8Rk2_DsZTRdYRaeECyvxtvxHle1-4EftLEq5YVvslxv0_6Hb6oFrwGQFJZAlvDBSVOuzcHhwqJ0wK-bvsGB7nH3beIVEtuD1Lwq8ZQPGC8of0ADhg9bbNXzcA2vtCxwP0m7AzJ2GtzM3k8KIXiP9JyxcIvFLEpkyguLQiK7R8cOJaJ6adUhhMPSlFjZ_kMC5T2pqJt06seGXvtXK8UED-hRa_BhL1I4ZyoLsdGwB5qASJ45zraEiljSymCYz4S_Z0GbvpjTj424b2ph5f6GJKfTReeZ8rLKA3Pw350T-p9RLP2OibyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن پست
:
درگیری ترامپ و هگست در کمپ دیوید بر سر نگرانی‌ها از کاهش ذخایر موشکی در جنگ ایران
ترجمه ماشین:
در نشست این آخر هفته در کمپ دیوید، رئیس‌جمهور ترامپ از پیت هگست، وزیر دفاع، درباره کمبود شدید مهمات توضیح خواست.
به گفته دو فرد آگاه از این گفت‌وگو به روزنامه واشنگتن‌پست، سرخوردگی دونالد ترامپ، رئیس‌جمهور آمریکا، از جنگ ایران هفته گذشته در کمپ دیوید فوران کرد؛ جایی که او از پیت هگست، وزیر دفاع، خواست توضیح دهد چرا ظاهراً درباره کمبود شدید مهمات ــ که اکنون گزینه‌های نظامی در برابر ایران را محدود می‌کند ــ گمراه شده است.
این رویارویی روز جمعه و در حاشیه نشست کابینه ترامپ در کمپ دیوید رخ داد. به گفته هر دو فرد آگاه از گفت‌وگو، ترامپ با عصبانیت به هگست گفت تصور می‌کرده مشکل مهمات «حل شده است». این افراد نیز مانند دیگران، به‌دلیل ترس از تلافی‌جویی، به شرط ناشناس‌ماندن صحبت کردند.
به گفته یکی از منابع، کمبودها، به‌ویژه در زمینه موشک‌های هدایت‌شونده دوربرد و موشک‌های رهگیر پدافند هوایی، از دلایلی بوده است که ترامپ در روزهای اخیر از اجرای حملات گسترده‌تر علیه ایران عقب‌نشینی کرده است.
کارولین لیویت، سخنگوی کاخ سفید، در پاسخ به پرسش‌های واشنگتن‌پست گفت: «این خبر صددرصد جعلی است. واقعاً هرگز چنین اتفاقی نیفتاده است. رئیس‌جمهور ترامپ نیز نهایت اعتماد را به وزیر هگست دارد.»
متن کامل فارسی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77761" target="_blank">📅 08:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=nj-ofjG95bT6yWFZ0fdoBBMLK4aqE3M-EpdPoEuWUQnGz7LDAFve5ascjYDcvztQlXvWxPBuHvR0y-tTyIhnmG0Q6DfWlmJoHt4pVeajYn7kSHeUUwq5OwWJzeJwES2tiVPu3lfRl2cv1h-mltRLIXTYRwJGO8tCh3n8wKmcqDhB5AR8RaDPNE0BBLoFYjTJGNcWT7cu02pdAlh4IUhmkZ7STDwVACkMgceyYADiO-jQffzKNE-rdmNOuRgRrjFclurhZR3zfHDj7c0Oz0q4E_ulzD0VCQ2vp7zepl_7iMkwXXLYs5SDkY1H5nZns0KvyZfYZkNAHhUlJp6rYmQu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=nj-ofjG95bT6yWFZ0fdoBBMLK4aqE3M-EpdPoEuWUQnGz7LDAFve5ascjYDcvztQlXvWxPBuHvR0y-tTyIhnmG0Q6DfWlmJoHt4pVeajYn7kSHeUUwq5OwWJzeJwES2tiVPu3lfRl2cv1h-mltRLIXTYRwJGO8tCh3n8wKmcqDhB5AR8RaDPNE0BBLoFYjTJGNcWT7cu02pdAlh4IUhmkZ7STDwVACkMgceyYADiO-jQffzKNE-rdmNOuRgRrjFclurhZR3zfHDj7c0Oz0q4E_ulzD0VCQ2vp7zepl_7iMkwXXLYs5SDkY1H5nZns0KvyZfYZkNAHhUlJp6rYmQu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش مربوط به ایران،
تشخیص و ترجمه ماشین:
در ونزوئلا خیلی خوب پیش می‌رویم.
نفت زیادی از ونزوئلا می‌گیریم و رابطه‌مان با آن‌ها هم بسیار خوب است.
میلیاردها و میلیاردها بشکه نفت از ونزوئلا خارج می‌شود. ونزوئلا یکی از غنی‌ترین نقاط جهان از نظر نفت است.
و همان‌طور که می‌دانید، آن یک جنگ ۴۸ دقیقه‌ای بود؛ ۴۸ دقیقه طول کشید.
و هزینه جنگ را با آنچه از آنجا بیرون آورده‌ایم، چندین و چند و چند برابر جبران کرده‌ایم.
قبلاً کجا چنین چیزی شنیده‌اید؟ هیچ‌جا نشنیده‌اید.
همان روش قدیمی است، درست است؟ همان روش قدیمی.
غنائم از آنِ فاتح است، درست است؟
و ضمناً همین کار را در جمهوری اسلامی «دوست‌داشتنی» ایران هم انجام می‌دهیم.
داریم حسابی می‌کوبیم‌شان.
ترجیح می‌دهم توافقی انجام شود، چون نمی‌خواهم مردم را بکشم. نمی‌خواهم مردم را بکشم.
اما بالاخره در مقطعی قرار است... ما... ما برای بزرگ‌ترین حمله در میان همه حملات آماده شده بودیم و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
اما کاملاً آماده بزرگ‌ترین حمله از زمان جنگ جهانی دوم بودیم.
آن‌ها با من تماس گرفتند و گفتند: «لطفاً این کار را نکنید. بیایید گفت‌وگو کنیم.»
بعد می‌گویند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟ رسانه‌های جعلی می‌دانند که آن‌ها چنین چیزی گفتند.
اما در حال گفت‌وگو هستیم. ببینیم چه اتفاقی می‌افتد.
ولی آن‌ها برای ما احترام قائل‌اند. به ما احترام می‌گذارند.
۴۷ سال گذشته است؛ ولی در واقع ۵۰ سال شده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال شده است.
هیچ رئیس‌جمهور دیگری کاری را که باید مدت‌ها پیش انجام می‌شد، انجام نداده است؛ زیرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد. نمی‌تواند داشته باشد.
---
و به‌محض اینکه این وضعیت با ایران پایان یابد، قیمت نفت به‌شدت سقوط خواهد کرد. قیمت بنزین هم پایین خواهد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddou34XQrgj1BfGgL9BCiLWipVd9nMiWZriJk00Hurisl2yQgrggE8j3k_MFSMZFYNXB5Ef3_0_Q4GllINLKmQSb_lTKzjMx87LE-0q1-XHUAs73P1w0JPf8Ny1wrfRXQCW5ZF6684HGF46svw2vUMeeS1nT6B_gp3gxkE-PjxOLnk5e8HFf81vnqZlo9oMXRn_9j2aZLj39PLxHBoOtqZxKS3LkEp4zYyNTUYpZwmM4k078mBkj92qlyWt6SjPR3ALQx778iqwdi7BesIw3o6lcZX6NvWxUrBGUL8J_FimYgJXAYUFtyFmekJ1Gly0lHjaddimDF-jc_SWFuEHT6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzrrpQlYUKrnfTVypwQwHHNGLVGyRjpuLJN5sraneTA8TQ5BQI3hAGmkZN9TZXdZ12YCjvHJBWvHVe_-LNlg9INE7i3btIMPMm25as_8BuZPoMhHRQi5k4CZt8fIdn5FAUY_xfC9_q0eQmm19Hi_LjGkV-40YBAvpVcqs46UKoiNalhXl3JtV4p1ZZinfFw2t5YbBd3fFgtGi8PuJkQmMyPLaJVDIZpsGyp3wcwBeXSHiUrBEBfwiYMoo666SFYKm0AMDjwfJ-IR5F-sedTbjM4VLL-HFOrHko0M7R6wA6L2D5L40fl-s1VOyNvt7WavdWN3XIrTHONPs4x97NV1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=Mt1t2m_-q74to1epatkzenUKbJjf46D82yuoSEtozSaOtQKCPmYHyaTwjmp3wOMwAbFQJg7UYLEk2NBRckHpXcPh-0Rscjqry1IFEkuGHgsCONCoctAljC5tcjeuxy7wgoKgREjwlQMK2ZfhcvTHq8-xOFf4nPzoZrqml6Ke-uqrhn797RaSDAYTWh2On5FCOUt9PBed2cEXvG4XwGFj7cZNjJgfnGZQ8Ghyp_F3t3xsqRjTZO5A0682OsFmMgYqsodrM9_CcGctemEUkXP7NKdg_ht_a8-62cQOdxSwZdC_RIhahPmkeZdRfglPW5b3xyHCiEHX2jX3hbt5xvfw-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=Mt1t2m_-q74to1epatkzenUKbJjf46D82yuoSEtozSaOtQKCPmYHyaTwjmp3wOMwAbFQJg7UYLEk2NBRckHpXcPh-0Rscjqry1IFEkuGHgsCONCoctAljC5tcjeuxy7wgoKgREjwlQMK2ZfhcvTHq8-xOFf4nPzoZrqml6Ke-uqrhn797RaSDAYTWh2On5FCOUt9PBed2cEXvG4XwGFj7cZNjJgfnGZQ8Ghyp_F3t3xsqRjTZO5A0682OsFmMgYqsodrM9_CcGctemEUkXP7NKdg_ht_a8-62cQOdxSwZdC_RIhahPmkeZdRfglPW5b3xyHCiEHX2jX3hbt5xvfw-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل روز چهارشنبه ۱۴ مردادماه با انتشار پیامی ویدیویی اعلام کرد این کشور با طرح پیشنهادی آمریکا برای خلع سلاح حماس و مدیریت غزه موافق نیست.
نتانیاهو در این پیام گفت: ««رئیس جمهوری ترامپ و تیمش فکر می‌کنند می‌توانند حماس را به خلع سلاح و غیرنظامی کردن غزه وادار کنند. ما در حال بررسی این موضوع هستیم. آنها پیش‌نویسی برای ما فرستادند، ما موافق نبودیم، این پیش‌نویس ما نیست؛ ما نظرات خود را ارسال کردیم.»
حماس هفته گذشته اعلام کرد به شرط خروج اسرائیل از نوار غزه، خود را خلع سلاح می‌کند. با وجود واکنش مثبت ترامپ، اسرائیل همچنان با این پیشنهاد حماس مخالف است و چند وزیر کابینه ائتلافی، پیشاپیش تاکید کرده‌اند که ارتش این کشور از غزه خارج نخواهد شد.
@
VahidOOnLine
نخست‌وزیر اسرائیل در سخنرانی خود در خاکسپاری رسمی پدربزرگ و مادربزرگ تئودور هرتسل، با اشاره به تحولات جاری تاکید کرد که این کشور در میان رویدادهای حساس نظامی و سیاسی قرار دارد.
بنیامین نتانیاهو با تمجید از رئیس‌جمهوری آمریکا گفت: «می‌خواهم این موضوع را روشن کنم؛ رئیس‌جمهوری ترامپ بزرگ‌ترین دوست ما و بزرگ‌ترین دوستی است که تا کنون در کاخ سفید داشته‌ایم و ایالات متحده نیز بزرگ‌ترین متحد ماست.»
با این حال، نخست‌وزیر اسرائیل با تاکید بر حفظ منافع بنیادین تل‌آویو افزود: «اما موجودیت اسرائیل — چه با توافق و چه بدون توافق — قابل مذاکره نیست. من مصمم هستم که هر آنچه برای تضمین امنیت و آینده‌مان لازم است را انجام دهیم.»
اسرائیل در حال حاضر در میانه گفتگوها برای دو توافق قرار دارد: توافق با لبنان برای خروج تدریجی نیروهایش از جنوب این کشور و توافق صلح غزه برای واگذاری مدیریت این مناطق به هیات صلح مطابق طرح ترامپ.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز چهارشنبه ۱۴ مرداد، در جریان بازدید از مرکز جذب سربازان جدید با تاکید بر اتحاد داخلی این کشور پس از حوادث هفتم اکتبر، تصریح کرد که تل‌آویو اجازه تشکیل کشور مستقل فلسطینی را نخواهد داد.
نتانیاهو با اشاره به این موضوع گفت: «ما در اینجا یک دولت تروریستی فلسطینی تاسیس نخواهیم کرد؛ دولتی که می‌دانیم قصد نابودی کشور-ملت یهود را دارد.»
نخست‌وزیر اسرائیل در ادامه افزود طرف مقابل در پی نابودی اسرائیل است، چرا که این کشور ترویج‌کننده ارزش‌های پیشرفت، دموکراسی و آزادی است؛ ارزش‌هایی که به گفته او، مورد نفرت «دشمنان بربر» قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZwD1yaRYIyGUWntM22rsSVvl9yw2XU-GrYs4bkvMQ08oGkXhB1wuEk4H8vZKqrzMPQAe888OkAGThz-KfJUAd7CrDUcPWbKhinz8B5zu1MYPsqSgDYEvkWdhwqUxxux3G82mk_kya0z0Qv7iSqFFBliWVYGcKG_dAf4esKr4KDuTfO9dAGYcUmO4LgD1iLc8bKD_ezFPhj5j8FpkIZOcQEgtTlvRSOG-HjxSdv2waWqcdSTUhNK5DDKaP0WMtoJsYV94l1IMDJ3T21NTykHrE8L16Q6SC9CYkrG3lTK9xGijfKuqNSlohnHir6vYtSJFBBv3NFxdSmGqS9htEdXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRgf6YBQXjJ9G-FxT3W0PPek_FtS_vKesWUQ_ExjARm13vRqb8KZJz0RFkLoXpSwHRdcEs8hp2bN1gIXybxidIJ4yH80UGL-yPa1UeJ4xqRq3rMRjwhCJstPoSWM7xldjWHJs9HjD-Z34XMtzG15ncRwRE5uRy6SOsJoHpzms51N72G9STbqMVpynGEC9nUNBVJyodzSe1UHnagIvAuym7kIc9cPx-kdnYEUPyQOLliW0lFpuTEEM3Fqhy654A_uDjT91glk3vsCcGYmH_WxEEREQZgjlj4uKhc4fUigKhlVBqrttqOMYZoOnOf_-xNkmGZvIPeLLt7BYUc7_H84oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در واکنشی دوپهلو به تکذیب دفتر مجتبی خامنه‌ای، اعلام کرد این تکذیبیه را می‌پذیرد، اما ابراز امیدواری کرد پس از «تغییرات مهم آینده» این دفتر نیز همچنان پابرجا بماند.
این واکنش شامگاه سه‌شنبه ۱۳مرداد۱۴۰۵، در صفحه اینستاگرام دفتر خرازی منتشر شد.
در بیانیه دفتر او آمده است: «گرچه به احترام قائد شهید و نیز رهبر معظم حاضر، تکذیبیه روابط عمومی و دفتر نشر آثار را حدوثاً می‌پذیریم، ولی امیدواریم پس از تغییرات مهم آینده در حوزه دفاتر فوق، این تکذیبیه همچنان باقی بماند.»
در ادامه بیانیه آمده است: «خداوند ما را در صورت استقامت و صبر در راه اهل‌بیت و ولایت معظم فقیه یاری خواهد فرمود.»
فرستاده است.
دفتر مجتبی خامنه‌ای ساعاتی پیش از انتشار پاسخ خرازی، ادعای او درباره هشدار رهبر جمهوری اسلامی به مسعود پزشکیان بر سر استعفا را تکذیب کرده بود.
در بیانیه این دفتر، بدون نام‌بردن از خرازی، آمده بود: «مطلب منتشرشده در فضای مجازی که در آن فردی، ادعایی را درباره واکنش رهبر انقلاب اسلامی به نامه رییس‌جمهوری محترم مطرح کرده، از اساس کذب و خلاف واقع است.»
دفتر مجتبی خامنه‌ای انتشار این ادعا را «زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه» توصیف کرده بود.
یک روز پیش از انتشار این تکذیبیه، ویدیویی از سخنان خرازی در شبکه‌های اجتماعی منتشر شده بود. او در این ویدیو مدعی شده بود مسعود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده است.
خرازی همچنین گفته بود مجتبی خامنه‌ای در واکنش به این موضوع نوشته است: «یک بار دیگر پزشکیان استعفا کند، استعفایش را می‌پذیریم.»
او مدعی شده بود پس از این هشدار، پزشکیان و دیگر مقام‌های دولت از مطرح‌کردن دوباره استعفا عقب‌نشینی کرده‌اند.
@
VahidHeadline
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tefPvTrxQGM8j8I8OFaB8wZpcgeNMEWxnqH6G_NI_ov7tVhjtmQfCb0qzsymQrZpsOKTiHVBuiueyxPPjnNKDG97-4OU4jhIfFZrr0kLLC0yU3lv7h8G5NuWGR2p86mMfGBQI5MeI0BpXU0PcxAGWDBN0weWO5pozY5XK8r7ktCwVA-jbf9bREd6robGWXL-z-1k19PX3NksG4Y3dXXSm8vZW6BfslZWRK3a1RhitTR2JtgfVXrPLJdy3NgTXjWkdi1IVRGgU7L0eQlDkvyjGrMqkL0bA2p8awQkG-OxcJREUEyLYWJ61F6qmNfx-ZxDZLdruL4niqR5xMckybYGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل متحد، اعلام کرد که از ۲۹ اسفند ۱۴۰۴ تاکنون، دست‌کم ۵۶ نفر در ایران با اتهام‌های امنیتی اعدام شده‌اند.
ولکر تورک با صدور بیانیه‌ای یادآور شد که از این تعداد ۲۷ نفر از معترضانی هستند که در تجمعات اعتراضی دستگیر شده‌اند.
او اعلام کرد که در این مدت روند صدور و اجرای احکام اعدام در ایران افزایش یافته است.
کمیسر عالی حقوق بشر سازمان ملل متحد از مقام‌های جمهوری اسلامی خواست تا همه اعدام‌ها را متوقف کنند و در مسیر لغو مجازات اعدام گام بردارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77754" target="_blank">📅 17:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoB_gRjShhIhz3M8e1_mT1SU276ZG0PrMWRXD9o4G9P3UXAp_EheSMrAaWBk1_ruXfpsBrNdmKDuNyaortv1Ijsip0eK8WjYx5d65J1V_zGqbqkKgb_aqMx1sF8to8ni5b9oyypqJIKlnsIGaH94AVfGBUVylXg3rxvpdP5kFHV8CsRnYscAPieHtuMpn55j1Lt79HuC9lLfBcL6UjqkGfuIvkBiLBaSdNmKnJoEagHOb8mi1_3aDEPa8ZmaYsOa7PFKsnFLDApV_E9ZEK_KTIocFV9Yq4dWO1s5MBDEBNA-y6DwjBZB-_6ht0gDOyEKQndGfuWXFEecebVR_LHWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی قاسمی حسنوند، شاعر، زندانی سیاسی سابق و شهروند اهل شهرستان الشتر، روز یکشنبه ۱۱ مرداد ۱۴۰۵ پس از اقدام به پایان دادن به زندگی خود مقابل دفتر سازمان ملل در اربیل جان باخت.
منابع آگاه به ایران‌وایر می‌گویند او پس از آزادی از زندان با مشکلات روحی و فشارهای ناشی از پرونده قضایی خود روبه‌رو بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77753" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04787365a6.mp4?token=bliyQM3nblgJizVt1StohJCivhR97dRiK3dklgXebnPrAXLHW-0sGzP0DXbOx6aq6LSoYB6ZKX7tcmUzWWvdZ8D-WrtGB47xfHMLHJj9FNWY8RA1WOSnLD0hdCvfKb6mEaf3n3R0wT4neieo6kjlRdJ7Q9x3mdu00HPTEMQSVc9kW_IuEd_XMBux-Y4g50zNnHwnIr9mSKSVChFWWj14RDQ15IptFSSebm_m8LufjjOorLTq8F9c59lKv7qwzQ8JuVU1h8Z8NanllHjvkycsc13xMAAh1EwFxyYWC5iK6OXYI_5ieBIm07FKWqkiWrLw8NBsrPxTZtkk4c2zI8j5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04787365a6.mp4?token=bliyQM3nblgJizVt1StohJCivhR97dRiK3dklgXebnPrAXLHW-0sGzP0DXbOx6aq6LSoYB6ZKX7tcmUzWWvdZ8D-WrtGB47xfHMLHJj9FNWY8RA1WOSnLD0hdCvfKb6mEaf3n3R0wT4neieo6kjlRdJ7Q9x3mdu00HPTEMQSVc9kW_IuEd_XMBux-Y4g50zNnHwnIr9mSKSVChFWWj14RDQ15IptFSSebm_m8LufjjOorLTq8F9c59lKv7qwzQ8JuVU1h8Z8NanllHjvkycsc13xMAAh1EwFxyYWC5iK6OXYI_5ieBIm07FKWqkiWrLw8NBsrPxTZtkk4c2zI8j5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
▪️
تنگه هرمز به‌زودی باز خواهد شد
▪️
مذاکرات با ایران به‌خوبی پیش می‌رود، اما تهران تمایلی به تایید آن ندارد
▪️
اگر بار دیگر عقب بکشند، ضربه سختی خواهند خورد
ترامپ:
اگر به اقتصاد نگاه کنید، اگر به اتفاقاتی که در حال رخ‌دادن است نگاه کنید... برای نمونه، ایران هرگز سلاح هسته‌ای نخواهد داشت. همین حالا هم دیگر نمی‌تواند داشته باشد، اما قرار است این موضوع رسمی شود.
تنگه [هرمز] خیلی زود باز خواهد شد؛ وگرنه ضربه بسیار سختی خواهند خورد و پس از آن، تنگه باز خواهد شد.
ما آماده انجام حمله‌ای عظیم بودیم؛ بزرگ‌ترین حمله از زمان جنگ جهانی دوم. بعد آنها با من تماس گرفتند و بسیار مؤدبانه گفتند: «لطفاً، می‌توانیم صحبت کنیم؟ می‌توانیم گفت‌وگو کنیم؟» آنها نمی‌خواستند... [جمله ناتمام است].
من هم گفتم: «بله، می‌توانیم صحبت کنیم. بیایید بالاخره این کار را تمام کنیم. بیایید انجامش دهیم.»
این کاری است که رؤسای‌جمهور دیگر باید طی ۵۰ سال گذشته انجام می‌دادند. می‌دانید، مدام عدد ۴۷ سال را می‌شنوید، اما سه سال است که همین عدد گفته می‌شود؛ حالا دیگر بیش از ۵۰ سال شده است.
رؤسای‌جمهور دیگر یا کشورهای دیگر باید می‌توانستند این کار را انجام دهند.
من کاری را انجام دادم که مجبور بودم انجام دهم؛ چون اگر آنها سلاح هسته‌ای داشتند، تمام این جهان جای متفاوتی می‌شد.
خبرنگار فاکس‌نیوز:
اگر دوباره عقب‌نشینی کنند و زیر توافق بزنند، کارشان تمام است؟
ترامپ:
اگر دوباره زیر توافق بزنند، ضربه واقعاً سختی خواهند خورد. خودشان این را می‌دانند و درک می‌کنند. من انتخاب دیگری ندارم. آنها نمی‌توانند سلاح هسته‌ای داشته باشند. موضوع بسیار ساده است.
این‌طور نیست که بگوییم: «خب، بیایید درباره چیز دیگری فکر کنیم.» نه؛ رؤسای‌جمهور بسیاری باید طی سال‌های طولانی این کار را انجام می‌دادند، اما انجام ندادند. حالا من دارم انجامش می‌دهم.
اوباما را کاملاً سرکیسه کردند. او فکر می‌کرد می‌تواند با پرداخت پول خودش را از این وضعیت خلاص کند. میلیاردها، ده‌ها میلیارد دلار به آنها داد؛ آن‌هم به‌شکلی بسیار احمقانه.
۱٫۷ میلیارد دلار پول نقد، اسکناس‌های سبز، در یک هواپیمای بوئینگ ۷۵۷؛ هواپیمایی پر از پول نقد. احتمالاً وقتی آن را دیدند، گفتند: «حتماً شوخی می‌کنید!»
نه، نمی‌توانید با پول‌دادن خودتان را از چنین وضعیتی خلاص کنید؛ تنها راه این است که با جنگیدن راه خروجتان را باز کنید.
اگر ما این کارها را انجام نداده بودیم، آنها مذاکره نمی‌کردند. ما ضربه بسیار بسیار سختی به آنها زدیم. اما ضربه سخت‌تر هنوز در راه است و امیدوارم مجبور نشویم از آن استفاده کنیم. امیدوارم مجبور نشویم.
گفت‌وگوهای بسیار خوبی داریم. آنها دوست ندارند به این موضوع اعتراف کنند، اما این کمی آزاردهنده است. به افرادی مثل شما می‌گوییم که گفت‌وگوهای فوق‌العاده‌ای داریم، بعد یک نفر از ایران می‌آید و می‌گوید: «ما دیدار نکرده‌ایم، ما...» [جمله در زیرنویس ناتمام است].
تمام روز چنین دروغ‌هایی می‌گویند. متوجه هستید؟ باورنکردنی است. می‌گویند: «ما این کار را نکردیم.» می‌گویند درباره موضوع هسته‌ای صحبت نکرده‌ایم.
خب، پس درباره چه چیزی صحبت می‌کنیم؟ آنجا نشسته‌ایم و بی‌کار انگشت‌هایمان را به هم می‌زنیم؟
اما اهمیتی ندارد. اینها فقط حرف است. تنها چیزی که اهمیت دارد، عمل است. آنها می‌خواهند توافق کنند. خواهیم دید چه اتفاقی می‌افتد. اگر توافق نکنند، برایشان خیلی بد خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77752" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpsx-OMVvFTW6uVvOvYYQ0uwS7oQDkcBDXTw_Nd7Nq7jJh43mWe7TASp0gzZeXbSxN9dtMw41ASqg5ZPAg1K8PvHD4GUubC4l-UIZgDrhZWsWE7ZNIIsgXUvLTlp-43hI00SI7z98-HMCFNd4fuzBwGsLs9nL9EwIhqToHysDWd3BsY15Se14weDuhNRuejUtJ_1JNVVW8kK_XbttkzK7qh9T462d11j9Bs3R1CowkrjXIjKcsTJ6G7obtNfHT-x1pDlTbeAmcWalK37Bpk9sUujfBPBXLKiPrVVcanJcAwwfTwKFfndYCAf6cfQMdwUVThg8AsIEfzj2wXjRCScIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"آمریکا به توافق درباره هرمز نزدیک شده و به‌دنبال اعلام آن در روز چهارشنبه است"
اکسیوس، ترجمه ماشین:
به گفته دو منبع منطقه‌ای و یک مقام آمریکایی، آمریکا، ایران و عمان به دستیابی به یک توافق موقت برای بازگشایی تنگه هرمز نزدیک شده‌اند و آمریکا قصد دارد این توافق روز چهارشنبه اعلام شود.
🔻
چرا اهمیت دارد:
هدف از این توافق که چند هفته است درباره آن مذاکره می‌شود، ازسرگیری آتش‌بس میان آمریکا و ایران و آغاز دوباره مذاکرات بر سر یک توافق هسته‌ای است.
▪️
رئیس‌جمهوری ترامپ روز شنبه تصمیم گرفت تهدیدهای خود برای آغاز یک کارزار بمباران گسترده را عملی نکند تا فرصت بیشتری برای دیپلماسی فراهم شود. با این حال، اگر به‌زودی توافقی حاصل نشود، ترامپ ممکن است با حملات بزرگ موافقت کند.
▪️
توافق در حال شکل‌گیری برخی از خواسته‌های ایران برای کنترل بیشتر بر رفت‌وآمد در تنگه هرمز را تأمین خواهد کرد؛ کنترلی که ایران پیش از جنگ در اختیار نداشت.
🔻
اصل خبر:
به گفته دو منبع منطقه‌ای، توافق مورد بحث یک سازوکار موقت ۶۰روزه میان عمان و ایران در تنگه هرمز ایجاد می‌کند که امکان تمدید آن نیز وجود دارد.
▪️
همه کشتی‌هایی که از طریق تنگه وارد خلیج فارس می‌شوند، از یک مسیر شمالی در آب‌های ایران عبور خواهند کرد.
▪️
همه کشتی‌هایی که از تنگه خارج می‌شوند و به دریای عرب می‌روند، با هماهنگی ایران از یک مسیر جنوبی در آب‌های عمان عبور خواهند کرد.
▪️
در دوره ۶۰روزه هیچ‌گونه عوارض یا هزینه‌ای دریافت نخواهد شد.
▪️
طرف‌ها تلاش خواهند کرد ظرف ۳۰ روز مین‌های دریایی را از مسیر میانی تنگه پاک‌سازی کنند.
▪️
پس از پاک‌سازی مسیر میانی، این مسیر بر اساس مفاد یک سازوکار دائمی که قرار است میان عمان و ایران درباره آن مذاکره شود، برای رفت‌وآمد کشتی‌ها در هر دو جهت مورد استفاده قرار خواهد گرفت.
🔻
بله، اما:
کاخ سفید، عمان و میانجی‌های منطقه‌ای سه هفته پیش تصور می‌کردند با ایران به توافق رسیده‌اند، اما ایران حملات به کشتی‌ها را از سر گرفت. این موضوع به دو هفته درگیری و وضعیتی نزدیک به جنگی تمام‌عیار منجر شد.
🔻
پشت‌پرده:
به گفته منابع منطقه‌ای، علاوه بر مذاکرات میان عمان و ایران، مقام‌هایی از قطر، پاکستان و عربستان سعودی نیز در تلاش‌های میانجی‌گرانه مشارکت داشتند.
▪️
منابع منطقه‌ای گفتند کاخ سفید به‌طور فعال در مذاکرات حضور داشت. در روزهای اخیر چندین تماس میان استیو ویتکاف، فرستاده ترامپ، عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، انجام شد.
▪️
دو منبع منطقه‌ای گفتند عراقچی در پایان هفته گذشته در اصل با توافق موافقت کرد، اما همچنان به تأیید مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، و شورای عالی امنیت ملی نیاز داشت.
▪️
یک مقام آمریکایی و یک منبع منطقه‌ای گفتند رهبری ایران روز سه‌شنبه روند تأیید توافق را تکمیل کرد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77751" target="_blank">📅 06:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlR8xRkTKJwdFdb8lqsUWJ38RtWvO6kaDW0ADvdMEb_G36A1PgbZQC77STrNaaDLuIyTeS2TwEZxR9ubEpZa7xuKeOzOjlYTM6R2u-LCkUb_02bOt4aIYMDn0b4_M4D5JaQn5gw_fg3SjOpXgh4QHvkWiwk8pbZu0__dubyq2L4R289jK0uAzhhPl2jhmYUQE8TBL9tetFumjgo33f1eXeTiFPhA4C9_8ZhR9lbJ0_JCoboYoeBWN7U9JJNC_IslA-wkhqyOh9rH09VqwuC4j4vgrxiV2fyA7Cgxl4nNlOtDxuayA3VNNsBUEBy7QTiY3pt69M4irx4DORe4IegGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77750" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=l605CzMZEkzDdC4TYW89oZCO2HEHDHEx_E64WiwkZL9FGmpetby8k81CdbOEr1YJu_c9PHZhmsviC6JqWMPgkdzBmUyNI0uQLz83gHee1cr60JZVnCf0uQqv-Ee49bOM1b5qIauGrGkrrn_rTn2Mh90aWwfFQo0KvLJmJ6tljGM9a_wBvdXrWop6okASgtsD9wvM1xE38fSXgqxqimEj247VgdASC3Ks-0R0tWpXkkpf0_B7wG8pap4YKExIpvPNpoX1KfSy0vAjA8zFE-jcMWuLkivu7woWd8vN68c8pAB2UsTiR0WS8VR9AyGESyCB8NhzDhHWuXtvWAPl0F_iJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=l605CzMZEkzDdC4TYW89oZCO2HEHDHEx_E64WiwkZL9FGmpetby8k81CdbOEr1YJu_c9PHZhmsviC6JqWMPgkdzBmUyNI0uQLz83gHee1cr60JZVnCf0uQqv-Ee49bOM1b5qIauGrGkrrn_rTn2Mh90aWwfFQo0KvLJmJ6tljGM9a_wBvdXrWop6okASgtsD9wvM1xE38fSXgqxqimEj247VgdASC3Ks-0R0tWpXkkpf0_B7wG8pap4YKExIpvPNpoX1KfSy0vAjA8zFE-jcMWuLkivu7woWd8vN68c8pAB2UsTiR0WS8VR9AyGESyCB8NhzDhHWuXtvWAPl0F_iJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت امیرعلی حیدری و سروش کرمی، دو نوجوان کشته در اعتراضات دی ۱۴۰۴ که هفته گذشته برای دومین بار به خاک سپرده شدند.
یکی از خانواده‌ها بعد از هفت ماه متوجه شد جسد اشتباهی به آنها تحویل دادند و خانواده دیگر دریافتند فرزندشان در بازداشت نیست و کشته شده.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77749" target="_blank">📅 01:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=H_asCsiZPLyQnJTObm9EML-etO5bqvILWK5pbxjNkvV8wSNx7OR0yLcFnLYbN99L5G2BhFYQJoeVsRyaGOjPqNQO-gxOSUkKM7lofSRYX2lq8h-b2Z1CKzNn_qdA5U6nx-0gx7XXR8ttGDObKOGwSSvhhTSf2rPEAskv1sKpAShxuUL75y2WvFIynBvOeIMs7NnZDE8zl6nla39mQRd0GIWUV8bZV4OI4TNMrxLEFoVUhXVzW2Roud6pqz2J-D3u0-Ypj6DLWD2Fpz_5HDY4hwo9pHzUW5dLDOgSkVCD5xNy8msMFqObMwujBTNw1aoLhvTgWnQfoHLm5uo29kXm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=H_asCsiZPLyQnJTObm9EML-etO5bqvILWK5pbxjNkvV8wSNx7OR0yLcFnLYbN99L5G2BhFYQJoeVsRyaGOjPqNQO-gxOSUkKM7lofSRYX2lq8h-b2Z1CKzNn_qdA5U6nx-0gx7XXR8ttGDObKOGwSSvhhTSf2rPEAskv1sKpAShxuUL75y2WvFIynBvOeIMs7NnZDE8zl6nla39mQRd0GIWUV8bZV4OI4TNMrxLEFoVUhXVzW2Roud6pqz2J-D3u0-Ypj6DLWD2Fpz_5HDY4hwo9pHzUW5dLDOgSkVCD5xNy8msMFqObMwujBTNw1aoLhvTgWnQfoHLm5uo29kXm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه ۱۳ مرداد اعلام کرد نیروهای این کشور تا خلع سلاح کامل حماس، از خطوط فعلی در نوار غزه عقب‌نشینی نخواهند کرد.
نتانیاهو در ویدیویی که در شبکه‌های اجتماعی منتشر شد، گفت: «ترامپ و تیم او بر این باورند که حماس می‌تواند کاملا خلع سلاح و غزه غیرنظامی شود؛ ما در حال بررسی این موضوع هستیم.»
نخست‌وزیر اسرائیل همچنین با اشاره به طرح پیشنهادی آمریکا افزود: «آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم، چرا که پیش‌نویس ما نبود. ما پاسخ‌های خود را ارسال کرده‌ایم.»
او تاکید کرد که نظرات و پاسخ‌های تل‌آویو پیش از رسانه‌ای شدن این موضوع به طرف آمریکایی تحویل داده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77748" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awuKa-5wwJ1RxMNOx7DC2PZDPjnPqwruXsIBVYdfKtjYs1JVR9SLEy7dhIXAU3h8DyLU7bxrnWu2RtxyXfMHPhSu1JBZzxd5STfyjcsMu7wbG9wOdZoUBmI6SW_ph3Be1dKI3ZsOZE_uFlXc5f0Tzlil7ZGPVIChmBlwmCArfR8On6VMQPSiGw5WF3zwZiyAppslEGVxrFwy1htyh5XcHcvK9AnFUoioQ4BJiox9u1M75SgqKQtIXBlr1nZsLdLkG9gB7xPE7w_b1fqOJZCrg4-1JqmwxN-VNgsGwdGzQ_1Hyq1r83R1xUx2hyXq30w8VC9QB1GumfeiP5JA_JzhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی قطر گزارش داد تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه در تماس تلفنی با دونالد ترامپ، رییس‌جمهوری آمریکا، آخرین تحولات منطقه، به‌ویژه تلاش‌ها برای کاهش تنش میان آمریکا و جمهوری اسلامی و نزدیک کردن دیدگاه‌های دو طرف را بررسی کرد.
بر اساس این گزارش، ترامپ از نقش قطر در حمایت از تلاش‌های دیپلماتیک و تسهیل گفت‌وگو میان طرف‌ها برای تقویت امنیت و ثبات منطقه قدردانی کرد.
امیر قطر نیز بر اهمیت ادامه گفت‌وگو، استفاده از راه‌حل‌های دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم میان تهران و واشینگتن تاکید کرد. او همچنین خواستار حمایت از ابتکارهای بین‌المللی برای مهار تنش‌ها شد.
دو طرف همچنین درباره شماری از موضوعات مورد علاقه مشترک گفت‌وگو و بر ادامه هماهنگی و رایزنی درباره تحولات منطقه‌ای و بین‌المللی تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77747" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5mFzQDAB6-9ihnZU42Ouf7lIKnjo9Ka91u1aJiPgJcDl6Ko6ARgkGLewQkkLG0RVdD4X4lpqKaAcpmZklFSsNRrQtWDvIRm-Ys7eNrdoWmYoTBq19Zy0OUVuC5I0PP_EvPaR3HbT3yGOh-fuJZ4JQealuJf6jOBgMhIXbDGle7YW1ppo0hq6iWLXCegQR0ZXzGPCg7Wm39GBe9VVEhkH2m8X3rq8p2R09lJsIdm1tNfWEv-a4F-Jx0MLxoVjOknj8wVL7mafhyZ2noPHdViNr5A_c_Xe0LWX_weGxWiPuYfi5maHBiBgTjPJ-xA8JJLgBtyhhATfJbNoHfakGphAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشتیرانی هند روز سه‌شنبه ۱۳ مرداد اعلام کرد که یک پرتابه به یک کشتی با پرچم هند در نزدیکی یمن اصابت کرد که باعث واژگونی و غرق شدن آن شد.
ساربانا‌ندا سونووال در پیامی در شبکهٔ ایکس نوشت که اما هر ۱۴ ملوان حاضر در کشتی، از جمله ۱۳ تبعهٔ هند، توسط گارد ساحلی یمن نجات یافته و به بندر مخا منتقل شدند.
وزارت خارجه هند نیز اعلام کرد که این کشتی تجاری به نام «ام‌اس‌وی فیض نور علیا» روز ۱۳ مرداد در دریای سرخ و در سواحل یمن غرق شده و این وزارتخانه در حال هماهنگی با مقام‌های یمنی دربارهٔ این حادثه است.
پالایشگاه‌های هند از زمان حملات حوثی‌ها به چند نفتکش سعودی، به دریافت محموله‌های نفتی خاورمیانه به‌صورت تحویلی روی آورده‌اند.
تردد در دریای سرخ در نزدیکی سواحل یمن به‌دلیل اقدامات حوثی‌های همسو با تهران مختل شده است. حوثی‌ها با ایجاد اختلال در صادرات نفت عربستان، دامنه درگیری میان آمریکا و ایران را گسترش داده‌اند. پیش‌تر نیز عرضه نفت از طریق تنگه هرمز مختل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77746" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u_pAx6x71LH8jGQQf35DCAnCrq-yAD9WBNj6ksWgL2SYV1mhd7dD0X2F4hKE6Ml8JUpVEZ62PFHLpcCJ-6Bz4-wJFe3RYYyR4rtbyKlANvpk4gTiOO52am5f2xPqfX0Q8la7gZDEptuyW5xrIhbe2Jz0N1_odUYCHG7cT_Oefm28wENR_y7CcTPJ1Nl8N22DwYwd9U0BTvDk2i92wM7XE2LmpvXTRXdJUyxHmAuNE20c_yltBwy8cektJOpGsWkF9mTAEtDjt4M0jGw18Dzus8ekXGUwhj9Yie119Z3t0LubTcoQccK1tCsbVQkvt_5BXfinFLMqgii9R6vAhQ3rUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eHVtsaPzeOVBwzTrl_YUMnuBv5WGykkWZj1xV_gU3bthtbsbZeskeUNg2kzuPxX1xOs-nWFLKhiCjvfefVfyF8ds_gDBP5W5DVqu17azYdU7R7bTwcdxxkGcBuCeo0c7jm2ThnFS75eu9YzjbSc7PB3MM-_lTGPD3xo5MFOuQa0SbtDfFqil0rGluUH_qAQxKUltyZSgW9JIxcWEjlTefMQMd_McwUxu2Fs5mBctPwmKnFgrgtlORds_h3oIXzBvT28by4IxJ7uRWm-K93OHjJ8L4bt5dPpwtII8hgObwYo03tx72pMmk8PAUt3pCNgsHsRzUjOqyLkdS4TFOnmk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fBOwskx0XOSkNsaLyoHypzH4HROwIt50hPhf3C4Tnv_7RiywYkDOKWSal6t3BEIlCzk9-kg2yI0Ey1TxLlD3kXid2VMH75s-bStzN2dSmayaYJbQrq0e4CsHwufuXNZXtJJzfCdBXdEqfEmCZf35U2h7dPwlNBPgvtX10_hhxTZi8ITtFBzilh8YQ7horNkzLn7wH5OwC2JZrtze3-7reNn1RjJjqPyo00EO14ffXK751TmwdCRtqHKb2Udt37yHbtCjTTJVUXkJK8djDWqgvx2Y2Nxczt34qkOVTmDBGkFaKJl6dhYmOiqsNq6Ocdf252XHt6oZOkvnCUJvqmAFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rQ35UjNTmFLk3IC18rt0KS5P74XX0RHTN5B3y_vzDjEcNvY8imOfDRMsM_p7XBQQbQksRURuMHtScNuQWr1OI1Y2UnBYYz7WMWUNjtd6h_Jj-W6EBxaT6LYTFEe_7uLbWI0GlYqtbNI03PVT-5wHhd6sDGvtL-DOlXSbYvXJoXlm6ygf4upBGGlal8JGLe_g7dJt48Y9u8t0lHUToHiZD0StiNGddx_BvQc_II-AW1ievA2SLHrkHj1HMR6hAT28BcVnJ_D_vd9pSI_WxPaRWMm2J-iyVzN9vIlr7si7kxII3diG7l1g5N9WPN3jtMfctYwFVnJKLGUlwQ_AQu0xVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=KImLsfTjV9cAD4k6GDI6plqQXNZJ8xynSzh905q1o0sMrqp5RcCHANvdvkHGDgWWlEZDIxXjgrh_kBhyifXJ5T4yfMLcS8aVSV9V51mJQRPQ57sMctgM9ZWrkCtN0H4cXHagN4fOA8S6XIXxLD8FAshm2m1CndKLDIJPPwfZZ_db-JQESNxyOc3J36dfK6EOglERxr_bWIEvePDWJb-XoQWM3QxMDE4eT2lbdxhA6DT_DWRYvracDYHLgpfxJcKL2yg4EA5G_JFPUK2zi6Oyg0xRFiwbJTzBI9NeyF_Huj1p_bFB4-S5vXiBWtg0_zwsme63x-z4z2E_xFQ96Sa6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=KImLsfTjV9cAD4k6GDI6plqQXNZJ8xynSzh905q1o0sMrqp5RcCHANvdvkHGDgWWlEZDIxXjgrh_kBhyifXJ5T4yfMLcS8aVSV9V51mJQRPQ57sMctgM9ZWrkCtN0H4cXHagN4fOA8S6XIXxLD8FAshm2m1CndKLDIJPPwfZZ_db-JQESNxyOc3J36dfK6EOglERxr_bWIEvePDWJb-XoQWM3QxMDE4eT2lbdxhA6DT_DWRYvracDYHLgpfxJcKL2yg4EA5G_JFPUK2zi6Oyg0xRFiwbJTzBI9NeyF_Huj1p_bFB4-S5vXiBWtg0_zwsme63x-z4z2E_xFQ96Sa6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت ایالات متحده ممکن است تا روز چهارشنبه برای بازگشایی تنگه هرمز با ایران به توافق برسد؛ توافقی که به گفته او می‌تواند قیمت انرژی را تثبیت کند.
او روز سه‌شنبه در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «ما با ایرانی‌ها در حال مذاکره هستیم و فکر می‌کنم این احتمال وجود دارد که امروز یا فردا برای بازگشایی تنگه و حرکت به سوی وضعیتی عادی‌تر در این درگیری به توافق برسیم.»
بسنت در پاسخ به این پرسش که آیا چنین توافقی به ایران اجازه خواهد داد از کشتی‌های عبوری عوارض دریافت کند، گفت: «فکر می‌کنم منظور، آزادی رفت‌وآمد خواهد بود.»
@
VahidHeadline
مارکو روبیو، وزیر امور خارجه آمریکا، روز سه‌شنبه ۱۳ مردادماه اعلام کرد هدف نهایی مذاکرات با ایران، دستیابی به توافقی برای خلع سلاح هسته‌ای این کشور است و گفت توافق کنونی که تمرکز اصلی بر آن قرار دارد، به تضمین عبور امن کشتی‌ها از تنگه مربوط می‌شود.
روبیو با اشاره به ادامه تردد کشتی‌ها و انتقال نفت از تنگه گفت: «همین حالا کشتی‌ها از تنگه عبور می‌کنند و صادرات نفت ادامه دارد. تنگه باز است.»
او افزود: «خلع سلاح هسته‌ای ایران توافق نهایی است. توافق فوری، که اکنون بیشترین تمرکز بر آن قرار دارد، مربوط به تنگه است.»
روبیو همچنین گفت مذاکراتی میان عمان و ایران درباره فراهم کردن امکان عبور امن کشتی‌های بیشتر از تنگه در کوتاه‌مدت در جریان است که آمریکا نیز در آن دخیل است. به گفته او، این مذاکرات پیشرفت کرده، اما هنوز به نتیجه نهایی نرسیده و واشنگتن امیدوار است به‌زودی به جمع‌بندی برسد.
@
VahidOOnLine
قطر اعلام کرد تلاش‌ها برای دستیابی به راه‌حلی دیپلماتیک میان ایران و ایالات متحده ادامه دارد، اما هنوز توافقی حاصل نشده و هیچ مذاکره مستقیمی میان دو طرف برنامه‌ریزی نشده است.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، روز سه‌شنبه ۱۳ مرداد ۱۴۰۵ به خبرنگاران گفت رایزنی‌های دوحه با ایران و آمریکا همچنان ادامه دارد. به گفته او، این رایزنی‌ها بر دستیابی به «راه‌حلی کوتاه‌مدت» متمرکز است تا زمینه ازسرگیری گفت‌وگوها و احیای کامل روند میانجی‌گری فراهم شود.
اظهارات سخنگوی وزارت خارجه قطر یک روز پس از آن مطرح شد که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود مذاکرات با تهران در جریان است و ایران با «آخرین فرصت» برای دستیابی به توافق روبه‌روست.
ترامپ گفته بود این مذاکرات به درخواست ایران، عربستان سعودی، امارات متحده عربی و قطر انجام می‌شود و افزوده بود: «این آخرین فرصت آن‌ها برای امضای یک توافق خوب است.»
در مقابل، مقام‌های جمهوری اسلامی تأکید کرده‌اند که هیچ مذاکره‌ای با آمریکا در جریان نیست و گفت‌وگوهای کنونی ایران تنها با عمان و درباره تنگه هرمز انجام می‌شود. تهران همچنین اعلام کرده است که این هفته هیچ نشست مهمی برنامه‌ریزی نشده است.
@
VahidHeadline
قیمت نفت روز سه‌شنبه ۱۳ مرداد پس از اظهارات مقامات قطر و وزیر خزانه‌داری آمریکا که امیدها را برای حل دیپلماتیک مناقشه خاورمیانه و بهبود عبور نفتکش‌ها از تنگه هرمز افزایش داد، حدود ۴ درصد کاهش یافت و به پایین‌ترین سطح خود در سه هفته اخیر رسید.
@
VahidOOnLine
—-
ترامپ هم دوباره چندین پست پشت هم منتشر کرد که یکیش لینکی است مربوط به مطلب ۲ روز پیش
breitbart
با تیتر:
ترامپ: «توافق قریب‌الوقوع است»؛ مذاکرات با ایران درباره خلع سلاح هسته‌ای و هرمز دوشنبه از سر گرفته می‌شود
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77740" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ai5TQzMZNNoZlt-48sQI7QJy8ld-1oeZBwemr4esie42BxTPER_d4T0FgLr23uEEzwofE-Vsy4PnwBgbtoLxwL6DOo-U4BFjW3nE4nOOCrG2DhaVHkSgC6CJGCb6D2y9cJ9XD4JJ-FHSv0t6xi3yJqRJqisg0cI3mcLVzXWP2DYptjzDm44pSc6NXObFPJnaEwNpEGl3BJ2CcCyIuqhMMxYRwhEvUbUnGRTgbORc1HbzCCdOfbKUtzwAHh1g2EYmaMSMooLxYb3E4XrpQ4H0wOlp3-DU1gtUlnBkrYIh4x0rZdoHBnL0go_sfxfOQhd-htQzGQY0iTco-290S_Lszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=F_2D7ac1Lexd_HMlrSu2S1Vgj4rGQfaqe-QcvbsSRAsVYdUvIfADT1pvP8PzY_TcpeplOmc-VxtizSwE_-njWJSwG4ZA6AWR7CxnP0d3Wu7GpjOySoBz5dLxdsZ7AsHAjvK6uXteBiooQPf2is4B-UDdujN9wtCU23LZCMwI9Nz9DcHwWp5ETS8FWrHi6mwzlIlGTM2dIzFobyEghMjIqTp9EkZLGKNTjMoqrAxtMZenvJ7JHNJvLfZR2EBzrukc3T0YvTVdFEAEafJnPK_LTBnzFI61nibcMliddSXi3jrCHGCHkndpgMNAABZHjCsu4oqN53liTixYWrgXjvHmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=F_2D7ac1Lexd_HMlrSu2S1Vgj4rGQfaqe-QcvbsSRAsVYdUvIfADT1pvP8PzY_TcpeplOmc-VxtizSwE_-njWJSwG4ZA6AWR7CxnP0d3Wu7GpjOySoBz5dLxdsZ7AsHAjvK6uXteBiooQPf2is4B-UDdujN9wtCU23LZCMwI9Nz9DcHwWp5ETS8FWrHi6mwzlIlGTM2dIzFobyEghMjIqTp9EkZLGKNTjMoqrAxtMZenvJ7JHNJvLfZR2EBzrukc3T0YvTVdFEAEafJnPK_LTBnzFI61nibcMliddSXi3jrCHGCHkndpgMNAABZHjCsu4oqN53liTixYWrgXjvHmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوها از کانال‌های غیررسمی حکومتی
درگیری میان حامیان جمهوری اسلامی و مقلدان صادق شیرازی، از مراجع تقلید منتقد جمهوری اسلامی، در جریان مراسم اربعین در کربلا به بازداشت ۱۴۰ نفر و مجروح شدن ۵۴ نفر انجامید.
شبکه تلویزیونی «اشعائر» عراق، رسانه نزدیک به "آیت‌الله صادق شیرازی"، صبح دوشنبه ۱۲ مرداد ویدیویی از این درگیری منتشر کرد.
بر اساس گزارش این رسانه، گروهی با در دست داشتن تصاویر علی و مجتبی خامنه‌ای و پرچم‌های «یا لثارات الحسین» و «یا لثارات الخامنه‌ای» مقابل دفتر آیت‌الله صادق شیرازی در کربلا تجمع کردند و علیه او شعار سر دادند.
این رسانه می‌گوید حامیان علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، و فرزندش مجتبی خامنه‌ای هنگام عبور از مقابل دفتر صادق شیرازی این شعارها را سر دادند که با واکنش هواداران و مقلدان این مرجع تقلید روبه‌رو شد.
به گفته کاربران شبکه‌های اجتماعی، این درگیری ابتدا با مداخله پلیس عراق متوقف شد، اما در ادامه میان حامیان جمهوری اسلامی و نیروهای امنیتی عراق نیز تنش و درگیری رخ داد و پلیس عراق در نهایت با استفاده از قوه قهریه به آن پایان داد.
بر اساس گزارش‌های منتشر شده، در جریان درگیری مقابل موکب منتسب به آیت‌الله صادق شیرازی، ۱۴۰ نفر بازداشت و ۵۴ نفر مجروح شدند. این آمار تاکنون به‌طور مستقل تأیید نشده است.
همچنین در برخی گزارش‌ها ادعا شده است که حسین ستوده، مداح حکومتی، از چهره‌های حاضر در این تجمع بوده و تلاش داشته این مراسم را به موضوعات سیاسی پیوند بزند.
"آیت‌الله صادق شیرازی" از منتقدان نظریه ولایت فقیه است و رسانه‌های جمهوری اسلامی او و جریان منتسب به وی را با عنوان «شیعه انگلیسی» معرفی می‌کنند. او ولایت فقیه را محدود به امر قضاوت می‌داند و با تفسیرهای جدید از اسلام و مذهب تشیع مخالفت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77735" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DykMRve6cz9ahyqbO4A7_MFAZCwUkidcUL7Yw-diqQMRPsLkAKG8r0UUYzFgQrQ1L50Zr2rmW18guLY3CF5D1kxontVZfmEkb_s6R3x44fmH9fHELcmd32b8yiigrjAaeGtXjx994v7B-bkp8vqNupPhU1Hsh0eybK47HJFD-oIJsWWmZJzUx8GzLMwakOqnm1g-ctHfRsX2JOsvg-ubm0mvL7EElG5-7E20EsG-UXovWF7FHVYnSgSo9FvJO0QgZ_PiQfbbYSQxPqrl0oAFjjsozDve68BmStG7pESj8N3G87yfSLqoy-tJp3_rXMqQqUH6h-E1kZ6RNMkhsTLLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ukI5u_vBbfvWWEf2UXZ4r7-jMN18v404n0R-lOk6IjNOthsMCp4B_HEqpXvJp0bzrOXkZVluAVc6LHvWc7CwEHdDDe8Ku9Pgp_WKiI7WhN5mVFnwnyuSZbH95wjnWj223BZet9ShC2RLVfJHy2tdZjOvMWnwvUe2TYogAym4Dd9BUICiBaHnqWeAxWWQz9_ZRgHHo-q9eZpT4HHl0QQPCl3JYnVqd-Ff1kr-es6k0Lnh6JuZe-7YG4PpOte_x6czf_xO0xRaR5hPDQ-nNdbC3bzJR3vHpP-aL_oRHj34hNHu2HswZpmbMj54HQ104RQke3EJPsHp3Ins8Ykudo-XrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شرکت نفتی آرامکوی عربستان سعودی روز سه‌شنبه اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال جاری، هم‌زمان با افزایش قیمت انرژی بر اثر جنگ خاورمیانه، ۴۴ درصد رشد کرده است.
بر اساس گزارش مالی آرامکو، سود خالص این شرکت از آوریل تا ژوئن به ۱۲۲ میلیارد و ۶۰۰ میلیون ریال سعودی، معادل ۳۲ میلیارد و ۷۰۰ میلیون دلار، رسید؛ در حالی که این رقم در دوره مشابه سال گذشته ۸۵ میلیارد ریال بود.
امین ناصر، مدیرعامل آرامکو، گفت این شرکت با وجود اختلال بی‌سابقه در عرضه نفت از مسیر تنگه هرمز، توانسته است با استفاده از خط لوله شرق به غرب، ظرفیت‌های ذخیره‌سازی و پایانه‌های صادراتی، فعالیت خود را ادامه دهد.
اعلام افزایش سود آرامکو هم‌زمان با انتقاد دونالد ترامپ، رئیس‌جمهور آمریکا، از سود بالای شرکت‌های نفتی صورت گرفت. او گفت این شرکت‌ها به‌دلیل کمبود نفت ناشی از جنگ «بیش از حد پول درمی‌آورند».
@
VahidHeadline
شرکت بزرگ انرژی بریتانیا، بی‌پی (از بزرگ‌ترین شرکت‌های نفت و گاز جهان)، اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال ۲۰۲۶، هم‌زمان با افزایش قیمت انرژی در پی جنگ آمریکا و جمهوری اسلامی، بیش از دو برابر شده و به سه میلیارد و ۹۱۰ میلیون دلار رسیده است.
سی‌بی‌اس به نقل از خبرگزاری فرانسه نوشت پنج شرکت بزرگ انرژی غربی، شامل بی‌پی، شورون، اکسون‌موبیل، شل و توتال‌انرژیز، در مجموع نزدیک به ۴۷ میلیارد دلار سود خالص در سه‌ماهه دوم سال ثبت کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77733" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hEjdlY43tdbcxKjdovI3-SS6-3uVL4expJZ5UqlG_F5yR3x12eDfrqL1ISfvO7YYLCr0SSj94zwkPIsxoP-udA3gJVfZOFmURgrpH3A8prKdmVOokkASHFPVQV9tcRfh2IptUOGbWDnyJlgxcGynCnScrjwsnA2mfcqHxDutaqbbY_2rnxb9dmy6QavefxvUVkpTsOJuxMBy6FcS7Q0woe9CrK_8RqIYtgEs0PoT0nXeigB6Dkvi4nNUAfPAPuo8WQcOCi-cAYMUg9x7cbAE-BA4t1lyD8vJOpO2KDcY4_BzfraQHeLCG-lq26QqNmjf9yqBCXWIV37O0iqOuknTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DmojMl975ahxpHtRlvT_S2t8TO_1nZ_Yq9k2u0XzA7a4PlmHZz8ei7sI6J3VLMjr9eErsLpB1SmOxqsq9Z8W4b14b-KvgqFPtYabs4VMUJjRHJlbcazomk2ce70xdd8XbECSGpcpeom0izFbPLITUaeP7CrgxsaXHEAQR99EemOjOx-uXNCGbdCGDLHaf2KVqCMMHb9Tz33cNx-Ua-4t9jyHMsz5buRQdHgag8DNyJzcklf2BOGOWivWYz4JyE44ASbi1wV5evMst80ArfIxpxYj5hT5dCytPH1e4_k7OOguBeu2Q9QdYZP2czgpFvHN1_d6Ke3XI0VgudqyleRPPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=FSzjq6BFhmLRfHu690xR2lHvT9PC2Q0hnNYVzpfTXgkZp6tS-xSLKhwqNz1QOOKOvPBP6KR5UkaHiQthOQPvWS-9l9Gc1pffnkldVa2r0Iig-SPtiys7Nbb9f5IQd-noVWEK2nmw0Yv8b4S_EpmqfZoQmcmqMk3Y0A8eXCkQrLxaTYjLdvDhJ_O-S00XvzXNqf3RGWDrsc9J1Y1Cop1xzG_1nKSMuFZRgyk0Z6xatdCBoRsOmO0sefTEZXOG6TDBsxsohpl2W_2Bov6l3BbVZYuYR_7kFA3fZhWrNQIJVF8SPUj_HFdhmwjY9MMLCkPPCVRAzLqNLCnvAJbGTQ-cCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=FSzjq6BFhmLRfHu690xR2lHvT9PC2Q0hnNYVzpfTXgkZp6tS-xSLKhwqNz1QOOKOvPBP6KR5UkaHiQthOQPvWS-9l9Gc1pffnkldVa2r0Iig-SPtiys7Nbb9f5IQd-noVWEK2nmw0Yv8b4S_EpmqfZoQmcmqMk3Y0A8eXCkQrLxaTYjLdvDhJ_O-S00XvzXNqf3RGWDrsc9J1Y1Cop1xzG_1nKSMuFZRgyk0Z6xatdCBoRsOmO0sefTEZXOG6TDBsxsohpl2W_2Bov6l3BbVZYuYR_7kFA3fZhWrNQIJVF8SPUj_HFdhmwjY9MMLCkPPCVRAzLqNLCnvAJbGTQ-cCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در تیزر تبلیغاتی حاوی بخشی از سخنانش که قرار است در چند قسمت و از امشب به وقت محلی از تلویزیون ایران پخش شود، ضمن رد گزارش‌ها درباره استعفایش گفت: «استعفا نخواهم داد و خواهم ایستاد. اینها می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و اینها یک چیزی می‌گویند.»
این سخنان یک روز پس از انتشار کلیپی پربازدید از سخنان محمدباقر خرازی، دبیرکل تشکلی موسوم به «حزب‌الله ایران» که برادر همسر مسعود، برادر مجتبی خامنه‌ای، رهبر سوم جمهوری اسلامی ایران منتشر می‌شود که او درباره «۲۸ بار استعفای پزشکیان» و «تهدید مجتبی خامنه‌ای به پذیرش استعفای بعدی» سخن گفته بود.
این سخنان واکنش‌های چهره‌ها، جریان‌ها و رسانه‌های حامی و منتقد دولت را برانگیخته است؛ از جمله حمید رسایی که از آقای پزشکیان خواسته بود برای راستی‌ازمایی سخنان محمدباقر خرازی استعفا کند.
مجتبی زارعی، نماینده عضو کمیسیون امنیت ملی مجلس ایران در واکنش به طعنه آقای رسایی نوشت: «از ۹۰ میلیون ایرانی فقط یک شاهد برای تهمت خرازی به امام سید مجتبی شهادت داد ؛ سرکرده شریان!»
@
VahidHeadline
حمید رسایی نیم‌ساعت پیش، یعنی پس از انتشار ویدیوی پزشکیان هم تاکید کرد که هنوز تکذیب نشده:
بعد از اینکه سیدمحمدباقر خرازی درباره نحوه برخورد رهبری با استعفای پزشکیان - که تاکنون تکذیب نشده - ادعایی کرد، اطرافیان رئیس جمهور برخوردهای متفاوتی و گاه توهین آمیزی داشتند.
تصور کنید اگر وی ادعایی برخلاف آنچه نقل کرده به زبان آورده بود (مثلا رهبری به پزشکیان گفته شما باید محکم ادامه بدی) چه اتفاقی می افتاد:
rasaee
👈
بعدش، یعنی دقایقی پیش، این خبر منتشر شد:
دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با انتشار بیانیه‌ای، گزارش‌ها درباره هشدار به مسعود پزشکیان در خصوص استعفا را تکذیب کرد. این بیانیه یک روز پس از انتشار ویدیویی از سخنان خرازی منتشر شد که در آن مدعی شده بود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده و مجتبی خامنه‌ای اعلام کرده در صورت تکرار این اقدام، استعفای او پذیرفته خواهد شد.
@
VahidHeadline
نسخه منابع حکومتی:
دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب:
بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی و ادای احترام به روح بلند رهبر شهید انقلاب به‌اطلاع مردم شریف و مبعوث‌شدهٔ ایران می رساند در روزهای گذشته برخی نقل‌قول‌ها از رهبری معظم انقلاب اسلامی در فضای مجازی منتشر شده که متاسفانه زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه است.
بر همین اساس برخی نکات را درباره اخبار و مطالب مربوط به مقام معظم رهبری بیان می‌داریم.
🔹
مرجع رسمی انتشار پیام ها، اخبار و مطالب مرتبط با آیت‌الله سیدمجتبی حسینی خامنه‌ای، پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و یا پایگاه حفظ و نشر آثار رهبر انقلاب است و هرگونه مطالبی که خارج از این چهارچوب منتشر شود، فاقد سندیت و صحت است.
🔹
رهبر معظم انقلاب اسلامی در پیام‌های خود از جمله در پیام اخیر بر حفظ اتحاد مقدس و حفظ حرمت مسئولان دلسوز و خدمتگزاران نظام اسلامی به‌ویژه دولت محترم تأکید داشته‌اند. مطالبی که برخلاف توصیه‌های مؤکد رهبری، موجب انشقاق و دودستگی در جامعه و زمینه‌ساز نسبت‌های نادرست به مسئولان محترم می‌شود، در جهت اهداف بدخواهان و دشمنان قسم‌خوردهٔ ملت ایران است.
🔹
بر همین اساس مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور محترم مطرح کرده از اساس کذب و خلاف واقع است.
روابط عمومی دفتر رهبر انقلاب اسلامی
۱۳ مرداد ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77730" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/naeOICYgqOyikaJ-05DnNKkrIzuHKpFtqb8WgBo08gP4kXu5iYtOmS4M3YEq5B6EYwOVYisWyocmMcFh2X5i8edG_9ZBtJ4eX-UOBc3zriPkhdaSvINuqStGvFso73eNXQEYJlzbRwD_MkAzg0yBf1Mzmx1tiR8DuZjH22y6n4XqyEJNY67evAqbdrP6NugsTl9ZONuN0ReQLahTCUb9NQVM4KJ4M9VjJQkNBNnRItC0bH-vct3MJfyMc4FWS6NNttx67MnX0-RdSiTj5H9-HEiCFaKh5Z9-BO9bu_aOCQ5NtOtJWE4yS5eKeq7-Hfyhq0v37Vihu6Q3iV3roRqqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساکنان شماری از روستاهای جزیره قشم حدود چهار ماه است به آب لوله‌کشی دسترسی ندارند و برای تامین آب مورد نیاز خود ناچار به خرید تانکرهای چندمیلیون‌تومانی یا استفاده از منابع نامطمئن شده‌اند.
براساس گزارش میدانی آوش، یکی از ساکنان روستای طبل گفته است: «چهار ماه است شیر آب خانه‌مان باز نشده. حالا فقط با تانکر زندگی می‌کنیم. من توانستم سه میلیون تومان بدهم و آب بخرم، اما خیلی از روستایی‌ها حتی همین پول را هم ندارند.»
پس از آسیب‌دیدن یکی از تاسیسات آب‌شیرین‌کن در جریان حملات ماه‌های گذشته آمریکا به نوار جنوبی ایران، وضعیت تامین آب در بخش‌هایی از جزیره به‌شدت بحرانی شده است. او گفته آب لوله‌کشی تقریبا قطع شده و مقدار آبی که با تانکر توزیع می‌شود نیز پاسخ‌گوی نیاز ساکنان نیست.
این اظهارات در حالی مطرح شده‌اند که عباس علی‌آبادی، وزیر نیرو، ۲۹تیر۱۴۰۵ و در جریان سفر به هرمزگان گفته بود همه آب‌شیرین‌کن‌های منطقه در مدار بهره‌برداری قرار دارند وهیچ‌یک از جزایر کشور با کمبود آب مواجه نیست.
او همچنین گفته بود با وجود آسیب‌دیدن زیرساخت‌ها در حملات اخیر، خدمات آب و برق پایدار مانده و شرایط مدیریت شده است.
عبدالرحیم رضوانی، نایب‌رییس شورای اسلامی بخش مرکزی قشم  گفته است ساکنان برخی روستاها بیش از سه ماه برای وصل‌شدن آب انتظار می‌کشند و پس از آن نیز تنها چند روز به آب شبکه دسترسی دارند. به گفته رضوانی، قیمت یک تانکر چهار هزار لیتری آب به حدود یک میلیون و ۴۰۰ هزار تومان رسیده است.
در همین حال، یکی از ساکنان قشم گفته است برخی خانواده‌ها که توانایی خرید آب ندارند، برای مصارف روزمره از چاه‌هایی استفاده می‌کنند که از سالم‌بودن آب آن‌ها اطمینان ندارند. او به نقل از یکی از اهالی گفته است: «آب تمیزی نیست؛ حتی حیوان داخل آن می‌میرد، اما به‌هرحال آب شیرین است. برای خوردن استفاده نمی‌کنیم، اما برای کارهای روزمره مجبوریم همین آب را به خانه ببریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77729" target="_blank">📅 18:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSsz4xQ0Th88QG-5qDDcZsb8KI6jpEApQqSpd8ACFj7-krw6hvwOJu-z1Sr01IGY_u5THuhZf3_QipyvxPXDxhhSbbkpP7h2Jy5auHc-V0jH-tc2OpCs45mgegRVf43g2cbSufr2Qn0ju4HLJ51ksqeN3yd83QSGBrRj-pM-UMm0LFSepoWTFNt5o0NvepVTXhjJr63qIqJTd7YWSwhliGjGzRYEkfr0-DHWjtXbiv0Ni68mrCnwv0oB6E8vD-9fwg0aL3XeCtK2gsphUzL0cXIliLG-_mUVSuzK65CzecFoXY8q1htvLNkd8qNaLe5wz7eHLvyFC5HlZL6NX7mNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه موج پلمپ واحدهای صنفی و مراکز فرهنگی در ایران، در روزهای اخیر، دست‌کم سه مجموعه فرهنگی و صنفی در بابل، مشهد و تهران با دستور مقام‌های قضایی یا نهادهای ناظر پلمب شده‌اند.
هرانا خبر داد مجموعه «شهر کتاب» در شهرستان بابل، با دستور قضایی و به‌دست اداره نظارت بر اماکن عمومی پلمب شده است.
هم‌زمان، گزارش‌ها از پلمپ «کافه معماری سکنج» در مشهد حکایت دارند؛ فضایی تخصصی و فرهنگی که محل فعالیت معماران، هنرمندان و دانشجویان بود. تاکنون درباره علت پلمپ این کافه اطلاعاتی منتشر نشده است.
مجموعه «خانه ارغوان» نیز اعلام کرده است که به‌دلیل «پلمب موقت از سوی مراجع ذی‌ربط»، فعالیت خود را تا رفع محدودیت‌ها متوقف می‌کند. این مجموعه در خیابان فرشته تهران فعالیت داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77728" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAzsjZnkntPSiLZ61b6tLqk0_nZlg89XuXfGQl3tJi21Lcq_LZAOKS1cP8ObWHY6q-wC0WiBsg21A9TlVpBPlqWP82gNqcEIOiH-MiHOjURD705G8xeX-93F48qCPBx0MIe25xgbJXP7QN0X179z7ufWVhQ5LEI_6JnxdUAK7CRo4dRabGxh2NpOsnLjF6NTJbC4ZeeOL2C2hzuAjcjj6w29PB74HGmtLYQ8NwloHh5W74NBmcV6M4mRM08ZTAyd2UDjj4N3A8ADRzrGmn5sPqCplbTUWlVowqVDO-KvEIBdo9N43V0xWacYnA4Dx64XwinsAFDSPIn6KctYx2IvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سازمان حقوق بشر ایران» اعلام کرد «مهدی روشنی»، معترض بازداشت‌شده در ارتباط با اعتراضات ۱۶دی‌۱۴۰۴ در شهرستان ملکشاهی، با اتهام‌های امنیتی به اعدام محکوم شده است.
این سازمان روز دوشنبه ۱۲مرداد۱۴۰۵ گزارش داد مهدی روشنی روز یکم بهمن‌ماه در منزل خود بازداشت و به تهران منتقل شد. به نوشته سازمان حقوق بشر ایران، او پس از بازداشت، دو ماه در بی‌خبری مطلق نگهداری شد و برای گرفتن اعترافات اجباری تحت شکنجه‌های شدید قرار گرفت؛ اعترافاتی که به گفته این سازمان، مبنای صدور حکم اعدام قرار گرفته است.
سازمان حقوق بشر ایران به نقل از یک منبع مطلع مدعی شده که یکی از افرادی که مهدی روشنی را پس از بازگشت از تهران دیده، آثار گسترده شکنجه را بر بدن او مشاهده کرده بود.
این فرد گفته است: «اگر بدنش را می‌دیدید وحشت می‌کردید. جای سالمی روی آن نبود. پر بود از آثار شوک الکتریکی و شلاق، اما حاضر نشده بود اعتراف کند.»
بر اساس این گزارش، مهدی روشنی اواخر اردیبهشت‌ماه ۱۴۰۵ با تودیع وثیقه آزاد شده بود، اما حدود دو هفته بعد بار دیگر نیروهای امنیتی او را بازداشت کردند و از آن زمان تاکنون در بی‌خبری مطلق به سر می‌برد.
این منبع همچنین گفته است خانواده مهدی روشنی تحت فشار قرار گرفته‌اند و به آنها هشدار داده شده درباره پرونده او سکوت کنند. به گفته این منبع، حدود یک ماه پیش به خانواده او اطلاع داده شده که وی با اتهام‌هایی از جمله قتل «احسان آقاجانی»، مامور پلیس، به اعدام محکوم شده است.
بر اساس گزارش‌های منتشر شده، احسان آقاجانی در جریان اعتراضات ۱۶دی‌ماه در شهرستان ملکشاهی کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77727" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NLmeyjQe1VbGhPRdgcs0_0mZozSN_uKEvxCMy23ITzml3Px8rFcFPJ3t6i8GQtbQDR8VFmqQu9zNEIsVc3FjagfPhGzbfBSD0TmU67PMuBBchlklZKPLTH4v-2ei2TxUcAUjpJRT2LK7yEr9gy7y5PiEsV9lvrghaSj1v9AkSU1-bulEBuGy_9Z1l10x_iF7RKJdof1f61y-_v2ITFFGXBuUB13JVpNfzSdEKh9GLTD4afAYX1EZ5j-O2Q6nuYGwnbdWpo40lpipTJpdADwFSKAgzIrvMa1xhsqzS5qV-5ACnyJdb6aZMfhAazF_KIdvdIEKRXbIUgyZTio24eWE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
آپدیت: برگشت
پیش از آپدیت:
نرم‌افزار پیام‌رسان «تلگرام»، روز دوشنبه، به‌طور ناگهانی از فروشگاه «اپ‌استور» شرکت اپل در سراسر جهان حذف شد.
بر اساس اعلام کاربران شبکه‌های اجتماعی، جست‌وجوی نام تلگرام در اپ‌استور با هیچ نتیجه‌ای همراه نیست و
صفحات رسمی دانلود
این برنامه با «خطای ۴۰۴» مواجه می‌شوند.
اگرچه این پیام‌رسان روی دستگاه‌هایی که از قبل آن را نصب داشته‌اند کماکان بدون مشکل کار می‌کند، اما امکان
دانلود تازه
یا نصب مجدد آن روی آیفون و آیپد فعلا وجود ندارد.
تاکنون هیچ‌یک از شرکت‌های اپل یا تلگرام بیانیه رسمی درباره دلایل این تصمیم صادر نکرده‌اند و مشخص نیست که این اقدام دائم است یا موقت و آیا ناشی از بررسی‌های قانونی و محتوایی است یا یک نقص فنی.
پیش از این نیز در سال ۲۰۱۸ اپل برای مدتی کوتاه تلگرام را به دلیل «نگرانی از انتشار برخی محتواهای خلاف قوانین» از اپ‌استور خارج کرده بود که پس از اعمال اصلاحات لازم، این برنامه مجددا بازگشت.
@
VahidOOnLine
🔄
و آپدیت چند ساعت بعد:
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
@
VahidOOnLine
🔄
پست پاول دورف، مدیرعامل تلگرام درباره این موضوع، ترجمه ماشین:
🍎
دیشب، اپل برای مدت کوتاهی تلگرام را از اپ استور حذف کرد، زیرا یک کاربر به‌تنهایی محتوای پورنوگرافیک غیرقانونی را در یک گفت‌وگوی گروهی عمومی جاسازی کرده بود.
⬅️
تلگرام ظرف چند ساعت دوباره در دسترس قرار گرفت. اما می‌خواهم توضیح بدهم چه اتفاقی افتاد؛ هم برای هشدار دادن به دیگر توسعه‌دهندگان اپلیکیشن‌ها و هم برای کمک به محافظت از جوامع آنلاین در برابر حملات مشابه.
🧹
از آنجا که تلگرام با استفاده از گزارش‌های کاربران، فیلترهای هوش مصنوعی، هش‌های محتوا و دیگر ابزارهای نظارتی، محتوای غیرقانونی را به‌سرعت از گروه‌های عمومی حذف می‌کند، مهاجم ناچار شد به یک ترفند فنی متوسل شود. او با ویرایش یک پیام قدیمی در یک گروه فعال، محتوای غیرقانونیِ تغییریافته با هوش مصنوعی را در آن قرار داد. در نتیجه، این محتوا عملاً از دید اعضای گروه پنهان ماند و آن‌ها نتوانستند آن را ببینند و فوراً گزارش کنند.
💰
مهاجم یک «باج‌گیرِ حذف محتوا» بود؛ کسی که از صاحبان گروه‌ها باج می‌خواهد و در ازای آن، جوامعشان را هدف قرار نمی‌دهد. این باج‌گیران با استفاده از حساب‌های خودکار، محتوای غیرقانونی را در گروه‌های عمومی قرار می‌دهند و سپس مستقیماً آن را به اپل گزارش می‌کنند تا باعث حذف جوامع مشروعی شوند که صاحبانشان از پرداخت باج خودداری کرده‌اند.
🤝
از نظر عملی، محتوای پورنوگرافیک غیرقانونی در گروه‌های عمومی تلگرام یک مشکل نظام‌مند نیست. نظارت ما مؤثر است (
https://telegram.org/safety
). همین که مهاجمان ناچارند به محتوای دارای تاریخ گذشته و عملاً نامرئی و دیگر ترفندهای فنی متوسل شوند، این موضوع را ثابت می‌کند.
⚠️
با این حال، دو درس مهم برای توسعه‌دهندگان اپلیکیشن‌ها و جوامع آنلاین وجود دارد:
— باج‌گیران راهی پیدا کرده‌اند تا اپل را وادار به واکنش افراطی کنند. اپل پیش از تماس با ما، تلگرام را از اپ استور حذف کرد. این موضوع برای هر اپلیکیشن موبایلی که میزبان محتوای تولیدشده توسط کاربران است، یک خطر بالقوه و نظام‌مند ایجاد می‌کند. اگر اپلیکیشنی که بیش از یک میلیارد نفر از آن استفاده می‌کنند بتواند بدون هشدار قبلی از اپ استور حذف شود، هر اپلیکیشنی ممکن است حذف شود.
— تاکتیک‌های مورد استفاده باج‌گیرانِ حذف محتوا در حال تکامل است و جوامع در سراسر پلتفرم‌های اجتماعی را در معرض خطر قرار می‌دهد. تلگرام تجربه گسترده‌ای در شناسایی ترفندهای باندهای هماهنگِ گزارش‌دهی و محافظت از جوامع مشروع دارد؛ حتی وقتی این کار خطر حذف موقت خود اپلیکیشن ما از اپ استور را به همراه داشته باشد. ممکن است دیگر پلتفرم‌ها به همین اندازه آماده نباشند.
هوشیار بمانید!
☝️
durov
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77726" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xc9zrgpr_7xI9egtPO9nRQojlEb_HUTbksdsTs8Fs7n3ngiqGruaSJyZ9NXPKr91YPy3UAcxGhe9gxTgN3ZnVHFGtSsN2Kj_3H5RzAOfSKy5F8y2utB8FYcuwH4TWW_W8xyUjMfTjLidaNV1iNqJePOKXtjSWR9_jz-cov_vi8SUljLruYgVV_GPVZYyR7x0Ian-mdTUGozvITNqPNWxU97zjTifskFLbxRdrJiZsbp9Tzi9PVCzL1VDdfhbPZpuexuiJx406tzS2fcHtz0sEqZcEffhyIT4PwKYSJBhd1RHDl1_QB7hv9wYy31yD86pILZBQGfB1h3KoPbBWjPZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  گزارشی درباره وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرق الخصب در عمان دریافت کرده است.
یک کشتی باری از طریق کانال ۱۶ بی‌سیم VHF اعلام کرده است که با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77725" target="_blank">📅 03:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuwnlh1e_261gQ3yTIrk0UNGcIwDZ57KpOrMwQ_fLvBEAFWcsobP1NFLf6HauBwpc8ORxebBmIrKOlg1EFboae9SzLJAzSpHmSOrSOiU7DzKzk_Y6DD-jqxIiIyKGYzaXYd5CH7VcjiuJw92U0p82b9TT-1SbsHWhRY1tjfZuPWX-DccM03jzevc7XAPYoytM5oBH8WeA3BJ2OoSJt2o5UQhuzixQQHxx6hD6ZdWkRYxLsSdzRnRbBxNnwd7dqzw3_0WIzk0bJsuPGjpkezuJeOJF9TC3t25v_FirAjHO6YAUrSloK6bJfs8CIha5i7eDCzUJvabzmpPDiYejplWW9kc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuwnlh1e_261gQ3yTIrk0UNGcIwDZ57KpOrMwQ_fLvBEAFWcsobP1NFLf6HauBwpc8ORxebBmIrKOlg1EFboae9SzLJAzSpHmSOrSOiU7DzKzk_Y6DD-jqxIiIyKGYzaXYd5CH7VcjiuJw92U0p82b9TT-1SbsHWhRY1tjfZuPWX-DccM03jzevc7XAPYoytM5oBH8WeA3BJ2OoSJt2o5UQhuzixQQHxx6hD6ZdWkRYxLsSdzRnRbBxNnwd7dqzw3_0WIzk0bJsuPGjpkezuJeOJF9TC3t25v_FirAjHO6YAUrSloK6bJfs8CIha5i7eDCzUJvabzmpPDiYejplWW9kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مربوط به ایران
متن مکالمه با تشخیص و ترجمه ماشین
:
به دلایلی، وقتی در حال مذاکره‌اند، دوست ندارند بگویند که دارند مذاکره می‌کنند. من می‌گویم: «صبر کنید، ما در حال مذاکره‌ایم. چه اهمیتی دارد؟ داریم مذاکره می‌کنیم.» و آن‌ها گاهی آن را انکار می‌کنند، با اینکه ساعت‌ها و ساعت‌ها کنار یکدیگر می‌نشینند و مذاکره می‌کنند.
مذاکرات در حال پیشرفت است.
قرار بود دیروز آن‌ها را به‌شدت هدف قرار دهیم؛ بسیار بسیار شدید. حمله‌ای شدیدتر از هر حمله دیگری.
فکر می‌کنم می‌توانم بگویم—و ژنرال‌ها از روی آگاهی می‌گویند—شدیدتر از هر حمله‌ای از زمان جنگ جهانی دوم تاکنون. این خیلی بزرگ است.
ما آماده اجرای حمله بودیم که آن‌ها تماس گرفتند. علاوه بر آن، عربستان سعودی تماس گرفت، امارات تماس گرفت، قطر تماس گرفت و افراد بسیاری با من تماس گرفتند. نمی‌خواهم از کلمه «التماس» استفاده کنم، اما به‌ویژه ایران نمی‌خواست هدف حمله قرار بگیرد.
آن‌ها گفتند: «می‌خواهیم مذاکره کنیم. می‌خواهیم درباره تنگه مذاکره کنیم.» اما از دیدگاه من مهم‌تر از آن، می‌خواهیم درباره هسته‌ای‌زدایی ایران مذاکره کنیم، زیرا اصل ماجرا همین است. دلیل اینکه این کار را انجام می‌دهم همین است.
این کار باید مدت‌ها پیش انجام می‌شد. اکنون ۵۰ سال شده است. همیشه می‌گفتیم ۴۷ سال، اما سه سال دیگر نیز گذشته است. ۵۰ سال است که رؤسای‌جمهور دیگر باید کاری را که من انجام می‌دهم، انجام می‌دادند. یا کشورهای دیگر؛ لازم نبود حتماً ما باشیم، اما کشورهای دیگر باید این کار را می‌کردند. هیچ‌کس انجامش نداد و زمان آن فرا رسیده بود.
ما درباره تنگه صحبت می‌کنیم؛ بازشدن تنگه و اینکه به معنای واقعی کلمه تا فردا کاملاً باز باشد. این مرحله اول است.
مرحله دوم این است که پس از آن درباره موضوع هسته‌ای  صحبت کنیم. اساساً هسته‌ای‌زدایی ایران باید انجام شود. باید انجام شود. این مرحله دوم خواهد بود.
اما
مرحله نخست، بازشدن تنگه است. مرحله دوم هسته‌ای‌زدایی خواهد بود. آن مرحله کمی زمان می‌برد، اما ما در این زمینه بسیار قاطع هستیم.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من هرگز موضعم را در این‌باره تغییر نداده‌ام.
درباره کشتیرانی در تنگه هرمز: من اجازه نمی‌دهم از کسی پول بگیرند. ما طرفی هستیم که کنترل کامل را در اختیار دارد. ما کنترل کامل داریم.
می‌دانید، چیزی به نام محاصره داریم که با این نیروی دریایی اجرا می‌شود و به آن «دیوار فولادین» می‌گویند؛ «دیوار فولادین ایالات متحده».
نه، نه، هیچ پولی گرفته نخواهد شد. اصلاً درباره گرفتن پول صحبت نمی‌کنیم. پولی گرفته نخواهد شد.
فکر می‌کنم به این واقعیت بسیار افتخار می‌کنم که به مردم فرصت می‌دهم. به مردم فرصت خواهم داد. انجام حمله‌ای به آن بزرگی علیه یک کشور، تصمیم بسیار بزرگی است. ترجیح می‌دهم اکنون آن را انجام ندهم.
امیدوارم سر عقل بیایند
قرار بود حمله دیشب آغاز شود و مدت زیادی ادامه پیدا کند و در نهایت عملاً چیز بسیار کمی باقی بماند؛ هیچ‌چیز باقی نمی‌ماند.
اگر این فرصت به من داده شود که اجازه دهم افراد زیادی زنده بمانند، می‌خواهم آن فرصت را به آن‌ها بدهم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77724" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-CcygcF90bygzBV_fVt7zMlRXtROHwfLagx2EtPOx2dB1_r7W6Au7R5Kjn6HNCcj9X8DcOUXaGc-nvKqS3tx-hduc4b6axcuTHiIDpeOWemiNuKu3pLZWFvpQLjbSPrd_7kitZaH0T8_FfJEr98XwyfIhaqvM7wHNGYONhh6GkQ1z7lHA7aNUJpILZ6C2baV5x7mDU6paRJ9mZL_CJnepkPbVKrh5lgpS0I2fgaBpAP4igggvm8FAdcM4YOpDn_hsv77l3-UoP1T5NAL7eJe4Mcygq42q5kJou6LLkzc-vhRruU6KgoQQUs59fro2ZtZBQWvOLxUTst8pynLx0x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۱۲ مرداد در حاشیه نشستی در کاخ سفید، به خبرنگاران گفت مذاکراتی که در حال حاضر با جمهوری اسلامی ایران جریان دارد، «آخرین فرصت» تهران برای امضای یک «توافق خوب» است.
ترامپ که پیش‌تر حمله‌ای که به گفته او «بزرگ‌ترین حمله نظامی از زمان جنگ جهانی دوم تا کنون» بود علیه ایران را لغو کرده بود، با انتقاد دوباره از مقام‌های جمهوری اسلامی که انجام مذاکره با ایالات متحده را تکذیب کرده بودند، گفت: «ایرانی‌ها تماس گرفتند، بعد از آن از عربستان سعودی، قطر، امارات و بسیاری کشورهای دیگر با من تماس گرفتند که یک فرصت دیگر بدهم. نمی‌خواهم بگویم «التماس» کردند ولی ایران واقعا نمی‌خواست مورد حمله قرار بگیرد.»
ترامپ تاکید کرد که این مذاکرات «با درخواست ایران» و حمایت کشورهای منطقه و جهان انجام می‌شود و «آخرین فرصت» برای جمهوری اسلامی است که انتظارات او درباره برنامه هسته‌ای را برآورده کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77723" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSZfDQw3ojAnJ7lELJEhet_B0Wyc_-1IKaL3DKr-C2Mi6pg9BilDuZetHRD6yDvNDi5ANTW_tDFzW_wMMbcJY2LTx7sATFfd8nHoCF9rhsrVleqajx6DHBVVsDacdf9vF6CVRnz1-zchYgi6BOHSxLEv5uj_Xal6LYytEVg_DKka1MKDS8y5N-On88Nqvt3E8qA3q_ENFwgXZ0YOYfwaMgXQIRHnu9W7CbhRQHprhPSsOGrzzaDbCMPfhEuzi_a1CbGMPtwrUDn3COMhMjqwJCX1xMtrXJP8iTe-EVtQjMqJtFKtWhYdP0CVkpbavk3GONCdeSLWd4rCf6_o9YfrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رهبری ایران به‌طرز باورنکردنی دورو است!
آن‌ها درخواست جلسه می‌کنند ــ بعضی‌ها می‌گویند «التماس می‌کنند» ــ مذاکرات آغاز می‌شود و جلسات بیشتری نیز برای آینده بسیار نزدیک برنامه‌ریزی می‌شود، اما بعد آشکارا و با افتخار می‌گویند که هیچ گفت‌وگویی ندارند، درباره هیچ‌چیز صحبت نمی‌شود و فقط با «عمان» سروکار دارند.
سپس همان یاوه‌گویی‌های همیشگی‌شان را ادامه می‌دهند و می‌گویند تنگه هرمز با قدرت توسط آن‌ها اداره خواهد شد، در حالی که این تنگه همین حالا نیز کاملاً تحت کنترل نیروی دریایی ایالات متحده و «محاصره» ما قرار دارد؛ یا همان‌طور که بعضی‌ها می‌گویند، «دیوار فولادین ایالات متحده»!
هیچ‌چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ‌چیز نیز نخواهد رسید، مگر آنکه توافقی حاصل شود یا تسلیم کامل صورت بگیرد. چه ایران بخواهد این را بپذیرد و چه نخواهد، ما در واقع در حال گفت‌وگو درباره راه‌حلی برای مشکلی هستیم که آن‌ها طی چندین دهه ایجاد کرده‌اند.
موضوع بسیار ساده است: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77722" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcuXX3i_Ts-PwsbzWlxckUJA6-iCLQ6PWc8LzHLRbH57FxHb7CwUZf6Y3dXo7s-kyhx5UdWtlRt8PRpi-B6pqiMJGgD2lVwQfi-2a_tT5zdPh_7YJrMWZuiI6xugS49V3H-QHFtPj7mW19KQC-O1Xz01XbuUbiOJ-rpsUTKUEtF88FgWVNwY02UWMZtOh01FNDGKdqyxPSelBaWyZNF4yNhLHSt2QYcTsiwMFXP1eG7x5d10YUxuCrnlMhP--5SHOgbo9Ojwu7_4FgDeI6qODxlA_wVLQhABhZsXODgrVxtkw-Nu0lNTtQGJ5KjoxgobWZq4GoGeDwcsZ1tSHbHBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران امور خارجه جمهوری اسلامی ایران و پاکستان در گفت‌وگویی تلفنی درباره تحولات منطقه‌ای و روند تحرکات دیپلماتیک رایزنی کردند. در این تماس، محمد اسحاق دار، وزیر امور خارجه پاکستان، از عباس عراقچی برای سفر به اسلام‌آباد در نخستین فرصت دعوت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77721" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3zubXewt8Y62nx-WQ4HKvBZal_Kt8Ar8zJc1_PKEsJYunh3QNi9KbjOt-VtEOJeq6ALS8DSDGdiOJ8ESAtZExIx0MZgVECYKIIaHZRTlN4126y2miUu0SoCyUomYMpm6oTlIZvGOZbaNiULBfatjrdc-USf1gxPjaj-Ej7Q7Xl9vvPNBXeT7pc1S8aze3IGhSdkfEhDMXnl94yzAcVOIT126C1vt8RZ5X9dhYyJvMyRpHgkiEeTpyxPn2B_F5mLcZqfFZqGfiIlOg_Ub7siS7JVC8YWjeSXXyPJzkg5NRXUsr-VXS6RvOkEVdyRrPM7EDXjmHKN6zCNqWsfksKfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز دوشنبه ۱۲ مرداد بار دیگر از شرکت‌های نفتی خواست قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند و مایک ویرث، مدیرعامل شورون، را به‌دلیل قدردانی نکردن از تلاش‌های دولتش در حمایت از صنعت نفت مورد انتقاد قرار داد.
دونالد ترامپ در یک مصاحبه تلویزیونی، ویرث را سرزنش کرد که به نقش دولت او در کمک به شرکت‌های نفتی اشاره نکرده است.
او در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «تنها چیزی که او به‌راحتی از گفتنش صرف‌نظر کرد این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و حتی خود کشور ما نابود می‌شد!»
ترامپ افزود: «برای مثال، آن‌ها مایک و شورون را از ونزوئلا بیرون کردند، اما حالا بازگشته‌اند، بزرگ‌تر و قدرتمندتر از همیشه، و انتظار دارند ثروت هنگفتی به دست آورند!»
به گفته ترامپ، «این موضوع شامل سایر شرکت‌های نفتی هم می‌شود... و همین حالا قیمت نفت برای مصرف‌کننده را پایین بیاورید!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77720" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkpQCrxo1rCedu7VTXIj8gR_6Tv9QkvrizAXtALQEvAXUtO1E1qI2Fx2k-xDNucbgBFVE-9q9DqTG9aCCjrj1bVwRxdPr2YLczIMZQyU8hgqhHj-TRYiVgEbNA-n4smaW6BPLyfNXUQ7hrgAj1xZ_4oGyDCxqUsASdTAGK9F0eRM3hHVpTXm-06-vuisKJ2DcLxfcqq1L3grHnwQEFEWZaRNUbTf0LTN7Md6KXoL0ScoHsB0_4I5PtY5TMB8lRCLKCzkFOYDJX0jdTmtP1g_BwQfkxbSRuijKn_ABkKqglw2pBGXq0se-oRbk6abGf86aPt-bX6TdEGUxaczb1ftYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌رغم افزایش امیدها برای دستیابی به پایان درگیری‌ها میان اسرائیل و گروه‌های فلسطینی، مقامات امدادی غزه اعلام کردند حملات هوایی اسرائیل برای دومین روز پیاپی به مناطق مختلف این منطقه در روز یکشنبه یازدهم مرداد، جان دست‌کم ۱۸ فلسطینی را گرفت.
به گفته مقام‌های بهداشتی فلسطینی، از بامداد یکشنبه، جنگنده‌های اسرائیلی شهر غزه در شمال، شهر دیرالبلح در مرکز و منطقه خان‌یونس در جنوب نوار غزه را هدف قرار دادند که بیشترین شمار تلفات روزانه در چند هفته اخیر را بر جا گذاشت.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از دستیابی به یک پیشرفت در تلاش‌ها برای اجرای توافق آتش‌بس سال گذشته خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77719" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvvkB_v6H_N8_10XWiZD7g6B_vdIuWdHvTc_7Ls-gGkdoftqE25slWSftGIOlGOYJSK3iM7vulBeHOwRUZ1GLh92hlzp1pUtY3Uf3STJ6yO-xnedinAMQ-VZaDbMGVgVc4Kkx4RwLQiYEbESwiOd9Z5x-3sSs6gW_sfjedJKGa7Xgs1aHRVFfVuBP__tigD0WKR7H9V0G8VotluZ8AJaAtz5ZbCSpWsJMZKN84tlWg1Od0i4qZgxRC1lLSlVqGlxLNGwTrDfy3PknfBd60C1a4dQAmTEl4XJXtgxFsLUB0tM4Fx9nqpwMYT7fQ5-2LhslBBewwoae9QEBGYwaqsWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۱۲ مردادماه گزارش کرد که «سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه» یک پهپاد ام‌کیو۹ را در آسمان تنگه هرمز رهگیری کرده و «مورد اصابت» قرار داده است.
این خبر در حالی اعلام می‌شود که دونالد ترامپ، رئیس جمهوری آمریکا از توقف طرح یک حمله بزرگ به ایران به شرط توافق برای بازگشایی تنگه هرمز و اطمینان از دست نیافتن ایران به سلاح هسته‌ای خبر داده بود.
مرکز فرماندهی ایالات متحده (سنتکام) هنوز واکنشی به این خبر نشان نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77718" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-GeL57WRyWM3wDdSEWLQ7in7QL6cPOkmO_nOzCv10eNtCP-tVARky9vhaTpQuQJ50vEtWQE-HBY4f-AW_M8lvc4Ehj4GZtNxbcR1wxyQ-FpvHxknAKrce1jsN7AESYa7i3tqnWmdA8qq06lINHlEMDLit-v5KwVW7gABygXXMt6z9h35XgYkCodimMqaDB6Y4fK0_JTyx5MCyW-9uxcUgB_rEnfNIlPlKPfhLMMyJAb9jxiZRFr2nTc24hcNlj-xhwtGe6oFmXuoam3LV-UR40160a117ccOR5zukunujUDzxtWXt7B7f1hlEt7nNgeYbQSZ6DgGzyQCP2b0NVvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=X_3LmBh1cD7Nzly4LdJk7Zar9x2cBCMEmrhaC13BwlttYf-TFUB8zi4NtNZrKcXFgBWbvTautgbD3b3J70zgayPyKtSRvOzIFTG4oDyA9LX2TIoep51QrIUobpJUMWx7-g0hx6R2OegN0-hjoyDmcx18-30hLP4K39Yuaq2sPFInsq0qcvb8MLTYh_awuDqosDKbyrWq_Lx6wZ81R7p5df7RlGjIQxT91xAgQnwaLErDnVABgPT0b9XvckuC2SVWWAJq3xWq3IYdxYg4rJ7Av4fDMdOISZGdv8CajxCHF4E5JvjSHTUW8oiaRhkFQKK29ADsr1f97kuvUUrSBDW12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=X_3LmBh1cD7Nzly4LdJk7Zar9x2cBCMEmrhaC13BwlttYf-TFUB8zi4NtNZrKcXFgBWbvTautgbD3b3J70zgayPyKtSRvOzIFTG4oDyA9LX2TIoep51QrIUobpJUMWx7-g0hx6R2OegN0-hjoyDmcx18-30hLP4K39Yuaq2sPFInsq0qcvb8MLTYh_awuDqosDKbyrWq_Lx6wZ81R7p5df7RlGjIQxT91xAgQnwaLErDnVABgPT0b9XvckuC2SVWWAJq3xWq3IYdxYg4rJ7Av4fDMdOISZGdv8CajxCHF4E5JvjSHTUW8oiaRhkFQKK29ADsr1f97kuvUUrSBDW12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی، می‌گوید در حال حاضر مذاکره‌ای بین ایران و آمریکا در جریان نیست.
اسماعیل بقائی در نشست هفتگی خود با خبرنگاران در روز دوشنبه ۱۲ مرداد، افزود آنچه در حال حاضر در جریان است، مذاکرات دو جانبه و بین دو دولت ساحلی ایران و عمان است.
او  می‌گوید که «حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.»
اظهارات او در شرایطی بیان می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرده که مذاکرات با ایران بعدازظهر دوشنبه ۱۲ مرداد آغاز خواهد شد.
با این حال او روز یکشنبه، هنگام بازگشت از تعطیلات آخر هفته در نیوجرسی به واشینگتن، به خبرنگاران توضیح نداد این مذاکرات در کجا برگزار می‌شود یا چه کسانی در آن شرکت خواهند کرد.
@
VahidHeadline
سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس می‌گوید در حال حاضر «هیچ بحثی» برای مذاکره با آمریکا در دستور کار قرار ندارد.
حسن قشقاوی در گفت‌و‌گویی که خبرگزاری دانشجو منتشر کرده، افزوده که حکومت ایران به‌ویژه در پرونده هسته‌ای، با واشینگتن مذاکره نمی‌کند.
او بدون اشاره به جزئیات افزود: «حتی در مسیر‌های احتمالی دیگر نیز بحث هسته‌ای مطرح نبوده و آینده این پرونده در متون مربوطه کاملاً روشن است».
این نماینده مجلس، اولویت فعلی جمهوری اسلامی را «لغو تحریم‌های اولیه و ثانویه در کنگره و بازگرداندن اموال بلوکه‌شده ایران» عنوان کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77716" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7s_1w9cYGW8k7lvZjPuoWYMxqxt8YpiJ3E2LcXhiMWtNL5Cvpx15VRHZvM3sc0EK-Bmvd_zJcdUbJfZL9TzX-N3pIplBUxlim0xYOo5ZuHA7Ge2ocylyoA3mJ2vWg9a38vmuNNuc9_xd1unMu1VQjs4-nU0oPZ9qYy02MNvFGqkDfmQ4vldEFaQMjiBJCZo51MxRzccxC6x4SbmNzmlmbHuj213N_nuwBDA3U0LuxdHYrSwK6HFp3cqr4-b88e_PUkjO4kw5l-fCXDn_vX7X2wdvg5YQi4LfOzJuhmMVTAB7r1u-ulAdWL_W-mToE1FExV05j-KQgMa5ovSXOx3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا، روز یکشنبه ۱۲ مردا گفت نیروهای این کشور همچنان در آماده‌باش هستند و آمادگی اقدام دارند؛ اظهاراتی که نشان می‌دهد تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به‌تعویق انداختن حمله به ایران، تأثیری بر آمادگی نظامی نگذاشته است.
پیت هگست در شبکه اجتماعی ایکس و در کنار انتشار ویدئویی از رئیس‌جمهوری آمریکا نوشت: «وزارت جنگ آماده اقدام بود و همچنان در سطحی که از زمان جنگ جهانی دوم دیده نشده، آماده است.» هگست سپس گفت ارتش «کاملاً مسلح و آماده شلیک» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77715" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY25zO1HA1a1mK8CSPE3cOgusKtaD50RxslXYjy2TqOwwoC0K9dwqT2isnrfIR2xX43JQDx3OzKGr61fYhtvBmGplFOtnf1UTT5v5PErOhYthLsXds86l52Y839SDBhV0xxqJ7AxYmwMEI41885bEnguS39Nn2Cle4lkeAcHg1EJhkljlCEJPGU48KxefBRsAXxv57ou_3KEJ9RpPGwP8eFW0NnS9HxJEMpk2Er5IS-5Ug9Hm-d_aO_HLlxsWopbQ9bwVb78LdX-vcCtSpQXofWvM7jUMIc1ZXu4CMqgs8CWcdu88KE-1zXH9bWbSdPh2jag19BJSTpXj5BWPiyG7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
خبرگزاری فارس از کشف یک خط لوله ۹۰۰ متری غیرمجاز انتقال نفت در استان بوشهر خبر داده و نوشته این لوله نفت سرقت شده را به مخزنی زیرزمینی منتقل می‌کرده است.
به گزارش فارس، فرماندۀ انتظامی استان بوشهر گفته است: «انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی» شده است.
این مقام محلی به فارس گفت که «تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات» مرتبط با این خط لوله غیرمجاز توقیف شده است.
در این گزارش به مشخصات فرد یا گروهی که در احداث و بهره‌برداری از این خط لوله غیرمجاز نقش داشته‌اند اشاره‌ای نشده است و معلوم نیست آیا آنها شناسایی و تحت تعقیب قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77714" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FldJtjFpY9OHAEzh17to1CJMrIlyXxcRhT_CMUPtRVLKLz0pSkkWQg0QThoiM9kH_z5Ki0C52xANEABtKfMg6r-f3sBUSiqs8FVvSr5i_oaY1bxfGY7ZFjpLQ2C4460YZggEfP6dUUb8Szzerfj7RWQgbj8URN7Bkn0kSdHPUpTQ2x01-PJMS0nTtQbArD0iNsh7gDVb9sA-wShYih2OHgauxtXRgZmVBQal9f8JrmbMOSJbv_JHz6Cx8zrL15Y298bdOfogZgjZjQIx2LWX5n8Fxo_IAlJgSjpXbINQMOt1R7xjGjjdRPt-ScqdHMHHqY_JVXVF0Noq3CrJeaOmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی نفت دوشنبه ۱۲مرداد۱۴۰۵ پس از اعلام «دونالد ترامپ» مبنی بر توقف حمله نظامی آمریکا به ایران و آغاز دور تازه مذاکرات میان دو کشور، بیش از پنج درصد کاهش یافت.
خبرگزاری «رویترز» گزارش داده که بازارهای جهانی، کاهش احتمال درگیری نظامی در خاورمیانه و افزایش امید به دستیابی به توافق میان تهران و واشنگتن را مهم‌ترین عامل افت قیمت نفت می‌دانند. به نوشته این خبرگزاری، نگرانی معامله گران از اختلال در عرضه نفت و بسته شدن احتمالی تنگه هرمز، پس از اظهارات ترامپ کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77713" target="_blank">📅 17:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QzwGLICKqolxkx-S8gwbSCrgZVgn8mStXuWz0GEBTGkgrofa8kJUScIJdZ0cdgh2UCgq_Pi1n3jm-N26I1AP1zgUADpF61qy-CrSXtaA3TCZsM3X1Sh2i683bz7fwX3ciOTpYwZ81_J8Sog1m1-a4gd6ksUNcN-AU1oTMmiwKl22ObZ6qOgULciJBECvTzoV1lSEyOLbiH1Q94vyG5kPrmZzwe8lFOZPJFcIoady-13N68zmmLSRux2WLOUIEt-BKDqgiQjb2gQf92uVkz7SzbWjPC-AwzQZDXQa16-DtjEVwI0lDr_mBbfP3aemW0SxYO8VqcgImgTq8BjioyVpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه وابسته به قوه قضاییه جمهوری اسلامی از اعدام دو زندانی به نام‌های «امید بهزاد» و «پوریا صفوت» به اتهام «جاسوسی» و «همکاری اطلاعاتی» با اسراییل از طریق «ارسال تصاویر مراکز امنیتی و نظامی» جمهوری اسلامی خبر داد.
خبرگزاری میزان، ارگان رسمی قوه قضاییه، اعلام کرد این دو زندانی بامداد دوشنبه ۱۲مرداد اعدام شدند.
به ادعای این نهاد، «بررسی‌های فنی» انجام‌شده روی تلفن همراه امید بهزاد این موارد را تایید کرده و او نیز «در جریان تحقیقات» به آنها اعتراف کرده بود. با این حال، مشخص نیست این اعترافات در چه شرایطی از او گرفته شده است. جمهوری اسلامی طی بیش از ۴ دهه حکومت خود، بارها اقدام به اخذ اعترافات اجباری کرده است.
در گزارش میزان، پوریا صفوت نیز بدون ارائه هیچ‌گونه سند یا جزییاتی، به همکاری «مستقیم با موساد» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77712" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=YyVesxR3pGM79cDpqkm_iMfbP3MeBDRH14luATNOkXZOwANJZ3xfMupEBwdIQ1ruRFQl_I_a-mTKc7WniwE5732THLV4r4VcpKXf8ycBRwSaQ4LTmFt-EMJt0-hqQy5HFV5Z-u0VTTdWUXaD7vtCiL97uHNwXWK14TkLhVJ8cWDO9vC78IB4-ILPq2OAn6aToXwr6ceCr60ebc0QySfqZYAqvvN3EWOzUwpg49Q9w195g7IMlTP2yM35RwHjNSrcuxWXUSeYmxr0uInMpNPX6LxmEmCxWwE2uwRdyOJVRkS2pEy2WGepiED1nPRi_y4_mAmg2c1xY_xiLGN4th9vgF3JSr8WHIVQXyEukzk2Yw7ZEL939iJ4pEZbqbvDZaLbCE1plaxnJdTaA5krn8Y1FgMFSABw0N5ArYs8ZSMBZOGq71Zftn-3GWg_6J6e8Fo_y_L9puUj-uvwW_-oz5PYvRuMd2uI3SR5FqXbUnsfpEau6rvG3nNrcyYJTeGVqU2wFVNeYxq4KIx4bRwYvhAqVJlvma4qx3SeWfk0x1Wxngyxx48mFhLU9kqQDqHfArd-eoCyKormYIzGRlZusPgTpwn-Mvzaev2TIF9YbW4H7ClyStUrPfsfdvWPDdJTdt8Jj0ps4Loqk_YJ0A_PKFMUcTkQjgy7Sk9vKl6ze16bLzI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=YyVesxR3pGM79cDpqkm_iMfbP3MeBDRH14luATNOkXZOwANJZ3xfMupEBwdIQ1ruRFQl_I_a-mTKc7WniwE5732THLV4r4VcpKXf8ycBRwSaQ4LTmFt-EMJt0-hqQy5HFV5Z-u0VTTdWUXaD7vtCiL97uHNwXWK14TkLhVJ8cWDO9vC78IB4-ILPq2OAn6aToXwr6ceCr60ebc0QySfqZYAqvvN3EWOzUwpg49Q9w195g7IMlTP2yM35RwHjNSrcuxWXUSeYmxr0uInMpNPX6LxmEmCxWwE2uwRdyOJVRkS2pEy2WGepiED1nPRi_y4_mAmg2c1xY_xiLGN4th9vgF3JSr8WHIVQXyEukzk2Yw7ZEL939iJ4pEZbqbvDZaLbCE1plaxnJdTaA5krn8Y1FgMFSABw0N5ArYs8ZSMBZOGq71Zftn-3GWg_6J6e8Fo_y_L9puUj-uvwW_-oz5PYvRuMd2uI3SR5FqXbUnsfpEau6rvG3nNrcyYJTeGVqU2wFVNeYxq4KIx4bRwYvhAqVJlvma4qx3SeWfk0x1Wxngyxx48mFhLU9kqQDqHfArd-eoCyKormYIzGRlZusPgTpwn-Mvzaev2TIF9YbW4H7ClyStUrPfsfdvWPDdJTdt8Jj0ps4Loqk_YJ0A_PKFMUcTkQjgy7Sk9vKl6ze16bLzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، می‌گوید که «مذاکرات جدید» با ایران روز دوشنبه آغاز می‌شود.
آقای ترامپ گفت که در حال حاضر توافقی درباره تنگه هرمز وجود دارد و توافقی هم درباره هسته‌ای زدایی ایران حاصل خواهد شد.
@
VahidHeadline
گفت‌وگوی ترامپ با خبرنگاران در هواپیما
تشخیص و ترجمه ماشین:
🔺
خبرنگار:
چه چیزی باعث شد حملات دیشب را لغو کنید؟
🔻
ترامپ:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند این کار را انجام دهم.
ما تقریباً همین موقع کاملاً آماده اجرای عملیات بودیم و قرار بود حمله‌ای عظیم باشد. همه‌چیز برای اجرا آماده بود. اما وقتی متحدان می‌خواهند حمله را لغو کنید، ناچارید بگویید: «خب، ببینیم چه می‌شود.»
دلیل درخواستشان این است که فکر می‌کنند توافقی وجود دارد. توافقی دربارهٔ [واژه نامفهوم] وجود دارد و بعد هم توافقی درباره موضوع هسته‌ای حاصل خواهد شد؛ یا می‌توانید آن را «هسته‌ای‌زدایی از ایران» بنامید. من آن را هسته‌ای‌زدایی از ایران می‌نامم.
فعلاً آن را متوقف نگه داشته‌ایم. فقط باید ببینیم چه می‌شود. هر زمان بخواهیم می‌توانیم آن را انجام دهیم.
اما سه طرف اصلی از ما درخواست کردند. ایران هم با تأکید زیادی از ما درخواست کرد. گفتند: «مایلیم توافق کنیم.»
حالا نمی‌دانم بیرون چه می‌گویند، چون خیلی وقت‌ها این را به من می‌گویند و بعد بیرون می‌روند و می‌گویند: «نمی‌دانیم او درباره چه حرف می‌زند.»
بدیهی است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها از وسعت حمله خبر داشتند، چون [عبارت پایانی نامفهوم است].
🔺
خبرنگار:
حالا چه اتفاقی می‌افتد؟
🔻
ترامپ:
کاری که اکنون انجام می‌دهیم این است که در قالب مذاکره با آن‌ها گفت‌وگو می‌کنیم. مذاکرات فردا بعدازظهر آغاز می‌شود و خواهیم دید آیا واقعیت دارد یا نه.
خیلی دوست دارم این اتفاق بیفتد. جان‌های زیادی نجات پیدا می‌کند و [ادامه جمله نامفهوم است].
سال‌های بسیار زیادی طول می‌کشید تا بتوانند آن را دوباره بسازند؛ البته اگر اصلاً امکان بازسازی‌اش وجود داشت. فکر نمی‌کنم حتی قابل بازسازی می‌بود.
حمله‌ای آماده کرده بودیم که اگر انجام می‌شد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
برای آن‌ها فاجعه‌بار می‌شد و نمی‌خواستند ما آن را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم آن را نمی‌خواست. آن‌ها فکر می‌کردند توافقی قریب‌الوقوع است.
🔺
خبرنگار:
آیا ضرب‌الاجلی وجود دارد، قربان؟
🔻
ترامپ:
توافقی قریب‌الوقوع است که به [واژه نامفهوم] و در نهایت به هسته‌ای‌زدایی از ایران مربوط می‌شود.
وقتی این را می‌شنوم، می‌گویم: «آیا می‌خواهیم تا این اندازه شدید عمل کنیم؟»
گروهی از مردم هستند که می‌خواهند من فوراً این کار را انجام دهم و گروه دیگری از مردم هم هستند که نمی‌خواهند من این کار را انجام دهم.
🔺
خبرنگار:
آقای رئیس‌جمهور، آیا ایران برای رسیدن به توافق ضرب‌الاجلی دارد؟
🔻
ترامپ:
باید ببینیم. ببینیم اوضاع چگونه پیش می‌رود. هر زمان بخواهیم آماده‌ایم وارد عمل شویم.
آیا ترجیح می‌دهم توافق کنم؟ من در پی کشتن مردم نیستم، چون مردم کشته می‌شوند؛ تعداد زیادی از مردم کشته می‌شوند و ما این را نمی‌خواهیم.
بنابراین آن‌ها از ما درخواست کردند؛ مشخصاً ایران. اما آن سه طرف دیگر هم گفتند که واقعاً...
از آن‌ها پرسیدم. [اشاره نامشخصی به پادشاه و سپس ولیعهد.] گفتم: «ترجیح می‌دهید چه کار کنیم؟ ترجیح می‌دهید ما این کار را انجام دهیم یا نه؟»
گفتند: «ما توافق را بسیار بیشتر از حمله ترجیح می‌دهیم، چون نمی‌دانید این [واژه نامفهوم؛ احتمالاً اشاره به حملات یا اقدامات] به کجا منتهی می‌شود.»
آیا کشورشان با ورود سیل‌آسای مردم و فاجعه روبه‌رو خواهد شد؟ اتفاق‌های بد زیادی ممکن است رخ دهد.
🔺
خبرنگار:
قربان، گزارشی منتشر شده است که می‌گوید نیروهای آمریکایی را از بحرین و کویت خارج می‌کنید. آیا نیروها از خاورمیانه خارج می‌شوند؟
[در ترنسکریپت هیچ پاسخی از ترامپ به این پرسش ثبت نشده است.]
....
🔺
خبرنگار:
بازگردیم به ایران؛ آیا آماده بودید اهداف انرژی را هدف حمله قرار دهید؟
🔻
ترامپ:
نمی‌خواهم این را بگویم. نمی‌توانم این را بگویم.
قرار بود حمله‌ای عظیم باشد. قرار بود حمله‌ای باشد که با فاصله بسیار زیاد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
اما از ما خواستند آن را انجام ندهیم. گفتند: «لطفاً این کار را نکنید.»
همسایگانشان هم همین را گفتند.
بنابراین فقط می‌خواهیم ببینیم آیا می‌توانیم درباره هسته‌ای‌زدایی به توافق برسیم یا نه.
🔺
خبرنگار:
[پرسش ناقص درباره اینکه مذاکرات فردا انجام می‌شود.]
🔻
ترامپ:
بله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77711" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjbR_edo2tfmUQgNuxSL4d6RD_EcuTmruG73pU5ko6RANGpj_rowchyrk_8M3ML9sp2vRLYfzN7PLTJavzq_CaPCnGcky0KcQD6h9IU_JjlYbXbU9vUsxzheuosS0Hc9uCcJrb4MocXHbN8aMZb8qgL7T_sIJXLMSgEJ4UOuI_Ov8m8pgWQyV-qyd9oaDdkZUqd-8Kp8Os738VCYTJlRKhH606s-z1rfoikyu0nhT7jEjoZKo0LdZi4yhQSnBcn0sU0gQkWv6kEtQX4-b9GPYu7DOdqmbySsZwi__-PrfUPRegOGZAid5a6Ew4w9n-aqp18yahpuVk9Fz74nOzESCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رییس‌جمهوری ایران، در پیامی یادداشت تفاهم امضا شده میان تهران و واشنگتن را «حاصل خرد جمعی اعضای شعام» توصیف کرد و نوشت: «باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند.»
پزشکیان روز یکشنبه ۱۱ مرداد در شبکه اجتماعی ایکس نوشت: «تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود. باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.»
همزمان، کانال ۱۲ اسراییل به نقل از منابع آگاه گزارش داد کشورهای منطقه در حال میانجیگری برای بازگرداندن آمریکا و ایران به یادداشت تفاهمی هستند که ماه گذشته میان دو طرف امضا شد.
بر اساس این گزارش، توافق پیشنهادی شامل باز ماندن تنگه هرمز به مدت ۶۰ روز بدون دریافت عوارض و تمدید آتش‌بس میان تهران و واشینگتن است. کانال ۱۲ گزارش داد یادداشت تفاهم پیشین به دلیل اختلاف بر سر نحوه مدیریت تنگه هرمز از هم پاشید؛ به گونه‌ای که دونالد ترامپ بر باز بودن کامل این آبراه تاکید داشت، در حالی که تهران معتقد بود این توافق به جمهوری اسلامی اجازه می‌دهد مسیر عبور کشتی‌ها را تعیین کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77710" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراقچی: مذاکرات ایران و عمان درباره تنگه هرمز به مراحل پایانی رسیده است
🔸
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه خبر داد که مذاکرات با عمان درباره تنگه هرمز به «مراحل پایانی» رسیده است.
🔸
به گزارش خبرگزاری رسمی دولت ایران، ایرنا، عراقچی در جلسه هیئت دولت از وضعیت این گفت‌وگوها گزارشی ارائه داد و اعلام کرد که «مذاکرات در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند».
🔸
هفته گذشته وزارت خارجه ایران گفته بود که مذاکره میان تهران و مسقط همچنان ادامه دارد. این در حالی است که کاظم‌غریب‌آبادی، معاون عباس عراقچی، سه‌شنبه همان هفته اعلام کرد که جمهوری اسلامی پیشنهاد عمان مبنی بر تقسیم برابر مسیرهای عبور و مرور میان دو کشور در تنگه هرمز را رد کرده است.
🔸
پیش از آن، خبرگزاری رویترز پیش‌تر به نقل از یک منبع آگاه گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
🔸
همزمان با انتشار اظهارات روز یکشنبه عراقچی، سخنگوی وزارت خارجه در گفت‌‌وگو با تلویزیونی حکومتی ایران مدعی شد که مذاکره بین ایران و عمان دربارۀ تنگه هرمز «ربطی به باز یا بسته‌شدن تنگه هرمز ندارد».
🔸
اسماعیل بقائی همچنین گفت که مدیریت آینده تنگه هرمز با ایران است و با مشورت عمان انجام می‌شود.
🔸
این مواضع در حالی مطرح شده که دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد یکشنبه اعلام کرد طرح جدید برای حمله به ایران را با درخواست جمهوری اسلامی و کشورهای خاورمیانه و برای تکمیل توافقی که به بازگشایی «فوری، کامل و تمام‌عیار» تنگه هرمز و «پایان تهدید هسته‌ای ایران» منجر شود، متوقف کرده است.
🔸
رسانه‌های ایران به نقل از منابع آگاه حکومتی درخواست از آمریکا برای توقف طرح حمله را رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77709" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CNiWlrnPO5gLiKD2-AiaIkF0P1jz1SBefHkZF4-l2zi4NZGjOHatT-v8ZiUUS02aGlAdaU_uluKIIqNL76XdnUoCeYGy4OISDUagM7S0AbnroXoQE0HrGxToj-xN0XLVRc7B3NFlYTHx6Zb8lcmekhsv_JdBl4OJJhWjRDnwoBUSKNvyo8nvjQ8XgNgDxuVUjWn9KrYTqfpD_-xE-fW3GWr6eiO4d8XXzPvg7JNDVTj0_o_pZxNFOgTlPrhRMAxF_mYyh-Nqhbgp5AoUgWZDBaX-bNCYygrIxq2fWel2DjTg-1A6wUNT3yQm1qLC03mdePfsS9te82vxHEUaa1FpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mlka6zVni1jdbYc4fEuO9x7opOs3YbXQxXq9XJHcrMUp9UnrQxg-0wYA-MSosx1SY2v7PeepwgGTdAYP4z-Ev4Y4E7Q9OtrEr8vlw--SarbTcMSF8Kdjq2zri4cvuP_vCZ4_aHDpsEej-Dxu9fq0NTwBFucaqjG2bm0nC_Xr9T7jVw8WYfzfczbiCQEO2AH0qo9cscNXWsflGrfCH5YcGxohEg8DjPvcOQ7Me7XOxpaqfghhEIo45Gn0YAYIpCJA0k2vDwCd1UtZIclwgQ0inN36Q0l9aaFgXWeZdvL44-PQH5zFlUouDWyyGrwQLE9xm_804PIG8ay_Hdp1cdsbUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل یک‌شنبه ۱۱ مرداد گزارش داد عباس عراقچی، وزیر خارجه جمهوری اسلامی، شب گذشته با پیشنهاد مصالحه‌ای که میانجی‌های قطری و آمریکا درباره سازوکار بازگشایی تنگه هرمز تدوین کرده بودند، موافقت کرده است.
این شبکه به نقل از دو دیپلمات آگاه از جزئیات مذاکرات گزارش داد پاسخ مثبت عراقچی یکی از دلایلی بود که دونالد ترامپ، رییس‌جمهوری آمریکا، با لغو حمله به ایران موافقت کرد.
@
VahidOOnLine
خبرگزاری فارس به نقل از دو «منبع آگاه» گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، با طرح بازگشایی تنگۀ هرمز را تکذیب کرد.
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای ایران به این خبرگزاری گفت هیچ توافقی درباره بازگشایی تنگۀ هرمز حاصل نشده و اخبار منتشرشده در این زمینه «کذب» است.
فارس همچنین به نقل از یک منبع نظامی نوشت تا زمانی که «اقدامات خصمانه آمریکا» ادامه داشته باشد، تنگۀ هرمز مسدود خواهد ماند و عبور شناورها تنها از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه پاسداران امکان‌پذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77707" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCi7_Rl2t0Q9feXBi6vuzX6v67c5R15fnKGQgApezgXzExP0RP4amkt65Ge9i1jOjGeIjjndaMfe8otW5wblwSa4epsmBYzVm0lJJvMW-W3b_5SGlgO0sZC35utbb73ojPPcGNcLuzglsrhF4nXYHLxnKH7w0QbkIUipjTuezWDQm8LnNQruYRMKVxgVRwgcX-HlnE3lwuWq3X-cAHSlyEbyABNf7xH0AfHLW54Cltd2yFyjdtXZJCB8gnNFepCnVPygytiD51aM9q6uyNjDur7ajjUMHqhrAtMf5auwrVuWPupE-n9zYp_vPQNa4xmMIOucflmiYDAp-oMRpmOdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در مصاحبه‌ای با فاکس نیوز که لارا ترامپ، عروس رئیس‌جمهور آمریکا، انجام داد، گفت حتی اگر در تهران به‌طور رسمی «تغییر رژیم» رخ ندهد، حکومت ایران «باید» روش خود را تغییر دهد.
وقتی از روبیو پرسیده شد آیا واشینگتن می‌تواند بدون تغییر رژیم در تهران، ایران را «هسته‌ای‌زدایی» کند، او گفت:
«فکر می‌کنم آنچه باید رخ دهد این است که حکومت باید تغییر کند. ممکن است تغییر رژیم نداشته باشید، اما حکومت باید تغییر کند.»
او افزود: «حکومت ایران به‌طور سنتی رویکردی توسعه‌طلبانه در خارج از مرزهایش داشته است. در اصل، دیدگاه آنها این است که نمی‌خواهند فقط بر ایران حکومت کنند؛ می‌خواهند بر منطقه حکومت کنند. آنها می‌خواهند انقلاب را صادر کنند.»
روبیو ادامه داد: «این رویکرد باید تغییر کند و تنها راه تغییر دادن آن این است که هزینه‌اش را آن‌قدر برایشان بالا ببرید که دیگر قادر به پرداخت آن نباشند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77706" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=pTUivmtQPZzp3Ohyd8bxWpaUBb3VCPP3yyqsagKXXD0d8u-SvwF2VNq_6T2S_hG_9LxtN5RTTAprZWUUKbBdliGAt00ZTfDLFjXsi9WBhXEboRSLcDWmhKx4P19vMf6sBrGsfb9N8Qrt4e9aziyiCkV0oe1vjAYzXZuIAs-ehlOeCjdBjYHbbcOU7mmBCRJ2iEBdjyPsOTXuZuMmoFBF-SYO97GtroDF08ShA00Mzw3j28LDFrrRW35vO7e0yo4LHkRk9GBGTsBfn2V4XYmelrGcm3kABFGIg4MteGLp6YwQb5oSQLljSozsDBv-8t7tAjLHzGWDypmrdk5CgPsB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=pTUivmtQPZzp3Ohyd8bxWpaUBb3VCPP3yyqsagKXXD0d8u-SvwF2VNq_6T2S_hG_9LxtN5RTTAprZWUUKbBdliGAt00ZTfDLFjXsi9WBhXEboRSLcDWmhKx4P19vMf6sBrGsfb9N8Qrt4e9aziyiCkV0oe1vjAYzXZuIAs-ehlOeCjdBjYHbbcOU7mmBCRJ2iEBdjyPsOTXuZuMmoFBF-SYO97GtroDF08ShA00Mzw3j28LDFrrRW35vO7e0yo4LHkRk9GBGTsBfn2V4XYmelrGcm3kABFGIg4MteGLp6YwQb5oSQLljSozsDBv-8t7tAjLHzGWDypmrdk5CgPsB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشر شده در رسانه‌های اجتماعی نشان می‌دهد بامداد روز یک‌شنبه ۱۱مرداد۱۴۰۵ پیکر آروین خیرخواهان معترضی که در جریان اعتراضات دی‌ماه۱۴۰۴ بازداشت و ۱۰مرداد در شاهرود اعدام شد به خاک سپرده شده است.
خاکسپاری در سکوت و تنها با حضور اعضای نزدیک خانواده او انجام شده است.
بازداشت، محاکمه، صدور حکم و اجرای آن برای این شهروند معترض ۲۰ساله در سکوت خبری رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/77704" target="_blank">📅 17:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y4CDRT8ueKBu3g_HgLubfMGxkFgzIEYj4YTke7FZ1sMJfmvbiF37rCKotpRi8usB1nx8PozfjWBsZ_Tpfd-7YuK1qSlC_oGiWJQ2k4r6LVhjS3bo7wJXJvX229BEJ-DC34euXq-QUr6xI7l2tgVQ_ZZHx2Wk4JsdvzgWZjb5xq-rpf-35wniOdB4nIIf2UqtNSuRZ6Ofp6F99vJtL6xigoeXUXnGDZraCrT9wyQ5kYPuBclttfuaOMlhJR-9tiBC27Bqo1qbO_VI9gdg7EoI0adABMjYnpxtcBfVPaQErjTrM9tp-HpZJd_FZEM40CBqKqz73_6kP90ArnyEebJvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به درخواست ایران و کشورهای منطقه، حمله را برای فراهم شدن زمینه توافق، متوقف کردم
ترجمه ماشین:
ایالات متحده کاملاً مسلح و آماده است تا با جمهوری اسلامی ایران مقابله کند؛ با سطحی از رعب نظامی، توان و قدرت که از زمان جنگ جهانی دوم تاکنون دیده نشده است.
با وجود این، ایران و دیگر کشورهای خاورمیانه همین حالا از ما خواسته‌اند که از هرگونه حمله دست نگه داریم، زیرا بر سر چارچوب‌های یک توافق تفاهم حاصل شده است.
این توافق شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
بر اساس این درخواست، برای منافع آینده جهان و همچنین بقای ایرانی موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانیم به‌سرعت به یک توافق دست پیدا کنیم.
کشور اسرائیل نیز در این تعهد با من همراه است.
همه دست‌به‌کار شوید و کار را تمام کنید. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. is locked and loaded and ready to go against the Islamic Republic of Iran, at levels of Military Terror, Strength, and Power not seen since World War II. Despite this, we have just been asked by Iran, and other Middle Eastern Countries, to hold off any attack in that the perimeters of a deal has been agreed to. This would include the Immediate, Complete, and Total OPENING OF THE HORMUZ STRAIT, and an end to Iran’s  nuclear threat. Based on this request, I have agreed, for the future benefit of the WORLD and, likewise, the survival of a successful and prosperous Iran, to cancel the attack, subject to being able to rapidly make a DEAL. The Country of Israel joins me in this commitment. Get to work, everybody, and get it DONE. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 562K · <a href="https://t.me/VahidOnline/77702" target="_blank">📅 05:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgjcPlniLdqU3fWr4MPjhoV02RTE0C0ziWPGCVCUMOcxRImiLILZKFpIpYoNWeXpwh97-w4KUn2QpmH1vPuXwipFgXLc7V5DEhL-011Hl05_11at-yV9Nvn-VQvfIoHIaM5JABcmJZgGv4KdIBNkAIhbKNSt4uU_XgNd7IIUElcE6N_EaQKru9Nd_rdJAF5gYrg8302Z7-h8UivtnTLMdNKbQzXODDe-pt6K7PN5_zf97QwTEkDp_ozwBpe_aCIaUjY3ZXM47ZLpP4PW3EU6Ycd3TaOzOWVkyfPRojeGTRP8xOgZwCBeIDgzyWqtHLWzylizp-3iHKkALoAlWKNruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان درباره برنامه‌های ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد
اختصاصی
اکسیوس، ترجمه ماشین:
محمد بن سلمان، ولیعهد عربستان سعودی، روز شنبه با دونالد ترامپ، رئیس‌جمهور آمریکا، گفت‌وگو کرد و درباره برنامه‌های او برای حملات گسترده جدید علیه ایران ابراز نگرانی کرد.
این خبر را دو مقام آمریکایی و یک منبع دیگر مطلع از این تماس اعلام کردند.
چرا اهمیت دارد:
ترامپ در واکنش به حمله موشکی ایران به یک پایگاه آمریکا در اردن و ادامه اختلال ایران در کشتیرانی از طریق تنگه هرمز، به‌طور جدی حمله به اهداف انرژی ایران در روزهای آینده را بررسی می‌کند. او هنوز دستور نهایی را صادر نکرده است.
تصویر کلی:
چنین حمله‌ای ممکن است به تشدید بی‌سابقه جنگ پنج‌ماهه منجر شود؛ جنگی که با باز کردن راه مذاکرات از سوی ترامپ بارها متوقف شده، اما پس از شکست این تلاش‌های دیپلماتیک دوباره از سر گرفته شده است.
جزئیات:
ایران تهدید کرده است که با انجام حملاتی علیه تأسیسات انرژی و زیرساختی در اسرائیل و کشورهای خلیج فارس تلافی خواهد کرد.
▪️
یک مقام آمریکایی به آکسیوس گفت: «سعودی‌ها ابراز نگرانی کردند و خواستار شفاف‌سازی درباره برنامه عملیاتی شدند.»
▪️
یک منبع دیگر مطلع از این تماس گفت محمد بن سلمان از ترامپ خواست تنش‌ها را کاهش دهد و از انجام این حملات خودداری کند.
▪️
کاخ سفید و سفارت عربستان سعودی در واشنگتن از اظهارنظر خودداری کردند.
مرور سریع:
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی که با نام اختصاری «کی‌بی‌اس» شناخته می‌شود، دیدار کرد.
▪️
یک منبع مطلع گفت این دیدار پس از آن به برنامه سفر وزیر سعودی افزوده شد که او با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، دیدار کرد و به او گفت عربستان سعودی خواهان کاهش تنش با ایران است.
▪️
این پیام با وجود حمله مشترک این هفته آمریکا و عربستان سعودی به شبه‌نظامیان طرفدار ایران در عراق منتقل شد.
▪️
این منبع گفت هدف از این دیدارها انتقال دیدگاه‌های محمد بن سلمان درباره جنگ ایران و اوضاع گسترده‌تر منطقه بود.
در پس ماجرا:
عربستان سعودی یکی از مهم‌ترین متحدان واشنگتن در منطقه است. ریاض، با وجود دوره‌هایی از تنش طی پنج ماه گذشته، از زمان آغاز جنگ در چند مقطع حساس بر سیاست ترامپ در قبال ایران تأثیر گذاشته است.
عامل خبرساز:
دیگر قدرت‌های منطقه‌ای، از جمله قطر، امارات متحده عربی، ترکیه و پاکستان نیز آمریکا و ایران را برای کاهش تنش تحت فشار قرار داده‌اند.
▪️
عباس عراقچی، وزیر امور خارجه ایران، روز شنبه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، که نقش میانجی مهمی میان واشنگتن و تهران داشته است، گفت‌وگو کرد.
▪️
عراقچی همچنین درباره احتمال حملات آمریکا با وزیران امور خارجه ترکیه و عربستان سعودی گفت‌وگو کرد.
▪️
عراقچی، بنا بر بیانیه‌ای در کانال تلگرامی خود، به همتای سعودی‌اش گفت: «هرگونه اقدام خصمانه از سوی آمریکا یا اسرائیل — یا مشارکت یا همکاری کشورهای منطقه در چنین اقداماتی — با پاسخ قاطع و متناسب نیروهای مسلح قدرتمند ایران روبه‌رو خواهد شد.»
آنچه باید زیر نظر داشت:
میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی برای بازگشایی تنگه هرمز، جداگانه با عراقچی، استیو ویتکاف فرستاده کاخ سفید و مقام‌های عمانی گفت‌وگو کردند.
▪️
یک منبع مطلع از مذاکرات گفت این گفت‌وگوها پیشرفت داشته است، اما هنوز مشخص نیست که آیا این پیشرفت برای فروکش کردن بحران کافی خواهد بود یا نه.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 502K · <a href="https://t.me/VahidOnline/77701" target="_blank">📅 03:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrpieNm7jWUgLNFSfURZ9mSVw1dTly5tmNgn-p7J-CvYEKy00Y62B-A7GUuW1URvSYaMH9WEbvdb2joO73WGtie-iY8gWuTzEGTouQSUXEVD_2VXUFym8AbrRCd706sNXOLgfEVWhRFxaGfw0UM0oS-CMAdaNeLtpnPmPXUV_T1LFV5UnD5ndlYXD63kjOl2ch3KUF6vEwGt3ms1kk4GckaEnJBvAqXiMw4_Lf5uraiQ7HacDGBsiWC3g61TkC3TEuThDcjCDER9PdTq6fdmeOao7xpkXHw8-5c1y_ogpCQrCbnEWJA915cGe-rSyE7A1wV5i8p6oXn6XmC5Q_Cqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با افزایش تنش‌ها میان واشنگتن و تهران، «وای‌نت» روز شنبه گزارش داد، ورود و استقرار بیش از ۳۰ هواپیمای سوخت‌رسان نظامی آمریکا در فرودگاه بن‌گوریون تل‌آویو و افزوده شدن ۱۰ هواپیمای دیگر در روزهای آینده، موجب بروز اختلالات شدید، ترافیک سنگین هوایی و تاخیرهای روزافزون در پروازهای این فرودگاه شده است.
بر اساس گزارش سازمان فرودگاه‌های اسرائیل، میانگین تاخیر پروازها در ترمینال‌های مختلف به بیش از یک ساعت رسیده و دریافت بار مسافران نیز تا دو ساعت معطل شده است. وضعیتی که هم‌زمان با اوج سفرهای تابستانی و نقایص فنی اخیر در سیستم‌های کنترل ترافیک هوایی اروپا، مسئولان را نسبت به تشدید بحران و جدی‌تر شدن اختلالات در پروازهای بین‌المللی نگران کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 501K · <a href="https://t.me/VahidOnline/77700" target="_blank">📅 03:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vb5Mz0IfKPs_P1Ew3O2tMhPGfKtapp0WujMK8MJy_UzUn96iiCrexw9LbGGb9y2Scwb_3BD1-mT8E5_gnJrDPQLy-Y_i-lRMN6XSP1sfMl6TQuRq49MJQLBeQ1UtW9HTIZwR9Gmon1xbodB78el7zQyOMEqpude2PkVdK91bR6C8wy6FXtpnwAQJWfpyVE7Gr-S6DN_hiRPGuicbtVHJeDYTCwssMT3OFX4N7pRvGpnGTzHlW5bttgF0RbiqApDV_mQykedw1HVExmcVWC9AypInY3_rJ2UsObfql7dA1QqgeyrtN5VE1g9gL5AgWOghsPEEONTP-b71_EmY9hDiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است
هم‌زمان با افزایش تنش‌ها در منطقه و انتشار گزارش‌هایی درباره احتمال از سرگیری حملات آمریکا علیه جمهوری اسلامی، دونالد ترامپ، رییس‌جمهوری آمریکا، تصویری را در تروث سوشال
منتشر کرد
که به کاهش ارزش ریال و افزایش تورم در ایران اشاره دارد.
در این تصویر با عنوان «ترامپ در حال نابود کردن ارزش پول ایران است» نوشته است که ایران با تورم شدید روبه‌رو است و ارزش هر دلار از حدود ۹۰ هزار تومان به ۱۹۰ هزار تومان افزایش یافته است.
ترامپ توضیح یا اظهارنظر دیگری درباره این تصویر منتشر نکرد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه شنبه دهم مرداد ماه، تصاویر ساخته با هوش مصنوعی را در شبکه تروث سوشال منتشر کرد که او را در لباس رزم جنگ استقلال آمریکا نشان می‌دهد. در مطلب دیگری، تصویری از ناوگان دریایی غرق شده جمهوری اسلامی در زمان ریاست جمهوری او دیده می‌شود.
در یکی از این تصاویر ساختگی، ترامپ با پوشیدن لباس فرماندهان جنگ استقلال آمریکا و در میان دود و آتش نبرد به تصویر کشیده شده است. در تصویری دیگر تحت عنوان «۱۵۹ کشتی ایرانی»، شناورهای نظامی ایران در دوره رییسان جمهوری سابق آمریکا روی آب نشان داده شده‌اند، در حالی که در به دوره ترامپ، تمامی این شناورها در قعر دریا غرق  شده‌اند.
این تصاویر در حالی منتشر می‌شوند که رسانه‌های مختلف از جمله
شبکه ۱۲ تلویزیون اسرائیل
از احتمال حمله گسترده ارتش آمریکا به ایران خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 574K · <a href="https://t.me/VahidOnline/77699" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEaWMA5dxY0G7jkshAV3hoM2Y0AtnAObr2pgGmqLeJQ3e2azt_wERgvlScGBydDvM2xWgD8pVN4dfjIIAmQ0SDm2JghgKStis9q6Q1_cmBIUnFylfq_3dSULK8dh_JcUK1XAsQpQVjsccWooRLjYhjtxmwhpFcOgN9jUdZuM1-eOUN4RZbyxUO72cZJZxpaMcaLd9zpF-ZcUsiJVo3gSOErlGRyl6oNAwkrGm6rMD_Ep6XTIVa2L-FUoniSkv-IEldsZp_Rkq-l87Nz0nUjQeQh4ZpRs6Rxlv9HKiEyn1f_LjHAzeHVq-0SFp7DSgPWmMQv3XNMTl2pInCJDr9A-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سحرگاه روز شنبه ۱۰ مرداد ۱۴۰۵، حکم اعدام آروین خیرخواهان، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان شاهرود به اجرا درآمد. این جوان معترض، پیش‌تر از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شده بود.
به گزارش خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، حکم اعدام آروین خیرخواهان حوالی ساعت چهار بامداد امروز اجرا شد.
یک منبع نزدیک به خانواده این زندانی با تایید این خبر به هرانا گفت که مسوولان زندان تاکنون پیکر او را به بستگانش تحویل نداده‌اند. به گفته این منبع، به خانواده اعلام شده است که ساعت سه بامداد فردا برای تحویل پیکر مراجعه کنند و مراسم خاکسپاری نیز باید ساعت پنج بامداد برگزار شود.
آروین خیرخواهان در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت و سپس از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شد. این حکم پس از اعتراض، در دادگاه تجدیدنظر و دیوان عالی کشور نیز بدون تغییر تایید شد.
تاکنون جزییات دقیقی درباره زمان و نحوه بازداشت، مصادیق اتهامی، روند بازجویی، دسترسی این زندانی به وکیل انتخابی و مستندات مورد استناد دادگاه برای صدور حکم اعدام منتشر نشده است.
هرانا نوشته است، آروین خیرخواهان هنگام اجرای حکم اعدام ۱۹ سال و شش ماه سن داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 586K · <a href="https://t.me/VahidOnline/77698" target="_blank">📅 18:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=uQAAhBk-uQhE-tL3hEbbT4MHy4r30qrYfbCUqNqgKAMuTHi6ksGGQobaRhywr9J5Cgm5oGa5m1BvE3Ne6VB1ly8DNx0uK-VFAaC4Nce2iYBFqtnHBzmH3LG3r39VLTXr_PO79o8tEnxCWEDzsMa5TAhf2VfmO6o8qVZQyqESb5wlrRJS6mak1O2Wwv257hktbNT6XbREULW0uu0NH46Z6xim6CcxqzkqfeVuMcsDJ8Cg4gxIfHdcYWaYVujbhhKOZTkmBzC8eSL2PjVG7R0em9-B6PeOkgmdMVw81XYMSdnYIv11Tf5LR1HXh0Rbo53trCCvUdYk6SILVl307QvtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=uQAAhBk-uQhE-tL3hEbbT4MHy4r30qrYfbCUqNqgKAMuTHi6ksGGQobaRhywr9J5Cgm5oGa5m1BvE3Ne6VB1ly8DNx0uK-VFAaC4Nce2iYBFqtnHBzmH3LG3r39VLTXr_PO79o8tEnxCWEDzsMa5TAhf2VfmO6o8qVZQyqESb5wlrRJS6mak1O2Wwv257hktbNT6XbREULW0uu0NH46Z6xim6CcxqzkqfeVuMcsDJ8Cg4gxIfHdcYWaYVujbhhKOZTkmBzC8eSL2PjVG7R0em9-B6PeOkgmdMVw81XYMSdnYIv11Tf5LR1HXh0Rbo53trCCvUdYk6SILVl307QvtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر علی منوچهرآبادی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، با انتشار ویدئویی در اینستاگرام، تولد خود را کنار مزار فرزندش جشن گرفت و یاد او را گرامی داشت.
علی منوچهرآبادی، شهروند ۲۵ ساله کُرد اهل کرمانشاه، در جریان اعتراضات دی‌ماه ۱۴۰۴ در محدوده فلکه سوم تهرانپارس با شلیک گلوله جان باخت.
او پسرخاله میثم کُرانیان، از دیگر جان‌باختگان اعتراضات مردمی در کرمانشاه، بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 527K · <a href="https://t.me/VahidOnline/77696" target="_blank">📅 17:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N4ZI12-oHiZf35A-SFREovHRBkQy1gh-j3Bm5r5GlJ5lsECpiDh_WcAK5PG8zWVBErDpViri9K_IS7uXQcBBTAcltaUCD9eOjBtwgPxojGJbr0aqwzCRy27yCBou1vFrg2idRybpLF1Ep5923bxtuRzrZn-D1JwSzqFphL9Kc_owbA4pFyV9XzqwGvZWLDg5ueiwcVclFZxVTlvKWD76xaqex24XCGV1BCMcfLXb53EBJKJweFwWhvok7xNO1UIJZw3ll7uEbhP3gOszwTnW2lXvrP0c-5O7X9fI-q_DIMb-f49u4IYm5DIFj3IqNHygrFUCk2dlDWwN66ORwgxLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت ارتش کویت، ترجمه ماشین:
سامانه‌های پدافند هوایی کویت در حال مقابله با حملات پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران، هستند.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان درخواست می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 580K · <a href="https://t.me/VahidOnline/77695" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krYNnZzjF67w51xQSrVwr88SV-FPB4SYNuF4trhL35b4ltoHIn7lpEeOK95dHSsEO1XChkHi7p6e6oJ5trnMbR2wrIrwClKb0tnEMnjo8oaKbrpbRdKyTtygvVfiErle4w2BPhlpxE5Pqu4A5B219eo8mND_gYkFIhALQiYM16gIschA7tMODbui6AKnZ8QpVeDJTBLm51EEuuw8FbmE3AhVBWVft3lTzI6VHGgjqYXhih6WO2jlYvzmqgJeNHL9tX-Gl3OfsKqu1vDs60dYhB3doJQ4VixUsFulLTWRTKm6-bgbTTbaVFUru9JZLHkNoXXy_qCDEfTxthwpFoq6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا از وقوع یک حادثه دریایی در شمال شرق خصب عمان، در نزدیکی یک نفتکش گزارش داد.
ساعاتی پیش نیز گزارش شد یک نفتکش در ۱۱ مایل دریایی شمال شرقی لیما، در مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 520K · <a href="https://t.me/VahidOnline/77694" target="_blank">📅 09:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-zrdgmJUSXruwEgrwvvQzI4x1pbzupSZKGzsDVj-KZWTHnZrfQC81qIS9859eTEnGwsft-7KxfuteaDyWbMZAfPLL3NiWcpXkQIz78JFgZrcIL8zkiSnH0GpYkYRstwRl5NFiK4aMFtCJUiRvaTua9ngdkYtL316k8V9iab75BLy0YeWWhWSiHUNtvwcoiAWVU_cHOdjIvnP3o3MQoShWC0K0K0GGM-fDdjjWpdxT17XTmakoIWnWTeLiM6SblA_XeaF8aLUW-4RpuyZCZSznr9MnNaergJkvIjvChaJMr9BVWeDBvI9V8PLIDPFZVHSLAhu4ZfJoAzpSEPDzhx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس گفت: در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.
او ادامه داد: تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.
او اضافه کرد: بعدتر تصمیم گرفتیم همان سحرگاه خبر مرگ رهبری را اعلام کنیم و به مردم بگوییم به خیابان بیایید.
قالیباف در حالی می‌گوید که همان ساعت اول از مرگ خامنه‌ای مطمئن شده که مقام‌های جمهوری اسلامی تا بامداد روز بعد خبر مرگ خامنه‌ای را تکذیب کرده و اعلام می‌کردند او در اتاق فرماندهی حضور داشته و مشغول راهبری جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 537K · <a href="https://t.me/VahidOnline/77693" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZiAVzvGht_oqUzqNNLiUNmNbS4iOfovkAEtflUE8tFDcJst4SruJK9VOYGFe2PsqaKGpMGuwemG0mz1uvhnpKSVBRfTjCGPulSN_ssjEnQmd9Fml13I7cn2xbDh-J_dGg08x11MygGnJjigHttwCll2XosqcqM51Lh5pqlyFpyQjPfvwDX3ePw0dy5QJXqZR34_VBr0qcrerezC60uZbONYUKkpYXfJo-qyGE8Y5Hpx3F8ZU0VkTPtKVuxPRn1BdwKd8RRT6wZE0gwinpBQoywzM69B8NtuYRijIbOqa7Tq_PH6lUcwAdSUqf04uzZA6pxPh5CMteLvCpyP38sxocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در حدود ۱۱ مایل دریایی (بیش از ۲۰ کیلومتری) شمال شرقی لیما، در استان مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 512K · <a href="https://t.me/VahidOnline/77692" target="_blank">📅 07:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZ6yWgIkQw7jp-eLKIlKZTV4IzVYVFzquEjBbqnkZz63y0Bn2_-wlXpA1P6mJm8IDhieujConi4bjeh7tppFV6vTr_MbCZS05qNXojPad753GxEVDx3LOmzC3xSV_3hcQb2eTlz4O8mWt2XzM86eqU6B9MWqCYwh3FqU16dM-UUMQ9LsvUNCF_r1TS8k5vDSN05gtw6NXvI1Pvd3Y5sLhNeFaJ9DqI1LyVtY85-POWHke_FpRa0IT1zMKgwvMMzBy1JJrnoeCAxwboI3dsae23fCuO87ojZAQyoOqJLKm57yWvhGgUWzIQzLHsYpPoSJRT4S5u9dVq0g5vQGvcV7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آمریکایی و اروپایی آگاه به «ان‌بی‌سی» گفتند که روسیه در حال به اشتراک‌گذاری اطلاعات ارزشمند الکترونیکی و ماهواره‌ای با ایران است که به تهران در جنگ جاری با ایالات متحده کمک می‌کند. به گفته این مقامات، ردیابی ماهواره‌ای و اطلاعات سیگنالی روسیه احتمالا ایران را قادر می‌سازد تا نیروهای آمریکایی را در حملات هوایی با دقت بیشتری هدف قرار دهد، دفاع هوایی خود را در برابر حملات ایالات متحده تقویت کند و در عملکرد تسلیحات ساخت آمریکا اختلال ایجاد نماید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 547K · <a href="https://t.me/VahidOnline/77691" target="_blank">📅 03:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQjfh1cnxSRgh7UKpPbS7YyB0KZRFqLHk8dexe13xPMudRafzeEF4hVEeBHhP2uQxMycku5lXTBqSj9m40Wx6AX1jgbQ7W4M1_imRJpfbDvNFhVPX5RyxLvM26ilDNpNMJq-uNIoi3aiPdeWCoceZbjA3YNAdstbkbLIssC4E50c7NV7RjRkq-yil611IbIvKKsyYFIiYFm42rvB3tsJXsxG3t8H-y5zryaGr8KTtUmL1aiPN9lZKwbVXmf_1S86bDxczcUgIdLvhTbRhGO4juNS5HBcyqb26yk-NdAFKKVcttDnfF5LWimWgftm-NpIVFCczEmaR1BTwQMi_wp_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
ترامپ دستور حمله‌ای تازه به ایران را صادر کرد
"
وال‌استریت ژورنال
به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، طرح حمله جدید به ایران را که در کمپ دیوید ارائه شده بود، تصویب کرده و این عملیات ممکن است از آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز ادامه یابد.
به گفته این منابع، هرگونه پیشرفت فوری در دیپلماسی یا تغییر نظر ترامپ می‌تواند اجرای حملات را متوقف کرده و مسیر مذاکرات را دوباره باز کند.
این روزنامه نوشت یکی از گزینه‌های مورد بررسی، کارزار دو هفته‌ای حملات هوایی فشرده برای تضعیف توان موشکی جمهوری اسلامی است.
مقام‌های آمریکایی گفتند ترامپ معتقد است توافق موقت صلح کارساز نبوده و همچنان بر توقف برنامه هسته‌ای جمهوری اسلامی و پایان کنترل تهران بر تنگه هرمز اصرار دارد، در حالی که تهران از مواضع خود عقب‌نشینی نکرده است.
وال‌استریت ژورنال افزود مشاوران نظامی ترامپ کاهش ذخایر مهمات آمریکا را یکی از مخاطرات احتمالی این عملیات ارزیابی کرده‌اند.
@
VahidOOnLine
اکسیوس:
ترامپ حمله به اهداف انرژی ایران در چند روز آینده را بررسی می‌کند
ترجمه ماشین: دونالد ترامپ، رئیس‌جمهوری آمریکا، به‌طور جدی در حال بررسی انجام حملاتی علیه اهداف انرژی در ایران طی چند روز آینده است، اما هنوز دستور نهایی اجرای آن را صادر نکرده است؛ یک مقام آمریکایی روز جمعه این موضوع را به اکسیوس گفت.
چرا اهمیت دارد:
هدف از کارزار جدید بمباران آمریکا علیه اهداف انرژی و زیرساختی در ایران، تلاش برای واداشتن ایرانی‌ها به پذیرش شروط ایالات متحده در مذاکرات جاری آتش‌بس خواهد بود.
▪️
این حملات ممکن است برای نخستین‌بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
▪️
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین رسانه‌هایی بودند که درباره حملات احتمالی گزارش دادند.
آنها چه می‌گویند:
ترامپ در آغاز جلسه روز جمعه کابینه به حمله احتمالی اشاره کرد و گفت: «خب، ما خیلی سخت به آنها ضربه خواهیم زد و می‌دانید، بالاخره در مقطعی خواهند گفت که دیگر نمی‌توانیم تحمل کنیم.»
▪️
او افزود هرچه ایالات متحده حملات بیشتری انجام دهد، ایرانی‌ها ضعیف‌تر می‌شوند «و بعد کم‌کم از پا می‌افتند.»
▪️
کارولین لیویت، سخنگوی کاخ سفید، به اکسیوس گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در جلسه کابینه گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 524K · <a href="https://t.me/VahidOnline/77690" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fPUbs8YZ9GdHnv1GRRmV5RDlHBddIRDRSdN8tkOSx9xNsK8l_pe_FLL4zSBe2Vkz4Wsa1ROEnPQAPHyOulDGHE3-QqNi9RW9bI5thMVjV263_u6YFtjBoHbDu2xNzGRTxb_v7IJHLHhhiEvDf9-5HWfPVkJIs4Yq0KV1WuGgKgKkFu90TAC0wnMRhw0jjcpIFEFbBHdr_vpSHRCChD4q-eK7KdpyemlVJNyOvoqJdFX2vH8plD9pxSnv_6DRfUIeMfC53hjTRsPaufhBuJ1gko_VjDAwZ0w5mEge9UThrPW8y2M9UU_L7QT8bGb8U8P_W7kc4RnrvXkSJkd8rWZjxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا و اسرائیل برای بمباران اهداف مرتبط با انرژی در ایران آماده می‌شوند
"
سی‌بی‌اس به نقل از منابع
ترجمه ماشین:
واشنگتن — چندین منبع به سی‌بی‌اس نیوز گفتند که ایالات متحده و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین کارزارهای بمباران تاکنون علیه اهداف زیرساخت‌های انرژی در ایران هستند و احتمال انجام حملات در طول تعطیلات آخر هفته وجود دارد.
بحث‌هایی درباره تلاش برای پایان دادن به عملیات تا زمان بازگشایی بازارهای مالی در روز دوشنبه مطرح شده بود، زیرا نگرانی‌هایی درباره تأثیر بمباران‌ها بر اقتصاد آمریکا و جهان وجود دارد، اما زمان مشخصی برای پایان عملیات قطعی نشده بود.
به گفته چندین منبع آمریکایی، اسرائیلی‌ها در جریان قرار گرفته‌اند و در حال هماهنگی با ایالات متحده هستند. این منابع گفتند رئیس‌جمهور هنوز دستور نهایی آغاز حملات را صادر نکرده است.
سخنگوی دولت اسرائیل به درخواست اظهارنظر پاسخ نداد.
یک عملیات مشترک به معنای بازگشت اسرائیل به عملیات رزمی خواهد بود؛ عملیاتی که این کشور در جریان آتش‌بس میانجی‌گری‌شده از سوی آمریکا متوقف کرده بود. از زمانی که تفاهم‌نامه از هم پاشید و ایالات متحده در اوایل ژوئیه عملیات رزمی را از سر گرفت، ایران اسرائیل را هدف قرار نداده است.
به گفته منابعی که بعداً در جریان قرار گرفتند، طرح حمله نظامی روز جمعه در نشست کابینه دونالد ترامپ، رئیس‌جمهور آمریکا، در کمپ دیوید مطرح شد. یکی از منابع گفت برخی از دستیاران کاخ سفید که بر مسائل سیاسی تمرکز دارند، به‌شدت با این طرح مخالف بودند.
زمانی که خبرنگاران در اتاق حضور داشتند، آقای ترامپ گفت: «ما آن‌ها را بسیار سخت هدف قرار خواهیم داد. بالاخره در مقطعی خواهند گفت: “دیگر نمی‌توانیم تحمل کنیم.”»
او در پاسخ به پرسش خبرنگاران درباره احیای دیپلماسی گفت: «فکر می‌کنم ما فقط می‌خواهیم پیروز شویم.»
دو منبع گفتند زیرساخت‌های انرژی، از جمله نیروگاه‌ها و پالایشگاه‌ها، احتمالاً هدف قرار خواهند گرفت.
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، در بیانیه‌ای به سی‌بی‌اس نیوز گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در نشست کابینه خود گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
شان پارنل، سخنگوی ارشد پنتاگون، گفت پنتاگون پیش از آنکه رئیس‌جمهور تصمیم نهایی خود را بگیرد، درباره اهداف اظهارنظر نخواهد کرد.
پارنل در بیانیه‌ای گفت: «وزارت جنگ کاملاً آماده و مهیای عملیات است و می‌تواند در هر لحظه دستورات رئیس‌جمهور را اجرا کند.»
یک مقام پیشین نظامی آمریکا به سی‌بی‌اس گفت، فایده حمله به زیرساخت‌های انرژی این خواهد بود که بر توان نیروهای نظامی ایران برای ارائه خدمات و اداره مؤثر کشور تأثیر بگذارد.
یک مقام ارشد اسرائیلی گفت هنگامی که آقای ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اوایل این هفته دیدار کردند، نتانیاهو او را در جریان سه گزینه برای جنگ قرار داد که یکی از آن‌ها حملات نظامی متمرکز بر مسیرهای تدارک‌رسانی زمینی بود. نتانیاهو همچنین با هگست، وزیر دفاع آمریکا، دیدار کرد.
یک مقام آمریکایی گفت ایالات متحده در جریان این درگیری پیش‌تر به پل‌هایی با کاربری دوگانه — که نظامیان و غیرنظامیان از آن‌ها استفاده می‌کردند — حمله کرده است.
روز جمعه گفت‌وگوهایی در سطوح عالی دولت آمریکا درباره قطع برق سراسر تهران انجام شد، اما تا بعدازظهر جمعه هیچ تصمیمی گرفته نشده بود.
هفته گذشته، آقای ترامپ در تروث سوشال نوشت که در ازای هر حمله به یک کشتی در تنگه هرمز، یک پل یا نیروگاه ایرانی را بمباران و نابود خواهد کرد.
این خبر فوری است و به‌روزرسانی خواهد شد.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77689" target="_blank">📅 00:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORRIKYlIk5gBOq8m49xX2-mU52ZHnkYtKbhqieyr1Wzo0OEihGtSKmlCvWPzH4SGaUIG08abBlbMhhI22a8m01ZyFae-rM7jGS-k7DpK2obi6-CijtVH6XeoSQ-kakjwSuYp93Y9wF6Zzdl7aesSx44MCWHCTiiF_7cpS2bzXv2MhbSXCq-uMsJgDujTHDu3WtX5lTtbozTJEzbUOSmizKJmqBpSv44jPlrPTNf3lX1vRTx3-dGv4U8xDeC-U1Q4g--RxIDYxZLL6XjgSLanRmLWWCIM6-HxMamSigIG5l3n3Zdp-EiWPTL10Q7giIuabweQ24SMCLWE_Puqz9323Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد. این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های…</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77688" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUzqDu64wEDoyb8bgJH4zfOCFGLSxajtL2rQEb4avMQsaj6UnE7Z9umg83mLzAEI-7Ts7uIrs5Xscrzx7M2WcqarbYu4EWSQZqIfSotHpztRAmH4_bozzhjD2K_2CDTJwUopbbxlS5PqRl10WdBrnQBkEPGZOrJ1D5FEFJrK4Rt1w_SshBHFoFzhSa4HSVlRmxVAkwsTUbeYfEH86edQ_2JDCpxIQTY8lRtJOC-qC7IqkCtJC8lXBFCSvmCz1MAOWxitDLVTzOaH__SYxIgYEl2cJHGnn15YnadnvyPk3tk_6FVkFFM0Zb3rUPqre_4KcNQMXI6DH3eU4dYMdEWtnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز جمعه ۹مرداد۱۴۰۵
گزارشی تحقیقی
منتشر کرده، از استفاده سپاه از شبکه قمار غیرقانونی ایران که با آن میلیاردها دلار را به رغم تحریم‌ها جابه‌جا می‌کند.در این گزارش به یک صرافی ارز دیجیتال مستقر در دوبی اشاره شده که  به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
در گزارش رویترز صرافی مذکور «شل‌بیت» معرفی شده و تایید شده است که این صرافی، یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.
بنابر گزارش منتشر شده، «شل‌بیت» صدها میلیون دلار ارز دیجیتال را به «بایننس»، بزرگ‌ترین صرافی ارز دیجیتال جهان، منتقل کرده است. دو شرکت تحقیقاتی حوزه ارزهای دیجیتال و یک تحلیلگر مستقل مدارکی ارایه کرده‌اند نشان می‌دهد نشانی ثبت‌شده صرافی بدون مجوز «شل‌بیت» دفتری در بالای یک هتل ارزان‌قیمت در محله‌ای معمولی و نه‌چندان مطرح در دوبی است. این صرافی توسط یک ایرانی مقیم خارج از کشور اداره می‌شود. رویترز اطلاعات ارایه شده در این زمینه را تایید کرده است.
در بخش دیگری از این گزارش آمده است که یکی از مشتریان اصلی «شل‌بیت»، یک شبکه قمار فارسی‌زبان متشکل از بیش از ۲ هزار وب‌سایت است که توسط دو اینفلوئنسر مشهور ایرانی در شبکه‌های اجتماعی تبلیغ و اداره می‌شود. گفته شده که این دو ارتباطاتی در سطوح بالای حکومت ایران دارند.
یکی از آن‌ها در یک ویلای گران‌قیمت در مادرید فعالیت می‌کند و دیگری تا همین اواخر در یک هتل لوکس در هنگ‌کنگ مستقر بود.
هر دو اینفلوئنسر اشاره شده و همچنین فرد اصلی اداره کننده صرافی «شل‌بیت» در سال ۲۰۲۳ در ایران به اتهام مشارکت در یک پرونده قمار غیرقانونی، محکوم شدند.
مطابق قوانین جمهوری اسلامی «قمار کردن» امری غیرقانونی است و مجازات‌های حبس و شلاق برای مرتکبان به‌دنبال دارد با این‌همه گزارش رویترز تایید می‌کند که این شبکه قمار تازه شناسایی شده به سیستم پرداخت آنلاین ایران که مستقیما تحت نظارت بانک مرکزی است دسترسی دارد.
شل بیت بر اساس گزارش رویترز در مرکز عملیاتی است که شبکه قمار، بانک مرکزی و دیگر نهادهای تحریم‌شده ایرانی را به بازارهای جهانی ارزهای دیجیتال مرتبط می‌کند.
یکی از چهره‌های اصلی این شبکه قمار، «ساشا سبحانی»، پسر یک دیپلمات و سفیر پیشین ایران و دیگری «پویان مختاری»، یک چهره مشهور شبکه‌های اجتماعی و خواننده است که پس از اخراج از دوبی در اواخر ماه آوریل، مدتی بین هتل‌های لوکس هنگ‌کنگ جابه‌جا می‌شد.
پویان مختاری اخیرا و در جریان جنگ آمریکا و اسراییل با انتشار ویدیویی گفت که مخالف جمهوری اسلامی نیست و دچار «تحول فکری» شده است.
تحقیقات رویترز آشکار می‌کند که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال پول به خارج از کشور استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77686" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YGygsKGS0szIQKKNaM--iE57n10Qu9VpVnvN-5HF0nYp1hTDZRy_TnsZ78iX4YR0Pqn44X6Zv-RQji5XI6oojDTK0S35dh_8lIVacTSW81htJskfXzTcRGt2wai59vtPfyzHQ9APJ14pyQwXuPISD3iGBtgEMy66kJwpmHRe3dFmMTgXvcjOWrPte3swYM1ZNsjxN62Lnwz93FwZ64Gd4pLrldmvxeGpX32Rkv48ss-WqXALhIjxc7RkvtstCU74sVxOBMyw3NqIDZOGZsCGYB1TxeaVRBduaoCH1f4Y2aVeWJuXuNSffhM4-5q8iH_hryc8VdYzYVprGt7TDSZhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pWGfADQ7ILq6jXEsNZwtCttpDxLNYGVoIhFUZakaGBAzEf-BJOEm4XZWuIOe4rcQD8g9cviToeLNo_YlL51ci-Rl_rt7wApj78tm0RtMr8MrEzg6SL9J4G1MsSvA7Vz6w1rsAY63rvHFO76R4hAdxdxJenL_TNpBzAUXVzl9eg6ctE2zDsFpZLU4Sp-tShysI2PoQ1BnclMUv9sFPenqTGhLkmTDF26haPUzNghuj1DN6O4MV8YlbuJYNwu3lARi7FGaj_uB_4EqUKc6_7i-ONyikZdEy9LVoNWTWBn-3298anMLGzpXNS4VSW9Usz_iYHQLicfsnPnpoQzAdeZrWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=v8Dged2ZUVIhLEGBSbBKFjRKOmMd3saduGocQESKpJicJY4qB6I2D9Qz9ROF8QtbYxUVOpYr9CgWhXxeHPjgBXRxoOSyhZR-P9JDRyRetz9KEjroIa8EzFmtTq5K2_lO32yYmK7SKidY7SiAiYrZPCqVXlqjUSfsGZaiw9hmADGnaDAckKFaURWVni5_hP5l31jmiHQLJhbJ13GzQ5cFFcmLIU9S9u8kvc0v3kZp0ZwAmohmFxvMueh64g1f1d8t41cBkwpND1h9fQNFP44Y3T0dcESI8uawH40SWsTFAZq7gaTZJczhe29FhTlx-v8KZSZZTIr4E7dlocwkL3OZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=v8Dged2ZUVIhLEGBSbBKFjRKOmMd3saduGocQESKpJicJY4qB6I2D9Qz9ROF8QtbYxUVOpYr9CgWhXxeHPjgBXRxoOSyhZR-P9JDRyRetz9KEjroIa8EzFmtTq5K2_lO32yYmK7SKidY7SiAiYrZPCqVXlqjUSfsGZaiw9hmADGnaDAckKFaURWVni5_hP5l31jmiHQLJhbJ13GzQ5cFFcmLIU9S9u8kvc0v3kZp0ZwAmohmFxvMueh64g1f1d8t41cBkwpND1h9fQNFP44Y3T0dcESI8uawH40SWsTFAZq7gaTZJczhe29FhTlx-v8KZSZZTIr4E7dlocwkL3OZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد.
این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های اسپانیا، پس از این موج ورود مهاجران، حدود ۳۷ هزار و ۵۰۰ نفر به‌صورت داوطلبانه به مراکش بازگشته‌اند.
در جریان تلاش برای عبور از مرز، دست‌کم ۵۷ نفر جان باختند؛ شماری بر اثر غرق‌شدن و برخی دیگر در ازدحام هنگام عبور از موانع مرزی.
پدرو سانچز، نخست‌وزیر اسپانیا، این رویداد را «نقض حاکمیت ارضی اسپانیا» خواند و گفت روند بازگرداندن مهاجران فاقد مدارک قانونی با همکاری مراکش تسریع خواهد شد.
اتحادیه اروپا در شرایط استثنایی به کشورهای عضو اجازه می‌دهد به‌طور موقت کنترل مرزهای داخلی منطقه شنگن را دوباره برقرار کنند.
@
VahidHeadline
پیش‌تر:
هزاران مهاجر از شامگاه پنج‌شنبه تا صبح جمعه با عبور از مرزهای مراکش وارد مناطق تحت اداره اسپانیا در شمال آفریقا شدند
ورود مهاجران در تمام طول شب ادامه داشته و صبح جمعه نیز همچنان ادامه پیدا کرده است.
همزمان، تصاویر خبرگزاری رویترز، هجوم جمعیتی از مهاجران به گذرگاه مرزی میان مراکش و شهر ملیلیه اسپانیا در شمال آفریقا، را نشان می‌دهد.
در سئوتا، دولت اسپانیا برای مقابله با صدها مهاجری که از مسیر دریا و خشکی وارد این منطقه شده‌اند، یگان‌های نظامی را مستقر کرده است.
تصاویر منتشرشده نشان می‌دهد صدها مهاجر با شنا کردن یا استفاده از تایرهای بادی از سمت مراکش تلاش کرده‌اند خود را به سئوتا برسانند و گروهی دیگر نیز با عبور از یک دروازه مرزی زمینی وارد شهر شده‌اند.
@
VahidOOnLine
وزیر کشور فرانسه روز جمعه اعلام کرد پاریس در پی ورود هزاران مهاجر از مراکش به سئوتا، کنترل‌های مرزی خود با اسپانیا را افزایش خواهد داد.
@
VahidOOnLine
فنلاند اعلام کرد از پیشنهاد ایتالیا برای تعلیق عضویت اسپانیا در منطقه بدون کنترل مرزی شنگن حمایت می‌کند. اقدامی که در پی ورود ده‌ها هزار مهاجر به منطقه سئوتا، تحت حاکمیت اسپانیا در شمال آفریقا، مطرح شده است.
@
VahidOOnLine
پدرو سانچز، نخست‌وزیر اسپانیا، روز جمعه نهم مرداد ماه، ورود گسترده مهاجران به سئوتا، منطقه تحت حاکمیت این کشور در شمال آفریقا، را «نقض و حمله به تمامیت ارضی اسپانیا» محکوم کرد.
سانچز پس از موج اخیر عبور مهاجران از مرز مراکش به سئوتا، این اقدام را محکوم کرد و تاکید کرد دولت اسپانیا از حاکمیت و مرزهای خود دفاع خواهد کرد.
@
VahidOOnLine
ایلان ماسک، میلیاردر آمریکایی و مالک شرکت‌های تسلا و اسپیس‌ایکس، در واکنش به ورود گسترده مهاجران مراکشی به شهر سئوتا در اسپانیا، با انتشار تصاویری از فیلم «جنگ جهانی زد»، این وضعیت را به «آخرالزمان زامبی‌ها» تشبیه کرد و نوشت: «وای، اوضاع اسپانیا واقعا دیوانه‌کننده به نظر می‌رسد!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77680" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نشست خبری دولت ترامپ در کمپ‌دیوید
ویدیوی کامل با زیرنویس فارسی:
۱۰۰ مگابایت
نسخه یک گیگابایتی:
اینجا
متن فارسی ۱۶ بازه از ویدیو
بخش‌هایی از متن لینک بالا:
🔻
ترامپ:
در مینه‌سوتا یک حمله سایبری رخ داده و آن را به ایران نسبت داده‌اند.
فکر نمی‌کنم چنین باشد. من مینه‌سوتا را مقصر می‌دانم، چون به‌شدت بی‌کفایت هستند. حمله‌ای سایبری به ۳۰ تأسیسات آب انجام شد و من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم.
آن‌ها دوست دارند بگویند: «اوه، کار ایران بود.» ایران باید خیلی خوش‌شانس باشد. ایران مشکلات بزرگ‌تری از نگرانی درباره مینه‌سوتا دارد.
....
🔻
ترامپ:
جنگی در جریان است. شاید شما آن را جنگ بنامید؛ من شاید آن را عملیات نظامی بنامم، چون آن‌ها دیگر نیروی دریایی ندارند؛ نابود شده است. نیروی هوایی‌شان نابود شده است. هواپیما ندارند.
بخش بزرگی از موشک‌هایشان از میان رفته است. هنوز مقداری دارند، اما بسیار کمتر از چهار یا پنج ماه قبل. ظرفیت تولیدشان تقریباً از میان رفته و ظرفیت پهپادی‌شان نیز تقریباً نابود شده است.
تعداد بسیار کمی دارند، اما هنوز مقداری باقی مانده است. از نظر من اگر حتی یکی داشته باشند، همان هم بیش از حد زیاد است.
🔻
به ویتنام نگاه کنید؛ ۲۰ سال آنجا بودند. به افغانستان نگاه کنید؛ سال‌های زیادی آنجا بودند. به جنگ کره یا هر جنگ دیگری نگاه کنید؛ سال‌ها طول کشید. ما پنج ماه است وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
باز هم مقداری برایشان باقی مانده، اما به‌زودی همان مقدار هم باقی نخواهد ماند.
🔻
مارکو روبیو:
نخستین موضوع، دادگاه کیفری بین‌المللی است؛ سازمانی بین‌المللی و نامشروع. خودشان را نامشروع کرده‌اند، چون ادعا می‌کنند حتی اگر عضو آن دادگاه نباشید، باز هم می‌توانند به سراغتان بیایند.
معنای واقعی آن این است که در آینده نظامیان آمریکایی، رهبران سیاسی و افراد دیگر ممکن است از سوی این دادگاه کیفری بین‌المللی تحت کیفرخواست قرار بگیرند. ...
🔻
ترامپ:
هیچ اطلاعاتی وجود ندارد که نشان دهد آن‌ها دنبال من هستند. البته ممکن است چنین اتفاقی بیفتد.
حرف من این است که این یعنی او نمی‌خواهد از من دفاع کند؛ می‌خواهد از بی‌بی و افراد مختلف دیگری دفاع کند.
افراد زیادی هستند که نباید به این شکل با آن‌ها برخورد شود، اما در حال حاضر هیچ نشانه‌ای وجود ندارد که من یکی از آن‌ها باشم.
....
🔻
پیت هگست:
... تعجب می‌کنید چرا حوثی‌ها در این درگیری حضور ندارند، با اینکه نیروی نیابتی ایران هستند؟ چون ۴۵ روز سنگینی قدرت آمریکا را احساس کردند. و شما شجاعت انجام این کار را داشتید.
🔻
اسکات بسنت:
... در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگ‌ترین بانک ایران فروپاشید. بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد.
اکنون تورم آن‌ها ۱۸۰ درصد است. قادر به پرداخت حقوق نیروهایشان نیستند و به دستور شما در سراسر جهان به‌دنبال دارایی‌هایشان می‌گردیم.
این پول به مردم ایران و آمریکایی‌هایی می‌رسد که از اقدامات ایرانی‌ها آسیب دیده‌اند؛ چه در ماجرای ناو یو‌اس‌اس کول، چه پادگان‌های لبنان، یا حملات ایرانی‌ها به آن کشتی‌های در حال خروج.
مشارکت در این کار برای من افتخار بوده و مشتاق ادامه آن هستم.
🔽
درباره ادامه جنگ:
🔺
خبرنگار:
آقای رئیس‌جمهور، در ۱۰ روز گذشته حملات میان ایران و ایالات متحده را دیده‌ایم. چگونه آتش‌بس را احیا می‌کنید و دیپلماسی را دوباره از سر می‌گیرید؟
🔻
ترامپ:
فکر می‌کنم فقط می‌خواهیم پیروز شویم. عملکردمان بسیار خوب است. تلاش می‌کنیم تا جایی که در چنین شرایطی ممکن است، ملایم باشیم، اما آن‌ها در حال نابودشدن هستند.
دیگر نیروی دریایی، نیروی هوایی یا پدافند هوایی ندارند. این به آن معنا نیست که هیچ توانی ندارند؛ مقداری دارند، اما بسیار اندک است.
فقط می‌خواهیم پیروز شویم. نمی‌خواهیم آن‌ها این توان را داشته باشند. موضوع بسیار ساده است.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران سلاح هسته‌ای نخواهد داشت و نمی‌تواند داشته باشد. اگر چنین سلاحی داشتند، خاورمیانه تا الان نابود شده بود.
اگر من برجام، همان توافق اوباما، را متوقف و لغو نکرده بودم، آن‌ها اکنون سلاح هسته‌ای داشتند.
فکر می‌کنم اسرائیل دیگر وجود نداشت؛ در بخش‌های بزرگی از خاورمیانه و شاید کشورهای دیگری در قاره‌های مختلف نیز، چون صادقانه بگویم این افراد دیوانه‌اند.
بنابراین نمی‌توانند سلاح هسته‌ای داشته باشند و نخواهند داشت.
🔺
خبرنگار:
[پرسش ناقص و نامفهوم درباره آنچه در چهار یا هشت هفته آینده باید انتظار داشت.]
🔻
ترامپ:
می‌دانید، به آن‌ها حمله خواهیم کرد؛ حملات بسیار سختی به آن‌ها وارد خواهیم کرد. بالاخره در مقطعی خواهند گفت: «دیگر نمی‌توانیم تحمل کنیم.»
🔺
خبرنگار:
آقای رئیس‌جمهور، بازگردیم به ایران. گزارشی منتشر شده که ارتش پیشنهادی داده است تا ظرف ۱۰ یا ۱۴ روز حمله‌ای بزرگ و سخت انجام دهید—
🔻
ترامپ:
ما همین حالا هم حمله بزرگ انجام داده‌ایم. منظورتان از «بزرگ» چیست؟
آن‌ها ۱۵۹ کشتی داشتند؛ تمام نیروی دریایی‌شان همین بود. هر ۱۵۹ کشتی، تمام نیروی دریایی‌شان، در کف دریا قرار دارد. من این را حمله بزرگ می‌نامم.
تسلیحات پدافند هوایی بسیار خوبی داشتند، اما کار نکرد و همه آن از بین رفته است. تمام رادارهایشان از بین رفته، رهبرانشان از بین رفته‌اند؛ همه‌چیز از بین رفته است.
🔻
ترامپ:
برای مثال، خواندید که پنج موشک شلیک شد. سرعتشان ۸۶۰۰ مایل در ساعت بود.
فکرش را بکنید؛ اگر با خودرو ۶۰ مایل در ساعت بروید، کمی سریع به نظر می‌رسد. این موشک‌ها ۸۶۰۰ مایل در ساعت سرعت داشتند و موشک‌های بزرگی بودند. به سوی اردن شلیک شدند و نیروهای ما آنجا بودند: بنگ، بنگ، بنگ، بنگ، بنگ.
[خنده حاضران]
این می‌توانست کلیپ صوتی خوبی باشد! پنج موشک شلیک شد و هر پنج موشک را پیش از آنکه نزدیک شوند، ساقط کردیم. هیچ کشور دیگری چنین توانی ندارد.
🔺
خبرنگار:
آقای رئیس‌جمهور، گفتید هنوز مقداری توان برایشان باقی مانده است. آیا آمریکایی‌ها باید آماده باشند که این حملات متقابل ادامه پیدا کند تا زمانی که ایران دیگر توان حمله فوری نداشته باشد؟
🔻
ترامپ:
ضعیف‌تر خواهند شد. شاید اکنون کمی قوی‌تر شوند، اما ضعیف‌تر خواهند شد.
🔺
خبرنگار:
و بعد به‌تدریج از نفس می‌افتند؟
🔻
ترامپ:
بله، فکر می‌کنم همین‌طور است. احمقانه است که بگویم نه. همیشه باید مراقب باشید.
🔺
خبرنگار:
وضعیت مذاکرات چگونه است؟ چه کسی از طرف دولت در مذاکرات حضور دارد؟
🔻
ترامپ:
آن‌ها همیشه می‌خواهند مذاکره کنند، اما بارها زیر قولشان می‌زنند. استیو در حال مذاکره است. جرد هم هست؛ افراد بسیار خوبی داریم. جی‌دی به‌شدت درگیر است. افراد فوق‌العاده‌ای در حال مذاکره هستند. مارکو هم درگیر است.
افراد بسیار خوبی داریم؛ بهترین‌ها را. اما آن‌ها توافق خواهند کرد.
برای مثال، درباره موضوع هسته‌ای صحبت می‌کنیم و هفت ساعت آنجا می‌نشینیم و درباره برنامه هسته‌ای حرف می‌زنیم. می‌گویم چرا هفت ساعت؟ ده دقیقه کافی است؛ پنج دقیقه وقت دارید، باید حلش کنید.
اما هفت ساعت صحبت می‌کنند، بعد بیرون می‌آیند و من می‌گویم درباره موضوع هسته‌ای گفت‌وگو کردند. آن‌ها بیرون می‌روند و می‌گویند: «ما هرگز درباره موضوع هسته‌ای صحبت نکردیم.»
می‌گویم چرا؟ چرا چنین چیزی می‌گویند؟ تنها کاری که می‌کنند این است که من را عصبانی می‌کنند.
🔺
خبرنگار:
با توجه به آنچه گفتید، باور دارید می‌توان با ایران به توافق رسید؟
🔻
ترامپ:
بله، می‌توان. ببینید، دارم اعتمادم را به آن‌ها از دست می‌دهم، چون دروغ می‌گویند و واقعیت را تحریف می‌کنند.
چند روز پیش پنج موشک شلیک شد. ما آن‌ها را ساقط کردیم، اما در میانه مذاکره بودیم. منتظر تماس استیو بودم تا ببینم مذاکرات چگونه پیش می‌رود؛ در عوض پیت تماس گرفت و گفت: «آن‌ها همین حالا پنج موشک به یکی از پایگاه‌های ما در اردن شلیک کردند.»
خوشبختانه نیروهای ما تجهیزات را به کار انداختند. کارکردن با این تجهیزات بسیار پیچیده است. از این افراد می‌پرسید کجا درس خوانده‌اند و پاسخ می‌دهند ام‌آی‌تی یا کلتک؛ دانشگاه‌هایی که معمولاً با نیروهای نظامی تداعی نمی‌شوند.
افرادی فوق‌العاده باهوش این تجهیزات را اداره می‌کنند. وقتی چنین افرادی نباشند، شلیک‌ها خطا می‌رود، سامانه ایمنی خطا می‌کند یا دقت کافی وجود ندارد. ما افراد فوق‌العاده‌ای داریم.
فکرش را بکنید؛ چند ماه پیش در یک بازه کوتاه ۱۱۱ موشک به سوی ناو هواپیمابر آبراهام لینکلن شلیک شد؛ ناوی بزرگ و زیبا و از نظر طراحی یکی از زیباترین کشتی‌ها.
هر ۱۱۱ موشک مدت‌ها پیش از رسیدن به ناو ساقط شدند. در چند مورد تقریباً همان لحظه‌ای که پرتاب شدند، سرنگون شدند. فناوری باورنکردنی‌ای است.
ناوی که میلیاردها دلار ارزش دارد و موشک‌ها به سوی آن در حرکت‌اند؛ هر ۱۱۱ موشک ساقط شدند. من با افرادی که این کار را انجام دادند صحبت کردم. دوست دارم به افراد پاداش بدهم؛ من رئیس‌جمهورم و با آن‌ها تماس می‌گیرم. آن‌ها کاملاً خونسرد بودند.
🔻
خبرنگار:
آقای رئیس‌جمهور، در دو هفته گذشته سنتکام حملاتی انجام داده است. سنتکام گفته هدف این حملات کاهش توان ایران برای مختل‌کردن تردد در تنگه هرمز بوده است. چند حمله دیگر لازم است تا این توان به‌طور چشمگیری کاهش یابد؟
🔺
ترامپ:
هیچ‌وقت نمی‌توان دانست. بیشتر مردم تا الان تسلیم شده بودند. آن‌ها دیگر نیروی دریایی یا نیروی هوایی ندارند. بیشتر مردم تسلیم می‌شدند، اما آن‌ها نشده‌اند. از این بابت به آن‌ها اعتبار می‌دهم. سرسخت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77678" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ffqLLWwQo5-Xr8jjueKiMRPOPF_0y3UYrNHwIpXybyLJR5sSWnSg0hllOaQWsP0peOUjbebuiOPd8apJC7Y7naxXQua692wrr-C1KqJdBw0R5doEpvTkkxG-YRPR5yIR5yXgUyWYQ4n3gXWmcYsJEkXZpLJFn3BMxes5a8bi5X_Cq1iuG3A8QWtQxYe5N96ghyWp1jThSYtuwXpXq8pXUFUIsT5CyHUCk7FTTjYwRZ_IQlmaVc_I_kY7yy1XQrgv4ZoTbataPdLgWG82o2zpSjRSsX5dIvxyKm6_BF6zHOSnAXw9wm6n_4cUZKD6fH58CNwE_yic9qTLnT0MibQmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
✅
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77677" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hLC9D5IRTg__sTWacadM_OLA2AG76BPrxgGgx6RjNhtyPDze3zxm8MgCYcaEfZwdpSh4x8W6GFgdUXgoZYnrE0V0h7QT5IFd9poqat4Qrp31YiAOccr9TQEOLpWOYk5sByiEB-9qfqbB-DHDzSAACegyg5xK8p7eOVqqFDkpJ2MxRWyCFY1MRwMjlmnw0xMB5BuzAwsBIoOFe9LlOBFLyEVMMsJmp6PEWzy2tMnT-klzjHV_XXHLTX3SBOSCQpFU2_r4W45fiId4nyzLDWy41BoBVCTrFHjvsXAEZKXA_HkOHPVGY3hRN7WkA5O1L0N8XlHQUS59I2oqgpo-JnSeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دوروف، بنیان‌گذار تلگرام، یک روز پس از آنکه اعلام کرد روسیه او را به دلیل مخالفت با درخواست‌های این کشور برای اعمال سانسور و نظارت گسترده بر کاربران، در فهرست «تروریست‌ها» قرار داده است، با انتشار تصویری از ملاقات مقام‌های طالبان با سرگئی لاوروف، وزیر خارجه روسیه، به این اقدام واکنش نشان داد.
دوروف در این تصویر که در شبکه اجتماعی ایکس به اشتراک گذاشت، عکس خود را با برچسب تروریست، کنار تصویری از دیدار مقام‌های روسیه با مقام‌های طالبان قرار داد و زیر عکس دوم نوشت: «شرکای مورداحترام» و برای عنوان این تصویر از عبارت «گیج نشوید» استفاده کرد.
دوروف پیش‌تر در ایکس خبر داده بود که روسیه به دلیل خودداری او از اجرای خواسته‌های این کشور برای نظارت گسترده و سانسور در تلگرام، نامش را در فهرست «تروریست‌ها» قرار داده است.
او همچنین به کنایه نوشت که بر اساس قوانین روسیه از «انتشار اطلاعات در اینترنت» منع شده است و افزود: «به نظر می‌رسد مقام‌های روسیه درباره اینکه چه کسی می‌تواند چه کسی را از اینترنت محروم کند، دچار سردرگمی شده‌اند.»
روسیه تنها کشور جهان است که رژیم طالبان را به رسمیت شناخته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77676" target="_blank">📅 19:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvCwJ5YC50BNuIR-9BtqBPaUsAwrdUrpFjzInGl07vFcZ-rCOUhhue4v7SUplStuzXse-YhxwS2ZWzVO_cl7sJ_EYMxIpTXXBxWdiir6sf2WTO1CobF7tnAdiDShZZzj0POh7aKzkg8of1PmLUjUe_-rMiMAJVEPUQ5UYBNRA202AGfHd59NohOidZuYHa2z2k4Ktp4BRltxpgp74BByTsd1kSBUlf_YtUr5_0VdcG5Rs_3-TH7uL-ajHr7v3nJnDCBrwYXzAL0C5w1vjKxMNouaz0paUAmtzFZ9ikU85L7F--kOEYt32aPjxW33GwHdY9SZkuucveT66fg-MDPHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن عاملی، امام جمعه اردبیل، در خطبه‌های نماز جمعه این شهر گفت: «نتانیاهو در دیدار با ترامپ گفته قدر مرا بدان، من جلوی موشکهای جمهوری اسلامی را گرفته‌ام. ایران موشک هشت هزار کیلومتری دارد و به راحتی می‌تواند خانه تو را با موشک بزند. من جلوی ایران را گرفته‌ام.»
او ادامه داد: «ترامپ همیشه از نتانیاهو گول خورده و حالا محل بحث است که آیا این بار هم گول خواهد خورد یا نه.»
امام جمعه اردبیل افزود: «ترامپ پهلوان رسانه‌ای است، عملیات ما کمر او را شکست. او هر وقت شکست می‌خورد به جنگ رسانه‌ای پناه می‌برد و خود را پیروز میدان نشان می‌دهد. اگر این کار را نکند دق می‌کند و می‌میرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77675" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5uQnq-PjCtnOcxD-1i5imuEXM8WIXxocf1Dgm-gXHolFQ-I9vzyp70lXL3m6GSzOvvpbP-LKw6OoZ5Jpm5Md0mCeS2k7Ja5oxm00QOx-TzNPqamv88mp-NgiGnjpQjoBmc-mjTkTQKzopfv9KcVPk-cLZZDtapB9hiWxShbI77Y0N6GBFcRa45y3nZtlJbn3lGcdFWHJjFwMc380B6u0vxHtMH7mSMNAH-e7_gMHoFuLwAyUSMe0uPBckXPVCwW2WTFhk8C9wCJYPSqbQOHkmEcrewIC2X84pTrOrhYIJ6ey7Sq1x660Hni3b5txZvinPTfyIHyIIFQ27EdFr6oVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس‌جمهور آمریکا، روز جمعه ۹مرداد۱۴۰۵ در گفتگو با شبکه «فاکس‌نیوز» گفت درگیری با ایران «به‌خوبی پیش می‌رود» و با اشاره به حملات ارتش ایالات متحده اعلام کرد که ایران در نهایت چاره ای جز عقب‌نشینی و تسلیم نخواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77674" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMgSc2WJzNfQhu3nUCtadO-mRw5uUmChHp3kKGItv16XhrD0tqK2uUzhC1K17F1hVe1oz8EFC8GiO_j0JNlvDYBtQBEI33r5Dugb6xFcmkXUPl06_DdRkyoSbUisaRPUaEChYbPg_jkj-XOzG43WuqaSU7isXFRv9i0LQTPT92lELksl2-n76CqLHs6uKAgFA_t3BEjzEDgGtkkmNuDo-1zQq--MmymG6-tARLBaN4hbj-Ozodbzwub0wkE6Lkvyz9Y35Bl18j7NBnbKQWjadVQr2umaUWCAMuA_7bhK4S6a2CSI2coLB3-iUkOiagEnySx1xnvLc-8e2okMIGxUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز جاری و در میانه تشدید تنش‌های خاورمیانه، نشست کابینه خود را در اقامتگاه کمپ دیوید برگزار می‌کند.
این نشست در شرایطی برگزار می‌شود که دونالد ترامپ در تلاش است راهی برای پایان دادن به جنگ با ایران پیدا کند و همزمان قیمت بنزین را که به تهدیدی برای جمهوری‌خواهان در انتخابات میان‌دوره‌ای نوامبر تبدیل شده، کاهش دهد.
انتظار می‌رود سیاست خارجی و موضوع جمهوری اسلامی بخش عمده دستور کار این نشست را تشکیل دهد. ترامپ درگیر حملات متقابل علیه اهداف نظامی در ایران است.
ترامپ برخلاف برخی رؤسای جمهوری پیشین، در دوره ریاست‌جمهوری خود کمتر به این اقامتگاه کوهستانی ریاست‌جمهوری در غرب ایالت مریلند رفته، و این سومین سفر او به کمپ دیوید در دوره دوم ریاست‌جمهوری‌اش خواهد بود.
@
VahidHeadline
چون جمعه هم هست و بازارهای مالی تعطیل میشن باعث توجه بیشتر هم شده. دیشب، توییتر:
فردا ترامپ قبل از رفتن به باشگاه گلفش در بدمینستر، توقفی در کمپ دیوید داره. در هر دو باری که به کمپ دیوید رفته اتفاق خاصی افتاده. اولینش حمله بمب‌افکن‌های B-2 به نطنز بهمراه داشت، دومیش هم توافق با رژیم...
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77673" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSPQlxk427tEOqXxmo2oFJzAfv5k8vzoSUHtHbvNqhpg_Ckj4m_9yxDyckX7ZW_rFakNzxNDogQlONt84JUOW_Z_HN62KqWGPfyaXJryrK4Tx4M-lbxx5LLG-o475W6RTS4RWZLMNU12UqRzw8zNe3X5oJQ2NMFfcAYlXty6RTH4ID7t6bGHlh2K_xdJWZlvSUgCburm40_YefS0Zn-21zkiKBHfX_tFm00xPnFIMquAIMdSG4qTjn0Tk2FOKQYngqsibAA682dtznqgGOHQgzZlwRpJRvBwbguz5O-PRJIFEWzVYpwhF8eOXZTW40jmKqZXcJ5sR7RX_Z24X6aABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی رسمی وزارت دفاع کویت اعلام کرد نیروهای مسلح این کشور، بامداد روز جمعه نهم مرداد ماه، چند پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده و آنها را منهدم کرده‌اند.
سعود عبدالعزیز العتیبی در بیانیه‌ای در شبکه اجتماعی ایکس نوشت: «تجاوز گناه‌آلود ایران تعدادی از تاسیسات حیاتی و نظامی را هدف قرار داد که اهداف متخاصم رهگیری و منهدم شدند.»
او افزود: «در نتیجه سقوط ترکش‌ها، خسارت‌های مادی وارد شد، اما هیچ تلفات انسانی ثبت نشده است.»
پیش از این بیانیه، ارتش جمهوری اسلامی با انتشار اطلاعیه‌ای از حمله به پایگاه احمد الجابر، محل استقرار ارتش آمریکا با «پهپادهای انهدامی» خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77672" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8X0cw8oG6SP4ScVIXud4p_cHhbSBO4Ry-sRZnhYx0ZcUze4sPlDHnGUvTdqVk7xVERAMBKOJK_xdstbSBMq2JHLeOWVc2V_Rn-N4N1sxievaSmB2K8Kc976ZSJuphWW6lfMQrkb7u7rbNilK21yL-Ud9b0wiXagJFG__BdcLDYrB4VGigxSENuqFJtopfdt7ZyZy6sYUOzlrldTxDkKG8_C4Aed9bJq8_mVy5qjir0kVlVSEK_oYfovgMP80KE3ThDgYGpulcA6FAN2ACvWj0XovFlQrAbsQQyAd30dDV9UcQ_DzT0mKUyY4vbUFHMMqC2RA6bcMUqc3CwPQ2WoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، در پی اعلام فرماندهی مرکزی ارتش آمریکا مبنی بر تکذیب ادعای سپاه دربارهٔ بسته بودن تنگه هرمز، با انتشار بیانیه‌ای دیگر با پافشاری بر ادعاهای قبلی‌اش گفت به دو نفتکش دیگر حمله و آن‌ها را متوقف کرده است.
سپاه در کنار این بیانیه که روز جمعه نهم مرداد منتشر شد، همچنین تصاویری از یک نفتکش را که در میان شعله‌های آتش در تاریکی می‌سوزد منتشر و تاریخ آن را روز جمعه اعلام کرد.
سنتکام بعدازظهر پنج‌شنبه سه ادعای مطرح‌شده از سوی سپاه پاسداران و رسانه‌های نزدیک به آن دربارهٔ بسته بودن تنگه هرمز، انهدام سه جنگنده اف-۳۵ و عبور یک نفتکش ایرانی از محاصره دریایی آمریکا را را «نادرست» خوانده و گفته بود این ادعاها با واقعیت مطابقت ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77671" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=HsFpyXGwFODWs2e3WvuRvsYKOK4PRFRTkV-YW_pIJvUtjAWnhYWBA_ziEne9AMZx9XiLzAjHh1LNr9zct6DID1f1uVnGYKjg-jlgTiGVDiiHT2kU31zntcYTDxAYAECbdRP5XZM0f8dpcPIesvPEYlWKy9x6lv8UQID3Wyfg_3N8QdRCNqt7R8HYmkkHDqGQ6u7Qc8qVpyH2cPNFc9rolMdDHqoPQ1gwsyEMfGBsjGVHLvxYYGKDMXMhLPvpJKVx5Tr-wpl9C1fHk7vbs6etNT4gDeSQQvHGbZwALaahwsq5KCL5jELyDXT7_tzQSjF0zTuUq8QINSlab8Twr_PTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=HsFpyXGwFODWs2e3WvuRvsYKOK4PRFRTkV-YW_pIJvUtjAWnhYWBA_ziEne9AMZx9XiLzAjHh1LNr9zct6DID1f1uVnGYKjg-jlgTiGVDiiHT2kU31zntcYTDxAYAECbdRP5XZM0f8dpcPIesvPEYlWKy9x6lv8UQID3Wyfg_3N8QdRCNqt7R8HYmkkHDqGQ6u7Qc8qVpyH2cPNFc9rolMdDHqoPQ1gwsyEMfGBsjGVHLvxYYGKDMXMhLPvpJKVx5Tr-wpl9C1fHk7vbs6etNT4gDeSQQvHGbZwALaahwsq5KCL5jELyDXT7_tzQSjF0zTuUq8QINSlab8Twr_PTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌تر در صبح جمعه:
ارتش جمهوری اسلامی ایران مدعی شده است بامداد جمعه ۹ مرداد، پایگاه هوایی احمدالجابر در کویت را با پهپادهای انهدامی هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای اعلام کرد در این حمله، آشیانه جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات ارتش آمریکا در این پایگاه هدف قرار گرفته‌اند. این ادعا تاکنون از سوی فرماندهی مرکزی آمریکا، سنتکام، یا مقام‌های کویتی تایید نشده است.
احمدالجابر یکی از پایگاه‌های مورد استفاده ارتش آمریکا در کویت است و در گذشته نیز ارتش جمهوری اسلامی بارها از حمله پهپادی به مواضع آمریکا در این کشور خبر داده است. در یکی از حملات پیشین، ارتش جمهوری اسلامی مدعی شده بود ساختمان‌های اداری و سامانه‌های جهت‌یاب در پایگاه عریفجان، محل استقرار بالگردها در اردوگاه العدیری و ساختمان استقرار نیروهای آمریکایی در احمدالجابر را هدف قرار داده است.
ارتش جمهوری اسلامی حمله ادعایی بامداد جمعه را واکنشی به حملات اخیر آمریکا به ایران توصیف کرده است. رسانه‌های ایران پیشتر از حمله آمریکا به بخش‌هایی از جزیره قشم و کشته شدن شماری از غیرنظامیان در این حملات خبر داده بودند.
با این حال، تا زمان انتشار این گزارش، مقام‌های آمریکایی و کویتی درباره وقوع حمله یا میزان خسارت احتمالی آن اظهار نظر رسمی نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77670" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GF4T3cYgIip9L92PUzuUsL9YaVD4zBSLfIrHhD3ExuoYgNxbmwp359hclXJD7vFBPYmk12euMZllt4Kykvkg0P56u6nn8OYD2rhbGfIClKwV8qRsjauvdzbgZY80QLLL4SWb_0c3ztRkRrREGyZYbqIxCf6yxWEvLcQV_HI8PMXm_Gm5GINF37DYBLaWkcuVcuuM5hl5MUOwx2lx21khdzA05LWwXxJMAcZzLyAzBIpZho-muAJcMskbzN8yotwRNAsuvwbANpZi-ZMktmS90neIBTYFDECJsbh4J-55xaMh0sL3LTvDzxdRwQ_67SjzwSnTrhYTCJGO7yB7YTADuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oYfgDaqZuTI4KDKInfGqdZUGEpWBtpNnC06aGuf6yisaqnkoneK3or9juVqVs_ewVq9kvWHgs4nIbxqP6rc-7td0Pv6IHvJElEbInEkiEojnOUNGA303vcyEipU8gFXPNq4eQT3HOn-WqpThgrzs8L7RqobPV7ACwVu8HIf7Wj-f4KRW3IqSDl1mrSBplZCnRMtP4zff8TeR5lXiNFHyIAIFXH0PsL5WzgV-FaytQPu3yl1Ghyj3qEY21QpvJVn7bV3SLrRCnRQCjzKrWV90X0ta3SdxZhIg1_tSuHoe1MTNJkmebvzcIcTtUuz41pu2dOCS-DpV9DEIDaSWkgqEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HfDZJltC8bhs6dzUT6bnZvzHZVfYLeQmhTeogZrcQMU6djBODVyWU-S-7uuZ_0RuEDkU8Hz4DDvI3fYRE8LCm1HMgAmiMCVprXrvIPPGQNBvo5VTxvFw6wzEadkb3--V6c3bOk0Y897AoORI1rfgW9hkNKV-4K2MkYQxM0UrPnWZZiY1VWUcIXCZXRD61BT3bz0CZPmMZ4h0vZ8S2CrwDNsAhPL3-PWOevK1K15ePiJ3zHt-25CLTba1VdswlM2haTA1Gn5ssd0oP5x_NC9uY745CtCvTuYJ3Lyyw4cWVfg12FXPqYxdl3AHp9a5ytiVtGIipbQmKGKvbbxRTJPuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jUuv91z2Ik2aMiXlYptiSWyBy_Qu0GNHMLUNQU1qqYzf2JXArSou6P4PQGmnc-wR2LD7N8gK5_riYQxesacZ_uPJIK-43V3i5WkmdqiRB_fbXmX0gSjD51YNczMKfSuTbmWGmNKDIqVaPMKJnMHo-rxXfataUzhztGoJbvV_9jjsYaatiiSTSEesHqhPASqbGVlVP_SrqpZ96ZIvZtcpj3dqSzP8JstOTYURFiYSnPnXC2WgR-YS4-f8y1WzAmqQqmjPhtGe2wG6B9kGI_u4MwQVueXrBLfPZFH7PGwsCVz9I6JtSZ0DzcyZvdi3ic_VjjinZ4AQpyCUueAMnP-69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TctXhNDFplntNZpWgXFqDwGCsWN4byncyHLkGMeDCDRajETE06WBs52g9fapPNryFe-okIfHiVFL3okOA51nb4oCwllW2IEXbP6paFkmSbgHrIfK55hlfjVIs48VpsD6wiZ4ewDbuMbrtqmmjRO8Spm6NPMmFe27BGLhmujyTOV0DBSDo1zxKrJ99tL_2jQrI7mcLYg1u-CTfid1k6pdEA5a1gCdxE5nJKfK4c60zffzOFWs2IEwRR9OIXZ707cM-zlW8WhAZ6fgg35t983oBhF2kE63LVonIXHlbS7TJKnELmk5wkNDx0sqtc2cF_i4BtcAFYEF4LrzTVbAJa7Tsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=CS9LM-U3IFz4pMiSx8JcdXCbS5-gEkLqD0udoPzOxLdMg_rOJajKx9dJ49ycC8-RjiKAOQrZB9kuMoFZYAeRONQDerbsAlzZon7k9ljCDDOw4L9fJUJkdHx-16W1TShECoWWng7xSIeD3jDj7vn0g3Gvc4imxsD2WFKPPsGa2akrOU02lWlaB3KqLCpImknKw9XMFeiv2a-95UcJI0oetqhHMOUoOxbHy_kU9sskF65YwCSlaXZw7lW9uk7KVbidQcSdCmEyPVJOPUY_lQ_AzTDRnJCPiwP3BCwV25jh5KNpNhJ4D3LI9aDiYC_bC0xPy6KofpvbQLJpdEaIX5LasA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=CS9LM-U3IFz4pMiSx8JcdXCbS5-gEkLqD0udoPzOxLdMg_rOJajKx9dJ49ycC8-RjiKAOQrZB9kuMoFZYAeRONQDerbsAlzZon7k9ljCDDOw4L9fJUJkdHx-16W1TShECoWWng7xSIeD3jDj7vn0g3Gvc4imxsD2WFKPPsGa2akrOU02lWlaB3KqLCpImknKw9XMFeiv2a-95UcJI0oetqhHMOUoOxbHy_kU9sskF65YwCSlaXZw7lW9uk7KVbidQcSdCmEyPVJOPUY_lQ_AzTDRnJCPiwP3BCwV25jh5KNpNhJ4D3LI9aDiYC_bC0xPy6KofpvbQLJpdEaIX5LasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۰:۳۷ درباره پرتاب موشک از یزد
همین الان از یزد موشک فرستادن ساعت10:37
۱۰:۳۵ پرتاب موشک از یزد
سلام الان موشک زدن از یزد
از یزد موشک بلند شد ۱۰:۳۷
از یزد موشک زدن الان
وحید جان همین الان ساعت ۱۰.۳۲ پرتاب موشک از یزد
وحید جان همین الان از یزد موشک زدن
جمعه ساعت ۱۰:۳۶
یزد ۱۰:۳۵ یه موشک زدن
بعد از مدت ها جالب بود سمت جنوب پرتاب شد
همین الان از یزد موشک شلیک کردن
۱۰:۳۷از یزد موشک زدن
همین الان از یزد موشک زدن
جمعه نهم امرداد ساعت۱۰/۳۰
سلام وحید جان همین الان از یزد موشک پرتاب شد
سلام خوبین الان موشک از یزد رفت
شلیک  یک موشک الان از یزد
وحید الان موشک از کشور یزد زدن
همین الان ساعت ۱۰.۳۶ دقیقه از یزد موشک زدن
شلیک موشک از یزد به سمت جنوب
ساعت ۱۰.۳۶
سلام ساعت ۱۰:۳۵ یک موشک از یزد بطرف جنوب کشور شلیک شد
از یزد موشک شلیک کردن ولی مسیر متفاوت از قبل بود
سمت بندر و جنوب میرفت
ساعت ۱۰:۴۰ صبح یزد  موشک پرتاب شد؛ صداش خیلی بلند بود
سلام جمعه ساعت ۱۰:۴۰ از یزد موشک پرتاب شد
۱۰:۳۷ از یزد موشک زدن جمعه ۹مرداد
سلام آقا وحید ۱۰:۴۲ از یزد موشک شلیک کردن
موشک از یزد زدند
وحید جان شلیک موشک از یزد
چند دقیقه پیش
ساعت ۱۰:۳۵ از یزد موشک زدن
از یزد همین الان موشک زدن
امروز جهتش سمت جنوب شرق بود
بر عکس روزای قبل که روی شهر رد میشد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77663" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اکسیوس:
ترجمه ماشین:
ترامپ از توافق «تاریخی» برای خلع سلاح حماس و بازسازی غزه تمجید کرد
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اعلام کرد که «هیئت صلح» او با حماس به توافقی دست یافته است که بر اساس آن، این گروه خلع سلاح می‌شود و کنترل امور غیرنظامی و امنیتی غزه به یک دولت جدید فلسطینی متشکل از تکنوکرات‌ها واگذار خواهد شد.
چرا اهمیت دارد:
در صورت اجرا، این توافق تحولی چشمگیر در طرح صلح ۲۰ ماده‌ای ترامپ برای غزه خواهد بود و مسیر بازسازی این منطقه ویران‌شده را هموار خواهد کرد.
▪️
اما این توافق مستلزم آن است که حماس و اسرائیل طی حدود هفت تا هشت ماه، مجموعه‌ای پیچیده از اقدامات متقابل و مستقل را که اجرای آن‌ها راستی‌آزمایی خواهد شد، به انجام برسانند.
▪️
مقام‌های اسرائیلی همچنان به‌شدت تردید دارند که حماس سلاح‌های خود را تحویل دهد؛ در همین حال، اظهارات یک مقام ارشد حماس نشان می‌دهد که ترتیب خلع سلاح و عقب‌نشینی اسرائیل همچنان ممکن است محل اختلاف باشد.
آنچه می‌گویند:
ترامپ عصر پنج‌شنبه در شبکه تروث سوشال نوشت: «امروز، هیئت صلح به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی گروه‌های مسلح دیگر در غزه دست یافت.»
▪️
او افزود: «این گامی عظیم به‌سوی صلح و امنیت پایدار است.»
وضعیت کنونی:
دو مقام آمریکایی گفتند حماس پس از چند ماه مذاکره با میانجی‌گری قطر، ترکیه و مصر که یک مقام ارشد دولت آمریکا آن را «بسیار حساس» توصیف کرد، با مفاد توافق موافقت کرده است.
▪️
این مقام ارشد آمریکایی گفت انتظار می‌رود اجرای توافق طی هفته‌های آینده آغاز شود.
▪️
یکی از مقام‌های هیئت صلح گفت این نخستین بار است که حماس و دیگر گروه‌های فلسطینی در غزه با غیرنظامی‌کردن این منطقه و واگذاری مسئولیت امنیت و خدمات غیرنظامی به یک دولت تکنوکرات موافقت کرده‌اند.
بر اساس این توافق،
حماس از هرگونه نقش در اداره غزه صرف‌نظر خواهد کرد. «کمیته ملی اداره غزه» موسوم به NCAG به‌عنوان جایگزینی برای حماس و تشکیلات خودگردان فلسطینی فعالیت خواهد کرد.
▪️
مقام ارشد آمریکایی گفت: «این ساختار به نفع مردم غزه خواهد بود.»
بررسی واقعیت:
غازی حمد، از مقام‌های حماس، در گفت‌وگو با الجزیره تأیید کرد که مذاکرات «دشوار» به توافق منجر شده است، اما توضیحات او بلافاصله پرسش‌هایی را درباره نحوه اجرای آن مطرح کرد.
▪️
حمد گفت: «ما پیش از عقب‌نشینی اسرائیل از نوار غزه هیچ اقدامی در زمینه خلع سلاح انجام نخواهیم داد.» او افزود که کمیته ملی اداره غزه بدون دخالت اسرائیل خلع سلاح را اجرا خواهد کرد.
▪️
این موضع ظاهراً با توصیف ترامپ از یک روند مرحله‌ای و «با ساختاری دقیق» تفاوت دارد؛ روندی که در آن، هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی می‌کنند.
▪️
مقام‌های آمریکایی و هیئت صلح گفتند اجرای توافق از طریق اقدامات متقابل و مستقلی که راستی‌آزمایی می‌شوند پیش خواهد رفت، هرچند اذعان کردند که جدول زمانی عقب‌نشینی اسرائیل هنوز در حال نهایی‌شدن است.
تصویر کلی:
بخش‌های وسیعی از غزه در جریان جنگ ویران شده و بیشتر جمعیت دو میلیون نفری آن همچنان در چادرها یا سرپناه‌های موقت زندگی می‌کنند.
▪️
مواد غذایی و دیگر کمک‌ها در حجم زیادی وارد غزه می‌شود، اما وضعیت انسانی همچنان وخیم است.
▪️
وزارت بهداشت غزه که تحت کنترل حماس است می‌گوید از زمان آتش‌بس ۱۰ اکتبر ۲۰۲۵، نزدیک به ۱۲۰۰ فلسطینی کشته شده‌اند. برخی از آن‌ها از نیروهای حماس بودند، اما بسیاری دیگر غیرنظامی، از جمله کودکان، بوده‌اند.
نگاهی نزدیک‌تر:
این توافق بر این اصل استوار است که غزه باید یک دولت، یک نظام حقوقی و یک مرجع امنیتی مشروع داشته باشد. انتظار می‌رود روند غیرنظامی‌سازی بین ۲۰۰ تا ۲۵۰ روز طول بکشد و هر بار در یکی از بخش‌های غزه اجرا شود.
▪️
پلیس غیرنظامی حماس ابتدا سلاح‌های خود را به یک نیروی پلیس جدید فلسطینی زیر نظر دولت تکنوکرات تحویل خواهد داد.
▪️
پس از آن، سلاح‌های سنگین حماس از رده خارج و در انبارهای امن نگهداری خواهد شد و تونل‌ها و کارخانه‌های تولید سلاح این گروه برچیده خواهد شد.
▪️
سلاح‌های سبک مطابق قوانین فلسطینی جمع‌آوری خواهد شد.
▪️
تمامی گروه‌های شبه‌نظامی دیگر در غزه، از جمله گروه‌های مخالف حماس که اسرائیل در جریان جنگ آن‌ها را مسلح کرده بود، نیز ملزم به تحویل سلاح‌های خود خواهند بود.
کمیته ملی اداره غزه
تنها زمانی کنترل هر منطقه را در دست خواهد گرفت که یک سازوکار نظارتی تأیید کند تعهدات مربوط به آن منطقه اجرا شده است.
▪️
مقام هیئت صلح گفت در پایان این روند، دولت تکنوکرات و نیروی پلیس آن انحصار سلاح در غزه را در اختیار خواهند داشت.
نحوه اجرا:
بر اساس توافق، یک نیروی بین‌المللی تثبیت‌کننده به آموزش پلیس جدید فلسطینی کمک خواهد کرد، در جمع‌آوری سلاح‌ها مشارکت خواهد داشت و میان مناطق تحت کنترل فلسطینی‌ها و نیروهای اسرائیلی مستقر خواهد شد.
▪️
یکی از مقام‌های هیئت صلح گفت این توافق بر مبنای «اعتماد صفر» طراحی شده است، زیرا حماس و اسرائیل از همان ابتدا به‌صراحت اعلام کردند که به یکدیگر اعتماد ندارند.
▪️
این روند تا زمانی که ناظران تأیید نکنند هر دو طرف به تعهدات خود عمل کرده‌اند، از یک مرحله به مرحله بعدی منتقل نخواهد شد.
▪️
این مقام گفت هدف آن است که از وضعیتی جلوگیری شود که دولت تکنوکرات در طول روز غزه را کنترل کند، اما گروه‌های مسلح شب‌ها همچنان قدرت را در دست داشته باشند.
طرف مقابل:
عقب‌نشینی اسرائیل به‌تدریج و بر اساس جدول زمانی‌ای انجام خواهد شد که هنوز در حال نهایی‌شدن است.
▪️
ترامپ گفت هم‌زمان با تکمیل خلع سلاح و برعهده‌گرفتن مسئولیت امنیت از سوی نیروی بین‌المللی و پلیس جدید فلسطینی، نیروهای اسرائیلی عقب‌نشینی خواهند کرد.
▪️
اسرائیل همچنین عملیات نظامی و ترورهای هدفمند در غزه را متوقف خواهد کرد، مگر در مواردی که تهدیدی قریب‌الوقوع وجود داشته باشد.
▪️
مقام هیئت صلح گفت: «تمامی فعالیت‌های نظامی در غزه باید متوقف شود؛ چه از سوی اسرائیل و چه از سوی حماس.»
پشت درهای بسته:
مقام ارشد آمریکایی گفت دولت ترامپ در تمام طول مذاکرات هماهنگی نزدیکی با اسرائیل داشته است.
▪️
دولت آمریکا همچنین قصد دارد با وجود تردید اسرائیل درباره خلع سلاح حماس، اطمینان حاصل کند که اسرائیل به تعهدات خود در چارچوب توافق عمل می‌کند.
▪️
این مقام گفت: «ما از اسرائیل چیزی جز اجرای تعهداتش در چارچوب طرح ۲۰ ماده‌ای نمی‌خواهیم.»
▪️
او افزود: «اگر آن‌ها این کار را انجام ندهند، رئیس‌جمهور ترامپ بسیار ناامید خواهد شد. فکر نمی‌کنم اسرائیلی‌ها در شرایط کنونی بخواهند تنش‌ها با ما را تشدید کنند.»
در پشت صحنه:
به گفته دو منبع آگاه از مذاکرات، مصر، قطر و ترکیه فشار شدیدی بر حماس وارد کردند تا این توافق را بپذیرد.
▪️
مقام‌های آمریکایی و دیگر افراد آگاه از مذاکرات گفتند حسن رشاد، رئیس دستگاه اطلاعاتی مصر، نقشی کلیدی داشت. او میزبان مذاکرات بود و رابطه نزدیکی با خلیل الحیه، رهبر سیاسی حماس، دارد.
نکته قابل‌توجه:
به گفته یک منبع آگاه از این دیدار، هیئتی از حماس در جریان سفر اخیر خود به ایران برای شرکت در مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، با مقام‌های ارشد سپاه پاسداران انقلاب اسلامی دیدار کرد.
▪️
این منبع گفت مقام‌های سپاه از حماس خواستند برای امضای توافق عجله نکند و با وقت‌کشی زمان بخرد.
▪️
یک مقام ارشد آمریکایی نیز مدعی شد ایران تلاش کرده است حماس را متقاعد کند که توافق را امضا نکند، اما گفت این گروه تصمیم گرفت به توصیه ایران گوش ندهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77662" target="_blank">📅 06:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U72iiqv9HOj_2vB_Sgnihw2aVDP3WcKz5cFGTbtLP5wXJ2S2Ae8l2nEe_gbmdjDP6bGzUt7LzpeY0JkTkrTTCeVgYS88KVD43hPqseZy_soS5EQ-y5zWgOIIqLgPnaimN4U2CDG7oYOj6r0b3KwVAscida1F4ur9kabvy8iRjIkaeviwIyexdETbCWN2iWtXfavZxGS_6Rd7A8M_AWhrhhK_G921uZZ1SwmpKArpo-CI63tJQ6Q6F675tP6FEFrs-n3nBnJCdrkKrUasfVPEB1KZlk7uBEb88AXb-t7_7cxXm3IsddqZiz9c0C_FP2tEBlImaTeimJnaHSea_HdXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
امروز، «هیئت صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و همه گروه‌های مسلح دیگر در غزه دست یافت. این گامی عظیم به‌سوی صلح و امنیت پایدار است.
این توافق، گامی حیاتی در مسیر آن است که غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای کمک به مردم فلسطین، از نزدیک با هیئت صلح همکاری خواهد کرد. هم‌زمان، اسرائیل نیز از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به‌عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این توافق، نقطه عطف بزرگی در اجرای طرح ۲۰ ماده‌ای ترامپ است. این توافق در مراحلی که با دقت طراحی شده‌اند اجرا خواهد شد. هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات» با یک نیروی پلیس جدید فلسطینی همکاری خواهد کرد تا مسئولیت تأمین امنیت غزه برای ساکنان آن و همسایگانش را بر عهده بگیرد.
یک سال پیش، جنگی خشونت‌بار و مهارنشدنی، بحرانی انسانی و گروگان‌هایی در اسارت وحشیانه وجود داشت. ما پیشرفتی تاریخی کرده‌ایم و هنوز کارهای زیادی باقی مانده است.
می‌خواهم از میانجی‌ها—مصر، قطر و ترکیه—به‌خاطر تلاش‌های مهمشان تشکر کنم، و به‌ویژه از تیم فوق‌العاده‌ام که تلاش خستگی‌ناپذیرشان این دستاورد تاریخی را ممکن کرد.
تهدیدی که در ۷ اکتبر از غزه سر برآورد، اجازه نخواهد یافت دوباره شکل بگیرد!
بر اساس این توافق، غزه سرانجام در اختیار یک دولت جدید فلسطینی قرار خواهد گرفت که به مردم خود خدمت می‌کند.
این تحول شگفت‌انگیز را که همه می‌گفتند هرگز دست‌یافتنی نیست، به همگان تبریک می‌گویم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77661" target="_blank">📅 02:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu8HKnHlZoONPQebbqpgIrCJ7rSxW2Zp1IaZ9f9Tm97qrx9AA8ayhtNKQ-BK6uGm1Rrmcxhta5H3IQzIJH3M4krD2-rL1HZv7CE1pgN8kmyoYX6P2fvTzPKcs33mFp8qo5tbwsBkAGgIXmcAVCvKuuvJ9ZDThvxSrvuRPiseFRVe9LCY8-Oatjm0lkqrw7Aphh1MkaCxvCrknRFXfAmt4_lT4I33Gh3i1YWKUPv4FxB7evlqqHgJbKHR9gUJKHi7uKg2UbwHktgMdOWLEb7M75pCWL8KEiN88_6QQrN6BhdjsJgbWkOeYIofASmqOEfI7QkhVTdsKHK7AbEXeTV1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس اعلام کرد افرادی که به سپاه پاسداران انقلاب اسلامی یا هواپیمایی ماهان خدمات مالی، پشتیبانی لجستیکی یا حمایت تجاری ارائه می‌کنند، به تداوم فعالیت یک سازمان تروریستی کمک می‌کنند.
او افزود وزارت خزانه‌داری آمریکا به شناسایی این افراد، افشای هویت آن‌ها و قطع دسترسی‌شان به نظام مالی ایالات متحده ادامه خواهد داد.
پیش از این، وزارت خزانه‌داری آمریک، شش فرد و نهاد در ایران، چین، هند و روسیه را به دلیل همکاری با هواپیمایی ماهان و سپاه پاسداران تحریم کرده بود. واشنگتن اعلام کرده بود برخی از شرکت‌های تحریم‌شده به‌عنوان نمایندگان فروش هواپیمایی ماهان فعالیت می‌کردند و در حفظ شبکه بین‌المللی این شرکت نقش داشتند. وزارت خزانه‌داری آمریکا همچنین شرکت «استودیوی استارت‌آپ داده‌نگار» را به اتهام همکاری با سپاه پاسداران تحریم کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77660" target="_blank">📅 02:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
مصر دوست و شریکی مهم برای ما در منطقه است و امنیت آن برای ما از بالاترین اهمیت برخوردار است.
همه ما باید در برابر توطئه‌های اسرائیل و عملیات‌های پرچم دروغین که برای تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.
تهدید روشن و مشترک است و از همبستگی مسلمانان هراس دارد.
araghchi
پست قالیباف:
ایالات متحده هر روز دست خود را به جنایت جدیدی آلوده می‌کند؛ حملهٔ تروریستی به منازل مسکونی غیرنظامیان در جزیرهٔ قشم، ادامهٔ جنایات در میناب و لامرد است.
امریکایی‌ها عادت کرده‌اند که سیلی‌هایی را که در میدان نبرد می‌خورند با ریختن خون بی‌گناهان جبران کنند. تاوان‌ خواهند داد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77659" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGIm_1hgt51ZPWgi7RAdOpaG5ynwPNSDkPo5988x43pINDet36M7yMqtYBBnBYH_1PaXLia15A3W48rhTjlcw6hYM3tQ_AXkqKqgu4Y2_B88WHeDpWQTO7tjetL-olGHogSvd1gnSKhG4Iz8pjq-3fJxsZ6xwYnXW8Hl1Thte2qZtoENeUBbc8Xm42Ruz4w_ZkAjYvZybOMae_s1jGmnOdsmLoZQ294PhtWFWxAXxdR4x3Lnu5hzTK3eIdlTTVDhGDHx5ZaoKpDWeqtUnsIknHGNBVlrSl7l09nbS24NF5kM4Kqr_wC1nEVvEk-snYP4tqhS1mrHDSBNhfjypvc_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی روز پنج‌شنبه از طرح تشکیل یک ائتلاف بین‌المللی برای دفاع دریایی با هدف حفاظت از کشتیرانی و مسیرهای انتقال انرژی در دریای سرخ خبر داد.
وزارت دفاع عربستان اعلام کرد نمایندگان ۴۳ کشور و اتحادیه اروپا در نشستی درباره این طرح شرکت کردند. بر اساس این پیشنهاد، عربستان به‌عنوان کشور بنیان‌گذار و رهبر ائتلاف عمل خواهد کرد و مقر آن نیز در این کشور خواهد بود.
به گفته وزارت دفاع عربستان، این ائتلاف با هدف تقویت امنیت دریایی، حفظ آزادی کشتیرانی، تأمین امنیت مسیرهای تجارت و انتقال انرژی و حفاظت از منافع مشترک دریایی در تنگه باب‌المندب و خلیج عدن تشکیل می‌شود.
این طرح پس از آن مطرح شده که حملات حوثی‌های مورد حمایت ایران به کشتی‌ها، یکی از مهم‌ترین مسیرهای تجاری جهان را با اختلال روبه‌رو کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77658" target="_blank">📅 22:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=HOTCP9zBnMV3NoWOW6oqtHoGlzzcRKyzDNfOcGMC0LSbs7x-h_UAHuIzRr--xRcTH_KxVCv1G10Bjl_61C55vLIRq_1KO9KM1QhNNJw_EHaR7QGsMPgTKS6PBB99emDW-aDk5FocJvTDySx_zDFeoJtuXGSExJNUBz_UeLfWv-cUB33inRDPoEL1qLQxNJf7AfzAqcHl1SaEfOOf8faNM1rZ9Mi75P1R3WhzVlHSmsJOvDh3aTN9_pNHZZck8r8ezHvKdnzvjNiw2xKtElP2TyoYD4k8tnuP-OigamcrSxjXRfU6VHMNFfDRIWXsyfFy9ft_S9UO0V3ZW4i-postLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=HOTCP9zBnMV3NoWOW6oqtHoGlzzcRKyzDNfOcGMC0LSbs7x-h_UAHuIzRr--xRcTH_KxVCv1G10Bjl_61C55vLIRq_1KO9KM1QhNNJw_EHaR7QGsMPgTKS6PBB99emDW-aDk5FocJvTDySx_zDFeoJtuXGSExJNUBz_UeLfWv-cUB33inRDPoEL1qLQxNJf7AfzAqcHl1SaEfOOf8faNM1rZ9Mi75P1R3WhzVlHSmsJOvDh3aTN9_pNHZZck8r8ezHvKdnzvjNiw2xKtElP2TyoYD4k8tnuP-OigamcrSxjXRfU6VHMNFfDRIWXsyfFy9ft_S9UO0V3ZW4i-postLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر جاویدنام آیدا حیدری، جوان معترض کشته‌شده به دست حکومت، در سالروز تولدش بر مزار او می‌گوید که آیدا حیدری «شیرزنی» بود که جانفدای میهن شد.
آیدا حیدری، دانشجوی رشته پزشکی دانشگاه علوم پزشکی تهران، در ۱۸ دی‌ماه ۱۴۰۴ در تهران با شلیک گلوله جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77657" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=mTKM7-HmGbzIeZmCKh9c4d38pNM8oghrpprwtlXm8T2TqZe0iwfzo5O-S-8GZeEjJAzXnN_qjbCz3XWd__fYHIUc_GRKWr2z9Rgs7mwgB_J6gVXLOH5Pznn1Mf2BRe4596Dkot3zfmbI4D5ly69Be5x62GMoDSFzzxT2cZKuF0QSH6Dr0ArRxKak575zQVNcZzaHKKf_z7JFNWvI-HF-Sw12laoiF1jRz6ZPqSP-nU6ifwpKPGFM_jyG-s9-Dc5SR1IwgIFwtvUgu9aaiilvm8f0mch3apTK5y2c907T6sx0osseHzBA7C1_-sUReAQCWpq9C7NGeeDCdE74x2tk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=mTKM7-HmGbzIeZmCKh9c4d38pNM8oghrpprwtlXm8T2TqZe0iwfzo5O-S-8GZeEjJAzXnN_qjbCz3XWd__fYHIUc_GRKWr2z9Rgs7mwgB_J6gVXLOH5Pznn1Mf2BRe4596Dkot3zfmbI4D5ly69Be5x62GMoDSFzzxT2cZKuF0QSH6Dr0ArRxKak575zQVNcZzaHKKf_z7JFNWvI-HF-Sw12laoiF1jRz6ZPqSP-nU6ifwpKPGFM_jyG-s9-Dc5SR1IwgIFwtvUgu9aaiilvm8f0mch3apTK5y2c907T6sx0osseHzBA7C1_-sUReAQCWpq9C7NGeeDCdE74x2tk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
در چند ساعت گذشته، رسانه‌های دولتی ایران همچنان ادعاهای دروغین سپاه پاسداران انقلاب اسلامی را منتشر کرده‌اند؛ به‌ویژه سه ادعای زیر:
🚫
ادعای نخست: سپاه پاسداران بار دیگر ادعا می‌کند که مسیرهای آزاد و باز عبور از تنگه هرمز برای کشتی‌های تجاری خطرناک است.
✅
واقعیت: خطرهای فوری برای کشتی‌های تجاری و خدمه غیرنظامی آن‌ها، تهدیدهای لفظی و تلاش‌های سپاه پاسداران برای حمله به آن‌هاست.
🚫
ادعای دوم: سپاه پاسداران مدعی است سه جنگنده رادارگریز اف-۳۵ آمریکا و سه هواپیمای دیگر در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✅
واقعیت: در تلاش‌های اخیر ایران برای حمله، هیچ هواپیمای آمریکایی منهدم یا آسیب‌دیده نشده است. همه موشک‌ها و پهپادها رهگیری شدند یا نتوانستند به مناطق هدف برسند.
🚫
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام M/T Nora محاصره آمریکا را شکسته است.
✅
واقعیت: این کشتی تجاری نتوانسته از محاصره «دیوار فولادین» آمریکا عبور کند. بیش از ۲۰ ناو جنگی آمریکا، صدها هواپیما و هزاران نیروی نظامی همچنان در آماده‌باش هستند و اجرای کامل محاصره را ادامه می‌دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77656" target="_blank">📅 19:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R64NmpZX1VCxdt8_b6j9mOY7tXEuCbWQKfccxz0ZdPDRvaoa-n9vo4uZWAKd5arsefAxiP9nnLxdsX_hPtvLwNmzWx_8YEb11t69IWx98lTA6rdDbV3j2gt97rf_8x6JoDwKtd5Xx07i0FXzviXPK9O3PeZ_K9Knnh-0-6VGntyLP6OJE_uQj4Y8uye72Qnclkbiz1Tb9OdY2abNbNLegCPdXZgzYdn0XWhbndMj9aAFfjbdXpgshS3KK_sEGWp7FKKNv8P2culDccQ7kzdbnOGyACbo1fZy38wPqEPBZr0nd2dkjVW980cHYuIZ1ZTMIqubyodO5X7I7zpJ76Zlbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=dPtniCMMboP_83wjHBZ60tqlGXEur0R1kJ-G7So-XEQe1WFbrmvQvOKKbyH-WktdyxBa2LzBcFBL0KI24HgTsrvbQGzPEVlGsEV_d_TjdzyvT0RbzhYjFGcALQ-1aq7uvUEaD1jxV-vPsbUNmRpX0wSFEefCRrgzxF1QHHl3GKjjuUtBCMqGXXwGtWGxQUdWkTpuigRUsvVbVzTZqRLMfabi3MTNvJz1wjHQy8wSajMfJ3jk1vIbCOkyElgeYwt4uF-ebbjxZxaRjkcvV2hmC1XZ57Gj7FuqHLscEH0E7cU-jCBFYyzXlSJ3_k-EIKTLm0EeQNfTR-0VSaRp4wofPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=dPtniCMMboP_83wjHBZ60tqlGXEur0R1kJ-G7So-XEQe1WFbrmvQvOKKbyH-WktdyxBa2LzBcFBL0KI24HgTsrvbQGzPEVlGsEV_d_TjdzyvT0RbzhYjFGcALQ-1aq7uvUEaD1jxV-vPsbUNmRpX0wSFEefCRrgzxF1QHHl3GKjjuUtBCMqGXXwGtWGxQUdWkTpuigRUsvVbVzTZqRLMfabi3MTNvJz1wjHQy8wSajMfJ3jk1vIbCOkyElgeYwt4uF-ebbjxZxaRjkcvV2hmC1XZ57Gj7FuqHLscEH0E7cU-jCBFYyzXlSJ3_k-EIKTLm0EeQNfTR-0VSaRp4wofPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی قدیمی منتشرشده در شبکه‌های اجتماعی رقص علیرضا سپاهی در اصفهان را نشان می‌دهد.
قرار بود او بامداد سه‌شنبه اعدام شود اما پیش از انتقال به محل اجرای حکم دچار سکته قلبی شد و به بیمارستان الزهرای اصفهان انتقال یافت.
@
VahidOOnLine
یک شاهد عینی گفت پس از انتقال علیرضا سپاهی، معترض محکوم به اعدام، به بیمارستان الزهرا اصفهان، فضای بخشی از این بیمارستان امنیتی شده و شماری از ماموران امنیتی در آن مستقر شده‌اند.
بامداد سه‌شنبه، ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو نفر دیگر از بازداشت‌شدگان اعتراضات ۱۸ و ۱۹ دی‌ماه ۱۴۰۵ در اصفهان، با حکم دادگاه انقلاب اسلامی اصفهان اعدام شدند. ابوالفضل سپاهی بادجانی، پسرعموی علیرضا سپاهی بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77654" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec49421.mp4?token=q9Z-TO1DUTVdbC2mdyDmLKnwrI2tXRqzpkBkzcaQ9p6nOp7qUv7k_Zeb43OobnnJrJiXmdN-ajSRWOPZtXnmxkPtWG2Q8Y3sHJCAQkr4uUOqkd4nXezWHWJPnOR5AdvVKLW61ZESrFj_UTKWVCYXgyWZrEdsEfYHkLL-TfyaYpVMJtfz57vBMEHFH8t91Q11uASR_ba1vjJ9FbcIXE_wI6DPBxoQpyfSynKnN_42ANeC1PDpPNmM69CSeazdKRRub8sXPkKhNScjh9ZB3DWYE5j6IJK4Xjyi3UWb6uwDuX-unupT4c5Ty9g4rFj7lnnF6oTATjvyP_lh_eS3hfRdxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec49421.mp4?token=q9Z-TO1DUTVdbC2mdyDmLKnwrI2tXRqzpkBkzcaQ9p6nOp7qUv7k_Zeb43OobnnJrJiXmdN-ajSRWOPZtXnmxkPtWG2Q8Y3sHJCAQkr4uUOqkd4nXezWHWJPnOR5AdvVKLW61ZESrFj_UTKWVCYXgyWZrEdsEfYHkLL-TfyaYpVMJtfz57vBMEHFH8t91Q11uASR_ba1vjJ9FbcIXE_wI6DPBxoQpyfSynKnN_42ANeC1PDpPNmM69CSeazdKRRub8sXPkKhNScjh9ZB3DWYE5j6IJK4Xjyi3UWb6uwDuX-unupT4c5Ty9g4rFj7lnnF6oTATjvyP_lh_eS3hfRdxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار خانواده جاویدنام محسن رشیدی خانی‌آبادی و علی ایازی با خانواده عرفان اسفندیاری و امیر حسین صفری ـ گزارشگر (ویدیو صدا ندارد)
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77653" target="_blank">📅 19:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbu5RT-VwdfuApiUJFJrpJzZTPSCAxS3GUW51htu5WNbS1508EHb0Vs2dAJeMCjy84vRCI4bNIn_oZs-dlqRqVcdGzxhoymJ_6cCim94fUYTOVQStSKKheFelWP6xnqVc8Eb5qpqkabiV1H5tjySKqHZqCjwNGeZX_LEkWt3bmKaJzoyCdBGmeJEh6N8tRRgW9W1sPwi4b-S-lfWzwCKkOwtKL4cbcdIqYC0iiTOOyqWuAVei5aZy8-gbLDvM49G3vfh18_hVpFaK8NoBpvt0xF3q-aU3OTGLRxkLsXQy0bj5S7vjccaDFDooZaER8qdEktKQuVQO-UeB0Ly5i_ktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ان‌بی‌سی نیوز روز پنجشنبه هشتم مرداد، به نقل از یک مقام آمریکایی گزارش داد که دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در جریان نشستی در هفته گذشته از فرسایشی شدن جنگ، محدودیت گزینه‌های نظامی علیه ایران و دست نیافتن به توافق خشمگین شده و بر سر مشاورانش فریاد کشیده است.
به گفته این مقام مسئول، بر خلاف اظهارات عمومی ترامپ مبنی بر رضایت از روند جنگ، نه او و نه مشاوران ارشدش از وضعیت موجود راضی نیستند. یکی از متحدان ترامپ در این باره گفت: «رئیس‌جمهور کلافه شده است؛ او تصور نمی‌کرد گرفتن امتیاز از ایران تا این حد دشوار باشد و هیچ راهبرد مشخصی برای چگونگی رسیدن به نقطه پایان وجود نداشت.»
این گزارش می‌افزاید نبود شفافیت درباره اهداف نهایی واشنگتن—از جمله این‌که آیا هدف اصلی جلوگیری از دستیابی ایران به سلاح هسته‌ای، بازگشایی تنگه هرمز یا نابودی برنامه‌های موشکی و پهپادی ایران است—برنامه‌ریزی برای پایان جنگ را دشوار کرده است. یک مقام آمریکایی تصریح کرد: «ما پیروزی‌های تاکتیکی متعددی داشته‌ایم، اما بدون داشتن یک راهبرد روشن، با یک شکست راهبردی روبه‌رو هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77652" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPMBg5FoGM2D1AkiN_36Nf-q7_A2z-YjVk0tGNZnVjAX5bMNdFbNBx4unCbmvC9pMe3IayLIzToEgYWZFXEUc5Y3M0srP2yItYFBLhc5O6UCBBiaMQr_0rqcitycmcHgId60F-Xj5_DeJpD8d_1pcfYlk46S72A_vTrT2x0VX59OvEtCG1I67I0phkm0GeTOxfvMlr3aQstKXcNwTFBZm0GVA_r9H9JdrO1jzbM1HMH7deHkcssUxhPC8y3irdpVPoSapJSpFOxLQFyBQpjQb9T1w-rxDAJ-8N-sXqUuy870TAEhRqxudJxSYTh-U2TrkNRPnnru4fIb0wtAK8LUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌وزارت دفاع چین گزارش‌ها درباره برنامه آن کشور برای تحویل صدها سامانه پدافند هوایی دوش‌پرتاب به ایران را رد کرده و آن را «کاملا نادرست و خلاف واقع» خوانده است.
جیانگ بین، سخنگوی وزارت دفاع چین، روز پنجشنبه در پاسخ به پرسشی درباره این گزارش گفت که ادعای مطرح‌شده صحت ندارد. وزارت خارجه چین نیز پیش‌تر گزارش مربوط به این معامله را «بی‌اساس» توصیف کرده بود.
رویترز روز چهارشنبه به نقل از سه منبع آگاه گزارش داد که ایران قرار است ظرف چند هفته نخستین محموله از مجموع ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل ساخت چین را دریافت کند. به گفته این منابع، قرارداد مورد نظر شامل موشک‌های کیودبلیو-۱۲ و اف‌ان-۱۶ است و ارزش آن بین ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود.
بر اساس این گزارش، قرارداد با یک شرکت مستقر در هنگ‌کنگ امضا شده که گفته می‌شود میان ایران و تأمین‌کننده چینی نقش واسطه را ایفا کرده است. منابع رویترز گفتند که قرار بود محموله‌های اولیه از شهر ارومچی در غرب چین ارسال و از مسیر پاکستان به ایران منتقل شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77651" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bCtJCSYNu0FR-9xzLobrlfI76p0Ynb1gaBFyDNp67h_mdMFSBD0UNZvXy5m3C4WEwUY74xkZeJym8iPdll3D48Z8d4qrlfBCFWKIncj2WHduq9xI7frrRq3ZIQyc_nUFyv8DMA8ToaLrqO0fuXngP1LsGazwYZmuuhNaCLkrrzgFsbYS7EGLPeEhTlqUx__6FT8XpM67iXW-d3NM5QjUtL3IcOWmYxKdQq4vUEx_tHIvRlJEZzldkL3F0Ln1NE8wugGfyo-Kt9P6jY0BxDPasWyrd5lm0qEB-YE9M1qADH6LmcWtMZi91kJXgEVSCpkQAiO7yB7hmOg6oHbNJGCpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kHdS7jNiwcpRoEuFQsirMLCa31oieDqMyRkUh8RC3cerqEc9FSnOlXDYZcqFH2EJKwd8ZXVx_eobGAuH4jHTOwK_vymv4RB0AXMJpw1QoW9nnHa__TMy28mnncNJSIwjJ_jLX9vuUip5yOLJz_xGDZcWMCxCdrbMCUaCYES_Ush8pQtpTjmLXi_FAo9deq6TKWMx9szt0Cw1gTfRQyTEAeMtfrow2Yd1cz9wJwHPn3zCqI8-unlMupUQ8jFrrRyyRsC6DtXevguJIB4fE_qA1tXDxkiibJv8nHOMA8GkWn_OGdnRo_SwLjAEPp1Yk92VqSW7KPDy52vaQQg6F59f9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: با شکاف عمیقی که پس از کشتار دی‌ماه بین مردم و رژیم ایجاد شد؛ حکومت ایران در نهایت سقوط می‌کند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در پاسخ به مجری ای‌بی‌سی که به او گفت طبق گزارش نیویورک‌تایمز شما به ترامپ گفته بودید که ظرفیت موشکی حکومت ایران ظرف چند هفته نابود می‌شود و تغییر رژیم ممکن است رخ دهد، گفت: این ارزیابی اولیه من نبود و این بیان نادرستی از آنچه گفتم است.
برآورد من این بود که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای اقدام کنیم.
نتانیاهو گفت، من گفته بودم که می‌توانیم شرایط را برای ضعیف‌تر شدن رژیم فراهم کنیم اما بر عهده مردم ایران خواهد بود که سرنوشت خود را تعیین کنند.
او درباره احتمال تغییر حکومت در ایران گفت: «فکر می‌کنم ایران از همیشه ضعیف‌تر و اسرائیل از همیشه قوی‌تر است، اما نمی‌توانم بگویم رژیم هم‌اکنون فروپاشیده است.»
نتانیاهو گفت: بگذارید یک پیش‌بینی کنم؛ پس از چنین شکاف بزرگی که به دنبال آن قتل‌عام (کشتار ۱۸ و ۱۹ دی‌ماه ۱۴۰۴) بین مردم و رژیم ایجاد شده، فکر می‌کنم که رژیم ایران در نهایت سقوط خواهد کرد.
نتانیاهو هشدار داد اگر ایران، اسرائیل را هدف حمله قرار دهد، «اشتباهی بسیار خطرناک» مرتکب خواهد شد و اسرائیل «بسیار شدید» پاسخ خواهد داد.
او در پایان گفت: «هدف من این است که مطمئن شوم ایران با این حکومت به سلاح هسته‌ای دست پیدا نمی‌کند. این موضوعی است که من و رئیس‌جمهور ترامپ هر دو بر سر آن توافق داریم، زیرا در آن صورت جهان متفاوتی خواهد بود.»
@
VahidOOnLine
نخست‌وزیر اسرائیل روز چهارشنبه در گفت‌وگویی اختصاصی با لینزی دیویس از شبکه ای‌بی‌سی نیوز تأکید کرد که دونالد ترامپ تصمیم‌گیرنده اصلی درباره جنگ ایران است و او تلاش نمی‌کند ترامپ را برای ادامه حملات علیه ایران متقاعد کند.
نتانیاهو در عین حال گفت نسبت به امکان دستیابی به راه‌حل دیپلماتیک با جمهوری اسلامی تردید دارد.
او گفت: «نمی‌دانم این احتمال کم است یا نه، اما نسبت به شیوه عمل ایران بدبینم. آن‌ها همیشه دروغ می‌گویند، تقلب می‌کنند و زمان می‌خرند. آیا تحت فشار کافی ــ فشار دیپلماتیک و اقتصادی ــ ممکن است این رفتار تغییر کند؟ می‌توان امتحان کرد.»
او افزود: «واقعیت این است که ما شریک و متحد هستیم. او شریک ارشد است؛ فراموش نکنیم که او رئیس‌جمهور ایالات متحده آمریکاست و من شریک کوچک‌تر هستم. اما من نخست‌وزیر اسرائیل هستم و هر زمان لازم باشد از منافع و امنیت کشورم دفاع می‌کنم.»
نتانیاهو همچنین از نقش دولت ترامپ در مقابله با «دشمن مشترک» قدردانی کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77649" target="_blank">📅 19:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om9B8gn2JVtn1VcCSO1f9n641t_THewzBwkciL_lzk-nn6Jo-8QzM_iMfHZOtX17efFhiaeE4hQn7l13sgmSgrLBzrexts4PLdvfuiLxeyWsdvkmmP0L1Jnu5N306-v3zuo4eI1dKuyAz9aB-VzzR0D7ERp5mbxpmIZ7-iidmclBmm48CuujQISbpfrmZoEJpAHWQLpPqUKyZHAoIzBXN_sPGoKjPRM9fBGACDHXeKDJ-4VtuMwK2s98l8pyA51fVc-sSTgqeFvuMrDIEN7cmplcn40fI0ZwCHUKmOEVg3y8WxgkyH8yMmy2Stoia9C2ttJcGgLW3Q5MEfPbK2Pd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار ویدیویی از ضرب‌وشتم چند زن در ایران در جریان یک پخش زنده اینستاگرامی، موجی از واکنش‌ها را در فضای مجازی به دنبال داشته است.
به‌ گزارش خبرگزاری میزان، وابسته به قوه قضائیه ایران، پس از انتشار ویدیوی این لایو اینستاگرامی با دستور مقام قضایی برای این فرد پرونده تشکیل شده است.
سعید راستی، معاون بخش «مبارزه با شرارت و جرایم خشن» پلیس اعلام کرد که این ویدیو باعث واکنش گسترده شهروندان شده و اطلاعات ارسالی مردم در شناسایی متهم نقش داشته است.
آقای راستی اضاف کرد که این فرد بامداد پنجشنبه، ۸ مرداد ۱۴۰۵، «در عملیاتی» در مرکز تهران شناسایی شد و «به دلیل مقاومت در برابر ماموران» دو گلوله به پاها و یک گلوله به دست او شلیک شده و در پی آن بازداشت شده است.
هم‌زمان، ویدیوهایی از این فرد پس از بازداشت در شبکه‌های اجتماعی منتشر شده است که او را در یک مرکز درمانی نشان می‌دهد. در یکی از این ویدیوها، او در حضور پلیس از زنانی که در ویدیوی ضرب و شتم دیده می‌شوند و همچنین از  شهروندان و پلیس عذرخواهی می‌کند.
@
VahidHeadline
دیروز بارها اون ویدیو رو برای من فرستاده بودند و می‌خواستند پخش بشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77648" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
