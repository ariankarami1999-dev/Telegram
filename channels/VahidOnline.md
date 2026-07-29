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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 00:13:06</div>
<hr>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c878874010.mp4?token=Kfz6MufPg7pDb1g51c8zLnE6hexcthzp2bKweaUYTtF41ieYgVQSzBe5OeD-9i8PbWqgmlvfrkrSn6cng1_HNCorSipOnpj09oaQsfIq0CnqjbJoeF2_Cq_SvehtzB-_C4zAKlKwPfrXzt3S-Ynlu5YWbYa_R8o0k1jntpL6DLCBUihf3R3VksVYWU0CVGpyQPIEyPHTG4ACIu0DZ-lTNHELA7dkCVz01UmLAd08K8n8-lb82sZ7JEkVQUspHU3drb0Bg07JZ_5TAB0jlZvBqB1slgRcWfwpn30d4N_8RCJzhgo4mxUmmYZaDNrZhATghGfbnsEEfb3zygtIA27Akw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c878874010.mp4?token=Kfz6MufPg7pDb1g51c8zLnE6hexcthzp2bKweaUYTtF41ieYgVQSzBe5OeD-9i8PbWqgmlvfrkrSn6cng1_HNCorSipOnpj09oaQsfIq0CnqjbJoeF2_Cq_SvehtzB-_C4zAKlKwPfrXzt3S-Ynlu5YWbYa_R8o0k1jntpL6DLCBUihf3R3VksVYWU0CVGpyQPIEyPHTG4ACIu0DZ-lTNHELA7dkCVz01UmLAd08K8n8-lb82sZ7JEkVQUspHU3drb0Bg07JZ_5TAB0jlZvBqB1slgRcWfwpn30d4N_8RCJzhgo4mxUmmYZaDNrZhATghGfbnsEEfb3zygtIA27Akw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از گفت‌وگوی ترامپ با خبرنگاران در کاخ سفید، ترجمه ماشین:
خبرنگار: در مورد حمله پهپادی به نفتکش LNG در سواحل مصر چه اطلاعاتی دارید؟ آیا نشانه‌ای وجود دارد که این حمله به ایران مربوط باشد؟
ترامپ: خب، می‌توانم گزارشی به شما بدهم. در این باره توجیه شده‌ام. این کمی از همان ماجراست، اما اوضاع رو به صاف‌شدن است؛ وضعیت دارد روشن می‌شود. در این میان، ما قرار است ضربه بسیار سختی به آنها بزنیم، چون نوبت ماست که ضربه بزنیم. آنها می‌دانند که این حمله در راه است و از ما می‌خواهند این کار را نکنیم. اما دیشب سعی کردند به آن شلیک کنند.
ما پنج موشک داشتیم که با سرعت ۸۵۰۰ مایل در ساعت در حرکت بودند و هر پنج موشک سرنگون شدند؛ اما با این حال آنها شلیک کردند. پس نوبت ماست. خواهیم دید که آیا در مقطعی به یک توافق می‌رسیم یا نه، اما ضربه بسیار سختی به آنها خواهیم زد.
—-
خبرنگار: در چه سناریویی تصور می‌کنید ایران به تأسیسات و پرسنل آمریکا در خارج حمله کند و شما عقب‌نشینی کنید؟
ترامپ: چنین چیزی را نمی‌بینم. نه، ما عقب‌نشینی نمی‌کنیم. ضربه سختی به آنها خواهیم زد. واقعاً می‌توانم این را بگویم، چون آنها در این مورد کار زیادی نمی‌توانند انجام دهند.
این گروه با گروهی که ما با آن سروکار داریم متفاوت بود. آنها قبلاً عذرخواهی کرده‌اند، اما باید یک ضربه‌ای به آنها بزنیم.
خبرنگار: وقتی آنها حمله می‌کنند، آیا همیشه پاسخ خواهید داد؟
ترامپ: بله، تقریباً.
خبرنگار: آقای رئیس‌جمهور، آیا این در پاسخ به حمله موشکی بالستیک شب گذشته به اردن است؟ وقتی می‌گویید نوبت ماست که ضربه بزنیم.
ترامپ: بله، فکر می‌کنم بیشتر به آن مربوط می‌شود. آن رویداد کوچک‌تری بود، اما آنها پنج موشک با سرعت ۸۰۰۰ مایل در ساعت به سمت ما شلیک کردند. خوشبختانه افرادی را داشتیم که بهترین تجهیزات جهان، یعنی سامانه پاتریوت، را به کار می‌گرفتند.
فکرش را بکنید؛ پنج موشک بزرگ با سرعت ۸۶۰۰ مایل در ساعت مستقیماً به سمت ما می‌آمدند و هر پنج موشک سرنگون شدند. چطور است؟ خیلی خوب است. فقط ما می‌توانستیم این کار را انجام دهیم؛ هیچ‌کس دیگری نمی‌توانست.
—-
خبرنگار: آقای رئیس‌جمهور، در مورد جنگ، آیا می‌خواهید مجلس نمایندگان پیش از ۳۱ اوت برای رسیدگی به لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: اگر لازم باشد، بله؛ هرچند راستش نباید لازم باشد. آیا منظورتان طرح لینزی گراهام است؟
خبرنگار: بله.
ترامپ: می‌خواهم ایران را هم به تعرفه‌ها اضافه کنند، نه فقط به تحریم‌ها. فکر می‌کنم این مهم است و همان چیزی است که لینزی می‌خواست. شنیده‌ام روی روسیه تعرفه گذاشته‌اند، اما روی آن پنج کشوری که به ایران مربوط می‌شوند تعرفه‌ای نگذاشته‌اند.
دوست دارم تعرفه‌هایی علیه ایران ببینم. این موضوع را بسیار قوی‌تر می‌کند. شاید بتوانید به آنها بگویید که به نظر من باید برای روسیه تعرفه بگذارند، اما برای ایران هم باید تعرفه در نظر بگیرند. این دقیقاً همان چیزی بود که لینزی می‌خواست.
——
خبرنگار:  رئیس‌جمهور شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اکنون گزارش جدیدی منتشر شده که می‌گوید ایران قرار است ۴۰۰ پرتابگر موشک از چین و از طریق پاکستان دریافت کند.
ترامپ: خب، این تعجب‌آور خواهد بود. چنین چیزهایی پیش می‌آید، اما واقعاً تعجب‌آور خواهد بود. او خیلی قاطع به من گفت که در این کار مشارکت نخواهد کرد و می‌داند که من کاملاً ناامید خواهم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/VahidOnline/77624" target="_blank">📅 23:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اکسیوس:
پشت پرده دیدار تعیین‌کننده «بی‌بی» با ترامپ در کاخ سفید
ترجمه ماشین:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدار خود با رئیس‌جمهور ترامپ درباره احتمال دستیابی به توافقی با ایران ابراز تردید کرد و درباره افزایش فشار اقتصادی بر ایران «از طریق ابزارهای نظامی و غیرنظامی» به گفت‌وگو پرداخت؛ یک مقام ارشد اسرائیلی این موضوع را در نشستی با خبرنگاران بیان کرد.
اهمیت موضوع:
دیدار روز سه‌شنبه نخستین ملاقات نتانیاهو و ترامپ از زمان آغاز جنگ در ۲۸ فوریه بود. این دیدار در حالی انجام شد که ترامپ همچنان برای دستیابی به توافقی با ایران تلاش می‌کند، اما هم‌زمان بازگشت به عملیات رزمی گسترده را نیز در نظر دارد.
▪️
چند ساعت پس از این نشست، ایران برای نخستین بار از زمانی که ترامپ روز جمعه حملات آمریکا در ایران را متوقف کرد، یک حمله موشکی علیه پایگاهی آمریکایی در اردن انجام داد.
▪️
ترامپ روز چهارشنبه در مصاحبه‌ای با فاکس‌نیوز وعده داد که پاسخی جدی خواهد داد. حمله غافلگیرانه ایران ممکن است رئیس‌جمهور را به سوی تشدید تمام‌عیار درگیری سوق دهد.
▪️
مقام اسرائیلی گفت نتانیاهو در انتظار تصمیم ترامپ است، اما به‌روشنی به او گفته است که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری و قدرتمند خواهد بود.
آنچه در اتاق گذشت:
ایران موضوع اصلی گفت‌وگوی ۹۰ دقیقه‌ای بود.
▪️
مقام اسرائیلی گفت آن‌ها سه گزینه‌ای را که ترامپ برای گام‌های بعدی در نظر دارد بررسی کردند:
۱. دستیابی به توافق با ایران.
استیو ویتکاف و جرد کوشنر، فرستادگان ترامپ، همچنان با ایرانی‌ها مذاکره می‌کنند، هرچند در حال حاضر اختلاف‌ها همچنان گسترده به نظر می‌رسد. مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است که نسبت به امکان دستیابی به توافق با ایرانی‌ها تردید دارد.
۲. ادامه محاصره دریایی ایران
هم‌زمان با افزایش فشار اقتصادی.
۳. ازسرگیری و تشدید حملات نظامی.
▪️
این مقام گفت: «همه این گزینه‌ها را به‌طور مفصل و بسیار صریح بررسی کردیم؛ نه با هدف ترجیح دادن یک گزینه بر گزینه‌ای دیگر، بلکه برای بررسی اینکه هرکدام چه نتیجه مطلوبی می‌تواند داشته باشد. موضوع گفت‌وگو همین بود.»
نمای نزدیک:
مقام اسرائیلی گفت ترامپ درباره تأثیر جنگ بر بازارهای انرژی و اقتصاد جهانی ابراز نگرانی کرد.
▪️
نتانیاهو به ترامپ گفت حکومت ایران عمدتاً می‌کوشد از تنها اهرمی که برایش باقی مانده است — تنگه هرمز — برای وادار کردن آمریکا به دادن امتیاز استفاده کند.
▪️
مقام اسرائیلی گفت نتانیاهو نگرانی‌های ترامپ را نادیده نگرفت، اما به او گفت راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد؛ اقتصادی که هم‌اکنون نیز تحت فشار شدیدی قرار دارد.
▪️
مقام اسرائیلی گفت: «درباره افزایش فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی گفت‌وگو کردیم. درباره امکان ادامه محاصره با هدف تحت فشار قرار دادن ایران صحبت کردیم.»
▪️
مقام اسرائیلی گفت در درون رهبری ایران میان کسانی که به‌شدت نگران فروپاشی اقتصادی هستند و عناصر تندروتری که معتقدند تا زمانی که کنترل تسلیحات را در اختیار دارند و می‌توانند از پایگاه حامیان حکومت پشتیبانی کنند مشکلی ندارند، اختلاف‌نظر وجود دارد.
▪️
مقام اسرائیلی افزود: «آن‌ها با مشکلات تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها و کمبود گازوئیل روبه‌رو هستند. اعتراض‌های کوچکی شکل گرفته است، زیرا مردم به‌شدت ناراضی‌اند. حکومت بسیار نگران این وضعیت است و می‌ترسد مردم به‌دلیل شرایط اقتصادی قیام کنند.»
پشت صحنه:
مقام اسرائیلی گفت مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، «درباره همه‌چیز» موضعی بسیار منفی دارد، اما مشخص نیست دستورهایی که به او نسبت داده می‌شود واقعاً از جانب خود او صادر می‌شود یا نه.
▪️
مقام اسرائیلی مدعی شد: «او زنده است، اما هیچ‌کس نمی‌تواند شهادت دهد که واقعاً او را دیده است. به اطرافیانش گفته بدون تأیید او هیچ کاری انجام ندهند و حتی گفته می‌شود یک بار وقتی بدون اجازه‌اش کاری کردند، عصبانی شد.»
نمای دور:
مقام اسرائیلی گفت نتانیاهو نقشه‌ای از سوریه را به ترامپ نشان داد که براساس آن، مناطقی که ترکیه در سوریه کنترل می‌کند «۵۰ برابر بزرگ‌تر» از مناطق تحت اشغال اسرائیل است.
▪️
مقام اسرائیلی مدعی شد ترکیه ۵ درصد از خاک سوریه را کنترل می‌کند، در حالی که اسرائیل ۰٫۱ درصد آن را در اختیار دارد.
▪️
یک مقام آمریکایی گفت برخلاف اشغالگری اسرائیل در جنوب سوریه، حضور نظامی ترکیه در شمال سوریه در حال حاضر با رضایت و به دعوت دولت سوریه انجام می‌شود.
▪️
مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است اسرائیل تا زمانی که تهدیدی از جانب «گروه‌های جهادی» وجود داشته باشد، حضور خود را در «منطقه حائل» جنوب سوریه حفظ خواهد کرد.
▪️
مقام اسرائیلی گفت: «نتانیاهو می‌خواست این موضوع را به ترامپ نشان دهد، زیرا او گاهی براساس اطلاعات نادرستی که بعضی افراد در اختیارش می‌گذارند، به دیدگاه‌های مشخصی می‌رسد. اگر در همان مراحل اولیه راهی برای تغییر نظرش پیدا نکنید، آن نظر تثبیت می‌شود. بنابراین می‌خواستیم واقعیت‌ها را، در صورت امکان به‌شکل تصویری، به او نشان دهیم.»
▪️
مقام اسرائیلی گفت نتانیاهو همچنین درباره توافق هسته‌ای آمریکا و عربستان سعودی با ترامپ گفت‌وگو کرد. ترامپ به نتانیاهو گفت این توافق را در چارچوب عادی‌سازی روابط عربستان سعودی با اسرائیل می‌بیند.
▪️
مقام اسرائیلی گفت: «اگر شاهد پیشرفت واقعی باشیم، درباره موضوع هسته‌ای حرف‌هایی برای گفتن خواهیم داشت.»
تصویر کلی:
مقام اسرائیلی گفت نتانیاهو به ترامپ، معاون رئیس‌جمهور ونس و ویتکاف گفته است که درباره کاهش کمک‌های نظامی آمریکا به اسرائیل تا رسیدن به صفر ظرف ۱۰ سال جدی است. او تأکید کرد که خواهان پیشبرد مذاکرات برای تدوین یک تفاهم‌نامه در این زمینه است.
▪️
مقام اسرائیلی گفت ترامپ و اعضای تیمش اعلام کردند بازخوردهایی از جمهوری‌خواهانی دریافت کرده‌اند که نگران‌اند به‌دلیل حمایت از حذف تدریجی کمک‌ها، به ضدیت با اسرائیل متهم شوند.
▪️
نتانیاهو به آن‌ها گفت شخصاً و به‌صورت علنی رهبری این تلاش را بر عهده خواهد گرفت، زیرا می‌خواهد اسرائیل به استقلال دفاعی دست یابد.
▪️
مقام اسرائیلی گفت: «درباره یک فرایند ۱۰ ساله صحبت می‌کنیم. از پیشنهادها استقبال می‌کنیم و شاید این اتفاق بتواند سریع‌تر رخ دهد.»
▪️
این مقام حتی گفت نتانیاهو به بخش دفاعی اسرائیل دستور داده است روی ساخت یک جنگنده مدرن ظرف یک دهه کار کند تا نیروی هوایی این کشور حتی در صورت توقف تحویل جنگنده‌های اف‌ـ۳۵ و دیگر هواپیماهای پیشرفته از سوی آمریکا، همچنان قدرتمند باقی بماند.
▪️
این مقام گفت نتانیاهو نمی‌خواهد اسرائیل به «حسن نیت کنگره آمریکا» وابسته باشد، زیرا معتقد است جهت‌گیری سیاسی هر دو حزب درباره کمک‌های نظامی در حال منفی‌تر شدن است.
▪️
نتانیاهو معتقد است وضعیت اقتصادی اسرائیل به این کشور اجازه می‌دهد کمک‌های نظامی آمریکا را به‌تدریج کنار بگذارد. مقام اسرائیلی گفت نتانیاهو پیشنهاد کرده است تفاهم‌نامه جدید شامل ۱۶ میلیارد دلار کمک نظامی مستقیم آمریکا و همچنین ۵ تا ۱۰ میلیارد دلار حمایت از توسعه سامانه‌های دفاع موشکی اسرائیل باشد.
▪️
افزون بر این، نتانیاهو پیشنهاد ایجاد یک صندوق مشترک ۱۶ میلیارد دلاری برای تحقیق و توسعه سامانه‌های تسلیحاتی جدید را مطرح کرده است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/VahidOnline/77623" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=R-LbNPhb84omR73LFyBxzc7-6otp6iaKQ-Wz775JOzXiNdwiaGGq6xrKP9eVUqYVo7-PuPsm6Kz2OB1PuE36cUt2MiopxFqZoBKu8KBSmljjf_fuMcpIq81b9BwcKhQcuzGjHKlin4TczP62Q77bLrZDDUs2Dsrdq_ubBj7Jkf3TuJcT6W_6iM78S8D9ejKHlo9r459gYnizOgOpTJ7h-TWxWja70FsrNu20UM9K0JhjjklY4AuT1Sf0Xe4MhFyOpe1X_SCmNdtb5soMTQEKi_5XLtIQppFnHfOdw0ZZDbO0EU83UufrlYBVqzeoj2cmEVts0Mfgkm5gFCnTXCd9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=R-LbNPhb84omR73LFyBxzc7-6otp6iaKQ-Wz775JOzXiNdwiaGGq6xrKP9eVUqYVo7-PuPsm6Kz2OB1PuE36cUt2MiopxFqZoBKu8KBSmljjf_fuMcpIq81b9BwcKhQcuzGjHKlin4TczP62Q77bLrZDDUs2Dsrdq_ubBj7Jkf3TuJcT6W_6iM78S8D9ejKHlo9r459gYnizOgOpTJ7h-TWxWja70FsrNu20UM9K0JhjjklY4AuT1Sf0Xe4MhFyOpe1X_SCmNdtb5soMTQEKi_5XLtIQppFnHfOdw0ZZDbO0EU83UufrlYBVqzeoj2cmEVts0Mfgkm5gFCnTXCd9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی، جزئیاتی از گفتگو و تبادل نظر خود با پیت هگست، وزیر جنگ ایالات متحده که روز چهارشنبه هفتم مردادماه در واشنگتن انجام شد را به اشتراک گذاشت.
نتانیاهو گفت: «هگست در این گفتگو به من گفت وقتی به وضعیت جهان نگاه می‌کنیم، کشورهایی هستند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی لازم را ندارند. در مقابل، کشورهایی هم هستند که از توانایی برخوردارند، اما اراده جنگیدن ندارند.»
نخست‌وزیر اسرائیل در ادامه افزود که وزیر جنگ آمریکا تاکید کرده است: «تنها در اسرائیل است که ما هم‌زمان شاهد وجود اراده و توانایی مبارزه هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/77622" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlYgjS5JyrnLysnvBCGmYg8momGLVG3X_I-3dqBZyWSnyVBDD2r5x7FO-Hmk9ICNwmq8-EX_St-lY-hGEtfLsGsdbEJXTDWggu-z505XXfmZOjSU_Cue-lnYJSNhiAqKPtcgo8dzEWOtd2LL6UJCHgVgr6mb8hXyySU1ggvVzsuBIQewope8MYlRAibnB-1ipfSaZxCVJLP3inS_5zVpyRiEEUgiW39C8zJ5LSaV29A8qBqdk0TqLM8cNnrELVcOxTNz7aF5xvKa6dW02C-N2PXxTPHKdR1Vvfd1_8PU-RB8Iy2ssWp6R86Z110FdnsmkutWIb3GZbpDCYA37Ka-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از وقوع انفجار در پایانه گاز طبیعی مایع بندر دمیاط مصر هنگام تخلیه محموله خبر دادند.
همزمان، شرکت امنیت دریایی امبری و منابع امنیتی اعلام کردند یک پهپاد به یک شناور ذخیره‌سازی گاز متعلق به آمریکا برخورد کرده است؛ حادثه‌ای که به آتش‌سوزی دو کشتی منجر شد، اما تاکنون گزارشی از تلفات جانی منتشر نشده است.
بر اساس گزارش‌ها، این انفجار هنگام تخلیه محموله در پایانه گاز طبیعی مایع بندر دمیاط رخ داد.
شرکت امنیت دریایی امبری اعلام کرد یک پهپاد به یک شناور ذخیره‌سازی شناور گاز که تحت مالکیت آمریکا است، برخورد کرده است. به گفته این شرکت، در پی این برخورد آتش‌سوزی ایجاد شد و سپس به کشتی دیگری نیز سرایت کرد.
شرکت خدمات بندری اینچ‌کیپ نیز در گزارشی جداگانه اعلام کرد دو کشتی حامل گاز در بندر دمیاط دچار آتش‌سوزی شده‌اند.
امبری اعلام کرد خدمه هر دو شناور تخلیه شده‌اند و آتش تحت کنترل درآمده است. این شرکت افزود تاکنون هیچ گروهی مسوولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77621" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HnIrfuYOa8H0UdP8M6yoRo0egk9eTNNxXya5Lg4TSMHRWhVh0jmC4SD9CtL082S4TElVttYMLwKioqlqldys8KtBkzSQ11qEeld0fjoy-7ZYBFIIcmbxoHpPUnj00cr-xmrBxXhenqOWxpuJyfVSRqSwCciM5ulsPBdVBB8L32-UsQJ9qyFdKvVeGJbNHNhlGcZhJigg0WdKyNypcXvzvskgiMjjs29pJ7qXkDJDaVsvJrtUUihevUzQ9R4vc0nd1plioE9nIfLGrROowvL2xeREBO0mNmNb_JMcYGzQn_e9vZcL4LAOg1-fZJOmkJYU6IqgrhcbRzHkf3_Bv0tiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: پس از تهدیدهای اخیر و تلاش برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناه در حال عبور از تنگه هرمز، سپاه پاسداران انقلاب اسلامی ایران همچنان ادعا می‌کند که دریانوردان بین‌المللی باید فقط از مسیرهای مورد ترجیح سپاه استفاده کنند.
✅
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه هیچ اختیاری برای تعیین مسیر حرکت آزاد و بدون مانع ندارد. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای سنتکام به عبور حدود ۱٬۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77620" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKpA1X59klDJZIX7n-3jleR1Lr_Fn8xm98lyGNCqvPF5LzE-2zU3MXbqqPZ0Eg9gWM65Z3mFjZrhUniHDzJUdmg0MOClYnbm6T6QXRk8WP6wb6WSGDGLw8hlk4EIYeqN2P6RVXnY6jiRUb-z1vZ1EfjEHL7fVNtgRDInX5Hp4ttaq4HjRpS7eg3t0xR6s-3dc1NGOeoa4xso2eWAFX9UpvQNLhhQeIHRFNmhjvySc-BudlomZZZFdruMFYO5HiGelKmkE31ej6q7SGSue1-eEUCOUYvI1NZBT2Mjay362-KSPQ6JbXEOGYWKPg2y-Arv5AAHQkjPTJYrHsQDVYmQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، نیروی دریایی سپاه پاسداران انقلاب اسلامی روز چهارشنبه هفتم مردادماه، اعلام کرد سه نفتکش را در تنگه هرمز به دلیل بی‌توجهی به هشدارها «هدف قرار داده و توقیف کرده است».
در این گزارش به نام این شناورها، مالکیت، محل دقیق حادثه و جزئیات تخلفات ادعایی آن‌ها در این آبراه اشاره‌ای نشده است، اما تهران مسیر جایگزین جنوبی در امتداد سواحل عمان را رد کرده است.
بر اساس بیانیه‌ای که تسنیم منتشر کرده، سپاه پاسداران تاکید کرده است که «مداخله‌ها و دستورات غیرقانونی» ایالات متحده از سوی شناورهای حاضر در منطقه «بی‌پاسخ نخواهد ماند».
مرکز عملیات تجارت دریایی بریتانیا، هنوز وقوع چنین حملاتی را تایید و گزارش نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77619" target="_blank">📅 18:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_wxTu8C3YZ6lO_uzeAa3ZABiz2kl-Sav1dE_SE-WyBLOCtz0D7zB-lntS5ryGGWaKUl3p_gtFZcWZLQwposzeQ-GgNYJRxghaD5WECp0C7UpkCzKUcpwmT3ZOXu47vXkx6XvkdAgUqyVDOIYNwLclFDtRdj1rglFXfHr-KtkHse0A8ehEc2D5UZQtzYW5JFCCjddIwcu_rY6gGD9-YLw98jhVW5fiwSavsje4R0u-7kNd_CVSVfEJUfg60qsb3TuRwEDbZqrXif60HPPNNYHTi2kdYGYFJXUwj1vmjurgBZAO2tXscy6dxAsv1y3075tR--51OUeeaQYAetHyw1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ دانشگاه ایرانی در رتبه‌بندی تاثیرگذاری تایمز ۲۰۲۶ حضور ندارد
در رتبه‌بندی تاثیرگذاری و پایداری دانشگاه‌های جهان در سال ۲۰۲۶، نام هیچ دانشگاهی از ایران دیده نمی‌شود؛ این در حالی است که در فهرست سال ۲۰۲۵، ۳۴ دانشگاه ایرانی حضور داشتند.
تایمز امسال نحوه مشارکت در این رتبه‌بندی را تغییر داده و آن را به عضویت دانشگاه‌ها در شبکه پایداری و ارائه اطلاعات از سوی خود موسسات مشروط کرده است.
برخی رسانه‌های ایران این تحول را با عنوان «حذف ایران» پوشش داده‌اند؛ تعبیری که اقدامی هدفمند یا تنبیهی را تداعی می‌کند، در حالی که هنوز مشخص نیست نبودن دانشگاه‌های ایرانی ناشی از تصمیم تایمز بوده یا شرکت نکردن آنها در سازوکار تازه رتبه‌بندی.
رتبه‌بندی‌های موسسه تایمز از شناخته‌شده‌ترین و پرمراجعه‌ترین نظام‌های ارزیابی دانشگاه‌ها در جهان است و نتایج آن می‌تواند بر اعتبار بین‌المللی، جذب دانشجو و همکاری‌های علمی دانشگاه‌ها اثر بگذارد.
@
VahidHeadline
برای نخستین‌بار از زمان آغاز انتشار رتبه‌بندی «دانشگاه‌های تأثیر‌گذار» موسسه آموزش عالی تایمز، نام هیچ دانشگاهی از ایران در نسخه سال ۲۰۲۶ این فهرست دیده نمی‌شود. رخدادی که در کنار افت مداوم جایگاه دانشگاه‌های ایران در دیگر نظام‌های معتبر رتبه‌بندی جهانی، بار دیگر وضعیت آموزش عالی کشور را زیر ذره‌بین برده است.
بر اساس نتایج منتشر شده، در رتبه‌بندی سال ۲۰۲۶ تایمز، یک‌هزار و ۶۴۶ دانشگاه از ۱۱۶ کشور بر پایه اهداف توسعه پایدار سازمان ملل متحد (SDGs) ارزیابی شده‌اند. با این حال، برخلاف سال‌های گذشته، نام ایران به‌طور کامل از این فهرست حذف شده و مؤسسه تایمز نیز تاکنون توضیحی درباره علت این موضوع ارائه نکرده است.
حذف نام ایران از این رتبه‌بندی در حالی رخ داده که دانشگاه‌های کشور از زمان آغاز انتشار آن در سال ۲۰۱۹ همواره در فهرست تایمز حضور داشتند. تنها در سال ۲۰۲۵، ۳۴ دانشگاه ایرانی در این رتبه‌بندی ارزیابی شدند و برخی از آن‌ها در چند شاخص توسعه پایدار، از جمله «سلامت و رفاه»، «آموزش باکیفیت»، «صنعت، نوآوری و زیرساخت» و «برابری جنسیتی»، جزو دانشگاه‌های برتر جهان بودند.
همزمان، نتایج تازه‌ترین رتبه‌بندی جهانی QS نیز از ادامه روند نزولی دانشگاه‌های ایران حکایت دارد. رتبه‌بندی QS که از معتبرترین نظام‌های ارزیابی آموزش عالی در جهان به شمار می‌رود، دانشگاه‌ها را بر اساس شاخص‌هایی مانند اعتبار علمی، کیفیت پژوهش، میزان استناد به مقالات، نسبت استاد به دانشجو، همکاری‌های بین‌المللی و اشتغال‌پذیری فارغ‌التحصیلان ارزیابی می‌کند.
در این ارزیابی دانشگاه تهران ۴۵ پله سقوط کرده و از رتبه ۳۲۲ به ۳۶۷ جهان رسیده است. دانشگاه تبریز ۱۰۸ رتبه، دانشگاه فردوسی مشهد حدود ۱۲۵ رتبه و دانشگاه‌های شیراز، اصفهان و آزاد اسلامی نیز افت قابل‌توجهی را تجربه کرده‌اند؛ به‌طوری که دانشگاه آزاد از جمع هزار و ۴۰۰ دانشگاه برتر جهان خارج شده است.
در مقابل، کشورهای منطقه روندی معکوس را طی کرده‌اند. ترکیه با ۲۵ دانشگاه در رتبه‌بندی QS حضور دارد و دانشگاه فنی استانبول به رتبه ۲۷۹ جهان رسیده است. امارات متحده عربی نیز سه دانشگاه در میان ۳۰۰ دانشگاه برتر جهان دارد.
حسین سیمایی‌صراف، وزیر علوم، کاهش سرمایه‌گذاری در پژوهش، ضعف همکاری‌های علمی بین‌المللی، کمبود زیرساخت‌های آموزشی و پژوهشی و محدود شدن فرصت‌های مطالعاتی را از عوامل افت جایگاه دانشگاه‌های ایران دانسته است.
شاهین آخوندزاده، معاون تحقیقات وزارت بهداشت، نیز اعلام کرده بود که محدودیت‌ها و اختلال‌های گسترده اینترنت در سال ۲۰۲۶، پژوهشگران ایرانی را حدود یک‌سوم سال از فعالیت علمی بازداشت؛ موضوعی که به گفته او می‌تواند به کاهش حدود ۱۰ هزار مقاله علمی و افت بیشتر جایگاه علمی ایران منجر شود.
کارشناسان آموزش عالی نیز می‌گویند کاهش ارتباط دانشگاه‌های ایران با مراکز علمی جهان، محدودیت در جذب استاد و دانشجوی خارجی، کاهش بودجه پژوهشی، ضعف زیرساخت‌های آموزشی و دسترسی محدود به منابع علمی بین‌المللی، از مهم‌ترین عوامل کاهش رقابت‌پذیری دانشگاه‌های ایران در رتبه‌بندی‌های جهانی است.
رتبه‌بندی دانشگاه‌های تأثیرگذار تایمز از سال ۲۰۱۹ با هدف ارزیابی عملکرد دانشگاه‌ها در تحقق ۱۷ هدف توسعه پایدار سازمان ملل منتشر می‌شود و تنها نظام رتبه‌بندی جهانی است که نقش دانشگاه‌ها را در حوزه‌هایی مانند آموزش، سلامت، برابری جنسیتی، نوآوری، محیط زیست، عدالت و توسعه پایدار می‌سنجد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77618" target="_blank">📅 17:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJo5W0z7UQhy8OemtIq_JzzUwz3EuzosvGIGWnP4IkWj6MwZc2jYWDLSNpNm72p2YgO-9QBlS_QD6c3cOP6LX8smW4miSdUBXbkd8r8xOANMEveVBzKWa5N5OUJTWvMl3AamQt0RfKgkbBLt7JbbIQIRjBnA6EkxBOLXdv8XmQNk8YGnbBlMniTkV9kohGR13cCepKQ5xlQINisldNXllbKiiNlgkIR5z4I2M5CBvOK4oj2eyIqHYgD0_M0wV8IVvQNDRo2imcJ0aeN6x7BjbskgzwQYIvMplOIFRicxClupYLHS1BlT6hTFVsKGaj89r1YVcsmA8GRPZjof8xYnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه پس از آنکه ارتش ایالات متحده اعلام کرد چندین موشک بالستیک شلیک‌شده از سوی ایران به سمت نیروهای آمریکایی در خاورمیانه را رهگیری کرده است، وعده داد که ایران را به‌شدت هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز گفت: «حسابی نابودشان خواهیم کرد. خیلی سخت به آنها ضربه خواهیم زد.»
این گفت‌وگوی تلفنی به‌صورت کامل پخش نشد، اما یکی از خبرنگاران فاکس نیوز خلاصه‌ای از اظهارات ترامپ را منتشر کرد.
@
VahidHeadline
گفت: حسابی نابودشان خواهیم کرد. ضربات سختی به آنها خواهیم زد و به‌شدت تنبیه خواهند شد.
ترامپ همچنین درباره حملات هوایی آمریکا و عربستان سعودی به شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق گفت این حملات با هماهنگی دولت عراق انجام شده است.
رییس‌جمهوری آمریکا این شبه‌نظامیان را «سرطانی برای جهان» توصیف کرد و گفت در حال بررسی صدور هشدارهای بیشتر علیه نیروهای نیابتی جمهوری اسلامی و ارتباط آنها با حکومت ایران است.
ترامپ همچنین گفت اکنون موضع بنیامین نتانیاهو درباره جمهوری اسلامی را درک می‌کند.
او در پاسخ به پرسشی درباره احتمال ادامه مذاکرات با جمهوری اسلامی نیز گفت: «اجازه می‌دهیم به گفت‌وگوهایشان ادامه دهند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77617" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=GwWm-etWWb43TO9qNeGyeE4rHW7re_iK6iD8v-0BpFbRiW0_ADzfRSUlCKbf_urpL-nUgLH3m1iRPks4BaOTbHF2tbV5no9_BlLNiatiYVvHBzhwnsn08ZFhC4pIeO7dLg96y2c_bydKcEMmawB5WmoKSOywniAsw4BHpa4gIcEFymVy61TzWqhPDfQ0bzRygdqtSqmsVq81uXbUnNDi1dOhX5DHmhfhqs4ejMmpa3igesDhyp5vFzTB2Nm6_uht8bkQxrlg41RU5mNcE2xpR7bLnEUdQp-HsmIzH3UMN3YPyNbaih852VULRtTHDq7cAf3QyDJ_KM73bLTfGvm-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=GwWm-etWWb43TO9qNeGyeE4rHW7re_iK6iD8v-0BpFbRiW0_ADzfRSUlCKbf_urpL-nUgLH3m1iRPks4BaOTbHF2tbV5no9_BlLNiatiYVvHBzhwnsn08ZFhC4pIeO7dLg96y2c_bydKcEMmawB5WmoKSOywniAsw4BHpa4gIcEFymVy61TzWqhPDfQ0bzRygdqtSqmsVq81uXbUnNDi1dOhX5DHmhfhqs4ejMmpa3igesDhyp5vFzTB2Nm6_uht8bkQxrlg41RU5mNcE2xpR7bLnEUdQp-HsmIzH3UMN3YPyNbaih852VULRtTHDq7cAf3QyDJ_KM73bLTfGvm-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته نیروهای آمریکایی و عربستان سعودی در عملیاتی مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در شرق عراق را هدف قرار داده‌اند.
@
VahidHeadline
بر اساس گزارش‌ها، پایگاه‌های حشد شعبی در استان‌های دیاله، کرکوک، کربلا و نینوا هدف حمله قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77615" target="_blank">📅 16:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2O0hCOFzrx74V7u7p-2TCcV_dzFjBJk1ndIqro4BVoQffW-D9SRNYWm6D51mNFodkoCZV3h-EUr4LH96UeXYvnw5_vN2ZN2V-M3Ru3hDXn9-v7C7lZS5QCtAvmGrxLDBsu9ifIuv0XTCuB-sK3Y0xsbzUKRpQcVxCBcBp_iAhQwjR3R58acdV6a_m-64LNHkiiL4qskPGs6BUhcyo7ZlO7w98iunv7YlIp0_hb6QZH7rhAccCh4S1pQbISMFSdFWoJ17pY8OZqpxOHyjggUEX1KXK4t-kGMSCrc1rIvXH76cIqL8Ov6NvpMLV8WlL9Y2RbIJ_U84wwC4KCg6g6bjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرحی را به مرحله بعد فرستاد که در کنار تشدید فشار اقتصادی بر روسیه، تحریم‌های مرتبط با ایران را تا سال ۲۰۳۱ تمدید می‌کند.
این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، هنوز باید در رأی‌گیری نهایی سنا تصویب و سپس در مجلس نمایندگان بررسی شود.
@
VahidHeadline
و  در خبری دیگر:
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) اعلام کرد ۱۰ شرکت و هشت نفتکش را به فهرست تحریم‌های خود افزود.
این تحریم‌ها بر اساس فرمان اجرایی ۱۳۹۰۲ و در ارتباط با جمهوری اسلامی اعمال شده‌اند.
در میان نهادهای تحریم‌شده، «اداره خدمات دریایی هرمزسیف» و «شرکت بیمه دریایی خلیج فارس» در ایران نیز قرار دارند.
وزارت خزانه‌داری آمریکا همچنین اعلام کرد این دو نهاد مشمول تحریم‌های ثانویه هستند.
شرکت‌های تحریم‌شده در هنگ‌کنگ، جزایر مارشال و چین ثبت شده‌اند و نفتکش‌های تحریم‌شده نیز با پرچم کشورهای مختلف فعالیت می‌کنند. این نفتکش‌ها به شرکت‌های تازه تحریم‌شده مرتبط معرفی شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/77614" target="_blank">📅 16:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7rWeiQS6t1i5ckSIHVHU7wuUDT_asZW_6-W4QOwACchpxI2dWo0kCsl286cZhrJo4SdzQSTC0a1aTBTfZqZ7O9yGbk8UUtua-c4W0CbzmE6BYZuY-AL8-qZNI0KCTTc4bYnSEyu5PQAsFAjR5ZFXWK20gJVSQ7LJhEPuwHfxgG8JQCX8IEK26QmjLmyVqbMEXNr4ViGEGVHmrF1naHjs62jY2ed67OOXwzr_gvFIb2qJCxE57Jgkt000jXDT0wgrDwud_hCKRgBRxW4FaGQzL4MYaPCEoP17YgnIY-ogz5YBP1OZQM2pmI5JDyDtF9Q6kJjuSp3tdWeNUXbrEv7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع منطقه‌ای گزارش داد که حوثی‌های یمن در حال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب هستند؛ اقدامی که به گفته این منابع، پس از اعلام محاصره دریایی عربستان سعودی مطرح شده و می‌تواند فشار بر آمریکا را افزایش دهد.
به گفته این منابع، حوثی‌ها در حال بررسی دریافت عوارض از بیشتر کشتی‌هایی هستند که از باب‌المندب، گذرگاه راهبردی میان دریای سرخ و خلیج عدن، عبور می‌کنند، اما هنوز زمان مشخصی برای اجرای این طرح تعیین نشده است. دفتر رسانه‌ای حوثی‌ها به درخواست رویترز برای اظهار نظر پاسخ نداد.
دو مقام منطقه‌ای که از سوی جمهوری اسلامی در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند مقام‌های حوثی در سفر خرداد به ایران برای شرکت در مراسم تشییع جنازه علی خامنه‌ای، درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب با مقام‌های جمهوری اسلامی گفت‌وگو کرده‌اند. به گفته منابع، هدف از این طرح عادی‌سازی دریافت عوارض از آبراه‌های بین‌المللی و افزایش فشار بر آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/77613" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGGh7K0CaiQh8Hn6zqJnz3v3fTTmWjM1xs7M1ZbfRcR08cv-fXV6z8pfZ4Fvh_VxNOwT0-6Xi3F7tJfs58Pcut0THWqNmXI02AEy7189XOTizYFflIuS_7QTk8jw6cjUWew00WqGYjunHkUFwDTJErQnDNq9Wdko77X9lL8OuArAhyYMEbb5-2KxY1no95AtcyvBj1n4mYHg38MFCQoeY8z8ZcPX9Zu5dwUiNV75u9puoAJrFX7S7WXo7EgH3bERaOp6EN_bhl74biEDeNa8lm1Aq7T2FPuQfoWA64_psdd3b1BkEf9Mcryhtme5Uebx0lZIv0WgPgXypTjYplMDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون دولتی جمهوری اسلامی گزارش داد منطقه‌ای در نوار مرزی پیرانشهر در استان آذربایجان غربی هدف حمله هوایی آمریکا قرار گرفته است. در این گزارش آمده است: «منطقه‌ای در نوار مرزی پیرانشهر مورد حمله هوایی دشمن آمریکایی قرار گرفت.»
پیش از آن، خبرگزاری فارس به نقل از یک مقام استان آذربایجان غربی گزارش داده بود موشکی به منطقه‌ای غیرمسکونی اصابت کرده و تلفاتی بر جای نگذاشته است.
فرماندهی مرکزی آمریکا تاکنون این حمله را تأیید نکرده و درباره آن اظهار نظری نکرده است. تأیید مستقلی نیز برای این گزارش وجود ندارد.
پیرانشهر در غرب استان آذربایجان غربی و در نزدیکی مرز عراق قرار دارد. این شهر پنج روز پیش نیز بر پایه گزارش سازمان مدیریت بحران استان به خبرگزاری ایرنا، هدف حمله هوایی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/77612" target="_blank">📅 16:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ALFg-yYouo2ur1eaWwAYOV2TVB-olx_ZxSaWfAPA_D1pzHlMEBv6RimnLuEe1sSGq03-CA5VCR32bKUlP1v22xzZZ7aVbbHAg-ZUkQgTU-f2oS5YTPhyVDkIEoHp_eMiUlrl2rN5H4cl83rbjCKW_hzFJP5Z2mA2zfFpzb__0EvKiNK1OccWTw9Nl62h_Wc1EdpJNwsQFvrqZqwYIZ0HL5mFWYf-0wFOhLbkkg9sfjuk5bNXrb4j36WDpeblLjw0dKsWG9t-3no1P30iC2JEH2A9HGzZMb70Z3r7Zjq2ASODuyztRt46Hzntnw3_Ca6FWq1yFIMdtM8Qd5RksaxGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر، رهبر جریان صدر عراق و از رهبران شیعیان عراق، با انتشار بیانیه‌ای از سپاه پاسداران خواست خاک عراق را هدف حملات خود قرار ندهد و هم‌زمان از گروه‌های مسلح عراقی نیز خواست با اقدامات خود به کشورهای منطقه بهانه حمله ندهند.
صدر در این بیانیه که روز چهارشنبه هفتم مرداد منتشر شد، نوشت عراق نباید به محلی برای هدف قرار دادن جمهوری اسلامی تبدیل شود و از «برادران در سپاه پاسداران» خواست از حمله به «سرزمین مقدس و مستقل عراق» خودداری کنند.
او همچنین از آنچه «میلیشیاهای خودسر» خواند، خواست با اقدامات خود زمینه حمله کشورهای عربی خلیج فارس به عراق را فراهم نکنند.
رهبر جریان صدر با محکوم کردن هدف قرار گرفتن خاک عراق از سوی هر کشور یا هر طرفی، از دولت بغداد خواست حاکمیت خود را اعمال کند، امنیت را برقرار سازد و مانع کشیده شدن این کشور به جنگ و درگیری‌های فرقه‌ای شود. او تاکید کرد عراق و مردمش بیش از هر چیز به صلح نیاز دارند و سال‌ها جنگ، توان و ظرفیت‌های این کشور را فرسوده است.
این بیانیه در شرایطی منتشر شده که از آغاز جنگ ۴۰ روزه، سپاه پاسداران بارها مواضع احزاب کُرد در اقلیم کُردستان عراق را هدف قرار داده است. هم‌زمان، فرماندهی مرکزی ارتش آمریکا (سنتکام) بامداد چهارشنبه هفتم مرداد اعلام کرد نیروهای آمریکایی و عربستان سعودی در یک عملیات مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در عراق را هدف قرار داده‌اند.
@
VahidHeadline
مقتدی صدر در بیانیه‌اش به جای خلیج فارس از عبارت دیگری استفاده کرده:
Mu_AlSadr
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/77611" target="_blank">📅 16:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMakUGM8DE7r-sdcNyo_FgsNzSRpyZdsS_-zBZEyNMcV4UxBRQIsmO29baN7w0rmNreVJUV-a9a213HjXdCgVVWjlGwSLAZPVZRYmm-sg34fOCUb5PobzeYhLx5IQd3iP10DQ2pENWMxblP1FllleIRsdWfWOPxL__yNI2nxn5Nd8iw5FJE16NwCsZWwQa_RcaXZuEizZ4MU7woFL9H-dOTZLKPT7-_SAwCzC9OOR5QQIOpqBOKBipWy86Rpvij0vN-6qEhQreYw0W6EnLGA39XvMeGnGksuZNymOF-pEsuypOxsMujJvEds5gW7hXp-xIgWyzlPGjGgv_BaW7xF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ نیویورک‌تایمز، به نقل از چند مقام ایرانی و غربی که نام‌شان اعلام نشده، گزارش داد که حکومت ایران قصد داشت در واکنش به حملهٔ اوکراین به یک کشتی ایرانی، به یک بندر در اوکراین حمله کند، اما به‌دنبال اقدامات دیپلماتیک از انجام این اقدام خودداری کرد.
این روزنامه به نقل از این مقام‌ها نوشته است که انتظار می‌رفت ایران در این حمله یک موشک بالستیک با کلاهک کوچک به سمت اوکراین شلیک کند تا خسارت نسبتاً کمی به بار آورد و به‌صورت نمادین پاسخی به حملهٔ اوکراین داده باشد. این مقام‌ها گفتند که هدف حمله احتمالاً یکی از بنادر اوکراین در دریای سیاه بود.
بر اساس این گزارش بامداد چهارشنبه هفتم مرداد منتشر شد، مقام‌های جمهوری اسلامی امیدوار بودند این درگیری با حملهٔ تلافی‌جویانهٔ آن‌ها پایان یابد، اما مقام‌های غربی هشدار دادند که پیش‌بینی چگونگی واکنش اوکراین دشوار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/77610" target="_blank">📅 16:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bY4HtpAue9qU5U_zHuIR7v2mRl_inHgipq8mM2X79DukZHLatYY0WOUqPgZplHrsPwpfKOMt-iESZIBYPcRvGwK76ARZcywHBujyozaLvHeCUB5dHuf9vBlM9tdMD06-r6UxYoieQzzy1VrjgvNkrcBR2NdWGTCWP8kS7OcIeHyQjo3gu3maQJRONaEGtJcL_pYBddeTvXByU5_mWZdYzWDEL0Wb0YJ4MTWQ1Ssxt2BQm1gMVk9jgbliCAAdOyCd-rlOeLDQmS8OKhGJ26H22BGKd60yuTjgQpFyqty_Lc1ingfPXOloxyRdGryylexef-gFaYqHCin_W8heU_0udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q7uFOmCZj0M2nLiW9afT824ySVdn52XgrXqG-lWmEFq94LkDybIpvI5gsvXVO2b3at2WvTO3TuIjoU23Pp_EnoNJ_7P8T5XtbUCRlDQ9o4qxuKYg9GAO6QQi5dU1XQs96rJvYTxcv0hCcYQLjP7deM3mj3EcWVUFYB74duZCU6LXPaEnE79o8pOslvWqgpsuBpkjmM3mMzcCFTYoyZ2SlrlcAUdMPlsE3uvb-lDlWtkkCzSddSoXx-YPgqZGdhMKc1bL6o4mnvAlj-il3bq_werqbn2Vmq34oakU1A7bi3AMqdxh6VgJELYCIrffcY1ntGoFJ-TfLlqoLSHgQEdxWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برخی رسانه‌های ایران و کانال‌های مرتبط با سپاه پاسداران گزارش دادند که چهار عضو سپاه پاسداران در حملات منتسب به آمریکا و عربستان سعودی به عراق کشته شدند.
به نوشته این رسانه‌ها، این افراد در حمله‌ای به کربلا جان باختند.
بر اساس این گزارش‌ها، علی اصغر آستانه، ابوالفضل متقی، مرتضی اکبری و امیرعباس درهم‌فروش از جمله کشته‌شدگان هستند.
@
VahidOOnLine
شبه‌نظامیان حشد‌ الشعبی صبح چهارشنبه هفتم مرداد اعلام کردند شمار کشته‌های حملات هوایی مشترک آمریکا و عربستان سعودی به پایگاه‌های این نیروهای تحت حمایت ایران به ۲۰ نفر رسیده است.
حشد الشعبی در بیانیه‌اش این میزان تلفات را آمار «اولیه» خوانده و گفته است که دست کم ۳۲ نفر نیز در این حملات مجروح شده‌اند.
حملات مشترک آمریکا و عربستان علیه مواضع نیروهای حشد الشعبی در بغداد، واسط، نینوا، بصره، کرکوک، کربلا و دیاله انجام شد و خسارات مادی به تأسیسات و تجهیزات نظامی نیروهای حشد الشعبی وارد کرد.
فرماندهی مرکزی ارتش آمریکا در بیانیه‌اش گفته بود که این شبه‌نظامیان طی روزهای اخیر بیش از ۲۴ حمله پهپادی انجام داده‌اند.
به‌گفتهٔ سنتکام، هدف این حملات «تروریست‌های همسو با ایران» بوده است که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/77608" target="_blank">📅 16:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=Ud-lYP4WHSXrZNuHC03Veks_2UZwA6R3EJtyY36dVoZsiRJM6VpXWbF6ALoEh51wTXPQLWNprvdLmEMDYp8pAo1QpTiUpypBDyLRT-1DvN7nVlGxH7FXYzE2V56EylA_VSlc08kFdDXE775p9yAxjta0vR6o_bPMSFAcfVX03hsfIgL8nYQI6qzgNdN1S17HtNDzxIEBt7xKd26GEAZrMKk6xML72OinOqVfccIohNLnU7GjhnT-GA74f6NuLDmAjlwL8beKn9DfVFUyVJ1rqO_bwYGcI-tvUcahhEIJwCLGrf5ZqOhH4jneNHZphslkFuFUyDwwQWoUMoomjnsXyTvgTx33GiZrX1eJNOg41iw5ytI8exxv0f-ArQUpKmBojz7aaDyfNsntHCKquS2I_MppDZ5wYvesqZFlTjxhMPK1c3y05q885vHipJewPBGWayXo1OI2Iz3KIG--ECwvs6EiEfSV5ToRtlODIpAEM1XHR1PBGvcuhdUe7gZD8b9Zx-nOVSlj3y7MQ_1SOsd9tkE7YWq7H91HKo_4GKrY7aaKsvFqKjTZ5DzdGarrbMeYgwMzHRLxYC-A21JvPDs1MbxTIbgVRGhMskvkhaGnuO7eG2IVoJXdt3bzrbA3YuUKfqfT8RLfDcyr7pPjHDjKZdP-IoN4ZfddrLPYZ1qraV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=Ud-lYP4WHSXrZNuHC03Veks_2UZwA6R3EJtyY36dVoZsiRJM6VpXWbF6ALoEh51wTXPQLWNprvdLmEMDYp8pAo1QpTiUpypBDyLRT-1DvN7nVlGxH7FXYzE2V56EylA_VSlc08kFdDXE775p9yAxjta0vR6o_bPMSFAcfVX03hsfIgL8nYQI6qzgNdN1S17HtNDzxIEBt7xKd26GEAZrMKk6xML72OinOqVfccIohNLnU7GjhnT-GA74f6NuLDmAjlwL8beKn9DfVFUyVJ1rqO_bwYGcI-tvUcahhEIJwCLGrf5ZqOhH4jneNHZphslkFuFUyDwwQWoUMoomjnsXyTvgTx33GiZrX1eJNOg41iw5ytI8exxv0f-ArQUpKmBojz7aaDyfNsntHCKquS2I_MppDZ5wYvesqZFlTjxhMPK1c3y05q885vHipJewPBGWayXo1OI2Iz3KIG--ECwvs6EiEfSV5ToRtlODIpAEM1XHR1PBGvcuhdUe7gZD8b9Zx-nOVSlj3y7MQ_1SOsd9tkE7YWq7H91HKo_4GKrY7aaKsvFqKjTZ5DzdGarrbMeYgwMzHRLxYC-A21JvPDs1MbxTIbgVRGhMskvkhaGnuO7eG2IVoJXdt3bzrbA3YuUKfqfT8RLfDcyr7pPjHDjKZdP-IoN4ZfddrLPYZ1qraV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند از ابتدای سال ۲۰۲۶ تاکنون، اعدام دست‌کم ۸۸۶ نفر در ایران را مستند کرده است که ۵۶ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
زندان قزل‌حصار یکی از بالاترین آمار اجرای احکام اعدام را در سراسر کشور دارد. همچنین بخش قابل‌توجهی از اعدام‌های صورت‌گرفته در ایران مربوط به جرایم مرتبط با مواد مخدر است؛ به‌طوری که طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مرتبط با مواد مخدر بوده است.
🔸
از ۲۲ تیرماه، در پی انتقال شش زندانی محکوم به اعدام در پرونده‌های مواد مخدر به سلول‌های انفرادی زندان قزل‌حصار، جمعی از زندانیان واحد دو این زندان دست به اعتصاب غذا زده و برخی نیز لب‌های خود را دوخته‌اند.
🔸
با گذشت بیش از دو هفته از آغاز این اعتصاب، مسئولان نه تنها هیچ پاسخی به خواسته‌های اعتصابیون نداده‌اند، بلکه با اقداماتی همچون جابه‌جایی زندانیان و ایجاد محدودیت‌های شدیدتر برای جلوگیری از ارسال پیام و ویدیو از داخل زندان، در تلاش‌اند صدای آنان را خفه کنند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77607" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز: منابع می‌گویند ایران ظرف چند هفته سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد
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
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77606" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUdyX-IQuSqqBaDnujA16dDmbi8SDMh_btFToQtcD4XLBuKcDNS2Y9PbqXSh3nKAPNvZVDkwDeqZQbRBrNoFy3KWn8uPBTlAlefEjyQDHHmJ2vLeM98cOC0UyCdO-0okLdcJqVE-dxoCckJdac7OLgNqoBgWCRhrOV-2-dDh6MnbhyBJzkRY1XWSFU4GJiBGCF0wrsHaP4SZ3R5ev3KBnDLFIhpbgFzp8ryjZqzyRcxBmB8FAPHtfQ_iLsiNn-LBbFWDmfeMyoKO28RrHt3AxADU_-i8FrEloAh4Ow05yX1pgfTkVk9HZn5VheHr6tZPPln6yqgEAR6rQsMRH_7Ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی ایران هویت خلبان کشته شده مجید کاظمی رو پس از چند ماه اعلام کرد.
نوشتند یکی از ۴ خلبان دو جنگنده سوخو ۲۴ بوده که در حمله به نیروهای آمریکایی در پایگاه العدید قطر هواپیماشون مورد هدف قرار گرفت.
نوشتند تلاش‌ها برای تعیین وضعیت ۳ نفر دیگر همچنان در جریان است و مجید کاظمی هم با آزمایش‌های تخصصی و بررسی DNA هویتش تایید شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77605" target="_blank">📅 07:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZI0ZFtthl8GtGWf8JXhV-slZjNg2O9x21RK17oLxRHCHUA7kMzpSA65ed7HrVXkW6-ybscnbDtL5f3C7gAAlGe3plCME58t_J2PHytyFL8DWqrMTpFX8TKdnE_VWlI0m4Lw7T8SluMlR0ulE0IhWEFQoR3mkoKPtS6NYonh73NeZUnA-VOTHsTLYKp-M7kvUISr1Ev1bLdPsUrcwX3CDvjgTjaRi-rXfty4qDGlLeOI4UPYHx1hJwPZ5JIk9e7OIRkzq-GM0uV6s7eMfuvMz_Wmq-tVMaD2gUrMscuLMYc3JSKKhLBrdYzr741wwHt2CPp9VOx2apUINZNEA0xvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران، صبح چهارشنبه، با انتشار دو بیانیه از حمله موشکی به پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن و همچنین هدف قرار دادن سه نفت‌کش خبر داد.
نیروی هوافضای سپاه اعلام کرد پایگاه نیروهای آمریکایی در اردن را با چند موشک بالستیک هدف قرار داده و هم‌زمان نیروی دریایی سپاه نیز گفت: «سه نفت‌کش متخلف که به اخطارها بی‌توجه بودند مورد اصابت قرار گرفته و متوقف شدند.»
این درحالی است که پیش از این، فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار بیانیه‌ای اعلام کرد که تمام موشک‌های شلیک‌شده سپاه از ایران به طور کامل رهگیری و منهدم شده‌اند و هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77604" target="_blank">📅 05:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، می‌گوید دونالد ترامپ، رئیس‌جمهوری آمریکا، با اعطای مجوزهای لازم برای تولید موشک‌های سامانه پاتریوت به اوکراین موافقت کرده است.
آقای زلنسکی شامگاه سه‌شنبه در گفت‌وگو با شبکه فاکس‌نیوز گفت پس از دیدار با آقای ترامپ، با نمایندگان چند شرکت بزرگ تسلیحاتی آمریکا نیز گفت‌وگو کرده و امیدوار است زمینه تولید مشترک این موشک‌ها فراهم شود.
رئیس‌جمهوری اوکراین که روز سه‌شنبه در واشینگتن با دونالد ترامپ دیدار کرد، تأکید کرد مهم‌ترین نیاز نظامی کی‌یف همچنان سامانه‌ها و موشک‌های دفاع ضدبالستیک است.
هم‌زمان، سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرح گسترده‌ای را برای تشدید فشار اقتصادی بر روسیه و ایران به مرحله بعد فرستاد. این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، به رئیس‌جمهوری آمریکا اجازه می‌دهد بر بزرگ‌ترین خریداران نفت و گاز روسیه تعرفه‌هایی تا سقف ۲۰۰ درصد وضع کند و تحریم‌ها علیه نهادهای مالی، مقام‌ها، الیگارش‌ها و ناوگان موسوم به «سایه» روسیه را گسترش دهد.
این طرح هنوز باید در رأی‌گیری نهایی سنا تصویب شود و سپس برای بررسی به مجلس نمایندگان برود؛ مجلسی که تا پایان تعطیلات ماه اوت تشکیل جلسه نخواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77603" target="_blank">📅 05:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbqNApVMjfF0OJN9WCosC5P1olCM3z84agVw_Xqtru1NJu2WDJQZHDZ9z-CVwPJaIn6u-K7C63dUsmr4-rpmVsgDrMBtJ9YOE6NNALAFRtrXapAeNAK_9tla7GQbXZkFlRVej9vBJlM7JUf6MSioibR0NZmDJHtX47_vm4_nZ1qjJo7YtGV2mtSX4gW9ZeQstWmMSHXWLBcpsTreVzeBXnO9-IxFO9OrJPOTOZxanPHX-y_ezK7dQyN1QRQ8fGQODEO8VjunSh_VC7MlM8Zf4CJZHVHABnrVCAf_XvO-XZ88IqnMqfPkotkGSGTcKWrcKmPPX9m93jDkUrHW67MVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، با انتشار تصاویری در «تروث سوشال» از دیدارهای جداگانه خود با رهبران اسرائیل و اوکراین، درباره دیدار با بنیامین نتانیاهو نوشت:
«نخست‌وزیر بی‌بی نتانیاهو از اسرائیل، همراه با من و نمایندگان، نشست بسیار خوبی داشتیم. بدیهی است که موضوعات مهم متعددی مورد بحث قرار گرفت.»
ترامپ همچنین با ابراز خرسندی از دیدار با ولودیمیر زلنسکی افزود: «دیدار با زلنسکی از اوکراین افتخار بزرگی بود. موارد زیادی بررسی شد و این نشست بسیار خوب پیش رفت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77602" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77601" target="_blank">📅 04:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77600" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/alYgGVhBIsxPno2Sm6dL3E9xYWr5YEF9ZRFExaukTHfdXKmkpu2b3XA3gw6jwA-kXViLiJgEAaNb5jEqztP_M9_87KvmXMgaglKX4-y_e_xpfhIpDhcqnJ4djW7663w2Tya3VCGQersn9iaobnM_e2hPxTwP08z6D-zbMdJGbsRl-90_V9uBmtvzNAZXqwCyDT4fkV36MsNxiQAZxazWriWRTUnbRLa2xtOPYHJ0sn1NKdIEIM6NOJ6VZc7zLAbUbWl9WHHUa-vUuX5wd8mpCIkDa_xIv0Hrtk4Nx55F7_nhTtHsHNey64AhpOhb8JJ36jVbd5MffJylQsMNgLPTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرق آمریکا [۱:۱۵ چهارشنبه به وقت تهران]، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از ایران، در تلاشی برای انجام حمله‌ای غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند.
همه موشک‌های ایران با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنان هوشیار و در بالاترین سطح آمادگی قرار دارند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77599" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77595">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77595" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77594" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=Uzyj_TYjw4FuPP1eP-jq0M2BlqAy117mjt33q3_XHwV5r-u5if8ZMsIY8CJEJWOeP142PKdpn83texRcQUAkLfve2-TV82RoRxuZ0thjvWi2822xfYkLzn65lPPCUO8t7U0e_OQxcXnLLerJ4aIvJ0ssf8EGOaM8eN-XdldUXmoCaLZIHrmUm073xClGTrin-NuWsVaYnYEMT9QMuIWGpIKNJS-_UdetiM2134ngxWeYMWc4L5m3RJxBrTDDmbU8ixejcHJv_PKnA1X8dj8XU0ssVDQde5ScZYD0K-EB-T4zqbZ9QRtQ43rhfD14GajtwF3enD1L1LEpJ8OKa2gyGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=Uzyj_TYjw4FuPP1eP-jq0M2BlqAy117mjt33q3_XHwV5r-u5if8ZMsIY8CJEJWOeP142PKdpn83texRcQUAkLfve2-TV82RoRxuZ0thjvWi2822xfYkLzn65lPPCUO8t7U0e_OQxcXnLLerJ4aIvJ0ssf8EGOaM8eN-XdldUXmoCaLZIHrmUm073xClGTrin-NuWsVaYnYEMT9QMuIWGpIKNJS-_UdetiM2134ngxWeYMWc4L5m3RJxBrTDDmbU8ixejcHJv_PKnA1X8dj8XU0ssVDQde5ScZYD0K-EB-T4zqbZ9QRtQ43rhfD14GajtwF3enD1L1LEpJ8OKa2gyGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77589" target="_blank">📅 00:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cUdoMxSbZu5YNz4iEUr7Q8gIbnfk141hREwQXQFdGy86h5MSU8FNSla4eMl-mZjKmfnSUZGcFJ5y2BK_dyyHh0xfAyDJpkBW9wf0nK9LpeRYN02YdfKWDS9fNo9KTCtVj1op3m7rBiLY7UanifE1mXBJkUPoxS65rNpkHK6Bcbll_pEpUYVR5FU5CQzS-zmILElcAwHLsRgietcE7ZLYcY2t9TH9kQ5aXP1Dts2yi4-CiiaQ7MJivUSq7Gk82GVQ4Vk8YSuYCGFZ70n-146svRXU9GotKBigodWR6zh2OmLRwrLO5s3l8rbCAOhMx70SXuawrNese_c3yzWYkEW5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
این حکم با اتهام «محاربه از طریق مشارکت در تخریب اموال عمومی، تبلیغ علیه نظام و اجتماع و تبانی» صادر شده است.
به گفته منبع این گزارش، مهنام نواب صفوی دو وکیل داشته، اما وکلای او به پرونده دسترسی نداشتند و امکان دفاع از او برایشان فراهم نشده است.
همچنین دادگاه او به صورت غیرحضوری برگزار شده است.
مهنام نواب صفوی در جریان اعتراضات دی‌ماه در اصفهان بازداشت شد و اکنون در زندان دستگرد این شهر  است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77588" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucPAIJktHRMSy8DLwGR5Qbn8ORf3eDnCnDY0dJMGbQHGMkeixl1magP8H9s5VUarn1cZLFu8Q4lEb87ogt6WGBI4C4JpPHrXxEqdLfrzsp7Nu6D-K_miUUd1OdIUJJWP6g_DtX04e2mrQHgoreQ5aLcFqmTfigeRg6ItHheyh7_EUJ2ASDdzUe7m6Zk-jzOaMHI65fG83yYJ7t5HfSNoqqlzlhIo3zRrLMH5r09yvd5XUlXbGknJmaBCIH4Hxm8mc9v1lgqV2v7dXAML8dHiqMe4iSUWKFnDlT1NMS9xXSqG_Gmydo1rokx2cgE0-3_Y5LrV-0ttMaFwsM5yYY4xkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:  برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.  بار دیگر تأکید کردم که تمام اقدامات…</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77587" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=Lkhksx3WP4QeVZS34Xm1Y7MBVqcUERwD8xCUI8AY3xMQHLhdT-Y-i5cZ5oupGaCxBZYoBQffFJ3-IiLzPvmTgXyrwfZ9pA2T1fQNuTNFHBoLOqgTtEadg9RGoIO6s81dQBS7DqpX6wiapPedmW332F1KbwPhSCHK0vkrljcZfPqlUS0W7h2XgCi5GcSFlzSJbb87vUF-T46vtILlmy3OBxY0zagWWLD-gbU7eev6sO338XIAqq7NBbijJIdJsWdBZarXwkJ3zXj1Y2jRjhEfe0g34eHG8SeAl3nKCFFp-AXbABZ5mmg1W0Z3yTsSHdZKgwb3s0QumH1sWTLC_7k2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=Lkhksx3WP4QeVZS34Xm1Y7MBVqcUERwD8xCUI8AY3xMQHLhdT-Y-i5cZ5oupGaCxBZYoBQffFJ3-IiLzPvmTgXyrwfZ9pA2T1fQNuTNFHBoLOqgTtEadg9RGoIO6s81dQBS7DqpX6wiapPedmW332F1KbwPhSCHK0vkrljcZfPqlUS0W7h2XgCi5GcSFlzSJbb87vUF-T46vtILlmy3OBxY0zagWWLD-gbU7eev6sO338XIAqq7NBbijJIdJsWdBZarXwkJ3zXj1Y2jRjhEfe0g34eHG8SeAl3nKCFFp-AXbABZ5mmg1W0Z3yTsSHdZKgwb3s0QumH1sWTLC_7k2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77586" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=gCU9n0MoqJv1tJ_29yLGA0tD8L8b5f_0j9fd8QJJVoJhWZk6Zf2bWulPwR8aggn-vTJ3JG5LzOBzAgRDHvclbGkAwjkJpUSISRKPZPeeC9ODa2NqvUYV7cn_Czg0ihpqP6kSuaS06A3xXEDSV-4e12vknVALbD93X9t7SUC8mve9Fs-1hJOTGUgTVJrK5yz_6jhJACz97LRdEG8wPS42aZ0BE30EmC_t3qjdIETJhbO_3cQaZv7we_bYa7_KDvP-rtxYKZLUKVSdzvD4dQ7URn11wUjtZIp0-2jhueuGg9RmML02ItG1WBZkKF6fcxGW2uemTOuDeyCzH8chm-BYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=gCU9n0MoqJv1tJ_29yLGA0tD8L8b5f_0j9fd8QJJVoJhWZk6Zf2bWulPwR8aggn-vTJ3JG5LzOBzAgRDHvclbGkAwjkJpUSISRKPZPeeC9ODa2NqvUYV7cn_Czg0ihpqP6kSuaS06A3xXEDSV-4e12vknVALbD93X9t7SUC8mve9Fs-1hJOTGUgTVJrK5yz_6jhJACz97LRdEG8wPS42aZ0BE30EmC_t3qjdIETJhbO_3cQaZv7we_bYa7_KDvP-rtxYKZLUKVSdzvD4dQ7URn11wUjtZIp0-2jhueuGg9RmML02ItG1WBZkKF6fcxGW2uemTOuDeyCzH8chm-BYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی که در حساب اینستاگرام خود منتشر کرد، دیدار روز سه‌شنبه ششم مرداد خود با دونالد ترامپ را «عالی» توصیف کرد.
او افزود: «این گفتگویی بر پایه مشارکت کامل، حمایت متقابل و درک هدف مشترک جهت اطمینان از دست نیافتن ایران به سلاح هسته‌ای و همچنین سایر اهداف بود. این یکی از بهترین گفتگوهایی بود که با رئیس‌جمهور ایالات متحده، دوستمان دونالد ترامپ، داشتم.»
نخست‌وزیر اسرائیل در حدود ۹۰ دقیقه در کاخ سفید با ترامپ به رایزنی پرداخت؛ دیداری که پشت درهای بسته و بدون حضور خبرنگاران برگزار شد. نتانیاهو تاکید کرد که «تمام تیم ارشد» ترامپ و همچنین «تیم ارشد ما» در این جلسه حضور داشتند و این دیدار «فرصتی برای تبادل نظر و هماهنگی ترتیبات مهم برای امنیت و آینده دولت اسرائیل» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77585" target="_blank">📅 22:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JSFC1W5S30sTN3giRc8mTN905rRdMNIkRBWp0kebpmun4HsxVuCFcOp94p8PX9DO3vN30Lmn_yCNaE2bxBafKs5wvns1GSFbW2Ws9m_51ArB1EPnHYhoaPMS0j7g8rqnn5WdeUy8C7A-ng566SCJ4Wd7pgJhm22PyaDqpaZqK4ToCEVEWHMIJdhraYxCfxg35md8mC0QYQeyApNeKjHsgUwUZjKIqvgbCduUUnhepNeX9-b4ZtFU5Fu-oguwEksRmOhKRU1M1jiu8vtZuVH2DJP-AiO9qxAsWNn-nT6XqsScLFVi3jRBo02ZP_l9e8_FKfkkORBELnvnLJTqiTjyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:
برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.
بار دیگر تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن شناورها یا افراد غیرنظامی را نداشته است.
این موضوع درباره اظهارات ایران در مورد تبعه این کشور که جان باخته و نیز یک شناور غیرنظامی که در حادثه‌ای اخیر هدف قرار گرفته است نیز صدق می‌کند. هدف ما مقابله با تجاوز روسیه است که ریشه اصلی همه این حوادث است؛ و این روسیه است که مسئولیت کامل همه تحریک‌ها و تلفات را بر عهده دارد.
بر ضرورت خودداری از هرگونه اقدام تنش‌زا و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین تأکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77584" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N7CsXPwBqbOvBpy4G5-FDEHUUjJfZiCJa8GxFfmh8ez4mWY52_nwnGxeZAqdJKNrpBVWlj9i8ECWD0pk-M_Y9UBZdXgzKaVBQMFwmqTXH1JBl3vl8OqACog0HUWTpX-BktxsoHXA1ulClFpsLHt7lAE51leMw_7PvuzxFzrm2injd2UuEYUIoBiV_C9T2oU6VTvIyQmya2W7TAD_TARPrAMuk0n_BOFZSIhX4TOJLUTdAgcVPbYkLjetsSQqILixgTaOdlzXYemYPnBhV_gQF7jWfngtCrvdOhwHzpA2tgPCitKh7jW-KWvAi2oZSvkrxYNL2qMLReoq0TmUvVXTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TjSL6EUOBWIlRZSU0zA1QU1KPKifkYY2d480_lt_tSPqOoWjXa3WLLOVXRXDcqoJemPwt0TUJAjIkLGBWFVA4gePpsFgcstpC6muhQJ2-XiccXjAGe2Gm3pVextjZodNMW02Rf0cIz5f1nsly85sBqlX6RYWPGBKeZRwTyHCfMvBj52lyw9XEIb9dulk26e8oLqEnH_wwiPSoy7QoVTdh838XLNkIAtCvUhmnkjl1bZvnw3O8ZIWGnT5omzmq-sGrYgO16FMSUYCzNXVUj1NtswIrv12pdHXAkHIcN0X5ijj_Dy8PLO4h7atZcLeesLe1xmoTIMz7rZnmG4ZISsZ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GLof1bq9m63okdzf3VqH2kdlw60qq2AKoD_OCRWBAudR7TR86DOnThvEqYCLVwVmusK36A1bybLf1icECUJYz0YhYIFrikGWvYTB3T1gyreScS4_w2BHcEL-nXWs051UkRJg9tdxb0ADkeOY5hrrczRgoRy8DRAz5ovlmZSY3KnGI7QxBdtUSiF63KuHp8PJdqzYz5AWez_jkp-BxiLyCYLrRa1AvWIOE8G2Lq8-nBkWk5PYcWvqHr6pLs1uOYTLplw6cirXxuHNKMyemXJ8q9-uQhkwCK22VZjnEHUlBkY4pISZLGmCHX0KFhXSMAuICuwgcTzhHkA2d9V_2CBWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CWXSwMJUBy-trDhcht1rxbVfdzIvZqP02yUPIauauHPO3YcokD7MR89zZiWi4bSHV4kJ4OZic9iezvwA1v-H9QmMixTbxxbpqJPfw1ZiJoYwvVNjPl_aSqxVeDQQ0MAxFSaCB9t3uyWuIkBII_G8myi0GrPRWp0sbKdzjbhK5IAU5XozLFfcEhjQIcHaClZSvs1uuVGHjPHc5o8t4BqenVrFM6inlQRwKnB3ELi-WPcL8ds7rFPw1YwiNulLesv4YqBsK0sarMqYuAG1dAG_SgrqDFe5FScNZAJZTMCci3oIDVtvU-sbpxDxGXuUjouFOnNyDXMWUjHdd3X4FXpC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S---kO7G_s-SRgG_kxTWN7BNK93yIIBinna8h6B0dzCDf_8eHxHxUqzVQWtRAIAQ0H1ezfYrUMq3OjgSQMTHaZFuSbNM4bkOFvwyWF4rGQMRMWBEUDpZRSyehqbzSABtQVIk_-kihHPPUKTooHOkNj6sint4Sqg_dQTHTG99At8HPlNv1IXtR4zqZ1TnY6Ju-FVEr3ZWE6zTc0BXpwu8954AaUoyl5Oc7BrglmgGYbw9zD5S2D_EH6zMQq7nhFLbLcKELa7nvFv0-2D8WQ9R-fw0Jn2-q5voZY5h6yGjcKrEIxQ0GulLYkCVBnlA1nzRJAYtp7N3KqYsaeokvm0HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XbO9zLXnhk-XFHuAHWLccGYdYxWh13bak2stRumhLYkXz5uKwe1L5s6FGgFyEn1Vx-OS9OOKHe_2jZXi1c4NnqY4DJBZrGAJs7DP5-9IZclqcoi7EOEL5LwSD62Q5HXAeQ1MnxcaW1Sy8yZVnMBRiNSvyqjnTIxPNz_B5X61moYf9bWR1ctEfZBh4fFrQ36cm1knQk9M2N7_eW405RWJfJLoFNc0jos9vPNq7vmtxjI5ezpZ6MbIHQtaV1Q5XC__GmeAsetHPK_a3DB3Nb9VWpsv53QYahaJllGRGVKV6eedVs8zhEI9Ns7DnZVgiixaeMBGBiH1wXG-qvtG0QPKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RS7ztSGXqfw2T3R15avocQUkL6WSPHgE5yOpTfvoLDCTcDjPNlFOxyFSO7IbjbvyF3wqT7ba1ElMdFOo6vhhzdLpdlsZ1ujxYA4rJz_3swRoGExwk3uXxyWbzuWXa5dBYMmaCVpgx_c9arW7mfyqch_hOrVe1XSnJWBfXKCX5paqo28MTJOGCQc59TExEoZBvug0jAFASnjyx7iRZQF68B4bKCdpCI5-WiOe757b0L0C7yE4dd6dBy-rj5rkXhcI-aBNGddxU6QMIeiziRwqtkGUgCExCLa2nSTyJoI87D8fpTumqb-7xADLaBkxohXilRCYRcsodqppN3wQRbsgWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YHrqmgNainK6BchLYsierhuYqNIat0n8tbaUdYZ8oIDGCwg2YB1Hl4BZzKigbAp0a9z1a9xweVy0ugBVZLypIKn1d5n4WOyPwA2WCUd0B2Bo35Jqg-pE6IpyObWVFyWfFKgADIYPP4YcG7omDfoONImSrT6nNtAdGWIz8dI8uluHqiDfo-lIF5CpZIgB1WgTEmH6GEsIE4BnY-q_q8VbUx0xpxAoTK6vdvNgYUEi7WrCox9bnjGJ3dOixqoZH5ODVw5atw802WO0vhoGyE2bv-XdDm_HbHejveOFx8cwaglB_C7D6PDZ-LTadjIsWGBvzxq9UAEVZj8xvbNp8ubKoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل روز سه‌شنبه ششم مردادماه برای هفتمین بار با دونالد ترامپ در آمریکا دیدار کرد.
این دیدار در کاخ سفید و پشت درهای بسته انجام شد.
دقایقی پیش از نتانیاهو نیز، ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، مهمان ترامپ بود.کارولین لویت، سخنگوی کاخ سفید هر دو دیدار را «مثبت و سازنده» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77576" target="_blank">📅 20:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vjHqW_tJ-3gtEIM4w0ldP7hznoEWi5id51pthNAayvP6w051iT69FBLEbC7G4B9zhKcTVLaBN2kG_BV2lGFELSiOcTILNSrKnNTprQY4sZFuW8J5iG-Ou-mu9Pt8unMPyCrJRTkos61I4QLhsXPx4UR6zl2tPcsoi-MKByELLuP7TIXyoR-m46LLHfcCJOAjLrAXCwBVbzy3v6X5zox2rR3xomgRaX19dFtrFe9as_Ae0tYA6Y7_u0vy7aB3wn4FejxMmUZGln64Bny_b2fcWVcf7L1R8DTwTYwPuGjCcA2MYpjJ8WuSAv1B5pnpeTtQDeFZo0wvD8LaM131nchejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j_jQ-ojP2dsQhNOeoumI1Wz6n7kS0T-ocd6ykKXmPZob7XmuLjWEuTsfwZ1Z0blmq9iH1NNLHRE9RAsGQ5prNZyLmIAnujL7qPehrxaZsAUBLyGJTXZEMyj7TdxA7zq2ToYpyId5a12Wh9tkVYmqIvnz9PvlkpyW9mezvmhWrHxK1p_MkWP04b3HW-qaRBO97ONsbzmyIMCTI7T5RqHD0RzEbpoqIh6-P7NP6ifKcZ5tpqIeq-ZyPSeYRlmHtuw-Dh6mmjoTbyxT3qejrdB2TS26dSY6P6CVygDuwVZ1HKs0u52qnuhFzGjPixu-blA1_o5CeX9SZtrI0_PGPrAurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/smtTmeQJIAlIAQqWNftnWS6hXKLKxJqTf4aB7eMc7z1q70-kvzSmRYskA182jxblR4gXnKvjc8CVX4xzEZbpRGsS5mZqBNopoYjqnmAe4LF4ItRBPXKb9njxb0Ir4lwzc7zgFQLQ_WBOP-25p95IflqRPSU-lECyBeciQlcG8B9MMKn3gB3BLZAeqdbAGjFHo4qAkpSaHIywMcFq9iOBv-bFnMNREf7V9c1iQys1NvCmGurM6ZYE5BZfx2JwLLWt3GbzH3h4kfUUhtWS68PozI_khTBLAcrPxoKCMNp5uju-T1xcOcV1RCkFi8o_K7kU-TzZUJ61iBYKFzmyJJzn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DYxLImM5-iLxW4SL46wOw0bLhQNAfklslwxU31Ex5O9OAMW4J-9PUrgG_khob_BPHWYQfz493PCWJpZi853LKPnH1v6sQKA1lBkc8gnsGjdrVJt3l1tPRLZn1jlpg5mlc7it8Ei9C27jw0Rxj6VyohHqUkDKQojqToePIJF-FNf402MGx6gSgpKhtLGX2tNcimF-0BVsZ55vFeXT1mVYmPsbt5MQKWLFEOywsnSyLM50-jqtB9v--03pH1AVhQyLB0RVdFboiYLOy-jmc9tUtk46GQNhLY2QzWmPCBEdHkPVieHmWTl_ftx9yMm-EgU8D8ZH3TOD88b3roXf1QG4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iGmeNSYQjAgVjGX_zj2IlbENLvfF81JrLxWB-hDZkh0mB06RfaKEgBp6ePQZrhRYhGwBR0d2SkqgFTkQcnFopEmXpyCrUANXSBMWtUIyfDl_p8TlNtKShbobIFFo-TEHbEWtoYu5I8pIojR4ilTeohXjc6xRCgkMZr7lon5LBRYI5jBSu_odUX7BIk4-lYVfzxb6nsZV47cJrwCLRduA1Pis3-ctOoJhDA9pKB63fjDf2whv_yXkboWuT5PRjgltAd93J2r7nJpuNGDrLYjaQMa15QrJ_3gcQ7rHH5rxSBWCATrHCeDiyuDM6B1wLzTolERCLNDiaF6BEN1Fki-zdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77571" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qa3IZKQ4NH600ynaxGnnTPYLqcP9KjWV-_ESm4LLHGUpR3fXKIOBTfHqCKFUjGzmvCT68_B9rwf5ZH6w-ys-Wanof8cCTf4aBNLgNs6R-JfiGIbUFRbUvCOTrmyejAtyb6_KbmWjMyTpFUXNr_gPaAem-BHR1hZV35MZb-3yR5Jp-v9T44sCZfPcf-kruOf7guBTu4opU2-Ju8QY2NzNJQkvocU5pcFTZhX8Qq1tFJDLIb-ChyOa_rR9mO_01ANV7eMUlZ1pgenoZ1R78JMGM9CZawkAyHHPjrUgNw-K99M7KbWcx70p3jKKCbAJqlBYY89IxhvhlFu2w6I5aIuXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های نزدیک به حکومت و شماری از مقام‌های جمهوری اسلامی در روزهای اخیر بار دیگر بر اجرای قانون حجاب اجباری و برخورد با زنانی که از این قانون تبعیت نمی‌کنند، تأکید کرده‌اند. هم‌زمان روزنامه «همشهری» با انتشار گزارشی، از قوه قضاییه و نیروی انتظامی خواست با آنچه «هنجارشکنی» و «بدپوششی» خوانده، برخورد کنند.
روزنامه همشهری، وابسته به شهرداری تهران، در گزارشی با اشاره به انتشار ویدیوهایی از حضور زنان بدون حجاب اجباری در سواحل کیش، مراکز تفریحی، مراکز خرید و برخی رویدادهای فرهنگی، این موارد را نشانه «حیازدایی فرهنگی» توصیف کرد و مدعی شد که ممکن است بخشی از این رویدادها در قالب «پروژه‌ای سازمان‌یافته» برای تضعیف ارزش‌های اسلامی انجام شود.
این روزنامه با اشاره به ویدیوهای منتشرشده از ساحل سیمرغ کیش، برگزاری نمایش‌های مد، جشن‌های مختلط، کنسرت‌ها و تغییر الگوی پوشش در اماکن عمومی، خواستار ورود دادستانی و نیروی انتظامی و برخورد با افرادی شد که از نگاه این رسانه، قوانین مربوط به حجاب اجباری را نقض می‌کنند.
هم‌زمان، شماری از نمایندگان مجلس نیز بار دیگر خواستار اجرای قانون موسوم به «حمایت از خانواده از طریق ترویج فرهنگ عفاف و حجاب» شدند. محمدتقی نقدعلی، نماینده خمینی‌شهر، مدعی شد «برهنگی و بی‌حجابی مانند خوره به جان جامعه افتاده» و از مسئولان خواست اجرای این قانون را در اولویت قرار دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77570" target="_blank">📅 17:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghety_Cb-kQbWHyHqWafsyCWyIxrcJy1525kNKgQiQZAAIOW5CWhLUu4yldgJ5MZZtEu2G0eGr5w6oReQeQM8-0bVb1q3qWidhKVxbMyY9awhRJgylOl-cQloYc6-y1FDVfo44Wj9Wfyz7jntez2xu1HG9yskbaUS1VQ8skkL7L3CSmJiha1-WID4_RhLOcY1p1N1B_W1EvV9QjfUf0uLCa7hdetLdHIiqi4eAMjbn_46JlFCDgObW_knvKlom_KP7xuI0aMsFml6VmlCLZ6GzN4nrcE-02O48TwpMcxg8pCyhAtu-uKStgMiauTKjYBNAbtTVgT1Xj3sr3Jo44dGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=j15XDMvwB6Eb6t75yWuqqrLGeaOLmZZynXHY1WT6nnOeDMwUaCS2A6VBNgbr3pXGmFVUbCsVp2Cm7_3PpdRK-O7SZS7IBbuSbFCwDk_BqW01S40ev2P3gbQkLDhy_AZ4eezsG3gBOWu1Q1C_klKWzGIBYffsn3jbF2Wiq9xJ1GhG1Y3gYRWgsLSlSGRri08iwSoBvJ64fyji3LLo4qKa9jvdN_-6QlsTEodWEH-bEtifk7PXlodjuqp7b8a4qJTXmykSwPZm2Y2vDkiNi-auABOPEHIIHuD1SGVkeqpJbNVxbGsM8-88qTKR46sZUhXg0ywJq0tWM7qq7sfGxVjxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=j15XDMvwB6Eb6t75yWuqqrLGeaOLmZZynXHY1WT6nnOeDMwUaCS2A6VBNgbr3pXGmFVUbCsVp2Cm7_3PpdRK-O7SZS7IBbuSbFCwDk_BqW01S40ev2P3gbQkLDhy_AZ4eezsG3gBOWu1Q1C_klKWzGIBYffsn3jbF2Wiq9xJ1GhG1Y3gYRWgsLSlSGRri08iwSoBvJ64fyji3LLo4qKa9jvdN_-6QlsTEodWEH-bEtifk7PXlodjuqp7b8a4qJTXmykSwPZm2Y2vDkiNi-auABOPEHIIHuD1SGVkeqpJbNVxbGsM8-88qTKR46sZUhXg0ywJq0tWM7qq7sfGxVjxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77568" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B0eCHlwfjl8dJzi1Q6d6yQHspkP3dFyjk-7H1fwXkgD_iF6Dn3Qs33c35aNHGXR55utjz0vEAt6PuXVwcmvkh22oowUkNTbbAnCWa7OqpYfebllhSKHIv13m4GRuUrPggEwgS7WO0l15hlGZ1mbVvIyK-8yph22s_B4nQvYcqLgDREqux07iglNBZcFd81K9xN2qdwM6Os4RY2b1SeTrY3W5vSSxseOyORLBBbouQ0tOamYf_7xwuYhlEYUE0ZyEfQyAFYwOZYj3VS0pOzT3wRfbUutpxkacotACrUZZrq--nhj5Is9O7r5QW_yMHLpCf2O4cI0resrUKGgW__0XOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VpXMGkmiyIWjP_kohLvVL2NYKqy6B5ZCv00l_dCvpn8z15uxgoWF6Li8yZ8h8uZg26IlmVN_98S1ISEi2UxjPItr5cEGZIF4VOAaNmXnpRpNdS2uNJMOLopApajs55TfE7adlMTi7JrOm6GEHIUUsb9rOLDdAE68s_iB6HJ_-BW9B4dBBKH1EIKH-tbcG0NS1qEp7snltf1bvOQe1MxbFfutve-qok52KgKE0MxpywF8nA1EtNY3Y6V-clxWjJd9Z3Rx01KFf4STdjGYEm1LYzzoTGQZaj2gTxjo4PPtdZtI_GXqlcCzqArP8Uf7sJbYAlQvsOTP_e71WaJt3A1-Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77566" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ11B57Khlb7xj4ng4Nbdi6-MmBPTH24avsjF0Xl8Av7GlZzGGCUX53RTzZIvDRo-8aUVwKyME4ZYp5JMvNgOTEX98TkfieCcjY8HNXtt4lR3lDpJROjviSB2a0d5biE-qmlZPD-vzMleJ9N1P69bzk0pAFo-J2mS7QmuXkos-pkOMn_LpGD2FudgPBEWnl6FfMYzhyT7GQiQuNPzleCywAsAzux_ZaliHCjqou6NW7VnmgyLwtlVeMSG8Ua5wROVEoVqMDlBCc3e30fBZ5OCJZjvA90SkclOJfdmbKUYGriArsounU7rKtHFI5DMcZ6PmlA17gpQhQ8cR-Sxs5U6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه می‌گوید که حمله اوکراین به کشتی ایرانی در دریای خزر «باید به‌عنوان حمله به خود ایران» تلقی شود.
دیمیتری پسکوف، سخنگوی کرملین، هشدار داد که این حمله نشان می‌دهد که از بین بردن «تهدید ناشی از کی‌یف» تا چه اندازه اهمیت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77565" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwAevk4cu5YMpC2qBgEP2Amtxd-fCH9hRn9u_GljvwAPK4Z5lfLNELTUGXb3M-nHc4B79xUfkcKvee8F2522_SAflysmVfKMhzy7-2OOl31bvUxsYGl1CdtYETU2EGxogKpBsYUz1rPcZOH3ALRgc5YUO9YaawSSuhMUKPf3WRQeaFpkVcVoZwBumfUGyevgNMyqbd0x_WvM8ygyjVzCZQzoKKTPuE4vggCQ7xebNMKmkrNVGbaRzRjBesNmVW_qVBuWFlCXdAQLTqm2vdkaALKFoo-Peia2g0iOcVFN7cUMrug_WMh94CXTP51PlgmUeyvCFdZk23IFzAVew73tTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77564" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YcVAt0DK-IOcEZP8J8B3j8r-Agdz2qVc0VkvEWltG0r0yfuXnORg2SJYz2rxQH88fFPj6uWRscUkMtt3ySZQEidlilQb6BY8WV7c51eip1YZkT4amOktFOdP3oLdatQW3q4mxVApY7lJ89vF2C7J6vSm7MI6Ye07ha47CvQle3v-8OxhJN5LF0zCFs5SZ5spuSOr5_Ei7Iv8AOdic25gg-owbxswSMGG_6WlELjJARySzyN9_Yd3IThd1k_u3X3INFJMQ7x4lxkQ9XX-kubK0kj_EZSrxcT2_ZG2LHo5nU7NdHekKLnUfrs7tQZnGTCsOnKfUklmaxk9eGs53HGZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاسین سرفراز، بوکسور ۱۷ ساله اهل بجنورد و عضو تیم ملی بوکس ایران، که در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت شده بود، به سه سال و سه ماه حبس محکوم شده است.
کمیته آزادی زندانیان سیاسی خبر داد، پرونده این ورزشکار نوجوان در شعبه چهارم دادگاه کیفری استان خراسان شمالی رسیدگی شده و او تنها در یک جلسه دادگاه، بدون دسترسی و حق انتخاب وکیل، به اتهام «اجتماع و تبانی علیه امنیت ملی» به سه سال و سه ماه زندان محکوم شده است. این حکم حدود پنج روز پیش به او ابلاغ شده است.
یاسین سرفراز از ورزشکاران شناخته‌شده بوکس ایران به شمار می‌رود و پیش از بازداشت، در رقابت‌های کشوری، آسیایی و بین‌المللی موفق به کسب عناوین قهرمانی شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77563" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BJ-occp3KpXlo4ffgJ_Ecs1fQg9hMJLoduS4bmew3sgWg3xoLcXxVchzHPi0aPEGlaI2g0NysUt_6yqHcefSJLhW0pAbb1UyCJe5QJwdy0xIxCCmzcfVEq1EpBJ2nAFbLBxkaY34ypwKC1Q0VObTysF4v1oGaQCt4myaEXpPMzSVx9c2oMQHyWpchpOyGrleOJyLj3j-EzgY_PhY9oQOPPe7n8cM2_L7To-R48lz8N36qDRdBAbspnWQI5nUc4cRgbMIgwAlhnuXJqmrVicma7malA_8FZOQtl3cNlIbTKDcxcOqGhjRQYboOGaheE6yBeVet9i7d5HPxEZ43Yo2XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77562" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f9b4sDQ2pKy7kUAm0A651i-UuguIsnp1NzXSRulN8JY82twEJAh0RD6PoarZNyr-RDWbZe-0UHB8iEzT5H6VmztzGYRbuq5WBPZyT3f7f_IbavSxIyynN37Ej5yx_4KzCb98gYwvMppG_Q6l9aK5ej4mwRk3gPnDE0MRrOl8FVFjc3SjvuMuotogjmMSceKJ3vkvc5kmzkYAFTypS6qayKJvi93Sf4AlwcTldILps_678TahqMnpGeT1JFKE_kml4qDTinoJEc81Wpa2zkoRxYC47KCKNRVjKfGm5ZBI0D5d64kYZVLVeVWYbAeXuccgmYBHV9tkB_OBkq4CnuT2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gykx3H_Nk0JFgcZ_FzsEPMiPzGDGI3uG16iquSctdc8oYPywkWAZr2i_D81bXIvVjURJVr_JNf7QF3hRfoEpNbMw41Ki2xPLxUq8WwfAgjFt-YKUiJJ_rzDRm5KJe8knnSV0syhQxPsM5rGKYk9IajvRU4ljZ4XrQ_z4URHbd6FZnwejZ_niPVJ8zaAkkhIxrpP9qcd0PoeDTBtEQ5liImwYgY6xM3Ngv2pd2Z3xVSZkaUzWQNJz3S7FXf3SrDC77E63g3eCY9x5YsRbr7gYwugpZMCZ6eQeG6d4OGXW8Wk_KK3mPOwVqz8mHdewABxx-K3X11ssAFPSgq2ZDpj0ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77560" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 487K · <a href="https://t.me/VahidOnline/77559" target="_blank">📅 05:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/77552" target="_blank">📅 05:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 488K · <a href="https://t.me/VahidOnline/77545" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=o46rlApo6fc7izHAFBjFOywSZPo4fDAncesbw1v5EwD6LwRwBj9bghR4MGIjYbV1zbt4nft54Hf34-Wih27tJqPZyE9xRtgki2VxofAG1nlSP1Kz0DxscwtX7gDVrdJhQass9GeOcM1ckTtFgdhffF9cGgXEA4-nFtE4GSKNwxDF-9CdKn-lTRXrzosT2T5B2vMf5TMUYPayj8KDaZDC4u-VXKPcUFcykOKx6nhlraOb3T_ezeGKBDGIQWYMq7VP154gc5s1aQ7PAu_3QccdJMQ7GI2D53enZf3y9bRd-bAHHIki62g3G9_EVUc58dm5mpYBC_YOBWyAMqKCaiZY6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=o46rlApo6fc7izHAFBjFOywSZPo4fDAncesbw1v5EwD6LwRwBj9bghR4MGIjYbV1zbt4nft54Hf34-Wih27tJqPZyE9xRtgki2VxofAG1nlSP1Kz0DxscwtX7gDVrdJhQass9GeOcM1ckTtFgdhffF9cGgXEA4-nFtE4GSKNwxDF-9CdKn-lTRXrzosT2T5B2vMf5TMUYPayj8KDaZDC4u-VXKPcUFcykOKx6nhlraOb3T_ezeGKBDGIQWYMq7VP154gc5s1aQ7PAu_3QccdJMQ7GI2D53enZf3y9bRd-bAHHIki62g3G9_EVUc58dm5mpYBC_YOBWyAMqKCaiZY6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77544" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77543" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77542" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdS2uKUt8QOk63a9Wp3KQIsbFI8xq9KYGm-LyVS8EUrWjWxR2cAaFj1J9vBh3_ObS4FaOT1IT5vsL5rww3vqZ3RXnhC801DIw56udcKlg-i7zJrNbYSfpo1Ccenp1kHly9Hj0v8y5GQjPXkTV9h3vybx-VAB9KbiiL2QBfwFovhwjgNkj02qnUM2Tr_YdWM7te6yWUGIOXInXzuLCBxyOdL3oI9AaZvB3BWsumTqfW_KqwaXHFAhwDfZMQb-wEOedrAfdpigDwAkcHqlM2p6G7ZCVehhAKl_mvaghrZXQ69h0NdJ-0ahVeBppyqwRclhD5dCEIf4vfWkH-ZxLhBf1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77541" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mkE1AZF1i1TXeJTFWOEoMQVHc5poyyiuKobBv2N3TugiLZ8c8kvN24XuwdFAZEjrTKcVfqG8LAGrNQbwXlKA5pOH3urnJv2Dq94QRpedkM1FvloRhCOubMhLFIsXR0t_MYzfT37bPAE5FZnxv6_2qxvaDcJr5-rr8ofi2IESGQdBaxZBsPJIN1ASpOaSkDa3gVniITvDWAq6iXqrlE_TbWkntsRgb2yhSYXo6oHdb79WHzLTdwmhDIjiqiplPW_hzotfuYSmutDNItqFLng1rbOhmJf9zRalrJCh3a4BRPAqySglLYyqAmymkeiqvAno_jViAq3sP57OTkxBLLr9tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77540" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W09B34WBP-maOAnKuStfCsUTrv0ROXb4NQhKORLQi4giTwEqywDwYK7Z4waeGVlB4diAseYjgSuj46stMlREJ8HSJAyZ60TvPbZrERL5xtnvagti1DVkMAX0DvYhmF1kh0R4XAfmmP0rOcWXtb9PDfsyR7V-1J_Tlil8iLqyRc9gnxWHOsozxBhBRv75g5WWLMf4GDycyPTqLg_YiI7OJdS9bekFMZRIsdaC-AJXoky7ZZRS31uWu8Qsy98kx5SWApEam0KOQvS4Y780mYakgN6UD2vZS9vb13PdnL4M7tjjt-hyKyN7EF445oKcyTwdbMyUKi4JVdwJHIhVdmQRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی روز دوشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور، پهپادهایی را که از عراق به‌سوی تأسیسات نفتی در استان شرقی عربستان و همچنین شهر ریاض پرتاب شده بودند، رهگیری و منهدم کرده‌اند.
این وزارتخانه اعلام کرد که این پهپادها توسط گروه‌های شبه‌نظامی مورد حمایت ایران در عراق به پرواز درآمده بودند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد و بار دیگر بر حق این کشور برای پاسخ به منشأ «تجاوز» و بازدارندگی در برابر عاملان آن تأکید کرد.
این وزارتخانه همچنین از دولت عراق خواست تمامی اقدامات لازم را برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی انجام دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77539" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OnSpmx_Zx46KN7zsEgETt5zz1ZcPuZLVn84VP1i8b6THC42sYXdqjku8UkSm0pWQfe6iM5L5osRo0Ln6MO_XV7QLInmzbj8zy39C4eKP_Pjnbs-QM9qQlfDvRw6lC3fL43HKqNerbRQquMUl1NH3eNatMJ7qDdWKlrrn8ySarzyDDeTkP8YXnxt0xIEEKhwfwsu1hBcFtt_TJU29RRamvJgGnwJuz2aVyuH9P8Hk1t3GIDEJ2Gfk_dRDV8NZOJfA8_FGWDyLYlXkCFyGJMncrwvXMeIAFlpXCDnYa1Pa_fZbcRnj5-xl2hNBpT8WzJwd6GY6tUb4uc5qN5RvbTy57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح اردن اعلام کردند که صبح دوشنبه دو پهپاد را رهگیری و سرنگون کرده‌اند.
این بیانیه مشخص نکرده است که چه کسی این پهپادها را به پرواز درآورده است.
کمی پیشتر، تایمز اسرائیل گزارش داد که ارتش این کشور دو پهپاد مشکوک را بر فراز مرز اردن رهگیری کرده است.
در آن گزارش نیز درباره منشا شلیک این پهپادها و زمان دقیق رهگیری آنها توضیحی داده نشده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77538" target="_blank">📅 17:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFJHq2TStq50CV167_cdpoHhvekETRfzh6gtHLAcQA8HZ3FvhwNSeBODhvGKDNCa_J9UUiSkqauoPRNbckdHMoNFtscuKwOFC9_V0UP8n6F-D6peXTB4jzXyGrPTsTKdGGQUKGlZ7IVrStEO6vL8eDFx16R-k7hDPc-qrKLD6XNTAr8xm9WCczfVNDDQd7Jz4MeBAW7smebfCRaH6ZzgFaZ5oYDVH-3-zvlVdx9nxddDPr178tPKALljU1VjqMmETThUTDvqgeB6l65E5f1aK6TZQ8rlv9SXDqWxzG55kdGe74LTrte_AR62gMWBqdaPiiDh0hX4qJSDeSiLYBBGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«احمد الشرع»، رییس‌جمهور سوریه، روز دوشنبه ۵مرداد۱۴۰۵ در گفت‌وگو با شبکه «الجزیره» اعلام کرد دمشق با مشارکت چند کشور در حال تلاش برای دستیابی به یک توافق امنیتی با اسراییل است.
الشرع ابراز امیدواری کرده که چنین توافقی بتواند زمینه را برای دستیابی به «صلحی فراگیر» فراهم کند، بدون آنکه «حق سوریه بر بلندی‌های جولان» نادیده گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77537" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW8l9zdSwsL1Keimy--szvWDPTfAKPL7OdLHgMOn13z34KCmrNN0i-BKPJix1F7P0NstC0W9n_xCZGVZhZG33orAl4Emtx8uZyUDMf9YxbXnAzzpYCvYQoFMYJG3AK-k1FIh78MiBlNlIqKPquOiTFyxK_uoLig4z52rcS_Bqef8MM8t4vy3zJ9CtPjGnu04Eh0_kFii2vcJuUz8O3E68Z8wVzkKuJG5hQghs_u32pk46KKmGCp-zLvz5h01ejoA9QA2kzXx0URJxUzqO2jk75C4d6QxHmz6YAK81E1ReLykcCYdLijlJi-0pp67ss3ckT_7rSal7bhWzgbCJpd0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل، می‌گوید هرگاه دوباره به نخست‌وزیری برسد، «فورا» قطر را کشوری «متخاصم» اعلام خواهد کرد.
آقای بنت در شبکه ایکس، دولت قطر را «خشن» و «سرطان یهودستیز» توصیف کرد که «شاخک‌هایش را در سرتاسر غرب و حتی در دفتر نخست‌وزیری اسرائیل دراز کرده است.»
او همچنین مدعی شد که در دوران نخست‌وزیریش، اطلاعاتی را دیده است که نشان می‌دهد قطر به سپاه پاسداران کمک مالی می‌کرده است.
این سیاستمدار راست افراطی که از چهره‌های اصلی اپوزیسیون اسرائیل است، قطر را متهم کرد به‌دنبال «نابودی» اسرائیل است.
آقای بنت نوشت که قطر «کشور پیچیده‌ای نیست، میلیاردها دلار در یک شبکه نفوذ قدرتمند جهانی سرمایه‌گذاری کرده است که صدمه زیادی به اسرائیل وارد می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77536" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhD3FaGK9pATLXkn7srS0rWmJ91mTbfeR5ybeupHMdml5s_OBZ4nkU7bWrTa22Tw424VUT_OxkU9-aJX3qRG4scp9_x72_VexqxxiD5UOl0pYVsdvs8oFeGGV7HZlew7cQMizZ4uqL6Iy9qaW-QMQc92hfliB-hwdPlcjwxeqNsheUiv9n965NJ93LwO-WWU4Zie2oj8LS_BzY0d3E6EWD3NEBe8JuX3GTGn5EeCDcGDm6Km4CZxJ8i7zKZJiAExgNgKG1RzxidZGy_fzkQjCfhaP2uex1Kh1eMMzbbq1mnup-F1-hCibZyKd8ZcPXxHnLe1cggNHkzU1jV8h1NttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع بریتانیا گفت کشورش از اقدام تهاجمی در برابر جمهوری اسلامی حمایت نکرده و نخواهد کرد.
وس استریتینگ در مصاحبه با شبکه اسکای‌نیوز افزود این موضع را در نخستین هفته کاری خود صریحاً به پیت هگست، همتای آمریکایی‌اش، گفته است.
استریتینگ روز ۲۹ تیر و در جریان تشکیل کابینه اندی برنهام، نخست‌وزیر جدید بریتانیا، این سمت را بر عهده گرفت. او در همان هفته با هگست درباره امنیت دریایی در تنگه هرمز و تعهدات ناتو گفت‌وگو کرد.
او گفت با وجود این، زمینه‌های فراوانی برای همکاری دو کشور از تأمین امنیت تنگه هرمز و جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تا سرمایه‌گذاری در توان نظامی بریتانیا و ناتو وجود دارد.
استریتینگ همچنین گفت اروپا روزی از دونالد ترامپ، رئیس‌جمهوری آمریکا، سپاسگزار خواهد بود که قاره را از رخوت بیرون کشید و متحدان ناتو را وادار کرد مسئولیت امنیت خود را بپذیرند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77535" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SCWg7SJVJNuH2ysMLECnmrGDkuT9ocQil6PTpkY9Jd9_sZLN1L79YVQFw3IITq5TsUr0nzgF7Ao5677fgTPfj6Eq7oKNyWSXXUYRHmSzLBzprZTu06VZrjbl5UnHjYGkCKkfgWg32NEo-QaxaxswRuYtunfoomiE6YtHrzERHxL7FE81-sBJCtQf9soGxmIb358d3xw-Azd2gs5VF4SrIIZC8ilebVsud8Uy6H8wT7Y5HTvijer5GqEEbiSLz0XHRY_k_OdGEOJgj3Xv4f1Aq0bGBrO8lPzcuIBD0C64qJbpVwJe9momm0nZk6unCgYmIkhSvdcBAnZMUt-r2W-IrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77534" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKL8Cf80u81PoP6ZgLudVwEyib3VfGGBWpfYvEcXdb9oMx06STS3l9YZNI0605n0DsIBNE7dwZLWTN1cQ7aDB1RdvsZQ2W9E0Yqkap1Ji5l8QVBd_5tfNGHV7Kbufam7OUytW_vwXQbO8YSEpAnH6J2MtNylmbYuZ1xxDZehk3KSRqzMQIiVZidIFoIZPs06zFBMfWmauWn_JepUWzsPbKC5N8cT60W3q-ZXkBdwEEHmV-6-m5rG9SzxOL7a3RRWS4IW9Mr3G-7j3WxbhW5U6t5ZNyihbVvpVq8g5HcLO727l2mzgghPW-YobgiLPp0ACI-Vz4j_OuLdgfcIiBwrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، دوشنبه ۵مرداد۱۴۰۵ در نشست هفتگی خود با خبرنگاران، گزارش‌ها درباره درخواست ایران برای مذاکره مستقیم با آمریکا را رد کرد و گفت: «درخواست مذاکرات مستقیم با آمریکا اصلا با ژن ما همخوانی ندارد.»
او تاکید کرد که در حال حاضر هیچ مذاکره‌ای میان تهران و واشنگتن جریان ندارد و خبرهای مربوط به درخواست ایران برای مذاکره، «خبرسازی» طرف‌های مقابل است.
بقایی با بیان اینکه جمهوری اسلامی هرگز از دیپلماسی برای صیانت از منافع ملی خود گریزان نبوده، گفت در شرایطی که آمریکا به گفته او همچنان به اقدامات «ایذایی و تجاوز» علیه ایران ادامه می‌دهد، تمرکز جمهوری اسلامی بر دفاع است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77533" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77532" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77531" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f52us-iZ1GfL-DynTtQgJXDDAjZIHZGsck-nA5tBldPomg-nHfmlZqFygsmy4k7M0wFY51TwE1KU0umbn8c7qAMD4tyKb2xCXH1XAQgW2sYkEVPlShvbcK2L2f5sjCG6m7FEfOj30t7PBCGEAuYL_INFrXd01A1slvSDuJnKCp0C4qId8yPB1X3qT9_M3ValotgJekh8cyb70SKycWDgt4t2hrL3KxEiR28TKlVJ0k_KXjFLQq6lmQHoPnDeKNBV8RzymzskNGkUsMmDqrtoN_vbcvtfjQa9eoQMGbi9R-eA9_wa2Tv9pcRi5IdXlXDt3SY4EeTrvVsUcpjTlAvNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش خبرگزاری «رویترز»، همزمان با ادامه وقفه در درگیری‌های مستقیم میان ایران و آمریکا، بازارهای جهانی روز دوشنبه با «کاهش قیمت نفت»، «افت ارزش دلار» و «رشد محتاطانه بازارهای سهام» واکنش نشان دادند؛ در حالی که داده‌های حمل‌ونقل دریایی از ادامه اختلال در مسیرهای کشتیرانی منطقه حکایت دارد.
بهای نفت خام برنت بیش از چهار درصد کاهش یافت و به حدود ۹۲ دلار در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز بیش از پنج درصد افت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77530" target="_blank">📅 16:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77529">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77529" target="_blank">📅 16:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQElW-Kg_GgWDT6WUNw6ElNS-y3zPb2r9rvJaxarkCxpKD_Mt0WAcmT1TSZzbIn37LweJg0ZD6QtSypqn4vQknj_3WnflKbYqh1zJioGiXIGBSt3vCgeAJWn_tnAbs8UXOLVSeQirljbROQ6qZVXct5d0P2CvXxP6R4hycxFWxvIOjfapQ6mKMt9GYbB_IHy45aC988nDfcQRREBkQfcPqiov01OvXVxXK5TfBry9_r_Z3bn58GvLmmn-bkiqUVykFur5wBH25LFcRL2BFYIFJBulaWJR2QJgo__phP3ZQfqL2aSavFVi8zxzj5vXeDpBvQ4xdYkJMKDsozl561YAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.
«علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای حکم آن‌ها در صبح سه‌شنبه ۶مرداد۱۴۰۵ بسیار جدی است.
همچنین به ایران‌وایر گفته شده است که «سمیه افشار»، مادر علیرضا سپاهی و مادر همسر ابوالفضل سپاهی، در همین پرونده به پنج سال حبس محکوم شده و هم‌اکنون دوران محکومیت خود را در زندان سپری می‌کند.
اطلاعات موجود در حال حاضر تنها درباره وضعیت این دو محکوم تایید شده است. با این حال، از آنجا که چند متهم دیگر این پرونده نیز با حکم اعدام روبه‌رو هستند، این احتمال وجود دارد که افراد دیگری نیز برای آخرین ملاقات فراخوانده شده و در معرض اجرای حکم قرار گرفته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77528" target="_blank">📅 16:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77519" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/py9RC4bCHOYqi1lLmtXLfrofsg_lycybcuNI2RQ8iFUFvTdSkrxKovwks2WPGvqQZ6SfHSJJRm5DcDStsr0LY1LnNCym71gvCI45QcDoGkilQzejZhv-0Nw15LEciukKTMVwzfyT3OrIP7qGoOSGFjtd0WgwCyC8952gEe_wWMRK4OXZUzfo-99aweIhJm4Ok1fm_y3jCxBpdpp-XgTiAfDu_8diLsji-vYJBEDHD5kfwQdCm3k5VZJ24wkGxuNW_VT-39rHkT9K6B4BRbgf3SpDnYnf0HuhHR8n23uSsecrRMTM_4rpZnwYGh7XquZTSmbxYVCnYfWGoEzvHvHlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MrBJOBzfmbet5pR7hOWjOzPLsQpA5s85WuDVV5eOlylBnrE6Zv_DULSAp_5x2pBTNKqcgEsQtXVzA7xRMnSIFalBt1GkAc1H4FLrrYvgWl4HulHe36y0ulbL9jhcNCrt0op1LJZogCrf5G7wBJqhFfc-ZFhwbZ--Zil4ORPZB_N0E-8ckszgAPNDZEeE73LKJRjn5eU5EjlWy8omGY3yxRlhpAuMyUWCSIjVOcIpjTQxqK5WKVC3vHXL68aV4cq5iTqGyPLD6uZt1qfEAL0Hi_eCQbsouv11Rzwg765yw7WM3DNCutCFu7V7i4M50X79Z8JFC5xnZPlYC_LpatL8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/drqrC0dYfupvoAU6n0QpbttvZbtlpgkhf8LL21tjYshBt5A7njuajjBEe9m9HlyokbTBuaIrZ0m9IEs-H25oDy4exN_rZy-GoEbh--RYL9UlHAeB8HjD4Qw0IoAKOt5ZPPMOqFn1mYQYmqmDTPQ2hVWsmBuPeDeXnTeWOUNcEyYWPR9qxgZQDv7gfgf9MIQC87ArQZPQRw5nGDD-Lc6zoXaPN9oV5nNlxp_AXZCntMxbhpe-mIgC9UUCE3t5gzRNf8SNVV6zdMRyt7_69FV_17lnnz0gmZ4ovuu9ZzuP-tAvMo__CPGkIOfXz8wQt_i7dXk_nV46NqvY00Gr_ObYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbACYxNc-TNbbfiKwTgZE3CKhm5k3cXfZx6egNS48fEWlZPfZq-8pxmBRpSeq6P1Mn1fSHMNKme8u80XtLK2QW3WHoaMIAk4-tLuByCo3-h95YL2eEfYFb1Rl04SJxHtACr7pwYHtIoAXoH5KxESIt-G4TUuc3oKn9Hvd_LlrOOMAZFumhx-uwyJDk51mDMHL8ruIGWYOst_bOBDiyPGjjlIu69XEJgqvMTW9AHLk4eMBpQZSl9ddC067iyr1a509Xnv-cvzTnKZrLfNtOt88mN7AaWVyGNImxTQEPHU8HMFH2aa-3pEbrUNbppnigmn_NBvmNRfhnRpqgzbtzfoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q1NRMlUTC0LGjy_VhhMZuHgSPkEV3q4dbKhBOjFAZs9W0fwbLHEn1H4_Utm2aM-_UxjbXJ17eOTUfSxEwwnP_ZtffNuUwCqcJb83FTcZ-kMMakeY3fSpA2flYMl7cPp8lKsteiZWDmkQ830YAMItVK94DzAs2ZLbKOPpd8pyXdFGsseiv0GB-Y2th7ndDDlA_P__vIy80xbOYYmGDz90dqsts6DP_KaFtUYgREmlpiSKa85R47Y4EtpECTLvBSFx9_nkDaHFsr9BeMHMQlNH2vmoFkqtDDfdFUyBq_in6ZDEhccoM305yH7XAMRdwe_ItbiFZCKvlg7UVLjeJ4geRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حساب کاربری خود در شبکه اجتماعی «تروث سوشال» تصویری ساخته‌شده با هوش مصنوعی منتشر کرد که یک جزیره شلوغ و ویران‌شده در میان آتش و دود را نشان می‌دهد.
روی این تصویر عبارت «حمله به خارگ» درج شده بود.
ترامپ تصاویر دیگری هم منتشر کرد که با هوش مصنوعی ساخته شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77514" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBRyowjzpjqnMYqKUQSNY1fkVh_4Vzs55eqDuJN4FF0ykqlB2Jq0Cg7PzP8tLvcettzkiWegzkfVLURv5Rn6Tv1ZplJlG64yiK-06cDWzYl3fOIm2pqPRQeHi0vtXiVtzNhIhbTBX2XOdtbNBMLPd9gHZSgdyOKNwERHEgzaTRWYDdyLINSuvM9p8Bne66PfYIdo90DczAj_81VOhIBvHgkG0jExM83gutJHtP22m4UaIrGZSnXZN8WWz79QUTX278nFD7f3X3FiaThjwk3UzXWD_BQw3QEZ2jlnojWXHpv0GSxEjIZYcZX7OycwfrOudVz1vfVmfeh_3vIDZtFvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از منابع آگاه گزارش داد برد کوپر، فرمانده فرماندهی مرکزی ارتش آمریکا (سنتکام)، به دولت دونالد ترامپ توصیه کرده است کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا به اعتقاد او این عملیات به سقف اثربخشی خود رسیده است.
به گفته این منابع، کوپر ارزیابی کرده است حملات دو هفته گذشته توانایی جمهوری اسلامی برای هدف قرار دادن کشتی‌ها در منطقه تنگه هرمز را به میزان قابل توجهی کاهش داده و بیشتر اهداف تعیین‌شده برای حملات هوایی نیز از بین رفته‌اند.
منابع آگاه افزودند کوپر به مقام‌های آمریکایی گفته است در صورت تصمیم برای از سرگیری عملیات گسترده نظامی، آمریکا می‌تواند ۲۰ درصد از اهدافی را که در عملیات «خشم حماسی» هدف قرار نگرفتند، مورد حمله قرار دهد. با این حال، او تاکید کرده است اگر تصمیمی برای بازگشت به عملیات گسترده گرفته نشود، ادامه کارزار بمباران دو هفته گذشته توجیهی نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77511" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkId03DhceTZi3P40ue7C3TMYRr_3cnJG1ZJEV7sDuDL0HPaoIqHbZmhUh-AhJVkXdz40DJuiaV6fJAnqurzZqSkPCobcEcZh_kRgr1ag3dXpPqs-IRypbVVAMwwKSpWDOFkfvxX6KcJPvQ5o2MCOQaw-g5peFQ7tM2eFCBnH4MqG2hh3EBNSJ60Uaf6ZbdX-wLsOWQGpXUP_xNxtWYZEgMhlz8zZxqR8K6851l56b26yrsB-U7Bj2dxoK9Q8ivWyhx9YjCImOz4-HHzUkbwwkFrckwK1sfnd2h611IFRt4s7GKnKx6K-YBPZtzH9TG9q_K0LYtFTnOHLjcfpCsXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران با انتشار پیامی در شبکه اجتماعی اکس، حمله اوکراین به یک شناور «تجاری» ایرانی در دریای خزر را «نقض آشکار منشور سازمان ملل متحد» خواند و اعلام کرد این اقدام «نمی‌تواند بی‌پاسخ بماند.»
عراقچی در این پیام نوشت که ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، با حمله به یک کشتی «تجاری» ایران که به کشته شدن یک ملوان ایرانی انجامید، به گفته او «به خواست اسرائیل» تلاش کرده است اروپا را وارد جنگ کند. وزیر خارجه اسلامی افزود که در گفتگوهای تلفنی خود با کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا و سرگئی لاوروف، وزیر خارجه روسیه، تاکید کرده است که این اقدام نباید بدون پاسخ باقی بماند.
ولودیمیر زلنسکی پیش‌تر اعلام کرده بود که نیروهای اوکراینی در عملیات‌های دوربرد در دریای خزر، کشتی‌هایی را هدف قرار داده‌اند که به گفته او برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77510" target="_blank">📅 19:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdg8cI4Et1KPwe5-tMx1aIMupErdReZo5Z-BYG0ZQi82iSvt7HYgQ5xad-v5Lk5YaYllC3WepcucGliHMGG8uswSrPDDx69Mr-CCpRzKn135TIBo9DLN81HOD2EN3bPo7t3u3vW9q8GoEJ3jYCl8PvlGRqycwC1v2aOD1rc5rWDjjyZHzxPiKJZx3kl5PXBlJ2Lrxm8laxYOE-YtCP5EqXNNzi6kU28u_RTJbUUzBExjNIFuF3m4nbRfwZZW715iPpX8-tMcrU7ADQnM4-xL_VI7p5jFv-Wfa3BHEQSfzB_E3Uv1B1d7ZIEf3yPt84_Mx2VuJi5lax85_2VR4v66QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77509" target="_blank">📅 19:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnWEGNGGNu6jRdzGG7M1RSltF8UmKUPFLu3gYvtbH4GLWHo6u_hcG1qE59YuKRGJfHvGXFukspt9u8QQqP6wLFUp4XHK47pLY5kl-e9CaqSVF8lK9v-Qmw21xz56UnT1b-MHTItLcDXryIgpRLb78abD52BsOgkHHQu5l9bfgJBR22cLhpmYMEm8yoThyV_DloW6S37GkbmXe73VT8cpEMuJSSSqz4q-gWt2s7O5Qfb7stYD_KQ2qc5iviVdxjBrDJedXRAcIbfBytme_VT8HLbDjpsOMp6goPNRJLo-rs-8PR3bltu4xo8d5f2-6jj9kcNoc9WfC8EAKr_bda3m3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل، اعلام کرد که دونالد ترامپ، رئیس‌جمهور آمریکا، حملات علیه ایران را به‌طور موقت متوقف کرده تا فرصت بیشتری برای پیشبرد دیپلماسی فراهم شود.
والتز روز یکشنبه در گفت‌وگو با شبکه فاکس نیوز گفت: «او دارد به مذاکرات فرصت می‌دهد؛ کمی فضا برای پیش رفتن گفت‌وگوها فراهم کرده است.»
سخنگوی ارتش جمهوری اسلامی نیز گفته که در پی توقف حملات آمریکا، ایران نیز حمله به متحدان واشینگتن در خاورمیانه را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77508" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TklC1gYRtbE3IH3sXLOg452d0LNw7q-_VnRGP0f9oDKj0x-llPE5lMtasmybCpbEG_HvzgQcNQaEqZwgBGUpkvv-kJV3hnfRRc2wcgflIIggkTLQh3o_SqZmNXVj3rMGS5bMpg8pc_0yjh1-sLYGE813fZ35xt4xZGL6XjKc2xDv51FQcXdhHdDLD1q9ORGOsYZgtQNp8SSoBVJ8DHXN8wFsQwP1jomdkp35-exAfY3J51vDdTk3fETclHdiI0eNK8qHxOTuV4xppfKquRC51euzpp1PJz5LK5bpew_XcrLmT1HAL4SHoqSIsMbhSNzwRoBnF8R8-N3nnqHG1AWb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز یکشنبه مدعی شد که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
بنابر گزارش تسنیم، این نفتکش پس از خروج از مسیر دریانوردی مشخص‌شده از سوی ایران در این آبراه راهبردی، با مین دریایی برخورد کرده است.
بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد که اواخر خرداد بین ایران و آمریکا برای تمدید آتش‌بس امضا شد، ایران متعهد شده بود طی ۳۰ روز در تنگه هرمز مین‌روبی کند تا تردد کشتی‌ها آزاد شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77507" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E18ehsqkhEA2CVSOxUjJFqwx-GPpdOsgLJ4N8wHVcSqWcprTFCnx4LSfgHoUuWZwJ_p7vfoWI64ElzW9ncj_w-nlpoyMq0OysJUUHqX8m4lBlFB1wVZyLRb0cTEZW3qoFaaA0HxpCWqFD-XK3HyhxEVqCXsLAiOWIK0nz1IKJ9O5hbP5enrFhEjZebdtP2vIMcOmEwWVP7ifk-MwgZU1hEz_OyJyU594Hyiy-JG8DsZS139zCXCQlWZWcoPoQkzxMI-xwvPtJgNWdSFvQMe6XVU3n8AtRFRVEm2Uxz85NkcH6LsPhr6sSSbWIsUfbVDvJu9V-VZC3b4jag_3PbEdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری العربیه، روز یکشنبه چهارم مرداد ماه گزارش کرد ایالات متحده آمریکا و جمهوری اسلامی ایران پاسخ‌ خود به پیشنهاد مشترک پاکستان و قطر را که با هدف ازسرگیری مذاکرات میان دو کشور ارائه شده بود، تحویل دادند.
بر اساس این گزارش، منابع آگاه در گفتگو با العربیه تایید کرده‌اند که کشورهای قطر، مصر، پاکستان و دیگر میانجی‌گران منطقه‌ای طرح جدیدی برای برقراری یک آتش‌بس ۱۰ روزه به واشنگتن و تهران ارائه داده‌اند. این طرح با هدف ایجاد فضای مناسب جهت حل بحران در تنگه هرمز و احیای توافقات پیشین تنظیم شده است.
العربیه نوشت، این پیشنهاد دو شرط اصلی برای بازگرداندن دو طرف به مسیر گفتگو دارد که شامل توقف فوری اقدامات خصمانه و بازگشایی کامل و ایمن تنگه هرمز به روی رفت‌وآمد کشتیرانی بین‌المللی است.
بر اساس جزئیات این طرح، مقرر شده است که مسیر جنوبی دریانوردی از طریق آب‌های عمان از حملات نیروهای مسلح جمهوری اسلامی در امان بماند و مسیر شمالی از طریق آب‌های ایران نیز از محاصره دریایی آمریکا خارج شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77506" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77505" target="_blank">📅 16:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77504" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lj8MvM_wpqfAV3uPrxxPEtfBXx65v-0AWIlLUUkLIX8GuyeQUjtYepNAq3TGpf2W6Z2UQfPbUmFv6al7gFjZsA1ob_7-idCRUuOSLt92_bsV87s4IbIYnZNoHNkYGz9vHRI-SskKiaArryXBUApfTwCYtUeBFRdzOThmREmWGtSW66jGO-FKF2SgwzYR0koyx23FI36UtcLecQZcWQhrThwbIy-zIgGxBir48UL_xzk_M-Lpz1Lh7i93MgC7fNnnzGXeZFjpXWpXANd3SP1kXSN91B_pVytoH8nucCiKEug58k4MPLz0PdXN4pw--lA4atJ7FoHJyAfKJ3LIydysRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، روز یک‌شنبه چهارم مرداد بدون اشاره به جزئیات از «پیشرفت‌هایی» در مذاکرات و تبادل نظر تهران و مسقط خبر داد.
این مقام جمهوری اسلامی پس از آن در این باره اظهار نظر کرده است که یک هیئت عمانی که برای گفت‌وگو درباره مدیریت تنگه هرمز به تهران آمده بود شنبه عصر ایران را ترک کرد.
بقایی درباره این مذاکرات این طور توضیح داد: «روزهای جمعه و شنبه چند دور گفت‌وگو بین ایران و عمان در سطح معاونان وزرای امور خارجه در تهران برگزار شد که طی آن دو طرف در مورد اصول مشترک و سازوکارهای عملیاتی برای مدیریت تردد ایمن کشتیرانی در تنگه هرمز با رعایت حقوق حاکمیتی دو دولت ساحلی تبادل نظر کردند.»
مقام وزارت خارجه در ادامه اضافه کرده است که «در حال حاضر تغییری در وضعیت تردد در تنگه ایجاد نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77503" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vp503spqIBDJ1hX9uzh2m4WSPpEIrtKNGqFTw4cHbjs_YSI-1MvVNvA-Px6ma2X6hw_tgIazigVqeK0IWBi2m2TdMmf_zu5yXkd3_bzqm9hBNW9BVXShqxugtxYw1VHvDYm8IujjnyhOlPk6eWya-auT05S4yxOKNn9z_tB10RPEDlrvvxXJai5gL2cBUjFAuOmWYbfbVQFA__4sNm5RbaRGaFZ4paTgtTA86rtyvexYh58TpXNyVaJwYjxL5vxxNOvWPXslk2wYROjBMfOiqAfUUNnDAFBNGMj2xC3LWFIz5GtSAFLir8lf-w0k0pPHHiIb4e8u5syxzpC0bUkzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که سال گذشته دختر ۱۷ ساله خود به نام فاطمه سلطانی را مقابل آرایشگاه محل کارش در اسلامشهر با ضربات چاقو به
#قتل
رسانده بود، با حکم دادگاه کیفری تهران به هشت سال حبس و پرداخت دیه محکوم شد.
در قوانین جمهوری اسلامی ایران، مقرراتی وجود دارد که پدرانی را که مرتکب قتل فرزند خود می‌شوند، از مجازات‌های سنگین معاف می‌کند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77502" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77501" target="_blank">📅 06:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77500" target="_blank">📅 03:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=aPQgCdNIY7JHD6ZHMGP4CsmJcP8FY1L_niAdlGKA27KVDZl4GzrhacjB87IvGIfvKvZULkpLS5hUEYroAeaaTTTq5jnniNpDN6kq37BKmUymEMEUhx4R4lMrQEJelFD__hFor973MImu-oObenI8YGNl4jHYAHIhtkiQ8rhymz3b0T9r5IkwnJVIdegDur-BjCkn_jvwSSR9AC1lRP0o6uXx8GWi2956Fcmcc8disiNTLP2IzE0vx8xM6qbrJFEV9U5cQhauOoLG7RGt3FAWNBhvp8bITyZ7OUCAJyvVkFAd2vN7lFU8VXLy0G-QnQzWKPZq0wjDY2cOVMdWAX6sag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=aPQgCdNIY7JHD6ZHMGP4CsmJcP8FY1L_niAdlGKA27KVDZl4GzrhacjB87IvGIfvKvZULkpLS5hUEYroAeaaTTTq5jnniNpDN6kq37BKmUymEMEUhx4R4lMrQEJelFD__hFor973MImu-oObenI8YGNl4jHYAHIhtkiQ8rhymz3b0T9r5IkwnJVIdegDur-BjCkn_jvwSSR9AC1lRP0o6uXx8GWi2956Fcmcc8disiNTLP2IzE0vx8xM6qbrJFEV9U5cQhauOoLG7RGt3FAWNBhvp8bITyZ7OUCAJyvVkFAd2vN7lFU8VXLy0G-QnQzWKPZq0wjDY2cOVMdWAX6sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77499" target="_blank">📅 01:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXNljbNU8g_7ul5Ht7b5zd7XFUHQSFZmGp2lWcaZhPIeF1tRbsmzey-t3ALcGNpCky5SYTfn-3Okve7n12dfzjM8KDPgUjy3Wz34VlJUtMoIFr4Xle2sGpgnT9g5qBMJbv747dpKtous09fmzrTQoJsDmd-9Ow-0Pzfqmss92AQ4p426D14j3BNTwGJCrMd7PAcNgpW-lvF8Bf7-ogAxffBuLa8cSPYRlC1zl6G_TiqZWu37gM7ueGl1ZscpysexUxY49yO6HYSbQY-uGynApY5K-CMiICyp1L0yNLJMuprgsFNxFyiWksOc-6iLC8cJwCEQYGDDwvh1oiibS61PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه هشدار داد که اگر دولتش به چیزی که در مذاکرات با ایران می‌خواهد نرسد، قطعا حملات گسترده به این کشور را از سرمی‌گیرد.
خبرنگار شبکه فرانسوی ال‌سی‌آی در شبکه ایکس نوشت که در گفت‌وگوی تلفنی با ترامپ از او سوال کرده که آیا در حال بررسی ازسرگیری یک جنگ گسترده علیه ایران است یا نه.
رئیس‌جمهور ایالات متحده در پاسخ گفته است: «اگر به صد درصد آنچه می‌خواهیم نرسیم، قطعاً.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77498" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRv7L5M1T6BmzEmdedxQjZlhrK4YIxDAxC9SY6JrNESxafcAXT9AKeUw0JFc2zAwAaK2FcVT8Z0mAifXHEKkllQtaKgWD_Rf8oQQZZMfGwyf6067FbE5FN7iBFc8SJYswTZ6FSpxuqX51nDhR7dmaKbTR0FllE4jsG-2nmo1xMiGoXQ_QIbx8YqLUvSyspNytl0saKyo-SnH74MvbqE1XoD8381avmLhsb5ty_ZGeDdW5b-JrmJ30UiNDgOkQzKRHSdK2ZA8Y863q9ZaWYlPmpecL4Ln3op9OQ8NtUpxX-esGyjnjvd-99FMm3uMNv1YNBG9ayMtDY9ldBWbHAvH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/77497" target="_blank">📅 22:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJBiE_KN0xKPNnYOULTf_EQKA3_HpaxvwvE3JGXI_STckrevTuKWLSU6BgCVjuvieV5rw9VOZQEon66lCOMzC9rkFryJ8cYgZrvFboPf3zLnrEkOpc5NN4TQxoKgvHP4LlVD7yYvSD9TvoLoYGXieEP05PYJZytcHeau_Gq6A6sooDBs1DxlgRmWjb6jz2ssafoa_cn4RauCkTW_03gbpj5AyyrDYkIKEPxw3QzTmyGXzQ2pB5ksx3KgDq2cSzH63wRRzJUbdrNsJMhR9HdY9iZT6Pt-7RTxiBEUy9UWSG8ldHeaQSfUypjiWVwxYuQEoLOT5XA8EBKI48WN0udCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی پری، خواننده آمریکایی، از استفاده کاخ سفید از آهنگ «Firework» (آتش‌بازی) در ویدیویی از حمله آمریکا به اهدافی در ایران انتقاد کرد و گفت این استفاده بدون اطلاع و رضایت او انجام شده است. او افزود که از این اقدام عمیقا شوکه و خشمگین شده است.
کاخ سفید روز پنج‌شنبه ویدیویی در حساب رسمی خود در تیک‌تاک منتشر کرد که در آن بخش «boom, boom, boom» آهنگ «Firework» با تصاویری از حملات آمریکا به اهدافی در جنوب ایران هم‌زمان شده است. کاخ سفید در توضیح این ویدیو نوشت: «به ایران هشدار داده شده است.»
کیتی پری روز شنبه در شبکه ایکس نوشت: «از اینکه آهنگ "Firework" به‌عنوان موسیقی پس‌زمینه ویدیوی حملات نظامی در حساب کاربری تیک‌تاک کاخ سفید استفاده شده، عمیقا شوکه و خشمگین هستم. من این استفاده را تایید نکردم، از من اجازه‌ای خواسته نشد و به هیچ وجه آن را تایید یا حمایت نمی‌کنم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77496" target="_blank">📅 22:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/phKaZs6Qk9KiMslB-KnsTc6BFoTa3qvpuGChtQG8kc9PmT-fYeJxo4UmK7Qrbj2ZoBdYMHfHMxN493Y1wLvBnIj2pClxRmJ3xaPXEedrSRE1HqP3vgsQ2Njeey8TV-DJJDnCm0YqEaMkdPjja67YUOYYC_f8YEQ3OHpjYyaX82GP1Nq3t4lFubjKLNFGN5TKq5UuUSD8NEmbKgJvIiSazRHzEFdjJ4M59iBb5uHIxBNS6T6-AxvxfUXkB-_ntMNtcuHf1I-xFRMdwPUlzGxdv-B7hkahpK3jd5fd2w5C_fBt-TrFC6O_hg6WXkNzi_cDkwad9NdAT4rmaJi3g9A5Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77495" target="_blank">📅 20:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=adHVwUbxZgzwn--GsBryj595L757LqdKkqZzlvYJMXGxTmbrY5GMv3seUrn3VYd6vYUxl30WJSDePDUVpT1lpNyHlEDKPjx_-dYO1npOyY8o57VLn0Yw7nIVWOFps8JISAGEMvw9d_893PAeagG7Fngn73JrgUnfuTU1PytDQqkEhZYG_HM5p6vJqfX5tiza5SAFpXxxpyAVCHJZGwxkXyso7HVcUPylv0W9W10wVX-XQWh1AQ68zSRD8DLP7sACjgNE9SClBAacbiFLI0Y8Ffd-eyAKH5WbJaF9aI654eAfH7XTJwuMPJmHCqAkK-RE2r_IhsAY5dMDXMABoDk3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=adHVwUbxZgzwn--GsBryj595L757LqdKkqZzlvYJMXGxTmbrY5GMv3seUrn3VYd6vYUxl30WJSDePDUVpT1lpNyHlEDKPjx_-dYO1npOyY8o57VLn0Yw7nIVWOFps8JISAGEMvw9d_893PAeagG7Fngn73JrgUnfuTU1PytDQqkEhZYG_HM5p6vJqfX5tiza5SAFpXxxpyAVCHJZGwxkXyso7HVcUPylv0W9W10wVX-XQWh1AQ68zSRD8DLP7sACjgNE9SClBAacbiFLI0Y8Ffd-eyAKH5WbJaF9aI654eAfH7XTJwuMPJmHCqAkK-RE2r_IhsAY5dMDXMABoDk3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: تغییر در قیمت یا سهمیه بنزین قطعی است
سخنگوی دولت مسعود پزشکیان اعلام کرد که تغییر در قیمت یا سهمیه بنزین قطعی است و دولت برای مدیریت مصرف این سوخت ناچار به اتخاذ راهکارهای جدید خواهد بود.
فاطمه مهاجرانی گفت دولت همچنان برای بنزین یارانه پرداخت می‌کند، اما با توجه به ضرورت ایجاد تعادل در مصرف، تصمیم‌گیری درباره نحوه عرضه این سوخت اجتناب‌ناپذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77494" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en-aWpcDPvsf2Xrl1XIaKHsj_tgPzbxUSonlc1lQYNXZD4BLU4wQDIYuV-JRM_V5pVpF0pmcSXWOVA6SBGFBUiQgFwyxWhxvtiXMLVY97elgcnadgZEevSJDc7sOPmiK_GT91rCnDuvietCZGGBQ4XhVtxGA8mym7lEwLOr4fQ1-4C2pNOXfcLSEcBLRc48JAzJJ3CyuY9uGxHahBhDNPtGy2po3GzZxaVynf_nYaLQWXbot__yi5sE9XsjiRIZHf-nFw2T2R3ZRNCtyyHU3CL5EQrUUYLLyOjOjROjNek_kImiG0nbcro-E60vMoFM_0RdmBqMj0jU7U2OQz9YMuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77493" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt6QaeIG4I9fa8N1oRZuRE7AVr-CGtyD1RR2i_tRFX74FsMurF6el5T0ywUt68VcmVGPLEcbO8aPQS7c_oCpfS6oOVF_H9JRmH9rE5eqo6na_ldDGJOl2C05lFQff_Edt898jMsbfWEzWsNkBPZj06UAMuyu9Nr1DF_K7HBPp0VDAIRM9rTTu4as1xDu3LoXqFPcpDVz0oxRA8XkddNsLNp-nlm4sWSog-rK5Up_vOq20Rz-davKzy2VRh6LdDLV7FwhzbR4fu-dNu6yELywiI1izkGzqHBVIlnVf2tBVV4FLxc01Ee2PdrQzhNYSzttSWYqFX4EttsXEPcsc_dagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.
زلنسکی روز شنبه، سوم مرداد، در پیامی در شبکه ایکس نوشت که اوکراین در حملات دوربرد شب گذشته در دریای خزر به نتایجی «بسیار خوب» رسیده است. به گفته او، در میان اهداف این عملیات، کشتی‌هایی نیز بوده‌اند که «با مشارکت ایران» برای انتقال محموله‌های نظامی استفاده می‌شدند. رییس‌جمهور اوکراین اطلاعات دقیق‌تری درباره هویت ناو جنگی یا کشتی‌های هدف قرارگرفته منتشر نکرد.
سرویس امنیتی اوکراین (اس‌بی‌یو) نیز همان روز گزارش داد پهپادهای اوکراینی سکوی نفتی «فیلانوفسکی»، متعلق به شرکت روسی لوک‌اویل واقع در دریای خزر، را هدف گرفته‌اند. بر اساس اعلام این نهاد، دو کشتی باری با نام‌های «پورت اولیا ۲» و «بگی» نیز در همین عملیات مورد اصابت قرار گرفتند؛ کشتی‌هایی که به گفته سرویس امنیتی اوکراین در انتقال محموله‌های نظامی میان روسیه و ایران نقش داشته‌اند.
تا کنون نه مسکو و نه تهران واکنشی به این ادعاها نشان نداده‌اند و گزارش‌های اوکراین نیز به صورت مستقل تایید نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77492" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 491K · <a href="https://t.me/VahidOnline/77491" target="_blank">📅 06:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77490">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77490" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77489">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fCbKce81_Vex3BTyzHvPXfDiIReZmEkru30tozIpVTzCSYh6xYHRs9dJxR8xyZhhNFW_aYD1C4CXIpv9QzfAE9aIbm0ihpOqVjG_8TR97d5fQ9x_OhC0RZrsBACTQqja-xBAvVqgN1ClpWgMDt0Ley_qz03K7jxJocVwdSjmKx09Za4ZyF38LcZVuy7PPZsyL7cm7BsTTW-8KXHBcGA9CTVN3ZPwHJwqjIxkISaNTwB-4EidFW5u1cTd7F19CoIA6BNC5vw-UV_oNnUhASTvpAqnHB4t2ulAHWgZrG57oiHu1BZ1niMb1nyVsZxvfaALp3_vsZ7DkTVBUaWwrGtrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت فرانسه در تهران با انتشار پیامی در حساب ایکس ادعای روزنامه انگلیسی‌زبان «تهران‌تایمز» مبنی بر برگزاری جلسه محرمانه دیپلمات‌های اروپایی و آسیایی در اقامتگاه سفیر فرانسه را به‌شدت تکذیب کرد و آن را کنایه‌آمیز پاسخ داد.
تهران‌تایمز پیش‌تر مدعی شده بود که در ۲۰ ژوئیه، نشستی با حضور سفرای چند کشور اروپایی، ژاپن، کره جنوبی و نیوزیلند در اقامتگاه سفیر فرانسه برگزار شده که در آن موضوع خروج دیپلمات‌های بریتانیایی و هماهنگی برای فشار سیاسی بر ایران مطرح شده است؛ اما سفارت فرانسه با رد کامل این ادعا خطاب به «خبرنگاران تهران‌تایمز» نوشت:
"به خبرنگاران محترم روزنامه تهران تایمز، دفعه بعد، لطفاً اطلاعات خود را با دوستان‌تان در سرویس‌های اطلاعاتی ایران که حدود ده دوربین برای نظارت بر سفارت فرانسه دارند، بررسی کنید. متاسفانه، هیچ مراسمی در سفارت ما در تاریخ ۲۰ جولای برگزار نشد !"
FranceenIran
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77489" target="_blank">📅 03:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77488">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77488" target="_blank">📅 02:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nb2TLhq_S6bL_n6kyuwsuVf7CNXRNl2HGSPEvVNa1EA23mcCiOUpY3uhis0vCt0XlAtRAR70vqb4eNvGjlHIGyt6nXLoSk7tFtzuujW4_yyUxrbjMSOzw-nOHGB37T6ZG5GcCpeFuTUsS-SREwvX1MbO7qFaBYV4C4pGFzjfbMS5ZFP5Vz_MExKOGLr4k3wZJ5vHjQVfkQUBY_epzUv_gVeL6OeaPkr2wr20Av7utxVL_j6hZTx8pHi1GSu9uoODRmBdrynlrS3Yk275M9wtebOW-nQXJydfT7rJJWBZHdqO4aCTR4Uo2pSa6mmJVpTrQw2NkUkflS-6deRJzC99VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مشترک نیروهای ائتلاف، جمعه‌شب، با انتشار بیانیه‌ای اعلام کرد که در پاسخ به اقدامات «بزدلانه و شتاب‌زده» شبه‌نظامیان حوثی در هدف قرار دادن کشتی‌های تجاری در دریای سرخ، عملیات نظامی متناسبی را علیه اهداف نظامی مشروع این گروه در استان الحدیده اجرا کرده است.
ترکی المالکی، سخنگوی رسمی ائتلاف، با تاکید بر اینکه عملیات پاسخ نظامی طبق قوانین بین‌المللی و با تحقق کامل اهداف عملیاتی به پایان رسیده، تصریح کرد: «بندر الحدیده هدف قرار نگرفته و تمامی بنادر یمن از جمله الحدیده، راس‌عیسی و الصلیف برای کشتیرانی، ورود کمک‌های غذایی و سوخت باز هستند.»
او همچنین افزود عربستان سعودی همواره در کنار ملت و دولت یمن باقی خواهد ماند و هشدار داد که در صورت تداوم اقدامات خصمانه حوثی‌ها، فرماندهی ائتلاف برای حفاظت از کشتی‌ها و منافع ملی «بدون هیچ‌گونه اغماضی» مجددا دست به اقدام خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77487" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77486" target="_blank">📅 01:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/77485" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4YdIt60AzEA11dRN8ixLZKx3VRZIyqPSakpgYihp5PSzW2utznHrB7YZQy7Q8EuK12te14x9_TP1pqJk_yME_Q-piVebnbwFSX_SwT9s5N-ALMKMW1siHnxc3ec9LwRGOt2uUj6fQbvH5AsE3jn5aQCnKOZFC439Y8Wfi6aW3iZaGNdq4l7WinqzfM250eoXteS1zmN2dnFWsb9b4IMpEjsocRru29bc4UAx1yiG3h0a3_sUfWtLaj-vbSla6fMPUxaSLllEJO-rdgo3SyVFIo1-Izo9jcnNhMCQcURAd7stSdMeP5I-cKCFKC4oFQzwCTzfuB7d56preJJlPJcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون روز جمعه دوم مرداد در ۶۶ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77484" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tveZmil4H2ESic7yiXFBjzsPNc2pMbsaNgLnM78Qn0VJTEXY9nA13HXYrIEWzPK43Gac_eJ0rAG3U9Fl5p_-al9xv2Zuu4FuLWyV0xbdfOJ1CsVulOUByysFGO2H5qnZfyKI5gcq6SK-kYLV_5mJXttPE8xEgWEOrI3yfhvZ_irYxmqx420Fj0_QcALKX5R7_1zK69Igju8SS3s8UKcsVtcTj1TeWvlbRxQJaaq9hoyPquPuZGXTcrCixAZottSq9P9znIG3SMEmp03e0lE1H7V1Lkp_DhaTCzCP8F7VtpBOrQGGk6z_cvlF72rmDweOq-8KVCFU0Yo6qrLjcV9b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WBOnlYuncX0t8rA-B0FcsMgaP8n30BKp7CeL_QCrbP2T9a9IirCByyLIUo_SKwO4b3NqsJhYWG481q8-gQgIohBH9gNZgvSfx8kpqUJePb3zyi4PnaQ-ap8dXwXv4Ih3sLo0-D57g9Mb-deTVvQZJmYMlGfeaaLpEfyLT7oivPwuD0GFYKZ8qlLqhJuxb4GDCuf_24jM6fDYxJePYCXr3bmMbdRlZqaPoHB_1Y70uz9iK5otK2eGkEe4fGom5Hgm2NwGOlshuLjgGxx_oxQt2VVmuRpFHoy2IZwwrnIl4sc64erga5eR8JfcfLE6t8ZfsFMAc1Mnngft8kLO-wWgOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77482" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1SqgtDaHGLCOUESuqKB58kyV313eUisn9mUPiCow8U11BmCT_ghdBEFosrqVOWmAKME_iKJ6Jkl3GjTA1bKUwGKmTrw4DwNxzeiFiWJX7YS_TtLPK4cMKrLP8Irjmc5CWIW7hrvVrOZcWXmv8tLzQm5nVmMcRLCW_2C_qoZg-MG_zO8qerpjTQZy2WgoLcqjr7cYywFJYkWi5bNThBlVX9D9Nlvda_kLJ_oknM0MLuy9IXAVUO2XXU7Efl_SaDVukHDGc9s70cfIjXDDPauQB6LOXH7RLz12R6468FLz-RP9KRCbjkbAcJO8atKqy6a72MX68AYeBdEifwyKphC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رئیس‌جمهور شی، در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت — و این اظهارات شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، حرف او را باور می‌کنم و علاوه بر این، من نیز لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین جریان دارد (روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز برقرار است)، به من گفت که به ایران سلاح نخواهد فروخت. او می‌داند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را پرداخت می‌کنند و اینکه آن سلاح‌ها چگونه توزیع می‌شوند، هیچ اطلاعی ندارم.
بنابراین، دو کشور بزرگی که مردم اغلب در ارتباط با ایران از آن‌ها نام می‌برند، به نظر من، در این موضوع مشارکت نمی‌کنند. اگر چنین می‌کردند، برایشان بسیار بد می‌شد — و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77481" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRClzuRPBerSa1ViUWrYO96g4K3L0mD4IElSLrthQ3tMOaJjkhDOBSrlVptmoNCN6issu03O4tmvkL7HLXAUbqLsAMbGimrHLeOYWPh4PTQecCWO4lziJmyUPOmMP6aVEEm2v_kGAiaX6jTpuAIy8wszN1d3Gxig1s0Hkq--Mbj2IjjUaXYK1hzX-hRPsayACpvByEUMwYMuDrhBjlI-yd37Tll3GZtJXJTZpFAfXIOrCQ-HvrCglpbA-I5gUd2RT-rbznl8eXHQ3dsGhbEEJ7IDsYEoIuaVNUy_U0lZwol_ihZH2zvO7Go7ZWYnI_y_q4soK7S3075ONaE_JZhdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای اطلاع‌رسانی دولت روز جمعه دوم مرداد، با صدور بیانیه‌ای از اقدام سازمان صداوسیما در سانسور بخشی از سخنرانی مسعود پزشکیان در روز ملی صنعت و معدن، درباره اجازه رهبر پیشین جمهوری اسلامی پیرامون مذاکرات، به‌شدت انتقاد کرد.
در این بیانیه با اشاره به سوابق مشابه، از جمله پخش نیمه‌کاره مصاحبه رئیس مجلس شورای اسلامی، سانسور سخنان رئیس قوه قضائیه و پخش نشدن مصاحبه‌های وزیر امور خارجه در طول جنگ، رفتارهای صداوسیما «گزینشی و مبتنی بر سلایق سیاسی یک جریان خاص» توصیف شده است.
شورای اطلاع‌رسانی دولت تاکید کرد این اقدامات وحدت‌شکنانه دقیقا پس از پیام رهبر جمهوری اسلامی مبنی بر لزوم «وحدت کلمه» صورت گرفته و نه تنها شایستگی این سازمان را به‌عنوان «رسانه ملی» زیر سوال می‌برد، بلکه تهدیدی برای امنیت ملی و انسجام اجتماعی محسوب می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77480" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77477" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4iRl25Sqcaln0H18yZrVBaw0Wrp6f-0_RZ6hv2s5-Q4hEyJy6ecr5MM7--epWZKxBfKDeshek6A3gi9t2-HBmvGVA0Hvw4S0NOyMn-NKoq8ND6wKkbzpEWgPMLga3ie_kTYmfMDGq0IHUQJimd2aLAbQtqSYzqjr8hH4_sC_HFXpgza57H_sF17G4ShXWrnKG1ZFFV1HAAiFNN2fQ8Ha4_mJG8sMKwNEs_N8rL6kD5hMVmRV_wSR5wbDd6RDRmQWagOv9_srzMSjrbZlJDMcyNdwCHB9aQYZ5lUO44rTRKPnmzBbiR0DNlaKj-bn-inS_m84P6DlP10CPskmbcC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران روز جمعه ۲مرداد۱۴۰۵ با انتشار بیانیه‌ای مدعی شد در جریان عملیات موسوم به «نصر ۲»، ساختمان باقی‌مانده مرکز داده‌های شرکت آمازون در بحرین را هدف قرار داده و منهدم کرده است.
سپاه در این بیانیه ادعا کرد مرکز داده آمازون نقش اصلی در تکمیل اطلاعات ارتش آمریکا را بر عهده داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77476" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y_mdFKXdd9viSBbth0wsw1oUTUZxWgl2nJ3M9dyYuZ5FLSYPU7a_RLQB39EG5XarnBXQDJ4aFfydqARHjsrTFAXPzrPfmWRS0VIp8RzzzNArrNPLLJ0HfxcnBgRX4SKDCS-6XxBTrAJtoiyMxZVxFcns8xo9atA7eKO3akPhSLGtNsObQKTAIz3oP9jJW9Sy63dhz5YRwMXWCA3MxCCTxKTFSfDp_EWR4bprsZqKNmD7I_w6BinPaO1PGoIXxRdxkj8zBx98kTOTDDYzw4lUA2BmXh-TEprf5-9Hgsx8W_YZ5j-BsUEqpEV_VBDhFbyothbLwmqy-naV3YKHVcAqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkmeV7D3Uy8M4xSThaFyAM1Fuf1iWI0q6ayjYCJNXJTb4OQR_FALjna46h2tQ5eNeG3I_y8r_1vghxlEvjASATHJk-m4d5iod-mvu45CRejK1MNJ8qBYMyWxFvtze_pX7llVLtDB1VPOHB4KpuXvTX-s5YCN7w0EXn-vCIy7aWAWTHCHRKvJXHEmGIDxNnlV-gFf1ZN6ARFhtFVhZauefpMPeH6JRN1h-j9h6Meosbymg7CoK9roocQowM-6DegrTal11BBdWGy5KjIESj3ax1F_1LS5zvKpmv678VHDNK4s9eD22bup5XjvhdRYSziGlEbReqChUWtuWx-bc-NzFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77474" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
