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
<img src="https://cdn4.telesco.pe/file/id5uQZ5JDqhCR7wbXivEfWa01wvd7iHPRLRHwOvCOOY3tC1qSMA6ljkjgsKBksjDN40_ILXVp9vCppuupAgfuONCR1-2jc4047kwtNjFay9dXj66dLCqWn7Obyo0t4mXj4O1GQ9dRVJpaHeYB_4jwqVPxYQ2iVdkHTmq31ug4-JskfmNSSKHQ4QCU1etrVbPQaYvgxJcwcqho7AjZ8FqcG1MxFmTbmQg984koqBjOu6QoU7BiJWI_AwWRrtFD5_3XWHcQytdGtnw26ynbeLN11kABZ4biAMZH38NEvs5mV6y34MTRy-zGSDFaUbev0I8vHAYv0maK_0-cHqkG0E8ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 12:34:36</div>
<hr>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/18514" target="_blank">📅 11:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/18513" target="_blank">📅 11:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرماندار پاکدشت: صدای انفجارهای دقایقی پیش در شرق استان تهران مربوط به عملیات کنترل شده امحای مواد منفجره بوده است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/18512" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/18511" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/18510" target="_blank">📅 09:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گفته می‌شود کارخانه فولکس‌واگن در اوسنابروک با خطر تعطیلی مواجه است و صدها شغل در خطر قرار دارند. دلیل این امر این است که صندوق ثروت ملی قطر یک قرارداد بین فولکس‌واگن و شرکت اسلحه‌سازی اسرائیلی رافائل را مسدود کرده است که برای تولید قطعات برای سیستم دفاع موشکی گنبد آهنی پیش‌بینی شده است.
صندوق ثروت حاکمیتی قطر سومین سهامدار بزرگ فولکس‌واگن است و انتظار می‌رود از حق وتوی خود بر سر معامله با رافائل استفاده کند.
بر اساس گزارش، قطر همچنین تلاش‌های گروه کشتیرانی آلمانی هاپاگ-لویرد برای تصاحب شرکت کشتیرانی اسرائیلی زیم را مسدود کرده است. صندوق ثروت حاکمیتی قطر حدود ۱۲.۳ درصد از سهام هاپاگ-لویرد و ۱۰.۴ درصد از سهام فولکس‌واگن را در اختیار دارد.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/18509" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صداوسیما :
ایران برای ادامه مذاکرات آمادگی ندارد، زیرا ایالات متحده به توافقات حاصل شده با اسلام‌آباد پایبند نبوده است.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18508" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:  "۱۰۰۰ موشک قفل و آماده شلیک به سمت ایران نشانه‌گیری شده‌اند و هزاران موشک دیگر بلافاصله پس از آن‌ها خواهند آمد در صورتی که دولت ایران بر تهدید خود که در بسیاری از نقاط جهان اعلام کرده است، برای ترور یا تلاش برای ترور رئیس‌جمهور فعلی ایالات متحده آمریکا،…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18507" target="_blank">📅 08:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/18506" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس— «ما انتظار داریم ایرانی‌ها بگویند که هر کانالی در تنگه باز خواهد بود و عوارضی دریافت نمی‌شود»، یک مقام آمریکایی گفت.
یک مقام دوم آمریکایی گفت که اگر ایران امتناع کند، «پیامدهای شدید» وجود خواهد داشت. «اگر این موضع آن‌ها [فردا] نباشد، روز خوبی برای آن‌ها نخواهد بود»</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18505" target="_blank">📅 08:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شرکت اسرائیلی رافائل در حال مذاکره با شرکت‌های دفاعی هندی برای تولید مشترک موشک‌های رهگیر تامیر برای سامانه دفاع هوایی گنبد آهنین در هند است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18504" target="_blank">📅 01:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه کم لوبیا زیاد خورده بودیم بادی خارج شد</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18503" target="_blank">📅 01:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مسئولان ارشد آمریکایی می‌گویند که ایران به آن‌ها گفته است حملات به کشتی‌ها از «بخشی خطاپذیر از سیستم خودشان» سرچشمه گرفته است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18502" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آمریکا به ایران ۲۴ ساعت مهلت داده تا به صورت عمومی متعهد شود که حملات به کشتی‌ها را متوقف کند و تنگه هرمز را باز نگه دارد.
واشینگتن هشدار داد که عدم رعایت این درخواست منجر به "پیامدهای جدی" خواهد شد و افزود که اگر دیپلماسی شکست بخورد، برنامه‌های اضطراری از قبل در حال اجرا هستند.
منبع: باراک رافید</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18501" target="_blank">📅 00:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه مقاومت اسلامی عراق در رابطه با ضرب العجل دولت برای تسلیم سلاح مقاومت   سلاح ما که زینت‌بخش بازوان مردان ما در میدان‌هاست، هرگز ابزار چانه‌زنی نبوده، بلکه مرام و پیمانی بر گردن ما و امانتی از جانب امام منتظر، صاحب الزمان (عج) و نایب محبوبش است و با آن…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18500" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18499" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbti4H9J2lJv7Wcv5BssAa92__AFaAL5PRotyLs1GyhPZDlDCc7bZXPcWffB5CWdZMtc5hiw38tDibPmCk076JsycVlF52J9YOsV1N0YbNdAUjlHIapWJur0cWRoyTO7upRfLrCiHmoqKXGkJLpTtgBC8G0KwJZ9t-LKLUxLKPPcO1fV9_vcTFuNwQAUit_T_Fzwntyllz4Ohk16lGCESmDWQv6WoTJ78qLvh74eu0utJmx36dCpsIcNpl0YNbOzpnLa0yBu_-Y9UBwa7uOYcLHxrxns6lHlNnb4vhdTNPEdCiRYUK2L6uSol_ZLeIz0VLtK50fGgCrUZoAWBxt7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا:
امروز، پس از از سرگیری حملات ایران به کشتیرانی بین‌المللی در تنگه هرمز، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC) یک تسهیل‌کننده مالی ایرانی را که عملاً اختلاس‌های کلان را در رژیم ایران نهادینه کرده و ثروت‌های عمومی را به خارج از کشور منتقل کرده است، تحریم کرد.
این اداره همچنین امروز همچنین صرافی‌های کلیدی ایرانی را که سالانه میلیاردها دلار را از طرف بانک‌های تحریم‌شده ایرانی جابجا می‌کنند، هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18498" target="_blank">📅 00:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18497" target="_blank">📅 00:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شورای رهبری یمن:  «پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.  ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18496" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شورای رهبری یمن:
«پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.
ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران می‌خواهیم که از یمن به عنوان میدان نبرد برای منازعات منطقه‌ای استفاده نکند.
دولت و نیروهای مسلح، اقدامات سیاسی و نظامی را برای جلوگیری از هرگونه تلاش برای نقض حاکمیت یمن، انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18495" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صدای انفجارهایی در کرج!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18494" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر دفاع روانی اسراییل:  امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.  اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.  ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18493" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3vS853eC7DKLuTwVhDxYZhPRV_Dq3xLMOCQpu7zWBiyudejaYTln9mXFHuTHd9tfFxX0qTm6HVZOeBP_VcEEX8SLwijInr9TFTqQQF-PFrMRN6tGck9eUyaC3d4lxTwQyJf0vPfI5GNBaAlxSgmFTR9n7N9cSZkY0e1Vy-AwrzwGg_UMJ6TuKfYNQbTS_wjdJk6vnqRjSP3dwaAls_BHD77bBGx8Ze9zX5xAwsLKJtOaacFNSQ6iWirtOHRlW7Dpv-OXpowi7zwSudpRvuDM-v7X2YVr9HDBGDE6oZrTAxDkacnLZJd8oiMlUs8Xz6cWJtnFan8ssg5nCduse0qXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع روانی اسراییل:
امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.
اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.
ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی را دوباره به دست آورد و برای بار سوم به ایران حمله کند.
احساس می‌کنم خلبانان جوان در آینده نزدیک مشکلی در کسب ساعات پرواز نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18492" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجار در پالایشگاه نفت پلدختر در استان لرستان</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18491" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک به درستی پیش بینی کرد که یک اصلاح نزولی در طلا و دیگر دارایی های ریسکی داریم که پایدار و شدید نیست.  اکنون هم سطح شاخص کاهش یافته و رشد بیشتر طلا را متصور هستیم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18490" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXEZoNB_s0VkoruIMlJSiBNmOQGPxdQ5oLGt50E8uEhbmJwT0UhTnXSRpHmKHxDR1MHLXqaCREeJ18-YiEywiWd26mEJ5CaqTy84gcl48zu7Ske7SnrQprPOt8rqPoF11-QHdM_a2PwHS9effXSr8TK8LDkJB1JGnPVb06Zjur2WHH7PHiA2WDYhiT_OujC5_i0mGgSB1n80F3p3N19nN8Te21-3pu6J-O6_Mdg4G0dNpfC5v6do2p8yCMow-trT3EAD_Vj6Sg4112iMEYNv7Z92Jk16POXOG18HCzwEVicgBRhKwd_VlMT9X448un64br-kemnAB35KFE0u13K2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18489" target="_blank">📅 18:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdUreS0PjUjcltnhC0sKqLG_UfLeobHfgk5hhfkmSUr5Wlshct6ykLLHe5goa55Y9CcbOuQyEp7H983gk4KCM_Brcu6HBnBuRRqGIz7H0dU0B8O0a2XBlC0ZgTaHGNc4J8fPg9CbujW8zdIQqCgNXk-iNNgnirt61p0Z5dS0VdLaJ7bvVmkZta9Sk6SavAIn3iBo-dVhDYVGZTA6qpd_dWVZqLIvNqpur7Imqd2sMfd3ZxEaL3_qDjNQnz_B67fIOvV7yb-5eECrMYOx377AmVclpXM8D7i8U3JmZUeVkGuJnsf-coHPimTBwEmAWn5yV9CC-ddQ63_ORyWmlOkqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18488" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLnpLTSKWz3du7pyaomjtUSR_MOXtTLyHGGyy_BQoTX46pzo1qyp-4et9GuUnD_T-ohMm-nxIjOp6ToMBEnHFQ8s4XUycO-hZoMkgkbnt9RAmOviwTFt8ha3kKZkDnBLPlQ--VL65P-hninUx2tt3p9jj4PorAp11z4y57i2aUd17u3pAkaltCqUwLwXk6R_zrhXSwWziK3vWK4WXYFYSw-zSSjPoqpDuflRGPP8lajr1bXFMc9Hr02Y9y9C4qLO9SpcrKaN9ulI8EEPc7y2fJ1jAJlPX1-S4vv196etmc-M7I2AjnnH9yRF-JBe7j6m2BSgNH8grmEEC-YWaxuxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18487" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بعد از اینکه ترامپ گفت آتش‌بس با ایران به پایان رسیده است، گزارش شده که دو ناو هواپیمابر آمریکایی به طور غیرعادی در نزدیکی ایران و در محدوده برد موشک های ایران دیده شده‌اند.
این موضوع می‌تواند نشانه‌ای از آماده‌سازی برای تجدید فشار یا اعمال محاصره در تنگه هرمز باشد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18486" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ :  در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18485" target="_blank">📅 18:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال‌استریت ژورنال:   بر اساس اطلاعاتی که اسراییل ارائه کرده، ایران طرح جدیدی برای ترور ترامپ طراحی کرده است.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18484" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5ga-DcFAGp8CgptQo0vE-BG44IDTu2RfVHrga3UufDjES0fcYQew8W2gTvFN6sD9ghTh17LqOt3xBpAOlWIlX1HbaU1BmfF2MrKQfvVJaRb8bbgBgfyELEQOGFBrEA0ZYkOML64FTogR-9hMudWQOvfjOuFiU4lsrpoKsjRnBu5NldOgzZDlx4hyS8xGvDinMpJvBhrIQKwu1Y8T7qJMl7ItgkAOf_6aIPqJhRfDfNKwjHX06dIN1DAXr4JlSda_ZXZtBhNc2UpPqYJP093-4_nLeXQCjuqzjjt4o21e4ITDUzc6zZs3l0BU1AoAMhHmq8CDB6N-BrF45eSgpPJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18482" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک هیئت قطری با هدف نجات مذاکرات بین ایالات متحده و ایران به تهران آمده است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18481" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فقط میخواست ما را ضایع کند که گفتیم فقط شبها برنامه بود در آن فیلم</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18480" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18479" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای انفجار در کنارک !</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18478" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خوب خاطرم هست در دوره دبیرستان یکی از بچه ها یک فیلم ویدیویی آورد که رویش نوشته بود «جدول تناوبی عناصر» و دقیقا داستانش مثل همین مذاکرات ما با آمریکا بود
روزها صحبت می‌کردند و شبها با هم حکم بازی می کردند. حکم تفخیذ.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18477" target="_blank">📅 18:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18476" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibl8j03U7bLLo2KBjaicv4MNj1R1GpDafmlI68ngYRAC_wkiLCVSGUjwXXnZAXKH4QmMlXvK3GpWC5ufUg2vstfBrPDJvVZtwpgLOhkDzEa9-ms61oVJRPEeJgKM9oki-yQU8MJtXspdbHmkZ6gMcZRFrDH6XfbLHjiurwBqbcvyufKIGwZMf9WIrWul5H27kLa6eIVYIhfo9RyxZ76LiuHDXKn7HJElueDdsHrONjEIzbBaPYFirRw10Htb-8v_Nz5A4LFngGj1Amd-9Mvy_8mbjNN764SekdBsJM5UfeoWDC9VIFY87LG4Q7taNIkuPS8-ufOVLBK6Bk1UsSjQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18475" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ادعای بابک زنجانی در خصوص خرابکاری در راه آهن آق قلا</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18474" target="_blank">📅 14:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgXP4PEUzxS1quhZrZVvSwaemfD2Mc6G2sfhEbcU1EigmKKtcoWD_RyF29kXXH7fVl9D8DHYJHRvD8JW2XKUkIomkFLaI84K1AYt4pi4QnMYtfi8orVd25J1LSTUahLwHp0DWhnZKYcFqAHnpZnoPdaJmGUUNyhpZCqZ4zMWF9RksnVYLb9AycaFcDLIKctC0GFzrpXbvLTWBIeHj5AT2VRbNer1fuznMEC6_-elcFVbczG0locdH7pZLDkxvvf4Mt2sf54SWqhzhovgkqAFOgKgTfnvF8Vv8X8Yv6urn3b2mLS6WW33zopLp-sqwsDxxs4oKo95HEzkm8UIKap-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای بابک زنجانی در خصوص خرابکاری در راه آهن آق قلا</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18473" target="_blank">📅 14:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 5  جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18472" target="_blank">📅 14:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18471" target="_blank">📅 13:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0sBKvyFZ1VSBp3CZGL9AjeykIZvU-PDtlM-GnbFEvnayzXnlk6zg3hkSMX58JOGl-_teiqy7-qLzNSei8DBqBVb7SOEgHLZmvSjFomXKK9F7A0o7hykT90VielwT5h-USCMNdmie2OiehHkHEuPdlYf7W8zQzl_aiKbI-SKO1FJWczopK92UxfvOXSTz3wyFdnL5pYhc4KszSujW9SuqO9f26t8maViDOIWus_7gKTqNv-UsjFBVtLxq628jiOmxXCr_bhSj3OqQFPvqDRar2t8bwuTnoN-v-WnApsiNs98lb_xriM4-H5vybpvVF4COF5HRbChU3ZWtWAE3UW4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18470" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الشرق الاوسط: حماس جلسات رهبری خود را از قطر به ترکیه منتقل می‌کند.
در ماه‌های اخیر، این گروه بخش قابل توجهی از فعالیت‌های سیاسی خود را به ترکیه منتقل کرده است، در حالی که قطر سال‌ها به عنوان مرکز اصلی فعالیت‌های سیاسی آن عمل می‌کرد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18469" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYG9T9BFVev1aPPsPeJ4L2Uah25PBxjEw5hPHbTs7slVQODB6_1Pzc1qyc2DdjCdmT-yRVLTIQD8N3z0Sx8MP-N0OjpI7SQ2Bz6FSmfa4KNWKXGutZkT5dDCyVmjzFYGpnQgRdaJSA7u3Q8bE4GfyCjMduHcSrwUC5CpL8pTIuVIRMghXaQjp2HvVhhWkj84r-I_pdxgFApD0TLfX1-rQ69t6W9sZscr8xKo8T7k9qzE_CdmxlYMpiB-rANZWVsmUACo_NhY-xJE-7IVUsjXTU2FWgENaGGnDB7vNAxNmzEi8t__78c-epYaEDahlEB8OoKq8TZIiXWUz1fo3Ymi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18468" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 5
جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18467" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک مقام آمریکایی به شبکه CNN گفت که ایالات متحده و ایران در حال انجام مذاکرات غیررسمی برای کاهش تنش‌ها هستند، این در حالی است که پس از یک سری حملات متقابل، این مذاکرات در جریان است.
ایالات متحده در حال حمله و سپس توقف است، به این امید که از تشدید بیشتر اوضاع جلوگیری کند و به دیپلماسی فرصت عمل دهد. در عین حال، واشنگتن برای انجام حملات بیشتر امشب، در صورت لزوم، آماده‌سازی‌ها را انجام می‌دهد.
بر اساس گزارش Axios، دونالد ترامپ "به شدت به دنبال راهی برای خروج از جنگی است که آمریکایی‌ها از آن حمایت نمی‌کنند."
پاکستان و قطر نیز در تلاش هستند تا هر دو طرف را به میز مذاکره بازگردانند. میانجی‌ها معتقدند که حملات اخیر ایران در تنگه هرمز، توسط جناح‌هایی در داخل رهبری ایران صورت گرفته است که با توافق‌نامه همکاری مخالفت دارند و در تلاش برای تضعیف آن هستند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18466" target="_blank">📅 11:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18465">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2Q_cY1s4JjXcP5zo_27SUrguSjAvNiNQq90nr0ypAu3BD8ya-ym2-HX3CQxfcAhv7ve1ESznkNa4cBfDeYgpndHNwQx0ng8N4FA5-8GAXh8D4PtRbl56Vds3ezctSgCYH5Yh85eQ0tDXsqbhYhkDDahnZNNngu6tQodeTWpnSap41dWFr11PuciSYWGpDLGqic0c6HQ8KPOxOTqSi6iUytFJ0NxFcqsFfbrgTKFN57sD2PsohhU4BTbWjU5asrD7JDuxWDVOPDsP7Pw9pJNANazIDPajVVC1TY9GOQ1y6M3qb1h2oOoh40EFbIdPaDyDYBPMQQ16dyXkTrTwpFxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18465" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ2NLWMiiA3YlqCAGJtcwhFvPAiqDeHTqtHSCNfMle4nu-OAN_XEIypQn1Zl_tGW9sqJgY50_6CHzfaPAIPzwkhQ0-hfF_Dj3HhHwRS8T9L2qupTSYsq3vhblpEsV3GeOK5kblLBcDo--L2e626w_02_STIrUgjbHS4GSSdHA_4Tmc92kRxUDk1STDxbbZ1UctcLPU621I1hXSzPep15TV8TlFIz4bWU1J80LTNGYXwJFXorBWC0UeL2t6oeVnUI4W0dhaUe62UEJUOBCwoHJv1TjhtVLyEVjrTbN--jafZOzzGFHtRqw7B-lAIp9mvRb-brfLGcba0MHbn94Rg07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگ-۲۹ همراه؛ جنگنده‌ای واقعی اما با محدودیت‌های مهم
انتشار تصاویر اسکورت هواپیمای حامل پیکر رهبر پیشین ایران توسط یک فروند میگ-۲۹، موجی از بحث‌ها را در فضای مجازی به راه انداخته است. برخی کاربران مدعی شده‌اند که این هواپیما در واقع یک
میگ-۲۹UB
، یعنی نسخه آموزشی دو سرنشینه، بوده و به همین دلیل از رادار بی‌بهره است. بررسی مشخصات فنی نشان می‌دهد که این ادعا تا حد زیادی صحیح است، اما نتیجه‌گیری برخی مبنی بر اینکه این هواپیما «جنگنده واقعی نیست» نادرست و اغراق‌آمیز است.
نسخه MiG-29UB برای آموزش خلبانان طراحی شده و به دلیل نصب کابین دوم، رادار اصلی N019 از دماغه آن حذف شده است. در نتیجه، این هواپیما توانایی کشف و درگیری فراتر از میدان دید (BVR) را مانند نسخه‌های تک‌سرنشینه ندارد و نمی‌تواند از موشک‌های هدایت راداری به همان شکل بهره ببرد. این موضوع، توان رزمی آن را در نبردهای هوایی مدرن کاهش می‌دهد.
با این حال، حذف رادار به معنای از دست رفتن کامل قابلیت رزمی نیست. میگ-۲۹UB همچنان از دو موتور قدرتمند RD-33، عملکرد پروازی مشابه نسخه استاندارد، توپ داخلی و امکان حمل برخی تسلیحات، به‌ویژه موشک‌های کوتاه‌برد حرارتی مانند R-73، برخوردار است. بنابراین این هواپیما همچنان قادر به انجام مأموریت‌های رهگیری دیداری، گشت هوایی، آموزش رزمی و اسکورت تشریفاتی است.
در مأموریتی مانند همراهی هواپیمای حامل پیکر یک مقام بلندپایه، هدف اصلی معمولاً نمایش اقتدار، احترام نظامی و ایجاد جلوه‌ای نمادین است، نه مقابله با یک تهدید هوایی پیچیده. از این رو، استفاده از یک فروند MiG-29UB برای چنین مأموریتی امری غیرعادی محسوب نمی‌شود.
در مجموع، اگرچه میگ-۲۹UB فاقد رادار است و از نظر توان رزمی با نسخه‌های عملیاتی میگ-۲۹ برابری نمی‌کند، اما همچنان یک هواپیمای جنگنده با قابلیت‌های قابل توجه است و نمی‌توان آن را صرفاً یک «هواپیمای آموزشی» فاقد ارزش رزمی دانست.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18464" target="_blank">📅 11:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سوزاندن ترامپ لگویی خندان دیشب در مشهد!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18463" target="_blank">📅 11:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usBzaAdaWHpyJOBP3TSPXiTSY6F1vBaOi1ei0k3GbE4kBmGwE_3b2-6syT5X5czkhxh-A5tXwrbWyUe88r2biKjDp5o0WGVggPPaS4XhBuXbwY7_0iaEuhq7jsd3bOVOYr8yk5eQuqY_gqJ03son6m4zXIWUBDWDU-fP0b3BNYv7_Z7cevTdLusi27u9cYNoXcyjF7X1c367fi0AF-U6v7m7ymfkRusNrqUeKZk6Pq5nVujs_zS1LZLzVW1DS2BwR5Hpuj6WMLs6zdE9cO-kuntSnkpaHk1ckaE1UbYRh2A9E2FHJFic_sPZY-K4L5c5NgKYUjWiQNRtf0UWJLEhfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hqqy7QPS1C_ZxrEZo1JD50qZcDvJBHnvOwtOaPGjEp2f-NJLaro-cW9jkjglteUKYD3Hf31Iq6JoYDDh3jRXYm0Llv0c1h8NItaVSAi97SrcPSOY6reR7sgpoUxiixoT-s_4uGQmZo1vMSyIh27CRzH194nOXIc0bM4Kd-JW2q4AhtJq0Z4FQE_EwwwM9T7CVkuZpZD17xxtQQ1PKY5w8D_NG9cRv6U1PIc5QHbkJnk2UiQuOUlVVgQBYBXyZCWLTmKU4JiTC2BcZfBUNtwi6xagHdqez79Cfb1mlZeLSPilFS94Z2FvlMcIk0UHBYbSEq62Yeu6aRlnm2PBvtEyIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه فکر می کنم به نظرم چهره آقای نجاتی در عکس سه نفره هم هست!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18461" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18460" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:  یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.  ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18459" target="_blank">📅 10:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال‌استریت ژورنال:
بر اساس اطلاعاتی که اسراییل ارائه کرده، ایران طرح جدیدی برای ترور ترامپ طراحی کرده است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18458" target="_blank">📅 01:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_fRSbGeTzeKEhbYDy7bxx0-nzxwNw_M6_QWVaA7_Yj4464wV1FMI4PTSx2IEM5Rem5-6Bh_vMG_w9xKP2TDnflVzJg4xai073x8ZlmF6exfQvjNmWo-2cKIdfZIWAMM7XxgcHS4BihSXF2w9tP72KOW2lwxg8P14wqY1nFzYdrQ5S5gsqJGMu1dHXCW9CwM0aVRW0fM8VEViXLMtJgNgF_WtcGbbMM8eBd130ooUUR1TQArQvwkfp6YTfHrIp9cAQTWdHwaDBgPn42qGvXEyVX-5OgiD-lypLNtBY_0IYivLtTtejqVJ4w1Me5j9j7wHdCUx8537AuY7cRbElywLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/18457" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انتشار اخباری تایید نشده از تیراندازی در اطراف حرم امام رضا</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/18456" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انتشار اخباری تایید نشده از تیراندازی در اطراف حرم امام رضا</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18455" target="_blank">📅 00:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تیم فرانسه به روزی افتاده که بلوندشان شده امباپه!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18454" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرماندار کنارک:
منطقه نظامی نیروی دریایی در دو مرحله هدف حمله دشمن قرار گرفت
ایرنا</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/18453" target="_blank">📅 23:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">برخی گزارش‌های اولیه حاکی از یک ترور هدفمند در اهواز علیه علیرضا خدادادی، مشاور قرارداد استانی ولی‌عصر سپاه پاسداران در اهواز، استان خوزستان، ایران است</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/18452" target="_blank">📅 22:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر کار آمریکا نباشد ۲ گزینه باقی می ماند:  — اسراییل — امارات</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18451" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آمریکایی ها هر گونه حمله جدید را منکر شده اند</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/18450" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش‌هایی مبنی بر حملات هوایی آمریکا در شهرهای اهواز، چابهار و بوشهر منتشر شده است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18449" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش‌هایی مبنی بر حملات هوایی آمریکا در شهرهای اهواز، چابهار و بوشهر منتشر شده است.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18448" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار در بوشهر!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18447" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار در چابهار !</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/18446" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فوری | رئیس ستاد مشترک نیروهای مسلح اسرائیل: ما به هر کسی که بخواهد به ما آسیب برساند، با قدرت پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18445" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/18444" target="_blank">📅 19:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sInCRoxd__Ag3xmvog-B4NZLH2-QYskNeS6Zkmkj27rLAdbpoW4U6ptrrvgEARU8QcUf8ZjfpjzuPYOCkanem87qO_UI_l8d8YZVfjYepkfo9gANRCoYqZhCvBu4z6eoxYZTYu8QM5RPnf-SAVFBgznk2FtilfGu4Jg5Ad4NjH8oGspHE97slIDX4_LdQycbzWnUsZjGBhx9-MHeSZnOwZwppppzAmSJpv9r37cDaVFffjQPqkdv-Cw-VmgMJkEARLlc0WbFu3QNdtoUU6lQOlJDd4X2H6p1Y74gPj649Q0CBA1_ocIkVuPWWK9WpVk5g9rR-2Mm8gMAN_h0j-FnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/18443" target="_blank">📅 19:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18442" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.
🔹
در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا! در منطقه از آتش سنگین ما در امان نخواهد بود.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18441" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:
یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.
ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده آمریکا خدمت می‌کند؟ بله یا خیر؟ و البته، پاسخ این سوال بر عهده مردم آمریکا و دولت آمریکا است.
این موضوع قطعی است که برای دولت ایالات متحده، ناتو و به ویژه ثبات در دریای مدیترانه شرقی، از اهمیت بالایی برخوردار است.
بنابراین، آیا ارائه یک پلتفرم به یک کشور در دریای مدیترانه شرقی، بدون این شرط که این پلتفرم نباید علیه یک عضو متحد دیگر مورد استفاده قرار گیرد، به نفع ایالات متحده است یا خیر؟</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18440" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ارتش اردن اعلام کرد که ۸ موشک بالستیک ایرانی که به سمت خاک این کشور شلیک شده بودند را رهگیری کرد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18439" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار در شیراز و کرمان</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18438" target="_blank">📅 15:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">— دونالد ترامپ:  «به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18437" target="_blank">📅 14:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18436" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‍
💢
وزارت خارجه: حملات جنایتکارانه آمریکا نقض فاحش بندهای یک و پنج یادداشت تفاهم است
🔹
وزارت امور خارجه حملات تجاوزکارانه ارتش تروریستی آمریکا طی بامداد پنج‌شنبه ۱۸ خردادماه به چندین نقطه در استان‌های ساحلی جنوب و نیز دو پل در استان‌های شرقی در مسیر ریلی…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18435" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18434" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18433" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=GvH4j_juDdIivXzCy1t7RqoWDidAKuPnU6aTCPy2cs1gDlos1gWB6qFBI4J__Tz_nTVEc30uBuo9Yc0_1TDmtc9ROqqtdv6lg6OPB-dABCUeNerdYzZPndR5Rjzn0RZMXlhwugZH9J3NbVN6Rh3HMXQ2MX5iObKBmq1-8aUv3w978NUcplJUW65NztfmOAONo7PdImCEgEbTi5BfYZ2Pl8mjB3nUhTc5I0rb_7TK4MvNvCxKoTAMJArLwsuESZV2heJtRUXQGzei10Gvhb8DHlv8F2WLTFN_dyqL9C0yfX3qGwcULlMG5B_eFaWSx2sw4FuWttR8ZkNYBvj_1h_fzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=GvH4j_juDdIivXzCy1t7RqoWDidAKuPnU6aTCPy2cs1gDlos1gWB6qFBI4J__Tz_nTVEc30uBuo9Yc0_1TDmtc9ROqqtdv6lg6OPB-dABCUeNerdYzZPndR5Rjzn0RZMXlhwugZH9J3NbVN6Rh3HMXQ2MX5iObKBmq1-8aUv3w978NUcplJUW65NztfmOAONo7PdImCEgEbTi5BfYZ2Pl8mjB3nUhTc5I0rb_7TK4MvNvCxKoTAMJArLwsuESZV2heJtRUXQGzei10Gvhb8DHlv8F2WLTFN_dyqL9C0yfX3qGwcULlMG5B_eFaWSx2sw4FuWttR8ZkNYBvj_1h_fzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18432" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWA9MmmLN7dkVg0kjHnbqJaYEDGFnnFEs0CM9mJ2Xf4OaswFT6SxukY4bP4PmPvkWkpPBc6bQ-1zHEot0YhIHYu2pink_caciUf0kC_3y97lN9mi_IBhrR9s1fUkPMqCIoYoIc_3c47JJfjTr78kKD0p3_p4BqtbbvkYZL77xlThhPbZMCvc05pK-Er9oOdKvI-txVXN-yUJ9xZ0_4pvTV-0XZba6jmy_kVxHrPbLAMkuma137ixuyPiT6gp3RgANlOLvHrKYXPUVxyZL0RP-xB3Xk1Ezo1_0Gtz4bwlRahhrsrGAdiPSwSebbPoL7sbQkOm3dgvQkb7S-d6aczvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با اینکه ترامپ برای عزیمت به ترکیه آماده می‌شد، مارکو روبیو، وزیر امور خارجه، و پیتر هیگست، وزیر دفاع، در دفتر بیضی‌شکل کاخ سفید، او را در جریان گزارش‌هایی قرار دادند مبنی بر اینکه ایران موشک‌های کروز و پهپادها را به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده و به سه فروند از این کشتی‌ها خسارت وارد کرده است.
ترامپ پرسید که آیا تهران هنوز به دستیابی به یک توافق نهایی متعهد است یا خیر، و پس از مشورت با مشاوران ارشد امنیت ملی خود، به این نتیجه رسید که اینطور نیست.
این جلسه، نقطه‌ی عطفی بود که باعث شد او طرح آتش‌بس را کنار بگذارد و مجوز حملات نظامی جدید و اعمال فشار اقتصادی مجدد بر ایران را صادر کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18431" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجار در بوشهر</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18430" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVH4cD10ssHheR-DrrwhLIlXRbp69pip_1eGpnC_ZJlraNRMmTXyBHpl8wCLeLthxJk-5u7QAo5r8R3BNZmAY_pAf6JPRq58nbxPJoWR7zn7_uTpJ5W_GG7OQfH-IQKudDn7mgZZCKJ4kuNStjYoO6pA3bZ4BTsUosjJbECpYoUPkzZckqCbl_5c8qLVNHPI-LnrAq50xNSACWys18Y_h9Sms-FFU_6TtIRZxKOD5MapS3UkgUi0Ub7x16Bm0dRIxxMvpmLkXyt1OKc7RnsJivcXED20OqAVjzVqdDBsPaf_4E_MwiJzSQfpjHx4TxvU4HhbU1r67tRa_lhpWJA1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18429" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18428" target="_blank">📅 12:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18427" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=j7liD4KBVQicDYu0LtekfgZEYyimrHme_eOXsZv19rT_yhOOHKiYbipD0CHhJPYrurxNUJYamzpEgaln8yFi838AT71keR6OIpfoQ3lJ0bOWuhVBf9E54Ktnnaq0L0dTpiffTVF2GaWwQmvm2_NpsZetMWT6uID84MPkSBoyeIBpyFipLbrTDkwwad0yIpVHcqZYkI07LPmW5igK-yde5xw24sIK60FQ-gll1UUsHvTI__K0BkMdYkILSpu1P6CcZP6jBT5wFzC93cEUcGfAiLhbYCBQVZhQp0GNH3hz9cMDT4fRu3IGg55bbUKWGQx96rEM_imV_EkMiWQAJpMQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=j7liD4KBVQicDYu0LtekfgZEYyimrHme_eOXsZv19rT_yhOOHKiYbipD0CHhJPYrurxNUJYamzpEgaln8yFi838AT71keR6OIpfoQ3lJ0bOWuhVBf9E54Ktnnaq0L0dTpiffTVF2GaWwQmvm2_NpsZetMWT6uID84MPkSBoyeIBpyFipLbrTDkwwad0yIpVHcqZYkI07LPmW5igK-yde5xw24sIK60FQ-gll1UUsHvTI__K0BkMdYkILSpu1P6CcZP6jBT5wFzC93cEUcGfAiLhbYCBQVZhQp0GNH3hz9cMDT4fRu3IGg55bbUKWGQx96rEM_imV_EkMiWQAJpMQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18426" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=l0L1_mjCQFJHs3a6S1X8beIhE2WwIRX7PG5YzoLwKvwBeH10yoGIKrjEWEjoUHb8gdfLzknO9y_feTxS4t3tMFbxF6IELTazIYqnEspd31KUOnoXFI29Bf_aAFiU6v0547MVYC-L5Dki_2jex-guziUSQV-H8ch36bnTJ2vClGAXcFDuvSA2cs_AYZjE63uMbzaEApJLeobdSneaGCJDtHtLK2ycAkdvIbC8m7FnLAB5UGkQF96fma3_ev_KUWi8q5O6onBUDI5BX25jgZTCTJLd_hO7eQ6JBa6P6RzV2w0MfbeLivfIeYPY6VhW6OqqQ-zYpNrNbUSA_QwhuufNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=l0L1_mjCQFJHs3a6S1X8beIhE2WwIRX7PG5YzoLwKvwBeH10yoGIKrjEWEjoUHb8gdfLzknO9y_feTxS4t3tMFbxF6IELTazIYqnEspd31KUOnoXFI29Bf_aAFiU6v0547MVYC-L5Dki_2jex-guziUSQV-H8ch36bnTJ2vClGAXcFDuvSA2cs_AYZjE63uMbzaEApJLeobdSneaGCJDtHtLK2ycAkdvIbC8m7FnLAB5UGkQF96fma3_ev_KUWi8q5O6onBUDI5BX25jgZTCTJLd_hO7eQ6JBa6P6RzV2w0MfbeLivfIeYPY6VhW6OqqQ-zYpNrNbUSA_QwhuufNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
🎬
هم‌اکنون هواپیمای حامل پیکر آیت‌الله خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18425" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟
درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در گذشته می‌توانست باعث جهش شدید قیمت نفت شود؛ زیرا بازار به اختلال ناگهانی در عرضه واکنش نشان می‌داد. اما شرایط بازار انرژی امروز نسبت به گذشته تغییرات مهمی کرده است و درگیری احتمالی آینده لزوماً به معنای تکرار شوک‌های نفتی تاریخی نخواهد بود.
یکی از مهم‌ترین عوامل، ایجاد مسیرهای جایگزین برای انتقال نفت در خارج از تنگه هرمز است. کشورهای تولیدکننده منطقه، به‌ویژه عربستان سعودی، امارات و عراق، در ماههای اخیر سرمایه‌گذاری‌هایی برای توسعه خطوط لوله، پایانه‌های صادراتی جایگزین و افزایش ظرفیت انتقال خارج از این آبراه انجام داده‌اند. این زیرساخت‌ها به بازار اجازه می‌دهد بخشی از نفت منطقه حتی در صورت اختلال در هرمز همچنان به بازارهای جهانی برسد. بنابراین، حساسیت بازار نسبت به تهدید بسته شدن کامل تنگه هرمز نسبت به گذشته کاهش یافته است.
عامل دوم، افزایش ظرفیت عرضه و انعطاف‌پذیری بیشتر بازار نفت است. تولیدکنندگان عضو سازمان کشورهای صادرکننده نفت (OPEC) و متحدان آن در قالب ائتلاف اوپک پلاس، در مقاطع مختلف توانسته‌اند با تغییر سیاست تولید، بخشی از شوک‌های عرضه را مدیریت کنند که یک نمونه جاری آن را با 3 بار افزایش تولید اخیر اوپک که آخرینش هفته پیش تصویب شد مشاهده می کنید. همچنین رشد تولید نفت شل در آمریکا باعث شده بازار جهانی نسبت به دهه‌های گذشته تنها به خاورمیانه وابسته نباشد.
از سوی دیگر، سمت تقاضا نیز تغییر کرده است. رشد خودروهای برقی، افزایش بهره‌وری انرژی، سیاست‌های کاهش مصرف سوخت‌های فسیلی و تغییر الگوی رشد اقتصادی چین باعث شده رشد تقاضای نفت کندتر شود. در نتیجه، هرگونه اختلال کوتاه‌مدت در عرضه ممکن است بیشتر به یک شوک موقت قیمتی تبدیل شود تا آغاز یک روند انفجاری پایدار.
موضوع مهم دیگر، پدیده «نابودی تقاضا» است. اگر قیمت نفت به‌سرعت افزایش یابد، مصرف‌کنندگان و صنایع واکنش نشان می‌دهند: استفاده از انرژی‌های جایگزین افزایش می‌یابد، فعالیت‌های انرژی‌بر کاهش پیدا می‌کند و اقتصاد جهانی با فشار رکودی مواجه می‌شود. تجربه بحران‌های قبلی نشان داده است که قیمت‌های بسیار بالا خودشان عاملی برای کاهش مصرف هستند.
البته این به معنای بی‌اهمیت شدن ریسک افزایش بهای نفت نیست. یک درگیری گسترده که تولید نفت ایران و دیگر کشورهای نفتی یا زیرساخت‌های اصلی منطقه را هدف قرار دهد، همچنان می‌تواند باعث جهش کوتاه‌مدت قیمت شود. بازارها به اخبار جنگی با سرعت واکنش نشان می‌دهند و عامل روانی می‌تواند قیمت‌ها را برای مدتی بالا ببرد.
اما تفاوت امروز با گذشته این است که بازار نفت ابزارهای بیشتری برای جذب شوک دارد. مسیرهای جایگزین صادرات، ظرفیت‌های ذخیره‌سازی، تولیدکنندگان جدید و تغییر رفتار مصرف‌کنندگان باعث شده‌اند احتمال تکرار جهش‌های تاریخی نفت در اثر یک درگیری منطقه‌ای کاهش یابد. در سناریوی درگیری بعدی ایران و آمریکا، احتمالاً واکنش بازار بیشتر یک جهش سریع و محدود خواهد بود، نه یک بحران انرژی مشابه دهه‌های گذشته.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18424" target="_blank">📅 11:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارتش ایران:  «ما با استفاده از پهپادها، سامانه‌های پدافند هوایی پاتریوت در کویت، یک مرکز هشدار اولیه در قطر و تاسیسات ذخیره‌سازی سوخت ارتش آمریکا در بحرین را هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18423" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔺
روابط‌عمومی ارتش:  در پی تجاوز ارتش تروریستی آمریکایی مناطقی از کشور و یگان‌های ارتش و در پاسخ به آن جنایت،  ساعتی قبل و در ادامۀ حملات ارتش به پایگاه‌های آمریکا در منطقه، سامانۀ پاتریوت در کویت، آنتن ماهواره‌ای…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18422" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به گزارش اکسیوس، پهپادهای ایرانی دو کشتی تجاری را در تنگه هرمز هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18421" target="_blank">📅 11:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبه نظامیان آزادی بلوچ یک حمله با بمب دست‌ساز (IED) و سپس یک کمین سنگین را علیه کاروانی متشکل از سه خودروی نیروهای امنیتی پاکستان در منطقه سچی واشوک، بلوچستان، انجام دادند.  خسارات سنگین جانی گزارش شده است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18420" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18419" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5Xjc9Nf1D8mkDnQ0MvxPxKHKDSBhwGbVHicP7V3WDUSqksQgER3yCOIXoQ7A9odE1-bsS0MVT1sFFw4s32DAexPwyWDD2YClvYg2_W0htx0pzRuBtENm_2XLBF3fY3Mz3altXSLRVjpPScefXhxWsIjD4k8R7fg8HLnlWsPb5jcy2AqLRA1ZK2Dn3NxB1Su3AhtFToscz96s3D2leTCMcO47_j0tgWHVaruiK-5kDCvSq2vwPmJZJ3aLh0HvJTCrYz_C_u01zB1PkHnVa5c_RHp2GpUcBUSkfEk6BNfTl3LuCYBgRbvkB-MjJzdDuNCPFyzTe61-8Q99GEcGpF7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18418" target="_blank">📅 10:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18417" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 4
پنج شنبه 9 جولای 2026</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18417" target="_blank">📅 10:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی   بسم الله قاصم الجبارین  قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18416" target="_blank">📅 09:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کاخ سفید برای یک درگیری بالقوه طولانی‌مدت با ایران بر سر تنگه هرمز آماده می‌شود.
مسئولان آمریکایی می‌گویند مدت زمان این درگیری به اقدامات بعدی تهران بستگی دارد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18415" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0gZglVeY7naWoHmj1Qb-rorIomObcCoSxIR4lpaEkRNt87B4o_W53WwlEZxfCD3wLBHA7_qUvs-aKLq1i_xTP1pkTHe5pc1dxvqRyLVUA6feSCoz-EAwQkKXGkMtnwwQRb3obTGhZ2zxRkCVNIhcljRyaJ5R3RSbsLJ4Q420H0-Sq4ogNtEolK2zDqeR1iJmJN0oo2jdMycecYfmQbGVTusNnU0j8I0klujSloLX0lqJwK5AOYIJlGgnd21OfVkiPWPyZBz5DuDKEuC0zmf-fuH8fzI6ghDdknAs5eJrPI4c_3S65JV1-YrV3m1K3t0QHG-azPKdNuf4FbBRlq0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18414" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:   به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.  برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18413" target="_blank">📅 08:39 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
