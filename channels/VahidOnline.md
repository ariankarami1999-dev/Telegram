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
<img src="https://cdn1.telesco.pe/file/t9t34FtENX5UNAiXcqV1S_e-eMFvMzDxaYxfHUI0ryeeWQj101UxzKbnndU8mSC8iq-3k0W_u-K3e0JKaXuyC9O-FlYCpyRRout2nshnMb7gmZ0L9dxOANZtuDim2G2CItN0irARZ8jCNl8ARxd67gt-Gvo4xyM_aArwKE2yJMeM3nyFK6qggW3lh_KZ2UzfVvljZDVj5zVGiiZa4DZOabMxbit5TFnIO8_8JcpiG_ak2Cvced2-QDUtkycXxgMyhl0Cav5rB1Mhj3Bw5YJzNvQNvBmpqR9Qp9YtdHK-sOvoTsZFN9cfb13YUu-FJwoZyDye2jOVNrO3y_ORc83kqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KrLlgvSzf0JMzHGuwoSKhGjbsPD-AH0TrQtTPE6rokSfkrg8ntZT_07raUTI_9g0LmBPgR_2qUcruL3wlWljlr_aLWez5UfiECyhXWrpmjmQRQAeps5EPjnt0G9rsJhdW93K_5z7phmPjbXUhyZny0mJDnMEebjMncECcsSZNKVYYOwyROvu9ybLmDCCsflUoYauyBSZXOUEV5EOz6JRrDlpj0f1OGwX2kHI920662Nz13DWGqDJkoM8RN7kbiPkUh-yl9MHwqH9cuZWV8ts2jF9ec2XEwyo1ejRdKE9YZmM79ItpujhSnG1KNdM_E2LsKKU1mq-8rZTW4iddtyneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در قعر دریا آرمیده است، و نیروی هوایی‌اش دیگر در میان ما نیست، و اگر تمام ارتشش از تهران خارج شود، سلاح‌ها را زمین بیندازد و دست‌ها را بالا بگیرد، هرکدام فریاد بزنند «تسلیمم، تسلیمم» و در حالی‌ که پرچم سفیدِ نمادین را دیوانه‌وار تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال (وال‌استریت ژورنال!)، سی‌ان‌انِ فاسد و اکنون بی‌اهمیت، و همه دیگر اعضای رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و حتی رقابت نزدیکی هم نبود.
دموکرات‌های احمق و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
پرزیدنت دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/VahidOnline/75540" target="_blank">📅 20:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ileLRG9T0lYNPzk2zBBZ1k4Gy-6MYChDWrIjanxIh_V2tUDXGfq-f8Yd7QQt8BbVp-cyTjZ4pq7sZa4MHitQXk13U5PBIEC7fGW-YGmr7aCaNfSqGDraymy1HyPNfRupvcQDrP5ZZPvin7AmDwjIoEotOlPYP90KipLlMd6rO3lZ5g92K5oHsavojqVy35Xtu1v03mNzRRGS_nutf8XgetuTnSLzxtcDDC19LdnHY4rwaDRfVfBtXVdKVy1bkqf6zqpTk6OEZD5IC9VnqphdNfiWJwbc2o8UZamJ2IAOffA6zp0DBK7RKQbau4o0OLuR4v9pS75kNGOWgInPyWRfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر مرکز روابط عمومی وزارت بهداشت جمهوری اسلامی، روز دوشنبه ۲۸ اردیبهشت مدعی شد که در حمله اسراییل به بیت خامنه‌ای «اتفاق خاصی» برای مجتبی خامنه‌ای نیفتاده و زخم‌های او نه چهره‌اش را مخدوش کرده و نه به قطع عضو انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/VahidOnline/75539" target="_blank">📅 19:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMVc2Ne4To0nG0A73Pq6CPMyeT26p7WfLCdhm0o89Zv8dYiu_cjp64lKp7_6wOcFL18LP8sdyimJECkD8mHTMgcHHOXq_EtPlTKX7UBfoYEOHc9ltWf5LPz_SXb24Ya6K_XdS0JBhnB_HX-OcgEQF826uft2O6rnn94rfWSJMN_NETbHHuJlN2CvbYHA8ZBp19ZEDvo8N844f87YE9sv1ov7htplCQ_VYcCqZleNNbn67QihVsHfcfZ-UojzE-3KyrTW8WyFhkr7XSrLeJkMUdHKxDKDLacGEFBerDgJ8T-50ciFLMX48jfGCqpbvNQ7TWvs44UV_ziWjY0wCTUMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردریش مرتس گفت که «ما حملات هوایی تازه ایران به امارات و دیگر شرکا را به‌شدت محکوم می‌کنیم.»
صدر‌اعظم آلمان در شبکه اجتماعی ایکس، حمله به «تاسیسات هسته‌ای» را تهدیدی برای ایمنی مردم سراسر منطقه خواند.
امارات متحده دیروز گفت که در حمله پهپادی، ژانراتور برق بیرون محوطه نیروگاه هسته‌ای براکه در نزدیکی ابوظبی آتش گرفته است. امارات در بیانیه‌هایش نامی از کشوری نبرد و فقط گفت پهپاد از «مرز غربی» وارد شده بود.
آقای مرتس در این پست نوشت که «ایران باید وارد مذاکره جدی با آمریکا شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون هیچ محدودیتی مجددا باز کند.»
اظهارات آقای مرتس درباره مذاکرات ایران و آمریکا اخیرا به تنش لفظی او با دونالد ترامپ منجر شد. او گفته بود مذاکره‌کنندگان ایران آمریکا را «تحقیر» کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/VahidOnline/75538" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dUxJ2TCCkSqBPVkA6QoFRNMTlj9S1KhtwxGk0ixUZs1i1bMEC9Sxu9KmCn527MI5pwH1-tJ1b8cSli3lITsRdI2Sjkonq2FUlyTsWCDL8nLqd7xoOiRj17950njVDeX-iX9YtQQC5RhvbpWwuxdMkVh_8QjOOzT9aDnXw6SPSi3iflIztS6-CoQEV-d041r_WVlKBdhjpotSq4A3eNgo8rTiHhXJQP8n_tnvvpzssLK3Z2cTPIrOXUFLaXpJVOqotwa6meVXQhVlOQLdKpP4DdfbGeZfazZAo-eIl1NGotMivgrBsLLbX4rTXQRCvRRsAVUVrNje8RhSWzVxGZxOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YewKo7eJF6pssuIz1u3l8GgObuGwvBw6091xLP1gPSzMvSHv0IcLj_ZutE6TXjqri8f86UJLKPONlCTlcRlSYqz4GpVu6wh4Dd2jcYCShoTmbJpYopNsr0HbaBVYaXPQC39bjxexU2ivNu1-g5zhSzkllTt_fy1bcuBqZeIrklMB35svdWnj2nNpcA1FUzpLwsF31asGWLoevoKWyEYkDp99e8y-_4la0X-k558WyfgL1XMeLipQhyZB3tuUi2WQGFDqPpC2ISL13oUYYGZw6Q-KjLE14TN_KRKajP1bl7JWZnCCZiI-3vugMTa91iVKF4g1NBGxkipmBphvLbLfWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت ماه به نقل از «یک منبع نزدیک به تیم مذاکره‌کننده» جمهوری اسلامی نوشت که تهران «جدیدترین متن خود را در ۱۴ بند به واسطه پاکستانی تحویل داده است و میانجی پاکستانی آن را به آمریکایی‌ها ارائه می‌کند.»
ساعتی پیش از انتشار این خبر رویترز به نقل از یک مقام پاکستانی گزارش کرده بود که اسلام‌آباد یکشنبه شب طرح پیشنهادی اصلاح‌شده جمهوری اسلامی ایران را به واشنگتن تحویل داده است.
@
VahidOOnLine
خبرگزاری العربیه، روز دوشنبه ۲۸ اردیبهشت ماه، بر اساس «جزئیات درزکرده» از آخرین نسخه پیشنهادی ایران به آمریکا، از مجموعه‌ای از خواسته‌ها و پیشنهادهای تازه تهران که بر آتش‌بس، تنگه هرمز و پرونده هسته‌ای تمرکز دارد، خبر داد.
طبق این گزارش، ایران خواستار یک آتش‌بس طولانی‌مدت و چندمرحله‌ای شده و همچنین درخواست کرده بازگشایی تنگه هرمز به‌صورت تدریجی و با تضمین‌های امنیتی انجام شود.
بر پایه این اطلاعات، تهران به‌جای برچیدن کامل برنامه هسته‌ای، با یک توقف طولانی‌مدت فعالیت‌های هسته‌ای موافقت کرده است. همچنین پیشنهاد شده انتقال ذخایر اورانیوم غنی‌شده به‌جای آمریکا، به‌صورت مشروط به روسیه انجام شود.
العربیه همچنین گزارش داده ایران از مطالبه دریافت غرامت عقب‌نشینی کرده، اما به‌جای آن خواستار تسهیلات و امتیازات اقتصادی شده است.
بر اساس این گزارش، ایران همچنین خواهان دریافت چندین تضمین بین‌المللی برای هرگونه توافق احتمالی است و تلاش دارد پرونده دریایی و موضوع تنگه هرمز را از پیچیدگی‌های مربوط به مذاکرات هسته‌ای جدا کند.
در بخش دیگری از این گزارش آمده است تهران خواستار نقش‌آفرینی پاکستان و عمان در مدیریت هرگونه تنش یا اصطکاک احتمالی در تنگه هرمز شده و همچنین بر استفاده از ادبیات و چارچوب سیاسی‌ای تاکید دارد که امکان «حفظ وجهه سیاسی جمهوری اسلامی» را فراهم کند
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/VahidOnline/75536" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDeXMpTGV0SZjmRTClakWGDiR0BjP4zwQAl_MrH0t4SKTV-uQ0J5NzUR-cQF65tg488Qsaplgz14S7vf6-HJDYCW-3liZVUu_ag7ayEU3yh3O1A93PD32doSaekHEIkORVluTNPgyOZ8yIsHnS30rJAfApKWKZc0q13lYXYKObnL8LPbs0U5hPdBwmwVG4xXmUtksxZDKt9v-wYz6D7kf1W3ivY7FeljjqGk8jS0yGLkVd3vnSRxhplByyXgjMo6GjQLxmYybg2ymQsVvD5N8tI20Q-e2hCxVI0NCLnwtwZjkNerN8XtQuyTUxd_iW8plRXsHD-4bZVmuTBqZWNkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری تسنیم وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت، به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد آمریکا در متن جدید پیشنهادی خود، برخلاف متون پیشین، پذیرفته است تحریم‌های نفتی ایران را «در طول دوره مذاکرات» به‌طور موقت تعلیق کند.
به گفته این منبع، آمریکایی‌ها در متن جدید با «تعلیق موقت» (Waive) تحریم‌های نفتی ایران موافقت کرده‌اند. «ویو» به معنای معافیت یا چشم‌پوشی موقت از اجرای تحریم‌ها است و به معنای لغو کامل و دائمی آن‌ها محسوب نمی‌شود.
بر اساس این گزارش، تیم مذاکره‌کننده ایرانی همچنان بر این موضع تاکید دارد که لغو همه تحریم‌های ایران باید بخشی از تعهدات آمریکا باشد. در مقابل، واشنگتن پیشنهاد داده است معافیت‌های مرتبط با اوفک (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) تنها تا زمان دستیابی به تفاهم نهایی اعمال شود.
به گزارش تسنیم، این تغییر در متن جدید آمریکا نسبت به پیشنهادهای قبلی، تحول تازه‌ای در روند مذاکرات به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/VahidOnline/75535" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTeu06HOU0metv_yTbXIcR86t1DaNnwjo1kbCCbELPKGB0syBXSUMpa-Q1JXDMTHZJqvDD3GCX2-3rb3UmvduOtp6EOd2PAnNh7gYhta1JLbm3Kwl-0XpO_FM9TbFKnnlW2Q-M1JmV3xSwJt1V3gnx4tmkPD3h9701lrL4dTlQfbWFeGH94kiVyXi4kxD0SBmnIG8VqnAI5iZMMmYU2EpKtB6yFkq4mUagWSGX_UPuUsOGwHxsp5eLphYTapl-JAMX9uMaMjCC6lucMl2PW6-MYKYNKpQY6oCnkyMZHgcmGJsDYD-zNRy0Xot_A36S9weTym7bLO3v6GvX1oFtFFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع آگاه گزارش داد پاکستان در چارچوب پیمان دفاعی خود با عربستان سعودی، ۸ هزار نیروی نظامی به همراه یک اسکادران جنگنده و سامانه پدافند هوایی به این کشور اعزام کرده است.
به گزارش رویترز، این نیروها از توان عملیاتی برخوردارند و با هدف حمایت از عربستان سعودی در صورت ازسرگیری حملات علیه این کشور مستقر شده‌اند.
این تحرک نظامی در حالی صورت می‌گیرد که پاکستان نقش اصلی میانجی‌گری میان تهران و واشینگتن را بر عهده دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/VahidOnline/75534" target="_blank">📅 17:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txuWYO_JNA4xRzIsK12XNoZNFGPfCK7cz6MBHxGj7m3hAPkee-KqkxmxNmd987xKQ7j7NmMXQWfiTBaFXJoYCNckglnHj2D5EDkpA-pjU3KkN7rbYuqoOp90TGgyMzaqMmBoHWvR_Wu2enuuSb9Xx2kcurGdrIRzURgNFDfxzf-4AUwlMWBM6ThlXEBScqBbg8cGj5-Lnn6Y5ncBB2wFoftzTKsV63lFyUI0BLRJco3MvgFJuYfmMXvPP2ukNmkYGRTDwAM-xDPxLXEEN065HsipCIYiZmHMX59BTwQt1BPcyOZuMJxbQ0RVotb67alYRFWeCpauYhXqBVuJR0wafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کل دادگستری آذربایجان غربی روز دوشنبه ۲۸ اردیبهشت از توقیف اموال ۱۲۹ نفر در این استان با اتهامات امنیتی خبر داد.
ناصر عتباتی از این افراد با عنوان «گروهک‌های ضدانقلاب و تجزیه‌طلب» نام برد و آن‌ها را به «اقدامات ضدامنیتی و همکاری با کشورهای متخاصم» متهم و اعلام کرد که اموال آن‌ها به «نفع ملت» مصادره شده است.
دادگستری آذربایجان غربی اسامی این افراد را اعلام نکرده و برای اتهامات علیه این افراد شواهد و مدارکی ارائه نداده است.
پیش از این نیز گزارش‌های متعددی از توقیف اموال شماری از روزنامه‌نگاران، فعالان سیاسی و مدنی، هنرمندان، ورزشکاران و چهره‌های شناخته‌شده با اتهامات مشابه منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/VahidOnline/75533" target="_blank">📅 17:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6g768la9TNQP-h8Wo_bZQJpaZvc8JRPo3AghAS53Wpl0vD74BMF7sTYPqdhO69LJCAQbwiHr9Wn_GdbiUqBYlw-Ljf5U3fvEojjiXbrNXxF1VmoDmoagskMJBgPHxJ-lveuh0F-eaK1kCOOLW54mE42-lEBymSIH3EBBMjzMIiSeqXJNWddtWsUsnkUSFFVXPnaE1ech1-zWWDO_ogYktojOJNWOJPWgJ_-P6EpbBJ7tEa5v3ApMEeiQBl_Fr2GbhXUnmK7QezL5HIsnv0BKQ8_BRLyP_WwLXLRFrfJmFOieJMKKJJ3PpG1w8NeIJe5CEt_EVYtCD7aAelBW6fWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا می‌گوید مقامات حکومت ایران برای امضای توافق با آمریکا «می‌میرند».
او در گفت‌و‌گو با نشریه تجاری «فورچون» افزوده با این حال آنها در جریان مذاکرات، «روی یک چیزی توافق می‌کنند»، اما «بعد یک کاغذی برایتان می‌فرستند که هیچ ارتباطی با توافقی که کرده‌اید ندارد. من می‌گویم: ‘شما دیوانه‌اید؟’»
ترامپ در این گفت‌و‌گو همچنین بر این نکته تأکید کرده که مقامات جمهوری اسلامی «مدام فریاد می‌زنند» و سروصدا می‌کنند، اما در عمل «تشنه توافق» هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/VahidOnline/75532" target="_blank">📅 17:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fOi_ZpWtTebjw-2ZhAL1uTmnTjUeGA-zDSW_E0w6MtxbmEEJe3QI4kVRIPgEdtS5UdYAIlvS1Q3BHoWAq84BjktZVrA44Agg1RKPxB68T5NepNNC12RQ-PvZmz_uLYeBMML7FWQxgC75NmpbkQy-z8_5RHTQ8GKtNnlvbcf-2koGO3HY9MXwmhB-yOyo-C2ImvtseHnjWik_HlFzi1rwHbVlI5BzL46ZFQMOlZ3VoaqtInlqk8gcxuAc5YBYTAqYNE_5CJCBvqDzKUQlDPlyDmMElmQ-qgywQcnwOvPYBgws9zGzMDVA_w55t3IYPc5gwZsS3XKpBPuMliIlj7Xjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sJggd1SNu9BV_Blhnd4vkrr6iMUmrDlFLM00P3i2j7esYKDx2rLgvOW79OlQd33DDeLelRjLdyxCcxkU4K0DqCO9JhUZiuiQjrYUTycC1sAIqDl-VWaSgYH5sXuXldnex-oDFdl0TFrzkyL80_AL7Z0zWYo50xTp08w-dwSWpJDKM1vFeicOhEeru4t3kwf1pm8hRCQdLwfFv07oyViThRfqPq6b8t8-c5cF2hGU1xdJFcSXaZVSw9FUcdYfwTLTdIq1OpQjKK3ekJUYOIOAU2ZszX7Yyu7WoFGSZBA-pIDeUx2A_qUaW0TPVDRbIZ0xktBoe-s-uz2-7v48QGejoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران می‌گوید روند مذاکرات تهران و واشینگتن، «ادامه‌دار» است و حکومت ایران از ایالات متحده، «اصلاحاتی» در پاسخ به طرح پیشنهادی خود دریافت کرده است.
اسماعیل بقائی در نشست خبری روز دوشنبه ۲۸ اردیبهشت گفت: هفته گذشته، علی‌رغم این‌که طرف‌های آمریکایی به‌صورت علنی اعلام کردند طرح پیشنهادی ایران مردود است «اما ما از طرف میانجی پاکستانی مجموعه نکات و ملاحظات اصلاحی را از نظر آن‌ها دریافت کردیم».
او افزود ایران بعد از این‌که طرح ۱۴ بندی خود را ارائه کرد، «طرف آمریکایی ملاحظاتش را مطرح کرد. متقابلاً ما نیز ملاحظات خود را مطرح کردیم. از روز بعد از ارسال نقطه‌نظر آمریکایی از طرف پاکستان، ما با مجموعه‌ای از پیشنهادات طرف مقابل مواجه شدیم که در این چند روز بررسی شد».
سخنگوی وزارت خارجه ایران به‌دلیل آنچه تبادل «نقطه‌نظرات متقابل» طرفین به یکدیگر نامیده، تأکید کرد که «بنابراین، روند [مذاکرات ]از طریق پاکستان ادامه دارد».
بقائی جزئیاتی در مورد اصلاحات مدنظر ایالات متحده ارائه نکرد.
@
VahidHeadline
او همچنین آمریکا را به «خیانت به دیپلماسی» متهم کرد و گفت واشینگتن دیگر «به‌عنوان یک طرف معتبر» در عرصه بین‌المللی تلقی نمی‌شود.
سخنگوی وزارت خارجه جمهوری اسلامی تاکید کرد تهران در مذاکرات با آمریکا همچنان خواهان آزادسازی دارایی‌های بلوکه‌شده ایران و دریافت غرامت جنگی است و این مطالبات را «حق ایران» توصیف کرد.
بقایی همچنین درباره تردد کشتی‌ها در تنگه هرمز گفت موضوع ترتیبات جدید امنیتی در این آبراه صرفا «مالی» نیست و هدف اصلی، حفظ امنیت تردد دریایی و صیانت از «حاکمیت ملی ایران» است.
او همچنین در واکنش به گزارش حمله به یک کشتی کره جنوبی در تنگه هرمز، بدون اشاره مستقیم به عامل حمله گفت «نباید عملیات‌های پرچم دروغین را دست‌کم گرفت» و مدعی شد هنوز مشخص نیست این حادثه توسط چه بازیگری در منطقه انجام شده است.
@
VahidHeadline
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، در پاسخ به پرسشی درباره گزارش‌ها از قصد امارات متحده عربی برای حمله به جمهوری اسلامی و سفر مقام‌های اسرائیلی به این کشور گفت: «ما قرار نیست با گزارش‌ها این واقعیت را از یاد ببریم که تهدید اصلی کدام طرف است.»
بقایی با تهدید کشورهای منطقه از جمله امارات متحده عربی گفت: « اماراتی‌ها از اتفاقاتی که در دو سه ماه اخیر افتاد باید درس بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/VahidOnline/75530" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odht9TtSgMx1RvscvDnhweUyeYBH0-7WHhZICzy1EuOdjFWU0zzhGa5uWt96b66SnWZgWjleXzcr-pGtM3LXuCAXefb0srEDxKT2tBjsSozLIl3YGQlOS-gOvTti2T64wex5VoXKlwJCg0kcocfeRdSEqB_9FwTEjUsfMwIBJUFkKiJT0C24tWRHqeDgEJpOy71RI37cLaH6VnP7Zg2QxslCyiJ-cFoM-cxaKlSuH_GitAzcfuzMD5nnk5baKGongM8P8_zu4PTZRvAS1lA0Vth6zi8IHWE9DTJpPGPJIPXv5LO74Oac_8HcrA6kEUvFHDdHZn4v9xc3AVmHm-FQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نت‌بلاکس» نهاد ناظر بر آزادی اینترنت اعلام کرد قطعی و محدودیت اینترنت در ایران وارد هشتادمین روز خود شده و مدت این خاموشی تاکنون از ۱۸۹۶ ساعت عبور کرده است.
نت‌بلاکس همچنین گزارش داده که هم‌زمان با ادامه محدودیت‌های اینترنتی، محتواهایی در حمایت از حکومت، شبکه‌های اجتماعی در ایران را پر کرده است.
بر اساس این گزارش، برخی شهروندان ایرانی که تلاش کرده‌اند به اینترنت موسوم به «سیم کارت سفید» یا اینترنت ویژه (اینترنت پرو) دسترسی پیدا کنند، گفته‌اند از آن‌ها خواسته شده سهمیه مشخصی از پست‌های تبلیغاتی روزانه در حمایت از حکومت را در صفحات اجتماعی خود منتشر کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/VahidOnline/75529" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQx18n1o5kLcSD4s4wG_ADgQbAYwIolAjMOA7M0ZwLyukzn35iY4Zp5HbakyvRYbnta3uIYGL71hNRBe3uNPNjMVLQ-YrS-yoFOMH7yxP8YIxTP0BXVLqsJQXIf_JjJohNjCMfRCs8kM_7pFmrobl0ru32E8QDFW2-XsduhNlkE538zFpdYAR0WhlMOj9EFobgqT1GFWsmwbbA4lQKXfeeV86z66VOqDhrJHzYpIqm1FrYUHtvnUHq8-wUZNsEN7OrWA7B67v1vGDMWVgp_5jvON4_juQ9080UihhghPzGgUzdEQd2yUOVvrFIFN1FIwCEf0Qu-WuVu8X-JVuxMZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل روز دوشنبه ۲۸ اردیبهشت گزارش داد که ایران در سال ۲۰۲۵ تعداد «بی‌سابقه» دو هزار و ۱۵۹ نفر را اعدام کرده است؛ رقمی که باعث افزایش آمار جهانی تا بالاترین سطح از سال ۱۹۸۱ به این سو شده است.
این سازمان مستقر در لندن اعلام کرد که در سال ۲۰۲۵ دست‌کم دو هزار و ۷۰۷ نفر در سراسر جهان اعدام شده‌اند، هرچند اعدام‌های انجام‌شده در چین در این آمار لحاظ نشده است.
عفو بین‌الملل گفت «هزاران اعدام» در چین، که بیشترین استفاده را از مجازات اعدام در جهان دارد، انجام شده، اما جزئیات به‌دلیل «محرمانه بودن داده‌های دولتی» در این کشور کمونیستی نامشخص است.
این سازمان افزود که آمار جهانی سال ۲۰۲۵، شامل اعدام‌ها در عربستان سعودی، کویت، مصر، یمن، سنگاپور و ایالات متحده، نسبت به مجموع سال ۲۰۲۴ بیش از دو سوم افزایش داشته است.
در این گزارش آمده است: «این روند بیشترین شدت را در کشورهایی داشته که مقامات در آن‌ها با محدود کردن فضای مدنی، خاموش کردن صداهای مخالف و بی‌اعتنایی به حمایت‌های مقرر در قوانین و استانداردهای بین‌المللی حقوق بشر، کنترل خود بر قدرت را تشدید کرده‌اند».
به نوشته عفو بین‌الملل، «افزایش بی‌سابقه اعدام‌های ثبت‌شده در ایران» در حالی رخ داده که مقام‌های جمهوری اسلامی، به‌ویژه پس از جنگ ۱۲ روزه تابستان پارسال با اسرائیل، «استفاده از مجازات اعدام را به‌عنوان ابزاری برای سرکوب و کنترل سیاسی تشدید کرده‌اند».
عفو بین‌الملل و دیگر گروه‌های حقوق بشری گفته‌اند که پس از اعتراضات گسترده ضدحکومتی در دی‌ماه پارسال و همچنین پس از آغاز جنگ با اسرائیل و ایالات متحده در اسفندماه، استفاده از مجازات اعدام در ایران افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/VahidOnline/75528" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trP72RNmV7rQz8ocLm954dDZ7amMIUVUo34vfUScYRAp1Tuzps9rvMNP4W5d3e9fjGYSzLyRMbZgsg5meaPPtGcjX5YaQU7h-q20DjQyAWS8l4VbsM6yxi17-VPznNq4xLj-REbHNo6plE2ykt9i7bywqZmE_urU4ILRTxweT4-0XGyw7cLo7cs302DWkY9b9hcLgoukZdD_3ab87hsxkWy9CSlv2PVxZgQxTtz-dJKBGX9SX2q-Jtnlywkb5Clw2G_P4TwVz1a3KD-CidR7lxpdSSEojvociGd8v14GwUW49bw3anik4tJH8qOZJFEp8vkU9Ta5znZHxr0XUfXs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌های ژئوپولیتیک در خلیج فارس و نگرانی از تداوم فشارهای تورمی، قیمت نفت در بازار جهانی انرژی افزایش یافت.
قیمت نفت برنت در روز دوشنبه ۲۸ اردیبهشت با رشد ۱.۲ درصدی به بیش از ۱۱۱ دلار در هر بشکه رسید و نفت خام وست تکزاس اینترمدیت آمریکا نیز با افزایش یک درصدی بیش از ۱۰۸ دلار معامله شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75527" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkkgYMUShEplpFnooBdz4vduYMovbwMgow0zmSvhZWPl7fGvs7RdM2AwewfgB6kVm4xSistZYyPz3-IfCE63YG1JcbKVwg5XacG0gXmoPXCFtPjMUeV9m-feCLKnnVGzzfbmzinY38u89Gr1I8np7IF7OLAt6eQLmQsI_Bsyowh-vK2aXrAn7YfYhqDTGKO13M7v91mIEiyDcIXOWDEgG8IDdHu8xp3L6Q3q4oPmeLADhMAomUR71p8XW_WIqMxE39Wd3BljPepQgJGO8FUGe_kUxQGw147BwT6XbHIYx9hfzVorJLZi0Di5O09NL0BPTq0s8VJToPk0sCPJBGtkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در مصاحبه با ان‌بی‌سی در پاسخ به مجری که از او درباره بازگشت «پروژه آزادی» (هدایت امن کشتی‌ها از تنگه هرمز از سوی ارتش آمریکا) و از سرگیری کارزار نظامی پرسید گفت: «ما پروژه آزادی را به درخواست پاکستان متوقف کردیم.»
روبیو افزود: پاکستان به ما گفت اگر پروژه آزادی را متوقف کنید، ما فکر می‌کنیم که می‌توانیم به توافق برسیم.»
او گفت که ما پذیرفتیم و رئیس‌جمهور هم دیپلماسی را ترجیح می‌دهد.
با این حال روبیو گفت ما در حال خارج کردن ناوشکن‌ها از تنگه هرمز بودیم که دیدید رژیم ایران آنها را هدف قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75526" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F3oSQNXLvg8YFVCO17NIDZlV20xtLmbYRE71Chy1Hx4ueV4bY-ixCxCP8v_9IzFNbsAUbyvVPNVmHUrtybVy6BE_qV7kttVz0WTHVSvWDP_-fkDzzN8KuDCWaTKJ4XIZBqc3vSQFocpCajbIS8z8q21i1q0keGW1JCiIMljrhr72wICibCq19BVyzgbk2FlPR6Z1NClxXTNb4Z1LltngRp-LQYsH3FD_Jg9jhQUWz_XTYI2ySNDf9qsjRpiZcX_bcPHlq4lDpAFFE-8DnXqITqRGwkVrpys-LZphaUsRohi-w7_8_gi6CG36q5FSY3yJqvLjiT62ZmSMDByJL2Z6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ترامپ به فاصله چند دقیقه‌ چندین تصویر مرتبط با ایران را در تروث‌سوشال بازنشر کرد.
ترامپ همچنین یک تصویر جدید از پرچم آمریکا را منتشر کرد که در پس‌زمینه آن نقشه خاورمیانه به مرکزیت ایران قرار دارد و از همه کشورهای همسایه فِلِش‌هایی به سمت ایران نشان داده شده است.
او همچنین چند تصویر و پویانما را بازنشر کرد که ناوها و پهپادهای آمریکایی را در حال هدف قرار دادن پهپادها و قایق‌های تندرو جمهوری اسلامی نشان می‌دهد.
@
VahidOOnLine
طرحی که سه‌شنبه از قایق‌های جمهوری اسلامی
پست کرده
بود رو
دوباره
منتشر کرد. ساعتی پیش‌تر اون
انیمیشن دیروزی
رو هم
دوباره
پست کرده بود. تصویر ساختگی یا طرح گرافیکی دیگری هم
منتشر کرده
با عنوان اینکه نفتکش‌های خالی برای خرید نفت به آمریکا می‌آیند.
اون پستش
علیه اوباما و بایدن با طرح گرافیکی قایق‌هایی با پرچم جمهوری اسلامی در کف دریا رو هم دوباره
منتشر کرده
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75524" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujxZrhuXH8LEpk-B205ntVNSnJnkRKvmdGGGy3TxZLZHT9arv2DfM1la4aqpUFwtH-wNP-AGL24iHTv0pB0YcWSgpHEtTn5GUEYpVKu3GX2_Atp_IjmyxpcVsrPi_eUksi_JpbI-VwjojCtbIobj3pNOSKrhBGvOE9ijFxCO6c2zUIEVIPRdDzKjmztgiWVVTGUYVa_3Dge38Up4RqZ85cn_h_5CusXRrMUyeXzvTHi_QGJ-V_6QpEOoOuPzQxxiLm0smKG3oRNL03-1ZWbWeP5iALOcwl7XLA-poUnemo7Nh5Nctxuvfwav8okFBvgNp8yC4eSyw0SjhSBOII37RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکی المالکی، سخنگوی رسمی وزارت دفاع عربستان سعودی، یکشنبه ۲۷ اردیبهشت‌ماه اعلام کرد سه پهپاد پس از ورود به حریم هوایی این کشور از سمت حریم هوایی عراق رهگیری و منهدم شدند.
سرلشکر ترکی المالکی تاکید کرد وزارت دفاع عربستان سعودی حق پاسخ‌گویی را در زمان و مکان مناسب برای خود محفوظ می‌داند و تمامی اقدامات عملیاتی لازم را برای مقابله با هرگونه تلاش جهت نقض حاکمیت، امنیت و سلامت شهروندان و ساکنان این کشور انجام خواهد داد.
وزارت دفاع عربستان سعودی افزود این کشور برای مقابله با هرگونه تلاش جهت نقض حاکمیت و امنیت خود، اقدامات عملیاتی لازم را اتخاذ خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75523" target="_blank">📅 00:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGdfVn-ncxntJWtzn7etiYBedmesxfILZ0iSDC6aEeNSGxrY2vIwI5_YKCTb2_D7Yku5Ow9GmbvIxeZEQB9mMeGr7Uk0iQlRA6OmR88yhkuqKUmoVPSWzAdlDRwEJPrIU1NBEZCYEfWQQ2tBwf7PzgCAXR4LlS2u5tzPpyGqC7S96swKfSKyisqrIjNSCrihvdlJEuToNb9VklSAprthZ9lRttSMt2w5EVj-ttID-puTq3qozQ1A1Y4LggT0gt1wIhYbq1NvuymxeGjtFxQ3nuPt_vYzrbqWdEpsaK2-fAuDvhRsSs1f9_5fQKQyw-bpMre8us4Yp1PSbGhsx7WtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح روز یکشنبه ۲۷ اردیبهشت ۱۴۰۵ یک دستگاه اتوبوس در محور عسلویه به کنگان، پس از پلیس راه سیراف، واژگون شد و جان هشت نفر از کارکنان مجتمع گاز پارس جنوبی را گرفت. پانزده نفر دیگر نیز  در جریان این حادثه مجروح و به بیمارستان منتقل شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75522" target="_blank">📅 22:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uu3tyOY0YMdVxwGLanciasw4IsctRmGAYQeAuJam_M4-EagJSZIwSPUf0Q4Ru9-ycg2f1wF0MyWIZQnH5XbYqi0RLidYBUgCSUiD5PEUQPwwk9LQEQRuejDqThTJDeZfb-AAX00EvTy7Czioc8s-BijVsWMXOQ3UspT7qtVeF5j_5Pp6uGSgRcUQb3ymgLCtScKuoKDSCJNVJ1NXOOgA2FPYEQzAUeA6WfZ2G5bAoPOqOBcIQ00gjwkpB7hCnbcccux7NhNnnqFczmkK0La0L3gdhV_TZVz4v0W3oVlyWuTTgJDGWIblbnYfwy6099zX60vHAGYcAA3oe6gETp9hRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
زمان برای ایران به‌سرعت در حال سپری شدن است و بهتر است هرچه زودتر اقدام کنند وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان حیاتی است.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75521" target="_blank">📅 20:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hds6LazpeRU5dzOXkAr2kQuzKUpv7YOfeB4RlygprC70VLbrLmAJcWbTz8f-9v0g0hfuvt0Jh9juBjgs4tf5pGoYoN0HAeOV6d_hu-V1UwZXp8t7UCfo25GqbtOEGg7QowezZryv84vh6zbVfF7OXZs7ZmYdv9uEHpc7QHqEOCHvEDsAQ2FSJA3jZ20u7G08jMvynvIkpBFQPpK9WU6t2R40in54SLKjDB5mk_QgQDA7qnFxNE0Gr0PIKQaNJau0p_cNJ9T3mO350JwnHFlbDfB97Ecak5Seomjm2SFW55rJQkcfIvWrdjrPEWg8eyGa6mvARGMlG_pNZzU1xu4s3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او روز یکشنبه و دقایقی پیش از برگزاری نشست امنیتی، در تماس تلفنی با دونالد ترامپ، درباره جنگ با ایران گفتگو کرده است.
به گزارش تایمز اسرائیل، این تماس در شرایطی که گزارش‌ها درباره آمادگی آمریکا و اسرائیل برای ازسرگیری جنگ با ایران منتشر شده است.
بر اساس گزارش رسانه‌های اسرائیلی، دو طرف در این تماس درباره احتمال ازسرگیری جنگ با ایران و همچنین سفر اخیر ترامپ به چین گفتگو کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75520" target="_blank">📅 20:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AFtXWl3jZrBrrgQHfrjrysFn3yj7mNJ65gW5QfqDfI-qJiQesosNn35roz82tMGhALvGB25yRHkrAA9qWQNNsc_c_lGndgmqTfRnNbuHjL_liaFq_DL_S8HmqxdZiLP1FA85O-HsKefh9VwP6TJ8JJtU8vmzoH1976s0N9bbbkuTZTJi_njPBerZN5agzWAmVg_GcuD_lrBKxrCJOx33l8w4FGKWd6L_TtK6h2g5LAM5QVaiKL31ArQxbxX8CECzeY0LWfbUnrQHczalNtAYdlV2NZrNGZZ2oI348o7KJUAlie9TVsF9CXcDYSaG_JAHWpc6CxFR8qXzMFvsraEYpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LJnpHwLJc78Pjwuti3cKTeWq1pCnkaJm7Rwb2imIeodo3M9qjg9T3NEFsF187DNMdKC159UDylrnKlpLfDby4QxYaeqtpBsTEbS4Id5uB9X0HKL-jVf51b1xrV4iFKfgdo3HJzRlOfcOZ83PFblzmgE-UlUzLDNXWS_efEeT8A-3_xnF_KQ7HzBY83-4VDHcXhpbyGYN7lSNGGxLaapo5RxIHY-1a00LShB3IQGp0QwllaTGhboYeX7spO98F5mAbkzHyUiVkrLE2v9ZZOA_-IXJ6DPrZJWzvKZfE37ibLwn5SV34m1iTAmi_LX4IB10pIYvHy1y-1F28nOvjZtGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YQlyeHcHR0B6-zor8Bi84tZfeo_azuGeHynfOvFN29PjxN1AngdgCtRsN2Ws0ZbFh0xcJjgYn0OBECNf2IBMczsD6qEOVXl_d2Z6fOx7SfHc9T74XqRDv711Sm86mqbhchbQkpYoX3upcnWLdtFSxKnLLePbDkiIaDDVkEMcf6tSEjLkgNPuKggbV-U3kMqexKaQ5JPnoEtTz33zghXyc0VCzj7En0MOmhoRPaxiahPZDFR0nWry4y2VbvypBMKraAgDpsezH4R19bI9xLrDvxBSga0CSO9NHthkdZIPdGTTMUNW9E41mtW9rFj03i8-4TJOkoYxW32IBnjax-7-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B_yz3zZyeU891KXXfxedLRfYznsJUbrrJENQw5C31MpFinH159I9yIsb1c5fML5ssqEkSSaqLdEdCg3jk7UdXNn4dj2cVVUihDaVQcY33-fd-5hew5QCWyA-QD5nbH6S86wCExdCgvSHhhELyCrJQxDmM0ybo3q9mQs_99pgljmMVx6dG_2F3hRM2Cmj6VFWj8hFAtlqVYZ7rVROF1rOtG8fJGwo-f7ouJ2smk3HOfGhsKgQ67o7Qhwefhstw0fv9bh25fPxRolyqe_gH-2XOXA6p95vPiHycT9xfbqkyDDJeD-DpY8ZuFrDibb_3DpVJszkL5wzZssIYUZyEKh6bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iNwwfJdyPVW0fblea5-4nmcb1UQI4k_D2yjVndEAHxjERUosdLEDQKijkqRvy_JLmItE5tjnLfka0fVQKKYlBZOUvTmELpTHX-au1uCijmlTo6jkQgWIit8VgSp7O5aC7yZtf8Kl8eIUMzCi_Zqe45mJeFsyQ3bOtJWa12qnZWG1_75ZoLDn-5fPFPEJI37WHSUMspy9ER8ekrCO5U_jLTF-gb3kVNULi6Tav5Th1H5CY-vJDyXvONUn7OPuvLy78aNBacMIw6vZvK_gMRo9xA0Ma3ZaV2ghH7a7RmNn3EPvK8Fz7SNb3LfpolTC5-t4sVVR3l7o4sAG5NKN9LzKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YJbpGc3dUoYaBVBjRNnXp7ABePRK9kEtSx0og8Bb77-INRPYuw3sHVU_eVVyX6LgS0o02xDi_zgdFZKU05XTYiGhsGaSJfP1Yikb9eu0-ujLc5J12CQanH4mmNi0GYVGEfax90kTQfnij2Yp7RXgG2fhWEUsxXEuf8VuPgezRG1MTyvHf_X7bDWwbUPjNXVunXePvP-DISUwTnFt50pfe-INM3HOPUtW8bpzFfFwkFbFf_kJoPQ655gXwvRqfYxlXZ6mUfsYOc2xTeYlHeCwbGKu-AijhHK72hTkOg_tmsHHbgsicxsIkSLDFI5KnXYpJ8yvJvkBsj4VPZV6o7MZbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس ایران در تهران دیدار و گفت‌وگو کرد.
رسانه‌های ایرانی و پاکستانی گزارش داده‌‌اند که آقای نقوی برای از سرگیری مذاکرات به ایران سفر کرده است.
گفته شده او حامل پیام‌ آمریکاست و پاسخ ایران را هم دریافت خواهد کرد.
به گفته سفارت پاکستان در تهران، آقای نقوی دیروز پس از ورود به تهران «نزدیک به سه ساعت در نهاد ریاست جمهوری حضور داشت» و اسکندر مومنی، وزیر کشور، و عباس عراقچی، وزیر امور خارجه نیز «در جریان این دیدار در نهاد ریاست جمهوری حضور داشتند.»
علاوه بر این، محسن نقوی «دیداری خصوصی» با مسعود پزشکیان داشت که «حدود ۹۰ دقیقه به طول انجامید و با حضور وزیر کشور ایران همراه بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQeXoX3pMw-sm18BjtZvEuBuqUfY9XE3cm_CCyGFsBpLZe3SeLATTGMS3pag3AXM8R4y5s_WtZXQ1Q0odjk8hFwjdbaACSZOJATbbGfWuno-WlxvfBpNGxneWjxFwMw9axAOVHzBsMfvEkXpMuXheO1Hwor5jHNwwqVD7QuAwDvzYpLx6A1zqVrvyGR1L12OsaYOf3G6joCQ1zx0brfAcjf9bTCXXw5Iv5sKjS0FrP6gRl9Gp8aZhm0rM-Tae85LmCP4xVgVMwkTqnW1RekkBOtQRqKnO3V-djwpfFfOWHo3FnmptXAT--6CnK0h4SY4dNUDcSzyX-_yHP5S_SYsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس با انتشار متنی مدعی شد جزئیاتی از پاسخ آمریکا به پیشنهادهای ایران در جریان مذاکرات به دست آورده است؛ گزارشی که در آن از پنج شرط اصلی واشنگتن برای توافق با تهران سخن گفته شده است.
براساس شنیده‌های فارس، شروط اعلام‌شده از سوی آمریکا شامل موارد زیر است:
۱- عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
۲- خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
۳- فعال ماندن تنها یک مجموعه از تاسیسات هسته‌ای ایران
۴- عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شده ایران
۵- منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
به گفته فارس، در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق پنج پیش‌شرط اعتمادساز دانسته است: «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3x3vIKfqcsuAjeW5VeXPHRvxfoai-csmeoRR-KPeuIGQbTZeGW1mkFMgE3pRq1S6SQ1f4k4-aoBT3o5WRcXhJ6VTejTJbGmGgPlSPnPzsrm6jCr7nQr12AmPT79GH2RPNmM9mdqcQqxX6efPRzT9Fj1YP_rlXmZfVP9StTdjXEc-DWHvHhLCcm9F_gv19g5pmk6rG_64W8ItCoa1vriHubPkewvQyYTkozIP0HHDiI15naD5Zq8RK2eBXQ4wPHro5NbBT1YcA-ZezMnKy2uqlAUSgObE7-D3VMEY9qHXjHaygU6Hc3lW8EAuFAW4fj_X8tO7NjKsSi8LA7RDfDAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ8i6MxwVieA8hOvHJrFTOzRbPOUoCvhZZOP8uIRKGH3Lx-XuYbsdQP7NrXFMQ_toHpxcXZGEscNOvD5nWpxWWokocMyjm0hH0HPGm3s35xeGoc0BKvMy5Cvmg6FcCsLNUrjxvFdnpe-C4QZHM-tHYL2WfPunK02FitfQfp9-H2M7q7rZygOIQGodP7MPV2u0NKShUnHGr8kopuUEY72qlrLn6jhfYHRPcLc1RL4jilACsMdbDR6MF6ojtdNHS5Y0U9D-a8ce7VZlaWQm1Ryod8axEnBdtsBMmUfbm1eQFVsa5H4aR4AgwMio_CKyYpSaatAxBd8BmOghnh9nG4YDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1Wz7g5-l2H0bW6rAn6kbTU6FogK75ZCI0MqOWP1TiKikNO9cPQBkBMMNFamrxEvfc96JPxC5ANrkgleMqFaiKDrNC2BOoiA402bgUGfz9AzEkRbXS4Lr76tJ75WPt_rc5VBZw7n7wK6tWDZP67OWy5BRWFOs9cDz4tO31b8Iz6O97oshidBCcVmQvkLd4BL9ySr8FJPTEgN4c7bGKeSTH3cVBXQf_uJjM5Xn9tiAkOGSn3-lX5Ht6qug9LRCD1jUIx4mrDcCph-uhXTItq24WZSEm8Vq9U3AyMCHQbCDAXV4rQXcuGkhQ9QBEY_d06IvTqHHTxxpGCEuGgTokbtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه ۲۷ اردیبهشت نوشت که محمدباقر قالیباف، رئیس مجلس شورای اسلامی و عضو سابق سپاه، به عنوان نماینده ویژه ایران در امور چین تعیین شده است.
این خبرگزاری امنیتی بدون هیچ توضیح دیگری تنها نوشته است:‌ «پیشتر علی لاریجانی و عبدالرضا رحمانی‌ فضلی چنین مسئولیتی را برعهده داشتند.»
🔸
در این خبر نه توضیح داده شده که چه کسی یا چه نهادی قالیباف را به این سمت منصوب کرده است و نه برهه کنونی چه اهمیتی دارد که حکومت تصور کرده است به این نماینده ویژه نیاز دارد.
اعلام تعیین قالیباف به عنوان نماینده ویژه در امور چین دو روز پس از دیدار رسمی رئیس جمهور آمریکا از کشور چین رخ می‌دهد که در آن یکی از موضوعات گفت‌وگو ایران و تنگه هرمز بود.
کاخ سفید روز پنجشنبه ۲۴ اردیبهشت اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دیدار خود درباره گسترش همکاری‌های اقتصادی، باز ماندن تنگه هرمز و جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگو و توافق کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6P7eHGu_s54vK657rvhL4U_FaZ_QxUi2gEsA5l0fOuXZO-QCrHV-Kab46o1X3xqrrMcj7835-yzdIvMj6rACAcMM7UMYK6NanEOFFj5pwAKLFnnne9PCuTyxKvh6Em5knURUbxdvfxbrLUxspvJJeuxxXS4MilzKEbatCZAVLsFHRCKthd0BLhgsHnQDf54czGZZaGDX9RLbNjB52nvHfVObXOEp_BgSOinjPgnawRSfPIpyTOlyvh_PnaPtGQNqtZXJv9N2_pUzzt794DJ1vhIGeUvCTCiXvnfkifwLnNiGWCuFXKxWTx09V09n0AFgax-xE3xMsbYtfR9dNL29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه دادگاه صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای ساعدی‌نیا که در اعتراضات سراسری دی ماه گذشته به همراه پدرش، محمدعلی ساعدی‌نیا، بازداشت شده بود در دادگاه انقلاب قم برگزار شد.
کافه‌های ساعدی‌نیا از جمله کسب‌وکارهایی بود که در اعتراضات دی ماه پارسال که با اعتراض بازار به نابسامانی اقتصادی آغاز شد، مغازه‌هایشان را تعطیل کردند.
نماینده دادستان قم در این جلسه آقای ساعدی‌نیا را به «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های معاند نظام از طریق انتشار استوری و فعالیت مجازی و حضور در تجمعات غیرقانونی و تعطیل کردن کافه‌ها و مغازه‌های خود در کل کشور و تشویق تعدادی از کارکنانش در ارتکاب جرایم علیه امنیت کشور» متهم کرد.
به گفته نماینده دادستان و قاضی، موارد اتهامی بر مبنای اطلاعاتی است که از محتوای لوازم الکترونیکی ضبط شده از آقای ساعدی‌نیا و از جمله تصاویر و چت‌های او در واتساپ استخراج شده است.
نماینده دادستان گفت که آقای ساعدی‌نیا در واتساپ خود «برنامه‌ریزی برای تعطیلی کافه‌ها را همزمان با صدور فراخوان دشمن به مشورت گذاشته بود.»
قاضی به او گفت: «شما با فراخوانی که داده‌اید با اقداماتی که انجام داده‌اید، این تعداد جوان را به این مهلکه وارد کرده‌اید و نظام متحمل صدمات زیادی شده است. چطور می‌توانید جبران کنید؟»
@
VahidHeadline
نماینده دادستان، مواردی از جمله فعالیت‌های ساعدی‌نیا در فضای مجازی، تهیه کلیپی از یکی از کارکنانش با نوشته «جاوید شاه» روی دست، ایجاد و مدیریت گروه واتساپی کارکنان کافه‌ها، انتشار پیام صوتی درباره خاموش کردن گوشی برای جلوگیری از ردیابی، حضور برخی کارکنان در اعتراضات و برنامه‌ریزی برای تعطیلی کافه‌ها و کارخانه‌ها همزمان با فراخوان‌های اعتراضی را از مصادیق اتهامات مطرح‌شده علیه او عنوان کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGlUSHhL1KHvJwgReQsgHSYU55-4R8HIW0-9su_5ELCCb7X1sjzhTtTiKkvZjL9iQrjLx3M88WfUouxcAfL3bAS7Jx1zfRhfUCoiB8z4gRIAoaWNuqT8WZCVKdwcw44wjPKEKDPAIabKJsHe9Oo_IsrCBhaJypgtPjHgd6nL-sJ8BCp-tkli3gdngJ-S56aOIul6nRjjY0v-1Pn9QQXJBOihSxA0Nlz1V5pQjkVZI8tPRr86KXkxACJCMkQOpDaJNu4NNziJotx8Ppc3x0A4tREZW9-v5NCrquHPI8qjVLNkIb-f0X6k-kNtXeCAuWkYjzlddEMHZvk20h3ergGiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=pd6uBKvOAekAjvAoSBLpW9SM84OCt7pkCYjdb1iSZvD-GZm9bWjKATHAvuXNj8lGwBcz_m7npIW4ibjTzPHqOlnoSES1K1MhCHUhIF8WXApL_IOFLWDcxtdsjzWeWvveUTa-uYal5Bg7uf3xpAXqecs4YAb7DbRqlNE9lZB1IwjTFyq55YSZOI7uanBm5e66g4AdbkPfcc_HkKZrSIr80wSrVPeYdFxL8ChM75oGZ-fN-w2LAzN-fwWECf1cIIdznJCkU8wMBWKzWfPImJO0cq6YzsDLRQ7GfyNrMXx7lGYxoJETTDtva2TYC3aBEiGGyrDxp1dbaV33-nAfbJxRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=pd6uBKvOAekAjvAoSBLpW9SM84OCt7pkCYjdb1iSZvD-GZm9bWjKATHAvuXNj8lGwBcz_m7npIW4ibjTzPHqOlnoSES1K1MhCHUhIF8WXApL_IOFLWDcxtdsjzWeWvveUTa-uYal5Bg7uf3xpAXqecs4YAb7DbRqlNE9lZB1IwjTFyq55YSZOI7uanBm5e66g4AdbkPfcc_HkKZrSIr80wSrVPeYdFxL8ChM75oGZ-fN-w2LAzN-fwWECf1cIIdznJCkU8wMBWKzWfPImJO0cq6YzsDLRQ7GfyNrMXx7lGYxoJETTDtva2TYC3aBEiGGyrDxp1dbaV33-nAfbJxRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rJPuDTM8IjNZxVdJA-VFJxiszuMe4vkE9A79eVKpRrq3m9ooxt-SnR7i9ckl22huZdtNmLnjKCefC3IAkRQe9fCa94Wm-IaSBgyucELVuFgZWlpNra8iSg_0nXqeD3eCarJdVLYidGiLqMKzcuF_fSRiaQQ2cRTsLG6uzrcYTXlJydKQOXWimG6FMp-cESkQw6nomP1_SFglMc3ezCATWSjM10rHxm1dg5yUMAq_saPd67j-I-DBl_pId5HkB-zNbvSjsvr5BgKiyRhaYnn8ubGfyY8KHrFxmzId9Uz118CNF6cgAP6kqwr78rvBezLdm606d3fEsYV4MY8yWvXTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LceV2kHgLgK8PI1vclHBiVfUXOqD_M0E21v0oV2yu0DKjgOsykZI0DWC7jGqddoP4B725l3mIhnm-LFa4-Xi35LdSg6-Zs4rF0Kl64R30QnZ_O1ErPMKEEyDSxtv4ntCae0F8EH2zb-SMepWZvMtZZ2iTN6oCerZ8pCIWzY-zjUXILt6hKknWq-XQFhuwDB2ftW2jgEpIf_5PRXxLwQcXQV3m0eP-spu7rzLpXtIepjSvEurkbR-EgTDSf_ZytTPrRI-N7xiHuWdq7x9QWVjrVf6VxhsMVWMdGb0IH6O3iMD57ciMV0gPpk5PommaJnDpfiA8-nse3qCvyvJE4eDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nC2CTA8F9bqOTuKYQfXWJTfLR30Nq9SlC18eYMCDNNi2ZzGkyralDPgUBaL7vFPGzXBfb1d7Z_R1ymokbcHMookDZvJN_cpYFALsH3xs4ocQaJRLki8UHdwdhvRGSkfCv5NQi4d_Vmdkmurq0lLr7j6mkO2sgYiRxwRe-4L7N6aD0I_e453DHHnB_OAkS4efSQIqzQ-EWVhshyWr8H3-r0M4xuLv7q6nQVpD8j-haFclf-sQTw336hQkksquWIEAdiEcQQiC4_GAWkmKBJvgvwOF88VQ41tHgapwSJqzPTsavoFdiubPNI7CrSJ5cmG9ASFLYZ7Xehw2Y8CuJCPXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XJujY0MthT0xXtCmF2jHuD5F6BfTCrypoRYNWhVyqa3vJLxUHjNvukTpCcUIQuSmc_kNR5oBpevgQIQ4eHeVXaO_36gtxno2MODl27o-tufN-QxurjmfMoCVypZ1Wh_ASY2lJWIGZ79oQ9S2XweXlkTPrK8vDW_zDxqCNhIo0SpHv5ttc1LaH5JiEEJMRGQKat_kDRUs8pLu1cL0kT3caXr5R--Gw4Sse3BgA_LIBqjntZ18Ffat5bWtQqMyDX2G2ECw5rY9JH75bOciz1ntiTDwh6bjf6DYQwBY1tlcRAk0f5QuR7h8_XptYZjYtIKmHafaWkbQsu7q5aNkJFyXiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=mbgSEN4UmO75rDLsXCDQ1PEIJPTVSgBL3QAoVFqyEyTgzCnqIbQKDSx34BDcczaBLu6J3lDTsmNQLBWSk9IuJ927BjL2m0ArMcnXgGhA5TKBpTIxOO132zrRwsFnNVQPpdGoXExLv93l0TbdLO4zgSIKAEFjd5USuNU0sOp4xLfM44fQs81D59mmo1JVrm6QeYAJcFEsBxM99e2kpHDu5Q09HOZ5Gmm36inZqFa-K0Xhk4jjr_DDiAsXZg1yyd3CtJ121e60_R_XK4r9azjb4XAGDHa5E3i5z-eYBv22_cLoXqEESpIa1cBQRC073j_zHcwoomhlJyiODCXFAzUcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=mbgSEN4UmO75rDLsXCDQ1PEIJPTVSgBL3QAoVFqyEyTgzCnqIbQKDSx34BDcczaBLu6J3lDTsmNQLBWSk9IuJ927BjL2m0ArMcnXgGhA5TKBpTIxOO132zrRwsFnNVQPpdGoXExLv93l0TbdLO4zgSIKAEFjd5USuNU0sOp4xLfM44fQs81D59mmo1JVrm6QeYAJcFEsBxM99e2kpHDu5Q09HOZ5Gmm36inZqFa-K0Xhk4jjr_DDiAsXZg1yyd3CtJ121e60_R_XK4r9azjb4XAGDHa5E3i5z-eYBv22_cLoXqEESpIa1cBQRC073j_zHcwoomhlJyiODCXFAzUcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=qp7K3ZWTdPxnvxL-OV-rcTW9jVEVSwl9VCSdYeDHowXJuEVo_3EBtlVtsmEm09hFswvhhhhW7sZ-2ytHHi2HXc-qV5xuYaJUxK4MosjmXOQbSQank6sCPe9PJhCv9MkISzvJMaQua8vAYc704JmE9Kb4wa4g3jvjv6cat9h8b1D3ZIapNKDvNNkh5OzzSVlUF3Nndd8KuFpJJ24BY75vDDJ0waoSfECihLNdSfYHFnMYtmKafl5Xvl8Q6GIhtkOBx1T_c50pJMsXgNqa0GMuTSncn4SGbZymQ8rMwXjP78Z_Dgip88ETnJ8j55xMyzpw4o3s-fZ9JH32Iu4hwLbm7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=qp7K3ZWTdPxnvxL-OV-rcTW9jVEVSwl9VCSdYeDHowXJuEVo_3EBtlVtsmEm09hFswvhhhhW7sZ-2ytHHi2HXc-qV5xuYaJUxK4MosjmXOQbSQank6sCPe9PJhCv9MkISzvJMaQua8vAYc704JmE9Kb4wa4g3jvjv6cat9h8b1D3ZIapNKDvNNkh5OzzSVlUF3Nndd8KuFpJJ24BY75vDDJ0waoSfECihLNdSfYHFnMYtmKafl5Xvl8Q6GIhtkOBx1T_c50pJMsXgNqa0GMuTSncn4SGbZymQ8rMwXjP78Z_Dgip88ETnJ8j55xMyzpw4o3s-fZ9JH32Iu4hwLbm7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=uCFaisQwoo5Gd8taqvDEHos8pkofSnjS_4ZFqpQpxuAyZVt6Zjfy49GPVvp8CpOZN-HdGalZgZY1BdG_f81g_h6_KZR46fybxdVywi-rXzjfMn8uz8hebNDXcKWT5utHPz9T8jAC85K6rdMZHdt1XmevG-2IGUg9Yipmxx1TqiwU1aKK0jtYiK8NYTXGjeOGxMtk56xB9XEp4DCzmGjvsHyDnb_0PZ3pd11pNipElbB_uE5uITlFF7Ek4JJz1bHtfAlOnyUVkUHe1-F94MZh_8Fk0xcwuSUH5so-FbD1QVImPvFnfGR6hJoJFdIq9AgMl3-XHih-Lc3SfVq6vDH35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=uCFaisQwoo5Gd8taqvDEHos8pkofSnjS_4ZFqpQpxuAyZVt6Zjfy49GPVvp8CpOZN-HdGalZgZY1BdG_f81g_h6_KZR46fybxdVywi-rXzjfMn8uz8hebNDXcKWT5utHPz9T8jAC85K6rdMZHdt1XmevG-2IGUg9Yipmxx1TqiwU1aKK0jtYiK8NYTXGjeOGxMtk56xB9XEp4DCzmGjvsHyDnb_0PZ3pd11pNipElbB_uE5uITlFF7Ek4JJz1bHtfAlOnyUVkUHe1-F94MZh_8Fk0xcwuSUH5so-FbD1QVImPvFnfGR6hJoJFdIq9AgMl3-XHih-Lc3SfVq6vDH35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1cXkkPdOrfEOEnb55NUQ829GwU5t0DZCaSf1y12W6CHkc_7j_hVjXSdhMbRXTRgQqV7ELPwy9BbKbCs3IXmnEDxDKfah-N6nQU4k7EXwkowCUvkZRFhFuNspEFApJaHKNiEX1wHrMkHuT_J-uVJ5UKy4fLUDJQrCbG1D8yjJDk9IaeHjQZl8uLMzYxxkzvAdqHJL6fR9rm2ypQK0oh9bvyXcmbLiGrk7HsHAvbQanU5RK1_Yca2UM-doAuxkxhZ71stwjPThFflKS8LjYVu6Fri-HHf3YxSRc5vj7e_DxXkAgfhPUpnBn8AjWJmjW78DjvJnsZIQHizwfRkSbaPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XDuKj3TBf688qCY3EjbyXxLQAz5_9WX__Vi0ISvbdocapoCX-S5gfqWtCzPjrCVGWZ97hhP8z0WBjcQhqjGcEvqBDrStJj0RJev1PwcymYuUSReDwV5RNM7DMYGszac5Cu7D-Jt06Om_x6zExnsy-djuPKOT8wEO8bWF_0PDVe08f9A-c6Bji9VubQu4bRKAMJcjvfRfFNMlQN994efp7rT7xCQs_Sov4K7R_7dLUer8D-63AV8w9z74BUnUMSQbPScVQj4C6AFQ2ibLXi7kIPFUYs43bFgILiEWrjKdEYK85PCR9MKRe6WqnLlhdOTEnmdbpsIsfMX1YhVCTiMiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Izgq4oD_XqUvcw1DPTP3Y22B61wdvBmo_7gmWz1TY8SzWlKRVX9ODSf8nONh3Yo8RHf19RlWamXpwX12mq08ShXKhHRfoEZLFsNHfr66pIH6f5CCBqAbHFfWNe8ciNCOYIP_C8M9om6Sf_56NBzOyieJPmxQVI0kA3A9L_MMrFDOI54gi1sehKSBJA7Q1UuC73EoiBdqq7SMMgnQP3K55Z0KVrmqcje25bPsSkytsX1P528_j7AhFQWH9Zhp0oY49qV_U8Vzugx0LBkLTtJ61TQi5F0Aw5kdLf3F9Y-G91cEjol0IlT5Q4_L8lE4NC6ogzQQ29z3dFvc29RcTwIvcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mS95MBMxcR6vLY9423eOaCet3f0LehbE-hBQgyDFRuKilxi-671p559bCDk_OMo4TSAn-yKU89ZKWh53hvVHqix1tk2K3L_vQZ27lVQBokeYmeeQmgIy7k4QP8RJ5aeWynSVj1W5yLhqiZkTe7IDsaW22a7cP67-56u4iy32lfKf9WaJ91Unv4vqfysZocHuOdFUxAzIpNbTRfh1O49-9aO6IJITJ_bzn00YIzVeGm0B19gIPHweazdch7w299mvVnk6IIIGJfZ1PFrChvhB7aF9fmtx2NEeZQHIiw9JAKw76T55GNgs_4iLFfpnB1h2AhEXmw-rYJAowYzPGub9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F_y5-oJx_S3pxtmHsvjkc02V1LGSQdQQvrR1lsNDhFgMTBrdmSxqwM88sd0eM_VDzk-9LuKPmlpAO4SnroHNjnT0qGmBBWr41nVNOFIiRI2KN5HYF6OHX4mwLDoOLUPMRq7EVYsFwrshYFoS6jmRl8mdYzEJDIPlag0Cz61W8ZYgg1A07zLkrTODH07_JZuvDFE6CJSZu--kJNTezhf-Wgh5oSclLC8KJUTiKQglwcJy8FVmncAwOeT3lcim2FKHmVmzoPX4N8HaVPKuC1E1oRpTe9jVt35t0nF9U_VLHlR9Iz3Ms6zLp1VUxc5K3wCAOJBR1oOYFsxOTUX1To_F-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او تاکید کرد: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت حکومت ایران از نظر نظامی به‌شدت آسیب دیده و بار دیگر تاکید کرد: «آن‌ها دیگر نیروی دریایی ندارند. نیروی هوایی ندارند. همه‌چیز نابود شده است. نیروی هوایی‌شان از بین رفته است.»
او تاکید کرد: «تنگه باز خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت و دنیا ادامه خواهد یافت.»
رییس‌جمهوری آمریکا گفت به درخواست مقام‌هایی از پاکستان، مرحله نهایی عملیات علیه ایران را متوقف کرده است. او گفت: «آن‌ها گفتند: می‌توانید متوقف شوید؟ ما قرار است به توافق برسیم. و واقعاً چارچوب یک توافق را داشتیم؛ بدون برنامه هسته‌ای.»
ترامپ در ادامه تاکید کرد تهران پذیرفته بود مواد باقی‌مانده از برنامه هسته‌ای خود را تحویل دهد، اما بعد از هر توافق عقب‌نشینی کرده است. او گفت: «هر بار توافق می‌کنند، روز بعد انگار می‌گویند چنین گفت‌وگویی نداشته‌ایم. این حدود پنج بار اتفاق افتاده است. مشکلی در آن‌ها وجود دارد. واقعاً دیوانه‌اند. و به همین دلیل نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا در بخش دیگری از مصاحبه، در پاسخ به این پرسش که آیا توان و مقاومت حکومت ایران را دست‌کم گرفته، گفت: «هیچ‌چیز را دست‌کم نگرفتم. ما به‌شدت به آن‌ها ضربه زدیم.»
ترامپ تاکید کرد آمریکا عمداً بخشی از زیرساخت‌های ایران را هدف قرار نداده است و افزود: «پل‌هایشان را باقی گذاشتیم. زیرساخت برق‌شان را باقی گذاشتیم. می‌توانیم همه آن را در دو روز نابود کنیم؛ همه‌چیز.» او گفت به تاسیسات نفتی و برخی زیرساخت‌ها در خارک حمله نشده، زیرا آسیب به آن‌ها می‌توانست موجب از بین رفتن نفت شود.
رییس‌جمهوری آمریکا درباره وضعیت مذاکرات با جمهوری اسلامی گفت افرادی که آمریکا با آن‌ها در حال گفت‌وگو است، به گفته او «منطقی» به نظر می‌رسند، اما توان یا آمادگی لازم برای تصمیم‌گیری ندارند.
ترامپ در پاسخ به این پرسش که آمریکا در حال حاضر با چه کسانی در ایران طرف است، گفت: «با افرادی طرف هستیم که فکر می‌کنم منطقی هستند، اما از توافق می‌ترسند. نمی‌دانند چطور توافق کنند. قبلاً در چنین موقعیتی نبوده‌اند.»
او در پاسخ به این سوال که آیا تا زمان دستیابی به توافق صبر خواهد کرد، تاکید کرد: «من کاری را انجام می‌دهم که درست باشد. باید کار درست را انجام دهم.»
او همچنین گفت مقام‌های ایرانی به او گفته‌اند محل نگهداری مواد هسته‌ای به‌شدت هدف قرار گرفته و «کوه گرانیتی» روی آن فرو ریخته است. ترامپ افزود: «آن‌ها گفتند فقط دو کشور می‌توانند به آن دسترسی پیدا کنند؛ ما و چین. گفتند خودشان توانایی دسترسی ندارند چون کاملاً نابود شده است.»
ترامپ گفت: «نمی‌توان اجازه داد ایران سلاح هسته‌ای داشته باشد. آن‌ها از آن علیه ما استفاده خواهند کرد. اول اسرائیل را نابود می‌کنند، بعد خاورمیانه را، بعد اروپا را.»
او درباره افزایش قیمت سوخت در آمریکا گفت فشار اقتصادی ناشی از بحران کوتاه‌مدت خواهد بود و افزود: «وقتی مردم توضیح کامل را می‌شنوند، همه موافق می‌شوند. این یک درد کوتاه‌مدت خواهد بود.» ترامپ گفت پس از پایان بحران، قیمت انرژی «مثل سنگ سقوط خواهد کرد.»
رییس‌جمهوری آمریکا در پاسخ به نگرانی‌ها درباره افزایش فشار اقتصادی بر خانواده‌های آمریکایی در پی جنگ با ایران و رشد هزینه‌ها، گفت شهروندان باید این فشارها را تحمل کنند زیرا به گفته او هدف، مقابله با تهدیدی بزرگ‌تر است.
ترامپ در واکنش به این موضوع که برخی آمریکایی‌ها افزایش هزینه‌ها و بدبینی اقتصادی را احساس می‌کنند، گفت: «باید تحمل کنند و باور داشته باشند که ما آن‌ها را به نقطه بهتری می‌رسانیم. اما من باید کار درست را انجام دهم.»
ترامپ در ادامه، فشارهای اقتصادی ناشی از بحران را با ضرورت مقابله با جمهوری اسلامی مرتبط دانست و گفت: «به مردم گفتم متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا همچنین گفت کشتی‌های حامل نفت ایران که چین در روزهای اخیر خارج کرده، با اجازه واشینگتن حرکت کرده‌اند. او گفت: «ما اجازه دادیم این اتفاق بیفتد.»
ترامپ در پایان در پاسخ به این پرسش که آیا حکومت ایران در نهایت عقب‌نشینی خواهد کرد گفت: «بله، قطعاً. هیچ شکی ندارم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP9MHz64B0YcCdz3C8OEzBRQ46RXZJ0OmluMQxA4VGpATgNB67cQDrPO3z35OGNPKUowyJUTaPthZE-N9delzb4V6PIAg7n5G3BhF-gMXrgkoedJiBoJoVAJ3M7uWxr0S00fCFakWZq9YaBLXFAwcrCK7N4LVLiE78S_TgS3AV1Zelq98en9okshi6FnFBbwleasfxPWIbhQCEijgjo-TYf_tYG33YvE4US_oERt3C_2NPS1DToLEn9Wsq4-guCjXqdUkANu4OAPHFCdQwQvAtjFDYQfak8719xSV2niK4-RqmFhMaOmtz9rIxLs7t5tioabjRZz9vllRlrqYeVEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdJoxNGdEH6Lx1d_P_lfbkAnGWqV1G4VVZ6oEmHBopzcBo5Js2HAqGjzpgbz6iP6YlWG6AFS-DWMyZNAXnwETZ7gPffH5fcl69lp6PMciipRj6JTpNh4eq7DTbnQpLyY3kQZq_IOiBswoM5K90cT4CVykmQlCCpWtlWtsNlYNhjJnUrM8GBj5e-G8FL3XSVO-5QAnOfqOcADahbw9i8SdncT28my5kix-sm6tW20anSup4FA88gczTcUM9trKGL3jnPuOCzATUtQ0lgvzgG6HJYiRjbO209UbizDcSP62Xd1NmzTL7-6Q6ao1e3RFfH7G2vqg66-0LD-GWnSIAtn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGLfuygO2GQc79XPRb-PDIDbbTVtbLzsMKU0ze_1E2NNVgGaZuJ5ed7xOB-dzaKtgV0g0iiogdkoYnh1nTJuL8LFau9MJflBeCW3GShpSCW7YbzYZEwekBfJ-uDyerXSGZ9PPOdEvKSCoOFcVxaMYsLpBeOahQAGGqjoPQb9nr8yGyP72eARzuGgc7Jl1HNw-wgr-Rg9fhF835_ar_G1diXQEr6y-l_Dtfi7qdePtvfNXjY6bnwqJmtpiamSoCqotUeIv2QiJ117XPRyrOBx9IBRTqING5owsqMuqn1wJWkvedeCse2GOgumVPuz1bTjt9gTYyRkyVMhldA3Wn6Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vf4rCEycw2Yk_0qS100haXG2_JGfKxma3AHvWRpZDmElgyWJBFEj0co6sQydDE8qChTyio7gTvi0NWVNKch9hvYDU3ChO_S_DyPELIBMYIR90IEIR9-jShdHQKdFX2we3fK6wuQJJEUJ6mCilQnsmPHNLsbKtnN8N1GxROXGeHvWK97EHp_pDlDC-EIuHI0r3GSAX-tDonjE3h8ZwcxUFGnmp6T9DFf3k5-z_x97nznZe6CYBk0gvGa-Rv1GKZ1oegJ7B9Ntt6N0PYbNY2MFjnscxbd5c4ZsV-NaCJQEuile3ltNrlfkNHshQIBxCBTOR9hAxT0L8FtYW1FeWx_TJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=noLzJJ4nHJoPBNKaZQ1Xzpga6dNtfLwJ9mVAK-w9FEDA2CnTjAYMQLcU6XH25oUt14LzoSX1SfO3A2uQngykR9sHTJRVUtmiJiKziwumSixplI04r_BJKQn_zBt6mTJ10KY24WeGboP0KTKkDYl0hnn8Lxcn98mhfvz-J_TxIKO4C4y7uxJJ_-4JmJpIPj1JisXnzNt-NIDxLekeHB6qKILLnViuYf7ngv0OuWRUt8Jisq6unKy16z6MCbh1JjiqIUgrha4l4Ia4-Etnok2YjOsjG2DUlnwraNeCcw2SkyzXttZlUTGZM5V2S7Q-WjpPkiwnfk97YdUAdKs7tWx9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=noLzJJ4nHJoPBNKaZQ1Xzpga6dNtfLwJ9mVAK-w9FEDA2CnTjAYMQLcU6XH25oUt14LzoSX1SfO3A2uQngykR9sHTJRVUtmiJiKziwumSixplI04r_BJKQn_zBt6mTJ10KY24WeGboP0KTKkDYl0hnn8Lxcn98mhfvz-J_TxIKO4C4y7uxJJ_-4JmJpIPj1JisXnzNt-NIDxLekeHB6qKILLnViuYf7ngv0OuWRUt8Jisq6unKy16z6MCbh1JjiqIUgrha4l4Ia4-Etnok2YjOsjG2DUlnwraNeCcw2SkyzXttZlUTGZM5V2S7Q-WjpPkiwnfk97YdUAdKs7tWx9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQL1rNqnvLGLNN9twwJb5lNgb79LbvVay9Wbn0YKxOMlDDE0jqauoNIw2caj-2LWoRN2MQAwP4Pj-gC7r8SADAs3Ui0L-tsk2L_EtPUA7vS4O8afC4W5YMNHjQLuTpEQq9iAaqr09Yajx5io3IQwvQL4y8NimCOWft7sxZ73NH051zrjeHCvcLPTd4zR2_iZU5Cnf6iHIlvReBMR1qpkzfm9hWalwc2u-ckOZcKwdPNZ_5oGVeXTHcaHJxJKUIa4gycGYQydudoGfLUcWZ5xk3YQbkgeEtDZ5OqJdIfVTk91Z-NWPk9vtGPr84dO5n-Y-yLyh3LQmBF5FadIWAXfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا سپهوند، عضو کمیسیون انرژی مجلس شورای اسلامی از کمبود روزانه دست‌کم «۲۰ میلیون لیتر بنزین» در ایران خبر داد.
به نوشته خبرگزاری تسنیم، این نماینده گفته که تولید روزانه بنزین در ایران بین « ۱۱۰ تا ۱۱۵ میلیون لیتر» و مصرف روزانه بین «۱۳۰ تا ۱۳۵ میلیون لیتر» است.
سپهوند با بیان اینکه «در کوتاه‌مدت امکان افزایش تولید وجود ندارد»، خواستار جدی‌گرفتن «مدیریت مصرف سوخت» شد.
پیش از این وزیر خزانه‌داری ایالات متحده گفته بود ایران به‌زودی با «کمبود بنزین» مواجه خواهد شد.
اسکات بسنت با انتشار مطلبی کوتاه در شبکۀ ایکس، نوشته بود: «در حالی‌که باقی‌ماندۀ سران سپاه پاسداران، مثل موش‌هایی که در لوله‌های فاضلاب غرق می‌شوند، گیر افتاده‌اند، به لطف محاصرۀ دریایی ایالات متحده، صنایع نفتی آسیب‌دیدۀ ایران، در حال از کار افتادن و توقف تولید است. پمپاژ نفت به زودی متوقف خواهد شد».
او سپس پیامش را به سبک دونالد ترامپ، با جمله‌ای که به‌طور کامل با حروف بزرگ نوشته شده، به پایان برده بود؛ جمله‌ای با این مضمون هشدار آمیز: «مرحلۀ بعد،‌ کمبود بنزین در ایران!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=tmI1h6n2KqyCOwU5f37ivgS4xoetWHEeCcPatF1n1iqOWKJPiUv5QxFLcIlXZI68cVnyp7fsVR7PJ8iV4UsoroSJc9cXgwh2FfdWqcRCRFyM1-GaEf5VO6LGt9f0rncsCn7rk1U1T7WnUt67uEsN1MbjQiscgqicTrttcMxK7vHn-h095c3kwEKWFHIIHz7-Ysa4fnjZnGOYeat1yluTAp_iUQjzFMhEHTa73nbRF-K0H0KcwEarDjY3xrhoql0w9nPHHqIIqZthIcGfHg-gkINHb8stGpjjuvCYtCyEkpM4FE63rrXXk-NBfRmuZbRoTKra6QXYRFSBMX4LStW2TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=tmI1h6n2KqyCOwU5f37ivgS4xoetWHEeCcPatF1n1iqOWKJPiUv5QxFLcIlXZI68cVnyp7fsVR7PJ8iV4UsoroSJc9cXgwh2FfdWqcRCRFyM1-GaEf5VO6LGt9f0rncsCn7rk1U1T7WnUt67uEsN1MbjQiscgqicTrttcMxK7vHn-h095c3kwEKWFHIIHz7-Ysa4fnjZnGOYeat1yluTAp_iUQjzFMhEHTa73nbRF-K0H0KcwEarDjY3xrhoql0w9nPHHqIIqZthIcGfHg-gkINHb8stGpjjuvCYtCyEkpM4FE63rrXXk-NBfRmuZbRoTKra6QXYRFSBMX4LStW2TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
نشت نفت به
#خلیج_فارس
پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
#جزیره_مارو
[با کیفیت بیشتر:
۶۰ مگابایت
]
KavehMadani
برشی از سی‌ثانیه سوم ویدیوی بالا درباره وضعیت ساحل بیشتر مورد توجه قرار گرفته:
AzamBahrami
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd89H_CiS4aeIk8y-t6Dx9407rskhVSABJ2BYGe4G8HlJtpmUAwHR-vV-NZDW0Kq0IRQXm2xE041w7OcoWeGPc2QdXUjYI8wzX9ZOEujrV_Yv-2FBcHplkTkJseGt_gOdHdSzBJE0ihaDg7C7hz4rbx7uPMPgriElzp7byRQbIBsOUQDxMmupgJdKqKblN1Zr9Y5vUHIodk_GVweGWofkvuABXoXXqcmYd5db7cI7zJXvZOaJ01X5tMoLtCAkPwQ2HXIL5zpUlE-4CiKzhYXTimGw0Gwcq_I2CJ4XWTsw3TD79ORADzYKs2gmKiG6KB9oQ71XKO-BUHaKWUVub_Ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFylVB4cUUFCSecJf50uzn5MTxHQyGMNU4X6aU-YXtCPFo-WEHKaLlvAp0Nq-Iv_2CFJNsWONaQgBUXWeRJVfcwEv8qYFbRSC22g9dtPDl79mJBBcpLkcK3s3mSi3ld1ekX5w_NJLx-hBSaVcsblM2TJ7moo377MUiChe6v4toKVK-2z0hqdGdnv-CrZyqqOAjpRFuXjtNe-6gvmRrgwFr0w9jUoi8AzzCYqC3_qktHCbmiCsbTQ1VsnWLFU2QdCV3ZZ5PiY9SAmBlGGP6-mkLb-yCbISCC4r8A9_lbvpdBrBd37ZeZ04keiHG3uVN0wI3K0NzyPwdVKWti__uiTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rsy-pcpfRUaMS0wetnUq3eloMPzvB3yxEii3fs1dVqGtSpWBp_2QporiQpY_u0C06IeFuM7F_aed01aERrdy34w_XTWVe5ZYLsQ4SR1lfd5UHIkjzxT6ouehOwz3sEefCOy3b_PESVW6U0auf892Hbz7Nickqf0-jK19UbLT9fNGmv2Q4wPam2I15rd7R2p17OJMCSm25U4pXbnjS9z0fF88sSgNBow3qcquOjhQEksZyhTC8x7cFGGE3RyMk_G1mLnCOksCKs9QizO3Pf_a_SEvlVstIezNTWX1eRbkMKm-D1mM-Z-ys7xBuamNeZockhdfDtsh8-wJfT7OqoHkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UNwGpHTJ3ztZ0b5CD8aP13PCfpw7WM5umA4J37Q6-sodT2JskIfRtxeJyLFFZmfeL9jb2bQ1HDfGafXCHdB84jbxQtTEM6kItT9UXitvOPy3jaxOZyxQQrT4xyi0yJLPj6tC3J8KEKSVSBkO0GkgXV-qN-CvKWkrkb7AEFrgCZ4l_TzsrQkN2qoUKLt4lp3dsQUq89hRzWh_aiNemgo-5aC25075fgvIsXfICR2ghRP2MZqFScESBRIL6GyeUoL0ztHvMPP_LVfKM1vcibOOlovoBVVH_1fAthEQtxpTIQMEHN62Z7bYXWIpxdYtXzTu3E_qOS2XycuDWS2dw8ejZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uWvxUeQeUbN4UNTJNecJ-vN18UHhTPmDzuEEVQqX8Md3ovPhbLOeuCiJFsUwaYSnktnTbuw3-aL1jK10JUm41d0kliXciMs1PXON8wedF8U3fuIEDh3A1SYwks6emmXAa3pSETQlQVy3hsFJmuksUBK5_K1RbNydYZ9oz2Zagv-sIQ9NK-_d9oOuhjor5xBispw_xH2kJnXifny_JIta8w3ziKDaGy6_IzfbshFJDiH3Me2CSp8XA19IM3XIiip-6ojf8an6dJzXphWlRm1q7MiTu1ifCrR91T505mrkWKgS30jWe0XJ1plQMIbokt-cao4KSCljdeU5MTY8h3ZlXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=kvBel-cOJ8VI0P5A6XxQDwVsr8v-wHfm9Ae9JKFj3PkdJQw6tbaL3U3-YrU8-3AifUfP1FMfNaQ6HLiFM3eU8_LfoYG9-IaGEK8U5nuiqSAJt6dWuycVLPKacldx0Dxs1AP6TvaHL5WMNlwK8WwXv0AcSgOyYBfmBRILvyqMnZfnYXj59TLGNbTZn5Uw4TGRpM4AB7biI6ttFulyobhapU1IY_b8zde4JIhaopmyoPfKOYOdgRMfIntHq3PG-JdKkIEXfl2_WglRB-622T1jsZdsatpKwcMaXMZ1ZGrYnrKsBFmnRRQjF7nIOJWUqa94G7_4lq-ilqHPP_pZQsiINg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=kvBel-cOJ8VI0P5A6XxQDwVsr8v-wHfm9Ae9JKFj3PkdJQw6tbaL3U3-YrU8-3AifUfP1FMfNaQ6HLiFM3eU8_LfoYG9-IaGEK8U5nuiqSAJt6dWuycVLPKacldx0Dxs1AP6TvaHL5WMNlwK8WwXv0AcSgOyYBfmBRILvyqMnZfnYXj59TLGNbTZn5Uw4TGRpM4AB7biI6ttFulyobhapU1IY_b8zde4JIhaopmyoPfKOYOdgRMfIntHq3PG-JdKkIEXfl2_WglRB-622T1jsZdsatpKwcMaXMZ1ZGrYnrKsBFmnRRQjF7nIOJWUqa94G7_4lq-ilqHPP_pZQsiINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5s25Tf-QesOrC1zcCt5jAn9OR43UHxQ9HXtsMItim0sEqIha69OVQh6Pcttt4YsTcCklCSOJpLtsJqzIeLJGSYZgyKePBbRx6cz9i5vyRgzQWFkz3BGjhLA6DeniNu0B3MoGgFhJ2qyi8VdGwHBmZzlUoEahX2hkbQVNRFui_XccojAtEQrENwOE0dZ7B5ZlazqVd49jceju1huh0mcCJcC7JqaCzGjbcmhuJ5v_8GmE5WtE0wWCPL1SDsSLoyKK-D3vKtnkCnBBQQCyH1MfKICkcfsI9WBalK4RwjSaesaX0f8IE0xUGAPb9ya9yeuwBTEKV5P4DBFnxDYL8E3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEUtNaD4Xyd6h1l0vsybd5qlYh29Jmo5vNbwhEkPlY6EzysAj6YfIXl6o6JugPHayHj38_v_N115GALUCLmeTSbY0Or1Rwevek4Ea-FO_GqHqW4qtyrFkvbcGWt-KMX8Ogw_69-kJcZWa_VpQi0emhZfF_a8Ak3sA4aU0g9GjZCdbtgmp_N-8mVL2wj4H31VuVAeXCuCyFbsGeOR5bnW7aqFWO5al37p-N7M8-fR5YCSyG5ZpiQR59NXTRIp9y41GmgMCNzpe21OdWVBgMq2tzsYqabHMin9H6n7qwsceqMQAgiXZ0MkU2YcOtAo1UCMx6l2Bugk-3aKxO-oEjyRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A5495GkWPQ6QII32XrvICYToko7cE4wwpJV5SZ2i8UUXNZ_ZntF4pLbqfD3OjYSJ7dzj9iYOZnoT4KpafjXR3XtMJ65uBdyJQ5CEB3BfVw9i-IEK27wHlgunEOT_o6qnuW3Slivynq8N4spin0DBe7pHN9-9aOBifuHwcrRbumiYdce-j9Adh9_Y7kIfcN055nx20_4wEnkCfgP6nvN3v59DOey8AOZgwfKfY85I69hxzQZM5UTcawlwszIcihwdFtS8FDhOwn7nWbL13P0TcNfJPHL7aCAW6NoCkmPGDOfaXspEDVnoOkHRwC9w82jpMYwD0sSuwg0R3qzNK730Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GMfKoShSnC7j4C6hYQtrffUSMjvocyA5USNql94_wnDSS7AMZIu4g0Al295gjuM6Rx9zfLF8DFPlvqU-3D4y4ZHQcGvQO8kaHPIDo3cLOSGTNGVSVcD4YvecX1trTxsD71Mmbinjrj4AKrJMkco4SMY2JKjPqN71IdxCUql8Zb35U8hWHNbbVaIkTb7A2fS6S7O-v5WVh64v9cSg_2qbBTg8vMJIhDqakzFVzA9re4kYGMtZy7TWObJx4ov-jDA6uPpFBePLyEKOQeEi9lbmbDD1IxnhohGsVUWOEfIE697aTMDh6bJYeko4YmHQ8UVRBQZ_oc9GhCnscYJ1MVh0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tll5P4fM0nPJppsx9Xs3IHNKcwnmzVVB-eRxdsyv5DRg1zaAKSBJrVrc_XzvMqRD7Bl9MZj5r-InxklsZBjv747RQTMgMVC7Mfz-4o78WxsrD5oKWPaBIkykYdSlnirIBTV40KxrSfXh-XxqNHaXvjo8Woy4M6zNOWFNBgzyQtl16PPLx7OcUD3KGL0ACS10pKZK51doqO5Llg5YQcT70S0L7upPOhT9Hg28AuthtatoQrnp70BSz7H6g_FgUgIFD4mrCbi4Ss2oKM44vf8VZxZfwh13GnGBCcYRpyUmOmqOxMiee60blXFt23jM9ivXG6ShC0FXNL-qnn7vK57ntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pmNAVPnxF_2FF7hFp5GAY2NmnK6sjEiz_sKfJ1zXtIO-ryn0JMo3j8IbwW6KTjPJH-caKtneIEJ_e-Bk1qVxT2IeV5GzIVcisS0ERmgmRbsqQvU1xvohWTicH_ygpW0IbH-Ll_jxHgktSrWdeljyF0lOAxG6pL8N4RVr_6B3B1e1JsDT8XXeB-q-3hgSxqobwOjleordNhLrsR0zG3GSXdGCLB8UrXIZyacLj-lV3ajQUTsoVbfzp4evfGr-C3fjFW-70WsTLq7PeuX9DiU9CRQ6e07ok_qp-waA25hczqh9n4H9gwfG35hFSn4cBCvf2D1bWf9xT5CyBPaLDb55Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cKXXUbNNej5_s_GyYGkWVXI76u4dutLhbt72JkogRDE4jbDwk4RtwZ9jiGmoQ1dGhU0Vysm5Xb1GUIHnXTcWKoyqYCcK9SiRfsLTvgeFUnOmLcwxLEvhnZv5z0cviV6zn13gQn0x6XlJTV1r5KOA7x46Vsy5VQj4cQlaqu_Fhf2fZrSN0eI2EXiDpGQIDA4LJi3ow91use0q1QKyup0T2cELv755kecAeEfADwregtN1V__uFe3g0Kb_-eX4uBBHmvuWmQGz2yp_C3r8dSwqqW5OGCMU30ULts4rpwMwkgqyH_JvBSL8Xl8KhBSWPy81fJrS4Xe-xUgK2gVRJ0rK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KHz3QUGkcQtuKhcV8vLgiKi43hAsFURkgrVGT21CqPjNq9BaaVndODTdnguONou1W_R8BzzurV-W_CtjIiwk52vzD5AC9GhdcvKyOngXXBQGVpP6JSbJ3goYdIaKkZdO_KXGjSgPr5FOjS8Iir317aDyGK1O3YYVeX9PooVsGbw3dyxTJxjCAQlverfTHx16zqIV0jDDj7qL8JphehL8aksDfJlONGabERZBL0IQz0qoX8f2PU8Meb0JZGX6jRxkORcTfHXpHb0p4BvlLdBuxEVJW8K7gUE031XDMyJbYlOgOhV5wVAQEctkQ59CmVaLz2FQGx20VXBA0XO7RJl-Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vILF2i2MrK9Czh3TRbToi8Bub5Ptt2yty0en5Dj_57WsH0WrHcjzFIjWyBMxdQqDZBJHmcOYY5yK5tOMsMZ_cNDbuCF1-jJrVBSrU0hct6VWtof1bIyhGgYMvw4IQrC1UpFmExzBSDOEKD5SeviOq5dIymHt_OmHMgxV1eUtZWdyVB7GG4UD6x1IxIy6UEVx7dkYf6suJFTFkuv5u9Ga7hu6o0Zgc4YPGue8tV2hzHOHm1ryTNs75g6KVn6LbvHFEd8B-yT7KXpJGR6ZooROLAS1PR3-KziRmEjoVset6kAXXWvroWa-Tvpvltc0POEnIVLO12LPx8o3HD_5i6JBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVK6k17oQm2DpEjStRWejkG7lAmwcJMSSbepTQlVsLgHbkSJmiXHN_C4NqDPtkvSTyQBPaW3c2-sGMUGbl3N3aILFWl13BWfcuszsMZ0o8C6Qo0-9N-NwnLIg_7TIGY6ZhlcSzRP8qu3QikIZhYJj2uF81xmhniTJYbOTC1VzfWonl8BC4nXH-23l89L7CS61H7VL359lknUZIOX9GtP-NjwfBNjalwONUjL-RAFouRrQG5F2L0gQhZftTCpCw_vpTCxIaWNo0s6v_k-vv-zNZPrYEUpvRwdkKDTDmeFZ7Chd46RCIkaJOlSwnn0FGix9ozZ1jQDDDuh8_Uj0DMWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKXk3oIzvaMy0E0shkp-zbPVcnGsDjyWVmH2433p3OemC6Wj2udxitn5dtaLAbflbEnox6s3D-CD4hIVRvdwAt-G0OhD9pirJplagtVOxOi0iUSdn8Rw206FLaGIvhh2RxULJRg-0AFJQFHBaW_Vm7cEReI5H5V2L1sF4GzU81mIvAUQ9CePdzi8Z_l8n8s8z2dhrmOYSE1N7NTzJQynHhI73cT9A2V8Lk4NnlsAhwXBkGRL3Qsvtb0zmX-G__ZaYcGqLKf6O9oJN0jc7ZKQQo5SfoAMeSP0myrxan3Nd82dJRflO6BZ9T3rK508ZgJCd7cYn5ONCiofY0Uc6VfuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX53eLjM3xmuMPV9nVQAWME0bJP6xdO-8tx9FAdGz-RNzy6osVYS1upQ7OB2Tr-1Ob6NOD3SFDEUDrM88GQ_bb2ohXrWMNdEO7XqvNU0EmbjZo-vgsMJf790x7XBQ4FEg11DJSwXedyMfqOoTBymhFOz4w_xRTIIW1jKW6e6cVGHAk97eFtpVNnUlOOk5RlyTnohOU6dYJyLuOg8PcUitAbX4iFmOjOMovSWTt2AH9NkGD5txdsQ4u1OfRgM-5lSQgIanZMtal2wn9YGuinSkO6F1TxDdIbb47czS7nagczHjwTtQTImk_4GLmWNdljrUUlyctEl_t_iUAhyYAa8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxr0foEO3FTgHKk_rqK6rltfyB8RbzzFA2jWp0sVOQFa0KjMezsOsyia_IcTHQQfBMX7Qrtp9UTtVTRm1TPfAKLS6MG9cZFcsnndp3uA_XyBGQ2ZVCmRSf8DivO4LvOkD_ZYGu3j9tZtCrw2QfsZSBgbgeYDVEBo48pB_cATZb9TUv3AoppVmJS5xXyROZucxSVX5oa5tDiK8NonK4hyov-wC6E_JG0CYo74hZBsgUYMSTPOJsgOvPq862BqqlkgDAQHPhBL0xm0XNB0OEAWQv3cz-SPCF0VMusaOW0MyhllSGi_MSY8X5FcYhX-PVn-G-M2rHc8xL5HTOce2F4_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY49QiEZG8pl55W5bU6XLlfQQ5hhQf5-AcDL45cI8Ll8-_WYPIEj6v39oYwfL09-evyqZAoaweI0jltYkyRZE36P43kZ8yb4xIBdJzrM8BB5fXwRJHIU3NRLLsg2GZppbMJOez9SMZLSr2D4aUyG6Ita5k2kIAgd3l2dTqH15OPzSfDoWMnDL9XHjFM2I7Uslq2Rop9rUzjz0uUnn3p1fnP0_TDkXCZdh8RLbOoyqe5P1hRrN4J6NbTcwiCJ7vk8ug4Z7F_pTqWAqWmkV_2xQfy18SEr2CE_LcMwp3oOLqx96AnPyBEnn7VV2aVGHzYG3KBApvobYiNDA4e_vWL4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcLBt4h2q5F_jj_Bfz2u-bZVfA_JaI7EymaYNsJSXUPiRE_AChie6zdrNRez8TgzrtQ07sBoiqeOls3vuxckWJkS7wGQBhsUNdLRrp8WVVgKE4d5OGT1Q2bLRizJxutx17f1FjzVYi27TDsO2MvCb35GCSBBReojia4aJGMnKVBX94-l73xMhtsUy3bXu-d1PdSJKLPdR3MzI3yhksVpJsYoN79FdKo3NxSCqHm6WRzJpZRHvjqJ9V-v5zYOel2lyYeixU172wev8E4e3M7F-z5i0DHSOVorNJr5RdLZs7Kl9C9iLcn8lMBco1mS9XBj5pjQLtjreE9dfzg7Bvetmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLqiJ3D0F9V69DiGQx0rY-U-qf9vwzFQtNb4QIHRLSr9P-Iz1wt7EcPx6vBrcoc3l5mT6jwgqxujfuE8A14UZu864P8O0DV2Cytp9UHDnGGiKnX9N0ChZQZn7kGk5Sn7m-NJ-FIH18xyaD26tg22ShlMbSNew6Mj7CB15z0ot_BffPyqMqEzfFzT3y9M38wQ72NtVM07Yx710PCOQZ3mGd8ZbdDY8bMVBQDASpdQo7qlSL5op3c0NEEVuzjMeuiR1xX_8VsFW4ojhgeVrC0WH7dUeWn39_ONiRPwMpcWSQetp4N-fqj6iZCL22aHOGAGpMy6OXIkNRwAOSVQ0QrJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSEqfqs3cJ1XBClOw8uQIijPLjtOrX9adCLpJRf_rU3-NrdWwaKyDEiKJV2PUw0_Pn9v7pyA6dSs3m7pVsxEMmo36r1m54p3U9qq-fCsGqHdKc2v28CsKCB5hkpIDoNNB-_WEkPE8zhlr0h4G70Z1fZNxg5Ot-vkblaRTn-P6Cs2LG-1p-iM1Dp_uvZlFuM0AIvGcc7IOZMqbyNNfshT130GpHH-NRp6oiVJO62DbvaYk2QCsNOzlsncXxhYzUosHnVRkSc8ZDrJglMX8_rQyFlcofB5Qd0JA4DMLHHsnrT6i9UR35SQIccO2pbcUFdYLeERogQVcOUSg8IMPYGhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeR1P8irRB0QiD6SADQdWk-RnPKDUMrdP-BNZjjxEA3o3R8VvyK95WQNG-IFY0-myHsSEYsjaRkdFmpRLmXMLnWesjcOEtIfBG6YJA-NPZ4PhZlvCasCDHVN_wSGQINRUkkgViflERow6G2wQats5SaVbv9K8StA8xZiW6SCPEZN7r1DEa3T7NBWICb0K9hQ0a7R2dfp8bz_phMFcMr7bFSwM_7n3868ApRMzArGAcvDT4cIIYUAaebp_dHlO3pRTgA-thnXQyAB4KDRLcxBS47drUT4fxedNvEme15Seu-9R166tM46Va3X_9aQHt48xK4slGPTQUr8ijBoroDBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOtxB0kAQMoThBMt864ecao29F4gP2cZ_A9XRonFaCOGCDdQjDiewtKL15ZERrb-Vm9XUxkK-eqCT1pE7UVma-WtnCglZz3ZzreEvWlx9Hk6WPQSl3Y1GIoJ21ZZNCBopqXcWWzmhv5NMtyZ1vlo63tL4hwwMbB32Ldvr6sf9FO3mYa4snvs4CEOTfq8tDGTlexCu1NS0VZDpC18bEOexfzYnIpjEIOp7FyK1Xu8T8mOxIkYPBETQR2tKUMFQDP8eTRX_tBE319vpqSE4x8w603NM4ZwI7Fa0PD7yYXR5Iw31nWkSB2OSA1euOqdv9ngQc1WgVYSbtvc00KPn6cTnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq_bpAovXco9BInGAR1qrnmWY23CIE4kYBQhGEkDd2uS6sYWmp_NQ_iwNghoM3DDT64c-To10JsQyJDNNCwSxaKwj1co44iJE-3s-UZoh5c01McmeUAxddTRTWeoJEFnTGYQfPBS57ra8E78GNOIrVwnyt4fF20F-KRTfhai_2iUWih3euWxJ_9M0V5eGjZBjCKejOro2ufq_8D4h2ISsMBYNNcwyiqqXWuYABVYajTNHzqht0Za2vyuF3Wtcf0emicY389ngZi9fbDGJIyWpxbYSWxv9teXQX0mLrqevzqZtedaEL5HR7-vi3jIMGzJX0zTpJea0YUTmG_WHuxqwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vgIjaAUPIN3m6WDmLV4wIBenPTM3zTQiEVTW5VaXOKrySe1ifQEqlM0qJneTi_E9Et7KQOuOyIJgzjYIkiQ3JhtvTJytGFyyqQwMJAM2D-CVsTijjAScWyaWX17EOohTp4uR98z-QjnlZV84xsLy6gOiDEoH4ny3cT_e5g37g4OHeoyO-aLknqWz-iVFD-x7D2JbK9vOohue4EJxiYy0hW7cfHEEkwdzeru25qZMRJxkQ66YBqq-LdPCbLIsPBVve1gPOHMz-hCcRqazOIGWFxqd2VUnc5aYv3VSwXz4JBjU9-koiou6uVjP5QDgwt0uSva0P4ncE5U8s3D1IhiJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FA6Xj1XmJCDBBsWAAMU5SSOD9d8AL9D95JR-788pyhq9ZIdRPLQbNlNUcGenkRdNQB0IQIw3ZgixyQ7C_qbngbvkzYaN7aAfG669y-u8mJHc_09p0IjoNLXiJ1bwEPTPdA1JMd07i_Fwu3fo4ZXvsNQCfUGBuEJ4QIFF_Df2qbmMf0CfoCWrmFIX6oYROPwLITQbLSI6w3h4Qt9OXJUr2FKsB6wSbnLdYaLSlHi_8PDkqbDw7nZC1zxrAvolXLyYy51WiODCF7WgqV1vpW6xCxXxQBFP8b9fgOeJOjMkO6AQVbtVFlQvl9uPKLnwccrE_MWnDHHqChCv9UMSxHPy0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد بین‌المللی پایش اینترنت، نوشت که پس از بیش از ۱۸۰۰ ساعت قطعی اینترنت در ایران، نظامی طبقاتی توسط جمهوری اسلامی برای دسترسی ایجاد شده است.
😋
💩
همزمان مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر مسعود پزشکیان، ادعا کرده است که اگر همه‌پرسی برگزار شود، مردم در شرایط جنگی، امنیت را به سهولت دسترسی به اینترنت ترجیح خواهند داد.
@
VahidHeadline
روزنامه اعتماد گزارش داد که نخستین نشست «ستاد ویژه ساماندهی و راهبری فضای مجازی» هفته آینده به ریاست محمدرضا عارف برگزار خواهد شد.
هدف اصلی این ستاد، فراهم کردن زمینه‌های لازم برای رفع محدودیت‌های فضای مجازی است تا حداکثر تا میانه خردادماه، امکان اتصال مجدد شهروندان به اینترنت بین‌المللی فراهم شود.
عارف در این مسیر قصد دارد از ظرفیت نخبگان و اساتید برجسته ارتباطات نظیر هادی خانیکی و علی ربیعی [
🤨
] استفاده کرده و میان نهادهای حاکمیتی برای بازگشت سرویس‌دهی هم‌افزایی ایجاد کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdta12OtSH9FV1_3-GKivD4xbONEUk3z7hdh0ux0C8rXgVKv3XUYV5P7PO3c1n5QwRvq7PE2rLXRc_usHNjZAbXJM62f0IQ07sPE-dsX6XOcQbWIGgZ1iF6WUqgjMg0-eptLmsaLqVYNI9SlqI-ZiMTKTiS0SHdZQzX4teKgJQEJmr2D20mrj9AJCt4YAPk7zTmbp_Gujg_udYF3RaTj6Mj1ymjVcwMmCCfj8TuPn7DilRs9FXn3h5AxBieHqepJMTcUge3tcgHhtvH9oRndygzH2TedvE11-y5uuS3EXm2rxJ22d2EPq5-6PrS5OdE2KJx0HHMd8KHuCi6UcClT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی شفاخواه، فعال حوزه آموزش و حمایت از کودکان کار و ساکنان مناطق محروم، توسط نیروهای وزارت اطلاعات جمهوری اسلامی بازداشت شد.
این فعال حوزه کودکان عصر سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، ماموران وزارت اطلاعات بازداشت و به مکان نامعلومی منتقل شد. همچنین تمامی وسایل الکترونیکی و ارتباطی او و همسرش نیز توقیف شده است.
@
VahidHeadline
هنوز از دلایل بازداشت، اتهامات انتسابی و محل دقیق نگهداری شفاخواه هیچ اطلاع دقیقی در دسترس نیست و پیگیری‌های خانواده او برای کسب اطلاع از وضعیت سلامت او بی‌نتیجه مانده است.
مهدی شفاخواه طی سال‌های اخیر به صورت داوطلبانه در مناطق محروم و حاشیه‌نشین فعالیت داشته و از طریق آموزش ورزش و مهارت‌های اجتماعی به کودکان کار و نوجوانان آسیب‌پذیر، در راستای کاهش آسیب‌های اجتماعی از جمله اعتیاد و بزهکاری تلاش می‌کرد.
او برادر رضا شفاخواه، وکیل دادگستری و فعال حقوق کودکان و زندانیان سیاسی، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=TV09RaOVDpsunUUOUZROi5dNezwrpSybWPBbWdw2r-9aFd6H1slQmKjkeZNNMbTJMddAylx7WxzsGapp31ayh3ScQ0-r-MC8sR9AqzLB0eOsQlMyuVIMK1NsJwrum6mh6nvdIFyMpcyfKwPvgr2UWVQBQSikJRYouGcAOFBedSEkMhLm7eJH1kEK8Y2HycoTj5cM76WIqaARuNzOY4gtdOg-2Jw9TQcEwjgFGUGgFPDWOM04Yo5iRsebb9AEFp1sBWnRVANqWxzB7HPsb8vSs58Hzy_o0U6b2IErBr1ZcZvduxvpP_qz_1txt_Xww1fKjaP1k2hyKzfcLkElZcPyaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=TV09RaOVDpsunUUOUZROi5dNezwrpSybWPBbWdw2r-9aFd6H1slQmKjkeZNNMbTJMddAylx7WxzsGapp31ayh3ScQ0-r-MC8sR9AqzLB0eOsQlMyuVIMK1NsJwrum6mh6nvdIFyMpcyfKwPvgr2UWVQBQSikJRYouGcAOFBedSEkMhLm7eJH1kEK8Y2HycoTj5cM76WIqaARuNzOY4gtdOg-2Jw9TQcEwjgFGUGgFPDWOM04Yo5iRsebb9AEFp1sBWnRVANqWxzB7HPsb8vSs58Hzy_o0U6b2IErBr1ZcZvduxvpP_qz_1txt_Xww1fKjaP1k2hyKzfcLkElZcPyaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر پرچم حزب‌الله را در ویدیوی مربوط به بدرقه فوتبالیست‌ها سانسور کرد.
FattahiFarzad
دیده شدن پرچم حزب‌الله تو اینستاگرام مساوی با پاک شدن ویدئوست و ممکنه حتی اکانتشون هم بن بشه.
Sam1Kia
اعضای تیم فوتبال چهارشنبه‌شب ۲۳ اردیبهشت‌ماه در میدان انقلاب تهران برای حضور در جام جهانی ۲۰۲۶ بدرقه شدند؛ رقابت‌هایی که خرداد و تیر ۱۴۰۵ به میزبانی مشترک آمریکا، مکزیک و کانادا برگزار خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sH9YmiBpJkKBJ8K05IHQdItG_l7GNnpouYdhhNfUo5IRJHWXkFy4Hrr_xnYWScBYnBWf8vIb4cRbFfCMceiJzKwN8oBiY6U2AAoJD2ywP9GPXeqS7CTkIH8Dsc20c2KsEaWRbGO3hU24UkNbTltbhyiskSSZhJkugpAaafdbDR8ow4HdOomlfIyJdGGh9BOYLJWZOcyRCl1PmFuDMSD_JA5fOsN6-hC76Tdk9-i-ISb4ndB9ii6k3rpcWw8Y6UgHNL8Imgx0DyUH_eOo9dzOMwf3JtJrSF7Arbb1a3W1QVh_OOizGh4wXDBAfvG1zm6Ri9x_lSWeW-ZTL16GpPEIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bll06oCehLqj6gfTT6Lp3fWz5RxpAzB5oIsGJdFrQBbk9MvDkXlnWUjo10hadEA6_JWk0UCcw6GAvkQpaDgJBRxnppmJ1IShXObPR3Vt7aA96y2WpN4YGdn2DWXG8MKRnFCX8RCRbefDRLJxwvVHh2WNIsHA0oUkDNh6W7Ly6NozToIzhUx8dtNxtkBjcTcSqRAIK3A1kdRTlCxR6rRo0pXRIYbfpRHvfPy95GzZQrZY1J6GhSzSDVPGbDMWaT2DZ7PycZ0g6aIhDgKi7VZDeJNBU5lVavpqZG5huKwAe3jVRpjz8LYGhaPM2ygQKJoIrT_WrstyiEdiWfCen2jefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CvEmMWxkaJE13Paes7S84cqUUTlPwbco69FLJQrhE2FqbjdsZXf8ImLSqy9j-v7LAnDEDzgHEiIycV-kjGBS6nAZlKh_mHSqFnGAH1Me7Qjx88b6qhTAieKF4oOZ7Z8BsJSzhIU8X7yGJ-SrbzG95fjbVtfMZBS0NJAUOv-thIsqupcBqgDOTtWkmt-O3GweuJCm_ahxZTJeeKA2y5jncdylKtU31sRe3sAg3mPs3B3I6FRSKzpA2W-a7brI53nYcEvaqJbvbk2Evn7WjMb_EdqQCfYFJbdsbu5YhxOOH_1AmcFgSB6SH8FHd4cNKl6t9QtFXF3MfKQiiu0xHyU-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ew-bQ7nxftCjMm0UdoSbmY6uwWFb3tiNXL1oNyq3HwUN_QpHwLisCHezGzLSKOVfVQsiUbubqRS2TBeUpHxn5261fg5MrSb7pgL4oNRJMOywnJx2pAuNPEweLfNXZz-82CsbsrvuST4S7FqlwST0M-JcduWSLTixXH3_N6HqomgqkozrUSYtzoPbnG2Y-_oFsSVO_tP1B95vB_NzLydcKrH5fQ3epmXCPKUSFquHzH3DLr8Jd8b3xjn81e-S9jB9DJMorGMsKk0S-OO1-uWYbdpDZcTWq7zW2dPzBDMReA5LXrRIzeSuV8Myt0Ptnd-sWj8ReDzpsyIZTMRTPMjnNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHyp0E-DIoAaI7b3xMNq5WgRZtlfRoxOWEH7bjP1-2jvz_0dLKPb0p2GEc8LYw-UfbbuQjNZ9FgEIpkAozk9MG-VX1nlGTE3vLRSMBCQqTUC_ieFHkDQh5sFSkgiCUYuGE0xi9loPrR66e0eRtcTacS0bpg09oiN2Y3OqNuSrFmpcU6ULEptNQxAH6kvHgEZH4VeF6PjL8JJrSd03VmnuhlksnCJi6Hsy0ckj6h0iLDSABTvM5DIP7sQeRgFR5KawW9iz23a-v1a5nWqv1xOUhlUzfJuKlTthwHleYJZT8e5w-NXvOehqEL0gy3LGNaKkYimftE2_e4zLWOAKUdEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=HpSKRKeZ1DyxPAavZxLEQkb_G07efVKnRgmMdE_gFwLFVerJFenJIswYWOoc2T8xA6sWoa1ovqxdtRhJMAZBWIXZxwUBCrlFBtFp0-SpBJGYmlFSl9cftvpMy6pl1Hff8kMivswtZ1_Nw66A44BjeItcW3rdQT0gSkrIuXYJuoyZdV_i7lcjFaLIf_V6kS_1_IyinNTOVwzpF9KNAqZyUFzsTICAPWJOEEd7oZP5uhmK1_UNI0XFwUyretELdZsmnMaZ5-A7GT0I7Jf_XbKWHj8qd4Kz2nv0fkpRIjQB-R03E6HB_KVBPJ-bQlZMSrHFZiCx9kgk0OqfsXuVjrlnig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=HpSKRKeZ1DyxPAavZxLEQkb_G07efVKnRgmMdE_gFwLFVerJFenJIswYWOoc2T8xA6sWoa1ovqxdtRhJMAZBWIXZxwUBCrlFBtFp0-SpBJGYmlFSl9cftvpMy6pl1Hff8kMivswtZ1_Nw66A44BjeItcW3rdQT0gSkrIuXYJuoyZdV_i7lcjFaLIf_V6kS_1_IyinNTOVwzpF9KNAqZyUFzsTICAPWJOEEd7oZP5uhmK1_UNI0XFwUyretELdZsmnMaZ5-A7GT0I7Jf_XbKWHj8qd4Kz2nv0fkpRIjQB-R03E6HB_KVBPJ-bQlZMSrHFZiCx9kgk0OqfsXuVjrlnig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJNlq7pMe5rL9JIw8uJQbz1md38uRmZBdmDwaDIEoHhXgv1-QZSUXxwQ0Vy6w2XjXJRBqv5u7YYdS5_Jj0q41WV7tNiBhPar-Ct7nHaljbdY9fTEE8gng0SV1Cuqahx9nV56GbiglddcWikOf3x5hHlqN80dgs3KeULgjXUwHhdhLI_N3_EYiGOmqc6HVXX7asXI7Tz39TzlDzoArv13eBG8KBWKVyOhR_V2OLHqUSjh2Q6dzhckbSfECNRp5PNqt1DyNbq-Z-9oyury_BDcmBWKDCfOwdDTDq8RJlBl6tucQvr0D9JNAgO7ThCb3nPs6v2jAIz7u5mIoN6MmzTB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfAnthSAO6gTgXXmblw48PDKIwg5OsDklgXupkt48u_xF4EL4I07V06vaCVZfbvEgr9L3eiCZrmwRfexQr4HZ2GMtdTkOYOSZvGxmaOUvfd5FgBGGWiplVaOErchKDy1pYTM0CvIcooWje0HpSTYL3-qWadpXQRRYiBfX8mmlu5ER_BmiYTgGIpzpN_znLpavr5FMy31nHMVDGCf-__pgthnFr6uSBchMas7qPEWfBKNOpcwOxzoSawMoCTYRrFJAcXW4kB7a8DWqteSZyZg9LlHEoyQudX8OYk1j4ToCPMKBp23xxQCoPrSjpw5bby9v5qA0JxE8u5N_k5K3N8f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OcCeWp80KyerjNT5rucUigF0aVCvzgQu6rsXiw8wkc5FxDbSLUwTOuEyKPe_vjEDUZzfnO3rUbz6RERnns8uau8sn6Etx1fjO42kwBOW5ICi2O6TzEicCcSftBbfwwQzHIpexZ4cM60A50aRduRSzTjIPOAhES6AZnS-DQIESIVrNf6qnuqcELwsDGSQ6CZ-1NHdHNd7T6FR1lG8lk-pUc-YOMj1mqVWWJ3ciccXesmXepAe944yrsxsfZfq7MY-AS8G5B_QRT1wPowrE8ZH-dCvsw8kjUROu3VLF2PhZF0kAq3v6Qg7IBo_jgr48DHCd6JQ3huz7zZxshPysHdhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AA5zYFRQJ5U96EFh--_nsCtfPuVVoa-T5j-2PNZF4RsnyMDH4JN5eV6pQIxnfANkER8ygYNq2soztZi9lbLc1kNsmCjon_82PPzcPCxQkk1gqgI2FCrkHZ68hpTrzgDcWEjcK02wlxoWquITg5ftzvqXUAjJv277no3sadQzMry-INcIclOF1sAlcRq2lHuSbEe99VTlEflEhTtQnDUHuFPPqMDxEN91lmXXK9FKbuaqe1cqmi-wdc5sNpriaCMa2iQYTZ5gvmqxp9OmaYv1zgZS6kLROQ83S8Cqr0NL8tguc3OFN_5WT8pbCd7VpIoKPKdVoVZ36FvcGANjUNIgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD8dSBcj1bypjrieS6pedcudQmV9vSmZVJfVi4ZAoPcyM25BpgMnRt1xKEs5ZvffMDrZ1EAHTyrfQCtVdnNOvSqNydimuk9KWO0mL1H1S0ohGmcNjNMsRnSFfy26IuGgDxC0269iQr82i5Twyt2KgtGYOhx4iEVJHcQskZMX8m1ey8QjsrEqt2Srj5VjN5k2JE_p_a0KwE2yytq221OpUmlyTPUlkJO3mQlzPIVeheEb7Iw-bIEjCs8i0UHkaWdS1VeLO_Yns-Gq5XO6Nvxblza31hAUDxFrLfuItbL2X4j5uCeQ9SVbZ7YdJAHRI4zsaV2wXGOubbcUshS79bEUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hd8LF5pXB3U7dqj4vjWcfRDlZ84WrQZw7gbNcP4SHfJnDUWDLRib3q6rydjEZncs8vPAfwoLX0DeRC2uwdLK17dyTxPgLq2ZRO4GWraLGEi5dbNE_TfkwBfKP1MN6iLpoApH1Zz0yiIzZ7cXZBKTkRsfhA02NB6EZWPS5pot8R_FsFCtT-Po7JwqiMk6CESuqvbSBMJ00lreoSdIQw_1y2pQ6xesZpAIWh-ErNXOYODgvMhIdTfP98iNW9rMGMPBC9KAUCUOWUnJR-OX9d4dUO4RofL70pV5fKlIjNCt0rcmHgC0esPvM3Ll6-5xU4d1OZWmFFMz64SGEXoDdGV3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OJLjJ4UDfwYWBHQ0ecLHKg3L0a_CyBraePtc0tWNzrL6o_eQGPdHI88np0KbFVWcRei0CJXX8kcxQqlU4T9NxUxIHl_rgKW65O1jvw7YZHOF3Ne0YhtRdi29t88rZLiSIJXssd2cZC4XCrLqZlug86d-7WADU4Bkg0JOnVP6Ax1bPWbeQLdWh5HwYptTl5CQ3iKjy7o8pNTs33LmJkZS9dOYL70TAyQaLagWOIlpV8Q9-wpEr58O_UcuBV8FZIxyue8PIGJgiBSmJwUKC9uYqF2K6vOvNknFPhLDaAZsJ2e9uPAv3zetvE20i6WRNgvHejWdmbvhSCegyQTKy_sIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N-m-lbXO1tuZ2wGnZF5x--z8F87ZUhgMxWTER62Upz67eOZ8nQEdj7Uz1n6_tXiJvLCDHJamH4XL4g_1FRyEIiYqZdrdPSJkRfEFWuWcJdtzMMZ6Pt7fGxTg56bEvNd2Fr8FJaSlFg1h_MOKyC2ZQLo18cLA6kcnCbKg_hVwm77JAb2lI9qR-GptKN5u78eSaGRVhW_z2Ftxf62johsSb5CvRUEQNAPNT6wV3w3iUryP57J2zJzkBSN-MCC0VydZ4S55OYxPOtxS0ZzFd-8Tnapp4qBd2_v1zvt1sVHo9DmnsKTT-bCmhHSUVTIqZ_VSfLVw5Siu2MQjtzlqdA6FSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EnmLdH_9s9TAqF7X32pyG-_wCq_7m7cy630BmY0aNmzLdmz-L1iMMUC_dLg1bS6szqQgzLM2rubvJRXerv7eaingK_JCth_ahh62vX2AzCcRXFBn-Y3k-sxuJjrcCafSDZO9YtFzfOTVUnAhjjtvaOVXelXYeA0ksnvqpA8CxqLp2mYsCwJvlD9r0gQurbxliyuo8zfOq0wqoIwXwcIMYnKjMMIfHuzqp_4Xljq1BURnGmt8gaQh_bdd0_DwxuBLBv8AYRtDu8MhwZnMXQ1ZIKH08mv9PqrlyVquHytOU1VvyqWNbJM0GSj0frjISVqozDU8RtzFJJ-_p0cCKCtPGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAoyltb9stVB-9czwYOqeIadiBVKsZQLvCiOh6hgieCMO4FHEk6zmFnrJwBkzT8sU79WVUoNIEXlHzNflnfe5mKY3nByaFIHwBc0tpy4l_3prHq-GH0ziI_x-LhPXJr68lvFXPHUJPu7sft71zBaI2J8wH0XdPrtHRQwfSkQ27lHOusNfbgyNDwW3mqGQ-B1h4N9RXCOiN3W72-DJgfU7wX92JQgDlyGI37ZQE_frlcyG6vd25o5mz8cirPcPkTz5t5N6vnkiSxOGwdrgJPfVlL9QW5oXMP7Cdm2gSzGpP6o3qTXxervA_uq0o4-gygxUlnw_yFeWZ8Yb4sdRm8kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4HGgv8TnHj7Z1-Kr8YCiBg3hV2le7MtdFUqX5Y-YZ7I6mBTTwAO0TXLzLmosK-Urn--R2o_rL_qnsPVRXWni-5ml49ZAnduCKRT9-GmxgmxJnV3IUFuozr5dKt8EEfr20B8ti-uOf0zMl6vXa-Xx85rIgPucnKQC8Vxkuz6C8FUFxPW6Eorp36Gee2kzMytZnWf5CPHHhl4M8puNWnq0rCCOCDKTj4lP3iRePzD2M-K4Unmb2xBMDBzg9wKjNME_7mQOM-_BRTUPYhkjDoqpXc4i5LUTLav2C9uKp1r1Z1QHhvQ1dctv8KwbTA8fr4T_83c49H1GLuOz4yNTVwFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lsEfbgUkI95_Ymc7_5wDokCllq7Pl0q1I03r8yndP3KpEzrllo0IjyHw-WFaIuWEgIL7BVL70nWsOolnSjQuQhX2IqV_xiLDuJAKVkR9tDQg5TEQ-_AuX79FybAewSj7VXcsGIK49g32iM89vznMGLjZvHzNoBkGhpxYHuPDNiLOWvnvTVkhHvKjG_PWHpsMGYCZTR0RoBt6PKCgLKuovm9QMHSnCaQS9tcIW8Da_QqxsdWfzRaf_6R12kBJrui1NXkj9YdSuSffcs48QlmQmimEMcKKRqJA9ITJTxrr9z6F7YZFjx7kyoczZThQ5R09zQeUzherkabGkTDYplSBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=b3z6cSk6UUMNc_X7p_MpHjR6VfnBovNH3Vuo2_fKgoaXlu1T_i5pSYfhmHSP4c83OCXdOPNtS2txpspBHnldz-q6XjFk9ga1-nMW0eHga8BmfxCulOg6GfuWm--DfxmUi_tLxamOlyAR5rJj17QA5C0KAzuAHeB8mhbmv1cxGie9cDxMq209TvMA0ZDL5uJYc1gobBjw16rCyR3kCABQHIF3WA6PrjusPrKpRgMBigE-K9r8bTdgeBVoaQ4g9bHtY-OO-Wa3hZnA77htYxl2sKDvqAj1cV7k3JhTunOf86nNZ_EGABPSIWnjZq54m3zLm3RlqgzxdqTWFerOEOj48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=b3z6cSk6UUMNc_X7p_MpHjR6VfnBovNH3Vuo2_fKgoaXlu1T_i5pSYfhmHSP4c83OCXdOPNtS2txpspBHnldz-q6XjFk9ga1-nMW0eHga8BmfxCulOg6GfuWm--DfxmUi_tLxamOlyAR5rJj17QA5C0KAzuAHeB8mhbmv1cxGie9cDxMq209TvMA0ZDL5uJYc1gobBjw16rCyR3kCABQHIF3WA6PrjusPrKpRgMBigE-K9r8bTdgeBVoaQ4g9bHtY-OO-Wa3hZnA77htYxl2sKDvqAj1cV7k3JhTunOf86nNZ_EGABPSIWnjZq54m3zLm3RlqgzxdqTWFerOEOj48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ePtGEstYUPIfNOq3n66mkQLg-jXm0dMgUsc39JMsb5KNGbduDHAfTwyefeubcZ3pCdFXhoKT2gsb5WYuvNvQgE67HANOyx6XwgAF5rZ9C5AHZvbDvENKzLHpKm8Sv9O7GGQeEpMHKzWgpFZCUjq_PNwzrayQc3VmwjwD_n1JrdZGWXELDq2i4Oiv-cxsAfyBR3gT8lXa55WJ-zs_cuGn9Q-Y8aJx8td5nYvYAJ1vcO_Enyy1SsZCNGfIzrouhx5lmDbmn3Ct4DknODn7h9fH_BREuvFn_LhJZQ98jqba88UGK81DiBrQGYeIq1pbOQWZr8wmCix2ceV7wDpw8vst4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqwwkBQ07yk7v40hZsTNdxg9O3eVsPULamPcSG8DZq5ZQ5W1ej3WAyCmQBAXbouDVZjJQXYWEtSoS8xN2MMfAJ7c1s5tCFV7KswnrRdm8OHs-qW7-6eIf7YFAUwACsgKcT56_5_ZFbvFoRAxuDBWa0iUIu7qx6nAJmUxUCCY5Xb6MNe4CeEQ4ga3EkkX6A2L1Z5hkf7Fe26uazRPwXAULheP4NOyPNg_vkhvkinCz3ovzSB8a0_ObHbd_Wm225cDRJYeimJC0xunthp4EuuAQmHSaLbDNj0pHPF_d8Tm-98KQBd9GfcFwEAimee4gmZwoYt4qCXXIqURermg05Ma1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kxuV_UgB1Cj5C9LZ3rPb41f5gF25pRVkFGjf1YaaQSqC99LzSlmmOXVtDV78bsKuyyTrD37MWwfmPWLHLdqFO8qTX-0AuwrYbXyZHk4D__4Nchcn9a1RVT0ZqCaBeAnpYaNp7gmiJCCSBVRXdzPnXsaULlptISbVVu-Rl_xaoXjQk9ipEb4Rs-ffygzxfw-YKXpCtFY1nXP6jhyIv1SNwYrITs9Rn0-nADFiSy5JEK-QEfIYg6EnPDxiBH_ziMlMW0sfZL69AS28PrJ3ZdnmjZTt_b8aelDqwjbTHENVjTxRgdN0yRiqlgIevXfCVtpQpdH5d3k_wncSgOhMtjszaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=OsqYu-lcPF9ijIdq2MVIg9kEjYsQB0mYzaRegsAZFSN6CKpF5ASK6zNlgXc1jQZot6H59eIyBNQJU4ODb71VGIlYPdjMc3-W71RgPMQe9RBCPBDvNwn90otpnZUU0lEs9dgV3SB4aLd7AINPkr1oF58j8wZ7JAA1uUpwwiUwxxvX5laChzf1Q6G8jP0VEx1234bzY29xTBtc_ISTsyvxJsLW9t9n7E9kdNXEpPT7tPWLNtIdsNp1EZkIy0YUbsYYyGXudXjdRMrUgambk3DyV6cAkt8mzHRg-hQ9Nw_7JFqWADDooCcbUQg3Lu7bYPtnG89GFncUpyL1nmai_pHxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=OsqYu-lcPF9ijIdq2MVIg9kEjYsQB0mYzaRegsAZFSN6CKpF5ASK6zNlgXc1jQZot6H59eIyBNQJU4ODb71VGIlYPdjMc3-W71RgPMQe9RBCPBDvNwn90otpnZUU0lEs9dgV3SB4aLd7AINPkr1oF58j8wZ7JAA1uUpwwiUwxxvX5laChzf1Q6G8jP0VEx1234bzY29xTBtc_ISTsyvxJsLW9t9n7E9kdNXEpPT7tPWLNtIdsNp1EZkIy0YUbsYYyGXudXjdRMrUgambk3DyV6cAkt8mzHRg-hQ9Nw_7JFqWADDooCcbUQg3Lu7bYPtnG89GFncUpyL1nmai_pHxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SvB_pnvcSOilXW9WQB7gHlC3jrZ9JD4UtV1qhM0h7-dta9u2OaeA6hk2pE16s_4Cvn6N9PD3vQzTcgcEVY-x-qBm4HkSStGFopRTUd8Ikbw91P_MTVB7RivLzn7WjKgYJlCpScU8KxdCedTfqCDJiIrX8MeKGhNmCaynP3kfL8rXEYe7y_AJJuSk_-hda8xUTvI9BqhtNdhMcunsK1hodfEKftlvcd78LRs7J6yn_dqzLUD-sBh03qoH4-wfyGSLNoWb2xhXtLvQFD_pMtZR4u7y9oJ7pzr5un9YJ_UnhjRKIxtxwUIkOSWwDcFijQjJui7xQ0TDwg8zs8bLF1evEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwdDVCjmD6H0IfQCEJbzhMUbIfNpun4ykOLBj1JQCJ57yN4TxPpaowcvKrA7CzKt1M0mqWXeHO2jBVglDLL9tG3UDZX7R52VDJy44H1EiGdh4_Nu0la_HdPVMezCWUdGo8clqzVMMZo0oM3f3jkDlX5zhzDQQhsgtMzVJVGFj-OO5VOJfj27m5ekwN1BBf_NzsTaal9D9GxUveo3QMbKqrwdWKYfXvFdE7UT_dabtuqgtYpWykw1MZyXEZLcSszsXwBqFbUsY5WSysfJT8BrhBtTwOFx09RxsF0kYG0WaOJRc0Nnamz_oxhMRnsUuRFKN227NCut-V36RfQdmFjeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGdMuZI1zTQUAAB7krQMeQIwJY8lYZoPrbk5I3dKG53uAlsuPXZV3kR9siuvyUNcZq9Be6A4h4KUbSFRR9cMGMnAJqrvaXgemp1k-e4pF5Gu8gKCOW1D-rVoSxExiQs3Cl0Aq9HB2EeCKa69jqTYsMNEBGizXhkrfmaTL6S0rZtT9e5v0eyHONO7TK3dCFiMVlr34LREeQOZ4m2lLF6g45u3vOKqvyfMKV_Be2JsL42kqSMBYh8JETLJVIyj29dIK-CyQhdg85AEh0-T1x97TS2ihyUalFvEkWGQvOQYVa3L9idmc7rKx02-7xF8-63kBJIODQVjzZSDEPF1i-nykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zi9D77dQ-IV6ffovqD1SvBMn58fip0Bpjt6p7HRifYfNNiUpuz_dyxvZY9v6VAFhBqOf6ZYe8X9Xux4T7sCqraK4t8ZEWC7exufXj4EkhqXhQEDmGDMsR03ki_mka6vAyslJFsdbqetUIuqL7HDIrQxsMGqvIxip2UadVwsWA-waWXTyMGTgKCTa0_BrO4QMx40xVvwHXGZi3as2leNo1kXjQ5_kBDfQp2_R9Ydek2NXxFUW4Fm9lfszvfn2gGhVmu2EOtDu0rdOe_azbxJ6WRjkb241rHxC0RhhrSakwJkw5y8kJbR021cbMs6XXkwpkbSyUZpF7t5P-qLAXXPj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-JZ60mpG4YEGbSuBejlmUEvvcarIH3w-s3bJX_6UYUyBKdXjnZXt5p0krRB1CCcEekNv85nZtot159Hi-WgLU058tuLwWyRKoqGB2oL4ncx-FElEeVuuQ1wKqRksv6R0f5vWXdIie9rxVytvY5Jtaz46VoEmRzj7s1-EHgpxgK2GszR7n_kOU1fBngoKen_RkVfUsTGnDo2ZGnFzxMW6XvtbJYhQua9T99-FdvI8OYQm3k8Ga-nnKN9rIBx75cRfaXqJofTcOQu1LnovSujDTXMNrP21V5bB2bvSIMV7_MHKvo2-XRKwTlgaYpQe3rNiHSr7IRrmsipC4ohwdcUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FAyK_e8bEmSOBaylmw_H4VjMLrhQC6lvI5VOEITvDy8TTIU7h3boKF19-7FiRzc7Ngt4YdKyCjvfsl7RlQxppdutT3d8UWtLWQk3j-dXRIm1lunR1kHviVYsMpI1RgQo2pYA8X0LBB7B7991vaGI2Rg109M0w0PwWHaENHChoczfkZq67-CAmHLsJDUNfdb40R8-or4evA3nwXtsUyHQaQ923PUCmBRYMOGYvxWb4S_SD-b6ERgx7QUuZF-MTzuuPvdRL3cf2eRkB3JLlCfwoxNjiLsHZGSv6kKHN4pX2dZXl9OW1AuAqIet0LIF1w_iRDyqVOqM6HLKbrFNiEuvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RI9onur2moM6Zo7utJpCLoD4cXMTive-QYN5L97lNh458UaFSqQByBKIzY9PznQUFhNWsJ3LGzwUUdNJ73NQr6MiDoUnyjRneMDnnDdwJE2nyb4-erWGHi8w0B6GT-qhuCpe8qgXw8AfQ6N2wyu8TOd45Sx1hZ-vknZanTipO3a6ZGc2vTZqzY5B8ZZ_leZA6O-5swsGoVXfMRouQI1SbeXscpFhEepWBkwXaTpFqCe6uDvtOADew8PdknSHBXx6rQRj-fplXwTv2EwpzqvZWHdKSDuz2G9EZHVIHgS0sJDdw5BWsmVBpfJ95QcY5VLDTc9okyRavkZoPlGnkMftmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KmEF6iZdCvplL9DVCcQ-bkBfD39DoaSSTyvKIjLxvG8iZKTpLSSZ3KqDGdEjRDYXnsxaG6Ci1xK_cM_rxSBTFP0SY-JotoCjWJREFycvdJtYIqdkLTQizdI-aznV7XkBlA90AAgQWbc5vdd0IEV-2ZqD0XdeIrTiUaiUQtvZMH-tShhbOckBr_v2MuVW4TJudSBhne-kSQMGK5YihC9Gw-_IABM_nZxmiZ0O6mMgpJEZKbDIZXWDGhJzet2X-2mWyhX2lNAWLLpKWH9Q27UsVpX_ZWBMBBTZN5EA6a9VEc-2loO2YdgJbyEJVXka1ParXxF751iIALW8LNBzOxP1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ub9clRcIUYlUW2JV-2KPYcpbzTHkMLcTUcF1vHUhrJAvxf5QJ0Spoqg6_nA3CKbJDpXc-mLgKG4RbV6zG28w2cCSXg6iwHhIyBFdBYNVsjYKQB1uGiBRyzejW5HGmbmwGVml1_8sJKGa-FO1G0eDX0d-afGGv4yrKe_mhkNKj4RvUmeQuEfc-KvfyxmvdURPNU3rqsh0ILy6ZdZnQEdjj3aeczd938GbGrRZXD2UJ7SuuQHplnbBkw7LUC-ojSTnS6GQYTFKXn6L3-iGfMBE8RAVUP9DwpHT-NllZIZCUe50XMW4BIEta71b8raunS6velRwofa1z90uycm59QIb9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pth6D9veNMsHOxdFN-BkWQN_YpuE3pGPCHgKBTT1nW5R4v74jVnNhkGyatq-Yhym4dGTXCGNRXsvzZYqCmbJpIIfhC1X7e9DwN_1nRqvDMN1GlBdfcJdsrwebEjlRqj9opRaTiOYm3Is7YNlvS8GOpDeX66mkm4wNDPnRTz-z4YdwjZ3N10pLK30HAol9-6VGkAwbNJanRpvgrX1R_rA9AYz3f79b0iizLppDCq6cN1PgZ5p7oKsPPoDavTZWhiajsJlReFcljzpZkoJ-VBzAwmKIuZ9ueKNKE1BpShj9FjWnNf8EFVgrzZRBPQa-WK0JJfzQ2XNR882BySKJnaEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y78VKN8Ja7bFShnFnOoTT251HraiEJ90a20ywVoiLOM3JhpBJd0UVBHpi-7HL7zSc_x7fn1KMbUTGTRt9B-Ngd-B7IF8oHiJ0FTjC7EatxWVjBNH5MWYmEITki6hkkiWAkJx-yydMm8lLYFrCZPMlhg5Kb9h9WDDDiM2FAEBgJ_75CafC2wXnKoHfMCdwhWXf9BmOorcafCEn5sOr2fzE5yGYiFoGuW5CwT4iUqObrBN2vZWwTmIZlA6hU9_AjLf2gigXzRIOuYo2cqIWFbFU4wBV26nK7IPiWC9O42LkPKCxcQfyyuD-BuTKxU9Oq513lz2MIzgbXfns3aHDULDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Obv4CdgMW6K-xhRptqInJMnGilm6BGlIJTQYX4QYJ0t1t4UihIXbLzXIDjKLBGXjoEk8vD3Dds_a9bV-zLt3o1GCgyQwbMYAlhZVK6rpKtMvhNeWV0bBqaNDVVmVlaJz59kELCoi2295wOiMHYTrpmgw1OW5H_BWx33Xxs8XSx9NDCJL3s0Q1eDumwFNFWGzTIewGqYqdOxD0L7er9AALyEcQ2ybjSAiyKPsDTHCZ2cuaHZAsFeJv-HXKzc7dDJQCUPuK9dZA70V2AJOqGS6jAAIZV_kEkjSXWiTHJ0Un87jY-QtqafPmfKnqNEjo76bg8koykhMG0AqtIEEWXOGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mif4i5Miw6c9t1SjpVQ9QOwfkrPAMIFSj03CEk3AB7jdf-1I3-RZr7cYJ8X8SFsWsvpHyjn8fLvBqAVmhRFrhWI8PZ9Zbt-4hjN6O2juXiaSeTSdBe7Gov5MY9jxRznPYNaDjd0nCkC9C_KynYLmTSKQRIKcGAH0jOE-RS_h1TvrS6E6hV7RCKsbE85ak9QMo6wtkbIiwQETS_YJ7RO73ucf7yoo6sGkOfLtqrhpuHZE9OKVnX8S4znGYmk8uDsQVXTe349hpoZnTEeJnM2DcMK5zeks5yvJnShsivycipJk18kcFBBJxDpTtTUyCSSTt6DazdDHJrgHAvFt7CzKfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=ZE1zTUqr3eke7a19W7Z2PFnNX8ybC9XCS-r3T9YGNqCYjFZ6lR6r4hjlniTWsLCrzfuB48Qaws-BGQg79ngiIzzfLMdCHIUNXy0WpG1X3XBsG3wcv-Oc6LxM7IFz_Qkut_vds717nTu5SrugOpi31n7LYp0ZKLgdtl5iFBJ1MQ4agDBP_2PrEVVIAe81YYk9CGNs9cvJQCidYsdNW7JP20-Onm0q_4lsrMqQN2KSWzXSD-NXOs8PoVo7wMG5A1u8N3sCjILpUGcuOtPeC3kNcuAeijFho0ujyr_kDczWEmYrHTlzm0C6sZWut_LyEDpyFsOJX0RwZQ8tys80VwvbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=ZE1zTUqr3eke7a19W7Z2PFnNX8ybC9XCS-r3T9YGNqCYjFZ6lR6r4hjlniTWsLCrzfuB48Qaws-BGQg79ngiIzzfLMdCHIUNXy0WpG1X3XBsG3wcv-Oc6LxM7IFz_Qkut_vds717nTu5SrugOpi31n7LYp0ZKLgdtl5iFBJ1MQ4agDBP_2PrEVVIAe81YYk9CGNs9cvJQCidYsdNW7JP20-Onm0q_4lsrMqQN2KSWzXSD-NXOs8PoVo7wMG5A1u8N3sCjILpUGcuOtPeC3kNcuAeijFho0ujyr_kDczWEmYrHTlzm0C6sZWut_LyEDpyFsOJX0RwZQ8tys80VwvbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u5N_EnLHn-B8rSdOMqvLFMFqgYlM98p9OH49jm4LM8ddd-dLvHvyPFzLYZfIiWE8z8yc8z11hxh8kh7bY2RJA0rJukXnjK87HBWsdiMUicis-XNu3efZMwnbdC89hRp5u4O6VdpL-MKuDjq8i-Da_MRdpwsvTXq6Ubr0F3GP_u10j80Q2wMrm3CId9GDDCahKy3mI2UColmOFdTG4cQDtCyX-Z6g9qALS4Akr-PxJWK1axKhwhgAiUH69llMou0HN7k4oNxbaXD4TIhf8iS8IJRIbZRnoISnK3mzaPVFBic-PwKTlvwKAGm62949MYtaWGg17NjirlC94A2lIPKmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZIZVMGfa4Z8nQuh0zkF27Y4Z1W14Rz6qbLg_mnxdBEo3RGtXQYHMnccFrPcQI-DMn9AWNiSa7LBzCECvMW4W0PC784mHX9N-59r7Eol024U1EYkID5bQLD2uqNx7AHc1_D3rmsTt1dHJX0bOPx9pxoHI_IokbO1b1wKAM4in4af2Nltg_SVLoUaYeG0khyYK_iB41Co1uzx0f5f_p04CvgUHwBQ-EV70YLsQLWVTdwiq9J3wQuMrVScCg2IgUi_Go6UxIwf2wu4QR7Hm9PxAOR9ucr4UxK5oyHEnDEMixGvRNsUueTu86J-xm9RWJBvyvzz_QCK6vKBn344Aw2r3Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAi-REiPsXAn1yCXMaJ3bzozKi1-f9qSCO0wq3qHBWAI2Pt_WIgvuntUaPBPketA25kOQa1jtR4q6noAZiIIpC7t8pmUKJ_ySNt3ECGg7oEFfmYuirHhIJIPus53TZx4qivxHlktPjuGNc52xx_XiAAaFjfmAoaFkfRzXhXlaqr45mzzEQJaavfM8aFhrQ-incTEbq2H4JVdg06E3E9wIU3BqibpaWAxj2I6ZLj8da0V8UFu593RyF8o4r_DmGGF19Zi8ti3FuY9w3q6dsNWiT9gV8pCneJr3Qj6dZcbqXosofbWiUu_b12kDeOxFgCtuG1c9dn9R0UCma6Ni1mUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vfMb9q-I_rOL41JtCPSVXZsNgOV3vOZaHWLZc1jwHN9LDQmMEwdzDHihv7t784tDP0OjxViGyV5LRG0GlkAU4ktsM7lNddm1NCjEYMA2TG783De-JdBJ0t_bGFfjkcYrYf7tGxLHcyriXwPuyQ6rEWb5qinAls9tEsjE-w2Wt7TKDhyvpk4vvOi2osUEdFCdZAycXwNdfhmmw0xFbjFwQjv7Sr3cV9sUtX-TVRZKSsfTi6--I549EdnaSXxDn_NmInJ2UQNXHS7VJPhnl8hqzDgRw2RcUjTP4tpx1jDW5vBTyYuN5k6ntH4l5O6qgzU-4uzDgSzZpPRI5R323RNjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pAPyynVHt0BNbrw-ViVt5Z3jFU7Bg1p0ZLH14pAoyQ3AwOWoEjLWTZYSqrBc-mVuzvq2E7troF-C04S-t1i63ujJu2iNnfqCHscOY2QCiqtz3AHbStbrc7--IN_Dr1WnqWG7ZR7iYZMo22wAS0qlTOIJo-V8q5WWJtaROp9bfkw4mkpAL0lEKpkqxuJafdQEBJhgSAkI3c_w_8QFx76EaZ9JfqbJotMVai2gwcG0vyA8YbsNl7U0bC-rhLYqnmUt6owPDzSgId3_1NB5T-O25HUNXDSKJjtgY46hxi-Y65oAmUgAaEvJAiYySVNvLQw8pcmAXfwm_YC6zNmnoOCAvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g-ZbPLDT619uXHx72YHz94XzLNTtnAYwPdpetV93inGrMpmOukrvGbyHGNi4ilYeaokOuJF8yrV08E8IFB9QwctoEY1tphO0zMh8j2pMSzr3jhej6qkKBryMJXltZkc3QVSYWaxXHwMcPlCnmRsiWGkfX8TKBVXfA9AIMrxDNeTh9BqgCCxuYtw9KXCeFoEnQtfy3QocBW7ZZ1E0Hu4D9WTJeQHydMGRjpl2VipD_4XtiFt17gqD5OpiasvIAMmIllmlLo4pPOmu7jjh9fb9lZtd6qpcbsBceLg2BrSA5ZsPaUQb6USVBO1siOwDxm62OR8igckBqqR4I54iNZbxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZYRashs5QUGx-_PRe2Y1B8jSqsLTDYs3MTwy5SBVyBhUcb5klY4mRmLHaxJFN8c4pr1PVUk3MLxAZCXxW3zFYxnMTMFCW9ozzkRhPjFwxZ6XO2k8sc-_jLyJkOTXFPmN4WPeGrP1fkxYetE0BZOzai21Wru6ENDIMPtdnbPnT7ru7JkTzu9LasEqw1g-QYCOgdfooo41XZJ9cmYW-1KmBr5M2JdoobdO_W47HCxirAETQ7kwxshy4Ux2NuBzuabbi1GxdJIf3BXOz5y-PI8w-6lyLxnYFQewg-J6U7gUJYCR4IUpqq4I7G5giKpt0pb83VIa8-5GzrXIarkqkYx-Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Sl0H44mxo8zTiirt_jIPyeJLJGWZ4kJbnzk_SF5-94WXbiY0zoLZf6KEEwqCgIaoeRythr_O_3d9gM8ndajlbCHScU_1mXs1S6NDaPH37VOd9gnRa14qavdWtnoyc5jWpQaqEpTh_fMMfX9Sd0ynlTB2jqhPbKQ5SFjWQIx0lLEGAW4lXY37WgdB9MKtTj2G6X_7g3kMJdX5e70nXdZhgXB-WoUJBjM_t0Yignmj35QExFPbUclQrfp9MTJnMPqOcJFqIwWv-ZXB-mmxoPpZ7_U_iEjqVlobHt92S8cc6Ufm34IPfXtrRRdyeRt3aAwIT6_QzdP6mOCF-1Zm_BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hm2DWeSfojv1yknkObkkT78EUDadnmFct_NWCI2nx9tvsTTqZgNvyR3UuGrSMRioSfjRM7o9cmENTKGZqbNFV4fMFScgUP3PfouXex4OPII89QXzsDhc9ZOES1-_wDhUXBZG0BdWF-V0-MaqK1uocNDAVQKohV1IhcDcQp3h2w0lB7HqernrjS5yczfhWUiZl0WhgTGfbVj_NmGO7XAMedISrY2PFu-O7zFSMElIniO_L1qgSSa976h2sbHej7z4ERy0AR8F25o-tTYhH7lxn41L498N5GLw2L_pmBYVC2vhaQFoU95RWsAk1UQgdzqAqIUvZaNJa5OZI_uGWSW8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bF3siz1dINcFxHBB7Nagng3Igkfx6u4AWJRg9hvwbNToAGRyVP7ITFP7CvW_r_upQtHAetjzhzObe2hlgHB-E7XqVMNbjfQZQbObQVhvktUCL7iFORDt0nsMvfVMPr1TNDLQ-H7F5Bgx17Ffh1VYLLQYje8zbqQeOfAL2lGrm0XVsqF5B-MN0X1y5vwQE6JD0ToyX2UkpHqAywXGG8GLuTg6DL9bpusy-GJ-Xw_obF_C6j6xe_cBqlymy0Pve5yLOkb08rDhg0bWJOTygs4YB2RoX6mJ2gxzwmmDftIuiK_8XDj9SErXZtWfMzsxTvvsinuklyexM7daUsB15d-Azw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=JNCNxN6X6VbkA5rRzNN8VBkSpLi9FdrS0e-t6y5hKORElXqbnJRxqjAFZVGQBmbjWDQGI-aMgcx7Kfb1RM44ZTL5H4rwbnqN4_xJCwNDY2572acTRmLO9QyUakYk05WJ9oYaSGwCOURMwy7WRvuYcJMSQ4M-k5tzRcYyHF4hsIhOvUgX5EXh8xRe0rtC-izAuOHvslTBGotlBEdUoSmlKSDsTDrOIQXFyUfgIj8MkSVcAHLWidhBt0BmgPokPOrhM-Bafj_PkgV0NcCGd8eXndhlnT83tC-KIvaxyH5ZlMtq_Wb2IhMUEqFqfAnBd30Lg1n0iyEOLwREQErm2FBwIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=JNCNxN6X6VbkA5rRzNN8VBkSpLi9FdrS0e-t6y5hKORElXqbnJRxqjAFZVGQBmbjWDQGI-aMgcx7Kfb1RM44ZTL5H4rwbnqN4_xJCwNDY2572acTRmLO9QyUakYk05WJ9oYaSGwCOURMwy7WRvuYcJMSQ4M-k5tzRcYyHF4hsIhOvUgX5EXh8xRe0rtC-izAuOHvslTBGotlBEdUoSmlKSDsTDrOIQXFyUfgIj8MkSVcAHLWidhBt0BmgPokPOrhM-Bafj_PkgV0NcCGd8eXndhlnT83tC-KIvaxyH5ZlMtq_Wb2IhMUEqFqfAnBd30Lg1n0iyEOLwREQErm2FBwIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFaw7TR0lF5Z3i34erd8DZlAZA2eA9csxBptqoNe_qrGOdlbogrmxc9YsEmj68XlTuX8pGQ69V0xtEZDODX4rLG1ZIcF-ZxIsGGqdMcxonz7WKvwCFYIlOR_GcpFfiNseiWUD5QlWImHduKAteteWayU7ahnZ0FA-J2IOjcr7x9WtOjfbWxO4j0ogloHuXbl1-OCeO_hxviISNg2j5_U7k7rW6wCivZRaYWD7aO_u2WupE6eP8ZGgmTjVVBG09QH0TY_aefnkWHW-2pBVoA09gQsn2T1PUIhKhcMW12kq6K6_AabZH-CfsLWnQos5-HJjtSmA1wSZjVkSwDAoDfYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PIHCQ8eDhzaUYCuGwvCGolv_Dof2UoLbk-vxFHyfpyBpLbPY5VV26TnZAMYgDbHERrpKlrkLPI0SBw2G1iKtlpbHnNyS9_0BQZ8dyXOjhr68ZU57BaWPUg78_slsTWdQdW-b6KRcJ4JA9vLrGdYfrrVr_imotRUpbKx6s27BBqDuHp5kayR5mAAk5-kpoKkxXtbv6U7rU6_l0yXUNFKgrYpXxCIYg3DOZ8TsTD3imMhjEmpej-8vlYofO4GIVHI1iDdOGaUVN5KBTC0smq_s7ZaUtLAIurSds8P8cGN8w48XBZruw8dBLEv0CN_xMdeUppcNiYe3FoQa6QfKE_tAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MdP6UCO0gGN4mOcqVj7YS6qvmIS_u6ve2_oxlcVgx6kqdF1GHTlN1ttSnTQxJhPCobDf_COKA30Ea8_iiW4IztZ7WCmQuoglIUOcTS6WDVw-V8Zk9_oZ_s5NngJSlBcDesyQe6LiqBnB86XD1vMAiRCtwvkmH2x35k581_Y8VADaGOxgv8GLB9DMJCR16-B_JLG6S702o4E_WpTQWOiBya3C9MfeATlLrazPPrgwoYRVIAu84PFGmoBQSeDvggxumJdcERWDwQa-HD_ecz9ji4pk7RSzSdokkVQG2vhY2Rby-PEpi_oBiYurrrbpxF6LvvJdlbzVnmL7Ozd5wK-NWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ghutbz6ZWvoygraPda7eUTALzAz1f5TP-Ks9W1kr3dSYBaigrgajyuUg4btkFT6SQ35jU38N1zqwJ8jjj3cs4jRIHryRz0g1b7Q8XX3v2KRP87z2hQQ1JRVSONuU2zi0bzCQN8d4l-ysM_BqECebWP2Lv9ppvJ4Ugsyfko0ccuOIZgLj18YspsUtIxjK74eXAeGwQptMIo20hRoqKrci0eoif_Ol-qB6APkRNeovhavJyRLW7kkkETxIOwH9e1pJsc2mrq12wSVblBDvqIZsvimV2chW_HuwpmLb59kiz0e_3LocGKBNmP4VAq5Mun_g8tk_pWCH1ZbyN66T0H17zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dAEHkD-yFgz5JxFSHPSSh7yrcPrFxWWhurNoH50cuOdZQkWSJb4YtSJdHm7vHSBbD6h8e5Rsqy95TULaSMTb7xRoNLu3yEQa7Mb3kYHoDW5Zm_vNDYfuQ90PJtZAMlJ2vPIjhZl_Nw573qdrhQ2EfJflFyyVVtBmTxQt9Y04YobeiI6yavnwYTfvkSfGUm6A4lUdzIIOWqdcz5hrlS4hj1I3eD1LWAEqM_SodzB7BjLh-qXEsz3rSxFV5vSr7ZIDFhlRZWD_2m79nK7ztvFIp0XVri6MG3CiGH7rcFcKIoxUJMFCs-l0EORzsSev_RGl9L1TgJSjuX5L5dqOblp_TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggVhmDJguPzCShFJfKNCkZTxfoB8p-owZ7uY2Jje5Yrc-6lLMVH3cnoUtznq4EJHSP9S7AkgRL1NvTuzWcMBZfWmilD1Ij8sRyIXAkilD1W0mdJ96S32KosvgmzSRjQ0LrXwGTu0GKEKg87FnR1Boyj-LFW6LXg589YY4CBDI1vTuZVTMz2sRzxJH2kEYisT6DxUURpDX2M8lUvaWHK95lO2sAEWCFqONi6gRXA0mnU7KS-u99R0b_8VQo-HjmgB_Po5W6thOfc79UJyP3LtVXCJddZAt8QZNPZxym4ppC_1LdolRho1WvSIAMSSfkw09CBffvs9mWi7Hc8NCTkiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GoB344LVrm0NXh71S1wWp-z7tfSqU0v2dKRX8dvsjkePCzZPliMFRLFWCCVGOkF7va00PxMD4WD8Ap6wcgRVLwwd14yXztxt4CiIWQ_VHH4OBYv7JrsvcWvk0pumMxHmJVL6xzxwvwcvxdTeSiBYsJVtUsQnZeEL0Hwr15X9ABruuQQkCudZDyTCV-RnLGJ_kCaIlOdqZOwdKC3QG6R4G19W3_wDZTspr_CP4stio10YrzPsNU93_-ikMwh4tWcbI6MLkU0yKstjelh8Z-DW1JzISlvgpIOk6bekjeyTiOIQG8w87TqwARszXoDZ8-0V7uDIdltZMXAb0BGwWPUpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
