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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:  ما اجازه نمی‌دهیم اردوغان سوریه را علیه ما تقویت کند. ما می‌دانیم چگونه منافع اسرائیل را دفاع کنیم.  در حال حاضر هیچ درگیری نظامی مستقیم بین اسرائیل و ترکیه وجود ندارد و ما تمایلی به ورود به چنین درگیری‌ای نداریم.  اما اردوغان…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SBoxxx/19360" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/19359" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، آمیخای چیکلی:  «ترکیه اردوغان و سوریه الشرع اکنون بسیار نگران‌کننده‌تر از ایران هستند.  دوران امپراتوری شیعه ایران به پایان رسیده است. محور جدید، محور اخوان المسلمین ترکیه، سوریه و قطر است».</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SBoxxx/19358" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SBoxxx/19357" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/19356" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/19355" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز: در پیشنهاد عمان، تهران کنترل انحصاری تنگه هرمز را در اختیار نخواهد داشت
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد عمان پیشنهادی را به جمهوری اسلامی ارائه کرده است که بر اساس آن، سازوکاری مشترک میان کشورهای منطقه برای مدیریت تنگه هرمز، با دریافت کارمزدهای داوطلبانه، ایجاد شود. بر پایه این پیشنهاد، جمهوری اسلامی کنترل انحصاری این آبراه راهبردی را در اختیار نخواهد داشت.
پیشنهاد عمان از حمایت کشورهای منطقه برخوردار است و بر اساس الگوی تنگه مالاکا تدوین شده است؛ الگویی که در آن استفاده‌کنندگان از آبراه به صورت داوطلبانه در تامین هزینه‌های ناوبری، حفاظت از محیط زیست و عملیات جست‌وجو و نجات مشارکت مالی می‌کنند.</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/19354" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/19353" target="_blank">📅 12:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axaQlMJBv6sJG0hcIXbRd1E5Nme04Fhyi_zptcWkSoxquFcp4jUS6hBpS0OIFCXsQZnr-puoxhxLajODHTc6VEzzCN9VKexHVDZxx_v-7lvNqZ88FSOTZH5n9mhwQWf7-WhenuLTDpm5vj6vkIiHsVS7NyFzQ6EEOKaMn9xYqLFyJN8kgVns21K7VgK6tcg0G62487_sLKlLnEvjTtjVNsWU4sBIPRdcwnD4yKNwLi8Ipb4ed-fEn0wwXXYMFBIMS7dhM4Hpe3UcCvr6sA1u4JDGCvjmy9saNOK9oZjszWr8HVqdZkK5bNnAWbGywUgf8ynvyWEYDUfSNPitBMiMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/19352" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhsmc-_UPeyrFF49IHUgUZc8svqIPDjJjZNqpLmYRwRTwu8kzZxV79QboKyvQ-I4-b2yRZLH0o34UfAbVA3DQc2S9xFXml9To7exytpNN66sr4_VAG6o8W1uDdNxFuRBIKGp7YVrF0KtX8tKhFDuZ6AnWZe0vB9SQP0_IKLW_sBxgyxJGQ_DHrJvOsCF8vCp-jAtTDzTRtF4-YzNTrB7T7x50vxmOqWlp7WE7dJvpbK_jNUGXEjindp3GSyBXEx9amlO7PWYKSKz-4Nb4KS94DkybnGNM6FkIa0dAjTDdrZPmBaKhJORneRE5rojYIMQCpNBt6qrSDkDzgWfSDn9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا زلنسکی هم به آمریکا همزمان با نتانیاهو سفر خواهدکرد تا دیدار مشترکی با ترامپ داشته باشند!</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/19351" target="_blank">📅 11:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=cCKFq33D-dCSAMF3u-DVrrb1OaLcwh2Os0wfkGMlaGSBsCzhBdpREfXDig4Ai-PSWU6i0f9aNW4Q2YQjQS2wUv_d5c9Bkm7ut3sNJb9kUyZfctRx1TEnGDZ8BJDJOS2VLIgoNIy_0MfXo3IRdusZ9O_PeccY1H_2imUahx2SR9vwu44Obb69z7MCHUF1-21gBWqRQbx3Xj1tW2C1ryX7L5j0dZ0y68inkjyORA_s0kKGKL-hG9WyZgHizPP_QyYdILTXcZ24iOLW-OeUYAbh2_pQE1DQiLeEF8g1Qp5S2q8pbetM-tC9IeZcw8oDGCD3TTk8ohalIFAov_eHlVcgOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=cCKFq33D-dCSAMF3u-DVrrb1OaLcwh2Os0wfkGMlaGSBsCzhBdpREfXDig4Ai-PSWU6i0f9aNW4Q2YQjQS2wUv_d5c9Bkm7ut3sNJb9kUyZfctRx1TEnGDZ8BJDJOS2VLIgoNIy_0MfXo3IRdusZ9O_PeccY1H_2imUahx2SR9vwu44Obb69z7MCHUF1-21gBWqRQbx3Xj1tW2C1ryX7L5j0dZ0y68inkjyORA_s0kKGKL-hG9WyZgHizPP_QyYdILTXcZ24iOLW-OeUYAbh2_pQE1DQiLeEF8g1Qp5S2q8pbetM-tC9IeZcw8oDGCD3TTk8ohalIFAov_eHlVcgOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/19350" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW3kw1xjLx8zQwl4Rqm7PATeTTtXtaNqWbSA1S3tw-eBwqEhq9LGwBbtkv_nGQD4gw37yNdKb9xtI9YFHaGoLh5Y_qQM0WPDj1i4lFQUNX5a9PCQbD2d8TfP8kt3IT9pGTLqBasNylOba8oGHUlv_gMqUQvZ9kObgngk4v6gqTEpPRrCjuylzo-hbVj3GXWTdvWmliGIadVVx2zYI3JqsOpV_iBoDfSBlIJPSGz5JtMrIa6zUzeF1BXYC6POLrs3tSmlEF4pcSerhGlKZc5QAQNrZh8aoT8kjWhOwIXOs_k23OA3TP9_Zo50VsDawKlgM8WwZqJLcmZDh2B9ulzldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/19349" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grBDKDJi5WCYS5erOA2TQLjjbl6dVRBH0VTV6m6XHiN2AKfVfLRMOQcNGN6OOLKAhTJh0xhxt9w-smWxU_D5xqWM2_DoemOaIn5EIQxQy9dE2R7dQlY1gphJPrtpkPQv5P-7QLUNe3FlwhrWb5z3bACrSxh4RyPlrJy1Yh1WWuRXsBONBNXMJB_xZdC28dGN5tgxZjY5rxA8lfVZgKzp9-Hf9-jWJisFTeXePJ4g-2YQlPNTGyQu_JwejGvDHOKz5USgIf3iiWC-Wwwx6RCeBVH_4twjax4XfdqH3kOt7kI8hRSrV9qcvL2CqhKXh-zOo_9MuXq2Rj22X6uAra-F0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc3554F2LmZeUm3I7noAZ9pQCnM44C0XV7XhXTKkqf-Yu7gjUOjRDv0KfZe4vP-DXI7LfLFqR8tf9qHAELWjvf9C3bAsl8BUmZZAqXGdHs5IAthwoc5wwiofDzi1D49LBe02c4jIm30ERdcziTtRPQSfRmd80iHSOy5Hto03WEWehm1BYO3bjMrWaRidS_odBlhXTNGBksLTXJAa1WI3jpfVMI_pGOM_E1Z1T8f9tZxzg7qjx5qcMQVzDdk7JCvhARrVux2q6E10Fq9pOsqH0tTwgsh3EaTYDmkaICfa984pZqsCpwf6SND1PSCKPo4ne4TGEfNmtRD7J48xhvU__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONveGHbFRPVNL23ZXjLSaox2Z8_zx9jYa-uui8kxyKHw6pMq_aGjZwXmVspWP5jkGVZW5JQY6WVXGnO4JSMmeHCnigp54Ks_VgyCsyB9NSVZJmiLB_1MzQ-pC6O5cr1ZQqO5OIhxIkIv7s-C-PC9I-Jab9aUsF7R3g1PM2wJCw9okDWKZyV8bSPHoZNR1y7yBtd59QdpgvMWBaHLNCE1oPKnGn7-LahytYQZMS53LxmMWtkUyUUaGljhtAmNr7BUOBlQfRyfBRvCrOZw5FQINGzFMGko9MwzSTLbKLSCtRKYMb1hMMmoCTC58Pj9G40TfV50VnQcx1veGAQF6TfXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=kRn8fQSjTUhOQq9kJz6xrDgfh1eFhpoRCDvhUta0aP99V1k3M7Ksxv4yWwGbfdJIicbB1u_MS67bRbY3PVXPKDX1bCpDfOvsJddqEh1rf-ZGFOQHQ1begfEe9RiGgmELL93eBD8Y9LGTdjzNHi916dkURQ0G6z9zWXnXqu7LYVZsfXWme_11RvSkghWlZl8ewLUh8cHt5wWoVen0DQVUWsGvjgrQdfJuPxc6GRyFBrvx0FRFsA9XPRQyODMeJoz0vmnEL6KMVYHocqKAoZK1nwMsyTAtN8YR7wwMik-kvu8-nm2sjfz4QdpVAiC3yl4w4sQ3JCAxZFNjM-D3nRmnFiaTJgHyCYnFjzdjI1Nchd-IaDEuDVUKql2jrHU7fAAM0bd-kct9yeax_CCT4-kR0h0h6wWJAVQLseiE067DVo42QQk_TiW9WBtnoyWSlbAeArdjmd8IisrDvvytLgO4iIyG1hmZrPljrbL9B8__q9yWPqGfpbbue9Zrzn2Xt4AmYjDiFXZhIk_wKlBaARQsVTM28la949euLZ6s1gZa2s5kkS7-f8XHu1kR_91Cpq0TgfGcqE_ZSjQkNdyncrYuEAIgOfbKKvg0thLmlsy8syKfkFPpWS_WmNhpOhfygqGuYs1kqfeUWgL4U6tzttYH6L917WARM-sjMEO9oB5yBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=kRn8fQSjTUhOQq9kJz6xrDgfh1eFhpoRCDvhUta0aP99V1k3M7Ksxv4yWwGbfdJIicbB1u_MS67bRbY3PVXPKDX1bCpDfOvsJddqEh1rf-ZGFOQHQ1begfEe9RiGgmELL93eBD8Y9LGTdjzNHi916dkURQ0G6z9zWXnXqu7LYVZsfXWme_11RvSkghWlZl8ewLUh8cHt5wWoVen0DQVUWsGvjgrQdfJuPxc6GRyFBrvx0FRFsA9XPRQyODMeJoz0vmnEL6KMVYHocqKAoZK1nwMsyTAtN8YR7wwMik-kvu8-nm2sjfz4QdpVAiC3yl4w4sQ3JCAxZFNjM-D3nRmnFiaTJgHyCYnFjzdjI1Nchd-IaDEuDVUKql2jrHU7fAAM0bd-kct9yeax_CCT4-kR0h0h6wWJAVQLseiE067DVo42QQk_TiW9WBtnoyWSlbAeArdjmd8IisrDvvytLgO4iIyG1hmZrPljrbL9B8__q9yWPqGfpbbue9Zrzn2Xt4AmYjDiFXZhIk_wKlBaARQsVTM28la949euLZ6s1gZa2s5kkS7-f8XHu1kR_91Cpq0TgfGcqE_ZSjQkNdyncrYuEAIgOfbKKvg0thLmlsy8syKfkFPpWS_WmNhpOhfygqGuYs1kqfeUWgL4U6tzttYH6L917WARM-sjMEO9oB5yBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6eT2TRdRog1O09sbpIQsD6zDFiY5F1CjVEOC_XC_5CNFj5mZASKkT3RkwrkCH_feBaShnkGlE1X38DQjIUFZE4MEnYmiCEmn79G6ndMTNh9P5Da9qdYllQTHZQdvs7UNWqC6zM4CyFb8lJk-3BbtbUsugTBtSOyoJu6gSEXCYVtPBfE3A7jkNMr3Urtr1nVZkvoebXULBRgdkbe2v2HRIxlUaOsXeCxsCV6Pd2PsRjcqSKRUPi7t1S9BBnOeaaqBU5x5DLdTNNYH3gKUbN6mPeZuIY5_wzglKbXYfydOq7y7BKT8aLWkfvxngrMWjlzZwJWKNi52Px_zdCDvyS1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaBYVWo3TRXdZVG0HZpyc5m4_PvoqeGRxZ7rovr0XO1tuTRLojAxBeQuRd3U8I6lQ85d702x7W450ebC0F-vCv_ZK2gRrAK8TYXagouM3784Jv2qoEwdom67x7uFGpN4mbbuzLJ4hgcUbTH6vz5CC-GYvRX4Nt1fcujo0ol5RSqNfZsf3-BLz3Ce5BgntV97-7VqBc3Tp1ID_Gs3npZsN45-wANVvMpCks2fKtcOih_lbppKyvs9cQh2JCYhFYPtqFb5XY-bHsPeJU72PRqkO3um62QE69Zc8LP--9cfwffdC5WgwKP7N64FhDCk9s8EBDqN1aUVI1ItGhh-3OWpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oso-hdOHHXOuvTtJYCG2VSyIvJH38ySTSuKmMmJMJW9uJd-rSZ3lwGl3fjEr5pl2ngKq0-SoXsifXTlJ_ppBGeDLgEeguvEEllNI20u_v3RH0emekQTgqndUCwEoiVDq0QoW5a7fm5CD0D9esw3c06lVzXBWUgtJHbTPBbq2CshL8AamWpfgsYc1Pj2vwS58oF7gW7aBdNyUX3bTpoHKReQekLzl8ZC8BY_aDFOsP_lJHX1lvb4Di897VtBdihKWQCaQaHBzqzIllts8nu5ibfwlDZ79BLtRdyMOyDEXRD97zly8zHiSPhefv48xzsjdUCNSsha2kusNft3PHhOFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG_gdQhfml4KoS68MHjWOytU0l8mPD4cdeIb5MiDtsycTldI33ovg4mBGN5lOPmDhmBtTwyRTsZNcN93WG28T8x5k5fECqf0l15_TTbLjKa0zr9beJAavG_kQGAntaMZNVloSKxBAOWoX0IGupO-xZrpvQpd8IHGH8v9HNo3x4YyU6HOBwQhzHjxQbqRPDlsgTxs9nfhqOdZmLWOFRAiEPpS8NxNVTmiqJIkqsfDXBaSm5lrZI06ZwDL3wsRdjhP6MZlAthVtu2d-adpAMeR4uwPJMZGsCy5cwLg-PThtKu_J0ns6mD99lQzOE4360Q3vh-TNZaNKkHSSbnWCO7B4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOMkYvjk8Gb28KMrVQNqgrSQlyiA9lCRct6bhSAWuHUY-k96ybEPMsrtWiEj79rdSYoswwV2v8AySs9GSayfS2CmbwX9FwLnf7AZao2CUI5ixglBZeYQoPxRrSa42jQUw24lepvW9q9ZXQH7ahgHY1fhwsUWHO8tLqtbkT03_IIupBhTxUFJMtKPP6Z9Q_XcN7-mMmH9XJuF-oaaj0n2x4se5KRsmQ1PSsthi5ZdN2qLMuYMA63cnW92BSNCYamATpf4B9PjV4kc8gedhKUyLNUQlbZ2Oary7oVvllW-bS0pnJobyFR58zlpQozDWTK-Nuw5tlnUCCk3W5_6lGuSVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zdp4HehuYjcu6K4oNKYhpLDWLbialsgyfFT8730FGm4Vq4ZbVGYbc4hIQ9gsb-EKaFQUzqxy-OilrVD-qQ1U3kg7QBsGYbPV66ID9oIzZ-0UQy-Bt7x8UFzJ1RsZfq6Gq1HjJGR3Xd0HL48u8mcCzADRaQdhiAIouwIzdmJOrhRum7qGV2A3sWCV8JeNwoYmV5-CmCzKB-6rdbMj9aoxmKHeHG6VNcVzzNQTTic9l2_JeeQLJnoVBmz-h8UmG0iJlLEwrw242j8KyAWApmGgot4Y5NbHeqkJqZayJcioY-jPmZj7DNEtA38fYzVJ41mrWcDar1ORZd649VdRck4eWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVPc73sXXgld8pYIu9v8pX9NuGXbPmAxwkrYXmiiKZxXKB4jkCDwizFqWiqcymDR4mXYDFgZMjlPijQD9csmRkOOKPoMcYzZi0eXJ_MmsArs77TSgULXmVuAlRY3TGcdyLx8eeb5ghZSP0crhNMTISbmbe8i43GQHEBi1KzWbYvusfh8YYFKD0CHzLBfzz3I40iQIVjUZrRZoYScB5kxqNliYBnPisYqGOfrMHYS5luCOsXUyB3Ig98VeKilSAryo4AlvdRXfYUiSyBnhPBbxoTFYUeiMNQOoTal1dNpiJ3ClKAVbxmIPq-GHTnL14zR-0pjWu7KkxovOzWNCU1Y4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VijBBo5lviaQoFEDADjAdWXHC5G779Cs_roJqgP3IVkE_Cue_lIf0udDug6pAuW2gkvtqDjIQ1DxZ5hzgqrHfBrWtVh-WFc87FlpT45d32EpjQ3p9SUJ62oA_OwwEmEOUxP1xJSbCbyBD_urSAMhZmDbptjSvBnAzH5iMcF3ZbDxJmE0iwEkJuD3D884ixrmPxTUcLXxLeHBAQHL0VSoIeo8ZW-zELX63zwXM7N3ANyMYHIHl2pu3aEtoJlv0kN_eLSfu0YrCAlJPth_HT6FgniZjH2tJ13ZwmhZ9nRhd0IrHCJrdQkbxEO-_2i53DYwkpXmwHOtBJI3EQoubkJAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmNAKOH5HrI9d1w4l2nyeWTGbUuq48jwbzQB4GP_ppZrjqvpNW5C1FEjmFCVVUJH5E49IH54PpoDNUQkKoPoLxeOwxMzKrhk73XkdZE8WKImdPTaGUqUsFTTatcSYVNyUBYJ-NZmQWnWawr7w68ED-IuGx-7RAa4QXB9T9U3aOaYc4Sr9NXHViuhLPXtKLWGqL63KoUK9ghyeSOE61rXzJRKDAfQykNVN7jANPKE8znC9qIPNzyBfG4ospKVLWyjKZqYeOAw7HoFb7HvfogTbPWmTW7kejVrYp_yAC7hhyL3IE_B7NUNylVmbxmQiBFbfqQg6DB--cp9Go0Ur0EfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiSQHWFlpBRuocUU7LasWpAL286t00-vuivUOqRxxzBfGKN8_axYCb2MQtVk-txkNEx7twBEZQ_Po5G3eWxG3CoETQysrMCgyR7_bqneAmJk3JCS4hiLwIR53SP49YIn2dQkJONckHF0jrI7ybQBzKSR-dD2j4-1V8ciOMtaNayDxM0HJNrOyLRZc0vuYDJfvhPjcdMFEbJQzrStGydJQnH63_IwCPoRq4LL-BmNQ7NN3IBQ7vITLTyseGD57RuqJv5ArllZeS-2207_x1VFVMY0pqrX2in5-AiO0aHu4DZt5WQPxlHgpL1wzGw6jUMI86zhKBw4_AWLqC8TCJq4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3PQRFTnJarXMjCHZpXmZG9D3wrcFxvOk4TiHqFPAZUWsAft718VGEw8MmFGqwEjrxrzal4K0LzoCK1OGERwlxr51KhLdP6byPBuzxHJm2-W88X_NLp5cDKU4Xgnhol8y9aCAkb6I-JRbVhtTLyTfT7fWKYhW67XK8Bc-NyUn1_8rPtR3_oe9vyeqmF_Aouo3CFpx3vHgiY3T_jEuKSSG0A6FgXmuZa3XggDtgwcjIb2Ib8gTjQ3BTeaWNpSKQi_cLDWsE-GIfWUmtx6OcvlwCC-fwAIuqT6lFKFkX-JN9ipwq9_FWsJrT6MtZkLbajbL6OkjbZUIx4BETPFm7GqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og4JdRueqRe5OVE8Fao9FhUQTdGqx5HUUOsaF4OgdsREom0j1zHPJnAm2UdzIzkyRtjL369JHW27tmwsEi0lBoFVqrn-77xpI_oVhg6blA3J2G7Htk1b83mHopxW7qXgWU7sDF7UuhezWhIF3ie8Uu9reh0R7Hfg78f2CHYfBHAUTXL5W6qQwed9w6fVgCRc1UTZs-XcrKEnvMd_pY4XkOUnwH3a84KR4dYntvtPIA-dL638uc0-k1ZpKCc6gBDlX3Dt_saPojRRvUWMMsBDD3VoE2moNIMDeAyYvD2fijpWTYbzxrT2kseZL_A5ZZ3XAI6--cuO5hYMNg9txCbZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg82B8wtjPXVJGh6_uc4Jm9gmEQ4pj9ylBr3pbHxLRcPABxhHTtVDkUfK0XuD7q4-L4YnFXs-43Nb2TXJdhc8kPwd01BiPci9VeQLUg77kpYP73fuQ2waO0U3DioO2yaQwe4KKoCGfkJksklgkDrtVyjIZI1gj84SoU8ILUJot6Ueb4wrNprdW5afcqtRbfm1uVUcuQxftyuh8d3fPoYRwhAKE5JXeH9iPOwiyQmMbHhBd6XfNZfnGZJZU0n9ktzhqXxvhfFZMbNsYPc__kNrQCYRYEDDqVzO-XY2hp6rNSv503xP0Cc3oTpN5IRxEm_IRXY4C4clY-Y7snF8kr02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ1adVwOiePQ6OJ_4WdpLl59OCJdBivnRcglVfvE7G1UuEdiqcQmijepAjcJRt04MJXpEZP02jzIsqEzqmjQuXeHh07xeNUZ0EdqH7b88UrJ8Om_DkJxf0WAbGhToE6RaBm8y_urqo-FSo4pfMGWph01D-Z_54dzA2t18c960ofjk0X19l27Btza-X9MNaNI5KV1jcJCfj-5Kpin-tFtvW_nDUD6zwstKUhZRF9DJ4CCSBAOfLosS_AJPBY6Z34RI0C7BkL7hCGekW1gXLEYeiiUZyOoj6oj4wS8_JBOLqIaq1wCWVnmmkvAgKrQwpXHC3i7_1vAJTYkxsOus2ogog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtJH3VxYvIAZQ81xisMd6HFwM5i4FiNJ7Q3bxdq4e_BzCOBrKPtqSk2SLo6MUIhl7bFILOMdO71-WyVSJhQO6WHDxGwv1CiwcZiMK3Pkst0rGmz5iWF72shrZWeBjB8tdjP5mPPIIpjsoh_qujpOXOj9zmaFIg5uilCRadeOHsVxgNr6N6oAztjIe7TYkmgFbi8p-mOXXTyFm9-S-XSlT1ElF5NQaMjfNkfmlIfDWL7w78_oy7IjP8Y7QoCVHzSAfXHNw7EUvFd4IvQZEjAEYIsO9uzZeSoqa3-cKFj4vGp33NKUE0lZZjjkgTpjz5lWFHdTGd3Dq35iD_gB1K4WGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsUO-FzQCp8QVCBTnVAUSNki1kar1s6in1-MksnAz5te_9UuzSmLwRCcrNszbrPop0pXUp6Dkz2rw22ZT3D7mHH8vFf84SdYBmq32PBmRSC4gkh4n8nFOx1t0e8OxBKmRZfSrttgQIBHH8if9R9gYr_AzmQXWC3tz7AAvtcdJM132cSKZGkNeHfy48Oi9yH3O8UHAe1D_pjtjAorvBlvnOfQTkehQmJC5WjXPPRf7YxFMuP2nCANFIlcknP1rWTcPL2HKg1ToysrUNWI7aUszkRbSc3S-PLgCaxf4X2xAw3x06tWjSDqZuWygVhfwsyHd2Ue5mG9dER7T-sVrrdCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prwAjuYZ-13LJbmOl-azXbfoEUOykJG3_MUm_eW9aNuvYgCjfWVv8TXo-SitZvv-PhNR1nxvDYYN35My4v4LdFCfIT-WRinw20_VCCRRHZn0SW2v10HftLd6SuFQgGpvkWxr0rXHBB1vQL1h0hAxQajW24LhDDBbGFCHxvMN343hPty6UKM-8715ufmfjUz4StlbyYGiSzzQZa1fT6jjLR40Gk9cfMfgZO2SWPYFWy8kVXtSKpAsS46N1aJTIynQZevLnc54OqTIIBdD615KCwM-KniT6_Jlvr-5rmsLdfbtu62dneEbVu8MnVNByngR9I3AuE-NDqbe8EnwodMRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM5iR803Vc9vZ8hpmbts0nZoxWVOzqixPop1WD25zLe-1fyY30G9EicV5ThKP4Fv_sCwuWUDDs83y5RGIPmYln3aMvb5JsVKxjZkcigrvFCnnBsb_GJ2pFogpEbg69PnyCzt_Lyx68oeJRqVuTf0Oek_04C--t86d8vcF5jXto5UHtgWpxGv4CsIt1emoWokVRG7wbE9gVCLtUfcDEPWWJq8uJ5jr4jtQlazp4r_u1S5HD3msbVYGy4XQI00myS8X14D-f71mcWVsZD6g5NKM8lFA8ehe2U86i8WOyZcIqUDMZUEOo1cA4bMzt7fYjbcxxcUgK4ndp1YjZyS__5b_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDVDElOR0BcNPvpQ32cFuRlHf1eV54q79RZ9Q69qDMLpuijFmU2kOH37KinemF68DsVcrhCI5VRoCl1kvkjv-kmxGhP98joNhpAPWoQYksIaBPxll0aCfwXyfiMmhddaAs_Zc8uY8awLaNKV7lQomHrp_YNmbS69k3eRUKvugaXuDM3mV9FLEw051le6m80gkrDiL9WYVvz1V3AJgHjUVtkqIDBNABgdCysY0O_s4rTV6vJikfVlXBRS9qWGYftxnAYoH6eWm5uapbH08kDMTasiuSHnYLvylIbzMm4ZHfDu463osP1Rm3X_h897XCN3SLJxfvCrvAUUuKU7rSEj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUZQr5Ph_u5bCtxyVWSYnaGfKsxNJ8EXusSr8ncPr6wDzPunq4EwuYd-ius_Qtv7reslDbVhDRor2D7Bex4CGCZt0ExpThwHCLlApj8XnrvzrIF6_l264O1bgRthxzhIEXcfwuVCvptq3dYu85GOwb_mpYNPkVijddroHrlsWxfHebWtmLw-iT8uASZbW3XAKL_VJpMxg2vi12dBxHblhMYuiU3PbX1u9Phmt3R7FsZpF7w81-HradUnonIcrlfugKK86y3wm7nrPri08fSq2v7AQCvsWe2kSj8NLBuKJ55SB5D6oVTIwSDnXaAEIG95X6-6duuG0hvpaOp7u97GVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=lAi57I5A48nyyV0r3OdNFEHnGPGowJs4psSqulJuaxuCf1F2b1VqORGQq5wu2G5L1KvWqcXy9G6RqZt4GJmfbcmEDL9oIv_fnzh7fRuaMk014WZh3bSJfiZHt8IRZ_qoqbrIQvASetBaAk76vftCZ7-qdHrSRJPN8Xdg9JS9Dhjj2-pd4Ekuur4OfP5AZcMSgkmSt5MkYqONyI4cs3-OC76vLlMaEfvYjoBHM6q_LIxuvTS8ArOaATAQBUPq0U9IF4epzgB0gJ9UHmKsEZ8SnvlxhUyNwOQA_Kk28MXvdNge77YhhA_Yc7_aDj1NNfOZS7o8Tir-9Rfpqf2keasTcYyqcKDfa8rmkUTVAA9AuDaGWkUVAyVQfuH5g73K62SyhCsSNW_peTO-os5DSZ4NG2s4yhjfcWyr__kOFrs1LVjnj3oL1oybxQ5PEfId2rBEROQYl_YEEPygwryYgayWZHZ0gtnV6ZrpFB98m7oIBHd-xKkFH0knpZorxkJgh89Ibeat31MvHPYLO_kU-Xft66baN1vTMzrV-lbIyMcjJId5Bt_6kwdueoelkGyMlk7o_ZYBj8sBtASz8wzScicjev67FZlPi9JAgw94miYbZPOJ2tFEQfhs1a7AXFz0IPJTop6FAu-DrkiUFYl_Nu3ldVuvXO7RqoaBMHY3dYslnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=lAi57I5A48nyyV0r3OdNFEHnGPGowJs4psSqulJuaxuCf1F2b1VqORGQq5wu2G5L1KvWqcXy9G6RqZt4GJmfbcmEDL9oIv_fnzh7fRuaMk014WZh3bSJfiZHt8IRZ_qoqbrIQvASetBaAk76vftCZ7-qdHrSRJPN8Xdg9JS9Dhjj2-pd4Ekuur4OfP5AZcMSgkmSt5MkYqONyI4cs3-OC76vLlMaEfvYjoBHM6q_LIxuvTS8ArOaATAQBUPq0U9IF4epzgB0gJ9UHmKsEZ8SnvlxhUyNwOQA_Kk28MXvdNge77YhhA_Yc7_aDj1NNfOZS7o8Tir-9Rfpqf2keasTcYyqcKDfa8rmkUTVAA9AuDaGWkUVAyVQfuH5g73K62SyhCsSNW_peTO-os5DSZ4NG2s4yhjfcWyr__kOFrs1LVjnj3oL1oybxQ5PEfId2rBEROQYl_YEEPygwryYgayWZHZ0gtnV6ZrpFB98m7oIBHd-xKkFH0knpZorxkJgh89Ibeat31MvHPYLO_kU-Xft66baN1vTMzrV-lbIyMcjJId5Bt_6kwdueoelkGyMlk7o_ZYBj8sBtASz8wzScicjev67FZlPi9JAgw94miYbZPOJ2tFEQfhs1a7AXFz0IPJTop6FAu-DrkiUFYl_Nu3ldVuvXO7RqoaBMHY3dYslnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlHYD5T7jBrnlUm6lXJArMEpYaHKkps1dAsM2QObCDcK650mr57Bf73-ZBMt31bUrJVZ30VgODntpLv0DL2T-oTvk7RBgyVWFBTuKrRNFFZ6WlQTWztUi9fMIvYA4zeo0sAPWJUxkilkVoqZtLhRNlCnM3hTEb990d3XqTbQ4cNOkdfQgkONW0Vhk7aKrt3EmpJx_nuLnxv-_eCxxXpt8Xv8OM2VDET20Kq7uh8Wg_jFVLiTlzCLxgpr4-PESpjDkXCUqxfWipd5oI8N2qdvIsxB8uztIUAHQr3xyKt2HRsME2OcqUX7ETEdWDZ_vgPz4hxabvi3aMJtQdjrZFTGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=KxUtPINURF3hxGaTnYyYa50FUx_qSoEdp7Xpf2NfSXSXqBQwOWr3S4G4iwbQ4mwlI8GSNdDDO-QQYMDy7RmHcYPvSWmhsHFyFxt9XSRe4ZJ2vKYKBANHoVUdFWU0DTituIq9QdvNx_AAUhnoa20eEZxwUKt1yDPBWfp5Yr4Kmc6W4g9uDd5e6BHtB6cIc9yYAPUOQ7hrKMMX9Y4xEX2epxdJqw0MIdh0PZE4WGJFeSQaqGKUOAtexlpZ4sqXv75B4nMXzjzHwoXM49LpMePH5VzFFoOVMtCa6NADoP8b-A-uhBfQMLs2_P3RB-ycOyGE9yNWMhiWTguyDlf8iXoVTa4bs11HVs1xT-cSByh8iE41W-11dIIwKLRqqT9p7tArHz_ch2_FoU1ae0gRd_ledlOa9BO4503Ee7bS8OhqNmJlbCfaetJvjUx7qmVNELTsG4jiAa5Ac-JMBGXqbWKHD8d9seTkv7r995gLSem6W4WLTcOd7MJ0c4c4tELpAsdxs5UsqwMo9rg3yLprGC9J-gg0G1o2pJ5GJx9LMCXq99TwVesKwYCwxm4pFJTZ_Byko73vjb22A9wVrdLx1PRNPzn_d25nUm0kTmCNTFk9QkxFJigPZf1hWCdfOFMHV4ZcdM4VwuadCm0tHcf-V2DlqSAf3FaxOhlaZHAvBE8HbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=KxUtPINURF3hxGaTnYyYa50FUx_qSoEdp7Xpf2NfSXSXqBQwOWr3S4G4iwbQ4mwlI8GSNdDDO-QQYMDy7RmHcYPvSWmhsHFyFxt9XSRe4ZJ2vKYKBANHoVUdFWU0DTituIq9QdvNx_AAUhnoa20eEZxwUKt1yDPBWfp5Yr4Kmc6W4g9uDd5e6BHtB6cIc9yYAPUOQ7hrKMMX9Y4xEX2epxdJqw0MIdh0PZE4WGJFeSQaqGKUOAtexlpZ4sqXv75B4nMXzjzHwoXM49LpMePH5VzFFoOVMtCa6NADoP8b-A-uhBfQMLs2_P3RB-ycOyGE9yNWMhiWTguyDlf8iXoVTa4bs11HVs1xT-cSByh8iE41W-11dIIwKLRqqT9p7tArHz_ch2_FoU1ae0gRd_ledlOa9BO4503Ee7bS8OhqNmJlbCfaetJvjUx7qmVNELTsG4jiAa5Ac-JMBGXqbWKHD8d9seTkv7r995gLSem6W4WLTcOd7MJ0c4c4tELpAsdxs5UsqwMo9rg3yLprGC9J-gg0G1o2pJ5GJx9LMCXq99TwVesKwYCwxm4pFJTZ_Byko73vjb22A9wVrdLx1PRNPzn_d25nUm0kTmCNTFk9QkxFJigPZf1hWCdfOFMHV4ZcdM4VwuadCm0tHcf-V2DlqSAf3FaxOhlaZHAvBE8HbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbj9wMnKKaoNsQSk9WOqXysDlEi0WCMqgHQIGYouIHko0nSrlPCSNBTK_FVi_COuyPcvyP8Sck4NVkOOoZ6MVziSx6v5NUsxK4SivsgY5S-1Fvup5Liubu7m3mw_PBP-_WX5nBs19ViP0iLSh5akbDmUZxyaAQ2nJ4Vl_E7tInYkYWp6zHZv_H7IHAOplzBKVOassZWxAKoekBytfalonGbmd-IXjILUZCm1105lNbAGf3XkDlNGeOdav9_MPF9TBEioIDZefQiaiOaTXzJgOSwPqVWbUBwj5TsZndLoVU8ojx0Q4gY73aFdNdiEGhcDsd5hABFFXJ2uJR7BrrZC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=mosuSrPjEgFYxd_CA_4U5NMT1GAugb_wm4ACdrl6iE59fVFcavXbJbeqHWuTc41_aYekS1ggMUGHcv24ljb9osHsPr7CuwbJonrq7igOG7XPM4PzL70jc6vlF6JMLAB_h3jbTmzLgja9TCOovZa4ebj07TdPOj0mBhaM9X_AdSf-T7lZsQEskXHBbFxB4sKAYtz5kNOoKzpMmTVu7zuQ8zO6-rPJwlbhUzNYfZyi885C0wnzkDJnLtMCAKyyAcjkt-Yco_3zMu3CghOx4PjUyBi-koakapAY8TB7MUVEm-QHIMShvKgroTbVMqlZqLt6SprmKvLeTyypHZa4lepzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=mosuSrPjEgFYxd_CA_4U5NMT1GAugb_wm4ACdrl6iE59fVFcavXbJbeqHWuTc41_aYekS1ggMUGHcv24ljb9osHsPr7CuwbJonrq7igOG7XPM4PzL70jc6vlF6JMLAB_h3jbTmzLgja9TCOovZa4ebj07TdPOj0mBhaM9X_AdSf-T7lZsQEskXHBbFxB4sKAYtz5kNOoKzpMmTVu7zuQ8zO6-rPJwlbhUzNYfZyi885C0wnzkDJnLtMCAKyyAcjkt-Yco_3zMu3CghOx4PjUyBi-koakapAY8TB7MUVEm-QHIMShvKgroTbVMqlZqLt6SprmKvLeTyypHZa4lepzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUrlIZglDMat8KIe_HckFZjJ30Px3QAmns-F5bb_VXh7yxOQNiKA7c6YYTTfLENL2g7oetu7nCarlJzI2-JAc0KGEwcaabCDO3Lx6FMjMOmxnWiYHerLY_JOQrdLC8b7zTUnyj-udp0YG8zW2H-OPUn0F4889AhVkT7pxLBINjCxorZvYmusMRsuvdUzp8MSPU1AD-cjz8G52AfFEHdkN9XjzxmaefsOmLSyRh5N6IGRFXT-H4qadJSgeQnqtVtwCB4__BjOlG3oJzARuHFgjdc_favybF5M9sZgXSw3mtDvOMNyyy5kEgve5wGssFbpWmwJLc6WSnBPVKv2KkRlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcelspWJodS1RRuSgBs8VcvcI_EyzvFZMcm_Ifp0obBomlkFFbTyth4AABTycXS31hqZSyP5dCaqokhbGP6FpO1OATCIComgKw5fnOFzftoPjXJqYqpZaBMMte1w0NnwKBc6UIKqTZck06CkdlJ9m_syDn2xrzTlVEH96LeiorrJcpbdnJRsy8WzxSoRdnniu5HpAuTIga-7k9rmfXDQTGFcm4ZqeksaW7ebxF9C1laGjcWbg344atkVF7EYBaek5vPNkors-iizR4puI6fXtCN4rsQ9HeflNTANkB06kUJNOgOoHGrOWzdeGd15olHl9lnqHfQowB1V1EIGifnNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF3lLLR0pJW9ajZQDdnMevNvKjYILXE0fbOsp0sIVq8Rnre_wffMJJ4MkXeChnym2r3035Ce2e5TZbyx5_h7-LLwDcQL734U5wZTP7Kp2aRW8q_XZJHYijMEFw9cn0I8GzLRXPWXHeWVF_nzaCETQ0y9kh-3XbsVLYIoFDim4aGoy9JMBwEfz9sUHivZlDj0r7Mz3Sxoj053eQDaPjC-RQZmxnKhY7GgpDahWpwHKif-yMzxFXTHENSfgdOsuFI398On3X0sB2i1ydDchCJntMbNyf7jA9bHzzYSaHLADX_vPCvro9y9k8to04Pex52C6Y5NMh7FG7_5jPv2FZYAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=g9tfyKWLW1FHOwH3tjQ9vRHYAuMjkRrN85bJJqMhBO3qNpvrsNhPpIKzSE-v_0JTO-nmmqz3ZuAfSnyQ6M_I30-N4jz1hpI0W1a0oEU0UMlFBV6QXEnZTjZtzVhx1_lJ7XrAnUR0NujrKJ9gNiQqnvo3EJ8M-CsOToYClzpd0zW9t9nSqMO2FszMp7rEQwiNYhgpCetUTTCOaAm8fUW_ZEgh65ZnmHV0fZqlmaTvaSwHrSmmaBDYU2mg9eHi6aU4Et3QDLy0isiQAYr0SnyhEPmcOxWOI77htIKDqedEU14dLjKUpFmC6J0BQ3cX8h-Ei6oZ5uu5DM7pF_lt6cNcPbOmsZiX0V6rrSHNY73-RE9BLtEXr2Uk-SY1OsFFo1bEP6_QO26d_D0v4aNwqweyWJkebvfL-GouBb7npGpWyKjclMKepKwdnge_-HBwAZLrk0rD0xH-kxIdKoK8jIziSs_oxv1Ejqt7cckOpxlHnjLeMTmey1jm_Yiw2i5f-nPldJFNhOU0mc8HTCU_AjSUsT7tK77xplV-NDuasED9r7nxDSInBCRQtH4b_pUGTP1Qnbt4A5EJxs9dHIduSVbaG-tG2XnsK4EB9bs0qZsScxMyw6BxdMSNR4qX7HyPJ8e9VTPbpP-eJysczanEYawu_8rtTyf72G63moYQv-kfC6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=g9tfyKWLW1FHOwH3tjQ9vRHYAuMjkRrN85bJJqMhBO3qNpvrsNhPpIKzSE-v_0JTO-nmmqz3ZuAfSnyQ6M_I30-N4jz1hpI0W1a0oEU0UMlFBV6QXEnZTjZtzVhx1_lJ7XrAnUR0NujrKJ9gNiQqnvo3EJ8M-CsOToYClzpd0zW9t9nSqMO2FszMp7rEQwiNYhgpCetUTTCOaAm8fUW_ZEgh65ZnmHV0fZqlmaTvaSwHrSmmaBDYU2mg9eHi6aU4Et3QDLy0isiQAYr0SnyhEPmcOxWOI77htIKDqedEU14dLjKUpFmC6J0BQ3cX8h-Ei6oZ5uu5DM7pF_lt6cNcPbOmsZiX0V6rrSHNY73-RE9BLtEXr2Uk-SY1OsFFo1bEP6_QO26d_D0v4aNwqweyWJkebvfL-GouBb7npGpWyKjclMKepKwdnge_-HBwAZLrk0rD0xH-kxIdKoK8jIziSs_oxv1Ejqt7cckOpxlHnjLeMTmey1jm_Yiw2i5f-nPldJFNhOU0mc8HTCU_AjSUsT7tK77xplV-NDuasED9r7nxDSInBCRQtH4b_pUGTP1Qnbt4A5EJxs9dHIduSVbaG-tG2XnsK4EB9bs0qZsScxMyw6BxdMSNR4qX7HyPJ8e9VTPbpP-eJysczanEYawu_8rtTyf72G63moYQv-kfC6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6ERGAWEq7TUOSriwHrmJN8EsXFNEG_O7kNypOBfKb8HztvWTDQlrnPWCe2n7FdnTQ2bm_cSrWlWY2N0tJAIsC4yTz5K1BU8LKWs8ZEsz0mZkfg7PkdHjg_DOo0m542yAfuWOOTWCulo-plvA_0K9-1rqgdlQ4Hwd2Ya2d9h7A9VKCyd3sDvnq_btV9J5YkdGotG-u6y8SSMPznpy83TA0jSDbehKuc-8FKzHqAl4o_ezYiGy5mJSw_W982B9s-c97lhHsvmcTzIjHTr5IflFUkbcvRUxJl_I2io7t-I5lkSEbbvX8V-Pf1m0N42a2AZKJJWCA-WpK9RNYfGKpj8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
