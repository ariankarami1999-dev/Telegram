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
<img src="https://cdn4.telesco.pe/file/Ha5Mw-tKkwlhBAvnOVMDWHiSy7Z9-H2J0RmrqHiLMSoYS9urnK-lt7zz6EKOgzqEcSQZpc-J-6zHG1dFM7T2mVzEWCMynmVVWaT-dRPsSiR-1O2P9_ZHGuyixwlrpmjRetPXJ_Fzif1B5MXGoXlS0RNN6kgI8E6X99st8_9xbkzA0VO9ti79Ab5bOJ_QZpLix-B6KZB5YVVKt9jaO-0aWg4MkeMDH6Q9Cjyf4qnrELgkpmQVb2nKsYb_3E7lnECXSchb7LV1L6ln2CFkB8pTyE2zU_cm6FkJJTLkUFlayi8TWzo8C__976J0tFx3uYS-DRmYniwKIISNrk7Cso76lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-17850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">— وزیر دفاع اسرائیل، کاتز:
"هیچ محدودیتی برای سربازان ارتش اسرائیل در لبنان برای اقدام به حذف تهدیدها وجود نداشته و وجود ندارد.
آتش‌بس دیروز اعلام شده، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که جوامع شمال اسرائیل را محافظت می‌کند، باقی می‌گذارد.
همانطور که نتانیاهو و من روشن کرده‌ایم: اسرائیل از منطقه امنیتی در لبنان عقب‌نشینی نخواهد کرد".</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SBoxxx/17850" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j69eTMa9mh-JxRhcJ5fWC1DHj9knDcR3F0BQ7iySgymKCO4dbFsEv3RunTwJdGMChMkNyrZGz8quI6Vb5eH4hYbTHswYFHVjn3hL8kx4ZzEEPb_7CyNGcEiEG4vqrC4ksES5vSZYVBl7SKH82k1xuFri4G5TsUCIgM_1C0jtkMO_47Mw3yzncXH0F5G4Y4JP6Mxh5Ok9N8lH-qYCjpJfveb8gXXzA2y80vkAEqCSJ0hTlWuin3okvWfQOiICf7uWpsMYMp39-lUaqurZkMP-ucWu14JlsNuv3hg9JjPY-ScbWMAet6eW3MniuzofUCXKCbgfJlNxIvwUEnTBa01Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو و پیام Hawkish به بازارها
در نشست فدرال رزرو آمریکا در ۱۸ ژوئن ۲۰۲۶، نرخ بهره بدون تغییر باقی ماند، اما لحن سیاست‌گذاران به‌وضوح
Hawkish
بود.
✔️
اعضای کمیته
FOMC
تأکید کردند که ریسک تداوم و حتی تشدید تورم همچنان بالاست. همچنین داده‌های
Dot Plot
نشان داد که بسیاری از اعضا احتمال یک مرحله افزایش نرخ بهره در ماه‌های آینده را منتفی نمی‌دانند.
اگرچه در داخل
FOMC
اختلاف‌نظرهایی وجود داشت، اما دیدگاه غالب این بود که
Rate Cut
در شرایط فعلی چندان مناسب نیست و در صورت لزوم حتی گزینه
Rate Hike
نیز می‌تواند مطرح شود.
🔽
واکنش بازار سریع و قابل‌توجه بود؛ پس از انتشار بیانیه،
USD
تقویت شد و انتظارات معامله‌گران نسبت به سیاست‌های انبساطی کاهش یافت.
نکته مهم اینجاست که بازار انتظار یک
Full Hold
(ثبات نرخ بهره بدون هیچ‌گونه سوگیری مشخص) را داشت، اما فدرال رزرو با اتخاذ یک
Hawkish Hold
نشان داد که همچنان نسبت به تورم نگران است و برای حفظ سیاست‌های پولی انقباضی آمادگی دارد.
🕯
جمع‌بندی:
فدرال رزرو برخلاف انتظارات بخش قابل‌توجهی از بازار، سیگنالی انقباضی ارسال کرد. این موضوع باعث افزایش تقاضا برای
USD
شد و تا زمانی که فشارهای تورمی به‌طور محسوسی کاهش پیدا نکنند، می‌تواند از دلار حمایت کند.
💬
برای کسب اطلاعات بیشتر، با آیدی آموزش (
@CWedu
) و یا شماره تماس 09908006002 در ارتباط باشید.
@CyclicalWaves</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/17849" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17848">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور
:
سرویس اینترنت پرو متوقف شد و مبالغ کاربران باید عودت داده شود</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/17848" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17847">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🗯
دونالد ترامپ ؛ رئیس دولت آمریکا
:
آنتروپیک دیگر تهدیدی برای امنیت ملی آمریکا نیست
وی در مصاحبه جدیدی اعلام کرد که پس از اقدامات اخیر شرکت آنتروپیک، دیگر این مجموعه و مدیرعامل آن را تهدیدی برای امنیت ملی آمریکا نمی‌داند. این موضوع پس از آن مطرح شد که آنتروپیک در پاسخ به دستور دولت، دسترسی کاربران خارجی به مدل‌های پیشرفته Fable 5 و Mythos 5 را مسدود کرد
اگرچه ترامپ از سرعت عمل و رفتار مسئولانه مدیرعامل آنتروپیک تمجید کرد اما همچنان احتمال استفاده از اختیارات اضطراری قانون تولید دفاعی را برای خود پابرجا نگه داشت. در‌همین‌حال، شرکت آنتروپیک نیز بر تعهد خود برای همکاری با دولت آمریکا جهت حفظ امنیت زیرساخت‌ها و پیشتازی در این فناوری تأکید کرده است</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/17847" target="_blank">📅 12:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17846">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAJpe4MrPLzHRqZgMASF7FNWnQNOYH1DC6rg0ZVHUSmQoHR06hX0jlBdhYoignm5U5dNKrhmGOQGRSGTv52ErQolTZIXVhhEWA0CiX4GZOF1XkSccy7EluR643-BXkXspw_Uq4S8Q2j9YcusKcsda8st27zgymTF1IBvBjMbja8oKmq1WCUWzE0PkLOmX16XiFLMJvH0hSqNnRteB535LEPPegwRjnAP-jcLOynUFrFZ5lPkaICiMA_02iCqtKYRBQXnAWnDKNPJu9Np6y6N9PYGKNFv9pmvs5smIlVVO_GMxFDRLtgyoVyk9RWefb9HO6LVvq9F6Y5X5frqJzt7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدانم ولی اگر بیعت کرده قطعاً مصعب سرش کلاه گذاشته بعداً</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/17846" target="_blank">📅 11:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان:  تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/17845" target="_blank">📅 11:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پزشکیان:
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/17844" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند  حسین شریعتمداری نوشت: «هموطنان بحرینی‌مان بارها اعلام کرده‌اند که خواستار پیوستن به ایران یعنی وطن اصلی خود هستند و انتظار آن است که مسئولان دست‌اندر‌کار نظام این خواسته…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/17843" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17842" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/17841" target="_blank">📅 10:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17840" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17839" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17838" target="_blank">📅 09:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:   «در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/17837" target="_blank">📅 08:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
«در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های گذشته، حال و آینده برای خدماتی که به عنوان فرشته نگهبان برای کشورهای خاورمیانه ارائه شده است».</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/17836" target="_blank">📅 08:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هشدار فوری مجدد نیروی دریایی سپاه روی سیگنال رادیویی برای گشودن آتش روی هر شناوری که به تنگه هرمز نزدیک شود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17835" target="_blank">📅 01:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17834" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLD-jc-uipQVGzXyGTfD--CilClBMdKIsKPp2lEAM5RjTObMoiYJU2LJzfkpnT82USXz1PQIXCWlCU8GUUysJtCM6L0sEqfMpUP7YXvgLp4z84ThYsmL96Cp7JrfEUYpqpMRYq5mFLTN1bGZgggCtmrC2ZkJkxWq12yTk8uPoK_hBEpB_rvLNNhFhBchWcIi3f1muYEzqjkHLuzasHxg2CtCTfy0Usp19xokUFrPGXditMNPUdh-P0vzG-3_LbWm7rtseuGQ40wZA9xbIgJcUYAsYL-z8yVrpO_IcUkdUOMZlGzgquskV01gyL3tJOVHbaA1GTzY0izkT-w_zXjvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها  دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17833" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=HIlLgNYwUvJbnEqYV8OOGMKIsl7ntO-Xi_Wsp2a7zeW5ojDYl2fEbpfFzY79skliq0joZe92OhM3MxvytwUDyBvPM51HEuwVDK7Kzj_DL-AFpAcg7sMoAJuprHQdHkNvzu-z1etegB6gUOIajmWa3fTWq063xpgeRlKSQQI_7LsWZbgoj3agxr0jFeH7QTqPqJTSG5e-ZcaEumFGIlm_BCkmYyPmuoLvgElk5G5RXPf0m-SZ_O8BD2v2DEdmvfn0z6pFzVjj2AKlycylT69MG9Ccc-F8zy4NcT7sPdE7tvk_9ScZrHT5aVtS2pLs35D2pwY8GtjKAEFsnc9AZ6KCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=HIlLgNYwUvJbnEqYV8OOGMKIsl7ntO-Xi_Wsp2a7zeW5ojDYl2fEbpfFzY79skliq0joZe92OhM3MxvytwUDyBvPM51HEuwVDK7Kzj_DL-AFpAcg7sMoAJuprHQdHkNvzu-z1etegB6gUOIajmWa3fTWq063xpgeRlKSQQI_7LsWZbgoj3agxr0jFeH7QTqPqJTSG5e-ZcaEumFGIlm_BCkmYyPmuoLvgElk5G5RXPf0m-SZ_O8BD2v2DEdmvfn0z6pFzVjj2AKlycylT69MG9Ccc-F8zy4NcT7sPdE7tvk_9ScZrHT5aVtS2pLs35D2pwY8GtjKAEFsnc9AZ6KCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17832" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17831" target="_blank">📅 20:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!  در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17830" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN0kX6EOMO7Z-7kHGPNlMmStn-L-kQ9ydudb1u5WouGYePVNG6P2ohrrP7dQEBFxSlHQnmSm7t57XlZ1x9c_SzIlDfNErBl-uI-tccGa8gjScK5pf1SMDozy_L41P1g3DaKh_mfQm-9JKiG8JiYvlelEQenW0fh2AR4vVTZmsQ15rdJowTBwtmKaO7nxeJbDuSEYQtUf-BwfCB9DeXLZZEDo-yDjtNfbzfZMC8CE2-sjOEcCdZOmZ3K1VL-YdonGqvB4V0Cjm3BTAML3KmH3l5fRwCCTU_rWmABA2N-fWJmWhdkhCyUM26I_XEaQ5ZpQufRXbUpqvdhgi5_DIsGROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!
در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان می‌دهند. در هند به دلیل فرهنگ پسرپرستی، کمبود زنان وجود دارد و زنان اغلب در صورت اطلاع از دختر بودن جنین، سقط جنین می‌کنند.
در مرحله اول، برنامه‌ریزی شده است که ۳۰۰٬۰۰۰ مهاجر وارد شود.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17829" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17828" target="_blank">📅 19:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_iFxzpsCJwoSXREcPRcdaqbHiemFxeIbBA5uZ3bIGmQcF634f1N4UtHzaklhFV2CUe8dLnDiBEaXXGRnj9nxmLCf9cFrhuLzSMmu2JyLpWIOYJ64iVtMGJ082S8kqLuE7brmIXdhf9zCfFeqGDjKmF8hEFOdmNYdqa5joz80cDQm91mibmHrCAiuPKuU4lhyL7J555prTImUAbh8N7C0n3MwK2sxQX9HxvBSUJEx-pN5rDcisguK7BJuZC4_OE-qTSG5Shpi331-yxc22uL5yP0kqUhY0bcLEIyoJaoyu5GujC_kS9ZgDw3y_pMwakNVh17qfeuTIV9dTr0ov575Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!  اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!  ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17827" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رسانه های اسرائیل:
عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17826" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17825" target="_blank">📅 17:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17824" target="_blank">📅 17:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه هرمز مجددا بسته خواهد شد.
قرارگاه مرکزی خاتم‌الانبیا اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17823" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یارانۀ 2 دلاری خرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17822" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoN80VrDi0olJ9VdSTxhl2SrpZvju4OgMlxNS9kGzgi9_8YLhhbulLKH-VviTtjXn9Gs-NirsnPb4YqL46ncCvtvfY6mtAxmKpeXdNghKEg8TCisL4AKIPse8bJCwbALb63Qn1jTsvQNDY0Jnrnef9TfgosUS-n2HEcrwi0_cKi6hXGJ_UNjoW9vi9F3nMqaZl-AW3h8r91nXQ-MDi46L_H1kMPNEINnK7BeVkcfSs_2-y628aobkD2J54WSclqMRPxkEN-uh7I_BfEP0GGDTugwVCdP_K8Ei2Oc7yrfMdiwsAKTEvo573lBh0zgQ-tTbR963Tv-3Pl3sJMtsAM-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لابد چون نظامیان می دانند درگیر شدن با ارتش اول دنیا و یک قدرت هسته ای با فنآوری بالا با توییت ریدن زیر کولر متفاوت است؟!
یک بار از بچه های پدافند و لانچر و ... بپرسید شرایط چطور بود؟!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17821" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17820" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17819" target="_blank">📅 16:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بخدا سوگند که ما هم خواستار ابطال این تفاهم نامه هستیم!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17818" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC_8Q1dJZHxznKwnEsGbLrnuFuYH8_ejl-kJQ-wygneEBDCJdQir5GpngV7F1ZBjo3mdezu2HnXTWbg-CJA9zVjzl3X6LlqKBF-VaWj15VwuG0HgoBbkJazpKyO6PhOSvi6UsBjL9IuYMeD7YxXwEnoJNfXsmebKrAgN-0z4swvqYr219S17vM7HW1725Q_Y8ALJ8dPdOu2OsTecX3GqMG8xpcNL1noNM8hJY4CMV2wa4zlj8jNpoaDYtkKcDS3w6eEg6nkJgD40EYOo8NVWB5B7g0MANc-p72NLmcY0n5OLMdzR8bEqPC46eOBnj8gFRZlLqGSWkqv3C_qKz1ma7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17817" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17816" target="_blank">📅 15:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17815" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2u6xnVxB02SHZRXPy-8T-iLlFsuUXf90QjmDb_FOjkPKBjwORDsxhs9Ka3Aw6owc1d2Mfurq_kltQuGTJ-yVv4Dr0jGGdi8r83d54cNroL2Tb6H5FvFnmux51MXT3RfzsjPTFVyCtNlvRGcKoDwKxnmHhh9gS93q__ylqN7PVJjgAwFpeFsOtb36mYSdGKvPt8WDF00sonfGdJLyErpIjXIuH_ggXyXUB7qFh9cBZoxBNVBCjl-CyimA8VWVLrrw7wg74otvw1t_n3fvwv1eGa0KPhWihKW3GIiw9lVoDgHLF_7h5J0h-XSRGTJ7XFlNyqgH6V5Q_5ijHD7YBTZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها
دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است و در سه تا پنج سال آینده، اگر درگیری با روسیه ادامه یابد، جنگ به رقابت بین سیستم‌های هوشمند تبدیل خواهد شد.
اوکراین، که پیش از تهاجم روسیه در سال ۲۰۲۲ سرمایه‌گذاری چندانی در پهپادها نداشت، اکنون به پیشتاز جنگ پهپادی تبدیل شده است. این کشور از هوش مصنوعی برای برنامه‌ریزی عملیات رزمی، تحلیل حملات موشکی روسیه و هدایت پهپادها استفاده می‌کند. تسوک می‌گوید: سیستمی که داده‌های بیشتری دارد و بهتر آنها را درک می‌کند، راه‌حل‌های بهتری پیشنهاد می‌دهد و برتری خواهد داشت.
مرکز هوش مصنوعی اوکراین، که در مارس ۲۰۲۶ تأسیس شد، در حال توسعه یک سیستم عامل واحد است که تمام داده‌های میدان جنگ را تحلیل کرده و تصمیمات را از سطح یگان‌های جلویی تا فرماندهی استراتژیک تسریع می‌بخشد. هدف، ادغام سلاح‌ها و سیستم‌های داده‌ای در یک ارگانیسم زنده واحد است که به صورت هماهنگ عمل کند.
جنگ اوکراین به یک مسابقه تسلیحاتی فناوری تبدیل شده است. شرکت‌های خارجی مانند Palantir سیستم‌های خود را در اختیار اوکراین قرار داده‌اند و پروژه Brave1 Dataroom  برای اشتراک‌گذاری داده‌های میدان جنگ با متحدان ایجاد شده است. روسیه نیز در حال توسعه قابلیت‌های هوش مصنوعی خود است و از آن برای برنامه‌ریزی حملات پهپادی و موشکی استفاده می‌کند.
تسوک می‌گوید: سوال این است که چقدر سریع می‌توانیم راه‌حل‌های خود را بسازیم و چقدر عملی آنها را پیاده‌سازی کنیم تا تأثیر اصلی را در میدان جنگ بگذاریم.  اوکراین در حال حاضر بر اصل حضور انسان در حلقه تصمیم‌گیری تأکید دارد، اما تسوک هشدار می‌دهد که ممکن است روزی برسد که سیستم‌های خودمختار آنقدر سریع عمل کنند که حضور انسان، تصمیم‌گیری را کند کند. در آن صورت، سوال این خواهد بود: چگونه می‌توانیم با تصمیماتی که سیستم‌های خودمختار پیشنهاد می‌دهند، همگام شویم؟</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17814" target="_blank">📅 15:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1iftGADw3nFIsSq5OQNNkIskozN3WOhYNFvSvMcUjOZViSrfDJggOLmyrxz_zlhxm9nhBwH4TfOLiHIak2j996G-4exv3vXBdvOq-RmzWGSZ_rzpqpaZ5GCeiUtG4ILzbvMBrlzr1vUJR2PwEgiFRmYRtm0bNH5dFhqrdsxXktGAXgwhs4f1Oja2Mq5LfnkrHdGp3z1gXE8k33jlG4JQXrdm4QvoUBci8HSTC0_i1MkQy6GScLT9ETShTmJfmLlB8p3n9TRPurW0M2nvn8uVO_69xqLTy_mr67V-p8_Qo_MM_nOOmNgpgaf1i7K6jDyrQbPnZhWW2AaUdG8DiICig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!
اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17813" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17812" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=F1L7cv2j_FW5y7vh14xlWDa5s0yXS0-yq-aGaeis5KH2h3EKrCs49uZcfVW8IvcC_nJikVZVdd9zJLz8cmi4EqJCiHxhOUN_pWZEjQb5VwLQyzwghs0KQcCTero-I47x-gGxnUuc6V1sP9ahIXRxY8XgqtF1oouGAngVr7vgHIT8Fhelr7tFEU87MH6fi7tjmxzpLsFMT9yCdpse9GfgjKUAjgUtltuiPPSccIoL3Z5RE0RV6Tqypzd9g68fubT1hYr_VC-AqWe_5fGImWJPa2inb74mpiwLtRXNB1Rsc-WrVYxws4em16AlvdP9MhovOQBIvc9mNECH5-CKqE2kGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=F1L7cv2j_FW5y7vh14xlWDa5s0yXS0-yq-aGaeis5KH2h3EKrCs49uZcfVW8IvcC_nJikVZVdd9zJLz8cmi4EqJCiHxhOUN_pWZEjQb5VwLQyzwghs0KQcCTero-I47x-gGxnUuc6V1sP9ahIXRxY8XgqtF1oouGAngVr7vgHIT8Fhelr7tFEU87MH6fi7tjmxzpLsFMT9yCdpse9GfgjKUAjgUtltuiPPSccIoL3Z5RE0RV6Tqypzd9g68fubT1hYr_VC-AqWe_5fGImWJPa2inb74mpiwLtRXNB1Rsc-WrVYxws4em16AlvdP9MhovOQBIvc9mNECH5-CKqE2kGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17811" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">➡️
استارلینک با مجوز دولت عراق ، بطور رسمی در این کشور فعالیت خودرا آغاز کرد</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17810" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📡
طالبان با دستور مستقيم ملا هبت الله آخندزاده رهبر این گروه در افغانستان ،  استفاده از گوشی های هوشمند را برای تمامی کارکنان نظامی و غیر نظامی خود ، ممنوع کرد</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17809" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N64OWNrojVTZxr8w_jtQ7qS8LiQc7iOHe21Ri-GE5nSperh8CLTuoXuqlWHH91AYkMMcrUu8kpS6HBR5Y27AkFGjzcMqGNxFJGdA1BuDIjfKWLwQiUk8C8NxUQXz-KY-ufTv7uz8nsdI1KKTHVY-BOhKrWL4qSi-W_cbkhUPtM4F5JqaR7EXtANZA73VKIS9KZdvAHSr1iBouoBpS3ACL6U1E3qLMbYSTQRrI4yGisY6yu_rVYHyuYWXKCuogInlzzuyFRWjHLZNzX7VGmVkLfknUOkm8ThLRKFPlRwa1iD5wOdfBI-I28YVpDixM97fW1BXn9kZ0Qa2HBnh7Nx_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ این مردک مجاهد خلق را رهبر اپوزیسیون ایران معرفی کرده!
این همان گهی است که 24 سال پیش برنامه هسته ای ایران را لو داد</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17808" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بلومبرگ: اتحادیه اروپا برنامه‌ریزی برای شراکت استراتژیک در زمینه مواد خام با ایالات متحده علیه چین کرده است  اتحادیه اروپا در نظر دارد با ایالات متحده بر سر نقشه راهی برای شراکت استراتژیک و توافقی درباره مواد معدنی حیاتی به توافق برسد. هدف کاهش قابل توجه نفوذ…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17807" target="_blank">📅 09:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcLkr9UpU-WguJ02z2OvcQZaHV9PKuZZ9p0U8Y89blxLGYuORums06sLDJGAQbvnOfPkJF-wl9BSK_AcV_tGAm_fn-aMVuaIctMbSLCkmMsePyYoyTGvk6PzsUJsQqW2A1Iuda7izSjoD2q8IMhd3pel-7LqfvAx5zQghqHRmORHPAIzbAPwHn5176_Jo31xvMEkfSYAcSLTY7ldrmR6R9tRNjKk36j8mQu0sXNlTbE2s0fODtNuWjW3Uz1yH2Bf2ckqHsBSI_b9zk1eRAeRr3IlCetdjuplkv07-tCLPVunc8JuDN56WG6sAU_5gqy_bQIvbTZlVvA1nmkmSxzsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای شهر نبطیه اعلام کرد با توجه به خطر احتمال بالای اشغال شهر و شدت درگیری مراسم تاسوعا و عاشورا لغو از شهروندان می‌خواهیم از شهر خارج شوند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17806" target="_blank">📅 01:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9SF-IGMJxlWcQbCnbkKSx6EpuMqLFx6QoGgtjv8IFkPngNqHBsdgFpLNozgc083iC1L09s5IIdzykyuoabV_rECwkn5cKxilENKVQO6gkwF5Kum4sN5Jm_AQo3G7vcs754OEhdYS4x9I6BrXuoEnu-FVHfugDdbUSmbVRfaUWOHGtB6xN-vuXzY9hxDRnHWg8ukurhM1iuNCqgOVnG4rC6-ouYaYKgbW62hB0qlIjGism64eAmmnT60lJ7Km_Mx-uqxwAfANMbSRNGenlDJPwM9wUMuiDGSuqp6RJG4a28oP5IO0vh2_rC5rgfpNmUe4XDbwqIwdAFpuSAmox4EcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی قبل ترامپ در توییتی اعلام کرد که ایرانی ها مسئول سقوط بالگرد آپاچی آمریکایی در تنگه هرمز بوده اند.  او اعلام کرد که ایالات متحده باید به این حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17805" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محسن رضایی:
به خطای دشمن شدیدتر از آنچه بوده پاسخ می دهیم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17804" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جی‌دی ونس درباره پیشنهاد آمریکا به ایران:  «گزینه اول این است که همچنان مانند یک حکومت تروریستی رفتار کنید؛ در این صورت، به‌معنای واقعی کلمه هیچ چیزی به دست نخواهید آورد.  گزینه دوم این است که مانند یک حکومت عادی رفتار کنید؛ در آن صورت، ایالات متحده واقعاً…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17803" target="_blank">📅 22:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17802">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17802" target="_blank">📅 22:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17801">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
"ایرانی‌ها، مردم بسیار باهوشی هستند. آن‌ها نوعی نابغه‌ی بدوی هستند، اما باهوش‌اند.
آن‌ها اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت."</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17801" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17800" target="_blank">📅 21:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خود عربها هم گفته بودند
که قرار نیست سرمایه گذاری بکنند</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17799" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:     تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران   ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17798" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17797">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این هم‌ در همین راستا است:  — مقامات اسرائیلی از انتقاد تند معاون رئیس‌جمهور ایالات متحده، جی‌دی وانس، از وزرای کابینه اسرائیل و هشدار ظاهری او مبنی بر اینکه حمایت نظامی ایالات متحده از اسرائیل بی‌قید و شرط نیست، شوکه شدند.  رهبران اسرائیلی عمدتاً از پاسخگویی…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17797" target="_blank">📅 21:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پس بند 1 توافقنامه که رفت روی هوا.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17796" target="_blank">📅 20:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حزب الله عملاً دارد سیگنال ادامه حملات به شهرک های شمال اسرائیل را می دهد؛ یعنی اقدامی که پس از آغاز جنگ آغاز کرد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17795" target="_blank">📅 20:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17794">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌  بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17794" target="_blank">📅 20:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله لبنان تأکید شده است، به هیچ توافق آتش‌بس پایبند نبوده است.
🔹
بلکه دشمن اسرائیلی در نقض‌های مکرر آتش‌بس افراط کرده و کشتارها و تخریب ساختمان‌های مسکونی و زیرساخت‌های غیرنظامی را مرتکب شده است، و به حملات زمینی خود از طریق تلاش برای نفوذ و کنترل روستاها و مناطقی که پیش از توافق نتوانسته بود به آنها دست یابد، ادامه داده است. تحقیر اسرائیل نسبت به آتش‌بس به حدی رسیده است که رئیس ستاد ارتش دشمن، جنایتکار آیال زامیر، دو هفته پیش اعلام کرد «در لبنان آتش‌بسی وجود ندارد»، و سخنگوی ارتش او دیروز مجدداً بر ادامه فعالیت نیروهای اشغالگر در جنوب لبنان تأکید کرد.
🔹
و طبق عادت خود، دشمن برای جبران ناتوانی در مقابله با مجاهدان مقاومت و پوشاندن شکست‌ها و خساراتش در میدان نبرد، به ارتکاب کشتار علیه غیرنظامیان و هدف قرار دادن روستاهای امن روی می‌آورد، همانطور که امروز پس از مقابله مجاهد دلیر با تلاش پیشروی به سمت تپه علی الطاهر در شب گذشته رخ داد.
🔹
مقاومت اسلامی همیشه آماده مقابله با هر تجاوزی است، مجاهدان آن با شجاعت و روحیه حسینی کربلایی از خاک و مردم خود دفاع می‌کنند و با تیرهای خود ارتش دشمن را به سختی می‌زنند، ده‌ها افسر و سرباز آن را کشته و زخمی می‌کنند و در تجهیزات آن آسیب‌های ویرانگری وارد می‌آورند، و میان ما و آنها روزها و شب‌ها و میدان نبرد ادامه دارد.
-جمعه ۱۹-۰۶-۲۰۲۶‌
-۰۴ محرم ۱۴۴۸ هـ</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17793" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17792">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.  ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17792" target="_blank">📅 20:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17791">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.
ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17791" target="_blank">📅 20:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17790">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اطلاعات آمریکا هشدار داد که اسرائیل احتمالاً توافق هسته‌ای ایران را تضعیف خواهد کرد</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17790" target="_blank">📅 19:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17789">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در راستای افزایش مخالفت با اسراییل در کشورهای غربی:  آلمان طبق گزارش RIAS، بالاترین تعداد حوادث ضدیهودی را در تاریخ خود ثبت کرد؛ ۸۷۲۵ مورد در یک سال.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17789" target="_blank">📅 18:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b325ce33.mp4?token=JY9s10PMYK3Cj1ZQIaTru8wJtFyhFh9Hiyr6aF9UOEvJedFXJV82fiNCpTkVFiyRs9GHhXL8SLEeq9m54ag0_cAQh3mq6Uodzk3iBjZuzg3lFE8vhQ60T2djVvgbQzGNUKJfD7Qha7tpOkBGArxOIBRLmga5z540X6VKlxCEU8-KGMKExnMkErQLE0ppumO8xutS9GorizCmeNBMVF0YI79kglGWH1XqjKH1MoDtGdfLm7BVWhJNC6MbJo-nlQLWmzT4Vp3R9e2rcIiEvaxEhS1pFRDkLKYB-KDPI8jOyj0P4tZTl4y4M7RmNEUQgXQX6Xgzd-oW3r-qaa9SfqqP-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b325ce33.mp4?token=JY9s10PMYK3Cj1ZQIaTru8wJtFyhFh9Hiyr6aF9UOEvJedFXJV82fiNCpTkVFiyRs9GHhXL8SLEeq9m54ag0_cAQh3mq6Uodzk3iBjZuzg3lFE8vhQ60T2djVvgbQzGNUKJfD7Qha7tpOkBGArxOIBRLmga5z540X6VKlxCEU8-KGMKExnMkErQLE0ppumO8xutS9GorizCmeNBMVF0YI79kglGWH1XqjKH1MoDtGdfLm7BVWhJNC6MbJo-nlQLWmzT4Vp3R9e2rcIiEvaxEhS1pFRDkLKYB-KDPI8jOyj0P4tZTl4y4M7RmNEUQgXQX6Xgzd-oW3r-qaa9SfqqP-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17788" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مسئول ارشد اسرائیلی:   ما در آتش‌بس هستیم؛ اگر حزب‌الله به ما حمله نکند، پس در زمان جنگ نیستیم اما نیروهای خود را در جنوب لبنان نگه می‌داریم</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17787" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مسئول ارشد اسرائیلی:
ما در آتش‌بس هستیم؛ اگر حزب‌الله به ما حمله نکند، پس در زمان جنگ نیستیم اما نیروهای خود را در جنوب لبنان نگه می‌داریم</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17786" target="_blank">📅 17:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ظاهرا معنی آتش بس از دید نتانیاهو صرفا توقف جنگ از سوی دشمن است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17785" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک حمله هوایی اسرائیل حدود ۵ دقیقه پس از آغاز آتش‌بس، منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17784" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک حمله هوایی اسرائیل حدود ۵ دقیقه پس از آغاز آتش‌بس، منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17783" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:  جنگ ایران را تضعیف کرده است! دیگر نیروی هوایی، نیروی دریایی، تجهیزات پدافند هوایی، رادار یا تقریباً هیچ چیز دیگری ندارد، با این حال دموکرات‌ها می‌گویند که وضعیت ایران اکنون بهتر از چهار ماه پیش است. آیا می‌توانید تصور کنید که با این موضوع کنار بیایید؟…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17782" target="_blank">📅 16:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:
جنگ ایران را تضعیف کرده است! دیگر نیروی هوایی، نیروی دریایی، تجهیزات پدافند هوایی، رادار یا تقریباً هیچ چیز دیگری ندارد، با این حال دموکرات‌ها می‌گویند که وضعیت ایران اکنون بهتر از چهار ماه پیش است. آیا می‌توانید تصور کنید که با این موضوع کنار بیایید؟ مردم چقدر می‌توانند احمق باشند؟</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17781" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ونس:  برخی عناصر در اسراییل به دنبال ایجاد یک دولت شکست خورده مانند لیبی در ایران هستند!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17780" target="_blank">📅 15:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43093b929e.mp4?token=iTJpop0K0tdQEIejWcHUIXQUdpMKgiotPQE-mbdG9mQN-EWKamQdNx-COIjWjA2IkPLZdL_q8oa5zsbsdctQik_iJPqPd8-iwen79eETqEHNJfzA-WP9xLHcLl8xOpF0BkPiARICobLIO-I_55f0tDd9rqfsKOPLWky9GmV7vfTeHs-Ec0oirioKlprc9VVPGguzFXDs7fOuzNtANh84fzFOhN9B3HGAk1z4x2aFO14f9fg8YRXnbuQ-00rFrqVWjc2OcjYvM7PUJXOCnVnnOPF6IlScztW4iQqVHdayMSvz2W8CsVnQZ_Stg71hn9xxz95RVRGpzlSWjO3hmbr7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43093b929e.mp4?token=iTJpop0K0tdQEIejWcHUIXQUdpMKgiotPQE-mbdG9mQN-EWKamQdNx-COIjWjA2IkPLZdL_q8oa5zsbsdctQik_iJPqPd8-iwen79eETqEHNJfzA-WP9xLHcLl8xOpF0BkPiARICobLIO-I_55f0tDd9rqfsKOPLWky9GmV7vfTeHs-Ec0oirioKlprc9VVPGguzFXDs7fOuzNtANh84fzFOhN9B3HGAk1z4x2aFO14f9fg8YRXnbuQ-00rFrqVWjc2OcjYvM7PUJXOCnVnnOPF6IlScztW4iQqVHdayMSvz2W8CsVnQZ_Stg71hn9xxz95RVRGpzlSWjO3hmbr7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر رییسی نژاد استاد تمام عیار ژئوپولیتیک است اما خواننده Secret Box از ۷ ژوئن میدانست متاسفانه استراتژی اسراییلی ها به سمت پلن B یعنی زدن زیرساخت‌ها و ایجاد یک دولت ورشکسته چرخیده است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17779" target="_blank">📅 15:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع آگاه:
آمریکا به ایران اطلاع داده که اسرائیل حملات خود را در لبنان تشدید نخواهد کرد</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17778" target="_blank">📅 15:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKYwO7QB70GVBUB3H7jcblA6OJX1wef2b7qTZuNL_N9n8F8kKTRPtm0cOlVLzEHaNSgqJXNiGeekHvly5sSO4CAa0IlFdXRhAAOzlMniEe81T2k1riSYU2pw6tH5xlvBfhnVTpax12bm1Km98Hj5AC5EdAVfMcE0UqwU6ULg9LA4ZLNkIWZ8R7x-vHVL08ijZSCLxUKSNyR9bwVZXKfEYkiN_aYRsyj4n-rqzrL-W3K9hBE_RelWY-sGd87pJYpf02uI8hhveAuJRuAdt9PWWF2OolQfaoBVRyC1IFiTwiydhyqNjixmXqSrIR2deRs3iGVtSaTIDeN1J-0amIAJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17777" target="_blank">📅 14:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:   با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17776" target="_blank">📅 14:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:   با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17775" target="_blank">📅 14:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:
با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17774" target="_blank">📅 14:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17773">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کلا تا اواخر دهه ۱۹۷۰ میلادی، عمده احزاب اسراییلی مبتنی بر ایده های سکولاریستی و مدرن بوده و اغلب سیاستمدارانشان هم اروپایی تبار بودند .
اصرار زیاد بر جذب مهاجران یهودی خصوصا از خاورمیانه و آفریقا (عراق، ایران، یمن، اتیوپی، مراکش …) باعث شکل گیری جوامع عقب مانده حاشیه نشین در اسراییل شد و حزب لیکود هم بر پایه خواسته های اینان قدرت گرفت.
اکنون این سفاردیم ها به سرعت جمعیتشان از اشکنازی ها در حال پیشی گرفتن است چون زادوولد بیشتری دارند و به نظرم از عوامل خشونت های اخیر در غزه و … همین ها بوده اند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17773" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17772">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاید…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17772" target="_blank">📅 14:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر امنیت ملی اسراییل ، ایتامار بن گویر:  امشب تهران باید بسوزد!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17771" target="_blank">📅 14:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارشهایی مبنی بر پیشروی سنگین نیروهای اسرائیلی برای محاصره کامل و تصرف نبطیه!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17770" target="_blank">📅 14:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در جریان درگیری‌های ۲۴ ساعت اخیر در جنوب‌لبنان تاکنون ۴ سرباز اسراییلی کشته شده و ۱۷ تن دیگر زخمی شده‌اند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17769" target="_blank">📅 14:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">داداش مسعود الان لابد فهمیده  چرا الان آدم حسابش کرده اند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17768" target="_blank">📅 12:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17767" target="_blank">📅 23:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شریعتمداری:
مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/17766" target="_blank">📅 22:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diJiqiKd-hxBUuTBUlv02q0v7QgY28o5Q78Dv3QXJn_tNDIDxvs6BcRWo99SY0YM4vWT2KjMoK5tV34F1ckejOwxFIy-wyS0ThZgyF0r_aj9ZtNuIECLoWZaPtm2eAcjrtxhQXWq2kw5tmaDnAWw2CdEireNksOgho9beM2NIwU-8dYD7iq_kCBdQHcVA4UfU2-iGF6DaHyVRSCbW4W6UbBOzKWlGc7Qc-nfgpKGOEZkhx5pzwaqavdqVCjm9493DJWbLF1sEeNiIjopfv1Z-nls4VMno4xypXnAnxd3ZrSVUF13X6PTEjuCNdrpcvKT5w7BoYnnSpugt5VeSbaFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر از چکیده پیام رهبری</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17765" target="_blank">📅 22:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چه کسی گمان می‌کرد روزی این امضای موزگونه زیر برگه ای بخورد که امضای ابوایوانکا هم روبروش باشد؟!  سبحان الله !</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17764" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ :  «اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»   «بهتر است مراقب باشی، جی‌دی!»  «او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17763" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17762">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
🔹
بسم‌ الله‌ الرّحمن ‌الرّحیم
ملّت پرشور و باوفای ایران
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی و با حُسن نظر، تلاش‌های زیادی را به‌عمل آوردند و البته این رئیس‌جمهور آمریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد.
🔹
بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت حقوق ملّت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه‌ی آن را صادر نمودم‌. ایشان همچنین تصریح کرده‌اند که اگر طرف آمریکایی بخواهد زیاده‌خواهی کند زیر بار آن نخواهند رفت. از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. امّا بدیهی است مذاکرات حضوری که در آینده برقرار خواهد شد، به معنی پذیرش نظر دشمن نخواهد بود. امیدواریم که دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع نصرت‌ها و فتوحات، برای ملّت باشرف ایران به ارمغان آورد.
🔹
والسّلام علیکم و رحمة الله و برکاته
✍
سید مجتبی حسینی خامنه‌ای
🗓
۲۸/خرداد/۱۴۰۵</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17762" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17761">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17761" target="_blank">📅 20:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده:   ناو‌های نیروی دریایی ایالات متحده برای اطمینان از رعایت تمام مفاد توافق‌نامه در منطقه باقی خواهند ماند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17760" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده:
ناو‌های نیروی دریایی ایالات متحده برای اطمینان از رعایت تمام مفاد توافق‌نامه در منطقه باقی خواهند ماند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17759" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17758">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-poll">
<h4>📊 در عصر مدرن، کدام کشور زیرساخت‌های نظامی زیرزمینی را به یک استراتژی ملی تبدیل کرد؟</h4>
<ul>
<li>✓ آلمان</li>
<li>✓ سوییس</li>
<li>✓ کره شمالی</li>
<li>✓ سوئد</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17758" target="_blank">📅 20:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17757">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام بسیار مهم رهبر معظم انقلاب حضرت ایت الله خامنه‌ای مدظله‌العالی درخصوص تفاهم پایان جنگ خطاب به ملت ایران تا ساعتی دیگر منتشر خواهد شد</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17757" target="_blank">📅 20:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ونس در مورد ایران و موشک‌ها:   ما انتظار داریم که به عنوان بخشی از توافق نهایی، ایران موشک‌هایی که کل جهان را تهدید می‌کنند، نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17756" target="_blank">📅 20:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ونس در مورد ایران و موشک‌ها:
ما انتظار داریم که به عنوان بخشی از توافق نهایی، ایران موشک‌هایی که کل جهان را تهدید می‌کنند، نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17755" target="_blank">📅 20:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فایننشال تایمز:
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌ های بلوکه‌ شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17754" target="_blank">📅 20:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آفند زرهی سنگین حاجی فتل به جوان دانشمند بمال صداوسیما
نابودش کرد !</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17753" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ فاش کرد که حملات و بمباران‌های ایالات متحده بیش از ۱ تریلیون دلار به ایران خسارت وارد کرده است.  «بازسازی آنها ۱۵ تا ۲۰ سال طول می‌کشد. بنابراین باید خودشان رفتار کنند. اگر رفتار خوبی نداشته باشند، دوباره ضربه می‌خورند.»  ترامپ همچنین تأیید کرد که ایالات…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17752" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTixObeuxv3DG1zvjDJ7OtVGNpzj2i-31PQXcD4aKvYKOxx6qeJLx74nSZTRKP26AOfiJVcUhJek2rVJovrOawXgx-ntRMtHcc43AAOcFfYjlzrvRz-9cCeNcL0yFqM1MrWNE2eXQ9bntEYRFVaBvrOIcx4CnQ09MjYV_rjJQEp3COi33jYOctMSN_wQnLdQ7EqSKjX22iJSI7_nv5H6WJovDWK6oIrPQS7K8Fnu3TrLEVK4tf0czANGzN_3zk3Yk8WouHwcPa3IAq_GrJJg5NfGvB8XrPy3B1bdLrTGr3KaegDsaATANb6SSWI98T0XNJkm4OVZImvBnNhumclGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی کانالهای ارزشی این عکس را منتشر کرده اند و نتیجه گرفته اند انتخاب این مدل و رنگ لباس از سوی پزشکیان نمیتواند اتفاقی باشد!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17751" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
