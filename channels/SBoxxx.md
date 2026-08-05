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
<img src="https://cdn4.telesco.pe/file/tqyhFWbbFealMpAGLaPtF0jGNDZNsBE08JFt1MLrt2JZh9TOdfEUCeya_PEQwv28cEkVymAVgkQcohZ-Gm6poGs0pBzJemw6KM1_AlLF98WFeZrwPvBk744aguV6q4_Li7jhZiDO9mGHCSZ0mr1FUMc8JRrp4pBDcvEksQO1GLiM1UWvYhlh4d8WHZx82krFEW6yPMrsKUGMYXnw7hF5sQQtv91-csJsLalvVWuQtCAE6pd_roKiiW2sLL1C7JdcLvzWEQ3LyTF5sd4u3HKm0ju8Kr9hPO0quwkI7ESi1jwt-qaEIxZx_0Zglsd_AajL2Z7H3Gg5vfovpV0HI92F2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حادثه دریایی جدید در دریای سرخ</div>
<div class="tg-footer">👁️ 349 · <a href="https://t.me/SBoxxx/19692" target="_blank">📅 15:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">422.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 19</div>
<div class="tg-footer">👁️ 506 · <a href="https://t.me/SBoxxx/19691" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19690">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 19</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19690" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 19
چهارشنبه 5 آگوست 2026</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SBoxxx/19690" target="_blank">📅 14:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ژاپن در حال بررسی ادغام سیستم‌های هوش مصنوعی ساخت آمریکا، از جمله سیستم هوشمند Maven شرکت Palantir و Lattice شرکت Anduril، در نیروهای دفاعی خود است تا فرآیند تصمیم‌گیری نظامی را تسریع کرده و همکاری با نیروهای آمریکا را بهبود بخشد.  برای کاهش وابستگی به فناوری‌های…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SBoxxx/19689" target="_blank">📅 14:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmMKmqhwp134hK89Tpgywj3j6tU9TlQ60ps3e_oct52SrDiqg8_cQengurMgkFqHH1IAyebm_bI8KY6xFQ_IwoIpPmB1JTyFubXihqtjonM34FlMv1MWvf-rBe3ljzRhmDcJzySVpdre6H2cuZVLMS-o-jY8io8T_x9bi7JeHIj6VVoRbSHbRDQR4CltPB-PJuZnsh5bfD4hEMgFZ1MLzcBYMfiR5kaiXfBwTu-mRre--7JaKD2Hnq5fIs50ndNfQNr2_M1vi-eMxxKZ8WiYJ6QeuqZ1d64GkzY80q0Z-Dd-I46aLBVnv3RiQcmDe7-V2yprb8OeTacGa41vn01eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/19688" target="_blank">📅 14:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش صداوسیما درباره مذاکرات بر سر بازگشایی تنگه هرمز:  "توافق احتمالی ایران و عمان درباره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد؛ باز شدن تنگه هرمز منوط به تغییر رفتار و تصحیح تخلفات آمریکا است و در صورت ادامه تخلفات…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/19687" target="_blank">📅 12:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صداوسیما  به نقل از یک منبع مطلع:  توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/19686" target="_blank">📅 12:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترور ناموفق ترامپ!</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/19685" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صداوسیما  به نقل از یک منبع مطلع:
توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/19684" target="_blank">📅 12:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfGdhSbuAVA6_mvR3uV90E82Nk2Jj0kRmrvllT6JypB1n0VgEK-kQy62ZUbR3_QnaThqa-5axNoPQJ8APOBDDdS37l6lz7efumIj3mIv89sgfvS3RblWBkDe-PDNkeeG6h2Z40kyXYX8HR0MTjXuyRuctLttjygAvcI4UV2fJmraEHw7BaruUBdY8xhan5p1oGdtlfapHd54UTe9-x-YCsJdYY6_Ft_KKeHGPdoaM2KqR-jK8b1v0VO8cbOWKwZMXqz5NFyMEaUXoHgDxSyrE06YbUoF0q95BA8vQlvpoeFEwweEjZ0PmkW5zNt8AqB_4NaJod7X9zbLdbLqR5dp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح پایینی قرار دارد و ادامه جو ریسک پذیری پیش بینی می کند.
(شخصاً با توجه به اینکه:
— عمده رشد امروز در سشن آسیا روی داده
— پس فردا گزارش NFP داریم
— اعتمادی به توافق ایران و آمریکا ندارم
اینجا خریدار نیستم و پله ای می فروشم)</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/19683" target="_blank">📅 11:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حوثی‌ها مدعی هستند که با موشک‌های بالستیک، تانکر نفتی سعودی به نام «وفا» را در دریای سرخ شمالی، در نزدیکی ساحل ینبع مورد هدف قرار داده‌اند و ادعا می‌کنند که اصابت مستقیم رخ داده است.
این هشتمین تانکر نفتی سعودی است که از زمان آغاز محاصره دریایی در تاریخ ۲۲ جولای، مورد هدف قرار گرفته است، و حوثی‌ها مدعی هستند که ۲۹ تانکر سعودی دیگر را نیز مجبور به بازگشت در دریای سرخ و دریای عرب کرده‌اند.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/19682" target="_blank">📅 11:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLibokS_gXVvFgwM-YLROsX8ZE_Au8U_d1zAiFgLHuiWST9zmTaYeQTMc4PxCgG3FOQL3q99j_Q1P35iiOvQiYMl1QVV4wgTIEY89SQzdpVcdpPEbKDrmOmuFaSpTCnEeZNce2L7X94XIaE4UnuEj4ac-GzPP7qiAjsWPycOqVQexdxOiAhnBOlkd34XIlEA70BRJb2gnM_BAGC-e0hExFPAkVaTsUyXfxt-bwaOCuIYWjgL-Fqvt6iAxS5zI4PeiH7nDXer4JVcTFHpelh0MmLxw0M-pTWZ-fjjWxLQWdGROmC6GPmKoVh1SXsxq6kLEfCYUlPzljw30hFgTnrEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدید ایران برای قدرت هوایی آمریکا
خرید موشک‌های شانه‌پرتاب چینی توسط ایران و پیامدهای آن برای عملیات‌های آمریکا
چین در حال ارسال ۳۰۰ تا ۴۰۰ دستگاه موشک دفاع هوایی شانه‌پرتاب (MANPADS) از نوع QW-12 و FN-16 به ایران است. این معامله که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود، قرار است طی هفته‌های آینده از طریق پاکستان و به صورت هوایی یا زمینی تحویل ایران گردد. این موشک‌ها، با هدایت مادون‌قرمز، قادرند پهپادها، بالگردها و جت‌های آمریکایی را که در ارتفاعات پایین پرواز می‌کنند، تهدید کنند.
هدف اصلی ایران از این خرید، بازسازی دفاع هوایی کوتاه‌برد پس از پنج ماه حملات مکرر آمریکا و اسرائیل است. این حملات، آسیب‌پذیری‌های زیرساخت‌های نظامی ثابت ایران را آشکار کرد. موشک‌های جدید، به ایران اجازه می‌دهند تیم‌های سیار و پراکنده‌ای را در اطراف سایت‌های استراتژیک مستقر کند که امضاهای راداری بسیار کمی دارند و شناسایی و نابودی آن‌ها دشوار است.
از نظر فنی، QW-12 با سر جنگی ۱٫۴۲ کیلوگرمی و برد ۰٫۵ تا ۶ کیلوگرم قادر است اهدافی را در ارتفاع ۱۰ متر تا ۴ کیلومتر درگیر کند. جستجوگر مادون‌قرمز آن می‌تواند جت‌ها را در فاصله بیش از ۹ کیلومتر تشخیص دهد و احتمال نابودی در شلیک اول آن بیش از ۸۰٪ است. FN-16 نیز برای درگیری کوتاه‌برد با پهپادها، بالگردها و هواپیماهای کم‌ارتفاع طراحی شده است.
این معامله، علاوه بر توافق قبلی ایران با روسیه برای خرید ۵۰۰ پرتابگر وربا و ۲۵۰۰ موشک به ارزش ۵۹۱ میلیون دلار (تحویل تا ۲۰۲۹)، توان دفاعی ایران را به‌طور چشمگیری افزایش می‌دهد. چین و پاکستان این گزارش را تکذیب کرده‌اند، اما دونالد ترامپ اعلام کرد که چنین ارسال‌هایی مغایرت مستقیم با قول شی جین‌پینگ دارد.
آمریکا در حال حاضر با کمبود پهپادها مواجه است. از آغاز عملیات در ایران، ۳۰ فروند MQ-9 Reaper سرنگون شده‌اند. با در نظر گرفتن خسارات جنگ یمن، آمریکا یک‌سوم از ناوگان ۱۳۵ فروندی خود را از دست داده است. خط تولید Reaper در ۲۰۲۵ متوقف شده و هر فروند ۵۶ میلیون دلار قیمت دارد، بنابراین جایگزینی آن دشوار است.
این موشک های دوش پرتاب نمی‌توانند هواپیماهای بلندپرواز را تهدید کنند، اما پهپادها و بالگردهای آمریکایی را در ارتفاعات پایین در معرض خطر قرار می‌دهند. برای مثال، در آوریل ۲۰۲۶، یک موشک دوش پرتاب ایرانی به یک بالگرد HH-60W آمریکایی اصابت کرد. همچنین، یک A-10 و یک F/A-18 در ماموریت‌های کم‌ارتفاع آسیب دیدند.
این موشک‌ها، به دلیل سیار بودن و عدم نیاز به رادار، قادرند حمله‌های غافلگیرانه انجام دهند. آمریکا برای انجام ماموریت‌های ISR (اطلاعات، نظارت، شناسایی) و جستجوی نجات رزمی (CSAR) مجبور است در ارتفاعات پایین پرواز کند، که این امر آن‌ها را در معرض تهدید قرار می‌دهد.
در نتیجه، ایران با استفاده از این موشک‌ها می‌تواند هزینه‌های جنگ فرسایشی را برای آمریکا در ارتفاعات پایین افزایش دهد. اگرچه آمریکا آسمان ایران را کنترل می‌کند، اما ایران می‌تواند با تیم‌های پراکنده موشکی پدافندی، عملیات‌های آمریکایی را پیچیده و پرهزینه‌تر کند.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19681" target="_blank">📅 08:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به عنوان بخشی از این توافق که بین کشورهای ساحلی ایران و عمان در حال مذاکره است، ترافیک ورودی از طریق یک مسیر شمالی واقع در آب‌های سرزمینی ایران وارد تنگه هرمز خواهد شد.
ترافیک خروجی از آب‌های عمان «با هماهنگی با ایران» (یعنی با مجوز صریح از نیروی دریایی سپاه پاسداران انقلاب اسلامی) خارج خواهد شد.
این توافق موقت به مدت ۶۰ روز طول خواهد کشید، در طی آن هیچ عوارض یا هزینه‌های دریایی دریافت نخواهد شد. در عرض ۳۰ روز، هر دو طرف تلاش می‌کنند مین‌ها را از مسیر میانی تنگه هرمز پاکسازی کنند و به یک حل و فصل دائمی نهایی دست یابند.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/19680" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دونالد ترامپ
:
ضربه واقعی هنوز در راه است و امیدواریم مجبور به استفاده از آن نشویم.
آنها دوست ندارند این را بپذیرند، اما می‌دانید، کمی نگران‌کننده است. شما به مردم می‌گویید که ما مذاکرات خوبی داریم، و بعد کسی از ایران می‌آید و می‌گوید: "ما ملاقات نکرده‌ایم." این یک دروغ است. آنها می‌خواهند معامله کنند
سوال: اگر ایران دوباره عقب‌نشینی کند، آیا این پایان کار است؟
ترامپ: خب، اگر آنها دوباره عقب‌نشینی کنند، ضربه بسیار بسیار سختی خواهند خورد.
تنگه خیلی زود باز خواهد شد، یا خیلی محکم به آنها ضربه زده خواهد شد و تنگه باز خواهد شد. آنها با من تماس گرفتند و خیلی مودبانه گفتند: "لطفا، می‌توانیم صحبت کنیم؟"
سوال: چه زمانی می‌گویید دیگر بس است؟ و آیا راهی برای بازگشت ایران وجود دارد؟
ترامپ: من وقت زیادی دارم
ما کنترل کامل تنگه هرمز را در دست داریم.
روز خیلی خوبی بود. ایرانی‌ها دوست ندارند این را بگویند. آنها همیشه ادعا می‌کنند که ما در مورد آن بحث نکردیم. اما مردم فهمیده‌اند که این درست نیست.
اگر تنگه هرمز باز شود و به هر حال تا حدی باز است.
قیمت بنزین به ۲.۵۰ دلار در هر گالن کاهش می‌یابد.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19679" target="_blank">📅 07:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
گفت‌وگوهای بسیار خوبی با ایران داریم.
تنگه هرمز به‌زودی باز خواهد شد یا ایران هدف ضربه‌ای فوق‌العاده سنگین قرار می‌گیرد</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19678" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfkWK69jqK8_58Ysb4FceogcKf-WZtlCrROK4kSumauDpvLu0S0HE1LHj2lJq78zrAJ4AG6Kx6hDHASosCG8OdRf0Fk70xszU8FrZS_GXmr5_6Fvvbi09dMn_is7N_sIcOgbyiQYYkM2cNNSD_QuWrDyywxnduXKg8xaQZH0n1vHv-BPOAPDOLwKHCoNk4hlewrZY8U3FC_li4SjV-qFveXzuouO-1Ho_ubhG0s5H5nED-SWcUUNrwTyaDCMS7lbl0KqVr9CsyaJovim2_L5kS0I8TGaeJ8girNImp7n_1rZlzoLkZdnBBw4J-ObERhrHodfEAJF1Hbknd1ysMc7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژاپن پس از آنکه کشتی‌های جنگی چینی، به همراه یک کشتی روسی، در داخل منطقه‌ای که توکیو آن را منطقه اقتصادی انحصاری (EEZ) خود در نزدیکی جزیره اوکینوتوری می‌نامد، رزمایشی با گلوله‌های جنگی انجام دادند، به چین اعتراض کرد.  ژاپن اعلام کرد که این رزمایش طبق قوانین…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19677" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش ایالات متحده تقریباً ۸۰ درصد از پیشرفته‌ترین موشک‌های رهگیر THAAD خود را مصرف کرده است
سی‌ان‌ان</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/19676" target="_blank">📅 04:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شب های خواهرمیانه !</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19675" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملات هوایی عربستان به صنعا</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19674" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترور ناموفق ترامپ!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19673" target="_blank">📅 02:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات هوایی عربستان به صنعا</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19672" target="_blank">📅 02:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سنتکام
:
مسیر جنوبی از تنگه هرمز همچنان برای تمام کشتی‌های تجاری که به دنبال عبور از این آبراه بین‌المللی هستند، آزاد و باز است.
در طول سه ماه گذشته، نیروهای ایالات متحده به بیش از ۱,۰۰۰ کشتی در عبور موفقیت‌آمیز از تنگه، علی‌رغم تهاجم بی‌دلیل ایران، کمک کرده‌اند و این عبورها امروز نیز ادامه دارند.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19671" target="_blank">📅 02:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeXJni4klCH_xrbA3Hmmq4x5BSftnYWOr8EYn_zu-B-V6IrH7uYYXzWs3DPol2gGlQF6IGsFf7OvOWdJyR1rZgKnzspnuma7YqhaEovM5eUJA4FlNH-OI87zMRo8cYyUuSafzNDVnEPAeAo9QDUv5h5II5VypAhzANBewOWHdtUEV0iax0h83yvH2R3Ef_z3brrya7W8qPCqxJ_VcFyB4sY1yBZcBsTFXvF1rdNCwaNG3rtlj9NXDRqynhOCNGy9ofPCwN2fqiMYcVRYqN1luH1e_nALkekeO2F_bqi5pXDVGkvzBhk-19BhEBr44NYizunWOXSOYP08qosiOFrHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه های مهم دریایی جهان و میزان نفت عبوری از آنها
ابتدا تنگه مالاکا و سپس هرمز.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19670" target="_blank">📅 01:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19669" target="_blank">📅 01:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJyt_Bx4AhuNnw75McONMzRbMK9FUWyMcazCWpWXmun6e3ee2RnYRlNNOw59lqjnzmZaYdG72buoDsxazmmnAdsFU1uZUorQ_aDJGjJFXHlu13oScMQJbfKWimUrc9YcA8KXqupU56eJHa4xJiNuTBgcbN3CUWNKYleTRsweFvicUnUK_OXeRXU92Ctz6lyjXeTFg45z0WZV6E1IieoMMt2Otw7s47yNpviYO1MN8XmH3LlUmgjXeY_JE09b_jMeBQwtrmQ-Esdb-cVf3WsfOP0Jb5TJ_r1jS2bTQ5AOfK8AXbeZHy-9B1xyQhxAbSQ6pNysxuwbtJbAUEMpyCHEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19668" target="_blank">📅 01:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsR24huMKdYw3yQ3EFIQWWU7IUjXp6rnOvpQdHWv3wmbC3-EHjxmAVtCSSikOED8WxFhKGaPgIfxJf7LFYNSSbxOFm2_jNgelhccrGY3To-QEYKyKheYe-WefA-rsoY0mW1wKy24kqIkyQVuoxcy-VDKxjlAu4H_lgchF4q_zTipzEYU4pv0oZuXXG9hSb3dCnXrQWDorpOuZupMngIYF9FmViA2b0-oEPotmJlAHKQuNHRC7cDgfOVLcW3p9TPxNmeYDpCcuu5Isjqhyfr5ZYaOTAPtGuUnnoTo3s0LDXIJiJDHkN8gzLMj30oAReqzLRm5RkiJGa__wMzLHIUmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
احیای بخش تولید آمریکا شتاب می‌گیرد  شاخص ISM تولید آمریکا در ژوئیه به ۵۵.۶ رسید و رشد همزمان تولید، سفارش‌های جدید، اشتغال و صادرات نشان داد که بخش صنعت پس از سال‌ها ضعف وارد مسیر احیا شده است. با وجود این بهبود، فشار هزینه‌های تولید، اختلالات زنجیره تأمین…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19667" target="_blank">📅 00:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.  به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19666" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.
به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات جستجو و نجات را پوشش خواهد داد، مشابه مدل موجود در تنگه مالاکا.
این پیشنهاد که به گفته منابع از عمان حمایت می‌شود، می‌تواند یک راهکار قانونی فراهم کند، زیرا قوانین بین‌المللی اجازه دریافت عوارض عبور اجباری در گلوگاه‌های کلیدی کشتیرانی را نمی‌دهند.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19665" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr9PAgspaswUQvXCVxR_qkoss2rkGF11HjDd7t8-eD1xX5Uhi5QkJJZe0dAhFeQFvt-n_JQ9xjiSbbsVX3q1HX8BoSH42bz4MxDutLxQyFgGkf5RE2ptzy5_j68lT7RQO1kUbHCyO4GWWF6stwWJEIYvBxIS4nUtrPjbkM6sR0Ip9xMlUycseep5r7oHP1iyJEasjhqv788fHJyzepGO1JMfSjTxCv5OgHyoR8aAhzk5Oh2B4-jWqCNyA_m_IqxQP_KkTfF38kJe1PzJkHhD3qaUnT5xOIok37dipqlF9LThWMmrC2zOnBM9OdqciBcbTt5k8Mqmkx3yOt5vElBikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
سوپر اپلیکیشن بله بعنوان اولین لژیونر اپ های داخلی وارد اپ استور شد</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19664" target="_blank">📅 22:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19663" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19662" target="_blank">📅 21:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19661" target="_blank">📅 21:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19660" target="_blank">📅 21:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19659" target="_blank">📅 20:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbrIdRpwR9x82-IGNFjZKrdVckhpuws5yNu3woZVK1JBE6YzaIIodoFFzh7T_DzF8nbJKGNFxt0cagaOLTaEKcj6DX-O2OafJqvhwv0Q0GqeWsiXxfSX9FicqqcRS520u89rfvGTGgKOWWM28Z8tvjFjIA7siz4R7bDw6GMKSRiS_C-35jLt62Sujlxb5lS-4Nx-qyAotaYU1OcPm9dkRXcCy6M4JblvRyk866wW6547IPCVRsaYcLrPx8yvWTIF7MphBNPYyYQ-SNMUJLl9wp1IoH2HKYs9PP-UFJKm2b7qqeYWhpC8ajTlMh8rtUsqtV2Mjb71vqjCnxVIEJQrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19658" target="_blank">📅 20:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.
روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ دهد.»</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19657" target="_blank">📅 20:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایران در حال بررسی اجازه دادن به کشورهای اروپایی برای خنثی‌سازی مین‌ها در تنگه هرمز است، امتیازی که می‌تواند بخشی از یک توافق برای عادی‌سازی حمل‌ونقل دریایی در این مسیر و تسهیل مذاکرات صلح با ایالات متحده باشد.
ایران بارها به‌طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در تلاش‌های خنثی‌سازی مین در این مرکز حیاتی حمل‌ونقل نفت و گاز طبیعی مایع‌شده مشارکت کنند. با این حال، طبق گفته دیپلمات‌هایی که با این وضعیت آشنا هستند و به شرط ناشناس بودن درباره مسائل حساس صحبت کردند، تهران در جلسات خصوصی در هفته‌های اخیر موضع خود را تعدیل کرده است.
وزارت خارجه ایران بلافاصله به درخواستی برای اظهار نظر پاسخ نداد.|</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19656" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19655">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">غرق شدن کشتی هندی در ساحل یمن  به‌گزارش برخی منابع یک کشتی هندی در فاصله ۱۳ مایلی جنوب حدیده، توسط نیروهای انصارالله مورد حمله قرار گرفته است. این حمله با استفاده از یک قایق انتحاری انجام شد و در نتیجه، کشتی غرق شد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19655" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19654">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حتی وقتی کشتی طوری ش نمی‌شود، هندی ها تلفات می‌دهند</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19654" target="_blank">📅 18:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">العربیه : تا ساعات آینده بیانیه بازگشایی تنگه هرمز، رفع محاصره و از سر گیری مذاکرات اعلام می‌شود</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19653" target="_blank">📅 18:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">323.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19652" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 18</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19652" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 18</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 18
سه شنبه 4 آگوست 2026</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19651" target="_blank">📅 15:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گروه حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19650" target="_blank">📅 14:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOUMP1MrKmrhopVWosEiio_Ps43m-9-JKdJwLDMFmd70_LsxvMhWVc2Cs-XnDTvCyDtGMNXMqYNcczXTSum_z90qA11nQI7AZ8JHald_obO5TczHyv2i8ttodxGDT2MeNiP4jkxNWSYVHQXxMXgkZw4dnXawnaqcK48BWx8qNyaj8l3bPtpeBJ68OBLF07j9DZapORuJH6F4RXCFzy9L2MR7DSbw6FQMYlcYj5PwfsNx0AEsbHsK_qadLlT6CVDk_uXF-QKZovIfJs2aM5bEJzBxTrAfyifiwqWWV4O6McfiFHYBbAypm9Cx71Hvz2vAPrihlXACpc_-pYJqAV1-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnYPGgdSGQptZHXlGFi4KvV8z6MLP5g5l4ozGOXeU_knoSuPaDnEk15DdtFE7MHo3mBKGwASNXU_Cv2ggkInIFrB8dSKmrDV1iylcLfLjIH1UukyYmwXLQn6cbUrNWce9uwaiDiIsqzkDZSSCkekQF_c8qo6L2kEY1yg_MuWS_usbF350oOBA5vY8fzyfmrf4HAi7A-cn0cuZ81bmaFzheQkNQsqm3xpxBu1DZzQmDDBDW92wFO3gpZ13b36MYCPb4JiKCjljvCzEVrqDEByi9NENy7c_tNe9zf5cZvf5O1vLzkCardjzoRYKpFeiNR9ZkZhfYaT6k_6HwGars9aEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19648" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXd3SkVxJqL0SWph38RcD8Tk7ueKy7A20XeARXyTIkEIVHf7Syh7yihM8EdOq2k5eAJgHhV9oIpja17NDEzQ4k_5FWfkevua1ltZQoct9rTcAzJeERs8dCI9GLHWWTDNIRzYopT3HU7x5Dsp3uxuZOnRKzhKIyKlfMEL2rkvVjNGCi8MnPk_HZjswDMTT3wkgL3CmKpApPH7fK62hYSLJBpb9le_hVQcRt3msvDzlev2maRfjBdY89aGYYfjQugpjd7aKDl0VOdNPnfrG5sDpZUL3nzIOAky_D34rBAPP3EcWSKRYEU_mylvvGRpPHHgOkFra-_vPH6NcHQC5j5dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی به قلم « احمد کوچاک»
ایران روی اخلال اقتصادی برای وادار کردن آمریکا به امتیازدهی حساب باز کرده است
ایران در حال اجرای یک راهبرد فرسایشی حساب‌شده در سراسر خاورمیانه است و با استفاده از مسیرهای کشتیرانی جهانی و زیرساخت‌های انرژی به‌عنوان ابزار فشار، تلاش می‌کند اراده واشنگتن را فرسوده کند. تهران بر این باور است که افزایش هزینه‌های اقتصادی در نهایت آمریکا را به دادن امتیازاتی درباره کنترل تنگه هرمز وادار خواهد کرد.
تهران در حال اجرای یک کارزار فرسایشی حساب‌شده علیه ایالات متحده است و کریدورهای تجاری و شبکه‌های انرژی خاورمیانه را به نقاط اصلی اعمال فشار تبدیل کرده است. این راهبرد از رویارویی مستقیم نظامی پرهیز می‌کند و در عوض بر افزایش هزینه‌های اقتصادی و لجستیکی ادامه این تقابل متمرکز است.
رهبران ایران بر این باورند که می‌توانند واشنگتن را پشت سر بگذارند؛ به این معنا که هزینه حفاظت از کشتیرانی بین‌المللی برای آمریکا و متحدانش را آن‌قدر افزایش دهند که در نهایت پذیرش خواسته‌های دیپلماتیک تهران برای واشنگتن کم‌هزینه‌تر از ادامه وضعیت موجود باشد.
گسترش نقشه تهدید
عملیات ایران دیگر به تنگه هرمز محدود نمانده و میزان تحمل آمریکا در برابر اختلال در چندین گلوگاه دریایی را هم‌زمان آزمایش می‌کند. اکنون تهدیدها دریای سرخ، تنگه باب‌المندب و زیرساخت‌های انرژی عربستان سعودی را نیز دربر گرفته‌اند.
این پراکندگی جغرافیایی، نیروهای دریایی بین‌المللی را وادار می‌کند مأموریت‌های اسکورت و حفاظت دفاعی بیشتری انجام دهند؛ اقدامی که منابع غرب را فرسوده می‌کند، بدون آنکه الزاماً توازن نظامی منطقه را تغییر دهد.
مایکل نایتس از مؤسسه واشنگتن می‌گوید:
«ایران از همان ابتدا تلاش کرده است با گسترش گزینه‌های تشدید تنش خود، آمریکا را در این زمینه پشت سر بگذارد؛ به‌گونه‌ای که همیشه بتواند هر هفته چیز جدیدی ارائه کند: جغرافیای جدید، نوع جدیدی از سلاح یا نوع جدیدی از هدف.»
بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است.
چرخش به سمت دیپلماسی
واشنگتن در حال حاضر برخی عملیات تهاجمی برنامه‌ریزی‌شده خود را متوقف کرده و به دنبال امکان آغاز مذاکرات با میانجیگری عمان است. این تغییر رویکرد پس از رایزنی‌های فوری با متحدان منطقه‌ای، به‌ویژه عربستان سعودی، صورت گرفته است؛ متحدانی که خواستار کاهش تنش برای حفاظت از دارایی‌های آسیب‌پذیر انرژی در خلیج فارس شده‌اند.
دولت آمریکا در این توقف تاکتیکی، دولت اسرائیل را نیز به شکل محسوسی در حاشیه قرار داده و ثبات در خلیج فارس را در اولویت قرار داده است.
با وجود گشایش دیپلماتیک، اختلاف اصلی بر سر تنگه هرمز همچنان حل‌نشده باقی مانده است. آمریکا خواستار آن است که این آبراه به‌عنوان یک مسیر بین‌المللی باز باقی بماند، در حالی که ایران بر حاکمیت مدیریتی خود و حق دریافت عوارض عبور تأکید دارد. اما تهران حاضر نیست از موضع ضعف وارد مذاکره شود و با استفاده از تهدید به گسترش اختلال اقتصادی تلاش می‌کند برای خود اهرم فشار ایجاد کند.
ری تاکیه، مشاور پیشین وزارت خارجه آمریکا، می‌گوید:
«اگر قرار باشد مذاکره‌ای انجام شود، ایران شرایط آن را تعیین خواهد کرد.»
در نهایت، رویارویی کنونی بیش از آنکه صرفاً یک تقابل نظامی باشد، آزمونی برای تاب‌آوری نهادی دو طرف است. ایران بر این باور است که ساختار داخلی آن می‌تواند تحریم‌های طولانی‌مدت را برای مدت بیشتری تحمل کند تا ائتلاف تحت رهبری آمریکا بتواند نوسان دائمی در تجارت جهانی و بازارهای انرژی را تحمل کند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19647" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای انفجاری در شهر صنعتی شمس‌آباد، واقع در جنوب تهران، خبر می‌دهند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19646" target="_blank">📅 13:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1p-3pu6KYK7CqnWTJxZbzHKUzWe9LFuSndCCzG1Zepih4xsrrcRwnmm6zE94omg2DEexE1TvcXQ95c1xujg62QJqOyvNerQXY5NZVhnHlfh7I_7laOXEqYyhK1cbxX7xAoEakIBy_Sg07JdM9QXDhNf-nhfAwC7YEj7Ae3S7ISefVupagkxWGYS3iBvrjyzT2aCErFYZN2DIvUuK2aSSRicKqKxxVKw0smLsjSgWbOj_uJqD4Vopi8HX9H1PEIRjqJbCQggn4-_1DanLnRYeA2uUXOznCuKMqFNPyuQcxUe51wb4EZj67mkrMy4M6JZiapAcrZ1xOpVk7GL8OAZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال احیای صنعت آمریکا است و این مسئله در گزارش درخشان دیروز PMI کارخانه ای آمریکا بازتاب یافت.  یادداشتی در این خصوص منتشر خواهدشد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19645" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBZN1K6-9anNik2pUvzt7V3tNsGUxr7ctpt1QDbiyXXl6nt_vpb_P79uTmlkSt5DrPqfjO-tThL3OYs7eAgML_OeKwumcSQXQlUfLLqQJwlmIQJQlBrhXT8G0hXasLX8vQb9WkPTMR74KBG4Rj_A25eEbG4Wwpdv_1Qna5s8AfleAQPuW8NWF1m1Y4ssYvzaTO8aP1ZJEk6V2ytk4rCRMbB-7BfdxXOYnmi4hvLRD0O9XPfZaooz_KVDHcN-C25YL6Mg7AdcXrSOJijyeP0HQhv-umV12eR0arhhOeaUjYMAPfYqmfYK41PUegLFZlrvGGMwKTf_p2FUSgOIm_4A7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Geomarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19644" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULiDqIgiRyqZooitYEeeuXDo0mJr4nG2aYNYx5KyZqmk4_rf5iNH5esJgsAaBNpIEG1cBkWnhF6xbsPD-fBHV8ucq5TXx_oITRGDGD-6kRK7CMo1LzqSk4gLR9DCo8RRNyq99EvR_AmbluoqLxunum7LDxK0vOu4kw8eH42RgTHcZVtv6ZJacd97jaO7renusLQXIq8BUmtVQxY9OySaCL_RDFrRIRrbn7qbTPnMaPpOlT3KxtoCgNQQARnVroLHf3ll0M-Xa-xI7jJNyhWeBWXTajFFai8zOX93KVMWeMhkfadUfEe_JM8qiGIpaH3b701wvttx65ZocxDF6Uw0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19643" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qD8v6mK3bC3qNiNQ_uuxU_Tt-jStiJyoT7SNqR3qpLgdPiMhQEMDurv2vVoEe0v-dxFRIFlCpOq9PaBInkRPpve65VcKxp6wkA9E6VtBIYBDcWmu4zHPYyHFtEBS4p13VnrYd_qMXyzd1J7WwzANhw7D_LD9AbDEON8RLGtF8OPxaDzMIpIHj-iEF-rwo5szQGjRBkqAjTi1W7sxbjtSUj3zfi2qjdX8Zc7sLoMz5MHQQnMjDSdsEYC_fzCaNNmE9iAjmLHq40h_BZNce99vJYCWBderrCjUGq1cL0VlO6l33cSzRFMaGHDQ0U7Jop9-mfeUBTwuS014eDZt91poXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا بخش تولیدی اقتصاد آمریکا در دوران ترامپ احیا شده است؟   داده‌های اخیر PMI نشان از رونق و رشد چشمگیر بخش تولیدی آمریکا در اوایل ۲۰۲۶ دارد که می‌تواند ناشی از سیاست‌های حمایتی و استراتژیک دولت ترامپ باشد.  با این حال، این بهبود به دلیل کاهش اشتغال و تغییر…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19642" target="_blank">📅 10:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایران و عمان به توافقی نزدیک شده‌اند تا پس از ماه‌ها اختلال، مجدداً تردد کشتی‌ها را از تنگه هرمز از سر بگیرند.
مهم‌ترین مسئله مورد اختلاف این است که این توافق پیشنهادی می‌تواند به ایران نفوذ بیشتری بر این آبراه بدهد.
مقامات ایرانی می‌گویند که کشتی‌هایی که وارد خلیج فارس می‌شوند، از یک مسیر نزدیک به ایران عبور خواهند کرد و هزینه‌ای را پرداخت می‌کنند که بین ایران و عمان تقسیم می‌شود. در مقابل، مقامات آمریکایی این ادعا را رد می‌کنند و می‌گویند که ایران هیچ اختیاری برای دریافت هزینه یا کنترل تردد نخواهد داشت.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19641" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5mKiojRg_ihScpH60U0hijhWllxlFgr6s_aaocsdY4gYR17QEimj2qJFSr5a-laqnSwfN5gvgATwCG4Zf2hp1XFbwfL1dEF_OqfUXVFb-nhthXnn_0fnHS-duoAc1NBHb_NV6lc1FgUu4ui_MwJ50eKob82R6bya5qbGjX_womu-JtCHqeVOsjsF90mEG2UbPfEJa8Zi41JAqi9O2a8ZJGxxQBN1kgw0snbXEKIk8wcoKtNHWnzouU7N6R81ImNmU9BmfjKNtmo2llqv4JjYlzaapj7Yf-S1jwl9B38yMWU1obSm7S6CHWC3zHDOPGwcTkZeBPyDDbGKZxd8OqYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19640" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19639">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19639" target="_blank">📅 00:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0Yu16PPijltkxpXTz_7J549vf45QFvdJcKhwL-Vj_WjnLPWd2AFIsSJ3XdcxptzA2HINduLJTMedR-LKa1JZ9843b9nGrZAHT7tcXTNuMz5_SII7uGPoSK6V-BOXc7n52Zr3-jrmnTeU36rX-T3OW9MknJtj9mWY-lEST_OwLGV209Olimfs-5hV4XRG_4RwkL17ZpyzW9H5ElK953jOaKZHGdKpTGZo5AjHgppgfdil49UmmM3WqwQ7fiabTv0PL_505i1sNg57bUL8xzbnTyOhYQzQ4pCDgPL0yuQXV5bil5SKzW4Mj9DguKyOSR7i5ULChycRA9fCKZ-ec5bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  به نظر تارگت 2 را می شود دستکم 120 درنظر گرفت.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19638" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک منبع آگاه به خبرگزاری رویترز:
ایران در 24 ساعت گذشته حداقل 3 پهپاد به سمت کشتی‌ها در هرمز شلیک کرده است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19637" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در حال حاضر خورشیدگرفتگی روی نداده اما ماه کنار مریخ است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19636" target="_blank">📅 23:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19635">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ژنرال محسن رضایی:
در حال حاضر، هیچ آتش‌بسی وجود ندارد. اما تمام عملیات‌های ما هدف مشخصی دارند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19635" target="_blank">📅 23:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19634">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">برنامه داریم اسم جزیره قشم را بگذاریم آمریکا و آن را محاصره کنیم.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19634" target="_blank">📅 22:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19633">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ژنرال  محسن رضایی:   اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.  ‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد. ‎</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19633" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19632">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
ژنرال
محسن رضایی:
اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.
‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد.
‎</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19632" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19631">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ژنرال محسن رضایی:
آمریکا در طراحی چهارم خود علیه ایران تلاش دارد از داخل شورش‌هایی انجام دهند
کشورهای دیگر را هم می‌خواهند وارد جنگ با ایران کنند!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19631" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19630">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19630" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19629">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:  من اجازه نخواهم داد که ایران این عوارض را دریافت کند.  اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.  ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19629" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19628">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دونالد ترامپ در مورد چمن:
چمن مثل انسان‌هاست. آن هم زندگی دارد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19628" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19627">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:
من اجازه نخواهم داد که ایران این عوارض را دریافت کند.
اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.
ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19627" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19626">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">منظور کله زرد از «این» چیست؟! وقتی مذاکره ای صورت نمیگیرد</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19626" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19625">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19625" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19624">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19624" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19623">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سوئیس: ما در ارتباط با ایران و ایالات متحده در مورد مذاکرات احتمالی هستیم -
خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19623" target="_blank">📅 21:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19622">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPdYh0dsixQc2XIwY9GKuL8ZTfo1PUGYL8Jp4OaEC3DshXB6h-QEEMhxZ9VQTTRaO4eL9AWbgsfk5S9Le-uLIfim1fRTOE5q6o1VWctEw8KOgT4zEjY5CUKboTnrxNz0dtRJebkYsRXsVpfh0_1A2JiX4NhLVbZ3yrz6rCZDp6Ns5fKbRVAkSGxcm0RrtxjPSauVe_62hZavGAbYVVmQWBINLZhrlEvDzN46MXTZRgBmsRDMsDmaUkVqjaWcodQHKcCeNBnk4Lv8I82HDobeJJwdHADLWy9sbmOoCZg2uKz48gLtToo6OF2FvDzTPaZjvJYttjxgQiUjSnLKIKmMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19622" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ:
رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان نیست، هیچ موضوعی مورد گفتگو قرار نمی‌گیرد، و آن‌ها فقط با "عمان" در ارتباط هستند.
سپس، آن‌ها به سخنان همیشگی خود ادامه می‌دهند و ادعا می‌کنند که تنگه هرمز به طور کامل توسط آن‌ها کنترل خواهد شد، در حالی که در حال حاضر، این تنگه به طور کامل تحت کنترل نیروی دریایی ایالات متحده و "محاصره" ما، یا همانطور که برخی می‌گویند، "دیوار فولادی ایالات متحده" است.
هیچ چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ چیز نخواهد رسید، مگر اینکه یک توافق حاصل شود، یا ایران به طور کامل تسلیم شود. چه ایران این را بپذیرد یا نه، در واقع، ما در حال بررسی راه حلی برای مشکلی هستیم که آن‌ها برای دهه‌ها ایجاد کرده‌اند.
این موضوع بسیار ساده است: ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19621" target="_blank">📅 19:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پاکستان وجود هر گونه مذاکره ای میان ایران و آمریکا را رد کرد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19620" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تصویر نگران‌کننده بازار کار ایران.
بر اساس تازه‌ترین نتایج طرح آمارگیری نیروی کار مرکز آمار ایران، اقتصاد کشور در بهار امسال حدود
۴۵۰ هزار شغل
را از دست داده است. همچنین
۶۲۹ هزار فرصت شغلی در بخش صنعت
حذف شده و شمار قابل‌توجهی به جمعیت بیکاران افزوده شده‌اند؛ آماری که از تشدید بحران در بازار کار حکایت دارد.
﻿
همچنین مرکز افکارسنجی دانشجویان ایران (وابسته به جهاد دانشگاهی) اعلام کرده است که
معیشت بیش از ۳۲ میلیون ایرانی
به‌صورت مستقیم یا غیرمستقیم به پایداری اینترنت وابسته است؛ موضوعی که اهمیت دسترسی پایدار به اینترنت را در اقتصاد و اشتغال کشور نشان می‌دهد</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19619" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو:
ما باید روابط خود را با متحدان بیشتری تقویت کنیم.
به همین دلیل است که من سرمایه‌گذاری زیادی در رابطه خود با هند انجام می‌دهم، با دوستم نارندرا، که یکی از بزرگترین دوستان ماست.
برخی می‌گویند اسرائیل منزوی است. اما حمایت‌هایی که اسرائیل – و من شخصاً – در هند دریافت می‌کنم، واقعاً شگفت‌انگیز است.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19618" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو:
اکثریت قاطع مردم ایران، اسرائیل را تحسین می‌کنند.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19617" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Geomarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">324.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 17</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19616" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19615">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار در دوبی همراه با یک کشته و 5 زخمی</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19615" target="_blank">📅 17:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa3QtrLNKfcnbrp8DK0c7x-NucptGjiGjJCfXrYG6MPrj2Z3SZUzMImCvzgoOG4c1tLHi-L_28_zP2mJSFXPE5OViXkbsoTJrLUtsLJJgfO03Z1-nYasHofpQmcHV8qbIATV9bYajEgisrCVBHSINDO_Ovr65KxSJzTtUk6TTJM-Hw74LjuwkPoUbS6ewdfQeLusTlHP4xm5PobyXymzRi2-1fjSR7vNxbHB-vcAxJCYt7XvvX5yBBVwvoi5DC-DqQwOeDM6AqUqDZs3RHAN-c-tQzbjb3XwHZ_JnHyY5rXq-g5xrOFtoS70gvC5NbywEK17Ftntz6ITmzF9IKNL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا بسته‌شدن 20 درصد صادرات نفت جهانی منجر به افزایش 80 درصدی درصدی قیمت شد؟
بسته شدن تنگه هرمز فقط به معنای حذف ۲۰ درصد از عرضه نفت نیست؛ بلکه ظرفیت مازاد تولید جهان را نیز از بین می‌برد و با از بین رفتن انعطاف‌پذیری بازار، حتی یک شوک محدود می‌تواند جهش بزرگی در قیمت نفت ایجاد کند.
علاوه بر این، بازار نفت ریسک‌های آینده مانند گسترش جنگ، اختلال در تأمین نفت جایگزین، محدودیت اوپک‌پلاس، مشکلات پالایش نفت سنگین و معاملات اهرمی را نیز پیش‌خور می‌کند؛ عواملی که مجموعاً جهش شدید قیمت‌ها را رقم می‌زنند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19614" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:
مایک ویرث، رئیس هیئت مدیره و مدیر عامل شرکت شرون، همین‌اکنون در مصاحبه‌ای با ماریا بارتیرومو که فوق‌العاده است، تمام دلایل موفقیت شرکتش را بیان کرد.
تنها چیزی که او به‌طور مصلحت‌آمیز فراموش کرد ذکر کند این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و خود کشور ما مرده بود!
به عنوان مثال، آن‌ها مایک و شرون را از ونزوئلا بیرون انداختند، اما اکنون آن‌ها بازگشته‌اند، بسیار بزرگتر و قدرتمندتر از هر زمان پیشین، و انتظار دارند ثروتی عظیم کسب کنند!
این موضوع برای سایر شرکت‌های نفتی نیز صدق می‌کند... و همین حالا قیمت‌های مصرفی (خرده‌فروشی) نفت را پایین بیاورید!
بابت توجه شما به این موضوع سپاسگزارم.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19613" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19612">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">المیادین:
ایران پیشنهاد بازگشایی تنگه هرمز تا پایان کامل جنگ را رد کرد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19612" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19611">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گادی آیزنکوت در مورد ایران:  در مورد ایران، یک هدف برتر و دو هدف بسیار مهم دیگر وجود دارد. هدف برتر، حذف حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شده از ایران است.  اگر این کار انجام نشود، ایرانیان می‌توانند با تصمیم خود، به سمت سلاح هسته‌ای پیش بروند. این چه معنایی…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19611" target="_blank">📅 16:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19610">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=YcIqejNEmP9jRD24RcEtzsfj-qEwcyBpGLvkpt3lCgPfTU5I6QENfBUAL_WiWG7jYgMpS-Xf54hibSQLCeYcPTUQoutt2F2NtMk2zgxEQbrltZwkgMP9_Vbyio9r1MaVOS4iN13egX6k_ast46KFb6dHXzHpSCiceJ_w-ZuHCOBFYZfjp8EwSALNs3Gz_rq07oDIeJrxpCEMBWbUuTij4ZUeocfc3mA4JQ3JKP1duXO5tKgmWEztUORNvoib5ajLMVN7S1iqGDJKX77Zfq0Wtw7bx_2Xyt6HnzHe7WmQdU-JMEBCiwRJixYMtff5dc2nt9wTRB9naPPGA8soejE4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=YcIqejNEmP9jRD24RcEtzsfj-qEwcyBpGLvkpt3lCgPfTU5I6QENfBUAL_WiWG7jYgMpS-Xf54hibSQLCeYcPTUQoutt2F2NtMk2zgxEQbrltZwkgMP9_Vbyio9r1MaVOS4iN13egX6k_ast46KFb6dHXzHpSCiceJ_w-ZuHCOBFYZfjp8EwSALNs3Gz_rq07oDIeJrxpCEMBWbUuTij4ZUeocfc3mA4JQ3JKP1duXO5tKgmWEztUORNvoib5ajLMVN7S1iqGDJKX77Zfq0Wtw7bx_2Xyt6HnzHe7WmQdU-JMEBCiwRJixYMtff5dc2nt9wTRB9naPPGA8soejE4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:  «ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19610" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19609">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qbon-K_m6lRUCJN7GScLPmCbzU2Pp6QmvxcAbBGWP9Vf5VLuEe6U_slUyAQpPzxuSDyTCUl_0U5pLbEGjz_CLWLwDPNjasTqgn8zON0oRK7qRBt7I_k9o4Y_fp6EiRsLZJirvZkBkpt1nckZIsMVrgIrkcrxXwy2bpby--JwVgBNL2LAopC06beAOB9nFgA7wqfD8u8Itj5hOGoZhxzVv3FXRlrHIaiumZBv2R5CI1M0WouveMq7EBlDyX_nIKCwzUDOTqbDuQxx-qzRBr8adUl03YTmYb5JS_Evw2Z-oUyYd0wHm8i40t3sT9v0v0rSM-psDimZP-dSFlo4YdEJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسناد فاش‌شده نشان می‌دهند که شرکت اسرائیلی "ال بیت سیستمز" (Elbit Systems)، فعال در زمینه تسلیحات، به دنبال انعقاد قراردادهای تسلیحاتی به ارزش تا 1.3 میلیارد دلار با امارات متحده عربی بوده است، که شامل پهپادهای پیشرفته "هرمس" و سیستم‌های اطلاعاتی می‌باشد.
منبع: هارتز (Haaretz)</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19609" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19608">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:  در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.  گزینه‌های نظامی واقع‌بینانه در نظر گرفته…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19608" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:
در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.
گزینه‌های نظامی واقع‌بینانه در نظر گرفته نمی‌شدند. رویکرد غالب، آشتی با رژیم بود. اگرچه بسیاری از سیاستمداران ترکیه در کارآمدی آشتی تردید داشتند، اما این مسیر در حال پیگیری بود.
ترکها همچنین می‌ترسیدند که اگر یک تهاجم نظامی شکست بخورد، روسیه با حملات هوایی گسترده به مناطق تحت کنترل مخالفان پاسخ دهد و موج دیگری از پناهندگان را به ترکیه که خود با بحران پناهندگی روبرو بود، وارد کند.
حتی کشورهای عربی - به جز قطر - در حال پیگیری عادی‌سازی روابط با رژیم بودند. هدف تأیید آنچه اسد انجام داده بود نبود، بلکه دور کردن سوریه از نفوذ ایران و کاهش خسارتی بود که به منطقه وارد می‌کرد.
عملیات نظامی با وجود آن نگرانی‌ها آغاز شد. این کاملاً تصمیم خودمان بود.
منبع: الجزیره</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19607" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19606">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 17</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 17
دوشنبه 3 آگوست 2026</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19606" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY_tiTetuSJj2m9-16xf58jrHxHnQ__yWJIVWEuNO4bPWiaf6Pg42i-T5BGchd_4hnDTH0mnHXs5770yxjXcDo_fl4VMln-I5fplZhFO44_5lxytEP84RF1-2Tu5Zs3CjEgk8mTKSPhHaALSqCx-GB4wnQZ7GRd9wwgwtHy9chPweUBdKw1_rHE22reB-KJs8trFNu2e6bfreEgu1vFtJWa9vXidCqsBRssXRUPhVQT5_I6ETorEnt6Es-xWs6MC3FwyZzvaZapyQF2ZmtcQaLtMbRhqz1pm9lxz2tA9Tb3JDkcuPMs--gK4VZflEU4iRmMp4KcDjR9XDAvmxwAlvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رنکینگ مسخره ضریب هوشی کشورهای جهان را ناموسا رها کنید!
اگر میانگین ضریب هوشی ما واقعا چهارم دنیا بود باید سطح رفاه و توسعه اقتصادی ما هم دستکم در ۱۰ کشور برتر جهان قرار میگرفت (کشورهای دیگر صدر جدول را بییینید) نه اینکه رییس جمهوری مثل پزشکیان داشته باشیم که سطح ادراکش از توسعه برق این است که برود آستین کوتاه بپوشد و یک لامپ خاموش کند!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19605" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19604" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19603" target="_blank">📅 12:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:
«ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»
این اقدام نشان‌دهنده درک این موضوع است که گزینه‌های موجود در حال حاضر برای دولت ترامپ محدود هستند و ممکن است از نظر سیاسی یا نظامی قابل قبول نباشند، که این امر ضرورت بررسی راهبردهای جایگزین را ایجاد می‌کند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19601" target="_blank">📅 12:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX_bVv0Yl0hjxtK2SqZ5nlPbkIlK_TyzyZCd7pjWoowukrC-M8R62d58kIWMJc4Umk4fk3rV6eBaCYm3g5ilHv4fzcuehu-I5wgMrWQmGPZtDwd6S35GGmNIiwxrlkrMf8S15Okv4NGSadl64oJnnvgXNfDHpaB6qITczTjrRnWMWfoYCqNfZYlGJ08jaR0aIpRI-v_JUcHiJh2UMEZs6CeLJ7OLY9ToRv0m582heYzPfoWVuC5vj_tom9z0CHYpoS3CQ3MBAKrBsBMZvriIjrx-bvKQVdMcD8Zma4thyA8q_wLBViF1vFxQiCg28AYvqr3Xz1wnaumQwKPjFV57xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19600" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.  این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19599" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19598">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.
این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.
منبع: i24</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19598" target="_blank">📅 10:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19597">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ ادعا می‌کند مذاکرات آمریکا-ایران روز دوشنبه آغاز می‌شود
او‌ گفت:
«خب، کاری که الان انجام می‌دهیم این است که در قالب مذاکره با آن‌ها صحبت می‌کنیم. این کار فردا بعدازظهر آغاز می‌شود و خواهیم دید که آیا این واقعیت دارد یا خیر. من عاشق انجام این کار هستم،»
ایران این ادعاها را رسماً تأیید نکرده است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19597" target="_blank">📅 02:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19596">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19596" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19595">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19595" target="_blank">📅 01:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19594">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانید این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم (ایران) به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند رخ دهد.
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم. مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19594" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19593">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ می‌گوید عربستان سعودی، امارات متحده عربی، قطر و ایران همگی از او خواسته‌اند حملات را لغو کند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19593" target="_blank">📅 01:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19592" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19591">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کشته شدن مامور پلیس در درگیری با اشرار مسلح شادگان  ستوان‌سوم شهید «سینا سیاه‌نژاد»، از نیروهای حافظ نظم و امنیت، هشتم مرداد در جریان درگیری با اشرار مسلح و حادثه تروریستی در شهرستان شادگان استان خوزستان، حین انجام ماموریت به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19591" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
