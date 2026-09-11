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
<img src="https://cdn4.telesco.pe/file/Tq5y5aPzdfKwpEnCpIFALweWWh3wVIUMFLCn7HcbuOo7Isgo4yiAHWHdMa-U-XC-YlAgR6H4l5WkWF27jotChOOKFcXRyuJO0d824Hh7qpKV1Fl9-6htkl60sbapIy-9niGFk2hem6Q2N9nHUb40uYdid6mIRSCuMZ4LCIJziiwXzjvZ8ThPMsF2RUaGbktI4FLzLdGSvoaZ-0tZhs9w9Gq8Nqk7hjj6wKWvyWsC7_Wt4PJ5Ka7ZbHI4l_BTZgEZf5KexRWGWEZI6YaOCkrYsFjg7vXsvUtSJABT5gQK_OAJOKgQTciRGzSlc2QvZuwWktWsjvjrjGNxR00fUxfuCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/SBoxxx/20815" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS4QtqTEoRaGpofpj4K9YmVypqb9pNo5BOKFryV0yBf7G229z1dae8OadX9D3zPiqHbEHSNYhIxGbf5rVNKoexuRHMoDanopq2CXNOHa6DHfm0eUCyW1y4ijnyepuiEjpFKZEADOVOFvo6guX_QKJm47hSQQ1y_vqErrfBdWFB4Rhh0NbNQfnXP6RVIXkMv9pzRgFrM_xQSW7NjmBNcdJhWQUvmQ4omCl07oeaQEi5t2exyhDTn1hbcI1eStYTSOYR5O0gcwBRkJx5JagHBIkWGBxtIoChlzmJVuw9AVSjZ86hj6lTgU3zGCUsjQY7mnir2doqURat-iRADkWr-Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/20814" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">— ۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران ایران یک موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/20813" target="_blank">📅 20:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Fq210UbvHzgVKAPvuQ8R6Yxqp9Sxz6cbmGFawoVeasqJloTtTD8yHVRaCChX6egwqWsyGc83yr2NUdNm2xH_dFRUF2wmZ66vUW_w1FLecySkYK-KMnQIFUx6T8JnTyrdt4ao5S39tfB1Ac9GdYb6mFEIG0wBKJ18fhm5CljaiZZSz01hF0wc-Avv6wrHfEBcXLZfNOLoT4Lr2aXJv6GUVyq2ElyFsfyehVzxfVWKE0PxaNNoAqWpGKk8EX81-7TmigbOAEkfV_NrcOjHbOSi2ORjdrPeGzs3qkr0PnuMAZy0e1svFqBdBTzYjKahsW6lV_51gEbnRTCpSKa74uYI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Fq210UbvHzgVKAPvuQ8R6Yxqp9Sxz6cbmGFawoVeasqJloTtTD8yHVRaCChX6egwqWsyGc83yr2NUdNm2xH_dFRUF2wmZ66vUW_w1FLecySkYK-KMnQIFUx6T8JnTyrdt4ao5S39tfB1Ac9GdYb6mFEIG0wBKJ18fhm5CljaiZZSz01hF0wc-Avv6wrHfEBcXLZfNOLoT4Lr2aXJv6GUVyq2ElyFsfyehVzxfVWKE0PxaNNoAqWpGKk8EX81-7TmigbOAEkfV_NrcOjHbOSi2ORjdrPeGzs3qkr0PnuMAZy0e1svFqBdBTzYjKahsW6lV_51gEbnRTCpSKa74uYI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین توزیع قند و شکر کوپنی در دهه ۶۰:
عبدالناصر همتی
، خبرنگار صداوسیما در میانه گفتگو با مردم به مصاحبه شونده می‌گوید:
«اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره!»
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/20812" target="_blank">📅 20:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0SmKDilUM6J4zq0ewOpFCnRAV1e7IqCfySoAfmke0BSHRMnc-j4ZoZ1bF-jOm_9TVlR-5OLgsSWaaANMbee_xgZl49Up9Pc9FZRjBwcZPLJCZHV7qILdXZ9hvRqWLyomjelQUssDdn3M4MMdHqyntQ4ungM5HSleMltchUq0Y-_IdFbZtuzRql8EXLqP30cUVPYYm1MmxgBfJZ76zIURCh1LhkChhq6E1iL0EQPD47v6MmvGvpHRpG2TvWc-Lib1XZRcQfHwKUkk2ZFIN0KXEM1sCrtPZM0AG4NblYV3pbr-Z3eVOuFQcSNL1EmIWOIadsNZCAh4jO74A697-2-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/20811" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مرتضی محمودی نماینده مجلس:
اکنون که قیمت نفت بار دیگر به 110 دلار رسیده از نیروهای امنیتی التماس میکنیم یک مدت کـوتاه هرگـونه وسایل ارتباطی و متصل به اینترنت را از دسترس عـراقچی و همتی و مشاوران و دستیاران پزشکیان و قالیباف‌دور نگهدارند تا قیمت ‌را در این جنگ اقتصادی کاهش ندهند</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/20810" target="_blank">📅 18:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
ایران بزرگ‌ترین حامی تروریسم در جهان است</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/20809" target="_blank">📅 18:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5uil_S27ghXgLaaRirJsP_Zf6dFEUnkhNFeUBMX2bJHWhmN56U99uFwnNKSlWIwDD9M7mwf759XBVomZLo2Lwme6bUMnGuxtWvBwIZ2t_-0pvn1hVqE0t4Oo9spHbObUpdyMnEAGiEjGNtjPKdULVMdM0oOj3zpiIcm-ni-cQR8qBOIVY3OqkC0G7clbDFXOObR0ZHj5qLb4CsSSp-JBTFKELKfXqXiZOAgpRkLO0aQcXl4YfPO377FwGoVAhtfCgMJi_Gg7dHhlf2NIjXJb3lpa6Lrd7ofZ9RSQvR90VC3qKBaHwN0UzDZ3VXcDnUwxHSXIGa6uVaQFtBtprk1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟
اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از یک درگیری نظامی به یک فشار اقتصادی و مالی گسترده‌تر تبدیل می‌شود.
در این چارچوب، ایران می‌تواند از ناامنی مسیرهای انرژی و افزایش قیمت نفت به‌عنوان اهرم مذاکره استفاده کند؛ هرچند این راهبرد دو لبه است و در صورت تداوم، ممکن است هزینه‌های اقتصادی و سیاسی قابل‌توجهی برای خود ایران نیز ایجاد کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/20808" target="_blank">📅 18:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA5PwIZqc6htFEyikZzzbzEtOpXCWZX4SnJ1ipZk0zdgHAvbBf8nk4eZSRfL_IMZkxUPlgFXOCUJlUiF2HUAB9XVINgZrUz_Wn84GmSFgaX-cCarZSheWwnwwRPJRAcFcynrVrW0pNx6kD5Q5V5VxlkyZjlwaovCBUm6Hp8tMhBwtbtJphfHuOCoWNAWZYuUiYXJ0fEsIzaNuykXL0I8uQbUBIpaczjy0AZLde5oeqIUIUVAepn-BJx_D9szTsduH2llYZnMfDynMtIsmktnBtbo3pVdgI0cnDlNirYWRDTGnKgBbJ3p9ovZiZq6H5KO7y_0WQ_JLpNEElSTgtuCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری روسای کشورهای بریکص</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20807" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20806" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20805" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 26
جمعه 11 سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20804" target="_blank">📅 13:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qffdl_VNT5dnH07sWWlFgBOrGwdbWhql33aFQ2hbS9hwcoLUNE3Qx6fmCS1m16rVM0MPDlG4oVn6J7TaHWqoCB9mjObBJp4Z4dOGtn9cNGezMF_RymDb8FBzAREGjxN2lpruSCC4MoJDVZiyvL_EdCUGp6j9HHDtY-6SmvnGKibzAgkLqu2GPNDYXF32ZirbgUfXDCxubZNfb-qWXs97Co0nf_n9tpMta2k2cDnw2xwmdmc1jJVwAAkSMA8mSAS9J1knKZmatKINbLV49ijLQ7cQIQ9YHCrpQz4m_HM2vc-YdQ3JGoOtGvBxzR2BLKog-pxEzazsGklUoCAsh5pyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20803" target="_blank">📅 12:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20802" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20801" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20800" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4NGeCWF4qttsqnWGozEbJmBq-YcWe2pJ17a2ZPYK7-IXg0XmHsgXQ0HzItDD4_e3tePjNMMZjOvZAbuk2C0D6Yt9Sg-whsR0db-pgAvqnhDfHGe2mqCq_xAD6cB4SYclcX0omwMr2PFdrY3mkGsCzcowsc56OmKT0RDX_6DqGO0mtesNSVB8XLf1IG4jhfwM7VGp-TevXmI0j_DWTr-XBEBcel3jiWteimmVnpZbm5wQFUuIRj5Q-O3QvzHBQmyOiU3joFttBivfgrDIuC7dHT2HGALhChRax7huIC24gQuIWVVjb5M8_BMhu6G7sCXeEmngx5UtqXYgwac-XBtKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.
نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20799" target="_blank">📅 11:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3KYn-38m_rpNU3q768ml-SLGWXXcraVQs7Z3PmGPaaZyqb1FTS6gC1yVz82aOlKxh089yF5xY1iwY37ihQDSFMhnDkloO-qUQT03p3s61lUzDDOPIyNPB2xZSo9aWSzW8SXUZa22YMVvt3e-5LwL3LDTZEFN-qVX6OlxlkF_pT80zIt9i-fWPOroFYLj5-F_g0Nm5dC2ft5OJVhmVtVbbL8SSwy-BP-Wwh_qfCF2JhCJNs-98aFK6WV1HrYyq_aETAsrIildscRvcScw9ZoJ4zNY-JBiKCn6weyzIuEaoAftn71RSYjnv0rSUJb723eFPd6LYdSPC49Vz2lgF2o1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جهش بهای نفت و تاثیر آن روی تورم تولیدکننده در آمریکا
جهش قیمت انرژی، به‌ویژه نفت، تورم تولیدکننده آمریکا را در اوت بالا برد و
فشارهای قیمتی را دوباره پررنگ کرد.
حالا بازار منتظر CPI است تا مشخص شود این شوک انرژی موقتی است یا می‌تواند مسیر سیاست پولی و قیمت طلا را تغییر دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20798" target="_blank">📅 11:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گویا امروز حوثی ها این خط لوله را هم در 6 نقطه هدف قرار داده اند!  با ادامه این وضعیت یعنی عربستان حتی از مسیرهای جایگزینی که طراحی کرده بود نیز نمی تواند نفت صادر کند!  به نظرم تشدید تنشی بسیار با اهمیت است و از دلایل جهش بی سابقه نفت در روز گذشته</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20797" target="_blank">📅 10:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi9-ik5qLBBztIq6IOz9qa_U5XYPtUmqorcOnVXNZYAXnzralAdEeHo4aeGIU0Y6XIrnLw4QCamDVHPi1Qci2qdFoIVpIMHusGyfchoIYHk_etVdEgCNSIB3nEbYJgI-tSq1ePLyE-Q_BtNzEO-jNGamPGZpFrnb0b5sHUD-bWLGLf8jFpA6eKfwEbsc3PqN4BVVP2QvgHMd4fw773l7bfQLRLxjasH80j8je26aG7Dd3A1twu709-wD-xpn29fPG-3gv8w2EhFEctqCi6k-54qi_NjAS6Qvnfa-ptukSjaZQh1lyZPaDSExI7U4R3gXlCqn-uOLn3zR3wnwAot_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای درک حجم و‌ عمق بی لیاقتی و بی عرضگی ارتش پفکی سعودی کافی است به این عکس یادگاری جنگجویان حوثی که پس از تصرف بندر راهبردی مخا گرفته شده نگاه کنید!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20796" target="_blank">📅 10:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20795" target="_blank">📅 01:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی ها هم می خواهند یک خط لوله از بصره به این خط متصل کنند</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20794" target="_blank">📅 00:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8aLHLSoiBGVrgyTkvCRew_gph3STi6rruqlT61W911L-XKQeNcQ_jeGoeDHKYfpEmX9kuh4VhO8snQ5p9rZM34G9oNh79tw8L4YW2gWfAhrqA2fFPd2eY7oVZsHUU83V75KGia6b5QFo-idjmgpkSKFPnlJ0BZuDyoR2vchgoFoX1-QsM374O6F73SWjA77ax6p66OLbcY_scplb8TbeNmb8EgQ82jX48SgXdmNVSN78XkPplmC80KYTrfiAnFlgVah-Huy3wtfxlxybO6DE7SE9rrL8AhDngda41bTiEItDnnU3n9xZkI8VoeQ6qkDeFJxdQFxExi_vcH3pwgrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20792" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علی الطاهر!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20791" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mleMDzSiIdxec5syexpLGqKyV2seDpnLB3Fe96laCqUz2XoeG8TSCIb1va_TbD6Z1DVbxp_bmdY1XYuhizB81qGCkQDpFWn73tdWoQBDZbQxBwGBKkZhoD6nbDLbGtkobl2YJFNIDVbwpiuVyJNE6zIpRScYYqKoapH0h-0HjqCOB4ApAi_jdtNZ_5-gT-SCMvuZCTEgpWOnpHBc9FVabee3YjpIjR7AEUpJODiKlvBwy_c7c8d7pFWfSwyM68HqtZFXB8tNLmZxKQSCZkN9K3evGcj6aI6jm8NXRRPjcy1zqIyEA1rvA7z_KLnUitgaO_dDkeEN1OQnyLaR6WLeoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکستن انحصار چین.pdf</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20790" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شکستن انحصار چین.pdf</div>
  <div class="tg-doc-extra">186.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا چین راه اوپک را می‌رود؟!  در دهه 1970، زمانی که کشورهای اوپک در واکنش به فشارهای ژئوپلیتیکی بر سر حمایت از اسرائیل، تولید و صادرات نفت خود را محدود کردند، کمبود عرضه نفت منجر به فشارهای تورمی شدید در اقتصادهای غربی شد. با این حال، این شوک عرضه، نوآوری…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20789" target="_blank">📅 23:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwJ7a5jExnQgxzDfvpMDNP6_PAeq2cdfle041ekCzsV6Xo2gn1UYxD8MHKhYkAm831jORKJYcIZ9E_5OmOQIyqRJFSqg_TnQxC33whoKebRHV9qz7vrbUWWba3UN756aVe56saJWIs3seCZNpO5mbUio-Sy353hmi6GpjheUxtexp4BRqJpk0DUM_VDw5xugOoc1r5EwoEFVRPsmXSJnl4slQQx9ORahbA_kIRHCAfD_-XOBiHkw0Fm_2IA_SMWRaelLDu95vy9YdPjtteHE23mPeszZM5t5IJj8UCeKRHpBgy8nqrjD4Y-AuLVcNNG76kW57ojlVAapxZB8rCQf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:  با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.  این زیرساخت‌ها،…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20788" target="_blank">📅 22:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:
با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.
این زیرساخت‌ها، یک شبکه تروریستی استراتژیک است که طی دو دهه گذشته، با بودجه و برنامه‌ریزی ایران ساخته شده است. این زیرساخت‌ها و مقرها در منطقه "علی طاهر" قرار داشتند و قرار بود به عنوان پایگاهی برای اشغال جلجول و کنترل و تیراندازی به سمت شهرهای "متولا" و "کریات شمعونه" عمل کنند. نابودی آن‌ها، به معنای تکمیل کنترل عملیاتی در منطقه "علی طاهر" است، هم از سطح زمین و هم از زیر زمین.
نیروهای ارتش اسرائیل برای دفاع از منطقه و جلوگیری از بازگشت دشمن به این منطقه، آماده هستند.
ارتش اسرائیل در این منطقه امن باقی خواهد ماند، به نابودی زیرساخت‌های تروریستی ادامه خواهد داد و از هرگونه تلاش سازمان تروریستی حزب‌الله برای استقرار مجدد و بازسازی توانایی‌های خود، جلوگیری خواهد کرد.
دولت اسرائیل به حفاظت از شهرها و مناطق شمالی از داخل لبنان ادامه خواهد داد و هرگونه تلاش برای آسیب رساندن به شهروندان و نیروهای ما، با قاطعیت پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20787" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وال استریت ژورنال :
ایران در حال ازسرگیری تولید محدود موشک‌های بالستیک در زیرزمین است و پس از آنکه حملات ایالات متحده و اسرائیل به تأسیسات تولیدی آن آسیب رساند و محاصره دریایی واردات سوخت را محدود کرد، در حال مونتاژ سلاح‌ها از قطعات ذخیره‌شده است.
تولید همچنان به‌طور قابل‌توجهی پایین‌تر از سطح پیش از جنگ باقی مانده است، اما تهران هنوز یک زرادخانه قابل‌استفاده از موشک‌ها را در اختیار دارد و در حال ساخت تأسیسات جدید زیرزمینی است که برای محافظت از ظرفیت‌های تولید سلاح در برابر حملات آینده طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20786" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">موج ۳ از ۵ در حال آغاز است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20785" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو
:
توانمندی فوری ایران برای تولید بمب هسته‌ای را دو بار نابود کردیم و آن‌ها بار دیگر در حال تلاش هستند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20784" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تنها دستاورد موشک پرانی های یمنی ها در دریای سرخ هم بدبخت تر شدن مصر بود و نیز برجسته شدن مسیر جایگزین ترانزیت دریایی از چین به روسیه</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20783" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHTVF75Xg0jVoKbfDHGfTf5X4XpqM7_3rqixjXyDeMYc3rbo0pdkawLZ7_lbswV3awMpRvoF4E-ghbLDf6jRr-Mojk31Tm2W7fCM6WPQHWO1Zs6dQ1DDTiYBte6peBHKdCAhwX1kb80m2l5RJidO4CJ-5Av8fgNgGr3fw47rJC3OBJaqAj7knfr6Pyk4BuHpgQshFM_MF4BV_w69HzY_VHxjjq4pQyAD2pfrwGWgZqri1JUHmXqxEMwQk-UDYAeg2drPvtN59TXvwmWEuhyubofMh-3jjzHtHuaT2t5rwN5QJVWIQv8qSFlxuNjuyAepFcPnf90Af6-50_nRNnQVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20782" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عربستان سعودی به اوپک گزارش داد که تولید نفت این کشور ماه گذشته به دلیل اختلالات ایجاد شده توسط حوثی‌ها به ۶.۲۴ میلیون بشکه در روز کاهش یافته است که پایین‌ترین سطح از سال ۱۹۹۰ است.
احتمالاً این ماه، پس از حملات به جازان و ابها، این رقم حتی کمتر هم خواهد شد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20781" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20780" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20779" target="_blank">📅 17:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urC16L2-AoYN4EcBn43DO4KSq4NhZY8EadjAaO2F0jWkB0yaH1HEV44ZDV0gjs4AGdDieO7CSnoc074QhqXNP9qFLZpigJFoe10YGelLuhwQsYnMinZXU4Fuf2k9AfYLgYavnPywUMbphnCSLEKflPjbmfGF5yDlm6inLhLoERmnRAp5iX7gvW_f995Zg69T5m72mZRaPpNtb1ltCL9rUKpscYG5sMuNLzEGw33mi_mVLq8DXbVpv2yjp7ViY4KMSBpUD5BF7Z1ByjDjJWEBb0-BMPjf8YxoKkiM-Ixvy6wxc1ZFMUCWKtciFiCbzFUMj-fsqgAf0Wx-1Pb-o8sZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این ترتیب باب المندب هم بسته شد و ۱۲ درصد تجارت جهان زیر ساطور حوثی ها قرار گرفته است!</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20778" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20777" target="_blank">📅 16:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اخبار اولیه حاکی از آن است که نیروهای مسلح حوثی(انصارالله) جزیره میون را در قلب تنگه باب‌المندب تصرف کرده‌اند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20776" target="_blank">📅 16:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گویا طلا منتظر انتشار خوانش شاخص بود تا ۳۰۰ پیپ بریزد!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20775" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">در یمن شاهد فروپاشی نیروهای مورد حمایت عربستان هستیم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20774" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGIsz0n-Soz10c17vbYw1odLo1aSXyOv1Xz9Q33LtrO2NpTGQs69Du-T3-DMSmJWH2nl32YAmEGNlP8HNqM3qaTuXrVogkGg7ygMD8PTST4rG7eGCn2jEuFk8MpgBn0Dupe1o3Hbi5p0rnjx-3GavYsoHY-Y1i-t5nl0bvJeFB1N_qjLg-HiAXHemehwCoRZkH4dED-TKsaZZcwtLBWVIuq-4I3_gx9ugl9Z0LAWuwbL4E_q-vRAXBXgn6hjDC78EC7ayBGUxSGb0_uioucltCnH6rgihLpQh4hhyk5MGPCUh6hRQDCqZ_wPSc3mENoT9ebuX8KBTDsGmPZS0BcYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزیره زُقَر هم به دست حوثی ها تصرف شد.  این جزیره در مسیر کشتیرانی بین‌المللی در جنوب دریای سرخ قرار دارد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20773" target="_blank">📅 15:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20772" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20771" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6Akvf-220lzwNpot3L_4GFjTGwYMYVhMmde5gTSoUvT-WdP2maKbOobNwzWInlS5YROXgkAhmBe-XOU2EYQ1aP48khlLptUVZX6S8Qpau72M83HT_MpFP9Tg4W8XuMbx9FrAT5SkDWaDKKOOChrjA4SCQ_b1-3eUnX_9XaQrWwQONQxaHgbfc1ZRFvYx3Oamgl2I5iSEKc84y8UprLNBRcaNMUNjxi1MUrSUvCTb-seLTXy-f0s1xLpqhC8FK6kVliipPEgYSrpF-ylcHKtqdJiQNJIdIDMdyWB9WJFLMSfPB6TSZ7AE4PFb0qfRCmnJu6WlMHVkXiLJ0B03cxvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 26</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20770" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حوثی‌ها در یک پیشروی ساحلی سریع، حدود ۲۶۰۰ کیلومتر مربع از قلمرو در غرب یمن را به دست گرفته‌اند.  این پیشروی به سمت استان‌های غربی تعز و جنوبی الحدیده هدف داشت و گزارش‌ها حاکی از آن است که نیروهای دولتی یمن با حمایت عربستان سعودی در سراسر یک جبهه گسترده به…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20769" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 26</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20768" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
پنجشنبه 10 سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20768" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بلومبرگ به نقل از منبع ایرانی:
ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20767" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG8bR77hanqsFFR5poTlOCZ3dSFyEm4ogY69o4r_DCsxMeQyH2g93zbybusoG8-2VKjl-Tg5u4tvGJfLCxaMpNz_DgmfH9huNQlBSkHpHya2HR2qgZkhXOlbK2BJjeVmAdDcODgVCPD03oth_9zoMBoyZXy0hvWxpDbVAN30_xQZiSMDFlywc1ssW-lCSpYyLGD-NZd1UizeOL9e-1OLr-kfxybeayUk6Jmin0vN4otbNE2XsegBoEoXVnPNOmi-F_vmM1LQ3JvovK_AAR4pwlDcFfdZSYfSef8fhmNIUlzs6OchFqKPqcE56Xj6ljaM83FIoEZK_DUYUGDKyfhqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20766" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">راستی فرهنگستان برای shemale هیچ برابر پارسی پیشنهاد نداده یک چند میلیاردی بدهیم شارژ بشود استاد؟</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20765" target="_blank">📅 12:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دارم حداد عادل را با شلوارک و پیراهن هاوایی و کلاه در پاتایا تصور میکنم!  اصلا آدم یک جوری می‌شود!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20764" target="_blank">📅 12:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH5x-HO2TIW7od5ju46r9-lljM5njiQvvMQCblGVxyqb4JaAUz4iobAs7Hkt3L8am8AaAz5aW8fI958YIM3XzMhyd1YFwf2MmW6pkkMXa_aSAnkTuk5kOeYfXCygas-zJowfLNhAHKyB6z8wNW2Nwi02Npr93LsMsDaUBZyFccR7QuPpW2Q60de6VLFJXpUcK82N-7eL60Bb84-vM5okvKHgosoYeeZpk6yDX-r680Km3oIPhelzyg88hjgoiemyJElL13wqNtiYY4AY8dxJw29c9uzvR6S5BxPv_bcqUNhirdoYLlnuxyTt-NLdu-dDIL3k6Hvo2TLuG8ZiSZx5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا انتظارهای تورمی واقعاً اهمیت دارند؟
انتظارهای تورمی زمانی بر اقتصاد اثر واقعی می‌گذارند که مصرف‌کنندگان، شرکت‌ها یا سرمایه‌گذاران بر اساس آن‌ها رفتار خود را تغییر دهند؛ از افزایش دستمزد و قیمت‌ها گرفته تا تغییر در سرمایه‌گذاری.
بنابراین صرفِ افزایش نگرانی درباره تورم کافی نیست و سیاست‌گذاران باید در کنار انتظارات، عوامل بنیادی مانند عرضه و تقاضا، هزینه تولید و قدرت خرید را نیز در نظر بگیرند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20763" target="_blank">📅 12:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پس مشخص است سفرهایی با اهداف خاص هم داشته اید کلک ها!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20762" target="_blank">📅 12:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:  وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر  با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20761" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:
وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر
با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی انتظار داریم که قانون حجاب را تعیین تکلیف کند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20760" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcUMHpMFuG-X053UfToocobSsY71UFgMDio6vnLk2w3u10JWQ6GnzcH0zXUX8xjQHSuaw_7sErZ1rmRN61RPdIBTxHUKpXGurYzyTIN7M2jS_bNaRL2MFVfJIj0uBnW5g1yAa5sUkQoWc7_7NtW0Wyc-w_sxWDfJaCp1O8YgGoE9EBFBc7IgWPDdFz9dsBv1hIrSvVANAd7yPtLUGjndDvsu4vY6-FRbFo81VvvSRe-R9Fa90_qYfyzKTK9wtSz_cqjz7NRwyKK2Eygd-av69arNOlfObVHH8sddG9ylg82V030nx3xX91GonNNUiglk0KAPsoVaxwic1_HB3FzrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.
نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20759" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ:   «به لطف نیروی فضایی آمریکا، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، ؛ هیچ وقت محمد جونز نیست مثلا؛ محمد العزوری.  می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20758" target="_blank">📅 11:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb_Y-E09cgr9sER8Y62w0BFN4XQ3bOyGFfUJ9v0LFbsxtPq1uXLM5MdFrbm_3l-G1htGnquQIE3wC_ycbXCrqwFjGsDUE8ZEvQmKnU1hlE-0fAVgkCqBOExAl37dpMua8NM0sLeB-4rcJZOuUnUqAnq22O5wjXIbMPNAre7EHqiw60-eHOn4mJp05aQrcgmdD2sL5pjpI7LnuR4CAcXRS10Xr3N_EeRXUYxL3bAy-jO4brqjAeZixPjwrY3B7B3dGVvFj6JvRPheITk7muQowxGrvgMN_AULaDyPiz0ecblo5Qr-WI1fOls29DQtVZz5Jm3bJtQwRRdioXVZM2HhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر بندری راهبردی «مخا» هم توسط انصارالله تصرف شد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20757" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20756" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20755" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شبکه سی‌بی‌اس گزارش داد در پی حمله موشکی ایران به پایگاه هوایی «موافق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگنده F-15 نیز دچار خسارت شدند.
بر اساس ادعای سی‌بی‌اس، نیروهای آمریکایی مستقر در اردن برای مقابله با حملات موشکی ایران مجبور شده‌اند، بیش از ۳۰ فروند موشک پاتریوت شلیک کنند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20754" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebnEVQRJWhHpJBkLbvjuOCgu2MOZE4sgBq99b5DxG3PLi-45WlOj_NCuvLlo9XB2x3rxMrJeh_lCxTIQW5_cF3wlcxJehbxqkJYCKuz1b8YOBhUM5oIgZpXDjnQVNnYcMyCf4ayYzqTWBcDDWED3WjI0EpFNRexPr6NQfX782eHI7Nl70MA7jye9wR7CowZ0WOKQH3oPeVCp2d08WwCvhEjJQ7fO8tuwwcpoTP6TWwtb6R8UQsNhOX_QZVLrwbkFsg88xNB6HiNZpR4xBXcN9rZ4u1iWn9fuDhuLo3tCEGGUpjgDBwNToIcQM45pToLHFWwMSqAkpvVg5rW_jS0lFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20753" target="_blank">📅 01:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دو انفجار در طائف عربستان</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20752" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ervyPINI2BztiE8kxQvtOZsvm2boToTFopwFO4aOVHYEenyrPdH7ke9PNckdPmRHOZRT6q-HVuFDwO32U4qH6o4aHaolhMN_ktUPON6vAA0nKpH6xz4pAwUa4_EQHy14qIdC3sJ4kIx_vmyv30GH80Tdtlyo9_2A3_xhO-bXt1jychsKoj90o4JyikMl2lKnBTIeIGm9-Flb6nS7oyncwxewhqbZlnolyHqNbu_hJWwDNV5XGCzSOB9IQURxWw2E1oycia__cSG_3ol5VpZPeGXnI8ijl7JE_qh7rLJJtQtaQwx7GFRfhaO980do6uHaTHNOElUU06Ee0gOMh0O9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک؟!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20751" target="_blank">📅 01:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پست ترامپ در
تروث‌سوشال
:
این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20750" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برخی منابع عربی از پرتاب موشک به سوی تنگه هرمز خبر می دهند</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20749" target="_blank">📅 01:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20748" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لینک ویدیوی ضبط شد
ه نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20747" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vau_Atw4Zw5kjqjBUPkFAMuWYy5Rj-TovHJFXpN9GjhAdBudLVD0bcExWWmt4payZyhHIPXuygGpnhUU4UBe93ihvXwm2wKz5u0Of1xuqWYviIJ0JKyyuTpyco5oOVhv9I3XiIoWmFdvmo36KphIDeAuAGTYlFnxx_lFT-vdCiLQstM1WL0ofZcyporNumSH6ZJ5f59-c45eCXII71glyTgLi3mfWeik5o6UMLf_Ex2uPJje_04SkS5L-6VzwalP4DtzG_ZzjMNFsa-dcWf9ByZqrbXg-xmyJqwyFIWoaUzwxsHgzW9xiVHIzd08NWbJNiC-i8tCWxVq5ZLAzgNGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20746" target="_blank">📅 01:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20745" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20744" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدای انفجار در بندرعباس و سیریک</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20741" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20740" target="_blank">📅 23:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIck74Gvxfvfj16CfkeEQzwGFjfkrEViSzvbxvmDIiQLDAGqh1oFL-welQCcxdb30r9a0wbc4ykNbLNbsa7I_B51BiS5P9sM_lIczIV41mrXz5bcdGHiyBdqGYxYia0-Y8UQ0yekVDlfw6Gp7BbB1dZzTa_0070uaXWL1p9XF-WSLpulf00uuq_LDi3K3Tl_jbZmwYyfxPt90lxR801ArCHtEhpmIGqeDljb1hugYo3JGqgnWn95LaRtpUstnZmIFVMc8vzMmaOtEDalj_7H8MIkRHH2N2GTOC1f7D-k6UZKltAvrdLYFIq8ecxW9EaMGykXXWwLUwQWzfXGJlV-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20739" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
باز هم به ایران حمله خواهیم کرد؛ مذاکراتی در کار نیست و جنگ علیه ایران بعد از انتخابات پایان خواهد یافت</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20738" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigiato | دیجیاتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVARaUSdyslRU7TXPDNvzOWzrKlg5u5qsAZaXqJlUiwZN64AXURUadNay7683XAuhhIhk98fQFLmPwRWoH39alL2rPFWCv7DCMKinjEiATdQagvFbqmaj6s04BgPC0X-_YLxobxyRHJJEkE79pXqjxWX6SZ3ZoMOwaPs3Y_nmq8wXUTgbpRudn4sn2QHIoQx9P2JLiHn3aFU59RLkpXZtC6V1RbA8GZOnXs_oa3xyQUSkk3NIKhbK0DAHRVwH5qMd3C8X-4bRIL4sE-VHDyIvtr2w90XGm6EdnbdhJSLkFj1LAs5ZxveGFTur1TYeDG43sUh7eYHvzGMwDXnQ8jhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
مریم عظیمی، مهندس ایرانی اپل دوربین iPhone 18 Pro را معرفی کرد
یک ایرانی در قلب توسعه دوربین آیفون؛ مریم عظیمی، دانشمند الگوریتم‌های زیبایی‌شناسی دوربین (Camera Aesthetics Algorithms Scientist) در اپل، در مراسم معرفی iPhone 18 Pro درباره فناوری‌های جدید دوربین این گوشی توضیح داد.
عظیمی که در تیم دوربین اپل روی الگوریتم‌های پردازش تصویر و بهبود کیفیت عکس و ویدیو کار می‌کند، درباره قابلیت‌های جدید سیستم دوربین iPhone 18 Pro صحبت کرد؛ دوربینی که حالا با دیافراگم متغیر، کنترل بیشتری روی نور و عمق میدان در اختیار کاربران قرار می‌دهد.
حضور یک مهندس ایرانی در یکی از بزرگ‌ترین مراسم‌های معرفی فناوری دنیا، بار دیگر نشان می‌دهد پشت محصولات محبوبی مثل آیفون، تیمی از مهندسان و پژوهشگران از سراسر جهان فعالیت می‌کنند.
#AppleEvent
🔵
@Digiato</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20737" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بیانیه ایران، روسیه و چین در نشست شورای حکام: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد   راه‌حل پایدار برای وضعیت کنونی تنها از طریق توقف فوری و دائمی تمامی حملات و رفع تهدید به تجاوز بیشتر حاصل می‌شود   همه پرسش‌های مشروع درباره برنامه…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20736" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20735" target="_blank">📅 21:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20734" target="_blank">📅 20:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20733" target="_blank">📅 20:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تغییر موازنه در یمن؟!
(این مقاله ترجمه یک یادداشت در یک سایت ترکی است و لزوماً همه موارد مطرح شده در آن مورد تایید من نیست)
جنگ یمن در سال ۲۰۲۶ وارد مرحله‌ای تعیین‌کننده شده است و ائتلاف ضدحوثی به رهبری عربستان سعودی پس از سال‌ها بن‌بست، بار دیگر ابتکار عمل را به دست گرفته است. نقطه عطف این تحول، توافق دفاعی مشترک مکه در ۷ اوت ۲۰۲۶ بود؛ پیمانی در سبک ناتو میان عربستان سعودی، ترکیه و پاکستان که همزمان با شکل‌گیری یک ائتلاف دفاع دریایی ۱۴ کشوری برای مقابله با تهدیدهای حوثی‌ها در دریای سرخ همراه شد.
این ائتلاف توانسته است نیروهای پراکنده و چندپاره ضدحوثی در یمن را تا حدی متحد کند و زمینه را برای عملیات‌های هماهنگ در تعز، الجوف و حضرموت فراهم آورد؛ مناطقی که نیروهای دولتی توانسته‌اند در آنها بخشی از سرزمین‌های تحت کنترل گروه مورد حمایت ایران را بازپس بگیرند.
نقش محوری پهپادهای ترکیه
یکی از عوامل اصلی این تغییر موازنه، توانمندی ترکیه در جنگ پهپادی است. پهپاد بیرقدار آکینجی، پیشرفته‌ترین پهپاد رزمی ترکیه، به‌صورت عملیاتی در یمن به کار گرفته شده و سرنگونی یک فروند از آن بر فراز استان الجوف در ژوئیه ۲۰۲۶ تأیید شده است. این تحول پس از انعقاد یک قرارداد دفاعی گسترده میان آنکارا و ریاض رخ داده که شامل انتقال فناوری و توافق‌های مربوط به تولید مشترک نیز می‌شود.
توافق مکه به‌طور مشخص همکاری در حوزه‌های پهپاد، جنگ الکترونیک و هوش مصنوعی را دربر می‌گیرد و به عربستان سعودی اجازه می‌دهد از سامانه‌های پیشرفته دفاعی و فناوری‌های عمیق ترکیه برای مقابله با حملات موشکی و پهپادی حوثی‌ها استفاده کند. اپراتورهای سعودی که آموزش آنها از اکتبر ۲۰۲۵ در ترکیه آغاز شده بود، اکنون از عملیات‌های تحت رهبری عربستان پشتیبانی می‌کنند. این مسئله نشان‌دهنده یک ارتقای راهبردی در توانایی ائتلاف برای انجام حملات دقیق است.
تأثیر فوری بر حوثی‌ها
تأثیر این تغییر بر حوثی‌ها فوری و شدید بوده است. پیش از این، مزیت نامتقارن این گروه ــ یعنی توانایی انجام حملات موشکی و پهپادی دوربرد ــ به حوثی‌ها اجازه می‌داد زیرساخت‌های نفتی عربستان، کشتیرانی در دریای سرخ و حتی اهدافی در خاک اسرائیل را با آزادی عمل قابل‌توجهی هدف قرار دهند. اما ورود پهپادهای آکینجی و سامانه‌های پیشرفته مقابله با پهپادها موجب کاهش آزادی عملیاتی حوثی‌ها شده است.
پدافند هوایی عربستان، که با فناوری ترکیه تقویت شده، توانسته است چندین پهپاد و موشک حوثی را در میانه مسیر رهگیری کند. همزمان، حملات هوایی ائتلاف، مواضع و سایت‌های پرتاب موشک حوثی‌ها را در صنعا و حدیده هدف قرار داده و منهدم کرده است. محاصره دریایی حوثی‌ها که در ۲۰ ژوئیه ۲۰۲۶ اعلام شد، و همچنین حملات آنها به تأسیسات آرامکوی عربستان در جیزان و ینبع، واکنش بی‌سابقه ریاض را به دنبال داشته است؛ از جمله حملات هوایی علیه مواضع نظامی حوثی‌ها و تعهد عربستان به استفاده از «نیرویی بی‌سابقه» در صورت تداوم تجاوزات.
حمایت گسترده‌تر دفاعی ترکیه از عربستان
نقش ترکیه تنها به پهپادها محدود نمی‌شود. حمایت دفاعی گسترده‌تر آنکارا نیز موقعیت عربستان را تقویت کرده است.
توافق مکه امکان اشتراک‌گذاری اطلاعات، ایجاد سامانه‌های هشدار زودهنگام و نظارت دریایی را فراهم می‌کند و در نتیجه توانایی حوثی‌ها برای گسترش قدرت خود فراتر از مرزهای یمن کاهش می‌یابد. اگرچه اعزام مستقیم نیروهای نظامی ترکیه به یمن همچنان بعید است، اما صنایع دفاعی ترکیه و شرکت‌های نظامی خصوصی مانند SADAT پشتیبانی لجستیکی و فنی در اختیار ائتلاف قرار داده‌اند که اثربخشی آن را افزایش می‌دهد. گزارش‌هایی نیز درباره انتقال تجهیزات نظامی ترکیه به یمن از طریق سومالی منتشر شده که می‌تواند نشان‌دهنده حمایت غیرمستقیم اما حیاتی آنکارا از نیروهای مورد حمایت عربستان باشد.
تضعیف موقعیت حوثی‌ها
اثر تجمعی این تحولات، تضعیف موقعیت نظامی حوثی‌ها است. این گروه اکنون با برتری هوایی، جنگ پهپادی پیشرفته‌تر و نیروهای زمینی متحدتر روبه‌روست و توانایی آن برای حفظ عملیات‌های گسترده در حال کاهش است.
شکست احتمالی حوثی‌ها می‌تواند ضربه سنگینی به «محور مقاومت» ایران وارد کند؛ زیرا تهران در این صورت مؤثرترین نیروی نیابتی خود در شبه‌جزیره عربستان را از دست خواهد داد. چنین تحولی می‌تواند توازن قدرت در خاورمیانه را به نفع بلوک سنی به رهبری عربستان سعودی تغییر دهد.
در شرایط کنونی، به نظر می‌رسد برتری فناوری و انسجام راهبردی ائتلاف ضدحوثی در حال تبدیل شدن به عوامل تعیین‌کننده‌ای هستند که می‌توانند روند جنگ طولانی یمن را تغییر دهند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20732" target="_blank">📅 19:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20731" target="_blank">📅 19:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHpt_DJJwf7NWR4bOvhiOJlseGCih4lgxfD69lLu_GxDynou8NClYE-_EeQKrz-0PCTdMRoRawAbcZ2QENMnuj4R2opU8XD3FcUR4vbFE_DAENmivpWUiNJc24qFHdx5KcdHkcc0a9EqL8nWVN58I4eUSuFVLu89KwmiORYJ6eoE7zPXYtpWI_BPXaWCryDgd8SqQs7Uv986oAjLJXs8afoapZzzVGgDUu4GS7MGta_aPeCWjHuNUpHB9fUkapDIfqsO3ShGtWxIeOyzdfSvlpN-suaE-jzhtSrDDCRbxZI3q2dbVSeVI4D0X1kA0x8A6dDy24NL7bGbGbxSPl8Ueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4xJZm7IJBsrsCEPY9QX7rrSA_W_Gci54v0M28bpzxDCm060DSg2pNafMIluAlGkD5YuS2in8NK5s5txdbmU7zjymXJnAmmue-kTQmwDZKR-90jDKUKb7-ipcXXeFaSjk8q6zqa5OQDQ4YePmIM4-WCD80oQd9z0iLxnClVnKFyBmGzN_dKln66Lj6R88yBDx_o1k89NLSRFUSFg7pMohwoQUtRioTxm_30aSXdHNHC0MVkIetfLm8_pkvOJAdqyPbbwwt6qL1pJ3c9-xN_UZATxOAF_2BqDAtgAarv6D_TxhlJ56oYTQQVmlmF7wRW-XprQF0KF5CDo20iJEVXArg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20729" target="_blank">📅 19:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20728" target="_blank">📅 19:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20727" target="_blank">📅 19:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20726" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک روزنامه ترکی:
عربستان سعودی از پاکستان خواسته است که در عملیات نظامی علیه انصارالله شرکت کند و مداخله نماید.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20725" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfrg9hN8dbeW73Umok99oP9RDkeHfFYq2HFlp7d16r4K_l9LRxZYq07zkWUVWFF2CfZ2KS8vSGV3bFQ8oVVfBImoMmH6aaAnVnKGDFhnNdsKN-55PyavUs-zM9qsBWlV1iyAHL2z32olKusJc3vhVyL5CyEmMtmigQYuNwrglZDr1AyjTiNz5ggcciI9uw53yA1Rx_qfOQVglN2eG9w6_MT1nBrFztuBNdqiFJj9cA5uSciDaxpbaoSQ4rxquju-PHY58eySwPg3gThR7vTYjeByE4aqTcdA9j1AjA54fCL-uUhiNnI6KIMCFbpHaP_1onaP8QgCjP0kQBrRX-_8zocM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfrg9hN8dbeW73Umok99oP9RDkeHfFYq2HFlp7d16r4K_l9LRxZYq07zkWUVWFF2CfZ2KS8vSGV3bFQ8oVVfBImoMmH6aaAnVnKGDFhnNdsKN-55PyavUs-zM9qsBWlV1iyAHL2z32olKusJc3vhVyL5CyEmMtmigQYuNwrglZDr1AyjTiNz5ggcciI9uw53yA1Rx_qfOQVglN2eG9w6_MT1nBrFztuBNdqiFJj9cA5uSciDaxpbaoSQ4rxquju-PHY58eySwPg3gThR7vTYjeByE4aqTcdA9j1AjA54fCL-uUhiNnI6KIMCFbpHaP_1onaP8QgCjP0kQBrRX-_8zocM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکایی ها عموما از اوضاع جهان بی اطلاع هستند و خصوصا سیاه پوست هایشان که رسما توی دیوارند!
اینجا این منگل در پاسخ به این که چرا به ایران حمله کردیم می‌گوید چون ایران داشت نفت ما را از زمین میدزدید!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20724" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">منابع محلی:
بیش از ۱۵ تروریست هیئت تحریر الشام (HTS) در پی انفجار انبار مهمات در حومه شمالی ادلب کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20723" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خر تو خر در یمن!
نیروهای ائتلاف جنوب مورد حمایت امارات امروز سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20722" target="_blank">📅 17:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAZOVMHQKVEub_k-hf2l7lpw-Q4-GnJPtfVkNayctDgVv2vrg1a2t0ZFKVyoeyzsjHrgcuhxBQVzawlh0XxvsVkKGemaLZrMrxU9YpyBRM5cgrRXAoj-4AvU4CoirTtSht1o-74ZI0japkDqA0O6C6-IaYODhXDMTPJtYKb0ZQUUZb12n6hVvb58t-BWpQeYKKB2Wp7LYKXdDkuP9qLklKaUBStS_YklxGPKs62bpwFCczSqVkG8JHJuKwjM5X4wJlkIR_byx5LJiuw0vW5pjsnJlGqTyrlxpYjqbVGyipGoiXB9sbf7kqzR25a-ZcqyYfCHaKId2FdT2YZtO1ZgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4DEAKytAQxLdVqZxJYXX3MfvNikkBCUn60aSrGrU-BwWH8thjV_ybh5_QiONoMSIar7OyBhmDuEGCqUkntdSwKB7dADtR-6Mf_IPO8R__nPDq0z2bf_uRhAs86F8CUrHBUFkT8jzqAvIXt0Q5mCKkO2nv6EiNlVk29PHDgp4is85nLbhvA9LEY9UTAeNiQdH4vl9NZO3hfsjGG18rOcaDQ9tDTPV_y5kt6ZlIYlT8A97sAJ2Z6HvNVaLYebZkfg84OrSI9QE-rXFEjeuG6wTpDxlypB64VxRZlQBVGX_l_BJFh5JX3wd4jMiWBgcBn-mQDLqddpv8P4rDfK7ME2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgH3eTIsiLujZfI5ZuGULFHKKjxfjYR0CSireO_j5qDSuI4O9fnXBrEhfLK283DwcJnP8pOpgB7-DQZHqggpEBKrX4blgxtbmfsitEXXS-KzDRtqg0PQxXK0r7dlSOH-PbgUqBqgneQqoV4KnqCDyLpZSYtxsh0BYtiNqusSWTbrZYdQmdSZL08Z0aj-LTtt-FLclT3-FBzFU9WqgNmi-ZOa447KVFlZKI3oUuMRe4X1DVKzpXFt_fhSXPAiNvylggxG__eB6lf3dfQXAYzvdOn3R-TpPlAxDvJZWZUf6b-y2wDqH7PGM7LbXAX79ypRFbtZRaWZ75dQYv6vEdnIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAMfa7hqdKmpsmQekwYHkGGzVLdrUiC0oCx5WzJiKnZ24nipj38Yj2_avoeBcVFaJYwTT4z6NbjFc0OrblIWP4wBfq2A0XhomYUuCUxcU4muWj0N8jC_HoSEH1kDBRhe1KqunRqZXz7gFDdH7QsLIdH7Uv7e1mAdh4Acbf47qIZcUu9PEhzjnRje_2NlSI3kh6fG3vkpJFzI9bc5csyxCWIGa287RKfiV9w2KDBlbzyDhS5yX2PtcopoSSxSBklhuvNejGhAf7yXFRIjGBtA1qDMHhc10YXfuBGNwwLL-quptkWS7-aqJcljPYxqE7dnDVTpVUx-iKyl6zbAawzMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-k8aShRDwgtn63W3yD_BGdaUuTK3AHg-tFI_tdylGb0V0nJspIR0zIQw3utYrEzddTAAcmPoInf5m-a3vixoCRuWQwqqjAkclNv3Z5vtMekggWhNuKWqAeobvIvsBBbdokn23X1rL85L18WJFIuDC28WJcqa-7uGw8WdR9O7_KVSWhItbO-M0lg0zeFRb6d3FPf25u5EHdLCc5vnJtZ2K85H8qMePS6iJruIaThHcJSAw9gcg4QHT07WhQdFkrNx0t9_EYZFQpX9zF3LkuS4oHkWD47gwLKikoK8WqALCU9vTQRsfjXmH53XjL9fYs6L95j2t9iB28cvuaCAtg02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3IekVVlSnN6ne5MGKrVncckwOfQCwR1m_WB-6x6_Hugd2KP6F1PpcGwkv8XpPWninjYK-SpAI3gj3FxOMiMwnVtt8QyandI_2thEGKGXYC_kWroQar_6WeUvaIYoROdAjaWFTznanjovkXr1z3AFXCABiZ-a-NHnU09eqv4b18J-_HoXybmKg3-KXqZbMiFi40z5xKevbAXcqTRP8N34kqhbqile_6xDAgApt1NMJUDms6FHSK8IsTE721XlbnxLmOeUZS5PRfKBmdg52r24HRVyDQD808iMFR6_Fb2aLZOvTz3Ug3bhb4hoE6yJzSXIPCsjzAEIgs-CEbePPsUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqF2ZPpirhNx0VaVMd-4zX6iy0sD_qd5XCCZhm567GYmpU1UFWHV3PbqYvT2eMRdpUUSYnknIScyBGSkNKPnihDwbVY2mMoap8ki2NApniJ980NYWhJ1asL01NVMu26mtrrUqmlDqxgO20KAUvencfHe7yjTf5UFiLZgkBjrtL8jSjrJFP-i02D34ZyCgfpEwMWPfb8N5c-P82bIGXaQwcQUiQydVnLaR163HUVSXN3vRrM4jnThC62XHtKi55DpBcDIvbmA32QZYA1hXnqUBIKogU8xLqcRBu6x40LoCy8LT_PAdoOJuR4l95ytz32IgNf04xK1vKF6ft6TlxlEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbOPyIC8UQX-odtnhIjPggL4eR4LgV14UPPf7cIz8TnLTQcx5sEVEDTTJ05P0yG3e1q7kc6OvzX5yHtJIGRdGE68_7OVAkTH-3dvap13LlJdBI2QLleO1YMzmyUR2X1t6YCl7gjahq8xm9sGPjbFQnnaa9Zcyra-wjQJV4ZmEKCTo7LwHTg3YW2Hrsucvy5UJHLxthiSm0ps1DQAGmmLQH9ACDXa8IRHpV1goBwDRz5NiRDBeX3sY_K7HdCL-VaDfJ9eoSwUDlpOWNr21LUGmvwtj6bnQHJM64VJjsBybeR4wwe1KP2yFNh92oxIWk6aMOnSQNJJQMeBAaqYRHZJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHGlWEF-6jYlOw8-AX4WcjqiJ4HZPjv8NbXUkdypqFaHspFt9ppgpd5b24ABfZvJd9yB8mlkEjhp1CO_eazZ-sWAxcLbVn05iiVey5IwLH9O0QZBJfzvQSKps4wTxEDuwa2jAU6snTdUPGb51MPOFDDR4RPkEFBJcP1Kk04uEAtZZmZ1zfwR7b2lU0CwISdUxGGwJ9hOW_-FVqhWNR2GUG8kzfPY8ViI2rvA2tLJoBc276K_3VtsqQBVfPG1eZY9v6-wyqfsYaw3MOWwWH8vNRrNACOb6g84zuhjfk62G5AJ2mZXtLKAxjDJyaljafK_sEsB7CscpP8IhU2VK9lTqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در دره پنجشیر، یک تنه در برابر ارتش سرخ شوروی ایستاد، آنگاه که کل افغانستان زیر سیطره رژیم کمونیستی کابل درآمده بود. در میانه جنگ‌های داخلی، کوشید که ثبات بر این کشور گسیخته‌از‌هم حاکم شود؛ اما نشد. تا انکه طالبان شهرهای افغانستان را یک به یک تسخیر کردند. این بار نیز در پنجشیر جانانه ایستاد، آنگاه که دست یاری‌کننده‌ای را نمی‌یافت.
در میانه سال‌های جنگ، روزی در تخار در شمال غرب افغانستان، در جمع مجاهدین و خبرنگاران نشسته بود و دیوان حافظ شیرازی را می‌خواند که خبر آوردند طالبان در منطقه‌ای حمله کرده و در حال پیشروی است. مسعود توجهی نکرد و به خواندن دیوان حافظ با عشق ادامه داد. یکی از فرماندهان از بی تفاوتی مسعود ناراحت شد و با صدای بلند گفت: آمر صاحب! طالبان حمله کرده اند. مسعود گفت: بگذار که این غزل را تمام کنم، مگر نمی دانی که جنگ با ما بر سر حافظ است؟!»
۲۵ سال پیش در چنین روزی، احمد شاه مسعود، شیر دره پنجشیر و قهرمان ملی افغانستان، ترور شد و جان خود را از دست بداد!⁩
@Iran_Simorq</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20713" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!  از این جهت خیلی شبیه احمدی نژاد است؛   منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20712" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع خارجی:
بر اساس تحلیلی که از بررسی تصاویر ماهواره‌ای به دست آمده است، در سال جاری شاهد افزایشی در ساخت‌وساز در محل زیرزمینی مشکوک هسته‌ای ایران در نزدیکی نطنز بوده‌ایم.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20711" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خارجه یونان، جورج گِراپتِریس، درباره ترکیه:
«ما درک می‌کنیم که این نوع تنش‌های بالا که اغلب از سوی محافلی در ترکیه همسایه می‌بینیم، همچنین به این دلیل است که یونان به قدرت واقعی دست یافته است — صدایی که بیش از هر زمان دیگر شنیده می‌شود.
من فقط می‌خواهم اشاره کنم که هر کسی که فریاد می‌زند، همیشه قوی‌ترین نیست. در واقع، اغلب آن فرد ضعیف است.»</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20710" target="_blank">📅 15:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20709" target="_blank">📅 15:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20708" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZSz_XV8aei7zQlYNOf7ic_0tuAT_6Ljx-LAbYipBJLrOZ1515lTNf1RR4zMksRo9Q94cI--f9VmkBObyai1o_sxFDnBvzgc5WT9_5wdz_mtv7fyXg12cnQ8PHKL9rYA0X7gXVQSG8YqY5lxOtDDlZYGht9BdJNtjIm_5gcq1MyxyKgl3aHDApMn6n4ZA0l6_5wdxd-QbANXcEnoSVyw4UURNLC7LwlClLiJ_pihbd8cDFVLy4ChkkamTyCAy87zMitS6TVxjjyIQlGFSo_CHldQV6pqSL3aJHUBcmQG7iuPYwlLbTwxDHTBMUjpZm0vh4baLVwNVAuReLPadOL3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20707" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سخنگوی سپاه:
هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20706" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این تحلیل برای 1 اردیبهشت است. تارگت من برای قبل عید 150 هزار تومان بود و تصورم این بود که از یکی دو هفته پیش یک اصلاح موقت بزند تا حدود 120 تومان که این پارت آخر نشد.  با این شتاب، اگر 150 تومان را رد کند تارگت مرکز تحقیقات مجلس در 240 تومان را فعال خواهدکرد…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20705" target="_blank">📅 15:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شروط ایران برای پایان جنگ توسط سخنگوی سپاه اعلام شد:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش اسرائیل از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20704" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
