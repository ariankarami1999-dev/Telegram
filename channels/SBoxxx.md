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
<img src="https://cdn4.telesco.pe/file/VcHhr_hKiUVuwWOARoyVOquS2SMKRZvgk0RkKWlnmRlL-jBr4dQI0LReJKQjJGP_qufk_lLLFBcjpyUmsFcl1y0nKwecDwdoF-BWtkq9EykOKs8Rp0wF2EMK_q8Z7zLSvVOTerUqDLAYib5Vpgx2xKRIxlto1gdqrUEDWS36TYW-lt0vspPV5kc6_8UgQJLFpSJwzM8aK0BRzGA2xFBo9SqtTSDCKWVuGT2Jw9tlhD9_m0kKrPHSAKpJPUh4CFjQmna82FEfEuWe_VWh5gPrv9h6dEjU5M2Y9wr9cGF6iPLsdv-hXcigBeYLeLxeVugpIXs2AZHLpTu52C_7dkiagw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💥
«هدف بعدی اسرائیل ترکیه است»
پل کریگ رابرتز می‌گوید که پس از یک کمپین برای شیطانی‌نمایی ترکیه—مشابه آنچه علیه ایران انجام شد—آمریکا به نمایندگی از اسرائیل به ترکیه حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SBoxxx/21489" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/21488" target="_blank">📅 19:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/21487" target="_blank">📅 19:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👤
مارکو روبیو، وزیر خارجه آمریکا
:
«ما طاعون روسیه را از نزدیک زیر نظر داریم و آن را به‌دقت رصد می‌کنیم. فکر نمی‌کنم دلیلی برای نگرانی و هراس وجود داشته باشد، اما قطعاً موضوعی است که باید با دقت و تمرکز بیشتری دنبال شود.»</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/21486" target="_blank">📅 18:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیویورک تایمز:
بیش از ۲۰۰ پرسنل نظامی و اطلاعاتی ایالات متحده به عربستان سعودی اعزام شده‌اند تا مستقیماً به نیروهای مسلح این پادشاهی در هدف‌گیری سایت‌های پرتاب و تأسیسات ذخیره‌سازی موشک‌هایی که توسط جنبش مقاومت انصارالله یمن اداره می‌شوند، کمک کنند.
این مأموریت مشاوره‌ای مخفی شامل تیم‌های کماندویی است که در طول مرز عربستان-یمن مستقر شده‌اند و در کنار فرماندهان ائتلاف برای کمک به جمع‌آوری اطلاعات، تداخل در حملات فرامرزی و تقویت توانایی‌های دفاعی ریاض در برابر حملات انتقامی پهپادی و موشک‌های بالستیک، همکاری می‌کنند.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21485" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کلیپی از کشتار نیروهای حوثی توسط سلفی های مورد حمایت عربستان   در ثانیه ۳۳ فردی که گزارش میداد می‌گوید باب المندب عربی است و نه فارسی ایران!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21484" target="_blank">📅 17:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=VzHrZ01Scgchku9fYHwCi1xkmweef77ztTbLCX8CoxXTPBywQGzIGV4dlLllfF_fShI8QyuWCKsV2P0GTYxR5oGaTIofn472HfQT4Z6P7hKDIBz85XrKz0B_cynGDcXqmzo8M__oydeA3nrvT2_Vokg6e2K6Pyvu8ihsAodB6t0q4hDLCQ0nWDKM3OYS6ao81MpJQ4UvqOt0mvN4zD_GZVg3mq_lKAWovkbQFKUkVkXm0qnP9fFIOpqoVepJWRnB1kqiSPpZLSc_mzctxQPECmmtFjaUvO2kvf4s6c_m_HD7b7BhxvkyUlUZg3R621dQsRf0fD2L71BJNV_OuzSdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=VzHrZ01Scgchku9fYHwCi1xkmweef77ztTbLCX8CoxXTPBywQGzIGV4dlLllfF_fShI8QyuWCKsV2P0GTYxR5oGaTIofn472HfQT4Z6P7hKDIBz85XrKz0B_cynGDcXqmzo8M__oydeA3nrvT2_Vokg6e2K6Pyvu8ihsAodB6t0q4hDLCQ0nWDKM3OYS6ao81MpJQ4UvqOt0mvN4zD_GZVg3mq_lKAWovkbQFKUkVkXm0qnP9fFIOpqoVepJWRnB1kqiSPpZLSc_mzctxQPECmmtFjaUvO2kvf4s6c_m_HD7b7BhxvkyUlUZg3R621dQsRf0fD2L71BJNV_OuzSdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/21483" target="_blank">📅 17:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">— مقامات اسرائیلی پرونده‌ای علیه یک استاد ریاضیات دانشگاه که مردی در دهه ششم زندگی  و اهل پتاح‌تیکوا است به اتهام برنامه‌ریزی برای حملات گسترده علیه شهروندان عرب اسرائیل تنظیم کرده‌اند.
بر اساس دادخواست، هدف او اجبار به اخراج دائمی آن‌ها به اردن، لبنان و غزه بود.
او قصد داشت ۷۲ اسرائیلی یهودی را در ۱۲ گروه برای انجام حملات هم‌زمان جذب کند، با حمایت از عناصری در ارتش اسرائیل، از جمله حملات هوایی به مراکز جمعیتی عرب.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/21482" target="_blank">📅 17:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/21481" target="_blank">📅 15:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/21480" target="_blank">📅 15:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-text">باب المندب؛ قدرت های بزرگ‌ بر می گردند؟!
وقتی ۲۹ شهریور(۲۰ سپتامبر)‌ نوشتم به زودی حوثی ها ناگزیر خواهند شد از باب المندب عقب نشینی کنند، سخت مورد نفد قرار گرفتم.  البته امروزه روز، مساله اصلی این نیست که حوثی ها شکست خوردند یا عربستان پیروز شد؛ بلکه مهم‌تر این است که باب المندب در حال خارج شدن از وضعیت اهرم یک بازیگر غیر دولتی(حوثی ها) و برگشتن به مرکز رقابت دولت های منطقه ای و قدرت های بزرگ‌ است.
پسگرفتن باب المندب از تسلط حوثی ها، در چارچوب بازآرایی ژئوپلیتیک ی پس از بحران ایران ـ آمریکا معنا دارد، نه صرفا یک عملیات جدید در جنگ یمن.
اگر باب‌المندب توسط مخالفین حوثی ها تثبیت شود و همزمان فشار بر هرمز ادامه پیدا کند، یک نتیجه بسیار مهم حاصل می‌شود:
دو گلوگاه دریایی خاورمیانه، به جای آنکه اهرم‌های مستقل ایران و حوثی‌ها باشند، ممکن است به تدریج تحت ترتیبات امنیتی چندجانبه عربستان، آمریکا و کشورهای غربی قرار گیرند. و این برای ایران از خود عملیات امروز مهم‌تر است؛ زیرا در آن صورت، عمق ژئوپلیتیک ی ایران در دو سوی شبه‌جزیره عربستان همزمان محدودتر می‌شود.
به لینک‌ زیر سری بزنید:
https://t.me/Karimipour_K/6256
#یدالله_کریمی_پور
#karimipour_kپ</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21479" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خوش چشم:
اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21478" target="_blank">📅 14:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لوئیز ایناسیو لولا دا سیلوا و فلاویو بولسونارو به دور دوم انتخابات ریاست‌جمهوری برزیل راه یافتند
با شمارش نزدیک به ۹۹ درصد از آرا، بولسونارو ۴۷.۲۸ درصد و لولا دا سیلوا ۴۴.۸۷ درصد آرا را به دست آوردند.
دور دوم (Runoff) در ۲۵ اکتبر برگزار خواهد شد. این دور به این دلیل برگزار می‌شود که هیچ‌یک از نامزدها بیش از ۵۰ درصد آرا را کسب نکرده‌اند.
لولا دا سیلوا، رئیس‌جمهور فعلی، نماینده حزب کارگران چپ‌گرا است. فلاویو بولسونارو، فرزند جیر بولسونارو، رئیس‌جمهور سابق برزیل، نماینده حزب لیبرال است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21477" target="_blank">📅 14:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اعتراضات گسترده در اسپانیا؛ خیزش علیه دولت چپ‌گرا و سیاست مهاجرتی سانچز  موج تازه اعتراضات در اسپانیا علیه دولت پدرو سانچز، نخست‌وزیر سوسیالیست این کشور، به یکی از جدی‌ترین چالش‌های سیاسی دولت او تبدیل شده است.   کانون اصلی اعتراضات، بحران مهاجرت در سئوتا،…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21476" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا  فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.  در کنار فشار بازارها، بن‌بست سیاسی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21475" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVaQ8WVhfzTM0Wf1_dYD7BwC5YjtDhI3xoN4cj4r8JfD0aaSyEEAELQw6tryxB1vy9WskU6YEBKJKR2zkr1qODBn7op8t_ywTO4pZGmcty-4PqKJ6GiOjVI4JecCkkAX1pNJSZpbHukhLHb9NDcp0eHXXrqeGGIDfpo9-Aux6Q3EW9ocnwzniQxtPaaAjRJpdq42omKXqd8mQcE-or1qobWypXF-lESQYhVbbklXIfeBhMbmW2jBfpOkt0uk-VlmjRhKllbYMmP6zVOM2aUs22NtG_BgqEvsIlHTWmn1GN_hZdSBgs1rypDW9NAtQCVXjQBluO39bcuP3bjCuonafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا
فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.
در کنار فشار بازارها، بن‌بست سیاسی و دشواری تصویب برنامه‌های ریاضتی، مسیر کاهش بدهی را پیچیده کرده و بحران مالی فرانسه می‌تواند به یکی از مهم‌ترین چالش‌های اروپا تا انتخابات ۲۰۲۷ تبدیل شود.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21474" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEfcJpcQhJmW-UUytnzZBbNBzKx4J8ZONpjqB7tkvosij6XLWfRECZxs-H0TtWUwHfEVpH6un9yq8UW-h1yC5OdvFaBjQu019XFUFsaGGv9-Cl_TxLuSB0krKuCNfPB5Xx6osgLEi1wnFKB2TXiAXmkW3v7voS1TLLw7L5eiHeONGJCH8iFsLN_Oso2oON02OvT30XKJsK4ojmORPJnuaUq-S6X5zTGwZYxEQmCZycmPUzdAo6juBkfkQbAf1UN1YsAwxZokk_3ebrKDmayWgDqUM2J8tgrGschCp5ObUk76LqYGXj6uhNRu_Mj0NUy-FiF0fYrwu8qt3ww7ZlmHFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله  به گشت پلیس در بمپور  بر اساس گزارش‌های اولیه و به گفته منابع آگاه، یک گشت پلیس در شهرستان بمپور هدف حمله تروریستی قرار گرفته است. این منابع از شهادت یک نفر از نیروهای پلیس در این حادثه خبر داده‌اند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21473" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21472" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Ylq4ldZFn3zNzxfXB_scahJ41OZ-v8mJYrrIv83xnP8Z5nd__gM27R6OLlO6hXyHGqcSLgmd80J7Wb0yctG_W1TcWbnfud3hsLfx9GtE5PdkbGE9UKIT9EbKN5SBF_OSA7quoOqEPNLde91NyxR4hZFDnb1dsT8q20pfJ1gkLkVsmCSMoHtb0M_RXUuZ1MlCbQ7RLuq_FkeDTpRBpos0FJBBz046gpGTh6rPL7xIOwjXqfaoMGaLLsCOeXG0YhxZE6jKBDJJHEQoDFeq9w9zWgAzfU5m9aLT-kuOppILEBnums0Gqnv3xWgjm36QMtBzF5EgRscH8mjN8fRdPlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان در سطوح پایینی قرار دارد و فضا برای رشد طلا هموار است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21471" target="_blank">📅 10:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-bw-coNEfG7VK44UI89RMRHI94Dk0jnkRThh8UjTBLkiRCJdYLDDnokxYbYjJqC9Nw-_cWs631-LEfiO3wpzaXAkaD8VTU9Tjnaf7sFb4iu8kYERmhY89aJTKnanCTul7En91CJ-bxTc5Cj411srXHYoVUXuRVG9YSTomEKV4jxtdMQj2vgycvjhp2XufYUm03ksE9tEwFyNmigRK61L7encaYMVeOtmOn9TJY3Mj3Q-B2zwrpaXoxs0cCGM-qkUjjuUiWpw4zmd1bHqFelkFRX8_lCjKsaP2wZy1WtanNY-rtH7Mh9ARehkRlkJSHkj0-q7bJAGUPoHUUfIKx2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21470" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر اقتصاد:   تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21469" target="_blank">📅 10:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر اقتصاد:
تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21468" target="_blank">📅 10:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21467" target="_blank">📅 09:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc5C3qeN0HnCC9Xyu7jWi5oyhtYaQwo49Tz2sc8Xn7vRV_1CzQZvFvM9FqbxhMa5oBIviYaFzJlqy5UPi69OU-n6TjVakQSjOVRqDs7MXbdX4ZYAf1jAVx9LWLyw-NgLnsmqu9V3w5MxePkOuFaUc-dwzpcHkkKGPQTQP99ruIgxpZHdaLrGspNwsO4Y5qoDB9HqoGLOae8E2huBPCjbN8l8ZITn4CGiqoeRb2zvEw-RUAvTmB3xEYLR9R3m4xj0gTOdRIu9L4nu7AX-eU9b3zJDjVFEuJa7Llxkp3yT-rwIaTQWkRDGUu3Ue6rQqFB7_G7RfvnLgGyEx0A7ZUTmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21466" target="_blank">📅 02:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حضور نظامی آمریکا در اسرائیل در حال افزایش است. در حال حاضر حدود ۳۰۰۰ سرباز در این کشور مستقر هستند و انتظار می‌رود نیروها و هواپیماهای بیشتری به آنجا اعزام شوند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21465" target="_blank">📅 01:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حضور نظامی آمریکا در اسرائیل در حال افزایش است. در حال حاضر حدود ۳۰۰۰ سرباز در این کشور مستقر هستند و انتظار می‌رود نیروها و هواپیماهای بیشتری به آنجا اعزام شوند.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21464" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pqrx7Nms5KaTgT2-QanG6OEwQ3dnU9S73-Xw4cJzccj7pBig5Oxe2Ijjo-uJsh_KUVsBzRItAbQ-6EMRnRySpQc2y17hHygov2ayda5B7W_lmWlMKu2GT2KZ_s-b1RGq-PvIooDRduSR4zA63V-YMvUJahhSCdB3IdEgELaXI5LXiywuorh5XLeReJgh0IM1edJ0kra1kt44H1DffA-j80_bkH6gtBaAY3Yxeb3kGFOUe11X2pMmIriL5LD7HWp7NiAIFeXnV9nJAYfMZnF_s7npS4NsV3j_A9omEsx5DZNnpjs9ba9JIXesN6dXanHsmYn6wYBsgEFzDjebPDX2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر سیاستهای ضدمهاجرتی ترامپ!
طی ۵۰ سال گذشته، دست‌کم ۲۳ میلیون نفر متولد آمریکای لاتین به ایالات متحده مهاجرت کردند. این بزرگ‌ترین جریان پیوسته مهاجرت در جهان به یک کشور بود که در سال‌های پس از کرونا به اوج رسید. دولت‌ها و مردم آمریکای لاتین به این موضوع — و به پولی که ساکنان جدید آمریکایی برای خانه می‌فرستادند — عادت کرده بودند.
سپس دونالد ترامپ دوباره به قدرت رسید. در سالِ منتهی به ژوئیه ۲۰۲۶، گمرک و حفاظت مرزی آمریکا در مرز جنوبی ۱۳۷ هزار مورد برخورد مأمورانش با مهاجران را ثبت کرد؛ یعنی ۹۴ درصد کاهش نسبت به همان دوره در سال ۲۰۲۴ که ۲.۴ میلیون برخورد ثبت شده بود. مسیر دارین — مسیر جنگلی از آمریکای جنوبی به پاناما — همین داستان را روایت می‌کند: عبور از این مسیر در همین دوره ۹۹.۹ درصد کاهش یافت. در کاستاریکا شمار مهاجرانی که به سمت شمال می‌روند تقریباً به صفر رسیده، در حالی که تعدادِ رو به جنوب به‌شدت افزایش یافته است (نمودار ۱). شلوغ‌ترین کریدور مهاجرتی جهان ساکت شده است.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21463" target="_blank">📅 01:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21462" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21461" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/21460" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏ مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:   به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم ‎ ‎</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21459" target="_blank">📅 19:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:
به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم
‎
‎</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21458" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=WGr9Pe92I9kFVdmCCv6RqfSGS50IOPEgqMDZywtgwVBklFTji_o7BFkIMeEIrs4ZTI_KwB6wrUSIZ4NFzVcBfDxbqlkWykAP6HUGZTbVVE6_qZmuIkhfIuZxSPQsq1mkSmFDPRy1LjQFRzRfUic7EIJ349s-QDiFzcnmws2iPvGMIVZyszC2WNOPIYyN3Vm4eVeNfPbw03aEjczLUkqYFFT2bbzT3v_Z3PBilcA09jvLBx3N2nq7hjtlAd0muuyvVEuZaFunEq58buzcTMVGmEEvp9_VB64xwoBvWvkyoZzzm947trMaSL3cUI9RqkP6RpWMWkadR4Ca1y9BOg0Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=WGr9Pe92I9kFVdmCCv6RqfSGS50IOPEgqMDZywtgwVBklFTji_o7BFkIMeEIrs4ZTI_KwB6wrUSIZ4NFzVcBfDxbqlkWykAP6HUGZTbVVE6_qZmuIkhfIuZxSPQsq1mkSmFDPRy1LjQFRzRfUic7EIJ349s-QDiFzcnmws2iPvGMIVZyszC2WNOPIYyN3Vm4eVeNfPbw03aEjczLUkqYFFT2bbzT3v_Z3PBilcA09jvLBx3N2nq7hjtlAd0muuyvVEuZaFunEq58buzcTMVGmEEvp9_VB64xwoBvWvkyoZzzm947trMaSL3cUI9RqkP6RpWMWkadR4Ca1y9BOg0Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار بالن هواشناسی خودمان توسط نگهبانان غیور!
آقایان صیدی و رضا عصمتی!
احمق‌ها کجای این شبیه پهپاد آمریکایی است؟!
هر چه میزنید ناموسا ۱۰۰ گرمش را برای ما بیاورید</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SBoxxx/21457" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گویا حاج عباس پرینت خیلی مهمی در نیویورک داشته.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21456" target="_blank">📅 16:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدودف:  هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.  ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21455" target="_blank">📅 14:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مدودف:
هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.
ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21454" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی ارتش ایران
گفت جنگ اخیر باعث شده تهران به این نتیجه برسد که باید
برد موشک‌های خود را افزایش دهد
و کار روی
سرعت و دقت موشک‌ها
نیز از هم‌اکنون آغاز شده است.
او گفت:
«در این جنگ به این نتیجه رسیدیم که
حتماً باید برد موشک‌هایمان را افزایش دهیم
و اکنون در همین مسیر حرکت کرده‌ایم.
نسل‌های آینده موشک‌های ما توانمندی‌های بیشتری خواهند داشت.
»
این مقام نظامی افزود که
دشمن اکنون در فاصله دورتری از سواحل ایران
و تا حدود
هزار کیلومتری
قرار دارد؛ بنابراین ایران به سامانه‌های
دوربردتر، از جمله موشک‌های کروز دوربرد
نیاز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21453" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21452" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGVVpAzfGrAxJJWfx9esop7OiGW_653spMscqnNpGyiFjquMF0cTBwbDEC3IwJqUWx3xOCl1yBHHNHGlau2wyacFePc-irybhTwU3DKyvhNr4K1nqYHkIkqkqDP02homSc0NT8keioi9OVbPUlKiYiGAGjjvTq5lxMnZygFcfA0J_DEtO53H-XTF1Wn-CGU83yjhVTS2pgh9wbTjr58C1px6IkLgwaGclXReNcDW_XMSiBPvaiNIxGYQjl-j5yY4AUXDChFmnHDloAn8YQOzHULcTGHAlVzi6Qm5viEuCmA61AQ41bnthbJI4UrthpMtKQrP9Xnmlz_p05aKT_hE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بار هم که شده فریب نخورید!</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/21451" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شما ولی قبول نکنید</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21450" target="_blank">📅 11:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21449">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قالیباف:   آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21449" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قالیباف:
آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21448" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بفرمایید ؛  پست جدید ترامپ تو تروث:   «صبحِ شکوه: آیا ترامپ تو جنگ با ایران میره سراغ مدل کامل “شرمن”؟»</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21447" target="_blank">📅 09:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چون نمی خواهم به وحشت افکنی متهم بشوم، فقط به شما توصیه می کنم این قسمت را درنظر داشته باشید و خود بیاندیشید که در «شرایط کنونی» که کشور تحت محاصره است و چپ و راست اتهامات تروریسم و .... به ما می بندند و همسایگان عرب نیز از حملات موشکی و پهپادی و حوثی ها و…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21446" target="_blank">📅 09:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21445" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ4towgyojoOieMuZ5W6xTPxdq0bHaZ6XNj_7HXMPS8jRe0VzBKEf6kDttHGprlAcCC4HQojcOeo1brL51kSff4fnMKBoCbFhrM8h4dMXJJGM3X4ewYdTjU-ZkddDTf9lx4ghlFshEzM6006p80u6LJiMzKTU-L6TlkKQyTNAFn8GjVzv6OfwWhapAtemCBdd_bJtD5I0MZog_MCL8_9jJh9cgqztZF5i2xchk9GXIm2E7Crcs2Qm6PHTU5Uu248eDOMrLp-ibcTTJUSVjdpSz5joT9wT3ZD-g_0C8UGSLyb__4Gxc_f7QbM-uyCKAQwzbEkBNd6iPrlM3OjsFCX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21444" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
  <div class="tg-doc-extra">172.4 KB</div>
</div>
<a href="https://t.me/SBoxxx/21443" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این فیلم از این ماده چپول مزدور را ببینید تا بعدا بگویم چه توطئه ای در کار است</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21443" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21442" target="_blank">📅 08:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/21441" target="_blank">📅 08:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21440">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد
من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.
اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21440" target="_blank">📅 08:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">— وزیر دفاع بریتانیا:
«حکومت ایران نیت‌های خصمانه دارد و تهدیدی برای کشور ما و متحدان ما محسوب می‌شود.
تحقیقات در مورد پایگاه هوایی RAF Fairford ادامه دارد و چندین سرنخ در حال پیگیری است و این موضوع بسیار جدی است.
ما پس از رسیدن به نتیجه‌گیری قطعی در مورد RAF Fairford، به یک پاسخ مناسب فکر خواهیم کرد».</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21439" target="_blank">📅 00:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21438">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👨‍💻
کارشناس صداوسیما:
چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است
چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SBoxxx/21438" target="_blank">📅 23:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">1-USA 2-PRC 3-N/A 4-IRI</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/21437" target="_blank">📅 19:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">1-USA
2-PRC
3-N/A
4-IRI</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21436" target="_blank">📅 19:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21435">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان  : «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21435" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21434">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان
: «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/21434" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21433">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادعای بِسنت درباره ایران:
برای اولین بار در تاریخ، از زمانی که شروع به استخراج نفت کردند، این هفته هیچ نفت روی آب نخواهند داشت. آنها هیچ درآمدی نخواهند داشت.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21433" target="_blank">📅 18:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حملات سنگین حوثی ها به تاسیسات نفتی آرامکو در عربستان</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SBoxxx/21432" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">— پلیس بریتانیا دو شهروند ایرانی به نام‌های رحمان صالحی، ۳۵ ساله، و سلام احمدیان، ۳۶ ساله را دستگیر کرده است که متهم به توطئه برای هدف قرار دادن جامعه یهودی در منطقه منچستر پیش از یوم کیپور هستند.
این دو نفر به «آماده‌سازی برای ارتکاب عمل تروریستی یا کمک به دیگری در ارتکاب عمل تروریستی» در منچستر، در تاریخ ۲۰ سپتامبر یا قبل از آن، متهم شده‌اند.</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SBoxxx/21431" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltte5lDmYJo16fPieymZMQB8N6aNVmwxX9wbAOul-emsBjXrjck_HraMWMmnBSGDVTcJHEp8jJrHjaCWh77GhFq6nmQP2Faax3cu3dzN6is-4c5jecogJQqR63iC5gMcR6uo4Vyf5JCCOyIv4OMx_VnYZSRMb0PA_dICznwDBmem09LMB3WndfwQMBkbS1nlZNOmYX54dHbIGUx2FcvT6c2VYXl-fp0Lpmcam0UKNTjb0Tks_bZPZMuVXBasRbQPVt5KSRqhVf0KAZh5zTwb-dI-dEiNZOUxpBZ0cTzZqC6e-RnHF9T0-GitZsudRIirN06my9WexhytWBXag9Q4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SBoxxx/21430" target="_blank">📅 02:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ادعای جدید ترامپ:  یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود  به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.  ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21429" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادعای جدید ترامپ:
یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود
به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.
ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد و این "کارخانه‌های مواد مخدر و هسته‌ای" به‌شدت هدف قرار گرفتند.
بر اساس گزارش رسانه‌های آمریکا این نخستین بار است که ترامپ به طور مستقیم از "کارخانه‌های مواد مخدر" در ایران به‌عنوان یکی از اهداف حملات هوایی آمریکا نام می‌برد.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SBoxxx/21428" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«چرا جنگ می شود و چگونه؟!»</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نشست لایو لغو شد.  در یک پادکست مفصل، خواهم کوشید اوضاع را از دید خودم بررسی کنم.</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/SBoxxx/21427" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SBoxxx/21424" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/21423" target="_blank">📅 15:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21422" target="_blank">📅 15:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=Py-uyqMyVGnfX0DCITrSfiV3eBGJGgUbOZ_1uQoxAuPLgr7Li-o6nga-lIHK8O5FEtcXJ0hHKzlDCeQ3tptOZFgexHmfpe5MCigQluyx0wOUcb-JwauFLUrxBF1qVGXdi3rIaJj6b-isZXNtfAMFwKoxJuFJRx0YIpDodQNgbdSfCcDKHboSwA8GLinXdoCnFTtilIuNbPKkL6yhMZ7JzrgiOoxlPS-6vJCwY7H3kIr5ANYBwB0l5LVF8bmiwqIIvjvHFD-z94U4TcpqmGgMFni8HmMMjrxl3TSx32BaLEVPX21wihX19iV-VpiIM_R0hMmn_mFIacMEJauLQpYcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=Py-uyqMyVGnfX0DCITrSfiV3eBGJGgUbOZ_1uQoxAuPLgr7Li-o6nga-lIHK8O5FEtcXJ0hHKzlDCeQ3tptOZFgexHmfpe5MCigQluyx0wOUcb-JwauFLUrxBF1qVGXdi3rIaJj6b-isZXNtfAMFwKoxJuFJRx0YIpDodQNgbdSfCcDKHboSwA8GLinXdoCnFTtilIuNbPKkL6yhMZ7JzrgiOoxlPS-6vJCwY7H3kIr5ANYBwB0l5LVF8bmiwqIIvjvHFD-z94U4TcpqmGgMFni8HmMMjrxl3TSx32BaLEVPX21wihX19iV-VpiIM_R0hMmn_mFIacMEJauLQpYcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/21421" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21420" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واشنگتن پست:
وزارت جنگ آمریکا برای اعزام 20 هزار نیروی نظامی دیگر ارتش آمریکا به خاورمیانه آماده می‌شود.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21419" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صداوسیما:
درگیری مسلحانه سپاه با تروریست‌ها در راسک
برخی منابع از درگیری مسلحانه میان نیروهای امنیتی و عناصر گروهک تروریستی در یکی از روستاهای شهرستان راسک در جنوب سیستان‌ و بلوچستان خبر دادند.
نیروهای امنیتی در حال پاکسازی منطقه و بررسی اوضاع هستند.
تاکنون جزئیات بیشتری درباره وضعیت عناصر تروریستی منتشر نشده است.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21418" target="_blank">📅 12:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_NfWZuNysEehmb8pgfeENJvYGCLpDizGyzHU75LEa-cigL55eY7jAK2D1gyGOAuD1x4gbSvsQ_WpO9R1Cpe-U4exuka9D-x_-baMTS8ucRnhSF8ZV_BKTgaij0bKm0G7Td_PaqZITz93LjdnX0dFNOj-9i4RiQXVdd11k0wZFoZycJXTmqZzxZ775BCLSCQaxXNrLHDUxFOSMUMs7U8RJ_KLCTy7iHcBPjefm-a0dOp5dcwYqGxWXkXhCDkMI9BHN3VZrMMPBht8nW4rabmXjUIyzen2AVvkByRif41O22M2SahA1tQSRwuHuTALv6XsTihKPXB4hiOqjvrDkM9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/21417" target="_blank">📅 11:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpMEW4UlHOQs1Mjub6uUPSqR9sXZ5eI627z_XmrqqGa9FJBrwrrPcfnukaF9ayH5bI-gUYTfGf-l7aPXn9t5pOeouZL3llLjwULyJJawLGyFlM0TPdx3IiecOycUKr7zmxSQCJkfclWB6a6QPbeKD_IEoHP6t68_7VVeI7G1kFJ0pqvGy18SddEP3w5MPjP3mUUHg_eKE0MS1nFwQqlAQRw9q7eEqaJItJ-byY4D6-Y9C4BKrxXdzV03cjds2JQqe4c2OW9zENUNA5Da_I_7psQRs-M8yg00k1fcYHI00tG90r-UcGh0ep7JCFQE55rhLbFsq7W64I9Lb9RqertoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC هم تغییر خاصی نسبت به پریروز و دیروز نداشته است چون عملاً قیمت همانجایی است که دیروز بوده</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21416" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcph5P-9gB4ZyDcXnOKAGBveykOdccmi3tRVK1nqLI-KWmVtryz3txarLhnz3FFqfN7yS8zhH9N1zYTuJhyqWXudC-C4NGQLmYdWPJkgB7Z5rIa-dOCK4NHuMQBjIZR8p92gOnImZPIDbAivgfceha9eg9zkb9Ov-oFoR9SwljL2HPcW4M4WAGa7cXx2YlTuEej_KNYai0IDUBIoTE7QUqREMidH3HiEahOxQwaGRUS57R7pSH6aHMlS9mWL5udTBrpKE4bfOcBhY02ZRTN6CPo2xK13o4rfL2gE4tPZzQUODMNXUwdtykt2TPRqFaXO-srzEiEjth-LiUNsipQeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسط به بالا قرار دارد.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21415" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اگر دوباره به پایین برگشت، تنها روی محدوده دوم ۴۱۴۸ ورود مجاز است.</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21414" target="_blank">📅 09:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SBoxxx/21413" target="_blank">📅 00:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/21412" target="_blank">📅 00:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51530cf576.mp4?token=c1y1UJpJHldYlD9ZRJvKgMZsZ4FAs5Mdf0a8Qq1ttSBuNp7GHJN01t17hGjNKzBXtEm77Y-lI7UqmMM4KdUyqbt6yks-7PphWd3LKnW59wyjjA6q-RuA85G3QHG8bdT2GWpMjQxMIvW_1MVRgoA5COwnXzn2E-jThZUHJUXw62Bo-h4TLOgtTdtd5D04v6x4hKV8mw8cSmc9v9-sUioB7gz55kfbPQpprVf9N7bKIj8ISvfpWXWdDaIhKW8ktrK2vEmZeq2bWhTi-YlaagGGXbfDg8n7MCe8Br8gps0tIdlyeoteS21wt5hKtlAhC-Umlxamknt-1SmEMJKULgD0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51530cf576.mp4?token=c1y1UJpJHldYlD9ZRJvKgMZsZ4FAs5Mdf0a8Qq1ttSBuNp7GHJN01t17hGjNKzBXtEm77Y-lI7UqmMM4KdUyqbt6yks-7PphWd3LKnW59wyjjA6q-RuA85G3QHG8bdT2GWpMjQxMIvW_1MVRgoA5COwnXzn2E-jThZUHJUXw62Bo-h4TLOgtTdtd5D04v6x4hKV8mw8cSmc9v9-sUioB7gz55kfbPQpprVf9N7bKIj8ISvfpWXWdDaIhKW8ktrK2vEmZeq2bWhTi-YlaagGGXbfDg8n7MCe8Br8gps0tIdlyeoteS21wt5hKtlAhC-Umlxamknt-1SmEMJKULgD0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SBoxxx/21411" target="_blank">📅 00:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارشگر:
«آیا ایران در حادثه پایگاه هوایی فرفورد دخالت داشت؟»
ترامپ:
«به نظر می‌رسد که بله.»</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21410" target="_blank">📅 00:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای وزیر خزانه‌داری آمریکا:
جمهوری اسلامی در یکماه گذشته حتی یک قطره نفت هم نفروخته است!</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21409" target="_blank">📅 23:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هدف قرار گرفتن شرکت آرامکو در شهر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/21408" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقام ایرانی:
ادعاهای بلومبرگ در مورد پیشنهاد هسته‌ای ارائه شده توسط ایران به طرف آمریکایی در جریان گفتگوها با میانجی‌گران نادرست است</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21407" target="_blank">📅 23:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سوپرنفتکش ۲.۵ میلیون بشکه‌ای در تنگه هرمز هدف قرار گرفت</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/21406" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
معاون وزیر ارتباطات
:
اگر استفاده از استارلینک گسترده شود ، در مواقع بحران مجبوریم تمام برق را قطع کنیم تا مودم های استارلینک هم از کار بیفتد؛ چراکه حکمرانی اینترنت را نخواهیم داشت</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SBoxxx/21405" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مقامات ایالات متحده به الجزیره:  ناو هواپیمابر یو‌اس‌اس تئودور روزولت به همراه گروه ضربتی خود، پایگاه سن دیگو را ترک کرده و به سمت خاورمیانه در حرکت است.  تا پایان نوامبر، ۳ ناو هواپیمابر و ۲ گروه ویژه حملات آبی-خاکی در اطراف ایران مستقر خواهند شد.</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/21404" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:  به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SBoxxx/21403" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:
به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SBoxxx/21402" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SBoxxx/21401" target="_blank">📅 17:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تا نزدیکی محدوده دوم ورود آمد.  پوزیشن اول را اینجا با حدود ۲۰۰ پیپ سود تسویه کنید</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SBoxxx/21400" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#FairValueCurve  نمایه FVC تغییر خاصی نسبت به دیروز نداشته.  محدوده های مناسب خرید:  4165 4148  تارگت ها:  4187 4213</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SBoxxx/21399" target="_blank">📅 15:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqqUmw_tLL8-71PsrX9xTlEGVLaamJUpjZxZHLStJByJeOwJrf-C5gEJZZU8EacmDBG4GaTK529XMl6pMDRCl_CDvEBwh6uI3pxUBUW-FLAOXGniCQu6ifEnu-rphEWl9XxBxIpFZw_bOxDeRU2KlNyUUBOMbhVbvXNcxVCJ2OOtM6c8GJ-3P5EaWngxYlScNTEm2vIg-AflcRoI-H2FPSC03fIeh2HCj9P9n3gRYwJf-wbUoZCu_hJ0YNQyWnF8ERwGcKUhe9oJajxBePv2YF8lsgQD5aWM0Hb2sOZ_R145cKeVg3TK_3khkiaPJ7uZ6_or879THpqAJTjweUXa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیآمدهای نظامی امپراتوری ایلان ماسک</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21398" target="_blank">📅 14:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21397">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز:
مقامات دولت سوریه و نمایندگان حزب‌الله در سپتامبر به‌صورت مخفیانه در ترکیه دیدار کردند که نخستین گفت‌وگوی حضوری شناخته‌شده میان این دو طرف پس از سقوط بشار اسد محسوب می‌شود.
این مذاکرات که با تسهیل‌گری نهادهای امنیتی و اطلاعاتی ترکیه انجام شد، بر کاهش تنش‌ها میان دمشق و حزب‌الله متمرکز بود.
سوریه به حزب‌الله اطمینان داد که برای تسلیح‌زدایی از این گروه، مداخله نظامی در لبنان نخواهد داشت، در حالی‌که از حزب‌الله خواست قاچاق سلاح از مرزها را متوقف کند و سلول‌های باقی‌مانده خود را در سوریه منحل سازد.
حزب‌الله تعهد کرد که در امور سوریه دخالت نکند، اما پاسخی مستقیم به این درخواست‌ها ارائه نداد. هیچ توافق نهایی‌ای حاصل نشد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21397" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21396">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9826.PNG</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/SBoxxx/21396" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21396" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21395" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_445
🗓
October 1, 2026
✔️
تحلیل گزارش دیروز شاخص خرجکرد شخصی مصرف کننده
✔️
ارزیابی وضعیت تنشهای مربوط به ایران
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21395" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">درگیری مسلحانه نیروهای انتظامی با شبه نظامیان مسلح ناشناس که از صبح امروز در زاهدان شروع شده طبق اخبار تاکنون ادامه دارد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21394" target="_blank">📅 10:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21393" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYQE1yj9NRnnL1fsIwlnTL1x8zutfknmZvXWI5FkUo2xmErfnbFx69Huj0jBzV_DunQChJo8ARlpO-I1Km7ZewEuu5S_p-DqKgRY-96lGEiL467SXxHs5MmIflr02eTUqUw5KDrI-iobWazetJDaJWbCKRrK-IYjlzceSJYfLfcuWabgJnSA3TlpK4NjYHoBzD8qtLiTElar80M8Rcv3yPEdPyjF_VNKZDX8rRfpRJEVHpCOi8kKdP6sc2vRr8Icydh-rnElPO8cnd7HEDk9ykRHPg9O_BppBMEcX1HNeJQ1LahLxlp8WPH0xSJ-SzrL_JK2CzySl-GZe13KZ0rfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC تغییر خاصی نسبت به دیروز نداشته.
محدوده های مناسب خرید:
4165
4148
تارگت ها:
4187
4213</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21392" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOcuBWNzpuBINylTSiF4eKJm2WYf1HX1ECtJRT6Up-90fD6MzgSQM78hrdDm6okRMnO9NtFdK45oPSvsYnzij3sVpTlwtFT3iCPgErwlJYptSkLrcwWmQ4Sh96CPPGIwSeHwlARl01xa842-kE9k9-UWMPv4DhwA97bKwGY-3hEgrHbl1zemqD34pFBsTl2jm65rmwSRfzDKd0ZCGb45p0vq-hXPUdaCUs6xor1tUxPOpyUp9qmXteBFQ8rtcKI7lrzi46BFQh3vay2QFc9BHhgjZx1HnygbHQOPBb261_NQv8ufrrUtgwfmO2J4xGCO32p8iJOKItkhgXg_65I21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در اصلاحی ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21391" target="_blank">📅 10:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اکسیوس:     روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21390" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اکسیوس:
روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21389" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای عجیب هگست وزیر دفاع آمریکا:
امروز دستور دادم ساختار عقیدتی سیاسی در ارتش آمریکا تشکیل شود!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21388" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
