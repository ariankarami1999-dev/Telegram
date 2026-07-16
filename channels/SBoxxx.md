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
<img src="https://cdn4.telesco.pe/file/kpLs67CG3FXweFN2uRQxenlUNcLNc0nUlccZ3dXpegDflM7GyrzvVjbYE5p-QuJOcoXZqa_LAbUZi_5AVtXnXJUh4tStai0MWPzG5iu8_2VV2sc-dnwfjJs8JX_MgksISnSSEXqmIjSPotd9maY0kDiF321VuKKZN7DwyEKPtAAyGzANuocheYnxMdLwoivqDe52xMYboM5at8UJ2h9Ej3DaJ5IC5Oc3B3GH9c_dc2kHN-V68p3LYK4GUGphGQTRNdstz0AxBswrXreexNhVlsm5UEmvK29OGm4uHj5CPoTl8wlTRn0lrA2ywoSWKpgWxBUyqbAC4LpxV1V7YmHR2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.3K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 01:59:37</div>
<hr>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/SBoxxx/18860" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تلویزیون ایران:
قطع برق در فرودگاه ایرانشهر واقع در استان سیستان و بلوچستان، در پی حمله آمریکا، اما هیچ تلفات جانی گزارش نشده است.</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SBoxxx/18859" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoUj0wPQJIsqd-OBy1MuRUgK4Z9NeK94qrJbx4r7Bdoq9QzEWrVQCpJCyOsdCylV0hR4B4Kb86M8mCnvAQvPtImTp0OiAfak7gaVPLXztyxT3S49o-9fCeA6TVAaw4LfVjUuDujh3bbUj7EE47mZi-WS3jln_le9jhKrF6esOOYB4z8ennox54NcGtRTDMKaon-YaEgG1C5JKd6AiaShzeo9r-teoGD7bwp5N3CcP_qwj-t0NlVurua3pzrAgvaLmVqMihB7-7lCzkRWzPUUuPDifW5jNczY3jBp3j_s3cLY6B5Vw4kBNNIyKx08ip99s8Yec9xj1uOZW3W6Zig9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا ایران مستقیماً یک سامانه موشکی زمین به زمین آمریکایی را در کویت هدف قرار داده است.</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/18858" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/18857" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/18856" target="_blank">📅 01:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!  هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/18855" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رسانه های اسرائیلی:
پرواز جنگنده‌های اسرائیلی به سمت مقصدی نامعلوم.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/18854" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/18853" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Business Insider:
اسرائیل از حملات موشکی ایران آموخت که به رهگیرهای بسیار بیشتری نیاز دارد؛ رئیس برنامه دفاع موشکی: «این یک مسابقه است»
حملات موشکی ایران، اسرائیل را به این نتیجه رسانده است که برای جنگ‌های آینده به تعداد بسیار بیشتری موشک رهگیر نسبت به برآوردهای قبلی نیاز دارد.
«موشه پاتل» (Moshe Patel)، رئیس سازمان دفاع موشکی اسرائیل، در گفت‌وگو با
Business Insider
گفت که تجربه نبردهای اخیر نشان داده است تولید رهگیرها باید با سرعت بسیار بیشتری انجام شود، زیرا «این یک مسابقه است»؛ مسابقه‌ای میان توان تولید رهگیرهای دفاعی و توان دشمن برای تولید و انباشت موشک‌های تهاجمی.
به گفته او، سامانه دفاع موشکی
Arrow
(پیکان)، که لایه اصلی دفاع اسرائیل در برابر موشک‌های بالستیک است، در جریان حملات ایران عملکرد موفقی داشته و طی عملیات‌های سال‌های ۲۰۲۴، ۲۰۲۵ و همچنین جنگ طولانی‌تر سال ۲۰۲۶، صدها موشک بالستیک را رهگیری کرده است.
پاتل گفت نرخ موفقیت این سامانه همچنان بیش از ۹۰ درصد بوده، اما حجم حملات و تغییر تاکتیک‌های دشمن نشان داده است که موجودی رهگیرها باید بسیار بیشتر از برآوردهای گذشته باشد. به گفته او، حتی اگر سامانه عملکرد بسیار خوبی داشته باشد، در یک جنگ طولانی، مصرف رهگیرها به سرعت افزایش می‌یابد.
وی افزود که اسرائیل اکنون علاوه بر افزایش تولید رهگیرهای فعلی، توسعه نسل‌های جدید این سامانه را نیز با سرعت بیشتری دنبال می‌کند. رهگیر
Arrow 4
به مراحل پایانی توسعه نزدیک شده و
Arrow 5
نیز در دست طراحی است. هر دو سامانه قرار است با بهره‌گیری از فناوری‌های جدید، از جمله هوش مصنوعی، توان مقابله با تهدیدات آینده را افزایش دهند.
پاتل تأکید کرد که اسرائیل تمامی داده‌های به‌دست‌آمده از رهگیری‌های واقعی را به دقت تحلیل می‌کند تا سامانه‌های دفاع موشکی خود را بهبود دهد. او گفت هر درگیری واقعی، اطلاعات ارزشمندی در اختیار مهندسان قرار می‌دهد که در آزمایش‌های عادی قابل دستیابی نیست.
این مقام اسرائیلی همچنین به فشار فزاینده بر زنجیره تأمین جهانی سامانه‌های دفاع هوایی اشاره کرد و گفت افزایش تقاضا برای موشک‌های رهگیر، از جمله سامانه آمریکایی
Patriot
، نشان می‌دهد بسیاری از کشورها به دنبال تقویت دفاع موشکی خود هستند و تولیدکنندگان باید ظرفیت تولید را افزایش دهند.
او در پایان گفت درس اصلی جنگ‌های اخیر این است که داشتن یک سامانه دفاعی پیشرفته به تنهایی کافی نیست؛ کشورها باید ذخایر بسیار بزرگی از موشک‌های رهگیر نیز در اختیار داشته باشند تا بتوانند در صورت وقوع یک نبرد طولانی، به دفاع مؤثر ادامه دهند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/18852" target="_blank">📅 00:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارهای شدید در سیریک</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18851" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!
هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18850" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نماینده کنگره آمریکا از «تغییر رژیم» در ایران گفت
نماینده کنگره آمریکا تیم بورچت خواستار روی کار آمدن فردی در ایران شد که به گفته او با آمریکا تعامل کند.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18849" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/18848" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18847">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/18847" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18846">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لطفاً از مراکز نظامی فاصله بگیرید. ویدیوی وحشتناکی از اصابت موشک های آمریکایی به جایی در بوشهر دیدم.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18846" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18845">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارهای بزرگ در بندرعباس، قشم و اهواز</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18845" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18844">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به نظر می رسد تنها یک معجزه می تواند از بروز حمله زمینی آمریکا جلوگیری کند.
تصور می کردم در اوج گرما این کار را نکنند اما روند حوادث چیز دیگری را می گوید فعلاً.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18844" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18842">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/545819aa84.mp4?token=FqlHa1nMwZp6AT22U0hVdWaiED-9ab4ymXL1vBOG8ZA0MLaVsUp8BrYgdOrw8MhQMdDJPst8Ly7zrWKxv0RStxsJSl_EOmPgj7HrgAf4cp8sHABZcng1LDcaJtbLc33NyH4j5G33IBpc0h_Dyzx84uH_yX_OQouC-YWZfkYdwTr4n26e6yN4PbfRDyQDGh93o6K8koG4nkM9yzHs1vUsB-JyJuLN3m4gsb4VS1aanNXFhI8TgN6C9_2N6hnSE8ho8EXa6sdvS_g5crRoxyhvKA_ZmaG0L6uq5hSYS2JLifLwt7c9WVMqDxPt0fsyZHOk58KR13rQiqCKHjvLC-6gZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/545819aa84.mp4?token=FqlHa1nMwZp6AT22U0hVdWaiED-9ab4ymXL1vBOG8ZA0MLaVsUp8BrYgdOrw8MhQMdDJPst8Ly7zrWKxv0RStxsJSl_EOmPgj7HrgAf4cp8sHABZcng1LDcaJtbLc33NyH4j5G33IBpc0h_Dyzx84uH_yX_OQouC-YWZfkYdwTr4n26e6yN4PbfRDyQDGh93o6K8koG4nkM9yzHs1vUsB-JyJuLN3m4gsb4VS1aanNXFhI8TgN6C9_2N6hnSE8ho8EXa6sdvS_g5crRoxyhvKA_ZmaG0L6uq5hSYS2JLifLwt7c9WVMqDxPt0fsyZHOk58KR13rQiqCKHjvLC-6gZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهار ماه پیش، در مقاله‌ام در Foreign Policy، استدلال کردم که پنج نقطه استراتژیک در جنوب ایران، محتمل‌ترین اهداف هرگونه کارزار نظامی گسترده آمریکا خواهند بود. امروز، الگوی در حال شکل‌گیری حملات بیش از هر زمان دیگری با آن ارزیابی همخوانی دارد.
توالی حملات نشان از استراتژی کلان‌تر محتملی دارد. عملیات از جزایر آغاز شد، سپس به سواحل رسید و اکنون در حال نفوذ به عمق بیشتری از جنوب ایران است؛ حتی به مناطقی که دیگر در نوار ساحلی قرار ندارند. این‌ها صرفاً مجموعه‌ای از حملات تاکتیکی و پراکنده نیستند. آنچه دیده می‌شود، به نظرمی‌رسد بخشی از تلاشی گسترده‌تر برای تضعیف تدریجی معماری دفاعی ایران در کنترل تنگه هرمز و دیگر گره‌های استراتژیک، از جمله جزیره خارک، باشد.
اینکه این روند در همین نقطه متوقف شود یا نه، هنوز پرسشی باز است. اما الگوی کنونی این احتمال را مطرح می‌کند که این حملات تنها بخش آشکار یک طرح عملیاتی بزرگ‌تر باشند؛ طرحی که هدف آن خنثی کردن، یا حتی فراهم کردن زمینه برای کنترل آینده برخی از مهم‌ترین نقاط استراتژیک جنوب ایران است.
@Iran_Simorq</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18842" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18841">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا (سنتکام): ارتش ایالات متحده حملات جدیدی را علیه ایران انجام می‌دهد.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18841" target="_blank">📅 22:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18840">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:   ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18840" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18839">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:   ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18839" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:
ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18838" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL8L0MiXF1sJJHmaSnFpSaz9Uj9O-DPo452KOdBRXuDZ1GSnmqXuCS30odTLKk-P3e6cOkGyX9wrEIXSCWN3YC9DDsvmtK43Dqdy2M00_AqmMM7uz-epDAaPqK4f-c2wypUiZibk6ADbqLr5L2b827uBreI7ulZMTOschu3xeIZqHbeCtud3_A07b5kS5fBNCEd8ZMsKaVvfWf-9LTicmgp1umnqOAc1hNpWOlxAoQduoaiGyLNAyjfjzHAFlvCLfqoDsni6l6dac7wrIBRTZsxC3W2KsMskf46ihqcOrq4dDR1rOlDLNxx7oXbqfJ8_t0-Mmq6bcZMzFHSek8Ofyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به حملات علیه املاک ترامپ در خاورمیانه تهدید کرد
باشگاه‌های گلف و برج‌های بلند در امارات متحده عربی، عربستان سعودی، قطر و عمان می توانند هدف قرار بگیرند:
- باشگاه گلف بین‌المللی ترامپ دبی - منطقه داماچ هیلز، دبی، امارات متحده عربی؛
- هتل و برج مسکونی بین‌المللی ترامپ دبی - مرکز شهر دبی، امارات متحده عربی؛
- برج ترامپ پلازا جدّه - ساحل جدّه، عربستان سعودی؛
- برج ترامپ ریاض - ریاض، عربستان سعودی؛
- باشگاه گلف بین‌المللی ترامپ وادی صَفار - وادی صَفار، دیریاه، عربستان سعودی؛
- باشگاه گلف و ویلاهای بین‌المللی ترامپ سمایسما - سمایسما، قطر؛
- هتل بین‌المللی ترامپ عمان - مسقط، عمان.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/18837" target="_blank">📅 21:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر امور خارجه اردن، ایمن صفیادی: ایالات متحده هیچ پایگاهی در اردن ندارد، اما سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین اردن و واشنگتن، در کشور ما حضور دارند. - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18836" target="_blank">📅 21:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر امور خارجه اردن، ایمن صفیادی: ایالات متحده هیچ پایگاهی در اردن ندارد، اما سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین اردن و واشنگتن، در کشور ما حضور دارند. - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18835" target="_blank">📅 21:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwsglzbQvElYB5rVGPR_1ksnscagMjYEykrQ4knzX70RBO9K6RU_acPNJWJ_fb8YOHuMciPzAPEgoGadZ_tUYT2A4shdI-de7P-Pp7UvVrRq6jLCC9dpSI7WQ7_pH0SpyUL57ssMznjqBluhrXqg4Ps5S1nhfVnO0J7J5hEwfD2xqZmQU1FoBomURL1PR-gadTy3sW__jL6IAYhP8kwL6ORxHDsvWiCPLZgxTAtu5G-bYtN1FvPAovho4C-z6wgjUaYXdpaltO9orSX6zSFuImpP0yQ7MphrygeoIO05NKzTABNUhx1nJo9On7zGrm76GH4XtKFUrJ3lccyeB46P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18834" target="_blank">📅 20:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9y8JLr5TQ-7oSQ9DYVYjXBAyiMAOXn3WN6WIenEHhTmZY6XjHnjSdZEFiztSOc7VXKmN98dvZuQMFlp_AazAbZ1PItzPDkU-h7s3BJzKFPpjvUOaAbNBeV1uDb7zepDuWkSuuoey9YSWMhUC2j3sAk3xat1V1yUb2l9HFDmv1Uh0RmqTBqbYbjeDmQPcHsHP2Wamye84S6Hbwjugeg5VV-gu6PNzPn-ES0j3_hksZnbFDVSoaQIfj804i4VFHSFglGw_cy4Y-ubP_6o_8U78uiO-NJlIquADFPU1arqmef42E86DwgCdoAV9kM2jJM3Q0-nWG0Edem84UX20LvJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سل طلا بسته شود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18833" target="_blank">📅 18:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">موشک‌های آمریکایی به اهدافی در جزیره قشم در جنوب ایران اصابت کرده‌اند.
— خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18832" target="_blank">📅 18:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رهبر یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18831" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این دیگر حماقت محض است. شما شاید بتوانید با موشک و پهپاد اهدافی را در یک کشور مرفه ثروتمند مانند قطر یا کویت بزنید و آنها را وادار به دادن امتیازاتی بکنید؛ اما زدن اهداف مربوط به کشوری که مانند صوریه جولانی 15 سال است اساساً در گه فرورفته و مردمش نمی دانند…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18830" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مشاور محسن رضایی:   تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18829" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0WK9GzgTyd5FgXZF65PHaeaEfkCxKb3X5kGry44NmzLqy3t6LHS78UJqvvW624gdAkEnuoCPD9ErBDcKysuduJb5Wwuuebs2IAph84UQNj8yMR3Ruqs85mD6zE0KY5rMg4TRpiBKapJR2JLp4rg6Iehy88UjODjENcwCLIxnpbT4YP7nwJMwnQ0sSYAOB3nhvwf858lbFS8tzJgTrrKGOCu0xWcVmzXM8uOys3KCM0ROJq4zv_8CGWFo1zpMq6kHVVZ8RONcYlJGVdNXEfabLjLtg4uT7AGbTwvCwLbwqX3qAmU84vxOIMIhLS7pqJk0nFccxYZ2G-DMpoHyn72og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18828" target="_blank">📅 17:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVt4LiaD2fHEA6qJNXqLNQMlW0b8Nf5y-R-RWgkOmy93BmK-iS8XCLrTxpejDK_9as5CKsm6XXz-VuSjCjNMGAnQWewtFxWA1U3VPOCH0wn4K395Gfu8v6N1Z2rAQp0JEhw68sB3R_Xtp07CTijaW1JOOsJ_8h6-rr3IE8iSGy6Ud5vgNY1oniATkqkdvXWw71COETL0ElLNExRWJJjjIUvyaM_S0Uxqpt8KsyS06U-o6w1U5eDheHrFFqAgvWvXwTAEdNQ4eCwpwEx4SROHc-Lye2mSLUyEqwu2lHAWJOxWM356ldTxJCsyyGwpFKwIjoejVqdjennToctxrlJfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18827" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رهبر
یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/18826" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18825" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی است و پیش بینی می شود شاهد جو ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18824" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نایا به نقل از یک منبع مطلع:
امارات در حمله شب گذشته به بندرعباس مشارکت داشته و در این عملیات، به‌طور مشخص از پهپادهای اماراتی علیه این شهر ایران استفاده شده است.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18823" target="_blank">📅 16:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr2585UU8rI2WUTBbyQanSU9pXIJi17kVUUeLb_LBGNNgpG4kOtZQNSp0SwW3rncv7CEqKe1Eo-ltn6bss2nZvooc8jfyp0FowI68gvtO1B7vRJmcCJfvVC1z6LWqKaeWfcpxZkfq9ea3CKs2mtmr8bcWcr7ORX74y2oQHpJsoSuBByEHCFJiF2Yd0VIcRaxmmzyM_A3T3zdszclzyv1DRMeQE1lCe2LKodjMAXFNUeQKXqjmEwcE8FyLFRsTXFwDr32xfhMgCRoErYq1HC6C0jsMpwQEHz7Ipwq2BE3zGGpx52JKefIJgHDsPqZN1MofmdgrQiS-liHfl8ypBYnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این قیمت های گوشت، همه مان باید بزودی به هیات مذاکره کننده پیوسته و گوشت الاغ مرده بخوریم.
آبش را هم بدهیم میساکی بخورد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18822" target="_blank">📅 15:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی قرارگاه مرکزی خاتم‌الانبیا:   زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18821" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک تانکر نفتی در بندر بصره در عراق مورد اصابت یک پهپاد قرار گرفت و تمامی عملیات بارگیری نفت در این بندر به حالت تعلیق درآمد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18820" target="_blank">📅 13:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYZCN9N-GKfSb4M92odNlJny3rMrB0JgyaMSkYPVlgrTFXEmXP7HMJecQTGHsKziHutS-QrC6Jy8JHiJYAHoj4ty6IvUcIlDYu9coO39u5ZvSrfBApxOUN9RFx6uyCX9JeQjxzEdZducGegUoTADjig4D7HLI9mXTLmOHYdvVU5Np-StdYyEi5WcuCTmuf8UnuL_6zOI6s0QKhdvplqS3bBvuIgfrQy9KLEt8h_MAAw3kbr2HUQqL6S5JZIjfo5qMpD68Cdr1Y4Psolj6GfcG0arfLTrYlPXxSlDY8hsL2EZQEIqOuEojRt7u6qoRetNI7X6bG_NZTH9kOCKY74_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی است و پیش بینی می شود شاهد جو ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18819" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18818" target="_blank">📅 13:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18817" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این امر روی بدهد، سپاه گزینه آخرالزمانی نابود کردن تاسیسات نفتی منطقه را فعال خواهدکرد.  البته همزمان ترامپ گفته که ایران خواهان توافق است و این ور هم سیگنالهای سازش می فرستند. روزهای آینده مشخص خواهدشد.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/18816" target="_blank">📅 11:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام:
موج جدید حملات ایالات متحده علیه ایران به پایان رسید
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (CENTCOM) در ساعت ۹ بعد از ظهر به وقت شرقی در ۱۵ ژوئیه، موجی از حملات علیه ایران را به پایان رساند.
نیروهای ایالات متحده به مراکز فرماندهی ایران، سایت‌های پدافند هوایی، توان موشکی و پهپادی و تأسیسات نظارتی ساحلی حمله کردند تا توانایی ایران در تهدید دریانوردان بی‌گناه خدمه‌رانی در کشتی‌های تجاری در حال عبور از تنگه هرمز را بیشتر تضعیف کنند. سنتکام از مهمات دقیق برای هدف قرار دادن اهداف در چندین مکان از جمله بندرعباس استفاده کرد.
اوایل امروز، نیروهای آمریکایی در یک موج ۹۰ دقیقه‌ای به سایت‌های دفاع ساحلی و موشک‌های کروز در جزیره بزرگ تنب حمله کردند.
ارتش ایالات متحده در جهت فرمانده کل قوا، ایران را مسئول می‌داند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18815" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آمریکا برای احیای خط لوله نفت عراق-سوریه جهت دور زدن تنگه هرمز فشار می‌آورد  واشنگتن در حال هماهنگی مذاکراتی برای احیای خط لوله نفت متروک عراق-سوریه است تا مسیر صادراتی امنی به سمت مدیترانه ایجاد کند که نفوذ استراتژیک تهران را تضعیف نماید.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18814" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18813" target="_blank">📅 10:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟   درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18812" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18811" target="_blank">📅 03:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: ایران یک شهروند  امریکایی را آزاد کرد، متشکرم!!
«ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود به‌طور ناعادلانه بازداشت شده بود، اجازه داد تا آن کشور را ترک کند. او اکنون در امنیت خارج از ایران و در شرایط خوبی است. ایالات متحده آمریکا از این اقدامِ مبتنی بر حسن نیت ایران قدردانی می‌کند!»</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18810" target="_blank">📅 02:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کما اینکه خراب کردن چیزی خیلی ساده تر از ساختن آن است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18809" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ونس :   با توجه به سهولت هدف قرار دادن کشتی ها با پهپادهای ارزان قیمت، امنیت ناوبری به تنهایی با استفاده از ابزار نظامی بسیار دشوار است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18808" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ونس :
با توجه به سهولت هدف قرار دادن کشتی ها با پهپادهای ارزان قیمت، امنیت ناوبری به تنهایی با استفاده از ابزار نظامی بسیار دشوار است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18807" target="_blank">📅 02:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده با قاطعیت پیشنهادی مبنی بر قطع ۳.۳ میلیارد دلار کمک نظامی به اسرائیل را رد کرد (۳۱۴ به ۱۰۴).</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18806" target="_blank">📅 02:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">7 جوان ارتشی پرپر شده در حمله دیشب آمریکا به سیستان و بلوچستان!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18805" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKIUbG3TIhGBRrnPxwqY588k3ViqQJiKkXVKFyQlSaRjP8-KVBIo37o70O2zWtbABBNyGPlx8D05ED-U37eir6P3x3lvWNmhArvimeQpPYWjt6QGxu6_JSshNOe1Y17pBdzXdk3BHxr_x1E6b4Y6frcYD8xy3prIi4Zbp9V0SvKkegi4B_4e7YKZngi5JCFQEcwLxAp0feTsmAPtZgxcPLZ1JwF0NZ75jf1nRhIktYWzErAwjyiVl3cVlg36y_HmL3BZNkrAxOEroyjBxTeY--m-ABnw0xZBjLxtxUgzGSvyoaHDzjjOgkJWPEq3ResG-obgFC1V-BjIW0x-7rcQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
💙
💙</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18804" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جی دی ونس:  اگر من یک انسان باشم و با یک روح شرور روبرو شوم، شاید فکر کنم یک دیو است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18803" target="_blank">📅 00:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18802">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جی دی ونس:
اگر من یک انسان باشم و با یک روح شرور روبرو شوم، شاید فکر کنم یک دیو است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18802" target="_blank">📅 00:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18801">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:
ایران به زودی شکست میخورد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18801" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18800">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آمریکا به عنوان «پاداش» حمایت از جنگ علیه ایران، به امارات متحده عربی دسترسی ممتاز به فناوری پیشرفته هوش مصنوعی اعطا کرد.
ابوظبی اکنون می‌تواند فناوری پیشرفته‌ای را خریداری کند که در دسترس هیچ کشور غرب آسیا، از جمله اسرائیل یا عربستان سعودی، نیست.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18800" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18799">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">محمد مرندی:
در همین حال، اردوغان همچنان نفت ارزان قیمت باکو را به شریک تجاری خود، نتانیاهو، منتقل می‌کند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18799" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18798">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دیدگاه ونس درباره اسرائیل:
من فراتر از کوچک‌ترین شک می‌دانم که افرادی در دولت اسرائیل وجود داشته‌اند که سعی در تغییر آن سیاست داشته‌اند زیرا می‌خواهند عملیات نظامی را ادامه دهند.
برخی افراد در سیستم آن‌ها، فراتر از کوچک‌ترین شک، وجود دارند که دستکاری کرده و سعی در تغییر افکار عمومی آمریکایی دارند تا جنگ را برای همیشه ادامه دهند.
دوباره، نه به سمت هیچ هدفی، بلکه فقط برای همیشه.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18798" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حملات سنگین به اهواز !</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18797" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18796">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سنتکام:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات خود را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند. تنگه هرمز یک آبراه بین‌المللی حیاتی برای تجارت جهانی است.
ارتش ایالات متحده در حال محاسبه مسئولیت ایران است، طبق دستور رئیس ستاد فرماندهی.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18796" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله ایران به اربیل</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18795" target="_blank">📅 22:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قبلاً هم گفته ام که پیش‌زمینه سخنان دونالد ترامپ درباره «تهدید کمونیسم» را باید بیش از آنکه در واقعیت سیاسی امروز آمریکا جست‌وجو کرد، در ادبیات سیاسی محافظه‌کاران این کشور و تلاش او برای پیوند زدن خود با میراث رونالد ریگان دید. از منظر علوم سیاسی، کمونیسم…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18794" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18793" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم  باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم  محمدباقر قالیباف در بیاینه تبینی خطاب به مردم عزیز ایران:   این روزها که دوباره آتش…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18792" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قالیباف:
باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
محمدباقر قالیباف در بیاینه تبینی خطاب
به مردم عزیز ایران:
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد.
لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18791" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWi3kw-KzCquRsKizgzJ3PVb2HScSdylnRgPt1w_w7KNXhfUNMfDQFT-9Ax8D1KriiNhTenv0kRuVs8e4xr0IpoS5sP5WJCG833zovW5t4AhWoXu9MNttzVOdZLaE1Ha7vROL0-lnkeqxxLzw742dQMYnioT_JHbsiNDSP2Mj5tjAAdJtobhc4SsGFTNga-KyZhJLYCS40jemvmQBBgszE13-T6z0vXJQ8mmKwnFeCYRHcx8HMSYZVujZ44crpJFYsBlg7TsGdDGiFi8N6icmfUpIWIzmqjKqLndW7c6DxJKpgir2GWNlzCRsVTgUyDUVMbmycNoBM7gAQDTIRX71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18790" target="_blank">📅 20:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به گزارش یک مقام ایرانی ناشناس، ایران یک پیام خصوصی به جِی. دی. ونس، معاون رئیس‌جمهور، ارسال کرد و در آن، جارد کوشنر و استیو ویتکوف را به سوءاستفاده از اطلاعات محرمانه حاصل از مذاکرات بین آمریکا و ایران برای کسب منافع مالی و انتشار اطلاعات متهم کرد.
دولت ترامپ به صراحت این ادعا را رد کرد و این اتهامات را نادرست خواند.
منبع: Drop Site News</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18789" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS4T7ZgZ7_1UVIRbifuVSeWvvItUV1jP_gYR_WsJTG072BFBy2tqt7HYFyZY6NX4I1SxTceLaxWSno7XalKVINmRiXy8cCRwgV-b_cLio_jtAZajx3WbMNBDgJ6DbUfEnHOFPKxnlNE5LdAjsq-34e6FDy63udHSknidn9XgjaenkQ94HLkLY3-QDUZcGq9Mdcia-c7DXpgvsY1R2FWdvuWvFarF1L3895cLs6nsUk97rM85Gl0IzpXMRF6fOsc2FPWSUFkLnbucRrv8mbCAKA9sCxQPFYcUDg3-AfFQ0GKJ07-aucH9JgZWbJbHEq0j5-ZHTbcfmMNwbyLxNrYerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:   چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18788" target="_blank">📅 20:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNIM-K4dfGincAZgP_vInPrGeSUfLRvILeWW5ThCd0wSyC0G4obucOSGjj0gWPhWdFa-JkhhjQ2f0WhmeC7fk_FB3v-1gancEbtmFT4t7UaaR2LXQea3VMh_j7zPOoqKRH_wg3rbqlAHCGFLMKJ-OaxYZytOGzwufygj-ApHUmS02PV91zTks-C1QotY0bwAlvYyIkSpF0-fr6bN2puMJk16xK4dnSv1koj0CZTNzdAqRf2D-guS8DxoBtFCy53LtnqV7K38F6Z8-uipXzrYB-6EXoKdUsog58lmhBDS5kX0ZhlRi0f-1vVBey5clMqBOXlBy7xhoq5omDPr_vUPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18787" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله به کویت</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18785" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک تبعه ترکیه مبتلا به اسکیزوفرنی در مرکز شهر درسدن تصادف کرد، اما هیچ‌کس را نکشت یا مجروح نکرد. پلیس آلمان به سمت او شلیک کرد و او اکنون در بازداشت به سر می‌برد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18784" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18783" target="_blank">📅 19:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">و از این جالب تر این است که نسل کشی یهودیان توسط نازیها در جنگ جهانی دوم به کلی الهام گرفته از نسل کشی ارمنی‌ها در جنگ جهانی اول توسط ترکان عثمانی بود.  اسناد بسیاری در این حوزه وجود دارد.  حالا نوه آن خونریزهای نسل کش آمده از خطر نسل کشی می‌گوید!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18782" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران:
نیروهای مسلح جمهوری اسلامی ایران نشان داده‌اند که هرگونه تجاوز به خاک ایران، قطعاً با پاسخ متقابل مواجه خواهد شد.
در حال حاضر، برنامه‌ای برای مذاکره نداریم و تمرکز ما بر دفاع است.
موافقت‌نامه همکاری، مجموعه‌ای از تعهدات متقابل است و در صورت نقض این تعهدات توسط طرف دیگر، ما نیز از اجرای تعهدات خود خودداری خواهیم کرد.
این یک اصل است و در آینده نیز از همین مسیر پیروی خواهد شد.
منبع: تسنیم</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18781" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18780">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18780" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو روز یکشنبه به ایالات متحده سفر خواهد کرد و روز دوشنبه با ترامپ دیدار خواهد داشت..
روزنامه "هایوم" اسرائیل
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18779" target="_blank">📅 18:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18778">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18778" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18777">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.  تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18777" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18776">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihc2z7eU-gr_tUoamY6elOCiW_4dtbQa5k5W28b5I-nEQX3AirQ2d_hN_9UQOV4Kn3H24MqqVsdHsjAuZOtWonelWHE750f6gevAhTIqGceLE9zIz8vsBHI5teKMxtQ5ZoRztwnCGbbgpYxqSqrZmJL45sHPv6MxSBv9YTmGKCir5DHRzg3OexkGbLWekWK1gOWeBi_UBmM-trGFHF-TN02bktdwvLq0DsGt2qGjBVfAgrNS18kMAnpomKaqAyN0ZwHLri_wECl_lJ6g0YAdlkBAaP5UORvQtczRysUP2pHMLrckcviG8H8BPzGAV0Coo-cZdvkFM-BnR2zFwIDdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.
تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18776" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18775">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18775" target="_blank">📅 17:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18774">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18774" target="_blank">📅 17:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18773">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ولایتمدار، عضو کمیسیون امنیت ملی:
به‌زودی دولایه از مسئولان آمریکا و اسرائیل را قصاص می‌کنیم
مردم نیز خود را برای تحمل شرایط سخت آماده کنند</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18773" target="_blank">📅 17:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZipm1uRJiXlH6Aa2bS0rdWAq1wZWNM6fdgBPgzDxqOtOAY7rIiVKNOwyB5GIGnxINfaPvSIKAO-hcB7uko5LVaLEvmWXhu_MdTfdV8iou9c6t3zBFi7eue9s6EhiCYRgfy032WN7omQ1NP5mWX9qszEhkzwKIBjY7NmRqWMsGZqbFxnZ_QDh0XptTgv-KKA_pyzDJdVIrvH1c9eQli4bQLKq6N2hm8tAbjEyXm-wqwkyrpD7gI5MqPSpEWjOG0RdYH_d0q4qJWocZNZD96aOtYKU9sLAZoiwJXM5D7Ouws4jWQ7XEjjWyNnf7csktw9VNMe8WFTY8YSB8iC472xVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBzYggk_IHslmpyOrqYWVF_MTpxZJgu3HEauKRjFe59aoZl6qKyAj6Pn30ttYlusCYBsTWX9BftgmWqfRE6KNO4P2dNtVDKEFg1VkOTTXq45UnqiBez6QOfrCC7IS6l5Ha-yaeenZTJ_z841pbo2VCTLDq98PDfpvdUSNHRqsYd4rMM9l06FWRj9se4FIqS1rdHL0-v4TFPqP053BM8ULlC5vEVC32TwFxtDj1FELCdQIwdpMhmyx6JanyZ21WO6ba0vouAQpkxGFYSK9WXQ2OY_sXAOMwA-d_QcclvlurZDuQN3TJ8IrMACbQDGxn3QdtdCyA9OKqJEYFkutU58PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک نشست امروز با نیما  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18771" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18770">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_rMiuK3AfLd3nA9FT1gbGIhjDr8_uH2ujQ6MVyKoox7sdGqt4T9YFUAZihph-J3WCeHIC8nWg1WhsdkanLEFBPxccanpBhgeFjk6rzHe9FPB9wKqYhU5Dmphg1xNCVvM4U23WaZttrdRK_fwy0MyNq-xNayQd9OYFWnaqUvWRoeXg-d8VGhh9scOTlx-G7ScWYfe3oHWzR1MkJXz5ukjGHNJAiN7sw_YGPpTGWYRaa9DC7nS4GWTLSFMfKDbnt68YcYUHZrafj3JeQqUdOROwBYomUYEgtRmhf9YWtFB5I4xTmS-ljmvWWK7QMfTqnAs5Yua9gQ3a05u6FH79Lo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک
نشست امروز با نیما
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18770" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18769">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8rKjKhgSattFwzWTdrH3jDpqYrjYrTG0w3_CgiH3HLL9caRh-2X-PVuXqZpBB3g29YX4FjDiV1DT7fpvW-i23lBhXfBLe8EwDwqJZQfN_gyLCufSmzwFDBdPVOKrQOggQ03l5kaHAg285b6BCO9k5Eoc14Ok9Yydg4-vtlzb2P-tt1e3iZJZc0m0y9mY2f-uR-K4Br-r0xJ685dIF9Vg6ik5FD_mGqHNZqPuuYDBpc4Fr117DgLldntY1f9VlfrJm7GiSHV885GNq6iU84X0f31ei_T3L0Q_rO7UH5I_7f-J5xQsZLOpUknyq4ikrcfxfPKTxJ6EI0xmTKp0WDOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خریدهای تسلیحاتی اشتباه ارمنستان — بخش ۱  این تحلیل توسط یک کارشناس نظامی روس نوشته شده و لزوما همه اش مورد تایید من نیست.  گفتن اینکه وضعیت استراتژیک ارمنستان نامطمئن است، دست کم گرفتن مشکل بزرگی است که ارمنستان با آن درگیر است. این کشور کوچک عملاً توسط دشمنان…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18769" target="_blank">📅 14:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18768">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار در شیراز !</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18768" target="_blank">📅 13:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=vh2hfdXYzRgiR-GLcy8Yj-ZWpfLxSZMD09DC48XO3be-VS-PgjnSPHQS5xGmktPkD4_j4MxdFzzBHn8Kx5OY8ZwgZdDcnQse1BWgAkUhjhXMsFQSlr0cYdlKDAEL_c6t-h3WODFQay1Cc0IN0_WxVga0oX2gvZGWQlxEgYmB8XZ__6VKtsjNgopdNL0fCx7C1sx9OVn4KufjoxNsgZTUj4qahOptdk-GD0D_QGNngP3Kw4_luOtcEg_bmW5nwvB-ss1ITA7JLP6bXqA4gysRFw16tO5WIRkJbFclq9TYoFQEKl3djgpBam5gWXJXx_UOyaUGf_3jTb6pCR2RyHEbYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=vh2hfdXYzRgiR-GLcy8Yj-ZWpfLxSZMD09DC48XO3be-VS-PgjnSPHQS5xGmktPkD4_j4MxdFzzBHn8Kx5OY8ZwgZdDcnQse1BWgAkUhjhXMsFQSlr0cYdlKDAEL_c6t-h3WODFQay1Cc0IN0_WxVga0oX2gvZGWQlxEgYmB8XZ__6VKtsjNgopdNL0fCx7C1sx9OVn4KufjoxNsgZTUj4qahOptdk-GD0D_QGNngP3Kw4_luOtcEg_bmW5nwvB-ss1ITA7JLP6bXqA4gysRFw16tO5WIRkJbFclq9TYoFQEKl3djgpBam5gWXJXx_UOyaUGf_3jTb6pCR2RyHEbYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18767" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18766" target="_blank">📅 13:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18765" target="_blank">📅 13:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX5y3XEdjj-wXXupJzFo2f78O8GuNxUbYrWYsmkeb2Bk6Mzt7l4YxtijAZSzp49V2DdwfDUKU5lSC3GKMyDerPRKCG5Q_A9Fn56_WVQoMd3nGINmQA7qeNUFAYX9Jg3Xo8cMw9jAKBAe_hSN_bIetli3RaWkLrBrm2JHxHTS3C2gfaR6EYZzqL3HnY8Q1ZH5vDJjta1gQUuPa3RjgZlseMKXPpPQ2zXthYZiE_kRzNZO5SCbpC9u7yV719Zra_QzWulujUiYd9WwDGjS_B7ztPp0Xlr6aPHeE3dbXBw6rJZ6W2rUgrNEE_yQ8GBxuwA38RaWYrr_09NnaoRS7ssYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.  وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18764" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.
وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:
"اگر جای اسلوبودان میلوشوویچ بودم، در سال ۱۹۹۸، پاکسازی قومی را در کوزوو انجام می‌دادم. این سخت‌ترین بیانیه‌ای است که تا به حال بیان کرده‌ام."
وزیر کشور کوزوو، ژلال سوهلا، دیروز گفت:
"من تصمیمی را امضا کرده‌ام که بر اساس آن، سِنیژانا پاونوویچ، شخص ناخوشایند اعلام شده است. ورود او به کوزوو و عبور از خاک جمهوری کوزوو به طور دائم ممنوع خواهد بود."
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18763" target="_blank">📅 12:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دقیقاً چه مدل آمادگی مدنظر هست لطفاً قید بفرمایید.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18762" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18761" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محمدجواد لاریجانی:
مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18760" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6S3bu8UMFz2ZsiZ0QuV3zCLfBZgrc8PkaM188EpJItL-rxyKdgD0NN87XH-Rdp3a4-NXrFM9QkwjU7TqmVcJxauQ_zP-cLhEi6fRFwfH65juPlGcANSFCtQx6ZyNiMqNOZnWmdEapZlfjz5L6qh1fER8OGJ4oasnZqRjiuVoVQinBz8DTFJQefENcC4aTbfLwzoKVhj0oh_6G5lus5nGuodWQ5jE0kqhlTsG1MPXhvv7kGg9wqDTFEsD_xuYRJ9eiC5y1Ti-nrUP8d6G919D8PTQgB26vSXw79pXSlXr_uU_KAmeGxl5U0biziC96zoXmAAHzhu2VbES2R7SVf59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18759" target="_blank">📅 11:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔔
#دلار
تهران =
187,000
#تتر
(تومان) = 186,340</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18758" target="_blank">📅 11:50 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
