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
<img src="https://cdn4.telesco.pe/file/XklY9S_68pndfpigZweJKbA_gdYDB2dgPdEE7k9crefM54ZGEfakoInzYQsjqWeLXzZibk0GT3e8DW0cqFth41eSjMG2Lz07aPVkZk0ay77wMJZCjZEY3wnxwmmhQP4nQficsIHAxbh8zOi2XBDgpreFxMe3fXOk-soXPmFsb1iUkfLUWdtizwPXMEb5J3p2R3-h21bKTivsRDpHWFm4hz60E23sqBg4KDm-CVESq1T24IyTDFsq9Tos1bXUWRT4NRUUZfjcjz4tYmUJEkNDi1eG-oPviZZlTkqhvx862caInlHRLNrGeUMc3AUKrsjXYv4s-eVDVdEV8y4Q9qB3lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو با محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 8.04K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تو ویس پایین توضیح میدم این اشتباه فاحش هوش مصنوعی رو!  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 345 · <a href="https://t.me/mohsentavoosiseo/966" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKex45Za4CZlaizIOEHUu5_MA0h__c2aGUHwVXUMf4MBJLeHwoGkf4I4c7llXzm0rO_qkvwg4tgUkWhO2mzgOyclwb_KpJSyPtWT2Wh4x7BY1wWmyOs8KOg4OU2Au7_nJTOYYqf_PdabTkgEctJut-bHPGJL79gKVB6h71TCUCkjzjAaWNTi0jWwjMkx_j39U47OU0IbqdwjQ3AHABUbydlrLTlKuk29p1GRrr-9y7ixv9uCZ5r4kSM23G2VUTT69ZKzsD2FG8cXHedOChOA0UEGqxwtwTqs56Gaj7TowuRQFeVPc_sZgTlwlZN5zb_t3GlOfmcLjCZ8shxlXmoumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ویس پایین توضیح میدم این اشتباه فاحش هوش مصنوعی رو!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 371 · <a href="https://t.me/mohsentavoosiseo/965" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⛔️
این خوب نیست!
تو این دو تا پست خیلی ها اومدن گفتن چرا به هوش مصنوعی توهین می کنی و اصلا اینکه هوش مصنوعی برات خط و نشون بکشه و چتت رو ببنده براشون مهم نبود! و فاز اخلاقی برداشتند!
سریال جاناتان نولان داره به واقعیت میپیونده. این خطرناکه‌. یکی حتی نوشته بود با کارگرت نباید بد حرف بزنی خب و همزادپنداری انسانی کرده بود!
خطرناکه عزیزم. لحن ما در چت خصوصی با هوش مصنوعی خطرناک نیست. سلطه ماشین بر انسان خطرناکه که از همین حالا عاشقان سینه چاک امام دیجیتالی(هوش مصنوعی) صف کشیدند برای بردگی و تعظیم برای یک چیز بی جان صفر و یکی(دیجیتالی) ساخته دست بشر.
خداروشکر از قشر آگاه تر و تکنیکال(دولوپرها) چنین چیزی ندیدم‌. دولوپر ها میدونن کت باید تن انسان باشه.
https://www.linkedin.com/posts/mohsentavoosi_%DA%A9%D9%84%D8%A7%D8%AFopus-5-high-effort-%D8%AA%D8%B0%DA%A9%D8%B1-%D8%AF%D8%A7%D8%AF-%D8%AA%D9%87%D8%AF%DB%8C%D8%AF-activity-7499816238756421632-mHI7
https://www.instagram.com/reel/DcqV0WHMZia/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/mohsentavoosiseo/964" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چالش تیم پشتیبانی رفع اشکال گاهی اوقات اینه که سوال کننده یه مدیری داره که مدیرش تو اینستاگرام یه پست دیده که یه چیزی نصب میکنی روزانه کلی بازدید روانه سایتت میشه دیگه هم به گوگل نیاز نداری.
از تمام دست اندرکاران و فعالان حوزه جدی تقاضا دارم، ابزاری که صرفا با نصبش، بدون کار محتوا، بدون کار آف پیج، بدون اینکه درگیر بهینه سازی بشی، اگر راهی میشناسید که با نصب یک افزونه و ابزارو پلاگین، روانه صدها و هزاران نفر از گوگل یا هوش مصنوعی ها بریزن تو سایت شما و سفارش بدن،
به من یاد بدید و مبلغ بسیار بزرگی هم پرداخت میکنم بابتش. تمام پروژه های اجرایی خارجی که دستم هست(و واقعا سخت و زمان بر هست) و فروش محصول آموزشی(دوره) هم میذارم کنار کلا و میرم که توسط ابزار شما، جریان مالی خیلی بزرگتری برای خودم ایجاد کنم و صد ها برابر مبلغی که به شما پرداخت میکنم هم خیلی سریع در میارم.
سپس میام یک پست میذارم و رایگان آموزشش میدم و میگم بچه ها! کلا دور خودمون میچرخیدیم! گوگل ادز و SEO/AEO و متاادز و گوگل بیزنس/مپ ادز(زیرمجموعه همون گوگل ادز) و تمام کانال های مارکتینگ بیخود و اشتباه بود. هممون اشتباه میکردیم. یه ابزار کافی بود ما رو سریع و ارزون و راحت به مشتری برسونه.
بعد هم میزنم تو کار املاک و پاسپورت چند تا کشور رو از طریق خرید ملک میگیرم و بقیه زندگیمو به گردشگری، دوچرخه سواری در تابستان های سوئیس میگذرونم و یک صرافی بزرگ هم در مرکز امارات با شعب مختلف در سراسر جهان، تاسیس می کنم و میام میگم همون پستی که اون روز گذاشتم و exit کردم یادتونه؟ همه اینا رو از اون پست اینستاگرام و اون پلاگین یا ابزار بدست اوردم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/mohsentavoosiseo/963" target="_blank">📅 12:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به من گفت: "خب حقوقتو گرفتی"!
تو ده سال جلو بیفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/mohsentavoosiseo/962" target="_blank">📅 15:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تله دلسوزی برای شرکت
تو ویس گفتم "خلق کن"
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/mohsentavoosiseo/961" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تله دلسوزی برای شرکت
اعتبار به صورت نقلی منتقل نمیشه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/mohsentavoosiseo/960" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/mohsentavoosiseo/959" target="_blank">📅 15:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینها رو تو اپدیت دوره پوشش دادم(اپدیت در حال ضبطه)
Agent بالاسر Agent
——-————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/mohsentavoosiseo/956" target="_blank">📅 11:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کلاد یا چت جی پی ای کدکس یا آنتی گرویتی گوگل؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/mohsentavoosiseo/955" target="_blank">📅 11:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توضیح ویس های بالا و بحث سیستم سازی در کلاد و یاد دادن به هوش مصنوعی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/mohsentavoosiseo/954" target="_blank">📅 11:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم بعد از اینکه فهمیدند کلاد هم اخیرا ویس رو گوش میده و میفهمه و متن روان میکنه.</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/mohsentavoosiseo/953" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم درباره ویسی که از سمت شرکت بروکر به عنوان ایراد محتوایی گفته درباره محتوای ما.
بخش ۲</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/mohsentavoosiseo/952" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen Tavoosi</strong></div>
<div class="tg-text">ویس من به تیم درباره ویسی که از سمت شرکت بروکر به عنوان ایراد محتوایی گفته درباره محتوای ما.
بخش ۱</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/mohsentavoosiseo/951" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جواب اون سوال.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/mohsentavoosiseo/950" target="_blank">📅 12:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این ویدیو درباره این ویس (سراب پروژه گرفتن) هم هست.  تله شهرت! تله geek بودن.  تله دانش بالا. تله محصول نداشتن در ازای برند عدم توجه به فرسایش ذهنی    https://youtu.be/njtLVwnzyIY  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/mohsentavoosiseo/946" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qumyW2f0j9TVoqkr36EYDMQTOBGevG5bhGWP11pZ05i7gZlZKko0mlf4LvsQeTqA-W3HUaOd6jP0JDWZ-UQvSVz4-2ENIiDvg19_Y9FAFIEsTcuGpn1aleD9gF9ty6bjtCBj-vzQJuR84ctl2D1Cghj6bocVKdIMuN7ezofSWGQwvwMNu4sTkoVnrdM0RavbLdePXwZbsddLVrWSAXDPASr0Uh668EKfvIovfewId41uItIJwI3n80sBzICiPMydbJnleobSBjXloOsV0rtDQzuckZIS3aOcYNqMBz65eIrbO7kNih--VjhnUUNTLvJSTN64m68XAG1bE2bSpZ8f1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdKtlxcCnZuW3NBaXA7Uil_SXFTYDPp-ZgEl41gfez7QoNIK9ryVbA5iNR_vuWbcx3DcZ4OljV543_bgmlo1pb2luIk-krid4wSJKbprgQPbWhscfvduNfxto1OvrTKl_kp-6z2NZ04Rz02cIc8QV34hJMG9Wkub3vhm9vX8ERNoyONVCD3JC8DYkIx63SoGE690Zp-eXHT94o9M0gcnRJQy8T3JsdXaaYBTCBvP4p9-_87yHIpZpoYF-2lnrifferu_mIovLlnIiYZXu3otN_LtWFAsxHP88AsbaPP_7Z9bbo2VrjP1nLgfiIM1SfM2xmMg5CWHg94HZ3Viht4NMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axR6yqC_MMkOtUBYiDbmhMZyl5oTzai0z-jJ5i3PecvzimeSGUrma0v3RYlVPnd1saTfbaS6GRYfjDCyfIMSoFVeRfErtRicDVmCKRDbrg585_9MyyMMZ7slWAtq67ALI1pVix9qbqEpouIZshGv84VEDLRJVM4TrPj-f6fgq5zY0ZI7IPqy8GIBGIftNQd482W7r4FAstXiDkzbqhdeeB1z9tKxC_XaSey81vq-7JMqK2U-2pwV0ZCIEleVXmC_xUbtFcxDzT3d50UJGCDBV3nIpqKhqGG-P92e8eHAvP7XE3Xn3fjBZGNz_fJThs7EwC2ze1tx3pcTCatp29s3mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول به نظر موفقیته. عکس دوم رشد کلیک ایمپرشن اسم برند هست در حالتی که رتبه فرقی نکرده. عکس سوم فیلتر رجکس غیر برند هاست که صفر هست آمارش!
روی سایت هم چند ماه هست حسابی داره کار میشه.
1️⃣
❓️
ممکنه تبلیغ شده یا کمپینی بوده که موقتا اسم برند، سرچش زیاد شده؟
2️⃣
❓️
ممکنه رو اسامی برندی رتبه نداشتیم که الان داریم؟ مثلا مشابه های اسم برند اصلی؟
3️⃣
❓️
ممکنه اسم برند رقیب شبیه ما بوده باشه و اون سرچش زیاد شده ولی رو ما کلیک شده؟
4️⃣
❓️
ممکنه چیزی غیر از موارد بالا باشه که هنوز ازش خبر نداریم؟
جواب من:
هر چهار احتمال رو باهم احتمال میدم. هر کدوم بخشی از تاثیر افزایش ده برابری کلیک هستند. در آینده واضح تر شد و تحلیل کردم میگم.
پی نوشت:
تحلیل و نتیجه گیری از نمودار پوزیشن روی بیش از یک exact query اشتباه فاحش و بزرگی هست. چرا؟
اینجا
و
اینجا
گفتم.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/mohsentavoosiseo/943" target="_blank">📅 00:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO4W4RMuL00_nmMJt-7o_8qquQmJ4gajk4GXB7iQCoRQ99m-u-cS7DMhu7jX9L6zoElWC9mKyYIhCuzd_i-rvvHvSkoZOCQNyR2S2nM7AS3mwbTzRySXJHWtohOJtgH3uLJrEP3p_ls0MWJea0_TwqOJc5xiR8H8pQCZMK1Zt95NoniRWbNmWfTanoWdJR4meu27w3siHQWrbGATkn3VhgMJyzSELtD7MObIZfKjIu7_ZVx9vRV8iH0W-WlrYPnNn9oH24wv2Y4JNCQVCERtsxvzndWqmoQRmS4XtE-qZt46jaOUQwiDWErk7XyMAMJy34x7-ZjnuY8SUrGDFsQnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/mohsentavoosiseo/939" target="_blank">📅 18:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Overlearning
Unlearning
❗️
مهارت یادگیری زدایی و جلوگیری از زیادی یادگرفتن تو این عصر خیلی مهمه.
❓️
چقدر عمیق شیم؟ از کجا به بعد زیادیه؟ چاهی که از یادگیری زیادی عمیق و بیش از حد داریم می کنیم، به آب و چشمه و گنج میرسه واقعا؟
❓️
چجوری بفهمیم داریم زیاده روی می کنیم تو یادگیری؟
❓️
تله آدم های باهوش و با استعداد و قوی چیه؟
❓️
وسعت دید همیشه باعث بهبود عملکرد میشه؟
❓️
پرداخت بهای عمیق شدن بیش از حد، میصرفه به نتیجش؟
❓️
چجوری بفهمیم تو overlearning افتادیم؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/mohsentavoosiseo/936" target="_blank">📅 23:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!   خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!   پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/mohsentavoosiseo/933" target="_blank">📅 14:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzLHL6z4NpRwni3wMtHBaFw3D116uWJgx8t_DdBNrbVPsLCzGXjaXFMSbo0RJNXNoanFrFH0EdmusywhK1fh10hHCwiaJvMOpUblqoEJfy5sJ9w0bcwLM2Mp9Y1nUHiytWqIRjgfwf5j4tLi-Q-Y4H3Ycx1TG2Ia32Wv62bSwBcaFrcg5Hym6QaMCkvs-u0CwfmO14MXAYibm0_kPNYlvvMcpT5PWepfbcKnuQCSgYYurgtY7137e5heyqEA1sCOa8GXxBV8m4pmHgs6r4iTnHJH4JkGi5GYSnk2nSWQfsIPlpfPxSUvEtcdMTKScDhhgcrETc6tq2_y5DgCGbAsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!
خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!
پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام میاد به ما دستور میده!
من برای اولین بار ترسیدم. این خوب نیست اصلا!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/mohsentavoosiseo/932" target="_blank">📅 14:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/mohsentavoosiseo/931" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ساختار سلسله مراتبی URL ها، یک احساس، بیش نیست. هیچ ربطی به درک گوگل از محتوا یا ساختار شما نداره.
+روش پیشنهادی بهتر
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/mohsentavoosiseo/930" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/mohsentavoosiseo/929" target="_blank">📅 13:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
سرابی به نام پروژه گرفتن
❗️
به نام پروژه خارجی داشتن
❗️
فکر نکن تمام ماجرا اینه بلد باشی و حرفه ای باشی.
❓️
من به گذشته برگردم و کسی من رو نشناسه چیکار می کنم؟ محسن طاوسی ای که بلد هست ولی بدون ارتباطات و بدون اینکه بشناسنش، چه مسیری رو میره؟
مسیر من رو نرید. از من استفاده کنید. از دانش من. از تجربه من. ولی مسیر من رو نرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/mohsentavoosiseo/928" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آموزش پایین اوردن نرخ تبدیل
😶
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/mohsentavoosiseo/926" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صحبت از اپدیت شد، نیاز هست به دوستان یاداوری کنم، محتوای متنی و ویدویی من رو درباره بحث جاوااسکریپت ببینید حتما.
برای وردپرسی ها کاربرد نداره. برای سایت اختصاصی ها و دولوپر هاست:
سئو سایت های وابسته به اجرای جاوااسکریپت در مروگر
ارتباط جاوااسکریپت با هزینه های گوگل
سئو صفحات فیلتر دسته بندی فروشگاه - Faceted Navigation
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/mohsentavoosiseo/925" target="_blank">📅 16:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Mohsen Tavoosi – چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/mohsentavoosiseo/924" target="_blank">📅 16:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
  <div class="tg-doc-extra">Mohsen Tavoosi</div>
</div>
<a href="https://t.me/mohsentavoosiseo/922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا آپدیت های گوگل اونقدر ها هم در لحظه مهم نیست؟
چرا نباید نگران اپدیت ها باشید؟
وقت تلف کن ترین کار ممکن، اینه که تند تند برید ببینید گوگل چه اپدیتی داد. رسمی بود یا غیر رسمی.
درست اینه که فرض کنید گوگل هرروز اپدیت میده. اونم چندین اپدیت. هم رسمی هم غیر رسمی. واقعا هم همینه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/922" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طنز:
موقع تهیه گزارش به کارفرما، وقتی پروژه ای 400 تا دونه کلیک داره در ماه، و 40 تا کلیکش کم میشه، میگیم، طبیعیه ده درصد کم و زیاد اصلا درست نیست در محاسبات و تحلیل بیاد در دنیای Organic Search.
اما وقتی 40 کلیک زیاد میشه نسبت به ماه قبل، 40 بار در گزارش، مینویسیم 40 تا کلیک اضافه شده
😎
✅
ولی واقعا، جدی، رشد و افت و درجا زدن رو باید همه رو نوشت. فاکتور هایی که هیجان الکی هست چه مثبت چه منفی هم باید نوشت.
✅
برند رو از نان برند هم باید جدا کرد حتما.
✅
میزان رشد ایمپرشن ها رو باید لحاظ کرد وقتی کیورد جدید رتبه گرفته ولی کلیک نگرفته.
کارهایی که فعلا باعث رشد نمیشه و حتی ممکنه باعث افت کلیک بشه ولی زیرساختی و لازم هست(مثل اصلاح تارگتینگ و هرس)، باید بهش اشاره بشه که توقع و انتظار طرف از نتیجه سریع، بیاد پایین.
❌
به هیچ وجه هم نباید نمودار کلی پوزیشن نشون داد از کل سایت. برای تک کیورد Exact اکیه. برای کل سایت، بسیار بسیار اشتباه و غیر حرفه ای هست.
اینجا
و
اینجا
رو بخونید.
متاسفانه بعضی ها که تجربشون بیشتر میشه فکر مکنن ایمپرشن کلیک ملاک نیست، میانگین رتبه ملاکه و شبیه پزشکان متخصصی عمل میکنن که زمان پزشک عمومی بودنشون، درمانشون بهتر جواب میداد. نمودار کلی رتبه برای کل یک دامنه، آمار بسیار بسیار تباهی هست.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/mohsentavoosiseo/921" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYj7wfY4oU_mcNRMc-jMzlzn-cH67qZ1YwOybzhBVJsxi6_W8YZGLA8UkBZlvb5jfNKIATk6OUGpHHpUoFmX50A6GOc-nRbpvi25Y5kzJgYig1AqJe1cjksfTxKZ73PyFrlk_WpJdn1bPkrZSKynGd4VXhH93EBNQ4B6Fc4a6IQBK12sIfPe9z5l8T7K3R2rkUU1lGImCtxi8uGi6xHu-sg54rOWxV_rAJRf3JFkIVdw6HDPZzhzPp0K1ekoT6d2_ZOWW4YbWRagLuEjBQbjPFcIwQKv-koqN189ezoPcP8uoyQ9tlKiv6dU7YQaVVJYxLiLoxifx58bl9vk7HJf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیچاره گوگل. عقبه هنوز.
تازه تو بعضی سایت های غیر فارسی بخش Generative AI داخل Performance اضافه کرده.
فعلا کلیک رو یا اصلا دیتاش رو ثبت نمیکنه یا تو گزارش نمیتونه بندازه. یا اصلا کلیک نمیگیره که برای من ننداخته. و طبیعیه که کلیک نگیره.
چرا بیچاره؟ چون خیلی عقبه. ما رفتیم تو آمار گیری از Generative Engine ها، این تازه بعد مدت ها آمار AI Overview خودش رو تازه داره میندازه. از گوگل انتظار بیشتری بود. ولی خب. خوبه باز.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/mohsentavoosiseo/920" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">لیست بایگانی مقالات (پست ها) من که سال 93 , 94 منتشر شدند! یعنی 12 سال گذشته. از سایت web archive.
✅
که همچنان معتبر هست! و بسیار همین الان با پوست و گوشت، لمس می کنید! باز هم باید بگیم سئو عوض شده؟ اصول سئو همون اصول هست!
اون زمان کسی نمینوشت و فقط بلغور ترجمه در سطح وب بود.
ولی می تونید خط فکری الان من رو 12 سال پیش ببینید! حتی پست دارم با عنوان "عصر بی حوصلگی آدم ها! که متاسفانه تو web archive نبود.
هوش مصنوعی گوگل به زبان ساده
اشتباه نکنید! این مقاله سال 93 من هست!
چرا محاسبات ما در سئو غلط از آب در می آید؟
قوانین نانوشته گوگل
خاصیت تضریبی فاکتور های سئو
تشخیص رقابت کلمات کلیدی
(پست تلگرام رو اپدیت کردم و این رو اضافه کردم. جا افتاده بود)
تناقض های گوگل
بروز رسانی Freshness گوگل – تغییر لحظه ای نتایج با فرشنس
پرستش گوگل
114 فاکتور رتبه بندی گوگل
لینک بیلدینگ نکنید وگرنه پنالتی می شوید!
اینجا در نقد تفکر اون زمان بود که تازه پنگوئن نسخه های چندمش رو داده بود و همه ترسیده بودند که کلا دیگه لینک سازی نباید کرد. و این تفکر که بک لینک بی اثر شده. اون زمان هم بود. اون موقع من میگفتم A و T از EAT رو چیکار می کنید پس؟ بهرحال فعالیت اف پیجی حتی نوفالو نیازه. میگفتن نه فقط محتوا کافیه. محتوای خالی فقط E هست. اون موقع هنوز E دوم یعنی Experience نیومده بود.
سه راه پنالتی شدن در گوگل
روش های خروج از پنالتی گوگل و ریکاوری
تراست رنک
محتوا پادشاه نیست
قوانین گوگل درباره بک لینک
جهت اطلاع کسانی که تازه وارد سئو شدند، هنوز هم در اواخر 2026 همین قوانین هست!
برندینگ، دست برتر سئو
اولین ویدیو یوتیوب من سال 94
- بررسی چند موضوع رقابتی در ایران
(ورودم به سئو از 91)
اگر دوره من رو دیدید یا حتی ویدیو های رایگان من رو، ادبیات و لحن این مقاله ها، براتون آشناست.
همین مطالب هم متاسفانه بدون منشن و یاد کردن و چیزی، توسط بعضی از دوستان، از زبان خودشون مطرح میشه.
حالا همون محسن طاوسی 15 سال پیش، یک اپدیت game changer داره که کاملا تهاجمیه! و عملا انقدر بزرگه که میتونم بگم یک دوره است!
دوره تهاجمی سئو بین المللی با Claude . بدون مرز جغرافیایی و زبانی. برای اکثر مدل های SERP فارسی و غیر فارسی. که در حال ضبط هست و برنامم اینه قبل از پایان 2026 منتشر بشه و هرکس دوره رو داشته باشه رایگان دریافت میکنه.
چرا تهاجمی؟ Aggressive در اینجا به معنی شدید و طوفانی هست. تا نبینید متوجه نمیشید چرا اسمش این هست. برای همین سورپرایز هست. ولی انتظار رو پایین نگه دارید که بعدا سرخوردگی ایجاد نشه. فرض کنید یک آپدیت معمولیه. خیلی معمولی. سرفصل های حدودیش هم در صفحه دوره هست هم در
این پست تلگرام
.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/mohsentavoosiseo/919" target="_blank">📅 12:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به زودی به جایی میرسیم که اخاذی از skill ها و md ها و اسناد کلاد میشه.
ما بحثی داریم به نام پرامپت های چرخشی یا لوپ یا تکرار شونده. بعد بالغ شدشون میشن Agent.
پیچیده نیست ها! مثلا یه کار رو سه بار میگی چک کنی بازبینی و اصلاح کنه. بعد مامور(agent) درست میکنی که اینکارو انجام بده. بعد اون ایجنت رو میذاری سر کارش، هربار خودکار انجام بده.
چند وقت یک بار هم میری سوله مامور هات، بهشون آب و علف میدی و پیچشون رو سفت میکنی و برمیگردی پی زندگیت.
چجوری اخاذی می کنند؟
مثلا میدزدند فایل های شخص، شرکت و سازمان شما رو و میگن انقدر بده تا این همه زحمتی که کشیدی این سیستم و مستندات و مهارت ها و بلوغ رو که ساختی، بهت برگردونیم.
دو بیت کوین بده بهت پس بدیم. شرکت های بزرگ هم می ارزه براشون که این باج رو بدن.
من بخش سئوییش رو آموزش میدم تو اپدیت جدید دوره که در حال ضبطه. بخش های دیگه خارج از سئوش با خودتون
😎
البته سئوش رو استاد شید بقیش هم استاد میشید.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/917" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مقاله من حدود دوازده سال پیش!
March 2015!
ویرایش هم نشده. همون خاصیت تضریبی فاکتور های سئو، چیزیه که تازه بعضی ها دارن کشفش میکنن. یا بهش فکر میکنن.
من خیلی خوب بلدم پیچیده حرف بزنم جوری که فکر کنید واااای من حالا حالا باید دانشمو زیاد کنم تا بفهمم محسن طاوسی چی میگه. اما فایدش برای شما چیه؟
برام مهمه مخاطب من، یه چیزی دستش بگیره و اجرا کنه و فقط نمایش سواد من نباشه.
114 فاکتور رتبه بندی در گوگل
https://www.linkedin.com/pulse/114-%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1-%D8%B1%D8%AA%D8%A8%D9%87-%D8%A8%D9%86%D8%AF%DB%8C-%D8%AF%D8%B1-%DA%AF%D9%88%DA%AF%D9%84-mohsen-tavoosi
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/mohsentavoosiseo/916" target="_blank">📅 16:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟢
دوره جامع SEO/AEO بین المللی با AI
🟢
از این به بعد، هر ماه، قیمت به صورت تدریجی افزایش داره و دیگه اطلاع رسانی مرتبط با قیمت انجام نمیشه.
https://mohsentavoosi.com/course/seo/
آپدیت جدید، صفر تا صد سئو هست و سرفصل هاش این موارد هست که هنوز در لینک صفحه دوره قرار داده نشده و محتوای این صفحه، بعد از انتشار کامل این بروز رسانی جنجالی، به روز خواهد شد:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors که جداگانه نیست و کاملا در فصل ها آمیخته شده است.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
🟢
Local SEO برای بیزنس پروفایل ها
🟢
تحلیل و بهبود وضعیت در AI Generative ها
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
به سرعت در حال ضبط هستم. و تیم تدوین، در حال تدوین هست. از نظر خودم این اپدیت، سورپرایز هست! اما دوست ندارم چیز بزرگی در ذهنتون بسازید که بعدا انتظار ایجاد بشه.
این امضا یا مشابهش، از این به بعد زیر پست بسیاری از محتواهای کانال، قرار خواهد گرفت و اطلاع رسانی قیمت و... حذف خواهد شد.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/mohsentavoosiseo/914" target="_blank">📅 12:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/mohsentavoosiseo/911" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/mohsentavoosiseo/910" target="_blank">📅 14:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/mohsentavoosiseo/909" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/mohsentavoosiseo/908" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خطاب به همه کسانی که خیلی حرفه ای و باهوش هستند.
خطاب به کسانی که از اینکه یک سری بی سواد یا کم سواد حرف اشتباه میزنن، ناراحتن.
خطاب به همه با سواد ها!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/mohsentavoosiseo/907" target="_blank">📅 13:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه اشتباه بزرگ کسانی که تازه مهاجرت کردند یا تازه درگیر پروژه های غیر فارسی شدند یا حتی مدت زیادی گذشته اصلا،
❗️
اینه که فکر میکنن جهان یا بین الملل یا "خارج"! یا کشورهای دیگه، همونی هست که ازش تجربه دارند و همه چیو با عینک خودشون میببنن.
❗️
❗️
حتی استناد میکنن که فلان همکار یا مدیر خارجی هم اصلا اعتقادش همینه.
❗️
❗️
❗️
در حالی که همون همکار خارجی هم اشتباه میکنه. اون هم فقط نگاه خودشو داره میگه و تجربیات خودشو.
✅️
در همه جای جهان(غیر از هند و پاکستان و اندونزی و روسیه و...)، لینک بیلدینگ و پست مهمان مشابه رپورتاژ، بوده و هست و خواهد بود.
✅️
مدل پیدا کردن و صحبت با رسانه ها در کمپین های روابط عمومی PR، یعنی کاملا کلاه سفید، بوده و هست و خواهد بود.
✅️
مدل اینکه کلا کمپین اف پیج یا PR و کلاه سفیدم ران نشه و فقط تبلیغ بنری یا گوگل ادز یا کلا کمپین های تبلیغاتی فقط ران بشه هم هست که سئوشون فقط تکنیکال و سئو داخلی و کیورد ریسرچ و ساخت صفحه میشه(اونم محدود).
✅️
✅️
همه اینا هست. فقط شرکت با شرکت، فرق داره. سایت با سایت فرق داره‌. هرچقدر بزرگ تر باشن شرکت ها، مدلاشون به مدل آخر نزدیک تر میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/906" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سوال:   دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش  اولین سایت که ترب هستش  ولی اگه ترب رو حساب نکنیم میشه سایت سوم طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته  ولی کلیک ۵ تا!! راه حل برای کلیک گرفتن چیه؟ عنوان  و متا هم از دو رقیب دیگه…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/mohsentavoosiseo/903" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-902">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سوال:
دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش
اولین سایت که ترب هستش
ولی اگه ترب رو حساب نکنیم میشه سایت سوم
طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته
ولی کلیک ۵ تا!!
راه حل برای کلیک گرفتن چیه؟
عنوان  و متا هم از دو رقیب دیگه خیلی بهتر هستش.
چون روی کلمه ی اصلی اومده بالا
پاسخ در ویس:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/mohsentavoosiseo/902" target="_blank">📅 19:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سوال:   من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟  پاسخ: https://t.me/mohsentavoosiseo/511 این ویس و ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/mohsentavoosiseo/901" target="_blank">📅 13:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-900">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سوال:
من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟
پاسخ:
https://t.me/mohsentavoosiseo/511
این ویس و ویس پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/mohsentavoosiseo/900" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/mohsentavoosiseo/898" target="_blank">📅 11:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/mohsentavoosiseo/897" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تولید محتوا با کلاد
استاندارد سازمان رو برای کلاد تعریف کردن
هوش مصنوعی، چت کردن و چهار تا فایل اتچ کردن و اسکرین شات فرستادن و چهار تا پرامپت خوب دادن نیست! اینا خیلی مقدماتیه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/mohsentavoosiseo/896" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/846
بن میشیم نمیتونیم کلاد بگیریم!
Ban
#بن
#ban
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/mohsentavoosiseo/895" target="_blank">📅 15:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/mohsentavoosiseo/894" target="_blank">📅 15:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تفاوت کلاد تو چیه دقیقا؟ نسبت به بقیه AI ها؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/mohsentavoosiseo/893" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=BqBNbMcBTcSPAbGPQ6ZQ6ZZMLFsbLqageD0iO4uch1CdtPgWz3Y3vkY7rzHZghxPFjGoSHCPrKfEPEGLLsCBancxqGapW7SB2Q1iLH6pw-ilrRL9qtC0qgIKb1P4B1j4Viha7eOLZVYw0FagbfDmSLrCKPyezpNhRvAj7Y57R3OzpwhtcSOZPflk25U4nI1tfgcJliUna_3vgdtspng4VoSsLpBfagHf19G5OM8rn3NOm1haAWDcDODFM6bpEIB0HudP70LAoNAedffwmNMCIKezbFOfvuS4DzcfeVLqJwHYQAmMDl-288-_vEHGHDDId3sSSBM1mSZes6DoiX9GqIFzhtuzHtsnklmQMjzJmTksMjfYWgqKZE6Kpzui6EsK0EcR1QVJWSNcdnXWMe5I3qjfN3nbCfnc0qtSLj5tiOy1mvQ9LOBiRcNV_VG4bVg7SAVpopJoOL0dsvEM41zT7-NRoGaIL-c0I1etKzBydoQZtqObJWMkS677pz9k6a4GfZyndgrLB_raxjg85sKfLS6B-faizZpLXc34TZmN5jIJ-qCf-vIWk7GrAHMuu44djOtnqG_lI8id0FJC1jJEIO9Vu6YUkisRxXmUoBSArDxEuF12LL8yu6I6S5htDO3eCtpuZWJ4fAaU7QW9q8VEV4-iQld4UYNOjZofvANlvc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=BqBNbMcBTcSPAbGPQ6ZQ6ZZMLFsbLqageD0iO4uch1CdtPgWz3Y3vkY7rzHZghxPFjGoSHCPrKfEPEGLLsCBancxqGapW7SB2Q1iLH6pw-ilrRL9qtC0qgIKb1P4B1j4Viha7eOLZVYw0FagbfDmSLrCKPyezpNhRvAj7Y57R3OzpwhtcSOZPflk25U4nI1tfgcJliUna_3vgdtspng4VoSsLpBfagHf19G5OM8rn3NOm1haAWDcDODFM6bpEIB0HudP70LAoNAedffwmNMCIKezbFOfvuS4DzcfeVLqJwHYQAmMDl-288-_vEHGHDDId3sSSBM1mSZes6DoiX9GqIFzhtuzHtsnklmQMjzJmTksMjfYWgqKZE6Kpzui6EsK0EcR1QVJWSNcdnXWMe5I3qjfN3nbCfnc0qtSLj5tiOy1mvQ9LOBiRcNV_VG4bVg7SAVpopJoOL0dsvEM41zT7-NRoGaIL-c0I1etKzBydoQZtqObJWMkS677pz9k6a4GfZyndgrLB_raxjg85sKfLS6B-faizZpLXc34TZmN5jIJ-qCf-vIWk7GrAHMuu44djOtnqG_lI8id0FJC1jJEIO9Vu6YUkisRxXmUoBSArDxEuF12LL8yu6I6S5htDO3eCtpuZWJ4fAaU7QW9q8VEV4-iQld4UYNOjZofvANlvc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/mohsentavoosiseo/892" target="_blank">📅 14:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سوال یکی از بچه های گروه دوره:
میشه بهم نظرتون رو بگید که چقدر تفاوت هست بین جمنای با اشتراک گوگل پرو و کلاد ؟
چرا کلاد انقدر محبوب شده و اقلای طاووسی هم دارن تاکید میکنن روش؟
تفاوت سطحش با جمنای در چی هست ؟
خصوصا برای تولید محتوا تجربه دارید جفتش رو مقایسه کنیم؟
البته چون اپدیت جدید در حال ضبطه این سوال پیش اومده براشون
😎
. پاسخ:
https://www.instagram.com/reel/DcBLYe_MLHx/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/891" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاسخ سوالات پر تکراری که درباره دو پست بالا پرسیده شد:
❓
آیا ما که قبلا دوره رو خریدیم دریافت می کنیم این اپدیت رو؟
بله! فکر کردید من شرکت های خودروسازی داخلی هستم؟ حالا که بازی قشنگ شده جدا شیم؟ شما همراهان قدیمی رو تنها بذارم؟ هوای شما رو که بیشتر باید داشته باشم! پشتیبانی هم دو نفره شده از دو نفر قوی. قدیمی های سال اول خبر ندارند پشتیبانی تلگرامی دارند. جایی دیدید بیفته دنبالتون بگه این ویژگی اضافه شده بیا دریافتش کن. قبلا پولش رو دادی. من میگم! الانم گفتم
😎
❓
این اپدیت چه زمانی منتشر میشه؟
شما تا پایان 2026 روش حساب کنید. خودم نمیدونم. در حال ضبطم. دوسه ماه طول میکشه حداقل. همین ماه البته فصل اولش میاد که البته سبک هست فصل اولش.
❓
من تهیه کردم ولی اون دوره بین المللی، توش خالی هست هیچی نیست!
بالاتر گفتم، اون رو تا اخر 2026 حساب کنید کامل بشه. کم کم میاد در حال ضبطم. اصلا هم نمیتونم عجله کنم. شما اون یکی رو ببینید. دوره سئو جامع. سوالات بعدی هم بخونید!
❓
به درد سایت فارسی هم میخوره؟
بله. ولی مثال های من به همه زبان هاست و کلا مبتنی بر زبان یاد نمی گیرید. مبتنی بر وردپرس هم یاد نمیگیرید. اما هر زبانی و هر CMS و برای وردپرس هم یاد می گیرید.
❓
برای چه سطحی هست؟
از صفر تا خیلی حرفه ای ها. همه. ولی کسی که تا حالا پشت کامپیوتر نبوده یا در حد لاگین کردن تو سایت ها بلد نیست یا تا حالا تو زندگیش فایل word باز نکرده یا بلد نیست وی پی ان استفاده کنه، نه ها!
❓
باید صبر کنیم اپدیت جدید بیاد؟
نه! ببینید دوره فعلی رو. دوره جامع فعلی که دسترسی دارید، کامل و به روز هست. اگر خیلی بی حوصله هستید از فصل "تحقیق کلمات کلیدی و صفحه بندی در عصر هوش مصنوعی" شروع کنید. همش مهم هست و موثر و به روز و کاربردی.
❓
میشه فقط آپدیت AI سئو بین المللی رو جداگونه بگیریم؟
کلا یکی هست! صفر تا صد هست. هوش مصنوعی جدا نیست. بین المللی هم جدا نیست. قیمت دوره هم بسیار پایین هست بخاطر جنگ. کلا امکان بخش خاصی رو جدا خریدن وجود نداره. یا همه یا هیچ هست.
❓
سرفصل های این اپدیت جدید که تصویر یک دوره جدید گذاشته بودید چی هست؟ تو صفحه دوره فعلی سر فصل های این اپدیت هست؟
اون عملا میشه محتوای فصل سئو بین المللی همین دوره جامع، که صفر تا صد سئو به هر زبانی و کاملا آمیخته با هوش مصنوعی(Claude) هست.
توی صفحه فعلی دوره، این سرفصل ها نیست. اما اگر بخرید، این ها هم دریافت خواهید کرد:
موضوعاتی که در آپدیت، پوشش داده میشه این هاست ولی دقیقا عنوان سرفصل ها این نیست. به دلایل متعددی، فقط کسی که دسترسی داره، عنوان ها و سرفصل ها رو دقیق میبینه بعد از انتشار:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
ساخت دسته جمعی صفحات سایت با AI
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
جهت خرید، به
@mohsentavoosisupport
پیام بدید. من نیستم پشت این اکانت. بچه ها هستند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/mohsentavoosiseo/890" target="_blank">📅 18:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
قیمت دوره، قرار بود سال 1405 بشه 18 تومن. بخاطر دو تا جنگ و دی ماه، با مبلغ پایین تر در دسترس شد و از 1 شهریور(هفته دیگه)، مشه حدود 6. و سپس هر ماه یا هر سه ماه، افزایش قیمت داره. و طبق معمول، تخفیف دوره ای و مناسبتی هم نداره و هر ماه یا هر 3 ماه، افزایش تدریجی داره.
کاهش قیمت بخاطر جنگ بود و هست. کسی که پارسال 12 تومن میداد، امسال 5 تومن رو سخت تر از اون 12 تومن پارسال میده. درامدش فرقی نکرده و هزینه هاش هم سه برابر شده!
✅
به نقل از خود شرکت کنندگان دوره میگم که در هایتلایت اینستاگرامم هم گذاشتم:
اگر اهل یادگیری سئو یا نمایش یا فروش بیشتر در AI ها هستید یا میخواید اپلای کنید یا پروژه بگیرید، یا کسب و کار خودتون در داخل یا خارج رو به هر زبانی، گسترس بدید، اگر دوره رو ندارید یا نگیرید، احتمال پشیمونی و حسرت که چرا زودتر نگرفتید بالاست. به نقل از خود بچه ها.
❕
اما در عین حال، تضمین نمی کنم. هیچ تعهد و در باغ سبزی هم نشون نمیدم. صرفا هر آنچه دارم رو در دوره آموزش میدم که هر کس با من جلو بیاد، قوی، حرفه ای، بازای و تجاری و بین المللی و با زیرساخت درست بالا بیاد و آبکی نباشه آموزشش و
احتمالا
به چرخه عوض کردن دوره های مختلفش پایان بده.
🟢
قبلش تحقیقات خودتون رو انجام بدید. اگر ذره ای شک داشتید، تهیه نکنید. پولی که با شک پرداخت می کنید برای من جذاب نیست.
و در نظر بگیرید، برای کسب و کار خودتون، خرج نقدی میخواد. فکر نکنید فقط یادگیری هست. پول هم باید خرج کنید. مگر اینکه بخواید استخدام بشید یا پروژه بگیرید.
خرید در:
@mohsentavoosisupport</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/889" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfEJ5zRDrHx4kHm1o_hIOgXLyPJxaXDWgIqAVurImQFlY5MX2mYNgSMh-mbi0Z69ETegatNGFN5ql_YljtWdHrEPeS62JCZ_RZtw00l2lPnA4OuSOijRBaB_REj08ncFSXJpKYx4BCsv_mWWKyXymFq5rRtK3iBkqr60Yi6xzuHMtdXWb7N-WKL5gCIWbmi6sdYbn37zdGfePHO-OhJ4lD8L8me-jx4qSddbFkAciE-VTrU1kB9PXoXx1G4ZnGqZzLCc7YWTQCedobn3Pg35gCjxcNpOT11j6zre8GS04DPdK10dgakBOR2sYhjx2PiPY8T5HfAgWGFXUgSoFwBLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).
دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست. کلاد اختصاصی در محیط خود کلاد. نه این Opus که هوش مصنوعی های ایرانی و خارجی، میفروشند.
البته بگم من مثال هندی پاکستانی نمیزنم. ولی از شرق آسیا یعنی ژاپن، تا قاره آمریکا رو پوشش میدم. آلمانی، ژاپنی، ترکی استانبولی، روسی، فرانسوی، اسپانیایی داریم. فارسی و انگلیسی هم که سرجاش.
این آپدیت احتمالا تا آخر مهر کامل میشه و برای قدیمی ها در فصل سئو بین المللی قرار میگیره. و برای جدید ها، در این یکی دوره
هم
قرار میگیره.
خرید در:
@mohsentavoosisupport
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/888" target="_blank">📅 14:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کلاد، برای هر متخصص SEO و هر متخصص دیگه ای ضروری هست و یک هزینه جاری هست. شما میگید من غذا نمیخورم؟ سوار وسیله نقلیه نمیشم؟ اجاره خونه یا پول قبض نمیدم؟
کلاد هم بهش اضافه کنید. بایدیه. اونم اختصاصی. نه اشتراکی. اصلا با محدودیتی که کلاد رو اکانت هاش داره اشتراکی معنا نداره. با این همه قابلیت، فقط چت نیست! باید اختصاصی بگیرید.
اپدیت دوره که تو همین شهریور یک فصلش میاد، کلا با Claude هست. کوبیدم از اول ساختم. نه فقط ایرانی و فارسی. نه فقط حتی انگلیسی! هرچند Base همون قبلی ها هست که الان هم تو دوره هست. فقط یک ابزار قدرتمند بهمون اضافه شده.
به زودی سورپرایز خواهید شد!
😎
پی نوشت:
(کلاد تلفظ انگلیسیش کلاد هست)، ریشه اسمش فرانسوی هست که میشه کلود. شرکت آنتروپیک هم آمریکایی هست.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/mohsentavoosiseo/886" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/885" target="_blank">📅 20:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی از
شاخص های سواد از نظر یونسکو
، توانایی یادگیری زدایی(unlearning) و یادگیری مجدد و توانایی استفاده کاربردی از دانش خود است.
خیلی از آموزش هایی که ما میبینیم فقط احساس یادگیری میده و چیز کاربردی یاد نمیده.
نه باعث افزایش درامد میشه. نه اپلای و کسب موقعیت شغلی بهتر، نه پروژه گرفتن و نه حتی نتایج و راحتی بیشتر و بهتر و کم خرج تر برای بهبود رتبه گوگل و شانس پیشنهاد شدن در AI!
خب الان فایدش چی شد؟ درک بیشتر تا یه حدی معنی داره. ارزش داره بری اتحاد، مشتق، انتگرال، اعداد مختلط، سری فوریه رو یاد بگیری که بعد بهتر بتونی مثلا معماری ساختمون انجام بدی؟ یا کد بزنی؟
اگه اعداد مختلط نون شد اومد سر سفره، یا ماشینتو عوض کردی یا خونتو یا دارایی هات رو یا زندگیت با کیفیت تر شد، قطعا مسیرت درسته.
حالا به جای این ریاضیات، هرچیزی بذار. از الگوریتم های گوگل تا مستندات و نحوه کارکرد مدل Fable کلاد تا... .
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/mohsentavoosiseo/884" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">با توجه به اینکه فصل اول اپدیت جدید، که یک دوره کامل جدید هست،
با عنوان "سئو بین المللی با AI با پوشش GEO/AEO" ضبطش شروع شد و زودتر از موعد(زودتر از آبان 1405)، منتشر میشه، قیمت دوره از 1 شهریور 1405،
⭕️
افزایش خواهد داشت و بین معادل 40 تا 80 دلار خواهد شد.
و طبق معمول هیچ کمپینی برگزار نمیشه و به جاش سال به سال، افزایش داره.
انقدر که آمیخته با AI (Claude) و مباحث بین المللی و چند زبانی و چند فرهنگی هست، برای من حتی تدوینش و ضبطش هم خیلی جذاب هست.
کسانی که به دوره فعلی(دوره جامع سئو) دسترسی کامل دارند، در فصل سئو بین المللی، این دوره جدید (اپدیت بزرگ) رو دریافت می کنند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/mohsentavoosiseo/883" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
این پست حاوی ایده درامد دلاری و افشاگری پشت پرده هست. دست به دست پخش کنید که در جریان قرار بگیرید پشت پرده چه خبره یا خودتون ازش استفاده کنید:
این نظر سنجی که روش ریپلای زدم رو یادتونه؟
نتیجش این شد که من ورود نمیکنم بهش. ولی شما ورود کنید! در ادامه میگم چرا من ورود نمیکنم.
اینجا بهتون میگم ممکنه برای بعضی ها به صرفه باشه خودتون کاسبیشو راه بندازید:
(توجه: لینک ها درست هستن. با آی پی ایران نرید. من لینک غلط نمیذارم! راهشو پیدا کنید و باز کنید لینک هارو)
https://www.trendyol.com/google/gemini-pro-18-ay-kisisel-mail-e-davet-p-1098587629
این جمینای رو میده240 لیر 18 ماهه. یعنی حدود 1 میلیون تومن. یعنی اگه ویزامستر کارت داشته باشی میخری. اصلا نداشته باشی هم میخری. میدی برات میخرن.
حالا اگه خواستی کاسبی راه بندازی این میشه یکی از منابعت که ازش بخری و بیای بفروشی.
یا برای کلاد بری 150 تا Seat بخری هر کدوم میشه 20 دلار. از ریجن نیجریه میتونی تا 16 دلار و یک کم کمتر بگیری. حالا ریجن نیجریه رو باید با اپل آیدی نیجریه ای بگیری. برای هر 150 تا اکانت که میفروشی(max seats) باید یه اپل ای دی جدا داشته باشی. برای اپل آی دی جدا هم باید از نامبرلند یا هرجا شماره مجازی نیجریه بگیری. ریسک های از دست دادن اکانت اپل و شمارت هم در نظر بگیر.
بعد باید بشینی مدیریت کنی اکانت هایی که میدی رو. و اکانت هایی که تمدید نمی کنن رو. چون از کارتت سر ماه کم میشه مگر اینکه لغو کنی.
من خودم حدود ده تا دونه، یک مدت کوتاه اکانت chatgpt فروختم و خیلی ها هم دوباره پیام دادن که باز هم میخوان. یادتونه؟ چرا متوقف کردم؟ از کجا خریدم خودم؟ از اینجا:
https://www.trendyol.com/openai/chatgpt-plus-aboneligi-kendi-mailinize-davet-ile-tanimlanir-p-947506812
اون موقع میداد 100 لیر و دعوت نامه ای بود! بعد ناگهان تمام سایت های ترکیه، ناموجود کردند! همه با هم! الان میده 600 لیر. یعنی 13 دلار حدودا. باز زیر قیمته.
از اینجا هم میخریدم:
https://www.epinline.com/chatgpt-plusgpt-5dall-e-vip-1-ay-p-26417-m-1
این الان یک ماهه میده 350 لیر. میشه حدود 7.8 دلار.
آیا برای من صرف داره از اینجا بخرم 8 دلار بفروشم 18 دلار اصلا؟ کمتر از 20 دلار خود chatgpt؟ بله ارزش داره!
یعنی رو هر اکانتی که میفروشی حتی دو دلار کمتر از سایت اصلیش، باز بین 5 تا 12 دلار سود میکنی. گاهی هم ممکنه سودت در حد 2 دلار باشه.
این جمینای یک ساله رو میده 150 لیر. یعنی 3 دلار!
https://www.epinline.com/gemini-google-pro-12-ay-mail-adresinize-davet--p-27078-m-1
هزینه جاری خرید اکانت ها، مدیریت، پشتیبانی، تبلیغات و اینکه اطمینان کنن ازت بخرن هم در نظر بگیر.
من بخش اعتماد کاربر و اطلاع رسانیش رو داشتم. با بخش مدیریت و توسعه پذیریش به نسبت دردسر مدیریتش تا رسیدن به سود ماهی 2.3 هزار دلار به صورت غیر فعال(بدون درگیری خودم) اکی نبودم. اگه یه روزی بفروشم، همینه روش کار. حداقل پایه اش اینه. فعلا اصلا ظرفیت ندارم برای پروژه جدید باز کردن تو زندگیم.
و خیلی ساده با گذر زمان همه این پست رو یادشون رفته. من یه پست میذارم میگم اکانت میفروشم. خوبی تلگرام و اینستاگرام همینه که با گذر زمان کسی برنمیگرده پست های قبلی رو بخونه
😅
😎
شاید هم همین الان یکی از بات های فروش این اکانت ها مال منه! از کجا معلوم؟ خدا میدونه
😶
حالا به شما گفتم! قطعا برای خیلی ها به صرفه هست برن تو کارش!
هم سایت بزن هم ربات تلگرام. خیلی راحت با کلاد بنویس ربات رو با وایب کدینگ(همین الان بات احراز هویت و ارتباط با پشتیبان های دوره من، همینطوری نوشته شده توسط خودم با کلاد).
بعد هم پول بده تبلیغ کن جا بنداز پشتیبانی خوب هم بده. این بخش از خود تامین، سخت تر هست. اول فروش. دوم فروش. سوم فروش. بعدا محصول. قطعا باید بها بپرداخت برای اینکه بشناسن محصول شما رو و اعتماد کنن. خیلی بیشتر از بهای خرید و تهیه و تامین خود محصول.
رفع مسئولیت: من فقط تجربه خرید خودم از این سایت ها و دانسته های خودم رو گفتم. هر قدمی برمیدارید خودتون مسئولید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/mohsentavoosiseo/882" target="_blank">📅 14:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDO3ccE56809llt-CfTJ9lQoOz_jprkxs7isrvpQGF4lLM2EFi3S5DO8UvL67-BSIGquyqL0dT9L4mwaORVqRv62vzpu6zN-WgLH4IHvOccZiErWIGuOMepFhWXyYr-mH9r5xHH8glERoWGWQC74hx2uEh10btoS41-dLL7nwjvHu9N0fI6_y4LYF6DM6WCGgEGh2wEjMNNUxmNkrC-8vUvC3FDMIRVRkP4Tx4Vf-9rVUi3S9W8PXVRhHziVk-phoWgSiUfpwBB9NR7A8YcQQtUKgejF33eQnCc4sZ7MAh4KN2c_lSS7sWMAXaKPAYEZK_9901w8V0_KTjAG7UzYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یکی از ساده ترین هنرکاری های کلاد هست! از منوی رفلکت، بهتون عملکرد خودتونو میگه و واقعا بازخورد های جذابی میده! در اپدیت پیش روی دوره، تمام کسانی که دوره رو دارند، سئو بین المللی با کلاد رو به خشن ترین حالت ممکن یاد می گیرند
😎
.
به من گفته:
ایراد هایی که از skill ها و عملکردشون میگیری، به خاطر دستورات خودت وسط کار هست و یادت میره که خودت خرابش کردی!
😅
یا گفته فلان جا حرف من رو بدون سند رد کردی و هنوز میگه تو اشتباه کردی!
بعد میگم کلاد خداست میگید نه! بازم میرید از فلان جی پی تی، ایرانیش رو میخرید؟ خیلی فرق داره! اختصاصی بگیرید. کانکتور و اسکیل و داکیومنت و کوورک و... تو اختصاصی هست فقط.
mohsentavoosi.com/1
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/mohsentavoosiseo/881" target="_blank">📅 15:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_NjIdUAygqrx8q1HqLy0oqoTSdkdnEvpIssYvgvjeWDVMCRYCtagDib3rVb4TjyZSHhCeSJONZ-2YMlgWrAaoh4r4kH0dTeksjqP5VDW2fkGugMZRhohZTir16FAIhKapWd6qP3b4uLyCkK-xy2MKyxcT47WgeplNBbzGIlt_zksRF-StnS4lNPscUBU_UFMIbS6mz4PfgdunkL80DsRIha8kstwUhOjYmFeuoCuasduHODJigIEcJMyTsa9yeYtyrsAFWcjIAJoJr7mO2CWWER9HBLs68Av6pQhtlVF5AlwldThVOs-WIBj_zB0kT9mYiGaDN8fy5RjMCLLgpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓️
از کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
با چی ایجنت بسازیم؟
کلاد
❓️
از ایجنت کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
از کدوم مدل ها LLM ها استفاده کنیم؟
همه مدل های کلاد. Haiko. Fable. Sonnet. Opus.
❓️
از کدوم AI های اشتراکی یا api داخلی غیر فیلتر استفاده کنیم؟
هیچ کدوم. فقط کلاد اختصاصی.
❓️
برای کد نویسی از چه AI استفاده کنیم؟
Claude Code
❓️
برای مدیریت تسک هامون و انجامشون چطور؟
Claude Cowork
❓️
برای تولید محتوا؟
کلاد
❓️
برای مردن؟
کلاد
❓️
برای...... انقدر سوال نپرس. پاسخ:
کلاد.
❓️
جایگزین کلاد چیه؟
سوال گستاخانه ای بود.
❓️
از سایت های ایرانی کلاد اوپوس گرفتم. خوبه؟
پناه بر کلاد
😭
❓️
چیکار کنم دیگه هی نگی کلاد؟
از کلاد بپرس.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/mohsentavoosiseo/879" target="_blank">📅 20:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/mohsentavoosiseo/877" target="_blank">📅 13:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG0u8ypoHw9XtYb80KDgGHenu2x_tmuOMPtVVClM3xPLdpUNl-9q-gQYDhvJadfwzWyK8RPzqKL2wAhNejJDmfWzfU7I0fvqoXBfUoz3TPQkoJLqxoSHf_Wmz14H_kts-6QFKTEjEak7nArlPRpZM_kT63zC0IjlqY1APvvfp-iRUbw7GKm6z8_VfJHJBrQcgpMsdt2UmAEFtuEip9D8mR_ucIvK_gWY4ShuLWW_Lb0Y8_ksdkYTFZ7dC--4oRHY5ws5VXlU4ZY4k2OBcFFkCc4_d8gvBTT-FksPOPy2ROd8FKHXYxZw0TQ1Fi11k923YN3YeamBQs8dX6p-y8cmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/mohsentavoosiseo/875" target="_blank">📅 13:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFyzOKwu9Ru3f83Eew5HImCBWbnnCWA-l9h5xEwva0I-UqYdtG4A5DCGQ14cLhMBkXR6tQQRLiXnhgkbaKAQqCAJKdr1pj8OVcPkBv1W_MAkxyhhcwFAwSlMSn6zdvGVfkg7pQtGsdzdmPxgQqwfjBOaMcTaG7VOH98k4145rWEN4u4soYTviDcyI69RZW-TcjmI1VcuBxWN1BTL_oSu-jZWCdvU7VQ6nNHSoaCvDaK6YXxH5XPCtrJgycSdlpn3Uv8lKN3vE9v2cBCDfCHXGvN9_elO17MzHHWTM13acOoQhIJ6KZAQOXChCRn13fobGpcwN6EI7qE9CZ1zmScjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf1gB52w1bMU5d4TnNPo8tz1GTIaxNAkRAJSMqF8IIr_FOo6XNnMgdQedXStoik1N5qQ5mJIp3szZYOWYXaOmLJuVJWSCZTuDbxvLZq9adkH9taN1jq_BMy_mYNXl0Snm_DUF1WpeRCp24ZMFpB9gy-54DlRb2BEe8_SE6wh0lmOxDa6Q2FrkYLh0B7itwCJa9ZHN_so8V3DuXq_LN-H7mh9KglZcfn7-oFici6Ys0RA3E7rCLDkCSsdPr_hSG2y7YrBw4OmSegHT5mk3_xmiGHastPW2mfCU8bqmcOk2-H7UR3iGr1FiX6onErx4D143BtwrjJwrx4ZtSK5L1kE5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصویر چهارستونه(گرونتر) برای ابزار keyword tool هست و تصویر سه ستونه(ارزون تر) برای ابزار Mangools که ایرانی ها به KWFinder میشناسنش.
شما خودتون رو بذارید جای سایتی که ابزار اشتراکی میفروشه.
منگولز، روزی 500 تا سرچ میده. هر منگولز رو به 20 نفر بده، میشه روزی 25 تا برای هر نفر. نفری 2 دلار میشه هزینه خودش. کلا 40 دلار برای 20 نفر میده. میتونه تو پکیج کلیش بگنجونه.
حالا اگه کیورد تول 390 دلاری رو بده، 200 تا در روز داره کلا. به 20 نفر بده هر نفر ماهی 10 تا سرچ داره(بجای 25 تا) و نفری 20 دلار میفته براش. یعنی با دلار نرخ امروز نفری 4 میلیون تومن فقط یه دونه اشتراکیش! فکر کن حالا بخود بیاره تو پکیج هایی که حداکثر یک یا یک و نیم میلیون تومنه!
به من بگو دقیقا چطوری باید این کارو انجام بده؟ در یک صورتی میتونه! اینکه یا جمع کنه بره یا خیریه باز کنه به همه از جیب خودش ابزار اشتراکی بده.
این رو برای مخاطبین خودم پرمیوم هستند نگفتم. چون شما همه چیز رو با دید تجاری پخته نگاه می کنید و نمیگید اااا چرا گرون شد چرا نیست. میفهمید پشت قضیه چطور هست.
برای کسانی گفتم که دید تجاری قوی ندارند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/mohsentavoosiseo/873" target="_blank">📅 12:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تیم پشتیبانی رفع اشکال دوره تغییر کرده، دیگه یک نفر نیست و روز های تعطیل آخر هفته هم پوشش داده شده. مگر تعطیلات خیلی بزرگ یا استثناها.
که سرعت پاسخگویی بالاتر بره.
نه تیکتی هست نه لزوما تایپی. نه وبینار هست که بخواد ساعت خاصی برگزار شه و آزادی زمانی شما گرفته بشه یا مجبور باشید تو روزها یا ساعت های خاصی آنلاین بشید. چت تلگرام هست. بهترین حالت ممکن.
البته قبلا هم چت تلگرام بود!
خیلی از شرکت کنندگان دوره، خبر ندارن و کلا از چیزی که دارند استفاده نمی کنند.
من که مشکلی ندارم استفاده نکنید
😎
. سر بچه ها خلوت تر میشه راحت تر هستند
😎
. ولی استفاده کنید کنتور نمیندازه! نمیگیم چرا زیاد سوال میپرسی! نمیگیم چرا هر چی توضیح میدی ما نمیفهمیم! برعکس کمک می کنیم سوال رو درست بتونید بپرسید. خیلی راحت هم اگر خارج از سئو باشه یا بلد نباشیم، میگیم نمیدونیم!
"نمیدونم" گفتن تو فرهنگ ما (تیم محسن طاوسی) تابو نیست. برعکس، کسی که همه چیز رو میدونه، احتمالا کلا چیزی نمیدونه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/mohsentavoosiseo/872" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سوال یکی از بچه های دوره در گروه دوره:
من سئوکار یه مجموعه هستم
قرار هست یه سایت دیگه هم بالا بیاریم و کارفرما میگن که کل محصولات همه چی رو یه صفحه باشه(  صفحه اصلی)  و تمامی فیلترها مثلا ارزان ترین گران ترین و تمامی محصولات بیاد صفحه اصلی.
و صفحه تک محصولات و درگاه و تمام
و ن لندینگ ن کتگوری هیچی هیچی
همه چی داخل صفحه اصلی
و من هرچی توضیح  میدم که این اصلا منطقی نیست از لحاظuxدرست نیست از لحاظ سئو چالشی دارید نمیشه کار کرد از همه لحاظ مشکل داره اما اصرار دارن که همین باشه.
حوزه سئویی هم حوزه خیلی سختی هست
چه پیشنهادی دارید؟؟
پاسخ:
اگه یکی اصرار کنه من ماشین با چرخ چهارگوش میخوام شما چون مکانیک یا خودروسازی باید بگی باشه؟ ولشکن کلا. نمیشه. اون کارفرما دید و اطلاعات حداقلی نداره. ولی شما که دارید.
نکته برای سوال کننده:
شما یو ایکس رو ولکن. چالش داره از نظر سئو درست نیست! کلا نمیشه. چالش یه چیز کوچکتر و معمولا قابل حله. نه یه زیرساخت مهم اصلی که بخواد وجود نداشته باشه.
و قطعا شما قاطع نگفتی نمیشه. داری چونه میزنی. اونم میخواد چونه بزنه. تخصصشو نداره که. از مدل سوال که نوشته شده "چالش داره سئوش" مشخص هست خود سوال کننده محکم نگفته نمیشه. خودشم شک داره. بدیهیه که کارفرما که دل خجسته ای داره بنده خدا و اطلاعات نداره چونه میزنه و اصرار میکنه که بشه. من ایرادی تو کارفرما با توجه به سوال(بخش چالش) نمیبینم. اون حق داره بخواد. شما حق نداری ببری رو اصرار و چالش و موضع غیر محکم. پاسخ انجام یک چیز چالش دار و با فشار نیست!
پاسخ یک "نه" و "کلا نمیشه" صد درصدی بزرگ و قاطع هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/mohsentavoosiseo/871" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">درباره کمپین تبلیغات محیطی ا.......پ
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/870" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/mohsentavoosiseo/869" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/737
صفر تا صد مشکلات ایندکس شدن صفحات سایت.
❗️
دست و پا نزن برای به زور ایندکس کردن.
✅️
7 چیزی که باید چک کنید. تمام پاسخ های من به این موضوع
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/mohsentavoosiseo/868" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستانی که ایران نیستند،
با توجه به اینکه اپدیت پیش روی دوره، بسیار تمرکزش سئو بین المللی و چند زبانه و مبتنی بر هوش مصنوعی هست،
و اسپات پلیر هم دوباره از وایت لیست خارج شده و از خارج دوباره در دسترس نیست و دیتا سنتر ها دوباره محدودیت هایی برای دسترسی از خارج به داخل اعمال کردند،
اگر نیاز به وی پی ان ایران دارید به دایرکت همین کانال(آیکون پیام یا کلید message) پیام بدید تا وی پی ان ایران براتون بفرستم. وی پی انی که خودم استفاده می کنم (میخرم).</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/mohsentavoosiseo/867" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرت تر از دو جمله زیر نمیشناسم تو زندگیم:
❌️
درخت پربارتر افتاده تر است.
❌️
هرجا خبری هست ادعایی نیست.
بولشیت کامل. Absolutely nonsense.
مغز اصلا نباید دنبال این باشه که کی متواضعه کی پرباره. هر قسمتی که برامون سودمنده بصورت متغیر و داینامیک و قسمت شده، بر میداریم و استفاده می کنیم.
❗️
نمونه انسان ها و شرکت های سوپرموفق و پر ادعا و متکبر و غیر متواضع:
✅️
استیو جابز. هم بنیانگذار اپل و مخترع صفحه نمایش لمسی و اسکرولی که همین الان گوشی ها دارند و کلی چیز دیگه.
اخلاق گند مرحوم به گوش همه رسیده.
✅️
تراویس کالانیک، هم بنیانگذار اوبر که بخاطر اخلاق گندش از شرکت خودش به عنوان مدیرعاملی اخراج شد. همچنان ثروتمند و صاحب شرکت Atoms هست که ربات تولید میکنه.
✅️
هنری فورد! شرکت بی نظیر خودرو Ford
✅️
ارسطو اوناسیس، غول کشتیرانی یونانی قرن گذشته.
✅️
لاری الیسون. هم بنیانگذار اوراکل.
✅️
پابلو اسکوبار. قاچاقچی و تولید کننده معروف کوکائین مدیین کلمبیا(مدلین که همه میگن غلطه. ل نیست. ی هست. Medellín) سی چهل سال پیش. راستی خلافکارای موفق چی؟ ادعا باید داشته باشن یا باید متواضع باشن؟
هزاران مثال می تونید در طول تاریخ پیدا کنید. کلا من با گره زدن اخلاق و کسب و کار یا موفقیت، مشکل دارم.
قطعا مرتبط و موثرند روی هم. قطعا اخلاق و انسانیت مهمه. کسب پول از راه سالم و بدون دروغ و فریب و دزدی و... مهمه. آسیب نزدن به کره زمین، طبیعت، آدم ها، همدیگه و حیوون ها مهمه و ضروریه. قطعا مهربونی با حیوانات نشانه ای از تمدن و انسانیت هست و بدرفتاری باهاشون نشانه عقب ماندگی و بربریت.
ولی خیلی گوگولی و کودکانست اون دو جمله بولشیت اول این پست درباره تواضع و ادعا.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/mohsentavoosiseo/866" target="_blank">📅 13:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/mohsentavoosiseo/864" target="_blank">📅 12:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فیچر و امکانات و قابلیت: ۱۰ درصد
فروش و به سود رسیدن: ۹۰ درصد
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/863" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حالا با توجه به دو پست بالا، الان سئو مرده با هوش مصنوعی؟
چرا سرچ کنسول جمع نمیکنه پس؟ چرا فیچر وریفای کردن پیج اینستا و...هم اضافه کرده؟ اون تیم به این بزرگی دنبال چی هست برای سئویی که مرده؟ ( اون تیم، عملا تیم پر هزینه توسعه سرچ کنسول هست برای وب مستر ها که زمین بازی و دون پاشی برای محصول اصلی یعنی گوگل ادز هست).
گوگل ادز چرا نمیمیره؟ چرا رشد هم داره فروش ادز؟ مگه جستجوی کلمه ای نمرده؟ چرا هنوز آدم ها و شرکت های زیادی در سراسر جهان، کمپین های بزرگ گوگل ادز با جستجوی کلمات کلیدی اجرا میکنند؟
الان این تحلیلی که داشتیم چه ربطی به هوش مصنوعی داشت؟
چرا این سئو بجای اینکه بمیره هی قدرتمند تر و مهم تر میشه؟
هوش مصنوعی فقط تسهیل گر و سرعت بخش و بالا برنده دقت ماست برای اجرا و پیاده سازی. برای تحقیق. برای تحلیل. قبلا چرتکه بود تو فروشگاه ها. الان کارتخوان متصل به صفحه نمایش دوطرفه و لمسی هست. حتی تو خیلی از فروشگاه ها که صندوق های فول اتوماتیک هست، باز یک مسئول و یک اپراتور تنظیم و تعمیر و راهنما داره.
شما اون اوپراتور هستید که خیلی بیشتر از یک اپراتور پشت صندوق، باید حرفه ای باشید و اصول رو بلد باشید بدون وابستگی به ابزار. بدون وابستگی به CMS و وردپرس بودن یا نبود و کد سایت و زبان پروژه!
حالا شما باید کلاد رو کانفیگ کنید که خروجی خوب بده. دیتا رو درست بخونه. یه مستر(استاد و حرفه ای) باید بالاسر هوش مصنوعی باشه تو سئو.
و اون Master شمایید. کسی که به هوش مصنوعی وقتی چیزی میگه، هوش مصنوعی میگه آهان اره و ادامش میده.
اون مغز متفکر که هوش مصنوعی از رود دستش باید ادامه بده، شمایید. پس باید کامل سئو رو بلد باشید. سنتی ولی عمیق بلد باشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/mohsentavoosiseo/861" target="_blank">📅 17:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این عکس، نمودار حدود 8 ماه گذشته یکی از پروژه های انگلیسی هست. هیچ فیلتری جز زمان هم ست نشده.  تاریخ 5 فوریه زمان شروع همکاری بوده.  به نظرتون بد شده اوضاعش یا خوب شده؟ اگه میخواید بگید نمودار پوزیشن بدتر شده پس بده که متاسفانه تحلیلتون غلطه و کل سئو رو درست…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/860" target="_blank">📅 17:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OstzjDtM3-afK2hafb9qhutf9sY2l7vCloT1LLk4iVE3eemKLVMzXP70h7TIpbHSSGXhQQrJShu4wK6ZrK1ORr3YZAmAcW0TWfTa4InAmSayTKBFuuhAUmMBGqkXOItc0Ma_BL9S2QETcoRmeRrfUUrWyfuR5kOE_UhYSMmq8ipVVVGC5loW2aFN_owhTnIpVlmC9mMV_1CpGUolbeL3ml_oyu-ktVKpTBTLbaMRGfIDNTqf6FT6hpmVWs0F-43S-Rwf8of0fnIq16JkoiZtWVtY9HWSs9nBnvw3ew8K8u6UAGujXErnMLBDJMOi8d8Vf5bDzrusr_jCie8TQ6Z0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس، نمودار حدود 8 ماه گذشته یکی از پروژه های انگلیسی هست. هیچ فیلتری جز زمان هم ست نشده.
تاریخ 5 فوریه زمان شروع همکاری بوده.
به نظرتون بد شده اوضاعش یا خوب شده؟
اگه میخواید بگید نمودار پوزیشن بدتر شده پس بده که متاسفانه تحلیلتون غلطه و کل سئو رو درست یاد نگرفتید. (
اینجا
توضیح دادم چرا).
اگر میخواید بگید کلیک ها کمتر شده در کل، پس بدتر شده، مثل پوزیشن اونقدر تحلیلتون اشتباه نیست. ولی باز هم کافی نیست. لزوما بدتر نشده.
اتفاقی که افتاده اینه که کلی صفحه با کیورد های اشتباه، حذف شدند. کلی صفحه که مانع رتبه گرفتن بقیه صفحات میشدند ریدایرکت و ادغام شدند(اصلاح تارگتینگ) و کلی صفحه بیخود که فقط باجت رو مصرف می کردند حذف شدند.
این یعنی کلیک هایی که الان نزدیک شده به کلیک زمان شروع این پروژه، نرخ تبدیل بالاتری دارند و کارفرما کاملا تفاوت تماس و مشتری از سایت رو متوجه میشه و مستقیما تاثیر مثبت مالی داره.
سوالم رو دوباره میپرسم. حالا به نظرتون وضعیت سایت بهتر شده یا بدتر؟
😎
سئو رو عمیق و درست یاد بگیریم و با دید تجاری. نه با بلغور ترجمه. نه سطحی. نه غیر کاربردی. نه با لفظ بازی بی کاربرد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/mohsentavoosiseo/859" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-858">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فلسفه زندگی من
روتین
نون کردن
پرداخت بهای غیر زمانی و غیر مالی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/mohsentavoosiseo/858" target="_blank">📅 14:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ادامه پست قبلی:  مغزتون رو درگیر واژه ها نکنید. تو بحث پیچیده و علمی و خاص و واژه سازی حرف زدن، من پروردگار پیچیده سازی هستم! میتونم یه کاری کنم از این به بعد پست های من رو ببینید بگید ااااااااا وای چقدر این آدم خفن و با سواده. ولی کاربرد نداره و بیشتر کسانی…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/mohsentavoosiseo/857" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادامه پست قبلی:
مغزتون رو درگیر واژه ها نکنید. تو بحث پیچیده و علمی و خاص و واژه سازی حرف زدن، من پروردگار پیچیده سازی هستم! میتونم یه کاری کنم از این به بعد پست های من رو ببینید بگید ااااااااا وای چقدر این آدم خفن و با سواده. ولی کاربرد نداره و بیشتر کسانی گول میخورن که تجربه کمتری دارند.
مهمه که انتقال مفهوم و آموزش دادن، ساده باشه، کاربردی باشه و یه نونی بده دستت یا تنور نونواییت رو داغتر کنه. وگرنه آدم ها بعد از مدتی دیدن آموزش هات، میفهمن که با واژه ها، کارشون باتو پیش نمیره.
الان همین پیلار کلاستر که من تو دوره دو فصل دربارش حرف زدم با عنوان Keyword Targeting on Pages،
شاخص داره، ل
ینک داخلی ازش در میاد،
عنوان ها ازش در میان،
نرخ تبدیل ازش در میاد،
رقابت و سرچ والیوم ازش در میاد،
اولویت بندی ازش درمیاد،
انتیتی ها خودبخود اجرا میشن،
ویژگی ها و صفت ها و کاربرد ها ازش در میان،
نالج گراف تا حد مورد نیاز و نه بیشتر، خودبخود تکمیل میشه
و به طور پیشفرض اصلا نقشه موضوعی یا Topical Map استخراج میشه.
و در نهایت منجر به رشد اعتبار موضوعی یا Topical Authority میشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/855" target="_blank">📅 14:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جمله زیر رو یکی از بچه ها در گروه شرکت کنندگان دوره به نقل از دیگری نوشت که نظرم رو در ادامه، زیرش مینویسم.
به نظر من کیورد ریسرچ به شکل سنتی خیلی وقته منسوخ شده.
اگر هنوز فرآیند سئو رو با پیدا کردن کیورد و ساختن لیست کلمات شروع می‌کنید، بهتره رویکرد رو تغییر بدید و وارد مسیرهای جدید بشید:
به جای کیورد ریسرچ، EAV Research
به جای پیدا کردن کلمه، Entity Research
به جای تمرکز روی سرچ‌ولوم، Topic Research
به جای پیلار کلاستر،  Topical Map
به جای تولید محتوا برای کلیک و ایمپرشن ، تکمیل Knowledge Graph سایت
امروز باید ببینید :
موجودیت اصلی کسب‌وکار شما چیست
چه Attribute هایی دارد
چه Entity هایی به آن مرتبط هستند
چه ارتباطی بین آن‌ها باید ساخته شود.
سئو دیگر فقط گرفتن رتبه برای Query نیست؛ ساختن یک مدل معنایی کامل از یک حوزه است که گوگل بتواند تخصص و اعتبار سایت را در آن درک کند.
این حرف، بسیار دهن پر کن و جذاب هست. اما در دنیای اجرا و عمل، برمیگرده به همون چیزهای قبل. وقتی شما به شکل سنتی کیورد ریسرچ میکنی بیشتر از 80 درصد موارد بالا، خودبخود انجام شده است.
یکی از جملات من در دوره که تو آموزش رایگان هم درباره تحقیق کلمات کلیدی در
این لینک
گفتم، اینه که تحقیق کلمات کلیدی، بر اساس صفت، برند و کاربرد باید انجام بشه. دقت کنید: صفت، برند و کاربرد.
همچنین آموزش دادم که چطور خارج از اون کیورد هم کلمه در بیاریم. مثلا برای دسته لوازم جانبی موبایل، "قاب موبایل" که توش "لوازم جانبی" نداره.
پس عملا شما با کیورد ریسرچی که من گفتم یا  خودتون به هر شکلی یاد گرفتید و اینطوری انجام میدید، بیشتر از 80 درصد جملات جذاب نقل قول شده بالا رو دارید اجرا میکنید.
حالا در این شرایط،
EAV Research و Entity Research و Topic Research و چه Attribute هایی دارد و چه Entity هایی به آن مرتبط هستند و  چه ارتباطی بین آن‌ها باید ساخته شود
خودبخود انجام شده. احتمالا نویسنده خودش روش هاش خیلی بیش از حد قدیمی بوده.
این جمله هم کلا اشتباهه:
به جای تولید محتوا برای کلیک و ایمپرشن ، تکمیل Knowledge Graph سایت.
چون اصلا نباید اینکار رو کنید به خصوص در این عصر هوش مصنوعی که AI Overview میاد از رقیب های  همین دیتا رو کامل تر از تو برمیداره و جستجوی عبارت های informational رفته سمت هوش مصنوعی.
گذشت زمانی که باید کامل راجع به یک چیزی حرف بزنی تا رتبه بگیری. واقعیت از اول هم اینطوری نبود اصلا!
یعنی برای اینکه تو "بروکر فارکس" بیای بالا لازم نیست عین همون الفبای قبلی رو درباره ترید مثل "اسپرد چیست" مثل "تحلیل تکنیکال و فاندامنتال" و... که تکرار مکررات هست بیای بنویسی دربارش.
قرار نیست برای اینکه تو کلمه "طراحی سایت" بیای بالا راجع به همه طراحی های سایت ها حرف بزنی. اصلا به این سادگی ها نیست. حرف بزن. بعد که صفحه 5 گیر کردی و رقیبت با Off-Page و ترافیک قوی و بدون هیچ نالج گراف کاملی در سایتش اومد بالا، بیا باهم صحبت کنیم اون موقع.
این جمله کلا از اساس غلطه و نویسنده حتی نمی دونه "موجودیت" یعنی چی.
موجودیت اصلی کسب‌وکار شما چیست.
یه برنامه نویس بهتر متوجه میشه entity یا موجودیت یعنی چی.
کسب و کار که موجودیت نمیشه! مجموعه ای از موجودیت های متصل به هم میشه یک کسب و کار. اگه بخوایم از نگاه اسکیما بهش موجودیت بدیم، میشه یه local business یا person یا organization. کسب و کار محلی، شخص یا سازمان. همین! الان این حس خفن بودن میده؟ واااااااای من موجودیت کسب و کارم رو دراوردم! سلطان خود پیش فرض افزونه های سئو وردپرس اینو برات میندازن اصلا. نیازی به زحمتت نبود!
اگرم منظور خود موجودیت غیر اسکیمایی هست که یک کسب و کار، یه دونه موجودیت نیست که! جمله غلطه!
انتیتی یا موجودیت یعنی یک چیز! واقعا چیز! یک thing. که جدا و قابل تشخیصه. و اسم داره، هویت داره، ویژگی داره و ارتباط با سایر موجودیت ها. الان محسن طاوسی یک موجودیت هست. اسم داره. مکان داره ویژگی داره. و تمام ویژگی های موجودیت "انسان" رو به ارث میبره.
الان حس می کنی سئو رو خیلی خفن تر بلدی؟ نه فقط مغز بیچارت رو پر از دیتای بی کاربرد کردی که تو رو از پول دور میکنه ولی احساس کاذب خفن بودن بهت میده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/mohsentavoosiseo/854" target="_blank">📅 14:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نظر من درباره ابزار های تحقیق کلمات کلیدی:
🔴
موافق اصرار بر اینکه کیورد تول خوبه منگولز خوب نیست(KWFinder) نیستم. این صرفا یه احساس هست. واقعا منگولز یه چیز دیگست. اگر مبلغ اورجینال اختصاصیشو حساب کنیم، از کیورتول ارزون تر هم هست. خیلی هم کامل تره. سرچ با دامنه هم داره. و کلی امکانات دیگه.
🟢
فقط برای کیورد های فارسی، همون سئو سیگنالز کافیه مگر اینکه دوست داشته باشید ابزار جهانی بخرید. یعنی صرفا با سئو سیگنال چیزی از دست نمیدید برای کیورد های فارسی. اتفاقا استخراج کلمات با وارد کردن دامنه هم داره. قوی هم هست تو فارسی ها.
عدد های سرچ والیوم(تعداد جستجوی کلمات در ماه) هم خیلی روش حساب نکنید. همه ابزار ها دقیق نیستند. کلا نمیشه دقیق فهمید. حدودی هم نمیشه فهمید. ولی نسبت رو میشه فهمید. همون کافیه. رو هر عددی که ابزار ها میدن حساب کنید. اما برنامه ریزی مالی روش نکنید.
🟢
ابزار خارجی ارزون تری که اشتراکیشم راحت تر در دسترس هست، سمراش هست. Semrush جستجو با دامنه هم داره. یعنی استخراج کلمات با وارد کردن دامنه. و گپ رقبا. اما خیلی ضعیف تر از منگولز و کیورد تول هست.
🟢
برای گپ، نیازی نیست خود اون ابزاره گپ داشته باشه. من تو آموزش زیر به صورت کاملا رایگان و با گوگل شیت یا اکسل، استخراج کیورد گپ رو آموزش دادم. کافیه با ابزار ها بر اساس دامنه، استخراج کنید. بعد رقیباتون رو طبق آموزشی که گفتم قرار بدید تو شیت. خودتونم کیورد های سایت خودتونو قرار بدید تو شیت.
و خود این فایل شیت که دادم(کپی بگیرید ازش)، گپ رو میده:
https://mohsentavoosi.com/video/keyword-gap-excel/
اینم لینک کامل آموزش و مستنداتش و گوگل شیتش(تقاضای دسترسی ندید. read only هست). به جاش کپی کنید ازش از منوی File، و برای خودتون مستقل داشته باشید و هر بلایی خواستید سرش بیارید.
اگر آموزش میدید یا به کسی کمک میکنید، منشن من و منبع(اینجا) رو فراموش نکنید. من کپی کننده خارجی ها نیستم که بگید خودشوم از خارجیا برداشته و این حرفا.
❕
پی نوشت 1:
کیورد گپ یعنی رقباتون رو چه کیورد هایی رتبه یا ایمپرشن کلیک دارند و شما ندارید. شکاف کلمات کلیدی. قسمت خالی کلمات کلیدی و ضعف شما نسبت به رقباتون.
❗️
پی نوشت 2:
کامنت های زیادی زیر پستی که گذاشتم اومده که لینک گوگل شیت کجاست؟ در حالی که تو متن پست گذاشتم تو ویدیو هم کلامی و تصویری گفتم لینک رو. بخونید کامل صفحه رو.
‼️
پی نوشت 3:
ترخدا مغزتونو با استوری و پست دیدن اینستا و یوتیوب نابود نکنید. مغز خیلی ها بدو بدو شده یه صفحه رو نمیتونن یک بار بشینن کامل بخونن. پنج هزار بار درباره محتوایی که میبینن سوال تو ذهنشون ایجاد میشه چون یک بار نمیتونن ببینن و تمرکز کنن. خیلی اوضاع تمرکز ذهن ها خرابه.
‼️
پی نوشت 4:
بخدا من هم ADHD دارم یا ژنتیکی یا از محیط و عادت. ولی کنترلش کردم. من هم درون گرام یا حداقل درون گرایی قوی دارم. ولی توجیه نمیکنم(میون پرانتز، توجیه رو توجیح ننویسید)  که چون از درون انرژی میگیرم، پس ارتباطات بلد نباشم یا خجالت بکشم، و بگم من خجالت و بلد نبودنم اشکال نداره چون درون گرام!
درونگرا باید بتونه جلوی پنج هزار نفر سخنرانی کنه حتی با تپق ولی بدون خجالت و بتونه احساساتشو در جمع بیان کنه. اگر نمیتونه ربطی به درون گرایی نداره. به خدا قسم نداره. اگر آتئیستی به خاک استیفن هاوکینگ و داروین قسم که بی مهارتیه. شرم الکیه. جای رشد داره.
درون گرا فقط از درون خودش بیشتر از بیرون انرژی دریافت میکنه. شارژش تو تنهاییه. همین! چه ربطی به خجالتی بودن و بی مهارت بودن تو ارتباطات داره؟!
یه ای دی اچ دی در سطحی که تو جامعست(نه بچه هایی که از سنین کم اختلال یادگیری دارند)، هم میتونه یاد بگیره تمرکز کنه. بدون قرص. یه بار هم که شده مسئولیت خودمونو گردن بگیریم. تو این عصر هوش مصنوعی میخواید همچنان بدو بدو همه چیو ببینید؟ چجوری میخواید AI Agent تربیت کنید پس؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/mohsentavoosiseo/852" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a9cb06f1.mp4?token=sHdzRq_GkPEa6gT65AO-vRHp_D6Tk_ma2-W4TfH63Y055iOdcG2R1a9J_m2Lp9oHfRqmDHy7M-Urk2YYxHUMckSUpdIJyP3ulaMlbq3ljzw91LlcF--Uz-G51pfuvx0WTT5f7riAyTP4ClMnK7Q5Ga6lvflwQBTX5AwekosiUTjo0hd1jxAXNR2iRTER5A4Ak9xL-6O9i4Uxo20pRdttEc8RjT6ejCmgM4XR0mE_PfLiyVnabodxMWEJfUssGzfzZYnoEMb4VSCsVyxAjvVBTrVHBDc1v5rVBGQvOG4zk2146iqf6ltTI2LSauKgXPwncR1Xf9z5zsrNiY8LGujJJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a9cb06f1.mp4?token=sHdzRq_GkPEa6gT65AO-vRHp_D6Tk_ma2-W4TfH63Y055iOdcG2R1a9J_m2Lp9oHfRqmDHy7M-Urk2YYxHUMckSUpdIJyP3ulaMlbq3ljzw91LlcF--Uz-G51pfuvx0WTT5f7riAyTP4ClMnK7Q5Ga6lvflwQBTX5AwekosiUTjo0hd1jxAXNR2iRTER5A4Ak9xL-6O9i4Uxo20pRdttEc8RjT6ejCmgM4XR0mE_PfLiyVnabodxMWEJfUssGzfzZYnoEMb4VSCsVyxAjvVBTrVHBDc1v5rVBGQvOG4zk2146iqf6ltTI2LSauKgXPwncR1Xf9z5zsrNiY8LGujJJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
تو جشنواره تریبون، رتبه‌ات رو برگردون
🍀
تا ۸۰٪ تخفیف خرید رپورتاژ
🌼
تا ۶۰٪ تخفیف خرید بک‌لینک
🌿
۲٪ کش بک روی هر سبد خرید
🌼
رپورتاژ رایگان و امکان پرداخت قسطی
🍒
فقط تا ۳ مرداد
🍊
همین الان وارد جشنواره تریبون شو و رتبه‌ات رو برگردون
اطلاعات بیشتر در:
⬇️
tribn.ir/Vrfz6P
tribn.ir/Vrfz6P
ℹ️
این پست، تبلیغ هست. Ad
ℹ️</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/851" target="_blank">📅 16:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان اینجا کسی هست تو عنوان نویسی رپورتاژ قوی باشه ؟
چه جالب مگه عنوان نویسی شاخه جدایی داره خوب هر کی مقاله رو بنویسه عنوانم در میاره دیگه! مگه اینجوری نیست!؟
Are you kidding? Realy?
واقعا بعد از دیدن دوره و این همه ویدیو و سرفصل، سوال دوم بالا سواله؟
😭
😭
یعنی تولید کننده محتوا اطلاعات داره از سرچ والیوم و ابزار کیورد ریسرچ و میانگین موضوع کیورد و سایت شما و سایت رسانه رپورتاژ که این همه تو دوره ویدیو داره؟
طبیعیه که ادم ها دوره رو کامل نبینن. ولی بهتر نیست سوال شه که ااااا راجع بهش تو دوره هست؟ کدوم فصل ها کدوم ویدیو ها؟
تو این عصر هوش مصنوعی همه رو از AI میپرسی یا از دانشگاه یوتیوب! پس قطعا من باید ارزش افزوده دیگه ای داشته باشم. وگرنه که این همه مدرس. این همه آموزش رایگان. این همه منبع.
اگر دوره من رو دارید، ببینیدش! استفاده کنید ازش. دریاییه که تو محتواش غرق میشید. ولی موج سوار تو دریای طوفانی بیرون میاید.
THANKS FOR YOUR ATTENTION TO THIS MATTER. PRESIDENT MT.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/mohsentavoosiseo/848" target="_blank">📅 00:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/mohsentavoosiseo/847" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/mohsentavoosiseo/846" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/mohsentavoosiseo/844" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.
با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.
پس من ورود نمی کنم به اینکار. و میخوام شما بگید از کجا میگیرید که عمومی بذارم بقیه هم برن بگیرن. کلاد بدون دردسر و بدون محدودیت.
از یک سرویس عمومی که همه بتونن. نه دوست و آشنا و کارت خارجی خودتون.
بگید که منم به بقیه بگم. تو دایرکت کانال بفرستید.
اگر ا......ت بوده فقط اگه بعد از اون بن شدن های دسته جمعیش بوده باشه بگید.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/mohsentavoosiseo/843" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/mohsentavoosiseo/842" target="_blank">📅 15:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/mohsentavoosiseo/841" target="_blank">📅 15:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ربطی به سوال بالا نداره. کلی هست.
با کلاس و بی کلاس در تعریف من.
پرداخت به هرچیزی جز خود‌ عیب جویی از هرکسی جز خود. مطابق مطالب زرد و سطحی.
#تروما
#آسیب
#سمی
#طرحواره
#تله
#عیب
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/mohsentavoosiseo/840" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/mohsentavoosiseo/839" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-838">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/838" target="_blank">📅 14:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پاسخ سوال بالا، قسمت ششم
در تجارت، تواضع اشتباه هست.منت گذاشتن بسیار مهم و جایز هست. ترکیب تضادها در کار.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/mohsentavoosiseo/837" target="_blank">📅 14:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پاسخ سوال بالا، قسمت پنجم
انتقال پیام پنهان ضعف
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/mohsentavoosiseo/836" target="_blank">📅 14:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پاسخ سوال بالا، قسمت چهارم
هم خدا هم خرما. در نظر گرفتن استاندارد تخفیفی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/mohsentavoosiseo/835" target="_blank">📅 14:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/mohsentavoosiseo/834" target="_blank">📅 14:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/mohsentavoosiseo/833" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/mohsentavoosiseo/831" target="_blank">📅 13:53 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
