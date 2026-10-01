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
<img src="https://cdn1.telesco.pe/file/pz6RWa6ew1D_KC-qHCWTWR78y-LEsgsKzGAGktx7lCEWSM8RbvEei97jaLvMUeU7_wr4BNj0WU35zaKjZ6ww2p9kVZI9Gc848c7Pao-bck5XJmaxnU-D7a2ZYxjzm8EPDt9GdmUTdd7lDGEPcaKvDnAJvbB3admnLI_DpUISJkJqTGUiLWvdqqSJJ0vEJt56RCsk1JZYbZYqyTyrGI8iuoCSY6Gh1rKFm9aRwNgi1JMzmlCwl2rkfSSOUtl2z6hM-c6iokxqNQESJayWRfpHSd8wcjk2DN6cBeZ63qFSrSlyUZfDIqiDEJb4QhUNIrY1BPU1ihGbFexaUDShtw-t2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YbVIKSP5Vxi8mqf5n7GTNxYi84mUmwNFfUUG6F9ruNLuf_nxAs175m2lFSFO419qrK6uhn4Pu1aOBsZiNbqznz_7bnDZh83HIWt4aGdj0TtaANRubdD_etroEbLzQ9qS9jtcEYN86SttAA8KWqFIWfEosKNBdQ8cPeTTsfjIexJN-y6jvEUDzFnkHjPc9Z_TPsgM0UvqVkMkyI5bf8td1tv0Fa8Y0vRB4Z6MEimxG-fDVrw82_uA7k4jk0JmK_oAYyJPg62Q4aZU8znDUskRLReA_tksgVySP86RgfcGKdfsa7uRyHz3DKcp44WD1wLjafnx2p-zSXUYOAEUdiE3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llz3JOxKP-5wl9UMk7YIHtZcaGex1NDusu19Fn6djEnjyfSihmdU4b4ywqDSqFSrz64Dy6tQRmRzU0-NKg2p8OvIEJJTe2hYNQayc8c2qW01G4WrPdZ9IZhVw2M21PQcvnav6LhsoM3fQvr9GjlDYuAPhb4ifoylPh-MjlFts9drpBgwN9BZJzjd89LqJiTMnJcSpUAlvdzWnDinPSqPWFhN0x0ng_l0V1SY0RQfJbChPIZBJWUWvkJDLLP2HW0CchXopr3MPokx3cZtsQHqAr-g5d8owLUWC4ai5MHDmPtMcmAgsFIaBCv0HzMfbdw-pvnkVEe-LAbssJJNU8hMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVffiMRqr8tKXKDmfYdboQieWghQ8nhvF0BXUslxItG3S1EvtidRC74q3X7ptWy--p-mVTpKG0oxgu3SL3i5rX-3m-D3vQbMVSX33nlUxQiEOhJL8YUvlITrcQSR9ZHcc6fNBtq3tAMuD4LxJdxP10DH_JG8y34MWZvFBL_GkyocGJKO2_EjOdiU1ZKx8nik0cb1YmycjOEyPl1sbWMGXU1wpaxBExgYUtexrItUd7kmofYPeNPgsaZnbLKvbkURprTBVvo6aZo6Kbg_ystVDPl-HjHekbUKA8IqcONAgmNv46PbKLPM7MIVbI2c4_yrLWlV8JSXht4ICT4ArnSJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HN3fBCNqU_hvEJe72teRuB-Aunwu-ZaWG1Y8kUtyKg_xvuFUm83Exj8dCEH0BRphB-I1_8kF9o1v4F9wlTO59PtozEFvPDuf1_VTlTsxxORL-SHkGthTB0Kv4phmYE6tttRS4BIDKf1kEVJkW25ymXiXMcV5dNtD-w0a3xAys1W3TeeHe4Is-0W-aYv87hkh6sbj1mNrm4597kGRNab4xVmzav7qysPW3o3yJhlRsARW66N_2goJxBiHgTVfn8Oa9t01vFXjhfK_Iw6WSj-alSQRUNjK65svBkS7ut7Q_sl2kIY8sLCmLTeax4fnxx8RwLwp_lhUpjynzImLkxj6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GzTJrZnVmCcbf7lz_bS95mdK-n1C1_oU8Eo4ligHmIhbGqLZb084rFM60lScA7H361dbNOTzipXM40dcH0NRrOjK4zGDU7uF-BTSYMB2AR-Fn0hMwkRxQgSwa-zVbdDFKAVmG_RN03E8p1DYNkm3CHZgsicb4-yvlVc1beCVDzoMtKvWBoQUu1aLVjbUXCEvXVv8bp2zUJCUdm4lCTmpd3QhOedOe5TfBd8vGtlTvwr8Z72JxyzLKweBXrXIWjxuaCmWzDbShFdSRln4OuQedqm-Non6mHjOlFMAD_-0ZjYk4EXFgHvDTxt1a59wQBElZ1im8Yg_s8Ir8P0Ou__aAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V2TdN4wlqGD5gASYzU7kAeIDW79SmKpL2VyArvPYc9MTmzh7ab5gFv3USuE2PsUeqtkmNbE3WbCT_Fhb2LUzlBahmCF4G99M034MjpKccoueeWDJorBj4zmcv1ZSXd8mTfKsjwBbSU4LMfojBzu7ow0yi6KIIKn4kaXkHur4ewXpNepsVwQZnJom4_ziZcW7-JhpmH4TM_wBg6UKXrQjrjTfC1tVvuxH7bxDBNXwp2w8kkqdjj7GkgzCSFKJpqclJPMzYUZFwOaeHNVLDhq4rr9dChcUrmdCgUsOvG1vlWPS15Gpaxc-ZTE1gbT8h9YO3GCFyXh56LlhYcX_PvPi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2LW-ZaQgcRxNm59_Xw4z7z5Xx1tROc78yyVQKKcmYJKFCrn3GXW3xA77wG8kartvQQQemy7br_ptjFsn7llMc_68QWAvFajRJYXUxCbAkx9bh8VlEbXjp1QSmvFktUt-j5bYtJVoNuG4TkUvmNBOW0NkJiSJGZWzbenOfi9jBuz1yoZM2as6VF40ZxkrHZqDYgXdXZq_okxf6_7yniN5nosXqJe4QpKmd51ulInW2qUhIfYZDfeEwpNvP-Y05xbZ5nofQcZT7jEo3C7xL5UyLWDzLqfwsY8TMrQSlKmorbPFfg6p1BCANJPBNwJk7lmMFJaRI8bklqbjwCzXnTeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EA68HbVAv4SjXTOYXVt3Q_19JAKjT6rEqEmhJGFCN8aUtpyyPvhs5DUUMtjq1mAMHatSzTQDhF9jkrVMW4M4I9fq1R6nrRJ9VI2QSZ1-_arkqxZGH54q9iW41EeXsNCEr8_qXY8lzZpc7kgTGVvNBxLX-gEX73D5T5u_9OVJMYW3Vsas1Sx7YEGmjTn5y762g9ywCHVwbdh0qWwPWlVzaIoM2Ed92f8D9lD2X8HDja6QRwskKu-PIf2Rz6HUINXpSt_naBnjNEZMO3BrMflsKsDj_X8-cLJB_wG-cJEgyhVANZ-BTtgNntRSsT2rCdh6kkp4SpgkZ-s9kBLkp3Jqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=jToy8tkBJfP1g_di-84wvCBmDLLfR__tJVBTXTaBy5tNSs6z90tPp4ksZkO2sb7NinlGUi8OQ_N4utmqiaqD85eZhKPNXdqHbBKB5_bDKMUyRaDEtt5pLZnrBbHbGo_8YJmxLYxVgYIBs5ObYgjTKXuQI5t8q3uk2RrM0FYiZFWKTB3GCvnev2pIZn08I0OIOJev83epL4V76Gy_XVdHrkWJPjaP9ekzhtc4tAVQ2ilFceh6QH7oYwcK-2ICO3yC88kuEw18KnYyJvtvptnWvf1d5w0yYItOK5cFagQwKu4wiwh6TijYEmla1sAjJZzNUezoi0vzQA9rp3mV_CTggg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=jToy8tkBJfP1g_di-84wvCBmDLLfR__tJVBTXTaBy5tNSs6z90tPp4ksZkO2sb7NinlGUi8OQ_N4utmqiaqD85eZhKPNXdqHbBKB5_bDKMUyRaDEtt5pLZnrBbHbGo_8YJmxLYxVgYIBs5ObYgjTKXuQI5t8q3uk2RrM0FYiZFWKTB3GCvnev2pIZn08I0OIOJev83epL4V76Gy_XVdHrkWJPjaP9ekzhtc4tAVQ2ilFceh6QH7oYwcK-2ICO3yC88kuEw18KnYyJvtvptnWvf1d5w0yYItOK5cFagQwKu4wiwh6TijYEmla1sAjJZzNUezoi0vzQA9rp3mV_CTggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqEIKwtYp6035H_gJt7nDBeySusjl25RzjmO0IDq_avtT96_0aECB0yZdgZD0MBnh2uWl7S0LTIjgoqnF9pbc9yjxJBozE5ai_vAWKYLRnsPFFnJYAdSLkZbwWGYsK_A3RYEJEggvD55baD4q9pmEdhgxZKuxaBjZvBWXvG2MxdGQMSimHSSMB_E1ebaXtq5HF3732AMsmeHNLZaOEDRvT7QSJ1WUL2CGTLhxX4s1MWcbddbuftcu7bunCfd1xImqzlrBJolI40O4BjmCqv0m8nuUmWNBXDE9tw3ySH1RymAYvVY3z0j0APn-ctUT6ZffBi2xS3HVCkG30BMQMesAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGtFarckMkzHFlJPSPmPSbk4RFQZEQCTR7JwOyFG0lHKAILn2esWOjgZ2fAznrEIfUQ117JoYCQdw5s-EWntkzMS8BnPeay3OHN92YBihV7i0-RBTgWm7UNiqTDFsuelFlGWiWsFakMU-WSKzKhpXjznpdh4-8GGrd5Vlnwwwq2Pgl4Zk9dEtTyHO_1F1HK8PK8YQOhoAUJ_m81X-NZiwhAbahVfYU6W3Ly5fB1VTPovMxwH7gZB4lboSlqBprgEznlqt9fSRxPeF7GfMD7fXDDZGjA8xkvgwCSeHxGWiqTvXSR9f8hGzdA3ag7Kr042wu6g7uopus60SdbK_U3_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه، چهارشنبه هشتم مهر گزارش داد صرافی‌های رمزارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کرده‌اند.
بر اساس این گزارش، این محدودیت از امروز ساعت ۲۱ تا یکشنبه ۱۲ مهرماه اعمال می‌شود و سقف خرید روزانه برای هر کاربر دو هزار تتر تعیین شده است.
این اقدام در پی افزایش پرشتاب قیمت ارزهای خارجی و سقوط ارزش ریال انجام شده است.
عصر چهارشنبه قیمت دلار در بازار آزاد ایران از ۲۵۵ هزار تومان عبور کرد و هر تتر نیز حدود ۲۵۵ هزار تومان معامله شد.
پیش از این بانک مرکزی جمهوری اسلامی نیز اعلام کرده بود اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9b_5-DsnfyfRTZE8PyUJovVAdg_U1qdZnyiP41-CtPdo1Wl3ukYWwzacY5_w919an5k9Gg2S7PNvdwyowYUpESUoChBRWa4F-F_E_v2bZDNxzKaW5riYfhoBkNp059clp-wjJtzUC41rIPJC8JM1wcqPkzUXslTc_6is4hlW3N1vVTkFxT1ynwd0gNwduPNFUXimOOm68kzEBddoDhFTpmyOu8lkWRgrHW-44k0GWGY7BiT8_S9-3ZT6Fffur5pRoqFA3a330Ldk_ZXQLJoRom_E5cI6uJpA8Kpb-XyBhQswDUOyxUDw7Zk8REKXnsCFtnZvdO2i2pbv4Mv8m_p0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKDzzmA0l8IVJGFZpm9E-XTtKrEoNdRX873Q2oBHojztS1WNHwmkJpxf8JoHwZ_N8FqxVYXFufl5o303a41Titdz_Unuv7mDk4_OX0b7anYjht5Uq5WrvyQUNWtifbSjGB4aTt7ICHuZ1YTJyX10y2LnykKEStrcPvy7CRY3SWRg6eZRtO_LqQPAu3KtBRDGc3zwVDGwwtfABJ6ycCt0zQWtAfxXGMLQucRqJoKMPFOpq64U9TMEl4KbBnlAEhnq5ADNfWDrHRWVCD6DmSeh6XJ-9GBW802ZNLFGAJNDFKSriR8zvDwAyEp16sMiI7LpQVxyVPXF4X1CMG4XvTOodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=edJEW0WZ4GcM5Kp1RAOlwRID6eOlJQ9QDqS_lqgLvL4x11q70-X4Nvp8uHF1PnOc1JVWi1tuu6SN4q2nnhSGT0Y8mk2H-tT5DmXwX4XuPV_eVU-gJtgXUItJCJQbEZqLlPNR_Ib9TS5PZg5yWnqC_3KEHXHLdfdDagkxeh7WGgIQT33jDZFmHVW5wzlt4CYcvrXHDmrxgaqDQoGfrr7ZIZo_GJKjQZZDmmyvjZenJvHN4BRbTPCXnXL0-7irnw5pOWG2agI2wLIYT-3IHxn6izYM5nYRVZi3JwOWP0lxboZDi5TApsKWiatOby_51vPnVyC8vUfvcfrUpkuEKooOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=edJEW0WZ4GcM5Kp1RAOlwRID6eOlJQ9QDqS_lqgLvL4x11q70-X4Nvp8uHF1PnOc1JVWi1tuu6SN4q2nnhSGT0Y8mk2H-tT5DmXwX4XuPV_eVU-gJtgXUItJCJQbEZqLlPNR_Ib9TS5PZg5yWnqC_3KEHXHLdfdDagkxeh7WGgIQT33jDZFmHVW5wzlt4CYcvrXHDmrxgaqDQoGfrr7ZIZo_GJKjQZZDmmyvjZenJvHN4BRbTPCXnXL0-7irnw5pOWG2agI2wLIYT-3IHxn6izYM5nYRVZi3JwOWP0lxboZDi5TApsKWiatOby_51vPnVyC8vUfvcfrUpkuEKooOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwCkfFMZlLCgW6z4HImBGNZ2DDiCXyQoI_kqctoLHU4kPapwJzlftk4W4CmovjHmfVzxv6Df3IZZAs3O3CVx0qvP6fzG76CVCH8YasjBwNNpCUd1Vezbfpt-F6Pw2d1GX48BABpHwMqSd7EFBZ-C4gTmXmzuW3q0O5qZvRXBxf80fG66g4nU-aHdW2Ms1db9fcwdaF2Yu09Xj4tJCVs9bE7k2CTbckp47uLdsmY5h6_JvDSC2RHeYc-p8Hr7dAoxNteXkjvCmZkvgzArsqTaBNSwpkFiYDEL7jxRRkW70_HgFi-h_-iQncC2CnoSnEYBfd3QMh7R-Q-9uyAeA1kNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgGQYQSjDZlhzIGufsLhdDc5qPlV8M5pGtg1aVpnR76ycdXp-5wiiV1kRI-XZdU0AKCZZ2sAMt31pjBByvsZD7AKVl0udAcvcjM5PSPu9WPfyVIwyPQcH7n1S1bzuUpbHR8lfDV84rw76fpmQcsXLMZlZxaFe8bkjOxYAWVch-VyazX7wr7TBwZVZRz2utAPTiPlKmZof-vDiDOvvH4k7DygR97BUXn45CF4zXkC3xhlY6JsxIzXcT8U255OKYeQFkv7IU8gWZKzuTohfJ-SrLIOclI7mTTKCQ8RVXnYQhIa96lygaNd2MxdEUaWnoN4HzE3Ix7y8WFuatwus79aYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3SsSv2Hf4hDK1NBhGlqXm9PQiqOM2Wr-IOoADE_MGr8S0k2KyE8xUwGJm77Ra051Xky4gpn8Fd8Ov1qB5N8q1fqLKSVzXTumUIz_xqWLb2O6YdNhKEfMT0zvrFNwXfZgwOb7WAGmHuWV7ZzFlPrl1GmUu5Z9y-p88KnQh7_5AgffUAto7MGlPl0F3IT_f9fOhah6hmOlSFRcnOAY5QmifuXkp5zLjrsinD_GkD452XF4FCfoY75-fDOxG3OTG5cwKe-y0Ngb-P7gYm1t_GoQBlphLyhvmFhJIuVpB9LD63x55CxzP0rGTvzYhByky8g986dMUWL0lCy8_Df6_XFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBN_Dtu1hvTj9tGzImrVRE7PU2rto2rhgg4V_2ETso-D4m0AHpzFdkBA6Q2wbkFhUxFZBnMCaK1keUEco9X2nawgc63Qdk8CK1utRPOCYC0qfe0N-xFw0WHP4Ou3Rmvxj9Ve92GQVlkMm0j1p48mnQv__k3xazLoZ4MVF-uCZPtu-0wVtT84s8TcTvvTIgleb_w4nOJL2e_rgxG7zy3N-Ex5S5PGIJ2-Hk8JMb78dKS3kqCEQaQhSlKPGKVQLc30vWKVQD7UH6Tcv8fuaj9joaoR7rBaH05l00kcHYINH1mO_4NPLOja0jOfC96SLsva18z4koJ5AzmsraI7jOKulA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
«برای کمک به پدر مجروحش رفت که  هدف گلوله قرار گرفت»
🔸
هفت روز طول کشید تا خانواده محمد عباس‌زاده بتوانند پیکر تنها فرزندشان را تحویل بگیرند. در این مدت، بارها به مراجع قضایی و نظامی مراجعه کردند، اما پاسخ روشنی دریافت نکردند و تنها به آنها گفته می‌شد منتظر پیامک بمانند.
🔸
فشارها پس از آن نیز ادامه یافت. برخی از بستگان احضار شدند، از اعضای خانواده تعهد کتبی گرفته شد و مقام‌های امنیتی برای نحوه برگزاری مراسم و حتی روایت چگونگی کشته‌شدن محمد برای آنها محدودیت تعیین کردند.
🔸
خانواده با وجود این فشارها، پیکر محمد را در زادگاهش اهواز به خاک سپرد؛ در حالی که پدر مجروحش هنوز در بیمارستان بستری بود و نتوانست در مراسم خاکسپاری تنها فرزندش حضور داشته باشد.
🔸
سرگذشت کامل محمد عباس‌زاده را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-9241/mohammad-abbaszadeh
@IranRights</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUDh44MDJfEeswOSlma9kl91vucetKG4xGJt9Bz3041uw5BwVf3rPXthEz7oSmiGcCr4OgE3kacWuYS-GYeQn6a1DbO624IAHxfn70H9TELrNEcuiaOQggJU-3yC5YHNfJUt1fPHk8hJ5naBNYilDpFfnatT99Gw2rBBF2GcN39z5d8YPbaI020tP9IqiWLjZojLLSPRLVEddK5lAP6ejOWk5ow_ud1AT75HRlMgreI8Op3uN_s6dm0P8Q8R_mo9oXvYRAC8Xlnq3yUJcJOp4YKtJtDca1Tnkg9L1FURwz1WFyJiBPewW8oqUy5Qs-rM2FXVi-Rlp6l9UhpxKj8YZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BG7Cn7GTIjmkatKzoWSnQ2gr_pFdwkzCLZHfyb4ZT6aGAtUcyerFoiiTwpJCBlzjsiSGI9_PrYkatjlV2-7IFii9UnMsDlS5z7mG5quGCPfww1fs6-5IodS-OViCPHJzO3vrRBXmzxFecIIxvyGzr0tKa_HBJur_E3_1_F-NAVd7I32YqZutXMHX5yvj7TyfMeAnI4r6f7LAA7T3V0nmUczmfw0wN1x5NUKZfox19v_JHIscwX5R82GI79sWdCThU5ukai3mDU3HHpylYh7xPOjM53rCza7emBktk6E42RA56j3JsSAJCvmYGJiN2crvu6A7v715pHcklpe3LiMJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KxLtfbWxCAql3n5WnuIF5SUkbDmqK8TpVZGXlZPoXqxp2qgbacMyB4Xces9mC_Dt0x6GRKp-L3PXdBTK4yDIup8YX072ow2_AlAafq1Gy1bfI0oINp9fAZpCohLD1qRbKjNs9vVsx4BWaf-YQh4YxVpx96tnokne2UGxFSLWWMk3qkhp5QmW4KjQmCdk-KJMKdICTITMl1WJIBpb3nv1V5NHHkevLdz7xkjWx3dze0dbhEJd_PTonOPGe14FMW9KF-OCOL-10Lnzl6X8AoNbAYRw2_HCIXI_NKpw7YbIKC-1vd34Htwj6YaEP8STXoSaT67uVf6FxTnsS54gzfXL6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن رضایی، دبیر "شورای عالی امنیت ملی"، در دیدار با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، با تکرار مواضع دیگر مقام‌های جمهوری اسلامی گفت: «ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.»
او افزود: «شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است.»
رضایی ادامه داد: «آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.»
@
VahidOOnLine
ساعاتی پیش از این عباس عراقچی در آستانه بازگشت از نیویورک به تهران گفته بود که ماموریتش در این سفر این بود که شروط ایران از جمله درباره بازگشایی تنگه هرمز را به اطلاع ایالات متحده برساند.
وزیر خارجه در جمهوری اسلامی گفته بود که «ایران در این خصوص طرح دارد، شروطش، کاملا عادلانه و منطقی است و اگر آمریکایی‌ها ادعا دارند که دنبال توافق هستند یا دنبال یک راه حل مسالمت‌آمیز هستند، ما این راه حل را معرفی کردیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=sgELLeHJ91E6lYBlSYCUIEaVbNQ12XRfOR7eeYL7otIaG8ibLAh_lF2o2H0M1znkqHM08zLF9KisCC_H4JI5Ut-ii9d2IUZgn9HJ8sQwYaFLERqnqp4MsSd5oYjrO_Qecvsx9dHVXqwuyL8MTfQ6bah_IbLtR80Bv-5eGMJLQKMU5ICNkzzLzqKFX8rObgJCAigI5Afln-twTih_DjnTGfC0MQZbk3Diaa60FhQeMmI2dtqyM5-zgAuK_30vDnDYSC9NG7XDLbtsmCzul9UTh10HjT-7u1mL0t4n5w6Z4Ml3K4BEhP1TiZOJUS8Dq9ie-76q6azmLJ9GEIkuo4H5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=sgELLeHJ91E6lYBlSYCUIEaVbNQ12XRfOR7eeYL7otIaG8ibLAh_lF2o2H0M1znkqHM08zLF9KisCC_H4JI5Ut-ii9d2IUZgn9HJ8sQwYaFLERqnqp4MsSd5oYjrO_Qecvsx9dHVXqwuyL8MTfQ6bah_IbLtR80Bv-5eGMJLQKMU5ICNkzzLzqKFX8rObgJCAigI5Afln-twTih_DjnTGfC0MQZbk3Diaa60FhQeMmI2dtqyM5-zgAuK_30vDnDYSC9NG7XDLbtsmCzul9UTh10HjT-7u1mL0t4n5w6Z4Ml3K4BEhP1TiZOJUS8Dq9ie-76q6azmLJ9GEIkuo4H5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qq5nKkN3BSjQZns8riXdnmfq3wT8R2Jf6t78gYVIj-YPa4Py5fCKmFmOYkNkETlf2M5OV8vZJbJF0xGbTPEfSw82OBdbhVS8DhLZvOCuLOFqf9WJijXvxhF3rLoylmWnd2v30D24RSTc80DBMFjDRJJQBnKhC1fB_8vAPFOyIqovPAGngBl3z4zUrn4g-EPCAydbMvJf9wPNbhnSI9ndshoo61C1YXL3QcOA6xVuAMpc7mccWm_f4DjnErVjCjKA4WlqWjmCZPtJMx42ku1ahXHy9pOp2X1WuWEPmBGtqXJ564DF8-xQeO26rdL9vRwPbgWcZEFsoyQkkDaJ12DICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drFCkYWQv4utIcIUSwZrbpQdVehjF4ZPGe_wY9AccPV99tftSyFkV8Ll3jCShBz5fUn4sIGeNl-ysOpM66RtUryGxO0sswYG_Cww8_ROMkBl-V7-rRWpHcvyNQwqrRVt1YwZ7NKpDfQDNjW4KbvtNomH15Q57wsCmrB5m87NkMuJZB8dyUGiTlui6FygaoCNBYNdqGOwbrYOs5OyDDMw6L_alMkOwYfOYuHOzrg6lAfqGDXTlmUdHrEtsR7EYVycl2AiZaKPtUW4hQuYllf9JtwHvM1yaiOk0stuKVoe8lctMrwQBamLlvyMFm3sCfxZgGUSpcRED45ekMvJKcR-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zif-XhpnbB5W0PGGdnGNICDj2PmtYLsyScLOYOhhhAgPSsVPFZO5QRyqr7hKn0xJl8svxv0XPqYsT6G_hCEc79HlOuwPPTpHRiHH-QMVLfkEdKY98aqDY00ojxxLx8sMywDyr9gMJbbUOHQgL_AkuwMYQ_dbaIF2arHKykhjv0OEaBmYQkgV4cSL_ns6wpI1h9ERkP6ns5DsIuku81zeQwTBYNXNai8D2iemWtsePncqZbj2PPOC1QKHpaShfk1j6_2jdvdFyvW8KXPzaXncFCTXNkcIzh8uhysyovfkxowXDznwvmQZFOtNm2RHbU05wFAsDbA_qtX0sTxooOU_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mt4yqG84Schl0UVqDtdwe6iaS0afS4lFo21efJmxZ-g1cRFjUPwU9fiaUJhqn8aOrgU3bQGNr-wFbGhUDD5ZbntbhFlNmkUC0F2ZZo6AqLXY_w_d1-lPLMUUFUYWyHdLYbvIUExDVug7bD2E0KPkiNB09H0Zuhyl0FIyy0V6OWxVlHbD2AKtSZwCqsi1iq69bokYxlflbWB84fgmgRi3_DpMzVLgRoJWKnZBArhcOIUCAQa6CZgjBUuceFKk5fHz7HgrfKn0dBuy83XZbuYsCc011lVbc3CGufA_MasanuAvNzcRvyv2vsfv0PORgRXVMoODbXuHY5xJ_uaD-gU2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC-p3URi7C3EhDEwDwigLdKLNLOjIRmJ4N2eswkAMBaK4IfGykbQ8nw50PJcXwU5iqJiigtAwjg0tuaxEpSqAN9iIpTDPNh8lf5IKLpS1hQFQ1eoYxZLcHcMZEpIAJ1WJxFItpsZFZXq8Nr0XYdA2KDtkNaSQbQXi4mBZ_jnqhMcqwKTg7QMiZL2Dmi1A4FYxwOEmU7DLcMV8qEIxNCm61AQO08yjkYmxvAdvU71sawalPPpAKtHAJjywoV8lPlE-PSro3fB7sAIY_cdKLJues8ts8oJmQGM9E4BXwbIYCjtPkCodZlkOy6CemlM6Kf4A5w2aqTvxAnYeh22tI1bdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی روز سه‌شنبه ۷ مهر متن نامه‌ای خطاب به مردم آمریکا، دانشمندان، دانشجویان و اصحاب رسانه این کشور منتشر کرد.
در بخشی از این نامه که به زبان انگلیسی نوشته شده، آمده است: «حساب خودتان را از اشغالگران فلسطین که خواه‌ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.»
سپاه که در دوره اول ریاست جمهوری ترامپ در فهرست سازمان‌های تروریستی آمریکا قرار گرفت، در این نامه از آمریکایی‌ها خواسته است «در برابر سیاست‌های دولت خود موضع بگیرند» و «امور خود را به جای اراذل به اندیشمندان بسپارند.»
@
VahidOOnLine
حسین محبی، سخنگوی سپاه پاسداران، در نشستی خبری با خبرنگاران خارجی درباره نامه سپاه پاسداران به مردم آمریکا گفت در این نامه درباره «میزان محبوبیت» سپاه پاسداران در ایران و خدماتی که به گفته او به مردم ایران و منطقه ارائه کرده، توضیح داده شده است.
محبی گفت: در نامه خود حقایق ژئوپولیتیکی را برای مردم آمریکا روشن کردیم.» او افزود: «از مردم آمریکا خواسته‌ایم که نامه ما را حداقل یک بار مطالعه کنند.
سخنگوی سپاه پاسداران گفت: هیات حاکمه آمریکا به مردم خودشان دروغ‌های بسیاری می‌گویند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ID4RnByyj-TzTH9KWz9v8ZAG4c1JH19ngHaB_A0Az6rdDE0PKqylnc7tSsGA6Yg1LgPDfYY9E8b8TU-9s3Ww2Y9IwK9PQ9hnRTHPdCFM9-wla7kI9ix2Q605iZYJUq_JVnvY-HAwSMsad7SK7vJUlCPoV3Ob0VnUXs91-bgNbzg3t7J5MYnfTa1H0mc7zNRpaZzho8IIJkzsHXhbVDc_b8Z1Jj9z0vjGcr_acakcpJGU9khvae7eaDU7caQIVPOVC3IYHG3LqqqfmdVKqtY_z281BEotWg3G-OpdkPpnIdFH5TI8XI8WQM2L3FL3BrLT_hLwlyOLq87YM4cw7RMRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t5LXxOuvHccl-bJNoAsFsN_kvZTVxKA-1f3Gs6Ftaa1SKl9keoHHdQ_wMdkzPLj31CruB-kHTQIFTW4bR1YJ8orZyg3R6UgBAQs1xvWBIEXfIFK2tVb-M2ZUk5A6W5Ro5R6xsqBz9twNdttg9GIYfL2PBrnhX-BhHwVTZ8X50CH6jshEnsEf6NKup-8qNF79keusn5hylGPbpY5ZcILiLzv_vtdIhTCyzOd_nOlPR5kV4UX24vfSR4_ms4xY30ZGIf2GTXOYuTnEP1T-5U99WmEX7K8Ym-ihDj5ZOGMboTUTJT1r2P2LBF4tpw-09bmDpUtpuLA4TGu1zp8cRKbfWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سه‌شنبه هفتم مهر در جلسه علنی وبیناری مجلس، آمریکا و کشورهای منطقه را به حمله به زیرساخت‌ها و نفتکش‌ها تهدید کرد.
این در حالی است که روز سه‌شنبه جمهوری اسلامی در انتظار پاسخ رسمی آمریکا به پیشنهادات تهران است که دونالد ترامپ قبلاً گفته آنها را رد کرده است.
قالیباف گفت: «در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.»
رئیس مجلس شورای اسلامی در عین حال مواضع دونالد ترامپ علیه جمهوری اسلامی در جریان مجمع عمومی سازمان ملل را «سبک‌سرانه» خواند و به او گفت: «بچرخ تا بچرخیم.»
روزنامه خراسان، نزدیک به محمدباقر قالیباف، هم نوشت: «اگر مذاکرات به دلیل اختلافات هسته‌ای به نتیجه نرسد، جمهوری اسلامی فرصت استفاده از نقشه دومش را خواهد داشت تا به انجام حملات پیش‌دستانه روی بیاورد و یک دوره جنگ پرفشار را قبل از پایان انتخابات میاندوره‌ای به ترامپ تحمیل کند.»
شماری از نمایندگان مجلس شورای اسلامی نیز دیگر کشورهای منطقه را به حملات جمهوری اسلامی تهدید کرده‌اند.
از جمله علیرضا سلیمی، عضو هیئت‌ رئیسه مجلس، در گفت‌وگو با خبرگزاری خانه ملت گفت: «باید پذیرفت که امنیت در منطقه یا برای همه خواهد بود یا برای هیچ‌کس».
او افزود که جمهوری اسلامی در برابر هرگونه اقدام تخریبی در منطقه «تماشاچی نخواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=TIjb6FNGcg-PNv7pcgwR5q527FLIxhK1ZvQNTt-pOvje6r0I2aNKfX46XgfI3jEyW5hYiYNwAkiSq3c_630JvAQd_PRUCUchIFZpz1k-90Dh6UoEK3aiNjK3_x9nGrIs_2YEo_MUDJKd6BMjCaBMeEpNfd5d7VpnAnkfdBWiLOv_7r3vT-bhppdKFkpjlFXHDd9Bkuz3XoPCsbvGedKQddaWMVfB_XyeDfxta-YKA0_AsCvQV7l-IHkp4s17uBe8R4LH8oy1xHzLVdVjOvdbGVAscnp_PT7weJl8IBvnO8fkIcUI7tekcNLhmszIPwNIMFPczlz-f4X5j4S934rApUO1iohXRoBII7l6514-NSA1Cczm1scg0HG7w_j5A0uw_dO9Z4GJrCJn4xUqpS5j1CQjiyikI8G0HzH8ZlKoGCo6umzmFofh0F0468wh6qkjDuCyHBmxFNpKqgGx0MRz2DkivQ3zL5z_XSI0lxYT2AksCu3x0c1qXruok8tbMs0MSpy0Y1BZ7aMtH3K2_TlDDFR0_H_oIZQt_NNh9rbg1n22HzmzDQC7-oXR8rnlYH7DO_-xKSyQdsah9UD890Swb21lZC0JHOHyAd-wZMbWkTO96WReV3tu_WHc3XYLsFxtAadec1XxDP83CqdTUyDQW_6Ew3WO9DB4b1gxvFcGLj4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=TIjb6FNGcg-PNv7pcgwR5q527FLIxhK1ZvQNTt-pOvje6r0I2aNKfX46XgfI3jEyW5hYiYNwAkiSq3c_630JvAQd_PRUCUchIFZpz1k-90Dh6UoEK3aiNjK3_x9nGrIs_2YEo_MUDJKd6BMjCaBMeEpNfd5d7VpnAnkfdBWiLOv_7r3vT-bhppdKFkpjlFXHDd9Bkuz3XoPCsbvGedKQddaWMVfB_XyeDfxta-YKA0_AsCvQV7l-IHkp4s17uBe8R4LH8oy1xHzLVdVjOvdbGVAscnp_PT7weJl8IBvnO8fkIcUI7tekcNLhmszIPwNIMFPczlz-f4X5j4S934rApUO1iohXRoBII7l6514-NSA1Cczm1scg0HG7w_j5A0uw_dO9Z4GJrCJn4xUqpS5j1CQjiyikI8G0HzH8ZlKoGCo6umzmFofh0F0468wh6qkjDuCyHBmxFNpKqgGx0MRz2DkivQ3zL5z_XSI0lxYT2AksCu3x0c1qXruok8tbMs0MSpy0Y1BZ7aMtH3K2_TlDDFR0_H_oIZQt_NNh9rbg1n22HzmzDQC7-oXR8rnlYH7DO_-xKSyQdsah9UD890Swb21lZC0JHOHyAd-wZMbWkTO96WReV3tu_WHc3XYLsFxtAadec1XxDP83CqdTUyDQW_6Ew3WO9DB4b1gxvFcGLj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rFRF5x_mP-EszMrV5wXUgsrcknWy8wODVDQZxrFrdHwt-o6RciUzWKimBTXkzJtm0j64gKITwh6f5Q8q7KVSLi8M4TUx6XNv1pNuQxgFAd8UsT-nKkO9fwQIu-dOl1_aLpm7uJIaAsOhpE7rIMUQhveBl_gbwC-UMcsiD9v7YmD5mWG0eRBmE_3SuEVdPovYj5ARY-Zn-0qq7-CchD-V3DBmehj17Wqcmv5MUtD4bRi8k2z2lZl0qjWDjtmbatsRfoG-Rqco-6APW0iyBCsIoLT8E_yof7W-FrefTl4eSC8sD_mCYv9zOwx-weCJQtaSwvv4cHS4fA-Z6cXcylh_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OyiC65ryVI7qQaVhuvxbe_YQhcyhhKCZatD5280LEsTjArMrvWuyBhmeHxiaGpRbZq5e5MTKPDZBKzcnpQic5nG_ONhxNcPoLK9LaDIjK-RICkCpOFH7-ReTJPAyotJCe3IIq5grXHWkhhPC7MIBRAv53-BkoYJsKLUB5TUS1VFM0Elsh3YscXI0eSgLV6AU-0KmkKjJCdGuf3Tj11j_T5a3xeGxJw-VY6oJXVEzH-vk4ZwfnEX2NBJ3VAPMLCLrDybD3CeqR4STQSWU8VURJzPUT-LAqocVjL2ZYaAnPDMjDM2JaG3F-ASV0u5vBE0Xr-MzZNMOqbv6nmSFC6lDaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، روز سه‌شنبه هفتم مهر در گفتگو با شبکه فاکس‌نیوز گفت رژیم ایران پولی را که به دستش می‌رسد خرج مردم نمی‌کند، بلکه آن را صرف ساخت تسلیحات و صدور انقلاب می‌کند.
او با اشاره به عملکرد تهران طی سه دهه گذشته افزود: «مسئله صرفا تحمیل هزینه‌های اقتصادی بر این رژیم نیست. پای هر دلاری که ایران در اختیار دارد در میان است. آنچه آن‌ها در ۳۰ سال گذشته انجام داده‌اند این است که هر زمان پولی به دستشان رسیده، چه در چارچوب رفع تحریم‌ها در دوره اوباما و چه از مسیر فروش نفت و گاز، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم ایران خرج نکرده‌اند.»
روبیو در ادامه گفت: «آن‌ها این پول را تنها برای دو هدف استفاده می‌کنند: ساخت تسلیحات برای خودشان و صدور انقلاب. آن‌ها این منابع مالی را برای تامین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق به کار می‌گیرند. آن‌ها این پول را برای حمایت مالی از تروریسم و طرح‌های ترور در سراسر جهان خرج می‌کنند و بنابراین هر پنی که به دستشان می‌رسد، پولی است که برای مقاصد این فعالیت‌های مخرب استفاده می‌شود.»
@
VahidOOnLine
مارکو روبیو، در گفتگو با شبکه «فاکس نیوز» با تاکید بر اینکه نباید ایران را با حکومت فعلی آن یکی دانست، گفت: «مردم اغلب این اشتباه را می‌کنند که ایران را معادل یک کشور عادی می‌دانند. بله، ایران یک کشور است، اما مشکل ما کشور ایران نیست؛ مشکل، انقلاب و سیستمی است که بر آن کشور حکومت می‌کند.»
او با اشاره به مقامات جمهوری اسلامی که با پوشش‌های دیپلماتیک در رسانه‌ها ظاهر می‌شوند، افزود: «کسانی که در ایران تصمیم‌گیرنده هستند، روحانیون تندرویی با دیدگاه‌های آخرالزمانی‌اند که باور دارند رسالت دینی‌شان رقم زدن روزهای پایانی جهان است.»
روبیو همچنین هشدار داد که دستیابی چنین رژیمی به سلاح هسته‌ای، یک خطر غیرقابل‌قبول برای جهان خواهد بود، چرا که از آن برای باج‌گیری و کشتار استفاده خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jAXC3k-kcXYAQ4M_pWt52dFqwAl6EU5HWG0BnUD8toOZfNwaHMwhVbVXx5V5f1WimgU55ao-kVc0ewN2PheATAInp1SFZsBYP9ItWnyesJMdHYBcoPrrcz7qomhYYpX3ngiU3LxPLS0qTbjCjwZwktKtRiaFKJAePOOP5QolbtLn65YKujRc73envznKFDZ18ZsBlcijMc2YMkzlzkIonn5lOzv2GdtrZyR9q70PqsNbqulhUXDrdCQSxPVFaievSRqULBF4PvZYhVH2YyzSGC_2TZXcQ5YWwyNkciyO3Rmu7ROgtJyUpruEU4WLTHg5J7w3MPT5lYaHRE7CKKqmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=ITJ3sGymp__QdV8SioXjl_vxPYKJs9NJuMupabzI11TKJOtQ0R6_D2szOy3LiSQd9pBpkalRdE1DmaTxcRsKpS-8JL_IWODVkz0e9LQHDRqJaESZDJe99BHC9Cb7U6pMnrEfaBaUh6B5NC4YhuHGIRuJ-4YOv-HRzV6nKlRkalF6ACbaL2mDIftFWwmcCHvC-aYrivFkPjG6HMKGhcDOJU8U_Yr-bnzURemaFMicrquf0WM7oRIvePUYPCTXLoyFIXGzEBIi2X7r_2ursFPm28e3QxXvE3MYoZklzvlREPPpmGi8CvnCJ1pWTGpv_-YgfxdNUEm3UYab5NV8DhIu4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=ITJ3sGymp__QdV8SioXjl_vxPYKJs9NJuMupabzI11TKJOtQ0R6_D2szOy3LiSQd9pBpkalRdE1DmaTxcRsKpS-8JL_IWODVkz0e9LQHDRqJaESZDJe99BHC9Cb7U6pMnrEfaBaUh6B5NC4YhuHGIRuJ-4YOv-HRzV6nKlRkalF6ACbaL2mDIftFWwmcCHvC-aYrivFkPjG6HMKGhcDOJU8U_Yr-bnzURemaFMicrquf0WM7oRIvePUYPCTXLoyFIXGzEBIi2X7r_2ursFPm28e3QxXvE3MYoZklzvlREPPpmGi8CvnCJ1pWTGpv_-YgfxdNUEm3UYab5NV8DhIu4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=seJyuHyyQ-e9jaxxxtxmu11dY_xu1yf-VeQMPt9pZzS72EjYld60JUIml0s9zYuzjDYIHFEBdUDcss5uxUvmONUKpGp54erDx_2-J-X-xshaYo4c1-4DkcAUepuZA5K3xDpzB_126ijKdYDG7X_0CPDzfsE5W6cK_TZIW5NwJuuORU7Ws9ooEBXxlh9vpPu6VGAjXdvEZuJaG8h7ckEpOLKTJojTCpsinObQVr9t2L9yr3B5HI5zmqzXjB48n0DP5uhkI7cIGzb53EFbX0eo0SLogaPyyXYAuWOGySUp4bTJ0lnPfieFp-RANT7UYmQrI6WVCODjLFJywFYMGkvgMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=seJyuHyyQ-e9jaxxxtxmu11dY_xu1yf-VeQMPt9pZzS72EjYld60JUIml0s9zYuzjDYIHFEBdUDcss5uxUvmONUKpGp54erDx_2-J-X-xshaYo4c1-4DkcAUepuZA5K3xDpzB_126ijKdYDG7X_0CPDzfsE5W6cK_TZIW5NwJuuORU7Ws9ooEBXxlh9vpPu6VGAjXdvEZuJaG8h7ckEpOLKTJojTCpsinObQVr9t2L9yr3B5HI5zmqzXjB48n0DP5uhkI7cIGzb53EFbX0eo0SLogaPyyXYAuWOGySUp4bTJ0lnPfieFp-RANT7UYmQrI6WVCODjLFJywFYMGkvgMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvAfE8H9VGj0RQ_FWtI82B9_xvtdDA1FuJeFJw44k0Uoq52ggxVnZ5v3PsirRUfbB68k90T4BKtpzg-cItre90SS60jb8GbVk7XhXOE5R8Un4FWK6-BMjpQLAuj69cLr4MU7ljwiRWqJYeHgyi_FRUiFu_ytjuuBudlWJNV3iRLUtgpoadH52bTGW6LgThubtX_1YrHBeOnX3mb1aDojLtCrUinZogy7G5Rgyn0v41QWcOdx1I9s-Uju1eDCTj_gHkht3db8HPGl_bJMJ5o93fgEn_Ok7wZOGXg73GsLIqlFfTKmyKg49y-vrIfVE2f0bmPIreR_9W3KxP3CL87fyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G2FncpkCEn3h5OfyAabPIXey4lVov0GgYGdKA2Q7Fgz0kr_hwaEBimMScYczjys4VShoTLYqGWVjCg2NYFx16N2gQ_iXReZmt0EN7ud8Yd5NkBeh6_OhTCljAi41548SnzooCkP94Eik4uVU9fcHuqS2fR9RNB-UTeKlcIp6ohg4nn8lyHC-OwyEJahX_yLpROKfOAQRfBX3D9Blnwoojed6Rzq9e_YIpD27BoRWPNWPBzYhM4_CMXN_9xypDgUbPleZYxkxPg9EnWec59PtprG2iOO5jWacstdJ8QaKf6MZB78ahq_B2NtT1FiIZ7OlTmovuCeFEurpP5GhmZ5dEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3ipXk1Z6-GT-gGkM2QNl1Av4-WPUybXmmxSqHsPDUfGI-XT8q2RdgBvtIzOoMeV-LI3uzbJJWRAge85KXyd4i2dggyY9qd_rTLacUxs5Bh27qDpV1j6TZPl554jFTsjHx3DMvXOfoALaEvz2tbZ77kZjbGuBwGvamjgndLMyTTgthipqqMMSuB9_AOgIyjSlXyYilzdvUnFIErZBztqxrOmAOqrRp4NIaDedJVp5knxarEsyzS2SR0op3-sUSfZaw_sJ6oNbgQhTHyuidBSHnWsGgWhSsWwjJdarwIWmv8yG-pnWkpTqPqfK6lZl2BmKp6lvo8RcIDwZQbJos5GgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=LUfFRXSTTqHPEHuGHJrP2aZgNe8ZfHH1VNOPEBJyjCgj2GEq8ZnLPQhVM3CtqJJOdIly_i3NjW4yOhbgGp5p66MrIDGqu9kI3gDhJKmYtxUI9cnn9l2sBFaEH1K50kQDum8O_jouleFFtwxgWHmAeolzP1E8yH4zBX1zRyMpl1i3U-npfCk3rhhmg4JEuidJnrxXNSkMAW2vCpGyCj09wDP1uA_aIHKtAFYQJ3LbLTV2eCRqTU80JWblJLQvrlOgthIfRLBgCML8pTbcq8spvCSGMjQ4RxPmnlKeUDF2eKWvL6O1RzgLUoCPJOClGgpl_4Ef-Q9welBezgPvXKZXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=LUfFRXSTTqHPEHuGHJrP2aZgNe8ZfHH1VNOPEBJyjCgj2GEq8ZnLPQhVM3CtqJJOdIly_i3NjW4yOhbgGp5p66MrIDGqu9kI3gDhJKmYtxUI9cnn9l2sBFaEH1K50kQDum8O_jouleFFtwxgWHmAeolzP1E8yH4zBX1zRyMpl1i3U-npfCk3rhhmg4JEuidJnrxXNSkMAW2vCpGyCj09wDP1uA_aIHKtAFYQJ3LbLTV2eCRqTU80JWblJLQvrlOgthIfRLBgCML8pTbcq8spvCSGMjQ4RxPmnlKeUDF2eKWvL6O1RzgLUoCPJOClGgpl_4Ef-Q9welBezgPvXKZXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJFirOe3DqgXlEMQJwTnddTSje1fgBtCHakWJV4jrfeYntN41FCxpGk-AFsbQTZelmWjIQxW2QDLk-EkAdKIQJc_cYbj2Mc91LEXUfW7LwI1MG5K8WPm8rTdx_J1MI2ALTHlVQ_dNu5BMLPjfQ6TbN6P21-aCSj6CYYCTZykS_RHdo_7zigjmNkpbekLhRCF7IBRd6pY-x66pdiMr31CNTHr6rfWHHsa8uPjbFoKyZff9CEP27okIpUxn_wCITvCklm33T05BG2lEOMgUcrR2wcArhabhv4ykVHAEDx1QazRF8flktHbJ8ipyy-uSaYFuoJRI0BlG-8pGdP54yczrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bGeMlq1tbMZpJjo0H76wdBNZmQ3YD-0pJA73a6tPuMMZBSTQRgPK8C9QEWVptaWv3LQpvMo7O52i08vg-CVewYfPb03LRZd0vCFXEsnfBlc6ozUEvrv71eC56VnSSjIe-7LD061xBJ9qpj1SZRoGNvZ-a6H-k0MJchqDzhfJ28WVYM8tgHaGYbgD8VG22n9MZ5GN6cNM4O1osZlbwMPX8mUTQD8brcjnK6qqW4LY0LwQRThLW81sFQZ488wn1gdoUQ39wT3Qy5N7NC_SHRcDzctA3p2XbkHimyZK_0oEySXbqI8S5U7F0m9rdZqd1e0llkDKc_4aiudEH6tqeylDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZTpmFqto5OS_kKbqk8N8R2WfPx6KE7ymMkmOD64urWu2kEPy2Fgwt6jHsLHznyC62-a8rFYpU64X7AU5grJzx_Ioinv8HZALyVxIA3TFBw9At_w7KqQDR0L-nhf6MHwk8L0_wHc3sUXHcUT4PQj_7v1rHqwZxXytt7UWP3MT_1JulIwawAYQiITsefYQe9CwJur0dEtxe3PTA8qPrCofiQw2Aya9kMFGiE5TfiODqMCgWOALCb325IaFPrIlXg_29iNWQZ2NQI0g21ACtqAjTY6RAVCN4eR2VV3TtnqBKda_QfVyaB6tlEKcsTBUzm4JHcmNwrd1y4HilRf0HQgSpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=e_e2F6KAOEh61vZMx0Jc2TRsP7dPnIpfEr9nzNQG6AIX5_YOf8irPpdzfLi87V_kM9lZZ49dAFdxoKFwcuFl082S_E_S3ACSae72BdJTovyb02pejIerrRTO1HbpvHpqTELTOqKKogNhTieR-4wwXoa_hqrp3V89_o9mADmti_usZgjq0pbfpssFhCAAWZ0DbD09gb3Wv0C3KNPnneDZr8AXOV2siXRb5Rvvvvq7C6jdv1PYEEq5qpx2cSuR4KpvLr-5Ig3yv_YmkqWDmDBEJPYtmDumRiBv7jTSMmtAjqQ4QseJRwOqi4jmeCH3ir6IHX_4nJqEK3K6f_YsKNmhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=e_e2F6KAOEh61vZMx0Jc2TRsP7dPnIpfEr9nzNQG6AIX5_YOf8irPpdzfLi87V_kM9lZZ49dAFdxoKFwcuFl082S_E_S3ACSae72BdJTovyb02pejIerrRTO1HbpvHpqTELTOqKKogNhTieR-4wwXoa_hqrp3V89_o9mADmti_usZgjq0pbfpssFhCAAWZ0DbD09gb3Wv0C3KNPnneDZr8AXOV2siXRb5Rvvvvq7C6jdv1PYEEq5qpx2cSuR4KpvLr-5Ig3yv_YmkqWDmDBEJPYtmDumRiBv7jTSMmtAjqQ4QseJRwOqi4jmeCH3ir6IHX_4nJqEK3K6f_YsKNmhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOU85KpXy4LlZ9JQ2mWTzvHCz4yNLkKu8OjXXsyQOMEGFMGHMbnFag-OJn2sPx1KNCHHXcdWP9oNCSVar1xR_ZAEP3WqmYuJK99ThrbigTsV-oLiXCIBa3dmYbRPwT06DudQ_ba3WgYBaAX34UqaMpfmpWy3sb_42GE1mOBxNouSLbfczCqzq00f814C16fqYTwDonDzikC69ckKbD7auVv6-U_tMnjmGxJ56HDUKtfRxq3YJb-ESgEruePRYQi0Lm71PlGtAil41BjFCmwaOyHAgDKT8s7theE-tTvVlReHyNHyO308zxohXMIjiS6zimZSZBPjcBr2NRWU_hFYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nH2ODt0kgFwHcDWkgN-ZrqRRETZCOa4c9pDaRYpPCudZpN-vSWMaEhguY5oxv_BdNGHnZWbDSfuMI6pUNjbR-a8YDUA4-u6nDv72VqosHq8TDx-L50dS8ZGzvSJqXIN9jhT85l_DkneR2rz1xtJVOMQk1saMzY9zomh1fMpfyBKGIK7aZjuOlmwPNTqtEJY2AoSi_xBUpMwdETTDa3LpNQlIp32LauWAs80YgW3PwUpj5LPaWhl6I1Q-ejWyQPTdmCDG6kEmbtqpc2qcdJ84i0aS1qEzPFyEUpWOKBpIw-3Doy16oqJvPQOkuMoUOh8stSlhqZnxEx2E2SGJaJmHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pOpsWLsQWaalVcEJFz7nwJwL7Kl-5LYTZhrcnhVknK6Za5rzlVNAomxD2A8yurl4FsqRVRds4j-L9yZNoauOyApugLkhfGw_LF8N6kGjN6QSRSpLdEkCucIaD23aDJ8zjCG9D1C3TqL3elYKvuZa644pH46RV6deDBMt2xnhyUDaxTUxURc9cbPnMgxVDtenorPUMfJyVwdRK51HMF-ny8OzlUDHl7RX51BUzoEsZ4ZDtjuD3kkFyH7BHNJGpS3hWZw6XT9ayOV_i9-apDKd2DY64PvgXX2FhKLw8ZsBw_0cwkTIqJ1BiXV0vaYWTZ0TykIJt1L_8g0qPXLRLZdYtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7dV-jZdv1Uys8GaoRMYcyJW2bv2oZuoMDkz8PB7FQUeRKoT_dV-8sHgIakLNwQizXFzVoDvhLbl9QibSNaTMZTnIL1YujMLijF8eh-CZwHW9Dc0NBGr5D1Q5stJN-Uqm8xRB5XkUlTd7oLnMq1Nsi9Vp4rmaIlSt5auYPAGUV8qOXOF0tQtLaA3fC8igTC69G8xr0WWKk2CGRgHZAaF6L_Hr8EyHOCpo0JqrE5PKJkue1_58GKnUaMkW7GE9eY61kbQgRf25X1Mx9OysG0KX8Qxk-ibadw4E49urErQcWvrLZn20-wMfIPBEbo0UcEfBK2aMYnEA34w9CIQYG0AhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE3hiTVDlB_1ica6kvHFN0DQpEs2eKM6iyIUQZzIlYpJwXxvpG1cfv-tvi0zJXDYmfpfAW-7tQzBw3p7K9pzmfkDQZUzKkrhvUtfaLkPfssqSPl_P4CgCaS3AePTLRzRJHsXzwkdQAiP_JZ2yHdVb8Ms1buUZp-ckHBTEnfnjH5EgENH0JS5_6PgDrP7C5fV_wpqjC15QDTTu1F89p0XsXjgEHX2WAM-UBj9y98YnOqZtVLLpjsMVQfVU5-f0-M2Vj3ao8tANxNQ1nlvFlltgqOecndHVIssd5u1mZYqI4TysnDsDP5Ioy8lJmAcbYVHI-fSLgV-PqlymQpFrlQTnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=QIg6YnGubGxyNW_sj4-ZYFdqBXoeFZEHBoTW6PH7Pyy6JfOyF-dcug4vsVO_Dl5fRGXIZNOUEeJyxdUv4TMhm3l7yWCvnh-p2CynJDitq7-2ZDMzDfhySw4zKtjpuisyIO3KgZ5PoGuwl9Lp083gWFODxIHqi0UV6Lk7cMdpXsFMZ7QjHw8-Bk0ACRKGZihZn4kfxuchMgslmyHUJjIZgFfV1ZrC1tdhKST6d86Y2au6oUK4ZdbqeR_GC_gRaI_lgQT6cvwuWdDy1KOvKbJzz4bBDFKDfS7dEH8SiC8kGH7DjDri8bX-ec-jZqJllAdkH5qkG46mz5_in3wGYoV6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=QIg6YnGubGxyNW_sj4-ZYFdqBXoeFZEHBoTW6PH7Pyy6JfOyF-dcug4vsVO_Dl5fRGXIZNOUEeJyxdUv4TMhm3l7yWCvnh-p2CynJDitq7-2ZDMzDfhySw4zKtjpuisyIO3KgZ5PoGuwl9Lp083gWFODxIHqi0UV6Lk7cMdpXsFMZ7QjHw8-Bk0ACRKGZihZn4kfxuchMgslmyHUJjIZgFfV1ZrC1tdhKST6d86Y2au6oUK4ZdbqeR_GC_gRaI_lgQT6cvwuWdDy1KOvKbJzz4bBDFKDfS7dEH8SiC8kGH7DjDri8bX-ec-jZqJllAdkH5qkG46mz5_in3wGYoV6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNAGNej3mqxzRERH3PFkdNILesErYv_xZxOAL2w2YKWQbNZs2gaEZpPv9hNbgJpHnx6oJL0G7VUJt2G8JmN64mHm4mE2Xpj2f3h5khtDMDqjmHMIJ3Tor2mOf9g0FjowA5i8x6WhW0Xl_WnjTslY4L09hYCut4dLwoXy0tqSCGVLx3soAD_yjH-12WtCw5Xrto9LZvoCklmW8l7pw89gp1SdceJzCFlx0Zs2hx_4UHn4d16ST8EYA6HSrtWLKy9XzZyynxNgNlPA5-GLZsbPMbPRlsGsvTQuMwatZDDYja6XsHPD45TN76aDqyk1ZqAo_w0IyeA5u0hVOmnBSc4Itg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=lM3vEcjGRiFLJCAuR0C6mfIgpdNkvEqxFsXATH9aYCGZPBYgH0irQ_goMvW-Gu_gOtehVDnvakjRcRHvEdSrwk3MV0En8Jd69lpVzw0eAxQ0nFSVvh44sfx0EklZXvSc2eVM4iwzf4KGl9t1sC3UsVMtkeUhYjoPnHuPBYyDJ2ohrbcCOCsR-FJB5ZF3lDeJBH_NUCQ523RIyJ3jHPU33rV9nOFYk-5EFVO4samTLuOgs3-C0XC6O3paSKS3BZQckt4HtQv_AJN9LzbrSEzh_kULtmhhuneF0XsftfAgDoRLE7Wk_V9ZchMOI3qOFJQ2POo0uHakYdwz59Dsm3VZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=lM3vEcjGRiFLJCAuR0C6mfIgpdNkvEqxFsXATH9aYCGZPBYgH0irQ_goMvW-Gu_gOtehVDnvakjRcRHvEdSrwk3MV0En8Jd69lpVzw0eAxQ0nFSVvh44sfx0EklZXvSc2eVM4iwzf4KGl9t1sC3UsVMtkeUhYjoPnHuPBYyDJ2ohrbcCOCsR-FJB5ZF3lDeJBH_NUCQ523RIyJ3jHPU33rV9nOFYk-5EFVO4samTLuOgs3-C0XC6O3paSKS3BZQckt4HtQv_AJN9LzbrSEzh_kULtmhhuneF0XsftfAgDoRLE7Wk_V9ZchMOI3qOFJQ2POo0uHakYdwz59Dsm3VZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhOi4WYhzNl6Lp6ByEo5QwO65mZfdJwuqeugT8WFlfEwu71wAPz-6iL5E8qhE-Ph3SoiMwbqJqoUdbOPIZs8C81nPKvgO98nC9jJS8BWJxiL-Sk8CO0Kaxkxjxliqr0EB98Wz7VSoCkbb3hD-PvwfBs7WjSBJYAZjtsY0dKGFLBXuTWXnkKvJ2cZxor9Mlyhau-T3vtm6pqC-Q31gZKCSkXxZ03m-C69AHStCjvm9ecINRjCOnHHBEFlIh230CBfyI56YLaRnwDS8F5ipbsttdmPUWnF8rUoI5RQ8aw0RT9K7Y111LxydPkKNJzSb3qHuOnc5kn5A-haCdavHkTN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mjnn7ACycdNQN55wKBZfHHwfmDQKgebJ0pQWCPRa5TLbv-nEugTslVvxlNYjRO1ixt5b5tDN7ySCSl9OamZdFzL6THr4dF7JSI4zIxYxaLm3zvSmfsA6Db0KanACyyfjMQKeKX6kjH7S9vYGrX57z9y5uo8_9Vk8Jcdy_07bMXzJt8epMo6DGm1-zE7gXzM7ea24re5qtsFhqzLqA46aKqIXHTKr1htTh8lu3992HV9zShNNwoFBicNYgJVVTGknGw7txy10z0E1hLXmqEhcE6YEaWXN7bLCR6J-qopVlRYOfdTcCrVlMk7DLjOMeZkYvF12LsVfOhTAORMwfNRGcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GXbzPrUtLD7NT7A7kRJJolbxpiBIKKLSQLqj6FWAohlUDG-nOtkbjUXFuuM2Fba80p0l2CaKz2qzzqNTVV0pKSFLspih7EteBLKXogPPWHoQoXdHTUJ4tanSMDlHt-iCW_T1T4iEyyN0b-dhi5Z1teFk9P6qtQqkyw7bM3fM2fW1dLd7eTPTAQvu7Vppfm2dm7Aqzh11Va55eEfE79Sst6Vvj_aD1Fr0vDq0Nr5yhuRL_5i8iU5wtfsaqkn32q4TKDtzjEg10wQJ_g7VT-Cgo0fNxJy8M8OgVRcash5DOTbwGMAU5pvfsB5HyMJwYIvo8kpUOflXgMJUi1xCDblIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=RnxHBp1779NXF_kKKIOdG0e__jRYXf2fuvNb6_jAg8JLsTm21WSJ1gbzezXcftksLyKTulg3j3RlcRtB3U28HYOlgyqstuLbyxzO-B-QxzQzrQLif87iI1yAVf4XsK9iSt8rD5R8psCzbWd5qkSWkfB7L9dvLEiQFyLygxFnPlSMlemqLKUZVMc4BlJ55bUsOCHpkX9JGwe5yfSDpjx8mRzX_dLP-Z1TpLXRidMrsNfIVI6VjzyjV_pO3UA41d3jkwTnBWTUQgLFio00_U4fP6CtMdYaSEkPDlVb595Lms7jDGyLNHq3Uswkr8zefJZ8OgO3TWYqWJippEdSQNR2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=RnxHBp1779NXF_kKKIOdG0e__jRYXf2fuvNb6_jAg8JLsTm21WSJ1gbzezXcftksLyKTulg3j3RlcRtB3U28HYOlgyqstuLbyxzO-B-QxzQzrQLif87iI1yAVf4XsK9iSt8rD5R8psCzbWd5qkSWkfB7L9dvLEiQFyLygxFnPlSMlemqLKUZVMc4BlJ55bUsOCHpkX9JGwe5yfSDpjx8mRzX_dLP-Z1TpLXRidMrsNfIVI6VjzyjV_pO3UA41d3jkwTnBWTUQgLFio00_U4fP6CtMdYaSEkPDlVb595Lms7jDGyLNHq3Uswkr8zefJZ8OgO3TWYqWJippEdSQNR2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmijyIL4GxI8MqLP5pSJoZgpqYzJpXy-8t_i67yGnkuOavEo7nAaAXUcaATW0vOIs5yTMTBHWhh5VWgkbYDYQr68KvA7k_Y59Aq7FDCEQjnKVhcpgKE-e5XWrLWRGzq9c9T_5uI8ZlvbQnXDNE0IhSlaNbQ8ztySQzAZ42LtxN8t2nb3GDfJE8gdzHERX_Rlec5KTrgNbGKcX_DP9sQCL0BKt7zi4teQcV6BFDVEF0kD_3fCsOTLoaWUvt0KYr7UykmWQa771Q-wT-z5p3ijB2cRoCPhJw-193-lkM3R4er0a419G0ZxvQXaWfz_AdHLw7H6O5UB9KckTgqho7NjdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uAonZwxcGuhGBJSveq5XL48LGwgH-Tv8n09sgXIWxYlNFnwXPnkIdLBtB7IWUoXg-vbSOCLVCj-4pUym4loVguzdyDgmzu6RXlYSPbPHLvFrms1Pbgt07ei0dHy-FBXcr7V9pnit0CTutt-eUV2EhG5UThuU2tpev6bCTADlC5dlELdzeON-Yxz1cPL0J8_P7F1m2IJuxCL8uZNh0vAnehz8Rpx6P6ZLDul6KktvRrTSRtYNNLRq_qlMg_viQMPaAlGqOosKu5WlI5hFGnfLAdn-n7XojPWMHQkWSKk0vF1jcylFrZCbp3XxEuOCXz_86pZGIs0OnUsjgzbqTC_txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge5KzQziT1syF4cxJK9u6i3LVL5QAjc7ZLkB3Sqm8POoWVjNbrrqrRpzVmAUotM_vYlXAwomcaxQ1zNrN5OPp6UdLj2URunvsJklZZu2as6zefLJxVcCxvSieopuch7eejBXUuO9xn1op5nRRjSUkL_rnzqFAXrXTzIl6Nx3PVSFdJ-xhSuFffzxu1oM_0KG1t9FdscJiH2i1dIxledkT9UU4JJiFbvDVTm-u-bvQNM2jh7tkSD7vTIwCE3h-IrDIMxV8Lasrl68iF0ypsbvM7rPJ6HX892hjmqFwsE3xmupSONLq0iptOBATQKmX3RfhnjW7ddEWzuSYGNAUJDbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGyL5bZG1QIJNItsXlJ_1i-WoIuD7zt5pxuPoisRBlZfoFSirrV9dd2HkebE4KIko4iMZKGh3SdEIBlzkfvT6SC7Gl4yyEbYr1LpvtenJWXkFnx2YW3sx8yCo9Q3YYVTKB4Cu0nxKMCvaYiFlNZ9ftO5rCw9mfICeM-7PW1e9srJOeX2T6cTiUtoA3XnHu5c9N90XnHBj6g1vquTrMuunMcND6E6ZDbvLXe_UxUjOCaAImO_as4x-qoCQz5opei22JvOU5pq5sQdkui0SSfkXaQxWrYjFuSxkN4NG-5AT5D5aOBYnkEQ9yzTNCVwx8jgzqLBqrvzyHhyRQx9SaZt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZaXPOYZ2S1MLtRrPfynMG31NIkJ-zeaXqQx2lO88B8Sx-E4Kdy-KIP4WaqorfIMdpFyeqUBgDTpbttAyssf3DL5uWGp1pkVgP9UNxxIcC0kJt82bE3CQ8Yjn6t3_GnxVUz4Q3C8GjRGKKfZv6PmPCxE8u6EoJuz0CO5kOjk5G2cVyFOLv13FNatTBvXt3kgV7zB3x0pnRBRzyxpnWmmzIx9x1-fj8IY6rRVeeqDe0r_28ZYcX8PAgylUUatlVhM3blPqM8SQrfLChd1zXV3y1EAmVcOLyWyly4Ns8B3HYrmd6VI2pcT6YRsF5BG99ZIpjsLUJaPTYVMhPOsjvQ6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0KjtOL5g0En9DVG5F1JJgUqR4T1HLUxIhWZU2eMDsVd70U_2AJZBGUrDZ5G6P6q-efkNT6BrxNgHC-1Qh4fG8XtXJ0Kfmc3vIUrTa6CWyNRDBvkbbpmRVDG1k33hcLlFPq68aKe_G9WY-XmlVTBEgnZqEr1Tl8tL51k_KHIJqXLOhxxx4uFjT6mC0ySF4T9IljWSeb_6-CwAAcv2DY-TAFTd0Cla94vIoG9Zi-f98BMHQaoP0Jj2fC6rWqZN_Bo1ipQ9tLcYh7fq40u7FiHyP10IgBvDiqLwVvubI_r6hZSI_I95XILWeMkRJMsBQHMiyoyMqNt4mbB6OVWATY9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwghPJz0tuowboR2J04xnoWZvT0KZLomXkB3I_5eV03zLoO2Mm90h7HjFDb4Q4u9I_xLjRQpToBOFgyHdceduoc-pgtrsX3CouwTv9B4ueK7RRDFoSIUgwWVX7-WpTJlamWSh2aLQ0hxopNv-AvsD2f82XOJnz5xMtxog_9GrGbVnc34BKTQ0gr0ugq8cDJCG5kEYwBzHeQ6ySnnh0h009L1DIv-jld3uLOvBB1yA0SQVod5fTCghzBBPmf1WhoDB1ewSDoJgOcG3sbsZ2tXgA365yjquXERQm1txnyZlQPkoZnQU9zfL2i-Crf7Wymoz1Pex2iZ8IfFUTPw2YfoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0y2nD-7CCBTyg3vvy0q3gOHQXK44F4gtCTcyd1nNOq6ZkNHWeDh_ZrapnLE2Af_BGqV_qOgb6oBdRMqr7ERka9w7bjE3AHLvoYvikp4nkf37wFHSFLc9kpfYQq8bp9V7NzZF7i76SrRXCCWwGROjcPFgzweEebZZJlLirjuU11_0YXlwT1gBObI0bUW1M-VTdjT_ZjkwLmy4mCEreiaSm_lTrycWKXHd_X-Tiy0J6GYl7n_lF6cEO9q7AYYOGSBNB0o-kmqSY_cqIn-YUXOTd6R1eIommcMqrLCv6ORbEN-1heyyqIPLq5bsxj2NL1uksfGN_LjvuADuB4H_Z_CRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9RZ_mv_rCN3iN9mRg6pN9mYG5hYsNwxcNApzP2ow4HiMqZQ8iAm57XGzFLMeJcsOKqHV3aA4Ut2l4ISzcB7y7A0KI1XxfTFIhVxG1J0zwK_NL3zgXZ7i7icc7e9Z1MzbVmr18ZsbThSnpboYNS8SLosEndiNZF1zrl2Bh9fyLGYDIwUWg4vPlatzqNuSXK1Qul-xHGY5SuRjIif-raxtIAiNzfCpTdWsDdLLasaqmV5YoV75PoMTYX3mwtYCq8T4V3Qk9grdhUYAbwDF1ayOeG0kk8igmOBwhRKrsjJKZ7_fpHVRPrmVWaBhd4FO_LuGLWgY9jCqY_3izO6PGPS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0qQS5XhEyxEq3JO_trtoNbPqJLB-tebXp_Bx8zgOi4A2ecgu3xgo_3X2MmNSiX0-AaxUKpQ28B8MR959oRgrmyqFoz7jIxsnnraw3ufZuWnSqjEvogh-2N1IVr-rys3EKJNM35zqOuge83LKRJ-fGkEcY2fSezq9ZzF-urQ4me_K7_xyAV5dI2rkW6g87shKZFuEGHD04e3f6zZAXmr0x4O3-c4RHWDx-fHTW_LoZp7g0A-g4Z0_qo63NyxPCJyZ46qlSCgB47uYCWcec0gvRfnreNa6691vGEMsMHWJdhjXux9F15fBD29_xL7ACQ6m-tic1swmJ7HtA-NMNY92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=pQCr3gyLZEEGVS5sJwLtyV10WgP0YLUpX-hzjSrpjrQOnfWFiaehpxADItNrXtm3w3bh7CZb9820GsxDiiJW9RcFWNEeNOsEeJJEeocT4lyGbW6D6RKMa0YcVHgfmIEEIY5aiNfv5vTc4X2_xKyhSYbOtm5bBZAFNV8NTYaxYuUnhL5Z76Ntbs0j1I5C2zk1FoLw9Bu7vgwwiEi6dgoPDC4Smvkw_aOv7AWLZwT9hnS2L6LUHuTpQFbAJqBK1wdw8ZS76hXN49USBsahuveJBWE13FAaMbNATY5aZtAGZs989hWiU8emmWTcilVMDdohEKRpX1_yzgBaBYqvKwOhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=pQCr3gyLZEEGVS5sJwLtyV10WgP0YLUpX-hzjSrpjrQOnfWFiaehpxADItNrXtm3w3bh7CZb9820GsxDiiJW9RcFWNEeNOsEeJJEeocT4lyGbW6D6RKMa0YcVHgfmIEEIY5aiNfv5vTc4X2_xKyhSYbOtm5bBZAFNV8NTYaxYuUnhL5Z76Ntbs0j1I5C2zk1FoLw9Bu7vgwwiEi6dgoPDC4Smvkw_aOv7AWLZwT9hnS2L6LUHuTpQFbAJqBK1wdw8ZS76hXN49USBsahuveJBWE13FAaMbNATY5aZtAGZs989hWiU8emmWTcilVMDdohEKRpX1_yzgBaBYqvKwOhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvU1vTV-zb2zme-0dyGdnnt1cHP0n6dJuTfobkImOz7PDYbx0lGNkCZZOBZ3hwXPV-LSd70wzfHYQXawFh-8ZXpkKn34T2TwlSOcnolgtsGg3irDxEYD_TmXkJ6_QLBYuDeI72syyFRrlRcb44DJIyjdKuf80-nj8Cc9PPH21pAUiHUC9wqlIpjAQ-vRaiVVx-SxE7AabtOTuzcdvNt1RQWrwkW7W7TG1Q48BTE4kO7FMYl5O1FHmpjiOKiu9-w4L2J_Q3DG_TMbxq5KbOEs_HCKh1_3a4MMC3T_05WtYzZNDVuSOXo-TPh8zklsrhWaIJIQTtFI0eG0CSra6A_EjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=Q8oefuXlDQD_tJc11tteQVznfvXcciZy-Sl7-zE3v6mT3LsUf_I05sWpw5FsXIJZ74O-xF-4xRnW7CxhuTsr8AJ2ad_8Ze7f3Am7qPrM9bdCH7IrehS6147y4u_HGZHHTQS5h4QM5dS8VnCiPUtKn4Us61Aks-oYt3Ry1sQUOllDiv8dpJGqosqbopt9zvVmQQy-2MwdhU-F2nUUTCeQUZA-G-FcW3cEOoanOKZFTuOC5EeQdajSgShdfzQzu6jeL9ty9vPc3n8ZzjsUCh90EUbgL7kc6uNeOdu70hD_Qd0lllEQSB1gsHEsUoDq92q4Ox32dX7tlzHzcFTlRyV4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=Q8oefuXlDQD_tJc11tteQVznfvXcciZy-Sl7-zE3v6mT3LsUf_I05sWpw5FsXIJZ74O-xF-4xRnW7CxhuTsr8AJ2ad_8Ze7f3Am7qPrM9bdCH7IrehS6147y4u_HGZHHTQS5h4QM5dS8VnCiPUtKn4Us61Aks-oYt3Ry1sQUOllDiv8dpJGqosqbopt9zvVmQQy-2MwdhU-F2nUUTCeQUZA-G-FcW3cEOoanOKZFTuOC5EeQdajSgShdfzQzu6jeL9ty9vPc3n8ZzjsUCh90EUbgL7kc6uNeOdu70hD_Qd0lllEQSB1gsHEsUoDq92q4Ox32dX7tlzHzcFTlRyV4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=dtzMWTy-zHOi_SJ8h7WI5o5H9u-xdgcEBHQA6sf9vmOz2DYM9ToGzOhWsPjWddn38AUOKir21yyLfPzg9KJ8-BKbTA1YO3d6U5v2C7p5IbmwtMCBQAcmwQ2ObWPrqBsYJNoEEpbxSJmLlq2Z2JGBXz5kXesJOq3oLuxtYNsWDXCKUtB19LT7tk9yfmQt0H5631RQKA4_gK34JUCGdTh-mP5JBcTef5s41Afo16e63bH4ZIkJc-cPAbwtGQpTZvB-QkW8vOoE0K9yuzwRyHqWp3AZv4G_IVcRu7lohQEl0Gy2Egg9GUInwDgiTvXN4SOEh8R76t4xoViAF8__AfhWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=dtzMWTy-zHOi_SJ8h7WI5o5H9u-xdgcEBHQA6sf9vmOz2DYM9ToGzOhWsPjWddn38AUOKir21yyLfPzg9KJ8-BKbTA1YO3d6U5v2C7p5IbmwtMCBQAcmwQ2ObWPrqBsYJNoEEpbxSJmLlq2Z2JGBXz5kXesJOq3oLuxtYNsWDXCKUtB19LT7tk9yfmQt0H5631RQKA4_gK34JUCGdTh-mP5JBcTef5s41Afo16e63bH4ZIkJc-cPAbwtGQpTZvB-QkW8vOoE0K9yuzwRyHqWp3AZv4G_IVcRu7lohQEl0Gy2Egg9GUInwDgiTvXN4SOEh8R76t4xoViAF8__AfhWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=ILHEbNWnIR7jDbH55xzWNK1EqH7R81R3UXRFBd6fN0P0iXRxzyXTerGZtQ7MBRjK3uFsiUMzXRcBpI_HX1b-gV__dhDHEkkSsm_iSVxbLahZIm9LU4MZ_AfIYwYL4p5hM6bIiFEm99szK8zfs6Mta6oeueNpFGs2YWn7p6NyWjXyfynmJWs27bksFefOKkd2oP147b4NjmDCK_iVvgVPjW_c3eloXv3wavhjyotD-z4daNdMrOmNrRf4SErj77O16BERGtUBGr0IowGU_nKd7g5Fm39gspPwHVCtnZnw8H-XKF6AQXxNyovb9pAhDUzXnSpXk5KLuJ3E-pvoGV2sG1-Iby8HLKOf-1HHEq60tmYPUADVwlDO3AkiEJcmNeE6g274eQh3VUxZRJkAN80DegCFLUPWT3A5mi5NeelJiTlGpBCezY2w_flCMo_UkJftVqDyLZ4rbu-GDAK5rJuUDJKkSKhF-KngqVY52FdL7XPgoC0Bw47lT6V-y0YpE5yGx7tpNkHW1AZYasO9m9gzjCX6vg54C2eYW551ubxTjvaXTWXjrhhEbsFlw3zkSa_fMpZYw9gznR3NbWY0SGa_sg0FdNy6mTupHlNT9Hi21hEuAJbmMOv0W3ZiXVWSbh7FZLqV8pkNbunWFVgcLJBkDGA9Xl4nzrH-n3xRAUYiNQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=ILHEbNWnIR7jDbH55xzWNK1EqH7R81R3UXRFBd6fN0P0iXRxzyXTerGZtQ7MBRjK3uFsiUMzXRcBpI_HX1b-gV__dhDHEkkSsm_iSVxbLahZIm9LU4MZ_AfIYwYL4p5hM6bIiFEm99szK8zfs6Mta6oeueNpFGs2YWn7p6NyWjXyfynmJWs27bksFefOKkd2oP147b4NjmDCK_iVvgVPjW_c3eloXv3wavhjyotD-z4daNdMrOmNrRf4SErj77O16BERGtUBGr0IowGU_nKd7g5Fm39gspPwHVCtnZnw8H-XKF6AQXxNyovb9pAhDUzXnSpXk5KLuJ3E-pvoGV2sG1-Iby8HLKOf-1HHEq60tmYPUADVwlDO3AkiEJcmNeE6g274eQh3VUxZRJkAN80DegCFLUPWT3A5mi5NeelJiTlGpBCezY2w_flCMo_UkJftVqDyLZ4rbu-GDAK5rJuUDJKkSKhF-KngqVY52FdL7XPgoC0Bw47lT6V-y0YpE5yGx7tpNkHW1AZYasO9m9gzjCX6vg54C2eYW551ubxTjvaXTWXjrhhEbsFlw3zkSa_fMpZYw9gznR3NbWY0SGa_sg0FdNy6mTupHlNT9Hi21hEuAJbmMOv0W3ZiXVWSbh7FZLqV8pkNbunWFVgcLJBkDGA9Xl4nzrH-n3xRAUYiNQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ1IIZJFgi7i3OoIcoxdoEMhPZ2UgyBEax4k3hkoFvBzNKy61oKg2DqmIsPZjXhrjy7oUbN-8SBipkVRuhQcpGPJ5vKQU4izBIu7Ir2GKBm4yhOmv1cuaBQxZp1Z8dcu0ys3V4lnNpVxAC96znrVD5HDhRwbI8K5sK9-6UmxjmdU9G7qZwSD4tzZGpImPftfjm0gc6BpIzEPAKf4F-nlZZDdJ9HoEifbfMVB8XrCokW2Hvcu12e-aRVmGqaquluCf4vCHs55WxVG4m6khS1khUksWurZMhE3I9EFd3D5evDyitsJQ29da5VBIzydL7L_38hu9cjzbsMcohayaT8eCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw6sWj_WBe1a48WH3K_uPUPe3BQokmWX-mjvECrnVchTBlrkN_V7_ePoJYnkPqhJKbIzpdYykJacoi02Stc-AgiN7zubOW1FcL7qq5hwKcBi6Lr8v9kgBUbVB_wWK1EwwDY5YrZU40PkCLV6__gVtOIlF4-bnLDrwpaMjzV7u6sHuhlOuAen7QBXK0l3s8rUW0A3sUyt7bafW45JDnJMXUUa_sG2mTxXHTopbMbfholtvVc8RWpgKa3wy9lcdMRIuyanlwYufe0fXcocXYoz-tHR9sPbU06GKYkOK92YgtjkDLFoWhhFEBOwkkEsauKRtHUJEGPllWjAkCVXy_C_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWzeq75W8oCGZEE9RxSn3sToLLm_4Mynx_sYQ9seFTiqV0oEHVfjFZY0WBPrrpkR4JekbzAYaUiEMg-x2k53R3ubJT7Oo3-4X-A0s-Rbi3I_fW6XY4HFwOs3VdFz4T9IzDSuNTJBoShM-dbD0eWygebMTngGfx-fQgOn7hMj4WGY-2BUhwDH7IW9ir0Z6q4CEcAU5n5AzrRiRZNWEb2b0Op6VxiNNQLkmQHmS9vKD_fWEi1HyvSI3_ENlM9_kDPg4lJ652MsKFsfrtcjtsMMxM0a_AB3S52-XA0GFnUxUQ_mZemE-igGG74KvmFMJbsIuVsbwkzIvTBB727d7vPZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR0WW_wv__pLvONHWJFWiwMM1GtNEwhU-YDual0JbYt6MhzwOe8nEi2nIJeu7zNkqDt-gveNpq77sCIshwJp_2JC0853LuBXbQy1KPI4c3hE0bFPxH2QheOSXj-85v91L-lNiAxTNDHc_6w31SRwLUAJGxbgDC5JI-XdE0blI22ltXsOZzQpW4cVO3c_lX3r2TdxhA9OtYf1YLP219BuOoWU2GmfwnbNzxGOn28W2NbZ3vRcKJOHFgpPnpbCJOS93p_TMSzLnzbxaktxKJq4DA07NTvYFSx_agHlyMcMQX2j-aOUE6RPn0pwttr4sYs9j5Uz3Zf9yEkT6RdMJR_a1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qRjIXOu7lX6slAzOu2vugcqHCSovCmQAqCda_EWClbElgj_9D9mm1Tu8hgAMXe7uWd87WbO5OTJ3GpMEXePgRSkViz0mp-9WHv4n-JCxt8yEtOJmzfGdAFToKz-JSpsPJcphPO9cHVqJrshrjXrua5aNNC11QCujAIC2swqtqsZ4kbhLF97Wxc18FSYZjU6VvKvE0Uey1qbv63I_az_GH1AFN7ICgoVNW5_jHmSlyzbVtOqnF4zYXrl7_3orugqdTRnwTVFbsq3v1Ld5DGyOzAWuTZ1yVmM5cWDS-HhU4-TmCClRIX-evD8qltb4ZToGBTvv4qdBIndOtrkcodRKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDUDUdRBN3d5AjW8Pjw3jH12cmGMZq3ZS_tPSphuLj1ukG0jLJfzIS8mmLnxufDOCnfc3AYTqZcRZs2RHfkyjz2de804GNyMgle15bvhuOw_oUzXzPke1McY3UCpwasz4kjvXa2b5HCirepylpAW3WQWjhqtcWs42LbXbYcriWPcbzfxTWhBpRVFJ78K2BCuGind3fL-JEFFxq-PtDXYZ9ghofeiskk8OWgOBsmbelVX6QWU9XQpAZ4QX7nDc9vJ640zXZaVnAGkDREboweU7YGGVAbnMg9UqEvj-rV1puM8XO1_HKzpJnX62hEwnvKzUnixrN_6pUCPvFuiiCYXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vvESVvrSjzW3mxdkl2y4WEI9iIg0UGQVc6ccoVnpkRs6GmI2aBIrXBB_pxeLvOAC4Dez_7-1-NQayeyl4q37iDkuovbwiU-ogkB9Pvq-yqfcD3gx8jAkiVhFYsmS3K15sCxxQuCw8f0rOymHLTQv_OxeWPWICfBXzywgDEzSXld7Y7BxG5LjeVs43EViTrhfu92ogs9cwdV4L2bCncO9qoBzLmRuLISFk8w7zaTG64Uawxd6RxE5ouLTECyRCyryWdOeTGf1hh2HNLUs9ziwSLBNLaZpRhYaBGDFE47MCU7bEy3xxsQXRvSp17SpsFf5RuVCfJDiev2svGdM7m43Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=MG1ZhAtkxizTBII2f-Q-2wIc8OUcsyNpnuU8Seg-5ddpwMPENcKzielgHy3NoyD5hnIR3CzXQwlKk1-to_tlNetHlWNL8AsBuic8OTH4QYwJ7rBJu2Su5coo16MdDoJ_hRJfJ6wmkC3fh5NDTrxAtYfTP2f4FUErH5-Sdx7JU7CcIyKs-E_63mpHy2ndNITRxm3E0D4TfLMLcfNneqkvbu2uPF8ynvesV8vaVHQ-tm5xA46zz23PKEWN-Eys-x7siwrTkALb3RvPAiGXhpjqzPsBc_Oty3sNYh4nu_vfY_QZGtyWDkpm6KQA6TZncLqiqNIBeLICgDV5FVPCEv9DRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=MG1ZhAtkxizTBII2f-Q-2wIc8OUcsyNpnuU8Seg-5ddpwMPENcKzielgHy3NoyD5hnIR3CzXQwlKk1-to_tlNetHlWNL8AsBuic8OTH4QYwJ7rBJu2Su5coo16MdDoJ_hRJfJ6wmkC3fh5NDTrxAtYfTP2f4FUErH5-Sdx7JU7CcIyKs-E_63mpHy2ndNITRxm3E0D4TfLMLcfNneqkvbu2uPF8ynvesV8vaVHQ-tm5xA46zz23PKEWN-Eys-x7siwrTkALb3RvPAiGXhpjqzPsBc_Oty3sNYh4nu_vfY_QZGtyWDkpm6KQA6TZncLqiqNIBeLICgDV5FVPCEv9DRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WF7YeaoNwc2D8wQpfx85dwOP27XDGLLG5I4RjWu4WGExBB5nAso-B2rlEqB13KEn45PXZZ82BCAHEoPI4T7RWdJEOsYV78Extfx5RnpkOOeITazojb8icW89aUx9qIWrJTTzU6iQVFdusYzspwPnCTGRqhmxbdiy4CaT2uURxrHEe984o83mn1E-wMgLmYVSpGmB_MTVpqBoyPz_JHRvpqmmqBANyGL-NvwJPQbIC91_VBYuDIGU_zSQY4TSwEvTg3w_pYytpOHWnKb4mlEdtK_0cGrt9dgNeSd0utXecNKR-4U73FDr6YW_w31lvyMXNmKCCZom19PIfdGa4GbYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=tutplq2IQizT2bAmVdjxsn_fItEKgMCFb4ohQvf4I7qTurzXuqUjRru4iAWb6xEx1ffS_7mMaVzXMzbsb-yx5_R3grsgY8BqgLU9FLqMS9yzAUSglf9aQiSfofB6jfku6mg61jYswavGs5e9UjNCU01LwU-lRWZUnic-btxcCz8V46xfazhBBHSyoaqLBCpOGvw6agmvlFPb75VGWnljvAu9d7BLr5Kb8acTOMpwyjAiZGQPBHE6sCkRtgf9hlDlZ4IYBIfh6Kwer-lGBgon2VQ6TJpeCI_N4bdJE57E0BFXLfBSQ_7u28plqDF888e3mYie_EytAEokQyX7_WhT2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=tutplq2IQizT2bAmVdjxsn_fItEKgMCFb4ohQvf4I7qTurzXuqUjRru4iAWb6xEx1ffS_7mMaVzXMzbsb-yx5_R3grsgY8BqgLU9FLqMS9yzAUSglf9aQiSfofB6jfku6mg61jYswavGs5e9UjNCU01LwU-lRWZUnic-btxcCz8V46xfazhBBHSyoaqLBCpOGvw6agmvlFPb75VGWnljvAu9d7BLr5Kb8acTOMpwyjAiZGQPBHE6sCkRtgf9hlDlZ4IYBIfh6Kwer-lGBgon2VQ6TJpeCI_N4bdJE57E0BFXLfBSQ_7u28plqDF888e3mYie_EytAEokQyX7_WhT2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=BDXK2CBEr18BuObBrZ10jADwwlnOnoqR1NTfVlgBo_2rtPmw7I8R9nbtjInk-X-Bob4m0xNL1kCLmSsqWskDnIHoWVPhq3UvwFLRCJ_loge3qqODR2mhzvcRPOaUHKAzvOIj_uxV2NNHBkczsDz9ycuWs1bky-idhUj4CF2bnoMOUAmQfOobluOngaLiiooq5FKMSfX0cfk9v6c6m_NVZgq6hrboNCqr5nM_LBUx6cySjIsUpUyiaxJXLxuK24zg2iF8PGmis986u766y9C3avRFyybBBqYg1qAC6MhMUVZFHB2cK5QrUPat6wVmi6jQJxv2wKPdwp3aWbhKFNBpxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=BDXK2CBEr18BuObBrZ10jADwwlnOnoqR1NTfVlgBo_2rtPmw7I8R9nbtjInk-X-Bob4m0xNL1kCLmSsqWskDnIHoWVPhq3UvwFLRCJ_loge3qqODR2mhzvcRPOaUHKAzvOIj_uxV2NNHBkczsDz9ycuWs1bky-idhUj4CF2bnoMOUAmQfOobluOngaLiiooq5FKMSfX0cfk9v6c6m_NVZgq6hrboNCqr5nM_LBUx6cySjIsUpUyiaxJXLxuK24zg2iF8PGmis986u766y9C3avRFyybBBqYg1qAC6MhMUVZFHB2cK5QrUPat6wVmi6jQJxv2wKPdwp3aWbhKFNBpxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HTjLs6o-Tq4Fr2ZJcxmG_n6LXh6uimJlcRukPI6F9UMgrk71qQrappHrg3mQxeqVZRt4B-1t1dTgtr2mEvPuinyTptk2LVZt5m6lMWm0bHLL9uh5fUHhWxN4zEojENYPny90KYr834w06RZBdnhbglIIqqOZLjPNThw8RFD4s_dyXMS8Oc6QpQPcDxSeKKya2iWnnIMglh6EZ3xqxVqnjuD5PZ_T8BmkfJ3vj5NWewSYWpgRSDh6vA7tv5sILLpD60mOBJZeuoBQItzDADrWvBsCdDzG19DUoego-EQFa9-1RdiPMoFOe_dxxOiOmnxXPSgi_-hQ-wRY83CWpX9Bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=UlOutA8_D2yKHMJme1X92BJAAvAbX1XNTRMY7UUNuNr2VFJ_h1R2-F4AxjrD9gOS0wC9ifHMNzx5oaAtprzMDjuBd6LTvytUvamy1NhMGkm9e6xsglgDA3sMCWtLNw7J7J4E8q4UKkRVTMEnn2l2zs2klBlJAByXZe8rhT5UgqSDnAVDpjgxpl7Yaz-HCVwr9C4eIXYG-tSnu25O7FXIS7Hq6mOiD4JzWsmS82rniWXdzr-L6_1FofH0nktxomgjZtmTWqxi_gCT8toKemxHV5WpVz7PLRZz4lBesehPxC2pzXGb7VcaStcj9bS8wbhgPyTJHZc8jebijdGqEdjoGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=UlOutA8_D2yKHMJme1X92BJAAvAbX1XNTRMY7UUNuNr2VFJ_h1R2-F4AxjrD9gOS0wC9ifHMNzx5oaAtprzMDjuBd6LTvytUvamy1NhMGkm9e6xsglgDA3sMCWtLNw7J7J4E8q4UKkRVTMEnn2l2zs2klBlJAByXZe8rhT5UgqSDnAVDpjgxpl7Yaz-HCVwr9C4eIXYG-tSnu25O7FXIS7Hq6mOiD4JzWsmS82rniWXdzr-L6_1FofH0nktxomgjZtmTWqxi_gCT8toKemxHV5WpVz7PLRZz4lBesehPxC2pzXGb7VcaStcj9bS8wbhgPyTJHZc8jebijdGqEdjoGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re_DgJ9n7oevdAr04PP-lBVndwXTg6TINI-nQZpQnCFiht4qDXdH3oIqEO5ouD4aqSVkWnxykcXhFVfBKA5oXVKX_UWXJSPLQUw8M_wv5qNL-De3U2riBL14RSe3jufW--gpDAIzxnHS0DX832B70fow2GxuFyr228nvoxeV6Lb6DeoDfDqaAf6RvJwJlM6gT5dlcJybSaN-Dm8N6_WlSZK7CCgyBu-z0Y9I8bVY6OkdCbpjnNjr0VfzyImJpp17r0cIORoHPRv7PH5PDq87gH9v_QTqnT4WlAjHL4P_DZjWjoC-aIL_Fhwr8o8Hgenx9Z8Reud3cPfUHKH_l9WXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=IMsOe6HH6BJiJWGJUcibhbQd3G9Pyn-6MlnMtMYwAIJL7jynAcvK_f3XRmOP1x885SD-uGF3a6ZNBGZMHOvv9qBVEhe_VGBba1cvhiCmF_dFovN69vw5RkhqdCtmXE9nW3tgoAfGFoRTxFy4w-F8eermivYiymfaYAJYSyRZy22M_KZvFqzLIlwDQZcatEtW18A6QLj62FKLjf89te-guOzKi4D9ujalicJu_EjP9tzfGdRNXAJZE8nxFw6p7rne1O1-PgyOM7HLRD5-3o9ww9VM-F9dveVkwJ4StQSwm6uXFTj1mIXGkL2fhc4VrSBmhvJTgWa46inAQYAPx5UnXo7vPfnPVrHuDkFLAYOm7MzgJG5O9yqinxCyYNYTVtgb94_DC5YkkFX7NW_5wkQ_pPPA2AZkWksjqk8RiW04HMuQYiOQUWcA_jiHkmeOJChIKDNg33Wm-Ljh_yKMHPlkeajTdtfuMdOmR1AghsH2CVPEUz7lEauGQH25qoRG9leCuyU8b49OOa3xmKifN815YgRas13Nnsq-cQkBCE0-ZnuO1sNL1MoP8-83KxPb_2GWZZ-3_xasS9U0vGicsHSw2RxmR1UB-QWqJ2SOptBrKupU1zMlSnTEQJUiQCu3TTS2OuhktB1L34WjpecFAwsyeV8fh7xDGG7O6Aflc5p-ZPY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=IMsOe6HH6BJiJWGJUcibhbQd3G9Pyn-6MlnMtMYwAIJL7jynAcvK_f3XRmOP1x885SD-uGF3a6ZNBGZMHOvv9qBVEhe_VGBba1cvhiCmF_dFovN69vw5RkhqdCtmXE9nW3tgoAfGFoRTxFy4w-F8eermivYiymfaYAJYSyRZy22M_KZvFqzLIlwDQZcatEtW18A6QLj62FKLjf89te-guOzKi4D9ujalicJu_EjP9tzfGdRNXAJZE8nxFw6p7rne1O1-PgyOM7HLRD5-3o9ww9VM-F9dveVkwJ4StQSwm6uXFTj1mIXGkL2fhc4VrSBmhvJTgWa46inAQYAPx5UnXo7vPfnPVrHuDkFLAYOm7MzgJG5O9yqinxCyYNYTVtgb94_DC5YkkFX7NW_5wkQ_pPPA2AZkWksjqk8RiW04HMuQYiOQUWcA_jiHkmeOJChIKDNg33Wm-Ljh_yKMHPlkeajTdtfuMdOmR1AghsH2CVPEUz7lEauGQH25qoRG9leCuyU8b49OOa3xmKifN815YgRas13Nnsq-cQkBCE0-ZnuO1sNL1MoP8-83KxPb_2GWZZ-3_xasS9U0vGicsHSw2RxmR1UB-QWqJ2SOptBrKupU1zMlSnTEQJUiQCu3TTS2OuhktB1L34WjpecFAwsyeV8fh7xDGG7O6Aflc5p-ZPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_0f5GdMRnuSDh9jrCbVrYkBHYP814IpvUGb53YYl-ZrBUX_MDewukl2maN0FXHa0g7sdFrNSDYZ-onUfWRi_BiQuvXELp1dTMs0fTwYv9TXms1m-hDPXik6UrlCp-nhcqwVpyq6ZD8T_MA5IN5UpmFOvMGOfd8EY1kyKcofVRamigz_jDO96W3UICoKLnyr3EfARJ14Tw5vChmOHzPdtS4yYLt2oCGlO3gddE8bS2kQ0CLkAEybkdBUs88w22pHnEbT-eIZ78rKNFWFwpwnD92li5gK1ekKf54JN0PUyqkVEBgIV03u3cjjtgPn7IghzlhfXyfOVxVuCeFQNPdfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=V2SxVay6WizExfD3k1SDDQ9exei-PUbph7zkz9bEbvZh1XM3OIAAjvQi5MuihuTMorTmr3nMJwc_VfK1ZsiPLTaKngXpx2y7BAgt9RGc8UKgkxqDuHw0NyDwnw5u73dgtaIk2ot7Yg--f8HmIDsQzTLynl3w465EONxmZM79guxjXsoQ7_GVG8LSW6GnouSwz3joUewsOs1-H8yOYeCOj17i8bmMEi7D3ZflKLPiftf-4bOro1ooa-qE-d9H-RC8Ym2AclkCtKKPsZ4JFw496aUXiM4oT166xihY0wHewtjpsCRGSBCNWpmQXrXf1cjGBAEzeSVUTRUxtKL6sgcPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=V2SxVay6WizExfD3k1SDDQ9exei-PUbph7zkz9bEbvZh1XM3OIAAjvQi5MuihuTMorTmr3nMJwc_VfK1ZsiPLTaKngXpx2y7BAgt9RGc8UKgkxqDuHw0NyDwnw5u73dgtaIk2ot7Yg--f8HmIDsQzTLynl3w465EONxmZM79guxjXsoQ7_GVG8LSW6GnouSwz3joUewsOs1-H8yOYeCOj17i8bmMEi7D3ZflKLPiftf-4bOro1ooa-qE-d9H-RC8Ym2AclkCtKKPsZ4JFw496aUXiM4oT166xihY0wHewtjpsCRGSBCNWpmQXrXf1cjGBAEzeSVUTRUxtKL6sgcPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiI96qlIe6quBTsAdvVod_4vxaUL3VvmoTf2n25pydygWSv9NhOf9SKzGygZ8pVGaytm_0C6e3EvPVxEVq9NQml4Q_6vsvd2BdwmUY9Zm5JGdvJcj6qdu5Ag-K5aXtQB5K1jCCGC7CD4nvlH9sXz7XzjZ6hHYLCGVu77AOvlDAZDczyrkDIjtRR7xkemxXOgBUyfjjP1zVj_veWNOzhoHZgKYeGAaa3NnLVQtyVBww0iuHE9mgCE-Db3apduLiLAQVk4FdQq0wwE35mPv6ym_KZRWuNLrD7OdwWybG-BbqSzVVMexsJrGLhEqbpIjy4j8Z1Qo4miEcC-pILeyuVZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zl0AUAao2FOFHYlfXjNGs40k4sdycdepd38CQjucOW8FKqVR01nE6TBR3P4Q7MIn0Eq_B4NE0Fw0eD9an3JlSdaS5VGo4aI0FmKVBjosiOps9sHErLkMm9D9IoktzsuGRhFTsdY929j9KZDW9168t1xm8l1iye1s1OqOBcD-RBRR7476q-2_NepGh411781kW5Uw27gP3TlPS0Uh-PiDPeabeJdP0J2osJcUQk5b2D4K8Gqea36TjUySCsC1P3XZTon9dcf7iiBrhRTGTb3Q1C4eZuzpfYIzkr2BCnEbalUAl8u-kMwClJz8TaDvOo8-wNO3jMtKX3OEQoM0aim1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftgkUYGDi9MJKa-TGl0JD5MqSBxatnCWFS4gxg44Thlkz0r2eJPPyzAt0Pi69KBIA2Pzuag0Z4i4uU47PYyxUdCJE1G-RKcTxVD48AIPd79236zeihvNnOISlHeZxuwMb7psm3Kn4_CNgI9tLwBt-IW-z84IAZZA5RBK3qRomSbidPA17MPUudf82bMAvMP5ZGlGzYzmhFwAFu3zAnilv72myEzssJmWj_dsDpXzkg0FxBTwgaiH4w8kHSL4DHmEKfzY8Vg980kPOKGd5Sd6V3L9GFpw7-HCGrFHAHL1gq6xbtYRJqO6U5GwIrjUKeHufFm-D4-tQMbW09pqBRXknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcqXtl5tYK3w1rNsNrlp6OFVgBU4W1MtDNFq2X3wjtD1mPaXGBe6f6XsHTnxY0vCg4pje1KUhnGTEiKzVZjBXoMdxqIWtxsjqyfnjMGFeZI8w5anWXEt8JIfMPtKJGT9OqfCr_FFr9FQyGBniz7EjOfPTOR5L0bVimonVh2y8bcMbG9NW_yFjlHppNwphr7wjePQ4-BS5oVfH0dPxDktXu8FCRnH6nkG6w8F_S44v6yCzc9Hk3jueuQvpYIKjWuCkP66EDkjF7yPre_VkPzO3a-C3jdno2HZBHcB8lsLX3eJoNXo8xwm4Lu2Jh95qPbjWigB-DvtH_jpeDqfLWywQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKgqiv_RbQv5Awm8jdrvm7QfIep6bj08wvG7mnMsOKUcZqfA-TsrNMRww8I2b5N763_UuyLRHrVXXndWYmzsteZlph-DJxE3Qamuq7KaptoDWcb5m88kWTDiLWk24sDM3N_fNgYq8PPcb_bTFcgWH8j7Uuo-6sTLeMjNbPhmX5mxoAT1nMCkcHhlFGrBSEdpGGKTukjILw4-TrR2uXAijLDu9ftp0Bi2a4yXs3op5bfQx8J2ufVDC4ZkpBUnx7VDzQQ54V-hgaxFkRLB0tqC3nraE7Whf-gqxK_LAHrVp9OsUqf2_bmlDuNV1BLqVXGNO9LIQILRrJZ812__ZOBc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=eMkXElxdaXLeN1N-m8XY2wC-QaY1TZLZ-7SIA69er-Phyg489pCTkCWVCZU-ZWNlxOpy7oDa5F2PNpFo5baJIOJKxQTiG-sZQVHlTv3rTP2wedCYPeSjXUMLqH5tBVAtF_29Fck0txyGL6GKuX3_DMIFdV0r7QondoElDfF6zKwpVd0lEA1APh1N_e42g8g-bGD2byu1DwuRqX7qcXDzNYo4BsXJ9Z9OBT5PIpo3SLmLFfiBbOBP4OEfHFAyUaQ5OfIcB0RwfXvTwqr4iWo_nvhzIKXdPImeT8q7YNLvQgaOUu3Od1nlcaGM8Gc2fYxQBwmX71JnR7Tkrqz1qHI1sqRZU8lxLJytb2pjl8RDUC074mV5NILAnSsnLsAE2S14Jei5tCJ8TItBOoTXXZwhtLXl6yXRzh1mruMfNWKkQHhN2jXmkLIYjveRm2EevnUJLOXhLfh2d9QWq7pJZMMBnNouyCZKPIyWZtopOvCZ0kZEC3iSn4aPPH60QgJbQHA3-MxFAqKlXT4j4EiHQKmv5uMlBwTga8046jCFjMpR3dH1E_i5ZlwKpt1ogl9Awc7OltVgnVnNGICnbOEJrnMO0qKylWryLwnWt8_YgpmgNoMlzCpBsZNjVBAYmUev8ZkJDouiW8a3QTjJVaCrwF3nvV_MIDFHbHcCbisx0FZQGhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=eMkXElxdaXLeN1N-m8XY2wC-QaY1TZLZ-7SIA69er-Phyg489pCTkCWVCZU-ZWNlxOpy7oDa5F2PNpFo5baJIOJKxQTiG-sZQVHlTv3rTP2wedCYPeSjXUMLqH5tBVAtF_29Fck0txyGL6GKuX3_DMIFdV0r7QondoElDfF6zKwpVd0lEA1APh1N_e42g8g-bGD2byu1DwuRqX7qcXDzNYo4BsXJ9Z9OBT5PIpo3SLmLFfiBbOBP4OEfHFAyUaQ5OfIcB0RwfXvTwqr4iWo_nvhzIKXdPImeT8q7YNLvQgaOUu3Od1nlcaGM8Gc2fYxQBwmX71JnR7Tkrqz1qHI1sqRZU8lxLJytb2pjl8RDUC074mV5NILAnSsnLsAE2S14Jei5tCJ8TItBOoTXXZwhtLXl6yXRzh1mruMfNWKkQHhN2jXmkLIYjveRm2EevnUJLOXhLfh2d9QWq7pJZMMBnNouyCZKPIyWZtopOvCZ0kZEC3iSn4aPPH60QgJbQHA3-MxFAqKlXT4j4EiHQKmv5uMlBwTga8046jCFjMpR3dH1E_i5ZlwKpt1ogl9Awc7OltVgnVnNGICnbOEJrnMO0qKylWryLwnWt8_YgpmgNoMlzCpBsZNjVBAYmUev8ZkJDouiW8a3QTjJVaCrwF3nvV_MIDFHbHcCbisx0FZQGhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=YHVni8a1dZd-AZMZou7RG50pUfiP_6OzVVoShOwwpOIeKr7UgbnpzuGhaeaW6GUEXw1QQWGx-C432xs1DEqp_IiUcbOKCmEMb2lCw4y2bGfRwDVGlFUObVjgvFhm1EJAR79Kl-W5wG-SuAYxFqQciRpFIgHfg88QEuhtKRj-v3OXFbMHIqAsCs7vrALd7Z-RC3anqEjdZPAzkFHfm70uc8Qx5-V3IclLNbS5Gukblk-zW3juKqEZnMwe4t826Kf8OC76ngQGmUM63DJjH2F_rNW_hyGfJEdQuKVBYgvUKYujqYr1igc4odIPxLTzBmPpmiPmLYmdJRrv-xs6DqLSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=YHVni8a1dZd-AZMZou7RG50pUfiP_6OzVVoShOwwpOIeKr7UgbnpzuGhaeaW6GUEXw1QQWGx-C432xs1DEqp_IiUcbOKCmEMb2lCw4y2bGfRwDVGlFUObVjgvFhm1EJAR79Kl-W5wG-SuAYxFqQciRpFIgHfg88QEuhtKRj-v3OXFbMHIqAsCs7vrALd7Z-RC3anqEjdZPAzkFHfm70uc8Qx5-V3IclLNbS5Gukblk-zW3juKqEZnMwe4t826Kf8OC76ngQGmUM63DJjH2F_rNW_hyGfJEdQuKVBYgvUKYujqYr1igc4odIPxLTzBmPpmiPmLYmdJRrv-xs6DqLSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY9R7TJEhQvuofyRPc2QDi4xoAWmKL6rTBtLyLWiz7YKIUZfc40qI7C_gHaZQXQM2-W3YdEXxA0Seq33OmxeOvXLR6Yi4fzc4joufHMQohv-Hu_knF-Z4ndZNmePXHw_U16c68yc1_VSL98l5oUctoIUclCQUIsoOadC0g5f3rA2aZhMweChKDzmc6gJLtwUHezML0kH58dgeVDYr9cW8vL41B2vpGCDLaJ22KXTJszf6eHSCodlzAwOslabwZZ2fM-ZNilRX_AHkxPY-Zn9h4exD0WkZUFBaosCVE8dJJlPhArnbV3LR39bJdCZF0sTR0wiZ9_e3OmOKqtJT_Xy1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifbCAUhud3uIpskm-fFC8OO2QT_DMz8ygJlBcX-lmXsc1IwGk97vVvh-NFBFBdYQ45dtAsyV-NY9SqAd6tYNOa-jqvmYlcs8QVAEWqqn1qgKyK1FHwQSe5XJsZ5OKFNQ_vi2zPV7NHtrK2mXGl0t5rMTlavyuIb0cwy1Rfs1XUJ3R4wGACuC3WZUCLLqFJzRx4EXjKWtsc1mqYtvxQxZi16dbUOfo2YtqFMM0EuAzvPXsatVBVOUoVa71sDUKk-M7Qg30eZ1anr0sLaEZqinyF4wA7rbFRzgNBcNZg4-o_0Gzt-3HWooJt9pXzK0_eQqioUUWh3srBe_oCIaqMhEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAmCiigu2RVDetk-OWDo8eFeQRpGaesoMCJ0WmwGmRd3_LeIBTdmAWmyuuZfuVNQ-3aurEb7SjRjwN-GYmlUSL3XDe1RmtO5AeOauIlJS1KMdHo-9P1ruk04JwiEyy9Mh329UQE9iv2Xm1maBRkJ7HmMBBqRmoOpFYTPo2CQCrB4AA1gSdHaGrQkVSvjR0Tpy9s2ve03p0xVoyz37aTPsaXrtMcf84V4o531YiefWAyrECU4iPGaO68pIeej0kfP1sUCSPq77VPyb_XLKu_nRgkrJLIGv3sh2T5ng8Y5ldmgBTEtzLrAh0zeTGU-qJ0K133OiBhmfz7ww7anMRt5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0o_z-r4xY48Z3I4QRJ_0fvAR531E15jEYGdEAD4r7WiSEBxl-HaFe4kyUQGycun8vfYGsf17rxlu8y9N6LM6Qmzj1pykkNnkQ5zuVlpW-Y4H0tc95pPDF3btXJBju2Ryui_2tvfXde5u-LPobr7C8bVdJc9qk78cUBF4pCksqAfNGFk3CAN2K1LOA7oHtJOVXUxrVhRyohS1adZ7A3LqdLuF9ZxLBVSY9YCovq8qAqerT1ue0OEU-XymQtCuv94807LpUPTMiGPByDUlhwNL9eX0LsBZUtm1YfotODOKD8HVlHnFNBB_6-l3miuEvSncGRMnjdHE3OW51L9-WxtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5g9Hts07ThsAlaLPuzjT1Ovu7OD7By1rmbAzUVa3dC09QOLYNW7lYci1RvnLXxOyJfe3yN9lkOyut8aPDy18hi7cNog3fVoXmfLl11aZ31XYLk10ByW_lXJ6KT0gSBt9tecAa5CyQpwuSBD_2U-IXjVFPWVGNEZ4QXDTGk9tUCuzU00YUPDf7AZMMDlyK5NI9axZKNq0rxYCU0YeXHI-YT-HiSE7VKvrM-ScYqDmefefF4FRl8GyWfRmxp-8m0ASKEP0VLj2dpNUne1tTnln3Jb2Qjvnh35HNYq-B1AlTJ9j5HSRBAlOO3PKZSYqbYpdY48NdY5pbh5l8bbQbgq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLlnqwrZEJZbasWkeFsThVYI0M9eCkn7JI07S_-rNuYJMB0uHdLd7IU97GvSwcoKIvbkjieXQd0hI6pIt5pCx4RY3HLBeEWV0NM5TPLlyw6QjHD_a0CvRra34gvSsO5CMOpc56TudrbDPofpCv5IZd9mxDIF0S171kNKFNlDJhWuVG0Oo3L7SDStBKrC9K3xk0x-ZkKPMMWae5-wySZD0yVpmcK9qgsyWZYuG12so8V92GMWXWWpqxEYpD7T0Iq5q8agl1-R15F0fRHVJPHSc5sCHRyq4E_ANfMB6O30zElQDlt2tN0JwpjQiatDV8K5JmCU-l0XaNsVEqRmtlRTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihwsPYwtMbzLExNk-lIuQzHWJQGHwfDW68pEBUGD_yzOicyZpV8DdgIjdK5x69POqIX0V0-_zc07VC25Ku-eljdZzP1yP7icLA71vr5yltPaUkfYEuUe2pVrIHpe_GbkI58cDVkoylxr5mXjzbKFchSKXRQdsCYLAHPcRxYAcmATGzUKtwqKRnBjgKnorksyDo-Fk3KrJwyZkf5tcYo_5nQ4lOoFoVVMIZZpUnY1PiHMRK11qXfGnGi_NxO59rKIPV2-areBpzn-2ICOBLlpwpZqTJXJi_EO7nKnV3LSkttINkbca-hDbPPBmcF44wmuAuXwcKudOvSb47PWGxUM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfUv8euq63HuuV2KTuKdrGSEoCC869s7Pk_SDJX5bwWf3ZX3MRkDA8kP74l0LeP4oo4t1axYj-3BWQe7GhRZV77vom37nK1FilOMSw4phKXDIZnLHJzgcbgcORNgloGJum5ARBriXpVWtstU8HXVOvEz4HRwNq5DwsoA_09_N2hlmgTKzQzLEy34NP5D9gE3EAqBE9zvqvl6-rp-9YpNVSZnYow2HMfEI8XkbtIWavo_AWT_1kckpew2fbiSQ-LdsQvYI8DRysUVljmpdK1kp86AJfuImNIa8Z3JJRQcrGb_hd4GUvO4v8luaWLdyHrBNtaibEAwZSfm8rpXAmuuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8Tz-UptdB0CRUnqlkYy02GFuifgGcdM2Lg1HOuL3y6lSr91ag7bJVOls-DoCa55ydlTLelRKId4IJjQ4xkI5267iJPb09M5MzHU9vis7PF-QHTCnA4c_iO0lpvJ9CG3wB5nPLIEBTSCn3mOx7HWYV2hQH8f_M4KUalPjuM4vaQ2amIEzF4_yRh9QrMPJ9kQ0Y3WM2Vsvx1I2FL0ksXl8Tif-lqhm04gnOTY8Cfe_2C8jWZhRl1y8PYo03WrtmZcxfvTGnMbZ9btLCi3SKai3R2xfjKXro7AsbdA-dpjBuyAqCII9DFahHvCawqS5DcxYJcqvBj6CC_tQK0p4OcovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg38ZgOkT_yTDKNvWBvGv8SjzwafN2lRPmfezKAUauTG_s9Df4FrL2Gxumuxcr0rsFgMpNWdeFqC2X14ABXU0EqpQ7UdegncwKpSWYlplt1pEVXSOasr66XZKLwSFBzABXNGuKnEq9-tRHdsCvMowqyr9P1G0lI08kfdsgW-kog4pIHjV-ke_53LJCkNwqtuWUXgSnuzcbsZMMA7yJHD5mONlrFIS1rS-tql9gHbmayMXKR_t2bGc1aP4SkXCWS9nm9mANgqr7pI1ZwhKewDAsVvsNidcD4YENCLRhdaGxka_-ukUuy-QNkDQ-I96Ho36p2VarX3rE2eK0Pz2iRRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfnN0VXx5w3h9Gu5UEdceRZk6CmYYGUpP9MKmocez3KjiaAIcb_c9eg2YaZnGmoiNus4JkEMKN3lsfEE2LDYatFHJRsbvPzNZlBA9wGkBBfead3V2QnQ1oQ4YBWcQ27-tQww2ByAjMXvynAy_bvJ0p6XOnww3vKevdaSg_IdS1RQUyCYcdZG1n4QcXVLsv8lM67s1ku5_uGEc62TC_20AOyIdiqp2tE-WI9rmRDsYLzKAp3iubl_kUUB4IOiMCP0GXKY5Sw-i4CubpMyc0apcgWHFJwM8nLhp8lEOMH5yJxyz3yQ0VHrqM78oZ2aNcXUBkyEx48mkyUzMBaU97ks7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=WgqJf7AvJX_vImSHJKb0uMV-nF8C0s8WMh50_xzDD2xJJFJmwGukBlZDOhw8i1HubgvM5GTY_81O-iXcDYB2uYAVQ4jjeFRTSR7_PpAcSOpzQIFaMkN6gWG8DYjzYBK6AZ__yaSbb79USniCm8KqPmvM90AE8Sw9TUZbK993nR_ShMgFOkFGo9jUIC-hVtzm8oxcfZX1ynpjCTJPx7Pr7ry39eiTimv8kWrCrmjR7UsnazQIqE3qkSvp_D0TPLsYcOjAeCCoIClDyWopxh6lvd7KVe8rUsEG2_9f1KjoaSQgPJECiFsD8pTBXDitJInhJR3q1qPbaV4Snl6UTvZ1hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=WgqJf7AvJX_vImSHJKb0uMV-nF8C0s8WMh50_xzDD2xJJFJmwGukBlZDOhw8i1HubgvM5GTY_81O-iXcDYB2uYAVQ4jjeFRTSR7_PpAcSOpzQIFaMkN6gWG8DYjzYBK6AZ__yaSbb79USniCm8KqPmvM90AE8Sw9TUZbK993nR_ShMgFOkFGo9jUIC-hVtzm8oxcfZX1ynpjCTJPx7Pr7ry39eiTimv8kWrCrmjR7UsnazQIqE3qkSvp_D0TPLsYcOjAeCCoIClDyWopxh6lvd7KVe8rUsEG2_9f1KjoaSQgPJECiFsD8pTBXDitJInhJR3q1qPbaV4Snl6UTvZ1hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
