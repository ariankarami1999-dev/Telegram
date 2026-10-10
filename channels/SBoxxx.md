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
<img src="https://cdn4.telesco.pe/file/RNySXtYNBopA3iwwhDcp3mKG5kQtJNw4c2vXJL92PGAxodh8onRPNimOu1159XNX1yh9UaLI8Y_JKIwxHHfZnu7IzBNRnmVOcvLWvJgKUsJ4bdQpbtM6e3uHXpYZ5IwRO241GRdBzqDSIXRPNkOIjDmb-FMS-O645EjAa_pX5Guo39ClUq-9U0WqWmDWT5mf_-nUX5OPWrgnFULC4JcqLDfFiBAtKLhzA20f4xXl-BDntA9cQ53N6nQjUK7O51OyoSHH8ENRS37a1c0Zm2KSKQYONMM8M5cOD70GrLHlpnHD_TBA7wlYYbDFzDOv6rg2FbDTku7mzOCKAuPb1HjXTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چه کسانی از خرابکاری در اهداف انرژی سوریه سود می‌برند؟
همان‌طور که سوریه خود را به عنوان یک مسیر بالقوه برای جریان نفت عراقی و گاز منطقه‌ای به سمت مدیترانه معرفی می‌کند، یک زنجیره از حملات مرموز زیرساخت‌های انرژی آن را هدف قرار داده است.
در ۱۸ اوت، یک انفجار پمپاژ گاز را از کارخانه ای در حسکه متوقف کرد
در ۲۸ سپتامبر، یک انفجار دیگر به خط لوله ای در دیرالزور ضربه زد
در ۳۰ سپتامبر، یک انفجار نیروگاه‌های تشرین، دیرعلی و الناصریه را از مدار خارج کرد
این حملات با تلاش سوریه برای گسترش لوله‌کشی گاز عربی همزمان است - بخشی که به تازگی در الفرقلوس افتتاح شده ظرفیت را به سمت ۱۱ میلیون متر مکعب در روز افزایش می‌دهد - و نیز احیای مسیر نفت کرکوک—بنیاس.
چنین مسیرهایی می‌توانند جایگزین‌هایی برای تنگه هرمز ارائه دهند، مسیر مستقیمی به بازارهای اروپا باز کنند و هزینه‌های ترانزیت را کاهش دهند
این مسیرها با صادرات گاز اسرائیل از لویاتان، تامار و کاریش رقابت خواهند کرد
اسرائیل، که از سقوط اسد حملاتش به خاک سوریه را افزایش داده است، از یک دولت سوری ضعیف‌تر سود می‌برد.
ایران هم از این جهت که جایگزینی برای اهرم فشارش در هرمز دشوارتر می‌شود از ناامنی در خطوط انرژی سوریه بهره مند می شود
باقی‌مانده‌های داعش با توجه به حملات گذشته به زیرساخت‌ها، یک احتمال دیگر هستند</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/21597" target="_blank">📅 14:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/21596" target="_blank">📅 14:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز گزارش داد که مقامات در تایوان می‌گویند معتقدند چین در حال تمرین برای یک محاصره دریایی احتمالی با استفاده از دارایی‌های نظامی، شبه‌نظامی و غیرنظامی متداخل است.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/21595" target="_blank">📅 11:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚪️
کاخ سفید دسترسی مایکروسافت به ویزای کار دائم را قطع کرد
دولت ترامپ دسترسی مایکروسافت به سازوکار ویزای کار دائم آمریکا را به‌دلیل سوءاستفاده از برنامه‌ی نیروی کار خارجی مسدود کرد. ادوبی، کاگنیزنت و اینفوسیس نیز در فهرست تعلیق قرار گرفته‌اند.
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، مایکروسافت را متهم کرد که بیش از هر مجموعه‌ی دیگری از روزنه‌های قانونی بهره برده است. کیت ساندرلینگ، وزیر کار، اعلام کرد مایکروسافت و ادوبی در مجموع نزدیک به سه میلیون درخواست استخدام خارجی ثبت کرده‌اند که به تأیید بیش از ۲۳۰ هزار ویزای H-1B و صدور بیش از ۱۰۰ هزار گرین‌کارت انجامید.
مایکروسافت در پاسخ گفت حدود ۸۰ درصد از ۶ هزار پرونده‌ی H-1B سال مالی اخیر برای تمدید اقامت یا اصلاح وضعیت کارکنان فعلی بوده و تنها یک درصد از بدنه‌ی استخدامی این شرکت در آمریکا را نیروهای تازه‌وارد تشکیل می‌دهند.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/21594" target="_blank">📅 10:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔸
قطعات حساس جنگنده F-۳۵ به چین رسید
🔹
اشتباه یکی از کارکنان شرکت پستی UPS موجب شد که قطعات حساس جنگنده F-۳۵ به جای آمریکا، در هنگ‌کنگ و در اختیار دولت چین قرار گیرد. این محموله شامل پوشش شفاف کابین خلبان با فناوری کاهش بازتاب امواج راداری بود که نباید هرگز به دست چین می‌رسید
🔹
کارمند مذکور ایمیل هشدار مربوط به محدودیت‌های حمل این محموله را نادیده گرفت و مسیر انتقال دو قطعه را تغییر داد. پنتاگون این قطعات را «غیرقابل‌استفاده» توصیف کرده و برای بازپس‌گیری آن‌ها با شرکای صنعتی همکاری می‌کند. پس از انتشار این گزارش بلومبرگ، ارزش سهام UPS کمتر از یک درصد کاهش یافت</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/21593" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زرادخانه موشکی ایران ممکن است شامل سیستم‌های پرتاب سرد باشد
سیستم‌های پرتاب سرد در اصل موشک را از یک کانتینر پرتاب خارج می‌کنند، پیش از آنکه موتور موشک روشن شود و به سمت هدف مورد نظر حرکت کند.
شایعات و ادعاهایی مبنی بر دستیابی ایران به این فناوری از تابستان امسال در شبکه‌های اجتماعی در گردش بوده و در روزهای اخیر شتاب تازه‌ای گرفته است.
با این حال، منتقدان ایران اصرار دارند که این گزارش‌ها عمدتاً توسط طرفداران ایران پخش می‌شوند و از تأیید مستقل برخوردار نیستند؛ که با توجه به بی‌میلی آشکار ارتش ایران به ارائه داده‌هایی درباره توانایی‌های واقعی خود به دشمنانش، چندان غریب نیست.
اوایل این هفته، سرهنگ‌کل محمد اکرمی‌نیا، سخنگوی ارتش ایران، اعلام کرد که تسلیحات پهپادی و موشکی ایران از ابتدای تهاجم آمریکا و اسرائیل پیشرفته‌تر شده است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/21592" target="_blank">📅 09:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پرواز انبوه هواپیماهای ترابری نظامی آمریکا به خاورمیانه</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/21591" target="_blank">📅 09:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from(تحلیل نظامی و اخبار جنگ) MilitaryToday.IR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGL3TYxQTCsYlIPOfW1dLB1Ddnz6nI3BIkXqE6TPC4Jam0WOhZlhkub_09kqsfSL6D7t9sMiboB4en8DQcKvBdv9rfQwYTca4L7P5cwRmzEOqSalBwKL2kxrDO1hA_gJhskrSD9hl18x3EQHpUo4SOWv0PHUkS9NDa6IZoYGgpWEX3oGITwyq6xi5yy-zDtNv3J9gLK_M4H2RyvBxNoUuhsilaUSRTSBVZaH1eCwJRSXdp2xLFvp1oWhmIc4OrItdVG5Evez5T5yvz6uDD159RMI5-QGrL5GgIwlq_fdhSfR2CXCFP_0Zw9ft36o94FWzJaAEhKIUwxcRd8Izz9fsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
افزایش چشمگیر حملات مسلحانه به نیروهای امنیتی کشور: 12 کشته و زخمی ظرف 24 ساعت (15 تا 16مهرماه) ثبت شده و هنوز بخشی از تلفات احراز نشده است.
Leopard
✍
@MilitarytodayIR</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21590" target="_blank">📅 00:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1s9VVJt9WAz8rLrVMJkTMHNQBhxRoX8iM4bvjTz81jP2-5AzvsyFe3in1Gjdd6jVTi0P0m9kR8_xlGSU5Ac_hdcAj867sY7WtsvMSMsez-1C7B0c3Fzx0QBTS7yRNZUhMkzFWchZpAPOww4aPUsFPo0zhNqmxTZ-7FTGgPz2vIYExyGHh8kJRQvRysLDZ7mIKgtDdRyR6hEX_wF_OkOjXaJSFhfN8ISCjAtR5dP4O1mpYksG1Y5qEoua9o9h29JlSBPLXzvvw39jVxQwlxggMFBFtbgX46nL54EYvDrk-WVCi35LZoCBgl6t_-jEHDZGz5dB_Ugv0zgoZPkzoq6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم عکس تانکری که امروز سپاه منفجر کرد
به نظر می‌رسد گاز قطر را حمل می کرده</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21589" target="_blank">📅 00:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قشنگ آدم حس می‌کند یک مشت مافیا با هم نشسته اند خلایق را از جانفدا تا جانفنا بازی می‌دهند !</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21588" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21587" target="_blank">📅 00:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHwD972xAswdf8oRgBYiX9aHhJ9pNBH3tibMv1ZFFc0qs7gFGrcwPJXdth8Px6zmFhKbquEhc19EMw5_8_PfIq3tUVPgCFLjt2AjhRQZThWy42cXS2rFT447mn7x5vUB_sGHNO5ONKchxRT2U5mKUnYqYh6lksokvqZFm6mhHoRRGQkCqJEEsxHyI12SJCCwjKqY6tQCnXSeYa6cqiZ9rsdBVh9AIj_UXCbWDrxanCWMgJdHIv6W8v2jFpUCDMKnKHbycHeDd8TnvfwOCfSNp5xzyF7T382CaruEs2VVDzYnXElQ-oDi3CFL_Sap374MNEBLiejakmx7I1toel85Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی با کمک هوش مصنوعی از حرکت اخیر روسیه</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21586" target="_blank">📅 00:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چه بازی شد….
طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21585" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حمله حوثی ها به تاسیسات نفتی عربستان</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21582" target="_blank">📅 20:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خلبان یک هواپیمای خطوط هوایی سعودی دیروز در اثر حمله نیروهای حوثی به یک هواپیمای مسافربری که در فرودگاه ریاض پارک شده بود، کشته شد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21581" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">افراد مسلح یک خودروی هایلوکس حامل نیروهای نظامی را در منطقه چشم‌زیارت زاهدان هدف قرار داده‌اند. پس از این حمله، نیروهای نظامی و انتظامی به محل اعزام شده و گزارش‌هایی از ادامه درگیری و پرواز یک بالگرد نظامی منتشر شده است.
تاکنون آمار رسمی از کشته‌ها و زخمی‌ها منتشر نشده است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21580" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kETwY9cZziHx4cUZ3UGctVQ7ScIaaR6skprXgM5kS_oQwuPhVtgw3XhfCz721aihcWSm8jC-3wp16u5onsOy_qN53F8uOHYesUS_eHbHPsqyK5O2WsnWuJxsQpGJskP6-8VCSPlWGaoHDn1G0Ghkh5qbek73FlK-ooNg86PHN-Oz13YhBx4Id1uTuI1eIeTPFeAH33ro5DD9Wor338YUvHInhn34-Wwnlpcan0fIfQu-ZZE6_wr4-4e0j_Ag3IgvwGt5xRm7JgXFDQCZCYOtySIj6wgx4APSMDMuerdMlC7oCsWRrnui3NvmJiMyo-vWuG5B6f6Xt5nqc8ZJXOZgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای بازار سرمایه و ایران.
کسب مقام نخست مصرف تریاک در میان تمام کشورهای دنیا رو بهتون تبریک میگیم.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21579" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by9kq85t8Pb8dSQ6WXF1bKzlssBJzW3p-xmaUFVrep0QA1cHVVpa27wHDvOu7DxmqgEcDySixLlNH2U0-8u5kSF0-qH5xCH2FG_x4q_Ax_KV7uuogwewTqVGi8EeoHvOPTreQOQmxTU9uMYGNa3Xh3RuGYMknPHMkPbW-eDOxAVYWwEqewPQp9hzRWayIdHKlGbIzmG2v_womuRaKF0aQiI-8cct7S0v1WsUyn7uE1NTCOJgjXvqQuNCWAgUCw_FxJNm1E5Nmdhtwu8a5j9enlLr6BRdb72BJwaqB9z0FujkrhGaKiA0tPMcQY9tKYkEUI0toNwi1Z64yGJc8VTPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21578" target="_blank">📅 11:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc4cDEeh004lVJq-1Bk3RpHiz2N_7eyBm2gv0AL-BunxIBhqUy43TdvVEGlhigclBf1SUhhIEKdl-l6iwUETznwmti830Prr_KSDVjkHhC3FmcO23-Ini1jyLdLw72joSrJkmG_yK7oiUiQb50mqMCXgmJSVAA20hP7LdYWCwyRWM_sEvX8bxUUVpeOBLnpPjX7yoBzx11Dmg_DJ7uJTrevmxIrCpgM5fBPCHfAnUDMfdyI4d5Uuo89R-1D_xT2-U7uZbNpY-AqrA4h0Ej9CJ_jhj82c2lTWP_3kaMpO_0klgI8f1r4gM8CsFprDWP4YeVDmkPmKrGkc0DFRwc_d5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC با رشد سنگین طلا به محدوده میانه نوار ارزش منصفانه رسیده و ارزندگی خاصی نشان نمی دهد.  در چنین شرایطی بهترین راهبرد، انتظار برای یک اصلاح «عمیق» و سپس خرید است.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21577" target="_blank">📅 10:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21576">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks222SE789_xU_XRIRDv1fhgPPJzG7yuG1jlMAR4wYPUwGJVLoas0xZ_-GsmdsP8aHBHK-1nItghYL4SiYuk_85frn3t_kXE3JVygtOKGMFCLbkJBxwJZbxlLnBm8hWg0-i2yFXB9eNNOhLy4-Cbjrq2AGSboOo0zgdLHuIB2Eck2DEo_Iks_j0BOf8vXQ4rgRcw6wqCrWhSGNBa0tDqGu2Iy2ZcUHQPA4BlpttERZhsm01IGjEa0uup-EG7Ov5RpjV45fscjUUxV6nxd8BEerblXgXs9dAPKVLnymQbcvvSjDWSW0_tz-x85tQXQmOWJ0z6A3rgjapXHNPwnc_y5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC با رشد سنگین طلا به محدوده میانه نوار ارزش منصفانه رسیده و ارزندگی خاصی نشان نمی دهد.
در چنین شرایطی بهترین راهبرد، انتظار برای یک اصلاح «عمیق» و سپس خرید است.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21576" target="_blank">📅 10:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmBFC-bDn_OZpkbPw3InoF6JuVHI2tkphXPjejHBJDIlfFdnLP3QKktSicnqc-Rgt6ZrBlehZERSc9E2QMR1CxVq1bEzunyMqht44whHt7oYa0eqnpd9b91J3H_CYlgOQ5nOtWIHv8BrQb3crIPIA4Iodh0FdtGJy3OX66o5CGMVjHTy7cuD2i4-ROSOGyiNvxi1Av7-Gr3bDewaB55s0TrMa8mzlxhkXxnJ4mSp4DuUJalzLw1NzbrpmQNepojCLhqBDKE50CV-Duw-sWrd1xTJQXvKpOPl9FvU90kwIGAF9ed0rD1oylFL4ZaV_6B9aztIOz7pRSYj1WJrtpcBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی + تقویم اقتصادی برای امروز در سطح نسبتاً پایینی قرار دارد اما رشد سنگین طلا عملاً این مسئله را پیشخور کرده است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21575" target="_blank">📅 10:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21574" target="_blank">📅 10:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21573">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
کره شمالی هزاران نفر را با هویت‌های جعلی آمریکایی وارد شرکت‌های فناوری آمریکا می‌کند تا از راه دور کار کنند
این افراد با کمک هوش مصنوعی در مصاحبه‌ها و تهیه رزومه تقلب می‌کنند، گاهی هم‌زمان چند شغل دارند و بخش بزرگی از درآمدشان را به کره شمالی می‌فرستند.
این شبکه می‌تواند سالانه تا ۸۰۰ میلیون دلار درآمد داشته باشد و بخشی از پول آن به برنامه‌های تسلیحاتی کره شمالی می‌رسد.
علاوه بر درآمدزایی، دسترسی این افراد به سیستم‌ها و اطلاعات شرکت‌ها می‌تواند خطر امنیتی هم ایجاد کند.
﻿</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21573" target="_blank">📅 09:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21572">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پنتاگون طرح ۳ روزه حمله به ایران را تدوین کرده است
بر اساس گزارش نیویورک تایمز، ارتش ایالات متحده گزینه‌هایی برای یک کارزار کوتاه و شدید علیه ایران با مدت حدود ۳ روز آماده کرده است؛ این حملات به سمت مخازن پهپاد و موشک ایران، تأسیسات انرژی و سایر مراکز نظامی هدف قرار خواهند گرفت.
طبق این گزارش، تیم ترامپ قبلاً ۵ پیشنهاد برای عملیات‌های بزرگ علیه ایران یا حوثی‌ها ارائه کرده است. ترامپ اکنون پس از یک جلسه با مقامات ارشد امنیت ملی که توسط نایب رئیس‌جمهور ونس در کمپ دیوید رهبری شد، در حال بررسی پیشنهاد ششم است.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21572" target="_blank">📅 01:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21571">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: من هرگز ایران را برای بمباران لس‌آنجلس دعوت نکردم، رسانه‌های جعلی این را ساختند
او در تروث سوشال، «اخبار جعلی و مصنوعی» را متهم کرد که سعی دارند بگویند او «دشمن را برای بمباران سن دیگو» و لس‌آنجلس دعوت می‌کند. به گفته او، او فقط می‌گفت که پرداخت کمی بیشتر برای بنزین برای مدت کوتاهی، بهایی کوچک برای جلوگیری از دستیابی ایران به سلاح هسته‌ای است. او توضیح داد که قیمت بزرگ، بمباران سن دیگو یا لس‌آنجلس توسط ایران خواهد بود.
این چیزی است که او واقعاً در یک تجمع در نبراسکا در روز دوشنبه، در مقابل دوربین گفت:
«پرداختن آن قیمت کوچکی است. آن‌ها می‌توانند یک شهر را نابود کنند. بگذارید لس‌آنجلس را نابود کنند، بگذارید سن دیگو را نابود کنند.»
که پس از آن گفت: «قیمتی بسیار کوچک برای پرداختن.»</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21571" target="_blank">📅 01:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ستوان سوم وحید عنایت از نیروی انتظامی امروز توسط شبه نظامی‌های تکفیری در سیستان و بلوچستان به شهادت رسید</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21570" target="_blank">📅 22:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همان گفتاردرمانی همیشگی ترامپ است. به نظر من هیچ گفتگوی جدی در حال حاضر جریان ندارد و همانطور که خود ترامپ می گوید، فقط زمان حملات آنها شاید به تعویق بیفتد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21569" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:  ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم و تا پیش از برگزاری انتخابات میان‌دوره‌ای، به هیچ وجه به ایران حمله نخواهیم کرد؛!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21568" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDwimDBrwxA3ivjV_q1LBZp-S3ORoQ96_WzmRx9hdrL-mQ_Hq5xl3CsJ1l2Vj95n8g1EUli1BpjFIDHV0XIkW090t0ckaSb6jSzZ8m0DyRJFLu4eouTXxvL7xVXCIZPMFk2UzXtstH5U5SNE_2ZfMEUVqGMk38oI5nGKu61Uih7pmPJec7LX0RR2-oAEdUgW0G3bHyA3P8BIoLG4iwz2Bugr17UR8XTrtZAmHhhL-KbhdqMvwqX1-TRusC7QFxhoz2nM6-WoriRfmBjGn23rt84e7T8JaclHyQ5wPMm-dPJOdeOQoWrJtFSNDyVv8uIj5JqJd9g_P_L72DagD2pOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش کانال 14 اسرائیل، مقامات ارشد سپاه پاسداران انقلاب اسلامی خواستار حمله به اهداف مهم در منطقه طی 3 هفته آینده شده‌اند. آن‌ها معتقدند که ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21567" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خیلی شبیه هم بود این 2 خبر که ولی خب</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21566" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21565">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21565" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21564" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21563" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq4UcwNVb9_us4YrBnrYs_2eYvJ2xn0hsLEseimpF4ZEj2YPwelBiozsqXzhjGdomRvHJh_tUR373te4CmuhoN48GX0M2X101djHlAZxzM5I34_6omcifRutZg5vMq0Od4TtT6LlgBz9z2pqViBb8e_J6guxCsJ5RikLqVa62lGvezeqEBP_OE-PdIknJwiNCEIOGcx_TRXF_nHkZKmCU9SRSI_JjI_GpZLl0l5VBL9Na-biy1_p4XKzMd8eIisSwYsZngS4XhVoSpW59SslfXTHFRgLGW0sYpcXHNU6P6w2K05hKp4tnGaQ-wm64cD6G_L9XVhmw3vT50vTeLERZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21562" target="_blank">📅 19:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzNrG3ZbdqOhjPBbn8dWHvSY63twwDvTvBtRR9dFKDaAzmtf6GDZ7y3rk17U-yK5SSjeswX00ivhiB60XdUKXnhi7uhWIvRw6z94rxSRDcUGeMymOAR-t0z9mE2AN5y6WqmMN19eX72KuVrlhRaeqa_ZiYwIicKsTcnCXyrfn107aVXZTU3bxxMphZdhmfzjnu6Jlche5ceEr6_6e4tpPDFiEEdv67wzqa7GIRLrOzrCTZwNDbBKiz_rKdK6vh1gN-KLSNd0I24zHjGqqdLQ5r1BvjUR1I4_zRfryi3DUK6VxotcQNpnqRZP1vt3Ck9a_bLngx3bkiWTe03okAtW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21561" target="_blank">📅 19:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21560" target="_blank">📅 19:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHVbFlHVaF6SkRofvBAtlBlSNnF9fEXg694MPKODUioIdPogFrkzfgYpx59U4lkQQ27jxPdlEn9RqUWr8CRKRiyL2oRmoIG0edeTK2PYRYLcknI5bxLx8gp0wkCV_1Gn9y2oOVnYvJNFY39F_tIgWG4yMEjEQ_swqYCPhiyDE-csF_RRtisYC8IxgZ7EPbJDpPf7Tag89cnuiJl0AZHUT5pSWjxYv3Ch_lG7WFZ-3xS9rkVV-YRNb8CKRUJ6gMA82UJggpIHh2VN1YGQTC01vpRkZyH9mJ9CRgWqhcD7VcN_OHFICqJOS66-RyTA_TZWBWBf6kICPa3rwqxm09IV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21559" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بر اثر برخورد صاعقه به یک هواپیمای هندی، دماغه‌ی هواپیما آسیب دید.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21558" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLfPChS3mWDkv_Uq-EXzlP8SN7UQcYDwvutUuTQYs_K3l1sW9J1CIlmXaVF2d6e_P2cMHjZKMvCTBd41uSTW3ik_gGAYa8fsY4WIS8QLoottnMbuOrbOgSOUJfi4wg4xVp88n1rRCJGUI1R4Lbrdk3gmPMZclMhsng8h89JVydAnE95whwJ60HKiO6E15ecq-lRECA9nFNNy6Phe-xUysgG0SRBX8JIZy-Qg4Av_Do_q-iUg4drXSEQ48XWhPl3x2pClq5nBiR5aAVbZynXbqftRrEaVLhO4NHK6SzHpy9OzrS4s6P9fhxVEZ6qzz6fMk2T-QyyRK0z0xyOqUefcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21557" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21556" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21555" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWOrKiMNCw-5JyZlmujdGV71lNAgSSakAafaenb7qOHaGh-Z9ZHvLjWu3ZJW2701ELTCh3LVsJyrrmDs5nAzn4GhvGN8g_mo5J8v2r0H0VTTlRqf207pthHBhQozWWqPukwK0DDZVKvtypPAI_5PilT9zH_TPCXeE6IIoovAp3uGryzMfs7fmSejHwjVGIZ3tHeW9gfWs8zFSSq993YqBnmsTyGr_eibr_xikUv2zRzDyNRh2PNBzq2jVTRg5n8x6pKJU_2inWZnbXqa9SYyfBYTBTilh3Rbf6A0ciAlJUugRuAm60MVnbIzy2AIvQOUvNwZYfXiuENI3ivO6qivGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک هرمز؛ آیا جهان در آستانه یک بحران اقتصادی جدید قرار دارد؟!
شوک هرمز با افزایش قیمت نفت می‌تواند تورم جهانی را دوباره تشدید کرده و بانک‌های مرکزی را به حفظ یا افزایش نرخ بهره وادار کند.
تداوم نفت بالای ۱۰۰ دلار می‌تواند هم‌زمان با رشد ضعیف‌تر، سرمایه‌گذاری کمتر و هزینه استقراض بالاتر، ریسک رکود تورمی را افزایش دهد.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21554" target="_blank">📅 15:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر    در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21553" target="_blank">📅 13:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صحبت های یک استاد دانشگاه امام صادق درباره اینکه چرا فقط تنگه هرمز برای جمهوری اسلامی به عنوان ابزار فشار باقی مانده است</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21552" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21551" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر
در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21550" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oib8pOSuSnYM_-XIoIhbMGI-0D9vWo3kL1beT3OcAY2---ABPXR1Qx8cjf9DbB7a9P3YvOi2M6fGSLCD3K_pqPdGhPFlgthPICAVVmV-ULLmj0KJh39K8vSKosozKve7zA8fAGMFsoKl45-Lmr4l-whdecy0O8sB4jKLsM-N6R1MhAqySVbfwAaQVJsZ7PJN0pJVNWARwX--_j-68inm9Tqn9IgewXWAGUNJcHaSRJJRrjcW0v_8CcCE7pBjkzUTidudV05mXt4SWMyLV5GLaozTg5hj6Icz0hN9M8yw21FFwhMsieZHvE2NtHtk8TUqTagyPc2XG9kPlymMFzBrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21549" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSSQCAsscCAsVsSeta-iZ3G9LpwEmGeG7Mxs7E79_BqGmu-n18cyl70PYsHPUsdvUVkIO728H88B61bT9HuqzdzCLOQe6zJ2Ap4F2X85hnEVbd-fuxSpkhOESxrN0n831R_FfOMSr4vqY5jKWchypEMlfSM_--R9B5gO2tq3mEjY6GE5GFcxHjwNjALHSYLBuL6hgUmysLhIfbunxi-HCDxmAhZjjZFdIVPRW36R2bEh_4OSurYH3ON6lA3b9p8dz33bIt2y2QguMYvjQTY1HD48_OqMBXGc-leaAjN7ZrXJuZ2dGXbRs_0VQSCfVV2FrQXW2pL3Qc6ZGd6KMjkclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده بیش—فروش قرار دارد و خرید در حمایت ها منطقی ترین گزینه است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21548" target="_blank">📅 10:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c20wGSvIFrxtZycNmECr7bWmX84_Z4OTvUKgryyrUJmCU3v4QqjOMelMC7horzO3bWsCvse9E_7QAqTqyvjJ0A1IqtUQ8cp_-l5_CM_pwJwweZAwko6QjUmRSbwvPK_icCC6PKrZCUGHGMgaHBuCtmOVBb0c77j8IqVlS0OfqN7LXOvvbDPoOYwC2BA9lRq8SCYQGluNxBQ_QvrDGSh18mchPk6-1fj0rZAUbDAEX2N4JpNOp6cN9B_lCUFD3g0aX-1q60-gnWoyZ_Yt4UfWU7uexSbVxTeYu8BaD2vzuZzzA39xGXTJGWrUDEwCqxoxp4jSiETXC4TVzbQf6jdFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در حمایت ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21547" target="_blank">📅 10:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.
ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر رخ دهد.
یک تهاجم جدید می‌تواند شامل حملات گسترده ایالات متحده و اسرائیل به زیرساخت‌های انرژی و تأسیسات هسته‌ای ایران باشد که احتمالاً منجر به تلافی موشکی ایران و افزایش قیمت نفت خواهد شد.
مذاکرات هسته‌ای ایالات متحده و ایران همچنان متوقف است، در حالی که ترامپ و نتانیاهو، نخست‌وزیر اسرائیل، در روزهای اخیر دو بار تلفنی با یکدیگر گفتگو کرده‌اند.
مقامات اسرائیلی معتقدند احتمال حملات پس از انتخابات میان‌دوره‌ای بیشتر است، اگرچه حمله زودهنگام همچنان ممکن است.
— آکسیوس</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21546" target="_blank">📅 09:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران،  بقایی:
عمان با ایران بر روی مختصات جغرافیایی مسیرهای امن عبور از تنگه هرمز و نحوه ارائه این توافق به صورت بین‌المللی به توافق رسیدند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21545" target="_blank">📅 00:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ایران، حفر و توسعه را در یکی از بزرگترین پروژه‌های غیرفعال خود، مجتمع زیرزمینی آبیک که توسط سازمان‌های اطلاعاتی غربی و اسرائیلی با نام رمز "سایت 311" شناخته می‌شود، از سر گرفته است.
این سایت در امتداد محور تهران-قزوین، در حدود 100 کیلومتری تهران واقع شده است. این مجموعه در دل کوه‌ها حفر شده و شامل چندین ورودی تونل است که احتمالاً به یک شبکه گسترده زیرزمینی شامل ده‌ها سالن و پناهگاه متصل می‌شود؛ این مجموعه یکی از بزرگترین پروژه‌های از این نوع در ایران است.
تصاویر ماهواره‌ای نشان می‌دهند که این یک پروژه بزرگ است، با حجم زیادی از خاک و سنگ‌های حفر شده، زیرساخت‌های پشتیبانی و پوشش سنگی قابل توجهی که از تأسیسات داخل کوه محافظت می‌کند.
بیشتر کارهای حفاری در این سایت بین سال‌های 2007 و 2016 انجام شد. پس از آن، به دلایل نامعلومی، کارها عملاً متوقف شد.
با این حال، بلافاصله پس از عملیات "خشم حماسی"، تصاویر ماهواره‌ای نشان دادند که تغییری آشکار رخ داده است: ایران به این پروژه بازگشته و با سرعتی که در طول حدود یک دهه در این سایت مشاهده نشده بود، حفاری را از سر گرفته است.
این سایت در سال 2010 توجه بین‌المللی را به خود جلب کرد، زمانی که از آن به عنوان یک مرکز مخفی غنی‌سازی اورانیوم نام برده شد. این ادعا هرگز به طور مستقل تأیید نشد و هنوز هیچ مدرک قطعی و عمومی وجود ندارد که نشان دهد غنی‌سازی اورانیوم در این سایت انجام شده است. هدف دقیق آن هنوز نامشخص است.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21543" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21542" target="_blank">📅 23:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرمساق کاکولد با بهترین تجهیزات آمده نیروی دریایی فرسوده ما را غرق کرده حالا کری می خواند!
پدرسگ اگر شما هم کشتی های ما را نمی زدید خودشان داشتند یکی یکی غرق می شدند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21541" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21540">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیت هگست، وزیر جنگ:  ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.  نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21540" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21539">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.
نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21539" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21538">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">موسسه UKMTO:
گزارش یک حادثه در ۵۱ مایل دریایی شمال مدینه الشمال، قطر دریافت شده است.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21538" target="_blank">📅 23:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21537">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، ایتامار بن‌گویر:
ما خیلی نرم هستیم. این جدل من با نتانیاهو است.
اگر کسی در حالی که پسر من در ارتش خدمت می‌کند، به زندگی او تهدید کند، خانه‌ای که آن شخص از آن بیرون می‌آید را از بین ببرید.
و اگر دختری دارید که سرباز است، می‌خواهم او را محافظت کنم تا حتی یک تار موی سرش آسیب نبیند — بگذارید ۱۰۰۰ تروریست بمیرند.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21537" target="_blank">📅 22:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار با دلیل نامعلوم در حیفا اسراییل</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21536" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">— حزب‌الله ماه گذشته ۲۰۰ میلیون دلار از ایران دریافت کرد تا به مردم لبنان که به دلیل جنگ امسال با اسرائیل آواره شده‌اند، کمک کند، با وجود افزایش فشارهای اقتصادی ایالات متحده بر ایران و دشواری‌های فزاینده در انتقال وجوه به این گروه.
واسطه‌هایی که پول را جابه‌جا کردند، کارمزد ۲۰ درصدی دریافت کردند که چهار برابر نرخ معمول است و این امر بازتاب‌دهنده خطرات مرتبط با مدیریت وجوه برای حزب‌الله است.
— رويترز</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21535" target="_blank">📅 19:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به نظرم وقتش رسیده که یک بار دیگر بکشیمش.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21534" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مقام ارشد ایرانی: ایران هرگز حق غنی‌سازی خود را رها نخواهد کرد، اما جزئیات غنی‌سازی می‌تواند بعداً مورد بحث قرار گیرد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21533" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
‏حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21532" target="_blank">📅 14:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو درباره ایران:
کشورها، حتی آن‌هایی که به ما حمله می‌کنند، به‌صورت پنهانی و پنهانی می‌گویند: «(حکومت ایران) باید سقوط کند. آن‌ها همه ما را خفه کرده‌اند.»
ما اطمینان حاصل خواهیم کرد که آنها سقوط کنند. آن‌ها سقوط خواهند کرد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21531" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21530" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0EA--jRfjrYjYzpabWjpeQ-wFkn2LNlWmGi1T_ZqwkxSYKRa8vx94cDvf-YS8CYeeA6LHpkGNl96MqZIRX0WE8_UVrzHuPMlWnwOJG1-qb1YgdY_RikNO8uk1GZgAmsv8s6sOeHw0ZTV2UoGEvNasoAaPdRnna0gXIqysvwYPh77EER3xBNevQ_z7TxBwRFzqIJcpZKCkkpe9_SxtWD3Dnk_xnvsXBOjQDSqMZaRuVpS6kiyHj6zpyxSBQM-hs1PoEaAHbVLbgEp0k0MkBwRHbT-agmSqmGj36yxuYhY-7lqI9HXUcOHuMC4Fk8YdpODK84a7R0DiWEl-2k4QnNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21529" target="_blank">📅 12:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3164ghAtOQrk5Axq2_f-CnP-qI-LOR7xczkTsoF1lRxPQnh1VPRXV8JzbQ8dI_xluAdjFhMwtYbM6VJpzyPD1ZGatNUGS6E4aymJI6eE6KdFQE9GO_PZaemwVYukSUYqrAnv_H_Bo11p0QsfBtED6MwUKduoimKIOn8SUgdBgoDcxoA_uEzWL1lEca2MJW7DzGkCEawGS4nYNFVadtCbaXNv_2Sv4rUiTCNsZ-ZskkiaK1bPurCmPxcJHv46VwDrfGeHLTCDguBBGac0fGFd96KeTauE-vCmPOEhQAsTTBZMMzUSXTNOO6i1yQJ_b9f3yfvE19t7rF9dRzbWiCGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21528" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHng_XT3MvO3hkepcCsfEcqBo3oWBseJpugkPHmZM3WUk8ekV5fkbhpxPNIkfjVRipyzai-uH1HRKVYhM--jLa6CP-_RjlE9pxxg9zWyLUW7azNcUd8mmo-IaLcrJltdPtNoeRUFe9T8o5LTyA_cq4O38ax_KzQY6-CUpr131ug6VNup1bGydmTMYFByECTMft59HNygDG13WP_FwvvI7K5N4XwFvgCbhx1PusIlr30yFSSp2FIIINzf4qeRHvsTyDj52ulNSWvbsx4u3wOI7EgtSEwXMKtB9WKPHyYaSOrXBHj4hNAuxxxXx0BsnBY36Oop0UShibRLUXT-fEg3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC به محدوده بیش—فروش نزدیک تر شده و این موضوع خرید را قوی تر می کند.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21527" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kuc9XqaVWLGoRFoahCmfiOfY3B28dx_hy0yjJx-YKsgAxJ8jWAGqHqlsTFxpoPO0rci4cNTrIp_71QgHzOzlHSrDnqEKkCzaUL4rrk-Sf5PL57kC2FixEQeYCgttqgkM-c7SCXLHL2Adbf10suikScrC8uOGxoKsblI3VIrcRn4_qrAy04KJHx3DAt0uJUkch9-SRzhX16Z4V9-_X9QfCcOTkf-pLPM6TbaF4-m7j6PQsZD2ewXqcxacy0yHnmdVQBA8jn_ELsaXSqbsS4BtShpkWki_IFouxRlQdbQZrPdiR1AGAYzNVIOaE0cwjH40QTu_mcNLMq-yWhXBpAKa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش طلا تا این لحظه، خرید توصیه می شود.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21526" target="_blank">📅 12:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxPY1Wm8bFVQvczoVswhPUvSoe8lv5QlOdYlYNiVEKVguUD96EJzdp0u7an6nPfx0uoq3qN6ThGAy621obAd8M4cHLW_V8arZJ5wdQv6ki3pPOqhlpnWg3jeo-7s2hyBd-FOszBemkPdlke-UcV4Tu10lSJHjLohFsOLWAi-jGPMk4RJ1dxLCCG9uD_cTqLDKDP3O6UMzhaDGOdZmKUEnyo5G9iL6IPtyAMwcOJ87QuEp_vFPXpwUQEhsNOrO0X2faIuSoshvLkBNYGCByp64r5DhBIN8fnQVwWHK6ldsnH04WZh1w-EWHAXPjV9ol8mK3ZzejZTKhITKuV_RXlV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21525" target="_blank">📅 11:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ذخایر طلای چین در پایان سپتامبر ۷۷.۴۷ میلیون اونس خالص بود، در حالی که در پایان اوت ۷۶.۷۳ میلیون اونس بود
اما ارزش این ذخایر طلای چین در پایان سپتامبر ۳۲۳.۵۲ میلیارد دلار در مقابل ۳۵۰.۰۸ میلیارد دلار در پایان اوت بود</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21524" target="_blank">📅 09:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تعز به تصرف حوثی ها درآمد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21523" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
اسکات بسنت :
ایران وزیر نفت جدیدی انتخاب کرده،
با توجه به اینکه آنها از 25 آگوست حتی یک بشکه نفت هم برای صادرات بارگیری نکرده اند، این وزیر جدید عملاً چه چیزی را مدیریت می کند؟!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21522" target="_blank">📅 08:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz_RcMp8nOZpKYgo0mWxFsUwNiCkml284zqYf3JtUpXROXY89fXEGDACqaaShSQcgdBQvpBohdcTZpQUeAtuLJ3BXOvZqinTurJZQ7pCa_Wxk9Nk27KVbTUKC5cBcqJ7dH9RkN2b6PTZ1ZJ1A5K6VFXnb6RWFckAD45jdP0qViS2OMncSC5wm4jpBarVa26lmKPY5PU5P09qSn1LfWNoGm0bksO73GMUbVx5NsPJTcgUAmTRQnrj9KMpI8QHxBRTuerHkSaRcQf_PPKPyuBOicKl2XFUvMznKcaWltww98OEAGLJyqbwy43ZEO-C3OnZYJgGt4qAONVlyuz9tJ6i8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خب بعد از اینکه به بسنت این را فهماندیم، دلار 40 هزار تومان کشید بالا که مهم نیست چون مهم این است که ما مجبور نشویم بکشیم پایین.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21521" target="_blank">📅 08:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21520" target="_blank">📅 07:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این مدلی بوده که اردوغان تروریست های جهادی ترکمن سوریه را که تحت فرماندهی «تیپ سلطان سلیمان شاه» قرار داشته اند به جبهه های جنگ قراباغ اعزام کرده است.  پس از ورود نیروهای سوری به جمهوری آذربایجان، در جلساتی با حضور رهبر تروریست های سوری و نیروهای نظامی ترکیه…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21519" target="_blank">📅 07:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آماده‌سازی‌ها برای جنگ میان اسرائیل و ترک‌ها با شدت تمام در جریان است Damir Nazarov  پس از به‌رسمیت‌شناختن سومالی‌لند از سوی اسرائیل، تحلیلگران این اقدام را تلاش نتانیاهو برای ایجاد پایگاهی در برابر انصارالله یمن و کسب اهرم فشار در دریای سرخ ارزیابی کردند.…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21518" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خیلی حرف های بد دیگری هم زده که اینجا نمی گذارم.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21517" target="_blank">📅 00:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دونالد ترامپ:  تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21516" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دونالد ترامپ:
تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21515" target="_blank">📅 00:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کاخ کرملین: رئیس‌جمهور ایران روز جمعه در اجلاس سران کشورهای سابق شوروی که به میزبانی روسیه در ترکمنستان برگزار می‌شود، شرکت خواهد کرد و با پوتین دیدار خواهد داشت.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21513" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21512" target="_blank">📅 19:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:
آنچه در فرانسه در حال وقوع است، چیزی جز مهاجرت گسترده و بی‌رویه نیست. این موضوع نه مربوط به مدارس است، بلکه مربوط به اسلام است که قصد دارد بر کشوری که قبلاً عالی بود مسلط شود! (رئیس‌جمهور دونالد ترامپ)</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21511" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فیلم وزارت اطلاعات از ضربات به گروه های تکفیری در سیستان و بلوچستان!
قشنگ خاطرات بازی Counter Strike زنده می شود.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21510" target="_blank">📅 18:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دبیرکل حزب‌الله:   آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21509" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دبیرکل حزب‌الله:
آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21508" target="_blank">📅 18:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21507" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SBoxxx/21506" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های عبری‌زبان در تاریخ ۵ اکتبر، اسرائیل در حال تدارک برای اقدام نظامی احتمالی جدید علیه ایران است؛ اقدامی که ممکن است به‌صورت مشترک با ایالات متحده یا به‌طور مستقل انجام شود.
روزنامه «اسرائیل هیوم» گزارش داد که ارتش اسرائیل ضمن حفظ همکاری‌های نزدیک اطلاعاتی و عملیاتی با ارتش آمریکا، خود را برای حمله احتمالی به جمهوری اسلامی آماده می‌کند. این تدارکات شامل سناریوهایی است که در آن‌ها اسرائیل یا دست به حمله پیش‌دستانه می‌زند و یا به حمله ایران پاسخ می‌دهد.
این گزارش احتمال وقوع حمله اسرائیل یا آمریکا پیش از انتخابات میان‌دوره‌ای ماه نوامبر را نسبتاً پایین ارزیابی کرده و حاکی از آن است که این آمادگی‌های نظامی برای رویارویی احتمالی در زمانی دیگر صورت می‌گیرد.
هم‌زمان، وب‌سایت «والا» گزارش داد که واشنگتن در حال آماده‌سازی برای اعزام نیروها و هواپیماهای بیشتر به اسرائیل در هفته‌های پیش رو است؛ این در حالی است که هم‌اکنون حدود ۳۰۰۰ نیروی نظامی آمریکایی در این کشور مستقر هستند.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/21505" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فوری - قطر اعلام کرد که ایالات متحده و ایران همچنان در حال مذاکرات برای پایان دادن به جنگ هستند</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21504" target="_blank">📅 15:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترکیه و پاکستان برای حمایت از عربستان سعودی در برابر یمن، توافق‌نامه مکه را فعال کردند
آنکارا و اسلام‌آباد متعهد شدند که به‌سرعت نیروهایی را به داخل خاک این پادشاهی اعزام کنند.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21503" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21502" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خلبان آن هواپیمای فلای دوبی هم که داشت سقوط می‌کرد هندی بود!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21501" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت امور خارجه هند:
۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21500" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21499" target="_blank">📅 14:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نشست کارشناسی بسیار جالب و دیدنی درباره روند جنگ ایران—عراق و فرصت هایی که برای پایان جنگ وجود داشته است:
https://www.aparat.com/v/goil745?playlist=27887251</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21498" target="_blank">📅 14:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انصارالله ادعا می‌کند که در دو روز گذشته حمله دوم به فرودگاه سعودی را انجام داده است
انصارالله اعلام کرد که با یک موشک بالستیک به فرودگاه بین‌المللی ابها در استان عسیر عربستان سعودی حمله کرده و ادعا می‌کند که این ضربه باعث اختلال در ترافیک هوایی فرودگاه شده است.
یحیی سریع، سخنگوی نظامی انصارالله، گفت که ضربه موشکی «دقیق و مستقیم» بود و به شرکت‌های هواپیمایی بین‌المللی هشدار داد که از ادامه پروازها از طریق فضای هوایی سعودی خودداری کنند، زیرا به گفته او این فضا به «صحنه عملیات نظامی ما» تبدیل شده است. ریاض تاکنون به‌طور فوری این حمله را تأیید نکرده است.
این حمله پس از حملاتی رخ داده که انصارالله در شب دوشنبه به فرودگاه‌های جازان و نجران نسبت داده بود و پس از آن حملات، مصدومیت‌ها و خساراتی گزارش شده بود.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21497" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فرانسه برای اولین بار موشک بالستیک جدید خود با قابلیت حمل سلاح هسته‌ای را از یک زیردریایی هسته‌ای آزمایش کرد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21496" target="_blank">📅 13:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCSVI6d3DzCLtyoUfFP-3cmlr-uUCw-Hi7YHQbc6YBv0UgwxB6iL0_K-bIufaPLckCrN2y_5U3AX2Z-ivnUDixEjeoMfx5-MdmFL7femr6ekRn-Owcy5nrfunF4ZpVhC2FTae0mwFXMsEwLuk74jTYyOwuEovNv0MKENB2qX0AXTImelJUfYPGPJHnLngEEDrETHsb5ibjrcywEGTB_VVMWCj5-hd2QO1sjwRmoV-lrRPARAjDNTyBZedV4AwfQMsZVjAZk2vtb3CxgbyfTLLW_xzkOJKDCm7u4ZeGECbRqsAZ8OUfXYZicn25WNH39aL7Bx3wSAclWx6ggRoADsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر وقت یک نفر که ذهنش اسیر تفکر فرقه ای نشده  فهمید که میان توران بزرگ با اسرائیل بزرگ کدام بیشتر به زیان ماست و آن را بدون هراس بر زبان آورد آن وقت می توان امیدوار بود که پویه های ژئوپولیتیک بر محاسبات کلان سیاست خارجی کشور حاکم بشود و نه انگاره های وهمی…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21495" target="_blank">📅 11:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">موسسه مطالعات جنگ درباره کوشش ایران برای بهبود و ارتقای توان موشکی خود:
ایران به احتمال زیاد در حال بازسازی و ارتقای توان خود برای هدف‌گیری اهداف نظامی دوربرد آمریکا در منطقه و کشتیرانی تجاری از طریق بهبود دقت، برد، سرعت و قابلیت‌های هدف‌گیری موشکی است. سخنگوی ارتش ایران، سرتیپ محمد اکرمی‌نیا، در مصاحبه‌ای با رسانه‌های ایرانی در ۴ اکتبر اظهار داشت که ایران در حال بهبود دقت، برد و سرعت همه موشک‌های خود است. اکرمی‌نیا افزود که ارتش باید برد موشک‌ها را افزایش دهد تا نیروهای آمریکایی در منطقه را هدف قرار دهد و اذعان کرد که نیروهای آمریکایی تا ۱,۰۰۰ کیلومتر دورتر از ایران جابه‌جا شده‌اند.
مقام‌های آمریکایی در ژوئیه ارزیابی کرده بودند که ایران نسخه‌های پیشرفته موشک بالستیک میان‌برد خیبرشکن را علیه پایگاه‌های آمریکا مستقر کرده است. این مقام‌های آمریکایی اشاره کردند که ایران این موشک‌ها را برای گریز از دفاع‌های آمریکایی از طریق مسیرهای پروازی متنوع، سرعت‌های متفاوت و مانورهای فاز پایانی، و از قابلیت پرتاب متحرک موشک برای ارتقای بقای پذیری و اثربخشی موشک تغییر داده است. ایران همچنین در آخرین حمله خود به نیروهای آمریکایی در اردن در ۹ سپتامبر موشک‌هایی با کلاهک‌های مهمات خوشه‌ای شلیک کرد. مهمات خوشه‌ای در ناحیه‌ای وسیع پخش می‌شوند و برای بیشینه‌سازی گستره خسارت طراحی شده‌اند، هرچند اثر هر گلوله‌ به‌صورت فردی را کاهش می‌دهند. ایران در حملات قبلی علیه اسرائیل از مهمات خوشه‌ای استفاده کرده است که عمدتاً برای جبران کمبود دقت در حملات موشکی بالستیک ایران انجام شده است.
اظهارات اکرمی‌نیا همچنین در پی اعلام ۲۱ سپتامبر دبیر شورای عالی امنیت ملی ایران، سپهبد محسن رضایی، مبنی بر اینکه ایران اخیراً یک موشک جدید با کلاهک مهمات خوشه‌ای را در حمله‌ای به ناو یو‌اس‌اس جورج واشینگتن آزموده و این سلاح در نزدیکی ناو هواپیمابر اصابت کرده است، مطرح شده است. گلوله‌های خوشه‌ای تقریباً به‌یقین نمی‌توانند یک ابرناو را غرق کنند، اما می‌توانند عرشه را آسیب بزنند و به این ترتیب عملیات پروازی را تا حدی و برای مدتی مختل کنند. رضایی احتمالاً به حمله ایران به ناو هواپیمابر آمریکا در ۹ سپتامبر اشاره می‌کرد. رسانه‌های ایرانی در آن زمان گزارش دادند که ایران از موشک بالستیک میان‌برد قاسم بصیر استفاده کرد که برد ۱,۲۰۰ کیلومتری دارد و کلاهک بازگشت قابل‌مانور آن برای گریز از پدافند هوایی طراحی شده است. اشخاص مطلع، 3 حمله موشکی بالستیک ایران به کشتی‌های جنگی نیروی دریایی آمریکا در اوایل سپتامبر را در گفتگو با وال‌استریت ژورنال در ۹ سپتامبر «خیلی نزدیک‌تر از حد انتظار» توصیف کردند.
ایران ممکن است این اصلاحات موشکی را بر حملات موشکی خود به کشتیرانی در تنگه هرمز اعمال کند. ایران از ۲۹ سپتامبر حملات تقریباً روزانه‌ای به کشتی‌های در حال عبور از تنگه انجام داده است. یک مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایران توان خود را برای هدف‌گیری کشتی‌ها بهبود داده و خطر برای کشتیرانی در تنگه را در هفته‌های اخیر افزایش داده است. ایران ممکن است از شرکای خود برای بهبود قابلیت‌های هدف‌گیری خود پشتیبانی دریافت کند، چراکه به‌گزارش‌ها روسیه اطلاعات هدف‌گیری ارائه کرده و جمهوری خلق چین تصاویر ماهواره‌ای به ایران داده است که احتمالاً به هدف‌گیری ایران در طول این درگیری کمک کرده است.
ایران به احتمال زیاد با اولویت‌دادن به بهبود قابلیت‌های موشکی خود، در پی افزایش توان بازدارندگی خود در برابر حملات هوایی آمریکا به دارایی‌های ایرانی، تحمیل هزینه به ایالات متحده و حفظ ابتکار عمل راهبردی در این درگیری است. همان مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایالات متحده کارزار خود علیه نفت‌کش‌های ایرانی را در واکنش به حملات ایران به کشتیرانی تجاری، پس از حمله ایران به پایگاه هوایی آمریکا در اردن متوقف کرده است. این مقام احتمالاً به حمله موشکی مهمات خوشه‌ای ایران به پایگاه هوایی موفق السلطی در اردن در ۹ سپتامبر اشاره می‌کند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21494" target="_blank">📅 11:12 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
