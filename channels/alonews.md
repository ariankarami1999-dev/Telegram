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
<img src="https://cdn4.telesco.pe/file/fGpM3Wtb8_UP4XsjmRS75dQQ48LrT8duiDKIfJ6iDAuETtFfK3h3QaJFHWfVnkhrQTukCCFqS7LoiVPlg7maYb1SsWj-bv0WbC7Is8qx6jPmWGFegXpBtgAGXECi-0cpqBhHNxlW6QZLmgcti1SWRR0KBdrAJo216T4y4zYFuj6Sao1pnGNsrjUoiLn1Ujf1PTbdwgyqBPh0w-q-xzZMrpcAOsVCtKKKGFnCS0RoKXBLOZp4klKLpjG1FHj45XcZvX755183CDoFpJ6U9CzaqeW5tfNnEPbnZhJbS0kb_VaesrQiSH1E4h4oth1W5BL9pANlsOWzGUnzbOhkFtn3pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 22:11:08</div>
<hr>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: فرمانده منطقه شمال به حزب الله دستور داد پرتاب یک پهپاد انفجاری به سمت نیروهای اسرائیلی را در 24 ساعت گذشته پنهان کند و جزئیات بیشتری از فعالیت این نیروها منتشر نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/140463" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رمضان‌زاده، سخنگوی دولت اصلاحات: باید جمهوری اسلامی خودش را به پیمان‌نامه دفاعی «مکه» الحاق کند تا اولین پیمان‌نامه بدون حضور اسرائیل امضا شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/140462" target="_blank">📅 22:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2yyHxPRVYuRJcLd5LeKM7cmRI_obWiInGmTRPmwiTWpqHCgCXIIc1iG_tKCUuOe9SheShsK7enQcHTPZi67-VJPhOA0ifIFvRa_P810wx1gBFcguwwvczDO3Ng9i45WWgS4y251I1hxknPXTEQ9DMKG_rGkVh70h3Fw0SaEA6_EncyNhwFaT14a2A_CtORlTGsQE-jiHKIM7-t0u1SVnbJNXfh-vJLZF82crqBHJw8x9x4JuNzewVacz5Cp3QltiziN5mgCRfeGZ-je4KZjKlcChc1ROenobbTBqQiOoF7Buas97ugE8_LsdD38RoARMgkidvjVB_4nvY_sEgH64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر وارد کانال ۱۸۶ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/140461" target="_blank">📅 21:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBlRbu5xeKo7wdflnA66IDx-3uFAUPxupcgTdWaPvkKJnf55VCe8aaT4oOtw9EkDV7QyWOXasbNymHCODlkZQsf8flmBZ16smnHcRbJKGBT2cOC9Q6uXbmj-9GONobGY4-92eojeEtllx1xFKF8p5ziBe7HoOnIWT7-L_t3Zir2BCJmKxTZZ7AbT2n11mu42MFzobWThi523ityaYs0OWL7X38AkawHPAhkKt-xoWC3nMnp-mqx463Jd2k2QenObpGDXvyLJ2Fo4s4N0IaRb5goXQk0TPe4kyyRRofQvDhBkgmpIcqVPK2QDu3aQH5Glfjk3rexL6edbl0ylPnscgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی
:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و قدرت خود را در برابر گران‌ترین ارتش جهان به رخ کشیدند.
🔴
وقتی مسلمانان متحد شوند، می‌توانیم با هر چالش و تهدیدی از سوی بیگانگان کینه‌توز، رویدَررو مقابله کنیم.
🔴
زمان آن فرا رسیده که تنها به خودمان متکی باشیم و برادری واقعی را در آغوش بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/140460" target="_blank">📅 21:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عربستان سعودی در طول ۳۸ روز اول درگیری، حدود ۸۶ درصد از ۲۸۰۰ موشک رهگیر PAC-3 خود را مصرف کرد و در ماه آوریل، تنها ۴۰۰ موشک باقی مانده بود.
🔴
ایالات متحده آمریکا نیز بین فوریه و جولای، حدود ۶۵ درصد از موشک‌های رهگیر پاتریوت خود را مصرف کرد و تعداد آن‌ها به کمتر از ۸۵۰ رسید، در حالی که قبل از جنگ با ایران، ۲۳۳۰ موشک رهگیر در اختیار داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/140459" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
المنار: بمباران توپخانه اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/140458" target="_blank">📅 21:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سازندگی : رئیس‌جمهور با استعفای "محمدباقر ذوالقدر" از دبیری شورای ‌عالی امنیت ملی موافقت نکرده است و به او گفته که کماکان به مأموریت محول‌شده با قوت و قدرت ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/140457" target="_blank">📅 21:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEjz0j8vkcOvpEK8IM9fulzaTKwVuDNW1mCImWpa4YFg_ua9bvrexdIbPKKjoJU-aUGlPG5dFsDvfBEMneFj7InVE_ryAFmjShhOuto07v0LWbEdU_MDlb64SfwI-QAAzmhX8Yxovz9rtMsRmuKFjWfxDdxl_aCHaPiAkVkscyOQlA3lBmGwBravXRcnrfeG2sMXgPR9sDuUVxKwlmNhJkzDiCFpC00SxdMbdKBoiBjRsJ5wt2h80fQFgwzA9kHNYM0L7mtiNPNj6Lz-JTlz-lQXIFQFjyvgJc_FTncgJfWgB5T1hH9WYbLiyTjr_I89Fed_3lONSW8qVFLAmWwOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: مذاکره‌کنندگان ایرانی منتظر تایید نهایی شعام در مورد توافق با عمان و آمریکا هستند.
‏
🔴
«انتظار داریم این تایید به زودی انجام شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140456" target="_blank">📅 21:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رسانه‌های عراق اعلام کردند که رئیس سازمان اطلاعات عربستان با علی فالح الزیدی نخست وزیر عراق دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140455" target="_blank">📅 21:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سنای آمريكا لايحه تحريم‌های گسترده انرژی روسيه را با ۸۶ رای  برابر ۱۱ رای تصويب كرد و آن را به مجلس نمايندگان فرستاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/140454" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJSKBT2kjvrcamFhKE6fWY7o2W5_D91I-NT2V_uqAvhgIHP9anBp9iyaBEkGwAksLa1wSZ3jKSU5qiq83vEfnRgmNKN5WYSz6fv5K1dZXAaik7VL8WdQhrCvynENv_t4zDck8dNxY8dIO-B9-H_qPkGxWJk_5YAWbhP509Zf5dUyuxrRE2ny5EE4S-w9Apv0rG_JwID0oGzMj2fQZTDo__Yc6fiTI3582MAfF33X0JGNawO0OxyPueaN-d4Xz3BOVkNOS0O4hGc5gd3LqWlwEyBh9stPoHgU_gGpSCCF-wYJRaS44BiMPU-XTEWNxJOqhNhGpNiD9bUTOc8_GEqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پرونده «مرکز نظامی» واشنگتن را به دیوان عالی آمریکا می‌بریم
🔴
دونالد ترامپ اعلام کرد دو قاضی دادگاه تجدیدنظر فدرال که در دوره‌های باراک اوباما و جو بایدن منصوب شده‌اند، علیه ایجاد آنچه او «مرکز نظامی ضروری برای امنیت ملی واشنگتن و آمریکا» خواند، رأی داده‌اند.
ترامپ این حکم را «ناعادلانه» توصیف کرد و گفت دولتش فوراً به دیوان عالی ایالات متحده اعتراض خواهد کرد تا این تصمیم به‌طور کامل لغو شود. توصیف این مرکز به‌عنوان ضرورتی برای امنیت ملی و همچنین «ناعادلانه» بودن رأی دادگاه، موضع شخصی ترامپ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/140453" target="_blank">📅 21:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
یان برمر، تحلیلگر امریکایی: «توافق‌نامه دفاع مشترک مکه» مسیری کاملاً متفاوت با پروژه توافق‌های ابراهیم در خاورمیانه را نشان می‌دهد
🔴
یان برمر، تحلیلگر امریکایی نوشت: عربستان سعودی، ترکیه و پاکستان با تشکیل یک پیمان دفاعی، که عملاً می‌توان آن را هسته مرکزی یک ائتلاف اسلامی دانست، در حال پاسخ به جنگ آمریکا و ایران و این برداشت هستند که دیگر نمی‌توان برای تأمین امنیت منطقه به ایالات متحده تکیه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/140452" target="_blank">📅 20:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بقائی در واکنش به سخنان ترامپ: پیش از آنکه کسی بتواند ادعای «غنائم جنگی» کند، ابتدا باید در جنگ پیروز شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140451" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
جنبش انصارالله اعلام کرد که یک حمله موشکی بالستیک و با استفاده از پهپادها علیه اردوگاه «صحن‌الجین» متعلق به نیروهای مسلح یمن وابسته به شورای انتقالی جنوب (PLC)، در شمال شرقی شهر مأرب، در یمن، انجام داده است.
🔴
این حمله به طور خاص به نیروهای یمنی و " مزدوران" (احتمالاً نیروهای سعودی) و همچنین انبارهای، خودروها و تجهیزات نظامی هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140450" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27c2dba3c0.mp4?token=sWi5Tmwus1fXE96mwF-KvUvj94NwvHHJjD1fa9XD9bIMYlxL1VXxTY-22h_k89_nYo1JINlSWKXOem727OxWRzgoOgtuzOybNZhMaO6HueJgkqrAXaTAAY8yGRuNZ39tnjbE4XlRZCOboaNos9TAoVdC8mVn-J6j3Fa6-IpIxZoln3kO9y-9lhs2eVukyQL5vde6jEy4xCh8Hz8D_LLzqG57HPI4FMuvBwYgF2I5--QrEL8l7OTElzCa1pf4Bq4dK55_CS-q40_UKj19ke_Ea3iN4z7z5lyOmBN7V4vJJq2ZbBaAPRARstR0old1xSeIrDQw9elbK-t5ljYygdw7hodmSMvCKfVVlb3J4gwXAU2dpOcy_IFyq0DT-7VCW_RFJaeOHyyzi4eKEbGninCfjHobjpjraaUnqx7HtcSwwY0afk5H3luuwmqtHQk83TesRG914ONS0MVRViPjg5MQz3stbQmNTexDMrzTYALFwsQurh8AVDFxB0_E76xEgBqIoC0NfpOOlhPbgJl8D296hPdh5Y7TZLjSVy40ypoy7-PXiYZvQlla8dgiNNvV8MGPMvnHyTBBEwvoMV9lIcFTWLBAdvchJ4v3dRTd-AKGfygW8x2TdtrU6HYPRjZGz5Hdc5_410e-5t2y4z5yxVa86vs2yOJQ_XvwUNMBq7W7NTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27c2dba3c0.mp4?token=sWi5Tmwus1fXE96mwF-KvUvj94NwvHHJjD1fa9XD9bIMYlxL1VXxTY-22h_k89_nYo1JINlSWKXOem727OxWRzgoOgtuzOybNZhMaO6HueJgkqrAXaTAAY8yGRuNZ39tnjbE4XlRZCOboaNos9TAoVdC8mVn-J6j3Fa6-IpIxZoln3kO9y-9lhs2eVukyQL5vde6jEy4xCh8Hz8D_LLzqG57HPI4FMuvBwYgF2I5--QrEL8l7OTElzCa1pf4Bq4dK55_CS-q40_UKj19ke_Ea3iN4z7z5lyOmBN7V4vJJq2ZbBaAPRARstR0old1xSeIrDQw9elbK-t5ljYygdw7hodmSMvCKfVVlb3J4gwXAU2dpOcy_IFyq0DT-7VCW_RFJaeOHyyzi4eKEbGninCfjHobjpjraaUnqx7HtcSwwY0afk5H3luuwmqtHQk83TesRG914ONS0MVRViPjg5MQz3stbQmNTexDMrzTYALFwsQurh8AVDFxB0_E76xEgBqIoC0NfpOOlhPbgJl8D296hPdh5Y7TZLjSVy40ypoy7-PXiYZvQlla8dgiNNvV8MGPMvnHyTBBEwvoMV9lIcFTWLBAdvchJ4v3dRTd-AKGfygW8x2TdtrU6HYPRjZGz5Hdc5_410e-5t2y4z5yxVa86vs2yOJQ_XvwUNMBq7W7NTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا سالانه ۴۰ میلیارد دلار به سوئیس می‌دهد؛ بدون ما با مشکلات جدی روبه‌رو می‌شوند
🔴
دونالد ترامپ مدعی شد آمریکا عملاً به برخی از ثروتمندترین کشورهای جهان یارانه می‌دهد و سوئیس را یکی از این کشورها دانست. او گفت ایالات متحده سالانه حدود ۴۰ میلیارد دلار در اختیار سوئیس قرار می‌دهد و بدون این مبلغ، این کشور دیگر جایگاه فعلی خود را نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140449" target="_blank">📅 20:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: خیلی‌ها می‌گویند من یکی از بزرگ‌ترین رؤسای‌جمهور تاریخ هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140448" target="_blank">📅 20:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تصاویر جدیدی از توقف کشتی‌ها در شمال تنگۀ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140447" target="_blank">📅 20:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f48f2a3f4.mp4?token=H_rxKHCXdmwN6-GvNT7FYqVIHVJN6L2PK4FKtcBkCqnfQLq19fvkPl3TxDRR8M-7GAVq4kNeU39Y7fq45uzNyc6jYNvaL0h5nQyc7wYyK5ouoWN3xsUdLs1ZZ6fxmskmWpH-bDV07RrM_Gz5Vdx4m-D8JyhOwgn8SEKMGUFqT1zXwYo3eOLGfR7w3aejLRamI0oBmsYaNdHdKfLvS0cBOvH7PpL3jH2Hx1T0e4U28QRJkAD4_MphykatOKHIyGOh00OOgtUAG6CYhXHThKRmm4NAHbt-ZXwyTUZFTcrKzfl08MQk57g3MtZFRmGxyXW0dZMy41DBVa9mQOJCL71Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f48f2a3f4.mp4?token=H_rxKHCXdmwN6-GvNT7FYqVIHVJN6L2PK4FKtcBkCqnfQLq19fvkPl3TxDRR8M-7GAVq4kNeU39Y7fq45uzNyc6jYNvaL0h5nQyc7wYyK5ouoWN3xsUdLs1ZZ6fxmskmWpH-bDV07RrM_Gz5Vdx4m-D8JyhOwgn8SEKMGUFqT1zXwYo3eOLGfR7w3aejLRamI0oBmsYaNdHdKfLvS0cBOvH7PpL3jH2Hx1T0e4U28QRJkAD4_MphykatOKHIyGOh00OOgtUAG6CYhXHThKRmm4NAHbt-ZXwyTUZFTcrKzfl08MQk57g3MtZFRmGxyXW0dZMy41DBVa9mQOJCL71Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی برای اولین‌بار از زمان شروع جنگ، وارد صربستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140446" target="_blank">📅 20:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت ورزش و جوانان : ۱۸ میلیون زن و مرد ایرانی بدون حتی یک بار ازدواج وارد ۴۰ سالگی شدن.
🔴
بخاطر شرایط اقتصادی و کسب تجربه از زندگی مشترک دیگران و هم چنین لذت بردن از تنهایی،بسیاری از جوونای ایرانی ترجیح میدن هرگز ازدواج نکنن و تا آخر عمر تنها بمونن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140445" target="_blank">📅 20:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d279dcf86.mp4?token=rzJRy2i-K1MgQZ09LXNLzAznZol9ihXqHZVIN7GinoFAAWwOBNjO0n5AQzjFOjTmyT_vrkQyf58AFYIES_Qq3DJlBbS53DfAH2WRUQ8gYrRO1JnGJdWxTX5fxz7ML24MuFUsvgVmnTKCxixYre--QXgUyQ-P1xAdSe1MeUquMiOxkVwKKwPYa8I3eJt_w6Eny4xFhVP32xRQMUPaSS6Vt9Hl6WRKrl7s23srhw0b74VBECSKe6nO4WNU6xmhzrV6qALU_kyF5Q01wuKfWbVOh4J34rS9AVwHmjUV4WGuzPfsTX5fzwDg10m3B72t7o44KHIgfNK3T7y1vNWgK28jUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d279dcf86.mp4?token=rzJRy2i-K1MgQZ09LXNLzAznZol9ihXqHZVIN7GinoFAAWwOBNjO0n5AQzjFOjTmyT_vrkQyf58AFYIES_Qq3DJlBbS53DfAH2WRUQ8gYrRO1JnGJdWxTX5fxz7ML24MuFUsvgVmnTKCxixYre--QXgUyQ-P1xAdSe1MeUquMiOxkVwKKwPYa8I3eJt_w6Eny4xFhVP32xRQMUPaSS6Vt9Hl6WRKrl7s23srhw0b74VBECSKe6nO4WNU6xmhzrV6qALU_kyF5Q01wuKfWbVOh4J34rS9AVwHmjUV4WGuzPfsTX5fzwDg10m3B72t7o44KHIgfNK3T7y1vNWgK28jUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:
من اگر بخواهم استعفا بدهم رسما اعلام می‌کنم!
🔴
آنهایی که به تفاهم‌نامه می‌گویند شکست، حرف اسرائیل را می‌زنند
🔴
برای جهالت انسان همین قدر کافی است که نداند قدرتش چقدر است.
🔴
یا رهبری را نشاختند یا منطق و عقل سرشان نمی شود. ما به آمریکا چه دادیم؟! کلی دستاورد داشتیم.
🔴
آنچه به اسم تفاهم نامه نوشتیم با قدرت از آن دفاع می کنیم، آنهایی که می خواهند آن را شکست لقب بدهند من می گویم که بی انصاف هستند و این چیزی است که اسرائیل می خواهد و دانسته یا ندانسته دارند پیام منتقل می کنند.
🔴
کنار گود ایستادند و  می‌گویند این جوری است و فردا هم اگر مشکلی پیش بیاید باز هم می گویند چرا این جوری شد.
🔴
از اقتصاد نظر می دهند، از سیاست نظر می دهند، جامعه شناسی نظر می دهند. من نمی دانم این علم را از کجا آورده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140444" target="_blank">📅 20:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
غریب آبادی: امنیت خلیج فارس باید به دست کشورهای منطقه تأمین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140443" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
🔴
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.
🔴
آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.
🔴
این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/140442" target="_blank">📅 20:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WZX-DWKVVdumy-5MkS9wqtYlMFtVCJg4rAF8IF5GP4pLCNipkE1H3LhtjH8nDqDx3wvnHofWSu3jmqO--YKV1Ks3jVd0a2QvMUKOpd1gHL435T22vc9gQ0H2y_xqesUWy8jOwvr9JSvCiSlp8zlqbX3dl5hg-wm31TW4MS0FgHFj8R-Zrbt6y5FwOGm1LMu855E53pHNFaGDVG8b7zHLPzPifFXDWxE9PTuuBBkFpb5BcBz3xeo0hAeITH_Cagl9cowm_1Xw3NoTWUysiTmmigNzPYKjQHXPLiPkGNxNOt56z3hSCbmxg3gsVmkxOEsd_ogwWF9fnsnu5HFzdeHBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنبش مقاومت اسلامی عراق اعلام کرد که عملیات برنامه‌ریزی‌شده علیه پایگاه‌های عربستان سعودی و آمریکا در غرب آسیا را به تعویق می‌اندازد، این اقدام در پاسخ به فراخوان قبلی مطرح‌شده توسط هادی العامری و سایر رهبران سیاسی عراقی صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140441" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خارجه آمریکا در بیانیه‌ای اعلام کرد اقدامات جدیدی برای قطع مبادلات مالی با ایران انجام داده است.
🔴
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140440" target="_blank">📅 19:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=ilnuMiAadNaSc0oCGPrD2ZJg8W3RYfeKwD8kkfRMwjrBZ19b8MyabVpYRgyhunXdxP8u3LQSRBTrZkVSzCDBpCF96qWZykV-Hj2iip4o-Q_ze3eU7m794WAs2AWSoNrx_UtdHZsv_lD8A2VBMWdchbjxUCc6kXL2tTcvtfERF3F3gAa1vpyK4vFtG8MrOL72JbKTRku4EPQkqZpY_6lpICgXTIcg9TqeU0hs_cQYDva61CDNF8LthU_8TQv8Ppjwys7KWj1_CddzLIXbljK02_a9bQfoWwhAhPQVkqpoZJfM1A8eF-jAhuOb_N03moH-SjB06kCUNACB2VKL5DEWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=ilnuMiAadNaSc0oCGPrD2ZJg8W3RYfeKwD8kkfRMwjrBZ19b8MyabVpYRgyhunXdxP8u3LQSRBTrZkVSzCDBpCF96qWZykV-Hj2iip4o-Q_ze3eU7m794WAs2AWSoNrx_UtdHZsv_lD8A2VBMWdchbjxUCc6kXL2tTcvtfERF3F3gAa1vpyK4vFtG8MrOL72JbKTRku4EPQkqZpY_6lpICgXTIcg9TqeU0hs_cQYDva61CDNF8LthU_8TQv8Ppjwys7KWj1_CddzLIXbljK02_a9bQfoWwhAhPQVkqpoZJfM1A8eF-jAhuOb_N03moH-SjB06kCUNACB2VKL5DEWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عطریانفر: پوست قالیباف به اندازه‌ای کلفت است که خیلی نگران اهانت تندروها به او بابت مذاکره و توافق نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140439" target="_blank">📅 19:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کانال ۱۴عبری: شواهدی از وخامت حال مجتبی خامنه‌ای وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140438" target="_blank">📅 19:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عبدالرضا داوری: ایران به توافق مکه وارد نمی شود، چون قدرت ایران ناشی از استقلال آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140437" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع در وزارت خارجه پاکستان: به احتمال زیاد، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه به پاکستان سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140436" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
به گزارش هیل، دونالد ترامپ گفت رأی‌دهندگان حزب جمهوری‌خواه در آستانه انتخابات میان‌دوره‌ای از عملکرد جمهوری‌خواهان حاضر در کنگره ناراضی و خشمگین هستند.
🔴
ترامپ مدعی شد این نارضایتی متوجه او نیست، بلکه متوجه نمایندگان جمهوری‌خواه در کنگره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140435" target="_blank">📅 19:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرنگار ارشد کاخ سفید: سنای ایالات متحده رسماً بررسی تحریم‌های سنگین علیه روسیه و ایران را آغاز کرده است.
رأی‌گیری نهایی ممکن است امروز برگزار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140434" target="_blank">📅 19:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پایگاه اینترنتی نیروی دریایی ترکیه: یک کشتی باری با پرچم ترکیه در سواحل بندر نووروسیسک روسیه هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140433" target="_blank">📅 19:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140432">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
معاون وزیر امور خارجه : اگر به شرایط صلح برگردیم، احتمالاً جلسات امنیتی بین کشورهای منطقه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140432" target="_blank">📅 19:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140431">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
المیادین: اطلاعات اولیه حاکی از آن است که نیروهای مسلح یمن یک عملیات جدید را علیه اردوگاه‌های سعودی انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140431" target="_blank">📅 19:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140430">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
اوپن سورس(رسانه نزدیک به ارتش آمریکا) : حال مجتبی خامنه ای مجددا رو به وخامت رفته و هرلحظه ممکنه از دنیا بره،اینو نزدیکان پزشکیان تایید کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140430" target="_blank">📅 19:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140429">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دادگاه تجدیدنظر آمریکا دستور توقف ساخت‌وساز سالن رقص کاخ سفید را صادر کرد و اعلام کرد ترامپ برای ادامه و تکمیل این پروژه باید از کنگره مجوز بگیرد.
🔴
به این ترتیب، پروژه‌ای که قرار بود با تصمیم کاخ سفید پیش برود، حالا به چراغ سبز قانون‌گذاران وابسته شده است.
👈
حتی ساخت یک سالن در کاخ سفید هم از سد تفکیک قوا عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140429" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140428">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
به گزارش بلومبرگ، دونالد ترامپ اعلام کرد اگر صلاحیت «تاد بلانش» برای تصدی سمت دادستان کل آمریکا در سنای این کشور تأیید نشود، او را همچنان به‌عنوان دادستان کل موقت حفظ خواهد کرد.
🔴
این اظهارات در حالی مطرح شده که روند بررسی صلاحیت بلانش در سنا با چالش‌هایی روبه‌رو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140428" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140427">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1129161947.mp4?token=mHyhncj5nn0RseK6Oz9LUNdca5EYJ2QQDiZEa2T5FDccqQh7E4VkUeQpBLuPeiB9zzCAgZlyK_083EfwfH1LRdg8wSTEo7e36mL-td39qsSZEap9gAan_WfN8y2TLnHq8l8CeiJZ-hqG-hE93KqClwifgCF_iZjjyixcIdCHtzfJpOYeclmtkYbSRn2yPGLzLGge25r-LHZwW28iio4Be1rH2-wKMlJ5HgM6QpS3-o2Dlpk7MTNsAbVRDTQRxnU6FoaqLB70N3BGrtnootuMW6W3FXYVXRF_7MWd3Ci-1eYBWGoIjrPja1KiqmBXAFNEscaTcO6k_oVOv-Dwi-IzEiLVY-TygwzZcOX2KiNz2z7pt27Jtuz-69FUEnke3TRWogCHpOHcVT8SlJYRmgAgpJA_y6wo9q10Xww2z_EXawdWjt_s9pBd-VBgeUHNPh45FOyV6ayD7tg79Sp5uvlyeldjTKEqzlYM9Egdf8Fo0O91GNVxffaQ-4kxh-qNf5X2OWKi_rRVEmJJVCBmkfrxwtaNsRXtIW_2bTflr-H6vnzcJVHVzL3dzbVXRQ5qSZSLhWVMvm2y5K1lZTkGJYD8j3sSV15Tjj0YTTPSUpORE7LlzxKWmDSg-x_VXIrJzpBm_mF0o2hLd70jy2FqvF_qJ0GmmFcGedNgxKc8EDsMQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1129161947.mp4?token=mHyhncj5nn0RseK6Oz9LUNdca5EYJ2QQDiZEa2T5FDccqQh7E4VkUeQpBLuPeiB9zzCAgZlyK_083EfwfH1LRdg8wSTEo7e36mL-td39qsSZEap9gAan_WfN8y2TLnHq8l8CeiJZ-hqG-hE93KqClwifgCF_iZjjyixcIdCHtzfJpOYeclmtkYbSRn2yPGLzLGge25r-LHZwW28iio4Be1rH2-wKMlJ5HgM6QpS3-o2Dlpk7MTNsAbVRDTQRxnU6FoaqLB70N3BGrtnootuMW6W3FXYVXRF_7MWd3Ci-1eYBWGoIjrPja1KiqmBXAFNEscaTcO6k_oVOv-Dwi-IzEiLVY-TygwzZcOX2KiNz2z7pt27Jtuz-69FUEnke3TRWogCHpOHcVT8SlJYRmgAgpJA_y6wo9q10Xww2z_EXawdWjt_s9pBd-VBgeUHNPh45FOyV6ayD7tg79Sp5uvlyeldjTKEqzlYM9Egdf8Fo0O91GNVxffaQ-4kxh-qNf5X2OWKi_rRVEmJJVCBmkfrxwtaNsRXtIW_2bTflr-H6vnzcJVHVzL3dzbVXRQ5qSZSLhWVMvm2y5K1lZTkGJYD8j3sSV15Tjj0YTTPSUpORE7LlzxKWmDSg-x_VXIrJzpBm_mF0o2hLd70jy2FqvF_qJ0GmmFcGedNgxKc8EDsMQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز: بیش از ۱۳۰۰ مهاجر زیر سن قانونی در سئوتای اسپانیا بلاتکلیف هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140427" target="_blank">📅 18:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در سواحل یمن؛ احتمال هدف قرار گرفتن یک کشتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140426" target="_blank">📅 18:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140425">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: بهای نفت تنها در صورتی افزایش می‌یابد که ناچار شویم ضربه تازه‌ای به ایران وارد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140425" target="_blank">📅 18:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
حوثی‌ها: توافق دفاعی عربستان، ترکیه و پاکستان معادله را تغییر نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140424" target="_blank">📅 18:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140423">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
امارات اعلام کرده که تنها در این هفته، سه کشتی متعلق به این کشور هنگام عبور از تنگه هرمز مورد حمله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140423" target="_blank">📅 18:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140422">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات ارشد دولتی امریکا: پس از تماس ترامپ با معاون وزیر دفاع در مورد میزان مهمات، مقامات ارشد دفاعی برای یک جلسه لحظه‌آخری در آن شب فراخوانده شدند
🔴
این جلسه برگزار شد تا راه‌هایی برای افزایش سریع تولید مهمات حیاتی راه‌اندازی شود
🔴
معاون هگست سعی کرده با ارائه مشوق‌هایی سرعت تولیدتسلیحات را افزایش دهد
🔴
هگست و کین به‌طور خصوصی با قانونگذاران دیدار کرده‌اند تا حمایت آنها را برای درخواست هزینه‌های خود جلب کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140422" target="_blank">📅 18:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140421">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیرۀ‌ استراتژیک نفت ایالات متحده به کمترین میزان از سال ۱۹۸۳ رسیده است.
🔴
این ذخیره هم‌اکنون تنها معادل ۴۳ روز مصرف نفت خام این کشور است و اگر نفت جدیدی به آمریکا نرسد این کشور با کمبود نفت مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140421" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140420">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نیویورک تایمز: بازرسان سازمان ملل ارزیابی کرده اند که ذخیره اورانیوم ایران برای ساخت ۱۰ بمب هسته‌ای کافیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140420" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140419">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق، شامل آتش‌بس ۳۰ تا ۶۰ روزه، خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140419" target="_blank">📅 18:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCEYmvp00AIGCQdIXTfzyYJz6GWmwhQ272--zJnbJbEDApvSk5wvRJV6fdThVVMQvr6lku0NFBBxvSA9O7EYhZzJlMwuc-I7iTWUjv2VCRBepBL3pDmIoIcmW-ZA29QXFErAp6O2YZlWZ2yLAsgEulaIP3OEJYANM8Th2mzNDY6zkx8EreqUHBAIg8a-uZXq7T0wt9tkG9YV5KWEW7AeJHkn_5AmROE6xGpHlPvwYzYeJDiyphQIGzu00mCeWSRPUuJRmEpkpziPeqq-eaqz-FLI0-SclJ3sPT-7X0w091_r8DgBMctMEPJa0qk7UNkkSKXd2OmdAk5pswVsDQfE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی اعلام کردند، سرلشکر عبدالله العنزي، مسئول واحد پهپاد های سعودی در حملات نیروهای مسلح یمن کشته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140418" target="_blank">📅 18:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
متن توافق مکه منتشر شد
🔴
۱. توافق مکه یک همکاری متمرکز بر دفاع است که هیچ کشور خاصی را هدف قرار نمی‌دهد و هدف آن تقویت تعهدات برای حفظ صلح، ثبات و رفاه منطقه‌ای و جهانی بر اساس تقسیم بار مسئولیت و درک مشترک از امنیت است.
🔴
۲. هدف این توافق‌نامه تقویت بازدارندگی جمعی در برابر هرگونه اقدام تجاوزکارانه است و تصریح می‌کند که هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله‌ ای علیه همه آنها تلقی خواهد شد.
🔴
۳. توافق مکه نتیجه ملموس تلاش‌های دیپلماتیک بلندمدت است که مطابق با اصل مالکیت منطقه‌ای برای ایجاد زمینه مشترک برای مبارزه با تهدیدات امنیتی فزاینده منطقه‌ای و بین‌المللی انجام شده است.
🔴
۴.توافق مکه که به معنای قطع هرگونه اتحاد یا توافقی نیست، با تکمیل روابط اتحاد موجود، امنیت منطقه‌ای را تقویت می‌کند و زمینه‌ای برای همکاری با مشارکت سایر کشورهای منطقه ایجاد می‌کند.
🔴
۵. عضویت ترکیه در ناتو و مشارکت‌های منطقه‌ای جایگزین یکدیگر نیستند، بلکه ساختارهای مکملی هستند که امکان تقسیم بار امنیتی را فراهم می‌کنند.
🔴
۶. این توافق یک جبهه نظامی تهاجمی، تلاش برای مهار یا طرحی برای حمله نیست؛ بلکه گامی است که به هدف ایجاد منطقه‌ای عاری از ترور با هدف تضمین ثبات منطقه‌ای کمک خواهد کرد.
🔴
۷. توافق مکه هیچ کشوری را هدف قرار نمی‌دهد و کانال‌های موجود گفتگو را نمی‌بندد.
🔴
۸. این توافق‌نامه صرفاً ماهیت دفاعی دارد، نه تنها با تعهد سه کشور امضاکننده به حمایت از دفاع یکدیگر، بلکه با تعهد آنها به افزایش همکاری و قابلیت همکاری در صنعت دفاعی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140417" target="_blank">📅 17:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه: توافق‌نامه مکه برای دفاع مشترک «گامی تاریخی» است. توافق مکه علیه هیچ کشور مشخصی نیست. این توافق‌نامه با هدف تقویت امنیت مشترک و بازدارندگی جمعی سه‌کشور امضا‌کننده است و در صیانت از صلح و ثبات در منطقه نقش خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140416" target="_blank">📅 17:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آسوشیتدپرس: فشار ناشی از جنگ علیه ایران، بازار کار آمریکا را بهم ریخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140415" target="_blank">📅 17:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEBGzyf3G2f129fftmJbkz01XMSKe0emk3pzwRr10WG6xW_hMAqkLM0tFM7pJ28sB7yysYmUcstVw9PiEd56MEetvuP10Nq_wIVkmiN4GKxZjzbBgicyPxTjJ0qYo5ppthF8EpPIPcGsUsijuZTRTvjYvoCzUeIpxyD3EsxiV-2MBXHIkQ86rCJmh-BuHN5htGzzYUZbW6y7kp-bzuP755BJjloJTBsYf0eWWSF-dUlLZw8y3kN5ZZ77SL_AqMOw20M30Z22G8ejcPlxaDr4qtAdLvnBMY9EKYgIa6tmO9fba3oCvbXP0wbHs9gLxFcr_Z5gMQJWs7yFK5424PanSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بار دیگر مقاله‌ای با عنوان «دونالد ترامپ، جنگ با ایران را برد» را منتشر کرد و آن را «مقاله ای که باید خوانده شود» نامید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140414" target="_blank">📅 17:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
موضع وزارت بهداشت درباره ظرفیت پزشکی کنکور ۱۴۰۵: خواستار اصلاح ظرفیت‌ها هستیم، اما هنوز پاسخ مشخصی نگرفته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140413" target="_blank">📅 17:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نشریه FT : یکی از دلایل اصلی عربستان برای رفتن به سمت این ائتلاف، حملات حوثی‌هاست
🔴
ریاض نگران حملات حوثی‌ها به کشتی‌ها تو دریای سرخ و تهدید مسیرهای مهم کشتیرانیه
🔴
به همین خاطر عربستان می‌خواد با ترکیه و پاکستان همکاری نظامی و اطلاعاتی نزدیک‌تری داشته باشه تا جلوی گسترش تهدید حوثی‌ها رو بگیره
🔴
این سه کشور قصد دارن اطلاعات امنیتی رو با هم به اشتراک بذارند
🔴
رزمایش‌های مشترک برگزار کنن و برای حفاظت از دریای سرخ و باب‌المندب هماهنگی بیشتری داشته باشند
🔴
چون عربستان معتقده حملات حوثی‌ها می‌تونه امنیت منطقه و صادرات نفت رو به خطر بنداز
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140412" target="_blank">📅 17:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نشریه FT:  به‌نظر می‌رسه محاصره دریایی آمریکا صادرات نفت خام ایران رو عملاً متوقف کرده
🔴
حدود یک هفته‌ست هیچ نفتکشی از جزیره خارگ، بارگیری نکرده
🔴
طولانی‌ترین وقفه از زمان شروع جنگ
🔴
داده‌های ماهواره‌ای و کشتیرانی هم نشون می‌ده اسکله‌های بارگیری خالیه و رفت‌وآمد نفتکش‌ها تقریباً متوقف شده
🔴
ایران فعلاً از فروش محموله‌هایی که قبل از محاصره صادر شده بود درآمد داره، اما اون محموله‌ها هم رو به اتمامه
🔴
ایران به‌جای پر کردن مخازن، تولید نفتش رو کاهش داده تا ظرفیت ذخیره‌سازی پر نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140410" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0343b54724.mp4?token=npWb9W4nZYO981O9eX93cCdRj0RtqdK7pHNLDIKaNkysvMpVUrYCYlcSID6PdUgQ8CFuQgV4tK4yMaDv0-qe367jX6e3TLvNCPlLSfJKzP4CaSZYYXroqZKcL9h7AWMDIpz3GskJPzVAu-Qfi15_uLd7oHHq4gzoBNQKVy52y_iuqIaxxHNwUt-yxMjmMMAFa1Vb2eGcKoYwv95qnytVYHIV-eTImGaWVvCuU0BJVxU-j-SdAmxi7_aHeBAEkF0-_HqqSjTphZ6LW5JgsGvhI-rFstiMCH0Go3lsDrvlLkACFhsqLbGj0GCy52mAQ5FWijSJAZtVvVNOM5CowP4lDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0343b54724.mp4?token=npWb9W4nZYO981O9eX93cCdRj0RtqdK7pHNLDIKaNkysvMpVUrYCYlcSID6PdUgQ8CFuQgV4tK4yMaDv0-qe367jX6e3TLvNCPlLSfJKzP4CaSZYYXroqZKcL9h7AWMDIpz3GskJPzVAu-Qfi15_uLd7oHHq4gzoBNQKVy52y_iuqIaxxHNwUt-yxMjmMMAFa1Vb2eGcKoYwv95qnytVYHIV-eTImGaWVvCuU0BJVxU-j-SdAmxi7_aHeBAEkF0-_HqqSjTphZ6LW5JgsGvhI-rFstiMCH0Go3lsDrvlLkACFhsqLbGj0GCy52mAQ5FWijSJAZtVvVNOM5CowP4lDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گفتگوی بن سلمان، اردوغان و شهباز شریف پس از امضای توافق سه جانبه مشترک
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140409" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT_HsEA2yHJmt6sBMtc75ika5GkBIc8am9Nw2XjthkZegp3ZCaa2e7D-zo5--XP6-Ic3uqOts38611KViKNy2y-_6bO5z7ibAMCdyssvstuMcYmEw3mXN9vIXojoK6070VApk2y8SB6bYeQLJs_vMwvwhvOPdnUWJLQr4jGyOX3O4w-csiKbkueLhT6fMYK-31Yw_FyDWH-96T6Jkmx7V5HIs8KvLp272iSKveHokw9o6SD9yMxQ55hVk0B2xmv_H0MWBs_Hed2seNO-DaoxvKxn_uSq6-PCio7FKG3c3WDXojYrcHAIfYrH-87-H36EnaCv1b3lXUBA55SUi8l_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگسث، وزیر جنگ آمریکا دقایقی پیش در حساب رسمی خود در ایکس متنی را منتشر کرد که عنوان آن “ترامپ جنگ ایران را برد” می باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140408" target="_blank">📅 16:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=DdvTpuyI4OGHVKKrKmhJ1PwsAlJADAlycrKHhxNRPIQaVhvUar3AklkIFw-49kz_RlDrtIYvzgdEEEBWZlQcghpI7JFL4HfuWPk-4V4myN0sGC9lMEqh44aPwEKFssrYpqNVnTq-BFRki2gIuvsimN_erhsBE_JVVkZ2DPmN_Ep-BfgKGVmZjdf8UhADS-M0yhzpEXeX8Z5P3iJZqaDZRT94HqQwd-cVzAggN3YVpgluXqGz_A-SWs4OE6qS5Yo1e61ucH1FbmNiiv2BVrqcn4_SpjMD3ddlSwjMB7L1gKM8oOjGPZwHP5LEJuuo21NoE1bevDQ1-P9yAI_hdaxccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=DdvTpuyI4OGHVKKrKmhJ1PwsAlJADAlycrKHhxNRPIQaVhvUar3AklkIFw-49kz_RlDrtIYvzgdEEEBWZlQcghpI7JFL4HfuWPk-4V4myN0sGC9lMEqh44aPwEKFssrYpqNVnTq-BFRki2gIuvsimN_erhsBE_JVVkZ2DPmN_Ep-BfgKGVmZjdf8UhADS-M0yhzpEXeX8Z5P3iJZqaDZRT94HqQwd-cVzAggN3YVpgluXqGz_A-SWs4OE6qS5Yo1e61ucH1FbmNiiv2BVrqcn4_SpjMD3ddlSwjMB7L1gKM8oOjGPZwHP5LEJuuo21NoE1bevDQ1-P9yAI_hdaxccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت جنگ ایالات متحده، پنجمین مجموعه از اسناد مربوط به یوفو ها را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140405" target="_blank">📅 16:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دولت اسپانیا ایتالیا را تهدید کرد که در صورت برنداشتن محدودیت های مرزی برای اسپانیایی ها تا یکشنبه، اسپانیا هم علیه ایتالیایی ها محدودیت مرزی وضع می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140404" target="_blank">📅 16:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بلومبرگ: نفتکش‌های حامل نفت عربستان برای جلوگیری از هدف قرار گرفتن، مقصد واقعی خود در دریای سرخ را پنهان کرده و بنادر مصر را به‌عنوان مقصد اعلام می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140403" target="_blank">📅 16:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va_W2RJUm-28PW73LPqoTha_jWcQLMcrIguF5DtXPpPmXo7GJYsodspKs23-CunSuiIknzNPnlvsiJA-Fm83-HKxU1B_WQnP1bRI0DR8D1nOjLMnI9Ot2209Ia8fXch57_yYOgsOwDceCugj0IKO7mdpMT6VcuQ-JAWOqDRM6le2KlagIpfvvybn8bHFCHc1vCrysUSb6jGqpx3AUVnwTVM_VZskTsKt20utBogzkf3g6FIayMvOr76e2kgVPCEhxYFOh-NEG3GyOjmby4uX298A672IBEbUGyVTgcz-MOj8BLVjl-VFBF9aoO3wAl2agcnhcuj29evTxTcLgBbjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از انتشار آمار جدید اقتصادی آمریکا قیمت جهانی اونس طلا ۶۰ دلار افزایش یافت
🔴
همزمان شاخص دلار تضعیف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140402" target="_blank">📅 16:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMNy_7D9DKPKzrQaHAy46py_KaL-PRbndNhAIk3M-nvrYk4NayeqavPmWH19X3EE0ZgdTJWT8ay4w-L8aFzMc3BXxWuXZ0nLAz0vB22V_nA9InXeYQbi_UZkWGQL8eOT1V8e0lFI8P3EsiAsvJ1gRtjlkBCcskNjGVoXK4XQhwjRBxrXlaOtrlWtbjrY2eWtTLzTh6ChqpDAfQRZtqmZvvTpD2dkecmMPvTlVJXZU9t262fBO5FBu6i9gxr-0vr8TOMI57d0vvppOM9udVyKzr4CgMYyPCqRa9s9sygGFR-5-UGqeJFY4Lqx9LsKlNHcb0qqmq_KEgIORHMiZjnAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: افرادی که می‌گویند جنگ را تمام کنید، منافق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140401" target="_blank">📅 16:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdYVgc4thnTEhxVIWMI5DNRIRgwYeBDeF6HxPVbijgVrDUlSqhh30LE9a5EmhMZCDog98n-CWv0_tN0j4evl75KOp_UMhNXAr3ocFduNOVdQl6t9MxLCVShn9r8L3yr__441-r8MOBKI8d7AS6hjjx6cOrgYjYrdXScGUvA4uYc1dFXTppy7bjH-y3TXeK5pwzNDQP3TictKkLUZ-OwPSno-WD5xk_DDkLloS9PXUYD9ZuGOPIOvBEEmzXLpMXJnxbXDNTzEfH3OEmM6bwciKSDcaVSgpbk8aqabnfws5zu1YytvWbmWhI4nJv5V8pl2oNRRphg7DSLZY5RVn6t3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی  در ایکس:
🔴
عربستان باید درک کند که یک توافق کاغذی با ترکیه و پاکستان امنیت را برای آن‌ها به ارمغان نخواهد آورد، درست همان‌طور که سال‌ها بهره‌کشی یک‌جانبه آمریکا امنیت را برای آن‌ها به ارمغان نیاورد. وضعیت را اصلاح کنید تا مجبور به التماس برای دریافت حمایت از دیگران نشوید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140400" target="_blank">📅 16:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قشقاوی، سخنگوی کمیسیون امنیت مجلس: چارچوب کلی تفاهم جمهوری اسلامی با عمان درباره تنگه هرمز مورد توافق قرار گرفته.بعد از اعلام نظر نهایی در سطوح بالاتر، بیانیه مشترک و جزئیات این تفاهم منتشر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140399" target="_blank">📅 16:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رویترز: بسیاری از شرکت‌های پالایشی چینی و هندی این هفته در پی رزرو نفتکش برای ورود به تنگه هرمز و بارگیری نفت خام در پایانه نفتی بصره در عراق بوده‌اند که ناشی از تخفیف‌های کلان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140398" target="_blank">📅 16:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=HZKodasV3BreM7ok_HvzDtStJY9SmB2ut56r21hIGm4p2jCNs81uDyr6IO8TOmo8gbUGAotl7sIrFBIbqWD5G0vw4W5StIFnpq5ED1G4Jq4g7VW1tHMc0J2R3-PlkDlf2JK1gNvnL045By5wS67zQvHzXhtQxjRGrYr2WriH3M5MXxF5qivhByi6ab3-4EgAaUZ6zTbXXQFiH-nTXRXvIDb6w5L0X0kpsauP4z6rrKfrCPa7jpShqKbTn_IM5QF7I9ietNYfC6lLN0VzHTaPfdrPDbl6BextAgSZWUiaSePSSgqK4cuDBu5WoHoO5aRZ8OMZYBt_iE4OPrhrAN-SiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=HZKodasV3BreM7ok_HvzDtStJY9SmB2ut56r21hIGm4p2jCNs81uDyr6IO8TOmo8gbUGAotl7sIrFBIbqWD5G0vw4W5StIFnpq5ED1G4Jq4g7VW1tHMc0J2R3-PlkDlf2JK1gNvnL045By5wS67zQvHzXhtQxjRGrYr2WriH3M5MXxF5qivhByi6ab3-4EgAaUZ6zTbXXQFiH-nTXRXvIDb6w5L0X0kpsauP4z6rrKfrCPa7jpShqKbTn_IM5QF7I9ietNYfC6lLN0VzHTaPfdrPDbl6BextAgSZWUiaSePSSgqK4cuDBu5WoHoO5aRZ8OMZYBt_iE4OPrhrAN-SiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحلیل جدید محمد باقر خرازی از حمله مسلمانان به هند و چین در آینده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140397" target="_blank">📅 15:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a993f21cea.mp4?token=uy2AvEHEF4EuQGxXghL6RbnZjklX8o-T27B11kYFCXPW5V0KFbZw0HYohr3mbxZ9LUVV8OslYOqZJibVS1Z1rzk-y1iphkY_KMCu5__K57e1OrF6-0cIzYuR19k0FjLbRk-37o3uAAjEwBse84k8VZqewmQJmrruIjaMdWbFMGMRlMi4krF3pXE48y1hOLMDKDglGOxb96tUywlg-ryU5Jj3JPREO8zl827FO43LlSFO6eJC_7n2oV6iQpyezbSc0zIJ88VTo4Or9rd78zDi2xLLAVaUxVZYLJBq5_1vGLfiCU7-tNLLK8cXUGjo9GZg7QJcGLDxpsIDJiZB_G5JwzKgvvXPOyyWSpPqf04NGnMylLlZ3vx2Y-ZeO3UJrg7ENQKMsbRkqqBWCZ4yQuIYZZVbhpOKuD-RwC-e5ZX0lD1ATmbF3FtUoEYoxEzvqmITt67oO8hJEeSLAoQX1LhWGbRR9MAFeqZeTasHrE5KGWtz2RQ4rgzdw5l6cySbhyE3QeDTNTovneeVV7Pk1bbBtvrGyeVIsS50s5JVwpEeiro4MTV9TWvSEic3IiZxPyBkBeNJQn0rTuN4BMWZ21A0U1__328ePyZAG08Twx5rNlzpzof6pjpaqGlhBFs6rHiH_SJHaxjVU2Or8HN3el0LZ7a8UoIYihbtpGvvnPz-E58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a993f21cea.mp4?token=uy2AvEHEF4EuQGxXghL6RbnZjklX8o-T27B11kYFCXPW5V0KFbZw0HYohr3mbxZ9LUVV8OslYOqZJibVS1Z1rzk-y1iphkY_KMCu5__K57e1OrF6-0cIzYuR19k0FjLbRk-37o3uAAjEwBse84k8VZqewmQJmrruIjaMdWbFMGMRlMi4krF3pXE48y1hOLMDKDglGOxb96tUywlg-ryU5Jj3JPREO8zl827FO43LlSFO6eJC_7n2oV6iQpyezbSc0zIJ88VTo4Or9rd78zDi2xLLAVaUxVZYLJBq5_1vGLfiCU7-tNLLK8cXUGjo9GZg7QJcGLDxpsIDJiZB_G5JwzKgvvXPOyyWSpPqf04NGnMylLlZ3vx2Y-ZeO3UJrg7ENQKMsbRkqqBWCZ4yQuIYZZVbhpOKuD-RwC-e5ZX0lD1ATmbF3FtUoEYoxEzvqmITt67oO8hJEeSLAoQX1LhWGbRR9MAFeqZeTasHrE5KGWtz2RQ4rgzdw5l6cySbhyE3QeDTNTovneeVV7Pk1bbBtvrGyeVIsS50s5JVwpEeiro4MTV9TWvSEic3IiZxPyBkBeNJQn0rTuN4BMWZ21A0U1__328ePyZAG08Twx5rNlzpzof6pjpaqGlhBFs6rHiH_SJHaxjVU2Or8HN3el0LZ7a8UoIYihbtpGvvnPz-E58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فعلی مملکت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140396" target="_blank">📅 15:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=ecwfxmWrluGOQeXLQqFMrMj1RamiRUrjwLA1u7XFSD9F0Ql3u5JTfqGHWzyYuiT1LXB6Yrh9tKPlgJqXaDCodGHxCV9pQyiwx0b9I7qiSMaET4tiYlTPzHeDR8AsYE33JUtG37FZsUpllyXhW4ezWkaOxYEHzSw-ATweMUHfFjcXNnzE7XHdeEFTQn5kMTsrhirol2BsCMQy8nYFheYXsQ9CLrL8dledjjKNiPN3N7PKsEa05eM_meEWrfNpPo88WVwVLk8xuCmjuFtxvye3W7IUhgdqpbIimAjrcyl3PLMi0ifvkMR9Htdffeo2lzS5h08ChMud2q1iBOyI4_0E2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=ecwfxmWrluGOQeXLQqFMrMj1RamiRUrjwLA1u7XFSD9F0Ql3u5JTfqGHWzyYuiT1LXB6Yrh9tKPlgJqXaDCodGHxCV9pQyiwx0b9I7qiSMaET4tiYlTPzHeDR8AsYE33JUtG37FZsUpllyXhW4ezWkaOxYEHzSw-ATweMUHfFjcXNnzE7XHdeEFTQn5kMTsrhirol2BsCMQy8nYFheYXsQ9CLrL8dledjjKNiPN3N7PKsEa05eM_meEWrfNpPo88WVwVLk8xuCmjuFtxvye3W7IUhgdqpbIimAjrcyl3PLMi0ifvkMR9Htdffeo2lzS5h08ChMud2q1iBOyI4_0E2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهم حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140395" target="_blank">📅 15:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbEgKr5SKzhrzIs1BRzUOCORbPLSD9U3ip6Gbbt9TJj95QNSxe45acSOVWTN0ckHbHCsej9a6v2J-8--hhUXCpMLA-gvLSyNYwIDNGFYWOIeZJkSzEIUMzqyCfY8FxGpyD1K7qAI4FJouEevxGowvvyhHMsAMnbwfn9a9HkS3FmQI4skOShKoVA-CuCrY-pSGZEoxq5cg69H3p2IPyVmuQX4Y4Y8qaMYleQL6EmeU90RCmIpUfgtWaqwgY7Ke0sGdOf7gXNcDnQLy52jKnV2vJ5z2-Pt6Jfg-3NUYWs4fZ-17X_h8GoqXbhPtXDsVw5UlcMW2TfZdeA0hRpbeyR-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال گزارش می‌دهد که رئیس جمهور ترامپ دستور تحقیقات جدید در مورد نشت اطلاعات مربوط به ذخایر مهمات فرسوده ایالات متحده را داده است، زیرا در خفا معتقد است که این گزارش‌ها «رژیم ایران را جسورتر می‌کند» و اهرم واشنگتن را در مذاکرات بر سر برنامه هسته‌ای تهران تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140394" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140393">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DruvME6VpRpd2nkALgJCFvvZMqYwsIXK-uPj5UQK8I6XlsDDj2-l2QSOIlXnG5j0ry1Ua4GKjb-Zg8eqbq7vFz5vVtsZ16L4bzGgblD3ipQHMN2-tR-Z4WjRevbunv5hCMfgrgypFLo9pW2_S86-EcB9Km0RrYyfSare14Bo9VtdSBkIQEIZooxXt3wOGxRfrKqNhJ4IuNSA0tjCE_RBkgjp8Iw5gvUdnnJoVXCj1eWtDAEMCcO-DX9Z8ByNA-Qm3t52Suxc8RFBM9dXtQ3jDqcPmD0T3LmdTAefg5G4tqEJzng2BhskgwaQPoXHciO0dmAorGlTNfRklFvo93ZsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: باید انقدر بجنگیم تا پیروز بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140393" target="_blank">📅 15:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im5l6ZLVpMZRKZ3Hu_tjrBsT1aXtLcZm1kVRbhnLuKrZA1aEBrzxZ74vmv548VJ1oJ81oPFtvqLPIVrl4TascbGf9k1xYfnbmxFQxsl8xiyHXHyMKSR2TJQv4fHb-RGrj2tInhpZAL8gBKAtQJR9_lcEBVAAlR1VBw7Y_sk4F6NAQRT0Eolmit3cXgY2xX5iHtCik1B8C7QC6QnS5sLwfYz3bY6GGD5YIjuhWGFcr6lnsMHRRYdpwaFTIJSwL21gEnJp6sQg645a1WbvztAwgWX8y73LspNtwTwp_mC1n5o4JsZ3GZjGqofbRVDNpCrYH0ZljVmGb53ntwhW41Zrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لائینی امام ساری:
مذاکره درباره تنگه هرمز اصلا تو این شرایط مصلحت نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140392" target="_blank">📅 15:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbRnH7aeqpPVTJq9gjpTQd_l3RjN5RCZTHa_ll6rQa89vpKttJpzONTkGX_1-0IUBThmQSxTuNXiNFSAShYoetkgIdaiapW2dcwOgXR49P8g_n3Dc7Y0ENZcQyB7raCPQYMo-hSSFh2vQh7K6JTXm62SfgRUrAvVuU2TJ6zcR1OGOnLuAD4fW5rS8HkfyuYgrV6iGN4RwbJ2TirH-HXc6aGt5gYd6sIhoQI8ZaG4inzFrNO7bqhptYm5ZaoO09zENbliI-_rbSjgp0jjzyoTZNi2SKEPUEc_BPWPmElfolvb0bRDQ0eTe7AB_yH7nMvge706o53C3veoe78iRyoosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140391" target="_blank">📅 15:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی:
به نظر می‌رسد توافق ترامپ در وضعیت وخیمی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140390" target="_blank">📅 15:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140386">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6iRhbTxzpyhpMWQyPiop9VqmNZR5hdNfMw6jnezanXi4k3U4QRBhWjabDa2yiEAncqBukItsh8oI7ddpiHzRChtK6KT4jGFnOxd8Vgn8snYEVMyJriUQ1sVlUM4QsEW2KPHqiKtQeB14wUpMtn-0H7yyo11DfIksqX4Qy7kHJ5lmTHIWJVFh4vopg87VqwY1Zed7R5MczP9lj9XGxKVbjDdwX5zy-yye2hJBm2lALYG3nVtkQlnxur-lTGGWEUH8gV1eUKKOlJIUGg_g2ZnAcD8RbHB1uQKHBRYgcrucyscG5Am8txJnYJ5-L21247YNLO1aHWw1tzJNu_U_sIddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt0sXRaEBXNUpacW4v31R4gC_1O1ApZYEk9GvSmy7yS44r0K4BRjOsP2CCys10Yb-n6-Jnypg8xplTGE1aoEbQ-VgnHYzoTJP4snq5gxWNIprdJ3O-q6SheqleUEl2_X1Fi7l5lytOc8SL0tMq3fJgs6AeOFqCL8XBoytRTKZ6O6divZkO5BO-u-1BeiFln-SBPIawVvHDMNa6NZje3G9WFOBZUl6gDEylDoy5Z6lXx2CRUVecryXk7PKjdUoZZduZlimrlnkJY6-KCWYeks_VRyJklF019pgnl9lvV2tgTTZ0KVsgo4uOYAah3x3dl7bK0Fz5nR51qBN-rFujBAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSHxCJvmCaHNlCmHqrvW9O9h6LNhucpJp_3E4JX38fveu4dA7gvhRv7CiaiFjSIZKsflaRrcRMvnxSwafgnXgAYJgZCMNOmm521UVcISVBfLmoRlzUqZPJEMxSSHgrIuP8btMqYLXcq3N1EhPvGzuzo4Upbz_jIEDx4Sao6Ktb9-GX_C9RUmfhNpLZ7xSs3XwYMsSYMziwiJiJRcXirSf_pdIF8i9DJCO9HQmiX5FUnT8oWTsVwQ_BcDuPt1hs4odbb2bD7KNuV1HmJ6w5Xbp4GZ-n5rxD801IBeMIJLFTLuwbH8Pv5iT9KYe82QT2K7ph2cwLTO1q7JR5LmUwU95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYFTSMY9l-l2Qxq-VfOS_Ue3cynfbNe7fcpF1FkscHyf921-8OiPkzut2c6cgStA3KUZeWR9zyM_8ORB4FONMUuO9F3MOv-S7tHbG2b2Af5vWpC2xyGZzcRq4HL7K_RK0GomJDn0rrv7ppZO8cK4WOMuQqlxHcY0TeOZoZuWRdj1XY94gvjKVYM9ThSqOfHG6ujQROUa8RKSKslfq5s4xEHCtzCfkjhGmtWAIUC8QWnDizYpWc4tcrETUoUI3B8tobgYklD7SFxjUpseJ6B6-dsusqE_jkMsI33wMa0tEmWuEdXiOku_ccb7qjDIleMMlNn4eXBnwAf986QBzFU5yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از انعقاد تفاهم نامه مکه در مرکز جهان اسلام
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140386" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBiFYavPnGYC71iv2GgaGJwPfwzNJ_9BO7If1Cd3a4wEiFU5OhcplwVWrUoL6Eq8X-Dq0LIbcZd5sIt1uUDSSpstuQdDQ8bjAZ5wIx6yZQ32qfPvJpjuRXwH_wl5EWkEim6EqBp2N3wnMB18_cHXRDo_3OZ1vOWqAAM-98kVGXRbhJq_c-dNYOi_rUTQaFEbXDQqAlMgrKytxSN6Eyu9PETGUjEKBjj174doZMPDdazwhni2RbN7EAPJUlQ4VRJJPJDwiKehk8s14VwTpdfEgO5zFOqTJHfhA11IPlRXb0vxMhGVT6bjZcwOBjjKBj8ZVc47OEAvVU-ZBgl5S29Aww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری i24 اسرائیل به نقل از دو مقام آگاه در دولت پزشکیان ادعا کرد حال مجتبی خامنه‌ای وخیم است و احتمال درگذشتش وجود دارد. گفته می‌شود به دلیل وخامت حال، کسی از کابینه با او دیدار نکرده و این خبر در سطوح بالا پخش شده؛ برخی مقامات ارشد معتقدند به زودی خبر درگذشت او منتشر می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/140385" target="_blank">📅 14:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOJalX1b7ehNLMOOaZCt6MitUxw19YNO8yDUNiPg6GO2jWJ6OITwFoAi0ZGGI5LPeHt4J8i80iRjS_f41sjqX2p6ZCC_z6Jkbc4qBiEOmstk2I6CcpEurR8f3DKKkPVmpILYGqKLlHwy6afB4oR67a6CzUoxou-dax5sCLdpoCmFAK1OPd_CloX_QGk-TKbF-gb1kM7F7jdVtWQQmbZ-o6A8ZTb9nRBVLeKV2Jo23ItGJ8DCkPeHMkKOls4B5jU5e2ZHLDPadXFsAEl8u9KAUS7iCw8hhPl5EIssg1OIIR5HscLO5Xr941J-wGtpenqQYrVaVasoERTiQJaKsIo9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdNQYUPQSR6EA86M1IBtEWxVhk2oeuw5bYHE57ffkRvWaKQaJ6KLmqDXE9qqpjITN7lqb0KP5WlXg742OW2OUF017E1t0rSPBVhK1itCZ094nKFDGBMNnZoydccQm5od9z7xeGa_v5mkl7_V9qRuN7oCaT0K_Q8U8Ih2z3yRIt49zT2AC18kNaOOPKcWXrc0beLlTSSeDOGs5NgU07g8O3XyEBLoNbhHoAlOuy5KWcgBSPw-ZyaxZK6Dmt2_qmRLkmdo1Cb1S0Av2QiU2o6DRgi1FfUBM-qjAgmHhpJ2PkBL6aM3F-mcvyOsXyMvhnDhEUb-vxNCDLvmnjWflmdiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnPUBr3BH94_F-3kIQQCRqm9XTjfT351vFO9hgYYEXM0gyXAdgrp4a4vwKI4PMbFVKtkkxUFtvSZFnqHayFVPI50bLT0JQmAtPyND_znW41oy2hIKT3UERWpCre6IXUlXQGzNtHfylsOkI6-eF5sOktHILwhtIGrg4TmJc3FvL_-O4sjmp42UUDKSpX4Dmgm3dj9iIi0JSZ--QwZTkeXg5EQKIVPS8QmA5f449KIPSoYCyBD-goc_Z1fQzlXbTb1rv5iNwrZpIHqRuO_PufdQ-xUUZCX3kjBirRbCY4JkPDqTJv8f9wcuyxWy5xO2F64zYzXuG9E9bTJ_hLhQTzsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از قطعات پهپادها و جنگنده آمریکایی و اسرائیلی که توسط سپاه به نمایش گذاشته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/140382" target="_blank">📅 14:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ سوییس رو تهدید کرد:
ترامپ در تازه ترین مصاحبه خود گفت آمریکا حدود ۳۹ میلیارد دلار کسری تجاری با سوئیس دارد و تأکید کرد: «می‌توانم با یک امضا این کسری را از بین ببرم و آن‌ها دیگر یک کشور ممتاز نخواهند بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140381" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
«توافقنامه دفاعی مکه» رسما امضا شد
🔴
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.
🔴
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔴
هدف این توافقنامه، تقویت بازدارندگی…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/140380" target="_blank">📅 14:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140379">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
«توافقنامه دفاعی مکه» رسما امضا شد
🔴
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.
🔴
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔴
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام تجاوزکارانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140379" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140378">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6SZP0b4DtJCK4wJeF3UpOJ4KhCL9BXe8Xgw36VwJT-_obJDQ2bgyynFfL6dS1JGFrCdGaivSWlyZsNcMJCYXVUW0c4aZjmYbKNbjY-x6CKgMUDZTKI1OhFYPHr-QvtzjpaTjSkyMPhNSSHgPTAJsIL__wWzKfrXNg2Y9KFxyHnbNjo0JjZ0I4s1OXIUhgmOqzJZSld3nn7SsSFH3r9Qjeky5I-PKRLOGuQ0HuIhASuDn5tut2J6cYup_wE_mKcP4jFpNvt0blaj2PIV0qNNY2uDFLTF1fk2xQe1zuCnWbL2-LDUWBxd9DExJ19hQJ3Su0X-_Pkv5Z_eBuw4xtqukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عبری:
محسن رضایی جزو اهداف ترور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140378" target="_blank">📅 14:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت دفاع روسیه از کنترل بر شهرک آنیشچینی در استان خارکیف خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/140377" target="_blank">📅 14:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
الجزیره: آمریکا ذخایر موشک‌های رهگیر خود را تا حد زیادی مصرف کرده؛ در صورت ادامه جنگ این روند ادامه خواهد یافت
🔴
به دلیل این کمبود فعالیت نیرو‌های نظامی آمریکا در منطقه خطرناک‌تر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140376" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140374">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3iEDdBRrzFAwkwbIkESuxDi7VODePboawwoXKqCVfIU_2y6mGG6VodJeOyZPjvb4l5EkgdBm9Hc8BUmixpQZvvoKFcKD6zeIxdh-mX199laPMZwZqbCCsYZyZY3DsySl4QPAdQ7PRorWyN4aHw1zjKNI0zvMNRzsVa1Nyo2gf0N3j0iSIcKowhxbmNbfGZkdLbynjAuRcmFoXIwglmoiYmVPTsifB21Rq-zEveJHms3P-w-iOZufc4lsW_rWOWVW1bxkd63M6mrR1ZtgrRn37bn5Mj_qPSpD_4ZK-w28g_E5yQJ5hGyr0Jt_m_zvpl_bf3Kd_MATuGQoUmI7rqyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWIhBOXjtleg0nGWgyWVf6JsjrnP4M89bjRj3XxGXmNaPCNTAwqL7zlLBsAH5Y-MPAe4mt5dl6ksvhM8dVn4OOoyEY1fpbPt0lakkacr6ZoSS-rtVZrlD_ISANuKEizHMr4XXZWatSBWxVxWBQgkWRnutLIurFd-kM-ih5IGAuMNOLbOObSiC5fHtCNskPWVCR8KKtieeDUx6w7kplS_TBB6f-_Oed887OqvqHmcDo9ve7P-LWojUp_aetNr2fA4iWcFpXY2olSwsQzyhQY-sHOIcgAnHEu7Tdh4c1pfdYiRqnt0Hyw7U6dLWX7zVIAOr-iyWUFu44GB4-7gfmhrPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سپاه تصاویری از مهندم کردن پهپاد MQ
-9
آمریکایی در طول جنگ منتشر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/140374" target="_blank">📅 13:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140373">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رئیس سیاست خارجی اتحادیه اروپا:
اتحادیه اروپا امروز (جمعه) فهرست تحریم‌های جدیدی را علیه پنج فرد مرتبط با مجتمع نظامی-صنعتی روسیه تصویب کرد
🔴
هر حمله جدید علیه اوکراین دلیلی دیگر برای اروپاست تا تحریم‌های خود را علیه روسیه شدیدتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140373" target="_blank">📅 13:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140372">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها می‌خواهند به توافقی برسند. ببینید، واضح است که آنها نمی‌خواهند مورد حمله قرار گیرند.
🔴
آنها می‌خواهند به توافقی برسند. پس، باید ببینیم چه می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140372" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140371">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfadad379f.mp4?token=SxicbsgUYxHlZce5-eigZN5Q1q9jXs-Cfdeu_De_7p0HBIyZz2MGZkVKPAQ7k9x9SFpdkwT6X-tiXLcZqbNH5920guRCysfCXfRRgj-TLaRdkvwB548gdCNKMHD1ZAUAOk1Ob8Lkue6-wzNeqJucWJvWs-jACx8ylAUric4VSMu3mFe8S3S2ssC1b00pJjnkSk3X8-1bWaBX23CYIhgHeZe8p3emHY4UiOvtx0Wre3gqyqvLYQbBpe6P9q2-HWlHoW9Al_-HgidsizboABkZNT4UB4TmTNMpSHik4ynpYGLz7PN0M8NOUY-htb2T-dU0TODvrbUjk8DznW8Yptv6OZaJrjgH2yPrqmc_9isQhD1LHmB6LqkP4FlwUAXfYlVynJccSAv94Dr_HxlT0zdKHG5E8YIW3iRaxzYMVyg5aXNzaCQz-Gi6pUDf4UE3hcHZBurjBhg8GDBq-opX-wwSJaUfGYYJu5dglag_GpBP6PucUVUS50akdFOphueAN4vYceCFm_1FkCn0pjp2TxysLavYE-oCTw7oPGEVyMMZ5i7JmcGsOTKZaRmIc7RJnidTeTWo_6t5QNPviv9qznYCDZz4aDpEuCPAFki64zPJQQZ6SszEl65UBNFIb2MsBZLpKNDLWgJ2bN9eRdu5JtHkS5OUMh3Q6P4zpun8ActamIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfadad379f.mp4?token=SxicbsgUYxHlZce5-eigZN5Q1q9jXs-Cfdeu_De_7p0HBIyZz2MGZkVKPAQ7k9x9SFpdkwT6X-tiXLcZqbNH5920guRCysfCXfRRgj-TLaRdkvwB548gdCNKMHD1ZAUAOk1Ob8Lkue6-wzNeqJucWJvWs-jACx8ylAUric4VSMu3mFe8S3S2ssC1b00pJjnkSk3X8-1bWaBX23CYIhgHeZe8p3emHY4UiOvtx0Wre3gqyqvLYQbBpe6P9q2-HWlHoW9Al_-HgidsizboABkZNT4UB4TmTNMpSHik4ynpYGLz7PN0M8NOUY-htb2T-dU0TODvrbUjk8DznW8Yptv6OZaJrjgH2yPrqmc_9isQhD1LHmB6LqkP4FlwUAXfYlVynJccSAv94Dr_HxlT0zdKHG5E8YIW3iRaxzYMVyg5aXNzaCQz-Gi6pUDf4UE3hcHZBurjBhg8GDBq-opX-wwSJaUfGYYJu5dglag_GpBP6PucUVUS50akdFOphueAN4vYceCFm_1FkCn0pjp2TxysLavYE-oCTw7oPGEVyMMZ5i7JmcGsOTKZaRmIc7RJnidTeTWo_6t5QNPviv9qznYCDZz4aDpEuCPAFki64zPJQQZ6SszEl65UBNFIb2MsBZLpKNDLWgJ2bN9eRdu5JtHkS5OUMh3Q6P4zpun8ActamIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر دموکرات‌ها به قدرت برسند، ممکن است من آخرین رئیس‌جمهور جمهوری‌خواه باشم.
🔴
اگر سنا عاقلانه عمل نکند، ممکن است من آخرین رئیس‌جمهور جمهوری‌خواه باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140371" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK-X8kh_9tFXONZXwCKQ3ROHOLD6BeZLITul6kRbJe06zXM7qrjxU9zAozES2QHZ0-yfUB55heJ6DbOACnqnB9hBi8kEiu_kiM50O7AJzI-W5wJgqIeI3gBCHvpyBZral6ch6Z_whFpc_JfHroOZ-pnyZLEbMeDOBF0KustiAc3GfZpQUJHCvMOofXxj6RHGBE-vriYUsDySd_lpRHnhpofbj1UNAUxZIVSYoIg_cv6gzEokPFQ4VteOK2aCJM1I0vskMSGHvrX8ZUueyab_NmQ5v6sZ9PzTB8SPSFOvlAsgYtOifKlXw2cvAPYJoPlh61OzOM1WSP9dVOdkvEL5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
رئیس‌جمهور چین، «شی جین‌پینگ»، احتمالاً طی چند هفته آینده به آمریکا سفر می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140370" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140369">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b39fb9f9d.mp4?token=aBRpYJ3a61YFZ74k1m31VxSa9_2Xik9HFvAteskiRRe_U-M4jDRUGro4ti-fVJBbWudmh4_lqEsp3tDrp_USKJhmZbLvcf1wW5bgwiKyt9-asKexMvFeiEap26iT9XVQF6oOHPv9xx61OipxZTvupcew3aSgm5cBe8O5WFU4vK1P8WihQ13d_Grsa6BRgJdjhNU1ikTfwT30v96hE6w86h_zuAKByV96m13q2FF7Zw72Pw2V5UdOxKAM-EVcRXafOA_eLP2UkNocsgg1hY5Fhpa-n3PLHhMaQI-YSrXun7HbfcKhR-R1lqtgZkPO-U5K2cbkMSM3raQr4JMF2ekWmwGyYKsIgvezY0cEPmWeWjzrT2zEEN2M6nALdcsyvyosyH7l4F3K68hUvxmY_2r57xnaS-p3RvCeZcq3y6AVqWAD2Clg6HDcAxKOYxYoHUW85ZxfdqMnQ4QJV9ZW8CNBktT7OedDqD99994PnSKFIR4jFufoBt1t5ARmqXtZiUTyvptAsDs_kgP-9YW_hzkI__TzE3BEnnLDTiIl8Gy-B57xpjJA8t__UUEmfH69e-QSrpvCg4kGL_72FTty5r9CgrsY7IKtuIlfl5O1LbFriHhE8Zqpam98XE42qITIX5uRvcC-9HpDcaDsAs61kVMRCUxSERSUjjgl58v6dv5LGsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b39fb9f9d.mp4?token=aBRpYJ3a61YFZ74k1m31VxSa9_2Xik9HFvAteskiRRe_U-M4jDRUGro4ti-fVJBbWudmh4_lqEsp3tDrp_USKJhmZbLvcf1wW5bgwiKyt9-asKexMvFeiEap26iT9XVQF6oOHPv9xx61OipxZTvupcew3aSgm5cBe8O5WFU4vK1P8WihQ13d_Grsa6BRgJdjhNU1ikTfwT30v96hE6w86h_zuAKByV96m13q2FF7Zw72Pw2V5UdOxKAM-EVcRXafOA_eLP2UkNocsgg1hY5Fhpa-n3PLHhMaQI-YSrXun7HbfcKhR-R1lqtgZkPO-U5K2cbkMSM3raQr4JMF2ekWmwGyYKsIgvezY0cEPmWeWjzrT2zEEN2M6nALdcsyvyosyH7l4F3K68hUvxmY_2r57xnaS-p3RvCeZcq3y6AVqWAD2Clg6HDcAxKOYxYoHUW85ZxfdqMnQ4QJV9ZW8CNBktT7OedDqD99994PnSKFIR4jFufoBt1t5ARmqXtZiUTyvptAsDs_kgP-9YW_hzkI__TzE3BEnnLDTiIl8Gy-B57xpjJA8t__UUEmfH69e-QSrpvCg4kGL_72FTty5r9CgrsY7IKtuIlfl5O1LbFriHhE8Zqpam98XE42qITIX5uRvcC-9HpDcaDsAs61kVMRCUxSERSUjjgl58v6dv5LGsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نمی‌خواهیم چین در هوش مصنوعی و رمزارزها پیشتاز شود
🔴
دونالد ترامپ گفت: آمریکا نباید اجازه دهد چین در حوزه‌های رمزارز و هوش مصنوعی برتری پیدا کند، زیرا این دو حوزه را برای آینده اقتصادی و فناوری بسیار مهم می‌داند.
🔴
او با اشاره به رشد استفاده از بیت‌کوین گفت: پرداخت‌های رمزارزی در حال گسترش است و به اعتقاد او می‌تواند فشار بر دلار آمریکا را کاهش دهد.
🔴
ترامپ افزود: اگر چین کنترل بازار رمزارزها یا توسعه هوش مصنوعی را در دست بگیرد، این موضوع برای آمریکا یک چالش بزرگ خواهد بود.
🔴
او تأکید کرد: آمریکا در رقابت هوش مصنوعی با چین پیشتاز است و گفت: هیچ‌کس فکر نمی‌کرد این اتفاق ممکن باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140369" target="_blank">📅 13:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140368">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a754dc045e.mp4?token=cbjKIsYN9rTxRHeTSUhBFMBkBIw0vSthla7HshuogTOnYgjSMuxYWakDgMAOCA3fpFSZccHvksL2We-F029yt-ww6pL9yIJSwrPsJZ5F3SDeTyM838lkmSm36syM33_UkZB40Ef1bJ53wHFb7XoiIMIuJlxty1aE8C9inoUhsdTwhgneKZQrydu1RjJxPoNw9Mg-etxTs62sjpGGPtqck-8WX8-hTDYxQpH1ddUIvYo5847kzGdBLj4UpKuog_Ydw7sqK2xxdbtMhsWYdPTJO60E9NAYXbyZfm2EUW7Nllx1vGqD2ouWstUooXr1xjsCEgljxCfFKihlK4MHEHIenzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a754dc045e.mp4?token=cbjKIsYN9rTxRHeTSUhBFMBkBIw0vSthla7HshuogTOnYgjSMuxYWakDgMAOCA3fpFSZccHvksL2We-F029yt-ww6pL9yIJSwrPsJZ5F3SDeTyM838lkmSm36syM33_UkZB40Ef1bJ53wHFb7XoiIMIuJlxty1aE8C9inoUhsdTwhgneKZQrydu1RjJxPoNw9Mg-etxTs62sjpGGPtqck-8WX8-hTDYxQpH1ddUIvYo5847kzGdBLj4UpKuog_Ydw7sqK2xxdbtMhsWYdPTJO60E9NAYXbyZfm2EUW7Nllx1vGqD2ouWstUooXr1xjsCEgljxCfFKihlK4MHEHIenzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر نامزد نشوم، نمی‌دانم طرفدارانم باز هم رأی می‌دهند یا نه
🔴
دونالد ترامپ گفت: مطمئن نیست اگر او در انتخابات حضور نداشته باشد، هوادارانش همچنان برای رأی دادن پای صندوق‌ها حاضر شوند.
🔴
او افزود: بسیاری از این افراد از حزب جمهوری‌خواه ناراضی و عصبانی هستند، اما این نارضایتی را متوجه شخص او نمی‌دانند.
🔴
ترامپ گفت: آن‌ها از جمهوری‌ خواهان ناراحت هستند، اما از من ناراحت نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140368" target="_blank">📅 13:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140367">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یدیعوت أحرونوت به نقل از یک منبع امنیتی ارشد:ایران، حزب الله را مجبور به پیوستن به جنگ در ماه مارس گذشته نکرد، زیرا شرایط پیچیده حزب الله را درک می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140367" target="_blank">📅 13:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140366">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8-Srl-BEAocxUWIaY54SlpVOEXDphO1G-QqAtEmFvaAOoc2fyrSEg3avJ-9DuP7MBw2BonHzLB99uccsu6DynIIGdwvOKRXjlmnokuJREOljL2eW9W7NCgqXdwar13icV-9YBqa74lS35uiQnsTJ-IoLXEwegRUxf3EySisSa8evLKLj1sA4fgyxKmi04pgHQmC0c-Y2XgOsHoYjYTwThenJ6uIueiGfROGjrw_tkOIdAmbdNN4RI0JeaTDnggHPlHYpe9EayocnIKngpZBOjzAzPguRD4L6Jk3d1mDseBzg7ZXyCvwXqjCFToR7WLeeBWNe9TsClPg1OLM_euTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خرازی مدتها پیش بر ضعف فنی قلعه‌نویی پی برده بود و اطرافیان او را با صراحت نقد کرده بود و خواهان جایگزینی گواردیولا با قلعه‌نویی شده بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140366" target="_blank">📅 13:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140365">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dc16a409.mp4?token=Ypy-NKyH-5f_tNyBMp4-910ErVewHAGiRYDlPNhWaRiDFsyomCzjiPzrJmEaCCNAmZascn7--vUUFfmrnGvnwBfVQUb-yl_viddp3NS3d5sTs9X-Bu5xgrK88XbZUH2LVsRcvz3LKYZBnSllUHWofakT-TCbS6tWk6vsZYD8_xhyjOej-4qe9N-dThvTdh79YbKbWWc6F_SL7a4i1eaf01iivZ9zAYmTcgZLZEAdmtQsCSZw2ASORJG8DD90WMGvMBAPsNWyijwQVMhEYE5alNNw4FhM5--FhcExuW9qI7Dnn4DMS7LWnNgjz7zeKpkqaX9SAkR5JYqFhPptg0OvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dc16a409.mp4?token=Ypy-NKyH-5f_tNyBMp4-910ErVewHAGiRYDlPNhWaRiDFsyomCzjiPzrJmEaCCNAmZascn7--vUUFfmrnGvnwBfVQUb-yl_viddp3NS3d5sTs9X-Bu5xgrK88XbZUH2LVsRcvz3LKYZBnSllUHWofakT-TCbS6tWk6vsZYD8_xhyjOej-4qe9N-dThvTdh79YbKbWWc6F_SL7a4i1eaf01iivZ9zAYmTcgZLZEAdmtQsCSZw2ASORJG8DD90WMGvMBAPsNWyijwQVMhEYE5alNNw4FhM5--FhcExuW9qI7Dnn4DMS7LWnNgjz7zeKpkqaX9SAkR5JYqFhPptg0OvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان یک خودروی بمب‌گذاری انتحاری (VBIED) را که توسط ارتش آزادی بلوچستان استفاده می‌شد، در شهر نوشکی، در منطقه بلوچستان پاکستان، منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140365" target="_blank">📅 13:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140364">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo-ZQpGoNQJgP4MJBHPLlzdtMrCIhUijecwZawrghNcEb8FYhiYNCmHlvAvrdVOvJrsBex4SF70mBo7GVBNu5YmxV7110YEA2s-mogqgw5kSu9JQp5gbLPUekaxful_f6mXoVhix_wbb2XBT4FqOt15jPCD1BYt3Rpb7hDRceJuTyCME-jaxwm3K_5FLL3EP7jE8JoSFrfZmDaN1Xiqb91Nb8d1l_oHj7UIDPBgeVOnOSDsNarE_JNOMY38AnQKrFe7MRRNCCHm7zsezRF_QnTpCs4BQ6C8KlFHm17snnu3z6VxwfmdLCnDbKmS7l4-En1AlgrAIOXyfbbg_4c-dkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطابق گزارش (CBO)، هزینه کل برنامه تجهیز مجدد ناوگان نیروی دریایی ایالات متحده با زیردریایی‌های هسته‌ای، حدود 275 میلیارد دلار برآورد می‌شود. هزینه ساخت اولین زیردریایی از سری کلاس "ترامپ" (Trump Class BBG(X))، حدود 23.4 میلیارد دلار پیش‌بینی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140364" target="_blank">📅 13:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140363">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وال‌استریت ژورنال: کاخ سفید هرگونه کمبود ذخایر موشکی رو رد کرده و به شدت دنبال نفوذی توی کاخ سفیده تا ببینه دلیل نشت خبر کمبود ذخایر موشکی کار کی بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140363" target="_blank">📅 13:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140362">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35faa8191.mp4?token=HSeNlej1I1v4zReUkYrkBUWLhpODN5yi90VIcVvfg0HRFcCPR1jpDubNqWEwxNUNiPzVyZTijjbf63jBS7gZxq7zIaJmrK0BhgDi-MOhie9xgaTRbDdMbXPDVPiuaOI2iOT3W56DFLK0Fn07pOfg1IDu5DpD6QRYZLSqXXpPps8gXtE_eQ0cl9LaadXlW1B4k2wt7DugQoeVAhjz35mCITaHKuyY5wXTC7P6IwqPaICoahXfmeTIa8sWxqIcGN8PhEk-DXPkSRsIF8aasCyatxkHPPWeA307a1aY006RmJxYk1n4kqQPIsasJ5MWkk1F9m77zRM0oV1HHiHKTpS2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35faa8191.mp4?token=HSeNlej1I1v4zReUkYrkBUWLhpODN5yi90VIcVvfg0HRFcCPR1jpDubNqWEwxNUNiPzVyZTijjbf63jBS7gZxq7zIaJmrK0BhgDi-MOhie9xgaTRbDdMbXPDVPiuaOI2iOT3W56DFLK0Fn07pOfg1IDu5DpD6QRYZLSqXXpPps8gXtE_eQ0cl9LaadXlW1B4k2wt7DugQoeVAhjz35mCITaHKuyY5wXTC7P6IwqPaICoahXfmeTIa8sWxqIcGN8PhEk-DXPkSRsIF8aasCyatxkHPPWeA307a1aY006RmJxYk1n4kqQPIsasJ5MWkk1F9m77zRM0oV1HHiHKTpS2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترکیه، اردوغان وارد عربستان شد
⠀
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140362" target="_blank">📅 13:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140361">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olQqC8iy5Wj4jeGoM_cMO4iLre1o06VpTjnA9qCwHTPGReu0K0PkiEXa2F2DxBLOrRWDr7NqBRj6YUwMqBg8yu_JGnJriFPd7Ut6PNIqSnJE7O6rLdh94McqtocGMAYWH7RUZXkvZNIjFuh5FHaxxsjHozNYCe3XTGZsK7AMSqvtUNiPQq5gz6ECY22n_2LnQFSPYTtgLRKpIe5zngpXOjb_OvCwQCu6tyQhcH9azsL8DGM2YhARukJbgurwVDOvRalj_WHbcIt5k5K-4DEm38TqFLaLrB36yLXCKFosgweRo47AFeZAIuatsFwNBCMMe-wM5rxbUqii4uYdaIWyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی : اتحاد سه کشور منطقه در مقابل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140361" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140360">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Zlimw9aXfZb5JuIv_D0HbUkOQciED7fwzYmt4qqtSz2S-aXikkbPjqpza54ATNowtutLO8p1JfBD1ucGOnZ1ROgs0Nnch6bV_BFhTbkQ-vyip2Sf26YGYCTjl5A1qlxDZU-3m7OwKa50ZDm0x89j1WpoxCLzwbYdcEqoHAKPU39TE1NwmVOc8fEtzM8RKdpAY8A61Co_-A2-1Q5w9vxc9jZ9VB8VqaDVk4PLDLQsCly0Jbvxpf51MqX1SlqLf2TouOxtuVvqPUupprpymxDA2FNQmtxgBAKIJ9vUOq2CDvjXkjs8H81iJUfGzLpe5-iKtSD_Cc4ymZ07d4O7_QPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای شناسایی و نظارتی دریایی مدل P8-A در حال پرواز در نزدیکی سواحل عمان مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140360" target="_blank">📅 12:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140359">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرنگار المیادین: انفجاری بزرگ پایتخت مسکو و حومه‌ی آن را لرزاند.
🔴
صدای انفجار احتمالاً ناشی از عبور هواپیمای نظامی از دیوار صوتی بر فراز مسکو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140359" target="_blank">📅 12:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140358">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فرماندار منطقه «یاروسلاول» روسیه اعلام کرد که پالایشگاه‌‌های این منطقه هدف «بزرگ‌ترین» حمله پهپادی اوکراین از زمان آغاز جنگ قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140358" target="_blank">📅 12:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الجزیره به نقل از مدیر مرکز عربی مطالعات ایران درباره توافق تنگه هرمز: عمان شرط انطباق توافق با حقوق بین‌الملل را مطرح کرد و ایران پذیرفت
🔴
در مقابل، ایران بر ممانعت از عبور شناور‌های نظامی آمریکا از آب‌های سرزمینی خود اصرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140357" target="_blank">📅 12:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شبکه خبری سی‌ان‌ان: توافق میان دو کشور ساحلی به‌تنهایی به معنای بازگشایی این آبراه راهبردی نخواهد بود و تهران تأکید دارد که آمریکا پیش از عبور آزادانه کشتی‌ها باید اقداماتی را که از نگاه ایران ناقض تعهدات پیشین بوده، اصلاح کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140356" target="_blank">📅 12:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: صدای انفجار مهیبی در مسکو و حومه آن شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140355" target="_blank">📅 12:31 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
