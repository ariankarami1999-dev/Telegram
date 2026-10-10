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
<img src="https://cdn4.telesco.pe/file/RNySXtYNBopA3iwwhDcp3mKG5kQtJNw4c2vXJL92PGAxodh8onRPNimOu1159XNX1yh9UaLI8Y_JKIwxHHfZnu7IzBNRnmVOcvLWvJgKUsJ4bdQpbtM6e3uHXpYZ5IwRO241GRdBzqDSIXRPNkOIjDmb-FMS-O645EjAa_pX5Guo39ClUq-9U0WqWmDWT5mf_-nUX5OPWrgnFULC4JcqLDfFiBAtKLhzA20f4xXl-BDntA9cQ53N6nQjUK7O51OyoSHH8ENRS37a1c0Zm2KSKQYONMM8M5cOD70GrLHlpnHD_TBA7wlYYbDFzDOv6rg2FbDTku7mzOCKAuPb1HjXTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 00:25:11</div>
<hr>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گویا تلفات غیرنظامی بسیار بالایی گزارش شده.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/21608" target="_blank">📅 23:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">روابط عمومی نیروی دریایی سپاه پاسداران انقلاب اسلامی:
یک فروند سوپرنفتکش متخلف حامل نفت خام، که قصد خروج از مسیر غیر مجاز تنگه هرمز را داشت، به دلیل برخورد با مین دریایی از مسیر پر خطر اعلام شده، دچار انفجار پر شدت گردید.
این سوپر نفتکش که سامانه های ناوبری و موقعیت یاب خود را خاموش کرده بود، بعد از برخورد با مین دریایی در یک آتش عظیم در حال سوختن است؛ به گونه ای که برای مردم ساحل نشین نیز آتش آن به وضوح قابل مشاهده است.
نیروی دریایی سپاه اعلام می کند: آتش سوزی مهیب عاقبت هر نفتکش متخلفی است که بخواهد امنیت و قوانین تنگه هرمز را نادیده بگیرد.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/21607" target="_blank">📅 21:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آیا موج آبی دموکرات‌ها در انتخابات میان‌دوره‌ای آمریکا واقعی است یا خطای نظرسنجی‌ها؟!
با نزدیک شدن به انتخابات میان‌دوره‌ای آمریکا، نظرسنجی‌ها از تضعیف موقعیت جمهوری‌خواهان و افزایش احتمال بازگشت دموکرات‌ها به قدرت در کنگره حکایت دارند. با این حال، یک پرسش اساسی همچنان مطرح است: آیا واقعاً شاهد شکل‌گیری موجی از حمایت انتخاباتی به سود دموکرات‌ها هستیم یا بخشی از این تصویر نتیجه خطاهای ساختاری در نظرسنجی‌هاست؟
بر اساس میانگین نظرسنجی های  RealClearPolling، دموکرات‌ها در رقابت سراسری برای مجلس نمایندگان با اختلاف قابل‌توجهی از جمهوری‌خواهان پیش هستند؛ به‌طوری‌که سهم آن‌ها از رأی عمومی کنگره ۴۹.۸ درصد، در برابر ۴۱.۹ درصد برای جمهوری‌خواهان برآورد شده است. مؤسسه Cook Political Report نیز پیش‌بینی می‌کند دموکرات‌ها بتوانند بین ۹ تا ۱۹ کرسی به دست آورند؛ نتیجه‌ای که احتمال بازپس‌گیری اکثریت مجلس نمایندگان را تقویت می‌کند.
در سنا نیز شرایط برای جمهوری‌خواهان چندان مطلوب نیست. برآوردهای کوک از احتمال کسب خالص 2 تا 6 کرسی توسط دموکرات‌ها حکایت دارد. دموکرات‌ها برای کنترل سنا به 4 کرسی بیشتر نیاز دارند و رقابت در برخی ایالت‌ها، از جمله کانزاس، اکنون بسیار نزدیک ارزیابی می‌شود. هم‌زمان، محبوبیت دونالد ترامپ نیز تحت فشار قرار دارد. بر اساس شاخص نظرسنجی‌های کوک، میزان تأیید عملکرد رئیس‌جمهور حدود ۳۷.۶ درصد است. در نظرسنجی اخیر اکونومیست و YouGov نیز تنها ۳۵ درصد از پاسخ‌دهندگان عملکرد او را تأیید کرده‌اند، در حالی که ۶۰ درصد نظر مخالف داشته‌اند.
با وجود این داده‌ها، نمی‌توان نتیجه انتخابات را از هم‌اکنون قطعی دانست. سابقه نظرسنجی‌ها نشان می‌دهد که برآورد حمایت از ترامپ در انتخابات ریاست‌جمهوری سال‌های ۲۰۱۶، ۲۰۲۰ و ۲۰۲۴ با خطا همراه بوده و میزان آرای او کمتر از واقعیت تخمین زده شده است. هرچند نظرسنجی‌های انتخابات میان‌دوره‌ای معمولاً عملکرد دقیق‌تری داشته‌اند، در انتخابات ۲۰۲۲ نیز برخی مؤسسات حمایت جمهوری‌خواهان را کمتر از میزان واقعی برآورد کردند.
یکی از مهم‌ترین مشکلات فعلی، کاهش نرخ مشارکت در نظرسنجی‌هاست. شواهد پژوهشی نشان می‌دهد جمهوری‌خواهان تا حدودی کمتر از دموکرات‌ها در نظرسنجی‌های تلفنی شرکت می‌کنند. بنابراین، نمونه‌های آماری ممکن است بیش از اندازه تحت تأثیر دیدگاه‌های رأی‌دهندگان دموکرات قرار بگیرند.
نظرسنجی‌گران برای حل این مشکل، از روش‌هایی مانند افزایش وزن آماری پاسخ‌های جمهوری‌خواهان و تنظیم نمونه‌ها بر اساس ویژگی‌های جمعیتی رأی‌دهندگان استفاده می‌کنند. با این حال، این روش‌ها نیز بدون ریسک نیستند؛ زیرا فرض می‌کنند افرادی که به نظرسنجی پاسخ می‌دهند، از نظر رفتار انتخاباتی نماینده مناسبی برای کسانی هستند که پاسخ نمی‌دهند.
بنابراین چنین می توان گفت که در شرایط فعلی، احتمال از دست رفتن اکثریت مجلس نمایندگان برای جمهوری‌خواهان جدی است و وضعیت سنا نیز می‌تواند به سود دموکرات‌ها تغییر کند. با این حال، سابقه خطاهای نظرسنجی و دشواری نمونه‌گیری از رأی‌دهندگان ترامپ، عدم قطعیت قابل‌توجهی ایجاد می‌کند. برای بازارهای مالی، نتیجه این انتخابات می‌تواند بر مسیر سیاست‌گذاری اقتصادی، مالیات، بودجه، تجارت و روابط خارجی آمریکا اثر بگذارد؛ اما تا زمانی که داده‌های معتبرتر و نتایج انتخاباتی در دسترس قرار نگیرند، نباید سناریوی پیروزی دموکرات‌ها را قطعی تلقی کرد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/21606" target="_blank">📅 21:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در ابرقدرت چهارم جهان؛  — برق به دلیل ناترازی در گرمای تابستان قطع می شود  — گاز به دلیل ناترازی در سرمای زمستان قطع می شود  — اینترنت هم هر بار یک شلوغی یا جنگی بشود توسط خود سران ابرقدرت قطع می شود!</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/21605" target="_blank">📅 21:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر ارتباطات:  در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال 90 درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/21604" target="_blank">📅 21:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر ارتباطات:
در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال
90
درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/21603" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/21602" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اسرائیل هایوم:
اطلاعاتی که سازمان‌های اطلاعاتی آمریکا در اختیار دارند، نشان می‌دهد که ایران با وجود ماه‌ها بمباران توسط آمریکا و اسرائیل، موفق شده است بیشتر تأسیسات تولید موشک و پهپاد خود را حفظ کند.
به گفته یک مقام ارشد نظامی آمریکایی که با جزئیات این موضوع آشنا است، ایران همچنان به خوبی مجهز به موشک‌های بالستیک، پهپادها و سلاح‌های ضدکشتی است و می‌تواند به سرعت ذخایر خود را دوباره پر کند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21601" target="_blank">📅 19:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد    گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21600" target="_blank">📅 17:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد    گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21599" target="_blank">📅 17:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد
گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21598" target="_blank">📅 17:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چه کسانی از خرابکاری در اهداف انرژی سوریه سود می‌برند؟
همان‌طور که سوریه خود را به عنوان یک مسیر بالقوه برای جریان نفت عراقی و گاز منطقه‌ای به سمت مدیترانه معرفی می‌کند، یک زنجیره از حملات مرموز زیرساخت‌های انرژی آن را هدف قرار داده است.
در ۱۸ اوت، یک انفجار پمپاژ گاز را از کارخانه ای در حسکه متوقف کرد
در ۲۸ سپتامبر، یک انفجار دیگر به خط لوله ای در دیرالزور ضربه زد
در ۳۰ سپتامبر، یک انفجار نیروگاه‌های تشرین، دیرعلی و الناصریه را از مدار خارج کرد
این حملات با تلاش سوریه برای گسترش لوله‌کشی گاز عربی همزمان است - بخشی که به تازگی در الفرقلوس افتتاح شده ظرفیت را به سمت ۱۱ میلیون متر مکعب در روز افزایش می‌دهد - و نیز احیای مسیر نفت کرکوک—بنیاس.
چنین مسیرهایی می‌توانند جایگزین‌هایی برای تنگه هرمز ارائه دهند، مسیر مستقیمی به بازارهای اروپا باز کنند و هزینه‌های ترانزیت را کاهش دهند
این مسیرها با صادرات گاز اسرائیل از لویاتان، تامار و کاریش رقابت خواهند کرد
اسرائیل، که از سقوط اسد حملاتش به خاک سوریه را افزایش داده است، از یک دولت سوری ضعیف‌تر سود می‌برد.
ایران هم از این جهت که جایگزینی برای اهرم فشارش در هرمز دشوارتر می‌شود از ناامنی در خطوط انرژی سوریه بهره مند می شود
باقی‌مانده‌های داعش با توجه به حملات گذشته به زیرساخت‌ها، یک احتمال دیگر هستند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21597" target="_blank">📅 14:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21596" target="_blank">📅 14:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز گزارش داد که مقامات در تایوان می‌گویند معتقدند چین در حال تمرین برای یک محاصره دریایی احتمالی با استفاده از دارایی‌های نظامی، شبه‌نظامی و غیرنظامی متداخل است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21595" target="_blank">📅 11:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚪️
کاخ سفید دسترسی مایکروسافت به ویزای کار دائم را قطع کرد
دولت ترامپ دسترسی مایکروسافت به سازوکار ویزای کار دائم آمریکا را به‌دلیل سوءاستفاده از برنامه‌ی نیروی کار خارجی مسدود کرد. ادوبی، کاگنیزنت و اینفوسیس نیز در فهرست تعلیق قرار گرفته‌اند.
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، مایکروسافت را متهم کرد که بیش از هر مجموعه‌ی دیگری از روزنه‌های قانونی بهره برده است. کیت ساندرلینگ، وزیر کار، اعلام کرد مایکروسافت و ادوبی در مجموع نزدیک به سه میلیون درخواست استخدام خارجی ثبت کرده‌اند که به تأیید بیش از ۲۳۰ هزار ویزای H-1B و صدور بیش از ۱۰۰ هزار گرین‌کارت انجامید.
مایکروسافت در پاسخ گفت حدود ۸۰ درصد از ۶ هزار پرونده‌ی H-1B سال مالی اخیر برای تمدید اقامت یا اصلاح وضعیت کارکنان فعلی بوده و تنها یک درصد از بدنه‌ی استخدامی این شرکت در آمریکا را نیروهای تازه‌وارد تشکیل می‌دهند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21594" target="_blank">📅 10:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔸
قطعات حساس جنگنده F-۳۵ به چین رسید
🔹
اشتباه یکی از کارکنان شرکت پستی UPS موجب شد که قطعات حساس جنگنده F-۳۵ به جای آمریکا، در هنگ‌کنگ و در اختیار دولت چین قرار گیرد. این محموله شامل پوشش شفاف کابین خلبان با فناوری کاهش بازتاب امواج راداری بود که نباید هرگز به دست چین می‌رسید
🔹
کارمند مذکور ایمیل هشدار مربوط به محدودیت‌های حمل این محموله را نادیده گرفت و مسیر انتقال دو قطعه را تغییر داد. پنتاگون این قطعات را «غیرقابل‌استفاده» توصیف کرده و برای بازپس‌گیری آن‌ها با شرکای صنعتی همکاری می‌کند. پس از انتشار این گزارش بلومبرگ، ارزش سهام UPS کمتر از یک درصد کاهش یافت</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21593" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زرادخانه موشکی ایران ممکن است شامل سیستم‌های پرتاب سرد باشد
سیستم‌های پرتاب سرد در اصل موشک را از یک کانتینر پرتاب خارج می‌کنند، پیش از آنکه موتور موشک روشن شود و به سمت هدف مورد نظر حرکت کند.
شایعات و ادعاهایی مبنی بر دستیابی ایران به این فناوری از تابستان امسال در شبکه‌های اجتماعی در گردش بوده و در روزهای اخیر شتاب تازه‌ای گرفته است.
با این حال، منتقدان ایران اصرار دارند که این گزارش‌ها عمدتاً توسط طرفداران ایران پخش می‌شوند و از تأیید مستقل برخوردار نیستند؛ که با توجه به بی‌میلی آشکار ارتش ایران به ارائه داده‌هایی درباره توانایی‌های واقعی خود به دشمنانش، چندان غریب نیست.
اوایل این هفته، سرهنگ‌کل محمد اکرمی‌نیا، سخنگوی ارتش ایران، اعلام کرد که تسلیحات پهپادی و موشکی ایران از ابتدای تهاجم آمریکا و اسرائیل پیشرفته‌تر شده است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21592" target="_blank">📅 09:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرواز انبوه هواپیماهای ترابری نظامی آمریکا به خاورمیانه</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21591" target="_blank">📅 09:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from(تحلیل نظامی و اخبار جنگ) MilitaryToday.IR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGL3TYxQTCsYlIPOfW1dLB1Ddnz6nI3BIkXqE6TPC4Jam0WOhZlhkub_09kqsfSL6D7t9sMiboB4en8DQcKvBdv9rfQwYTca4L7P5cwRmzEOqSalBwKL2kxrDO1hA_gJhskrSD9hl18x3EQHpUo4SOWv0PHUkS9NDa6IZoYGgpWEX3oGITwyq6xi5yy-zDtNv3J9gLK_M4H2RyvBxNoUuhsilaUSRTSBVZaH1eCwJRSXdp2xLFvp1oWhmIc4OrItdVG5Evez5T5yvz6uDD159RMI5-QGrL5GgIwlq_fdhSfR2CXCFP_0Zw9ft36o94FWzJaAEhKIUwxcRd8Izz9fsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
افزایش چشمگیر حملات مسلحانه به نیروهای امنیتی کشور: 12 کشته و زخمی ظرف 24 ساعت (15 تا 16مهرماه) ثبت شده و هنوز بخشی از تلفات احراز نشده است.
Leopard
✍
@MilitarytodayIR</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21590" target="_blank">📅 00:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1s9VVJt9WAz8rLrVMJkTMHNQBhxRoX8iM4bvjTz81jP2-5AzvsyFe3in1Gjdd6jVTi0P0m9kR8_xlGSU5Ac_hdcAj867sY7WtsvMSMsez-1C7B0c3Fzx0QBTS7yRNZUhMkzFWchZpAPOww4aPUsFPo0zhNqmxTZ-7FTGgPz2vIYExyGHh8kJRQvRysLDZ7mIKgtDdRyR6hEX_wF_OkOjXaJSFhfN8ISCjAtR5dP4O1mpYksG1Y5qEoua9o9h29JlSBPLXzvvw39jVxQwlxggMFBFtbgX46nL54EYvDrk-WVCi35LZoCBgl6t_-jEHDZGz5dB_Ugv0zgoZPkzoq6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم عکس تانکری که امروز سپاه منفجر کرد
به نظر می‌رسد گاز قطر را حمل می کرده</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21589" target="_blank">📅 00:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قشنگ آدم حس می‌کند یک مشت مافیا با هم نشسته اند خلایق را از جانفدا تا جانفنا بازی می‌دهند !</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21588" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21587" target="_blank">📅 00:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwDhWWWLpgHdK-bO6Vy0TF8F14eAAg1XO6b-qkMiBMSfXf7Re3n4dd6VMhwd0BKTaLl5bZ7uaukLMJEtqH9pVJtpo1oOcKdIjcZKVoqdW_GOjuuEZHi_gZfuP99Xf7Aqd73S-m4NBI22Qv3NW4dGA_QtszuM1Wa_jfFpRIYIh5yJS9yFujRwek6RvqLRPS86BIf377iFOct2lchw1sv4tvGayEacBYWUm8eVYFyoiyDtKJ7ayOeLj7HYbUVnJVLD-X9r1uT07FxMIRyCKU8CaDc64GtS6FIBJn0QdWiS59b5KAM4W_ugzK7Y3rhKK3gXshTbq-be1IT7Xgg2fP5z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی با کمک هوش مصنوعی از حرکت اخیر روسیه</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21586" target="_blank">📅 00:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چه بازی شد….
طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21585" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله حوثی ها به تاسیسات نفتی عربستان</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21582" target="_blank">📅 20:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خلبان یک هواپیمای خطوط هوایی سعودی دیروز در اثر حمله نیروهای حوثی به یک هواپیمای مسافربری که در فرودگاه ریاض پارک شده بود، کشته شد.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21581" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">افراد مسلح یک خودروی هایلوکس حامل نیروهای نظامی را در منطقه چشم‌زیارت زاهدان هدف قرار داده‌اند. پس از این حمله، نیروهای نظامی و انتظامی به محل اعزام شده و گزارش‌هایی از ادامه درگیری و پرواز یک بالگرد نظامی منتشر شده است.
تاکنون آمار رسمی از کشته‌ها و زخمی‌ها منتشر نشده است.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/21580" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AejvHYMfSmBLXVO64HmcWOvg_Chk_1AHABhNqU4ae5f1R5VTTz8UI5mCLeGCduql3dJbsPFyEnkwT31JI1QQ6uubyzgeIaxN5vnmUKts-NGt8b7Ql1A9VM-th1clyiq7kVKWw6sbN0-E9Z2F88YMVteO4D2_E5sdWaUZPUmblrs8fDgf3JXo1HP17tEL7HFrWFYBVBdtG5YC8tJSyr30lxP4tN7w7E2am_eCJkatGZ6m8XY4izAUj8YIGj0RTaVBYHuKmD9YyGYXOG9VsEL3hhFeI4BhFdytUej1l8o3PLY4xRZjPCJBNdyiHtYKD2O9tWHkpu9aVtUXKEpCXTO70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای بازار سرمایه و ایران.
کسب مقام نخست مصرف تریاک در میان تمام کشورهای دنیا رو بهتون تبریک میگیم.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21579" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8OrTYQmPz_zv06Sf95fNqDsNEJFB_98-rEoxaQk7YR37jH-pBOAgGAxYGxNa9SzOfDJcCOos9ZLS7gl9p_uzgcZqUQq3QeFh9PMUE1IwXqb73LnRPSWEILZiNJZK_ctJ1pxNbI-usuFYDAc5stio30NiN3mK6JxT485Frul1NHnq6ia0dNPKJsnk6nWLhRRKRMaF_hp1GTYVbhE_oCcsL918q4sqDM1nibQ786wMR_vEFEuwcy6QyXYD9flUMm_2EexVaJ_3ZqkdbWnk3YdcfCKy6TwfSWc6HhVatYcVflQFMgUGorDQL2x91aqvTvU8C8M30yJN_gn7d_5CvbUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21578" target="_blank">📅 11:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAIF57QBcxQ5fVexvv30-2ivurxpAaP1YebKE4-n25nNv9q8oCR-Q1_8rWjbeR0Jzc1uKOU8vT_6pMMWxEFChG-VQvnH3gzrFI76lNBz7q16BN_opU_h9lWxExUcux32vFT1xqbXiDByjbuqX_cH0Rzue7-vHtF2KXimtJkQW_Ni0CqD3lRktCFMSDrjFxWl-o7LA7S3qk_VesZNJOlGMIyHGUJAdkPshcPUkBYKT9qndnye7o0vzjHFLo0zteQrhq7DiFY4xrnI15gm33eKLmX6Xqo6ZyoXJbnLDpQ_SuORR5VPwO5Zho18RkMkiw3IPKn_Utw147lyKnhAcrxDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC با رشد سنگین طلا به محدوده میانه نوار ارزش منصفانه رسیده و ارزندگی خاصی نشان نمی دهد.  در چنین شرایطی بهترین راهبرد، انتظار برای یک اصلاح «عمیق» و سپس خرید است.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21577" target="_blank">📅 10:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff8ajtybZ9eaGPwETOa_ryzVIDXSZ3qN4Pu0W9hWxq0O5gXTyUhOd_Srq1NAKBcRUsoRoE6zYv173TA0X5mjUeKQT63hqzyykzfveTT05mwVKTo8w4wVie-2UfeM1c5ljQ1xUTdH_-9UfqPazS1n-AnZ01wSPKcnIeC3bbIyVtfm-jRb8aXG1rOpevi4QW1_PDGNfhEwfxtxENo-QbZN3nsM8n89w9dSNU2HlnrIIdiljb_tRrBoHi8P-VLz04ZNqzWrFhkiR_uILDxcIYmGukmOmjURG_U1UCbCEl7JZHWU9HVDFrghfVew9rAsJWtQ7IKJwF4cop_jg4x4CzvPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC با رشد سنگین طلا به محدوده میانه نوار ارزش منصفانه رسیده و ارزندگی خاصی نشان نمی دهد.
در چنین شرایطی بهترین راهبرد، انتظار برای یک اصلاح «عمیق» و سپس خرید است.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21576" target="_blank">📅 10:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZNiJagn5Nn2RZbYVqWaGGzhVD41MRwSwyatqK-gFsQNRm3wcQgGjYPUdrOpI-OGbj250YZMzryQUDBzJebVZEtnJ7M901nGjwamMPxHgJi2LO1LLYMYe3SmAujfYKvxuKJ1rWU8pPoVUNxmq75zvgn488on501Hive4SJvC2WOejMx899ju9gox4yObWb8X6egq9NZw41Sy9806LOb9n1G086ZdacjfWlgBHvXXnVTw3tjuoU-Bswfl4a4qXI0If-p13UpptwVKGoTEDqWeRreXO_6A0zXGMNrf_n2290Lksg5vTyLVLZkdF_JMpRnIVLek1CI1Md1FRX-UlP2p0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی + تقویم اقتصادی برای امروز در سطح نسبتاً پایینی قرار دارد اما رشد سنگین طلا عملاً این مسئله را پیشخور کرده است.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21575" target="_blank">📅 10:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21574" target="_blank">📅 10:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
کره شمالی هزاران نفر را با هویت‌های جعلی آمریکایی وارد شرکت‌های فناوری آمریکا می‌کند تا از راه دور کار کنند
این افراد با کمک هوش مصنوعی در مصاحبه‌ها و تهیه رزومه تقلب می‌کنند، گاهی هم‌زمان چند شغل دارند و بخش بزرگی از درآمدشان را به کره شمالی می‌فرستند.
این شبکه می‌تواند سالانه تا ۸۰۰ میلیون دلار درآمد داشته باشد و بخشی از پول آن به برنامه‌های تسلیحاتی کره شمالی می‌رسد.
علاوه بر درآمدزایی، دسترسی این افراد به سیستم‌ها و اطلاعات شرکت‌ها می‌تواند خطر امنیتی هم ایجاد کند.
﻿</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21573" target="_blank">📅 09:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پنتاگون طرح ۳ روزه حمله به ایران را تدوین کرده است
بر اساس گزارش نیویورک تایمز، ارتش ایالات متحده گزینه‌هایی برای یک کارزار کوتاه و شدید علیه ایران با مدت حدود ۳ روز آماده کرده است؛ این حملات به سمت مخازن پهپاد و موشک ایران، تأسیسات انرژی و سایر مراکز نظامی هدف قرار خواهند گرفت.
طبق این گزارش، تیم ترامپ قبلاً ۵ پیشنهاد برای عملیات‌های بزرگ علیه ایران یا حوثی‌ها ارائه کرده است. ترامپ اکنون پس از یک جلسه با مقامات ارشد امنیت ملی که توسط نایب رئیس‌جمهور ونس در کمپ دیوید رهبری شد، در حال بررسی پیشنهاد ششم است.</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21572" target="_blank">📅 01:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: من هرگز ایران را برای بمباران لس‌آنجلس دعوت نکردم، رسانه‌های جعلی این را ساختند
او در تروث سوشال، «اخبار جعلی و مصنوعی» را متهم کرد که سعی دارند بگویند او «دشمن را برای بمباران سن دیگو» و لس‌آنجلس دعوت می‌کند. به گفته او، او فقط می‌گفت که پرداخت کمی بیشتر برای بنزین برای مدت کوتاهی، بهایی کوچک برای جلوگیری از دستیابی ایران به سلاح هسته‌ای است. او توضیح داد که قیمت بزرگ، بمباران سن دیگو یا لس‌آنجلس توسط ایران خواهد بود.
این چیزی است که او واقعاً در یک تجمع در نبراسکا در روز دوشنبه، در مقابل دوربین گفت:
«پرداختن آن قیمت کوچکی است. آن‌ها می‌توانند یک شهر را نابود کنند. بگذارید لس‌آنجلس را نابود کنند، بگذارید سن دیگو را نابود کنند.»
که پس از آن گفت: «قیمتی بسیار کوچک برای پرداختن.»</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21571" target="_blank">📅 01:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ستوان سوم وحید عنایت از نیروی انتظامی امروز توسط شبه نظامی‌های تکفیری در سیستان و بلوچستان به شهادت رسید</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21570" target="_blank">📅 22:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همان گفتاردرمانی همیشگی ترامپ است. به نظر من هیچ گفتگوی جدی در حال حاضر جریان ندارد و همانطور که خود ترامپ می گوید، فقط زمان حملات آنها شاید به تعویق بیفتد.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21569" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:  ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم و تا پیش از برگزاری انتخابات میان‌دوره‌ای، به هیچ وجه به ایران حمله نخواهیم کرد؛!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21568" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um99s99Qd1v8X_kfIix7mAXWUAwSVOK8o02lNk4iiPGtZAWE_eTj6SqysT-f6WLBNd8IML0DN3utGMV3gL3BtAIZ3tWKt30ZWtb0Nr_kTCFrcmMcOtrOcihQfSp5sse9ygOZt0bZhFpVyZZZX1OggP8txGF79xaBny4h8SZyZsQnDMFRPCi2TZhWshWlhc2EmEJ8LZex9Pnbe2jPaGaSaBmF-yiM9jcRfWaupJOu6E7iWshFkET45gmWwLyAiIZ9hYkI8_IS4uVBzB590Q8kWnqR09ygbB7DBeYMt4-_APQsF06hr5SjMqx0ICcZDjM15Ac9owM4kgkHRX7PAZVvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش کانال 14 اسرائیل، مقامات ارشد سپاه پاسداران انقلاب اسلامی خواستار حمله به اهداف مهم در منطقه طی 3 هفته آینده شده‌اند. آن‌ها معتقدند که ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21567" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خیلی شبیه هم بود این 2 خبر که ولی خب</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21566" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21565" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21564" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21563" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZvyOC46djjqSejLd_fyhb9hzIYh1xKe1QDRC62cl2lRwNTtyRqRiDv5_BJzcP-HFG2D288AFXt9ZtzlUjdDojoUGEX9SoYlkL2jOYBqFDhmLJTt34BMrLC7W1ZmnToVdGIZIDOlvgRUlJs7HuzrpYlFoAh8O6W8TxJ01y3EuUfp2lSfw-L0CJQ_urcCMdEM9Ol1YhRmOpQpQu920QEsecbrWhHcSqq8NwRwsmr8wA6MqUIWmE4pFH5pK6Ro_-HzOk_-s4d4Le-ytaPtX5DPm_YsMtRvkkxDu2u6cffUNzSnVifXYcattH59s8CmgX9C3u4bM4h5YZN990MFpFB5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21562" target="_blank">📅 19:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8AmJPgT9zekTHnVzCbdzzfefIib3Kw5uQTG0QI57d5-mTc5EcGQuCoK507QID25cXve_HKR_UqBHVcn5vcfS9sYyGM6Vn4W84KsahO6jqw8wgzj7XmumG1IZJEXl6n4OBsLpthOGQCZeIdiPimsf_ds1VilPCq_n29SSfehCAGyQoq15yUHWyhBwh_KrV21DeKxWJ38GnuchEspRzNbAWFcLwrcjQxLJXbSOuLRvNOXV5rnlKIdkfCM7ZX-CoWoGXFZszCJUclItWbxrXr8aiB7Imk26LU2vPjEkIvaBWHjdQM4nvWkj9EYPojkxifs2xFMJsWnvq4p5__QGXp1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21561" target="_blank">📅 19:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21560" target="_blank">📅 19:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKmekhAIK8yvdoSmA1Wj-ixtwN9cFYPNQKU021hBANqPspFxzwTXNlHiXcalRYccarn8dPc4BH5-uWN85J_BemaUMfqQeiCU8RKLRnW9xNAJsK2P8blQA_Eu1dpCazxtXSoba2ciUjMN7QSVgvCBPeX3GPnQ0Wvwm121HAyZN6ZcimPvv-n7ls0BeFuEGYbx0H71v1sxobhhpztfzCX5tFGeQJSey1y4A5Q3EOfK1U7OP7rJ0c4_o5JSR_hLl7OrjvRQvKdyV98fJkP4_JAHQVnC81MXA-XpC1mRiIR9u4n67iddA7wMGcD1XytObJAxxsM8nAGu0clfREdWn-nz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21559" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بر اثر برخورد صاعقه به یک هواپیمای هندی، دماغه‌ی هواپیما آسیب دید.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21558" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcSPfc1EhDT9T0Gm2HZ78c8cVNq28Zsev-gUitCtU8J_PnVfIXVnyIs2DEbOVnF3m6XLAreQCuxNjYjDErbpynYRwzpBZZSMPijFv9MjgKyrnBdpfGrygIHcJWHpxGE60QQvNwDT1_Zyf-_3xgrdbZe74x7SHYuvd6DM2paZ4iqibfKhp6Gohg2wX9v-8lXVWBhgydJeWgSqVWZ5e5d24zo0K3AvGWjBW7HPh0SThkiuT1rqsL1IPF2vePldcAFchzsgk6-4AyJ236u5VGZMuTu9lCDTqe4cAuNyS3IrC_T92KfNNayKKYWQzIeq2yPcXlH8qdrQb-OIR8imWwJJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21557" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21556" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21555" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS3rOQ1iQ0tpBOrtfrt4IUHvpnE1S1pdit9_7xqp4Up5SNHmTPV62s4JtC-BN3Cxg7p91vyYvp97gcPoHO9XwMcUHqkCrYwG63nx9UDAFhxbMXRDrbP7VPbf0Fzghv2dUInrDYY_JfaJQEg43DwTNeY0LJJB_lH9DE3zUDSlzf9zeLPaf_BzFjTcxN8M0mtxdUWbUJzcDr9pkQz336OvFutWB9PBGXBILqG4UjafB9nXsL_UcOEsU_j7eBJWtMaBwY2xQV_14IkHvRcIF2ZzAL0QhKyi0qk4UqunlSEppE7A7NJhGpD7ysJVj94k8-PWoSg_QebvbKPAUULmDDOaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک هرمز؛ آیا جهان در آستانه یک بحران اقتصادی جدید قرار دارد؟!
شوک هرمز با افزایش قیمت نفت می‌تواند تورم جهانی را دوباره تشدید کرده و بانک‌های مرکزی را به حفظ یا افزایش نرخ بهره وادار کند.
تداوم نفت بالای ۱۰۰ دلار می‌تواند هم‌زمان با رشد ضعیف‌تر، سرمایه‌گذاری کمتر و هزینه استقراض بالاتر، ریسک رکود تورمی را افزایش دهد.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21554" target="_blank">📅 15:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر    در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21553" target="_blank">📅 13:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صحبت های یک استاد دانشگاه امام صادق درباره اینکه چرا فقط تنگه هرمز برای جمهوری اسلامی به عنوان ابزار فشار باقی مانده است</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21552" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21551" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر
در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21550" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmQQJ1N4k0XNcCHmVn_bKMNcPkiSiPUGpcnaD3WRSyMg_PuYL5OyCtsYiTjtqwQ-hGNj4fQTKo7m-Mi9sZeBZ9SU0j3QLCCitaMpOGUrAUVkJVXD5KEDnwTQAREp8ijiiQQC_huE0l5SyBQutKon44dA5BYqevOKGDKsFjGkog0mpm9XnlZyIcIpew5m4a8jhkeeb8jTP6ERqwOM4QYTzIJppB80IjJ4N_lOcJaHyaEAmNdAWl3xsg2tBl2UUpDGJUOUVh7TIR2l2eFfiOr66cGgzYpT2ozxaOXLROlXLU2twbSKyqKUAfEwNlEJPeojTP-QeW2XBlqJhTv4vREJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21549" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXRPb92hVajrfccnC0i23YnA5rF0clcT7b_B5F9ixr7EuV9IPEAqr-W2RwmsBdvxlJJk6AfM8OSmTGV2x5QOK7SN9Npp5_Re15mWddrP3qGHNJc06QHl7gGoo3zp1qjPAW5BnpfnaWpnMTGGnk-7t7RpEFZCGxvTCRVKpk-3Fqp8DPLQOKMlYzqWBXYQ4P42pJR7CITwRPBWEnV6hmZ6N6sHVDxnGQOZ4IjV-PgFNx42bnDS5oka5DDPQuBNhWzmG01g1EiJ1KdXf1f6C5eXFhFH2AZc4bvqTo3Y2NITpiqBGlguKRhZDoTb9TR9ZSzQEz-y8-x61dqFBEjRkDQr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده بیش—فروش قرار دارد و خرید در حمایت ها منطقی ترین گزینه است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21548" target="_blank">📅 10:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2fKhYLDKhMoiTixn7x5fWpyqsgXzH3NT2W3_-IPcTPRsjcjz4Ihe7W5aO6d9IDFxZH5LwraRetfvnheWt1-Fi8W7tl5HXi5KIr0vd9vv1TcixDkSmDUY932BbNBigsNIsOIWN8B2HC9XtiqPbhaQ4C5f3eZCQNkiYWPIyNloJKsMKYmqr3NDYgpl-ci07l0bDdgPetWotKtkpyeIsvI95k8ziRf6Id-y23IzLSuO2mFwDgKc6lXvyStBiLvmcARyy6-zr-VysKBTctNEQ2BkIrbFVvPY6zVmc3XPmL4phITvVRTZ-D5dyVJxJfVxUwnRfufRG01kJlCjQLRtL6cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در حمایت ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21547" target="_blank">📅 10:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.
ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر رخ دهد.
یک تهاجم جدید می‌تواند شامل حملات گسترده ایالات متحده و اسرائیل به زیرساخت‌های انرژی و تأسیسات هسته‌ای ایران باشد که احتمالاً منجر به تلافی موشکی ایران و افزایش قیمت نفت خواهد شد.
مذاکرات هسته‌ای ایالات متحده و ایران همچنان متوقف است، در حالی که ترامپ و نتانیاهو، نخست‌وزیر اسرائیل، در روزهای اخیر دو بار تلفنی با یکدیگر گفتگو کرده‌اند.
مقامات اسرائیلی معتقدند احتمال حملات پس از انتخابات میان‌دوره‌ای بیشتر است، اگرچه حمله زودهنگام همچنان ممکن است.
— آکسیوس</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21546" target="_blank">📅 09:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران،  بقایی:
عمان با ایران بر روی مختصات جغرافیایی مسیرهای امن عبور از تنگه هرمز و نحوه ارائه این توافق به صورت بین‌المللی به توافق رسیدند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21545" target="_blank">📅 00:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایران، حفر و توسعه را در یکی از بزرگترین پروژه‌های غیرفعال خود، مجتمع زیرزمینی آبیک که توسط سازمان‌های اطلاعاتی غربی و اسرائیلی با نام رمز "سایت 311" شناخته می‌شود، از سر گرفته است.
این سایت در امتداد محور تهران-قزوین، در حدود 100 کیلومتری تهران واقع شده است. این مجموعه در دل کوه‌ها حفر شده و شامل چندین ورودی تونل است که احتمالاً به یک شبکه گسترده زیرزمینی شامل ده‌ها سالن و پناهگاه متصل می‌شود؛ این مجموعه یکی از بزرگترین پروژه‌های از این نوع در ایران است.
تصاویر ماهواره‌ای نشان می‌دهند که این یک پروژه بزرگ است، با حجم زیادی از خاک و سنگ‌های حفر شده، زیرساخت‌های پشتیبانی و پوشش سنگی قابل توجهی که از تأسیسات داخل کوه محافظت می‌کند.
بیشتر کارهای حفاری در این سایت بین سال‌های 2007 و 2016 انجام شد. پس از آن، به دلایل نامعلومی، کارها عملاً متوقف شد.
با این حال، بلافاصله پس از عملیات "خشم حماسی"، تصاویر ماهواره‌ای نشان دادند که تغییری آشکار رخ داده است: ایران به این پروژه بازگشته و با سرعتی که در طول حدود یک دهه در این سایت مشاهده نشده بود، حفاری را از سر گرفته است.
این سایت در سال 2010 توجه بین‌المللی را به خود جلب کرد، زمانی که از آن به عنوان یک مرکز مخفی غنی‌سازی اورانیوم نام برده شد. این ادعا هرگز به طور مستقل تأیید نشد و هنوز هیچ مدرک قطعی و عمومی وجود ندارد که نشان دهد غنی‌سازی اورانیوم در این سایت انجام شده است. هدف دقیق آن هنوز نامشخص است.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21543" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21542" target="_blank">📅 23:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قرمساق کاکولد با بهترین تجهیزات آمده نیروی دریایی فرسوده ما را غرق کرده حالا کری می خواند!
پدرسگ اگر شما هم کشتی های ما را نمی زدید خودشان داشتند یکی یکی غرق می شدند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21541" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21540">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیت هگست، وزیر جنگ:  ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.  نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21540" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21539">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.
نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21539" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21538">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">موسسه UKMTO:
گزارش یک حادثه در ۵۱ مایل دریایی شمال مدینه الشمال، قطر دریافت شده است.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21538" target="_blank">📅 23:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21537">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، ایتامار بن‌گویر:
ما خیلی نرم هستیم. این جدل من با نتانیاهو است.
اگر کسی در حالی که پسر من در ارتش خدمت می‌کند، به زندگی او تهدید کند، خانه‌ای که آن شخص از آن بیرون می‌آید را از بین ببرید.
و اگر دختری دارید که سرباز است، می‌خواهم او را محافظت کنم تا حتی یک تار موی سرش آسیب نبیند — بگذارید ۱۰۰۰ تروریست بمیرند.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21537" target="_blank">📅 22:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجار با دلیل نامعلوم در حیفا اسراییل</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/21536" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">— حزب‌الله ماه گذشته ۲۰۰ میلیون دلار از ایران دریافت کرد تا به مردم لبنان که به دلیل جنگ امسال با اسرائیل آواره شده‌اند، کمک کند، با وجود افزایش فشارهای اقتصادی ایالات متحده بر ایران و دشواری‌های فزاینده در انتقال وجوه به این گروه.
واسطه‌هایی که پول را جابه‌جا کردند، کارمزد ۲۰ درصدی دریافت کردند که چهار برابر نرخ معمول است و این امر بازتاب‌دهنده خطرات مرتبط با مدیریت وجوه برای حزب‌الله است.
— رويترز</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21535" target="_blank">📅 19:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به نظرم وقتش رسیده که یک بار دیگر بکشیمش.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21534" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مقام ارشد ایرانی: ایران هرگز حق غنی‌سازی خود را رها نخواهد کرد، اما جزئیات غنی‌سازی می‌تواند بعداً مورد بحث قرار گیرد.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21533" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
‏حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21532" target="_blank">📅 14:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو درباره ایران:
کشورها، حتی آن‌هایی که به ما حمله می‌کنند، به‌صورت پنهانی و پنهانی می‌گویند: «(حکومت ایران) باید سقوط کند. آن‌ها همه ما را خفه کرده‌اند.»
ما اطمینان حاصل خواهیم کرد که آنها سقوط کنند. آن‌ها سقوط خواهند کرد.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21531" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21530" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbQwL25ziE2X5sfIt3xo22HXwCnmttAVBV3ZBMkDke7vs4Ek9MdFdipCPWTKuw4-RFha_auWTbZRlm_z9ybcK5dDHqmCc0mWNRzSGOA_-oMNAihvRRIA-gP78wg2C-7y7O6uQZ8387BnimMCL9x54fveCg5RVaqqz7MoHwahloUnCSvuF14GOvtJzOuIy9h1ygtmddt0ANTIzxcyKnZb1yKknwTUq9MiMUjpIsSiPTvTh45jEUJYwnLHG9HEdXZEM4WAdvcuWIihXMm-2JXUpZWXSq-z0KM0Lk0dq-03qJ3f6xcMwip7gSJSogpVuSDyxi8QzA6ow9FWoHgR1FgEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21529" target="_blank">📅 12:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC9vkdMElQ1VtJPWJu3wLjRc14CCTVQCxJxZhCtkZHwdzb3NKYjoC03WnS8Ux1XIz7mFsP6UfeZkptnvdb1pXeFOJr64o5gP7qY3HD7YK46Cr3vu-SrUgYtyXV5wMMt6Il_NfNkHJT1PdyGAomMpmqYpRzrtbo2ml8eyGvSvv0heJrF5Nq7rau7AP_qS-s4A7iHkYs79yXapJZAp3ooWjmw1P_z87BmnBFiy5zR-Hh0rjt-azGbK65wXD3692Z-XhuNWuucgVXzO0wWMfN3GUa4KIcLJQ-lTClkJs6X52XkqXqNpUbiCKaUr-37yaD4JrgU_4vtRAf8DYCcOg8xQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21528" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSRFDiMUFx1kZTv8HSNqTDr5kCHnT8P4CPsZeLAeX3fyMFgVoWwK7krMILmOqOuDVciaUS7jYS0C_LGqamFNyrLtXLSik9ZBbi1CsnnGA-Xbk4wkMHCU1bQkR8mjc13HzZDaNOF94cLBtDHe8tmjgRfoVE5BuABqFhUDq7Bco2a4qj-rtbb2d6wqPLgvORNNvS9yoWEr9WBizKAWEpn1rIfN70NZnJpUZPNf0dl7XGS-uUbZGdy_BEn7U0G7Q8WxoXGoNHHrjVjB9F7YC-URuqo9RaWC2EYeEwJKetK7Q_qPjETSI7NedPGPnuQXW7NiphIJ-BGYxvuYGwZehFB8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC به محدوده بیش—فروش نزدیک تر شده و این موضوع خرید را قوی تر می کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21527" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-RQEItB0L0xVlSqSwphVIE31XDZwhxoGaSfjTl4zlfsOVq4Idj-TN7wKQ6uuTQaY_U6T_BmfGc71GTUCKwh-B6iNeAYVjwIsDwf9R4TKG3ZV_KMqzVA13MGoRltASVmOYrqSlEZAHn4mjzKiHHfZvT64C1ReXbuShyIH9GRG1nIBDzQmHmo9seCbh3H0-Y7EDec3TynvOuceM02O0qnOb1c9z6O-XL3d5aP4XGzqMMxH-rx5abDT3KgfeFlLFsEEU1ta-qv0n-scs5KBgjoac7W2lA5jI-b7uTn6Q5Gypz-aP3_lo-waQ6ilTQOKBYuK-nsf1qX6OxufJp8U_aMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش طلا تا این لحظه، خرید توصیه می شود.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21526" target="_blank">📅 12:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTd93Mi3aitvQQcM5DQ1SYK_Tg7f1sh3vxBOf9NEkFN3wLiHEwP0fJoDeZ5cGAXJurcjo9L3ZRxo7KuWjPEcK_yu_3X8TwLiMgrzaqL-ItPup4Cd6a2Ta9aDq6uH5vOTmABYjuMMLOg4YXa1e6P9M_7xA28w8wY9NYU9uFAkKOMEdxIP7udJttV2buj-YkHtPu2bqJ9G_-HGCZyEuFVfNZ-acDkbLDnDegER5pkB2looGCWywOjXS88YykRa_LbxbhPOXirr1hjE8pJXbAtTcn44U1TtuIuHIOX2E97ipCvZ5PK2VqZyr2BE6hKwdXyuUvQOy9Doihp81QrLv-LkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21525" target="_blank">📅 11:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ذخایر طلای چین در پایان سپتامبر ۷۷.۴۷ میلیون اونس خالص بود، در حالی که در پایان اوت ۷۶.۷۳ میلیون اونس بود
اما ارزش این ذخایر طلای چین در پایان سپتامبر ۳۲۳.۵۲ میلیارد دلار در مقابل ۳۵۰.۰۸ میلیارد دلار در پایان اوت بود</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21524" target="_blank">📅 09:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تعز به تصرف حوثی ها درآمد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21523" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
اسکات بسنت :
ایران وزیر نفت جدیدی انتخاب کرده،
با توجه به اینکه آنها از 25 آگوست حتی یک بشکه نفت هم برای صادرات بارگیری نکرده اند، این وزیر جدید عملاً چه چیزی را مدیریت می کند؟!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21522" target="_blank">📅 08:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKiTQq9UzDcIYAb5mJzUSa70JrKJLL54enVTu-C4ewIZF1-9op0ZuqM4e_bSy5SMCiaIrCtGLz0qD4rolpDprsbLIWH4TrsEPq7RQnVzanG165mM5DHbafwXRZgOj-CBH94TJtu3tnQbAtdNRJiHTklavsj5mDKf42F8sntDIQLKc_xoEyNImjwr3TrHJ5rUfAagYztlKEFweLwmHjWzco36Qi76adOQrCVdrGz8E-GMSZLtZXfVu5Vx4xAyrrkO4sFEUhqas2IO2FHfgQRs2FrnKL5pqPBDmAkUXnXYZXaEqH_EphmBkmb7-QtZSn-GlguE2VtmnKncOij7oj_TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خب بعد از اینکه به بسنت این را فهماندیم، دلار 40 هزار تومان کشید بالا که مهم نیست چون مهم این است که ما مجبور نشویم بکشیم پایین.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21521" target="_blank">📅 08:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21520" target="_blank">📅 07:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این مدلی بوده که اردوغان تروریست های جهادی ترکمن سوریه را که تحت فرماندهی «تیپ سلطان سلیمان شاه» قرار داشته اند به جبهه های جنگ قراباغ اعزام کرده است.  پس از ورود نیروهای سوری به جمهوری آذربایجان، در جلساتی با حضور رهبر تروریست های سوری و نیروهای نظامی ترکیه…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21519" target="_blank">📅 07:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آماده‌سازی‌ها برای جنگ میان اسرائیل و ترک‌ها با شدت تمام در جریان است Damir Nazarov  پس از به‌رسمیت‌شناختن سومالی‌لند از سوی اسرائیل، تحلیلگران این اقدام را تلاش نتانیاهو برای ایجاد پایگاهی در برابر انصارالله یمن و کسب اهرم فشار در دریای سرخ ارزیابی کردند.…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21518" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خیلی حرف های بد دیگری هم زده که اینجا نمی گذارم.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21517" target="_blank">📅 00:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دونالد ترامپ:  تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21516" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دونالد ترامپ:
تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21515" target="_blank">📅 00:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21513">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کاخ کرملین: رئیس‌جمهور ایران روز جمعه در اجلاس سران کشورهای سابق شوروی که به میزبانی روسیه در ترکمنستان برگزار می‌شود، شرکت خواهد کرد و با پوتین دیدار خواهد داشت.</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SBoxxx/21513" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21512">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SBoxxx/21512" target="_blank">📅 19:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21511">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
آنچه در فرانسه در حال وقوع است، چیزی جز مهاجرت گسترده و بی‌رویه نیست. این موضوع نه مربوط به مدارس است، بلکه مربوط به اسلام است که قصد دارد بر کشوری که قبلاً عالی بود مسلط شود! (رئیس‌جمهور دونالد ترامپ)</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21511" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21510">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فیلم وزارت اطلاعات از ضربات به گروه های تکفیری در سیستان و بلوچستان!
قشنگ خاطرات بازی Counter Strike زنده می شود.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21510" target="_blank">📅 18:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دبیرکل حزب‌الله:   آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21509" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دبیرکل حزب‌الله:
آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21508" target="_blank">📅 18:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21507" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SBoxxx/21506" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های عبری‌زبان در تاریخ ۵ اکتبر، اسرائیل در حال تدارک برای اقدام نظامی احتمالی جدید علیه ایران است؛ اقدامی که ممکن است به‌صورت مشترک با ایالات متحده یا به‌طور مستقل انجام شود.
روزنامه «اسرائیل هیوم» گزارش داد که ارتش اسرائیل ضمن حفظ همکاری‌های نزدیک اطلاعاتی و عملیاتی با ارتش آمریکا، خود را برای حمله احتمالی به جمهوری اسلامی آماده می‌کند. این تدارکات شامل سناریوهایی است که در آن‌ها اسرائیل یا دست به حمله پیش‌دستانه می‌زند و یا به حمله ایران پاسخ می‌دهد.
این گزارش احتمال وقوع حمله اسرائیل یا آمریکا پیش از انتخابات میان‌دوره‌ای ماه نوامبر را نسبتاً پایین ارزیابی کرده و حاکی از آن است که این آمادگی‌های نظامی برای رویارویی احتمالی در زمانی دیگر صورت می‌گیرد.
هم‌زمان، وب‌سایت «والا» گزارش داد که واشنگتن در حال آماده‌سازی برای اعزام نیروها و هواپیماهای بیشتر به اسرائیل در هفته‌های پیش رو است؛ این در حالی است که هم‌اکنون حدود ۳۰۰۰ نیروی نظامی آمریکایی در این کشور مستقر هستند.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21505" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
