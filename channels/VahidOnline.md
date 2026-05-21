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
<img src="https://cdn1.telesco.pe/file/gNqzxE3XLgtNAsbzDHN7OAij5_nZAreHb1rDdRv0fxBR0fDsJh8G7G4o8LHPuYhlHfoOCdrMgYmucRDqyIytPHUqq4Y75AQr6A_kXL17O1R1DbjACeOqtn-Cg-UIKWYtWboiCMn1ZNzouhDVxHKp8Wpcs2oWkdLDIZifaJFcTClHTiYLxoiUiI9VPyB-xP8xafypwpdM8D_0OgPYL5Q3rbBL6bmD1_oOyGvo_WP5vXy1bLbw4PveETB15stTeCAkTRnuov20p4HpejWwh6rbEgi2KFSu4FRiuhAE8QvBEomFscv03hdVL4osD1ar9c1Cnpn_hIcUqMhQuUpU4FNwYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugLJDM8CRyU9Ir0dZpZwLfaE9Z3nyfyQlPQW5yBzAvrdLUHvko1RGKQGoxtdH3vpw80s3eTU29yRHbFsouzr8HSe92zlrrTWEM35UDTSpOzvFqEXp8DmXcH_8W4a8PoLy7ayZseqaqi3GH-gRaWliay6mWSt_n8Ey0aFCsstJ6iJAG4wCSeAq_P-yuaPAlIwoEPTfOr88vB9goQbOSnFAIbmKr10Ro0RBo4M-BKgt-bnCsw9MX3t3xYJ5PzarJ2HPuvIrncw8eheTWQI_av9j16Z2l4ia9ztZrMDmJCJ3clYSlQHSxwegFRylpTfCzLvB0P4yxaC3HPsiJH9M4aALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی دو زندانی را به اتهام عضویت در «گروه‌های تروریستی تجزیه‌طلب» و «قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه» اعدام کرد.
ارگان رسمی دستگاه قضایی ایران، میزان، هویت این دو نفر را رامین زله و کریم معروف‌پور معرفی کرده و نوشته که آنها صبح روز پنج‌شنبه، ۳۱ اردیبهشت، اعدام شدند.
میزان نوشته که رامین زله «پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند».
ارگان رسمی قوه قضائیه ایران همچنین نوشته که این دو نفر «اعتراف» کرده بودند که «برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور» با یکدیگر «همکاری» داشته و برای این کار، «سلاح» نگهداری می‌کردند.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/VahidOnline/75589" target="_blank">📅 09:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/622e876399.mp4?token=JIp6xcKmWP1k3UO5Dh5DBCjpmQDrLHSb3Yeo8fqJ_xUr6WyZuB0BBZ43-mDShRzi1NyBYFFvAuvSQ7ijoZHXT42GnL1FVNqeMOYUydQLao6bP8rXYah0rdRFmeG3SXv3xNjiN1BQ47FU4rPNuo8TlSIAdfTE01VrUOI6aJTB2fYkUkgSPXZFFP5bTv3PzIxuWriwnPtIJz38owGafmvDEPHfWWS64L-zDHu0o2FZVPl1ubcTbLQR15Uwo0WPJq38flwEP2IXNFPFCWHQq08kLuKLtxNywgksjK8P4Ae7-aUUl8qnitgMzmxeTERvtcXT-3Tk3HXkX8J8KKzClK3pEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/622e876399.mp4?token=JIp6xcKmWP1k3UO5Dh5DBCjpmQDrLHSb3Yeo8fqJ_xUr6WyZuB0BBZ43-mDShRzi1NyBYFFvAuvSQ7ijoZHXT42GnL1FVNqeMOYUydQLao6bP8rXYah0rdRFmeG3SXv3xNjiN1BQ47FU4rPNuo8TlSIAdfTE01VrUOI6aJTB2fYkUkgSPXZFFP5bTv3PzIxuWriwnPtIJz38owGafmvDEPHfWWS64L-zDHu0o2FZVPl1ubcTbLQR15Uwo0WPJq38flwEP2IXNFPFCWHQq08kLuKLtxNywgksjK8P4Ae7-aUUl8qnitgMzmxeTERvtcXT-3Tk3HXkX8J8KKzClK3pEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'کمور، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75588" target="_blank">📅 03:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1R9xrBqQNg_VUHgbpnEZJ_Pl9Zow4t8LycYBSkag0cg5zLy0Woan_f-Stn_oOhRnkiaQUTpGVe81x9WJx6rvapuwQFJ7CuxCdG_0zFaCYSbWt7zVi6KDRXtSMJ98t8Ok24wKv6FDJzfVjYAPJ_wsRNTDN4nR-WqozcHqKUq56Nle5mlUZMRwV-JseKqk9FHuMReWDhIm6wui3dTBAQXUSOBaI7z4jdEvhMZQwOSiZVnnue3cALCKlB0uiRjjDwjudzldWhACpsOZ275zvQNjZZBZIMnyvKGIHpMpSLObyC2esOfAyx6FLgJLetpOONZMdL-9SAFOxEnm3rTnnb8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی کاخ سفید در شبکه اجتماعی ایکس، روز چهارشنبه ۳۰ اردیبهشت در پُستی، عکسی از رئيس جمهوری آمریکا، دونالد ترامپ را منتشر کرد که زیر آن تصاویری از «دشمنان خنثی‌شده آمریکا بدست پرزیدنت دونالد جی. ترامپ» دیده می‌شود.
در این پست تصاویری از علی خامنه‌‌ای رهبر کشته‌شده جمهوری اسلامی، نیکلاس مادورو رهبر دستگیر‌شده ونزوئلا، رائول کاسترو رهبر سابق کوبا، و ابو بلال المنوکی از رهبران داعش که به جای تصویرش پرچم داعش نشان داده شده، منتشر شده است.
کاخ سفید در مورد کاسترو، روی تصویر او نوشت که علیه او کیفرخواست صادر شده است. در مورد مادورو روی تصویر او نوشت که دستگیر شده است. و در مورد علی خامنه‌ای و ابو بلال المنوکی روی تصاویر آن‌ها نوشت که «کشته‌ شدند.»
حساب رسمی کاخ سفید افزود: «عدالت اجرا خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75587" target="_blank">📅 03:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lqe_Mbs-iCQQUCe5bovjVQCv8sQLOI-aBmaSX8OXJzMvN0nmeoU1cbnIUdSofZ_DoICwu4zqR-8biBFfn6JIToeFtSBTSF_x37KbCsK_K1iKx-AsQUaSXuPh5MH5V4INPVe8AEyrkaAgzLMIq4sBoXcCd0Uca9N-GBXe37tfg4K0yV3r0IN-AZ1PWBYxooUVJjCMlxDdcCbc060R5xtNNrJtsLR2-1UQe_5Arf157pLaA3rCOYwiSWNno81IHYo5NdjE2oEOhAybLHDQBWTufTJG4yiZL0M7S7OnZFWD-zeXWAHa_8Kc0XivQX5cvUmSd-xZ4JM3Sg76DnmRvWrS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیل هیوم به نقل از «منابع آگاه» نوشت جلسه چهارشنبه ۳۰ اردیبهشت در کاخ سفید درباره ایران با اختلاف‌نظر شدید میان مقام‌های ارشد دولت آمریکا همراه شد، اما رییس‌جمهوری آمریکا در نهایت، خلاف نظر وزیر جنگ و وزیر امور خارجه، و همسو با دیدگاه جی‌دی ونس و فرستادگان ویژه‌اش، ادامه مذاکرات با جمهوری اسلامی را تایید کرد.
این روزنامه راستگرا نوشت ارزیابی مارکو روبیو، وزیر امور خارجه، و پیت هگست، وزیر جنگ آمریکا، این بود که در این مرحله، بدون اعمال فشار قابل‌توجه، از جمله تهدید به حمله و تشدید تحریم‌های اقتصادی، نمی‌توان از جمهوری اسلامی امتیاز گرفت. در مقابل، ونس معتقد بود تازه‌ترین پیشنهاد تهران نشانه‌ای از انعطاف است و می‌تواند زمینه حرکت به سوی یک توافق اولیه را فراهم کند.
منابع آگاه از این جلسه به اسرائیل هیوم گفتند که استیو ویتکاف و جرد کوشنر، فرستادگان ویژه دونالد ترامپ نیز در این گفت‌وگو از موضع ونس حمایت کردند.
آنها پیش از این جلسه با رهبران عمان، قطر و عربستان سعودی گفت‌وگو کرده بودند.
به نوشته این رسانه تنش در این جلسه زمانی شدت گرفت که ترامپ از ونس و فرستادگان انتقاد و آنها متهم کرد که رویکردشان به جمهوری اسلامی امکان می‌دهد زمان بخرد و به تصویر ایالات متحده و نهاد ریاست‌جمهوری آسیب بزند. ونس با لحنی قاطع پاسخ داد که دولت باید به دنبال پایان دادن به این کارزار نظامی، بازگرداندن سربازان به خانه، کاهش قیمت نفت و تمرکز بر مشکلات داخلی آمریکا باشد؛ پاسخی که حاضران را غافلگیر کرد.
اسرائیل هیوم در ادامه این گزارش به گفت‌وگوی ترامپ با رهبران منطقه اشاره کرد و به نقل از دو منبع نوشت که رهبران اسرائیل و امارات متحده عربی، همزمان با تاکید بر ضرورت حفاظت از تاسیسات حساس خود در قبال حملات احتمالی جمهوری اسلامی، از پیش گرفتن «سیاست‌های سخت‌گیرانه» علیه جمهوری اسلامی حمایت می‌کنند.
در مقابل، رهبران عربستان سعودی و قطر ترجیح می‌دهند از بازگشت به درگیری‌ها پرهیز شود.
این روزنامه همچنین به نقل از یک مقام آمریکایی درباره تماس تلفنی ترامپ با نخست‌وزیر اسرائیل نوشت که نتانیاهو از رفتار جمهوری اسلامی و احتمال وقت‌کشی تهران ابراز سرخوردگی کرد، در حالی که ترامپ بر پیچیدگی شرایط و دشواری‌هایی پیشِ رو تاکید داشت. با این حال رییس‌جمهوری آمریکا بار دیگر گفت که به رفع تهدید هسته‌ای حکومت ایران متعهد است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75586" target="_blank">📅 02:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKCd0ka1cAgzzWaZt_rNUY_4GoIl7-fy4YiGGGbupQNWaOpgj9xKhWDDSwqO9yHEiVC3subnM49uAD1ctrAHAk2UbVUvxnDY4fSQxEtl8Fnc_jWpXqR03YDxCwxXv-NkT5HI36OROxssE_yPMMGDbGQ137cnrjcGceWndthMuTub4kkKBz9Oa77XeBfuHs63DNeW9nLk61QQDR8i8KAmyyIedtLXAa2F5u48Tw6gGf34xoP6HIx9IQfKq5j7SJFgPWL7gxaZdPnMetETorMhtSZ9BYu1NWKh8uo9I75Lm6tRgO45Nu8AfKihOSpHn6R7i4Oo_oZUAqC9dyhF3M-FBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=gZKIw1D-9M7Spjg42ipEwH7pH7HCdsknPr_UgwfYZSodzF2E56-CHFPZ_7OXyK_WMVjeAwY22kC5Frqc9d_R5SHKOClriWHeUC7I-zKvMR9_G239fEjpVYFI2TTiaN2s5VfLgp8U_47bfLd8BSH1X9w9oK8wXgOrubjofsOY-ny1TlBHfHlc9txIBrFR-acOQ_io97k3KIO2tWOd_csptnyjSbRx6nHdUlXSpCiZRhEe-u3iaLHkV3wWyjsRJyqpCq1YXQ4iszLKGr2U-XvbyEMfhy5Fg9ENHpZoBZHoCUgh3Bo94Tqh_9t_OEJH8eEeRQm7itz0QAroMN30K3Uzbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=gZKIw1D-9M7Spjg42ipEwH7pH7HCdsknPr_UgwfYZSodzF2E56-CHFPZ_7OXyK_WMVjeAwY22kC5Frqc9d_R5SHKOClriWHeUC7I-zKvMR9_G239fEjpVYFI2TTiaN2s5VfLgp8U_47bfLd8BSH1X9w9oK8wXgOrubjofsOY-ny1TlBHfHlc9txIBrFR-acOQ_io97k3KIO2tWOd_csptnyjSbRx6nHdUlXSpCiZRhEe-u3iaLHkV3wWyjsRJyqpCq1YXQ4iszLKGr2U-XvbyEMfhy5Fg9ENHpZoBZHoCUgh3Bo94Tqh_9t_OEJH8eEeRQm7itz0QAroMN30K3Uzbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه چهارشنبه گفت حاضر است «چند روز» برای رسیدن پاسخ ایران به پیشنهاد واشینگتن درباره توافق پایان جنگ صبر کند اما هشدار داد که این پاسخ باید «۱۰۰ درصد درست» باشد.
او بعد از سخنرانی در جمع دانشجویان نظامی به خبرنگاران گفت اگر پاسخ ایران درست نباشد، تشدید تنش به سرعت رخ می‌دهد و افزود: «ما آماده پیش‌روی هستیم. باید جواب‌های ۱۰۰ درصد درست و خوبی بگیریم.»
ترامپ اعلام کرد که آمریکا در حال حاضر با افراد «خیلی خوبی» از طرف ایرانی مواجه است که «استعداد و قدرت ذهن» دارند؛ افرادی که به گفته او جایگزین رهبران پیشین ایران شده‌اند.
این اظهارات ساعتی بعد از آن است که سخنگوی وزارت خارجه ایران اعلام کرد تهران در حال بررسی طرح پیشنهادی جدید آمریکا است.
این طرح توسط اسلام‌آباد به دست مقام‌های جمهوری اسلامی رسیده است؛ همزمان با سفر وزیر کشور پاکستان به تهران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75584" target="_blank">📅 23:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OjCD64bTFRd86__mZjXU7rcIhOQPUT1cmxGFxQOAH2TR3YMVXxX-ahh385m_lA9b7BlosOid_exk5icl_iB-f1T9R9pwBL5ndpWHzKKJvzQAYKuY8cEONwWk1wBmpr9vxPdya6_1GJhh-XMsIe0pwZI5lcJpoLH2agHx1ncC-Z3-b_WD1jvGrlyEbxUSTaBrMXvAgImlEzWFI2hAg6X-4f4AX-023fhMe29F7_iFo1R2OzP4J4ZoE75MueNKA5h783QZrO49_h_4pc5K9lEX2KpHQShv3SiW-s_Tg1JFJuCXmUA5NaFh6NDsjRBMMiUuzfdJDq3AfEH7hjzpwt9SOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PVGf0x2o68pn9uH-JVdzp58jHx-tOtz9M6YoHy3I1KKcEuM-Wt1xwCkLro_wlgvQUKCvEvyxjye-Hv0AvqDh0vSoeVpL2Hr69LA7iRWruJXhxsbfriTv2u2sO9-CeCVPAXIZNYJuujzBcfGGfid_woovQmrF_J9OmGljwc41SZ3kMyP3JimbGKPkJZpVthNQ9GSIcLL5FLFjEOe_LPsG_pw3-yg69w3n3lzRg-9cxYND0OQcE6bQU8fMmsY5eVVppmyXAH11amSPPVKcdhAiomiJf8JOITmkfKCSdzzxHH9UsIDlHkXs0pFLPPvGnWY5FtIS8A2uYQcuIFQ5MF0aXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس در گزارشی اختصاصی اعلام کرد دونالد ترامپ در تماس تلفنی طولانی و «دشوار» خود با بنیامین نتانیاهو، از تلاش میانجی‌ها برای تدوین یک «تفاهم‌نامه» خبر داده است. بر اساس این طرح، آمریکا و جمهوری اسلامی با امضای این تفاهم‌نامه رسما به جنگ پایان داده و یک دوره ۳۰ روزه را برای مذاکره درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کنند.
به گفته دو نفر از منابع آکسیوس، این پیشنهاد با مخالفت شدید نخست‌وزیر اسرائیل مواجه شده و دو رهبر درباره مسیر پیش‌رو اختلاف‌نظر جدی دارند. یک مقام آمریکایی وضعیت نتانیاهو را پس از این تماس، «بسیار خشمگین و آشفته» توصیف کرد.
آکسیوس به نقل از منابع خود نوشت سفیر اسرائیل در واشنگتن نیز نگرانی شدید نتانیاهو از این گفتگو را به اطلاع قانون‌گذاران آمریکایی رسانده است؛ هرچند سخنگوی سفارت این موضوع را تکذیب کرد. یکی از منابع با اشاره به بدبینی همیشگی نتانیاهو به روند گفتگوها گفت: «بی‌بی همیشه نگران است.» کاخ سفید و دفتر نخست‌وزیری اسرائیل از اظهارنظر در این باره خودداری کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75582" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=d0UEnsE3-x2HMdbnxvd25kobakhOXCgY2tK9qHVsdORrSGmd6q6xJxfke5h-A1iIvQWB24xx9HfsBHwUMc1rn5XddhDO8e2fgJoKDgHkfufqrZMRv_x8qkEs5y82mBgvsibYLcIuoUFmBOBuZKKaaGvW7V2sKMLi0BA3oWVtZzSTmG_ETLHmjuDo4Gt0SY9fSVw9BHjEwcvLvGX0PDO76YeWlflGCf41MyKYgbB_5QUrh3xwT5prlAWjFs7b6llkzA1VS-kt6pV4x9JGBVlAJa2VmuNMDfxuCA773e6G3M4CQ4ioiBok-SrIJKfNN2lnsapnlHql7LuMAyM60uequA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=d0UEnsE3-x2HMdbnxvd25kobakhOXCgY2tK9qHVsdORrSGmd6q6xJxfke5h-A1iIvQWB24xx9HfsBHwUMc1rn5XddhDO8e2fgJoKDgHkfufqrZMRv_x8qkEs5y82mBgvsibYLcIuoUFmBOBuZKKaaGvW7V2sKMLi0BA3oWVtZzSTmG_ETLHmjuDo4Gt0SY9fSVw9BHjEwcvLvGX0PDO76YeWlflGCf41MyKYgbB_5QUrh3xwT5prlAWjFs7b6llkzA1VS-kt6pV4x9JGBVlAJa2VmuNMDfxuCA773e6G3M4CQ4ioiBok-SrIJKfNN2lnsapnlHql7LuMAyM60uequA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز چهارشنبه ۳۰ اردیبهشت با تاکید بر این‌که نیروی دریایی و هوایی ایران از بین رفته‌اند، گفت اکنون تنها سوال این است که آیا آمریکا برای تمام کردن کار بازمی‌گردد یا جمهوری اسلامی پای امضای یک سند (توافق‌نامه) خواهد آمد.
ترامپ که در مراسم فارغ‌التحصیلی آکادمی گارد ساحلی آمریکا سخنرانی می‌کرد، گفت: «همه چیزِ آن‌ها از دست رفته است؛ نیروی دریایی‌شان نابود شده، نیروی هوایی‌شان از بین رفته و تقریبا همه‌چیزشان را از دست داده‌اند. اکنون تنها سوال این است که آیا ما پیش می‌رویم تا کار را تمام کنیم، یا اینکه آن‌ها یک سند را امضا خواهند کرد؟ باید ببینیم چه پیش می‌آید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75581" target="_blank">📅 20:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BRuN8K1Z_-EAA8WJe11DMS-Ye-hg3HirQuP_ca-v8T0-tWEE5V-T1KIpyfjUPCyjuuUZlso47Iu5EuCp15p_T4w-jeyzplDPzqTFqVvQ8WBfnutqF-c_dxusdy_vvUfL2VOtEjNMOfYCMTZDiPH7kxp9caNL5jsvQuTtBDxqcNgosbpFGyHEYO7XyS-QtUJZaLGXyK8vxWowVtX_SpnZRuCF9QnvBH0vmznFZmipZ9_eyx25cLsWdYr3bWQ641nV2BNt-X55-tyqJ5EJSfiC8HQHA_C3uAQEDy0wPEnq3Ze3LSHqYnXRcn8z3pQMMOm96Wo-2ne_1KUKSzmO-3eo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت، چهارشنبه ۳۰ اردیبهشت پس از اظهارات خوش‌بینانه دونالد ترامپ درباره مذاکرات با جمهوری اسلامی بیش از پنج درصد کاهش یافت.
بهای نفت برنت به ۱۰۵ دلار و ۷۰ سنت رسید؛ زیرا معامله‌گران به نشانه‌هایی واکنش نشان دادند که حاکی از نزدیک‌تر شدن واشینگتن و تهران به توافقی است که می‌تواند از دور تازه حملات جلوگیری کند و نگرانی‌ها درباره اختلال طولانی‌مدت عرضه در خاورمیانه را کاهش دهد.
ترامپ گفت مذاکرات با جمهوری اسلامی در «مراحل نهایی» قرار دارد، اما هشدار داد اگر تهران با توافق صلح موافقت نکند، آمریکا ممکن است حملات بیشتری انجام دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75580" target="_blank">📅 20:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFcI_czlDAMf_11XdfuqsdgsSBqytujU5EmHn56t2J2jwLHrG_DP7X72eqAwV3aOULlolVuXW_GbUZPjWbvzHY4lZ4xlrsehhljY2EJ1A7yDjfDIDstADLEHMb--KCWiCzAyhKjsW0f9BsEbKBO-Z2A_94uAHmXa36EhgkAjPv_IRGjg-INQGiIaTgfa8ZYpUgc8XnGLfComGr_fPo4BVXpzqV-8PtH8PeTKYA1Jv3ZUaJ-3sMF19tWyjl9rYEgNfPeMSbpxlL5HOMaAkWXo8OWNEmYayHgVsy2ircyA0k63Jpw49KyDFuWwoLb1mEQ7M9Svt6rIP2j4h_hsFbfOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیصل بن فرحان، وزیر خارجه عربستان سعودی، نوشت ریاض از تصمیم رییس‌جمهوری آمریکا برای دادن فرصت دوباره به مذاکرات با جمهوری اسلامی به‌منظور دستیابی به توافقی که به پایان جنگ و بازگشت امنیت و آزادی کشتیرانی در تنگه هرمز به وضعیت پیش از ۹ اسفند ۱۴۰۴ منجر شود، قدردانی می‌کند.
او همچنین از تلاش‌های مستمر پاکستان برای میانجی‌گری در این زمینه تقدیر کرد و در شبکه ایکس نوشت عربستان سعودی امیدوار است جمهوری اسلامی از این فرصت برای جلوگیری از «پیامدهای خطرناک تشدید تنش» استفاده کرده و فورا به تلاش‌ها برای پیشبرد مذاکرات پاسخ دهد.
وزیر خارجه عربستان سعودی افزود هدف از این تلاش‌ها، دستیابی به توافقی جامع است که صلح پایدار در منطقه و جهان را محقق کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75579" target="_blank">📅 19:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=JD2jD7SjC7Xik6iVY6EV4_aYD-HgXp9wrgnnF9AW5ORgbaqc9-IGzKGi0uT0IIBP2aDWFJFxULyh75LMchfwSr45MmEFBmBLqG5N-VY5Z_6nolKB1WtgoysQmZ5nBfp-h_4jum4iC6FaWHE5ptkEVfOBSaExJTWsh-TtmXNTIMNheJCRoNWzLklfmBaElAKBDkb8dXdneCeVoBXGD9VH3GN2OGr-JwMBAnTN3Ptwy8CmR72BHMffNNH9zVXJuG4fg6KC5PYf37j0tOJEUyTzovVzhe1xN2VmNgX2xq4WHOEQ0SN48mdymWYTvrwE0KstNzyZUW97knKnO8Po1Pk0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=JD2jD7SjC7Xik6iVY6EV4_aYD-HgXp9wrgnnF9AW5ORgbaqc9-IGzKGi0uT0IIBP2aDWFJFxULyh75LMchfwSr45MmEFBmBLqG5N-VY5Z_6nolKB1WtgoysQmZ5nBfp-h_4jum4iC6FaWHE5ptkEVfOBSaExJTWsh-TtmXNTIMNheJCRoNWzLklfmBaElAKBDkb8dXdneCeVoBXGD9VH3GN2OGr-JwMBAnTN3Ptwy8CmR72BHMffNNH9zVXJuG4fg6KC5PYf37j0tOJEUyTzovVzhe1xN2VmNgX2xq4WHOEQ0SN48mdymWYTvrwE0KstNzyZUW97knKnO8Po1Pk0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75578" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=oiAz-Y6v3VYcTKEl7CVQBL-myobge1pYtMHU1VtSKRi4bPGSQDOXJSvtCHATVJnBhZbEy08RSN9H8kVodbd_GI9k0G9DHD3quEpShxsJchD8bHmw-_QzCjU2Qc1jbhPL9u9M0eiantQhEXkWVGt-mN_zstVi7h6ZuQEUXiVbYP9Bx7FifQw1twBRs1xa2w6CPsYnQKeJrCnoBUrmwc_U35e4AhJgHTiWTFkxSPQHf3a7IZD73iSlwGgMa8XMJrozDRRqJ6HxMKL-AcMp08PeUeMDsfMW9URs_Tzr2ocSsfbKfO4fOnEzS3R9Xb1F68Y1NaXNn-MIwOCsV_Au2Ak7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=oiAz-Y6v3VYcTKEl7CVQBL-myobge1pYtMHU1VtSKRi4bPGSQDOXJSvtCHATVJnBhZbEy08RSN9H8kVodbd_GI9k0G9DHD3quEpShxsJchD8bHmw-_QzCjU2Qc1jbhPL9u9M0eiantQhEXkWVGt-mN_zstVi7h6ZuQEUXiVbYP9Bx7FifQw1twBRs1xa2w6CPsYnQKeJrCnoBUrmwc_U35e4AhJgHTiWTFkxSPQHf3a7IZD73iSlwGgMa8XMJrozDRRqJ6HxMKL-AcMp08PeUeMDsfMW9URs_Tzr2ocSsfbKfO4fOnEzS3R9Xb1F68Y1NaXNn-MIwOCsV_Au2Ak7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، پیش از ترک واشنگتن به مقصد کانتیکت، در گفتگو با خبرنگاران در فرودگاه به تشریح وضعیت تقابل با ایران و گزینه‌های روی میز پرداخت.
او با اشاره به وضعیت داخلی ایران مدعی شد: «در حال حاضر خشم زیادی در ایران وجود دارد، زیرا مردم در شرایط بسیار بدی زندگی می‌کنند. ناآرامی و تلاطمی در آنجا جریان دارد که قبلا نظیرش را ندیده‌ایم؛ باید دید چه پیش می‌آید.»
ترامپ در پاسخ به سوال خبرنگار درباره احتمال انجام یک «توافق محدود برای تمدید آتش‌بس» گفت: «ما این شانس را امتحان می‌کنیم. من عجله‌ای ندارم؛ هرچند موضوع انتخابات میان‌دوره‌ای مطرح است، اما در حالت ایده‌آل ترجیح می‌دهم به جای افراد زیاد، آدم‌های کمتری کشته شوند.»
رئیس‌جمهوری آمریکا همچنین با ابراز تردید درباره نیت مقامات تهران گفت: «من متعجبم که آیا آن‌ها واقعا خیر و صلاح مردم خود را می‌خواهند یا خیر؛ رفتار آن‌ها نشان می‌دهد که به فکر مردم نیستند، در حالی که باید خیر و صلاح کل منطقه را در نظر بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/75577" target="_blank">📅 18:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gfHh1xPtJ4YTHN91wlZZxb8cya6aLwKqarhMe8_MkHQMhHVezFvEaCqZ4AsJY8W7N8QdpuhMP6iXmQH5T2wEkcjQiNWRKAWvttlmq0mk_d2J38sgI-T8Ep84AQboqjNrs8nkPOXR0WL_mDaVKx8ftgDuZMFuv--nDECF9oe-kAfJK6YarELvb__VyV0kk2rLPpKTOFuAcZW0kiSjjcJK0ywJOCjahaSF5_2zc_jegbWjoXzuxml-yTuGJrVTU0wL8r8GvbKGyk3Ha8lIjrs5BBxI5nSRIQ2JcK2YLXZ0C-U_MzfODcWFnLTN44jF-OqjST4zLEMzKFlcVlnlasFrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OKReQWmi1acxKGC4scOSjxRPqsty3g3Rw79sUiXdIBNW14oHm57CrSp8R5ElAmWGGZIfFMMVpq0KLJ_NaElK4uVZepVsz8TCleqCtJgxK1CtAiBl-KiqNVl0snq8M1Wi5KhuoME9RYcHRjmuv8KQbEVG3IExZt0ANyz9brfbqCrVvrR2OkGzd_zJn0dGbL3iabf8CQg4ijnlXFmzfSbsiWoVfNBTmkztqiHBQO3TtYbrYxZDDBByYbrArxMQ3MFNvD6DknKrDTjPVctDAGBahquAAiVcNznKJ-VzyhrQQizWPlonN2ZLJhJKOQnrIw6jx50IvitkbOLYerxn5fqNrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=u1aeoPjT1qDlPbvu8ZY1-1YJcinpJe-jiaAa7Yx_kgUE-sQV6p3hVQa24PQCk2Z_mrVexiVjxrrE1BFW3LW29qesmKbV4GqFe57stkAqySq1RyuTEWq6Y6lAo2YaL9FZGTiBGO02LFaUi0tcN0xQjguhEsQFbKZliRizB2lShAZwiJ0pFSc1mgHM_YBYM2ZsG5ChNnC_SaD53pznC6ZJDRuNApCgDM_inWBN5xWbhtdJ_GHYCcHbrdZ8lvaBCavC-UpuCSJFKBSGOax7RvlhtDd1LIPfyQuiekk5ZQnAzJeLNF3HUvbK7TC5QnnQi71nqsA4a_ik9Y25rKYpXXbf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=u1aeoPjT1qDlPbvu8ZY1-1YJcinpJe-jiaAa7Yx_kgUE-sQV6p3hVQa24PQCk2Z_mrVexiVjxrrE1BFW3LW29qesmKbV4GqFe57stkAqySq1RyuTEWq6Y6lAo2YaL9FZGTiBGO02LFaUi0tcN0xQjguhEsQFbKZliRizB2lShAZwiJ0pFSc1mgHM_YBYM2ZsG5ChNnC_SaD53pznC6ZJDRuNApCgDM_inWBN5xWbhtdJ_GHYCcHbrdZ8lvaBCavC-UpuCSJFKBSGOax7RvlhtDd1LIPfyQuiekk5ZQnAzJeLNF3HUvbK7TC5QnnQi71nqsA4a_ik9Y25rKYpXXbf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز چهارشنبه ۳۰ اردیبهشت‌ماه درباره گمانه‌زنی‌ها راجع به سفر عباس عراقچی به نیویورک گفت:  «وزیر خارجه ایران برای شرکت در نشست شورای امنیت سازمان ملل درباره صلح و امنیت بین‌المللی دعوت شده، اما حضور او هنوز قطعی نیست.»
به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی «این نشست به ریاست دوره‌ای چین در شورای امنیت، روز پنجم خرداد برگزار خواهد شد، اما با توجه به برنامه کاری فشرده وزیر امور خارجه»، تصمیم نهایی درباره سفر هنوز گرفته نشده است.»
این اظهارات پس از آن مطرح شد که علی خضریان، عضو کمیسیون امنیت ملی مجلس، در یک برنامه تلویزیونی نسبت به احتمال سفر عراقچی به نیویورک برای مذاکره درباره تنگه هرمز انتقاد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75574" target="_blank">📅 18:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/USUpbF2aw-Iip221qrZZpXsmgHFzdgqjLgpW65BmJjioeBPEE48d4jZcEF_LKFjGxUHQUzGS-rP_lU5gGAvwO4ZzcypLaOp2BQQMG8o_UXRWPxRMGtFk8OYwikAxkJ9YLRatGsfgQd7heb6TBIvKHtA7uDd5V0Y9kMIY0thF2T-NkvV_9jqWAtX--cGZdhZ43W8QtSgIjAh9peToBuePdt_TGOzrR2tT5T0fznj43uoUZgxW1rtX8nRFP1qBA0ZB_mBqKplwYpL4Bb3YE1OGQu95NaqP7312FLontI73hYIQvMJuQCW7r6sv-5ZoUVuOH9dd9zmo_T8alxSxj5UdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mD-UDZwZ79TUpXMiLQblR1US6LezUqOG3xut9JIq379pCqSCg0C97RfxPSrWudy5B4o_elSnIP_ktbDrnZik7-yf3m8R4WNgwDN0KxJjFmVf92J7K48rVYViEJZeRwPF9xbIkczd0trT_xFoo6bmAmREz_yHAUNW_Kknle3fJtHrfPnSiRKJAcd6ACBpUd46zp4ZaSF6rG7xwLUERu6ae31AUylIifbXMN-8gJd7BlGO0I5iatwYkUeWUyKoWLpy9aeYUKX35WtY8NoLs5kY2HnMTY9PofZv624JfQFxt42F4H_BssNTGkDavGH58_WEpUcUtfb2qVaE_3Ofj-OsUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه گزارش داد رشید مظاهری، دروازه‌بان پیشین تیم ملی فوتبال و استقلال تهران، «هنگام تلاش برای خروج غیرقانونی از مرزهای غربی ایران بازداشت شده است.»
میزان در این گزارش رشید مظاهری را متهم کرده که «قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از کشور خارج شود.»
قوه قضائیه به زمان بازداشت این بازیکن پیشین تیم ملی فوتبال ایران اشاره نکرده است.
رشید مظاهری پس از کشتار معترضان در ۱۸ و ۱۹ دی، با انتشار ویدیویی در پنجم اسفند، علی خامنه‌ای را مسئول کشته‌شدن معترضان معرفی کرده بود. پس از انتشار آن ویدیو، تا مدت‌ها خبری از وضعیت او منتشر نشده بود.
خبرگزاری میزان گزارش کرده که مظاهری در «بند عمومی زندان» به سر می‌برد و قرار است به اتهام‌های «پرداخت رشوه به مامور دولت»، «فعالیت تبلیغی برخلاف امنیت ملی در شرایط جنگی» و «اقدام به عبور غیرمجاز از مرز» محاکمه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75572" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GHA_9Nt1XYjOrr7yd4P1w1R7P8Qet5PxdGXkxOuoz5QBRLGeFX-NNjoGAM1WTwY5dALXPHqOFk6NZ7Q6U-CU76obrtK1yEJY5zBFVNZqr0skYwD2IyCkyhtqitdyI3FekxYZNehoryf_T0_9EZ-ervj2yGKqsKjTuhxM-3-GGrHd43PA_aHEKpmChe3YXXjP0DdQXkxDczJB2I_yJtnfO6ALsa84zwAxpA4nwOdImG4dTllX_ycIpqtJ57XB2WabTwjDQmk9AXG-4vmM9QiTVnsr40-_iZ9Ya6-nAKyYrnTQ1mdto1_P-e8aT4iKnvFfjOewzg6nJDB0crdyrUdAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در میانه اختلال در مسیرهای رسمی تجارت و فشار بر زنجیره تأمین صنایع، سازمان توسعه تجارت ایران واردات برخی مواد اولیه پتروشیمی و پلیمری را از طریق رویه‌های کولبری و ملوانی مجاز اعلام کرد.
این تصمیم نشان می‌دهد بحران تأمین مواد اولیه در صنایع پایین‌دستی به مرحله‌ای رسیده که حکومت برای جبران کمبود، به مسیرهای مرزی و غیرمتعارف متوسل شده است.
اما این تصمیم پرسش‌های جدی ایجاد می‌کند. مواد اولیه پلیمری و پتروشیمی کالای مصرفی ساده نیستند؛ واردات آنها نیازمند حجم بالا، کنترل کیفیت، استاندارد، ردیابی منشأ، بیمه، حمل‌ونقل تخصصی و تسویه تجاری منظم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/75571" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXFnAoXKqcXZL7d3_kV7HYlSAH4krE890rsYamto2GanEsFIW8k61F6r03xSGv91Ff7-5T0bPCA3KEcGXSDUjgrEDTnPjAS4iVmeni6BgqLxo5EyCvX70eVtAJ3jTt-hj5ix3P2sRr9oP1I5-sc4dIU0D97s5kO2StcmnboZ83o1r7inua_9e-S1tA7kdneh0ATp8yX7Xu-q_a7ZL3k5pCbNcVTG1VFp-O36L1f7G4IN7tg9HY0bWlqhBRvKagn5rNkYJGthQpEVE4iKvuwxST42-MZTt2aie4CTxNcf5ufV_mP818YYak9meoqyMia0s6uJBUki5lUeY82LV1m6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران با انتشار بیانیه‌ای تهدید کرده که در صورت آغاز دوباره جنگ آمریکا و اسرائیل علیه ایران، جنگ «به فراتر از منطقه کشیده خواهد شد.»
در این بیانیه با اشاره به تهدیدهای دونالد ترامپ و مقام‌های اسرائیل برای حمله مجدد به ایران آمده: «اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبنده ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.»
عباس عراقچی، وزیر خارجه ایران هم در واکنش به اظهارات تهدیدآمیز دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال از سرگیری حمله نظامی به ایران، در شبکه ایکس نوشته «با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75570" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSRd1YitmDKOkLx7SFW8invTNzdpAvfgq-yes2F73P830t4IY_Izg9DNGcM6l3fTDZlGufQd4kIrrSWey473FJDL-EMqOVBWNkeoPac7XJsEb2W7VlGG4O_ZUeFSBC23RJROdIfFpYvDX_X6doJKkAAZxJuTFH_HT2so906fYHR5QOH2F8l7n2hj0JTEWFwbRDnBr0tyGUjAfk56ryC2YjRiGaSxLGqFBbWoUzhVVsshzqhXzMwD7B0hQrvLmbxQEeLyt6qNXAUFdxCGj9NWixbcLiXSfJAs00JyfL89-rjrsDRxoWENZQUfLLfOQ7brChYG2h160o1yz8DLZ8GZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران روز چهارشنبه ۳۰ اردیبهشت خبر دادند که محسن نقوی، وزیر کشور پاکستان، وارد تهران شده است. او روز ۲۶ اردیبهشت نیز به ایران سفر کرده بود.
خبرگزاری ایسنا اعلام کرده که برنامه و اهداف سفر این مقام ارشد پاکستانی در ایران «مشخص نیست». خبرگزاری تسنیم نیز گزارش داده که آقای نقوی در بدو ورود به تهران با وزیر کشور ایران دیدار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/75569" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpN_PMSYI9ja9T73JJ-WMfAQA48Wbt8tr-L3OprcaFX3YwHF0NsWLaYHl5CSMyG_5-RVHO_cpnOiV_gWDpJ-hDaWy5f4cNSPEDg5hZwQvfpl9H-k31ZCWaqjGgJM7rgXlMEtSUSDZQ5wnhjYGffHrbKitjFd7qwni1r8nz0UO_t2d0snhhfMZait6hrBl7Ke9gLm9pGzbfcFSsBRXJnucF9bm9R5h-hkrEOfcYw3RdHtB-hsAn7EjGZjdTLm1yWr9iR333HFXtfyL4Jma37fHxdSp68n5KqzKNO1EsReR__jRAe_dmJ8BZxEYNY6RDKgUH5rtYOEz8aBBiM3CTEOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از اجرای حکم اعدام قاتل الهه حسین‌نژاد، که جسد او اوایل خرداد سال گذشته در بیابان‌های اطراف تهران پیدا شد، خبر می‌دهند.
عصر چهارم خرداد ۱۴۰۴ الهه حسین‌نژاد ۲۴ ساله از سالن زیبایی که در آنجا مشغول به کار بود، بیرون آمد تا به خانه‌اش در اسلامشهر برود، اما ناپدید شد و وقتی خانواده‌اش اعلام شکایت کردند بررسی‌های تیم جنایی نشان می‌داد الهه از میدان آزادی سوار یک خودروی عبوری شده است.
جست و جوها برای یافتن الهه سرانجام پس از ۱۱ روز نتیجه داد و با دستگیری راننده خودرو به نام بهمن ۳۷ ساله و اعتراف به قتل الهه، جسد او در بیابان‌های اطراف تهران پیدا شد. متهم نیز پس از محاکمه به اعدام محکوم شد.
این قتل جنجال زیادی درباره امنیت زنان در ایران به پا کرد و تا مدت‌ها رسانه‌ها درباره آن مطالب مختلفی منتشر می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/75568" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NbMn7H4pklhF3tEEKPVA_H_qPbseOqthqXvIr6nJUtciqwfScN8UeZL0Eb38gc2NteQl7J5x-Lqbgv_xX0sGX57g-e106KzyS46c6q5guXZIwU4mRuLolPAadRzaKk8E0t_ytwvO28zKo78vzEhNEpxK32JMaMbUnSkuzQxoRKEdI-Fb95ZOR9zmDmRiAYANOyDyEdgRX_BH9byNTIZexfAUr5DXgQAkL0gEWizogJdcT7KobW6S2jDTbhVwivTeQW78XjYT-nzQ3XLb4sbrG2nBahBarNqyEp2h2HIsizPKtu-3GGIIbQynl4bjqsAGMoXCQ1aDeeH3VZE5OlQu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حقوق بشری گزارش دادند دادگاه کیفری تهران پس از رسیدگی دوباره به پرونده شهرک اکباتان، سه معترض بازداشت‌شده در این پرونده را به دیه و پنج سال حبس محکوم و سه معترض دیگر را از اتهام مشارکت در «قتل عمد» تبرئه کرد. حکم اعدام این شش تن پیش‌تر در دیوان عالی کشور نقض شده بود.
سایت هرانا چهارشنبه ۳۰ اردیبهشت گزارش داد شعبه ۱۳ دادگاه کیفری یک استان تهران، میلاد آرمون، علیرضا کفایی و امیرمحمد خوش‌اقبال را بابت اتهام «مشارکت در قتل عمد» آرمان علی‌وردی، از نیروهای بسیج، محکوم کرد. هر یک از آن‌ها به پرداخت سهم مساوی از دیه کامل یک انسان و پنج سال حبس محکوم شده‌اند.
طبق گزارش هرانا، نوید نجاران، حسین نعمتی و علیرضا برمرزپورناک، سه متهم دیگر این پرونده، به دلیل «فقدان مدارک دال بر وارد کردن ضربه به ناحیه مشخصی از بدن علی‌وردی» از اتهام مشارکت در قتل عمد تبرئه شدند.
این حکم ۱۵ بهمن سال گذشته صادر و سه‌شنبه ۲۹ اردیبهشت به وکلای این افراد ابلاغ شده است.
این شش شهروند معترض در آبان ۱۴۰۳ از سوی همین شعبه به اعدام محکوم شده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75567" target="_blank">📅 17:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=Dn8bDgjJpgwshoNoRoO1mZf-haY9NlO5JzEsumtjTNnRyBNFN8oVYO30jXMn5NFwzHttGQZ0fS36Mt9HSYtnYMI4GL1EUN02ejIwH5OAQ9MjGAKoZ5TrNcHS2BzFIxx99GIkQhJ8bWy9RMgXVnqVUIy_JDI-QK6Qe3SRMl8esFBkulqIzBzcqL1LChJpuOiNKRNGuT6A1JBm6P-4yKO_B_osFuZzyN29BgCCEK9Ak02_bbJMwtlPULUnlYLQpKd_xqnOWu5p2fZBWxuvik_BZLbah6Rw33ayJO-RKRZY2RSmTIUhHFIqE1jtJDc9UBwiHb9h4RyGTWqKrgkSIEEgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=Dn8bDgjJpgwshoNoRoO1mZf-haY9NlO5JzEsumtjTNnRyBNFN8oVYO30jXMn5NFwzHttGQZ0fS36Mt9HSYtnYMI4GL1EUN02ejIwH5OAQ9MjGAKoZ5TrNcHS2BzFIxx99GIkQhJ8bWy9RMgXVnqVUIy_JDI-QK6Qe3SRMl8esFBkulqIzBzcqL1LChJpuOiNKRNGuT6A1JBm6P-4yKO_B_osFuZzyN29BgCCEK9Ak02_bbJMwtlPULUnlYLQpKd_xqnOWu5p2fZBWxuvik_BZLbah6Rw33ayJO-RKRZY2RSmTIUhHFIqE1jtJDc9UBwiHb9h4RyGTWqKrgkSIEEgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین هم به خدمت شی رسید.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75566" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SCtxp76U_kZviqPs9KcTIjopJcD4cg-AYZoWjUIeJTxKJA5YNTbvawYo83UfUOdeWhQALAgGJJBS3qlcKP6reUKCWZ45Gh48MGoDelbmiZbAVdV9bi7mHUQhd7lnADzFQmw5TzRAdctNQnvovXwzInJi7Fo1aWtIJ6aOmVcZQwJIF7G8roeE8qQ7R_9BdM6RFkBeP0eWyfv3lvyGms8wvTn7tIZXocg4puSx36uBy2hwnA8c2g5lZ2_UO7nG0q7peYkUDb96MVd78AI1C8v60pV7CfeXKC8uFsn6vs692ZrDNixV5_LdWUizK5JDamHPVsLvU2tga3VkpTsmrfgaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین
تیتر نیویورک‌تایمز: هدف اولیه جنگ، روی کار آوردن رئیس‌جمهور تندروی پیشین به عنوان رهبر ایران بود
بخش‌های خبری مطلب:
به گفته مقامات آمریکایی، حمله اسرائیل که با هدف آزادی محمود احمدی‌نژاد از حبس خانگی در تهران طراحی شده بود، بخشی از تلاش‌ها برای تغییر رژیم و به قدرت رساندن او بود.
چند روز پس از آنکه حملات اسرائیل در آغازین روزهای جنگ، رهبر ایران و سایر مقامات ارشد را به قتل رساند، پرزیدنت ترامپ علناً اظهار داشت که بهتر است «شخصی از درون» ایران کنترل کشور را به دست بگیرد.
اکنون مشخص شده است که ایالات متحده و اسرائیل با در نظر داشتن شخصیتی خاص و بسیار غافلگیرکننده وارد این درگیری شدند: محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران که به دلیل دیدگاه‌های تندرو، ضداسرائیلی و ضدآمریکایی‌اش شناخته می‌شود.
اما بر اساس گفته‌های مقامات آمریکاییِ مطلع از این موضوع، این طرح جسورانه که توسط اسرائیلی‌ها تدوین شده بود و با آقای احمدی‌نژاد نیز درباره آن مشورت شده بود، به سرعت با شکست مواجه شد.
مقامات آمریکایی و یکی از نزدیکان آقای احمدی‌نژاد اعلام کردند که او در روز اول جنگ بر اثر حمله اسرائیل به خانه‌اش در تهران - که برای رهایی او از حصر خانگی طراحی شده بود - مجروح شد. آن‌ها گفتند که او از این حمله جان سالم به در برد، اما پس از این خطر جانی، نسبت به طرح تغییر رژیم دلسرد و ناامید شد.
او از آن زمان تاکنون در انظار عمومی دیده نشده است و مکان و وضعیت فعلی او نامشخص است.
...
اینکه آقای احمدی‌نژاد چگونه برای مشارکت در این طرح به کار گرفته شد، هنوز در هاله‌ای از ابهام قرار دارد.
...
سخنگوی موساد، سازمان اطلاعات خارجی اسرائیل، از اظهارنظر در این باره خودداری کرد.
...
مقامات آمریکایی گفتند که این حمله - که توسط نیروی هوایی اسرائیل انجام شد - به منظور کشتن نگهبانان مراقب آقای احمدی‌نژاد و به عنوان بخشی از طرحی برای رهایی او از حبس خانگی صورت گرفت.
این حمله آسیب چندانی به خانه آقای احمدی‌نژاد که در انتهای یک کوچه بن‌بست قرار داشت، وارد نکرد. اما پاسگاه امنیتی در ورودی کوچه مورد اصابت قرار گرفت. تصاویر ماهواره‌ای نشان می‌دهد که آن ساختمان ویران شده است.
در روزهای پس از آن، خبرگزاری‌های رسمی روشن کردند که او جان سالم به در برده است، اما «محافظان» او - که در واقع اعضای سپاه پاسداران انقلاب اسلامی بودند و همزمان وظیفه محافظت و نگهداری او در حبس خانگی را بر عهده داشتند - کشته شده‌اند.
مقاله‌ای در نشریه آتلانتیک در ماه مارس، با استناد به منابع ناشناس نزدیک به آقای احمدی‌نژاد، نوشت که رئیس‌جمهور پیشین پس از حمله به خانه‌اش از حصر دولتی آزاد شده است؛ این مقاله آن رویداد را «در عمل یک عملیات فرار از زندان» توصیف کرد.
پس از انتشار آن مقاله، یکی از نزدیکان آقای احمدی‌نژاد در گفتگو با نیویورک تایمز تأیید کرد که آقای احمدی‌نژاد این حمله را به عنوان تلاشی برای آزادی خود تلقی کرده است. این فرد مطلع گفت که آمریکایی‌ها آقای احمدی‌نژاد را شخصی می‌دانستند که می‌تواند ایران را رهبری کند و توانایی مدیریت «وضعیت سیاسی، اجتماعی و نظامی ایران» را دارد.
این فرد مطلع اظهار داشت که آقای احمدی‌نژاد می‌توانست در آینده نزدیک «نقش بسیار مهمی» در ایران ایفا کند و اشاره کرد که ایالات متحده او را شبیه به دلسی رودریگز می‌دید؛ کسی که پس از دستگیری آقای مادورو توسط نیروهای آمریکایی در ونزوئلا قدرت را به دست گرفت و از آن زمان همکاری نزدیکی با دولت ترامپ داشته است.
...
در چند سال گذشته آقای احمدی‌نژاد سفرهایی به خارج از ایران داشته است که به گمانه‌زنی‌ها دامن زده است.
به گزارش مجله نیولاینز، او در سال ۲۰۲۳ به گواتمالا و در سال‌های ۲۰۲۴ و ۲۰۲۵ به مجارستان سفر کرد. هر دو کشور روابط نزدیکی با اسرائیل دارند.
ویکتور اوربان، نخست‌وزیر مجارستان در آن زمان، روابط نزدیکی با آقای نتانیاهو دارد. در طول این سفرها به مجارستان، آقای احمدی‌نژاد در دانشگاهی مرتبط با آقای اوربان سخنرانی کرد.
او تنها چند روز قبل از آغاز حملات اسرائیل به ایران در ژوئن گذشته از بوداپست بازگشت. زمانی که آن جنگ درگرفت، او حضور علنی کمرنگی داشت و تنها چند بیانیه در شبکه‌های اجتماعی منتشر کرد. سکوت نسبی او در مورد جنگ با کشوری که آقای احمدی‌نژاد مدت‌ها آن را دشمن اصلی ایران می‌دانست، مورد توجه بسیاری در شبکه‌های اجتماعی ایران قرار گرفت.
...
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75565" target="_blank">📅 06:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RngJ9ut3EUmNoxoEXPxvOsImQu1TbALJ2OaU5HeQTWGCrkQjiymx_sTkFaQTJWUJ2XEsNvsdnT7RclUmfWD311Pn2iUDfBsm1nAheuWWUlUIL0birpRbPE4-vmnOVUJ3EoWg1sfCgsocCWIofRIQeTvXbULX8yDs0rgGR2fsZp86e5bHw88JGt1qcMeRKU4rWyo69P37WZDPoMcBdJAtf8N2IVG4tqL039_8RqrwYAZbv8SnCz9PoraDvqh1-Jsq_jtClN5_2LAUCSLmCSrUNtiHy1nHYE_aZsZAkfZlvzW9ch_K7q03x0wYQBLnh6ZGj_JYLGI1j6_nBU_kl-Pz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در یک سخنرانی در کاخ سفید گفت  ایران قرار نیست به سلاح هسته‌ای دست پیدا کند. نمی‌توانند سلاح هسته‌ای داشته باشند. ما نمی‌توانیم چنین چیزی را تحمل کنیم و آن را تحمل نخواهیم کرد.
او گفت ما نیروی دریایی آن‌ها را نابود کردیم. نیروی هوایی آنها از بین رفته است. سامانه‌های پدافند هوایی آنها از بین رفته است. تمام تجهیزاتی که برای جنگ استفاده می‌کردند از بین رفته است. تقریبا همه چیز از بین رفته است.
ترامپ افزود: نمی‌خواهم بگویم رهبران آنها از بین رفته‌اند، چون بیان آن چندان خوشایند نیست، اما واقعیت همین است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75564" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tC0UPzcHlfTzK58PkGj2ICQgMorrljhUGn56ONJDnALQvSY5biW5Akldrn4EV3L9i2W0ndC0bkej7nTEFluIxfHrgR1Dha5H8jlqq7p-R-22kSV-S_gp4L-36p_4CO6tvn6w8zQUkZsaUdOrNThEvp95JMB8-yppT57a5zCDkbPEfGOpaeFttYqZPxuFmemW_N6PXsvNbj_-Rec0s5fKo4nW-bYAllVmnS4gxmJrgdoPfEqjWe1EYEffPQcOW0JnMDvRgXmLjzOSu5YMN62T51Tv0TsDphNxg5MXYEnfY87Je_FdGoixi7W3XP6vj4G2lI0iuEZCuM2g_re_BQcqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه در قشم
آپدیت:‌
تصویر بالا:
#زلزله
به بزرگی ۴٫۷ در عمق ۲۰ کیلومتری بندر لافت در جزیره قشم هرمزگان
پیام‌های دریافتی:
سلام وحید دو زلزله شدید بندرعباس رو لرزاند
ساعت ۳:۱۱ دقیقه بندرعباس زلزله اومد
همین الان ساعت ۳:۱۲ دوبار به مدت ۱۵ ثانیه وحشتناک بندرعباس لرزید
من بندرعباس هستم دو بار لرزید
زلزله اومده خیلی بد بود
زمین لرزه نسبتا شدید ساعت ٣:١٠ بامداد بندرعباس
بندرعباس هستم فکر کردیم باز زدن دقیقا ۲۰ ثانیه همه جا میلرزید
چند دقیقه پیش زمین لرزه نسبتا شدید اومد دوبار تو فاصله خیلی کم بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75563" target="_blank">📅 03:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSAWkvNSTil7CEOGTb23xG4AFo3CWH_G_hIaCU9EoekueEveA4fs_vLraDLXgVjPH-nGDEOFuBJYGh7Mt5j0YpTpRFqleh2lQnKovi5I56-hZp9yUgjGvp0IwyMXjf0W1UvIOtxkJ6HFXYQpqwPbMdJW83SZj-SOr2axyhVqr0g3IbIZUjfrI_KGt4eaDBxkv0aG9Vq4hSq3oknUMbKBCfvkVYv5I9YCTeduwMOgNfVy0G6DnC-_JBA6Cmx2hRyB61CJ_kaiotMJwdipz_bDNQo3t2OtheywdrkuS2XyoQlyyFsihse2qhZT6YubmSVWMrXO4QXJa-4ak_yJpBeEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا روز سه‌شنبه قطعنامه‌ای را برای توقف اقدام نظامی در ایران پیش برد.
پیش بردن این قطعنامه پس از آن صورت گرفت که سناتور جمهوری‌خواه، بیل کسیدی از لوئیزیانا، به آن رای مثبت داد. کسیدی چند روز پیش، در رقابت‌های درون حزبی ایالتی برای ادامه حضورش در سنا، به نامزدی که از حمایت ترامپ برخوردار بود، باخت.
به گزارش سی‌ان‌بی‌سی، با وجود اینکه قطعنامه اختیارات جنگی با نتیجه ۵۰ به ۴۷ به تصویب رسید، اما هنوز احتمال کمی برای تبدیل شدن به قانون دارد. این قطعنامه باید ابتدا در سنا به تصویب نهایی برسد، سپس مجلس نمایندگان به رای بدهد و سپس نیز، دونالد ترامپ به احتمال قریب به یقین، آن را وتو خواهد کرد.
@
VahidHeadline
چهار جمهوری‌خواه هم‌حزبی ترامپ همراه با همه دموکرات‌ها به جز یک نفر، به آن رای مثبت دادند. سه سناتور جمهوری‌خواه نیز در رای‌گیری غایب بودند.
باوجود تصویب این آیین‌نامه، حتی اگر قطعنامه‌ای در سنا با ۱۰۰ عضو هم به تایید برسد، کار دشواری در مجلس نمایندگان خواهد داشت که تحت کنترل جمهوری‌خواهان است و پس از آن نیز باید دو‌سوم رای کنگره و سنا را داشته باشد تا بتواند گزینه وتوی احتمالی رئیس‌جمهور را دور بزند.
طبق قانون اختیارات جنگی آمریکا مصوب ۱۹۷۳ که در واکنش به جنگ ویتنام تصویب شد، رئیس‌جمهور آمریکا تنها ۶۰ روز می‌تواند بدون مجوز کنگره عملیات نظامی انجام دهد و پس از آن باید یا جنگ را متوقف کند، یا از کنگره مجوز بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75562" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GUlCsuCaqMhhpofbYwfwGGP2XSyfj3pA8zNnz5uxmY7Xck24j430f9fO-QMWHtek1RmbjHs1wUH02r0T51tZpi2z3_b8ADH-XA68wNak9SVGDYiIDcCbZ_OShNvmUsdxnM3VQXZuQeGxxzRdEW1-TT1RtRjCO2z2bl2-A9gd2l7VeEaF0MODaWG5s44-NlAe_Z0xzTb1pY_5EYXl4Dnfb0gS0nGvbahl9y--hzEnFKtAadQ7dYYUXIabSBcVrz7KFta7EFM_cUIDrRxaeIlV5chM-5ygEcA4JYNkezCvcqEnuftWiB_OP9GIaTOvjEmwPmCgj2mlKIgb1NB0Ndw5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f9OT9-mMBegKscr1-JSRw4Tkq9RCKbrEb-0P-4ebns8F6Yi2ojSrtiWG7yUL9Jkz1qD8-CemZORnPO7EsPtUsF73DxDZdVbb4voh5jqr9GhSM8-6c4Y9vHrzHowhxw_malj3fklgXEXADfhOMVWaCTl4jtpBCm8I2RiH57BMstkOOPxuKBFFPjYoxliPkYVtg-GbFswYIfRfIWKoLMtAOHXTrFskC6hAoqrSqQiK67ZBJN5N_iuCiU-YeSEUHBikd1cUh6bzx3xdv_8qwXHTn-3a6UyW7Ew0Rk7Wkqxcd7QA4YuNp6xcBwy7CDOUvn56uC16FgUWFaFn2eS8gWF6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hzMcUM4nG037mQJ2C4_GVnIzv46GgpsId15MLbbXPdrNEYYFuM5A5HARLySEnykkqe61GUYJPddTMXqIca6cNZY7vE9biA4gx7orpt8E-F6pMbb1cClLecpJ-4hnHXwjz22HFDygsfiDxntvHcqXEK3VT0vIu6jzm5v46ALXzzoBzaVvYgD57qg5UvZPRa8BprsoIUpKH7MSndUGyxX73c5_7J-v6M9sQroLZtRY-GTTBgDvBk8WUWd2nbM2NDDxDH_NIN3AmZrcN_2XzHJqL58mD9RgoJ680_5wF7ZeJboRGALxw0rrCxnnqde6orUn7oodXE-mb7ZKMCAIj7e_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y957ehYd1YV9rpumLeRAz5J-y8KNuqgUZKnUhVu6BNSZik9l_XvhWhNKYyyIFepDeGYCZ-zv76iFhkzvBmgtReAbmV0WhT3kiNCkulvcpXrDUR5lN_CF9XD8LEj5J5_DWY9aPt0be7eYq4_RjLjwNETrf3-r0oPEah2Vwy4mVEcBrhYinMqn4OGV9FyyRbpLkIVpu2M90MviYyUbFkfts2TbZnMexTKjCjGc_VPZUCGAKlXRl8_G5MPhts7yv_HQ-jCTsJtLv2FFvzhcl7bXR5iuvX7TQehggeqWkug-YnDxmpdtnlQ1nnpMQtHSXoBkDwkfSGZbcWTYweEgzbCpYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=dSjuIgxSd-53Hi2GV6C-9rXYRvpQlhGsYRSqkeNgKdE01HHv7ruOrJl3JvK_L96dDyfa5JwKIEmCypl8BfQorVoBQnN6d_Zgt4h945JfMI45xED4oZILH98y-j-h_MsX_E9gQoVADz-hDGD30RocF-2MsNVkJm5AQMk8sKoCb3ayCMuG7bOCmM-0m7KFuxQbgwgpDLOwJAjGHwiGKMyGgCr1EeCWziFh6N01uUt1zqEgeBAQT1wUCb4wXDffGNoi_zGgaPfV42q_AwAeCIF845VLy5HWHtDrjyrW1ag17RBhA2v2w5Df4CGRU2cNBAIFaaLu63ZQ5EGlw9j1hs0Ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=dSjuIgxSd-53Hi2GV6C-9rXYRvpQlhGsYRSqkeNgKdE01HHv7ruOrJl3JvK_L96dDyfa5JwKIEmCypl8BfQorVoBQnN6d_Zgt4h945JfMI45xED4oZILH98y-j-h_MsX_E9gQoVADz-hDGD30RocF-2MsNVkJm5AQMk8sKoCb3ayCMuG7bOCmM-0m7KFuxQbgwgpDLOwJAjGHwiGKMyGgCr1EeCWziFh6N01uUt1zqEgeBAQT1wUCb4wXDffGNoi_zGgaPfV42q_AwAeCIF845VLy5HWHtDrjyrW1ag17RBhA2v2w5Df4CGRU2cNBAIFaaLu63ZQ5EGlw9j1hs0Ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهور آمریکا، گفت واشینگتن و تهران پیشرفت زیادی در گفت‌وگوهای خود داشته‌اند و هیچ‌یک از دو طرف خواهان ازسرگیری کارزار نظامی نیستند.
ونس افزود: «ما فکر می‌کنیم پیشرفت زیادی داشته‌ایم. تصور می‌کنیم مقام‌های تهران نیز می‌خواهند به توافق برسند.»
او گفت آمریکا می‌تواند کارزار نظامی را از سر بگیرد، اما «این چیزی نیست که ترامپ یا ایران می‌خواهند.»
ونس همچنین گفت: «فکر می‌کنم جمهوری اسلامی می‌خواهد توافق کند، اما تا زمانی که توافق امضا نشود، نخواهیم دانست.»
@
VahidOOnLine
جی‌دی ونس اعلام کرد که دولت ترامپ برای دستیابی به توافقی جهت پایان دادن به جنگ تلاش می‌کند، اما او همچنان شاهد وجود شکاف و گسست در میان سران ایران است و موضع مذاکراتی تهران شفاف نیست.
معاون رییس‌جمهور آمریکا گفت: «خودِ ایرانی‌ها هم دقیقا مطمئن نیستند که می‌خواهند در چه مسیری حرکت کنند؛ آن‌ها در حال حاضر کشوری چندپارچه و دارای شکاف هستند.»
او در ادامه افزود: «در ساختار حاکمیتی این کشور، رهبر وجود دارد و در رده‌های پایین‌تر از او نیز مقامات زیادی هستند که بر روند مذاکرات نفوذ دارند. به همین دلیل، گاهی اوقات اصلا مشخص نیست که موضع واقعی تیم مذاکره‌کننده چیست.»
ونس  با اشاره به اینکه هنوز روشن نیست این تشتت آرا ناشی از ضعف در هماهنگی است یا سوءنیت، تاکید کرد که نتیجه این وضعیت، ایجاد فرآیندی مبهم و سردرگم‌کننده بوده است. ونس در پایان گفت: «با اطمینان می‌گویم که گاهی درک این نکته که ایرانی‌ها دقیقا می‌خواهند از این مذاکرات به چه هدفی دست یابند، بسیار دشوار است.»
@
VahidOOnLine
جی‌دی ونس گفت اعضای تیم مذاکره‌کننده جمهوری اسلامی برخی ویژگی‌های ایرانیان، از جمله «هوش و سختکوشی» را دارند، اما همزمان مواضع «بسیار تندروانه» نیز در میان آن‌ها دیده می‌شود.
معاون رئیس‌جمهوری آمریکا با توصیف ایران به‌عنوان «تمدنی بزرگ و پرافتخار» گفت مردم ایران «شگفت‌انگیز» هستند و جامعه ایرانی-آمریکایی در ایالات متحده نیز نمونه‌ای از این ویژگی‌ها را نشان می‌دهد.
او در عین حال افزود گاهی مشخص نیست تهران دقیقا چه هدفی را از مذاکرات دنبال می‌کند و ساختار تصمیم‌گیری در جمهوری اسلامی را «چندپاره» توصیف کرد.
ونس همچنین بار دیگر تاکید کرد واشنگتن اجازه نخواهد داد جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند و هدف مذاکرات، جلوگیری بلندمدت از بازسازی توان هسته‌ای جمهوری اسلامی است.
@
VahidOOnLine
جی‌دی ونس اعلام کرد: «فکر می‌کنم ما در حال حاضر فرصتی داریم تا رابطه‌ای را که طی ۴۷ سال گذشته بین ایران و ایالات متحده وجود داشته است، بازتنظیم کنیم.»
معاون رئیس‌جمهوری آمریکا که در نبود کارولین لویت، سخنگوی کاخ سفید، مسئولیت نشست خبری روزانه را بر عهده داشت، در ادامه افزود: «این همان چیزی است که رئیس‌جمهوری از ما خواسته و ما به تلاش در این مسیر ادامه خواهیم داد. اما برای این کار، همراهی هر دو طرف لازم است (یک دست صدا ندارد).»
ونس با تبیین خطوط قرمز واشنگتن تاکید کرد: «ما به توافقی که به ایرانی‌ها اجازه دسترسی به سلاح هسته‌ای را بدهد، تن نخواهیم داد. بنابراین، همان‌طور که رئیس‌جمهوری ترامپ به من گفت، ما در حالت آماده‌باش کامل نظامی هستیم. ما تمایلی به پیمودن این مسیر [از سرگیری جنگ] نداریم، اما اگر مجبور شویم، رئیس‌جمهوری آمادگی و توانایی پیشبرد آن را دارد.»
@
VahidOOnLine
ونس افزود که به‌تازگی با آقای ترامپ صحبت کرده و رئیس‌جمهور آمریکا تأکید کرده است که مسئله اصلی برای آمریکا این است که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند.
ونس یادآوری کرد که اگر چنین اتفاقی بیفتد، کشورهای حاشیه خلیج فارس نیز به‌دنبال سلاح هسته‌ای خواهند رفت و سپس کشورهای دیگر جهان هم همین مسیر را دنبال خواهند کرد.
او گفت: «ما می‌خواهیم تعداد کشورهایی که سلاح هسته‌ای دارند محدود باقی بماند، و به همین دلیل ایران نمی‌تواند سلاح هسته‌ای داشته باشد.»
وقتی از ونس پرسیده شد که آیا ممکن است روسیه مالکیت اورانیوم غنی‌شده ایران را در اختیار بگیرد، او پاسخ داد: «این در حال حاضر برنامه دولت ایالات متحده نیست. ایرانی‌ها هم چنین موضوعی را مطرح نکرده‌اند.»
@
VahidHeadline
جی‌دی ونس همچنین گفت واشینگتن می‌خواهد جمهوری اسلامی فرایندی را بپذیرد که تضمین کند ایران حتی سال‌ها بعد از دوران ریاست‌جمهوری ترامپ هم نتواند توان هسته‌ای خود را بازسازی کند.
او گفت: «ما می‌خواهیم نه فقط تعهد به عدم دستیابی به سلاح هسته‌ای را ببینیم، بلکه می‌خواهیم تعهدی برای همکاری در یک فرایند ببینیم تا اطمینان حاصل شود که نه فقط اکنون، نه فقط وقتی دونالد ترامپ رئیس‌جمهور است، بلکه سال‌ها بعد هم ایرانی‌ها به دنبال بازسازی توان هسته‌ای خود نباشند.»
او افزود: «این چیزی است که ما در مذاکرات در تلاش برای رسیدن به آن هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75556" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=plVgejP_pIz9gH9YH6DX7VBcbpyoo8GpSi4PO8xhyyhv5sad4L9ISvaXMHMsvT_lModPFz4T06Zvw9Pm9k3OGEUO0GSWEH4vypnKQ5NE_txtzZvn8dHZ4iVBOiy0MY89vSP8BYxhT8PVsCbTpFdFpK_tkFwnrrbOm3bWf29GMSASqjj7-46A0voWh4-AgFDQ7KjSeLzSjXqzeyilt1Jb4lIdhrb9n82RbCpk_4VGdoGwsjOMVLAvyxs7OukxNmaJjyIPVr-Q5XAY4BWzLrHDoe_JECtuV6h7ZNS7Ag2XcljAjBrLgyyW3fK8HBOl7991tpgp5xmZT6QdAuEtMIZv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=plVgejP_pIz9gH9YH6DX7VBcbpyoo8GpSi4PO8xhyyhv5sad4L9ISvaXMHMsvT_lModPFz4T06Zvw9Pm9k3OGEUO0GSWEH4vypnKQ5NE_txtzZvn8dHZ4iVBOiy0MY89vSP8BYxhT8PVsCbTpFdFpK_tkFwnrrbOm3bWf29GMSASqjj7-46A0voWh4-AgFDQ7KjSeLzSjXqzeyilt1Jb4lIdhrb9n82RbCpk_4VGdoGwsjOMVLAvyxs7OukxNmaJjyIPVr-Q5XAY4BWzLrHDoe_JECtuV6h7ZNS7Ag2XcljAjBrLgyyW3fK8HBOl7991tpgp5xmZT6QdAuEtMIZv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا سه‌شنبه به خبرنگاران در کاخ سفید گفت ممکن است مجبور شویم دوباره به  ایران ضربه بزنیم، مطمئن نیستم.
او گفت منظورم این است که دو یا سه روز، شاید جمعه، شنبه، یکشنبه، چیزی در این حدود، شاید اوایل هفته آینده؛ یک بازه زمانی محدود، چون نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای جدید داشته باشند.
رییس‌جمهور آمریکا ادامه داد که او دوشنبه تنها یک ساعت با تصمیم‌گیری برای انجام یک حمله فاصله داشت، اما این حمله را به تعویق انداخت.
او افزود جمهوری اسلامی برای رسیدن به توافق التماس می‌کند.
ترامپ درباره جنگ گفت: «همه به من می‌گویند این کار محبوب نیست، اما من فکر می‌کنم خیلی محبوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75555" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=AkjdTON-aS6MtzdorhxkH9ufDZy2rrlfSbir13oLLY-P9NM3c877MWPK_z7uZl2GU1YxR12gDX58RWcguDDeb1IpR_OwW9-vStPJa63rf1-2PyEm5VOjlThqbheRttM_jJTEbD5wuj4fQi-XB2J0FYFpjJcN-cRY7qzwxNYA8xU1HnM8QmDYEgWgYsts6INYcplul5Cgbl160bLvQoaFbPDA4amGN1Pz1ixWaJSN00GQxp5_Ldx8yWkNM4GK_gEcvnU7ZLAunB16a-HQhrxhbFvrkbWP8X46So3JXku8xZTi9eZLxivFAaYWqZ3fyaNvfmtU3MchFi9qFnnQtFpmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=AkjdTON-aS6MtzdorhxkH9ufDZy2rrlfSbir13oLLY-P9NM3c877MWPK_z7uZl2GU1YxR12gDX58RWcguDDeb1IpR_OwW9-vStPJa63rf1-2PyEm5VOjlThqbheRttM_jJTEbD5wuj4fQi-XB2J0FYFpjJcN-cRY7qzwxNYA8xU1HnM8QmDYEgWgYsts6INYcplul5Cgbl160bLvQoaFbPDA4amGN1Pz1ixWaJSN00GQxp5_Ldx8yWkNM4GK_gEcvnU7ZLAunB16a-HQhrxhbFvrkbWP8X46So3JXku8xZTi9eZLxivFAaYWqZ3fyaNvfmtU3MchFi9qFnnQtFpmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی کارزار ایران‌اینترنشنال برای یافتن هویت پیکر جاویدنامان در بیمارستان الغدیر تهران، ویدیویی از لحظه قتل جاویدنام آیدا عقیلی به دست ما رسیده است.
آیدا عقیلی، ۳۴ ساله، شامگاه ۱۸ دی ۱۴۰۴ در شرق تهران با شلیک دو گلوله ماموران به سرش کشته شد که پیکر او را پیچیده در پتویی چهارخانه در حیاط پشتی بیمارستان الغدیر یافتند.
@
VahidOOnLine
مربوط به این تصاویر تکان‌دهنده: @
VahidOnline
این ویدیوی دلخراش: @
VahidOnline
اعتراض‌های چهارشنبه ۱۷ دی:@
VahidOnline
#بیمارستان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75554" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5uNM7K9Zt6cFuP3B3X3ZS1TCe_OH3LjmFbrBRRdZjweRtSzn1Uvfe9mx8TTpiqUPfLXU3tGhPIPB4NXJLN5lWMxj4nxLfS3doffTuh1bk-dW2BR4vVhAtnGENP2UwKzdh1RaC3wbEfNzumXVW7ZEMr-ou0TVQiEzd0-d__cdx74w0MNmyld0rPMNo_0UnSp4ZIqON4jZPKDSWsqUxJe_-PcExlVhCAKTPtoerGhcxyHc8XOejwwh4RlRoDTl1lZTk4nrTTTTR4QSkV_1Ed1_3hlEc2sDGRhtuZ4eYbNdvtpD6JiTACOMPtavEmtqZzY_keHSTTOoaMFrMzOg074wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرش زاد
:
آمار نشون می‌ده در سه ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75553" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnE_czF4QWekatwX7DSxQFmhBzgDR_l8pNHq6fSIGJlYT2vghzJgTNWwPx8GJq-tMaOLR7iY2BZ5XWHCrZqaQ1ZU-KeEWktA5AwBUpEsHde1FRQMROYT3mRu-ZZXAz-N3ssC6KlvqpXTwPxyl8mJ2yvFYhAK5VqAdq1OFTtW6-MgoQ9Z3f6d9dNkuCuydNB0KXU7TI6ShTh9xUPI7nNj0toZgAgtMib-WY8YxHYAcXITemKby8I2v_QYcMHOMJhy_LOwdkjj5M3eL5CfItDmSWiEJ_9IFS8WlixcZVRMoVW2OlyHE3CA9HDO2zvYPpGvHEKMOtt_I5MIrnLt5wyJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی ایرنا در گزارشی تصویری با عنوان «مهر مادری به عمر چهل روز»، داستان زنی را منتشر کرد که در جریان جنگ ۴۰ روزه، سرپرستی یک نوزاد رهاشده در بیمارستان را برعهده گرفته است.
در این گزارش، برای نخستین‌بار تصاویری از یک زن ایرانی بدون پوشش سر منتشر شد؛ موضوعی که بازتاب گسترده‌ای در افکار عمومی یافت.
با این حال، دقایقی پس از انتشار این گزارش، چهار تصویری که در آن زن بدون پوشش سر دیده می‌شد، از خروجی وب‌سایت ایرنا حذف شد.
@
VahidHeadline
+ بحث‌هایی دیگر:
twitter
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75552" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHadRDKUKiXmKd0gdgrq5p1HQFjoql0Ap2byNMs-I1R0ISy12y_-i0ZG-CKFCibP2oXwr-3JGuvmoDmAMPkSzTDrtWBoBS8N5cXsfu1t9sgMdAQBuGPEqN_G922vaBN2-fCo3LJFbHegdMFWll_ah2gFfF_csKAx6ngeGeDSepQAfhmo2xpY7of8YcdVtR_kbaHAOwWQrInYk8OD5X04Z6UvIOp0dPz0sWyoyd7mu_jHDDlBKHUooA0c4SlaNZU0uOVZUE6dGfsg2JSQ39by1gt76AZgkqUrt5pu9QyJb7_iaLqNW23mwy5KE0xIQJvuAq1nwqxXRx1GFn29DXLOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایووت کوپر، وزیر خارجه بریتانیا روز سه‌شنبه ۲۹ اردیبهشت هشدار داد که جهان دیگر نمی‌تواند بیش از این برای بازگشایی تنگه هرمز صبر کند  و ادامه بسته‌ماندن آن امنیت غذایی کشورهای آسیب‌پذیر را با بحران جدی‌تری روبه‌رو می‌کند.
وزارت خارجه بریتانیا روز سه‌شنبه اعلام کرد کوپر در کنفرانس جهانی مشارکت‌ها در لندن، با اشاره به پیامدهای بحران جنگ ایران بر انرژی، کود کشاورزی و قیمت مواد غذایی، خواستار فشار فوری بین‌المللی برای بازگشایی تنگه هرمز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75550" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XABr-IAJSBh5dRkdPq1Wl7jlDLXHuULorbWwYeTAGdyq0td1XNfnaQeIK0DzMRX_4upB47IFYT5kyQaVr99_NrNE2vjRXmjgFCNeCNTgF04iATNbE94GsO8tF04pPBLf7ddIj_bvvYkSXtjtZnN0AbU1PME9bAHycGv2f48JqSG0pj48PIpPiRJ_U5pBTZ3jXwSCnBaRyhcqKYXRMYA0xU7tblVUsBV6Q4q9N0qUcs7D7RxOaGuoYOWK4ze2-m30d613JtNh6pXdRijsVyF56dSQwCL12NBqtyvbI5mvZD08a7HRSZGriVa_CPQ78Ot00M7NhMpbQRbjOOJlZfVTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه ایران می‌گوید تهران در پیشنهادهای اخیر خود به آمریکا برای پایان جنگ میان دو کشور، خواستار برخورداری از حق غنی‌سازی، خاتمه جنگ در تمام جبهه‌ها از جمله لبنان و خروج نیروهای آمریکایی از محیط پیرامونی ایران شده است.
کاظم غریب‌آبادی که روز سه‌شنبه ۲۹ اردیبهشت برای ارائه گزارشی در مورد روند مذاکرات میان تهران و واشینگتن، در کمیسیون امنیت ملی و سیاست خارجی مجلس حاضر شده بود، از دیگر شروط ایران را «رفع محاصرهٔ دریایی آمریکا، آزادسازی اموال و دارایی‌های ایران، تأمین خسارت‌های وارد شده در جنگ توسط ایالات متحده جهت بازسازی و خاتمه تمامی تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت» اعلام کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75549" target="_blank">📅 17:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4RGngNAQ5HaV07RDO618f78-ps-Ep9uPEHjYwdFd4o42UA8z7iRax3EMSDiIgmq11gZyDWJDTQAU0JAhXX5xkwm9Ryeb4_Wumv9VDHcdqJLWfslO0L89QjB7128DHqIdKLTXBFF8KXDHiz-4u-W-m8r4ZgvI6LFhuAIbha-ZQnRWQ12rCXIIX6-AXwjBEYkzde0wAtU96-hDXNrDj8QPNRZEBd6_XrYq4_7MQxIWBFt7svrfxta8_kUTYm40RVgoMskvu-cyXIoVqKRqq3KrtPZnfysSKlgsdcfmHjaQt_zyKyMa6eh56UQI100LyELhajC04y_k2VmUJOHht-bWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان «کمک به گروگان‌ها در سراسر جهان» دوشنبه شب اعلام کرد شهاب دلیلی، زندانی سیاسی و کاپیتان پیشین شرکت کشتی‌رانی ایران، پس از آزادی از زندان اوین از طریق ایروان به واشینگتن منتقل شده و به خانواده‌اش پیوسته است.
این سازمان اعلام کرد دلیلی پس از گذراندن بیش از یک دهه «بازداشت غیرقانونی» در ایران، اکنون در سلامت کامل قرار دارد.
شهاب دلیلی که ساکن آمریکا بود، سال ۱۳۹۵ خورشیدی برای مراسم خاکسپاری پدرش به تهران سفر کرده بود اما هنگام بازگشت توسط نیروهای امنیتی بازداشت شد.
خانواده او گفته بودند جمهوری اسلامی او را با اتهام‌هایی از جمله «جاسوسی» و «همکاری با دولت متخاصم» به ۱۰ سال حبس محکوم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75548" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khDTLk2hD93vfjIeu58V30Nfry9QO08HEsLgHwhH-4jJyG4EA1re46Xi7MKAY1ODa4GlgQ3ukKSpwJsKuPjHsPwqKKNtRg70ial63BxUHssH9ShHs7wBdtgPxsW6Sorcuqg1W_6JHfKLf8YffL9szJzO8pMgakE1OHCtq72v7ZdnXKYd3lxa5qGktCtRU4uc7Q8bU5nMvcf2Y3T1v7rDKSfnvquvrG3qSHTmn0SWcoT_Z5iqYFnSkavcKbJDXsbP_qs5jrFbH0MmDwAeyvbSaVUQc93cW1bjvGRAARlN0N4baDCBVnZx28Zc_83YxM0Iz9E37lNHoacxWVJzfiJy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.
به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.
اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع و تبانی با هدف اقدام علیه امنیت ملی» عنوان شده است.
بازداشت او در پی انتشار مطالبی انتقادی درباره کشتار معترضان در دی‌ماه و همچنین اعتراض به اعدام‌ها در شبکه‌های اجتماعی صورت گرفته است.
آقای تیزرویان از عکاسان برجسته و سرشناس حیات وحش است و ثبت عکس‌های کمیاب از حیات وحش ایران از جمله خرس قهوه‌ای و مرال به عنوان گونه‌های‌ در معرض خطر انقراض، بخشی از کارنامه کاری این عکاس حیات وحش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75547" target="_blank">📅 17:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/olmjmuPVIP2m0T1nHtXJhZJZR8yUCGUs_YOvYO5f1dK6nerARkQWkwCJw2uSx8KAr2tFAYOEzAEMR5kdtd-dRWHGCksEzGqEwgH6Z_Tqgg2wg6JkBefNAFOJAkierUGNo25nZ1j-0z6JWZ1BlNdFNJc8cVTKn4-A-T3aHcaMiSP_-JV67OSr59hTbci-EqUv3czkQXd_skS1L2f7eJAtN-Tyh8vQ293X2DYUUTv8qbcVk0wuAjDKTEK5hCECRqYUhrhTBQvCRSC2oYCjeR5n4DyIkuKqq45Rwdk19X7Xwn-NY0I77D0Fa_Kg87EzVmf6O_q4VTsxbYh0D6Rd9LfSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر صدا و سیمای جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75546" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3F6qfM4cQwCH5OQBkydvH2HwltNiXtnQ3esDJBK1KlL1dlMd6XkM6N9DvnikVXIPp7WgeiQIW-U26YIQtCJCY_MoM1tX20b2zQIiQDuReOwGZ0Z15V5giaZlXzcxrjjluL6Ry30RkcfcUdRpXC3zswnoh33JQ2fslQMKMK1G7xxzb9SuXURyBudZRIyddexG0WK4u7vR1jkmDGmpzAO_K5oCxM5-uzs_6uzmnD2BSftE5pKgU3pA3OQV6y_0If0vipF2yHmhPwdLVX6KYOOu-p1UpL0WDTBIQxwy1EUDZv-iKT7ZZzz9TsK1K-eWLzb6trtYfvXyEnrlqMbriQBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله فردا را به تعویق انداختم
پست ترامپ ترجمه ماشین:
از سوی امیر قطر تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی  محمد بن سلمان آل سعود و رئیس امارات متحده عربی محمد بن زاید آل نهیان، از من خواسته شده است حمله نظامی برنامه‌ریزی‌شده ما علیه جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛
زیرا مذاکرات جدی اکنون در جریان است
و
به باور آن‌ها، به‌عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین همه کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
این توافق، نکته مهمی را در بر خواهد داشت: هیچ سلاح هسته‌ای برای ایران!
بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دانیل کین، و ارتش ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده فردا به ایران را انجام ندهیم؛ اما همچنین به آن‌ها دستور داده‌ام که آماده باشند، در صورت حاصل نشدن یک توافق قابل قبول، در یک لحظه و بدون درنگ، حمله‌ای کامل و گسترده علیه ایران را آغاز کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/75545" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShNzIXkDeL7vu9ucinTJB56LWwFj_hJoptFbY06SoSjmtbyBiZo4mASVhLyO__rDNYGHRbwY1hZG-CxK4tinG1taYjSVotCx4ScNXkRcilNacGshRkSvt8KzSgYNsFjZcC5-jZ0Lg6My4VHoviJ_RuSG4tb6n12FqfEBUCb-R5630YhsrM9EVRIEe_WCIFIn-o8mjf4thnxRuxDbcGzw9pPcs0thkSSQjjY5ftQulraQEh5ZTihIdZimOIhOaZPqWCftPNYZIkI51BbgkgNh8aVItM441s545vE-BFzbZzkmv4T3c6Wv3LJqw9WncMeN4B2YymcgmdfvbOW_kgnYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز دوشنبه در گفتگو با نیویورک پست اعلام کرد که پس از دریافت آخرین پاسخ ناامیدکننده تهران در مذاکرات توافق صلح، «به هیچ وجه حاضر به دادن امتیاز» به ایران نیست.
ترامپ در مصاحبه تلفنی کوتاه، ضمن ابراز نارضایتی از آخرین پیشنهاد تهران گفت ایران می‌داند «به‌زودی چه اتفاقی خواهد افتاد».
به گزارش نیویورک پست، وقتی از ترامپ درباره اظهارنظر روز جمعه‌اش مبنی بر اینکه مایل به پذیرش تعلیق ۲۰ ساله غنی‌سازی اورانیوم ایران است سوال شد، جواب داد: «در حال حاضر به هیچ وجه آماده دادن امتیاز نیستم».
ترامپ ادامه داد: «من واقعا نمی‌توانم در این مورد با شما صحبت کنم. چیزهای بسیار زیادی در حال رخ دادن است».
رئیس جمهوری آمریکا همچنین گفت از تهران «ناامید یا کلافه» نشده، اما هم‌زمان تأکید کرد ایران به‌خوبی آگاه است که ایالات متحده می‌تواند فشار بیشتری وارد کند.
ترامپ گفت: «می‌توانم به شما بگویم آن‌ها بیش از هر زمان دیگری خواستار توافق هستند، زیرا آن‌ها می‌دانند ما...به‌زودی چه اتفاقی قرار است بیفتد».
وقتی درباره ادعاهای منابع منطقه‌ای مبنی بر اینکه ایران تلاش می‌کند در قبال هر دو مسئله هسته‌ای و بازگشایی تنگه هرمز در برابر واشنگتن «سیاست صبر و انتظار» پیش بگیرد، سوال شد، ترامپ گفت «چنین چیزی نشنیده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75544" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IptLoZfwCIOWTg43wGftcsX-e6m06x_S_HL9QNQYibm1wwVBXGbYjYnWgTMwdZhBo8u1XBpugvwXxZxjdgZ8w5WeSCRZhbU2MP6IJOVdPp4meNgagaIu5pG0QwW_UK2vS-ljvFOjoem1OX2lXx09agsp_wXGHd0BEJypm8oGwL-DmRFjPmFgGJs7nNng3Hy_s2CyElI3A2xXVpWbzagjy_riY5Mauxn1kkKRqkV5LTugIolkNgynCpohyXm7ID1lpd6nfOlEd0RCVaYj0bLdLa3kKA3TwUXyA487w1qNyqzQ4YeL0F-Hs4AVBHcSv0tr8cTsmsA-BLB6W3QkD6afLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، دوشنبه گفت که آمریکا در حال صدور یک مجوز عمومی ۳۰ روزه برای فراهم کردن دسترسی موقت به آن بخش از نفت روسیه‌ است که در دریا سرگردان مانده است.
بسنت در شبکه ایکس نوشت: «این تمدید، انعطاف‌پذیری بیشتری فراهم خواهد کرد و ما با این کشورها همکاری خواهیم کرد تا در صورت نیاز، مجوزهای مشخص صادر کنیم.»
او افزود: «این مجوز عمومی به ثبات بازار فیزیکی نفت خام کمک خواهد کرد و اطمینان می‌دهد که نفت به آسیب‌پذیرترین کشورهای از نظر انرژی برسد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75543" target="_blank">📅 21:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZSd-T0UG6Gz0o9PbhUlQgViW_dMFKZbdBs_fAoE6ilXTfsc6unwSOkwgoLunNzfQSI9vRIxP_FHqJvKsDCMNy6OpTPuOr3h3CVHzseVSJxYbWm-27JFa35XrnZqqQNaURa9gS7MPkKCPMiApqcYWVcpdRvFuXCXuEP998VIheZlT_3BvgiOdOUQPtwZsdQcbWcayenmNpdobEY9yrEx54bGijO1YZPKaJFOgIU9enX-tif6kuV8WYnrXmVU2tgKLYxiF957IC5MGDzWfmCZslPYSjpmsQjE7q1qIRObm4NUKm70CFZBnP2XtUqrjJFp-vttsaKh5DrIYQ71WM4dENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CMNaK5fQ8GOkiK0pd8Cy2E5Oq4D3J55J5Rmlw4k-GL4OH3CloVGY8wdDD-Qo4189fI0Q5-iXrGnmx0mr8XyATD49UEzawAVKSZUg0A8BQJ4uoI7MmSYQ3V_fYvYdlJdK3hOXv6M4fmCfMxTLqqWOjYS9djdvTMm8t1rUH1vce9TCS4SmQLFbswAgIR3E3yFEosvINzA3PLyvhj1rG_ypBKlHO5sjxdzcA3GjYCGuE4fA0AI8S_vkUXE1WD9QUBFcOwdLcV6WM-xN3c9smLZFCBbbPQ-2-4RYRTTEQ6NaVCiKECTOOSSqLds2KRimjuNjzzN3rXbqQrrIBHGZEdGGgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس، روز دوشنبه ۲۸ اردیبهشت ۱۴۰۵ به نقل از یک مقام ارشد آمریکایی و یک منبع آگاه گزارش داد که تهران پیشنهاد تازه‌ای برای توافق ارایه کرده، اما کاخ سفید آن را «پیشرفت معنادار» ندانسته و برای دستیابی به توافق کافی نمی‌داند.
به گفته مقام ارشد آمریکایی، اگر ایران موضع خود را تغییر ندهد، مذاکرات «از طریق بمب‌ها» ادامه خواهد یافت.
بر اساس  گزارش اکسیوس، مقام‌های آمریکایی می‌گویند دونالد ترامپ خواهان دستیابی به توافقی برای پایان جنگ است، اما هم‌زمان به دلیل رد بسیاری از خواسته‌های واشنگتن از سوی ایران و خودداری تهران از ارایه امتیازهای قابل‌توجه در برنامه هسته‌ای، گزینه ازسرگیری حملات را نیز بررسی می‌کند.
دو مقام آمریکایی گفته‌اند ترامپ قرار است روز سه‌شنبه نشست تیم ارشد امنیت ملی خود را در اتاق وضعیت کاخ سفید برگزار کند تا گزینه‌های نظامی را بررسی کند.
آکسیوس گزارش داده پیشنهاد تازه ایران که شامگاه یک‌شنبه از طریق میانجی‌گران پاکستانی به آمریکا منتقل شده، تنها تغییرات محدودی نسبت به نسخه قبلی دارد.
بر اساس این گزارش، در پیشنهاد جدید، توضیحات بیشتری درباره تعهد ایران به نساختن سلاح هسته‌ای آمده، اما هیچ تعهد مشخصی درباره توقف غنی‌سازی اورانیوم یا تحویل ذخایر اورانیوم با غنای بالا ارایه نشده است.
در حالی که رسانه‌های دولتی ایران گزارش داده بودند آمریکا در جریان مذاکرات با لغو برخی تحریم‌های نفتی موافقت کرده، مقام آمریکایی به آکسیوس گفته است هیچ کاهش تحریمی «رایگان» و بدون اقدام متقابل از سوی ایران انجام نخواهد شد.
این مقام آمریکایی همچنین گفته است: «ما واقعا پیشرفت زیادی نداشته‌ایم. اکنون در نقطه بسیار حساسی قرار داریم و فشار بر ایران است تا به شکل درستی پاسخ دهد.»
او افزوده است: «زمان آن رسیده که ایرانی‌ها امتیاز واقعی بدهند. ما به گفت‌وگوهای جدی، دقیق و جزیی درباره برنامه هسته‌ای نیاز داریم. اگر این اتفاق رخ ندهد، گفت‌وگو از طریق بمب‌ها انجام خواهد شد و این مایه تاسف است.»
در ادامه این گزارش آمده است که ایران و آمریکا هنوز مذاکرات مستقیم درباره جزییات توافق ندارند و گفت‌وگوها به‌صورت غیرمستقیم برای رسیدن به چارچوبی مشترک ادامه دارد.
این مقام آمریکایی مدعی شده که ارایه پیشنهاد تازه از سوی ایران، با وجود تغییرات اندک، نشان می‌دهد تهران نگران اقدام نظامی بیشتر آمریکا است.
در مقابل، مقام‌های ایرانی همواره تاکید کرده‌اند که این ترامپ است که برای دستیابی به توافق عجله دارد و زمان به سود ایران پیش می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75541" target="_blank">📅 20:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dz9TxWYC57jcj7-W3RN460bnMbZijjKPnJBY3DQyCVhQD2R88U_K8AJYkoIyhyJri2UqlQ-WaefO1BI4xOc-X-PDs-itejS9nnmkh9LqH8nNuLylw_4r_dq25Fxv4fo2KC315ozFf2kDJ_r5mwxnzliFhb_f8NUXapl5jMkC8LVF5FZdedgw5Ea2NyCNoIQGSo2N0rpXhj44I5yni3kloDKEySme6_LavntaLBvXucZTXU2Yc29szs_OZWLadPzx7qMK0PbsKQi1Q3gZAS9fm79xf7Z3SObdUaBUxalCoFfcQqRdAytFCtjFLBSpCfHVsWS2jR8anrLhtb20rwVp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در قعر دریا آرمیده است، و نیروی هوایی‌اش دیگر در میان ما نیست، و اگر تمام ارتشش از تهران خارج شود، سلاح‌ها را زمین بیندازد و دست‌ها را بالا بگیرد، هرکدام فریاد بزنند «تسلیمم، تسلیمم» و در حالی‌ که پرچم سفیدِ نمادین را دیوانه‌وار تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال (وال‌استریت ژورنال!)، سی‌ان‌انِ فاسد و اکنون بی‌اهمیت، و همه دیگر اعضای رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و حتی رقابت نزدیکی هم نبود.
دموکرات‌های احمق و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
پرزیدنت دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75540" target="_blank">📅 20:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMQtH4K0q7jerhXk9LB7H-MdxpasCmxds3k60J6eiUw4AtE5tzpnlbzIcetWYR_fdJisK0g2v-YGGMQSav3h2pzLNz3U32zw7WkQc-jpWIdHZt0hp8wRMY5CXMGa43b__ZLM18AkU6d_OzwdkpnJsqgEN5mlmRo4fNxar5HFKw9N7zx1rVccoiar96Or5yOVnkBRImLBWGDh47WghYhziz92MIRuGt0LVYYVb727B95m-9CjN118AST3XRoFN2ShrtMwj5DQgWSNPt6_XU_xcgBBGJdpa2_jZlVNOzzHF-WsF7tdNTIwksN6E7GXFAMNFInrOZhtWHODOkTNTyCekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر مرکز روابط عمومی وزارت بهداشت جمهوری اسلامی، روز دوشنبه ۲۸ اردیبهشت مدعی شد که در حمله اسراییل به بیت خامنه‌ای «اتفاق خاصی» برای مجتبی خامنه‌ای نیفتاده و زخم‌های او نه چهره‌اش را مخدوش کرده و نه به قطع عضو انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75539" target="_blank">📅 19:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTFmGHUDwvQqq1l2JAWlAXJf7K-O8O8KnTLZB5koL1iWmvYfSvaUedpSd4Np0EDum7MdzsEkoXSTqJCS_1kp8U3Wq5G05SmbHdn5FFZvSNWEblsQs3GXrOe31tnHHFF6rsy6hK06WPiWvHYoGaIDdTi0Eq7Ia3vqhz2UrctscTBDOlZpdLrgTyrO29GquK2WvdMbVkH8YqZXVeFX3_11CzlSRKOmZQ5Lcxm2c2k2XIW3Ywk0BnnIIFn9DAKL8de573Z4NI1zH-iMtPA5H1IuhTNI_9LF2yyBhYlEWRW9Q4D8d6HhsbolQFFZsQFyUrKtKdUw9dGx_BdrzQSwbsFIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردریش مرتس گفت که «ما حملات هوایی تازه ایران به امارات و دیگر شرکا را به‌شدت محکوم می‌کنیم.»
صدر‌اعظم آلمان در شبکه اجتماعی ایکس، حمله به «تاسیسات هسته‌ای» را تهدیدی برای ایمنی مردم سراسر منطقه خواند.
امارات متحده دیروز گفت که در حمله پهپادی، ژانراتور برق بیرون محوطه نیروگاه هسته‌ای براکه در نزدیکی ابوظبی آتش گرفته است. امارات در بیانیه‌هایش نامی از کشوری نبرد و فقط گفت پهپاد از «مرز غربی» وارد شده بود.
آقای مرتس در این پست نوشت که «ایران باید وارد مذاکره جدی با آمریکا شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون هیچ محدودیتی مجددا باز کند.»
اظهارات آقای مرتس درباره مذاکرات ایران و آمریکا اخیرا به تنش لفظی او با دونالد ترامپ منجر شد. او گفته بود مذاکره‌کنندگان ایران آمریکا را «تحقیر» کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75538" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vcvR0VKakNsmzJQKtWIIQOGk3sg0kEHeOf4k6sbcOQNX9naEoBKcw4iPLvP0kuYSgq8eHyUT2bgYHXDFCOyUu-FLx2RWii9F3pRLX_SIfpMxsrDm8AvHN1RYL1bXR0y0HSR92EwVpPKbpC-GxDpMzTnshcs8Qs4phU4p7UFVsZ0RRaNemvZQNw0JO4oTHTjZoq3YmfY5372eA4GSAGWZPjeAgqN_7l9Tr3vMvfccRYJUlnsfA7Qz5BQwlM_3Dgw-TvOM4qDQ2anwu7P8YFPycyRjZW7JXBkmtYXxdjTVe4GCA-KCBVfGNK-xeFbZXXw6DQ0_q3qnQkVwPkgPUOW8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OAd-4HKQuWPKdXt-VjZMOUgz27W749cP9S264KkOBCQtVa-UyhuyKqTzSI1_tzw91tYv1cN6Ez76Q8ovZBFgDktropOTJx3TYG6-aIrj-YKjDBUjjmvgSgJo1hNSjp6pJkz0YgmQItpgTV2fPIK-KWtDij0KqEoICump14we5TBBPmELdVIjv8DoK-gDIejbZtReMk_j9ltMrTaOkST2qyRSgfraWH9wMvYXANQEHsGqwejoDZr887B0gOktCsMfIAkvBUfGG5KAPi1Vim8uWr-3kZ0Nw6A7eyB-VJbSVp7V30Syv7NGjF40hx7VmTmfbaTUEW7KOv7SjhGlP3hefg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75536" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iruZmqkMZu3O31RLg-u-_fFHIEQYCkXwMBW7xNTU08J4Q9UHYvTM9tGeXbWvEoIYcP7JbQ-Jaw0wYSkvE1-1ULiC3x5VOeJfB8FXDsq7jl66dL4y8rjebOkTixbi9jQ6nLJLBESKoCECsExjqiDsvLtoxefiLPIVNJNmiJ7H1JtMncK6VRFqAsKvkyRJPw7WCnFx_eMUXmKW0MyMX8bMaRcdfKO4yMiQQuZNy4YK6A4tO8DVQ4vb2qcaTYN6nmJ0r4ukPJbeuq3bu-oF_M5n1GNrgkhu3IZRW4MDmLszl4ArnHtLMm17ghEEGZYsuO4cWeUKvnCyOq2sp02rlxZdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری تسنیم وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت، به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد آمریکا در متن جدید پیشنهادی خود، برخلاف متون پیشین، پذیرفته است تحریم‌های نفتی ایران را «در طول دوره مذاکرات» به‌طور موقت تعلیق کند.
به گفته این منبع، آمریکایی‌ها در متن جدید با «تعلیق موقت» (Waive) تحریم‌های نفتی ایران موافقت کرده‌اند. «ویو» به معنای معافیت یا چشم‌پوشی موقت از اجرای تحریم‌ها است و به معنای لغو کامل و دائمی آن‌ها محسوب نمی‌شود.
بر اساس این گزارش، تیم مذاکره‌کننده ایرانی همچنان بر این موضع تاکید دارد که لغو همه تحریم‌های ایران باید بخشی از تعهدات آمریکا باشد. در مقابل، واشنگتن پیشنهاد داده است معافیت‌های مرتبط با اوفک (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) تنها تا زمان دستیابی به تفاهم نهایی اعمال شود.
به گزارش تسنیم، این تغییر در متن جدید آمریکا نسبت به پیشنهادهای قبلی، تحول تازه‌ای در روند مذاکرات به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75535" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHZOT9cuzoc-5sSPXASgevO5N35VOWdZuBgGbVlcZZnd3vOHWL-fBXv9xLDdS1DcTiF0dg36lMDzVYc8lwK2x7LJRIit2omNXwATpf1POKPA8lTwSl7IVsMAWKTJDfjv-BaZIRIdwprmuH0N9eDzqtc99VLmzAU87wktJk6R8U9wy5svvN1miDw5b6JFnp7pUXZejDU0tfhWRq4qw2Z8ruZRWLHErrtHOCfttaETJQybnOdGhc5NY7nsI44UwcMi7pPi5K8dk8DwMiKM5wMkD5ZWQVxKnNXXLM60SuW9us24RWWCuDDkBnFtOs9KpIqcw_fPaaZM__w5jvAGR5kr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع آگاه گزارش داد پاکستان در چارچوب پیمان دفاعی خود با عربستان سعودی، ۸ هزار نیروی نظامی به همراه یک اسکادران جنگنده و سامانه پدافند هوایی به این کشور اعزام کرده است.
به گزارش رویترز، این نیروها از توان عملیاتی برخوردارند و با هدف حمایت از عربستان سعودی در صورت ازسرگیری حملات علیه این کشور مستقر شده‌اند.
این تحرک نظامی در حالی صورت می‌گیرد که پاکستان نقش اصلی میانجی‌گری میان تهران و واشینگتن را بر عهده دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75534" target="_blank">📅 17:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjB57m2ymUqHq-svXfzvRvDy2CT6nqANcD0_VWfnl1hPv5fUoIpaH4rZiUOHELLONuOxE5qXfthFNfblOM0AWiAXCHzE9DJ0I3g5UFflKw91Wu22NeQ35RGE22LEGIzLXLdEwVXZb0Rv0E2OJyXLBQs5qNWY3-tSSJTdbre1xKoxHRNIvv-d05oKx02YJWdFQj6fXZCmEsWBf2q5vCXnX_rXUJNRuV-mmWISN0ZHhPxaW2Ds8YYD0JpPjrRVJL9D3K1yllMqVt28WFu41L4i1KHCSm-l7xv5JDDOvLkzTt3fd8dBnXyBkIm0nXzVsq7mzK5Asb-CqVQdULnCMZ756Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کل دادگستری آذربایجان غربی روز دوشنبه ۲۸ اردیبهشت از توقیف اموال ۱۲۹ نفر در این استان با اتهامات امنیتی خبر داد.
ناصر عتباتی از این افراد با عنوان «گروهک‌های ضدانقلاب و تجزیه‌طلب» نام برد و آن‌ها را به «اقدامات ضدامنیتی و همکاری با کشورهای متخاصم» متهم و اعلام کرد که اموال آن‌ها به «نفع ملت» مصادره شده است.
دادگستری آذربایجان غربی اسامی این افراد را اعلام نکرده و برای اتهامات علیه این افراد شواهد و مدارکی ارائه نداده است.
پیش از این نیز گزارش‌های متعددی از توقیف اموال شماری از روزنامه‌نگاران، فعالان سیاسی و مدنی، هنرمندان، ورزشکاران و چهره‌های شناخته‌شده با اتهامات مشابه منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75533" target="_blank">📅 17:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6KKzLF6mpuXLvar7B_K90Vqk9bwW-lkGwkrrWW7zK1qAdNEPt4IEsjT5xvCbq67CrC1-VhPZO1Coe11nrE68uOSMRgZ27jqhbLguCF7NF6w_KLk0MXFrnr_oCxq8eM9weSjyD6ExdGnzbDpBbe5eBgIoCZ3nSXLtBYfYj8zw4l9Pm3ZkJVFFeE4Ljxb8CQElhJ1NFJf73zmKqfYjEddiAS7POK2dNkDeBuSkwcRwEt0Nu7bA7HNyIJkoyqRuKO4GASsVjnENdhb5aWa4NxFVYLqlk_WzNuHLDfp_-la6uWOboKCQglMK5wgttViIWHjqUumTGdTYs1aqJRNwposxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا می‌گوید مقامات حکومت ایران برای امضای توافق با آمریکا «می‌میرند».
او در گفت‌و‌گو با نشریه تجاری «فورچون» افزوده با این حال آنها در جریان مذاکرات، «روی یک چیزی توافق می‌کنند»، اما «بعد یک کاغذی برایتان می‌فرستند که هیچ ارتباطی با توافقی که کرده‌اید ندارد. من می‌گویم: ‘شما دیوانه‌اید؟’»
ترامپ در این گفت‌و‌گو همچنین بر این نکته تأکید کرده که مقامات جمهوری اسلامی «مدام فریاد می‌زنند» و سروصدا می‌کنند، اما در عمل «تشنه توافق» هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/75532" target="_blank">📅 17:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rV-ZpHAYe4cLDKAmqwBb6YcdnxnnaEvYIM_JDotMGnKWmjnaPxPzoBtcJf3jKm7YqRMwywy7ATU9QCHmGRdzVVt66rBe1DV9PKzTrDnYSH-qAcB7joszMqsJ_v6fP5YfCggPIDcW9mJnx9qW_klRdn3UrCnqdIDSlqTXPV9y5l-X8z-JNMI1YxzNC5XWf4kRE9cyAsQ-OjBmg5F8BkQXrv4xS9K2nXae2mJG7efNNnMZ4hcklxrXCNKLhcNxQ-LG6_j2CT8R-EmQPw9fHCBx_2EuASpGm0--qw3OLI5sROffZDgnOFyBLrOnPSdQK7tMN_JJDTkHiZYXypi0_AlV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bG71cichYw_gpa-drQml6W9zuvp7LDSi99BFetrHqkI5iSG70T3K2xo3pKORIN2uSO_IG4SmCVGcTt1lDsBEcolL_ZnD28dcsMKr9-wGHG4zLR1iB6GNGXtT_fSMbvVrrCGU_cic4kwEVQhE5wVPD30en5GrLDuG6z8cwvKDHNmdaYMtHHQPYT65ZOp9fbXXo71_mdJSoWI8VACLc9GsXUFSun9EkvJ-H3gIsv1gcXj6DZ3x4XsZ7Pm1bb5uL-Blm7AzBdM1z4KRaWOlgN2ypGPuN7IPipGZub3X6prPtroITsOU1Tu3mnISrLGBYO0-0KsifM8QyIhFdxvyehHGhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75530" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPIaqVMfcJ0Sw0gBarccUleiW9Ijunrb9c6wBf2AS6P2A0RSXBYHiWZ4g9oYfVG9giFgLB3NgBhZ3-i8ZxSQFTtHjHwdFvXNFLKiOOZCz4jY-ZaZLpc018fkya8S8CsA4mkrn_90vBB4jt8YX_s4qu8c89T4EcZuUdCbmuNgePLPsowIk1Y1yR2gD3Dh7c2diEESfFht2kmvYvvhK2Yz5sahMZTqYfuxhU3Mfpz_EJQ429lolcCs1jHnwab3vu6qoknwQslqh7-XExHcJNWBoZX9p-lEkhN-zfu6No6qkEwCRa3BFq8XOlsZOsA8kuH-d7S5vwMAybr6xtx498m45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نت‌بلاکس» نهاد ناظر بر آزادی اینترنت اعلام کرد قطعی و محدودیت اینترنت در ایران وارد هشتادمین روز خود شده و مدت این خاموشی تاکنون از ۱۸۹۶ ساعت عبور کرده است.
نت‌بلاکس همچنین گزارش داده که هم‌زمان با ادامه محدودیت‌های اینترنتی، محتواهایی در حمایت از حکومت، شبکه‌های اجتماعی در ایران را پر کرده است.
بر اساس این گزارش، برخی شهروندان ایرانی که تلاش کرده‌اند به اینترنت موسوم به «سیم کارت سفید» یا اینترنت ویژه (اینترنت پرو) دسترسی پیدا کنند، گفته‌اند از آن‌ها خواسته شده سهمیه مشخصی از پست‌های تبلیغاتی روزانه در حمایت از حکومت را در صفحات اجتماعی خود منتشر کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/VahidOnline/75529" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/akDcg0nmUi-Q32oeuZ_IbKBvpiU8X9CgWNFtjry7u-4PWgsRmf9UA1VJ5NXJrSRbFqjED3vYQIKf44s-ZxqbpWQDpYkI1DL3FWeQxBHTt9xWPIsyTizXqHajhD6sTK0SHvrXwMC-dk5vFaHw8-UAL1vc9_G_MsyaO8hVsdnroHuE9-Juq9RPTc5x9kB5zAMyhczLiESK-st-HRQicbujxJdTNlkWVuKZSNHG8igi8nCq7gM9XwvIe-1r_cev7kojuilopGJQZUIR--6gOoS6k75T2I3ot97wfMQ6628MMtSSoekKxRp2e446Te_8PIy_hXSaLt1BiNyWXqW4ORVdYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75528" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgsCP1GraEYR5brAX7UNLNWfIusu63yHAld6qzX-9t3enBKj3HJ7uB7oIJ7JW6AUMwj_ahrWIwF3jRBP4_Aer4e98oMF5CpDDbU-ew7dVg2O3Ql5ilwq7-OKR4OfiXIpGsPVjfBAaOCzq4kxW2Cg1eCEl-RosmLvt-UIcpomG9JAPWjw34v6AMB8ZclNdWAieV08V__uIi_Bf2-NLIgJOaQnjG_idB1bR0vx4r8SZfq8t9a7SkUmKvhKAs1j0hlDIgMrb4pH3fwOh4txozRP8Nn0FLu6juMnD2YOFnAiRPGvnmsE2_3so88Stoa5eMLFYsyqDEZOn7So_Vyn18bWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌های ژئوپولیتیک در خلیج فارس و نگرانی از تداوم فشارهای تورمی، قیمت نفت در بازار جهانی انرژی افزایش یافت.
قیمت نفت برنت در روز دوشنبه ۲۸ اردیبهشت با رشد ۱.۲ درصدی به بیش از ۱۱۱ دلار در هر بشکه رسید و نفت خام وست تکزاس اینترمدیت آمریکا نیز با افزایش یک درصدی بیش از ۱۰۸ دلار معامله شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75527" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C2j-s3wXr51xN3M3pv1Zznm2_GUGM70SfeQDPHwVOFy8U4HF6ZehZ0YXOvqIDE3iHRcObAXMh1oQQzNQ7e8DJQD0pziZF4VPHAkdrnZ30XsgfKKgBgViYMYqvds30SNftzAycEi_0CF9XGdpQDCf-bIJQUl8AxAvJ-9LrR8RLgsAv-zDRLaBbD22EwqC_no4svCEJtVW_llNcD5zXCSBfzwilrIAFMshPhS9jdBBFpdOC1yVJhT6_Dcjt16RSQEOjQ23M5ciIIetyErlXHvindLU1DFY6KsAQTKGjLVSA05ueZ1YY5IaQScKf5O-bfJiGnuu9b0VuZXFByWe9-8llQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در مصاحبه با ان‌بی‌سی در پاسخ به مجری که از او درباره بازگشت «پروژه آزادی» (هدایت امن کشتی‌ها از تنگه هرمز از سوی ارتش آمریکا) و از سرگیری کارزار نظامی پرسید گفت: «ما پروژه آزادی را به درخواست پاکستان متوقف کردیم.»
روبیو افزود: پاکستان به ما گفت اگر پروژه آزادی را متوقف کنید، ما فکر می‌کنیم که می‌توانیم به توافق برسیم.»
او گفت که ما پذیرفتیم و رئیس‌جمهور هم دیپلماسی را ترجیح می‌دهد.
با این حال روبیو گفت ما در حال خارج کردن ناوشکن‌ها از تنگه هرمز بودیم که دیدید رژیم ایران آنها را هدف قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75526" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWmPkwpOr06etWfn1vdbV2x3cB9aaHcz2TNiy2ej4TA4y935uzq9ra6BwSwwXnr6KH-Is6gj0w-XDqFJqaO3rKdoJUAwdxnPsbZ7Vm8FOoYzRNUum6t8u2IjI5ZXVBK8W0Nl1KmymkJrLjf0RTWgNCFkQQvzP2eMnGDLg0k9fl7Dn4nWkLwqwcuH0Vj3wLAB2B4Jv7nrAEEv1-UcwGGoTC6kvCdlmUZbIW1eSge38H-Lvy2XtJYCHTITBO4kmqVJSn3UgGDoSzhvQraIU4X9RiWzqhx8tnPExT3LfNHSH-uVykumKVL0-QPE4_woweabLJkljzg0nP1LPwsNAadrGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75524" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GoKfedYas_Wf3eMa9EAnpo9OTdv-wz4-9zhwOLOmvBYIEVV5eaOHcOR4EbTfTJCp9zhhk_XnDdW_QbhpNslGxZystYsw6gf9b6e8Lo5OQ6o-0e5KVL-ak0_krVCPNkr2clj14PDlbpHKYLInjsAf8mr7WDadro2myWNclbE6217H7ivRVPi3ayjujzfZ_giCahJINSLkT34G4J0l2rX4cZuFvXE3RDyVK16CtmTvi1zeFqh995xVUWyIxlsqkjyqaLefiz8Fqdcf4hEoI7G6Lja2szzDTH1w4LJgxidHLw4b_VY3yk6IfCoOr6NYq7q3QD8OExcG6wQAdlR6tghkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکی المالکی، سخنگوی رسمی وزارت دفاع عربستان سعودی، یکشنبه ۲۷ اردیبهشت‌ماه اعلام کرد سه پهپاد پس از ورود به حریم هوایی این کشور از سمت حریم هوایی عراق رهگیری و منهدم شدند.
سرلشکر ترکی المالکی تاکید کرد وزارت دفاع عربستان سعودی حق پاسخ‌گویی را در زمان و مکان مناسب برای خود محفوظ می‌داند و تمامی اقدامات عملیاتی لازم را برای مقابله با هرگونه تلاش جهت نقض حاکمیت، امنیت و سلامت شهروندان و ساکنان این کشور انجام خواهد داد.
وزارت دفاع عربستان سعودی افزود این کشور برای مقابله با هرگونه تلاش جهت نقض حاکمیت و امنیت خود، اقدامات عملیاتی لازم را اتخاذ خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75523" target="_blank">📅 00:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvN2A0GIJ-o_IW37GbAlbZxMvf1uI9Qh5bT5RbuKafvSBPYNyMPAYRtr32b0WtNo0Hx7czEvW9WdDYMMuIkn6RH9eAfEA2c5tayFUsoREdrLXFWeiWmJH3HNt21A9cjmJ99Z3BLoZPhe86DR0_rTKwW64J0r4zBVZ-YeP0A3rgWQPEnwStUdpc25URBOvr_frWrPxLB8rhbBV2rGG5guqIStEIwCgHaq9yQrRJxc5IJcLTqppPmdlneLRM85E9meqixcMtPRnkcvF7gy7_XQmFXaEXD_82cdtFFfVXBzbuZlJsTBBD6tRZbm4QqUQS-086Lz0VAITtCaWfsz0yFzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح روز یکشنبه ۲۷ اردیبهشت ۱۴۰۵ یک دستگاه اتوبوس در محور عسلویه به کنگان، پس از پلیس راه سیراف، واژگون شد و جان هشت نفر از کارکنان مجتمع گاز پارس جنوبی را گرفت. پانزده نفر دیگر نیز  در جریان این حادثه مجروح و به بیمارستان منتقل شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75522" target="_blank">📅 22:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RnfT3-51BHYDAOXyXefD9iWNtnZaVnUJyqYu1_L8w3-qL28RNXCPYmstUTUx5sSm_thOOIC56z_6UL_ryd3ofvIsBwEOvlU-_lMtR16iASTAZtLOgjGvemwmhUrkU587wmxV3MX-wzTocUNGLjM_6ms9XlWZ1yJMHIw0cbSYTrx2L1bZakm11hIVt33JPe8HAtvKaWQTWxg0c-Ho0niZ4f87QAgLeDXcPE-dnx493nA6lqWG6rIWrBBkq-UgdsGpg1jhDkuEKX2KDxEjVbywaK719RlGWOPbZ2nm1fCag-TrCENa07YB8ewlKfZkt6Sf3C_jy-jKzBC8XdwBzW921g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
زمان برای ایران به‌سرعت در حال سپری شدن است و بهتر است هرچه زودتر اقدام کنند وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان حیاتی است.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75521" target="_blank">📅 20:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnfe2SHqa7xZkSfwVeOXQCK-Fql9wqBprh6FikzFaPMZTp36EGaceX1xLc31XsOETX-d8iJhuW2Su3hCOVmFptcsDjAIrAqRrz1XOOAPCmQol3c_ZhVd_wwsI2_YGStpp7fEUgRyyScfcnYhvI7rmoJkc2yDoys9iCHHb3exFYDhg5jHg_jytVZuxcYhVt7_6bbusfGcTu2A5dDhogwzKzcUmWrwbB2AOs-nXSLTuMX6lNwEaDT6fQHk-2XaKqmDYo0CHIWaeQwKMuDPAUvvi91hEFDEfuy2cc55vjO7ytAvYY4fPiVvY_wtYgH0aE3Csg_pxP53Cai1oy_dtXfHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او روز یکشنبه و دقایقی پیش از برگزاری نشست امنیتی، در تماس تلفنی با دونالد ترامپ، درباره جنگ با ایران گفتگو کرده است.
به گزارش تایمز اسرائیل، این تماس در شرایطی که گزارش‌ها درباره آمادگی آمریکا و اسرائیل برای ازسرگیری جنگ با ایران منتشر شده است.
بر اساس گزارش رسانه‌های اسرائیلی، دو طرف در این تماس درباره احتمال ازسرگیری جنگ با ایران و همچنین سفر اخیر ترامپ به چین گفتگو کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75520" target="_blank">📅 20:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k3Zu9AkN9eY3uOl8Jv1oIn1vWksW3vnm6JoDz6GkABxzylCsOou7Xy5ZJdX8Tycrjdql-MprERFN84QG3DJfUILQCg7HjTzK2CprWcXNzvFmoPQc_XNIYrvwwcj6i9-j_M_TdZmEeM4TbGqnjiBxvxGmAutrqryQr1pWtNAGc1DL-LOoeisfW1zdUhFunBjeEM1UO-LhWNd3StTcmuHPHjNSq6P7lUDFpL-0JENDZRvgp8Umy5mdBdlqZ2weJXJU4DoAZhpx2jz3Egggkh0Z41j-gARkMvE2c0NhnmU-TPCiJjBTi2LHw2osRsEqfM6tYRVRjDYjAW1qjo4-V1ZvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wuj_4A2arkLLcC7zRPyePt9slZxv-4-y3MP8HUGn17I4q8rO98-kv_KGMxR9PXzOL6FAs1CfPeu5ir4Dx1PcByxpsg7y9ok9Tr-w7_Rt5qrZ3InIk3x09Oehq_R7N3xUiGu92_z49_OH7S8o5eq6Yz88HI2nXs6myzNnWybCFvsw-7RDRc3bRv9EINB5J7SSFaHy_9yRji_I8pH6TuMWiK8DQWg10MvlGQTPZInb046elPDKXhofti7vNQghW9Kq-aLm5Jh8PQ8YskQYbqGJ9WkEIhnyy5h1itYUQddRfEBnjyEb980S6Cxi-cfS0zkNge3azvkSAmGyrWVicgjVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDgPCBr1EyzKo09H5x9aP1noZcHGTC_-mRExpuhg8lo3ivW4xVoiG3ihB5zryFSMXLmSlT87gbNpdjuIjTPRUyOPxSTlRS8nkrwFPL2TrQUZuKJY5_y3qcDezdFL1bhN_BS97W1-epV0Ha8BHBUwSK5UHYdjGYbgmccajGRC1UdxOjClNIp74Yp-d78fQ3MbSY9ZvrS6jnIhAAI2mt_awW26ki3IM9aPpeTfgMlMbyLb-h8Pj317st17aXOvr-SFn3WOTeg7yRQHjOnoLJyShz61hY63hYzKjIgHiceKcno-o6OhHHuQm5xFltm2vF8RfdKjZabRqYHIgBuMwYm6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GKKIZbjbdJa2VJ263f5Ud8lk851EKMJCioH4po2etjroSVWsKT3TVMwv6IrNSsFk0RL0EDe5P8JW6aotfkgPdEQ8e-5JwhkUUmA0_Xett1A23hlQ16bDVvApbWcgEv7Jf0sdy8opg8ThBriIGNPIhkTQnUtFOtUTbBTEtEF78zjBuTCypMkXH0j_Otoro74IquHpncIRGfUWccKS9PDjbVpcFWA1q0GqinIHyYXn05fg1-J5-imD8ks7CpsccGhBpM2xD4ckztM8fLw7EnUkX2SUAJQszDbvqHgC_7qhnnN6L8uFwjRLqMCX9bnGk8OSPLpucfzyuONIaIZyQxJGlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZAE_-yH1wGIwS_dmpdACntjnLgsWRGm7cF4F9dFIDgvMaYRF9SFw3dZY2HiWCyMa4snB79dwnTj7mfLmWwErrEPuAJ5ye4nhY6pgsvMS24UOpBKiJQEzc2pkf36UxJz6GolxImIxonUVq9NVHA_2fcmCBKMOsrJ-3ee7yAiez2E7K1I9ovnwQtb8RTT5FUhUpdhgiQDioeVsNtokaCrGaLwY2rqnijYLhdGBjBUwbY3NTeSpg8ukVvTtXiHFM2Tl2hpAqTRnqYpZHf5f_hAVN7YbZsDbxM6ZaN6ikzEDt1mqSXWQTd49qRi5n2Pu04Xi4gMi_M7aouk8Yg3y1xbguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HMwnL9LlyWCYML7-kHBe2iNE4N5RkVvGa-Fn8XSB_ZJQWi-xukIW5kitMcV8aleN8ZkENoUz5E2TbMsZpgFDvi2f9mQv3yZVFvtyGee-ufYZ6ksCsiD4dyZ8TCaAfkdV_awNbUNs6wXKTmuRTcvOQJsXzo9-vLqsFZaRrAd4Ig5-gghJAE_ihwWSPJZFPZqhCnUvQN15cOb0kHLL37OUn6FwkvmIFWfh7N10BqwRYwrbR4PUTWZ3XuqG3zYa6Q3X1A4Mt3L2Fj6Gw3_IakoetR2PuaQC-oGqbG0orOTORGgSsCytmtSflBwXoYFK9FJO4WK1GO13280GXb-Zxh11vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxFLp0J4RyP8XFccFTxV9zY2l-t8lCtN1msRYbSyiPU6ClhEYVqvxt_p9mu-aD9XPGJX-tC7oCGz5PZraf8eQ9X_xpKty4HTMpK15l4CKCiyjZVL9o-oxE9yG5CvKbseoVNhy4-9_6oG9849q8OSX234UiI96my-nCRI9Phim2HKy3Ul9fOUXFLeA89QzWlHp5xlfCmcP7sOkHE9GZkxOmW8BT6tnD4_nqT7KMESwMeCJFa7hsmpZ9qXrVIdES8jC1GP_SeXZ5VAscT1LTBbO22OHIZ56Hpw0lGw8slZTbLzGM9m3KZk7inOLL8SfZ2I8tq6VF4B53cpSF9XIXvllg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BypYPjiAia3B1do8UDjW7Itd0UOLHjX6uzh0eq8_qJxhLM2iXRhFz4O_05R0lSw5wRsYBnXdGP_iKNqhlSE4ANWn5jDwED9kfFyarQNoKvIEVsYcOrXzNtjEOwAxBbjkqjZo-aHhBWhpcILBku0nsS3qjJHzneCj2Z0dsPZ-jn6jN5FsfANynUoP7BVC8yQ_5vvH-hh98Afl9wwJPGW17BAQ_I7s4X01NGQahPWu10phqGF7oudRVecx5meq-yF3obqV5niZYnUY72iHTEsHPo5_sbd4aRTIfeBgGbysbGcnx5ozg_ip1cGyH13Da5BnWGsa4dhq7_iYouYUbIq_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYzaHArYWwdY0V7VPkVSL419xMoNmFu0oJoNatZlo9Jpv8HuGj8u015Jih3EALkO0aQqVOZGzj5q0_l40DyARxT2DSebcfVG3jFUhC5GoRJPJ4dy90Kiw8RmkF17RZdPzszSwbAikT9u-dOciYI9-yx8wOf4rXgzquXJ9ilRyCwrx27on7k7YF92amVY8oiU4Gj5h38S6Q2tifoVdiCKeWyYyefsLame1kMQgqOlki21FScNdmXRMHRDnp5B863iUf4JvQMWSejW_d6_gwvkYxMJe7du-KBvdjEuvbbqbSRLAv3yJw22fRYrg_IC5Zc0CEdelvN8s2SfBQvbULgrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKpVAyihUK5pPoZUfm1QBgVGmuU4yrsxPCu8gds7isc4KvkpC7rns0OuGBZb1Apvv6mWqqGn33mtMBO2cX7cO4mciGcixcvbr51tA8D-BiY6iKbLwZeNB5vdpJoJN5kvgc1J2yuDP-pbdyEYdwWX3if8J7BL2tl53uqOIAbwq5FJBqcyagdKdUkU4gNc1AS_pBRkrRE0HGrwW1E84xRZNhYKTcxtF12kAY1c1GPtVuIRzKpiJ3xD2YgCLTmpPDqAQIOwi9zfKqYTRw3rspTBT2tAinKhXm0-sD5tx_4eT6SCc5TE0GDg_N4i1H43SZWz3nn-iQJ0l_3Aw2GPRHW4ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VvaQShUKb5MZjWETEmMeaqFmm5qskrv3xd4h8BoPIjxAsGQAUTFX37YZdc0g8l-zyxw2CvjQ_EfEwxdQ-To6GIlvWmO847j-mPSmXhOfrhejyFMHaOgtzUrNKEyAb5m5opfh5o61KYCRirVdUdDfBEEWuyrw41ioiN8cF8NODUc7_BxexR6kjxvCwWza2eXN8TvIGrCB5Rb6_wBLe6zIpkegPoC1wLw-Z5-K1pyXBU5r10F-9DXeLKHydCnrpiqjhK9lacUxi9zrSZVT42oz175jFUu9pFbE-dHjWqMexnozFr2NhYyUTMyVB94Yv4B6i1BnVLnuypzD4dOGF4HKzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v1RTI0Z45SX_Mh4mth6ZO07dG53yWCloFRTz1ouQy7lcQw9EjFV4yMvSZPnBE7HiS8j6ewHc1QI2AYMmwqJ_hbc2fP-XZpma1hLs_VH32Lx_bCTvcxJrBXPDsVOC_-pavLgiH-wVemnT6TINKFir-TaLpH2VIb1xs2vl8vlWw33KaXB5zcmJIEc28dtAXANzQ83MqmC2XfpWkHdxctUv_jH05vjDs2MmlEuM_l-ULAwEWf0fbC-KW_IYQ76H35VCMqU_Xt2vSnMX3h0R_oIuHVDuw8r_zylIJ8Cvq_GdW7HBu_SUjDjXBFI3uGla01Vw-6F4xgparR7veFwkNC0Jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=V6x_tCbr5to05BYNa1nDI6sgRnB2Eid5QiBWQFuar8HSSig9bOPjseAY5XRKB5UYDpjvuAenIpOBPYPGOJSY7btvR8I-QVOXug47TODFh3Wf_oFkhuWiOZAFYM6YSj5PF2wXK71dwRrnqCpx5ZeWlHxB1fMhceEjKIqkp8ymENojTDk8QkDpUQBCGq1MZvRZzC8NWZ5b4vL2i5eoDCWSoJ4GugT4pqlZURLijUoxW0PEMYB7avFNUuyhyRBoiccUgrpsI-ryZ3DyGKz-DCPXJol9ce4B9N0Zn3xZaGHdNuVN-kXqy8MoRFDb38_lU8-L7jp_dkpVH6P2ebPLLUNPVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=V6x_tCbr5to05BYNa1nDI6sgRnB2Eid5QiBWQFuar8HSSig9bOPjseAY5XRKB5UYDpjvuAenIpOBPYPGOJSY7btvR8I-QVOXug47TODFh3Wf_oFkhuWiOZAFYM6YSj5PF2wXK71dwRrnqCpx5ZeWlHxB1fMhceEjKIqkp8ymENojTDk8QkDpUQBCGq1MZvRZzC8NWZ5b4vL2i5eoDCWSoJ4GugT4pqlZURLijUoxW0PEMYB7avFNUuyhyRBoiccUgrpsI-ryZ3DyGKz-DCPXJol9ce4B9N0Zn3xZaGHdNuVN-kXqy8MoRFDb38_lU8-L7jp_dkpVH6P2ebPLLUNPVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7nagdxCRbqms9JUvi1_t1Fv-YKi2L694oI4Hz-nV5IVYxhwXDdnRoVG66rUwqRVPgoPJjxHNEaLYjQ1aNPW2al_gCvWMp7cdg9k7ks4eBLC6QvPqB733X-S0pshjRV--2QMMwifRhv1zeRxSbOmTw8WiCDkRTEhAQLvD5aMNCnSYTELBHvlcXjh9gD3JDjh1HR6Ju7nfWZKx_t0nAIUBmbCbe4peeylDhB3IRetf_1briXjceuOy5ewLQA5UGAu55pK34gfdymStn_Zppsht4hTE0Rv2p1KbAb963Nb_Tvah6QgfJ9byN6gc6nzCxO7jloz_kW9T55235jow46ggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJf670i0jG_I3EN-7M6VTQtSxWxIvedfaL9AWnrSpw3yxPzC93AliWIUgST0k7vBrXvuvN5oup9eT1mm4XRjUWwdWVYLu7ABOqRyILRaSuGhbp4IOPnpsc76xALP618n5MdsssibhK0TlGuNdjC44_kWNdRrhC9chNqWPRGUvhMVdj0Q_eKoCk5XXo2OJMCJHM255C7gvEDNu0XxsfY02wFX_6fGBZnTQN6qnVXGke5avsJxSCOjok-4XUcarHo0JJTuWdOTfLUWd1hP9yCjWfBfHCODrfLF9vaMP-EgAuOqrhZCOQdwRzj_THg8_0RU3bSAfke6qn01neXBm9OlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mCYR_ny9MaqNuqWx1eouBTYDd7GOKHQIK-Pz-DQWojljdJ3triaLp-t8lgFdzR1opnjqCZOPun92ClCCkvgGfkeIYtlJyH-p89VCesvRBZj0aKIvNaHY-mYj99oOr8ZClIX7vpAjZB40ezK0Ojy1vJs05W3_rcsBGJcCkzfyHVWwUDGnRpxOvIHU857agpK4NvJECtawLlZanocnsEcvhuvxs-Gw01RPKPpnbKEgRpb0ndv3AOdNEcsQxNsPCpXTuGLJSWoAH00gdgwCcTsY8uH6ezA2jlANvuc6PSgtopoIdR5D8SLBvjI1ejMf08J8RxS8dIGEY5jsGuYr6KNFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y2HW83CKGxnDz5Zy4dBiNQhk389rhTpSldoAE-4EZpnF2QnUTKulloIwmSPwvzOke8Z0E_8VndTXbBGldtIMYDu33pZvhxFXwRG78jfJbETkF6xWRY0_A03eWdp8FXl6GH_Ita5loYT_v0pyVjRikK8PZPLdEakdcxVwmTzav_6h3RWgeAFiuAQv3H18APserlD8psE1T3odaA4xGE6f_5iTAxOyAiXFqkBw_PzMFNy34vBL4AiOAxe1mTuaLll13-LVQcsE7LdbdCSabtsBGlSsvFh-WHlGWgvchbc05APmFL8cAgpkSrvmvuZna7jFVPQiRPXOOfhhDBwNFhVsnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=rghO_kb8m0vEBe5ieuCxXLOrqEP0b35Eah5GhrMPTLnlsNM_UlrpjQ_namxgn7K4bMxKt3te-Yd3i2gO2CeHnqwRZjQ1iJXcf9S0aXlYUDFPA7t3DpfzUmN1Tj4nJcG-TxWXB2ucCC76j4GHXQg4GC7-6yDkDkW17k6bG1AVLpDhncCs5ofUIaUugrMUWVwrrob87uJfdM6Q-u53c4s0ZmBTQRbYv-ArBYRYqEd8LkSYO8JfhIRWSzMt5YgW_5ZhV4fHG9lBB7T4URsu6cbGamjfDtX47Kv7Qm4z84c4zz2KHRc8IgMpYWo7S6lzQvAc6mlD9NWZKx8Pyp4qGluEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=rghO_kb8m0vEBe5ieuCxXLOrqEP0b35Eah5GhrMPTLnlsNM_UlrpjQ_namxgn7K4bMxKt3te-Yd3i2gO2CeHnqwRZjQ1iJXcf9S0aXlYUDFPA7t3DpfzUmN1Tj4nJcG-TxWXB2ucCC76j4GHXQg4GC7-6yDkDkW17k6bG1AVLpDhncCs5ofUIaUugrMUWVwrrob87uJfdM6Q-u53c4s0ZmBTQRbYv-ArBYRYqEd8LkSYO8JfhIRWSzMt5YgW_5ZhV4fHG9lBB7T4URsu6cbGamjfDtX47Kv7Qm4z84c4zz2KHRc8IgMpYWo7S6lzQvAc6mlD9NWZKx8Pyp4qGluEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=skUuYmgpM45nat5j_RXJA6vYhIH0To6h5nAUzCRVYyM9LlYnPsXppF6TapXClCJM8IexEUO-vQrK7X9ghaVBtrODfP0JKVTr1ajaGnTlg1PD9DNQn4YwWHEsHJiKZR2pCZYkokw6V6YLirM1_CfqEQTzd7al_R6AkTVW9vYC4EdWQoKTJCKSSfrXng5--pPRRsfj5EPdDBBUl7TOPRdJcMPky0d1VK5MIchUqqqr8n266XkFfnr2FniYDGBWCw3cfjBPNd-sagP3tC07VqEv6e7-w4geIqdNUW8-UBEbvlk88v90RHa3sUT7J-U_dLoaCiM4_FMyKDjH0YHxtpU9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=skUuYmgpM45nat5j_RXJA6vYhIH0To6h5nAUzCRVYyM9LlYnPsXppF6TapXClCJM8IexEUO-vQrK7X9ghaVBtrODfP0JKVTr1ajaGnTlg1PD9DNQn4YwWHEsHJiKZR2pCZYkokw6V6YLirM1_CfqEQTzd7al_R6AkTVW9vYC4EdWQoKTJCKSSfrXng5--pPRRsfj5EPdDBBUl7TOPRdJcMPky0d1VK5MIchUqqqr8n266XkFfnr2FniYDGBWCw3cfjBPNd-sagP3tC07VqEv6e7-w4geIqdNUW8-UBEbvlk88v90RHa3sUT7J-U_dLoaCiM4_FMyKDjH0YHxtpU9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=uRqoY6zHPFwW9aqbMhKQhvc3vZQvjla7Hhtg371NbeUgFFqrFDKRNq-txwmleG2vmR25upvEsrrDwPMKbQ0V_T_-70xl9bncPqiFvBh6SHnZVu3pb19x3PAuC1jnIFHWzLxv8ch0rj2WnBK7t4ZbhQ92a5YlCyvmlN_dvoM1nmkqhHYtx5txI9PUjhdiHDlI3884JALk-22nta07tdcaK1ThPhk3b4s43bdFriaHK7LsPTfnc-bIEt10GDi14DbxhZ-XtDzzi_l_-qBIALKr83knxGwWnApltULTvAD12gSgLZ1zU93SHU8plGuOZzGKi4GzK1tA0m7RWK1n6EtwIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=uRqoY6zHPFwW9aqbMhKQhvc3vZQvjla7Hhtg371NbeUgFFqrFDKRNq-txwmleG2vmR25upvEsrrDwPMKbQ0V_T_-70xl9bncPqiFvBh6SHnZVu3pb19x3PAuC1jnIFHWzLxv8ch0rj2WnBK7t4ZbhQ92a5YlCyvmlN_dvoM1nmkqhHYtx5txI9PUjhdiHDlI3884JALk-22nta07tdcaK1ThPhk3b4s43bdFriaHK7LsPTfnc-bIEt10GDi14DbxhZ-XtDzzi_l_-qBIALKr83knxGwWnApltULTvAD12gSgLZ1zU93SHU8plGuOZzGKi4GzK1tA0m7RWK1n6EtwIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H98c7W1JVkeFXh3z3u8L29WUtf-V66ySjjuKlUq-z2CBUfuYaFfAcmibBeb9L6rhftjjNINL9pZ9h-ih8qfhHr0HvGvtBHEx1ImpexU5thXTVAdwYrJ90RJDTBve7vm64JkAypYplRP_mhY5oLU6nCaI3eMXKryH9mNi8x-t9jvFHA-NVCtWfURgj6TSpex6Xx1JcKdLK3ul4TcZd3ui8Q_SgEspyovpzsd3FKALwvk4kUmyRF_mdOu_3diznVoMq3nLzyh7JID0cMc_Pe8icFCY4LA7CE4cnJegdvcc5Y53IiDKEueNXGNuJG1UBjrFhwAdiGQy4_lK8rJjVomjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T8NcL5woH_mLcXcswmqVAUQLkBGOsJtQn68EMhVymocSChIZCQxnfm3xeYYBsdj11L97-otJISGTuryqszI_ZWEWultXmK1Npv98RQLN7688e35rW3AVT8QrNtcJBqfMuVWeWF0ZC1GQJMMebRwLt5wSmEZ7oeRdK7jQ5Wdl5_Uo-hRep7ZqvPUvfdhBPNtAqfxD0HD1fSAv_Hb8S76rAlL0ylO3wRS6BzeeRnNp4EWFwcb9dk37PkPSlINGbGrAj7skU6moWzdmdkwT8yY4YIJdrkxNz1-U0xJqKDtaR3u0HQSWixp8xwbX_FFyc-pCNlJWjLn7Ud3-Ph-UI_7qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qadyXGN06K9_Qm2D5BHKJ31DMF-0EE9FrpN1EospOxUepbh4D_kqq72tVJ9_NQHz6R5W5afXL0PSDWpSaV1HOYcMEdqa_8HsXVYxxA1WPgHx4wLEUZwKTsjZH1egRVLNQHF3AvTFGULV6TpwU_YVaeazRdFDCliOl7FwxtOmfmpSko_Uh3oTEQEfqI7uc-fQh6sfB9icMvHqdxoumsxInIRBIEE9GiWgH3Cb5qkfvdglQ2oYorqsVZmwzjS9JDICp46RC3IjH734tuX4z-maDu955AklQ9Wo0RbkHPFZoW_x-3MyHXZGOFukrQzXHaV2btqOq90hS4_r8phzd8GUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mahIcSTqCLpJhnd2yr3SXtXk2qnU4RpzprAa1J70IrXkMY-OEgRDYhpB08AW5y18WB4S0bjcRjJG3Hr6y13YL4_3I0LlmwBDrOthnTuQB88SqgODwQi1EaX2kuGmBQbcU-dMOMmWsWwXyZnKFDhsertkXEAgqzIjskXXgssUBr6NmCsCpCZvIbukHV1eiqhCSXCnLlt32Z1YOkMuUWIhwJni4kCpKw4c5ilJYFvQxNmyMZe2pAIn9YMmbO1tPTgY_pSLB6KfIm6CXwfe3ZEvtGSEiwEnwXtIJ4JcvLGmWmHKCTb9kuojoSAqe1ZhzDaCEq1s3HObAr0LRsh5SNNL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VLXO3fdd0DiVKjWiuoibEqAgo2guajRODIZCKOkB-TvCVDzTnlFl3Hv_EvA4HwvcmcbkUfx2L9NlmH5I6FPMNuaOKzNjoA-_2NRRGzraeztb_I8L3yzMQqysB30YxxNLM7Flt-1d6mmPwqtFWFcNSgzSuXZJpuyOgCqnndglfZpbCGr8XKcXCZcdgRnCZ6V3V2G9YVeAT_4huOGqlMAIOqQ1y-aa-TSKvMw3g5vhIoHo2YIsMrlEPMlAmET3Dr1z44wRYnE7hH2ZxdBT3S9xVJDReawSSCzpPaOvfYQolaVmscf7a6dcsVcMpzxipENuayWBfswML-mq5vs21At1TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3kKaavajZeuvrP2jgJgGlFeR95xIyA2Rr_MOxbTElXt0sSQiJU98PR0A_idphSXj-xdI9WHl5XG8GKX6qTsuI1o7KAZbrN2f0XdECqQHTZ3KbQBjX6h0lq0e4xviapIsAfum9emSHBKeZw7CQmccUccqx9r5mG09j7rnjCr2_DofS4HX0E8r8JohbRIHnuZn-LE6divJoH7MRalmypHIj8ugdYu12mGWOZMwrzaNgiiNr4fn6LCp4EExZshDFae1T6PcFWAUeX3z1SVhNLXItozh2ONYEi5zVYyTt9e3QICKa_cXzkUl3N-Qax2DXDS-1Wg8vF-RLHwtoTCoOXvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijs39vP2343Ymj5oKC6FYGY96MTsTqYRc9NL3NVdHXjRdQUjyAApDtgy3E_JmLSRO9hUBITTXA9QDm_vyCUvjSco7mL5aUgQgblq_gNinCfFnEJCNmhkLKlB1uulYiZO1fO2Ms5T7Q1v7u0UqcsBsaXXoOSFbJYt3HpWxGBxmk3gNHAGLuKsj0ci_VYHNnJg4m9485nT2U8YwMcCaIbpsrZ65KeCLP-6-K8aYmiaTxWyLTvpIlOyXgqAL4Vd61oqk8l4RAWjFB5EwngtKDCXm0sINQp3MYX2nfpQpBC0Ni9-jGMyfY7TqWz1gAd0bvKIJFzJPLfeCOL7fkLQTL7o5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YlaXdZJartPHFBwdmPGI_IN2vBDWWM-2oN7-Eivviqxv07N_UP9qTO_2hk9f2bGjbTIYKSJLI_tniSjwVeI2bYXjsygNMBCa2SB8LgARKz5y8A4ZMRDYvW0HUrcvtvIHJFzUikFA8UQd8o87HEhQCcPf9Ue0KuWW0c-RkgtruO1FDNuhgw4yxEe_Hkf8Trx7di7ZMjo-z1DOuOvMQZ9WsXXjiE_okjRpSwa2m5mh2T1PyTmJ8RsScZTLcrB1W9axezC2dxhSc8_YE0cCDa09TMYtwoAHbCktIGHm-JO2PuVBa3M0di7pKieDE0aYS75xPNtIwgxscomgzKSYvekr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HNxLFEMkfoXNwLvSS-SKzqENHNEnXKtwRvaznH764JFxrYEsKhlcXLQQE1xS62MLoPUHYUM0ZPUgcbIg1lgfqEmhrE5Zf5z20Ky1_MDFq3WcnOo8wmSsKNx8IvnqLoxp6wwcwr_3_RfN3rsm5hB738pi1-YoPC2HKCPYCEAAv2HspgXVxBpnyY6kwINyX0jKTLkkBXG29tceKqkH9m_S_hH_GlRCbw12o4FlbOp0EjcyKZkmmWKkKcejsMTizrkTzHieykqGcaF8f-IB9PfuQ6oNBP25zGMlBGAJqfyM8rlFGMzHKLB-Ej6W29H-6TwR6kdjm93v7rHJ5hHCtQEviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=cSw4s9Pooy3VIN9xKkQEWc8ccYqGNZ0UvAFDQ_VhFJ0AhQK_Y8nqCoPY5sSQZQbxre8cikADJ8WD-EgzOrdYzzCoARnwQOJ3VVCEyvztQeNBZgnCJ2EwLpSwJ13b0QGXW13aIjRHc8pw1mGnHPnEiBEHf_BGZ8Vu13kD6KD36dRnqVdsCBKFQ1I1cCHOOLdkcZ9vyXHf3sC5YXKWlPPlvd27Wzf0rdA5hwwpXES2wOwiNLuIBZqFFYW6GcZhXmneayCQDh6FzmUXu1dnL2aDSYbUFKwW21rMunzKWiHBJp6lNgNGXrwL44w1fKWiLZYG-gVQUgY3NgzD-62rJnzrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=cSw4s9Pooy3VIN9xKkQEWc8ccYqGNZ0UvAFDQ_VhFJ0AhQK_Y8nqCoPY5sSQZQbxre8cikADJ8WD-EgzOrdYzzCoARnwQOJ3VVCEyvztQeNBZgnCJ2EwLpSwJ13b0QGXW13aIjRHc8pw1mGnHPnEiBEHf_BGZ8Vu13kD6KD36dRnqVdsCBKFQ1I1cCHOOLdkcZ9vyXHf3sC5YXKWlPPlvd27Wzf0rdA5hwwpXES2wOwiNLuIBZqFFYW6GcZhXmneayCQDh6FzmUXu1dnL2aDSYbUFKwW21rMunzKWiHBJp6lNgNGXrwL44w1fKWiLZYG-gVQUgY3NgzD-62rJnzrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIgM4IIie3Ip6Jp8MtTW1Ue1jGXB2JCALHhHiyNRLk--yhunmnwnW6ZFlES27tLEJ6vCe6D75l4WQg1mqsKWHRRDYBBiKGu_irlcRQmRqknJOVgX49gYvQXJ1RjrNyIx5iRk7ckBEIY3ofAAPuRnpEnLzkTqKNbVKNb8ZwSW4dIvgvTaTn3WcE33qYY89cOxex9BEGiCKHvHbqzmcuye5QG-5j2DoWEUROlW6Ivz1n6FnWpfo99pidWgRQy_lVIxPGSj1v1nzVhz13O4YnNeF9GjA29aaCJ-kDUeIFbegj5UHlhrjAtzPFttEFOALYKmh-KKY3a3P_48FvYnb4nVcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=pNujd2PC1zdMEN4jj91B_rbkkzoMOQL_pjh_jTffe3VYcHHF105_8H-4ivH5BSHGwL4JypXFmijb7YTMM16mAM62eeIV6R8jXFLbCWL8KNK8lt9hiJB28EJiiWf8M_hIc4Ajn2EKqezKRRGzTx_1SnLHG6aOurIN_yD7_P0xOPYeRQJWBcwzkIHmtGTL0aGe1MgzfbLDlkrrIZz-qj8gKqbpPpb6Cc8vNCTJaIJ_G26KeXhJHD4zZ3zEU2HUv_JwcZ-40HsCucHNOzNY0qN4d_xTU0AlgaZDyqauigqRLcOVRtd3rbWUZjokyD4IG50hOwmaMMpKcJW98zQ8y7QMuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=pNujd2PC1zdMEN4jj91B_rbkkzoMOQL_pjh_jTffe3VYcHHF105_8H-4ivH5BSHGwL4JypXFmijb7YTMM16mAM62eeIV6R8jXFLbCWL8KNK8lt9hiJB28EJiiWf8M_hIc4Ajn2EKqezKRRGzTx_1SnLHG6aOurIN_yD7_P0xOPYeRQJWBcwzkIHmtGTL0aGe1MgzfbLDlkrrIZz-qj8gKqbpPpb6Cc8vNCTJaIJ_G26KeXhJHD4zZ3zEU2HUv_JwcZ-40HsCucHNOzNY0qN4d_xTU0AlgaZDyqauigqRLcOVRtd3rbWUZjokyD4IG50hOwmaMMpKcJW98zQ8y7QMuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUTE-aYJ3E4ZJAZpphO-438exUTX1CBguhFMDOYTVjYZhqjf2g6Ir2tt6UU5ArkOT1UsFFpJ_ODE9IE2kqaLKLpu9KFanXQUzCQDAyqXn28Jctni7EI9eIEYRqDoNtBVdiOtom2pVqSDBXOa1HIW6DLIbGdfVVKgSwUeRg8_xcVVFw5awterXxoB_-5QsOQQOyoGHN6tZm4Mh0pHOL_m3GdUCs77kJpT9t8NSSajPgg2OcfKHEBy4xhVZ1GfJmqiSyoWgPiRW6P5Be9BbJbC6Cm-6rPlQPdIBU1z7I4v4O8dM5sIMoNbBh1UKRusxpkGpFJ3kXqvrlk9dMDmIIC5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QifGwDGPemyFLE3u1cwQoPSJgNjSRuxQzh68JmrO6jEVmI6b5IhNQmOuFyVQ-HKVTJJY-S-bufipLpS9QKzs2u6Opgq8z2Qc8ZT4K7qzhVpbM-CUSIrt4kLfl3KKl-1mEEhi2K1TlFro3alf5BQsZk1A8x0dzqfOALioH_x43Lf7QFjwvpe-aEJUNZeg0fnNGiTSyUXdW5OA0KaT1-V-Nennb9W3Xauj2T1TcqJ-r4GL69z0cjslf6Kci4Y95l5BXGocGFHyZ2vtgKKk7inGQKaHDerc1ZyG7g0H8cB_T40VhP0rXEIGI8iq3PKnrn4EDVB1hcCTOg6WNKZPEiCqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UxZcMxKFLuwPn_hqShOrM-yJvekuHfz2lspGcXpLE7MgdLnkkjmCBKCjdfz85V2_TwfS7j3V6I9E4aeKpYzlNJRQcEQoWS7fr0m3DSW-dTgP_7UR9xsruZocO_qoKccYCuPYV0ArS5gCWtxxX0-Uzdv8xWSeZ29CBZEoslJ1CaSfkSukKSClVNuDdgjppUQtWFIC0hbh-dfxex_ngh8jVgZGtChgMzpUrH8TEfEVhpSv0vyybtQQPkCrpSCEtonQ-wIEh_7wI2BZnZd-UoQExh7uBHza83ygP96rBj-z7kQACpCLevS0x1wJvZznHUkh7eV8Wk3Kr8PxV4rwNM0t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a7eQu_TQ5VoHl6kTUtKU_v5SQxWD56cZTLSLuQEHqI2EKvINgRV0pMHfyN2j6AQyjTWglIFSgFrNrWQPRTZPhn5p9VH890hN2IRUv8C6g8BWNMowvNKSaTIil25C0Bh_u9S6DVTr9Z-Dth7PdwZJsXwWn-jvxXYCs2Heac_gqnjPTBBHE-RJk4rROYYu3-t6hAocTz6_qlAgLt6Ny_7G47acpP_pIKr4PAYFwK1k75Wr2eJQfLNQq5T2Pcb1-0JPB5Tjx_JbaBoZdKoIPDrQ33VSGV87AItXCc9hj5z8Phn-cLyi8BDM1jCn0Lvw6PcCaSOzWPWhlMc33N9caMNN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/swUNEmxsIjAiSeDyJS8SRLqhDzhhnkqNyXSgzoISwgfhCLm6IxkCF8vofkF_gSYdc65QSOu3XTSC9a27KFHyZGurTzFMHUe3K1XrdOpqHV1ei3eEEXM92qTrn9i8rOkcaNzf-_K2yHsj2DAlQLkBZZvCruOB2lW9F4zwh6HbsNfqzclT9iaix_Nb6OwB5S5PM4RESEfSRkWAseXBjQwqjy02ubDGMqu9om7Gs4xNSaMB8LBSQsV8TcHfnyb8E2gL37htht1dwxOIpNicrW6ZVGmaGaEIA7FXmXWg1-xGTjllvT0cA-8qJaLAvPeY2Vhte2KVZdkRhlHIVW8Quxy-Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=W2s8p_hPOuVi5X5CUmsdybZ39Cr8zhMcfsofA6KWSqKLh5JrUR54njrwJ3X3WUo5Khx_N10Z8jzdMIDB0pYFxu0GSY6eBftDIXEuYk0ENXewqw_c7NxtVrM8Jo61JTKNIJe9IqmEZx0GVZ7fSgwYg3rjaVCwHbEWI2GRWGIyKCAOUyMQHFVT5etKGZDB4Ar_xgwbnYTzT0qXFGbOGSeiF6PxmY8I_hkvsWXQtb8DB42HNFtdp3NX_z7MljbE4Vcl5p2ghY9khtvjctc9RFU7hR8g4H88sDxedYXxYjlyffZJX40CSYSwUhMOOmLtttWt0ueyEZbL7kaIzSjFmhYUeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=W2s8p_hPOuVi5X5CUmsdybZ39Cr8zhMcfsofA6KWSqKLh5JrUR54njrwJ3X3WUo5Khx_N10Z8jzdMIDB0pYFxu0GSY6eBftDIXEuYk0ENXewqw_c7NxtVrM8Jo61JTKNIJe9IqmEZx0GVZ7fSgwYg3rjaVCwHbEWI2GRWGIyKCAOUyMQHFVT5etKGZDB4Ar_xgwbnYTzT0qXFGbOGSeiF6PxmY8I_hkvsWXQtb8DB42HNFtdp3NX_z7MljbE4Vcl5p2ghY9khtvjctc9RFU7hR8g4H88sDxedYXxYjlyffZJX40CSYSwUhMOOmLtttWt0ueyEZbL7kaIzSjFmhYUeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHGpd0xword28J41WQ3DPwxgfMDkZ0DD_x37E1TththPY586iKB2usmzkD9gnSjsTwS2nJFfRSgHoby73drFlvO2pdXaxY0-9gS4O0UyfQciHe7KzkNFY_oqcNHeVcDRdGNrorkUeGDNbqqOeczCVY41S0LGhsQBNntCZC4HfV9Er44wkk3VcK4SWcCz93Hdt9njPIm6EB8VliueRitfyAPf0MUBk4ha4132R-7AYAPiz2f0RrDPmSUgNegF-u1EX4WgIc6MHiF10XgWZmY-gP4Kx3u-Kj0SeisE1LqC2OmwzeMloXaaoZyV-6JPgqjOYkCY03w9XXFsA9eaS1DKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orc09UopqqJKc2BBhb4SG2SJOJdrGremPskYAKtCd0GlMK4K0aXswt0XFd-YEFDiVVh1wfhKFBbiteF0qYwnPFtd1sXtr4NbOP5VbLisE7-kU9U0LpPQE8iWmztMS5ThqrkC98-5nsNDqFksrsKY9jvKvEwa7CF5Csi2G8BZ0zfE5CGUTPWPdHK1KU1OeH00tJmm7towd1Ayb2gpIghJdZds50oF3bSXhPMARX5VBmQPpk9fxLdCSteuI8C9SFJc2RePfzGyLnl93y3h5M8Hu21X-EggIHDZUCw1A6dGOv7WkDA7DXlZIavDsj04tkZy0aoQ9iVAsSkKxPUIpNKDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OxrZodD36cCuxdGYVC656Fa_zHw3WMdmNLCb7PXpYmSV7Szld1fC_cIZiV2rSKFFgfG99EFOn5RZBJSCt6f4EjLI5zdaOLh1bQIamfE59q6FB__HeO_ySDfJdcdVUWJWUGo4WfMlOfLJ0zLPOaAoYOCOlayzqDs259EpU4qaAiDPiCOytiyaLtGtp0-Tt_rO6MGFhic3T5-q9oy8pPqy7zcPI7j2d518F8kmwgbi1O7suLykN0HVJd-Amaeybol4cnAJEgpPZX9zBtU1yUVztf1gVzQ1-z__xYnTqI1BWstOR8UOIfODbjgeaUeORT-os1IKfLl0o--PLawXeAzmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jISeXq9p0mnW3SKP7hnCYS3cuFsbN-TZ5bgvg6njXAlow8J4eFhZkLb58xu1rRYxnw4GqBvpPF0vomXkAxDFvY6tTFl2p6lgAmc9q9Q8aC9JqOvE7988OKbx1wOL6KPorGDfP-9OusyS3_z8NwvhdQ_stXvTAXzomo_KrDmC4IT2DbibiG7DSfybhS9ogvUtV0np8GIFIVvg3wq0RBgHN617JaNJy_SknPd3TqoBLSHkIuy7Vkbb-FTt7WbkUc797q7Xpepbs0ZSZnWI2Corr-K2HWNnUoAsUDFjPk8UxdBv5U7FpChEzhuZzlSIp8JscBqRvXXTJmLXkvYhJRN3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TJUGuYCqWdUAY2DEUP0MYQMAvMeYr3K_nwrZ62hGqWpmUSskl2sUXPojmx291pL7oXP2ydsIVUhGgVcR9UJ4a1-hKxGR4GIfnSuImqWAP0lh2Q3UQC7xN2pHVwGHeql1CjkxGO5PYF482sH2e14uHdRqtc9gdByXFavLRTNc9Tz1si1xxKC3BtAlahfvP63aFtbrws8Qt2FDxt1S9uFynziVdSONqus5G11cjEzndqVMrGcMFv-ULvqnyv11gTHr7hccg6Q9ZEWj2opQvgGVoW_TgZUGhQjz1arDsVdSoyEr0uzc6vt4f-jqBQbcXa_IOm0X2BFf7IU19NQr9lyhFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihLr9RnSro0EefR79Y3vFUlFGK1mt-qNakIW5Or0SH74QIts0MKTIi4DZMGuOkEnQQSvaQZOlJIf123u256krlMSma2a712HOnOgAVFmtxj48moKU0klHlSUP3k9RNR_5rn3N4xQEDK71yOEi7H_jyYI9xauYBOUtcBut5EI3wiUSEbFkAF7PCEMsrUD5SCyqovSoIzkvhvHs0KgM-dyHaY5wrlJwPHswXD8pCFpQtpFyhraEA9noCuxEweeXuUjngndsEx4i_rZZVjO9iqO07GGvNRJj9VdZz14IVo4_6xya2SUsIgpZU8Iot5LoWBktZLdif3Rqg6Yj9n953BCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VGM2a7x9FlDvbwvqYYUrPZABmVQ0uWhQ2fXeyk1eJ4Wwa_sE3a1siqmDMwY3ot2P1SSUOkCZbkt5WYOA8tBU3JumSQAKw-_uCFZYJxTurGGDDU5FfyeZGmYTA7YSn0V-N-VpfFJNiNd0Dgc_BgybJ1aWmLWaQYPQHqWTuTWtGZZTRqCeJZMBzYppG5crDIWR7GWV3Sb9G5g5a4CG_ov7AiP2XzzUIjBpFCqV-OdpamoP5flGp-HnOJefK7soO_h-GuJctDd5AmcHHbG-N9ANskk2WBBWh1RPFb91vz2y5EiB-oc0v8YsG-qR7slMr-pV0I6IpOZTG9A2ZMYou6_Gbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_CnDwbfxAFgzj9SNDayaeQztzgozGUANmCPZz1r7nSdUORKeGDwAuS7PVALzSjFuNnnnu4YEp2ibscBVXEV9_2aYcGT_MVm6gkfrcmOWBMbs5-zYn18szXqSiNti4ipnaryzBl6ucWRYyLH8WXs9WgnifdkvU82EC_OiaQdLnCGb8iYU6t9Zf1-odJwmPYkfZZ-X8WIqsWvPyN__xy1n-NbbeYlxKDFsz-ThY8s5_U9BjU4pZ6oaiZsXUkah1yA2V0ixF7bg7edgYGsRXaDHs2v3wSaz7V5e-ZNdxeoalBjDgr29qEdYRjypUi6uRoL6hay3M1PsH3M2lYLfYkQVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T905qsW7FQlX2dqHV17OFvSijY1lEcUP9BAFCyA1RKBTC8Us5JlfErW7rBxYzKsGHjyE8XqB66bAG_ld-Q_fJPz8WxKQYQqJGRrRvIpcuC0SBRgdiCoCw6JBM7ZzjBuZkDLPIbL3ERPQFwmm8XJ4li9aqWeD_NseWcTN8HlJruwhpz7mATFG_OC4yFDHeGPI4zastv8O88PpE5uveXnrqwkxTz6-ARvM4awzPE5Sbu16cCQxQA8uhfy7nwYGPEKZEcRt_JrRGfSa-T5wRwe9A3HmAUqca3_obvk5UQWdo3n4wfuGoiPrEFO28yZza90HsoRL_9gudfbgBi8q4hhK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2WoZ9c7C9j5WXoG8twuXdv1LZkW2OauApXSFrUXIJ_H36Vmul2kpsf5WiIKxdmjqcRF1UjYZOFxAxxY2p7-o7anRBKePreMMFJbJwWjV7atvzDQcytRnUlaY_UvQcEET2AqpNXzJb7tkAOIqsT2cRMQOCxM_qUttjuGiRVb-HGhDjRelks0TjWLsBlNeCCSQMH2W_VYdXGoFhJsVXxSTwvwlmricOBAhl5f3mLA8ml3Geu2lbOK0EzetL0R8KP9z_V-m2_yYLZGYXi8JcbqQeOQ3xmJrRC2qxvexqTdPRc1BUSkjlGJ9O_R6qB9XMHtOxImqGXNKKg1G74wtihqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDFypWa7pOn6_epcc5xwroQWTKBhXjJBpbgWrjCnZB6I-lJpOq4IWI39GBWVIQ-3xmjwSs6FMTnawTfIcEB8ZWm1QxenpNWrghfzRtIjqoRbrwqtmV8K4wdra37j-ilrmKlLI1PMK5nS-YKUPOxZZ_U9xQ9EpIfANTt-CFjM6aWAYQaBmPHWKQuywP9tJRlPGnNmm_AfW1CyvdxIfbZAx3eCY68Qo8CC-gGAsUoi_GX3TxsiFfjdZoGNZw28grmaYqNDdNpK1eYroZC6ZoWx3JG89ZlPtg3vP6pcn9QOSQonN3G_92dC-KasAK_sNsJ-hP3CYRLSab-_UD7uxtIXZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0JPb7UKNGBarbQPUSvbUGAB3ximJ1eAzbrqYWZfp0dbAKOpUNUaQZ5KkcrEXlmMujXdurv2vsYgqsazkSiHtv7KReFm8tND9QouqIvgKFN36VKy8IDnyi6G-GP6RD5jCtrIvKZjZd29bEUUs4-qM5VsAKuGOqM2AkO16MNaT-37hx3tb_96BHdbkNWGcRgL5qYJRsmUS6z3brDWazJMHfix3G6mFLr0_ki147J83RIZaUIxzpiB92uoMkw1rs-sMHspDWa2xMuNV7A72W46WTHWCJ9E33v0yU9LSNKjyET-vh87Vk9IQ6k7_BR-9rCAMq4hIKSTjG7frrHJ_YqLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5SA_u1BmYKA74Xdr3RzU8M9-GHZyIHGsuQuEcKDD5_6H6NPnKK0gkXZNDJtrWXEnBVRWV3GwETJm04GGs_ZAjYoLyxJ4BYvRg1293uqATgufNZnmpToZbLtf8mXidixJPZfd_Z67aC6qO124yppvUPP7nwk-scQD1PKj6GaXYNgAxwR_pzey7hP3gYH0uXN351lQuL9ofX0TQ2YBu7_idRArwQhZV2ecSttWfyxtoovHHbUhbGWeM-R9Sv91mQXi2qUC4Ctj5h6P9l6MieB71VNTGuBZsxPKKG_j2qSauRHnxARftho2XeaGBNAcCI-YKYujyAC_nuR6ZNQ1PLzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTxdJEFQQW3lDiGBCbzpQ0Sc2FOxKxcV3AdCfZEwbHEPoRGXhDtD5nqEyeEOwclbweUXOAlEcs_Hml2dXCmEnTjefOVon6-dteiB5VFQUPQZb_KALqp_scYCneY918VC9-bS4yV_ngm3dw9XxHJr8F2dHDAjip9u3DJ9MY6rRP2a89dGCZ-oTgDpnUpBgnewXHtBtvzpl9GvyKKU6HsdYEWEalLzhiN7pntc7xPLiWg8YLhu192EyqznJ3DejaUKnmBAhGLDM_K-vXbG1bBBQflSssa4hHiYqDF9F06m_zq4Ng6yInknSYjOkG3r1ptYpjo1Mh_N05-9BL7-HyGSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHjZN1vtEtLqUVfo4YqS07o7dPobXWySSqI5asf3CsiTXCVcTAF0E_JzBX-xFZdzRNemRM8fk_yMgzDje0JsbnTWUN67MX7PK0GPPiMIUfII2_BmBOs5mSrcjCrF6qjQmT4TjqsPMPpqTOx0wzx05iNiFV_fH4vIr1NUkp3v5IhQ5Qkz2SN_MK47RnK1oaDNnDXPJCBt6bGl2gxBEQPwLrzzzvaNfcq6T_zISy4r__Afmerz5nXIywRbuRhTEEWzAYrgl9PWNObY8PXKf3Gpb3RLUlBHJzJkHou3-TSOgdy34u9IuiggFjFDXaexb6mmxFKfYwQ3hdCp4q0viOdoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdZrK_k01WcK_HAoy7Gdcuo7vXiMntfp-cY5dpCHftFLDRzaPXFJlxGLRcOV3m2vc6dk1KmUIv1U0GgNe3fih1ZcrHPEAwsePnMyVSJWkRa9RD4gOpsb7zfyKbq-LwUEl0XICqP78nvmBo1u18lzBpwCf0ezlZoqQfVG2EPHEzMWAm1YM2duqrvKCbEylW7qEA4xFW62HpT3buJQIOMc4swSqnEjKm2KLoEIvhdpG_P-ZD839ZiF9LzwHfvefA0PwnpnY6h47gNDgmFTHpX-hlfLaXvQGHfP459AL8acu-YxNc8k3v88AUJOfXYncQ__9NoEbh8wVLPcoWBPV8h3fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoLSn8rBXCsnKn9ocYuWlZc1vetGumMFKLwj84HnTtedYv1M9OqU3OUngtuOikDLWySkz-_PXyxxBXsEdsSyzGHEwwzIYMq1S66yFKZfVhDI8sH4zgkQJlUQpX-Vi_nnB5fpJLykENTtwus_08vbDZiwivESRCvduwqrXDp0cSaC3Lu2TE1iOeuDC7xCNJX16xvPm267mmL9HpQBkI-OKqtas27DePstYyxnXaNy86ChcZm7gcqFPqYiyjHgQGbyfjQWnM8VMRk7kRI3o7KDdrn7XeTfkcaf59COFOQgFZmCM6NDBsSDAvnm-mFCFnmqhR4zpwDv9lRuAj4zMMTUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYcup2UA2sCc-C1Mr25K_ToOchn5LgaAMtB-pULYbBClSLHY-Mrmt6esYGWdaEq3hqWS8hXC908CMMNEkZ-cXhGCsa6uedf0pQIin01N9CR6ta6f4h4ST-Uko1k-IpL2fns8vsHZFFw-X_ruH1G2nulVG4h4SxMOTp5Hg2HTsHSpnP3n1ENRcVjBUHBghRtjm7hvf_Ds2Uaxp5QLBjqwJT1FapPPrx4cHawpGB_6U8-vheUMyRnHM7SyPmhCZmGOo_88H8ftQ4CthyhymPzg-BvTSDQtilRlYufDE0ZLrzN2CzhVHL360ClXbI7omSI84vpb3-ax2I0WJwL4GuT42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCld8J2Di5c-drnh5XyRTO7WU1P3TjH9SRWT4aABtbjraTqQSBH4ySxaJyOZ8DWaltUED_1pHJCbu74Ml8Ik2svWEQNUcwDGw3H2xTjasgSI_KcmRigAPwkweio0CDXIREMLsryXwU0S3qfRJQMXRuMl-U4NRrQDK0ZZdwG8Y8-sKb09USOvXNazFKP20Z65FPLAm_NfJuk_LFy_uYNETq5EkHSHcMksgTDq4xfXAHyl1U2pjll9krOkaZcwXB9UcLbKXlUDgxfDfhfF_8ct8f7MGO0rnQyRstvAxuCBd5viqa1ICsOYpQHqcgv3zTNDhyMh2HshFDmSHVwCA6wgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9ASUrcvCziKEP9opOHMqBYgJI_BOab_aOa-ptKyDySIdmHWjD81Jps0qBAO-CXsMq6RAa1ucg-Q4AzyaXcjPU0Y7YB2QIDEirqcJYPwBF2ZbTsEV8QWCkiooxiPpvwVONiWafXIBRWWuMrjgFCe1xgaDkpJj23M7mhsw-dK8reQUTZGTfjYsdmkkOiDUCpLdZd_tJTSRBvvTmKPmZhFHu-sgjZnAIc4D1PoXRt3P9MbcQB0oDa3g4DXG5kDi-dSzdgccKxClwhssoyvzEsnG87HtkxAHHLuC_bhK9k29meOOjTYRTOb3f3ROpq--7Z1YxBeSvV-myetVY5b6_w6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VxTRGTME7Na2lZjhpabWZ8hjc6bVBV5c8HeyrKfa0CZ1m0tiCnE8rTTahHpm9goKA2eCl3VNFuSGNEtEwX_F0TQEVR4NlBdZEg9cFAWawg1wpac1JCrwWwjQflQqBaWz2sdMfEPUG6AYRwN70I5m9l0TbjRxjAFgvcTgaSRuDzxhqL6GilFmVxAVUj-28TT1BGgtRVXJIJ7P4Qg_B--N-XjYqVkfPt2XQuGdDqbESCLXOQFRebKxhxJcge_wlprg32QODRth0ZBudMP3P1wIMyDCZ7Jutw9ddD2O0KXtsEoYPYEPGcGMP6j2DCI6oWpJIDe0TJ8du9F1-uoyNnz6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/unrmPdZIJguID_DTypnVVkQL65zdBb5RR2URyvyaOT_dOVvK91hVnuQoaZMmLIdsDV-eQ4uOxfdyvSU2F8AvG2HoU7xjFhmPpijPj1jjUzvDZc5OOwWK52HDl7ZEdDuSKWeXrZsFdLDAv851y-UtKSWVkzduLYiaVcdQZVowwmdgqy3UnRvQGXJnovHsT9zTc5JjnhnJVGRIlNClqsue-DBxzkrANcc7UDn7TKSAXetjp1N5bAAbRQdg05HfrtUXVoz2cnDYmgi9_vko2uOjIiSu_CJ3fJUvj5gyraj0-Q95PGWrrOo43TKNExkhAB_ud3I7tc5UVrNEA4K1DRk_xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfUNuFGkcrQAkFtXQ_tftJgMGbyod8wSta9KDCWMnESXSb70bfZ8l-hGHEM6hIROgAiS9cXN8qB8PkZ1sEFMZEZ1p5Sog9-P9iFmk-9Tv1HWWUTuLS0cMVImVVKKrAVH0m9ZPVLXPAXXXub0LDkLdkeE1uzBd8CjpcDEaOJ8zVnX-TmESax40EEcqc2Ck-ixa79xkUqF_ZY-VqWMO9tmaXSxIAGNFRY_DrNhs5XN_2OlKIaDNyMoB_RR-577TVKcgYPhFxc71HLFahzu5HfTxRoEWyCW1qtBu5QzMlVCjZu8B1teXvAHQ9xQ9D9AQEdgvt2DWoO7KUkOUnXY4S-r9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=Md7fpiZWvYzWVBThQCo2SwPImwsDebaY27xROWjBj7drvnXSfwRq7qqXhEccGbH74Jc9WQhcHDZPZ9hUZL_y5T9jaGpWICUBwUzdD_7qPgla9msHATO0SXe8wMxuMD2OeLLBmt23spOPtk52ZYskLmDdzIhdmu_2wqFHyohImSRCTKcUeMOWUrsr1BIYmKhJNOOiEI-qO_Lpkoy54fEnmd0ocUVvtugah87EeDR8vR6uPKqzLJuw0EdIhIbp9-F1xvB0PEDBhi4OSUcr-Dw6Iir-0FEvGNIbqonCXP1aKxJZpIQsQd7ZXeDRrWmn4ZFeh4MXh42tVnwWkJCIk61k4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=Md7fpiZWvYzWVBThQCo2SwPImwsDebaY27xROWjBj7drvnXSfwRq7qqXhEccGbH74Jc9WQhcHDZPZ9hUZL_y5T9jaGpWICUBwUzdD_7qPgla9msHATO0SXe8wMxuMD2OeLLBmt23spOPtk52ZYskLmDdzIhdmu_2wqFHyohImSRCTKcUeMOWUrsr1BIYmKhJNOOiEI-qO_Lpkoy54fEnmd0ocUVvtugah87EeDR8vR6uPKqzLJuw0EdIhIbp9-F1xvB0PEDBhi4OSUcr-Dw6Iir-0FEvGNIbqonCXP1aKxJZpIQsQd7ZXeDRrWmn4ZFeh4MXh42tVnwWkJCIk61k4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghy6eiLMMrmsYzrkCOUwaza1pWvnDm-jN6IQS2gwLya0SMNqPIuoP8C6aCBgkH6AdAq9ZRNmwgDSrFWdPwgLtdG7w4dh4gplVBYKprIN1bfIwBLdwT2zQye4Jo9zSts3ks5dRqiBLxmwrvPwCTKp1QrtnmOZrvsvN5SQ5aA0zpOpa4ejMDmTbMv94gWCytrNpDKV48VQXovSqUDIRh-q5I7RRS2pZNbfOHFLPBtn9kwLZTfI6wzyoZE20ViYcc4Z65B_H1YGvgtaahazde55SJfP8LLSuwmJzcdnH33LCK0s9lDxMhj5l29Gjs4bYQgg_RFgASBqUY-gTIo8pZIA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0d1GCcTbJzoEJNtWsIYTAkmMuAnBLcJHvNFAyO-Nh839ksnvQ-ValjmKxNWWqscTMhkp-QQvvn626LNvi_5hbs1qkruxNlP8NeZ1xLBczkK7_BnlF1MmT2GUoXS70CkGAPhzL6USdNV6jQIhCGAZEbkP6Dm7F3wtRPECo0w3WV4Tojx-RZX7ZRe5pd4_LmwoCdI1w29j1n25hhACE_KlKRP6KQGJhzXeA5N64XgdTuzBkVTWH0fBRAyMbjG1PkOl_wWroTUh9i76-z83UvmpomjuhAiK3dJ1EX0GupaxdnnhuO6FZxmaXaG9h63kjF3ZNHFfFDOorRl-PQO3J6e0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BbJYGXXLWJEqVFhXDE5cN25eGqJz3HAvdI8RwstKrcaOyxH08ixcRhtac88NwkUyfEV86XXYbt-1L92J08dK4SIXnbFIkC6YanKJyYaH1LcqXUo5c4CFvZqMbws7WmOjQ6b8Yu1gIylyhMVBewCxPtlsjXgMgqounkpSppMpnoD4ZXrgwgIkZPPXuYqhONmmho0sjeqVTErjXj7BgfRX9DBvRn_VOwR3FiBcWH9O7WI-i0EqqicTbVkb42jsSzsnmjAsgEuvlEi0KaXXbLDLV08zllwSmlm_V4j_aJ17EfaEK4hfTsbV5LRP_8Ye7hj_LN2saMqPInCOn1S3yCbxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBCF2ai1vTS-SlyAWO4E5IyspcYlHaDGIQAoC8m6WjHixonZxYLHZ_CQW7oJZijcnfIlHMkZ6Go-55p7fPtbYaZaxSVPH7nGZjR_iNDOmHSjdkYTqWovoFD6BuCwVgiTRT_PUpKwnemoR_elB556-5d4JjtK-jDnzuce2ldj4loWjQeJDDDmLZf6JEFd_ZbPEZQtxFQKcFhk6CGafgIcD8cvng_54rW0X2usHu3zOmmlJOPW6uhtjJzYGRUWjjYxeaRV-wjMpitHyO1bSpkjDtTGjPIBCUjVa9H4YLfdqVQeNv0TJyM8mWkf3L4oLgnG-9K_ynm-SfGSOECgmChbdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
