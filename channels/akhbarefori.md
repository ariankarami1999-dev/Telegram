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
<img src="https://cdn4.telesco.pe/file/FIXAL94d67otrcg8al9JeVjYlStH4suVu0r5XETLbJi8FwmuwZqNN3_IpLUuGWr2IbZxXmy-EI9H5YVvn3XSI86dvx9Mr5XHRirG9Zr2D-GUbOmRBjhFVkahDMsIp8xzh5VMdM9MrhtxnBL9IPBFnt3lp4IJzxY9zd8JDfhi7MhdUuizq4SQxFY40YTaQNRcYNGmXVOg3KSJDEPqq2QYf3W_vZNp_INN2c66pn8vI5Zt6dTWBsnZUFhFfYAd9ErQ8iUyjLuAcoJ9sXr4uHIB9R4RTErnF3gAr0fM7piI3sU7c05OHww-jPnUvSuCEjYt-86IjHR_CVgN7xQAZozeaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.11M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-690344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ایرنا: ۶ همت از مطالبات مراکز درمانی دانشگاهی پرداخت شد
🔹
سازمان تأمین اجتماعی امروز سه‌شنبه، ۲۴ شهریور، ۶ هزار میلیارد تومان از مطالبات مربوط به اسناد رسیدگی‌شده مراکز درمانی دانشگاهی و علوم پزشکی طرف قرارداد در سراسر کشور را پرداخت کرد.
🔹
این پرداخت، بخشی از روند تسویه مطالبات مراکز درمانی است و با هدف حمایت از مراکز ارائه‌دهنده خدمات و جلوگیری از ایجاد اختلال در درمان بیمه‌شدگان و بازنشستگان انجام شده است. روند پرداخت سایر مطالبات نیز از سوی سازمان تأمین اجتماعی ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
| Link</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/akhbarefori/690344" target="_blank">📅 14:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وزیر اقتصاد: ۳۰۰ هزارتومان کف افزایش کالابرگ است   وزیر اقتصاد:
🔹
درباره میزان رقم افزایش کالابرگ هنوز جزییات مشخص نیست و در حال بحث است.
🔹
کف افزایش ۳۰۰ هزار تومان است ولی هنوز دهک ها مشخص نیست./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/690343" target="_blank">📅 13:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وزیر اقتصاد: ۳۰۰ هزارتومان کف افزایش کالابرگ است   وزیر اقتصاد:
🔹
درباره میزان رقم افزایش کالابرگ هنوز جزییات مشخص نیست و در حال بحث است.
🔹
کف افزایش ۳۰۰ هزار تومان است ولی هنوز دهک ها مشخص نیست./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/690342" target="_blank">📅 13:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYiNYWoaGryiUFbwGrR-D6eSWQXn6qharw6U7E6er1Tj_JJlNuocYQByEDdHXs5UMvcQZu80bQjyVLNMIiijDcIHfMGr5z43W6s4PILxczLBmX8UbH2jkviL-tJOIUog8mALsrnymPH9Aj_Y05K_hwhSQQNxPZDtiBuHZZECtpIJAVz4c_BZd94Da7Xoga55Zy7f8PahhyGX-p3L__bAltb-nWFN70LNUXy5uiD6Jlj9qOsCuHTk5eRO2obOVhCsNb3uWWK7KWuIf4XqtHILsyaum05wMq_jocm8ayJlRWVLiDiWJf7GgswKWBIHuzPxH9P0mVf_C1FIQM5CZ5EXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامانه ناظر طلا؛ نظارت بدون متولی؟
🔹
الزام سکوهای فروش آنلاین طلا به اتصال به «سامانه ناظر» در حالی وارد مرحله اجرا شده که همچنان درباره متولی سامانه، مبنای حقوقی، دستورالعمل نظارتی و حدود مسئولیت دستگاه‌ها پرسش‌هایی وجود دارد. این سامانه قرار است موجودی طلای سکوها را با تعهدات آنها تطبیق دهد و از خالی‌فروشی جلوگیری کند.
🔹
در کنار ضرورت نظارت بر پشتوانه معاملات، نحوه حفاظت از اطلاعات مالی کاربران نیز به یکی از چالش‌های اصلی تبدیل شده است؛ اینکه داده‌ها کجا نگهداری می‌شوند، چه نهادهایی به آنها دسترسی دارند و در صورت خطا یا نشت اطلاعات، چه دستگاهی پاسخگو خواهد بود.
🔹
حاکم ممکان، عضو کمیسیون اقتصادی مجلس، با تاکید بر ضرورت نظارت بر سکوهای فروش آنلاین طلا گفت: «اصل نظارت بر فعالیت سکوهای طلا و اطمینان از وجود پشتوانه کافی برای معاملات ضروری است»، اما متولی سامانه و حدود مسئولیت دستگاه‌ها باید به‌طور شفاف مشخص شود.
🔹
فرشاد ابراهیم‌پور، عضو هیات‌رئیسه مجلس نیز تاکید کرده است: «اصل نظارت بر فعالیت سکوهای فروش طلا موضوعی قابل دفاع است»، اما پیش از الزام سکوها به اتصال، دستورالعمل نظارتی و مسئولیت دستگاه‌ها باید مشخص و ابلاغ شود.
🔹
در نهایت، پرسش اصلی این است: سامانه‌ای که قرار است ابزار نظارت بر بازار طلا باشد، خود تحت نظارت کدام نهاد و بر اساس چه چارچوبی فعالیت می‌کند؟/ دنیای اقتصاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/690340" target="_blank">📅 13:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معرفی و میزان تخریب پایگاه شاهزاده سلطان (الخرج)
🔹
در طول جنگ رمضان، ایران در جواب حملات دشمنان، ضربات متعددی به پایگاه‌های آمریکایی در ۷ کشور منطقه وارد کرد.
🔹
آمریکا دارای ۱ پایگاه اصلی در کشور عربستان است و بقیه تجهیزات نظامی آن در کل کشور عربستان به صورت…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/690339" target="_blank">📅 13:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
افزایش رقم کالابرگ قطعی شد
🔹
رقم جدید و نحوه توزیع این افزایش میان دهک‌ها هنوز مشخص نیست و گزارش‌هایی درباره احتمال اختصاص اعتبار بیشتر به دهک‌های پایین درآمدی مطرح شده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/690338" target="_blank">📅 13:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
خبرفوری| هم‌اکنون نرخ سوم سوخت از ۵ هزار تومان به ۱۰ هزار تومان تغییر کرد @AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/690337" target="_blank">📅 13:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGR-6jzYHh_Il3Jp0bc8UOQQFvz2w1XHMuo8ulXAbkS8kobeQKE7ADYo0ZIbVqwq4-chLGAwiYGRcME5fCiO4lebo8jFIToKVtHEnZitJZLnROxzcHpvqyMfz_6H2k81okrsDjsOwMkMLijjzeHN_eGwn82dUsejV5k8ZaHPiueprWDfIgua07i0eXprC23tQNCZzaVRt1Qe9HJeUUHiU7xpT_pID0ozgCzDW6-NwLmvwKX7jlxVGD1ksAc_tnQUXwq2o0hOBMoGliMEtidXLAMEPV8_wHuWoLNmhJR_zVz-14EtAeMRp16iGOK7rhLINw7UtlmzYs-QAWjZhnoJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌زمان با تشدید حملات یمن به عربستان سعودی، سفارت آمریکا در ریاض از شهروندان این کشور خواست از سفر به مناطق نزدیک مرز عربستان با یمن خودداری کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/690336" target="_blank">📅 13:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGXoRBPVXHWdIHNkvPQDNiyPJB_8Bjw4wZM_1K3SsdeMeqUr2LGJ60AvfAU7HhtXl2TShaz0_WnfSCkh6bcWZlrp9SIRQu3dqZhWacEoQC6Osflcrkdr0TB3UOABPLqxlZKne7_0mKMCuJ9EGIPDqx5_wYin0r2gzLQlU3k86meO8PG19giSgwAOi90Uf_9UWk3zWtjf0pJExbms6n6VXzIXdMiMYvD2pRYPSvCAWV193RTcgOCvjtocQ7bfUWXuXejIjldisUw62B7VImWTsvk1iiU69Yjw-pgsclj9bnnefr6j1ikZ_07wBF9zvH-JBkwxD4gWZGrMUEmSbKe4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش میلی‌ به ادعای طلای تقلبی: تصویر منتشرشده ارتباطی با شمش‌های میلی ندارد
🔹
پس از انتشار ادعاهایی درباره تحویل طلای تقلبی در میلی‌، مدیر ارتباطات این پلتفرم در گفت‌وگو با رویداد۲۴ این ادعاها را رد کرد و گفت بسته‌بندی منتشرشده در فضای مجازی اساساً متعلق به میلی نیست.
🔹
امیرحسین صدقی تأکید کرد تاکنون بیش از ۵۵۰ کیلوگرم طلای فیزیکی به کاربران تحویل شده و هیچ گزارشی درباره تقلبی بودن شمش‌های تحویلی ثبت نشده است.
🔹
او ادامه داد:  آنچه در روز‌های اخیر در فضای مجازی منتشر شده، اساساً ارتباطی با شمش‌های تحویلی میلی ندارد. شمش‌های طلای میلی با بسته‌بندی اختصاصی، قفل‌های امنیتی مشخص، هولوگرام و چندین لایه اصالت‌سنجی به کاربران تحویل داده می‌شوند. سکه یا بسته‌بندی که تصاویر آن در شبکه‌های اجتماعی منتشر شده، از اساس متعلق به میلی نیست و نسبت دادن آن به این مجموعه نادرست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690335" target="_blank">📅 13:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
الجزیره: چین از ایران و آمریکا خواست به تفاهم‌نامه بازگردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690334" target="_blank">📅 13:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال قطع گاز خانگی در پاییز و زمستان
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
با توجه به احتمال سردتر بودن پاییز و زمستان امسال، افزایش مصرف خانگی و کاهش بخشی از تولید به‌دلیل حملات آمریکا به تاسیسات گاز، کشور در حوزه تأمین گاز با چالش جدی مواجه خواهد بود.
🔹
بخش عمده کسری گاز از طریق محدودیت مصرف صنایع، جبران می‌شود اما ممکن است امسال برخی استان‌های دورتر از منابع گازی به‌دلیل کاهش فشار، حتی گاز خانگی خود را نیز از دست بدهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/690333" target="_blank">📅 13:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پایین کشیدن پرچم حکومت جولانی در منطقه الحسکه در شمال شرق سوریه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/690332" target="_blank">📅 13:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daTchCF_wtTl-GJphlA69ne4EyTfovtUphhNRoWeeKiUH4UgyEhIVtv-mn5YI3E-6-hgL1JVlUH7SOCDxVaqK0O-E7jVJETCsyO3_occmdfufQ3Q1F8d0PJF-m7YTVW2xxfJFEYnSM_ZLOLhSiNScytCLIZFsWgGHIZjEzbK8g-9W1Tvp-2SMBy00SldO7A7iyh4b_iCTc0bmQxCa8wCtszsk9d7d64iI8MnH7BqtZkcQ_JQgQmr-66WyIAFwWZk8dRU11cH_AGv9ufVpo3sjOD5PVwHWd6a9C_TClclSajUpoGw-QjgHxJjtLNPQV0mDt87ZUMt_VUfsiUdFyor2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۵ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
بازار امروز شاهد رفتارهای واگرا میان بازارهای دارایی بود؛ در حالی که دلار آزاد با عقب‌نشینی از سطح ۲۳۰ هزار تومانی به مسیر کاهشی بازگشت، بازارهای طلا و سکه تحت تأثیر رشد انس جهانی طلا، روند صعودی را در پیش گرفتند.
🔹
طلا ۱۸ عیار با جهش ۳۵۰ هزار تومانی از مرز ۲۳ میلیون و ۵۰۰ هزار تومان عبور کرد و سکه بهار آزادی نیز با قیمت ۲۲۹ میلیون و ۵۴۰ هزار تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690331" target="_blank">📅 12:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/busjA1nMn9P8T83msPQVDWsolcTI9LYSCl9sz5p80CwsZCJZ__ghAmme6p7rMmxITCi0OYbABb7Lar5CZpSzvU-yqWhTrOj6Z_cDboS8Kjmenyztza7uW8U0kSxCxCju_IcXNRqeFCVKq6PEiwioI33ohb-l_HDjb1GgpXXChbXzotKHnQnkA-p1U7rm_7jZaMzzaxAAdorLVN1r47ghn3OAlNKsWVOOo2YnTpdgIRxqAltjKjZbrmUiAHnOlCLtgD5H-KSAzyAs5UEcvUGBkO47bGLhPNUgDq__tyKkh4rVl9Y2MIYC8ObLdRjUWyTf-mQ12a8BBOUMkUc1PZbs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین دیوارنگاره میدان ونک با اشاره به غنیمت گرفتن زیردریایی آمریکایی
صید هرمز؛ بازار باشه!
🔹
همزمان با هدف قرار گرفتن ناوهای متخاصم و زیردریایی پیشرفته آمریکایی در آب‌های خلیج فارس، از جدیدترین طرح دیوارنگاره میدان انقلاب تهران با شعار "لشکر شیطان در خلیج فارس غرق خواهد شد" رونمایی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/690330" target="_blank">📅 12:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
الجزیره: چین از ایران و آمریکا خواست به تفاهم‌نامه بازگردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/690329" target="_blank">📅 12:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17905a14b6.mp4?token=lxmZDrQMERRwtbX6soAWWKcZqX8LU7cyvB9HRbqB_NlIoukKqAgR7LbUDt-VEpHm33lgr83tzc8uOkLYl1cX0XB9mf0ycmPbbZiIO9Lq9jM5sL--4HEYEBVglPT-YUcjlGXiQN3nD9gNlZzkVkidMA_6hUVoRcWxrQQkXK6WjfEfiTgIBqt21avAYg8auF84OoXSvgckNVRwjAIJfUIDrvhUisNdU1tUpPgAqWWx9CbevMXsACxlm6-x0BnbiAzEEDD9MjbyayuwX9XEunSkXDUl_e7cpNHZLy6b62gX-K6eHOHZE3x8tka48g7-kxgxAio78FyiM7xCozapG25kxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17905a14b6.mp4?token=lxmZDrQMERRwtbX6soAWWKcZqX8LU7cyvB9HRbqB_NlIoukKqAgR7LbUDt-VEpHm33lgr83tzc8uOkLYl1cX0XB9mf0ycmPbbZiIO9Lq9jM5sL--4HEYEBVglPT-YUcjlGXiQN3nD9gNlZzkVkidMA_6hUVoRcWxrQQkXK6WjfEfiTgIBqt21avAYg8auF84OoXSvgckNVRwjAIJfUIDrvhUisNdU1tUpPgAqWWx9CbevMXsACxlm6-x0BnbiAzEEDD9MjbyayuwX9XEunSkXDUl_e7cpNHZLy6b62gX-K6eHOHZE3x8tka48g7-kxgxAio78FyiM7xCozapG25kxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز خنک‌کننده یخچال‌های باستانی ایران؛ شاهکار مهندسی و معماری
🔹
در دل کویرهای ایران، یخچال‌های باستانی راهکاری شگفت‌انگیز برای تولید و نگهداری یخ بودند؛ بدون برق و با استفاده از معماری هوشمندانه، سایه، جریان هوا و سرمای شب.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/690328" target="_blank">📅 12:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حمله سایبری به دو نفتکش در تنگه جبل‌الطارق
وال‌استریت‌ژورنال:
🔹
دو نفتکش با پرچم کشورهای خارجی که عازم آمریکا بودند، هنگام عبور از تنگه جبل‌الطارق هدف حملات سایبری قرار گرفتند. واشنگتن تاکنون عامل این حملات را شناسایی نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/690327" target="_blank">📅 12:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
گلایه رانندگان از وضعیت نابسامان مرز دوغارون/ متولی این مرز کدام دستگاه است؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/690326" target="_blank">📅 12:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d353ee59.mp4?token=PFA1RyxBgzJik96Mz5pWmmFvqheI_I5mRY9WJByW5VxE54a_ceT0v8fkgQzUd0CF3KDQgRe2TAmlkjNU7xA00O1QhiquW4T9fFzX6bODNpm3j1fFms3ZdyhUJbnrlvgPJpkjx3l-vKtED3WjnbZkiaPyUrisZ7P0cjTNah4UF6lEQ_avIj4Bx9REpHSI-gV3_cVxeiN_70z9xBYkICghjL_hsY5yX0SS94m-GX2nQLZjPw59584KIksNTZ8Sgv4ZQbmNE_3NTy58vEZYjvTtZrsgF-Cks2NgAFY5wUotOIA03V0Mwg7QN0UmYLbWG-kPj_JoL87rIoX3_ObvD-eWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d353ee59.mp4?token=PFA1RyxBgzJik96Mz5pWmmFvqheI_I5mRY9WJByW5VxE54a_ceT0v8fkgQzUd0CF3KDQgRe2TAmlkjNU7xA00O1QhiquW4T9fFzX6bODNpm3j1fFms3ZdyhUJbnrlvgPJpkjx3l-vKtED3WjnbZkiaPyUrisZ7P0cjTNah4UF6lEQ_avIj4Bx9REpHSI-gV3_cVxeiN_70z9xBYkICghjL_hsY5yX0SS94m-GX2nQLZjPw59584KIksNTZ8Sgv4ZQbmNE_3NTy58vEZYjvTtZrsgF-Cks2NgAFY5wUotOIA03V0Mwg7QN0UmYLbWG-kPj_JoL87rIoX3_ObvD-eWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جانشین ستاد کل نیروهای مسلح: موشک‌های ما آسیب‌های جدی به ناوهای آمریکایی و ناوچه‌های همراهشان وارد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/690325" target="_blank">📅 12:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه آرمان آتی | ArmanAti</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3HH1_O2XcdYj1uJK9EDON_zb2IumG9vG0VIwb7ZdGQfybrAh3fs-x81OvpnglgfIgXGVrZKiqKY0WWLInqL1lke7GpWhHl5G1HGxJX9yJkccvrlHepRQzCi_ZOKmmySJL8tiMDrkvjHq3rxJaeOA3hd_af0JUgDg-VThJ4E1YXMF1LUhhBeC0bgpuupgTWkmWG_ZLNFua_VD-EbcQBSUu76yXJ3txClQ3V0aOszkjWE_uYSkHF1eI2a0775KtKWB-oQfLQ-Q9iI1gByuD5gNgWtvX-3sgCIX9zJeTq05In1F_00v_bDOgetVCmu6e8gGlxBw653cvrBhSudkon5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏦
بالاترین نرخ سود موثر سالیانه
صندوق‌های تقسیم سودی با "گلبرگ" هم‌اکنون ۳۹
٪
است!
💳
هر ۱۰۰ میلیون تومان سرمایه‌گذاری = ۳۹ میلیون تومان سود
✅
سابقه درخشان – پایبندی به تعهدات سوددهی حتی در تعطیلات
✅
مدیریت حرفه‌ای دارایی – رشد سرمایه در امنیت کامل
✅
واریز سود ماهانه و کاملا منظم
💰
سرمایه گذاری از طریق سایت صندوق با نماد:
◀️
گلبرگ
➡️
🖥
لینک سرمایه‌گذاری و کسب اطلاعات بیشتر
⬇️
🗣
سایت صندوق گلبرگ
⚡️
همچنین جهت دریافت مشاوره رایگان و کسب اطلاعات بیشتر می‌توانید با شماره زیر تماس حاصل فرمایید:
🗣
02157206000
❤️
یک آتیه آرمانی…
📱
@ArmanAti</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/690324" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc63f399e.mp4?token=Qx1WhnjCg7iTNeBsO25TsLSQ8TZ0WCZnQTvc-edihQnb0L5pH2I9Eivm010m0ZPS9f6mLcwR7ecsde-9eDmEzwgJOSMT5Fe9xCUwEG7xtY4loG6bYkxV9UbLtEx-hl4JKggR6o1nIuujsKFdhoCrWTnfgjv3HQd3blEumVfrBTXZRtBq5sJNkUEkOIvp3-L5ihzd2QMie5qWZ1c9Dt99FGQdBgI4rvwZy978xE8W2DogiTzhwyfeunaY_CERPSWQxXTb8ZEDLXjXU1rIOJGnq5om25If2YdoaVBmKLH9tjwqW654WgPNVhqiIekuxtlWakXXCu6g2s21zm3SfMClbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc63f399e.mp4?token=Qx1WhnjCg7iTNeBsO25TsLSQ8TZ0WCZnQTvc-edihQnb0L5pH2I9Eivm010m0ZPS9f6mLcwR7ecsde-9eDmEzwgJOSMT5Fe9xCUwEG7xtY4loG6bYkxV9UbLtEx-hl4JKggR6o1nIuujsKFdhoCrWTnfgjv3HQd3blEumVfrBTXZRtBq5sJNkUEkOIvp3-L5ihzd2QMie5qWZ1c9Dt99FGQdBgI4rvwZy978xE8W2DogiTzhwyfeunaY_CERPSWQxXTb8ZEDLXjXU1rIOJGnq5om25If2YdoaVBmKLH9tjwqW654WgPNVhqiIekuxtlWakXXCu6g2s21zm3SfMClbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♥️
یک تغییر کوچک، یک همراهی بزرگ
پویش ملی «۲۵ درجه؛ قرار همدلی» با همراهی شما به ثمر نشست؛ با هم نشان دادیم که مسئولیت‌پذیری هرکدام از ما، پایداری برق برای همه است. از همراهی شما صمیمانه سپاسگزاریم.
💚
قرار همدلی ما برقرار می‌ماند...
#پویش_ملی_۲۵_درجه
|
#قرار_همدلی
|
#صنعت_برق_عرصه_تلاش_و_خدمت
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/690323" target="_blank">📅 12:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سفارت آمریکا در ریاض: به شهروندان خود توصیه می‌کنیم با توجه به احتمال هدف قرار گرفتن منافع ما توسط ایران، در مورد سفر به این کشور تجدید نظر کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/690321" target="_blank">📅 12:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8008a3b3f9.mp4?token=Lu7dWTWGelrLGZM3Xgr5GT7bst3pRn59LohrioUEfvHXE_Ml2-lPwfTIqYweRFB81AkpDoz10dqvnpOHQvB7dqjJGEN5vjHO067CYzuF_jc9oQMc_O45UwJW2Bnd8Vw7wiWcpdy9MhGhXbpekEIXTOeJYbvYSp6qyag45XtIBhUhNTnoy4r3GCydoaz5QgBgMphxRiWFV9CtlrGurLyCjH7gAYwuCDk50xzTIfChLxfAIkjkLzgVEBKnW0FSga69kmCN4SHT_6c578T3v4zfzURsLul2sXxYpnOfnYjnW2-L94fs7_04YQpLmKEl8DCWy84UMVuovuRMcz3DGbsang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8008a3b3f9.mp4?token=Lu7dWTWGelrLGZM3Xgr5GT7bst3pRn59LohrioUEfvHXE_Ml2-lPwfTIqYweRFB81AkpDoz10dqvnpOHQvB7dqjJGEN5vjHO067CYzuF_jc9oQMc_O45UwJW2Bnd8Vw7wiWcpdy9MhGhXbpekEIXTOeJYbvYSp6qyag45XtIBhUhNTnoy4r3GCydoaz5QgBgMphxRiWFV9CtlrGurLyCjH7gAYwuCDk50xzTIfChLxfAIkjkLzgVEBKnW0FSga69kmCN4SHT_6c578T3v4zfzURsLul2sXxYpnOfnYjnW2-L94fs7_04YQpLmKEl8DCWy84UMVuovuRMcz3DGbsang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده‌ای ساده برای جابه‌جایی وسایل سنگین در ساختمان‌های بدون آسانسور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/690320" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UputzRVYPkn4zYE11xJ5kqqULR58EAOTmkQQvXru4kzypSTJimgNMXUU4DguHJeYM_6ecYoKyNrJxx7D6xkgCKJs9UPx4exnHeSlq5SrYUQBKwvCkq-98T0-BzAo3I0ESwK5OlFIoMrm5B5JAwfOeoA4S39Z-PrfjzOX9rxKYkzpoVIacFmd-4ORuArTMrxGCBK0TBKoOmeoN4Ux_KQe8pExi8_wLTU5LOflMay18cWv2ocVl2F-U0cHYy6TWe0gAp7WuyApwa6Q98IkUfuct3-7AbMplE7isEnFadR2T0UZ-AziqMIjM-vhQjGWOppPRVWgydSpwoCYrr5BVkKuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار نیوزمکس: روایت «نجات خلبان» آمریکا نیازمند راستی‌آزمایی است
🔹
برجسته‌سازی روایت نجات خلبان می‌تواند بخشی از تلاش برای مدیریت افکار عمومی، پنهان کردن هزینه‌ها و نتایج احتمالی عملیات و بهره‌برداری انتخاباتی باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/690319" target="_blank">📅 12:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bd069184.mp4?token=VGB7GAh0cY1Kyr6GNM-UZP2NIOy-dYb_l28KrXC3wL_x3xrCPQw1e8Yk-3tYwE-sfrHXCk8KRLWBiWgfGNhulhMf9KE3gFjnNOY3_NdOOg1lZo0zd8ZY8rLDHSyr2SFB1qL4cTgMFyWZs_KPBz-0m2QhfrIROriMO1FYNWLAvCm9NsovqLQRr6YA_bkfEpNEWqE1WblxOq1v3-320ViSvm9RanG1di3chMeBbgOk0T0ng9DLsLYEXQFg8bsOv-qTayNeR6hMyEkPvZPstRTmkGvuJz0vVOSprXqZX0yzc1aaEHi0FpQKJdZwpQZYGfDubzVjUIP0MWZw2eiC2WsDRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bd069184.mp4?token=VGB7GAh0cY1Kyr6GNM-UZP2NIOy-dYb_l28KrXC3wL_x3xrCPQw1e8Yk-3tYwE-sfrHXCk8KRLWBiWgfGNhulhMf9KE3gFjnNOY3_NdOOg1lZo0zd8ZY8rLDHSyr2SFB1qL4cTgMFyWZs_KPBz-0m2QhfrIROriMO1FYNWLAvCm9NsovqLQRr6YA_bkfEpNEWqE1WblxOq1v3-320ViSvm9RanG1di3chMeBbgOk0T0ng9DLsLYEXQFg8bsOv-qTayNeR6hMyEkPvZPstRTmkGvuJz0vVOSprXqZX0yzc1aaEHi0FpQKJdZwpQZYGfDubzVjUIP0MWZw2eiC2WsDRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای یک آهنگ بلوچی برای یک رهگذر بلوچ در شیراز؛ واکنش جالب این رهگذر به اجرای خواننده
🎶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690318" target="_blank">📅 11:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W02O_9H2M36hWlNA-j9TD7gHougV2NVwKnhWjwesMuYKYENnT1k2eJnMEq2q1_vJOseQCHLJmckIlRL1TSYuSOTF1pHHuzveO6Lj6Q124yowu_DSWQVi7U8L-Rec7DnjjnUoDdeiLexYxfdyHaXIza3qTcgnpvhTiQL5jktMLBq5kGXapTyJxbU14YCYaXc1BlfYa8ySvihfcBMnrhT2OKnfSp6APqERb8UWTXRN2UlxaTP0b5M8msjCSuo_Bj24bGA7sq5tdAKK8kpr9juGNpOA4aqBpGxXzXULbSqxA8bp06jWUCpBmWRdl8_ukh9m_SNVWZyKyOt2NL0RwzTS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/690317" target="_blank">📅 11:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9VBZj6aSy9VrEDtkJhsx52A3iCZoMaza8NrhU8hgAJNpYWDcroXlGG0Rqp_hCCaOwSoa2yFEtzuCG_ByrFakWms2ohqIMz0S1EP0pfIbdHzJ5WvVABKYDHHbMl3vQqzjRjbpobURcNtAXUrGEbVOX_RpOjPuG07pyUhSLGuEth1e7P-88JqNFE2KmwiB6ymj7uYrz7-iJjn3hBYbxV9TIGjUlW7fUMo1xfE-GivNIUOpKs4ATkH3NW8_H58O-7vrlLUpTrN-No3VBNZcFcDMoQDAJEkhBx3RgKtOfZOfvZ5W6KymqJha8zZcU8Inazh9jeXp3hb-LNnYw-8VoOrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه‌های رنگی زیبای آلاداغلار، زنجان
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690316" target="_blank">📅 11:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال به نقل از مقامات: آمریکا در جریان حمله هفته گذشته ایران به اردن، بین ۶۰ تا ۷۰ موشک پاتریوت، بیش از ۱۲ موشک رهگیر تاد و ۲۰ موشک بالستیک شلیک کرد؛ این تقریباً معادل میزان استفاده واشنگتن طی یک هفته کامل در دوره‌های دیگر جنگ بوده
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/690314" target="_blank">📅 11:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/690313" target="_blank">📅 11:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bacb2b39.mp4?token=YvLCb1Y3d3ffIwAjDJNBD2hOjeLcw3Kydhrh2NB0AtIm4tUP6GUJEQbqPSkBhjg-Ba_mvGSalKe847fDOf-jNOZOmt3qvREosk6YHg4kTfT_-BuO2kCw3RLww2htHhbCAXFTtOvt2Fgj6fk2QBsKYVVsgjLXNVADzHbF1tHbNYIqY-6SGEnF6wyCygAcgAendQqnk4osl25Yfh0Y5ILrGhahVwQIXqcYnLyz481YHGG9dQKF_qktwx9M3iA17cfw2kJp2lVbBpkQi2Na8dQHMWq86PxQPSDElV-prg0L9NzIhqIVamXCJMO7xnoBKKvvcWZyIkK4-SM469a93N-Big" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bacb2b39.mp4?token=YvLCb1Y3d3ffIwAjDJNBD2hOjeLcw3Kydhrh2NB0AtIm4tUP6GUJEQbqPSkBhjg-Ba_mvGSalKe847fDOf-jNOZOmt3qvREosk6YHg4kTfT_-BuO2kCw3RLww2htHhbCAXFTtOvt2Fgj6fk2QBsKYVVsgjLXNVADzHbF1tHbNYIqY-6SGEnF6wyCygAcgAendQqnk4osl25Yfh0Y5ILrGhahVwQIXqcYnLyz481YHGG9dQKF_qktwx9M3iA17cfw2kJp2lVbBpkQi2Na8dQHMWq86PxQPSDElV-prg0L9NzIhqIVamXCJMO7xnoBKKvvcWZyIkK4-SM469a93N-Big" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد پلیس بلژیک با زن دست‌بسته
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که در آن یک مأمور پلیس بلژیک هنگام سوار کردن زنی دست‌بسته به ون پلیس، با او برخورد فیزیکی خشن داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/690312" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
افزایش رقم کالابرگ قطعی شد
🔹
رقم جدید و نحوه توزیع این افزایش میان دهک‌ها هنوز مشخص نیست و گزارش‌هایی درباره احتمال اختصاص اعتبار بیشتر به دهک‌های پایین درآمدی مطرح شده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/690311" target="_blank">📅 11:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تحقق آرزوی دیرینه کرجی‌ها/ دیوار زندان رجایی‌شهر تخریب شد
🔹
مهرداد کیانی، شهردار کرج از تخریب دیوار زندان رجایی‌شهر کرج خبر داد و از ادامه مراحل تخریب می‌گوید.
🔹
شهردار کرج می‌افزاید: این زمین وسیع به‌ پارک، فضای سبز، اماکن فرهنگی و... تبدیل می‌شود. این اقدام می‌تواند فضای رفاهی بسیاری ارزشمندی را به شهروندان کرج هدیه بدهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/690310" target="_blank">📅 11:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
طالبان: تحصیل دختران از پایه هفتم به بعد تعلیق شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/690309" target="_blank">📅 10:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
رئیس پلیس ترافیک شهری فراجا: خودروهای فاقد الزامات ایمنی، مجوز فعالیت به عنوان سرویس مدرسه دریافت نخواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690307" target="_blank">📅 10:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جنوب اصفهان/ عملیات انفجار مهمات عمل‌نکرده امروز در محدوده جنوب شهر اصفهان اجرا می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/690305" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a43b876c.mp4?token=km1JMRaYIrfYVMn0oxqkEj4Oebk7oaGsM55KOlbRF9PXiRHLhDBm55adLOiD4Zs-4G6ZNQbH88aZdLZ-VqTPUcx7YCCR3gUukDtXdyH46-T_lyUopfxU9VZG2NYHy5vkMor5Cmd7W5kWtszrLCxFuDn6qBz8N27QYRIkDuy8xFuoeN-pvB1sh2HBHCBxbETGYPEgHYdeAFJyo-0rPNXImV1nI-8m5D94tJXXQo99_GwfnMuZ0ZNYw5ue3fI8JSqPZvSt0UjU23f0JzNUXWhXaFrljwTkwcCWfFh4opyejIsyPtGHuOZA0lJnw9t9j8YdtOlXo2P9fPo-8xm2dJiPL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a43b876c.mp4?token=km1JMRaYIrfYVMn0oxqkEj4Oebk7oaGsM55KOlbRF9PXiRHLhDBm55adLOiD4Zs-4G6ZNQbH88aZdLZ-VqTPUcx7YCCR3gUukDtXdyH46-T_lyUopfxU9VZG2NYHy5vkMor5Cmd7W5kWtszrLCxFuDn6qBz8N27QYRIkDuy8xFuoeN-pvB1sh2HBHCBxbETGYPEgHYdeAFJyo-0rPNXImV1nI-8m5D94tJXXQo99_GwfnMuZ0ZNYw5ue3fI8JSqPZvSt0UjU23f0JzNUXWhXaFrljwTkwcCWfFh4opyejIsyPtGHuOZA0lJnw9t9j8YdtOlXo2P9fPo-8xm2dJiPL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای ساده برای رب خانگی خوش‌رنگ، خوش‌طعم و ماندگار
🥫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/690304" target="_blank">📅 10:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">🌐
سامانه رفاتم بانک رفاه کارگران
🔗
زنجیره تامین مالی تولید
🔹
تقویت روابط پایدار میان تولیدکنندگان و تأمین‌کنندگان با بهره‌گیری از ابزارهای تعهدی در سامانه رفاتم بانک رفاه کارگران
🌍
آدرس سایت:
scf.rb24.ir
✅
مزایا:
🔹
تسهیل و تسریع فرایند مالی سرمایه در گردش بنگاه‌های تولیدی
🔹
تقویت روابط پایدار بین تولیدکننده و تأمین‌کننده
🔹
افزایش شفافیت و نظارت‌پذیری جریان‌های مالی اقتصاد
@refahkhabar
| بانک رفاه‌کارگران</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/690303" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای ونس: خروج آمریکا از معادلات خاورمیانه می‌تواند به بحران جهانی انرژی منجر شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690302" target="_blank">📅 10:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گزارش تصویری شبکه CBS از آسیب موشک‌های ایران به پایگاه‌های آمریکا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/690301" target="_blank">📅 10:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465ed155a1.mp4?token=ntVQ376hzOSeUEME6kvGIm4rIoqU2IETKxD97gOe2AiQ-u4Vy01fZsaMU_dkqKg1T_tSnZ6ZvWjjqTrCvTDpMf50RyfixGfogAix9-j_fW9xyNy2ZUs-OlYKkjOOwELhFsjB4PuL9HZld_6Pc7ll-Wt-f4uWfXG_6dy8rqCf15jTPv8S_5p35CN3W8MLL7wbo1PCrNFEQFxPudtQD0kmF5s1Jdcj02A3ujppZ94-YNHWejCAj8MNwIt9NDk6MeSJLlaZRTktsa8Cd45jlZ_n8syU4Sp5l8zhfidH_IrGq6EMzLzNBFt1qmjMUQcOALUei9zum7tHiRPLzcKqe6QUSxUhSsvcdCo8Bd2rMqjSoy_PIAqddhj39bNvFRSDZeRFdiphApAGW-KBivOq83OcO-uNZFBZJdDAhVT7YMFpZ94OrWYUQmGWBat4cfiU0vBcreqRlK2pSOWAObHQDJ-29dpN8oAnTfdHaJHXzNdroegRWQIRHopliUmduY6cpuuGFP3HEmzqlT9wDW4XVVFBIyYzeIC2pt8QTP7KQFI6LCsBzgkjbEfTVw4PBsKSFOhxYHSQ2jbRucruQ2sLwzsLU2askD3pdF4XqRweCCkDXWyEoN_L9uJs9jSFPQvGIg-PmPl3s7E9nDeEOT4RD8Tegg6p8QYHaq78rE1Icf5qfII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465ed155a1.mp4?token=ntVQ376hzOSeUEME6kvGIm4rIoqU2IETKxD97gOe2AiQ-u4Vy01fZsaMU_dkqKg1T_tSnZ6ZvWjjqTrCvTDpMf50RyfixGfogAix9-j_fW9xyNy2ZUs-OlYKkjOOwELhFsjB4PuL9HZld_6Pc7ll-Wt-f4uWfXG_6dy8rqCf15jTPv8S_5p35CN3W8MLL7wbo1PCrNFEQFxPudtQD0kmF5s1Jdcj02A3ujppZ94-YNHWejCAj8MNwIt9NDk6MeSJLlaZRTktsa8Cd45jlZ_n8syU4Sp5l8zhfidH_IrGq6EMzLzNBFt1qmjMUQcOALUei9zum7tHiRPLzcKqe6QUSxUhSsvcdCo8Bd2rMqjSoy_PIAqddhj39bNvFRSDZeRFdiphApAGW-KBivOq83OcO-uNZFBZJdDAhVT7YMFpZ94OrWYUQmGWBat4cfiU0vBcreqRlK2pSOWAObHQDJ-29dpN8oAnTfdHaJHXzNdroegRWQIRHopliUmduY6cpuuGFP3HEmzqlT9wDW4XVVFBIyYzeIC2pt8QTP7KQFI6LCsBzgkjbEfTVw4PBsKSFOhxYHSQ2jbRucruQ2sLwzsLU2askD3pdF4XqRweCCkDXWyEoN_L9uJs9jSFPQvGIg-PmPl3s7E9nDeEOT4RD8Tegg6p8QYHaq78rE1Icf5qfII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ونس: خروج آمریکا از معادلات خاورمیانه می‌تواند به بحران جهانی انرژی منجر شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/690300" target="_blank">📅 10:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690298">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نتانیاهو از ترس بازداشت، محل فرود هواپیمایش در نیویورک را تغییر داد
🔹
زهران ممدانی، شهردار نیویورک پیش از این اعلام کرده بود که نتانیاهو را بازداشت خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690298" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c7b56713.mp4?token=dkbmz41CbP_59IBqzodokqa5TtQy5x72SgtcKgBx4_O3FL2HKb99oNFIcGV-QoG8PWKKHSewF248ptqS4WwexcMH0hy0MR1I1fl9yTEP6xBRsgYSi38W3mSsiUhTabejumo_DvpCqlvj7CMDThUw_QB89DAUMEgeZt7t0HSy4R5PQT9chIniMUcC4CSYAJsA4taFMEU08aRff_H9b-ZyjuL77dikNHuK5WQF6YbM0koJuVph8sq2gpiSyrd2eKbImkepMk0f3iVhlp9vZEHAqWuLx7EmzKHLL83CEcD_G92YS6BUhm4sj6NmJB2sXS7fQlyImdvVDtd2dTU0EDRToKr2tdUtZroUnQZQdHRmlJBO4kka9TaTbQhLT89HGZaTet-Jzhs0cbR3uiUO-CCApziv2MP3AQddUQZydE39CCHkCeSPmA5IY9jN6TM7Clqidn_8nrTG8GzFJOOzuTQXHjY2oXU47ro2jC_641rTdwqj3I2l5rTevXBwWMRYN3oLiVsNTfzN_e6gOJY90Mmm0fkzQo4GIMRuHBUogVHRpZ8WCC_FmXLRmMuZFzof7g4JW71qrE9T1wszVykAp5skmfpNTRkadSa945a3xdGLOeGm0niWXUVvaAt3JyYU7Up8aLv8yxm9ifV5GkILr3RaZpWYWjAV6VnmfeMSNbnEijc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c7b56713.mp4?token=dkbmz41CbP_59IBqzodokqa5TtQy5x72SgtcKgBx4_O3FL2HKb99oNFIcGV-QoG8PWKKHSewF248ptqS4WwexcMH0hy0MR1I1fl9yTEP6xBRsgYSi38W3mSsiUhTabejumo_DvpCqlvj7CMDThUw_QB89DAUMEgeZt7t0HSy4R5PQT9chIniMUcC4CSYAJsA4taFMEU08aRff_H9b-ZyjuL77dikNHuK5WQF6YbM0koJuVph8sq2gpiSyrd2eKbImkepMk0f3iVhlp9vZEHAqWuLx7EmzKHLL83CEcD_G92YS6BUhm4sj6NmJB2sXS7fQlyImdvVDtd2dTU0EDRToKr2tdUtZroUnQZQdHRmlJBO4kka9TaTbQhLT89HGZaTet-Jzhs0cbR3uiUO-CCApziv2MP3AQddUQZydE39CCHkCeSPmA5IY9jN6TM7Clqidn_8nrTG8GzFJOOzuTQXHjY2oXU47ro2jC_641rTdwqj3I2l5rTevXBwWMRYN3oLiVsNTfzN_e6gOJY90Mmm0fkzQo4GIMRuHBUogVHRpZ8WCC_FmXLRmMuZFzof7g4JW71qrE9T1wszVykAp5skmfpNTRkadSa945a3xdGLOeGm0niWXUVvaAt3JyYU7Up8aLv8yxm9ifV5GkILr3RaZpWYWjAV6VnmfeMSNbnEijc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حالا که داره فصل پرتقال میاد، بیا یک پاستیل خوشمزه و ضدسرماخوردگی درست کنیم
🍊
😋
مواد لازم:
🔹
پرتقال: ۲ عدد
🔹
نارنگی: ۲ عدد
🔹
لیموترش: ۱ عدد
🔹
پودر ژلاتین: ۴ قاشق غذاخوری
🔹
پودر زنجبیل: ۱ قاشق چای‌خوری
🔹
عسل: ۱ قاشق چای‌خوری
🔹
آب: یک‌سوم لیوان #آشپزی
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/690297" target="_blank">📅 10:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بازنشر خاطره قاضی‌پور از سالم ماندن بعد از پریدنش از هلیکوپتر به مناسبت سالم ماندن خلبان آمریکایی پس از برخورد با سرعت ۱۶۰ کیلومتر بر ساعت به زمین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690296" target="_blank">📅 09:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d09fabd3c.mp4?token=oxMxJuf8s51cK222dz7AOT3l04PFO6HH8tCe7S6Tmm-kVZN_OzrtPTOVF1NMsRcVeuEl_9t9voIKv6X4sE2ME2LHDQJ71dmSi5Hx2raDuUNyvIz6p-J1G9DFZdJjTC7ESp9BErY5Dg_B35J4XOfE4XjsukhFvTcBnnSHOc7lBGG4-RTW59ySv85QEKyNiXAT7yNgDSwO7YxfYcpji6f95DmAFW1HA7cdRWVK8J-hl71VUFyZV_45XOACq3SsghietTWa-KzrupFMTJI0c0mM_ZmMxSsEqjNO5jfZWBzMP8LJvxxzY2ft7fQ8LPqveHzKCksgPV8IODHKtNNDrbTUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d09fabd3c.mp4?token=oxMxJuf8s51cK222dz7AOT3l04PFO6HH8tCe7S6Tmm-kVZN_OzrtPTOVF1NMsRcVeuEl_9t9voIKv6X4sE2ME2LHDQJ71dmSi5Hx2raDuUNyvIz6p-J1G9DFZdJjTC7ESp9BErY5Dg_B35J4XOfE4XjsukhFvTcBnnSHOc7lBGG4-RTW59ySv85QEKyNiXAT7yNgDSwO7YxfYcpji6f95DmAFW1HA7cdRWVK8J-hl71VUFyZV_45XOACq3SsghietTWa-KzrupFMTJI0c0mM_ZmMxSsEqjNO5jfZWBzMP8LJvxxzY2ft7fQ8LPqveHzKCksgPV8IODHKtNNDrbTUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سامانه «علاج» برای شناسایی و پیگیری «خائنان خارج‌نشین» شروع به کار کرده
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/690295" target="_blank">📅 09:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErZX39sBwncgjLxlVqHWp0-Vw4ijqeWuqwpRX_ZFcLca1zsYhj5n4AG3xiV_3C1pQvteKsbSGe78NQxJSqFUnFFGnzigmuTP5XTEI_3SZINKnkwdSwcuQ4dXZ5p2RtKYyS0J-CciufKMMjG-EbxGVrFXvq2xaTuXidY211IVvpQ7__n9S5hnk_WFSFKhR32AWOZXXxk1J1Ze-P36s5rSebxy5PSMn04X-hi-YiVwBGAteDf2Pt7Q50Ai6pCYrXCW0FGt6rvQX2SAl8TgmVse5zreDOZWRaqRmawj1nIeNMM5Xc3Wa84mgR1T5jl4Ddip5_Gi9RB6H_yodVV8WpY_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامانه بارشی جدید از شنبه وارد کشور می‌شود؛ تشدید بارش‌ها در شمال‌غرب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690293" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e328e93b.mp4?token=Sd3HQAKF65k34ctHNXsORDrDojzvFPGDzOfMnnozoQoIuyjrdrsHZiCfXKE_xB2mREqR1b_QRjX3CZukFbvY0w7BdBIfp7qmBvVwy-95srDaN03eOAhiY4ASrFdH3UfcBs_XQEjIXkLpI0qKDkUx--hsXIDQngdD7UCon8YqUWGxkoSM8xqbSp2vE4_oXZBHJEiTEL8fq0iZtzR2qLvy7qtg6LesM0wN1XABO4w6yIMP_O5RTvHjIj7bqtSejKUGHu8chlTypaUPCL0d-CT0qIX2Vo3LXX8dk0iEYk_hL5xKo6YSYeOZ7x_fra1lcwh1x-mbip8JPCVVqgrgsgf6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e328e93b.mp4?token=Sd3HQAKF65k34ctHNXsORDrDojzvFPGDzOfMnnozoQoIuyjrdrsHZiCfXKE_xB2mREqR1b_QRjX3CZukFbvY0w7BdBIfp7qmBvVwy-95srDaN03eOAhiY4ASrFdH3UfcBs_XQEjIXkLpI0qKDkUx--hsXIDQngdD7UCon8YqUWGxkoSM8xqbSp2vE4_oXZBHJEiTEL8fq0iZtzR2qLvy7qtg6LesM0wN1XABO4w6yIMP_O5RTvHjIj7bqtSejKUGHu8chlTypaUPCL0d-CT0qIX2Vo3LXX8dk0iEYk_hL5xKo6YSYeOZ7x_fra1lcwh1x-mbip8JPCVVqgrgsgf6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازنشر خاطره قاضی‌پور از سالم ماندن بعد از پریدنش از هلیکوپتر به مناسبت سالم ماندن خلبان آمریکایی پس از برخورد با سرعت ۱۶۰ کیلومتر بر ساعت به زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690291" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqm9bDZsZB95EOjiP9tj0Ykp0wnRmqPsdIyOfsZmy_zY40NeOSI-7y8IIO0PEDoaMOBuPQlffQsz7j8P8_vicQMBcDxMGjeY_KYgYnj73UdU4WkcIswrT2AFvGBvA7tjdPY1CiYEXEeIU114F_e5fYZAYPjs8YR19MIdP2ybS1b1BG3vYjbxa-BlpCl77igA_WAS23jGLmwqGEP7UIdwQs1Ps93JTxJlmTGnnrwBZFawpyPyb5A3Fj5co7_JpW18eNUZzStm9n514FtO_8g50Nx0EJo1Rsp4dcrBsdUmdDmUo5Yw93_VxAchP6aOhxOdWEuxGsFf8SaFAjLdbQtwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای کاربردی اکسل که هم سرعت رو بالا می‌بره و هم کار رو راحت‌تر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/690289" target="_blank">📅 09:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
خانواده شهید رئیسی: اخبار مربوط به فوت مادر شهید که در فضای مجازی منتشر شده صحت ندارد
🔹
در این زمینه اقدام قضایی خواهیم کرد تا این خبرسازی‌ها صورت نگیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690288" target="_blank">📅 09:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تیم ملی بسکتبال با پیروزی مقابل بحرین به جمع چهار تیم برتر بیستمین دوره بازی‌های آسیایی، راه یافت
۷۴
🇮🇷
۲۱ | ۲۲ | ۱۷ | ۱۴
۶۹
🇧🇭
۱۷ | ۱۷ | ۲۲ | ۱۳
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/690287" target="_blank">📅 09:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دادستان جاسک: از یازدهم هر ماه به مدت ۲۰ روز، سهمیه ۴۰ لیتر از کارت آزاد جایگاه‌ها برای وسایل نقلیه اختصاص می‌یابد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/690286" target="_blank">📅 09:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌ صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌ از دیگری به‌ سراغ او می‌آیند
🔹
رسانه‌های خبری از سرنگونی جنگنده F۱۵ عربستان توسط نیروهای ارتش یمن (انصارالله) خبر دادند
🇮🇷
…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690285" target="_blank">📅 09:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رشد بی‌سابقه ثروت ترامپ در دوران ریاست جمهوری/ فوربس: بعد از بازگشت او به کاخ سفید ثروتش دو میلیارد و ۷۰۰ میلیون دلار افزایش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690284" target="_blank">📅 09:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFPbbROfkpijKPe6lQuoAFZ8FbUv_cnOVvkz3u3x_Yk7H1DYe9jVGbEjjqiRuA7D_Tknb5tA8Afk_S2V6dWc23hgbFUsONw9HfWy0kPPjL0QshpJ8Z7ec8QpraZuhjdXyYQZKOQOIFkB79XtljyyHtXMwONytoDiQ0HC_0Vk-15I17n4HDaOnFHTz7I3boEQJ489TSBssqeVYKHJbGhEuVTWPsg3-yD-MxXTquw1pLzizDh5LPiH8uWl8W6V1nkiq4xyBFQwH_WMU2KGX77-cOgwrnBFVHQ-8sYVXhREynuycDt_6rLBXBARN7e_ueUsOxCgqCRKgUNQTnQc0AkaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر یک جوری هست که اگر تفنگ روی دوش اینها نبود، هر آن فکر میکردم جنگ بدر در زمان رسول‌الله می‌باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690281" target="_blank">📅 08:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nG80eH7VxCM_dx5SMsEpwF_Y_L5idrJuPC-4DUW2hzbtduwD3Xv4z17d-eyBgUQjAOCrjxpBW01FtmMM2uyZz_U4G1hFOuaox2pCmg-EX-ixjtFp_rK6URSzKBIRCr5uDCxCvP0J11iI2BReMblgqMmL6O9Kkn48KR6q7P19McM6nb5Y_qofZtqti9CU0Mok5m2ILpqd6nUDwn3kfC9n_Tx6s3C6Ojc8vpxRPgLL6Xwy7kfOf3diSQoJ9ik2NBYkfsDDdSyT441dmg4x4hi3hHGLewlJ2QgwHhxLF2q9hyry3PCuw1aYSqCc5906f_GfuoArwpzMbr8aP-Sn2QUAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر قسمت از خونه چه رایحه‌ای مناسبه؟
جدول راهنمای انتخاب بوی ایده‌آل
🌺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690279" target="_blank">📅 08:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690278">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
سپاه: بامداد امروز پنجاه‌ودومین پهپاد MQ-9 ارتش آمریکا را در جزیره قشم رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/690278" target="_blank">📅 08:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690277">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVslP7zeiVHRzqUu5DmDWhbSxALLhAtRrO5cWUrE5L_3qQ2HB2tYZgu5zzvl7bdjqWLR8d8qZUg8L7wVUnzYyjhC6UdWIuS_savegBqWFFpC1tdjW6J6ph-0moZvbKe-CYFXQ9Tlawi8fUJYCsCSzQ_xeeMhePpe5R_xtsaCGH6KrM7yn8mJWybVtObMXFn0HDBvbI4ZGfEi5rJpL_fWqPiybLbF8iVXPXsgsddIG92Vd0sPmEfcf2SCUAqBJFgItHuTmcy_TwZ481vx0Mp1DksZbipyIfPj8mkdW9-6_ymJQ5bqSG_our76wJCH2gSV9Gkd6rM2xUr9EP1aK4cK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌ صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌ از دیگری به‌ سراغ او می‌آیند
🔹
رسانه‌های خبری از سرنگونی جنگنده F۱۵ عربستان توسط نیروهای ارتش یمن (انصارالله) خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/690277" target="_blank">📅 08:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690276">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT5ByJHFCgN7EpIzgvIui5CRve_PlHi0gFqrdaK4gACRHbSfS3m5-SskRlqD5jKNLxu645vef1J8R3Rr_AqZBTfmdklkHWho1hzmQZQSve4kj7xBlpCW33xBql9TNvbw9B3zfX3mwB62qE92H8bAje5PIcFCkHELVxP04QBh4sMKBgI4kfoJW40vQAPv4Ac4tzXbipgf4GF9txerUUCXj1Xaxu5QrJK0-3dIx64icwZNLaH-uyA9xt6Zv7yRDwGdH18mzXNTvF2j72ZXTodvQjJHxUU2PXcAx9CtjPmI7gwe1E1gv6saGZxHE5tFW6IAoCIo_U1q0Y7BmxvdfOU5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایندگان آمریکا برای سومین‌بار با طرح استیضاح ترامپ مخالفت کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/690276" target="_blank">📅 08:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr2ea-y1Yaa8niEj93Sq9TeaB6zLDMqIAz1UKaAucRMZvyl3yS75Gr93swUykl3VlGOH1z1uyjVJ2yImq6xU3qEJ_8DEQyWXXs2Bgvp3xY01-HZu1KWqk8uXNMIbiO0A2abXbkwPsJ26z1gloqtnH13y2NiVYhNrRpJGAZZ9S9cAjbCkz1PrVlFh7zyqbtl-FAsFYaqtil8Xkmd0p5-Vy5PL_pm80JjM4iTHafGevijZUR-dqjvLCVtCzf_d7T65WzlPO8x9OhqdHudKLeOSwDalWHFR4GaU_hKzvyZehk5u6V4ldPPbOvEPxKdNbwr0a1SQBdgDWh0tfHfalS7BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVqIU-GnJuikR7mxggXa6bisVE7V5zvHX7G5VoQToRXZ_W4aoc4u3NWI1odiFkPmvvt96xbqOP7Oo_MEtEbgfvgVaSApU1pWS3bxKB_p9SAGs_MwZf73KUzQpIktfQcr0sL-OJnPpg2rQDYh2g1XB0L_qB6KVwUbVuWvWnZnp7B7Fxc_lFbS9E1VNgO0By9i0-yaZgo4g8YRAIdriINGUo2SLlw4NVJmOi9wf6KDzM-deQHo26XdlFaN4zlbIi7FGbIN80cIcfY32juveA8huMlT4xaZvqQIq4WUGixPDlTkYplWq4nrVjGo2tvK1T9v1plqoiVR-JySrCbx0YPaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_RcrKfxs6dMQkOcYMRRy0K8mRVGg676GjrNqDMG2jfE5cFGctAXw7H4UeDlLTwMT83q-enJSjB0oKD-oNSw87pb_kkQtQFEMc5ZUDCHyaCbH9XYow2uzTfr0NVaNP0-tiSGuriPweD39cWkDBH2sY06pkuh2uyYmISmkKwTDimgX25te_iiQA46SIOZ48aANF819kg1ujA4r24zcASdGxM8byqsowOD_o8TEdSVEKX9kBdrayxPSHw093Ok4MLTJKp4f64ZuCZEH4sNspJLE0l_eZezVUOnzSy2DqI0zZ6XQb9JcHwGf1TRXmvX6ZIFKVaOevlx7kpPNwiw4cw3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htWIKIMm2Cce2wfveL5WTV8Tm7tKCkUxVhTnGSWMN-Mp8CRaBqtJiMzbTxnNVGL3nQ1nW_6WOZjos13vNYwOcHn7diEcEBWbq0uxUC80qxy2fi5bJ6aYfU-HqJ1FzGBHKuTSRX2NlpR61Vsg9VfOp3S-z-xMyp9YQA5U0hMcF8GwFDJyYmT0-d3Xz2GfRyI2vjDIpfiXipi_FxXOEoteHLcvkteVbzDWFxozLz0rps7rWzUH7S4rW6autdaLoigkhYbMR_L-8ONPW4PK5BGZxVsbUiTothnLpRdAnQ84zejg1SIsSFcKPQNyXVm288SK7_PjENPtnKxUV9svYRylKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شبکه سی‌بی‌اس آمریکا برای اولین بار تصاویری از خسارات وارد شده به پایگاه‌های آمریکا در غرب آسیا را منتشر کرد
🔹
این تصاویر که توسط اعضای ناشناس ارتش آمریکا برای سی‌بی‌اس ارسال شده‌اند، ساختمان‌ها، هواپیماها و تجهیزات تخریب‌ شده در پایگاه‌های این کشور در عربستان و کویت را نشان می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/690272" target="_blank">📅 08:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد و تا پایان مهر قابل استفاده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/690271" target="_blank">📅 08:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_5FWdQkPsYwPoS7I9avrLkCJp2MPQh-1jz_kdADPCORGwk9Hjm1HMi2iez78kaSvKsSzlmWwCdnFX8wUo73-fZGXPAZOibLfCY0kMoSpfX2KXOYO3S8sfIuWUQCK8s4PATpbdarL1bOWuvK_K-yCGQQRYSdzjYdY-BfGoQ9iNnFyFLl4TZY5PHhHfuLzk5Rr6gJ940mHssrNdVvEAMwZAadhkbfwtyPaxFL2L1FJuQ1HONWep8TiFKiTnFOJBz2m3hTfk4lsh9J20j_r5vUqIrdQJ0WA3AGrJNG5oVeTQsS-UxuWJ2HF830z80VX3VB8LiAVae1SP-zhoePMdpVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۵ شهریور ماه
۴ ربیع‌الثانی ۱۴۴۸
۱۶ سپتامبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/690270" target="_blank">📅 08:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHUkTS1k6LXOGXjcJvl7_XNBzBhaRlpPkBj_yvDgWv60j0u-8qQIORHL-sAu4DyvYVUxTsZo6VW4csnAymLOUfHjgtYsQeZ_fNVa_ZARF-ubuwopFsUllPCFdmwSwQ3dx_mz7nwQksynGTqfcjSRZqWzZGE4y0Z0RsbJ5QZYrINjVqMP3nEDHZvA0Mc-Ki1va0twYsUsi54JgFBdtyUH7EjbcufV2YXBw3-GppdHMYKhx02CWTAtPH9DUg1yfqK8JTPCBm88Lxr6awmCQUufqKE3Gm1TWDtO22F8_p3DIMdtUkvsGY6S94H2k0kgv90i-jkkNfreH6OWLDyRCUMrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
این بار خریدتون،
یک هدیه هم داره!
🤩
🎊
جشنواره پُرهدیه مایدا شروع شد
🎊
با خرید طلا،
چه نقدی، چه اقساطی،
یک هدیه منتظر شماست.
😍
✨️
❌️
برای مدت محدود
❌️
جزئیات جشنواره در
👇🏻
پیام پین‌شده کانال مایدا
https://t.me/maydajewelry
راه ارتباطی:
@maydajewelryam</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/690268" target="_blank">📅 00:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9oeei8FQ4oTAYFsOhViJ-Z_CteSn8RrCY18gnERlM7w0GJxHkV_g82Tq1WV5jfBN9LiTU_DbW0PTb6lsCLd6QwuXglGyBsPfL8dfBPrlipiEvpnfpr7gETwLVV5qkP1kekBStiquDTuqFWbsVpJ06xTR_j_ivt1c9SEVMqOqxBFYOrbDHkfx1IXhHn006a6V95ygcjQIxG0OhWulkmW-exo600wA3SW_V5GcsxV-c7tPrYavyA7-0Pv5nDjFjbeUUN4gFrSHsPbOTW4mjvxRKJlq4IyifmxHoTjQfmxIBKC6Do-ovEZ7gen4WmQ7gUXbSfu1rfri8TWV6lzqhYaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
فشارسنج سخنگو فارسی؛ اندازه‌گیری فشار، راحت و دقیق!
❤️
مناسب سالمندان و افرادی که نیاز به کنترل منظم فشار خون دارن
🔊
اعلام نتیجه به زبان فارسی
📊
اندازه‌گیری فشار خون و ضربان قلب
🏠
مناسب استفاده در منزل
🔥
قیمت ویژه: فقط
1,990,000 تومان
برای اطلاع از جزئیات و خرید
👇
خرید از سایت
👇
https://memarket24.ir/product/brief/63656/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/690267" target="_blank">📅 00:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc10d9838.mp4?token=R6ozjDKSjWA6tbt6Ta1G0B3jxWR6BQL_mecfwFtECmRX7QnRDNM20pwHzZFNoh53UOatZS5ehJIPGYaqlUGUNzBaAv0NC-ovIfUvfiSnSm9BlJ-z5SApx84vvHcfjzdi-8zI03cvs5-J2BFqtOWgbqIjC_-nxQp4_NzfNsz96Me4a0N7EJ-2cFp7S0MWkEsy9IQCt3vuRbbk2Gg5C1ouUcltyvTyadqhsPFJ4Tru1f4eFOVOidXyC0X9An298nEY_njEjwGKzDHmmck8MreV7Ry5Q59ryR3s7vpPkqhXJVe6N-P5rEuYXE5AcShbV-zum5ViI4mZusM9TLdYeRpqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc10d9838.mp4?token=R6ozjDKSjWA6tbt6Ta1G0B3jxWR6BQL_mecfwFtECmRX7QnRDNM20pwHzZFNoh53UOatZS5ehJIPGYaqlUGUNzBaAv0NC-ovIfUvfiSnSm9BlJ-z5SApx84vvHcfjzdi-8zI03cvs5-J2BFqtOWgbqIjC_-nxQp4_NzfNsz96Me4a0N7EJ-2cFp7S0MWkEsy9IQCt3vuRbbk2Gg5C1ouUcltyvTyadqhsPFJ4Tru1f4eFOVOidXyC0X9An298nEY_njEjwGKzDHmmck8MreV7Ry5Q59ryR3s7vpPkqhXJVe6N-P5rEuYXE5AcShbV-zum5ViI4mZusM9TLdYeRpqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلینکن: ترامپ، آمریکا را در موقعیت بسیار دشواری قرار داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/690266" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d71a461.mp4?token=tKcVCho_k_Omxlol5Kg9CksqMWjU8CMPwW58__m8dtxNitKCRja27iLV8m2bbEPNmcTgepqnmY_vip7nKqrM_ciTK5aZOXwu4DyLKrHE68RUzgjcxKpdsvExzFvYFD93TecsZ-mbijl8CZn848vslRE3jNkVwIR1jcGq54ul5VhoJMRMa5mWjAQEPhLMPCpWDnG48n1ZMmJfYwW8jgW_bWM-TorhJCkfxdhIHTcxSlXvGzE7Rq3Y26LqCJLSDmoURkhcbozQNOb3qRwimYV1S_SAqdHF84jFRkDwDergNoKH-hlL_0KW9ar_Icq09IwP0qpJ7sOYzFUr8YUOlJU95Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d71a461.mp4?token=tKcVCho_k_Omxlol5Kg9CksqMWjU8CMPwW58__m8dtxNitKCRja27iLV8m2bbEPNmcTgepqnmY_vip7nKqrM_ciTK5aZOXwu4DyLKrHE68RUzgjcxKpdsvExzFvYFD93TecsZ-mbijl8CZn848vslRE3jNkVwIR1jcGq54ul5VhoJMRMa5mWjAQEPhLMPCpWDnG48n1ZMmJfYwW8jgW_bWM-TorhJCkfxdhIHTcxSlXvGzE7Rq3Y26LqCJLSDmoURkhcbozQNOb3qRwimYV1S_SAqdHF84jFRkDwDergNoKH-hlL_0KW9ar_Icq09IwP0qpJ7sOYzFUr8YUOlJU95Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنتونی بلینکن، وزیر خارجه پیشین آمریکا: جنگ ایران می‌تواند و باید فردا تمام شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/690263" target="_blank">📅 00:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKvXcDbsFxeoShi2vdbBvW66QJjsPBf4bEelh1Li1nBfxcN50YUX1ZHATceohkXZC3hrRR9cW23W8sGK3cmE3ZHVa36OD-Zm6O70hVRW1IueZbIren_CmuJsyHFkVXxBtLWhs2Q1_cm4FsL-O2ogFWEpFoBmo5N9kJXT2ok___2a6atNoeLCuHiNSEayBhuGscWEcXSnrcZIf4-ze7PYX_KZSMBWO2XHatOMh49JPcmU_pM0RnD4Z0NO3deavW23VAt2cvOqApo36iTrg7T_SUBHvipoBwy96KbZPVAvZ7Okg3246LI7HcQsmYrPXNT38xFItJ-NH9qpLRQ8U28cqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاک ۱۶۳ خودروی متخلف سوخت‌گیری در رودان منتشر شد
🔹
این خودروها طی ۴۸ ساعت گذشته بیش از یک‌بار در جایگاه‌های سوخت این شهرستان اقدام به سوخت‌گیری کرده‌اند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/690262" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690260">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=Za3kDEBmCmyIJgheDxw8Lu1UKNTGRYwRWRY7KhZMRMFnRbXlUSNLrAtRNgjjul6V-Fy7peYTK9PgWDbWscmkhVLj2uN518wAkeh5pk2qVbvn1bllEfQVaxuZehKePT9kmdB6rOmNQS2adTiRMgc45HLpqyoTlSSze2EOxagYadzqf5dNaetkxgasEwCetVZ4O3qGyU9Vs-idxtU3nutqkEGXRcv2rSLmZLgwLAdWf-OvA0GbxEN32sHsnhvGrcIyZcb_PB3W6KMV8SQm96kJWI2HAbJYAWLWDM_fbcb93KzfFfSyJKUDbDuSTICPCVb_iUCcV_0bsOAo5GmilOQToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=Za3kDEBmCmyIJgheDxw8Lu1UKNTGRYwRWRY7KhZMRMFnRbXlUSNLrAtRNgjjul6V-Fy7peYTK9PgWDbWscmkhVLj2uN518wAkeh5pk2qVbvn1bllEfQVaxuZehKePT9kmdB6rOmNQS2adTiRMgc45HLpqyoTlSSze2EOxagYadzqf5dNaetkxgasEwCetVZ4O3qGyU9Vs-idxtU3nutqkEGXRcv2rSLmZLgwLAdWf-OvA0GbxEN32sHsnhvGrcIyZcb_PB3W6KMV8SQm96kJWI2HAbJYAWLWDM_fbcb93KzfFfSyJKUDbDuSTICPCVb_iUCcV_0bsOAo5GmilOQToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادل فردوسی‌پور: قلعه‌نویی درخواست پرداخت ماهانه ۱۵ میلیارد کرده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/690260" target="_blank">📅 00:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690259">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز جانمانید
🔹
🔹
تغییر مهم در جنگ ایران و آمریکا؛ غافلگیری بزرگ در راه است
👇
khabarfoori.com/fa/tiny/news-3245496
🔹
نشست محرمانه فرماندهان نظامی آمریکا، اسرائیل و کشورهای عربی درباره ایران
👇
khabarfoori.com/fa/tiny/news-3245498
🔹
بی‌حجاب شدن ناگهانی یک خانم روی آنتن زنده شبکه خبر/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3245521
🔹
هویت خلبان جنگنده سرنگون‌شده آمریکایی در خاک ایران افشا شد | جاناتان بات یا همان آلفا کیست؟
👇
khabarfoori.com/fa/tiny/news-3245456
🔹
هزینه بنزین خودروهای نوشماره چقدر است؟
👇
khabarfoori.com/fa/tiny/news-3245374
🔹
خبرهای جذاب را در خبرفوری بخوانید و ببینید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/690259" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690258">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/690258" target="_blank">📅 00:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690257">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOJ5aGY47qFhj675YnppL3X39DNX0jit10KZFP-CwnlvffFbQJd7mAA5nwOe3fLE-hZ7GAIa83TMUH6sFUsL_AtmtoMTxeOVZCULDCqpDh1jJLdT_ORTnXJu1Ghzt7CoiifIXwOprdxgGJKgRzAWpqBZkHs3_8Qe1Hc1QDu8lHd2xL47yjQmj-Sx-IeQu7mpZHbWvTTiGMXmGLym2cqYBtQ8USuI8-2RAiLxqSkPDMJb3nruI7d5b7n_nj8S2MUWrmnTNXFyycUyQjiac6KKP6iqUL5WrQyEilv2unFM7QSUiwevAN1j_TCsws1ik8r1Y4hrUbF8yXD9vwFz99akZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690257" target="_blank">📅 00:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
نماینده بریتانیا در جلسه شورای امنیت درباره بحران یمن: نمی‌توان یک مسیر حیاتی تجارت جهانی مانند باب‌المندب را در معرض خطر قرار داد. حوثی‌ها مسئول تشدید تنش‌ها در یمن هستند و این اقدامات با حمایت ایران صورت می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/690256" target="_blank">📅 23:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
معاون ترامپ: جنگ چند ماه دیگر وارد مرحله‌ای کاملاً متفاوت خواهد شد
جی‌دی ونس در مصاحبه با نیویورک پست:
🔹
ما نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم ترامپ درست می‌گوید که این درگیری چند ماه دیگر وارد مرحله‌ای کاملاً متفاوت خواهد شد.
🔹
من قطعاً درک می‌کنم که مردم آمریکا تا حدی بی‌تاب شده‌اند، اما اساساً آنچه اکنون در جریان است اینکه ایالات متحده در عملیات تهاجمی درگیر نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/690255" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
حملات موشکی یمن به جنوب عربستان
🔹
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/690254" target="_blank">📅 23:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhFX2DDW05wXbjtJSyXRoqs-KGyhkIsbGvrNzd9XQGTk8H5Pk0LSO2uHD1CTIeItvmEuv7eqxL_6MXss-YZUbyveFid8hrJcWurikjOPEB9_t6JPLVCI1i0E004eH03AL-sfeVbjk8v_XQWi4vSQSo5tcbSuxStdMZA6o9pqXTT7EFxEbXkXivOCc08-4miuqysG7j8DbNa0UoCgav1ikg6K3omo8Udli-ObApgXSzIfkN0JlPZE0FIy8NeCdevXf9YC6VCCuHu-NVDLxz8ObEF8ofM0q04SD7wpI_iTjxyTPvOlrBScsDNKVlFSiHUOPICNNW6eWdtpOzqcX95KOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی زیبا از حمام تاریخی کردشت، جلفا
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/690253" target="_blank">📅 23:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: هیچ صحبتی از غیرحضوری بودن مدارس نیست
عبدالوحید فیاضی، عضو کمیسیون آموزش در
#گفتگو
با خبرفوری:
🔹
مدارس باید به‌ صورت حضوری افتتاح شوند و در حال حاضر هیچ صحبتی از غیرحضوری بودن مدارس مطرح نیست، اصل بر حضور دانش‌آموزان در مدارس است.
🔹
در شرایط فعلی، مدارس ۱۰۰ درصد حضوری است اما تصمیم‌گیری درباره نحوه فعالیت آن‌ها در آینده، متناسب با شرایط روز انجام خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/690252" target="_blank">📅 23:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei7433i9V_WfWrLQY40gPclMtD5_iWFz8jXavfhwfYVsq5hUX8y6dKOyX1_uwz-ivL3y_J-szh2nSgHh0W4tB7nrA7N616DfpxuwnKTaTf9Hiq7tVcqBX07h_5vt65mvTAQOkZTWC4fesyqvfHLxhYtgWCiSHHCjWngaSlZ0YO79uc9QyY6Xa_Rxs0812dhB1_Ls75SoP9Ki2TnSpmt9c6EJj0U0liGAbmwmTT5HrSAhXtGW2xkZjMc8OSFiVKOCPXQU8CvvOZQkwCHSHVosHzf8ZZr-lRL1Zcj2WWLZIjcj6CmQcQF6kFlODre7P9U2QWIDVPmzF0MbR8BLtoSgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای عراقی: عربستان می‌گه حوثی‌ها کعبه رو هدف قرار می‌دن نه تاسیسات نفت
🔹
خب پس چرا قیمت نفت بالا رفته؟ چیکار کردن لوله‌های نفت رو توی حرم مکه گذاشتن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/690251" target="_blank">📅 23:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLpwwNqoPp3uZ_EPKGFTreVbZd0KAode7OHT-QqUAeRk9K1JUX1nrLkMKwbvvmhNS8cLGx2SclXggIBHJbhCL_L0xOyYvJa6Xj9KB_neoKFmF3IbrH2RdLkMna5eiz5VHlt4CrhyAAJa5p7fCjkUCTFEn3Nju0ze7Xyv9MkKPDCR7-LeQ_8O57SoSPOT_jHyTm4RdueV8gcd71d5uK-MCJtlsvUtcvMPhYb-vj_jBOTkRvY-LsT9sRkxn4jROcX2sQsQZ9NebFv-pWea5Vwxuuv0FopLn9PZLYm18gjsGB_SGewR1CtiPMfDRw6XnY4SF4_1JLRLzlrjByXit0VXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون، راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه شهریورماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و بررسی شماره‌های قابل ارائه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/690250" target="_blank">📅 23:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مقایسه وضعیت روستاهای اطراف شهر نبطیه قبل و پس از اشغال توسط ارتش اسرائیل
🔹
وضعیت تپه علی‌الطاهر نیز پس از انهدام تونل‌های در تصاویر واضح است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/690249" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566a2e474c.mp4?token=RToxW8G06G7QTbyZcVIWCXicwrBhA-GY1_-qKO1anVDiWC7O8XpB5lNvQWEgf8LZqM2qQrQQqr0XfB7w9AfXbiS__tMWXJTl2Nm94C2IvotXfAEbhx2z5Q_p78i8vPevXRKF6fI9BBawoklJkooH238hQqt1PSvPWZjom__sP_gyB6_SIVMn3Aquj1QxnYQEW5l3zc7EAvLrwTaFsPppEuz1py1DAcQB65FEuXjW5wDbUS2_dT1oiK1OYhR-eFfK8ot2R5p8LuTCR9ax6K-vfJ6dhZiQvd5LFzBoH5tPeDT7_YzOFgSjk-8xOBGm-G1amypsg5Tn1rEncKhxc9JAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566a2e474c.mp4?token=RToxW8G06G7QTbyZcVIWCXicwrBhA-GY1_-qKO1anVDiWC7O8XpB5lNvQWEgf8LZqM2qQrQQqr0XfB7w9AfXbiS__tMWXJTl2Nm94C2IvotXfAEbhx2z5Q_p78i8vPevXRKF6fI9BBawoklJkooH238hQqt1PSvPWZjom__sP_gyB6_SIVMn3Aquj1QxnYQEW5l3zc7EAvLrwTaFsPppEuz1py1DAcQB65FEuXjW5wDbUS2_dT1oiK1OYhR-eFfK8ot2R5p8LuTCR9ax6K-vfJ6dhZiQvd5LFzBoH5tPeDT7_YzOFgSjk-8xOBGm-G1amypsg5Tn1rEncKhxc9JAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوران طلایی نوکیا؛ زمانی که هر ایده‌ای می‌تونست تبدیل به یک گوشی متفاوت بشه
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/690248" target="_blank">📅 23:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955fbe362f.mp4?token=t7ugcdHvL09KlW8NiIUPoXc8deumSWVrKuKZZd3ChqjcLS8Y95lozTO_6UlSr2lTUhw_vjXk5KivUz1ECVuG7ohtze1m19ChzZ9qE4MmTapWGizfWQonweHIagAQXGo9UAPw6Pd4cdbzfWkpP192kfOd0Sz7O5WhYPgu8Ut3iZIv4DYhBFDG3Cv24WsR-LLFaiO0XUdsRJUAw_CgQ69IliUAMZlI-RGXzpuGpPfoHy0H49_Hcop0d_bvsUMAKcpNUvMVWI-I1CO0A7aqHwxJmEXBq09bS1p5VjXwppYn_pAEk3YgZ5skmQbQnYzX4U0pXnAXgFLaGZBUE47GAXh9Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955fbe362f.mp4?token=t7ugcdHvL09KlW8NiIUPoXc8deumSWVrKuKZZd3ChqjcLS8Y95lozTO_6UlSr2lTUhw_vjXk5KivUz1ECVuG7ohtze1m19ChzZ9qE4MmTapWGizfWQonweHIagAQXGo9UAPw6Pd4cdbzfWkpP192kfOd0Sz7O5WhYPgu8Ut3iZIv4DYhBFDG3Cv24WsR-LLFaiO0XUdsRJUAw_CgQ69IliUAMZlI-RGXzpuGpPfoHy0H49_Hcop0d_bvsUMAKcpNUvMVWI-I1CO0A7aqHwxJmEXBq09bS1p5VjXwppYn_pAEk3YgZ5skmQbQnYzX4U0pXnAXgFLaGZBUE47GAXh9Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاهبرداری از پزشک سابق استقلال؛ پیش از سفر به عربستان با استقلال ۳ نفر با یک وکالت‌نامه تمام زندگی‌ام را نابود کردند!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/690246" target="_blank">📅 23:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGOdyEvkGe9JIRsWQ5Lhv9PtYTYdvSAoTPjl69LpUCCWnNBCYYdJh58Yx3v06AZTDPn1R5G3QHmli2j1vNGcoMmr1TmSpKWQkzaGt4tNvYJRJC9hFw_jQ1v0cZKCXgSb-36PM0T2Qt1j4gLiWByXm1IaTTDB9Wl2rHYC4u2JFVkMa43Fo5nAaDHGH5MvSAs6w25Zw-s9oFB640Z9nWpehHaY4_jq0vXTFBGwStoqwjDPILe3SeeBTJU98Mzg7y0qR1FoVDxMgYeo5fHCCjBaTjcEfPhcECh-JxInsl6zHpZfB2IF3L-yKc5_OTQJEHQBu6zGMSRmWy2R3mn9EiahBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق گزارش شرکت دریایی Vortexa: عربستان سعودی از روز شنبه هیچ نفتی از طریق بنادر دریای سرخ صادر نکرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/690245" target="_blank">📅 23:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حملات موشکی یمن به جنوب عربستان
🔹
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/690244" target="_blank">📅 22:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908b07ec94.mp4?token=TQg4QQVzis7XTeNnMNgyyd1usfHGOPspTPyI2znQpSnJdERqkL12y0Ke79WTsC0HGaHOZ3JWq5hfANhAWnrXOMsUPZWKkLCnWN2bkNQW0Er4ZiDQu11kPSC_il55pLLLf0LBqkGwi793_-5mlL-ocrlYYgkEiP42pjGiXucyGI8zVwPXkjsXF6helrhVfSi6XExdl_zBCwR4KRnU1CbJduRCh37oi-uSb9_ufHy9do7rzBd06Iu7z8ada1d3dPPEr14yiiS6-oNozin3FSfvoxteqDH7CtkEEWV4VpWAiwjo0TJmdMy4KHaiUcqzAUzYiw6UGDh708R9ER2VAZ0VxL2WFUr0XBLaWP876BgdYpLBHVaQOkiGki-XJPF6RgbFdUwPXx1jy6ILvuoQ7r20KUUcnQXS4ZW5tS1KE6BfBDfi0HBWMLi4H9w7pb5QyX9UZ6E1YW4uXViG4BP39IoyI3yd8CEpCCTSUCTGFLZk7F9o0ZqP9F64r6FTvx60O47JI8G59ebZ-uU8JP3zBaufRJB6GtP0pNTN4s1uhbgoxJAbbJGidDbm-LTBsrlhUkjRYUlTtWdLMMKUb7Ry0iZMCIQUdMREAoDfGD06tACaiY8E2VRQf8gI1ITPJsvKVGoI1JIp96Cip7GpImSBavp2PFDdWG_UJ5pLwo9oNOgQ0pI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908b07ec94.mp4?token=TQg4QQVzis7XTeNnMNgyyd1usfHGOPspTPyI2znQpSnJdERqkL12y0Ke79WTsC0HGaHOZ3JWq5hfANhAWnrXOMsUPZWKkLCnWN2bkNQW0Er4ZiDQu11kPSC_il55pLLLf0LBqkGwi793_-5mlL-ocrlYYgkEiP42pjGiXucyGI8zVwPXkjsXF6helrhVfSi6XExdl_zBCwR4KRnU1CbJduRCh37oi-uSb9_ufHy9do7rzBd06Iu7z8ada1d3dPPEr14yiiS6-oNozin3FSfvoxteqDH7CtkEEWV4VpWAiwjo0TJmdMy4KHaiUcqzAUzYiw6UGDh708R9ER2VAZ0VxL2WFUr0XBLaWP876BgdYpLBHVaQOkiGki-XJPF6RgbFdUwPXx1jy6ILvuoQ7r20KUUcnQXS4ZW5tS1KE6BfBDfi0HBWMLi4H9w7pb5QyX9UZ6E1YW4uXViG4BP39IoyI3yd8CEpCCTSUCTGFLZk7F9o0ZqP9F64r6FTvx60O47JI8G59ebZ-uU8JP3zBaufRJB6GtP0pNTN4s1uhbgoxJAbbJGidDbm-LTBsrlhUkjRYUlTtWdLMMKUb7Ry0iZMCIQUdMREAoDfGD06tACaiY8E2VRQf8gI1ITPJsvKVGoI1JIp96Cip7GpImSBavp2PFDdWG_UJ5pLwo9oNOgQ0pI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر: شبکه صهیونیستی و دوزاری ایران اینترنشنال بداند که من اهل باج دادن به هیچکس نیستم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/690242" target="_blank">📅 22:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eb4nKCNuoWeZAWfY5b0YU0Lnre5WxXKCQgSO-MNBEajGMl94zHafmwIIxHX6lLmMTrmc16hGhrRhPKcundwcyG3aB5HcRwR6BJTMrQ98IKG9O1eqBF3fFP2Hrbx1d67bgMp8Wftm61zUmQhvm_XxYwEVcoTtvk7FfhLEk23BtLHPrbHAHTV_MltvXiNZVwtNsOrj95bBpMs6osZKp27HG00EHy4YfEIrl0Ztd8eJciMEy8y0J6lJrHHnOxypHM9TPhJnFQCoAazsQK34bqf1ZLCOH5xg_Eqge2KmaRRsZfEZah7ExvKQJyUh7j6scE-JFf_Pu9c4EHMe7I3kauZxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh1_VxX1LThttFG-GVp9eZAdV607bAvKebFEkHuKW9gRvHzxXnRzWCypub_qG6im0PX6zC4iUJT6HVxRQh395t-na1MzI-3pdKyiHpop8o1jtuZ_N_qeFsGcG9Y6HxTOtgEnKM9ALkle0GHl5Cq0tyu3sBlyCm-Yy3wJUMps5MkLN03o7yC9bZiDLSiXuWavsA6KXzsaIER02HMVIjUYQHz6aixIagDVmlmTJYhzjIxejJMjaKyJ-qiSRFPlNBpxXPbJ-o0YO32HrYy4NkRpihtqWVuVaEkm1yJokYsg_WPCLIctgsNdHWwZj4xIn0zzgBT2_ZYjvSy8uqy2KtKwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF52vjeMfQXyA5nlMy8RF5-SasfDoLvIKPTm70HuxfEkOCk-RRbUH3Zw_UqG5NawBHi7iBozm0TGHpfG29JxUPtn41e7lABFS25mhSZD8fjuEzf1uJIn8IBVq8u0PhBANF3F_Q41vIawv_Qz33-7BDyOK9-ddOFcTco3T3cveNZVH8mY5Sw820FfD6O3oq5GpTioxjc08e2CPvxxerDlzs0fdVIdzMzpQ411fattSvZxrwgB6HBKpaeMpprr0zdO7B3s2DGKm0DEEw0_iGHT43q3ST2ChjGrDB0W0aTmvMy_UEB1k0OIVEGepl0bZfKyxO1rob24Vf4uH-UU398uKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UI9HcLkyzBLoLMO6t7Fwp2mLoAYRkFlk4TlplCIVg2LeF2OGB5czhVvExvvVbrnQSRDkAOddBxLmrHVKcKLEHgB_B4nmF6W7jirDtdRbua9FuXOvB5Vv4p5kuNUAz3I3VnsJydJsXVHnSYKTqh3HhDtkXyVDHnZwkw9wSlwq9wZDwvKr3yZkmPilR9wE73pc9jMnI_sO2G1Wq9s05SANFEBwdbGEp0sD4CxeV0ZGLDSvCktxd8Tg_ILCkdWl4eByYrDyJ9Wfh_WM0cohKIUIDxGsIAv3lT8kZMxEoLr390658fhH5LAMl-Ydom4Y3ekoCNGv9egGnHOL8nwfxohc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvQwQmYfNbCXNiEFcOUYQi-LPM8OJdnj9UcABtI6t19xuJ-ySElNGNVgHv6b-W0oPKwTqFYbjTLWwWX18h2rxIfNA3k9MCkHo7H0qjp3wFYenE3ZgtAO4B26JqbP9T9ZfuavQnKWnYvz-NBfHZf_fOIpX0uaDpYfVOjN-TxYmgmaibq7_YxGY_KiMLh1krY3DAaFKjvca4m9MYUHrJ0z7eJwDf-LGIprQol0g-LUlIz7gy-ZQd6N4bIU71MOupsA2zxjuorTH223Aqjqq1f40WNWyziOlJXYUBtbdoSl1E-8jgnoehX59OJJJ1f1sWkrmp1fwJOO2P5uoIhh-wT4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BE4f2wlBXQ8rOT8ofvoFJisDPxt1XpQ39JQ6cIJNWWcoQNuiplvF0GV6tx91vCjuU16-fPyikw7lhlxSZOgFuNakSniMVFuuQ4ee0hLPqUV29TFnQ63GrlEDv7PGm83ElI3RFslBgkeZvcfLrP6tcEW8onukAVpM0dIgb5nlwiB5SkyjCcIamNA7GpKLc0W8TqausGiH-fPhyG8q2KNnN35Bb0Y91i2XMc1chM4DMlL8yQ5CNBdzkgLyIMEnmQFWXQhZXTIb87MSsnFnF2wx4x1Hy-rdATitFdYa-xk4COnN1gcdopyfgx4M98j44t7o-oiC46pYogpqwuH43LN-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vt2QBE7D2tW50_mJtwkqZprsJPrFHqPU_QXYEhXXfR_t0jwttBlLb69lhAb-JHGYHjaRMI2Gbk5HeA12cumPT92tPzcVNpzM3QQSLGUIGbYfHTmntx7C5a5xqv5LhYr4_hEDeUNwwJK6ujt6IAOuJ55DaYwmrnwVhKax9HNVvr1JhDb2DXb14XfZIGeWt2zy4i6KQe_O4mVU2EcA_UWqi6ShImOJAJAyZs374lPMlGFilg0Hdps8Z9I0bmxX0C8eczTlrLk0MdU_ipqchCEaUmc4j8N1MvoKVLDbEtmZPNHcObIfvdf0teOZusrD052FQonWcmh8_WHzT4WNWzA9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxEZex-Eth64kQ0Ra2iLzGpd37g_fZtKfC4Zplf-oHY0JTexii5uXY498NLQf8oKt-9wj7vAzJYp8Y2N1lUhp2Zn5pZxRScHXGR6ieqllAsdonh2p5673jT9Id26osxQPq-L6rW1Qh8vrqAjpJBng_Xn3MkaM9VPJc310Qr-i_vHluNXZ07EsG2dUwzDXbu2vz52gbPM8pKOeSkN4SRNSKGWH48RzromsFyOfpwanoSzXKKBDdXsAYoCAz_LNHWYpTapSxnqIVS2mSAQGlWbCY3rztiB2LCizQidetU3lHu2Z1AAJRqd5u0yRNIPslgO3GlLDAZoZYVak8IfXp86Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUVBFa-hZ6RtNtINKESsrD8q4FmG476f5uVSrBhxypKiptbtXNqqREXtbng66daPCbnUqves3hbX-KAEySo6m4ksDf6AWrpMMZNGgN1NPJxuFmHYTiDcxyTugoAu6NUzELRN7ic8ygVRY5eGf3juEDBB_fJDXRNR0RXwYEyDNZ-16oe90gDTWW7yhIe5mbNGBqaDCQDgsPOqEsezA5y7pId4JOnLjvKHU2u5aWBhXBS9oNEN9Zl6XFzHnZjNMi6t0Xa35rLwKi_QZAqehWsg62EndqUzITmKDKh4krFmjLTUsV0GGbO7AK1u_fKX9p19VrJvhwl4bcZMquyn99O5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxD74u7aaN0Mpj6XO5W6xMwu60kxkaH7CvhxhdPVK_5QvYLu2ttJMPaJR_8fjTzHcfykheUQ1zcdwhKTSyI9k8s6mtBqmcP5s8U9K6wTTLS-eyyLotrA_HKgPUqcPkF7yAFCe-D35P8p1cM8hj5EPzCAvElCA9Sm5DFUpK1AlVRF8sr76ZHp84mH0SQKf2Z2wDRSnnvo-X068e6BScK1JcWN-17P-Y6DjLjpNEhCocPYNr3WnkTn2hXx04-6uwPw-yFFuPWAGiV6oALADmmAJDqyfVITTGXv19573qESn6pI9BIryzFQbzeO3m3WUmgahWHFqWKyjoZrJRK8wEBGPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت مخاطبین از گرانی، کمبود و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/690232" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حملات موشکی یمن به جنوب عربستان
🔹
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/690231" target="_blank">📅 22:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeMJafpcrlAIzspDHED-OHC7sfT-RNpQsaRF-VRV9AARdC4_G3R7-wYo0h2Sxo1TYuvzp3ISivK4Vuy74x19j_rBGdBAYTnue6XbI4pHxS-dl9_y4nXJMOdD-EbAP7VUg2tBBzkc1Wcsx3B2PxBh2EnK_yMiw_NcYlUwYo6QQ-t_TN_n9QqE9b6mQ42dLHZ6Pg0-JRIF1DsdFQHl6uqItkLslHF2XpgF6J9s2IldHhspyygNhJb7WelUl9070XG_DrmmAU45Vv8GO7BykaBN27H_-e6NnInb0KKjVnR3yW3A0GyVnd24tYAhItcbrQmaNOB-XyRHoN1oNUXTQ5ZnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: آماده باشید برای جهش دوباره قیمت‌های سوخت
🔹
حمله جدید حوثی‌ها به پالایشگاه ۴۰۰,۰۰۰ بشکه‌ای آرامکو - سینوپک در انتهای دریای سرخ، آخرین کریدور نفت خام عربستان سعودی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/690230" target="_blank">📅 22:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o78vlt4fHaFlNfLRFX-5l3rYKFz2HQIONKdEWEKpabBiE07WkaM2z1-qtYlsb3eTI5RfMYfUvyx1BCVHcalV5oK8hyH3V-g5zT-c9BO35SO2ba1D730bmzsiPOYOGHMoUC79JcKCszlMkdc6FD5-Rm1ZWkQNkDMsrY6KbA5jugv-dF1AMlvss8oMp6E1KUydBoBKzkj8dt9eifHKnnf1Us27uJo3EpXJPy_gL124iXO4POi6k_husVCj_Vp9ez-vOFZ6MwPKY1rHuT2PM0mdc-V8FvYeDjyt0q2Y3hFdXVkEA8XamrIo-5p4kNqtv7XeQDY1HNYpC6m7kBLdkt9yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از شوگر ددی تا موساد؛ حرف‌های جنجالی امیر نوری | پولدارم، می‌خورم و می‌خوابم!
🔹
امیر نوری در گفت‌وگویی تازه با مجید واشقانی، از وضعیت مالی و دلیل ازدواج نکردنش گفت و درباره روابط عاطفی، حواشی «موساد» و فیلترینگ و حضور احتمالی‌اش در جنگ زمینی اظهاراتی خبرساز…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/690229" target="_blank">📅 22:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند روز حساس و سرنوشت‌ساز برای قیمت طلا
🔹
این هفته یکی از حساس‌ترین هفته‌ها برای طلا است؛ چند روز آینده مشخص می‌شود که طلای جهانی قرار است یک حرکت جدی دیگر داشته باشد یا وارد فاز اصلاح شود.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/690228" target="_blank">📅 22:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ca3e41fe.mp4?token=fVW1OLS5Qvjwq6uZLvNdPY3iV5wLt7Yx4C7oSyVJu1g7PEa3PeGYt5usQ7ypLOiJEdXosO2P-NZjW1C0tFXN6URsQ_ybzFFnqYCYvH9VL0FesdR-m_0h5c7VoDVLH0Eker_XpB5dpOO5pG_HlbU4o2XLmbOIeiqaqcwmkn9edTXjnZKd9omG1swPareO5ZxCLdfh6N08A3dB0WRtOzGHy3SxcXFw1arMsdtSRRCi3c5vdqlRM0pDRznbbo-_rmMUgPp4F7y60Te-STn8vIsj0k4l11IK6HVGI-rtwpd0aF81_7GloSpO3afRGHJigOcVcswurgpl4WbBxNnfj1p5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ca3e41fe.mp4?token=fVW1OLS5Qvjwq6uZLvNdPY3iV5wLt7Yx4C7oSyVJu1g7PEa3PeGYt5usQ7ypLOiJEdXosO2P-NZjW1C0tFXN6URsQ_ybzFFnqYCYvH9VL0FesdR-m_0h5c7VoDVLH0Eker_XpB5dpOO5pG_HlbU4o2XLmbOIeiqaqcwmkn9edTXjnZKd9omG1swPareO5ZxCLdfh6N08A3dB0WRtOzGHy3SxcXFw1arMsdtSRRCi3c5vdqlRM0pDRznbbo-_rmMUgPp4F7y60Te-STn8vIsj0k4l11IK6HVGI-rtwpd0aF81_7GloSpO3afRGHJigOcVcswurgpl4WbBxNnfj1p5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادش بخیر؛ سال‌هایی که بازگشایی مدارس، یکی از شیرین‌ترین اتفاق‌های سال بود
🎒
📚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/690227" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFirMzuEtgPnaHJI6B8X_TQl-xm9IFkXaFxp2vHiEjNh9VcUIRzVw4pymUYckw9hqY18SjahT8OE00hBOXGD-4By4w6likb-2Ve5NJj0c_vDIEVabcHyuhe4DcyIzK4WLGXnsWcW1IUEWE2SN3XSBPUw5UTiyJnbb0NFpxmWRTSUmlAuCJ4ADYJduJAousAOmUzgpHdpkhPZDKW_wIBEmWy2UKJMdxt8Yza7lUyVcVhsYDRd5bwRFtpKJO9-m3WvLTDJP2419HdJ27nDjqed2HideF13_44DPKHcLnvsTWBQCh2uOoDj19vYJkoHQNYyCNeYKiL3JQ9uXj2ou81OYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویل شرایور، با کنایه به ترامپ: «ملت شکست‌خورده ایران» تمام پایگاه‌های اصلی آمریکا در منطقه خلیج‌فارس را درهم کوبیده است؛ پایگاه‌هایی که اکنون همگی غیرقابل‌دفاع هستند
🔹
ایران، همراه با متحدان منطقه‌ای خود، همچنین کنترل مؤثر سه گلوگاه راهبردی مهم جهان را به دست گرفته است: تنگه هرمز، باب‌المندب و کانال سوئز.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/690226" target="_blank">📅 22:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcpBJB7b84HjEkhY503nfGuK0NDXolpXc8Cuvf34oIHCQyiXvSDLJeF0y1q9QB0UcloAzVnHOIFV7RlOtzNHUx02ZkRMylJOIL9oVpalmz97z54w6PsV4rNz-l9u8ovAQskCZlYyILpHq2h2XpaD2TkUC4hPhpqzdCn_DRDQ-uuid66pncnrlLYpzuzraFmuS1hh4Yl0B8IL48xR604cchYkfoIQWzu6YKGgwOHcfVxxqmZUXvfVFDgFOr0dhVO9IcEP6guM5fy8FxOnsGTzpB6VeIr_tWulcxf9diLd476Jln4UR8wm0Und_Ybk7QsMrmuoNGWR4qKLPHaXPHsKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام شانگهای به رکورد ۱۳۵ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/690225" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/690224" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">گزارش بازارها سه شنبه ۲۴ شهریور ۱۴۰۵
بورس با تقاضا همراه بود
طلا اصلاح کرد
دلار در محدوده ۲۳۰
همه چشم انتظار جلسه فردا فدرال رزرو
@Titretejarat</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/690224" target="_blank">📅 22:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbaab5618f.mp4?token=a_fjHbCqmcjhLgL5wV7q1TAM7U85-2vrcybcFvFXvRFoAo8LSJUwxte539iKMDoGZHp4VphNP3yR_DnFZXGf9N2ND2Wk0RbqqbEvIDhncT0-7ASkOdy0Ktxrk66rL1--Wcx_du8f-FH615zu1FyQ1gtjCPIKfD848V4d6SMTL6V4DoI0xgCRx-fDJ1iWixewO4Rou2q4D5FSq_BwGgzGqF28R3H8y2x--F4mAeRylqw_WgjM5WDEuH7MvEuNM_c-bKeaL2kog1piEYN-731AGA18XZl_Ygukz1zfSeVwGoC7xJVgMbJJ7Uc8Ar3U7lleaWu2KrlO5uN_8Lqku0RkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbaab5618f.mp4?token=a_fjHbCqmcjhLgL5wV7q1TAM7U85-2vrcybcFvFXvRFoAo8LSJUwxte539iKMDoGZHp4VphNP3yR_DnFZXGf9N2ND2Wk0RbqqbEvIDhncT0-7ASkOdy0Ktxrk66rL1--Wcx_du8f-FH615zu1FyQ1gtjCPIKfD848V4d6SMTL6V4DoI0xgCRx-fDJ1iWixewO4Rou2q4D5FSq_BwGgzGqF28R3H8y2x--F4mAeRylqw_WgjM5WDEuH7MvEuNM_c-bKeaL2kog1piEYN-731AGA18XZl_Ygukz1zfSeVwGoC7xJVgMbJJ7Uc8Ar3U7lleaWu2KrlO5uN_8Lqku0RkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعات تکمیلی سخنگوی ستاد مردمی پویش جانفدا از فراخوان آموزش و سازماندهی یگان‌های مردمی جانفدا
🔹
ساسان زارع: افرادی که پس تکمیل ظرفیت ثبت‌نام می‌کنند در لیست انتظار ذخیره و پس از هماهنگی با نیروهای مسلح سازماندهی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/690223" target="_blank">📅 22:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3482a7dc19.mp4?token=YD8YDwyPJJkVRHonka8yMpuEyN4AgIfiVwUSr_YlJGeMFKpGMXXU02nWCymAGKknd7P8czC9wYY6nCUtXzaqsSmvl9UzlijEdYglPVFTSJx5euf8-9dnMiXmyXPnX9-fimydBcj5cfA8hSnT4sq2JC1h-S5VvMtuTOtzIyS9q8fnB3B4k62Y6aySBL2NuaTwvmkktpXhYbCJAJt9t4rSeoTmRj3ErKqWoX3Tk7tTfYlU4tCvz7oG4LA4ZajarXlbAVQnNhRIli_3VZC1i3-hJp7yQ2qS5OHeFQF7FBY4eP3jWjam9qMOBo1QTby2S6a-7SbumfpRtAlX-RE_8UWV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3482a7dc19.mp4?token=YD8YDwyPJJkVRHonka8yMpuEyN4AgIfiVwUSr_YlJGeMFKpGMXXU02nWCymAGKknd7P8czC9wYY6nCUtXzaqsSmvl9UzlijEdYglPVFTSJx5euf8-9dnMiXmyXPnX9-fimydBcj5cfA8hSnT4sq2JC1h-S5VvMtuTOtzIyS9q8fnB3B4k62Y6aySBL2NuaTwvmkktpXhYbCJAJt9t4rSeoTmRj3ErKqWoX3Tk7tTfYlU4tCvz7oG4LA4ZajarXlbAVQnNhRIli_3VZC1i3-hJp7yQ2qS5OHeFQF7FBY4eP3jWjam9qMOBo1QTby2S6a-7SbumfpRtAlX-RE_8UWV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا فرماندهان ما به وسیله واتس‌اپ ترور شدند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/690222" target="_blank">📅 21:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس سازمان نوسازی: بازسازی مدارس آسیب‌دیده، بدون استفاده از اعتبارات دولتی انجام شده است
حمیدرضا خان‌محمدی، معاون وزیر و رئیس سازمان نوسازی مدارس کشور در
#گفتگو
با خبرفوری:
🔹
برای مرمت مدارس آسیب‌دیده و ساخت مدارسی که به‌طور کامل تخریب شده‌اند، از اعتبارات دولتی استفاده نشده و تمام این اقدامات با کمک گروه‌های مردمی، جهادی و نهادهای مختلف انجام شده است.
🔹
بیش از ۲.۵ میلیون نفر در پویش فرشته‌های میناب مشارکت کردند و کمک‌های مردمی از هزار تومان تا ۱۰ میلیارد تومان برای ساخت مدرسه اختصاص یافت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/690221" target="_blank">📅 21:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9258f4680.mp4?token=JzAVmi7a7kHFzaoCC_0Dn9pzGaqqfS7AIwn1afMIOWo1b7l7-YtgTpan6EpeQMJ9DeFwh9oeEO5_n0g6EbmGzXabS_vaYAlfMjFUiVn_52ZAnbMsaKJyqD2diZz5sPqreRV6KVjCrRbLVvVP_xYLfqMgFDK19RRVcBKjjL41VMbwF0IwByR5C5epL_tZEQkAraCdw11CyQeNOW0a7WLuFhlxkQwugCwaJNHfzGlN5cD0x4Vgu0qlGy_FCid7-3WfuBDKthGaWE57PmWiiXyQTl0SmlUmcZn5p7muKV2Wxlxp-7-PxLrOP2MR0_AsRchuy0H6izFp6gQ8L1Ah8Dts0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9258f4680.mp4?token=JzAVmi7a7kHFzaoCC_0Dn9pzGaqqfS7AIwn1afMIOWo1b7l7-YtgTpan6EpeQMJ9DeFwh9oeEO5_n0g6EbmGzXabS_vaYAlfMjFUiVn_52ZAnbMsaKJyqD2diZz5sPqreRV6KVjCrRbLVvVP_xYLfqMgFDK19RRVcBKjjL41VMbwF0IwByR5C5epL_tZEQkAraCdw11CyQeNOW0a7WLuFhlxkQwugCwaJNHfzGlN5cD0x4Vgu0qlGy_FCid7-3WfuBDKthGaWE57PmWiiXyQTl0SmlUmcZn5p7muKV2Wxlxp-7-PxLrOP2MR0_AsRchuy0H6izFp6gQ8L1Ah8Dts0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی تاچ‌پد لپ‌تاپ که احتمالاً تا امروز نمی‌دانستید
💻
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/690220" target="_blank">📅 21:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
درخواست ۴۰۰ همتی بانک‌ها از بانک مرکزی
🔹
عملیات بازار باز بانک مرکزی در هفته گذشته بدون تغییر ماند. بانک مرکزی حدود ۷۰ همت منابع در اختیار بانک‌ها قرار داد اما با سررسید شدن همین میزان ریپو، تزریق خالص پول به شبکه بانکی عملاً صفر بود.
🔹
در مقابل، تقاضای بانک‌ها برای منابع از ۴۰۰ همت فراتر رفت که با ادامه سیاست پولی انقباضی و محدودیت منابع بانک مرکزی برای مهار تورم رو‌به‌رو شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/690219" target="_blank">📅 21:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYzbSU0SCYA59Mlla_0xz2uA-Tk6oNmNtbkPPl4Ki1PpnQy0Gz_rzups4fd7aWaKfJhxvnwCpP5HOwyZ8eRIxpsBWHNilR9nhxKaaDWcFj0_39EPewS89NpAEYsGbsg8TQoD4GrMYZ5wmj4z7_S-yug6EELLVlBciHjsc8RbCZFkCPtqVFncTP4nXB9D09hen2zGHqC1khI4ftSw11gjbw_5SCLq3373lsYQwhLPPMVjOA-k9DFevwyljGk6v5NxDP_qOAcYHsioUqobzxX4BIiEGMNdYY73AUi_ALayUxTBLlc9E94JTK-EkxTCSvNBVQPrKd7wIx2QPxXQc4gBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbAOLNHy2WZde1rXA3sMik3555MFzxSR0e0WdvGz1U1CRh-w94RaF5cEK8HwKqafxqNmmEDmFg9KY_VltdKdgmcDFZ-kVYaUu4_IjmZHq5X2ydPUW82FxbZfwVHWBcQZ_RM3aUHfb42wvJTtBYBt8_OIEx-JjOw7mxZqgHB215LN4-1SFeaJ4Zbl4yvvRaN5_6rwmC7t1tfhj-3hDD4DuD9Oxv4dEkLhdiKMp6MmteCVWiuMbYESr-AwxdErqmgdqzynAEGBbVn1-GhX1Me4nM4n_xAnGtuG8412YgHAxNMjs8wY6_pn0RoecZlVMI7rUG0oeBbJR7ptaS_dnwMatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGwbWcoIbMezYVrvzYvi5h4Olkg329mWwESHcdV1A4-YaikmtIaQoVhC63ihN2pEW0Ho25jd4q7mpBLMRq_L--Ds0i6Adxqpnkn9YhHJ4WZiB0d-CeTgj7Igb42ARm3Z__TwJOaiIt32pJ-wTEY3erTy1OEdV94Dmj6Lj1fCBXjEZRxul7DGn-vehR-tGNVMM6kF9hK1xZCs2A1daNVBG8P1qqW8aRZMltmK7SDmlvIRRHJ3-8o1mee6cae0nzQ06Y79ce8OlkiqHbQzyur_G3pXSXZZX0jw6SoPap3dy0VPYEIn5bnG4JoUMdWiR2awBZyrAMstDQViJq29n0hxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXwdykDordaCMJDxzGVVQTvZn0j5k38z4VP50-JUh_WY1gGkWHcUvmthl1I90-C8wbVSEp8JN-REAKBWonSOZAr2NEFmjnObwr5CcEZqboa5ojLCRjG_ltjILN6BbkZ4zZU7eWd6BDaexYJBo5ELjP7TG7knfdeDifwqC8EBsq6NY_P23vdKPuk4M1uxIpFP7xNik1XT2Xi44EWIBcV6vHIQYvfUm5k0Z1XaQXXGI3G4rwDNW20JwzMF5MvWE-RALXGkTbECmwQ_y2S0m723hZDQS_JEpFz1yi6v8HL_y3GcdEE59sWrmTGpQPH9qMpDg6nrK0d8Z1XY3e8yiPchXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1g1yFkl1A_F1DkRR3qqn2mSQXf6ZWqFNpwxlH2krvTUAUwwmaewegji_D-xTIFGOsx1elCMY1MlaGc3dzaaNAaQwZu5cYPhabQHgCReGpnzDNaYtc-akaW3vMvWFYLlxoKB7g_NKq-ovlI3-6WqtX99i4-1kjS0VRVk1caAp9sG_ZaX9V8u1wlnoKdGcYiwcxZ37Mt_AZ8QBqIJovwtULK73OT1n9W29YHlNza8CErFVXtntscCkEJ8IXrjmYczTGiheG9VzXNbC1sMCcdQK_KxKjSzjycXZUF37bL3ZzJ009GuLjYmbxKsOVokBEj4H4c5TX-JjkuCAY5Kj0HMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7kwZNz8HTz0AzS89vhUxf3fiKlCMOLrGpHkyKaW-WfA5QDjIQLeqVKvOSggRj6fgGOZVOhAzX4pIq-BsT9w7TW6RDn__iD96a4_KuZxzUYCiB6FLjhfgs9VXvnDTqnidDR-dSIVIb9RmgGO-pDaG4ca3SEw5TKhc5T-ahr3n54MPhvca305yHP_bBXVCc8J3MXdi7_Io5OaPtm8ixGvTmaLDe9jY_yC-isda-7qutw7VUQp9xkpoAgnrhmd9PopxTVQqo0Xe_cYh9wFb4cRfDTQdC-xrrX2p-Ex5kAkeFU7ojVvRB1La6v1nZIxsDbw9DeS4vxdx0vitlZeERBTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGKLbnyKkeZA87LKdGVpXYdWNp7AMaNIJMwDWbLJ78PS3wAzQ4b-PuW9jkGZkvfvA_-QvpzzOAPpsmsc2pHU-OZl4V_GqvtLIjY2RPgdkea0nZYLXdT69mozhofN9nAb59J3L71LH-Vr99GykaT7x-Ec27abwOJsXlEoLwO72JjBrdIkFAEI3A6vkDpfDGrp2s5M8xNuL0TAGQDdA9jLMCs9C1dITF7-Roj6x-hpJNyOWSz3xlEYEb83FzV-klHFNxFFS3uRctdbYNy6sFFbxSgf0DC-nb9322e2LOa9W_98-GuvmvOFwhQ8PkGlPyw7_P-pdDDpTt6eTtH-qb1Djw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwNchPvip7HQNEXnfVrwQF4DTPZglIVQluRRN4Se4_kduXlSt3i-U3dIov1Zua7qhsFGy0wnn7Bxu6L0aATzEh7eS7o-cdkscE6Dc_rsI5ACERi9vmO6j93yGXnAmc1FNUuNo2y9_a9P55exc4LbImPrAS4Yy9fJzbEsVs-KWDOGM5OiJOLwMECe6sqAMkWw89QAhTZfCN20e_tS1iYGgY2HWgBYkjxMrru0N0hQAHl9t5nFtFiDGZFhJZtSOrDanDsPMrjx39t6Ljpbr1T0WSNHSHzGde_ZcXaagfQDAdghFy2riEgTtReK8emTAJ6Ewz0ubl7SHSsogMd8Wi3neA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت مهرِ جاری
💫
✨
مهری که از دل‌ها آغاز می‌شود، وقتی به دست مردم می‌رسد، معنای دیگری پیدا می‌کند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این مهر را جاری نگه می‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/690211" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بحران بزرگ سوخت در جهان آغاز شده است
وال‌استریت‌ژورنال:
🔹
مدیران شرکت‌های بزرگ نفتی آمریکا که در ماه مارس و همزمان با آغاز حمله به ایران درباره پیامدهای بازار انرژی به ترامپ هشدار داده بودند، اکنون می‌گویند بحران سوخت وارد مرحله جدی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/690210" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690209">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سه‌شنبه‌ها روز بدون خودروی کارکنان دولت
رئیس سازمان اداری و استخدامی:
🔹
به همه دستگاه‌ها ابلاغ کرده‌ایم که تا حد امکان، روزهای سه‌شنبه را تا پایان سال به‌عنوان «روز بدون خودرو» در نظر بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/690209" target="_blank">📅 21:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
طرح استیضاح وزیر جنگ آمریکا کلید خورد
🔹
توماس مَسی، نماینده جمهوری‌خواه کنگره، طرح استیضاح «پیت هگست» را به دلیل تداوم عملیات نظامی آمریکا علیه ایران و نقض «قطعنامه اختیارات جنگی» ارائه کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/690208" target="_blank">📅 21:29 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
