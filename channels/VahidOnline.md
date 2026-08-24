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
<img src="https://cdn1.telesco.pe/file/XDCW7bgGHLUQGR5eYbUK6QROVD2HaOXnI0uYqFFARukStzprqT82FWhANGo0g3GxU8f8in-T2savWATigxoTOIJNrX5Isk-7MNpoHwempLCA_kpIuQhBIwpxSsgxbABmyJU13hkr-zLSOrcbKvYMi9r6TcCiK9GdWVwLIias3HVmL1rX_jkQSB1-a-63of2bQ6G2o5c-z-OAoNUiPRzLasLbRRSAJFoO9YbWYyDPaAfw4UOJiJqqHf7MqCo2m8-e4iVNfQvoVfs5900eFGSpztATyQWZ7csaxg5UjLsX7jjf_KGXpDjuqBlzuxo0JyIX0JALAfAoYwLRqJ8hQFfWJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 03:13:02</div>
<hr>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ah2s-2is7j0Djl_10nSNEr5xKWK6XKizjoW8ZJi6VAIjjycHJKOHIVZzQPi30VwsxGRoALB1Re1CCsLSkMEKPpMvADf6X6fAcb6jeVIZFF6i9Ur0VgQo-TdO9uOsGse2Hrr0ObEvDTz9UOtDyKojKJkYAxfUDE508qTnESM-AmzZ4RBot1hU1onYVRjW68wjRgVg1ALuf-L4zXrHmWeXLTuKRXEdBQbE_zy8f4C8excGW9PshiTd8m2ORgBgMntdFXtgko7znWdNTKMVomUFsi955xjAFhRDZpdXH4HBEwQ-luXEbwrvX6BDMBvYjih5bEqo5g0fp3RHMC2sPZZLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LQN1_xEPEQiaNutxcTCMW5YQWgJagPXl76rN7qXnmvUhUqzp3UWH3Z6gtQFbcF5Arp3M2DxWVUVbxJE9AY2c_OzM96uUk0Jnuo7D48rCpPFq1-TDflIYls1MqBpDEsDaUy4qXcnBhB4_RevB2drHEtOt8oDaBknKeY70oPGHzkeHYXw7osXjfthylQp5xKLuAWoAejayf8hpd41ot9vkD5pxaoGBuNfM0eP0sevDvD8vhSEjpH-In-F26Wp9unvF_nPg6epSb7lhMW8331HR6_X5arn2T7TJneB0kEFl0fzkD87z5Shv8xxFRHl3QOZu5KlppymLzJm-Kpv9FPzZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rv1C_78KgXy4FUYYDnZ6cHpBxtgHlOQy3d3ifpfBjsB0sLktSxX6K2xdBvil-IgGmSQIG4sqLNv30fGbPthDq7KqoQhpSllK3xAjHJe-ettCwOPqOIOUP548PEErXzspN3cxhgOduSYiD0nKtQIQVTfyTUt1KtQlR__sVdnv1AdY_Xf0T_HmJW6rix1ZhRtnz_whU3z4gD_5mHtMLFqVTtTVG46fKA97oHfljsHecV9WTBXDeSZcgktX6gMp2GZvPvBSLw7IW3i2uJVrQb6N6YrAnK3vYUPZ8rfRu8AODAX5W0IcBaq9WQKINYZVSVd4loEjpQl06gc_FBUlKAhgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bV1i9Prx0qzscVFY7EZXo7slSG0j6YMZrmIe4cD9OOiDaUDY9dZEKU3VUUgu5AHGWV7hz2QCVg7pXoi09zkELRcFlVZkz0f3raWeJL92FPRj_XCWraoEeq4SB38K54feE36brjUVqb_qFTeP5-TqYymOSq3GeJRxKE5OIKo7xQ4XcVSbh2-t4X7Jn1N-02CkgixvgOUlfzn67Pbp9SSszxWrC-xs-fTbCAEa1h5w3fR_lk8_7apkHh2Tk-9kEAPfYWi2S5syu14Bb8kJdjtB6S_dHYnjm80OtkI8Vr-B6UCPsBpEWbqw7bUg7kxooixmd2nOcT6pAnh-gDJeXaCfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GA2Sv3ihmf1UTAf51vTssqJV71KIB3TF1MaKKLsFcIMk2PTTyOml4mdclyRrd_FU05rI68aedVBBQPnLYrZo2Blck6xrLwu7-F_o-R_4bfJ1n3Vp4EYANxNNacVhVTO_5SXUuKUJ8BckL21eLuwtop6jqTc4xcUp-CTdDdRgNBbrOLbkm0qFCPmq_Fg9ypYXuJbqocUVaFgwnlVKas8T70aiYrh2VTivpI9Wn8xMNrbfOPpKEy32IaT-Zm4d-l6PxNj9WG1Kk0AeInd60foBZThcPpTkoO37kMJKGagUiLpR_kRx26tcOEbGI5A1T4sn2j8Ky7RRAQWKMuo0gGLJoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CjSNzBcP4mlhqOkhx60RxRk0S1gyApTGODvQ3K23-bHfQJfqCZlBqZFvLH_vq9rgo5H8O7y-41lXAW66uQUlIybUnfmVIQm_K9IFUJsAo9h5rLQt7zQ6OMeBqiennkr-lE6S_g8wMRwC8QwF7rcAe_L4iJIKwVsIXF0NwVl_09rhhXD2JtvMbyIdsr4iBW5xh0NtQq3WCAhZSVR-eo0DT0E8di9CENhSEn8BQcMt2HZ2dtnksMA9v2Pn8T6SRa1SOrRRFwgUytjo5T-I8g7jMSLmAZIFeESquGcic6gWoeY-iD3Z-CNYxpOYRS5E4DDumCEG_--UZljrr-KQVDg_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxBaxEbDOt9LIXKICIyv1Px3ssTRyZpT85gUiVVp8U3NNrCglEho-od7UjMpTHkJ58pag8jiSf3sSwd2ZLARZrYHrPtM5ah6abK-9-ZCJ9VvdB1RbQboQ2fBm6yUTjbrUPHUCd0YuorHiksQWg5HA__LPVFn3mAgZYwCtGFKfkcPEEAYwbHV31qaF8BRxKiP4CwpRk_ZDzSMLizr7XuGhAFlQE8QFxzq67yQsIfMV8TPPRGMf8fOKzQlgloJbAxSXQUXiyJvOOaGUuJZU_NFtr89wyKsLY8TanBbOCefh_iXMawD9AuII6WSF6XMpknSVEsc8oH0i53oghkRKtQ6yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=h54gJly5KwtdX0H5MJL0IhT_y5ODQZmaV8lTxDlbsS1rKtAOA7cqzaM2PwTJgVxgYHv1aglBVSzXMvZdm1I-mM-rXbKSa1aGh88WE612GNB7FOjmWPRPsamR3UE-NAe1dy8Sg4ydiWWFaFDuVNQBEUa6C8LQkIVMbi58TBQShsm1Ug6ODYPzfZQ7s2vLMIsIFNgPYFePyCY7jSx0IMdy17wbd8B5pjqwM9hG513a1IBHWr7QmQSmgHr5TdTzVVBS3YBDUSKSWYCKU8CumVLA6YaD3LS2kAZTm9Daumr4D5eO2jC_frn87HZFbFVGhvIExCdeiMzCUHlyAeTeQ16Sig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=h54gJly5KwtdX0H5MJL0IhT_y5ODQZmaV8lTxDlbsS1rKtAOA7cqzaM2PwTJgVxgYHv1aglBVSzXMvZdm1I-mM-rXbKSa1aGh88WE612GNB7FOjmWPRPsamR3UE-NAe1dy8Sg4ydiWWFaFDuVNQBEUa6C8LQkIVMbi58TBQShsm1Ug6ODYPzfZQ7s2vLMIsIFNgPYFePyCY7jSx0IMdy17wbd8B5pjqwM9hG513a1IBHWr7QmQSmgHr5TdTzVVBS3YBDUSKSWYCKU8CumVLA6YaD3LS2kAZTm9Daumr4D5eO2jC_frn87HZFbFVGhvIExCdeiMzCUHlyAeTeQ16Sig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgldezbcyZ2jcYj2tQv0qaTnwrMQO4PeFbpHyYSHU2A9EjaZEcQiqwykWBTlfJtBiqVuKsHZM2c3wib3IF6WiWd26GRhEdJ5lhwNB_FOX0Jhe897J76h0gLlz4mwUc8Qs1KqHtW4TeC25JEJbtgDCJD9MxNhP6V2kQQy3uc9hI99zoc9JSTW-IcMH-d2m99JNP6F1fXcodAWviRbDfjJ542dofxpg6Cdt94J6MdPySlBkRKMWX8fn7IIBQa7V_LTF4U1bIYlEewXvcuCSEpjNhmI2Q0QAP2DVtBWCk2InP421m3Mzv52E2zjM_cziLtuyFuObAX9YOTVs1Q6swziRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oiV_eDXJ3ibgGW9rtqHagQ16Z6HELanoFOUGP_bF76_gcoRqRIBoIikSHdeQp8F5aFlo23uO36FZz5FetdHwMq0GJldcgTxGzuJqVh_-Ov0-zWm9q2m7vEkqfV2fvv4l2z_ZXkAnPAU-1jfYPzAh-d1T1nXYYFGraxHbmYHKZcdZ8wOLJME2PVGvOhLySPVGtscAue7Y6KsZY-otw9u_yOJ-ImZ-nWlissoGdhNEpYi3su2LvJ0hL1OuUTn4tRKfDwwbAyhnpdS3rxU7jCfAMVQZnSgMj1WQ9BM6eCZEDzxPJu77-y0LtQ5SCZbuRKeF4KmYzhOtXz_q9lbj4v700Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T1oLUZEZZdBepNpZY2Jo-lgV4DGBVHCF4Q9HNDZoyhKbyEWswa97kOT8tYy1XUQbw12S-HFvPyYPAy-sxF-iNxdWf6sedcRjzb28aD9M3llZ2sq9EFs1JDVHzg4dVhqHbVmyWZ_C2BpIgYgb1fdmxxzmHvyzgfPTv4qBoY_7amcKRxOWeZ4Gca7uFKtsAqLEtyiOurQ_i_9G_y3X4rm7YlHt2zkLHoPY1xZpMAyZPZX9PIdCqE5d0_PaYBlw0o_kXBIlZT-FrQ4gibKJxEwG8O1rCRlCXNWovvUXuA8HEP9a77s35uF53ASOplmZUyOF61xWHRpmbuidNfJ-6NYR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D-BpBd6wI6S4dmlkmmjdR_7iwKfNMWCbiQm64sn0Hp9zIHgHkJySvY0Nrc1tSxAuoKBI6H7JHCMwL6rHQU6HmcJhYA8nWcj0BNlYPwvQIRIYlI-Uo4kKGCSGIB1-M5pld5RFGTEtRccgMdysj-OXsT5L7ZtoCS17bHyTA92-GRaSOmJq25Cu5KmfG3qPkDWquvTW0hbqpUAy4u9gBiYPuztOoc1DXnGyvc7Uj6jULSensqu8UXHDSH4WIl0d_Auxua6ExSN3QZGdicip2_1ZbtAdh-ASxeD4K5RFSpbBLIFmjjgoKW1k__bdcS8Q8uxJnqRlnnnA102ay1WIehx2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UO0xKR1ZOoamPC5W1qjsug2OHS3AO0qfNf9BdgVTLdAXwbs9diRfb215O8u9MBBi5udK43-P2UmDXXn85wPClHgWFKEZTBd7GiG3zGQ73oof_2g5-eH6qkUDsH-YY83tIhckkeQPt4i0hdnvgs7Ngr05ft9PSTNtunCXvAttT9PqyPdEO5xPm7s1H94enqCV90C3JXLrmDdwk9xTIHm7OoTBL_Qh7VE5m4CTqdo0dMY-f5juihGLkHiqBETj7u67JnAI__Kei7KARiItgzPDtAou2wy6qIqfcQxHiKVmmI0gzeWU6zdG0vcjwiEh-nX9uzRkjEXjb0yO_M4bNoCz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XfkzW2P_5JaQzaICN5MBAV8t0kfu0R5PulF8PYCK_cX7C8G5Z20LHBM4mN82TumO5FYSGsbblvgL_8iW8xf9XKMNc77hAaC2qtXkElBsDcPzn8tufY7aZeguIS2kXRvX6zhQtadBBKJ_EIF05vj-Hm7f6SDw57qePfduB2JIqYxS6qalVSyYsSUK7afz1LVNiZCnpKYhNcxsV1ZJUGYvYq8_GzXcKh9gr3eFTiBmBm9sbXUNOWz6mQh5CVbr_-_-NdWYCgMI8E8JFuR7QJMgUWIQQyK5c3iebxaCThgQ_w93QzCq5ozoj-WaYQTITXBi50MAFiDCqFWtPG4b7N67zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqo9lqujSHi_uSJ41tjZzeU2Oev7PORv2w9Mkck0T_RZgbcNkJvogCakMulHrXhJlJtjuK45J-jt1wXseVeVYQ_OcutAGbuPyhUqQ41o-4tG9CcgvABMQeD9FYpHtfdL8DlsIwygzOJo8ITkn0wvJ4lv1SumoNcq2w-H5JDYF_tXI4WrbJMVQ4nekNDhPyQ_sYMZ0J-Ml4-aXsG593MfWqicemTOxxJ2fXgpGEbyaddny-mXMdvUuzOa_FEnwYCewFEUB-bpqK3N3vDpUxFjjOcYW1BmWFKA8eVnWahctWyDdxxXiAGzhp93aPb2LbD-EJ8ScbGOYtTdtLJ154LkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNaiU0sU6dfE14KSBVNBZxnjNBomWrhY7WK-USRAzxJHTyzcsvlTjq6qtgO0_-iRN2bK5eydacba4UdKWyXPiyimM61UCQNKk57nNjRe-GgykgWbAshs2P5CjYup1KESO4KU4ELLuJYF5t3En0cTtRpeETXsAljbVSDk_44jYcrf5Lf-dotmn5nspA9IiGjU7tZ3OtXrvexR98H3_4ygWbHiVizrbgByAuSFj7NcW1rCWx59uG2NhYJWNQYEeJ3fGUmavm7gxkVL0uMiQjlH_yIwwH-5eLpdTaj-iluIwJDCq0AYXHkLHLcUwwyzQNEPfEBnKBauzgB6aNRK-PhTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-ZBNZwtRgpzwhXw_6IdfzycdWguLPQNP86dXhu3UAIpW4H6IpdPmsktVMmHKbV69XzxsOM3fwP6nB0Hm0MClT-lK6XrRytHbbFbKRZeBie194q8RXvyVlGSigFNlZy6aEISbuo8SNTeO61xtV3U1bg1B96wTJKkIMDgNyncvnu_q0TvTxxL47-DGtky0j1TnHTpgjJILsNVYCSHP5p8GwFcNEMqJp7RAad0BMkkHVmmGKIptafodX0RsZUnMmXkxDzoYmObx-IGdk9W7z_bT6TpOobJB5uJ9bIVvqW1okbNBTCaZ3-QOLwAduUruH42GoV0reaUseNO_U2dLoIVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=QxmgwJMcGQFxvI9h8VH5wsuuLVFz-x6BVad-5HjANrsUKQj8qwo0oogLlmFj_b7ygPhyQ5BhjLdzeVKeMQ04zs6EStXRnOdXvP0Fil0Y4R0cu6mVqG6-P_cuGjxLqNKknx74b1RnJVDv7vnZsyX-_C68nxZgMnSKoiq4s93qliGqfCoDjvLM6qtoWZZF1YtEtuoOHhmu4s209dmFMUCdTsi0J5Qt20CrmF-w4wWL1gY8Od_ztg96OOIG1bTzpD82IAzRytJQKrkjeoS3FyOQLqjJlGn1-dnf0OXUdQHK8g2ZXrvMHJZomf_zHJOpQVOeVMbf3uwMCN-945OCEgPjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=QxmgwJMcGQFxvI9h8VH5wsuuLVFz-x6BVad-5HjANrsUKQj8qwo0oogLlmFj_b7ygPhyQ5BhjLdzeVKeMQ04zs6EStXRnOdXvP0Fil0Y4R0cu6mVqG6-P_cuGjxLqNKknx74b1RnJVDv7vnZsyX-_C68nxZgMnSKoiq4s93qliGqfCoDjvLM6qtoWZZF1YtEtuoOHhmu4s209dmFMUCdTsi0J5Qt20CrmF-w4wWL1gY8Od_ztg96OOIG1bTzpD82IAzRytJQKrkjeoS3FyOQLqjJlGn1-dnf0OXUdQHK8g2ZXrvMHJZomf_zHJOpQVOeVMbf3uwMCN-945OCEgPjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xj0Pm24-r0vgTjtFx_vi7aVPQVVfYnP2dlIygm5wb_ij9bbiMPcRo67h6AV8Uk9pdGoxjWgFOZKl4aOFiwgeWNvRbuQJkhSUjdFhjY5H1QHlYnlcxoxNYLN_IvNGd952dGJHUehQwzM7zToEn5S8325zkjFVxsLIfz8R7pUseqFdzlUrcGqxWCKoiPDFLc1wax8wbNcPFEcInXMt2UXauMCYLZiUaqleLMMVf_QRVmybJLXMAB3FHaTu_ipVQ0NBvbW9_KHZBtcfXYVn6kPSV4m4FjAyjxiefgtBnKvh7mk3vwNcYsaFU44SJHAtxlKF_QhHEHfONcYXLrysNRIvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_GhA2T5YwIjGXWWy0H8mY2WpAiQRMSgl9XTiDRKRZdm7ZsOfClGuThJgBm6jAogbLhBfhXgy-EqF_p_i-gnF1ab5F2ecJ6VrYC8dvjyzEp_JT5vbJ_TkUl-6s0IT2Ci1vHoWT8bQzmfHOVytRVfvmHO1e0aczHGBgaUOj-sbr-2-b6c2JBrXG6AyrmaacT41WbcefbNuoW5MiFu-9m6bynF3P3zRmCse3dAgp4ZXK_hhWHD0KO2XO-DkxnPoP3_OL8-OBKIQDAjwyB3YMmEbx8HMOAfwWnzV9XCBQl2GCe6ISFgnojyV5CHfrywPcDlwjkzeD18KA3SWyFP1UvE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r1zlhvaHmex3bXIu74h9aViwMbhJ9zQx2hgkPiBaan8_7awxJQghpPw-5qurGxC8cfHaG-i4yfMERHDbkoI3QcG_sDyCx-sPDcumWfHt2M_zVDH8B7FFb6WFgHdEW97XNqH2fl61CqAX4Frhj3lJHP7EJeLWMt9n6U9GO9LKr9xeQ5RYyk2c0yJ_YPx2FDoWp7SWwzVS43RdTGAz3PnmciHb59NvFMEGsqunF8djGOotry8ag_PzJG22aZj-bHYXP5nUOL0Y3l-_MNn6Vr9SSwCaZ1jpEd9erWunFn26wGponVlz8zUEHOamTGdI71CvEuiDC3g6-TuReUp0OlmzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rIyBm1y6RlpqK2ZMi7nAezUufbVb31sQPRFeFT0Hgj1Db33c3Q5Cn46I0o2A0xiYdWWWj5JdvFFrlfa607X20_yrXjV6CR5YGMNyXWlU--kLTDglIYOZDD8EOurODNPGNObQeFR0m2sDYdpaUfblotLw_dqLlhvvLrab4VdS6xVaDI2bpXE1TwkKBVIEo_IG8Cle3oZn_bal7tVifyelqpdpdQGbMdn4wFjlCcEvPlhucgVh0H1VNVCvRckxaUR2IyxYk4tbjJOsYPCpIFbtttHKYFrvkWmCTyuwhJAdDC0Jk0MZStwsyvygwMQ1SOxeEfUWKIn8J-FD6LP3PqRmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5dv7I7Xko_tMd97bY4n3njO1sQnqcn5CN-cDkQJZXu5AUUAygv98xzKJZQ_KWfWL9wfVz_du9GZjQlsyjmSmRRKBppqp2B8RfKXkQgVq53tKRUDHRn9o4SzohZPiAb9JM1PxVwi4_iRZLtEKDoc2jJMjuYuYlzwKRwcurTWSRqdKJuXPnU7S-eH0tPh1EpFsdHK8IXZQnqi9tIXt7cMCwDBE2tIEz8aWlkNu3LV-8Z-_icbuvgthR4mSKC3jx-xRdbjXxts5mNpbZJo1m2nbeuSuL8Vyrev8lPzxqlrNPCtUGx-158Bk69jN-fAp26rxj30vNYFXa4r_R8daplUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fpL5Ivc4N3wlgYQQ3_Je6rFiUNRMXOt5nRzUIzkI75c8VRv1O1_sspZFaCxe-KAeME6lxd7kN6vBNcjHtAroi3Vcs1gyIYQQiZK22_daADiDe1iMgwlMoxA0Wdq-bf4bipTK8-E19puJufdxS6fm23_kpjMH_jPm6P--eRsFaC26lDlAXjbQJGkM3tNUtXzpvmjhzb990JSjnMQUOdMW_AYo1oW6EaPILWwR06ZJOQC4_MMj08Nh5mWL_wf7KeLqGCRJ0h2yyWLrlj29zsG5WlOMo3SlnNJL3lO6vnLksAjV-6eTUdbOfMVu6_34bWys3Bzf1Pl8P56snxU_EMHU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8VV8fE-O9Ub99SHojmlcTfTHKYFQ1xY1WQtVOmxVIts2_k-6ZC_ml8NP4ZvmldOF7YibC9RW5RLrgCXiATwwUSqmuirlGVL5VTJfR6YplFGZbN3WsRYQevPxvNraSWlRAPYyihONWQMjiquSgU3g768ujvyfdJG-gpIi7C1rhVz9Tjhq4CdFWyvktyxLFG8JdvERT8HYF1bYhUQtF1MBDxYcdCzNUpJ1zpt6MdFV5wDMyS4WxMRc2madV1m7wwze_Fk0SvhYmJvoNYxZX7YRh-e3o2IlTqAr4Wm_nSDkbUCs6xPGwEzOWe5vimSY6uK8Cqx7r0-OoZUzPRS1C4BWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EK7---6fQRwo2x6bBijOVOSOraD7nNRPoyMPpUBwZcfTqncPiQht7w1IDUvtxY06PMzFaZfLZRx6vE_9RKxDGNl-LtWpJMYAE4ZLVkuGnZl2uG51-sJH5MspkBzib1IvDdOb7KLEO7Ho74P--Rx_ixpIkP6pmLsRfcu_YeJGZUPE-ogVcDq2AJtH4lTN3Xg3rk9IVWTJzOMei6ACjUoYK0GdxaXuLKlBUiTXv2Mk7jAPreDf-ppGDDXnI9kLj9lxO2J-vdGtvi5dlS7Tp1pdPGNO7JbMZyWe8a3iwDYQ0YpWJiZ3BaM-e2Kk3AtDMxlkPq9ewPfZ5jIYWvaY1vQpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HbvXF9u1qqee87oDn0BMTDV5byU40YKIDg1Lv7SLT_MJzSDNqcKR5SdByt1jwvj7CX-EeH-td_DCuqcy4rVawHQoxe6IUZlnJC-AL07htySkJWhSQGTYKFUD02fZYa8ggK1w8fWxN9YUMaW6ud9SpGmGae9vxBDz4XM1qqM94H4ybdGSQtfagC9wWBDL-VVmv38Z3Ciwkt0CH_cG6cknOKNbIDQxq1ebeYzC7pTBZAYpFOALheBoz2gkz7lq76q2_EQxPPe5-IBx_K5wityYRO-XQhtNxQei90IQKV5wGL7o53D0WRx6JzhgpKrVGIA1DYLFZj614RC5UYpPHcyd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MaA7-9DysIdY0RlCoiOSf9r8s-D3XQY4YvhHbDmOhbiYFvv2GzqLYYDdflPVf2aonX6sAVFFo17Cg7f7JT4vMdV2-iNNKrV1RyFW6g0Mgxh8OwEatUAxUBwTX6aGnXtiyrJDFcGCpXc2UCP_zDM7enNx7UKM9X-2hnPhS2ShLbIuAci1G2N5yoUG8ESkoSLwukK-GQb24YpVCLW4hZWmiM3jUqDzkmmtzCRehxNdEegxJWiAX-kQ7Ffc5UtdDuOKMd2bFTvK7FHClFnBzlRee4raGf1HuEEyR8SqhEegQV0-wV5x183fGrDAs5ZVNm3VZWByKnz8wmTrooZFLFOx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OCiFThjpi3zt5Fn7L3pl_1aQq-APzyIUYOK98A2b61eFr47fz_tET9UIfItR7k8pvQwPR51hKjJmYcu1zf_QUjJ8kxwIr_vPHVQbndFV7Oov0XUR1D1M-hpugsFdGIFeCId6iKwmyyiqy_o9KkK7rpsAE-t2yVWo9byKzpNAXVm8Anrqg5yhLKtiT4mW64Ye-UdrLX5LAOP3N8dAs-11M584HVzkOZS1D6rQJh4tzZ0h-ahLZdM6vyN6S0S3hjov0FEg1JaIeSaHYre_gwDMe-mWO5_ZnziLmgamJfN0G1GCFABvQaYQsKrT-lDo0S6OBK88F3MLf46uQn-rLi3MXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=XfzB-ce7xyZF6csQ_W9sCZWrbxbR4pEV80bFAiOcqYXQ1YdzCNC0p7PIGm0-gAv9Uku6XBZDXwZet4e8b2i_kws0hkeVCgoXra4SFz7GD7LqoqRa23fFUJwTPHDyCRHJ95EwdQUcnYGFsD5g1Ok3httrXprS8hWGkiWWlrHNT6KbnJ9XRHcZGqgPGEMzAsY1LGOHZiSPbtAx1VPFVMkwx4ZfDS8R-mywSBO-QWGKtwjuGzp1_VHnWVKYxbwyVBzjjtxqarFOjCk1Z6QSEc9QtB99rNAHn2bH5jMeIElwJbnnzdjK5IXkkgQOa-kI2PnmEzmwdSVFn3RhJ4uW7AGl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=XfzB-ce7xyZF6csQ_W9sCZWrbxbR4pEV80bFAiOcqYXQ1YdzCNC0p7PIGm0-gAv9Uku6XBZDXwZet4e8b2i_kws0hkeVCgoXra4SFz7GD7LqoqRa23fFUJwTPHDyCRHJ95EwdQUcnYGFsD5g1Ok3httrXprS8hWGkiWWlrHNT6KbnJ9XRHcZGqgPGEMzAsY1LGOHZiSPbtAx1VPFVMkwx4ZfDS8R-mywSBO-QWGKtwjuGzp1_VHnWVKYxbwyVBzjjtxqarFOjCk1Z6QSEc9QtB99rNAHn2bH5jMeIElwJbnnzdjK5IXkkgQOa-kI2PnmEzmwdSVFn3RhJ4uW7AGl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=ba4p92Zi6DlmGOW6vyyVkH3nkH9MQm0l5owF5qIV4VrYgkEZq4zVEuuwFHaWL4qcLGszicmcIWx-ecekxFAxsvDB58yuIHnM_Vlb6BnuCmQMEeP_BibQWBZ10S-t6lpszaOX6trbDHFFjJAY39jDUy8rVbKqU6rRS8A1FMNQUzcXD_MkaYzKvMVTLcqgDP8fMZ8Hfr0jCBjROWTq86E1XY3TOTC7T1WqMgUUR7g7vEtGxk8roxRdzRJ38CUzSSCLYKOcOVffEdPC5tp_AM8wLnvhh49Zc-xtsCZYo-CHDbVFZjOu9T4WzKUkl4nTuCTZefxblMTogLyCs3N32dtglA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=ba4p92Zi6DlmGOW6vyyVkH3nkH9MQm0l5owF5qIV4VrYgkEZq4zVEuuwFHaWL4qcLGszicmcIWx-ecekxFAxsvDB58yuIHnM_Vlb6BnuCmQMEeP_BibQWBZ10S-t6lpszaOX6trbDHFFjJAY39jDUy8rVbKqU6rRS8A1FMNQUzcXD_MkaYzKvMVTLcqgDP8fMZ8Hfr0jCBjROWTq86E1XY3TOTC7T1WqMgUUR7g7vEtGxk8roxRdzRJ38CUzSSCLYKOcOVffEdPC5tp_AM8wLnvhh49Zc-xtsCZYo-CHDbVFZjOu9T4WzKUkl4nTuCTZefxblMTogLyCs3N32dtglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jk0qoTfbSe5abJ1DHjtR3XJCvcjDiA6-XjN5xEU5ZxcohA_S38X1W_1MCmUox24MVrf-JbD7MJe8zXYGnoGHCjggd_JES8dSKTGPcxkNpps7-6pva5jJxA5vVmq6mbS9AscWb3c9dMdSJ_JLk7iut1UdkS11YpRU0x4pWwZ4uJ0XzScXqQYXyAoRn2JERIWaTM-x7uRYm6yUbL7ZWxfq7Jce9pa6RR3aCy8qrHTPfirPg2p-ZuBflfoK_lfiQ_pDJdDVFKSRGMSrvq-mMjcl5zPckCAW1dupY3bc0Iyw5UaiFFBcTc1hVbSY3jl1G0yVQThOvmgob81py1xAgqk_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ObKblOeus-eN039HhAAZ4-BCqAKsRDQZTZ6L6U3S_QMWLk1LPLgVtuFbNM4zWec5OeMM6bX_gNBFOBlfzaid1TDEroCdNCxs551Tlw6qUx5uCT4Ocq4-PqftAceVTEf1GUxOz4RzO-dLZ3AoAWsdAEEp5cOlN70HVkSGzp__Qd5uKEpQ2vmboUpcdEhNGi3SGcbm_pjCYPxfdEvQt5vG8UiRDnCBVJMTE0wPLbuI5iMPLlcBgZPW1CypVCaFPKSB-YBVZJiGj38V71Y4Hq4oCcXSOkDIU73EB49Ax59mCiENP5FVSO9i5xPaSP5P536DiIqAMjvWk1rQLzKcPkZOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tPA7ltxw3IGB8Vt2xxoXXoAVP0gigXTUu22ovPvxsidJpsV4QO4OWDjbdf9kVTdC7V7d06-twlKrVShAKgimsxo7uDd95UiTDqaUy7_c6C8zSbhEUq5gfxRrBY98_WXGVIzqQfMTEFOecSan88aeNxXS6R9cJlcMijfm-Kl2Txbwcf_2vkakmsGdRFiSN3SUPLkZz0oLpepkt2m5r9-FR7V9aZdTnIo_993ZFmVTppwZEaFOmN3GvyMQgR-9yJjAmIJoEVRlPOrk2rghn8AGISlxVeaaLJw6fu0doMug3f8H_VAYuFj6CQ7GhDIzxG2lJVK_4bupMmJpL4mu-iyQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=YCp3lfF3up_JdDMeJEC6qhVb9JhwJUb4cP4WN3XuLaHcOx3-jOjwl03DdaisMt8cub4YZU5BhJBrPCVxcAr5jlrOOCiZ5n0TAuASt8v0m3Fxx5TuEG-WpANnOZO9pyNXSg30XrUbwnR1MJrqpsXxRPpHzeiHtxdjqcVGBEGNOXci7z1FGO3ZRtkqTEu7iP5RL9Ie-p_0WvbnYQAps6ALXBdKKm55EqOplphoC7aUn07YUcW8tb1Jp93a4ZjQvG2GneCFji5V67UQmUJ5cf60Y97qRnVOXBvlTtyOQhYEFbjOSZvuDTOmSNKS-ZcBe14cni3LHTl8rtmj6kK6ZQBAkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=YCp3lfF3up_JdDMeJEC6qhVb9JhwJUb4cP4WN3XuLaHcOx3-jOjwl03DdaisMt8cub4YZU5BhJBrPCVxcAr5jlrOOCiZ5n0TAuASt8v0m3Fxx5TuEG-WpANnOZO9pyNXSg30XrUbwnR1MJrqpsXxRPpHzeiHtxdjqcVGBEGNOXci7z1FGO3ZRtkqTEu7iP5RL9Ie-p_0WvbnYQAps6ALXBdKKm55EqOplphoC7aUn07YUcW8tb1Jp93a4ZjQvG2GneCFji5V67UQmUJ5cf60Y97qRnVOXBvlTtyOQhYEFbjOSZvuDTOmSNKS-ZcBe14cni3LHTl8rtmj6kK6ZQBAkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U2-ZtD8Yg_NIk9WIfub-n7qWg4BfECZIbqco8fA6z9yTT7r0wyGSLpo5auYdc7lXwfv5gzDvWRMfWUnt1kQtbYBX9tC1ECAcfLG_zBaHq4tb6hzh7AHQ45szIfpJmmjMButp8xZJ00rGTUq8YZbRw4WnwVay793MI5BMjI42v7N3cByPvUOtxUlhHtmlPY1UXLLmOUq7gLfX69BK4t4xFLnbujMV29U__EABf50RNPrFs5dbuzYGYzvM_N2Xs2a8ajl4dsji1RVkN8JLBV0tXjwC3dS3yAOhG_mzSRgO5L2LSDVF1rbNJ07E8H4XoYkkP8iJUTdcxB7cloDrG1WIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DmYI4ZWFTst_qNdyCD5xAJoAtKQ5ZFWRPDTjAW9UMjvZfjnA9wgb7oC81ZCFFOZDNr0nP03QHoZkHFzETxNCN9NiAG9iyPEkR8jB01qSIpsS2F4nGicLB8grhpTg8rXwbwDu9Hhfoae-vPxazpNiV1U9HF-9rReV-dLfucbvBJ4gWinFDYTP9WVTo9X1cV1792tG-ZF3lEn5PL0SF6LYRm_A-IhuAUEXsOFZaQaEwfzLWHK6pIarKJ1NQqfKwLrWVdcpU_xT2rEqL97DzKgynRM1N5YWfnb5bAHjuc0uKf1zaNNVhs17YaRJ7Wvlpj1XsIdDjXCuqXpigFQ4OsQ0yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iIBgocqKcDZvmBQ59eKl4s_7Z3pRMxxzxbJBCl24Si76YhWNftxfWeyTDJ8U2bT2cDFI-xDC2NkGdkjpLLd2to2hC8tCc5MC3af5Bj-KKe2DCW5pLcn-9McR7gEJEsok1IdXnFL7EyCDYhxB5QWyFtCJLg65AVFPt-KOzUUd79VTrwql2Q9FjQH1LUmdyZrSLNtYznrQhYlPazktwUcyYs4SOle_vDAPCdcU4dfWAIgq9fL9UiWNuAuYz6dnUPPZhLuCFBVoAhrWC_Mh3PAYYfy4Mi5nzeKdlZ_sgz6mOR1-3EYcfs5zYrNsYxtTxbod20fXXD0m1UWCi_efAjpLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=DXw4m_NXdUlOGIz8WcVRc5MTWS1uLnegxKGQq3mNVmzF7tfjgZZx1iKU6v7Y_QmOAPqQSjWTz4Znq58AbOGn3D7wNnNrfZAUbzGLY9ltMkvBSABBBi77yygIATo-5IpvIkswHO3HGBbKSMd8vEnQAOsWOF1wZpyngg3NfKCPsuegWLj7Bl5Y2HfB7J1uc7ycqECM89XL0eJEMETwSlXXv20Ykoqrl5xo-2cu8jwMus79VRkI9LG0Jq0nkH_TDNeZ_PyS3Gmwiqhr0mN0NMJv_0VFFit3PQX6r4NIkYEY5bg6nO4utoLPbtV3tt-0hlvyVpSj3HN0-031CXh7YSZe3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=DXw4m_NXdUlOGIz8WcVRc5MTWS1uLnegxKGQq3mNVmzF7tfjgZZx1iKU6v7Y_QmOAPqQSjWTz4Znq58AbOGn3D7wNnNrfZAUbzGLY9ltMkvBSABBBi77yygIATo-5IpvIkswHO3HGBbKSMd8vEnQAOsWOF1wZpyngg3NfKCPsuegWLj7Bl5Y2HfB7J1uc7ycqECM89XL0eJEMETwSlXXv20Ykoqrl5xo-2cu8jwMus79VRkI9LG0Jq0nkH_TDNeZ_PyS3Gmwiqhr0mN0NMJv_0VFFit3PQX6r4NIkYEY5bg6nO4utoLPbtV3tt-0hlvyVpSj3HN0-031CXh7YSZe3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AK6QS_7MvqBYJ1A24PpmTRxuh3E-dhetgXplt7_04EzgM0f1AMCAeliF-4WzntTEf9FKqG_AQUil2IBOLvZ_DeyrSjOUETg8W4GeI-HhKU3Fp1VgFP-dgYG85BNZ_K8shqrD_3MoNkkeIy5kVxMlPc-zADhQeDGS2rSSM5F2Dvu0K0kCCEsCvqEOvalD7EzXQJ5kBx8YxDqoowk4PfRN1tXzbwSyCG5HD4Esa0RxlgsKw3yscLpsVxZ8uop7hm0zpEQdaRZQ1S8niq2c4a_kkPbqU1_Pb97qN4OEnO5EI4hUfi-7lCqi20iFDjAvvjy9lOmLEtaDXF1ksnK_BLW0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFS_YwR1QSJj8ny54OHfAweIii_pRBvJvdn-GjQ5CIPa7Nzd3AwRhPQYRVNcRYXWPauj1kNAnEXNyM4IQ6tvLd5TkJ4p64D04JN7pqy6ItucPR9hTqX7WxIpf5vHc0zAp4TqB9AKljI7RwAQA0NJpzrVhzsId9MPN_vcbyv14kHf2679jl49DjomBVtLVhG6lAtc-AMeVKgez4CiD6VmmKpEgPlwu5R2DDflUjnRjTJObVWvQr0eCwIVfOSJe__Ps8pxyimDC2msRs5F6lb2vP0n6DgJIxer7-Hg5wOlBp2HK_Z8Ds0AAlk-sFPpih3w3K7phOAvmom0Fu4LGNLb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=POdTZFCmcRihS1e7r8x7vjdkW2cw6j6fMOJz-cCjtlEE1__iu4NGmv0NaQe-hOxZITU1c-CeBp4Jfph60aTaUNvE5QiioJXkpKhvtm4MXmEjeV1boOTfGZsDEWBiXzAV5QjMzAH0t4fAreJQTIqUmpEy8vCAAdYSuRT3A4ZxXGAN1RG3RZxCSdJ9Nj3_kCjhnvFaqcx0oHdyf5qUBepWjPFciiE_MGIw-jDLexxxga8J6ctJoFDVNILKqii30rCW3t_KzcjuL1qf9URi1PD4TQ2z7g-1oHFr5k-9aW3odHFQyaRZSzUHTHkjlC9J62uNVyAQBGb_9VNa6IqrEwCQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=POdTZFCmcRihS1e7r8x7vjdkW2cw6j6fMOJz-cCjtlEE1__iu4NGmv0NaQe-hOxZITU1c-CeBp4Jfph60aTaUNvE5QiioJXkpKhvtm4MXmEjeV1boOTfGZsDEWBiXzAV5QjMzAH0t4fAreJQTIqUmpEy8vCAAdYSuRT3A4ZxXGAN1RG3RZxCSdJ9Nj3_kCjhnvFaqcx0oHdyf5qUBepWjPFciiE_MGIw-jDLexxxga8J6ctJoFDVNILKqii30rCW3t_KzcjuL1qf9URi1PD4TQ2z7g-1oHFr5k-9aW3odHFQyaRZSzUHTHkjlC9J62uNVyAQBGb_9VNa6IqrEwCQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYG1e7kVv8ajooxt9tjfNWQWUXUQ2a98MrtSvRyNiryCPPdPCLI8ziMDnqJEJj1eZL9kFtEhD6hkmeTlBBuYrA54gjacfdqLLFCjYCMgYivWHK3FNQ56mZZ893etgyz7wh8Z66zkAHmEFxQmJXwJWLQ0YiO7sEJIVuxFYqial3Jnvum62htmvNnFNeUuL2iDM4k6HCnIY0XqC6UJOTtGo0mD4dZ-hyHtuNmzWJe696yn82j43mOXWjyIGDFWGDkH0o8gaRYF5vayMYfrJtmFBJHgl0aCSoMAqgi8N_jax5BZvje3ZqcpQbLV3hgkN_CIOnAfXE5jycjkzeolwrq8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJ5usPfkDitHSDi-Y27y78Rxvc-JXsrjl-wYixOSv9aqt72C3txrThwRD4YRR27hm2414vaNrHCETeKbER4V_DdPxnWaJ0De28e0hsBcVatHywyGPWixEgC-eKOIdKSkW_3Wu9MYbkskw7_swGRmgxB8UGtYtabOKDACpyy4Vh2Z14h5qNsSxM5_ndypQoKXZlQVqblsDe5J0N-FFuijRzefDesdYsDL1iOw7XIwBNb39HkynlFfq9nUsZBpqIJrF5CyoXP9hhlGh6_x6BKD4CaruCp3CPrDrbbtverhdRLC3IseXWAXbsyr6GAE0KraUQdD4FDIw_V8vdwogTHrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hZ2YWaFhrOA2QTdKuQFECEgLPRW0yPh1rLWRqc79rdkvy2IyXawBAJYv5Gic4CsSXUz7_7uf4LyuY_gt_GDouSUDx0a4XEF2i0gTdHnNFklEX491Fli8Mlik7XoBrwUeNVemHf96v4FnYx2Qd-Yna9QhOKd2-t802Ja7UM1Oo48IPpisG_i9Jd0brzuuUcUL4zGoKf6QYg_WbfYOk1LD1DLF1eLZGWLBMGvvHZGpJZXadz-con6f3E3ntE3azQAXWKYWPZDTMc9LDnGu-zeFUt9b4T7n1aTsKj1kCBwsF9bEI1yXgBT9dxbn9GXPd0LCtMMpLIK74orFsVPdthKPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cvp4PNmYqtDBUU7bCRUyt8t9icWlewCZVpPySKy37M5M37SwiQ1LSm7OXJ2kBPLCKOCVYsnZrR26sUbZ-fR-22A4USHjj1uXxWxz_XZPOVpqzDqjjzkf-7eMBWJLMFvwErnWD0ywRkVeBbwmrWcUhrh_D2sZbDOLFqWwTUnXYdQ98sWm4YajFumiZFske-XvRTiRISj3mufaQF6iT0wbjg5HedCXKvFm4NhQzH753YcqXMJnOKkkBQ4AsG5i4RqmMoLE05T_hLaOwwj4wf0qU45VHbtpj-jrtuiz_NnVLQqs1M5qj734VRTPY6_0Fx2UGEezAoMSP-K9h9gfLQA7Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcXBsTzbc2oWTdNx4ihaZyNXQD184LdO2BzUwybzPJLk1D2UDuwSQnjYVlTyrww9xsBZ3iCG1pJNlCwzDKgYjhIdjBsG5cGXmfwXvnbN6j4aMOZtkjl7Wqj4ob6WrfEDWh9I0aNaCekzGxEEY7NRs4D1JVcy2frf5YOVfnYWw0n45YcTC-YctLGh521Ye3xxpSf8TguB4-33qWeDYhJjk93rJfdHi4VMu60GdbXMDI_oSqeahP7EBXFdOLM9OumqaebOpk6gtrDUiMmN9I1KlER99eOjNUpLz_RZTyqkZHHnooAm8H43dT3z3CVr6bIdvbYUgnLNcDL1WXjpFQiGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kFF_oP44g9f-vqJK3tzeOusXyWwlCi_tkgZ7MFqjiobZ4jcsS65cMG_zRxuuSONMJtVnjxZUxT1B12cRvo9LOVb87fKWq6xBmrLIpEUZgjrIc65FgQXefmV9ROKx7a5rLjO0LJ9E6JH3dC_Ipz50UUlZPaTomM59PYUtGZYsLAzQevZ9zdoSwArx_6MQCUe52nn5uO42jXYXX1EZj2FbfU1xZqhUw3CCq7yws2Q_MiW5uExlNAmwoz6_6AjBPqWDst49JyckN3AwWkmNkfwtO2VlzNFLA_YFCDTzer5q_s2iDld43icEboNjCudl41K9IJcuTt7XbAMOsZYGp6yR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QbOEPNrucu_L5gPxd44tly7quYVN9Vo0LPaIQizxbVd_BuqPomlRb_wuYkzU0DTKBTlE5ULFr032HYxvZj0WuzDHmQ9GASq8GNsz9GGiaTSxr72i96tqQsh8fLkK6AUuDHmsOzRdit7RH2vZaHScvszZR1j2mX1lgZGYHPfi-Cp_-vUM3D82dLAiDrTLQGnCElDRGqn7-zxewr2tPmpFAcHHPYxIgJXeFtRXqKGH41u3Yer7Zhh0S0f_ILbgjshowmsFtZp64XFr7Qj3g-MkZKGb5t3UjLQysIH9c14zH4p9ksneAatJK8nOA3yUC6NUOIV6PpTKjVrayKPmpf-jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vtrNYcTi4w4gYR9VU-_XVT3XzvdU2xr8F8VAKf9JMf2J4prP2MF4Tc4j_il8R8t3mmQqCsb0y7eGw7AxJTn78tmfI37PsxECCwPtWLivbTHg_-s4u50p_mM6fMao8OKc4IB_eWHOxnt7MD28h_Pskm4qnvAuuFzqhDrZVrbk0bKVKq0RXb_onuoI3abbqENXUO5SzHiwQMhDNBdwZ4MgPOBsMeaJsbnWKGyeW1LjRm8SulBdvBOuGr_aRkQ3EAQVdUawCOApHRHZQ3EtET_yb8nCHcfLiFKjiDkbrZKPYtUsQdmtpxa7OHPCyr1HUCgO3Mu2gbdE8dh7RUkI9YWVHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=q-_4MJ1TA03fFwS9HjysafQFBfikY_jOPPNwNL1WRZgc4uzGva89thozAsz3Fmhdv5r4iCYOFqHLFZWuPhVmS0TxKfPvQMoiDOgprsAiNk5dP4kmCfBWPFd_zYdDlNWFxuLQsG1jg0dNLzqs8ezpFAAEVIHfpGxH697bF_bOEkJ7G-wOVRSY2Ws4eWcFSiwVqg6KFZhjMSNc5hpYrsWjZBm7p7JHack8qt6FjI_ftq0GQUqHC11J6-AsoNheiVXkqdG1fwJ2ZMA4J2bJOgm64zrZG2z5QwnwcqHl8aLKflKyIYtw9cnPZnaTagDqYLYK3o8noqSOHdBIFKsyKIoLkplVksMbp1kW3PcywoQhVpIZ2eWOUuI1_O2qXzg4d7U3QoRvseGRohueBuSvMqn4wOOVicqFl0dU4pRlMyWYfM_oE8B0vwFzcIpOiZPIh_K6HYLVmwWnrJiemzERLu1JCwymuXPTISO3ahvFp-O-jXZPEP3E7EjfGqf11aRdF7BVYoDDDDxUgMAeTsOC4Csg9lQQfoS2z281ePmwTT-xNz9aeahWKpSNKJWxWQz3dRuecHbqv2VXleTOODpjUQuKkw3Id1b6uzSoLCKmgXB-KDauFgj2rDP_njfDVrkTkZaIowPpzw8cYA3NJ6ElopZosEu6Y9rjEXWfrBFYgCDe7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=q-_4MJ1TA03fFwS9HjysafQFBfikY_jOPPNwNL1WRZgc4uzGva89thozAsz3Fmhdv5r4iCYOFqHLFZWuPhVmS0TxKfPvQMoiDOgprsAiNk5dP4kmCfBWPFd_zYdDlNWFxuLQsG1jg0dNLzqs8ezpFAAEVIHfpGxH697bF_bOEkJ7G-wOVRSY2Ws4eWcFSiwVqg6KFZhjMSNc5hpYrsWjZBm7p7JHack8qt6FjI_ftq0GQUqHC11J6-AsoNheiVXkqdG1fwJ2ZMA4J2bJOgm64zrZG2z5QwnwcqHl8aLKflKyIYtw9cnPZnaTagDqYLYK3o8noqSOHdBIFKsyKIoLkplVksMbp1kW3PcywoQhVpIZ2eWOUuI1_O2qXzg4d7U3QoRvseGRohueBuSvMqn4wOOVicqFl0dU4pRlMyWYfM_oE8B0vwFzcIpOiZPIh_K6HYLVmwWnrJiemzERLu1JCwymuXPTISO3ahvFp-O-jXZPEP3E7EjfGqf11aRdF7BVYoDDDDxUgMAeTsOC4Csg9lQQfoS2z281ePmwTT-xNz9aeahWKpSNKJWxWQz3dRuecHbqv2VXleTOODpjUQuKkw3Id1b6uzSoLCKmgXB-KDauFgj2rDP_njfDVrkTkZaIowPpzw8cYA3NJ6ElopZosEu6Y9rjEXWfrBFYgCDe7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cwgPzWvQDucW3jf_grap_2zu3mrJGXxW03LEq33YaD6YAfsOMIIlMOuO_l6wsxyVH2aUPskUW0twQH8ihM5SpBX0sxw4JYGMSWn56-JJA4cYzeVKO-UXctL_rQILLDl7iEqRlivJiOu9SomIEKTG-4JZ6mS1b9cxwbQAP-Ns3SkWzAlHJHYOpyplffS1YMnK67OFAPgXFQ0UrFr-A8moddWMaQXzGhkhQXAwTYmhv5jRGfAk_giTT-ckqmP1Emt36LabbLXBKBkKJA3F8zutOseawNPIZ3uJTWiq71EBcolR50tLpD3Al0PVFkWXW3N_vBGvzYDlof9hHFeQFxnUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BWTtCSJfbZLcgTkf1aVGFpcGLVlvN2rYmtWE4TiZ6cSE1C-bjs4KxFgdD94i3K01-y7HyleC2naKIDiL0dxQl_tOO_EvqxCgeIed3nton8TDH57WMSutHHAZWrwoNUA7R9dekwN_saX4FleWOPEdwcdQ3d2p1YfhMzAuAri4jGXWtLIVkc7_ijkBfMTT9LhUrBEInl17Sn0Wta4v0-Wfk_iO4ZYxNxSdi_ZBPUQXBSWXM6-aBmKQIJ00nrxcYCIGsrJcrnm8H8IdUEACOH_LjCx4HkbgCIWtnic5jAYf3Ue1O3tg1uvGpSor8UQAWadtrJklhBdCxW7jVqx6Kt2L2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=AbBlFSte4LalpnNv7FMdZfPZjAyN_yT5OB9oXvjf3H6jBtDWWHBsRgx-yDUgw9lRjtLA_rNCsnzZxYPgR51Llv_t5ivMmo7pY_aRrOFp7ACVasd3adVCyWZtuCj-xZVS1C_XRWbCyaTrNVEH0x60hmvVKIAGKyOVT-82noORFnRfN9sYNTKi7CPV4n2rEdhSYLsPz8WZoRmPlOJezSsSfjJEXbioak49zn-c7Y9FeG-Z802EXdfLhdniL6Qk6ZSUK_gXjPh6U95BxHgMgi0CaKS61ZJKaTwf-3ZLCZsYNbRfIfZaLV4VPUl1QFFtSdwrrHL7Qu33ku7LQNeaH9Ttjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=AbBlFSte4LalpnNv7FMdZfPZjAyN_yT5OB9oXvjf3H6jBtDWWHBsRgx-yDUgw9lRjtLA_rNCsnzZxYPgR51Llv_t5ivMmo7pY_aRrOFp7ACVasd3adVCyWZtuCj-xZVS1C_XRWbCyaTrNVEH0x60hmvVKIAGKyOVT-82noORFnRfN9sYNTKi7CPV4n2rEdhSYLsPz8WZoRmPlOJezSsSfjJEXbioak49zn-c7Y9FeG-Z802EXdfLhdniL6Qk6ZSUK_gXjPh6U95BxHgMgi0CaKS61ZJKaTwf-3ZLCZsYNbRfIfZaLV4VPUl1QFFtSdwrrHL7Qu33ku7LQNeaH9Ttjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWkWpu5pFuBMTJa-DDBMrGxfK3-T7aMIwqUC__yBNK6uM4n_CThExECvQrEtDfzk3yhf0U6CYbbtvvYvBwSFOWLpmgHWXsAnd1HJdwkd22XrNRQ8Cc4OxI8FeKYKHbRvivkV5nXAuT6moUqeoUHSUO6tkQfzvlGpf5AeQFWyXcY-Z3bqisJV6zHK0nO5teW1JyDi8j5Cl8QjBQ7oo-VicZAaMlFMgMeUu-817DkkU9NEuytHDeVpusxSb1XJwKfZOjQRM8KyNLfDGV0CVAapoqOz4-Fun_CT9xhyT-h_MGvXgx2NPbQj-2KVPWG96NEakSiEbBc6Gkln8mbdEk7DGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/us43aWPqtvLB7L2taPqANfNNjdh2fnUBD5hbpyKb85XUFh2hxX0nXJcLHAdFczgQBsty-kPcvoeq_V_rt60o_Vk8OHKOxuIolmhZqDmX4dtoRvwbSptBHvhPujt4SUHHB7pIxqej8-AwUWhVSdxAwpFjyG6uzxVzZMC1WSNbh_ZZZ9rZdSQEbTLUFC1QfPiejA94zqg3ihymmY1BnJXxMuTsfZ0DK_pa2M3_RtG6ZPaqQ4SN-eUpv7sc1QtGu7XXjVp_UN4bNuHVJXasqIjvNVtjgkhT05k6MN5POLuTs15D24ADyzQ0r8WZOLZUA0TrxcPENAsDwvLevmp2ioFxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F7p_Y1KXezoFbRM_4dC7eD_KISmrCFNolx9Bnt9RfpnVPJH-S_zHC-EnWE_TyMfhhztogACxMqahjoRoFGnUYrFjodboMZu1z5MMYKEixPuP9sGtWITKz5ZW4DAlk4_CNe9WQGBcgNcDSU4HrNA7f_0M_rztJm3tTr_DrNDDABywoHfjQdU7xjDvUPux12da7VCa8ryzFfhBsC_6O1V7ipQAJIXxqPAzbjJEQx2L5Knzs2XIEPdcEW-bLbpQd24-Nw9qZGH04-ZS1Wfg5Y9980XXm0SJTY8Xs9zaAUnTEF2kbvdkjfhXmMd_Cev4Hf4B9OuthX88dq2CGlqjdwNpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=YF1QMCIXDBllFcETvvNaiuBl_uYGC2nRlB7fWaY6QRnlEdoXnYliENeTuh-B3f7BxpAMxEvboNSz4MzwONxd6WkLm-orbtAJHEmrwkkin2SfixipajnU9uF_0JxUx6NkxXpptTZfRini1EbJwovQGyEDJSeMXO873XmrV5dpgNs7nxoANBhe68B1GX6S2tqOumAHnoaRc_hdI8-Wybhu5Lsn7WMCofKhKPJ3PVnEO5hG74TtjWnl8DzsODxSWtcxFyE6YOlM_xWAsV_zXBMZrXQYt7dhNNMyIV81tptEtn4dYwUYtBmsjUj_0l6TjUc7-7xLCt8Smbo3-lOZFuf6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=YF1QMCIXDBllFcETvvNaiuBl_uYGC2nRlB7fWaY6QRnlEdoXnYliENeTuh-B3f7BxpAMxEvboNSz4MzwONxd6WkLm-orbtAJHEmrwkkin2SfixipajnU9uF_0JxUx6NkxXpptTZfRini1EbJwovQGyEDJSeMXO873XmrV5dpgNs7nxoANBhe68B1GX6S2tqOumAHnoaRc_hdI8-Wybhu5Lsn7WMCofKhKPJ3PVnEO5hG74TtjWnl8DzsODxSWtcxFyE6YOlM_xWAsV_zXBMZrXQYt7dhNNMyIV81tptEtn4dYwUYtBmsjUj_0l6TjUc7-7xLCt8Smbo3-lOZFuf6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nPcy60NK3OH2fcnwQX3WApVWGH0NlhWJy79GtrTsYNtClju-Cy9beaRDkYInd5OuR4CUk3vDrWS-fQ9E3zxmKdUfA7RGpZczymM-0VaKD6m_qowK08ZaGQIgZ3hnYRm22Z-81VHvedgffHnVZMSP7y7uHR1AcZ17DrimApDLlb8P9sA9zdmPsThz0IyQjW6OprZluwW7l5rTsNzUaTkODmfKX6kJzd0dmQ69qfXqUTtp3Vw1QxYf0r36I8Hz6k-C4AOk3sUygkKfOSUMdlIfQtFDssXg5l-vBAcHXTgmYBhVvT-QOkVNjSD3F-ZSebhBg2kwQi9ZIJVJ_oL9KQt3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=e10t91xbBaMV5fJLeZTDbDvAZojcpygsfbPv4a6aJjPTi2PDIH5jfxA22dsLfxDtl0jxiu8MMgc6agZ_h1xw1Qi469TrwVas9wnMrK8-30g8lXOmvgTwE9_3bQGLLZzX2J4X_uOv2bfbYZpGDO52sTkdGl0LEKxr13eZ9tv3VAm_UTimRBJpHHajzgIjsL_4jog81nHGYg54sYgkwAk9m8AEc7hpXITKxHTtdgYiNkxjJ_600Clw6Ei1-qXQNxwKHHYqfgSVkLWXHJ3-W0NdkuBvbheJ4VPL5oh5AqLSulGnCEKmgaezwe-ErJTXjGXCjbY32pTjxsV_pxJ17bKezw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=e10t91xbBaMV5fJLeZTDbDvAZojcpygsfbPv4a6aJjPTi2PDIH5jfxA22dsLfxDtl0jxiu8MMgc6agZ_h1xw1Qi469TrwVas9wnMrK8-30g8lXOmvgTwE9_3bQGLLZzX2J4X_uOv2bfbYZpGDO52sTkdGl0LEKxr13eZ9tv3VAm_UTimRBJpHHajzgIjsL_4jog81nHGYg54sYgkwAk9m8AEc7hpXITKxHTtdgYiNkxjJ_600Clw6Ei1-qXQNxwKHHYqfgSVkLWXHJ3-W0NdkuBvbheJ4VPL5oh5AqLSulGnCEKmgaezwe-ErJTXjGXCjbY32pTjxsV_pxJ17bKezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lM4ORIUmO_fsDpTlgZorUsnWCGQUzTZmyqgvsMqkJLwIQC5OikOXtsVEJQOCavxWEgSrFlPJHQNSbdHK79T_44lqwSD4og57Scjq0DTEwsCruAdKw_91cu_-Bm1o-skoDb1_WJe_oMYJjiJa2nnQVWw9NkEH3quB0FvexPcIDwtWH9xPS-KTAqiBRCXMwajm4WrSmF4jzq3v2GmdHjLNIVvD7_eQqugWZ50zgOjPtloOJ4kPK0iSaJoMj0MNkNshvfYWTC3ALanR4LP0I3roDwKoueUFICDx2OY3dlwX6_4Uqc7vf6h65t0LzeSlC6pZm5bOyn-JgOZ4qNagJeseOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TqcS-ttOZG3moTNJ9QWHXJsECvE_cvlh1WPcZMkk40Y-lD0p9GAb0J_Yu0JG-Z8dNJDZT2TlZEobUQIWNKCdhaBgzBCLQxTCcJ9GmQ6i02sNLZYBuuEH3LCH8AASA4ZHvCzVPTb9PKDMKPYSOaaT3URIU6OYsU8_-2AFql4j68E2t1dxGx1Lp1uGTsdUSpyo0WDIac0y17sK_wX6uj5EJov3HPgKkZ2zev6eBWHyXY3HypqSIq9YJb3KYyNpd0O6r8ZBA-CQN-LXfP4iXjBhEfdOnBM2OmTCqy7IbjkVUx4RQ2s43NxyCq2bZw3bCoQauPlF1zziUG8HOyER8NGj7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NeCMDhW3E-sAx3wP39FL8F9PFeUsk1m8azjSjLnb70nfo-vIXHpt_F2NQuRhVncCTZn2efHOSQ3LITklEwhKbAx-gtemicfEEW91a7gIiz508Y5nt8tPlcGM72q-_Y8cPj0zKLQXoU_MSkQ8qBaJfA9dnuUBT5diIUi31pfuBCpzy_5AYvrcDd_D5s9M35zLJr5QAhmWPNcZHLN7fRkzpSDDw6m-M9AW5J_UitkJxVjGT49QZRqLtCpRtze_klAkgX4UsltUOHux1Y2UoP9clQ3QcfmTGtoSgu5Ytm2Vy0NyB9tUCoa7qlTYdZlSkUmAVbY-y-7OU9oYGdPODsClTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vo-OqdAbkv2t1koSJYyvUnbjlNYgjHfevwr-Ggc5CXLEwT5UMvuVxmhCtnWVXnphUxGp87gYTwKL76fKY776xSuNtRzlH80dZ82UAGB6ieLLDrldmL4BapZ_Gl7xZPse8IHwTzP0NQBNgHN4PDg9qXBjiBz7QLVNuYg8C6XUIwf3ICqdeGLriTW0GsylFln9q1hKrkoxxOHlNlG-lo4zmjZ5hsC5y2AVSGbwI9oEymjxgIc8sP6LFqC71D4Hoh5rCNKnzhq1lNQtSXyVjl0-sk3yNGcgAeRoUPFonZ8pNx2u0UkLsFEgbwkV9hclKkzYE9armveQ7EkASL31hHVQHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t_uu52R7vYc9lIe-qcFE8tUuWBDeI-T-E3eEWD_R6MMagASHtI0WYRozRP8K_GZJb0yNfLW34FVP_y1_-HPYcYqGi4udmWT7-K5obmcJAGR5SOpxQZtSg0xqgAdEFKTNokM0Cw5cGn8qwMQ2X6ug98wlhk_sJRHYWRCpak4TfPTb8bO4sQvfyuO3tuPKzdvykf17OsMT6DQpMk9yXe7JaJJMJ297Zh6Mf8mffffdEhsU2ZsiVBV6ptHecTyXGA5h0QWaav7gk6Vi5Vy1A0QpFJU_dVvJRJ7cSrcAVi023h74pyYOtLgQq4l8YT9dfWexEL11-vklGxGFPxbz7CMG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GoxbjIowMz3dmj-ip4tXnfNBHDe5kWp-wSKIhgcmGyQcpuuuXuGzDhFw2mzjVkLdVK6BhF5ETCzybtiliOYMJMbJgNLiltxYDK0fK86LlKyOuTuzs3oRfzR4xgocGOixA9EL-dKgaSzLIxKCnMg6EAadtG9hCPb0CUwm07d6b5OwhFOncI785VozJxt65oeab0XVcnrEycqd2p6KIGSOjYwPrcm9RMJdMofdjMctQhwD3gNWN47IkyN5hIt_MxOA9_UpGcOYWJlnCoO9_ANs8wh1th4O4-zfIOvCwlBU4BEsCWE3l04Obf4JkTh6W4Ulx8oaZOsSMmY4t_O3YbwkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DrUi5Kqa2xFbbFuJ5YhByrpvwl_MmkwGdJhK9cIkuK_5XOIyT8VTcyE9tdoprw_8IaE1DAiG_tSU_MlKXIwtndYHhgKJgzUK7Hc5UP9yPtqRI7VdZ6yN7dAFb9ISqkf_xLVBcwif4d2H_LLQqg6wbAq-laPWRk1Cs_NP60eG9elDew9P3DeAQ8okSUG5dIKHqaNmPwJp1IrDVMaHgSsnlvtUCnQKASM7DG_VsjRyYJEFyGE-kqY0KiCYKEF-aVdMiNZ-S1BgA-755Lkege19WeZiP_UuSUPKKMh7XlpjDzSvrV8H9YW5mnBcu4X8g_OQWYkVY1ieu_vYquumbA_Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gbbhpbLacqBIRqgatAIb5Mf5CQ_oY6AKz7mLpkQsNYkcUs0NITDsLZFrAuUTr878xT2mrTOiIwGVMXIByHyBhI6MhaMRmCc6bg84c_jO_gz6vt7AOjjtG9i-8Zxga0O8ofVlh3Zohl7AWFpB04tCled7RvvmI-q-n0dzb4u6MZSH4n5CrBlpSf7fr4eblaX5ZqhHQdKNrEjwPFgyP7QuNM_DEwLX3uJ2VzMwDucWlpzZ4XffTSCkQoFTGhBFmBSCUvvzWEj6t1j-XC_KM34pi_2s7nMun1684eoMsY9wBGA3_HbiMRjBgy6nE3YhZiPGdNcMuMNAW2dmR_x1g0-7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=l1jvW2JA6oJEpolsX6vXsRSQuIIzbdYVuHN3kLWr1Hr91-yoKg82Bx4327fNz9kKNnRoPzRY2VrwDRdV5Mrf6v07ROrP79xjLCNw6ToDfIgXavGA2tOxvrFqfMZiAM47SxjcGv7W5knjf7V40TKCnhLC-ozcGYXIwLntYjJ0EP_Hox606V8-vOPAr5TSYQ4r0pvuz1Fhv06tudaOkKZdvvr35BTomBzQ7YQEkHPEXrxX8DWjkx4CrsKkMpn9R6IzQx9_4ipPtBN_L3Wmu7qDyXJIl9c2SjT1GO-v_wxq8N1-8NyvwZIlc9ATKV0vu519uLc37o80yuf-6iM8TNz6nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=l1jvW2JA6oJEpolsX6vXsRSQuIIzbdYVuHN3kLWr1Hr91-yoKg82Bx4327fNz9kKNnRoPzRY2VrwDRdV5Mrf6v07ROrP79xjLCNw6ToDfIgXavGA2tOxvrFqfMZiAM47SxjcGv7W5knjf7V40TKCnhLC-ozcGYXIwLntYjJ0EP_Hox606V8-vOPAr5TSYQ4r0pvuz1Fhv06tudaOkKZdvvr35BTomBzQ7YQEkHPEXrxX8DWjkx4CrsKkMpn9R6IzQx9_4ipPtBN_L3Wmu7qDyXJIl9c2SjT1GO-v_wxq8N1-8NyvwZIlc9ATKV0vu519uLc37o80yuf-6iM8TNz6nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PiO6bYxM7cRXMuE2D29UAo2ASUc8a9sTlPv_HVaQlTXWWozc9p5XFWR9a6EPHk6Fu3hv1P89ouP14WdVXp63iHBLyJf4HtjnIrmDJIZs6xaBwgEbKRqYMK-oogugxRdu1ZUM6lXU5Y4sjt7YMLMr3j9MOh6oGnbpEQdZgiD-Gg6-yXaCWm3r-S_-_SjcBs0Nu7diSGOWyCjljO4W22ME750ZKy7naIU_Y2l2-ZA-wUVlFD9x6cX3wZz8XpBFqc8uHClxYlydGGx1iJHvoDcOLZb_oFzOqjC9VIwdMw7menWMFOgTYhC6Mk-0M9QhsMh4r0qLm9kcgrnUzq7KaS_UxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGrmK0U_3lv3b0it81M04csUVe-VdgLkfegeLz9qJEaxCenx_0gEnmGm9WSads5ZAnV3pgsBoNpp42-oqOcsELkdqFcla_zlEoYBuCOxjVY3Xb-son2NbXNDjyM285eToo-sZs30wr4mXj17hHePUKQdDm-C1iUruhdLeb8XuUdT92MKYrJjPq5UZ9qAutKGya-V1-HQI2_N2U8v-gYlym8EP_ZV8di906ljNTGBUDiFMlkzK6nd915xjEkOIhertKTtoIkmF2Ah-siIXTpJVNri4gVAwyDIq4cTu5k5nLkxNbH5igYdVkTQCutol_9wXBUzyi0T73Ktu8Wm2M0ceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pJZ9kMn6uqst2Tr1SjwJMCAW2XsTaC9VX_0h4lJ2fgCKpoCb0L60pYbvXCctjegtPpJaSY91_7pHEu8wwUgozoLmC28SYkcLnFofxYj7W0XGJKUtm_wsThO9FWnjE-VMBqqHZRXodH-R6EX939FDUAFIIpwAoHrc-VwgOo-iIpX0YlHVmsKa6gNLSyrMNVnDoMUEJE0HxOoiuZcpAD5HEPu-PY7MvwAamj9JFxL2XJn6iwBQIKidduKfjEdvPkDa6g38lqbig_u8smXogvl_63vDrIWfmCy7ivkL5F_xPC7TLJoxvk_RuT9teDb3rEQIuJEhz2DKwYaJXTS83Mm7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eh7kRJXus0rM_tRoTl_kmAwKKlSaaSJDCExvVRnZN1oQvMrc671hHBVhctUnXeGWJ442srYi8rZ9ZnEp0QKmhkfl_I9U6DhPf7Lic9aceRrsL6SbFHtExIOTcq8GnP7nbAFH4UZXBTCg7nzpFuL7jg0wTyMIuSUOQ5af_JTP3BrvzCXFNS7Bjak3GHp8IGa_i_pWlD4Z1H0L-lDitKa21QpiBNsxKygZCx8uI3rQtFStR3eBO20UvqPLVdvuah7fEYbkO8IVpDAw3ofA1s-7TjAa-yaRLy9qiDz7TG8R-bizSCi-DqBlSrojK8-1it1dULwVjK8cKkhTC5ywgNjj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IfVJMktelgNZ7loL459zi5sFkBODsCoTwUUqOdCw-BOP9m-WKGZ7D9kdozniof8gvg-3u6E8RdmkPYMs7N_YcEjbtuT7FvOa61DoueatjhYMRnnet5WV8Klf8eRyrmHQ5AtTlJsgqWyXd8EnR54W7QvkVglXxuZhzG1MC2bQ_NbbK9E67xZhtgXyWRTJiMC_aP7_qHVO_UVWYP6NDRkWyolmcoDdx0EzHeD_KVLXaft503Y_tMg4L2Jbmw4cGWdis8TpCBVKr45aZ0ujLvH3xW_NvERqiyImd-th7eLbYV2LJNVuFNPa5l-JwYlMdKx0irooMLKTcMT6K28hrsTc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1cp8CpXcTasaXgB9kLgOGOW8qrsz5V-5aW2ufpy9ojBKXM3Qcn8Vc6Os1puKWPjEjjJgHmCOp5_dwIQkbBD7ZNL4HYTwszyXfA3G1mqGkFu4Pv3dV_f24Bqf6GmKsIaxl3Up4mJdaTyS2GYC6jBc0z2g6zP0iZ_D_1PEb_liso0Xe-VQHWPZSFTJmmTv-qm5fpas5QCeMC7xvXmPYQLNFtaMYcVfOiQQaKUEGQQCjXyT5Qo48dPyicUFZkAbKOgM2n8V91u8-84bL483vdTbrCxupf3zFZxbBUoFBsWewiE7HEytwefGK9TmqadwLR1sKPGz47HvCrlVG2yp0LMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OedHH2LLrbRe0sI4XHamRjCm8j-scZvdmWx_VMGUn06HetvLaZZxvODXNJCy1IK14bBUohK9uZtrXMkPzoubNQHsDSMbWmNg4uggldXPtAyQOrnFIju_X9F2yY8lSkGg75EszIu_Vi-JsI4dNRC61XqI8QJFTU1ohIxdl9Q2FxpCLcHWCCtuNP4-Pp-dXSI5HC2cJe-iw4dTaUQgSHH84PYhco6-y_VDCvXu3J4sGiLZL14k9I6zdRkGwEAMbfiYR6ZQGMNBI-U2YWPsButDMEiNk2zsOkxD-ewB_4VIPudXSDKxY9prOKScTQKjV-_MHKDSK9UAgubMX1ib8OhGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FcYxTXg8PtlJiYNWuPC6KmbQ2M2Z5cPAqvSvrOn93u9uTLed6tKSyqWKcweIJMml1c69fbJ-L9fG07X6lce59YHa4VcHC7iVnfX4ykmcyef7A98Ha5LPAXqWGuSv_jwN3y7d4Uw1PP5NtBvEEV2ccFRPSiSR64yE1lSrhe3_HBrttSUc4Tk4u2UI9PMDSCyqLhprVRBHzb0XMWmlLYR9BkMLb63ky26Px8uuUI-Gfvr0LBBTqHzurdFAnaH_lOlgMb7wgEovrjIvFW0PtUU934svoSMtL6Uopkz8X52x_dRiaoLX5uxSOuJgd3XcjFIMP7WTP4ykUb3wEd7e-cbc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2wzz50qWKFY0ACThvvUuamBtkIifNYZm0puLbVeEQ_W0rfFrpmpN7oP1TbIqfTQgpj5MX4wRfdcnccrQjTsFsrtXktpB0wVNjgV_rICVCnRq1xf0XT2qntwuSWIxfuqksHgejC-wFU0N3jHlEHpgVlQ5RRuT59Dj_CfXjz_s87vinq-e8QC4o_qXJuwfNf9kAjH4a-r6Iw4SFRLegjinNBkFSEMhyUM7qLaT9FDC4QeH8p3i0QPIjbzLuyPtwDmEE9uwIT36l4saZOtquQZPRyukKZmHi0DT30AMipzfUZXcHEtuHFZMJbFombaU9dkq8qDNy3RXEE8hnyZzqFNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILhuYQ7A24SLR21bRKtXuQuZf9KIthKOEu6PvJqPss0Q5JpDKL9w-ckb1z6TkzcCEBIIU2m0V3ZlOcNZte7GXTSThEJR8LalJ1pqZsixGXUlAuOjvbp_cfUb06T_xqIlMrz9SOPfHC6NKfQ4VL-VYqEZnEeGFkF5vr25IkncVQNLEXhgLoPQ0S26FXGc7gWHlwx_BmxGyDvsLTqaXbE3bxxeoG9yHfnJ9CdZipdym5cosFLgN-PiIEm_omlJaZrs2wgSPapo_DLr0FpXjrJoZ9KVPD66Rs28yFMIQljfxbqADrZt4KdAdlV1CYJNMop0Q4aqSf-udw9eMaOqia4Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=iIrbPCKvRAH-CAZKN1RTdidmiXm3I1AlyYBDooV32_yVjhKET987mcdvBRt8zQVR1y8OBPvaaK75eTSLJXLlbr4VKzsMgFAoVFDD9-02-nhc1dFGKsmyX5vYasdBPQFOo2CUM8YXG3icIjLls2I10v0A4GuvjQKxMu1ICCHjXzkh8irM_0Nr5FG8F3pUyG67aZp6TT6krkEpWm4ANkEqs2PkXfdJsxI990LNfdoK3wGLVW_5MF2XFq1ZwWlLi7666FSSQq5s9Az-ybIPI_G-a2gdyih8bL1E22BH4hdFpfgqbwZPXnnysjL0CWU0aJGxjCziDjfKabcNLfHDjwuesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=iIrbPCKvRAH-CAZKN1RTdidmiXm3I1AlyYBDooV32_yVjhKET987mcdvBRt8zQVR1y8OBPvaaK75eTSLJXLlbr4VKzsMgFAoVFDD9-02-nhc1dFGKsmyX5vYasdBPQFOo2CUM8YXG3icIjLls2I10v0A4GuvjQKxMu1ICCHjXzkh8irM_0Nr5FG8F3pUyG67aZp6TT6krkEpWm4ANkEqs2PkXfdJsxI990LNfdoK3wGLVW_5MF2XFq1ZwWlLi7666FSSQq5s9Az-ybIPI_G-a2gdyih8bL1E22BH4hdFpfgqbwZPXnnysjL0CWU0aJGxjCziDjfKabcNLfHDjwuesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZsZcgLNVBrnGKQQp1cTFb1kVPVosnVH_Hb_1b7wdUpzN1iLWPz-6DLKkQO-65aXzkntR0sSS2r0bZ1F94kiVQv0qF5pcXIDB_r5hN7wBdcsUuDXISA5kOJw8DRkUjBM_fUMt0GYl5HJp_SYTwQyOZhvf7WmPYwwzYg-hCwzPAVG-vZyHC4y_GdigUWdMhxCkkpqOmY0j2o_LT4YvuVh1NkXzfdGpbigDiKq8mlraLe9hDa-V_X6TzuF1NlewW4c3_uAGtI1DLi-UDq-XBxZLBfvvNoTpXB_6QLKtRl5QeE5Lcj5nrR1UBjm4qJ4Gq-_JlNmG748xNbVWFPYxcooqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=htlgRynDmhVkgvYYqJlMeHJPZ_Qyr_LCz2yU55JPmj_JF8ngwrvPlMWtXbd9cvvjd-8ndhsUQorZnt_GvSwG5kDTc68iyaXcVwZK57k1Hg63I_grcq6yOIJuLTBcAPMnx6mSSGDO44uqeqxPxX4EqIpFVIoTa9nU8GcgogW5AdwejuP4p3TjMInfXsLTikBJcBEV2KT7ql3VmRKcGoQwQLSxImebEFDoGntFwiKMVNuZPVGRtTTQCPDSi2AddcK_db4FV_clr-JT2iqsJI1QOw9judI7cYXZ3KPNoc0SQnGdIlbGXtXRytT0-hwUbfMOzgZ-kFpMdtyvirn7eRJs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=htlgRynDmhVkgvYYqJlMeHJPZ_Qyr_LCz2yU55JPmj_JF8ngwrvPlMWtXbd9cvvjd-8ndhsUQorZnt_GvSwG5kDTc68iyaXcVwZK57k1Hg63I_grcq6yOIJuLTBcAPMnx6mSSGDO44uqeqxPxX4EqIpFVIoTa9nU8GcgogW5AdwejuP4p3TjMInfXsLTikBJcBEV2KT7ql3VmRKcGoQwQLSxImebEFDoGntFwiKMVNuZPVGRtTTQCPDSi2AddcK_db4FV_clr-JT2iqsJI1QOw9judI7cYXZ3KPNoc0SQnGdIlbGXtXRytT0-hwUbfMOzgZ-kFpMdtyvirn7eRJs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHTlmdklqz1ot4TkUyHH-zCPX9VUlMG9ZDX2mNKmUKS8kfMg1chQ46Wkb_8P6HGVLIHLj1YahPBKpzOWBcXlGd2ASSgKpMbeVLQqEtrdg7FzEKGS6LIu6ZOY5DbfvuxIf46c0QDRdUntKE4YkqwUSaqGPGpzLc0ZUYIzDyrIB5NddBdbUacvdZxfA9et-1o9sIdNPL5BTGd7ISZIRGcL8ZnU_1tbFPvCwaxYlgaJRr1R4Sjkh9UVE0AMJ-eMQiKP62hJOyPMZ6aocquIo5AmOQ04T8xjpP_ZSD-bm2kNKMBb6g7xx7_kv3uxgh01Oum20UJ7GSPT6mS6podUJhlRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DiDnebohs3oleEcIbrqjWuITzLdwZEkhM8w7I86Ll_pxpn-WPjDuo8osO8uOJv-nAv8l4cdYIocmMkzNs_32oco7zUurYIBZN4ozXPxuOKhfjV_9A8BkM_I62MNlFLknyPXf0geqV6kLpGxu293pfDJcYkRoCGd8yCbyJMBazhg_gfZJOWnEymuJWJ5WB14DxetVanT3qY-TXmBRqVexDHFzT0zfoNO0K4nXL3Le5MWoXBwnc9iWeAXrtSaR0iFNrZxubvbUsf6ArGshVmi1SXxMoARmO2DJcZTxf-f0k60ssztm8j_S04oPLbgQax0J0PlURqBWTm6rWMz2fj0pHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3PmJOuU9jL_w4td5A4ypojU5XeRMeEicg1wRM2lTFaNUh448xQv-2tZgHr3hSRYqwDGMlViq-PnpsGcLkiR8oAYZLHaMLGc5Y9yYiyv7pexA5bBMRZY5h4-LHLmYHqX5dwrkQJFPPOfSqkX_ZLxTt3gjM473fCnGiMbNbbAW5HUS64bq5AjEGsFX7KICrSEmJb0nGJflrACwufUVniBqJSDE6tmR2TapHKklgytCR6yfePYq19RiSV5-KQUVfMeU7La0wHGcDccHV6FPXhB4c_SKOlQnJ2GG8uKmpX_PVGp6jU6eOQD0qGQR-_Q8e5O7uvxgPo1eCtNIVlg825VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cT9XkySUflvuUc27Pb2QAB5TBF72GCRf_hPGZK9hXxTG5T_VW8hVNyoYP6gRX5s3LVgy3NsFqd32ZB_2ZjXcqIdtVUl2e1SRHE9pmzLmWFXA_lYdo-qNqxoHUIjUkAjRvs51_oTKIkRK0eiHhQ0IyPfED-f2WjJxTudjfsvT4d4XaVUiJqUXos1jzmboBOKAYcc49KSA7uRJbZ6Doa0nOGHlgBKrtCSP0Jgp9lVMD15SqOlj9bR5EKfSlS27xvtVHEBkZQTKKJrdBgEd2V1fID5TluKLJAINXhIe-7yv0Pf94mLukPkCr3BzjzRrgeLIyO71K1wrCZhVZj7iHWx_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=BhjJ6ImYm9MqASH_eHDpoHKiRRBbKwzfZjcAWeweAqcXXZE6JXSFmL9LVgER8Fehz8hn-5BvAhhgSbiNjn5Z2nvElmfn_7T8jgAVUNqPGi_6Lp-0gFiBAM9aL-JqJe8umHR9uSpzOwICFuX8mAdno_i88QCN_FLr3etrAJrovbfCGos1gnkkDezINzgtmVDFbyfVoyOzBUCIm4n9dDGcqxbt-NjH1Y1aPqEsDybUktB-Y-3bRFx4fuZ2nnqxu92ipNyyfrAE8WqfOeWcZZQCZ6VSFk_NcowkmsupC0TKWRhEsmJmFso_q3cmBNy6Jz8fp64vQukT7XJ2PY6IHAsjioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=BhjJ6ImYm9MqASH_eHDpoHKiRRBbKwzfZjcAWeweAqcXXZE6JXSFmL9LVgER8Fehz8hn-5BvAhhgSbiNjn5Z2nvElmfn_7T8jgAVUNqPGi_6Lp-0gFiBAM9aL-JqJe8umHR9uSpzOwICFuX8mAdno_i88QCN_FLr3etrAJrovbfCGos1gnkkDezINzgtmVDFbyfVoyOzBUCIm4n9dDGcqxbt-NjH1Y1aPqEsDybUktB-Y-3bRFx4fuZ2nnqxu92ipNyyfrAE8WqfOeWcZZQCZ6VSFk_NcowkmsupC0TKWRhEsmJmFso_q3cmBNy6Jz8fp64vQukT7XJ2PY6IHAsjioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9jCdAFfBRewhqXCQ79t0q8m97rZKQ9urSZk7uXJasDGbKIF6ZnbC0DlwHsyvx8ZKsqeQUWK_NUPCoRLQSMjRBkpwPO7JjNJucju_XuRu5FjZfmuYAZeUIaKsTFRIguqkpmvFe9fu0EI_0ZeGd_KIU155akPXnJEC02V6EYlhcntfDk2QTsifukAcoPYK0y0LtAS1rE2LyIyv9P-AcWETcSc-UYUKP896tXPpn4eUQ17bNvgBWBpoWMjPG2YA_cEIlwVQ7gzBvB8CQi59g_9PhrK5MLf6vl-UXECalqM2m1SJcnZU1PfHYsyC44Gi4Kf3N8StiXYMU7s7wCIxPrkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=oizt2fkYRi9mWD08DPC7SZGumfOnnUfnL3r-xbjLEiRjOJcLVixhiIS1CY39bzERF_eedd66oFNNW90JYJ4STmLrZ5oIacRgIVjCxG0vsk5s0Tu-gFaqpYbeLvbFz6U9eEgherixcpphktsHcG03vT94NT8sg5ODZUpn7o5PotPX6wdCRG_LzYydJleM_5XJzLsjga0hq0lL9Aa0sLD5mEt4gmPWLvnTHl6TlIGrRe9M12k4pcxB2kwe8-LDKuQJXLGz3awsdsKslfbceZfhEsuZAi-B2qLX4-hG1ZHIOuHNdBxguhOUNwBHjL2pXVRN6VsFUvCnZ-NMj9T1NJlfDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=oizt2fkYRi9mWD08DPC7SZGumfOnnUfnL3r-xbjLEiRjOJcLVixhiIS1CY39bzERF_eedd66oFNNW90JYJ4STmLrZ5oIacRgIVjCxG0vsk5s0Tu-gFaqpYbeLvbFz6U9eEgherixcpphktsHcG03vT94NT8sg5ODZUpn7o5PotPX6wdCRG_LzYydJleM_5XJzLsjga0hq0lL9Aa0sLD5mEt4gmPWLvnTHl6TlIGrRe9M12k4pcxB2kwe8-LDKuQJXLGz3awsdsKslfbceZfhEsuZAi-B2qLX4-hG1ZHIOuHNdBxguhOUNwBHjL2pXVRN6VsFUvCnZ-NMj9T1NJlfDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZyGCqkt66N4EUO7CBNS484jqbxZ5J74XL7VMdohrooThwfDIQ_fN7d_hsA2uyf7RqymNJ8gjMeOyogw7rCniywR4FD-7B0vA_c1ERRgnZ6b5WOCGgsRnutfmPg_Ja0MZ2P2q1YkY8HBR_DIRWp9b32QrPrw7qiNKN5fvaI0edJRYI4Yym_vYeF0nQED59OKUotKgXrwTW9aG_qtSZDf_EFoKbCAEd1zhJMeA6JVoJ1DbrJFFdpYETqB5NMRSZIIXohADQ5ny0TcJBLCSfiApoZTLw9xJnieS4sEw03Yp6VKA0QvthtsYMFicQ5qZgpe1I9tGJkrH7r_1HIcTrrMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=aSBoDiWNzX8NfBeeKtbeC0mDe4igjQh0dYVGsuwRKHHrhTD9uV9pk0SbOPGcO4h7zYXdHK4Xyxlp9VgCg_Ow4510c-tvCOOSFRoxwe7AOG9C1EXG9MeG_nJfQ3-SxvCe1Fk_Jkaa4s_LvqhetPgKGeoGgqQPSJJE-hi13fPFSdHIZA3PnrRAl08FJtwKl9dSZEz721Qk87ZzBGW3rOXhXgkwth0zt9BbN6if49sKo4unuwNXtu5_LJOZnMylTceF32538tdfPwnzbsqjX-Hc1ohQFUV3Tbn9TS9naz4GDur_TeaiZIknahgwhcP1eqpyXq5YuzZAE4qRu1J6wwEIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=aSBoDiWNzX8NfBeeKtbeC0mDe4igjQh0dYVGsuwRKHHrhTD9uV9pk0SbOPGcO4h7zYXdHK4Xyxlp9VgCg_Ow4510c-tvCOOSFRoxwe7AOG9C1EXG9MeG_nJfQ3-SxvCe1Fk_Jkaa4s_LvqhetPgKGeoGgqQPSJJE-hi13fPFSdHIZA3PnrRAl08FJtwKl9dSZEz721Qk87ZzBGW3rOXhXgkwth0zt9BbN6if49sKo4unuwNXtu5_LJOZnMylTceF32538tdfPwnzbsqjX-Hc1ohQFUV3Tbn9TS9naz4GDur_TeaiZIknahgwhcP1eqpyXq5YuzZAE4qRu1J6wwEIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YnweOm-LBw6xPLnyihrbhD3cawzRgwvVv17Qq4ZwIfasK4ziLeeTa-gNdx0DWW6Fo-27xqhcScdwVPNkFTELU1GNo9JpL_fOjHf2DiNEaEEDvdKCu5cSi0iBtxbywXB0iZO8LGY7K9KltV1E7yAvwlsNZXs3033xAomOBGDTz0WQ52pm4R_E1_RDm_5w69x6IN1sK4r8pIUytRrTN7_jbzzD8JirXLkhE9awPQuiRjf2dMCfkWZpE9hdzxHktwWwX7wcDJijQC1VvppOe5hRuY_8MH6bgW370yG-s51mAWZiOrIiWurfjo0-IRRFD4nN1cR1LyUxziS6lUXOG3_FGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uiNGvACIU4RHNBIq-bGsyYjqf2QIQZNcvIuNVM7qSw0u50nKgubRHJbXMATXVOdGVVo5p9UyGLBS-Kgf9Tptq24fQiLGr4xcppcWmu1VBvgmaEFUlZ1t91Z24-ekGhyMJR12cYmvtEkiJfAqdrq11hv5czlzKd9mbM0ZF6z_UTDT6x6F6fYvqlFPmX3jU73J6OAgt4uKsT9MYcjYVKkQxjXjVqxbbfxmQhiSLStgx-qgt-El4v9tAwTeZNeFCbftoj_XxpzmzHfDmGLhl03iIdVTqVEbtfQacEznbqAEjQBe8R6SFU_9LiDvW1zoOsnw31VPtsD7G_-nnpavg9ZMHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUJ3cqCzdj19ai5Tpe3o_ThzTs3BOmMc0wsDBxwWYcEQCQX6XwW5RvY6nQmddrO7LS9ndvswMU-_xA5y-uDioHwQv_DeBlnp6NJ0IKq66zaOLFJyHbG-pa2whmEfvsFVIF_53Sxbv0fB4JN7fSpl-meI6cqdZtRH9--URbyps-LHzE61SkAm1CFb86Z1FTmXx-IXwisEY6c-uxDu9tzsiUCEHtf3Vugfz3AcY_SDdD2lGHxGOfWs-WoC8aI_XuXSvffmAxP4X4W8UUcYgIjr9Ea25SwufxQHllhF5j9ACG2UTXDq-H_RJ2RXMXj3IvwimCyoz7pi3yLSIfwPFGEayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=L_TagGs65EYOhVu4ISNWeRybDB-sV47q8yy5Rrq4IuNYObq0Vp0BnQ8NwW8p7uzlZ_LFLR_eTGq0fb0nq_IuydembVtEfRAlj4mcXgp5bMC5SWTStdK46tTVRpcKQ_PDRh85Ob4BUA3bJwBZ6fRS0SizwmVuoP_RP-9jR2Z1l20cl3xWQo4z7MqlKm5I9DEM_xL-2B8HpSFNqpuYhA7susPCLyZ-mhcKFEzy4jMIHGP0xFgeKZofWDvk8ozkQ58RYRHDlx5UNOdP7Q6_zlfS89lx3s-R477BlEuuN17Vnf-rrrYeACEVxwpiNbXHQqHD-ocuHoleEwrBQ2yUZDMqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=L_TagGs65EYOhVu4ISNWeRybDB-sV47q8yy5Rrq4IuNYObq0Vp0BnQ8NwW8p7uzlZ_LFLR_eTGq0fb0nq_IuydembVtEfRAlj4mcXgp5bMC5SWTStdK46tTVRpcKQ_PDRh85Ob4BUA3bJwBZ6fRS0SizwmVuoP_RP-9jR2Z1l20cl3xWQo4z7MqlKm5I9DEM_xL-2B8HpSFNqpuYhA7susPCLyZ-mhcKFEzy4jMIHGP0xFgeKZofWDvk8ozkQ58RYRHDlx5UNOdP7Q6_zlfS89lx3s-R477BlEuuN17Vnf-rrrYeACEVxwpiNbXHQqHD-ocuHoleEwrBQ2yUZDMqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BV0VNm2BBEAz6WQ22sOUoMEHo-hEm94Eruu_4tm-Ls-ZsJxA4mx2rDAmT4S-E-N5oA6lVm7gLkPaJumh-cQOiXhDiZK3bd7B__0bAC0edLAqz3SP0U8BhCC_8Lee2VqoWWmO5hbT02kW8GLPTt2UeCMD9eU6F4echqNWV1m3KjUB3gQF2BLp66WcFlWAz6UUYF90UjOZWhJtPtI4H-JQwWRt8MoQdT7xPMKcv3l3AWi21LijVPg1_Y5Alf0UyAJepxdyUvebilCYxgBIFGPdXtVLkE8IUd_8I0YTKOHATIssOoNsTmMaLIM_I7QO_rJfVuIhjbTSGLmotlnsv1YyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBxZUtS9vKRsZ4czYnT3mksM5q9X4QDoZrkGe2bsJVWlYLAfoIb0BeUNF65HQGVO67EwtcCHZOQKdVUmWsToWXAFYQtDuCIMOI-s_ZFRifp6iC-Bxryka-8HDTclvlNhkYqirBtbkWSqfdGSTw70BuMlC7Dr24zDAuPUUn1RLicjxEnk_1RYNh8tXbJJFb9yWOsXu0YwRoLScS25ryAS_PnctAtoA3gyKhTCp5dNKw83GPiT29Nub9t2Dd8qdrxuY9IwjgwESbO1cqP5_Tt4_uPRWyyUPJZG8DoO7rwVOBUnNFxRG5WyQH6_aEuQkzq5XrTG8239TJ4Rycg3O-ovkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ملیکا همت‌زاده»، دختر ۱۳ ساله اهل روستای دسک شهرستان نیکشهر، پس از عقرب‌گزیدگی و در شرایطی که به گفته پدرش امکانات و داروی مورد نیاز برای درمان او در دسترس نبود، در بیمارستان نیکشهر  استان سیستان و بلوچستان جان باخت.
پدر ملیکا روایت کرده است: «فقط یک خانم دکتر آمد و گفت سرم می‌زنم و پس از تمام شدن سرم، او را به بیمارستان نیکشهر که مجهزتر است ببرید.»
با وجود وضعیت او، مرکز درمانی بنت آمبولانس نداشت و خانواده با خودروی شخصی مسیر ۷۵ کیلومتری تا نیکشهر را طی کردند و ساعت ۳:۳۰ عصر به بیمارستان رسیدند.
سعید همت‌زاده درباره ساعات بعدی گفته است بیمارستان نیکشهر نیز به دخترش سرم وصل کرد، اما پلاکت خون در اختیار نداشت.
بیمارستان چابهار نیز پلاکت نداشت و قرار شد آن را از ایرانشهر تهیه کنند: گفتند یکی دو ساعت طول می‌کشد. یکی دو ساعت شد پنج ساعت اما پلاکت به دست ما نرسید. تا ساعت ۱۰ شب منتظر ماندیم، اما به جز همان سرم، هیچ خدمات درمانی دیگری ارائه نشد.
ملیکا همت‌زاده سرانجام در اواسط شب بر اثر تاثیر سم عقرب دچار تشنج شد و جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=OakiGkKnAxGvZw8lYaAEwTcE4LcFZsStOxIvz33hTmpVm9A7RLWMq8k3vleD_1XSti4NDhzuy0aQ_RT4kKjovDWaIIk4cfAYHPPECWsdzvIPCNcorLUlh0j9HIILWV_jlIe68bB0yVS3cq8sXd_R0ClIizK40pHQQzTK9luomZ7KOVU_4ReZme5BHy5EprrygWpSsU89Gd0ZqVcIKS3DzaCbaTQogT14GOjZUNVbVUWrGU0Oe0ZnXmvKRsNAVjuOW9CEEzuKeY03bo0sK4Kx_SoHkFvt3mmfpfzxCfJu3wSsBLVeywQCpz-gkD4tBUwmaho098yTCwWCkzJhIUq1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=OakiGkKnAxGvZw8lYaAEwTcE4LcFZsStOxIvz33hTmpVm9A7RLWMq8k3vleD_1XSti4NDhzuy0aQ_RT4kKjovDWaIIk4cfAYHPPECWsdzvIPCNcorLUlh0j9HIILWV_jlIe68bB0yVS3cq8sXd_R0ClIizK40pHQQzTK9luomZ7KOVU_4ReZme5BHy5EprrygWpSsU89Gd0ZqVcIKS3DzaCbaTQogT14GOjZUNVbVUWrGU0Oe0ZnXmvKRsNAVjuOW9CEEzuKeY03bo0sK4Kx_SoHkFvt3mmfpfzxCfJu3wSsBLVeywQCpz-gkD4tBUwmaho098yTCwWCkzJhIUq1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=ngc2JB0vqvyGhPb0i7eK1xfjfmopYi1kbDS_RYwlvmvqM4ucjJBzCHI_OMV1c4I-eYElHdg959PLBx6flrzvyTBII-Cy5-M8Sz8Jp1WfE9lJ4bfZSiAGKtVsdlmB_FZ3G1fguSbbYTkVst8IViOCCbfGLaxsap3QUq4HHI0pQwmkwQq5-DvOuk1LmbA9RMNZonPlAdIjaUPKGEp-uq3SZoec9wMwcXqVDYKn-ChvXotXGuPzFqYlM1RUg-wC1KSrID3qVZnS-RX67nfpfWnvtYy97gWTWgFz8qetvIvReGRm-Vy_vtjcmfq8P5En6vxelNwKfxEQ-4abtFREn9ncZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=ngc2JB0vqvyGhPb0i7eK1xfjfmopYi1kbDS_RYwlvmvqM4ucjJBzCHI_OMV1c4I-eYElHdg959PLBx6flrzvyTBII-Cy5-M8Sz8Jp1WfE9lJ4bfZSiAGKtVsdlmB_FZ3G1fguSbbYTkVst8IViOCCbfGLaxsap3QUq4HHI0pQwmkwQq5-DvOuk1LmbA9RMNZonPlAdIjaUPKGEp-uq3SZoec9wMwcXqVDYKn-ChvXotXGuPzFqYlM1RUg-wC1KSrID3qVZnS-RX67nfpfWnvtYy97gWTWgFz8qetvIvReGRm-Vy_vtjcmfq8P5En6vxelNwKfxEQ-4abtFREn9ncZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر قالیباف تفاهم‌نامه میان ایران و آمریکا را «سند افتخار و پیروزی در عرصه دیپلماسی» توصیف کرد و تاکید کرد که ایالات متحده و اسرائیل در جنگ اخیر «به هیچ یک از اهداف خود دست نیافته‌اند» و تهران پیروز شده است.
قالیباف که در جلسه‌ای به مناسبت روز خبرنگار [در تقویم جمهوری اسلامی] صحبت می‌کرد گفت: «با تمام وجود اعلام می‌کنم که ما در این جنگ پیروز شدیم.»
او افزود: «در جنگی ناعادلانه به رهبری ایالات متحده و اسرائیل، ملت ما با قلبی باز و بدون انتظار هیچ چیز در ازای آن، شجاعانه ایستاد و جنگید.»
اظهارات قالیباف در حالی مطرح می‌شود که او جزئیاتی در مورد اهدافی که معتقد است واشنگتن و اورشلیم در دستیابی به آنها شکست خورده‌اند، ارائه نکرد.
@
VahidHeadline
قالیباف: ما نتوانستیم آن‌طور که باید این پیروزی بزرگ را روایت کنیم تا حس افتخار در ذهن و وجود همه مردم، جبهه مقاومت و آزادی‌خواهان دنیا شکل بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=aExzLF-lFE4lpahFEdHXCH7xhsYkrpaD975P3yBdKBhF-1685Pkaql-uALtXtUldf6zl38LhIcW1twHRYZdxMN8dRZ7o-DxG3RbJKPli4q4rzJGpVpWChBoulefIDVQsPIJTssCFeC2v73r2EhDU9KIOZcQJ3MErTrtPQxBM20Q2n67fY3exikA2F9qR_kaIDsq4_9ajjWLFIAmWNJcI7yKsXd3FWkJ6iUmoOH8S46QYZCggQmBclFjeQG-AjIL3SbM_yvpWYgEuZydq4cn2RSoyQmQc32E5KcInJtxCFsuD_OF-U6Zf5Pks7QiOMBNlESgwLF-wkys1HQLBpqje5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=aExzLF-lFE4lpahFEdHXCH7xhsYkrpaD975P3yBdKBhF-1685Pkaql-uALtXtUldf6zl38LhIcW1twHRYZdxMN8dRZ7o-DxG3RbJKPli4q4rzJGpVpWChBoulefIDVQsPIJTssCFeC2v73r2EhDU9KIOZcQJ3MErTrtPQxBM20Q2n67fY3exikA2F9qR_kaIDsq4_9ajjWLFIAmWNJcI7yKsXd3FWkJ6iUmoOH8S46QYZCggQmBclFjeQG-AjIL3SbM_yvpWYgEuZydq4cn2RSoyQmQc32E5KcInJtxCFsuD_OF-U6Zf5Pks7QiOMBNlESgwLF-wkys1HQLBpqje5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1wDibbZ6Q9lm-_YtJEWmrY5hdPMAO8Kk-OKoYf5AKteiyCs3_0OmP-bBPK_UCb401IEzUQEkg8b2pB9PjZOvn2_gWjpCTtv5C8YFhVpT4eM4duX-yFhCF97MR52butdxThespia843WzT7DaDrWQvQLNKasDjREEVTJvAuL2ZFMnA_iKBHVM_uu6AAgED5R6sXiKbSXech-8gaJel5RVDSz6pIWwMpWTFaTLHHo3s4pI52GmeBmDbCWAO5F0tzx1pOE2lzmkudKK73p9xQnAV8nevLXzEK2DLX2LdRAToEVsaZt7AAAgB1qof4kVDAE2ldnEE20sEkVjFSoXLsVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BW9fXscca41so5IsphakABySL37i2fwZXnIZBZYg9YmSuTji7haTwYBMstK-a2sYsPK3EHNGcbl7rU1Tnn1F6z1PdHUzlg-fZOz1znS7YlfiQYUhgWOXJewJBfwApOCJhUa_Lt9Z-BTBTC58knyO--bwUlRIJF4Xe_R-V055nC9elw45g-9H-ZdoxP2wlX7XzI3S2hK4B2mb8tU5NPwwLHhbRRMVXm6myPQby9WDEI-EK5CFRWIA9XfyYxAuXyMGkiOv8a_Z3QnvBcJHylY8VhtYBunKQ866mIGljpVlKkKugxHzPW-FS6-sD5PUmWSGf2im3BAiIlsC40k7Xk-csw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PW5QzkRvx1yMfnCMq9UPlS1CeFUxXYrXXzaU7GU_uEb8GkwbM0VaTJqAOlOjsQNT3lQha7_mnytgeLhgIrSVqTi1UpeExzSUshtAgHqUKI_sg4rP-0S413LdW7NnhMMHq8so6G81sAaxLfQOg4izsBFMvMuBMCKD-DIitZpYk0oVV-zUhjYowyKM_wb7A3mlEVs9T3ryOP78j0HKEOtlaNOrXzg70ej4WlLG3sAmFopujyGxkoOTKQkxCGJCyaw0qsh84zWeDU-B6W2-ybGN05UrtdTBWSAxzGY6pnIJMrc-4c6IHC2u9h3EpJ-68PKRIAcp7Umjc-DXvqpIwk6qgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdwzCSeV1IMDs-912doXAdt-iHl9YWKioOY7KfPd-Bf5nQHCC6EEHRO1wFer-eWwnsNglORROWqK7gpU-du0afHS_eEANK6uZqfhU4hNwifs8x833K00BK7or48BfWAagH1ASaF0Z4og9EJ_ru8_V6IDT3omzkoslPUkpOdgY047UD-Hwk2UMlp12rG88mqR65DLK4oyoCV743Ivg3KrNp9_78lZevSxpE5PxtXH59os27qf-SAk12j9fiTtQ9l72BPu-wIZJ29jcDlwdIYQmlIjVWp8mkdDK6BlZPG79K-MjMcbk-NE3_r9A9U5xoqPnRdpIF3TR6rzS9GvHzIRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMHzjvothDTp6fOJdPBSb8npq3hYSeg0bccUyTURjzEEBt1sh4ahqX8Bfrp2QJYCis1MNvbkmUvyUeKxfCiIY26oBD54BZjBglPKTsFiYXJXer3g8_R6z9Y0AQiuWEo-B1ZvdQ1bipG9zb04O1ajKxOMf54IMaVd3nacQuUkvvv9hLTuLPT4i0E07Y3bcaIdUCQGFd5VYj6-mjl-a3hjxy3kKRmvFbSuH2Pq-kujPsi5fxHBnJMKhf4YFIf0DLmeO7Hocbaq3zv_RRNdm5l_o9AVU2pPL7v21MiSCYCUiCI3vrDQFjoUTkDZYS02aOsqfH9LlHDCW-jhnkbpkIjTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZbMYp8AM6r4TWjXpfC2aEtyBPIy3z1uozNHvBpPSuVbJabmWTqymbP57aWZZNzSOh60ssxiO9148NycNz72gDjAz-30zrLDqDP3xotyBde1arwIbPWAXoSgppjQbL6rChEypeiq14cDFwb0yM0QrrqLxuqpoZ9x_6Lt80MLr-iFXC3G3VRdIzLwhPsp8uLeTy9AXUdPRj-IpTstTLiU4bngJ5wubsLm6t96LJT9OSAMWmQO74YRF7JovgsIlOIEOLclm7YN8txolUEMwARstFnSq1a2jsdZg6SJnXmjOvCs4B_4Pa_RFg4_eunYaIQREvk40bvW70EdnihC74uR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ-KYJ-6luIhV0_DZGpYjaXOhEU5ZEcMIjOm9Xcdix64G2zS9exzj7dCEvLV6PUKsO8_i8tNAA8b0O922LoQrUypj7DWSY78igPEXDaqbSnWQTahzMaFh6HjMs7QFXTGdxg6HkDd5Xpxt-U772MIOYVqp-zLKtIyz75hlNZO1NGraPKpq_MZW5MBzzLKh8iBdr7uQAuYn10SBPNqFVN8iF6yQxc81ddDEIFJz1ayHHcOg3bwEFY9T_EakRbV9m4sgKMyTfxDQseSt3yiVROsrTyG5_W8jlAr0R-sokLDaQdz1dxIKBXnF0_X-CAhrGQl15mYHqG4qrmlHjaWdqC58w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=VSiDKs9aXkZFt_QnN2yqxiMDyZzKXzuu-p2A-_E_8DkTkdjwz5n-Lv2WXyjNTKXW7LtBE7R8Z_eLG75G1VO3UPzKkrvCLx7I2ZAYOFdwz9IPBZXdUDFYKX77AtGW0q23AeZXHgwSF8rnn3XxrrgjbqOkk0YjLWeTKUHsTKzThia4UMuk9xzE3UPtxBveiGNSFrjdVQEoFjFxlVH2SpjXAqgbG7cITjQKBp83wPQTHJOGp1_Q89L2WqCNYa_d-7Y5Fh0FZtmXuN53Agz0-23oyguIoVI98n_XsoOjQX-QtAGy-5IIUTD3lQTXfQyq7zRbbTe9-o4jYDxGk8IsJC9i0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=VSiDKs9aXkZFt_QnN2yqxiMDyZzKXzuu-p2A-_E_8DkTkdjwz5n-Lv2WXyjNTKXW7LtBE7R8Z_eLG75G1VO3UPzKkrvCLx7I2ZAYOFdwz9IPBZXdUDFYKX77AtGW0q23AeZXHgwSF8rnn3XxrrgjbqOkk0YjLWeTKUHsTKzThia4UMuk9xzE3UPtxBveiGNSFrjdVQEoFjFxlVH2SpjXAqgbG7cITjQKBp83wPQTHJOGp1_Q89L2WqCNYa_d-7Y5Fh0FZtmXuN53Agz0-23oyguIoVI98n_XsoOjQX-QtAGy-5IIUTD3lQTXfQyq7zRbbTe9-o4jYDxGk8IsJC9i0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzdusfD3CxFAqxoa0LyWc9AK1_Jn5F_9l4A8MiMUpGloOaZAHSl6U1COW8qv_BSFjbB0VmU4PwHtf6e1uwgnL8ghKTixZ0ml6SN8nFbESIv3cb0Ei-NgAIr9YJl3KWhtOMDNV8pwv5zsjbF1h5fVbtHfiIz1SrzxNLwjqPYYx-7K6TeLwZNzPXCxCdGzoZZ6fiQLcLKFgCFqTJ8oBY1cQl1sCDp_xy9TouYEVcRtOqw9u-Q_Xkr7CD2wQ-8rVkjd4Y3k1_tZwpRPKRJfqjepQ21bVtoYw-Lu56lddTFU1-2RZepNVdmFbqJZ1T6DHG1FDaViSGIttnzwAB3VpWjGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZm8H1rsUgS4tcKF27EYuMh9uHBlasoIYSAgOVciCab2LimFH7XxEREVX2wOwES4cnLFRQ5vRqUaOQGiPJ_Jr2GlgdkyjQfWOZIm3-ES51mtyARZn1fvXWzyEivvdnjt_Zbls_5Mv6mKOWQlMa1kKga82uJenYJvMTugTrdvo9Ya3ucMlBlvpHKZINbTCfDztI9yxwmjobvL7tkaczuFXwxb3mqb0LVJ1DmiYwGu3yrKrh5w8GM3r9bKQJa4HYjOJ-8yApLfJShiVcHvvnv-mUHDIdiDalBEYS-8lg6nWxovhOv4rn58vFWLiAavqOW_sXeDlR24CeeiIcSG0Daoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0cDCYDYev5k8Xob_kqHYF8q46DJx3ruKz8r1ebk56fdaIOvZhoDGHSnpnyOQ-52xXDfiJAUOKNlZ-ifKkD62V7ZMsYn2NXDl9v2WHwXvjPPcNln6U4JwLeE1SgFHD_uxRwja3ZWLb-D2m0inl8hoMeptzlavxICbAAjKyWAAF_y4EutelpCtlD9KefDkt6KGaWqL9ak4QkITj7RLL9s06Jqsm_oS9Z07eqwiqWyUrnXUr0jSE9ZjwzVtEwQkMa53PIq15NRr1F82L2D7E86mxikHNw0rXeuPIBXBGhGL5Cyc_blPr4hLu0kl4GbGbtmUAlWJq5ofyIHzqVOskUzKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=flitbXAV_iQ1UKZMn9bjhb-kAIG-57bvoFopv0c1iUT3-4P4yMnW6QlqPw_sTU9iIxb9DPK1n-GjN1n4csa4voLur8WjQGzqUBKBBk9b19EgZ5Y3Sr00uu7zlNKjVCY7PEtKSbITGqSBXiQ1WtcPtordNLy1IOMAMm7_Qdg_F7QbLDw954SMmmjfZ012Kpiid_qicqGMZaGjqgBTD-MyQ85s7t0zsahC2fBHuXWUgZLixTGe79wrQJU5nTPtL_OEquLVMy0QHzRypL-3PjqI12tEf6XmRekngztii1yLJTVoFNWZzPKinP8BkKZIvZP8RKku9eZkND3Ghe7Yl6YboQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=flitbXAV_iQ1UKZMn9bjhb-kAIG-57bvoFopv0c1iUT3-4P4yMnW6QlqPw_sTU9iIxb9DPK1n-GjN1n4csa4voLur8WjQGzqUBKBBk9b19EgZ5Y3Sr00uu7zlNKjVCY7PEtKSbITGqSBXiQ1WtcPtordNLy1IOMAMm7_Qdg_F7QbLDw954SMmmjfZ012Kpiid_qicqGMZaGjqgBTD-MyQ85s7t0zsahC2fBHuXWUgZLixTGe79wrQJU5nTPtL_OEquLVMy0QHzRypL-3PjqI12tEf6XmRekngztii1yLJTVoFNWZzPKinP8BkKZIvZP8RKku9eZkND3Ghe7Yl6YboQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rSzDmdau19Ad0eCGC2Qcj7rzRFSOW1_QNjPo7QawK4HunAK6mnLqp18QBvPxt5hR1mrv_NKHK0u7ZXyh-3aBIrswbHCanHTC_qGotR96wYXfJLISK8H-iqXVKqZN9cuTkM3tr0rjyC0WylgkmQIshWwuGtB-INXOI2aF4pgKA2wVYjL5uamGTifH6Ko_-wYPw3YAFC8jX0WFOllpY-5L6YdeMUSJfA9f_2XF3vTpHlBwx8-jbTfoS0R4zYuJYNRXRxsR6zL5m4BVf94UBxmQg_ZhPwTfCLhMWJUuoHXnTUnSvXj7Qu5pfrxPoYVuEPG2ToOCp4dIcqiVZSOZIck39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EhW_7Ji-sITljB8uAvudarFSaQSc7FyW99FI2JAUj4sSyovX7P2QHq2brjp8wPU1m5Mp5EOtac5vwBrSRGkRis_OliQ1Y0JCLGNRwyUq9ITgnK7Oze4yNl13KlPt8rGcc2656Cv6Kes9_tQTiIliWW67-TWEM06xERHWVf9EeVdalpNsII0qAWkaU0jiSCV12xmdWl7j3INfo1nuQWjHmkYyaKM9Sf-Z5-2IOcTUEjvrGlILJgYuQiwFemnfp4jlUgpcKxdlhBafUwNLqIAKSLSm-1pPFZNPHBGol4y73uaYc6YjR2qGjO3shjibqtP4TAmoAe_Uxuc0bvVnwyiXFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iodlUNS6ve-hCSmjYmLXalWYTO26uJNO9CeR78aFLMbpngvm0trkkgUqk5fLc5PcgvL_SMNmpjZhi9Ci7ZcqAVc_CERuZdY5sXWbYUZdXuPcqBeC0SREgETOSrPzC904dka-xPYjvYge08NNAKvuHu4zGY8nNJBxYTzeeLeNAX18quXma7c79MAAjAVTnsjrTUjVF8zAkU3o8EFOjpj4hBIBrWQ7DSRfwxufyleNBjPk-XvLtJmOH70vJmUT1PYkbfQocQ-VsC0LOlB9DsetI-0h6nSeJYgUeLwVx_40vovixMWK8WX6w4JuOAWLTt26xWjft4SjpPWEbOn_gCDv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fq-Qygq2ncNaU2eyAP-uYLXxxszAeTHk7w-bXdEGI0iCq5OU78J41u4y5W729jZXj6yx3Itd1JnmuvunvNTJNdShlxnVwP_0cczLQzBZ3h92gzjS2VImoZfBXfc8TXF3exni-swwlt9WO7oRic1UZjTp1BTF0bo2mWDjrs99_fVTGJXHFNczeXx9g1O46jU7YQjE0WNzLkD_2JKviitihoPePLHCu1K8KaN7Rgwl-KNpZLZtb3K27dt1XsLWJ0Ohug2Xo_gl_9FrKuJET9b0S51QGSfdwJRjiqeISX3prROMiIrJaaK5Hn3vbnndsuCExT58LrPGpws7_xR0E0jysg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=FLZLoZYtkrC84OVxGo9AnxQYKUfJaCFvq5N6wpVYuSZSn4IwKPvYXhuBecDfuxFhpmTOHWLGuHpARiAdkWgNwSej-H3fzL4MXFUYEhmfq_HUqYhP-VJUbXBWB91ktyWa_BVE0Nj0LYhQ29-1pEeB23uFZZJh-aSElpL0qg8XLMra3MYqwIHfqFLXzKPYsiL_NV86Afa7eclIeee5T6dXgkkX4HB6uDPQCLv32J9zgVKEyFzqUpntSHqqrNLUisqcPdGgRErnC6pL0Q1yHQ5iCpjTxsekd3Vmd2gt0Sm9Q9CSbYWnP-eeJPDCPxV6XESss1-0EoRhp4qGPPEnIMeg3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=FLZLoZYtkrC84OVxGo9AnxQYKUfJaCFvq5N6wpVYuSZSn4IwKPvYXhuBecDfuxFhpmTOHWLGuHpARiAdkWgNwSej-H3fzL4MXFUYEhmfq_HUqYhP-VJUbXBWB91ktyWa_BVE0Nj0LYhQ29-1pEeB23uFZZJh-aSElpL0qg8XLMra3MYqwIHfqFLXzKPYsiL_NV86Afa7eclIeee5T6dXgkkX4HB6uDPQCLv32J9zgVKEyFzqUpntSHqqrNLUisqcPdGgRErnC6pL0Q1yHQ5iCpjTxsekd3Vmd2gt0Sm9Q9CSbYWnP-eeJPDCPxV6XESss1-0EoRhp4qGPPEnIMeg3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ddPl0p1JSw9JJTQK1vsEcAIWG2Y6rMwE5_QPi25HXOTuKcTJqPmxp3k6yBeJq-T3VodvThF9XpGnf_0DUU4zY3hhtNbaTlFI6h89Tc396fuYw7dV2gpQiQN2hFahHGCrMYuwSPSydRJU8yvHnTJaLQQH-YUn-eFQkyona1dk4hreX7y-dMxpc__kZQtHmTDGiDZgXCUGFLU5Pk30Gac3In6BVyOKLmfQvMpwayvCPQFasJAUzgDtMfNK07nUsFbgvtWLzUVHUoqKFRhc0x10ZF0a-1KUoDMBclgyl7XGxO2DOxlM1bncQCzEs7do63KpCfg1XWS--LUFwkFsWIDKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UHJQeuqEIdNblMrmxz400-1z4FhXh4MGqX34bxRN1JnmO89sCzKJlMxK_3hmzQypC_6IAEm16NYaqzZ_PVQZ7nh6MFQFdaSj9f3HERs9pix9_rGdPo-ekEac_8NwDsBQRYzbrFmh1oY-TSgLNOxBDn0GYmn_kGsKKaOpQJnsB7zKc4rEGML9EdrIz7mxtWcFbdufUrwR9oFTGaBjCOCO_zJE0G76G3ArbCQeSyRW1adIPvpgh7z1e4hX72CdOGnGQKR7RwNipNhPGxoPk90yG9yF8KIoAFjx-w-Y9N6M6k_K8Jdn4UO3OLIpztMk1BJTo20eByCJFriWX37uJr7tyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gL8Z9CDqLhI_b6Nz3ghprtK17IN6sjKG7W7nFtbU6VNxsi0S8oUPfeBywUnGAkqqw5g8dmjEDHECbuNYoo9qlxs8PrlOflh8P82tk6Hd-jCvcTU03rD7CdRhrkDI83X9xH8REnxXNjip_XmfgTB0Sji5eAyOzHNaBiCZWQVdvzOfqt1dFVI76jbybuv-1UnJPKrnNiJF__2tsFCV3C0gzKkuv5szEFrCzLgp_ovlXUpdIlNi1RIySlrQ8Jl4tnQOjZD_w_MV8FNr5xnqZ7m0Pb42oI5ZQBEf6OnIBXSQV63AyEI9AmbAEwF7i-9eR1Cdm-7ddZxGg_siu5qEfSqEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QQN3Q3xFJ28vWUA3odrFIJTKtclc0BTw6LLZX9SAyI5qhZVpFP_BcMP6w_jTEBf089UQeTHTlnLhJFO7MOY_cxHRKHC4Iemfhh3TeeIWjeUkAgV9OWLHI8cltnPVBROq0u9pC1XKvGaHd7AA8KgGEq25vTH4ONgFeJ-n1ZjWpYoUauOfgWlSkFUcFvL3gJv7jROWGT-eJqceDkfcliGkgJX6ypg8IVBA9WDQOFZ4HFJHg_SxcMMunnxR5hkgrga5f27EmVR_RmOudhXsXIKA50thUA5_URYJ0uoygk8ZOWCf9PC7JYBM_2hx3KpBwntU5SrVedca8wnUGv55eymz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tzfcELdzSRWro7TBjEyVfbmXIOmmhoqL5OhOV2tEJtkH4Ipgbw6vuGUQN1JbTt-bp03jEvMVCpvBPxr5tb6jGkDp2-22t7LVNlDjHARqdSLqaI7Pb5t7SxbAmJg7ZqkF0w3gKFxmrFqShVDGCJfMyr8-5hJEWCS0qe9gwhHTVgUMy8EPp7I-Xqm-hhIu4p3VgP5Oyg5XskTdUKUvrrS_6A3EBC8xNo3eKqisrUh0wdm-q_ordQYxslJ7oHTkZb54QOPi5yBfLm2WFFGGOmt4hUM88zX-cyWkD4l8QKzKI-vJLfjv_ZuLSM51X01smaqnfNmWZusADNaPMbaIiT_Wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/plKBVWA280VkIEZa51r6z8h1ouJN5A2YaFEDJFfaNSd2w-Z-Fpuvoq4zl6f76QWiLaifVtA9NfB-2h6kqGCzx9rGUf8vFrbfT4tcykl59Mp6Z1IwGkTRk8RTznloxa1gZSVSb-xmevK8-bWp5LjzA8rse4YOC93sKZOqwZGgKFXTBeppYjFFpeYC8X1wtdCmgiaZoPcbYEqhdaD7QXG04HoHcezjotyh-5lIg6ZddfsStDjnC1sppUcsakyXsQQTbkkadQ4xCrsdoS4Jq4aiGLm21rB7HitAv1p-qxFtPEWizA3wGFfK8XiNV3paxj3IbI7nqSYM6bCDFR2eMz5RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gHEbJCSRG3bbfxKiv_4A7Vv77_b1xN3xKAjUMo7yvsKtNo2DxlpLD94hkT1Q2scAt6YqGKKvqq_txpegPIEf8FsjAqs66JwWBzxdPjtj7zHdFt9cu4t9GKClP0-uNMlB4UqfLIpKO2oiHWNBBgFo5cjGsNuPHUANbTgUIOauBLGz-bvEj-LVyDQz7LW_CzlVWI448W3PtubICtlt7yy3wv45i3otD-0_Q-ZJokuIbVLUCwrr51JQ8J4l0WrR0OGNwvXiuOZvpiaCIe0xQZsTdyjYfV0wjDBJZAHJKD7oQ75vVcuIoshoAQ7OZ0xOTwyZktf0NKPsgX7C5WxgjvKcEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vmNHthtwsCNy4SObai8kal_QZN3hHIgH2qlCL9C9D-c2m7OFTMtoXvGYJTl41aarHlbE0axLg9gFwm8_thuXT8Lts48YzcVM3pfJGdM8mWXimSfdvQVxHJFpB4qsm_9ddQF5NsF73c2uxpS9p5J9hJpRMyX7pMEXV46QuljeXzfboyVnSbelsXX5UCzg95lL0bmN0yYL827LGaVveti6k6CRurv0JKqYffFRrtjBBm4D0etEBTXTo3WoPuCC5jTS0WwCuuHtBdXntSeSfS5MtSFcuBUfMBlxiswK6BDWmouS5WveheNCxG9EMuvk1mVKpGH4h-PEUfcq5Xa39Bp-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qe6qIwVdi6oY6V54zojNKQ3wjRorRIHyYXw6JQXXOr_u-zLMF-EgM_Oj6PPCoXZtYf4Gw5yHRuSmGvuSYqUMowZ__8NHU__pa5K8Uyx51TCQsb4j3T3hnmWyRCGZupooUYc3dtrzTLp4du4hLRldTckSNR77odVtpt069gAo7nvFSVSiBPPpFjC_OEFsKJy1MKCKJE8gqpkxzhqBM_pJG69aeFzwxVX6NBoBTNzbCQFZNOV4yATvcfrgz4CVjp8B_CCGzDFhtSij6QddSdxCNGIBoV-z1eaNX5gLU1y7xlKfj5XFlxbdEs1qpqEiR4vW71HFfQ2nenPkMESPBS6XaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gI7-f16dT-iuTlWqvwcvWI75RXiihmpjfP2CnF-k7yGp1bXVh48CXKA_YEWqO_5bFT5gIFWVeh04R0X7dAPY3LUPVcOzOukFIMQhtROZELgcACOnUQTNbE2tbxwA6X8z8z2kA_CjKhDNbftUOrHELBBkuQhs-isKAtwyfQat8-FPMw9krP7pEgeVmVaOf-EzsBkZNikOG1V4uryssnMqZnh7Ic2WpsdKxFyo22rucg4V-fyeeilhYD8sSJv7mtalP3PxOCItYFPTNA6V1Lvzuyp5zqoNrOcl8rUKAswDtnF8F8AMTpx7T_vYsdeD-Rn0EPb4ckoMQ4vs1hn526_jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eRrhn53y85tomqzrLsY0tZoRWh9zlFPbG4Ky_JzyF8tA_iWvG9DkYmWAmpCCTwBrXLCoqkh8F4KLMcwGLvkGFxx3KeomGb4XgSSOEL695FANS6UGvwC_iV681_KnMHGB4s0HygpepvQ4PnZNXnplevEKWhQfs0coXFhGe2TG7uRkXQII54xE0qY-8tekZmn8DriZ2FXaWCKLyiUgxzupGyyHog2HQHy0ysRxCCTLPymLCukV45s_SinU0ln-syP64-j3a39SmYY6q4Q1BYqN21SVR424soFxXVYSrzKnRExWornn2DxKBu8hirBwPRb93tuUy-OtmHtP4mkChVpigg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=MGCxC_bKaOZDMAFBGpZomqmiGmxv0cYpyJ8K6UoyDoaJ7K97Ejzf-Rq7J9euoTkcLEUhD9el_lg_9CPrZ22JBrGLcQwy_4M6oaS8ps7vg-XByH4me_O7LT2j30LcyuFqeNIHQ56hSYop8V28lWOocn2wKoNyqOods9Xuvq4UPI62f3A62MiKpEoBwKQm7-56w5wBgxBj_UZajZd46ASuqWLLT31esRgi6cpHA784dA93wU0dtf6NCauB_66UK84E1mBteocO6R-9mofpq89E5XFkFjM3QvyvnMB2KYUgvuFt_loHkdvy_OrmqSNPnhpxzB-377vCWRjkxz05lX1_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=MGCxC_bKaOZDMAFBGpZomqmiGmxv0cYpyJ8K6UoyDoaJ7K97Ejzf-Rq7J9euoTkcLEUhD9el_lg_9CPrZ22JBrGLcQwy_4M6oaS8ps7vg-XByH4me_O7LT2j30LcyuFqeNIHQ56hSYop8V28lWOocn2wKoNyqOods9Xuvq4UPI62f3A62MiKpEoBwKQm7-56w5wBgxBj_UZajZd46ASuqWLLT31esRgi6cpHA784dA93wU0dtf6NCauB_66UK84E1mBteocO6R-9mofpq89E5XFkFjM3QvyvnMB2KYUgvuFt_loHkdvy_OrmqSNPnhpxzB-377vCWRjkxz05lX1_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JxnAhm0gTNEqSMarvijp1-7yiao6go44DHAoBP2pw9lQ6cVWQ0RqGkmWBxPdOdycdJ8s4nBiL3Sk5n1StS-pR2My6osoADd9P2Rn7GCcrLmYDnOyJAo4B7O2NCmrLwQaiSyRWumDk9tBEdXBjYOSwt-Mr_2GSFUoVX-gg4Fj1PKuO_OLNe7zYZGE-69U8Crxvd__2GAPyUkL1nPemyMfI9U5hO9LdgQKSebQ8efhI33i7n9ZORPLNuHwHarucpUfy5Soa6AincdMmm6vCXrSDDj9rLQUW1zKL7uz5Mbpxm3sY_zcgj7G-53FmfzlGPaUtb2qgsumEqKYZXNpgadLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r92WuLSjUEltiMFAX-jTDDsYIOt0pVAFhynGcURcfiqdQ7i44a7MjBxhQLj_XXem2hpgRZ4WmUBURH8H8_dcZ-LX4nGshIi-TIMLg1FW_KjtDWrZutWmukWCAzuXLgweTkvczU8Pb_-tvq8HLW24zc0DULQANf0m7tHOfHBm4kM4eHfEUSxbXqDKNIhq8V1aHvhVBeXEfId3KwkGev0Nqx3WsVytxbtmonTO3c6Uikw0SI-IdvOCvMNWI9Yh4iq6kyhJtMGIpwrhleqqvMy8fPDJTbpBFlhq6AdtLcNaWRmqA9dpGeK0v3dWXGSivm1E-s24xljYr9QKXFs45EvT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JR-6SfL8Rb35GolinIse_A3nlwtH2USfBODDPXOX8a5oC3d7UkNkSXYsmf2RzLgaDc9NOub2fXyd_VCDjr4hNANw1eoJ0c8NgQD-WTi_7kRk15g_kjEQr0wMngFUPtsi5DNImqVZ4FViNLXWg2A5uL-CLuNw7u31hA4pk8P-mwlOvH86NAEMPH4IDQ-J2_JTZiUW9N7uEXmBakqNbNgN2PmwXBCldmBhnrLsZJTkq7GNVFeM3wlUXoTdIiiQm4d1KhoJYfxVkarsUHMzG6q9_C1HtpWEtaR3KXZHbEEiTJFRLWxpk_78il0deL2fw73Vxv_M8C1W4AFPkAQPgsh8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=kQv50bYMWcc9gNkvcpgq3f2RfIxfwt-m8KPOid5rmAJLdZ5nyZT6MZn6v2pdZGZ2NUPq9zkn0txG2Wsrhax_jBxRXg4zjXytuMuuDCBgJLqJEmom-vqtp5Uzx3PTuEYWDb5WsyNfC-0vz3d20tazplF99n1N9Lfl0Le7wg_6dad4N3LM-UrjltM0jYB2P3uqWWgGWk9SJzTtYS_6SH3F0pOl75YL_0Lo2qr-PtqA2jrfhY6jYPJDfSipAlodSagLGnbUJ9gMQldsZnMHPv6Khjnt51hREol4abxrR1sR0anwkyN4OHUWdoObsPPe-XlbkounWKfBxHyI3T2lmsZSeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=kQv50bYMWcc9gNkvcpgq3f2RfIxfwt-m8KPOid5rmAJLdZ5nyZT6MZn6v2pdZGZ2NUPq9zkn0txG2Wsrhax_jBxRXg4zjXytuMuuDCBgJLqJEmom-vqtp5Uzx3PTuEYWDb5WsyNfC-0vz3d20tazplF99n1N9Lfl0Le7wg_6dad4N3LM-UrjltM0jYB2P3uqWWgGWk9SJzTtYS_6SH3F0pOl75YL_0Lo2qr-PtqA2jrfhY6jYPJDfSipAlodSagLGnbUJ9gMQldsZnMHPv6Khjnt51hREol4abxrR1sR0anwkyN4OHUWdoObsPPe-XlbkounWKfBxHyI3T2lmsZSeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=ufuc8KiAELtaKqJQFAziaCgxlMnJG1lIkS83eHyQwR57xzsmgzIevL6-N-Yg1KCKIx_Mj_kYgdSN1IGfQKhYJU_E88N49g3m1GApVJYd6otZYG9hKmWZeiv84wE7VW8iPDNZFs1romPB8y8YnOsUorVUUM-VsbKff_iI33Uo1KLQM41v_ZePjerrGTvrAapYhydrUbwiwWQEnaIbkoYDgaBES0MIHSyHdnnmo-hix1Wj9Zr2_3ItvMEQGCmxJNrqPKNRXk3fBrZeAh90ZCXNFG413Gp4iit71y-hMZsMid3SajpVRKki-4QknxNWzEFwnTYRvUxO7Xz8RMem6DBabg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=ufuc8KiAELtaKqJQFAziaCgxlMnJG1lIkS83eHyQwR57xzsmgzIevL6-N-Yg1KCKIx_Mj_kYgdSN1IGfQKhYJU_E88N49g3m1GApVJYd6otZYG9hKmWZeiv84wE7VW8iPDNZFs1romPB8y8YnOsUorVUUM-VsbKff_iI33Uo1KLQM41v_ZePjerrGTvrAapYhydrUbwiwWQEnaIbkoYDgaBES0MIHSyHdnnmo-hix1Wj9Zr2_3ItvMEQGCmxJNrqPKNRXk3fBrZeAh90ZCXNFG413Gp4iit71y-hMZsMid3SajpVRKki-4QknxNWzEFwnTYRvUxO7Xz8RMem6DBabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
