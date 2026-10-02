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
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QE58XO_sEaHruALgp1ZzZrrIiUQ4R4MeCvOeFtdYG8X-l55U7gMcOUA_YZX6e2RLh0QKk_FsgcMpKP0nh5GT-Ra8c9elGbwj2ty7p4jRNPE6s1iWzx0OETREiIJHTcAX2vcCmSl0-cJU6mFp6G2Oo5eVE1Apusvn0ypn4LPT1w09RwCWqZ9D6_4f6ua4ysJ6RPtfrlKMvxtV1oifqhj3ohi_k1avZkWcrM5vv6JPTESagfSFE2wSC4BKF123Q5F2YfIkUHj10tLJzpoiGhWHEX2clAUnfn4Fc2tfKbmeLAvtyL4HhKeZMECuEOJ-Et_yMV7Mq5vnIGZy-2VW_4NGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NUWQnCr8EIJFQT2Wpwhron_1uBzVnqsCo5OwQponGWJvDOoUzfKnIl6YzzXHqLl_Zuh4PN3Zp56_M_ycX3GJ3NgUVVBdM6bEcstyjQ7NxX0urG7wgv7YXMmQkwc3ERvgfZgGZ30DpidKYRh8T97D7-anjlU_sR5cy-Ph_TIBsS_X1Xs_adBeTvyHkiWtKH2G14u65I6HC9SGpzrKw9w5WGGAYMlyrF2eV5-m_UfZSQujFs38xaADae-mOOolZ2eAeINHhc-fFJ4SySnPtobxlqzAeJEixMSW4tZNdR4Xr-7u8rFJdFlFB1FFDXVKmdQVmkO0TQ8YLlst2NV-im2ziw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=p9yGEPoHEhgRQGgxsRkIE_rSePwSF9dyF_Ovvsxs2DWNZO9eD3f-Ob8YHT8aFneJvE7eNBCP7o3EdnFXuoY6O47_RRGIwXxllRpQyh_oecqcufy1dUiZfY9XybL_FkfROv9NElmrqdkOdH6TEogZ4JMMe3wazJe5q7z1IZd0_1DUuaNe5ASG34eSakrM5Y10kkx7OHI4eCfqJnjs2XPkBGcilU_aPsiUgPqjZAdmLyYeWJLvpwivzGQmhocEOTNeAOvvLJpCp2cbZD4Qct-bzqhmLZ4OnBJAGj-G0r4mhZstboeW-uWB4iAU09Y7tkJHhauyL37diHAxePwufoVNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=p9yGEPoHEhgRQGgxsRkIE_rSePwSF9dyF_Ovvsxs2DWNZO9eD3f-Ob8YHT8aFneJvE7eNBCP7o3EdnFXuoY6O47_RRGIwXxllRpQyh_oecqcufy1dUiZfY9XybL_FkfROv9NElmrqdkOdH6TEogZ4JMMe3wazJe5q7z1IZd0_1DUuaNe5ASG34eSakrM5Y10kkx7OHI4eCfqJnjs2XPkBGcilU_aPsiUgPqjZAdmLyYeWJLvpwivzGQmhocEOTNeAOvvLJpCp2cbZD4Qct-bzqhmLZ4OnBJAGj-G0r4mhZstboeW-uWB4iAU09Y7tkJHhauyL37diHAxePwufoVNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8sHE_d06Gqu26_r3EoQG_Zp0P-zHiyatVKVMdlmeSrT2Pqa3kzEALRRSTZdU8mL2yYddfmGBMbKGwj5Lk1bILJjCMG8G1BGiwaEvxKRk8O2gXDi8FzlTAcQzHMIponl02ZvKyNqIX9RAt9TE0Ey01xIYCSaDbLRTkytMDuiPySZnSjOr1nRWy3zBhRbdMD3rbeXSwlJSWSDq-c1vIu83hmVncvmWc3BzyN4fAr7VnAYyrV7lH7G2Q3ycEOx_ZnKysn5zgAfp5B1VTTRLpz7i8erpXPUoJMSs1sOP1t1tYf5wwBbkvsDTuF-NTXwZww7jmycXh5IzLfhUU6ozARGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRsX5VG4271uuYpczw9XKdTp11T-LxhDLT1YGN0F7dCE_xsQz-yCEAfkQQ2eQldaIUuJ6IqoTmQCQxBRLlMWPa9CB30eYoOG4B7xYPGmXVbGDwFLRo5a70M2KgesvDVvfVmGCj_PwCQ9CgzrWnfcrb1UvyBfiwLJaNw3gCvpEqK3DszNTfiCfQNVl0LqmiSrYa7hBMpdSudncBWbKVCAkihJTXPJe_QVrNOqiYOY4mH3T0QGFX3ZfiwiGl0fm7p6PqK_RLZNqeIXR6R_cvQquzSxe_7mJ04j6wPUBiu_z3QC373FClvTeFQ3VzrMwp4M2rCZxhQ63Pc3UcwmId0oJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw-KyXTaM_Z8hpxLdG9_X3OaHkLvZXn1up-yUOQ7gM8ogaAuuFm7C2RHTfCFYC4mDyrEQvYqxUwYPuTk-RHe_2cm1xkFZ6_ysWVsIPwtkwfMGfeS5P_1vc9MggSokPl_NunhbT3yyv3UW33q7svaN0YYSsUzyyONf7ySJCd5OJSCt1W22hv4H6Jw-3pQUQoQ80-k9ATs_cWf1PmBwZaITI31o5M0pHOz1gw8GbktfSl1Hq83GR0rt5VDqA1koVCLybr5lexPX60TUoOArK38OdBJS7Lhj6gDb3y1AmcwGMmQf4U0OJKY7cmkt6pAJ_nu4Tntktk7IdcrEQuuRGRURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEs81iKO8BDB4zxL6akjPHjF5KpgJicQhVnaoUkZmt25VG0DGZC0i1Cbjk89GJ2qMbBdQZiwdlV9tqNagWdryxtT-0fauZ_JaTUH_XdIp9YIZjkEjvJOZQ5MuVE2XslviifiSdf4XfLKzGrjYdoUsC7ZryM0CsaG3E1NEYB5njC_K9qBINQNwyradzf86ZwL4nHB5znclMkQG5QmD9i0ijutaaotpsniHdJVRnUczHZ64ePusmIcLak0WbKv0HdMqpzsAQK2JBC9BupvMi32Fia_-lwbAsPwZHmoNRIpejui5EE9Irf6m43U5BOSjTkA_VMPEIrzFQGv7frBIERHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DO1udFNV1brhil_45DGr0K6V5T-VewUX9LUZKw1XCrWI2WGcw2JzwBwaMUh85khO7dSM5qns94nV-fGwrqE7-hRJsFOoyD70snnNtycbGAjf4qisI2RZDRFnuDTX6z2lSyO63EaDyYOCa69_Xhkq8OGj78VveyHMl1cco-6GoiQdQDb-W4CmzhCBfOl8TUKkn3wi4B9nusVrIwkmJ4KsFgXmOHKPIKS4E22KsP5Rtq3ASwcx5ulP3geuSN4xiNmpYaLonoi-fYKf82TSHWL12t2hpO_LhSSA05tpiFUflVffFrje_ry5efZO6zeVeFnMIzGzwbWJAOhCWV0oo-tn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YbVIKSP5Vxi8mqf5n7GTNxYi84mUmwNFfUUG6F9ruNLuf_nxAs175m2lFSFO419qrK6uhn4Pu1aOBsZiNbqznz_7bnDZh83HIWt4aGdj0TtaANRubdD_etroEbLzQ9qS9jtcEYN86SttAA8KWqFIWfEosKNBdQ8cPeTTsfjIexJN-y6jvEUDzFnkHjPc9Z_TPsgM0UvqVkMkyI5bf8td1tv0Fa8Y0vRB4Z6MEimxG-fDVrw82_uA7k4jk0JmK_oAYyJPg62Q4aZU8znDUskRLReA_tksgVySP86RgfcGKdfsa7uRyHz3DKcp44WD1wLjafnx2p-zSXUYOAEUdiE3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CrtRsN5A5Y7oLuerAgqJ7TpB4qo1zH7SnQASq75L6hL_jMf6v6sLkC-v5iJ9gdINWSLREjjA9sLl8v1UB4qF5mH-2XWM1uBV_j7IUb7N_uxE9M3UbxGI-et7nEkUmPQ6UgJSMt2xtfBFWZcml9iMx0awU2PHwJawsBGktoqLXM7xAYungjliAziPN5J3_NU-jupE6Bo3C7gbHgJH1pI8j8p86hZC-bYfZV8dPVz6mYdw1sYJbFOJtF6kl6DZcmjO40uGyoIpxINbMSIN29MY9VIBn10vBNyXeCxlsWUuBU6BYjb_bIH5_aaDtzryW25Wz7zXULrkc5X3EiqvCvq-JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5P2UiCZ6tOupK5iqUIuoT5rjOl50x89rYM7jXIiZerD3QbUySoyvL51B4RFdPjD6WLrmPugjnP6Q5zOjMLvZ7Yz8UBgAyRBzTjLVSWvZhEpxmTP3tw7KxnW2jZp70S4wdB6BezR5HYUOB_WyxqJar2-Vpcz0s1f0elzd2G_cfpUfS9ErcJiJxTF2zPiL2sj3-96L7Nvjhjc5b_h75xGjFD4eWoSd0Q9l8yQTV3FIZ_pR7A5sbbLWetQau8me77MAylMnHtzeJzm5uNzTsQ6Olpe61dlewP4Qsg2ZSDDrJ43rZ6K2VqHGLBH4SRi4xQIxQAyGV0CexWNt6iwymg36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IV0f0orXLfSJ0MQ8YeqtX0t5N446Lus9AxIEANN-qhv7y4RU_xCHpNxE_f7RBw9UP-e3PSTqrlybwsw7q9l1sA7g_xMmjzyvf6hJFAWa1nGsIFjB3ObYwceV_2dcm5bwMj7el_U-BhURcYaCY1lM1oA0eWbbHvEnZRkZbAIoW_txI5VDBqZUfIKQdRpcF-CirTzaF4sMUAkpC2ZQEvj7i44A-nhvZdOOmi4VXp4wQfIktfQPirXwq1b0UAMuuTqKnESprYY3xUISRhJMzhc3UOxS8fjiyiea3YkImL9aU8O5mg_mX1b6k80oJq9UoKwgn3pflRgZRgbJiNLhgjXJ9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJVpEUSakNK6Uv8G4FSCBclEWp5NFZK1krBBIU7l7Gbrpe93SLM3ew-KOz-oJUof3jkjV083WzTKXv8NOqFTDY6OCfOdlEE79tm1qqgJHQ0BTbXtOBsj3ETeu6GObqFeR60DDJlVBTNpAJwcuBOyUenBUVnB6XT0YSRpdz4rB5LR_B5cKDYWWuf1qsxHKwdHQwRklps27RafKprMZoKp9sSTGjIpaAAr3WPz81KqeowqmbctIikufP8BRT5bW8lhTBqCJSuAr68TDJlg4YBUhAVZJGO2Trt7fztr-Ry0rPwksMp4FPX3f3IZNVyqlosnrgwn0YARMxeDfmeWPElYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YN0c8hRc5yzu6KzGLcfIylbxgdh2iZgXMzmohgj0JxphQtfz0eN3nXMdhU6r6pkDraMY-6FzNs3ryFAi-cmpgZY2kS-iPi5-Q91evKBx0Qs24BNkD5ABD5Hb2xLHfpJACl-zPJFAAnQYQTba0xzxKtOgv-TQ-XYd8fMIDXI8-sW3NZygMwP5OyDikeaEBbplNWxFX0kWX8fYPbctAfOoXf6O_zllquRy9ISAEi2LKU3lTZFM-oPb9doeopi847RG8BV9cW4fBu-d5Xf5Zgj49pffqiN5EnFlCMP4PKnCE2-XXldwwmn1AlZvO1HZABtTJsF6NTpxGNM3zfunhSCjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1ZPypMJmdGyS42xtV_DeVrmBd2pG2hd3qWJu-h86bhPMMr8sE_UM1LeiQpvTC8LXhm84EtqC5DBCRjthCjXLERvT719r5Q7j8Af7Ivsg-MeLhGBg0Ar1t39pOVG99fcHEvxAk0_bWmegsOwgdcA8svAZuB3DWDAOtU3sFhe-UdrfbIaTF0800QdIOFw6swFpe391F-l8X5Jd_cUA3iedJU0zbUoHaNINMDqXKUBUiXED9is5o-wmqL78eRyxP3KxskLh-MN8wUMxM2wYW-oQmmZifeBAxN6IDiBSD1lDcFNnQo8cjoru2wEdPsaVRN5y0Luh0HFgOgczpRwvVanpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MgKfV68pW8HDcr7aiyavrdB-JBbf47gEkcUw_iTuAVghJd_RmhVm7ZxHfm9b9eeYqL-xVqDK5dyhp1d-8RRjPWRH4nUAIKZ2dXwplRTk2UEAjBjFeVaSI5R_rdIZ24lw8m9pNVEA6KU_vQt26zi6r36rgxxVWsu44hzeDzB_TkFdd81B4dzxsFoS7cY4GaCzFBMXwLtZcbI9G5hE0biO7qGVOYMtULkeNdQbycPm9uGirP2Gq3cALZtDxcR8Hs9Wz1hcKUC-LZdWa3x9eg6hQiB3WzdvDI7ii5rGts97CRTFdKab4_hvcGDfwTCTfo3hISa_OlUVkNTObDkyugL4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqEIKwtYp6035H_gJt7nDBeySusjl25RzjmO0IDq_avtT96_0aECB0yZdgZD0MBnh2uWl7S0LTIjgoqnF9pbc9yjxJBozE5ai_vAWKYLRnsPFFnJYAdSLkZbwWGYsK_A3RYEJEggvD55baD4q9pmEdhgxZKuxaBjZvBWXvG2MxdGQMSimHSSMB_E1ebaXtq5HF3732AMsmeHNLZaOEDRvT7QSJ1WUL2CGTLhxX4s1MWcbddbuftcu7bunCfd1xImqzlrBJolI40O4BjmCqv0m8nuUmWNBXDE9tw3ySH1RymAYvVY3z0j0APn-ctUT6ZffBi2xS3HVCkG30BMQMesAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZvSh6FhzI9JPMvLF74_fdP5NW4JNWd7H2OsEVStSwYsP9MtgoxIuyxzLAoZvd6n4YgrBMf5HZewE11d04WNK5PR2Z53m_merJMc26P_4cNG_5LxaP56E4zGDPbjZIu7Cwr7HAAvEBCeFZlfMWTbJuZhLW4kGKN6MK5JQbfkzh_i80ck1NIcLLSvOsaaJUlblUtg1HKqY6UrQqzlEvqn_6ZrWrtHHwPoSE2FKE2FKBev4VzM5TsHfW6015yCpr7f2CwH3jJNJjDV416qIGPK6k8PgEH1K79_4FWG8fPGfTcxo487RGQjT-OsCj8qWtG6t3bbx7FBLfocrAKQ-d1ZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O6pY04de9gBAzq4HykLSqTPTiYzzXIOswKgbgZFm8YcajavPj8CrCHEGzFA-VGbW4EO_EdEjoSLNXnAxYG1wE6lxBSnf4zqUq77D5W2XivoupYOty5jkCAZD_Z8b0Dofdew96jilJm_bV-LrEBd7OmuhJJOHciA8J3I5tl7SKzgR3oFiC_6cbuU604jKsSytaMA-ZvidGg9oaNChcENQpc2bZ_wC_vLdH3DzcuxbABuu4MvkSSkavu94kPO-_7-Tohrw_29iqrD6vRnIThn3_wKWjzU5rfnTEd0oKokRFMXTNIUU7wcQo6pdUeTNLBP_wM_GS4K5ZR2dd8zQr1jUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=f8Udx-b9RbPyebov6OFRDejHTy0hvlnSlp_tlLxLZ4Ciq9V3xVSc25ITO9MwlBlT6mdZl8OWYNtfh9PXHv6bOupoObBOv0_kL1xNPpReqrdeZdTFk_-lwQ1-NtplqqN4Mv_PekEfjQV4x32_T9yfjUdbbp4PxQenCEGIMI3VSIlgYnEYuDWmqsE0sg4KkVyMObC-Mj-t6B6swjDqQqDf5P5FmwoAQrZBcctl4XuTRS7IEbRuv81rxgDTGdqxgVEA0ed82YL_Pdt3bkhLZLOhDbXojH4bezASSjVTloe3OJSMPzcTasPFOqKb2G5Q4Lr0Ed5KigmNXX0kM4lLPR-WTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=f8Udx-b9RbPyebov6OFRDejHTy0hvlnSlp_tlLxLZ4Ciq9V3xVSc25ITO9MwlBlT6mdZl8OWYNtfh9PXHv6bOupoObBOv0_kL1xNPpReqrdeZdTFk_-lwQ1-NtplqqN4Mv_PekEfjQV4x32_T9yfjUdbbp4PxQenCEGIMI3VSIlgYnEYuDWmqsE0sg4KkVyMObC-Mj-t6B6swjDqQqDf5P5FmwoAQrZBcctl4XuTRS7IEbRuv81rxgDTGdqxgVEA0ed82YL_Pdt3bkhLZLOhDbXojH4bezASSjVTloe3OJSMPzcTasPFOqKb2G5Q4Lr0Ed5KigmNXX0kM4lLPR-WTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ei_Z24fcXLyTu1nVVqs14TxhaOGhFW3VlGtOvUNqC5Ch4wjXQkpZkfD6BRYsHeM9Wr_m8YMrMPQYPn-EUz-M1oFm0e-MoNY59ByP2vypHEf0oj4FFwMSs95k5mdj9qE0RmFP-YDXwziOI6S1V4Ul9UrGhsMqwL9DFi_7VQTC7Azd2UBNIReLPHI6Tu2vC3qh2ha3lrW4yJrXlvxnQnMS0H1fBeWTCNP2phMqP1B_i72LXE59DqEcD3VZrzOVbjTPuyqNFB9h8z1SeksSqGQnb6K1etA4TMExjvrU4I6aQSG5yhJEOj4WWq0bMRWebN3MgPKfaxqA-dGf3Y53s4n1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gp_REQaBt7nwUUZpLpn8gpYPsMhSUaumQvotd0OVCadTzuCoQqxzfZivADElP8QUqL3cL6Wv4hSyAWnZMuRvVzsItxo61lA2P-wO2f71OBKcAL3ZWl1LnM4evmAUExSxBnCGWfQXkBjYTjF1ie6ZkDIoKgbjVch20wdaKn6sUVhkEdnzkZa6V2HtSGQjdgkVRjgOg7EPdHp_YdKTN5Qc7ZDUTiRYIO-TBqFueMD_OdOxFK_bsPKYwSAidyqW_h2H9y3IZxLBVzuWLnJbEOezswFhRgiRjWFjRMTsMdcsWIFopNJGvrmEUeHuN9JRRnLMKfs48fynmiJyie9sxUAGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oN2uVoqp_Kfsx6pbOvTWfdztM3A4l9gLr56JCOoKB_veKoLlL7V8L5r56zQRsqgJKzfGc7J85gqDIVnhEai5MqPdqKFjJXJG09moazaVKkjzaA3hwsvLQdpPz_4hN3pYc2qv_yFU_8EW9S7x89GT2G15qB6ECnoLg9bau5YO_iTt7roGqgh9ONIdx7pFCgtVE0ptxMRG8C-iBCS_bAbQH1A7uDtYCqGtwqeVX0cSl3E551DauhtFinBXyvohYyl8kjGCziXTroWcvN2mNjkqWA6LLHPo3_UxFxF_g7Ch0BhHpxIeSIHURA0v6dHmKlDB5myWyTtWSv5mMu7lbsYN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxAHVUNzT_ZhmTlalPp5WWpeyiYZUQU-yqGB_34R7m641HNviaRTPQhOsqT_s9r03g0RmfLOkRZuIk9owdesvv95blhp-7cyBS_J7_4D60LS9h8OPMC7y9Wv-X5eSc1_xWpdsvSR998gMw3giy9SWbRIS8lJcRfap5iUdPqknqsbBVkZPQM7B2rAG_wI6H-XVf6QXhbqUC6nyPbiF7yXy3XhW64OqX74kor0tQskZSLAuEfxcSGZxtXlN1qcpV21WcjgD8oS2LjuQPzsEBIWA4V9sb4CrlcxAbFrz_ALqb-elxyxpx3gYcS611xSqefrnUSuXG30F4mqJtgddW2QHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYwTVRwP_kMeeqhGtqlVv1irYdU140EyP3ImIvvvNgkHHimN3AKFAWIIFrJZ37y_OEMcQXznzO2UY0YbDxCKA-X2o1EGl5i8yKcFvEiQAHjwfT_KFKx_62IXaFq6jZaAuSiX5ttyIJk5II7IlnLOyuZQTOp8eUJsCnQxZMlxKjLu4Xs8kwewr-L0Joa9XkZcgg-toH3aY-rap3cyuRNhiy38-On11sXyKQRZZK7n_JCr_v743DXoYXZbod4KKvWm_uTm7yx4giNvu3EaQczqKoggjdbKpDohXq-k9YIKYj4vHnUNfltuDWspTpyN_755LuPkm7bfjtwESqiBtt26bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khnzWFCPdp2g3EMHL9lBrNCXZmHQ2lBB0fO_aJR3FHfAUXQy2jM7LfeCy9Oi_BebGIPVoNWhfpk0QyvEL2ftyfRhtGuXlzRCDMmxALsF5qW2PtLZ8-ZILy-HskWmk8s5btC2bHll7OO9IH-COOz9_5itgs-Rd_ADd2IncjIz3SIOYdBuH5X4SAm0Q_KEKEvuD0w1LRrzXqlx-q0u00oYLq3AhfHjOfF_bXhKGFU-1utid_Avn4l7ecPlkMLysIc9bjrBds4jgGfVY2MpkhBik0knGpTVvQYFY2prwCOgTQEv4DPluxVssCS_w-zVD0EJ7UOYrw5IE3jt0Di1fOIgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4HXtN7YlN7Zxw4qBxEsIcOaMkm8Im6dUcZFqZ-GhhufWw0_Fyu-czKSKL9U5NKtsE0P5r6LfKYaVBAwfzwCqEZlAlEVa4szQkIrwhKT3_GW8AhyswKW8NXye2FkvG9IpINe7bHpiQJ1wVUQyM6Ik9spkVXE8WeGlxV6VvFPR5xbXQ5POCjdU0XvWgcHCt9lRWvfRJkXnwW2glPySWw1-gbpVzvIMh7HoF9WVXDTVV5iR568i1lbGeEQzC-cwj3vCQNaCv5sU-jjEmbHsn4pozdehR1YEnyJiWHw6wW8nGVQHe1zxzWoqEnOBhdOkRsD_BO7ZE1bHiUCXqIYbHEOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tA9abc-FNasFvopbftX1zOf8kkSUiJ2tNb5BPeQH7tjT29FHtlkNygOrl0fgpn4RSO2ytE3Kn47XBcyFYQ-3ypNmSc8G78u9H1XkOGBWQTXbRIB010uzoVVgXcjjI5CoMAXV4VV2EOBJM_dg0BzuofDzPtPg3kYC2o2xIpmhZMje1_VpVCSpkM8IjP6r2Pl1rqmBa1DpFIuDml4kagUsOSP7znvysmEbDKDS8k9dCga4i1zm2IJm5uDFW_knADanVEcRDumXxm6u1qTjOpkHMjGWOVywfjwj0iV1EpS6t2S9ZViTG4FRHF2_muZF4L5v_mymkmoCRc6YM6NQ1Getfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WUe64A7xRA1TV0MYRP189DgA1VGy2nkuSGDyhrRl43XSmKOfSY6URm5LlOcILMSILmbrhOFEUo-8oM_Cbi-ZD6rvLoeAGvmHHLZPBwzCG9uvCRDWOGltPnxKUQOUbZOLIO81vnxQOt8iqTNWM1ZBhX-vcHaQtiN_2EjNGRtnyXhhsFLGuLcj_y3aEFkAouSTHUNQ-oD49Du8mv1Y5sJuJkkD5nhYggVSMB2zrg3UvdDNwfsOGpOhwNAXGmKPd59_HPBGytjWY6pxVA5xbbquIsNT40Hvl86KKV9zS7RL-1-WzW-p_bnIOLOQ4X3B1XY9VLKq22he5brtNfchUnpTJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-s-sd6I4YBbP0GEbXTAd59OQMQFPTmmmQQCJOkM8-rNioDcVE3k-5CuThyqSswaT3j9hPRFmmA-TLtg0TcOS05OyEcwBRiQSaH2CKHJC_aQpOd_yjux2O7ay57EXNG-_WWvPyB8ivHzwhJq4HrcM4iMSaE2lIT6L8uzZtc0gqm2Ri6DkQS_Tot6itRTKZVGxVGEyFy5QMirlrea2xrnUHvBwRn5QjL3j3EZuAuZ7POGuoc9iqOo1waKEJyP9-aFU5Veq6EiCPAsit32VKYR26RXAo-2yOUyBTTVtSY6mpq3BCJXKeVNKYz5f8dbxMdE5YBS-rcVV8hwC-Z3lf3nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ENOTL2wWHLBikNlYNWPnIVAEJC8NWP-MJCaBe9Vi_T39LG_lu2bdwXk9fmDLrrmFiHRR_6H99spoiqr7H8ydbJbQIbsFuuLDDzlWSH_M9LAHiDM0vTjOS0Mi5Bs5UduyC5AFbrrweQyq_9XF8lyOJetmLK4A0XeI9KLfkHvy6MHkN-UUm6yilxPsRPzD36xecLBW04xpRVDYFZtPsdZ-ofkYwBAq4Szee3e27gdQMzCGkY_gkRdXHErvvKoLRjSl5iTm3UN6N9HF7JODPrv3xh6NxPTci_Uf-j08eS8NinvwmU6fjr67JM7ztHjoZHeOSF_Ybm99hknxcEILXz4hLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=hAMyX96B72Lc8sFNrzbUiJo0h3BjjZcmys58s7BS_mMNCEdvM7kNH-9fgunimum7b8zMixEEbDPVTvP-KJtfCqg6gVGcrRgwA0QqCFGRlEgEd3rYE6nezD2mM1k_mpHgUny_lfa1ztvVAFOv493Q3i6uKLf_wXVPI08BusdMV6B-_ik8uprZXVEU7SnLAukh3a_exrQUGVyFPH-q0z_fQ7hnFYkB_TQEbxeCtxZYhMMX-Tkiit4ovDNpv_W8iiZlvDerl_Y-e2IxPEoIW2iQqlrmIx4ZjuU9seNcitSksCBaOUk0j7nCtG4HFbWvvHkYFQwE23ZGl70M2TkUL49lSg75nx3lhph9jFZkm4luAL4UdRlLAsnbhxy4is8XClnyHVS0SaGN7MX5EVoTX9ti6joY2dizySvSYfjR4A4efH3-cguD-CClr6bN1wPTTyBm0xxm67Zst41RRTOtOgh0bJbb3Ar8N3xkFpC2rOCBEuH2H9t8rX07-EGVZ25N6eIOz1Lfb6P0Fg-qg7u5yhKXzb-2UoGOL6h2aR82TgwoFeas9PPccf4D9GzrgLQgLzipfv-5Ks7rQB3Rj5xcLrMk0yk29MN_05T68dTqHtKYF-yRaKGW3TkpRdF8Gk9si6aiRtdmlwTt-IU5fHPIPIy15onXzqU-XTyttpbV68c4iZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=hAMyX96B72Lc8sFNrzbUiJo0h3BjjZcmys58s7BS_mMNCEdvM7kNH-9fgunimum7b8zMixEEbDPVTvP-KJtfCqg6gVGcrRgwA0QqCFGRlEgEd3rYE6nezD2mM1k_mpHgUny_lfa1ztvVAFOv493Q3i6uKLf_wXVPI08BusdMV6B-_ik8uprZXVEU7SnLAukh3a_exrQUGVyFPH-q0z_fQ7hnFYkB_TQEbxeCtxZYhMMX-Tkiit4ovDNpv_W8iiZlvDerl_Y-e2IxPEoIW2iQqlrmIx4ZjuU9seNcitSksCBaOUk0j7nCtG4HFbWvvHkYFQwE23ZGl70M2TkUL49lSg75nx3lhph9jFZkm4luAL4UdRlLAsnbhxy4is8XClnyHVS0SaGN7MX5EVoTX9ti6joY2dizySvSYfjR4A4efH3-cguD-CClr6bN1wPTTyBm0xxm67Zst41RRTOtOgh0bJbb3Ar8N3xkFpC2rOCBEuH2H9t8rX07-EGVZ25N6eIOz1Lfb6P0Fg-qg7u5yhKXzb-2UoGOL6h2aR82TgwoFeas9PPccf4D9GzrgLQgLzipfv-5Ks7rQB3Rj5xcLrMk0yk29MN_05T68dTqHtKYF-yRaKGW3TkpRdF8Gk9si6aiRtdmlwTt-IU5fHPIPIy15onXzqU-XTyttpbV68c4iZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K03lDWz2LuJ1CHMbsxvfRHeolmncens6i5am2nGZYFUYXjc_UPF99XXng_SqQQePfTmXla4VpIEF8JDgWwGg6XPvVhsACnjq-H7gRZjcYelHjLDNw_ojDDgOYPJsI1-hUgM7Mj0vzqyL8jWgf7WcYuO-1pT1NmrQrI9PYUlwbBlz_CSx9HyZOv1U6k7EXgtQSHD1nVgmnKPml_tktuy9SjiKEC6AQo6HBVQvHSRngYX-OVRXwD9_xBN8c2W800dqrwWG5KcQbOK8xSBSDzeEsq_m_0j7uD8RpDIb7_pIjj3h2feXkuccwbCFUB3-BSLrygVhYTB2tlXisF7ouP6kbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XTePZLKL2GLT3fuDqhgFtRCryQXKiXp0vE6XHTp_O_3QzM0AhHhx55_ji_PsJW5YcShFJk0LAkotfYggMeMNyKz0K8Xs_MJBd9JGan3JZhzxNFiNXcJeYisn-akQj4QLD4RQGyujJyJzjUE7s94G656ym_IrDEinBeMi1azCM9qFD0u2A9cn9V_SxDSbSR_-BmHpyW9NPF-6-I700rt-zx_K3jA6ESe5xq1emJ22DZgdIfA2PqsjAGhc1HbWFMlYhWuKNYI5PfAQtEkoJbFQfly0TmVgSqmBXms9orXSfe43HReuFt2B2UNo1oVooAsJl7IZEcFG6En83B07m0_Ysw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpRKW9AO56JUuJ72O-6dS8SGs2SP3YyG7gUri1O7NNphQKa9MF3sZL3uQd5m5UUbW3z9TTMERDbvxl0xq4869W11lF6kdxOwVW4OvuowOARY_BH7Uyc7dg-FcnrM0b_hnPvq0ru4quXWLH1oewGxVRM5CkhjqsdJOfSMdOgwg0c_zhQMseZN2AsCjnR482cYtvs64G33afqUF_TKPOoteVQTJQcbyZ_lnHc03Jk60I94RDU4pfjVhCJD6ni8L2l_ElhkOUuVUh8qrw8jLTB2XSM-BBQ_UrB0v_uXd4syiE0P4RTKXIYd39ul7Vl5TBRhG96Cr-ESIrcViwayD6eYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=d4sb0wDqOi9DYU_lscvMoDhcScYthjsW7-AEWSKM-AoD2fBUd19YuTT_TkxkfoMxc4JPNohd-u2v3o1P9Q9YoMhEvqJnILxaT6_ibb0-B2C4Nl7jGKvthjYK-LQ6AZPNgBkCynxAytIWQuVZR0kA0ldBGLQ-u2Sv4Kzcx8eOu2SZ6jOK3ZlrFF-gjUZh35NL0rpGJ-xQn4fAnJ4nUSsr5haKA8UJ_FraFWVLFKCaApBXrL1JVOG9AHeiszqEfaxbo-UivcT3LVdrqqfv8LGmJIQ43aTNE18JShpYaRevcQ51tcsNUpQDdSS-mxgGTyJENoS2qGu8RFkPvbodAi-5UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=d4sb0wDqOi9DYU_lscvMoDhcScYthjsW7-AEWSKM-AoD2fBUd19YuTT_TkxkfoMxc4JPNohd-u2v3o1P9Q9YoMhEvqJnILxaT6_ibb0-B2C4Nl7jGKvthjYK-LQ6AZPNgBkCynxAytIWQuVZR0kA0ldBGLQ-u2Sv4Kzcx8eOu2SZ6jOK3ZlrFF-gjUZh35NL0rpGJ-xQn4fAnJ4nUSsr5haKA8UJ_FraFWVLFKCaApBXrL1JVOG9AHeiszqEfaxbo-UivcT3LVdrqqfv8LGmJIQ43aTNE18JShpYaRevcQ51tcsNUpQDdSS-mxgGTyJENoS2qGu8RFkPvbodAi-5UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=VBZ-zhvaWosPsfJfYyd4LXrHUFzzjCsU15QglKbgT3XIRqZngiyWiXYdYnVNfqKxV3bJ7YQ7NQ0nO8JrFKqjQRMAw_LJ3B7YAZHOAvGlSfkNpNYNuMYzGNhsniOYjaUP4aMPKXKNkwud0hFVYEX-FZTq7_QC3cmKqxBYjMj0u_5m2wcNpIo1h2_0a_SBvIJUKd44hu6lR5wkoZNihh-5pxCebEVQnHOrhG20i_TQN1HzLoCi9FyJHkDBpjy4jhz53v-QDaVuib_ZtRMo9b_PIOVtjjNqjOAze0nPNuR3bWhPZh0nzvRhVMs41Yx8NzombtzRJbN3hP7Scv72ghliBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=VBZ-zhvaWosPsfJfYyd4LXrHUFzzjCsU15QglKbgT3XIRqZngiyWiXYdYnVNfqKxV3bJ7YQ7NQ0nO8JrFKqjQRMAw_LJ3B7YAZHOAvGlSfkNpNYNuMYzGNhsniOYjaUP4aMPKXKNkwud0hFVYEX-FZTq7_QC3cmKqxBYjMj0u_5m2wcNpIo1h2_0a_SBvIJUKd44hu6lR5wkoZNihh-5pxCebEVQnHOrhG20i_TQN1HzLoCi9FyJHkDBpjy4jhz53v-QDaVuib_ZtRMo9b_PIOVtjjNqjOAze0nPNuR3bWhPZh0nzvRhVMs41Yx8NzombtzRJbN3hP7Scv72ghliBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0PBTyQBreON2Gqn7XDFR92_fcORlSslzHyyhrODmhWS9FFDO0KsgqYw1in78-xP1J173chE7OtmuI4vePB18jYjk4_z08iLFGmQIxHNzoeOiw32FDDNbK6C7HfWOYqwX2yKEOFdxL2e4sD5UHHo9WnMnAiEWePab1EbwNv2lFV-vpQxNT-7i3lQwyHyi4xd-IULNDbRjgLKW2OBtEw6aWYJmhp5Sr1QV98UIuFq9vMdfO47e2QRqnb-umC4kxL8-5ZqBELED-aozlXWS-_icyAVpkcqVMVY-nfa3FZhn5U4GEZpbAr6NbimgafSnCRng38Dk6CSkwejLLJbpZhU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5xZhPm5LEfx5s5A2KYoW-n6CYmispxxtYB-B-JS5_y0eqUNy0MzLB0z_aV4RJN7lHi66QdBXYjiJiYSZw_bx_Gr4xfXSu7Tt3PoMzPz_BZRHLvLrjraKWHh7eIKE8y9X08VuH8fMWqMFRMhkCbUm6Kt-E0Z8dnsvgwgOFYFjCFvVRjIB0Es0-k_Yu-zTFJjXDRUXzFA9uSYz6G2bvZblxHGEcjb2oCU1hu0bMWFAXBTkjFP136T_FRcwSyPzNsz2APSGJK2tkOjIHv6UAxsaNxt_7s8EelgSwyVSFYx22kR-IVSGOt_dxOucZzYwBRm86LRhdEPyqACEUl90ip2VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDe_zHHNYyLkY4zmdlEXlfD_yyY4WFOgYMzzpZDFTTCO06lfakNPi71aMqEN9jlo00jlAFnXEMN4CRevrzbbxese6RVmKCPsjxasuQIS7_B1wiiECuM6dZ1IbqCD2I7GfpIaBvIWrhb4uh-orgT94mRpX9GGD9pn2IPgmPWVHqiogpj7q2RQ2ROTm_F3GhOc8cIprQuwbXeAzQZ1G4BYWBEEKRG7YbKi5rSuojYLSwoiCgEnF-9wcnWnmarDkUswtGIgXjA7vSMZfFtCxsKNYgumiOs99lqayAflFVBBgnULlOzFKFAAFSaq2SUEliihX5ya2oeCsdNVhgusazsl4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=YbkIQDtRsJzO2Ij1jm0yLGxSkQ-2eUYhaSYytN5lVcMhIHjMDlDBvluHsp9KMx228zaE5vRW6DjdkwqRqPH9EcdUr0_SIWRc3mfrsNeKn0y8fGbhUR3DHyEe7nJGPDGmnxvu_dHtU9RhNXNH1Tf_BiZoWPvoIgB15Mclk3-NGGQTDlS9Fz0GKG9fQxSjnrsd9jOpEVTDLfWzlbU2BQKJqTBq2e18cLl0zhGmtvk8v_XKdhUhp9iv6ZVqwJAXpy1l4lrmfcIr70h_Ct1S6QRfTmYv9ripQwcKuB6WaFSbX5CUVLkL6hO6CB0Rl7gCbCd9hpMNiVhjdC6KugfvcOx96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=YbkIQDtRsJzO2Ij1jm0yLGxSkQ-2eUYhaSYytN5lVcMhIHjMDlDBvluHsp9KMx228zaE5vRW6DjdkwqRqPH9EcdUr0_SIWRc3mfrsNeKn0y8fGbhUR3DHyEe7nJGPDGmnxvu_dHtU9RhNXNH1Tf_BiZoWPvoIgB15Mclk3-NGGQTDlS9Fz0GKG9fQxSjnrsd9jOpEVTDLfWzlbU2BQKJqTBq2e18cLl0zhGmtvk8v_XKdhUhp9iv6ZVqwJAXpy1l4lrmfcIr70h_Ct1S6QRfTmYv9ripQwcKuB6WaFSbX5CUVLkL6hO6CB0Rl7gCbCd9hpMNiVhjdC6KugfvcOx96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z_inidN0gBXVqR1hK7qQAfRUcXGvGoKJYmGhCli4LjA7pxjvx0ukZvMdBLsfod3XDV37fcvun-9CXJUyfO_TGXIdpIEPsVa2Sv5qwlhdqaX47u6Zd2FoZkewcL-V8gGJeca3xfGZpan1A1fJa6jzCK-0ejCI-K3ZavY_dI5KiXmqoZNsrJttVFpJoLsYpGhShS2h_9lBJLLrpDw9gzkz8hssDtMIBDK3AbivOW0rF_y1xzkZOvb4KQmnhcZI0BbGdS3KXqZejYQlIDch52V03yZwqwQTK0ipQfVh_6TYs_K8DuJ3B6dUhL5ga7ZIk0dq_FXiUAgK7RYh_31AvaMrgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dtm3xe-SJQu-G55-nqgcWmq90z-UELdW7px996N6JfzjAn4iq3dOSOcvEeLeyJtf63AP3iOrsqIjWlvGiVniAGIaxNtZs8tRzgWjg66qfZ_KWGWHAOgl2WbmTohBb39D-T61q2v_wruFISbwkoWmnplGBM5EChra1jvcqssbCnq8o_d48T3cv6bfzA8Y7t4LF9bTf2rI8QvEVfOfwTOCsy3s5bG7WvDjr5IEJqozOeAjpwu5JqR-Z_ASJT8Do54Mw-PZlF9mK8kodQFjYvY-L01iEvLy1Qp2839rfWPYnCiIsT6hSPy4VVhB6_xmEs9HvNSltodxAlKKjVf-ysAOLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=CWceghS2W77DAwP00h5MyCj3JZxG-bGQYm2PAOBauZozA7Y7bizcYHdrHFBz0wTcqbpjRYYXV_Q9GyZrDM03RYk6F7zps1du1ULzaxnzDUn0sY02eiQN2BQo_0IyslcZ1CnuXkLGV8pcJE-YN14pb_Boyny6imuGO1urDDeaz290rByKTC61jD5oTjcKsY0MDSy6lGOVecMC0FVZ-S7_x1bNxRpD46rNLPLe7SxSlL0GY6ShBSsdjKxENw9F2RzMfQj4ZHk9Ckuj4FPyhHtLY0xpDtcDV25S3aqTAbzF1cwelfvGfBgOuopL7HdnFpuZQajWljZZBaWkKunkVMxiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=CWceghS2W77DAwP00h5MyCj3JZxG-bGQYm2PAOBauZozA7Y7bizcYHdrHFBz0wTcqbpjRYYXV_Q9GyZrDM03RYk6F7zps1du1ULzaxnzDUn0sY02eiQN2BQo_0IyslcZ1CnuXkLGV8pcJE-YN14pb_Boyny6imuGO1urDDeaz290rByKTC61jD5oTjcKsY0MDSy6lGOVecMC0FVZ-S7_x1bNxRpD46rNLPLe7SxSlL0GY6ShBSsdjKxENw9F2RzMfQj4ZHk9Ckuj4FPyhHtLY0xpDtcDV25S3aqTAbzF1cwelfvGfBgOuopL7HdnFpuZQajWljZZBaWkKunkVMxiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOU85KpXy4LlZ9JQ2mWTzvHCz4yNLkKu8OjXXsyQOMEGFMGHMbnFag-OJn2sPx1KNCHHXcdWP9oNCSVar1xR_ZAEP3WqmYuJK99ThrbigTsV-oLiXCIBa3dmYbRPwT06DudQ_ba3WgYBaAX34UqaMpfmpWy3sb_42GE1mOBxNouSLbfczCqzq00f814C16fqYTwDonDzikC69ckKbD7auVv6-U_tMnjmGxJ56HDUKtfRxq3YJb-ESgEruePRYQi0Lm71PlGtAil41BjFCmwaOyHAgDKT8s7theE-tTvVlReHyNHyO308zxohXMIjiS6zimZSZBPjcBr2NRWU_hFYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C-AKCnvHvB7kvnsQGdl2iPigxX6MHKySsgiwTX2T0ZwPnK9XylRaD2-28lIv8aOcb1rHAGBZMMbc6vABE4tappjBNSivvu2J-UNbp_AMrWJJHrXEkbPZMn6WEH4P_gqG9VxJ5eC_OjAZ4uxyw0i1g80pdeXUkhITgCnkIICHzP44RsJaRFMRmc3y8bFDOVxmHQxxcQCE4bkaeCPXdLNmxue6FHwqG_IDvaNNBq2kbx9x0qAISgCeqIwvF7y8I03-jO1_QlUjGLybbpGg5somqi2fK-PhKZkfOH7hFopRpkwJL18taNfMsm7Kd8koN0MOKWU8aXZDsrCmbO_PNMeVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HyryYtGIHA8uLtaI5wCIKws2kFJLpB2DnLWfKTX4tigga7hVCQ7xd-i6GyhsikiEj-9GDSC47AiERhN1VMV6k_PGpMWsw7PNSHfgIWKQHwoqW6dyZiyeZKzEGvq0OK2ePWz8eveitaZXevYAgBU5MOMBxWFcPMIFyx3uISE_mMN6HsxcCnpycLxHqPTUzEEWr_QAasFzB2ryACB_L5_z3_7ujcFLzaW6pM_cgqaO_nlv2OtTjLAJXiBvdCDjUjDbOwtE8eGgVAZVUxs9bEQtM8i-Ts5z4Jp-D1qenfP823pSLkVFhXFDdphH5Nkl142mS96E0Dq2NXW93WzRcz4qWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZwlOIowj74GbyyNE64wR93LDLdMGclXIE850VVObUPdg3345GpILFKUn-ahHKYrgwS-zMb2r0p_aAsHBEC-6ajqdVTR2w6PBZH9Oe2mFUx8cII0IqxHQIrfC5yXTJXHf7BfIQ_dVnilD9xalb9WxDUapNB8DA1qBlfohgKXdbPbDDOgSlC_bIlUuZnZ5u0a9TyNgT5qdtTwGmv10v700Lj6px8OEQjwVQ4Bvw9VASzmc14YxvpyX73hX8ZMMdIAUGCSQzITQoA3bWLVNQCRbotUqbaXUiKBeX7HGAqKQnUKMGINUm0A-VkOwaaW-Apy1abKQ74dUKXeekFlXOuNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=Jr5v8dG0Dr5ybHBlLdoeV6rSewZj2ceM5TrDAniz1RlQd_xtEBUfJ1Nqz_swTzKxLs7h6IgXD5lxblVwBU4xpv0SLxvgRS0WazNKEDzYjW9Bg0mgVefTYI1QMVIi-MJ38fZnOISYBs2otCPFZffSQ88Tc8zCvscoNK-z_uJBZ-SXycBd54HWjRZ2ftT7ev82RdBurD_sAgkLgQpwpcnEbHBB0lQ8Fo0J-dmWn3HkIZ_X0g1jJcMairKSwos6R2sNOkFPG1uescu0G-AKTnWG77bLqSbh2F8nqOKH5xN5PGF-E8I2PVpIZwAqFqqerOXfrWvyaxOGj0D3splLStMiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=Jr5v8dG0Dr5ybHBlLdoeV6rSewZj2ceM5TrDAniz1RlQd_xtEBUfJ1Nqz_swTzKxLs7h6IgXD5lxblVwBU4xpv0SLxvgRS0WazNKEDzYjW9Bg0mgVefTYI1QMVIi-MJ38fZnOISYBs2otCPFZffSQ88Tc8zCvscoNK-z_uJBZ-SXycBd54HWjRZ2ftT7ev82RdBurD_sAgkLgQpwpcnEbHBB0lQ8Fo0J-dmWn3HkIZ_X0g1jJcMairKSwos6R2sNOkFPG1uescu0G-AKTnWG77bLqSbh2F8nqOKH5xN5PGF-E8I2PVpIZwAqFqqerOXfrWvyaxOGj0D3splLStMiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d18QfgEUKnt3UnOp9nCY3JwqL4gcdzpbHbuNALi0gcD-mfQSYmCGRL485h_5t1ggg9Er366y52E7mWMdvcSrdgFkZMSCslXyHfwiCYzxcctgKFClXrBbgmpqcXdc8zm2dgQAQ3nOXwhyKWkGFZiPFE4Kgz1yUjxEp2F13F92Hn7Z-E-iEaL0zjEjQOyw78mdnSjmE4NtnHVIOywHvuyLN1z6rUp19pIBIxUDr5amAxbfhyJyOCbbxSnLgOSWzQpPMegdGYkLvoDjmIITWAraDGdv0Akpnu38O5D4RH_W4RP5WnggGi9aPiS5MycQJfy3yToIaY6QQzuiUfOvkcNHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=b1ej-MQdZr9dSIqnOpkWAPxXoew30MXyuxB7R3iJIopScpmn-z1IbbKOGeh51_KbJrPTPfbNAayG3f6fCRohNZ6vrBEai9gNt3ZfpE7F5w22t2zi1bQAHxnQTEqmTvuCkp3SZj3f3h4BCT1ldowJrfvJXyLEU_vV5BiT_AabchrhPYDVujT7x8ZXUAUrWPfQJsUbMk_UCbCW3FourEb-OIFYY1S0jTFvmMsGH-ihYRokzRYb5Fl5AZ0FczZGIgkC1Cb-il-KNQNME8PHeq3K2682Bk1D0C_Mv-NH_LvgbBqLKrS-DosiLHVAHJedTbdwxM4lK91SkC4ZNZtPm-Z7Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=b1ej-MQdZr9dSIqnOpkWAPxXoew30MXyuxB7R3iJIopScpmn-z1IbbKOGeh51_KbJrPTPfbNAayG3f6fCRohNZ6vrBEai9gNt3ZfpE7F5w22t2zi1bQAHxnQTEqmTvuCkp3SZj3f3h4BCT1ldowJrfvJXyLEU_vV5BiT_AabchrhPYDVujT7x8ZXUAUrWPfQJsUbMk_UCbCW3FourEb-OIFYY1S0jTFvmMsGH-ihYRokzRYb5Fl5AZ0FczZGIgkC1Cb-il-KNQNME8PHeq3K2682Bk1D0C_Mv-NH_LvgbBqLKrS-DosiLHVAHJedTbdwxM4lK91SkC4ZNZtPm-Z7Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke9kZrx6UlELocPVZvEuPjFfv6Dp_OQTVZGwkcYX_apfcOEBvaO4A3Bc9xeQmsfFsds5Y6WkqHy0TSc1iPeMHDsAjg2hHZGfdFfNgDnVH_2NZAmGBXh0Q8afl4Po6lz5n4NOpuRnqzm37M4gbEHKHr-Nb7GrHTc4s2PsxKFtIMl_am49M8jXrt0lmjmRLUo8XOvL9q4dkbCucdFjjyrPHXLfrFQTWAPC4JqSejscCfb0sthZKTBIKHePVY0kl4F0sBRrQ2h7hptLpMpcIaVY37qbcsP8VD87RQpmZRQFZBcMegcd8GRBguf1M9It07xGaPjvrghwbVBowVVRXMOD1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAW2zkOz45ZZ3nO6vwZiQD7YcTVc5btA25oTE8pBBC9clUjUQo5QPf-1NH-4cvfnN-PcPCNE9fVlX9devYsXHd0uynpNAHmuEctNOxpYbk6GbgKi9KC4YsE6ajX55MzLg5RseBJqYunlBLSmdQB8_p26MbRgaAaT4Ugh5C4ONo1Pkb1PVHzVnLiy2gwEbGtaCwjcC1pTUilf1ZFUon4-mgKFFVHDfjawYFDyzPACzDR0CyvRt_5qBA0kig7iYEYhkums8CAPoXMHnhlVAlPnEQJKZK-1CVKH-AEMmNnNt8cbiuzV5IGI1BFyl0f4Q8Na2y2_BVctjD8i3JSOCb58bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upFRL7MF_eJMZMvLp48QH3LCC6z6TOg8Vyp-SgRQ_gkG77vN32gssjo5Kso4bz2uJFA1nNRu49LLRkae-WeWzv2D8pU2jU2c5JZYPs4-O6-3DC2Z8LCd6ewG_YWeZVR9CvNQajoQqHdZfXkuw1RxTOiGIjpaT_tSISJnZYsrbN4WtQfbKwJm58aOxsxqPltgaGYB-fXhBnXbjUqqpwx9Y6v-N8xJQLnPTLIOo4ml4OdvqdiwSt9MllUw5KEwWTkSDbQoCJnpRtQtG1SRdj9m0-PWcCTfe0sGEHitfQq9k4ryamK0NehklShUF5rcRmzlXwUZaZc8cJxZbrjrpXFygw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P2wL3t9ppb1WGguokMYYk-X9qUej490RZWoIdXSlqsfvetjHd87tkHv2G03Z30Xwm2Vatu-xfGF99tmRLkdjV73RIecdIoWh1ISMOdBo5PPiVZBTBZmPh8mtfkjmG8jpbRU2N3g0T_799b_Gpolw2onIUj8me6Zp9AX5JogQj7JqUCRDkuyuAtoADqcVIvTHkQmMdLkj9kvGcyTKiPgSG_sPtIdO6F-jRsBQBlneWzG1j6fflFO12O2OyjFnmOqqDG8L3euLdAoXAVn9bWcr5De0rRazaK7Y_PTAmZB-Ra_-OwwzhTuvD2BE7LfolcGwJfwHsKeK2hLkb21-dBg0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT6VUvXfuogCrlXIgnxEL7TNQLhpBzq_H_cGv3mIDobTUTLZAXx3_-vCljqPjcAyxsYsh1r69rD3Skxnw7-K7_6TgZh4Cj4x3DNlKQHYCF76LJzTlUj8x9b2tPbQngmIG0VgRZmejr7WEXr18ePltQ_ILIRgRZIoQV5BUQNqBocl0SrSupiqvNjxn05a55Cs6QuGswRayxyVa8_Y0Lb2xV-1Hmll5kivtonE-HVlrQxj1pBCCllTH76Laq058AvL9U0ZD9xyacsCqtxdw_jNxsuKcmOpybcYPr13Rt0SFgZc412LL738MVbj38tP6WEtBWBm8o-BQyDbahLQ53MI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdbfeTj2OKVvmnQ7288PLUwpK5YjWaI8b7RWo0-dep5DeVazsQAkkSQrsQjh7bl6RmAB2cgKpLfTO-9QJAc1pFnrSrWv3jGjw9cIFG189IYNKSSQQs0wMdof5-wCWwk_dYbh74wQpyQvPobQiNE7-FypfPkErrxBNkG9S2zFQpV9OmViiCIREcn9flk3-Nz8TFfwCZPaxGEa_2qsroXKhKZh_Gl2UWZJRe9LMdZY-YxWNsxjRpoHE2E37ymFzZLdJY0jGbDErIWISMTQXEmCZVM4nAnfiA3AU9UKM6FfjriLLRWm8ooIXmsO2RPjWOmX9kbXQIeQPAN61SAplkpnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZaXPOYZ2S1MLtRrPfynMG31NIkJ-zeaXqQx2lO88B8Sx-E4Kdy-KIP4WaqorfIMdpFyeqUBgDTpbttAyssf3DL5uWGp1pkVgP9UNxxIcC0kJt82bE3CQ8Yjn6t3_GnxVUz4Q3C8GjRGKKfZv6PmPCxE8u6EoJuz0CO5kOjk5G2cVyFOLv13FNatTBvXt3kgV7zB3x0pnRBRzyxpnWmmzIx9x1-fj8IY6rRVeeqDe0r_28ZYcX8PAgylUUatlVhM3blPqM8SQrfLChd1zXV3y1EAmVcOLyWyly4Ns8B3HYrmd6VI2pcT6YRsF5BG99ZIpjsLUJaPTYVMhPOsjvQ6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzVaggUl-nNWR1SGbXt3zMsQo9D0rZ5BpuBorx07WUmqwGm-QIPJjvVD-j9GEE-bfkPEYtCr6Jj7XoyJws1XgMASZftxz_sa8aqKU5XpNBTYyI9GzvH7O1KylBIhNeVc0j845EMZqIYvwVyhySjXo3WwkRQJuUEQXBlLIKhJV8_PCkEuPzsBWrJblNDjNKB_7xbFotqxW5jiu_rNJwPqNpM8vkfux4PL7nhFwIy10wzqcy2cTQ4ptPaOsHx4R6WDrsv6ttR9aksxfgZul6JDSQf4uuLV8vN_dl-iiNTwyoB5cO0-sKfrlCkM6eD0nou6NJkC7z7MNek4ZE03kgZgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwghPJz0tuowboR2J04xnoWZvT0KZLomXkB3I_5eV03zLoO2Mm90h7HjFDb4Q4u9I_xLjRQpToBOFgyHdceduoc-pgtrsX3CouwTv9B4ueK7RRDFoSIUgwWVX7-WpTJlamWSh2aLQ0hxopNv-AvsD2f82XOJnz5xMtxog_9GrGbVnc34BKTQ0gr0ugq8cDJCG5kEYwBzHeQ6ySnnh0h009L1DIv-jld3uLOvBB1yA0SQVod5fTCghzBBPmf1WhoDB1ewSDoJgOcG3sbsZ2tXgA365yjquXERQm1txnyZlQPkoZnQU9zfL2i-Crf7Wymoz1Pex2iZ8IfFUTPw2YfoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLFXzzBHRLjcuYquvcVSxmRbyoyDk14hZR_gdm87LlCOpyPHnweLTxA_6CjpPeCHwn8Khe-Kv7CXAc5oGMnxZoMEVwfwqtWXEm80HiDTLdIy_WZkKMTbHaQDoMvzjr6vHNguqVDMfrn9xJscdfgLrayVoGufHFBH-W5rALP2wVNQi4TIiyP2UhxyM61DPT7oR1F16e94lzRn8Mc3V4F1QyxGZJfH5QHJ1Vx57zmuyJVR5ViAFJx_YWitJNZZQjDiy-hi1eqtAg81ZXxIJsVOeq7jdVPHBjzwQxruY4nh68sR-AFxF3ru26dQBBfAQpTzMQlDE4h2M24kqRFUKHhQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9RZ_mv_rCN3iN9mRg6pN9mYG5hYsNwxcNApzP2ow4HiMqZQ8iAm57XGzFLMeJcsOKqHV3aA4Ut2l4ISzcB7y7A0KI1XxfTFIhVxG1J0zwK_NL3zgXZ7i7icc7e9Z1MzbVmr18ZsbThSnpboYNS8SLosEndiNZF1zrl2Bh9fyLGYDIwUWg4vPlatzqNuSXK1Qul-xHGY5SuRjIif-raxtIAiNzfCpTdWsDdLLasaqmV5YoV75PoMTYX3mwtYCq8T4V3Qk9grdhUYAbwDF1ayOeG0kk8igmOBwhRKrsjJKZ7_fpHVRPrmVWaBhd4FO_LuGLWgY9jCqY_3izO6PGPS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT3i-uOkrwHvdTg0gJjbQ5hkaPNeDB6ZRl_0bEtnkldt-J2l3fzdwMrcFZn30yT8smXlaFp3tc--C7hvPW-UBxX9RcF_gaDA_mxydYKP9W0HIn704_p6C7N1q60S2Ysqlvys-E3aKf71repzLN_wTv4s3TlkEGdVzVlkeiTy73qX6jICJufnVF0Nl-ShWGsq_EXvEezECI8X0QGmyhUCJXllaeVnawOf9y-w5dWp6YGlH43t6t-cBChYacx2QxPikr4JsoKf3G5ne_SidtSEHXVvsiJ0WlMYqJx3mrWrIp2XVC1l9T0iDsZSCoF3w0nEB-SeF3hOobCrsuMvYocvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=nirfP-6rK4WkGMzfMOHX2VtKWUzzPiyRmmaaNmLBB-vvH5NqQ6vMjlnN9CKHbK1ivx-q6JoDbEYJYDEoSy0PbHHtuikSJgnCVTQP9xpLJAaAvBOJLp1eggnGxelTTPIqXwaeyvSZO5qWqee3b0CL9P7vpOvvHVJUCcCceEgiiTD4JABVzzp9ZaJIMm7lgaga88KwDjmtCDYv1spzLwhQSfMR62Z6qUg9DwRBbbxn4pptyfRuw19H7UhD1RM-ZzjdPeghjqHWU3RrWFItnJ4jUIt5_o0BcaXSPUTGqOsEUW4J8A8nkEOLM4wJ5wYgQpleJtYqR5vV80yFQ6hWJ_RL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=nirfP-6rK4WkGMzfMOHX2VtKWUzzPiyRmmaaNmLBB-vvH5NqQ6vMjlnN9CKHbK1ivx-q6JoDbEYJYDEoSy0PbHHtuikSJgnCVTQP9xpLJAaAvBOJLp1eggnGxelTTPIqXwaeyvSZO5qWqee3b0CL9P7vpOvvHVJUCcCceEgiiTD4JABVzzp9ZaJIMm7lgaga88KwDjmtCDYv1spzLwhQSfMR62Z6qUg9DwRBbbxn4pptyfRuw19H7UhD1RM-ZzjdPeghjqHWU3RrWFItnJ4jUIt5_o0BcaXSPUTGqOsEUW4J8A8nkEOLM4wJ5wYgQpleJtYqR5vV80yFQ6hWJ_RL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuWKLe0Odq0p1XP0EiyPTErNl1hgzHwkmbnwDZdIL7PUsHa5ghH_YZU-qKEDcSAQHYeo_-2rXeceuP3EJvQugLmFp2eO_pVQ8Y0HYp0gt4jPQNEAYP1K0FGxM_CxMGv1o2KS1T8-UakjK1ihMRBzOYpdCN6E7BC6aoMFBRkvkXgrDbzvcUh9IGRr1PE9QKy69CqNEanu1Ytfz3CSEUJtwbRaq9GyE6qAUvawa90jSqhNSGE1225gT8edVhlhDjYQdLODK9KUBZ_4y_x0-h-f7exTS9uhM_q4OckMsHmwmWMe7GQk6zHR18dkX8JaB0zMXjG8vqInzmUBPN-Gxd-Pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=v29i9OB73vykq_IGqMXoB_Tg6ZWD7Q1Eh4SVX1n0DFlLXzbAzlOg6kviYrzblAvR-ZRFLDXdQX7lpoVcmy4AZ55jaM5KwO1pxKCAnbAJoi-kQjS7BkRj1N5txhaYfJp_CmvcfsnN1BPeoIKqHqHRMEgYd7hancL9cS6suSTG0CwhzLiAAJcNdbvGAHZJYFgfjQn0kyHcxnlipYpM7vkxqrQiQD8Dlgvu6ij7B15IkSaozP3-UudMGNLYfVd5Og39CAo49xqpTsI3wHt3sZIeiwXXdth0O27JyNZualEhJ-09y88lqM78f7hCMeJ4Y8HqXuN7Y7bdix2xA6BVJLZ7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=v29i9OB73vykq_IGqMXoB_Tg6ZWD7Q1Eh4SVX1n0DFlLXzbAzlOg6kviYrzblAvR-ZRFLDXdQX7lpoVcmy4AZ55jaM5KwO1pxKCAnbAJoi-kQjS7BkRj1N5txhaYfJp_CmvcfsnN1BPeoIKqHqHRMEgYd7hancL9cS6suSTG0CwhzLiAAJcNdbvGAHZJYFgfjQn0kyHcxnlipYpM7vkxqrQiQD8Dlgvu6ij7B15IkSaozP3-UudMGNLYfVd5Og39CAo49xqpTsI3wHt3sZIeiwXXdth0O27JyNZualEhJ-09y88lqM78f7hCMeJ4Y8HqXuN7Y7bdix2xA6BVJLZ7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcFO-Kfxr5eoEFDDOsv8KOELUgozGHFWCG0smD57YJHMHsnzfE5rslCuKVsaXYazKGHR4eJzMS4RDph6h1K98TijbaiapHKzqgfa7neJG4tQDic-gZcLvjMlA0gL4RyraB-MM3jf6GvsbIU343kOTezY2aqU46_VvQe8-yo_MX0oc_fb1S5HCChowlS1Om1p9F7pfORc2PiwnB0nbhDHeStUMamrNgKidgNMteFsZzieGRrmgQkpgMJIBevP8L7juqDiWDwc68RSkXe_iRaqPICmrLH8g7ZcEWwb6fPfWYN1NfrnQPd0zdEKRcD2HgciFWaastipL4mxIP_bZZWQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw6sWj_WBe1a48WH3K_uPUPe3BQokmWX-mjvECrnVchTBlrkN_V7_ePoJYnkPqhJKbIzpdYykJacoi02Stc-AgiN7zubOW1FcL7qq5hwKcBi6Lr8v9kgBUbVB_wWK1EwwDY5YrZU40PkCLV6__gVtOIlF4-bnLDrwpaMjzV7u6sHuhlOuAen7QBXK0l3s8rUW0A3sUyt7bafW45JDnJMXUUa_sG2mTxXHTopbMbfholtvVc8RWpgKa3wy9lcdMRIuyanlwYufe0fXcocXYoz-tHR9sPbU06GKYkOK92YgtjkDLFoWhhFEBOwkkEsauKRtHUJEGPllWjAkCVXy_C_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etTtn_WzqqJLXaUvDDH5S9pxI6ixTHg0nTDV1h8P-rM3y6qhs1GhDGtxkvesZOTHBFnlea6RFuBT4yt1VuZ9PalepCz0MPywqb1CVp99CXUAh_JgfLplIAiibz3SDFv2ex6JBq7dpCUpHDeOv1utJAmuSKrXhRzX7ZxKGpjhs_U10BAlH8krGAIriIfCsRo96puqDXJOmv_JNcgsjGZ-PbLVM8-7syinuTDrtI-1WPZKqYOkn3youOMDWu30V0QKhgjbCwTOOwt9G-3epMb6sbjhQYOVmAvhXmxBb6ZgXz82vMw9lF28JGAZuWHSLHdGcW1T55HVpjqsz4j4FfKelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJX9w0SXIowZJO5DK0csDVGHCpHKcTlY6-lBT6sW6SXCEum6R_SaromUx2CzgdaiCBoMgujEtLIwmIWX1EUnZEB0reQ9GLhwUJfTyeKOy0IjeM6VJ57Yd4lX6itMlS9B1QB5yYGPOZAfkV3380V_1za9TC7YLXSO0rEGrG79zxtnFvujwwd_kzTwYRJZtYqYrKnLjZmhRAxBoNFoh89A1ssw8j-d99lA76zl9iIYLe6IVg23cV5kBNCe5pPJd9PKsjYOB2jnZMP5r_av5wfIixYSCUHvqj4_W8IXp9tBiyipVjRGYOtC5rSac0K5W_5sT-Zq3yEGItuIhW3aM0oEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX6eBfAaIDWDbxLg7mSUJyKw4KQ94mQsXsPhU2Emfsdsii8UY5BbEMAtS4yfpeJyOsqhPGRQcAJoE7n7nZqtt_svGfSYQKbkUEPCG_T8ZmQA01muefPnIzV8na-ZlaEY1ze-_bnVvAkU5ePNPA4tyc9kKQdd-UsRywbVTownHs5ZsynAOxhEI50yUsz6a58hwvfRFCF3jnFgg8nW8QuUwFDmtiVK9P6v-tPn9UgaHEMeVsIXHDXklaUJ94aSyitfMSAU7lokwsyxXVbT4YfhJK_ThDo4oW0VQXLQXMvHoFXrH4VPyop3Te2TuDn0KdO9KkNZIwJFIM4tZzHIRBi-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zj0qJumaUb7uME_pc8I6Vz6C1FwTr9mJRsBb8d51dUD-O-peoz1UOYkg-6Jnc2RApZlJLu-PAeYiqW5--NyvwZiFxQHKOa8rfQ4LGE-6JZMVFiuxFlvepmyLddjuUeMj59NMY11b38A-yn-yNjDGc47c2jA1ovnOlPc-GJKmHWqDyWMAoNlcyGUl_AclDNBtBdMuVqCU9eMylTesCbF4FFqmufnCtnxwvFF0rEgJohKi4lttsL97v8o0Z9x1bpsfhtLm1VMIOM3gcTMFpEvtVA5t3kn6k1TPiyNcNhvTGwf60toAuwpr_Z6e8_UxQfI3WmgST0JBtgKoBttfolEs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=kAJWw2RHCejaYCQnE1TuFxVvi08e-kixacdOayG2lbSIxNg4McLh4pIYuNfOvlXCi0iW-6fjis9SF7KlhQ0F5_81K4c4Vf5zTshdXL5NofoNHj2povJH27WR7tbRfDisZOGDNK7AlTwpq6j9Mw0-rm5GCquu-o_mySqr2lqA0kxEm6Ah5qKxcPcrLOLXluPF79nnLGGLQJzuxG0URM6MGqemDYQQxh7y4LU7losRaTvq8mv6XOXCf5Vg7CHnhKQ5fXkZSeBLp6OecKTuzXtjcisEs7t8uv03kUD3JN2aRxgtN-vUoSIU0VNOyxlN740Tj6eXLXF5ohcLti6j-8HKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=kAJWw2RHCejaYCQnE1TuFxVvi08e-kixacdOayG2lbSIxNg4McLh4pIYuNfOvlXCi0iW-6fjis9SF7KlhQ0F5_81K4c4Vf5zTshdXL5NofoNHj2povJH27WR7tbRfDisZOGDNK7AlTwpq6j9Mw0-rm5GCquu-o_mySqr2lqA0kxEm6Ah5qKxcPcrLOLXluPF79nnLGGLQJzuxG0URM6MGqemDYQQxh7y4LU7losRaTvq8mv6XOXCf5Vg7CHnhKQ5fXkZSeBLp6OecKTuzXtjcisEs7t8uv03kUD3JN2aRxgtN-vUoSIU0VNOyxlN740Tj6eXLXF5ohcLti6j-8HKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WF7YeaoNwc2D8wQpfx85dwOP27XDGLLG5I4RjWu4WGExBB5nAso-B2rlEqB13KEn45PXZZ82BCAHEoPI4T7RWdJEOsYV78Extfx5RnpkOOeITazojb8icW89aUx9qIWrJTTzU6iQVFdusYzspwPnCTGRqhmxbdiy4CaT2uURxrHEe984o83mn1E-wMgLmYVSpGmB_MTVpqBoyPz_JHRvpqmmqBANyGL-NvwJPQbIC91_VBYuDIGU_zSQY4TSwEvTg3w_pYytpOHWnKb4mlEdtK_0cGrt9dgNeSd0utXecNKR-4U73FDr6YW_w31lvyMXNmKCCZom19PIfdGa4GbYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=JBSfGDvpCcKo_wyf0RbgWVn4JShyK2qHrmHrgIxR-v1ruXJBiu7XJlIMd2M5hC1UFAZL5HV-BqnXACrtogO5mbO1G2AbCF91BNB4aOzyyzTt9uoVqVX-OK5IAVfU_IbKHRYGzlkpc5eHaO-CeMCvKEOw63vKyYOm9zC4kYVY0zhzAZal6k1cxOxMp3rT_Sae5TOpgEVbL4ZbFIvCLWfhKqGhs9B1dTWpsMLRf2_sh9S_FDZiz1UefbNpY6pAt1CPpMVu5xoBPEo37gs5shT70GeQpbQREBvmluxR3ctMmKgAaGLFbaT9qoKFI0IzY2HlDAl6ZExqOuwP1DKUjk7XaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=JBSfGDvpCcKo_wyf0RbgWVn4JShyK2qHrmHrgIxR-v1ruXJBiu7XJlIMd2M5hC1UFAZL5HV-BqnXACrtogO5mbO1G2AbCF91BNB4aOzyyzTt9uoVqVX-OK5IAVfU_IbKHRYGzlkpc5eHaO-CeMCvKEOw63vKyYOm9zC4kYVY0zhzAZal6k1cxOxMp3rT_Sae5TOpgEVbL4ZbFIvCLWfhKqGhs9B1dTWpsMLRf2_sh9S_FDZiz1UefbNpY6pAt1CPpMVu5xoBPEo37gs5shT70GeQpbQREBvmluxR3ctMmKgAaGLFbaT9qoKFI0IzY2HlDAl6ZExqOuwP1DKUjk7XaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8BQMEIKfSu-0OL7v_u5muVYnk1AaRPgNCOV8Lij61KO7RtEwZVK8yYOdJj3Ga979AtPSAXj9r64wQR6Ag0vjzwpguL-akdWH3T5x4UWWhxk-0yFv2jD0IycYzNOmzid-fSKGGOuhrH9fSq9Qpwm-RYuoRonIuJrGgw4C20uxnpwcpHD9tXvCutD6pj2_ohB_J-WPALXbxj6waY7xgR39aELqeJBvbUNXJUXApeNl_rXraXBOE5uz4p38Tv5R3hYc4f_8zpTsWbQzImgM_CdFopmVZR38CzCJ1BOm_nIhBMWAaMr-LT0JIUCSd2MeGfgVNVINiLs_bq4M5q6WKSupQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re_DgJ9n7oevdAr04PP-lBVndwXTg6TINI-nQZpQnCFiht4qDXdH3oIqEO5ouD4aqSVkWnxykcXhFVfBKA5oXVKX_UWXJSPLQUw8M_wv5qNL-De3U2riBL14RSe3jufW--gpDAIzxnHS0DX832B70fow2GxuFyr228nvoxeV6Lb6DeoDfDqaAf6RvJwJlM6gT5dlcJybSaN-Dm8N6_WlSZK7CCgyBu-z0Y9I8bVY6OkdCbpjnNjr0VfzyImJpp17r0cIORoHPRv7PH5PDq87gH9v_QTqnT4WlAjHL4P_DZjWjoC-aIL_Fhwr8o8Hgenx9Z8Reud3cPfUHKH_l9WXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_0f5GdMRnuSDh9jrCbVrYkBHYP814IpvUGb53YYl-ZrBUX_MDewukl2maN0FXHa0g7sdFrNSDYZ-onUfWRi_BiQuvXELp1dTMs0fTwYv9TXms1m-hDPXik6UrlCp-nhcqwVpyq6ZD8T_MA5IN5UpmFOvMGOfd8EY1kyKcofVRamigz_jDO96W3UICoKLnyr3EfARJ14Tw5vChmOHzPdtS4yYLt2oCGlO3gddE8bS2kQ0CLkAEybkdBUs88w22pHnEbT-eIZ78rKNFWFwpwnD92li5gK1ekKf54JN0PUyqkVEBgIV03u3cjjtgPn7IghzlhfXyfOVxVuCeFQNPdfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=nh8d6Dy57ySaGy6kTdChipGhGrgIuGpRMg4vybKnZW3W5xaynnY7ECMiUPUr7CPyWoZrV8E-P9NYVfwG77_xdU5zQPblRcEet8xbEavhZDA0Mn0IMjmMujsWARmVpoELPB1B4b957nvEPpw5rlOEzs2estTxVUDYzxtzC7Os0Fp8XKEuAttKhwItRW62NtmTOcTXGa5vNQJ1HagTifAbYalBP6-OPgWlIgKY4a3NTmajkLbTqKB82GrgolRDFHOmUQ-t-R-rKFv9uMJxgxZPGPLNhD6VjK4j6uMrXULKsiZFIzF5YI92vfVe6ezBaXESBrtohlcWXd-P5TPNRsCJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=nh8d6Dy57ySaGy6kTdChipGhGrgIuGpRMg4vybKnZW3W5xaynnY7ECMiUPUr7CPyWoZrV8E-P9NYVfwG77_xdU5zQPblRcEet8xbEavhZDA0Mn0IMjmMujsWARmVpoELPB1B4b957nvEPpw5rlOEzs2estTxVUDYzxtzC7Os0Fp8XKEuAttKhwItRW62NtmTOcTXGa5vNQJ1HagTifAbYalBP6-OPgWlIgKY4a3NTmajkLbTqKB82GrgolRDFHOmUQ-t-R-rKFv9uMJxgxZPGPLNhD6VjK4j6uMrXULKsiZFIzF5YI92vfVe6ezBaXESBrtohlcWXd-P5TPNRsCJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiI96qlIe6quBTsAdvVod_4vxaUL3VvmoTf2n25pydygWSv9NhOf9SKzGygZ8pVGaytm_0C6e3EvPVxEVq9NQml4Q_6vsvd2BdwmUY9Zm5JGdvJcj6qdu5Ag-K5aXtQB5K1jCCGC7CD4nvlH9sXz7XzjZ6hHYLCGVu77AOvlDAZDczyrkDIjtRR7xkemxXOgBUyfjjP1zVj_veWNOzhoHZgKYeGAaa3NnLVQtyVBww0iuHE9mgCE-Db3apduLiLAQVk4FdQq0wwE35mPv6ym_KZRWuNLrD7OdwWybG-BbqSzVVMexsJrGLhEqbpIjy4j8Z1Qo4miEcC-pILeyuVZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SOa68ndOt2M_DzELxIkSEPxwdBgDGrdz5F3dNof8KcYEgSTGhNQDMTgMqhgWKDGql6vV3ZEsnTXRMxiWeFfIvcDdxzfdek0mLJTnFgWFvhVuFoZBr9EB7QZ3TJLNv4fngEF-TW6b10gB004jDHxneKnvdUMk_GNdsntiRmxn-39ekOqheOKeVD_DXFPTOW7KKpnx9uwK5V3WYEv7SWzmPdABqIJP-2FWjksQR6zbYiqLw7onyP0aoWWkumH2DL9hANmPfQ7exU1JrbDNccmReIKBbNZKJ1GItNGzVU_OJJ9hJslT1LaSB_3-s8ujFxsa2QwOEmM0H0V39d9fBX1R7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnTb9tyqdww-mHbl0SM5g4X9aSBIc8j33veGk-KNUVmlIRVR5ldeTbuovA4Lp6_DsrE80IsI-jIQ3FvmI_s2uq3_8RmUGYFEOgZ_-9EziN2inFI0_O_loEApZsX98ViBjECN5oHNBFeNZqagPfFnR4oDqOWSE-k57qbqO8DoDJBsGZznyNdpCi-VxXGQH7Zc8t60H-sx8QyMH4xvoomVIzA0Dgi-EBWQkWbzacI2SS5KAtKBAZaTTTSIYF4pKq54KY6wb1nfrBfM9cmhfQXzOB4jsw3IuZ8zH_HX4tSWzBa6kOPsQAAJP34tQZNkaE-6jTk8bJLbqIGNtBzDPkgguQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcqXtl5tYK3w1rNsNrlp6OFVgBU4W1MtDNFq2X3wjtD1mPaXGBe6f6XsHTnxY0vCg4pje1KUhnGTEiKzVZjBXoMdxqIWtxsjqyfnjMGFeZI8w5anWXEt8JIfMPtKJGT9OqfCr_FFr9FQyGBniz7EjOfPTOR5L0bVimonVh2y8bcMbG9NW_yFjlHppNwphr7wjePQ4-BS5oVfH0dPxDktXu8FCRnH6nkG6w8F_S44v6yCzc9Hk3jueuQvpYIKjWuCkP66EDkjF7yPre_VkPzO3a-C3jdno2HZBHcB8lsLX3eJoNXo8xwm4Lu2Jh95qPbjWigB-DvtH_jpeDqfLWywQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ7uCtKw445Ep6NnpFgVTLsx9-ebI2B9pTG-iUtHH-NJNr6QS7_92zK7sdZ9n3NT2wVvFksn5eAyDWs1jcPSgJWPtbRD3FuWbMWxuMxh1CfhgsJjek__3xOQn-1Mgz4KjViYd6M3LtkQhrQq0FdMsNH4l5bfOIRPsOBWC2rIwymhTmio4vk9RhI7YpRX5kfcF3e_ZuOVIKC_xAPLeP9hmiNOU0FForHdtF7JSwIP9RkFvzyDN5hIRvjAV2qgMy96rhcjFRg3yORxt66OGkWwoazyEjoem-3NjN2nV6_Vye59DRzpEp__UwKg09wd7eEQlaK_8lv32PXuVvjnVx64QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpzZrLHBiILINLtu_XoCoTzNAoy04Pz4IO3SRnwlI4Jt92h3fg6LDfy6bIZyqZ34CtcO2lYbg-VJSSa6xeqRpposDmopwgjbXNE3WK1OYmfWC7TJnXK_jH4-qdyIDjCTnWtBCAdqsXEB14dg-Z_TpPnAHKYb55cbl8Nk2D17V_xttiTxGxBjsrCyH5SKtKSxAdo_Cc4mbsNHUWpHdQ_NJR94BknOrHQn3xwatPHfJC6xWlk9kUiELJeZtNdS9icjTRr8PHBWDMvdysw_cbnkiZHYtxTpNMlZ8Sa5lXc0qoJ1f9Vq2jbtSwwj-00CmgU0-DMFp8CoNft8IKU8eVc678C0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpzZrLHBiILINLtu_XoCoTzNAoy04Pz4IO3SRnwlI4Jt92h3fg6LDfy6bIZyqZ34CtcO2lYbg-VJSSa6xeqRpposDmopwgjbXNE3WK1OYmfWC7TJnXK_jH4-qdyIDjCTnWtBCAdqsXEB14dg-Z_TpPnAHKYb55cbl8Nk2D17V_xttiTxGxBjsrCyH5SKtKSxAdo_Cc4mbsNHUWpHdQ_NJR94BknOrHQn3xwatPHfJC6xWlk9kUiELJeZtNdS9icjTRr8PHBWDMvdysw_cbnkiZHYtxTpNMlZ8Sa5lXc0qoJ1f9Vq2jbtSwwj-00CmgU0-DMFp8CoNft8IKU8eVc678C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=Kiu1W_202NNCeV6phz56iYMAFwv_hK4JsymlrX5k0xO6aSlvg13FccxAp5ONTZFSyQ9u2iKAh_oKyGMFQFkte4jYGNDzgxOK_z7mWyRXkAtL603K6UXxH2uWmCXuPPxoe_aX2NbF8TR6JvrOR-5mrQWnHa8C2Rla6mJtOaBh75LvRgCuBPM10XiwMntXuCnHWOVwLOlJIrXuRFZzLnIfIgQWlM3-HdrEPlGgin2FAJKLBcS8qiZtEd7qUHUMWtYGgJ5k-BH_88j9G7Y5C4dyFh55mpw1PJatMPRdJFio08zvT7Jf7r0pyQclj0ofnwyDpcCZIm26rim_973Kze6vkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=Kiu1W_202NNCeV6phz56iYMAFwv_hK4JsymlrX5k0xO6aSlvg13FccxAp5ONTZFSyQ9u2iKAh_oKyGMFQFkte4jYGNDzgxOK_z7mWyRXkAtL603K6UXxH2uWmCXuPPxoe_aX2NbF8TR6JvrOR-5mrQWnHa8C2Rla6mJtOaBh75LvRgCuBPM10XiwMntXuCnHWOVwLOlJIrXuRFZzLnIfIgQWlM3-HdrEPlGgin2FAJKLBcS8qiZtEd7qUHUMWtYGgJ5k-BH_88j9G7Y5C4dyFh55mpw1PJatMPRdJFio08zvT7Jf7r0pyQclj0ofnwyDpcCZIm26rim_973Kze6vkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYqWOJuENPAQ-qRGHaYqjhVpP46_UCxohe06fa54WegIw5tEifRaykznAPLA7x2bb9hkBLI2zCKaNEynoiJLUjWZ5ZJrfKwV4eu6flwAsl4wZF5vNpj4YeFdQSEbRtSnY7WBNoc4MOq5Cd3EvqWengckFSpsvLR7K8l3FK3CtFmL1g_UtnAWyOL1p1g4VChPwS35R4Xup4XGa1w-QaP7K8GyHzhM_5QKQqurBwf6AIs8lDHSbMxTGJjRFEpcYiLbt2IRGXdRjUnMKOMiZRUXWqLEK7aTnJTLSIN3MZaIgJIG58FfyLGsZufKlEilRCZY8OHE-uhEsC6eg2gnKvNEiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChEl4olS-NcRSqE8rB31Xf0CDYsp_R3KpnomgHVw9Z8i_5rP_t8sy1j0SGmkWMVoGCjiyeopRETLw9Ozp7g4aU-Pq7hAZzsoR3Fh7TaB2hElNyPO3TN3zQQNbjiUEKEXFrojh_I7iBMpBAXQ6fGGKZeQGRGbiZaWZnq1FoRCJ8lIS2zJPEQULlM9kYgujp4ftifiISbMjwpczLKm1cs4KqSYEpBkXEgq6lNzlEZ90WVVbhly-Xi8PtmbkSwa-9tUGWA33P4WYb7ML9QlJ0Gv7qzshyOgl-Rz10KT5Ee0vqaeVtdSPqZ4j-jtulmgJYazfBSfET4UItoogtY-rHVx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCPFugqcKOuzJRbQqy4gnpl3EsY_Zig5EGEqCNWKqaDR702MLEPIi8XfOcabtQoD51aB8Lt-9P7L8zTFfSH4cXfDkZfNvW6sfU-xbP3SxbS1uZLWhRNRyAoDyWfBGpYD3_zd2CehmhSJ1-JqW4K4XNoBi3IZFmahwgDeVxskwEsibAk3y1DRXO9HiN2ol6UXaEImrMuCWnwEpYSbvzgDNTM_A9TpXrCveLAQo6pz_bVvWOB1ulkDD3BPjKWhgQ1rwRwGOLGZLNUUtP5BbBjabhwVCt0ywLmEpXf-V7N_oX_hIV9cISETOE1iRyQa5m86lHtqbZlhoGhgqt66bPQJJA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
