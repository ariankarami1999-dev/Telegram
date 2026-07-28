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
<img src="https://cdn4.telesco.pe/file/TFVI06otTWwqb3qYvcO7VHKFGXtD7EtWSsg1kLAwT_t7qJ2E7Y0yY1KHmMutoPd2xfgPm-JO2NOwWYZ29S05au9Atroaq4cKUa67gPkewEOSGQXdbBWMzFiJO4x8vpCOBNlCgnjE6_nzAxkP9nDCHgHcMMKJz4r7DoN15e5QI5-hUlWjJa7TaIAAmKkgrN5BosaoF-G3N6ZxmQb5aPr4j34FyR1R7KnT-6RjH--XWyi-yRx9vWIMq34MZ8gfejtnwehzeBYt7JQyqjVuTkJ-9Xn6L9_g4h73ZZiu3aYSgGuy_du34h3XEnj5zCXJdUJWog8Wn74gjAGkW7hQMv0kew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.  سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/19365" target="_blank">📅 14:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شما ببینید چقدر سرعت تحولات ژئوپولیتیکی بالا و تاثیرگذاری آن روی پارامترهای اقتصادی از جمله احساسات مصرف کننده و تولیدکننده بالاست که امروز موسسه ING در
تحلیل گزارش مثبت دیروز IFO آلمان
چنین نوشته:
Normally, three consecutive increases in the Ifo index points would be a reason to party, celebrating increasing optimism in German businesses and higher hopes for an economic rebound in the second half of the year. However, in this highly volatile geopolitical environment, even leading indicators have become rather outdated.
Today’s Ifo index reading probably reflects more the initial relief after the US-Iran Memorandum of Understanding than the recent surge in energy prices.
ترجمه:
به‌ طور معمول، سه افزایش متوالی در شاخص ایفو دلیلی برای جشن گرفتن است؛ چراکه نشانه‌ای از افزایش خوش‌بینی در کسب‌وکارهای آلمانی و امید به بهبود اقتصادی در نیمه دوم سال است. با این حال، در محیط ژئوپلیتیکی بسیار ناپایدار کنونی، حتی شاخص‌های پیشرو نیز تا حدودی از اعتبار افتاده‌اند.
ارقام امروز شاخص ایفو احتمالاً بیش‌تر بازتاب‌دهنده آرامش اولیه پس از تفاهم‌نامه آمریکا و ایران است تا افزایش اخیر قیمت‌های انرژی.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/19364" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">311.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 14</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/19363" target="_blank">📅 14:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/19362" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر دفاع اسرائیل:
در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/19361" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:  ما اجازه نمی‌دهیم اردوغان سوریه را علیه ما تقویت کند. ما می‌دانیم چگونه منافع اسرائیل را دفاع کنیم.  در حال حاضر هیچ درگیری نظامی مستقیم بین اسرائیل و ترکیه وجود ندارد و ما تمایلی به ورود به چنین درگیری‌ای نداریم.  اما اردوغان…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/19360" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/19359" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، آمیخای چیکلی:  «ترکیه اردوغان و سوریه الشرع اکنون بسیار نگران‌کننده‌تر از ایران هستند.  دوران امپراتوری شیعه ایران به پایان رسیده است. محور جدید، محور اخوان المسلمین ترکیه، سوریه و قطر است».</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/19358" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/19357" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 14</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 14
سه شنبه 28 جولای 2026</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19356" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/19355" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز: در پیشنهاد عمان، تهران کنترل انحصاری تنگه هرمز را در اختیار نخواهد داشت
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد عمان پیشنهادی را به جمهوری اسلامی ارائه کرده است که بر اساس آن، سازوکاری مشترک میان کشورهای منطقه برای مدیریت تنگه هرمز، با دریافت کارمزدهای داوطلبانه، ایجاد شود. بر پایه این پیشنهاد، جمهوری اسلامی کنترل انحصاری این آبراه راهبردی را در اختیار نخواهد داشت.
پیشنهاد عمان از حمایت کشورهای منطقه برخوردار است و بر اساس الگوی تنگه مالاکا تدوین شده است؛ الگویی که در آن استفاده‌کنندگان از آبراه به صورت داوطلبانه در تامین هزینه‌های ناوبری، حفاظت از محیط زیست و عملیات جست‌وجو و نجات مشارکت مالی می‌کنند.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/19354" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUJNmeYMvQD1yV4KOZ4EGkWuYTI8dpL5duUD-jQeyUf_6v1tfJPsLfpMsYdhPYs-hpfky0zoFojBWwL6E5pLBi-U5hmEnwnCewukwGPxZJY07dWzxZpawigsAke3zLXaDfttOSgIpoqUe2W-iKFcxJkiYNGpmx6I84RHzovkPpihO_T-88Qk6-nS6ZipwdT3fj8zgy-pblkEYs1mkbxIRq15oEubCfqyNsdRp95A-W-VOLMLvc56sJmaTZ5WhDMzB3o3LftFRMnzz8rRQtqcnVWWZkjHGdJz3mY36m26dDBk0iLqsLftOSzUxx1hlZwtLha9C-rcMOXYm0nye5yjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب تأسیسات گاز پارس جنوبی عمق بحران ناترازی انرژی در ایران را چند برابر کرده است!
خروج ناگهانی ۲۳۰ میلیون متر مکعب از ظرفیت تولید روزانه گاز، شوک شدیدی به رگ‌های حیاتی اقتصاد و رفاه عمومی وارد آورده است. این رخداد، ناترازی مزمن گاز را از یک چالش مدیریتی و ساختاری به یک بحران ملی و اضطراری تبدیل کرده و پیامدهای این ویرانی به سرعت در دو جبهه حیاتی خود را نشان خواهدداد: سفره و آسایش مردم در بخش گاز شهری، و شریان‌های اقتصادی در بخش صنایع سنگین مانند فولاد.
سقوط مصرف در بخش گاز شهری
گاز شهری خط قرمز دولت‌ها برای حفظ رضایت عمومی است. با این حال، کسر بخش بزرگی از تولید، پایداری شبکه توزیع را در شهرهای بزرگ و مناطق سردسیر به لرزه درآورده است. افت فشار شدید در شبکه‌های خانگی، قطع پراکنده گاز در نقاط انتهایی شبکه و لزوم جیره‌بندی پنهان انرژی، نخستین پیامدهای ملموس این بحران هستند.
دولت برای جلوگیری از خاموشی مطلق خانه‌ها، مجبور به کاهش ارسال گاز به نیروگاه‌ها خواهدشد. این تغییر مسیر، نیروگاه‌ها را به سمت سوزاندن مازوت و گازوئیل سوق می‌دهد. نتیجه این زنجیره، تشدید آلودگی هوا در کلان‌شهرها و به خطر افتادن سلامت عمومی است. به عبارتی، شهروندان هزینه این تخریب را یا با سرمای خانه‌ها یا با استنشاق هوای آلوده و یا هر دو پرداخت می‌کنند.
فلج شدن صنعت فولاد و زنجیره‌های تولید
بخش عمده‌ای از بار سنگین این کسری به دوش بخش مولد اقتصاد، به‌ویژه صنعت فولاد، افتاده است. تولید فولاد در ایران به شدت وابسته به فرآیند احیای مستقیم و مصرف گاز طبیعی به عنوان ماده اولیه و سوخت است. قطع یا محدودیت شدید گاز صنایع به معنای توقف کوره‌ها و کاهش چشمگیر حجم تولید است.
کاهش درآمد و صادرات
افت تولید فولاد، ارزآوری کشور را کاهش داده و ارز غیرنفتی را محدود می‌کند.
کاهش سود کارخانه‌ه:
توقف خطوط تولید، هزینه‌های ثابت را بالا برده و سودآوری شرکت‌های بورسی را کاهش می‌دهد.
بحران در صنایع وابسته
کمبود فولاد خام، صنایع خودروسازی، ساختمان‌سازی و لوازم خانگی را نیز با جهش قیمت مواجه می‌کند.
سرایت بحران به سیمان و پتروشیمی
علاوه بر فولاد، صنایع سیمان و پتروشیمی نیز در صف نخست آسیب قرار دارند. پتروشیمی‌ها که گاز را به عنوان خوراک مصرف می‌کنند، با توقف تولید و فسخ قراردادهای صادراتی روبرو شده‌اند. کارخانه‌های سیمان نیز با قطع گاز به سمت مازوت‌سوزی رفته‌ و خواهندرفت که هزینه‌های حمل‌ونقل و تولید آن‌ها را به شدت افزایش داده و قیمت نهایی ساخت‌وساز را بالا می‌برد.
نتیجه‌گیری
تخریب‌های ناشی از جنگ، ساختار آسیب‌پذیر انرژی ایران را با چالشی بی‌سابقه روبرو کرده است. جبران ۱۰۰ میلیون متر مکعب از این ظرفیت در ماه‌های آینده، تنها یک مُسکن موقت است. تا زمانی که زیرساخت‌ها به طور کامل بازسازی نشوند و سرمایه‌گذاری کلان در بهینه‌سازی مصرف رخ ندهد، ناترازی گاز مانند سایه‌ای سنگین بر سر رفاه خانگی و رشد صنعتی کشور باقی خواهد ماند.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19353" target="_blank">📅 12:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axaQlMJBv6sJG0hcIXbRd1E5Nme04Fhyi_zptcWkSoxquFcp4jUS6hBpS0OIFCXsQZnr-puoxhxLajODHTc6VEzzCN9VKexHVDZxx_v-7lvNqZ88FSOTZH5n9mhwQWf7-WhenuLTDpm5vj6vkIiHsVS7NyFzQ6EEOKaMn9xYqLFyJN8kgVns21K7VgK6tcg0G62487_sLKlLnEvjTtjVNsWU4sBIPRdcwnD4yKNwLi8Ipb4ed-fEn0wwXXYMFBIMS7dhM4Hpe3UcCvr6sA1u4JDGCvjmy9saNOK9oZjszWr8HVqdZkK5bNnAWbGywUgf8ynvyWEYDUfSNPitBMiMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/19352" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhsmc-_UPeyrFF49IHUgUZc8svqIPDjJjZNqpLmYRwRTwu8kzZxV79QboKyvQ-I4-b2yRZLH0o34UfAbVA3DQc2S9xFXml9To7exytpNN66sr4_VAG6o8W1uDdNxFuRBIKGp7YVrF0KtX8tKhFDuZ6AnWZe0vB9SQP0_IKLW_sBxgyxJGQ_DHrJvOsCF8vCp-jAtTDzTRtF4-YzNTrB7T7x50vxmOqWlp7WE7dJvpbK_jNUGXEjindp3GSyBXEx9amlO7PWYKSKz-4Nb4KS94DkybnGNM6FkIa0dAjTDdrZPmBaKhJORneRE5rojYIMQCpNBt6qrSDkDzgWfSDn9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا زلنسکی هم به آمریکا همزمان با نتانیاهو سفر خواهدکرد تا دیدار مشترکی با ترامپ داشته باشند!</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19351" target="_blank">📅 11:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=cCKFq33D-dCSAMF3u-DVrrb1OaLcwh2Os0wfkGMlaGSBsCzhBdpREfXDig4Ai-PSWU6i0f9aNW4Q2YQjQS2wUv_d5c9Bkm7ut3sNJb9kUyZfctRx1TEnGDZ8BJDJOS2VLIgoNIy_0MfXo3IRdusZ9O_PeccY1H_2imUahx2SR9vwu44Obb69z7MCHUF1-21gBWqRQbx3Xj1tW2C1ryX7L5j0dZ0y68inkjyORA_s0kKGKL-hG9WyZgHizPP_QyYdILTXcZ24iOLW-OeUYAbh2_pQE1DQiLeEF8g1Qp5S2q8pbetM-tC9IeZcw8oDGCD3TTk8ohalIFAov_eHlVcgOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=cCKFq33D-dCSAMF3u-DVrrb1OaLcwh2Os0wfkGMlaGSBsCzhBdpREfXDig4Ai-PSWU6i0f9aNW4Q2YQjQS2wUv_d5c9Bkm7ut3sNJb9kUyZfctRx1TEnGDZ8BJDJOS2VLIgoNIy_0MfXo3IRdusZ9O_PeccY1H_2imUahx2SR9vwu44Obb69z7MCHUF1-21gBWqRQbx3Xj1tW2C1ryX7L5j0dZ0y68inkjyORA_s0kKGKL-hG9WyZgHizPP_QyYdILTXcZ24iOLW-OeUYAbh2_pQE1DQiLeEF8g1Qp5S2q8pbetM-tC9IeZcw8oDGCD3TTk8ohalIFAov_eHlVcgOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/19350" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW3kw1xjLx8zQwl4Rqm7PATeTTtXtaNqWbSA1S3tw-eBwqEhq9LGwBbtkv_nGQD4gw37yNdKb9xtI9YFHaGoLh5Y_qQM0WPDj1i4lFQUNX5a9PCQbD2d8TfP8kt3IT9pGTLqBasNylOba8oGHUlv_gMqUQvZ9kObgngk4v6gqTEpPRrCjuylzo-hbVj3GXWTdvWmliGIadVVx2zYI3JqsOpV_iBoDfSBlIJPSGz5JtMrIa6zUzeF1BXYC6POLrs3tSmlEF4pcSerhGlKZc5QAQNrZh8aoT8kjWhOwIXOs_k23OA3TP9_Zo50VsDawKlgM8WwZqJLcmZDh2B9ulzldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/19349" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grBDKDJi5WCYS5erOA2TQLjjbl6dVRBH0VTV6m6XHiN2AKfVfLRMOQcNGN6OOLKAhTJh0xhxt9w-smWxU_D5xqWM2_DoemOaIn5EIQxQy9dE2R7dQlY1gphJPrtpkPQv5P-7QLUNe3FlwhrWb5z3bACrSxh4RyPlrJy1Yh1WWuRXsBONBNXMJB_xZdC28dGN5tgxZjY5rxA8lfVZgKzp9-Hf9-jWJisFTeXePJ4g-2YQlPNTGyQu_JwejGvDHOKz5USgIf3iiWC-Wwwx6RCeBVH_4twjax4XfdqH3kOt7kI8hRSrV9qcvL2CqhKXh-zOo_9MuXq2Rj22X6uAra-F0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc3554F2LmZeUm3I7noAZ9pQCnM44C0XV7XhXTKkqf-Yu7gjUOjRDv0KfZe4vP-DXI7LfLFqR8tf9qHAELWjvf9C3bAsl8BUmZZAqXGdHs5IAthwoc5wwiofDzi1D49LBe02c4jIm30ERdcziTtRPQSfRmd80iHSOy5Hto03WEWehm1BYO3bjMrWaRidS_odBlhXTNGBksLTXJAa1WI3jpfVMI_pGOM_E1Z1T8f9tZxzg7qjx5qcMQVzDdk7JCvhARrVux2q6E10Fq9pOsqH0tTwgsh3EaTYDmkaICfa984pZqsCpwf6SND1PSCKPo4ne4TGEfNmtRD7J48xhvU__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afK4F8fLAmLmboU0rtNhIhQho6329B7enuWYLcDM0seyT2auDkcjD_Z0CzMVXN5vb9W0u8Zvt8QFzXEDSrnpcWF4RILMgwKPjIARf7dv1xyOj5ri3Ze1yqrJxwtSyAA3ZuRaxtc3obROkJtD2tbMJDPmeUdAcvTR-R8Eq81Cj8jR96P8tyn574w_h4DlapyCjyWIAvTeIbZAkoxiHjExJp_pwh4zOX3_gFw6DC6iKIJ_T7fy_GoCaqaA1GIou-PPfhmJSICHFA6rg4oMJ0FDDOxdt_CiWK5pdKczlbKiPKdqChC7vQodGNhaP7B8yxbJdij5PrdfaPRL7cIW8-R_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=kRn8fQSjTUhOQq9kJz6xrDgfh1eFhpoRCDvhUta0aP99V1k3M7Ksxv4yWwGbfdJIicbB1u_MS67bRbY3PVXPKDX1bCpDfOvsJddqEh1rf-ZGFOQHQ1begfEe9RiGgmELL93eBD8Y9LGTdjzNHi916dkURQ0G6z9zWXnXqu7LYVZsfXWme_11RvSkghWlZl8ewLUh8cHt5wWoVen0DQVUWsGvjgrQdfJuPxc6GRyFBrvx0FRFsA9XPRQyODMeJoz0vmnEL6KMVYHocqKAoZK1nwMsyTAtN8YR7wwMik-kvu8-nm2sjfz4QdpVAiC3yl4w4sQ3JCAxZFNjM-D3nRmnFjX6fOi5XMji7U3BC4eIKA7L3gTrXujJV5CRdNQzYVxe-9zupeHAdLgz2F4MiulM_B-zrFH9IBGadRMNSqgPpeRTFSNkgEvds5IoKTdsBStUFvR_eAMdYWvjM1uTekrZp6hVYHp4__BE3vn71CbLqyjbnuU9smM3MVL3X0BJiL4EeiaFHFKuOc8f2oFoH7YXE_fYybrQp_k_Oe7BbX4x2CF2eJjrr3LBqxOirag3oqENPgWQD_Q9mPDmDRPEsdygXsFqVxu6qw-Ecl8VouVG9KWHljR3AkWYP7cLMaGEhZ3ayl7veIvkuJry6syPkeB8UEO0-t9_Xni8mnIb37r1zCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=kRn8fQSjTUhOQq9kJz6xrDgfh1eFhpoRCDvhUta0aP99V1k3M7Ksxv4yWwGbfdJIicbB1u_MS67bRbY3PVXPKDX1bCpDfOvsJddqEh1rf-ZGFOQHQ1begfEe9RiGgmELL93eBD8Y9LGTdjzNHi916dkURQ0G6z9zWXnXqu7LYVZsfXWme_11RvSkghWlZl8ewLUh8cHt5wWoVen0DQVUWsGvjgrQdfJuPxc6GRyFBrvx0FRFsA9XPRQyODMeJoz0vmnEL6KMVYHocqKAoZK1nwMsyTAtN8YR7wwMik-kvu8-nm2sjfz4QdpVAiC3yl4w4sQ3JCAxZFNjM-D3nRmnFjX6fOi5XMji7U3BC4eIKA7L3gTrXujJV5CRdNQzYVxe-9zupeHAdLgz2F4MiulM_B-zrFH9IBGadRMNSqgPpeRTFSNkgEvds5IoKTdsBStUFvR_eAMdYWvjM1uTekrZp6hVYHp4__BE3vn71CbLqyjbnuU9smM3MVL3X0BJiL4EeiaFHFKuOc8f2oFoH7YXE_fYybrQp_k_Oe7BbX4x2CF2eJjrr3LBqxOirag3oqENPgWQD_Q9mPDmDRPEsdygXsFqVxu6qw-Ecl8VouVG9KWHljR3AkWYP7cLMaGEhZ3ayl7veIvkuJry6syPkeB8UEO0-t9_Xni8mnIb37r1zCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfJ05cI4BGDORFjz9ILSu4gaS6YZ6c4W2NEM2PBIBTyZdnfxwEltp1aadUamBc-O0TWSKKhNWNVXpRCP0grP6EZJitcyaDplpfnKXRRvJrwuNrAJeIjC7FQxKkAFFrFQMDONRmHDy1rtm3P4wA2NIg6bEPt2a4xMPLn2nrp_hXBXQGwM51a5LEuSYYhktbA3Xb0a3pZjAvhcfey58S9gghabKhf2ldGy-ZYA_Ug3S_garcDF1DlnNj4QyowOOaRF6OY6dSpUfMTAUxB6uaHcSz3F-nOQ5yhBkzpW0boQobmd7iFuDlw7d1ValM7EbOR1Qahjry9RZRjYoowjZDLF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7XeatP5e9O0zfHhdsmrhv6NZU-SaZNnoErMFQxNh4QPwgfu-Sl3NB5XyQshJO4Lc27gH8KpdOUUj4htdf7aOrRfkBUvuV8E2Hfrm2LZQxnYhCTomBHIHrtmd6bjbjSaar5kfe37hH_dKNhanHvwKmdoPr_de1SoH_BXHeyFeP9nkvyWN_VLudKqs4KwdQGCZE4-yz4J_UwoqkAUlW3KB7zB6I323B0cA6HL4xRUCE8ixSri_Ocf5rOjjUPT7rQXUbTnMQYt--My3Yh0AtAzlGkb8yXEAfOCuLHj_WTV-QvyNI_Ap_Nw1im7snGtGJZztHVgRVSsi5-Isb5R_wooig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFUTgzcGp9WN_BvURNFe_bwYzbtiBiPmb3OqcLTuhFrIEue0iDBtPykAwnh9i7wKDRD94agaOGAk0LZwJZZ6DMnUnwYawPJYJ-Ha5FbPPAaSf93cdGGcrPzgKVVethObZPCDEP2F4jAUjGakcRM-HSvbzOPPT7trGuMhe-8K9SMGveKqkQowMH3x72fa-hLtI8zISvisYOq6HXch_vXZYsidseDlxYt1-VZOOLR2hzIw6o3gNryAaZdqs2T8YLsYu24x0bfILC38oF3h516mQw-3c8-RPpAAn2iV7pAwjVo9Gog8dFwcuiGY09deU3P8GeBJZBwlloIiJVog2X3cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVgMsAvRxWNEdUqhQ2FdWgKKbBMoixQx-57DMA_D5Rc4Sdgc-pT3D75bo9RbzxncqD38q8KBMuokDRjm89iWLWyirVlbXllc9FKq3DJPZrVk20RVh96pxhiWCz0y-MSX56EXvBesvO6k6KkW1vHlSFFzGxv_-e5xYMEFsncZ_um35usoSKLNu6g4DHYgEaA5ghfUlMw08yrRylmhsmpNf2of8O1KJbLrgeEwt_ci_qteOarBo5Rk8CyG2baexoMj5nVcbPGEZQv9qYdiG3zKD0lIJ17OGnMLUW6lYP4pLlBVXdHfr4YoSA4LLbg8gLmRkllfkpz0mopxnR3agUftdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بازار اوراق قرضه پیش از فدرال رزرو رأی خود را صادر کرده است
افزایش بازدهی اوراق خزانه‌داری آمریکا نشان می‌دهد بازارها با نگرانی از بازگشت تورم، کسری بودجه و رشد بدهی دولت، انتظار دارند نرخ‌های بهره بلندمدت برای مدت بیشتری بالا بمانند.
تنش‌های خاورمیانه، جهش قیمت نفت و تعرفه‌های جدید این نگرانی را تشدید کرده و باعث شده بازار اوراق پیش از تصمیم فدرال رزرو، عملاً موضع خود را درباره ماندگاری فشارهای تورمی اعلام کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 13</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 13
دوشنبه 27 جولای 2026</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6q9W-FWSCS6hnoJCXw7SAQRzajF88WP96DyvEE1471HYB4CACU3WpvZ-Vkr3gcCDuKSkEwOXccRlLRggqYAJkwyW1AFX8YZf0n4RwcAuSURUnDOYQchpGqDYv4XYjHnKfpvEN3orhry6CQq2hEVvUwTfNd4e8BqK4-NH8aBbCg-QxhmYhF-ULE9A3Xw7dxLFry0s3mhFOX9UJ7hUypYE4JV-s5yaqHkVE-aGCSKHm0EzAql2ooGArBN2LaBLJh7AgYPrWIWO_W7hSBWj5X8yaNOIu3aqK_QHikaWjmjuhDenmVAnvzbHdvoN740AvZiIQbV-EjNX-l7B6BsN7cYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvgcgzLt9wLmOFAB7mhegcRyUbDTq7_DX9mG2zEhf5UvM_wA4BT9E0vdB8oxqXh9MW1A4ElJQvM3vpdwi7gfrPhjVH3rkNvqZliTXS6Nz6sca1oEPRLO1bxCUsgxyg3l6rIMd2Jf83UAJ2_ZLE3xbjGgrIL9QpO7VLY-y805LrpvXAbjcXPRNM__HDQSSmXRh_MnpVZ4x0UedlcTcwCJtbc17Xv1w2DDUD6FpGPqDWwXrY8vgc3EVpIzdtsai5qhu7UO2nxwK5kSlJlaEU8Jl71nN_4-gSz1yKRZg8kjQmskRd0Nz0_xtkipeqomgk73WrCgExqjOuBdmM_8vbNYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Gsvn88_tk1OZrMtfCQQGL1hXqFO0lAST0U2KFi2B00DnHOeHrZ8CdK5Y5FDlnzxn8ugD-vmHThCW8nalyBVJocB8Q0GTl3YcfKnuqFgVCih9V-g1FpeRyB95Ghy7x1yiEOiUvp-gV9X-LD8v8PpTEyY3PMpPEYy0Fe3yen3VgYHEVTGqZpIMFesTOoLeij-G5ZLJ2Z9pnXEXz9RC2fdQvuRd33Wj7O787bpNtv0FTQv_FrCp4EDgO3VoIaAZK8FC9ZmrrhPKaJohnX94tGuwQasbPa7C0qvq0Y1XwKd6ZSesldgJy_F8AK24DCnwxZd1gCdGi-Y-Aadknnnd6RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها و اخلال در مسیر جایگزین صادرات نفت عربستان
با ادامه تنش‌ها در تنگه هرمز و دریای سرخ، عربستان سعودی برای صادرات نفت خود بیش از گذشته به مسیر دریای سرخ و کانال سوئز وابسته شده است. ریاض از زمان آغاز جنگ با ایران، با استفاده از خط لوله شرق–غرب، بخش عمده نفت خود را به پایانه‌های دریای سرخ منتقل کرده و صادرات از این مسیر را از حدود
۷۰۰ هزار بشکه
به
۴.۹ میلیون بشکه در روز
افزایش داده است؛ رقمی معادل نزدیک به
۵ درصد عرضه جهانی نفت
. از این مقدار، حدود
۳.۵ میلیون بشکه در روز
از تنگه باب‌المندب، عمدتاً به مقصد آسیا، عبور می‌کند.
اما حملات اخیر حوثی‌ها به کشتی‌های سعودی، این مسیر جایگزین را نیز با خطر مواجه کرده است. در نتیجه، بخشی از نفت عربستان ناچار است از
کانال سوئز
یا حتی با دور زدن
دماغه امید نیک
در جنوب آفریقا به بازارهای آسیایی برسد؛ مسیری که
۲۰ تا ۳۰ روز
به زمان حمل‌ونقل می‌افزاید و هزینه‌های حمل و بیمه را به‌طور قابل توجهی افزایش می‌دهد.
در سه هفته نخست ژوئیه، حجم عبور نفت از کانال سوئز به بالاترین سطح خود در
دو سال و نیم گذشته
رسید و انتقال نفت از طریق خط لوله
سومد
مصر نیز نسبت به ماه قبل
۵۰ درصد
افزایش یافت. با این حال، محدودیت عمق کانال سوئز باعث می‌شود نفتکش‌های غول‌پیکر نتوانند با بار کامل از آن عبور کنند و ناچار به تخلیه بخشی از محموله و انتقال آن از طریق خط لوله سومد یا استفاده از نفتکش‌های کوچک‌تر شوند.
در همین حال، ایران پیش‌تر هشدار داده بود که در صورت تشدید اقدامات آمریکا، ممکن است
باب‌المندب و دریای سرخ
را نیز هدف قرار دهد. به همین دلیل، تحلیلگران هشدار می‌دهند که با محدودتر شدن مسیرهای صادرات نفت، توان بازار جهانی برای مقابله با هرگونه شوک جدید عرضه کاهش یافته است. در شرایطی که قیمت نفت برنت به حدود
۹۷ دلار
رسیده و برای مدتی از
۱۰۰ دلار
نیز عبور کرده بود،
گلدمن ساکس
احتمال افزایش قیمت تا
۱۲۰ دلار
را مطرح کرده است.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilecjd_Hz210F5jm3yUmUxhfwBcT8i8elpyA8J-aOOXWavaNDb7kGezJM_Et2lN1fbyq0oOSlfHb6VVrL3LLq-iM0sWc_e0MECzOWIOzhKE_yX8PEF8vEXZQiGwUgasZ3xAgMbg9xz72dGWMp81vUKLWQCW1kzVu4MRjzkB9ScMJ3MV-EyTPhjFe5mzbliILP-jMzrxsKZxvTgCvjv4H8xuzrDEuZj_0FSMJvrCC07sHXy-BaaOkjEpmML0xZcvqKrCsy7lZR-U60MJMvXpiotgbKs3wQfnZH2RYsHtjuCuyKHS-4ZU94pptvG8REhrvs1MgkgrHXXPoWeOqhYFJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akpv9jl708CLjpWkAqsU7SKbN1Tdpfm2kvspVT8GRJJT8ZgiVIMUYeRXNLkG_PXXlLG-yEy6MwsbN-xnyLsbO5zbrD9VDQSyPPsj4ELYw8eDaRfCmceTw0vE8WvCHpm5gitzL00SsnZrgZyy5tQozMBbO5SSZuXii9K0ipbxtcwdZu9meMWB0eICpEr8feO53UallRomapI7JirlJfDh3mq_H_osoeogpBZz--J9Q6B39N10zpPzKVDJzjDIhBZw_dgiWcu1kIHXhNrzv2D6LbMUU20UpYPb8sBmIKe1akKiyJ5gwQvHCIUaZFN3xxnzDEL7FWaK8brjUG5gi12J_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYLRVPs_QQksnuZWhV849TUuxmWO1-kbrN6JUyHa1o_z2E-dlbYV5Y9wGMZS66XBmF2xV_AUpH2r-3Rcio7rc4s7x6skGSS5TYHZz6VQmUimJ6JczYIQmE_NTm3HixYK9SEpwWoaGZXGbcrY4KnuSW1R1GifhQE8_H6g91LZ03zSnxlak-akJwculEjce3CcBfirCopBZcZPR05P7Ucp4xrE59gIKt2XMqVV6COej-HZ4j--StZUJh_IyG32Kl9-KbF2sIESXxG5xTPyVkYZutfi7xaHxVqYN5eh1F3I21s5zB8qhBIhbjCVJ_toxrKUUvqmGWcBLQBpAGGLMARfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww7wzQV_u4no9DZYZCpGDBApMyQzHzLlPz28ECdDAiWlQL6j0eS1afgOAmURaj9flWHAlbsThbmbiF4URxiwr0aV73mHRy4JrBh6QE8PfW-tv45u-cd_j0TJNn9DPvx_iDthezYHj3c-Bxz78hCqBe689gxgH5sWoROSBKD2hT7gPjzaXB-GMIKH7luXIDT31vlfUQZpuV1qDBkzhAWCmViHEI8nxlqBOo-Uj-u39aYwm7pUVUEt91eabr-EWANCzniztdm9IT6kPYgy69Z4b_azzC7l9BEJHv_VgXrPEOb2LyqoesEf2TdXCB7w7F_qpecnszInxFUHN5_Dr46zFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVDXWzHhS3nnLIl2cV1xGnRebXwAulYl9Af0viUhnvv8fSKAqoguPE8RlpCnimQ6c3gmDYbFoEianD-OtAMQoY5zJCqddOjcWyhsREPRG27B1JQ8ZnToD3Sg0jJ8wkyQeXrUbdJQIIwAimIXLccHGe3GsJ4sii-2M7CDy1WCQmu6yIQbNlfpzKejSCxYSPwSQP9bH9op1dFZ5UgIviSulB5V27CRTecw7I5K3gw2LhebDbOU1YgHLzp1Yf6VLYbitdrE6A6WNl-NxlBaXTZfu_inJhHz55rfrhfJY4zxc2vcaEXPP-Wdj2NNi9Zp9QFjicNNaI3utlzHzNPcomOwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال استریت ژورنال:
الکس هولدر، فیلمساز مستندی که به زودی درباره لیندسی گراهام منتشر می‌شود، گفته که این سناتور در هفته‌های پایانی زندگی‌اش به تدریج خسته‌تر به نظر می‌رسید.
وقتی هولدر پرسید که آیا او خوب است یا نه، گراهام پاسخ داد که برای خوابیدن زمانی ندارد زیرا هنوز باید رژیم ایران را سرنگون کند، به میانجی‌گری صلح بین روسیه و اوکراین کمک کند و روابط عربستان سعودی و اسرائیل را تا پایان سال عادی‌سازی کند.
بر اساس گفته‌های الکس هولدر، فیلمساز، لیندزی گراهام به تدریج نسبت به هر دو دولت ترامپ و هم‌حزبی‌هایش در جمهوری‌خواهان به دلیل جنگ با ایران ناامید شده بود.
گراهام گفت که با «تعداد زیادی از افراد در داخل» که با درگیری آمریکا مخالف بودند، درگیر شد و افسوس خورده که مقامات کمی از دولت به‌طور عمومی از این تعارض دفاع می‌کنند.
«تعداد بسیار کمی از افراد در دولت این جنگ را تبلیغ می‌کنند. من شوکه‌ام،» گراهام گفت.
هولدر گفت که گراهام همچنین پس از اینکه رئیس‌جمهور در ژوئن یک توافق مقدماتی با ایران امضا کرد، از ترامپ ناامید شد.
در مصاحبه نهایی آن‌ها که چند هفته پیش از مرگ گراهام در یک مغازه باقلوا در کلمبیا، کارولینای جنوبی انجام شد، سناتور گفت که ترامپ بیش از حد مردد شده است.
«او اجازه می‌دهد این موضوع از دست برود،» گراهام گفت. «باید بروم و با او صحبت کنم.»
در اوایل مارس، لیندسی گراهام پیش‌بینی کرده بود که رژیم ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «تکانه‌ای تقریباً غیرقابل بازگشت» ایجاد خواهد کرد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzV7nbpOxsrT0ZUFl43Bu04osl9mB2pEaggST_TimGButs3HSauayLpHN3mDwx6NkOdNKywgbdZUm0bnRCIT9wlrOonK7horujU1NESeFA445yN_ROzCl_mmz2OiF05m1pPnixnxzXe-QtaE2fwu5evQAN68bePwtmuUIdRS6Ktegby8qEx_mi649zM_GkhmsyYon-CamJp60T4mWJHHzMsxX3C5jONqSlq0H4a0zzikrM1Xl8eeMkdWmzCoWkARCNEWtbayjbK2MrEyaM57VeqbqR11nQDJghg6v8_xOTWzi5RHR8FZoW07slCSmpWTSi7ZD2jY6FYS53aEs23V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp3VZQp24NrWup5VTcZV08aM6QmC7rLI03QK_YWeqXu6FiXITLd8rtCWy02KVaxh24PfcvFwOq5uOMLSYRaJwKF1ABZ6-21W2DIy-_p0067cJvXP9Qs3PDQI7DuGSMmNrAwQlSJgxBU8Dsw9A_xdiDqFH_E3UrGu5S4svJ6mMIHiXE-NGrC3tfEvSeMeEalMA2lDdGVfco8tkf_-iYO0ZutpQMkgEXmBsrX9kyB9OEKN-1XyXXfNmngb_v0YghWf58J_TM9yf6_aAZwh-3El1DL_5S-UcPh57IFnWP6eBU3Ji9Y78txXBlECluxf-768lnwsY3ZyTlcBWWJ8c_brww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ING9FpPyw7AdsNsYhfn-vsZ1wlNOolHaMM9NFTT9A2r5t66YIx5hNpUQsMWOTwF3JDoN-JZCpofYtA4I33Jzb1QEPbtNH6dl9wVn_aNa0w2ooy90WIf-ZwdOFq1gMLRZgaw8G-ezOsP-7b-1eGbHseTK1Tw1aOW8wK4S2KSIS0Bnsdqj5xxvknMGcoI6a9dn-m31XUQGqi9S4sn59NErIYWi6KeX2wvolAeP25wErXPNEVgnMTM1ZXxC3DSmRioMqihTB1eX8FAZJ0RiIfZ3K9bg9XPfi_C8mTBKl4ezdaeYwgRiP2SqIl5Es25Lf0j0PreOf8J79cR-Rs-S58k2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBHjW8D2zSuhUVS0DYD3w40DFgHh46t1prXnPmqkDSvMwVx2DBzQ0IUeco383Bk0GohXjP-4Sm-RDDecxlCq2TnqGwwTjJtnXozZgbGx4kFANF1OToyPrSwYaypiZJw2D2h44HC486CJg-_Gn7Q8wiXYyuFjJHylz69tzTaDcrP6PFMEKKc5pEyLtUH8cAto7GpFhXaVTvO778XzdWeQjrXPg90_nxKGVG9R9qP1JY9opfDCDtOAaBmy565IWmUBQKpiJSCU7A9FS-4rQ8YplvJXaolBfTrq40Jbo3674Hl3SqdfQcIn5jPXOUadTslEfo2XYRdpSf7DUsRhcvu1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0aDiNh5JP2IbyC1d6J8tvf2xx1vImtLs3NJjTnH2GqLYazNs_gPV4A5RFdHUt1jnaED7yqXgAhb-X9mbWCqOZb5Z7dWXG2Z0JLk0iKEnHMA6GwOoHILIOO-C6e-tQOFKZrVm3MkhMschavuizWRsIrI0gvQOVemdNDo808GwNsXxKOYFVOeiONPS0DLhIuSqr0DcwZdlynuHFdgeRB5CPISPh0g8EDM9iQi3YfpVIjBaR8fcSRi0IYJpZHlAUcwj96Q-FM4R7vE0kygPSlZXcOd5OI2i42PaL-qwTm6gCj5svdUonNyDq45VqpOAwRsowP6jVBT6XFbpn05J114Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfVofhdDNRZAZ-pU5dgd2ovu1NhAQtB3GlXuJZIpjHPz0JRloo2i51hdnL0DX1kRfmRppIWq5kirtTG2VbBHgv0LTbndPn8bdS7k-fNG0Wbb_voHpr4vhN9aL0IqvoWJYNY526leICWjeiTS3lCDFc6GW5V15XLSaNGBuy3nh6AtDrNZjRH5OdX_TaI0SGp71XXZCoLNee1WSie0BE_9ZBJgO7iQv6srbxAbsBGtx7MRZd6y3beZ2PY-LqfLiUHVgtGMzzQNR_ceHwmMhR1zDrJVLXB4DVft5UwlYFkgyVPM06Kb_-qmYMaNbhXiY07Lmf4Eyp2G_ZQIugE_dH2ogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At27CdsGsyEHb8QdzNS1r0wrgKScHChoNR9BvlLrp6AL0lzmhG8fOtEABH5POkvcc2rRJ-D19zszGkWzaian1RKvNBnD_VZu55aaNPED1PbkGiJGA-sjotXuJtCIkLHgLl9r2a0GiJrB3LQtyGAMK6w8Gamib_i0F_7KYzz0lGDGI_80Fr3J-U8h6RoX_BKgpFHJQitmdbquw10DDRmqI_jbaSK1l9THNbuzqCb5G3UuE0Rph4YCQHfMH3VKdY2XJXTPFLfjDvym4GwkoXM6K6OBEqRXmFpIa1d7RfdUN03yJpTDmNdRWbM5SuB1irBl7O7sNaXdWGc7hQoDAQdW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvyf6LWDRdkrakDfvMJHHURAN47yvkfrBmfGp47EmifKR0e7f2hyNCDFHh1dht9tHRw0HjB1GsbGkgmrZXkAlJRa5ahdWGVGNVDvACadG2A4tknOOlTUO4UaPHM7gpQFMs1zNar7A_DL1rEulH3dGL42rPVZDXekR41d1SCxQV8_63aUO0TbkOgvrI5nmoiuA7yDilhasa6Qh_Db1jYM1YaHANsE_V_cNMoX8VFv9DIySioOJmVMozMKmA3cWstOen8CsCXGeQl0CJtfqGWUFcOeqiG0cSlDTEw8Gr9_kxADjTzlH_7V5ksJZKAbkamSRMyofGwOCPGFWOT8Nqwgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=mmf5KMU2O5Hbej7arDu18dGFXjYUK3hEbtiMZcEy0vfWQQUHNlCi0x_TTWQnZkqp6H_65pS_WSo7doWzMA5LPHjHpk02ct4NmsGRNaddXilN060SufPHdZ1PQwzS8PBH0yC2amstbZL6RhZQojqIhLyQktX12AjZOaKxgSFe0rxSsBHwhPg3tPxA9IW13UJCUug4UK6MObr-OWVn8Nl57NZbfuqiQDL3sRsa3Mm4UwFeLciKuiFv07EFCbsTyOfvTaOpdqdW_YXQONIAp8hX1FJ29wPxC_tBHET2dRAKq75X0xEE6er69ZNOcdaymUTq79j0mWQErtdXlP6iwZUPyIbwgQxDn31P0NflikLF1YK7bqp6zui9b9UYIvSuPtI4L11gptm0YD3VLFLLoorIwGM7AlovVM3P-i8JQULfTPWiw4PK5t60R10ZdJKgsZ4VSL96sq8aA9HqBzflkzKa6A1rz9_11RKKSSxVv6ikdS_DSyQHh4Qln8fVjoWVT_1plwN9SG3Lg-r8NUH7Nihq06WRCTDpcBc945ih0o3d0dw9xih6YyDxR1hIkSl7AtQ5a4y6BWbcVrjjN7n0uURSgh7vSLHXbR3aHigfdPCpWneeiI7U1cZS0y1vTcG-O2n3RyLJYlIGxFA8xWCNc7UTbGm10eSzkwSEjL3R1yAmknU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=mmf5KMU2O5Hbej7arDu18dGFXjYUK3hEbtiMZcEy0vfWQQUHNlCi0x_TTWQnZkqp6H_65pS_WSo7doWzMA5LPHjHpk02ct4NmsGRNaddXilN060SufPHdZ1PQwzS8PBH0yC2amstbZL6RhZQojqIhLyQktX12AjZOaKxgSFe0rxSsBHwhPg3tPxA9IW13UJCUug4UK6MObr-OWVn8Nl57NZbfuqiQDL3sRsa3Mm4UwFeLciKuiFv07EFCbsTyOfvTaOpdqdW_YXQONIAp8hX1FJ29wPxC_tBHET2dRAKq75X0xEE6er69ZNOcdaymUTq79j0mWQErtdXlP6iwZUPyIbwgQxDn31P0NflikLF1YK7bqp6zui9b9UYIvSuPtI4L11gptm0YD3VLFLLoorIwGM7AlovVM3P-i8JQULfTPWiw4PK5t60R10ZdJKgsZ4VSL96sq8aA9HqBzflkzKa6A1rz9_11RKKSSxVv6ikdS_DSyQHh4Qln8fVjoWVT_1plwN9SG3Lg-r8NUH7Nihq06WRCTDpcBc945ih0o3d0dw9xih6YyDxR1hIkSl7AtQ5a4y6BWbcVrjjN7n0uURSgh7vSLHXbR3aHigfdPCpWneeiI7U1cZS0y1vTcG-O2n3RyLJYlIGxFA8xWCNc7UTbGm10eSzkwSEjL3R1yAmknU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4bJknqVpGmPmb5R4QK86G7VwfFmzovCqO3OSlVrez9S4ihslZDFsjQI_PA-QJj0cEjHrKABPubtzKaCRKeQR6VNm4z3DeXx8Z7D7ZdRqseDvllbhG9vmmrSqF_A2C4_fYdbLu3PNh83K_C0v0x0xp6_REYmIcMD_gX4dWFdbO3h1wRkgLKQKHbti_i_uIShczAL1wl9xWpksb_9t4Q_bH2_ZQZr04hDIPZg2rrbJNWd_ZITlv3lXxIr7egi7C47FIJlA2bST1VOMqM8O1FwgLDML3_DOnXOOOoV9hyRwVQmefcpeN06JaWH-Y7nkEGkYmPqAV8NGRBXFNsmyA4XlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=geClL_1MAMibslwecm24Sj6PYAOWAul2VljoNHTNvyTgpWTEDfkyzyiAvroTKGc_v8buWyBBL5EYWDtIfgmsCiRjAXm8-wqcJFD50bp_5e_N_LTiiAScwvuBWiWHN6qgSKbhjc5Nt21nTCI4YLRlnbPYyut65yWM3ws8cbuG-sMHeaVG-l7t0rn_ep5_l7gTdgwhhdrFACPBnKvtQHaeN-2Wjwl3WpmCcc4AMJkOrSye3IhTtO-1fUgp-Kv5nCWj6_Xly5r7fSFSMqT_TF-5unvJambRnjkkgQ1JZY_dPi2Ar-QxD5svylbtg4Wmv-4qmpmSMZT4hFI3P2CZ0t8k2Rs_PD-McrjvcBHDpVP5aWWq5kZ3ehRA-e0qlbGYnwHbCwF1CWgYhre4IQFvhvOqJv5BFN0BUPT56jmwzil1XCi8o2te-T6vucNXpnbBbfbU2wK0NXDmsZP8Txs4R1ED_6Weej8AJT9HCG4OsTad1cUFuQsz45oQNwVzCRpk53jxmuAjQBiQNUEC1VT_JD3SQuMujqKP5q6ZxFufz8FD2R14ZqdxIo5gUDIa56SgeQnweNZlrSeJ3COjyo7kkDfNqU89SLtPmvwWkOhNJ7qTbEHiovET4Sbc6ZXja0DZlZ4wpemCslTdNE6Zx7ih-5XMcibSfwgsPqDANAJiKM_2kF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=geClL_1MAMibslwecm24Sj6PYAOWAul2VljoNHTNvyTgpWTEDfkyzyiAvroTKGc_v8buWyBBL5EYWDtIfgmsCiRjAXm8-wqcJFD50bp_5e_N_LTiiAScwvuBWiWHN6qgSKbhjc5Nt21nTCI4YLRlnbPYyut65yWM3ws8cbuG-sMHeaVG-l7t0rn_ep5_l7gTdgwhhdrFACPBnKvtQHaeN-2Wjwl3WpmCcc4AMJkOrSye3IhTtO-1fUgp-Kv5nCWj6_Xly5r7fSFSMqT_TF-5unvJambRnjkkgQ1JZY_dPi2Ar-QxD5svylbtg4Wmv-4qmpmSMZT4hFI3P2CZ0t8k2Rs_PD-McrjvcBHDpVP5aWWq5kZ3ehRA-e0qlbGYnwHbCwF1CWgYhre4IQFvhvOqJv5BFN0BUPT56jmwzil1XCi8o2te-T6vucNXpnbBbfbU2wK0NXDmsZP8Txs4R1ED_6Weej8AJT9HCG4OsTad1cUFuQsz45oQNwVzCRpk53jxmuAjQBiQNUEC1VT_JD3SQuMujqKP5q6ZxFufz8FD2R14ZqdxIo5gUDIa56SgeQnweNZlrSeJ3COjyo7kkDfNqU89SLtPmvwWkOhNJ7qTbEHiovET4Sbc6ZXja0DZlZ4wpemCslTdNE6Zx7ih-5XMcibSfwgsPqDANAJiKM_2kF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRwB8bCQbZcPt8XbN8gxt4Sd3beg2yyTtsK67AfoI8bTsptiHwbcfrt8b8nE1u9U2NoSAwdicpP5B5GuS_NcrcUOa9lnThCxcOt5r0hhye6SJIUGiaS6OyRHxgTu0Y_XziNSWlAGzlLktEEFyf9KBxWBwmpSTaxf-QwrnIqI0faT2_OeGu36fP3sIjORO2Yge04ASYhuCGi9gjCyT54YU0NqzKQ3LoUqQjtlsU8_okYD_vTFazC6TGhQ9FkqrisOrIA1SfJEIVUud20CV41AVjNujM51JyZAebZWo3FpSioejpGbdD5y0bwMxHaMNyP0fPZVDos-K1Hkvr1QAPqfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=TP1_xe6Q8zb5GDtcMeIVQ1ssx-4bEXv0QsoXf40iYAftThVtyUDh3LI7BBnc4T5-cIkveyzPCC5pebbbE68MswmkXTsuHivE6Puk972v1Fvt80KkVpAyNt1EnwKDl9HFCYze09qjPWA3Bn7tmJfpuh9DitODJmPNBn8K3veDwnE-lfiifyc65V4EXqHhi_WCPiNPd5c3f-6smEhvkj2S-rpx75_7NNP0WqFpoJMHrCzZEFsLc3LCkbAmbQ3xD2xzecKMlEgHTxqvwGCvUBS718p2C2lq_aAcyTujqhXOAldZ1dl01A_BKbpDbCXfBgqou_PuQJwzuIM392wtSvNXag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=TP1_xe6Q8zb5GDtcMeIVQ1ssx-4bEXv0QsoXf40iYAftThVtyUDh3LI7BBnc4T5-cIkveyzPCC5pebbbE68MswmkXTsuHivE6Puk972v1Fvt80KkVpAyNt1EnwKDl9HFCYze09qjPWA3Bn7tmJfpuh9DitODJmPNBn8K3veDwnE-lfiifyc65V4EXqHhi_WCPiNPd5c3f-6smEhvkj2S-rpx75_7NNP0WqFpoJMHrCzZEFsLc3LCkbAmbQ3xD2xzecKMlEgHTxqvwGCvUBS718p2C2lq_aAcyTujqhXOAldZ1dl01A_BKbpDbCXfBgqou_PuQJwzuIM392wtSvNXag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzaCq2r3VLkWJgbAI-NwVal0WiYZGeF7ZkZ521CxwOHUVldgwfGxBBSIYfPCviRVHjwMIC7VXNQZR_zOpsDgSUe6lIF2bU-DJVa9shHjQ5cIPUUv6psqI7E-3iPqlICuZBFX-PE2mJSkNJy266UFdJ-Uo2jyKK8jto10aiCz8Lk6pn6mAibaQEMi1mK8Ditv1PzLtDGCR1XdRHp2G24Bblk_VtLXR1MZI4sZ0HCM5O2OEKWW-4IE3gtP7DWa-Nstuvckvp0vTRurg5dqaMPH57Hz1uKxDeYv6K69TD5nK53NT5mCA2lWjsTn7nTPDRFbaae4NR3mFiVqAp61eSdMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUdwVYldxtMWkmLlSa0FYpmH9KAcVz1pws4a_d_C_Uvxb8guatPkl4K1qpPrvxGduNTKYfUN5YPU5WEzCnsRh9wVm9pWHRxMrHf63rbkVSnLFPnsATc6l4Nz4S3vuIkB3Wdgfqywz5v3bLIytDv35wR950WZovm2y_EnlxKikuDxdVdUIWclDKEVvVArWRN2O1TQbRwRYe6PyJJktRgizGMRTPTP24SLZ186nrt4VGefXgZJrrxiXSruHd2jTOk9yDsgq_NFq0NEwPCjbVAszs55D5sbTjZuLhsjJLKZGSQOTbyUG9JKO1OYfuayX03R4If70q7QKElpw3I29QhfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2tdVFX0OBSG7pJezZexT4DHr0-Dp06WzdQ4wmJjoLw5HBocyAB7CubrPpWgIUQaf3e3yxWpHrSbJXLyA2hym2aV0_H8WWKlSr7YT17i9hrADxQTTLoG7oBvfubwijtqWVBGGiiY90cRSIZRpbOom_YhE7MTwU5rEe54e_iDLKEQ9_3hj5YpfwB7dVh6W9DHrKDIzkTO8-QN85pAziHd-rGiUWAS_8IdomxeyZ5fIY4bmbZR_5kkoV_4-Bj-MXTRoBRiZvPgoySab7I8uYHLpQJVhFRPDihJ7i0Sb7zVXg-0qdno6EiNaHcBZFL-cuAjIRL0p3r48QnvbAvopjK_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpnReH3bAlmqP3Kxc6pHejpJQE1LiCGoMb_9172YGGc3elPWIFGuHqNAkBCaGltur_PU6vUQ_ZpNL1zpd0NyfzzlGnffueoJZUinCtbj0pAU7xgBhn2WEdeeQOkgiixYz-laysIVPXe5PQh4jukX3spFyK3w4sb7lRfEsQGnL2up__qH9cm3mgpGBudvsRnBiz5eVi62c0H4aM-KJxzRQqVX2S_DXObeCr-MEycIt8R_DBT72VFs4Bs_WPwiz_MWDeu4z8gU0rTZH9WukBTEgxxmMkZwuYSrIL0Uf4GysrPuyMJYAbBaV4bSwHo7rnQ7OP3TiEDb578GlvdfkJ0YNPfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpnReH3bAlmqP3Kxc6pHejpJQE1LiCGoMb_9172YGGc3elPWIFGuHqNAkBCaGltur_PU6vUQ_ZpNL1zpd0NyfzzlGnffueoJZUinCtbj0pAU7xgBhn2WEdeeQOkgiixYz-laysIVPXe5PQh4jukX3spFyK3w4sb7lRfEsQGnL2up__qH9cm3mgpGBudvsRnBiz5eVi62c0H4aM-KJxzRQqVX2S_DXObeCr-MEycIt8R_DBT72VFs4Bs_WPwiz_MWDeu4z8gU0rTZH9WukBTEgxxmMkZwuYSrIL0Uf4GysrPuyMJYAbBaV4bSwHo7rnQ7OP3TiEDb578GlvdfkJ0YNPfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
