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
<img src="https://cdn4.telesco.pe/file/QiFnG7BvGrrczFglE4ZkmaSLhGM3yODwT0iRSN8yYHq9hw4dPMMj03AT24m5rw1AV4bS5tiQX-y0d7TqYT3Dv4wmHLul3L-4Wsfbc2uuOsM92ErUUGqdwXsfbkcy2xIP7GPyvSz6gZk286tYVsRDvIuUgvVo--t9t6cz2HeiSbQQmWQHMYr8eGs8qC-4E3l-ALOTdD_PrPveK1SfyPOGpFqpsQ3XpFOxdObUlSMQ3MJDvdgd0Nv0iFsWseRQsxqACF8UwPOphdRKVJql_L34bl-APoS_ev0as6ONPx38HGAP7uxDBc-zg-9EAbVLZKnfOYFmIfiVzm1iuM1kW1IVvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/SBoxxx/20836" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد
رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.
مسعود پزشکیان گفت: «کشورهایی که خاکشان از سوی آمریکا برای حمله به ما استفاده شد نیز در این نشست حاضر خواهند بود.»</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/20835" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20834">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBjYbk47i1Iop4kyI8bOT3tCOyARTTl1l4nk9thFQEdPd8eI-O2ADM6mB7yAlsIJlP1EWcSG-AQr6VrsbZ2AbQrphEtgCmM-tuOodkG3SYpBjb4akoo0GODFP_l5KCrtIZkqWHclGoF1OYFpwBEbGeXrbHczDyaQzHAsdNxCaI7soxUzTVr9W6AdcbH75u0-DFePDl9ucTb6r97fsrHBdLXaITWrxRdaxJCbrNb_2_ylPq9kOeh7X2zpPz1SqMKznr2LpnVmo3XFT630P0TFqSSDYDW1u1OBfa-bxCI9GbO_yLoxwoXEPpWEVCRWGlV343x2T0D64z0-Ec98IWmzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی ان ان:
اوکراین در نبرد با روسیه، فراتر از اروپا، تیم‌های کوچک متخصص پهپاد را به آفریقا و خاورمیانه اعزام می‌کند تا نیروهای محلی را آموزش دهند، از گروه‌های ضد روس حمایت کنند و به منافع روسیه حمله کنند
حدود ۱۵ متخصص اوکراینی در شمال مالی در کنار جبهه آزادی‌بخش آزاواد (FLA) که توسط توآرگ‌ها رهبری می‌شود، فعالیت می‌کنند و به جای درگیری مستقیم در خط مقدم، آموزش پهپاد، اطلاعات و پشتیبانی عملیاتی از راه دور ارائه می‌دهند.
نیروهای اوکراینی همچنین نیروهای چاد، نیجر و بورکینافاسو را آموزش داده‌اند، در حالی که چندین متخصص در سودان نیز عملیات کرده‌اند.
سازمان اطلاعات اوکراین می‌گوید این اعزام‌ها با هدف فشار آوردن به روسیه در خارج از کشور و تبدیل تخصص اوکراین در پهپادها به یک «ابزار سیاست خارجی» انجام شده است.
نیروهای اوکراینی در سال جاری میلادی، هنگام تصرف کیدال توسط شورشیان توآرگ، به آن‌ها کمک کردند؛ جایی که نیروهای شورشی و وابسته به القاعده، نیروهای سپاه آفریقای روسیه را به عقب‌نشینی واداشتند.
نیروهای اوکراینی همکاری خود با توآرگ‌ها را عملیاتی و نه ایدئولوژیک توصیف کردند و یک منبع اطلاعاتی گفت: «وقتی توسط همان احمق‌ها مورد حمله قرار می‌گیرید، تفاوت‌های ایدئولوژیک در پس‌زمینه محو می‌شوند.»
اوکراین همچنین از اواخر سال ۲۰۲۵، اپراتورهای پهپادهای دریایی را در شمال غربی لیبی مستقر نگه داشته است. یک اپراتور گفت که یگان او از پایگاه نظامی بین‌المللی در مصراته برای انجام حملات علیه «ناوگان سایه» روسیه که از تحریم‌ها فرار می‌کند استفاده می‌کند و در عین حال نیروهای محلی را آموزش می‌دهد. یک پهپاد دریایی انفجاری اوکراینی از دست اپراتورهایش خارج شد و در سال جاری میلادی به سمت یونان هدایت شد که باعث اعتراض آتن و عذرخواهی کییف شد.
اوکراین همچنین تیم‌هایی را به حداقل ۵ کشور خاورمیانه اعزام کرد تا در طول جنگ، آموزش سرنگون کردن پهپادهای شاهد ایرانی را ارائه دهند.
مسئولان اوکراین مأموریت‌های خارجی را هم به عنوان راهی برای تضعیف روسیه در هر جایی که فعالیت می‌کند و هم به عنوان فرصتی برای آزمایش فناوری پهپاد اوکراین در شرایط میدان نبرد مختلف، از گرمای شدید و گرد و غبار ساحل در آفریقا تا عملیات دریایی در مدیترانه، معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SBoxxx/20834" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiBDu36mk8gOWNY7ZPxqoMQJHjidYoY-NgFSZI4Ao1tiHnC6p_unsua_l1HTb-VyUzviKNB5glDxTJOg-bdE9GZJjtXSOqOEpSS-mdKfVG8pcSYvLHUR_rajlzh1-ZPBP6qNL6FEQ0Ems5YS3QXP0_AIL2f90iFw_HZ_jN5M41yTliA30rtwx5Q8ifErABQMelVz8KvAsfgeFmLoCK5CgxTHn7_yph-visCoWv99y2nfXluRZWE7WtQsQHQ_ars5-8gcnOCqqTi4z9y_04tHsvIv5k4Fi2TYl6TIqQhyy1Y00-pbVNlFJx7RHfywhjMKhVxQ-8zcQH-nC_eim-KMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/20833" target="_blank">📅 19:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/20832" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مدتی است به صورت آشکار و بی پرده، صحبت از لزوم ساخت سلاح هسته ای ایران از سوی مقامات کلان جمهوری اسلامی مطرح می‌شود</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20831" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:   حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.   ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20830" target="_blank">📅 13:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:
حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.
ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند و فقط با یک کشور (عربستان سعودی) مشکل دارند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20829" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20828">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20828" target="_blank">📅 13:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=lPvO6eZnUD10zE5NAx9o50GCEtOv_ETGa73REClSxdL8S6MW_Beg6N2Lvf3ZLLwirL_zaMbs347nMw9uBRHkaS0vJVe_OLgt5Rm0wOBKY0XJPwY5j4K5sJUkXcr_PgPLRKs96HT4TNLiOozO42502j8LPPJj1n19pjjosTLMwqvcvlLB1e4i2MfQHITkFBGyaqJOgs4vrGjNBYOpuW4Oag23yA8vROxp6876__dZIcoOH5otC_6Mm3MnFmLFaFkSwd42OFZjlGCemBY3WJnJd4ejJUrNtCsNFQD2e2Pkaj06CfrUNhCYZ4-6m5SclwbQ7Vu5ewL2udgtY39UBE2WiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=lPvO6eZnUD10zE5NAx9o50GCEtOv_ETGa73REClSxdL8S6MW_Beg6N2Lvf3ZLLwirL_zaMbs347nMw9uBRHkaS0vJVe_OLgt5Rm0wOBKY0XJPwY5j4K5sJUkXcr_PgPLRKs96HT4TNLiOozO42502j8LPPJj1n19pjjosTLMwqvcvlLB1e4i2MfQHITkFBGyaqJOgs4vrGjNBYOpuW4Oag23yA8vROxp6876__dZIcoOH5otC_6Mm3MnFmLFaFkSwd42OFZjlGCemBY3WJnJd4ejJUrNtCsNFQD2e2Pkaj06CfrUNhCYZ4-6m5SclwbQ7Vu5ewL2udgtY39UBE2WiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلی دیدنی از پتانسیل صعودی شدید ریال</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20827" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ درباره ایران:   قیمت‌های نفت پس از پایان درگیری سقوط خواهند کرد</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/20826" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20825">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ درباره ایران:   همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/20825" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20824">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ درباره ایران:
همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20824" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده در آستانه گسترش تحریم‌های ثانویه علیه ایران
بر اساس اطلاعاتی که یک منبع آگاه از برنامه‌ها به
رویترز
گفت، انتظار می‌رود وزارت خزانه‌داری ایالات متحده دامنه تحریم‌های ثانویه‌ای که می‌تواند بر شرکت‌ها و کشورهایی که همچنان با ایران تجارت می‌کنند، اعمال کند را گسترش دهد
این منبع گفت که این اقدام به عنوان یک هشدار نهایی به کشورها برای قطع روابط تجاری با ایران انجام می‌شود
انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری ایالات متحده، جزئیات بیشتری از این تدابیر را در یک نشست خبری در ساعت ۱۳:۰۰ به وقت شرقی ایالات متحده (۱۷:۰۰ به وقت گرینویچ) روز دوشنبه اعلام کند.
طبق گفته منبع، بسنت همچنین یک کمپین فشار اقتصادی گسترده‌تر علیه ایران را ترسیم خواهد کرد که او و دونالد ترامپ، رئیس‌جمهور ایالات متحده، آن را «روز D اقتصادی» نامیده‌اند.
این منبع گفت که انتظار می‌رود بسنت روشن کند که کشورها باید بین همسویی با ایالات متحده یا ریسک قطع دسترسی شرکت‌ها و نهادهای بزرگ از سیستم مالی مبتنی بر دلار، انتخاب کنند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20823" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20822" target="_blank">📅 11:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مرزهای بازرگان و بصره بسته شدند.
مرز بصره جوری بسته شده که تیم تاج برای سفر به بصره جهت میزبانی بازی های آسیایی (سبحان الله چرا بازی پرافتخارترین تیم ابرقدرت چهارم جهان باید در بصره باشد اصلا؟!) به مشکل خورده!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20821" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8ER6fjVLBUMp2kdtBfHz5dSAtU_Vk2dZgssvmKm2Qoqe1bXKUotmMciaM28SFQAdpg4lMcc1_iDSHG9Wi5-u6MhzzUBHiX09HJAcVFqA1dPqcSVhAD-Ku8h6jSKYFVQc7OPxYdtUXdji8-vy4w3Dwzt9zm3qWFCnO0cBNn-rv_nUk3yaj55w29pCMRh5RrAtz9dMk23Gv8-OJe_N9RM3Mm7ag9I6VmfRtnbExM_0H2qSG3LWWQA1URGrQIH6TtWMyVdYypIZ_9mK_TOmzp2gfswh3B7Ybc77Me_bYbJvfgheIbfAnQ6MsMeoSt-HF0qMT_pXsfXhmMM4HkD42v4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…
توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20820" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">— یک مقام اسرائیلی به کانال ۱۲ گفت که کنترل حوثی‌ها بر تنگه باب‌المندب «خطرناک‌تر» از وضعیت فعلی در تنگه هرمز است و به جغرافیای این آبراه اشاره کرد.
کانال شرقی حمل‌ونقل دریایی در نزدیکی جزیره پریم تنها حدود ۳ کیلومتر عرض دارد، به این معنی که کشتی‌ها در محدوده دید مستقیم از مواضع حوثی‌ها عبور خواهند کرد.
«آن‌ها قادر خواهند بود با موشک‌های ضدتانک به هر چیزی که بخواهند شلیک کنند. آن‌ها می‌توانند کشتی‌ها را با چشم خود ببینند. این همان تفاوت است.
در هرمز، ایران به رادار، سیستم‌های نظارتی و موشک‌های ضدکشتی نیاز دارد تا ترافیک دریایی را تهدید کند. اما در باب‌المندب، یک جنگجو با یک موشک ضدتانک ساده در جزیره میون می‌تواند به یک کشتی تانکر شلیک کند که می‌تواند آن را به صورت فیزیکی ببیند،»</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20819" target="_blank">📅 07:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— دادستان‌های فدرال آلمان هفت مظنون عضو حماس را متهم کرده‌اند.
به گزارش‌ها، اینها در حال برنامه‌ریزی برای انجام یک حمله مرگبار علیه اهداف اسرائیلی یا یهودی در آلمان یا اتریش بودند.
این توطئه تا ژوئیه ۲۰۲۵ به مرحله عملی رسید و قرار بود در دومین سالگرد حملات حماس به اسرائیل در ۷ اکتبر ۲۰۲۳ انجام شود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20818" target="_blank">📅 07:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران
به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.
در این حمله ۳ نظامی آمریکایی کشته و چند نفر زخمی شدند.
آمریکا نام شرکت‌های چینی را اعلام نکرده و چین را مستقیماً به مشارکت در حمله متهم نکرده است. پکن نیز این ادعاها را رد کرده و خواستار ارائه مدارک شده است.
نگرانی اصلی واشنگتن این است که ایران از تصاویر ماهواره‌ای چین برای شناسایی و ردیابی نیروها و شناورهای آمریکایی نیز استفاده کند.
اگر این ادعا درست باشد، همکاری ایران و چین وارد مرحله مهم‌تری شده است: انتقال اطلاعات ماهواره‌ای می‌تواند دقت هدف‌گیری موشک‌ها و پهپادهای ایران را افزایش دهد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20817" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار در استان خمیس مشیط عربستان سعودی</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20816" target="_blank">📅 00:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/20815" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS4QtqTEoRaGpofpj4K9YmVypqb9pNo5BOKFryV0yBf7G229z1dae8OadX9D3zPiqHbEHSNYhIxGbf5rVNKoexuRHMoDanopq2CXNOHa6DHfm0eUCyW1y4ijnyepuiEjpFKZEADOVOFvo6guX_QKJm47hSQQ1y_vqErrfBdWFB4Rhh0NbNQfnXP6RVIXkMv9pzRgFrM_xQSW7NjmBNcdJhWQUvmQ4omCl07oeaQEi5t2exyhDTn1hbcI1eStYTSOYR5O0gcwBRkJx5JagHBIkWGBxtIoChlzmJVuw9AVSjZ86hj6lTgU3zGCUsjQY7mnir2doqURat-iRADkWr-Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20814" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">— ۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران ایران یک موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20813" target="_blank">📅 20:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=F3nhTdTjCDrk2UB2ug-9rL5DYSkwMgh_H6E7fzXSlsVX6a_9okHXh050lTFoNsjX26WZCgzcV7ZE0B10gZOf-vum5nZBjo9JePaC9ikPrMQTaRMP3RffCcr4OvxqGZSZre-yPo57krr4wzud4qEJ5kAcKu_mT-FzXNgjQDCVXoZvJwgOeQnJi141pnSezbtdMGSSKBe3n6ks8okEbZ21oDIBHEADJa8bW1zynU1q3mRWWWXMrw8H7ufSc0KKGWeGhc91ymiVIxChDErr86tgyNoiyCK0yNLeE5QfSvpMntYmL1whOuKnJ6aPJZJGLh1_Lm_DgAsIftdoN5xdwYrOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=F3nhTdTjCDrk2UB2ug-9rL5DYSkwMgh_H6E7fzXSlsVX6a_9okHXh050lTFoNsjX26WZCgzcV7ZE0B10gZOf-vum5nZBjo9JePaC9ikPrMQTaRMP3RffCcr4OvxqGZSZre-yPo57krr4wzud4qEJ5kAcKu_mT-FzXNgjQDCVXoZvJwgOeQnJi141pnSezbtdMGSSKBe3n6ks8okEbZ21oDIBHEADJa8bW1zynU1q3mRWWWXMrw8H7ufSc0KKGWeGhc91ymiVIxChDErr86tgyNoiyCK0yNLeE5QfSvpMntYmL1whOuKnJ6aPJZJGLh1_Lm_DgAsIftdoN5xdwYrOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین توزیع قند و شکر کوپنی در دهه ۶۰:
عبدالناصر همتی
، خبرنگار صداوسیما در میانه گفتگو با مردم به مصاحبه شونده می‌گوید:
«اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره!»
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20812" target="_blank">📅 20:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGueThmMuqaLBYNjYWftaUzvff0dvn5iD2qybn7R81YIaRiurvicp5_QmtrTArdI5XN88m1fAdUyHjz9fgqGemGqVA5tEDYcwmiw2fLDbT4ojTvnWCTCZjEJrVf7Zfm7O-Q6qeie3nUN1uIxexhRPAwfoQj_d6_ABTZci44Ti7tNPs3Ne5lnvM6PeY1bwjPYEvuv_6ZVA2Kr7n-v3uxTV2mXv9MFrLHktE-p4EhsTvYC75W_1Kg6MomQXBBcrzs4yMDxG0gv8wjeXehdkwj6LPCGN7Z9Y8TK8OffLgGigoBhzYfmZo52RB5Q0lo9VZvh_ED1_Ga2-6_nAEgW3kjoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20811" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مرتضی محمودی نماینده مجلس:
اکنون که قیمت نفت بار دیگر به 110 دلار رسیده از نیروهای امنیتی التماس میکنیم یک مدت کـوتاه هرگـونه وسایل ارتباطی و متصل به اینترنت را از دسترس عـراقچی و همتی و مشاوران و دستیاران پزشکیان و قالیباف‌دور نگهدارند تا قیمت ‌را در این جنگ اقتصادی کاهش ندهند</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20810" target="_blank">📅 18:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
ایران بزرگ‌ترین حامی تروریسم در جهان است</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20809" target="_blank">📅 18:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY1V8Gh-uXYYRHeS0-BOElat9eL6lpP3MEYkt886EN4EaNxAntvADGYV_wrTsITV-4SNwZS7ftXEQhAvyy0eBTdSLyEcGaaf8unZfkSg7itvoIzNx3SdPT0tDiW6VYYWyyVDny7T1FIAEvR-C61yyQDl0sNTti45x9sz1UxR-aphaZKrd2P8nIbgCcUbAVuKgpbwPFZi8f7pxlqhi3DULeg9agnZWXL9awLdNxkDVqqe6eZ3AIUCcK7axAdc3fsWIEGQDabWHk2MJJb1QZx08cpPOlMJ2ANH7yJF4zBDgilDDKbpEJltzwJnRj-fl4P38SYhx5yK7Ro9f2rmSOuqDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20808" target="_blank">📅 18:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-lX7jdlN2rZstp1ShRYBnqUnz9u_-S1_lQRmUsgnEkfdqk5FUICr-xHYSh9p__IyM_roh3sAv8f2bG_rU1KbERksFd_tdPHUeBbjwlxL26d5vK-6wlpX_43f8sX3tM1b8YkBXE2HmHjCqmHegF0DFmTd3JIK50SbKm-JN1UCndjKp-TILpLYBUOMk-RLXK1THurxEbCXWmJeYUZWpgnLJSSH1MbC35ARWMR_hLBca20ERYg6HheC3_FJGFCNeYEn0ADAzn-4bRra7qJNdqmC_PFTRcrkr7MRjntIbdKlr_kZm3EfyAukQ-jvMv1jl6QsyjLDj2KCvMcIPiO6s4CCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری روسای کشورهای بریکص</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20807" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20806" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20805" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20804" target="_blank">📅 13:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQePSY5o0qhco6M5_-MLikZZZwIomY4BkiR0Xj9lNTkI8EuvB2wh5CZl65730mKKyEeriHUqw9Ct0cJ-BdPTf_xx2IU6_Sod38wk2eo-24WdChdzda1fy3mU2Wu5mEutq1W1f23CaiMZumKcmurDFqmD2X9Mm2CRMVHs1fkAVwurG0JlB1VQr5yE1kScIX7ESuKBDO87wjdikHJjuAypxsWReddHKaTrk3xSI1KqMbQVh0r4h9F0vUWRoceqFWhQYB20RWOTnBkyM6rzHhU8_fWrS3gKdJLDVgBVwcJv5ckYorUfVliGXSzkYgfjlrYL10o9ExUyb9v6haXriwLvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20803" target="_blank">📅 12:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20802" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20801" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20800" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxnWb5_eVXP3xl9HDFaZ2XX2HVO6jT3t0ZIQ237jpbOjKkGCVbTKJ5wBSltRoVFRKKUwnS6mq0jTXoi9js-8Jscov1MB05j6974tgpmtOOhL0zf0HQOuLmDRFiSDm37kk1Dz0Z7rK6v7LQS4Wu7NwK2JN54mD0_dQ5P7UEVgsLLkjl6EBWxsD8fmTazOSLA5yaUsE8tNKr6gB0fWDpw7CMko4-pEg-XvAVk6CTae5XdYHEv60pRKsLlCMPJeUEFCNAofBOhQulbY80eJNmLovrByL0ZA2uJ0X5BSTCIMjqav7zKO_7UtFsZBLfE7HZjN3ar2B5J5L6EVLzD1cR-1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.
نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20799" target="_blank">📅 11:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d95Jy5iYZUow_RFj8sTDuClr-jHfxO77dKiPBhEHmMmd0OLKZgBVYpRsTyRmOspmdPOtad8AvcXzvaA-kDK2bkiRIv7H79wJ6YScoH6b0LI7c_sU1xRlHOL0zbzMoR_RiImF7BDzHG7Te--6k-GRsclZrZ8C6PeftXMfrRmixXNwdtRkufF4ng55je0hmhDnI-XmbcsjIb_rEwBJfyDcbuu7-e0DDEXmA-pL4ZgCAq_e7Kfb28ZSaErTs-wcdh1D4Ft09qs1vfaqPvqFDEuAF2snbkNAcSb2bOx1byskrnlU4K90RaTHgP5qh_6rCvkzL-JJ2mNPX9AWgLzMr_ZeGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20798" target="_blank">📅 11:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گویا امروز حوثی ها این خط لوله را هم در 6 نقطه هدف قرار داده اند!  با ادامه این وضعیت یعنی عربستان حتی از مسیرهای جایگزینی که طراحی کرده بود نیز نمی تواند نفت صادر کند!  به نظرم تشدید تنشی بسیار با اهمیت است و از دلایل جهش بی سابقه نفت در روز گذشته</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20797" target="_blank">📅 10:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieqihflSojkbLLNYR5-mQ1I1U6kou1yuAiB-sg65mpuj11g9bQ2adr3o-x_TRWa7fb1VQbzukxEx1JQ2u4bzMbWsdobd76IOfC_FNR9qEPB5abTFQn_gROmWc9RoOqutny2l1PL1pLYwP_OIs5kU6ns5QqTzGMGgqPIF-HxXfqYS8ejQTZce0MmL6NP7bfKMlZwxxMhtrEFcGTlq0XKqqQGlAAo1U8rzrwNfa6j-IyNnhhiHcS4N5UVrixPp7QO0m59Iw0013_EyW4kbIZI9A9rLDVhjIVJtymaRgaXf5oeuNdzq8ljih78qsA11X0IvlXmeer4uxZX3cy4b5O7ErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای درک حجم و‌ عمق بی لیاقتی و بی عرضگی ارتش پفکی سعودی کافی است به این عکس یادگاری جنگجویان حوثی که پس از تصرف بندر راهبردی مخا گرفته شده نگاه کنید!</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20796" target="_blank">📅 10:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SBoxxx/20795" target="_blank">📅 01:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی ها هم می خواهند یک خط لوله از بصره به این خط متصل کنند</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20794" target="_blank">📅 00:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGfOodq976TBbwfMuL4YoUpZf-nPUnVTGF_Usy3Z8jm5PBMsYXUwI4fD7cxrNnORx_ytEEJS3rlS9q9hNG-UAecbCX86boGlmgH--wVE7i0xSJH74AevIBXuwNT8K453rOeWlnZINIdKQkbBqffZvXZ9WJn8GQNt37tciTFME2kEHd0fE1JJ47Mxh67oLVylCoRfoF6PnLAAbcDwew_vqAPoYqt_Pb2AB81kZBhvrGODb4026ht-CPF8AM0KMxVK8l1dwatKR3V1r8ZYk8DC7aQlCf8cKFWy6Gk7DiLeF7_n5ZuLkcTxB2_9NQ6c5ZymvS0XX3VIzGTuZgFwyOVtnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20792" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">علی الطاهر!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20791" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3RZNWB_oqLwLhv4lk_VUoR2411AwbvuunzlCMk15ss53CUSkv6ewckancL4Tl8tykXdYBFKVfUui8YF_uhINOS5KncoU264bXwJVVoso3vsu4EBPefd4krftoaR8d5WgroLvuFvvV_JngBy2pkp0ZPjGTuDxYHusfg88w82NfSJEvs9duU-5pJcXg6Rz8RFRdeaQe8NDR84W96EuyY9sfEFsWKtwzbMQ8CqzFubUvbFhozlRGRM3UBlRPB1fhOqetwLS0meBMih2Bz1q0cvmGB43H3XfZO6F6g8ukfhDjG1TTKzybLyPQJ_l0Gv7l56HK_NaauFIAJiMnHDDzvcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکستن انحصار چین.pdf</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20790" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شکستن انحصار چین.pdf</div>
  <div class="tg-doc-extra">186.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا چین راه اوپک را می‌رود؟!  در دهه 1970، زمانی که کشورهای اوپک در واکنش به فشارهای ژئوپلیتیکی بر سر حمایت از اسرائیل، تولید و صادرات نفت خود را محدود کردند، کمبود عرضه نفت منجر به فشارهای تورمی شدید در اقتصادهای غربی شد. با این حال، این شوک عرضه، نوآوری…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20789" target="_blank">📅 23:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAMjZc6M2WSMSn4RyfHtIACprAQ2Nwhk3-GBDzArvsAIAYxEO_PQ4gWWf6ylvuh-3Hd9_4IjhNhXTXAeZJ0iPSMWk3BmDioozjXb1S-xorlZRY9hoXmTifTe4vjdfAq8VBS32nAYKqt-G6rcQRttDBOBLvUerBK3oC83QEAGSNwosGwNTlWGnrLmhd25ZCdzM3PbqW73s381rbYHvibtyMUQMC37Q45cYbf8OGVb--J78E0vAuwD1-qEBlMmmOP0TTHi3lg2Jo7WpE_c967awO2ZPtHeQpQ5IOHx0UrkvUzgNS6Uqi0-OHv20YFvq3bE8oXXDEO0Oids-fCyLmt4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:  با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.  این زیرساخت‌ها،…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20788" target="_blank">📅 22:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:
با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.
این زیرساخت‌ها، یک شبکه تروریستی استراتژیک است که طی دو دهه گذشته، با بودجه و برنامه‌ریزی ایران ساخته شده است. این زیرساخت‌ها و مقرها در منطقه "علی طاهر" قرار داشتند و قرار بود به عنوان پایگاهی برای اشغال جلجول و کنترل و تیراندازی به سمت شهرهای "متولا" و "کریات شمعونه" عمل کنند. نابودی آن‌ها، به معنای تکمیل کنترل عملیاتی در منطقه "علی طاهر" است، هم از سطح زمین و هم از زیر زمین.
نیروهای ارتش اسرائیل برای دفاع از منطقه و جلوگیری از بازگشت دشمن به این منطقه، آماده هستند.
ارتش اسرائیل در این منطقه امن باقی خواهد ماند، به نابودی زیرساخت‌های تروریستی ادامه خواهد داد و از هرگونه تلاش سازمان تروریستی حزب‌الله برای استقرار مجدد و بازسازی توانایی‌های خود، جلوگیری خواهد کرد.
دولت اسرائیل به حفاظت از شهرها و مناطق شمالی از داخل لبنان ادامه خواهد داد و هرگونه تلاش برای آسیب رساندن به شهروندان و نیروهای ما، با قاطعیت پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20787" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال استریت ژورنال :
ایران در حال ازسرگیری تولید محدود موشک‌های بالستیک در زیرزمین است و پس از آنکه حملات ایالات متحده و اسرائیل به تأسیسات تولیدی آن آسیب رساند و محاصره دریایی واردات سوخت را محدود کرد، در حال مونتاژ سلاح‌ها از قطعات ذخیره‌شده است.
تولید همچنان به‌طور قابل‌توجهی پایین‌تر از سطح پیش از جنگ باقی مانده است، اما تهران هنوز یک زرادخانه قابل‌استفاده از موشک‌ها را در اختیار دارد و در حال ساخت تأسیسات جدید زیرزمینی است که برای محافظت از ظرفیت‌های تولید سلاح در برابر حملات آینده طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20786" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موج ۳ از ۵ در حال آغاز است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20785" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو
:
توانمندی فوری ایران برای تولید بمب هسته‌ای را دو بار نابود کردیم و آن‌ها بار دیگر در حال تلاش هستند.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20784" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تنها دستاورد موشک پرانی های یمنی ها در دریای سرخ هم بدبخت تر شدن مصر بود و نیز برجسته شدن مسیر جایگزین ترانزیت دریایی از چین به روسیه</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20783" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcV3S2PMEmReEO00hCLUXVrNE7NrpM37TTv1luG7I7C6PqtpszVNWIspk1vK5_CtqYOAvf9MPyJLqA55j-XstD1Zoz2Mk0NZG_mLkgTAWo1SKiSFercT_4coxactpwpt5zVDrvM0DVLAyjU6eexAHZ4TIFiy72D9MjNl491d-6NVwe7Omed7mFb8-rUOYv09PrQpkRw1vxOvqhrS0Avlc-hFyU8J_p3XIpWmkxPgX48r_HmoYII4sgGuhyrX_JpzVFw8BttKrnYzdxQSRDNURxQ28v4f-FolkJpjdSHJRqK93fagXklG2QOCW8Of41yS9dY_ncnAKp_A1xxq6E964Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20782" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عربستان سعودی به اوپک گزارش داد که تولید نفت این کشور ماه گذشته به دلیل اختلالات ایجاد شده توسط حوثی‌ها به ۶.۲۴ میلیون بشکه در روز کاهش یافته است که پایین‌ترین سطح از سال ۱۹۹۰ است.
احتمالاً این ماه، پس از حملات به جازان و ابها، این رقم حتی کمتر هم خواهد شد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20781" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20780" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20779" target="_blank">📅 17:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkHAQkDO6_-Pt7BxYR9-RvwOvNW4yF8gBP4DyhRZrshYaj_z6XnGL6M95f1ZiUyHw_CYc6tWVa0VQ5sJqnQ4nlZ-aaU1yghQCVDiotQVoF8DGJF0o9G21yNSxbiqGrnDYi7e8FBhOHx_MiIVD2oxm4reNa5ugRbowQdH34Ln8sYpKNdEbv7PcgCvHuelQXJvThomHrZSxm8rUgIssafY7hShwrFWbXW2I8n-QB3lq1fvaHFM-nGt8aN4JtezxyxNxsDs0gN7mEzqoOCNoC6bJoUXkVcinPDv_5Tffcy8oZRcRJW2-rembYB60F5Ayts8P7EaWHz2CTbpF1K27PRuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این ترتیب باب المندب هم بسته شد و ۱۲ درصد تجارت جهان زیر ساطور حوثی ها قرار گرفته است!</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20778" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20777" target="_blank">📅 16:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اخبار اولیه حاکی از آن است که نیروهای مسلح حوثی(انصارالله) جزیره میون را در قلب تنگه باب‌المندب تصرف کرده‌اند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20776" target="_blank">📅 16:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گویا طلا منتظر انتشار خوانش شاخص بود تا ۳۰۰ پیپ بریزد!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20775" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در یمن شاهد فروپاشی نیروهای مورد حمایت عربستان هستیم.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20774" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxfK0ndiMKKoocTm2Ol6yZ3B0TSaXqtB_UKfgRm1gelZTCaBFM2R2DLQPunAvYRMBfSoPBEN7HdT-40xe0UdvY-_yspCn296QjoS2fboue8poyTLMqJ6202d9ieOSrOvoYJkklhZz76-yKbJx4SuK6HwFqzpZ7-XC3LsWeasvgcPnpynxu2XrGsTjgKiW18GLk6YEINlbo7VhB1OBZkGOFVTVa1XUyvGvsEiM0J2n0liAmhleaNHPA8v4il6f3jhSQTDgWuO38z3B0EZ45zUGbREwG3N6hatWRq73g35FCb-dFv2MpY2JjZteX6v6zVZhhEaroGLK552OmdIuLg9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزیره زُقَر هم به دست حوثی ها تصرف شد.  این جزیره در مسیر کشتیرانی بین‌المللی در جنوب دریای سرخ قرار دارد.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20773" target="_blank">📅 15:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20772" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20771" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHZzYCXby7pAH-ZuJunot90_0KBqr6LVkgv1Q_suo64b_Nz75p2GYb01h6bETyNTuWpEUPURml7sRKZ3MQBEFnCqadP4vEekq4cLdPj7DJqeB6P0YhsyHOv10y-lyHvoAluEbExg-gzyLAAhYh7bf2StmQxv2UpKWFCm8pxhy8doMY-grLOX9mIBICqwqL4DKPlkHhoQpn0BCTX7oqmL6LuzPavX8A2MuUasm_aZxo-qF3CW5dTsA1ilOy6gF_JTIGCdH293prAcvlZTcA2VkJ3xfjEo7lqBnJRQ-hQg59dUFHzVv8jDepyYtPHMBXNYFcMLTemXRYuKnuggsF0Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 26</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20770" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حوثی‌ها در یک پیشروی ساحلی سریع، حدود ۲۶۰۰ کیلومتر مربع از قلمرو در غرب یمن را به دست گرفته‌اند.  این پیشروی به سمت استان‌های غربی تعز و جنوبی الحدیده هدف داشت و گزارش‌ها حاکی از آن است که نیروهای دولتی یمن با حمایت عربستان سعودی در سراسر یک جبهه گسترده به…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20769" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20768" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بلومبرگ به نقل از منبع ایرانی:
ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20767" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLgg6rvchYqB86JmhbpW9--UFvmJ74Z3AQXXMfwfDReNBYsS4Y5We18EfiU5r7CWh7pXHaEZpvbqdjoize_y4lyJdwYltGWCmj9udHDXrZye9cnwBTA6DtMVE8mh9VqG899NA0HYAQcE_Hq77OMjzL4nvQLIGnnMtVKOooraDwh5ehFJwQFjMOJkv9VoD6i_kXcX2pt_P9eS_O8SDtN5sH3iyAm1NvbWzjUiPW30YpqmvUG__MBlx4teHXz-0dlp7LfhVry3iaJLXCi8E7FSx8fiH_VD5VDWvQYhe56OxrZn6D2S_ETdMGWiJkScac7Mwr_zcPy--bjBHcsDYKtLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20766" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">راستی فرهنگستان برای shemale هیچ برابر پارسی پیشنهاد نداده یک چند میلیاردی بدهیم شارژ بشود استاد؟</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20765" target="_blank">📅 12:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دارم حداد عادل را با شلوارک و پیراهن هاوایی و کلاه در پاتایا تصور میکنم!  اصلا آدم یک جوری می‌شود!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20764" target="_blank">📅 12:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9fjQV_UWT0kbhGYtRBOGUkp_QLnctV8iaxIKgTy6BT3BfNUo1s2nIqoXDiiBC01PLIttXoN_UvtsSw-l6wYW-w2HHEks1ReXvpAG7BBiU4NXaE8oAW48wI3z2d6JT4mB3Ud2thUYMBL80h91MnsdC9LUy3ytZp5bbXd5SlXzOVGQXQPxKs6zu0Sb_EzkM0qYzvc6ov8OctE_isYUS6eTWJZhxnQhg-CunUiNe-S4t2tuhBmMDDH185OhbARQd1cHKg48I4UqFB8SB23Qkq3ojc2aUm9_pwnfrC2Qy570TnzryZ33tMSnbUzsM3AqakLjqUPlVgJEkrmrPL6DWkMzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20763" target="_blank">📅 12:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پس مشخص است سفرهایی با اهداف خاص هم داشته اید کلک ها!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20762" target="_blank">📅 12:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:  وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر  با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20761" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:
وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر
با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی انتظار داریم که قانون حجاب را تعیین تکلیف کند</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20760" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBSCfIrMJ6h4e2JEoBXE7bIMrtqmycfwYBqRpRL3N3ut8iHLSn5f5oDTeVGmryFaHn5ZYrhgLEmLh61v8ioumzSunUFMheMj_ZlgcJQBzP3FE3ggWcbtaK5dPpZ6DQZ7ThjuI3ZwvEhhZ7mGqqzeKYhvHaE0nrt37YowfRlcvDEHEiL3gBQ2Q5dNE4nq4Cct4X5OnAxYLb7xNZoUlUf_-tt8nrbOxxe3pm9NlBDmuaRDGPSYXhQQz_5VsTJ6Zm55WLmT3BypElVJVLtUISjXwMu1iQugvRiwt4hX7F2NxIqkau7nSAvcjDQRsofdcHdWeg7Mcp_kd6XC5Kbq5fj_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.
نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20759" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ:   «به لطف نیروی فضایی آمریکا، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، ؛ هیچ وقت محمد جونز نیست مثلا؛ محمد العزوری.  می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20758" target="_blank">📅 11:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmRs3ccEVjuuAdJkGX20q6dYTZIdO1z-yALVWV1XZl12gjRCJOyvYWz3PTbkkouTZYfiwxF0sz-02UsHdGUBRO1u1Cl7jIwT--7njC2S5mGxMALM46sh1KCuX7my5HDcIQEuigHKCrc7mgVgjx9KL_NCKSxWqy5fyhs4mZgQBHH6ANVibiw7M8Po_KoQlhApd6NxSgf1MSsvxZzizm9R_jDWOMFrYRO99Rsyt7_ONAdosfl1QzMK6STAb1Z_DAqqxkvlncbhlOfKryM179WoOwXGGGBhrGgISGF7A1NQo2wUK0mvPBFQilomaEHPSiJUvAWtPNEZTfnupePE5moZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر بندری راهبردی «مخا» هم توسط انصارالله تصرف شد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20757" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20756" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20755" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شبکه سی‌بی‌اس گزارش داد در پی حمله موشکی ایران به پایگاه هوایی «موافق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگنده F-15 نیز دچار خسارت شدند.
بر اساس ادعای سی‌بی‌اس، نیروهای آمریکایی مستقر در اردن برای مقابله با حملات موشکی ایران مجبور شده‌اند، بیش از ۳۰ فروند موشک پاتریوت شلیک کنند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20754" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt7WJ2bZqlHFq3e5DdzMy7zP94DFjIancuPyJqtyIKVG9BbgiTfs4eR9E_9uksuGDZZpNchBNmHq1UuMC_qbUscP3c7DAODtfZ6zX3FyC9Np-PbF6G_Z6cN9AfKUqrEQfMSy8Co1ibIHUuT2embBitXgMG2jupLDCh9l-BlwG--qp-uQfOrc_EKpP5wIhFkI8pjjt3li48myarhTGzcdShgcKr8TAOiJzU0ktP5iXfJTwtxTRgMchxoHZmlGy8bDFDuYm8uOmqax9Okuc49ZeiLG8qqjpbUjJ7_E2X4HJvVel8ooQN2kXC898lLxZSBNpJU73O5VU6AosxFoP1mTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20753" target="_blank">📅 01:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دو انفجار در طائف عربستان</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20752" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKx0Nv98Aobc37PuoJD8_cDN09bUhI_8QfwNV-A14OxqHDZ-SUz7Ov6bDrauZUFxTpiAXPC7EnvMeJAI9efIRZbO23x-oKZeViJkPKjJOfU9e__qA40XzMIGqKvm2EiHBGoBstSTajt72RInhOxypupUW6wYtO9o_VpYFUmrmJf52Yor2aa6lxNKcFp4SszRDF3xNknAxhtJblNDLd6ycapGD5liN3jh9d_te8Y0S3WDFvMrUE3dfZxQiT1gczSInYLlq1zA6uq5kIdCSmTZX9Vr812SqV_dYfyQY3z3tVeyQmbyWogwbTXxlZwmQLjAgjWrBjzBKFOQTWYBmhaPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک؟!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20751" target="_blank">📅 01:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پست ترامپ در
تروث‌سوشال
:
این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20750" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برخی منابع عربی از پرتاب موشک به سوی تنگه هرمز خبر می دهند</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20749" target="_blank">📅 01:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20748" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">لینک ویدیوی ضبط شد
ه نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20747" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA1Nty9uW78I6qK7Ejsq11mO-8R6A3wIu7zS0htb8006vegyke_dKiQCiD94EndHGQWk9irrwSTFNIi0MOYk6SB4gsoiUP7JqKpuSET91KCU6AffKdZJoC7Dn55flyjcD4OnxUr80rWhgyKGdEeUQqxJB659cK3RYIASmNXyfFcH5A5sAiUc-CrTnSZP14I9GAOCpXObVtlIaCxEuUgNeUrSRZYfEEFcnxhaP3rTtn-nisqLpoHM3iatzMdiLBdrygo6V7cCc_O1xxO1tdAvtqEuK-v4v7K7arUS79HWhQMNvUHBOEtLVW-2oeHU8Z7PZmBwVFVms2qVp6w_Jl1dYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20746" target="_blank">📅 01:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20745" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20744" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صدای انفجار در بندرعباس و سیریک</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20741" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20740" target="_blank">📅 23:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUEvm375AQFS_q5ulZJqrRH5ib3_LASpBt_ew697cswy2o1tQ-7gx2sjoU7vm15NluwQ8cpX6GbxKtDOcuV-ZVETeq9hZqZtPInw5Qt5vxd7ogps0kFphaRebVbhvRk_AIG5-3R0rRqTcjbW-zwq7mlqgRAu-Io9vrfcipI1ahHvVABL1eKroi0hd9pbozHkkyXa1E0rsmHY56cTkC54QsQyKifF_bEmqvRE0wnTu_YnAy0Ns2ByzIVjls5w2NF1iqtBTO9HzEaFZeBDCVw99ph9zcSLh5-GIb4NuUI0ShFF45t20YqcmmTpgQ3P4EzE8KH4674yWjk6VxcNY-Gbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20739" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ:
باز هم به ایران حمله خواهیم کرد؛ مذاکراتی در کار نیست و جنگ علیه ایران بعد از انتخابات پایان خواهد یافت</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20738" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigiato | دیجیاتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX_0xC5yXCHNIy0yTsuv_ATxnBefUeS8rQOInLmB3iXCDTmaTnw6IFKqR0KTvJEnBQlWUsAuLdBcJ03yaoKprTsMvLNdGU9D-IuYo5e5tNRE9iD_djdVBDiMHvLFWKuPfEDo2g7T5pI657VVZZGATP9G5as5JGZsmCfkwY3Bkoy9j7Hp44PwJlSKHPQUmJ8y7WtJcX9q0nnvR-QwtOtG3qpEkEpgohx3Tx_qBdnMndSpQ8JErDyV384ejRsFSlWfm0B0QO5a0Co78-s1lO35shGQ7hQ4vTctvpXMaToN8E4y6dpP3uazSPm3kOKXU50JgDv03g1J4QKCQUZhny4wQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
مریم عظیمی، مهندس ایرانی اپل دوربین iPhone 18 Pro را معرفی کرد
یک ایرانی در قلب توسعه دوربین آیفون؛ مریم عظیمی، دانشمند الگوریتم‌های زیبایی‌شناسی دوربین (Camera Aesthetics Algorithms Scientist) در اپل، در مراسم معرفی iPhone 18 Pro درباره فناوری‌های جدید دوربین این گوشی توضیح داد.
عظیمی که در تیم دوربین اپل روی الگوریتم‌های پردازش تصویر و بهبود کیفیت عکس و ویدیو کار می‌کند، درباره قابلیت‌های جدید سیستم دوربین iPhone 18 Pro صحبت کرد؛ دوربینی که حالا با دیافراگم متغیر، کنترل بیشتری روی نور و عمق میدان در اختیار کاربران قرار می‌دهد.
حضور یک مهندس ایرانی در یکی از بزرگ‌ترین مراسم‌های معرفی فناوری دنیا، بار دیگر نشان می‌دهد پشت محصولات محبوبی مثل آیفون، تیمی از مهندسان و پژوهشگران از سراسر جهان فعالیت می‌کنند.
#AppleEvent
🔵
@Digiato</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20737" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بیانیه ایران، روسیه و چین در نشست شورای حکام: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد   راه‌حل پایدار برای وضعیت کنونی تنها از طریق توقف فوری و دائمی تمامی حملات و رفع تهدید به تجاوز بیشتر حاصل می‌شود   همه پرسش‌های مشروع درباره برنامه…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20736" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20735" target="_blank">📅 21:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20734" target="_blank">📅 20:26 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
