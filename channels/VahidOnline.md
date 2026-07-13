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
<img src="https://cdn1.telesco.pe/file/JdqaX7Z88hGSHTldXJLartefzcDwE_1_ejYEivwt-vClUNO-9eyx4ZlK0F_ifWLBIdPj-d5T3ua-IOTRTE7UPNMqDaYSzCxnszrrX2OTnx-hCya9QFEA1Geyo0nVkD8vdeg8U3qbll-6Iywmqw_mPGRqnkzU7vdpB84vTaBu4zO5MHUjM8pbMqPJxr8Ug7sy4yPWdMocXv5KH3VPXdQotw0Pk71--DVh_SLwjf_4-v03Bqai5XqMKMlOJngOVC5hnJw5dG0l5Bk-zoXXzCndzPDL9CiNobhpJrLNdEKYF4AeMdfsm6yxWRJypF8CqaSW_S8KPuce6PlkuE5ny3vrFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.37M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4930898fcb.mp4?token=qvZyPHbIsrDkYrlB1lyu8SL12oeM5nDYJfik-ukZzBfRAOWO96qpW_IvAu2T8xGlL3uGIY_CT5r7upxEu01g5sLygJqv-L-AkfK7osRaoN7_GsoIOUp--_e-yUCTB4VOUSO9-SrWswXUj1-jZzn6QH7RuLvEKZFnwl07TUyuMVk7wLgyx1g8VKuQ-OBb4MJL0eDnqQDf1PJ31zEMb5CdPuGBSA1Tad8fjr6cbG5R_rS765gRiVrkrpqn-zQ6Zzv83Z4ULEza_Pe-4soSl5u6wSjpc-cK8E5S7g150TKCBpLKasXjomBqJQ3J_3zEtkXk3QkOLWKhCosVeuZ8JeZESA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4930898fcb.mp4?token=qvZyPHbIsrDkYrlB1lyu8SL12oeM5nDYJfik-ukZzBfRAOWO96qpW_IvAu2T8xGlL3uGIY_CT5r7upxEu01g5sLygJqv-L-AkfK7osRaoN7_GsoIOUp--_e-yUCTB4VOUSO9-SrWswXUj1-jZzn6QH7RuLvEKZFnwl07TUyuMVk7wLgyx1g8VKuQ-OBb4MJL0eDnqQDf1PJ31zEMb5CdPuGBSA1Tad8fjr6cbG5R_rS765gRiVrkrpqn-zQ6Zzv83Z4ULEza_Pe-4soSl5u6wSjpc-cK8E5S7g150TKCBpLKasXjomBqJQ3J_3zEtkXk3QkOLWKhCosVeuZ8JeZESA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکایی محاصره دریایی ایران را از سر می‌گیرند
ترجمه ماشین:
تامپا، فلوریدا — بنا به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) از ساعت ۴ بعدازظهر روز ۱۴ ژوئیه به وقت شرق آمریکا [ساعت ۲۳:۳۰ فردا سه‌شنبه به وقت تهران]، محاصره تردد دریایی ورودی به بنادر ایران و خروجی از آن‌ها را از سر خواهند گرفت.
نیروهای سنتکام این محاصره را علیه شناورهایی که به مقصد بنادر و مناطق ساحلی ایران یا از مبدأ آن‌ها در حرکت‌اند، اعمال خواهند کرد. ارتش ایالات متحده همچنان از جریان تردد در آب‌های منطقه برای تمام شناورهایی که محاصره را نقض نمی‌کنند، پشتیبانی خواهد کرد.
ازسرگیری محاصره ایران از سوی آمریکا پس از اجرای اولیه آن از ۱۳ آوریل تا ۱۸ ژوئن صورت می‌گیرد. نیروهای سنتکام در این دوره دوماهه، مسیر بیش از ۱۴۰ شناورِ تابع مقررات را تغییر دادند، ۹ کشتیِ متخلف را از کار انداختند و به بیش از ۵۰ کشتی تجاری حامل کمک‌های بشردوستانه اجازه دادند از محدوده محاصره عبور کنند.
به همه دریانوردان توصیه می‌شود هنگام فعالیت در دریای عمان و مسیرهای ورودی تنگه هرمز، پیام‌های «اطلاعیه به دریانوردان» را دنبال کنند و از طریق کانال ۱۶ ارتباط پل‌به‌پل با نیروهای دریایی ایالات متحده تماس بگیرند.
اطلاعات تکمیلی از طریق یک اطلاعیه رسمی در اختیار دریانوردان تجاری قرار خواهد گرفت.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/VahidOnline/77009" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77008">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb1Mwq682EdcWq0GSrlYV8AEpsHdhlSHathS21RWbskvqFVIYEWGAVVVYjy7Lz4TN_uGcvCsm0Im5In0GvmQ8eFU6xvE42pXpimFPlM8XrXSGd9q34Jtw9viLdZq_caPYw6YdTXYJh2E95QBjixaszEEyiIcgUxndibTAjejTkO7ZzUECGQ1cofaHh4UndYlelkBnJV2WAh7KScR4fnx3aDCYiZUV6spGH3KFaVwhPL3G_J0UX2nT2zgxef5qLttHZ18nXLCAzoHoXp7_RSdkC880v86VwyFS-W33DyuuUPl4R298jTsoZDMBwiPWz5pasj50wDueJx5hpS_WV8UTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه ۲۲ تیرماه و دقایقی پس از اعلام تعطیلی سراسری دو روزه در هرمزگان، استاندارای‌های خوزستان و بوشهر نیز از تعطیلی و محدودیت ساعات کاری این دو استان جنوبی در روزهای سه‌شنبه و چهارشنبه ۲۳ و ۲۴ تیرماه خبر دادند.
خبرگزاری‌های دولتی ایران، دلیل این تعطیلی را «افزایش بی‌سابقه دمای هوا و به منظور حفظ پایداری شبکه برق کشور» اعلام کرده‌اند.
بر اساس اطلاعیه استانداری بوشهر، تمامی ادارات و دستگاه‌های اجرایی این استان در روز چهارشنبه به طور کامل تعطیل خواهند بود و ساعت کاری آن‌ها در روز سه‌شنبه نیز تا ساعت ۱۱ کاهش یافته است.
هم‌زمان، استانداری خوزستان نیز اعلام کرد با توجه به شدت گرما، ادارات این استان در روز چهارشنبه به صورت دورکار فعالیت خواهند کرد و روز سه‌شنبه نیز همانند استان همسایه، تا ساعت ۱۱ دایر خواهند بود.
تعطیلی بی‌سابقه در استان‌های جنوبی در حالی اعلام می‌شود که در پی افزایش تنش‌ها در تنگه هرمز، ارتش آمریکا در پنج روز گذشته حملات گسترده‌ای را به شهرهای مختلف به این استان‌ها انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/VahidOnline/77008" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/be__PIz3ekLLuaUlb-K2xIckxgx5ghgghycFgYxPBsi2lw3CQrvo5x7KR_m8zctlnBgqkI-RPmaZrs88HS7fFPx8gSbncvzeQsxnRQU57u6vMK9GZY5gvqUZ3dS1IkN0pylhdrRnCz_vsN9xZaTsWYqgYNeoov4LxgpYFqpRo2GbMUg-Tw50jqBAtiVBxgGXhuX_r5eYNGb0j4-yDtyb3HbiN0IkXTDHqOkqZxB5ah1JFmRc3L18U-OLLzg2xY6hFw8O042S-hcQd7OqCv-i-8hC6_ENrMYwiDG8WUmizFpT5PLf4Ts6RCrOiJ0X-7SFFGn_hz8HjFTH9w4Cs_tRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، ترجمه ماشین:
رئیس‌جمهور آمریکا کاملاً درست می‌گوید. هر کسی که عبور امن و بی‌خطر کشتی‌های تجاری از تنگه هرمز را تأمین می‌کند، باید بابت این خدمت غرامت دریافت کند.
ایران همیشه «نگهبان» تنگه بوده و تا ابد نیز خواهد ماند.
البته ۲۰ درصد بیش از حد زیاد است. ما منصف خواهیم بود.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/VahidOnline/77006" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxaGIH3dse4vhJ1b9X92opur9k_VkglPvtz6Fo3Ont949MbL3TQ-602uBEjnAKjHdlfMLXFGGkty_zum88SgtrXx2pYvW2luO-0qdGDislErQfG7U-jSE9eXhtGP5hhWRJYr-rcFb-zQNSXQbpTnrnwioOVvJlWioXJmpaEO_ixmv1r3MDGN6VjOfjwfrFHFnBXBcYmKyiOT-u6U8wRQidsOeugAekY4hdh3vE0FSuWu0057PtWozEA7ccv4nefxTmrmct7sKW6_2jEKKnSDbjCRLu1s71B4RM3jvFYol_x0z09D09EpgoV8hcQlGt4oxI-VQvAZ-GLe65p9UYSk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا پاکروان، معاون استاندار هرمزگان، روز دوشنبه ۲۲ تیرماه، از تعطیلی تمامی دستگاه‌های اجرایی، ادارات، بانک‌ها، مراکز آموزشی و دانشگاه‌های این استان در روزهای سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه خبر داد.
این مقام استانداری هرمزگان در گفتگو با خبرگزاری مهر اعلام کرد: «این تصمیم با توجه به بررسی‌های کارشناسی، موافقت استاندار و مصوبه کارگروه انرژی استان به دلیل افزایش شدید دمای هوا اتخاذ شده است.»
به گزارش مهر، مراکز خدمات‌رسان، درمانی، امدادی، امنیتی و انتظامی برای ارائه خدمات دایر خواهند بود و
امتحانات نهایی دانش‌آموزان و دانشجویان طبق برنامه قبلی برگزار می‌شود.
این خبر در حالی منتشر می‌شود که در پی اقزایش تنش‌ها در تنگه هرمز، ارتش آمریکا از بامداد ۱۷ تیرماه حملات گسترده‌ای را به شهرهای مختلف این استان ساحلی انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/77005" target="_blank">📅 21:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U9RS2qF0pOh4GSoKAKMyW_d9-r4dPJXzWyqhBemmZdlpobJ3YQ8pGVxgaVAv18w81WIfXwAwSW-bB1WX8lbcU_0ytsYoMfztprUUv5iEh0yPGDmBDVL2dD1w0jC_lHzp4rDixMVTHHi-ErNRM1HQ21wol-19lNDd4eRSfmFOTMgowsQDa4a8ZuT8I75oTk5P_zybBvU_Ttsfyym2yck03jKOH_bH-kUkE1njwD9io5FNiOTp8gLUZrCDzZmhliQviQZDNAoh7YNYZFp1e23RSEGaQ3UbZ_J9t2PabYz6SEz9Y09l3khRgE0TtX8UWpm0CJ6ZCBPhxjC2VBqn1NHi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تام کاتن، سناتور، ترجمه ماشین:
رئیس‌جمهور ترامپ حق دارد که به‌دلیل زیر پا گذاشتن قول از سوی رژیم ایران، هزینه‌های سنگینی بر آن تحمیل کند.
در برابر حملات تروریستی ایران علیه همسایگانش و در تنگه هرمز نباید هیچ‌گونه مماشاتی صورت گیرد.
برقراری دوباره محاصره، رژیم را بیش از پیش فلج خواهد کرد و اجازه خواهد داد نفت برای متحدان و دوستان ما از طریق تنگه جریان یابد.
SenTomCotton
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/VahidOnline/77004" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5ObQLwmV8jY3dHaf9g0VF6TG4SL5pK9Hqn3o8-SLW5rDs8ggmI4mvmiAuZXBSoemtNtkW9g_LKsBZzbUcdjYGk7XU3Dzm9q0fnifpNzeukqqFRFU96fxWnQKQfVO_y29TiWeVOLKpcPpFr6Yhcmi981rAzIYn3Qthpdk-rWinceeVssDF2MOZNxnkgb8CWwPljO8lfJyZyvDzv1wK74G_HP8lOTjg-7AHks4UbZ0H54sreNu8NU_yaZDnPdEasvsVdBAW6QQv9gQgIOi8_18gerfVGmIHqtgJmpy1amDjQ4fi4e3NzNV2kQ0Psb9r0j0zMjkPXawrvaGiS-7KZKAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس روز دوشنبه گزارش داد که اعمال دوباره محاصرهٔ دریایی ایران هنوز اجرایی نشده است، زیرا طبق الزامات قانونی باید ۲۴ ساعت پیش از آن به مالکان کشتی‌ها اطلاع داده شود.
یک مقام آمریکایی به این وبسایت گفته که فرماندهی مرکزی آمریکا، سنتکام، زمان دقیق اجرا را اواخر روز دوشنبه اعلام خواهد کرد.
یک منبع ارشد در خلیج فارس به آکسیوس گفت ایالات متحده موضوع دریافت عوارض احتمالی برای تأمین امنیت تنگه هرمز را با متحدان خود در منطقه مطرح نکرده است.
دونالد ترامپ رئیس‌جمهوری ایالات متحده روز دوشنبه اعلام کرد که محاصره دریایی ایران بار دیگر برقرار می‌شود.
او همچنین تصریح کرد که آمریکا به‌عنوان «نگهبان تنگهٔ هرمز» شناخته خواهد شد، اما ۲۰ درصد از ارزش همهٔ محموله‌های عبوری را به‌عنوان هزینه دریافت می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/77003" target="_blank">📅 20:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urgJqQ_Nhbw7TMB4Gn9APT0tnBw88-ZXi2oBoQNLMw7syE_Kg6Iei9_36LCnyQnufKE2fn5CXsOgbC_sB_C_wTNFcf5s8Lw6Tx15a7iK2YtZpBk0a0nCsCxjv5_PvcfNaEREsy4XrM80UzkyOOjKREaxG3NYk0x1IfGvfRrWBaNtB4Cn7c8tH6Oc8g8qsmWYfcdS9ANXohtIuN--txw8rDNrkmQESTjRcEBQPRYV_bWKA2TI-UQEXmz-vg8Ow2LZ_XPmwsEpKwKcSZ1NwbSDC6JcfYsafiJxAkweqtqRcGkOWRWE1w7g9odCZjmQtf1bY_qXumJY7RVva5erVeSIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در راس نظام سیاسی ایران پس از سرنگونی حکومت فعلی بود.
بر اساس این گزارش که به نقل از منابع آگاه آمریکایی و ایرانی تهیه شده، ماموران موساد طی چند سال گذشته در سفرهای خارجی احمدی‌نژاد با او دیدار کرده و حتی هزینه‌های مسکن و رفت‌وآمد او را تامین کرده‌اند. «دیوید بارنیا»، رییس پیشین موساد که پنج سال این نهاد را اداره می‌کرد، شخصا برای دیدار با احمدی‌نژاد به بوداپست سفر کرده و به گفته مقام‌های سابق آمریکایی، موساد، موضوع تماس با احمدی‌نژاد را به‌طور رسمی به سازمان سیا اطلاع داده بود.
...
بر اساس این گزارش، در ۹ اسفند یک حمله هوایی اسراییل به محل اقامت احمدی‌نژاد صورت گرفت که ساختمان محافظان و خودروی زرهی او را هدف قرار داد.
به گفته چهار مقام ارشد ایرانی، پس از این حمله یک خودروی پژو مشکی‌رنگ در صحنه حاضر شده و احمدی‌نژاد را با سرعت از محل خارج کرده بود.
منابع آمریکایی و ایرانی آگاه از این عملیات گفته‌اند راننده این خودرو از ماموران موساد بوده و احمدی‌نژاد را به یک خانه امن در داخل ایران منتقل کرده است.
اما طبق این گزارش، این طرح در نهایت ناکام ماند. احمدی‌نژاد از شیوه اجرای این عملیات نجات ناراضی بوده و به گفته افراد آگاه از جریان ماجرا، نسبت به برنامه اسراییل برای بازگرداندن او به قدرت دچار دلسردی شده بود. او سرانجام خانه امن را ترک کرد، هرچند شرایط دقیق این خروج همچنان نامعلوم است.
احمدی‌نژاد از آن زمان تا دوشنبه هفته گذشته، که برای لحظاتی کوتاه در مراسم تشییع پیکر آیت‌الله علی خامنه‌ای، رهبر فقید ایران، ظاهر شد، در هیچ رویداد عمومی دیده نشده بود. در تصاویر منتشرشده از این مراسم، او با وجود گرمای هوا ژاکتی ضخیم بر تن داشت و ماسک جراحی را تا زیر چانه پایین کشیده بود؛ در حالی که سرش به زیر افتاده و از هر سو افرادی که به‌نظر محافظ می‌رسیدند او را احاطه کرده بودند. حسن روحانی و محمد خاتمی، دو رییس‌جمهور پیشین دیگر ایران، به این مراسم دعوت نشده و در هیچ‌یک از تشریفات مربوط به تشییع حضور نداشتند.
به گفته چهار مقام ارشد ایرانی، احمدی‌نژاد اکنون در بازداشت واحد اطلاعات سپاه پاسداران به‌سر می‌برد، پس از آنکه نهادهای اطلاعاتی ایران بخش عمده‌ای از ارتباطات او با اسراییل را کشف کردند.
...
متن کامل:
telegra.ph/ahmadinejad-07-13-2
هم‌زمان گزارش مشابه دیگری از هاآرتص: @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77002" target="_blank">📅 18:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/246c412fdb.mp4?token=AhzZdEbOnLylIsPi35si9FRH0xv1d0Vzh2NlebTI7n5qY7qw6JYnCL-j5w9biJbCL3x2Wlwfbuf3wGJIEUfRlz1xXa6VMCeXpkRnuPQFO8ACKM0BOa0TDRpU8b7CzyVjZ1UzgNdtvHKFlft9h3cVkPZfnKBsNfmhJUQ2saOfk0dBkK9eLybVzFzXImbHqSc_6E9VGjZidiCeGoQJmIpBU8zAZvYBV83zUYwJ2CF6SdG5fZp4RQsEoO-ZN3Wo2W4dLmwe-gn4slALe_OtKkwEOpomhoQjtCvqfUMtkAlK_oHrBOpaYdSeGausPEIEGep8POW3c6-7dJDF-Z0yizJDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/246c412fdb.mp4?token=AhzZdEbOnLylIsPi35si9FRH0xv1d0Vzh2NlebTI7n5qY7qw6JYnCL-j5w9biJbCL3x2Wlwfbuf3wGJIEUfRlz1xXa6VMCeXpkRnuPQFO8ACKM0BOa0TDRpU8b7CzyVjZ1UzgNdtvHKFlft9h3cVkPZfnKBsNfmhJUQ2saOfk0dBkK9eLybVzFzXImbHqSc_6E9VGjZidiCeGoQJmIpBU8zAZvYBV83zUYwJ2CF6SdG5fZp4RQsEoO-ZN3Wo2W4dLmwe-gn4slALe_OtKkwEOpomhoQjtCvqfUMtkAlK_oHrBOpaYdSeGausPEIEGep8POW3c6-7dJDF-Z0yizJDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام): یک تأسیسات نگهداری زیردریایی و کشتی در ایران برای نخستین‌بار با استفاده از شهپاد هدف قرار گرفتند
ترجمه ماشین:
دیروز، نیروهای سنتکام با استفاده از چندین شناور سطحی تهاجمی یک‌طرفه، با موفقیت یک زیردریایی و یک تأسیسات تعمیر و نگهداری کشتی در ایران را هدف قرار دادند. سه شناور سطحی بدون سرنشین «کورسِر» به بندر پایگاه دریایی بندرعباس اصابت کردند؛ رویدادی که نخستین استفاده نیروهای آمریکایی از پهپادهای دریایی در عملیات رزمی را رقم زد. حملات شب گذشته توانایی ایران برای ادامه حمله به کشتیرانی تجاری را کاهش داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77001" target="_blank">📅 18:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQY-7hRXIAQ8E1FJexRb14bBtzJiGczBKFCSf4_rR8x8ef3XI4VUToD6_djQoAlvewpTaK79eVuJAB6MgV5jiaxfo3NuaYRBL6msRd8NdIXWjdYReaJPEeTMdF5jlg5CLnLT2dvE_4RN0yEFPJzKMoXPOYoAuujp86rdfvGJOG4mjqyeGvsavzdEx1JKpydGXqY3oNUWw5UaMelM-f18A04-pCwdrrmNXCU4_l4-6T7dW3t9ig3QepkpfSPHoq0SX3EQUghhxskoL8H7SuhGCpffgD7VV7-WnFE6lCOJblmaVh_qviR-nQL6ZHK3GlWD8okpH_E7_r7cgNMEWlg6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره دریایی ایران را دوباره برقرار  می‌کنیم
ترجمه ماشین:
تنگه هرمز باز است و با ایران یا بدون ایران، باز خواهد ماند.
ما «محاصره ایران» را دوباره برقرار می‌کنیم؛ این نام به این دلیل انتخاب شده که این محاصره فقط مانع ورود یا خروج کشتی‌ها یا مشتریان ایران می‌شود. همه کشورهای دیگر امکان استفاده آزادانه و منصفانه از تنگه را خواهند داشت.
از این پس، ایالات متحده آمریکا با عنوان «نگهبان تنگه هرمز» شناخته خواهد شد؛ اما در مقام چنین نقشی و از سر انصاف، بابت تمامی هزینه‌های لازم برای تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان، معادل ۲۰ درصد ارزش تمام محموله‌های حمل‌شده را دریافت خواهد کرد.
روند اجرا و تشکیل این سازوکار بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77000" target="_blank">📅 17:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fe40c2602.mp4?token=UtdrUsINHLPecaxjuEPKhEzTk43ounqGsTnZrGncjaZyIhFgeOy2FjDECXOm-Sqvci93SX_DrL_IY_-yDnMBiNK2-lIQatWO7eYkzAspZi4HzUfaLB7Sm6dWSaANbEEjWOSC5b7i-joM-bpbpoJc32POVjbCyO2IaLPY6OEOkmF-4dxcEHat_mK_REPir4rbIxwhgjr3_pQLHUp66mypwTMAbFOYQy4YpIx0I8G68M1eOFL9W1AX638ikX9bJl_e7oMhOnCE3Q9xt_BNeOSfiFyzfCRyjoC7bOhQhTg5218frmm2QxTeeZEQTjLLWWhSdVHh4TtmvFtmewn3akj42g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fe40c2602.mp4?token=UtdrUsINHLPecaxjuEPKhEzTk43ounqGsTnZrGncjaZyIhFgeOy2FjDECXOm-Sqvci93SX_DrL_IY_-yDnMBiNK2-lIQatWO7eYkzAspZi4HzUfaLB7Sm6dWSaANbEEjWOSC5b7i-joM-bpbpoJc32POVjbCyO2IaLPY6OEOkmF-4dxcEHat_mK_REPir4rbIxwhgjr3_pQLHUp66mypwTMAbFOYQy4YpIx0I8G68M1eOFL9W1AX638ikX9bJl_e7oMhOnCE3Q9xt_BNeOSfiFyzfCRyjoC7bOhQhTg5218frmm2QxTeeZEQTjLLWWhSdVHh4TtmvFtmewn3akj42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شبکه فاکس‌نیوز گفت: خامنه‌ای مرده، پسرش ۹۰ درصد مرده است.
از زمان جنگ از مجتبی خامنه‌ای عکس، صدا یا تصویری منتشر نشده است و در انظار دیده نشده است.
دو روز پیش عکسی جدید در وبسایت رهبر جمهوری اسلامی منتشر شد اما نشانه‌ای از اخیر بودن در آن دیده نمی‌شد.
رئیس‌جمهور آمریکا بار دیگر تاکید کرد که نیروی دریایی، نیروی هوایی و پدافند ایران از بین رفته و رهبرانشان هم کشته شده‌اند.
او در این مصاحبه همچنین گفت دیروز پس از یک «جلسه ۱۱ ساعته» بر سر «همه چیز توافق شد» که اشاره‌اش به ایران بود.
او به جزئیات این جلسه اشاره نکرد.
او افزود: «کار اینها همیشه ۱۱ ساعت طول می‌کشد درحالی‌که باید یک دقیقه باشد... اما از اتاق که بیرون رفتند، دوباره تماس گرفتند و گفتند باید چند تغییر اعمال شود.»
دونالد ترامپ سپس افزود: «همیشه تغییراتی در کار است. می‌دانید، آنها مذاکره‌کنندگان حرفه‌ای هستند، کارشان همین است. البته من حتی نمی‌گویم در این کار مهارت دارند... آنها هیچ چیزی از من به دست نیاوردند.»
آقای ترامپ چند روز پیش هم گفته بود با ایران بر سر همه چیز توافق شده بود اما ساعاتی بعد آنها به یک کشتی تجاری در تنگه هرکز حمله کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76999" target="_blank">📅 16:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8qAKqT7mYcrk7Y7tmeFMh7Sd3ASqgQczQN0y1h5FxoK8aJP-qVnDtlkUyizCJ30Rm1WJWUpsCiW3YGWzETlmKWWaZ0t20X044XSu--F4-fkmzBk9EHgCZ_UJ-tuJSl9looNE298GYuPG2eiqgrwYoWbGQu0bi2r8IfdixZBcaRdms0FmZPBE9odCquHdkaLYBU9YuWKXxNs_A1DwoqRlPfgDMphBsiiY1_7_g9JoSiSwHt9LWo91WPjC9iiIz3_Xfkptl0lCmT2RJar0OogRBTNBYHhkI-u-ia5mvwYGTFV3rUjz7UaOTn87ZHfv8tvcjCJoUB2pyHNnqnPcB4heQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه فاکس‌نیوز با اشاره به تحولات مربوط به ایران و تنگه هرمز گفت: «کنترل تنگه هرمز را به دست خواهیم گرفت.»
او افزود: «ما به یک توافق رسیده بودیم، اما آن‌ها آن را نقض کردند.»
ترامپ گفت ایالات متحده مسئولیت حفاظت از تنگه هرمز را بر عهده خواهد گرفت و افزود: «باید هزینه این کار به ما پرداخت شود. ما بابت حفاظت از این تنگه، پول دریافت خواهیم کرد.»
رییس‌جمهوری آمریکا همچنین درباره مقام‌های جمهوری اسلامی گفت: «آن‌ها گروهی بد هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76998" target="_blank">📅 16:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6AWuo4_e5QImAzSWUv3Y6JFkO69jqnm0u4aWqqFwbe2HASmKfW3c9vR2wOGfKKRa55oPeh-UaXzOZB6Mx_jc_1SUDLG26Dt956Zl7hDurdnDlpPdcWZCnxmWzOwbiZn3TTdMyij5orHlFRlNR8fNisNSflStz6nZ1Kkcb9X9K3pv5bxkBIXxu5Y3C76Tt0un3JLPibGglJH8W6lTMDM_k1OpxoMNY76AO4Rr7Q3yN3ucpSYMQjToJhkPktDsy-TmSVzHNXt34lzl8ozP05lWaLFlYeLTYd6w7FQMEEPadqo7BrcM9icLisqdleDZRgDHWjghXxDHkQA6gERYCvVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.
سپاه پاسداران پیش‌تر به‌طور کامل مشمول تحریم‌های بریتانیا بود، اما دولت‌های مختلف در بریتانیا از اعلام آن به‌عنوان سازمان تروریستی خودداری کرده بودند.
لندن سال‌ها زیر فشار پارلمان و نهادهای امنیتی برای این اقدام بود. سازمان اطلاعات داخلی بریتانیا، ام‌آی‌فایو، اعلام کرده بود بیش از ۲۰ توطئه بالقوه مرگبار مرتبط با جمهوری اسلامی را خنثی کرده است.
دولت در ژانویه گفته بود سازوکار موجود برای ممنوع‌کردن نهاد وابسته به یک دولت خارجی مناسب نیست و در حال تدوین اختیارات قانونی تازه‌ای برای این کار بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76997" target="_blank">📅 15:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8171dfe95.mp4?token=MzChlQT5eZm_ifyw5UrKGe4Vvzi6RZaIg3_WQE8SBsXPS3MUL7YmUDj_HjbvQB466BQaRvrgI81WYl1c0LkVIyNr3M4EWR_rih_Fht4gB9CUXsJLMNns1bepICeoR5V0VDMRUCRSyA3IUv1Beg0RvjxyImarugO4WE4QcEH53CsI8ZdzrrtwTOEs9HD-iz35XPyFxd9gPgnf-H8BWcFKRzTHYXLt6oSiSsanKwbshZZTpt2drNyJU47_rxC7Sl7dexywX5VdadA6rK80UjwFdvccmIkJGOnfHp9fjp8J4Sc9PvD8vlNL7qHonAA7aLg9jCPrcS6xk78JB_VuzJ28sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8171dfe95.mp4?token=MzChlQT5eZm_ifyw5UrKGe4Vvzi6RZaIg3_WQE8SBsXPS3MUL7YmUDj_HjbvQB466BQaRvrgI81WYl1c0LkVIyNr3M4EWR_rih_Fht4gB9CUXsJLMNns1bepICeoR5V0VDMRUCRSyA3IUv1Beg0RvjxyImarugO4WE4QcEH53CsI8ZdzrrtwTOEs9HD-iz35XPyFxd9gPgnf-H8BWcFKRzTHYXLt6oSiSsanKwbshZZTpt2drNyJU47_rxC7Sl7dexywX5VdadA6rK80UjwFdvccmIkJGOnfHp9fjp8J4Sc9PvD8vlNL7qHonAA7aLg9jCPrcS6xk78JB_VuzJ28sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات متعدد به باند فرودگاه صنعا امروز ۲۲ تیر منتشر شده است.
وزارت دفاع دولت یمن، که از حمایت عربستان برخوردار است، اعلام کرد که باند فرودگاه بین‌المللی صنعا را هدف قرار داده‌اند تا از فرود یک هواپیمای ایرانی جلوگیری کنند.
حوثی‌ها، که متحد [حکومت] ایران هستند و کنترل فرودگاه بین‌المللی صنعا را در دست دارند، عربستان را متهم کردند و گفتند به ان پاسخ خواهند داد.
بعد از حمله به فرودگاه صنعا گزارش شد که یک هواپیمای ماهان ایر در فرودگاه حدیده به زمین نشسته است. ویدیوهای منتشر شده نشان می‌دهد مسافران این هواپیما پیاده شده‌اند. خبرگزاری فارس اعلام کرد هیئت رسمی یمن به سلامت در حدیده از هواپیما پیاده شدند.
پبش از این هم یک پرواز شرکت هوایی ماهان ۱۳ تیر به صنعا رفته و ساعاتی بعد به تهران بازگشت. این پرواز ساعاتی پس از آن انجام شد که گفته شد «توافقنامه حمل و نقل هوایی میان اداره کل حمل و نقل هوایی یمن و شرکت هواپیمایی ماهان ایر» ایران امضا شده است که بر اساس آن «۱۴ سفر هوایی در هفته از سوی ایران و یمن می‌تواند انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76996" target="_blank">📅 15:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌های دریافتی یک ساعت و نیم پیش:
‌
درود بندرعباس ساعت ۱۲:۳۱ دقیقه انفجار شد
بندرعباس انفجار ۱۲:۳۱
بندرعباس دو انفجار شدید
پایگاه هوایی 12:31
سلام بندرعباس ۱۲:۳۰ صدا انفجار اومد پایگاه هوایی فکر کنم زدن
سلام دارن بندرعباسو میزنن خداحافظ
آبادان بریم صدا اومد 13:19
صداش هم با لرزش بود ینی احتمالا درست شنیدم
صدای انفجار اومد تو ابادان
کجا بود و نمیدونم
هرچی بود اطراف پالایشگاه بود احتمالا باز پدافند الفی یا جزیره مینو
سلام وحید جان، صدای انفجار در آبادان
سه بار شنیدیم
ساعت ۱۳:۲۷
بندرعباس
ساعت ۱۲:۳۰ ظهر امروز دو تا انفجار بزرگ تو پایگاه هوایی رخ داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76995" target="_blank">📅 15:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aad6931866.mp4?token=G-TTQE8Z3gomiipOOV_zhPZIl_MO12qbPqGeKMjMiTcT_x6p_S_Kd701PkmKyy7DJnnOdoGlEC1-Aden2Tbg_vQg8nz5hAfq-VjjhnDes3TMeeajb_FP3xd99ksVnst6lbKBlLmNUFTzonhVfe3-QwPYZ-K6KlvXzKTIbyA0lIjEacRzT8CLkr0qY6zuu1TVKSxZeA-V-EAvVc1EuQKyRFa2BQr2_NSrDnx7FfkFHrk5XD6-2ovoU3KSJQcX2nIhVk0J91Mf-809q7tAX9ImiJzZxJooju2higdeepqjboWaN7iVENVoAOb41yzG4oGWuTZH_5qxoI9_RZOA4330fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aad6931866.mp4?token=G-TTQE8Z3gomiipOOV_zhPZIl_MO12qbPqGeKMjMiTcT_x6p_S_Kd701PkmKyy7DJnnOdoGlEC1-Aden2Tbg_vQg8nz5hAfq-VjjhnDes3TMeeajb_FP3xd99ksVnst6lbKBlLmNUFTzonhVfe3-QwPYZ-K6KlvXzKTIbyA0lIjEacRzT8CLkr0qY6zuu1TVKSxZeA-V-EAvVc1EuQKyRFa2BQr2_NSrDnx7FfkFHrk5XD6-2ovoU3KSJQcX2nIhVk0J91Mf-809q7tAX9ImiJzZxJooju2higdeepqjboWaN7iVENVoAOb41yzG4oGWuTZH_5qxoI9_RZOA4330fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: سنتکام موج دیگری از حملات علیه ایران را به پایان رساند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساندند و با مهمات هدایت‌شونده دقیق، ده‌ها هدف را در چندین نقطه مورد اصابت قرار دادند تا توانایی ایران برای ادامه حمله به کشتیرانی بین‌المللی در حال عبور از تنگه هرمز را تضعیف کنند.
نیروهای سنتکام با استفاده از جنگنده‌های آمریکایی، شناورهای نیروی دریایی، پهپادهای تهاجمی یک‌طرفه و برای نخستین بار، شناورهای بدون سرنشین تهاجمی یک‌طرفه، سامانه‌های پدافند هوایی ارتش ایران، سایت‌های راداری ساحلی، توانمندی‌های موشکی و پهپادی و قایق‌های کوچک را هدف قرار دادند.
تنگه هرمز یک کریدور دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در اختیار ندارد.
نیروهای ایالات متحده در وضعیت استقرار و آمادگی قرار دارند تا تضمین کنند که با وجود ادامه تجاوزهای بی‌دلیل، مزاحمت‌ها، تهدیدها و اعلامیه‌های خودسرانه ایران، آزادی کشتیرانی همچنان برای کشتی‌های تجاری برقرار بماند.
CENTCOM
سپاه: پایگاه آمریکا در بحرین را نابود کردیم
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی به نقل از منابع حکومتی:
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔺
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات خود ادامه می‌دهد.
🔺
در پاسخ به این شرارت‌ها، رزمندگان هوافضای سپاه در مرحله دوم عملیات مقابله به مثل خود مراکز مهم تعمیرات و نگهداری بالگردی، آشیانه هواپیمای جنگ الکترونیک پی ۸ و مرکز فرماندهی و کنترل پهپادی ارتش کودککش آمریکا در پایگاه آمریکا در شیخ عیسی بحرین را در هم کوبیدند.
🔺
عملیات مقابله به مثل ادامه دارد.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
سپاه: آمریکا را در کویت منهدم کردیم
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانه پدافند هوایی پاتریوت در پایگاه آمریکایی در علی سالم کویت و همچنین یک سامانه راداری راهبردی FPS در پایگاه احمد الجابر را به طور کامل منهدم کردند.
🔹
عملیات مقابله به مثل فرزندان غیور شما ادامه دارد.
🔹
تنگه هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76994" target="_blank">📅 06:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی:
درود همین الان صدای انفجار بندرعباس
ساعت 5:47 یک انفجار بندرعباس
سلام وحید
صدای انفجار  الان توی بندرعباس
خیلی شدید بود
سلام بندرعباس الان صدای انفجار اومد ۵:۴۸
سلام وحید 5:47 دقیقه بندرعباس صدای انفجار اومد
۵:۴۸ بندرعباس صدای بلند
05:48 بندرعباس صدای انفجار، خیلی زیاد بود صداش
5:48 انفجار مهیب در شرق بندرعباس
فاصله یک ساعت و نیمی ازمون نهایی صدای انفجار مهیب بندرعباس
سلام ۵:۴۹ بندرعباس یه صدای انفجار شدید اومد
سلام همین الان صدای موشک در بندر عباس شنیده شد
همین الان بندر عباس صدای انفجار ساعت ۵:۵۰
بندرعباس
ما ۱۲ فروردین هستیم
کامل شیشه لرزیدددد
درود آقا وحید همین الان
بندرعباس انفجار خیلی شدید
بندرعباس الان صدای انفجار همرا با لرزش شدید
5:47تک انفجار بندرعباس
صدای انفجار نسبتا شدید بندرعباس
بندرعباس همین الان انفجار خیلی شدید از توی خواب پریدیم
وحید ۵:۴۸ یه انفجار خیلی بزرگ بندرعباس صداش ب شدت زیاد بود
صدا اومد  موجش خونه رو لرزوند همین الان بندرعباس خونمون نزدیک جاییه که موشک میزنن
سلام بندر امام از ساعت چند همینطور دارن میزنن
🔄
صدای یک انفجار دیگر ساعت ۵:۵۱
05:51 یکی دیگم زد
صدایی بلند تر همین الان
دوباره انفجارر
دوباره زدن ۲ تا انفجاز بندرعباس همین لحظه ۵:۵۱
دوبارهههههه
سلام همین الان دوباره صدا انفجار اومد بندر
بندرعباس دوباره صدای انفجار اومد ساعت 5:51
ساعت 5:51 یک انفجار دیگه بندرعباس
سلام ۵:۵۰ بندرعباس دوباره صدا انفجار اومد خیلی شدید بود
این دفعه چیزی تکون نمیخوره فقط صداش بلندههه
واییی دوباره زدنن
دومین انفجار شدید تر
نزدیکی پایگاه هوایی
سلام
صدای وحشتناک انفجار از سمت دریا، همبن الان بندرعباس 05:52
سلام میشه خواهش کنم بذارید تو کانال؟
الان دارن حمله میکنن
بعد ما باید یه ساعت دیگه آزمون نهایی بدیم اگه خدایی نکرده کسی خون از دماغش بیاد کی پاسخگوعه؟ جدی باید یه فکری به حال ما دانش آموزا بکنن
همین الان ۵:۵۳ بازم یه انفجار شدید بندرعباس
خونمون داره میلرزه
😳
بندرعباس
بندرعباس پشت سر هم داره میزنه بعد بچه های یازدهم یه ساعت دیگه باید مدرسه باشن آزمون دارن
نهایت نامردیه در حق بچه های جنوب شب تا صبح چشم رو هم نذاشتن از صدای انفجار
بندرعباس احتمالا مناطق نظامی داخل شهر (نیروی دریایی سمت صداوسیما) رو داره میزنه که صدا اینهمه واضح و شدیده
چون انفجارهای قبلی رو ما با اینکه تقریبا وسط شهر ساکن هستیم متوجه نشده بودیم.
🔄
صدای یک انفجار دیگر شدید ساعت ۵:۵۵
بندرعباس باز زدن ۵:۵۵
۳ انفجار دوباره ۵:۵۵ بندرعباس
05:55 از بقیشون شدیدتر بود
آقا دوباره انفجار
وحید بندرعباس همچنان داره میزنه
صدای سوم انفجار در بندر عباس 5:55
۵:۵۵ دوباره صدای انفجار
5و55 دوباره زدن بندرعباس
بازم زدن هر بار شدیدترر
بندرعباس انفجار ۵:۵۵ درگیری از سمت ساحله
۵:۵۵ سلام برای بار سوم صدای انفجار بندرعباس اومد خیلی شدیده
آقا وحید سومی هم خیلی شدید بود
۵:۵۵ یکی دیگه زد خیلی بد بود
دوبارهههه همونقدر صدای بلندد و لرزیدن شیشه ها
برای بار سوم
این بلند تر از دوتای قبلی
۵:۵۵ انفجار سوم بندر عباس
۵:۵۵ صدای انفجار ب شدت بلند و مهیبه خونه رو کامل می‌لرزونه
بندرعباس ساعت ۵:۵۵ سومین تک انفجار قوی
وحید جان قشم هم صدای انفجار حس میشه خیلی شدید نمی‌دونم کجا اینجا یا بندر
بندرعباس صدای انفجار سوم
خیلی شدید بود
هر بار شدتش بیشتر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76992" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cFDn-0-Q3stux-1hOnLmJ91jSzrvLjXmJGxZ0DcCYiDk-ckHrkt8rf4E2z-J89pBOZpGmAQf5IYm0rxMrULHS3Plaskzrb9esEE70mDCaUCc2vJED0KRBeaXOB8vZAQ0obShloIqioUaGduaudfFgXmclq-4IQa7_fNLNcpZZFSqV7BHkJtS8WtgT3qZnhlKGXT4We-Wa-d9cOV-lDgVxjyffLcGSHW9HOITFS06WOBB8Py5dX8PCJS4TuuORauNLsilX_WPRfGm1bNbRh2houn3ziuQISOHD3R8GWwZ7qpKC3pbvK4GqFrDv36JCCqkuGRdCHF1ZfvxsWu33cicug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HnteobKk2_Iq3oSSMJY_QBd5tT--pIq8FYhG5Rx5S9X9TbXZyf4GmSQMF5xdl_d-vh54aMIL4z8hq0V20Es_4ZWkZ4EQ5E1Q7FaSpHWz4yZKYi9WsT_h4lGre2D8BdZJPYlutSI_wQkJLYTkKg5DBt7v_hyTKKB_CWk6Ik6Z1OkAz6l9-Im4qp-bNo3dQ9dvHcnMCPBacKBzMZ6EkbZhGqXhpsB7Wq8u3yMb0w0BrDSZAXZM9aqMIIoIPdUe-tgDi-FHdQpOCnoDlmcsoAysBmFfJEUJiUgxxA1f8qhiv3p6euBHl87elmbnhnlfgfOLi8ySUTV5DzSZUluuwT6LDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79d39aa187.mp4?token=i-3-Xw1u4Jt8PzqqoKSKv1U5BDgpfakz3eVCIIdAFZlI8K0Md-E4wuzcf5rAB2bHc658gJA1iT5pKhnVlth2DhIihIc6LVFZXMRYKua1QKudFHFqMNN9g0G-WiY7nyNUrFxxpXFFLaHJyb1oKmMIMFA-GyOViyo9tnjbrCTTobrBOyqCEfNPVOCeATJ5Le-SE41iwoqWssxBA-XEIIUyhYkBfo4CHHFIJKSGw-5ku6iPwbGXEZLwhyCioghaCEVW_cgLx7qNfyaPHNyi9hYkPke1Ym6vQzAkCo926oXr187qdYggw_2QFTidXX4ekDR86naEbVtYx5DEf5kbaK3RtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79d39aa187.mp4?token=i-3-Xw1u4Jt8PzqqoKSKv1U5BDgpfakz3eVCIIdAFZlI8K0Md-E4wuzcf5rAB2bHc658gJA1iT5pKhnVlth2DhIihIc6LVFZXMRYKua1QKudFHFqMNN9g0G-WiY7nyNUrFxxpXFFLaHJyb1oKmMIMFA-GyOViyo9tnjbrCTTobrBOyqCEfNPVOCeATJ5Le-SE41iwoqWssxBA-XEIIUyhYkBfo4CHHFIJKSGw-5ku6iPwbGXEZLwhyCioghaCEVW_cgLx7qNfyaPHNyi9hYkPke1Ym6vQzAkCo926oXr187qdYggw_2QFTidXX4ekDR86naEbVtYx5DEf5kbaK3RtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره شلیک موشک از بوشهر
Vahid
سلام ساعت٥:٢١ دقيقه صبح از شهرستان جم موشك بلند شد
همین الان جم چهارتا موشک بلند کرد
سلام وحید
شلیک موشک از جم-بوشهر ساعت 5:21
سلام ساعت ۵:۲۰ از جم صدای پرتاب موشک اومد
همین الان جم چهار تا موشک پرتاب شد
ساعت ۵:۲۰ بامداد چهار موشک‌از شهرستان جم بلند شد
وحید جان سلام . همین الان از جم ۴ تا موشک زدن
پیام دریافتی:
direct impact in bahrain, smoke visible from far away
[اصابت مستقیم در بحرین؛ دود از فاصله‌ای دور قابل مشاهده است.]
🔄
وزارت کشور بحرین با انتشار هشدار فوری در اکس اعلام کرد که آژیرهای خطر در این کشور، صبح دوشنبه، به صدا درآمده‌اند. این نهاد امنیتی با صدور این بیانیه، از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش کامل، به سرعت به نزدیک‌ترین مکان امن و پناهگاه‌ها بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76988" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FU9wQNlNIuu2BgyIGTViqCz9Dwaytaa_kup8Nh3jAIf47xapwEX6giKgxVnp9aaWDFtzYtqbSIt3clDCZI5Z7xcCSL59lppf45Eb0x_-DylBMuqKUjJy1gM0q5UGMT3UJSr5gTyHuXAWBMu_S3oNhCogWXxPY3CacmCXH5Dpdo8BPV6H-Q_4u5w6HXu2bscfNRpB-o_XgFp9Uu4iIA8hotL9gkMuMwtDieqYAy1GsVk3iUWjmJW321nhMC6-e0mVl58Zgvn351mbq-q55oqI71j1hSzRnmMGlfytmsl7vjIJpO1GaiiCD4UUMjKJs7IyZ4JMY3GvfxR1FzAwvVYAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در
تروث سوشال
عکسی از لیندزی گراهام منتشر کرده است با کلاه
Make Iran Great Again
سناتوری گراهام در این تصویر کلاهی بر سر دارد که روی آن نوشته شده است «ایران را دوباره با عظمت کن» و عکسی بزرگ از صفحه دونالد ترامپ در دانشنامه ویکی‌پدیا را بدست گرفته است.
دونالد ترامپ در این پیام غمگینی عمیق خود را از درگذشت سناتور لیندزی گراهام ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76987" target="_blank">📅 05:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ce9a9iPUoJISI1qVcCX0B8oUztAKPJvhINeznDVzvS9AE8OKs3JJld2K-K69J9DHJs2ss8b2w7q_So1ApL4KS-TQ_XumoJfH8TdSKSp8kqeDl7bT8HRAe8kd2cSGf7nZxUMJa4BBbKDHNRa9sOIHsJto6b8SoeyP7NbpY5OCP8N8aHMAbvBdbbF1j5XUpgQzI5cRumCZTcgqH-TiWQt4P5o429iADeEcCd6JCNyN114qXLp3QzQtMI3MO1OKwsoYEfREswQaDWCluhDSoaL6E6-CavWPfse8EKTmYq7DbRTX0wCAqMl-_EQCKRqkD10f_jvCjHueGQ9O0czzFpZ65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fKb1OR4YQs7ncILWu9ilTbG64q1x7-GNakpi2t-hojKn0uJjivee3euvXrZUu0upQqhtjJm35tacHzPa62jZy5kZDrxOueSuI8Pl9zpvzJ9b94iUa3d5e8Mzhnkd0vRyIHbl0OExgQl7k8hOQlytCepQUMdR83C0pE9IW345MC49j3Di9idrXW3nncGJbQ-6n2B0ch6FJCiaxU2jWsnTCNTyeYFtAIhmas21TxWAMH1CKxtXYHPI6paYISIrWkD5UEwsHCJjyWJqbM5GH9DZt0CCsrQl9oEHhKhce6YT9C7lr_EXwmt6PEcCnbiFC9hJ9VUb3EUNltnvb94NvjcZ7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان دوباره ساعت۴:۲۸ دوتا موشک از خمین زدن
شلیک دو موشک از خمین
درود ساعت 29 4  الیگودرز دو شلیک موشک
خمین الان دوتا موشک
وحید از سمت خمین و الیگودرز دوتا شلیک کردن ۴:۳۰
همین الان صدای انفجارزیادامد
من حوالی شهراراکم سمت خمین بود
خمین ساعت ۴و۲۷ دقیقه موشک پرتاب شد
+
از زنجان و ازنا هم پیام‌هایی دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76985" target="_blank">📅 04:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VSeSNEwm9ExvmwlIXIrL50mYGmBT0TDQHnUpWB4ry56cksBj-GfbGviu0VJKL18S9TPw5nJ5vIJv7BI7x5PVoatZnXlPTHBrC8Ko7Vr7jVBO_HG4IyTfV0sO-wU0Ie8Oc94BHFO_ZfTUpsvk9SXTtAHRKODob6-x1bhZqyeda7s33JA2YKxtgQcK5-j5h3eppixRXfmXWTXg6xCCGEIS28yRcqaXNYrkq9pHKK7BaLX99Qj6gCnMPKnfMpHnpKeq2MCCPjn2EZOIN-TNgyX8BWSL3jPP93gwJxH2CxPog06dmMbwFvfPEu8JB6ou6BknjQ449L_QopkoMCXMmX-keQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l2Ac4F8vfXUg7Of4CTW8E9ApF6FK3LY65QAlKCDm6vki9BS4v0_tuYDRK8isF7PsT3kapYqYYL3B5--LVpuyPzPZB2YTrU2wmWYBuF1hnwMf1-YI2CdWtbin1-MYF39SKy7VETIVzYRZNAJD5sJ4PEP2rZu2zCPky5udcjXxe1P2bIp3gFK_XUp2hvSQPnaCULGEWWa6oj3NX8q-p_dJIM1tDeJW7i_Z5A4SESQ5I5ipSuwtlzudr1oZ319sd9PyylCfAAC9PqTlbG4ZapBghUy09hkg12TwQD4gjIzjK7BmlKcxFlGX2ixSzFhvysrClLAsN9hH67689LoIqeqqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BgiFawh7I_5Z6jWh3EK4StxL6YXN2io86hcZu8E_D1VrxUoRGzt2u3zLE4oFYDlvRnl7qi4plU5CmIryarvvEzI4-hioLgV8r978cd5MPnLKZpdoAWsVHe4reRq2ogDY5oXNWBzaWPUdwnHXR89o8YBeT11T8X-VEnFx5pMsMLSwKTkdxaBWvzFcnDPCAiOLqqCJp7tgxnzWUFqRy9sFgSyDsj7tEiRlAlUNDNY9WJG3u870IWJFJ5qQstXDcQ3a8jLEx4Ci-9rJl5qIyLN4UyjSCJXCvPPiBt0u4geaBvfrGeeWZI5iOUuF7uQkfbRp_0DlszsUc6GhBzYVmvXpvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/892957aa92.mp4?token=dlaUHyLigSpG5Hj328Q4WYEL2O8QKQnp0GlChYZTTgECkTsVosukZfFiqzfexNKshuswLCRwuJxayjyq8os6dCENKsMocmpqYTutf8B2UNdfd3voEfw58AHZanbocLYS3-u_Jztcl0eZ1M6-KSlS192yngzuzw-Q_pQg5hJB6V2_IeGlctLxuFMbW2kuforUJB0uAqOCYVsEXHWV-s5YGwRu2L26zDXHiCBsIp-EDaRBSOB1T0nnvgsag0zaN4Q32j_GprvJ0BHqX_GdJDMEuKmsjLehnSzr3UoM0fCHMOCV3zwg8OwxlliHAxv96yOTTeMNXFe7MFG7PISj65MdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/892957aa92.mp4?token=dlaUHyLigSpG5Hj328Q4WYEL2O8QKQnp0GlChYZTTgECkTsVosukZfFiqzfexNKshuswLCRwuJxayjyq8os6dCENKsMocmpqYTutf8B2UNdfd3voEfw58AHZanbocLYS3-u_Jztcl0eZ1M6-KSlS192yngzuzw-Q_pQg5hJB6V2_IeGlctLxuFMbW2kuforUJB0uAqOCYVsEXHWV-s5YGwRu2L26zDXHiCBsIp-EDaRBSOB1T0nnvgsag0zaN4Q32j_GprvJ0BHqX_GdJDMEuKmsjLehnSzr3UoM0fCHMOCV3zwg8OwxlliHAxv96yOTTeMNXFe7MFG7PISj65MdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'انفجار و آتش‌سوزی [سمت] فرودگاه
#امیدیه
در خوزستان
دوشنبه ۲۲ تیر حدود ساعت ۳ بامداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76980" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام‌های دریافتی:
‌
اهواز صدای خیلی شدید اومد
همین الان انفجار شدید اهواز
درود وحید جان ، همین الان اهواز صدای انفجار شدید اومد ساعت 1:31
اهواز ساعت 1:31 بامداد صدای انفجار
اهواز ساعت ۱:۳۰ صدای ۳ تا انفجار
هواز همین الان زدن ۰۱:۳۲
سه تا موج انفجار پشت‌سر هم ، شدید تر از دوران جنگ  بود ، من مرکز شهر ساکن هستم
سلام دارن اهواز و میزنن ساعت 1/28دقیقه
سلام وحید ساعت ۱:۳۰ سمت فرودگاه و گلف رو زدن خیلی وحشتناک بود
😭
😭
😭
سلام  آقا وحید. اهواز ساعت ۱:۳۰ دو تا انفجار پشت هم
وحید همین الان ساعت ۱:۳۰ اهواز رو زدن، کیانپارس خیلی شدید حس کردیم
اهواز دو تا محکم زد
ساعت ۱:۲۹
اهواز و‌همین الان زدن صدای سه انفجار اومد نزدیک سیصددستگاه/سپیدار
اهواز صدای انفجار
سلام الان ساعت ۱:۳۲اهواز سه صدا انفجار اومد
اهواز همین الان دو صدا همراه با لرزش ساعت ۱:۳۰
وحید جان همین الان ساعت  ۱:۳۰ اهواز صدای انفجار اومد.
وحید جان اهواز صدای انفجار شدید
وحید انفجار به شدت قوی تو اهواز خونه لرزید ۱:۳۰
سلام وحید جان ساعت ۱:۳۰ اهواز صدا دوتا انفجار اومد منطقه کیانپارس یک مقدار ضعیف بود صداش
سلام وحید
ساعت ۰۱:۳۱ اهواز صدای انفجار اومد
فکر کردم خیالاتی شدم، اومدم بیرون دیدم همسایه ها هم ریختن بیرون
وحید جان
اهواز ساعت 01:31  دو تا یا سه تا صدای شدید اومد
اهواز لرزش شدید و صدای انفجار
دقیقا نمیدونم کجا، اما زاویه‌‌ی صدا از سمت چهارشیر بود به نظرم فکر کنم سپاه چهارشیر
صدا انفجار ماهشهر
ماهشهر همین الان
ما اهوازیم کوی باهنر
صدای انفجار شدید
بندر ماهشهر صدا اومد.
اهواز ما سمت کیان آبادیم و واقعا صدای انفجار زیاد بود
🔄
همچنان خوزستان:
انفجار شدید ماهشهر"همین الان"
دوباره الان ماهشهرو زد،1:51
شش انفجار 1/52 قشم-طولا شنیده شد
سلام ماهشهر هم صدای انفجار اومد
دوتا تا این لحظه 1:52
سلام وحید جان اطراف بهبهان تا الان صدای ۶ انفجار اومد
همینطور دارن میزنن
سلام قشم همین الان صدای چند انفجار
صدای از دور از سمت غرب جزیره
همین الان صدای انفجار زیاد بالای ۵ تا داخل قشم شنیده شد
بهبهان ساعت 1:52 بامداد صدای چهار انفجار شدید
سلام وحید ما نزدیک فرودگاه ساکنیم حدود ساعت حدود یک و نیم دوتاصدای انفجار اومد همه همسایه ها ریختن بیرون معلوم نیست کجارو زدن
قشم ساعت ۱:۵۰ زدن ، چندین انفجار شدید
بهبهان‌رو الان چند بار زدن
روشمهر پایگاه موشکی ساجد
بهبهان خوزستان/ ۱:۳۲ ... صدای ۲ انفجار.
مجددا ۱/۴۵ تا ۱/۵۰ بهبهان خوزستان صدای ۴ انفجار
سلام وحید جان
امیدیه صدای بسیار خفیف انفجار
مشخصاً درون شهر مورد هدف قرار نگرفته
احتمالا دقایقی بوده
همین الان خوزستان بهبهان ۴ بار پشت سر هم زدن
نمی‌دونم کجا بود
🔄
ساعت ۲:۱۵ دقیقه دزفول رو زدن
در و پنجره ها لرزید
دزفول خوزستان
همین الان زدن
سلام وحید
دزفول رو دارن میزنن
۰۲:۱۵ دقیقه
سلام دزفول رو دوبار پشت هم زدن
🔄
موج بعدی پیام‌ها از دزفول درباره شنیدن شدن صدای انفجار در ساعت ۲:۱۹ و ۲:۲۵
🔄
امیدیه ساعت ۳:۰۲
درود امیدیه خوزستان همین الان صدای چندتا انفجار پست سر هم اومد
امیدیه خوزستان چند دقیقه پیش ۴ تا پشت هم زدن کل شهر لرزید
ساعت 3:02 دقیقه
صدای بشدت وحشتناک توی امیدیه اونقد که شیشه ها لرزید
پازنون هم زدن
صدای چند انفجار  در امیدیه شنیده شد
حدود ساعت 3 بامداد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76979" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H6ImycqV23u-4MXMf-ZttpJnUcP-PO9Z2vwMjeWFWZoiCAMvM5cvf5ncepidRNR7R9aBMvXDk8Ai023uB4F1ZJiORH6ulx6P7n3SEKdlIVZb0OnAd5R0-7JylFdlEkF_Pk6gdcIdXJy1z6Jj4r83tf6raVTxJbXFdOmXi8VdZV_FISSBuX28tGZtCzN5HEqQnYoTlq7twJFJeadm-gLZtQxPQpBBIRNAxd8mMHl_ruzzAuTSKFAlsBIcfZi8rX5Q8eLT6N1d5mGcOe7IOKhlVzgUiXYvViF2CqsNSZiTEJuxwF-0hUnAcG-iJOiQDnSoJ7y_Tr_a8d5ggia0MDauxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cfc3526ac6.mp4?token=j1dmMb828NhgB8y5jhHiedPOOmRzmngjOIamQgTytmny9kTJEQuIjuCArVkoalX4HZy6g84b_nvNgGB9__lT2iq5xB3xX7itMSybP-1WfaSB-mxr7jqgsvABabqDq69-NngUbtazYkQxFjhkdOUbJ6vBLZsGUSoIuVHEAbliKs7n43TW-XysTREJbcKSdvd3geMrdea7gJBD0TDByLWi9Q4-toDeq1q0lWjx7z1ED3zvY2oluG5FnzRdBTFjnEXlx5cbHMgKwHpyIrBdZTUqUJez7-eBEYPNCNsZgnX9p1body-OvN4EXlnkgwfhCHJKbMrb63fCzSU3cnrjI-2FVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cfc3526ac6.mp4?token=j1dmMb828NhgB8y5jhHiedPOOmRzmngjOIamQgTytmny9kTJEQuIjuCArVkoalX4HZy6g84b_nvNgGB9__lT2iq5xB3xX7itMSybP-1WfaSB-mxr7jqgsvABabqDq69-NngUbtazYkQxFjhkdOUbJ6vBLZsGUSoIuVHEAbliKs7n43TW-XysTREJbcKSdvd3geMrdea7gJBD0TDByLWi9Q4-toDeq1q0lWjx7z1ED3zvY2oluG5FnzRdBTFjnEXlx5cbHMgKwHpyIrBdZTUqUJez7-eBEYPNCNsZgnX9p1body-OvN4EXlnkgwfhCHJKbMrb63fCzSU3cnrjI-2FVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: 'بندرعباس، ساعت ۰۰:۴۳ بامداد دوشنبه ۲۲ تیر'
Vahid
صدا و سیما:
بر اساس گزارش‌های اولیه، حمله امشب به دکل مخابراتی اطراف روستای طاهرویی سیریک بوده، همون جایی که در حملات قبلی هم مورد اصابت قرار گرفته بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76977" target="_blank">📅 01:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRFjvEWNF5urDLBZdZAltarhyWf4gjKemV4x36qUogKkBYfh6LNzXpveWweUPRzLMcOjwfT4mLVxqWoFyJJy69xU5R6MkxsG7jun7LNpBycp9211vr-IKP50KlD2bAjjwsGy0dYX8f9XxJ0O37wy_0E3onrkmEJ0f_USmi5pn7JNBus82tXRNv6YTMF9d84FaP3JsLqy4ebU2bNfG-sLtVGWOLSNEUVsjOJM9d7AHcxnEeiXhdBNaBk8dqdOCM0dgdcU4bt4y7QyP8frWg3aUruh-gVf8ppwa6CV5Mxv8pYIi7s-tr7WSH6JbI3Hlj6KsLfyQIPoj14_q7CEHb6-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت سنتکام:
ساعت ۵ عصر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی این کشور برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76976" target="_blank">📅 00:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
00:38 صدای چندین انفجار در بندرعباس
همین الان انفجار پیاپی بندرعباس ۰۰:۳۹
بندرعباس ساعت ۱۲:۳۸ صدای انفجار چنتا اومد
باز هم داره صدا میاد
بندرعباس همین الان چهار پنج صدای انفجار پشت سر هم اومد
😭
صدای سه انفجار بندرعباس ساعت ٣٨ دقیقه بامداد
00:39 بندرعباس سه چهارتا صدا اومد
قشم الان صدای انفجار اومد
ولی از خود جزیره نبود، بندرعباس سیریک یا روی دریا بود
سلام وحید از بند عباس خبر میدم صدا ۳ تا انفجار شنیدم شدید بود شیشه ها لرزید
🔄
جنگنده الان بالای شهر جاسک
۴ تا صدا انفجار اومد
دوباره جاسک داره میزنه
همین الان
سه انفجار درجاسک
همین الان دوتا انفجار جاسک
صدای جنگنده هم خیلی زیاده
صدا و سیما:
🔺
دقایقی پیش؛ شنیده شدن صدای چندین انفجار در اطراف روسنای طاهرویی سیریک
🔺
صدای سه انفجار در جاسک شنیده شد
🔺
صدای چند انفجار در قشم شنیده شد
🔄
خنداب در استان مرکزی:
سلام وحید جان. همین الان سمت ساعت  یک بامداد صدای جنگنده شنیده شد.
خنداب.
همین الان صدای انفجاررر
سلام ۳ دیقه پیش خنداب رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76975" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXfhTa8f_7WKlopYIUb0tJTrt7es0VeD0QJVGHNcSZQN64f9yMeALvBS7eotgz6-ZGQNzYGaFEXD3RCH7rSu2No6F3zzTVa3cDoaUsAPwNCrFVGHQB-xJPQ9V2h6QyseTKwAA4XByPtZgd31p7YDOhMg085lXHIdUAKWWW-v7iUZHadn8HnahkH-cv6DyONq0ywslnArHE_B429CjSAYckuyNqFmZP7vugoKEamnZE1KGCjaY2s-6czLbFMbKALmkp33gDKbaetQtvIug2CE8odAU-gE5oN_fH0MTFbmrHlQ8NGbWor2ajrwwLmTKrwYFJN9xdxwhfRWwrmrAMqa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام) شامگاه یکشنبه ۲۱ تیر، ادعای رسانه‌های وابسته به جمهوری اسلامی درباره کشته شدن نظامیان آمریکایی در کویت را رد کرد.
سنتکام
نوشت
:
🚫
ادعا: تبلیغات ایران امروز مدعی شد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. نادرست.
✅
حقیقت: هیچ گزارشی از کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد. وضعیت همه نیروها مشخص و تأیید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76974" target="_blank">📅 00:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری مهر:
گزارش‌هایی از شنیده شدن انفجار در جزیره بوموسی؛ وضعیت جزیره لارک عادی است
ساعتی پیش منابع محلی از اصابت ۲ پرتابه به جزیره بوموسی در جنوبی‌ترین نقطه کشور خبر دادند.
در حوالی ساعت ۲۰:۳۰ امشب، صدای چند انفجار دیگر در بندرعباس شنیده شده است که به نظر می‌رسد مربوط به شلیک یا اصابت‌هایی در محدوده دریایی بوده است.
پیگیری خبرنگار مهر از جزیره لارک نیز حاکی از آن است که وضعیت در این جزیره واقع در تنگه هرمز کاملاً امن بوده و هیچگونه گزارشی از حمله یا حادثه‌ای در این منطقه وجود ندارد.
اخبار تکمیلی متعاقباً ارسال خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76973" target="_blank">📅 21:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q5Fml5uq0IN5i__wM513aErCwICNQExrw6zNWsYduvz4ZvNgcU-kadR2J_0vEVWJXw4OCUTsQcar3LSFT7NvZdCMXeyUerXiqwEZY5ae_supwOul4fXEwfWjc0vH7_1uxHbhE1HTsXmo9ro7G8kxrtIiTo1AzwOiKaLGAw5bkGb963Ev92g92e8F61tOIXiK3NM1KFtZysy3trE6mpVcKqnC4mjkhOaiNVarMg6Xhx9-Vv4FhShf6o-KWfjTsngQa6KUdbdOfCNZCtKnLu4Olj-aILKaVKs8GcfEowmoZA_LpHHQmCHy6Y2TRKXttS5kGrcCj08SBapy-beSpiBIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fN_n6OarGRkPwr8a48Fo8lmlyWk_ODA74WNjW4nzNFVotVQ9FfGJRryUd5CTe3GMBttVrGOvTjTxgjdn0s2xUvgUY4Ov7yIzw0DYsWLGGMbpbLpoKz4HiSC7SvyXF73PYUUOpYdEKVNYqAI6iR5-wF2kKWKc-TagP1Xf6ToCxfObBHadbgzYyD1EWOfsSglAkVXPlhudX1m3ElhQfR6IFW93sEghNM5bwyPrfZtiNVwkk1eWJNSCjmXcmNKSdB4rb5TPPeZv3AZluPJlEEJsSAdASMX4AE4ISuEjvsm19qT81591-0xEpZO1gB_lx5uhourkiRU7xub9_Y384wdu4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=owshZPJ45bAraqgc9tJd4EmaLKvtMvHHqnmdGdYy4ehi2g8oJ65-9Lov51yeDvB50J4J5USR3uQMS4aTPt8QlOzDCdQ_L1cb8TCeHf1LZ0I6lwIOTf6oR9m_z499X3eIkiuGzYVj4Wn8D-95Rz8xd5nA5XJ1nhFIlHHgrxYS-T8bA0V-jUZt30b5va0UoWuE4EF4EWm_qjPnIa-epU6i38GCxq-ytYTn9kOk0n43P9ODIvfWbyKL3hEqB2XiZPGIpJh3lBT9z6SySQ39nrou8PZhHtBRygfVtT8iNcetvGzhrtnF4__y2gMqMiE5MYujnPzK5ISYngX5nimbmlYrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=owshZPJ45bAraqgc9tJd4EmaLKvtMvHHqnmdGdYy4ehi2g8oJ65-9Lov51yeDvB50J4J5USR3uQMS4aTPt8QlOzDCdQ_L1cb8TCeHf1LZ0I6lwIOTf6oR9m_z499X3eIkiuGzYVj4Wn8D-95Rz8xd5nA5XJ1nhFIlHHgrxYS-T8bA0V-jUZt30b5va0UoWuE4EF4EWm_qjPnIa-epU6i38GCxq-ytYTn9kOk0n43P9ODIvfWbyKL3hEqB2XiZPGIpJh3lBT9z6SySQ39nrou8PZhHtBRygfVtT8iNcetvGzhrtnF4__y2gMqMiE5MYujnPzK5ISYngX5nimbmlYrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای شاخ‌دار دکتر کلانتر معتمدی درباره رابطه واکسن فایزر با نازایی و عقیم شدن زنان
🔹
محمدرضا کلانتر معتمدی، دبیر فرهنگستان علوم پزشکی، در یک برنامه تلویزیونی گفته است: «بعد از ۸ ماه مشخص شد واکسن فایزر حاوی همان ماده‌ای است که در واکسن ابولا بود و دختران را عقیم می‌کرد.»
🔹
این ادعا صرفاً تئوری توطئه بی‌پایه و اساسی است که از سوی پزشکی مطرح شده که در جریان تحولات علمی روز قرار ندارد.
🔹
واکسن کرونای فایزر چه در ساختار و چه در عملکرد، شباهتی به واکسن‌های تأییدشده ابولا ندارد.
🔹
سازمان بهداشت جهانی تأکید می‌کند: «هیچ شواهدی مبنی بر تداخل واکسن‌های کووید-۱۹ با باروری وجود ندارد و هیچ مدرک بیولوژیکی وجود ندارد که نشان دهد آنتی‌بادی‌های ناشی از واکسن یا ترکیبات آن آسیبی به اندام‌های تولیدمثل وارد کنند.»
🔹
محمدرضا کلانتر معتمدی، پزشک و جراح است و به عنوان عضو، دبیر یا حتی رئیس گروه‌های علمی فعالیت می‌کند، اما اغلب اظهارنظرهای او در فضای عمومی جنبه اجتماعی و سیاسی دارد.
🔹
ما در منابع عمومی چند مقاله از او پیدا کردیم که عنوان موضوعات آن «اقتصاد مقاومتی در نظام سلامت»، «فقر و هزینه‌های جراحی»، «تجربه‌های دفاع مقدس» و «مولفه‌های فرهنگ ایثار و شهادت در جامعه سلامت کشور» است.
🔹
او یکی از امضاکنندگان نامه منتسب به «۲۵۰۰ پزشک» است که چند روز بعد از ممنوعیت واردات واکسن از سوی خامنه‌ای اعلام شد.
🔹
بررسی‌های فکت‌نامه
همان زمان توضیح داد که هم محتوای نامه بی‌پایه و اساس و تئوری توطئه است و هم نامه‌ای که به «۲۵۰۰ پزشک» منتسب شده کمتر از ۱۸۰ امضا با نام‌های تکراری و مخدوش دارد.
🔹
با این توضیحات فکت‌نامه به این ادعا نشان
«شاخ‌دار»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76970" target="_blank">📅 20:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=E7aVf6MmkrQAv0IZ0dQgCfMWmKMA2cGfLkITddRZqjuv0Vkjwhe3D6rtYRqgBLJsj7bHEWVWFOSk3CK49NVMqnsxUBnRFpupeSyE-MYL2ECEmWh0ePZ-Nz1JW8NneUsWzOVTTwUZvcNCSznuKWN7Bd29Q_zbrus1GhTeq8sTPI6M_ub0eoox-ru1FUVEFzEdmYtxhRxRkRkr7GpBpSMkay1ILKar7JXdlNbSh5mtBTovF4VkxatO71_6rTMT1hFKh0KAT1pqxQE4JCAkZ-Ufy_2wsPs3ripS8jNTGSeng6w4J4NGbfX8Gv5FHx5De4mVLexWz2x-YuVpculWMqXUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=E7aVf6MmkrQAv0IZ0dQgCfMWmKMA2cGfLkITddRZqjuv0Vkjwhe3D6rtYRqgBLJsj7bHEWVWFOSk3CK49NVMqnsxUBnRFpupeSyE-MYL2ECEmWh0ePZ-Nz1JW8NneUsWzOVTTwUZvcNCSznuKWN7Bd29Q_zbrus1GhTeq8sTPI6M_ub0eoox-ru1FUVEFzEdmYtxhRxRkRkr7GpBpSMkay1ILKar7JXdlNbSh5mtBTovF4VkxatO71_6rTMT1hFKh0KAT1pqxQE4JCAkZ-Ufy_2wsPs3ripS8jNTGSeng6w4J4NGbfX8Gv5FHx5De4mVLexWz2x-YuVpculWMqXUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت دفاع کویت شامگاه یک‌شنبه در بیانیه‌ای اعلام کرد که سه پاسگاه مرزی زمینی در شمال این کشور هدف یک حمله «خصمانه و جنایتکارانه» قرار گرفتند که در پی آن خساراتی به تاسیسات وارد شد.
وزارت دفاع کویت افزود همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت در آب‌های سرزمینی این کشور هدف یک پهپاد مهاجم قرار گرفت. این حمله خساراتی به بار آورد و یکی از کارکنان زخمی شد. این فرد در حال دریافت خدمات درمانی است.
ستاد کل ارتش کویت نیز تاکید کرد نیروهای مسلح این کشور همچنان در آمادگی کامل قرار دارند و همه تدابیر و اقدامات لازم را برای حفظ امنیت کشور و تمامیت ارضی آن اتخاذ کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76969" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcqWQsNFRyi7zjXDF0EfQTUoUiqbmHP9mys40un4O2unUDDt829czxDPEEwaG_m23LPWAdwm3s9TR-_gpaimcXJZy2WM6ldM7LcRM1Tf5lsNHnfo6z97tbq9wtVsFap3-k34pBBL1KZomtPZifz6m_xfMSmf87yq_gjRqZTJjf7K1tqfM60X5AYHY7Frcv7rqIpme66QoTBU2TQNHgoi3GuFTX8u6dnX8Qov3258bhxfKpnvSJzHoxR7XrTfAAOBEYqdGh3PimHGW7Up0w8_cITCphkdYPzBP5aQ930JSlH1xnYSNF9d71N0CuUXiLY1BhECdK3-cQ9BZYPEYi_GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی، یکشنبه‌شب ۲۱ تیرماه، به خبرنگار آکسیوس گفت ارتش ایالات متحده چند حمله را به سامانه‌های موشکی و پدافند هوایی ایران و همچنین قایق‌های تندرو سپاه پاسداران در چند مکان در اطراف تنگه هرمز انجام داده است.
حسین امیرتیموری، فرماندار قشم، تایید کرد یکشنبه شب حدود ۱۰ پرتابه به اهداف نظامی در این جزیره اصابت کرده است
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76968" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=le68eJXSknkdfTixHKGj2XBKb-YUZAW5PZoqEHpLrZffSAqJrhYCuioT_bheSlt9k1jpBQor-EcnIMASk6kaW7k54srzw1nt2HkN1WUUDBl0brQZVEU4RCXC4uDboKs2P8WZxCcEPnTrvZ09z7-98AAYM0JyRJl1R1Kgej28Yp8mN3P_ldfenY0Ns7Kq4oBxHaVC7n59qdWv7y6JmFACTVoA-9eP2s51pMVaRyITWZpX5n2eobWbsT_QyomanMbRBJVdEap3k22ZlnAGX9DT8i0rxkIs2MFu341U4vi5jwKc5HkUhlLiAf9E1CWyMLXfdFEDy1wutno4REEfW8fRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=le68eJXSknkdfTixHKGj2XBKb-YUZAW5PZoqEHpLrZffSAqJrhYCuioT_bheSlt9k1jpBQor-EcnIMASk6kaW7k54srzw1nt2HkN1WUUDBl0brQZVEU4RCXC4uDboKs2P8WZxCcEPnTrvZ09z7-98AAYM0JyRJl1R1Kgej28Yp8mN3P_ldfenY0Ns7Kq4oBxHaVC7n59qdWv7y6JmFACTVoA-9eP2s51pMVaRyITWZpX5n2eobWbsT_QyomanMbRBJVdEap3k22ZlnAGX9DT8i0rxkIs2MFu341U4vi5jwKc5HkUhlLiAf9E1CWyMLXfdFEDy1wutno4REEfW8fRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
همچنین اهالی منطقهٔ مسن در جنوب جزیرهٔ قشم نیز صدای چند انفجار را شنیده‌اند.
ماهیت انفجارها هنوز مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
پیش‌تر نیز برخی رسانه‌ها از وقوع انفجارهایی در کویت خبر داده بودند.
@
VahidOOnLine
🔄
ایرنا:
اصابت پرتابه در جزیزه قشم
🔹
فرماندار قشم از اصابت 10 تا 11 پرتابه دشمن از عصر امروز یکشنبه در جزیره قشم خبر داد.
🔹
حسین امیر تیموری در گفت و گو با ایرنا افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76967" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4ea69d634.mp4?token=CtyTTwbBOHDWrab7gEI_83ca2gH8hhGCP1TbUFJLpFRgPkf9mAlkGFNZtjaaWUheI_FrY-HZJSSvFLau_OuUI54GLQqHdgIOrLXeB-wiDSnxIy52iGQXPEnCcAvwQ8UVt-xPpVHP09Tte4EaeLrgtLp9nqk2lPVt96nfmCOmu8hZYsyrSDQjCj68Koo9kTQrowm6PrZ_iiIv1oQDfhRJUzGi2ObHO7ttPtehY9OHMUSvyd9sHVlI0j7vc-RntCWH_tvRluSgNqEN_KvffGl-jvn515LjfHZnHyQ_MA42GKXE3uPQ1owsJDo6g8XRAEDE9Vctq6lBI9l7gXUc1p9AZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4ea69d634.mp4?token=CtyTTwbBOHDWrab7gEI_83ca2gH8hhGCP1TbUFJLpFRgPkf9mAlkGFNZtjaaWUheI_FrY-HZJSSvFLau_OuUI54GLQqHdgIOrLXeB-wiDSnxIy52iGQXPEnCcAvwQ8UVt-xPpVHP09Tte4EaeLrgtLp9nqk2lPVt96nfmCOmu8hZYsyrSDQjCj68Koo9kTQrowm6PrZ_iiIv1oQDfhRJUzGi2ObHO7ttPtehY9OHMUSvyd9sHVlI0j7vc-RntCWH_tvRluSgNqEN_KvffGl-jvn515LjfHZnHyQ_MA42GKXE3uPQ1owsJDo6g8XRAEDE9Vctq6lBI9l7gXUc1p9AZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
شما آشکارا دور تازه‌ای از حملات را آغاز کردید؛ آن هم شبانه. ایران شب گذشته گفت تنگه هرمز بسته است. سنتکام صبح امروز اعلام کرد تنگه هرمز باز است. کدام درست است، آقای رئیس‌جمهور؟
ترامپ:
نمی‌خواهم درباره‌اش صحبت کنم، چون می‌خواهم به زندگی لیندسی گراهام ادای احترام کنم. بنابراین نمی‌خواهم درباره‌اش حرف بزنم. پیش از تماس هم این را به شما گفتم.
بله، تنگه باز است. دیشب حسابی بمبارانشان کردیم. آن‌ها آدم‌های بسیار، بسیار شرور و بیماری هستند.
تمام روز گذشته با آن‌ها جلسه داشتیم. دیروز با یک توافق عالی برای ما موافقت کردند: نه برنامه هسته‌ای، نه این و نه آن، هیچ‌چیز. از همه‌چیز دست کشیدند و بعد از آن اتاق را ترک کردند و سپس، ظرف یک ساعت، پهپادی به‌سوی یک کشتی پرتاب کردند.
گفتم: «شما بیمارید؛ آدم‌های بیماری هستید.»
بنابراین ماجرا از همین قرار است. نمی‌خواهم درباره‌اش صحبت کنم.  می‌خواهم امروز درباره یک نفر صحبت کنم: لیندسی گراهام.
NBC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76966" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc9b71e145.mp4?token=uJml2_uDthPiAB6ewkC9BdfDHpilGcDmf9KHn-5Sw871KjRaqeOqqdRbvKWcCe-H3CMjwge2MtKDM2G3MeL-I4bAiDjR5odJ-zS7oYb-zilZI7IpxjVNhhoUNiOZ-8BT2cdvgjx8I8PskvIW8owX-d1_lTepbnQ8vD1pxIaj4ZPSJq7_9Um0oR3BckyU-ZD16AH_Hh9wkcPxZbjz8mqPWzS8763jH4KyaddRj3Y2JOYPiYLPDwMYc4_GlCkH52Xaf7dDJm7Bl4l63nmr-EZ9wVd33OQ-N1jGN7ICdNQq6lYk3vWE4b4fNYI6blj-qoZQXy-W2QTB9saH7A0jkEbgDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc9b71e145.mp4?token=uJml2_uDthPiAB6ewkC9BdfDHpilGcDmf9KHn-5Sw871KjRaqeOqqdRbvKWcCe-H3CMjwge2MtKDM2G3MeL-I4bAiDjR5odJ-zS7oYb-zilZI7IpxjVNhhoUNiOZ-8BT2cdvgjx8I8PskvIW8owX-d1_lTepbnQ8vD1pxIaj4ZPSJq7_9Um0oR3BckyU-ZD16AH_Hh9wkcPxZbjz8mqPWzS8763jH4KyaddRj3Y2JOYPiYLPDwMYc4_GlCkH52Xaf7dDJm7Bl4l63nmr-EZ9wVd33OQ-N1jGN7ICdNQq6lYk3vWE4b4fNYI6blj-qoZQXy-W2QTB9saH7A0jkEbgDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
مجری:
ایران اعلام کرده تنگه هرمز را بسته است. آیا این درست است، آقای رئیس‌جمهور؟
دونالد ترامپ:
تا جایی که به ما مربوط است، باز است. درباره‌اش صحبت نکن. درباره موضوعی صحبت کن که به خاطرش از من خواستی حرف بزنم.
مجری:
باشه. از وقتی که در اختیار ما گذاشتید ممنونیم، قربان. پیش از اینکه اجازه بدهم بروید، آیا حرف پایانی دیگری هست که می‌خواهید مردم آمریکا درباره لیندسی گراهام بدانند؟
ترامپ:
نه، فکر می‌کنم بهترین لحظه‌اش دفاع او از برت کاوانا بود؛ مرد فوق‌العاده‌ای که دموکرات‌ها با او بسیار، بسیار ناعادلانه رفتار کردند.
هرگز چیزی شبیه آن ندیده‌ام. شاید بدترین رفتاری بود که تا به حال با کسی دیده‌ام. من را هم شامل می‌شود. البته، شاید نه من، اما تقریباً همه را شامل می‌شود.
با او به‌شدت ناعادلانه رفتار شد و لیندسی، همان‌طور که یادت هست، آن لحظه را رقم زد. و می‌دانی، باید به تو بگویم، جیک، فکر می‌کنم یکی از ده لحظه برتر، شاید یکی از پنج لحظه برتر تاریخ سنا بود.
نمایشی باورنکردنی بود. و آن را از ته دل انجام داد. نسبت به برت احساس عمیقی داشت و آن را از ته دل انجام داد و کل ماجرا را برگرداند.
واقعاً شگفت‌انگیز بود. آن یکی را باید دوباره پخش کنند.
مجری:
خب، می‌دانم که از روی احترام به لیندسی گراهام نمی‌خواهید درباره هیچ موضوع دیگری صحبت کنید، اما ما دوست داریم زمانی دوباره شما را داشته باشیم، چون واقعاً پرسش‌های بسیار دیگری از شما دارم، قربان.
ترامپ:
حتماً. این کار را می‌کنیم. این کار را می‌کنیم.
مجری:
از اینکه تلفنی با ما همراه شدید متشکرم.
ترامپ:
می‌خواهیم CNN را در مسیری عادی قرار دهیم و این کار را خواهیم کرد.
مجری:
خب، من همین‌جا در مسیر عادی هستم، قربان، و از وقتی که در اختیار ما گذاشتید سپاسگزارم و ممنون که تماس گرفتید.
ترامپ:
باشه. خیلی ممنون.
مجری:
بسیار متشکرم. بعد از این وقفه کوتاه برمی‌گردیم.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76965" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCMOH1xOx0VyDpvcpBUtOgUO4wSXkar9RKhxyTg5rkfGGTKbFPVszVqbqtbMRoIyjqzgKianrFIiJucJPcgXKsLqfF7CWba_1CGhdClMVpiF5NmfwbbpkFw6XcqyyfUOOr0FsPstM-sSACzveaEdHIT5f2Fck_ojdf8JCaKlPfdXsWnee3Qb4XBfArdVzaaiLrMnj04mHZuqsO3GjdNp_ceolzKgFtVGuFZ4krQRlZVrrRQVThNrOzRWi81Gd1hbPUGBELJngc9rl0n-WhYvs71d2sxbsGMPAz-7_eL81w6pKtKtD_7n4ddcZdXNS592lsUvvKTM1CrQguJx0yxvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس، نهادی که به‌تازگی برای اعمال مدیریت جمهوری اسلامی ایران بر تنگه هرمز تاسیس شده است، یکشنبه ۲۱ تیرماه با انتشار بیانیه‌ای اعلام کرد تردد از این آبراه در حال حاضر امکان‌پذیر نیست.
در این بیانیه، آنچه «تحرکات غیرقانونی اخیر نیروهای نظامی ایالات متحده در منطقه» خوانده شد، علت توقف تردد عنوان شده است. این نهاد افزود پس از برقراری ثبات و آرامش، درخواست‌ها بر اساس زمان ثبت بررسی و مجوزهای لازم صادر خواهد شد.
@
VahidOOnLine
پست سنتکام، ترجمه ماشین:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه دولتی گفته است هیچ شناور خارجی‌ای نمی‌تواند بدون شناسایی، ردیابی و نظارت نیروهای ایرانی از تنگه هرمز عبور کند.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این تنگه همچنان یک آبراه بین‌المللی است. نیروهای ایالات متحده مستقر و آماده‌اند تا همین وضعیت را حفظ کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76964" target="_blank">📅 17:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBkxOR8ph4m-5WSjTzk1B6nPhqk5TCb_r7M3Lmaogk41zayUQbumDE7C00WdF4BnWHos5FOG6LG8cGDn7jtBS8Eke4ysFH2-S0nam-QF9Nz1MWHxXtiLreTJBAnanDnbY8WkZdacHeElNAzXX4cl-9wMkTxJiJZAzPhbnYiVli_7tcFyWXpyd_kWkUEm-PmuC7gc2hDGsy9cGPG0DptGXrLkzft_-xMSLlq6shrH3An1mvF5EMcrNctEaAH_h6KLBDbJCl0xDLEMAGbO2hk2QMdQvOsHmaO8v8ZqMo8y9RC-C69p31TPUAmeMbsN4Hd0_gksFCyCiswpU-pvrOyVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی نظامی آمریکا، ترجمه ماشین:
تنگه هرمز به روی همه شناورهایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای ایالات متحده مستقر و آماده‌اند تا اطمینان حاصل کنند که آزادی کشتیرانی، با وجود تجاوزگری بی‌دلیل، آزار و اذیت، تهدیدها و اعلامیه‌های خودسرانه ایران، همچنان برقرار می‌ماند. ایران کنترل تنگه را در دست ندارد. تردد در جریان است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76963" target="_blank">📅 15:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ak1XfI999Hv9d5stxhwyNQWdV0sK_Z7ICpJm72KjFpN6ucV8FQJRVDvEtJkOrJU0mSmTPYJ4rvAIjQnVRI3zCCeUgB_Y9kiADk6_MErkQu9mrWJ10W1i559RWkquf3T4wbE06JaUmjrxRAP4TGRY2FPdKznUdCBHsm1T2oQqFUPmXTjlpCi3t35cHVSX9-H-0_59Q49UTqdaW0X125mLPLT0aiqAC0iG1CVBJFPtPXdEr8Y0Cw6Il6THEUVbk5FU7imihCXlRia9YvSzn5uBHtDzQptaxSDr4sxmC66_7VoFRaq7e7IE9mVwBFaZHNd0461YwySxdeQI25Hokgir9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vP4D_g9uHo6ewkhTx3gqSRWm-7ZlQqhuyeK9X1ZhjpY9bqGoFhcK7iXgCCO_1R3KWAW7QxeQO7c6N65JrDpN5h8g59G965DBJa0q7QDMJW8a0oVzRmsG_-Ng-2RHa6p8WaqXqfU8V82LzvJtoP_5DqxfvfSOhgCtYd51lxH6gwhKG1VC7lhSzMOAXm4-JskWElFhjS33Z37mk8pnZaRI8cROW9MDF6LrhK2_7Ay9UfCrgkz503DnKrqa7BlL9TySZLoSeyzGCxcA2ksw-KyBUgMOSnUqOd7qFUilfAXT9TipspTgmXQckMsU3ZJyN0Ry53paAzB6HwJHhQdpCRG6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GHyLIBAtlrNNA7xvCF3NCO8xOiwqAUAOoGmfw2p1OtKRAOcO4xOIiv1SRHCyNM_Hatvnkd6PyhLshDDCsq6T5gsWwgUINVU4hwl8wg-WQpsVE5xjLNmq7PWmNlTfoZ4lBzY9dLsIVQ7V77INI9sthvmlIb2R1EThporfq9njrPCt7pdH5YWLwkUYOoTCB4PmQ6Wkftzr02xxpJaNYNgH1acMFv6bOKf-uzN5hHtAgYVlV3t-JeC06Bsgx9mFrXH3kycaVU0jY2rUdCMa5rAuNbum4fpzeU3YhOW9b7akgFromi_fqRCfrQ7BkkiVT8AKg4HLcGRzHHYbdHP_ouPNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HcGBkHM6x_CNnXFyjERb62ZHDEODcnTGQJ9LAgQqT9nMLlgDJogzmJCpLyN7bQ0sQpL6OvcCo5NLrjOF1tXI9IWLwESRPTKSfJ-GpRh5xqo-bTBNZ2IWfYPMYpVmByxB71IvUCX2nd9ZUZiH6hK7FXctI4Tv98BeR0Bc5XyUY5MmJV-JNvTUGEDrYEEGgrtJJwnCOku9cKyS3u4xTNATESAjhJAa1q_3a12Hc-cnBjQajHqcDtQvXwNubrMuMPnLsqFKWuseGrDvpEZ_MdmXXfYInsr8dYW9hvOionEdtVVGYZOL8XuGEjYHMcJYCoaLOdTu3raQlZt55jR6zx7DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CI7SDOPuh30YQBk5PViz_Pswgp5nzLI9UTpe4rIM6RObtLbPlROnsz4as1D2y3p6UmnPPb09Vm2ml5J4_y4DiGG_-WNEngMsGwZ9TCCQ86TyhaidNxyUIDT8baGMXsqecgkfBYS4kZM-1dWVQgzGvSb_mPLEe3vRlZ9jfqdBFwU4R05yEaufkoy836HopGJdFbyANhavjusDW-jbmIz_9d3dnZItUBaFvhUF3Zqumxeb53Ducbq7IqJyK9srUjgbiZwGZIMONgoHrWgD9hlDHW3lLAzdEZYod8BUg_FMqYfUw0PEWrNE2bI7YTk03vLcqsn3CWe8pPAALRrNi02gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XDmeWeYU-V8-qAgdaP5g_TgQ7T7sbsKQxouFTaiJDrRfZO3EDVmcCUm44SE7reA5WEFQ3wcRLiVnHyWoHGsARvNGsJxYpI_dbjXmsgoJM2KSItrTXgWLI8B7FJHUxYJwcHmpKps9wzNiz1JnLyV9n5b2gkMlZlC2Bv3gjWktoy-1pgFbNFhZ9-ryxPJ5WEVSWxsqNsGvDpg7-7NuYX9l5BKZjzsAi5TKUsC7ZdAGQpK5BuBJuy10h3Ms1eGUXhDUoAtU1hENz6c-8kXFYAEMiiTmOdPxCIfmLfN0van_YKFkeL8w3GHASF7YfhNMCpWRZEn0G4illdDK1MxKC2vo_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51caf6abe5.mp4?token=PbTtp2bLTaUtq87aysZ79V0vFEaKaPbAnYh6GecEag_5JeXbZvX5Eu3-6whz2Y3NNoyyxqmiVBf4QrODt-KiJwzBmwxqhj19BhEKySVEdbsIyKTp2OKDn_sVjyghZsZc3jG4-Ayok2Esm-lCBtBtGbNgZgQ7mXgMLrGQp-nT_hrbWmXjtMEj6IPICftIXakWRoy9LwGpyok9MYyMOrdSTxlay0eTdcrxz-UZyV3khZiNbNjB6WMJMr17aeROPbaRR4QFBRsGCQm95r5Z7WV-OatjjuVvZYkfY1l7DPlqFcgHWnyMDKXABe0g8HiGZNTDFpKgcMxdONTpl7gnlhIuew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51caf6abe5.mp4?token=PbTtp2bLTaUtq87aysZ79V0vFEaKaPbAnYh6GecEag_5JeXbZvX5Eu3-6whz2Y3NNoyyxqmiVBf4QrODt-KiJwzBmwxqhj19BhEKySVEdbsIyKTp2OKDn_sVjyghZsZc3jG4-Ayok2Esm-lCBtBtGbNgZgQ7mXgMLrGQp-nT_hrbWmXjtMEj6IPICftIXakWRoy9LwGpyok9MYyMOrdSTxlay0eTdcrxz-UZyV3khZiNbNjB6WMJMr17aeROPbaRR4QFBRsGCQm95r5Z7WV-OatjjuVvZYkfY1l7DPlqFcgHWnyMDKXABe0g8HiGZNTDFpKgcMxdONTpl7gnlhIuew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران و ارتش جمهوری اسلامی بامداد یک‌شنبه ۲۱ تیر۱۴۰۵، از گسترش دامنه حملات خود به پایگاه‌ها و تاسیسات نظامی آمریکا در منطقه خبر دادند و مدعی شدند هم‌زمان اهدافی در عمان، قطر، اردن، کویت و بحرین را هدف قرار داده‌اند.
هم‌زمان گزارش‌هایی از فعال شدن سامانه‌های پدافندی، به صدا درآمدن آژیر های خطر و شنیده شدن صدای انفجار در چند کشور منطقه منتشر شد.
این حملات در حالی رخ داده که عمان و قطر طی هفته‌های گذشته نقش اصلی میانجی‌گری میان جمهوری اسلامی و آمریکا را بر عهده داشته‌اند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، یک روز پیش از این حملات در مسقط با بدر البو سعیدی، وزیر خارجه عمان، درباره کاهش تنش‌ها و سازوکار عبور امن کشتی‌ها از تنگه هرمز گفت‌وگو کرده بود. عمان همچنین پیشنهادهایی برای حفظ امنیت کشتیرانی و اجرای تفاهم‌های مربوط به تنگه هرمز ارائه داده بود.
قطر نیز در کنار پاکستان از میانجی‌های اصلی گفت‌وگوهای تهران و واشنگتن در چارچوب تفاهم‌نامه اسلام‌آباد محسوب می‌شود. با این حال، سپاه پاسداران هم‌زمان با تأکید مقام‌های جمهوری اسلامی بر ادامه مسیر دیپلماسی، بار دیگر مدعی حمله به پایگاه العدید در قطر شد و اکنون نیز از حمله به اهدافی در خاک دو کشور میانجی، عمان و قطر، خبر داده است.
@
VahidHeadline
فرماندار درود در استان لرستان روز یکشنبه ۲۱ تیرماه از برخورد بوستر (پیشران) یک موشک به یک منزل مسکونی در محله بلوار تختی این شهر خبر داد.
به گفته این مقام محلی یک واحد مسکونی و پارکینگ بر اثر این اصابت دچار خسارت شدند اما کسی بر اثر این سانحه کشته یا مجروح نشده است.
@
VahidOOnLine
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۲۱ تیرماه با انتشار پیامی در شبکه اجتماعی ایکس، درگذشت شیخ حمد بن خلیفه آل ثانی، امیر پیشین قطر، را تسلیت گفت.
عراقچی در این پیام به زبان عربی نوشت: « صمیمانه‌ترین مراتب تسلیت و همدردی خود را به امیر شیخ تمیم بن حمد آل ثانی، خاندان ارجمند آل ثانی و ملت برادر قطر ابراز می‌داریم.»
این پیام عراقچی در حالی منتشر می‌شود که بامداد روز یکشنبه، نیروهای مسلح جمهوری اسلامی، مناطقی در قطر را هدف حملات موشکی و پهپادی قرار داده بودند.
قطر یکی از میانجی‌گران کلیدی در جریان مذاکرات جمهوری اسلامی ایران با آمریکا به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76956" target="_blank">📅 15:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NsASC61Yfe-PotkH8Rq83ThuhtgnsxhS_2MH_7UG4xLkHDafNP-zmq0gxd_SojrYpahodcwJIJT13_yY_rbXQXPuQwQRjcnzSC3N3_TA1q1qO_nvUKQuYJH0ciZ8XJsuy171T64R_xPRsk__Yv1s5s3Ry4kwKjh47SF6ldcD1xauA0fgu5tiroglv09uac3hWuQnjrvLAkanHCXsmNqJGl251NLIbh6Stv35j-exG67okQYRmzXXth4lZg9N0eyH8LWLqJEX1Qw5A0eweVXIILdS_KVJP_IWgJpHgqMEI_4wH7GCwakD3F1hsHr9OQFxX6pn_f4IsC5nYxVXss3lDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYnRo0ZfgLlVvpo6-QG-xn-uij5T1DF2eWunt3nlFO94-MvbiwLKIEOJfGFUyv-JZOy8pvRDchJ4Z6iB0rloVv4fXJU_mt0rvuoENDoZFkcMhHypPWvF9_Vjhvv5i7CkviAorzDJl8N3f_Hgs-9T0ycxQSVEfSduCxc1Ek9L_wkaTn6bPWLgJ7d_idPpUzJ0Jr0SRFXVNEGS-UNdcpZkfL4FKJbZ4GBfGFn_bwvVp-9MVgRGyNkODfEDncFSSaml8YZdxBcRheJrHJVMWLLamhdNAx5MDx7HnRIxKS6sM2-Oimmj1ZC34YhmrgBSsvjUFXXIRI8p7jYqXX6riismAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون امنیتی و انتظامی استاندار کرمان روز یکشنبه ۲۱ تیر اعلام کرد ارتش آمریکا یک دکل ارتباطی در ارتفاعات جنوب این استان را هدف قرار داده است.
به گزارش خبرگزاری مهر، بر اثر این حمله دو نفر مجروج و با هلی‌کوپتر به مراکز درمانی منتقل شدند.
@
VahidOOnLine
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان، اعلام کرد شهر ویسیان از توابع شهرستان چگنی در استان لرستان، صبح یکشنبه ۲۱ تیرماه، دو بار هدف حمله هوایی قرار گرفته است.
سعید پورعلی گفت این حمله تلفات جانی نداشته و شرایط در این شهر هم‌اکنون عادی است.
پیشتر و در پی حملات نیروهای آمریکایی به استان‌های جنوبی ایران، معاون امنیتی استانداری خوزستان، از اصابت «پرتابه‌های دشمن» به مناطقی در شهرستان‌های هندیجان، ماهشهر و آبادان خبر داده بود.
شنیده شدن صدای انفجارهایی در بوشهر، بندرعباس، سیریک، عسلویه، کنگان و بندر نیز از گزارش‌های مربوط به تحرکات جنگی بامداد یکشنبه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76954" target="_blank">📅 15:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CetLlqouxqHkrxTwPwjhQA3ObfzxQjb3eCx5NgWZMD2Ps5Rw_VAbD2lUanfItGfF9z8MU1Ti6lh0CYvWFIvtZ5paQBhwnPeX_WvuWQqDuk62Zu1v1WDD-30Bwe4OzxhL20LQQAb89euU6O7HVJ69ooDpBoAaibO_AqE2yWP65I4JkJ3jtcdXg6rliYDryzP9pvMySMq-5RcDoPUg_ZFI6O7Ur5DlMECjZXsuH2R9L7h04zZImZ65nd0_I9-r4V9HtpqzJJqHxebPo6Sn75NScum41wDSkiJuajFP96uZVSeDyn57leTSbr7719kOpxy8FK-Ep2gQgztzCQA5BYlu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیندسی گراهام، سناتور ارشد جمهوری‌خواه ایالت کارولینای جنوبی و از نزدیک‌ترین متحدان دونالد ترامپ، شامگاه شنبه ۲۰ تیر۱۴۰۵، در ۷۱ سالگی پس از یک دوره کوتاه بیماری درگذشت.
دفتر این سناتور با انتشار بیانیه‌ای اعلام کرد که گراهام شامگاه شنبه در گذشته و خانواده او از مردم خواسته‌اند در این دوران دشوار، ضمن دعا برای آنان، حریم خصوصی‌شان را نیز رعایت کنند.
گراهام یکی از شناخته‌شده‌ترین چهره‌های جریان محافظه‌کار آمریکا و از اعضای باسابقه مجلس سنای این کشور بود.
او طی سال‌های گذشته به‌ویژه در حوزه سیاست خارجی، از نزدیک‌ترین هم‌پیمانان دونالد ترامپ محسوب می‌شد و مواضعی تند علیه جمهوری اسلامی اتخاذ می‌کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76953" target="_blank">📅 15:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eWzM-yEqPmgIUs1U-GTv_M0nxYy6rRP5SclDOib09NWTp902gmXchtewrLI-X-GdCRhTZ18IHVophsHeq9LFMOAQcg4GXYcr0vUiOS_8BHTf-APweEQrKO0DODq6EpJtpTt0JjZ9PEXfduMvuyfw5XD9w2BwrM14RezBzhMnlOiDmETnEhETOWgOQDSykTiD8riLl1pM1dkhF_iMadaGKzPmR2JJqY083na8xIt9WUjVRg5uruw3f1tWDesOvWZK3b13PW3tH_wYFl4zsGXyuHwXJQNqD2pTNvZq3TuvH-L05X09Ku0zU2zZqO-3tJcfg32ajlxcXqt3QQ9buiMjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۱۲ حکم اعدام در پرونده "میدان علیخانی اصفهان" به مرحله اجرای احکام رسید
🔹️
بر اساس گزارش‌های منتشرشده و اطلاعاتی که به کمیته رسید، پرونده موسوم به «میدان علیخانی اصفهان» وارد مرحله اجرای احکام شده و جان ۱۲ زندانی در معرض خطر جدی اجرای حکم اعدام قرار دارد. گزارش‌ها حاکی از آن است که احکام پس از تأیید در دیوان عالی کشور در روز ۱۴ تیر، به اجرای احکام دادگاه انقلاب اصفهان ارسال شده‌اند.
🔹️
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان، بازمی‌گردد؛ جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند. در پی این رخداد، ۵۹ نفر بازداشت شدند و برای آنان پرونده‌ای گسترده تشکیل شد.
🔹️
بر اساس اطلاعات منتشرشده، رسیدگی به این پرونده در شعبه اول دادگاه انقلاب اصفهان به ریاست محمد براتی درچه و محمد توکلی (معروف به وکیلی، از قضات پرونده «خانه اصفهان») انجام شده و دادستان پرونده محمد نخجوان بوده است. همچنین گزارش شده که کل روند دادرسی تنها در سه جلسه یک‌ساعته برگزار شده است؛ موضوعی که نگرانی‌های جدی درباره رعایت اصول دادرسی عادلانه را افزایش داده است.
در میان ۵۹ متهم این پرونده، ۲۳ نفر با وجود تبرئه از برخی اتهامات، همچنان به احکام ۵ تا ۱۰ سال زندان محکوم شده‌اند.
🔹️
در مقابل، ۱۲ نفر با حکم اعدام روبه‌رو شده‌اند که در میان آنان چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود.
اسامی محکومان به اعدام عبارت‌اند از:
علیرضا سپاهی (متولد ۱۳۸۰) – محکوم به چهار بار اعدام
ابوالفضل سپاهی (متولد ۱۳۸۲) – محکوم به سه بار اعدام
علیرضا رئیسی (متولد ۱۳۸۳) – محکوم به دو بار اعدام
قائم حسینی (متولد ۱۳۸۴) – محکوم به دو بار اعدام
گل‌محمد محمدی (متولد ۱۳۸۱)، شهروند افغانستان که بنا بر گزارش‌ها به معترضان پناه داده بود – محکوم به دو بار اعدام
امیرحسین صفری (متولد ۱۳۷۷) – محکوم به اعدام
امیرحسین ملکی (متولد ۱۳۸۵) – محکوم به اعدام
علی دشتی (متولد ۱۳۸۵) – محکوم به اعدام
امیرحسین ابراهیمی انالوجه (متولد ۱۳۸۵) – محکوم به اعدام
شروین باقریان (متولد ۱۳۸۶) – محکوم به اعدام
عرفان اسفندیاری (متولد ۱۳۸۶) – محکوم به اعدام
ابوالفضل ابراهیمی (متولد ۱۳۸۶) – محکوم به اعدام
🔹️
همزمان، گزارش‌ها یادآوری می‌کنند که در روزهای ۱۸ و ۱۹ دی‌ماه در همین محدوده، شماری از شهروندان اصفهان در جریان اعتراضات با شلیک مستقیم نیروهای حکومتی جان خود را از دست دادند.
🔹️
نام محمد توکلی نیز در این پرونده بار دیگر مطرح شده است؛ قاضی‌ای که پیش‌تر در پرونده «خانه اصفهان» نیز حضور داشت؛ پرونده‌ای که به اعدام مجید کاظمی، صالح میرهاشمی و سعید یعقوبی انجامید و همچنان از پرونده‌های بحث‌برانگیز سال‌های اخیر به شمار می‌رود.
🔹️
با توجه به گزارش‌های منتشرشده درباره تأیید احکام در دیوان عالی کشور و ارسال پرونده به اجرای احکام، نگرانی‌ها نسبت به احتمال اجرای قریب‌الوقوع این احکام افزایش یافته است.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76952" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=baTW-dAWusqx2Ld88IM4gnnlxcPJaS00TSUNsrcZQcX5FXuFkdJbswPGEPAaEc0ReYI6SI8XxlW5Di4SRVF1P50YbShfo_kPWVecgLhXhdxdXE1yACOUkQjSVXysMc15CyDPK-nu3w2fO5YT7nsgv6dvG445JBZfWKtnT5giRCR3fHMJbjvEM1OJLSX8DODV6_O6y_q5K-RPXOct3mKs9RfoM7fzDCX3xDPiS9L0ncd3hse0_hYinaKmneKk1B1F0HlyZkpJe-ETOIC3ziXZXbFhnP0kQ3mcdT1YdcHxzIK98d6prn7cshp07TtKlpE8WPuwvJx4tZlPM1g3NnslUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=baTW-dAWusqx2Ld88IM4gnnlxcPJaS00TSUNsrcZQcX5FXuFkdJbswPGEPAaEc0ReYI6SI8XxlW5Di4SRVF1P50YbShfo_kPWVecgLhXhdxdXE1yACOUkQjSVXysMc15CyDPK-nu3w2fO5YT7nsgv6dvG445JBZfWKtnT5giRCR3fHMJbjvEM1OJLSX8DODV6_O6y_q5K-RPXOct3mKs9RfoM7fzDCX3xDPiS9L0ncd3hse0_hYinaKmneKk1B1F0HlyZkpJe-ETOIC3ziXZXbFhnP0kQ3mcdT1YdcHxzIK98d6prn7cshp07TtKlpE8WPuwvJx4tZlPM1g3NnslUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام:‌ حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) روز ۱۱ ژوئیه سومین دور حملات این هفته علیه ایران را به پایان رساند تا نیروهای ایرانی را بابت حمله به یک کشتی تجاری دیگر در تنگه هرمز پاسخ‌گو کند.
نیروهای آمریکایی با استفاده از مهمات نقطه‌زن شلیک‌شده از جنگنده‌های مستقر در خشکی و دریا، پهپادها و شناورهای نیروی دریایی، حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادند. این اهداف شامل سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی، تأسیسات ذخیره مهمات، شبکه‌های ارتباطی و مراکز پایش ساحلی بود.
سنتکام طی سه شب حملات این هفته، به دستور فرمانده کل قوا بیش از ۳۰۰ هدف را مورد اصابت قرار داده است تا توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تضعیف شود. عبور کشتی‌های تجاری از این کریدور حیاتی دریایی بین‌المللی همچنان ادامه دارد.
از اوایل ماه مه تاکنون، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۴۰۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند.
CENTCOM
منابع حکومتی:
دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز تعمیرات و نگهداری جنگنده‌ها و مرکز فرماندهی و کنترل  ین پایگاه در هم کوبیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی اعلام کرد:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
🔹
در پاسخ به ادامه تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگه هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحله دوم عملیات مقابله به مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های و مرکز فرماندهی این پایگاه در هم کوبیده شد.
🔹
دشمن امریکایی - صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت.
بجنگ تا بجنگیم.
روابط عمومی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/76951" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dnOmRQ9QsdsuexiuNBFGd7N6FSgf3a7Nbec1ioz-qZ1hRgvfAIfe7_GYga4NhGo_yJfQb5KJJF4Uq7Azwm6jccixdr-liVvhQz58nYzx2TdQ7uKSWbHNPPxfpcGPooQ9QOF461BDbMWk8RnXuXjn4exJaE9i0gk3JokahyBIttuTnS6-Y2dePVyZfcZM5N4vEojEVHOlOlVrHpWk3HUo_VaxfmOGQKLY4aEZUBm9-DaY9kQjcjzyJtEGbooN_0TmBFdTTIVXBDAm39GAONKrRUJVOr1kA4vWt7FXvvbra5shgw7Qqc6fLgTer6R0x35jaN-KuHCA06upnFM6ijY6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از شاهدان عینی، خبر از شنیده شدن صدای انفجار در دوحه، پایتخت قطر خبر داد.
پیش از این، وزارت کشور امارات متحده عربی با انتشار هشداری فوری، صبح شنبه، اعلام کرد که سیستم‌های پدافند هوایی این کشور در حال حاضر در حال مقابله با یک «تهدید موشکی» هستند.
همزمان وزارت کشور بحرین نیز اعلام کرد که آژیرهای خطر در این کشور، صبح یکشنبه، به صدا درآمده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76949" target="_blank">📅 06:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=iqTWp5PiUlC2FlruiZhjaNoFtqLsNp98Uih7Xd5RPSFCHR0fToFyyifkCDtuyLX1nv-wT5WQEBpB-6WvzcWMLYbtAdrKeFTHbbSDYcHwVkWcgN34W3ZuAdDEqOgC61rk8Clplgm31q8UWcBppFv8K0BDgkdxnLNzlKDmLRap6XcshhabMoj9zknopG6kgbStNV5kNV8-E2afLkrrGrZymCiEpfUj-7NoHpOPFHVpgIlnxE8fEHba85RtyMmfJtEVMnO43OP9xWzCP1cB8ZUpDBTP9F9azZCF7SsWduCJTm9q30NfmXLC5UmbvF9hE-Os2dFye6PiQxeEW4931xOR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=iqTWp5PiUlC2FlruiZhjaNoFtqLsNp98Uih7Xd5RPSFCHR0fToFyyifkCDtuyLX1nv-wT5WQEBpB-6WvzcWMLYbtAdrKeFTHbbSDYcHwVkWcgN34W3ZuAdDEqOgC61rk8Clplgm31q8UWcBppFv8K0BDgkdxnLNzlKDmLRap6XcshhabMoj9zknopG6kgbStNV5kNV8-E2afLkrrGrZymCiEpfUj-7NoHpOPFHVpgIlnxE8fEHba85RtyMmfJtEVMnO43OP9xWzCP1cB8ZUpDBTP9F9azZCF7SsWduCJTm9q30NfmXLC5UmbvF9hE-Os2dFye6PiQxeEW4931xOR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی (به همراه تصاویر مختلفی از رد دو موشک):
همین الان از خمین دوتا موشک شلیک شد
درود وحید جان همین الان از خمین دو تا موشک شلیک شد
سلام،،ساعت ۵ نی دوتا موشک از الیگودرز شلیک شد
زنجان
۲۱ تیر ۱۴۰۵ ساعت ۵:۳۲
صدای بلند و ممتدی هم اومد برای چند ثانیه
وحید این دفعه هم از سمت خمین و الیگودرز شلیک کردن صداش زیاد بود ولی ۲ تا رد موشک بیشتر نمیبینم.
شلیک موشک از خمین
درود وحید جان از حدود زنجان موشک بلند شد دوتا
🔄
شهرستان داراب استان فارس ساعت ۶ شلیک ۲ موشک
یه موشک از داراب فارس بلند شد رفت ساعت 6:05 دقیقه
همزمان:
آژیر در بحرین
sirens in bahrain
5 دقیقه پیش قطر صدای پدافند اومد و آلارم روی گوشیا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76947" target="_blank">📅 05:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JnDNlkbkybiDAujkGUwlk8s-Ab7Ftqu3JLh1u3ZpujZy8uTYMpQssx7vGsuaZVp1wdiA22V_tpiv8ka1oSaB0zDRXUMEbaJVZzpKLgz8SaTOdytNMk1mlavPU-uHJ02QRf2VQFepCsF3QgVtEAiotTva8NQksUt9wk6s3badfjhjobf6tbPM4cWLvB3mw9GZjbYMwmZujHPiy6s8fg9khXSv9NG8MQloHiV8Kk9f8EMlw_UU7Jv9YGEF-5ZL__naHGpBPb2dxSPqQXb_KPoLN7Nf5f_6TeNR-bPZ8rsX15a9AiUWY5SsVtvG1LxTfBFsPpAuLr3TNUyUfBA7NWYKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی استانداری خوزستان گفته است که شهرستان‌های هندیجان، ماهشهر و آبادان هدف پرتابه‌هایی قرار گرفته‌اند.
هنوز جزئیاتی درباره محل دقیق اصابت، خسارات و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76946" target="_blank">📅 05:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YfTAJ17iDaYEiVz9QRPxTiw4JLQGPCmmrGOMDkcF4JWsz_Udj52zLd1rlpphis9XiEJNnxLhchYH_eq8RFR6OWevqIquLdONHYpaYnJiZi1fp-eqFpgkFZBIlBAK7A9k-3Dz4A59m-lLOIKqVTy8VIrsZr-dPI-IdsSCiqViveWYxR7_cS4UDMPDZWxPD-T5XJcKcRrxdw7V9P71xbMKJXRYCSrFSEaz6uv_TLvLKcGXYbJcHEa27XLt9kMIiWV6XbP4N7mo3k_FP2j8I1DsbxJBoEy5eYLzLZR27UDsULpK6eDJ9mllqd2XbA-0VOvFG2V5LSOX1utf-Icdr2KmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر و پیام‌های دریافتی تایید نشده:
سلام باز بوشهرو زدن ۳:۴۶
سلام وحید جان بوشهر سمت سرتل رادار زدن
بوشهر همین الان 3:48 دقیقه دو بار لرزید
سلام وحید جان ۳:۴۷ دقیقه بوشهر سه تا انفجار شدید شنیدیم
اقای وحید ساعت ۳ وربع صدای انفجار شدید اومد عسلویه از خواب پریدم
صدای دوتا انفجار  الان اومد  پایگاه هوایی بوشهر
۵ تا زد سایت موشکی چغادک-بوشهر،۰۳:۴۵
سلام وحید جان
ساعت 03:47
بوشهر سه چاربار صدای انفجار اومد
سلام وحید جان الان 3:45 دقیقه بهمنی بوشهر صدا اومد دو سه تا که خونه لرزید
🔄
جاسک
وحید ۳:۵۰ جاسک رو زد ۳ بار
سلام وحید جان همین الان دو انفجار وحشتناک در جاسک
منطقه نیرو دریایی جاسک
3:50 صدای جنگنده و چندین انفجار از بندر جاسک
سلام وحید صدای چند انفجار شدید در بندر جاسک
🔄
جاسک
خدایا بازم داره میزنه
دوتا دقیقا همون نقطه قبلی زد
ساعت ۵ جاسک
۲ انفجار دیگه جاسک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76945" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dIzpjJoqy_IeagPeQOSH8yeHs77CK1_bBb1Z_ESV22XdW4IY0NU6BKQTF4T_n1gHc5TccTSQiQcKAQwLn4-G7Kmf_GdJS7Kc6JKcunzXBsK8V0VIMKIfRgg2m_iix7v7KVC4LU3i7D-OMDT4_ObsHE1qsW11Vnrx7aCLwxOs5wTo8fXHNc68JNXdFPiJFbHmk3FJE873Zbh3ZgRrI44gb587wDk9NO0pi6tPKiuttGgG_fDhuUnBgSf27cEPU7WPJXENAnq6CXPJZ1gMpnsj2YkOBj7ulFiUqLOIqxo5OzlIdhekB0TJzkemPkX-GsDE6NLcvtTk6JQmrBhqpmE-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا:
"ایران انتخاب بدی کرد. حالا تاوانش را می‌دهد."
PeteHegseth
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76944" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌‌های دریافتی:
دوتا سنگین زد کنارک همین الان  ۳:۱۸
چابهار الان دو دفعه صدای انفجار اومد
سلام وحید جان چابهار همین الان دو تا انفجار مهیب
ساعت ۳:۱۸ دقیقه دو انفجار با صدای بلند در کنارک
همین الان ساعت 3:30 دو انفجار شدید در جابهار و یکی هم صداش خیلی دور بود شاید اطراف فرودگاه کنارک. ولی دو انفجار چابهار واقعا شدید بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76943" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
ترجمه ماشین:
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، [۲:۱۵ بامداد شنبه تهران] نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76942" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNQivVnF8W0kKb6KQg5Ljz0y7JcDXD7QWkYRJHJb067jm1CzcCvW-9Zw2nT3gt628W6jTykOcNDNi95ilvEQMsmd0ZAzlIjMOlbCm0_p5DgZ8ygK-6ssvtcd0EC_7WhHOBgNX-evI8C7iNMZ8jOeycwjhf2I19uUFMdud1OXG43QbBItWIBmRIQFL7RETad0pCit8ZXX0ZQJGLOEOCDt19_VP0NhuGOuXlKUBbErmDoWXKj-VDo6GnD8OOkS1Nkm3xRsErhMBBw67Wb_cfgq9IauEs2ui1xSa7JDKaGj6EWiSLjY6gorPZD6jyEDzcwvnE-GDoS4XMO5x7H5WhEUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
‌
بوشهر صدای چند انفجار لرزش زمین احساس شد زیرپام
صدای دو تا انفجار بندر دیر ساعت ۲:۴۶
۲۱ تیر
سلام
ساعت ۲:۴۰ شنيده شدن چهار تا پنج انفجار در کنگان و حوالی آن
وحیدجان
الان حدود دو و چهل و پنج دقیقه صدای چهار پنج انفجار بزرگ توی بوشهر
شبشه های خونه لرزید
وحیدجان سمت نیروگاهه
من تنگک هستم الان دود و نور قرمز از اون سمت می بینم
سلام اقا وحید ساعت ۲:۴۵ بندر کنگان چهارتا صدای انفجار اومد
سلام ساعت ۲ و ۵۰ دقیقه بوشهر صدای چندین انفجار
۲:۵۰ بوشهر صدا انفجار
صدای چند انفجار اومد در بندرکنگان
سلام.ساعت ۲/۴۵ دقیقه شهرستان دیر استان بوشهر.صدای دو انفجار مهیب با فاصله یک دقیقه از هم شنیده شد.موجش شدید بود
سلام وحید
بندر دیر رو زدن ساعت ۲:۴۶
تو جنک هم ۱۰ ۱۲ باری زد یا بیشتر یادم نیست الان
اسکله نیرو دریایی زدن
🔄
همین الان ستا انفجار دیگهههههه.
بندر دیر.
وحید جان الان ساعت ۲:۵۶ باز دوتا بمب دیگه بندر دیر رو زدن
۲:۵۵ بازم زدن بندر دیر رو
دو بار دیگه ۲:۵۶ زدن
کنگان همین الان دوتا صدای بزرگ انفجار اومد۲:۵۶
کنگان رو دوباره زدن
🔄
تایید نشده:
صدای انفجار شدید بندرعباس
همین الان قشم صدای یه انفجار مهیب اومد
دقیقا ساعت ۳
ساعت ۳:۱ بندرعباس صدای دو انفجار پشت هم اومد
صدای انفجار، سیریک.
🔄
استان بوشهر
سلام وحید جان بندر بوالخیر  رو زدن
سلام اقا وحید بندر بوالخیرو زدن
🔄
عسلویه بوشهر
یکی که در واکنش به خبر  قبلی درباره عسلویه پیام داده بود: "ببین ۱۰ دیقه پیش صدا اومد ولی نزدیک نبود" الان پیام داده که:
وحید اینجارو دارن میزنن
همین الان صدا و لرزش خونه ۱۰ تا انفجار
عسلویه
پیامی دیگر:
عسلویه
حدود یک ساعته نه یا ده صدای انفجار اومد که دوتای اخری خیلی شدیدتر بود
ولی منطقه پتروشیمی و پالایشگاه خداروشکر خبری نیست
همه‌ی صداها از  سمت ساحل حاله و ساحل بنود یا بندر تین هستن
تقریباً بین۱۰تا ۲۰ کیلومتر با عسلویه فاصله دارن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76941" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAS08lLYtLXpAzDe9Cna-Iq1j3RGEJAzWPaMx18q2Qgekg7Clj3SHZMIQPm0pkAIu7EIMZ2168mTjy8jSqvF9z_lw_DAhCyM0s0h1uSKom3rpk6RJpRhx_Cw-uTRrurPutD0zgGDouk-tOLPPPxfVXqH82I0mPcrotIXfY67lwVhdu45fp9o4gX6nZBgMymbZSrDrwro1WWaaAAuNmS8g0pIHsyKgcmAPYgsAKPsfUywFq2rvFEkKm0ed3kQDbMLFqWaTDIYPYsM8XhhE0pn5r6LTkYtwSdpkRFbpa25Cd2trBzxawyY-bG94HLM-NLn3F6CzNevyh6Z4jhw_2ojVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با بیانیه سپاه پاسداران مبنی بر «بسته بودن تنگه هرمز تا اطلاع ثانوی و پایان مداخلات آمریکا»، یک مقام آمریکایی در گفتگو با خبرنگار آکسیوس اعلام کرد که سپاه یک موشک به سمت یک کشتی باری تجاری که قصد عبور از تنگه هرمز را داشت، شلیک کرده است.
به گفته این مقام، کشتی مذکور مورد اصابت قرار گرفته و دچار خسارت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76940" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ReXtI1p6e_qe9_PhPBHIWsrkpzeeG06jameBRkJ5v4LZrv6g_QQz3JgJjNu2TYSe4M8PR73tLho6DGUe7CTyuDbs48zmP_f13Hq60ElgT4ZQvYkX8yXthy0WFFxX2RDcvD0GpMLV4j88VhYikYGKfAnVFlTb2XABAX4bIbXNaxMzXm9O-NJF56aFugKj_Pb8EDuQSssyFvyp8sL3ZVK86MNM_mHiVYw2GRVV9B67Yb-3RDm1bXKJMMUMltI65hbdbfD08npN_hJhgtUlditnk6RVjDAAMuBqOJtdChH9i6Bpbx8KOJLwZBjzGAjV4sExmE6un0RDto7cxw0uZOsQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: یک کشتی را هدف قرار دادیم / تنگه هرمز تا اطلاع ثانوی بسته شد
ایرنا:
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
بسم الله قاصم الجبارین
در اطلاعیه قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
🔹
به ناچار یک فروند کشتی‌ که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌اخطار واقع و متوقف شد.
🔹
به دنبال این حادثه، اولا با توجه به بروز این ناامنی به سبب مداخله غیرقانونی بیگانگان، تنگه هرمز تا اطلاع ثانوی و تا پایان مداخلات آمریکا در این منطقه بسته و هیچ شناوری اجازه تردد نخواهد داشت، ثانیا اگر دشمن متجاوز به بهانه این حادثه که خود، مسبب آن بوده است، خطایی کند و تجاوز جدیدی علیه ما داشته باشد با شدت پاسخ داده خواهد شد و پایگاه های جدیدی از دشمن در منطقه مورد هدف قرار خواهد گرفت.
🔹
عواقب چنین مداخله‌ای بر عهده دشمن آمریکایی - صهیونی و کشورهایی است که خاک خود را برای این تهدیدات در اختیار پایگاه دشمن گذاشته‌اند.
و ما النصر الا من عند الله العزیز الحکیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76939" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرنگار اکسیوس:
‏
🇴🇲
🇮🇷
یک دیپلمات که در جریان مذاکرات قرار گرفته است گفت عمان در گفت‌وگوهای امروز مسقط پیشنهاد کرد که مسیر جنوبی در آب‌های عمان و مسیر شمالی در آب‌های ایران، هر دو به‌طور کامل فعال باشند.
‏
🇴🇲
🇮🇷
این دیپلمات گفت طبق پیشنهاد عمان، مسیر جنوبی بدون هیچ‌گونه الزام برای دریافت مجوز باز خواهد بود؛ همان‌طور که پیش از جنگ بود.
‏
🇮🇷
🇴🇲
این دیپلمات گفت ایرانی‌ها نتوانستند این پیشنهاد را در جلسه به تصویب برسانند و ناچار شدند آن را برای گفت‌وگوهای داخلی به تهران ببرند.
BarakRavid
سی‌ان‌ان:
یک منبع آگاه از مذاکرات به سی‌ان‌ان گفت عمان پیشنهادی را برای مدیریت تردد در تنگه هرمز از طریق دو مسیر با کنترل جداگانه تدوین کرده است.
بر اساس این توافق که هنوز نهایی نشده است، هر دو کریدور باز خواهند ماند. کریدور جنوبی که از آب‌های سرزمینی عمان عبور می‌کند، امکان کشتیرانی آزاد را مطابق شرایط پیش از جنگ فراهم خواهد کرد.
کشتی‌هایی که از کریدور شمالی، در آب‌های سرزمینی ایران، عبور می‌کنند، باید از ایران مجوز قبلی دریافت کنند؛ با این حال، طبق این توافق هیچ عوارضی از آن‌ها دریافت نخواهد شد.
CNN
علی قلهکی
:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/76938" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n7U87hdAFO36KgW6BTsCBYDjXkbfbSbrcKteldYYQ5SJMF_luChZJJ-3yLFCm9DV_iTK-6HyrYnLC-ZWeNYMcpD-b3fKA0-qW119WxrsbnvbB03_h1vNaFAWk85H6pBxxpPQ144DihdTTloue6fCWTVZjt2Lh7xHtsUfnX2IJqLDD_m0dSiGjCPI3TmxPDNl8ALusSPWideodGQJQKeEhfsrBbZk-FTe7NEq6d7FjqPaKQ-J_nSISL9GeOhp57swa8rJqLfalrKvBvDtZ9q99mTFHdpPV70JJ6eShet55Mr117HrQdYIUVNarsXy8xnfVQ2l2f1rFP-8EZMI9lVtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا، طی روزهای گذشته پیش بینی شده بود گرمای هوا تا هفته منتهی به دوم مردادماه با میانگین دمای بالاتر از ۳۹.۷ درجه تداوم خواهد داشت، از این رو تمامی سناریوهای بهره‌برداری شبکه بر مبنای نیاز مصرف ۷۵ هزار و ۵۰۰ مگاوات طراحی شده و مرکز ملی راهبری شبکه برق کشور و واحدهای عملیاتی صنعت برق در آماده‌باش کامل قرار دارند با این وجود بنا به گفته مسوولان شرکت توانیر  هیچ محدودیتی در تامین برق بخش خانگی اعمال نخواهد شد.
اما امروز  ۲۰ تیرماه برخی کاربران ایسنا [و بسیاری از دنبال‌کنندگان اینجا] طی تماسی عنوان کردند که در برخی مناطق  همچون محدوده ولیعصر، مطهری و قائم‌مقام فراهانی [و مناطقی دیگر و شهرهایی دیگر] با قطعی برق چهار ساعته مواجه شدند و با وجود پیگیری‌های ایسنا از شرکت توزیع نیروی برق تهران بزرگ تاکنون علت این خاموشی‌ها اعلام نشده است.
به گفته مشترکان همزمان، حجم بالای تماس‌های شهروندان با سامانه فوریت‌های برق ۱۲۱ موجب شده زمان انتظار برای ارتباط با اپراتور در برخی موارد به حدود نیم ساعت برسد.
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76937" target="_blank">📅 17:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUoMuvwZS3gqfpNWi9PbUSB4wbPHa2afHe8NslZ4FNI0itrAxf3F0RC89qsIeLu9AzT07wATvdZI2Z8j4tlMsMbE92dzXTEQQExZ5TvstLoHnDwtv6eWFW7vwVnXibQk_XI4WxlwmNUS9uu5LiMwianmnVWjwisaEYSMk7tMdFlCSflQnZtjk5OmhYlH9GZkilHUGMq-vIEVOC_fd1_2jT802NkvFt0jsDXialxNbIb_dQbrCkKpQeqtonu3ebabpLV0FNZgkezAuy75FYr2wjH7pfyxzfHqxe6NhDgkz4Gjh54AqkoZaNivnHCY8aK-6LIPnx7_Honci9tRXJWdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه امام رضا اعلام کرد دو نیروی بسیجی به نام‌های «سید سجاد علوی» و «مهدی هنرمند» در حوالی میدان سرافرازان مشهد هدف تیراندازی قرار گرفتند و کشته شدند.
بر اساس اطلاعیه سپاه، این دو بسیجی در زمان وقوع حادثه در حال گشت‌زنی در محدوده بلوار سرافرازان، در فاصله حدود ۱۵ کیلومتری حرم امام رضا، بودند. این حادثه همزمان با برگزاری مراسم تشییع و تدفین علی خامنه‌ای در مشهد رخ داد.
سپاه امام رضا اعلام کرده است که این نیروها در چارچوب مأموریت‌های تأمین امنیت مراسم تشییع و خاکسپاری علی خامنه‌ای در منطقه حضور داشتند.
در این حادثه همچنین یک عابر پیاده مجروح شد و به بیمارستان انتقال یافت.
اعلام کشته شدن این دو بسیجی در حالی صورت می‌گیرد که امیرالله شمقدری، معاون امنیتی [دروغگوی] استانداری خراسان رضوی، جمعه ۱۹ تیرماه
گفته بود
تیراندازی در بلوار سرافرازان مشهد «اقدامی تروریستی» نبوده و ریشه در یک «درگیری شخصی» داشته است.
خبر این درگیری مسلحانه همزمان با تدفین علی خامنه‌ای در شامگاه ۱۹ تیر منتشر شده بود. آن‌زمان اما جزئيات آن منتشر نشده بود. اگرچه ساعتی پس از این درگیری سازمان هواپیمایی کشوری از اجرای «مجموعه‌ای از تمهیدات ویژه» در مشهد خبر داده بود. همچنین گزارش‌ها حاکی از آن است که برای ساعاتی، مسیرهای خروجی شهر مشهد بسته شد و تدابیر امنیتی در این شهر به‌طور چشمگیری افزایش یافت.
این حادثه در شرایطی رخ داد که مشهد میزبان آخرین مرحله از مراسم تشییع و خاکسپاری علی خامنه‌ای بود و هزاران نفر برای شرکت در این مراسم به این شهر سفر کرده و امنیت شهر در بالاترین سطح خود بود.
@
VahidHeadline
شخص همون معاونی که اون طور صریح دروغ گفته بود امروز آمار هم اعلام کرده درباره تشییع‌کنندکان مشهد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76936" target="_blank">📅 17:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nSr7z8VtxmX6m-7XlTqvQMZWBC-8zZtTQXbh7UPfA043SnFB9tEJBvMX-xGeX1GUIPWHwJSBe-LkmOYxDNMNoT9hm28VVnaMsNfNt_dYqrTk24xfhFqs_Cljl9b_IqagrhaZoChpMFtd5_0fn3V3awnl6WDoYIO7iCfOWM-nO1QVLI-wK58dR1cQiLAYNFE_A6S2EtOCnhbW53DHrvGYsJkG7CJDWI7DTDT7VNHIcDHMcoNM92s1SHgY_yDh290TBBJt7tGTWllmwwg43wLwl-r0BXxC5Kz2IeFwxv6TceYMeJfAmI-pSfphgOGU2AI_-K-G2hQucyyJVv02dKEAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، رهبر جمهوری اسلامی، در پیام مکتوبی منسوب به او که روز شنبه ۲۰ تیرماه منتشر شد اما تاریخ آن مربوط به دو روز پیش است، اعلام کرد انتقام خون پدرش علی خامنه‌ای «به‌طور حتمی باید صورت بگیرد».
خامنه‌ای در این پیام همچنین به «قاتلین» پدرش هشدار داد که «این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگ آرام و در بستر را با خود به گور خواهند برد».
او در عین حال تأکید کرد که انتقام «متوقف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادِ آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد».
مجتبی خامنه‌ای در این پیام نامی از کسی نبرد، بخش‌های دیگر پیام خود را نیز به تشکر از تشییع‌کنندگان رهبر کشته‌شدهٔ جمهوری اسلامی اختصاص داد و به درگیری‌های اخیر ایران و آمریکا بر سر آتش‌بس، تفاهم‌نامه و تنگه هرمز نیز هیچ اشاره‌ای نکرد.
دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد شنبه نوشت در صورت هرگونه اقدام یا تلاش برای ترور او، «هزار موشک آمادهٔ شلیک» به سوی ایران هدف‌گیری شده و ارتش آمریکا برای یک دورهٔ یک‌ساله، با امکان تمدید، آماده است «تمام مناطق ایران را به‌طور کامل نابود کند».
پیام عمومی مکتوب قبلی منسوب به مجتبی خامنه‌ای ۱۱ روز پیش به‌مناسبت هفتهٔ قوه قضاییه منتشر شده بود.
مجتبی خامنه‌ای در عین حال غایب بزرگ مراسم تشییع علی خامنه‌ای بود که بیش از چهار ماه پس از کشته‌ شدنش در اولین موج از حملات آمریکا و اسرائیل طی چندین روز با سازماندهی حکومت برگزار شد و نهایتاً ۱۸ تیرماه در مشهد به پایان رسید.
در جریان تشییع جنازهٔ یک‌هفته‌ای علی خامنه‌ای، بسیاری از شرکت‌کنندگان در این مراسم خواستار «خون‌خواهی» و «عدم سازش» شدند و گروهی نیز پارچه‌نوشتهٔ بسیار بزرگی با مضمون درخواست برای «قتل دونالد ترامپ» همراه داشتند.
مجتبی خامنه‌ای بود که کمتر از ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر تازه جمهوری اسلامی معرفی شد، در هیچ بخشی از این مراسم حضور نداشت. در این مدت طولانی هیچ فایلی صوتی یا ویدئویی نیز از او که نشان دهد در چه وضعیتی است، منتشر نشده است.
این در حالی است که در مراسم تشییع جنازه علی خامنه‌ای تقریباً تمامی مقام‌های ارشد جمهوری اسلامی حضور داشتند، از سران سه قوه تا فرماندهان سپاه پاسداران و حتی سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از ۹ اسفندماه پارسال یعنی آغاز جنگ تاکنون خبری از آن‌ها نبود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76935" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY8PaWcOi6VbQAbEdIMRzxM6GVUjomSUPxsjiCbaOcWnreCgYYet2MFL_-65OwqnnSL89BTSuCocDlFOFj-6m08imsc5B4BhHWlN4FmIIUUEcuvl3GK7374InxZEK8jCgDPIxA8-c59TvIKi07lgHhPeBlFUTW6l_hvbYY_CuTDe1BEUs_47rUyY1Te4PX0JNAiP8m-0aIth6qZJ6vZAtgvMccOe2HWT_P0SOh7E5sV1oyydicBxArfXe8VxLY0fUl6Qc59vmElqxpxx6OIpd-ANZ2dln9eucb_aQV7aJHCUhC5Qub66-mu9I1UzABw97omLsIq-VqZzmngYHcBqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، از صدور حکم حبس برای یک فعال صنفی معلمان خبر داد.
این شورا روز شنبه ۲۰ تیر اعلام کرد شعبه ۱۰۳ دادگاه کیفری ممسنی شکرالله احمدی، بازرس این شورا و عضو هیئت‌مدیره انجمن صنفی معلمان فارس، را در مجموع به سه سال و هفت ماه و ۱۵ روز حبس محکوم کرده است.
آقای احمدی به «اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی و خارجی» و «فعالیت تبلیغی علیه نظام جمهوری اسلامی» محکوم شده است. او ۲۰ دی ۱۴۰۴ در خانه‌اش بازداشت و چند روز بعد آزاد شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76934" target="_blank">📅 17:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJyfn29kZEcoQz4OgIKGz775UD-FW1Z_yYPjXw7gKEAumcM-P4wSSI0EYqiQvIjsyc3FsKcHwj0cBxRvk6wlsOjIA33M4kSjQisC1TPJYvk7gBO9SxlqGyzAfHmdLapNLx4oOTTeDJTGngeQBIqh52Mm5jCoplMC0EbT2FrUNTHmPwICid3wQ8s47YQOZktIBPbDRntUzUgRsTbusjh-hVoFD4Q-O5Rx8KdJcFDkhn1snLkb0c7Vj_LwcwMOrfTJst_766niCRFa9WG0Od4S1PzQGaAOc9pYSwoiUmiURHB6FFvNTQ2uwFt1RiyKXTAJlhb7mnp-rgOeth6bORdhJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کودک ۱۳ ساله در پی تیراندازی نیروهای مرزبانی به سوی یک خودروی خانوادگی در منطقه هو‌رامان استان کردستان جان خود را از دست داد. مقام‌های محلی اعلام کرده‌اند که این حادثه از سوی مراجع قضایی و نظامی در دست بررسی است.
تابناک خبر داد که این حادثه در منطقه مرزی «ته‌ته» هو‌رامان رخ داده است. اعضای یک خانواده پس از پایان کار روزانه در باغ خانوادگی، با یک دستگاه خودروی تویوتا در مسیر بازگشت به منزل خود در روستای «دره‌کی» از توابع شهرستان سروآباد بودند که نیروهای مرزبانی، به ظن آن‌که خودرو متعلق به قاچاقچیان است، به سوی آن تیراندازی کردند.
در جریان این تیراندازی، گلوله به کودک ۱۳ ساله‌ای که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
استاندار کردستان با تایید این حادثه اعلام کرده است که موضوع از طریق وزارت کشور، دادسرای نظامی و مراجع قضایی نیروهای مسلح در حال پیگیری است. او همچنین بر لزوم روشن شدن ابعاد حادثه، نحوه وقوع آن و اطلاع‌رسانی نتایج تحقیقات به افکار عمومی تأکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76933" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hJq_psHfmEAxk4YbB9vYKJYP3EHVXOglrVHD0MHSS26RkgY_eRDmsiR755elbNESHGVQUV4lfQNOz2EgrM0pwpFa-fW21-0kIetwGNRiohr2KIvYRiNbohPk5aTh5TZElngJMo2qNA-wfNW1mytTTcCXy-wf1O1nR1NZ1_ZT9J3wZsf_InvltGhFAt3XFlNSsLTkjcXfPBmVySg0-S0TwJjGfZfUT26KzVFfpLvr4eFBHc0s6RvjmeyAleYyd243D7sE3Ex2OmnZNpSwJw6L6EY6N8Vlh3BAImslxHLtIFhGejMnTeWdNMwmc1sQwIOPAsFo5rRZqQDTCvVp8nHS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GUkjLN4Fg_ybDUlBi7D4RMVRmvz3e18OMfNYXurQ9XZXmsAMZB1v0iVP1M13dVyaJOaITmDn69Fe-7cMHNGb8qd0F4qrLwjpE0xvHy-CBWR9ELAk2jAjPgsTBf7MSC9Dol8CxTLnFN9UhlKJGvgbIwcSHVAyMrJ6tTbxLBonj68vWFLiWMcPYX18O0kqMJa9Q7BhEPpTpS8PiJ_xv8OXFoPyY8O4nNmvSHX5_6p1JJN_T1ERpsR8-m0DlKYl2CdRRP1kkt5DW3n7oXtYZxoy31BiXd9qKHefcXIgMktSR4G89KX4vsbDEk0SdyONrtK46-q5Gh980Nsuo2BydnIrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qVZAC4T1F0-iXls6rAbUu1g9ny5ea1Tl2ppZmfZhFhpMxdFripe_vfbmik4ZGwjVwoP-HdWJdBaPv338fhTBJdKo74hq5vZKv_A15mRF-4-anm3c6VPb9slufQT-fMhcdGiNQOR1U_gq0ZWdgErP47kvA5o1wo1w8OF7HakqY3yadD3j7J8ig77mCnXA9cwVioyk_HazgCzfiJW3hIdHnyDeFe-yvCX0aDJvmOcbWHvYXQC9JF3JbcvRGz1dQ5GxgZ7vq7xCH6fgFy9PmX83TVdPYIidf1KRQPCMnDumyl7WjmGaJgit37xhocMdD4E95qSDUhagP6YapK07F-no3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=sSzjGC4MvoGUQ49OxzeSkVL2B5Tj56ncANrsxsjAu2yUj41L7s7ocyvdBEYJ6BUs6WP2r5AW7ZzBhB8CUcMbantBjnBHK01hlFtmqR6dYmVxreqM_wsn12k81JJMOpsy_7uOZDsIwJFmWDsdVERVeeuExD1F579lNGrkFFcM2eXbQQ3b_ES4wj1NoUBHN-6VctBkMPV4CuuaGNGeBgTEfhnpABV3HJl0-l98q2jRPuSjuAx99nLpeAIDweZYa_Go9o1B0CSZjDxRUywgmrGzdw3Vdv06bUyAwnrT83tI--ju4NeaKKEHYeCo2hu-DuepQzzr8__1E44YVaVGBV2o7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=sSzjGC4MvoGUQ49OxzeSkVL2B5Tj56ncANrsxsjAu2yUj41L7s7ocyvdBEYJ6BUs6WP2r5AW7ZzBhB8CUcMbantBjnBHK01hlFtmqR6dYmVxreqM_wsn12k81JJMOpsy_7uOZDsIwJFmWDsdVERVeeuExD1F579lNGrkFFcM2eXbQQ3b_ES4wj1NoUBHN-6VctBkMPV4CuuaGNGeBgTEfhnpABV3HJl0-l98q2jRPuSjuAx99nLpeAIDweZYa_Go9o1B0CSZjDxRUywgmrGzdw3Vdv06bUyAwnrT83tI--ju4NeaKKEHYeCo2hu-DuepQzzr8__1E44YVaVGBV2o7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
Vahid
خبرگزاری فارس:
فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده و از پیش برنامه‌ریزی شده بود.
پس چرا اعلام نشده بود؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76929" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kSefMvZSw0BLTuIR7_5S2OgU6jxHx_vqsW_WPKGKTh9OzSGzGcpE2vG303vunzMsJpYPE7JusIu32_KQosAtc8rnOKD2fIIT_oE5qMzvdF60tf77MRIZ4-YcMJKRIJ-OczwkeTxNKbEuCbl0xUhRrrnkBgN_05DmtV2t_l_3xhjrLKabj04DjNw3jL2sINDbiGFocZGRn649zH8Sq6Xi4Wr37cGWJ_nn4Uf4e6M9SPitasDINzvAuyQJJldOUpz3OJzVGTMwVhFlseW3nC8e60SsGoBz5utvfip90JMPIdMfdAb7MqPPO9zzbcF_VHQQD9GBk7wOnLuCh6xC2r5cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در پاکدشت پارچین
سلام وحید جان
پارچین همین الان صدای یه انفجار شدید ۹:۳۱
صدای وحشتناک قرچک. مغازه لرزید
کل قرچک صدا رو شنیدن
معلوم نیست هیچی
ساعت ۹:۳۰ صدای انفجار شدید سمت پارچین
دودش مشخصه
قیامدشت کلا لرزید
شهرک صنعتی خاوران
شیشه های مغازه لرزید ۹:۳۰
سلام ما خاور شهریم صدای انفجار شدید اومد شیشه ها لرزید
صدای انفجاری محیب از قیامدشت به گوش رسید
به حدی مهیب بود خونه لرزید
سمت شهرری هم لرزید حتی
درود ، عزیز پاکدشت صدای انفجار اومده دقیق ساعت 9:28
سلام ماهم صدای انفجار پاکدشتو حس کردیم از خواب پریدیم و ترسیدیم ولی یک انفجار بود
سلام اقا وحید ما تو قیامدشت چنان حس کردیم که انگار کارخونه خودمون منفجر شد
کل قیامدشت و چهلقز شیشه ها و خونه ها لرزید
سلام وحید جان ،پارچین انفجار شدید بود،ما قیامدشتیم،موجش تا اینجا اومد
سلام قرچک صدای انفجار اومد شیشها لرزید ولی دود دیده نمیشه
سلام ما محله ی ارکیده های پاکدشت زندگی می‌کنیم
و انقد انفجار شدید بود ساختمان ها لرزیدن
سلام پردیس  شنبه ۲۰ تیر حدود ساعت ۹،۳۰ یه صدای بلند اومد
ما پارچین هستیم همین الان صدای انفجار اومد تقریبا ده دقیقه قبل ،الان دودش هم میاد
وحید جان پارچین یه انفجار شد ستون دودش معلوم بود. پشت تپه های پارچین
تموم خونه ها شدید لرزیدن
سلام. نارمک ما صدارو شنیدیم تا قبل پیامها فکر کردیم توهم بوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76928" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qjo9gLGX0UW20aACDW4fWb59pdhMuMTXx7XoawyE5TxQWmxEM9gZlWBYzqRfnCTkamGf7UwwWyA1Jm79pN8y2dsp8aWk9KiNHQoPM3t6uxMWR1qo5IPRa0O142zYa9FPgiWe5DlDzjlYS0bfhGUFeUZekIbsnyLvS-2lmoAF_i209fZe4_A7meZYlFg-6Hw-sE6JZ9wRkUcqzQT9hDUceyy0CuNZZR-w8y8RcazSmKFPErbGua8tHBiQXhPPyqnOmAxJ8QirYHkGR9upLq58RIL8FryVVqLoRgUp2iWuJTTycVw2VhPHr6jtyYlW_eZWcM8KJrC4F2UtlQbROZu5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر تهران برای ترور من تلاش کند، هزاران موشک دیگر شلیک خواهند شد
ترجمه ماشین:
هزار موشک در حالت آماده شلیک قرار گرفته و جمهوری اسلامی ایران را هدف گرفته‌اند و در صورتی که دولت ایران تهدید خود را ــ که در بسیاری از نقاط جهان اعلام کرده ــ برای ترور یا تلاش برای ترور رئیس‌جمهور مستقر ایالات متحده آمریکا، که در این مورد شخص من هستم، عملی کند، بلافاصله هزاران موشک دیگر نیز به دنبال آن‌ها شلیک خواهند شد!
دستورها از پیش صادر شده‌اند و ارتش آمریکا آماده، مایل و قادر است برای مدت یک سال ــ که قابل تمدید است ــ تمام مناطق ایران را به‌طور کامل درهم بکوبد و نابود کند — ستایش از آنِ الله باد!
رئیس‌جمهور دونالد جی. ترامپ
1000 Missiles are Locked and Loaded and aimed at the Islamic Republic of Iran, with thousands of more to immediately follow, should the Iranian Government act on its threat, pronounced in many corners of the Globe, to assassinate, or attempt to assassinate, the sitting President of the United States of America, in this case, ME! Orders have already been given, and the U.S. Military is ready, willing, and able, for a one year period of time, subject to extension, to completely decimate and destroy all areas of Iran - PRAISE BE TO ALLAH! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76927" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IPy-065Q7ZBgqa5RG2_upHiCB-xvRzuEL-UiV9ybtNpxuNQ4zSuv-NHDlPQDMjUQIumg6llXxyYcl0gWEsT64So-XkfhdD-35QrkeRH8irU8JbpcZuacYanpLKL8aWujEsM_KsHsVvCPmd1uXrzkokybTp4kjbHkuqJuSHX7hiFc1nj5lcrFYhivnGMNUcTnChVso4hXix6UsyKn6gzaNKxDZtuhiT11WEHNizZc7Wg5-fau8w3vFEK3aiCIjN5MV15cXSmbLj3rJiu5UpVcGv3UQjC9D4NqN__vf3bgDW6auLYcaRv0Q7aFF0VOuFN7XngSLgBSQU8e8zgRBWHL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «سی‌بی‌اس نیوز»، مقامات ارشد آمریکایی روز جمعه فاش کردند که مقامات ایران در پیامی محرمانه به مشاوران دونالد ترامپ اعتراف کرده‌اند که شلیک به کشتی‌های تجاری در تنگه هرمز یک «اشتباه» بوده و این حملات توسط یک جریان «خودسر» از تندروها با هدف تخریب مذاکرات انجام شده است.
با این حال، کاخ سفید این اقدام را نقض صریح آتش‌بس دانسته و خواستار اعتراف علنی تهران به این اشتباه شده است.
براساس این گزارش، تیمی ارشد از سوی ترامپ، شامل جی‌دی ونس، معاون رئیس‌جمهوری، جارد کوشنر، داماد ترامپ، استیو ویتکاف، فرستاده ویژه کاخ سفید و مارکو روبیو، وزیر خارجه، مامور شده‌اند تا گفتگوها را روز شنبه در عمان ادامه دهند. در حالی که واشنگتن انتظار دارد ایران پس از این نشست تعهد خود را به باز بودن کامل تنگه اعلام کند، مقامات آمریکایی هشدار داده‌اند که اگر ایران نتواند به این ساده‌ترین بخش توافق پایبند بماند، امیدی به حل مسائل پیچیده‌تر نظیر تسلیم ذخایر اورانیوم غنی‌شده نخواهد بود و در صورت ادامه اقدامات خصمانه، با پاسخ سخت نظامی و اقتصادی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76926" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZBSj7P7bLdf7zBcTVaBcDQwDapIZzcv7X6ioYMsFBK9s8eaau-rQMS7eEVt733ayX1bdCG07IvnYbvvhzzkmf_3zz--6LwdTw5FQ62NTUauWUf-XQprNrGK01yR91TUb4nK0pKshJFcznXOxP_9XUszjOmbElOVXRQjKVTlmTe9npic6Pd3bn1si5ljczZYdweK6DwFzF2DrF1AuozuFKY8ClzyNdp8tqX7y2r7O7j0e0vGVMlEcQPHqcBoCuKL1ovajTY9sfbTYRIsjej9pJyprTNKgBx0l7J1OTVACYG9jjS3bCCUUJHY6KbfbIOIxbv5UArWIQGRD_yVP5D6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از ایران خواسته است ظرف ۲۴ ساعت علناً متعهد شود که شلیک به سوی شناورها در تنگه هرمز را متوقف خواهد کرد
اکسیوس (ترجمه ماشین):
سه مقام ارشد آمریکایی روز جمعه در جلسه‌ای توجیهی با خبرنگاران گفتند ایالات متحده، هم به‌طور مستقیم و هم از طریق میانجی‌های منطقه‌ای، از ایران خواسته است امروز، شنبه، بیانیه‌ای علنی منتشر کند که در آن روشن شود تنگه هرمز باز است و ایران متعهد شود به سوی کشتی‌های تجاری عبوری از این منطقه شلیک نکند.
چرا اهمیت دارد:
ایران با چندین بار شلیک به سوی کشتی‌های تجاری در تنگه هرمز، یادداشت تفاهمی را که سه هفته پیش با ایالات متحده امضا کرده بود، نقض کرد.
این اقدام به چند دور تبادل آتش انجامید و توافق را در معرض فروپاشی قرار داد.
مقامات آمریکایی می‌گویند اگر ایران به چنین تعهد روشن و صریحی پایبند نباشد، این موضوع تردیدهای جدی درباره اجرای یک توافق هسته‌ای ایجاد می‌کند؛ توافقی که بسیار پیچیده‌تر و حساس‌تر است.
محور خبر:
قرار است عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، روز شنبه در مسقط دیدار کنند تا درباره وضعیت تنگه هرمز گفت‌وگو کنند.
عمان در هفته‌های اخیر، حتی پیش از امضای یادداشت تفاهم، با ایالات متحده و متحدانش در خلیج فارس همسو شد و یک مسیر کشتیرانی جنوبی در نزدیکی سواحل خود گشود که کشتی‌ها می‌توانند از طریق آن از تنگه عبور کنند.
ایرانی‌ها که معتقد بودند این اقدام اهرم فشارشان در مذاکرات با ایالات متحده را تضعیف کرده است، خشمگین شدند.
مقامات آمریکایی می‌گویند اعضای تیم مذاکره‌کننده ایران به آن‌ها گفته‌اند عناصر تندرو در داخل حکومت تصمیم گرفتند برای بازگرداندن این اهرم فشار، شلیک به سوی کشتی‌ها را آغاز کنند.
در مواضع علنی، تیم مذاکره‌کننده ایران، فرماندهان سپاه پاسداران انقلاب اسلامی و دیگر مقامات ارشد، همگی موضع واحدی دارند و خواستار کنترل ایران بر تنگه در آینده هستند.
پشت پرده:
یک مقام ارشد آمریکایی مدعی شد که پس از دو روز درگیری در اطراف تنگه در اوایل این هفته، ایرانی‌ها «دوباره به سراغ ما آمدند و خواستار گفت‌وگوهای بیشتری شدند تا برای حل برخی مسائل تلاش کنند.»
این مقام آمریکایی گفت: «آن‌ها به ما گفتند: “گند زدیم. اشتباه کردیم. بیایید به گفت‌وگو ادامه دهیم.”»
به گفته او، در داخل حکومت ایران بر سر اجرای یادداشت تفاهم و مرحله بعدی مذاکرات با دولت ترامپ، جنگ قدرتی در جریان است.
یکی از مقامات ارشد آمریکایی گفت: «افرادی در داخل نظام آن‌ها هستند که می‌خواهند به توافق برسند، اما ما نمی‌توانیم به‌جای آن‌ها تصمیم بگیریم. خودشان باید اوضاع را تحت کنترل بگیرند.»
چه می‌گویند:
مقامات آمریکایی گفتند انتظار دارند ایرانی‌ها پس از نشست روز شنبه در عمان بیانیه‌ای منتشر کنند.
یکی از مقامات ارشد آمریکایی گفت: «ما می‌خواهیم آن‌ها علناً بگویند که شلیک به سوی کشتی‌ها را متوقف خواهند کرد و به‌صراحت یا دست‌کم به‌طور ضمنی بپذیرند که گند زده‌اند.
در حال حاضر روی همین موضوع کار می‌کنیم. انتظار داریم ایرانی‌ها بگویند همه مسیرهای کشتیرانی در تنگه باز خواهند بود و هیچ عوارض عبوری دریافت نخواهد شد.»
یک مقام ارشد آمریکایی دیگر گفت اگر ایرانی‌ها از انجام این کار خودداری کنند، پیامدهای سنگینی در انتظارشان خواهد بود. او گفت: «اگر فردا موضع آن‌ها این نباشد، روز خوبی برایشان نخواهد بود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/76925" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSU-UWCb2JFCcHZTVL0i5-2s1l7IX84Suh-eh2K0dqXs2eE4aCppFgmjNiDuVWseeJpw5GRmdPZVRsz_tsaKKbs7pNVO2YQT4OTEO_3OWEzY4PxLzU80hU6lJdaz-B1lgPGkShvIvdMg6xDHSrIw_bhKZw4jY7HsMqzNf4se90CFOj2gdlQXIoXcYJvTJIgRtrVFI5e5s6ER-KhqFj_5ru833RPWnHq6MnLdxm5e-8HIPLGPEOvxLmnfGLSminDqyO8lRYJgwttk6p8ZQLWAJ5EXzOQeK7ZxSnnH63s6QT7Vjb23AkAakUXS57nVRE3rLmkWlivD5n4kc2hBrb1WbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در اقدامی که از بی‌اثر شدن تفاهم اخیر میان تهران و واشینگتن حکایت دارد، تحریم‌های تازه‌ای علیه جمهوری اسلامی و شبکه مالی آن وضع کرد. در فهرست تحریم‌های جدید نام علی انصاری، از چهره‌های نزدیک به مجتبی خامنه‌ای و متهم به فساد اقتصادی، دیده می‌شود.
وزارت خزانه‌داری آمریکا جمعه ۱۹ تیر اعلام کرد این تحریم‌ها در واکنش به حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز اعمال شده است.
این وزارتخانه علی انصاری را «تسهیل‌گر مالی» جمهوری اسلامی معرفی کرد و نوشت او بر شبکه‌ای گسترده از دارایی‌های جهانی به سود مجتبی خامنه‌ای و دیگر مقام‌های حکومت نظارت دارد.
بر اساس بیانیه وزارت خزانه‌داری، انصاری با نهادینه کردن اختلاس در ساختار جمهوری اسلامی و انتقال ثروت‌های عمومی به مجموعه‌ای از املاک و دارایی‌های تجاری در خارج از کشور، خود، مقام‌های حکومت و مسئولان ارشد دفتر رهبر جمهوری اسلامی و سپاه پاسداران را ثروتمند کرده است.
وزارت خزانه‌داری آمریکا همچنین شماری از صرافی‌های کلیدی وابسته به حکومت ایران را تحریم کرد؛ نهادهایی که سالانه میلیاردها دلار را به نمایندگی از بانک‌های تحریم‌شده ایران جابه‌جا می‌کنند و با استفاده از شبکه‌ای از شرکت‌های پوششی، فعالیت‌های مالی حکومت را پنهان می‌سازند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از وضع تحریم‌های جدید گفت مجتبی خامنه‌ای «در حالی در انزوا پنهان شده که حکومتش در حال فروپاشی است».
او ادامه داد: «وزارت خزانه‌داری همچنان از همه ابزارهای خود برای جدا کردن او و دیگر مقام‌های ارشد حکومت از نظام مالی جهانی بهره خواهد گرفت. ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76924" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=T1FJfTeqZRKPR7CXBQJI_gMdHpx9oVY-16phgTlKICAGUDPa2PZyCmNSqg3ubD4QvZzHbx3J74sN68SR-y-23iwye-ckqqSD6VcZ8KiwliIh_IrSTXI-O8G47KU1YXeZ8RSmLRqlcC_agvlWb6vSvxPZuXBO7VfNRnCcDUHSIkqsR3ci3FdCvZE6WQx-n_2zgZZcC_0HD4DXq6avqK4n4vW-67tcbWJva0h3DKHJZfEibZSw3hP-quIxK9QMc4ozajAJareiYFv7P7LaURdFuBjduzhWh4H5WfrcvRuGPwR0WAEQtmLCA4Jn7GExFwQYY9mGfJqNjPpRRsQ2L7yrTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=T1FJfTeqZRKPR7CXBQJI_gMdHpx9oVY-16phgTlKICAGUDPa2PZyCmNSqg3ubD4QvZzHbx3J74sN68SR-y-23iwye-ckqqSD6VcZ8KiwliIh_IrSTXI-O8G47KU1YXeZ8RSmLRqlcC_agvlWb6vSvxPZuXBO7VfNRnCcDUHSIkqsR3ci3FdCvZE6WQx-n_2zgZZcC_0HD4DXq6avqK4n4vW-67tcbWJva0h3DKHJZfEibZSw3hP-quIxK9QMc4ozajAJareiYFv7P7LaURdFuBjduzhWh4H5WfrcvRuGPwR0WAEQtmLCA4Jn7GExFwQYY9mGfJqNjPpRRsQ2L7yrTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رسانه‌های دولتی چین، ‌این کشور برای نخستین بار با موفقیت یک موشک با قابلیت استفاده مجدد را فرود آورد که این امر پیشرفت بزرگی برای برنامه فضایی این کشور محسوب می‌شود.
پیش از این، قابلیت استفاده مجدد موشک‌ها در انحصار شرکت‌های اسپیس‌ایکس ایلان ماسک و بلو اوریجین، متعلق به جف بزوس، بنیانگذار آمازون بود. حالا چین با انجام این آزمایش موفقیت‌آمیز می‌تواند برتری آمریکا در زمینه موشک‌های قابل استفاده مجدد را به چالش بکشد.
شرکت فضایی اسپیس ایکس در دسامبر ۲۰۱۵، برای نخستین بار یک موشک فالکون ۹ قابل استفاده مجدد را فرود آورد و پس از آن در نوامبر ۲۰۲۵، موشک نیو گلن شرکت بلو اوریجین به زمین نشست.
فالکون ۹ حالا حدود ۱۵۰ بار در سال با پیشرانه‌هایی پرتاب می‌شود که قابلیت ده‌ها بار استفاده مجدد را دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76923" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrrf2LxKaLSCwRgiimpbIIi_BlWDv8zPSjti_fURYrsri_6ECNc1jehipn61g9gc01b--3m-zyE6L_s5w0XpbqohPVZBKH-hEvbD9PQTO8vCTFBFeUNDpbyn1Myr3LW8YU3vpRqFc-l6pPu4OPUtPVSsqIbNcrJCveN4hL4HdD6mcewfg3rq_1uXp62N2YIyHQQOF9_eEQU0vn1mVKUsJUrzeYA02gHjAUkJc4BX7UelNHhKm8SrAx-Z5K67Ch5euj6wciUb7XZC0OTEpuosaiaZIDTMFCofYMz21k_aFGAC3Nb5OjjGAFoFJBLK-hA7ypBC1yDMJ9b34nzzxlnpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=Y-A2gjwccdPPrzazEIY4J-AAoWIMd6X_XOT7z6bje_DfxOnaFSPUoGVa1Q08KeA-gQJEIaX0IxWuhAXwMWpjfIqRKththrFiyTY_QC_mFA85IYlvW_J3tanTSa1ZOuocnGfxfu-2ZUgy6tiHAd7x7RSVDVw8rCD8HH6FxizOqS0XycTi1AQ5DDJdRQOAcv4qVB4N7BGtqdnIBaWMLKVpwZlCik6KBbO2dpZkzEWh1pFTcScvSa5PBiF9ZkrTsypRIR_5eM9PG5KtInLh4-ZSCIirXLErxgGQAtYqYfdjPSVx5Bm7t0yw650w_E6gf0plFTmGEu3K4CNghWarBRcyyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=Y-A2gjwccdPPrzazEIY4J-AAoWIMd6X_XOT7z6bje_DfxOnaFSPUoGVa1Q08KeA-gQJEIaX0IxWuhAXwMWpjfIqRKththrFiyTY_QC_mFA85IYlvW_J3tanTSa1ZOuocnGfxfu-2ZUgy6tiHAd7x7RSVDVw8rCD8HH6FxizOqS0XycTi1AQ5DDJdRQOAcv4qVB4N7BGtqdnIBaWMLKVpwZlCik6KBbO2dpZkzEWh1pFTcScvSa5PBiF9ZkrTsypRIR_5eM9PG5KtInLh4-ZSCIirXLErxgGQAtYqYfdjPSVx5Bm7t0yw650w_E6gf0plFTmGEu3K4CNghWarBRcyyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست افتخاری برای حذف صدای خود از آلبوم "بدرقه" [بدرقه خامنه‌ای]
علیرضا افتخاری با انتشار ویدئویی علت این درخواست را ضعف فنی اثر عنوان کرد.
این آلبوم با صدای هفت خواننده از جمله محمد معتمدی، پرواز همای و ... به مناسبت تشییع پیکر رهبر جمهوری اسلامی ایران، توسط شهرداری تهران منتشر شده است.
Koronmusic
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76921" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=MlTHs0WuoQqkGlGSedYkW38Eq6mIeGCKHDlHIgOaoVcbqA1gWT8KifPP735Xw-BNNim4MDKoJnltckOou7h0KdVWcLsnIVqtz3iR56QvNHDkXC0mTzV5wc7gehz55lWiENYYIE690ewuKWh_Nui3rDqNyrE8b1TCzYEU_AO_2yxykI9k29Hj_bSRZI34ncOstBtBvRC33uYeJFwjyUbR9tWLezlb4ydFmvo0f7WwRdjdBRl9FILRy0b-bZgzKKVCpk27gq5d3Z9_KyrQjaxangdgWMBdcZG-t6EpZ__acKP4rRMnBaSHa4GR9BM0pQE3VB7NJ6oqIoGVjZ6nkzSuBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=MlTHs0WuoQqkGlGSedYkW38Eq6mIeGCKHDlHIgOaoVcbqA1gWT8KifPP735Xw-BNNim4MDKoJnltckOou7h0KdVWcLsnIVqtz3iR56QvNHDkXC0mTzV5wc7gehz55lWiENYYIE690ewuKWh_Nui3rDqNyrE8b1TCzYEU_AO_2yxykI9k29Hj_bSRZI34ncOstBtBvRC33uYeJFwjyUbR9tWLezlb4ydFmvo0f7WwRdjdBRl9FILRy0b-bZgzKKVCpk27gq5d3Z9_KyrQjaxangdgWMBdcZG-t6EpZ__acKP4rRMnBaSHa4GR9BM0pQE3VB7NJ6oqIoGVjZ6nkzSuBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">PapiTrumpo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76920" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TtTGzwasm_2H30Pv2Et440uYGG5OGrveVzpkTR26OYpH3EgiU7taNnxcvWy5MHKrx2Kc9xL9oDZ1Q2oaw9zgVqtjcEDPztaDk0Z4I1JDRHDdJuJNdnjMpIxRWMdKT6G2S2crp4rVufgSXXGc--WYs_0XTSsM_GzsqUI6nbiUYob0XNRyrzEcBGDcexagTZxJiA1A0q2YL1KnCCzbCQu2yw3l_UcJ8rEcVICTMp6QvI8nDSxkZQljw13KCUYlhoS6TByDkcE8E1WTKThUion7TLGFce2VeOpuXIFfLo6nEwS55aeZxNPD2HE7FZ-ZMhBKJhJQyqK6LGxl22hzKyPXxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع آگاه نوشت که دور جدیدی از مذاکرات میان واشینگتن و تهران، احتمالا هفته آینده و شاید در سوئیس برگزار شود.
مقام‌های جمهوری اسلامی تاکنون در این خصوص اظهار نظری نکرده‌اند.
همزمان دونالد ترامپ، رییس‌جمهوری ایالات متحده، در تروث سوشال نوشت که با درخواست تهران برای ادامه مذاکره موافقت کرده اما به آن‌ها گفته آتش‌بس پایان یافته است.
@
VahidOOnLine
خبرگزاری فارس:
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76919" target="_blank">📅 19:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9dU-ulT55OKaa4L0xdl0Gr0EuLonyDdTCIJBhtxfY6YP3fREEQDfTE6Hl623Mq6mTsdqssykjfgOabtKbj_EJCLFSdOH1EleXMGv2ZUDw7oJUPmBOowalvUGRW2LljyRbWY7fgrzFdaZhciZv7mFQRC9x-2bJGn232YKM1Tmh2QozsqhxcogDZBoOwYO5lT1WJp4FMgV3LBms0kglOQDZlKbPexMIRdE8EtCsHd69MiWrDddao2ONIEMHZ2zlBf9BXulTKDqq685ZavXGrhG8SWjMrs7gcVdUYymcahj_7kdZb_Rwn4k_5jIe_cHjrET9fGoJT3KhlwbRlVXjqnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگویی با «نیویورک‌پست» اعلام کرد که دستورات لازم را برای واکنش به هرگونه تلاش احتمالی ایران برای ترور خود صادر کرده و در صورت وقوع چنین حادثه‌ای، ایران با پاسخی ویرانگر و بی‌سابقه مواجه خواهد شد.
ترامپ اظهار داشت که مدت‌هاست در فهرست ترور تهران قرار دارد و به همین دلیل دستور داده است که اگر اتفاقی برای او بیفتد، ایالات متحده باید ایران را «به سطحی بمباران کند که هرگز پیش از آن ندیده‌اند».
او در پاسخ به گزارش‌های اخیر مبنی بر هشدار اسرائیل درباره طرح ترور جدید، با رد وجود طرحی تازه تاکید کرد که ایران سال‌هاست به دنبال حذف او بوده است. ترامپ گفت: «من از مدت‌ها قبل در صدر فهرست ترور آن‌ها بوده‌ام؛ زندگی همین است. امیدوارم دلتان برایم تنگ شود!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76918" target="_blank">📅 19:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjqqqCP4g1pqeT1UI4wvVOA-eeFwDfitj-e5VcqUKjWPveH35daCxN9WEGTn1MTkQNwCeLGWfr-OJuhD6IvIr2RsLXqIfMn9oVnWeW5Ml-8g5jYVhPL-WXsKQcuYZkFeHVLYWdbtnTz2pa4s40G7IsjJ7IDxQhbWdmHqRNBBMmE9GB9z7XYttysTTwCq2WK0Zb9i0TpzM28QnDrzbok17gPKsB0R9zItKfbsx6O2O_zru2pzug1oDpgZldJYCQ_mausUoux6f0FmunpYX7S8TtKbAb1PUube17KQidFOp-cTBpTKxCYqxvH8xr32fGh58mcuil5kD82RjODQncZAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه اهواز گفت: فریاد ملت ایران انتقام است و از هرکسی که موشک و پهپاد دارد می‌خواهیم که زمین را از لوث وجود ترامپ پاک کند.
احمدرضا حاجتی  در خطبه‌های نماز جمعه گفت: سایه حکمرانی رهبر شهید همواره هست و آن مشت گره کرده او بر سر آمریکا فرود خواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76917" target="_blank">📅 18:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv4NeP6HTqGqHE7csnxaRyA3sM-b2I-XQWX_4iHFTkSJrdSDxLgB2M7hSzEbrwD6toGy_VKPysRvpVGByuAdIvH6_R1wnQVeZNlHeSfooSh_S6dbAvnk5BRVz5mbNoPnqXXVlaS7cxrKEH-jY2MqgYrZdVNSbtSS1d25wc9HpevoKHh8TKgC0Tzx9Dmf2wXjwOIwQpx5SZJyXyCPJ2O1zrIblsGiKTsGM-zhJ79Nxv8peM-GGwc-jhYHaevDjfIQTR3WMkL4CAWVPztNxWnjodOnEbPEdvwFBJNZGNKb7JDoe7IUXkqmDkPyv_gKpS5ajUWEGyuWMGIy898z76IgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره زیر خاک رفت</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76916" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p_mXXAFHuoULSp0_mc8Jc6-DmQLUpiyLJN1OViZFAcC2_IbhGxca_Y5KGvxOAxosZN0T-lLeqTrwxtC5jaUwYzGNitR80ddCH4yTQx5xzZXxhcih_Zy7ANcw9rdaQd13hfToPPg_bx3C0Nv5tK-Q0KrLoufDrIRDueoColhRecNQhBiJBV2_8yMdYwCBxJRUipVEIv7vWnDzvcbpQg3k5Ft6F_Bk5Y4EPX_0atW7VjKupKwaDi44idfiJNWqU2R-mvQKY222bVpR3mpDYib2iqP83iiBKhraQT7niTUpa7b3jrqBHGCk93X4K6Y4teyAO7IY_pajJoiBy08m9DHJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران از ما خواسته است که «مذاکرات» را ادامه دهیم.
ما با این درخواست موافقت کرده‌ایم، اما ایالات متحده به‌صراحت و بدون هیچ ابهامی به آنها اعلام کرده است که آتش‌بس تمام شده است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76915" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VexQFPWBaf5r3tBKtqriZH-XJdFzxPOG3sH1tL-vQjAsKhHuMUIQhP1O5RZYnFzbxlMFKeosVXcQShp9O2OQtLwyCHY4LMnBAdRmlNr8GS3FH-9RBnJXAUdTH7CbPYODmcWX-SwjgemlLj_PUdEHj6PNV83aX0REtw7WcjaYp9B03gN-uHEnz5FlUGkflvYpO6A4yEkwV2w97kWuKnKvIuUQtEV9YhMH2r8hNwSDmuTQC9LaX-JoXaK1cKfGH7b6ZtldNSdd-N06SCXTi_4-i8o1fIvsBDOcUiXp1NWQW4fcBMjt4Emd_VVvOSL9P-icnicknSXkvQnl9dDGs1p-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت اکسیوس می‌گوید قطر، پاکستان و چند میانجی منطقه‌ای دیگر از جمله ترکیه، مصر و عربستان سعودی در تلاشند تنش میان آمریکا و ایران را کاهش دهند و مذاکرات هسته‌ای را از فروپاشی نجات دهند.
بر اساس این گزارش، با وجود آن‌که دونالد ترامپ روز ۱۷ تیرماه تفاهم‌نامه و آتش‌بس با ایران را «پایان‌یافته» اعلام کرد و دستور حملات هوایی داد، دولت او همچنان خواهان بازگشایی تنگهٔ هرمز و پرهیز از بازگشت به جنگ تمام‌عیار است.
یک منبع منطقه‌ای گفته میانجی‌ها معتقدند حملات اخیر ایران در تنگهٔ هرمز احتمالاً از سوی عناصری در داخل حکومت ایران انجام شده که با تفاهم‌نامه مخالفند و قصد تضعیف آن را دارند.
اکسیوس می‌نویسد مقام‌های میانجی روز چهارشنبه تماس‌های متعددی با مقام‌های آمریکایی و ایرانی داشته‌اند تا ابتدا بر سر کاهش تنش توافق شود و سپس تاریخی برای دور تازه مذاکرات فنی تعیین شود.
یک مقام آمریکایی نیز پس از نشست ترامپ با تیم امنیت ملی خود گفت دولت آمریکا همچنان به یافتن راه‌حل متعهد است و گفت‌وگوهای فنی برای رسیدن به توافق هسته‌ای ادامه دارد، هرچند واشینگتن حملات ایران به کشتی‌ها را «اقدامات تروریستی» و نقض عملکرد مورد انتظار در تفاهم‌نامه می‌داند.
@
VahidHeadline
خبرگزاری رویترز روز جمعه ۱۹ تیر به نقل از یک منبع آگاه اعلام کرد مذاکره‌کنندگان قطری برای دیدار با مقام‌های جمهوری اسلامی و با هدف کاهش تنش‌ها و فراهم کردن شرایط برای ادامه مذاکرات گسترده‌تر، در ایران به سر می‌برند.
بر اساس این گزارش، گفت‌وگو بین دوحه و تهران «با هماهنگی ایالات متحده» در حال انجام است.
این منبع گفت که هدف این مذاکرات، رسیدگی به اجرای تفاهم‌نامه میان آمریکا و ایران و همچنین موضوعاتی است که موجب تشدید اخیر تنش‌ها میان واشینگتن و تهران شده‌اند؛ از جمله اختلاف‌ها بر سر کشتیرانی در تنگه هرمز.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76914" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZpMNRsDoW2tG-t-4d0DP0r6V4Y9vob4FiczV2V4mdqwsbRVdP9JX3Rv8EY5hXKjWZzwk55acmGQyTYfRJm62Fkz_RLlMaGc34h-v-hU8u93iTV6hRHCjfAQCYi4Sai6l3bMvHqo4feGYGlsq4LyBwDIm2U_h9AXOZnJcpSA0Clbdx9GKJbLKmu7EnvO5Is01j53KyA9y9LpuAIHIojlHLpGxyqx0InWB1bRVIc1zb5IOK0PYnwVEWzhiPRlwCoxIKelMpHB7Iyj0kbMdHfGTNU8QlPl56A4TrsEG1IaEF1HsuW9MuXpEcbbN5MArS63--dNzV6XAHYP8XVw-_9jCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gQtoh-9J0h4mpUSkQR8Lk33KVvzT0kd3SfWIfXPIs3XDE4FWqrcgWKnYVjJCaa3_k5Pl_SjD6xJdL5taR_vJxEUpjP69D5NiGBYd04ThvE3ax1w6cT-pTyjWJUyumvBOt3dF0mDMcePu2WAafbntzz4S_-iM9gH45tBxQ5C1g7RkCCMelTTnXabGa5pSk44FGGMY6r7WcCKI1GCMQF-YpkACH4K8Zw5jJ84ilVwLGCUVJNwf7J2erFq2dRGXiZthkP8ZTiwIPN6jUYPTdSsRJwko7q-oloczz7Zq9P1ANjOnTRjlQj10jVpuX4qpSe5591fyq8AoB_xD1XUaspUxjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش منابع حقوق بشری، نیروهای مرزبانی جمهوری اسلامی ایران با شلیک مستقیم به خودروی یک خانواده در روستای درکی از توابع شهرستان سروآباد، یک کودک ۱۵ ساله را کشتند و پدر او را به شدت مجروح کردند.
به گزارش هه‌نگاو، غروب پنج‌شنبه ۱۸ تیر ۱۴۰۵ (۹ ژوئیه ۲۰۲۶)، نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
هه‌نگاو گزارش داد که در نتیجه این تیراندازی، سام حسنی، کودک ۱۵ ساله، بر اثر اصابت گلوله به سر در دم جان باخت و پدرش، احسن حسنی، از ناحیه ران به شدت مجروح شد. به گفته این نهاد، پیکر سام حسنی به سردخانه بیمارستان بوعلی مریوان منتقل شده و احسن حسنی نیز در همین بیمارستان تحت درمان است.
شبکه حقوق بشر کردستان نیز با تأیید این رویداد از تشدید فضای امنیتی در مناطق مرزی مریوان، پاوه، بانه و سردشت خبر داده و به نقل از منابع محلی نوشته است که نیروهای مرزبانی و سپاه پاسداران در برخی از این مناطق، ضمن افزایش حضور نظامی، محدودیت‌های بیشتری بر رفت‌وآمد روستاییان اعمال کرده و در مواردی از دسترسی ساکنان به باغ‌ها و مراتع شخصی‌شان جلوگیری کرده‌اند.
تیراندازی نیروهای نظامی جمهوری اسلامی به سوی غیرنظامیان، در سال‌های اخیر بارها به کشته و زخمی شدن شهروندان، از جمله کودکان، منجر شده است. کیان پیرفلک، کودک ۹ ساله اهل ایذه، در حالی که شامگاه ۲۵ آبان ۱۴۰۱ همراه با خانواده‌اش در ماشین در حال گذر از خیابانی در این شهر استان خوزستان بود، هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و کشته شد. در این واقعه پدر او میثم پیرفلک نیز به‌شدت زخمی شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76912" target="_blank">📅 17:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GNrlrfUof581k4N3z6JOMSqJu55_5U_KwhFfO14IKacSV9C4ORWcbdsH0jyqA-Up5djaTNsOCV31W877BGkzrnj57n90R7-CHrNpySPhdQY5t0rLBXO9Ec_725IUisarD4Eu_-ZsQZixJNU_-F-4cEh-2x1lFrzNpApiBmRGCmstVuADgTyp7g7DMmQoBJQcxmaMDFmx0lSDkDgGFZuH67XOCWFNgA0GImawj5x-Yfbacbt47WNp11YjQFHxiXXnb79BsJ0rf2xHXPeoQFLf1vx34OBtgW4ifY1aUvkL2W1h5s3LPf3KiNgPpGocqusdNSePIZueJX_BP3XmnpXc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از دو منبع آگاه گزارش داد اسرائیل این هفته اطلاعاتی را در اختیار آمریکا قرار داده که نشان می‌دهد جمهوری اسلامی به‌تازگی طرح مشخصی برای ترور دونالد ترامپ تهیه کرده است؛ گزارشی که هم‌زمان با تشدید تنش‌ها میان تهران و واشینگتن منتشر شده است.
به گزارش سی‌ان‌ان، یکی از منابع آگاه گفته است هشدار اسرائیل در هفته جاری به مقام‌های آمریکایی منتقل شده است. منبع دیگری نیز گفته نهادهای اطلاعاتی آمریکا در هفته‌های اخیر به‌طور مداوم اطلاعاتی درباره احتمال تلاش برای ترور ترامپ دریافت کرده بودند، اما اطلاعات ارائه‌شده از سوی اسرائیل جدید بوده و به یک طرح مشخص مربوط می‌شده است.
سی‌ان‌ان نوشت جزئیات این طرح هنوز روشن نیست و همچنین مشخص نشده که آیا دستگاه‌های اطلاعاتی آمریکا نیز به‌طور مستقل این طرح را شناسایی کرده بودند یا تنها از طریق هشدار اسرائیل از آن مطلع شده‌اند.
کاخ سفید در پاسخ به درخواست این شبکه برای اظهار نظر درباره این گزارش، که نخستین بار روزنامه وال‌استریت ژورنال منتشر کرده بود، به اظهارات اخیر دونالد ترامپ اشاره کرد.
ترامپ روز چهارشنبه ۱۷ تیر به خبرنگاران گفت: «آنها می‌خواهند رهبر آمریکا، یعنی من، را از میان بردارند. من در همه فهرست‌های آنها هستم. امروز صبح دیدم که در تک‌تک فهرست‌هایشان قرار دارم. تا اینجا کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد. اینها آدم‌های شرور و بیماری هستند و باید این سرطان را ریشه‌کن کنیم. سرطان را باید از همان ابتدا از بدن خارج کرد.»
سی‌ان‌ان همچنین گزارش داد تنش‌ها میان آمریکا و جمهوری اسلامی در روزهای اخیر، هم‌زمان با فروپاشی آتش‌بس ۶۰ روزه، افزایش یافته و دو طرف تهدیدها و حملات متقابلی را علیه یکدیگر انجام داده‌اند. با این حال، به گفته یک مقام آمریکایی، تلاش‌های دیپلماتیک همچنان پشت پرده ادامه دارد.
به گفته چند مقام آمریکایی، برای انجام حملات احتمالی در شامگاه پنج‌شنبه آماده‌سازی‌هایی انجام شده بود، اما مقام‌های آمریکایی در نهایت ترجیح دادند فعلاً به جای اقدام نظامی، مسیر دیپلماسی را دنبال کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 502K · <a href="https://t.me/VahidOnline/76911" target="_blank">📅 02:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHSimfwkPwvIRxCDtFevuhutKdLLxaCh2nm_5G8BESnVMGQWLzaeJQq3xhlyzyGLPIJhLEBPxifQA2A5yxoh90jTyOwXXbSgzxqhP0ae-qOmNRbByTb7yQ9zwmpTFaghI-yB2dstMS4zplqDBbhORspC24g8TZuP_uOeGwM5gagFt5nOpS91bXx-BM6RGFPWSruTW4ZthpWb6IxNJaOQX78LPDZ_TULJ8fP3uqus7EctjwScEXiBDl4vHbsJ555k4Qsrp4BB-he01zBSgDhuEnsn9hwTQgIhKI0SJBCXnvkETDnWj2biVUuHxgbJmB73XCKDyfGO_6Z1hpWS530KYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 495K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P0oRzq_573A_aYqbFPY0RqaNVGdPvJnVZddpCxth4qiKuyWOkbAgHEpOP4wQP3SDjwy7aH_m4ig_BtEQPM11mjcxR7Vhy-ob9RO0ecCEbOJG2M2AG-AYHIbFRNew_TU9TyLiHldikvctWF93p8WZoUWHDzOv3MawzZsOLOqhT-0A1ZAJVHzlYSgZcHU5fBlaP9xMJTHo3S_k7oaue5FN8qeTyyQpLJTtZua8P1SncIgSD0TxmAhO-qc5UCvQwkGetHoEC7YPP5MKS6V_j5HC01iWxKHvoayGsxfqGbymlLr065qXvI4B1M8fkHuolRhSXwe7-6xMFsyN2h-L5_hpCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/roVBb0RZzExTEz6t4h_Xvo4qc0sC-L0c2vxObR0BywGwvhdAOLSJzGWmeSeP_LlRq8i2GLdvPQ0kEB3W9ChZpLQnFhmD9BGYD5VrdIpCZCAprYdi4zqAb00tqPotenvDzbcrPwZGvjMI1WcoIMJs89Wel4P-biOxYlgRFPHN4G1yXyrYZkSQzLtwfJcEwX6UAjJ58TGN85hYMyyUq96srrPVQkobz6jxnbrskXK7_h8e3qeIdY4uDFLOgdminmaSPx5g8hg4FWkk7fBBveOGWrHq2-oTOY5fjRe8IitmtZUO955YDzPBJWPP1Tjfbi1dqErndoxEoSymoYXREDUABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DKcXGInj9j7r01PQWznYyKigXQ_2SPLi-vmwn3-_GjAOfypVbph-xm56yfBiR0V7xMMqYp6L0Dws8_fggDTx5mkfPXkqFx74lX6AyZpvN8SGzeZ_U_YPsbJCrjKN3RecD0widK24NJ1obaWrAPlgrsrX15_ULBWYdpiPkbyXVjyQOS3m3CaorvYqltMtmUoL9P9tKoVcINlxuQMNRsNgGyPrYjrHe_Q-OmNli_ehNxYwSpRkuQYC2WeHPL1mopsEgor8AvWmZgaKuDwL6d6-S2bu3o5mcR48yskA-wBK-lO9z5tvoixL_MmqWM6BO2MVNHS9MLYZooVPshRVFoVG7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری جمهوری اسلامی، ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان در غرب مشهد و کشته شدن دو نفر را تایید کرده است.
ایرنا گزارش کرده که امیرالله شمقدری گفته است این رویداد تروریستی نبوده و انگیزه اصلی وقوع این درگیری در دست بررسی است.
معاون امنیتی استاندار خراسان رضوی به ایرنا گفته است: «براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده‌اند که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم، نفر دوم نیز جان می‌بازد، هر دو نفر با سلاح گرم کشته شده‌اند.»
آقای شمقدری تاکید کرده است که حادثه در منطقه سرافرازان مشهد روی داده است.
او وقوع هر گونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم امام رضا در روز پنجشنبه را تکذیب کرده است.
ایرنا اضافه کرده که بلوار سرافرازان که تیراندازی در آن رخ داده، در غرب مشهد واقع شده است و حدود ۱۷ کیلومتر تا حرم فاصله دارد.
@
VahidHeadline
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 526K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5Zz3xYTOqPKgecQEky6VZ-3ymc8HX2BtVPAr860Q5QkbNPmsDwnuatR61ZwRHK49kx38oXaFz5C6_ru0YUvvLeFwZgjobU1gHDyDvsZUkNyV42pYGMN9IaVXDBHmT16-I32O7tpHIGG2lZ5AUq8BSN6fLIVGtxLN07AyzrV16r3dk0-0qmG32kM91eqfL1Zjv7U9MJFbWN7SZSexibbSjzyHZTQXL6Iqeh6PsJbxcA3JmOK7HPP3pVmElEmMrFFIzEa_IbS7UiTeivtn6wbs80X8JPbY87w39LcErtyNwOq6m6qaH6uIv-M9YXvPaAIHPJvRpLs9jOIodEiNziYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
فرماندار کنارک اعلام کرد یک منطقه نظامی متعلق به نیروی دریایی در این شهرستان شامگاه پنجشنبه در دو مرحله هدف حمله قرار گرفته است.
🔸
محمدیونس حقانی به خبرگزاری ایرنا گفت این حمله توسط «جنگنده‌های دشمن» انجام شده و نیروهای امدادی، امنیتی و دستگاه‌های مسئول در حال بررسی ابعاد حادثه هستند.
🔸
ساعاتی پیش از این نیز معاون سیاسی و امنیتی استاندار بوشهر از حمله به یک مقر نظامی در حاشیه شهر بوشهر خبر داده و گفته بود صدای انفجار شنیده‌شده در این شهر ناشی از فعالیت پدافند هوایی بوده است.
🔸
این در حالی است که صداوسیمای جمهوری اسلامی پیش‌تر گزارش‌های مربوط به وقوع انفجار در شهرهای جنوب ایران را رد کرده و اعلام کرده بود «تاکنون هیچ انفجاری در جنوب کشور رخ نداده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hywWd0Nl6pjZSzJAB6C8FtIPGb9pwSktC4KArXBNQNZx5fPGGiFdA0fgOYdqGhVWnXYuXUFVRn3Ikfnxh1X0cz-Co2TU1P5_Fd33ndWAyeaf8902kk0yRGZ0sd1Yc0qMQJQH8EkzvAk3-T59Rgw48CqPtuZNRi2X0hYpeVyxMySw2LATS-uRbvkN28bBDL3TLCj1DJUqqqgkiJFCa1zW_s6Iid6o6Ep42F9FEDEQTQsJ-odygZzItilU4b5bssrQ7CtgSzakSOR-bKzD9oI6Zc5WUaP9g-WTSa4T7q_jrAzLZnLKmnJUf8ta8dfGhSTj37Qv17td_7TcR0w3l-59ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ایرنا به زبان فارسی سخت تیتری درباره صدای فعالیت پدافند نوشتند، می‌ری توی متن خبر می‌بینی نوشته:
"لحظاتی قبل یک مقر نظامی در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه دشمن آمریکایی- صهیونی قرار گرفت."
irna
به نظر می‌رسه از روی صدای انفجار برخورد پرتابه، مدعی تشخیص کشور پرتاب‌کننده هم شدند.
احسان جهانیان، معاون سیاسی و امنیتی استاندار بوشهر، شامگاه پنج‌شنبه اعلام کرد یک مقر نظامی در حاشیه شهر بوشهر مورد اصابت پرتابه قرار گرفته است.
همزمان صداوسیمای جمهوری اسلامی خبر داد تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujnVraq13dCqsq5Ne21L-nXmfGvX4e86lIeITbdbsboJC34pmU6sTV6-NQiMLAzotUCLR3PSSDXE472XF50NcDQlVjRSwDIzHO74M5Nm-9adVbbs5-7oGfyd9Mkj8iNUeQFXdseVMx2U5XW92jc4-ejfeeupel0NLngkg-KOJN6Eero0VDctT-hqzuKPDFmg_FypnKBhSBzhIKoyAP964gQyzWWCML-7_3CI3qIkJUUJI04BxOpvV8Tb05hReT_GTWDPQ2ThCRu-lq4yyvSgxecS8inUnemCGi5lTdaaHH6aB2XFXu4XCgzadmkEuTh-0q-lvmZWwUmzYo1jwFmpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
همزمان آتش‌نشانی اهواز اعلام کرد انفجار شامگاه پنج‌شنبه ناشی از «نشت گاز» در یک ساختمان مسکونی در منطقه حصیرآباد بوده است.
@
VahidOOnLine
صدا و سیما بعد از تکذیب آمریکا:
برخلاف برخی خبرهای منتشر شده در  فضای مجازی، تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j-8bTc_8IMnqMGfrpECAVR5wsR_IlO59FOCC8xxNjlRK_Ot7zJW5CVfhhQyavvkO3yHRv8uYJo78SDznv0U2WibtcZDsBviD4q9PHCQ1HboxdAdORpzZhN5SaZnkAT1y1XYFi2E6yVUyvACSvNSiJgFK4NfI3Lc7cik16Wr7gLAFNVsxg6ps4cZyTrI9Z0h39BG0JCEj9-yXMpHyk91LM9R0e2CgOKJcpWoWFn0K52zPe3OTIznhHnt0e5_b6DHfEcRRja5unae7ilNy0wwa0g-mdGJGRhaEjM3QI8JgD3ghgkVUSiI7P6nsgXIEP4rrr4A6nOdkITSBkgxxZlNM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZ-slCSNwZ_T7b-Z_-7DqyFaHiQKgfutaYGBKf-nNYmynP1L06NQc56463AH1Ds8lpd7-o1ALEVEJ7bklzck2PWF9oJvzrv7NmGubzC_q9KYg_A0rMQi9x56jfP311E_tv5dJRO1FTSd45CPyScJLjZVIhn8jdeCOsNaZpKsx5E8yykmysTiULSI7p78B13OOKY-oLs0IjCIpTIvlo7WbJLnY45cSbpzw9OCyGYw9XRKunbU6xaT9jm97XtTU3wq6RhmCpbkuM694-2tCAhUDoI7AMFGB_49ooBNov8CS1l3UxK_0Q2TIlg7SVccY-ScOeQ5oBH2BbalIILhChxJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6nhoj2zafqU1JG9Ulg5fTpMLw_kW0wCcQaglerm0SwG1GG4LPFganI1l1gOKAo3OQAiXt0uzL9zG6_nX0Q76ucamV61jTPgCwguoiMkUQLUQJPuTDIZqslGoQhyKCYiMKMl-ci2JvEZqMY-GPTrCgsddaDpAzTjL4BUJObxrSXPkFHb_QfeNAsILFIF5_kRZIYiydmmU3DikARIU1eOKiIKui_m92Ek3M6k8yEg32I6UF5hC20VlbMLlNRW99JHVmTTkFb0pO5gRCcbajgtBj27MXu8J2AIopN9d6fpWjqPTOtayY7eUkxEd8VnaBYnxYMzbxWcDIU7U4uI2e43dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t2u32qQcgu6jy1lNP7Gwny9v3uh5T0MhGCxZ9EEeJvENaA1detRiAAzYKRrismRjdCcuodQDs-qIxSQnq6aC1ahh7zTg4KrMvTCGFiPjoOVSimR8jbPlKWxsewpBhXByShULUJk4-1hJPrMU2huPLrC85IT_nyeDhqym8MGATf00-mFCP0e6fKoxKZKZ2S4KHDbNym_KiXShWCmvep7zYvWHsYuTBfMKX6lHN3pSa_9oulqhRfGB74KFqhXwvhATIWVkAm81sgtj2Nzq_OLQgjitjtwbwxQ35eHjcfu7TfPIvIKCZIe9iptTqbtrzhce8TY9hyLqcLqKh7DUtcoyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lAyy2n0zyWhLBl2QEeMZ5Lgs3f8-q9W65Ojw5xXcV9xz7yYY0iwXTA1Ve3HCWOLJissoSG0l0VwwS--fiA8ospYAaCKGtdECXT4rlf9ad-Hher5C2TuEANsw7Y2XR7e50cZZg0U-D9Ku0FSmVsMRXMnQAFgpBJ85OQO8iNdm6bzJHCqTLlyV0qR4tr77hrh1mVDKfQGXVTF1MSvwRANXSJ2WQ-m9QgyqPIvxEG-SfRXtP2un66Y1gpT0LKDq3Q13OUD0okkLft7aTxojqWt0Bq4BHb4E2h7i8evMBZK1_kO7qUC9Clt5WuVO0VB2KemAdnCnWKXoAf3W7YPXibWL2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک‌تایمز به نقل از فرماندهی مرکزی ایالات متحده (سنتکام)، نیروهای آمریکایی در طول دو روز گذشته بیش از ۱۷۰ هدف نظامی را در امتداد سواحل ایران در نزدیکی تنگه هرمز هدف قرار داده‌اند. این اهداف شامل سامانه‌های پدافند هوایی، انبارهای پهپاد و موشک، قایق‌های تندروی نظامی و زیرساخت‌های لجستیکی بوده است.
سنتکام اعلام کرد که هدف از این عملیات، کاهش توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز بوده است. این روزنامه آمریکایی افزود که تعداد این حملات، حدود ۱۴ برابر تعداد اهدافی است که واشنگتن در آخرین دور تشدید تنش‌ها در ماه ژوئن مورد اصابت قرار داده بود.
@
VahidOOnLine
سپاه پاسداران انقلاب اسلامی روز پنجشنبه ۱۸ تیر اعلام کرد که حملات نظامی ایالات متحده نه‌تنها «پاسخ کوبنده» ایران را در پی خواهد داشت، بلکه ترافیک دریایی حیاتی در تنگه هرمز را نیز با اختلال مواجه می‌کند.
سپاه در بیانیه‌ای اعلام کرد که تردد دریایی به ۵۰ درصد سطح پیش از جنگ بازگشته بود، اما «ماجراجویی و دخالت‌های» واشنگتن در تعیین مسیرهای تردد، عامل اختلالات فعلی است. با این‌وجود سپاه مدعی است که جمهوری اسلامی در تلاش است ظرفیت عبور شناورهایی که مطابق با «ضوابط امنیتی» از سپاه «کسب مجوز» کنند را افزایش دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tuX2bOAzFsKzBSXvNEdqNvoSNX_Ia-5X0ei6YS0obRqJwT9sWM0EGohC19dHikeoNdOxEKOoLSZr-dgTx9PLp3T5gUKmsQWGZV5T135KF1VsWqHRgiy-amJ-xWn7pPa_Jd0W1DdZlGqDJO8jx-97OJWrxW8y0ylGBu5bvAKfaTo0mRwsoUzzLt4MwrOBBGTk2mTwz6XanwrypIcwLXlOHyWT4zLBA4GI9Xlg9SUeQbtUaSsKzT44d-8hAcJtdln1cebOnPaJgu0r2vIXBNDMQrInnujPecdJQelcjIn33X-nYMrKrxDpJ1ic7B0Xr8ICRLI5EQKJ-0V2nY_HX1-cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pymIpr1smYrMGacSXl4rpRw_q7za1djh8NQtQp0K66gHdn2dGhuaHIc_LzPb-0hlnEgjO5x2A_oZFsX0JKwBrThG8cpBzEinfiGszDkPHGYAdfors-4eN4zCcuXXogYMZBL3DyjMW0cTbpRX2jfv231LO4p95p8q1gC_iy3chb3OR1ENXnqUcVykFdHj3ILAJEeKrIwkM10Wp5w4SpP1bFbllKUKdiXz1aOXi6HnB7RvJs2m7Eh8UduSAoNmJr96t1Ryp84QnDXxQykAlATB-SApkMRTNwSXYuLE69e90XIU6nBs-SSJx3yYiZ0otup27LExZnBLxElPHmBg-SrRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FamG8A6m5O3C84IjqKIYdf5Qn-3Wlz_XEY5YK7ElZwj8_J2hDZadin8bTQ_DnGGU6XLJF-r3FMMj8XbFKIeKnf-QhkLp0eahTiBV1jhFk7LvQAytIqaD3ogTMXEdoK949eHPyv45IMJu2bKmXjlvy_6jLtPNKb9JWNckO6hPIBUhsgYhVaT1S8hH_mBs5LOhXfPL8wXKCJU-49cCyj2v1ox_wOKsgItKKkCAKgGnPFtLJdBZA9x3pzeyrnVrtgDtwyU22sI7wJb3V3O1TEKy469IBgxkm5Bo5TSeTbWWD2CazXUPbzVKDJ0WCuta8gkHKSkQjovmK97bqu1vQy_wJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=IVgTbCw8aVQY80C-nh34QqXCET1DAYvmg7Aa9Lb5kZICZU2iE9mllCLETrmk2phmZoYgCJwuBf3gZSQ3mOAjAsydHU2DjgcqE0LeKy_feBgLfGK-1iXU2ICoYJpRaHO95Z1a3ZOZV14rR-XD0GIoiApTezZO5cSLjceTjSoe1P5NQiQemS7gSF0gEZicghfY3ILI9egJ5RoBOTQ_J7tiG9vZgQn6fKtMnRhe0r-3aVXPux4PmEZ-XHFe8tBV2ruSnlD-zhUy_NXNYmlqeV2IRoNS4grhsvJ_53lbfWAxq0BmX2H6cFsKjd5hfRP3yKq3NIq66ZaPwJX-JO0v4Xf07Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=IVgTbCw8aVQY80C-nh34QqXCET1DAYvmg7Aa9Lb5kZICZU2iE9mllCLETrmk2phmZoYgCJwuBf3gZSQ3mOAjAsydHU2DjgcqE0LeKy_feBgLfGK-1iXU2ICoYJpRaHO95Z1a3ZOZV14rR-XD0GIoiApTezZO5cSLjceTjSoe1P5NQiQemS7gSF0gEZicghfY3ILI9egJ5RoBOTQ_J7tiG9vZgQn6fKtMnRhe0r-3aVXPux4PmEZ-XHFe8tBV2ruSnlD-zhUy_NXNYmlqeV2IRoNS4grhsvJ_53lbfWAxq0BmX2H6cFsKjd5hfRP3yKq3NIq66ZaPwJX-JO0v4Xf07Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با ادامه درگیری‌های نظامی میان جمهوری اسلامی و ایالات متحده، روز پنج‌شنبه ۱۸ تیر نیز حملات متقابل دو طرف ادامه یافت؛ حملاتی که از جنوب ایران تا عراق، کویت و آسمان اردن را دربر گرفت.
رسانه‌های داخلی ایران از شنیده شدن چندین انفجار در استان بوشهر خبر دادند.
خبرگزاری فارس گزارش داد که صبح پنج‌شنبه مناطقی در استان بوشهر هدف حملات آمریکا قرار گرفته‌اند.
معاون سیاسی استانداری بوشهر نیز به خبرگزاری ایرنا گفت چند نقطه در این استان، از جمله حریم پیرامونی نیروگاه اتمی بوشهر، هدف پرتابه‌های آمریکا قرار گرفته است.
ساعاتی بعد، صداوسیمای جمهوری اسلامی به نقل از منابع محلی از شنیده شدن صدای چند انفجار در شهر چغادک، در نزدیکی بوشهر، خبر داد.
در همین حال، فرماندار عسلویه اعلام کرد بر اثر اصابت دو پرتابه به اسکله صیادی بنود، ۱۰ قایق صیادی دچار آتش‌سوزی شده‌اند. گزارشی درباره تلفات احتمالی این حمله منتشر نشده است.
هم‌زمان، رسانه‌های عراقی از به صدا درآمدن آژیر خطر در پایگاه نظامی «حریر» محل استقرار نیروهای آمریکایی در استان اربیل خبر دادند. همچنین گزارش‌هایی از فعال شدن آژیر‌های هشدار در پایگاه «ویکتوری» آمریکا در بغداد منتشر شده است.
در کویت نیز رسانه‌های محلی از وقوع انفجار در نزدیکی پایگاه هوایی «علی السالم» و منطقه بندری این کشور خبر دادند. وزارت دفاع کویت اعلام کرد در حملات تازه جمهوری اسلامی، دست‌کم یک نفر زخمی شده و وضعیت او پایدار است.
هم‌زمان، سامانه‌های هشدار در اردن از مشاهده چند موشک، پهپاد یا راکت در حریم هوایی این کشور خبر دادند و از شهروندان خواسته شد برای حفظ ایمنی، در پناهگاه‌ها یا داخل ساختمان‌ها بمانند و دستورالعمل‌های مقام‌های محلی را دنبال کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2NQFIIojNgoZe9snlqYR_-yxa6l2qjrRUnz4UkntMizCdtWuZU2OuEFjcIHsTchVtEarr1nCL7aGBTfcpFZt6VA2ktYRJIsPVjDOfplveyuyyyOJgpKv4e7AqloZcWIruSROJvAMCuIQmd8OR3tpiEXjkWLem1H9b_e1KDBXBrCnSRxVJb16c5g_d1063gtVDt8GVVLapJy97jiHaEs89UIlZi6QqQsNXKC0DdE4UPXaIUFWGKNK-ILUhc5go8TIyzQBF8fDcoSeG4DUE6BRZ9H4p7EjdjYBlj3LuR0WZ20Mh-lefpdo5u1XxV5gDUjFFCWKLSM9N_sVkeJ0a4PAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IItPBgkyVPipSXo-AxNWmcXiUHkC0jkEYqef9EGpXqTJY1bnwydXXfkNI9WwA6nyrL0RbxardKNOLQmZjdWfxxaNXrlqehc-yWAFO4j9Xo01-tKgqNxMWTgc30ZmGs7W1ZThoZxPgSAyhWBLk0cQyEZWg4391bZkEIuxQriyOTRIOwB4YloG15PZJZqRdOCNxabEMkh8kvkiiO2RiDxznrlBSmiX1jTEBOMBwBWM42hIEI7q1vbtyPpKX5uaOHGMHX5i0OFwDkoJeelcWiIQVb5P9j-neONJ9xNMkoPdqQeJ1YR5P4hXq0ooYpdLrrrlmua-2nR4-27FT8B5rSca1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fO0cMJ4Npc0PRCfgo6OtKT1fUoIUfnu5Fqtxqv2u4C_gbOPm23wrCH0CnKMfoOsBI98dqVfP6_mwD4MmmK_32oN3Aq0w5xtCgH-4R7lnidYKkis0t-pcZSsrnuMYtVjiCTvmfQRFUs1owVtapVO1WiMnF9kszJBJz-gFqvmNwFGmcTqFS0Ua8z1o2Od6fVbHOrBFBKUZdrI3d-T1p-QPh1UOSRs3OMMdySnWbExMPwT7gDCHD2DBWGd5CBcNwUAqckN7F3NTkDYeoJVmUYq-kSQWHPvpp42Z7Dw6JAq3Fl_7ETCNUxZiBeNswI2aTq_S19KH2_6GXygfOYk4cYOw4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 497K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=sgwXy2KXli1NydENbZO2qDOSNpwpJ-V_4hThwkO_26xj5wbgk0M0o_J5CcxMaJbfRTwzxroImoEk0M6pMaGypBJeaJl4MAzaRptGb6JPtXKNnsmYfnB5m33N-YdxIoE0A1HJZftTxZ5l6WKba2Qx-Fsi3MEnzRzx-jXfgqrTAytmoVExQnWAHjxG3NltPxHz1FAeEQFKPedaDL7mmIPLr-fyDK4PFPhBjTYEjvOsF1dLbJKVoaQpbuv5Znq1cXXdg59JZHFsdsaedpsIuVkFQ_XAjLBMzAfa5Cp75JD2aWrpcRscjydbOevIsrfadrpvDajo5-lXd3t-4NnkE7zcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=sgwXy2KXli1NydENbZO2qDOSNpwpJ-V_4hThwkO_26xj5wbgk0M0o_J5CcxMaJbfRTwzxroImoEk0M6pMaGypBJeaJl4MAzaRptGb6JPtXKNnsmYfnB5m33N-YdxIoE0A1HJZftTxZ5l6WKba2Qx-Fsi3MEnzRzx-jXfgqrTAytmoVExQnWAHjxG3NltPxHz1FAeEQFKPedaDL7mmIPLr-fyDK4PFPhBjTYEjvOsF1dLbJKVoaQpbuv5Znq1cXXdg59JZHFsdsaedpsIuVkFQ_XAjLBMzAfa5Cp75JD2aWrpcRscjydbOevIsrfadrpvDajo5-lXd3t-4NnkE7zcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 519K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=n0q690lQRyxzvl12_KEcQV_i0KBcec1QjL0JI1zbDON6mSD_0mj6fKWmY9ZucUCBDuujgQelnquETHBpqpiYMJp0HYZ6FA2CRR-jnb8hYCky6U2OxZEkU8hltZUaKTaS_oHGxqaka_DP39AxxCh97NiwEL05rZ2GrIW-oScElUKjuJWy9VOx_WP8Zf7ogLOHymU2KZX9oJe8s62pf-Qmk33z3DS9j_kxQXgKnZgf5zq6GWyPgVUZpe0nS6o8FTTeL6at9m5h4fo_NLQwESIP9pszxZ3BImdDHrfNVKPcYpdsWv8MFFXCoUR2ftNTZxWirVMBHxsN9yA_UvJnFmUuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=n0q690lQRyxzvl12_KEcQV_i0KBcec1QjL0JI1zbDON6mSD_0mj6fKWmY9ZucUCBDuujgQelnquETHBpqpiYMJp0HYZ6FA2CRR-jnb8hYCky6U2OxZEkU8hltZUaKTaS_oHGxqaka_DP39AxxCh97NiwEL05rZ2GrIW-oScElUKjuJWy9VOx_WP8Zf7ogLOHymU2KZX9oJe8s62pf-Qmk33z3DS9j_kxQXgKnZgf5zq6GWyPgVUZpe0nS6o8FTTeL6at9m5h4fo_NLQwESIP9pszxZ3BImdDHrfNVKPcYpdsWv8MFFXCoUR2ftNTZxWirVMBHxsN9yA_UvJnFmUuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTevLNkRaK7iGqgFOXN2etJ_5HxrFzGu_D_R2ycUaHrqxl3CVgRU1SshIhuS4PteI0WvSrpoHvm3e3DiAEMKr-STe4cN7HW-mUw3FEIcJd1ixodpeoVtEXTpmgTLL0xbzUYrET6DbQ3wrvoSp_edTjLpOjuRPlt9TB52yRFziQIx6a6IvjP858nHuRLj75vOM04wHldJ5kahQJnM4kmFoc9ih3iSnJzQNeDesW7Qhy--MlQmArR0di_Y9B0Dv34qY__rmdNiHL_20mxRqQmucnLikgzSt0F2s5i2qddAmHABgxRZbDVuReUQKfU56K_SloC5QEpC97diD46KHiZDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fErxRMlGP1briGgVgw6IiGykvm4y1YKmLBLx_QzA9gb9ziva50Y5s5AjnBUePKQ2xwQjm-_OtZ-PU_0IuW67llJPGQVFXSsnYxRoEGMn8v0ruFykrwOn8VnBAGhiuF5XoBejCPOTcXvvj4hHdNB3H5_kmLWISRdl0pgOnpDL5VMv1sEnnB35ufYXeDtbkpG5bhiM6lm9bFzCb9YBL8-VXiV2rjrx7v9T7Ni-YMjONNRVXg26EZR6KMSc5ANpigmsN-TXbRakf2QHfp2n1k5LruDaR92oycEEKP4B7rKtvg_eezltyCP2IpPg8QUcv477qzA85n09QvSOUIYFeIkqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=Y5mIrcpV4abZ43HINifvKs8EjSrZnN9J7VRIL9TWwrefHegljIbkeNLKEV-rlTCbjjG1UvgulCxLE0uUxrDfR5k3dqw0emeJD5bHoB7_ROh7M-NdYQuGawdexHFB06k6ozz0HVpgVTpKjpt5EVnv0OWUK58gCUMkPXSNNh9SxctMTbOErB8_3cIZcTTJ7ESSgtMpF7xIjj26bjRvoq54ycf2pJKNhM61KIDdgXz6VWafVOXQWVBJYiAdebZa1Cs2suh110Ne0jMcglXwfOJrG1COe4Jlhh4-Jhq8Sy3Q0iPwsPdTHXBjuS92tiRf0VaF1dQuUQG1CkN7bBk4f-ixBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=Y5mIrcpV4abZ43HINifvKs8EjSrZnN9J7VRIL9TWwrefHegljIbkeNLKEV-rlTCbjjG1UvgulCxLE0uUxrDfR5k3dqw0emeJD5bHoB7_ROh7M-NdYQuGawdexHFB06k6ozz0HVpgVTpKjpt5EVnv0OWUK58gCUMkPXSNNh9SxctMTbOErB8_3cIZcTTJ7ESSgtMpF7xIjj26bjRvoq54ycf2pJKNhM61KIDdgXz6VWafVOXQWVBJYiAdebZa1Cs2suh110Ne0jMcglXwfOJrG1COe4Jlhh4-Jhq8Sy3Q0iPwsPdTHXBjuS92tiRf0VaF1dQuUQG1CkN7bBk4f-ixBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=DfIndH_SZ-5TI2jAoeh53xxZ5JKuV9JX_1zG5DOFuCPiWSA0B1_7Fn2obnxoludUWnz5uSea0f0IcndqhMYzzmXuX6Owl3dvlqmkLRGWtrPwTwKu1q2HDyrDH7BczDhRbMg4Mxq8HFxyIGyBeyVgfO9_V_AljExQUX8_ESfBEzaAMWyeMnltrxvNgYx9n1Q-jG7wXT0qRo9lxfU6Oml_vsoVaJogCTt7HkGcqyEFcF13yK-IGnr4I8ZRHDtXc5hhSb1OqvKdxT1c5Q8WfYOqbN_T_ERDmKnINHSxteJReJ7KdqaegfXuAIgRvsJFFRReTkvL6HJlJsXycRo5IyJd2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=DfIndH_SZ-5TI2jAoeh53xxZ5JKuV9JX_1zG5DOFuCPiWSA0B1_7Fn2obnxoludUWnz5uSea0f0IcndqhMYzzmXuX6Owl3dvlqmkLRGWtrPwTwKu1q2HDyrDH7BczDhRbMg4Mxq8HFxyIGyBeyVgfO9_V_AljExQUX8_ESfBEzaAMWyeMnltrxvNgYx9n1Q-jG7wXT0qRo9lxfU6Oml_vsoVaJogCTt7HkGcqyEFcF13yK-IGnr4I8ZRHDtXc5hhSb1OqvKdxT1c5Q8WfYOqbN_T_ERDmKnINHSxteJReJ7KdqaegfXuAIgRvsJFFRReTkvL6HJlJsXycRo5IyJd2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhyYelWS4QIADluPziWb-Y0Ynp9ehnLnPW3Y6AMVxCfzv9W9Qs0EtilA6Nq8KMFw5MOJEiNAdiJBM8rw4xfYidBbPN3Z_h2_BLVJ4lYBCF8Ck4fwKJQsT9ddbGXmF0bfHuUtzzgGJyaGTac_URh-J7DwLk6TwNiaWxCNgJENtJEVAt51Hm6LIjNKy55je3Bu_Ihco0Ns1n3fP3FrvTlfGJlKuEDZKsXiGgSVsE5EBbPr2PEOXlV-q2DwYDqFnrjKEWdp9ThboHRyCOqq2quSrCI4PggrEpNc5cpD5DZgXw2EpdbR24Ovb-PSpGGtRBxN3YC3r244xEEs_USs-MhssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=oUo47e-tnvX5QJHuIe56mq03tSs9YoqmnUmaJC69AN7ZW2EQHjdfB93d8i7g6nXycNk2om5pukSrw2IR2QQFAXB7EQt6dPLPUo6TuxXZFxgDsOv_i5C51TQxLeB1Z0Cp3-ts6wzkxsj-LG6dU8TjQYKi7iIS0gqzeyoNWFtmK7MsE_vTfcRVhTTSfNhVVNcCo0pBwjDCW69cRmuA7tTIur2jWp03_PP9A9Fo8_u80fG4xwpaOzVsma9pUQY7qjmRVvlR6WPf8knfCj1eICH_bp-qUiAdcGvBct8SMajsu8ph_TTF9SO6gujf5_4AE4lUjY-6Rw-tGvJ1LnK3giST8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=oUo47e-tnvX5QJHuIe56mq03tSs9YoqmnUmaJC69AN7ZW2EQHjdfB93d8i7g6nXycNk2om5pukSrw2IR2QQFAXB7EQt6dPLPUo6TuxXZFxgDsOv_i5C51TQxLeB1Z0Cp3-ts6wzkxsj-LG6dU8TjQYKi7iIS0gqzeyoNWFtmK7MsE_vTfcRVhTTSfNhVVNcCo0pBwjDCW69cRmuA7tTIur2jWp03_PP9A9Fo8_u80fG4xwpaOzVsma9pUQY7qjmRVvlR6WPf8knfCj1eICH_bp-qUiAdcGvBct8SMajsu8ph_TTF9SO6gujf5_4AE4lUjY-6Rw-tGvJ1LnK3giST8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvH9BOzJP9cV7w8a0L0hYBXAyuVd9YQhPKqYVKlH6ya64X_BulAw-loPKR68sF1GJ5udhjx-Tc34TlavQFE5aRYfcGUFLo73Q09MtMlEwiLC76JmcZBAHo99y5ry-W57sZ7KPY51tvid1MNpbsWRT4Y51nQ_JXwWqVVh7Hidgt3HHNp5VjYFpuEiaNpmS0PYNNJ_RrM_80y8ZcLOG4qkIchyFP6jp1K93aOIFZmUcTZyt_AZvpbBrvWnnySXFhiThwpOSYM8_O0TxJ_wu2FVopJAazwi6KkU5BVPGQhOA9uQqbX-0i1tmfcB_LtXF5zSXISeXkfZZxWxwqbtGDQMhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=T3vrumgKxRvClDsbINyyg9lpJEEgxeVVV3ifV7ngt4yOibqkezVbJuvaGAuFI8ghXMEXmbAk0scHBDCAk9YdebMCxzcdPdLJ5WapgzU64gParwH7R98_qxu_kkH-d6gdJvzuWzVoM0TDtBEH1UcF1g9aTt-LLJ82oObZoJjkOtbv1xZAvrehn9LdClG4poeMGgWRSEC44Ns2Zewf6eFQJlEiVwd4YSkaMFUJjLVSdBFJTQx8xvaoaawGdfbcSPRLzjVrfbR6LzT6LvZhEGBQjsHg0Y8JPLcE_Cw2Wv4yrn4YfA2XtjOExY3ADYjAWB3UEI_EHrQOgPKX4Fr2btRbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=T3vrumgKxRvClDsbINyyg9lpJEEgxeVVV3ifV7ngt4yOibqkezVbJuvaGAuFI8ghXMEXmbAk0scHBDCAk9YdebMCxzcdPdLJ5WapgzU64gParwH7R98_qxu_kkH-d6gdJvzuWzVoM0TDtBEH1UcF1g9aTt-LLJ82oObZoJjkOtbv1xZAvrehn9LdClG4poeMGgWRSEC44Ns2Zewf6eFQJlEiVwd4YSkaMFUJjLVSdBFJTQx8xvaoaawGdfbcSPRLzjVrfbR6LzT6LvZhEGBQjsHg0Y8JPLcE_Cw2Wv4yrn4YfA2XtjOExY3ADYjAWB3UEI_EHrQOgPKX4Fr2btRbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=vckVRUow-WP8amXCXWmGcxG1_vLg9eurRFlIFN3Cny-rod_bvkIRC7bP5hLC7yeMfW0i7_gAzWy8gdPBvhKBlhE5xAov35aZFdpVyhN-0hw8GhrYGfHqqnIWd55Bocc8ronNoBU7H3UUM4_3CfR1wT8QjkB7bO-vohRaRC9MBy2Zw5DK9zj24_Ui-jsj-YdTgUlS2FRouZAwJ5A9T5oeQCSAz6leg2LZmi-7pTDsELrvzt2YWckgUfpcgdta_UcjLjKbWrLRjP7GNYt9zfxUTHtpLNwopfy6q47Ynx1bUarAshl-tbFkEFovW6hvNvyXs0zFRaYvLV2ppjxa1_pgHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=vckVRUow-WP8amXCXWmGcxG1_vLg9eurRFlIFN3Cny-rod_bvkIRC7bP5hLC7yeMfW0i7_gAzWy8gdPBvhKBlhE5xAov35aZFdpVyhN-0hw8GhrYGfHqqnIWd55Bocc8ronNoBU7H3UUM4_3CfR1wT8QjkB7bO-vohRaRC9MBy2Zw5DK9zj24_Ui-jsj-YdTgUlS2FRouZAwJ5A9T5oeQCSAz6leg2LZmi-7pTDsELrvzt2YWckgUfpcgdta_UcjLjKbWrLRjP7GNYt9zfxUTHtpLNwopfy6q47Ynx1bUarAshl-tbFkEFovW6hvNvyXs0zFRaYvLV2ppjxa1_pgHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H8rf121ia3CHcRjNmOwe9LH-90RUmxjZ4VXOzQfTvXho1qQlceO1y8aPaJa4wEGIdq7YGo1gos3OvkxeANoPmKAYK9QrbjStRnaQsNU8drWDq76Z-yg9JSG8VKNdPNL49EBo0mVsb3InfLoIbNikbHUUQ5kf0tdYl7mU5fGSDhEpiio3n2nDb4ssVYF4a3mqh_n0t6IQFQaXUqLO-0hDz5mMJTsx6M2mHf6QC9KIxjbelj4-Z4V8ZB6SPIBnigs4sWDFl2gxAcVMBPzYKFPkiOsfYLylZZpzw-EalQP1UqfY1n2dLasoKWP8K2OVuljwncvKop5N4zOBVvHK2F_HBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XD0-O78p6Lzuh-iISTU4tBRUT_UF5rP2tgBHyIgET9s11Rw9meZF6ejzStKXysINBICgAnDAjnoC-q6lkbzMFyydikxJcdY0EKZLtJUYio5eBq-h6i4shqSib4KA6zvmvgyejeW4AzIXgJRCQ30EAZPy0g3DyitWNHLa_lsw1nJNHG5bNwkHu5fbwi1U0FWzJKLgar8wzmzyHEujiSWEE9Uxro9Bty_csNNaLm_MEpzfjIYXQslgxnxnh3yCuVdSngvnsbKYew2IMflUKc-SnolZrkzuA3h8WPa0cDyaJlQc8l9qw-DpOE7odjWBmgKkT054vZK9x2VNcL4HjKLAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YPX2vAOpbrfhLOIysU-c5S0nHOA4C5XmR_j6nsl1ExtL3NEJuxJMQwzzYWsczmkoMooCKnDHWXFZkQDr6N5-n0XrrCO_vq84uXBvK2VuxwKiUfgb5ujHvN_KLpnHE7YJK5OcJ47fQCNvqcp-bWbxMXACphbSHBndB-K10jZgaiWMI1Qlrc4u0JpScOtf1MMCZlGjf9bwSOlupAki8r4Ppa3WjC-ewZ6QcVkJSGhwaQHyUD6o8Quc0gmQ_leEnyjOtb2LQBPLdS-gOgMq74kSeRJyiXkdhdxpHYQgF41oQv4xjR6UQfAuUbeCO9nlPzOFiJcG3xHQk3gwT_AHaN6GGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=Rb-APtz3MVuAeL37V0AvnvhgAOv3xsfsR_a-LwhKyFG7rOp1BFEWILz5w_N0dMhxQJoyr7m1eJ9OFBKwk_38jITP96ULLs32kUHMqrx660QglZFWIztJYDu-7epyb11dDcVkTnWRd12Oeu7H4WenDm51l7KE1Vtxs5bhJxzHlzOq_bT39vAuGEAI-hVkbes74ykY_Ndwmgi9-F_rA0kniBEqIIlqY2xouo23aXf8_wPkbfu5Xf3s4opu--9MCC1kfhrJAQd6YVNRVl0wYFp0vq-JIL3r10G1WFcmrZ8nXCmSOIQoE0LGOtAWdRGi2FFHEQvuKS2K3swHTVoJGgCwjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=Rb-APtz3MVuAeL37V0AvnvhgAOv3xsfsR_a-LwhKyFG7rOp1BFEWILz5w_N0dMhxQJoyr7m1eJ9OFBKwk_38jITP96ULLs32kUHMqrx660QglZFWIztJYDu-7epyb11dDcVkTnWRd12Oeu7H4WenDm51l7KE1Vtxs5bhJxzHlzOq_bT39vAuGEAI-hVkbes74ykY_Ndwmgi9-F_rA0kniBEqIIlqY2xouo23aXf8_wPkbfu5Xf3s4opu--9MCC1kfhrJAQd6YVNRVl0wYFp0vq-JIL3r10G1WFcmrZ8nXCmSOIQoE0LGOtAWdRGi2FFHEQvuKS2K3swHTVoJGgCwjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9h5YEXcGHHFyvoCiY5Achr1NU6-3g4oCGIID7mSpbEBZ6K55xpZaI0ZH1ygW-42AUUXtu2iMvZplbKS93DCp-iRaTekRJspV4E4vHoh18ltW1HuEr2wXwY2bSYVvMzgOHmisXAmbORKLMeH1HCwXsjRwp54StBhUVEu0-CHPb0T6255F6XL2pvLiA6xvipeV9AlGCSBg15flPK4MIDnrPbDJKM07Y6O44HZQacCRFOshkb4L--RtMXs1rtvRuSAodvcbh-IKKK5rTbwEt9cCagDKuGsHevmvbIyk6SBK1IsWrdNH98Mh4GKncPg-bgYukallNOZgWtmjrBXvrsX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fb2iNwlBLRnacvHiZzo7A1qrgiSowRJNJ-BrERT_H93metbAj2PEbj5l1o-HxovurbpRBXy4EoFNGfWxQm-Tyub5Uet8QUJ7rxDnkXshR8ounNn_MoPvapC4XwklmS88lQ3oMnZcOTvcZtns3eByQLesqWqQTMDZ3bTpD3zoajpoM5hN7gZ9czTsSk2ra7DvpJdOuOsTbHUGc2geiLEDC3zps0tzmYx77Y4kk2UogZueM4HzMH-km2QNUQoUddvOx9_N-DpCoRKYy9PXM7hbiRrtHMGxRom_rPRB1cAGW8yBkM28y3mUm6oS8e7oByHf-3Ff3jc-JEKDrneRif_NgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=aaLeLDZcFsarbDkxBHYIPKGZDtGHU--j7PGfCr-TIWzZGLaNUNiOHSgZiJ8jgUUcbhouB115KdkvpQE9mKa389vF9lPsPuvQGNRV4Jwf7WnVzmafDO1Miga1i6COkWFDOqKNZvHN3uRjNc9Tw1SHwTg9WOWZJTspujt2u0SH1ITwjc2qgJGY15PJ7L98fzmPSb-9uVzfrwZHgBwguwPPbPtBDB3qbrqAsLxnx2DGEBM1HH612kQj6NIUxG6kuNeTp0sLCmq5gd1L1jSHgf2dfYaOAXAXmhb2NmHQ71gutmRXJ7mbC2PDds39ZtM2xVWKsSq5feBV-iTkODNJXUAMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=aaLeLDZcFsarbDkxBHYIPKGZDtGHU--j7PGfCr-TIWzZGLaNUNiOHSgZiJ8jgUUcbhouB115KdkvpQE9mKa389vF9lPsPuvQGNRV4Jwf7WnVzmafDO1Miga1i6COkWFDOqKNZvHN3uRjNc9Tw1SHwTg9WOWZJTspujt2u0SH1ITwjc2qgJGY15PJ7L98fzmPSb-9uVzfrwZHgBwguwPPbPtBDB3qbrqAsLxnx2DGEBM1HH612kQj6NIUxG6kuNeTp0sLCmq5gd1L1jSHgf2dfYaOAXAXmhb2NmHQ71gutmRXJ7mbC2PDds39ZtM2xVWKsSq5feBV-iTkODNJXUAMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
